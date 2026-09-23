"""Symulacja protokolu BB84 z podsłuchem typu intercept-resend.

Sprawdzamy:
  * bez podsłuchu: QBER = 0 (idealny kanał),
  * z podsłuchem: QBER ~ 25% przy pełnym podsłuchu, ~25%*f przy odsetku f,
  * prawdopodobieństwo wykrycia podsłuchu w próbce n bitów,
  * pojedynczy przypadek protokołu krok po kroku (wypis tabeli).

Uruchomienie:
    python kod/bb84.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# bazy: 0 = Z (|0>,|1>), 1 = X (|+>,|->)
BASES = ("Z", "X")


def encode(bit: int, basis: int) -> str:
    """Stan wyslany przez Alicje: '0','1','+','-'."""
    if basis == 0:                      # baza Z
        return "0" if bit == 0 else "1"
    return "+" if bit == 0 else "-"     # baza X


def measure(state: str, basis: int, rng: np.random.Generator) -> int:
    """Pomiar stanu w wybranej bazie; zwraca bit 0/1."""
    in_x_basis = state in "+-"
    if (basis == 1) == in_x_basis:
        # wlasciwa baza -> wynik deterministyczny
        return 0 if state in ("0", "+") else 1
    # zla baza -> wynik losowy
    return int(rng.integers(0, 2))


def run_protocol(n_bits: int = 4000, eavesdrop_fraction: float = 0.0, seed: int = 1) -> dict:
    """Przeprowadza BB84 i zwraca statystyki (QBER, dlugosc klucza)."""
    rng = np.random.default_rng(seed)
    alice_bits = rng.integers(0, 2, n_bits)
    alice_bases = rng.integers(0, 2, n_bits)
    bob_bases = rng.integers(0, 2, n_bits)

    states = [encode(int(b), int(bas)) for b, bas in zip(alice_bits, alice_bases)]

    # podsłuch: Eve mierzy losowa baza i odsyla przelany stan (intercept-resend)
    eaves_mask = rng.random(n_bits) < eavesdrop_fraction
    for i in np.flatnonzero(eaves_mask):
        eve_basis = int(rng.integers(0, 2))
        eve_bit = measure(states[i], eve_basis, rng)
        states[i] = encode(eve_bit, eve_basis)      # odsyla w swojej bazie

    bob_bits = np.array([measure(states[i], int(bob_bases[i]), rng) for i in range(n_bits)])

    sift = alice_bases == bob_bases
    a_key, b_key = alice_bits[sift], bob_bits[sift]
    errors = int((a_key != b_key).sum())
    qber = errors / max(len(a_key), 1)
    return {
        "n_sent": n_bits,
        "n_sifted": int(sift.sum()),
        "qber": float(qber),
        "eavesdrop_fraction": eavesdrop_fraction,
        "a_key": a_key,
        "b_key": b_key,
    }


def detection_probability(qber: float, sample: int) -> float:
    """P(przynajmniej jeden blad w probce n bitow) = 1 - (1 - qber)^n."""
    return float(1 - (1 - qber) ** sample)


def main() -> None:
    print("=== BB84: wymiana klucza kwantowego z podsłuchem ===")

    # 1) protokół krok po kroku na 8 bitach
    print("\n(1) przebieg protokolu na 8 bitach:")
    rng = np.random.default_rng(0)
    a_bits = rng.integers(0, 2, 8)
    a_bas = rng.integers(0, 2, 8)
    b_bas = rng.integers(0, 2, 8)
    print(f"{'i':>2} {'bit A':>6} {'baza A':>7} {'stan':>5} {'baza B':>7} {'bit B':>6} {'zgodne?':>8}")
    key_a, key_b = [], []
    for i in range(8):
        st = encode(int(a_bits[i]), int(a_bas[i]))
        bit_b = measure(st, int(b_bas[i]), rng)
        same = a_bas[i] == b_bas[i]
        if same:
            key_a.append(int(a_bits[i]))
            key_b.append(bit_b)
        print(f"{i:>2} {a_bits[i]:>6} {BASES[a_bas[i]]:>7} {st:>5} {BASES[b_bas[i]]:>7} {bit_b:>6} {str(same):>8}")
    print(f"    klucz A = {key_a}")
    print(f"    klucz B = {key_b}")
    assert key_a == key_b
    print("[OK] bez podsłuchu klucze sa identyczne")

    # 2) QBER bez podsłuchu i z podsłuchem
    print("\n(2) QBER w zaleznosci od odsetka podsłuchiwanych bitow:")
    print(f"{'podsłuch':>9} {'QBER':>9} {'klucz':>7} {'teoria':>9}")
    for frac in (0.0, 0.1, 0.25, 0.5, 1.0):
        res = run_protocol(20_000, frac, seed=2)
        theory = 0.25 * frac
        print(f"{frac:>9.2f} {res['qber']:>9.4f} {res['n_sifted']:>7} {theory:>9.4f}")
        assert abs(res["qber"] - theory) < 0.01
    print("[OK] QBER = 0.25 * (odsetek podsłuchu)")

    # 3) wykrywalnosc podsłuchu
    print("\n(3) prawdopodobienstwo wykrycia podsłuchu (proba n bitow):")
    for frac in (0.1, 0.25, 1.0):
        qber = 0.25 * frac
        for n in (20, 50, 100, 200):
            print(f"    podsłuch {frac:>4.0%}, proba {n:>3} bitow -> P(wykrycia) = "
                  f"{detection_probability(qber, n):.4f}")
    assert detection_probability(0.25, 100) > 0.999
    print("[OK] juz 100 bitow proby wykrywa pełny podsłuch z p > 0.999")

    # 4) prog bezpieczenstwa
    print("\n(4) prog bezpieczenstwa BB84:")
    print("    QBER < 11%  -> klucz uznajemy za bezpieczny (mozliwe uzgodnienie + wzmocnienie)")
    print("    QBER ~ 25%  -> pelny podsłuch intercept-resend, klucz odrzucamy")
    print("    QBER > 11%  -> odrzucamy klucz (potencjalny podsłuch)")

    print("\nWYNIK: BB84 OK")


if __name__ == "__main__":
    main()
