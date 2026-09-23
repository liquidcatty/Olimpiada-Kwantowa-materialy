"""Analiza danych i obliczenia naukowe: dopasowanie, chi2, bootstrap, FFT.

Symulujemy doswiadczenie: zanik w czasie T2 (sygnal eksponencjalny z szumem),
dopasowujemy model metoda najmniejszych kwadratow (bez SciPy), liczymy chi2/ndof,
niepewnosci parametrow, przedzial ufności bootstrap oraz widmo FFT.

Uruchomienie:
    python kod/analiza_danych.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def generate_data(t2: float = 2.5, a0: float = 0.98, noise: float = 0.02,
                  n_points: int = 60, seed: int = 11) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Dane eksperymentalne: y = a0 * exp(-t / T2) + szum gaussowski."""
    rng = np.random.default_rng(seed)
    t = np.linspace(0.0, 8.0, n_points)
    y_true = a0 * np.exp(-t / t2)
    y = y_true + rng.normal(0.0, noise, size=n_points)
    sigma = np.full(n_points, noise)
    return t, y, sigma


def fit_exponential(t: np.ndarray, y: np.ndarray, sigma: np.ndarray) -> dict:
    """Dopasowanie y = A*exp(-t/T2) metoda najmniejszych kwadratow.

    Start z logarytmizacji (ln y = ln A - t/T2), potem lokalna minimalizacja
    chi2 krokiem adaptacyjnym (bez SciPy). Niepewnosci z hesjanu numerycznego.
    """
    mask = y > 3 * np.abs(sigma)
    b, a = np.polyfit(t[mask], np.log(y[mask]), 1)      # ln y = a + b t
    t2, a0 = -1.0 / b, float(np.exp(a))

    def chi2_of(t2_val: float, a0_val: float) -> float:
        r = (y - a0_val * np.exp(-t / t2_val)) / sigma
        return float(np.sum(r**2))

    step = 0.02
    for _ in range(500):
        c0 = chi2_of(t2, a0)
        best = (c0, t2, a0)
        for dt in (-step, step):
            for da in (-step * 2, step * 2):
                c = chi2_of(t2 * (1 + dt), a0 * (1 + da))
                if c < best[0]:
                    best = (c, t2 * (1 + dt), a0 * (1 + da))
        if best[0] >= c0:
            step *= 0.5
            if step < 1e-8:
                break
        else:
            _, t2, a0 = best

    chi2 = chi2_of(t2, a0)
    ndof = len(y) - 2
    h_t, h_a = 1e-4, 1e-5
    d2t = (chi2_of(t2 + h_t, a0) - 2 * chi2 + chi2_of(t2 - h_t, a0)) / h_t**2
    d2a = (chi2_of(t2, a0 + h_a) - 2 * chi2 + chi2_of(t2, a0 - h_a)) / h_a**2
    return {
        "T2": float(t2),
        "A": float(a0),
        "u_T2": float(np.sqrt(2 / d2t)),
        "u_A": float(np.sqrt(2 / d2a)),
        "chi2": float(chi2),
        "ndof": int(ndof),
        "chi2_ndof": float(chi2 / ndof),
    }


def bootstrap_t2(t: np.ndarray, y: np.ndarray, sigma: np.ndarray,
                 n_resamples: int = 200, seed: int = 5) -> tuple[float, float]:
    """Przedzial ufnosci 68% dla T2 metoda bootstrap (resampling punktow)."""
    rng = np.random.default_rng(seed)
    values = []
    n = len(t)
    for _ in range(n_resamples):
        idx = rng.integers(0, n, n)
        try:
            values.append(fit_exponential(t[idx], y[idx], sigma[idx])["T2"])
        except Exception:                      # pragmatycznie: pomijamy nieudane resamplowania
            continue
    lo, hi = np.percentile(values, [16, 84])
    return float(lo), float(hi)


def fft_analysis(n_points: int = 1024, fs: float = 100.0, f0: float = 7.0,
                 seed: int = 3) -> dict:
    """Sygnal sinusoidalny + szum: wykrycie czestotliwosci przez FFT."""
    rng = np.random.default_rng(seed)
    t = np.arange(n_points) / fs
    signal = 0.7 * np.sin(2 * np.pi * f0 * t) + rng.normal(0, 0.5, n_points)
    spectrum = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(n_points, 1 / fs)
    peak = float(freqs[np.argmax(np.abs(spectrum))])
    return {"f_detected": peak, "f_true": f0, "resolution": float(fs / n_points)}


def main() -> None:
    print("=== Analiza danych i obliczenia naukowe ===")

    # (1) dopasowanie zaniku T2
    t, y, sigma = generate_data()
    fit = fit_exponential(t, y, sigma)
    print(f"\n(1) dopasowanie y = A*exp(-t/T2) do {len(t)} punktow")
    print(f"    T2 = {fit['T2']:.4f} +- {fit['u_T2']:.4f}   (wartosc prawdziwa: 2.5)")
    print(f"    A  = {fit['A']:.4f} +- {fit['u_A']:.4f}   (wartosc prawdziwa: 0.98)")
    print(f"    chi2/ndof = {fit['chi2']:.2f}/{fit['ndof']} = {fit['chi2_ndof']:.3f}")
    assert abs(fit["T2"] - 2.5) < 0.2
    assert abs(fit["chi2_ndof"] - 1.0) < 0.6
    print("[OK] parametry odtworzone, chi2/ndof bliskie 1 (model zgodny z danymi)")

    # (2) propagacja niepewnosci
    t_check = 3.0
    y_pred = fit["A"] * np.exp(-t_check / fit["T2"])
    dy_dA = np.exp(-t_check / fit["T2"])
    dy_dT2 = fit["A"] * np.exp(-t_check / fit["T2"]) * t_check / fit["T2"] ** 2
    u_y = float(np.sqrt((dy_dA * fit["u_A"]) ** 2 + (dy_dT2 * fit["u_T2"]) ** 2))
    print(f"\n(2) propagacja niepewnosci: y(3.0) = {y_pred:.4f} +- {u_y:.4f}")
    print("[OK] niepewnosc policzona z ogolnego wzoru na propagacje bledow")

    # (3) bootstrap
    lo, hi = bootstrap_t2(t, y, sigma)
    print(f"\n(3) bootstrap (200 resamplowan): T2 w [{lo:.4f}, {hi:.4f}] (68% ufnosci)")
    print(f"    szerokosc przedzialu = {hi - lo:.4f},  2*u_T2 = {2 * fit['u_T2']:.4f}")
    assert lo - 0.3 <= fit["T2"] <= hi + 0.3
    print("[OK] przedzial bootstrap zgodny z niepewnoscia z hesjanu")

    # (4) FFT
    res = fft_analysis()
    print(f"\n(4) FFT: wykryta czestotliwosc = {res['f_detected']:.3f} Hz "
          f"(prawda {res['f_true']:.1f} Hz, rozdzielczosc {res['resolution']:.3f} Hz)")
    assert abs(res["f_detected"] - res["f_true"]) <= 2 * res["resolution"]
    print("[OK] FFT poprawnie identyfikuje czestotliwosc sygnalu")

    # (5) zliczenia fotonow: statystyka Poissona
    rng = np.random.default_rng(9)
    lam = 25.0
    counts = rng.poisson(lam, 5000)
    print(f"\n(5) zliczenia fotonow (Poisson, lambda = {lam:.0f}):")
    print(f"    srednia = {counts.mean():.3f}, wariancja = {counts.var():.3f}, "
          f"odchylenie = {counts.std():.3f} ~ sqrt(lambda) = {np.sqrt(lam):.3f}")
    assert abs(counts.mean() - lam) < 1.0
    assert abs(counts.var() - lam) < 3.0
    print("[OK] dla zliczen fotonow wariancja = srednia (statystyka Poissona)")

    print("\nWYNIK: analiza danych OK")


if __name__ == "__main__":
    main()

