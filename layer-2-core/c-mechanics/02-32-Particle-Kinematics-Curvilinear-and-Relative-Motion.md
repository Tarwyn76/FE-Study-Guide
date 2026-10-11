---
chapter: "02-32"
title: "Particle Kinematics — Curvilinear and Relative Motion"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-032-01, MECH-2C-032-02, MECH-2C-032-03, MECH-2C-032-04, MECH-2C-032-05, MECH-2C-032-06, MECH-2C-032-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-31 Rectilinear Kinematics · 01-13 Vectors

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly provides Cartesian, radial/transverse, normal/tangential, circular-motion, projectile, and relative-motion kinematic relations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **32.1** Explain and apply **Cartesian Curvilinear Motion**.
* **32.2** Explain and apply **Projectile Motion**.
* **32.3** Explain and apply **Normal and Tangential Coordinates**.
* **32.4** Explain and apply **Radial and Transverse Coordinates**.
* **32.5** Explain and apply **Plane Circular Motion**.
* **32.6** Explain and apply **Relative Motion with Translating Axes**.
* **32.7** Explain and apply **Choosing the Best Coordinate System**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 32.1 Cartesian Curvilinear Motion

For planar motion, position, velocity, and acceleration can be resolved into independent Cartesian components.

Different components may have different functional forms, but they share the same time variable.

\[\mathbf r=x\hat i+y\hat j,\quad\mathbf v=\dot x\hat i+\dot y\hat j,\quad\mathbf a=\ddot x\hat i+\ddot y\hat j\]

![FIG-02-32-001: Curved particle path with x-y position, velocity components, and acceleration components.](../figures/FIG-02-32-001-cartesian-curvilinear-motion.png)

### Worked Example 1

**Problem.** Projectile speed 20 m/s at 30°. Find horizontal and vertical initial components.

**Solution.** vx0=17.32 m/s; vy0=10.0 m/s. Reasoning: this uses the **32.1 Cartesian Curvilinear Motion** model from Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## 32.2 Projectile Motion

With negligible air resistance, projectile acceleration is zero horizontally and \(-g\) vertically for an upward-positive axis. Horizontal velocity remains constant.

Resolve the initial velocity first, then use the same time in both directions.

\[x=x_0+v_0\cos\theta\,t,\qquad y=y_0+v_0\sin\theta\,t-\tfrac12gt^2\]

![FIG-02-32-002: Projectile trajectory with initial speed/angle, constant horizontal velocity, and downward gravity.](../figures/FIG-02-32-002-projectile-motion.png)

### Worked Example 2

**Problem.** For Problem 1 from ground level, find time to return to same height with g=9.81.

**Solution.** t=2vy0/g=2.039 s. Reasoning: this uses the **32.2 Projectile Motion** model from Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## 32.3 Normal and Tangential Coordinates

For motion along a known curved path, tangential acceleration changes speed and normal acceleration changes direction.

The normal component points toward the instantaneous center of curvature.

\[a_t=\frac{dv}{dt},\qquad a_n=\frac{v^2}{\rho}\]

![FIG-02-32-003: Curved path with tangent et, inward normal en, velocity v, at and an.](../figures/FIG-02-32-003-normal-and-tangential-coordinates.png)

### Worked Example 3

**Problem.** A particle moves at 12 m/s on a path of radius 8 m. Find normal acceleration.

**Solution.** an=v²/ρ=144/8=18 m/s². Reasoning: this uses the **32.3 Normal and Tangential Coordinates** model from Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## 32.4 Radial and Transverse Coordinates

Polar coordinates are useful when geometry is referenced to an origin and both radial distance \(r\) and angle \(	heta\) can vary.

The acceleration includes coupling terms; radial acceleration is not simply \(\ddot r\) when angular motion exists.

\[\mathbf v=\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta\]\n\[\mathbf a=(\ddot r-r\dot\theta^2)\mathbf e_r+(r\ddot\theta+2\dot r\dot\theta)\mathbf e_\theta\]

![FIG-02-32-004: Particle in r-θ coordinates with er/eθ components and radial/transverse velocity and acceleration.](../figures/FIG-02-32-004-radial-and-transverse-coordinates.png)

### Worked Example 4

**Problem.** A wheel radius 0.4 m rotates at 10 rad/s. Find rim speed.

**Solution.** v=rω=4 m/s. Reasoning: this uses the **32.4 Radial and Transverse Coordinates** model from Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## 32.5 Plane Circular Motion

For constant radius \(r\), transverse speed is \(v=r\omega\), tangential acceleration is \(rlpha\), and inward radial acceleration is \(r\omega^2=v^2/r\).

Constant angular speed still produces acceleration because velocity direction changes continuously.

\[v=r\omega,\qquad a_t=r\alpha,\qquad a_n=r\omega^2\]

![FIG-02-32-005: Particle on circle with velocity tangent, tangential acceleration, and inward centripetal acceleration.](../figures/FIG-02-32-005-plane-circular-motion.png)

### Worked Example 5

**Problem.** For Problem 4 at constant ω, find inward acceleration.

**Solution.** an=rω²=0.4(100)=40 m/s². Reasoning: this uses the **32.5 Plane Circular Motion** model from Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## 32.6 Relative Motion with Translating Axes

For two particles observed in the same inertial frame,

\[
\mathbf r_A=\mathbf r_B+\mathbf r_{A/B}
\]

and differentiation gives relative velocity and acceleration relations for translating axes.

This is useful for moving-platform, vehicle, and mechanism problems.

\[\mathbf v_A=\mathbf v_B+\mathbf v_{A/B},\qquad \mathbf a_A=\mathbf a_B+\mathbf a_{A/B}\]

![FIG-02-32-006: Absolute and relative position/velocity vectors for particles A and B.](../figures/FIG-02-32-006-relative-motion-with-translating-axes.png)

### Worked Example 6

**Problem.** What does tangential acceleration change?

**Solution.** Speed magnitude. Reasoning: this uses the **32.6 Relative Motion with Translating Axes** model from Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## 32.7 Choosing the Best Coordinate System

Cartesian coordinates are best when acceleration components are simple in fixed axes. Normal-tangential coordinates are best when path geometry and speed are known. Polar coordinates are best when motion is naturally described by radius and angle.

Changing coordinates does not change the physics; it changes the algebra.

\[\text{choose coordinates to match geometry and known quantities}\]

![FIG-02-32-007: Decision tree choosing Cartesian, n-t, or r-θ coordinates based on problem data.](../figures/FIG-02-32-007-choosing-the-best-coordinate-system.png)

### Worked Example 7

**Problem.** What does normal acceleration change?

**Solution.** Velocity direction. Reasoning: this uses the **32.7 Choosing the Best Coordinate System** model from Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** State the radial velocity component in polar coordinates.

**Solution.** vr=rdot. Reasoning: this uses the **Integrated Worked Examples** model from Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

### Worked Example 9

**Problem.** Two particles have vA=(5,2), vB=(1,-1) m/s. Find vA/B.

**Solution.** (4,3) m/s. Reasoning: this uses the **Integrated Worked Examples** model from Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## As the Handbook States It

### Source Boundary

- **FE-Handbook-supported** — For concepts marked `in_handbook` in the ledger, the cited FE Reference Handbook section/page supplies the formula, table, definition, or exam-scope anchor used by this chapter.
- **Externally supported** — Engineering LibreTexts, Introductory Dynamics (Steeneken, Delft University of Technology) (https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Introductory_Dynamics%3A_2D_Kinematics_and_Kinetics_of_Point_Masses_and_Rigid_Bodies_%28Steeneken%29) supports curvilinear particle kinematics, coordinate-system selection, normal-tangential/polar descriptions, and relative motion.
- **Guide synthesis** — Worked-example sequencing, engineering interpretation, exam strategy, comparison heuristics, checklists, and explanatory derivations beyond the cited source statements are instructional synthesis developed for this guide.


Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Dynamics, printed pp. 102–106**.

**Source boundary:** The Handbook directly provides Cartesian, radial/transverse, normal/tangential, circular-motion, projectile, and relative-motion kinematic relations.

---

## Where This Goes Wrong

**Applying Cartesian kinematics before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying projectile motion before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying normal-tangential motion before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying polar kinematics before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying circular motion before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying relative motion before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying coordinate-system selection before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| Cartesian kinematics | Concept developed in §32.1; apply only under that section's model assumptions. |
| projectile motion | Concept developed in §32.2; apply only under that section's model assumptions. |
| normal-tangential motion | Concept developed in §32.3; apply only under that section's model assumptions. |
| polar kinematics | Concept developed in §32.4; apply only under that section's model assumptions. |
| circular motion | Concept developed in §32.5; apply only under that section's model assumptions. |
| relative motion | Concept developed in §32.6; apply only under that section's model assumptions. |
| coordinate-system selection | Concept developed in §32.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **Cartesian kinematics** and state the governing relation or modeling rule.

2. Define **projectile motion** and state the governing relation or modeling rule.

3. Define **normal-tangential motion** and state the governing relation or modeling rule.

4. Define **polar kinematics** and state the governing relation or modeling rule.

5. Define **circular motion** and state the governing relation or modeling rule.

6. Define **relative motion** and state the governing relation or modeling rule.

7. Define **coordinate-system selection** and state the governing relation or modeling rule.

8. What error is likely if **Cartesian kinematics** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **projectile motion** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **normal-tangential motion** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **polar kinematics** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **circular motion** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **relative motion** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **coordinate-system selection** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **Cartesian kinematics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **projectile motion**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **normal-tangential motion**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **polar kinematics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **circular motion**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **relative motion**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **coordinate-system selection**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **Cartesian kinematics**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **projectile motion**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **Cartesian kinematics** is developed in §32.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **projectile motion** is developed in §32.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **normal-tangential motion** is developed in §32.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **polar kinematics** is developed in §32.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **circular motion** is developed in §32.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **relative motion** is developed in §32.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **coordinate-system selection** is developed in §32.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **Cartesian kinematics**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **projectile motion**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **normal-tangential motion**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **polar kinematics**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **circular motion**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **relative motion**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **coordinate-system selection**.

15. Create the chapter-specific mechanics model for **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion** before solving: define the body or system, coordinates, geometry, loads, constraints, and unknowns that enter the governing equations.

16. Independently verify a result in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion** by substituting it back into the governing equation, checking units and signs, and testing equilibrium, compatibility, or a limiting case as appropriate.

17. A negative result reverses an assumed direction only when the physical element can act in that opposite sense. In **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**, also test whether unilateral contact, tension-only, or compression-only behavior changes the model.

18. Match the Handbook coordinate and sign convention before comparing expressions in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. A different positive direction can reverse component or moment signs while leaving the physical state unchanged.

19. **A.** The nineteenth review item tests **Cartesian kinematics** in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

20. **A.** The twentieth review item tests **projectile motion** in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

21. **A.** The twenty-first review item tests **normal-tangential motion** in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

22. **A.** The twenty-second review item tests **polar kinematics** in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

23. **A.** The twenty-third review item tests **circular motion** in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

24. **A.** The twenty-fourth review item tests **relative motion** in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

25. **A.** The twenty-fifth review item tests **coordinate-system selection** in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

26. **A.** The twenty-sixth review item tests **Cartesian kinematics** in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention. This application check also tests whether the model assumptions are established before any numerical or symbolic manipulation.

27. **A.** The twenty-seventh review item tests **projectile motion** in **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention. This final application check emphasizes that a valid mechanics relation cannot replace the diagram, geometry, and constraints that define the problem.

---

## Practice Problems

1. Projectile speed 20 m/s at 30°. Find horizontal and vertical initial components.

2. For Problem 1 from ground level, find time to return to same height with g=9.81.

3. A particle moves at 12 m/s on a path of radius 8 m. Find normal acceleration.

4. A wheel radius 0.4 m rotates at 10 rad/s. Find rim speed.

5. For Problem 4 at constant ω, find inward acceleration.

6. What does tangential acceleration change?

7. What does normal acceleration change?

8. State the radial velocity component in polar coordinates.

9. Two particles have vA=(5,2), vB=(1,-1) m/s. Find vA/B.

10. Which coordinates are usually best when speed and path radius are known?


---

## Practice Problem Solutions

1. vx0=17.32 m/s; vy0=10.0 m/s.

2. t=2vy0/g=2.039 s. Practice verification: use the **32.2 Projectile Motion** relation for Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

3. an=v²/ρ=144/8=18 m/s².

4. v=rω=4 m/s. Practice verification: use the **32.4 Radial and Transverse Coordinates** relation for Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

5. an=rω²=0.4(100)=40 m/s².

6. Speed magnitude. Practice verification: use the **32.6 Relative Motion with Translating Axes** relation for Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

7. Velocity direction. Practice verification: use the **32.7 Choosing the Best Coordinate System** relation for Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

8. vr=rdot. Practice verification: use the **Integrated Worked Examples** relation for Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

9. (4,3) m/s. Practice verification: use the **Integrated Worked Examples** relation for Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

10. Normal-tangential coordinates. Practice verification: use the **Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion** relation for Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

---

## Quick Reference

**Handbook anchor:** Dynamics, printed pp. 102–106.

- **Cartesian kinematics:** Cartesian Curvilinear Motion
- **projectile motion:** Projectile Motion
- **normal-tangential motion:** Normal and Tangential Coordinates
- **polar kinematics:** Radial and Transverse Coordinates
- **circular motion:** Plane Circular Motion
- **relative motion:** Relative Motion with Translating Axes
- **coordinate-system selection:** Choosing the Best Coordinate System
---

## What's Next

**02-33 — Particle Kinetics — Force and Acceleration**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor