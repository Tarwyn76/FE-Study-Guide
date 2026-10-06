---
chapter: "03-54"
title: "Groundwater Flow, Aquifer Tests, Wells, and Drawdown"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-054-01, ENV-3-054-02, ENV-3-054-03, ENV-3-054-04, ENV-3-054-05, ENV-3-054-06, ENV-3-054-07]
routes: [environmental]
status: drafted
---

# Chapter 03-54: Groundwater Flow, Aquifer Tests, Wells, and Drawdown

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-020-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Groundwater Flow, Aquifer Tests, Wells, and Drawdown**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **54.1** Explain and apply **Aquifer properties, porosity, and hydraulic conductivity**.
* **54.2** Explain and apply **Darcy law and groundwater velocity**.
* **54.3** Explain and apply **Hydraulic head and gradient**.
* **54.4** Explain and apply **Pumping wells and drawdown**.
* **54.5** Explain and apply **Steady radial-flow well relations**.
* **54.6** Explain and apply **Transient aquifer tests — Theis and Jacob concepts**.
* **54.7** Explain and apply **Specific capacity, interference, and groundwater system checks**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 54.1 Aquifer properties, porosity, and hydraulic conductivity

Groundwater systems are described by porosity, effective porosity, hydraulic conductivity, saturated thickness, transmissivity, and storage properties.

\[n=\frac{V_v}{V},\qquad T=Kb\]

![FIG-03-54-001: Confined and unconfined aquifer sections with porosity, K, b, T, and water-level surfaces.](../figures/FIG-03-54-001-aquifer-properties-porosity-and-hydraulic-conductivity.png)

### Worked Example 1

**Problem.** K=20 m/day and b=15 m gives T=300 m²/day.

**Solution.** Apply the relation and environmental model in §54.1; then verify units, boundary conditions, and physical limits.

---

## 54.2 Darcy law and groundwater velocity

Darcy flux is discharge divided by gross area; seepage or average linear velocity accounts for effective porosity. These are not the same quantity.

\[Q=KiA,\qquad v_s=\frac{Ki}{n_e}\]

![FIG-03-54-002: Porous medium with hydraulic gradient, Darcy flux, effective porosity, and seepage velocity.](../figures/FIG-03-54-002-darcy-law-and-groundwater-velocity.png)

### Worked Example 2

**Problem.** If Ki=0.3 m/day and ne=0.25, seepage velocity is 1.2 m/day.

**Solution.** Apply the relation and environmental model in §54.2; then verify units, boundary conditions, and physical limits.

---

## 54.3 Hydraulic head and gradient

Groundwater flows from higher hydraulic head toward lower hydraulic head. Elevation and pressure head must share a common datum.

\[i=\frac{\Delta h}{L}\]

![FIG-03-54-003: Piezometers across an aquifer with head contours and groundwater-flow direction.](../figures/FIG-03-54-003-hydraulic-head-and-gradient.png)

### Worked Example 3

**Problem.** A 2-m head drop over 100 m gives i=0.02.

**Solution.** Apply the relation and environmental model in §54.3; then verify units, boundary conditions, and physical limits.

---

## 54.4 Pumping wells and drawdown

Pumping creates a cone of depression. Drawdown varies with pumping rate, aquifer properties, time, distance, and boundary conditions.

\[s=h_0-h\]

![FIG-03-54-004: Pumping well and observation wells across a cone of depression.](../figures/FIG-03-54-004-pumping-wells-and-drawdown.png)

### Worked Example 4

**Problem.** Static head 50 m and pumping head 44 m gives drawdown 6 m.

**Solution.** Apply the relation and environmental model in §54.4; then verify units, boundary conditions, and physical limits.

---

## 54.5 Steady radial-flow well relations

Thiem/Dupuit-style steady relations connect pumping rate to head differences and radial distance. Use the confined or unconfined form supplied by the problem.

\[Q\propto \frac{T(h_1-h_2)}{\ln(r_2/r_1)}\]

![FIG-03-54-005: Steady radial head profile to a pumping well with r1, r2, h1, h2, and T.](../figures/FIG-03-54-005-steady-radial-flow-well-relations.png)

### Worked Example 5

**Problem.** Greater transmissivity produces less drawdown for the same pumping rate and geometry.

**Solution.** Apply the relation and environmental model in §54.5; then verify units, boundary conditions, and physical limits.

---

## 54.6 Transient aquifer tests — Theis and Jacob concepts

Transient pumping tests infer transmissivity and storage from drawdown versus time/distance. Theis and Cooper-Jacob methods are specification topics; use the relation supplied when detailed constants are needed.

\[\text{drawdown}=f(Q,T,S,r,t)\]

![FIG-03-54-006: Semilog drawdown versus time plot with pumping well, observation well, and transmissivity/storage interpretation.](../figures/FIG-03-54-006-transient-aquifer-tests-theis-and-jacob-concepts.png)

### Worked Example 6

**Problem.** At a fixed observation point, drawdown generally increases after pumping begins until boundaries or steady conditions alter the trend.

**Solution.** Apply the relation and environmental model in §54.6; then verify units, boundary conditions, and physical limits.

---

## 54.7 Specific capacity, interference, and groundwater system checks

Specific capacity is a practical well-performance measure. Nearby pumping wells can interfere because their cones of depression overlap.

\[\text{specific capacity}=\frac{Q}{s}\]

![FIG-03-54-007: Multiple wells with overlapping cones of depression and specific-capacity labels.](../figures/FIG-03-54-007-specific-capacity-interference-and-groundwater-system-checks.png)

### Worked Example 7

**Problem.** A well pumping 600 gpm with 20 ft drawdown has specific capacity 30 gpm/ft.

**Solution.** Apply the relation and environmental model in §54.7; then verify units, boundary conditions, and physical limits.

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

Primary source basis: **FE Environmental specification Area(s) 11; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** Some Environmental specification topics are directly tabulated in the Handbook, while others require learned engineering knowledge. The chapter keeps those two categories separate.

---

## Where This Goes Wrong

**Using environmental aquifer properties without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental Darcy flow without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using groundwater hydraulic gradient without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental well drawdown without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using steady groundwater well flow without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using transient aquifer test without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using well specific capacity without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| environmental aquifer properties | Concept developed in §54.1; apply with that section's stated environmental basis and assumptions. |
| environmental Darcy flow | Concept developed in §54.2; apply with that section's stated environmental basis and assumptions. |
| groundwater hydraulic gradient | Concept developed in §54.3; apply with that section's stated environmental basis and assumptions. |
| environmental well drawdown | Concept developed in §54.4; apply with that section's stated environmental basis and assumptions. |
| steady groundwater well flow | Concept developed in §54.5; apply with that section's stated environmental basis and assumptions. |
| transient aquifer test | Concept developed in §54.6; apply with that section's stated environmental basis and assumptions. |
| well specific capacity | Concept developed in §54.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **environmental aquifer properties** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **environmental Darcy flow** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **groundwater hydraulic gradient** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **environmental well drawdown** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **steady groundwater well flow** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **transient aquifer test** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **well specific capacity** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental aquifer properties**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental Darcy flow**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **groundwater hydraulic gradient**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental well drawdown**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **steady groundwater well flow**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **transient aquifer test**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **well specific capacity**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **environmental aquifer properties**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **environmental Darcy flow**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **groundwater hydraulic gradient**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **environmental well drawdown**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **steady groundwater well flow**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **transient aquifer test**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **well specific capacity**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **environmental aquifer properties**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **environmental Darcy flow**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **environmental aquifer properties** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **environmental Darcy flow** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **groundwater hydraulic gradient** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **environmental well drawdown** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **steady groundwater well flow** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **transient aquifer test** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **well specific capacity** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **environmental aquifer properties**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **environmental Darcy flow**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **groundwater hydraulic gradient**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **environmental well drawdown**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **steady groundwater well flow**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **transient aquifer test**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **well specific capacity**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

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

1. K=20 m/day and b=15 m gives T=300 m²/day.

2. If Ki=0.3 m/day and ne=0.25, seepage velocity is 1.2 m/day.

3. A 2-m head drop over 100 m gives i=0.02.

4. Static head 50 m and pumping head 44 m gives drawdown 6 m.

5. Greater transmissivity produces less drawdown for the same pumping rate and geometry.

6. At a fixed observation point, drawdown generally increases after pumping begins until boundaries or steady conditions alter the trend.

7. A well pumping 600 gpm with 20 ft drawdown has specific capacity 30 gpm/ft.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §54.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §54.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §54.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §54.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §54.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §54.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §54.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 11, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 11.

- **environmental aquifer properties:** Aquifer properties, porosity, and hydraulic conductivity
- **environmental Darcy flow:** Darcy law and groundwater velocity
- **groundwater hydraulic gradient:** Hydraulic head and gradient
- **environmental well drawdown:** Pumping wells and drawdown
- **steady groundwater well flow:** Steady radial-flow well relations
- **transient aquifer test:** Transient aquifer tests — Theis and Jacob concepts
- **well specific capacity:** Specific capacity, interference, and groundwater system checks

---

## What's Next

**Chapter 03-55: Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
