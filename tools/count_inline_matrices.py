"""Liczy wystapienia inline-macierzy (do przydzialu pracy).

Uruchomienie:
    python tools/count_inline_matrices.py
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
ENV_RE = re.compile(r"\\begin\{(pmatrix|bmatrix|vmatrix|matrix|smallmatrix|cases|aligned|array|split)\}")


def main() -> int:
    per_file: collections.Counter[str] = collections.Counter()
    kinds: collections.Counter[str] = collections.Counter()
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP):
            continue
        text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"),
                      path.read_text(encoding="utf-8"), flags=re.S)
        text = re.sub(r"`[^`\n]*`", " ", text)
        flat = re.sub(r"\$\$.+?\$\$", " ", text, flags=re.S)
        for match in re.finditer(r"\$([^$\n]+)\$", flat):
            seg = match.group(1)
            if "\\\\" in seg or ENV_RE.search(seg):
                per_file[path.relative_to(ROOT).as_posix()] += 1
                line_start = flat.rfind("\n", 0, match.start()) + 1
                line = flat[line_start:flat.find("\n", match.start())].strip()
                if line.startswith("|"):
                    kinds["tabela"] += 1
                elif re.match(r"^(?:[-*+]|\d+[.)])\s", line):
                    kinds["lista"] += 1
                else:
                    kinds["akapit"] += 1
    print("inline-macierze per plik:")
    for name, count in per_file.most_common():
        print(f"  {count:>3}  {name}")
    print("\nkontekst:", dict(kinds), "razem:", sum(per_file.values()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
