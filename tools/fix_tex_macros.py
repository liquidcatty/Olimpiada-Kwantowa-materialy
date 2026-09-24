"""Zamienia makra, ktore GitHub (MathJax w konfiguracji GitHuba) odrzuca.

Zglaszany blad: "the following macros are not allowed: operatorname".
  * \\operatorname{X}  ->  \\mathrm{X}   (identyczny wyglad, makro dozwolone)
  * \\tag{N}           ->  usuniete (numer przenoszony poza wzor, jesli potrzebny)

Uzycie:
    python tools/fix_tex_macros.py            # dry-run
    python tools/fix_tex_macros.py --apply
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}

OPERATORNAME = re.compile(r"\\operatorname\{([^{}]*)\}")
# \tag{N} jest w GitHubie ryzykowne; numer przenosimy do wnetrza wzoru jako tekst
TAG = re.compile(r"\s*\\tag\{([^{}]*)\}")


def main() -> int:
    apply = "--apply" in sys.argv
    files = 0
    ops = 0
    tags = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP):
            continue
        text = path.read_text(encoding="utf-8")
        new, n_ops = OPERATORNAME.subn(r"\\mathrm{\1}", text)
        new, n_tags = TAG.subn(lambda m: f" \\qquad ({m.group(1)})", new)
        if n_ops or n_tags:
            files += 1
            ops += n_ops
            tags += n_tags
            print(f"{path.relative_to(ROOT)}: operatorname {n_ops}x, tag {n_tags}x")
            if apply:
                path.write_text(new, encoding="utf-8")
    print(f"\n{'ZAPISANO' if apply else 'DRY-RUN'}: plikow {files}, operatorname {ops}, tag {tags}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
