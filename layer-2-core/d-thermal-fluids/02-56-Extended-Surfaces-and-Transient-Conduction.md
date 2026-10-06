---
chapter: "02-56"
title: "Extended Surfaces and Transient Conduction"
layer: 2
tier: D
template: technical
ledger_ids: [HT-2D-056-01, HT-2D-056-02, HT-2D-056-03, HT-2D-056-04, HT-2D-056-05, HT-2D-056-06, HT-2D-056-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-56: Extended Surfaces and Transient Conduction

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-55 Conduction and Thermal Resistance · 01-16 Exponential Functions

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives lumped-capacitance validity and response, one-term transient-conduction approximations with Biot/Fourier numbers, and straight-fin relations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **56.1** Explain and apply **Biot Number and Lumped-Capacitance Criterion**.
* **56.2** Explain and apply **Lumped Transient Temperature Response**.
* **56.3** Explain and apply **Total Heat Transfer During Lumped Cooling/Heating**.
* **56.4** Explain and apply **Fourier Number and Distributed Transient Conduction**.
* **56.5** Explain and apply **One-Term Approximation**.
* **56.6** Explain and apply **Straight Fins and Corrected Length**.
* **56.7** Explain and apply **Fin Heat Rate and Effectiveness**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 56.1 Biot Number and Lumped-Capacitance Criterion

The Biot number compares internal conduction resistance to external convection resistance. When the Handbook criterion \(Bi<0.1\) is satisfied, the solid can be treated as spatially uniform in temperature at each instant.

Use characteristic length \(L_c=V/A_s\) for the lumped model.

\[Bi=\frac{hV}{kA_s}=\frac{hL_c}{k}\]

![FIG-02-56-001: Solid with internal conduction and external convection resistances illustrating Biot number.](../figures/FIG-02-56-001-biot-number-and-lumped-capacitance-criterion.png)

### Worked Example 1

**Problem.** A lumped body has h=20, V=0.001 m³, As=0.06 m², k=50 W/mK. Find Bi.

**Solution.** Bi=hV/(kAs)=0.00667.

---

## 56.2 Lumped Transient Temperature Response

For a body with uniform internal temperature exposed to a constant-temperature fluid, the lumped solution is exponential.

The thermal time constant is \(	au=ho Vc_p/(hA_s)\).

\[\frac{T-T_\infty}{T_i-T_\infty}=\exp\left(-\frac{hA_s}{\rho Vc_p}t\right)\]

![FIG-02-56-002: Exponential heating/cooling curve with thermal time constant.](../figures/FIG-02-56-002-lumped-transient-temperature-response.png)

### Worked Example 2

**Problem.** Is lumped capacitance valid for Problem 1 under Bi<0.1?

**Solution.** Yes.

---

## 56.3 Total Heat Transfer During Lumped Cooling/Heating

Energy transferred up to time \(t\) equals the body's change in sensible internal energy under the lumped assumptions.

The sign depends on whether the body heats or cools; magnitude follows \(mc_p|T-T_i|\).

\[Q_{\rm body}=m c_p(T-T_i)\]

![FIG-02-56-003: Lumped body with initial/current temperatures and cumulative heat transfer.](../figures/FIG-02-56-003-total-heat-transfer-during-lumped-cooling-heating.png)

### Worked Example 3

**Problem.** ρ=7800, V=0.001, cp=500, h=20, As=0.06. Find time constant.

**Solution.** τ=ρVcp/(hAs)=3250 s.

---

## 56.4 Fourier Number and Distributed Transient Conduction

When internal temperature gradients matter, transient conduction depends on Fourier number \(Fo=lpha t/L^2\) and Biot number.

The Handbook provides one-term approximations for plane walls, infinite cylinders, and spheres under sudden convection.

\[Fo=\frac{\alpha t}{L^2},\qquad \alpha=\frac{k}{\rho c_p}\]

![FIG-02-56-004: Bi-Fo map distinguishing lumped and spatially varying transient-conduction models.](../figures/FIG-02-56-004-fourier-number-and-distributed-transient-conduction.png)

### Worked Example 4

**Problem.** For Problem 3, find temperature ratio θ/θi after one time constant.

**Solution.** e^-1=0.3679.

---

## 56.5 One-Term Approximation

For sufficiently large Fourier number under the Handbook criteria, centerline temperature ratio is approximated using coefficients determined by Bi.

Spatial temperature ratios are then obtained from the corresponding eigenfunction form for wall, cylinder, or sphere.

\[\frac{\theta_0}{\theta_i}\approx C_1e^{-\zeta_1^2Fo}\]

![FIG-02-56-005: Plane wall with centerline and surface temperatures and one-term coefficient table concept.](../figures/FIG-02-56-005-one-term-approximation.png)

### Worked Example 5

**Problem.** k=15, ρ=8000, cp=500. Find thermal diffusivity.

**Solution.** α=15/(8000*500)=3.75e-6 m²/s.

---

## 56.6 Straight Fins and Corrected Length

Fins increase convective area. The Handbook gives straight-fin relations using \(m=\sqrt{hP/(kA_c)}\) and a corrected length for an insulated-tip approximation.

High fin conductivity, large perimeter, and adequate length improve performance, but fin efficiency is less than 1.

\[m=\sqrt{\frac{hP}{kA_c}}\]

![FIG-02-56-006: Rectangular and pin fins with base temperature, perimeter, cross-sectional area, and corrected length.](../figures/FIG-02-56-006-straight-fins-and-corrected-length.png)

### Worked Example 6

**Problem.** For L=0.02 m and t=100 s with α from Problem 5, find Fo.

**Solution.** Fo=0.9375.

---

## 56.7 Fin Heat Rate and Effectiveness

For a straight uniform fin with the Handbook assumptions, heat transfer can be expressed with hyperbolic functions or corrected-length approximations.

Fin effectiveness compares heat transfer with the fin to what the base area would transfer without the fin. Added area is useful only when it produces enough extra heat transfer to justify the fin.

\[\varepsilon_f=\frac{\dot Q_{\rm fin}}{hA_b(T_b-T_\infty)}\]

![FIG-02-56-007: Bare base versus finned base showing increased area and fin temperature decay.](../figures/FIG-02-56-007-fin-heat-rate-and-effectiveness.png)

### Worked Example 7

**Problem.** What does Bi compare?

**Solution.** Internal conduction resistance to external convection resistance.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What does Fo represent?

**Solution.** Nondimensional elapsed diffusion time.

### Worked Example 9

**Problem.** Why do fins help heat transfer?

**Solution.** They increase exposed convective area.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Heat Transfer, printed pp. 211–214**.

**Source boundary:** The Handbook directly gives lumped-capacitance validity and response, one-term transient-conduction approximations with Biot/Fourier numbers, and straight-fin relations.

---

## Where This Goes Wrong

**Using Biot number outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using lumped capacitance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using transient heat content outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Fourier number outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using one-term transient solution outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using fin parameter outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using fin effectiveness outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| Biot number | Concept developed in §56.1; use the section definition and conditions. |
| lumped capacitance | Concept developed in §56.2; use the section definition and conditions. |
| transient heat content | Concept developed in §56.3; use the section definition and conditions. |
| Fourier number | Concept developed in §56.4; use the section definition and conditions. |
| one-term transient solution | Concept developed in §56.5; use the section definition and conditions. |
| fin parameter | Concept developed in §56.6; use the section definition and conditions. |
| fin effectiveness | Concept developed in §56.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **Biot number** and state the governing equation or modeling rule.

2. Define **lumped capacitance** and state the governing equation or modeling rule.

3. Define **transient heat content** and state the governing equation or modeling rule.

4. Define **Fourier number** and state the governing equation or modeling rule.

5. Define **one-term transient solution** and state the governing equation or modeling rule.

6. Define **fin parameter** and state the governing equation or modeling rule.

7. Define **fin effectiveness** and state the governing equation or modeling rule.

8. What is the most likely error if **Biot number** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **lumped capacitance** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **transient heat content** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **Fourier number** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **one-term transient solution** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **fin parameter** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **fin effectiveness** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **Biot number**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **lumped capacitance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **transient heat content**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **Fourier number**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **one-term transient solution**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **fin parameter**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **fin effectiveness**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **Biot number**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **lumped capacitance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **Biot number** is developed in §56.1. Use the displayed relation together with that section's assumptions and units.

2. **lumped capacitance** is developed in §56.2. Use the displayed relation together with that section's assumptions and units.

3. **transient heat content** is developed in §56.3. Use the displayed relation together with that section's assumptions and units.

4. **Fourier number** is developed in §56.4. Use the displayed relation together with that section's assumptions and units.

5. **one-term transient solution** is developed in §56.5. Use the displayed relation together with that section's assumptions and units.

6. **fin parameter** is developed in §56.6. Use the displayed relation together with that section's assumptions and units.

7. **fin effectiveness** is developed in §56.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Biot number**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **lumped capacitance**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **transient heat content**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Fourier number**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **one-term transient solution**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **fin parameter**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **fin effectiveness**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **Biot number** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **lumped capacitance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **transient heat content** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **Fourier number** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **one-term transient solution** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **fin parameter** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **fin effectiveness** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **Biot number** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **lumped capacitance** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. A lumped body has h=20, V=0.001 m³, As=0.06 m², k=50 W/mK. Find Bi.

2. Is lumped capacitance valid for Problem 1 under Bi<0.1?

3. ρ=7800, V=0.001, cp=500, h=20, As=0.06. Find time constant.

4. For Problem 3, find temperature ratio θ/θi after one time constant.

5. k=15, ρ=8000, cp=500. Find thermal diffusivity.

6. For L=0.02 m and t=100 s with α from Problem 5, find Fo.

7. What does Bi compare?

8. What does Fo represent?

9. Why do fins help heat transfer?

10. What is fin effectiveness comparing?


---

## Practice Problem Solutions

1. Bi=hV/(kAs)=0.00667.

2. Yes.

3. τ=ρVcp/(hAs)=3250 s.

4. e^-1=0.3679.

5. α=15/(8000*500)=3.75e-6 m²/s.

6. Fo=0.9375.

7. Internal conduction resistance to external convection resistance.

8. Nondimensional elapsed diffusion time.

9. They increase exposed convective area.

10. Heat transfer with fin to heat transfer from the same base area without the fin.


---

## Quick Reference

**Handbook anchor:** Heat Transfer, printed pp. 211–214.

- **Biot number:** Biot Number and Lumped-Capacitance Criterion
- **lumped capacitance:** Lumped Transient Temperature Response
- **transient heat content:** Total Heat Transfer During Lumped Cooling/Heating
- **Fourier number:** Fourier Number and Distributed Transient Conduction
- **one-term transient solution:** One-Term Approximation
- **fin parameter:** Straight Fins and Corrected Length
- **fin effectiveness:** Fin Heat Rate and Effectiveness
---

## What's Next

**02-57 — Convection and Thermal Radiation**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor