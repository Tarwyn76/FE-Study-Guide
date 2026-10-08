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

**Solution.** Use the mass-based water-cement ratio, \(w/c=W_w/W_c\). Substituting the batch masses gives \(w/c=320/640=0.50\). Because both quantities are masses in the same unit, pounds (lbm) cancel and the ratio is dimensionless. The result is therefore a water-cement ratio of **0.50**. Both batch masses are expressed in **lb**, so the pounds cancel and the final ratio is dimensionless.

---

## 14.2 Asphalt binder, aggregate gradation, and volumetrics

Asphalt performance depends on binder content, aggregate structure, air voids, and compaction. Recognize the distinction between bulk specific gravity and theoretical maximum specific gravity.

\[V_a=100\left(1-\frac{G_{mb}}{G_{mm}}\right)\]

![FIG-03-14-002: Asphalt specimen cross-section showing aggregate skeleton, binder film, and air voids with Gmb and Gmm labels.](../figures/FIG-03-14-002-asphalt-binder-aggregate-gradation-and-volumetrics.png)

### Worked Example 2

**Problem.** If G_mb = 2.35 and G_mm = 2.50, air voids are 6.0%.

**Solution.** Use \(V_a=100(1-G_{mb}/G_{mm})\). With \(G_{mb}=2.35\) and \(G_{mm}=2.50\), \(V_a=100[1-(2.35/2.50)]=100(0.06)=6.0\%\). The bulk specific gravity must be less than the theoretical maximum specific gravity for a positive air-void content.

---

## 14.3 Aggregate gradation, specific gravity, absorption, and durability

Aggregate behavior is governed by gradation, particle shape, absorption, durability, and specific gravity. Sieve results are cumulative and should be checked for monotonic consistency.

\[\%\,\text{passing}=100\frac{W_{\text{passing}}}{W_{\text{total}}}\]

![FIG-03-14-003: Sieve stack and semilog gradation curve with percent passing versus sieve size.](../figures/FIG-03-14-003-aggregate-gradation-specific-gravity-absorption-and-durability.png)

### Worked Example 3

**Problem.** A 1000 g sample has 620 g passing a sieve; percent passing is 62%.

**Solution.** Percent passing is the mass passing the sieve divided by the total sample mass. Thus \(\%\,passing=100(620/1000)=62\%\). A gradation table should also be checked to make sure cumulative percent passing decreases consistently as sieve opening decreases.

---

## 14.4 Concrete testing — slump, cylinders, air, and unit weight

Field and laboratory concrete tests do not measure the same property. Slump indicates consistency, cylinders estimate compressive strength, air tests quantify entrained air, and unit-weight tests support yield checks.

\[f_c=\frac{P}{A}\]

![FIG-03-14-004: Concrete testing workflow from sampling to slump, air, unit weight, curing, and compression testing.](../figures/FIG-03-14-004-concrete-testing-slump-cylinders-air-and-unit-weight.png)

### Worked Example 4

**Problem.** A cylinder fails at 95 kip with area 28.27 in²; compressive stress is about 3.36 ksi.

**Solution.** Compressive stress is load divided by loaded area: \(f_c=P/A\). Convert \(95\) kip to \(95{,}000\) lb and divide by \(28.27\ \text{in}^2\): \(f_c=3360\ \text{psi}=3.36\ \text{ksi}\). The reported cylinder strength is therefore approximately **3.36 ksi**.

---

## 14.5 Asphalt, aggregate, and wood test methods

Civil materials questions often test what a procedure measures rather than requiring a full standard. Match the specimen, loading mode, measured response, and engineering property.

\[\sigma=\frac{P}{A}\]

![FIG-03-14-005: Matrix linking material specimens to common civil-engineering tests and measured properties.](../figures/FIG-03-14-005-asphalt-aggregate-and-wood-test-methods.png)

### Worked Example 5

**Problem.** A tension coupon carrying 24 kN over 120 mm² has stress 200 MPa.

**Solution.** Apply \(\sigma=P/A\). Since \(1\ \text{N/mm}^2=1\ \text{MPa}\), \(24\ \text{kN}=24{,}000\ \text{N}\), so \(\sigma=24{,}000/120=200\ \text{N/mm}^2=200\ \text{MPa}\). The unit conversion is built directly into the N/mm²-to-MPa equivalence.

---

## 14.6 Physical and mechanical properties of metals and wood

Elastic modulus, yield strength, ultimate strength, density, thermal expansion, moisture effects, and anisotropy influence material selection. Wood is strongly direction-dependent.

\[E=\frac{\sigma}{\varepsilon}\]

![FIG-03-14-006: Comparative stress-strain sketches for structural steel, concrete, asphalt, and wood with key qualitative differences.](../figures/FIG-03-14-006-physical-and-mechanical-properties-of-metals-and-wood.png)

### Worked Example 6

**Problem.** Stress 12 ksi at strain 0.0010 corresponds to E = 12,000 ksi.

**Solution.** In the linear-elastic range, \(E=\sigma/\varepsilon\). Substituting \(12\ \text{ksi}\) and \(0.0010\) gives \(E=12/0.0010=12{,}000\ \text{ksi}\). Strain is dimensionless, so the modulus carries the same stress unit as the numerator.

---

## 14.7 Specification selection, durability, and failure modes

Material selection is not based on strength alone. Exposure, durability, constructability, variability, test acceptance, and governing specifications all matter.

\[\text{design check: demand}\le \text{allowable or design resistance}\]

![FIG-03-14-007: Material selection flowchart from loads and exposure through properties, test criteria, durability, and acceptance.](../figures/FIG-03-14-007-specification-selection-durability-and-failure-modes.png)

### Worked Example 7

**Problem.** A high-strength material that is incompatible with freeze-thaw exposure may still be an unacceptable selection.

**Solution.** Strength alone does not establish suitability. Freeze-thaw exposure can govern durability through scaling, cracking, or deterioration even when nominal strength is high. The selection therefore fails unless the material system also satisfies the applicable exposure, air-entrainment, permeability, and durability requirements.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** First separate the problem into the two governing ideas—for example, a material-property calculation followed by an acceptance or durability decision. Sketch the specimen or material system, list the given quantities with units, perform the quantitative check, and then apply the second criterion. Keeping the numerical and specification checks separate prevents a correct calculation from being mistaken for an acceptable material selection.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the FE Reference Handbook form when the exam provides that relation. Match its symbols and unit convention to the problem data, convert the givens as needed, and solve from that form. A remembered equation may be equivalent, but the Handbook version reduces the risk of using a different convention, coefficient, or definition.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 7; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-014-01` — ACI Committee 211. (2022). *Selecting Proportions for Normal-Density and High-Density Concrete—Guide* (ACI PRC-211.1-22). American Concrete Institute. ISBN 978-1-64195-186-9. Verified location: Chapter 3 pp. 4–5 (w/cm, strength, durability); §4.7 p. 8; Chapter 5 pp. 13–14; Chapters 8–9 pp. 21–28.
- `CIV-3-014-02` — Asphalt Institute. (2014). *Asphalt Mix Design Methods* (MS-2, 7th ed.). Asphalt Institute. ISBN 978-1-934154-70-0. Verified location: pp. 12–14 (volumetric characteristics); p. 24 (aggregate gradation); pp. 34–45 (laboratory mixture testing); pp. 46–61 (specific gravities, absorption, and volumetric properties).
- `CIV-3-014-03` — Asphalt Institute. (2014). *Asphalt Mix Design Methods* (MS-2, 7th ed.). Asphalt Institute. ISBN 978-1-934154-70-0. Verified location: pp. 12–14 (volumetric characteristics); p. 24 (aggregate gradation); pp. 34–45 (laboratory mixture testing); pp. 46–61 (specific gravities, absorption, and volumetric properties). ASTM International. *ASTM C136/C136M, Standard Test Method for Sieve Analysis of Fine and Coarse Aggregates*; *ASTM C127, Standard Test Method for Relative Density (Specific Gravity) and Absorption of Coarse Aggregate*; *ASTM C128, Standard Test Method for Relative Density (Specific Gravity) and Absorption of Fine Aggregate*; and *ASTM C88/C88M, Standard Test Method for Soundness of Aggregates by Use of Sodium Sulfate or Magnesium Sulfate*. Cited at publication/standard level; no page-level claim.
- `CIV-3-014-04` — ACI Committee 211. (2022). *Selecting Proportions for Normal-Density and High-Density Concrete—Guide* (ACI PRC-211.1-22). American Concrete Institute. ISBN 978-1-64195-186-9. Verified location: Chapter 3 pp. 4–5 (w/cm, strength, durability); §4.7 p. 8; Chapter 5 pp. 13–14; Chapters 8–9 pp. 21–28. ASTM International. *ASTM C143/C143M, Standard Test Method for Slump of Hydraulic-Cement Concrete*; *ASTM C39/C39M, Standard Test Method for Compressive Strength of Cylindrical Concrete Specimens*; *ASTM C231/C231M* and *ASTM C173/C173M* for air content; and *ASTM C138/C138M* for density (unit weight), yield, and gravimetric air content. Cited at publication/standard level; no page-level claim.
- `CIV-3-014-05` — Asphalt Institute. (2014). *Asphalt Mix Design Methods* (MS-2, 7th ed.). Asphalt Institute. ISBN 978-1-934154-70-0. Verified location: pp. 12–14 (volumetric characteristics); p. 24 (aggregate gradation); pp. 34–45 (laboratory mixture testing); pp. 46–61 (specific gravities, absorption, and volumetric properties). Forest Products Laboratory. (2021). *Wood Handbook—Wood as an Engineering Material*. General Technical Report FPL-GTR-282. U.S. Department of Agriculture, Forest Service, Forest Products Laboratory. Verified location: Chapter 4, pp. 4-1–4-22 (physical/moisture properties); Chapter 5, pp. 5-1–5-44 (mechanical properties); p. 5-26 notes ASTM D143-based test procedures. ASTM International. *ASTM D143, Standard Test Methods for Small Clear Specimens of Timber*; and *ASTM E8/E8M, Standard Test Methods for Tension Testing of Metallic Materials*. Cited at publication/standard level; no page-level claim.
- `CIV-3-014-06` — Forest Products Laboratory. (2021). *Wood Handbook—Wood as an Engineering Material*. General Technical Report FPL-GTR-282. U.S. Department of Agriculture, Forest Service, Forest Products Laboratory. Verified location: Chapter 4, pp. 4-1–4-22 (physical/moisture properties); Chapter 5, pp. 5-1–5-44 (mechanical properties); p. 5-26 notes ASTM D143-based test procedures. ASTM International. *ASTM D143, Standard Test Methods for Small Clear Specimens of Timber*; and *ASTM E8/E8M, Standard Test Methods for Tension Testing of Metallic Materials*. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

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

15. Draw the batch/specimen model first so water, cementitious material, aggregate condition, loaded area, and test geometry are not confused before selecting a materials relation.

16. Prefer the FE Handbook relation when it supplies the material-property or test equation because its definitions and unit convention are the ones the exam expects.

17. Concrete and materials problems commonly mix psi or ksi, MPa, inches, millimeters, and pounds; explicit conversion prevents a correct formula from producing a dimensionally invalid result.

18. Check whether the result is physically credible: water-cement ratios should be plausible, strengths should match the stated material scale, and asphalt bulk specific gravity should remain below theoretical maximum specific gravity.

19. **A.** For **Concrete mix proportions, water-cement ratio, and strength**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Asphalt binder, aggregate gradation, and volumetrics**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Aggregate gradation, specific gravity, absorption, and durability**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Concrete testing — slump, cylinders, air, and unit weight**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Asphalt, aggregate, and wood test methods**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Physical and mechanical properties of metals and wood**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Specification selection, durability, and failure modes**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Civil Materials — Concrete, Asphalt, Aggregates, Wood, and Testing, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** For this chapter, learned material beyond Handbook tables is labeled explicitly and supported by the reconciled ACI 211, Asphalt Institute MS-2, USDA Wood Handbook, and ASTM references rather than by an invented Handbook citation.



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

1. **Independent check for §14.1.** Rework the problem from the stated givens rather than copying the worked-example result. Use the mass-based water-cement ratio, \(w/c=W_w/W_c\). Substituting the batch masses gives \(w/c=320/640=0.50\). Because both quantities are masses in the same unit, pounds cancel and the ratio is dimensionless. The result is therefore a water-cement ratio of **0.50**. **Check:** confirm the final magnitude and units against the physical meaning of §14.1 before accepting the answer.



2. **Independent check for §14.2.** Rework the problem from the stated givens rather than copying the worked-example result. Use \(V_a=100(1-G_{mb}/G_{mm})\). With \(G_{mb}=2.35\) and \(G_{mm}=2.50\), \(V_a=100[1-(2.35/2.50)]=100(0.06)=6.0\%\). The bulk specific gravity must be less than the theoretical maximum specific gravity for a positive air-void content. **Check:** confirm the final magnitude and units against the physical meaning of §14.2 before accepting the answer.



3. **Independent check for §14.3.** Rework the problem from the stated givens rather than copying the worked-example result. Percent passing is the mass passing the sieve divided by the total sample mass. Thus \(\%\,passing=100(620/1000)=62\%\). A gradation table should also be checked to make sure cumulative percent passing decreases consistently as sieve opening decreases. **Check:** confirm the final magnitude and units against the physical meaning of §14.3 before accepting the answer.



4. **Independent check for §14.4.** Rework the problem from the stated givens rather than copying the worked-example result. Compressive stress is load divided by loaded area: \(f_c=P/A\). Convert \(95\) kip to \(95{,}000\) lb and divide by \(28.27\ \text{in}^2\): \(f_c=3360\ \text{psi}=3.36\ \text{ksi}\). The reported cylinder strength is therefore approximately **3.36 ksi**. **Check:** confirm the final magnitude and units against the physical meaning of §14.4 before accepting the answer.



5. **Independent check for §14.5.** Rework the problem from the stated givens rather than copying the worked-example result. Apply \(\sigma=P/A\). Since \(1\ \text{N/mm}^2=1\ \text{MPa}\), \(24\ \text{kN}=24{,}000\ \text{N}\), so \(\sigma=24{,}000/120=200\ \text{N/mm}^2=200\ \text{MPa}\). The unit conversion is built directly into the N/mm²-to-MPa equivalence. **Check:** confirm the final magnitude and units against the physical meaning of §14.5 before accepting the answer.



6. **Independent check for §14.6.** Rework the problem from the stated givens rather than copying the worked-example result. In the linear-elastic range, \(E=\sigma/\varepsilon\). Substituting \(12\ \text{ksi}\) and \(0.0010\) gives \(E=12/0.0010=12{,}000\ \text{ksi}\). Strain is dimensionless, so the modulus carries the same stress unit as the numerator. **Check:** confirm the final magnitude and units against the physical meaning of §14.6 before accepting the answer.



7. **Independent check for §14.7.** Rework the problem from the stated givens rather than copying the worked-example result. Strength alone does not establish suitability. Freeze-thaw exposure can govern durability through scaling, cracking, or deterioration even when nominal strength is high. The selection therefore fails unless the material system also satisfies the applicable exposure, air-entrainment, permeability, and durability requirements. **Check:** confirm the final magnitude and units against the physical meaning of §14.7 before accepting the answer.



8. Before accepting a civil materials — concrete, asphalt, aggregates, wood, and testing result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Start with **FE Civil specification Area 7** and the Civil Engineering/material-property locations recorded in the ledger. For split-required material, use the chapter's reconciled ACI, Asphalt Institute, USDA, or ASTM source as applicable.

10. For civil materials — concrete, asphalt, aggregates, wood, and testing, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

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
