---
chapter: "03-24"
title: "Columns, Buckling, and Elementary Indeterminate Structures"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-024-01, CIV-3-024-02, CIV-3-024-03, CIV-3-024-04, CIV-3-024-05, CIV-3-024-06, CIV-3-024-07]
routes: [civil]
status: drafted
---

# Chapter 03-24: Columns, Buckling, and Elementary Indeterminate Structures

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-023-07

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Columns, Buckling, and Elementary Indeterminate Structures**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **24.1** Explain and apply **Euler buckling and effective length**.
* **24.2** Explain and apply **Radius of gyration and slenderness ratio**.
* **24.3** Explain and apply **Inelastic versus elastic column behavior**.
* **24.4** Explain and apply **Compatibility in indeterminate structures**.
* **24.5** Explain and apply **Force method and redundant release**.
* **24.6** Explain and apply **Moment-distribution and stiffness concepts**.
* **24.7** Explain and apply **Second-order effects and stability screening**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 24.1 Euler buckling and effective length

Euler buckling describes ideal elastic instability of slender columns. End restraint enters through effective-length factor K.

\[P_{cr}=\frac{\pi^2EI}{(KL)^2}\]

![FIG-03-24-001: Columns with pinned, fixed, and mixed end conditions showing effective buckling lengths.](../figures/FIG-03-24-001-euler-buckling-and-effective-length.png)

### Worked Example 1

**Problem.** Doubling KL reduces Euler critical load by a factor of four.

**Solution.** Apply the relation and definitions in §24.1; the stated result follows with consistent units and sign convention.

---

## 24.2 Radius of gyration and slenderness ratio

Slenderness compares effective column length with cross-sectional stiffness distribution. Buckling about the weaker axis often governs.

\[\lambda=\frac{KL}{r},\qquad r=\sqrt{\frac{I}{A}}\]

![FIG-03-24-002: Column section with strong and weak axes, radii of gyration, and associated buckling directions.](../figures/FIG-03-24-002-radius-of-gyration-and-slenderness-ratio.png)

### Worked Example 2

**Problem.** If KL=120 in and r=2.0 in, slenderness is 60.

**Solution.** Apply the relation and definitions in §24.2; the stated result follows with consistent units and sign convention.

---

## 24.3 Inelastic versus elastic column behavior

Real design columns transition from yielding-dominated behavior at low slenderness to elastic buckling at high slenderness.

\[\text{column strength}=f\!\left(\frac{KL}{r},F_y,E\right)\]

![FIG-03-24-003: Column compressive strength versus slenderness with inelastic and elastic regions.](../figures/FIG-03-24-003-inelastic-versus-elastic-column-behavior.png)

### Worked Example 3

**Problem.** A short stocky column is less likely to be governed by Euler elastic buckling.

**Solution.** Apply the relation and definitions in §24.3; the stated result follows with consistent units and sign convention.

---

## 24.4 Compatibility in indeterminate structures

Statically indeterminate structures require deformation compatibility in addition to equilibrium. Redundant reactions are not found from statics alone.

\[\text{equilibrium}+\text{compatibility}+\text{constitutive relation}\]

![FIG-03-24-004: Fixed-fixed beam with redundant reactions and a compatibility condition illustrated.](../figures/FIG-03-24-004-compatibility-in-indeterminate-structures.png)

### Worked Example 4

**Problem.** A fixed-fixed beam has more reaction unknowns than planar equilibrium equations.

**Solution.** Apply the relation and definitions in §24.4; the stated result follows with consistent units and sign convention.

---

## 24.5 Force method and redundant release

The force method removes one or more redundants to create a determinate primary structure, then enforces the released displacement condition.

\[\delta_{\text{load}}+R\,f=0\]

![FIG-03-24-005: Three-panel force-method sequence: original indeterminate structure, released primary structure, redundant load case.](../figures/FIG-03-24-005-force-method-and-redundant-release.png)

### Worked Example 5

**Problem.** For one redundant, solve the displacement caused by loads plus redundant effect equal to zero.

**Solution.** Apply the relation and definitions in §24.5; the stated result follows with consistent units and sign convention.

---

## 24.6 Moment-distribution and stiffness concepts

Elementary indeterminate analysis may use relative stiffness to distribute joint moments. Know the physical meaning even when a full code procedure is not required.

\[\text{distribution factor}=\frac{K_i}{\sum K}\]

![FIG-03-24-006: Joint with connected members, relative stiffnesses, distribution factors, and balancing moment arrows.](../figures/FIG-03-24-006-moment-distribution-and-stiffness-concepts.png)

### Worked Example 6

**Problem.** A member with twice the stiffness of another at the joint receives twice the share before carryover effects.

**Solution.** Apply the relation and definitions in §24.6; the stated result follows with consistent units and sign convention.

---

## 24.7 Second-order effects and stability screening

Axial compression acting through lateral displacement increases moments. FE-level problems may treat this conceptually or provide an amplification relation.

\[\text{total response}\approx \text{first-order response}+\text{P-}\Delta\text{ effect}\]

![FIG-03-24-007: Laterally displaced column/frame showing axial P acting through lateral offset Δ and added moment PΔ.](../figures/FIG-03-24-007-second-order-effects-and-stability-screening.png)

### Worked Example 7

**Problem.** Greater axial load or drift increases P-Δ sensitivity.

**Solution.** Apply the relation and definitions in §24.7; the stated result follows with consistent units and sign convention.

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

**Using Euler buckling without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using column slenderness without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using column strength regime without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using deformation compatibility without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using force method without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using stiffness distribution without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using second-order effect without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| Euler buckling | Concept developed in §24.1; apply with that section's stated assumptions and units. |
| column slenderness | Concept developed in §24.2; apply with that section's stated assumptions and units. |
| column strength regime | Concept developed in §24.3; apply with that section's stated assumptions and units. |
| deformation compatibility | Concept developed in §24.4; apply with that section's stated assumptions and units. |
| force method | Concept developed in §24.5; apply with that section's stated assumptions and units. |
| stiffness distribution | Concept developed in §24.6; apply with that section's stated assumptions and units. |
| second-order effect | Concept developed in §24.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **Euler buckling** and identify the principal quantity, relation, or decision it organizes.

2. Define **column slenderness** and identify the principal quantity, relation, or decision it organizes.

3. Define **column strength regime** and identify the principal quantity, relation, or decision it organizes.

4. Define **deformation compatibility** and identify the principal quantity, relation, or decision it organizes.

5. Define **force method** and identify the principal quantity, relation, or decision it organizes.

6. Define **stiffness distribution** and identify the principal quantity, relation, or decision it organizes.

7. Define **second-order effect** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **Euler buckling**?

9. What assumption or unit error is most likely to cause a wrong result when applying **column slenderness**?

10. What assumption or unit error is most likely to cause a wrong result when applying **column strength regime**?

11. What assumption or unit error is most likely to cause a wrong result when applying **deformation compatibility**?

12. What assumption or unit error is most likely to cause a wrong result when applying **force method**?

13. What assumption or unit error is most likely to cause a wrong result when applying **stiffness distribution**?

14. What assumption or unit error is most likely to cause a wrong result when applying **second-order effect**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **Euler buckling**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **column slenderness**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **column strength regime**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **deformation compatibility**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **force method**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **stiffness distribution**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **second-order effect**?
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

1. **Euler buckling** is developed in §24.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **column slenderness** is developed in §24.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **column strength regime** is developed in §24.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **deformation compatibility** is developed in §24.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **force method** is developed in §24.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **stiffness distribution** is developed in §24.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **second-order effect** is developed in §24.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **Euler buckling**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **column slenderness**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **column strength regime**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **deformation compatibility**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **force method**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **stiffness distribution**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **second-order effect**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

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

1. Doubling KL reduces Euler critical load by a factor of four.

2. If KL=120 in and r=2.0 in, slenderness is 60.

3. A short stocky column is less likely to be governed by Euler elastic buckling.

4. A fixed-fixed beam has more reaction unknowns than planar equilibrium equations.

5. For one redundant, solve the displacement caused by loads plus redundant effect equal to zero.

6. A member with twice the stiffness of another at the joint receives twice the share before carryover effects.

7. Greater axial load or drift increases P-Δ sensitivity.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §24.1. Doubling KL reduces Euler critical load by a factor of four. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §24.2. If KL=120 in and r=2.0 in, slenderness is 60. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §24.3. A short stocky column is less likely to be governed by Euler elastic buckling. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §24.4. A fixed-fixed beam has more reaction unknowns than planar equilibrium equations. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §24.5. For one redundant, solve the displacement caused by loads plus redundant effect equal to zero. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §24.6. A member with twice the stiffness of another at the joint receives twice the share before carryover effects. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §24.7. Greater axial load or drift increases P-Δ sensitivity. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 11 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 11.

- **Euler buckling:** Euler buckling and effective length
- **column slenderness:** Radius of gyration and slenderness ratio
- **column strength regime:** Inelastic versus elastic column behavior
- **deformation compatibility:** Compatibility in indeterminate structures
- **force method:** Force method and redundant release
- **stiffness distribution:** Moment-distribution and stiffness concepts
- **second-order effect:** Second-order effects and stability screening

---

## What's Next

**Chapter 03-25: Steel Design — Tension Members, Beams, Columns, and Connections**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
