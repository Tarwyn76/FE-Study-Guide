---
chapter: "03-31"
title: "Semiconductor Materials, Energy Bands, Doping, and p-n Junctions"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-031-01, ECE-3-031-02, ECE-3-031-03, ECE-3-031-04, ECE-3-031-05, ECE-3-031-06, ECE-3-031-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-31: Semiconductor Materials, Energy Bands, Doping, and p-n Junctions

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** MAT-2B-017-04 · MAT-2B-018-01

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Semiconductor Materials, Energy Bands, Doping, and p-n Junctions**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **31.1** Explain and apply **Conductivity, resistivity, carriers, and mobility**.
* **31.2** Explain and apply **Energy bands, intrinsic material, and the Fermi-level concept**.
* **31.3** Explain and apply **Doping, donors, acceptors, and majority carriers**.
* **31.4** Explain and apply **Mass-action relation and minority carriers**.
* **31.5** Explain and apply **Drift, diffusion, and junction formation**.
* **31.6** Explain and apply **Built-in potential and depletion-region behavior**.
* **31.7** Explain and apply **Junction capacitance, thermal voltage, and temperature effects**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 31.1 Conductivity, resistivity, carriers, and mobility

Semiconductor conductivity depends on mobile electron and hole concentrations and their mobilities. Doping changes carrier concentration by many orders of magnitude, which is why semiconductor conductivity is controllable.

\[\sigma=q(n\mu_n+p\mu_p),\qquad \rho=\frac{1}{\sigma}\]

![FIG-03-31-001: Semiconductor bar showing electron and hole drift directions under an electric field, with n, p, mobility, conductivity, and resistivity labels.](../figures/FIG-03-31-001-conductivity-resistivity-carriers-and-mobility.png)

### Worked Example 1

**Problem.** For n=1.0×10^16 cm^-3, μn=1350 cm²/(V·s), and negligible holes, σ≈2.16 (Ω·cm)^-1.

**Solution.** Use the relation and model in §31.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 31.2 Energy bands, intrinsic material, and the Fermi-level concept

The valence band, conduction band, and band gap organize semiconductor behavior. Intrinsic material has equal equilibrium electron and hole concentrations; the Fermi-level concept indicates carrier occupancy tendency.

\[E_g=E_C-E_V\]

![FIG-03-31-002: Energy-band diagrams for conductor, semiconductor, and insulator, plus intrinsic semiconductor EC, EV, Eg, and Fermi-level placement.](../figures/FIG-03-31-002-energy-bands-intrinsic-material-and-the-fermi-level-concept.png)

### Worked Example 2

**Problem.** A material with a wider band gap generally requires more energy to create mobile carriers.

**Solution.** Use the relation and model in §31.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 31.3 Doping, donors, acceptors, and majority carriers

Donor doping creates n-type material with electrons as majority carriers; acceptor doping creates p-type material with holes as majority carriers. Charge neutrality still applies.

\[n_n\approx N_D,\qquad p_p\approx N_A\]

![FIG-03-31-003: Crystal-lattice concept with donor and acceptor dopants and corresponding n-type and p-type energy-band sketches.](../figures/FIG-03-31-003-doping-donors-acceptors-and-majority-carriers.png)

### Worked Example 3

**Problem.** If a silicon region is doped with 10^16 donors/cm³ and is fully ionized, the majority electron concentration is approximately 10^16 cm^-3.

**Solution.** Use the relation and model in §31.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 31.4 Mass-action relation and minority carriers

At thermal equilibrium, electron and hole concentrations satisfy the mass-action relation. Once the majority carrier concentration is known, the minority concentration follows directly.

\[np=n_i^2\]

![FIG-03-31-004: Log-scale carrier concentration chart showing intrinsic, n-type, and p-type cases linked by np=ni².](../figures/FIG-03-31-004-mass-action-relation-and-minority-carriers.png)

### Worked Example 4

**Problem.** If ni=10^10 cm^-3 and n=10^16 cm^-3, then p=10^4 cm^-3.

**Solution.** Use the relation and model in §31.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 31.5 Drift, diffusion, and junction formation

Carrier transport combines electric-field-driven drift and concentration-gradient-driven diffusion. A p-n junction forms when diffusion initially moves majority carriers across the metallurgical junction, leaving a depletion region and built-in electric field.

\[J_n=q n\mu_n E+qD_n\frac{dn}{dx}\]

![FIG-03-31-005: Step-by-step p-n junction formation showing diffusion, ionized donors/acceptors, depletion region, and built-in electric field.](../figures/FIG-03-31-005-drift-diffusion-and-junction-formation.png)

### Worked Example 5

**Problem.** A strong carrier concentration gradient can create diffusion current even when the external electric field is zero.

**Solution.** Use the relation and model in §31.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 31.6 Built-in potential and depletion-region behavior

The built-in potential depends logarithmically on doping concentrations and temperature. Forward bias reduces the junction barrier; reverse bias increases it and widens the depletion region.

\[V_0=\frac{kT}{q}\ln\!\left(\frac{N_A N_D}{n_i^2}\right)\]

![FIG-03-31-006: Equilibrium, forward-bias, and reverse-bias p-n junction energy-band/depletion sketches with barrier changes.](../figures/FIG-03-31-006-built-in-potential-and-depletion-region-behavior.png)

### Worked Example 6

**Problem.** Increasing either NA or ND increases built-in potential, all else equal.

**Solution.** Use the relation and model in §31.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 31.7 Junction capacitance, thermal voltage, and temperature effects

Thermal voltage sets the exponential scale for junction current. Depletion capacitance varies with junction bias because the depletion width changes.

\[V_T=\frac{kT}{q}\approx 0.026\text{ V at 300 K}\]

![FIG-03-31-007: Reverse-bias depletion width and junction capacitance plotted qualitatively versus applied junction voltage.](../figures/FIG-03-31-007-junction-capacitance-thermal-voltage-and-temperature-effects.png)

### Worked Example 7

**Problem.** At room temperature, use VT≈26 mV unless the problem specifies another temperature.

**Solution.** Use the relation and model in §31.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

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

Primary source basis: **FE Electrical and Computer specification Area 5; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using semiconductor conductivity outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using semiconductor energy bands outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using semiconductor doping outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using carrier mass action outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using drift-diffusion transport outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using p-n junction built-in potential outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using junction capacitance outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| semiconductor conductivity | Concept developed in §31.1; apply with that section's stated model and conventions. |
| semiconductor energy bands | Concept developed in §31.2; apply with that section's stated model and conventions. |
| semiconductor doping | Concept developed in §31.3; apply with that section's stated model and conventions. |
| carrier mass action | Concept developed in §31.4; apply with that section's stated model and conventions. |
| drift-diffusion transport | Concept developed in §31.5; apply with that section's stated model and conventions. |
| p-n junction built-in potential | Concept developed in §31.6; apply with that section's stated model and conventions. |
| junction capacitance | Concept developed in §31.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **semiconductor conductivity** and identify the governing relation, state variable, or decision it organizes.

2. Define **semiconductor energy bands** and identify the governing relation, state variable, or decision it organizes.

3. Define **semiconductor doping** and identify the governing relation, state variable, or decision it organizes.

4. Define **carrier mass action** and identify the governing relation, state variable, or decision it organizes.

5. Define **drift-diffusion transport** and identify the governing relation, state variable, or decision it organizes.

6. Define **p-n junction built-in potential** and identify the governing relation, state variable, or decision it organizes.

7. Define **junction capacitance** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **semiconductor conductivity**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **semiconductor energy bands**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **semiconductor doping**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **carrier mass action**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **drift-diffusion transport**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **p-n junction built-in potential**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **junction capacitance**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **semiconductor conductivity**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **semiconductor energy bands**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **semiconductor doping**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **carrier mass action**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **drift-diffusion transport**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **p-n junction built-in potential**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **junction capacitance**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **semiconductor conductivity**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **semiconductor energy bands**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **semiconductor conductivity** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **semiconductor energy bands** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **semiconductor doping** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **carrier mass action** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **drift-diffusion transport** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **p-n junction built-in potential** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **junction capacitance** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **semiconductor conductivity**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **semiconductor energy bands**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **semiconductor doping**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **carrier mass action**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **drift-diffusion transport**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **p-n junction built-in potential**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **junction capacitance**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

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

1. For n=1.0×10^16 cm^-3, μn=1350 cm²/(V·s), and negligible holes, σ≈2.16 (Ω·cm)^-1.

2. A material with a wider band gap generally requires more energy to create mobile carriers.

3. If a silicon region is doped with 10^16 donors/cm³ and is fully ionized, the majority electron concentration is approximately 10^16 cm^-3.

4. If ni=10^10 cm^-3 and n=10^16 cm^-3, then p=10^4 cm^-3.

5. A strong carrier concentration gradient can create diffusion current even when the external electric field is zero.

6. Increasing either NA or ND increases built-in potential, all else equal.

7. At room temperature, use VT≈26 mV unless the problem specifies another temperature.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §31.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §31.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §31.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §31.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §31.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §31.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §31.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 5, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 5.

- **semiconductor conductivity:** Conductivity, resistivity, carriers, and mobility
- **semiconductor energy bands:** Energy bands, intrinsic material, and the Fermi-level concept
- **semiconductor doping:** Doping, donors, acceptors, and majority carriers
- **carrier mass action:** Mass-action relation and minority carriers
- **drift-diffusion transport:** Drift, diffusion, and junction formation
- **p-n junction built-in potential:** Built-in potential and depletion-region behavior
- **junction capacitance:** Junction capacitance, thermal voltage, and temperature effects

---

## What's Next

**Chapter 03-32: Diodes, Rectifiers, Thyristors, and Device Models**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
