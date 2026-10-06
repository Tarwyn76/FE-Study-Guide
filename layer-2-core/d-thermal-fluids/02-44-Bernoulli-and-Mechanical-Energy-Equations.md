---
chapter: "02-44"
title: "Bernoulli and Mechanical-Energy Equations"
layer: 2
tier: D
template: technical
ledger_ids: [FLUID-2D-044-01, FLUID-2D-044-02, FLUID-2D-044-03, FLUID-2D-044-04, FLUID-2D-044-05, FLUID-2D-044-06, FLUID-2D-044-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-44: Bernoulli and Mechanical-Energy Equations

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-43 Continuity and Flow Kinematics · 02-41 Hydrostatics

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly supplies the Bernoulli equation, steady incompressible energy equation with head loss, hydraulic grade line, energy line, and Euler's unsteady one-dimensional relation.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **44.1** Explain and apply **Pressure, Velocity, and Elevation Head**.
* **44.2** Explain and apply **Bernoulli Equation and Its Assumptions**.
* **44.3** Explain and apply **Hydraulic Grade Line and Energy Grade Line**.
* **44.4** Explain and apply **Mechanical-Energy Equation with Head Loss**.
* **44.5** Explain and apply **Pressure-Velocity-Elevation Tradeoffs**.
* **44.6** Explain and apply **Euler Equation for Local Acceleration**.
* **44.7** Explain and apply **Energy-Equation Selection Checklist**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 44.1 Pressure, Velocity, and Elevation Head

Mechanical-energy terms are often written per unit weight as head: pressure head \(P/\gamma\), velocity head \(v^2/(2g)\), and elevation head \(z\).

Each term has units of length and can be compared on one energy-line diagram.

\[H=\frac{P}{\gamma}+\frac{v^2}{2g}+z\]

![FIG-02-44-001: Pipe section with pressure, velocity, and elevation head contributions stacked to total head.](../figures/FIG-02-44-001-pressure-velocity-and-elevation-head.png)

### Worked Example 1

**Problem.** Water pressure head is 12 m. Find gauge pressure using γ=9810 N/m³.

**Solution.** P=117.7 kPa.

---

## 44.2 Bernoulli Equation and Its Assumptions

Bernoulli relates two points in steady, incompressible, frictionless flow when no pump or turbine work occurs between them along the modeled streamline.

It is not a universal pressure equation. If losses or machinery matter, use the mechanical-energy equation instead.

\[\frac{P_1}{\gamma}+\frac{v_1^2}{2g}+z_1=\frac{P_2}{\gamma}+\frac{v_2^2}{2g}+z_2\]

![FIG-02-44-002: Two points along a streamline with pressure, velocity, and elevation terms.](../figures/FIG-02-44-002-bernoulli-equation-and-its-assumptions.png)

### Worked Example 2

**Problem.** Velocity is 6 m/s. Find velocity head.

**Solution.** v²/(2g)=1.835 m.

---

## 44.3 Hydraulic Grade Line and Energy Grade Line

The hydraulic grade line (HGL) is \(P/\gamma+z\). The energy grade line (EGL) adds velocity head. Their vertical separation is \(v^2/(2g)\).

In a constant-diameter pipe without pumps/turbines, both lines decrease in the flow direction when losses occur.

\[HGL=\frac{P}{\gamma}+z,\qquad EGL=HGL+\frac{v^2}{2g}\]

![FIG-02-44-003: Pipeline profile with HGL and EGL and velocity-head separation.](../figures/FIG-02-44-003-hydraulic-grade-line-and-energy-grade-line.png)

### Worked Example 3

**Problem.** A large reservoir free surface is 20 m above a nozzle, both at atmospheric pressure; neglect losses. Find exit speed.

**Solution.** v=sqrt(2gΔz)=19.81 m/s.

---

## 44.4 Mechanical-Energy Equation with Head Loss

For steady incompressible flow, losses due to friction and fittings appear as head loss \(h_L\). A complete engineering equation can also include pump head added and turbine head removed.

Keep the sign convention explicit.

\[\frac{P_1}{\gamma}+\frac{v_1^2}{2g}+z_1+h_p-h_t-h_L=\frac{P_2}{\gamma}+\frac{v_2^2}{2g}+z_2\]

![FIG-02-44-004: Reservoir-pipe-pump-turbine system with energy head added, removed, and lost.](../figures/FIG-02-44-004-mechanical-energy-equation-with-head-loss.png)

### Worked Example 4

**Problem.** A pump adds 15 m head and total losses are 5 m between equal reservoirs. What elevation rise is possible if velocities negligible?

**Solution.** Δz=10 m.

---

## 44.5 Pressure-Velocity-Elevation Tradeoffs

Bernoulli is especially useful for nozzles, free jets, reservoirs, and venturi-like changes where pressure, speed, and elevation trade mechanical energy.

Use continuity together with Bernoulli when cross-sectional areas differ.

\[Q=A_1v_1=A_2v_2\]

![FIG-02-44-005: Reservoir-to-nozzle system combining continuity and Bernoulli terms.](../figures/FIG-02-44-005-pressure-velocity-elevation-tradeoffs.png)

### Worked Example 5

**Problem.** For constant-diameter horizontal pipe with 4 m head loss, what is pressure drop in water?

**Solution.** ΔP=ρg hL=39.24 kPa.

---

## 44.6 Euler Equation for Local Acceleration

The Handbook provides a one-dimensional Euler relation for unsteady flow in which local fluid acceleration contributes to pressure variation.

This is a reminder that hydrostatic and Bernoulli relations may fail when significant unsteady acceleration exists.

\[\Delta P+\gamma\Delta z+\rho a_x\Delta x=0\quad\text{(stated 1D model)}\]

![FIG-02-44-006: Accelerating liquid column showing pressure difference, elevation, and local acceleration.](../figures/FIG-02-44-006-euler-equation-for-local-acceleration.png)

### Worked Example 6

**Problem.** What separates EGL from HGL?

**Solution.** Velocity head v²/(2g).

---

## 44.7 Energy-Equation Selection Checklist

Before writing Bernoulli, ask: steady? incompressible? negligible viscous loss? same streamline/model? no shaft work between points?

If any answer is no, use the more general balance or include the missing term.

\[\text{Bernoulli only when its assumptions are satisfied}\]

![FIG-02-44-007: Decision tree selecting hydrostatics, Bernoulli, or mechanical-energy equation.](../figures/FIG-02-44-007-energy-equation-selection-checklist.png)

### Worked Example 7

**Problem.** When is Bernoulli invalid without extra terms?

**Solution.** When losses, shaft work, compressibility, unsteadiness, or violated streamline assumptions matter.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** If area decreases in incompressible steady flow, what happens to velocity?

**Solution.** It increases.

### Worked Example 9

**Problem.** What does a pump do to EGL?

**Solution.** Raises it by pump head.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Fluid Mechanics, printed pp. 185–186**.

**Source boundary:** The Handbook directly supplies the Bernoulli equation, steady incompressible energy equation with head loss, hydraulic grade line, energy line, and Euler's unsteady one-dimensional relation.

---

## Where This Goes Wrong

**Using fluid head outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Bernoulli equation outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using hydraulic grade line outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using mechanical-energy equation outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using energy-continuity coupling outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using unsteady pressure relation outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using energy-equation audit outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| fluid head | Concept developed in §44.1; use the section definition and conditions. |
| Bernoulli equation | Concept developed in §44.2; use the section definition and conditions. |
| hydraulic grade line | Concept developed in §44.3; use the section definition and conditions. |
| mechanical-energy equation | Concept developed in §44.4; use the section definition and conditions. |
| energy-continuity coupling | Concept developed in §44.5; use the section definition and conditions. |
| unsteady pressure relation | Concept developed in §44.6; use the section definition and conditions. |
| energy-equation audit | Concept developed in §44.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **fluid head** and state the governing equation or modeling rule.

2. Define **Bernoulli equation** and state the governing equation or modeling rule.

3. Define **hydraulic grade line** and state the governing equation or modeling rule.

4. Define **mechanical-energy equation** and state the governing equation or modeling rule.

5. Define **energy-continuity coupling** and state the governing equation or modeling rule.

6. Define **unsteady pressure relation** and state the governing equation or modeling rule.

7. Define **energy-equation audit** and state the governing equation or modeling rule.

8. What is the most likely error if **fluid head** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **Bernoulli equation** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **hydraulic grade line** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **mechanical-energy equation** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **energy-continuity coupling** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **unsteady pressure relation** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **energy-equation audit** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **fluid head**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **Bernoulli equation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **hydraulic grade line**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **mechanical-energy equation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **energy-continuity coupling**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **unsteady pressure relation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **energy-equation audit**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **fluid head**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **Bernoulli equation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **fluid head** is developed in §44.1. Use the displayed relation together with that section's assumptions and units.

2. **Bernoulli equation** is developed in §44.2. Use the displayed relation together with that section's assumptions and units.

3. **hydraulic grade line** is developed in §44.3. Use the displayed relation together with that section's assumptions and units.

4. **mechanical-energy equation** is developed in §44.4. Use the displayed relation together with that section's assumptions and units.

5. **energy-continuity coupling** is developed in §44.5. Use the displayed relation together with that section's assumptions and units.

6. **unsteady pressure relation** is developed in §44.6. Use the displayed relation together with that section's assumptions and units.

7. **energy-equation audit** is developed in §44.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **fluid head**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Bernoulli equation**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **hydraulic grade line**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **mechanical-energy equation**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **energy-continuity coupling**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **unsteady pressure relation**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **energy-equation audit**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **fluid head** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **Bernoulli equation** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **hydraulic grade line** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **mechanical-energy equation** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **energy-continuity coupling** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **unsteady pressure relation** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **energy-equation audit** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **fluid head** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **Bernoulli equation** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Water pressure head is 12 m. Find gauge pressure using γ=9810 N/m³.

2. Velocity is 6 m/s. Find velocity head.

3. A large reservoir free surface is 20 m above a nozzle, both at atmospheric pressure; neglect losses. Find exit speed.

4. A pump adds 15 m head and total losses are 5 m between equal reservoirs. What elevation rise is possible if velocities negligible?

5. For constant-diameter horizontal pipe with 4 m head loss, what is pressure drop in water?

6. What separates EGL from HGL?

7. When is Bernoulli invalid without extra terms?

8. If area decreases in incompressible steady flow, what happens to velocity?

9. What does a pump do to EGL?

10. What does friction do to EGL?


---

## Practice Problem Solutions

1. P=117.7 kPa.

2. v²/(2g)=1.835 m.

3. v=sqrt(2gΔz)=19.81 m/s.

4. Δz=10 m.

5. ΔP=ρg hL=39.24 kPa.

6. Velocity head v²/(2g).

7. When losses, shaft work, compressibility, unsteadiness, or violated streamline assumptions matter.

8. It increases.

9. Raises it by pump head.

10. Decreases it in the flow direction.


---

## Quick Reference

**Handbook anchor:** Fluid Mechanics, printed pp. 185–186.

- **fluid head:** Pressure, Velocity, and Elevation Head
- **Bernoulli equation:** Bernoulli Equation and Its Assumptions
- **hydraulic grade line:** Hydraulic Grade Line and Energy Grade Line
- **mechanical-energy equation:** Mechanical-Energy Equation with Head Loss
- **energy-continuity coupling:** Pressure-Velocity-Elevation Tradeoffs
- **unsteady pressure relation:** Euler Equation for Local Acceleration
- **energy-equation audit:** Energy-Equation Selection Checklist
---

## What's Next

**02-45 — Internal Flow — Reynolds Number, Friction, and Head Loss**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor