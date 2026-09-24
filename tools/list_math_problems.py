"""Inwentarz dwoch problemow renderowania na GitHubie (caly plik, nie linia po linii):

  A. znak * wewnatrz matematyki -> Markdown robi z niego kursywe (blad wykladnika),
  B. podwojny backslash / srodowisko macierzowe w matematyce INLINE -> GitHub nie
     rozpoznaje wzoru (dziala tylko w bloku $$).

Uruchomienie:
    python tools/list_math_problems.py
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


def iter_md() -> list[Path]:
    return [p for p in sorted(ROOT.rglob("*.md"))
            if not any(x in SKIP for x in p.relative_to(ROOT).parts)]


def strip_code_and_fences(text: str) -> str:
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    return re.sub(r"`[^`\n]*`", " ", text)


def classify(text: str, start: int) -> str:
    """Okresla kontekst wzoru: tabela / lista / akapit."""
    line_start = text.rfind("\n", 0, start) + 1
    line = text[line_start:text.find("\n", start)]
    stripped = line.strip()
    if stripped.startswith("|"):
        return "tabela"
    if re.match(r"^(?:[-*+]|\d+[.)])\s", stripped):
        return "lista"
    return "akapit"


def main() -> int:
    stars: collections.Counter[str] = collections.Counter()
    inline_matrix: collections.Counter[str] = collections.Counter()
    examples: dict[str, list[str]] = collections.defaultdict(list)
    for path in iter_md():
        rel = path.relative_to(ROOT).as_posix()
        text = strip_code_and_fences(path.read_text(encoding="utf-8"))
        for match in re.finditer(r"\$\$(.+?)\$\$", text, flags=re.S):
            if "*" in match.group(1):
                stars["blok $$"] += 1
                examples["A: blok $$"].append(f"{rel}: {match.group(1).strip()[:70]}")
        without_blocks = re.sub(r"\$\$.+?\$\$", " ", text, flags=re.S)
        for match in re.finditer(r"\$([^$\n]+)\$", without_blocks):
            seg = match.group(1)
            if "*" in seg:
                stars["inline"] += 1
                examples["A: inline"].append(f"{rel}: {seg.strip()[:70]}")
            if "\\\\" in seg or ENV_RE.search(seg):
                kind = classify(without_blocks, match.start())
                inline_matrix[kind] += 1
                examples[f"B: {kind}"].append(f"{rel}: {seg.strip()[:75]}")
    print("=== A. gwiazdka * wewnatrz matematyki ===")
    for key, count in stars.most_common():
        print(f"  {key}: {count}")
    print("\n=== B. inline z podwojnym backslashem lub srodowiskiem ===")
    for key, count in inline_matrix.most_common():
        print(f"  {key}: {count}")
    for key in sorted(examples):
        items = examples[key]
        print(f"\n--- {key} ({len(items)}) ---")
        for item in items[:14]:
            print("   ", item)
    return 0


if __name__ == "__main__":
    sys.exit(main())
