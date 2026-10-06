---
chapter: "02-50"
title: "First Law — Closed Systems"
layer: 2
tier: D
template: technical
ledger_ids: [THERMO-2D-050-01, THERMO-2D-050-02, THERMO-2D-050-03, THERMO-2D-050-04, THERMO-2D-050-05, THERMO-2D-050-06, THERMO-2D-050-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-50: First Law — Closed Systems

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-47 Systems, Work, and Heat · 02-49 Ideal Gases

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly states the closed-system first law and gives reversible boundary-work relations and constant-P, constant-v, isothermal, isentropic, and polytropic special cases.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **50.1** Explain and apply **Closed-System Energy Balance**.
* **50.2** Explain and apply **Internal, Kinetic, and Potential Energy Changes**.
* **50.3** Explain and apply **Constant-Pressure Boundary Work**.
* **50.4** Explain and apply **Constant-Volume Process**.
* **50.5** Explain and apply **Isothermal Ideal-Gas Process**.
* **50.6** Explain and apply **Polytropic and Isentropic Processes**.
* **50.7** Explain and apply **Closed-System Solution Workflow**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 50.1 Closed-System Energy Balance

For a closed system, no mass crosses the boundary. The first law states that heat added minus work done by the system equals the change in total system energy.

Use the Handbook sign convention consistently.

\[Q-W=\Delta U+\Delta KE+\Delta PE\]

![FIG-02-50-001: Closed system with heat/work arrows and changes in internal, kinetic, and potential energy.](../figures/FIG-02-50-001-closed-system-energy-balance.png)

### Worked Example 1

**Problem.** A closed system receives 100 kJ heat and does 40 kJ work, with negligible KE/PE. Find ΔU.

**Solution.** ΔU=60 kJ.

---

## 50.2 Internal, Kinetic, and Potential Energy Changes

Many piston-cylinder problems neglect kinetic and potential energy, but this must be justified. If they are negligible, the balance reduces to \(Q-W=\Delta U\).

Internal-energy change for an ideal gas can often be obtained from \(c_v\Delta T\).

\[\Delta E=\Delta U+\frac m2(V_2^2-V_1^2)+mg(z_2-z_1)\]

![FIG-02-50-002: Energy-change stack showing internal, kinetic, and potential contributions.](../figures/FIG-02-50-002-internal-kinetic-and-potential-energy-changes.png)

### Worked Example 2

**Problem.** A rigid tank receives 80 kJ heat, no other work. Find ΔU.

**Solution.** 80 kJ.

---

## 50.3 Constant-Pressure Boundary Work

At constant boundary pressure, reversible boundary work equals pressure times volume change.

For an ideal gas under constant pressure, temperature is proportional to specific volume.

\[W_b=P(V_2-V_1)\]

![FIG-02-50-003: Horizontal constant-pressure path with area under curve equal to work.](../figures/FIG-02-50-003-constant-pressure-boundary-work.png)

### Worked Example 3

**Problem.** Constant pressure 200 kPa, volume increases 0.5 m³. Find boundary work.

**Solution.** W=100 kJ.

---

## 50.4 Constant-Volume Process

A rigid tank has no moving boundary, so boundary work is zero. Heat transfer then changes internal energy when other work modes and KE/PE are absent.

Pressure may still change significantly as temperature changes.

\[W_b=0,\qquad Q=\Delta U\quad\text{(if other terms negligible)}\]

![FIG-02-50-004: Rigid tank heated at constant volume with changing pressure and temperature.](../figures/FIG-02-50-004-constant-volume-process.png)

### Worked Example 4

**Problem.** Ideal gas m=1 kg, R=0.287, T=300 K expands isothermally V2/V1=2. Find work.

**Solution.** W=0.287*300*ln2=59.67 kJ.

---

## 50.5 Isothermal Ideal-Gas Process

For an ideal gas at constant temperature, internal energy is unchanged when ideal-gas internal energy depends only on temperature. Reversible boundary work follows a logarithmic relation.

Thus, for a simple isothermal ideal-gas closed process with negligible other work, heat equals boundary work.

\[W_b=mRT\ln\frac{V_2}{V_1}\]

![FIG-02-50-005: Hyperbolic isothermal expansion curve with work area.](../figures/FIG-02-50-005-isothermal-ideal-gas-process.png)

### Worked Example 5

**Problem.** Polytropic process P1V1=200 kJ, P2V2=150 kJ, n=1.3. Find W.

**Solution.** W=(150-200)/(1-1.3)=166.7 kJ.

---

## 50.6 Polytropic and Isentropic Processes

A polytropic process obeys \(PV^n=	ext{constant}\). For \(n
e1\), boundary work has a closed-form expression. An isentropic ideal-gas process is a special case with exponent \(k\) under constant-specific-heat assumptions.

Use the actual process model stated in the problem.

\[W_b=\frac{P_2V_2-P_1V_1}{1-n}\]

![FIG-02-50-006: Family of P-v curves for different polytropic exponents including isothermal and isentropic.](../figures/FIG-02-50-006-polytropic-and-isentropic-processes.png)

### Worked Example 6

**Problem.** For an expansion under Handbook sign convention, is boundary work generally positive or negative?

**Solution.** Positive, if the system does work on surroundings.

---

## 50.7 Closed-System Solution Workflow

Identify the system, states, process path, heat/work signs, and property model. Evaluate state properties before substituting into the first law.

Finally, verify that work sign matches expansion/compression and that energy units are consistent.

\[\text{state 1}\rightarrow\text{process}\rightarrow\text{state 2}\rightarrow Q-W=\Delta E\]

![FIG-02-50-007: Closed-system problem workflow from state definition to energy-balance check.](../figures/FIG-02-50-007-closed-system-solution-workflow.png)

### Worked Example 7

**Problem.** What is boundary work in a constant-volume process?

**Solution.** Zero.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** If ideal-gas temperature is constant, what is ΔU under ideal-gas assumption?

**Solution.** Zero.

### Worked Example 9

**Problem.** Why is process path needed for boundary work?

**Solution.** Work is path-dependent and equals ∫P dV.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Thermodynamics, printed p. 147**.

**Source boundary:** The Handbook directly states the closed-system first law and gives reversible boundary-work relations and constant-P, constant-v, isothermal, isentropic, and polytropic special cases.

---

## Where This Goes Wrong

**Using closed-system first law outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using closed-system energy change outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using constant-pressure process outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using constant-volume process outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using isothermal process outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using polytropic process outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using closed-system workflow outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| closed-system first law | Concept developed in §50.1; use the section definition and conditions. |
| closed-system energy change | Concept developed in §50.2; use the section definition and conditions. |
| constant-pressure process | Concept developed in §50.3; use the section definition and conditions. |
| constant-volume process | Concept developed in §50.4; use the section definition and conditions. |
| isothermal process | Concept developed in §50.5; use the section definition and conditions. |
| polytropic process | Concept developed in §50.6; use the section definition and conditions. |
| closed-system workflow | Concept developed in §50.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **closed-system first law** and state the governing equation or modeling rule.

2. Define **closed-system energy change** and state the governing equation or modeling rule.

3. Define **constant-pressure process** and state the governing equation or modeling rule.

4. Define **constant-volume process** and state the governing equation or modeling rule.

5. Define **isothermal process** and state the governing equation or modeling rule.

6. Define **polytropic process** and state the governing equation or modeling rule.

7. Define **closed-system workflow** and state the governing equation or modeling rule.

8. What is the most likely error if **closed-system first law** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **closed-system energy change** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **constant-pressure process** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **constant-volume process** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **isothermal process** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **polytropic process** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **closed-system workflow** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **closed-system first law**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **closed-system energy change**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **constant-pressure process**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **constant-volume process**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **isothermal process**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **polytropic process**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **closed-system workflow**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **closed-system first law**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **closed-system energy change**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **closed-system first law** is developed in §50.1. Use the displayed relation together with that section's assumptions and units.

2. **closed-system energy change** is developed in §50.2. Use the displayed relation together with that section's assumptions and units.

3. **constant-pressure process** is developed in §50.3. Use the displayed relation together with that section's assumptions and units.

4. **constant-volume process** is developed in §50.4. Use the displayed relation together with that section's assumptions and units.

5. **isothermal process** is developed in §50.5. Use the displayed relation together with that section's assumptions and units.

6. **polytropic process** is developed in §50.6. Use the displayed relation together with that section's assumptions and units.

7. **closed-system workflow** is developed in §50.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **closed-system first law**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **closed-system energy change**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **constant-pressure process**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **constant-volume process**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **isothermal process**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **polytropic process**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **closed-system workflow**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **closed-system first law** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **closed-system energy change** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **constant-pressure process** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **constant-volume process** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **isothermal process** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **polytropic process** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **closed-system workflow** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **closed-system first law** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **closed-system energy change** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. A closed system receives 100 kJ heat and does 40 kJ work, with negligible KE/PE. Find ΔU.

2. A rigid tank receives 80 kJ heat, no other work. Find ΔU.

3. Constant pressure 200 kPa, volume increases 0.5 m³. Find boundary work.

4. Ideal gas m=1 kg, R=0.287, T=300 K expands isothermally V2/V1=2. Find work.

5. Polytropic process P1V1=200 kJ, P2V2=150 kJ, n=1.3. Find W.

6. For an expansion under Handbook sign convention, is boundary work generally positive or negative?

7. What is boundary work in a constant-volume process?

8. If ideal-gas temperature is constant, what is ΔU under ideal-gas assumption?

9. Why is process path needed for boundary work?

10. What should be determined before applying the first law?


---

## Practice Problem Solutions

1. ΔU=60 kJ.

2. 80 kJ.

3. W=100 kJ.

4. W=0.287*300*ln2=59.67 kJ.

5. W=(150-200)/(1-1.3)=166.7 kJ.

6. Positive, if the system does work on surroundings.

7. Zero.

8. Zero.

9. Work is path-dependent and equals ∫P dV.

10. States, process, system boundary, and heat/work sign conventions.


---

## Quick Reference

**Handbook anchor:** Thermodynamics, printed p. 147.

- **closed-system first law:** Closed-System Energy Balance
- **closed-system energy change:** Internal, Kinetic, and Potential Energy Changes
- **constant-pressure process:** Constant-Pressure Boundary Work
- **constant-volume process:** Constant-Volume Process
- **isothermal process:** Isothermal Ideal-Gas Process
- **polytropic process:** Polytropic and Isentropic Processes
- **closed-system workflow:** Closed-System Solution Workflow
---

## What's Next

**02-51 — First Law — Control Volumes**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor