---
chapter: "02-53"
title: "Power Cycles"
layer: 2
tier: D
template: technical
ledger_ids: [THERMO-2D-053-01, THERMO-2D-053-02, THERMO-2D-053-03, THERMO-2D-053-04, THERMO-2D-053-05, THERMO-2D-053-06, THERMO-2D-053-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-53: Power Cycles

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-50 Closed-System First Law · 02-51 Control Volumes · 02-52 Second Law

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives heat-engine efficiency, Carnot limit, and plotted/common relations for Carnot, Otto, Rankine, and Brayton-cycle material in the thermodynamics/mechanical sections. Detailed cycle-improvement discussion is guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **53.1** Explain and apply **Heat Engines and Thermal Efficiency**.
* **53.2** Explain and apply **Carnot Cycle and Maximum Efficiency**.
* **53.3** Explain and apply **Otto Cycle**.
* **53.4** Explain and apply **Brayton Cycle**.
* **53.5** Explain and apply **Rankine Cycle**.
* **53.6** Explain and apply **Cycle Component Efficiencies**.
* **53.7** Explain and apply **Cycle Improvement and Limits**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 53.1 Heat Engines and Thermal Efficiency

A heat engine receives heat \(Q_H\), rejects \(Q_L\), and produces net work. Thermal efficiency is net work divided by heat input.

For a cycle, total energy change of the working fluid is zero, so \(W_{net}=Q_H-Q_L\).

\[\eta=\frac{W_{\rm net}}{Q_H}=1-\frac{Q_L}{Q_H}\]

![FIG-02-53-001: Heat engine between hot and cold reservoirs with QH, QL, and Wnet.](../figures/FIG-02-53-001-heat-engines-and-thermal-efficiency.png)

### Worked Example 1

**Problem.** Heat engine receives 1000 kJ and rejects 600 kJ. Find efficiency.

**Solution.** η=(1000-600)/1000=40%.

---

## 53.2 Carnot Cycle and Maximum Efficiency

The Carnot cycle establishes the maximum possible efficiency between two thermal reservoirs.

Absolute temperature must be used.

\[\eta_C=1-\frac{T_L}{T_H}\]

![FIG-02-53-002: Carnot cycle on T-s plot with two isotherms and two isentropes.](../figures/FIG-02-53-002-carnot-cycle-and-maximum-efficiency.png)

### Worked Example 2

**Problem.** Carnot engine between 900 K and 300 K. Find maximum efficiency.

**Solution.** η=1-300/900=66.7%.

---

## 53.3 Otto Cycle

The ideal Otto cycle models spark-ignition engines with isentropic compression/expansion and constant-volume heat addition/rejection.

Under constant-specific-heat assumptions, efficiency depends strongly on compression ratio.

\[\eta_{\rm Otto}=1-\frac{1}{r^{k-1}}\]

![FIG-02-53-003: Ideal Otto cycle on P-v and T-s diagrams with four processes.](../figures/FIG-02-53-003-otto-cycle.png)

### Worked Example 3

**Problem.** Otto cycle r=8, k=1.4. Find ideal efficiency.

**Solution.** η=1-1/(8^0.4)=56.5%.

---

## 53.4 Brayton Cycle

The Brayton cycle models ideal gas turbines: isentropic compression, constant-pressure heat addition, isentropic expansion, and constant-pressure heat rejection.

Net work is turbine work minus compressor work.

\[w_{\rm net}=w_t-w_c\]

![FIG-02-53-004: Compressor-combustor-turbine Brayton system with T-s cycle.](../figures/FIG-02-53-004-brayton-cycle.png)

### Worked Example 4

**Problem.** Rankine states h1=200, h2=210, h3=3200, h4=2300 kJ/kg. Find efficiency.

**Solution.** η=[(3200-2300)-(210-200)]/(3200-210)=29.77%.

---

## 53.5 Rankine Cycle

The Rankine cycle models steam power plants using pump, boiler, turbine, and condenser. Enthalpy differences at each component determine work and heat transfer.

Pump work is often small relative to turbine work but should not be discarded automatically.

\[\eta_{\rm Rankine}=\frac{(h_3-h_4)-(h_2-h_1)}{h_3-h_2}\]

![FIG-02-53-005: Pump-boiler-turbine-condenser Rankine loop with T-s and component state numbers.](../figures/FIG-02-53-005-rankine-cycle.png)

### Worked Example 5

**Problem.** A Brayton turbine produces 500 kJ/kg and compressor consumes 300 kJ/kg. Find net work.

**Solution.** 200 kJ/kg.

---

## 53.6 Cycle Component Efficiencies

Real compressors, pumps, and turbines deviate from ideal isentropic behavior. Use the isentropic-efficiency definitions from the Handbook to find actual outlet enthalpy.

Do not apply turbine efficiency formula to a compressor or vice versa; numerator/denominator roles differ.

\[\eta_t=\frac{h_1-h_2}{h_1-h_{2s}},\qquad \eta_c=\frac{h_{2s}-h_1}{h_2-h_1}\]

![FIG-02-53-006: Actual and isentropic turbine/compressor paths on T-s plot.](../figures/FIG-02-53-006-cycle-component-efficiencies.png)

### Worked Example 6

**Problem.** What four components define a simple Rankine cycle?

**Solution.** Pump, boiler, turbine, condenser.

---

## 53.7 Cycle Improvement and Limits

Increasing average heat-addition temperature and decreasing average heat-rejection temperature generally improve thermal efficiency, subject to material, pressure, moisture, combustion, and equipment constraints.

Regeneration, reheating, intercooling, and feedwater heating are engineering modifications; use the specific cycle model supplied by the problem.

\[\text{first law + second law + component limits}\Rightarrow\text{cycle performance}\]

![FIG-02-53-007: Cycle-improvement map showing reheat, regeneration, intercooling, and temperature limits.](../figures/FIG-02-53-007-cycle-improvement-and-limits.png)

### Worked Example 7

**Problem.** Which cycle idealizes spark-ignition engines?

**Solution.** Otto cycle.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Which cycle idealizes gas turbines?

**Solution.** Brayton cycle.

### Worked Example 9

**Problem.** What is the reversible upper efficiency bound between two reservoirs?

**Solution.** Carnot efficiency.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Thermodynamics, printed pp. 149 and 176; Mechanical Engineering supplemental cycle material pp. 462–465**.

**Source boundary:** The Handbook directly gives heat-engine efficiency, Carnot limit, and plotted/common relations for Carnot, Otto, Rankine, and Brayton-cycle material in the thermodynamics/mechanical sections. Detailed cycle-improvement discussion is guide-developed.

---

## Where This Goes Wrong

**Using thermal efficiency outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Carnot efficiency outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Otto cycle outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Brayton cycle outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using Rankine cycle outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using isentropic efficiency outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using cycle performance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| thermal efficiency | Concept developed in §53.1; use the section definition and conditions. |
| Carnot efficiency | Concept developed in §53.2; use the section definition and conditions. |
| Otto cycle | Concept developed in §53.3; use the section definition and conditions. |
| Brayton cycle | Concept developed in §53.4; use the section definition and conditions. |
| Rankine cycle | Concept developed in §53.5; use the section definition and conditions. |
| isentropic efficiency | Concept developed in §53.6; use the section definition and conditions. |
| cycle performance | Concept developed in §53.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **thermal efficiency** and state the governing equation or modeling rule.

2. Define **Carnot efficiency** and state the governing equation or modeling rule.

3. Define **Otto cycle** and state the governing equation or modeling rule.

4. Define **Brayton cycle** and state the governing equation or modeling rule.

5. Define **Rankine cycle** and state the governing equation or modeling rule.

6. Define **isentropic efficiency** and state the governing equation or modeling rule.

7. Define **cycle performance** and state the governing equation or modeling rule.

8. What is the most likely error if **thermal efficiency** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **Carnot efficiency** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **Otto cycle** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **Brayton cycle** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **Rankine cycle** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **isentropic efficiency** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **cycle performance** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **thermal efficiency**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **Carnot efficiency**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **Otto cycle**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **Brayton cycle**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **Rankine cycle**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **isentropic efficiency**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **cycle performance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **thermal efficiency**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **Carnot efficiency**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **thermal efficiency** is developed in §53.1. Use the displayed relation together with that section's assumptions and units.

2. **Carnot efficiency** is developed in §53.2. Use the displayed relation together with that section's assumptions and units.

3. **Otto cycle** is developed in §53.3. Use the displayed relation together with that section's assumptions and units.

4. **Brayton cycle** is developed in §53.4. Use the displayed relation together with that section's assumptions and units.

5. **Rankine cycle** is developed in §53.5. Use the displayed relation together with that section's assumptions and units.

6. **isentropic efficiency** is developed in §53.6. Use the displayed relation together with that section's assumptions and units.

7. **cycle performance** is developed in §53.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **thermal efficiency**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Carnot efficiency**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Otto cycle**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Brayton cycle**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **Rankine cycle**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **isentropic efficiency**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **cycle performance**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **thermal efficiency** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **Carnot efficiency** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **Otto cycle** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **Brayton cycle** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **Rankine cycle** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **isentropic efficiency** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **cycle performance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **thermal efficiency** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **Carnot efficiency** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Heat engine receives 1000 kJ and rejects 600 kJ. Find efficiency.

2. Carnot engine between 900 K and 300 K. Find maximum efficiency.

3. Otto cycle r=8, k=1.4. Find ideal efficiency.

4. Rankine states h1=200, h2=210, h3=3200, h4=2300 kJ/kg. Find efficiency.

5. A Brayton turbine produces 500 kJ/kg and compressor consumes 300 kJ/kg. Find net work.

6. What four components define a simple Rankine cycle?

7. Which cycle idealizes spark-ignition engines?

8. Which cycle idealizes gas turbines?

9. What is the reversible upper efficiency bound between two reservoirs?

10. Why does real turbine inefficiency reduce cycle efficiency?


---

## Practice Problem Solutions

1. η=(1000-600)/1000=40%.

2. η=1-300/900=66.7%.

3. η=1-1/(8^0.4)=56.5%.

4. η=[(3200-2300)-(210-200)]/(3200-210)=29.77%.

5. 200 kJ/kg.

6. Pump, boiler, turbine, condenser.

7. Otto cycle.

8. Brayton cycle.

9. Carnot efficiency.

10. Actual turbine produces less work than the isentropic reference for the same inlet/exit pressure conditions.


---

## Quick Reference

**Handbook anchor:** Thermodynamics, printed pp. 149 and 176; Mechanical Engineering supplemental cycle material pp. 462–465.

- **thermal efficiency:** Heat Engines and Thermal Efficiency
- **Carnot efficiency:** Carnot Cycle and Maximum Efficiency
- **Otto cycle:** Otto Cycle
- **Brayton cycle:** Brayton Cycle
- **Rankine cycle:** Rankine Cycle
- **isentropic efficiency:** Cycle Component Efficiencies
- **cycle performance:** Cycle Improvement and Limits
---

## What's Next

**02-54 — Refrigeration and Heat Pumps**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor