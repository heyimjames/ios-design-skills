#!/usr/bin/env bash
# Install iOS design skills into the AI tool of your choice.
#
# Usage:
#   ./install.sh <tool> [install|uninstall]
#
# Examples:
#   ./install.sh claude-code              # symlink skills into ~/.claude/skills/
#   ./install.sh cursor                   # copy .mdc rules into ./.cursor/rules/
#   ./install.sh cursor --global          # ...into ~/.cursor/rules/ instead
#   ./install.sh codex                    # append to ./AGENTS.md (or create)
#   ./install.sh codex --global           # ...append to ~/.codex/AGENTS.md
#   ./install.sh claude-code uninstall    # remove symlinks

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS=(camera-and-photos chat-and-messaging interaction-primitives the-final-5-percent)

TOOL="${1:-}"
shift || true

ACTION="install"
GLOBAL=false
for arg in "$@"; do
    case "$arg" in
        uninstall|install) ACTION="$arg" ;;
        --global) GLOBAL=true ;;
    esac
done

usage() {
    cat <<EOF
Usage: ./install.sh <tool> [install|uninstall] [--global]

Tools:
  claude-code   Symlink into ~/.claude/skills/        (user-level, all projects)
  cursor        Copy .mdc into .cursor/rules/         (project; use --global for ~/.cursor/rules/)
  codex         Append to AGENTS.md                    (project; --global for ~/.codex/AGENTS.md)
  windsurf      Copy .windsurfrules                    (project)
  aider         Copy CONVENTIONS.md                    (project)
  continue      Copy into .continue/rules/             (project; --global for ~/.continue/rules/)
  zed           Copy into .rules/                      (project)

Examples:
  ./install.sh claude-code
  ./install.sh cursor --global
  ./install.sh codex uninstall
EOF
    exit 1
}

[[ -z "$TOOL" ]] && usage

# Run build if dist is missing or stale
if [[ ! -d "$REPO_DIR/dist" && "$TOOL" != "claude-code" ]]; then
    echo "→ Building dist/ ..."
    "$REPO_DIR/build.sh" all
fi

case "$TOOL" in
    # ------------------------------------------------------------------
    claude-code)
        TARGET="$HOME/.claude/skills"
        mkdir -p "$TARGET"
        if [[ "$ACTION" == "install" ]]; then
            for skill in "${SKILLS[@]}"; do
                ln -sfn "$REPO_DIR/skills/$skill" "$TARGET/$skill"
                echo "  ✓ linked $TARGET/$skill"
            done
            echo
            echo "✓ Installed 4 skills into Claude Code."
            echo "  Restart Claude Code (or /reload) to pick them up."
        else
            for skill in "${SKILLS[@]}"; do
                if [[ -L "$TARGET/$skill" ]]; then
                    rm -f "$TARGET/$skill"
                    echo "  ✓ removed $TARGET/$skill"
                fi
            done
            echo "✓ Uninstalled from Claude Code."
        fi
        ;;

    # ------------------------------------------------------------------
    cursor)
        if [[ "$GLOBAL" == "true" ]]; then
            TARGET="$HOME/.cursor/rules"
        else
            TARGET="$PWD/.cursor/rules"
        fi
        mkdir -p "$TARGET"
        if [[ "$ACTION" == "install" ]]; then
            cp "$REPO_DIR"/dist/cursor/.cursor/rules/*.mdc "$TARGET/"
            echo "✓ Copied 4 rules into $TARGET"
            echo "  Cursor will auto-attach them based on file globs."
        else
            rm -f "$TARGET"/ios-*.mdc
            echo "✓ Removed iOS rules from $TARGET"
        fi
        ;;

    # ------------------------------------------------------------------
    codex)
        if [[ "$GLOBAL" == "true" ]]; then
            TARGET_DIR="$HOME/.codex"
            mkdir -p "$TARGET_DIR"
            TARGET="$TARGET_DIR/AGENTS.md"
        else
            TARGET="$PWD/AGENTS.md"
        fi
        MARKER_BEGIN="<!-- BEGIN ios-design-skills -->"
        MARKER_END="<!-- END ios-design-skills -->"

        if [[ "$ACTION" == "install" ]]; then
            # Remove any existing block first
            if [[ -f "$TARGET" ]] && grep -q "$MARKER_BEGIN" "$TARGET"; then
                python3 -c "
import re, sys
p = '$TARGET'
content = open(p).read()
content = re.sub(r'$MARKER_BEGIN.*?$MARKER_END\n?', '', content, flags=re.DOTALL)
open(p, 'w').write(content)
"
            fi
            {
                [[ -f "$TARGET" ]] && echo ""
                echo "$MARKER_BEGIN"
                cat "$REPO_DIR/dist/codex/AGENTS.md"
                echo "$MARKER_END"
            } >> "$TARGET"
            echo "✓ Appended iOS design skills to $TARGET"
        else
            if [[ -f "$TARGET" ]] && grep -q "$MARKER_BEGIN" "$TARGET"; then
                python3 -c "
import re
p = '$TARGET'
content = open(p).read()
content = re.sub(r'\n*$MARKER_BEGIN.*?$MARKER_END\n?', '', content, flags=re.DOTALL)
open(p, 'w').write(content)
"
                echo "✓ Removed iOS design skills from $TARGET"
            else
                echo "  (no iOS design skills block found in $TARGET)"
            fi
        fi
        ;;

    # ------------------------------------------------------------------
    windsurf)
        TARGET="$PWD/.windsurfrules"
        if [[ "$ACTION" == "install" ]]; then
            cp "$REPO_DIR/dist/windsurf/.windsurfrules" "$TARGET"
            echo "✓ Copied .windsurfrules to $TARGET"
        else
            rm -f "$TARGET"
            echo "✓ Removed $TARGET"
        fi
        ;;

    # ------------------------------------------------------------------
    aider)
        TARGET="$PWD/CONVENTIONS.md"
        if [[ "$ACTION" == "install" ]]; then
            cp "$REPO_DIR/dist/aider/CONVENTIONS.md" "$TARGET"
            echo "✓ Copied CONVENTIONS.md to $TARGET"
            echo "  In .aider.conf.yml, set: read: CONVENTIONS.md"
        else
            rm -f "$TARGET"
            echo "✓ Removed $TARGET"
        fi
        ;;

    # ------------------------------------------------------------------
    continue)
        if [[ "$GLOBAL" == "true" ]]; then
            TARGET="$HOME/.continue/rules"
        else
            TARGET="$PWD/.continue/rules"
        fi
        mkdir -p "$TARGET"
        if [[ "$ACTION" == "install" ]]; then
            cp "$REPO_DIR"/dist/continue/.continue/rules/*.md "$TARGET/"
            echo "✓ Copied 4 rules into $TARGET"
        else
            rm -f "$TARGET"/ios-*.md
            echo "✓ Removed iOS rules from $TARGET"
        fi
        ;;

    # ------------------------------------------------------------------
    zed)
        TARGET="$PWD/.rules"
        mkdir -p "$TARGET"
        if [[ "$ACTION" == "install" ]]; then
            cp "$REPO_DIR"/dist/zed/.rules/*.md "$TARGET/"
            echo "✓ Copied 4 rules into $TARGET"
        else
            rm -f "$TARGET"/ios-*.md
            echo "✓ Removed iOS rules from $TARGET"
        fi
        ;;

    # ------------------------------------------------------------------
    *)
        echo "Unknown tool: $TOOL"
        echo
        usage
        ;;
esac
