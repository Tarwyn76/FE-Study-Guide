---
chapter: "02-45"
title: "Internal Flow — Reynolds Number, Friction, and Head Loss"
layer: 2
tier: D
template: technical
ledger_ids: [FLUID-2D-045-01, FLUID-2D-045-02, FLUID-2D-045-03, FLUID-2D-045-04, FLUID-2D-045-05, FLUID-2D-045-06, FLUID-2D-045-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-45: Internal Flow — Reynolds Number, Friction, and Head Loss

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-44 Mechanical Energy · 02-41 Viscosity

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly supplies Reynolds-number characterization, laminar profiles, Darcy-Weisbach and Fanning friction relations, minor losses, Hagen-Poiseuille flow, hydraulic diameter, series/parallel piping, and the Moody chart.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **45.1** Explain and apply **Reynolds Number and Flow Regimes**.
* **45.2** Explain and apply **Laminar Velocity Profile**.
* **45.3** Explain and apply **Darcy-Weisbach Head Loss**.
* **45.4** Explain and apply **Moody Chart and Friction Factor**.
* **45.5** Explain and apply **Minor Losses**.
* **45.6** Explain and apply **Noncircular Conduits and Hydraulic Diameter**.
* **45.7** Explain and apply **Laminar Pressure Drop and Pipe Networks**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 45.1 Reynolds Number and Flow Regimes

For Newtonian pipe flow, Reynolds number compares inertial and viscous effects. The Handbook characterizes pipe flow as generally laminar below about 2,100, transitional between about 2,100 and 10,000, and fully turbulent above about 10,000.

These ranges are guidance, not universal sharp boundaries for every geometry and disturbance condition.

\[Re=\frac{\rho vD}{\mu}=\frac{vD}{\nu}\]

![FIG-02-45-001: Reynolds-number axis showing laminar, transition, and turbulent pipe-flow regions.](../figures/FIG-02-45-001-reynolds-number-and-flow-regimes.png)

### Worked Example 1

**Problem.** Water flows at 2 m/s in D=0.05 m with ν=1.0e-6 m²/s. Find Re.

**Solution.** Re=100,000.

---

## 45.2 Laminar Velocity Profile

Fully developed laminar flow in a circular tube has a parabolic velocity profile. The Handbook gives \(v_{max}=2ar v\) for circular-tube laminar flow.

The wall velocity is zero under the no-slip model.

\[v(r)=v_{\max}\left[1-\left(\frac rR\right)^2\right]\]

![FIG-02-45-002: Parabolic laminar velocity profile in a circular pipe with vmax=2vavg.](../figures/FIG-02-45-002-laminar-velocity-profile.png)

### Worked Example 2

**Problem.** For Re=1000 laminar pipe flow, find Darcy f.

**Solution.** f=64/Re=0.064.

---

## 45.3 Darcy-Weisbach Head Loss

Major head loss in a straight pipe is represented by Darcy-Weisbach. The friction factor is dimensionless and depends on Reynolds number and relative roughness.

Use the Darcy factor with the Darcy-Weisbach equation; do not mix it with Fanning friction factor without converting.

\[h_f=f\frac LD\frac{v^2}{2g}\]

![FIG-02-45-003: Straight pipe with L, D, average velocity, and head loss.](../figures/FIG-02-45-003-darcy-weisbach-head-loss.png)

### Worked Example 3

**Problem.** For f=0.02, L=50 m, D=0.10 m, v=2 m/s, find major head loss.

**Solution.** hf=0.02(50/0.1)(4/(2*9.81))=2.04 m.

---

## 45.4 Moody Chart and Friction Factor

For laminar circular-pipe flow, \(f=64/Re\). For turbulent flow, use the Moody chart or a stated correlation using \(Re\) and \(arepsilon/D\).

The Handbook notes the Fanning factor is one-fourth the Darcy factor.

\[f_{\rm Darcy}=4f_{\rm Fanning}\]

![FIG-02-45-004: Simplified Moody chart showing laminar line and turbulent roughness families.](../figures/FIG-02-45-004-moody-chart-and-friction-factor.png)

### Worked Example 4

**Problem.** A fitting has K=1.5 at v=3 m/s. Find minor head loss.

**Solution.** hm=1.5(9/(19.62))=0.688 m.

---

## 45.5 Minor Losses

Fittings, valves, entrances, exits, contractions, and expansions add localized losses often written using a loss coefficient \(K\).

The problem may provide \(K\) directly. Sum individual minor losses using the velocity appropriate to each element.

\[h_m=K\frac{v^2}{2g},\qquad h_{m,\rm total}=\sum_iK_i\frac{v_i^2}{2g}\]

![FIG-02-45-005: Pipe system with valves/elbows and associated K-loss terms.](../figures/FIG-02-45-005-minor-losses.png)

### Worked Example 5

**Problem.** Rectangular duct 0.2 m by 0.1 m is full. Find hydraulic diameter.

**Solution.** Dh=4A/P=4(0.02)/0.6=0.133 m.

---

## 45.6 Noncircular Conduits and Hydraulic Diameter

For a noncircular closed conduit, use hydraulic diameter based on flow area and wetted perimeter when the Handbook relation is applicable.

Keep the characteristic length definition consistent in both Reynolds number and head-loss correlation.

\[D_h=\frac{4A}{P_w}\]

![FIG-02-45-006: Rectangular duct with area A, wetted perimeter Pw, and equivalent hydraulic diameter.](../figures/FIG-02-45-006-noncircular-conduits-and-hydraulic-diameter.png)

### Worked Example 6

**Problem.** What is vmax/vavg for fully developed laminar circular-tube flow?

**Solution.** 2.

---

## 45.7 Laminar Pressure Drop and Pipe Networks

For fully developed laminar circular-tube flow, Hagen-Poiseuille gives a direct relation among flow rate, viscosity, geometry, and pressure drop.

In series pipes, the same flow passes each segment and head losses add. In parallel branches, head loss between common junctions is equal while branch flows sum.

\[Q=\frac{\pi D^4\Delta P}{128\mu L}\]

![FIG-02-45-007: Series and parallel pipe arrangements with flow and head-loss constraints.](../figures/FIG-02-45-007-laminar-pressure-drop-and-pipe-networks.png)

### Worked Example 7

**Problem.** How are Darcy and Fanning factors related?

**Solution.** fDarcy=4 fFanning.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What is equal across parallel pipe branches between common junctions?

**Solution.** Head loss.

### Worked Example 9

**Problem.** What is equal through pipes in series without branches?

**Solution.** Flow rate.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Fluid Mechanics, printed pp. 186–191 and 206**.

**Source boundary:** The Handbook directly supplies Reynolds-number characterization, laminar profiles, Darcy-Weisbach and Fanning friction relations, minor losses, Hagen-Poiseuille flow, hydraulic diameter, series/parallel piping, and the Moody chart.

---

## Where This Goes Wrong

**Using Reynolds number outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using laminar pipe flow outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Darcy-Weisbach equation outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using friction factor outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using minor loss outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using hydraulic diameter outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using pipe-network flow outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| Reynolds number | Concept developed in §45.1; use the section definition and conditions. |
| laminar pipe flow | Concept developed in §45.2; use the section definition and conditions. |
| Darcy-Weisbach equation | Concept developed in §45.3; use the section definition and conditions. |
| friction factor | Concept developed in §45.4; use the section definition and conditions. |
| minor loss | Concept developed in §45.5; use the section definition and conditions. |
| hydraulic diameter | Concept developed in §45.6; use the section definition and conditions. |
| pipe-network flow | Concept developed in §45.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **Reynolds number** and state the governing equation or modeling rule.

2. Define **laminar pipe flow** and state the governing equation or modeling rule.

3. Define **Darcy-Weisbach equation** and state the governing equation or modeling rule.

4. Define **friction factor** and state the governing equation or modeling rule.

5. Define **minor loss** and state the governing equation or modeling rule.

6. Define **hydraulic diameter** and state the governing equation or modeling rule.

7. Define **pipe-network flow** and state the governing equation or modeling rule.

8. What is the most likely error if **Reynolds number** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **laminar pipe flow** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **Darcy-Weisbach equation** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **friction factor** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **minor loss** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **hydraulic diameter** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **pipe-network flow** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **Reynolds number**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **laminar pipe flow**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **Darcy-Weisbach equation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **friction factor**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **minor loss**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **hydraulic diameter**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **pipe-network flow**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **Reynolds number**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **laminar pipe flow**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **Reynolds number** is developed in §45.1. Use the displayed relation together with that section's assumptions and units.

2. **laminar pipe flow** is developed in §45.2. Use the displayed relation together with that section's assumptions and units.

3. **Darcy-Weisbach equation** is developed in §45.3. Use the displayed relation together with that section's assumptions and units.

4. **friction factor** is developed in §45.4. Use the displayed relation together with that section's assumptions and units.

5. **minor loss** is developed in §45.5. Use the displayed relation together with that section's assumptions and units.

6. **hydraulic diameter** is developed in §45.6. Use the displayed relation together with that section's assumptions and units.

7. **pipe-network flow** is developed in §45.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Reynolds number**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **laminar pipe flow**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Darcy-Weisbach equation**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **friction factor**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **minor loss**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **hydraulic diameter**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **pipe-network flow**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **Reynolds number** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **laminar pipe flow** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **Darcy-Weisbach equation** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **friction factor** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **minor loss** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **hydraulic diameter** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **pipe-network flow** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **Reynolds number** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **laminar pipe flow** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Water flows at 2 m/s in D=0.05 m with ν=1.0e-6 m²/s. Find Re.

2. For Re=1000 laminar pipe flow, find Darcy f.

3. For f=0.02, L=50 m, D=0.10 m, v=2 m/s, find major head loss.

4. A fitting has K=1.5 at v=3 m/s. Find minor head loss.

5. Rectangular duct 0.2 m by 0.1 m is full. Find hydraulic diameter.

6. What is vmax/vavg for fully developed laminar circular-tube flow?

7. How are Darcy and Fanning factors related?

8. What is equal across parallel pipe branches between common junctions?

9. What is equal through pipes in series without branches?

10. Why must relative roughness ε/D be known for turbulent Moody-chart use?


---

## Practice Problem Solutions

1. Re=100,000.

2. f=64/Re=0.064.

3. hf=0.02(50/0.1)(4/(2*9.81))=2.04 m.

4. hm=1.5(9/(19.62))=0.688 m.

5. Dh=4A/P=4(0.02)/0.6=0.133 m.

6. 2.

7. fDarcy=4 fFanning.

8. Head loss.

9. Flow rate.

10. Turbulent friction factor depends on both Reynolds number and relative roughness.


---

## Quick Reference

**Handbook anchor:** Fluid Mechanics, printed pp. 186–191 and 206.

- **Reynolds number:** Reynolds Number and Flow Regimes
- **laminar pipe flow:** Laminar Velocity Profile
- **Darcy-Weisbach equation:** Darcy-Weisbach Head Loss
- **friction factor:** Moody Chart and Friction Factor
- **minor loss:** Minor Losses
- **hydraulic diameter:** Noncircular Conduits and Hydraulic Diameter
- **pipe-network flow:** Laminar Pressure Drop and Pipe Networks
---

## What's Next

**02-46 — Momentum, Flow Measurement, Pumps, and Turbines**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor