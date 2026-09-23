"""Zadanie P1: czastka w nieskonczonej studni potencjalu.

Sprawdzamy numerycznie:
  * normalizacje stanu psi = (1/sqrt(5))*(2*psi_1 + psi_2),
  * prawdopodobienstwa P(E_1), P(E_2) i wartosc oczekiwana <E>,
  * dodatkowo <x> dla stanu psi (wynik analityczny: 0.3559 L).

Uruchomienie:
    python kod/p1_studnia.py
"""

from __future__ import annotations

import numpy as np

L = 1.0                     # szerokosc studni (umownie 1)
N = 400_001                 # liczba punktow siatki
X = np.linspace(0.0, L, N)
NORM = np.sqrt(2.0 / L)     # czynnik normalizacyjny stanu wlasnego


def psi(n: int) -> np.ndarray:
    """N-ty stan wlasny nieskonczonej studni: sqrt(2/L) sin(n pi x / L)."""
    return NORM * np.sin(n * np.pi * X / L)


def integrate(f: np.ndarray) -> float:
    """Calka po x (metoda trapezow)."""
    return float(np.trapezoid(f, X))


def main() -> None:
    psi1, psi2 = psi(1), psi(2)
    print("=== P1: czastka w nieskonczonej studni potencjalu ===")

    # ortogonalnosc i normalizacja stanow wlasnych
    o11, o22, o12 = integrate(psi1**2), integrate(psi2**2), integrate(psi1 * psi2)
    print(f"<psi1|psi1> = {o11:.10f}   <psi2|psi2> = {o22:.10f}   <psi1|psi2> = {o12:+.2e}")
    assert abs(o11 - 1) < 1e-8 and abs(o22 - 1) < 1e-8 and abs(o12) < 1e-8
    print("[OK] stany wlasne sa unormowane i ortogonalne")

    # (a) normalizacja stanu psi
    p2 = (2.0 * psi1 + psi2) / np.sqrt(5.0)
    norm = integrate(p2**2)
    print(f"\n(a) <psi|psi> = {norm:.10f}")
    assert abs(norm - 1.0) < 1e-8
    print("[OK] stan psi jest unormowany")

    # (b) prawdopodobienstwa P(E_1), P(E_2)
    c1 = integrate(psi1 * p2)
    c2 = integrate(psi2 * p2)
    P1, P2 = c1**2, c2**2
    print(f"\n(b) c1 = {c1:.10f}  ->  P(E1) = {P1:.10f}")
    print(f"    c2 = {c2:.10f}  ->  P(E2) = {P2:.10f}")
    print(f"    suma = {P1 + P2:.10f}")
    assert abs(P1 - 0.8) < 1e-8 and abs(P2 - 0.2) < 1e-8
    assert abs(P1 + P2 - 1.0) < 1e-10
    print("[OK] P(E1) = 4/5 = 0.8, P(E2) = 1/5 = 0.2")

    # (c) wartosc oczekiwana energii: E_n ~ n^2, wiec liczymy w jednostkach E1
    E1 = 1.0                                  # E_1 w jednostkach pi^2 hbar^2/(2 m L^2)
    En = {1: E1, 2: 4 * E1}
    E_exp = P1 * En[1] + P2 * En[2]
    print(f"\n(c) <E> = {P1:.6f}*E1 + {P2:.6f}*E2 = {E1:.1f}*({P1:.4f} + 4*{P2:.4f}) = {E_exp:.6f} E1")
    print(f"    <E> = {E_exp:.6f} * pi^2 hbar^2 / (2 m L^2) = 4/5 * pi^2 hbar^2 / (m L^2)")
    assert abs(E_exp - 8 / 5) < 1e-9
    print("[OK] <E> = 8/5 E1 = 4 pi^2 hbar^2 / (5 m L^2)")

    # rozszerzenie: <x>
    x_exp = integrate(X * p2**2)
    x_analytic = L / 2 - 64 * L / (45 * np.pi**2)
    print(f"\n(+) <x> numerycznie = {x_exp:.6f} L, analitycznie = {x_analytic:.6f} L")
    assert abs(x_exp - x_analytic) < 1e-5
    print("[OK] <x> = L/2 - 64L/(45 pi^2) = 0.3559 L  (przesuniecie w lewo)")

    print("\nWYNIK: P1 OK")


if __name__ == "__main__":
    main()
