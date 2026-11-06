# Docs enhancement plan

Status on 2026-11-06: no open issues, no open PRs on `Stihotvor/name_it_right`.

## Known state
- 24 pages, about 1980 lines.
- Thin pages: `docs/databases/*` (9-24 lines) and `docs/common/*` (31-56 lines).
- Unfinished work: `docs/common/references-and-glossary.md` (381 lines, `status: new`) and its `mkdocs.yml` nav entry. It exists only as uncommitted files in `~/PycharmProjects/name_it_right` on branch `docs/01-references-and-glossary`.
- CI only deploys on push to `main`. No build check on pull requests.

## Existing plan (opencode)
An earlier plan exists outside the repo: `~/.opencode/plan/name-it-right-naming-examples.md` (created 2026-11-06).
- Goal: add a sourced catalogue of naming examples. 32 steps in phases A-H, one branch and one PR per step.
- Status: all steps are `Pending`. Step A01 (`docs/01-references-and-glossary`) is the unfinished local work above.
- Related files in `~/.opencode/plan/`: `name-it-right-naming-examples-loop.md` (delivery loop) and `name-it-right-qa-checklist.py` (QA script).
- This backlog below is a short draft. Merge it with the opencode plan before work starts.

## Backlog
1. Bring the references and glossary page into this repo (copy from PycharmProjects) and review it.
2. Expand `databases/` pages: enums, tables, indexes, constraints, columns. Add good and bad examples.
3. Expand `common/` pages: meaning, consistency, structure, abbreviations. Add a decision checklist.
4. Add cross-links between `common/` rules and the language pages.
5. Add missing areas. Candidates: API/REST, JS/TS, git branches and commits, tests across languages. Confirm scope first.
6. Quality gate: `mkdocs build --strict`, link check, consistent `status` front matter. Consider a PR build job in CI.

## Open questions
- Which of the candidate areas in item 5 are in scope?
- Add a PR build check to CI?
