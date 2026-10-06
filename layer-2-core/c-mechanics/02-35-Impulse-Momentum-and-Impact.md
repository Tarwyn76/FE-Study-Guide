---
chapter: "02-35"
title: "Impulse, Momentum, and Impact"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-035-01, MECH-2C-035-02, MECH-2C-035-03, MECH-2C-035-04, MECH-2C-035-05, MECH-2C-035-06, MECH-2C-035-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-35: Impulse, Momentum, and Impact

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-33 Particle Kinetics

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines linear/angular momentum, impulse-momentum, conservation forms, direct central impact, and coefficient of restitution.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **35.1** Explain and apply **Linear Momentum**.
* **35.2** Explain and apply **Linear Impulse-Momentum**.
* **35.3** Explain and apply **Conservation of Linear Momentum**.
* **35.4** Explain and apply **Angular Momentum and Angular Impulse**.
* **35.5** Explain and apply **Direct Central Impact**.
* **35.6** Explain and apply **Coefficient of Restitution**.
* **35.7** Explain and apply **Elastic, Inelastic, and Perfectly Plastic Impact**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 35.1 Linear Momentum

For a particle of constant mass, linear momentum is \(m\mathbf v\). It is a vector; direction must be preserved.

For a system of particles, total momentum is the vector sum over all particles.

\[\mathbf p=m\mathbf v,\qquad \mathbf P=\sum_i m_i\mathbf v_i\]

![FIG-02-35-001: Two-particle system with individual momentum vectors summing to total momentum.](../figures/FIG-02-35-001-linear-momentum.png)

### Worked Example 1

**Problem.** A 2-kg mass moves at 5 m/s. Find momentum.

**Solution.** p=10 kg·m/s.

---

## 35.2 Linear Impulse-Momentum

Integrating Newton's second law over time gives change in momentum equal to impulse.

This is especially effective for short-duration forces or when force is known as a function of time.

\[m\mathbf v_2=m\mathbf v_1+\int_{t_1}^{t_2}\mathbf F\,dt\]

![FIG-02-35-002: Force-time curve with shaded area equal to impulse and resulting momentum change.](../figures/FIG-02-35-002-linear-impulse-momentum.png)

### Worked Example 2

**Problem.** A constant 20-N force acts for 0.5 s. Find impulse.

**Solution.** J=10 N·s.

---

## 35.3 Conservation of Linear Momentum

If net external impulse in a direction is negligible, system momentum in that direction is conserved.

Internal forces cancel in the system sum, which is why collisions can often be analyzed without knowing the detailed contact force history.

\[\sum m_i\mathbf v_{i1}=\sum m_i\mathbf v_{i2}\quad(\text{zero external impulse})\]

![FIG-02-35-003: Two-body collision control system showing internal contact forces canceled.](../figures/FIG-02-35-003-conservation-of-linear-momentum.png)

### Worked Example 3

**Problem.** If the mass in Problem 1 receives -4 N·s impulse along its motion, find new velocity.

**Solution.** p2=10-4=6; v2=3 m/s.

---

## 35.4 Angular Momentum and Angular Impulse

Angular momentum about point O for a particle is \(\mathbf H_O=\mathbf r	imes m\mathbf v\). The time integral of external moment about O changes angular momentum.

Choose O to eliminate unknown impulsive forces when their lines of action pass through O.

\[\mathbf H_{O2}=\mathbf H_{O1}+\int_{t_1}^{t_2}\mathbf M_O\,dt\]

![FIG-02-35-004: Particle relative to point O with r, mv, and moment impulse.](../figures/FIG-02-35-004-angular-momentum-and-angular-impulse.png)

### Worked Example 4

**Problem.** Two masses 2 kg at 4 m/s and 3 kg at 0 collide and stick. Find final velocity.

**Solution.** v=(2·4)/(5)=1.6 m/s.

---

## 35.5 Direct Central Impact

For a short direct central impact with negligible external impulse along the impact line, linear momentum is conserved along that line.

Momentum conservation alone provides one equation for two unknown post-impact velocities; a second relation is needed.

\[m_1v_1+m_2v_2=m_1v_1'+m_2v_2'\]

![FIG-02-35-005: Two masses before and after a one-dimensional central collision.](../figures/FIG-02-35-005-direct-central-impact.png)

### Worked Example 5

**Problem.** For a perfectly elastic direct impact, what is e?

**Solution.** 1.

---

## 35.6 Coefficient of Restitution

The Handbook gives coefficient of restitution as the ratio of relative separation speed after impact to relative approach speed before impact along the normal direction.

Its physical range is \(0\le e\le1\).

\[e=\frac{v_2'-v_1'}{v_1-v_2}\quad\text{for chosen 1D orientation}\]

![FIG-02-35-006: Before/after impact velocities with relative approach and separation speeds.](../figures/FIG-02-35-006-coefficient-of-restitution.png)

### Worked Example 6

**Problem.** For no rebound in the restitution model, what is e?

**Solution.** 0.

---

## 35.7 Elastic, Inelastic, and Perfectly Plastic Impact

At \(e=1\), direct impact is perfectly elastic in the ideal model and kinetic energy is conserved. At \(e=0\), bodies have no relative rebound speed; for a one-dimensional sticking impact they move together.

Most real impacts lie between these limits and dissipate mechanical energy.

\[e=1:\text{ elastic},\qquad e=0:\text{ no rebound}\]

![FIG-02-35-007: Impact spectrum from perfectly elastic through partially inelastic to perfectly plastic/no rebound.](../figures/FIG-02-35-007-elastic-inelastic-and-perfectly-plastic-impact.png)

### Worked Example 7

**Problem.** Can momentum be conserved while kinetic energy decreases?

**Solution.** Yes; inelastic impacts conserve momentum when external impulse is negligible but dissipate kinetic energy.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What is angular momentum of a particle about O?

**Solution.** H_O=r×mv.

### Worked Example 9

**Problem.** Why choose a moment point through an unknown impulsive reaction?

**Solution.** That reaction has zero moment about the point and drops out of angular impulse-momentum.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Dynamics, printed pp. 108–109**.

**Source boundary:** The Handbook directly defines linear/angular momentum, impulse-momentum, conservation forms, direct central impact, and coefficient of restitution.

---

## Where This Goes Wrong

**Applying linear momentum before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying linear impulse before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying momentum conservation before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying angular impulse-momentum before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying direct central impact before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying coefficient of restitution before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying impact classification before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| linear momentum | Concept developed in §35.1; apply only under that section's model assumptions. |
| linear impulse | Concept developed in §35.2; apply only under that section's model assumptions. |
| momentum conservation | Concept developed in §35.3; apply only under that section's model assumptions. |
| angular impulse-momentum | Concept developed in §35.4; apply only under that section's model assumptions. |
| direct central impact | Concept developed in §35.5; apply only under that section's model assumptions. |
| coefficient of restitution | Concept developed in §35.6; apply only under that section's model assumptions. |
| impact classification | Concept developed in §35.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **linear momentum** and state the governing relation or modeling rule.

2. Define **linear impulse** and state the governing relation or modeling rule.

3. Define **momentum conservation** and state the governing relation or modeling rule.

4. Define **angular impulse-momentum** and state the governing relation or modeling rule.

5. Define **direct central impact** and state the governing relation or modeling rule.

6. Define **coefficient of restitution** and state the governing relation or modeling rule.

7. Define **impact classification** and state the governing relation or modeling rule.

8. What error is likely if **linear momentum** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **linear impulse** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **momentum conservation** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **angular impulse-momentum** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **direct central impact** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **coefficient of restitution** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **impact classification** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **linear momentum**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **linear impulse**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **momentum conservation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **angular impulse-momentum**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **direct central impact**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **coefficient of restitution**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **impact classification**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **linear momentum**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **linear impulse**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **linear momentum** is developed in §35.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **linear impulse** is developed in §35.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **momentum conservation** is developed in §35.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **angular impulse-momentum** is developed in §35.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **direct central impact** is developed in §35.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **coefficient of restitution** is developed in §35.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **impact classification** is developed in §35.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **linear momentum**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **linear impulse**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **momentum conservation**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **angular impulse-momentum**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **direct central impact**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **coefficient of restitution**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **impact classification**.

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

1. A 2-kg mass moves at 5 m/s. Find momentum.

2. A constant 20-N force acts for 0.5 s. Find impulse.

3. If the mass in Problem 1 receives -4 N·s impulse along its motion, find new velocity.

4. Two masses 2 kg at 4 m/s and 3 kg at 0 collide and stick. Find final velocity.

5. For a perfectly elastic direct impact, what is e?

6. For no rebound in the restitution model, what is e?

7. Can momentum be conserved while kinetic energy decreases?

8. What is angular momentum of a particle about O?

9. Why choose a moment point through an unknown impulsive reaction?

10. State the physical bounds on e.


---

## Practice Problem Solutions

1. p=10 kg·m/s.

2. J=10 N·s.

3. p2=10-4=6; v2=3 m/s.

4. v=(2·4)/(5)=1.6 m/s.

5. 1.

6. 0.

7. Yes; inelastic impacts conserve momentum when external impulse is negligible but dissipate kinetic energy.

8. H_O=r×mv.

9. That reaction has zero moment about the point and drops out of angular impulse-momentum.

10. 0≤e≤1 for the Handbook impact model.


---

## Quick Reference

**Handbook anchor:** Dynamics, printed pp. 108–109.

- **linear momentum:** Linear Momentum
- **linear impulse:** Linear Impulse-Momentum
- **momentum conservation:** Conservation of Linear Momentum
- **angular impulse-momentum:** Angular Momentum and Angular Impulse
- **direct central impact:** Direct Central Impact
- **coefficient of restitution:** Coefficient of Restitution
- **impact classification:** Elastic, Inelastic, and Perfectly Plastic Impact
---

## What's Next

**02-36 — Rigid-Body Planar Kinematics and Kinetics**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor