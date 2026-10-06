---
chapter: "02-24"
title: "Method of Joints for Planar Trusses"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-024-01, MECH-2C-024-02, MECH-2C-024-03, MECH-2C-024-04, MECH-2C-024-05, MECH-2C-024-06, MECH-2C-024-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-24: Method of Joints for Planar Trusses

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-23 2D Concurrent Equilibrium

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly describes statically determinate trusses, zero-force-member rules, and the method of joints.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **24.1** Explain and apply **Ideal Planar Truss Model**.
* **24.2** Explain and apply **Determinacy and Stability**.
* **24.3** Explain and apply **Zero-Force Members**.
* **24.4** Explain and apply **Support Reactions Before Joint Analysis**.
* **24.5** Explain and apply **Method of Joints**.
* **24.6** Explain and apply **Tension and Compression Sign Interpretation**.
* **24.7** Explain and apply **Efficient Joint Order and Global Check**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 24.1 Ideal Planar Truss Model

An ideal planar truss is composed of straight two-force members joined by frictionless pins, with external loads and support reactions applied at joints. Under these assumptions, each member carries only axial tension or compression.

If loads are applied between joints or joints transmit moments, the simple truss model is no longer exact and member bending may matter.

\[\text{member force acts along member axis}\]

![FIG-02-24-001: Ideal planar pin-jointed truss with joint loads and axial member forces.](../figures/FIG-02-24-001-ideal-planar-truss-model.png)

### Worked Example 1

**Problem.** For a simple planar truss with j=6 and r=3, what member count satisfies m+r=2j?

**Solution.** m=2(6)-3=9.

---

## 24.2 Determinacy and Stability

For a simple planar truss, the count \(m+r=2j\) is a useful determinacy check, where \(m\) is members, \(r\) support reaction components, and \(j\) joints.

The count is necessary but not sufficient for geometric stability. A poorly arranged truss can satisfy the equation and still form a mechanism.

\[m+r=2j\]

![FIG-02-24-002: Stable and unstable trusses with member/joint/reaction counts.](../figures/FIG-02-24-002-determinacy-and-stability.png)

### Worked Example 2

**Problem.** At an unloaded joint, two noncollinear members meet. What are their forces?

**Solution.** Both are zero-force members.

---

## 24.3 Zero-Force Members

The Handbook gives two common rules. At an unloaded joint with only two noncollinear members, both are zero-force members. At an unloaded joint with three members where two are collinear, the third noncollinear member is zero force.

Zero-force members are not useless; they may stabilize the structure for different loading cases or prevent buckling.

\[\text{unloaded joint + geometry rules}\Rightarrow F=0\]

![FIG-02-24-003: Two standard zero-force-member joint configurations with the zero member highlighted.](../figures/FIG-02-24-003-zero-force-members.png)

### Worked Example 3

**Problem.** At an unloaded joint, three members meet and two are collinear. What about the third?

**Solution.** The noncollinear member is zero force.

---

## 24.4 Support Reactions Before Joint Analysis

When convenient, analyze the entire truss as a rigid body to determine external support reactions before solving member forces. This reduces the number of unknowns at each joint.

Select a moment center that eliminates as many support unknowns as possible.

\[\sum F_x=0,\quad\sum F_y=0,\quad\sum M_O=0\]

![FIG-02-24-004: Whole-truss FBD with pin and roller reactions and a moment equation about one support.](../figures/FIG-02-24-004-support-reactions-before-joint-analysis.png)

### Worked Example 4

**Problem.** Why are support reactions often solved before joints?

**Solution.** They become known external forces at joints and reduce unknowns.

---

## 24.5 Method of Joints

Isolate a joint with no more than two unknown member forces. Assume unknown members are in tension, pulling away from the joint. Apply the two planar force-equilibrium equations.

Move systematically from solved joints to adjacent joints. A negative calculated tension means the member is actually in compression.

\[\sum F_x=0,\qquad\sum F_y=0\]

![FIG-02-24-005: Isolated truss joint with assumed tensile member-force arrows and component equations.](../figures/FIG-02-24-005-method-of-joints.png)

### Worked Example 5

**Problem.** How many unknown member forces should an ideal starting joint have?

**Solution.** No more than two for direct use of ΣFx=0 and ΣFy=0.

---

## 24.6 Tension and Compression Sign Interpretation

A consistent sign convention prevents relabeling errors. The common approach is to assume every unknown member is in tension. Positive results remain tension; negative results are compression.

Always report the physical state, not merely the sign.

\[F>0:\text{ tension (assumed)}\qquad F<0:\text{ compression}\]

![FIG-02-24-006: Same member shown in tension and compression with joint-end force directions.](../figures/FIG-02-24-006-tension-and-compression-sign-interpretation.png)

### Worked Example 6

**Problem.** If a member assumed in tension solves to -12 kN, report its state.

**Solution.** 12 kN compression.

---

## 24.7 Efficient Joint Order and Global Check

Start at a joint with one or two unknowns. Use zero-force rules early. Avoid beginning at a joint with three unknown member forces because only two independent equations are available.

After solving, check a previously unused joint or verify overall external equilibrium. The forces at every joint should close vectorially.

\[\sum\mathbf F_{\rm joint}=\mathbf0\]

![FIG-02-24-007: Truss solution path highlighting best starting joint, zero-force members, and progression through adjacent joints.](../figures/FIG-02-24-007-efficient-joint-order-and-global-check.png)

### Worked Example 7

**Problem.** What force type exists in an ideal truss member?

**Solution.** Axial tension or compression only.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Why are loads assumed applied at joints?

**Solution.** Otherwise members develop bending/shear and cease to be ideal two-force members.

### Worked Example 9

**Problem.** How can you check a completed method-of-joints solution?

**Solution.** Check equilibrium at an unused joint or whole-truss equilibrium.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Statics, printed p. 98**.

**Source boundary:** The Handbook directly describes statically determinate trusses, zero-force-member rules, and the method of joints.

---

## Where This Goes Wrong

**Applying truss model before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying truss determinacy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying zero-force member before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying truss reactions before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying method of joints before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying member force before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying joint-order strategy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| truss model | Concept developed in §24.1; apply only under that section's model assumptions. |
| truss determinacy | Concept developed in §24.2; apply only under that section's model assumptions. |
| zero-force member | Concept developed in §24.3; apply only under that section's model assumptions. |
| truss reactions | Concept developed in §24.4; apply only under that section's model assumptions. |
| method of joints | Concept developed in §24.5; apply only under that section's model assumptions. |
| member force | Concept developed in §24.6; apply only under that section's model assumptions. |
| joint-order strategy | Concept developed in §24.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **truss model** and state the governing relation or modeling rule.

2. Define **truss determinacy** and state the governing relation or modeling rule.

3. Define **zero-force member** and state the governing relation or modeling rule.

4. Define **truss reactions** and state the governing relation or modeling rule.

5. Define **method of joints** and state the governing relation or modeling rule.

6. Define **member force** and state the governing relation or modeling rule.

7. Define **joint-order strategy** and state the governing relation or modeling rule.

8. What error is likely if **truss model** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **truss determinacy** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **zero-force member** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **truss reactions** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **method of joints** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **member force** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **joint-order strategy** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **truss model**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **truss determinacy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **zero-force member**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **truss reactions**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **method of joints**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **member force**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **joint-order strategy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **truss model**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **truss determinacy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **truss model** is developed in §24.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **truss determinacy** is developed in §24.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **zero-force member** is developed in §24.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **truss reactions** is developed in §24.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **method of joints** is developed in §24.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **member force** is developed in §24.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **joint-order strategy** is developed in §24.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **truss model**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **truss determinacy**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **zero-force member**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **truss reactions**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **method of joints**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **member force**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **joint-order strategy**.

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

1. For a simple planar truss with j=6 and r=3, what member count satisfies m+r=2j?

2. At an unloaded joint, two noncollinear members meet. What are their forces?

3. At an unloaded joint, three members meet and two are collinear. What about the third?

4. Why are support reactions often solved before joints?

5. How many unknown member forces should an ideal starting joint have?

6. If a member assumed in tension solves to -12 kN, report its state.

7. What force type exists in an ideal truss member?

8. Why are loads assumed applied at joints?

9. How can you check a completed method-of-joints solution?

10. What does m+r=2j fail to guarantee?


---

## Practice Problem Solutions

1. m=2(6)-3=9.

2. Both are zero-force members.

3. The noncollinear member is zero force.

4. They become known external forces at joints and reduce unknowns.

5. No more than two for direct use of ΣFx=0 and ΣFy=0.

6. 12 kN compression.

7. Axial tension or compression only.

8. Otherwise members develop bending/shear and cease to be ideal two-force members.

9. Check equilibrium at an unused joint or whole-truss equilibrium.

10. Geometric stability; a mechanism can satisfy the count.


---

## Quick Reference

**Handbook anchor:** Statics, printed p. 98.

- **truss model:** Ideal Planar Truss Model
- **truss determinacy:** Determinacy and Stability
- **zero-force member:** Zero-Force Members
- **truss reactions:** Support Reactions Before Joint Analysis
- **method of joints:** Method of Joints
- **member force:** Tension and Compression Sign Interpretation
- **joint-order strategy:** Efficient Joint Order and Global Check
---

## What's Next

**02-25 — Moments, Couples, and Equivalent Force Systems**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor