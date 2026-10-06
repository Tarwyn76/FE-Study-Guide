---
chapter: "02-48"
title: "Pure Substances, Phase Diagrams, and Property Tables"
layer: 2
tier: D
template: technical
ledger_ids: [THERMO-2D-048-01, THERMO-2D-048-02, THERMO-2D-048-03, THERMO-2D-048-04, THERMO-2D-048-05, THERMO-2D-048-06, THERMO-2D-048-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-48: Pure Substances, Phase Diagrams, and Property Tables

> *"Thermal-fluid problems become manageable when the state, control volume, constitutive model, and conservation law are separated before calculation."*

---

## Before You Start

**Prerequisites:** 02-47 Thermodynamic Systems and Properties

**Skip if:** You can identify the governing thermal-fluid model, locate the necessary Handbook data, solve representative FE-level calculations, and check conservation, units, and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives two-phase quality relations, saturated/superheated property tables, and P-v/T-s/P-h diagrams for water and refrigerants.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **48.1** Explain and apply **Pure-Substance Phases and Saturation**.
* **48.2** Explain and apply **Saturation Dome and Critical Point**.
* **48.3** Explain and apply **Quality in the Two-Phase Region**.
* **48.4** Explain and apply **Using Saturated Property Tables**.
* **48.5** Explain and apply **Superheated Vapor and Compressed Liquid**.
* **48.6** Explain and apply **P-v, T-s, and P-h Diagrams**.
* **48.7** Explain and apply **Interpolation and State Consistency**.

---

## Notation Used Here

Symbols are defined at first use. Use SI units unless the problem or Handbook table specifies another basis. Absolute temperature and absolute pressure must be used in equations that require them.

---

## 48.1 Pure-Substance Phases and Saturation

A pure substance can exist as compressed/subcooled liquid, saturated liquid-vapor mixture, superheated vapor, or other phase states.

At saturation, pressure and temperature are linked. Specifying both does not provide two independent properties.

\[P=P_{\rm sat}(T)\quad\text{on the saturation line}\]

![FIG-02-48-001: P-v dome showing compressed liquid, saturated mixture, and superheated vapor regions.](../figures/FIG-02-48-001-pure-substance-phases-and-saturation.png)

### Worked Example 1

**Problem.** A saturated mixture has x=0.30, hf=500 kJ/kg, hfg=2200 kJ/kg. Find h.

**Solution.** h=500+0.30(2200)=1160 kJ/kg.

---

## 48.2 Saturation Dome and Critical Point

The liquid-vapor dome is bounded by saturated-liquid and saturated-vapor lines. The critical point is where the distinction between liquid and vapor disappears.

The triple point is the unique equilibrium of solid, liquid, and vapor phases.

\[x=0:\text{ saturated liquid},\qquad x=1:\text{ saturated vapor}\]

![FIG-02-48-002: Saturation dome with critical point, saturated-liquid line, saturated-vapor line, and quality lines.](../figures/FIG-02-48-002-saturation-dome-and-critical-point.png)

### Worked Example 2

**Problem.** A mixture contains 2 kg vapor and 6 kg liquid. Find quality.

**Solution.** x=2/8=0.25.

---

## 48.3 Quality in the Two-Phase Region

Quality \(x\) is vapor mass fraction in a saturated liquid-vapor mixture. It is defined only inside the two-phase region.

Any specific extensive property \(y\in\{v,u,h,s\}\) follows \(y=y_f+x(y_g-y_f)\).

\[x=\frac{m_g}{m_f+m_g},\qquad y=y_f+xy_{fg}\]

![FIG-02-48-003: Two-phase mixture with liquid/vapor masses and property interpolation between f and g states.](../figures/FIG-02-48-003-quality-in-the-two-phase-region.png)

### Worked Example 3

**Problem.** At fixed P, T is above Tsat. Identify region.

**Solution.** Superheated vapor.

---

## 48.4 Using Saturated Property Tables

Saturated tables may be indexed by temperature or pressure. Once the saturation state is known, read \(v_f,v_g,u_f,u_g,h_f,h_g,s_f,s_g\) or \(fg\) differences.

Do not interpolate between a saturated table and a superheated table as though they were one continuous column set.

\[y_{fg}=y_g-y_f\]

![FIG-02-48-004: Annotated saturated-water table showing f, g, and fg columns.](../figures/FIG-02-48-004-using-saturated-property-tables.png)

### Worked Example 4

**Problem.** At fixed P, T is below Tsat. Identify region.

**Solution.** Compressed/subcooled liquid.

---

## 48.5 Superheated Vapor and Compressed Liquid

If \(T>T_{m sat}(P)\), the state is superheated vapor. If \(T<T_{m sat}(P)\), it is compressed/subcooled liquid.

Use the appropriate table or stated approximation. A common liquid approximation uses saturated-liquid properties at the same temperature when permitted.

\[T>T_{\rm sat}(P)\Rightarrow\text{superheated vapor}\]

![FIG-02-48-005: State point comparison with saturation temperature at fixed pressure.](../figures/FIG-02-48-005-superheated-vapor-and-compressed-liquid.png)

### Worked Example 5

**Problem.** What is quality of saturated liquid?

**Solution.** 0.

---

## 48.6 P-v, T-s, and P-h Diagrams

Different diagrams emphasize different processes. P-v makes boundary work visible; T-s makes reversible heat transfer visible; P-h is especially useful for refrigeration components.

Read axes and phase region before tracing a process.

\[q_{\rm rev}=\int T\,ds\]

![FIG-02-48-006: P-v, T-s, and P-h diagrams for the same saturated dome and representative process.](../figures/FIG-02-48-006-p-v-t-s-and-p-h-diagrams.png)

### Worked Example 6

**Problem.** What is quality of saturated vapor?

**Solution.** 1.

---

## 48.7 Interpolation and State Consistency

When a state lies between table entries, linear interpolation is often used unless the problem directs otherwise. Interpolate only within the same region and same independent-variable pair.

After obtaining properties, verify they are consistent with the identified phase and quality bounds.

\[y\approx y_1+\frac{x-x_1}{x_2-x_1}(y_2-y_1)\]

![FIG-02-48-007: Two table rows with a state between them and linear interpolation geometry.](../figures/FIG-02-48-007-interpolation-and-state-consistency.png)

### Worked Example 7

**Problem.** Can quality be used for superheated vapor?

**Solution.** No.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Which diagram is especially convenient for vapor-compression refrigeration?

**Solution.** P-h diagram.

### Worked Example 9

**Problem.** Which diagram makes reversible heat transfer appear as area under a curve?

**Solution.** T-s diagram.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Thermodynamics, printed pp. 143–144 and property tables/diagrams in pp. 157–180**.

**Source boundary:** The Handbook directly gives two-phase quality relations, saturated/superheated property tables, and P-v/T-s/P-h diagrams for water and refrigerants.

---

## Where This Goes Wrong

**Using pure substance outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using saturation dome outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using vapor quality outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using saturated property table outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using superheated vapor outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using thermodynamic property diagram outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Using property interpolation outside its assumptions.** Check state, geometry, flow/thermal regime, property basis, and units before applying the relation.

**Ignoring conservation.** Mass, energy, momentum, or entropy balances provide independent checks and often reveal a sign or state error.


---

## Key Terms

| Term | Working definition |
|---|---|
| pure substance | Concept developed in §48.1; use the section definition and conditions. |
| saturation dome | Concept developed in §48.2; use the section definition and conditions. |
| vapor quality | Concept developed in §48.3; use the section definition and conditions. |
| saturated property table | Concept developed in §48.4; use the section definition and conditions. |
| superheated vapor | Concept developed in §48.5; use the section definition and conditions. |
| thermodynamic property diagram | Concept developed in §48.6; use the section definition and conditions. |
| property interpolation | Concept developed in §48.7; use the section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **pure substance** and state the governing equation or modeling rule.

2. Define **saturation dome** and state the governing equation or modeling rule.

3. Define **vapor quality** and state the governing equation or modeling rule.

4. Define **saturated property table** and state the governing equation or modeling rule.

5. Define **superheated vapor** and state the governing equation or modeling rule.

6. Define **thermodynamic property diagram** and state the governing equation or modeling rule.

7. Define **property interpolation** and state the governing equation or modeling rule.

8. What is the most likely error if **pure substance** is used without checking state, geometry, flow regime, or property assumptions?

9. What is the most likely error if **saturation dome** is used without checking state, geometry, flow regime, or property assumptions?

10. What is the most likely error if **vapor quality** is used without checking state, geometry, flow regime, or property assumptions?

11. What is the most likely error if **saturated property table** is used without checking state, geometry, flow regime, or property assumptions?

12. What is the most likely error if **superheated vapor** is used without checking state, geometry, flow regime, or property assumptions?

13. What is the most likely error if **thermodynamic property diagram** is used without checking state, geometry, flow regime, or property assumptions?

14. What is the most likely error if **property interpolation** is used without checking state, geometry, flow regime, or property assumptions?

15. What state, control volume, diagram, or flow model should be established before beginning calculation?

16. Give one dimensional or conservation check for a final answer.

17. When should a Handbook table/correlation override a remembered rule of thumb?

18. Why should absolute temperature or absolute pressure be used where required?

### Multiple Choice

19. Which statement best describes **pure substance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

20. Which statement best describes **saturation dome**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

21. Which statement best describes **vapor quality**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

22. Which statement best describes **saturated property table**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

23. Which statement best describes **superheated vapor**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

24. Which statement best describes **thermodynamic property diagram**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

25. Which statement best describes **property interpolation**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

26. Which statement best describes **pure substance**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws

27. Which statement best describes **saturation dome**?
A) It is conditional on the physical model and assumptions
B) It is valid independent of state and geometry
C) It is only a unit conversion
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **pure substance** is developed in §48.1. Use the displayed relation together with that section's assumptions and units.

2. **saturation dome** is developed in §48.2. Use the displayed relation together with that section's assumptions and units.

3. **vapor quality** is developed in §48.3. Use the displayed relation together with that section's assumptions and units.

4. **saturated property table** is developed in §48.4. Use the displayed relation together with that section's assumptions and units.

5. **superheated vapor** is developed in §48.5. Use the displayed relation together with that section's assumptions and units.

6. **thermodynamic property diagram** is developed in §48.6. Use the displayed relation together with that section's assumptions and units.

7. **property interpolation** is developed in §48.7. Use the displayed relation together with that section's assumptions and units.

8. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **pure substance**.

9. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **saturation dome**.

10. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **vapor quality**.

11. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **saturated property table**.

12. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **superheated vapor**.

13. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **thermodynamic property diagram**.

14. The equation or property may be applied outside its valid model. Identify the state/geometry/regime first, then apply **property interpolation**.

15. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

16. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

17. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

18. Define the physical model first, use conservation and units as checks, rely on supplied Handbook/property data, and use absolute scales whenever the governing equation requires them.

19. **A.** The chapter applies **pure substance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

20. **A.** The chapter applies **saturation dome** only after the state, geometry, flow/thermal regime, and assumptions are defined.

21. **A.** The chapter applies **vapor quality** only after the state, geometry, flow/thermal regime, and assumptions are defined.

22. **A.** The chapter applies **saturated property table** only after the state, geometry, flow/thermal regime, and assumptions are defined.

23. **A.** The chapter applies **superheated vapor** only after the state, geometry, flow/thermal regime, and assumptions are defined.

24. **A.** The chapter applies **thermodynamic property diagram** only after the state, geometry, flow/thermal regime, and assumptions are defined.

25. **A.** The chapter applies **property interpolation** only after the state, geometry, flow/thermal regime, and assumptions are defined.

26. **A.** The chapter applies **pure substance** only after the state, geometry, flow/thermal regime, and assumptions are defined.

27. **A.** The chapter applies **saturation dome** only after the state, geometry, flow/thermal regime, and assumptions are defined.


---

## Practice Problems

1. A saturated mixture has x=0.30, hf=500 kJ/kg, hfg=2200 kJ/kg. Find h.

2. A mixture contains 2 kg vapor and 6 kg liquid. Find quality.

3. At fixed P, T is above Tsat. Identify region.

4. At fixed P, T is below Tsat. Identify region.

5. What is quality of saturated liquid?

6. What is quality of saturated vapor?

7. Can quality be used for superheated vapor?

8. Which diagram is especially convenient for vapor-compression refrigeration?

9. Which diagram makes reversible heat transfer appear as area under a curve?

10. What must be checked before linear interpolation in a property table?


---

## Practice Problem Solutions

1. h=500+0.30(2200)=1160 kJ/kg.

2. x=2/8=0.25.

3. Superheated vapor.

4. Compressed/subcooled liquid.

5. 0.

6. 1.

7. No.

8. P-h diagram.

9. T-s diagram.

10. Same phase region and same independent variables.


---

## Quick Reference

**Handbook anchor:** Thermodynamics, printed pp. 143–144 and property tables/diagrams in pp. 157–180.

- **pure substance:** Pure-Substance Phases and Saturation
- **saturation dome:** Saturation Dome and Critical Point
- **vapor quality:** Quality in the Two-Phase Region
- **saturated property table:** Using Saturated Property Tables
- **superheated vapor:** Superheated Vapor and Compressed Liquid
- **thermodynamic property diagram:** P-v, T-s, and P-h Diagrams
- **property interpolation:** Interpolation and State Consistency
---

## What's Next

**02-49 — Ideal Gases, Gas Mixtures, and Psychrometrics**

Carry forward the thermal-fluid workflow: define the state/control volume, identify property data and assumptions, apply conservation and constitutive relations, then verify units and physical limits.

— Your Mentor