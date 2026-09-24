# Narzędzia kontroli jakości

Skrypty nie są częścią materiału do nauki — służą do utrzymania repozytorium.
Uruchamia się je z katalogu głównego repo.

## Kontrole (używane w CI)

| Skrypt | Do czego służy | Oczekiwany wynik |
| --- | --- | --- |
| `kod/verify_all.py` | uruchamia 12 skryptów numerycznych z `kod/` | `12/12 OK` |
| `tools/check_links.py` | sprawdza wszystkie linki relatywne w plikach `.md` | `wszystkie linki ... poprawne` |
| `tools/audit_github_math.py` | czy matematyka renderuje się na GitHubie (blok `$$` po tekście, oba delimitery doklejone, `$$` w tabeli, kreska `\|` w tabeli, inline złamane na dwa wiersze) | `problemow: 0` |
| `tools/audit_github_math.py --self-test` | 16 przypadków kontrolnych: audyt musi flagować błędy i **nie** flagować poprawnych zapisów (w tym przykładów w code-spanach) | `self-test OK` |
| `tools/audit_content.py --math` | składnia LaTeX: `\operatorname`, `\tag`, ryzykowne makra, `\left`/`\right`, nieparzyste `$` | `problemow: 0` |
| `tools/audit_content.py --mot` | pozostałości komentarzy motywacyjnych i meta | `trafien: 0` |
| `tools/verify_structure.py` | sekcje 1–8 w rozdziałach, zadania Z-NN i ich rozwiązania, 10 zadań w PD | `problemow: 0` |
| `tools/verify_math_integrity.py [--base REF]` | porównuje wszystkie wzory z wersją z gita (kontrola, że redakcja nie zmieniła wzorów) | `0` plików z różnicą |

## Narzędzia naprawcze i diagnostyczne

| Skrypt | Do czego służy |
| --- | --- |
| `tools/fix_display_math.py [--apply]` | sprowadza bloki `$$` do formy kanonicznej (`$$` w osobnej linii + puste linie) |
| `tools/fix_math_wrap.py [--apply]` | scala matematykę inline złamaną na dwa wiersze |
| `tools/fix_tex_macros.py [--apply]` | `\operatorname{X}` → `\mathrm{X}`, `\tag{N}` → `\qquad (N)` |
| `tools/probe_github_math.py` | sonda: wysyła próbki do `api.github.com/markdown` i pokazuje HTML z renderera wraz z werdyktem |
| `tools/list_tex_macros.py` | inwentarz makr LaTeX używanych w repo + lista makr ryzykownych |

Reguły zapisu matematyki (z tabelą przypadków i uzasadnieniem):
[docs/03-konwencje-i-notacja.md, sekcja 6](../docs/03-konwencje-i-notacja.md).

