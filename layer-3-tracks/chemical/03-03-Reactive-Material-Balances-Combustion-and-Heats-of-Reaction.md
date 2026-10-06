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

By the end of this chapter, you will be able to:

* **3.1** Explain and apply **Stoichiometric Coefficients, Extent, Conversion, Yield, and Selectivity**.
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

**Solution.** For **Stoichiometric Coefficients, Extent, Conversion, Yield, and Selectivity**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) =3, A=7 mol; B=6 mol. This is the section-specific result for feed mol extent mol outlet no enters. The stated units/basis (s) are retained.

---

## 3.2 Reactive Species Balances

A reactive balance can be written using extent or explicit generation terms. Extent is often fastest for a single known reaction; generation-rate balances are more general for multiple reactions or continuous reactors.

Element balances remain valid even when species are created or consumed.

\[\dot n_{i,out}=\dot n_{i,in}+\sum_r\nu_{i,r}\dot\xi_r\]

![FIG-03-03-002: Continuous reactor with species inlet/outlet flows and reaction extents for two simultaneous reactions.](../figures/FIG-03-03-002-reactive-species-balances.png)

### Worked Example 2

**Problem.** For A→B, 100 mol/h A enters and 25 mol/h remains. Find conversion.

**Solution.** For **Reactive Species Balances**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 100, 25, 75%. This is the section-specific result for mol enters mol remains conversion. The stated units/basis (mol/h, s) are retained.

---

## 3.3 Limiting and Excess Reactants

The limiting reactant is consumed first if the reaction proceeds to completion. An excess reactant is fed above the stoichiometric requirement.

Percent excess is measured relative to the stoichiometric amount required for the actual limiting-reactant feed.

\[\%\text{ excess}=\frac{n_{\rm actual}-n_{\rm stoich}}{n_{\rm stoich}}\times100\%\]

![FIG-03-03-003: Feed table identifying limiting reactant, stoichiometric requirement, and excess reactant percentage.](../figures/FIG-03-03-003-limiting-and-excess-reactants.png)

### Worked Example 3

**Problem.** Reaction 2A+B→P. Feed 10 mol A and 8 mol B. Identify limiting reactant.

**Solution.** For **Limiting and Excess Reactants**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 2, 10, 8, A requires 5 mol B, so A is limiting. This is the section-specific result for Reaction Feed mol mol Identify limiting reactant.

---

## 3.4 Combustion, Theoretical Air, and Excess Air

The Handbook states that dry air may be modeled as 3.76 mol nitrogen per mol oxygen for combustion calculations. Begin by balancing the fuel combustion equation, then determine theoretical oxygen and air.

With excess air, unused oxygen appears in products. Incomplete combustion may also produce CO or unburned fuel if specified.

\[\%\text{ excess air}=\frac{(A/F)_{\rm actual}-(A/F)_{\rm stoich}}{(A/F)_{\rm stoich}}\times100\%\]

![FIG-03-03-004: Fuel plus air into combustor, products containing CO2, H2O, N2, possible O2/CO, and theoretical/excess-air calculation.](../figures/FIG-03-03-004-combustion-theoretical-air-and-excess-air.png)

### Worked Example 4

**Problem.** Methane burns with 20% excess air. Stoichiometric O2 is 2 mol/mol CH4. Find actual O2 feed per mol CH4.

**Solution.** For **Combustion, Theoretical Air, and Excess Air**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 20%, 2, 2, 2.4 mol O2/mol CH4; air also carries 2.4×3.76=9.024 mol N2. This is the section-specific result for Methane burns excess air Stoichiometric mol mol. The stated units/basis (s, h) are retained.

---

## 3.5 Standard Heats of Formation and Heat of Reaction

The Handbook evaluates standard heat of reaction from stoichiometric sums of heats of formation. The standard state is identified at the Handbook reference condition.

Apply products minus reactants using signed stoichiometric coefficients.

\[\Delta H_r^\circ=\sum_i\nu_i\Delta H_{f,i}^\circ\]

![FIG-03-03-005: Reaction enthalpy constructed from standard heats of formation of reactants and products.](../figures/FIG-03-03-005-standard-heats-of-formation-and-heat-of-reaction.png)

### Worked Example 5

**Problem.** For a reaction with ΣνΔHf°=-100 kJ/mol reaction, find heat of reaction.

**Solution.** For **Standard Heats of Formation and Heat of Reaction**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) =-100, -100 kJ/mol reaction (exothermic). This is the section-specific result for reaction Hf kJ mol reaction heat reaction. The stated units/basis (kJ/mol, h) are retained.

---

## 3.6 Heat of Reaction Away from the Reference Temperature

If reaction temperature differs from the reference state, the Handbook corrects \(\Delta H_r\) using the difference between product and reactant heat capacities.

For constant heat capacities over a modest range, the integral becomes a heat-capacity difference times temperature change.

\[\Delta H_r(T)=\Delta H_r^\circ(T_{ref})+\int_{T_{ref}}^T\Delta C_p\,dT\]

![FIG-03-03-006: Reference-temperature reaction enthalpy plus sensible-enthalpy correction to operating temperature.](../figures/FIG-03-03-006-heat-of-reaction-away-from-the-reference-temperature.png)

### Worked Example 6

**Problem.** ΔCp=20 J/(mol·K), ΔHr°=-100 kJ/mol at 298 K. Estimate ΔHr at 398 K with constant ΔCp.

**Solution.** For **Heat of Reaction Away from the Reference Temperature**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) Cp=20, =-100, -100+0.020×100=-98 kJ/mol. This is the section-specific result for Cp mol Hr kJ mol Estimate Hr. The stated units/basis (kJ/mol, J/(mol·K)) are retained.

---

## 3.7 Reactive Energy Balances and Adiabatic Temperature

A reactive process energy balance combines material stoichiometry with sensible enthalpies and reaction enthalpy. In an adiabatic reactor with no shaft work, the reaction energy appears primarily as a temperature change and/or phase change.

Solve reaction extent first, then close the energy balance on a common reference state.

\[0=\sum_{\rm out}\dot n_i\hat H_i-\sum_{\rm in}\dot n_i\hat H_i-\dot Q+\dot W_s\]

![FIG-03-03-007: Adiabatic reactor showing inlet/outlet species, reaction extent, and temperature determined by the energy balance.](../figures/FIG-03-03-007-reactive-energy-balances-and-adiabatic-temperature.png)

### Worked Example 7

**Problem.** What must be solved before an adiabatic flame/reactor temperature?

**Solution.** For **Reactive Energy Balances and Adiabatic Temperature**, Reaction extent/composition and a reactive energy balance. This follows because a reactive process energy balance combines material stoichiometry with sensible enthalpies and reaction enthalpy.. That physical distinction controls the result for must be solved before adiabatic flame reactor.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** For A→D and A→U, 80 mol D and 20 mol U form. Find D/U selectivity.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 80, 20, 4. This is the section-specific result for mol mol form selectivity. The stated units/basis (s) are retained.

### Worked Example 9

**Problem.** Stoichiometric air/fuel mass ratio is 17.2; actual is 20.64. Find percent excess air.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 17.2, 20.64, (20.64-17.2)/17.2×100=20%. This is the section-specific result for Stoichiometric air fuel mass ratio actual percent. The stated units/basis (s, h) are retained.

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

1. **Stoichiometric Coefficients, Extent, Conversion, Yield, and Selectivity.** For reaction calculations, use signed stoichiometric coefficients \(\nu_i\): negative for reactants and positive for products. In Reactive Material Balances, Combustion, and Heats of Reaction, this is the definition or balance being tested by Question 1.

2. **Reactive Species Balances.** A reactive balance can be written using extent or explicit generation terms. In Reactive Material Balances, Combustion, and Heats of Reaction, this is the definition or balance being tested by Question 2.

3. **Limiting and Excess Reactants.** The limiting reactant is consumed first if the reaction proceeds to completion. In Reactive Material Balances, Combustion, and Heats of Reaction, this is the definition or balance being tested by Question 3.

