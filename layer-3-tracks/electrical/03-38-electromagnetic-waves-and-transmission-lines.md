---
chapter: "03-38"
title: "Electromagnetic Waves and Transmission Lines"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-038-01, ECE-3-038-02, ECE-3-038-03, ECE-3-038-04, ECE-3-038-05, ECE-3-038-06, ECE-3-038-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-38: Electromagnetic Waves and Transmission Lines

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-037-07 · ELEC-2E-062-01

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Electromagnetic Waves and Transmission Lines**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **38.1** Explain and apply **Wave speed, frequency, wavelength, and phase constant**.
* **38.2** Explain and apply **Lossless transmission-line characteristic impedance**.
* **38.3** Explain and apply **Load reflection coefficient**.
* **38.4** Explain and apply **Standing waves and SWR**.
* **38.5** Explain and apply **Input impedance versus line length**.
* **38.6** Explain and apply **Matched lines, power transfer, and termination**.
* **38.7** Explain and apply **When distributed behavior matters**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 38.1 Wave speed, frequency, wavelength, and phase constant

A sinusoidal wave advances one wavelength in one period. Propagation speed depends on the medium; phase constant measures radians of phase change per unit length.

\[\lambda=\frac{u}{f},\qquad \beta=\frac{2\pi}{\lambda}\]

![FIG-03-38-001: Sinusoidal traveling wave with wavelength, propagation direction, phase reference, frequency, and velocity.](../figures/FIG-03-38-001-wave-speed-frequency-wavelength-and-phase-constant.png)

### Worked Example 1

**Problem.** At 100 MHz in free space, wavelength is approximately 3 m.

**Solution.** Use the relation and model in §38.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 38.2 Lossless transmission-line characteristic impedance

Characteristic impedance is the voltage-to-current ratio of a single traveling wave on a lossless line. It is not the DC resistance of the conductors.

\[Z_0=\sqrt{\frac{L'}{C'}}\]

![FIG-03-38-002: Distributed L'-C' transmission-line segment and forward traveling voltage/current wave defining Z0.](../figures/FIG-03-38-002-lossless-transmission-line-characteristic-impedance.png)

### Worked Example 2

**Problem.** If L'=250 nH/m and C'=100 pF/m, Z0=50 Ω.

**Solution.** Use the relation and model in §38.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 38.3 Load reflection coefficient

A mismatch causes part of the incident wave to reflect. The magnitude of Γ indicates reflection strength and its angle determines reflected phase.

\[\Gamma_L=\frac{Z_L-Z_0}{Z_L+Z_0}\]

![FIG-03-38-003: Incident and reflected waves at a mismatched load with Z0, ZL, V+, V-, and ΓL.](../figures/FIG-03-38-003-load-reflection-coefficient.png)

### Worked Example 3

**Problem.** For ZL=Z0, ΓL=0 and there is no load reflection.

**Solution.** Use the relation and model in §38.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 38.4 Standing waves and SWR

Incident and reflected waves interfere to produce standing-wave maxima and minima. SWR equals 1 for a perfect match and grows with mismatch.

\[\mathrm{SWR}=\frac{1+|\Gamma|}{1-|\Gamma|}\]

![FIG-03-38-004: Voltage envelope along a transmission line showing maxima, minima, wavelength relation, and SWR.](../figures/FIG-03-38-004-standing-waves-and-swr.png)

### Worked Example 4

**Problem.** If |Γ|=0.5, SWR=3.

**Solution.** Use the relation and model in §38.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 38.5 Input impedance versus line length

A transmission line transforms load impedance as a function of electrical length. At high frequency, a physically short line can no longer be treated as a lumped wire.

\[Z_{in}=Z_0\frac{Z_L+jZ_0\tan(\beta l)}{Z_0+jZ_L\tan(\beta l)}\]

![FIG-03-38-005: Transmission line of length l between source and load with Zin, Z0, ZL, and electrical length βl.](../figures/FIG-03-38-005-input-impedance-versus-line-length.png)

### Worked Example 5

**Problem.** A quarter-wave line can strongly transform impedance even though the load itself is unchanged.

**Solution.** Use the relation and model in §38.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 38.6 Matched lines, power transfer, and termination

Matching suppresses reflections and maximizes forward power delivery under the line model. Termination strategy depends on frequency, line length, and source/load impedances.

\[Z_L=Z_0\Rightarrow \Gamma=0\]

![FIG-03-38-006: Source, transmission line, and matched/mismatched terminations with reflected-wave outcomes.](../figures/FIG-03-38-006-matched-lines-power-transfer-and-termination.png)

### Worked Example 6

**Problem.** A 50-Ω coaxial line terminated in 50 Ω is matched at the load.

**Solution.** Use the relation and model in §38.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 38.7 When distributed behavior matters

Lumped-circuit assumptions degrade when interconnect electrical length becomes a significant fraction of wavelength. Rise time can make digital interconnects transmission-line problems even when clock frequency seems modest.

\[\theta=\beta l=\frac{2\pi l}{\lambda}\]

![FIG-03-38-007: Chart of physical length versus wavelength/electrical length showing lumped and transmission-line regimes.](../figures/FIG-03-38-007-when-distributed-behavior-matters.png)

### Worked Example 7

**Problem.** A 0.3-m trace is electrically much longer at 1 GHz than at 1 MHz.

**Solution.** Use the relation and model in §38.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation gives a numerical answer but violates the assumed device region, logic state, or protocol condition. Is the answer valid?

**Solution.** No. Re-select the appropriate piecewise model or system state and solve again. Algebraic consistency does not override the model's validity conditions.

### Worked Example 9

**Problem.** A remembered formula differs from the expression printed in the FE Reference Handbook. Which should govern an exam solution?

**Solution.** Use the Handbook expression and its definitions unless the problem explicitly supplies a different model.

---

## As the Handbook States It

Primary source basis: **FE Electrical and Computer specification Area 11; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using electromagnetic wavelength outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using characteristic impedance outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using load reflection coefficient outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using standing wave ratio outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using transmission-line input impedance outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using transmission-line matching outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using electrical length outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| electromagnetic wavelength | Concept developed in §38.1; apply with that section's stated model and conventions. |
| characteristic impedance | Concept developed in §38.2; apply with that section's stated model and conventions. |
| load reflection coefficient | Concept developed in §38.3; apply with that section's stated model and conventions. |
| standing wave ratio | Concept developed in §38.4; apply with that section's stated model and conventions. |
| transmission-line input impedance | Concept developed in §38.5; apply with that section's stated model and conventions. |
| transmission-line matching | Concept developed in §38.6; apply with that section's stated model and conventions. |
| electrical length | Concept developed in §38.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **electromagnetic wavelength** and identify the governing relation, state variable, or decision it organizes.

2. Define **characteristic impedance** and identify the governing relation, state variable, or decision it organizes.

3. Define **load reflection coefficient** and identify the governing relation, state variable, or decision it organizes.

4. Define **standing wave ratio** and identify the governing relation, state variable, or decision it organizes.

5. Define **transmission-line input impedance** and identify the governing relation, state variable, or decision it organizes.

6. Define **transmission-line matching** and identify the governing relation, state variable, or decision it organizes.

7. Define **electrical length** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **electromagnetic wavelength**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **characteristic impedance**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **load reflection coefficient**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **standing wave ratio**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **transmission-line input impedance**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **transmission-line matching**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **electrical length**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **electromagnetic wavelength**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **characteristic impedance**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **load reflection coefficient**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **standing wave ratio**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **transmission-line input impedance**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **transmission-line matching**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **electrical length**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **electromagnetic wavelength**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **characteristic impedance**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **electromagnetic wavelength** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **characteristic impedance** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **load reflection coefficient** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **standing wave ratio** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **transmission-line input impedance** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **transmission-line matching** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **electrical length** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **electromagnetic wavelength**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **characteristic impedance**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **load reflection coefficient**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **standing wave ratio**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **transmission-line input impedance**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **transmission-line matching**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **electrical length**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

15. The same symbol or equation can represent different physical behavior outside its valid device region, frequency range, timing model, or protocol abstraction.

16. The Handbook is the exam reference; using its definitions prevents hidden differences in constants, RMS/peak values, sign convention, or model form.

17. Algebra can be internally consistent while predicting an impossible device state, voltage, timing relationship, address range, or complexity claim. The physical/logical model must also be satisfied.

18. Limiting cases and order-of-magnitude checks expose sign errors, impossible gains, invalid probabilities, unrealistic timing, and model misuse.

19. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

20. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

21. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

22. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

23. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

24. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

25. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

26. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

27. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.


---

## Practice Problems

1. At 100 MHz in free space, wavelength is approximately 3 m.

2. If L'=250 nH/m and C'=100 pF/m, Z0=50 Ω.

3. For ZL=Z0, ΓL=0 and there is no load reflection.

4. If |Γ|=0.5, SWR=3.

5. A quarter-wave line can strongly transform impedance even though the load itself is unchanged.

6. A 50-Ω coaxial line terminated in 50 Ω is matched at the load.

7. A 0.3-m trace is electrically much longer at 1 GHz than at 1 MHz.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §38.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §38.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §38.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §38.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §38.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §38.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §38.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 11, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 11.

- **electromagnetic wavelength:** Wave speed, frequency, wavelength, and phase constant
- **characteristic impedance:** Lossless transmission-line characteristic impedance
- **load reflection coefficient:** Load reflection coefficient
- **standing wave ratio:** Standing waves and SWR
- **transmission-line input impedance:** Input impedance versus line length
- **transmission-line matching:** Matched lines, power transfer, and termination
- **electrical length:** When distributed behavior matters

---

## What's Next

**Chapter 03-39: Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
