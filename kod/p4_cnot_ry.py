"""Zadanie P4: obwod dwukubitowy H + R_Y(theta) + CNOT.

Sprawdzamy:
  * stan po CNOT i kryterium splatania (wyznacznik macierzy amplitud),
  * P_00, P_01, P_10, P_11 jako funkcje theta i sume = 1,
  * P(zgodny wynik) = cos^2(theta/2) oraz <Z (x) Z> = cos(theta),
  * przypadki theta = 0, pi/2, pi.

Konwencja maloendianowa: stan |q1 q0>, q1 = kubit GORNY (bramka H), q0 = DOLNY.

Uruchomienie:
    python kod/p4_cnot_ry.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

I2 = np.eye(2, dtype=complex)
Z = np.diag([1, -1]).astype(complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)
ZZ = np.kron(Z, Z)
KET00 = np.array([1, 0, 0, 0], dtype=complex)


def r_y(theta: float) -> np.ndarray:
    """Bramka obrotu wokol osi Y z konwencja theta/2 (jak w zadaniu)."""
    return np.array(
        [[np.cos(theta / 2), -np.sin(theta / 2)], [np.sin(theta / 2), np.cos(theta / 2)]],
        dtype=complex,
    )


def state_after_circuit(theta: float) -> np.ndarray:
    """H na q1, R_Y(theta) na q0, CNOT(kontrola q1, cel q0)."""
    psi = np.kron(H, I2) @ KET00            # bramka na gornym kubicie
    psi = np.kron(I2, r_y(theta)) @ psi     # bramka na dolnym kubicie
    return CNOT @ psi                       # kontrola = q1, cel = q0


def main() -> None:
    print("=== P4: obwod H + R_Y(theta) + CNOT ===")

    theta = 0.7
    psi = state_after_circuit(theta)
    print(f"\n(theta = {theta} rad)")
    print("amplitudy:", np.round(psi, 6))
    expected = np.array(
        [
            np.cos(theta / 2) / np.sqrt(2),
            np.sin(theta / 2) / np.sqrt(2),
            np.sin(theta / 2) / np.sqrt(2),
            np.cos(theta / 2) / np.sqrt(2),
        ]
    )
    assert np.allclose(psi, expected)
    print("[OK] stan zgodny z rozwiazaniem analitycznym")

    # (a) splatanie: wyznacznik macierzy amplitud
    det = np.linalg.det(psi.reshape(2, 2))
    print(f"\n(a) det(macierz amplitud) = {det.real:.6f}  (analitycznie cos(theta)/2 = {np.cos(theta) / 2:.6f})")
    assert abs(det.real - np.cos(theta) / 2) < 1e-12
    print("    stan splatany? ", abs(det) > 1e-9)
    assert abs(det) > 1e-9

    # (b) prawdopodobienstwa
    p = np.abs(psi) ** 2
    print(f"\n(b) P = {np.round(p, 6)}")
    print(f"    P00 = P11 = {p[0]:.6f}, P01 = P10 = {p[1]:.6f}")
    print(f"    suma = {p.sum():.12f}")
    assert abs(p.sum() - 1) < 1e-12
    assert abs(p[0] - p[3]) < 1e-15 and abs(p[1] - p[2]) < 1e-15
    print("[OK] P00 = P11 = cos^2(theta/2)/2, P01 = P10 = sin^2(theta/2)/2, suma = 1")

    # (c) zgodne wyniki i <Z x Z>
    same = p[0] + p[3]
    zz = np.real(psi.conj() @ (ZZ @ psi))
    print(f"\n(c) P(zgodne wyniki) = {same:.6f}, analitycznie cos^2(theta/2) = {np.cos(theta / 2) ** 2:.6f}")
    print(f"    <Z (x) Z>        = {zz:.6f}, analitycznie cos(theta)  = {np.cos(theta):.6f}")
    assert abs(same - np.cos(theta / 2) ** 2) < 1e-12
    assert abs(zz - np.cos(theta)) < 1e-12
    print("[OK] P(zgodne) = (1 + cos theta)/2 oraz <Z (x) Z> = cos theta")

    # przypadki szczegolne
    print("\n(+) przypadki szczegolne:")
    print(f"{'theta':>8} {'P00':>10} {'P01':>10} {'P10':>10} {'P11':>10} {'P(zg)':>8} {'<ZZ>':>7}  stan")
    for th in (0.0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi):
        ps = state_after_circuit(th)
        pr = np.abs(ps) ** 2
        sg = pr[0] + pr[3]
        z = np.real(ps.conj() @ (ZZ @ ps))
        d = abs(np.linalg.det(ps.reshape(2, 2)))
        name = "iloczynowy" if d < 1e-9 else ("Bell |Phi+>" if abs(th) < 1e-12 else "Bell |Psi+>" if abs(th - np.pi) < 1e-12 else "splatany")
        print(f"{th:>8.4f} {pr[0]:>10.6f} {pr[1]:>10.6f} {pr[2]:>10.6f} {pr[3]:>10.6f} {sg:>8.4f} {z:>7.4f}  {name}")
        assert abs(sg - np.cos(th / 2) ** 2) < 1e-12
        assert abs(z - np.cos(th)) < 1e-12

    # theta = pi/2 -> stan iloczynowy |+>|+>
    pp = state_after_circuit(np.pi / 2)
    plus_plus = np.ones(4, dtype=complex) / 2
    print(f"\n(+) theta = pi/2 daje |+>|+> ? {np.allclose(pp, plus_plus)}")
    assert np.allclose(pp, plus_plus)
    print("[OK] dla theta = pi/2 stan jest iloczynowy (CNOT nie zmienia |++>)")

    print("\nWYNIK: P4 OK")


if __name__ == "__main__":
    main()
