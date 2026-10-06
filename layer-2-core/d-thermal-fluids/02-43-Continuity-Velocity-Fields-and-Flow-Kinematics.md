---
chapter: "02-43"
title: "Continuity, Velocity Fields, and Flow Kinematics"
layer: 2
tier: D
template: technical
ledger_ids: [FLUID-2D-043-01, FLUID-2D-043-02, FLUID-2D-043-03, FLUID-2D-043-04, FLUID-2D-043-05, FLUID-2D-043-06, FLUID-2D-043-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-43: Continuity, Velocity Fields, and Flow Kinematics

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-41 Fluid Properties · 01-23 Partial Derivatives and Vector Calculus

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives one-dimensional continuity, volumetric and mass-flow relations, and Euler's equation for local acceleration. Velocity-field, streamline, and control-volume interpretation is guide-developed fluid-kinematics context.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **43.1** Explain and apply **Volumetric Flow Rate and Average Velocity**.
* **43.2** Explain and apply **Mass Flow Rate**.
* **43.3** Explain and apply **Steady One-Dimensional Continuity**.
* **43.4** Explain and apply **Velocity Fields and Acceleration**.
* **43.5** Explain and apply **Streamlines, Pathlines, and Steady Flow**.
* **43.6** Explain and apply **Control-Volume Mass Balance**.
* **43.7** Explain and apply **Flow-Kinematics Checks**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 43.1 Volumetric Flow Rate and Average Velocity

Volumetric flow rate is volume crossing a section per unit time. For a one-dimensional section using average velocity normal to the area, \(Q=Av\).

If velocity varies across the section, the exact relation is an area integral and \(v\) is the area-average normal velocity.

\[Q=\int_A\mathbf v\cdot\mathbf n\,dA\approx Av\]

![FIG-02-43-001: Pipe cross-section with nonuniform velocity profile and equivalent average velocity.](../figures/FIG-02-43-001-volumetric-flow-rate-and-average-velocity.png)

### Worked Example 1

**Problem.** A pipe has A=0.020 m² and average velocity 3 m/s. Find Q.

**Solution.** Q=0.060 m³/s.

---

## 43.2 Mass Flow Rate

Mass flow rate combines volumetric flow and density. For a uniform one-dimensional stream, \(\dot m=ho Av\).

For gases or varying-density flow, constant volumetric flow does not imply constant mass flow.

\[\dot m=\rho Q=\rho Av\]

![FIG-02-43-002: Stream tube showing density, area, average velocity, volumetric flow, and mass flow.](../figures/FIG-02-43-002-mass-flow-rate.png)

### Worked Example 2

**Problem.** Water at ρ=1000 kg/m³ flows at Q=0.060 m³/s. Find mass flow.

**Solution.** ṁ=60 kg/s.

---

## 43.3 Steady One-Dimensional Continuity

For steady flow through a control volume with one inlet and one outlet, mass flow in equals mass flow out.

If density is constant, the relation reduces to equal volumetric flow and \(A_1v_1=A_2v_2\).

\[\rho_1A_1v_1=\rho_2A_2v_2,\qquad \rho=\text{const}\Rightarrow A_1v_1=A_2v_2\]

![FIG-02-43-003: Converging nozzle with inlet/outlet area, density, velocity, and equal mass flow.](../figures/FIG-02-43-003-steady-one-dimensional-continuity.png)

### Worked Example 3

**Problem.** Incompressible flow enters a 0.040 m² section at 2 m/s and exits through 0.010 m². Find exit speed.

**Solution.** v2=A1v1/A2=8 m/s.

---

## 43.4 Velocity Fields and Acceleration

A velocity field assigns a velocity vector to every point and time. Fluid-particle acceleration contains local time variation and spatial change as particles move through a nonuniform field.

This full material-derivative form is guide-developed background; the Handbook separately gives an Euler relation for local acceleration in a one-dimensional setting.

\[\mathbf a=\frac{\partial\mathbf v}{\partial t}+(\mathbf v\cdot\nabla)\mathbf v\]

![FIG-02-43-004: Velocity field with one particle moving through changing spatial velocity and local time variation.](../figures/FIG-02-43-004-velocity-fields-and-acceleration.png)

### Worked Example 4

**Problem.** Air enters at ρ1=1.2, A1=0.10, v1=5 and exits at ρ2=0.9, A2=0.08. Find v2 for steady one-stream flow.

**Solution.** v2=ρ1A1v1/(ρ2A2)=8.33 m/s.

---

## 43.5 Streamlines, Pathlines, and Steady Flow

A streamline is tangent to the instantaneous velocity field. A pathline is the actual trajectory of one fluid particle.

In steady flow, streamlines and pathlines coincide. In unsteady flow they need not.

\[\frac{dx}{u}=\frac{dy}{v}=\frac{dz}{w}\quad\text{along a streamline}\]

![FIG-02-43-005: Steady-flow streamline/pathline coincidence versus unsteady case where they differ.](../figures/FIG-02-43-005-streamlines-pathlines-and-steady-flow.png)

### Worked Example 5

**Problem.** At steady state, a mixer has inflows 2 and 3 kg/s. Find total outflow.

**Solution.** 5 kg/s.

---

## 43.6 Control-Volume Mass Balance

The general control-volume statement is accumulation equals inflow minus outflow. For steady flow, the accumulation term vanishes.

This framing extends continuity to multiple inlets, multiple outlets, tanks, and mixing junctions.

\[\frac{dm_{CV}}{dt}=\sum\dot m_{\rm in}-\sum\dot m_{\rm out}\]

![FIG-02-43-006: Control volume with multiple inlet/outlet streams and mass accumulation term.](../figures/FIG-02-43-006-control-volume-mass-balance.png)

### Worked Example 6

**Problem.** What is area under a velocity profile integrated over area?

**Solution.** Volumetric flow rate.

---

## 43.7 Flow-Kinematics Checks

Check the units of \(Q\), \(\dot m\), area, and velocity. For incompressible steady flow, a smaller area requires a larger average velocity if no branches exist.

At a junction, total mass inflow must equal total mass outflow at steady state even if stream densities differ.

\[\sum\dot m_{\rm in}=\sum\dot m_{\rm out}\quad(\text{steady})\]

![FIG-02-43-007: Continuity checklist for units, density variation, branches, and steady/unsteady accumulation.](../figures/FIG-02-43-007-flow-kinematics-checks.png)

### Worked Example 7

**Problem.** Distinguish streamline from pathline.

**Solution.** Streamline is instantaneous tangent field; pathline is a particle trajectory.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** When do streamlines and pathlines coincide?

**Solution.** Steady flow.

### Worked Example 9

**Problem.** What does the accumulation term equal at steady state?

**Solution.** Zero.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Fluid Mechanics, printed pp. 185–186**.

**Source boundary:** The Handbook directly gives one-dimensional continuity, volumetric and mass-flow relations, and Euler's equation for local acceleration. Velocity-field, streamline, and control-volume interpretation is guide-developed fluid-kinematics context.

---

## Where This Goes Wrong

**Using volumetric flow rate outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using mass flow rate outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using continuity equation outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using fluid acceleration outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using streamline outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using control-volume mass balance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using flow kinematics audit outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| volumetric flow rate | Concept developed in §43.1; use the section definition and conditions. |
| mass flow rate | Concept developed in §43.2; use the section definition and conditions. |
| continuity equation | Concept developed in §43.3; use the section definition and conditions. |
| fluid acceleration | Concept developed in §43.4; use the section definition and conditions. |
| streamline | Concept developed in §43.5; use the section definition and conditions. |
| control-volume mass balance | Concept developed in §43.6; use the section definition and conditions. |
| flow kinematics audit | Concept developed in §43.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **volumetric flow rate** and state the governing equation or modeling rule.

2. Define **mass flow rate** and state the governing equation or modeling rule.

3. Define **continuity equation** and state the governing equation or modeling rule.

4. Define **fluid acceleration** and state the governing equation or modeling rule.

5. Define **streamline** and state the governing equation or modeling rule.

6. Define **control-volume mass balance** and state the governing equation or modeling rule.

7. Define **flow kinematics audit** and state the governing equation or modeling rule.

8. What is the most likely error if **volumetric flow rate** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **mass flow rate** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **continuity equation** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **fluid acceleration** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **streamline** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **control-volume mass balance** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **flow kinematics audit** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **volumetric flow rate**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **mass flow rate**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **continuity equation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **fluid acceleration**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **streamline**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **control-volume mass balance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **flow kinematics audit**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **volumetric flow rate**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **mass flow rate**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **volumetric flow rate** is developed in §43.1. Use the displayed relation together with that section's assumptions and units.

2. **mass flow rate** is developed in §43.2. Use the displayed relation together with that section's assumptions and units.

3. **continuity equation** is developed in §43.3. Use the displayed relation together with that section's assumptions and units.

4. **fluid acceleration** is developed in §43.4. Use the displayed relation together with that section's assumptions and units.

5. **streamline** is developed in §43.5. Use the displayed relation together with that section's assumptions and units.

6. **control-volume mass balance** is developed in §43.6. Use the displayed relation together with that section's assumptions and units.

7. **flow kinematics audit** is developed in §43.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **volumetric flow rate**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **mass flow rate**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **continuity equation**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **fluid acceleration**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **streamline**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **control-volume mass balance**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **flow kinematics audit**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **volumetric flow rate** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **mass flow rate** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **continuity equation** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **fluid acceleration** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **streamline** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **control-volume mass balance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **flow kinematics audit** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **volumetric flow rate** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **mass flow rate** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. A pipe has A=0.020 m² and average velocity 3 m/s. Find Q.

2. Water at ρ=1000 kg/m³ flows at Q=0.060 m³/s. Find mass flow.

3. Incompressible flow enters a 0.040 m² section at 2 m/s and exits through 0.010 m². Find exit speed.

4. Air enters at ρ1=1.2, A1=0.10, v1=5 and exits at ρ2=0.9, A2=0.08. Find v2 for steady one-stream flow.

5. At steady state, a mixer has inflows 2 and 3 kg/s. Find total outflow.

6. What is area under a velocity profile integrated over area?

7. Distinguish streamline from pathline.

8. When do streamlines and pathlines coincide?

9. What does the accumulation term equal at steady state?

10. Why can Q vary while ṁ remains constant in compressible steady flow?


---

## Practice Problem Solutions

1. Q=0.060 m³/s.

2. ṁ=60 kg/s.

3. v2=A1v1/A2=8 m/s.

4. v2=ρ1A1v1/(ρ2A2)=8.33 m/s.

5. 5 kg/s.

6. Volumetric flow rate.

7. Streamline is instantaneous tangent field; pathline is a particle trajectory.

8. Steady flow.

9. Zero.

10. Density changes.


---

## Quick Reference

**Handbook anchor:** Fluid Mechanics, printed pp. 185–186.

- **volumetric flow rate:** Volumetric Flow Rate and Average Velocity
- **mass flow rate:** Mass Flow Rate
- **continuity equation:** Steady One-Dimensional Continuity
- **fluid acceleration:** Velocity Fields and Acceleration
- **streamline:** Streamlines, Pathlines, and Steady Flow
- **control-volume mass balance:** Control-Volume Mass Balance
- **flow kinematics audit:** Flow-Kinematics Checks
---

## What's Next

**02-44 — Bernoulli and Mechanical-Energy Equations**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor