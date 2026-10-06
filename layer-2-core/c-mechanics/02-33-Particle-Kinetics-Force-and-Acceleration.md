---
chapter: "02-33"
title: "Particle Kinetics — Force and Acceleration"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-033-01, MECH-2C-033-02, MECH-2C-033-03, MECH-2C-033-04, MECH-2C-033-05, MECH-2C-033-06, MECH-2C-033-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-33: Particle Kinetics — Force and Acceleration

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-22 Free-Body Diagrams · 02-32 Curvilinear Kinematics

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives weight, Newton's second law for a particle, and Cartesian and normal/tangential force-acceleration relations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **33.1** Explain and apply **Newton's Second Law for a Particle**.
* **33.2** Explain and apply **Weight and Mass**.
* **33.3** Explain and apply **Cartesian Force-Acceleration Equations**.
* **33.4** Explain and apply **Normal-Tangential Kinetics**.
* **33.5** Explain and apply **Connected Particles and Constraint Forces**.
* **33.6** Explain and apply **Friction in Particle Kinetics**.
* **33.7** Explain and apply **Kinetics Solution Workflow**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 33.1 Newton's Second Law for a Particle

For constant mass, the Handbook gives \(\sum\mathbf F=m\mathbf a\). The force sum must contain only external forces acting on the isolated particle or particle-like body.

Draw the FBD first; then choose coordinates and write component equations.

\[\sum\mathbf F=m\mathbf a\]

![FIG-02-33-001: Particle FBD connected to acceleration vector and Newton's second law.](../figures/FIG-02-33-001-newton-s-second-law-for-a-particle.png)

### Worked Example 1

**Problem.** A 10-kg particle has net force 50 N in +x. Find acceleration.

**Solution.** a=5 m/s².

---

## 33.2 Weight and Mass

Mass measures inertia; weight is the gravitational force.

In SI,

\[
W=mg.
\]

Do not substitute a weight value in newtons where mass in kilograms is required by \(F=ma\).

\[W=mg\]

![FIG-02-33-002: Mass m and gravitational force W=mg with SI unit distinction.](../figures/FIG-02-33-002-weight-and-mass.png)

### Worked Example 2

**Problem.** A 5-kg block weighs how much at g=9.81?

**Solution.** 49.05 N.

---

## 33.3 Cartesian Force-Acceleration Equations

Resolve forces and acceleration along fixed Cartesian axes.

The equations remain valid even when acceleration varies with time, position, or velocity, provided the instantaneous acceleration components are correct.

\[\sum F_x=ma_x,\qquad \sum F_y=ma_y\]

![FIG-02-33-003: Particle with multiple forces resolved into x/y and matched to ax/ay.](../figures/FIG-02-33-003-cartesian-force-acceleration-equations.png)

### Worked Example 3

**Problem.** A 2-kg particle travels at 6 m/s on radius 3 m. Find required inward resultant force.

**Solution.** Fn=m v²/r=2(36)/3=24 N.

---

## 33.4 Normal-Tangential Kinetics

For curved motion, normal force balance determines the force required to bend the trajectory, while tangential force balance governs change in speed.

The normal direction is toward the center of curvature.

\[\sum F_t=m\frac{dv}{dt},\qquad\sum F_n=m\frac{v^2}{\rho}\]

![FIG-02-33-004: Particle on curved path with tangential and inward normal force sums.](../figures/FIG-02-33-004-normal-tangential-kinetics.png)

### Worked Example 4

**Problem.** A 20-kg crate is pulled horizontally by 100 N with kinetic friction 30 N. Find acceleration.

**Solution.** a=(100-30)/20=3.5 m/s².

---

## 33.5 Connected Particles and Constraint Forces

Particles connected by ideal cords share kinematic constraints. A massless inextensible cord has a length relation whose derivatives connect velocities and accelerations.

Ideal pulley/cable models may use equal tension in a continuous massless cable, unless friction or pulley inertia is included.

\[L=\text{constant}\Rightarrow \dot L=0,\ \ddot L=0\]

![FIG-02-33-005: Two masses connected by an ideal cable over a pulley with acceleration constraint.](../figures/FIG-02-33-005-connected-particles-and-constraint-forces.png)

### Worked Example 5

**Problem.** Why must a cable constraint be differentiated to relate accelerations?

**Solution.** The fixed-length relation is geometric in positions; differentiating gives velocity then acceleration relations.

---

## 33.6 Friction in Particle Kinetics

When sliding occurs, kinetic friction acts opposite relative motion with magnitude \(F_k=\mu_kN\) in the simple model. For no slip, static friction is whatever value equilibrium/kinetics requires up to \(\mu_sN\).

Do not automatically set static friction equal to its maximum.

\[|F_s|\le\mu_sN,\qquad F_k=\mu_kN\]

![FIG-02-33-006: Accelerating block on rough surface with applied force, normal, weight, and friction.](../figures/FIG-02-33-006-friction-in-particle-kinetics.png)

### Worked Example 6

**Problem.** Can static friction always be set to μsN?

**Solution.** No, only at impending slip.

---

## 33.7 Kinetics Solution Workflow

A reliable workflow is: isolate the body, draw external forces, select coordinates, determine acceleration from kinematics/constraints, write \(\sum F=ma\), solve, and check force directions and units.

If the assumed contact force becomes tensile where contact can only push, the assumed motion/contact state must be reconsidered.

\[\text{FBD}\rightarrow\text{kinematics}\rightarrow\sum F=ma\rightarrow\text{check}\]

![FIG-02-33-007: Particle kinetics workflow from isolation to physical validation.](../figures/FIG-02-33-007-kinetics-solution-workflow.png)

### Worked Example 7

**Problem.** What is the first step in a kinetics problem?

**Solution.** Isolate the body and draw the FBD.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** If a normal reaction solves negative for a simple contact that can only push, what does it imply?

**Solution.** Contact assumption is invalid/separation occurs or model is wrong.

### Worked Example 9

**Problem.** What is the normal force equation in n-t coordinates?

**Solution.** ΣFn=m v²/ρ.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Dynamics, printed pp. 106–107**.

**Source boundary:** The Handbook directly gives weight, Newton's second law for a particle, and Cartesian and normal/tangential force-acceleration relations.

---

## Where This Goes Wrong

**Applying particle kinetics before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying weight-mass distinction before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying Cartesian kinetics before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying normal-tangential kinetics before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying connected particles before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying dynamic friction before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying kinetics workflow before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| particle kinetics | Concept developed in §33.1; apply only under that section's model assumptions. |
| weight-mass distinction | Concept developed in §33.2; apply only under that section's model assumptions. |
| Cartesian kinetics | Concept developed in §33.3; apply only under that section's model assumptions. |
| normal-tangential kinetics | Concept developed in §33.4; apply only under that section's model assumptions. |
| connected particles | Concept developed in §33.5; apply only under that section's model assumptions. |
| dynamic friction | Concept developed in §33.6; apply only under that section's model assumptions. |
| kinetics workflow | Concept developed in §33.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **particle kinetics** and state the governing relation or modeling rule.

2. Define **weight-mass distinction** and state the governing relation or modeling rule.

3. Define **Cartesian kinetics** and state the governing relation or modeling rule.

4. Define **normal-tangential kinetics** and state the governing relation or modeling rule.

5. Define **connected particles** and state the governing relation or modeling rule.

6. Define **dynamic friction** and state the governing relation or modeling rule.

7. Define **kinetics workflow** and state the governing relation or modeling rule.

8. What error is likely if **particle kinetics** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **weight-mass distinction** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **Cartesian kinetics** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **normal-tangential kinetics** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **connected particles** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **dynamic friction** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **kinetics workflow** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **particle kinetics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **weight-mass distinction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **Cartesian kinetics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **normal-tangential kinetics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **connected particles**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **dynamic friction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **kinetics workflow**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **particle kinetics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **weight-mass distinction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **particle kinetics** is developed in §33.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **weight-mass distinction** is developed in §33.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **Cartesian kinetics** is developed in §33.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **normal-tangential kinetics** is developed in §33.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **connected particles** is developed in §33.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **dynamic friction** is developed in §33.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **kinetics workflow** is developed in §33.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **particle kinetics**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **weight-mass distinction**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **Cartesian kinetics**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **normal-tangential kinetics**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **connected particles**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **dynamic friction**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **kinetics workflow**.

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

1. A 10-kg particle has net force 50 N in +x. Find acceleration.

2. A 5-kg block weighs how much at g=9.81?

3. A 2-kg particle travels at 6 m/s on radius 3 m. Find required inward resultant force.

4. A 20-kg crate is pulled horizontally by 100 N with kinetic friction 30 N. Find acceleration.

5. Why must a cable constraint be differentiated to relate accelerations?

6. Can static friction always be set to μsN?

7. What is the first step in a kinetics problem?

8. If a normal reaction solves negative for a simple contact that can only push, what does it imply?

9. What is the normal force equation in n-t coordinates?

10. Why are force and acceleration components resolved in the same coordinates?


---

## Practice Problem Solutions

1. a=5 m/s².

2. 49.05 N.

3. Fn=m v²/r=2(36)/3=24 N.

4. a=(100-30)/20=3.5 m/s².

5. The fixed-length relation is geometric in positions; differentiating gives velocity then acceleration relations.

6. No, only at impending slip.

7. Isolate the body and draw the FBD.

8. Contact assumption is invalid/separation occurs or model is wrong.

9. ΣFn=m v²/ρ.

10. Newton's law equates vector components along the same axes.


---

## Quick Reference

**Handbook anchor:** Dynamics, printed pp. 106–107.

- **particle kinetics:** Newton's Second Law for a Particle
- **weight-mass distinction:** Weight and Mass
- **Cartesian kinetics:** Cartesian Force-Acceleration Equations
- **normal-tangential kinetics:** Normal-Tangential Kinetics
- **connected particles:** Connected Particles and Constraint Forces
- **dynamic friction:** Friction in Particle Kinetics
- **kinetics workflow:** Kinetics Solution Workflow
---

## What's Next

**02-34 — Work, Energy, and Power**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor