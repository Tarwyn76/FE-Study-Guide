---
chapter: "02-42"
title: "Buoyancy, Manometry, and Forces on Submerged Surfaces"
layer: 2
tier: D
template: technical
ledger_ids: [FLUID-2D-042-01, FLUID-2D-042-02, FLUID-2D-042-03, FLUID-2D-042-04, FLUID-2D-042-05, FLUID-2D-042-06, FLUID-2D-042-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-42: Buoyancy, Manometry, and Forces on Submerged Surfaces

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-41 Fluid Properties, Pressure, and Hydrostatics · 02-29 Area Moments of Inertia

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly supplies simple-manometer relations, barometer principles, hydrostatic force and center-of-pressure formulas, and Archimedes' principle.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **42.1** Explain and apply **Simple Manometers**.
* **42.2** Explain and apply **Barometers and Atmospheric Pressure**.
* **42.3** Explain and apply **Buoyant Force and Archimedes' Principle**.
* **42.4** Explain and apply **Floating Bodies**.
* **42.5** Explain and apply **Resultant Force on a Plane Submerged Surface**.
* **42.6** Explain and apply **Center of Pressure**.
* **42.7** Explain and apply **Combined Hydrostatic Force and Equilibrium**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 42.1 Simple Manometers

A manometer converts a pressure difference into fluid-column height differences. Traverse the connected fluid from one point to the other, adding pressure when moving downward and subtracting when moving upward.

For multiple fluids, apply each fluid's own specific weight over its vertical height.

\[\Delta P=\sum (\pm \rho_i g\,\Delta h_i)\]

![FIG-02-42-001: U-tube manometer with two fluids, labeled elevations, and pressure-traversal arrows.](../figures/FIG-02-42-001-simple-manometers.png)

### Worked Example 1

**Problem.** A water manometer shows 0.40 m difference. Find pressure difference.

**Solution.** ΔP=ρgh=3.924 kPa.

---

## 42.2 Barometers and Atmospheric Pressure

A barometer balances atmospheric pressure against a liquid column plus any vapor pressure above the column. The measured column height therefore depends on fluid density and vapor pressure.

Use absolute pressure for atmospheric/barometric relations.

\[P_{\rm atm}=P_v+\rho gh\]

![FIG-02-42-002: Simple barometer showing atmospheric pressure, vapor space, and liquid-column height.](../figures/FIG-02-42-002-barometers-and-atmospheric-pressure.png)

### Worked Example 2

**Problem.** Mercury density is 13,600 kg/m³. A barometer column is 0.760 m and vapor pressure is neglected. Find atmospheric pressure.

**Solution.** P=ρgh≈101.4 kPa.

---

## 42.3 Buoyant Force and Archimedes' Principle

The buoyant force on a submerged or floating body equals the weight of displaced fluid. The line of action passes through the centroid of the displaced fluid volume, called the center of buoyancy.

For a fully submerged object in a uniform fluid, buoyant-force magnitude depends on displaced volume, not depth.

\[F_B=\rho_f gV_{\rm displaced}=\gamma_fV_{\rm displaced}\]

![FIG-02-42-003: Submerged body with weight through center of gravity and buoyant force through center of buoyancy.](../figures/FIG-02-42-003-buoyant-force-and-archimedes-principle.png)

### Worked Example 3

**Problem.** A 0.020 m³ object is fully submerged in water. Find buoyant force.

**Solution.** FB=1000(9.81)(0.020)=196.2 N.

---

## 42.4 Floating Bodies

A floating body in static equilibrium displaces a weight of fluid equal to its own weight. The submerged volume adjusts until \(F_B=W\).

For a body crossing two immiscible fluids, the total buoyancy is the sum of the displaced-fluid weights in each fluid.

\[W=\sum_i \rho_i gV_i\]

![FIG-02-42-004: Floating body partially submerged in one fluid and a second example spanning two immiscible fluids.](../figures/FIG-02-42-004-floating-bodies.png)

### Worked Example 4

**Problem.** A floating object weighs 490.5 N in water. Find displaced volume.

**Solution.** V=W/(ρg)=0.0500 m³.

---

## 42.5 Resultant Force on a Plane Submerged Surface

Hydrostatic pressure varies linearly with depth. The resultant force on a plane surface equals pressure at the area centroid times area when the atmospheric contribution cancels on both sides.

Use vertical centroid depth \(h_C\), not slant distance, in \(P_C=ho gh_C\).

\[F_R=P_CA=\rho g h_C A\]

![FIG-02-42-005: Inclined submerged gate with centroid depth and distributed pressure replaced by resultant force.](../figures/FIG-02-42-005-resultant-force-on-a-plane-submerged-surface.png)

### Worked Example 5

**Problem.** A vertical gate area 2 m² has centroid 3 m below water surface. Find net hydrostatic force with atmospheric pressure both sides.

**Solution.** FR=ρghC A=58.86 kN.

---

## 42.6 Center of Pressure

Because pressure increases with depth, the resultant usually acts below the centroid for a submerged plane surface. The Handbook gives center-of-pressure relations using the centroidal area moment of inertia.

The geometry must match the axis used for \(I_{xC}\).

\[y_{CP}=y_C+\frac{I_{xC}}{y_CA}\]

![FIG-02-42-006: Triangular/trapezoidal pressure distribution on inclined plate with centroid and center of pressure.](../figures/FIG-02-42-006-center-of-pressure.png)

### Worked Example 6

**Problem.** Why is center of pressure below centroid for a vertical submerged plate?

**Solution.** Pressure increases with depth, weighting lower area more heavily.

---

## 42.7 Combined Hydrostatic Force and Equilibrium

Once hydrostatic resultants are determined, the gate, dam, or body can be analyzed by ordinary statics. Include hinge reactions, cable forces, body weight, and any pressure acting on the opposite side.

Separate the fluid problem from the rigid-body equilibrium problem rather than mixing pressure distribution algebra with support-reaction algebra.

\[\sum F=0,\qquad \sum M=0\]

![FIG-02-42-007: Hinged gate FBD with hydrostatic resultant, center-of-pressure location, weight, cable force, and reactions.](../figures/FIG-02-42-007-combined-hydrostatic-force-and-equilibrium.png)

### Worked Example 7

**Problem.** If an object density is less than fluid density, what does it do if free?

**Solution.** It rises until partially submerged and buoyancy equals weight.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What must a manometer traversal preserve?

**Solution.** Continuous pressure accounting across interfaces using each fluid density.

### Worked Example 9

**Problem.** Where does buoyant force act?

**Solution.** Through centroid of displaced fluid volume, the center of buoyancy.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Fluid Mechanics, printed pp. 183–185**.

**Source boundary:** The Handbook directly supplies simple-manometer relations, barometer principles, hydrostatic force and center-of-pressure formulas, and Archimedes' principle.

---

## Where This Goes Wrong

**Using manometer outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using barometer outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using buoyant force outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using floating equilibrium outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using hydrostatic resultant outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using center of pressure outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using hydrostatic equilibrium outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| manometer | Concept developed in §42.1; use the section definition and conditions. |
| barometer | Concept developed in §42.2; use the section definition and conditions. |
| buoyant force | Concept developed in §42.3; use the section definition and conditions. |
| floating equilibrium | Concept developed in §42.4; use the section definition and conditions. |
| hydrostatic resultant | Concept developed in §42.5; use the section definition and conditions. |
| center of pressure | Concept developed in §42.6; use the section definition and conditions. |
| hydrostatic equilibrium | Concept developed in §42.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **manometer** and state the governing equation or modeling rule.

2. Define **barometer** and state the governing equation or modeling rule.

3. Define **buoyant force** and state the governing equation or modeling rule.

4. Define **floating equilibrium** and state the governing equation or modeling rule.

5. Define **hydrostatic resultant** and state the governing equation or modeling rule.

6. Define **center of pressure** and state the governing equation or modeling rule.

7. Define **hydrostatic equilibrium** and state the governing equation or modeling rule.

8. What is the most likely error if **manometer** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **barometer** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **buoyant force** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **floating equilibrium** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **hydrostatic resultant** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **center of pressure** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **hydrostatic equilibrium** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **manometer**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **barometer**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **buoyant force**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **floating equilibrium**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **hydrostatic resultant**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **center of pressure**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **hydrostatic equilibrium**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **manometer**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **barometer**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **manometer** is developed in §42.1. Use the displayed relation together with that section's assumptions and units.

2. **barometer** is developed in §42.2. Use the displayed relation together with that section's assumptions and units.

3. **buoyant force** is developed in §42.3. Use the displayed relation together with that section's assumptions and units.

4. **floating equilibrium** is developed in §42.4. Use the displayed relation together with that section's assumptions and units.

5. **hydrostatic resultant** is developed in §42.5. Use the displayed relation together with that section's assumptions and units.

6. **center of pressure** is developed in §42.6. Use the displayed relation together with that section's assumptions and units.

7. **hydrostatic equilibrium** is developed in §42.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **manometer**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **barometer**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **buoyant force**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **floating equilibrium**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **hydrostatic resultant**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **center of pressure**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **hydrostatic equilibrium**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **manometer** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **barometer** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **buoyant force** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **floating equilibrium** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **hydrostatic resultant** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **center of pressure** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **hydrostatic equilibrium** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **manometer** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **barometer** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. A water manometer shows 0.40 m difference. Find pressure difference.

2. Mercury density is 13,600 kg/m³. A barometer column is 0.760 m and vapor pressure is neglected. Find atmospheric pressure.

3. A 0.020 m³ object is fully submerged in water. Find buoyant force.

4. A floating object weighs 490.5 N in water. Find displaced volume.

5. A vertical gate area 2 m² has centroid 3 m below water surface. Find net hydrostatic force with atmospheric pressure both sides.

6. Why is center of pressure below centroid for a vertical submerged plate?

7. If an object density is less than fluid density, what does it do if free?

8. What must a manometer traversal preserve?

9. Where does buoyant force act?

10. After finding hydrostatic resultant, what analysis determines hinge/cable forces?


---

## Practice Problem Solutions

1. ΔP=ρgh=3.924 kPa.

2. P=ρgh≈101.4 kPa.

3. FB=1000(9.81)(0.020)=196.2 N.

4. V=W/(ρg)=0.0500 m³.

5. FR=ρghC A=58.86 kN.

6. Pressure increases with depth, weighting lower area more heavily.

7. It rises until partially submerged and buoyancy equals weight.

8. Continuous pressure accounting across interfaces using each fluid density.

9. Through centroid of displaced fluid volume, the center of buoyancy.

10. Rigid-body equilibrium.


---

## Quick Reference

**Handbook anchor:** Fluid Mechanics, printed pp. 183–185.

- **manometer:** Simple Manometers
- **barometer:** Barometers and Atmospheric Pressure
- **buoyant force:** Buoyant Force and Archimedes' Principle
- **floating equilibrium:** Floating Bodies
- **hydrostatic resultant:** Resultant Force on a Plane Submerged Surface
- **center of pressure:** Center of Pressure
- **hydrostatic equilibrium:** Combined Hydrostatic Force and Equilibrium
---

## What's Next

**02-43 — Continuity, Velocity Fields, and Flow Kinematics**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor