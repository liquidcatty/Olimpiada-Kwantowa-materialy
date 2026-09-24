"""Wysyla do renderera GitHuba realny fragment pliku z repo i pokazuje wynik.

Uruchomienie:
    python tools/probe_file_segment.py praca-domowa/praca-domowa-02.md 8 24
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from probe_github_math import post  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    rel = sys.argv[1]
    first = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    last = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    lines = (ROOT / rel).read_text(encoding="utf-8").splitlines()
    segment = "\n".join(lines[first - 1:last]) + "\n"
    print(f"--- wejscie: {rel} linie {first}-{last} ---")
    print(segment)
    html = post(segment)
    print("--- HTML z GitHub ---")
    print(html)
    blocks = html.count('class="js-display-math"')
    inline = html.count('class="js-inline-math"')
    print(f"--- WERDYKT: blokow math-renderer {blocks}, inline math-renderer {inline} ---")
    return 0


if __name__ == "__main__":
    sys.exit(main())
