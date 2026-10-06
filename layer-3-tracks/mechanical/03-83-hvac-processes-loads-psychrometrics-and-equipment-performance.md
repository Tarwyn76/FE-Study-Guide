---
chapter: "03-83"
title: "HVAC Processes, Loads, Psychrometrics, and Equipment Performance"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-083-01, MEC-3-083-02, MEC-3-083-03, MEC-3-083-04, MEC-3-083-05, MEC-3-083-06, MEC-3-083-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-83: HVAC Processes, Loads, Psychrometrics, and Equipment Performance

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** THERMO-2D-047-01 · HT-2D-055-01

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **HVAC Processes, Loads, Psychrometrics, and Equipment Performance**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **83.1** Explain and apply **Dry-bulb, wet-bulb, humidity ratio, and relative humidity**.
* **83.2** Explain and apply **Sensible heating and cooling**.
* **83.3** Explain and apply **Cooling and dehumidification**.
* **83.4** Explain and apply **Humidification and evaporative cooling**.
* **83.5** Explain and apply **Mixing of moist-air streams**.
* **83.6** Explain and apply **Building sensible and latent loads**.
* **83.7** Explain and apply **COP, equipment capacity, and HVAC performance**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 83.1 Dry-bulb, wet-bulb, humidity ratio, and relative humidity

Moist-air state is described by pressure plus two independent properties. Psychrometric charts connect temperature, humidity ratio, relative humidity, and enthalpy.

\[\omega=0.622\frac{P_v}{P-P_v}\]

![FIG-03-83-001: Psychrometric chart with dry-bulb, humidity ratio, relative humidity, wet-bulb, enthalpy, and a state point.](../figures/FIG-03-83-001-dry-bulb-wet-bulb-humidity-ratio-and-relative-humidity.png)

### Worked Example 1

**Problem.** At a fixed pressure and humidity ratio, heating air lowers relative humidity.

**Solution.** Apply the relation and model in §83.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 83.2 Sensible heating and cooling

Sensible processes change dry-bulb temperature without changing humidity ratio, absent condensation or humidification.

\[\dot Q_s=\dot m_a c_p(T_2-T_1)\]

![FIG-03-83-002: Horizontal sensible heating and cooling paths on a psychrometric chart.](../figures/FIG-03-83-002-sensible-heating-and-cooling.png)

### Worked Example 2

**Problem.** Heating 1 kg/s of air by 10 K requires about 10 kW per kJ/(kg·K) of cp.

**Solution.** Apply the relation and model in §83.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 83.3 Cooling and dehumidification

Cooling below dew point removes both sensible and latent heat and condenses water. Coil leaving conditions are limited by apparatus dew point and bypass behavior.

\[\dot Q=\dot m_a(h_1-h_2)\]

![FIG-03-83-003: Cooling coil with condensate drain and psychrometric path downward-left.](../figures/FIG-03-83-003-cooling-and-dehumidification.png)

### Worked Example 3

**Problem.** A dehumidifying coil reduces both enthalpy and humidity ratio.

**Solution.** Apply the relation and model in §83.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 83.4 Humidification and evaporative cooling

Humidification adds moisture. Adiabatic evaporative humidification can lower dry-bulb temperature while increasing humidity ratio.

\[\dot m_w=\dot m_a(\omega_2-\omega_1)\]

![FIG-03-83-004: Humidifier/evaporative cooler with psychrometric path and water mass balance.](../figures/FIG-03-83-004-humidification-and-evaporative-cooling.png)

### Worked Example 4

**Problem.** If humidity ratio rises by 0.004 kg/kg for 2 kg/s dry air, water addition is 0.008 kg/s.

**Solution.** Apply the relation and model in §83.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 83.5 Mixing of moist-air streams

Two air streams mix to an intermediate state governed by mass and energy balances. On a psychrometric chart, the mixture lies on the straight line between the entering states.

\[\dot m_1 h_1+\dot m_2 h_2=(\dot m_1+\dot m_2)h_3\]

![FIG-03-83-005: Outdoor and return-air streams mixing to supply state on a psychrometric chart.](../figures/FIG-03-83-005-mixing-of-moist-air-streams.png)

### Worked Example 5

**Problem.** Equal dry-air mass flows mix to a state midway along the connecting line under the ideal model.

**Solution.** Apply the relation and model in §83.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 83.6 Building sensible and latent loads

HVAC equipment is selected from heating/cooling loads, not only indoor setpoint. Envelope conduction, solar gains, ventilation, occupants, equipment, and infiltration contribute.

\[\dot Q_{load}=\dot Q_{envelope}+\dot Q_{solar}+\dot Q_{people}+\dot Q_{equipment}+\dot Q_{vent}\]

![FIG-03-83-006: Building load diagram splitting envelope, solar, people, equipment, ventilation, and infiltration loads.](../figures/FIG-03-83-006-building-sensible-and-latent-loads.png)

### Worked Example 6

**Problem.** Increasing outdoor-air ventilation can increase both sensible and latent cooling load.

**Solution.** Apply the relation and model in §83.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 83.7 COP, equipment capacity, and HVAC performance

Equipment performance connects thermal capacity to input power. Operating conditions, part load, and heat-exchanger temperatures affect real COP.

\[\mathrm{COP_R}=\frac{Q_L}{W_{in}},\qquad \mathrm{COP_{HP}}=\frac{Q_H}{W_{in}}\]

![FIG-03-83-007: Refrigeration/heat-pump system with evaporator, compressor, condenser, expansion device, loads, and COP definitions.](../figures/FIG-03-83-007-cop-equipment-capacity-and-hvac-performance.png)

### Worked Example 7

**Problem.** A refrigerator removing 30 kW with 10 kW input has COPR=3.

**Solution.** Apply the relation and model in §83.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. Select the correct model or failure/operating region and solve again. Algebra does not override geometry, material behavior, or component-state validity.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** Use the Handbook expression and its definitions unless the problem explicitly provides another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 11; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** The Mechanical specification includes both directly tabulated Handbook equations and learned design concepts. This chapter does not assign invented Handbook pages to specification-required material that is not directly tabulated.

---

## Where This Goes Wrong

**Using psychrometric state outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using sensible HVAC process outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using cooling and dehumidification outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using humidification process outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using air mixing outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using HVAC load outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using HVAC coefficient of performance outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| psychrometric state | Concept developed in §83.1; apply with that section's geometry and operating assumptions. |
| sensible HVAC process | Concept developed in §83.2; apply with that section's geometry and operating assumptions. |
| cooling and dehumidification | Concept developed in §83.3; apply with that section's geometry and operating assumptions. |
| humidification process | Concept developed in §83.4; apply with that section's geometry and operating assumptions. |
| air mixing | Concept developed in §83.5; apply with that section's geometry and operating assumptions. |
| HVAC load | Concept developed in §83.6; apply with that section's geometry and operating assumptions. |
| HVAC coefficient of performance | Concept developed in §83.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **psychrometric state** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **sensible HVAC process** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **cooling and dehumidification** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **humidification process** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **air mixing** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **HVAC load** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **HVAC coefficient of performance** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **psychrometric state**?

9. What geometric, material, operating, or model assumption must be checked before applying **sensible HVAC process**?

10. What geometric, material, operating, or model assumption must be checked before applying **cooling and dehumidification**?

11. What geometric, material, operating, or model assumption must be checked before applying **humidification process**?

12. What geometric, material, operating, or model assumption must be checked before applying **air mixing**?

13. What geometric, material, operating, or model assumption must be checked before applying **HVAC load**?

14. What geometric, material, operating, or model assumption must be checked before applying **HVAC coefficient of performance**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **psychrometric state**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **sensible HVAC process**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **cooling and dehumidification**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **humidification process**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **air mixing**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **HVAC load**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **HVAC coefficient of performance**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **psychrometric state**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **sensible HVAC process**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **psychrometric state** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **sensible HVAC process** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **cooling and dehumidification** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **humidification process** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **air mixing** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **HVAC load** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **HVAC coefficient of performance** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **psychrometric state**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **sensible HVAC process**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **cooling and dehumidification**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **humidification process**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **air mixing**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **HVAC load**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **HVAC coefficient of performance**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

15. The sketch exposes supports, force directions, geometry, constraints, energy/flow paths, and missing load cases before algebra obscures them.

16. Mechanical equations are model-dependent. The result must remain compatible with yielding/buckling/fatigue, flow regime, thermal state, contact, or kinematic constraints.

17. The Handbook is the supplied exam reference; its definitions, correction factors, unit conventions, and tables should govern unless the problem explicitly supplies another relation.

18. These checks catch impossible motion, unit errors, invalid thin-wall or linear assumptions, unrealistic stresses, interference, and parts that cannot be manufactured or assembled.

19. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

20. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

21. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

22. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

23. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

24. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

25. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

26. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

27. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.


---

## Practice Problems

1. At a fixed pressure and humidity ratio, heating air lowers relative humidity.

2. Heating 1 kg/s of air by 10 K requires about 10 kW per kJ/(kg·K) of cp.

3. A dehumidifying coil reduces both enthalpy and humidity ratio.

4. If humidity ratio rises by 0.004 kg/kg for 2 kg/s dry air, water addition is 0.008 kg/s.

5. Equal dry-air mass flows mix to a state midway along the connecting line under the ideal model.

6. Increasing outdoor-air ventilation can increase both sensible and latent cooling load.

7. A refrigerator removing 30 kW with 10 kW input has COPR=3.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. Use §83.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §83.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §83.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §83.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §83.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §83.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §83.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 11, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 11.

- **psychrometric state:** Dry-bulb, wet-bulb, humidity ratio, and relative humidity
- **sensible HVAC process:** Sensible heating and cooling
- **cooling and dehumidification:** Cooling and dehumidification
- **humidification process:** Humidification and evaporative cooling
- **air mixing:** Mixing of moist-air streams
- **HVAC load:** Building sensible and latent loads
- **HVAC coefficient of performance:** COP, equipment capacity, and HVAC performance

---

## What's Next

**Chapter 03-84: Mechanical Springs**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
