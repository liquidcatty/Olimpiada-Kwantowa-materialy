# 14. Narzędzia informatyczne

> **Warsztat źródłowy:** „Narzędzia informatyczne” (warsztat organizatora).
> **Czas nauki:** ~4 h teorii + ~5 h zadań.
> **Wymagana wiedza wstępna:** obsługa komputera; notacja i odsyłacze w [konwencjach](../docs/03-konwencje-i-notacja.md).

## 1. Po co to jest

Etap I jest zdalny i pisemny: rozwiązania wysyła się przez system (PDF, `.ipynb`, `.py`,
rękopisy jako JPEG). Co roku część uczestników traci punkty nie na fizyce, lecz na rzemiośle:
nieczytelny skan, brakujący plik `.py`, zniknięte wyniki notebooka, dane osobowe w pracy
(prace są anonimowe!), brak potwierdzenia wysyłki przed terminem. Ten rozdział to
„narzędziownia”: terminal, git, Markdown/LaTeX, PDF, Jupyter, środowiska wirtualne, praca
zdalna (SSH, SLURM), bezpieczeństwo i zasady używania narzędzi symbolicznych.

> **Ponad program:** to jedyne miejsce w programie, gdzie pojawia się praca na klastrze
> (HPC) i system kolejek SLURM — przydatne w finałowych zadaniach symulacyjnych i w nauce.

## 2. Najważniejsze definicje

- **Terminal / powłoka (shell)**: program do wpisywania poleceń; na Windows **PowerShell**
  (wersja 5.1), na Linuksie/macOS `bash`/`zsh`; Git Bash łączy oba światy.
- **Polecenie**: `program argumenty --opcje`; zwraca **kod wyjścia** (`0` = sukces).
- **Potok `|`** przekazuje wyjście dalej; **przekierowanie `>`/`>>`** zapisuje do pliku.
- **Ścieżka (path)**: `.` = katalog bieżący, `..` = nadrzędny.
- **Repozytorium git**: katalog z historią zmian (`.git/`). **Commit** = zapisany stan;
  **branch** = gałąź; **remote** = kopia zdalna; **pull request** = propozycja scalenia.
- **`.gitignore`**: lista plików nieśledzonych przez git (`__pycache__/`, `.venv/`).
- **Markdown**: lekki format tekstowy; **LaTeX**: skład wzorów (`$...$`, `$$...$$`).
- **pandoc**: konwersja Markdown → PDF/DOCX/HTML.
- **`.ipynb`**: notebook Jupyter (kod + wyniki + opis); **jądro** = proces wykonujący kod;
  **Restart & Run All** = odtworzenie wyników od zera.
- **`venv`**: izolowane środowisko Pythona; **`requirements.txt`**: lista zależności z wersjami.
- **SSH**: szyfrowane logowanie zdalne (klucz = para plików); **SCP/SFTP/rsync**: kopiowanie.
- **HPC / klaster**: komputer obliczeniowy z kolejką; **SLURM**: `sbatch` (zlecenie),
  `squeue` (podgląd), `scancel` (anulowanie).
- **RODO/anonimowość**: wyniki publikowane pod **kodem uczestnika**, w pracy nie podaje się
  imienia, nazwiska ani szkoły.

## 3. Teoria krok po kroku

### 3.1 Organizacja pracy i terminal

Trzymaj jedną strukturę katalogów: `teoria/` (notatki), `zadania/`, `rozwiazania/` (jedno
zadanie = jeden plik: `z14-1.md`), `kod/` (skrypty uruchamialne jako `python kod/plik.py`),
`dane/` (nigdy nie nadpisuj oryginałów), `wyniki/`, `wyslane/` (dokładnie to, co poszło do
systemu). Nazwy plików bez polskich znaków i spacji.

| Zadanie | PowerShell | bash |
| --- | --- | --- |
| lista plików | `Get-ChildItem` (`ls`) | `ls -la` |
| katalog / kopiowanie / usuwanie | `New-Item -ItemType Directory`, `Copy-Item`, `Remove-Item` | `mkdir`, `cp`, `rm` |
| zawartość pliku | `Get-Content plik.md` | `cat plik.md` |
| szukanie w plikach | `Select-String -Pattern "TODO" -Path *.py` | `grep -n "TODO" *.py` |
| liczba wierszy | `(Get-Content p.md).Count` | `wc -l p.md` |
| kod wyjścia | `$LASTEXITCODE` | `echo $?` |

**Pułapki Windowsa.** (1) PowerShell 5.1 **nie zna `&&`** (jest w wersji 7) — używaj `;` lub
`if ($?) { ... }`. (2) `>` w PowerShell 5.1 zapisuje UTF-16; dla UTF-8 użyj
`| Out-File -Encoding utf8 plik.txt`. (3) Polskie znaki w konsoli: `chcp 65001` albo zapis
wyników do pliku UTF-8. Skrypt wsadowy: `powershell -ExecutionPolicy Bypass -File uruchom.ps1`.

### 3.2 Git — kontrola wersji

```bash
git status                       # co się zmieniło (najczęstsze polecenie)
git add rozwiazania/z13-1.md     # przygotowanie pliku; git add . = wszystko
git commit -m "Z-13.1: syndrom kodu 3-kubitowego"
git --no-pager log --oneline --graph     # historia
git --no-pager diff              # zmiany niezatwierdzone; --staged = przygotowane
git switch -c poprawki-13        # nowa gałąź; git switch main = powrót
git remote -v ; git push origin main     # adres zdalny i wysłanie
git config --global user.name "Kod Uczestnika"
git config --global user.email "ja@example.com"
git config --global core.autocrlf true   # Windows: końce linii
```

`.gitignore` (wzorzec z tego repozytorium): `__pycache__/`, `*.py[cod]`, `.venv/`,
`*.ipynb_checkpoints/`, `.vscode/`, `*.tmp`. Jeśli przez pomyłkę zacommitowałeś hasło:
`git rm --cached plik` i **natychmiast zmień hasło** (historia bywa publiczna). Praca
zespołowa z opiekunem: gałąź na każde zadanie + pull request, konflikty rozwiązuje się ręcznie.
Wspólne rozwiązywanie zadań jest niedozwolone ([zakres materiału](../docs/02-zakres-materialu.md)) —
git służy do własnej archiwizacji, nie do wymiany rozwiązań.

### 3.3 Markdown, LaTeX i PDF

**Markdown:** `# Tytuł`, listy `-`/`1.`, `**pogrubienie**`, `*kursywa*`, `` `kod` ``, tabele
(`| a | b |` plus wiersz `| --- | --- |`), bloki kodu w potrójnych backtickach.

**LaTeX:** `$E=mc^2$` w tekście, `$$\Delta\varphi\ge\frac{1}{\sqrt N}$$` osobno. Najczęstsze:
`\frac{a}{b}`, `\sqrt{x}`, `x^{2}`, `x_{i}`, `\lvert\psi\rangle`, `\langle\phi\vert`,
`\begin{pmatrix}a&b\\c&d\end{pmatrix}`, `\alpha,\beta,\varphi,\theta,\hbar`,
`\sum_{k=1}^{N}`, `\approx`, `\le`, `\cdot`. Przecinek dziesiętny piszemy jako `{,}`.
Nie używaj znaków Unicode dla indeksów i ułamków — „rozjadą się” przy konwersji.

**PDF — trzy drogi.** (1) Eksport z edytora Markdown (np. rozszerzenie *Markdown PDF*
w VS Code). (2) pandoc, najlepszy efekt typograficzny:
```bash
pandoc rozwiazanie.md -o rozwiazanie.pdf --pdf-engine=xelatex -V lang=pl -V geometry:margin=2.5cm
```
(3) LaTeX bezpośrednio — szkielet:
```latex
\documentclass[11pt]{article}
\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}\usepackage[polish]{babel}
\usepackage{amsmath,amssymb}\usepackage[margin=2.5cm]{geometry}
\begin{document}\section*{Z-13.1} Syndrom to $(1,1)$, poprawka $X$ na $q_1$.\end{document}
```
Kompilacja: `pdflatex rozwiazanie.tex` (dwa razy, jeśli są odsyłacze). Word: równania przez
`Alt`+`=`, eksport do PDF — ale **zawsze obejrzyj gotowy PDF** (czcionki bywają zamieniane).

**Co musi być w PDF-ie:** numer zadania, pełny rachunek (nie tylko wynik), wyróżniona
odpowiedź, interpretacja. Bez imienia, nazwiska i szkoły.

### 3.4 Skan i czytelność pracy

Rękopis wysyła się jako zdjęcie/skan (organizator dopuszcza JPEG dla rękopisów).

1. **Format i ostrość.** JPEG (lub PDF ze skanów), $150$–$300$ dpi; kartka wypełnia kadr, ale
   **widać całe narożniki** — obcięty fragment to utracone punkty.
2. **Oświetlenie i tło.** Równomierne światło, ciemny długopis, brak cienia ręki, tło kontrastowe.
3. **Orientacja i kolejność.** Jedna orientacja, strony **ponumerowane**, w kolejności zadań.
4. **Rozmiar i weryfikacja.** Kompresja JPEG $70$–$85\%$; sprawdź limit systemu i otwórz plik
   na telefonie — czy każdy wzór da się odczytać bez powiększania?

### 3.5 Jupyter

Notebook (`.ipynb`) łączy kod, komentarze i wyniki; organizator często dopuszcza go w zadaniach
obliczeniowych. Instalacja i uruchomienie: `python -m pip install jupyterlab`, potem
`jupyter lab` w katalogu projektu (w środowisku warsztatowym Jupyter może nie być zainstalowany —
sprawdź `python -c "import jupyter_client"`).

- **Kolejność wykonania ma znaczenie.** Jupyter wykonuje komórki w kolejności klikania, więc
  łatwo dostać wynik „z przeszłości”. Przed oddaniem pracy: **Restart Kernel → Run All**.
- **Powtarzalność:** ziarno losowości `rng = np.random.default_rng(42)` i wydruk wersji
  bibliotek (`numpy.__version__`).
- **Rozmiar pliku:** duże wykresy i tablice w wynikach „puchną”; kasuj zbędne wyniki albo
  zapisuj dane do plików.
- **Eksport:** `jupyter nbconvert --to html rozwiazania/z14.ipynb`; dołącz też wersję `.py`.

### 3.6 Środowiska wirtualne i pakiety

```powershell
python -m venv .venv                          # izolowane środowisko projektu
.\.venv\Scripts\Activate.ps1                  # aktywacja (Windows)
# jeśli pojawi się błąd o zasadach wykonywania:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
python -m pip install --upgrade pip
python -m pip install numpy sympy
python -m pip freeze > requirements.txt       # zamrożone wersje
python -m pip install -r kod/requirements.txt # odtworzenie u kogoś innego
deactivate
```

Na Linuksie/macOS: `source .venv/bin/activate`. Warto znać `conda`, `uv` (szybki instalator)
i `pipx`. Zawsze używaj `python -m pip` — instaluje w to samo środowisko, z którego uruchamiasz
kod. Kontrola: `python -c "import numpy; print(numpy.__version__)"`.

### 3.7 Praca zdalna: SSH, SCP i SLURM

```bash
ssh user@klaster.edu.pl                  # logowanie
ssh-keygen -t ed25519 -C "olimpiada-2027"  # para kluczy (~/.ssh/id_ed25519 + .pub)
ssh-copy-id user@klaster.edu.pl          # klucz publiczny na serwer
scp kod/korekcja_3bit.py user@klaster:~/projekt/       # kopiowanie pliku
scp -r dane user@klaster:~/projekt/                    # kopiowanie katalogu
rsync -avz --progress dane/ user@klaster:~/projekt/dane/   # szybkie, wznawialne
```

Klucz prywatny **nigdy** nie opuszcza Twojego komputera. W `~/.ssh/config` zapisz skrót
(`Host klaster`, `HostName`, `User`), żeby potem pisać `ssh klaster`.

**SLURM.** Na klastrze ciężkie zadania zleca się kolejce (nie liczy się ich na węźle logowania).
Plik `job.sh`:

```bash
#!/bin/bash
#SBATCH --job-name=syndrom
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=slurm-%j.out
module load python/3.11
python kod/korekcja_3bit.py
```

Polecenia: `sbatch job.sh` (wypisuje `Submitted batch job 12345`), `squeue -u $USER` (kolejka),
`scancel 12345` (anulowanie), `sinfo` (stan klastra), `salloc`/`srun` (sesja interaktywna).
Wynik trafia do `slurm-12345.out` (`%j` = numer zadania).

### 3.8 Bezpieczeństwo haseł i RODO

- **Hasła:** menedżer haseł (Bitwarden, KeePassXC), inne hasło do każdej usługi, wszędzie
  włączone **2FA** (konto Olimpiady, e-mail, GitHub).
- **Klucze SSH:** prywatny klucz zostaje u Ciebie i ma frazę hasła; udostępniasz tylko `.pub`.
- **Sekrety w kodzie:** nie wpisuj haseł, tokenów i kluczy API do `.py`/`.ipynb` — trzymaj je
  w zmiennych środowiskowych lub w pliku `.env` wpisanym do `.gitignore`. Ujawniony sekret
  natychmiast zmień: historia git bywa publiczna.
- **RODO i anonimowość:** prace ocenia się anonimowo, wyniki publikuje się pod **kodem
  uczestnika**; w pracy nie umieszczaj imienia, nazwiska ani szkoły, a dane osobowe podawaj
  wyłącznie w systemie rejestracyjnym organizatora.
- **Użycie AI i narzędzi:** w Etapie I AI jest dozwoloną **pomocą**, ale nie może wytworzyć
  całej pracy; użycie trzeba opisać i oznaczyć. W finale obowiązuje tylko lista materiałów
  dopuszczonych w ZOZ.

### 3.9 Kalkulator symboliczny (sympy, Wolfram Alpha)

Sympy to biblioteka Pythona do rachunku symbolicznego; Wolfram Alpha to narzędzie online.
Typowy wzorzec (ze sprawdzeniem informacji Fishera z rozdziału 11):

```python
import sympy as sp
phi = sp.symbols('phi', real=True)
p_plus, p_minus = sp.cos(phi/2)**2, sp.sin(phi/2)**2
print(sp.simplify(p_plus + p_minus))              # 1
F = sp.diff(p_plus, phi)**2/p_plus + sp.diff(p_minus, phi)**2/p_minus
print(sp.simplify(sp.trigsimp(F)))                # 1
x = sp.Symbol('x')
print(sp.integrate(sp.exp(-x)*x**2, (x, 0, sp.oo)))   # 2
```

**Kiedy wolno, a kiedy nie.** W Etapie I wolno (kalkulator, komputer, AI to dozwolone pomoce),
ale rachunek musi być **widoczny w pracy**. W finale wolno tylko to, co wymienia ZOZ — zakładaj
domyślnie kartkę i prosty kalkulator, więc **trenuj rachunek ręczny**. Każdy wynik symboliczny
sprawdzaj numerycznie (podstaw liczbę) i kontroluj jednostki: kalkulator nie wie, czy liczysz
prawdopodobieństwo, energię czy bezwymiarową fazę.

### 3.10 Check-lista „jak oddać pracę, żeby nie stracić punktów”

- [ ] Każde zadanie w osobnym pliku, nazwa bez polskich znaków i spacji.
- [ ] Pełny rachunek (nie tylko wynik), wyróżniona odpowiedź, interpretacja, jednostki.
- [ ] Prawdopodobieństwa sumują się do $1$; sprawdzone przypadki graniczne.
- [ ] **Brak danych osobowych** (praca jest anonimowa).
- [ ] Kod `.py` uruchamia się na innym komputerze (bez brakujących plików danych).
- [ ] Notebook: **Restart Kernel → Run All** wykonany, rozmiar pliku sensowny.
- [ ] PDF/JPEG czytelny: ponumerowane strony, widoczne narożniki, ostre wzory.
- [ ] Opisane użycie AI i narzędzi; plik z kodem dołączony, gdy wymagany.
- [ ] Wysłane z zapasem czasu, potwierdzenie w panelu, kopia w `wyslane/`.

## 4. Przykłady rozwiązane

### Przykład 14.1 (łatwy): od zadania do wysłanej pracy

**Cel:** przygotować i wysłać rozwiązanie Z-13.1 jako PDF.
```powershell
New-Item -ItemType Directory rozwiazania, wyslane -ErrorAction SilentlyContinue
notepad rozwiazania\z13-1.md        # albo: code rozwiazania\z13-1.md
python -c "import numpy as np; print(np.log(0.5)/np.log(0.997))"   # kontrola rachunku: 231.4
git add rozwiazania/z13-1.md
git commit -m "Z-13.1: syndrom kodu 3-kubitowego"
pandoc rozwiazania\z13-1.md -o rozwiazania\z13-1.pdf --pdf-engine=xelatex -V lang=pl
Copy-Item rozwiazania\z13-1.pdf wyslane\z13-1-2027-01-15.pdf
```
**Odpowiedź (efekt):** `z13-1.pdf` z pełnym rachunkiem, wersja w historii git i kopia w
`wyslane/` z datą — a w systemie Olimpiady potwierdzenie wysyłki.
*Interpretacja:* `$0{,}997^n=0{,}5$ daje $n=231{,}4$, czyli granica $50\%$ wypada po 231 bramkach
(rozdział 12) — sprawdzenie jednym poleceniem to standard pracy.

### Przykład 14.2 (trudniejszy): notebook, środowisko, powtarzalność

**Cel:** rozwiązanie obliczeniowe, które recenzent uruchomi u siebie jedną komendą.
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install numpy sympy jupyterlab
python -m pip freeze > requirements.txt      # np. numpy==2.4.6, sympy==1.14.0
jupyter lab                                   # tworzymy rozwiazania\z14.ipynb
jupyter nbconvert --to html rozwiazania\z14.ipynb
```
W notebooku: pierwsza komórka z ziarnem `rng = np.random.default_rng(42)`, ostatnia — wydruk
wersji bibliotek; przed eksportem **Restart Kernel → Run All**.
**Odpowiedź (efekt):** `z14.ipynb`, `z14.py`, `z14.html`, `requirements.txt`; odtworzenie:
`python -m pip install -r requirements.txt`.
*Interpretacja:* powtarzalność jest kryterium oceny — jeśli recenzent nie może uruchomić kodu,
nie może przyznać punktów za metodę obliczeniową.

## 5. Typowe pułapki

1. **Praca bez pełnego rachunku.** Sam wynik to najwyżej połowa punktów (rozdział [04 strategii](../docs/04-strategia-rozwiazywania-zadan.md)).
2. **Kolejność komórek w notebooku.** Wyniki „z przeszłości” nie odtwarzają się po Restart & Run All — i recenzent to zobaczy.
3. **Brak pliku z kodem.** Zadanie programistyczne bez `.py`/`.ipynb` nie ma jak zostać ocenione za metodę.
4. **Dane osobowe w pracy.** Prace są anonimowe; podpisanie pracy może oznaczać odrzucenie.
5. **Sekrety w repozytorium.** Hasło/token raz wypchnięty do GitHuba jest ujawniony — trzeba je zmienić, nie „usunąć pliku”.
6. **Nieuważne skany.** Obcięte narożniki, cień ręki, nieostre wzory, brak numeracji stron — punkty tracone bezpowrotnie.
7. **Praca na węźle logowania klastra.** Ciężkie obliczenia uruchomione po SSH mogą zostać zabite i zablokować konto — używaj `sbatch`.

## 6. Zadania (Z-14)

**Z-14.1.** Terminal. (a) Podaj polecenia (PowerShell i bash) tworzące katalogi `rozwiazania` i `wyniki`. (b) Policz liczbę wierszy wszystkich plików `.md` w katalogu. (c) Znajdź wszystkie pliki `.py` zawierające słowo `assert` i wyjaśnij, po co sprawdzać kod wyjścia.

