---
chapter: "03-81"
title: "Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-081-01, MEC-3-081-02, MEC-3-081-03, MEC-3-081-04, MEC-3-081-05, MEC-3-081-06, MEC-3-081-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-81: Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MEC-3-080-07 · THERMO-2D-047-01

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **81.1** Explain and apply **Speed of sound and Mach number**.
* **81.2** Explain and apply **Stagnation and static properties**.
* **81.3** Explain and apply **Area-Mach relation and choking**.
* **81.4** Explain and apply **Mass flow through compressible nozzles**.
* **81.5** Explain and apply **Normal shock relations and entropy rise**.
* **81.6** Explain and apply **Converging-diverging nozzle operating regimes**.
* **81.7** Explain and apply **Compressible-flow model checks**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 81.1 Speed of sound and Mach number

Mach number compares flow speed with acoustic propagation speed and organizes compressible-flow regimes.

\[M=\frac{V}{a},\qquad a=\sqrt{\gamma RT}\]

![FIG-03-81-001: Subsonic, sonic, supersonic, and hypersonic flow regimes with disturbance cones.](../figures/FIG-03-81-001-speed-of-sound-and-mach-number.png)

### Worked Example 1

**Problem.** At V=340 m/s and a=340 m/s, M=1.

**Solution.** Apply the relation and model in §81.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 81.2 Stagnation and static properties

Isentropic flow relations connect static and stagnation temperature, pressure, and density. Stagnation quantities represent reversible deceleration to zero velocity.

\[\frac{T_0}{T}=1+\frac{\gamma-1}{2}M^2\]

![FIG-03-81-002: Flow decelerated isentropically to a stagnation point with static and total properties.](../figures/FIG-03-81-002-stagnation-and-static-properties.png)

### Worked Example 2

**Problem.** At M=0, stagnation and static properties are equal.

**Solution.** Apply the relation and model in §81.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 81.3 Area-Mach relation and choking

For one-dimensional isentropic flow, nozzle area and Mach number are coupled. Once a converging nozzle is choked, lowering downstream pressure cannot increase mass flow indefinitely.

\[M=1\text{ at the minimum-area throat of an ideal choked nozzle}\]

![FIG-03-81-003: Converging-diverging nozzle with throat, subsonic/supersonic branches, and Mach distribution.](../figures/FIG-03-81-003-area-mach-relation-and-choking.png)

### Worked Example 3

**Problem.** At choking, throat Mach number is 1.

**Solution.** Apply the relation and model in §81.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 81.4 Mass flow through compressible nozzles

Continuity still governs compressible flow, but density varies with pressure and temperature. Critical conditions set maximum ideal mass flow for a given stagnation state and throat area.

\[\dot m=\rho AV\]

![FIG-03-81-004: Nozzle mass flow versus downstream-to-upstream pressure ratio showing choking plateau.](../figures/FIG-03-81-004-mass-flow-through-compressible-nozzles.png)

### Worked Example 4

**Problem.** At fixed stagnation conditions and throat area, choked mass flow is insensitive to further downstream-pressure reduction in the ideal model.

**Solution.** Apply the relation and model in §81.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 81.5 Normal shock relations and entropy rise

A normal shock abruptly converts supersonic flow to subsonic flow, raising static pressure and temperature while decreasing stagnation pressure.

\[M_1>1,\quad M_2<1\]

![FIG-03-81-005: Normal shock in a duct with upstream/downstream Mach, pressure, temperature, and total-pressure change.](../figures/FIG-03-81-005-normal-shock-relations-and-entropy-rise.png)

### Worked Example 5

**Problem.** A normal shock cannot be treated as isentropic.

**Solution.** Apply the relation and model in §81.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 81.6 Converging-diverging nozzle operating regimes

A converging-diverging nozzle can exhibit entirely subsonic flow, choking, internal shocks, or supersonic expansion depending on pressure ratio.

\[\text{back pressure controls subsonic, choked, shocked, or fully supersonic states}\]

![FIG-03-81-006: Nozzle pressure profiles for subsonic, choked-with-shock, design, and under/overexpanded operation.](../figures/FIG-03-81-006-converging-diverging-nozzle-operating-regimes.png)

### Worked Example 6

**Problem.** The diverging section acts as a diffuser for subsonic flow but a nozzle for supersonic flow.

**Solution.** Apply the relation and model in §81.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 81.7 Compressible-flow model checks

Before using incompressible formulas, check Mach number and pressure/temperature changes. At sufficiently low Mach number, incompressible approximations may be adequate.

\[\text{compressibility becomes important as density changes are no longer negligible}\]

![FIG-03-81-007: Decision tree for incompressible versus compressible gas-flow modeling.](../figures/FIG-03-81-007-compressible-flow-model-checks.png)

### Worked Example 7

**Problem.** Gas flow through a large pressure ratio requires compressible treatment even if inlet speed is modest.

**Solution.** Apply the relation and model in §81.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

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

Primary source basis: **FE Mechanical specification Area(s) 10; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** The Mechanical specification includes both directly tabulated Handbook equations and learned design concepts. This chapter does not assign invented Handbook pages to specification-required material that is not directly tabulated.

---

## Where This Goes Wrong

**Using Mach number outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using stagnation temperature outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using choked flow outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using compressible nozzle mass flow outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using normal shock outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using de Laval nozzle outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using compressible-flow validity outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| Mach number | Concept developed in §81.1; apply with that section's geometry and operating assumptions. |
| stagnation temperature | Concept developed in §81.2; apply with that section's geometry and operating assumptions. |
| choked flow | Concept developed in §81.3; apply with that section's geometry and operating assumptions. |
| compressible nozzle mass flow | Concept developed in §81.4; apply with that section's geometry and operating assumptions. |
| normal shock | Concept developed in §81.5; apply with that section's geometry and operating assumptions. |
| de Laval nozzle | Concept developed in §81.6; apply with that section's geometry and operating assumptions. |
| compressible-flow validity | Concept developed in §81.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **Mach number** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **stagnation temperature** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **choked flow** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **compressible nozzle mass flow** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **normal shock** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **de Laval nozzle** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **compressible-flow validity** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **Mach number**?

9. What geometric, material, operating, or model assumption must be checked before applying **stagnation temperature**?

10. What geometric, material, operating, or model assumption must be checked before applying **choked flow**?

11. What geometric, material, operating, or model assumption must be checked before applying **compressible nozzle mass flow**?

12. What geometric, material, operating, or model assumption must be checked before applying **normal shock**?

13. What geometric, material, operating, or model assumption must be checked before applying **de Laval nozzle**?

14. What geometric, material, operating, or model assumption must be checked before applying **compressible-flow validity**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **Mach number**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **stagnation temperature**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **choked flow**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **compressible nozzle mass flow**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **normal shock**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **de Laval nozzle**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **compressible-flow validity**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **Mach number**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **stagnation temperature**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **Mach number** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **stagnation temperature** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **choked flow** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **compressible nozzle mass flow** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **normal shock** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **de Laval nozzle** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **compressible-flow validity** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **Mach number**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **stagnation temperature**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **choked flow**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **compressible nozzle mass flow**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **normal shock**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **de Laval nozzle**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **compressible-flow validity**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

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

1. At V=340 m/s and a=340 m/s, M=1.

2. At M=0, stagnation and static properties are equal.

3. At choking, throat Mach number is 1.

4. At fixed stagnation conditions and throat area, choked mass flow is insensitive to further downstream-pressure reduction in the ideal model.

5. A normal shock cannot be treated as isentropic.

6. The diverging section acts as a diffuser for subsonic flow but a nozzle for supersonic flow.

7. Gas flow through a large pressure ratio requires compressible treatment even if inlet speed is modest.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. Use §81.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §81.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §81.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §81.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §81.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §81.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §81.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 10, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 10.

- **Mach number:** Speed of sound and Mach number
- **stagnation temperature:** Stagnation and static properties
- **choked flow:** Area-Mach relation and choking
- **compressible nozzle mass flow:** Mass flow through compressible nozzles
- **normal shock:** Normal shock relations and entropy rise
- **de Laval nozzle:** Converging-diverging nozzle operating regimes
- **compressible-flow validity:** Compressible-flow model checks

---

## What's Next

**Chapter 03-82: Combustion and Combustion Products**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
