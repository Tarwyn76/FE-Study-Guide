---
chapter: "02-40"
title: "Combined Stress, Principal Stress, and Mohr's Circle"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-040-01, MECH-2C-040-02, MECH-2C-040-03, MECH-2C-040-04, MECH-2C-040-05, MECH-2C-040-06, MECH-2C-040-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-37 Axial Stress · 02-38 Torsion · 02-39 Beam Stress

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives 2D principal-stress equations, Mohr's-circle construction/sign convention, maximum in-plane and 3D shear concepts, and plane-stress Hooke's law.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **40.1** Explain and apply **Combined Normal and Shear Stress States**.
* **40.2** Explain and apply **Stress Transformation**.
* **40.3** Explain and apply **Principal Stresses**.
* **40.4** Explain and apply **Maximum In-Plane Shear Stress**.
* **40.5** Explain and apply **Constructing Mohr's Circle**.
* **40.6** Explain and apply **Principal-Plane Orientation**.
* **40.7** Explain and apply **Plane Stress, 3D Shear, and Constitutive Check**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 40.1 Combined Normal and Shear Stress States

At a point in a loaded member, axial force, bending, torsion, and transverse shear may contribute simultaneously. Under linear elasticity, stress components from admissible load effects can be superposed at the same point.

The result is a stress element described by \(\sigma_x,\sigma_y,	au_{xy}\) for plane stress.

\[\sigma_x=\sum \sigma_{x,i},\qquad \tau_{xy}=\sum\tau_{xy,i}\]

![FIG-02-40-001: 2D stress element showing positive σx, σy, and τxy components.](../figures/FIG-02-40-001-combined-normal-and-shear-stress-states.png)

### Worked Example 1

**Problem.** Given σx=80 MPa, σy=20 MPa, τxy=30 MPa, find circle center C.

**Solution.** C=(80+20)/2=50 MPa. Reasoning: this uses the **40.1 Combined Normal and Shear Stress States** model from Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

<!-- VERIFY id="WE-02-40-001-center" expr="(80+20)/2" expected="50" units="MPa" atol="1e-9" rtol="1e-9" -->

## 40.2 Stress Transformation

Normal and shear stress on a rotated plane depend on orientation. The transformation equations can be evaluated directly or represented geometrically by Mohr's circle.

Principal planes are orientations where in-plane shear stress is zero.

\[\sigma_{x'}=\frac{\sigma_x+\sigma_y}{2}+\frac{\sigma_x-\sigma_y}{2}\cos2\theta+\tau_{xy}\sin2\theta\]

![FIG-02-40-002: Stress element rotated by θ with transformed normal/shear stresses.](../figures/FIG-02-40-002-stress-transformation.png)

### Worked Example 2

**Problem.** For Problem 1, find radius R.

**Solution.** R=sqrt(30²+30²)=42.43 MPa. Reasoning: this uses the **40.2 Stress Transformation** model from Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

<!-- VERIFY id="WE-02-40-002-radius" expr="sqrt(((80-20)/2)**2+30**2)" expected="42.43" units="MPa" atol="0.005" rtol="1e-9" -->

## 40.3 Principal Stresses

For plane stress, the principal stresses are the center of Mohr's circle plus or minus its radius.

They are the algebraically maximum and minimum normal stresses in the plane.

\[\sigma_{1,2}=\frac{\sigma_x+\sigma_y}{2}\pm\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}\]

![FIG-02-40-003: Plane-stress components mapped to principal stress values σ1 and σ2.](../figures/FIG-02-40-003-principal-stresses.png)

### Worked Example 3

**Problem.** Find principal stresses for Problem 1.

**Solution.** σ1=92.43 MPa, σ2=7.57 MPa. Reasoning: this uses the **40.3 Principal Stresses** model from Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

<!-- VERIFY id="WE-02-40-003-sigma1" expr="(80+20)/2+sqrt(((80-20)/2)**2+30**2)" expected="92.43" units="MPa" atol="0.005" rtol="1e-9" -->
<!-- VERIFY id="WE-02-40-003-sigma2" expr="(80+20)/2-sqrt(((80-20)/2)**2+30**2)" expected="7.57" units="MPa" atol="0.005" rtol="1e-9" -->

## 40.4 Maximum In-Plane Shear Stress

The maximum in-plane shear stress equals the radius of Mohr's circle.

The corresponding normal stress on those planes equals the circle center.

\[\tau_{\max,\rm in}=\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}\]

![FIG-02-40-004: Stress element oriented for maximum in-plane shear with accompanying average normal stress.](../figures/FIG-02-40-004-maximum-in-plane-shear-stress.png)

### Worked Example 4

**Problem.** Find maximum in-plane shear for Problem 1.

**Solution.** τmax,in=42.43 MPa. Reasoning: this uses the **40.4 Maximum In-Plane Shear Stress** model from Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

<!-- VERIFY id="WE-02-40-004-taumax-in" expr="sqrt(((80-20)/2)**2+30**2)" expected="42.43" units="MPa" atol="0.005" rtol="1e-9" -->

## 40.5 Constructing Mohr's Circle

The Handbook specifies the Mohr's-circle stress sign convention. Plot the two perpendicular-face stress points, locate the center on the normal-stress axis, compute radius, and read principal stresses and maximum in-plane shear.

Physical-plane rotation angle \(	heta\) corresponds to \(2	heta\) around Mohr's circle.

\[C=\frac{\sigma_x+\sigma_y}{2},\qquad R=\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}\]

![FIG-02-40-005: Mohr's circle with points for x/y faces, center C, radius R, principal stresses, and max shear.](../figures/FIG-02-40-005-constructing-mohr-s-circle.png)

### Worked Example 5

**Problem.** For plane stress, what is the third principal stress before ordering?

**Solution.** 0. Reasoning: this uses the **40.5 Constructing Mohr's Circle** model from Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## 40.6 Principal-Plane Orientation

Principal-plane orientation can be found from stress-transformation relations. A common relation is

\[
	an2	heta_p=rac{2	au_{xy}}{\sigma_x-\sigma_y}.
\]

Quadrant-aware evaluation is essential. Mohr's circle provides a geometric check of the angle.

\[\tan2\theta_p=\frac{2\tau_{xy}}{\sigma_x-\sigma_y}\]

![FIG-02-40-006: Physical stress element and corresponding doubled angle on Mohr's circle.](../figures/FIG-02-40-006-principal-plane-orientation.png)

### Worked Example 6

**Problem.** Using principal values 92.43, 7.57, 0 MPa, find absolute maximum 3D shear.

**Solution.** (92.43-0)/2=46.22 MPa. Reasoning: this uses the **40.6 Principal-Plane Orientation** model from Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

<!-- VERIFY id="WE-02-40-006-taumax-3d" expr="(92.43-0)/2" expected="46.22" units="MPa" atol="0.0051" rtol="1e-9" -->

## 40.7 Plane Stress, 3D Shear, and Constitutive Check

In plane stress, the third principal stress is \(\sigma_3=0\) before ordering. The absolute maximum shear stress in three dimensions depends on the largest separation among all three principal stresses.

The Handbook also gives plane-stress Hooke's-law relations, linking the transformed stress state to strains for isotropic linear elastic material.

\[\tau_{\max,3D}=\frac{\sigma_{\max}-\sigma_{\min}}{2}\]

![FIG-02-40-007: Three principal stresses on a number line showing absolute maximum shear as half the largest separation.](../figures/FIG-02-40-007-plane-stress-3d-shear-and-constitutive-check.png)

### Worked Example 7

**Problem.** What stress exists on a principal plane?

**Solution.** Normal principal stress with zero in-plane shear. Reasoning: this uses the **40.7 Plane Stress, 3D Shear, and Constitutive Check** model from Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What is the angle relationship between physical rotation and Mohr-circle rotation?

**Solution.** Mohr-circle angle is twice the physical-plane angle, with sign interpretation following the chosen convention. Reasoning: this uses the **Integrated Worked Examples** model from Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

### Worked Example 9

**Problem.** Why must σ3=0 be included in absolute max-shear evaluation for plane stress?

**Solution.** Because the largest principal-stress separation may involve the out-of-plane zero stress. Reasoning: this uses the **Integrated Worked Examples** model from Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## As the Handbook States It

### Source Boundary

- **FE-Handbook-supported** — For concepts marked `in_handbook` in the ledger, the cited FE Reference Handbook section/page supplies the formula, table, definition, or exam-scope anchor used by this chapter.
- **Externally supported** — Engineering LibreTexts, Mechanics of Materials (Roylance) (https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_of_Materials_%28Roylance%29) supports combined stress, plane-stress transformation, principal stresses/orientation, maximum shear, Mohr’s circle, and constitutive checks.
- **Guide synthesis** — Worked-example sequencing, engineering interpretation, exam strategy, comparison heuristics, checklists, and explanatory derivations beyond the cited source statements are instructional synthesis developed for this guide.


Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Mechanics of Materials, printed pp. 132–134**.

**Source boundary:** The Handbook directly gives 2D principal-stress equations, Mohr's-circle construction/sign convention, maximum in-plane and 3D shear concepts, and plane-stress Hooke's law.

---

## Where This Goes Wrong

**Applying plane stress state before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying stress transformation before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying principal stress before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying maximum in-plane shear before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying Mohr circle before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying principal orientation before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying absolute maximum shear before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| plane stress state | Concept developed in §40.1; apply only under that section's model assumptions. |
| stress transformation | Concept developed in §40.2; apply only under that section's model assumptions. |
| principal stress | Concept developed in §40.3; apply only under that section's model assumptions. |
| maximum in-plane shear | Concept developed in §40.4; apply only under that section's model assumptions. |
| Mohr circle | Concept developed in §40.5; apply only under that section's model assumptions. |
| principal orientation | Concept developed in §40.6; apply only under that section's model assumptions. |
| absolute maximum shear | Concept developed in §40.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **plane stress state** and state the governing relation or modeling rule.

2. Define **stress transformation** and state the governing relation or modeling rule.

3. Define **principal stress** and state the governing relation or modeling rule.

4. Define **maximum in-plane shear** and state the governing relation or modeling rule.

5. Define **Mohr circle** and state the governing relation or modeling rule.

6. Define **principal orientation** and state the governing relation or modeling rule.

7. Define **absolute maximum shear** and state the governing relation or modeling rule.

8. What error is likely if **plane stress state** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **stress transformation** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **principal stress** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **maximum in-plane shear** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **Mohr circle** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **principal orientation** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **absolute maximum shear** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **plane stress state**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **stress transformation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **principal stress**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **maximum in-plane shear**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **Mohr circle**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **principal orientation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **absolute maximum shear**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **plane stress state**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **stress transformation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **plane stress state** is developed in §40.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **stress transformation** is developed in §40.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **principal stress** is developed in §40.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **maximum in-plane shear** is developed in §40.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **Mohr circle** is developed in §40.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **principal orientation** is developed in §40.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **absolute maximum shear** is developed in §40.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **plane stress state**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **stress transformation**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **principal stress**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **maximum in-plane shear**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **Mohr circle**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **principal orientation**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **absolute maximum shear**.

15. Create the chapter-specific mechanics model for **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle** before solving: define the body or system, coordinates, geometry, loads, constraints, and unknowns that enter the governing equations.

16. Independently verify a result in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle** by substituting it back into the governing equation, checking units and signs, and testing equilibrium, compatibility, or a limiting case as appropriate.

17. A negative result reverses an assumed direction only when the physical element can act in that opposite sense. In **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**, also test whether unilateral contact, tension-only, or compression-only behavior changes the model.

18. Match the Handbook coordinate and sign convention before comparing expressions in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. A different positive direction can reverse component or moment signs while leaving the physical state unchanged.

19. **A.** The nineteenth review item tests **plane stress state** in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

20. **A.** The twentieth review item tests **stress transformation** in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

21. **A.** The twenty-first review item tests **principal stress** in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

22. **A.** The twenty-second review item tests **maximum in-plane shear** in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

23. **A.** The twenty-third review item tests **Mohr circle** in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

24. **A.** The twenty-fourth review item tests **principal orientation** in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

25. **A.** The twenty-fifth review item tests **absolute maximum shear** in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

26. **A.** The twenty-sixth review item tests **plane stress state** in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention. This application check also tests whether the model assumptions are established before any numerical or symbolic manipulation.

27. **A.** The twenty-seventh review item tests **stress transformation** in **Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention. This final application check emphasizes that a valid mechanics relation cannot replace the diagram, geometry, and constraints that define the problem.

---

## Practice Problems

1. Given σx=80 MPa, σy=20 MPa, τxy=30 MPa, find circle center C.

2. For Problem 1, find radius R.

3. Find principal stresses for Problem 1.

4. Find maximum in-plane shear for Problem 1.

5. For plane stress, what is the third principal stress before ordering?

6. Using principal values 92.43, 7.57, 0 MPa, find absolute maximum 3D shear.

7. What stress exists on a principal plane?

8. What is the angle relationship between physical rotation and Mohr-circle rotation?

9. Why must σ3=0 be included in absolute max-shear evaluation for plane stress?

10. What is the Mohr-circle radius formula?


---

## Practice Problem Solutions

1. C=(80+20)/2=50 MPa. Practice verification: use the **40.1 Combined Normal and Shear Stress States** relation for Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

2. R=sqrt(30²+30²)=42.43 MPa.

3. σ1=92.43 MPa, σ2=7.57 MPa.

4. τmax,in=42.43 MPa. Practice verification: use the **40.4 Maximum In-Plane Shear Stress** relation for Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

5. 0. Practice verification: use the **40.5 Constructing Mohr's Circle** relation for Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

6. (92.43-0)/2=46.22 MPa. Practice verification: use the **40.6 Principal-Plane Orientation** relation for Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

7. Normal principal stress with zero in-plane shear.

8. Mohr-circle angle is twice the physical-plane angle, with sign interpretation following the chosen convention.

9. Because the largest principal-stress separation may involve the out-of-plane zero stress.

10. R=sqrt[((σx−σy)/2)^2+τxy^2].

---

## Quick Reference

**Handbook anchor:** Mechanics of Materials, printed pp. 132–134.

- **plane stress state:** Combined Normal and Shear Stress States
- **stress transformation:** Stress Transformation
- **principal stress:** Principal Stresses
- **maximum in-plane shear:** Maximum In-Plane Shear Stress
- **Mohr circle:** Constructing Mohr's Circle
- **principal orientation:** Principal-Plane Orientation
- **absolute maximum shear:** Plane Stress, 3D Shear, and Constitutive Check
---

## What's Next

**02-41 — Fluid Properties, Pressure, and Hydrostatics**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor