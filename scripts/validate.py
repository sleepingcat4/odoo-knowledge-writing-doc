"""Validate this repository without third-party dependencies."""

from pathlib import Path
import re
import struct
from urllib.parse import unquote, urlsplit
import zlib

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    required = [
        'SKILL.md', 'README.md', 'LICENSE', 'assets/guide-template.md',
        'references/writing-conventions.md', 'references/screenshots.md',
        'references/pos-example.md',
        'references/images/pos-order-note-editor.png',
        'references/images/pos-order-note-saved.png',
    ]
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f'Missing file: {name}')
    skill = ROOT / 'SKILL.md'
    if skill.is_file():
        match = re.match(r'\A---\n(.*?)\n---\n', skill.read_text(), re.S)
        if not match:
            errors.append('SKILL.md: missing YAML frontmatter')
        else:
            fields = dict(re.findall(r'^(name|description):\s*(.+)$', match[1], re.M))
            if fields.get('name') != 'odoo-knowledge-writing-doc':
                errors.append('SKILL.md: unexpected skill name')
            if not fields.get('description', '').strip():
                errors.append('SKILL.md: missing description')
    for path in sorted(ROOT.rglob('*.md')):
        if any(p in {'.git', 'dist'} for p in path.relative_to(ROOT).parts):
            continue
        content = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', content):
            url = urlsplit(target.strip('<>'))
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f'{path.relative_to(ROOT)}: invalid local link {target}')
    for path in sorted((ROOT / 'references').rglob('*.png')):
        try:
            data = path.read_bytes()
            if data[:8] != b'\x89PNG\r\n\x1a\n':
                raise ValueError('invalid signature')
            offset = 8
            types = []
            while offset < len(data):
                length = struct.unpack('>I', data[offset:offset + 4])[0]
                kind = data[offset + 4:offset + 8]
                payload = data[offset + 8:offset + 8 + length]
                crc = struct.unpack('>I', data[offset + 8 + length:offset + 12 + length])[0]
                if zlib.crc32(kind + payload) & 0xffffffff != crc:
                    raise ValueError('CRC mismatch')
                types.append(kind)
                offset += 12 + length
            if not types or types[0] != b'IHDR' or types[-1] != b'IEND':
                raise ValueError('incomplete PNG')
        except (ValueError, struct.error) as exc:
            errors.append(f'{path.relative_to(ROOT)}: {exc}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Validation passed: skill metadata, resources, local links, and PNG integrity.')


if __name__ == '__main__':
    validate()
