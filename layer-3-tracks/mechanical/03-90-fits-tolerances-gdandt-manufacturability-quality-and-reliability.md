---
chapter: "03-90"
title: "Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-090-01, MEC-3-090-02, MEC-3-090-03, MEC-3-090-04, MEC-3-090-05, MEC-3-090-06, MEC-3-090-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-90: Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MEC-3-079-07 · MEC-3-086-07 · MATH-1A-001-01

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **90.1** Explain and apply **Basic size, deviations, tolerance, and allowance**.
* **90.2** Explain and apply **Clearance, transition, and interference fits**.
* **90.3** Explain and apply **Hole-basis system and IT grades**.
* **90.4** Explain and apply **GD&T datums and feature control frames**.
* **90.5** Explain and apply **MMC, LMC, RFS, and virtual condition**.
* **90.6** Explain and apply **Tolerance stack-up and manufacturability**.
* **90.7** Explain and apply **Quality, reliability, drawing interpretation, and release checks**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 90.1 Basic size, deviations, tolerance, and allowance

Limits and fits define acceptable size variation around a basic size. Upper/lower deviations locate the tolerance zone relative to nominal size.

\[\Delta D=D_{max}-D_{min}\]

![FIG-03-90-001: Hole and shaft tolerance zones around the basic-size zero line.](../figures/FIG-03-90-001-basic-size-deviations-tolerance-and-allowance.png)

### Worked Example 1

**Problem.** A hole from 20.000 to 20.021 mm has 0.021-mm size tolerance.

**Solution.** Apply the relation and model in §90.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 90.2 Clearance, transition, and interference fits

Clearance fits always permit assembly clearance; interference fits always require interference; transition fits can produce either depending on actual sizes.

\[\text{clearance}=D_{hole}-d_{shaft}\]

![FIG-03-90-002: Clearance, transition, and interference tolerance-zone examples.](../figures/FIG-03-90-002-clearance-transition-and-interference-fits.png)

### Worked Example 2

**Problem.** A minimum hole larger than maximum shaft guarantees clearance.

**Solution.** Apply the relation and model in §90.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 90.3 Hole-basis system and IT grades

Hole-basis fits keep the basic hole reference fixed while shaft tolerance positions create the desired fit. IT grade specifies tolerance magnitude by size range.

\[\text{H hole has fundamental lower deviation at the basic size}\]

![FIG-03-90-003: Annotated H7/g6, H7/k6, and H7/s6 examples on a tolerance-zone chart.](../figures/FIG-03-90-003-hole-basis-system-and-it-grades.png)

### Worked Example 3

**Problem.** 34H7/s6 identifies a 34-mm basic size, H7 hole, and s6 shaft.

**Solution.** Apply the relation and model in §90.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 90.4 GD&T datums and feature control frames

GD&T communicates geometric design intent separately from size tolerances. Datums establish reference geometry for orientation and location controls.

\[\text{feature control frame}=\text{symbol+tolerance+modifiers+datum references}\]

![FIG-03-90-004: Mechanical drawing detail with datum features and annotated feature control frame.](../figures/FIG-03-90-004-gdandt-datums-and-feature-control-frames.png)

### Worked Example 4

**Problem.** A position tolerance referenced to A|B|C is interpreted relative to that datum reference frame.

**Solution.** Apply the relation and model in §90.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 90.5 MMC, LMC, RFS, and virtual condition

Material-condition modifiers connect feature size to allowable geometric variation and functional assembly boundaries.

\[\text{external virtual condition}=\mathrm{MMC}+\text{geometric tolerance}\]

![FIG-03-90-005: Hole and shaft features illustrating MMC, LMC, RFS, bonus tolerance, and virtual condition.](../figures/FIG-03-90-005-mmc-lmc-rfs-and-virtual-condition.png)

### Worked Example 5

**Problem.** For a shaft, MMC is its largest permissible diameter.

**Solution.** Apply the relation and model in §90.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 90.6 Tolerance stack-up and manufacturability

Assembly variation accumulates from part dimensions. Worst-case stack-up guarantees limits but can be conservative; statistical methods require justified assumptions.

\[\Delta_{worst}\approx\sum |\Delta_i|\]

![FIG-03-90-006: Dimension chain through an assembly with worst-case and statistical tolerance concepts.](../figures/FIG-03-90-006-tolerance-stack-up-and-manufacturability.png)

### Worked Example 6

**Problem.** Three independent ±0.10-mm worst-case contributors can create ±0.30-mm stack range.

**Solution.** Apply the relation and model in §90.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 90.7 Quality, reliability, drawing interpretation, and release checks

A mechanical drawing must communicate geometry, materials, tolerances, finishes, interfaces, and inspection intent. Quality and reliability close the loop between design assumptions and production/service performance.

\[\text{release requires function+strength+fit+manufacturability+inspection+reliability}\]

![FIG-03-90-007: Drawing-to-production release checklist linking CAD/drawing, tolerances, process capability, inspection, reliability, and configuration control.](../figures/FIG-03-90-007-quality-reliability-drawing-interpretation-and-release-checks.png)

### Worked Example 7

**Problem.** A dimensioned part can still be unreleasable if datums, material, finish, or inspection requirements are ambiguous.

**Solution.** Apply the relation and model in §90.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

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

Primary source basis: **FE Mechanical specification Area(s) 14; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** The Mechanical specification includes both directly tabulated Handbook equations and learned design concepts. This chapter does not assign invented Handbook pages to specification-required material that is not directly tabulated.

---

## Where This Goes Wrong

**Using limits and fits outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using fit class outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using hole-basis fit outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using geometric dimensioning and tolerancing outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using maximum material condition outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using tolerance stack-up outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using mechanical design release check outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| limits and fits | Concept developed in §90.1; apply with that section's geometry and operating assumptions. |
| fit class | Concept developed in §90.2; apply with that section's geometry and operating assumptions. |
| hole-basis fit | Concept developed in §90.3; apply with that section's geometry and operating assumptions. |
| geometric dimensioning and tolerancing | Concept developed in §90.4; apply with that section's geometry and operating assumptions. |
| maximum material condition | Concept developed in §90.5; apply with that section's geometry and operating assumptions. |
| tolerance stack-up | Concept developed in §90.6; apply with that section's geometry and operating assumptions. |
| mechanical design release check | Concept developed in §90.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **limits and fits** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **fit class** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **hole-basis fit** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **geometric dimensioning and tolerancing** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **maximum material condition** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **tolerance stack-up** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **mechanical design release check** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **limits and fits**?

9. What geometric, material, operating, or model assumption must be checked before applying **fit class**?

10. What geometric, material, operating, or model assumption must be checked before applying **hole-basis fit**?

11. What geometric, material, operating, or model assumption must be checked before applying **geometric dimensioning and tolerancing**?

12. What geometric, material, operating, or model assumption must be checked before applying **maximum material condition**?

13. What geometric, material, operating, or model assumption must be checked before applying **tolerance stack-up**?

14. What geometric, material, operating, or model assumption must be checked before applying **mechanical design release check**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **limits and fits**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **fit class**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **hole-basis fit**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **geometric dimensioning and tolerancing**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **maximum material condition**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **tolerance stack-up**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **mechanical design release check**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **limits and fits**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **fit class**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **limits and fits** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **fit class** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **hole-basis fit** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **geometric dimensioning and tolerancing** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **maximum material condition** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **tolerance stack-up** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **mechanical design release check** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **limits and fits**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **fit class**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **hole-basis fit**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **geometric dimensioning and tolerancing**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **maximum material condition**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **tolerance stack-up**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **mechanical design release check**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

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

1. A hole from 20.000 to 20.021 mm has 0.021-mm size tolerance.

2. A minimum hole larger than maximum shaft guarantees clearance.

3. 34H7/s6 identifies a 34-mm basic size, H7 hole, and s6 shaft.

4. A position tolerance referenced to A|B|C is interpreted relative to that datum reference frame.

5. For a shaft, MMC is its largest permissible diameter.

6. Three independent ±0.10-mm worst-case contributors can create ±0.30-mm stack range.

7. A dimensioned part can still be unreleasable if datums, material, finish, or inspection requirements are ambiguous.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. Use §90.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §90.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §90.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §90.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §90.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §90.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §90.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 14, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 14.

- **limits and fits:** Basic size, deviations, tolerance, and allowance
- **fit class:** Clearance, transition, and interference fits
- **hole-basis fit:** Hole-basis system and IT grades
- **geometric dimensioning and tolerancing:** GD&T datums and feature control frames
- **maximum material condition:** MMC, LMC, RFS, and virtual condition
- **tolerance stack-up:** Tolerance stack-up and manufacturability
- **mechanical design release check:** Quality, reliability, drawing interpretation, and release checks

---

## What's Next

**Other Disciplines integration track begins at 03-91**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
