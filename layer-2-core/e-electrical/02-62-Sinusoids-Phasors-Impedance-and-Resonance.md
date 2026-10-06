---
chapter: "02-62"
title: "Sinusoids, Phasors, Impedance, and Resonance"
layer: 2
tier: E
template: technical
ledger_ids: [ELEC-2E-062-01, ELEC-2E-062-02, ELEC-2E-062-03, ELEC-2E-062-04, ELEC-2E-062-05, ELEC-2E-062-06, ELEC-2E-062-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-62: Sinusoids, Phasors, Impedance, and Resonance

> *"Electrical problems become much easier when references, topology, energy flow, and the correct steady-state or transient model are established before algebra."*

---

## Before You Start

**Prerequisites:** 02-61 Capacitance and Inductance · 01-12 Complex Numbers and Phasor Prerequisites

**Skip if:** You can identify the governing electrical model, choose correct voltage/current references, use the FE Handbook relation, solve representative FE-level calculations, and verify power, units, and physical behavior.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives sinusoidal frequency/period relations, average and RMS values, phasor transforms, impedance/admittance of R/L/C elements, series/parallel combination rules, AC maximum-power transfer, and series/parallel resonance relations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **62.1** Explain and apply **Sinusoidal Waveforms, Frequency, Period, and Phase**.
* **62.2** Explain and apply **Average and RMS Values**.
* **62.3** Explain and apply **Phasor Representation**.
* **62.4** Explain and apply **Impedance and Admittance of R, L, and C**.
* **62.5** Explain and apply **Series and Parallel AC Networks**.
* **62.6** Explain and apply **Series and Parallel Resonance**.
* **62.7** Explain and apply **AC Maximum Power Transfer**.

---

## Notation Used Here

Voltage polarities and current directions are reference choices. RMS quantities are used for AC power unless otherwise stated. Use SI units unless a problem explicitly supplies another system.

---

## 62.1 Sinusoidal Waveforms, Frequency, Period, and Phase

A sinusoid is specified by amplitude, angular frequency, and phase. Frequency \(f\) in hertz and period \(T\) are reciprocals, with \(\omega=2\pi f\).

Phase compares the timing of sinusoids at the same frequency. A phase lead means the waveform reaches corresponding points earlier in time.

\[x(t)=X_{\max}\cos(\omega t+\phi),\qquad f=\frac1T=\frac{\omega}{2\pi}\]

![FIG-02-62-001: Two sinusoidal waveforms with amplitude, period, angular frequency, and phase difference labeled.](../figures/FIG-02-62-001-sinusoidal-waveforms-frequency-period-and-phase.png)

### Worked Example 1

**Problem.** A sinusoid has f=60 Hz. Find period and angular frequency.

**Solution.** T=1/60=16.67 ms; ω=2π60=377 rad/s.

---

## 62.2 Average and RMS Values

Average value is the time average over one period. RMS is the square-root of the mean square and is the effective value for resistive heating.

For a sinusoid, \(X_{rms}=X_{\max}/\sqrt2\).

\[X_{\rm rms}=\sqrt{\frac1T\int_0^T x^2(t)\,dt},\qquad X_{\rm rms}=\frac{X_{\max}}{\sqrt2}\ \text{for a sinusoid}\]

![FIG-02-62-002: Sinusoid annotated with peak, RMS level, average over a full cycle, and period.](../figures/FIG-02-62-002-average-and-rms-values.png)

### Worked Example 2

**Problem.** A sine wave has 170 V peak. Find RMS voltage.

**Solution.** Vrms=170/√2=120.2 V.

---

## 62.3 Phasor Representation

A phasor represents sinusoidal magnitude and phase at one frequency as a complex number, suppressing the common time factor. Differential equations for steady-state sinusoidal circuits become algebraic impedance equations.

Do not mix peak-value phasors with RMS-value phasors in the same calculation.

\[\underline V=V_{\rm rms}\angle\phi_V,\qquad \underline I=I_{\rm rms}\angle\phi_I\]

![FIG-02-62-003: Time-domain sinusoid paired with rotating-vector/complex-plane phasor representation.](../figures/FIG-02-62-003-phasor-representation.png)

### Worked Example 3

**Problem.** Convert 10∠30° to rectangular form.

**Solution.** 8.66+j5.00.

---

## 62.4 Impedance and Admittance of R, L, and C

Impedance is the phasor voltage-to-current ratio. Resistors have real impedance, inductors positive imaginary reactance, and capacitors negative imaginary reactance.

Admittance is the reciprocal of impedance and is often convenient for parallel networks.

\[Z_R=R,\qquad Z_L=j\omega L,\qquad Z_C=\frac1{j\omega C},\qquad Y=\frac1Z\]

![FIG-02-62-004: Complex impedance plane with resistor, inductive, and capacitive impedance directions.](../figures/FIG-02-62-004-impedance-and-admittance-of-r-l-and-c.png)

### Worked Example 4

**Problem.** Find XL for L=0.10 H at 60 Hz.

**Solution.** XL=ωL=37.7 Ω.

---

## 62.5 Series and Parallel AC Networks

Series impedances add directly. Parallel impedances combine reciprocally, or their admittances add directly.

Once equivalent impedance is known, apply phasor Ohm's law \(\underline V=\underline I Z\).

\[Z_s=\sum Z_i,\qquad Y_p=\sum Y_i,\qquad \underline I=\frac{\underline V}{Z_{eq}}\]

![FIG-02-62-005: Series RLC and parallel RLC networks reduced using impedance and admittance.](../figures/FIG-02-62-005-series-and-parallel-ac-networks.png)

### Worked Example 5

**Problem.** Find XC for C=100 µF at 60 Hz.

**Solution.** XC=1/(ωC)=26.5 Ω.

---

## 62.6 Series and Parallel Resonance

Ideal RLC resonance occurs when inductive and capacitive reactances cancel. Both series and parallel resonance share the ideal resonant frequency \( \omega_0=1/\sqrt{LC}\).

At series resonance the input impedance is purely resistive and minimum for the simple series RLC case; the Handbook also gives bandwidth and quality-factor relations.

\[\omega_0=\frac1{\sqrt{LC}},\qquad f_0=\frac1{2\pi\sqrt{LC}}\]

![FIG-02-62-006: Series-RLC impedance/current versus frequency with resonant frequency, bandwidth, and Q marked.](../figures/FIG-02-62-006-series-and-parallel-resonance.png)

### Worked Example 6

**Problem.** For L=0.10 H and C=100 µF, find ideal resonant frequency.

**Solution.** f0=1/(2π√LC)=50.3 Hz.

---

## 62.7 AC Maximum Power Transfer

For an AC Thévenin source, maximum average power transfer occurs when the load impedance equals the complex conjugate of the source Thévenin impedance.

This condition cancels the load/source reactance pair and matches the resistive parts.

\[Z_L=Z_{Th}^{*}\]

![FIG-02-62-007: Complex Thévenin source impedance and conjugate-matched load on the complex plane.](../figures/FIG-02-62-007-ac-maximum-power-transfer.png)

### Worked Example 7

**Problem.** A Thévenin impedance is 4+j3 Ω. What load impedance gives AC maximum power transfer?

**Solution.** ZL=4-j3 Ω.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A series circuit has R=10 Ω and XL-XC=10 Ω. Find |Z| and phase angle.

**Solution.** |Z|=14.14 Ω; θ=45° inductive.

### Worked Example 9

**Problem.** A 120 V RMS source sees Z=30∠-20° Ω. Find current phasor.

**Solution.** I=4∠20° A.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Electrical and Computer Engineering, printed pp. 365–368**.

**Source boundary:** The Handbook directly gives sinusoidal frequency/period relations, average and RMS values, phasor transforms, impedance/admittance of R/L/C elements, series/parallel combination rules, AC maximum-power transfer, and series/parallel resonance relations.

---

## Where This Goes Wrong

**Using sinusoidal waveform without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using RMS value without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using phasor representation without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using electrical impedance without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using AC network reduction without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using electrical resonance without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using AC maximum power transfer without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Skipping a power or conservation check.** A circuit solution should satisfy KCL/KVL where applicable and should not create unexplained power.


---

## Key Terms

| Term | Working definition |
|---|---|
| sinusoidal waveform | Concept developed in §62.1; use the section definition and stated conditions. |
| RMS value | Concept developed in §62.2; use the section definition and stated conditions. |
| phasor representation | Concept developed in §62.3; use the section definition and stated conditions. |
| electrical impedance | Concept developed in §62.4; use the section definition and stated conditions. |
| AC network reduction | Concept developed in §62.5; use the section definition and stated conditions. |
| electrical resonance | Concept developed in §62.6; use the section definition and stated conditions. |
| AC maximum power transfer | Concept developed in §62.7; use the section definition and stated conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **sinusoidal waveform** and state its governing equation or condition.

2. Define **RMS value** and state its governing equation or condition.

3. Define **phasor representation** and state its governing equation or condition.

4. Define **electrical impedance** and state its governing equation or condition.

5. Define **AC network reduction** and state its governing equation or condition.

6. Define **electrical resonance** and state its governing equation or condition.

7. Define **AC maximum power transfer** and state its governing equation or condition.

8. What is a common analysis error involving **sinusoidal waveform**?

9. What is a common analysis error involving **RMS value**?

10. What is a common analysis error involving **phasor representation**?

11. What is a common analysis error involving **electrical impedance**?

12. What is a common analysis error involving **AC network reduction**?

13. What is a common analysis error involving **electrical resonance**?

14. What is a common analysis error involving **AC maximum power transfer**?

15. Why must voltage polarity and current direction be defined before using signed power?

16. What conservation principle should be used as an independent circuit or machine check?

17. When should a Handbook equation be preferred over a remembered shortcut?

18. Why should RMS and peak values not be mixed in AC power or impedance calculations?

### Multiple Choice

19. Which statement is most accurate for **sinusoidal waveform**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

20. Which statement is most accurate for **RMS value**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

21. Which statement is most accurate for **phasor representation**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

22. Which statement is most accurate for **electrical impedance**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

23. Which statement is most accurate for **AC network reduction**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

24. Which statement is most accurate for **electrical resonance**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

25. Which statement is most accurate for **AC maximum power transfer**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

26. Which statement is most accurate for **sinusoidal waveform**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

27. Which statement is most accurate for **RMS value**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **sinusoidal waveform** is developed in §62.1. Use the displayed relation together with its stated sign convention and assumptions.

2. **RMS value** is developed in §62.2. Use the displayed relation together with its stated sign convention and assumptions.

3. **phasor representation** is developed in §62.3. Use the displayed relation together with its stated sign convention and assumptions.

4. **electrical impedance** is developed in §62.4. Use the displayed relation together with its stated sign convention and assumptions.

5. **AC network reduction** is developed in §62.5. Use the displayed relation together with its stated sign convention and assumptions.

6. **electrical resonance** is developed in §62.6. Use the displayed relation together with its stated sign convention and assumptions.

7. **AC maximum power transfer** is developed in §62.7. Use the displayed relation together with its stated sign convention and assumptions.

8. Applying **sinusoidal waveform** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

9. Applying **RMS value** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

10. Applying **phasor representation** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

11. Applying **electrical impedance** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

12. Applying **AC network reduction** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

13. Applying **electrical resonance** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

14. Applying **AC maximum power transfer** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

15. Because the sign of power depends on the chosen voltage/current references and the passive sign convention.

16. Charge/KCL, energy/power balance, and where applicable KVL should close consistently.

17. Whenever the Handbook supplies the relation or when the shortcut's assumptions are uncertain.

18. They represent different magnitudes; mixing them introduces factors such as √2 and gives incorrect power.

19. **A.** The chapter treats **sinusoidal waveform** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

20. **A.** The chapter treats **RMS value** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

21. **A.** The chapter treats **phasor representation** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

22. **A.** The chapter treats **electrical impedance** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

23. **A.** The chapter treats **AC network reduction** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

24. **A.** The chapter treats **electrical resonance** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

25. **A.** The chapter treats **AC maximum power transfer** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

26. **A.** The chapter treats **sinusoidal waveform** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

27. **A.** The chapter treats **RMS value** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.


---

## Practice Problems

1. A sinusoid has f=60 Hz. Find period and angular frequency.

2. A sine wave has 170 V peak. Find RMS voltage.

3. Convert 10∠30° to rectangular form.

4. Find XL for L=0.10 H at 60 Hz.

5. Find XC for C=100 µF at 60 Hz.

6. For L=0.10 H and C=100 µF, find ideal resonant frequency.

7. A Thévenin impedance is 4+j3 Ω. What load impedance gives AC maximum power transfer?

8. A series circuit has R=10 Ω and XL-XC=10 Ω. Find |Z| and phase angle.

9. A 120 V RMS source sees Z=30∠-20° Ω. Find current phasor.

10. At series resonance in an ideal RLC with R=8 Ω and 120 V RMS source, find current.


---

## Practice Problem Solutions

1. T=1/60=16.67 ms; ω=2π60=377 rad/s.

2. Vrms=170/√2=120.2 V.

3. 8.66+j5.00.

4. XL=ωL=37.7 Ω.

5. XC=1/(ωC)=26.5 Ω.

6. f0=1/(2π√LC)=50.3 Hz.

7. ZL=4-j3 Ω.

8. |Z|=14.14 Ω; θ=45° inductive.

9. I=4∠20° A.

10. I=120/8=15 A.


---

## Quick Reference

**Handbook anchor:** Electrical and Computer Engineering, printed pp. 365–368.

- **sinusoidal waveform:** Sinusoidal Waveforms, Frequency, Period, and Phase
- **RMS value:** Average and RMS Values
- **phasor representation:** Phasor Representation
- **electrical impedance:** Impedance and Admittance of R, L, and C
- **AC network reduction:** Series and Parallel AC Networks
- **electrical resonance:** Series and Parallel Resonance
- **AC maximum power transfer:** AC Maximum Power Transfer
---

## What's Next

**02-63 — AC Power, Power Factor, and Three-Phase Systems**

Carry forward the electrical workflow: define voltage/current references and topology, choose the correct DC/AC or transient model, apply the Handbook relation, and close with conservation and power checks.

— Your Mentor