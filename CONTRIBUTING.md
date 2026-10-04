# Contributing

1. Pick a category folder in `skills/` (or add a new numbered one).
2. Create `skills/<category>/<skill-name>/SKILL.md` with `name` (lowercase-hyphen, matches folder) and a specific, trigger-rich `description` (max 1024 chars).
3. Keep `SKILL.md` under ~500 lines; move long material to `references/`.
4. Run `python3 scripts/validate_skills.py`.
5. Open a pull request describing what the skill does and 2-3 example prompts.
