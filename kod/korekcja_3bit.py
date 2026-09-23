"""Kod powtarzalny 3-kubitowy (bit-flip) - syndromy i korekta.

Kod logiczny:
    |0>_L = |000>,   |1>_L = |111>
    syndrom = (pomiar Z1Z2, pomiar Z2Z3)  (bez pomiaru samych kubitow!)

Sprawdzamy:
  * dla kazdego pojedynczego bledu X na jednym z 3 kubitow syndrom wskazuje
    pozycje bledu i korekta odtwarza stan logiczny,
  * brak bledu -> syndrom 00,
  * kod nie koryguje dwoch bledow (dla porownania),
  * stan logiczny |+>_L = (|000> + |111>)/sqrt(2) i jego odpornosc na phase-flip.

Konwencja: stan |q2 q1 q0>, indeks = 4*q2 + 2*q1 + q0.

Uruchomienie:
    python kod/korekcja_3bit.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)


def kron3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    """Iloczyn tensorowy w kolejnosci |q2 q1 q0>."""
    return np.kron(np.kron(a, b), c)


def op_on(qubit: int, gate: np.ndarray) -> np.ndarray:
    """Operator `gate` na kubicie `qubit` (0 = najmłodszy bit) w 3-kubitowym ukladzie."""
    factors = [I2, I2, I2]                  # indeks 0 -> q2, 1 -> q1, 2 -> q0
    factors[2 - qubit] = gate               # q0 to ostatni czynnik
    return kron3(*factors)


def measure_zz(state: np.ndarray, q_a: int, q_b: int) -> int:
    """Pomiar Z (x) Z na kubitach q_a, q_b - wynik 0 lub 1 (bez kolapsu)."""
    dim = len(state)
    # wartosci +/-1 -> zamieniamy na bit: (+1, -1) -> (0, 1)
    probs = np.abs(state) ** 2
    result = 0.0
    for idx in range(dim):
        bits = [(idx >> k) & 1 for k in range(3)]        # bits[k] = wartosc kubitu k
        z_a = 1 - 2 * bits[q_a]
        z_b = 1 - 2 * bits[q_b]
        result += probs[idx] * z_a * z_b
    # dla stanow wlasnych Z1Z2 wynik jest dokladny (+/-1)
    eigenvalue = round(float(result))
    return 0 if eigenvalue == 1 else 1


def syndrome(state: np.ndarray) -> tuple[int, int]:
    """Syndrom (s12, s23) z pomiarow Z(q2)Z(q1) i Z(q1)Z(q0)."""
    return measure_zz(state, 2, 1), measure_zz(state, 1, 0)


def main() -> None:
    print("=== Kod powtarzalny 3-kubitowy (bit-flip) ===")
    ket0L = np.zeros(8, dtype=complex)
    ket0L[0b000] = 1.0
    ket1L = np.zeros(8, dtype=complex)
    ket1L[0b111] = 1.0

    print("\n(1) syndromy dla kazdego pojedynczego bledu X:")
    print(f"{'blad na q':>10} {'syndrom':>8} {'poprawka':>9} {'stan po korekcie':>18} {'= |0>_L ?':>10}")
    expected_correction = {
        (0, 0): None,      # brak bledu
        (1, 0): 2,         # blad na q2 -> poprawka X na q2
        (1, 1): 1,         # blad na q1
        (0, 1): 0,         # blad na q0
    }
    for err_qubit in (None, 2, 1, 0):
        state = ket0L.copy()
        if err_qubit is not None:
            state = op_on(err_qubit, X) @ state
        syn = syndrome(state)
        fix = expected_correction[syn]
        fixed = state if fix is None else op_on(fix, X) @ state
        ok = np.allclose(fixed, ket0L)
        label = "brak" if err_qubit is None else f"q{err_qubit}"
        fix_label = "-" if fix is None else f"X na q{fix}"
        print(f"{label:>10} {str(syn):>8} {fix_label:>9} {str(np.round(fixed, 3)):>18} {str(ok):>10}")
        assert ok
    print("[OK] kazdy pojedynczy blad bit-flip jest wykrywany i korygowany")

    # to samo dla stanu |1>_L
    for err_qubit in (2, 1, 0):
        state = op_on(err_qubit, X) @ ket1L
        syn = syndrome(state)
        fix = expected_correction[syn]
        fixed = state if fix is None else op_on(fix, X) @ state
        assert np.allclose(fixed, ket1L)
    print("[OK] korekta dziala tak samo dla |1>_L")

    # (2) dwa bledy: syndrom moze wskazywac zla poprawke
    print("\n(2) dwa bledy X (kod NIE koryguje dwoch bledow):")
    for q_a, q_b in ((2, 1), (2, 0), (1, 0)):
        state = op_on(q_a, X) @ (op_on(q_b, X) @ ket0L)
        syn = syndrome(state)
        fix = expected_correction[syn]
        fix_label = "-" if fix is None else f"X na q{fix}"
        fixed = state if fix is None else op_on(fix, X) @ state
        print(f"    bledy na q{q_a}, q{q_b}: syndrom {syn}, kod sadzi, ze trzeba '{fix_label}', "
              f"stan po 'korekcie' = {np.round(fixed, 3)}")
        assert not np.allclose(fixed, ket0L)
    print("[OK] dwa bledy nie sa poprawnie korygowane (ograniczenie kodu, dystans 3)")

    # (3) stan logiczny |+>_L i podatnosc na phase-flip
    print("\n(3) stan logiczny |+>_L = (|000> + |111>)/sqrt(2):")
    ket_plus_L = (ket0L + ket1L) / np.sqrt(2)
    print(f"    syndrom |+>_L = {syndrome(ket_plus_L)}  (kod nie rozroznia superpozycji)")
    assert syndrome(ket_plus_L) == (0, 0)
    # phase-flip (Z) na jednym kubicie psuje stan logiczny, syndrom Z1Z2 = 00
    damaged = op_on(1, Z) @ ket_plus_L
    print(f"    po Z na q1: syndrom = {syndrome(damaged)}  (nie wykrywa!)")
    assert not np.allclose(damaged, ket_plus_L)
    print("[OK] kod bit-flip nie widzi bledow fazowych - stad potrzebny kod phase-flip / Shora")

    # (4) kod phase-flip = kod bit-flip w bazie X
    print("\n(4) kod phase-flip w bazie |+/->:")
    ket_plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    ket_minus = np.array([1, -1], dtype=complex) / np.sqrt(2)
    plusL = kron3(ket_plus, ket_plus, ket_plus)
    minusL = kron3(ket_minus, ket_minus, ket_minus)
    # blad fazowy = Z dziala jak X w bazie X: X|+> = |+>, X|-> = -|->, wiec
    # poprawka: sprzezenie koniugacja Hadamarda na wszystkich kubitach
    HHH = kron3(H, H, H)
    print(f"    HHH |+>_L = stan |000>? {np.allclose(HHH @ plusL, ket0L)}")
    assert np.allclose(HHH @ plusL, ket0L)
    print("[OK] HHH zamienia kod phase-flip na kod bit-flip (ta sama korekcja)")

    print("\nWYNIK: korekcja 3-bit OK")


if __name__ == "__main__":
    main()
