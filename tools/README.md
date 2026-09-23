# Narzędzia kontroli jakości

Skrypty nie są częścią materiału do nauki — służą do utrzymania repozytorium.
Wszystkie uruchamia się z katalogu głównego repo.

| Skrypt | Do czego służy | Oczekiwany wynik |
| --- | --- | --- |
| `verify_all.py` (w `kod/`) | uruchamia 12 skryptów numerycznych z `kod/` | `12/12 OK` |
| `check_links.py` | sprawdza wszystkie linki relatywne w plikach `.md` | `wszystkie linki ... poprawne` |
| `audit_github_math.py` | sprawdza, czy matematyka renderuje się na GitHubie (bloki `$$` w akapicie, `$$` w tabeli, `\|` w tabeli) | `problemow: 0` |
| `audit_content.py --math` | skladnia LaTeX: ryzykowne makra, `\left`/`\right`, nieparzyste `$` | `problemow: 0` |
| `audit_content.py --mot` | pozostałości komentarzy motywacyjnych i meta | `trafien: 0` |
| `verify_structure.py` | sekcje 1–8 w rozdziałach, zadania Z-NN i ich rozwiązania, 10 zadań w PD | `problemow: 0` |
| `verify_math_integrity.py [--base REF]` | porównuje wszystkie wzory z wersją z gita (kontrola, że redakcja nie zmieniła wzorów) | `0` plików z różnicą |
| `fix_math_wrap.py [--apply]` | scala matematykę inline złamaną na dwa wiersze | raport scalen |
| `fix_block_math.py [--apply]` | wstawia puste linie wokół bloków `$$` (wymóg GitHuba) | raport wstawień |
| `probe_github_math.py` | sonda: wysyła próbki do `api.github.com/markdown` i pokazuje HTML z renderera | werdykt dla każdego przypadku |

Reguły zapisu matematyki (z uzasadnieniem i tabelą przypadków):
[docs/03-konwencje-i-notacja.md, sekcja 6](../docs/03-konwencje-i-notacja.md).
