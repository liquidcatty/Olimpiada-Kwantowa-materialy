"""Scala matematyke inline rozciagnieta na dwa wiersze ($...$ przez zlamanie wiersza).

GitHub (podobnie jak inne renderery) nie renderuje matematyki inline, ktora
przechodzi przez koniec wiersza - pokazuje surowe $. Naprawa: laczy takie wiersze
w jeden (spacja wewnatrz math jest nieistotna skladniowo).

Uzycie:
    python tools/fix_math_wrap.py            # podglad zmian (dry-run)
    python tools/fix_math_wrap.py --apply    # zapis zmian
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}


def strip_for_state(line: str) -> str:
    """Usuwa code-spany i pary $$, zeby liczyc tylko pojedyncze $."""
    line = re.sub(r"`[^`]*`", "", line)
    line = re.sub(r"\$\$", "", line)
    return line


def open_at_end(state: bool, line: str) -> bool:
    for ch in strip_for_state(line):
        if ch == "$":
            state = not state
    return state


def fix_file(path: Path, apply: bool) -> tuple[int, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    state = False
    buffer: str | None = None
    merged = 0
    log: list[str] = []
    fence: str | None = None          # otwarte ogrodzenie ``` / ~~~
    for idx, line in enumerate(lines, 1):
        stripped = line.lstrip()
        # obsluga ogrodzen kodu: wewnatrz nich nic nie zmieniamy
        if fence is None and (stripped.startswith("```") or stripped.startswith("~~~")):
            fence = stripped[:3]
            out.append(line)
            continue
        if fence is not None:
            out.append(line)
            if stripped.startswith(fence):
                fence = None
            continue
        if buffer is not None:
            buffer = buffer + " " + line.strip()
            log.append(f"  scalono z wierszem {idx}: {line.strip()[:80]}")
            merged += 1
        else:
            buffer = line
        state = open_at_end(state, line)
        if not state:
            out.append(buffer)
            buffer = None
    if buffer is not None:
        out.append(buffer)
        log.append("  UWAGA: niezamkniete $ na koncu pliku")
    if apply and out != lines:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return merged, log


def main() -> int:
    apply = "--apply" in sys.argv
    total = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP for part in path.relative_to(ROOT).parts):
            continue
        merged, log = fix_file(path, apply)
        if merged:
            total += merged
            print(f"{path.relative_to(ROOT)}: scalen {merged}")
            for entry in log:
                print(entry)
    print(f"\n{'ZAPISANO' if apply else 'DRY-RUN'}: scalen lacznie {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
