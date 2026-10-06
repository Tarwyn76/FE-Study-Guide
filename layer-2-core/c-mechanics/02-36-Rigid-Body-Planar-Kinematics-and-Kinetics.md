---
chapter: "02-36"
title: "Rigid-Body Planar Kinematics and Kinetics"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-036-01, MECH-2C-036-02, MECH-2C-036-03, MECH-2C-036-04, MECH-2C-036-05, MECH-2C-036-06, MECH-2C-036-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-36: Rigid-Body Planar Kinematics and Kinetics

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-32 Curvilinear Kinematics · 02-35 Momentum

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives plane rigid-body equations of motion, fixed-axis rotational kinematics, instantaneous centers, mass moments of inertia, parallel-axis theorem, kinetic energy, and angular impulse-momentum.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **36.1** Explain and apply **Translation and Rotation of a Rigid Body**.
* **36.2** Explain and apply **Relative Acceleration on a Rigid Body**.
* **36.3** Explain and apply **Fixed-Axis Rotation**.
* **36.4** Explain and apply **Instantaneous Center of Zero Velocity**.
* **36.5** Explain and apply **Mass Moment of Inertia**.
* **36.6** Explain and apply **Rigid-Body Equations of Motion**.
* **36.7** Explain and apply **Rigid-Body Energy and Angular Momentum**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 36.1 Translation and Rotation of a Rigid Body

In plane motion, a rigid body's motion can be decomposed into translation of a reference point plus rotation about that point. Distances between material points remain constant.

Pure translation has the same velocity and acceleration for all points at an instant; general plane motion does not.

\[\mathbf v_B=\mathbf v_A+\boldsymbol\omega\times\mathbf r_{B/A}\]

![FIG-02-36-001: Rigid body with points A and B, translational velocity at A and rotational contribution at B.](../figures/FIG-02-36-001-translation-and-rotation-of-a-rigid-body.png)

### Worked Example 1

**Problem.** A point on a disk radius 0.5 m rotates at 8 rad/s. Find speed.

**Solution.** v=rω=4 m/s.

---

## 36.2 Relative Acceleration on a Rigid Body

For two points fixed in the same rigid body,

\[
\mathbf a_B=\mathbf a_A+oldsymbollpha	imes\mathbf r_{B/A}+oldsymbol\omega	imes(oldsymbol\omega	imes\mathbf r_{B/A}).
\]

The tangential term depends on angular acceleration; the normal term points toward the rotation center relative to A.

\[\mathbf a_B=\mathbf a_A+\boldsymbol\alpha\times\mathbf r_{B/A}-\omega^2\mathbf r_{B/A}\]

![FIG-02-36-002: Rigid link AB with tangential and normal relative acceleration components at B.](../figures/FIG-02-36-002-relative-acceleration-on-a-rigid-body.png)

### Worked Example 2

**Problem.** Same disk has α=3 rad/s². Find tangential acceleration at rim.

**Solution.** at=rα=1.5 m/s².

---

## 36.3 Fixed-Axis Rotation

For rotation about a fixed axis, angular position, velocity, and acceleration obey the same constant-acceleration structure as rectilinear motion when \(lpha\) is constant.

Point speed grows linearly with radius.

\[\omega=\omega_0+\alpha t,\qquad \theta=\theta_0+\omega_0t+\tfrac12\alpha t^2,\qquad v=r\omega\]

![FIG-02-36-003: Disk rotating about fixed axis with angular variables and point velocity.](../figures/FIG-02-36-003-fixed-axis-rotation.png)

### Worked Example 3

**Problem.** Find normal acceleration at rim for Problem 1.

**Solution.** an=rω²=0.5(64)=32 m/s².

---

## 36.4 Instantaneous Center of Zero Velocity

In general plane motion, there is often an instantaneous center about which the body is momentarily rotating. Velocities are perpendicular to lines from the instant center and have magnitude \(v=\omega r\).

The instantaneous center is a velocity construction, not generally a zero-acceleration point.

\[v_P=\omega r_{P/IC}\]

![FIG-02-36-004: Rigid link with velocities at two points and perpendicular lines locating the instantaneous center.](../figures/FIG-02-36-004-instantaneous-center-of-zero-velocity.png)

### Worked Example 4

**Problem.** A solid disk has m=10 kg, I_G=0.5mr² with r=0.4 m. Find I_G.

**Solution.** I=0.5(10)(0.16)=0.8 kg·m².

---

## 36.5 Mass Moment of Inertia

Mass moment of inertia measures rotational inertia about an axis.

The Handbook gives the mass parallel-axis theorem for shifting from a centroidal axis to a parallel axis.

\[I=\int r^2\,dm,\qquad I_O=I_G+md^2\]

![FIG-02-36-005: Rigid body mass distribution with centroidal axis G and shifted parallel axis O.](../figures/FIG-02-36-005-mass-moment-of-inertia.png)

### Worked Example 5

**Problem.** Shift the inertia in Problem 4 to a parallel axis 0.3 m away.

**Solution.** I=0.8+10(0.3²)=1.7 kg·m².

---

## 36.6 Rigid-Body Equations of Motion

For planar motion of a rigid body, translation of the mass center and rotation about the mass center satisfy

\[
\sum F_x=ma_{Gx},\quad \sum F_y=ma_{Gy},\quad \sum M_G=I_Glpha.
\]

The force and moment equations are coupled through the body's constraints and geometry.

\[\sum\mathbf F=m\mathbf a_G,\qquad \sum M_G=I_G\alpha\]

![FIG-02-36-006: Rigid body FBD with mass-center acceleration and angular acceleration.](../figures/FIG-02-36-006-rigid-body-equations-of-motion.png)

### Worked Example 6

**Problem.** A body has m=5 kg, vG=2 m/s, IG=0.4 kg·m², ω=3 rad/s. Find kinetic energy.

**Solution.** T=0.5(5)(4)+0.5(0.4)(9)=11.8 J.

---

## 36.7 Rigid-Body Energy and Angular Momentum

The Handbook gives planar rigid-body kinetic energy as translation of the mass center plus rotation about the mass center.

Angular impulse-momentum can be written about the mass center or another suitable point with the corresponding inertia and moment definitions.

\[T=\tfrac12mv_G^2+\tfrac12I_G\omega^2\]

![FIG-02-36-007: Rigid body with translational velocity vG and angular speed ω contributing to total kinetic energy.](../figures/FIG-02-36-007-rigid-body-energy-and-angular-momentum.png)

### Worked Example 7

**Problem.** Is an instantaneous center generally a zero-acceleration point?

**Solution.** No; it is a zero-velocity point at that instant.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** State the planar rotational equation about G.

**Solution.** ΣM_G=I_G α.

### Worked Example 9

**Problem.** How many instant centers exist for n links?

**Solution.** n(n−1)/2.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Dynamics, printed pp. 110–112**.

**Source boundary:** The Handbook directly gives plane rigid-body equations of motion, fixed-axis rotational kinematics, instantaneous centers, mass moments of inertia, parallel-axis theorem, kinetic energy, and angular impulse-momentum.

---

## Where This Goes Wrong

**Applying rigid-body kinematics before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying rigid-body acceleration before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying fixed-axis rotation before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying instantaneous center before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying mass moment of inertia before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying rigid-body kinetics before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying rigid-body energy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.

**Mixing area and mass moments of inertia.** They have different units and different physical roles.


---

## Key Terms

| Term | Working definition |
|---|---|
| rigid-body kinematics | Concept developed in §36.1; apply only under that section's model assumptions. |
| rigid-body acceleration | Concept developed in §36.2; apply only under that section's model assumptions. |
| fixed-axis rotation | Concept developed in §36.3; apply only under that section's model assumptions. |
| instantaneous center | Concept developed in §36.4; apply only under that section's model assumptions. |
| mass moment of inertia | Concept developed in §36.5; apply only under that section's model assumptions. |
| rigid-body kinetics | Concept developed in §36.6; apply only under that section's model assumptions. |
| rigid-body energy | Concept developed in §36.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **rigid-body kinematics** and state the governing relation or modeling rule.

2. Define **rigid-body acceleration** and state the governing relation or modeling rule.

3. Define **fixed-axis rotation** and state the governing relation or modeling rule.

4. Define **instantaneous center** and state the governing relation or modeling rule.

5. Define **mass moment of inertia** and state the governing relation or modeling rule.

6. Define **rigid-body kinetics** and state the governing relation or modeling rule.

7. Define **rigid-body energy** and state the governing relation or modeling rule.

8. What error is likely if **rigid-body kinematics** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **rigid-body acceleration** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **fixed-axis rotation** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **instantaneous center** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **mass moment of inertia** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **rigid-body kinetics** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **rigid-body energy** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **rigid-body kinematics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **rigid-body acceleration**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **fixed-axis rotation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **instantaneous center**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **mass moment of inertia**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **rigid-body kinetics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **rigid-body energy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **rigid-body kinematics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **rigid-body acceleration**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **rigid-body kinematics** is developed in §36.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **rigid-body acceleration** is developed in §36.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **fixed-axis rotation** is developed in §36.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **instantaneous center** is developed in §36.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **mass moment of inertia** is developed in §36.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **rigid-body kinetics** is developed in §36.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **rigid-body energy** is developed in §36.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **rigid-body kinematics**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **rigid-body acceleration**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **fixed-axis rotation**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **instantaneous center**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **mass moment of inertia**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **rigid-body kinetics**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **rigid-body energy**.

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

1. A point on a disk radius 0.5 m rotates at 8 rad/s. Find speed.

2. Same disk has α=3 rad/s². Find tangential acceleration at rim.

3. Find normal acceleration at rim for Problem 1.

4. A solid disk has m=10 kg, I_G=0.5mr² with r=0.4 m. Find I_G.

5. Shift the inertia in Problem 4 to a parallel axis 0.3 m away.

6. A body has m=5 kg, vG=2 m/s, IG=0.4 kg·m², ω=3 rad/s. Find kinetic energy.

7. Is an instantaneous center generally a zero-acceleration point?

8. State the planar rotational equation about G.

9. How many instant centers exist for n links?

10. What does rigid-body motion preserve?


---

## Practice Problem Solutions

1. v=rω=4 m/s.

2. at=rα=1.5 m/s².

3. an=rω²=0.5(64)=32 m/s².

4. I=0.5(10)(0.16)=0.8 kg·m².

5. I=0.8+10(0.3²)=1.7 kg·m².

6. T=0.5(5)(4)+0.5(0.4)(9)=11.8 J.

7. No; it is a zero-velocity point at that instant.

8. ΣM_G=I_G α.

9. n(n−1)/2.

10. Distance between every pair of material points.


---

## Quick Reference

**Handbook anchor:** Dynamics, printed pp. 110–112.

- **rigid-body kinematics:** Translation and Rotation of a Rigid Body
- **rigid-body acceleration:** Relative Acceleration on a Rigid Body
- **fixed-axis rotation:** Fixed-Axis Rotation
- **instantaneous center:** Instantaneous Center of Zero Velocity
- **mass moment of inertia:** Mass Moment of Inertia
- **rigid-body kinetics:** Rigid-Body Equations of Motion
- **rigid-body energy:** Rigid-Body Energy and Angular Momentum
---

## What's Next

**02-37 — Stress, Strain, and Axial/Thermal Deformation**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor