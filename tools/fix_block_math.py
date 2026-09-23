"""Naprawa blokow wyswietlania ($$) tak, aby GitHub je renderowal.

Dowod empiryczny (POST https://api.github.com/markdown, mode=gfm):
  * `$$` w akapicie razem z tekstem -> HTML zostaje jako tekst z <br>, BEZ math-renderer
    (formula sie NIE renderuje),
  * `$$` rozpoczynajacy osobny akapit (pusta linia przed nim) -> math-renderer (OK),
  * `$$` po naglowku -> OK, w tabeli -> nie dziala, matematyka w naglowkach -> OK.

Naprawa: wstaw pusta linie przed kazdym blokiem `$$` poprzedzonym linia tekstu
oraz po bloku, po ktorym bezposrednio nastepuje tekst.

Uzycie:
    python tools/fix_block_math.py            # dry-run
    python tools/fix_block_math.py --apply
"""

from __future__ import annotations

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}


def find_blocks(lines: list[str]) -> list[tuple[int, int]]:
    """Zwraca liste (start, end) blokow wyswietlania (indeksy 0-based, end exclusive)."""
    blocks: list[tuple[int, int]] = []
    fence = False
    i = 0
    while i < len(lines):
        st = lines[i].strip()
        if st.startswith("```") or st.startswith("~~~"):
            fence = not fence
            i += 1
            continue
        if fence or not st.startswith("$$"):
            i += 1
            continue
        start = i
        # blok jednolinijkowy: $$...$$ na jednej linii
        if st.endswith("$$") and len(st) > 2:
            blocks.append((start, i + 1))
            i += 1
            continue
        i += 1
        while i < len(lines):
            if lines[i].strip().endswith("$$"):
                break
            i += 1
        blocks.append((start, min(i + 1, len(lines))))
        i += 1
    return blocks


def needs_blank_before(lines: list[str], start: int) -> bool:
    if start == 0:
        return False
    prev = lines[start - 1]
    if not prev.strip():
        return False
    if prev.strip().startswith("#"):
        return False
    return True


def needs_blank_after(lines: list[str], end: int) -> bool:
    if end >= len(lines):
        return False
    nxt = lines[end]
    if not nxt.strip():
        return False
    if nxt.strip().startswith("#"):
        return False
    return True


def fix_file(path: Path, apply: bool) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    log: list[str] = []
    # przechodzimy od konca, zeby indeksy pozostawaly aktualne
    for start, end in reversed(find_blocks(lines)):
        if needs_blank_after(lines, end):
            lines.insert(end, "")
            log.append(f"  pusta linia PO bloku konczacym sie w linii {end}")
        if needs_blank_before(lines, start):
            lines.insert(start, "")
            log.append(f"  pusta linia PRZED blokiem zaczynajacym sie w linii {start + 1}")
    if apply and log:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return log


def main() -> int:
    apply = "--apply" in sys.argv
    files = 0
    entries = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP):
            continue
        log = fix_file(path, apply)
        if log:
            files += 1
            entries += len(log)
            print(f"--- {path.relative_to(ROOT)}")
            for entry in log:
                print(entry)
    print(f"\n{'ZAPISANO' if apply else 'DRY-RUN'}: plikow {files}, wstawionych pustych linii {entries}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