4. **Combustion, Theoretical Air, and Excess Air.** The Handbook states that dry air may be modeled as 3.76 mol nitrogen per mol oxygen for combustion calculations. In Reactive Material Balances, Combustion, and Heats of Reaction, this is the definition or balance being tested by Question 4.

5. **Standard Heats of Formation and Heat of Reaction.** The Handbook evaluates standard heat of reaction from stoichiometric sums of heats of formation. In Reactive Material Balances, Combustion, and Heats of Reaction, this is the definition or balance being tested by Question 5.

6. **Heat of Reaction Away from the Reference Temperature.** If reaction temperature differs from the reference state, the Handbook corrects \(\Delta H_r\) using the difference between product and reactant heat capacities. In Reactive Material Balances, Combustion, and Heats of Reaction, this is the definition or balance being tested by Question 6.

7. **Reactive Energy Balances and Adiabatic Temperature.** A reactive process energy balance combines material stoichiometry with sensible enthalpies and reaction enthalpy. In Reactive Material Balances, Combustion, and Heats of Reaction, this is the definition or balance being tested by Question 7.

8. For **Stoichiometric Coefficients, Extent, Conversion, Yield, and Selectivity**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For reaction calculations, use signed stoichiometric coefficients \(\nu_i\): negative for reactants and positive for products. This is the specific failure mode emphasized in Reactive Material Balances, Combustion, and Heats of Reaction.

9. For **Reactive Species Balances**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A reactive balance can be written using extent or explicit generation terms. This is the specific failure mode emphasized in Reactive Material Balances, Combustion, and Heats of Reaction.

10. For **Limiting and Excess Reactants**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The limiting reactant is consumed first if the reaction proceeds to completion. This is the specific failure mode emphasized in Reactive Material Balances, Combustion, and Heats of Reaction.

11. For **Combustion, Theoretical Air, and Excess Air**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook states that dry air may be modeled as 3.76 mol nitrogen per mol oxygen for combustion calculations. This is the specific failure mode emphasized in Reactive Material Balances, Combustion, and Heats of Reaction.

12. For **Standard Heats of Formation and Heat of Reaction**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook evaluates standard heat of reaction from stoichiometric sums of heats of formation. This is the specific failure mode emphasized in Reactive Material Balances, Combustion, and Heats of Reaction.

13. For **Heat of Reaction Away from the Reference Temperature**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. If reaction temperature differs from the reference state, the Handbook corrects \(\Delta H_r\) using the difference between product and reactant heat capacities. This is the specific failure mode emphasized in Reactive Material Balances, Combustion, and Heats of Reaction.

14. For **Reactive Energy Balances and Adiabatic Temperature**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A reactive process energy balance combines material stoichiometry with sensible enthalpies and reaction enthalpy. This is the specific failure mode emphasized in Reactive Material Balances, Combustion, and Heats of Reaction.

15. In **Reactive Material Balances, Combustion, and Heats of Reaction**, close the material balance first because stream amounts and compositions feed the later energy calculation. Otherwise enthalpy and duty terms may be evaluated for unresolved streams.

16. For **Reactive Material Balances, Combustion, and Heats of Reaction**, a degrees-of-freedom check counts unknowns against independent equations before solving. Zero indicates a closed problem; a positive count signals missing independent information.

17. In **Reactive Material Balances, Combustion, and Heats of Reaction**, a relation supplied by the FE problem defines the intended model for that question. A remembered correlation can carry different assumptions, coefficients, validity limits, or reference states.

18. For **Reactive Material Balances, Combustion, and Heats of Reaction**, separating Handbook-supported material from specification-required learned material distinguishes lookup knowledge from material the guide develops. That boundary prevents guide-developed content from being presented as Handbook text.

19. **A.** For **Stoichiometric Coefficients, Extent, Conversion, Yield, and Selectivity**, the relation is meaningful only with the correct basis and physical assumptions. For reaction calculations, use signed stoichiometric coefficients \(\nu_i\): negative for reactants and positive for products. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

20. **A.** For **Reactive Species Balances**, the relation is meaningful only with the correct basis and physical assumptions. A reactive balance can be written using extent or explicit generation terms. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

21. **A.** For **Limiting and Excess Reactants**, the relation is meaningful only with the correct basis and physical assumptions. The limiting reactant is consumed first if the reaction proceeds to completion. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

22. **A.** For **Combustion, Theoretical Air, and Excess Air**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook states that dry air may be modeled as 3.76 mol nitrogen per mol oxygen for combustion calculations. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

23. **A.** For **Standard Heats of Formation and Heat of Reaction**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook evaluates standard heat of reaction from stoichiometric sums of heats of formation. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

24. **A.** For **Heat of Reaction Away from the Reference Temperature**, the relation is meaningful only with the correct basis and physical assumptions. If reaction temperature differs from the reference state, the Handbook corrects \(\Delta H_r\) using the difference between product and reactant heat capacities. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

25. **A.** For **Reactive Energy Balances and Adiabatic Temperature**, the relation is meaningful only with the correct basis and physical assumptions. A reactive process energy balance combines material stoichiometry with sensible enthalpies and reaction enthalpy. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

26. **A.** This later check revisits **Stoichiometric Coefficients, Extent, Conversion, Yield, and Selectivity** from a different review position. For reaction calculations, use signed stoichiometric coefficients \(\nu_i\): negative for reactants and positive for products. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.

27. **A.** This later check revisits **Reactive Species Balances** from a different review position. A reactive balance can be written using extent or explicit generation terms. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.


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

1. For the practice case involving **feed mol extent mol outlet no enters**, Using =3, A=7 mol; B=6 mol. This completes Practice Problem 1 in Reactive Material Balances, Combustion, and Heats of Reaction. The original s basis is preserved.

2. For the practice case involving **mol enters mol remains conversion**, Using 100, 25, 75%. This completes Practice Problem 2 in Reactive Material Balances, Combustion, and Heats of Reaction. The original mol/h, s basis is preserved.

3. For the practice case involving **Reaction Feed mol mol Identify limiting reactant**, Using 2, 10, 8, A requires 5 mol B, so A is limiting. This completes Practice Problem 3 in Reactive Material Balances, Combustion, and Heats of Reaction.

4. For the practice case involving **Methane burns excess air Stoichiometric mol mol**, Using 20%, 2, 2, 2.4 mol O2/mol CH4; air also carries 2.4×3.76=9.024 mol N2. This completes Practice Problem 4 in Reactive Material Balances, Combustion, and Heats of Reaction. The original s, h basis is preserved.

5. For the practice case involving **reaction Hf kJ mol reaction heat reaction**, Using =-100, -100 kJ/mol reaction (exothermic). This completes Practice Problem 5 in Reactive Material Balances, Combustion, and Heats of Reaction. The original kJ/mol, h basis is preserved.

6. For the practice case involving **Cp mol Hr kJ mol Estimate Hr**, Using Cp=20, =-100, -100+0.020×100=-98 kJ/mol. This completes Practice Problem 6 in Reactive Material Balances, Combustion, and Heats of Reaction. The original kJ/mol, J/(mol·K) basis is preserved.

7. For the practice case involving **must be solved before adiabatic flame reactor**, Reaction extent/composition and a reactive energy balance. This is the chapter-specific distinction required by Practice Problem 7 in Reactive Material Balances, Combustion, and Heats of Reaction.

8. For the practice case involving **mol mol form selectivity**, Using 80, 20, 4. This completes Practice Problem 8 in Reactive Material Balances, Combustion, and Heats of Reaction. The original s basis is preserved.

9. For the practice case involving **Stoichiometric air fuel mass ratio actual percent**, Using 17.2, 20.64, (20.64-17.2)/17.2×100=20%. This completes Practice Problem 9 in Reactive Material Balances, Combustion, and Heats of Reaction. The original s, h basis is preserved.

10. For the practice case involving **fuel releases kJ mol mol reacts adiabatically**, Using 800, 0.5, 400 kW. This completes Practice Problem 10 in Reactive Material Balances, Combustion, and Heats of Reaction. The original kJ/mol, s basis is preserved.


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
