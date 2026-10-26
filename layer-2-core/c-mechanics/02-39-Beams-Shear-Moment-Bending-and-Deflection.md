---
chapter: "02-39"
title: "Beams — Shear, Moment, Bending, and Deflection"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-039-01, MECH-2C-039-02, MECH-2C-039-03, MECH-2C-039-04, MECH-2C-039-05, MECH-2C-039-06, MECH-2C-039-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-28 Distributed Loads · 02-29 Area Moments · 02-37 Stress/Strain

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives beam shear/moment sign conventions, load-shear-moment differential relations, bending and transverse-shear stress, beam-deflection differential equation, double integration, superposition, and transformed sections.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **39.1** Explain and apply **Internal Shear and Bending Moment**.
* **39.2** Explain and apply **Load-Shear-Moment Relations**.
* **39.3** Explain and apply **Shear and Moment Diagrams**.
* **39.4** Explain and apply **Bending Normal Stress**.
* **39.5** Explain and apply **Transverse Shear Stress**.
* **39.6** Explain and apply **Beam Deflection by Integration**.
* **39.7** Explain and apply **Superposition and Composite Sections**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 39.1 Internal Shear and Bending Moment

Cut the beam at the section of interest and apply equilibrium to one side. The exposed internal resultants include shear \(V\) and bending moment \(M\).

Use one sign convention consistently; the Handbook defines positive bending as concave upward and gives a corresponding positive-shear convention.

\[\sum F_y=0\Rightarrow V,\qquad \sum M_{\rm cut}=0\Rightarrow M\]

![FIG-02-39-001: Beam section cut showing internal shear V and bending moment M with positive sign convention.](../figures/FIG-02-39-001-internal-shear-and-bending-moment.png)

### Worked Example 1

**Problem.** A simply supported beam has a 10-kN central load over 4 m. Find reactions.

**Solution.** 5 kN each. Reasoning: this uses the **39.1 Internal Shear and Bending Moment** model from Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

<!-- VERIFY id="WE-02-39-001-RA" expr="10/2" expected="5" units="kN" atol="1e-9" rtol="1e-9" -->
<!-- VERIFY id="WE-02-39-001-RB" expr="10/2" expected="5" units="kN" atol="1e-9" rtol="1e-9" -->

## 39.2 Load-Shear-Moment Relations

The Handbook relates distributed load, shear, and bending moment through differentiation/integration.

These relations make diagram slopes and areas powerful checks.

\[\frac{dV}{dx}=-w(x),\qquad \frac{dM}{dx}=V(x)\]

![FIG-02-39-002: Aligned load, shear, and moment diagrams with slope/area relationships.](../figures/FIG-02-39-002-load-shear-moment-relations.png)

### Worked Example 2

**Problem.** For Problem 1, what is maximum moment?

**Solution.** Mmax=PL/4=10 kN·m. Reasoning: this uses the **39.2 Load-Shear-Moment Relations** model from Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

<!-- VERIFY id="WE-02-39-002-Mmax" expr="10*4/4" expected="10" units="kN*m" atol="1e-9" rtol="1e-9" -->

## 39.3 Shear and Moment Diagrams

Start with support reactions, then move along the beam. Point loads cause jumps in shear; applied concentrated moments cause jumps in the moment diagram. Distributed load changes shear continuously.

Local extrema in \(M\) occur where \(V=0\) in smooth regions.

\[\Delta V=-P,\qquad \Delta M=M_{\rm applied}\]

![FIG-02-39-003: Example w-V-M diagrams showing jumps and slopes.](../figures/FIG-02-39-003-shear-and-moment-diagrams.png)

### Worked Example 3

**Problem.** If a constant distributed load w=3 kN/m acts, what is dV/dx?

**Solution.** -3 kN/m. Reasoning: this uses the **39.3 Shear and Moment Diagrams** model from Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

<!-- VERIFY id="WE-02-39-003-dVdx" expr="-3" expected="-3" units="kN/m" atol="1e-9" rtol="1e-9" -->

## 39.4 Bending Normal Stress

For elastic bending about a centroidal principal axis,

\[
\sigma_x=-rac{My}{I}.
\]

Stress varies linearly through the depth and is zero at the neutral axis. The extreme magnitude is \(Mc/I=M/S\).

\[\sigma_{\max}=\frac{Mc}{I}=\frac{M}{S}\]

![FIG-02-39-004: Beam cross-section with linear tensile/compressive bending stress distribution and neutral axis.](../figures/FIG-02-39-004-bending-normal-stress.png)

### Worked Example 4

**Problem.** Where does a smooth-region moment diagram have an extremum?

**Solution.** Where V=0. Reasoning: this uses the **39.4 Bending Normal Stress** model from Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## 39.5 Transverse Shear Stress

The Handbook gives

\[
	au=rac{VQ}{Ib}.
\]

Here \(Q\) is the first moment of the area above or below the level where shear stress is evaluated, about the neutral axis. For rectangular sections, shear stress is zero at free top/bottom surfaces and maximum at the neutral axis.

\[\tau=\frac{VQ}{Ib},\qquad q=\frac{VQ}{I}\]

![FIG-02-39-005: Rectangular/I-beam cross-section with Q area, b thickness, and shear-stress distribution.](../figures/FIG-02-39-005-transverse-shear-stress.png)

### Worked Example 5

**Problem.** A rectangular beam has M=5 kN·m, I=8e-6 m^4, c=0.05 m. Find extreme bending stress.

**Solution.** σ=Mc/I=31.25 MPa. Reasoning: this uses the **39.5 Transverse Shear Stress** model from Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

<!-- VERIFY id="WE-02-39-005-stress" expr="5000*0.05/8e-6/1e6" expected="31.25" units="MPa" atol="1e-9" rtol="1e-9" -->

## 39.6 Beam Deflection by Integration

For small elastic deflection, the Handbook gives curvature relation \(1/
ho=M/(EI)\) and the differential equation

\[
EI\,y''=M(x)
\]

under the stated sign convention. Integrate twice and use boundary/continuity conditions to determine constants.

\[EI\frac{d^2y}{dx^2}=M(x)\]

![FIG-02-39-006: Beam elastic curve with slope, deflection, moment equation, and boundary conditions.](../figures/FIG-02-39-006-beam-deflection-by-integration.png)

### Worked Example 6

**Problem.** State the transverse shear formula.

**Solution.** τ=VQ/(Ib). Reasoning: this uses the **39.6 Beam Deflection by Integration** model from Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## 39.7 Superposition and Composite Sections

For linear elastic small-deflection problems, superposition allows responses from separate loads to be added. For beams of dissimilar materials, the Handbook uses transformed-section methods with modular ratio.

Both methods require linear behavior and consistent geometry/compatibility assumptions.

\[n=\frac{E_1}{E_2}\]

![FIG-02-39-007: Beam loads decomposed for superposition and a two-material section transformed by modular ratio.](../figures/FIG-02-39-007-superposition-and-composite-sections.png)

### Worked Example 7

**Problem.** Where is transverse shear zero on the top and bottom free surfaces of a rectangular beam?

**Solution.** At the free surfaces; maximum occurs at the neutral axis. Reasoning: this uses the **39.7 Superposition and Composite Sections** model from Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What differential relation connects beam moment and deflection?

**Solution.** EI y''=M(x) under the Handbook sign convention. Reasoning: this uses the **Integrated Worked Examples** model from Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

### Worked Example 9

**Problem.** What conditions determine integration constants in beam deflection?

**Solution.** Physical boundary and continuity conditions on slope/deflection. Reasoning: this uses the **Integrated Worked Examples** model from Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection. Apply the governing relation to the stated data with consistent units, preserve the section sign convention, and then check the result against the physical constraint described in that section.

---

## As the Handbook States It

### Source Boundary

- **FE-Handbook-supported** — For concepts marked `in_handbook` in the ledger, the cited FE Reference Handbook section/page supplies the formula, table, definition, or exam-scope anchor used by this chapter.
- **Externally supported** — Engineering LibreTexts, Mechanics of Materials (Roylance) (https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_of_Materials_%28Roylance%29) supports beam loading, shear and moment diagrams, flexural behavior, deflection, superposition, and composite-section reasoning.
- **Guide synthesis** — Worked-example sequencing, engineering interpretation, exam strategy, comparison heuristics, checklists, and explanatory derivations beyond the cited source statements are instructional synthesis developed for this guide.


Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Mechanics of Materials, printed pp. 135–137**.

**Source boundary:** The Handbook directly gives beam shear/moment sign conventions, load-shear-moment differential relations, bending and transverse-shear stress, beam-deflection differential equation, double integration, superposition, and transformed sections.

---

## Where This Goes Wrong

**Applying beam internal forces before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying load-shear-moment relation before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying shear-moment diagrams before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying bending stress before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying beam shear stress before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying beam deflection before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying beam superposition before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.

**Mixing area and mass moments of inertia.** They have different units and different physical roles.


---

## Key Terms

| Term | Working definition |
|---|---|
| beam internal forces | Concept developed in §39.1; apply only under that section's model assumptions. |
| load-shear-moment relation | Concept developed in §39.2; apply only under that section's model assumptions. |
| shear-moment diagrams | Concept developed in §39.3; apply only under that section's model assumptions. |
| bending stress | Concept developed in §39.4; apply only under that section's model assumptions. |
| beam shear stress | Concept developed in §39.5; apply only under that section's model assumptions. |
| beam deflection | Concept developed in §39.6; apply only under that section's model assumptions. |
| beam superposition | Concept developed in §39.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **beam internal forces** and state the governing relation or modeling rule.

2. Define **load-shear-moment relation** and state the governing relation or modeling rule.

3. Define **shear-moment diagrams** and state the governing relation or modeling rule.

4. Define **bending stress** and state the governing relation or modeling rule.

5. Define **beam shear stress** and state the governing relation or modeling rule.

6. Define **beam deflection** and state the governing relation or modeling rule.

7. Define **beam superposition** and state the governing relation or modeling rule.

8. What error is likely if **beam internal forces** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **load-shear-moment relation** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **shear-moment diagrams** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **bending stress** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **beam shear stress** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **beam deflection** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **beam superposition** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **beam internal forces**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **load-shear-moment relation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **shear-moment diagrams**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **bending stress**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **beam shear stress**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **beam deflection**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **beam superposition**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **beam internal forces**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **load-shear-moment relation**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **beam internal forces** is developed in §39.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **load-shear-moment relation** is developed in §39.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **shear-moment diagrams** is developed in §39.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **bending stress** is developed in §39.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **beam shear stress** is developed in §39.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **beam deflection** is developed in §39.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **beam superposition** is developed in §39.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **beam internal forces**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **load-shear-moment relation**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **shear-moment diagrams**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **bending stress**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **beam shear stress**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **beam deflection**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **beam superposition**.

15. Create the chapter-specific mechanics model for **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection** before solving: define the body or system, coordinates, geometry, loads, constraints, and unknowns that enter the governing equations.

16. Independently verify a result in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection** by substituting it back into the governing equation, checking units and signs, and testing equilibrium, compatibility, or a limiting case as appropriate.

17. A negative result reverses an assumed direction only when the physical element can act in that opposite sense. In **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**, also test whether unilateral contact, tension-only, or compression-only behavior changes the model.

18. Match the Handbook coordinate and sign convention before comparing expressions in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. A different positive direction can reverse component or moment signs while leaving the physical state unchanged.

19. **A.** The nineteenth review item tests **beam internal forces** in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

20. **A.** The twentieth review item tests **load-shear-moment relation** in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

21. **A.** The twenty-first review item tests **shear-moment diagrams** in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

22. **A.** The twenty-second review item tests **bending stress** in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

23. **A.** The twenty-third review item tests **beam shear stress** in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

24. **A.** The twenty-fourth review item tests **beam deflection** in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

25. **A.** The twenty-fifth review item tests **beam superposition** in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

26. **A.** The twenty-sixth review item tests **beam internal forces** in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention. This application check also tests whether the model assumptions are established before any numerical or symbolic manipulation.

27. **A.** The twenty-seventh review item tests **load-shear-moment relation** in **Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention. This final application check emphasizes that a valid mechanics relation cannot replace the diagram, geometry, and constraints that define the problem.

---

## Practice Problems

1. A simply supported beam has a 10-kN central load over 4 m. Find reactions.

2. For Problem 1, what is maximum moment?

3. If a constant distributed load w=3 kN/m acts, what is dV/dx?

4. Where does a smooth-region moment diagram have an extremum?

5. A rectangular beam has M=5 kN·m, I=8e-6 m^4, c=0.05 m. Find extreme bending stress.

6. State the transverse shear formula.

7. Where is transverse shear zero on the top and bottom free surfaces of a rectangular beam?

8. What differential relation connects beam moment and deflection?

9. What conditions determine integration constants in beam deflection?

10. When is superposition valid?


---

## Practice Problem Solutions

1. 5 kN each. Practice verification: use the **39.1 Internal Shear and Bending Moment** relation for Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

2. Mmax=PL/4=10 kN·m. Practice verification: use the **39.2 Load-Shear-Moment Relations** relation for Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

3. -3 kN/m. Practice verification: use the **39.3 Shear and Moment Diagrams** relation for Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

4. Where V=0. Practice verification: use the **39.4 Bending Normal Stress** relation for Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

5. σ=Mc/I=31.25 MPa. Practice verification: use the **39.5 Transverse Shear Stress** relation for Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

6. τ=VQ/(Ib). Practice verification: use the **39.6 Beam Deflection by Integration** relation for Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection, retain the stated sign convention and units, and confirm that the result is consistent with the section's equilibrium, kinematic, or constitutive constraint.

7. At the free surfaces; maximum occurs at the neutral axis.

8. EI y''=M(x) under the Handbook sign convention.

9. Physical boundary and continuity conditions on slope/deflection.

10. For linear response with small deformations that do not change load application conditions.

---

## Quick Reference

**Handbook anchor:** Mechanics of Materials, printed pp. 135–137.

- **beam internal forces:** Internal Shear and Bending Moment
- **load-shear-moment relation:** Load-Shear-Moment Relations
- **shear-moment diagrams:** Shear and Moment Diagrams
- **bending stress:** Bending Normal Stress
- **beam shear stress:** Transverse Shear Stress
- **beam deflection:** Beam Deflection by Integration
- **beam superposition:** Superposition and Composite Sections
---

## What's Next

**02-40 — Combined Stress, Principal Stress, and Mohr's Circle**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor