# name_it_right

MkDocs Material site with naming rules for code entities. Live site: https://stihotvor.github.io/name_it_right/

## Layout
- `docs/common/` - rules for all languages
- `docs/python/` - Python entities
- `docs/databases/` - tables, columns, indexes, constraints, enums
- `mkdocs.yml` - site config and `nav`. Add each new page to `nav`.
- `requirements.txt` - pinned docs tools. Do not install them in the OS. Use a project `.venv`. CI does not use these pins (it runs an unpinned `pip install mkdocs-material`).

## Build
- Preview: `mkdocs serve`
- Check: `mkdocs build --strict`. Run it locally. CI does not run it on pull requests.
- Deploy: CI runs `mkdocs gh-deploy --force` on push to `main`. Never deploy by hand.

## Rules
- Follow the page layout in `PLAN.md` ("Rules for every page"). Existing pages such as `docs/python/functions.md` use admonitions (`success`, `tip`, `danger`) and code blocks.
- Add `status: new` as front matter to each new page. Most existing pages have no front matter.
- Work on a branch. Open a PR to `main`.
- `git-agent` (the agent for remote git and `gh` work) pushes and merges. For the merge rule, see "Delivery loop" in `PLAN.md`.
- Backlog: see `PLAN.md`.
