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

**Solution.** \(\mathrm{Re}=\rho VL/\mu\). With fluid properties and characteristic length fixed, \(\mathrm{Re}\propto V\); doubling velocity therefore **doubles Reynolds number** and can move the flow toward a different regime.

---

## 80.2 Boundary-layer thickness and wall shear

No-slip creates velocity gradients near a solid surface. Wall shear and boundary-layer growth determine skin-friction drag.

\[\tau_w=\mu\left.\frac{\partial u}{\partial y}\right|_w\]

![FIG-03-80-002: Boundary-layer velocity profiles at increasing downstream positions with wall shear.](../figures/FIG-03-80-002-boundary-layer-thickness-and-wall-shear.png)

### Worked Example 2

**Problem.** A larger near-wall velocity gradient produces larger viscous wall shear in a Newtonian fluid.

**Solution.** For a Newtonian fluid, \(\tau_w=\mu(\partial u/\partial y)_w\). A steeper near-wall velocity gradient at the same viscosity produces a larger magnitude of wall shear stress.

---

## 80.3 Pressure drag and flow separation

Adverse pressure gradients can separate a boundary layer, producing a wake and pressure drag. Streamlining delays separation.

\[D=D_{\text{friction}}+D_{\text{pressure}}\]

![FIG-03-80-003: Bluff body and streamlined body with separation points and wakes.](../figures/FIG-03-80-003-pressure-drag-and-flow-separation.png)

### Worked Example 3

**Problem.** A bluff cylinder has substantial pressure drag because of its separated wake.

**Solution.** A bluff body promotes boundary-layer separation and creates a broad low-pressure wake. The resulting front-to-back pressure imbalance produces substantial **pressure (form) drag**, often dominating skin-friction drag.

---

## 80.4 Drag coefficient

Drag coefficient packages geometry and flow-regime effects into a dimensionless force relation.

\[F_D=\frac12\rho V^2 C_DA\]

![FIG-03-80-004: Drag coefficient versus Reynolds number for representative shapes.](../figures/FIG-03-80-004-drag-coefficient.png)

### Worked Example 4

**Problem.** Doubling velocity quadruples drag if CD remains unchanged.

**Solution.** \(F_D=\tfrac12\rho V^2C_DA\). If \(\rho,C_D,A\) stay fixed, \(F_D\propto V^2\); doubling speed gives \(F_{D,2}/F_{D,1}=4\), so drag **quadruples**.

---

## 80.5 Lift coefficient

Lift arises from pressure and shear distributions with a component normal to the free-stream direction. Angle of attack strongly affects CL until stall.

\[F_L=\frac12\rho V^2 C_LA\]

![FIG-03-80-005: Airfoil with pressure distribution and lift/drag vectors plus CL versus angle-of-attack curve.](../figures/FIG-03-80-005-lift-coefficient.png)

### Worked Example 5

**Problem.** At constant CL, doubling speed quadruples ideal lift.

**Solution.** \(F_L=\tfrac12\rho V^2C_LA\). Under the stated constant-\(C_L\) assumption, doubling speed also multiplies lift by \(2^2=\mathbf4\).

---

## 80.6 Dimensional analysis and similarity

Model testing requires matching the dimensionless groups governing the physics, not simply geometric scale. Reynolds, Mach, Froude, or other similarity may dominate.

\[\Pi_i=f(\Pi_1,\Pi_2,\ldots)\]

![FIG-03-80-006: Scale model and prototype with geometric similarity and dimensionless-number matching.](../figures/FIG-03-80-006-dimensional-analysis-and-similarity.png)

### Worked Example 6

**Problem.** A small wind-tunnel model at the same speed as a full-size vehicle does not necessarily match Reynolds number.

**Solution.** Geometric similarity alone is not enough. For the same fluid, \(\mathrm{Re}=VL/\nu\), so a smaller model at the same speed has a proportionally smaller Reynolds number; matching the relevant dimensionless groups may require changing velocity, fluid, pressure, or scale.

---

## 80.7 Fan/pump/compressor similarity laws

Affinity/scaling laws estimate performance changes for geometrically similar rotating fluid machines under appropriate assumptions.

\[Q\propto ND^3,\quad H\propto N^2D^2,\quad P\propto N^3D^5\]

![FIG-03-80-007: Pump/fan performance curves shifted with rotational speed using affinity-law trends.](../figures/FIG-03-80-007-fan-pump-compressor-similarity-laws.png)

### Worked Example 7

**Problem.** At fixed diameter, doubling speed approximately doubles flow and quadruples head.

**Solution.** At fixed diameter, the affinity laws give \(Q\propto N\), \(H\propto N^2\), and \(P\propto N^3\). Doubling speed therefore gives approximately **2× flow, 4× head, and 8× power** within the similarity range.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. Drag/lift or similarity equations are only valid for the stated flow regime and dimensionless similarity. A Reynolds-number or separation-regime mismatch invalidates a coefficient copied from another condition.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **WHITE** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 10; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- White, F. M., & Xue, H. *Fluid Mechanics* (9th ed.). McGraw Hill. ISBN 978-1-260-25831-8. Supporting scope: External flow, Reynolds number, boundary layers, drag/lift, dimensional analysis, similarity, and turbomachinery scaling.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity**, start from the physical model and system/component state, not from an isolated formula. A valid solution must check Reynolds number, boundary-layer/separation regime, reference area/coefficient definition, and whether the required dimensionless groups are matched before using model or correlation data.

16. Units and sign/reference conventions are part of the model in **External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity**. External sources **WHITE** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: double velocity at fixed \(C_D,C_L\) and confirm ideal drag/lift become four times larger; at fixed diameter double fan speed and confirm the affinity-law 2/4/8 trend. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §80.1, **Reynolds number and external-flow regimes**, uses \(\mathrm{Re}=\frac{\rho VL}{\mu}=\frac{VL}{\nu}\). Apply it only under the geometry/material/operating assumptions stated in §80.1, then compare the result with the physical behavior described there.

20. **A.** Section §80.2, **Boundary-layer thickness and wall shear**, uses \(\tau_w=\mu\left.\frac{\partial u}{\partial y}\right|_w\). Apply it only under the geometry/material/operating assumptions stated in §80.2, then compare the result with the physical behavior described there.

21. **A.** Section §80.3, **Pressure drag and flow separation**, uses \(D=D_{\text{friction}}+D_{\text{pressure}}\). Apply it only under the geometry/material/operating assumptions stated in §80.3, then compare the result with the physical behavior described there.

22. **A.** Section §80.4, **Drag coefficient**, uses \(F_D=\frac12\rho V^2 C_DA\). Apply it only under the geometry/material/operating assumptions stated in §80.4, then compare the result with the physical behavior described there.

23. **A.** Section §80.5, **Lift coefficient**, uses \(F_L=\frac12\rho V^2 C_LA\). Apply it only under the geometry/material/operating assumptions stated in §80.5, then compare the result with the physical behavior described there.

24. **A.** Section §80.6, **Dimensional analysis and similarity**, uses \(\Pi_i=f(\Pi_1,\Pi_2,\ldots)\). Apply it only under the geometry/material/operating assumptions stated in §80.6, then compare the result with the physical behavior described there.

25. **A.** Section §80.7, **Fan/pump/compressor similarity laws**, uses \(Q\propto ND^3,\quad H\propto N^2D^2,\quad P\propto N^3D^5\). Apply it only under the geometry/material/operating assumptions stated in §80.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **WHITE**; guide synthesis is supplemental explanation and exam-oriented workflow.


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

1. **Independent check for §80.1 — Reynolds number and external-flow regimes.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\mathrm{Re}=\rho VL/\mu\). With fluid properties and characteristic length fixed, \(\mathrm{Re}\propto V\); doubling velocity therefore **doubles Reynolds number** and can move the flow toward a different regime.

2. **Independent check for §80.2 — Boundary-layer thickness and wall shear.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For a Newtonian fluid, \(\tau_w=\mu(\partial u/\partial y)_w\). A steeper near-wall velocity gradient at the same viscosity produces a larger magnitude of wall shear stress.

3. **Independent check for §80.3 — Pressure drag and flow separation.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A bluff body promotes boundary-layer separation and creates a broad low-pressure wake. The resulting front-to-back pressure imbalance produces substantial **pressure (form) drag**, often dominating skin-friction drag.

4. **Independent check for §80.4 — Drag coefficient.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(F_D=\tfrac12\rho V^2C_DA\). If \(\rho,C_D,A\) stay fixed, \(F_D\propto V^2\); doubling speed gives \(F_{D,2}/F_{D,1}=4\), so drag **quadruples**.

5. **Independent check for §80.5 — Lift coefficient.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(F_L=\tfrac12\rho V^2C_LA\). Under the stated constant-\(C_L\) assumption, doubling speed also multiplies lift by \(2^2=\mathbf4\).

6. **Independent check for §80.6 — Dimensional analysis and similarity.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Geometric similarity alone is not enough. For the same fluid, \(\mathrm{Re}=VL/\nu\), so a smaller model at the same speed has a proportionally smaller Reynolds number; matching the relevant dimensionless groups may require changing velocity, fluid, pressure, or scale.

7. **Independent check for §80.7 — Fan/pump/compressor similarity laws.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. At fixed diameter, the affinity laws give \(Q\propto N\), \(H\propto N^2\), and \(P\propto N^3\). Doubling speed therefore gives approximately **2× flow, 4× head, and 8× power** within the similarity range.

8. For **External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity**, one required acceptance screen is: check Reynolds number, boundary-layer/separation regime, reference area/coefficient definition, and whether the required dimensionless groups are matched before using model or correlation data. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity**. For `split_required` concepts, use **WHITE** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: double velocity at fixed \(C_D,C_L\) and confirm ideal drag/lift become four times larger; at fixed diameter double fan speed and confirm the affinity-law 2/4/8 trend. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

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
