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

**Solution.** The beam differential relations are \(dV/dx=-w\) and \(dM/dx=V\). If shear is constant and positive over a region, integrating \(dM/dx=V\) gives a moment diagram that increases linearly with \(x\).

---

## 23.2 Truss analysis by joints

At each pin-jointed truss joint, member forces are axial. Start at a joint with no more than two unknown member forces when possible.

\[\sum F_x=0,\qquad \sum F_y=0\]

![FIG-03-23-002: Truss with one isolated joint free-body diagram and member-force arrows.](../figures/FIG-03-23-002-truss-analysis-by-joints.png)

### Worked Example 2

**Problem.** Assume unknown member forces in tension; a negative result indicates compression.

**Solution.** At a truss joint, assume each unknown member force acts in tension, pointing away from the joint, and solve \(\sum F_x=0\) and \(\sum F_y=0\). If the computed force is negative, the actual member force is opposite the assumed direction and the member is in compression.

---

## 23.3 Truss analysis by sections

A section cut can solve selected member forces without analyzing the entire truss. Cut through no more than three unknown members for a planar truss.

\[\sum M=0\]

![FIG-03-23-003: Truss cut through three members with one side isolated for equilibrium.](../figures/FIG-03-23-003-truss-analysis-by-sections.png)

### Worked Example 3

**Problem.** Take moments about the intersection of two cut members to eliminate them.

**Solution.** For the method of sections, cut through no more than three unknown member forces in a planar truss. Taking moments about the intersection of two cut-member lines eliminates those two forces from the moment equation, allowing the third cut force to be found directly.

---

## 23.4 Frame and machine equilibrium

Frames include multi-force members and may transfer moments; do not apply truss two-force assumptions automatically.

\[\sum F_x=0,\ \sum F_y=0,\ \sum M=0\]

![FIG-03-23-004: Pin-connected frame with separated member free-body diagrams and internal pin forces.](../figures/FIG-03-23-004-frame-and-machine-equilibrium.png)

### Worked Example 4

**Problem.** A pin-connected frame member with three applied forces is generally a multi-force member.

**Solution.** A two-force member carries forces only at two points and those forces must be equal, opposite, and collinear. A member acted on by three distinct forces does not satisfy that definition and must generally be analyzed as a multi-force rigid body using all planar equilibrium equations.

---

## 23.5 Beam deflection by integration and superposition

Elastic-curve relations connect bending moment, rotation, and deflection. Boundary conditions determine integration constants.

\[EI\,v''(x)=M(x)\]

![FIG-03-23-005: Beam with bending-moment diagram and corresponding exaggerated elastic curve showing slope and deflection.](../figures/FIG-03-23-005-beam-deflection-by-integration-and-superposition.png)

### Worked Example 5

**Problem.** A simply supported beam has zero deflection at both supports.

**Solution.** For a simply supported beam, the vertical displacement boundary conditions are \(v=0\) at each support. Integrating \(EI\,v''=M(x)\) introduces constants that are evaluated from those support conditions; rotations are generally not zero at simple supports.

---

## 23.6 Truss deflection by virtual work or unit load

The unit-load method evaluates displacement from real member force N and virtual member force n caused by a unit load at the desired displacement location.

\[\delta=\sum \frac{N\,n\,L}{AE}\]

![FIG-03-23-006: Truss shown once with real loads and once with a unit virtual load at the target displacement.](../figures/FIG-03-23-006-truss-deflection-by-virtual-work-or-unit-load.png)

### Worked Example 6

**Problem.** Only members carrying force in either system contribute to the summation.

**Solution.** In the unit-load method for a truss, \(\delta=\sum NnL/(AE)\). A member contributes zero whenever either the real-load force \(N\) or unit-load force \(n\) is zero, because the product \(Nn\) vanishes.

---

## 23.7 Frame deflection and structural-analysis checks

Frame deflection may be dominated by bending. Use symmetry, boundary conditions, and order-of-magnitude checks to catch sign or support errors.

\[\delta=\sum \int \frac{M\,m}{EI}\,dx\]

![FIG-03-23-007: Portal frame with real bending diagram, unit-load bending diagram, and lateral deflection shape.](../figures/FIG-03-23-007-frame-deflection-and-structural-analysis-checks.png)

### Worked Example 7

**Problem.** A fixed support has zero translation and zero rotation in the ideal model.

**Solution.** For a fixed support in the ideal planar model, both translation and rotation are restrained. Accordingly, the displacement and rotation compatibility conditions at that support are zero, providing the boundary conditions needed for frame-deflection calculations.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a combined beam/truss/frame problem, first solve the real-load internal forces using equilibrium, then define the displacement direction of interest and apply the corresponding unit load or integration method. Keep real-load and virtual/unit-load quantities clearly distinguished.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook beam, truss, and deflection formulas only with the support conditions and loading cases for which they are derived. If a remembered table entry has different end restraints or load placement, the Handbook case that matches the actual model should govern.

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

15. Sketch the beam, truss, or frame with supports, loads, member axes, and the requested displacement direction before analysis so internal-force and compatibility equations refer to the correct model.

16. Use the Handbook beam, truss, and deflection case that matches the actual support and loading conditions because a table entry for a different restraint pattern is not interchangeable.

17. Keep force, length, modulus, area, and moment-of-inertia units consistent; mixing kN with inches or ksi with metric section properties corrupts both force and deflection results.

18. Check diagram behavior and compatibility: shear changes with load, moment slope follows shear, simple supports have zero displacement, and computed deflection direction should agree with the loading.

19. **A.** For **Beam reactions, shear, and moment**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Truss analysis by joints**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Truss analysis by sections**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Frame and machine equilibrium**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Beam deflection by integration and superposition**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Truss deflection by virtual work or unit load**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Frame deflection and structural-analysis checks**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Structural Analysis — Beams, Trusses, Frames, and Deflections, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Core beam/truss/frame relations are tied to the Handbook and ledger; any additional derivation in this chapter is identified as guide synthesis rather than given a fabricated Handbook citation.



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

1. **Independent check for §23.1.** Rework the problem from the stated givens rather than copying the worked-example result. The beam differential relations are \(dV/dx=-w\) and \(dM/dx=V\). If shear is constant and positive over a region, integrating \(dM/dx=V\) gives a moment diagram that increases linearly with \(x\). **Check:** confirm the final magnitude and units against the physical meaning of §23.1 before accepting the answer.



2. **Independent check for §23.2.** Rework the problem from the stated givens rather than copying the worked-example result. At a truss joint, assume each unknown member force acts in tension, pointing away from the joint, and solve \(\sum F_x=0\) and \(\sum F_y=0\). If the computed force is negative, the actual member force is opposite the assumed direction and the member is in compression. **Check:** confirm the final magnitude and units against the physical meaning of §23.2 before accepting the answer.



3. **Independent check for §23.3.** Rework the problem from the stated givens rather than copying the worked-example result. For the method of sections, cut through no more than three unknown member forces in a planar truss. Taking moments about the intersection of two cut-member lines eliminates those two forces from the moment equation, allowing the third cut force to be found directly. **Check:** confirm the final magnitude and units against the physical meaning of §23.3 before accepting the answer.



4. **Independent check for §23.4.** Rework the problem from the stated givens rather than copying the worked-example result. A two-force member carries forces only at two points and those forces must be equal, opposite, and collinear. A member acted on by three distinct forces does not satisfy that definition and must generally be analyzed as a multi-force rigid body using all planar equilibrium equations. **Check:** confirm the final magnitude and units against the physical meaning of §23.4 before accepting the answer.



5. **Independent check for §23.5.** Rework the problem from the stated givens rather than copying the worked-example result. For a simply supported beam, the vertical displacement boundary conditions are \(v=0\) at each support. Integrating \(EI\,v''=M(x)\) introduces constants that are evaluated from those support conditions; rotations are generally not zero at simple supports. **Check:** confirm the final magnitude and units against the physical meaning of §23.5 before accepting the answer.



6. **Independent check for §23.6.** Rework the problem from the stated givens rather than copying the worked-example result. In the unit-load method for a truss, \(\delta=\sum NnL/(AE)\). A member contributes zero whenever either the real-load force \(N\) or unit-load force \(n\) is zero, because the product \(Nn\) vanishes. **Check:** confirm the final magnitude and units against the physical meaning of §23.6 before accepting the answer.



7. **Independent check for §23.7.** Rework the problem from the stated givens rather than copying the worked-example result. For a fixed support in the ideal planar model, both translation and rotation are restrained. Accordingly, the displacement and rotation compatibility conditions at that support are zero, providing the boundary conditions needed for frame-deflection calculations. **Check:** confirm the final magnitude and units against the physical meaning of §23.7 before accepting the answer.



8. Before accepting a structural analysis — beams, trusses, frames, and deflections result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Start with **FE Civil specification Area 11** and the specific beam, truss, frame, or deflection case cited in the chapter ledger; verify that its restraint and loading case matches the problem.

10. For structural analysis — beams, trusses, frames, and deflections, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

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
