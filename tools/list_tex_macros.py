"""Inwentarz makr LaTeX uzywanych w repo (do kontroli zgodnosci z GitHubem).

Uruchomienie:
    python tools/list_tex_macros.py
"""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}

# makra, ktore GitHub (MathJax w konfiguracji GitHuba) potrafi odrzucic
RISKY = {
    "operatorname", "DeclareMathOperator", "newcommand", "renewcommand", "def", "require",
    "href", "style", "class", "cssId", "id", "unicode", "textTip", "bm", "boldsymbol",
    "label", "tag", "bbox", "enclose", "htmlClass", "htmlStyle", "htmlId", "boldsymbol",
    "newenvironment", "providecommand", "let", "xrightarrow", "xleftarrow", "substack",
    "overbrace", "underbrace", "stackrel", "binom", "dbinom", "tbinom", "vmatrix",
    "smallmatrix", "substack", "prescript", "overset", "underset", "bbox", "color",
    "textcolor", "definecolor", "includegraphics", "raisebox",
}


def main() -> int:
    counter: collections.Counter[str] = collections.Counter()
    where: dict[str, list[str]] = collections.defaultdict(list)
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP):
            continue
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        text = re.sub(r"`[^`\n]*`", " ", text)
        for match in re.finditer(r"\\([A-Za-z]+)", text):
            name = match.group(1)
            counter[name] += 1
            if len(where[name]) < 4:
                where[name].append(path.relative_to(ROOT).as_posix())
    print(f"makra uzywane w repo: {len(counter)}")
    for name, count in counter.most_common():
        flag = "  <-- RYZYKOWNE" if name in RISKY else ""
        print(f"  {name:22} {count:>5}x{flag}")
    print("\n--- podsumowanie ryzyka ---")
    risky_found = [n for n in counter if n in RISKY]
    if risky_found:
        for name in risky_found:
            print(f"  {name}: {counter[name]}x, np. {where[name][:3]}")
    else:
        print("  brak ryzykownych makr")
    return 0


if __name__ == "__main__":
    sys.exit(main())
