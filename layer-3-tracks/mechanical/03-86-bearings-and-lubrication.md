---
chapter: "03-86"
title: "Bearings and Lubrication"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-086-01, MEC-3-086-02, MEC-3-086-03, MEC-3-086-04, MEC-3-086-05, MEC-3-086-06, MEC-3-086-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-86: Bearings and Lubrication

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MEC-3-078-07 · MAT-2B-016-01

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Bearings and Lubrication**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **86.1** Explain and apply **Bearing types and load directions**.
* **86.2** Explain and apply **Basic dynamic load rating and L10 life**.
* **86.3** Explain and apply **Equivalent radial bearing load**.
* **86.4** Explain and apply **Bearing life conversion from revolutions to hours**.
* **86.5** Explain and apply **Lubrication regimes**.
* **86.6** Explain and apply **Journal-bearing concepts**.
* **86.7** Explain and apply **Bearing failure, fits, mounting, and service checks**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 86.1 Bearing types and load directions

Rolling-element, journal, thrust, and specialty bearings support different load/speed regimes. Selection starts with load direction and operating conditions.

\[\text{bearing choice}=f(\text{radial load, thrust, speed, life, stiffness, environment})\]

![FIG-03-86-001: Ball, roller, thrust, and journal bearings with principal load directions.](../figures/FIG-03-86-001-bearing-types-and-load-directions.png)

### Worked Example 1

**Problem.** A deep-groove ball bearing can support radial load and some axial load, unlike a pure radial journal bearing concept.

**Solution.** A deep-groove ball bearing can carry substantial radial load plus some thrust load, whereas a plain journal-bearing model is primarily radial. Bearing family selection must match radial/thrust load, speed, required life, stiffness, environment, and lubrication.

---

## 86.2 Basic dynamic load rating and L10 life

The Handbook defines the basic dynamic rating associated with 90% survival to the specified life basis. Exponent a differs for ball and roller bearings.

\[C=P L^{1/a}\]

![FIG-03-86-002: Bearing life distribution with L10 concept and load-life relation.](../figures/FIG-03-86-002-basic-dynamic-load-rating-and-l10-life.png)

### Worked Example 2

**Problem.** For the same P and life, roller and ball bearing rating relations use different exponents.

**Solution.** Basic rating life and dynamic rating are related by \(C=P L^{1/a}\) when \(L\) is on the required normalized basis. Ball and roller bearings use different life exponents, so the same \(P,L\) do not imply the same required \(C\).

---

## 86.3 Equivalent radial bearing load

Combined radial and axial load is converted to an equivalent radial load using factors tied to bearing type and load ratio.

\[P_{eq}=XVF_r+YF_a\]

![FIG-03-86-003: Ball bearing with Fr, Fa, rotating ring factor V, and equivalent load calculation.](../figures/FIG-03-86-003-equivalent-radial-bearing-load.png)

### Worked Example 3

**Problem.** If axial load is negligible under the applicable criterion, X=1 and Y=0 for the cited deep-groove relation.

**Solution.** When the applicable deep-groove criterion makes thrust negligible, \(X=1\) and \(Y=0\), so \(P_{eq}=VF_r\) (and \(P_{eq}=F_r\) if \(V=1\)). Do not discard axial load unless the specified bearing relation permits it.

---

## 86.4 Bearing life conversion from revolutions to hours

Bearing life often comes from operating hours and shaft speed. Convert to millions of revolutions before using the Handbook rating equation.

\[L_{rev}=60n\,L_h\]

![FIG-03-86-004: RPM and operating-hour timeline converted to total and million revolutions.](../figures/FIG-03-86-004-bearing-life-conversion-from-revolutions-to-hours.png)

### Worked Example 4

**Problem.** At 1200 rpm for 10,000 h, life is 720 million revolutions.

**Solution.** \(L_{rev}=60nL_h=60(1200\ {\rm rev/min})(10{,}000\ {\rm h})=\mathbf{720{,}000{,}000\ rev}\), or **720 million revolutions**.

---

## 86.5 Lubrication regimes

Boundary, mixed, hydrodynamic, and elastohydrodynamic lubrication represent increasing separation of surfaces. Viscosity selection depends on speed, load, temperature, and bearing type.

\[\text{film thickness/roughness and speed-load-viscosity determine regime}\]

![FIG-03-86-005: Stribeck-style friction curve labeling boundary, mixed, and full-film lubrication regimes.](../figures/FIG-03-86-005-lubrication-regimes.png)

### Worked Example 5

**Problem.** Higher temperature generally lowers oil viscosity, which can reduce film thickness.

**Solution.** Oil viscosity normally decreases as temperature rises. Lower viscosity can reduce hydrodynamic/elastohydrodynamic film thickness, making surface roughness and mixed/boundary lubrication more important under the same speed/load.

---

## 86.6 Journal-bearing concepts

Hydrodynamic journal bearings develop a pressure wedge from relative motion and converging film geometry.

\[\text{load supported by pressure generated in the lubricant film}\]

![FIG-03-86-006: Journal bearing cross-section with eccentric shaft, converging oil film, pressure distribution, and rotation.](../figures/FIG-03-86-006-journal-bearing-concepts.png)

### Worked Example 6

**Problem.** A stationary shaft does not generate the same hydrodynamic pressure wedge as a rotating shaft under otherwise similar conditions.

**Solution.** A hydrodynamic journal bearing develops pressure from relative surface motion and a converging lubricant wedge. With the shaft stationary, that self-generated pressure mechanism is absent; only externally supplied/static effects remain.

---

## 86.7 Bearing failure, fits, mounting, and service checks

Bearing design also checks static load, speed limit, lubrication, contamination, alignment, fits, temperature, and installation.

\[\text{life calculation is only one part of bearing suitability}\]

![FIG-03-86-007: Bearing failure modes montage: spalling, contamination, overheating, misalignment, and poor mounting.](../figures/FIG-03-86-007-bearing-failure-fits-mounting-and-service-checks.png)

### Worked Example 7

**Problem.** A bearing with adequate calculated L10 life can still fail early from contamination or incorrect fit.

**Solution.** Calculated L10 life addresses rolling-fatigue probability under the rating model, not every failure cause. Contamination, poor lubrication, mounting damage, electrical erosion, misalignment, overload, or incorrect fit can cause much earlier service failure.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. Bearing rating life is only one suitability check. A selection that violates speed, lubrication, fit, load direction, contamination, or mounting conditions must be changed even if L10 life is numerically adequate.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Bearings and Lubrication**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **SHIGLEY, ISO281** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 14; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Nisbett, K. J., & Budynas, R. G. *Shigley's Mechanical Engineering Design* (2024 Release). McGraw Hill. ISBN 978-1-265-47269-6. Supporting scope: Failure theories, fatigue, springs, pressure-vessel screening, bearings, fasteners, shafts, keys, couplings, gears, and machine-element design.
- ISO. (2007). *Rolling bearings—Dynamic load ratings and rating life* (ISO 281:2007; confirmed current by ISO in 2021). Supporting scope: Basic dynamic load ratings and basic rating life of rolling bearings.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using bearing selection outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using bearing L10 life outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using equivalent bearing load outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using bearing life hours outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using lubrication regime outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using journal bearing outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using bearing service check outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| bearing selection | Concept developed in §86.1; apply with that section's geometry and operating assumptions. |
| bearing L10 life | Concept developed in §86.2; apply with that section's geometry and operating assumptions. |
| equivalent bearing load | Concept developed in §86.3; apply with that section's geometry and operating assumptions. |
| bearing life hours | Concept developed in §86.4; apply with that section's geometry and operating assumptions. |
| lubrication regime | Concept developed in §86.5; apply with that section's geometry and operating assumptions. |
| journal bearing | Concept developed in §86.6; apply with that section's geometry and operating assumptions. |
| bearing service check | Concept developed in §86.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **bearing selection** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **bearing L10 life** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **equivalent bearing load** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **bearing life hours** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **lubrication regime** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **journal bearing** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **bearing service check** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **bearing selection**?

9. What geometric, material, operating, or model assumption must be checked before applying **bearing L10 life**?

10. What geometric, material, operating, or model assumption must be checked before applying **equivalent bearing load**?

11. What geometric, material, operating, or model assumption must be checked before applying **bearing life hours**?

12. What geometric, material, operating, or model assumption must be checked before applying **lubrication regime**?

13. What geometric, material, operating, or model assumption must be checked before applying **journal bearing**?

14. What geometric, material, operating, or model assumption must be checked before applying **bearing service check**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **bearing selection**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **bearing L10 life**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **equivalent bearing load**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **bearing life hours**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **lubrication regime**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **journal bearing**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **bearing service check**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **bearing selection**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **bearing L10 life**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **bearing selection** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **bearing L10 life** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **equivalent bearing load** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **bearing life hours** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **lubrication regime** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **journal bearing** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **bearing service check** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **bearing selection**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **bearing L10 life**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **equivalent bearing load**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **bearing life hours**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **lubrication regime**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **journal bearing**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **bearing service check**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

15. In **Bearings and Lubrication**, start from the physical model and system/component state, not from an isolated formula. A valid solution must match bearing type to radial/thrust load and speed, use the correct equivalent load and life exponent, and check lubrication, fit, contamination, and mounting.

16. Units and sign/reference conventions are part of the model in **Bearings and Lubrication**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Bearings and Lubrication**. External sources **SHIGLEY, ISO281** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: let axial load become negligible and confirm the stated equivalent-load relation reduces to radial loading; set MTBF-style service hours to zero and confirm accumulated bearing revolutions are zero. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §86.1, **Bearing types and load directions**, uses \(\text{bearing choice}=f(\text{radial load, thrust, speed, life, stiffness, environment})\). Apply it only under the geometry/material/operating assumptions stated in §86.1, then compare the result with the physical behavior described there.

20. **A.** Section §86.2, **Basic dynamic load rating and L10 life**, uses \(C=P L^{1/a}\). Apply it only under the geometry/material/operating assumptions stated in §86.2, then compare the result with the physical behavior described there.

21. **A.** Section §86.3, **Equivalent radial bearing load**, uses \(P_{eq}=XVF_r+YF_a\). Apply it only under the geometry/material/operating assumptions stated in §86.3, then compare the result with the physical behavior described there.

22. **A.** Section §86.4, **Bearing life conversion from revolutions to hours**, uses \(L_{rev}=60n\,L_h\). Apply it only under the geometry/material/operating assumptions stated in §86.4, then compare the result with the physical behavior described there.

23. **A.** Section §86.5, **Lubrication regimes**, uses \(\text{film thickness/roughness and speed-load-viscosity determine regime}\). Apply it only under the geometry/material/operating assumptions stated in §86.5, then compare the result with the physical behavior described there.

24. **A.** Section §86.6, **Journal-bearing concepts**, uses \(\text{load supported by pressure generated in the lubricant film}\). Apply it only under the geometry/material/operating assumptions stated in §86.6, then compare the result with the physical behavior described there.

25. **A.** Section §86.7, **Bearing failure, fits, mounting, and service checks**, uses \(\text{life calculation is only one part of bearing suitability}\). Apply it only under the geometry/material/operating assumptions stated in §86.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Bearings and Lubrication** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **SHIGLEY, ISO281**; guide synthesis is supplemental explanation and exam-oriented workflow.


---

## Practice Problems

1. A deep-groove ball bearing can support radial load and some axial load, unlike a pure radial journal bearing concept.

2. For the same P and life, roller and ball bearing rating relations use different exponents.

3. If axial load is negligible under the applicable criterion, X=1 and Y=0 for the cited deep-groove relation.

4. At 1200 rpm for 10,000 h, life is 720 million revolutions.

5. Higher temperature generally lowers oil viscosity, which can reduce film thickness.

6. A stationary shaft does not generate the same hydrodynamic pressure wedge as a rotating shaft under otherwise similar conditions.

7. A bearing with adequate calculated L10 life can still fail early from contamination or incorrect fit.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. **Independent check for §86.1 — Bearing types and load directions.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A deep-groove ball bearing can carry substantial radial load plus some thrust load, whereas a plain journal-bearing model is primarily radial. Bearing family selection must match radial/thrust load, speed, required life, stiffness, environment, and lubrication.

2. **Independent check for §86.2 — Basic dynamic load rating and L10 life.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Basic rating life and dynamic rating are related by \(C=P L^{1/a}\) when \(L\) is on the required normalized basis. Ball and roller bearings use different life exponents, so the same \(P,L\) do not imply the same required \(C\).

3. **Independent check for §86.3 — Equivalent radial bearing load.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. When the applicable deep-groove criterion makes thrust negligible, \(X=1\) and \(Y=0\), so \(P_{eq}=VF_r\) (and \(P_{eq}=F_r\) if \(V=1\)). Do not discard axial load unless the specified bearing relation permits it.

4. **Independent check for §86.4 — Bearing life conversion from revolutions to hours.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(L_{rev}=60nL_h=60(1200\ {\rm rev/min})(10{,}000\ {\rm h})=\mathbf{720{,}000{,}000\ rev}\), or **720 million revolutions**.

5. **Independent check for §86.5 — Lubrication regimes.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Oil viscosity normally decreases as temperature rises. Lower viscosity can reduce hydrodynamic/elastohydrodynamic film thickness, making surface roughness and mixed/boundary lubrication more important under the same speed/load.

6. **Independent check for §86.6 — Journal-bearing concepts.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A hydrodynamic journal bearing develops pressure from relative surface motion and a converging lubricant wedge. With the shaft stationary, that self-generated pressure mechanism is absent; only externally supplied/static effects remain.

7. **Independent check for §86.7 — Bearing failure, fits, mounting, and service checks.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Calculated L10 life addresses rolling-fatigue probability under the rating model, not every failure cause. Contamination, poor lubrication, mounting damage, electrical erosion, misalignment, overload, or incorrect fit can cause much earlier service failure.

8. For **Bearings and Lubrication**, one required acceptance screen is: match bearing type to radial/thrust load and speed, use the correct equivalent load and life exponent, and check lubrication, fit, contamination, and mounting. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Bearings and Lubrication**. For `split_required` concepts, use **SHIGLEY, ISO281** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: let axial load become negligible and confirm the stated equivalent-load relation reduces to radial loading; set MTBF-style service hours to zero and confirm accumulated bearing revolutions are zero. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 14.

- **bearing selection:** Bearing types and load directions
- **bearing L10 life:** Basic dynamic load rating and L10 life
- **equivalent bearing load:** Equivalent radial bearing load
- **bearing life hours:** Bearing life conversion from revolutions to hours
- **lubrication regime:** Lubrication regimes
- **journal bearing:** Journal-bearing concepts
- **bearing service check:** Bearing failure, fits, mounting, and service checks

---

## What's Next

**Chapter 03-87: Power Screws, Threaded Fasteners, and Mechanical Joints**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
