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

**Solution.** Apply the relation and model in §82.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 82.2 Theoretical air and excess air

Real burners often operate with excess air to promote complete combustion. Excess air changes flue-gas composition and stack losses.

\[\%\text{excess air}=100\frac{A_{actual}-A_{theoretical}}{A_{theoretical}}\]

![FIG-03-82-002: Combustor with theoretical and actual air inputs and dry/wet product composition.](../figures/FIG-03-82-002-theoretical-air-and-excess-air.png)

### Worked Example 2

**Problem.** 120% theoretical air corresponds to 20% excess air.

**Solution.** Apply the relation and model in §82.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 82.3 Combustion-product analysis

Product analysis distinguishes wet and dry basis and can be used to infer excess air or incomplete combustion.

\[\text{atom balances constrain CO}_2,\mathrm{H_2O},\mathrm{O_2},\mathrm{N_2},\mathrm{CO}\]

![FIG-03-82-003: Wet versus dry flue-gas composition and atom-balance table.](../figures/FIG-03-82-003-combustion-product-analysis.png)

### Worked Example 3

**Problem.** Dry-basis analysis excludes water vapor from the composition denominator.

**Solution.** Apply the relation and model in §82.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 82.4 Heating value and combustion energy balance

Heating value connects fuel consumption with released chemical energy. Higher and lower heating values differ in treatment of water condensation.

\[\dot Q\approx \dot m_f\,HV\]

![FIG-03-82-004: Combustor energy-flow diagram with fuel heating value, sensible enthalpy, heat loss, and products.](../figures/FIG-03-82-004-heating-value-and-combustion-energy-balance.png)

### Worked Example 4

**Problem.** A 0.01 kg/s fuel flow at 40 MJ/kg represents 400 kW fuel-energy rate.

**Solution.** Apply the relation and model in §82.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 82.5 Adiabatic flame temperature concept

The ideal adiabatic flame temperature follows from an energy balance with no heat loss and specified reaction products. Dissociation can matter at very high temperature.

\[\sum H_{reactants}=\sum H_{products}\]

![FIG-03-82-005: Combustor enthalpy balance showing reactant inlet temperature and product adiabatic flame temperature.](../figures/FIG-03-82-005-adiabatic-flame-temperature-concept.png)

### Worked Example 5

**Problem.** Preheating reactants generally raises the ideal adiabatic flame temperature.

**Solution.** Apply the relation and model in §82.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 82.6 Incomplete combustion and emissions

Incomplete combustion can create carbon monoxide, soot, and unburned hydrocarbons. Too much excess air can also reduce thermal efficiency.

\[\text{insufficient mixing/oxygen/time/temperature can produce CO and unburned species}\]

![FIG-03-82-006: Combustion quality map showing effects of equivalence/excess air on CO, unburned fuel, and efficiency.](../figures/FIG-03-82-006-incomplete-combustion-and-emissions.png)

### Worked Example 6

**Problem.** CO in products indicates incomplete oxidation of carbon under the simplified interpretation.

**Solution.** Apply the relation and model in §82.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 82.7 Combustion safety and model verification

Combustion calculations are sensitive to molar versus mass basis and wet versus dry products. Engineering design must also address ignition, flame stability, ventilation, and material temperatures.

\[\text{verify fuel basis, air basis, wet/dry products, energy basis, and safe operating limits}\]

![FIG-03-82-007: Combustion calculation checklist linking atom balance, air ratio, products, energy, emissions, and safety.](../figures/FIG-03-82-007-combustion-safety-and-model-verification.png)

### Worked Example 7

**Problem.** A dry flue-gas oxygen percentage cannot be inserted directly into a wet-basis balance without conversion.

**Solution.** Apply the relation and model in §82.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. Select the correct model or failure/operating region and solve again. Algebra does not override geometry, material behavior, or component-state validity.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** Use the Handbook expression and its definitions unless the problem explicitly provides another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 11; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** The Mechanical specification includes both directly tabulated Handbook equations and learned design concepts. This chapter does not assign invented Handbook pages to specification-required material that is not directly tabulated.

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

15. The sketch exposes supports, force directions, geometry, constraints, energy/flow paths, and missing load cases before algebra obscures them.

16. Mechanical equations are model-dependent. The result must remain compatible with yielding/buckling/fatigue, flow regime, thermal state, contact, or kinematic constraints.

17. The Handbook is the supplied exam reference; its definitions, correction factors, unit conventions, and tables should govern unless the problem explicitly supplies another relation.

18. These checks catch impossible motion, unit errors, invalid thin-wall or linear assumptions, unrealistic stresses, interference, and parts that cannot be manufactured or assembled.

19. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

20. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

21. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

22. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

23. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

24. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

25. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

26. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

27. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.


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

1. Use §82.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §82.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §82.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §82.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §82.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §82.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §82.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 11, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

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
