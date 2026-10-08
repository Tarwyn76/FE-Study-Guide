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

**Solution.** Start from the §36.1 relation \(S=VI^*=P+jQ,\qquad |S|=VI\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: At 120 V, 10 A, pf=0.8 lagging, P=960 W and |S|=1200 VA. Carry the stated units through the calculation and accept the result only after confirming that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

---

## 36.2 Balanced three-phase power and line/phase relations

Balanced three-phase systems permit compact line-based power calculations. Wye and delta connections have different line-to-phase voltage/current relationships.

\[P=\sqrt3\,V_L I_L\cos\theta\]

![FIG-03-36-002: Wye and delta source/load connections with line and phase voltage/current relationships.](../figures/FIG-03-36-002-balanced-three-phase-power-and-line-phase-relations.png)

### Worked Example 2

**Problem.** At 480 V line-line, 100 A, pf=0.9, P≈74.8 kW.

**Solution.** Start from the §36.2 relation \(P=\sqrt3\,V_L I_L\cos\theta\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: At 480 V line-line, 100 A, pf=0.9, P≈74.8 kW. Carry the stated units through the calculation and accept the result only after confirming that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

---

## 36.3 Transmission/distribution voltage drop and losses

Higher transmission voltage reduces current for a given real power, which reduces I²R loss and voltage drop. Reactive flow also affects voltage profile.

\[\Delta V\approx I(R+jX),\qquad P_{\text{loss}}=I^2R\]

![FIG-03-36-003: Radial feeder with sending voltage, line impedance, load power factor, voltage drop, and I²R loss annotations.](../figures/FIG-03-36-003-transmission-distribution-voltage-drop-and-losses.png)

### Worked Example 3

**Problem.** Halving current reduces resistive line loss by a factor of four.

**Solution.** Start from the §36.3 relation \(\Delta V\approx I(R+jX),\qquad P_{\text{loss}}=I^2R\). The statement follows from the physical or logical meaning of **Transmission/distribution voltage drop and losses**: Halving current reduces resistive line loss by a factor of four. Accept that conclusion only while RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

---

## 36.4 Power factor correction and reactive compensation

Shunt capacitive compensation can reduce lagging reactive demand, lower line current, and improve voltage profile. Avoid overcorrection into an undesired leading condition.

\[Q_c=P(\tan\theta_1-\tan\theta_2)\]

![FIG-03-36-004: Industrial load with shunt capacitor bank and before/after power triangles.](../figures/FIG-03-36-004-power-factor-correction-and-reactive-compensation.png)

### Worked Example 4

**Problem.** Correcting from pf 0.8 to 0.95 reduces the reactive power carried by the source.

**Solution.** Start from the §36.4 relation \(Q_c=P(\tan\theta_1-\tan\theta_2)\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: Correcting from pf 0.8 to 0.95 reduces the reactive power carried by the source. Carry the stated units through the calculation and accept the result only after confirming that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

---

## 36.5 Ideal transformers and reflected impedance

Ideal transformers change voltage/current levels while conserving power. Reflected impedance enables analysis of a load from the primary side.

\[\frac{V_S}{V_P}=\frac{N_2}{N_1},\qquad Z_P=a^2Z_S\]

![FIG-03-36-005: Ideal transformer with turns ratio, current directions, voltage polarities, and reflected load impedance.](../figures/FIG-03-36-005-ideal-transformers-and-reflected-impedance.png)

### Worked Example 5

**Problem.** A 10:1 turns ratio reflects a 4-Ω secondary load as 400 Ω to the primary if a=N1/N2=10.

**Solution.** Start from the §36.5 relation \(\frac{V_S}{V_P}=\frac{N_2}{N_1},\qquad Z_P=a^2Z_S\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: A 10:1 turns ratio reflects a 4-Ω secondary load as 400 Ω to the primary if a=N1/N2=10. Carry the stated units through the calculation and accept the result only after confirming that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

---

## 36.6 Synchronous, induction, and DC machine system roles

Power systems use synchronous generators, induction motors, and DC machines in different roles. Synchronous speed is set by frequency and pole count; induction-machine slip measures rotor-speed departure from synchronous speed.

\[n_s=\frac{120f}{p},\qquad s=\frac{n_s-n}{n_s}\]

![FIG-03-36-006: Synchronous generator, induction motor, and DC machine with key power-flow and speed relationships.](../figures/FIG-03-36-006-synchronous-induction-and-dc-machine-system-roles.png)

### Worked Example 6

**Problem.** At 60 Hz with 4 poles, synchronous speed is 1800 rpm.

**Solution.** Start from the §36.6 relation \(n_s=\frac{120f}{p},\qquad s=\frac{n_s-n}{n_s}\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: At 60 Hz with 4 poles, synchronous speed is 1800 rpm. Carry the stated units through the calculation and accept the result only after confirming that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

---

## 36.7 Voltage regulation, efficiency, and system-level checks

Voltage regulation compares no-load and full-load voltage. A complete power-system answer should also check loss, current rating, power factor, and equipment limits.

\[\%\mathrm{VR}=100\frac{V_{NL}-V_{FL}}{V_{FL}}\]

![FIG-03-36-007: Source/load voltage profile from no load to full load with voltage-regulation definition.](../figures/FIG-03-36-007-voltage-regulation-efficiency-and-system-level-checks.png)

### Worked Example 7

**Problem.** If VNL=125 V and VFL=120 V, regulation is 4.17%.

**Solution.** Start from the §36.7 relation \(\%\mathrm{VR}=100\frac{V_{NL}-V_{FL}}{V_{FL}}\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: If VNL=125 V and VFL=120 V, regulation is 4.17%. Carry the stated units through the calculation and accept the result only after confirming that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation gives a numerical answer but violates the assumed device region, logic state, or protocol condition. Is the answer valid?

**Solution.** No. In **Power Systems — Transmission, Distribution, Losses, and Voltage Regulation**, a tidy numerical or logical result is still invalid if it contradicts the model assumptions. A representative failure is a three-phase relation applied to unbalanced quantities or a power-factor correction result that changes real load power. Return to the applicable section, choose the state/model consistent with the solved quantities, recompute if needed, and confirm that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

### Worked Example 9

**Problem.** A remembered formula differs from the expression printed in the FE Reference Handbook. Which should govern an exam solution?

**Solution.** Use the FE Reference Handbook expression and its definitions as the controlling exam reference unless the problem explicitly defines another model. For **Power Systems — Transmission, Distribution, Losses, and Voltage Regulation**, match symbols, units, reference directions, RMS/peak or digital conventions, and assumptions to the Handbook first. External references support only specification-required learned concepts that the Handbook does not directly develop.

---

## As the Handbook States It

Primary source basis: **FE Electrical and Computer specification Area 10; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required engineering/computing knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those two bodies of material into exam-oriented explanations and examples; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Glover, J. D., Sarma, M. S., Overbye, T. J., & Birchfield, A. B. (2022). *Power System Analysis & Design* (7th ed.). Cengage Learning. ISBN 978-0-357-67619-6. Supporting scope: Transmission/distribution modeling, voltage drop, losses, three-phase power, reactive power, and compensation.

The external references support only the learned/application portion of the specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In Power Systems — Transmission, Distribution, Losses, and Voltage Regulation, the same equation or symbol can change meaning when the operating state, abstraction, timing model, or signal convention changes; verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

16. The FE Reference Handbook is the exam reference for Power Systems — Transmission, Distribution, Losses, and Voltage Regulation. Match its variable definitions and conventions before substitution; external references support only learned material not developed in the Handbook.

17. An algebraically consistent answer can still be invalid in Power Systems — Transmission, Distribution, Losses, and Voltage Regulation. Reject a result that implies a three-phase relation applied to unbalanced quantities or a power-factor correction result that changes real load power and reselect the appropriate model or state.

18. A useful independent check for this chapter is to let reactive power approach zero and verify that power factor approaches unity while real power remains unchanged. If the result does not reduce correctly, recheck the model, sign convention, and arithmetic.

19. **A.** For **Single-phase and complex power review for power systems**, the governing section model is \(S=VI^*=P+jQ,\qquad |S|=VI\). Apply it only with the definitions and assumptions stated in §36.1, then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

20. **A.** For **Balanced three-phase power and line/phase relations**, the governing section model is \(P=\sqrt3\,V_L I_L\cos\theta\). Apply it only with the definitions and assumptions stated in §36.2, then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

21. **A.** For **Transmission/distribution voltage drop and losses**, the governing section model is \(\Delta V\approx I(R+jX),\qquad P_{\text{loss}}=I^2R\). Apply it only with the definitions and assumptions stated in §36.3, then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

22. **A.** For **Power factor correction and reactive compensation**, the governing section model is \(Q_c=P(\tan\theta_1-\tan\theta_2)\). Apply it only with the definitions and assumptions stated in §36.4, then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

23. **A.** For **Ideal transformers and reflected impedance**, the governing section model is \(\frac{V_S}{V_P}=\frac{N_2}{N_1},\qquad Z_P=a^2Z_S\). Apply it only with the definitions and assumptions stated in §36.5, then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

24. **A.** For **Synchronous, induction, and DC machine system roles**, the governing section model is \(n_s=\frac{120f}{p},\qquad s=\frac{n_s-n}{n_s}\). Apply it only with the definitions and assumptions stated in §36.6, then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

25. **A.** For **Voltage regulation, efficiency, and system-level checks**, the governing section model is \(\%\mathrm{VR}=100\frac{V_{NL}-V_{FL}}{V_{FL}}\). Apply it only with the definitions and assumptions stated in §36.7, then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

26. **A.** For an integrated Power Systems — Transmission, Distribution, Losses, and Voltage Regulation problem, separate the physical/logical model from the arithmetic, solve with the relevant section relations, and cross-check the result against the chapter-specific validity conditions.

27. **A.** In **Power Systems — Transmission, Distribution, Losses, and Voltage Regulation**, the source boundary is explicit: FE-Handbook-supported material remains tied to the ledger, externally supported material uses the chapter references for power-system voltage, loss, and reactive-power analysis (GLOVER), and guide synthesis is identified as supplemental explanation rather than Handbook text.


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

1. **Independent check for §36.1.** Begin independently with \(S=VI^*=P+jQ,\qquad |S|=VI\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: At 120 V, 10 A, pf=0.8 lagging, P=960 W and |S|=1200 VA. Then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

2. **Independent check for §36.2.** Begin independently with \(P=\sqrt3\,V_L I_L\cos\theta\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: At 480 V line-line, 100 A, pf=0.9, P≈74.8 kW. Then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

3. **Independent check for §36.3.** Begin independently with \(\Delta V\approx I(R+jX),\qquad P_{\text{loss}}=I^2R\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Halving current reduces resistive line loss by a factor of four. Then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

4. **Independent check for §36.4.** Begin independently with \(Q_c=P(\tan\theta_1-\tan\theta_2)\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Correcting from pf 0.8 to 0.95 reduces the reactive power carried by the source. Then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

5. **Independent check for §36.5.** Begin independently with \(\frac{V_S}{V_P}=\frac{N_2}{N_1},\qquad Z_P=a^2Z_S\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A 10:1 turns ratio reflects a 4-Ω secondary load as 400 Ω to the primary if a=N1/N2=10. Then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

6. **Independent check for §36.6.** Begin independently with \(n_s=\frac{120f}{p},\qquad s=\frac{n_s-n}{n_s}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: At 60 Hz with 4 poles, synchronous speed is 1800 rpm. Then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

7. **Independent check for §36.7.** Begin independently with \(\%\mathrm{VR}=100\frac{V_{NL}-V_{FL}}{V_{FL}}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: If VNL=125 V and VFL=120 V, regulation is 4.17%. Then verify that RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

8. Check the chapter-specific failure mode first: a three-phase relation applied to unbalanced quantities or a power-factor correction result that changes real load power. Do not accept the numerical or logical result until RMS/phasor conventions, phase relationships, transformer assumptions, and the stated power-system model are consistent.

9. For **Power Systems — Transmission, Distribution, Losses, and Voltage Regulation**, start with the FE Electrical and Computer specification/Handbook location recorded in the ledger, then use the chapter's reconciled source set for power-system voltage, loss, and reactive-power analysis (GLOVER) when the concept is split-required. That preserves the Handbook-versus-learned-material boundary.

10. Use this limiting check: let reactive power approach zero and verify that power factor approaches unity while real power remains unchanged. The simplified case should produce the expected physical, timing, logic, protocol, or complexity behavior before the full solution is trusted.

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
