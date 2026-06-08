#!/usr/bin/env bash
# Regenerate per-tool variants from canonical /skills/ source.
#
# Usage: ./build.sh [tool]
#   tool: cursor | codex | aider | windsurf | continue | zed | all (default)

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 is required but not found in PATH." >&2
    exit 1
fi

python3 "$REPO_DIR/scripts/build.py" "$@"
