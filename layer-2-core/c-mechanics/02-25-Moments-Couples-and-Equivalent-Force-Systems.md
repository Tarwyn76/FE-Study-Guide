---
chapter: "02-25"
title: "Moments, Couples, and Equivalent Force Systems"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-025-01, MECH-2C-025-02, MECH-2C-025-03, MECH-2C-025-04, MECH-2C-025-05, MECH-2C-025-06, MECH-2C-025-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-25: Moments, Couples, and Equivalent Force Systems

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-23 2D Equilibrium · 01-13 Vector Fundamentals

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines moments, couples, resultant force/moment systems, and equilibrium requirements.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **25.1** Explain and apply **Moment of a Force**.
* **25.2** Explain and apply **2D Moment Components**.
* **25.3** Explain and apply **Couples**.
* **25.4** Explain and apply **Equivalent Force-Couple Systems**.
* **25.5** Explain and apply **Resultant of a General Force System**.
* **25.6** Explain and apply **Varignon's Theorem and Component Moments**.
* **25.7** Explain and apply **Moment Sign and Sanity Checks**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 25.1 Moment of a Force

A moment measures the rotational tendency of a force about a point. In vector form the Handbook gives \(\mathbf M_O=\mathbf r	imes\mathbf F\), where \(\mathbf r\) runs from the moment center to any point on the force line of action.

In 2D, the scalar moment is force times perpendicular distance, with sign determined by the chosen clockwise/counterclockwise convention.

\[\mathbf M_O=\mathbf r\times\mathbf F,\qquad M_O=F d_\perp\]

![FIG-02-25-001: Force line of action, position vector r, perpendicular lever arm, and moment sense about O.](../figures/FIG-02-25-001-moment-of-a-force.png)

### Worked Example 1

**Problem.** A 100-N force acts perpendicular to a 0.40-m lever arm. Find moment magnitude.

**Solution.** M=100(0.40)=40 N·m.

---

## 25.2 2D Moment Components

For \(\mathbf r=x\hat i+y\hat j\) and \(\mathbf F=F_x\hat i+F_y\hat j\), the out-of-plane moment is \(M_z=xF_y-yF_x\).

This component form is often safer than estimating perpendicular distance when geometry is given in coordinates.

\[M_z=xF_y-yF_x\]

![FIG-02-25-002: Coordinate point of application with x,y, Fx,Fy and resulting z moment.](../figures/FIG-02-25-002-2d-moment-components.png)

### Worked Example 2

**Problem.** At r=(0.3 i+0.2 j) m, F=(50 i+80 j) N. Find Mz.

**Solution.** Mz=xFy-yFx=0.3(80)-0.2(50)=14 N·m.

---

## 25.3 Couples

A couple consists of equal, opposite, parallel forces separated by a distance. Net force is zero, but the pair creates a pure moment.

A couple moment is a free vector for rigid-body statics: it can be applied anywhere on the body without changing the external force-moment effect.

\[M_c=F d\]

![FIG-02-25-003: Equal and opposite force pair separated by d, replaced by a single couple moment.](../figures/FIG-02-25-003-couples.png)

### Worked Example 3

**Problem.** Two 200-N opposite parallel forces are 0.15 m apart. Find couple moment magnitude.

**Solution.** M=200(0.15)=30 N·m.

---

## 25.4 Equivalent Force-Couple Systems

Moving a force from one point to another requires adding a couple equal to the moment created by the shift. The force alone cannot simply be slid to a parallel, offset line of action.

This is the basis for reducing distributed or multiple loads to a resultant force plus a resultant moment at a chosen reference point.

\[\mathbf F@A\equiv \mathbf F@O+\mathbf r_{OA}\times\mathbf F\]

![FIG-02-25-004: Force at point A replaced by same force at O plus a compensating couple.](../figures/FIG-02-25-004-equivalent-force-couple-systems.png)

### Worked Example 4

**Problem.** A force is moved to a parallel line 0.20 m away. What must be added?

**Solution.** A couple M=F(0.20), with sign matching the moment of the offset.

---

## 25.5 Resultant of a General Force System

For multiple forces, sum all forces and all moments about a common reference point.

If the resultant force is nonzero, the system may sometimes be represented by a single force at an appropriate line of action. If resultant force is zero but resultant moment is nonzero, the system reduces to a pure couple.

\[\mathbf R=\sum\mathbf F_i,\qquad \mathbf M_O=\sum(\mathbf r_i\times\mathbf F_i)+\sum\mathbf M_i\]

![FIG-02-25-005: Multiple forces/couples reduced to resultant R and resultant moment M_O.](../figures/FIG-02-25-005-resultant-of-a-general-force-system.png)

### Worked Example 5

**Problem.** What moment does a force produce about a point on its line of action?

**Solution.** Zero.

---

## 25.6 Varignon's Theorem and Component Moments

The moment of a force equals the sum of the moments of its components about the same point. This lets you resolve an angled force and compute component moments separately.

It is especially useful when one component passes through the moment center and therefore contributes zero moment.

\[M_O(\mathbf F)=M_O(F_x)+M_O(F_y)\]

![FIG-02-25-006: Inclined force resolved into components, with one component passing through O and the other creating moment.](../figures/FIG-02-25-006-varignon-s-theorem-and-component-moments.png)

### Worked Example 6

**Problem.** Can a pure couple be moved anywhere on a rigid body in statics?

**Solution.** Yes, as a free vector under rigid-body statics.

---

## 25.7 Moment Sign and Sanity Checks

Choose a sign convention and use it consistently. In planar statics, counterclockwise positive is common but not mandatory.

Check dimensions: force times length. Check lever-arm geometry: only perpendicular distance matters. Check whether a force whose line of action passes through the moment center correctly gives zero moment.

\[[M]=\text{force}\times\text{length}\]

![FIG-02-25-007: Moment checklist covering sign, perpendicular distance, line of action, units, and zero-moment cases.](../figures/FIG-02-25-007-moment-sign-and-sanity-checks.png)

### Worked Example 7

**Problem.** State Varignon's theorem.

**Solution.** Moment of a force equals the sum of moments of its components about the same point.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What are the units of moment in SI?

**Solution.** N·m.

### Worked Example 9

**Problem.** If ΣF=0 but ΣM≠0, to what does the system reduce?

**Solution.** A pure couple.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Statics, printed p. 95**.

**Source boundary:** The Handbook directly defines moments, couples, resultant force/moment systems, and equilibrium requirements.

---

## Where This Goes Wrong

**Applying force moment before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying scalar moment before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying couple moment before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying force-couple equivalence before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying equivalent resultant before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying Varignon theorem before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying moment audit before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| force moment | Concept developed in §25.1; apply only under that section's model assumptions. |
| scalar moment | Concept developed in §25.2; apply only under that section's model assumptions. |
| couple moment | Concept developed in §25.3; apply only under that section's model assumptions. |
| force-couple equivalence | Concept developed in §25.4; apply only under that section's model assumptions. |
| equivalent resultant | Concept developed in §25.5; apply only under that section's model assumptions. |
| Varignon theorem | Concept developed in §25.6; apply only under that section's model assumptions. |
| moment audit | Concept developed in §25.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **force moment** and state the governing relation or modeling rule.

2. Define **scalar moment** and state the governing relation or modeling rule.

3. Define **couple moment** and state the governing relation or modeling rule.

4. Define **force-couple equivalence** and state the governing relation or modeling rule.

5. Define **equivalent resultant** and state the governing relation or modeling rule.

6. Define **Varignon theorem** and state the governing relation or modeling rule.

7. Define **moment audit** and state the governing relation or modeling rule.

8. What error is likely if **force moment** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **scalar moment** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **couple moment** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **force-couple equivalence** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **equivalent resultant** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **Varignon theorem** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **moment audit** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **force moment**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **scalar moment**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **couple moment**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **force-couple equivalence**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **equivalent resultant**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **Varignon theorem**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **moment audit**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **force moment**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **scalar moment**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **force moment** is developed in §25.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **scalar moment** is developed in §25.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **couple moment** is developed in §25.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **force-couple equivalence** is developed in §25.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **equivalent resultant** is developed in §25.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **Varignon theorem** is developed in §25.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **moment audit** is developed in §25.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **force moment**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **scalar moment**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **couple moment**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **force-couple equivalence**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **equivalent resultant**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **Varignon theorem**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **moment audit**.

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

1. A 100-N force acts perpendicular to a 0.40-m lever arm. Find moment magnitude.

2. At r=(0.3 i+0.2 j) m, F=(50 i+80 j) N. Find Mz.

3. Two 200-N opposite parallel forces are 0.15 m apart. Find couple moment magnitude.

4. A force is moved to a parallel line 0.20 m away. What must be added?

5. What moment does a force produce about a point on its line of action?

6. Can a pure couple be moved anywhere on a rigid body in statics?

7. State Varignon's theorem.

8. What are the units of moment in SI?

9. If ΣF=0 but ΣM≠0, to what does the system reduce?

10. Why must all moments be summed about one common reference point during reduction?


---

## Practice Problem Solutions

1. M=100(0.40)=40 N·m.

2. Mz=xFy-yFx=0.3(80)-0.2(50)=14 N·m.

3. M=200(0.15)=30 N·m.

4. A couple M=F(0.20), with sign matching the moment of the offset.

5. Zero.

6. Yes, as a free vector under rigid-body statics.

7. Moment of a force equals the sum of moments of its components about the same point.

8. N·m.

9. A pure couple.

10. Mixing reference points changes force-moment equivalence.


---

## Quick Reference

**Handbook anchor:** Statics, printed p. 95.

- **force moment:** Moment of a Force
- **scalar moment:** 2D Moment Components
- **couple moment:** Couples
- **force-couple equivalence:** Equivalent Force-Couple Systems
- **equivalent resultant:** Resultant of a General Force System
- **Varignon theorem:** Varignon's Theorem and Component Moments
- **moment audit:** Moment Sign and Sanity Checks
---

## What's Next

**02-26 — Rigid-Body Equilibrium and Support Reactions**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor