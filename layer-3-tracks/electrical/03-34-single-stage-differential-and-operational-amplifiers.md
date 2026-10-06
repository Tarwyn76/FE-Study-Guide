---
chapter: "03-34"
title: "Single-Stage, Differential, and Operational Amplifiers"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-034-01, ECE-3-034-02, ECE-3-034-03, ECE-3-034-04, ECE-3-034-05, ECE-3-034-06, ECE-3-034-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-34: Single-Stage, Differential, and Operational Amplifiers

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-033-07 · INST-2F-067-07

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Single-Stage, Differential, and Operational Amplifiers**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **34.1** Explain and apply **Common-emitter gain, inversion, and small-signal loading**.
* **34.2** Explain and apply **Source/emitter followers and buffering**.
* **34.3** Explain and apply **Differential-pair operation and common-mode rejection**.
* **34.4** Explain and apply **Ideal op-amp rules and negative feedback**.
* **34.5** Explain and apply **Inverting, noninverting, summing, and difference amplifiers**.
* **34.6** Explain and apply **Nonideal op amps, saturation, bandwidth, and CMRR**.
* **34.7** Explain and apply **Instrumentation chain, sensors, and data-acquisition interfaces**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 34.1 Common-emitter gain, inversion, and small-signal loading

A common-emitter stage provides voltage gain and phase inversion. The effective collector load includes external loading as well as the collector resistance.

\[A_v\approx -g_m R_{\text{effective}}\]

![FIG-03-34-001: Biased common-emitter amplifier with small-signal equivalent and inverted input/output waveforms.](../figures/FIG-03-34-001-common-emitter-gain-inversion-and-small-signal-loading.png)

### Worked Example 1

**Problem.** If gm=20 mS and effective collector load is 2 kΩ, the unloaded model gives Av≈-40.

**Solution.** Use the relation and model in §34.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 34.2 Source/emitter followers and buffering

Emitter and source followers trade voltage gain for buffering, typically providing high input resistance and lower output resistance.

\[A_v\lesssim 1\]

![FIG-03-34-002: Emitter/source follower concept showing high input impedance, near-unity voltage gain, and lower output impedance.](../figures/FIG-03-34-002-source-emitter-followers-and-buffering.png)

### Worked Example 2

**Problem.** A follower is useful between a high-impedance signal source and a lower-impedance load.

**Solution.** Use the relation and model in §34.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 34.3 Differential-pair operation and common-mode rejection

A differential amplifier responds primarily to input difference while rejecting common-mode signals. Matched devices and a stable tail current improve symmetry.

\[v_{id}=v_1-v_2,\qquad v_{icm}=\frac{v_1+v_2}{2}\]

![FIG-03-34-003: BJT differential pair with tail current, differential input, common-mode input, and collector outputs.](../figures/FIG-03-34-003-differential-pair-operation-and-common-mode-rejection.png)

### Worked Example 3

**Problem.** If v1=1.01 V and v2=0.99 V, vid=20 mV and vicm=1.00 V.

**Solution.** Use the relation and model in §34.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 34.4 Ideal op-amp rules and negative feedback

Ideal op-amp analysis uses zero input current and equal input-node voltage only when the amplifier is operating linearly with negative feedback.

\[i_+=i_-=0,\qquad v_+\approx v_-\text{ in linear negative feedback}\]

![FIG-03-34-004: Ideal op-amp equivalent showing infinite open-loop gain, zero input currents, and negative-feedback virtual short.](../figures/FIG-03-34-004-ideal-op-amp-rules-and-negative-feedback.png)

### Worked Example 4

**Problem.** An op amp driven into saturation does not satisfy the virtual-short assumption.

**Solution.** Use the relation and model in §34.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 34.5 Inverting, noninverting, summing, and difference amplifiers

Closed-loop op-amp gains are set primarily by feedback networks when the ideal assumptions are valid. Keep track of input polarity and reference node.

\[A_{v,\text{inv}}=-\frac{R_f}{R_{in}},\qquad A_{v,\text{noninv}}=1+\frac{R_f}{R_g}\]

![FIG-03-34-005: Inverting, noninverting, summing, and difference op-amp circuits with their principal gain relationships.](../figures/FIG-03-34-005-inverting-noninverting-summing-and-difference-amplifiers.png)

### Worked Example 5

**Problem.** Rf=20 kΩ and Rin=5 kΩ gives inverting gain -4.

**Solution.** Use the relation and model in §34.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 34.6 Nonideal op amps, saturation, bandwidth, and CMRR

Finite open-loop gain, bandwidth, slew rate, input/output limits, offsets, and common-mode gain can matter when ideal assumptions predict unrealistic behavior.

\[\mathrm{CMRR}=\frac{A_d}{A_{cm}},\qquad \mathrm{CMRR}_{dB}=20\log_{10}\!\frac{A_d}{A_{cm}}\]

![FIG-03-34-006: Op-amp output transfer with saturation rails plus gain-bandwidth and common-mode rejection callouts.](../figures/FIG-03-34-006-nonideal-op-amps-saturation-bandwidth-and-cmrr.png)

### Worked Example 6

**Problem.** A 10-V predicted output is impossible if the amplifier output saturates at ±5 V.

**Solution.** Use the relation and model in §34.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 34.7 Instrumentation chain, sensors, and data-acquisition interfaces

Instrumentation problems combine sensors, conditioning, conversion, and loading. The ECE specification explicitly includes measurements, DAQ, and transducers; Layer 2F supplies the shared instrumentation foundation.

\[\text{measurand}\rightarrow\text{transducer}\rightarrow\text{conditioning}\rightarrow\text{ADC}\rightarrow\text{processing}\]

![FIG-03-34-007: Sensor-to-ADC measurement chain with bridge/sensor, amplifier, filter, ADC, and digital processor.](../figures/FIG-03-34-007-instrumentation-chain-sensors-and-data-acquisition-interfaces.png)

### Worked Example 7

**Problem.** Choose conditioning gain so the sensor's expected range fits the ADC input range without clipping.

**Solution.** Use the relation and model in §34.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

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

**Using common-emitter amplifier outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using voltage follower transistor stage outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using differential amplifier outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using ideal operational amplifier outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using op-amp closed-loop gain outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using op-amp nonideality outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using instrumentation amplifier chain outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| common-emitter amplifier | Concept developed in §34.1; apply with that section's stated model and conventions. |
| voltage follower transistor stage | Concept developed in §34.2; apply with that section's stated model and conventions. |
| differential amplifier | Concept developed in §34.3; apply with that section's stated model and conventions. |
| ideal operational amplifier | Concept developed in §34.4; apply with that section's stated model and conventions. |
| op-amp closed-loop gain | Concept developed in §34.5; apply with that section's stated model and conventions. |
| op-amp nonideality | Concept developed in §34.6; apply with that section's stated model and conventions. |
| instrumentation amplifier chain | Concept developed in §34.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **common-emitter amplifier** and identify the governing relation, state variable, or decision it organizes.

2. Define **voltage follower transistor stage** and identify the governing relation, state variable, or decision it organizes.

3. Define **differential amplifier** and identify the governing relation, state variable, or decision it organizes.

4. Define **ideal operational amplifier** and identify the governing relation, state variable, or decision it organizes.

5. Define **op-amp closed-loop gain** and identify the governing relation, state variable, or decision it organizes.

6. Define **op-amp nonideality** and identify the governing relation, state variable, or decision it organizes.

7. Define **instrumentation amplifier chain** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **common-emitter amplifier**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **voltage follower transistor stage**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **differential amplifier**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **ideal operational amplifier**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **op-amp closed-loop gain**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **op-amp nonideality**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **instrumentation amplifier chain**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **common-emitter amplifier**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **voltage follower transistor stage**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **differential amplifier**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **ideal operational amplifier**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **op-amp closed-loop gain**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **op-amp nonideality**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **instrumentation amplifier chain**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **common-emitter amplifier**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **voltage follower transistor stage**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **common-emitter amplifier** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **voltage follower transistor stage** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **differential amplifier** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **ideal operational amplifier** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **op-amp closed-loop gain** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **op-amp nonideality** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **instrumentation amplifier chain** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **common-emitter amplifier**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **voltage follower transistor stage**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **differential amplifier**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **ideal operational amplifier**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **op-amp closed-loop gain**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **op-amp nonideality**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **instrumentation amplifier chain**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

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

1. If gm=20 mS and effective collector load is 2 kΩ, the unloaded model gives Av≈-40.

2. A follower is useful between a high-impedance signal source and a lower-impedance load.

3. If v1=1.01 V and v2=0.99 V, vid=20 mV and vicm=1.00 V.

4. An op amp driven into saturation does not satisfy the virtual-short assumption.

5. Rf=20 kΩ and Rin=5 kΩ gives inverting gain -4.

6. A 10-V predicted output is impossible if the amplifier output saturates at ±5 V.

7. Choose conditioning gain so the sensor's expected range fits the ADC input range without clipping.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §34.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §34.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §34.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §34.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §34.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §34.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §34.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 9, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 9.

- **common-emitter amplifier:** Common-emitter gain, inversion, and small-signal loading
- **voltage follower transistor stage:** Source/emitter followers and buffering
- **differential amplifier:** Differential-pair operation and common-mode rejection
- **ideal operational amplifier:** Ideal op-amp rules and negative feedback
- **op-amp closed-loop gain:** Inverting, noninverting, summing, and difference amplifiers
- **op-amp nonideality:** Nonideal op amps, saturation, bandwidth, and CMRR
- **instrumentation amplifier chain:** Instrumentation chain, sensors, and data-acquisition interfaces

---

## What's Next

**Chapter 03-35: Power Electronics — Rectifiers, Converters, Inverters, and Switching**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
