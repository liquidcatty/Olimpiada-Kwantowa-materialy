"""Audyt tresci repo: (1) ryzykowne konstrukcje matematyczne dla GitHub MathJax,
(2) wszystkie bloki cytatow (info-kramki), (3) frazy motywacyjne/meta.

Uruchomienie:
    python tools/audit_content.py            # pelny raport
    python tools/audit_content.py --math     # tylko problemy z matematyka
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "_tmp", "tools", "node_modules"}

# --- konstrukcje, ktore na GitHubie (MathJax) sa ryzykowne lub nie dzialaja ----
RISKY_MACROS = [
    (r"\\bm\{", "\\bm{} (pakiet bm - czesto niedostepny; uzyj \\mathbf{})"),
    (r"\\boldsymbol\{", "\\boldsymbol{} (ryzykowne; uzyj \\mathbf{})"),
    (r"\\operatorname\{", "\\operatorname{} - GitHub odrzuca to makro; uzyj \\mathrm{}"),
    (r"\\tag\{", "\\tag{} - ryzykowne; numer wpisz jako \\qquad (N) wewnatrz wzoru"),
    (r"\\newcommand", "\\newcommand (ryzykowne)"),
    (r"\\def\\", "\\def (ryzykowne)"),
    (r"\\require\{", "\\require{} (niedozwolone)"),
    (r"\\href\{", "\\href{} (niedozwolone)"),
    (r"\\label\{", "\\label{} (nie dziala)"),
    (r"\\ref\{", "\\ref{} (nie dziala)"),
    (r"\\eqref\{", "\\eqref{} (nie dziala)"),
    (r"\\begin\{align\}", "\\begin{align} (GitHub wymaga aligned w $$)"),
    (r"\\begin\{equation\}", "\\begin{equation} (nie dziala)"),
    (r"\\begin\{eqnarray\}", "\\begin{eqnarray} (nie dziala)"),
    (r"\\begin\{table\}", "\\begin{table} (nie dziala)"),
    (r"\\begin\{figure\}", "\\begin{figure} (nie dziala)"),
    (r"\\mathbbm", "\\mathbbm (niedostepne; uzyj \\mathbb)"),
    (r"\\begin\{tikz", "tikz (nie dziala)"),
]

# wzorce tekstowe, ktore psuja parsowanie matematyki (sprawdzane w liniach z $)
RISKY_TEXT = [
    (r"<[A-Za-z][A-Za-z0-9]*>", "<litera...> w linii z math (moze byc zjedzone jako tag HTML)"),
]

# w wierszach tabeli znak | wewnatrz math rozbija tabele (trzeba \lvert / \rvert)
TABLE_MATH_PIPE = True

MOTIVATION = [
    r"\bPowodzenia\b", r"\bpowodzenia\b", r"\bpamiętaj\b", r"\bPamiętaj\b", r"\bZapamiętaj\b",
    r"\bNie zrażaj\b", r"\bwarto\b", r"\bWarto\b", r"świetny trening", r"najlepszy trening",
    r"buduje pewność", r"Nie bój", r"zaskoczy", r"To nic trudnego", r"\bspokojnie\b",
    r"Klucz do sukcesu", r"Nie panikuj", r"\bgratulacje\b", r"\bGratulacje\b",
    r"dasz radę", r"uwierz", r"nie przejmuj", r"ciesz się", r"trudno Ci", r"zbuduj pewność",
]


def iter_md() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    )


def strip_code(text: str) -> str:
    """Usuwa bloki kodu i code-spany, zeby nie raportowac falszywych trafien."""
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    return re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), text)


def math_segments(text: str) -> list[tuple[int, str, str]]:
    """Zwraca (linia, typ, tresc) dla segmentow matematycznych."""
    out: list[tuple[int, str, str]] = []
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\$\$(.+?)\$\$", line):
            out.append((i, "display-inline", m.group(1)))
        rest = re.sub(r"\$\$.+?\$\$", "", line)
        for m in re.finditer(r"\$([^$]+)\$", rest):
            out.append((i, "inline", m.group(1)))
    return out


def report_math() -> int:
    problems = 0
    print("=== 1. MATEMATYKA: ryzykowne konstrukcje ===")
    for path in iter_md():
        text = strip_code(path.read_text(encoding="utf-8"))
        rel = path.relative_to(ROOT)
        for i, kind, seg in math_segments(text):
            for pattern, desc in RISKY_MACROS:
                if re.search(pattern, seg):
                    print(f"  {rel}:{i} [{kind}] {desc}")
                    problems += 1
            left = len(re.findall(r"\\left(?![A-Za-z])", seg))
            right = len(re.findall(r"\\right(?![A-Za-z])", seg))
            if left != right:
                print(f"  {rel}:{i} [{kind}] niezbalansowane \\left ({left}) / \\right ({right})")
                problems += 1
            for env in re.findall(r"\\begin\{(\w+\*?)\}", seg):
                if f"\\end{{{env}}}" not in seg:
                    print(f"  {rel}:{i} [{kind}] \\begin{{{env}}} bez \\end")
                    problems += 1
            # GitHub nie renderuje $ ... $ (spacja tuz za otwierajacym lub przed zamykajacym $)
            if kind == "inline" and (seg[:1].isspace() or seg[-1:].isspace()):
                print(f"  {rel}:{i} [inline] spacja wewnatrz $ ... $ -> ${seg[:40]}$")
                problems += 1
            # <x> wewnatrz matematyki moze zostac zjedzone jako tag HTML
            for m in re.finditer(r"<[A-Za-z][A-Za-z0-9]*>", seg):
                print(f"  {rel}:{i} [{kind}] <...> wewnatrz math -> {m.group(0)}")
                problems += 1
        for pattern, desc in RISKY_TEXT:
            for i, line in enumerate(text.splitlines(), 1):
                if "$" not in line:
                    continue
                for m in re.finditer(pattern, line):
                    frag = line[max(0, m.start() - 30): m.end() + 30].strip()
                    print(f"  {rel}:{i} {desc} -> ...{frag}...")
                    problems += 1
        for i, line in enumerate(text.splitlines(), 1):
            if line.count("$") % 2 == 1 and "$$" not in line:
                print(f"  {rel}:{i} nieparzysta liczba $ w linii (math rozciagnieta na 2 wiersze)")
                problems += 1
            if line.strip().startswith("|") and "$$" in line:
                print(f"  {rel}:{i} wyswietlanie $$ wewnatrz wiersza tabeli")
                problems += 1
            # | wewnatrz math w wierszu tabeli rozbija tabele
            if TABLE_MATH_PIPE and line.strip().startswith("|"):
                for seg in re.findall(r"\$([^$\n]+)\$", line):
                    if re.search(r"(?<!\\)\|", seg):
                        print(f"  {rel}:{i} znak | wewnatrz math w tabeli -> ${seg[:60]}$")
                        problems += 1
    print(f"  -> problemow: {problems}")
    return problems


def report_quotes(verbose: bool = True) -> int:
    print("=== 2. BLOKI CYTATOW (info-kramki) ===")
    total = 0
    blocks: dict[str, int] = {}
    for path in iter_md():
        lines = path.read_text(encoding="utf-8").splitlines()
        rel = path.relative_to(ROOT)
        i = 0
        while i < len(lines):
            if lines[i].lstrip().startswith(">"):
                start = i
                while i < len(lines):
                    if lines[i].lstrip().startswith(">"):
                        i += 1
                    elif lines[i].strip() == "" and i + 1 < len(lines) and lines[i + 1].lstrip().startswith(">"):
                        i += 1
                    else:
                        break
                first = lines[start].lstrip("> ").strip()
                blocks[first[:60]] = blocks.get(first[:60], 0) + 1
                total += 1
                if verbose:
                    print(f"  {rel}:{start + 1}-{i} | {first[:100]}")
            else:
                i += 1
    print(f"  -> blokow: {total}")
    print("\n  Najczestsze pierwsze linie:")
    for key, count in sorted(blocks.items(), key=lambda kv: -kv[1])[:20]:
        print(f"    {count:>3}x {key}")
    return total


def report_motivation() -> int:
    print("=== 3. FRAZY MOTYWACYJNE / META ===")
    hits = 0
    for path in iter_md():
        text = strip_code(path.read_text(encoding="utf-8"))
        rel = path.relative_to(ROOT)
        for i, line in enumerate(text.splitlines(), 1):
            if any(re.search(w, line) for w in MOTIVATION):
                print(f"  {rel}:{i} | {line.strip()[:110]}")
                hits += 1
    print(f"  -> trafien: {hits}")
    return hits


def main() -> int:
    args = set(sys.argv[1:])
    if not args:
        report_math()
        print()
        report_quotes(verbose=False)
        print()
        report_motivation()
        return 0
    if "--math" in args:
        return 1 if report_math() else 0
    if "--quotes" in args:
        return 1 if report_quotes() else 0
    if "--mot" in args:
        return 1 if report_motivation() else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())

