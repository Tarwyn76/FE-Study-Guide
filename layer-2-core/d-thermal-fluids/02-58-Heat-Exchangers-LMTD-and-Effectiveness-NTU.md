---
chapter: "02-58"
title: "Heat Exchangers — LMTD and Effectiveness-NTU"
layer: 2
tier: D
template: technical
ledger_ids: [HT-2D-058-01, HT-2D-058-02, HT-2D-058-03, HT-2D-058-04, HT-2D-058-05, HT-2D-058-06, HT-2D-058-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-58: Heat Exchangers — LMTD and Effectiveness-NTU

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-51 Control-Volume First Law · 02-55 Thermal Resistance · 02-57 Convection

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly supplies heat-exchanger stream balances, LMTD relations, correction factor concept, effectiveness, capacity rates, NTU, common effectiveness-NTU relations, and overall heat-transfer coefficient including wall and fouling resistances.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **58.1** Explain and apply **Heat-Exchanger Energy Balance**.
* **58.2** Explain and apply **Parallel-Flow and Counterflow Temperature Profiles**.
* **58.3** Explain and apply **Log-Mean Temperature Difference**.
* **58.4** Explain and apply **Overall Heat-Transfer Coefficient**.
* **58.5** Explain and apply **Correction Factor for Multipass/Crossflow Exchangers**.
* **58.6** Explain and apply **Effectiveness and Maximum Possible Heat Transfer**.
* **58.7** Explain and apply **NTU Method and Method Selection**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 58.1 Heat-Exchanger Energy Balance

For an adiabatic heat exchanger with no work and negligible KE/PE changes, heat lost by the hot stream equals heat gained by the cold stream.

For constant \(c_p\), define capacity rate \(C=\dot m c_p\).

\[\dot Q=C_H(T_{Hi}-T_{Ho})=C_C(T_{Co}-T_{Ci})\]

![FIG-02-58-001: Two-stream heat exchanger with inlet/outlet temperatures and equal heat transfer.](../figures/FIG-02-58-001-heat-exchanger-energy-balance.png)

### Worked Example 1

**Problem.** Hot stream C=4 kW/K cools 120→80°C. Find heat transfer.

**Solution.** Q=4(40)=160 kW.

---

## 58.2 Parallel-Flow and Counterflow Temperature Profiles

In parallel flow both streams enter the same end; in counterflow they enter opposite ends. Counterflow usually maintains a larger average temperature difference and can permit cold-outlet temperature to exceed hot-outlet temperature.

Temperature profiles must not cross in an ideal sensible-only exchanger model without phase change or additional effects.

\[\Delta T(x)=T_H(x)-T_C(x)\]

![FIG-02-58-002: Parallel-flow and counterflow temperature profiles along exchanger length.](../figures/FIG-02-58-002-parallel-flow-and-counterflow-temperature-profiles.png)

### Worked Example 2

**Problem.** If cold stream capacity rate is 2 kW/K and receives 160 kW starting at 20°C, find outlet temperature.

**Solution.** Tco=20+160/2=100°C.

---

## 58.3 Log-Mean Temperature Difference

When terminal temperatures are known, the LMTD method represents the correct logarithmic average driving temperature difference for simple parallel or counterflow arrangements.

Use the appropriate terminal differences for the selected arrangement.

\[\Delta T_{lm}=\frac{\Delta T_1-\Delta T_2}{\ln(\Delta T_1/\Delta T_2)}\]

![FIG-02-58-003: Terminal temperature differences on a counterflow exchanger and logarithmic mean construction.](../figures/FIG-02-58-003-log-mean-temperature-difference.png)

### Worked Example 3

**Problem.** Counterflow terminal differences are 20 K and 40 K. Find LMTD.

**Solution.** ΔTlm=(40-20)/ln(40/20)=28.85 K.

---

## 58.4 Overall Heat-Transfer Coefficient

The overall coefficient \(U\) combines inside convection, wall conduction, outside convection, and fouling resistances on a chosen reference area.

The area basis must match the definition of \(U\).

\[\dot Q=UA F\Delta T_{lm}\]

![FIG-02-58-004: Tube wall with inside/outside convection, wall conduction, fouling layers, and equivalent UA resistance.](../figures/FIG-02-58-004-overall-heat-transfer-coefficient.png)

### Worked Example 4

**Problem.** If U=500 W/m²K, A=10 m², F=1, ΔTlm=30 K, find heat rate.

**Solution.** Q=150 kW.

---

## 58.5 Correction Factor for Multipass/Crossflow Exchangers

For shell-and-tube multipass or crossflow configurations, the Handbook introduces correction factor \(F\) multiplying the counterflow LMTD reference.

Use the supplied chart/data for \(F\); do not assume \(F=1\) for a complex arrangement unless justified.

\[\dot Q=UA\,F\Delta T_{lm}\]

![FIG-02-58-005: Multipass shell-and-tube exchanger with correction factor applied to reference LMTD.](../figures/FIG-02-58-005-correction-factor-for-multipass-crossflow-exchangers.png)

### Worked Example 5

**Problem.** CH=5 kW/K, CC=3 kW/K, THi=120°C, TCi=20°C. Find Qmax.

**Solution.** Cmin=3; Qmax=300 kW.

---

## 58.6 Effectiveness and Maximum Possible Heat Transfer

Effectiveness is actual heat transfer divided by the maximum possible heat transfer. The maximum is based on the smaller capacity rate and the inlet temperature difference.

This method is useful when outlet temperatures are unknown.

\[\varepsilon=\frac{\dot Q}{\dot Q_{\max}},\qquad \dot Q_{\max}=C_{\min}(T_{Hi}-T_{Ci})\]

![FIG-02-58-006: Cmin/Cmax streams and actual versus maximum possible heat transfer.](../figures/FIG-02-58-006-effectiveness-and-maximum-possible-heat-transfer.png)

### Worked Example 6

**Problem.** If actual Q=180 kW in Problem 5, find effectiveness.

**Solution.** ε=0.60.

---

## 58.7 NTU Method and Method Selection

Number of transfer units is \(NTU=UA/C_{\min}\), and capacity ratio is \(C_r=C_{\min}/C_{\max}\). The Handbook gives effectiveness-NTU relations for common configurations.

Use LMTD when all terminal temperatures are known or easily obtained; use \(arepsilon\)-NTU when outlet temperatures are unknown and \(UA\) is known.

\[NTU=\frac{UA}{C_{\min}},\qquad C_r=\frac{C_{\min}}{C_{\max}}\]

![FIG-02-58-007: Decision tree selecting LMTD or effectiveness-NTU and showing NTU/Cr inputs.](../figures/FIG-02-58-007-ntu-method-and-method-selection.png)

### Worked Example 7

**Problem.** If UA=6 kW/K and Cmin=3 kW/K, find NTU.

**Solution.** NTU=2.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Find capacity ratio for Cmin=3, Cmax=5.

**Solution.** Cr=0.60.

### Worked Example 9

**Problem.** When is LMTD usually convenient?

**Solution.** When terminal temperatures are known or can be found.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Heat Transfer, printed pp. 220–222**.

**Source boundary:** The Handbook directly supplies heat-exchanger stream balances, LMTD relations, correction factor concept, effectiveness, capacity rates, NTU, common effectiveness-NTU relations, and overall heat-transfer coefficient including wall and fouling resistances.

---

## Where This Goes Wrong

**Using heat-exchanger energy balance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using heat-exchanger flow arrangement outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using log-mean temperature difference outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using overall heat-transfer coefficient outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using LMTD correction factor outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using heat-exchanger effectiveness outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using effectiveness-NTU method outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| heat-exchanger energy balance | Concept developed in §58.1; use the section definition and conditions. |
| heat-exchanger flow arrangement | Concept developed in §58.2; use the section definition and conditions. |
| log-mean temperature difference | Concept developed in §58.3; use the section definition and conditions. |
| overall heat-transfer coefficient | Concept developed in §58.4; use the section definition and conditions. |
| LMTD correction factor | Concept developed in §58.5; use the section definition and conditions. |
| heat-exchanger effectiveness | Concept developed in §58.6; use the section definition and conditions. |
| effectiveness-NTU method | Concept developed in §58.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **heat-exchanger energy balance** and state the governing equation or modeling rule.

2. Define **heat-exchanger flow arrangement** and state the governing equation or modeling rule.

3. Define **log-mean temperature difference** and state the governing equation or modeling rule.

4. Define **overall heat-transfer coefficient** and state the governing equation or modeling rule.

5. Define **LMTD correction factor** and state the governing equation or modeling rule.

6. Define **heat-exchanger effectiveness** and state the governing equation or modeling rule.

7. Define **effectiveness-NTU method** and state the governing equation or modeling rule.

8. What is the most likely error if **heat-exchanger energy balance** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **heat-exchanger flow arrangement** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **log-mean temperature difference** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **overall heat-transfer coefficient** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **LMTD correction factor** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **heat-exchanger effectiveness** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **effectiveness-NTU method** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **heat-exchanger energy balance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **heat-exchanger flow arrangement**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **log-mean temperature difference**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **overall heat-transfer coefficient**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **LMTD correction factor**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **heat-exchanger effectiveness**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **effectiveness-NTU method**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **heat-exchanger energy balance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **heat-exchanger flow arrangement**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **heat-exchanger energy balance** is developed in §58.1. Use the displayed relation together with that section's assumptions and units.

2. **heat-exchanger flow arrangement** is developed in §58.2. Use the displayed relation together with that section's assumptions and units.

3. **log-mean temperature difference** is developed in §58.3. Use the displayed relation together with that section's assumptions and units.

4. **overall heat-transfer coefficient** is developed in §58.4. Use the displayed relation together with that section's assumptions and units.

5. **LMTD correction factor** is developed in §58.5. Use the displayed relation together with that section's assumptions and units.

6. **heat-exchanger effectiveness** is developed in §58.6. Use the displayed relation together with that section's assumptions and units.

7. **effectiveness-NTU method** is developed in §58.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **heat-exchanger energy balance**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **heat-exchanger flow arrangement**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **log-mean temperature difference**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **overall heat-transfer coefficient**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **LMTD correction factor**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **heat-exchanger effectiveness**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **effectiveness-NTU method**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **heat-exchanger energy balance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **heat-exchanger flow arrangement** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **log-mean temperature difference** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **overall heat-transfer coefficient** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **LMTD correction factor** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **heat-exchanger effectiveness** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **effectiveness-NTU method** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **heat-exchanger energy balance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **heat-exchanger flow arrangement** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Hot stream C=4 kW/K cools 120→80°C. Find heat transfer.

2. If cold stream capacity rate is 2 kW/K and receives 160 kW starting at 20°C, find outlet temperature.

3. Counterflow terminal differences are 20 K and 40 K. Find LMTD.

4. If U=500 W/m²K, A=10 m², F=1, ΔTlm=30 K, find heat rate.

5. CH=5 kW/K, CC=3 kW/K, THi=120°C, TCi=20°C. Find Qmax.

6. If actual Q=180 kW in Problem 5, find effectiveness.

7. If UA=6 kW/K and Cmin=3 kW/K, find NTU.

8. Find capacity ratio for Cmin=3, Cmax=5.

9. When is LMTD usually convenient?

10. When is ε-NTU usually convenient?


---

## Practice Problem Solutions

1. Q=4(40)=160 kW.

2. Tco=20+160/2=100°C.

3. ΔTlm=(40-20)/ln(40/20)=28.85 K.

4. Q=150 kW.

5. Cmin=3; Qmax=300 kW.

6. ε=0.60.

7. NTU=2.

8. Cr=0.60.

9. When terminal temperatures are known or can be found.

10. When outlet temperatures are unknown but UA and inlet conditions are known.


---

## Quick Reference

**Handbook anchor:** Heat Transfer, printed pp. 220–222.

- **heat-exchanger energy balance:** Heat-Exchanger Energy Balance
- **heat-exchanger flow arrangement:** Parallel-Flow and Counterflow Temperature Profiles
- **log-mean temperature difference:** Log-Mean Temperature Difference
- **overall heat-transfer coefficient:** Overall Heat-Transfer Coefficient
- **LMTD correction factor:** Correction Factor for Multipass/Crossflow Exchangers
- **heat-exchanger effectiveness:** Effectiveness and Maximum Possible Heat Transfer
- **effectiveness-NTU method:** NTU Method and Method Selection
---

## What's Next

**02-59 — Electrical Quantities, Ohm's Law, and DC Power**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor