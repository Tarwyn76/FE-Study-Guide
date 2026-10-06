---
chapter: "02-30"
title: "Static Friction"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-030-01, MECH-2C-030-02, MECH-2C-030-03, MECH-2C-030-04, MECH-2C-030-05, MECH-2C-030-06, MECH-2C-030-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-30: Static Friction

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-26 Rigid-Body Equilibrium

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives the static/kinetic friction laws, limiting friction, screw-thread relation, and belt-friction relation.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **30.1** Explain and apply **Static Friction Is Reactive**.
* **30.2** Explain and apply **Impending Motion**.
* **30.3** Explain and apply **Kinetic Friction**.
* **30.4** Explain and apply **Blocks on Inclines**.
* **30.5** Explain and apply **Tipping versus Sliding**.
* **30.6** Explain and apply **Belt Friction**.
* **30.7** Explain and apply **Square-Thread Screw Friction**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 30.1 Static Friction Is Reactive

Static friction adjusts as needed to prevent relative sliding, up to a limiting value. Therefore \(F=\mu_sN\) is not valid for every static problem.

The correct inequality is

\[
|F|\le\mu_sN.
\]

Equality applies only at impending slip.

\[|F|\le\mu_sN\]

![FIG-02-30-001: Block on rough surface with applied force, normal force, and static friction adapting below its maximum.](../figures/FIG-02-30-001-static-friction-is-reactive.png)

### Worked Example 1

**Problem.** A 100-N block on a horizontal surface has μs=0.40. Find maximum static friction.

**Solution.** Fmax=0.40(100)=40 N if N=100 N.

---

## 30.2 Impending Motion

At the threshold of sliding, static friction reaches its limiting magnitude and acts opposite the impending relative motion.

Assume an impending direction, draw friction opposing it, solve equilibrium, and verify that the resulting normal force and friction sense are physically consistent.

\[F=\mu_sN\quad\text{at impending slip}\]

![FIG-02-30-002: Block about to slide right with limiting friction left and friction cone inset.](../figures/FIG-02-30-002-impending-motion.png)

### Worked Example 2

**Problem.** If the applied horizontal force in Problem 1 is 25 N and the block remains at rest, what is friction?

**Solution.** 25 N opposite the applied force, not 40 N.

---

## 30.3 Kinetic Friction

Once sliding occurs, the simple Coulomb model uses

\[
F_k=\mu_kN.
\]

The Handbook notes that the force needed to initiate sliding is typically greater than the force needed to maintain low-speed sliding, so generally \(\mu_s>\mu_k\).

\[F_k=\mu_kN\]

![FIG-02-30-003: Static-friction range up to μsN followed by lower kinetic level μkN after slip.](../figures/FIG-02-30-003-kinetic-friction.png)

### Worked Example 3

**Problem.** If μk=0.30 and the block slides, find kinetic friction.

**Solution.** 30 N.

---

## 30.4 Blocks on Inclines

Resolve weight into components parallel and normal to the incline. For a simple block with no other normal-direction forces,

\[
N=W\cos	heta.
\]

The downslope gravity component is \(W\sin	heta\). Compare required friction with \(\mu_sN\) to determine whether rest is possible.

\[W_\parallel=W\sin\theta,\qquad W_\perp=W\cos\theta\]

![FIG-02-30-004: Block on rough incline with weight components, normal force, and friction direction.](../figures/FIG-02-30-004-blocks-on-inclines.png)

### Worked Example 4

**Problem.** A block on a 20° incline weighs 500 N. Find normal force with no other normal loads.

**Solution.** N=500 cos20°=469.8 N.

---

## 30.5 Tipping versus Sliding

A rigid block under horizontal loading may slide or tip first. Sliding threshold follows friction; tipping threshold follows moment equilibrium when the normal reaction shifts to the edge of the base.

Compute both critical loads and the smaller one governs the first motion mode.

\[P_{\rm slide}=\mu_sN,\qquad \sum M_{\rm edge}=0\text{ for tipping}\]

![FIG-02-30-005: Block with applied force at height h, base width b, showing sliding and tipping thresholds.](../figures/FIG-02-30-005-tipping-versus-sliding.png)

### Worked Example 5

**Problem.** For Problem 4 with μs=0.50, is gravity alone enough to cause slip?

**Solution.** Required friction=500 sin20°=171.0 N; max=0.5(469.8)=234.9 N, so no.

---

## 30.6 Belt Friction

The Handbook gives the belt-friction relation

\[
F_1=F_2e^{\mu	heta},
\]

where \(	heta\) is contact angle in radians and the forces correspond to the tight and slack sides at impending slip.

The exponential relation applies to flexible belt/capstan contact under its model assumptions.

\[\frac{F_1}{F_2}=e^{\mu\theta}\]

![FIG-02-30-006: Belt wrapped around pulley through angle θ with tight-side F1 and slack-side F2.](../figures/FIG-02-30-006-belt-friction.png)

### Worked Example 6

**Problem.** What equation defines impending slip?

**Solution.** F=μsN.

---

## 30.7 Square-Thread Screw Friction

For a square-thread screw jack, the Handbook gives a torque relation involving mean thread radius, pitch angle, and friction angle \(\phi\) with \(\mu=	an\phi\).

Use the specified plus/minus form carefully for tightening/raising versus loosening/lowering. The self-locking behavior depends on geometry and friction.

\[M=Pr\tan(\alpha\pm\phi),\qquad \mu=\tan\phi\]

![FIG-02-30-007: Square-thread screw helix unwrapped into an inclined-plane analogy with pitch angle α and friction angle φ.](../figures/FIG-02-30-007-square-thread-screw-friction.png)

### Worked Example 7

**Problem.** Why compute both tipping and sliding thresholds for a tall block?

**Solution.** Whichever critical load is smaller occurs first.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A belt has μ=0.2, wrap θ=π rad, slack tension 100 N. Find tight tension at impending slip.

**Solution.** F1=100 exp(0.2π)=187.4 N.

### Worked Example 9

**Problem.** What angle unit is required in the belt formula?

**Solution.** Radians.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Statics, printed pp. 97–98; Dynamics pp. 109–110**.

**Source boundary:** The Handbook directly gives the static/kinetic friction laws, limiting friction, screw-thread relation, and belt-friction relation.

---

## Where This Goes Wrong

**Applying static friction before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying impending slip before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying kinetic friction before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying inclined-plane friction before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying tipping versus sliding before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying belt friction before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying screw friction before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| static friction | Concept developed in §30.1; apply only under that section's model assumptions. |
| impending slip | Concept developed in §30.2; apply only under that section's model assumptions. |
| kinetic friction | Concept developed in §30.3; apply only under that section's model assumptions. |
| inclined-plane friction | Concept developed in §30.4; apply only under that section's model assumptions. |
| tipping versus sliding | Concept developed in §30.5; apply only under that section's model assumptions. |
| belt friction | Concept developed in §30.6; apply only under that section's model assumptions. |
| screw friction | Concept developed in §30.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **static friction** and state the governing relation or modeling rule.

2. Define **impending slip** and state the governing relation or modeling rule.

3. Define **kinetic friction** and state the governing relation or modeling rule.

4. Define **inclined-plane friction** and state the governing relation or modeling rule.

5. Define **tipping versus sliding** and state the governing relation or modeling rule.

6. Define **belt friction** and state the governing relation or modeling rule.

7. Define **screw friction** and state the governing relation or modeling rule.

8. What error is likely if **static friction** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **impending slip** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **kinetic friction** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **inclined-plane friction** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **tipping versus sliding** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **belt friction** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **screw friction** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **static friction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **impending slip**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **kinetic friction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **inclined-plane friction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **tipping versus sliding**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **belt friction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **screw friction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **static friction**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **impending slip**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **static friction** is developed in §30.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **impending slip** is developed in §30.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **kinetic friction** is developed in §30.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **inclined-plane friction** is developed in §30.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **tipping versus sliding** is developed in §30.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **belt friction** is developed in §30.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **screw friction** is developed in §30.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **static friction**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **impending slip**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **kinetic friction**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **inclined-plane friction**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **tipping versus sliding**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **belt friction**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **screw friction**.

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

1. A 100-N block on a horizontal surface has μs=0.40. Find maximum static friction.

2. If the applied horizontal force in Problem 1 is 25 N and the block remains at rest, what is friction?

3. If μk=0.30 and the block slides, find kinetic friction.

4. A block on a 20° incline weighs 500 N. Find normal force with no other normal loads.

5. For Problem 4 with μs=0.50, is gravity alone enough to cause slip?

6. What equation defines impending slip?

7. Why compute both tipping and sliding thresholds for a tall block?

8. A belt has μ=0.2, wrap θ=π rad, slack tension 100 N. Find tight tension at impending slip.

9. What angle unit is required in the belt formula?

10. Why is static friction called reactive?


---

## Practice Problem Solutions

1. Fmax=0.40(100)=40 N if N=100 N.

2. 25 N opposite the applied force, not 40 N.

3. 30 N.

4. N=500 cos20°=469.8 N.

5. Required friction=500 sin20°=171.0 N; max=0.5(469.8)=234.9 N, so no.

6. F=μsN.

7. Whichever critical load is smaller occurs first.

8. F1=100 exp(0.2π)=187.4 N.

9. Radians.

10. It adjusts to the value needed to prevent motion until the limiting value is reached.


---

## Quick Reference

**Handbook anchor:** Statics, printed pp. 97–98; Dynamics pp. 109–110.

- **static friction:** Static Friction Is Reactive
- **impending slip:** Impending Motion
- **kinetic friction:** Kinetic Friction
- **inclined-plane friction:** Blocks on Inclines
- **tipping versus sliding:** Tipping versus Sliding
- **belt friction:** Belt Friction
- **screw friction:** Square-Thread Screw Friction
---

## What's Next

**02-31 — Particle Kinematics — Rectilinear Motion**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor