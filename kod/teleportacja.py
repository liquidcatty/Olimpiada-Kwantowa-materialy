"""Teleportacja kwantowa - pelny rachunek macierzowy (NumPy).

Protokol:
  1. Alicja i Bob dziela stan Bella |Phi+> = (|00> + |11>)/sqrt(2).
  2. Alicja ma kubit do teleportacji |psi> = alpha|0> + beta|1>.
  3. Alicja mierzy swoje dwa kubity w bazie Bella i wysyla 2 bity klasyczne.
  4. Bob wykonuje korekte (I, X, Z, ZX) i odtwarza |psi>.

Uklad kubitow: |q2 q1 q0>, gdzie q2 = kubit teleportowany (Alicja),
q1 = kubit Alicji ze splatania, q0 = kubit Boba.
Weryfikujemy wszystkie cztery przypadki pomiaru Bella.

Uruchomienie:
    python kod/teleportacja.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)

KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)

# baza Bella dla pary (q2, q1) w kolejnosci |Phi+>, |Phi->, |Psi+>, |Psi->
BELL_STATES = {
    0: np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2),
    1: np.array([1, 0, 0, -1], dtype=complex) / np.sqrt(2),
    2: np.array([0, 1, 1, 0], dtype=complex) / np.sqrt(2),
    3: np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2),
}


def build_state(alpha: complex, beta: complex) -> np.ndarray:
    """|psi>|Phi+> w ukladzie |q2 q1 q0> (q2 = teleportowany, q0 = Bob)."""
    psi_q2 = np.array([alpha, beta], dtype=complex)
    bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)   # |q1 q0> = |Phi+>
    return np.kron(psi_q2, bell)


def bell_measurement_on_A(state: np.ndarray) -> dict[int, tuple[float, np.ndarray]]:
    """Pomiar w bazie Bella kubitow (q2, q1).

    Zwraca slownik {wynik: (prawdopodobienstwo, znormalizowany stan Boba)}.
    """
    out: dict[int, tuple[float, np.ndarray]] = {}
    for outcome, bell in BELL_STATES.items():
        coeff = np.zeros(2, dtype=complex)                 # wspolczynniki stanu Boba
        coeff[0] = np.vdot(np.kron(bell, KET0), state)     # <bell| (x) <0| |psi>
        coeff[1] = np.vdot(np.kron(bell, KET1), state)     # <bell| (x) <1| |psi>
        p = float(np.vdot(coeff, coeff).real)
        if p > 1e-12:
            out[outcome] = (p, coeff / np.sqrt(p))
    return out


def correction(outcome: int) -> np.ndarray:
    """Korekta Boba dla wyniku pomiaru Bella (2 bity klasyczne)."""
    return {0: I2, 1: Z, 2: X, 3: Z @ X}[outcome]


def main() -> None:
    print("=== Teleportacja kwantowa ===")
    tests = [
        ("|0>", 1.0, 0.0),
        ("|1>", 0.0, 1.0),
        ("|+>", 1 / np.sqrt(2), 1 / np.sqrt(2)),
        ("|psi> = (2|0> + i|1>)/sqrt(5)", 2 / np.sqrt(5), 1j / np.sqrt(5)),
    ]
    for name, alpha, beta in tests:
        state = build_state(alpha, beta)
        assert abs(np.linalg.norm(state) - 1) < 1e-12
        outcomes = bell_measurement_on_A(state)
        total_p = 0.0
        print(f"\n{name}: alpha = {alpha:.4f}, beta = {beta:.4f}")
        for outcome, (p, bobs_state) in sorted(outcomes.items()):
            bits = format(outcome, "02b")
            corrected = correction(outcome) @ bobs_state
            target = np.array([alpha, beta], dtype=complex)
            ok = np.allclose(corrected, target) or np.allclose(corrected, -target)
            total_p += p
            print(f"    wynik pomiaru Bella {bits}: p = {p:.2f}, "
                  f"stan Boba po korekcie = {np.round(corrected, 4)}, zgodny z |psi>? {ok}")
            assert ok
        assert len(outcomes) == 4
        assert abs(total_p - 1.0) < 1e-12

    print("\n[OK] dla kazdego z 4 wynikow pomiaru Bella teleportacja odtwarza stan")
    print("[OK] teleportacja przenosi stan przy uzyciu 1 e-bitu i 2 bitow klasycznych")
    print("     (uwaga: nie kopiuje stanu - oryginal zostaje zniszczony przez pomiar)")

    # kontrola: bez korekty stan Boba nie jest rowny |psi> (dla nietrywialnego |psi>)
    state = build_state(2 / np.sqrt(5), 1j / np.sqrt(5))
    outcomes = bell_measurement_on_A(state)
    bad = 0
    for outcome, (p, bobs_state) in outcomes.items():
        if not np.allclose(bobs_state, np.array([2 / np.sqrt(5), 1j / np.sqrt(5)])):
            bad += 1
    print(f"\n(+) bez korekty klasycznej tylko {4 - bad}/4 wynikow daje wlasciwy stan")
    assert bad > 0
    print("[OK] 2 bity klasyczne sa niezbedne")

    print("\nWYNIK: Teleportacja OK")


if __name__ == "__main__":
    main()
