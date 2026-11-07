"""Check the basic page structure and the size of the example tables.

Run from the repository root: python3 scripts/check_docs.py
The script exits with 1 when it finds a problem. Run `mkdocs build --strict` for links.
"""
import glob
import re
import sys
from pathlib import Path

# Minimum rows per example page: entities, actions, traps.
EXAMPLE_MINIMUMS = {
    "ecommerce": (15, 12, 10),
    "payments": (15, 8, 10),
    "fintech": (15, 8, 10),
    "healthcare": (15, 8, 10),
    "logistics": (15, 8, 8),
    "saas": (15, 8, 8),
    "ml": (15, 8, 8),
}


def table_rows(text, heading):
    """Count the data rows of the first table in a section."""
    match = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", text, flags=re.S | re.M)
    if not match:
        return 0
    rows = [l for l in match.group(1).splitlines() if l.startswith("|") and not re.match(r"^\|[-:| ]+\|$", l)]
    return max(len(rows) - 1, 0)


def check_page(path):
    problems = []
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    # Front matter is a block between two `---` lines.
    body = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S).lstrip()
    if not body.startswith("# "):
        problems.append("no H1 at the top")
    in_fence = False
    headings = []
    for line in lines:
        if re.match(r"\s*(```|~~~)", line):
            in_fence = not in_fence
        elif line.startswith("## ") and not in_fence:
            headings.append(line)
    if in_fence:
        problems.append("unbalanced code fence")
    for number, line in enumerate(lines, 1):
        if line != line.rstrip():
            problems.append(f"trailing space on line {number}")
        if "\t" in line:
            problems.append(f"tab on line {number}")
    problems += [f"duplicate heading {h!r}" for h in sorted(set(headings)) if headings.count(h) > 1]
    return problems


def check_examples():
    problems = []
    for name, (entities, actions, traps) in EXAMPLE_MINIMUMS.items():
        text = Path(f"docs/examples/{name}.md").read_text(encoding="utf-8")
        found = (table_rows(text, "Entities"), table_rows(text, "Actions"), table_rows(text, "Traps"))
        for label, have, need in zip(("entities", "actions", "traps"), found, (entities, actions, traps)):
            if have < need:
                problems.append(f"docs/examples/{name}.md: {have} {label}, need {need}")
    return problems


def main():
    problems = []
    for path in sorted(glob.glob("docs/**/*.md", recursive=True)):
        problems += [f"{path}: {p}" for p in check_page(path)]
    problems += check_examples()
    print("\n".join(problems) or "ok")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
