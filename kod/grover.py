"""Algorytm Grovera: liczba iteracji, prawdopodobienstwo sukcesu, symulacja.

Sprawdzamy dla N = 4 i N = 8:
  * optymalna liczba iteracji k* = round(pi/4 * sqrt(N) - 1/2),
  * prawdopodobienstwo sukcesu po k iteracjach: sin^2((2k+1)*theta),
    gdzie sin(theta) = 1/sqrt(N),
  * symulacje pomiarow na obwodzie (NumPy),
  * dla N = 4 sukces po 1 iteracji jest pewny (p = 1).

Uruchomienie:
    python kod/grover.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def grover_theta(n_states: int) -> float:
    """Kat theta z relacji sin(theta) = 1/sqrt(N)."""
    return float(np.arcsin(1 / np.sqrt(n_states)))


def success_probability(n_states: int, k: int) -> float:
    """Dokladne p(sukces) po k iteracjach Grovera."""
    theta = grover_theta(n_states)
    return float(np.sin((2 * k + 1) * theta) ** 2)


def optimal_iterations(n_states: int) -> int:
    """Optymalna liczba iteracji wg wzoru pi/4*sqrt(N) - 1/2."""
    return int(np.round(np.pi / 4 * np.sqrt(n_states) - 0.5))


def grover_statevector(n_qubits: int, marked: int, iterations: int) -> np.ndarray:
    """Symulacja obwodu Grovera (stan wektorowy) dla N = 2^n_qubits.

    Wyrocznia: mnozy amplitude stanu |marked> przez -1.
    Operator dyfuzji: 2|s><s| - I, gdzie |s> to rownomierna superpozycja.
    """
    n_states = 2 ** n_qubits
    s = np.ones(n_states, dtype=complex) / np.sqrt(n_states)
    psi = s.copy()
    for _ in range(iterations):
        psi[marked] *= -1.0                  # wyrocznia (faza)
        psi = 2 * s * np.vdot(s, psi) - psi  # dyfuzja wokol |s>
    return psi


def main() -> None:
    print("=== Algorytm Grovera ===")
    for n_qubits in (2, 3, 4):
        n_states = 2 ** n_qubits
        marked = n_states - 1
        k_opt = optimal_iterations(n_states)
        print(f"\nN = {n_states} (n = {n_qubits} kubitow), oznaczony stan |{marked:0{n_qubits}b}>")
        print(f"  k* = {k_opt}  (wzor: pi/4*sqrt(N) - 1/2 = {np.pi / 4 * np.sqrt(n_states) - 0.5:.3f})")
        for k in range(0, k_opt + 2):
            p_analytic = success_probability(n_states, k)
            psi = grover_statevector(n_qubits, marked, k)
            p_sim = float(abs(psi[marked]) ** 2)
            print(f"    k = {k}:  p(analitycznie) = {p_analytic:.6f}  p(symulacja) = {p_sim:.6f}")
            assert abs(p_analytic - p_sim) < 1e-12

    # dla N = 4 po jednej iteracji sukces jest pewny
    p = success_probability(4, 1)
    print(f"\nN = 4, k = 1:  p = {p:.12f}")
    assert abs(p - 1.0) < 1e-12
    print("[OK] dla N = 4 algorytm Grovera daje sukces z prawdopodobienstwem 1")

    # skanowanie iteracji dla N = 8 (wyscig z optymalna liczba iteracji)
    print("\nN = 8: prawdopodobienstwo sukcesu dla kolejnych iteracji")
    for k in range(0, 4):
        print(f"    k = {k}: p = {success_probability(8, k):.6f}")
    assert success_probability(8, 2) > success_probability(8, 1)
    assert success_probability(8, 3) < success_probability(8, 2)
    print("[OK] dla N = 8 optymalnie jest k = 2 (dalsze iteracje psuja wynik)")

    # pomiary na symulowanym obwodzie
    rng = np.random.default_rng(7)
    psi = grover_statevector(3, 7, 2)
    p = np.abs(psi) ** 2
    samples = rng.choice(8, size=2000, p=p)
    counts = {format(i, "03b"): int((samples == i).sum()) for i in range(8)}
    print("\n2000 pomiarow dla N = 8, k = 2:", counts)
    assert counts["111"] > 1800
    print("[OK] symulacja pomiarow potwierdza przewage kwantowa Grovera")

    print("\nWYNIK: Grover OK")


if __name__ == "__main__":
    main()
