#!/usr/bin/env python3
"""
Leapfrog low-pass filter – educational digital implementation.

A classic odd-order leapfrog (active-ladder) structure simulated with
simple forward-Euler integrators.  This is a public textbook topology;
it is not an implementation of any patented circuit.
"""

from __future__ import annotations
import math
from typing import List


class LeapfrogLowpass:
    """
    Simple N-th order leapfrog low-pass filter (N odd, typically 3 or 5).

    State variables represent the integrator outputs.
    Coefficients are chosen for a rough Butterworth-like response
    and can be scaled by the cut-off frequency.
    """

    def __init__(self, order: int = 5, cutoff_hz: float = 1000.0, sample_rate: float = 48000.0):
        if order < 1 or order % 2 == 0:
            raise ValueError("order must be a positive odd integer")
        self.order = order
        self.sample_rate = sample_rate
        self.cutoff = cutoff_hz

        # Normalised angular frequency
        w0 = 2.0 * math.pi * cutoff_hz / sample_rate

        # Very simple coefficient set (educational, not optimised)
        # Feedback strengths decrease toward the middle of the chain
        self.g = [w0 * (1.0 + 0.3 * abs(i - order // 2)) for i in range(order)]
        self.state = [0.0] * order

    def process(self, x: float) -> float:
        """Process one sample and return the filter output."""
        # Forward path + local feedback (leapfrog)
        # First integrator
        self.state[0] += self.g[0] * (x - self.state[0] - self.state[1] if self.order > 1 else x - self.state[0])

        # Intermediate integrators
        for i in range(1, self.order - 1):
            self.state[i] += self.g[i] * (self.state[i - 1] - self.state[i] - self.state[i + 1])

        # Last integrator
        if self.order > 1:
            self.state[-1] += self.g[-1] * (self.state[-2] - self.state[-1])

        return self.state[-1]

    def process_block(self, samples: List[float]) -> List[float]:
        return [self.process(s) for s in samples]

    def reset(self) -> None:
        self.state = [0.0] * self.order


def impulse_response(order: int = 5, length: int = 256) -> List[float]:
    f = LeapfrogLowpass(order=order, cutoff_hz=800.0, sample_rate=48000.0)
    ir = []
    for i in range(length):
        x = 1.0 if i == 0 else 0.0
        ir.append(f.process(x))
    return ir


def main() -> None:
    print("Leapfrog low-pass filter demo (Python)")
    print("Order 5, cutoff ≈ 800 Hz, Fs = 48 kHz")
    print("-" * 50)

    ir = impulse_response(order=5, length=32)
    for i, y in enumerate(ir):
        print(f"sample[{i:2d}] = {y: .6f}")

    print("\nDone.")


if __name__ == "__main__":
    main()
