# Portfolio maintenance

Follow `README.md` for the canonical authoring, preview, checking and publishing workflow.

- Preserve the existing Jekyll / GitHub Pages framework and warm editorial design. Do not introduce a frontend framework or dependencies without approval.
- The repository's `index.html` is the sole homepage source. Do not create v1/v2 copies or edit an unrelated preview directory as the authoritative version.
- Keep all projects on the same content schema: Goal, Contribution, optional figure, Outcome, Lessons, Tools, Resources. Distinguish motivation, personal contribution, demonstrated results and limitations.
- Preserve stable project slugs, accessible dialog behavior, timeline return position, URL/history handling and automatically generated project counts. Do not hand-number figures or breadcrumbs.
- Use only user-approved public facts/resources. Do not commit private notes, internal logs, screenshots containing confidential data, or raw source resumes without explicit approval.
- Keep both public resume paths identical when the user requests a resume update. Do not replace them merely because another local PDF is newer.
- Run `python3 scripts/check_site.py` and `node tests/project_index.cjs`, then browser checks from README. When the isolated build environment is available, also run `sh scripts/jekyll.sh build --trace`, `sh scripts/jekyll.sh doctor`, and `python3 tests/check_build.py`. Report full Jekyll build limitations separately.
- Do not run legacy `__deploy.sh`. Do not delete legacy routes/assets casually. Do not commit, push or publish without explicit user approval.
