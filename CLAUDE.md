# name_it_right

MkDocs Material site with naming rules for code entities. Live site: https://stihotvor.github.io/name_it_right/

## Layout
- `docs/common/` - rules for all languages
- `docs/python/` - Python entities
- `docs/databases/` - tables, columns, indexes, constraints, enums
- `mkdocs.yml` - site config and `nav`. Add each new page to `nav`.
- `requirements.txt` - pinned docs tools. Do not install them in the OS. Use a project `.venv`.

## Build
- Preview: `mkdocs serve`
- Check: `mkdocs build --strict`
- Deploy: CI runs `mkdocs gh-deploy --force` on push to `main`. Never deploy by hand.

## Rules
- Follow the page style of `docs/python/functions.md` (good and bad examples).
- Keep front matter `status:` on new pages.
- Work on a branch. Open a PR to `main`. Only `git-agent` pushes.
- Backlog: see `PLAN.md`.
