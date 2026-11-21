# Screenshot and annotation workflow

These are production conventions for this skill. They extend the writing principles; they are not presented as Apple or Adobe specifications.

## Decide what needs a figure

Use a figure for an unfamiliar entry point, a dense form requiring explanation, a consequential confirmation, or a result users need to recognize. Avoid an image for every click. The written procedure must remain usable without the image.

Create a capture plan before collecting images. For each figure, record its task and step, purpose, exact UI state, role, company context, language, target filename, and whether capture is available. A planned image is not evidence that a screen exists.

## Capture real, safe UI

1. Match the documented Odoo version, module revision, role, company, and relevant configuration. Record unknowns rather than guessing. Use demo or sanitized records, with consistent sample data across a procedure.
2. Close unrelated menus and notifications. Wait for loading to finish. Keep the viewport, theme, browser zoom, and language consistent across a sequence; start with 100% zoom and adjust only for legibility.
3. Capture enough context to identify the page and target. Crop irrelevant browser chrome and empty margins, but retain labels, breadcrumbs, and statuses necessary to understand the action.
4. Prefer PNG for UI text. Keep an original capture and an annotated derivative when useful. Name them by task and state, for example `approve-request-02-before-confirm.png` and `approve-request-02-before-confirm-annotated.png`. Do not commit an original containing sensitive content.
5. Remove personal details, financial information, credentials, tokens, internal URLs, and revealing browser tabs before sharing. Prefer recapture with safe data. If redaction is necessary, use an opaque replacement and export a flattened image; blur or a removable overlay is insufficient. Inspect the exported pixels and metadata.

Do not synthesize a UI screenshot with an image generator, reconstruct an unavailable screen, alter a status or label, or combine incompatible states into apparent evidence. A requested conceptual mockup must be clearly labeled as such and kept separate from captured figures.

## Annotate with restraint

- Use a thin rectangle around the exact control; add an arrow only if its target would otherwise be unclear. Do not obscure labels, values, status indicators, or validation messages.
- Use numbered badges when explaining several targets. Number in reading or action order, restarting for each figure. Explain every badge in adjacent text. Figure badge numbers are local to the image; explicitly identify their corresponding procedure steps when needed.
- Aim for one to three callouts per image. Split a crowded figure into focused views instead of shrinking text.
- Use one accent color with a light or dark outline as needed for contrast. Pair color with shapes, numbers, or text; meaning must survive grayscale viewing.
- At the final displayed size, start with 2–3 px outlines, 24–32 px badges, and callout text at least 14–16 px. Scale these together as needed. These are starting values, not accessibility guarantees; inspect the actual output for readable UI text and clear contrast.
- Put longer explanations below the image. Keep annotation wording consistent with the guide's UI labels.

Use an available image editor or annotation tool. If none is available, preserve the real capture and provide exact annotation instructions in author notes. Do not claim an unannotated capture has callouts.

## Place figures accessibly

Place an image immediately after the relevant step or paragraph. Introduce it by figure number when helpful. Add a sentence-case caption that states its purpose, and alt text that conveys the meaningful visual information rather than repeating the filename.

Illustrative Markdown, to use only after the referenced image exists:

```markdown
![Request form with callout 1 around the Approver field and callout 2 around Confirm.](images/approve-request-02-before-confirm-annotated.png)

*Figure 1. Review the approver before confirming the request.*

Callout 1 identifies **Approver**. Callout 2 identifies **Confirm**.
```

The example labels are illustrative, not Odoo facts. In final documentation, provide all essential actions in text, including the expected result. Do not rely on alt text alone for the full procedure. For other output formats, use their actual alt-text and caption features.

## When screenshots are unavailable

Do not insert a Markdown image pointing to a nonexistent file. Add a capture request to author notes instead:

| Figure | Task and step | Required state and role | Capture/annotation instructions | Proposed filename | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Verified task title, step number | Verified screen; role; context | Capture target; describe callouts after UI confirmation | Descriptive PNG filename | Capture needed |

Replace illustrative cells with source-supported details. Mark UI details that still need confirmation. If an essential instruction cannot be established without a screenshot or live observation, identify that specific gap.

## Final visual check

Open every delivered figure at its intended output width. Check that its state matches the instruction, the target is visible, callouts and captions agree, sensitive data is absent, and relative links resolve. Recheck the exported document because scaling or page breaks can make an otherwise good image unreadable.
