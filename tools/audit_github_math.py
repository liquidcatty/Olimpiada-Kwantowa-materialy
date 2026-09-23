"""Audyt renderowania matematyki na GitHubie (z wlasnym self-testem).

Sprawdza reguly potwierdzone empirycznie na rendererze GitHuba
(`tools/probe_github_math.py`, POST api.github.com/markdown):
  * blok `$$...$$` musi rozpoczynac akapit - po linii tekstu bez pustej linii
    NIE renderuje sie,
  * blok `$$` nie dziala w wierszu tabeli,
  * inline `$...$` nie moze byc zlamane na dwa wiersze,
  * goła kreska pionowa wewnatrz wzoru w tabeli rozbija tabele.

Kod wewnatrz code-spanow (`` ` ``) i blokow ``` jest pomijany - dzieki temu
dokumentacja opisujaca te skladnie nie wywoluje falszywych alarmow.

Uruchomienie:
    python tools/audit_github_math.py               # audyt repo + self-test
    python tools/audit_github_math.py --self-test   # tylko self-test

Kod wyjscia: 0 = brak problemow, 1 = problemy w repo, 2 = blad self-testu.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}
FENCE_RE = re.compile(r"^\s*(```|~~~)")
DOLLAR_SINGLE = re.compile(r"(?<!\$)\$(?!\$)")


def strip_code_spans(line: str) -> str:
    """Usuwa code-spany, zeby $ i | wewnatrz `...` nie byly liczone jako skladnia."""
    return re.sub(r"`[^`\n]*`", "", line)


def strip_double_dollars(line: str) -> str:
    """Usuwa pary $$, zeby liczyc tylko pojedyncze $ (matematyka inline)."""
    return line.replace("$$", "")


def iter_md() -> list[Path]:
    return [p for p in sorted(ROOT.rglob("*.md"))
            if not any(x in SKIP for x in p.relative_to(ROOT).parts)]


def check_text(rel: str, text: str) -> tuple[list[str], dict[str, int]]:
    """Zwraca (lista problemow, licznik kategorii) dla tresci jednego pliku."""
    issues: list[str] = []
    counts = {"inline_multi": 0, "block_after_text": 0, "block_and_text": 0,
              "heading_math_info": 0, "table_math_pipe": 0}
    lines = text.splitlines()
    fence = False
    clean: list[str] = []          # tresc bez code-spanow i bez blokow kodu
    for raw in lines:
        if FENCE_RE.match(raw):
            fence = not fence
            clean.append("")
            continue
        clean.append("" if fence else strip_code_spans(raw))

    inside_block = False
    for i, line in enumerate(clean, 1):
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith("|") and "$$" in line:
            issues.append(f"  {rel}:{i} [tabela] $$ w wierszu tabeli")
            counts["table_math_pipe"] += 1

        if not inside_block and stripped.startswith("$$"):
            prev = clean[i - 2].rstrip() if i >= 2 else ""
            if prev and not prev.lstrip().startswith("#") \
                    and not prev.rstrip().endswith("\\") and not prev.strip().startswith("$$"):
                issues.append(f"  {rel}:{i} [blok] $$ po linii tekstu bez pustej linii")
                counts["block_after_text"] += 1
            if not (stripped.endswith("$$") and len(stripped) > 2):
                inside_block = True
        elif inside_block and stripped.endswith("$$"):
            inside_block = False
        elif not inside_block and "$$" in line:
            issues.append(f"  {rel}:{i} [blok] $$ w linii z tekstem: {stripped[:60]}")
            counts["block_and_text"] += 1

        if stripped.startswith("#") and len(DOLLAR_SINGLE.findall(line)) >= 2:
            # sonda GitHub API potwierdzila, ze matematyka w naglowkach renderuje sie
            counts["heading_math_info"] += 1

        if stripped.startswith("|"):
            for seg in re.findall(r"\$([^$\n]+)\$", line):
                if re.search(r"(?<!\\)\|", seg):
                    issues.append(f"  {rel}:{i} [tabela] kreska | wewnatrz math -> ${seg[:50]}$")
                    counts["table_math_pipe"] += 1

    # inline $...$ zlamane przez koniec wiersza
    open_math = False
    for i, line in enumerate(clean, 1):
        payload = strip_double_dollars(line)
        for _ in DOLLAR_SINGLE.finditer(payload):
            open_math = not open_math
        if open_math:
            issues.append(f"  {rel}:{i} [inline] $...$ zlamane na dwa wiersze")
            counts["inline_multi"] += 1
            open_math = False
    return issues, counts


SELF_TEST_CASES: list[tuple[str, str, bool]] = [
    ("inline w akapicie", "Tekst z $x^2$ w linii.\n", False),
    ("inline w code-spanie", "Tekst `$x^2$` w linii.\n", False),
    ("blok po pustej linii", "Tekst.\n\n$$\nx = y\n$$\n", False),
    ("blok po naglowku", "## Naglowek\n$$\nx = y\n$$\n", False),
    ("blok po tekscie bez pustej linii", "Tekst:\n$$\nx = y\n$$\n", True),
    ("dwa bloki pod rzad", "$$\na = b\n$$\n$$\nc = d\n$$\n", False),
    ("wiersz tabeli z $$ w code-spanie", "| a | b |\n| --- | --- |\n| `$$` | tak |\n", False),
    ("wiersz tabeli z gołym $$", "| a | b |\n| --- | --- |\n| $$ | nie |\n", True),
    ("wiersz tabeli z | w math", "| a | b |\n| --- | --- |\n| $x|y$ | $z$ |\n", True),
    ("wiersz tabeli z \\lvert", "| a | b |\n| --- | --- |\n| $x$ | $\\lvert y\\rvert$ |\n", False),
    ("inline zlamane na dwa wiersze", "Tekst $a = b\n+ c$ dalej.\n", True),
    ("blok w code-fence", "```\n$$\nx = y\n$$\n```\n", False),
    ("dokumentacja skladni w code-spanach", "| blok `$$` w linii z tekstem | nie |\n", False),
]


def self_test() -> list[str]:
    """Sprawdza, czy audyt poprawnie klasyfikuje znane przypadki."""
    failures: list[str] = []
    for name, text, should_flag in SELF_TEST_CASES:
        issues, _ = check_text("<self-test>", text)
        flagged = bool(issues)
        if flagged != should_flag:
            failures.append(
                f"  '{name}': oczekiwano {'flagi' if should_flag else 'braku flagi'}, "
                f"otrzymano {'flage' if flagged else 'brak flagi'}"
            )
    return failures


def main() -> int:
    failures = self_test()
    if failures:
        print("=== SELF-TEST AUDYTU: BLAD ===")
        for failure in failures:
            print(failure)
        return 2
    if "--self-test" in sys.argv:
        print(f"self-test OK ({len(SELF_TEST_CASES)} przypadkow)")
        return 0

    issues: list[str] = []
    totals = {"inline_multi": 0, "block_after_text": 0, "block_and_text": 0,
              "heading_math_info": 0, "table_math_pipe": 0}
    for path in iter_md():
        file_issues, counts = check_text(path.relative_to(ROOT).as_posix(),
                                         path.read_text(encoding="utf-8"))
        issues.extend(file_issues)
        for key, value in counts.items():
            totals[key] += value
    print("=== AUDYT RENDEROWANIA MATEMATYKI (GitHub) ===")
    for issue in issues:
        print(issue)
    print("Podsumowanie:", totals)
    print(f"problemow: {len(issues)}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())

