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

**Solution.** \(M=V/a=(340\ {\rm m/s})/(340\ {\rm m/s})=\mathbf{1.00}\). The flow is sonic relative to the stated local speed of sound.

---

## 81.2 Stagnation and static properties

Isentropic flow relations connect static and stagnation temperature, pressure, and density. Stagnation quantities represent reversible deceleration to zero velocity.

\[\frac{T_0}{T}=1+\frac{\gamma-1}{2}M^2\]

![FIG-03-81-002: Flow decelerated isentropically to a stagnation point with static and total properties.](../figures/FIG-03-81-002-stagnation-and-static-properties.png)

### Worked Example 2

**Problem.** At M=0, stagnation and static properties are equal.

**Solution.** At \(M=0\), the kinetic contribution vanishes. Thus \(T_0/T=1+[(\gamma-1)/2](0)^2=1\), so stagnation and static temperature are equal; analogous stagnation/static differences also vanish.

---

## 81.3 Area-Mach relation and choking

For one-dimensional isentropic flow, nozzle area and Mach number are coupled. Once a converging nozzle is choked, lowering downstream pressure cannot increase mass flow indefinitely.

\[M=1\text{ at the minimum-area throat of an ideal choked nozzle}\]

![FIG-03-81-003: Converging-diverging nozzle with throat, subsonic/supersonic branches, and Mach distribution.](../figures/FIG-03-81-003-area-mach-relation-and-choking.png)

### Worked Example 3

**Problem.** At choking, throat Mach number is 1.

**Solution.** For ideal one-dimensional nozzle flow, choking places the throat at **Mach number 1.00**, i.e. \(\mathbf{M_t=1.00}\) (dimensionless), at the minimum-area section. Further lowering downstream pressure cannot increase the throat Mach number above one in a purely converging throat.

---

## 81.4 Mass flow through compressible nozzles

Continuity still governs compressible flow, but density varies with pressure and temperature. Critical conditions set maximum ideal mass flow for a given stagnation state and throat area.

\[\dot m=\rho AV\]

![FIG-03-81-004: Nozzle mass flow versus downstream-to-upstream pressure ratio showing choking plateau.](../figures/FIG-03-81-004-mass-flow-through-compressible-nozzles.png)

### Worked Example 4

**Problem.** At fixed stagnation conditions and throat area, choked mass flow is insensitive to further downstream-pressure reduction in the ideal model.

**Solution.** Once an ideal nozzle is choked, mass flow is fixed primarily by upstream stagnation state, throat area, and gas properties. Further downstream-pressure reduction changes downstream behavior but not the ideal choked mass-flow rate until the governing regime changes.

---

## 81.5 Normal shock relations and entropy rise

A normal shock abruptly converts supersonic flow to subsonic flow, raising static pressure and temperature while decreasing stagnation pressure.

\[M_1>1,\quad M_2<1\]

![FIG-03-81-005: Normal shock in a duct with upstream/downstream Mach, pressure, temperature, and total-pressure change.](../figures/FIG-03-81-005-normal-shock-relations-and-entropy-rise.png)

### Worked Example 5

**Problem.** A normal shock cannot be treated as isentropic.

**Solution.** A normal shock is irreversible: upstream \(M_1>1\), downstream \(M_2<1\), stagnation pressure decreases, and entropy increases. Treating the shock itself as isentropic would violate the second law.

---

## 81.6 Converging-diverging nozzle operating regimes

A converging-diverging nozzle can exhibit entirely subsonic flow, choking, internal shocks, or supersonic expansion depending on pressure ratio.

\[\text{back pressure controls subsonic, choked, shocked, or fully supersonic states}\]

![FIG-03-81-006: Nozzle pressure profiles for subsonic, choked-with-shock, design, and under/overexpanded operation.](../figures/FIG-03-81-006-converging-diverging-nozzle-operating-regimes.png)

### Worked Example 6

**Problem.** The diverging section acts as a diffuser for subsonic flow but a nozzle for supersonic flow.

**Solution.** The area effect reverses across Mach 1. In a diverging passage subsonic flow tends to decelerate, whereas supersonic flow can accelerate; back pressure determines whether the nozzle is fully subsonic, choked, shock-containing, or supersonic downstream.

---

## 81.7 Compressible-flow model checks

Before using incompressible formulas, check Mach number and pressure/temperature changes. At sufficiently low Mach number, incompressible approximations may be adequate.

\[\text{compressibility becomes important as density changes are no longer negligible}\]

![FIG-03-81-007: Decision tree for incompressible versus compressible gas-flow modeling.](../figures/FIG-03-81-007-compressible-flow-model-checks.png)

### Worked Example 7

**Problem.** Gas flow through a large pressure ratio requires compressible treatment even if inlet speed is modest.

**Solution.** A large pressure ratio can create substantial density and temperature changes even when the inlet velocity is modest. In that case a constant-density incompressible model is not adequate; compressible continuity/energy/state relations are required.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. Compressible-flow equations are regime specific. If the solution crosses Mach 1, choking, or a shock without using the corresponding model, the operating point must be reclassified and recalculated.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **ANDERSON** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 10; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Anderson, J. D., Jr. (2021). *Modern Compressible Flow: With Historical Perspective* (4th ed.). McGraw Hill. ISBN 978-1-260-47144-1. Supporting scope: Mach number, speed of sound, stagnation properties, choking, nozzle flow, and normal shocks.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks**, start from the physical model and system/component state, not from an isolated formula. A valid solution must identify Mach regime, choking state, stagnation/static basis, nozzle geometry, and whether a shock or isentropic relation is actually applicable.

16. Units and sign/reference conventions are part of the model in **Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks**. External sources **ANDERSON** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: set \(M=0\) and confirm stagnation and static properties coincide; at an ideal choked throat confirm \(M=1\). A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §81.1, **Speed of sound and Mach number**, uses \(M=\frac{V}{a},\qquad a=\sqrt{\gamma RT}\). Apply it only under the geometry/material/operating assumptions stated in §81.1, then compare the result with the physical behavior described there.

20. **A.** Section §81.2, **Stagnation and static properties**, uses \(\frac{T_0}{T}=1+\frac{\gamma-1}{2}M^2\). Apply it only under the geometry/material/operating assumptions stated in §81.2, then compare the result with the physical behavior described there.

21. **A.** Section §81.3, **Area-Mach relation and choking**, uses \(M=1\text{ at the minimum-area throat of an ideal choked nozzle}\). Apply it only under the geometry/material/operating assumptions stated in §81.3, then compare the result with the physical behavior described there.

22. **A.** Section §81.4, **Mass flow through compressible nozzles**, uses \(\dot m=\rho AV\). Apply it only under the geometry/material/operating assumptions stated in §81.4, then compare the result with the physical behavior described there.

23. **A.** Section §81.5, **Normal shock relations and entropy rise**, uses \(M_1>1,\quad M_2<1\). Apply it only under the geometry/material/operating assumptions stated in §81.5, then compare the result with the physical behavior described there.

24. **A.** Section §81.6, **Converging-diverging nozzle operating regimes**, uses \(\text{back pressure controls subsonic, choked, shocked, or fully supersonic states}\). Apply it only under the geometry/material/operating assumptions stated in §81.6, then compare the result with the physical behavior described there.

25. **A.** Section §81.7, **Compressible-flow model checks**, uses \(\text{compressibility becomes important as density changes are no longer negligible}\). Apply it only under the geometry/material/operating assumptions stated in §81.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **ANDERSON**; guide synthesis is supplemental explanation and exam-oriented workflow.


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

1. **Independent check for §81.1 — Speed of sound and Mach number.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(M=V/a=(340\ {\rm m/s})/(340\ {\rm m/s})=\mathbf{1.00}\). The flow is sonic relative to the stated local speed of sound.

2. **Independent check for §81.2 — Stagnation and static properties.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. At \(M=0\), the kinetic contribution vanishes. Thus \(T_0/T=1+[(\gamma-1)/2](0)^2=1\), so stagnation and static temperature are equal; analogous stagnation/static differences also vanish.

3. **Independent check for §81.3 — Area-Mach relation and choking.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For ideal one-dimensional nozzle flow, choking places \(M=\mathbf1\) at the minimum-area throat. Further lowering downstream pressure cannot increase the throat Mach number above one in a purely converging throat.

4. **Independent check for §81.4 — Mass flow through compressible nozzles.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Once an ideal nozzle is choked, mass flow is fixed primarily by upstream stagnation state, throat area, and gas properties. Further downstream-pressure reduction changes downstream behavior but not the ideal choked mass-flow rate until the governing regime changes.

5. **Independent check for §81.5 — Normal shock relations and entropy rise.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A normal shock is irreversible: upstream \(M_1>1\), downstream \(M_2<1\), stagnation pressure decreases, and entropy increases. Treating the shock itself as isentropic would violate the second law.

6. **Independent check for §81.6 — Converging-diverging nozzle operating regimes.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. The area effect reverses across Mach 1. In a diverging passage subsonic flow tends to decelerate, whereas supersonic flow can accelerate; back pressure determines whether the nozzle is fully subsonic, choked, shock-containing, or supersonic downstream.

7. **Independent check for §81.7 — Compressible-flow model checks.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A large pressure ratio can create substantial density and temperature changes even when the inlet velocity is modest. In that case a constant-density incompressible model is not adequate; compressible continuity/energy/state relations are required.

8. For **Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks**, one required acceptance screen is: identify Mach regime, choking state, stagnation/static basis, nozzle geometry, and whether a shock or isentropic relation is actually applicable. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks**. For `split_required` concepts, use **ANDERSON** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: set \(M=0\) and confirm stagnation and static properties coincide; at an ideal choked throat confirm \(M=1\). If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

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
