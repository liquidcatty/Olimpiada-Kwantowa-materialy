# Rozwiązania do rozdziału 14

## Z-14.1

(a) Utworzenie dwóch katalogów:
```powershell
New-Item -ItemType Directory rozwiazania, wyniki     # PowerShell (wiele ścieżek naraz)
New-Item -ItemType Directory rozwiazania -ErrorAction SilentlyContinue   # gdy katalog może istnieć
```
```bash
mkdir -p rozwiazania wyniki                          # bash (-p = bez błędu, gdy istnieje)
```

(b) Liczba wierszy wszystkich plików `.md` w katalogu (rekurencyjnie):
```powershell
(Get-ChildItem -Recurse -Filter *.md | Get-Content).Count        # np. 10708
```
```bash
wc -l $(find . -name "*.md") | tail -n 1
```
Uwaga: liczba zależy od tego, czy pliki mają końcowy znak nowej linii, i obejmuje puste wiersze.

(c) Pliki `.py` zawierające `assert`:
```powershell
Select-String -Path kod\*.py -Pattern "assert" -List      # -List = tylko pierwsze trafienie w pliku
```
```bash
grep -l "assert" kod/*.py
```
Kod wyjścia sprawdzamy, bo **skrypt ma sygnalizować porażkę maszynie**, nie tylko człowiekowi:
`python kod/korekcja_3bit.py; echo $LASTEXITCODE` wypisuje `0` przy sukcesie i wartość niezerową
przy wyjątku. Na tym opiera się automatyzacja (`.github/workflows/verify.yml`): jeśli którykolwiek
skrypt zgłosi `AssertionError`, kod wyjścia jest $\ne0$ i cała weryfikacja „czerwienieje”.

**Odpowiedź:** (a) `New-Item -ItemType Directory` / `mkdir -p`; (b) `(Get-ChildItem -Recurse -Filter *.md | Get-Content).Count` / `wc -l $(find . -name "*.md")`; (c) `Select-String -Pattern "assert" -List` / `grep -l`, a kod wyjścia `$LASTEXITCODE`/`$?` jest sygnałem dla automatyzacji.

*W praktyce:* trzy polecenia z tego zadania (tworzenie katalogów, liczenie linii, wyszukiwanie
wzorca) pokrywają większość codziennej pracy z repozytorium materiałów.

## Z-14.2

(a) `.gitignore` to lista wzorców plików, których git **nie śledzi** (nie pojawiają się
w `git status` ani w commitach). Trzy typowe wpisy dla Pythona:
```
__pycache__/          # skompilowane pliki .pyc
.venv/                # środowisko wirtualne (setki plików bibliotek)
.env                  # sekrety (hasła, tokeny) - nigdy w repozytorium
```
(przydatne też: `*.ipynb_checkpoints/`, `.vscode/`, `*.tmp`).

(b) Kolejność: `git status` (co się zmieniło) → `git add plik` (przygotowanie) →
`git commit -m "opis"` (zapis w historii) → `git push origin main` (wysłanie na zdalne
repozytorium). Sprawdzenie: `git --no-pager log --oneline`.

(c) Gdy plik z hasłem trafił do commita:
```bash
git rm --cached haslo.txt          # usuwa z indeksu, zostawia w katalogu roboczym
echo "haslo.txt" >> .gitignore     # blokuje na przyszłość
git commit -m "usunięcie pliku z sekretem z repozytorium"
```
`git rm --cached` **nie usuwa pliku z historii poprzednich commitów** — hasło nadal jest
w `git log`. Dlatego obowiązkowe jest **natychmiastowe unieważnienie i zmiana hasła** (rotacja
klucza/tokenu). Jeśli repozytorium jest publiczne, trzeba dodatkowo przepisać historię
(`git filter-repo`) i zmusić wszystkich współpracowników do ponownego klonowania.

**Odpowiedź:** (a) lista nieśledzonych plików, wzorce jak `__pycache__/`, `.venv/`, `.env`;
(b) `status → add → commit → push`; (c) `git rm --cached` + `.gitignore` + **zmiana hasła**
(historia commitów przechowuje sekret).

*W praktyce:* żadne narzędzie nie „odzyska” sekretu z cudzego repozytorium — jedyną skuteczną
reakcją jest rotacja poświadczeń.

## Z-14.3

(a) W LaTeX-u:
```latex
$\Delta\varphi \ge \frac{1}{\sqrt{N}}$
$\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$
```
(Preferowany zapis w tym repozytorium: `\lvert\psi\rangle`, `\frac{1}{\sqrt N}` bez nawiasów
w mianowniku, przecinek dziesiętny jako `{,}`.)

(b) Komenda pandoc (pandoc + `xelatex` obsługują polskie znaki):
```bash
pandoc zadanie.md -o zadanie.pdf --pdf-engine=xelatex -V lang=pl -V geometry:margin=2.5cm
```

(c) **Musi być:** (1) numer zadania, (2) pełny rachunek z uzasadnieniem, (3) wyróżniona
odpowiedź z interpretacją i jednostkami. **Nie może być:** (1) danych osobowych (imię, nazwisko,
szkoła — prace są anonimowe), (2) treści wygenerowanej w całości przez AI bez opisu użycia
(regulamin Etapu I wymaga czytelnego oznaczenia).

**Odpowiedź:** (a) `$\Delta\varphi\ge\frac{1}{\sqrt N}$` i
`$\begin{pmatrix}0&-i\\i&0\end{pmatrix}$`; (b) `pandoc ... --pdf-engine=xelatex -V lang=pl`;
(c) numer zadania + rachunek + odpowiedź; bez danych osobowych i nieoznaczonego AI.

*W praktyce:* `xelatex` rozwiązuje 90% problemów z polskimi znakami i wzorami; `pdflatex`
wymaga dodatkowo `[T1]{fontenc}` i `[utf8]{inputenc}`.

## Z-14.4

(a) Utworzenie i aktywacja środowiska (Windows) oraz zapis wersji:
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   # gdy skrypt aktywacji jest blokowany
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy sympy
python -m pip freeze > requirements.txt
```
(Linux/macOS: `python3 -m venv .venv` i `source .venv/bin/activate`.)

(b) `requirements.txt` zapisuje **konkretne wersje** bibliotek, dzięki czemu wynik jest
odtwarzalny (numpy 2.4.6 u każdego). Eksport `.py` z notebooka daje kod czytelny i uruchamialny
bez Jupytera — recenzent może go obejrzeć i przetestować z linii poleceń.

(c) Notebook zapisuje **wyniki**, ale nie kolejność wykonania komórek. Bez „Restart Kernel →
Run All” obraz w pliku może pochodzić z nieaktualnego stanu pamięci (usunięte zmienne, stare
wartości po edycji). Odpowiednik kontroli rachunku w zadaniu fizycznym.

**Odpowiedź:** (a) jak wyżej; (b) dla odtwarzalności wersji i czytelności kodu; (c) bo kolejność
wykonania komórek nie jest zapisana w pliku — trzeba wymusić przebieg od zera.

*W praktyce:* `python -m pip freeze` w chwili oddania pracy to najprostszy sposób, by recenzent
mógł odtworzyć dokładnie Twoje liczby.

## Z-14.5

(a) Plik `job.sh` zlecający `kod/analiza.py` (1 węzeł, 4 rdzenie, 8 GB, 30 minut):
```bash
#!/bin/bash
#SBATCH --job-name=analiza
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=slurm-%j.out
module load python/3.11
python kod/analiza.py
```
Format `HH:MM:SS` w `--time`; `--cpus-per-task=4` wymaga, by skrypt faktycznie korzystał
z 4 wątków (np. `OMP_NUM_THREADS=4`).

(b) Zgłoszenie, podgląd i anulowanie:
```bash
sbatch job.sh          # -> Submitted batch job 12345
squeue -u $USER        # stan kolejki: PD (oczekuje), R (liczy), CG (kończy)
scancel 12345          # anulowanie zadania o numerze 12345
sinfo                  # stan partycji klastra
```

(c) Wynik trafia do pliku `slurm-12345.out` (standardowe wyjście zadania; `--error` wskazuje
osobny plik na błędy). Wzorzec `%j` jest zastępowany numerem zadania, więc każde uruchomienie
ma własny plik i nie nadpisuje poprzedniego.

**Odpowiedź:** (a) jak wyżej; (b) `sbatch` → `squeue -u $USER` → `scancel <id>`; (c) plik
`slurm-<id>.out`, a `%j` to numer zadania nadany przez kolejkę.

*W praktyce:* limity `--mem` i `--time` nie są „sugestią”: przekroczenie pamięci zabija zadanie
(`OUT_OF_MEMORY`), a przekroczenie czasu — `TIMEOUT`. Ustawiaj je z rozsądnym zapasem.

## Z-14.6

(a) Pięć wymagań dobrego skanu rękopisu:
1. **ostrość** i rozdzielczość $150$–$300$ dpi (tekst czytelny bez powiększania),
2. **widoczne całe narożniki** kartki — nic nie jest obcięte,
3. **równe światło** i kontrastowe tło, bez cienia ręki,
4. **jednolita orientacja** i **ponumerowane strony** w kolejności zadań,
5. **sensowny rozmiar pliku** (JPEG, kompresja $70$–$85\%$, zgodny z limitem systemu).

(b) Weryfikacja przed wysłaniem: otwórz plik **na telefonie**, wykadruj do $100\%$ i spróbuj
odczytać najmniejszy wzór oraz indeks dolny; sprawdź, czy widać wszystkie cztery narożniki
i czy strony są w kolejności; porównaj rozmiar pliku z limitem systemu; na końcu pobierz plik
z systemu (jak zrobi to recenzent) i powtórz sprawdzenie.

(c) Pięć punktów check-listy z 3.10: (1) osobny plik na zadanie, nazwa bez polskich znaków;
(2) pełny rachunek i wyróżniona odpowiedź; (3) brak danych osobowych; (4) kod uruchamialny
poza Twoim komputerem; (5) potwierdzenie wysyłki przed terminem. **Najczęściej lekceważone:**
numeracja stron (i widoczność narożników) oraz anonimowość — a oba kosztują punkty bez
jakiegokolwiek błędu merytorycznego.

**Odpowiedź:** (a) ostrość, narożniki, światło, orientacja/numeracja, rozmiar; (b) test na
telefonie + sprawdzenie narożników i kolejności stron; (c) jak wyżej — najczęściej zaniedbane
są numeracja stron i anonimowość.

*W praktyce:* zasada „najpierw sprawdź plik tak, jak zobaczy go recenzent” dotyczy również
PDF-ów i notebooków, nie tylko skanów.

