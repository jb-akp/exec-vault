#!/usr/bin/env python3
"""Vault check: broken [[wikilinks]], notes missing frontmatter, a CLAUDE.md that has grown too long.
Usage: python3 tools/vault_check.py [vault_dir]   (exit 1 if anything fails)"""
import re, sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
SKIP = {".git", ".claude", ".obsidian", "tools", "examples", "90 Archive"}
MAX_RULES_LINES = 60

notes = [p for p in root.rglob("*.md") if not SKIP & set(p.relative_to(root).parts)]
names = {p.stem.lower() for p in notes} | {str(p.relative_to(root).with_suffix("")).lower() for p in notes}
problems = []

for p in notes:
    rel = p.relative_to(root)
    text = p.read_text()
    if rel.name != "CLAUDE.md" and not text.startswith("---\n"):
        problems.append(f"no frontmatter: {rel}")
    elif rel.name != "CLAUDE.md":
        fm = text.split("---", 2)[1]
        for key in ("type", "updated"):
            if not re.search(rf"^{key}:", fm, re.M):
                problems.append(f"frontmatter missing '{key}': {rel}")
    for link in re.findall(r"\[\[([^\]|#]+)", re.sub(r"`[^`]*`", "", text)):
        if link.strip().lower() not in names:
            problems.append(f"broken link [[{link.strip()}]] in {rel}")

rules = root / "CLAUDE.md"
if rules.exists():
    n = len(rules.read_text().splitlines())
    if n > MAX_RULES_LINES:
        problems.append(f"CLAUDE.md is {n} lines (max {MAX_RULES_LINES}): move content into the folders it points to")
else:
    problems.append("no CLAUDE.md at the vault root")

print(f"{len(notes)} notes checked in {root.name}/")
for line in problems:
    print("  FAIL", line)
print("OK: 0 problems" if not problems else f"{len(problems)} problems")
sys.exit(1 if problems else 0)
