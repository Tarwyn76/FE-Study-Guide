---
chapter: "02-29"
title: "Area Moments of Inertia and the Parallel-Axis Theorem"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-029-01, MECH-2C-029-02, MECH-2C-029-03, MECH-2C-029-04, MECH-2C-029-05, MECH-2C-029-06, MECH-2C-029-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-29: Area Moments of Inertia and the Parallel-Axis Theorem

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-28 Centroids · 01-21 Integration

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines second moments of area, polar moment, radius of gyration, product of inertia, the area parallel-axis theorem, and tabulated values for common shapes.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **29.1** Explain and apply **Second Moment of Area**.
* **29.2** Explain and apply **Common Centroidal Shapes**.
* **29.3** Explain and apply **Parallel-Axis Theorem**.
* **29.4** Explain and apply **Composite Areas**.
* **29.5** Explain and apply **Polar Moment of Area**.
* **29.6** Explain and apply **Radius of Gyration**.
* **29.7** Explain and apply **Product of Inertia and Axis Choice**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 29.1 Second Moment of Area

The area moment of inertia measures how area is distributed relative to an axis. The Handbook defines

\[
I_x=\int_A y^2\,dA,\qquad I_y=\int_A x^2\,dA.
\]

It is a geometric property with units of length to the fourth power. It is not the same quantity as mass moment of inertia.

\[I_x=\int y^2dA,\qquad I_y=\int x^2dA\]

![FIG-02-29-001: Area with differential element dA at x,y showing squared distances to x and y axes.](../figures/FIG-02-29-001-second-moment-of-area.png)

### Worked Example 1

**Problem.** Find Ix,c for a 0.20 m wide by 0.30 m high rectangle.

**Solution.** Ix=bh^3/12=0.20(0.30^3)/12=4.50×10^-4 m^4.

---

## 29.2 Common Centroidal Shapes

Use Handbook tables for rectangles, circles, triangles, and other standard shapes. Always confirm whether the listed expression is about a centroidal axis, an edge axis, or another reference.

For a rectangle of width \(b\) and height \(h\),

\[
I_{x,c}=rac{bh^3}{12},\qquad I_{y,c}=rac{hb^3}{12}.
\]

\[I_{x,c}=\frac{bh^3}{12}\]

![FIG-02-29-002: Rectangle and circle with centroidal axes and standard area moments of inertia.](../figures/FIG-02-29-002-common-centroidal-shapes.png)

### Worked Example 2

**Problem.** A centroidal Ix=2.0×10^-6 m^4, A=0.001 m², shifted d=0.05 m. Find new Ix.

**Solution.** I=2.0e-6+0.001(0.05²)=4.5e-6 m^4.

---

## 29.3 Parallel-Axis Theorem

Once a centroidal moment of inertia is known, shift to a parallel axis using the Handbook relation.

The distance \(d\) must be perpendicular to the two parallel axes. Do not use the theorem to rotate axes.

\[I=I_c+Ad^2\]

![FIG-02-29-003: Centroidal axis and parallel shifted axis separated by d, with area A.](../figures/FIG-02-29-003-parallel-axis-theorem.png)

### Worked Example 3

**Problem.** What are units of area moment of inertia?

**Solution.** Length^4, e.g. m^4 or mm^4.

---

## 29.4 Composite Areas

For a composite section, find the overall centroid first. Then shift each piece's centroidal inertia to the common composite axis and sum.

For holes, subtract both the area and the shifted inertia contribution. Never subtract the squared distance term separately from a positive hole inertia; treat the hole as a negative area component consistently.

\[I=\sum_i\left(I_{c,i}+A_i d_i^2\right)\]

![FIG-02-29-004: Built-up section split into simple areas with centroid distances to a common neutral axis.](../figures/FIG-02-29-004-composite-areas.png)

### Worked Example 4

**Problem.** State J in terms of perpendicular Ix and Iy through same point.

**Solution.** J=Ix+Iy.

---

## 29.5 Polar Moment of Area

For perpendicular axes through the same point, the Handbook gives

\[
J=I_x+I_y.
\]

For circular shafts, the polar area moment appears directly in torsion formulas. This geometric polar moment is distinct from polar **mass** moment used in dynamics.

\[J=I_x+I_y\]

![FIG-02-29-005: Circular cross-section with x,y axes and polar radius r.](../figures/FIG-02-29-005-polar-moment-of-area.png)

### Worked Example 5

**Problem.** A section has Ix=8e-6 m^4 and A=0.002 m². Find rx.

**Solution.** rx=sqrt(Ix/A)=sqrt(0.004)=0.06325 m.

---

## 29.6 Radius of Gyration

The area radius of gyration is the distance at which the entire area could be imagined concentrated to produce the same area moment of inertia.

It is useful in slenderness and buckling calculations.

\[r_x=\sqrt{\frac{I_x}{A}},\qquad r_y=\sqrt{\frac{I_y}{A}}\]

![FIG-02-29-006: Area replaced conceptually by concentrated area at radius of gyration about an axis.](../figures/FIG-02-29-006-radius-of-gyration.png)

### Worked Example 6

**Problem.** Why find composite centroid before composite I?

**Solution.** The common axis distances d for parallel-axis shifts depend on the composite centroid.

---

## 29.7 Product of Inertia and Axis Choice

The Handbook defines

\[
I_{xy}=\int_A xy\,dA.
\]

For an area symmetric about either x or y centroidal axis, the product of inertia about those symmetry axes is zero. Product of inertia becomes important when rotating axes and finding principal area axes.

\[I_{xy}=\int xy\,dA\]

![FIG-02-29-007: Area elements in quadrants showing signs of xy contribution and symmetry cancellation.](../figures/FIG-02-29-007-product-of-inertia-and-axis-choice.png)

### Worked Example 7

**Problem.** How is a hole treated in I summation?

**Solution.** As negative area/inertia contribution consistently.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Does I=Ic+Ad² rotate an axis?

**Solution.** No; it shifts to a parallel axis only.

### Worked Example 9

**Problem.** When is Ixy zero by symmetry?

**Solution.** When the area is symmetric about either chosen centroidal x or y axis.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Statics, printed pp. 96–101**.

**Source boundary:** The Handbook directly defines second moments of area, polar moment, radius of gyration, product of inertia, the area parallel-axis theorem, and tabulated values for common shapes.

---

## Where This Goes Wrong

**Applying area moment of inertia before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying centroidal inertia before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying parallel-axis theorem before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying composite inertia before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying polar moment of area before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying area radius of gyration before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying product of inertia before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.

**Mixing area and mass moments of inertia.** They have different units and different physical roles.


---

## Key Terms

| Term | Working definition |
|---|---|
| area moment of inertia | Concept developed in §29.1; apply only under that section's model assumptions. |
| centroidal inertia | Concept developed in §29.2; apply only under that section's model assumptions. |
| parallel-axis theorem | Concept developed in §29.3; apply only under that section's model assumptions. |
| composite inertia | Concept developed in §29.4; apply only under that section's model assumptions. |
| polar moment of area | Concept developed in §29.5; apply only under that section's model assumptions. |
| area radius of gyration | Concept developed in §29.6; apply only under that section's model assumptions. |
| product of inertia | Concept developed in §29.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **area moment of inertia** and state the governing relation or modeling rule.

2. Define **centroidal inertia** and state the governing relation or modeling rule.

3. Define **parallel-axis theorem** and state the governing relation or modeling rule.

4. Define **composite inertia** and state the governing relation or modeling rule.

5. Define **polar moment of area** and state the governing relation or modeling rule.

6. Define **area radius of gyration** and state the governing relation or modeling rule.

7. Define **product of inertia** and state the governing relation or modeling rule.

8. What error is likely if **area moment of inertia** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **centroidal inertia** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **parallel-axis theorem** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **composite inertia** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **polar moment of area** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **area radius of gyration** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **product of inertia** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **area moment of inertia**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **centroidal inertia**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **parallel-axis theorem**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **composite inertia**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **polar moment of area**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **area radius of gyration**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **product of inertia**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **area moment of inertia**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **centroidal inertia**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **area moment of inertia** is developed in §29.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **centroidal inertia** is developed in §29.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **parallel-axis theorem** is developed in §29.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **composite inertia** is developed in §29.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **polar moment of area** is developed in §29.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **area radius of gyration** is developed in §29.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **product of inertia** is developed in §29.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **area moment of inertia**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **centroidal inertia**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **parallel-axis theorem**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **composite inertia**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **polar moment of area**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **area radius of gyration**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **product of inertia**.

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

1. Find Ix,c for a 0.20 m wide by 0.30 m high rectangle.

2. A centroidal Ix=2.0×10^-6 m^4, A=0.001 m², shifted d=0.05 m. Find new Ix.

3. What are units of area moment of inertia?

4. State J in terms of perpendicular Ix and Iy through same point.

5. A section has Ix=8e-6 m^4 and A=0.002 m². Find rx.

6. Why find composite centroid before composite I?

7. How is a hole treated in I summation?

8. Does I=Ic+Ad² rotate an axis?

9. When is Ixy zero by symmetry?

10. Distinguish area moment from mass moment of inertia.


---

## Practice Problem Solutions

1. Ix=bh^3/12=0.20(0.30^3)/12=4.50×10^-4 m^4.

2. I=2.0e-6+0.001(0.05²)=4.5e-6 m^4.

3. Length^4, e.g. m^4 or mm^4.

4. J=Ix+Iy.

5. rx=sqrt(Ix/A)=sqrt(0.004)=0.06325 m.

6. The common axis distances d for parallel-axis shifts depend on the composite centroid.

7. As negative area/inertia contribution consistently.

8. No; it shifts to a parallel axis only.

9. When the area is symmetric about either chosen centroidal x or y axis.

10. Area moment is a cross-section geometric property (L^4); mass moment measures rotational inertia (mass·L²).


---

## Quick Reference

**Handbook anchor:** Statics, printed pp. 96–101.

- **area moment of inertia:** Second Moment of Area
- **centroidal inertia:** Common Centroidal Shapes
- **parallel-axis theorem:** Parallel-Axis Theorem
- **composite inertia:** Composite Areas
- **polar moment of area:** Polar Moment of Area
- **area radius of gyration:** Radius of Gyration
- **product of inertia:** Product of Inertia and Axis Choice
---

## What's Next

**02-30 — Static Friction**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor