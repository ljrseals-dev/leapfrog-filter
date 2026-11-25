# Notes on US Patent 4,509,019

**Tunable active filter**  
Mihai Banu & Yannis Tsividis  
AT&T Bell Laboratories  
Filed 27 Jan 1983 – Issued 2 Apr 1985  
Expired.

## What the patent covers

The patent teaches a **balanced (fully differential) active-RC filter** technique suitable for MOS integrated circuits.  
Key ideas:

- Use of a balanced amplifier with electronically controlled resistances (MOS transistors) and capacitors.
- Distortion cancellation through the differential structure.
- Ability to realize both low-pass and high-pass responses by swapping the placement of capacitors and controlled resistances.
- On-chip tuning referenced to a precision source (clock or resistor).

One of the example circuits is a fifth-order low-pass filter drawn in leapfrog / ladder form (see the patent figures, typically labelled FIG. 8 and FIG. 9 in the literature).

## What this repository implements

This repository implements a **digital simulation of the classic leapfrog topology**, not the patented balanced MOS-C circuitry.

The leapfrog structure itself is a public, textbook analog-filter topology that has been known and used for decades.  
The patent is referenced only for historical context because it contains a clear leapfrog example.

## Legal status

US patents filed before 8 June 1995 had a term of 17 years from grant (or 20 years from filing under transitional rules).  
Patent 4,509,019 was issued in 1985 and has long expired.  
Even while it was in force, it covered a specific analog integrated-circuit technique, not digital software implementations of the leapfrog idea.
