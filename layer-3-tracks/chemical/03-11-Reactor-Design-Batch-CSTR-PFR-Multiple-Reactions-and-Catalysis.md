---
chapter: "03-11"
title: "Reactor Design — Batch, CSTR, PFR, Multiple Reactions, and Catalysis"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-011-01, CHE-3-011-02, CHE-3-011-03, CHE-3-011-04, CHE-3-011-05, CHE-3-011-06, CHE-3-011-07]
routes: [chemical]
status: drafted
---

# Chapter 03-11: Reactor Design — Batch, CSTR, PFR, Multiple Reactions, and Catalysis

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 03-10 Reaction Kinetics · 03-03 Reactive Material Balances

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly provides batch-reactor integration, variable-volume relations, PFR and CSTR design equations, space time/space velocity, CSTRs in series, multiple-reaction yield/selectivity, and catalytic/enzyme kinetic examples.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **11.1** Explain and apply **Constant-Volume Batch Reactor Design**.
* **11.2** Explain and apply **Variable-Volume Batch Reactors**.
* **11.3** Explain and apply **Plug-Flow Reactor Design**.
* **11.4** Explain and apply **CSTR Design**.
* **11.5** Explain and apply **CSTRs in Series**.
* **11.6** Explain and apply **Multiple Reactions, Yield, and Reactor Choice**.
* **11.7** Explain and apply **Catalysis and Biocatalysis in Reactor Design**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 11.1 Constant-Volume Batch Reactor Design

A well-mixed batch reactor has no flow during the reaction step. For constant volume, the design equation integrates concentration or conversion over the kinetic rate.

Batch time increases sharply when the rate becomes small near the target conversion.

\[t=C_{A0}\int_0^{X_A}\frac{dX_A}{-r_A}\]

![FIG-03-11-001: Batch vessel with time trajectory from initial concentration to target conversion and integral design equation.](../figures/FIG-03-11-001-constant-volume-batch-reactor-design.png)

### Worked Example 1

**Problem.** First-order batch k=0.1 min^-1. Time for 90% conversion?

**Solution.** t=-ln(0.1)/0.1=23.03 min.

---

<!-- VERIFY id="WE-03-11-001-time" expr="-ln(0.1)/0.1" expected="23.03" units="min" atol="0.005" rtol="1e-9" -->

## 11.2 Variable-Volume Batch Reactors

Gas-phase or constant-pressure batch systems may change volume with conversion. The Handbook gives a volume-expansion relation and the resulting concentration correction.

Do not insert \(C_A=C_{A0}(1-X_A)\) when volume changes significantly.

\[V=V_0(1+\varepsilon_A X_A),\qquad C_A=C_{A0}\frac{1-X_A}{1+\varepsilon_A X_A}\]

![FIG-03-11-002: Piston/gas batch reactor expanding with conversion and concentration corrected for changing volume.](../figures/FIG-03-11-002-variable-volume-batch-reactors.png)

### Worked Example 2

**Problem.** If ε=0.5 and X=0.8, find V/V0.

**Solution.** 1+0.5×0.8=1.4.

---

<!-- VERIFY id="WE-03-11-002-Vratio" expr="1+0.5*0.8" expected="1.4" units="dimensionless" atol="1e-9" rtol="1e-9" -->

## 11.3 Plug-Flow Reactor Design

In an ideal PFR, composition changes continuously with axial position and there is no axial mixing. The Handbook gives reactor volume from an integral over conversion.

Rate is evaluated at the local composition corresponding to each conversion.

\[V_{PFR}=F_{A0}\int_0^{X_A}\frac{dX_A}{-r_A}\]

![FIG-03-11-003: Tubular reactor with conversion increasing along length and Levenspiel-style area interpretation.](../figures/FIG-03-11-003-plug-flow-reactor-design.png)

### Worked Example 3

**Problem.** PFR with FA0=10 mol/s and constant -rA=2 mol/(m³·s), target X=0.6. Find V.

**Solution.** V=FA0 X/r=3 m³.

---

<!-- VERIFY id="WE-03-11-003-V" expr="10*0.6/2" expected="3" units="m3" atol="1e-9" rtol="1e-9" -->

## 11.4 CSTR Design

An ideal CSTR is perfectly mixed, so the reactor contents and outlet have the same composition. The Handbook therefore evaluates the reaction rate at outlet conditions.

For positive-order kinetics, a CSTR generally needs more volume than a PFR for the same feed and conversion because the entire tank operates at the lower outlet reactant concentration.

\[V_{CSTR}=\frac{F_{A0}X_A}{(-r_A)_{\rm exit}}\]

![FIG-03-11-004: Well-mixed CSTR with feed, uniform reactor/outlet concentration, and rectangle area on a 1/r versus X plot.](../figures/FIG-03-11-004-cstr-design.png)

### Worked Example 4

**Problem.** CSTR same data as Problem 3 with exit rate 2. Find V.

**Solution.** 3 m³.

---

<!-- VERIFY id="WE-03-11-004-V" expr="10*0.6/2" expected="3" units="m3" atol="1e-9" rtol="1e-9" -->

## 11.5 CSTRs in Series

Multiple equal CSTRs in series approach PFR behavior as the number of tanks increases. The Handbook provides a closed form for a first-order reaction.

Each successive tank operates at a lower reactant concentration.

\[\frac{C_{AN}}{C_{A0}}=\left(\frac1{1+k\tau}\right)^N\]

![FIG-03-11-005: One, two, and many equal CSTRs in series with concentration decline and approach toward PFR behavior.](../figures/FIG-03-11-005-cstrs-in-series.png)

### Worked Example 5

**Problem.** First-order CSTRs in series kτ=1, N=2. Find CA2/CA0.

**Solution.** (1/2)^2=0.25.

---

<!-- VERIFY id="WE-03-11-005-ratio" expr="(1/(1+1))**2" expected="0.25" units="dimensionless" atol="1e-9" rtol="1e-9" -->

## 11.6 Multiple Reactions, Yield, and Reactor Choice

For parallel or series networks, the reactor type changes the concentration history and therefore selectivity. A PFR exposes material to a changing concentration; a CSTR exposes all reactor contents to the exit concentration.

When desired and undesired pathways have different orders, reactor selection can influence desired-product yield.

\[\text{reactor choice}\rightarrow C_A(t\text{ or }V)\rightarrow r_D/r_U\rightarrow\text{selectivity}\]

![FIG-03-11-006: Parallel-reaction network compared in PFR and CSTR concentration environments.](../figures/FIG-03-11-006-multiple-reactions-yield-and-reactor-choice.png)

### Worked Example 6

**Problem.** If desired reaction is higher order in A than undesired reaction, which reactor often favors desired path at high A?

**Solution.** A PFR can favor it by exposing feed to high A near inlet; exact result depends on rates.

---

## 11.7 Catalysis and Biocatalysis in Reactor Design

Catalysts change reaction rates without changing the equilibrium condition itself. The FE specification includes homogeneous, heterogeneous, and biological reactions and catalysis.

The Handbook gives Michaelis–Menten behavior as one saturating catalytic example; other catalytic rate forms should be used as supplied by the problem.

\[\text{catalyst changes kinetics, not the thermodynamic equilibrium constant at fixed }T\]

![FIG-03-11-007: Homogeneous catalyst, porous heterogeneous catalyst pellet, and enzyme/biocatalytic reactor concepts.](../figures/FIG-03-11-007-catalysis-and-biocatalysis-in-reactor-design.png)

### Worked Example 7

**Problem.** Does a catalyst change equilibrium constant at fixed temperature?

**Solution.** No; it changes rates of approach to equilibrium.

---

**Why this works.** Choose the reactor-specific mole balance first, then combine it with kinetics, conversion, residence time, and the applicable mixing assumption. In this example, the stated setup (“Problem. Does a catalyst change equilibrium constant at fixed temperature? Solution. No; it changes rates of approach to equilibrium”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## Integrated Worked Examples

### Worked Example 8

**Problem.** First-order CSTR single tank kτ=1. Find conversion.

**Solution.** CA/CA0=1/(1+kτ)=0.5, so X=0.5.

<!-- VERIFY id="WE-03-11-008-ratio" expr="1/(1+1)" expected="0.5" units="dimensionless" atol="1e-9" rtol="1e-9" -->
<!-- VERIFY id="WE-03-11-008-X" expr="1-1/(1+1)" expected="0.5" units="dimensionless" atol="1e-9" rtol="1e-9" -->

### Worked Example 9

**Problem.** First-order PFR kτ=1. Find conversion.

**Solution.** X=1-e^-1=0.632.

---

<!-- VERIFY id="WE-03-11-009-X" expr="1-exp(-1)" expected="0.632" units="dimensionless" atol="0.0002" rtol="1e-9" -->

## As the Handbook States It

Primary source basis: **Chemical Engineering, printed pp. 243–247; FE Chemical specification Area 12C–F**.

**Source boundary:** The Handbook directly provides batch-reactor integration, variable-volume relations, PFR and CSTR design equations, space time/space velocity, CSTRs in series, multiple-reaction yield/selectivity, and catalytic/enzyme kinetic examples.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using batch reactor design without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using variable-volume batch reactor without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using plug-flow reactor without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using CSTR design without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using CSTRs in series without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using reactor selectivity without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using catalytic reactor selection without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| batch reactor design | Concept developed in §11.1; apply with the section's stated basis and assumptions. |
| variable-volume batch reactor | Concept developed in §11.2; apply with the section's stated basis and assumptions. |
| plug-flow reactor | Concept developed in §11.3; apply with the section's stated basis and assumptions. |
| CSTR design | Concept developed in §11.4; apply with the section's stated basis and assumptions. |
| CSTRs in series | Concept developed in §11.5; apply with the section's stated basis and assumptions. |
| reactor selectivity | Concept developed in §11.6; apply with the section's stated basis and assumptions. |
| catalytic reactor selection | Concept developed in §11.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **batch reactor design** and state the governing relation or balance.

2. Define **variable-volume batch reactor** and state the governing relation or balance.

3. Define **plug-flow reactor** and state the governing relation or balance.

4. Define **CSTR design** and state the governing relation or balance.

5. Define **CSTRs in series** and state the governing relation or balance.

6. Define **reactor selectivity** and state the governing relation or balance.

7. Define **catalytic reactor selection** and state the governing relation or balance.

8. What is the most likely error if **batch reactor design** is applied before the process basis and boundary are defined?

9. What is the most likely error if **variable-volume batch reactor** is applied before the process basis and boundary are defined?

10. What is the most likely error if **plug-flow reactor** is applied before the process basis and boundary are defined?

11. What is the most likely error if **CSTR design** is applied before the process basis and boundary are defined?

12. What is the most likely error if **CSTRs in series** is applied before the process basis and boundary are defined?

13. What is the most likely error if **reactor selectivity** is applied before the process basis and boundary are defined?

14. What is the most likely error if **catalytic reactor selection** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **batch reactor design**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **variable-volume batch reactor**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **plug-flow reactor**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **CSTR design**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **CSTRs in series**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **reactor selectivity**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **catalytic reactor selection**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **batch reactor design**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **variable-volume batch reactor**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **batch reactor design** is developed in §11.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **variable-volume batch reactor** is developed in §11.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **plug-flow reactor** is developed in §11.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **CSTR design** is developed in §11.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **CSTRs in series** is developed in §11.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **reactor selectivity** is developed in §11.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **catalytic reactor selection** is developed in §11.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.
8. Applying **batch reactor design** before the process basis and system boundary are fixed can use a CSTR, PFR, or batch design equation under the wrong mixing assumption or pair kinetics with the wrong residence-time definition. In this chapter, reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model. Define the basis, boundary, known streams or states, and independent specifications first; then apply the batch reactor design relation to that defined system.

9. Applying **variable-volume batch reactor** before the process basis and system boundary are fixed can use a CSTR, PFR, or batch design equation under the wrong mixing assumption or pair kinetics with the wrong residence-time definition. In this chapter, reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model. Define the basis, boundary, known streams or states, and independent specifications first; then apply the variable-volume batch reactor relation to that defined system.

10. Applying **plug-flow reactor** before the process basis and system boundary are fixed can use a CSTR, PFR, or batch design equation under the wrong mixing assumption or pair kinetics with the wrong residence-time definition. In this chapter, reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model. Define the basis, boundary, known streams or states, and independent specifications first; then apply the plug-flow reactor relation to that defined system.

11. Applying **CSTR design** before the process basis and system boundary are fixed can use a CSTR, PFR, or batch design equation under the wrong mixing assumption or pair kinetics with the wrong residence-time definition. In this chapter, reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model. Define the basis, boundary, known streams or states, and independent specifications first; then apply the CSTR design relation to that defined system.

12. Applying **CSTRs in series** before the process basis and system boundary are fixed can use a CSTR, PFR, or batch design equation under the wrong mixing assumption or pair kinetics with the wrong residence-time definition. In this chapter, reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model. Define the basis, boundary, known streams or states, and independent specifications first; then apply the CSTRs in series relation to that defined system.

13. Applying **reactor selectivity** before the process basis and system boundary are fixed can use a CSTR, PFR, or batch design equation under the wrong mixing assumption or pair kinetics with the wrong residence-time definition. In this chapter, reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model. Define the basis, boundary, known streams or states, and independent specifications first; then apply the reactor selectivity relation to that defined system.

14. Applying **catalytic reactor selection** before the process basis and system boundary are fixed can use a CSTR, PFR, or batch design equation under the wrong mixing assumption or pair kinetics with the wrong residence-time definition. In this chapter, reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model. Define the basis, boundary, known streams or states, and independent specifications first; then apply the catalytic reactor selection relation to that defined system.

15. Close the material balance first because it establishes the flow rates and compositions that the energy balance must use. For this chapter, reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model; without those material quantities, enthalpy, heat duty, reaction energy, or phase-change terms can be attached to the wrong amount of material.

16. A degrees-of-freedom check compares the number of unknowns with the number of independent balances, constitutive relations, equilibrium or rate equations, and specifications. For 03-11, this prevents algebra from starting before the reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model are sufficiently defined and exposes redundant or missing equations.

17. Use a relation supplied in the FE problem whenever it defines the model or data for that question. That stated relation controls the calculation even if another correlation is familiar; in 03-11, substituting an unstated model can change the assumptions behind the reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model.

18. Separate Handbook-supported material from specification-required or externally supported material so the learner knows what may be looked up and what must be understood independently. In 03-11, the distinction matters because the reactor calculations depend on the reactor-specific mole balance, kinetics, residence time, conversion target, and mixing model can include methods or assumptions that are required by the exam specification but are not fully tabulated in the Handbook.


19. **A.** The relation or workflow for **batch reactor design** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **variable-volume batch reactor** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **plug-flow reactor** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **CSTR design** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **CSTRs in series** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **reactor selectivity** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **catalytic reactor selection** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **batch reactor design** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

27. **A.** The relation or workflow for **variable-volume batch reactor** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. First-order batch k=0.1 min^-1. Time for 90% conversion?

2. If ε=0.5 and X=0.8, find V/V0.

3. PFR with FA0=10 mol/s and constant -rA=2 mol/(m³·s), target X=0.6. Find V.

4. CSTR same data as Problem 3 with exit rate 2. Find V.

5. First-order CSTRs in series kτ=1, N=2. Find CA2/CA0.

6. If desired reaction is higher order in A than undesired reaction, which reactor often favors desired path at high A?

7. Does a catalyst change equilibrium constant at fixed temperature?

8. First-order CSTR single tank kτ=1. Find conversion.

9. First-order PFR kτ=1. Find conversion.

10. Why do multiple CSTRs in series approach PFR performance?


---

## Practice Problem Solutions

1. t=-ln(0.1)/0.1=23.03 min.

2. 1+0.5×0.8=1.4.

3. V=FA0 X/r=3 m³.

   **Explanation.** Choose the reactor-specific mole balance first, then combine it with kinetics, conversion, residence time, and the applicable mixing assumption. The question is framed around “PFR with FA0=10 mol/s and constant -rA=2 mol/(m³·s), target X=0.6. Find V.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

4. 3 m³.

   **Explanation.** Choose the reactor-specific mole balance first, then combine it with kinetics, conversion, residence time, and the applicable mixing assumption. The question is framed around “CSTR same data as Problem 3 with exit rate 2. Find V.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

5. (1/2)^2=0.25.

   **Explanation.** Choose the reactor-specific mole balance first, then combine it with kinetics, conversion, residence time, and the applicable mixing assumption. The question is framed around “First-order CSTRs in series kτ=1, N=2. Find CA2/CA0.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

6. A PFR can favor it by exposing feed to high A near inlet; exact result depends on rates.

7. No; it changes rates of approach to equilibrium.

8. CA/CA0=1/(1+kτ)=0.5, so X=0.5.

9. X=1-e^-1=0.632.

   **Explanation.** Choose the reactor-specific mole balance first, then combine it with kinetics, conversion, residence time, and the applicable mixing assumption. The question is framed around “First-order PFR kτ=1. Find conversion.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

10. Concentration varies stepwise instead of remaining at one low exit concentration throughout.


---

## Quick Reference

**Source anchor:** Chemical Engineering, printed pp. 243–247; FE Chemical specification Area 12C–F.

- **batch reactor design:** Constant-Volume Batch Reactor Design
- **variable-volume batch reactor:** Variable-Volume Batch Reactors
- **plug-flow reactor:** Plug-Flow Reactor Design
- **CSTR design:** CSTR Design
- **CSTRs in series:** CSTRs in Series
- **reactor selectivity:** Multiple Reactions, Yield, and Reactor Choice
- **catalytic reactor selection:** Catalysis and Biocatalysis in Reactor Design
---

## What's Next

**03-12 — Process Flow Diagrams, P&IDs, Equipment Sizing, Scale-Up, and Cost Estimation**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor