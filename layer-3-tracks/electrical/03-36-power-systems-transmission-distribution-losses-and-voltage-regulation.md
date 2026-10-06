---
chapter: "03-36"
title: "Power Systems — Transmission, Distribution, Losses, and Voltage Regulation"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-036-01, ECE-3-036-02, ECE-3-036-03, ECE-3-036-04, ECE-3-036-05, ECE-3-036-06, ECE-3-036-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-36: Power Systems — Transmission, Distribution, Losses, and Voltage Regulation

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ELEC-2E-063-07 · ELEC-2E-064-07 · ELEC-2E-065-07

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Power Systems — Transmission, Distribution, Losses, and Voltage Regulation**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **36.1** Explain and apply **Single-phase and complex power review for power systems**.
* **36.2** Explain and apply **Balanced three-phase power and line/phase relations**.
* **36.3** Explain and apply **Transmission/distribution voltage drop and losses**.
* **36.4** Explain and apply **Power factor correction and reactive compensation**.
* **36.5** Explain and apply **Ideal transformers and reflected impedance**.
* **36.6** Explain and apply **Synchronous, induction, and DC machine system roles**.
* **36.7** Explain and apply **Voltage regulation, efficiency, and system-level checks**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 36.1 Single-phase and complex power review for power systems

Power systems use complex power to track real power, reactive power, apparent power, and power factor. The sign convention for reactive power must be consistent.

\[S=VI^*=P+jQ,\qquad |S|=VI\]

![FIG-03-36-001: Complex-power triangle with P, Q, S, and lagging/leading power-factor angle.](../figures/FIG-03-36-001-single-phase-and-complex-power-review-for-power-systems.png)

### Worked Example 1

**Problem.** At 120 V, 10 A, pf=0.8 lagging, P=960 W and |S|=1200 VA.

**Solution.** Use the relation and model in §36.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 36.2 Balanced three-phase power and line/phase relations

Balanced three-phase systems permit compact line-based power calculations. Wye and delta connections have different line-to-phase voltage/current relationships.

\[P=\sqrt3\,V_L I_L\cos\theta\]

![FIG-03-36-002: Wye and delta source/load connections with line and phase voltage/current relationships.](../figures/FIG-03-36-002-balanced-three-phase-power-and-line-phase-relations.png)

### Worked Example 2

**Problem.** At 480 V line-line, 100 A, pf=0.9, P≈74.8 kW.

**Solution.** Use the relation and model in §36.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 36.3 Transmission/distribution voltage drop and losses

Higher transmission voltage reduces current for a given real power, which reduces I²R loss and voltage drop. Reactive flow also affects voltage profile.

\[\Delta V\approx I(R+jX),\qquad P_{\text{loss}}=I^2R\]

![FIG-03-36-003: Radial feeder with sending voltage, line impedance, load power factor, voltage drop, and I²R loss annotations.](../figures/FIG-03-36-003-transmission-distribution-voltage-drop-and-losses.png)

### Worked Example 3

**Problem.** Halving current reduces resistive line loss by a factor of four.

**Solution.** Use the relation and model in §36.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 36.4 Power factor correction and reactive compensation

Shunt capacitive compensation can reduce lagging reactive demand, lower line current, and improve voltage profile. Avoid overcorrection into an undesired leading condition.

\[Q_c=P(\tan\theta_1-\tan\theta_2)\]

![FIG-03-36-004: Industrial load with shunt capacitor bank and before/after power triangles.](../figures/FIG-03-36-004-power-factor-correction-and-reactive-compensation.png)

### Worked Example 4

**Problem.** Correcting from pf 0.8 to 0.95 reduces the reactive power carried by the source.

**Solution.** Use the relation and model in §36.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 36.5 Ideal transformers and reflected impedance

Ideal transformers change voltage/current levels while conserving power. Reflected impedance enables analysis of a load from the primary side.

\[\frac{V_S}{V_P}=\frac{N_2}{N_1},\qquad Z_P=a^2Z_S\]

![FIG-03-36-005: Ideal transformer with turns ratio, current directions, voltage polarities, and reflected load impedance.](../figures/FIG-03-36-005-ideal-transformers-and-reflected-impedance.png)

### Worked Example 5

**Problem.** A 10:1 turns ratio reflects a 4-Ω secondary load as 400 Ω to the primary if a=N1/N2=10.

**Solution.** Use the relation and model in §36.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 36.6 Synchronous, induction, and DC machine system roles

Power systems use synchronous generators, induction motors, and DC machines in different roles. Synchronous speed is set by frequency and pole count; induction-machine slip measures rotor-speed departure from synchronous speed.

\[n_s=\frac{120f}{p},\qquad s=\frac{n_s-n}{n_s}\]

![FIG-03-36-006: Synchronous generator, induction motor, and DC machine with key power-flow and speed relationships.](../figures/FIG-03-36-006-synchronous-induction-and-dc-machine-system-roles.png)

### Worked Example 6

**Problem.** At 60 Hz with 4 poles, synchronous speed is 1800 rpm.

**Solution.** Use the relation and model in §36.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 36.7 Voltage regulation, efficiency, and system-level checks

Voltage regulation compares no-load and full-load voltage. A complete power-system answer should also check loss, current rating, power factor, and equipment limits.

\[\%\mathrm{VR}=100\frac{V_{NL}-V_{FL}}{V_{FL}}\]

![FIG-03-36-007: Source/load voltage profile from no load to full load with voltage-regulation definition.](../figures/FIG-03-36-007-voltage-regulation-efficiency-and-system-level-checks.png)

### Worked Example 7

**Problem.** If VNL=125 V and VFL=120 V, regulation is 4.17%.

**Solution.** Use the relation and model in §36.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

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

Primary source basis: **FE Electrical and Computer specification Area 10; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using power-system complex power outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using balanced three-phase power outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using line voltage drop outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using power factor correction outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using transformer reflected impedance outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using electric machines in power systems outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using power-system voltage regulation outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| power-system complex power | Concept developed in §36.1; apply with that section's stated model and conventions. |
| balanced three-phase power | Concept developed in §36.2; apply with that section's stated model and conventions. |
| line voltage drop | Concept developed in §36.3; apply with that section's stated model and conventions. |
| power factor correction | Concept developed in §36.4; apply with that section's stated model and conventions. |
| transformer reflected impedance | Concept developed in §36.5; apply with that section's stated model and conventions. |
| electric machines in power systems | Concept developed in §36.6; apply with that section's stated model and conventions. |
| power-system voltage regulation | Concept developed in §36.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **power-system complex power** and identify the governing relation, state variable, or decision it organizes.

2. Define **balanced three-phase power** and identify the governing relation, state variable, or decision it organizes.

3. Define **line voltage drop** and identify the governing relation, state variable, or decision it organizes.

4. Define **power factor correction** and identify the governing relation, state variable, or decision it organizes.

5. Define **transformer reflected impedance** and identify the governing relation, state variable, or decision it organizes.

6. Define **electric machines in power systems** and identify the governing relation, state variable, or decision it organizes.

7. Define **power-system voltage regulation** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **power-system complex power**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **balanced three-phase power**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **line voltage drop**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **power factor correction**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **transformer reflected impedance**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **electric machines in power systems**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **power-system voltage regulation**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **power-system complex power**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **balanced three-phase power**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **line voltage drop**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **power factor correction**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **transformer reflected impedance**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **electric machines in power systems**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **power-system voltage regulation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **power-system complex power**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **balanced three-phase power**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **power-system complex power** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **balanced three-phase power** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **line voltage drop** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **power factor correction** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **transformer reflected impedance** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **electric machines in power systems** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **power-system voltage regulation** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **power-system complex power**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **balanced three-phase power**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **line voltage drop**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **power factor correction**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **transformer reflected impedance**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **electric machines in power systems**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **power-system voltage regulation**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

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

1. At 120 V, 10 A, pf=0.8 lagging, P=960 W and |S|=1200 VA.

2. At 480 V line-line, 100 A, pf=0.9, P≈74.8 kW.

3. Halving current reduces resistive line loss by a factor of four.

4. Correcting from pf 0.8 to 0.95 reduces the reactive power carried by the source.

5. A 10:1 turns ratio reflects a 4-Ω secondary load as 400 Ω to the primary if a=N1/N2=10.

6. At 60 Hz with 4 poles, synchronous speed is 1800 rpm.

7. If VNL=125 V and VFL=120 V, regulation is 4.17%.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §36.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §36.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §36.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §36.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §36.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §36.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §36.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 10, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 10.

- **power-system complex power:** Single-phase and complex power review for power systems
- **balanced three-phase power:** Balanced three-phase power and line/phase relations
- **line voltage drop:** Transmission/distribution voltage drop and losses
- **power factor correction:** Power factor correction and reactive compensation
- **transformer reflected impedance:** Ideal transformers and reflected impedance
- **electric machines in power systems:** Synchronous, induction, and DC machine system roles
- **power-system voltage regulation:** Voltage regulation, efficiency, and system-level checks

---

## What's Next

**Chapter 03-37: Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
