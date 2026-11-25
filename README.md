# Leapfrog Filter

A simple, educational implementation of a **leapfrog low-pass filter** topology in Python and C++17.

This repository demonstrates the classic analog leapfrog (ladder) structure that appears in continuous-time filter literature, including the fifth-order example referenced in US Patent 4,509,019.

## Patent Reference

**US Patent 4,509,019**  
**Title:** Tunable active filter  
**Inventors:** Mihai Banu, Yannis Tsividis  
**Assignee:** AT&T Bell Laboratories  
**Filed:** 27 January 1983  
**Issued:** 2 April 1985  
**Status:** Expired (patent term long completed)

The patent describes a balanced (fully differential) active-RC technique for realizing tunable continuous-time filters on integrated circuits. One of the figures (FIG. 8 / FIG. 9 in the patent literature) shows a fifth-order leapfrog / ladder low-pass filter realized with that balanced technique.

This repository does **not** implement the patented balanced MOS-C circuitry.  
It implements a straightforward digital simulation of the classic **leapfrog topology** itself (a public, well-known analog filter structure that predates and is independent of the specific patent claims).

The patent is cited only for historical and educational context.

## What is a Leapfrog Filter?

The leapfrog (or “active ladder”) topology maps a passive LC ladder network into a set of interconnected integrators with local feedback.  
It is valued for low sensitivity to component variations and good dynamic range.

A typical odd-order low-pass leapfrog consists of a chain of integrators where:
- Each integrator receives the previous stage output and a feedback from the next stage.
- The final output is taken from the last integrator.
- Cut-off frequency and Q are set by the integrator time-constants and feedback coefficients.

## Repository Contents

```
leapfrog-filter/
├── README.md                 # This file
├── LICENSE                   # MIT
├── docs/
│   └── patent-notes.md       # Short notes on US 4,509,019
├── src/
│   ├── python/
│   │   └── leapfrog.py       # Pure-Python implementation + demo
│   └── cpp/
│       ├── leapfrog.hpp      # Header-only C++17 implementation
│       └── main.cpp          # Example driver
└── examples/
    └── plot_response.py      # Optional frequency-response plot (needs numpy/matplotlib)
```

## Building & Running

### Python
```bash
cd src/python
python3 leapfrog.py
```

### C++17
```bash
cd src/cpp
g++ -std=c++17 -O2 -o leapfrog main.cpp
./leapfrog
```

Both demos generate a short impulse response and print a few samples.

## License

MIT License – see `LICENSE`.

## Disclaimer

This is an independent educational implementation of a classic public filter topology.  
It is **not** affiliated with, endorsed by, or derived from FabFilter, AT&T, or any commercial product.  
No proprietary code or assets are included.
