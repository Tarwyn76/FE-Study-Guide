---
chapter: "02-23"
title: "Equilibrium Equations for a 2D Concurrent Force System"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-023-01, MECH-2C-023-02, MECH-2C-023-03, MECH-2C-023-04, MECH-2C-023-05, MECH-2C-023-06, MECH-2C-023-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-23: Equilibrium Equations for a 2D Concurrent Force System

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-22 Constructing a Free-Body Diagram · 01-13 Vector Fundamentals

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives force resolution, resultant-force construction, equilibrium requirements, and the definition of a concurrent-force system.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **23.1** Explain and apply **Concurrent Force Systems**.
* **23.2** Explain and apply **Resolving Forces into Components**.
* **23.3** Explain and apply **The Two Scalar Equilibrium Equations**.
* **23.4** Explain and apply **Solving Two Unknown Forces**.
* **23.5** Explain and apply **Resultants and Equilibrants**.
* **23.6** Explain and apply **Three-Force Equilibrium and Geometry**.
* **23.7** Explain and apply **Checks: Magnitudes, Directions, and Units**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 23.1 Concurrent Force Systems

A concurrent-force system has lines of action that intersect at one point. Because all forces pass through the same point, moments about that intersection vanish automatically and translational equilibrium is sufficient for a particle or concurrent system.

The first task is to confirm concurrency. A rigid body carrying forces at different lines of action is not reduced to a two-equation concurrent problem merely because it is drawn in two dimensions.

\[\sum \mathbf F=\mathbf 0\]

![FIG-02-23-001: Several force vectors with lines of action intersecting at one point.](../figures/FIG-02-23-001-concurrent-force-systems.png)

### Worked Example 1

**Problem.** A 500-N force acts 30° above +x. Find components.

**Solution.** Fx=500 cos30°=433 N; Fy=500 sin30°=250 N.

---

## 23.2 Resolving Forces into Components

Resolve each inclined force into signed Cartesian components. Use geometry, not a memorized sign pattern. Components inherit their signs from the chosen positive axes.

If a force direction is defined by a triangle or coordinate difference, construct a unit vector first and multiply by force magnitude.

\[F_x=F\cos\theta,\qquad F_y=F\sin\theta\]

![FIG-02-23-002: Inclined force resolved into signed x and y components with angle convention shown.](../figures/FIG-02-23-002-resolving-forces-into-components.png)

### Worked Example 2

**Problem.** A ring carries forces (300,0) N and (0,-400) N. Find resultant magnitude.

**Solution.** R=sqrt(300²+400²)=500 N.

---

## 23.3 The Two Scalar Equilibrium Equations

For a planar concurrent system, equilibrium requires both Cartesian component sums to vanish. These are independent scalar equations and can solve at most two independent unknown force quantities without additional geometric relations.

Choose axes that simplify the equations. Aligning an axis with an unknown cable force or surface can eliminate one component from an equation.

\[\sum F_x=0,\qquad \sum F_y=0\]

![FIG-02-23-003: Concurrent FBD beside the two scalar equilibrium equations with matching x/y component rows.](../figures/FIG-02-23-003-the-two-scalar-equilibrium-equations.png)

### Worked Example 3

**Problem.** What equilibrant balances the forces in Problem 2?

**Solution.** (-300,+400) N, magnitude 500 N.

---

## 23.4 Solving Two Unknown Forces

Write the component equations symbolically before substituting numbers. Solve the simultaneous equations while preserving signs. A negative force magnitude means the actual sense is opposite the assumed arrow.

Avoid replacing a vector equation with a scalar magnitude sum. Opposing force directions matter.

\[\begin{bmatrix}a&b\\c&d\end{bmatrix}\begin{bmatrix}F_1\\F_2\end{bmatrix}=\begin{bmatrix}r_1\\r_2\end{bmatrix}\]

![FIG-02-23-004: Two unknown cable tensions balancing a known load at a ring, with component-equation matrix.](../figures/FIG-02-23-004-solving-two-unknown-forces.png)

### Worked Example 4

**Problem.** A particle is in equilibrium under two unknown component forces and a known load. How many independent planar force equations are available?

**Solution.** Two: ΣFx=0 and ΣFy=0.

---

## 23.5 Resultants and Equilibrants

The resultant of several forces is their vector sum. An **equilibrant** is a single force equal in magnitude and opposite in direction to the resultant.

This provides a fast check: if known forces sum to \(\mathbf R\), the required balancing force for equilibrium is \(-\mathbf R\).

\[\mathbf R=\sum_i\mathbf F_i,\qquad \mathbf F_{\rm eq}=-\mathbf R\]

![FIG-02-23-005: Vector polygon showing resultant R and equilibrant -R closing the polygon.](../figures/FIG-02-23-005-resultants-and-equilibrants.png)

### Worked Example 5

**Problem.** Can three nonparallel forces keep a rigid body in equilibrium if their lines of action are not concurrent and no couple acts?

**Solution.** No; for a three-force body they must be concurrent.

---

## 23.6 Three-Force Equilibrium and Geometry

When exactly three nonparallel forces maintain a rigid body in equilibrium and no couple moments act, their lines of action must be concurrent. This geometric fact can locate an unknown reaction direction before the component equations are solved.

Do not apply the three-force-body shortcut when a couple moment acts or when more than three independent forces are present.

\[\text{3 nonparallel forces in equilibrium}\Rightarrow\text{concurrent lines of action}\]

![FIG-02-23-006: Three-force rigid body with the three lines of action extended to a common intersection.](../figures/FIG-02-23-006-three-force-equilibrium-and-geometry.png)

### Worked Example 6

**Problem.** A cable-force solution is -2.0 kN under a tension-positive assumption. Interpret it.

**Solution.** The assumed direction is wrong; an ideal cable cannot push, so the modeled configuration/contact must be reconsidered.

---

## 23.7 Checks: Magnitudes, Directions, and Units

After solving, reconstruct the vector balance and verify both component sums are approximately zero. Check that cable forces are tensile, contact forces obey any stated smooth-surface direction, and units are consistent.

An algebraic solution that requires a cable to push or a frictionless surface to pull signals a modeling error or an incorrect assumed configuration.

\[\left|\sum F_x\right|\approx0,\qquad\left|\sum F_y\right|\approx0\]

![FIG-02-23-007: Post-solution equilibrium audit showing component residuals and physical-direction checks.](../figures/FIG-02-23-007-checks-magnitudes-directions-and-units.png)

### Worked Example 7

**Problem.** Why can axes be rotated in a concurrent-force problem?

**Solution.** Equilibrium is vectorial; any orthogonal axes are valid, and convenient axes simplify components.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What is the difference between a resultant and equilibrant?

**Solution.** The resultant is the vector sum; the equilibrant is equal and opposite.

### Worked Example 9

**Problem.** How do you verify a solved concurrent system?

**Solution.** Recompute ΣFx and ΣFy and check both are zero within rounding.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Statics, printed pp. 95 and 98**.

**Source boundary:** The Handbook directly gives force resolution, resultant-force construction, equilibrium requirements, and the definition of a concurrent-force system.

---

## Where This Goes Wrong

**Applying concurrent forces before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying force components before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying planar equilibrium before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying equilibrium solution before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying resultant force before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying three-force body before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying equilibrium check before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| concurrent forces | Concept developed in §23.1; apply only under that section's model assumptions. |
| force components | Concept developed in §23.2; apply only under that section's model assumptions. |
| planar equilibrium | Concept developed in §23.3; apply only under that section's model assumptions. |
| equilibrium solution | Concept developed in §23.4; apply only under that section's model assumptions. |
| resultant force | Concept developed in §23.5; apply only under that section's model assumptions. |
| three-force body | Concept developed in §23.6; apply only under that section's model assumptions. |
| equilibrium check | Concept developed in §23.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **concurrent forces** and state the governing relation or modeling rule.

2. Define **force components** and state the governing relation or modeling rule.

3. Define **planar equilibrium** and state the governing relation or modeling rule.

4. Define **equilibrium solution** and state the governing relation or modeling rule.

5. Define **resultant force** and state the governing relation or modeling rule.

6. Define **three-force body** and state the governing relation or modeling rule.

7. Define **equilibrium check** and state the governing relation or modeling rule.

8. What error is likely if **concurrent forces** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **force components** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **planar equilibrium** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **equilibrium solution** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **resultant force** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **three-force body** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **equilibrium check** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **concurrent forces**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **force components**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **planar equilibrium**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **equilibrium solution**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **resultant force**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **three-force body**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **equilibrium check**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **concurrent forces**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **force components**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **concurrent forces** is developed in §23.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **force components** is developed in §23.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **planar equilibrium** is developed in §23.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **equilibrium solution** is developed in §23.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **resultant force** is developed in §23.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **three-force body** is developed in §23.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **equilibrium check** is developed in §23.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **concurrent forces**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **force components**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **planar equilibrium**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **equilibrium solution**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **resultant force**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **three-force body**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **equilibrium check**.

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

1. A 500-N force acts 30° above +x. Find components.

2. A ring carries forces (300,0) N and (0,-400) N. Find resultant magnitude.

3. What equilibrant balances the forces in Problem 2?

4. A particle is in equilibrium under two unknown component forces and a known load. How many independent planar force equations are available?

5. Can three nonparallel forces keep a rigid body in equilibrium if their lines of action are not concurrent and no couple acts?

6. A cable-force solution is -2.0 kN under a tension-positive assumption. Interpret it.

7. Why can axes be rotated in a concurrent-force problem?

8. What is the difference between a resultant and equilibrant?

9. How do you verify a solved concurrent system?

10. Why is ΣM not needed about the common intersection for a concurrent particle system?


---

## Practice Problem Solutions

1. Fx=500 cos30°=433 N; Fy=500 sin30°=250 N.

2. R=sqrt(300²+400²)=500 N.

3. (-300,+400) N, magnitude 500 N.

4. Two: ΣFx=0 and ΣFy=0.

5. No; for a three-force body they must be concurrent.

6. The assumed direction is wrong; an ideal cable cannot push, so the modeled configuration/contact must be reconsidered.

7. Equilibrium is vectorial; any orthogonal axes are valid, and convenient axes simplify components.

8. The resultant is the vector sum; the equilibrant is equal and opposite.

9. Recompute ΣFx and ΣFy and check both are zero within rounding.

10. Every force has zero moment about that intersection.


---

## Quick Reference

**Handbook anchor:** Statics, printed pp. 95 and 98.

- **concurrent forces:** Concurrent Force Systems
- **force components:** Resolving Forces into Components
- **planar equilibrium:** The Two Scalar Equilibrium Equations
- **equilibrium solution:** Solving Two Unknown Forces
- **resultant force:** Resultants and Equilibrants
- **three-force body:** Three-Force Equilibrium and Geometry
- **equilibrium check:** Checks: Magnitudes, Directions, and Units
---

## What's Next

**02-24 — Method of Joints for Planar Trusses**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor