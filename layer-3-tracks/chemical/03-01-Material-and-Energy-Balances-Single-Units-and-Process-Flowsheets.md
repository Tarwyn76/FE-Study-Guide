---
chapter: "03-01"
title: "Material and Energy Balances — Single Units and Process Flowsheets"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-001-01, CHE-3-001-02, CHE-3-001-03, CHE-3-001-04, CHE-3-001-05, CHE-3-001-06, CHE-3-001-07]
routes: [chemical]
status: drafted
---

# Chapter 03-01: Material and Energy Balances — Single Units and Process Flowsheets

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 02-12 Chemical Quantities, Stoichiometry, and Reaction Balancing · 02-43 Continuity and Flow Kinematics · 02-51 First Law — Control Volumes

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The FE Chemical specification explicitly requires steady-state mass and energy balances. The Handbook supplies the control-volume energy equation but does not provide a comparable general chemical-process material-balance tutorial; process-basis, degrees-of-freedom, and flowsheet workflows below are guide-developed to meet the specification.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **1.1** Explain and apply **Process Streams, Basis, and Composition**.
* **1.2** Explain and apply **Steady-State Total and Component Material Balances**.
* **1.3** Explain and apply **Degrees of Freedom and Independent Equations**.
* **1.4** Explain and apply **Mixers, Splitters, and Separators**.
* **1.5** Explain and apply **Process Flowsheets and Boundary Selection**.
* **1.6** Explain and apply **Steady Nonreactive Energy Balances**.
* **1.7** Explain and apply **Coupled Material-and-Energy Balance Workflow**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 1.1 Process Streams, Basis, and Composition

A process balance starts by defining a **basis**: a convenient amount or time interval on which every flow and composition is expressed. Typical bases are 100 mol feed, 1 h of operation, or 1 kg product.

For a stream with total molar flow \(\dot n\) and mole fractions \(y_i\), component flow is \(\dot n_i=y_i\dot n\). Mass fractions use the same structure on a mass basis. Fractions in a stream must sum to one.

\[\dot n_i=y_i\dot n,\qquad \sum_i y_i=1\]

![FIG-03-01-001: Process stream arrow labeled total flow, component fractions, temperature, pressure, and chosen calculation basis.](../figures/FIG-03-01-001-process-streams-basis-and-composition.png)

### Worked Example 1

**Problem.** A feed is 100 kmol/h containing 30 mol% A and 70 mol% B. Find component molar flows.

**Solution.** For **Process Streams, Basis, and Composition**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 100, 30, 70, A=30 kmol/h; B=70 kmol/h. This is the section-specific result for feed kmol containing mol mol component molar. The stated units/basis (kmol/h, mol/h) are retained.

---

## 1.2 Steady-State Total and Component Material Balances

For a nonreacting steady process unit, there is no accumulation. Total material entering equals total material leaving, and each conserved chemical species can be balanced separately.

A component balance is often more useful than the total balance because it connects compositions to flow rates.

\[\sum \dot m_{\rm in}=\sum \dot m_{\rm out},\qquad \sum \dot n_{i,\rm in}=\sum \dot n_{i,\rm out}\]

![FIG-03-01-002: Mixer-separator control volume with total and component flow arrows and steady-state accumulation equal to zero.](../figures/FIG-03-01-002-steady-state-total-and-component-material-balances.png)

### Worked Example 2

**Problem.** A steady nonreacting unit receives 120 kg/h and discharges one product at 75 kg/h. Find the second product flow.

**Solution.** For **Steady-State Total and Component Material Balances**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 120, 75, 45 kg/h. This is the section-specific result for steady nonreacting unit receives kg discharges one. The stated units/basis (kg/h, s) are retained.

---

## 1.3 Degrees of Freedom and Independent Equations

Before solving, count unknowns and independent equations. A well-posed calculation has enough independent material balances, specifications, equilibrium relations, and property relations to determine the unknowns.

Writing more equations does not help if they are algebraically dependent. For an \(N\)-component nonreacting system, the total balance is the sum of all component balances, so only \(N\) of those \(N+1\) equations are independent.

\[\text{DOF}=(\text{unknowns})-(\text{independent equations})\]

![FIG-03-01-003: Table counting process unknowns, independent component balances, specifications, and resulting degrees of freedom.](../figures/FIG-03-01-003-degrees-of-freedom-and-independent-equations.png)

### Worked Example 3

**Problem.** A binary separator has unknown feed F, product P, waste W, and two independent composition specifications. If F is known, how many independent material-balance equations are available?

**Solution.** For **Degrees of Freedom and Independent Equations**, Two independent equations may be chosen: one total plus one component balance, or two component balances. This follows because a well-posed calculation has enough independent material balances, specifications, equilibrium relations, and property relations to determine the unknowns.. That physical distinction controls the result for binary separator has unknown feed product waste.

---

## 1.4 Mixers, Splitters, and Separators

A mixer combines streams and is usually solved with total and component balances. An ideal splitter divides one stream into two or more outlets of identical composition. A separator produces outlets of different composition and therefore requires separation specifications in addition to balances.

Do not assign independent compositions to an ideal splitter; its outlet compositions equal the feed composition.

\[\dot n_{\rm feed}=\sum_j\dot n_j,\qquad y_{i,j}=y_{i,\rm feed}\ \text{for an ideal splitter}\]

![FIG-03-01-004: Mixer, ideal splitter, and separator side by side with composition constraints highlighted.](../figures/FIG-03-01-004-mixers-splitters-and-separators.png)

### Worked Example 4

**Problem.** A 100 kg/h stream is ideally split 40/60. Feed is 20 wt% solute. Find solute flow in each outlet.

**Solution.** For **Mixers, Splitters, and Separators**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 100, 40, 60, 8 kg/h and 12 kg/h solute. This is the section-specific result for kg stream ideally split Feed wt solute. The stated units/basis (kg/h, s) are retained.

---

## 1.5 Process Flowsheets and Boundary Selection

A flowsheet is an accounting map. Label every known flow, composition, state, recycle, utility, and product before writing equations. Then choose a boundary that eliminates internal streams whenever possible.

For multiple units, an overall plant balance can determine external streams even when internal streams are unknown. Unit-by-unit balances are then used only where the internal information is actually needed.

\[\text{choose boundary}\rightarrow\text{label streams}\rightarrow\text{count DOF}\rightarrow\text{write independent balances}\]

![FIG-03-01-005: Two-unit process flowsheet with an overall boundary and a smaller unit boundary showing which internal streams cancel.](../figures/FIG-03-01-005-process-flowsheets-and-boundary-selection.png)

### Worked Example 5

**Problem.** A two-unit process has an unknown internal stream but all external flows except one are known. Which balance should be attempted first?

**Solution.** For **Process Flowsheets and Boundary Selection**, An overall process balance, because the internal stream cancels. This follows because label every known flow, composition, state, recycle, utility, and product before writing equations.. That physical distinction controls the result for two-unit process has unknown internal stream but.

---

## 1.6 Steady Nonreactive Energy Balances

The Handbook's steady-flow first law provides the energy-balance backbone. For many chemical process units, kinetic and potential terms are negligible, leaving enthalpy flow, heat transfer, and shaft work.

Use a single enthalpy reference consistently. If all inlet and outlet enthalpies use the same reference, only enthalpy differences matter.

\[\dot Q-\dot W_s=\sum_{\rm out}\dot n_i\hat H_i-\sum_{\rm in}\dot n_i\hat H_i\quad\text{when KE/PE are negligible}\]

![FIG-03-01-006: Steady process unit with feed/product enthalpy flows, heat transfer, and shaft work.](../figures/FIG-03-01-006-steady-nonreactive-energy-balances.png)

### Worked Example 6

**Problem.** A heater raises 2 kg/s of liquid with cp=4 kJ/(kg·K) by 20 K with no shaft work. Find heat duty.

**Solution.** For **Steady Nonreactive Energy Balances**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) cp=4, Q=2×4×20=160 kW. This is the section-specific result for heater raises kg liquid cp kJ kg. The stated units/basis (kg/s, kJ/(kg·K)) are retained.

---

## 1.7 Coupled Material-and-Energy Balance Workflow

Many FE problems require a material balance first and an energy balance second. The material balance determines stream amounts and compositions; the energy balance then determines heat duty, outlet temperature, or utility requirement.

Keep the two accounting systems separate until the needed flow rates are known. A common error is inserting total feed flow into an enthalpy expression that should use only one component or phase.

\[\text{material balance}\Rightarrow\{\dot n_i\}\Rightarrow\text{property evaluation}\Rightarrow\text{energy balance}\]

![FIG-03-01-007: Workflow from basis and material balance to properties and final process energy balance.](../figures/FIG-03-01-007-coupled-material-and-energy-balance-workflow.png)

### Worked Example 7

**Problem.** Why is it usually efficient to solve the material balance before the energy balance?

