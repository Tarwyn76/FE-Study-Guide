---
chapter: "02-28"
title: "Distributed Loads, Centroids, and Centers of Gravity"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-028-01, MECH-2C-028-02, MECH-2C-028-03, MECH-2C-028-04, MECH-2C-028-05, MECH-2C-028-06, MECH-2C-028-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-28: Distributed Loads, Centroids, and Centers of Gravity

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-25 Moments · 01-21 Integration

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly supplies centroid formulas for discrete and continuous masses/areas/lengths/volumes, first moments of area, and common centroid tables. Distributed-load resultants are direct statics applications.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **28.1** Explain and apply **Distributed Load Resultant**.
* **28.2** Explain and apply **Uniform and Triangular Loads**.
* **28.3** Explain and apply **Centroid of Discrete Areas**.
* **28.4** Explain and apply **Centroids by Integration**.
* **28.5** Explain and apply **Center of Mass and Center of Gravity**.
* **28.6** Explain and apply **Composite Bodies and Symmetry**.
* **28.7** Explain and apply **Resultant-Location Verification**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 28.1 Distributed Load Resultant

A distributed line load \(w(x)\) has units force per length. Its equivalent resultant force equals the area under the load diagram.

The resultant location is found by matching the moment of the distribution, so it acts through the centroid of the load-intensity area.

\[R=\int_a^b w(x)\,dx,\qquad x_R=\frac{\int_a^b xw(x)\,dx}{R}\]

![FIG-02-28-001: Variable distributed load over a beam replaced by equivalent resultant at the centroid of the load diagram.](../figures/FIG-02-28-001-distributed-load-resultant.png)

### Worked Example 1

**Problem.** A uniform 4 kN/m load acts over 3 m. Find resultant and location.

**Solution.** R=12 kN at the midpoint, 1.5 m from either end.

---

## 28.2 Uniform and Triangular Loads

A uniform load has resultant \(wL\) at the segment midpoint. A triangular load has resultant equal to the triangle area and acts one-third of the base length from the larger-intensity end.

These are centroid results, not separate force laws.

\[R_{\rm uniform}=wL,\qquad R_{\rm triangle}=\tfrac12 w_0L\]

![FIG-02-28-002: Uniform and triangular beam loads with equivalent resultants and centroid locations.](../figures/FIG-02-28-002-uniform-and-triangular-loads.png)

### Worked Example 2

**Problem.** A triangular load rises from 0 to 6 kN/m over 4 m. Find resultant.

**Solution.** R=0.5(6)(4)=12 kN.

---

## 28.3 Centroid of Discrete Areas

For composite areas divided into simple pieces, the centroid coordinates are area-weighted averages.

Holes are conveniently handled as negative areas. Use one common reference axis and signed centroid coordinates.

\[\bar x=\frac{\sum A_i x_i}{\sum A_i},\qquad \bar y=\frac{\sum A_i y_i}{\sum A_i}\]

![FIG-02-28-003: Composite plate split into rectangles and a circular hole with centroid locations and signed areas.](../figures/FIG-02-28-003-centroid-of-discrete-areas.png)

### Worked Example 3

**Problem.** Where does the triangular-load resultant in Problem 2 act from the larger end?

**Solution.** One-third of 4 m = 1.333 m from the larger end.

---

## 28.4 Centroids by Integration

For a continuous area,

\[
ar x=rac1A\int_A x\,dA,\qquad ar y=rac1A\int_A y\,dA.
\]

Choose differential elements that make the boundary function simple. Symmetry should be used before integration whenever possible.

\[A=\int_A dA\]

![FIG-02-28-004: Area under y=f(x) with differential vertical strip dA=y dx and centroid coordinate x.](../figures/FIG-02-28-004-centroids-by-integration.png)

### Worked Example 4

**Problem.** Areas 2 m² at x=1 m and 3 m² at x=5 m form a composite area. Find xbar.

**Solution.** xbar=(2·1+3·5)/5=3.4 m.

---

## 28.5 Center of Mass and Center of Gravity

For discrete masses, the Handbook gives a mass-weighted position vector. In uniform gravity, center of gravity coincides with center of mass.

For nonuniform density, the mass center requires weighting by density rather than geometric area alone.

\[\mathbf r_G=\frac{\sum m_i\mathbf r_i}{\sum m_i}\]

![FIG-02-28-005: Discrete masses at coordinates combined to a center-of-mass point G.](../figures/FIG-02-28-005-center-of-mass-and-center-of-gravity.png)

### Worked Example 5

**Problem.** How is a hole handled in composite centroid calculation?

**Solution.** As negative area with its centroid coordinate.

---

## 28.6 Composite Bodies and Symmetry

A composite body can be decomposed into simple volumes or masses. If density is uniform, volume weighting may replace mass weighting. Symmetry immediately fixes one or more centroid coordinates.

A centroid may lie outside the material itself, as with a semicircular arc or C-shaped area; this is physically acceptable.

\[\bar x=\frac{\sum V_i x_i}{\sum V_i}\quad(\rho=\text{constant})\]

![FIG-02-28-006: Symmetric and hollow composite shapes with centroid on symmetry axes, including one centroid outside material.](../figures/FIG-02-28-006-composite-bodies-and-symmetry.png)

### Worked Example 6

**Problem.** Can a centroid lie outside the material?

**Solution.** Yes.

---

## 28.7 Resultant-Location Verification

A distributed-load replacement must preserve both total force and total moment about any point. After locating the resultant, verify

\[
R=\int w\,dx,\qquad Rx_R=\int xw\,dx.
\]

The same first-moment logic underlies area centroids and centers of gravity.

\[\text{same force + same moment}\Rightarrow\text{statically equivalent resultant}\]

![FIG-02-28-007: Distributed-load and centroid equivalence check based on force/area and first moment.](../figures/FIG-02-28-007-resultant-location-verification.png)

### Worked Example 7

**Problem.** What must an equivalent distributed-load resultant preserve?

**Solution.** Total force and total moment.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** For uniform density in uniform gravity, how are center of mass and center of gravity related?

**Solution.** They coincide.

### Worked Example 9

**Problem.** What does symmetry tell you about centroid location?

**Solution.** The centroid lies on every axis/plane of symmetry.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Statics, printed pp. 96 and 99–101**.

**Source boundary:** The Handbook directly supplies centroid formulas for discrete and continuous masses/areas/lengths/volumes, first moments of area, and common centroid tables. Distributed-load resultants are direct statics applications.

---

## Where This Goes Wrong

**Applying distributed-load resultant before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying common load resultants before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying area centroid before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying centroid integration before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying center of mass before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying composite centroid before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying first moment before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| distributed-load resultant | Concept developed in §28.1; apply only under that section's model assumptions. |
| common load resultants | Concept developed in §28.2; apply only under that section's model assumptions. |
| area centroid | Concept developed in §28.3; apply only under that section's model assumptions. |
| centroid integration | Concept developed in §28.4; apply only under that section's model assumptions. |
| center of mass | Concept developed in §28.5; apply only under that section's model assumptions. |
| composite centroid | Concept developed in §28.6; apply only under that section's model assumptions. |
| first moment | Concept developed in §28.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **distributed-load resultant** and state the governing relation or modeling rule.

2. Define **common load resultants** and state the governing relation or modeling rule.

3. Define **area centroid** and state the governing relation or modeling rule.

4. Define **centroid integration** and state the governing relation or modeling rule.

5. Define **center of mass** and state the governing relation or modeling rule.

6. Define **composite centroid** and state the governing relation or modeling rule.

7. Define **first moment** and state the governing relation or modeling rule.

8. What error is likely if **distributed-load resultant** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **common load resultants** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **area centroid** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **centroid integration** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **center of mass** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **composite centroid** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **first moment** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **distributed-load resultant**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **common load resultants**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **area centroid**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **centroid integration**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **center of mass**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **composite centroid**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **first moment**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **distributed-load resultant**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **common load resultants**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **distributed-load resultant** is developed in §28.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **common load resultants** is developed in §28.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **area centroid** is developed in §28.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **centroid integration** is developed in §28.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **center of mass** is developed in §28.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **composite centroid** is developed in §28.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **first moment** is developed in §28.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **distributed-load resultant**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **common load resultants**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **area centroid**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **centroid integration**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **center of mass**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **composite centroid**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **first moment**.

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

1. A uniform 4 kN/m load acts over 3 m. Find resultant and location.

2. A triangular load rises from 0 to 6 kN/m over 4 m. Find resultant.

3. Where does the triangular-load resultant in Problem 2 act from the larger end?

4. Areas 2 m² at x=1 m and 3 m² at x=5 m form a composite area. Find xbar.

5. How is a hole handled in composite centroid calculation?

6. Can a centroid lie outside the material?

7. What must an equivalent distributed-load resultant preserve?

8. For uniform density in uniform gravity, how are center of mass and center of gravity related?

9. What does symmetry tell you about centroid location?

10. State the continuous area-centroid formula for xbar.


---

## Practice Problem Solutions

1. R=12 kN at the midpoint, 1.5 m from either end.

2. R=0.5(6)(4)=12 kN.

3. One-third of 4 m = 1.333 m from the larger end.

4. xbar=(2·1+3·5)/5=3.4 m.

5. As negative area with its centroid coordinate.

6. Yes.

7. Total force and total moment.

8. They coincide.

9. The centroid lies on every axis/plane of symmetry.

10. xbar=(1/A)∫x dA.


---

## Quick Reference

**Handbook anchor:** Statics, printed pp. 96 and 99–101.

- **distributed-load resultant:** Distributed Load Resultant
- **common load resultants:** Uniform and Triangular Loads
- **area centroid:** Centroid of Discrete Areas
- **centroid integration:** Centroids by Integration
- **center of mass:** Center of Mass and Center of Gravity
- **composite centroid:** Composite Bodies and Symmetry
- **first moment:** Resultant-Location Verification
---

## What's Next

**02-29 — Area Moments of Inertia and the Parallel-Axis Theorem**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor