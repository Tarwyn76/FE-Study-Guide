---
chapter: "03-33"
title: "BJT and MOSFET Biasing and Small-Signal Models"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-033-01, ECE-3-033-02, ECE-3-033-03, ECE-3-033-04, ECE-3-033-05, ECE-3-033-06, ECE-3-033-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-33: BJT and MOSFET Biasing and Small-Signal Models

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-032-07 · ELEC-2E-060-05

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **BJT and MOSFET Biasing and Small-Signal Models**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **33.1** Explain and apply **BJT regions, current relations, and DC bias**.
* **33.2** Explain and apply **BJT load line and Q-point selection**.
* **33.3** Explain and apply **BJT transconductance and hybrid-pi small-signal model**.
* **33.4** Explain and apply **JFET and depletion-MOSFET biasing**.
* **33.5** Explain and apply **Enhancement MOSFET regions and DC bias**.
* **33.6** Explain and apply **MOSFET transconductance and small-signal model**.
* **33.7** Explain and apply **Bias stability, headroom, and device-model verification**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 33.1 BJT regions, current relations, and DC bias

A BJT bias calculation must first identify cutoff, active, or saturation operation. The active-region current-gain relation is not valid in saturation.

\[I_C\approx \beta I_B,\qquad I_E=I_B+I_C\]

![FIG-03-33-001: NPN transistor circuit with cutoff, active, and saturation regions mapped onto an IC-VCE characteristic family.](../figures/FIG-03-33-001-bjt-regions-current-relations-and-dc-bias.png)

### Worked Example 1

**Problem.** If β=100 and IB=20 μA in active operation, IC≈2.0 mA.

**Solution.** Use the relation and model in §33.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 33.2 BJT load line and Q-point selection

The DC load line constrains transistor collector current and collector-emitter voltage. The Q point should support the intended signal swing without clipping.

\[V_{CE}=V_{CC}-I_C R_C\]

![FIG-03-33-002: BJT output curves with DC load line and Q point centered for signal swing.](../figures/FIG-03-33-002-bjt-load-line-and-q-point-selection.png)

### Worked Example 2

**Problem.** For VCC=10 V and RC=2 kΩ, the load-line intercept current is 5 mA.

**Solution.** Use the relation and model in §33.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 33.3 BJT transconductance and hybrid-pi small-signal model

Small-signal analysis linearizes the transistor about its Q point. Device parameters therefore depend on the DC bias current.

\[g_m\approx \frac{I_{CQ}}{V_T},\qquad r_\pi\approx \frac{\beta}{g_m}\]

![FIG-03-33-003: BJT hybrid-pi model with rπ, gm vπ source, ro, and terminal labels.](../figures/FIG-03-33-003-bjt-transconductance-and-hybrid-pi-small-signal-model.png)

### Worked Example 3

**Problem.** At ICQ=1 mA and VT=25 mV, gm≈40 mS.

**Solution.** Use the relation and model in §33.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 33.4 JFET and depletion-MOSFET biasing

JFET and depletion-MOSFET devices can conduct at zero gate-source voltage. Check the valid operating region before using the square-law saturation relation.

\[I_D=I_{DSS}\left(1-\frac{V_{GS}}{V_P}\right)^2\]

![FIG-03-33-004: JFET transfer curve and output characteristics with cutoff, triode, and saturation regions.](../figures/FIG-03-33-004-jfet-and-depletion-mosfet-biasing.png)

### Worked Example 4

**Problem.** At VGS=0, the saturation drain current is IDSS.

**Solution.** Use the relation and model in §33.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 33.5 Enhancement MOSFET regions and DC bias

An enhancement MOSFET requires gate overdrive above threshold before it conducts significantly in the idealized model. Saturation and triode regions use different current relations.

\[I_D=K(V_{GS}-V_t)^2\quad\text{in saturation under the Handbook model}\]

![FIG-03-33-005: NMOS output characteristics and transfer curve with cutoff, triode, and saturation regions.](../figures/FIG-03-33-005-enhancement-mosfet-regions-and-dc-bias.png)

### Worked Example 5

**Problem.** If VGS≤Vt in the ideal model, ID=0.

**Solution.** Use the relation and model in §33.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 33.6 MOSFET transconductance and small-signal model

The MOSFET small-signal model converts small gate-voltage changes into drain-current changes through transconductance. Output resistance may be included when channel-length modulation is modeled.

\[g_m=2K(V_{GS}-V_t)\]

![FIG-03-33-006: Low-frequency MOSFET small-signal model with gm vgs controlled source and output resistance.](../figures/FIG-03-33-006-mosfet-transconductance-and-small-signal-model.png)

### Worked Example 6

**Problem.** For K=1 mA/V² and overdrive 2 V, gm=4 mS in the Handbook model.

**Solution.** Use the relation and model in §33.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 33.7 Bias stability, headroom, and device-model verification

A useful bias design provides headroom for the signal and reasonable tolerance to β, threshold, temperature, and component variation. Always re-check the operating region after solving.

\[\text{Q-point must remain in intended region over expected variation}\]

![FIG-03-33-007: Bias point with allowable signal swing and variation envelope inside a transistor operating region.](../figures/FIG-03-33-007-bias-stability-headroom-and-device-model-verification.png)

### Worked Example 7

**Problem.** A calculated VCE below the assumed saturation threshold invalidates an active-region BJT solution.

**Solution.** Use the relation and model in §33.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

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

**Using BJT bias point outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using BJT load line outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using BJT small-signal model outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using depletion FET bias outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using enhancement MOSFET bias outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using MOSFET small-signal model outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using transistor bias stability outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| BJT bias point | Concept developed in §33.1; apply with that section's stated model and conventions. |
| BJT load line | Concept developed in §33.2; apply with that section's stated model and conventions. |
| BJT small-signal model | Concept developed in §33.3; apply with that section's stated model and conventions. |
| depletion FET bias | Concept developed in §33.4; apply with that section's stated model and conventions. |
| enhancement MOSFET bias | Concept developed in §33.5; apply with that section's stated model and conventions. |
| MOSFET small-signal model | Concept developed in §33.6; apply with that section's stated model and conventions. |
| transistor bias stability | Concept developed in §33.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **BJT bias point** and identify the governing relation, state variable, or decision it organizes.

2. Define **BJT load line** and identify the governing relation, state variable, or decision it organizes.

3. Define **BJT small-signal model** and identify the governing relation, state variable, or decision it organizes.

4. Define **depletion FET bias** and identify the governing relation, state variable, or decision it organizes.

5. Define **enhancement MOSFET bias** and identify the governing relation, state variable, or decision it organizes.

6. Define **MOSFET small-signal model** and identify the governing relation, state variable, or decision it organizes.

7. Define **transistor bias stability** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **BJT bias point**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **BJT load line**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **BJT small-signal model**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **depletion FET bias**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **enhancement MOSFET bias**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **MOSFET small-signal model**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **transistor bias stability**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **BJT bias point**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **BJT load line**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **BJT small-signal model**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **depletion FET bias**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **enhancement MOSFET bias**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **MOSFET small-signal model**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **transistor bias stability**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **BJT bias point**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **BJT load line**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **BJT bias point** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **BJT load line** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **BJT small-signal model** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **depletion FET bias** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **enhancement MOSFET bias** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **MOSFET small-signal model** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **transistor bias stability** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **BJT bias point**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **BJT load line**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **BJT small-signal model**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **depletion FET bias**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **enhancement MOSFET bias**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **MOSFET small-signal model**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **transistor bias stability**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

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

1. If β=100 and IB=20 μA in active operation, IC≈2.0 mA.

2. For VCC=10 V and RC=2 kΩ, the load-line intercept current is 5 mA.

3. At ICQ=1 mA and VT=25 mV, gm≈40 mS.

4. At VGS=0, the saturation drain current is IDSS.

5. If VGS≤Vt in the ideal model, ID=0.

6. For K=1 mA/V² and overdrive 2 V, gm=4 mS in the Handbook model.

7. A calculated VCE below the assumed saturation threshold invalidates an active-region BJT solution.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §33.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §33.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §33.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §33.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §33.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §33.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §33.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 9, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 9.

- **BJT bias point:** BJT regions, current relations, and DC bias
- **BJT load line:** BJT load line and Q-point selection
- **BJT small-signal model:** BJT transconductance and hybrid-pi small-signal model
- **depletion FET bias:** JFET and depletion-MOSFET biasing
- **enhancement MOSFET bias:** Enhancement MOSFET regions and DC bias
- **MOSFET small-signal model:** MOSFET transconductance and small-signal model
- **transistor bias stability:** Bias stability, headroom, and device-model verification

---

## What's Next

**Chapter 03-34: Single-Stage, Differential, and Operational Amplifiers**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
