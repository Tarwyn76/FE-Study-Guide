---
chapter: "02-57"
title: "Convection and Thermal Radiation"
layer: 2
tier: D
template: technical
ledger_ids: [HT-2D-057-01, HT-2D-057-02, HT-2D-057-03, HT-2D-057-04, HT-2D-057-05, HT-2D-057-06, HT-2D-057-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-57: Convection and Thermal Radiation

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-45 Reynolds Number and Internal Flow · 02-55 Conduction

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives Newton's law of cooling, Nusselt/Reynolds/Prandtl definitions and correlations for internal/external/natural convection, and radiation properties, view-factor relations, and net-exchange equations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **57.1** Explain and apply **Newton's Law of Cooling**.
* **57.2** Explain and apply **Nusselt, Reynolds, and Prandtl Numbers**.
* **57.3** Explain and apply **External Forced Convection**.
* **57.4** Explain and apply **Internal Forced Convection**.
* **57.5** Explain and apply **Natural Convection**.
* **57.6** Explain and apply **Radiation Properties and Blackbody Emission**.
* **57.7** Explain and apply **View Factors and Net Radiation Exchange**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 57.1 Newton's Law of Cooling

Convection is modeled by a heat-transfer coefficient \(h\) relating surface-to-fluid temperature difference to heat rate.

The coefficient is not a pure fluid property; it depends on geometry, flow regime, velocity, properties, and thermal boundary conditions.

\[\dot Q=hA(T_s-T_\infty)\]

![FIG-02-57-001: Wall with fluid boundary layer, surface temperature, bulk temperature, and convective heat flux.](../figures/FIG-02-57-001-newton-s-law-of-cooling.png)

### Worked Example 1

**Problem.** h=50 W/m²K, A=2 m², Ts=100°C, T∞=20°C. Find convection heat rate.

**Solution.** Q=8000 W.

---

## 57.2 Nusselt, Reynolds, and Prandtl Numbers

Convection correlations are commonly written in terms of dimensionless groups. Nusselt number represents nondimensional heat-transfer coefficient, Reynolds represents inertia/viscosity, and Prandtl compares momentum and thermal diffusivities.

Evaluate properties at the temperature basis specified by the correlation.

\[Nu=\frac{hL}{k},\qquad Re=\frac{\rho VL}{\mu},\qquad Pr=\frac{c_p\mu}{k}\]

![FIG-02-57-002: Nu-Re-Pr relationship map connecting flow and thermal transport.](../figures/FIG-02-57-002-nusselt-reynolds-and-prandtl-numbers.png)

### Worked Example 2

**Problem.** Fluid k=0.6 W/mK, h=120 W/m²K, L=0.05 m. Find Nu.

**Solution.** Nu=hL/k=10.

---

## 57.3 External Forced Convection

The Handbook gives correlations for flat plates, cylinders in crossflow, and spheres. Select the correlation matching geometry and Reynolds-number range.

A coefficient from one geometry or regime should not be transferred to another without justification.

\[Nu=CRe^mPr^n\quad\text{(correlation form)}\]

![FIG-02-57-003: Flat plate and cylinder in external flow with thermal/velocity boundary layers.](../figures/FIG-02-57-003-external-forced-convection.png)

### Worked Example 3

**Problem.** ρ=1000, V=2, L=0.05, μ=0.001. Find Re.

**Solution.** Re=100,000.

---

## 57.4 Internal Forced Convection

For fully developed laminar flow in circular tubes, the Handbook gives constant Nusselt numbers for constant heat flux or constant wall temperature. Turbulent internal-flow correlations depend on Reynolds and Prandtl numbers.

The bulk-mean fluid temperature changes along the tube as heat is transferred.

\[Nu_D=4.36\ \text{(laminar, uniform heat flux)},\qquad Nu_D=3.66\ \text{(laminar, const. }T_s)\]

![FIG-02-57-004: Heated tube with developing/fully developed thermal profiles and bulk temperature.](../figures/FIG-02-57-004-internal-forced-convection.png)

### Worked Example 4

**Problem.** cp=4180, μ=0.001, k=0.6. Find Pr.

**Solution.** Pr=6.97.

---

## 57.5 Natural Convection

Natural convection is driven by buoyancy from density differences caused by temperature variation. The Handbook expresses correlations in terms of Rayleigh number.

Orientation and characteristic length matter strongly.

\[Ra=Gr\,Pr\]

![FIG-02-57-005: Heated vertical plate and horizontal cylinder with buoyant natural-convection plumes.](../figures/FIG-02-57-005-natural-convection.png)

### Worked Example 5

**Problem.** Laminar fully developed circular tube, constant wall temperature. What Nu does Handbook give?

**Solution.** 3.66.

---

## 57.6 Radiation Properties and Blackbody Emission

Radiation can occur through vacuum. The Handbook gives emitted radiation proportional to emissivity, area, and absolute temperature to the fourth power.

For opaque surfaces, absorptivity plus reflectivity equals 1; a blackbody has \(arepsilon=lpha=1\).

\[\dot Q_{\rm emit}=\varepsilon\sigma AT^4\]

![FIG-02-57-006: Gray surface radiating to surroundings with emissivity and Stefan-Boltzmann law.](../figures/FIG-02-57-006-radiation-properties-and-blackbody-emission.png)

### Worked Example 6

**Problem.** A gray surface ε=0.8, A=1 m², T=500 K. Find emitted radiation using σ=5.67e-8.

**Solution.** Q=0.8*5.67e-8*500^4=2835 W.

---

## 57.7 View Factors and Net Radiation Exchange

View factor is the fraction of radiation leaving one surface that reaches another. Reciprocity and summation rules reduce enclosure calculations.

For a small gray body in large surroundings, net exchange simplifies to \(arepsilon\sigma A(T_s^4-T_{sur}^4)\).

\[A_iF_{ij}=A_jF_{ji},\qquad \sum_jF_{ij}=1\]

![FIG-02-57-007: Two-surface enclosure with view factors, reciprocity, and net radiation exchange.](../figures/FIG-02-57-007-view-factors-and-net-radiation-exchange.png)

### Worked Example 7

**Problem.** Small gray body ε=0.8, A=1 m², Ts=500 K, surroundings 300 K. Find net radiation.

**Solution.** Q=0.8σ(500^4-300^4)=2467 W.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What does view factor Fij represent?

**Solution.** Fraction of radiation leaving surface i intercepted by j.

### Worked Example 9

**Problem.** State reciprocity relation.

**Solution.** AiFij=AjFji.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Heat Transfer, printed pp. 209 and 214–224**.

**Source boundary:** The Handbook directly gives Newton's law of cooling, Nusselt/Reynolds/Prandtl definitions and correlations for internal/external/natural convection, and radiation properties, view-factor relations, and net-exchange equations.

---

## Where This Goes Wrong

**Using convective heat transfer outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using convection dimensionless groups outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using external convection outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using internal convection outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using natural convection outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using thermal radiation outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using view factor outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| convective heat transfer | Concept developed in §57.1; use the section definition and conditions. |
| convection dimensionless groups | Concept developed in §57.2; use the section definition and conditions. |
| external convection | Concept developed in §57.3; use the section definition and conditions. |
| internal convection | Concept developed in §57.4; use the section definition and conditions. |
| natural convection | Concept developed in §57.5; use the section definition and conditions. |
| thermal radiation | Concept developed in §57.6; use the section definition and conditions. |
| view factor | Concept developed in §57.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **convective heat transfer** and state the governing equation or modeling rule.

2. Define **convection dimensionless groups** and state the governing equation or modeling rule.

3. Define **external convection** and state the governing equation or modeling rule.

4. Define **internal convection** and state the governing equation or modeling rule.

5. Define **natural convection** and state the governing equation or modeling rule.

6. Define **thermal radiation** and state the governing equation or modeling rule.

7. Define **view factor** and state the governing equation or modeling rule.

8. What is the most likely error if **convective heat transfer** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **convection dimensionless groups** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **external convection** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **internal convection** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **natural convection** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **thermal radiation** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **view factor** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **convective heat transfer**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **convection dimensionless groups**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **external convection**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **internal convection**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **natural convection**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **thermal radiation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **view factor**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **convective heat transfer**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **convection dimensionless groups**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **convective heat transfer** is developed in §57.1. Use the displayed relation together with that section's assumptions and units.

2. **convection dimensionless groups** is developed in §57.2. Use the displayed relation together with that section's assumptions and units.

3. **external convection** is developed in §57.3. Use the displayed relation together with that section's assumptions and units.

4. **internal convection** is developed in §57.4. Use the displayed relation together with that section's assumptions and units.

5. **natural convection** is developed in §57.5. Use the displayed relation together with that section's assumptions and units.

6. **thermal radiation** is developed in §57.6. Use the displayed relation together with that section's assumptions and units.

7. **view factor** is developed in §57.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **convective heat transfer**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **convection dimensionless groups**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **external convection**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **internal convection**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **natural convection**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **thermal radiation**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **view factor**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **convective heat transfer** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **convection dimensionless groups** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **external convection** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **internal convection** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **natural convection** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **thermal radiation** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **view factor** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **convective heat transfer** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **convection dimensionless groups** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. h=50 W/m²K, A=2 m², Ts=100°C, T∞=20°C. Find convection heat rate.

2. Fluid k=0.6 W/mK, h=120 W/m²K, L=0.05 m. Find Nu.

3. ρ=1000, V=2, L=0.05, μ=0.001. Find Re.

4. cp=4180, μ=0.001, k=0.6. Find Pr.

5. Laminar fully developed circular tube, constant wall temperature. What Nu does Handbook give?

6. A gray surface ε=0.8, A=1 m², T=500 K. Find emitted radiation using σ=5.67e-8.

7. Small gray body ε=0.8, A=1 m², Ts=500 K, surroundings 300 K. Find net radiation.

8. What does view factor Fij represent?

9. State reciprocity relation.

10. Why must radiation temperatures be absolute?


---

## Practice Problem Solutions

1. Q=8000 W.

2. Nu=hL/k=10.

3. Re=100,000.

4. Pr=6.97.

5. 3.66.

6. Q=0.8*5.67e-8*500^4=2835 W.

7. Q=0.8σ(500^4-300^4)=2467 W.

8. Fraction of radiation leaving surface i intercepted by j.

9. AiFij=AjFji.

10. Stefan-Boltzmann law uses T^4 measured from absolute zero.


---

## Quick Reference

**Handbook anchor:** Heat Transfer, printed pp. 209 and 214–224.

- **convective heat transfer:** Newton's Law of Cooling
- **convection dimensionless groups:** Nusselt, Reynolds, and Prandtl Numbers
- **external convection:** External Forced Convection
- **internal convection:** Internal Forced Convection
- **natural convection:** Natural Convection
- **thermal radiation:** Radiation Properties and Blackbody Emission
- **view factor:** View Factors and Net Radiation Exchange
---

## What's Next

**02-58 — Heat Exchangers — LMTD and Effectiveness-NTU**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor