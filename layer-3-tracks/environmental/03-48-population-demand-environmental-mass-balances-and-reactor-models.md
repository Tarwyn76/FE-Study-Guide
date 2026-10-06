---
chapter: "03-48"
title: "Population, Demand, Environmental Mass Balances, and Reactor Models"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-048-01, ENV-3-048-02, ENV-3-048-03, ENV-3-048-04, ENV-3-048-05, ENV-3-048-06, ENV-3-048-07]
routes: [environmental]
status: drafted
---

# Chapter 03-48: Population, Demand, Environmental Mass Balances, and Reactor Models

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** FLUID-2D-043-06

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Population, Demand, Environmental Mass Balances, and Reactor Models**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **48.1** Explain and apply **Population projections and demand forecasting**.
* **48.2** Explain and apply **Control volumes, steady and unsteady environmental mass balances**.
* **48.3** Explain and apply **Concentration-flow loading calculations**.
* **48.4** Explain and apply **Reaction order and environmental decay kinetics**.
* **48.5** Explain and apply **Ideal batch and plug-flow reactors**.
* **48.6** Explain and apply **Completely mixed flow reactors**.
* **48.7** Explain and apply **Reactor selection, residence time, and model verification**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 48.1 Population projections and demand forecasting

Environmental facilities are sized from projected population and per-capita or unit demand. Distinguish arithmetic, geometric, and supplied projection methods, and keep the design horizon explicit.

\[P_t=P_0(1+r)^t,\qquad D=P_t\,d_{pc}\]

![FIG-03-48-001: Population versus time with design horizon and corresponding water, wastewater, solid-waste, and energy demand projections.](../figures/FIG-03-48-001-population-projections-and-demand-forecasting.png)

### Worked Example 1

**Problem.** A population of 50,000 growing at 1.5%/yr for 20 years becomes about 67,300 under geometric growth.

**Solution.** Apply the relation and environmental model in §48.1; then verify units, boundary conditions, and physical limits.

---

## 48.2 Control volumes, steady and unsteady environmental mass balances

Mass balances are the foundation of fate, treatment, and reactor calculations. Define the control volume, constituent, reaction sign convention, and whether accumulation is zero before solving.

\[\frac{dM}{dt}=\sum \dot M_{in}-\sum \dot M_{out}+rV\]

![FIG-03-48-002: Environmental control volume with flow, concentration, reaction, and accumulation terms.](../figures/FIG-03-48-002-control-volumes-steady-and-unsteady-environmental-mass-balances.png)

### Worked Example 2

**Problem.** At steady state with no reaction, 100 mg/s entering requires 100 mg/s leaving.

**Solution.** Apply the relation and environmental model in §48.2; then verify units, boundary conditions, and physical limits.

---

## 48.3 Concentration-flow loading calculations

Loading is mass per time, not concentration. Convert flow and concentration to compatible units before multiplying; in U.S. customary wastewater work, the 8.34 factor often appears with MGD and mg/L.

\[\dot m=QC\]

![FIG-03-48-003: Pipe flow labeled Q and C feeding a daily mass-loading calculation in SI and MGD-mg/L forms.](../figures/FIG-03-48-003-concentration-flow-loading-calculations.png)

### Worked Example 3

**Problem.** 2 MGD at 15 mg/L corresponds to about 250 lb/day.

**Solution.** Apply the relation and environmental model in §48.3; then verify units, boundary conditions, and physical limits.

---

## 48.4 Reaction order and environmental decay kinetics

Zero-, first-, and second-order decay have different concentration-time relationships and different units for k. Do not use a first-order exponential unless the process is modeled as first order.

\[r=-kC^n\]

![FIG-03-48-004: Zero-, first-, and second-order concentration decay curves with rate-law forms and k units.](../figures/FIG-03-48-004-reaction-order-and-environmental-decay-kinetics.png)

### Worked Example 4

**Problem.** For first-order decay with k=0.20 day^-1, half-life is ln2/k≈3.47 days.

**Solution.** Apply the relation and environmental model in §48.4; then verify units, boundary conditions, and physical limits.

---

## 48.5 Ideal batch and plug-flow reactors

An ideal batch reactor has no continuous inflow/outflow during reaction; an ideal plug-flow reactor advances material without longitudinal mixing. For first-order decay, batch and PFR residence-time relations have the same exponential form.

\[\theta=\frac{V}{Q}\quad\text{for flowing reactors}\]

![FIG-03-48-005: Batch and plug-flow reactor sketches with concentration profiles and residence-time definitions.](../figures/FIG-03-48-005-ideal-batch-and-plug-flow-reactors.png)

### Worked Example 5

**Problem.** For first-order decay, C/C0=e^{-kθ}.

**Solution.** Apply the relation and environmental model in §48.5; then verify units, boundary conditions, and physical limits.

---

## 48.6 Completely mixed flow reactors

A CMFR/CSTR is perfectly mixed, so reactor concentration equals effluent concentration. Mixing changes first-order performance relative to plug flow at the same residence time.

\[C=\frac{C_0}{1+k\theta}\quad\text{for first-order steady decay}\]

![FIG-03-48-006: Completely mixed reactor with influent C0, effluent C, volume V, flow Q, and internal mixing.](../figures/FIG-03-48-006-completely-mixed-flow-reactors.png)

### Worked Example 6

**Problem.** At kθ=1, a first-order CMFR has C/C0=0.5.

**Solution.** Apply the relation and environmental model in §48.6; then verify units, boundary conditions, and physical limits.

---

## 48.7 Reactor selection, residence time, and model verification

The most important reactor step is choosing the correct idealization. A correct equation used with the wrong mixing model can be more misleading than a rough calculation with the right model.

\[\text{select reactor model from mixing, flow, reaction order, and steady/unsteady assumptions}\]

![FIG-03-48-007: Decision flowchart for batch, plug-flow, and completely mixed environmental reactor models.](../figures/FIG-03-48-007-reactor-selection-residence-time-and-model-verification.png)

### Worked Example 7

**Problem.** A long narrow contact basin with limited axial mixing is often approximated more closely by plug flow than by complete mix.

**Solution.** Apply the relation and environmental model in §48.7; then verify units, boundary conditions, and physical limits.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** The algebra or model assumptions are invalid for that condition. Recheck the balance, reaction/order assumptions, time basis, units, and any zero-concentration limiting condition.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** Use the Handbook relation and its definitions unless the problem explicitly supplies a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 5; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** Some Environmental specification topics are directly tabulated in the Handbook, while others require learned engineering knowledge. The chapter keeps those two categories separate.

---

## Where This Goes Wrong

**Using environmental demand projection without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental mass balance without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using pollutant loading rate without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental reaction kinetics without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using batch and plug-flow environmental reactor without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using complete-mix flow reactor without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental reactor selection without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| environmental demand projection | Concept developed in §48.1; apply with that section's stated environmental basis and assumptions. |
| environmental mass balance | Concept developed in §48.2; apply with that section's stated environmental basis and assumptions. |
| pollutant loading rate | Concept developed in §48.3; apply with that section's stated environmental basis and assumptions. |
| environmental reaction kinetics | Concept developed in §48.4; apply with that section's stated environmental basis and assumptions. |
| batch and plug-flow environmental reactor | Concept developed in §48.5; apply with that section's stated environmental basis and assumptions. |
| complete-mix flow reactor | Concept developed in §48.6; apply with that section's stated environmental basis and assumptions. |
| environmental reactor selection | Concept developed in §48.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **environmental demand projection** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **environmental mass balance** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **pollutant loading rate** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **environmental reaction kinetics** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **batch and plug-flow environmental reactor** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **complete-mix flow reactor** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **environmental reactor selection** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental demand projection**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental mass balance**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **pollutant loading rate**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental reaction kinetics**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **batch and plug-flow environmental reactor**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **complete-mix flow reactor**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental reactor selection**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **environmental demand projection**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **environmental mass balance**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **pollutant loading rate**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **environmental reaction kinetics**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **batch and plug-flow environmental reactor**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **complete-mix flow reactor**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **environmental reactor selection**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **environmental demand projection**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **environmental mass balance**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **environmental demand projection** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **environmental mass balance** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **pollutant loading rate** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **environmental reaction kinetics** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **batch and plug-flow environmental reactor** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **complete-mix flow reactor** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **environmental reactor selection** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **environmental demand projection**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **environmental mass balance**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **pollutant loading rate**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **environmental reaction kinetics**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **batch and plug-flow environmental reactor**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **complete-mix flow reactor**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **environmental reactor selection**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

15. The boundary determines what enters, leaves, accumulates, reacts, or transfers between media. Without it, terms are easily omitted or double counted.

16. Concentration is mass per volume; loading is mass per time. A low concentration at very high flow can still create a large load.

17. The FE Handbook is the supplied exam reference. Its variable definitions and unit conventions should govern unless the problem explicitly provides another relation.

18. A mass/energy balance and physical check can reveal impossible signs, removal above 100%, negative concentrations, unrealistic flows, or model misuse.

19. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

20. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

21. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

22. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

23. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

24. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

25. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

26. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

27. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.


---

## Practice Problems

1. A population of 50,000 growing at 1.5%/yr for 20 years becomes about 67,300 under geometric growth.

2. At steady state with no reaction, 100 mg/s entering requires 100 mg/s leaving.

3. 2 MGD at 15 mg/L corresponds to about 250 lb/day.

4. For first-order decay with k=0.20 day^-1, half-life is ln2/k≈3.47 days.

5. For first-order decay, C/C0=e^{-kθ}.

6. At kθ=1, a first-order CMFR has C/C0=0.5.

7. A long narrow contact basin with limited axial mixing is often approximated more closely by plug flow than by complete mix.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §48.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §48.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §48.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §48.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §48.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §48.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §48.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 5, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 5.

- **environmental demand projection:** Population projections and demand forecasting
- **environmental mass balance:** Control volumes, steady and unsteady environmental mass balances
- **pollutant loading rate:** Concentration-flow loading calculations
- **environmental reaction kinetics:** Reaction order and environmental decay kinetics
- **batch and plug-flow environmental reactor:** Ideal batch and plug-flow reactors
- **complete-mix flow reactor:** Completely mixed flow reactors
- **environmental reactor selection:** Reactor selection, residence time, and model verification

---

## What's Next

**Chapter 03-49: Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
