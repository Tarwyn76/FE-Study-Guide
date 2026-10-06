---
chapter: "02-47"
title: "Thermodynamic Systems, Properties, Work, and Heat"
layer: 2
tier: D
template: technical
ledger_ids: [THERMO-2D-047-01, THERMO-2D-047-02, THERMO-2D-047-03, THERMO-2D-047-04, THERMO-2D-047-05, THERMO-2D-047-06, THERMO-2D-047-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-47: Thermodynamic Systems, Properties, Work, and Heat

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-41 Fluid Properties · 02-34 Work, Energy, and Power

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines intensive/extensive/specific properties, thermodynamic state functions, closed/open systems, heat/work sign conventions, boundary work, and common ideal-gas process relations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **47.1** Explain and apply **Systems, Surroundings, and Boundaries**.
* **47.2** Explain and apply **Intensive, Extensive, and Specific Properties**.
* **47.3** Explain and apply **Internal Energy, Enthalpy, and Entropy**.
* **47.4** Explain and apply **Heat and Work Sign Convention**.
* **47.5** Explain and apply **Boundary Work**.
* **47.6** Explain and apply **Common Thermodynamic Processes**.
* **47.7** Explain and apply **State Principle and Modeling Discipline**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 47.1 Systems, Surroundings, and Boundaries

A thermodynamic system is the matter or region selected for analysis. A closed system contains fixed mass; an open system/control volume allows mass crossing the boundary.

Energy may cross by heat and work in either system type. Define the boundary before writing any balance.

\[\text{closed system: }\dot m_{\rm boundary}=0\]

![FIG-02-47-001: Closed system and open control volume compared with heat, work, and mass arrows.](../figures/FIG-02-47-001-systems-surroundings-and-boundaries.png)

### Worked Example 1

**Problem.** Classify pressure as intensive or extensive.

**Solution.** Intensive.

---

## 47.2 Intensive, Extensive, and Specific Properties

Intensive properties do not scale with system mass; extensive properties do. Dividing an extensive property by mass gives a specific property.

Pressure and temperature are intensive. Total volume and total internal energy are extensive; specific volume and specific internal energy are intensive.

\[v=\frac Vm,\qquad u=\frac Um,\qquad h=\frac Hm,\qquad s=\frac Sm\]

![FIG-02-47-002: Intensive, extensive, and specific property classification with examples.](../figures/FIG-02-47-002-intensive-extensive-and-specific-properties.png)

### Worked Example 2

**Problem.** Classify total internal energy U as intensive or extensive.

**Solution.** Extensive.

---

## 47.3 Internal Energy, Enthalpy, and Entropy

Internal energy \(U\) is microscopic stored energy. Enthalpy combines internal energy with flow-work term \(PV\), making it especially useful in control-volume analysis.

Entropy is a state property central to the second law; it is not simply 'waste heat.'

\[H=U+PV,\qquad h=u+Pv\]

![FIG-02-47-003: Relationship among internal energy, flow work Pv, and enthalpy.](../figures/FIG-02-47-003-internal-energy-enthalpy-and-entropy.png)

### Worked Example 3

**Problem.** If U=500 kJ and m=10 kg, find u.

**Solution.** u=50 kJ/kg.

---

## 47.4 Heat and Work Sign Convention

The Handbook takes heat \(Q\) as positive into the system and work \(W\) as positive out of the system.

Heat and work are energy transfers, not stored properties. A system does not 'contain heat' as a state property.

\[Q>0:\text{ into system},\qquad W>0:\text{ out of system}\]

![FIG-02-47-004: System boundary with positive heat entering and positive work leaving.](../figures/FIG-02-47-004-heat-and-work-sign-convention.png)

### Worked Example 4

**Problem.** If u=200 kJ/kg, P=300 kPa, v=0.5 m³/kg, find h.

**Solution.** h=u+Pv=200+150=350 kJ/kg.

---

## 47.5 Boundary Work

For quasi-equilibrium/reversible boundary work, the Handbook gives \(w_b=\int P\,dv\) on a specific basis.

On a \(P-v\) diagram, boundary work is the area under the process curve between states.

\[w_b=\int_1^2P\,dv\]

![FIG-02-47-005: P-v process curve with shaded area representing boundary work.](../figures/FIG-02-47-005-boundary-work.png)

### Worked Example 5

**Problem.** A constant-pressure specific-volume change is 0.2 m³/kg at P=500 kPa. Find specific boundary work.

**Solution.** wb=PΔv=100 kJ/kg.

---

## 47.6 Common Thermodynamic Processes

Constant pressure, constant volume, isothermal, isentropic, and polytropic processes have special relations under stated ideal-gas assumptions.

Do not apply a process formula because the endpoint states happen to fit; the process path itself must satisfy the condition.

\[Pv^n=\text{constant}\quad\text{(polytropic ideal-gas process)}\]

![FIG-02-47-006: P-v diagram comparing constant-P, constant-v, isothermal, isentropic, and polytropic paths.](../figures/FIG-02-47-006-common-thermodynamic-processes.png)

### Worked Example 6

**Problem.** What is positive heat under Handbook sign convention?

**Solution.** Heat into the system.

---

## 47.7 State Principle and Modeling Discipline

For a simple compressible single-phase pure substance, two independent intensive properties fix the state. In the two-phase region, pressure and temperature are not independent.

The first step in any thermodynamics problem is therefore state identification, not energy algebra.

\[\text{two independent intensive properties}\Rightarrow\text{state fixed (single phase)}\]

![FIG-02-47-007: State-identification decision tree for single-phase versus two-phase pure substance.](../figures/FIG-02-47-007-state-principle-and-modeling-discipline.png)

### Worked Example 7

**Problem.** What is positive work?

**Solution.** Work done by the system/outward.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Is heat a state property?

**Solution.** No.

### Worked Example 9

**Problem.** How many independent intensive properties fix a simple single-phase pure-substance state?

**Solution.** Two.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Thermodynamics, printed pp. 143 and 147–148**.

**Source boundary:** The Handbook directly defines intensive/extensive/specific properties, thermodynamic state functions, closed/open systems, heat/work sign conventions, boundary work, and common ideal-gas process relations.

---

## Where This Goes Wrong

**Using thermodynamic system outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using thermodynamic property outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using enthalpy outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using heat and work outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using boundary work outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using thermodynamic process outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using thermodynamic state outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| thermodynamic system | Concept developed in §47.1; use the section definition and conditions. |
| thermodynamic property | Concept developed in §47.2; use the section definition and conditions. |
| enthalpy | Concept developed in §47.3; use the section definition and conditions. |
| heat and work | Concept developed in §47.4; use the section definition and conditions. |
| boundary work | Concept developed in §47.5; use the section definition and conditions. |
| thermodynamic process | Concept developed in §47.6; use the section definition and conditions. |
| thermodynamic state | Concept developed in §47.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **thermodynamic system** and state the governing equation or modeling rule.

2. Define **thermodynamic property** and state the governing equation or modeling rule.

3. Define **enthalpy** and state the governing equation or modeling rule.

4. Define **heat and work** and state the governing equation or modeling rule.

5. Define **boundary work** and state the governing equation or modeling rule.

6. Define **thermodynamic process** and state the governing equation or modeling rule.

7. Define **thermodynamic state** and state the governing equation or modeling rule.

8. What is the most likely error if **thermodynamic system** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **thermodynamic property** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **enthalpy** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **heat and work** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **boundary work** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **thermodynamic process** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **thermodynamic state** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **thermodynamic system**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **thermodynamic property**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **enthalpy**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **heat and work**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **boundary work**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **thermodynamic process**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **thermodynamic state**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **thermodynamic system**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **thermodynamic property**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **thermodynamic system** is developed in §47.1. Use the displayed relation together with that section's assumptions and units.

2. **thermodynamic property** is developed in §47.2. Use the displayed relation together with that section's assumptions and units.

3. **enthalpy** is developed in §47.3. Use the displayed relation together with that section's assumptions and units.

4. **heat and work** is developed in §47.4. Use the displayed relation together with that section's assumptions and units.

5. **boundary work** is developed in §47.5. Use the displayed relation together with that section's assumptions and units.

6. **thermodynamic process** is developed in §47.6. Use the displayed relation together with that section's assumptions and units.

7. **thermodynamic state** is developed in §47.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **thermodynamic system**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **thermodynamic property**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **enthalpy**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **heat and work**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **boundary work**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **thermodynamic process**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **thermodynamic state**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **thermodynamic system** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **thermodynamic property** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **enthalpy** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **heat and work** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **boundary work** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **thermodynamic process** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **thermodynamic state** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **thermodynamic system** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **thermodynamic property** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. Classify pressure as intensive or extensive.

2. Classify total internal energy U as intensive or extensive.

3. If U=500 kJ and m=10 kg, find u.

4. If u=200 kJ/kg, P=300 kPa, v=0.5 m³/kg, find h.

5. A constant-pressure specific-volume change is 0.2 m³/kg at P=500 kPa. Find specific boundary work.

6. What is positive heat under Handbook sign convention?

7. What is positive work?

8. Is heat a state property?

9. How many independent intensive properties fix a simple single-phase pure-substance state?

10. Why are P and T not independent in a saturated two-phase pure substance?


---

## Practice Problem Solutions

1. Intensive.

2. Extensive.

3. u=50 kJ/kg.

4. h=u+Pv=200+150=350 kJ/kg.

5. wb=PΔv=100 kJ/kg.

6. Heat into the system.

7. Work done by the system/outward.

8. No.

9. Two.

10. They are linked by the saturation relation.


---

## Quick Reference

**Handbook anchor:** Thermodynamics, printed pp. 143 and 147–148.

- **thermodynamic system:** Systems, Surroundings, and Boundaries
- **thermodynamic property:** Intensive, Extensive, and Specific Properties
- **enthalpy:** Internal Energy, Enthalpy, and Entropy
- **heat and work:** Heat and Work Sign Convention
- **boundary work:** Boundary Work
- **thermodynamic process:** Common Thermodynamic Processes
- **thermodynamic state:** State Principle and Modeling Discipline
---

## What's Next

**02-48 — Pure Substances, Phase Diagrams, and Property Tables**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor