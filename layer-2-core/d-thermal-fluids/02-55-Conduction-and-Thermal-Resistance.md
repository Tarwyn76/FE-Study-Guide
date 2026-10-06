---
chapter: "02-55"
title: "Conduction and Thermal Resistance"
layer: 2
tier: D
template: technical
ledger_ids: [HT-2D-055-01, HT-2D-055-02, HT-2D-055-03, HT-2D-055-04, HT-2D-055-05, HT-2D-055-06, HT-2D-055-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-55: Conduction and Thermal Resistance

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-17 Thermal Properties · 02-52 Energy and Entropy Context

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives Fourier's law, plane/cylindrical conduction, critical insulation radius, thermal resistances, convection resistance, and composite-wall networks.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **55.1** Explain and apply **Fourier's Law of Conduction**.
* **55.2** Explain and apply **Plane-Wall Conduction**.
* **55.3** Explain and apply **Cylindrical-Wall Conduction**.
* **55.4** Explain and apply **Thermal Resistance Networks**.
* **55.5** Explain and apply **Composite Walls and Interface Temperatures**.
* **55.6** Explain and apply **Critical Radius of Insulation**.
* **55.7** Explain and apply **Conduction Modeling Checks**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 55.1 Fourier's Law of Conduction

Conduction transfers energy through a temperature gradient. Fourier's law includes a negative sign because heat flows in the direction of decreasing temperature.

Thermal conductivity \(k\) is a material property and may depend on temperature.

\[\dot Q=-kA\frac{dT}{dx}\]

![FIG-02-55-001: Plane wall with temperature gradient and conductive heat-flow direction.](../figures/FIG-02-55-001-fourier-s-law-of-conduction.png)

### Worked Example 1

**Problem.** Plane wall k=2 W/m·K, A=4 m², L=0.1 m, ΔT=20 K. Find heat rate.

**Solution.** Q=1600 W.

---

## 55.2 Plane-Wall Conduction

For steady one-dimensional conduction through a constant-k plane wall with no internal generation, the temperature profile is linear.

The heat rate depends on area, conductivity, thickness, and temperature difference.

\[\dot Q=\frac{kA(T_1-T_2)}{L}\]

![FIG-02-55-002: Plane wall of thickness L with surface temperatures and heat flow.](../figures/FIG-02-55-002-plane-wall-conduction.png)

### Worked Example 2

**Problem.** Plane-wall resistance L=0.05 m, k=0.5, A=2. Find R.

**Solution.** R=0.05 K/W.

---

## 55.3 Cylindrical-Wall Conduction

Radial heat flow through a cylindrical wall has changing area with radius, leading to a logarithmic resistance.

Do not use the plane-wall \(L/kA\) expression across a thick cylinder unless a thin-wall approximation is explicitly justified.

\[\dot Q=\frac{2\pi kL(T_1-T_2)}{\ln(r_2/r_1)}\]

![FIG-02-55-003: Hollow cylinder with r1, r2, length L, temperatures, and radial heat flow.](../figures/FIG-02-55-003-cylindrical-wall-conduction.png)

### Worked Example 3

**Problem.** Convection h=25 W/m²K, A=4 m². Find Rconv.

**Solution.** 0.010 K/W.

---

## 55.4 Thermal Resistance Networks

Heat transfer can be written like an electrical-resistance analogy: heat rate equals temperature difference divided by total thermal resistance.

Series resistances add directly. Parallel paths require conductance addition.

\[\dot Q=\frac{\Delta T}{R_{\rm total}},\qquad R_{\rm cond,plane}=\frac{L}{kA},\qquad R_{\rm conv}=\frac1{hA}\]

![FIG-02-55-004: Thermal resistance circuit with convection and conduction resistances in series.](../figures/FIG-02-55-004-thermal-resistance-networks.png)

### Worked Example 4

**Problem.** Composite series resistances 0.02, 0.04, 0.01 K/W with ΔT=70 K. Find heat rate.

**Solution.** Q=70/0.07=1000 W.

---

## 55.5 Composite Walls and Interface Temperatures

A composite wall combines multiple conduction layers and convection films. Once heat rate is known, intermediate temperatures follow from temperature drops \(\Delta T_i=\dot Q R_i\).

Interface temperatures are useful for checking condensation, material limits, and contact conditions.

\[R_{\rm total}=\frac1{h_1A}+\sum_i\frac{L_i}{k_iA}+\frac1{h_2A}\]

![FIG-02-55-005: Multilayer wall with fluids, convection films, layer resistances, and interface temperatures.](../figures/FIG-02-55-005-composite-walls-and-interface-temperatures.png)

### Worked Example 5

**Problem.** Cylinder r1=0.02, r2=0.04 m, k=0.2, L=1 m. Find Rcond.

**Solution.** R=ln2/(2π0.2)=0.552 K/W.

---

## 55.6 Critical Radius of Insulation

For cylindrical insulation, adding insulation increases conduction resistance but also increases outer convection area. The Handbook gives a critical insulation radius where these effects balance.

Beyond the critical radius, additional insulation decreases heat loss; below it, heat loss can initially increase.

\[r_{\rm cr}=\frac{k_{\rm insulation}}{h_\infty}\]

![FIG-02-55-006: Heat loss versus insulation radius with maximum at critical radius.](../figures/FIG-02-55-006-critical-radius-of-insulation.png)

### Worked Example 6

**Problem.** What does negative sign in Fourier's law indicate?

**Solution.** Heat flows down the temperature gradient.

---

## 55.7 Conduction Modeling Checks

Confirm geometry, steady/transient condition, heat generation, property assumptions, area definition, and boundary temperatures. Thermal resistance methods require a valid one-dimensional path or separately defined parallel paths.

Use kelvin or Celsius temperature differences interchangeably, but absolute temperature is required for radiation.

\[\text{geometry + boundaries + properties}\Rightarrow\text{valid resistance model}\]

![FIG-02-55-007: Conduction checklist for geometry, dimensionality, k variation, generation, and boundary conditions.](../figures/FIG-02-55-007-conduction-modeling-checks.png)

### Worked Example 7

**Problem.** Do series thermal resistances add?

**Solution.** Yes.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What is critical insulation radius for k=0.05 W/mK and h=10 W/m²K?

**Solution.** rcr=0.005 m.

### Worked Example 9

**Problem.** Can Celsius differences be used in conduction equations?

**Solution.** Yes; a temperature difference in °C equals the same difference in K.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Heat Transfer, printed pp. 209–211**.

**Source boundary:** The Handbook directly gives Fourier's law, plane/cylindrical conduction, critical insulation radius, thermal resistances, convection resistance, and composite-wall networks.

---

## Where This Goes Wrong

**Using Fourier conduction outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using plane-wall conduction outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using cylindrical conduction outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using thermal resistance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using composite wall outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using critical insulation radius outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using conduction audit outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| Fourier conduction | Concept developed in §55.1; use the section definition and conditions. |
| plane-wall conduction | Concept developed in §55.2; use the section definition and conditions. |
| cylindrical conduction | Concept developed in §55.3; use the section definition and conditions. |
| thermal resistance | Concept developed in §55.4; use the section definition and conditions. |
| composite wall | Concept developed in §55.5; use the section definition and conditions. |
| critical insulation radius | Concept developed in §55.6; use the section definition and conditions. |
| conduction audit | Concept developed in §55.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **Fourier conduction** and state the governing equation or modeling rule.

2. Define **plane-wall conduction** and state the governing equation or modeling rule.

3. Define **cylindrical conduction** and state the governing equation or modeling rule.

4. Define **thermal resistance** and state the governing equation or modeling rule.

5. Define **composite wall** and state the governing equation or modeling rule.

6. Define **critical insulation radius** and state the governing equation or modeling rule.

7. Define **conduction audit** and state the governing equation or modeling rule.

8. What is the most likely error if **Fourier conduction** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **plane-wall conduction** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **cylindrical conduction** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **thermal resistance** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **composite wall** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **critical insulation radius** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **conduction audit** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **Fourier conduction**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **plane-wall conduction**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **cylindrical conduction**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **thermal resistance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **composite wall**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **critical insulation radius**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **conduction audit**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **Fourier conduction**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **plane-wall conduction**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **Fourier conduction** is developed in §55.1. Use the displayed relation together with that section's assumptions and units.

2. **plane-wall conduction** is developed in §55.2. Use the displayed relation together with that section's assumptions and units.

3. **cylindrical conduction** is developed in §55.3. Use the displayed relation together with that section's assumptions and units.

4. **thermal resistance** is developed in §55.4. Use the displayed relation together with that section's assumptions and units.

5. **composite wall** is developed in §55.5. Use the displayed relation together with that section's assumptions and units.

6. **critical insulation radius** is developed in §55.6. Use the displayed relation together with that section's assumptions and units.

7. **conduction audit** is developed in §55.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Fourier conduction**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **plane-wall conduction**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **cylindrical conduction**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **thermal resistance**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **composite wall**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **critical insulation radius**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **conduction audit**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **Fourier conduction** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **plane-wall conduction** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **cylindrical conduction** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **thermal resistance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **composite wall** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **critical insulation radius** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **conduction audit** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **Fourier conduction** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **plane-wall conduction** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Plane wall k=2 W/m·K, A=4 m², L=0.1 m, ΔT=20 K. Find heat rate.

2. Plane-wall resistance L=0.05 m, k=0.5, A=2. Find R.

3. Convection h=25 W/m²K, A=4 m². Find Rconv.

4. Composite series resistances 0.02, 0.04, 0.01 K/W with ΔT=70 K. Find heat rate.

5. Cylinder r1=0.02, r2=0.04 m, k=0.2, L=1 m. Find Rcond.

6. What does negative sign in Fourier's law indicate?

7. Do series thermal resistances add?

8. What is critical insulation radius for k=0.05 W/mK and h=10 W/m²K?

9. Can Celsius differences be used in conduction equations?

10. When is plane-wall resistance invalid for a thick cylinder?


---

## Practice Problem Solutions

1. Q=1600 W.

2. R=0.05 K/W.

3. 0.010 K/W.

4. Q=70/0.07=1000 W.

5. R=ln2/(2π0.2)=0.552 K/W.

6. Heat flows down the temperature gradient.

7. Yes.

8. rcr=0.005 m.

9. Yes; a temperature difference in °C equals the same difference in K.

10. When radial area variation is significant.


---

## Quick Reference

**Handbook anchor:** Heat Transfer, printed pp. 209–211.

- **Fourier conduction:** Fourier's Law of Conduction
- **plane-wall conduction:** Plane-Wall Conduction
- **cylindrical conduction:** Cylindrical-Wall Conduction
- **thermal resistance:** Thermal Resistance Networks
- **composite wall:** Composite Walls and Interface Temperatures
- **critical insulation radius:** Critical Radius of Insulation
- **conduction audit:** Conduction Modeling Checks
---

## What's Next

**02-56 — Extended Surfaces and Transient Conduction**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor