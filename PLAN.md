# Docs enhancement plan

Merged on 2026-11-06 from the opencode plan `~/.opencode/plan/name-it-right-naming-examples.md` and the repo status check.
The opencode files stay the detailed source: research tables (sections 2-3), page template (4.1), per-step research anchors (7).
Also there: `name-it-right-naming-examples-loop.md` (delivery loop) and `name-it-right-qa-checklist.py` (QA script).
These files are local to the author's machine. A fresh clone cannot reach them (see open question 1).

## Goal
Add a large, sourced catalogue of naming examples to the site. The site has strong rules but few worked examples. It has no API or operations guidance and no non-Python languages.

Out of scope: theme or build changes, generated content, analytics, licence changes, translation.

## Status on 2026-11-07
- Repo `Stihotvor/name_it_right`, default branch `main`. No open issues. Step PRs were merged one at a time.
- Done: A01 (2026-11-06, [PR #5](https://github.com/Stihotvor/name_it_right/pull/5)), A02 (2026-11-06, [PR #7](https://github.com/Stihotvor/name_it_right/pull/7)), B01 (2026-11-06, [PR #8](https://github.com/Stihotvor/name_it_right/pull/8)), B02 (2026-11-06, [PR #9](https://github.com/Stihotvor/name_it_right/pull/9)), B03 (2026-11-06, [PR #10](https://github.com/Stihotvor/name_it_right/pull/10)), C01 (2026-11-06, [PR #11](https://github.com/Stihotvor/name_it_right/pull/11)), C02 (2026-11-06, [PR #12](https://github.com/Stihotvor/name_it_right/pull/12)), C03 (2026-11-06, [PR #13](https://github.com/Stihotvor/name_it_right/pull/13)), C04 (2026-11-06, [PR #14](https://github.com/Stihotvor/name_it_right/pull/14)), C05a (2026-11-06, [PR #15](https://github.com/Stihotvor/name_it_right/pull/15)), C05b (2026-11-06, [PR #16](https://github.com/Stihotvor/name_it_right/pull/16)), D01 (2026-11-06, [PR #17](https://github.com/Stihotvor/name_it_right/pull/17)), D02 (2026-11-06, [PR #18](https://github.com/Stihotvor/name_it_right/pull/18)), D03 (2026-11-06, [PR #19](https://github.com/Stihotvor/name_it_right/pull/19)), D04 (2026-11-07, [PR #20](https://github.com/Stihotvor/name_it_right/pull/20)), E01 (2026-11-07, [PR #21](https://github.com/Stihotvor/name_it_right/pull/21)), E02 (2026-11-07, [PR #22](https://github.com/Stihotvor/name_it_right/pull/22)), E03 (2026-11-07, [PR #23](https://github.com/Stihotvor/name_it_right/pull/23)), E04 (2026-11-07, [PR #24](https://github.com/Stihotvor/name_it_right/pull/24)), E05 (2026-11-07, [PR #25](https://github.com/Stihotvor/name_it_right/pull/25)), E06 (2026-11-07, [PR #26](https://github.com/Stihotvor/name_it_right/pull/26)), F01 (2026-11-07, [PR #27](https://github.com/Stihotvor/name_it_right/pull/27)), F02 (2026-11-07, [PR #28](https://github.com/Stihotvor/name_it_right/pull/28)), F03 (2026-11-07, [PR #29](https://github.com/Stihotvor/name_it_right/pull/29)), F04 (2026-11-07, [PR #30](https://github.com/Stihotvor/name_it_right/pull/30)), F05 (2026-11-07, [PR #31](https://github.com/Stihotvor/name_it_right/pull/31)), G01 (2026-11-07, [PR #32](https://github.com/Stihotvor/name_it_right/pull/32)), G02 (2026-11-07, [PR #33](https://github.com/Stihotvor/name_it_right/pull/33)), G03 (2026-11-07, [PR #34](https://github.com/Stihotvor/name_it_right/pull/34)), H01 (2026-11-07, [PR #35](https://github.com/Stihotvor/name_it_right/pull/35)), H02 (2026-11-07, [PR #36](https://github.com/Stihotvor/name_it_right/pull/36)). All 31 steps are Done.
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
5. `git-agent` pushes and opens the PR. A review subagent checks the diff. Fix findings on the same branch. Then `git-agent` squash merges.
   - Default rule: the user reviews and merges, and the agent never self-merges.
   - Exception from 2026-11-06: the user authorized the agent to push, review with a subagent, merge and continue while the user is away. The exception ends when the user says so.
6. Mark the step `Done` here with date and PR URL, in the step's own PR before the merge. The PR number is known after step 5 opens it.
7. Ask the user to compact the chat when the user is present. Repeat.

## Backlog
Branch numbers follow the opencode plan. The numbering conflicts below were fixed before step B01.

| Phase | Step | Branch | Scope |
|---|---|---|---|
| A Foundations | A01 (Done) | `docs/01-references-and-glossary` | Sources (30+) and master glossary |
| | A02 (Done) | `docs/03-patterns-index-action-context` | Patterns overview, action-and-context page |
| B Patterns | B01 (Done) | `docs/04-patterns-booleans-collections-units-time` | Booleans, collections, units, money, time |
| | B02 (Done) | `docs/05-patterns-symmetry-negation` | Symmetry pairs, negation, optionality |
| | B03 (Done) | `docs/06-patterns-cookbook` | 60+ bad -> better rows in 10+ categories |
| C Python | C01-C04 (Done) | `docs/08` to `docs/11-python-*` | Variables, functions, classes, class methods |
| | C05a (Done), C05b (Done) | `docs/12-python-test-naming-patterns`, `docs/12-python-test-advanced` | Test naming patterns, advanced test topics |
| D Databases | D01 (Done), D02 (Done), D03 (Done), D04 (Done) | `docs/13` to `docs/16-db-*` | Columns, tables, indexes and constraints, warehouse |
| E Languages | E01 (Done) | `docs/17-languages-index` | Languages overview, move Python nav, check links |
| | E02 (Done), E03 (Done), E04 (Done), E05 (Done), E06 (Done) | `docs/18` to `docs/22` | JS/TS, Java/Kotlin, C#/.NET, Go, Rust |
| F Systems | F01 (Done), F02 (Done), F03 (Done), F04 (Done), F05 (Done) | `docs/23` to `docs/27` | REST, GraphQL and events, errors and config, flags and observability, CLI |
| G Domains | G01 (Done), G02 (Done), G03 (Done) | `docs/28` to `docs/30` | E-commerce, payments/fintech/healthcare, logistics/SaaS/ML |
| H Final | H01 (Done) | `docs/31-index-crosslinks` | Home cards, landing cards, cross-links |
| | H02 (Done) | `docs/32-editorial-qa` | Consistency pass, link check, QA script |

## QA report (H02, 2026-11-07)
Checks run on the whole site (55 pages):
- `mkdocs build --strict` passes. It fails on a broken internal link or anchor.
- `python3 scripts/check_docs.py` reports `ok`. It checks a top heading on each page, balanced code fences (at any indent), no trailing spaces or tabs, no duplicate `##` headings, and the minimum rows on the seven example pages. The minimums are 15 entities, 8 to 12 actions and 8 to 10 traps (see `EXAMPLE_MINIMUMS` in the script). The script does not check the identifier counts or the "Why" columns of the page rules.
- Example pages: every page has 20 or more entities, 12 or more actions and 13 or more traps.
- Glossary: the script checks `##` headings only. The repeated letter headings (`####`) are the verb list and the noun list. They are not duplicate entries.

Fixed in H02: 7 pages had no top heading (Tables, Columns, Indexes, Constraints, Enums, Variables, Classes). 32 trailing spaces were removed from three Python pages (Functions, Classes, Variables).

Left as it is, on purpose:
- Admonition kinds. The pages use `success`, `tip` and `danger` for the three standard blocks, `warning` for the common anti-pattern pages, `info` for "See also" and `note` for side remarks. This follows the original pages.
- Contractions in the original pages (`don't`, `it's`). The new pages avoid them. A full tone rewrite of the original pages is out of scope.
- Spelling of `canceled` and `cancelled`. The examples use `canceled`. The healthcare page keeps the FHIR spelling `cancelled` and says so. The glossary, the Python enums and tests pages, and the gRPC code on the errors page use `cancelled`. These were left as they are.
- External URLs were not fetched. The Stripe, Shopify, ISO 20022, FHIR, GS1 and MLflow facts come from reviewer knowledge. Check them against the live pages before you rely on them.

Delivery notes:
- The step PRs (#5, and #7 to #36) were squash merged and opened ready, not as drafts. PR #36 is the last one. The repo rules for `git-agent` say merge commits and draft PRs. The user asked for squash merges in the overnight loop.
- The squash message of PR #18 has the trailer `Claude Haiku 5.5`. The other squash messages have `Claude Sonnet 5.5`.
- `gh-pages` was force updated many times by the CI step `mkdocs gh-deploy --force`. This is expected.
- CI has no build check on pull requests (open question 4).

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
