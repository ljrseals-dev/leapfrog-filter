#!/usr/bin/env python3
"""
Optional frequency-response plot for the leapfrog filter.
Requires: numpy, matplotlib
"""

import sys
sys.path.insert(0, "../src/python")

import numpy as np
import matplotlib.pyplot as plt
from leapfrog import LeapfrogLowpass

def frequency_response(order=5, cutoff=1000.0, fs=48000.0, n_fft=4096):
    f = LeapfrogLowpass(order=order, cutoff_hz=cutoff, sample_rate=fs)
    # Impulse
    impulse = np.zeros(n_fft)
    impulse[0] = 1.0
    response = np.array(f.process_block(impulse.tolist()))
    spectrum = np.fft.rfft(response)
    freqs = np.fft.rfftfreq(n_fft, 1.0 / fs)
    mag_db = 20.0 * np.log10(np.maximum(np.abs(spectrum), 1e-12))
    return freqs, mag_db

def main():
    freqs, mag = frequency_response(order=5, cutoff=1000.0)
    plt.figure(figsize=(10, 5))
    plt.semilogx(freqs, mag)
    plt.axvline(1000.0, color="r", linestyle="--", label="target cutoff")
    plt.grid(True, which="both", ls=":")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title("Leapfrog 5th-order low-pass – frequency response")
    plt.legend()
    plt.ylim(-60, 5)
    plt.xlim(20, 20000)
    plt.tight_layout()
    plt.savefig("leapfrog_response.png", dpi=120)
    print("Saved leapfrog_response.png")
    plt.show()

if __name__ == "__main__":
    main()
