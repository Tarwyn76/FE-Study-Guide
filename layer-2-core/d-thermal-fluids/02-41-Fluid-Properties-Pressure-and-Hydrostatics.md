---
chapter: "02-41"
title: "Fluid Properties, Pressure, and Hydrostatics"
layer: 2
tier: D
template: technical
ledger_ids: [FLUID-2D-041-01, FLUID-2D-041-02, FLUID-2D-041-03, FLUID-2D-041-04, FLUID-2D-041-05, FLUID-2D-041-06, FLUID-2D-041-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-41: Fluid Properties, Pressure, and Hydrostatics

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-20 Fire, Explosion, Electrical, and Confined-Space Hazards · 01-02 Units and Dimensions

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines density, specific weight, specific gravity, dynamic/kinematic viscosity, Newtonian and power-law behavior, surface tension, capillary rise, absolute/gauge/vacuum pressure, and the hydrostatic pressure field.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **41.1** Explain and apply **Density, Specific Volume, Specific Weight, and Specific Gravity**.
* **41.2** Explain and apply **Pressure, Absolute Pressure, Gauge Pressure, and Vacuum**.
* **41.3** Explain and apply **Dynamic and Kinematic Viscosity**.
* **41.4** Explain and apply **Newtonian and Non-Newtonian Behavior**.
* **41.5** Explain and apply **Surface Tension and Capillarity**.
* **41.6** Explain and apply **Hydrostatic Pressure Variation**.
* **41.7** Explain and apply **Hydrostatic Modeling Checks**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 41.1 Density, Specific Volume, Specific Weight, and Specific Gravity

Fluid-property calculations begin by distinguishing mass per volume from weight per volume. Density is \(ho=m/V\), specific volume is \(v=1/ho\), and specific weight is \(\gamma=ho g\). Specific gravity compares fluid density or specific weight to water at the stated reference condition.

Do not mix mass density and specific weight. In SI, density has units kg/m³ while specific weight has units N/m³.

\[\rho=\frac{m}{V},\qquad v=\frac1\rho,\qquad \gamma=\rho g,\qquad SG=\frac{\rho}{\rho_w}\]

![FIG-02-41-001: Fluid property map linking density, specific volume, specific weight, and specific gravity.](../figures/FIG-02-41-001-density-specific-volume-specific-weight-and-specific-gravity.png)

### Worked Example 1

**Problem.** Water has density 1000 kg/m³. Find specific weight at g=9.81 m/s².

**Solution.** γ=ρg=9.81 kN/m³.

---

## 41.2 Pressure, Absolute Pressure, Gauge Pressure, and Vacuum

Pressure is normal compressive stress in a fluid. Engineering instruments often report gauge pressure relative to local atmosphere, while thermodynamic equations require absolute pressure.

A vacuum gauge reports how far pressure lies below atmospheric pressure. Always identify the pressure reference before inserting a value into an equation.

\[P_{\rm abs}=P_{\rm atm}+P_{\rm gage},\qquad P_{\rm abs}=P_{\rm atm}-P_{\rm vacuum}\]

![FIG-02-41-002: Absolute-pressure scale showing vacuum, atmospheric pressure, gauge pressure, and absolute zero.](../figures/FIG-02-41-002-pressure-absolute-pressure-gauge-pressure-and-vacuum.png)

### Worked Example 2

**Problem.** An oil has SG=0.85. Find density using ρw=1000 kg/m³.

**Solution.** ρ=850 kg/m³.

---

## 41.3 Dynamic and Kinematic Viscosity

Viscosity measures resistance to shear deformation. For a Newtonian fluid, shear stress is proportional to velocity gradient. Kinematic viscosity divides dynamic viscosity by density.

Viscosity is strongly temperature-dependent for many fluids, so use properties at the temperature specified by the problem.

\[\tau=\mu\frac{dv}{dy},\qquad \nu=\frac{\mu}{\rho}\]

![FIG-02-41-003: Newtonian fluid between plates showing velocity gradient and shear stress.](../figures/FIG-02-41-003-dynamic-and-kinematic-viscosity.png)

### Worked Example 3

**Problem.** A gauge reads 250 kPa with atmospheric pressure 101 kPa. Find absolute pressure.

**Solution.** Pabs=351 kPa.

---

## 41.4 Newtonian and Non-Newtonian Behavior

A Newtonian fluid has a linear shear-stress versus shear-rate relation with constant \(\mu\). The Handbook also gives a power-law model \(	au=K(dv/dy)^n\).

For \(n<1\), the model is pseudoplastic/shear-thinning; for \(n>1\), it is dilatant/shear-thickening. Do not assume a constant viscosity model when the problem explicitly provides non-Newtonian parameters.

\[\tau=K\left(\frac{dv}{dy}\right)^n\]

![FIG-02-41-004: Shear stress versus shear rate for Newtonian, shear-thinning, and shear-thickening fluids.](../figures/FIG-02-41-004-newtonian-and-non-newtonian-behavior.png)

### Worked Example 4

**Problem.** Dynamic viscosity is 0.002 Pa·s and density is 800 kg/m³. Find kinematic viscosity.

**Solution.** ν=μ/ρ=2.50×10^-6 m²/s.

---

## 41.5 Surface Tension and Capillarity

Surface tension is force per unit contact length at an interface. In a small tube, the balance of surface-tension forces and liquid weight produces capillary rise or depression.

The contact angle determines the sign through \(\coseta\). The capillary effect becomes stronger as tube diameter decreases.

\[\sigma=\frac{F}{L},\qquad h=\frac{4\sigma\cos\beta}{\gamma d}\]

![FIG-02-41-005: Liquid column in a capillary tube with contact angle, surface tension, diameter, and capillary rise.](../figures/FIG-02-41-005-surface-tension-and-capillarity.png)

### Worked Example 5

**Problem.** A Newtonian fluid has μ=0.5 Pa·s and dv/dy=4 s^-1. Find shear stress.

**Solution.** τ=2.0 Pa.

---

## 41.6 Hydrostatic Pressure Variation

In a static fluid of constant density, pressure increases with depth. Pressure at points on the same horizontal level in the same connected static fluid is equal.

The pressure difference depends only on vertical elevation difference, not container shape.

\[P_2-P_1=-\gamma(z_2-z_1)=\rho g(z_1-z_2)\]

![FIG-02-41-006: Static liquid tank with two elevations and linear pressure increase with depth.](../figures/FIG-02-41-006-hydrostatic-pressure-variation.png)

### Worked Example 6

**Problem.** A point is 3 m below a free water surface. Find gauge pressure using ρ=1000 kg/m³.

**Solution.** P=ρgh=29.43 kPa.

---

## 41.7 Hydrostatic Modeling Checks

Before solving a fluid-statics problem, identify the fluid, density or specific weight, gravitational field, vertical coordinate sign, and pressure reference.

Hydrostatic equations do not apply through regions with significant fluid acceleration. If the fluid is moving but pressure variation is being approximated hydrostatically, the assumptions must be justified.

\[\text{static fluid}\Rightarrow \frac{dP}{dz}=-\rho g\]

![FIG-02-41-007: Hydrostatic-analysis checklist covering pressure reference, fluid density, elevations, and static assumption.](../figures/FIG-02-41-007-hydrostatic-modeling-checks.png)

### Worked Example 7

**Problem.** A 1-mm capillary contains water with σ=0.072 N/m, β=0°, γ=9810 N/m³. Estimate rise.

**Solution.** h=4σ/(γd)=0.0294 m.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Distinguish gauge pressure from absolute pressure.

**Solution.** Gauge is relative to atmosphere; absolute is relative to vacuum.

### Worked Example 9

**Problem.** What does n<1 mean in the power-law model?

**Solution.** Shear-thinning/pseudoplastic behavior.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Fluid Mechanics, printed pp. 181–182**.

**Source boundary:** The Handbook directly defines density, specific weight, specific gravity, dynamic/kinematic viscosity, Newtonian and power-law behavior, surface tension, capillary rise, absolute/gauge/vacuum pressure, and the hydrostatic pressure field.

---

## Where This Goes Wrong

**Using fluid density outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using fluid pressure outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using viscosity outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using non-Newtonian fluid outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using capillarity outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using hydrostatic pressure outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using hydrostatic model outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| fluid density | Concept developed in §41.1; use the section definition and conditions. |
| fluid pressure | Concept developed in §41.2; use the section definition and conditions. |
| viscosity | Concept developed in §41.3; use the section definition and conditions. |
| non-Newtonian fluid | Concept developed in §41.4; use the section definition and conditions. |
| capillarity | Concept developed in §41.5; use the section definition and conditions. |
| hydrostatic pressure | Concept developed in §41.6; use the section definition and conditions. |
| hydrostatic model | Concept developed in §41.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **fluid density** and state the governing equation or modeling rule.

2. Define **fluid pressure** and state the governing equation or modeling rule.

3. Define **viscosity** and state the governing equation or modeling rule.

4. Define **non-Newtonian fluid** and state the governing equation or modeling rule.

5. Define **capillarity** and state the governing equation or modeling rule.

6. Define **hydrostatic pressure** and state the governing equation or modeling rule.

7. Define **hydrostatic model** and state the governing equation or modeling rule.

8. What is the most likely error if **fluid density** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **fluid pressure** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **viscosity** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **non-Newtonian fluid** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **capillarity** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **hydrostatic pressure** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **hydrostatic model** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **fluid density**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **fluid pressure**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **viscosity**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **non-Newtonian fluid**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **capillarity**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **hydrostatic pressure**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **hydrostatic model**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **fluid density**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **fluid pressure**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **fluid density** is developed in §41.1. Use the displayed relation together with that section's assumptions and units.

2. **fluid pressure** is developed in §41.2. Use the displayed relation together with that section's assumptions and units.

3. **viscosity** is developed in §41.3. Use the displayed relation together with that section's assumptions and units.

4. **non-Newtonian fluid** is developed in §41.4. Use the displayed relation together with that section's assumptions and units.

5. **capillarity** is developed in §41.5. Use the displayed relation together with that section's assumptions and units.

6. **hydrostatic pressure** is developed in §41.6. Use the displayed relation together with that section's assumptions and units.

7. **hydrostatic model** is developed in §41.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **fluid density**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **fluid pressure**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **viscosity**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **non-Newtonian fluid**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **capillarity**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **hydrostatic pressure**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **hydrostatic model**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **fluid density** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **fluid pressure** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **viscosity** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **non-Newtonian fluid** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **capillarity** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **hydrostatic pressure** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **hydrostatic model** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **fluid density** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **fluid pressure** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Water has density 1000 kg/m³. Find specific weight at g=9.81 m/s².

2. An oil has SG=0.85. Find density using ρw=1000 kg/m³.

3. A gauge reads 250 kPa with atmospheric pressure 101 kPa. Find absolute pressure.

4. Dynamic viscosity is 0.002 Pa·s and density is 800 kg/m³. Find kinematic viscosity.

5. A Newtonian fluid has μ=0.5 Pa·s and dv/dy=4 s^-1. Find shear stress.

6. A point is 3 m below a free water surface. Find gauge pressure using ρ=1000 kg/m³.

7. A 1-mm capillary contains water with σ=0.072 N/m, β=0°, γ=9810 N/m³. Estimate rise.

8. Distinguish gauge pressure from absolute pressure.

9. What does n<1 mean in the power-law model?

10. Why is pressure at the same horizontal level equal in a connected static fluid?


---

## Practice Problem Solutions

1. γ=ρg=9.81 kN/m³.

2. ρ=850 kg/m³.

3. Pabs=351 kPa.

4. ν=μ/ρ=2.50×10^-6 m²/s.

5. τ=2.0 Pa.

6. P=ρgh=29.43 kPa.

7. h=4σ/(γd)=0.0294 m.

8. Gauge is relative to atmosphere; absolute is relative to vacuum.

9. Shear-thinning/pseudoplastic behavior.

10. Hydrostatic pressure depends on elevation; equal z gives equal P within the same connected fluid.


---

## Quick Reference

**Handbook anchor:** Fluid Mechanics, printed pp. 181–182.

- **fluid density:** Density, Specific Volume, Specific Weight, and Specific Gravity
- **fluid pressure:** Pressure, Absolute Pressure, Gauge Pressure, and Vacuum
- **viscosity:** Dynamic and Kinematic Viscosity
- **non-Newtonian fluid:** Newtonian and Non-Newtonian Behavior
- **capillarity:** Surface Tension and Capillarity
- **hydrostatic pressure:** Hydrostatic Pressure Variation
- **hydrostatic model:** Hydrostatic Modeling Checks
---

## What's Next

**02-42 — Buoyancy, Manometry, and Forces on Submerged Surfaces**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor