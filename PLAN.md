# Docs enhancement plan

Merged on 2026-11-06 from the opencode plan `~/.opencode/plan/name-it-right-naming-examples.md` and the repo status check.
The opencode files stay the detailed source: research tables (sections 2-3), page template (4.1), per-step research anchors (7).
Also there: `name-it-right-naming-examples-loop.md` (delivery loop) and `name-it-right-qa-checklist.py` (QA script).

## Goal
Add a large, sourced catalogue of naming examples to the site. The site has strong rules but few worked examples. It has no API or operations guidance and no non-Python languages.

Out of scope: theme or build changes, generated content, analytics, licence changes, translation.

## Status on 2026-11-06
- Repo `Stihotvor/name_it_right`, default branch `main`. No open issues, no open PRs.
- A01 is `Done` (2026-11-06, [PR #5](https://github.com/Stihotvor/name_it_right/pull/5)). The other 31 steps are `Pending`.
- A01 result: 45 sources, 172 verbs, 100 nouns, 34 suffixes, 48 states, 5 links to Python pages.
- The uncommitted copy in `~/PycharmProjects/name_it_right` (branch `docs/01-references-and-glossary`) is now obsolete. The user decides when to remove it.
- CI deploys on push to `main` only. No build check on pull requests.

## Rules for every page
1. Examples outnumber rules. At least 20 identifiers per page, 40 on domain pages.
2. Every rule has a named example.
3. Every bad -> better table has a "why" column.
4. Version-specific claims have a source link.
5. One running example: an e-commerce checkout flow. Domain pages use their own vocabulary.
6. Correct casing per language. No duplication: link to the glossary and pattern pages.
7. Use only the Markdown extensions enabled in `mkdocs.yml`. New pages get `status: new`.

## Definition of Done (each step)
- Pages exist at the listed paths. `mkdocs.yml` nav entry is in the same PR.
- Minimum example count is met. Page template is followed.
- `mkdocs build --strict` passes in the project `.venv`. `git diff --check` is clean.
- PR text names the step ID and the verification commands. PR has no unrelated change.

## Delivery loop (one step = one branch = one PR)
1. Pick the lowest `Pending` step whose dependencies are `Done`.
2. `git-agent` syncs `main` (`git switch main`, `git pull --ff-only`).
3. Create branch `docs/NN-slug`. Implement only that step. Extra work becomes a new step.
4. Verify. Commit as `docs(NN): <short title>`.
5. `git-agent` pushes and opens the PR. The user reviews and merges (squash). The agent never self-merges.
6. After the user confirms the merge, mark the step `Done` here with date and PR URL.
7. Ask the user to compact the chat. Repeat.

## Backlog
Branch numbers follow the opencode plan. Fix the numbering conflicts below before step B01.

| Phase | Step | Branch | Scope |
|---|---|---|---|
| A Foundations | A01 (Done) | `docs/01-references-and-glossary` | Sources (30+) and master glossary |
| | A02 | `docs/03-patterns-index-action-context` | Patterns overview, action-and-context page |
| B Patterns | B01 | `docs/04-patterns-booleans-collections-units-time` | Booleans, collections, units, money, time |
| | B02 | `docs/05-patterns-symmetry-negation` | Symmetry pairs, negation, optionality |
| | B03 | `docs/06-patterns-cookbook` | 60+ bad -> better rows in 10+ categories |
| C Python | C01-C04 | `docs/08` to `docs/11-python-*` | Variables, functions, classes, class methods |
| | C05a, C05b | `docs/12a-...`, `docs/12b-...` | Test naming patterns, advanced test topics |
| D Databases | D01-D04 | `docs/13` to `docs/16-db-*` | Columns, tables, indexes and constraints, warehouse |
| E Languages | E01 | `docs/17-languages-index` | Languages overview, move Python nav, check links |
| | E02-E06 | `docs/18` to `docs/22` | JS/TS, Java/Kotlin, C#/.NET, Go, Rust |
| F Systems | F01-F05 | `docs/23` to `docs/27` | REST, GraphQL and events, errors and config, flags and observability, CLI |
| G Domains | G01-G03 | `docs/28` to `docs/30` | E-commerce, payments/fintech/healthcare, logistics/SaaS/ML |
| H Final | H01 | `docs/31-index-crosslinks` | Home cards, landing cards, cross-links |
| | H02 | `docs/32-editorial-qa` | Consistency pass, link check, QA script |

## Problems found in the opencode plan
- Step B01 and B02 in the backlog overlap in scope. The progress log renumbers them (B01 combined, B02 symmetry, B03 cookbook). Use the progress-log version.
- Branch numbers skip `02` and `07`.
- Dependency rules cite step numbers (26-29, 30, 31) that do not match the branch numbers (G01 is 28, H01 is 31, H02 is 32).
- Review log says "Pending review" while the header says the architect review is complete.
- The loop document lists `git pull --ff-only` as a direct command. Only `git-agent` may run it.

## Open questions
1. Keep the detailed plan in `~/.opencode/plan/` or copy a snapshot into this repo?
2. Are short snippets in each page's own language welcome?
3. Is a per-page `Sources` section plus one global references page enough?
4. Add a PR build check (`mkdocs build --strict`) to CI?
5. What about the remote branch `more-class-methods`? Merge or drop?
