"""Zadanie P3: bramki H, Z, H na kubicie + rozpoznanie HZH = X.

Uruchomienie:
    python kod/p3_hzh.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)


def prob(psi: np.ndarray, basis: np.ndarray) -> float:
    """Prawdopodobienstwo wyniku = |<basis|psi>|^2."""
    return float(abs(np.vdot(basis, psi)) ** 2)


def main() -> None:
    print("=== P3: bramki H, Z, H na kubicie ===")

    # (a) krok po kroku: H|0> = |+>, Z|+> = |->, H|-> = |1>
    psi = H @ KET0
    plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    print(f"\n(a) H|0> = {np.round(psi, 6)}  = |+>")
    assert np.allclose(psi, plus)

    psi = Z @ psi
    minus = np.array([1, -1], dtype=complex) / np.sqrt(2)
    print(f"    Z|+> = {np.round(psi, 6)}  = |->")
    assert np.allclose(psi, minus)

    psi = H @ psi
    print(f"    H|-> = {np.round(psi, 6)}  = |1>")
    assert np.allclose(psi, KET1)

    p0, p1 = prob(psi, KET0), prob(psi, KET1)
    print(f"    P(0) = {p0:.6f},  P(1) = {p1:.6f}")
    assert abs(p0) < 1e-15 and abs(p1 - 1) < 1e-15
    print("[OK] stan przed pomiarem to |1>: wynik pomiaru jest deterministyczny")

    # (b) HZH = X
    HZH = H @ Z @ H
    print(f"\n(b) HZH =\n{np.round(HZH.real, 6)}")
    assert np.allclose(HZH, X)
    print("[OK] HZH = X = [[0,1],[1,0]]")

    # dodatkowe tozsamosci sprzezenia Hadamarda
    print("\n(+) kontrola pozostalych tozsamosci:")
    print(f"    HXH = Z ? {np.allclose(H @ X @ H, Z)}")
    print(f"    HYH = -Y ? {np.allclose(H @ np.array([[0, -1j], [1j, 0]]) @ H, -np.array([[0, -1j], [1j, 0]]))}")
    print(f"    H = (X+Z)/sqrt(2) ? {np.allclose(H, (X + Z) / np.sqrt(2))}")
    assert np.allclose(H @ X @ H, Z)
    assert np.allclose(H, (X + Z) / np.sqrt(2))
    assert np.allclose(H @ np.array([[0, -1j], [1j, 0]]) @ H, -np.array([[0, -1j], [1j, 0]]))
    print("[OK] HZH = X, HXH = Z, HYH = -Y, H = (X+Z)/sqrt(2)")

    # sprawdzenie ogolne: HZH|0> = |1> niezaleznie od rozkladu na |+>, |->
    print("\n(+) rozklad |0> = (|+> + |->)/sqrt(2):")
    for sign, label in ((1, "|+>"), (-1, "|->")):
        amp = (1 / np.sqrt(2)) * H @ KET0 if sign > 0 else (1 / np.sqrt(2)) * H @ KET1
        print(f"    amplituda przy {label}: {amp[0]:.6f}")

    print("\nWYNIK: P3 OK")


if __name__ == "__main__":
    main()
