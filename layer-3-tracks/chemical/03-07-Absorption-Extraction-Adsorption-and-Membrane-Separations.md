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

By the end of this chapter, you will be able to:

* **7.1** Explain and apply **Packed-Column Absorption — NTU and HTU**.
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

**Solution.** For **Packed-Column Absorption — NTU and HTU**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) NTU=5, HTU=0.8, Z=4.0 m. This is the section-specific result for Packed absorber NTU HTU packing height. The stated units/basis (Pa, s) are retained.

---

## 7.2 Stripping as the Reverse Gas-Liquid Operation

Stripping transfers a volatile solute from liquid to gas. The same two-film and operating/equilibrium-line ideas used for absorption apply, but the desired transfer direction is reversed.

This treatment is guide-developed from the same mass-transfer balances because the Handbook p. 253 presents the packed-column relation generically.

\[N_A=K_G'(p_A-p_A^*)=K_L'(C_A^*-C_A)\]

![FIG-03-07-002: Countercurrent stripper with solute leaving liquid and entering gas, showing equilibrium and operating lines.](../figures/FIG-03-07-002-stripping-as-the-reverse-gas-liquid-operation.png)

### Worked Example 2

**Problem.** What is the direction of solute transfer in stripping?

**Solution.** For **Stripping as the Reverse Gas-Liquid Operation**, From liquid to gas. This follows because stripping transfers a volatile solute from liquid to gas.. That physical distinction controls the result for direction solute transfer stripping.

---

## 7.3 Liquid-Liquid Extraction

**Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Liquid-liquid extraction transfers a solute between partially immiscible liquid phases.

At equilibrium, a distribution coefficient may be written \(K_D=y/x\) on a specified composition basis. Stagewise balances then combine feed, solvent, extract, and raffinate streams.

\[K_D=\frac{y_A}{x_A},\qquad Fz_A+Sx_{A,S}=R x_A+E y_A\]

![FIG-03-07-003: Mixer-settler stage showing feed, solvent, extract, raffinate, and an equilibrium distribution relation.](../figures/FIG-03-07-003-liquid-liquid-extraction.png)

### Worked Example 3

**Problem.** Extraction feed carries 10 mol solute; extract contains 7 mol. If no reaction/loss, how much solute remains in raffinate?

**Solution.** For **Liquid-Liquid Extraction**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 10, 7, 3 mol. This is the section-specific result for Extraction feed carries mol solute extract contains. The stated units/basis (s, h) are retained.

---

## 7.4 Adsorption

**Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Adsorption transfers a species from a fluid to a solid surface.

For FE-level conceptual calculations, the problem may provide an isotherm such as a linear, Langmuir, or Freundlich relation. Treat that supplied relation as the equilibrium model and combine it with a solute balance.

\[q=q^*(C)\]

![FIG-03-07-004: Adsorbent particles and equilibrium isotherm q versus fluid concentration C, with a batch solute balance.](../figures/FIG-03-07-004-adsorption.png)

### Worked Example 4

**Problem.** Batch adsorption: 1 L solution drops from 100 to 20 mg/L using adsorbent. How much solute is adsorbed?

**Solution.** For **Adsorption**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 1, 100, 20, 80 mg. This is the section-specific result for Batch adsorption solution drops from mg using. The stated units/basis (s, h) are retained.

---

## 7.5 Membrane Separations

**Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** A membrane separates species through selective transport driven by pressure, concentration, chemical potential, or electrical potential differences.

When a problem supplies permeability \(P_i\), a common simplified solution-diffusion form is flux proportional to driving-force difference divided by membrane thickness.

\[J_i=\frac{P_i}{\delta}\,\Delta(\text{driving force})\]

![FIG-03-07-005: Feed-retentate-permeate membrane module with species-selective fluxes and driving force across membrane thickness.](../figures/FIG-03-07-005-membrane-separations.png)

### Worked Example 5

**Problem.** Membrane permeability coefficient P/δ gives flux coefficient 2e-6 mol/(m²·s·kPa), Δp=50 kPa. Find flux.

**Solution.** For **Membrane Separations**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) p=50, 1.0e-4 mol/(m²·s). This is the section-specific result for Membrane permeability coefficient gives flux coefficient e-. The stated units/basis (kPa, Pa) are retained.

---

## 7.6 Separation Selection by Equilibrium, Driving Force, and Phase

A separation method is chosen from the physical property that creates selectivity: volatility for distillation, solubility for absorption/extraction, surface affinity for adsorption, and permeability/selectivity for membranes.

The FE problem usually supplies enough equilibrium or performance information; the engineering task is recognizing which balance and driving force belong to the unit.

\[\text{separation}=\text{balance}+\text{equilibrium/selectivity}+\text{driving force}\]

![FIG-03-07-006: Matrix comparing distillation, absorption, extraction, adsorption, and membranes by phases, driving force, and key equilibrium quantity.](../figures/FIG-03-07-006-separation-selection-by-equilibrium-driving-force-and-phase.png)

### Worked Example 6

**Problem.** Which separation property most directly drives distillation?

**Solution.** For **Separation Selection by Equilibrium, Driving Force, and Phase**, Volatility/VLE difference. This follows because a separation method is chosen from the physical property that creates selectivity: volatility for distillation, solubility for absorption/extraction, surface affinity for adsorption, and permeability/selectivity for membranes.. That physical distinction controls the result for Which separation property most directly drives distillation.

---

## 7.7 Stagewise versus Continuous-Contact Separations

Stagewise devices idealize repeated equilibrium contacts; packed columns and many membrane modules behave as continuous-contact devices. The Handbook relates packed-column height to transfer units and also gives HETP as an equivalent stage measure.

Do not mix ideal-stage count directly with physical height without an efficiency, HETP, HTU, or other conversion relation.

\[Z=N_{EQ}HETP=NTU\cdot HTU\]

![FIG-03-07-007: Tray column and packed column side by side with stage count, HETP, HTU, and NTU relationships.](../figures/FIG-03-07-007-stagewise-versus-continuous-contact-separations.png)

### Worked Example 7

**Problem.** Why can ideal-stage count not be directly used as packed height?

**Solution.** For **Stagewise versus Continuous-Contact Separations**, A conversion such as HETP or HTU/NTU is required. This follows because stagewise devices idealize repeated equilibrium contacts; packed columns and many membrane modules behave as continuous-contact devices.. That physical distinction controls the result for can ideal-stage count not be directly used.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** If KG doubles at same driving force and area, what happens to transfer rate?

**Solution.** For **Integrated Worked Examples**, It doubles. This follows because the section distinguishes the governing physical behavior from the alternatives. That physical distinction controls the result for KG doubles same driving force area happens.

### Worked Example 9

**Problem.** Which process is typically chosen for a dilute gas solute with high liquid solubility?

**Solution.** For **Integrated Worked Examples**, Absorption. This follows because the section distinguishes the governing physical behavior from the alternatives. That physical distinction controls the result for Which process typically chosen dilute gas solute.

---

## As the Handbook States It

Primary source basis: **Chemical Engineering absorption relations, printed p. 253; FE Chemical specification Area 10C–E. Extraction, adsorption, and membrane-process coverage is required by the specification but is not developed with dedicated formula sets in the Chemical Engineering Handbook pages.**.

**Source boundary:** Packed-column absorption is directly supported by Handbook p. 253. Extraction, adsorption, and membrane chapters are specification-required topics for which the Handbook provides limited or no dedicated formulas; those sections are guide-developed and explicitly marked as such.

**External source support:** Green and Southard, eds., *Perry's Chemical Engineers' Handbook*, 9th ed. (2019), supports the non-Handbook separation material: liquid-liquid extraction in Chapter 15 (overview 15-6; design considerations 15-19 to 15-20); adsorption design/equilibrium/equipment in Chapter 16; and membrane-based processes 15-91 to 15-93 plus membrane filtration/scale-up material 20-48 to 20-55. Stripping is supported by Perry's gas-liquid stripping treatment and applications.

**Classification:** Packed-column absorption remains FE-Handbook-supported. Extraction, adsorption, membranes, and broader separation-selection guidance are **specification-required, externally supported**; the final cross-process selection framework is guide synthesis based on the cited Perry sections.

Where the FE specification requires material not directly developed in the Handbook, this chapter now distinguishes **FE-Handbook-supported**, **specification-required / externally supported**, and **guide synthesis based on cited sources**.

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

1. **Packed-Column Absorption — NTU and HTU.** The Handbook writes packed-column height as number of transfer units times height of a transfer unit, on either a gas or liquid basis. In Absorption, Extraction, Adsorption, and Membrane Separations, this is the definition or balance being tested by Question 1.

2. **Stripping as the Reverse Gas-Liquid Operation.** Stripping transfers a volatile solute from liquid to gas. In Absorption, Extraction, Adsorption, and Membrane Separations, this is the definition or balance being tested by Question 2.

3. **Liquid-Liquid Extraction.** **Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Liquid-liquid extraction transfers a solute between partially immiscible liquid phases. In Absorption, Extraction, Adsorption, and Membrane Separations, this is the definition or balance being tested by Question 3.

4. **Adsorption.** **Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Adsorption transfers a species from a fluid to a solid surface. In Absorption, Extraction, Adsorption, and Membrane Separations, this is the definition or balance being tested by Question 4.

5. **Membrane Separations.** **Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** A membrane separates species through selective transport driven by pressure, concentration, chemical potential, or electrical potential differences. In Absorption, Extraction, Adsorption, and Membrane Separations, this is the definition or balance being tested by Question 5.

6. **Separation Selection by Equilibrium, Driving Force, and Phase.** A separation method is chosen from the physical property that creates selectivity: volatility for distillation, solubility for absorption/extraction, surface affinity for adsorption, and permeability/selectivity for membranes. In Absorption, Extraction, Adsorption, and Membrane Separations, this is the definition or balance being tested by Question 6.

7. **Stagewise versus Continuous-Contact Separations.** Stagewise devices idealize repeated equilibrium contacts; packed columns and many membrane modules behave as continuous-contact devices. In Absorption, Extraction, Adsorption, and Membrane Separations, this is the definition or balance being tested by Question 7.

8. For **Packed-Column Absorption — NTU and HTU**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook writes packed-column height as number of transfer units times height of a transfer unit, on either a gas or liquid basis. This is the specific failure mode emphasized in Absorption, Extraction, Adsorption, and Membrane Separations.

9. For **Stripping as the Reverse Gas-Liquid Operation**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Stripping transfers a volatile solute from liquid to gas. This is the specific failure mode emphasized in Absorption, Extraction, Adsorption, and Membrane Separations.

10. For **Liquid-Liquid Extraction**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. **Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Liquid-liquid extraction transfers a solute between partially immiscible liquid phases. This is the specific failure mode emphasized in Absorption, Extraction, Adsorption, and Membrane Separations.

11. For **Adsorption**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. **Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Adsorption transfers a species from a fluid to a solid surface. This is the specific failure mode emphasized in Absorption, Extraction, Adsorption, and Membrane Separations.

12. For **Membrane Separations**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. **Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** A membrane separates species through selective transport driven by pressure, concentration, chemical potential, or electrical potential differences. This is the specific failure mode emphasized in Absorption, Extraction, Adsorption, and Membrane Separations.

13. For **Separation Selection by Equilibrium, Driving Force, and Phase**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A separation method is chosen from the physical property that creates selectivity: volatility for distillation, solubility for absorption/extraction, surface affinity for adsorption, and permeability/selectivity for membranes. This is the specific failure mode emphasized in Absorption, Extraction, Adsorption, and Membrane Separations.

14. For **Stagewise versus Continuous-Contact Separations**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Stagewise devices idealize repeated equilibrium contacts; packed columns and many membrane modules behave as continuous-contact devices. This is the specific failure mode emphasized in Absorption, Extraction, Adsorption, and Membrane Separations.

15. In **Absorption, Extraction, Adsorption, and Membrane Separations**, close the material balance first because stream amounts and compositions feed the later energy calculation. Otherwise enthalpy and duty terms may be evaluated for unresolved streams.

16. For **Absorption, Extraction, Adsorption, and Membrane Separations**, a degrees-of-freedom check counts unknowns against independent equations before solving. Zero indicates a closed problem; a positive count signals missing independent information.

17. In **Absorption, Extraction, Adsorption, and Membrane Separations**, a relation supplied by the FE problem defines the intended model for that question. A remembered correlation can carry different assumptions, coefficients, validity limits, or reference states.

18. For **Absorption, Extraction, Adsorption, and Membrane Separations**, separating Handbook-supported material from specification-required learned material distinguishes lookup knowledge from material the guide develops. That boundary prevents guide-developed content from being presented as Handbook text.

19. **A.** For **Packed-Column Absorption — NTU and HTU**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook writes packed-column height as number of transfer units times height of a transfer unit, on either a gas or liquid basis. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

20. **A.** For **Stripping as the Reverse Gas-Liquid Operation**, the relation is meaningful only with the correct basis and physical assumptions. Stripping transfers a volatile solute from liquid to gas. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

21. **A.** For **Liquid-Liquid Extraction**, the relation is meaningful only with the correct basis and physical assumptions. **Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Liquid-liquid extraction transfers a solute between partially immiscible liquid phases. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

22. **A.** For **Adsorption**, the relation is meaningful only with the correct basis and physical assumptions. **Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** Adsorption transfers a species from a fluid to a solid surface. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

23. **A.** For **Membrane Separations**, the relation is meaningful only with the correct basis and physical assumptions. **Specification-required; not directly tabulated in the Chemical Engineering Handbook section.** A membrane separates species through selective transport driven by pressure, concentration, chemical potential, or electrical potential differences. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

24. **A.** For **Separation Selection by Equilibrium, Driving Force, and Phase**, the relation is meaningful only with the correct basis and physical assumptions. A separation method is chosen from the physical property that creates selectivity: volatility for distillation, solubility for absorption/extraction, surface affinity for adsorption, and permeability/selectivity for membranes. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

25. **A.** For **Stagewise versus Continuous-Contact Separations**, the relation is meaningful only with the correct basis and physical assumptions. Stagewise devices idealize repeated equilibrium contacts; packed columns and many membrane modules behave as continuous-contact devices. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

26. **A.** This later check revisits **Packed-Column Absorption — NTU and HTU** from a different review position. The Handbook writes packed-column height as number of transfer units times height of a transfer unit, on either a gas or liquid basis. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.

27. **A.** This later check revisits **Stripping as the Reverse Gas-Liquid Operation** from a different review position. Stripping transfers a volatile solute from liquid to gas. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.


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

1. For the practice case involving **Packed absorber NTU HTU packing height**, Using NTU=5, HTU=0.8, Z=4.0 m. This completes Practice Problem 1 in Absorption, Extraction, Adsorption, and Membrane Separations. The original Pa, s basis is preserved.

2. For the practice case involving **direction solute transfer stripping**, From liquid to gas. This is the chapter-specific distinction required by Practice Problem 2 in Absorption, Extraction, Adsorption, and Membrane Separations.

3. For the practice case involving **Extraction feed carries mol solute extract contains**, Using 10, 7, 3 mol. This completes Practice Problem 3 in Absorption, Extraction, Adsorption, and Membrane Separations. The original s, h basis is preserved.

4. For the practice case involving **Batch adsorption solution drops from mg using**, Using 1, 100, 20, 80 mg. This completes Practice Problem 4 in Absorption, Extraction, Adsorption, and Membrane Separations. The original s, h basis is preserved.

5. For the practice case involving **Membrane permeability coefficient gives flux coefficient e-**, Using p=50, 1.0e-4 mol/(m²·s). This completes Practice Problem 5 in Absorption, Extraction, Adsorption, and Membrane Separations. The original kPa, Pa basis is preserved.

6. For the practice case involving **Which separation property most directly drives distillation**, Volatility/VLE difference. This is the chapter-specific distinction required by Practice Problem 6 in Absorption, Extraction, Adsorption, and Membrane Separations.

7. For the practice case involving **can ideal-stage count not be directly used**, A conversion such as HETP or HTU/NTU is required. This is the chapter-specific distinction required by Practice Problem 7 in Absorption, Extraction, Adsorption, and Membrane Separations.

8. For the practice case involving **KG doubles same driving force area happens**, It doubles. This is the chapter-specific distinction required by Practice Problem 8 in Absorption, Extraction, Adsorption, and Membrane Separations.

9. For the practice case involving **Which process typically chosen dilute gas solute**, Absorption. This is the chapter-specific distinction required by Practice Problem 9 in Absorption, Extraction, Adsorption, and Membrane Separations.

10. For the practice case involving **Which process relies on surface affinity solid**, Adsorption. This is the chapter-specific distinction required by Practice Problem 10 in Absorption, Extraction, Adsorption, and Membrane Separations.


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
