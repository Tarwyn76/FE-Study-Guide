---
chapter: "02-38"
title: "Torsion"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-038-01, MECH-2C-038-02, MECH-2C-038-03, MECH-2C-038-04, MECH-2C-038-05, MECH-2C-038-06, MECH-2C-038-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-38: Torsion

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-29 Area Moments · 02-37 Stress/Strain

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives circular-shaft torsional stress, shear-strain distribution, angle-of-twist relation, torsional stiffness, and thin-walled hollow-shaft stress.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **38.1** Explain and apply **Torque and Internal Torsional Moment**.
* **38.2** Explain and apply **Polar Moment for Circular Shafts**.
* **38.3** Explain and apply **Torsional Shear Stress**.
* **38.4** Explain and apply **Angle of Twist**.
* **38.5** Explain and apply **Torsional Stiffness**.
* **38.6** Explain and apply **Power Transmission by Rotating Shafts**.
* **38.7** Explain and apply **Thin-Walled Closed Circular Tubes**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 38.1 Torque and Internal Torsional Moment

A shaft transmits torque when external couples create an internal twisting moment. Use a cut and moment equilibrium about the shaft axis to determine internal torque \(T\).

Torque sign may change between applied couples, so construct a torque diagram for multi-segment shafts.

\[\sum M_{\rm axis}=0\Rightarrow T_{\rm internal}\]

![FIG-02-38-001: Shaft with applied torques, section cut, and internal torque T.](../figures/FIG-02-38-001-torque-and-internal-torsional-moment.png)

### Worked Example 1

**Problem.** Find J for a solid shaft d=40 mm.

**Solution.** J=πd^4/32=2.513×10^-7 m^4.

---

## 38.2 Polar Moment for Circular Shafts

Circular-shaft torsion uses the polar area moment \(J\). For a solid circular shaft and a hollow circular shaft,

\[
J_{m solid}=rac{\pi d^4}{32},\qquad
J_{m hollow}=rac{\pi(d_o^4-d_i^4)}{32}.
\]

Because diameter appears to the fourth power, modest diameter changes strongly affect torsional stiffness and stress.

\[J=\int r^2dA\]

![FIG-02-38-002: Solid and hollow circular cross-sections with radii and polar moment formulas.](../figures/FIG-02-38-002-polar-moment-for-circular-shafts.png)

### Worked Example 2

**Problem.** For Problem 1 with T=500 N·m, find τmax.

**Solution.** τ=Tc/J=500(0.02)/2.513e-7=39.8 MPa.

---

## 38.3 Torsional Shear Stress

For linear elastic circular-shaft torsion,

\[
	au(r)=rac{Tr}{J}.
\]

Stress is zero at the center and maximum at the outer radius \(c\).

\[\tau_{\max}=\frac{Tc}{J}\]

![FIG-02-38-003: Circular shaft cross-section with linear shear-stress distribution from center to surface.](../figures/FIG-02-38-003-torsional-shear-stress.png)

### Worked Example 3

**Problem.** For T=500 N·m, L=1 m, G=80 GPa, J as Problem 1, find twist.

**Solution.** φ=TL/GJ=0.02487 rad=1.425°.

---

## 38.4 Angle of Twist

The Handbook gives angle of twist for a uniform segment as

\[
\phi=rac{TL}{GJ}.
\]

For stepped shafts, sum signed segment twists. Compatibility may impose a specified total twist.

\[\phi=\int\frac{T(x)}{G(x)J(x)}dx\]

![FIG-02-38-004: Stepped shaft with segment torques, lengths, G, J, and accumulated angle of twist.](../figures/FIG-02-38-004-angle-of-twist.png)

### Worked Example 4

**Problem.** If diameter doubles under same torque, by what factor does solid-shaft τmax change?

**Solution.** τmax∝1/d^3, so it becomes 1/8.

---

## 38.5 Torsional Stiffness

Torsional stiffness is torque per radian of twist.

For a uniform prismatic shaft,

\[
k_t=rac{T}{\phi}=rac{GJ}{L}.
\]

Longer shafts are more flexible; larger \(G\) or \(J\) increases stiffness.

\[k_t=\frac{GJ}{L}\]

![FIG-02-38-005: Two shafts comparing effects of length and diameter on twist under equal torque.](../figures/FIG-02-38-005-torsional-stiffness.png)

### Worked Example 5

**Problem.** If diameter doubles, by what factor does torsional stiffness GJ/L change?

**Solution.** J∝d^4, so stiffness increases by 16.

---

## 38.6 Power Transmission by Rotating Shafts

Rotational mechanical power is

\[
P=T\omega.
\]

This lets you find required torque from power and rotational speed before sizing a shaft for stress and twist.

\[P=T\omega\]

![FIG-02-38-006: Motor-shaft-load system with torque T, speed ω, and transmitted power P.](../figures/FIG-02-38-006-power-transmission-by-rotating-shafts.png)

### Worked Example 6

**Problem.** A shaft transmits 10 kW at 100 rad/s. Find torque.

**Solution.** T=P/ω=100 N·m.

---

## 38.7 Thin-Walled Closed Circular Tubes

For a thin-walled closed circular shaft, the Handbook gives a membrane-like shear-stress relation involving mean enclosed area and wall thickness.

Use thin-wall formulas only when wall thickness is small relative to radius; otherwise use the thick/solid circular-shaft relation.

\[\tau=\frac{T}{2A_m t}\]

![FIG-02-38-007: Thin-walled circular tube with mean area Am, wall thickness t, and shear flow around perimeter.](../figures/FIG-02-38-007-thin-walled-closed-circular-tubes.png)

### Worked Example 7

**Problem.** What is shear stress at center of a solid circular shaft in elastic torsion?

**Solution.** Zero.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** State J for a hollow circular shaft.

**Solution.** J=π(do^4−di^4)/32.

### Worked Example 9

**Problem.** What is torsional stiffness of a uniform shaft?

**Solution.** kt=GJ/L.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Mechanics of Materials, printed pp. 134–135**.

**Source boundary:** The Handbook directly gives circular-shaft torsional stress, shear-strain distribution, angle-of-twist relation, torsional stiffness, and thin-walled hollow-shaft stress.

---

## Where This Goes Wrong

**Applying internal torque before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying shaft polar moment before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying torsional shear stress before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying angle of twist before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying torsional stiffness before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying shaft power before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying thin-wall torsion before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.

**Mixing area and mass moments of inertia.** They have different units and different physical roles.


---

## Key Terms

| Term | Working definition |
|---|---|
| internal torque | Concept developed in §38.1; apply only under that section's model assumptions. |
| shaft polar moment | Concept developed in §38.2; apply only under that section's model assumptions. |
| torsional shear stress | Concept developed in §38.3; apply only under that section's model assumptions. |
| angle of twist | Concept developed in §38.4; apply only under that section's model assumptions. |
| torsional stiffness | Concept developed in §38.5; apply only under that section's model assumptions. |
| shaft power | Concept developed in §38.6; apply only under that section's model assumptions. |
| thin-wall torsion | Concept developed in §38.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **internal torque** and state the governing relation or modeling rule.

2. Define **shaft polar moment** and state the governing relation or modeling rule.

3. Define **torsional shear stress** and state the governing relation or modeling rule.

4. Define **angle of twist** and state the governing relation or modeling rule.

5. Define **torsional stiffness** and state the governing relation or modeling rule.

6. Define **shaft power** and state the governing relation or modeling rule.

7. Define **thin-wall torsion** and state the governing relation or modeling rule.

8. What error is likely if **internal torque** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **shaft polar moment** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **torsional shear stress** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **angle of twist** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **torsional stiffness** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **shaft power** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **thin-wall torsion** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **internal torque**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **shaft polar moment**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **torsional shear stress**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **angle of twist**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **torsional stiffness**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **shaft power**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **thin-wall torsion**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **internal torque**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **shaft polar moment**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **internal torque** is developed in §38.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **shaft polar moment** is developed in §38.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **torsional shear stress** is developed in §38.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **angle of twist** is developed in §38.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **torsional stiffness** is developed in §38.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **shaft power** is developed in §38.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **thin-wall torsion** is developed in §38.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **internal torque**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **shaft polar moment**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **torsional shear stress**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **angle of twist**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **torsional stiffness**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **shaft power**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **thin-wall torsion**.

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

1. Find J for a solid shaft d=40 mm.

2. For Problem 1 with T=500 N·m, find τmax.

3. For T=500 N·m, L=1 m, G=80 GPa, J as Problem 1, find twist.

4. If diameter doubles under same torque, by what factor does solid-shaft τmax change?

5. If diameter doubles, by what factor does torsional stiffness GJ/L change?

6. A shaft transmits 10 kW at 100 rad/s. Find torque.

7. What is shear stress at center of a solid circular shaft in elastic torsion?

8. State J for a hollow circular shaft.

9. What is torsional stiffness of a uniform shaft?

10. When is τ=T/(2Am t) appropriate?


---

## Practice Problem Solutions

1. J=πd^4/32=2.513×10^-7 m^4.

2. τ=Tc/J=500(0.02)/2.513e-7=39.8 MPa.

3. φ=TL/GJ=0.02487 rad=1.425°.

4. τmax∝1/d^3, so it becomes 1/8.

5. J∝d^4, so stiffness increases by 16.

6. T=P/ω=100 N·m.

7. Zero.

8. J=π(do^4−di^4)/32.

9. kt=GJ/L.

10. For a thin-walled closed circular tube under the Handbook model.


---

## Quick Reference

**Handbook anchor:** Mechanics of Materials, printed pp. 134–135.

- **internal torque:** Torque and Internal Torsional Moment
- **shaft polar moment:** Polar Moment for Circular Shafts
- **torsional shear stress:** Torsional Shear Stress
- **angle of twist:** Angle of Twist
- **torsional stiffness:** Torsional Stiffness
- **shaft power:** Power Transmission by Rotating Shafts
- **thin-wall torsion:** Thin-Walled Closed Circular Tubes
---

## What's Next

**02-39 — Beams — Shear, Moment, Bending, and Deflection**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor