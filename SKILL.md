---
name: odoo-knowledge-writing-doc
description: Write or update clear, task-based documentation for custom Odoo modules from source code and available UI evidence. Apply Apple and Adobe writing principles and plan, capture, and annotate accessible screenshots for user and administrator guides.
---

# Document a custom Odoo module

Turn a module path, uploaded module archive, or repository into a simple guide that explains what people can do, how to do it, and what happens next. Default to business users; include administrator setup only when needed. Add developer reference only when requested.

## Portability and invocation

Keep this folder intact when adding it to a skill-capable ChatGPT or Claude environment. The entry point is this `SKILL.md`; supporting files use relative paths. No vendor-specific tools, package dependencies, or network access are required. Installation and available file/browser tools depend on the host. If the host only accepts instructions, supply this file and the referenced resources together as project knowledge.

Example request: “Use odoo-knowledge-writing-doc to document /path/to/custom_addons/my_module for sales users. Write a Markdown guide with annotated screenshots where available.”

For an illustrative POS request and sample output, see [POS example](references/pos-example.md). Read it when explaining how to use this skill; its fictional behavior is not evidence about a real module.

## Establish scope and evidence

1. Read applicable repository instructions and existing documentation. Inspect the specified module and necessary dependencies; avoid unrelated modules.
2. Identify the technical module name, business purpose, Odoo version evidence, edition requirements, and intended roles. A manifest version alone does not prove compatibility. If the audience is unspecified, use business users and state that assumption.
3. Trace actual workflows through `__manifest__.py`, Python models and wizards, XML views/actions/menus, security groups and access CSVs, record rules, data files, reports, controllers, and relevant JS/OWL components. Read tests for useful scenarios. Treat comments and old guides as leads to verify.
4. Record the entry point, visible labels, prerequisites, required inputs, actions, resulting state, permissions, and meaningful exceptions for each documented task. Check inherited views and actions when their parent definitions are available. Distinguish standard Odoo behavior from this module's changes.
5. Use a running UI when available to check navigation, labels, role visibility, and results. Source-only evidence supports a draft, not a claim that the procedure was tested. Do not install a module, change access rights, send email, post accounting entries, or run business transactions merely to document it without appropriate authorization.

Maintain a compact author-only evidence table: claim or task, source path and symbol/XML ID, live verification if any, and unresolved question. Include file line numbers when practical. Code-level access checks, record rules, company context, and view visibility can differ; a visible button does not establish permission.

Do useful work with the available evidence. Ask only for information that materially blocks accuracy. If source or UI access is missing, describe the gap and request the relevant files or access. Never invent menu paths, defaults, roles, error messages, screenshot content, or successful outcomes.

## Write the guide

Read [Writing conventions](references/writing-conventions.md). Use [the guide template](assets/guide-template.md) as a starting structure, omitting sections that add no value. Replace every placeholder before delivery.

- Open with the module's purpose in business terms and the tasks it supports.
- Put access and setup prerequisites before the first affected task. Explain role names in plain language; keep technical identifiers in author notes or a requested developer appendix.
- Organize around goals such as “Approve a request,” rather than models, Python classes, or a tour of every screen.
- For each task, give the starting location, necessary inputs, ordered actions, and a concrete success check. Explain fields only when users need them to decide what to enter.
- Describe consequential effects before the action: notifications, external requests, stock movements, financial postings, and irreversible changes, when evidenced by the module.
- Distinguish manual actions from automation. Describe triggers, timing, and prerequisites only when supported. A configured scheduled interval does not guarantee an exact completion time.
- Troubleshooting should connect an observable symptom to an evidenced cause and a safe next step. Label unverified hypotheses in author notes instead of publishing them as facts.

Default to Markdown and relative image paths unless the user or repository specifies another format. Follow existing documentation placement; otherwise use `<module>/docs/user-guide.md` and `<module>/docs/images/`. If the module is read-only or uploaded, create a separate deliverable folder. Do not overwrite unrelated documentation.

## Screenshots

Read [Screenshot and annotation workflow](references/screenshots.md) before planning or producing figures. Capture real UI when tools and an appropriate environment are available. If capture is unavailable, deliver the useful text guide with clearly marked capture requests in author notes; do not embed broken image links or pretend placeholders are screenshots.

## Review and deliver

- Trace every described feature, permission, and result back to code or observed behavior. Resolve conflicts or state the uncertainty.
- Check that a reader in the stated role can follow each task without developer knowledge. If not exercised live, mark the verification limit in author notes.
- Check terminology, navigation, image links, figure references, captions, alt text, and redaction. Inspect annotated images at their final display size. For PDF or Word output, render and inspect the final pages when tools permit.
- Remove template markers and speculative claims. Preserve useful uncertainty in a separate author-notes file, not mixed into confirmed instructions.
- Deliver the guide and actual image assets, plus concise author notes containing version/source context, the evidence table, verification limits, and any capture requests. Report what was verified and what remains unverified.
