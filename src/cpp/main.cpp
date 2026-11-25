/**
 * Simple driver for the leapfrog low-pass filter (C++17).
 */

#include "leapfrog.hpp"
#include <iostream>
#include <iomanip>
#include <vector>

int main() {
    std::cout << "Leapfrog low-pass filter demo (C++17)\n";
    std::cout << "Order 5, cutoff ≈ 800 Hz, Fs = 48 kHz\n";
    std::cout << std::string(50, '-') << "\n";

    LeapfrogLowpass f(5, 800.0, 48000.0);

    constexpr int N = 32;
    for (int i = 0; i < N; ++i) {
        double x = (i == 0) ? 1.0 : 0.0;
        double y = f.process(x);
        std::cout << "sample[" << std::setw(2) << i << "] = "
                  << std::fixed << std::setprecision(6) << y << "\n";
    }

    std::cout << "\nDone.\n";
    return 0;
}
