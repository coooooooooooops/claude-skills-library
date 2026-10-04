#!/usr/bin/env bash
# Build one zip per skill into dist/ for upload to Claude.ai.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$here/dist"
for d in "$here"/skills/*/*/; do
  n="$(basename "$d")"
  (cd "$(dirname "$d")" && zip -qr "$here/dist/$n.zip" "$n")
done
echo "Wrote $(ls "$here/dist" | wc -l) zips to dist/"
