# AGENTS.md

This repository publishes the GitHub profile README and the images in `assets/`.
It is not the source repository for the featured applications.

## Editing the profile

- Read [README.md](README.md) and inspect the relevant asset before editing.
- Keep career claims factual. Do not invent credentials, metrics, work history,
  deployment status, or verification results. Check the relevant project's current
  source before updating its technical claims; ask when a personal fact is missing.
- Do not copy private career documents or unpublished writing into the profile.
- Keep light and dark asset variants aligned when a change affects both. Preserve
  useful image alt text and the existing links to source repositories.
- Change the profile only; work on a linked application belongs in its own repo.

## Verification and reporting

There is no package manager or application build in this repository. Check changed
Markdown/HTML links, referenced asset paths, and image rendering. Describe those
checks honestly rather than reporting application tests that were not run.

Read [SECURITY.md](SECURITY.md) before sharing a suspected vulnerability. Public
issues, PRs (including drafts), logs, and artifacts are not private channels.
Use synthetic evidence and coordinate disclosure with the maintainer.

Draft-only requests stay on a branch and in draft PRs. Do not merge or publish
them without the owner's explicit authorization.

## Review rules

Use these rules when a review is requested or required; they do not add review rounds.

- Review the diff and affected references for incorrect claims, broken links or assets,
  privacy exposure, data loss, and changes outside the PR's stated purpose. Leave formatting
  and lint findings to automated checks.
- Order findings by severity. Each gives severity, `path:line`, the concrete trigger and
  consequence, and a fix. Mark it confirmed (verified against the source) or plausible
  (state the missing evidence); distinguish static review from executed checks.
- Flag new dependencies, network calls, or stored-data shape changes absent from the PR
  description. Disclosure does not replace any required approval.
- Prose-only changes do not require code tests. If no defects are found, say so in one line
  and identify the review scope and unrun checks without implying runtime validation.
- Follow this repository's security-reporting rules for sensitive findings; keep private
  source material out of review comments.
