---
chapter: "03-22"
title: "Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-022-01, CIV-3-022-02, CIV-3-022-03, CIV-3-022-04, CIV-3-022-05, CIV-3-022-06, CIV-3-022-07]
routes: [civil]
status: drafted
---

# Chapter 03-22: Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** MECH-2C-026-04 · MECH-2C-024-03

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **22.1** Explain and apply **Structural idealization, supports, and degrees of freedom**.
* **22.2** Explain and apply **Determinacy and stability of beams and frames**.
* **22.3** Explain and apply **Truss determinacy and load path**.
* **22.4** Explain and apply **Dead, live, environmental, and moving loads**.
* **22.5** Explain and apply **Tributary area and gravity load paths**.
* **22.6** Explain and apply **Influence lines for reactions and member actions**.
* **22.7** Explain and apply **Load combinations and design-demand organization**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 22.1 Structural idealization, supports, and degrees of freedom

Structural analysis starts with the idealized model: supports, connectivity, load locations, and member behavior. A wrong support model invalidates every later calculation.

\[\sum F_x=0,\qquad \sum F_y=0,\qquad \sum M=0\]

![FIG-03-22-001: Beam and frame support symbols with corresponding restrained degrees of freedom.](../figures/FIG-03-22-001-structural-idealization-supports-and-degrees-of-freedom.png)

### Worked Example 1

**Problem.** A planar pin contributes two reaction components; a roller typically contributes one.

**Solution.** Apply the relation and definitions in §22.1; the stated result follows with consistent units and sign convention.

---

## 22.2 Determinacy and stability of beams and frames

Determinacy is not the same as stability. A structure can have the right reaction count yet still be geometrically unstable.

\[\text{unknown reactions/internal forces}\ \text{vs. independent equilibrium equations}\]

![FIG-03-22-002: Stable, externally unstable, and internally unstable planar structural examples.](../figures/FIG-03-22-002-determinacy-and-stability-of-beams-and-frames.png)

### Worked Example 2

**Problem.** Three independent reaction components can be statically determinate for a stable planar rigid body.

**Solution.** Apply the relation and definitions in §22.2; the stated result follows with consistent units and sign convention.

---

## 22.3 Truss determinacy and load path

For a simple planar truss, the member-joint-reaction count is a useful screening rule. It does not replace a geometric stability check.

\[m+r\stackrel{?}{=}2j\]

![FIG-03-22-003: Planar truss with joints, members, supports, applied load, and highlighted load path.](../figures/FIG-03-22-003-truss-determinacy-and-load-path.png)

### Worked Example 3

**Problem.** If m=11, r=3, j=7, then m+r=14=2j, a candidate for determinate behavior.

**Solution.** Apply the relation and definitions in §22.3; the stated result follows with consistent units and sign convention.

---

## 22.4 Dead, live, environmental, and moving loads

Loads differ in source, variability, and distribution. FE problems may supply load combinations; use the stated combination rather than inventing code factors.

\[w_{\text{total}}=\sum w_i\]

![FIG-03-22-004: Building bay showing dead, live, roof, wind/lateral, and moving-load concepts with tributary areas.](../figures/FIG-03-22-004-dead-live-environmental-and-moving-loads.png)

### Worked Example 4

**Problem.** A 0.15 kip/ft self-weight and 0.60 kip/ft imposed load total 0.75 kip/ft before factors.

**Solution.** Apply the relation and definitions in §22.4; the stated result follows with consistent units and sign convention.

---

## 22.5 Tributary area and gravity load paths

Tributary area converts distributed surface loading into beam, girder, or column loads. Follow the load path from slab to supports without double counting.

\[P=qA_t\]

![FIG-03-22-005: Floor framing plan with slab tributary strips to beams and tributary areas to columns.](../figures/FIG-03-22-005-tributary-area-and-gravity-load-paths.png)

### Worked Example 5

**Problem.** q=80 psf over 200 ft² produces 16 kip.

**Solution.** Apply the relation and definitions in §22.5; the stated result follows with consistent units and sign convention.

---

## 22.6 Influence lines for reactions and member actions

An influence line shows how a response quantity changes as a unit load moves across a structure. It is different from a shear or moment diagram for a fixed load.

\[\text{response}=\sum P_i\,y_i\]

![FIG-03-22-006: Simply supported beam with moving unit load and reaction/moment influence lines beneath it.](../figures/FIG-03-22-006-influence-lines-for-reactions-and-member-actions.png)

### Worked Example 6

**Problem.** A moving 10-kip load at influence ordinate 0.6 contributes 6 kip to the chosen response.

**Solution.** Apply the relation and definitions in §22.6; the stated result follows with consistent units and sign convention.

---

## 22.7 Load combinations and design-demand organization

Load combinations combine factored effects according to the governing design philosophy. On the FE exam, use factors provided by the applicable relation or problem statement.

\[U=\sum \gamma_i Q_i\]

![FIG-03-22-007: Load-combination worksheet linking load cases to factored design demand.](../figures/FIG-03-22-007-load-combinations-and-design-demand-organization.png)

### Worked Example 7

**Problem.** Apply each factor to the correct load type before combining effects.

**Solution.** Apply the relation and definitions in §22.7; the stated result follows with consistent units and sign convention.

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

**Using structural idealization without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using structural determinacy without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using truss load path without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using structural loads without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using tributary area without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using influence line without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using design load combination without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| structural idealization | Concept developed in §22.1; apply with that section's stated assumptions and units. |
| structural determinacy | Concept developed in §22.2; apply with that section's stated assumptions and units. |
| truss load path | Concept developed in §22.3; apply with that section's stated assumptions and units. |
| structural loads | Concept developed in §22.4; apply with that section's stated assumptions and units. |
| tributary area | Concept developed in §22.5; apply with that section's stated assumptions and units. |
| influence line | Concept developed in §22.6; apply with that section's stated assumptions and units. |
| design load combination | Concept developed in §22.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **structural idealization** and identify the principal quantity, relation, or decision it organizes.

2. Define **structural determinacy** and identify the principal quantity, relation, or decision it organizes.

3. Define **truss load path** and identify the principal quantity, relation, or decision it organizes.

4. Define **structural loads** and identify the principal quantity, relation, or decision it organizes.

5. Define **tributary area** and identify the principal quantity, relation, or decision it organizes.

6. Define **influence line** and identify the principal quantity, relation, or decision it organizes.

7. Define **design load combination** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **structural idealization**?

9. What assumption or unit error is most likely to cause a wrong result when applying **structural determinacy**?

10. What assumption or unit error is most likely to cause a wrong result when applying **truss load path**?

11. What assumption or unit error is most likely to cause a wrong result when applying **structural loads**?

12. What assumption or unit error is most likely to cause a wrong result when applying **tributary area**?

13. What assumption or unit error is most likely to cause a wrong result when applying **influence line**?

14. What assumption or unit error is most likely to cause a wrong result when applying **design load combination**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **structural idealization**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **structural determinacy**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **truss load path**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **structural loads**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **tributary area**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **influence line**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **design load combination**?
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

1. **structural idealization** is developed in §22.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **structural determinacy** is developed in §22.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **truss load path** is developed in §22.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **structural loads** is developed in §22.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **tributary area** is developed in §22.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **influence line** is developed in §22.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **design load combination** is developed in §22.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **structural idealization**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **structural determinacy**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **truss load path**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **structural loads**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **tributary area**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **influence line**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **design load combination**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

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

1. A planar pin contributes two reaction components; a roller typically contributes one.

2. Three independent reaction components can be statically determinate for a stable planar rigid body.

3. If m=11, r=3, j=7, then m+r=14=2j, a candidate for determinate behavior.

4. A 0.15 kip/ft self-weight and 0.60 kip/ft imposed load total 0.75 kip/ft before factors.

5. q=80 psf over 200 ft² produces 16 kip.

6. A moving 10-kip load at influence ordinate 0.6 contributes 6 kip to the chosen response.

7. Apply each factor to the correct load type before combining effects.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §22.1. A planar pin contributes two reaction components; a roller typically contributes one. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §22.2. Three independent reaction components can be statically determinate for a stable planar rigid body. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §22.3. If m=11, r=3, j=7, then m+r=14=2j, a candidate for determinate behavior. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §22.4. A 0.15 kip/ft self-weight and 0.60 kip/ft imposed load total 0.75 kip/ft before factors. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §22.5. q=80 psf over 200 ft² produces 16 kip. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §22.6. A moving 10-kip load at influence ordinate 0.6 contributes 6 kip to the chosen response. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §22.7. Apply each factor to the correct load type before combining effects. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 11 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 11.

- **structural idealization:** Structural idealization, supports, and degrees of freedom
- **structural determinacy:** Determinacy and stability of beams and frames
- **truss load path:** Truss determinacy and load path
- **structural loads:** Dead, live, environmental, and moving loads
- **tributary area:** Tributary area and gravity load paths
- **influence line:** Influence lines for reactions and member actions
- **design load combination:** Load combinations and design-demand organization

---

## What's Next

**Chapter 03-23: Structural Analysis — Beams, Trusses, Frames, and Deflections**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