**Solution.** For **Coupled Material-and-Energy Balance Workflow**, It determines the stream amounts/compositions needed for enthalpy and heat-duty calculations. This follows because many FE problems require a material balance first and an energy balance second.. That physical distinction controls the result for it usually efficient solve material balance before.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A mixture of 40 kmol/h A and 60 kmol/h B is reported as 20 mol% A. Identify the inconsistency.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 40, 60, 20, 40/(40+60)=40 mol% A, not 20%. This is the section-specific result for mixture kmol kmol reported as mol Identify. The stated units/basis (kmol/h, mol/h) are retained.

### Worked Example 9

**Problem.** A cooler removes 500 kW from 10 kg/s of liquid, cp=2.5 kJ/(kg·K). Estimate temperature drop.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) cp=2.5, ΔT=500/(10×2.5)=20 K. This is the section-specific result for cooler removes kW from kg liquid cp. The stated units/basis (kg/s, kJ/(kg·K)) are retained.

---

## As the Handbook States It

Primary source basis: **FE Chemical specification, Area 8; general Thermodynamics steady-flow energy balance, printed pp. 147–149**.

**Source boundary:** The FE Chemical specification explicitly requires steady-state mass and energy balances. The Handbook supplies the control-volume energy equation but does not provide a comparable general chemical-process material-balance tutorial; process-basis, degrees-of-freedom, and flowsheet workflows below are guide-developed to meet the specification.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using process basis and stream composition without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using steady material balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using process degrees of freedom without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using mixing splitting and separation without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using process flowsheet balance strategy without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using chemical-process energy balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using coupled process balances without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| process basis and stream composition | Concept developed in §1.1; apply with the section's stated basis and assumptions. |
| steady material balance | Concept developed in §1.2; apply with the section's stated basis and assumptions. |
| process degrees of freedom | Concept developed in §1.3; apply with the section's stated basis and assumptions. |
| mixing splitting and separation | Concept developed in §1.4; apply with the section's stated basis and assumptions. |
| process flowsheet balance strategy | Concept developed in §1.5; apply with the section's stated basis and assumptions. |
| chemical-process energy balance | Concept developed in §1.6; apply with the section's stated basis and assumptions. |
| coupled process balances | Concept developed in §1.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **process basis and stream composition** and state the governing relation or balance.

2. Define **steady material balance** and state the governing relation or balance.

3. Define **process degrees of freedom** and state the governing relation or balance.

4. Define **mixing splitting and separation** and state the governing relation or balance.

5. Define **process flowsheet balance strategy** and state the governing relation or balance.

6. Define **chemical-process energy balance** and state the governing relation or balance.

7. Define **coupled process balances** and state the governing relation or balance.

8. What is the most likely error if **process basis and stream composition** is applied before the process basis and boundary are defined?

9. What is the most likely error if **steady material balance** is applied before the process basis and boundary are defined?

10. What is the most likely error if **process degrees of freedom** is applied before the process basis and boundary are defined?

11. What is the most likely error if **mixing splitting and separation** is applied before the process basis and boundary are defined?

12. What is the most likely error if **process flowsheet balance strategy** is applied before the process basis and boundary are defined?

13. What is the most likely error if **chemical-process energy balance** is applied before the process basis and boundary are defined?

14. What is the most likely error if **coupled process balances** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **process basis and stream composition**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **steady material balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **process degrees of freedom**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **mixing splitting and separation**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **process flowsheet balance strategy**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **chemical-process energy balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **coupled process balances**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **process basis and stream composition**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **steady material balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **Process Streams, Basis, and Composition.** A process balance starts by defining a **basis**: a convenient amount or time interval on which every flow and composition is expressed. In Material and Energy Balances — Single Units and Process Flowsheets, this is the definition or balance being tested by Question 1.

2. **Steady-State Total and Component Material Balances.** For a nonreacting steady process unit, there is no accumulation. In Material and Energy Balances — Single Units and Process Flowsheets, this is the definition or balance being tested by Question 2.

3. **Degrees of Freedom and Independent Equations.** A well-posed calculation has enough independent material balances, specifications, equilibrium relations, and property relations to determine the unknowns. In Material and Energy Balances — Single Units and Process Flowsheets, this is the definition or balance being tested by Question 3.

4. **Mixers, Splitters, and Separators.** A mixer combines streams and is usually solved with total and component balances. In Material and Energy Balances — Single Units and Process Flowsheets, this is the definition or balance being tested by Question 4.

5. **Process Flowsheets and Boundary Selection.** Label every known flow, composition, state, recycle, utility, and product before writing equations. In Material and Energy Balances — Single Units and Process Flowsheets, this is the definition or balance being tested by Question 5.

6. **Steady Nonreactive Energy Balances.** The Handbook's steady-flow first law provides the energy-balance backbone. In Material and Energy Balances — Single Units and Process Flowsheets, this is the definition or balance being tested by Question 6.

7. **Coupled Material-and-Energy Balance Workflow.** Many FE problems require a material balance first and an energy balance second. In Material and Energy Balances — Single Units and Process Flowsheets, this is the definition or balance being tested by Question 7.

8. For **Process Streams, Basis, and Composition**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A process balance starts by defining a **basis**: a convenient amount or time interval on which every flow and composition is expressed. This is the specific failure mode emphasized in Material and Energy Balances — Single Units and Process Flowsheets.

9. For **Steady-State Total and Component Material Balances**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For a nonreacting steady process unit, there is no accumulation. This is the specific failure mode emphasized in Material and Energy Balances — Single Units and Process Flowsheets.

10. For **Degrees of Freedom and Independent Equations**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A well-posed calculation has enough independent material balances, specifications, equilibrium relations, and property relations to determine the unknowns. This is the specific failure mode emphasized in Material and Energy Balances — Single Units and Process Flowsheets.

11. For **Mixers, Splitters, and Separators**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A mixer combines streams and is usually solved with total and component balances. This is the specific failure mode emphasized in Material and Energy Balances — Single Units and Process Flowsheets.

12. For **Process Flowsheets and Boundary Selection**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Label every known flow, composition, state, recycle, utility, and product before writing equations. This is the specific failure mode emphasized in Material and Energy Balances — Single Units and Process Flowsheets.

13. For **Steady Nonreactive Energy Balances**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook's steady-flow first law provides the energy-balance backbone. This is the specific failure mode emphasized in Material and Energy Balances — Single Units and Process Flowsheets.

14. For **Coupled Material-and-Energy Balance Workflow**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Many FE problems require a material balance first and an energy balance second. This is the specific failure mode emphasized in Material and Energy Balances — Single Units and Process Flowsheets.

15. In **Material and Energy Balances — Single Units and Process Flowsheets**, close the material balance first because stream amounts and compositions feed the later energy calculation. Otherwise enthalpy and duty terms may be evaluated for unresolved streams.

16. For **Material and Energy Balances — Single Units and Process Flowsheets**, a degrees-of-freedom check counts unknowns against independent equations before solving. Zero indicates a closed problem; a positive count signals missing independent information.

17. In **Material and Energy Balances — Single Units and Process Flowsheets**, a relation supplied by the FE problem defines the intended model for that question. A remembered correlation can carry different assumptions, coefficients, validity limits, or reference states.

18. For **Material and Energy Balances — Single Units and Process Flowsheets**, separating Handbook-supported material from specification-required learned material distinguishes lookup knowledge from material the guide develops. That boundary prevents guide-developed content from being presented as Handbook text.

19. **A.** For **Process Streams, Basis, and Composition**, the relation is meaningful only with the correct basis and physical assumptions. A process balance starts by defining a **basis**: a convenient amount or time interval on which every flow and composition is expressed. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

20. **A.** For **Steady-State Total and Component Material Balances**, the relation is meaningful only with the correct basis and physical assumptions. For a nonreacting steady process unit, there is no accumulation. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

21. **A.** For **Degrees of Freedom and Independent Equations**, the relation is meaningful only with the correct basis and physical assumptions. A well-posed calculation has enough independent material balances, specifications, equilibrium relations, and property relations to determine the unknowns. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

22. **A.** For **Mixers, Splitters, and Separators**, the relation is meaningful only with the correct basis and physical assumptions. A mixer combines streams and is usually solved with total and component balances. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

23. **A.** For **Process Flowsheets and Boundary Selection**, the relation is meaningful only with the correct basis and physical assumptions. Label every known flow, composition, state, recycle, utility, and product before writing equations. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

24. **A.** For **Steady Nonreactive Energy Balances**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook's steady-flow first law provides the energy-balance backbone. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

25. **A.** For **Coupled Material-and-Energy Balance Workflow**, the relation is meaningful only with the correct basis and physical assumptions. Many FE problems require a material balance first and an energy balance second. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

26. **A.** This later check revisits **Process Streams, Basis, and Composition** from a different review position. A process balance starts by defining a **basis**: a convenient amount or time interval on which every flow and composition is expressed. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.

27. **A.** This later check revisits **Steady-State Total and Component Material Balances** from a different review position. For a nonreacting steady process unit, there is no accumulation. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.


---

## Practice Problems

1. A feed is 100 kmol/h containing 30 mol% A and 70 mol% B. Find component molar flows.

2. A steady nonreacting unit receives 120 kg/h and discharges one product at 75 kg/h. Find the second product flow.

3. A binary separator has unknown feed F, product P, waste W, and two independent composition specifications. If F is known, how many independent material-balance equations are available?

4. A 100 kg/h stream is ideally split 40/60. Feed is 20 wt% solute. Find solute flow in each outlet.

5. A two-unit process has an unknown internal stream but all external flows except one are known. Which balance should be attempted first?

6. A heater raises 2 kg/s of liquid with cp=4 kJ/(kg·K) by 20 K with no shaft work. Find heat duty.

7. Why is it usually efficient to solve the material balance before the energy balance?

8. A mixture of 40 kmol/h A and 60 kmol/h B is reported as 20 mol% A. Identify the inconsistency.

9. A cooler removes 500 kW from 10 kg/s of liquid, cp=2.5 kJ/(kg·K). Estimate temperature drop.

10. A unit receives 50 kg/h solute and 150 kg/h solvent. Product contains all solute at 25 wt%. Find product flow and solvent removed.


---

## Practice Problem Solutions

1. For the practice case involving **feed kmol containing mol mol component molar**, Using 100, 30, 70, A=30 kmol/h; B=70 kmol/h. This completes Practice Problem 1 in Material and Energy Balances — Single Units and Process Flowsheets. The original kmol/h, mol/h basis is preserved.

2. For the practice case involving **steady nonreacting unit receives kg discharges one**, Using 120, 75, 45 kg/h. This completes Practice Problem 2 in Material and Energy Balances — Single Units and Process Flowsheets. The original kg/h, s basis is preserved.

3. For the practice case involving **binary separator has unknown feed product waste**, Two independent equations may be chosen: one total plus one component balance, or two component balances. This is the chapter-specific distinction required by Practice Problem 3 in Material and Energy Balances — Single Units and Process Flowsheets.

4. For the practice case involving **kg stream ideally split Feed wt solute**, Using 100, 40, 60, 8 kg/h and 12 kg/h solute. This completes Practice Problem 4 in Material and Energy Balances — Single Units and Process Flowsheets. The original kg/h, s basis is preserved.

5. For the practice case involving **two-unit process has unknown internal stream but**, An overall process balance, because the internal stream cancels. This is the chapter-specific distinction required by Practice Problem 5 in Material and Energy Balances — Single Units and Process Flowsheets.

6. For the practice case involving **heater raises kg liquid cp kJ kg**, Using cp=4, Q=2×4×20=160 kW. This completes Practice Problem 6 in Material and Energy Balances — Single Units and Process Flowsheets. The original kg/s, kJ/(kg·K) basis is preserved.

7. For the practice case involving **it usually efficient solve material balance before**, It determines the stream amounts/compositions needed for enthalpy and heat-duty calculations. This is the chapter-specific distinction required by Practice Problem 7 in Material and Energy Balances — Single Units and Process Flowsheets.

8. For the practice case involving **mixture kmol kmol reported as mol Identify**, Using 40, 60, 20, 40/(40+60)=40 mol% A, not 20%. This completes Practice Problem 8 in Material and Energy Balances — Single Units and Process Flowsheets. The original kmol/h, mol/h basis is preserved.

9. For the practice case involving **cooler removes kW from kg liquid cp**, Using cp=2.5, ΔT=500/(10×2.5)=20 K. This completes Practice Problem 9 in Material and Energy Balances — Single Units and Process Flowsheets. The original kg/s, kJ/(kg·K) basis is preserved.

10. For the practice case involving **unit receives kg solute kg solvent Product**, Using 50, 150, 25, Product=50/0.25=200 kg/h; solvent removed=0 kg/h. This completes Practice Problem 10 in Material and Energy Balances — Single Units and Process Flowsheets. The original kg/h, s basis is preserved.


---

## Quick Reference

**Source anchor:** FE Chemical specification, Area 8; general Thermodynamics steady-flow energy balance, printed pp. 147–149.

- **process basis and stream composition:** Process Streams, Basis, and Composition
- **steady material balance:** Steady-State Total and Component Material Balances
- **process degrees of freedom:** Degrees of Freedom and Independent Equations
- **mixing splitting and separation:** Mixers, Splitters, and Separators
- **process flowsheet balance strategy:** Process Flowsheets and Boundary Selection
- **chemical-process energy balance:** Steady Nonreactive Energy Balances
- **coupled process balances:** Coupled Material-and-Energy Balance Workflow
---

## What's Next

**03-02 — Recycle, Bypass, Purge, and Unsteady Material Balances**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor
