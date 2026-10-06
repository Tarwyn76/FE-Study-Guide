---
chapter: "02-54"
title: "Refrigeration and Heat Pumps"
layer: 2
tier: D
template: technical
ledger_ids: [THERMO-2D-054-01, THERMO-2D-054-02, THERMO-2D-054-03, THERMO-2D-054-04, THERMO-2D-054-05, THERMO-2D-054-06, THERMO-2D-054-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-54: Refrigeration and Heat Pumps

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-52 Second Law · 02-48 Refrigerant Properties

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines refrigerator and heat-pump COP, Carnot COP limits, ton of refrigeration, and provides refrigeration cycles, refrigerant property diagrams/tables, and psychrometric charts.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **54.1** Explain and apply **Refrigeration and Heat-Pump Objectives**.
* **54.2** Explain and apply **Carnot COP Limits**.
* **54.3** Explain and apply **Vapor-Compression Refrigeration Cycle**.
* **54.4** Explain and apply **Refrigeration COP from Enthalpies**.
* **54.5** Explain and apply **Refrigeration Capacity and Tons**.
* **54.6** Explain and apply **Heat Pumps and Heating COP**.
* **54.7** Explain and apply **Real-System Considerations**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 54.1 Refrigeration and Heat-Pump Objectives

A refrigerator removes heat \(Q_L\) from a low-temperature region using work input. A heat pump is judged by heat delivered \(Q_H\) to the high-temperature region.

The same device can be described by different COPs depending on desired effect.

\[COP_R=\frac{Q_L}{W_{in}},\qquad COP_{HP}=\frac{Q_H}{W_{in}}=COP_R+1\]

![FIG-02-54-001: Refrigerator/heat-pump diagram between cold and warm reservoirs with QL, QH, and work.](../figures/FIG-02-54-001-refrigeration-and-heat-pump-objectives.png)

### Worked Example 1

**Problem.** A refrigerator removes 10 kW and requires 2 kW input. Find COPR.

**Solution.** 5.

---

## 54.2 Carnot COP Limits

The reversed Carnot cycle gives the maximum possible COP between two thermal reservoirs. Use absolute temperatures.

A smaller temperature lift generally permits higher COP.

\[COP_{R,C}=\frac{T_L}{T_H-T_L},\qquad COP_{HP,C}=\frac{T_H}{T_H-T_L}\]

![FIG-02-54-002: COP versus temperature-lift concept with hot/cold absolute temperatures.](../figures/FIG-02-54-002-carnot-cop-limits.png)

### Worked Example 2

**Problem.** For Problem 1, find COPHP for same cycle.

**Solution.** 6.

---

## 54.3 Vapor-Compression Refrigeration Cycle

The basic vapor-compression cycle has four principal components: compressor, condenser, expansion valve, and evaporator.

Compression raises pressure and enthalpy, condensation rejects heat, throttling is approximately constant enthalpy, and evaporation absorbs heat.

\[1\to2:\text{compression},\ 2\to3:\text{condensation},\ 3\to4:h=\text{const},\ 4\to1:\text{evaporation}\]

![FIG-02-54-003: Vapor-compression components with state numbers and P-h cycle.](../figures/FIG-02-54-003-vapor-compression-refrigeration-cycle.png)

### Worked Example 3

**Problem.** Carnot refrigerator TL=270 K, TH=300 K. Find COPR.

**Solution.** COP=270/30=9.

---

## 54.4 Refrigeration COP from Enthalpies

For a simple steady vapor-compression refrigerator with negligible KE/PE changes, refrigeration effect is \(h_1-h_4\) and compressor work is \(h_2-h_1\).

Use actual compressor outlet enthalpy unless the compressor is explicitly ideal/isentropic.

\[COP_R=\frac{h_1-h_4}{h_2-h_1}\]

![FIG-02-54-004: P-h diagram with refrigeration effect and compressor work enthalpy differences.](../figures/FIG-02-54-004-refrigeration-cop-from-enthalpies.png)

### Worked Example 4

**Problem.** Vapor-compression: h1=400, h2=450, h4=250 kJ/kg. Find COPR.

**Solution.** (400-250)/(450-400)=3.

---

## 54.5 Refrigeration Capacity and Tons

The Handbook gives one ton of refrigeration as 12,000 Btu/hr or approximately 3.516 kW of cooling capacity.

Mass flow follows cooling load divided by refrigeration effect.

\[\dot Q_L=\dot m(h_1-h_4)\]

![FIG-02-54-005: Cooling load converted to refrigerant mass flow using enthalpy difference.](../figures/FIG-02-54-005-refrigeration-capacity-and-tons.png)

### Worked Example 5

**Problem.** Cooling load is 105.5 kW. Convert approximately to tons refrigeration.

**Solution.** 105.5/3.516≈30.0 tons.

---

## 54.6 Heat Pumps and Heating COP

A heat pump uses the same cycle but values heat rejected at the condenser. Because \(Q_H=Q_L+W\), heat-pump COP exceeds refrigerator COP by 1 for the same cycle.

COP can exceed 1 because it is not a heat-engine efficiency.

\[COP_{HP}=COP_R+1\]

![FIG-02-54-006: Heat pump moving heat from outdoor reservoir to indoor space with work input.](../figures/FIG-02-54-006-heat-pumps-and-heating-cop.png)

### Worked Example 6

**Problem.** For cycle h1=400, h4=250 kJ/kg and cooling load 30 kW, find refrigerant flow.

**Solution.** ṁ=30/150=0.20 kg/s.

---

## 54.7 Real-System Considerations

Superheat, subcooling, compressor efficiency, pressure drop, heat-exchanger approach temperatures, and refrigerant selection affect actual performance.

Use property data and the cycle state points given rather than assuming ideal saturated states at every component boundary.

\[\text{actual cycle}\ne\text{ideal reversed cycle}\]

![FIG-02-54-007: Ideal and actual vapor-compression cycles on P-h chart with superheat/subcooling and pressure drops.](../figures/FIG-02-54-007-real-system-considerations.png)

### Worked Example 7

**Problem.** What component is approximately constant enthalpy?

**Solution.** Expansion/throttling valve.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What component absorbs QL?

**Solution.** Evaporator.

### Worked Example 9

**Problem.** What component rejects QH?

**Solution.** Condenser.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Thermodynamics, printed pp. 149–150 and common-cycle diagrams pp. 176–180**.

**Source boundary:** The Handbook directly defines refrigerator and heat-pump COP, Carnot COP limits, ton of refrigeration, and provides refrigeration cycles, refrigerant property diagrams/tables, and psychrometric charts.

---

## Where This Goes Wrong

**Using coefficient of performance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Carnot COP outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using vapor-compression cycle outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using refrigeration COP outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using refrigeration capacity outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using heat pump outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using refrigeration system audit outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| coefficient of performance | Concept developed in §54.1; use the section definition and conditions. |
| Carnot COP | Concept developed in §54.2; use the section definition and conditions. |
| vapor-compression cycle | Concept developed in §54.3; use the section definition and conditions. |
| refrigeration COP | Concept developed in §54.4; use the section definition and conditions. |
| refrigeration capacity | Concept developed in §54.5; use the section definition and conditions. |
| heat pump | Concept developed in §54.6; use the section definition and conditions. |
| refrigeration system audit | Concept developed in §54.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **coefficient of performance** and state the governing equation or modeling rule.

2. Define **Carnot COP** and state the governing equation or modeling rule.

3. Define **vapor-compression cycle** and state the governing equation or modeling rule.

4. Define **refrigeration COP** and state the governing equation or modeling rule.

5. Define **refrigeration capacity** and state the governing equation or modeling rule.

6. Define **heat pump** and state the governing equation or modeling rule.

7. Define **refrigeration system audit** and state the governing equation or modeling rule.

8. What is the most likely error if **coefficient of performance** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **Carnot COP** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **vapor-compression cycle** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **refrigeration COP** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **refrigeration capacity** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **heat pump** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **refrigeration system audit** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **coefficient of performance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **Carnot COP**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **vapor-compression cycle**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **refrigeration COP**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **refrigeration capacity**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **heat pump**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **refrigeration system audit**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **coefficient of performance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **Carnot COP**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **coefficient of performance** is developed in §54.1. Use the displayed relation together with that section's assumptions and units.

2. **Carnot COP** is developed in §54.2. Use the displayed relation together with that section's assumptions and units.

3. **vapor-compression cycle** is developed in §54.3. Use the displayed relation together with that section's assumptions and units.

4. **refrigeration COP** is developed in §54.4. Use the displayed relation together with that section's assumptions and units.

5. **refrigeration capacity** is developed in §54.5. Use the displayed relation together with that section's assumptions and units.

6. **heat pump** is developed in §54.6. Use the displayed relation together with that section's assumptions and units.

7. **refrigeration system audit** is developed in §54.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **coefficient of performance**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Carnot COP**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **vapor-compression cycle**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **refrigeration COP**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **refrigeration capacity**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **heat pump**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **refrigeration system audit**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **coefficient of performance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **Carnot COP** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **vapor-compression cycle** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **refrigeration COP** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **refrigeration capacity** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **heat pump** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **refrigeration system audit** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **coefficient of performance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **Carnot COP** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. A refrigerator removes 10 kW and requires 2 kW input. Find COPR.

2. For Problem 1, find COPHP for same cycle.

3. Carnot refrigerator TL=270 K, TH=300 K. Find COPR.

4. Vapor-compression: h1=400, h2=450, h4=250 kJ/kg. Find COPR.

5. Cooling load is 105.5 kW. Convert approximately to tons refrigeration.

6. For cycle h1=400, h4=250 kJ/kg and cooling load 30 kW, find refrigerant flow.

7. What component is approximately constant enthalpy?

8. What component absorbs QL?

9. What component rejects QH?

10. Why can COP exceed 1?


---

## Practice Problem Solutions

1. 5.

2. 6.

3. COP=270/30=9.

4. (400-250)/(450-400)=3.

5. 105.5/3.516≈30.0 tons.

6. ṁ=30/150=0.20 kg/s.

7. Expansion/throttling valve.

8. Evaporator.

9. Condenser.

10. COP compares transferred heat to work input; the device moves heat rather than converting work entirely to heat.


---

## Quick Reference

**Handbook anchor:** Thermodynamics, printed pp. 149–150 and common-cycle diagrams pp. 176–180.

- **coefficient of performance:** Refrigeration and Heat-Pump Objectives
- **Carnot COP:** Carnot COP Limits
- **vapor-compression cycle:** Vapor-Compression Refrigeration Cycle
- **refrigeration COP:** Refrigeration COP from Enthalpies
- **refrigeration capacity:** Refrigeration Capacity and Tons
- **heat pump:** Heat Pumps and Heating COP
- **refrigeration system audit:** Real-System Considerations
---

## What's Next

**02-55 — Conduction and Thermal Resistance**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor