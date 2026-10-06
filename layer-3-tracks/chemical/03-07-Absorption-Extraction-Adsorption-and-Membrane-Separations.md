---
chapter: "03-07"
title: "Absorption, Extraction, Adsorption, and Membrane Separations"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-007-01, CHE-3-007-02, CHE-3-007-03, CHE-3-007-04, CHE-3-007-05, CHE-3-007-06, CHE-3-007-07]
routes: [chemical]
status: drafted
---

# Chapter 03-07: Absorption, Extraction, Adsorption, and Membrane Separations

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 03-05 Mass Transfer · 03-04 Phase Equilibrium · 03-01 Material Balances

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

Packed-column absorption is directly supported by Handbook p. 253. Extraction, adsorption, and membrane chapters are specification-required topics for which the Handbook provides limited or no dedicated formulas; those sections are guide-developed and explicitly marked as such.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **7.1** Explain and apply **Packed-Column Absorption — NTU and HTU**.
* **7.2** Explain and apply **Stripping as the Reverse Gas-Liquid Operation**.
* **7.3** Explain and apply **Liquid-Liquid Extraction**.
* **7.4** Explain and apply **Adsorption**.
* **7.5** Explain and apply **Membrane Separations**.
* **7.6** Explain and apply **Separation Selection by Equilibrium, Driving Force, and Phase**.
* **7.7** Explain and apply **Stagewise versus Continuous-Contact Separations**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 7.1 Packed-Column Absorption — NTU and HTU

The Handbook writes packed-column height as number of transfer units times height of a transfer unit, on either a gas or liquid basis.

For dilute systems with a known equilibrium line, the NTU integral measures how much mass-transfer driving force is available through the column.

\[Z=NTU_G\,HTU_G=NTU_L\,HTU_L=N_{EQ}HETP\]

![FIG-03-07-001: Countercurrent packed absorber with gas/liquid flows, rich/lean ends, HTU, NTU, and total packing height.](../figures/FIG-03-07-001-packed-column-absorption-ntu-and-htu.png)

### Worked Example 1

**Problem.** Packed absorber NTU=5 and HTU=0.8 m. Find packing height.

**Solution.** Z=4.0 m.

---

## 7.2 Stripping as the Reverse Gas-Liquid Operation

Stripping transfers a volatile solute from liquid to gas. The same two-film and operating/equilibrium-line ideas used for absorption apply, but the desired transfer direction is reversed.

This treatment is guide-developed from the same mass-transfer balances because the Handbook p. 253 presents the packed-column relation generically.

\[N_A=K_G'(p_A-p_A^*)=K_L'(C_A^*-C_A)\]

![FIG-03-07-002: Countercurrent stripper with solute leaving liquid and entering gas, showing equilibrium and operating lines.](../figures/FIG-03-07-002-stripping-as-the-reverse-gas-liquid-operation.png)

### Worked Example 2

**Problem.** What is the direction of solute transfer in stripping?

**Solution.** From liquid to gas.

---

## 7.3 Liquid-Liquid Extraction

**Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Liquid-liquid extraction transfers a solute between partially immiscible liquid phases.

At equilibrium, a distribution coefficient may be written \(K_D=y/x\) on a specified composition basis. Stagewise balances then combine feed, solvent, extract, and raffinate streams.

\[K_D=\frac{y_A}{x_A},\qquad Fz_A+Sx_{A,S}=R x_A+E y_A\]

![FIG-03-07-003: Mixer-settler stage showing feed, solvent, extract, raffinate, and an equilibrium distribution relation.](../figures/FIG-03-07-003-liquid-liquid-extraction.png)

### Worked Example 3

**Problem.** Extraction feed carries 10 mol solute; extract contains 7 mol. If no reaction/loss, how much solute remains in raffinate?

**Solution.** 3 mol.

---

## 7.4 Adsorption

**Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Adsorption transfers a species from a fluid to a solid surface.

For FE-level conceptual calculations, the problem may provide an isotherm such as a linear, Langmuir, or Freundlich relation. Treat that supplied relation as the equilibrium model and combine it with a solute balance.

\[q=q^*(C)\]

![FIG-03-07-004: Adsorbent particles and equilibrium isotherm q versus fluid concentration C, with a batch solute balance.](../figures/FIG-03-07-004-adsorption.png)

### Worked Example 4

**Problem.** Batch adsorption: 1 L solution drops from 100 to 20 mg/L using adsorbent. How much solute is adsorbed?

**Solution.** 80 mg.

---

## 7.5 Membrane Separations

**Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** A membrane separates species through selective transport driven by pressure, concentration, chemical potential, or electrical potential differences.

When a problem supplies permeability \(P_i\), a common simplified solution-diffusion form is flux proportional to driving-force difference divided by membrane thickness.

\[J_i=\frac{P_i}{\delta}\,\Delta(\text{driving force})\]

![FIG-03-07-005: Feed-retentate-permeate membrane module with species-selective fluxes and driving force across membrane thickness.](../figures/FIG-03-07-005-membrane-separations.png)

### Worked Example 5

**Problem.** Membrane permeability coefficient P/δ gives flux coefficient 2e-6 mol/(m²·s·kPa), Δp=50 kPa. Find flux.

**Solution.** 1.0e-4 mol/(m²·s).

---

## 7.6 Separation Selection by Equilibrium, Driving Force, and Phase

A separation method is chosen from the physical property that creates selectivity: volatility for distillation, solubility for absorption/extraction, surface affinity for adsorption, and permeability/selectivity for membranes.

The FE problem usually supplies enough equilibrium or performance information; the engineering task is recognizing which balance and driving force belong to the unit.

\[\text{separation}=\text{balance}+\text{equilibrium/selectivity}+\text{driving force}\]

![FIG-03-07-006: Matrix comparing distillation, absorption, extraction, adsorption, and membranes by phases, driving force, and key equilibrium quantity.](../figures/FIG-03-07-006-separation-selection-by-equilibrium-driving-force-and-phase.png)

### Worked Example 6

**Problem.** Which separation property most directly drives distillation?

**Solution.** Volatility/VLE difference.

---

## 7.7 Stagewise versus Continuous-Contact Separations

Stagewise devices idealize repeated equilibrium contacts; packed columns and many membrane modules behave as continuous-contact devices. The Handbook relates packed-column height to transfer units and also gives HETP as an equivalent stage measure.

Do not mix ideal-stage count directly with physical height without an efficiency, HETP, HTU, or other conversion relation.

\[Z=N_{EQ}HETP=NTU\cdot HTU\]

![FIG-03-07-007: Tray column and packed column side by side with stage count, HETP, HTU, and NTU relationships.](../figures/FIG-03-07-007-stagewise-versus-continuous-contact-separations.png)

### Worked Example 7

**Problem.** Why can ideal-stage count not be directly used as packed height?

**Solution.** A conversion such as HETP or HTU/NTU is required.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** If KG doubles at same driving force and area, what happens to transfer rate?

**Solution.** It doubles.

### Worked Example 9

**Problem.** Which process is typically chosen for a dilute gas solute with high liquid solubility?

**Solution.** Absorption.

---

## As the Handbook States It

Primary source basis: **Chemical Engineering absorption relations, printed p. 253; FE Chemical specification Area 10C–E. Extraction, adsorption, and membrane-process coverage is required by the specification but is not developed with dedicated formula sets in the Chemical Engineering Handbook pages.**.

**Source boundary:** Packed-column absorption is directly supported by Handbook p. 253. Extraction, adsorption, and membrane chapters are specification-required topics for which the Handbook provides limited or no dedicated formulas; those sections are guide-developed and explicitly marked as such.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using packed-column absorption without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using gas stripping without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using liquid-liquid extraction without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using adsorption equilibrium without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using membrane separation without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using separation-process selection without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using stagewise and continuous-contact separation without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| packed-column absorption | Concept developed in §7.1; apply with the section's stated basis and assumptions. |
| gas stripping | Concept developed in §7.2; apply with the section's stated basis and assumptions. |
| liquid-liquid extraction | Concept developed in §7.3; apply with the section's stated basis and assumptions. |
| adsorption equilibrium | Concept developed in §7.4; apply with the section's stated basis and assumptions. |
| membrane separation | Concept developed in §7.5; apply with the section's stated basis and assumptions. |
| separation-process selection | Concept developed in §7.6; apply with the section's stated basis and assumptions. |
| stagewise and continuous-contact separation | Concept developed in §7.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **packed-column absorption** and state the governing relation or balance.

2. Define **gas stripping** and state the governing relation or balance.

3. Define **liquid-liquid extraction** and state the governing relation or balance.

4. Define **adsorption equilibrium** and state the governing relation or balance.

5. Define **membrane separation** and state the governing relation or balance.

6. Define **separation-process selection** and state the governing relation or balance.

7. Define **stagewise and continuous-contact separation** and state the governing relation or balance.

8. What is the most likely error if **packed-column absorption** is applied before the process basis and boundary are defined?

9. What is the most likely error if **gas stripping** is applied before the process basis and boundary are defined?

10. What is the most likely error if **liquid-liquid extraction** is applied before the process basis and boundary are defined?

11. What is the most likely error if **adsorption equilibrium** is applied before the process basis and boundary are defined?

12. What is the most likely error if **membrane separation** is applied before the process basis and boundary are defined?

13. What is the most likely error if **separation-process selection** is applied before the process basis and boundary are defined?

14. What is the most likely error if **stagewise and continuous-contact separation** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **packed-column absorption**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **gas stripping**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **liquid-liquid extraction**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **adsorption equilibrium**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **membrane separation**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **separation-process selection**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **stagewise and continuous-contact separation**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **packed-column absorption**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **gas stripping**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **packed-column absorption** is developed in §7.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **gas stripping** is developed in §7.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **liquid-liquid extraction** is developed in §7.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **adsorption equilibrium** is developed in §7.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **membrane separation** is developed in §7.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **separation-process selection** is developed in §7.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **stagewise and continuous-contact separation** is developed in §7.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

8. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

9. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

10. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

11. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

12. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

13. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

14. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

15. The material balance determines the amounts and compositions needed for enthalpy and reaction-energy calculations.

16. To verify that the unknowns are matched by independent equations/specifications before algebra begins.

17. Whenever the problem provides the model/data; use that stated relation rather than substituting an unstated correlation.

18. The Handbook intentionally omits some theories and formulas; exam specifications can require knowledge not directly tabulated in it.

19. **A.** The relation or workflow for **packed-column absorption** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **gas stripping** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **liquid-liquid extraction** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **adsorption equilibrium** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **membrane separation** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **separation-process selection** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **stagewise and continuous-contact separation** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **packed-column absorption** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

27. **A.** The relation or workflow for **gas stripping** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. Packed absorber NTU=5 and HTU=0.8 m. Find packing height.

2. What is the direction of solute transfer in stripping?

3. Extraction feed carries 10 mol solute; extract contains 7 mol. If no reaction/loss, how much solute remains in raffinate?

4. Batch adsorption: 1 L solution drops from 100 to 20 mg/L using adsorbent. How much solute is adsorbed?

5. Membrane permeability coefficient P/δ gives flux coefficient 2e-6 mol/(m²·s·kPa), Δp=50 kPa. Find flux.

6. Which separation property most directly drives distillation?

7. Why can ideal-stage count not be directly used as packed height?

8. If KG doubles at same driving force and area, what happens to transfer rate?

9. Which process is typically chosen for a dilute gas solute with high liquid solubility?

10. Which process relies on surface affinity to a solid?


---

## Practice Problem Solutions

1. Z=4.0 m.

2. From liquid to gas.

3. 3 mol.

4. 80 mg.

5. 1.0e-4 mol/(m²·s).

6. Volatility/VLE difference.

7. A conversion such as HETP or HTU/NTU is required.

8. It doubles.

9. Absorption.

10. Adsorption.


---

## Quick Reference

**Source anchor:** Chemical Engineering absorption relations, printed p. 253; FE Chemical specification Area 10C–E. Extraction, adsorption, and membrane-process coverage is required by the specification but is not developed with dedicated formula sets in the Chemical Engineering Handbook pages..

- **packed-column absorption:** Packed-Column Absorption — NTU and HTU
- **gas stripping:** Stripping as the Reverse Gas-Liquid Operation
- **liquid-liquid extraction:** Liquid-Liquid Extraction
- **adsorption equilibrium:** Adsorption
- **membrane separation:** Membrane Separations
- **separation-process selection:** Separation Selection by Equilibrium, Driving Force, and Phase
- **stagewise and continuous-contact separation:** Stagewise versus Continuous-Contact Separations
---

## What's Next

**03-08 — Humidification, Drying, and Evaporation**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor