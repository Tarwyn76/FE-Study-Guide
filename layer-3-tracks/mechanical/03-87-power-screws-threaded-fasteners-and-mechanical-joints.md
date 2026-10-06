---
chapter: "03-87"
title: "Power Screws, Threaded Fasteners, and Mechanical Joints"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-087-01, MEC-3-087-02, MEC-3-087-03, MEC-3-087-04, MEC-3-087-05, MEC-3-087-06, MEC-3-087-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-87: Power Screws, Threaded Fasteners, and Mechanical Joints

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MEC-3-078-07 · MECH-2C-022-03

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Power Screws, Threaded Fasteners, and Mechanical Joints**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **87.1** Explain and apply **Square-thread power screw torque**.
* **87.2** Explain and apply **Power-screw efficiency and self-locking**.
* **87.3** Explain and apply **Preloaded bolted joints and stiffness ratio**.
* **87.4** Explain and apply **Bolt and member load under external tension**.
* **87.5** Explain and apply **Joint separation and bolt design factors**.
* **87.6** Explain and apply **Shear joints, bearing/crushing, and net-section rupture**.
* **87.7** Explain and apply **Eccentrically loaded fastener groups and joining alternatives**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 87.1 Square-thread power screw torque

Power screws convert torque to axial force. Raising and lowering torque depend on thread geometry, friction, lead, and collar friction.

\[T_R=\frac{Fd_m}{2}\frac{\pi\mu d_m+l}{\pi d_m-\mu l}+\frac{F\mu_cd_c}{2}\]

![FIG-03-87-001: Square-thread power screw with load, mean diameter, lead, collar, and applied torque.](../figures/FIG-03-87-001-square-thread-power-screw-torque.png)

### Worked Example 1

**Problem.** Higher thread friction increases required raising torque.

**Solution.** Apply the relation and model in §87.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 87.2 Power-screw efficiency and self-locking

Efficiency compares useful lifting work per revolution with input work. Friction and lead angle determine whether a screw backdrives or self-locks.

\[\eta=\frac{Fl}{2\pi T_R}\]

![FIG-03-87-002: Power screw force/torque work diagram with lead helix and friction angle concept.](../figures/FIG-03-87-002-power-screw-efficiency-and-self-locking.png)

### Worked Example 2

**Problem.** At fixed load and lead, more torque means lower efficiency.

**Solution.** Apply the relation and model in §87.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 87.3 Preloaded bolted joints and stiffness ratio

In a preloaded joint, only a fraction C of an external separating load adds to bolt load; the rest relieves member compression.

\[C=\frac{k_b}{k_b+k_m}\]

![FIG-03-87-003: Bolt/member spring analogy with preload Fi and external separating load P.](../figures/FIG-03-87-003-preloaded-bolted-joints-and-stiffness-ratio.png)

### Worked Example 3

**Problem.** A stiff member stack relative to the bolt gives a smaller fraction of external load added to the bolt.

**Solution.** Apply the relation and model in §87.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 87.4 Bolt and member load under external tension

These relations apply while the members remain in compression/contact according to the model. Once separation occurs, the load sharing changes.

\[F_b=CP+F_i,\qquad F_m=(1-C)P-F_i\]

![FIG-03-87-004: Bolt and member load lines versus external load showing separation point.](../figures/FIG-03-87-004-bolt-and-member-load-under-external-tension.png)

### Worked Example 4

**Problem.** If the member compression reaches zero, the pre-separation equations should no longer be extrapolated.

**Solution.** Apply the relation and model in §87.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 87.5 Joint separation and bolt design factors

Joint design checks both bolt strength and separation. Adequate preload can improve fatigue behavior but must remain below proof/yield limits.

\[n_s=\frac{F_i}{P(1-C)}\]

![FIG-03-87-005: Bolted joint design map showing proof limit, preload, external load fraction, and separation limit.](../figures/FIG-03-87-005-joint-separation-and-bolt-design-factors.png)

### Worked Example 5

**Problem.** Increasing preload raises separation margin but also raises mean bolt stress.

**Solution.** Apply the relation and model in §87.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 87.6 Shear joints, bearing/crushing, and net-section rupture

Bolted or riveted shear joints may fail by fastener shear, member bearing/crushing, or net-section rupture. All plausible modes must be checked.

\[\tau=\frac FA,\qquad \sigma_{bearing}=\frac{F}{dt}\]

![FIG-03-87-006: Bolted lap joint with shear planes, net section, bearing stress, and failure modes.](../figures/FIG-03-87-006-shear-joints-bearing-crushing-and-net-section-rupture.png)

### Worked Example 6

**Problem.** A thicker plate increases projected bearing area dt and reduces bearing stress for fixed load.

**Solution.** Apply the relation and model in §87.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 87.7 Eccentrically loaded fastener groups and joining alternatives

An eccentric load creates direct shear plus a moment-induced shear pattern about the fastener-group centroid. Welds and adhesives may provide alternative load paths with different design issues.

\[F_{2i}=\frac{Mr_i}{\sum r_i^2}\]

![FIG-03-87-007: Eccentric fastener group with centroid, direct shear, moment, and individual force vectors.](../figures/FIG-03-87-007-eccentrically-loaded-fastener-groups-and-joining-alternatives.png)

### Worked Example 7

**Problem.** Fasteners farther from the centroid carry larger moment-induced force in the simplified elastic model.

**Solution.** Apply the relation and model in §87.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

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

Primary source basis: **FE Mechanical specification Area(s) 14; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** The Mechanical specification includes both directly tabulated Handbook equations and learned design concepts. This chapter does not assign invented Handbook pages to specification-required material that is not directly tabulated.

---

## Where This Goes Wrong

**Using power screw torque outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using power screw efficiency outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using bolted joint coefficient outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using preloaded bolt load outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using bolted joint safety factor outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using fastener shear joint outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using fastener group outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| power screw torque | Concept developed in §87.1; apply with that section's geometry and operating assumptions. |
| power screw efficiency | Concept developed in §87.2; apply with that section's geometry and operating assumptions. |
| bolted joint coefficient | Concept developed in §87.3; apply with that section's geometry and operating assumptions. |
| preloaded bolt load | Concept developed in §87.4; apply with that section's geometry and operating assumptions. |
| bolted joint safety factor | Concept developed in §87.5; apply with that section's geometry and operating assumptions. |
| fastener shear joint | Concept developed in §87.6; apply with that section's geometry and operating assumptions. |
| fastener group | Concept developed in §87.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **power screw torque** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **power screw efficiency** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **bolted joint coefficient** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **preloaded bolt load** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **bolted joint safety factor** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **fastener shear joint** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **fastener group** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **power screw torque**?

9. What geometric, material, operating, or model assumption must be checked before applying **power screw efficiency**?

10. What geometric, material, operating, or model assumption must be checked before applying **bolted joint coefficient**?

11. What geometric, material, operating, or model assumption must be checked before applying **preloaded bolt load**?

12. What geometric, material, operating, or model assumption must be checked before applying **bolted joint safety factor**?

13. What geometric, material, operating, or model assumption must be checked before applying **fastener shear joint**?

14. What geometric, material, operating, or model assumption must be checked before applying **fastener group**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **power screw torque**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **power screw efficiency**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **bolted joint coefficient**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **preloaded bolt load**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **bolted joint safety factor**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **fastener shear joint**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **fastener group**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **power screw torque**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **power screw efficiency**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **power screw torque** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **power screw efficiency** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **bolted joint coefficient** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **preloaded bolt load** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **bolted joint safety factor** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **fastener shear joint** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **fastener group** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **power screw torque**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **power screw efficiency**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **bolted joint coefficient**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **preloaded bolt load**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **bolted joint safety factor**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **fastener shear joint**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **fastener group**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

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

1. Higher thread friction increases required raising torque.

2. At fixed load and lead, more torque means lower efficiency.

3. A stiff member stack relative to the bolt gives a smaller fraction of external load added to the bolt.

4. If the member compression reaches zero, the pre-separation equations should no longer be extrapolated.

5. Increasing preload raises separation margin but also raises mean bolt stress.

6. A thicker plate increases projected bearing area dt and reduces bearing stress for fixed load.

7. Fasteners farther from the centroid carry larger moment-induced force in the simplified elastic model.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. Use §87.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §87.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §87.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §87.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §87.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §87.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §87.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 14, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 14.

- **power screw torque:** Square-thread power screw torque
- **power screw efficiency:** Power-screw efficiency and self-locking
- **bolted joint coefficient:** Preloaded bolted joints and stiffness ratio
- **preloaded bolt load:** Bolt and member load under external tension
- **bolted joint safety factor:** Joint separation and bolt design factors
- **fastener shear joint:** Shear joints, bearing/crushing, and net-section rupture
- **fastener group:** Eccentrically loaded fastener groups and joining alternatives

---

## What's Next

**Chapter 03-88: Shafts, Keys, Couplings, Gears, Belts, Chains, and Power Transmission**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
