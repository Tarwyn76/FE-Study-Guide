---
chapter: "02-52"
title: "Second Law, Entropy, and Isentropic Processes"
layer: 2
tier: D
template: technical
ledger_ids: [THERMO-2D-052-01, THERMO-2D-052-02, THERMO-2D-052-03, THERMO-2D-052-04, THERMO-2D-052-05, THERMO-2D-052-06, THERMO-2D-052-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-52: Second Law, Entropy, and Isentropic Processes

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-51 First Law — Control Volumes · 02-49 Ideal Gases

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives Kelvin-Planck and Clausius statements, entropy relations, Clausius inequality, isentropic/adiabatic distinctions, entropy generation, T-s interpretation, and exergy/irreversibility relations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **52.1** Explain and apply **Kelvin-Planck and Clausius Statements**.
* **52.2** Explain and apply **Entropy as a State Property**.
* **52.3** Explain and apply **Entropy Balance and Entropy Generation**.
* **52.4** Explain and apply **Adiabatic versus Isentropic**.
* **52.5** Explain and apply **Ideal-Gas Entropy Change**.
* **52.6** Explain and apply **Entropy Change of Solids and Liquids**.
* **52.7** Explain and apply **Exergy and Irreversibility**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 52.1 Kelvin-Planck and Clausius Statements

The second law limits the direction and maximum performance of thermal processes. Kelvin-Planck rules out a cyclic heat engine that converts heat from a single reservoir entirely into work. Clausius rules out refrigeration without net work input.

These statements explain why first-law energy conservation alone cannot determine feasibility.

\[\eta_{\rm engine}<1\quad\text{for finite-temperature heat engines}\]

![FIG-02-52-001: Heat engine and refrigerator diagrams illustrating Kelvin-Planck and Clausius limits.](../figures/FIG-02-52-001-kelvin-planck-and-clausius-statements.png)

### Worked Example 1

**Problem.** A reversible reservoir receives 100 kJ at 500 K. Find entropy change of reservoir.

**Solution.** ΔS=Q/T=0.200 kJ/K.

---

## 52.2 Entropy as a State Property

For a reversible differential heat transfer, \(ds=\delta q_{rev}/T\). Entropy is a state property even though heat transfer is path-dependent.

For irreversible processes, entropy generation accounts for the difference.

\[ds=\frac{\delta q_{\rm rev}}{T}\]

![FIG-02-52-002: T-s path with reversible heat-transfer area under the curve.](../figures/FIG-02-52-002-entropy-as-a-state-property.png)

### Worked Example 2

**Problem.** An ideal gas cp=1.0, R=0.287 kJ/kg·K changes T 300→600 K at constant P. Find Δs.

**Solution.** Δs=cp ln2=0.693 kJ/kg·K.

---

## 52.3 Entropy Balance and Entropy Generation

The entropy balance tracks entropy carried by heat and mass plus entropy generated internally. Entropy generation is nonnegative.

A reversible process has zero entropy generation; a real irreversible process has positive entropy generation.

\[\Delta S_{\rm system}=\int\frac{\delta Q}{T_b}+S_{\rm gen},\qquad S_{\rm gen}\ge0\]

![FIG-02-52-003: Entropy balance showing transfer by heat/mass and internal generation.](../figures/FIG-02-52-003-entropy-balance-and-entropy-generation.png)

### Worked Example 3

**Problem.** A solid c=0.5 kJ/kg·K heats 300→600 K. Find Δs.

**Solution.** 0.5 ln2=0.347 kJ/kg·K.

---

## 52.4 Adiabatic versus Isentropic

Adiabatic means no heat transfer. Isentropic means constant entropy. A reversible adiabatic process is isentropic; an irreversible adiabatic process generates entropy and is not isentropic.

This distinction is central to turbine/compressor efficiency calculations.

\[\delta q=0\ \&\ S_{\rm gen}=0\Rightarrow \Delta s=0\]

![FIG-02-52-004: Adiabatic reversible path versus adiabatic irreversible path on T-s axes.](../figures/FIG-02-52-004-adiabatic-versus-isentropic.png)

### Worked Example 4

**Problem.** If an adiabatic process has positive entropy generation, is it isentropic?

**Solution.** No.

---

## 52.5 Ideal-Gas Entropy Change

For constant-specific-heat ideal gases, the Handbook provides entropy-change relations using temperature with either pressure or volume.

These formulas apply to state changes, regardless of whether the actual path is reversible, because entropy is a property.

\[\Delta s=c_p\ln\frac{T_2}{T_1}-R\ln\frac{P_2}{P_1}\]

![FIG-02-52-005: Ideal-gas entropy change shown using T-P and T-v forms.](../figures/FIG-02-52-005-ideal-gas-entropy-change.png)

### Worked Example 5

**Problem.** What condition makes an adiabatic process isentropic?

**Solution.** Reversibility/zero entropy generation.

---

## 52.6 Entropy Change of Solids and Liquids

For incompressible solids/liquids with approximately constant heat capacity, entropy change depends logarithmically on absolute temperature.

Pressure effects are often small under the Handbook approximation unless a more complete model is supplied.

\[\Delta s\approx c\ln\frac{T_2}{T_1}\]

![FIG-02-52-006: Solid/liquid heating from T1 to T2 with entropy change.](../figures/FIG-02-52-006-entropy-change-of-solids-and-liquids.png)

### Worked Example 6

**Problem.** Can a cyclic heat engine convert all QH from one reservoir into work?

**Solution.** No, Kelvin-Planck statement.

---

## 52.7 Exergy and Irreversibility

Exergy is the maximum useful work relative to an environment. Irreversibility quantifies lost work potential and is tied to entropy generation.

The Handbook gives \(I=T_0\Delta S_{total}\) for the stated environment model.

\[I=T_0S_{\rm gen}\]

![FIG-02-52-007: Energy versus exergy flow showing useful work potential destroyed by irreversibility.](../figures/FIG-02-52-007-exergy-and-irreversibility.png)

### Worked Example 7

**Problem.** Can a refrigerator operate cyclically without work input?

**Solution.** No, Clausius statement.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What is sign of entropy generation in a real irreversible process?

**Solution.** Positive.

### Worked Example 9

**Problem.** What does exergy measure?

**Solution.** Maximum useful work potential relative to an environment.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Thermodynamics, printed pp. 150–152**.

**Source boundary:** The Handbook directly gives Kelvin-Planck and Clausius statements, entropy relations, Clausius inequality, isentropic/adiabatic distinctions, entropy generation, T-s interpretation, and exergy/irreversibility relations.

---

## Where This Goes Wrong

**Using second law outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using entropy outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using entropy generation outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using isentropic process outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using ideal-gas entropy outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using incompressible entropy outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using exergy destruction outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| second law | Concept developed in §52.1; use the section definition and conditions. |
| entropy | Concept developed in §52.2; use the section definition and conditions. |
| entropy generation | Concept developed in §52.3; use the section definition and conditions. |
| isentropic process | Concept developed in §52.4; use the section definition and conditions. |
| ideal-gas entropy | Concept developed in §52.5; use the section definition and conditions. |
| incompressible entropy | Concept developed in §52.6; use the section definition and conditions. |
| exergy destruction | Concept developed in §52.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **second law** and state the governing equation or modeling rule.

2. Define **entropy** and state the governing equation or modeling rule.

3. Define **entropy generation** and state the governing equation or modeling rule.

4. Define **isentropic process** and state the governing equation or modeling rule.

5. Define **ideal-gas entropy** and state the governing equation or modeling rule.

6. Define **incompressible entropy** and state the governing equation or modeling rule.

7. Define **exergy destruction** and state the governing equation or modeling rule.

8. What is the most likely error if **second law** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **entropy** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **entropy generation** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **isentropic process** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **ideal-gas entropy** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **incompressible entropy** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **exergy destruction** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **second law**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **entropy**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **entropy generation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **isentropic process**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **ideal-gas entropy**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **incompressible entropy**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **exergy destruction**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **second law**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **entropy**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **second law** is developed in §52.1. Use the displayed relation together with that section's assumptions and units.

2. **entropy** is developed in §52.2. Use the displayed relation together with that section's assumptions and units.

3. **entropy generation** is developed in §52.3. Use the displayed relation together with that section's assumptions and units.

4. **isentropic process** is developed in §52.4. Use the displayed relation together with that section's assumptions and units.

5. **ideal-gas entropy** is developed in §52.5. Use the displayed relation together with that section's assumptions and units.

6. **incompressible entropy** is developed in §52.6. Use the displayed relation together with that section's assumptions and units.

7. **exergy destruction** is developed in §52.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **second law**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **entropy**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **entropy generation**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **isentropic process**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **ideal-gas entropy**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **incompressible entropy**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **exergy destruction**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **second law** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **entropy** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **entropy generation** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **isentropic process** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **ideal-gas entropy** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **incompressible entropy** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **exergy destruction** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **second law** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **entropy** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. A reversible reservoir receives 100 kJ at 500 K. Find entropy change of reservoir.

2. An ideal gas cp=1.0, R=0.287 kJ/kg·K changes T 300→600 K at constant P. Find Δs.

3. A solid c=0.5 kJ/kg·K heats 300→600 K. Find Δs.

4. If an adiabatic process has positive entropy generation, is it isentropic?

5. What condition makes an adiabatic process isentropic?

6. Can a cyclic heat engine convert all QH from one reservoir into work?

7. Can a refrigerator operate cyclically without work input?

8. What is sign of entropy generation in a real irreversible process?

9. What does exergy measure?

10. If T0=300 K and Sgen=2 kJ/K, find exergy destruction.


---

## Practice Problem Solutions

1. ΔS=Q/T=0.200 kJ/K.

2. Δs=cp ln2=0.693 kJ/kg·K.

3. 0.5 ln2=0.347 kJ/kg·K.

4. No.

5. Reversibility/zero entropy generation.

6. No, Kelvin-Planck statement.

7. No, Clausius statement.

8. Positive.

9. Maximum useful work potential relative to an environment.

10. I=600 kJ.


---

## Quick Reference

**Handbook anchor:** Thermodynamics, printed pp. 150–152.

- **second law:** Kelvin-Planck and Clausius Statements
- **entropy:** Entropy as a State Property
- **entropy generation:** Entropy Balance and Entropy Generation
- **isentropic process:** Adiabatic versus Isentropic
- **ideal-gas entropy:** Ideal-Gas Entropy Change
- **incompressible entropy:** Entropy Change of Solids and Liquids
- **exergy destruction:** Exergy and Irreversibility
---

## What's Next

**02-53 — Power Cycles**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor