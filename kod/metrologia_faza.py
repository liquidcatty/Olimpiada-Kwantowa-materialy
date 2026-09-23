"""Metrologia kwantowa: estymacja fazy i granice dokladnosci.

Porownujemy:
  * strategie klasyczna: N niezaleznych pomiarow (granica srutowa) ~ 1/sqrt(N),
  * strategie kwantowa ze stanem GHZ/N00N (granica Heisenberga) ~ 1/N,
  * informacje Fishera dla interferometru Macha-Zehndera.

Model: prawdopodobienstwo wyniku zalezy od fazy phi.
  - klasycznie (N fotonow niezaleznie):  p = cos^2(phi/2) na foton,
  - kwantowo (stan N00N):                p = cos^2(N*phi/2).

Uruchomienie:
    python kod/metrologia_faza.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def fisher_information(p_func, phi: float, dphi: float = 1e-7) -> float:
    """Klasyczna informacja Fishera F = sum_i (1/p_i)(dp_i/dphi)^2."""
    p = np.atleast_1d(p_func(phi))
    dp = (np.atleast_1d(p_func(phi + dphi)) - np.atleast_1d(p_func(phi - dphi))) / (2 * dphi)
    mask = p > 1e-14
    return float(np.sum((dp[mask] ** 2) / p[mask]))


def classical_probs(phi: float, n_photons: int = 1) -> np.ndarray:
    """Rozklad dla n niezaleznych fotonow: kazdy z p = cos^2(phi/2)."""
    return np.array([np.cos(phi / 2) ** 2, np.sin(phi / 2) ** 2])


def n00n_probs(phi: float, n_photons: int) -> np.ndarray:
    """Rozklad dla stanu N00N: interferencja o efektywnej fazie N*phi."""
    return np.array([np.cos(n_photons * phi / 2) ** 2, np.sin(n_photons * phi / 2) ** 2])


def main() -> None:
    print("=== Metrologia kwantowa: granica srutowa vs Heisenberga ===")
    phi = 0.1      # nieznana faza (niewielka, zeby przyblizenie bylo dobre)

    # informacja Fishera dla jednego fotonu i granica srutowa
    F1 = fisher_information(lambda p: classical_probs(p), phi)
    print(f"\nF dla 1 fotonu (klasycznie) = {F1:.6f}")
    assert abs(F1 - 1.0) < 1e-4
    print("[OK] F = 1 (dla malej fazy), wiec sigma >= 1/sqrt(N)")

    # informacja Fishera dla stanu N00N
    print("\nporownanie granic dla N fotonow:")
    print(f"{'N':>4} {'sigma klasyczna':>16} {'sigma N00N':>12} {'zysk':>7}")
    for n in (1, 2, 4, 8, 16):
        F_class = n * F1                                   # N niezaleznych fotonow
        s_class = 1 / np.sqrt(F_class)
        F_n00n = fisher_information(lambda p: n00n_probs(p, n), phi)
        s_n00n = 1 / np.sqrt(F_n00n)
        gain = s_class / s_n00n
        print(f"{n:>4} {s_class:>16.6f} {s_n00n:>12.6f} {gain:>7.2f}")
        assert abs(F_n00n - n**2) < 1e-2          # F ~ N^2 -> sigma ~ 1/N
        assert abs(s_n00n - 1 / n) < 1e-3
    print("[OK] klasycznie sigma ~ 1/sqrt(N), ze stanem N00N sigma ~ 1/N")

    # symulacja: estymacja fazy przez N pomiarow
    print("\n(2) Monte Carlo: estymacja fazy przy tym samym budzecie fotonowym")
    print("    Kazda strategia pracuje w swoim optymalnym punkcie (p = 1/2):")
    print("    klasycznie phi = pi/2, dla N00N phi = pi/(2N).")
    print("    (R = 100 eksperymentow na kampanie, K = 400 kampanii)")
    rng = np.random.default_rng(3)
    R, K = 100, 400
    print(f"{'N':>4} {'fotony':>7} {'sigma klass.':>13} {'1/sqrt(M)':>10} "
          f"{'sigma N00N':>11} {'1/(N sqrt R)':>13} {'stosunek':>9} {'sqrt(N)':>8}")
    for n in (4, 8, 16, 32):
        phi_class = np.pi / 2             # optymalna faza dla strategii klasycznej
        phi_n00n = np.pi / (2 * n)        # optymalna faza dla N00N (N*phi/2 = pi/4)
        m = R * n                         # budzet fotonowy (taki sam dla obu strategii)

        # klasycznie: M niezaleznych fotonow, kazdy z p = cos^2(phi/2) = 1/2
        p_class = np.cos(phi_class / 2) ** 2
        k_class = rng.binomial(m, p_class, size=K)
        phi_class_hat = 2 * np.arccos(np.sqrt(np.clip(k_class / m, 0, 1)))
        sigma_class = float(np.std(phi_class_hat))

        # N00N: R eksperymentow po N fotonow, p = cos^2(N*phi/2) = 1/2
        p_n00n = np.cos(n * phi_n00n / 2) ** 2
        k_n00n = rng.binomial(R, p_n00n, size=K)
        phi_n00n_hat = 2 * np.arccos(np.sqrt(np.clip(k_n00n / R, 0, 1))) / n
        sigma_n00n = float(np.std(phi_n00n_hat))

        print(f"{n:>4} {m:>7} {sigma_class:>13.6f} {1 / np.sqrt(m):>10.6f} "
              f"{sigma_n00n:>11.6f} {1 / (n * np.sqrt(R)):>13.6f} "
              f"{sigma_class / sigma_n00n:>9.2f} {np.sqrt(n):>8.2f}")
        assert sigma_n00n < sigma_class
        assert abs(sigma_n00n / (1 / (n * np.sqrt(R))) - 1) < 0.15
        assert abs(sigma_class / (1 / np.sqrt(m)) - 1) < 0.15
    print("[OK] przy tym samym budzecie fotonow N00N daje dokladnosc lepsza o ~sqrt(N)")
    print("[OK] przy tym samym budzecie fotonow N00N daje dokladnosc lepsza o ~sqrt(N)")

    print("\n(3) dekoherencja niszczy przewage kwantowa:")
    print("    dla stanu GHZ z prawdopodobienstwem przezycia p_decoherencji")
    print("    F ~ p * N^2 + (1 - p) * N  ->  dla p < 1 granica przechodzi w 1/sqrt(N)")
    for p_surv in (1.0, 0.9, 0.5, 0.1):
        n = 100
        F_eff = p_surv * n**2 + (1 - p_surv) * n
        print(f"    p = {p_surv:>4.1f}: F = {F_eff:>9.1f}, sigma = {1 / np.sqrt(F_eff):.6f}, "
              f"granica 1/sqrt(N) = {1 / np.sqrt(n):.6f}")
    assert 1 / np.sqrt(1.0 * 100**2) < 1 / np.sqrt(0.5 * 100**2 + 0.5 * 100) < 1 / np.sqrt(0.1 * 100**2 + 0.9 * 100) < 1 / np.sqrt(100)
    print("[OK] im silniejsza dekoherencja, tym mniejsza informacja Fishera (przewaga slabnie)")

    print("\nWYNIK: metrologia OK")


if __name__ == "__main__":
    main()
