"""Zadanie P2: polaryzatory i pojedynczy foton (prawo Malusa).

Sprawdzamy:
  * (a) natezenie po dwoch polaryzatorach (0 -> 45 -> 90 stopni),
  * (b) natezenie po usunieciu pierwszego polaryzatora,
  * (c) prawdopodobienstwa przejscia pojedynczego fotonu,
  * oraz "paradoks trzech polaryzatorow" (0 -> 45 -> 90 daje I0/8).

Uruchomienie:
    python kod/p2_polaryzatory.py
"""

from __future__ import annotations

import numpy as np


def malus(i_in: float, angle_deg_between: float) -> float:
    """Natezenie po polaryzatorze: I = I_in * cos^2(alpha)."""
    return i_in * np.cos(np.deg2rad(angle_deg_between)) ** 2


def transmission_probability(angle_deg_between: float) -> float:
    """Prawdopodobienstwo przejscia pojedynczego fotonu (stan -> stan)."""
    return float(np.cos(np.deg2rad(angle_deg_between)) ** 2)


def main() -> None:
    I0 = 1.0
    print("=== P2: polaryzatory i pojedynczy foton ===")

    # (a) I0 -> P1 (45 st.) -> P2 (90 st.)
    I1 = malus(I0, 45.0)          # 0 -> 45
    I_out = malus(I1, 45.0)       # 45 -> 90
    print(f"\n(a) I po P1  = {I1:.6f} I0")
    print(f"    I wyjsciowe = {I_out:.6f} I0")
    assert abs(I_out - I0 / 4) < 1e-12
    print("[OK] I_wy = I0/4")

    # (b) bez P1: swiatlo poziome pada na polaryzator pionowy
    I_no_p1 = malus(I0, 90.0)
    print(f"\n(b) I wyjsciowe bez P1 = {I_no_p1:.1e} I0")
    assert abs(I_no_p1) < 1e-15
    print("[OK] I_wy = 0  (polaryzator P1 nie przepuszcza, ale obraca polaryzacje)")

    # (c) pojedynczy foton
    p_stage = transmission_probability(45.0)
    p_total = p_stage * p_stage
    print(f"\n(c) P(przejscie przez P1) = {p_stage:.6f}")
    print(f"    P(przejscie przez uklad) = {p_total:.6f}")
    assert abs(p_total - 0.25) < 1e-12
    p_no_p1 = transmission_probability(90.0)
    print(f"    P(przejscie bez P1) = {p_no_p1:.1e}")
    assert abs(p_no_p1) < 1e-15
    print("[OK] P = 1/4 z P1 oraz P = 0 bez P1")

    # bonus: paradoks trzech polaryzatorow 0 -> 45 -> 90 -> 135
    chain = I0
    for k in range(1, 4):
        chain = malus(chain, 45.0)
        print(f"    po {45 * k:>3} st.: I = {chain:.6f} I0")
    assert abs(chain - I0 / 8) < 1e-12
    print("[OK] kazdy dodatkowy polaryzator obrocony o 45 st. mnozy natezenie przez 1/2")

    print("\nWYNIK: P2 OK")


if __name__ == "__main__":
    main()
