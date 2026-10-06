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

**Solution.** Apply the relation and definitions in §16.1; the stated result follows with consistent units and sign convention.

---

## 16.2 Rainfall intensity, duration, frequency, and design storms

Design rainfall intensity depends on storm duration and return period. The selected duration should be physically consistent with the drainage response being modeled.

\[i=i(T_r,t_d)\]

![FIG-03-16-002: Intensity-duration-frequency curves with a design point selected at a specified duration and return period.](../figures/FIG-03-16-002-rainfall-intensity-duration-frequency-and-design-storms.png)

### Worked Example 2

**Problem.** For a Rational Method problem, use rainfall intensity corresponding to the time of concentration.

**Solution.** Apply the relation and definitions in §16.2; the stated result follows with consistent units and sign convention.

---

## 16.3 Infiltration, abstraction, and effective rainfall

Only rainfall excess contributes directly to surface runoff in a simplified event model. Initial abstraction and infiltration reduce effective rainfall.

\[P_e=P-I_a-F\]

![FIG-03-16-003: Rainfall hyetograph separated into abstractions and effective rainfall.](../figures/FIG-03-16-003-infiltration-abstraction-and-effective-rainfall.png)

### Worked Example 3

**Problem.** Rainfall 2.0 in with 0.3 in abstraction and 0.7 in infiltration gives 1.0 in excess.

**Solution.** Apply the relation and definitions in §16.3; the stated result follows with consistent units and sign convention.

---

## 16.4 Rational Method peak runoff

The Rational Method estimates peak discharge for small watersheds using a runoff coefficient, rainfall intensity, and drainage area in a compatible unit system.

\[Q=CIA\]

![FIG-03-16-004: Small urban watershed draining to one outlet with C, I, A, and peak Q labels.](../figures/FIG-03-16-004-rational-method-peak-runoff.png)

### Worked Example 4

**Problem.** C=0.6, I=3 in/hr, A=10 acres gives Q=18 cfs in the common US customary form.

**Solution.** Apply the relation and definitions in §16.4; the stated result follows with consistent units and sign convention.

---

## 16.5 NRCS curve-number rainfall-runoff relation

The curve-number method relates storm depth, soil-cover condition, and retention to runoff depth. Apply the threshold condition before using the runoff equation.

\[Q=\frac{(P-0.2S)^2}{P+0.8S},\qquad S=\frac{1000}{CN}-10\]

![FIG-03-16-005: Rainfall-runoff relation showing P, initial abstraction, S, CN, and runoff depth Q.](../figures/FIG-03-16-005-nrcs-curve-number-rainfall-runoff-relation.png)

### Worked Example 5

**Problem.** CN=80 gives S=2.5 in; if P=4 in, Q≈1.80 in.

**Solution.** Apply the relation and definitions in §16.5; the stated result follows with consistent units and sign convention.

---

## 16.6 Hydrographs, unit hydrographs, and baseflow

A runoff hydrograph separates baseflow from direct runoff. A unit hydrograph represents the direct-runoff response to one unit depth of effective rainfall over a stated duration.

\[Q(t)=Q_b(t)+Q_d(t)\]

![FIG-03-16-006: Storm hyetograph above a streamflow hydrograph with baseflow and direct-runoff components.](../figures/FIG-03-16-006-hydrographs-unit-hydrographs-and-baseflow.png)

### Worked Example 6

**Problem.** Scaling a 1-in unit hydrograph by 1.5 in effective rainfall multiplies ordinates by 1.5.

**Solution.** Apply the relation and definitions in §16.6; the stated result follows with consistent units and sign convention.

---

## 16.7 Evaporation, evapotranspiration, and storage change

Evaporation and evapotranspiration are losses in a water balance. Pan evaporation may be converted to lake evaporation with a pan coefficient.

\[E_L=P_cE_p\]

![FIG-03-16-007: Reservoir water balance showing precipitation, evaporation, inflow, outflow, and change in storage.](../figures/FIG-03-16-007-evaporation-evapotranspiration-and-storage-change.png)

### Worked Example 7

**Problem.** Ep=8 mm/day and Pc=0.70 gives EL=5.6 mm/day.

**Solution.** Apply the relation and definitions in §16.7; the stated result follows with consistent units and sign convention.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** Draw the system, identify the requested quantity, establish units and sign conventions, and list the governing relations before substituting numbers.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook form and its unit convention unless the problem explicitly supplies a different relation.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 10; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** Some Civil specification topics are directly tabulated in the Handbook; others are named by the specification but require learned engineering knowledge. This chapter does not imply that every workflow, code provision, or design factor is printed in the Handbook.

Where the FE specification requires a topic that is not directly developed in the Handbook, the ledger marks it **specification-required / guide-developed** rather than inventing a Handbook citation.

---

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

15. The sketch exposes geometry, boundaries, loads/flows, signs, and missing data before algebra begins.

16. Use the Handbook form when it is available because the FE exam supplies that reference and its constants/unit conventions govern the problem.

17. Mixed unit systems create hidden conversion errors and can invalidate dimensional consistency.

18. A reasonableness check can catch sign, magnitude, boundary-condition, and unit errors that algebra alone does not reveal.

19. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

20. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

21. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

22. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

23. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

24. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

25. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

26. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

27. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.



---

## Practice Problems

1. If inflows total 12 cm, losses total 9 cm, storage increases 3 cm.

2. For a Rational Method problem, use rainfall intensity corresponding to the time of concentration.

3. Rainfall 2.0 in with 0.3 in abstraction and 0.7 in infiltration gives 1.0 in excess.

4. C=0.6, I=3 in/hr, A=10 acres gives Q=18 cfs in the common US customary form.

5. CN=80 gives S=2.5 in; if P=4 in, Q≈1.80 in.

6. Scaling a 1-in unit hydrograph by 1.5 in effective rainfall multiplies ordinates by 1.5.

7. Ep=8 mm/day and Pc=0.70 gives EL=5.6 mm/day.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §16.1. If inflows total 12 cm, losses total 9 cm, storage increases 3 cm. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §16.2. For a Rational Method problem, use rainfall intensity corresponding to the time of concentration. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §16.3. Rainfall 2.0 in with 0.3 in abstraction and 0.7 in infiltration gives 1.0 in excess. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §16.4. C=0.6, I=3 in/hr, A=10 acres gives Q=18 cfs in the common US customary form. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §16.5. CN=80 gives S=2.5 in; if P=4 in, Q≈1.80 in. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §16.6. Scaling a 1-in unit hydrograph by 1.5 in effective rainfall multiplies ordinates by 1.5. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §16.7. Ep=8 mm/day and Pc=0.70 gives EL=5.6 mm/day. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 10 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

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
