# name_it_right

MkDocs Material site with naming rules for code entities. Live site: https://stihotvor.github.io/name_it_right/

## Layout
- `docs/common/` - rules for all languages
- `docs/patterns/` - patterns that hold in every language
- `docs/python/`, `docs/languages/` - Python and other languages
- `docs/databases/` - tables, columns, indexes, constraints, enums
- `docs/systems/` - REST, GraphQL, events, errors, configuration, flags, observability, CLI
- `docs/examples/` - worked vocabularies for seven domains
- `docs/interlinks/README.md` - site map, built from `nav`
- `scripts/check_docs.py` - editorial checks. Run `python3 scripts/check_docs.py` from the repo root. It prints `ok`.
- `mkdocs.yml` - site config and `nav`. Add each new page to `nav`.
- `requirements.txt` - pinned docs tools. Do not install them in the OS. Use a project `.venv`.

## Build
- Preview: `mkdocs serve`
- Check: `mkdocs build --strict` and `python3 scripts/check_docs.py`. CI runs both on pull requests.
- Deploy: CI runs `mkdocs gh-deploy --force` on push to `main`. Never deploy by hand. The deploy job installs unpinned `mkdocs-material`.

## Rules for every page
1. Examples outnumber rules. At least 20 identifiers per page, 40 on domain pages.
2. Every rule has a named example.
3. Every bad -> better table has a "why" column.
4. Version-specific claims have a source link.
5. One running example: an e-commerce checkout flow. Domain pages use their own vocabulary.
6. Correct casing per language. Do not repeat content: link to the glossary and pattern pages.
7. Use only the Markdown extensions enabled in `mkdocs.yml`. Use admonitions (`success`, `tip`, `danger`) and code blocks as in `docs/python/functions.md`.
8. Add `status: new` as front matter to each new page. Most existing pages have no front matter.

## Git
- Work on a branch `docs/NN-slug`. Commit as `docs(NN): <short title>`. Open a PR to `main`.
- `git-agent` (the agent for remote git and `gh` work) pushes and merges. The user reviews and merges unless the user says otherwise.
- The PR text names the checks that were run. The PR has no unrelated change.
- Do not keep a plan or backlog file in the repo.
