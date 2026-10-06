---
chapter: "03-03"
title: "Reactive Material Balances, Combustion, and Heats of Reaction"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-003-01, CHE-3-003-02, CHE-3-003-03, CHE-3-003-04, CHE-3-003-05, CHE-3-003-06, CHE-3-003-07]
routes: [chemical]
status: drafted
---

# Chapter 03-03: Reactive Material Balances, Combustion, and Heats of Reaction

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 03-01 Material and Energy Balances · 02-12 Stoichiometry · 02-47 Thermodynamic Properties

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines extent, conversion, limiting reactant, selectivity, yield, heats of reaction, combustion relations, reaction rates, and reactor conversion. This chapter integrates those relations into reactive material and energy balances.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **3.1** Explain and apply **Stoichiometric Coefficients, Extent, Conversion, Yield, and Selectivity**.
* **3.2** Explain and apply **Reactive Species Balances**.
* **3.3** Explain and apply **Limiting and Excess Reactants**.
* **3.4** Explain and apply **Combustion, Theoretical Air, and Excess Air**.
* **3.5** Explain and apply **Standard Heats of Formation and Heat of Reaction**.
* **3.6** Explain and apply **Heat of Reaction Away from the Reference Temperature**.
* **3.7** Explain and apply **Reactive Energy Balances and Adiabatic Temperature**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 3.1 Stoichiometric Coefficients, Extent, Conversion, Yield, and Selectivity

For reaction calculations, use signed stoichiometric coefficients \(\nu_i\): negative for reactants and positive for products. Extent of reaction \(\xi\) converts the balanced equation into a mole-accounting equation.

Conversion measures reactant consumption. Yield and selectivity quantify desired-product performance and require definitions consistent with the problem statement.

\[N_{i,out}=N_{i,in}+\nu_i\xi\]

![FIG-03-03-001: Stoichiometric reaction table linking inlet moles, stoichiometric change, outlet moles, conversion, yield, and selectivity.](../figures/FIG-03-03-001-stoichiometric-coefficients-extent-conversion-yield-and-selectivity.png)

### Worked Example 1

**Problem.** For A→2B, feed 10 mol A and extent ξ=3 mol. Find outlet A and B if no B enters.

**Solution.** A=7 mol; B=6 mol.

---

## 3.2 Reactive Species Balances

A reactive balance can be written using extent or explicit generation terms. Extent is often fastest for a single known reaction; generation-rate balances are more general for multiple reactions or continuous reactors.

Element balances remain valid even when species are created or consumed.

\[\dot n_{i,out}=\dot n_{i,in}+\sum_r\nu_{i,r}\dot\xi_r\]

![FIG-03-03-002: Continuous reactor with species inlet/outlet flows and reaction extents for two simultaneous reactions.](../figures/FIG-03-03-002-reactive-species-balances.png)

### Worked Example 2

**Problem.** For A→B, 100 mol/h A enters and 25 mol/h remains. Find conversion.

**Solution.** 75%.

---

## 3.3 Limiting and Excess Reactants

The limiting reactant is consumed first if the reaction proceeds to completion. An excess reactant is fed above the stoichiometric requirement.

Percent excess is measured relative to the stoichiometric amount required for the actual limiting-reactant feed.

\[\%\text{ excess}=\frac{n_{\rm actual}-n_{\rm stoich}}{n_{\rm stoich}}\times100\%\]

![FIG-03-03-003: Feed table identifying limiting reactant, stoichiometric requirement, and excess reactant percentage.](../figures/FIG-03-03-003-limiting-and-excess-reactants.png)

### Worked Example 3

**Problem.** Reaction 2A+B→P. Feed 10 mol A and 8 mol B. Identify limiting reactant.

**Solution.** A requires 5 mol B, so A is limiting.

---

## 3.4 Combustion, Theoretical Air, and Excess Air

The Handbook states that dry air may be modeled as 3.76 mol nitrogen per mol oxygen for combustion calculations. Begin by balancing the fuel combustion equation, then determine theoretical oxygen and air.

With excess air, unused oxygen appears in products. Incomplete combustion may also produce CO or unburned fuel if specified.

\[\%\text{ excess air}=\frac{(A/F)_{\rm actual}-(A/F)_{\rm stoich}}{(A/F)_{\rm stoich}}\times100\%\]

![FIG-03-03-004: Fuel plus air into combustor, products containing CO2, H2O, N2, possible O2/CO, and theoretical/excess-air calculation.](../figures/FIG-03-03-004-combustion-theoretical-air-and-excess-air.png)

### Worked Example 4

**Problem.** Methane burns with 20% excess air. Stoichiometric O2 is 2 mol/mol CH4. Find actual O2 feed per mol CH4.

**Solution.** 2.4 mol O2/mol CH4; air also carries 2.4×3.76=9.024 mol N2.

---

## 3.5 Standard Heats of Formation and Heat of Reaction

The Handbook evaluates standard heat of reaction from stoichiometric sums of heats of formation. The standard state is identified at the Handbook reference condition.

Apply products minus reactants using signed stoichiometric coefficients.

\[\Delta H_r^\circ=\sum_i\nu_i\Delta H_{f,i}^\circ\]

![FIG-03-03-005: Reaction enthalpy constructed from standard heats of formation of reactants and products.](../figures/FIG-03-03-005-standard-heats-of-formation-and-heat-of-reaction.png)

### Worked Example 5

**Problem.** For a reaction with ΣνΔHf°=-100 kJ/mol reaction, find heat of reaction.

**Solution.** -100 kJ/mol reaction (exothermic).

---

## 3.6 Heat of Reaction Away from the Reference Temperature

If reaction temperature differs from the reference state, the Handbook corrects \(\Delta H_r\) using the difference between product and reactant heat capacities.

For constant heat capacities over a modest range, the integral becomes a heat-capacity difference times temperature change.

\[\Delta H_r(T)=\Delta H_r^\circ(T_{ref})+\int_{T_{ref}}^T\Delta C_p\,dT\]

![FIG-03-03-006: Reference-temperature reaction enthalpy plus sensible-enthalpy correction to operating temperature.](../figures/FIG-03-03-006-heat-of-reaction-away-from-the-reference-temperature.png)

### Worked Example 6

**Problem.** ΔCp=20 J/(mol·K), ΔHr°=-100 kJ/mol at 298 K. Estimate ΔHr at 398 K with constant ΔCp.

**Solution.** -100+0.020×100=-98 kJ/mol.

---

## 3.7 Reactive Energy Balances and Adiabatic Temperature

A reactive process energy balance combines material stoichiometry with sensible enthalpies and reaction enthalpy. In an adiabatic reactor with no shaft work, the reaction energy appears primarily as a temperature change and/or phase change.

Solve reaction extent first, then close the energy balance on a common reference state.

\[0=\sum_{\rm out}\dot n_i\hat H_i-\sum_{\rm in}\dot n_i\hat H_i-\dot Q+\dot W_s\]

![FIG-03-03-007: Adiabatic reactor showing inlet/outlet species, reaction extent, and temperature determined by the energy balance.](../figures/FIG-03-03-007-reactive-energy-balances-and-adiabatic-temperature.png)

### Worked Example 7

**Problem.** What must be solved before an adiabatic flame/reactor temperature?

**Solution.** Reaction extent/composition and a reactive energy balance.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** For A→D and A→U, 80 mol D and 20 mol U form. Find D/U selectivity.

**Solution.** 4.

### Worked Example 9

**Problem.** Stoichiometric air/fuel mass ratio is 17.2; actual is 20.64. Find percent excess air.

**Solution.** (20.64-17.2)/17.2×100=20%.

---

## As the Handbook States It

Primary source basis: **Thermodynamics, printed pp. 152–156; Chemical Engineering, printed pp. 243–247; FE Chemical specification Areas 7H and 8F**.

**Source boundary:** The Handbook directly defines extent, conversion, limiting reactant, selectivity, yield, heats of reaction, combustion relations, reaction rates, and reactor conversion. This chapter integrates those relations into reactive material and energy balances.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using reaction extent and performance measures without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using reactive material balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using limiting and excess reactants without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using combustion air balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using heat of reaction without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using temperature-corrected reaction enthalpy without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using reactive energy balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| reaction extent and performance measures | Concept developed in §3.1; apply with the section's stated basis and assumptions. |
| reactive material balance | Concept developed in §3.2; apply with the section's stated basis and assumptions. |
| limiting and excess reactants | Concept developed in §3.3; apply with the section's stated basis and assumptions. |
| combustion air balance | Concept developed in §3.4; apply with the section's stated basis and assumptions. |
| heat of reaction | Concept developed in §3.5; apply with the section's stated basis and assumptions. |
| temperature-corrected reaction enthalpy | Concept developed in §3.6; apply with the section's stated basis and assumptions. |
| reactive energy balance | Concept developed in §3.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **reaction extent and performance measures** and state the governing relation or balance.

2. Define **reactive material balance** and state the governing relation or balance.

3. Define **limiting and excess reactants** and state the governing relation or balance.

4. Define **combustion air balance** and state the governing relation or balance.

5. Define **heat of reaction** and state the governing relation or balance.

6. Define **temperature-corrected reaction enthalpy** and state the governing relation or balance.

7. Define **reactive energy balance** and state the governing relation or balance.

8. What is the most likely error if **reaction extent and performance measures** is applied before the process basis and boundary are defined?

9. What is the most likely error if **reactive material balance** is applied before the process basis and boundary are defined?

10. What is the most likely error if **limiting and excess reactants** is applied before the process basis and boundary are defined?

11. What is the most likely error if **combustion air balance** is applied before the process basis and boundary are defined?

12. What is the most likely error if **heat of reaction** is applied before the process basis and boundary are defined?

13. What is the most likely error if **temperature-corrected reaction enthalpy** is applied before the process basis and boundary are defined?

14. What is the most likely error if **reactive energy balance** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **reaction extent and performance measures**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **reactive material balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **limiting and excess reactants**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **combustion air balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **heat of reaction**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **temperature-corrected reaction enthalpy**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **reactive energy balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **reaction extent and performance measures**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **reactive material balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **reaction extent and performance measures** is developed in §3.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **reactive material balance** is developed in §3.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **limiting and excess reactants** is developed in §3.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **combustion air balance** is developed in §3.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **heat of reaction** is developed in §3.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **temperature-corrected reaction enthalpy** is developed in §3.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **reactive energy balance** is developed in §3.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

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

19. **A.** The relation or workflow for **reaction extent and performance measures** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **reactive material balance** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **limiting and excess reactants** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **combustion air balance** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **heat of reaction** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **temperature-corrected reaction enthalpy** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **reactive energy balance** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **reaction extent and performance measures** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

27. **A.** The relation or workflow for **reactive material balance** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. For A→2B, feed 10 mol A and extent ξ=3 mol. Find outlet A and B if no B enters.

2. For A→B, 100 mol/h A enters and 25 mol/h remains. Find conversion.

3. Reaction 2A+B→P. Feed 10 mol A and 8 mol B. Identify limiting reactant.

4. Methane burns with 20% excess air. Stoichiometric O2 is 2 mol/mol CH4. Find actual O2 feed per mol CH4.

5. For a reaction with ΣνΔHf°=-100 kJ/mol reaction, find heat of reaction.

6. ΔCp=20 J/(mol·K), ΔHr°=-100 kJ/mol at 298 K. Estimate ΔHr at 398 K with constant ΔCp.

7. What must be solved before an adiabatic flame/reactor temperature?

8. For A→D and A→U, 80 mol D and 20 mol U form. Find D/U selectivity.

9. Stoichiometric air/fuel mass ratio is 17.2; actual is 20.64. Find percent excess air.

10. A fuel releases 800 kJ/mol and 0.5 mol/s reacts adiabatically. What energy release rate must products absorb if no work?


---

## Practice Problem Solutions

1. A=7 mol; B=6 mol.

2. 75%.

3. A requires 5 mol B, so A is limiting.

4. 2.4 mol O2/mol CH4; air also carries 2.4×3.76=9.024 mol N2.

5. -100 kJ/mol reaction (exothermic).

6. -100+0.020×100=-98 kJ/mol.

7. Reaction extent/composition and a reactive energy balance.

8. 4.

9. (20.64-17.2)/17.2×100=20%.

10. 400 kW.


---

## Quick Reference

**Source anchor:** Thermodynamics, printed pp. 152–156; Chemical Engineering, printed pp. 243–247; FE Chemical specification Areas 7H and 8F.

- **reaction extent and performance measures:** Stoichiometric Coefficients, Extent, Conversion, Yield, and Selectivity
- **reactive material balance:** Reactive Species Balances
- **limiting and excess reactants:** Limiting and Excess Reactants
- **combustion air balance:** Combustion, Theoretical Air, and Excess Air
- **heat of reaction:** Standard Heats of Formation and Heat of Reaction
- **temperature-corrected reaction enthalpy:** Heat of Reaction Away from the Reference Temperature
- **reactive energy balance:** Reactive Energy Balances and Adiabatic Temperature
---

## What's Next

**03-04 — Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor