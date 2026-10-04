#!/usr/bin/env bash
# Install all skills for Claude Code.  Usage: ./scripts/install.sh --user | --project
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
case "${1:---user}" in
  --user) dest="$HOME/.claude/skills" ;;
  --project) dest="$PWD/.claude/skills" ;;
  *) echo "Usage: $0 --user | --project"; exit 1 ;;
esac
mkdir -p "$dest"
count=0
for d in "$here"/skills/*/*/; do
  cp -R "$d" "$dest/$(basename "$d")"
  count=$((count+1))
done
echo "Installed $count skills into $dest"
