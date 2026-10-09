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

**Solution.** Size tolerance is the upper minus lower limit: \(20.021-20.000=\mathbf{0.021\ mm}\). The nominal/basic size is not itself the tolerance.

---

## 90.2 Clearance, transition, and interference fits

Clearance fits always permit assembly clearance; interference fits always require interference; transition fits can produce either depending on actual sizes.

\[\text{clearance}=D_{hole}-d_{shaft}\]

![FIG-03-90-002: Clearance, transition, and interference tolerance-zone examples.](../figures/FIG-03-90-002-clearance-transition-and-interference-fits.png)

### Worked Example 2

**Problem.** A minimum hole larger than maximum shaft guarantees clearance.

**Solution.** If the minimum permissible hole is larger than the maximum permissible shaft, every allowed assembly has positive clearance, so the fit is guaranteed **clearance**. Overlapping tolerance zones permit transition; a shaft zone wholly above the hole zone gives interference.

---

## 90.3 Hole-basis system and IT grades

Hole-basis fits keep the basic hole reference fixed while shaft tolerance positions create the desired fit. IT grade specifies tolerance magnitude by size range.

\[\text{H hole has fundamental lower deviation at the basic size}\]

![FIG-03-90-003: Annotated H7/g6, H7/k6, and H7/s6 examples on a tolerance-zone chart.](../figures/FIG-03-90-003-hole-basis-system-and-it-grades.png)

### Worked Example 3

**Problem.** 34H7/s6 identifies a 34-mm basic size, H7 hole, and s6 shaft.

**Solution.** In \(34H7/s6\), 34 mm is the basic size, H7 is the hole tolerance class, and s6 is the shaft class. In the ISO basic-hole system the H-hole lower deviation is at the basic size.

---

## 90.4 GD&T datums and feature control frames

GD&T communicates geometric design intent separately from size tolerances. Datums establish reference geometry for orientation and location controls.

\[\text{feature control frame}=\text{symbol+tolerance+modifiers+datum references}\]

![FIG-03-90-004: Mechanical drawing detail with datum features and annotated feature control frame.](../figures/FIG-03-90-004-gdandt-datums-and-feature-control-frames.png)

### Worked Example 4

**Problem.** A position tolerance referenced to A|B|C is interpreted relative to that datum reference frame.

**Solution.** A position tolerance referenced to A|B|C is evaluated relative to the datum reference frame established in that precedence order. The tolerance value cannot be interpreted independently of datum simulators, modifiers, and the controlled feature.

---

## 90.5 MMC, LMC, RFS, and virtual condition

Material-condition modifiers connect feature size to allowable geometric variation and functional assembly boundaries.

\[\text{external virtual condition}=\mathrm{MMC}+\text{geometric tolerance}\]

![FIG-03-90-005: Hole and shaft features illustrating MMC, LMC, RFS, bonus tolerance, and virtual condition.](../figures/FIG-03-90-005-mmc-lmc-rfs-and-virtual-condition.png)

### Worked Example 5

**Problem.** For a shaft, MMC is its largest permissible diameter.

**Solution.** For an external cylindrical feature, MMC is the **largest** allowed shaft diameter. Its external virtual condition combines the MMC size boundary with the applicable geometric tolerance according to the stated material-condition modifier.

---

## 90.6 Tolerance stack-up and manufacturability

Assembly variation accumulates from part dimensions. Worst-case stack-up guarantees limits but can be conservative; statistical methods require justified assumptions.

\[\Delta_{worst}\approx\sum |\Delta_i|\]

![FIG-03-90-006: Dimension chain through an assembly with worst-case and statistical tolerance concepts.](../figures/FIG-03-90-006-tolerance-stack-up-and-manufacturability.png)

### Worked Example 6

**Problem.** Three independent ±0.10-mm worst-case contributors can create ±0.30-mm stack range.

**Solution.** Worst-case stack-up adds absolute contributors: \(\pm0.10\pm0.10\pm0.10\ {\rm mm}\) gives a possible total of \(\mathbf{\pm0.30\ mm}\). Thus the maximum magnitude of the accumulated worst-case variation is **0.30 mm**. Statistical stack methods require an explicit statistical basis and are not the same as worst-case.

---

## 90.7 Quality, reliability, drawing interpretation, and release checks

A mechanical drawing must communicate geometry, materials, tolerances, finishes, interfaces, and inspection intent. Quality and reliability close the loop between design assumptions and production/service performance.

\[\text{release requires function+strength+fit+manufacturability+inspection+reliability}\]

![FIG-03-90-007: Drawing-to-production release checklist linking CAD/drawing, tolerances, process capability, inspection, reliability, and configuration control.](../figures/FIG-03-90-007-quality-reliability-drawing-interpretation-and-release-checks.png)

### Worked Example 7

**Problem.** A dimensioned part can still be unreleasable if datums, material, finish, or inspection requirements are ambiguous.

**Solution.** A part is not ready for release merely because nominal dimensions exist. Datums/GD&T, material and heat treatment, surface finish, fit/tolerance intent, inspection method, manufacturability, special processes, reliability/safety requirements, and configuration status must be unambiguous.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. A dimension or tolerance solution is invalid if its fit/GD&T interpretation conflicts with the datum scheme, material condition, manufacturability, or inspection method. Product definition must be internally consistent.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **SHIGLEY, Y145, ISO286** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 14; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Nisbett, K. J., & Budynas, R. G. *Shigley's Mechanical Engineering Design* (2024 Release). McGraw Hill. ISBN 978-1-265-47269-6. Supporting scope: Failure theories, fatigue, springs, pressure-vessel screening, bearings, fasteners, shafts, keys, couplings, gears, and machine-element design.
- ASME. (2018, reaffirmed 2024). *Dimensioning and Tolerancing* (ASME Y14.5-2018 (R2024)). Supporting scope: GD&T symbols, datums, feature control frames, material-condition modifiers, and product-definition tolerancing.
- ISO. (2010). *Geometrical product specifications (GPS)—ISO code system for tolerances on linear sizes—Part 1: Basis of tolerances, deviations and fits* (ISO 286-1:2010; confirmed current in 2026). Supporting scope: Basic size, deviations, tolerance classes, fits, basic-hole and basic-shaft systems.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability**, start from the physical model and system/component state, not from an isolated formula. A valid solution must separate size tolerance from allowance, classify the fit from limit sizes, construct the correct datum/GD&T interpretation, evaluate MMC/LMC/RFS correctly, and close tolerance stacks against functional/manufacturing limits.

16. Units and sign/reference conventions are part of the model in **Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability**. External sources **SHIGLEY, Y145, ISO286** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: make shaft and hole tolerance zones identical at the same limits and confirm zero nominal clearance at coincident sizes; set every stack contributor to zero and confirm total stack variation is zero. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §90.1, **Basic size, deviations, tolerance, and allowance**, uses \(\Delta D=D_{max}-D_{min}\). Apply it only under the geometry/material/operating assumptions stated in §90.1, then compare the result with the physical behavior described there.

20. **A.** Section §90.2, **Clearance, transition, and interference fits**, uses \(\text{clearance}=D_{hole}-d_{shaft}\). Apply it only under the geometry/material/operating assumptions stated in §90.2, then compare the result with the physical behavior described there.

21. **A.** Section §90.3, **Hole-basis system and IT grades**, uses \(\text{H hole has fundamental lower deviation at the basic size}\). Apply it only under the geometry/material/operating assumptions stated in §90.3, then compare the result with the physical behavior described there.

22. **A.** Section §90.4, **GD&T datums and feature control frames**, uses \(\text{feature control frame}=\text{symbol+tolerance+modifiers+datum references}\). Apply it only under the geometry/material/operating assumptions stated in §90.4, then compare the result with the physical behavior described there.

23. **A.** Section §90.5, **MMC, LMC, RFS, and virtual condition**, uses \(\text{external virtual condition}=\mathrm{MMC}+\text{geometric tolerance}\). Apply it only under the geometry/material/operating assumptions stated in §90.5, then compare the result with the physical behavior described there.

24. **A.** Section §90.6, **Tolerance stack-up and manufacturability**, uses \(\Delta_{worst}\approx\sum |\Delta_i|\). Apply it only under the geometry/material/operating assumptions stated in §90.6, then compare the result with the physical behavior described there.

25. **A.** Section §90.7, **Quality, reliability, drawing interpretation, and release checks**, uses \(\text{release requires function+strength+fit+manufacturability+inspection+reliability}\). Apply it only under the geometry/material/operating assumptions stated in §90.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **SHIGLEY, Y145, ISO286**; guide synthesis is supplemental explanation and exam-oriented workflow.


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

1. **Independent check for §90.1 — Basic size, deviations, tolerance, and allowance.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Size tolerance is the upper minus lower limit: \(20.021-20.000=\mathbf{0.021\ mm}\). The nominal/basic size is not itself the tolerance.

2. **Independent check for §90.2 — Clearance, transition, and interference fits.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. If the minimum permissible hole is larger than the maximum permissible shaft, every allowed assembly has positive clearance, so the fit is guaranteed **clearance**. Overlapping tolerance zones permit transition; a shaft zone wholly above the hole zone gives interference.

3. **Independent check for §90.3 — Hole-basis system and IT grades.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. In \(34H7/s6\), 34 mm is the basic size, H7 is the hole tolerance class, and s6 is the shaft class. In the ISO basic-hole system the H-hole lower deviation is at the basic size.

4. **Independent check for §90.4 — GD&T datums and feature control frames.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A position tolerance referenced to A|B|C is evaluated relative to the datum reference frame established in that precedence order. The tolerance value cannot be interpreted independently of datum simulators, modifiers, and the controlled feature.

5. **Independent check for §90.5 — MMC, LMC, RFS, and virtual condition.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For an external cylindrical feature, MMC is the **largest** allowed shaft diameter. Its external virtual condition combines the MMC size boundary with the applicable geometric tolerance according to the stated material-condition modifier.

6. **Independent check for §90.6 — Tolerance stack-up and manufacturability.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Worst-case stack-up adds absolute contributors: \(\pm0.10\pm0.10\pm0.10\ {\rm mm}\) gives a possible total of \(\mathbf{\pm0.30\ mm}\). Statistical stack methods require an explicit statistical basis and are not the same as worst-case.

7. **Independent check for §90.7 — Quality, reliability, drawing interpretation, and release checks.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A part is not ready for release merely because nominal dimensions exist. Datums/GD&T, material and heat treatment, surface finish, fit/tolerance intent, inspection method, manufacturability, special processes, reliability/safety requirements, and configuration status must be unambiguous.

8. For **Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability**, one required acceptance screen is: separate size tolerance from allowance, classify the fit from limit sizes, construct the correct datum/GD&T interpretation, evaluate MMC/LMC/RFS correctly, and close tolerance stacks against functional/manufacturing limits. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability**. For `split_required` concepts, use **SHIGLEY, Y145, ISO286** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: make shaft and hole tolerance zones identical at the same limits and confirm zero nominal clearance at coincident sizes; set every stack contributor to zero and confirm total stack variation is zero. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

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
