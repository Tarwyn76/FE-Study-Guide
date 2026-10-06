---
chapter: "02-49"
title: "Ideal Gases, Gas Mixtures, and Psychrometrics"
layer: 2
tier: D
template: technical
ledger_ids: [THERMO-2D-049-01, THERMO-2D-049-02, THERMO-2D-049-03, THERMO-2D-049-04, THERMO-2D-049-05, THERMO-2D-049-06, THERMO-2D-049-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-49: Ideal Gases, Gas Mixtures, and Psychrometrics

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-47 Thermodynamic Properties · 02-48 Property Tables

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly supplies ideal-gas equations, specific-heat/entropy relations, ideal-gas mixture formulas, real-gas compressibility discussion, and psychrometric definitions.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **49.1** Explain and apply **Ideal-Gas Equation of State**.
* **49.2** Explain and apply **Specific Heats and Ideal-Gas Property Changes**.
* **49.3** Explain and apply **Isentropic Ideal-Gas Relations**.
* **49.4** Explain and apply **Ideal-Gas Mixtures**.
* **49.5** Explain and apply **Real-Gas Correction with Compressibility Factor**.
* **49.6** Explain and apply **Humidity Ratio, Relative Humidity, and Dew Point**.
* **49.7** Explain and apply **Common Psychrometric Processes**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 49.1 Ideal-Gas Equation of State

For an ideal gas, \(Pv=RT\) or \(PV=mRT\), using absolute pressure and absolute temperature.

The specific gas constant is \(R=ar R/M\), where \(M\) is molar mass.

\[Pv=RT,\qquad PV=mRT,\qquad R=\frac{\bar R}{M}\]

![FIG-02-49-001: Ideal-gas state box linking pressure, volume, mass, gas constant, and absolute temperature.](../figures/FIG-02-49-001-ideal-gas-equation-of-state.png)

### Worked Example 1

**Problem.** Air: m=2 kg, R=0.287 kJ/kg·K, T=300 K, V=1 m³. Find pressure.

**Solution.** P=mRT/V=172.2 kPa.

---

## 49.2 Specific Heats and Ideal-Gas Property Changes

For ideal gases with constant specific heats, \(\Delta u=c_v\Delta T\) and \(\Delta h=c_p\Delta T\), with \(c_p-c_v=R\).

The ratio \(k=c_p/c_v\) appears in isentropic relations.

\[\Delta u=c_v\Delta T,\quad\Delta h=c_p\Delta T,\quad c_p-c_v=R\]

![FIG-02-49-002: Ideal-gas energy changes tied to temperature and cp/cv.](../figures/FIG-02-49-002-specific-heats-and-ideal-gas-property-changes.png)

### Worked Example 2

**Problem.** Ideal gas cp=1.005 and cv=0.718 kJ/kg·K. Find R and k.

**Solution.** R=0.287 kJ/kg·K; k=1.400.

---

## 49.3 Isentropic Ideal-Gas Relations

For constant-specific-heat ideal gases undergoing an isentropic process, pressure, temperature, and specific volume obey power-law relations.

These relations require both ideal-gas behavior and an isentropic process.

\[\frac{T_2}{T_1}=\left(\frac{P_2}{P_1}\right)^{(k-1)/k}\]

![FIG-02-49-003: Ideal-gas isentropic compression/expansion on P-v and T-s plots.](../figures/FIG-02-49-003-isentropic-ideal-gas-relations.png)

### Worked Example 3

**Problem.** Ideal gas at constant cv=0.718 warms 50 K. Find Δu.

**Solution.** 35.9 kJ/kg.

---

## 49.4 Ideal-Gas Mixtures

Mixtures use mole fraction \(x_i\) and mass fraction \(y_i\). Dalton's law gives total pressure as the sum of partial pressures; for ideal gases, \(x_i=P_i/P\).

Mixture molecular weight is mole-fraction weighted.

\[x_i=\frac{N_i}{N},\quad y_i=\frac{m_i}{m},\quad P=\sum P_i,\quad M=\sum x_iM_i\]

![FIG-02-49-004: Gas mixture with component mole fractions and partial pressures adding to total pressure.](../figures/FIG-02-49-004-ideal-gas-mixtures.png)

### Worked Example 4

**Problem.** Mixture x1=0.3 with M1=28, x2=0.7 with M2=44 kg/kmol. Find mixture M.

**Solution.** M=39.2 kg/kmol.

---

## 49.5 Real-Gas Correction with Compressibility Factor

The Handbook discusses real-gas deviation and compressibility factor \(Z\). The ideal-gas equation is modified to \(Pv=ZRT\).

When \(Zpprox1\), ideal-gas behavior is a good approximation.

\[Pv=ZRT\]

![FIG-02-49-005: Conceptual compressibility-factor chart versus reduced pressure/temperature.](../figures/FIG-02-49-005-real-gas-correction-with-compressibility-factor.png)

### Worked Example 5

**Problem.** At total P=100 kPa and water-vapor partial pressure 2 kPa, find humidity ratio.

**Solution.** ω=0.622(2)/(98)=0.01269 kg/kg dry air.

---

## 49.6 Humidity Ratio, Relative Humidity, and Dew Point

For moist air modeled as an ideal mixture, humidity ratio relates vapor and dry-air mass. Relative humidity compares water-vapor partial pressure with saturation pressure at the same dry-bulb temperature.

Dew point is the saturation temperature corresponding to the existing vapor partial pressure.

\[\omega=0.622\frac{P_v}{P-P_v},\qquad \phi=\frac{P_v}{P_g(T)}\]

![FIG-02-49-006: Psychrometric-chart segment labeling dry bulb, humidity ratio, relative humidity, wet bulb, and dew point.](../figures/FIG-02-49-006-humidity-ratio-relative-humidity-and-dew-point.png)

### Worked Example 6

**Problem.** If saturation pressure at T is 4 kPa, find RH for Pv=2 kPa.

**Solution.** φ=0.50=50%.

---

## 49.7 Common Psychrometric Processes

Sensible heating/cooling changes dry-bulb temperature with approximately constant humidity ratio if no condensation or humidification occurs. Cooling below dew point causes condensation and reduces humidity ratio.

Humidification, evaporative cooling, and mixing processes are read from the psychrometric chart using mass and energy balances.

\[\dot m_a\omega_1+\dot m_w=\dot m_a\omega_2\]

![FIG-02-49-007: Psychrometric chart with sensible heating, cooling/dehumidification, and humidification paths.](../figures/FIG-02-49-007-common-psychrometric-processes.png)

### Worked Example 7

**Problem.** What is dew point?

**Solution.** Saturation temperature corresponding to the current water-vapor partial pressure.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What does Z=1 mean?

**Solution.** Ideal-gas behavior.

### Worked Example 9

**Problem.** What is Dalton's law?

**Solution.** Total pressure equals sum of component partial pressures.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Thermodynamics, printed pp. 144–150 and psychrometric charts pp. 179–180**.

**Source boundary:** The Handbook directly supplies ideal-gas equations, specific-heat/entropy relations, ideal-gas mixture formulas, real-gas compressibility discussion, and psychrometric definitions.

---

## Where This Goes Wrong

**Using ideal gas outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using ideal-gas specific heat outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using isentropic ideal gas outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using ideal-gas mixture outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using compressibility factor outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using psychrometric humidity outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using psychrometric process outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| ideal gas | Concept developed in §49.1; use the section definition and conditions. |
| ideal-gas specific heat | Concept developed in §49.2; use the section definition and conditions. |
| isentropic ideal gas | Concept developed in §49.3; use the section definition and conditions. |
| ideal-gas mixture | Concept developed in §49.4; use the section definition and conditions. |
| compressibility factor | Concept developed in §49.5; use the section definition and conditions. |
| psychrometric humidity | Concept developed in §49.6; use the section definition and conditions. |
| psychrometric process | Concept developed in §49.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **ideal gas** and state the governing equation or modeling rule.

2. Define **ideal-gas specific heat** and state the governing equation or modeling rule.

3. Define **isentropic ideal gas** and state the governing equation or modeling rule.

4. Define **ideal-gas mixture** and state the governing equation or modeling rule.

5. Define **compressibility factor** and state the governing equation or modeling rule.

6. Define **psychrometric humidity** and state the governing equation or modeling rule.

7. Define **psychrometric process** and state the governing equation or modeling rule.

8. What is the most likely error if **ideal gas** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **ideal-gas specific heat** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **isentropic ideal gas** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **ideal-gas mixture** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **compressibility factor** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **psychrometric humidity** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **psychrometric process** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **ideal gas**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **ideal-gas specific heat**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **isentropic ideal gas**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **ideal-gas mixture**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **compressibility factor**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **psychrometric humidity**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **psychrometric process**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **ideal gas**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **ideal-gas specific heat**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **ideal gas** is developed in §49.1. Use the displayed relation together with that section's assumptions and units.

2. **ideal-gas specific heat** is developed in §49.2. Use the displayed relation together with that section's assumptions and units.

3. **isentropic ideal gas** is developed in §49.3. Use the displayed relation together with that section's assumptions and units.

4. **ideal-gas mixture** is developed in §49.4. Use the displayed relation together with that section's assumptions and units.

5. **compressibility factor** is developed in §49.5. Use the displayed relation together with that section's assumptions and units.

6. **psychrometric humidity** is developed in §49.6. Use the displayed relation together with that section's assumptions and units.

7. **psychrometric process** is developed in §49.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **ideal gas**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **ideal-gas specific heat**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **isentropic ideal gas**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **ideal-gas mixture**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **compressibility factor**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **psychrometric humidity**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **psychrometric process**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **ideal gas** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **ideal-gas specific heat** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **isentropic ideal gas** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **ideal-gas mixture** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **compressibility factor** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **psychrometric humidity** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **psychrometric process** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **ideal gas** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **ideal-gas specific heat** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Air: m=2 kg, R=0.287 kJ/kg·K, T=300 K, V=1 m³. Find pressure.

2. Ideal gas cp=1.005 and cv=0.718 kJ/kg·K. Find R and k.

3. Ideal gas at constant cv=0.718 warms 50 K. Find Δu.

4. Mixture x1=0.3 with M1=28, x2=0.7 with M2=44 kg/kmol. Find mixture M.

5. At total P=100 kPa and water-vapor partial pressure 2 kPa, find humidity ratio.

6. If saturation pressure at T is 4 kPa, find RH for Pv=2 kPa.

7. What is dew point?

8. What does Z=1 mean?

9. What is Dalton's law?

10. During sensible heating with no moisture addition/removal, what happens to humidity ratio?


---

## Practice Problem Solutions

1. P=mRT/V=172.2 kPa.

2. R=0.287 kJ/kg·K; k=1.400.

3. 35.9 kJ/kg.

4. M=39.2 kg/kmol.

5. ω=0.622(2)/(98)=0.01269 kg/kg dry air.

6. φ=0.50=50%.

7. Saturation temperature corresponding to the current water-vapor partial pressure.

8. Ideal-gas behavior.

9. Total pressure equals sum of component partial pressures.

10. Approximately constant.


---

## Quick Reference

**Handbook anchor:** Thermodynamics, printed pp. 144–150 and psychrometric charts pp. 179–180.

- **ideal gas:** Ideal-Gas Equation of State
- **ideal-gas specific heat:** Specific Heats and Ideal-Gas Property Changes
- **isentropic ideal gas:** Isentropic Ideal-Gas Relations
- **ideal-gas mixture:** Ideal-Gas Mixtures
- **compressibility factor:** Real-Gas Correction with Compressibility Factor
- **psychrometric humidity:** Humidity Ratio, Relative Humidity, and Dew Point
- **psychrometric process:** Common Psychrometric Processes
---

## What's Next

**02-50 — First Law — Closed Systems**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor