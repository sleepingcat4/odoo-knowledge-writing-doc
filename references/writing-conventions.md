# Writing conventions

These are a practical synthesis, not a reproduction of either source or a claim of official endorsement. The screenshot production specifications in the companion reference are local conventions.

## Source-derived principles

From the [Apple Style Guide](https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf), June 2026 edition: use numbered, complete sentences for sequential instructions; prefer present tense for immediate results; avoid “please” in procedures. Include figures when they clarify something text alone does not convey, and refer to figures consistently. Relevant entries: “lists (numbered),” “future tense,” “please,” “figures,” and “figure references.”

From [Adobe Spectrum: Grammar and mechanics](https://spectrum.adobe.com/page/grammar-and-mechanics/): prefer active voice, address readers as “you,” use sentence case, simple tenses, and familiar contractions when appropriate. Use a serial comma. Write “and” rather than an ampersand unless reproducing an actual name. Keep language inclusive. Relevant sections: Active and passive voice, Contractions, Verb tenses, Capitalization, Pronouns, and Punctuation.

## House decisions for Odoo guides

When the sources differ, apply explicit user requirements first, then exact product labels, then these conventions. Use Apple for procedural structure and Adobe for general sentence mechanics; do not import either company's product terminology into Odoo.

- Default to U.S. English; follow the requested language and locale when specified.
- Preserve the actual capitalization and wording of UI labels, even when they use title case. Use sentence case for authored headings.
- Use bold for UI labels, such as **Confirm**; code formatting for identifiers, commands, and literal technical values.
- Use `>` between verified navigation levels: **Requests > My requests**. Do not construct a menu path from model names or XML IDs.
- Use “select” for choosing an item, “enter” for field input, and “open” for a record or page. Name the control; avoid “click here,” “above,” or color-only directions.
- Keep one meaningful action per numbered step; group closely related field inputs when that improves readability. Put explanations beside the relevant action.
- Define necessary business terms on first use. Avoid implementation terms such as “many2one” in a business guide.
- Use a field table only when several fields need explanation. Describe their purpose, allowed values, and conditions rather than restating their labels.
- Place warnings before consequential actions. Use notes for useful exceptions, not as storage for unrelated detail.

## Illustrative rewrite

Weak: “The user must simply click the button to execute the validation functionality.”

Better: “Select **Validate**. The request moves to **Approved**.”

This example is invented to illustrate wording. Use it only if the inspected module has that label and transition. Replace it with the module's verified behavior.

If the sources cannot be accessed, use this bundled synthesis and disclose that no fresh source review was performed. Do not claim to have checked later revisions.
