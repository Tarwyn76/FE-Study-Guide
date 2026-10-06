---
chapter: "02-31"
title: "Particle Kinematics — Rectilinear Motion"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-031-01, MECH-2C-031-02, MECH-2C-031-03, MECH-2C-031-04, MECH-2C-031-05, MECH-2C-031-06, MECH-2C-031-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-31: Particle Kinematics — Rectilinear Motion

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 01-18 Derivatives · 01-19 Integrals

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines particle position, velocity, acceleration, rectilinear derivative relations, constant-acceleration equations, and nonconstant-acceleration integration.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **31.1** Explain and apply **Position, Displacement, Velocity, and Acceleration**.
* **31.2** Explain and apply **Constant-Acceleration Equations**.
* **31.3** Explain and apply **Free Fall and Sign Convention**.
* **31.4** Explain and apply **Variable Acceleration as a Function of Time**.
* **31.5** Explain and apply **Acceleration as a Function of Position**.
* **31.6** Explain and apply **Interpreting Motion Graphs**.
* **31.7** Explain and apply **Relative Rectilinear Motion**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 31.1 Position, Displacement, Velocity, and Acceleration

Rectilinear motion uses one position coordinate \(s(t)\). Velocity is the time derivative of position and acceleration is the derivative of velocity.

Signs convey direction along the chosen axis. Speed is the magnitude of velocity.

\[v=\frac{ds}{dt},\qquad a=\frac{dv}{dt}=\frac{d^2s}{dt^2}\]

![FIG-02-31-001: Position, velocity, and acceleration graphs connected by differentiation.](../figures/FIG-02-31-001-position-displacement-velocity-and-acceleration.png)

### Worked Example 1

**Problem.** A car starts at 5 m/s and accelerates at 2 m/s² for 4 s. Find final velocity.

**Solution.** v=5+2(4)=13 m/s.

---

## 31.2 Constant-Acceleration Equations

When acceleration is constant, the Handbook gives the familiar kinematic equations. Use them only when acceleration truly is constant over the interval.

Choose the equation that eliminates the variable you do not need.

\[v=v_0+at,\quad s=s_0+v_0t+\tfrac12at^2,\quad v^2=v_0^2+2a(s-s_0)\]

![FIG-02-31-002: Three constant-acceleration equations arranged by variables present.](../figures/FIG-02-31-002-constant-acceleration-equations.png)

### Worked Example 2

**Problem.** For Problem 1, find displacement over 4 s.

**Solution.** Δs=5(4)+0.5(2)(16)=36 m.

---

## 31.3 Free Fall and Sign Convention

Near Earth's surface, free fall is modeled with constant downward acceleration \(g\) when air resistance is neglected.

If upward is positive, \(a=-g\). If downward is positive, \(a=+g\). The physics is unchanged; only signs differ.

\[a_y=-g\quad(\text{upward positive})\]

![FIG-02-31-003: Vertical trajectory with upward-positive axis, velocity changing through zero at the top, and acceleration downward throughout.](../figures/FIG-02-31-003-free-fall-and-sign-convention.png)

### Worked Example 3

**Problem.** An object is dropped from rest for 2 s. Find speed using g=9.81 m/s².

**Solution.** Speed=19.62 m/s downward.

---

## 31.4 Variable Acceleration as a Function of Time

For known \(a(t)\), integrate acceleration to obtain velocity and then integrate velocity to obtain position. Include initial conditions in each integration.

Definite-integral form often reduces constant-of-integration mistakes.

\[v(t)=v_0+\int_{t_0}^{t}a(\tau)d\tau,\qquad s(t)=s_0+\int_{t_0}^{t}v(\tau)d\tau\]

![FIG-02-31-004: Variable acceleration curve with area under a-t giving velocity change.](../figures/FIG-02-31-004-variable-acceleration-as-a-function-of-time.png)

### Worked Example 4

**Problem.** A particle has s=3t²+2t m. Find v and a.

**Solution.** v=6t+2 m/s; a=6 m/s².

---

## 31.5 Acceleration as a Function of Position

When acceleration is given as a function of position and time is absent, use the chain-rule relation

\[
a=vrac{dv}{ds}.
\]

Integrate \(v\,dv=a(s)\,ds\) between known states.

\[a=v\frac{dv}{ds}\]

![FIG-02-31-005: Velocity-versus-position curve with differential relation v dv = a ds.](../figures/FIG-02-31-005-acceleration-as-a-function-of-position.png)

### Worked Example 5

**Problem.** If v changes sign during an interval, how should total distance be found?

**Solution.** Break at the turning point and sum absolute displacements.

---

## 31.6 Interpreting Motion Graphs

Slope of the \(s-t\) graph is velocity. Slope of the \(v-t\) graph is acceleration. Area under \(v-t\) is displacement; area under \(a-t\) is change in velocity.

Distance traveled differs from displacement when velocity changes sign. Break the interval at turning points to compute total distance.

\[\Delta s=\int v\,dt,\qquad \Delta v=\int a\,dt\]

![FIG-02-31-006: Aligned s-t, v-t, and a-t plots with slope/area relationships.](../figures/FIG-02-31-006-interpreting-motion-graphs.png)

### Worked Example 6

**Problem.** What is the area under an a-t curve?

**Solution.** Change in velocity.

---

## 31.7 Relative Rectilinear Motion

For particles A and B moving along the same line, relative position and velocity follow vector subtraction.

A positive \(v_{A/B}\) means A moves in the positive direction relative to B; closing speed must be interpreted from the chosen coordinate system.

\[s_{A/B}=s_A-s_B,\qquad v_{A/B}=v_A-v_B\]

![FIG-02-31-007: Two vehicles on one axis with absolute and relative positions/velocities.](../figures/FIG-02-31-007-relative-rectilinear-motion.png)

### Worked Example 7

**Problem.** What is the slope of an s-t curve?

**Solution.** Velocity.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** When is a=v dv/ds useful?

**Solution.** When acceleration is given as a function of position and time is absent.

### Worked Example 9

**Problem.** Two cars move +x at 20 and 15 m/s. Find vA/B if A is first.

**Solution.** 5 m/s.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Dynamics, printed pp. 102–106**.

**Source boundary:** The Handbook directly defines particle position, velocity, acceleration, rectilinear derivative relations, constant-acceleration equations, and nonconstant-acceleration integration.

---

## Where This Goes Wrong

**Applying rectilinear kinematics before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying constant acceleration before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying free fall before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying time-dependent acceleration before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying position-dependent acceleration before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying motion graphs before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying relative rectilinear motion before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| rectilinear kinematics | Concept developed in §31.1; apply only under that section's model assumptions. |
| constant acceleration | Concept developed in §31.2; apply only under that section's model assumptions. |
| free fall | Concept developed in §31.3; apply only under that section's model assumptions. |
| time-dependent acceleration | Concept developed in §31.4; apply only under that section's model assumptions. |
| position-dependent acceleration | Concept developed in §31.5; apply only under that section's model assumptions. |
| motion graphs | Concept developed in §31.6; apply only under that section's model assumptions. |
| relative rectilinear motion | Concept developed in §31.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **rectilinear kinematics** and state the governing relation or modeling rule.

2. Define **constant acceleration** and state the governing relation or modeling rule.

3. Define **free fall** and state the governing relation or modeling rule.

4. Define **time-dependent acceleration** and state the governing relation or modeling rule.

5. Define **position-dependent acceleration** and state the governing relation or modeling rule.

6. Define **motion graphs** and state the governing relation or modeling rule.

7. Define **relative rectilinear motion** and state the governing relation or modeling rule.

8. What error is likely if **rectilinear kinematics** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **constant acceleration** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **free fall** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **time-dependent acceleration** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **position-dependent acceleration** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **motion graphs** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **relative rectilinear motion** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **rectilinear kinematics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **constant acceleration**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **free fall**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **time-dependent acceleration**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **position-dependent acceleration**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **motion graphs**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **relative rectilinear motion**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **rectilinear kinematics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **constant acceleration**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **rectilinear kinematics** is developed in §31.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **constant acceleration** is developed in §31.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **free fall** is developed in §31.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **time-dependent acceleration** is developed in §31.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **position-dependent acceleration** is developed in §31.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **motion graphs** is developed in §31.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **relative rectilinear motion** is developed in §31.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **rectilinear kinematics**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **constant acceleration**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **free fall**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **time-dependent acceleration**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **position-dependent acceleration**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **motion graphs**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **relative rectilinear motion**.

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

1. A car starts at 5 m/s and accelerates at 2 m/s² for 4 s. Find final velocity.

2. For Problem 1, find displacement over 4 s.

3. An object is dropped from rest for 2 s. Find speed using g=9.81 m/s².

4. A particle has s=3t²+2t m. Find v and a.

5. If v changes sign during an interval, how should total distance be found?

6. What is the area under an a-t curve?

7. What is the slope of an s-t curve?

8. When is a=v dv/ds useful?

9. Two cars move +x at 20 and 15 m/s. Find vA/B if A is first.

10. Why are constant-acceleration equations invalid for arbitrary a(t)?


---

## Practice Problem Solutions

1. v=5+2(4)=13 m/s.

2. Δs=5(4)+0.5(2)(16)=36 m.

3. Speed=19.62 m/s downward.

4. v=6t+2 m/s; a=6 m/s².

5. Break at the turning point and sum absolute displacements.

6. Change in velocity.

7. Velocity.

8. When acceleration is given as a function of position and time is absent.

9. 5 m/s.

10. They were derived assuming a is constant.


---

## Quick Reference

**Handbook anchor:** Dynamics, printed pp. 102–106.

- **rectilinear kinematics:** Position, Displacement, Velocity, and Acceleration
- **constant acceleration:** Constant-Acceleration Equations
- **free fall:** Free Fall and Sign Convention
- **time-dependent acceleration:** Variable Acceleration as a Function of Time
- **position-dependent acceleration:** Acceleration as a Function of Position
- **motion graphs:** Interpreting Motion Graphs
- **relative rectilinear motion:** Relative Rectilinear Motion
---

## What's Next

**02-32 — Particle Kinematics — Curvilinear and Relative Motion**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor