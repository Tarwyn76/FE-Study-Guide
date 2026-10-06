---
chapter: "03-80"
title: "External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-080-01, MEC-3-080-02, MEC-3-080-03, MEC-3-080-04, MEC-3-080-05, MEC-3-080-06, MEC-3-080-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-80: External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** FLUID-2D-041-01

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **80.1** Explain and apply **Reynolds number and external-flow regimes**.
* **80.2** Explain and apply **Boundary-layer thickness and wall shear**.
* **80.3** Explain and apply **Pressure drag and flow separation**.
* **80.4** Explain and apply **Drag coefficient**.
* **80.5** Explain and apply **Lift coefficient**.
* **80.6** Explain and apply **Dimensional analysis and similarity**.
* **80.7** Explain and apply **Fan/pump/compressor similarity laws**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 80.1 Reynolds number and external-flow regimes

External-flow behavior depends strongly on Reynolds number and geometry. Transition location and separation influence drag and heat transfer.

\[\mathrm{Re}=\frac{\rho VL}{\mu}=\frac{VL}{\nu}\]

![FIG-03-80-001: Flow over a flat plate with growing laminar/transitional/turbulent boundary layer.](../figures/FIG-03-80-001-reynolds-number-and-external-flow-regimes.png)

### Worked Example 1

**Problem.** For fixed fluid and length, doubling velocity doubles Reynolds number.

**Solution.** Apply the relation and model in §80.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 80.2 Boundary-layer thickness and wall shear

No-slip creates velocity gradients near a solid surface. Wall shear and boundary-layer growth determine skin-friction drag.

\[\tau_w=\mu\left.\frac{\partial u}{\partial y}\right|_w\]

![FIG-03-80-002: Boundary-layer velocity profiles at increasing downstream positions with wall shear.](../figures/FIG-03-80-002-boundary-layer-thickness-and-wall-shear.png)

### Worked Example 2

**Problem.** A larger near-wall velocity gradient produces larger viscous wall shear in a Newtonian fluid.

**Solution.** Apply the relation and model in §80.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 80.3 Pressure drag and flow separation

Adverse pressure gradients can separate a boundary layer, producing a wake and pressure drag. Streamlining delays separation.

\[D=D_{\text{friction}}+D_{\text{pressure}}\]

![FIG-03-80-003: Bluff body and streamlined body with separation points and wakes.](../figures/FIG-03-80-003-pressure-drag-and-flow-separation.png)

### Worked Example 3

**Problem.** A bluff cylinder has substantial pressure drag because of its separated wake.

**Solution.** Apply the relation and model in §80.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 80.4 Drag coefficient

Drag coefficient packages geometry and flow-regime effects into a dimensionless force relation.

\[F_D=\frac12\rho V^2 C_DA\]

![FIG-03-80-004: Drag coefficient versus Reynolds number for representative shapes.](../figures/FIG-03-80-004-drag-coefficient.png)

### Worked Example 4

**Problem.** Doubling velocity quadruples drag if CD remains unchanged.

**Solution.** Apply the relation and model in §80.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 80.5 Lift coefficient

Lift arises from pressure and shear distributions with a component normal to the free-stream direction. Angle of attack strongly affects CL until stall.

\[F_L=\frac12\rho V^2 C_LA\]

![FIG-03-80-005: Airfoil with pressure distribution and lift/drag vectors plus CL versus angle-of-attack curve.](../figures/FIG-03-80-005-lift-coefficient.png)

### Worked Example 5

**Problem.** At constant CL, doubling speed quadruples ideal lift.

**Solution.** Apply the relation and model in §80.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 80.6 Dimensional analysis and similarity

Model testing requires matching the dimensionless groups governing the physics, not simply geometric scale. Reynolds, Mach, Froude, or other similarity may dominate.

\[\Pi_i=f(\Pi_1,\Pi_2,\ldots)\]

![FIG-03-80-006: Scale model and prototype with geometric similarity and dimensionless-number matching.](../figures/FIG-03-80-006-dimensional-analysis-and-similarity.png)

### Worked Example 6

**Problem.** A small wind-tunnel model at the same speed as a full-size vehicle does not necessarily match Reynolds number.

**Solution.** Apply the relation and model in §80.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 80.7 Fan/pump/compressor similarity laws

Affinity/scaling laws estimate performance changes for geometrically similar rotating fluid machines under appropriate assumptions.

\[Q\propto ND^3,\quad H\propto N^2D^2,\quad P\propto N^3D^5\]

![FIG-03-80-007: Pump/fan performance curves shifted with rotational speed using affinity-law trends.](../figures/FIG-03-80-007-fan-pump-compressor-similarity-laws.png)

### Worked Example 7

**Problem.** At fixed diameter, doubling speed approximately doubles flow and quadruples head.

**Solution.** Apply the relation and model in §80.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

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

**Using external-flow Reynolds number outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using boundary layer outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using flow separation outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using drag coefficient outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using lift coefficient outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using Buckingham Pi similarity outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using rotating-fluid-machine scaling outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| external-flow Reynolds number | Concept developed in §80.1; apply with that section's geometry and operating assumptions. |
| boundary layer | Concept developed in §80.2; apply with that section's geometry and operating assumptions. |
| flow separation | Concept developed in §80.3; apply with that section's geometry and operating assumptions. |
| drag coefficient | Concept developed in §80.4; apply with that section's geometry and operating assumptions. |
| lift coefficient | Concept developed in §80.5; apply with that section's geometry and operating assumptions. |
| Buckingham Pi similarity | Concept developed in §80.6; apply with that section's geometry and operating assumptions. |
| rotating-fluid-machine scaling | Concept developed in §80.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **external-flow Reynolds number** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **boundary layer** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **flow separation** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **drag coefficient** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **lift coefficient** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **Buckingham Pi similarity** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **rotating-fluid-machine scaling** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **external-flow Reynolds number**?

9. What geometric, material, operating, or model assumption must be checked before applying **boundary layer**?

10. What geometric, material, operating, or model assumption must be checked before applying **flow separation**?

11. What geometric, material, operating, or model assumption must be checked before applying **drag coefficient**?

12. What geometric, material, operating, or model assumption must be checked before applying **lift coefficient**?

13. What geometric, material, operating, or model assumption must be checked before applying **Buckingham Pi similarity**?

14. What geometric, material, operating, or model assumption must be checked before applying **rotating-fluid-machine scaling**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **external-flow Reynolds number**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **boundary layer**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **flow separation**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **drag coefficient**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **lift coefficient**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **Buckingham Pi similarity**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **rotating-fluid-machine scaling**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **external-flow Reynolds number**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **boundary layer**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **external-flow Reynolds number** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **boundary layer** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **flow separation** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **drag coefficient** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **lift coefficient** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **Buckingham Pi similarity** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **rotating-fluid-machine scaling** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **external-flow Reynolds number**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **boundary layer**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **flow separation**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **drag coefficient**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **lift coefficient**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **Buckingham Pi similarity**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **rotating-fluid-machine scaling**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

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

1. For fixed fluid and length, doubling velocity doubles Reynolds number.

2. A larger near-wall velocity gradient produces larger viscous wall shear in a Newtonian fluid.

3. A bluff cylinder has substantial pressure drag because of its separated wake.

4. Doubling velocity quadruples drag if CD remains unchanged.

5. At constant CL, doubling speed quadruples ideal lift.

6. A small wind-tunnel model at the same speed as a full-size vehicle does not necessarily match Reynolds number.

7. At fixed diameter, doubling speed approximately doubles flow and quadruples head.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. Use §80.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §80.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §80.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §80.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §80.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §80.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §80.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 10, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 10.

- **external-flow Reynolds number:** Reynolds number and external-flow regimes
- **boundary layer:** Boundary-layer thickness and wall shear
- **flow separation:** Pressure drag and flow separation
- **drag coefficient:** Drag coefficient
- **lift coefficient:** Lift coefficient
- **Buckingham Pi similarity:** Dimensional analysis and similarity
- **rotating-fluid-machine scaling:** Fan/pump/compressor similarity laws

---

## What's Next

**Chapter 03-81: Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
