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

**Solution.** Euler load is \(P_{cr}=\pi^2EI/(KL)^2\). If \(KL\) doubles while \(E\) and \(I\) remain unchanged, the denominator increases by \(2^2=4\), so \(P_{cr}\) becomes one-fourth of its original value.

---

## 24.2 Radius of gyration and slenderness ratio

Slenderness compares effective column length with cross-sectional stiffness distribution. Buckling about the weaker axis often governs.

\[\lambda=\frac{KL}{r},\qquad r=\sqrt{\frac{I}{A}}\]

![FIG-03-24-002: Column section with strong and weak axes, radii of gyration, and associated buckling directions.](../figures/FIG-03-24-002-radius-of-gyration-and-slenderness-ratio.png)

### Worked Example 2

**Problem.** If KL=120 in and r=2.0 in, slenderness is 60.

**Solution.** Slenderness is \(\lambda=KL/r\). With \(KL=120\ \text{in}\) and \(r=2.0\ \text{in}\), \(\lambda=120/2.0=60\). The inches cancel, so slenderness is dimensionless.

---

## 24.3 Inelastic versus elastic column behavior

Real design columns transition from yielding-dominated behavior at low slenderness to elastic buckling at high slenderness.

\[\text{column strength}=f\!\left(\frac{KL}{r},F_y,E\right)\]

![FIG-03-24-003: Column compressive strength versus slenderness with inelastic and elastic regions.](../figures/FIG-03-24-003-inelastic-versus-elastic-column-behavior.png)

### Worked Example 3

**Problem.** A short stocky column is less likely to be governed by Euler elastic buckling.

**Solution.** Euler buckling describes slender-column elastic instability. A short, stocky column has a relatively small \(KL/r\), so material yielding or inelastic column behavior is more likely to control before ideal Euler buckling is reached.

---

## 24.4 Compatibility in indeterminate structures

Statically indeterminate structures require deformation compatibility in addition to equilibrium. Redundant reactions are not found from statics alone.

\[\text{equilibrium}+\text{compatibility}+\text{constitutive relation}\]

![FIG-03-24-004: Fixed-fixed beam with redundant reactions and a compatibility condition illustrated.](../figures/FIG-03-24-004-compatibility-in-indeterminate-structures.png)

### Worked Example 4

**Problem.** A fixed-fixed beam has more reaction unknowns than planar equilibrium equations.

**Solution.** A fixed-fixed beam develops more reaction components than can be solved from the three independent planar equilibrium equations alone. The additional unknowns require deformation compatibility together with force-deformation relations, making the structure statically indeterminate.

---

## 24.5 Force method and redundant release

The force method removes one or more redundants to create a determinate primary structure, then enforces the released displacement condition.

\[\delta_{\text{load}}+R\,f=0\]

![FIG-03-24-005: Three-panel force-method sequence: original indeterminate structure, released primary structure, redundant load case.](../figures/FIG-03-24-005-force-method-and-redundant-release.png)

### Worked Example 5

**Problem.** For one redundant, solve the displacement caused by loads plus redundant effect equal to zero.

**Solution.** In the force method with one redundant \(R\), release the redundant to form a determinate primary structure. Compute the displacement at the released coordinate from the real loads, \(\delta_L\), and the flexibility coefficient \(f\); compatibility requires \(\delta_L+Rf=0\), so \(R=-\delta_L/f\).

---

## 24.6 Moment-distribution and stiffness concepts

Elementary indeterminate analysis may use relative stiffness to distribute joint moments. Know the physical meaning even when a full code procedure is not required.

\[\text{distribution factor}=\frac{K_i}{\sum K}\]

![FIG-03-24-006: Joint with connected members, relative stiffnesses, distribution factors, and balancing moment arrows.](../figures/FIG-03-24-006-moment-distribution-and-stiffness-concepts.png)

### Worked Example 6

**Problem.** A member with twice the stiffness of another at the joint receives twice the share before carryover effects.

**Solution.** A distribution factor is \(DF_i=K_i/\sum K\). If one member stiffness is \(2K\) and another is \(K\), their factors are \(2/3\) and \(1/3\), respectively, so the stiffer member receives twice the distributed unbalanced moment before carryover.

---

## 24.7 Second-order effects and stability screening

Axial compression acting through lateral displacement increases moments. FE-level problems may treat this conceptually or provide an amplification relation.

\[\text{total response}\approx \text{first-order response}+\text{P-}\Delta\text{ effect}\]

![FIG-03-24-007: Laterally displaced column/frame showing axial P acting through lateral offset Δ and added moment PΔ.](../figures/FIG-03-24-007-second-order-effects-and-stability-screening.png)

### Worked Example 7

**Problem.** Greater axial load or drift increases P-Δ sensitivity.

**Solution.** Second-order \(P-\Delta\) effects arise because axial load acts through lateral displacement and creates additional moment. Increasing either axial load \(P\) or drift \(\Delta\) increases that secondary moment, so stability sensitivity grows as either quantity increases.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For an indeterminate-column/frame problem, first establish the first-order equilibrium solution, then impose compatibility or stiffness relations to obtain redundants. Only after the primary response is known should second-order stability effects be screened or amplified.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook column-strength and buckling expressions that correspond to the stated end conditions and effective-length model. A remembered Euler equation is not sufficient when the Handbook indicates inelastic behavior, effective-length factors, or code-style column strength.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 11; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-024-03` — Hibbeler, R. C. (2023). *Mechanics of Materials* (11th ed.). Pearson. ISBN 978-0-13-760561-3. Cited at publication/standard level; no page-level claim.
- `CIV-3-024-04` — Hibbeler, R. C. (2024). *Structural Analysis* (11th ed.). Pearson. ISBN 978-0-13-802625-7. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

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

15. Sketch the column end restraints and the released/compatible degrees of freedom first so effective length, redundant reactions, and second-order displacement are defined before solving.

16. Use the Handbook buckling or stiffness relation that matches the end condition because Euler load and indeterminate-structure formulas depend directly on effective length and restraint assumptions.

17. Column calculations require consistent force, length, modulus, and inertia units; mixing ksi, kips, inches, and metric section properties changes both slenderness and critical load.

18. Check trends: Euler critical load must be positive and should decrease as effective length increases, while an indeterminate solution must satisfy the imposed compatibility condition.

19. **A.** For **Euler buckling and effective length**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Radius of gyration and slenderness ratio**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Inelastic versus elastic column behavior**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Compatibility in indeterminate structures**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Force method and redundant release**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Moment-distribution and stiffness concepts**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Second-order effects and stability screening**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Columns, Buckling, and Elementary Indeterminate Structures, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Inelastic buckling and compatibility details beyond Handbook tables are labeled learned material and supported by the reconciled Hibbeler references rather than an invented Handbook page.



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

1. **Independent check for §24.1.** Rework the problem from the stated givens rather than copying the worked-example result. Euler load is \(P_{cr}=\pi^2EI/(KL)^2\). If \(KL\) doubles while \(E\) and \(I\) remain unchanged, the denominator increases by \(2^2=4\), so \(P_{cr}\) becomes one-fourth of its original value. **Check:** confirm the final magnitude and units against the physical meaning of §24.1 before accepting the answer.



2. **Independent check for §24.2.** Rework the problem from the stated givens rather than copying the worked-example result. Slenderness is \(\lambda=KL/r\). With \(KL=120\ \text{in}\) and \(r=2.0\ \text{in}\), \(\lambda=120/2.0=60\). The inches cancel, so slenderness is dimensionless. **Check:** confirm the final magnitude and units against the physical meaning of §24.2 before accepting the answer.



3. **Independent check for §24.3.** Rework the problem from the stated givens rather than copying the worked-example result. Euler buckling describes slender-column elastic instability. A short, stocky column has a relatively small \(KL/r\), so material yielding or inelastic column behavior is more likely to control before ideal Euler buckling is reached. **Check:** confirm the final magnitude and units against the physical meaning of §24.3 before accepting the answer.



4. **Independent check for §24.4.** Rework the problem from the stated givens rather than copying the worked-example result. A fixed-fixed beam develops more reaction components than can be solved from the three independent planar equilibrium equations alone. The additional unknowns require deformation compatibility together with force-deformation relations, making the structure statically indeterminate. **Check:** confirm the final magnitude and units against the physical meaning of §24.4 before accepting the answer.



5. **Independent check for §24.5.** Rework the problem from the stated givens rather than copying the worked-example result. In the force method with one redundant \(R\), release the redundant to form a determinate primary structure. Compute the displacement at the released coordinate from the real loads, \(\delta_L\), and the flexibility coefficient \(f\); compatibility requires \(\delta_L+Rf=0\), so \(R=-\delta_L/f\). **Check:** confirm the final magnitude and units against the physical meaning of §24.5 before accepting the answer.



6. **Independent check for §24.6.** Rework the problem from the stated givens rather than copying the worked-example result. A distribution factor is \(DF_i=K_i/\sum K\). If one member stiffness is \(2K\) and another is \(K\), their factors are \(2/3\) and \(1/3\), respectively, so the stiffer member receives twice the distributed unbalanced moment before carryover. **Check:** confirm the final magnitude and units against the physical meaning of §24.6 before accepting the answer.



7. **Independent check for §24.7.** Rework the problem from the stated givens rather than copying the worked-example result. Second-order \(P-\Delta\) effects arise because axial load acts through lateral displacement and creates additional moment. Increasing either axial load \(P\) or drift \(\Delta\) increases that secondary moment, so stability sensitivity grows as either quantity increases. **Check:** confirm the final magnitude and units against the physical meaning of §24.7 before accepting the answer.



8. Before accepting a columns, buckling, and elementary indeterminate structures result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Begin with **FE Civil specification Area 11** and the Handbook column/buckling relations in the ledger; use the external mechanics/structural-analysis reference only for the reconciled learned portion.

10. For columns, buckling, and elementary indeterminate structures, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

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
