---
chapter: "02-46"
title: "Momentum, Flow Measurement, Pumps, and Turbines"
layer: 2
tier: D
template: technical
ledger_ids: [FLUID-2D-046-01, FLUID-2D-046-02, FLUID-2D-046-03, FLUID-2D-046-04, FLUID-2D-046-05, FLUID-2D-046-06, FLUID-2D-046-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-46: Momentum, Flow Measurement, Pumps, and Turbines

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-43 Continuity · 02-44 Mechanical Energy · 02-45 Internal Flow

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly supplies the impulse-momentum principle, pipe-bend/jet/blade force relations, pump/fan/compressor/turbine performance and affinity laws, and pitot/venturi flow-measurement relations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **46.1** Explain and apply **Control-Volume Linear Momentum**.
* **46.2** Explain and apply **Forces on Pipe Bends, Jets, and Blades**.
* **46.3** Explain and apply **Pitot/Stagnation Measurements**.
* **46.4** Explain and apply **Venturi and Differential-Pressure Flowmeters**.
* **46.5** Explain and apply **Pump Head, Power, and Efficiency**.
* **46.6** Explain and apply **Pump/Fan Affinity Laws and Performance Curves**.
* **46.7** Explain and apply **Turbines and Energy Extraction**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 46.1 Control-Volume Linear Momentum

For steady one-dimensional streams, the net external force on a control volume equals the net momentum-flow rate leaving minus entering.

Pressure forces, body forces, and support forces all belong in the external-force sum.

\[\sum\mathbf F=\sum_{\rm out}\dot m\,\mathbf v-\sum_{\rm in}\dot m\,\mathbf v\]

![FIG-02-46-001: Control volume around a nozzle/bend with inlet/outlet momentum vectors and external forces.](../figures/FIG-02-46-001-control-volume-linear-momentum.png)

### Worked Example 1

**Problem.** Water flow 0.05 m³/s turns from +x at 4 m/s to +y at 4 m/s. Find momentum-flow change vector using ρ=1000 kg/m³.

**Solution.** ṁ=50 kg/s; Δ(momentum rate)=(-200 i+200 j) N.

---

## 46.2 Forces on Pipe Bends, Jets, and Blades

Apply momentum separately in coordinate directions. The force solved in the fluid control volume is the force of surroundings on the fluid; the force of the fluid on the hardware is equal and opposite.

Pressure forces use pressure times area and act inward on the control surface.

\[\mathbf F_{\rm fluid\ on\ hardware}=-\mathbf F_{\rm hardware\ on\ fluid}\]

![FIG-02-46-002: Pipe bend with pressure forces, weight, velocities, and reaction components.](../figures/FIG-02-46-002-forces-on-pipe-bends-jets-and-blades.png)

### Worked Example 2

**Problem.** A jet Q=0.01 m³/s, ρ=1000 kg/m³ is brought to rest from 20 m/s in x. Find force magnitude on plate.

**Solution.** F=ρQv=200 N.

---

## 46.3 Pitot/Stagnation Measurements

For incompressible flow, stagnation pressure minus static pressure corresponds to velocity head. The Handbook allows the incompressible relation for compressible flow only at sufficiently low Mach number as stated there.

Pitot measurements determine local velocity, not automatically section-average flow.

\[v=\sqrt{\frac{2(P_0-P_s)}{\rho}}\]

![FIG-02-46-003: Pitot-static probe showing stagnation pressure, static pressure, and inferred velocity.](../figures/FIG-02-46-003-pitot-stagnation-measurements.png)

### Worked Example 3

**Problem.** Water stagnation-static pressure difference is 5 kPa. Find velocity.

**Solution.** v=sqrt(2ΔP/ρ)=3.162 m/s.

---

## 46.4 Venturi and Differential-Pressure Flowmeters

A venturi meter combines continuity with Bernoulli and a calibration coefficient. Reduced throat area increases speed and lowers static pressure.

Orifices use the same energy idea but generally produce greater permanent pressure loss.

\[Q=C_vA_2\sqrt{\frac{2\Delta P/\rho}{1-(A_2/A_1)^2}}\quad\text{(level incompressible form)}\]

![FIG-02-46-004: Venturi with upstream/throat pressures, areas, velocities, and differential-pressure measurement.](../figures/FIG-02-46-004-venturi-and-differential-pressure-flowmeters.png)

### Worked Example 4

**Problem.** A pump moves water Q=0.02 m³/s through 30 m head at total efficiency 0.75. Find input power.

**Solution.** Win=ρgQH/η=7.85 kW.

---

## 46.5 Pump Head, Power, and Efficiency

A pump adds mechanical energy to a liquid. Hydraulic power is \(ho gQH\); required input power is higher when efficiency is below 1.

The operating point is set by both the pump curve and the system curve.

\[\dot W_{\rm in}=\frac{\rho gQH}{\eta_{\rm total}}\]

![FIG-02-46-005: Pump between reservoirs with head rise, flow rate, efficiency, and hydraulic/input power.](../figures/FIG-02-46-005-pump-head-power-and-efficiency.png)

### Worked Example 5

**Problem.** If pump speed rises 10% at same diameter/density, estimate flow ratio by affinity laws.

**Solution.** Q2/Q1=1.10.

---

## 46.6 Pump/Fan Affinity Laws and Performance Curves

For geometrically similar machines or speed changes under the Handbook scaling assumptions, flow scales with \(ND^3\), head with \(N^2D^2\), and power with \(ho N^3D^5\).

Use affinity laws only when dynamic similarity assumptions are reasonable.

\[Q\propto ND^3,\qquad H\propto N^2D^2,\qquad \dot W\propto \rho N^3D^5\]

![FIG-02-46-006: Pump/fan performance curves and arrows showing speed-change affinity scaling.](../figures/FIG-02-46-006-pump-fan-affinity-laws-and-performance-curves.png)

### Worked Example 6

**Problem.** Under same speed change, estimate head ratio.

**Solution.** H2/H1=1.10²=1.21.

---

## 46.7 Turbines and Energy Extraction

A turbine extracts energy from a fluid, reducing fluid head or enthalpy while producing shaft work. Fluid-mechanics turbine analysis can use mechanical head; thermodynamic turbine analysis commonly uses enthalpy change.

Keep the chosen energy basis consistent.

\[\dot W_{\rm out}\approx \rho gQH_t\eta_t\]

![FIG-02-46-007: Hydraulic turbine with inlet/outlet head, flow, shaft power, and efficiency.](../figures/FIG-02-46-007-turbines-and-energy-extraction.png)

### Worked Example 7

**Problem.** Under same speed change, estimate power ratio.

**Solution.** W2/W1=1.10³=1.331.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What pressure does a Pitot tube measure at its forward stagnation opening?

**Solution.** Stagnation pressure.

### Worked Example 9

**Problem.** What does a turbine do to fluid mechanical energy?

**Solution.** Extracts it and converts part to shaft work.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Fluid Mechanics, printed pp. 191–200**.

**Source boundary:** The Handbook directly supplies the impulse-momentum principle, pipe-bend/jet/blade force relations, pump/fan/compressor/turbine performance and affinity laws, and pitot/venturi flow-measurement relations.

---

## Where This Goes Wrong

**Using fluid momentum balance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using flow-induced force outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Pitot tube outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Venturi meter outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using pump power outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using affinity laws outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using fluid turbine outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| fluid momentum balance | Concept developed in §46.1; use the section definition and conditions. |
| flow-induced force | Concept developed in §46.2; use the section definition and conditions. |
| Pitot tube | Concept developed in §46.3; use the section definition and conditions. |
| Venturi meter | Concept developed in §46.4; use the section definition and conditions. |
| pump power | Concept developed in §46.5; use the section definition and conditions. |
| affinity laws | Concept developed in §46.6; use the section definition and conditions. |
| fluid turbine | Concept developed in §46.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **fluid momentum balance** and state the governing equation or modeling rule.

2. Define **flow-induced force** and state the governing equation or modeling rule.

3. Define **Pitot tube** and state the governing equation or modeling rule.

4. Define **Venturi meter** and state the governing equation or modeling rule.

5. Define **pump power** and state the governing equation or modeling rule.

6. Define **affinity laws** and state the governing equation or modeling rule.

7. Define **fluid turbine** and state the governing equation or modeling rule.

8. What is the most likely error if **fluid momentum balance** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **flow-induced force** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **Pitot tube** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **Venturi meter** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **pump power** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **affinity laws** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **fluid turbine** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **fluid momentum balance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **flow-induced force**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **Pitot tube**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **Venturi meter**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **pump power**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **affinity laws**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **fluid turbine**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **fluid momentum balance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **flow-induced force**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **fluid momentum balance** is developed in §46.1. Use the displayed relation together with that section's assumptions and units.

2. **flow-induced force** is developed in §46.2. Use the displayed relation together with that section's assumptions and units.

3. **Pitot tube** is developed in §46.3. Use the displayed relation together with that section's assumptions and units.

4. **Venturi meter** is developed in §46.4. Use the displayed relation together with that section's assumptions and units.

5. **pump power** is developed in §46.5. Use the displayed relation together with that section's assumptions and units.

6. **affinity laws** is developed in §46.6. Use the displayed relation together with that section's assumptions and units.

7. **fluid turbine** is developed in §46.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **fluid momentum balance**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **flow-induced force**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Pitot tube**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Venturi meter**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **pump power**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **affinity laws**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **fluid turbine**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **fluid momentum balance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **flow-induced force** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **Pitot tube** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **Venturi meter** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **pump power** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **affinity laws** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **fluid turbine** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **fluid momentum balance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **flow-induced force** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Water flow 0.05 m³/s turns from +x at 4 m/s to +y at 4 m/s. Find momentum-flow change vector using ρ=1000 kg/m³.

2. A jet Q=0.01 m³/s, ρ=1000 kg/m³ is brought to rest from 20 m/s in x. Find force magnitude on plate.

3. Water stagnation-static pressure difference is 5 kPa. Find velocity.

4. A pump moves water Q=0.02 m³/s through 30 m head at total efficiency 0.75. Find input power.

5. If pump speed rises 10% at same diameter/density, estimate flow ratio by affinity laws.

6. Under same speed change, estimate head ratio.

7. Under same speed change, estimate power ratio.

8. What pressure does a Pitot tube measure at its forward stagnation opening?

9. What does a turbine do to fluid mechanical energy?

10. Why is hardware force opposite the force solved on the fluid CV?


---

## Practice Problem Solutions

1. ṁ=50 kg/s; Δ(momentum rate)=(-200 i+200 j) N.

2. F=ρQv=200 N.

3. v=sqrt(2ΔP/ρ)=3.162 m/s.

4. Win=ρgQH/η=7.85 kW.

5. Q2/Q1=1.10.

6. H2/H1=1.10²=1.21.

7. W2/W1=1.10³=1.331.

8. Stagnation pressure.

9. Extracts it and converts part to shaft work.

10. Newton's third law.


---

## Quick Reference

**Handbook anchor:** Fluid Mechanics, printed pp. 191–200.

- **fluid momentum balance:** Control-Volume Linear Momentum
- **flow-induced force:** Forces on Pipe Bends, Jets, and Blades
- **Pitot tube:** Pitot/Stagnation Measurements
- **Venturi meter:** Venturi and Differential-Pressure Flowmeters
- **pump power:** Pump Head, Power, and Efficiency
- **affinity laws:** Pump/Fan Affinity Laws and Performance Curves
- **fluid turbine:** Turbines and Energy Extraction
---

## What's Next

**02-47 — Thermodynamic Systems, Properties, Work, and Heat**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor