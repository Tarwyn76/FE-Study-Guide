---
chapter: "02-22"
title: "Constructing a Free-Body Diagram"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-022-01, MECH-2C-022-02, MECH-2C-022-03, MECH-2C-022-04, MECH-2C-022-05, MECH-2C-022-06, MECH-2C-022-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-22: Constructing a Free-Body Diagram

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 01-13 Vector Fundamentals · 01-02 Units and Dimensions

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines force as a vector, gives force resolution and equilibrium requirements, and defines concurrent forces/two-force bodies. The step-by-step free-body-diagram workflow is guide-developed engineering practice.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **22.1** Explain and apply **What a Free-Body Diagram Represents**.
* **22.2** Explain and apply **Choosing the Body or Subsystem**.
* **22.3** Explain and apply **Forces: Magnitude, Point of Application, and Direction**.
* **22.4** Explain and apply **Support Reactions in Two Dimensions**.
* **22.5** Explain and apply **Weight, Mass, and Distributed Weight**.
* **22.6** Explain and apply **Two-Force Members and Cables**.
* **22.7** Explain and apply **FBD Quality-Control Checklist**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 22.1 What a Free-Body Diagram Represents

A free-body diagram (FBD) replaces the physical surroundings of a selected body with the external forces and couple moments that those surroundings exert on it. The diagram is not a picture of the whole machine. It is a mechanics model of one isolated body or one selected subsystem.

The most important decision is the **system boundary**. Forces internal to the chosen system are not drawn; forces crossing the boundary are. A correct FBD therefore begins before any equilibrium equation is written.

\[\mathbf F=F_x\hat{\mathbf i}+F_y\hat{\mathbf j}\]

![FIG-02-22-001: Physical object beside its isolated free body, with the system boundary highlighted and only external forces retained.](../figures/FIG-02-22-001-what-a-free-body-diagram-represents.png)

### Worked Example 1

**Problem.** A 20-kg crate rests on a horizontal floor. Draw the FBD and find its weight using g=9.81 m/s².

**Solution.** Weight is W=20(9.81)=196.2 N downward; the floor normal is upward and equals 196.2 N if no other vertical forces act.

---

## 22.2 Choosing the Body or Subsystem

Choose the smallest body or subsystem that exposes the unknowns you need without creating unnecessary internal forces. A whole structure may be useful for finding support reactions; a cut member or joint may be better for finding internal forces.

If two connected bodies are isolated together, their mutual interaction forces become internal and disappear from the combined FBD. If they are isolated separately, the interaction appears on both diagrams as equal-and-opposite force pairs.

\[\text{external to chosen system}\Rightarrow \text{show on FBD}\]

![FIG-02-22-002: Same two-body assembly isolated as one combined system and then as two separate bodies, showing which interaction forces disappear or appear.](../figures/FIG-02-22-002-choosing-the-body-or-subsystem.png)

### Worked Example 2

**Problem.** A smooth roller contacts a horizontal surface. How many reaction components appear?

**Solution.** One, normal to the surface.

---

## 22.3 Forces: Magnitude, Point of Application, and Direction

The Handbook states that a force is defined by magnitude, point of application, and direction. Preserve all three when transferring a force to an FBD.

A cable tension acts along the cable. A smooth contact force acts normal to the surface. Weight acts through the center of gravity. An applied force must remain at its actual line of action unless it is replaced by a statically equivalent force-couple system.

\[F_x=F\cos\theta,\qquad F_y=F\sin\theta\]

![FIG-02-22-003: Force representation showing magnitude, line of action, point of application, and x-y components.](../figures/FIG-02-22-003-forces-magnitude-point-of-application-and-direction.png)

### Worked Example 3

**Problem.** A pin support in 2D is isolated. What reaction components may it exert?

**Solution.** Two force components, commonly Ax and Ay; no reaction couple for an ideal pin.

---

## 22.4 Support Reactions in Two Dimensions

Replace each support by the force or moment components it can exert. A smooth roller supplies one reaction normal to the surface. A pin supplies two force components. A fixed support can supply two force components and a reaction couple moment.

Do not draw reaction components a support cannot physically provide. Assumed directions may be chosen for unknown reactions; a negative solved value simply means the actual direction is opposite the assumption.

\[\text{roller: }1\text{ unknown}\quad\text{pin: }2\quad\text{fixed: }3\]

![FIG-02-22-004: 2D support-reaction reference showing roller, pin, cable/link, and fixed support with allowed reaction components.](../figures/FIG-02-22-004-support-reactions-in-two-dimensions.png)

### Worked Example 4

**Problem.** A cable pulls a ring. In what direction is cable tension drawn?

**Solution.** Along the cable, pulling away from the isolated ring.

---

## 22.5 Weight, Mass, and Distributed Weight

Weight is a force, not a mass. In SI, \(W=mg\). For a rigid body in a uniform gravitational field, the resultant weight acts through the center of gravity, which coincides with the mass center for uniform gravity.

When a body is modeled with a distributed weight, replace it by an equivalent resultant only when the chosen analysis permits that simplification; preserve its line of action through the distribution centroid.

\[W=mg\]

![FIG-02-22-005: Rigid body with distributed self-weight replaced by a single resultant W through the center of gravity.](../figures/FIG-02-22-005-weight-mass-and-distributed-weight.png)

### Worked Example 5

**Problem.** A link has exactly two pin forces and no other loads. What can be concluded?

**Solution.** It is a two-force member; the two forces are equal, opposite, and collinear.

---

## 22.6 Two-Force Members and Cables

A two-force body in static equilibrium has exactly two applied forces; those forces are equal in magnitude, opposite in direction, and collinear. This lets you replace an unknown pin reaction pair at a member end with a single axial member force.

An ideal cable carries tension only, directed away from the isolated body along the cable. Recognizing these constraints reduces unknowns before equations are written.

\[\mathbf F_A=-\mathbf F_B,\qquad \mathbf F_A\parallel AB\]

![FIG-02-22-006: Two-force link with collinear end forces and a cable with tension directed along its axis.](../figures/FIG-02-22-006-two-force-members-and-cables.png)

### Worked Example 6

**Problem.** Why are equal-and-opposite contact forces not both drawn on one body's FBD?

**Solution.** They act on different bodies; only the force acting on the isolated body belongs on that FBD.

---

## 22.7 FBD Quality-Control Checklist

Before solving, verify: the correct body is isolated; every external load is present; every support has only physically valid reactions; dimensions and angles needed for moments are shown; internal forces have not been mixed with external forces; and no action-reaction pair has been drawn on the same isolated body.

A clean FBD is a computational tool. If the FBD is wrong, correct algebra will only solve the wrong mechanics problem.

\[\boxed{\text{isolate}\rightarrow\text{replace contacts}\rightarrow\text{show loads}\rightarrow\text{add geometry}\rightarrow\text{check}}\]

![FIG-02-22-007: Five-step FBD checklist with common errors: missing force, impossible support reaction, duplicated action-reaction pair, and missing geometry.](../figures/FIG-02-22-007-fbd-quality-control-checklist.png)

### Worked Example 7

**Problem.** Where does uniform-gravity weight act for a rigid body?

**Solution.** Through the center of gravity, coincident with mass center under uniform gravity.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** If a solved reaction is negative, what does it mean?

**Solution.** The true reaction acts opposite the assumed direction.

### Worked Example 9

**Problem.** Why include dimensions on an FBD?

**Solution.** They locate lines of action and moment arms needed later.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Statics, printed pp. 95 and 98**.

**Source boundary:** The Handbook directly defines force as a vector, gives force resolution and equilibrium requirements, and defines concurrent forces/two-force bodies. The step-by-step free-body-diagram workflow is guide-developed engineering practice.

---

## Where This Goes Wrong

**Applying system boundary before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying body isolation before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying applied force before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying reaction force before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying weight force before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying two-force member before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying FBD audit before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| system boundary | Concept developed in §22.1; apply only under that section's model assumptions. |
| body isolation | Concept developed in §22.2; apply only under that section's model assumptions. |
| applied force | Concept developed in §22.3; apply only under that section's model assumptions. |
| reaction force | Concept developed in §22.4; apply only under that section's model assumptions. |
| weight force | Concept developed in §22.5; apply only under that section's model assumptions. |
| two-force member | Concept developed in §22.6; apply only under that section's model assumptions. |
| FBD audit | Concept developed in §22.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **system boundary** and state the governing relation or modeling rule.

2. Define **body isolation** and state the governing relation or modeling rule.

3. Define **applied force** and state the governing relation or modeling rule.

4. Define **reaction force** and state the governing relation or modeling rule.

5. Define **weight force** and state the governing relation or modeling rule.

6. Define **two-force member** and state the governing relation or modeling rule.

7. Define **FBD audit** and state the governing relation or modeling rule.

8. What error is likely if **system boundary** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **body isolation** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **applied force** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **reaction force** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **weight force** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **two-force member** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **FBD audit** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **system boundary**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **body isolation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **applied force**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **reaction force**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **weight force**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **two-force member**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **FBD audit**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **system boundary**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **body isolation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **system boundary** is developed in §22.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **body isolation** is developed in §22.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **applied force** is developed in §22.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **reaction force** is developed in §22.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **weight force** is developed in §22.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **two-force member** is developed in §22.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **FBD audit** is developed in §22.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **system boundary**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **body isolation**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **applied force**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **reaction force**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **weight force**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **two-force member**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **FBD audit**.

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

1. A 20-kg crate rests on a horizontal floor. Draw the FBD and find its weight using g=9.81 m/s².

2. A smooth roller contacts a horizontal surface. How many reaction components appear?

3. A pin support in 2D is isolated. What reaction components may it exert?

4. A cable pulls a ring. In what direction is cable tension drawn?

5. A link has exactly two pin forces and no other loads. What can be concluded?

6. Why are equal-and-opposite contact forces not both drawn on one body's FBD?

7. Where does uniform-gravity weight act for a rigid body?

8. If a solved reaction is negative, what does it mean?

9. Why include dimensions on an FBD?

10. State the five-step FBD workflow.


---

## Practice Problem Solutions

1. Weight is W=20(9.81)=196.2 N downward; the floor normal is upward and equals 196.2 N if no other vertical forces act.

2. One, normal to the surface.

3. Two force components, commonly Ax and Ay; no reaction couple for an ideal pin.

4. Along the cable, pulling away from the isolated ring.

5. It is a two-force member; the two forces are equal, opposite, and collinear.

6. They act on different bodies; only the force acting on the isolated body belongs on that FBD.

7. Through the center of gravity, coincident with mass center under uniform gravity.

8. The true reaction acts opposite the assumed direction.

9. They locate lines of action and moment arms needed later.

10. Isolate; replace contacts with reactions; show external loads; add required geometry/axes; audit for omissions/duplicates.


---

## Quick Reference

**Handbook anchor:** Statics, printed pp. 95 and 98.

- **system boundary:** What a Free-Body Diagram Represents
- **body isolation:** Choosing the Body or Subsystem
- **applied force:** Forces: Magnitude, Point of Application, and Direction
- **reaction force:** Support Reactions in Two Dimensions
- **weight force:** Weight, Mass, and Distributed Weight
- **two-force member:** Two-Force Members and Cables
- **FBD audit:** FBD Quality-Control Checklist
---

## What's Next

**02-23 — Equilibrium Equations for a 2D Concurrent Force System**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor