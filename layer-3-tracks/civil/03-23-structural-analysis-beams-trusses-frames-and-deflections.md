---
chapter: "03-23"
title: "Structural Analysis — Beams, Trusses, Frames, and Deflections"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-023-01, CIV-3-023-02, CIV-3-023-03, CIV-3-023-04, CIV-3-023-05, CIV-3-023-06, CIV-3-023-07]
routes: [civil]
status: drafted
---

# Chapter 03-23: Structural Analysis — Beams, Trusses, Frames, and Deflections

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** MECH-2C-039-01 · MECH-2C-024-01

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Structural Analysis — Beams, Trusses, Frames, and Deflections**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **23.1** Explain and apply **Beam reactions, shear, and moment**.
* **23.2** Explain and apply **Truss analysis by joints**.
* **23.3** Explain and apply **Truss analysis by sections**.
* **23.4** Explain and apply **Frame and machine equilibrium**.
* **23.5** Explain and apply **Beam deflection by integration and superposition**.
* **23.6** Explain and apply **Truss deflection by virtual work or unit load**.
* **23.7** Explain and apply **Frame deflection and structural-analysis checks**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 23.1 Beam reactions, shear, and moment

Beam analysis proceeds from support reactions to shear and moment. Consistent sign conventions are essential.

\[\frac{dV}{dx}=-w,\qquad \frac{dM}{dx}=V\]

![FIG-03-23-001: Loaded beam with reaction diagram, shear diagram, and bending-moment diagram aligned by x-coordinate.](../figures/FIG-03-23-001-beam-reactions-shear-and-moment.png)

### Worked Example 1

**Problem.** A region with constant positive shear has linearly increasing moment.

**Solution.** Apply the relation and definitions in §23.1; the stated result follows with consistent units and sign convention.

---

## 23.2 Truss analysis by joints

At each pin-jointed truss joint, member forces are axial. Start at a joint with no more than two unknown member forces when possible.

\[\sum F_x=0,\qquad \sum F_y=0\]

![FIG-03-23-002: Truss with one isolated joint free-body diagram and member-force arrows.](../figures/FIG-03-23-002-truss-analysis-by-joints.png)

### Worked Example 2

**Problem.** Assume unknown member forces in tension; a negative result indicates compression.

**Solution.** Apply the relation and definitions in §23.2; the stated result follows with consistent units and sign convention.

---

## 23.3 Truss analysis by sections

A section cut can solve selected member forces without analyzing the entire truss. Cut through no more than three unknown members for a planar truss.

\[\sum M=0\]

![FIG-03-23-003: Truss cut through three members with one side isolated for equilibrium.](../figures/FIG-03-23-003-truss-analysis-by-sections.png)

### Worked Example 3

**Problem.** Take moments about the intersection of two cut members to eliminate them.

**Solution.** Apply the relation and definitions in §23.3; the stated result follows with consistent units and sign convention.

---

## 23.4 Frame and machine equilibrium

Frames include multi-force members and may transfer moments; do not apply truss two-force assumptions automatically.

\[\sum F_x=0,\ \sum F_y=0,\ \sum M=0\]

![FIG-03-23-004: Pin-connected frame with separated member free-body diagrams and internal pin forces.](../figures/FIG-03-23-004-frame-and-machine-equilibrium.png)

### Worked Example 4

**Problem.** A pin-connected frame member with three applied forces is generally a multi-force member.

**Solution.** Apply the relation and definitions in §23.4; the stated result follows with consistent units and sign convention.

---

## 23.5 Beam deflection by integration and superposition

Elastic-curve relations connect bending moment, rotation, and deflection. Boundary conditions determine integration constants.

\[EI\,v''(x)=M(x)\]

![FIG-03-23-005: Beam with bending-moment diagram and corresponding exaggerated elastic curve showing slope and deflection.](../figures/FIG-03-23-005-beam-deflection-by-integration-and-superposition.png)

### Worked Example 5

**Problem.** A simply supported beam has zero deflection at both supports.

**Solution.** Apply the relation and definitions in §23.5; the stated result follows with consistent units and sign convention.

---

## 23.6 Truss deflection by virtual work or unit load

The unit-load method evaluates displacement from real member force N and virtual member force n caused by a unit load at the desired displacement location.

\[\delta=\sum \frac{N\,n\,L}{AE}\]

![FIG-03-23-006: Truss shown once with real loads and once with a unit virtual load at the target displacement.](../figures/FIG-03-23-006-truss-deflection-by-virtual-work-or-unit-load.png)

### Worked Example 6

**Problem.** Only members carrying force in either system contribute to the summation.

**Solution.** Apply the relation and definitions in §23.6; the stated result follows with consistent units and sign convention.

---

## 23.7 Frame deflection and structural-analysis checks

Frame deflection may be dominated by bending. Use symmetry, boundary conditions, and order-of-magnitude checks to catch sign or support errors.

\[\delta=\sum \int \frac{M\,m}{EI}\,dx\]

![FIG-03-23-007: Portal frame with real bending diagram, unit-load bending diagram, and lateral deflection shape.](../figures/FIG-03-23-007-frame-deflection-and-structural-analysis-checks.png)

### Worked Example 7

**Problem.** A fixed support has zero translation and zero rotation in the ideal model.

**Solution.** Apply the relation and definitions in §23.7; the stated result follows with consistent units and sign convention.

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

**Using beam internal forces without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using method of joints without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using method of sections without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using frame analysis without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using beam deflection without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using truss deflection without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using frame deflection without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| beam internal forces | Concept developed in §23.1; apply with that section's stated assumptions and units. |
| method of joints | Concept developed in §23.2; apply with that section's stated assumptions and units. |
| method of sections | Concept developed in §23.3; apply with that section's stated assumptions and units. |
| frame analysis | Concept developed in §23.4; apply with that section's stated assumptions and units. |
| beam deflection | Concept developed in §23.5; apply with that section's stated assumptions and units. |
| truss deflection | Concept developed in §23.6; apply with that section's stated assumptions and units. |
| frame deflection | Concept developed in §23.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **beam internal forces** and identify the principal quantity, relation, or decision it organizes.

2. Define **method of joints** and identify the principal quantity, relation, or decision it organizes.

3. Define **method of sections** and identify the principal quantity, relation, or decision it organizes.

4. Define **frame analysis** and identify the principal quantity, relation, or decision it organizes.

5. Define **beam deflection** and identify the principal quantity, relation, or decision it organizes.

6. Define **truss deflection** and identify the principal quantity, relation, or decision it organizes.

7. Define **frame deflection** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **beam internal forces**?

9. What assumption or unit error is most likely to cause a wrong result when applying **method of joints**?

10. What assumption or unit error is most likely to cause a wrong result when applying **method of sections**?

11. What assumption or unit error is most likely to cause a wrong result when applying **frame analysis**?

12. What assumption or unit error is most likely to cause a wrong result when applying **beam deflection**?

13. What assumption or unit error is most likely to cause a wrong result when applying **truss deflection**?

14. What assumption or unit error is most likely to cause a wrong result when applying **frame deflection**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **beam internal forces**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **method of joints**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **method of sections**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **frame analysis**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **beam deflection**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **truss deflection**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **frame deflection**?
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

1. **beam internal forces** is developed in §23.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **method of joints** is developed in §23.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **method of sections** is developed in §23.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **frame analysis** is developed in §23.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **beam deflection** is developed in §23.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **truss deflection** is developed in §23.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **frame deflection** is developed in §23.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **beam internal forces**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **method of joints**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **method of sections**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **frame analysis**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **beam deflection**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **truss deflection**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **frame deflection**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

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

1. A region with constant positive shear has linearly increasing moment.

2. Assume unknown member forces in tension; a negative result indicates compression.

3. Take moments about the intersection of two cut members to eliminate them.

4. A pin-connected frame member with three applied forces is generally a multi-force member.

5. A simply supported beam has zero deflection at both supports.

6. Only members carrying force in either system contribute to the summation.

7. A fixed support has zero translation and zero rotation in the ideal model.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §23.1. A region with constant positive shear has linearly increasing moment. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §23.2. Assume unknown member forces in tension; a negative result indicates compression. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §23.3. Take moments about the intersection of two cut members to eliminate them. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §23.4. A pin-connected frame member with three applied forces is generally a multi-force member. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §23.5. A simply supported beam has zero deflection at both supports. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §23.6. Only members carrying force in either system contribute to the summation. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §23.7. A fixed support has zero translation and zero rotation in the ideal model. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 11 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 11.

- **beam internal forces:** Beam reactions, shear, and moment
- **method of joints:** Truss analysis by joints
- **method of sections:** Truss analysis by sections
- **frame analysis:** Frame and machine equilibrium
- **beam deflection:** Beam deflection by integration and superposition
- **truss deflection:** Truss deflection by virtual work or unit load
- **frame deflection:** Frame deflection and structural-analysis checks

---

## What's Next

**Chapter 03-24: Columns, Buckling, and Elementary Indeterminate Structures**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
