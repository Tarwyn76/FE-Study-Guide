---
chapter: "03-27"
title: "Soil Classification, Phase Relations, Compaction, and Effective Stress"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-027-01, CIV-3-027-02, CIV-3-027-03, CIV-3-027-04, CIV-3-027-05, CIV-3-027-06, CIV-3-027-07]
routes: [civil]
status: drafted
---

# Chapter 03-27: Soil Classification, Phase Relations, Compaction, and Effective Stress

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** MAT-2B-016-02

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Soil Classification, Phase Relations, Compaction, and Effective Stress**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **27.1** Explain and apply **Soil phase relationships and unit weights**.
* **27.2** Explain and apply **Specific gravity, saturation, and unit-weight relations**.
* **27.3** Explain and apply **Grain-size distribution and gradation parameters**.
* **27.4** Explain and apply **Atterberg limits and plasticity index**.
* **27.5** Explain and apply **Unified Soil Classification System**.
* **27.6** Explain and apply **Compaction, moisture-density relation, and relative compaction**.
* **27.7** Explain and apply **Total stress, pore pressure, and effective stress**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 27.1 Soil phase relationships and unit weights

The three-phase diagram is the bookkeeping foundation for geotechnical calculations. Keep volume and weight relationships separate.

\[e=\frac{V_v}{V_s},\quad n=\frac{V_v}{V},\quad w=\frac{W_w}{W_s}\]

![FIG-03-27-001: Three-phase soil diagram showing air, water, solids volumes and weights with e, n, w, S labels.](../figures/FIG-03-27-001-soil-phase-relationships-and-unit-weights.png)

### Worked Example 1

**Problem.** If Vv=0.4 m³ and Vs=0.6 m³, e=0.667 and n=0.40.

**Solution.** Void ratio is \(e=V_v/V_s=0.4/0.6=0.667\). Porosity is \(n=V_v/V_t=0.4/(0.4+0.6)=0.40\). The two quantities are related but not interchangeable: \(e\) uses solids volume in the denominator, while \(n\) uses total volume.

---

## 27.2 Specific gravity, saturation, and unit-weight relations

Specific gravity describes soil solids; saturation describes how much of the void volume contains water. Do not confuse them.

\[S=\frac{V_w}{V_v}\times100\%\]

![FIG-03-27-002: Soil phase diagram annotated for specific gravity, saturation, dry, saturated, and submerged unit weights.](../figures/FIG-03-27-002-specific-gravity-saturation-and-unit-weight-relations.png)

### Worked Example 2

**Problem.** If Vw=0.30 and Vv=0.40 m³, S=75%.

**Solution.** Degree of saturation is \(S=V_w/V_v\). With \(V_w=0.30\ \text{m}^3\) and \(V_v=0.40\ \text{m}^3\), \(S=0.30/0.40=0.75=75\%\).

---

## 27.3 Grain-size distribution and gradation parameters

Gradation parameters help classify coarse-grained soils. Read D-values from the percent-passing curve.

\[C_u=\frac{D_{60}}{D_{10}},\qquad C_c=\frac{D_{30}^2}{D_{10}D_{60}}\]

![FIG-03-27-003: Semilog grain-size distribution curve marking D10, D30, D60, Cu, and Cc.](../figures/FIG-03-27-003-grain-size-distribution-and-gradation-parameters.png)

### Worked Example 3

**Problem.** D60=0.60 mm and D10=0.10 mm gives Cu=6.

**Solution.** The coefficient of uniformity is \(C_u=D_{60}/D_{10}\). Thus \(C_u=0.60/0.10=6\). Both particle sizes are given in **mm**, which cancel in the ratio; the result is dimensionless.

---

## 27.4 Atterberg limits and plasticity index

Liquid and plastic limits characterize fine-grained soil consistency. The plasticity chart uses LL and PI for classification.

\[PI=LL-PL\]

![FIG-03-27-004: Casagrande plasticity chart with A-line and representative soil point.](../figures/FIG-03-27-004-atterberg-limits-and-plasticity-index.png)

### Worked Example 4

**Problem.** LL=45 and PL=25 gives PI=20.

**Solution.** Plasticity index is \(PI=LL-PL\). With \(LL=45\) and \(PL=25\), \(PI=20\). The liquid and plastic limits are reported as water-content percentages, so the index is expressed in percentage points.

---

## 27.5 Unified Soil Classification System

USCS classification combines grain-size distribution and plasticity. Follow the decision sequence rather than guessing from appearance.

\[\text{classification}=\text{gradation/fines/Atterberg limits}\]

![FIG-03-27-005: USCS decision flowchart from coarse/fine fraction through gradation and plasticity.](../figures/FIG-03-27-005-unified-soil-classification-system.png)

### Worked Example 5

**Problem.** A clean sand with appropriate gradation may classify as SW or SP depending on Cu and Cc.

**Solution.** For clean sands in USCS, the distinction between well graded and poorly graded depends on gradation criteria involving \(C_u\) and \(C_c\), in addition to fines content. A clean sand meeting the well-graded limits is SW; one failing them is SP.

---

## 27.6 Compaction, moisture-density relation, and relative compaction

Compaction increases dry unit weight by reducing air voids. Optimum moisture content corresponds to the laboratory compaction curve's peak dry density.

\[RC=\frac{\gamma_{d,\text{field}}}{\gamma_{d,\max}}\times100\%\]

![FIG-03-27-006: Dry unit weight versus moisture content showing optimum moisture, maximum dry density, and field test point.](../figures/FIG-03-27-006-compaction-moisture-density-relation-and-relative-compaction.png)

### Worked Example 6

**Problem.** Field dry unit weight 118 pcf and lab maximum 124 pcf gives RC≈95.2%.

**Solution.** Relative compaction is \(RC=\gamma_{d,field}/\gamma_{d,max}\times100\). Thus \(RC=118/124\times100=95.16\%\approx95.2\%\). Both dry unit weights are in **pcf** and must be based on comparable moisture/density test conditions.

---

## 27.7 Total stress, pore pressure, and effective stress

Effective stress controls many soil strength and deformation behaviors. Water-table changes alter pore pressure and therefore effective stress.

\[\sigma'=\sigma-u\]

![FIG-03-27-007: Soil profile with water table and plots of total stress, pore pressure, and effective stress versus depth.](../figures/FIG-03-27-007-total-stress-pore-pressure-and-effective-stress.png)

### Worked Example 7

**Problem.** Total vertical stress 100 kPa and pore pressure 35 kPa gives effective stress 65 kPa.

**Solution.** Terzaghi effective stress is \(\sigma'=\sigma-u\). With total vertical stress \(100\ \text{kPa}\) and pore-water pressure \(35\ \text{kPa}\), \(\sigma'=100-35=65\ \text{kPa}\).

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a soil-profile problem, first compute phase relationships or classification quantities, then determine total stress, pore pressure, and effective stress at the depth of interest. Do not mix total and effective stress parameters in the same shear-strength or settlement calculation.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook definitions for void ratio, saturation, gradation coefficients, compaction, and effective stress. These quantities have similar symbols and percentages, so the exact Handbook denominator and basis should control rather than a remembered shortcut.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 12; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** Some Civil specification topics are directly tabulated in the Handbook; others are named by the specification but require learned engineering knowledge. This chapter does not imply that every workflow, code provision, or design factor is printed in the Handbook.

Where the FE specification requires a topic that is not directly developed in the Handbook, the ledger marks it **specification-required / guide-developed** rather than inventing a Handbook citation.

---

## Where This Goes Wrong

**Using soil phase relationships without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using degree of saturation without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using soil gradation without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using plasticity index without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using USCS soil classification without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using relative compaction without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using effective stress without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| soil phase relationships | Concept developed in §27.1; apply with that section's stated assumptions and units. |
| degree of saturation | Concept developed in §27.2; apply with that section's stated assumptions and units. |
| soil gradation | Concept developed in §27.3; apply with that section's stated assumptions and units. |
| plasticity index | Concept developed in §27.4; apply with that section's stated assumptions and units. |
| USCS soil classification | Concept developed in §27.5; apply with that section's stated assumptions and units. |
| relative compaction | Concept developed in §27.6; apply with that section's stated assumptions and units. |
| effective stress | Concept developed in §27.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **soil phase relationships** and identify the principal quantity, relation, or decision it organizes.

2. Define **degree of saturation** and identify the principal quantity, relation, or decision it organizes.

3. Define **soil gradation** and identify the principal quantity, relation, or decision it organizes.

4. Define **plasticity index** and identify the principal quantity, relation, or decision it organizes.

5. Define **USCS soil classification** and identify the principal quantity, relation, or decision it organizes.

6. Define **relative compaction** and identify the principal quantity, relation, or decision it organizes.

7. Define **effective stress** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **soil phase relationships**?

9. What assumption or unit error is most likely to cause a wrong result when applying **degree of saturation**?

10. What assumption or unit error is most likely to cause a wrong result when applying **soil gradation**?

11. What assumption or unit error is most likely to cause a wrong result when applying **plasticity index**?

12. What assumption or unit error is most likely to cause a wrong result when applying **USCS soil classification**?

13. What assumption or unit error is most likely to cause a wrong result when applying **relative compaction**?

14. What assumption or unit error is most likely to cause a wrong result when applying **effective stress**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **soil phase relationships**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **degree of saturation**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **soil gradation**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **plasticity index**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **USCS soil classification**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **relative compaction**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **effective stress**?
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

1. **soil phase relationships** is developed in §27.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **degree of saturation** is developed in §27.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **soil gradation** is developed in §27.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **plasticity index** is developed in §27.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **USCS soil classification** is developed in §27.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **relative compaction** is developed in §27.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **effective stress** is developed in §27.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **soil phase relationships**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **degree of saturation**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **soil gradation**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **plasticity index**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **USCS soil classification**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **relative compaction**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **effective stress**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. Draw the soil phase diagram and layer profile first so volumes, weights, groundwater level, total stress, pore pressure, and effective stress use the correct reference quantities.

16. Use the Handbook soil relation when available because void ratio, porosity, saturation, gradation, compaction, and effective stress have similar symbols but different definitions.

17. Do not mix pcf, kN/m³, feet, meters, kPa, and psf without conversion; soil phase and stress calculations require one consistent unit system.

18. Check physical bounds: saturation must lie between 0 and 100 percent, porosity between 0 and 1, and effective stress should not exceed total stress when pore pressure is positive.

19. **A.** For **Soil phase relationships and unit weights**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Specific gravity, saturation, and unit-weight relations**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Grain-size distribution and gradation parameters**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Atterberg limits and plasticity index**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Unified Soil Classification System**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Compaction, moisture-density relation, and relative compaction**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Total stress, pore pressure, and effective stress**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Soil Classification, Phase Relations, Compaction, and Effective Stress, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Soil-classification and application details beyond Handbook formulas are labeled learned material and supported by the reconciled geotechnical reference rather than an invented Handbook page.



---

## Practice Problems

1. If Vv=0.4 m³ and Vs=0.6 m³, e=0.667 and n=0.40.

2. If Vw=0.30 and Vv=0.40 m³, S=75%.

3. D60=0.60 mm and D10=0.10 mm gives Cu=6.

4. LL=45 and PL=25 gives PI=20.

5. A clean sand with appropriate gradation may classify as SW or SP depending on Cu and Cc.

6. Field dry unit weight 118 pcf and lab maximum 124 pcf gives RC≈95.2%.

7. Total vertical stress 100 kPa and pore pressure 35 kPa gives effective stress 65 kPa.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. **Independent check for §27.1.** Rework the problem from the stated givens rather than copying the worked-example result. Void ratio is \(e=V_v/V_s=0.4/0.6=0.667\). Porosity is \(n=V_v/V_t=0.4/(0.4+0.6)=0.40\). The two quantities are related but not interchangeable: \(e\) uses solids volume in the denominator, while \(n\) uses total volume. **Check:** confirm the final magnitude and units against the physical meaning of §27.1 before accepting the answer.



2. **Independent check for §27.2.** Rework the problem from the stated givens rather than copying the worked-example result. Degree of saturation is \(S=V_w/V_v\). With \(V_w=0.30\ \text{m}^3\) and \(V_v=0.40\ \text{m}^3\), \(S=0.30/0.40=0.75=75\%\). **Check:** confirm the final magnitude and units against the physical meaning of §27.2 before accepting the answer.



3. **Independent check for §27.3.** Rework the problem from the stated givens rather than copying the worked-example result. The coefficient of uniformity is \(C_u=D_{60}/D_{10}\). Thus \(C_u=0.60/0.10=6\). The result is dimensionless because both particle sizes use the same length unit. **Check:** confirm the final magnitude and units against the physical meaning of §27.3 before accepting the answer.



4. **Independent check for §27.4.** Rework the problem from the stated givens rather than copying the worked-example result. Plasticity index is \(PI=LL-PL\). With \(LL=45\) and \(PL=25\), \(PI=20\). The liquid and plastic limits are reported as water-content percentages, so the index is expressed in percentage points. **Check:** confirm the final magnitude and units against the physical meaning of §27.4 before accepting the answer.



5. **Independent check for §27.5.** Rework the problem from the stated givens rather than copying the worked-example result. For clean sands in USCS, the distinction between well graded and poorly graded depends on gradation criteria involving \(C_u\) and \(C_c\), in addition to fines content. A clean sand meeting the well-graded limits is SW; one failing them is SP. **Check:** confirm the final magnitude and units against the physical meaning of §27.5 before accepting the answer.



6. **Independent check for §27.6.** Rework the problem from the stated givens rather than copying the worked-example result. Relative compaction is \(RC=\gamma_{d,field}/\gamma_{d,max}\times100\). Thus \(RC=118/124\times100=95.16\%\approx95.2\%\). Both dry unit weights must be based on comparable moisture/density test conditions. **Check:** confirm the final magnitude and units against the physical meaning of §27.6 before accepting the answer.



7. **Independent check for §27.7.** Rework the problem from the stated givens rather than copying the worked-example result. Terzaghi effective stress is \(\sigma'=\sigma-u\). With total vertical stress \(100\ \text{kPa}\) and pore-water pressure \(35\ \text{kPa}\), \(\sigma'=100-35=65\ \text{kPa}\). **Check:** confirm the final magnitude and units against the physical meaning of §27.7 before accepting the answer.



8. Before accepting a soil classification, phase relations, compaction, and effective stress result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Start with **FE Civil specification Area 12** and the soil/effective-stress relations in the ledger; use the external geotechnical source for the reconciled learned classification/application material.

10. For soil classification, phase relations, compaction, and effective stress, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 12.

- **soil phase relationships:** Soil phase relationships and unit weights
- **degree of saturation:** Specific gravity, saturation, and unit-weight relations
- **soil gradation:** Grain-size distribution and gradation parameters
- **plasticity index:** Atterberg limits and plasticity index
- **USCS soil classification:** Unified Soil Classification System
- **relative compaction:** Compaction, moisture-density relation, and relative compaction
- **effective stress:** Total stress, pore pressure, and effective stress

---

## What's Next

**Chapter 03-28: Shear Strength, Earth Pressure, Bearing Capacity, Foundations, Settlement, and Slope Stability**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
