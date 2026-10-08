---
chapter: "03-28"
title: "Shear Strength, Earth Pressure, Bearing Capacity, Foundations, Settlement, and Slope Stability"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-028-01, CIV-3-028-02, CIV-3-028-03, CIV-3-028-04, CIV-3-028-05, CIV-3-028-06, CIV-3-028-07]
routes: [civil]
status: drafted
---

# Chapter 03-28: Shear Strength, Earth Pressure, Bearing Capacity, Foundations, Settlement, and Slope Stability

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-027-07

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Shear Strength, Earth Pressure, Bearing Capacity, Foundations, Settlement, and Slope Stability**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **28.1** Explain and apply **Mohr-Coulomb shear strength**.
* **28.2** Explain and apply **At-rest, active, and passive earth pressure**.
* **28.3** Explain and apply **Retaining-wall stability checks**.
* **28.4** Explain and apply **Ultimate bearing capacity and allowable pressure**.
* **28.5** Explain and apply **Foundation types and load transfer**.
* **28.6** Explain and apply **Consolidation and settlement**.
* **28.7** Explain and apply **Slope stability and stabilization**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 28.1 Mohr-Coulomb shear strength

Shear strength depends on effective normal stress, cohesion intercept, and friction angle for the Mohr-Coulomb model.

\[\tau_f=c'+\sigma'\tan\phi'\]

![FIG-03-28-001: Shear stress versus effective normal stress with Mohr-Coulomb failure envelope and Mohr circle.](../figures/FIG-03-28-001-mohr-coulomb-shear-strength.png)

### Worked Example 1

**Problem.** If c'=0, σ'=100 kPa, φ'=30°, τf≈57.7 kPa.

**Solution.** Use the Mohr-Coulomb relation \(\tau_f=c'+\sigma'\tan\phi'\). With \(c'=0\), \(\sigma'=100\ \text{kPa}\), and \(\phi'=30^\circ\), \(\tau_f=100\tan30^\circ=57.7\ \text{kPa}\).

---

## 28.2 At-rest, active, and passive earth pressure

Lateral earth pressure depends on wall movement and soil state. Active pressure is mobilized by wall movement away from soil; passive by movement into soil.

\[\sigma_h=K\,\sigma'_v\]

![FIG-03-28-002: Retaining wall with at-rest, active, and passive pressure diagrams and wall movement directions.](../figures/FIG-03-28-002-at-rest-active-and-passive-earth-pressure.png)

### Worked Example 2

**Problem.** Use the K value corresponding to at-rest, active, or passive condition.

**Solution.** Earth-pressure coefficient selection depends on wall movement and boundary condition. Use \(K_0\) for at-rest conditions, \(K_a\) when sufficient movement mobilizes active conditions, and \(K_p\) when movement into the soil mobilizes passive resistance. Selecting the wrong state can dominate the error.

---

## 28.3 Retaining-wall stability checks

Retaining structures are checked for sliding, overturning, bearing, and global stability. Water pressure can materially change demand.

\[FS=\frac{\text{resisting effect}}{\text{driving effect}}\]

![FIG-03-28-003: Retaining wall free-body diagram with soil pressure, surcharge, weight, base reaction, sliding, and overturning checks.](../figures/FIG-03-28-003-retaining-wall-stability-checks.png)

### Worked Example 3

**Problem.** For overturning, compare resisting moments with overturning moments about the toe.

**Solution.** For overturning stability, choose a consistent pivot—commonly the toe—and sum resisting and overturning moments about that point. A factor of safety may be formed as \(FS=M_R/M_O\); forces passing through the toe have no moment about that pivot.

---

## 28.4 Ultimate bearing capacity and allowable pressure

Bearing capacity limits shear failure beneath foundations. The exact qult relation depends on foundation geometry, depth, soil, and provided factors.

\[q_{allow}=\frac{q_{ult}}{FS}\]

![FIG-03-28-004: Shallow footing with general shear failure zones and q_ult/q_allow labels.](../figures/FIG-03-28-004-ultimate-bearing-capacity-and-allowable-pressure.png)

### Worked Example 4

**Problem.** If qult=600 kPa and FS=3, qallow=200 kPa.

**Solution.** Allowable bearing pressure is ultimate capacity divided by the specified factor of safety. Thus \(q_{allow}=600/3=200\ \text{kPa}\). This value must be distinguished from net versus gross bearing pressure if the problem defines those separately.

---

## 28.5 Foundation types and load transfer

Spread footings, mats, wall footings, and deep foundations transfer load differently. Selection depends on load, soil profile, settlement, constructability, and groundwater.

\[q=\frac{P}{A}\]

![FIG-03-28-005: Comparative sketches of isolated footing, strip footing, mat, driven pile, and drilled shaft.](../figures/FIG-03-28-005-foundation-types-and-load-transfer.png)

### Worked Example 5

**Problem.** A 900-kN column on a 9 m² footing applies 100 kPa average contact pressure.

**Solution.** Average footing contact pressure is \(q=P/A\). With \(P=900\ \text{kN}\) and \(A=9\ \text{m}^2\), \(q=100\ \text{kN/m}^2=100\ \text{kPa}\).

---

## 28.6 Consolidation and settlement

Settlement can include immediate, primary consolidation, and secondary components. Differential settlement often matters more structurally than uniform settlement.

\[S=S_i+S_c+S_s\]

![FIG-03-28-006: Building footings over compressible layer showing uniform and differential settlement profiles.](../figures/FIG-03-28-006-consolidation-and-settlement.png)

### Worked Example 6

**Problem.** Two supports settling equally may cause little distortion; unequal settlement induces rotation and internal force.

**Solution.** Equal settlement of two supports produces translation with little relative distortion, whereas differential settlement changes the relative support elevations. That rotation or curvature can induce additional member forces and serviceability problems even when the total average settlement is modest.

---

## 28.7 Slope stability and stabilization

Slope stability depends on geometry, soil strength, groundwater, loading, and potential failure surface. Stabilization can alter geometry, drainage, reinforcement, or soil properties.

\[FS=\frac{\text{available shear resistance}}{\text{mobilized shear demand}}\]

![FIG-03-28-007: Slope with circular trial failure surface, slice forces, groundwater line, and stabilization measures.](../figures/FIG-03-28-007-slope-stability-and-stabilization.png)

### Worked Example 7

**Problem.** Lowering groundwater can improve effective stress and slope stability.

**Solution.** Lowering the groundwater table generally reduces pore-water pressure \(u\). Since effective stress is \(\sigma'=\sigma-u\), a reduction in \(u\) increases effective stress and can increase available shear strength, improving stability under otherwise comparable conditions.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a foundation/slope problem, compute effective stress first, then select the correct strength parameters and failure mechanism. Bearing, sliding, overturning, settlement, and slope stability are distinct checks; a satisfactory factor of safety in one mode does not guarantee acceptable performance in the others.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook relation that matches the stated geotechnical failure mode and drainage condition. Remembered bearing-capacity or earth-pressure formulas can differ in assumptions and factors, so the Handbook definitions and effective-stress basis should govern.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 12; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-028-03` — Das, B. M. (2024). *Principles of Foundation Engineering* (10th ed.). Cengage. ISBN 978-0-357-68465-8. Cited at publication/standard level; no page-level claim.
- `CIV-3-028-06` — Das, B. M. (2022). *Principles of Geotechnical Engineering* (10th ed.). Cengage. ISBN 978-0-357-42047-8. Cited at publication/standard level; no page-level claim. Das, B. M. (2024). *Principles of Foundation Engineering* (10th ed.). Cengage. ISBN 978-0-357-68465-8. Cited at publication/standard level; no page-level claim.
- `CIV-3-028-07` — Das, B. M. (2022). *Principles of Geotechnical Engineering* (10th ed.). Cengage. ISBN 978-0-357-42047-8. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

## Where This Goes Wrong

**Using soil shear strength without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using earth pressure state without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using retaining structure stability without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using bearing capacity without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using foundation selection without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using consolidation settlement without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using slope stability without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| soil shear strength | Concept developed in §28.1; apply with that section's stated assumptions and units. |
| earth pressure state | Concept developed in §28.2; apply with that section's stated assumptions and units. |
| retaining structure stability | Concept developed in §28.3; apply with that section's stated assumptions and units. |
| bearing capacity | Concept developed in §28.4; apply with that section's stated assumptions and units. |
| foundation selection | Concept developed in §28.5; apply with that section's stated assumptions and units. |
| consolidation settlement | Concept developed in §28.6; apply with that section's stated assumptions and units. |
| slope stability | Concept developed in §28.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **soil shear strength** and identify the principal quantity, relation, or decision it organizes.

2. Define **earth pressure state** and identify the principal quantity, relation, or decision it organizes.

3. Define **retaining structure stability** and identify the principal quantity, relation, or decision it organizes.

4. Define **bearing capacity** and identify the principal quantity, relation, or decision it organizes.

5. Define **foundation selection** and identify the principal quantity, relation, or decision it organizes.

6. Define **consolidation settlement** and identify the principal quantity, relation, or decision it organizes.

7. Define **slope stability** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **soil shear strength**?

9. What assumption or unit error is most likely to cause a wrong result when applying **earth pressure state**?

10. What assumption or unit error is most likely to cause a wrong result when applying **retaining structure stability**?

11. What assumption or unit error is most likely to cause a wrong result when applying **bearing capacity**?

12. What assumption or unit error is most likely to cause a wrong result when applying **foundation selection**?

13. What assumption or unit error is most likely to cause a wrong result when applying **consolidation settlement**?

14. What assumption or unit error is most likely to cause a wrong result when applying **slope stability**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **soil shear strength**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **earth pressure state**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **retaining structure stability**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **bearing capacity**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **foundation selection**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **consolidation settlement**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **slope stability**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept


26. Which check is most useful immediately before accepting a numerical answer?
A) Dimensional consistency and physical reasonableness
B) Replacing the stated geometry with a standard case
C) Dropping signs and directions
D) Assuming every quantity is SI

27. When a Civil specification topic is not fully tabulated in Handbook 10.6, the guide should:
A) Identify it as specification-required / learned material
B) Invent a Handbook page reference
C) Omit the topic
D) Treat it as optional


---

## Answer Key with Explanations

1. **soil shear strength** is developed in §28.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **earth pressure state** is developed in §28.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **retaining structure stability** is developed in §28.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **bearing capacity** is developed in §28.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **foundation selection** is developed in §28.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **consolidation settlement** is developed in §28.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **slope stability** is developed in §28.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **soil shear strength**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **earth pressure state**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **retaining structure stability**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **bearing capacity**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **foundation selection**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **consolidation settlement**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **slope stability**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. Sketch the retaining wall, footing, soil layers, groundwater, slope, and candidate failure surface before selecting earth-pressure, bearing, settlement, or stability equations.

16. Use the Handbook geotechnical relation that matches the drainage and failure mode because active/passive pressure, bearing capacity, and slope-stability models are not interchangeable.

17. Convert kPa, kN, kN/m, pcf, psf, feet, and meters consistently before computing stresses, resultants, moments, or factors of safety.

18. Check the failure mode separately: sliding, overturning, bearing, settlement, and slope stability each require a physically sensible resistance-to-demand result and none is automatically satisfied by another.

19. **A.** For **Mohr-Coulomb shear strength**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **At-rest, active, and passive earth pressure**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Retaining-wall stability checks**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Ultimate bearing capacity and allowable pressure**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Foundation types and load transfer**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Consolidation and settlement**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Slope stability and stabilization**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Shear Strength, Earth Pressure, Bearing Capacity, Foundations, Settlement, and Slope Stability, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Retaining-wall, settlement, and slope-stability detail beyond Handbook relations is labeled learned material and supported by the reconciled Das geotechnical/foundation references.



---

## Practice Problems

1. If c'=0, σ'=100 kPa, φ'=30°, τf≈57.7 kPa.

2. Use the K value corresponding to at-rest, active, or passive condition.

3. For overturning, compare resisting moments with overturning moments about the toe.

4. If qult=600 kPa and FS=3, qallow=200 kPa.

5. A 900-kN column on a 9 m² footing applies 100 kPa average contact pressure.

6. Two supports settling equally may cause little distortion; unequal settlement induces rotation and internal force.

7. Lowering groundwater can improve effective stress and slope stability.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. **Independent check for §28.1.** Rework the problem from the stated givens rather than copying the worked-example result. Use the Mohr-Coulomb relation \(\tau_f=c'+\sigma'\tan\phi'\). With \(c'=0\), \(\sigma'=100\ \text{kPa}\), and \(\phi'=30^\circ\), \(\tau_f=100\tan30^\circ=57.7\ \text{kPa}\). **Check:** confirm the final magnitude and units against the physical meaning of §28.1 before accepting the answer.



2. **Independent check for §28.2.** Rework the problem from the stated givens rather than copying the worked-example result. Earth-pressure coefficient selection depends on wall movement and boundary condition. Use \(K_0\) for at-rest conditions, \(K_a\) when sufficient movement mobilizes active conditions, and \(K_p\) when movement into the soil mobilizes passive resistance. Selecting the wrong state can dominate the error. **Check:** confirm the final magnitude and units against the physical meaning of §28.2 before accepting the answer.



3. **Independent check for §28.3.** Rework the problem from the stated givens rather than copying the worked-example result. For overturning stability, choose a consistent pivot—commonly the toe—and sum resisting and overturning moments about that point. A factor of safety may be formed as \(FS=M_R/M_O\); forces passing through the toe have no moment about that pivot. **Check:** confirm the final magnitude and units against the physical meaning of §28.3 before accepting the answer.



4. **Independent check for §28.4.** Rework the problem from the stated givens rather than copying the worked-example result. Allowable bearing pressure is ultimate capacity divided by the specified factor of safety. Thus \(q_{allow}=600/3=200\ \text{kPa}\). This value must be distinguished from net versus gross bearing pressure if the problem defines those separately. **Check:** confirm the final magnitude and units against the physical meaning of §28.4 before accepting the answer.



5. **Independent check for §28.5.** Rework the problem from the stated givens rather than copying the worked-example result. Average footing contact pressure is \(q=P/A\). With \(P=900\ \text{kN}\) and \(A=9\ \text{m}^2\), \(q=100\ \text{kN/m}^2=100\ \text{kPa}\). **Check:** confirm the final magnitude and units against the physical meaning of §28.5 before accepting the answer.



6. **Independent check for §28.6.** Rework the problem from the stated givens rather than copying the worked-example result. Equal settlement of two supports produces translation with little relative distortion, whereas differential settlement changes the relative support elevations. That rotation or curvature can induce additional member forces and serviceability problems even when the total average settlement is modest. **Check:** confirm the final magnitude and units against the physical meaning of §28.6 before accepting the answer.



7. **Independent check for §28.7.** Rework the problem from the stated givens rather than copying the worked-example result. Lowering the groundwater table generally reduces pore-water pressure \(u\). Since effective stress is \(\sigma'=\sigma-u\), a reduction in \(u\) increases effective stress and can increase available shear strength, improving stability under otherwise comparable conditions. **Check:** confirm the final magnitude and units against the physical meaning of §28.7 before accepting the answer.



8. Before accepting a shear strength, earth pressure, bearing capacity, foundations, settlement, and slope stability result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Begin with **FE Civil specification Area 12** and the applicable Handbook soil/foundation relation in the ledger; use the Das references only for the reconciled learned-design detail.

10. For shear strength, earth pressure, bearing capacity, foundations, settlement, and slope stability, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 12.

- **soil shear strength:** Mohr-Coulomb shear strength
- **earth pressure state:** At-rest, active, and passive earth pressure
- **retaining structure stability:** Retaining-wall stability checks
- **bearing capacity:** Ultimate bearing capacity and allowable pressure
- **foundation selection:** Foundation types and load transfer
- **consolidation settlement:** Consolidation and settlement
- **slope stability:** Slope stability and stabilization

---

## What's Next

**Chapter 03-29: Transportation Engineering — Geometric Design, Pavements, Traffic Flow, and Planning**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
