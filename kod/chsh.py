"""Nierownosc CHSH: granica klasyczna 2, granica kwantowa (Tsirelson) 2*sqrt(2).

Zawiera:
  * analityczne E(a,b) dla stanu |Psi-> = (|01> - |10>)/sqrt(2),
  * wartosc S dla optymalnych katow (2*sqrt(2)) i dla katow klasycznych (<= 2),
  * symulacje Monte Carlo pomiarow (sprawdzenie E(a,b)),
  * model zmiennych ukrytych (klasyczny) dla porownania.

Konwencja: pomiar w kierunku n = (sin(2a), 0, cos(2a)) na sferze Blocha
(kat polaryzatora `a` odpowiada polowie kata na sferze). Wtedy dla |Psi->
    E(a, b) = -cos(2*(a - b)).

Uruchomienie:
    python kod/chsh.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

Z = np.diag([1, -1]).astype(complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
PSI_MINUS = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)   # |01> - |10>, konw. maloendianowa


def correlation_analytic(a: float, b: float) -> float:
    """E(a,b) = <Psi-| (sigma_a (x) sigma_b) |Psi-> = -cos(2(a-b))."""
    return float(-np.cos(2 * (a - b)))


def correlation_simulated(a: float, b: float, shots: int = 200_000, seed: int = 1) -> float:
    """Symulacja Monte Carlo pomiarow na stanie |Psi-> w kierunkach a i b (w rad).

    Kat polaryzatora `a` odpowiada katowi Blocha alpha = 2a; spinor kierunku
    n = (sin alpha, 0, cos alpha) to (cos(alpha/2), sin(alpha/2)).
    """
    rng = np.random.default_rng(seed)

    def plus(alpha: float) -> np.ndarray:
        return np.array([np.cos(alpha / 2), np.sin(alpha / 2)], dtype=complex)

    def minus(alpha: float) -> np.ndarray:
        return np.array([-np.sin(alpha / 2), np.cos(alpha / 2)], dtype=complex)

    probs: dict[tuple[int, int], float] = {}
    for s1, v1 in ((+1, plus(2 * a)), (-1, minus(2 * a))):
        for s2, v2 in ((+1, plus(2 * b)), (-1, minus(2 * b))):
            ket = np.kron(v1, v2)          # kolejnosc |q1 q0>
            probs[(s1, s2)] = float(abs(np.vdot(ket, PSI_MINUS)) ** 2)
    assert abs(sum(probs.values()) - 1) < 1e-12

    keys = list(probs)
    p = np.array([probs[k] for k in keys])
    p = p / p.sum()
    idx = rng.choice(len(keys), size=shots, p=p)
    total = 0
    for i in idx:
        s1, s2 = keys[int(i)]
        total += s1 * s2
    return total / shots


def chsh_value(angles: tuple[float, float, float, float], simulated: bool = False) -> float:
    """|E(a,b) - E(a,b') + E(a',b) + E(a',b')|."""
    a, a_p, b, b_p = angles
    f = correlation_simulated if simulated else correlation_analytic
    return float(abs(f(a, b) - f(a, b_p) + f(a_p, b) + f(a_p, b_p)))


def classical_bound_scan() -> float:
    """Maksimum S dla modelu zmiennych ukrytych: przeglad wszystkich 16 strategii.

    W modelu lokalnym wyniki sa ustalone z gory: A(a), A(a'), B(b), B(b') w {-1,+1}.
    """
    import itertools

    best = 0.0
    for A_a, A_ap, B_b, B_bp in itertools.product((-1, 1), repeat=4):
        s = abs(A_a * B_b - A_a * B_bp + A_ap * B_b + A_ap * B_bp)
        best = max(best, float(s))
    return best


def main() -> None:
    print("=== Nierownosc CHSH ===")

    # optymalne katy dla splatania (konwencja polaryzatorowa, E = -cos(2(a-b)))
    angles_opt = (0.0, np.pi / 4, np.pi / 8, 3 * np.pi / 8)
    S_opt = chsh_value(angles_opt)
    print(f"\noptymalne katy (0, 45, 22.5, 67.5 stopni): S = {S_opt:.6f}")
    print(f"granica Tsirelsona 2*sqrt(2) = {2 * np.sqrt(2):.6f}")
    assert abs(S_opt - 2 * np.sqrt(2)) < 1e-12
    print("[OK] S = 2*sqrt(2) ~= 2.828 > 2 (granica klasyczna)")

    # katy "klasyczne": wszystkie pomiary w tej samej plaszczyznie, rowno odlegle
    angles_class = (0.0, np.pi / 2, np.pi / 4, np.pi / 2)
    S_class = chsh_value(angles_class)
    print(f"\nkaty bez naruszenia (0, 90, 45, 90 stopni): S = {S_class:.6f}")
    assert S_class <= 2 + 1e-12

    # nasladowanie pomiarow (Monte Carlo)
    print("\nsymulacja pomiarow (MC):")
    for pair in ((0.0, np.pi / 8), (0.0, 3 * np.pi / 8), (np.pi / 4, np.pi / 8), (np.pi / 4, 3 * np.pi / 8)):
        e_a = correlation_analytic(*pair)
        e_s = correlation_simulated(*pair, shots=100_000)
        print(f"    E({np.degrees(pair[0]):5.1f}, {np.degrees(pair[1]):5.1f} st.) = "
              f"{e_a:+.4f} (analitycznie)  {e_s:+.4f} (MC)")
        assert abs(e_a - e_s) < 0.01
    S_mc = chsh_value(angles_opt, simulated=True)
    print(f"    S z symulacji = {S_mc:.4f}  (analitycznie {S_opt:.4f})")
    assert abs(S_mc - S_opt) < 0.02
    print("[OK] symulacja potwierdza naruszenie nierownosci CHSH")

    # granica klasyczna
    bound = classical_bound_scan()
    print(f"\nmax S dla modelu zmiennych ukrytych (dyskretne +/-1) = {bound:.2f} <= 2")
    assert bound <= 2.0 + 1e-12
    print("[OK] zadna strategia klasyczna nie przekracza S = 2")

    print("\nWYNIK: CHSH OK")


if __name__ == "__main__":
    main()
