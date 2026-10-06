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

**Solution.** Apply the relation and definitions in §26.1; the stated result follows with consistent units and sign convention.

---

## 26.2 Singly reinforced rectangular beam strength

Beam flexural strength depends on tensile steel area, yield strength, effective depth, and compression-block depth.

\[M_n=A_sf_y\left(d-\frac{a}{2}\right)\]

![FIG-03-26-002: Singly reinforced beam section with steel area As, effective depth d, compression block a, and internal lever arm.](../figures/FIG-03-26-002-singly-reinforced-rectangular-beam-strength.png)

### Worked Example 2

**Problem.** Once a is known from force equilibrium, compute Mn from the internal couple.

**Solution.** Apply the relation and definitions in §26.2; the stated result follows with consistent units and sign convention.

---

## 26.3 Strength-reduction and design check

Use the strength-reduction factor associated with the strain condition or relation supplied by the Handbook/problem. Do not mix nominal and design strength.

\[\phi M_n\ge M_u\]

![FIG-03-26-003: Concrete flexural design flow from strains to Mn, φ, and comparison with Mu.](../figures/FIG-03-26-003-strength-reduction-and-design-check.png)

### Worked Example 3

**Problem.** If Mn=200 kip-ft and φ=0.90, design strength is 180 kip-ft.

**Solution.** Apply the relation and definitions in §26.3; the stated result follows with consistent units and sign convention.

---

## 26.4 Reinforced concrete beam shear

Concrete and transverse reinforcement may both contribute to shear resistance. Check the specific relation supplied for the problem.

\[\phi(V_c+V_s)\ge V_u\]

![FIG-03-26-004: RC beam with diagonal shear cracks, stirrups, shear span, and contributions Vc and Vs.](../figures/FIG-03-26-004-reinforced-concrete-beam-shear.png)

### Worked Example 4

**Problem.** Stirrups increase Vs by providing transverse reinforcement crossing diagonal cracks.

**Solution.** Apply the relation and definitions in §26.4; the stated result follows with consistent units and sign convention.

---

## 26.5 Development, anchorage, and reinforcement placement

Reinforcing steel must develop stress through bond. Bar placement affects effective depth, cover, spacing, and constructability.

\[\text{available development length}\ge l_d\]

![FIG-03-26-005: Rebar development and anchorage detail with cover, hook, lap, and effective depth labels.](../figures/FIG-03-26-005-development-anchorage-and-reinforcement-placement.png)

### Worked Example 5

**Problem.** A bar cut off too close to a high-moment region may not develop the assumed tensile force.

**Solution.** Apply the relation and definitions in §26.5; the stated result follows with consistent units and sign convention.

---

## 26.6 Axially loaded concrete columns

Concrete columns carry load through both concrete and longitudinal reinforcement. Actual design strength includes code reductions and eccentricity considerations.

\[P_n\approx 0.85f'_c(A_g-A_s)+f_yA_s\]

![FIG-03-26-006: Tied reinforced-concrete column cross-section with longitudinal bars, ties, Ag, As, and load P.](../figures/FIG-03-26-006-axially-loaded-concrete-columns.png)

### Worked Example 6

**Problem.** Increasing gross area generally increases axial nominal strength, all else equal.

**Solution.** Apply the relation and definitions in §26.6; the stated result follows with consistent units and sign convention.

---

## 26.7 Beam-column interaction and eccentric loading

Columns rarely carry perfectly concentric load. Axial force and bending moment interact; a capacity curve organizes acceptable combinations.

\[\text{capacity depends on }(P,M)\]

![FIG-03-26-007: P-M interaction diagram for a reinforced-concrete column with representative demand points.](../figures/FIG-03-26-007-beam-column-interaction-and-eccentric-loading.png)

### Worked Example 7

**Problem.** More eccentricity generally shifts demand toward a flexure-dominated condition.

**Solution.** Apply the relation and definitions in §26.7; the stated result follows with consistent units and sign convention.

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

Primary source basis: **FE Civil specification Area 11; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** Some Civil specification topics are directly tabulated in the Handbook; others are named by the specification but require learned engineering knowledge. This chapter does not imply that every workflow, code provision, or design factor is printed in the Handbook.

Where the FE specification requires a topic that is not directly developed in the Handbook, the ledger marks it **specification-required / guide-developed** rather than inventing a Handbook citation.

---

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

1. Use §26.1. For a singly reinforced rectangular beam, locate the compression block so C equals T. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §26.2. Once a is known from force equilibrium, compute Mn from the internal couple. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §26.3. If Mn=200 kip-ft and φ=0.90, design strength is 180 kip-ft. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §26.4. Stirrups increase Vs by providing transverse reinforcement crossing diagonal cracks. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §26.5. A bar cut off too close to a high-moment region may not develop the assumed tensile force. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §26.6. Increasing gross area generally increases axial nominal strength, all else equal. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §26.7. More eccentricity generally shifts demand toward a flexure-dominated condition. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 11 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

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
