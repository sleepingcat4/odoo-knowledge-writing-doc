"""Build a portable skill ZIP containing only intended distribution files."""

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

from validate import ROOT, validate


def main():
    validate()
    destination = ROOT / 'dist' / 'odoo-knowledge-writing-doc.zip'
    destination.parent.mkdir(exist_ok=True)
    files = [ROOT / name for name in ('SKILL.md', 'README.md', 'LICENSE')]
    for directory in ('assets', 'references', 'scripts'):
        files.extend(p for p in (ROOT / directory).rglob('*')
                     if p.is_file() and p.suffix in {'.md', '.png', '.py'})
    with ZipFile(destination, 'w', ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(path, Path(ROOT.name) / path.relative_to(ROOT))
    print(f'Built {destination.relative_to(ROOT)} ({len(files)} files).')


if __name__ == '__main__':
    main()
