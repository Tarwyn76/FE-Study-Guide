---
chapter: "03-82"
title: "Combustion and Combustion Products"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-082-01, MEC-3-082-02, MEC-3-082-03, MEC-3-082-04, MEC-3-082-05, MEC-3-082-06, MEC-3-082-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-82: Combustion and Combustion Products

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** THERMO-2D-047-01

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Combustion and Combustion Products**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **82.1** Explain and apply **Fuel formulas and stoichiometric oxygen demand**.
* **82.2** Explain and apply **Theoretical air and excess air**.
* **82.3** Explain and apply **Combustion-product analysis**.
* **82.4** Explain and apply **Heating value and combustion energy balance**.
* **82.5** Explain and apply **Adiabatic flame temperature concept**.
* **82.6** Explain and apply **Incomplete combustion and emissions**.
* **82.7** Explain and apply **Combustion safety and model verification**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 82.1 Fuel formulas and stoichiometric oxygen demand

Complete stoichiometric combustion balances atoms to determine theoretical oxygen and air requirements.

\[\mathrm{C_xH_y}+\left(x+\frac y4\right)\mathrm{O_2}\rightarrow x\mathrm{CO_2}+\frac y2\mathrm{H_2O}\]

![FIG-03-82-001: Fuel plus air reaction balance with carbon, hydrogen, oxygen, and nitrogen species tracked.](../figures/FIG-03-82-001-fuel-formulas-and-stoichiometric-oxygen-demand.png)

### Worked Example 1

**Problem.** Methane requires 2 mol O2 per mol CH4 for complete combustion.

**Solution.** Balance atoms: \(\mathrm{CH_4}+2\mathrm{O_2}\rightarrow\mathrm{CO_2}+2\mathrm{H_2O}\). Therefore complete stoichiometric combustion requires **2 mol O\(_2\)** per mol CH\(_4\).

---

## 82.2 Theoretical air and excess air

Real burners often operate with excess air to promote complete combustion. Excess air changes flue-gas composition and stack losses.

\[\%\text{excess air}=100\frac{A_{actual}-A_{theoretical}}{A_{theoretical}}\]

![FIG-03-82-002: Combustor with theoretical and actual air inputs and dry/wet product composition.](../figures/FIG-03-82-002-theoretical-air-and-excess-air.png)

### Worked Example 2

**Problem.** 120% theoretical air corresponds to 20% excess air.

**Solution.** \(120\%\) theoretical air means \(A_{actual}=1.20A_{theoretical}\). Thus excess air is \((1.20-1.00)\times100\%=\mathbf{20\%}\).

---

## 82.3 Combustion-product analysis

Product analysis distinguishes wet and dry basis and can be used to infer excess air or incomplete combustion.

\[\text{atom balances constrain CO}_2,\mathrm{H_2O},\mathrm{O_2},\mathrm{N_2},\mathrm{CO}\]

![FIG-03-82-003: Wet versus dry flue-gas composition and atom-balance table.](../figures/FIG-03-82-003-combustion-product-analysis.png)

### Worked Example 3

**Problem.** Dry-basis analysis excludes water vapor from the composition denominator.

**Solution.** Dry-basis product composition excludes water vapor from the mole-fraction denominator. The same product stream therefore has different wet- and dry-basis percentages; atom balances must be performed before choosing the reporting basis.

---

## 82.4 Heating value and combustion energy balance

Heating value connects fuel consumption with released chemical energy. Higher and lower heating values differ in treatment of water condensation.

\[\dot Q\approx \dot m_f\,HV\]

![FIG-03-82-004: Combustor energy-flow diagram with fuel heating value, sensible enthalpy, heat loss, and products.](../figures/FIG-03-82-004-heating-value-and-combustion-energy-balance.png)

### Worked Example 4

**Problem.** A 0.01 kg/s fuel flow at 40 MJ/kg represents 400 kW fuel-energy rate.

**Solution.** \(\dot Q_{fuel}=\dot m_fHV=(0.01\ {\rm kg/s})(40\ {\rm MJ/kg})=0.40\ {\rm MJ/s}=\mathbf{400\ kW}\).

---

## 82.5 Adiabatic flame temperature concept

The ideal adiabatic flame temperature follows from an energy balance with no heat loss and specified reaction products. Dissociation can matter at very high temperature.

\[\sum H_{reactants}=\sum H_{products}\]

![FIG-03-82-005: Combustor enthalpy balance showing reactant inlet temperature and product adiabatic flame temperature.](../figures/FIG-03-82-005-adiabatic-flame-temperature-concept.png)

### Worked Example 5

**Problem.** Preheating reactants generally raises the ideal adiabatic flame temperature.

**Solution.** Under an adiabatic model, reactant enthalpy plus chemical energy is balanced by product enthalpy. Preheating the reactants raises their initial sensible enthalpy, so the ideal adiabatic flame temperature generally rises when the product set is otherwise comparable.

---

## 82.6 Incomplete combustion and emissions

Incomplete combustion can create carbon monoxide, soot, and unburned hydrocarbons. Too much excess air can also reduce thermal efficiency.

\[\text{insufficient mixing/oxygen/time/temperature can produce CO and unburned species}\]

![FIG-03-82-006: Combustion quality map showing effects of equivalence/excess air on CO, unburned fuel, and efficiency.](../figures/FIG-03-82-006-incomplete-combustion-and-emissions.png)

### Worked Example 6

**Problem.** CO in products indicates incomplete oxidation of carbon under the simplified interpretation.

**Solution.** CO in the products means some carbon did not reach complete oxidation to CO\(_2\). Insufficient oxygen, mixing, residence time, or temperature can cause incomplete combustion and leave CO/unburned species.

---

## 82.7 Combustion safety and model verification

Combustion calculations are sensitive to molar versus mass basis and wet versus dry products. Engineering design must also address ignition, flame stability, ventilation, and material temperatures.

\[\text{verify fuel basis, air basis, wet/dry products, energy basis, and safe operating limits}\]

![FIG-03-82-007: Combustion calculation checklist linking atom balance, air ratio, products, energy, emissions, and safety.](../figures/FIG-03-82-007-combustion-safety-and-model-verification.png)

### Worked Example 7

**Problem.** A dry flue-gas oxygen percentage cannot be inserted directly into a wet-basis balance without conversion.

**Solution.** Always state fuel basis, actual/theoretical-air basis, and wet/dry product basis. For example, a dry flue-gas O\(_2\) percentage cannot be inserted directly into a wet-basis mole balance because water is absent from the dry denominator.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. Combustion calculations must conserve each element and energy on one wet/dry and actual/theoretical-air basis. Negative species or unbalanced atoms identify an invalid product model.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Combustion and Combustion Products**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **TURNS** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 11; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Turns, S. R., & Haworth, D. C. (2021). *An Introduction to Combustion: Concepts and Applications* (4th ed.). McGraw Hill. ISBN 978-1-260-47769-6. Supporting scope: Stoichiometry, theoretical/excess air, combustion products, heating values, flame temperature, and emissions.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using stoichiometric combustion outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using excess air outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using flue gas analysis outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using fuel heating value outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using adiabatic flame temperature outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using combustion completeness outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using combustion design check outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| stoichiometric combustion | Concept developed in §82.1; apply with that section's geometry and operating assumptions. |
| excess air | Concept developed in §82.2; apply with that section's geometry and operating assumptions. |
| flue gas analysis | Concept developed in §82.3; apply with that section's geometry and operating assumptions. |
| fuel heating value | Concept developed in §82.4; apply with that section's geometry and operating assumptions. |
| adiabatic flame temperature | Concept developed in §82.5; apply with that section's geometry and operating assumptions. |
| combustion completeness | Concept developed in §82.6; apply with that section's geometry and operating assumptions. |
| combustion design check | Concept developed in §82.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **stoichiometric combustion** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **excess air** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **flue gas analysis** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **fuel heating value** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **adiabatic flame temperature** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **combustion completeness** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **combustion design check** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **stoichiometric combustion**?

9. What geometric, material, operating, or model assumption must be checked before applying **excess air**?

10. What geometric, material, operating, or model assumption must be checked before applying **flue gas analysis**?

11. What geometric, material, operating, or model assumption must be checked before applying **fuel heating value**?

12. What geometric, material, operating, or model assumption must be checked before applying **adiabatic flame temperature**?

13. What geometric, material, operating, or model assumption must be checked before applying **combustion completeness**?

14. What geometric, material, operating, or model assumption must be checked before applying **combustion design check**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **stoichiometric combustion**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **excess air**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **flue gas analysis**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **fuel heating value**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **adiabatic flame temperature**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **combustion completeness**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **combustion design check**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **stoichiometric combustion**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **excess air**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **stoichiometric combustion** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **excess air** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **flue gas analysis** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **fuel heating value** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **adiabatic flame temperature** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **combustion completeness** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **combustion design check** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **stoichiometric combustion**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **excess air**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **flue gas analysis**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **fuel heating value**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **adiabatic flame temperature**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **combustion completeness**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **combustion design check**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

15. In **Combustion and Combustion Products**, start from the physical model and system/component state, not from an isolated formula. A valid solution must balance C/H/O/N atoms, state theoretical versus excess air, keep wet/dry product basis explicit, and close the combustion energy balance.

16. Units and sign/reference conventions are part of the model in **Combustion and Combustion Products**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Combustion and Combustion Products**. External sources **TURNS** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: use methane and verify atom balance requires two O2 per CH4; set actual air equal to theoretical air and confirm excess air is zero. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §82.1, **Fuel formulas and stoichiometric oxygen demand**, uses \(\mathrm{C_xH_y}+\left(x+\frac y4\right)\mathrm{O_2}\rightarrow x\mathrm{CO_2}+\frac y2\mathrm{H_2O}\). Apply it only under the geometry/material/operating assumptions stated in §82.1, then compare the result with the physical behavior described there.

20. **A.** Section §82.2, **Theoretical air and excess air**, uses \(\%\text{excess air}=100\frac{A_{actual}-A_{theoretical}}{A_{theoretical}}\). Apply it only under the geometry/material/operating assumptions stated in §82.2, then compare the result with the physical behavior described there.

21. **A.** Section §82.3, **Combustion-product analysis**, uses \(\text{atom balances constrain CO}_2,\mathrm{H_2O},\mathrm{O_2},\mathrm{N_2},\mathrm{CO}\). Apply it only under the geometry/material/operating assumptions stated in §82.3, then compare the result with the physical behavior described there.

22. **A.** Section §82.4, **Heating value and combustion energy balance**, uses \(\dot Q\approx \dot m_f\,HV\). Apply it only under the geometry/material/operating assumptions stated in §82.4, then compare the result with the physical behavior described there.

23. **A.** Section §82.5, **Adiabatic flame temperature concept**, uses \(\sum H_{reactants}=\sum H_{products}\). Apply it only under the geometry/material/operating assumptions stated in §82.5, then compare the result with the physical behavior described there.

24. **A.** Section §82.6, **Incomplete combustion and emissions**, uses \(\text{insufficient mixing/oxygen/time/temperature can produce CO and unburned species}\). Apply it only under the geometry/material/operating assumptions stated in §82.6, then compare the result with the physical behavior described there.

25. **A.** Section §82.7, **Combustion safety and model verification**, uses \(\text{verify fuel basis, air basis, wet/dry products, energy basis, and safe operating limits}\). Apply it only under the geometry/material/operating assumptions stated in §82.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Combustion and Combustion Products** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **TURNS**; guide synthesis is supplemental explanation and exam-oriented workflow.


---

## Practice Problems

1. Methane requires 2 mol O2 per mol CH4 for complete combustion.

2. 120% theoretical air corresponds to 20% excess air.

3. Dry-basis analysis excludes water vapor from the composition denominator.

4. A 0.01 kg/s fuel flow at 40 MJ/kg represents 400 kW fuel-energy rate.

5. Preheating reactants generally raises the ideal adiabatic flame temperature.

6. CO in products indicates incomplete oxidation of carbon under the simplified interpretation.

7. A dry flue-gas oxygen percentage cannot be inserted directly into a wet-basis balance without conversion.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. **Independent check for §82.1 — Fuel formulas and stoichiometric oxygen demand.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Balance atoms: \(\mathrm{CH_4}+2\mathrm{O_2}\rightarrow\mathrm{CO_2}+2\mathrm{H_2O}\). Therefore complete stoichiometric combustion requires **2 mol O\(_2\)** per mol CH\(_4\).

2. **Independent check for §82.2 — Theoretical air and excess air.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(120\%\) theoretical air means \(A_{actual}=1.20A_{theoretical}\). Thus excess air is \((1.20-1.00)\times100\%=\mathbf{20\%}\).

3. **Independent check for §82.3 — Combustion-product analysis.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Dry-basis product composition excludes water vapor from the mole-fraction denominator. The same product stream therefore has different wet- and dry-basis percentages; atom balances must be performed before choosing the reporting basis.

4. **Independent check for §82.4 — Heating value and combustion energy balance.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\dot Q_{fuel}=\dot m_fHV=(0.01\ {\rm kg/s})(40\ {\rm MJ/kg})=0.40\ {\rm MJ/s}=\mathbf{400\ kW}\).

5. **Independent check for §82.5 — Adiabatic flame temperature concept.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Under an adiabatic model, reactant enthalpy plus chemical energy is balanced by product enthalpy. Preheating the reactants raises their initial sensible enthalpy, so the ideal adiabatic flame temperature generally rises when the product set is otherwise comparable.

6. **Independent check for §82.6 — Incomplete combustion and emissions.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. CO in the products means some carbon did not reach complete oxidation to CO\(_2\). Insufficient oxygen, mixing, residence time, or temperature can cause incomplete combustion and leave CO/unburned species.

7. **Independent check for §82.7 — Combustion safety and model verification.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Always state fuel basis, actual/theoretical-air basis, and wet/dry product basis. For example, a dry flue-gas O\(_2\) percentage cannot be inserted directly into a wet-basis mole balance because water is absent from the dry denominator.

8. For **Combustion and Combustion Products**, one required acceptance screen is: balance C/H/O/N atoms, state theoretical versus excess air, keep wet/dry product basis explicit, and close the combustion energy balance. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Combustion and Combustion Products**. For `split_required` concepts, use **TURNS** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: use methane and verify atom balance requires two O2 per CH4; set actual air equal to theoretical air and confirm excess air is zero. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 11.

- **stoichiometric combustion:** Fuel formulas and stoichiometric oxygen demand
- **excess air:** Theoretical air and excess air
- **flue gas analysis:** Combustion-product analysis
- **fuel heating value:** Heating value and combustion energy balance
- **adiabatic flame temperature:** Adiabatic flame temperature concept
- **combustion completeness:** Incomplete combustion and emissions
- **combustion design check:** Combustion safety and model verification

---

## What's Next

**Chapter 03-83: HVAC Processes, Loads, Psychrometrics, and Equipment Performance**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
