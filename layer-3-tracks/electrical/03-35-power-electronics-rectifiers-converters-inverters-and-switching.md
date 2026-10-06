---
chapter: "03-35"
title: "Power Electronics — Rectifiers, Converters, Inverters, and Switching"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-035-01, ECE-3-035-02, ECE-3-035-03, ECE-3-035-04, ECE-3-035-05, ECE-3-035-06, ECE-3-035-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-35: Power Electronics — Rectifiers, Converters, Inverters, and Switching

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-032-07 · ELEC-2E-061-03

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Power Electronics — Rectifiers, Converters, Inverters, and Switching**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **35.1** Explain and apply **Power-switching devices and idealized switching states**.
* **35.2** Explain and apply **Single-phase and multipulse rectifier concepts**.
* **35.3** Explain and apply **Buck converter steady-state gain**.
* **35.4** Explain and apply **Boost and buck-boost converter gains**.
* **35.5** Explain and apply **Inductor current ripple and capacitor voltage ripple**.
* **35.6** Explain and apply **Voltage-source inverters and PWM**.
* **35.7** Explain and apply **Efficiency, thermal stress, and switching tradeoffs**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 35.1 Power-switching devices and idealized switching states

Power electronics uses semiconductor devices as switches rather than linear dissipative elements whenever possible. Conduction and switching losses determine efficiency.

\[P_{\text{switch,cond}}\approx V_{\text{on}}I\]

![FIG-03-35-001: Diode, SCR, MOSFET, and IGBT switching roles with current/voltage direction and control terminal concept.](../figures/FIG-03-35-001-power-switching-devices-and-idealized-switching-states.png)

### Worked Example 1

**Problem.** A switch with 1.5-V on-state drop at 20 A dissipates 30 W while on.

**Solution.** Use the relation and model in §35.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 35.2 Single-phase and multipulse rectifier concepts

Power rectifiers convert AC to DC. The Handbook provides a general n-pulse rectifier average-output relation; topology and filtering determine ripple and device stresses.

\[\overline V_o=\text{rectifier average determined by pulse number and input RMS}\]

![FIG-03-35-002: Single-phase bridge and three-phase six-pulse rectifier with source, switching sequence, and DC output waveform.](../figures/FIG-03-35-002-single-phase-and-multipulse-rectifier-concepts.png)

### Worked Example 2

**Problem.** Increasing pulse number generally raises ripple frequency and can reduce filtering burden.

**Solution.** Use the relation and model in §35.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 35.3 Buck converter steady-state gain

For an ideal buck converter in continuous steady operation, duty ratio controls the step-down voltage gain. Inductor and capacitor ripple sit on top of the average values.

\[\frac{V_o}{V_{in}}=D\]

![FIG-03-35-003: Buck converter schematic with switch, diode, inductor, capacitor, and switch/inductor/output waveforms.](../figures/FIG-03-35-003-buck-converter-steady-state-gain.png)

### Worked Example 3

**Problem.** Vin=24 V and D=0.25 gives Vo=6 V ideally.

**Solution.** Use the relation and model in §35.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 35.4 Boost and buck-boost converter gains

Ideal boost and inverting buck-boost gains follow from inductor volt-second balance. Duty ratio must remain within physical operating limits.

\[\frac{V_o}{V_{in}}=\frac{1}{1-D},\qquad \frac{V_o}{V_{in}}=-\frac{D}{1-D}\]

![FIG-03-35-004: Buck, boost, and inverting buck-boost topologies with ideal gain equations and energy-transfer intervals.](../figures/FIG-03-35-004-boost-and-buck-boost-converter-gains.png)

### Worked Example 4

**Problem.** For a boost converter at D=0.5, ideal voltage gain is 2.

**Solution.** Use the relation and model in §35.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 35.5 Inductor current ripple and capacitor voltage ripple

Switching ripple follows directly from inductor and capacitor constitutive relations over each switching interval. Higher switching frequency typically reduces passive-component ripple for fixed L and C.

\[\Delta i_L\approx \frac{V_L\Delta t}{L},\qquad \Delta v_C\approx \frac{I_C\Delta t}{C}\]

![FIG-03-35-005: Inductor current and capacitor/output voltage ripple over one PWM switching period.](../figures/FIG-03-35-005-inductor-current-ripple-and-capacitor-voltage-ripple.png)

### Worked Example 5

**Problem.** Doubling switching frequency approximately halves a triangular ripple increment under otherwise identical conditions.

**Solution.** Use the relation and model in §35.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 35.6 Voltage-source inverters and PWM

A voltage-source inverter synthesizes AC from DC by controlled switching. In sine-triangle PWM, fundamental output magnitude scales with modulation index in the linear modulation range.

\[V_{LL,1,\mathrm{rms}}\propto mV_{dc}\]

![FIG-03-35-006: Three-phase bridge inverter with DC link, PWM gate pattern, phase voltage, and fundamental line-voltage component.](../figures/FIG-03-35-006-voltage-source-inverters-and-pwm.png)

### Worked Example 6

**Problem.** Increasing m within the linear range increases the fundamental AC output voltage.

**Solution.** Use the relation and model in §35.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 35.7 Efficiency, thermal stress, and switching tradeoffs

Higher switching frequency can reduce passive size and ripple but increase switching loss. Device voltage/current ratings and thermal design must include transient and steady stresses.

\[\eta=\frac{P_o}{P_{in}}=\frac{P_o}{P_o+P_{\text{loss}}}\]

![FIG-03-35-007: Power-converter loss breakdown into conduction, switching, magnetic, capacitor, and control losses with thermal path.](../figures/FIG-03-35-007-efficiency-thermal-stress-and-switching-tradeoffs.png)

### Worked Example 7

**Problem.** A 1-kW converter with 50 W total loss has efficiency about 95.2%.

**Solution.** Use the relation and model in §35.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

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

Primary source basis: **FE Electrical and Computer specification Area 9; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using power semiconductor switch outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using power rectifier outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using buck converter outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using boost and buck-boost converter outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using converter ripple outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using voltage-source inverter outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using power-converter efficiency outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| power semiconductor switch | Concept developed in §35.1; apply with that section's stated model and conventions. |
| power rectifier | Concept developed in §35.2; apply with that section's stated model and conventions. |
| buck converter | Concept developed in §35.3; apply with that section's stated model and conventions. |
| boost and buck-boost converter | Concept developed in §35.4; apply with that section's stated model and conventions. |
| converter ripple | Concept developed in §35.5; apply with that section's stated model and conventions. |
| voltage-source inverter | Concept developed in §35.6; apply with that section's stated model and conventions. |
| power-converter efficiency | Concept developed in §35.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **power semiconductor switch** and identify the governing relation, state variable, or decision it organizes.

2. Define **power rectifier** and identify the governing relation, state variable, or decision it organizes.

3. Define **buck converter** and identify the governing relation, state variable, or decision it organizes.

4. Define **boost and buck-boost converter** and identify the governing relation, state variable, or decision it organizes.

5. Define **converter ripple** and identify the governing relation, state variable, or decision it organizes.

6. Define **voltage-source inverter** and identify the governing relation, state variable, or decision it organizes.

7. Define **power-converter efficiency** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **power semiconductor switch**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **power rectifier**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **buck converter**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **boost and buck-boost converter**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **converter ripple**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **voltage-source inverter**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **power-converter efficiency**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **power semiconductor switch**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **power rectifier**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **buck converter**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **boost and buck-boost converter**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **converter ripple**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **voltage-source inverter**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **power-converter efficiency**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **power semiconductor switch**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **power rectifier**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **power semiconductor switch** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **power rectifier** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **buck converter** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **boost and buck-boost converter** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **converter ripple** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **voltage-source inverter** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **power-converter efficiency** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **power semiconductor switch**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **power rectifier**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **buck converter**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **boost and buck-boost converter**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **converter ripple**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **voltage-source inverter**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **power-converter efficiency**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

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

1. A switch with 1.5-V on-state drop at 20 A dissipates 30 W while on.

2. Increasing pulse number generally raises ripple frequency and can reduce filtering burden.

3. Vin=24 V and D=0.25 gives Vo=6 V ideally.

4. For a boost converter at D=0.5, ideal voltage gain is 2.

5. Doubling switching frequency approximately halves a triangular ripple increment under otherwise identical conditions.

6. Increasing m within the linear range increases the fundamental AC output voltage.

7. A 1-kW converter with 50 W total loss has efficiency about 95.2%.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §35.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §35.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §35.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §35.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §35.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §35.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §35.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 9, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 9.

- **power semiconductor switch:** Power-switching devices and idealized switching states
- **power rectifier:** Single-phase and multipulse rectifier concepts
- **buck converter:** Buck converter steady-state gain
- **boost and buck-boost converter:** Boost and buck-boost converter gains
- **converter ripple:** Inductor current ripple and capacitor voltage ripple
- **voltage-source inverter:** Voltage-source inverters and PWM
- **power-converter efficiency:** Efficiency, thermal stress, and switching tradeoffs

---

## What's Next

**Chapter 03-36: Power Systems — Transmission, Distribution, Losses, and Voltage Regulation**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
