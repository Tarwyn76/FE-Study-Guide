---
chapter: "03-26"
title: "Reinforced Concrete Design — Beams and Columns"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-026-01, CIV-3-026-02, CIV-3-026-03, CIV-3-026-04, CIV-3-026-05, CIV-3-026-06, CIV-3-026-07]
routes: [civil]
status: drafted
---

# Chapter 03-26: Reinforced Concrete Design — Beams and Columns

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-023-07

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Reinforced Concrete Design — Beams and Columns**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **26.1** Explain and apply **Concrete flexural design assumptions**.
* **26.2** Explain and apply **Singly reinforced rectangular beam strength**.
* **26.3** Explain and apply **Strength-reduction and design check**.
* **26.4** Explain and apply **Reinforced concrete beam shear**.
* **26.5** Explain and apply **Development, anchorage, and reinforcement placement**.
* **26.6** Explain and apply **Axially loaded concrete columns**.
* **26.7** Explain and apply **Beam-column interaction and eccentric loading**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 26.1 Concrete flexural design assumptions

At nominal flexural strength, internal concrete compression and steel tension resultants balance. Strain compatibility determines stress states.

\[C=T\]

![FIG-03-26-001: Rectangular reinforced-concrete beam showing strain distribution, Whitney stress block, C, T, d, and neutral axis.](../figures/FIG-03-26-001-concrete-flexural-design-assumptions.png)

### Worked Example 1

**Problem.** For a singly reinforced rectangular beam, locate the compression block so C equals T.

**Solution.** For a singly reinforced rectangular section, equilibrium requires compression equal tension: \(C=T\). With the rectangular stress block, \(C=0.85f'_cba\) and \(T=A_sf_y\) when the steel yields; solve \(0.85f'_cba=A_sf_y\) for the compression-block depth \(a\).

---

## 26.2 Singly reinforced rectangular beam strength

Beam flexural strength depends on tensile steel area, yield strength, effective depth, and compression-block depth.

\[M_n=A_sf_y\left(d-\frac{a}{2}\right)\]

![FIG-03-26-002: Singly reinforced beam section with steel area As, effective depth d, compression block a, and internal lever arm.](../figures/FIG-03-26-002-singly-reinforced-rectangular-beam-strength.png)

### Worked Example 2

**Problem.** Once a is known from force equilibrium, compute Mn from the internal couple.

**Solution.** Once \(a\) is obtained from force equilibrium, the internal tensile and compressive resultants form a couple with lever arm \(d-a/2\). Therefore \(M_n=A_sf_y(d-a/2)\). Maintain consistent force and length units so the resulting moment unit is correct.

---

## 26.3 Strength-reduction and design check

Use the strength-reduction factor associated with the strain condition or relation supplied by the Handbook/problem. Do not mix nominal and design strength.

\[\phi M_n\ge M_u\]

![FIG-03-26-003: Concrete flexural design flow from strains to Mn, φ, and comparison with Mu.](../figures/FIG-03-26-003-strength-reduction-and-design-check.png)

### Worked Example 3

**Problem.** If Mn=200 kip-ft and φ=0.90, design strength is 180 kip-ft.

**Solution.** Design strength is \(\phi M_n\). With \(M_n=200\ \text{kip-ft}\) and \(\phi=0.90\), \(\phi M_n=0.90(200)=180\ \text{kip-ft}\). This available strength is then compared with the factored moment demand.

---

## 26.4 Reinforced concrete beam shear

Concrete and transverse reinforcement may both contribute to shear resistance. Check the specific relation supplied for the problem.

\[\phi(V_c+V_s)\ge V_u\]

![FIG-03-26-004: RC beam with diagonal shear cracks, stirrups, shear span, and contributions Vc and Vs.](../figures/FIG-03-26-004-reinforced-concrete-beam-shear.png)

### Worked Example 4

**Problem.** Stirrups increase Vs by providing transverse reinforcement crossing diagonal cracks.

**Solution.** Concrete alone has limited diagonal-tension capacity after cracking. Stirrups cross potential diagonal cracks and develop tensile force, adding a shear contribution \(V_s\) to the concrete contribution \(V_c\). The design check uses the applicable strength-reduction factor on the total nominal shear strength.

---

## 26.5 Development, anchorage, and reinforcement placement

Reinforcing steel must develop stress through bond. Bar placement affects effective depth, cover, spacing, and constructability.

\[\text{available development length}\ge l_d\]

![FIG-03-26-005: Rebar development and anchorage detail with cover, hook, lap, and effective depth labels.](../figures/FIG-03-26-005-development-anchorage-and-reinforcement-placement.png)

### Worked Example 5

**Problem.** A bar cut off too close to a high-moment region may not develop the assumed tensile force.

**Solution.** Development length ensures that reinforcement can transfer its required stress into the surrounding concrete through bond. Cutting a bar off before sufficient development length is available can prevent the assumed tensile force from developing, even if the flexural calculation based on full yield strength appears adequate.

---

## 26.6 Axially loaded concrete columns

Concrete columns carry load through both concrete and longitudinal reinforcement. Actual design strength includes code reductions and eccentricity considerations.

\[P_n\approx 0.85f'_c(A_g-A_s)+f_yA_s\]

![FIG-03-26-006: Tied reinforced-concrete column cross-section with longitudinal bars, ties, Ag, As, and load P.](../figures/FIG-03-26-006-axially-loaded-concrete-columns.png)

### Worked Example 6

**Problem.** Increasing gross area generally increases axial nominal strength, all else equal.

**Solution.** For a reinforced-concrete column, axial nominal strength depends strongly on gross concrete area and longitudinal reinforcement. Increasing gross area generally raises axial capacity when material strengths and reinforcement ratio are otherwise comparable, although slenderness and eccentricity may still govern.

---

## 26.7 Beam-column interaction and eccentric loading

Columns rarely carry perfectly concentric load. Axial force and bending moment interact; a capacity curve organizes acceptable combinations.

\[\text{capacity depends on }(P,M)\]

![FIG-03-26-007: P-M interaction diagram for a reinforced-concrete column with representative demand points.](../figures/FIG-03-26-007-beam-column-interaction-and-eccentric-loading.png)

### Worked Example 7

**Problem.** More eccentricity generally shifts demand toward a flexure-dominated condition.

**Solution.** Axial load with increasing eccentricity produces a larger bending moment \(M=Pe\). As eccentricity grows, the demand point moves along the axial-force/moment interaction relationship toward a flexure-dominated condition and away from nearly concentric compression.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a reinforced-concrete member, first establish equilibrium and strain-compatible section forces, then apply the strength-reduction factor and compare with factored demand. Development, shear reinforcement, and interaction effects are separate checks and should not be assumed satisfied by a flexural-strength calculation.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook reinforced-concrete expressions and stated resistance factors for the exam. Remembered code provisions may come from another edition or may use different assumptions for stress blocks, development, or column interaction; the Handbook form should govern.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 11; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-026-04` — ACI Committee 318. (2025). *Building Code for Structural Concrete—Code Requirements and Commentary* (ACI CODE-318-25). American Concrete Institute. Cited at publication/standard level; no page-level claim.
- `CIV-3-026-07` — ACI Committee 318. (2025). *Building Code for Structural Concrete—Code Requirements and Commentary* (ACI CODE-318-25). American Concrete Institute. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

## Where This Goes Wrong

**Using reinforced concrete flexure without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using RC beam nominal moment without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using RC design strength without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using RC beam shear without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using reinforcement development without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using RC column axial strength without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using RC interaction without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| reinforced concrete flexure | Concept developed in §26.1; apply with that section's stated assumptions and units. |
| RC beam nominal moment | Concept developed in §26.2; apply with that section's stated assumptions and units. |
| RC design strength | Concept developed in §26.3; apply with that section's stated assumptions and units. |
| RC beam shear | Concept developed in §26.4; apply with that section's stated assumptions and units. |
| reinforcement development | Concept developed in §26.5; apply with that section's stated assumptions and units. |
| RC column axial strength | Concept developed in §26.6; apply with that section's stated assumptions and units. |
| RC interaction | Concept developed in §26.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **reinforced concrete flexure** and identify the principal quantity, relation, or decision it organizes.

2. Define **RC beam nominal moment** and identify the principal quantity, relation, or decision it organizes.

3. Define **RC design strength** and identify the principal quantity, relation, or decision it organizes.

4. Define **RC beam shear** and identify the principal quantity, relation, or decision it organizes.

5. Define **reinforcement development** and identify the principal quantity, relation, or decision it organizes.

6. Define **RC column axial strength** and identify the principal quantity, relation, or decision it organizes.

7. Define **RC interaction** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **reinforced concrete flexure**?

9. What assumption or unit error is most likely to cause a wrong result when applying **RC beam nominal moment**?

10. What assumption or unit error is most likely to cause a wrong result when applying **RC design strength**?

11. What assumption or unit error is most likely to cause a wrong result when applying **RC beam shear**?

12. What assumption or unit error is most likely to cause a wrong result when applying **reinforcement development**?

13. What assumption or unit error is most likely to cause a wrong result when applying **RC column axial strength**?

14. What assumption or unit error is most likely to cause a wrong result when applying **RC interaction**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **reinforced concrete flexure**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **RC beam nominal moment**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **RC design strength**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **RC beam shear**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **reinforcement development**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **RC column axial strength**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **RC interaction**?
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

1. **reinforced concrete flexure** is developed in §26.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **RC beam nominal moment** is developed in §26.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **RC design strength** is developed in §26.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **RC beam shear** is developed in §26.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **reinforcement development** is developed in §26.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **RC column axial strength** is developed in §26.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **RC interaction** is developed in §26.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **reinforced concrete flexure**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **RC beam nominal moment**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **RC design strength**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **RC beam shear**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **reinforcement development**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **RC column axial strength**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **RC interaction**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. Sketch the reinforced-concrete section, neutral axis, compression block, reinforcement location, and eccentric load before selecting flexural, shear, or interaction equations.

16. Use the Handbook reinforced-concrete relation where supplied, and use the cited ACI code only for learned design provisions not printed in the Handbook.

17. Concrete design mixes psi or ksi, inches, square inches, and kip-in or kip-ft; convert consistently before section forces and moments are compared.

18. Check equilibrium and capacity: compression and tension resultants should balance for the assumed section state, and the reduced design strength must meet or exceed the factored demand.

19. **A.** For **Concrete flexural design assumptions**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Singly reinforced rectangular beam strength**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Strength-reduction and design check**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Reinforced concrete beam shear**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Development, anchorage, and reinforcement placement**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Axially loaded concrete columns**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Beam-column interaction and eccentric loading**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Reinforced Concrete Design — Beams and Columns, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Shear and beam-column interaction provisions beyond Handbook equations are labeled learned material and supported by ACI CODE-318-25 rather than assigned a false Handbook page.



---

## Practice Problems

1. For a singly reinforced rectangular beam, locate the compression block so C equals T.

2. Once a is known from force equilibrium, compute Mn from the internal couple.

3. If Mn=200 kip-ft and φ=0.90, design strength is 180 kip-ft.

4. Stirrups increase Vs by providing transverse reinforcement crossing diagonal cracks.

5. A bar cut off too close to a high-moment region may not develop the assumed tensile force.

6. Increasing gross area generally increases axial nominal strength, all else equal.

7. More eccentricity generally shifts demand toward a flexure-dominated condition.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. **Independent check for §26.1.** Rework the problem from the stated givens rather than copying the worked-example result. For a singly reinforced rectangular section, equilibrium requires compression equal tension: \(C=T\). With the rectangular stress block, \(C=0.85f'_cba\) and \(T=A_sf_y\) when the steel yields; solve \(0.85f'_cba=A_sf_y\) for the compression-block depth \(a\). **Check:** confirm the final magnitude and units against the physical meaning of §26.1 before accepting the answer.



2. **Independent check for §26.2.** Rework the problem from the stated givens rather than copying the worked-example result. Once \(a\) is obtained from force equilibrium, the internal tensile and compressive resultants form a couple with lever arm \(d-a/2\). Therefore \(M_n=A_sf_y(d-a/2)\). Maintain consistent force and length units so the resulting moment unit is correct. **Check:** confirm the final magnitude and units against the physical meaning of §26.2 before accepting the answer.



3. **Independent check for §26.3.** Rework the problem from the stated givens rather than copying the worked-example result. Design strength is \(\phi M_n\). With \(M_n=200\ \text{kip-ft}\) and \(\phi=0.90\), \(\phi M_n=0.90(200)=180\ \text{kip-ft}\). This available strength is then compared with the factored moment demand. **Check:** confirm the final magnitude and units against the physical meaning of §26.3 before accepting the answer.



4. **Independent check for §26.4.** Rework the problem from the stated givens rather than copying the worked-example result. Concrete alone has limited diagonal-tension capacity after cracking. Stirrups cross potential diagonal cracks and develop tensile force, adding a shear contribution \(V_s\) to the concrete contribution \(V_c\). The design check uses the applicable strength-reduction factor on the total nominal shear strength. **Check:** confirm the final magnitude and units against the physical meaning of §26.4 before accepting the answer.



5. **Independent check for §26.5.** Rework the problem from the stated givens rather than copying the worked-example result. Development length ensures that reinforcement can transfer its required stress into the surrounding concrete through bond. Cutting a bar off before sufficient development length is available can prevent the assumed tensile force from developing, even if the flexural calculation based on full yield strength appears adequate. **Check:** confirm the final magnitude and units against the physical meaning of §26.5 before accepting the answer.



6. **Independent check for §26.6.** Rework the problem from the stated givens rather than copying the worked-example result. For a reinforced-concrete column, axial nominal strength depends strongly on gross concrete area and longitudinal reinforcement. Increasing gross area generally raises axial capacity when material strengths and reinforcement ratio are otherwise comparable, although slenderness and eccentricity may still govern. **Check:** confirm the final magnitude and units against the physical meaning of §26.6 before accepting the answer.



7. **Independent check for §26.7.** Rework the problem from the stated givens rather than copying the worked-example result. Axial load with increasing eccentricity produces a larger bending moment \(M=Pe\). As eccentricity grows, the demand point moves along the axial-force/moment interaction relationship toward a flexure-dominated condition and away from nearly concentric compression. **Check:** confirm the final magnitude and units against the physical meaning of §26.7 before accepting the answer.



8. Before accepting a reinforced concrete design — beams and columns result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Begin with **FE Civil specification Area 11** and the reinforced-concrete relations identified in the ledger; use ACI 318 only for the reconciled learned/code portion.

10. For reinforced concrete design — beams and columns, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 11.

- **reinforced concrete flexure:** Concrete flexural design assumptions
- **RC beam nominal moment:** Singly reinforced rectangular beam strength
- **RC design strength:** Strength-reduction and design check
- **RC beam shear:** Reinforced concrete beam shear
- **reinforcement development:** Development, anchorage, and reinforcement placement
- **RC column axial strength:** Axially loaded concrete columns
- **RC interaction:** Beam-column interaction and eccentric loading

---

## What's Next

**Chapter 03-27: Soil Classification, Phase Relations, Compaction, and Effective Stress**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
