#!/usr/bin/env python3
"""Validate every SKILL.md: frontmatter, name/folder match, description length."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent / "skills"
errors, seen, count = [], set(), 0
for f in sorted(root.rglob("SKILL.md")):
    count += 1
    text = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{f}: missing frontmatter"); continue
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name or not desc:
        errors.append(f"{f}: needs name and description"); continue
    n = name.group(1).strip()
    if n != f.parent.name: errors.append(f"{f}: name '{n}' != folder '{f.parent.name}'")
    if n in seen: errors.append(f"{f}: duplicate name {n}")
    seen.add(n)
    if not re.fullmatch(r"[a-z0-9-]+", n): errors.append(f"{f}: bad name format")
    if len(desc.group(1)) > 1030: errors.append(f"{f}: description too long")
    if len(text.splitlines()) > 500: errors.append(f"{f}: over 500 lines")
print(f"Checked {count} skills")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("All good")
