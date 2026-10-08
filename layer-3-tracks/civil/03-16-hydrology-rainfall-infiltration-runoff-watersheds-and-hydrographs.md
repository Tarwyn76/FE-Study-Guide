---
chapter: "03-16"
title: "Hydrology — Rainfall, Infiltration, Runoff, Watersheds, and Hydrographs"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-016-01, CIV-3-016-02, CIV-3-016-03, CIV-3-016-04, CIV-3-016-05, CIV-3-016-06, CIV-3-016-07]
routes: [civil]
status: drafted
---

# Chapter 03-16: Hydrology — Rainfall, Infiltration, Runoff, Watersheds, and Hydrographs

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** FLUID-2D-044-02

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Hydrology — Rainfall, Infiltration, Runoff, Watersheds, and Hydrographs**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **16.1** Explain and apply **Watershed boundaries and hydrologic mass balance**.
* **16.2** Explain and apply **Rainfall intensity, duration, frequency, and design storms**.
* **16.3** Explain and apply **Infiltration, abstraction, and effective rainfall**.
* **16.4** Explain and apply **Rational Method peak runoff**.
* **16.5** Explain and apply **NRCS curve-number rainfall-runoff relation**.
* **16.6** Explain and apply **Hydrographs, unit hydrographs, and baseflow**.
* **16.7** Explain and apply **Evaporation, evapotranspiration, and storage change**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 16.1 Watershed boundaries and hydrologic mass balance

A watershed is a control volume. Water-balance terms must be assigned signs consistently and evaluated over the same time interval.

\[P+Q_{in}+Q_g-Q_{out}-E-T-I=\Delta S\]

![FIG-03-16-001: Watershed control volume with precipitation, runoff, infiltration, evapotranspiration, groundwater exchange, and storage.](../figures/FIG-03-16-001-watershed-boundaries-and-hydrologic-mass-balance.png)

### Worked Example 1

**Problem.** If inflows total 12 cm, losses total 9 cm, storage increases 3 cm.

**Solution.** Apply the watershed water balance: precipitation/inflow equals losses plus change in storage. With 12 cm of inflow and 9 cm of combined losses, \(\Delta S=12-9=3\ \text{cm}\). The positive sign means watershed storage increased by **3 cm of equivalent depth**.

---

## 16.2 Rainfall intensity, duration, frequency, and design storms

Design rainfall intensity depends on storm duration and return period. The selected duration should be physically consistent with the drainage response being modeled.

\[i=i(T_r,t_d)\]

![FIG-03-16-002: Intensity-duration-frequency curves with a design point selected at a specified duration and return period.](../figures/FIG-03-16-002-rainfall-intensity-duration-frequency-and-design-storms.png)

### Worked Example 2

**Problem.** For a Rational Method problem, use rainfall intensity corresponding to the time of concentration.

**Solution.** For the Rational Method, the design rainfall intensity must correspond to a duration equal to the watershed time of concentration for the selected return period. That choice represents the condition in which runoff from the hydraulically most remote point can contribute at the design location.

---

## 16.3 Infiltration, abstraction, and effective rainfall

Only rainfall excess contributes directly to surface runoff in a simplified event model. Initial abstraction and infiltration reduce effective rainfall.

\[P_e=P-I_a-F\]

![FIG-03-16-003: Rainfall hyetograph separated into abstractions and effective rainfall.](../figures/FIG-03-16-003-infiltration-abstraction-and-effective-rainfall.png)

### Worked Example 3

**Problem.** Rainfall 2.0 in with 0.3 in abstraction and 0.7 in infiltration gives 1.0 in excess.

**Solution.** Effective rainfall equals gross rainfall minus abstractions and infiltration for this simplified balance. Thus \(P_e=2.0-0.3-0.7=1.0\ \text{in}\). The resulting **1.0 in** is the depth available to produce direct runoff under the stated assumptions.

---

## 16.4 Rational Method peak runoff

The Rational Method estimates peak discharge for small watersheds using a runoff coefficient, rainfall intensity, and drainage area in a compatible unit system.

\[Q=CIA\]

![FIG-03-16-004: Small urban watershed draining to one outlet with C, I, A, and peak Q labels.](../figures/FIG-03-16-004-rational-method-peak-runoff.png)

### Worked Example 4

**Problem.** C=0.6, I=3 in/hr, A=10 acres gives Q=18 cfs in the common US customary form.

**Solution.** Using the common U.S. customary Rational Method form, \(Q=CIA\) when \(I\) is in in/hr and \(A\) is in acres. Substitution gives \(Q=0.6(3)(10)=18\ \text{cfs}\). The coefficient \(C\) is dimensionless and represents the runoff response of the drainage area.

---

## 16.5 NRCS curve-number rainfall-runoff relation

The curve-number method relates storm depth, soil-cover condition, and retention to runoff depth. Apply the threshold condition before using the runoff equation.

\[Q=\frac{(P-0.2S)^2}{P+0.8S},\qquad S=\frac{1000}{CN}-10\]

![FIG-03-16-005: Rainfall-runoff relation showing P, initial abstraction, S, CN, and runoff depth Q.](../figures/FIG-03-16-005-nrcs-curve-number-rainfall-runoff-relation.png)

### Worked Example 5

**Problem.** CN=80 gives S=2.5 in; if P=4 in, Q≈2.04 in.

**Solution.** For \(CN=80\), \(S=1000/CN-10=2.5\ \text{in}\). With \(P=4\ \text{in}\), the standard NRCS runoff expression gives \(Q=(P-0.2S)^2/(P+0.8S)=(4-0.5)^2/(4+2.0)=12.25/6\approx2.04\ \text{in}\). The result is therefore approximately **2.04 in of direct runoff** under the standard initial-abstraction assumption \(I_a=0.2S\).

---

## 16.6 Hydrographs, unit hydrographs, and baseflow

A runoff hydrograph separates baseflow from direct runoff. A unit hydrograph represents the direct-runoff response to one unit depth of effective rainfall over a stated duration.

\[Q(t)=Q_b(t)+Q_d(t)\]

![FIG-03-16-006: Storm hyetograph above a streamflow hydrograph with baseflow and direct-runoff components.](../figures/FIG-03-16-006-hydrographs-unit-hydrographs-and-baseflow.png)

### Worked Example 6

**Problem.** Scaling a 1-in unit hydrograph by 1.5 in effective rainfall multiplies ordinates by 1.5.

**Solution.** A unit hydrograph represents the direct-runoff hydrograph produced by one unit of effective rainfall. Therefore 1.5 in of effective rainfall scales every ordinate of a 1-in unit hydrograph by 1.5, provided the watershed response is treated as linear and time invariant over the event.

---

## 16.7 Evaporation, evapotranspiration, and storage change

Evaporation and evapotranspiration are losses in a water balance. Pan evaporation may be converted to lake evaporation with a pan coefficient.

\[E_L=P_cE_p\]

![FIG-03-16-007: Reservoir water balance showing precipitation, evaporation, inflow, outflow, and change in storage.](../figures/FIG-03-16-007-evaporation-evapotranspiration-and-storage-change.png)

### Worked Example 7

**Problem.** Ep=8 mm/day and Pc=0.70 gives EL=5.6 mm/day.

**Solution.** Actual evapotranspiration is estimated from pan evaporation using the pan coefficient: \(E_L=P_cE_p\). With \(P_c=0.70\) and \(E_p=8\ \text{mm/day}\), \(E_L=0.70(8)=5.6\ \text{mm/day}\).

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** Separate the problem into rainfall/runoff transformation and routing or storage. First determine excess rainfall or peak runoff using the appropriate loss/runoff method; then use that output as the input to the hydrograph or storage calculation. Keep rainfall depth, rainfall intensity, discharge, and volume units distinct throughout.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the FE Handbook relation when available, but verify that its coefficient matches the unit system. Hydrology equations such as the Rational Method are especially sensitive to customary-versus-SI conventions, so the Handbook form and units should govern.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 10; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-016-02` — Kilgore, R., Atayee, A. T., & Herrmann, G. R. (2024). *Urban Drainage Design* (Hydraulic Engineering Circular No. 22, 4th ed., FHWA-HIF-24-006). Federal Highway Administration. Verified location: Chapter 4, pp. 21–24 for rainfall/IDF/design-storm and runoff concepts; Chapter 10, pp. 182–229 for detention, stage-storage/stage-discharge, routing, and outlet control.
- `CIV-3-016-03` — Kilgore, R., Atayee, A. T., & Herrmann, G. R. (2024). *Urban Drainage Design* (Hydraulic Engineering Circular No. 22, 4th ed., FHWA-HIF-24-006). Federal Highway Administration. Verified location: Chapter 4, pp. 21–24 for rainfall/IDF/design-storm and runoff concepts; Chapter 10, pp. 182–229 for detention, stage-storage/stage-discharge, routing, and outlet control. U.S. Army Corps of Engineers, Hydrologic Engineering Center. *HEC-HMS Technical Reference Manual* (CPD-74B), current online edition. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

## Where This Goes Wrong

**Using watershed water balance without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using design rainfall without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using effective rainfall without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using Rational Method without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using curve number method without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using unit hydrograph without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using evapotranspiration loss without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| watershed water balance | Concept developed in §16.1; apply with that section's stated assumptions and units. |
| design rainfall | Concept developed in §16.2; apply with that section's stated assumptions and units. |
| effective rainfall | Concept developed in §16.3; apply with that section's stated assumptions and units. |
| Rational Method | Concept developed in §16.4; apply with that section's stated assumptions and units. |
| curve number method | Concept developed in §16.5; apply with that section's stated assumptions and units. |
| unit hydrograph | Concept developed in §16.6; apply with that section's stated assumptions and units. |
| evapotranspiration loss | Concept developed in §16.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **watershed water balance** and identify the principal quantity, relation, or decision it organizes.

2. Define **design rainfall** and identify the principal quantity, relation, or decision it organizes.

3. Define **effective rainfall** and identify the principal quantity, relation, or decision it organizes.

4. Define **Rational Method** and identify the principal quantity, relation, or decision it organizes.

5. Define **curve number method** and identify the principal quantity, relation, or decision it organizes.

6. Define **unit hydrograph** and identify the principal quantity, relation, or decision it organizes.

7. Define **evapotranspiration loss** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **watershed water balance**?

9. What assumption or unit error is most likely to cause a wrong result when applying **design rainfall**?

10. What assumption or unit error is most likely to cause a wrong result when applying **effective rainfall**?

11. What assumption or unit error is most likely to cause a wrong result when applying **Rational Method**?

12. What assumption or unit error is most likely to cause a wrong result when applying **curve number method**?

13. What assumption or unit error is most likely to cause a wrong result when applying **unit hydrograph**?

14. What assumption or unit error is most likely to cause a wrong result when applying **evapotranspiration loss**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **watershed water balance**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **design rainfall**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **effective rainfall**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **Rational Method**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **curve number method**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **unit hydrograph**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **evapotranspiration loss**?
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

1. **watershed water balance** is developed in §16.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **design rainfall** is developed in §16.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **effective rainfall** is developed in §16.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **Rational Method** is developed in §16.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **curve number method** is developed in §16.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **unit hydrograph** is developed in §16.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **evapotranspiration loss** is developed in §16.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **watershed water balance**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **design rainfall**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **effective rainfall**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **Rational Method**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **curve number method**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **unit hydrograph**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **evapotranspiration loss**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. Sketch the watershed boundary, outlet, rainfall input, abstractions, and routing path first so the analysis uses the correct drainage area and distinguishes rainfall depth, intensity, runoff depth, and discharge.

16. When the Handbook gives the hydrologic relation, use that form and its coefficient because Rational Method and related equations are sensitive to the stated unit system and variable definitions.

17. Do not combine inches per hour, acres, cubic feet per second, millimeters, and SI areas without conversion; hydrology formulas often hide unit-dependent coefficients.

18. Check hydrologic bounds: runoff depth should not exceed rainfall depth, runoff coefficients should remain physically meaningful, and the selected rainfall intensity should be compatible with the chosen duration or time of concentration.

19. **A.** For **Watershed boundaries and hydrologic mass balance**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Rainfall intensity, duration, frequency, and design storms**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Infiltration, abstraction, and effective rainfall**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Rational Method peak runoff**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **NRCS curve-number rainfall-runoff relation**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Hydrographs, unit hydrographs, and baseflow**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Evaporation, evapotranspiration, and storage change**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Hydrology — Rainfall, Infiltration, Runoff, Watersheds, and Hydrographs, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** IDF/design-storm and loss-model details beyond Handbook tables are identified as learned material and supported by FHWA HEC-22 and, where needed, HEC-HMS rather than by fabricated Handbook references.



---

## Practice Problems

1. If inflows total 12 cm, losses total 9 cm, storage increases 3 cm.

2. For a Rational Method problem, use rainfall intensity corresponding to the time of concentration.

3. Rainfall 2.0 in with 0.3 in abstraction and 0.7 in infiltration gives 1.0 in excess.

4. C=0.6, I=3 in/hr, A=10 acres gives Q=18 cfs in the common US customary form.

5. CN=80 gives S=2.5 in; if P=4 in, Q≈2.04 in.

6. Scaling a 1-in unit hydrograph by 1.5 in effective rainfall multiplies ordinates by 1.5.

7. Ep=8 mm/day and Pc=0.70 gives EL=5.6 mm/day.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. **Independent check for §16.1.** Rework the problem from the stated givens rather than copying the worked-example result. Apply the watershed water balance: precipitation/inflow equals losses plus change in storage. With 12 cm of inflow and 9 cm of combined losses, \(\Delta S=12-9=3\ \text{cm}\). The positive sign means watershed storage increased by **3 cm of equivalent depth**. **Check:** confirm the final magnitude and units against the physical meaning of §16.1 before accepting the answer.



2. **Independent check for §16.2.** Rework the problem from the stated givens rather than copying the worked-example result. For the Rational Method, the design rainfall intensity must correspond to a duration equal to the watershed time of concentration for the selected return period. That choice represents the condition in which runoff from the hydraulically most remote point can contribute at the design location. **Check:** confirm the final magnitude and units against the physical meaning of §16.2 before accepting the answer.



3. **Independent check for §16.3.** Rework the problem from the stated givens rather than copying the worked-example result. Effective rainfall equals gross rainfall minus abstractions and infiltration for this simplified balance. Thus \(P_e=2.0-0.3-0.7=1.0\ \text{in}\). The resulting **1.0 in** is the depth available to produce direct runoff under the stated assumptions. **Check:** confirm the final magnitude and units against the physical meaning of §16.3 before accepting the answer.



4. **Independent check for §16.4.** Rework the problem from the stated givens rather than copying the worked-example result. Using the common U.S. customary Rational Method form, \(Q=CIA\) when \(I\) is in in/hr and \(A\) is in acres. Substitution gives \(Q=0.6(3)(10)=18\ \text{cfs}\). The coefficient \(C\) is dimensionless and represents the runoff response of the drainage area. **Check:** confirm the final magnitude and units against the physical meaning of §16.4 before accepting the answer.



5. **Independent check for §16.5.** Rework the problem from the stated givens rather than copying the worked-example result. For \(CN=80\), \(S=1000/CN-10=2.5\ \text{in}\). With \(P=4\ \text{in}\), the standard NRCS runoff expression gives \(Q=(P-0.2S)^2/(P+0.8S)=(4-0.5)^2/(4+2.0)=12.25/6\approx2.04\ \text{in}\). The result is therefore approximately **2.04 in of direct runoff** under the standard initial-abstraction assumption \(I_a=0.2S\). **Check:** confirm the final magnitude and units against the physical meaning of §16.5 before accepting the answer.



6. **Independent check for §16.6.** Rework the problem from the stated givens rather than copying the worked-example result. A unit hydrograph represents the direct-runoff hydrograph produced by one unit of effective rainfall. Therefore 1.5 in of effective rainfall scales every ordinate of a 1-in unit hydrograph by 1.5, provided the watershed response is treated as linear and time invariant over the event. **Check:** confirm the final magnitude and units against the physical meaning of §16.6 before accepting the answer.



7. **Independent check for §16.7.** Rework the problem from the stated givens rather than copying the worked-example result. Actual evapotranspiration is estimated from pan evaporation using the pan coefficient: \(E_L=P_cE_p\). With \(P_c=0.70\) and \(E_p=8\ \text{mm/day}\), \(E_L=0.70(8)=5.6\ \text{mm/day}\). **Check:** confirm the final magnitude and units against the physical meaning of §16.7 before accepting the answer.



8. Before accepting a hydrology — rainfall, infiltration, runoff, watersheds, and hydrographs result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Start with **FE Civil specification Area 10** and the Handbook hydrology relations recorded in the ledger; for IDF, design-storm, or loss-model details use the reconciled FHWA HEC-22/HEC-HMS support.

10. For hydrology — rainfall, infiltration, runoff, watersheds, and hydrographs, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 10.

- **watershed water balance:** Watershed boundaries and hydrologic mass balance
- **design rainfall:** Rainfall intensity, duration, frequency, and design storms
- **effective rainfall:** Infiltration, abstraction, and effective rainfall
- **Rational Method:** Rational Method peak runoff
- **curve number method:** NRCS curve-number rainfall-runoff relation
- **unit hydrograph:** Hydrographs, unit hydrographs, and baseflow
- **evapotranspiration loss:** Evaporation, evapotranspiration, and storage change

---

## What's Next

**Chapter 03-17: Open-Channel Flow — Manning Equation, Specific Energy, and Hydraulic Jumps**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
