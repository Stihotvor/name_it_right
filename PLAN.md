# Docs enhancement plan

Merged on 2026-11-06 from the opencode plan `~/.opencode/plan/name-it-right-naming-examples.md` and the repo status check.
The opencode files stay the detailed source: research tables (sections 2-3), page template (4.1), per-step research anchors (7).
Also there: `name-it-right-naming-examples-loop.md` (delivery loop) and `name-it-right-qa-checklist.py` (QA script).
These files are local to the author's machine. A fresh clone cannot reach them (see open question 1).

## Goal
Add a large, sourced catalogue of naming examples to the site. The site has strong rules but few worked examples. It has no API or operations guidance and no non-Python languages.

Out of scope: theme or build changes, generated content, analytics, licence changes, translation.

## Status on 2026-11-06
- Repo `Stihotvor/name_it_right`, default branch `main`. No open issues, no open PRs.
- Done: A01 (2026-11-06, [PR #5](https://github.com/Stihotvor/name_it_right/pull/5)), A02 (2026-11-06, [PR #7](https://github.com/Stihotvor/name_it_right/pull/7)), B01 (2026-11-06, [PR #8](https://github.com/Stihotvor/name_it_right/pull/8)), B02 (2026-11-06, [PR #9](https://github.com/Stihotvor/name_it_right/pull/9)), B03 (2026-11-06, [PR #10](https://github.com/Stihotvor/name_it_right/pull/10)), C01 (2026-11-06, [PR #11](https://github.com/Stihotvor/name_it_right/pull/11)), C02 (2026-11-06, [PR #12](https://github.com/Stihotvor/name_it_right/pull/12)), C03 (2026-11-06, [PR #13](https://github.com/Stihotvor/name_it_right/pull/13)), C04 (2026-11-06, [PR #14](https://github.com/Stihotvor/name_it_right/pull/14)), C05a (2026-11-06, [PR #15](https://github.com/Stihotvor/name_it_right/pull/15)), C05b (2026-11-06, [PR #16](https://github.com/Stihotvor/name_it_right/pull/16)), D01 (2026-11-06, [PR #17](https://github.com/Stihotvor/name_it_right/pull/17)), D02 (2026-11-06, [PR #18](https://github.com/Stihotvor/name_it_right/pull/18)), D03 (2026-11-06, [PR #19](https://github.com/Stihotvor/name_it_right/pull/19)), D04 (2026-11-07, [PR #20](https://github.com/Stihotvor/name_it_right/pull/20)), E01 (2026-11-07, [PR #21](https://github.com/Stihotvor/name_it_right/pull/21)), E02 (2026-11-07, [PR #22](https://github.com/Stihotvor/name_it_right/pull/22)), E03 (2026-11-07, [PR #23](https://github.com/Stihotvor/name_it_right/pull/23)), E04 (2026-11-07, [PR #24](https://github.com/Stihotvor/name_it_right/pull/24)), E05 (2026-11-07, [PR #25](https://github.com/Stihotvor/name_it_right/pull/25)), E06 (2026-11-07, [PR #26](https://github.com/Stihotvor/name_it_right/pull/26)), F01 (2026-11-07, [PR #27](https://github.com/Stihotvor/name_it_right/pull/27)), F02 (2026-11-07, [PR #28](https://github.com/Stihotvor/name_it_right/pull/28)), F03 (2026-11-07, [PR #29](https://github.com/Stihotvor/name_it_right/pull/29)), F04 (2026-11-07, [PR #30](https://github.com/Stihotvor/name_it_right/pull/30)), F05 (2026-11-07, [PR #31](https://github.com/Stihotvor/name_it_right/pull/31)), G01 (2026-11-07, [PR #32](https://github.com/Stihotvor/name_it_right/pull/32)), G02 (2026-11-07, [PR #33](https://github.com/Stihotvor/name_it_right/pull/33)). The other 3 steps are `Pending`.
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
Branch numbers follow the opencode plan. Fix the numbering conflicts below before step B01.

| Phase | Step | Branch | Scope |
|---|---|---|---|
| A Foundations | A01 (Done) | `docs/01-references-and-glossary` | Sources (30+) and master glossary |
| | A02 (Done) | `docs/03-patterns-index-action-context` | Patterns overview, action-and-context page |
| B Patterns | B01 (Done) | `docs/04-patterns-booleans-collections-units-time` | Booleans, collections, units, money, time |
| | B02 (Done) | `docs/05-patterns-symmetry-negation` | Symmetry pairs, negation, optionality |
| | B03 (Done) | `docs/06-patterns-cookbook` | 60+ bad -> better rows in 10+ categories |
| C Python | C01-C04 (Done) | `docs/08` to `docs/11-python-*` | Variables, functions, classes, class methods |
| | C05a (Done), C05b (Done) | `docs/12a-...`, `docs/12b-...` | Test naming patterns, advanced test topics |
| D Databases | D01 (Done), D02 (Done), D03 (Done), D04 (Done) | `docs/13` to `docs/16-db-*` | Columns, tables, indexes and constraints, warehouse |
| E Languages | E01 (Done) | `docs/17-languages-index` | Languages overview, move Python nav, check links |
| | E02 (Done), E03 (Done), E04 (Done), E05 (Done), E06 (Done) | `docs/18` to `docs/22` | JS/TS, Java/Kotlin, C#/.NET, Go, Rust |
| F Systems | F01 (Done), F02 (Done), F03 (Done), F04 (Done), F05 (Done) | `docs/23` to `docs/27` | REST, GraphQL and events, errors and config, flags and observability, CLI |
| G Domains | G01 (Done), G02 (Done), G03 | `docs/28` to `docs/30` | E-commerce, payments/fintech/healthcare, logistics/SaaS/ML |
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
