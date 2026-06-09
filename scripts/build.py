#!/usr/bin/env python3
"""
Build per-tool variants of the iOS design skills from canonical SKILL.md files.

The canonical source lives in /skills/<name>/SKILL.md (Claude Code native format).
This script reads those and emits per-tool variants into /dist/<tool>/.

Usage:
    python3 scripts/build.py [tool]

Where tool is one of: cursor, codex, aider, windsurf, continue, zed, all (default).

No external dependencies — uses Python 3 stdlib only.
"""

import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "plugins" / "heyimjames" / "skills"
DIST_DIR = REPO_ROOT / "dist"

SKILLS = [
    "camera-and-photos",
    "chat-and-messaging",
    "interaction-primitives",
    "the-final-5-percent",
    "og-image-design",
]

# Per-skill, per-tool config
SKILL_LABELS = {
    "camera-and-photos": "heyimjames:camera-and-photos — Camera & Photos",
    "chat-and-messaging": "heyimjames:chat-and-messaging — Chat & Messaging",
    "interaction-primitives": "heyimjames:interaction-primitives — Widgets, Live Activities, Haptics",
    "the-final-5-percent": "heyimjames:the-final-5-percent — The Final 5% Polish",
    "og-image-design": "heyimjames:og-image-design — OG Image Design",
}

# File-name prefix for per-skill outputs (Cursor / Continue / Zed)
FILE_PREFIX = "heyimjames-"

# File patterns that auto-attach each rule in Cursor/Windsurf/Continue
SKILL_GLOBS = {
    "camera-and-photos": [
        "**/Camera*.swift", "**/Photo*.swift", "**/Capture*.swift",
        "**/*Camera*.swift", "**/*Photo*.swift", "**/*Capture*.swift",
        "**/AV*.swift", "**/PhotoKit*.swift", "**/Vision*.swift",
    ],
    "chat-and-messaging": [
        "**/Message*.swift", "**/Chat*.swift", "**/Conversation*.swift",
        "**/*Message*.swift", "**/*Chat*.swift", "**/*Conversation*.swift",
        "**/Composer*.swift", "**/Bubble*.swift", "**/Inbox*.swift",
    ],
    "interaction-primitives": [
        "**/Widget*.swift", "**/*Widget*.swift",
        "**/LiveActivity*.swift", "**/*LiveActivity*.swift",
        "**/Activity*.swift", "**/AppIntent*.swift", "**/*Intent*.swift",
        "**/Haptic*.swift", "**/*Haptic*.swift",
        "**/ControlWidget*.swift",
    ],
    "the-final-5-percent": [
        "**/*.swift",  # cross-cutting polish — applies to any Swift code
    ],
    "og-image-design": [
        # Cross-platform — attaches when OG-image-related files are in context.
        "**/og*.tsx", "**/og*.ts", "**/og*.jsx", "**/og*.js",
        "**/opengraph-image*.tsx", "**/opengraph-image*.ts", "**/opengraph-image*.jsx", "**/opengraph-image*.js",
        "**/twitter-image*.tsx", "**/twitter-image*.ts",
        "**/og.html", "**/og-image*.html",
        "**/satori*.ts", "**/satori*.tsx",
        "**/*.figma.ts",  # designers staging an OG in Code Connect
    ],
}


def parse_skill(skill_dir: Path):
    """Parse SKILL.md and return (frontmatter_dict, body_text)."""
    skill_md = skill_dir / "SKILL.md"
    content = skill_md.read_text(encoding="utf-8")

    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        return {}, content

    fm_text, body = match.groups()
    fm = {}
    current_key = None
    current_value_lines = []

    for line in fm_text.split("\n"):
        # New top-level key
        if re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*:", line):
            if current_key:
                fm[current_key] = "\n".join(current_value_lines).strip().strip('"').strip("'")
            key, _, value = line.partition(":")
            current_key = key.strip()
            current_value_lines = [value.strip()] if value.strip() else []
        elif line.strip() and current_key:
            current_value_lines.append(line.strip())

    if current_key:
        fm[current_key] = "\n".join(current_value_lines).strip().strip('"').strip("'")

    return fm, body.lstrip()


def reset_dist():
    """Wipe the dist directory before regenerating."""
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()


# -------- Cursor -------------------------------------------------------------

def build_cursor(skills_data):
    out_dir = DIST_DIR / "cursor" / ".cursor" / "rules"
    out_dir.mkdir(parents=True, exist_ok=True)

    for skill_name, (fm, body) in skills_data.items():
        target = out_dir / f"{FILE_PREFIX}{skill_name}.mdc"
        globs = SKILL_GLOBS.get(skill_name, ["**/*.swift"])
        globs_str = ", ".join(f'"{g}"' for g in globs)

        # Cursor description should be a single line; strip newlines from canonical.
        # Prefix with the brand for visibility in Cursor's rules panel.
        raw_description = fm.get("description", "").replace("\n", " ").strip()
        description = f"heyimjames:{skill_name} — {raw_description}"

        frontmatter = (
            "---\n"
            f"description: {description}\n"
            f"globs: [{globs_str}]\n"
            "alwaysApply: false\n"
            "---\n\n"
        )

        target.write_text(frontmatter + body, encoding="utf-8")
        print(f"  ✓ cursor/.cursor/rules/{FILE_PREFIX}{skill_name}.mdc")


