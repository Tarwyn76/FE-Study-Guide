---
chapter: "02-37"
title: "Stress, Strain, and Axial/Thermal Deformation"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-037-01, MECH-2C-037-02, MECH-2C-037-03, MECH-2C-037-04, MECH-2C-037-05, MECH-2C-037-06, MECH-2C-037-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-37: Stress, Strain, and Axial/Thermal Deformation

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-17 Material Properties · 02-26 Equilibrium

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives engineering strain, uniaxial stress/deformation, Hooke's law, elastic constants, thermal deformation, pressure-vessel relations, and plane-stress constitutive equations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **37.1** Explain and apply **Normal Stress and Average Axial Stress**.
* **37.2** Explain and apply **Engineering Strain and Elastic Modulus**.
* **37.3** Explain and apply **Axial Deformation**.
* **37.4** Explain and apply **Poisson's Ratio and Elastic Constants**.
* **37.5** Explain and apply **Thermal Deformation**.
* **37.6** Explain and apply **Statically Indeterminate Axial Members**.
* **37.7** Explain and apply **Thin-Walled Pressure Vessels**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 37.1 Normal Stress and Average Axial Stress

For a prismatic member carrying centric axial load \(P\), average normal stress is

\[
\sigma=rac{P}{A}.
\]

Tension is commonly positive and compression negative. The relation is an average over the section and does not capture stress concentrations near load application or abrupt geometry changes.

\[\sigma=\frac{P}{A}\]

![FIG-02-37-001: Prismatic bar in tension with load P and cross-section A.](../figures/FIG-02-37-001-normal-stress-and-average-axial-stress.png)

### Worked Example 1

**Problem.** A 20-kN axial load acts on 400 mm². Find stress.

**Solution.** σ=20000/400=50 MPa.

---

## 37.2 Engineering Strain and Elastic Modulus

Engineering strain is change in length divided by original length. In the linear elastic uniaxial range, Hooke's law relates stress and strain through Young's modulus \(E\).

Modulus measures stiffness, not strength.

\[\varepsilon=\frac{\delta}{L},\qquad \sigma=E\varepsilon\]

![FIG-02-37-002: Linear elastic segment of stress-strain curve showing slope E.](../figures/FIG-02-37-002-engineering-strain-and-elastic-modulus.png)

### Worked Example 2

**Problem.** A 2-m bar elongates 1 mm. Find engineering strain.

**Solution.** ε=0.001/2=0.0005.

---

## 37.3 Axial Deformation

Combining equilibrium, stress, strain, and Hooke's law gives axial deformation for a uniform prismatic member.

For multiple segments, sum each segment's signed deformation. For continuously varying \(P(x),A(x),E(x)\), integrate.

\[\delta=\frac{PL}{AE},\qquad \delta=\int\frac{P(x)}{A(x)E(x)}dx\]

![FIG-02-37-003: Stepped axial bar with segment loads, lengths, areas, and summed elongations.](../figures/FIG-02-37-003-axial-deformation.png)

### Worked Example 3

**Problem.** If E=200 GPa and ε=0.0005, find stress.

**Solution.** σ=100 MPa.

---

## 37.4 Poisson's Ratio and Elastic Constants

Poisson's ratio relates lateral contraction to longitudinal extension in uniaxial loading.

For isotropic linear elastic material, the Handbook gives a relation among Young's modulus, shear modulus, and Poisson's ratio.

\[\nu=-\frac{\varepsilon_{\rm lateral}}{\varepsilon_{\rm longitudinal}},\qquad G=\frac{E}{2(1+\nu)}\]

![FIG-02-37-004: Axially stretched element showing longitudinal extension and lateral contraction.](../figures/FIG-02-37-004-poisson-s-ratio-and-elastic-constants.png)

### Worked Example 4

**Problem.** A uniform bar P=30 kN, L=2 m, A=300 mm², E=200 GPa. Find elongation.

**Solution.** δ=PL/AE=0.001 m=1.0 mm.

---

## 37.5 Thermal Deformation

For a free member under uniform temperature change,

\[
\delta_T=lpha L\Delta T.
\]

If expansion or contraction is restrained, thermal strain contributes to stress. A fully restrained uniaxial member under ideal linear-elastic conditions develops \(\sigma=-Elpha\Delta T\).

\[\varepsilon_T=\alpha\Delta T,\qquad \delta_T=\alpha L\Delta T\]

![FIG-02-37-005: Free-heating bar expanding versus restrained bar developing compressive thermal stress.](../figures/FIG-02-37-005-thermal-deformation.png)

### Worked Example 5

**Problem.** A steel bar α=12e-6/K, L=3 m, ΔT=50 K. Find free expansion.

**Solution.** δ=12e-6(3)(50)=0.0018 m=1.8 mm.

---

## 37.6 Statically Indeterminate Axial Members

When reaction unknowns exceed available equilibrium equations, compatibility of deformation supplies additional equations.

Typical compatibility statements specify equal displacements at connected points or zero net deformation between rigid supports.

\[\text{equilibrium}+\text{compatibility}+\text{constitutive law}\]

![FIG-02-37-006: Bar between rigid supports with multiple segments and zero total deformation compatibility.](../figures/FIG-02-37-006-statically-indeterminate-axial-members.png)

### Worked Example 6

**Problem.** If the bar in Problem 5 is fully restrained and E=200 GPa, find thermal stress magnitude.

**Solution.** |σ|=EαΔT=120 MPa compressive for heating.

---

## 37.7 Thin-Walled Pressure Vessels

For thin-walled cylindrical vessels, the Handbook gives hoop and axial membrane stresses. The thin-wall approximation applies when wall thickness is small relative to radius.

Hoop stress is twice the axial stress for the same pressure, radius, and thickness in a closed-end cylinder.

\[\sigma_h=\frac{pr}{t},\qquad \sigma_a=\frac{pr}{2t}\]

![FIG-02-37-007: Thin-walled closed cylinder with internal pressure, hoop stress, and axial stress directions.](../figures/FIG-02-37-007-thin-walled-pressure-vessels.png)

### Worked Example 7

**Problem.** If ν=0.30 and E=200 GPa, find G.

**Solution.** G=E/[2(1+ν)]=76.9 GPa.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Thin cylinder p=2 MPa, r=0.25 m, t=5 mm. Find hoop stress.

**Solution.** σh=pr/t=100 MPa.

### Worked Example 9

**Problem.** For Problem 8, find axial stress.

**Solution.** σa=pr/(2t)=50 MPa.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Mechanics of Materials, printed pp. 130–134**.

**Source boundary:** The Handbook directly gives engineering strain, uniaxial stress/deformation, Hooke's law, elastic constants, thermal deformation, pressure-vessel relations, and plane-stress constitutive equations.

---

## Where This Goes Wrong

**Applying axial stress before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying axial strain before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying axial deformation before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying Poisson ratio before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying thermal deformation before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying axial compatibility before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying thin-wall pressure vessel before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| axial stress | Concept developed in §37.1; apply only under that section's model assumptions. |
| axial strain | Concept developed in §37.2; apply only under that section's model assumptions. |
| axial deformation | Concept developed in §37.3; apply only under that section's model assumptions. |
| Poisson ratio | Concept developed in §37.4; apply only under that section's model assumptions. |
| thermal deformation | Concept developed in §37.5; apply only under that section's model assumptions. |
| axial compatibility | Concept developed in §37.6; apply only under that section's model assumptions. |
| thin-wall pressure vessel | Concept developed in §37.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **axial stress** and state the governing relation or modeling rule.

2. Define **axial strain** and state the governing relation or modeling rule.

3. Define **axial deformation** and state the governing relation or modeling rule.

4. Define **Poisson ratio** and state the governing relation or modeling rule.

5. Define **thermal deformation** and state the governing relation or modeling rule.

6. Define **axial compatibility** and state the governing relation or modeling rule.

7. Define **thin-wall pressure vessel** and state the governing relation or modeling rule.

8. What error is likely if **axial stress** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **axial strain** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **axial deformation** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **Poisson ratio** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **thermal deformation** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **axial compatibility** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **thin-wall pressure vessel** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **axial stress**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **axial strain**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **axial deformation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **Poisson ratio**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **thermal deformation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **axial compatibility**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **thin-wall pressure vessel**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **axial stress**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **axial strain**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **axial stress** is developed in §37.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **axial strain** is developed in §37.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **axial deformation** is developed in §37.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **Poisson ratio** is developed in §37.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **thermal deformation** is developed in §37.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **axial compatibility** is developed in §37.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **thin-wall pressure vessel** is developed in §37.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **axial stress**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **axial strain**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **axial deformation**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **Poisson ratio**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **thermal deformation**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **axial compatibility**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **thin-wall pressure vessel**.

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

1. A 20-kN axial load acts on 400 mm². Find stress.

2. A 2-m bar elongates 1 mm. Find engineering strain.

3. If E=200 GPa and ε=0.0005, find stress.

4. A uniform bar P=30 kN, L=2 m, A=300 mm², E=200 GPa. Find elongation.

5. A steel bar α=12e-6/K, L=3 m, ΔT=50 K. Find free expansion.

6. If the bar in Problem 5 is fully restrained and E=200 GPa, find thermal stress magnitude.

7. If ν=0.30 and E=200 GPa, find G.

8. Thin cylinder p=2 MPa, r=0.25 m, t=5 mm. Find hoop stress.

9. For Problem 8, find axial stress.

10. What additional relation is needed for an axially indeterminate restrained system?


---

## Practice Problem Solutions

1. σ=20000/400=50 MPa.

2. ε=0.001/2=0.0005.

3. σ=100 MPa.

4. δ=PL/AE=0.001 m=1.0 mm.

5. δ=12e-6(3)(50)=0.0018 m=1.8 mm.

6. |σ|=EαΔT=120 MPa compressive for heating.

7. G=E/[2(1+ν)]=76.9 GPa.

8. σh=pr/t=100 MPa.

9. σa=pr/(2t)=50 MPa.

10. A deformation compatibility equation.


---

## Quick Reference

**Handbook anchor:** Mechanics of Materials, printed pp. 130–134.

- **axial stress:** Normal Stress and Average Axial Stress
- **axial strain:** Engineering Strain and Elastic Modulus
- **axial deformation:** Axial Deformation
- **Poisson ratio:** Poisson's Ratio and Elastic Constants
- **thermal deformation:** Thermal Deformation
- **axial compatibility:** Statically Indeterminate Axial Members
- **thin-wall pressure vessel:** Thin-Walled Pressure Vessels
---

## What's Next

**02-38 — Torsion**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor