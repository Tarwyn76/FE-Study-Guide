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

**Solution.** Humidity ratio \(\omega\) is unchanged by sensible heating when no water is added or removed. Raising dry-bulb temperature increases the saturation vapor pressure while \(P_v\) stays essentially fixed, so relative humidity **decreases**.

---

## 83.2 Sensible heating and cooling

Sensible processes change dry-bulb temperature without changing humidity ratio, absent condensation or humidification.

\[\dot Q_s=\dot m_a c_p(T_2-T_1)\]

![FIG-03-83-002: Horizontal sensible heating and cooling paths on a psychrometric chart.](../figures/FIG-03-83-002-sensible-heating-and-cooling.png)

### Worked Example 2

**Problem.** Heating 1 kg/s of air by 10 K requires about 10 kW per kJ/(kg·K) of cp.

**Solution.** \(\dot Q_s=\dot m_ac_p\Delta T=(1\ {\rm kg/s})(1\ {\rm kJ/(kg\cdot K)})(10\ {\rm K})=\mathbf{10\ kW}\).

---

## 83.3 Cooling and dehumidification

Cooling below dew point removes both sensible and latent heat and condenses water. Coil leaving conditions are limited by apparatus dew point and bypass behavior.

\[\dot Q=\dot m_a(h_1-h_2)\]

![FIG-03-83-003: Cooling coil with condensate drain and psychrometric path downward-left.](../figures/FIG-03-83-003-cooling-and-dehumidification.png)

### Worked Example 3

**Problem.** A dehumidifying coil reduces both enthalpy and humidity ratio.

**Solution.** A cooling/dehumidifying coil lowers moist-air enthalpy and, once the air is cooled below its dew point, condenses water so humidity ratio also decreases. The total coil load is \(\dot m_a(h_1-h_2)\).

---

## 83.4 Humidification and evaporative cooling

Humidification adds moisture. Adiabatic evaporative humidification can lower dry-bulb temperature while increasing humidity ratio.

\[\dot m_w=\dot m_a(\omega_2-\omega_1)\]

![FIG-03-83-004: Humidifier/evaporative cooler with psychrometric path and water mass balance.](../figures/FIG-03-83-004-humidification-and-evaporative-cooling.png)

### Worked Example 4

**Problem.** If humidity ratio rises by 0.004 kg/kg for 2 kg/s dry air, water addition is 0.008 kg/s.

**Solution.** \(\dot m_w=\dot m_a(\omega_2-\omega_1)=(2\ {\rm kg_{da}/s})(0.004\ {\rm kg_w/kg_{da}})=\mathbf{0.008\ kg_w/s}\).

---

## 83.5 Mixing of moist-air streams

Two air streams mix to an intermediate state governed by mass and energy balances. On a psychrometric chart, the mixture lies on the straight line between the entering states.

\[\dot m_1 h_1+\dot m_2 h_2=(\dot m_1+\dot m_2)h_3\]

![FIG-03-83-005: Outdoor and return-air streams mixing to supply state on a psychrometric chart.](../figures/FIG-03-83-005-mixing-of-moist-air-streams.png)

### Worked Example 5

**Problem.** Equal dry-air mass flows mix to a state midway along the connecting line under the ideal model.

**Solution.** For equal dry-air mass flow rates, conservation of dry air and enthalpy gives \(h_3=(h_1+h_2)/2\) and similarly \(\omega_3=(\omega_1+\omega_2)/2\). The mixed state lies midway along the straight connecting line on the psychrometric chart under the ideal model.

---

## 83.6 Building sensible and latent loads

HVAC equipment is selected from heating/cooling loads, not only indoor setpoint. Envelope conduction, solar gains, ventilation, occupants, equipment, and infiltration contribute.

\[\dot Q_{load}=\dot Q_{envelope}+\dot Q_{solar}+\dot Q_{people}+\dot Q_{equipment}+\dot Q_{vent}\]

![FIG-03-83-006: Building load diagram splitting envelope, solar, people, equipment, ventilation, and infiltration loads.](../figures/FIG-03-83-006-building-sensible-and-latent-loads.png)

### Worked Example 6

**Problem.** Increasing outdoor-air ventilation can increase both sensible and latent cooling load.

**Solution.** Outdoor ventilation introduces both temperature difference and moisture difference. Increasing outside-air flow can therefore increase sensible load and latent load simultaneously when outdoor air is hotter and more humid than the conditioned space.

---

## 83.7 COP, equipment capacity, and HVAC performance

Equipment performance connects thermal capacity to input power. Operating conditions, part load, and heat-exchanger temperatures affect real COP.

\[\mathrm{COP_R}=\frac{Q_L}{W_{in}},\qquad \mathrm{COP_{HP}}=\frac{Q_H}{W_{in}}\]

![FIG-03-83-007: Refrigeration/heat-pump system with evaporator, compressor, condenser, expansion device, loads, and COP definitions.](../figures/FIG-03-83-007-cop-equipment-capacity-and-hvac-performance.png)

### Worked Example 7

**Problem.** A refrigerator removing 30 kW with 10 kW input has COPR=3.

**Solution.** \(\mathrm{COP_R}=Q_L/W_{in}=30/10=\mathbf{3.0}\). This means the refrigerator removes three units of heat from the cooled space per unit of input work under the stated operating condition.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. A psychrometric state must satisfy pressure, saturation, humidity-ratio, and energy constraints. A result above saturation without condensation or with inconsistent dry-air basis must be corrected.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **HVAC Processes, Loads, Psychrometrics, and Equipment Performance**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **ASHRAE** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 11; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- ASHRAE. (2025). *2025 ASHRAE Handbook—Fundamentals*, SI edition. ISBN 978-1-964173-11-5. Supporting scope: Psychrometrics, thermodynamics, heat transfer, load calculations, HVAC&R fundamentals, duct/piping design, and building environmental calculations.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **HVAC Processes, Loads, Psychrometrics, and Equipment Performance**, start from the physical model and system/component state, not from an isolated formula. A valid solution must use dry-air basis consistently, verify the state lies physically on/below saturation, close moist-air mass/enthalpy balances, and distinguish sensible, latent, and total load.

16. Units and sign/reference conventions are part of the model in **HVAC Processes, Loads, Psychrometrics, and Equipment Performance**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **HVAC Processes, Loads, Psychrometrics, and Equipment Performance**. External sources **ASHRAE** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: set water addition/removal to zero and confirm sensible heating keeps humidity ratio constant; set \(W_{in}=Q_L/3\) and confirm \(COP_R=3\). A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §83.1, **Dry-bulb, wet-bulb, humidity ratio, and relative humidity**, uses \(\omega=0.622\frac{P_v}{P-P_v}\). Apply it only under the geometry/material/operating assumptions stated in §83.1, then compare the result with the physical behavior described there.

20. **A.** Section §83.2, **Sensible heating and cooling**, uses \(\dot Q_s=\dot m_a c_p(T_2-T_1)\). Apply it only under the geometry/material/operating assumptions stated in §83.2, then compare the result with the physical behavior described there.

21. **A.** Section §83.3, **Cooling and dehumidification**, uses \(\dot Q=\dot m_a(h_1-h_2)\). Apply it only under the geometry/material/operating assumptions stated in §83.3, then compare the result with the physical behavior described there.

22. **A.** Section §83.4, **Humidification and evaporative cooling**, uses \(\dot m_w=\dot m_a(\omega_2-\omega_1)\). Apply it only under the geometry/material/operating assumptions stated in §83.4, then compare the result with the physical behavior described there.

23. **A.** Section §83.5, **Mixing of moist-air streams**, uses \(\dot m_1 h_1+\dot m_2 h_2=(\dot m_1+\dot m_2)h_3\). Apply it only under the geometry/material/operating assumptions stated in §83.5, then compare the result with the physical behavior described there.

24. **A.** Section §83.6, **Building sensible and latent loads**, uses \(\dot Q_{load}=\dot Q_{envelope}+\dot Q_{solar}+\dot Q_{people}+\dot Q_{equipment}+\dot Q_{vent}\). Apply it only under the geometry/material/operating assumptions stated in §83.6, then compare the result with the physical behavior described there.

25. **A.** Section §83.7, **COP, equipment capacity, and HVAC performance**, uses \(\mathrm{COP_R}=\frac{Q_L}{W_{in}},\qquad \mathrm{COP_{HP}}=\frac{Q_H}{W_{in}}\). Apply it only under the geometry/material/operating assumptions stated in §83.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **HVAC Processes, Loads, Psychrometrics, and Equipment Performance** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **ASHRAE**; guide synthesis is supplemental explanation and exam-oriented workflow.


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

1. **Independent check for §83.1 — Dry-bulb, wet-bulb, humidity ratio, and relative humidity.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Humidity ratio \(\omega\) is unchanged by sensible heating when no water is added or removed. Raising dry-bulb temperature increases the saturation vapor pressure while \(P_v\) stays essentially fixed, so relative humidity **decreases**.

2. **Independent check for §83.2 — Sensible heating and cooling.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\dot Q_s=\dot m_ac_p\Delta T=(1\ {\rm kg/s})(1\ {\rm kJ/(kg\cdot K)})(10\ {\rm K})=\mathbf{10\ kW}\).

3. **Independent check for §83.3 — Cooling and dehumidification.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A cooling/dehumidifying coil lowers moist-air enthalpy and, once the air is cooled below its dew point, condenses water so humidity ratio also decreases. The total coil load is \(\dot m_a(h_1-h_2)\).

4. **Independent check for §83.4 — Humidification and evaporative cooling.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\dot m_w=\dot m_a(\omega_2-\omega_1)=(2\ {\rm kg_{da}/s})(0.004\ {\rm kg_w/kg_{da}})=\mathbf{0.008\ kg_w/s}\).

5. **Independent check for §83.5 — Mixing of moist-air streams.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For equal dry-air mass flow rates, conservation of dry air and enthalpy gives \(h_3=(h_1+h_2)/2\) and similarly \(\omega_3=(\omega_1+\omega_2)/2\). The mixed state lies midway along the straight connecting line on the psychrometric chart under the ideal model.

6. **Independent check for §83.6 — Building sensible and latent loads.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Outdoor ventilation introduces both temperature difference and moisture difference. Increasing outside-air flow can therefore increase sensible load and latent load simultaneously when outdoor air is hotter and more humid than the conditioned space.

7. **Independent check for §83.7 — COP, equipment capacity, and HVAC performance.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\mathrm{COP_R}=Q_L/W_{in}=30/10=\mathbf{3.0}\). This means the refrigerator removes three units of heat from the cooled space per unit of input work under the stated operating condition.

8. For **HVAC Processes, Loads, Psychrometrics, and Equipment Performance**, one required acceptance screen is: use dry-air basis consistently, verify the state lies physically on/below saturation, close moist-air mass/enthalpy balances, and distinguish sensible, latent, and total load. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **HVAC Processes, Loads, Psychrometrics, and Equipment Performance**. For `split_required` concepts, use **ASHRAE** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: set water addition/removal to zero and confirm sensible heating keeps humidity ratio constant; set \(W_{in}=Q_L/3\) and confirm \(COP_R=3\). If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

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