**Z-14.2.** Git. (a) Wyjaśnij rolę `.gitignore` i podaj trzy typowe wpisy dla projektu w Pythonie. (b) Wypisz kolejność poleceń od zmiany w pliku do wysłania na GitHub. (c) Co zrobić, jeśli przez pomyłkę zacommitowałeś plik z hasłem? Podaj polecenia i uzasadnij, dlaczego trzeba też zmienić hasło.

**Z-14.3.** Markdown i PDF. (a) Zapisz w LaTeX-u: $\Delta\varphi\ge\frac{1}{\sqrt N}$ oraz macierz Pauliego $Y$. (b) Podaj komendę pandoc tworzącą PDF z pliku `zadanie.md` z polskimi znakami. (c) Wymień trzy rzeczy, które muszą znaleźć się w wysyłanym PDF-ie, i dwie, których być nie może.

**Z-14.4.** Notebook i środowisko. (a) Podaj polecenia tworzące i aktywujące `venv` w Windows oraz zapisujące wersje bibliotek. (b) Po co dołączać `requirements.txt` i eksport `.py`? (c) Wyjaśnij, dlaczego przed oddaniem notebooka trzeba zrobić „Restart Kernel → Run All”.

**Z-14.5.** Praca zdalna i SLURM. (a) Napisz plik `job.sh` zlecający skrypt `kod/analiza.py` na 1 węzeł, 4 rdzenie, 8 GB pamięci i 30 minut. (b) Podaj polecenia zgłoszenia, sprawdzenia kolejki i anulowania zadania. (c) Wyjaśnij, gdzie znajdziesz wynik obliczeń i co robi wzorzec `%j`.

**Z-14.6. [★]** Skan i oddanie pracy. (a) Wymień pięć wymagań dobrego skanu rękopisu. (b) Opisz, jak sprawdzisz, że plik jest czytelny, zanim go wyślesz. (c) Wypisz pięć punktów check-listy z 3.10 i oceń, które najczęściej są lekceważone.

## 7. Wskazówki do zadań

- **Z-14.1.** (a) `New-Item -ItemType Directory` / `mkdir -p`; (b) `Get-ChildItem -Recurse -Filter *.md | Measure-Object -Line` / `wc -l *.md`; (c) `Select-String -Pattern assert -Path *.py -List` / `grep -l "assert" *.py`.
- **Z-14.2.** (b) `status → add → commit → push`; (c) `git rm --cached` usuwa plik z indeksu, ale **nie z historii** poprzednich commitów.
- **Z-14.3.** (a) `$\Delta\varphi\ge\frac{1}{\sqrt N}$`, `$\begin{pmatrix}0&-i\\i&0\end{pmatrix}$`; (b) `--pdf-engine=xelatex`; (c) patrz 3.3 i 3.4.
- **Z-14.4.** (a) patrz blok kodu w 3.6; (b) powtarzalność wersji; (c) kolejność wykonania komórek nie jest zapisana w pliku.
- **Z-14.5.** (a) wzór z 3.7; (b) `sbatch`, `squeue -u $USER`, `scancel`; (c) plik `slurm-<numer>.out`.
- **Z-14.6.** (a) patrz 3.4; (c) najczęściej lekceważy się numerację stron i brak danych osobowych.

## 8. Co dalej

- **Oprogramowanie kwantowe** — [rozdział 15](15-oprogramowanie-kwantowe.md): Qiskit, Cirq, PennyLane i wysyłanie obwodów do chmury.
- **Korekcja i mitygacja błędów** — [rozdział 13](13-korekcja-i-mitygacja-bledow.md): macierz kalibracji i ZNE, które liczy się w tych samych narzędziach.
- **Analiza danych** — [rozdział 16](16-analiza-danych-i-obliczenia-naukowe.md): pandas, dopasowania, bootstrap.
- Ćwiczenia wykonuj wprost w terminalu repozytorium: `python kod/verify_all.py` uruchamia wszystkie skrypty i pokazuje tabelę `OK`/`FAIL`.
- Środowisko warsztatowe: Python 3.11, numpy 2.4.6, sympy 1.14.0; `matplotlib` i Jupyter może wymagać doinstalowania.




