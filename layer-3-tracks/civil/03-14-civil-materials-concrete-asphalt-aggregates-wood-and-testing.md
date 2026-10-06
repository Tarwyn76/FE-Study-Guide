---
chapter: "03-14"
title: "Civil Materials — Concrete, Asphalt, Aggregates, Wood, and Testing"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-014-01, CIV-3-014-02, CIV-3-014-03, CIV-3-014-04, CIV-3-014-05, CIV-3-014-06, CIV-3-014-07]
routes: [civil]
status: drafted
---

# Chapter 03-14: Civil Materials — Concrete, Asphalt, Aggregates, Wood, and Testing

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** MAT-2B-016-02

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Civil Materials — Concrete, Asphalt, Aggregates, Wood, and Testing**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **14.1** Explain and apply **Concrete mix proportions, water-cement ratio, and strength**.
* **14.2** Explain and apply **Asphalt binder, aggregate gradation, and volumetrics**.
* **14.3** Explain and apply **Aggregate gradation, specific gravity, absorption, and durability**.
* **14.4** Explain and apply **Concrete testing — slump, cylinders, air, and unit weight**.
* **14.5** Explain and apply **Asphalt, aggregate, and wood test methods**.
* **14.6** Explain and apply **Physical and mechanical properties of metals and wood**.
* **14.7** Explain and apply **Specification selection, durability, and failure modes**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 14.1 Concrete mix proportions, water-cement ratio, and strength

Concrete mix design balances workability, durability, and strength. For FE work, keep the water-cement ratio on a mass basis and distinguish cementitious material from total aggregate.

\[\text{w/c}=\frac{W_w}{W_c}\]

![FIG-03-14-001: Concrete batch components labeled cement, water, fine aggregate, coarse aggregate, air, and admixture with water-cement ratio highlighted.](../figures/FIG-03-14-001-concrete-mix-proportions-water-cement-ratio-and-strength.png)

### Worked Example 1

**Problem.** A batch contains 320 lb of water and 640 lb of cement. The water-cement ratio is 0.50.

**Solution.** Apply the relation and definitions in §14.1; the stated result follows with consistent units and sign convention.

---

## 14.2 Asphalt binder, aggregate gradation, and volumetrics

Asphalt performance depends on binder content, aggregate structure, air voids, and compaction. Recognize the distinction between bulk specific gravity and theoretical maximum specific gravity.

\[V_a=100\left(1-\frac{G_{mb}}{G_{mm}}\right)\]

![FIG-03-14-002: Asphalt specimen cross-section showing aggregate skeleton, binder film, and air voids with Gmb and Gmm labels.](../figures/FIG-03-14-002-asphalt-binder-aggregate-gradation-and-volumetrics.png)

### Worked Example 2

**Problem.** If G_mb = 2.35 and G_mm = 2.50, air voids are 6.0%.

**Solution.** Apply the relation and definitions in §14.2; the stated result follows with consistent units and sign convention.

---

## 14.3 Aggregate gradation, specific gravity, absorption, and durability

Aggregate behavior is governed by gradation, particle shape, absorption, durability, and specific gravity. Sieve results are cumulative and should be checked for monotonic consistency.

\[\%\,\text{passing}=100\frac{W_{\text{passing}}}{W_{\text{total}}}\]

![FIG-03-14-003: Sieve stack and semilog gradation curve with percent passing versus sieve size.](../figures/FIG-03-14-003-aggregate-gradation-specific-gravity-absorption-and-durability.png)

### Worked Example 3

**Problem.** A 1000 g sample has 620 g passing a sieve; percent passing is 62%.

**Solution.** Apply the relation and definitions in §14.3; the stated result follows with consistent units and sign convention.

---

## 14.4 Concrete testing — slump, cylinders, air, and unit weight

Field and laboratory concrete tests do not measure the same property. Slump indicates consistency, cylinders estimate compressive strength, air tests quantify entrained air, and unit-weight tests support yield checks.

\[f_c=\frac{P}{A}\]

![FIG-03-14-004: Concrete testing workflow from sampling to slump, air, unit weight, curing, and compression testing.](../figures/FIG-03-14-004-concrete-testing-slump-cylinders-air-and-unit-weight.png)

### Worked Example 4

**Problem.** A cylinder fails at 95 kip with area 28.27 in²; compressive stress is about 3.36 ksi.

**Solution.** Apply the relation and definitions in §14.4; the stated result follows with consistent units and sign convention.

---

## 14.5 Asphalt, aggregate, and wood test methods

Civil materials questions often test what a procedure measures rather than requiring a full standard. Match the specimen, loading mode, measured response, and engineering property.

\[\sigma=\frac{P}{A}\]

![FIG-03-14-005: Matrix linking material specimens to common civil-engineering tests and measured properties.](../figures/FIG-03-14-005-asphalt-aggregate-and-wood-test-methods.png)

### Worked Example 5

**Problem.** A tension coupon carrying 24 kN over 120 mm² has stress 200 MPa.

**Solution.** Apply the relation and definitions in §14.5; the stated result follows with consistent units and sign convention.

---

## 14.6 Physical and mechanical properties of metals and wood

Elastic modulus, yield strength, ultimate strength, density, thermal expansion, moisture effects, and anisotropy influence material selection. Wood is strongly direction-dependent.

\[E=\frac{\sigma}{\varepsilon}\]

![FIG-03-14-006: Comparative stress-strain sketches for structural steel, concrete, asphalt, and wood with key qualitative differences.](../figures/FIG-03-14-006-physical-and-mechanical-properties-of-metals-and-wood.png)

### Worked Example 6

**Problem.** Stress 12 ksi at strain 0.0010 corresponds to E = 12,000 ksi.

**Solution.** Apply the relation and definitions in §14.6; the stated result follows with consistent units and sign convention.

---

## 14.7 Specification selection, durability, and failure modes

Material selection is not based on strength alone. Exposure, durability, constructability, variability, test acceptance, and governing specifications all matter.

\[\text{design check: demand}\le \text{allowable or design resistance}\]

![FIG-03-14-007: Material selection flowchart from loads and exposure through properties, test criteria, durability, and acceptance.](../figures/FIG-03-14-007-specification-selection-durability-and-failure-modes.png)

### Worked Example 7

**Problem.** A high-strength material that is incompatible with freeze-thaw exposure may still be an unacceptable selection.

**Solution.** Apply the relation and definitions in §14.7; the stated result follows with consistent units and sign convention.

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

Primary source basis: **FE Civil specification Area 7; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** Some Civil specification topics are directly tabulated in the Handbook; others are named by the specification but require learned engineering knowledge. This chapter does not imply that every workflow, code provision, or design factor is printed in the Handbook.

Where the FE specification requires a topic that is not directly developed in the Handbook, the ledger marks it **specification-required / guide-developed** rather than inventing a Handbook citation.

---

## Where This Goes Wrong

**Using concrete mix design without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using asphalt mixture volumetrics without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using aggregate gradation without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using concrete acceptance testing without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using civil materials testing without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using civil material properties without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using materials specification basis without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| concrete mix design | Concept developed in §14.1; apply with that section's stated assumptions and units. |
| asphalt mixture volumetrics | Concept developed in §14.2; apply with that section's stated assumptions and units. |
| aggregate gradation | Concept developed in §14.3; apply with that section's stated assumptions and units. |
| concrete acceptance testing | Concept developed in §14.4; apply with that section's stated assumptions and units. |
| civil materials testing | Concept developed in §14.5; apply with that section's stated assumptions and units. |
| civil material properties | Concept developed in §14.6; apply with that section's stated assumptions and units. |
| materials specification basis | Concept developed in §14.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **concrete mix design** and identify the principal quantity, relation, or decision it organizes.

2. Define **asphalt mixture volumetrics** and identify the principal quantity, relation, or decision it organizes.

3. Define **aggregate gradation** and identify the principal quantity, relation, or decision it organizes.

4. Define **concrete acceptance testing** and identify the principal quantity, relation, or decision it organizes.

5. Define **civil materials testing** and identify the principal quantity, relation, or decision it organizes.

6. Define **civil material properties** and identify the principal quantity, relation, or decision it organizes.

7. Define **materials specification basis** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **concrete mix design**?

9. What assumption or unit error is most likely to cause a wrong result when applying **asphalt mixture volumetrics**?

10. What assumption or unit error is most likely to cause a wrong result when applying **aggregate gradation**?

11. What assumption or unit error is most likely to cause a wrong result when applying **concrete acceptance testing**?

12. What assumption or unit error is most likely to cause a wrong result when applying **civil materials testing**?

13. What assumption or unit error is most likely to cause a wrong result when applying **civil material properties**?

14. What assumption or unit error is most likely to cause a wrong result when applying **materials specification basis**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **concrete mix design**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **asphalt mixture volumetrics**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **aggregate gradation**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **concrete acceptance testing**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **civil materials testing**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **civil material properties**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **materials specification basis**?
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

1. **concrete mix design** is developed in §14.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **asphalt mixture volumetrics** is developed in §14.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **aggregate gradation** is developed in §14.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **concrete acceptance testing** is developed in §14.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **civil materials testing** is developed in §14.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **civil material properties** is developed in §14.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **materials specification basis** is developed in §14.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **concrete mix design**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **asphalt mixture volumetrics**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **aggregate gradation**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **concrete acceptance testing**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **civil materials testing**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **civil material properties**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **materials specification basis**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

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

1. A batch contains 320 lb of water and 640 lb of cement. The water-cement ratio is 0.50.

2. If G_mb = 2.35 and G_mm = 2.50, air voids are 6.0%.

3. A 1000 g sample has 620 g passing a sieve; percent passing is 62%.

4. A cylinder fails at 95 kip with area 28.27 in²; compressive stress is about 3.36 ksi.

5. A tension coupon carrying 24 kN over 120 mm² has stress 200 MPa.

6. Stress 12 ksi at strain 0.0010 corresponds to E = 12,000 ksi.

7. A high-strength material that is incompatible with freeze-thaw exposure may still be an unacceptable selection.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §14.1. A batch contains 320 lb of water and 640 lb of cement. The water-cement ratio is 0.50. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §14.2. If G_mb = 2.35 and G_mm = 2.50, air voids are 6.0%. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §14.3. A 1000 g sample has 620 g passing a sieve; percent passing is 62%. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §14.4. A cylinder fails at 95 kip with area 28.27 in²; compressive stress is about 3.36 ksi. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §14.5. A tension coupon carrying 24 kN over 120 mm² has stress 200 MPa. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §14.6. Stress 12 ksi at strain 0.0010 corresponds to E = 12,000 ksi. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §14.7. A high-strength material that is incompatible with freeze-thaw exposure may still be an unacceptable selection. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 7 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 7.

- **concrete mix design:** Concrete mix proportions, water-cement ratio, and strength
- **asphalt mixture volumetrics:** Asphalt binder, aggregate gradation, and volumetrics
- **aggregate gradation:** Aggregate gradation, specific gravity, absorption, and durability
- **concrete acceptance testing:** Concrete testing — slump, cylinders, air, and unit weight
- **civil materials testing:** Asphalt, aggregate, and wood test methods
- **civil material properties:** Physical and mechanical properties of metals and wood
- **materials specification basis:** Specification selection, durability, and failure modes

---

## What's Next

**Chapter 03-15: Surveying, Leveling, Coordinates, Grades, Earthwork, and Volumes**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
