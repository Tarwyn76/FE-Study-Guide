---
chapter: "02-26"
title: "Rigid-Body Equilibrium and Support Reactions"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-026-01, MECH-2C-026-02, MECH-2C-026-03, MECH-2C-026-04, MECH-2C-026-05, MECH-2C-026-06, MECH-2C-026-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-26: Rigid-Body Equilibrium and Support Reactions

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-22 Free-Body Diagrams · 02-25 Moments

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives force and moment equilibrium. Support-reaction modeling is standard guide-developed application of those equations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **26.1** Explain and apply **Planar Rigid-Body Equilibrium**.
* **26.2** Explain and apply **Pins, Rollers, and Fixed Supports**.
* **26.3** Explain and apply **Moment-Center Selection**.
* **26.4** Explain and apply **Beams and Simple Support Reactions**.
* **26.5** Explain and apply **Three-Dimensional Awareness**.
* **26.6** Explain and apply **Static Determinacy**.
* **26.7** Explain and apply **Physical and Algebraic Checks**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 26.1 Planar Rigid-Body Equilibrium

A rigid body in planar static equilibrium has no translational or angular acceleration. Three independent scalar equations are available.

Unlike a concurrent-force system, moments cannot generally be omitted because force lines of action do not all intersect at one point.

\[\sum F_x=0,\qquad\sum F_y=0,\qquad\sum M_O=0\]

![FIG-02-26-001: Rigid body with nonconcurrent loads and the three 2D equilibrium equations.](../figures/FIG-02-26-001-planar-rigid-body-equilibrium.png)

### Worked Example 1

**Problem.** A simply supported 6-m beam carries a 12-kN midspan point load. Find vertical reactions.

**Solution.** By symmetry Ay=By=6 kN upward.

---

## 26.2 Pins, Rollers, and Fixed Supports

Model support reactions according to constrained motion. A roller or smooth contact supplies one force normal to the contact. A pin prevents translation in two directions but permits rotation. A fixed support prevents translation and rotation, supplying two force components and a couple moment in 2D.

Over-modeling a support creates fictitious unknowns and can make a determinate problem appear indeterminate.

\[\text{roller }1,\quad \text{pin }2,\quad \text{fixed }3\text{ reaction unknowns}\]

![FIG-02-26-002: Reference chart for 2D supports and corresponding reaction unknowns.](../figures/FIG-02-26-002-pins-rollers-and-fixed-supports.png)

### Worked Example 2

**Problem.** A 10-kN load acts 2 m from A on a 5-m simply supported beam. Find By.

**Solution.** ΣMA=0: By(5)=10(2), so By=4 kN; Ay=6 kN.

---

## 26.3 Moment-Center Selection

Moment equations are most efficient when the moment center lies at the intersection of unknown reaction lines. Those forces then contribute zero moment.

The equilibrium equations are valid about any point; strategic point selection only simplifies algebra.

\[\sum M_A=0\]

![FIG-02-26-003: Beam with pin and roller, moment taken about pin to eliminate two reaction components.](../figures/FIG-02-26-003-moment-center-selection.png)

### Worked Example 3

**Problem.** How many 2D reactions does a fixed support provide?

**Solution.** Three: Ax, Ay, and a couple moment.

---

## 26.4 Beams and Simple Support Reactions

For a simply supported beam, first replace distributed loads by equivalent resultants if the reaction calculation only needs overall force/moment balance. Then solve moments for one reaction and vertical-force equilibrium for the other.

Keep any horizontal applied load and pin horizontal reaction in the model.

\[\sum M_A=0\rightarrow B_y,\qquad \sum F_y=0\rightarrow A_y\]

![FIG-02-26-004: Simply supported beam with point and distributed loads replaced for reaction calculation.](../figures/FIG-02-26-004-beams-and-simple-support-reactions.png)

### Worked Example 4

**Problem.** How many independent planar rigid-body equilibrium equations are available?

**Solution.** Three.

---

## 26.5 Three-Dimensional Awareness

Tier 2C focuses primarily on planar mechanics, but real supports may restrain three translations and three rotations. A 2D model is valid only when loading and geometry justify reduction to a plane.

Do not discard an out-of-plane reaction simply because it is inconvenient; establish the symmetry or loading condition that makes it zero.

\[\sum\mathbf F=\mathbf0,\qquad\sum\mathbf M=\mathbf0\]

![FIG-02-26-005: 3D support/loading system reduced to 2D only after symmetry and coplanarity are established.](../figures/FIG-02-26-005-three-dimensional-awareness.png)

### Worked Example 5

**Problem.** What is gained by taking moments about a pin support?

**Solution.** Both pin reaction components have zero moment and are eliminated from that equation.

---

## 26.6 Static Determinacy

A structure is externally statically determinate when the available independent equilibrium equations are sufficient to solve the reaction unknowns.

More reaction unknowns than independent equations does not mean equilibrium fails; it means deformation/compatibility relations are also needed and the system is statically indeterminate.

\[\text{unknown reactions}\le \text{independent equilibrium equations}\]

![FIG-02-26-006: Determinate simply supported beam versus indeterminate fixed-fixed beam.](../figures/FIG-02-26-006-static-determinacy.png)

### Worked Example 6

**Problem.** If a system has four independent reaction unknowns but only three equilibrium equations, what is it externally?

**Solution.** Statically indeterminate by one degree, absent additional special relations.

---

## 26.7 Physical and Algebraic Checks

After solving reactions, verify the net force and net moment. Then check physical plausibility: a roller normal reaction should have the expected contact sense unless uplift/separation is possible; symmetry should produce symmetric reactions under symmetric loading.

A negative assumed reaction direction is not automatically wrong—it indicates the true sense is opposite the assumed arrow.

\[\sum F_x=\sum F_y=\sum M_O=0\]

![FIG-02-26-007: Support-reaction audit with residual equilibrium and symmetry/contact checks.](../figures/FIG-02-26-007-physical-and-algebraic-checks.png)

### Worked Example 7

**Problem.** Can a negative roller reaction always occur physically?

**Solution.** Not if the roller/contact cannot sustain tension; it may imply separation or an incorrect assumed loading state.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Why may a distributed load be replaced by a resultant for reaction calculations?

**Solution.** Because the equivalent force and moment produce the same external static effect.

### Worked Example 9

**Problem.** What symmetry check applies to symmetric loading on symmetric supports?

**Solution.** Corresponding reactions should be symmetric/equal where geometry and support conditions are symmetric.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Statics, printed p. 95**.

**Source boundary:** The Handbook directly gives force and moment equilibrium. Support-reaction modeling is standard guide-developed application of those equations.

---

## Where This Goes Wrong

**Applying rigid-body equilibrium before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying support reaction before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying moment-center strategy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying beam reactions before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying planar reduction before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying static determinacy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying reaction check before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| rigid-body equilibrium | Concept developed in §26.1; apply only under that section's model assumptions. |
| support reaction | Concept developed in §26.2; apply only under that section's model assumptions. |
| moment-center strategy | Concept developed in §26.3; apply only under that section's model assumptions. |
| beam reactions | Concept developed in §26.4; apply only under that section's model assumptions. |
| planar reduction | Concept developed in §26.5; apply only under that section's model assumptions. |
| static determinacy | Concept developed in §26.6; apply only under that section's model assumptions. |
| reaction check | Concept developed in §26.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **rigid-body equilibrium** and state the governing relation or modeling rule.

2. Define **support reaction** and state the governing relation or modeling rule.

3. Define **moment-center strategy** and state the governing relation or modeling rule.

4. Define **beam reactions** and state the governing relation or modeling rule.

5. Define **planar reduction** and state the governing relation or modeling rule.

6. Define **static determinacy** and state the governing relation or modeling rule.

7. Define **reaction check** and state the governing relation or modeling rule.

8. What error is likely if **rigid-body equilibrium** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **support reaction** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **moment-center strategy** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **beam reactions** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **planar reduction** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **static determinacy** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **reaction check** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **rigid-body equilibrium**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **support reaction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **moment-center strategy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **beam reactions**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **planar reduction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **static determinacy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **reaction check**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **rigid-body equilibrium**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **support reaction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **rigid-body equilibrium** is developed in §26.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **support reaction** is developed in §26.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **moment-center strategy** is developed in §26.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **beam reactions** is developed in §26.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **planar reduction** is developed in §26.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **static determinacy** is developed in §26.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **reaction check** is developed in §26.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **rigid-body equilibrium**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **support reaction**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **moment-center strategy**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **beam reactions**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **planar reduction**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **static determinacy**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **reaction check**.

15. Define the system and axes first, then use residual equilibrium, units, known limiting behavior, or constitutive/kinematic constraints to check the answer. Negative values often reverse an assumed vector sense when the physical model still permits that direction.

16. Define the system and axes first, then use residual equilibrium, units, known limiting behavior, or constitutive/kinematic constraints to check the answer. Negative values often reverse an assumed vector sense when the physical model still permits that direction.

17. Define the system and axes first, then use residual equilibrium, units, known limiting behavior, or constitutive/kinematic constraints to check the answer. Negative values often reverse an assumed vector sense when the physical model still permits that direction.

18. Define the system and axes first, then use residual equilibrium, units, known limiting behavior, or constitutive/kinematic constraints to check the answer. Negative values often reverse an assumed vector sense when the physical model still permits that direction.

19. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

20. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

21. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

22. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

23. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

24. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

25. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

26. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

27. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.


---

## Practice Problems

1. A simply supported 6-m beam carries a 12-kN midspan point load. Find vertical reactions.

2. A 10-kN load acts 2 m from A on a 5-m simply supported beam. Find By.

3. How many 2D reactions does a fixed support provide?

4. How many independent planar rigid-body equilibrium equations are available?

5. What is gained by taking moments about a pin support?

6. If a system has four independent reaction unknowns but only three equilibrium equations, what is it externally?

7. Can a negative roller reaction always occur physically?

8. Why may a distributed load be replaced by a resultant for reaction calculations?

9. What symmetry check applies to symmetric loading on symmetric supports?

10. State the full 2D equilibrium set.


---

## Practice Problem Solutions

1. By symmetry Ay=By=6 kN upward.

2. ΣMA=0: By(5)=10(2), so By=4 kN; Ay=6 kN.

3. Three: Ax, Ay, and a couple moment.

4. Three.

5. Both pin reaction components have zero moment and are eliminated from that equation.

6. Statically indeterminate by one degree, absent additional special relations.

7. Not if the roller/contact cannot sustain tension; it may imply separation or an incorrect assumed loading state.

8. Because the equivalent force and moment produce the same external static effect.

9. Corresponding reactions should be symmetric/equal where geometry and support conditions are symmetric.

10. ΣFx=0, ΣFy=0, ΣM=0.


---

## Quick Reference

**Handbook anchor:** Statics, printed p. 95.

- **rigid-body equilibrium:** Planar Rigid-Body Equilibrium
- **support reaction:** Pins, Rollers, and Fixed Supports
- **moment-center strategy:** Moment-Center Selection
- **beam reactions:** Beams and Simple Support Reactions
- **planar reduction:** Three-Dimensional Awareness
- **static determinacy:** Static Determinacy
- **reaction check:** Physical and Algebraic Checks
---

## What's Next

**02-27 — Method of Sections, Frames, and Machines**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor