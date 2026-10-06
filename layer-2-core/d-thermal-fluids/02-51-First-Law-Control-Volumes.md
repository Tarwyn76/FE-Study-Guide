---
chapter: "02-51"
title: "First Law — Control Volumes"
layer: 2
tier: D
template: technical
ledger_ids: [THERMO-2D-051-01, THERMO-2D-051-02, THERMO-2D-051-03, THERMO-2D-051-04, THERMO-2D-051-05, THERMO-2D-051-06, THERMO-2D-051-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-51: First Law — Control Volumes

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-50 Closed-System First Law · 02-43 Mass Conservation

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly supplies the open-system first law, steady-flow energy equation, and special cases for nozzles/diffusers, turbines, pumps/compressors, throttling valves, boilers/condensers, heat exchangers, mixers, and separators.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **51.1** Explain and apply **Open-System Energy Balance**.
* **51.2** Explain and apply **Steady-Flow Energy Equation**.
* **51.3** Explain and apply **Nozzles and Diffusers**.
* **51.4** Explain and apply **Turbines**.
* **51.5** Explain and apply **Compressors and Pumps**.
* **51.6** Explain and apply **Throttling Valves**.
* **51.7** Explain and apply **Heat Exchangers, Boilers, Condensers, and Mixers**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 51.1 Open-System Energy Balance

A control volume allows mass to cross the boundary. Flow energy is included through enthalpy \(h=u+Pv\).

The general balance includes accumulation plus heat, work, enthalpy, kinetic energy, and potential energy carried by mass streams.

\[\frac{dE_{CV}}{dt}=\dot Q-\dot W+\sum_{\rm in}\dot m\left(h+\frac{V^2}{2}+gz\right)-\sum_{\rm out}\dot m\left(h+\frac{V^2}{2}+gz\right)\]

![FIG-02-51-001: Open control volume with heat, shaft work, mass streams, and specific flow energies.](../figures/FIG-02-51-001-open-system-energy-balance.png)

### Worked Example 1

**Problem.** Steady nozzle: h1=500 kJ/kg, h2=450 kJ/kg, V1≈0. Find exit speed neglecting heat/work/PE.

**Solution.** V2=sqrt(2*50,000)=316.2 m/s.

---

## 51.2 Steady-Flow Energy Equation

At steady state, energy stored inside the control volume does not change with time. For one inlet and one outlet, the balance simplifies substantially.

Mass flow is constant through a one-stream steady device.

\[\dot Q-\dot W=\dot m\left[(h_2-h_1)+\frac{V_2^2-V_1^2}{2}+g(z_2-z_1)\right]\]

![FIG-02-51-002: Generic one-inlet one-outlet device with steady-flow energy terms.](../figures/FIG-02-51-002-steady-flow-energy-equation.png)

### Worked Example 2

**Problem.** Adiabatic turbine h1=1200, h2=900 kJ/kg. Find specific work output.

**Solution.** 300 kJ/kg.

---

## 51.3 Nozzles and Diffusers

Nozzles convert enthalpy to kinetic energy; diffusers do the reverse. The Handbook special case neglects work, heat transfer, and elevation change when appropriate.

Velocity changes may dominate the balance.

\[h_1+\frac{V_1^2}{2}=h_2+\frac{V_2^2}{2}\]

![FIG-02-51-003: Nozzle and diffuser showing area, velocity, pressure, and enthalpy changes.](../figures/FIG-02-51-003-nozzles-and-diffusers.png)

### Worked Example 3

**Problem.** Compressor h1=300, h2=420 kJ/kg. Find specific work input.

**Solution.** 120 kJ/kg.

---

## 51.4 Turbines

An adiabatic turbine with negligible KE/PE change produces shaft work as enthalpy decreases.

Actual turbine efficiency compares actual work with the isentropic reference expansion.

\[w_t=h_1-h_2,\qquad \eta_t=\frac{h_1-h_2}{h_1-h_{2s}}\]

![FIG-02-51-004: Turbine with inlet/outlet states and actual versus isentropic exit enthalpy.](../figures/FIG-02-51-004-turbines.png)

### Worked Example 4

**Problem.** Throttling valve inlet h=250 kJ/kg. What is outlet h under ideal throttling assumptions?

**Solution.** 250 kJ/kg.

---

## 51.5 Compressors and Pumps

Compressors and pumps require work input. For an adiabatic compressor with negligible KE/PE change, \(w_{in}=h_2-h_1\).

For an incompressible pump, the isentropic enthalpy rise is approximated by \(v(P_2-P_1)\).

\[\eta_c=\frac{h_{2s}-h_1}{h_2-h_1},\qquad w_{p,s}\approx v(P_2-P_1)\]

![FIG-02-51-005: Compressor and pump diagrams with work input and isentropic-efficiency definitions.](../figures/FIG-02-51-005-compressors-and-pumps.png)

### Worked Example 5

**Problem.** Adiabatic pump v=0.001 m³/kg raises pressure by 5 MPa ideally. Find specific work.

**Solution.** w=vΔP=5 kJ/kg.

---

## 51.6 Throttling Valves

A throttling valve has no shaft work, usually negligible heat transfer and KE/PE change, so enthalpy remains approximately constant.

Pressure can fall substantially even though \(h_1=h_2\).

\[h_1=h_2\]

![FIG-02-51-006: Throttling valve with pressure drop and constant enthalpy on a P-h diagram.](../figures/FIG-02-51-006-throttling-valves.png)

### Worked Example 6

**Problem.** What energy property naturally includes flow work?

**Solution.** Enthalpy.

---

## 51.7 Heat Exchangers, Boilers, Condensers, and Mixers

A boiler or condenser on one stream commonly uses \(q=h_2-h_1\). An insulated two-stream heat exchanger has no net heat loss to surroundings, so energy lost by one stream is gained by the other.

Mixers require both mass and energy balances.

\[\sum\dot m_{\rm in}h_{\rm in}=\sum\dot m_{\rm out}h_{\rm out}\quad\text{(adiabatic mixer, negligible KE/PE)}\]

![FIG-02-51-007: Boiler, condenser, two-stream heat exchanger, and mixing chamber with simplified energy balances.](../figures/FIG-02-51-007-heat-exchangers-boilers-condensers-and-mixers.png)

### Worked Example 7

**Problem.** At steady state, what happens to energy accumulation in the control volume?

**Solution.** Zero.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A boiler with one stream and no work has h1=500, h2=1500 kJ/kg. Find q.

**Solution.** 1000 kJ/kg added.

### Worked Example 9

**Problem.** An insulated two-stream heat exchanger loses no heat externally. What relation holds?

**Solution.** Energy lost by hot stream equals energy gained by cold stream.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Thermodynamics, printed pp. 147–149**.

**Source boundary:** The Handbook directly supplies the open-system first law, steady-flow energy equation, and special cases for nozzles/diffusers, turbines, pumps/compressors, throttling valves, boilers/condensers, heat exchangers, mixers, and separators.

---

## Where This Goes Wrong

**Using control-volume energy balance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using steady-flow energy equation outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using nozzle energy balance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using turbine energy balance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using compressor and pump outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using throttling process outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using steady-flow components outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| control-volume energy balance | Concept developed in §51.1; use the section definition and conditions. |
| steady-flow energy equation | Concept developed in §51.2; use the section definition and conditions. |
| nozzle energy balance | Concept developed in §51.3; use the section definition and conditions. |
| turbine energy balance | Concept developed in §51.4; use the section definition and conditions. |
| compressor and pump | Concept developed in §51.5; use the section definition and conditions. |
| throttling process | Concept developed in §51.6; use the section definition and conditions. |
| steady-flow components | Concept developed in §51.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **control-volume energy balance** and state the governing equation or modeling rule.

2. Define **steady-flow energy equation** and state the governing equation or modeling rule.

3. Define **nozzle energy balance** and state the governing equation or modeling rule.

4. Define **turbine energy balance** and state the governing equation or modeling rule.

5. Define **compressor and pump** and state the governing equation or modeling rule.

6. Define **throttling process** and state the governing equation or modeling rule.

7. Define **steady-flow components** and state the governing equation or modeling rule.

8. What is the most likely error if **control-volume energy balance** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **steady-flow energy equation** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **nozzle energy balance** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **turbine energy balance** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **compressor and pump** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **throttling process** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **steady-flow components** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **control-volume energy balance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **steady-flow energy equation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **nozzle energy balance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **turbine energy balance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **compressor and pump**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **throttling process**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **steady-flow components**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **control-volume energy balance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **steady-flow energy equation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **control-volume energy balance** is developed in §51.1. Use the displayed relation together with that section's assumptions and units.

2. **steady-flow energy equation** is developed in §51.2. Use the displayed relation together with that section's assumptions and units.

3. **nozzle energy balance** is developed in §51.3. Use the displayed relation together with that section's assumptions and units.

4. **turbine energy balance** is developed in §51.4. Use the displayed relation together with that section's assumptions and units.

5. **compressor and pump** is developed in §51.5. Use the displayed relation together with that section's assumptions and units.

6. **throttling process** is developed in §51.6. Use the displayed relation together with that section's assumptions and units.

7. **steady-flow components** is developed in §51.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **control-volume energy balance**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **steady-flow energy equation**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **nozzle energy balance**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **turbine energy balance**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **compressor and pump**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **throttling process**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **steady-flow components**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **control-volume energy balance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **steady-flow energy equation** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **nozzle energy balance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **turbine energy balance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **compressor and pump** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **throttling process** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **steady-flow components** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **control-volume energy balance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **steady-flow energy equation** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Steady nozzle: h1=500 kJ/kg, h2=450 kJ/kg, V1≈0. Find exit speed neglecting heat/work/PE.

2. Adiabatic turbine h1=1200, h2=900 kJ/kg. Find specific work output.

3. Compressor h1=300, h2=420 kJ/kg. Find specific work input.

4. Throttling valve inlet h=250 kJ/kg. What is outlet h under ideal throttling assumptions?

5. Adiabatic pump v=0.001 m³/kg raises pressure by 5 MPa ideally. Find specific work.

6. What energy property naturally includes flow work?

7. At steady state, what happens to energy accumulation in the control volume?

8. A boiler with one stream and no work has h1=500, h2=1500 kJ/kg. Find q.

9. An insulated two-stream heat exchanger loses no heat externally. What relation holds?

10. Why may KE matter in a nozzle but be negligible in a turbine?


---

## Practice Problem Solutions

1. V2=sqrt(2*50,000)=316.2 m/s.

2. 300 kJ/kg.

3. 120 kJ/kg.

4. 250 kJ/kg.

5. w=vΔP=5 kJ/kg.

6. Enthalpy.

7. Zero.

8. 1000 kJ/kg added.

9. Energy lost by hot stream equals energy gained by cold stream.

10. Nozzles are specifically designed for large velocity change; many turbines have modest inlet/outlet velocity differences relative to enthalpy change.


---

## Quick Reference

**Handbook anchor:** Thermodynamics, printed pp. 147–149.

- **control-volume energy balance:** Open-System Energy Balance
- **steady-flow energy equation:** Steady-Flow Energy Equation
- **nozzle energy balance:** Nozzles and Diffusers
- **turbine energy balance:** Turbines
- **compressor and pump:** Compressors and Pumps
- **throttling process:** Throttling Valves
- **steady-flow components:** Heat Exchangers, Boilers, Condensers, and Mixers
---

## What's Next

**02-52 — Second Law, Entropy, and Isentropic Processes**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor