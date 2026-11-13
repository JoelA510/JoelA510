# AGENTS.md

This repository publishes the GitHub profile README and the images in `assets/`.
It is not the source repository for the featured applications.

## Editing the profile

- Read [README.md](README.md) and inspect the relevant asset before editing.
- Keep career claims factual. Do not invent credentials, metrics, work history,
  deployment status, or verification results. Check the relevant project's current
  source before updating its technical claims; ask when a personal fact is missing.
- Do not copy private career documents or unpublished writing into the profile.
- The SVGs in `assets/` are generated: edit the text in `assets/build.py` and run
  `python3 assets/build.py`, which rewrites every light and dark variant. Never edit an
  SVG by hand. Counts that go stale (tests, versions) belong in README text, not a graphic.
- Preserve useful image alt text and the existing links to source repositories.
- The featured projects were built by directing AI agents under written rules; keep
  that stated wherever a project is described.
- Change the profile only; work on a linked application belongs in its own repo.

## Verification and reporting

There is no package manager or test suite. After a graphics change, run
`python3 assets/build.py` and confirm `git status` shows only the SVGs you expected.
Check changed links, referenced asset paths, and image rendering in both themes.
Describe those checks honestly rather than reporting tests that do not exist.

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