# -------- Codex CLI ----------------------------------------------------------

def build_codex(skills_data):
    """
    Codex reads AGENTS.md at project or user level. Concatenate all skills
    with section headers so they're all accessible at all times.
    """
    out_dir = DIST_DIR / "codex"
    out_dir.mkdir(parents=True, exist_ok=True)

    parts = [
        "# heyimjames Design-Engineering Skills\n",
        "\n",
        "This document encodes five detailed design-engineering skills — four for\n",
        "building best-in-class native iOS/SwiftUI apps, plus one cross-platform\n",
        "OG image design skill. When working on Swift/SwiftUI code, consult the\n",
        "relevant iOS section. When designing OG / social-preview images, consult\n",
        "the OG section.\n",
        "\n",
        "## Index\n",
        "\n",
    ]
    for skill_name in SKILLS:
        label = SKILL_LABELS[skill_name]
        anchor = skill_name.replace("-", "-")
        parts.append(f"- **{label}** — see `## {label}` below\n")
    parts.append("\n---\n\n")

    for skill_name in SKILLS:
        fm, body = skills_data[skill_name]
        label = SKILL_LABELS[skill_name]
        description = fm.get("description", "").replace("\n", " ").strip()

        parts.append(f"## {label}\n\n")
        parts.append(f"_When to use this section: {description}_\n\n")
        parts.append(body)
        parts.append("\n\n---\n\n")

    (out_dir / "AGENTS.md").write_text("".join(parts), encoding="utf-8")
    print(f"  ✓ codex/AGENTS.md")


# -------- Aider --------------------------------------------------------------

def build_aider(skills_data):
    """Same content as Codex, different filename."""
    out_dir = DIST_DIR / "aider"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Reuse Codex content
    codex_content = (DIST_DIR / "codex" / "AGENTS.md").read_text(encoding="utf-8")
    (out_dir / "CONVENTIONS.md").write_text(codex_content, encoding="utf-8")
    print(f"  ✓ aider/CONVENTIONS.md")


# -------- Windsurf -----------------------------------------------------------

def build_windsurf(skills_data):
    out_dir = DIST_DIR / "windsurf"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Single .windsurfrules at project root, concatenated
    codex_content = (DIST_DIR / "codex" / "AGENTS.md").read_text(encoding="utf-8")
    (out_dir / ".windsurfrules").write_text(codex_content, encoding="utf-8")
    print(f"  ✓ windsurf/.windsurfrules")


# -------- Continue -----------------------------------------------------------

def build_continue(skills_data):
    out_dir = DIST_DIR / "continue" / ".continue" / "rules"
    out_dir.mkdir(parents=True, exist_ok=True)

    for skill_name, (fm, body) in skills_data.items():
        target = out_dir / f"{FILE_PREFIX}{skill_name}.md"
        description = fm.get("description", "").replace("\n", " ").strip()
        frontmatter = (
            "---\n"
            f"name: {fm.get('name', f'ios-{skill_name}')}\n"
            f"description: {description}\n"
            "---\n\n"
        )
        target.write_text(frontmatter + body, encoding="utf-8")
        print(f"  ✓ continue/.continue/rules/{FILE_PREFIX}{skill_name}.md")


# -------- Zed ----------------------------------------------------------------

def build_zed(skills_data):
    out_dir = DIST_DIR / "zed" / ".rules"
    out_dir.mkdir(parents=True, exist_ok=True)

    for skill_name, (fm, body) in skills_data.items():
        target = out_dir / f"{FILE_PREFIX}{skill_name}.md"
        # Zed reads plain markdown
        description = fm.get("description", "").replace("\n", " ").strip()
        header = f"# {SKILL_LABELS[skill_name]}\n\n_{description}_\n\n---\n\n"
        target.write_text(header + body, encoding="utf-8")
        print(f"  ✓ zed/.rules/{FILE_PREFIX}{skill_name}.md")


# -------- Main ---------------------------------------------------------------

BUILDERS = {
    "cursor": build_cursor,
    "codex": build_codex,
    "aider": build_aider,
    "windsurf": build_windsurf,
    "continue": build_continue,
    "zed": build_zed,
}


def main():
    tool = sys.argv[1] if len(sys.argv) > 1 else "all"

    if tool not in BUILDERS and tool != "all":
        print(f"Unknown tool: {tool}")
        print(f"Available: {', '.join(BUILDERS.keys())}, all")
        sys.exit(1)

    # Load all skills once
    print("Loading canonical skills...")
    skills_data = {}
    for skill_name in SKILLS:
        skill_dir = SKILLS_DIR / skill_name
        if not skill_dir.exists():
            print(f"  ✗ missing: {skill_dir}")
            sys.exit(1)
        skills_data[skill_name] = parse_skill(skill_dir)
        print(f"  ✓ loaded {skill_name}")

    print()

    if tool == "all":
        print("Building all variants (clean dist/)...")
        reset_dist()
        # Order matters: codex first, then aider/windsurf reuse its output
        for t in ["cursor", "codex", "aider", "windsurf", "continue", "zed"]:
            print(f"\nBuilding {t}...")
            BUILDERS[t](skills_data)
    else:
        print(f"Building {tool}...")
        BUILDERS[tool](skills_data)

    print("\n✓ Done.")


if __name__ == "__main__":
    main()
