# Kod — symulatory i weryfikacja numeryczna

Wszystkie skrypty korzystają **wyłącznie z NumPy** (matplotlib opcjonalnie, tylko
wykresy). Dzięki temu działają offline, bez instalowania Qiskita czy dostępu do
chmury.

## Wymagania

```powershell
python -m pip install -r kod/requirements.txt
```

lub ręcznie: `python -m pip install numpy` (+ opcjonalnie `matplotlib`).

## Uruchamianie

```powershell
python kod/verify_all.py               # wszystko naraz + raport OK/FAIL
python kod/p4_cnot_ry.py               # pojedynczy skrypt
```

## Konwencje code'u

- Kolejność kubitów **małoendianowa**: stan $\lvert q_{n-1}\dots q_1q_0\rangle$ ma
  indeks $q_0+2q_1+\dots+2^{n-1}q_{n-1}$; bramka na kubicie $k$ to $I\otimes\dots\otimes G\otimes\dots\otimes I$
  z $G$ na pozycji $k$-tej **od prawej** (najmniej znaczącej).
- Wektory stanu: `numpy.ndarray`, kształt `(2**n,)` (wektor jednowymiarowy).
- Macierze: `(2**n, 2**n)`; składanie iloczynu tensorowego przez `numpy.kron`.
- Każdy skrypt kończy się funkcją `main()` z asercjami i wypisuje `OK`/`FAIL`.

## Spis skryptów

| Plik | Temat | Rozdział teorii |
| --- | --- | --- |
| `simulator.py` | silnik obwodów: bramki 1- i 2-kubitowe, pomiary, rozkład wyników | [06](../teoria/06-kubity-bramki-obwody-pomiary.md) |
| `p1_studnia.py` | nieskończona studnia potencjału: normalizacja, $P(E_n)$, $\langle E\rangle$, $\langle x\rangle$ | [05](../teoria/05-podstawy-mechaniki-kwantowej.md) |
| `p2_polaryzatory.py` | prawo Malusa: wiązka vs pojedynczy foton | [05](../teoria/05-podstawy-mechaniki-kwantowej.md) |
| `p3_hzh.py` | $HZH=X$, rozkład wyników pomiaru | [06](../teoria/06-kubity-bramki-obwody-pomiary.md) |
| `p4_cnot_ry.py` | stan po CNOT, $P_{00}\dots P_{11}$, $\langle Z\otimes Z\rangle$, splątanie | [06](../teoria/06-kubity-bramki-obwody-pomiary.md) |
| `grover.py` | Grover dla $N=4,8$: iteracje i prawdopodobieństwo sukcesu | [08](../teoria/08-algorytmy-kwantowe.md) |
| `chsh.py` | CHSH: maksimum $2\sqrt2$, symulacja pomiarów | [09](../teoria/09-splatanie-i-twierdzenie-bella.md) |
| `bb84.py` | BB84 z podsłuchem: QBER vs odsetek podsłuchu | [10](../teoria/10-kryptografia-kwantowa.md) |
| `teleportacja.py` | teleportacja: pełna macierz i korekty | [19](../teoria/19-ponad-program-algorytmy-zaawansowane-i-granice.md) |
| `korekcja_3bit.py` | syndromy i korekta kodu powtarzalnego 3-kubitowego | [13](../teoria/13-korekcja-i-mitygacja-bledow.md) |
| `metrologia_faza.py` | estymacja fazy: $\Delta\varphi\propto1/\sqrt N$ vs $1/N$ | [11](../teoria/11-metrologia-kwantowa.md) |
| `analiza_danych.py` | dopasowanie, $\chi^2$, bootstrap, FFT | [16](../teoria/16-analiza-danych-i-obliczenia-naukowe.md) |
| `verify_all.py` | uruchamia wszystko i drukuje tabelę wyników | — |

## Wynik przykładowy

```
$ python kod/verify_all.py
=== WERYFIKACJA NUMERYCZNA PRZEWODNIKA ===
------------------------------------------------------------------------------
[OK  ] simulator.py           - [OK] simulator.py: wszystkie testy wewnetrzne przeszly
[OK  ] p1_studnia.py          - WYNIK: P1 OK
[OK  ] p2_polaryzatory.py     - WYNIK: P2 OK
[OK  ] p3_hzh.py              - WYNIK: P3 OK
[OK  ] p4_cnot_ry.py          - WYNIK: P4 OK
[OK  ] grover.py              - WYNIK: Grover OK
[OK  ] chsh.py                - WYNIK: CHSH OK
[OK  ] bb84.py                - WYNIK: BB84 OK
[OK  ] teleportacja.py        - WYNIK: Teleportacja OK
[OK  ] korekcja_3bit.py       - WYNIK: korekcja 3-bit OK
[OK  ] metrologia_faza.py     - WYNIK: metrologia OK
[OK  ] analiza_danych.py      - WYNIK: analiza danych OK
------------------------------------------------------------------------------
WYNIK: 12/12 OK
```

