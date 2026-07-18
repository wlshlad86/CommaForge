from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "CANONICAL-STATE.md",
    "AGENTS.md",
    "docs/PHASE1.md",
    "experiments/001-solo-founder-ai-operator-sprint/EXPERIMENT.md",
    "scoreboard/SCOREBOARD.md",
    "intelligence/SOURCE-REGISTER.md",
]


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken local link in {path.relative_to(ROOT)}: {target}")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository validation passed: {len(list(ROOT.rglob('*.md')))} Markdown files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())

