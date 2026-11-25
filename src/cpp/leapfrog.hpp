#pragma once
/**
 * Leapfrog low-pass filter – educational C++17 implementation.
 *
 * Classic odd-order leapfrog (active-ladder) topology simulated with
 * simple forward-Euler integrators.  Public textbook structure.
 */

#include <vector>
#include <cmath>
#include <stdexcept>
#include <cstddef>

class LeapfrogLowpass {
public:
    LeapfrogLowpass(int order = 5, double cutoff_hz = 1000.0, double sample_rate = 48000.0)
        : order_(order), sample_rate_(sample_rate), cutoff_(cutoff_hz)
    {
        if (order < 1 || order % 2 == 0) {
            throw std::invalid_argument("order must be a positive odd integer");
        }

        const double w0 = 2.0 * M_PI * cutoff_hz / sample_rate;
        g_.resize(static_cast<size_t>(order));
        state_.assign(static_cast<size_t>(order), 0.0);

        for (int i = 0; i < order; ++i) {
            g_[static_cast<size_t>(i)] = w0 * (1.0 + 0.3 * std::abs(i - order / 2));
        }
    }

    double process(double x) {
        // First integrator
        if (order_ > 1) {
            state_[0] += g_[0] * (x - state_[0] - state_[1]);
        } else {
            state_[0] += g_[0] * (x - state_[0]);
        }

        // Intermediate integrators
        for (int i = 1; i < order_ - 1; ++i) {
            state_[static_cast<size_t>(i)] += g_[static_cast<size_t>(i)] *
                (state_[static_cast<size_t>(i - 1)] - state_[static_cast<size_t>(i)] - state_[static_cast<size_t>(i + 1)]);
        }

        // Last integrator
        if (order_ > 1) {
            state_[static_cast<size_t>(order_ - 1)] += g_[static_cast<size_t>(order_ - 1)] *
                (state_[static_cast<size_t>(order_ - 2)] - state_[static_cast<size_t>(order_ - 1)]);
        }

        return state_[static_cast<size_t>(order_ - 1)];
    }

    void process_block(const double* in, double* out, std::size_t n) {
        for (std::size_t i = 0; i < n; ++i) {
            out[i] = process(in[i]);
        }
    }

    void reset() {
        std::fill(state_.begin(), state_.end(), 0.0);
    }

    int order() const { return order_; }

private:
    int order_;
    double sample_rate_;
    double cutoff_;
    std::vector<double> g_;
    std::vector<double> state_;
};
