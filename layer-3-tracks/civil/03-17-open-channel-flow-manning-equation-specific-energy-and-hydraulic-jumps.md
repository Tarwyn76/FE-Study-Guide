---
chapter: "03-17"
title: "Open-Channel Flow — Manning Equation, Specific Energy, and Hydraulic Jumps"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-017-01, CIV-3-017-02, CIV-3-017-03, CIV-3-017-04, CIV-3-017-05, CIV-3-017-06, CIV-3-017-07]
routes: [civil]
status: drafted
---

# Chapter 03-17: Open-Channel Flow — Manning Equation, Specific Energy, and Hydraulic Jumps

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** FLUID-2D-044-02

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Open-Channel Flow — Manning Equation, Specific Energy, and Hydraulic Jumps**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **17.1** Explain and apply **Open-channel geometry and hydraulic radius**.
* **17.2** Explain and apply **Manning equation and uniform flow**.
* **17.3** Explain and apply **Froude number and flow regime**.
* **17.4** Explain and apply **Specific energy and critical depth**.
* **17.5** Explain and apply **Weirs and open-channel flow measurement**.
* **17.6** Explain and apply **Momentum function and hydraulic jump**.
* **17.7** Explain and apply **Channel controls, normal depth, and gradually varied flow**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 17.1 Open-channel geometry and hydraulic radius

Open-channel calculations use flow area and wetted perimeter, not total perimeter. Hydraulic radius changes with depth.

\[R=\frac{A}{P_w}\]

![FIG-03-17-001: Trapezoidal channel cross-section labeling depth, top width, area, wetted perimeter, and hydraulic radius.](../figures/FIG-03-17-001-open-channel-geometry-and-hydraulic-radius.png)

### Worked Example 1

**Problem.** For A=20 ft² and wetted perimeter 12 ft, R=1.667 ft.

**Solution.** Apply the relation and definitions in §17.1; the stated result follows with consistent units and sign convention.

---

## 17.2 Manning equation and uniform flow

Manning flow assumes approximately uniform, steady open-channel flow. Use the coefficient appropriate to the unit system.

\[Q=\frac{1.49}{n}AR^{2/3}S^{1/2}\quad\text{(USCS)}\]

![FIG-03-17-002: Prismatic channel on slope with energy grade line and variables n, A, R, S, and Q.](../figures/FIG-03-17-002-manning-equation-and-uniform-flow.png)

### Worked Example 2

**Problem.** With n, A, R, and slope given, solve directly for discharge or invert numerically for depth.

**Solution.** Apply the relation and definitions in §17.2; the stated result follows with consistent units and sign convention.

---

## 17.3 Froude number and flow regime

Froude number distinguishes subcritical, critical, and supercritical open-channel flow. Hydraulic depth is area divided by top width.

\[\mathrm{Fr}=\frac{V}{\sqrt{gD_h}}\]

![FIG-03-17-003: Three channel profiles illustrating subcritical, critical, and supercritical flow with Froude numbers.](../figures/FIG-03-17-003-froude-number-and-flow-regime.png)

### Worked Example 3

**Problem.** Fr<1 is subcritical; Fr=1 critical; Fr>1 supercritical.

**Solution.** Apply the relation and definitions in §17.3; the stated result follows with consistent units and sign convention.

---

## 17.4 Specific energy and critical depth

Specific energy is measured relative to the channel bottom. At a given discharge, minimum specific energy corresponds to critical flow.

\[E=y+\frac{V^2}{2g}\]

![FIG-03-17-004: Specific-energy curve E versus depth with critical depth and alternate depths labeled.](../figures/FIG-03-17-004-specific-energy-and-critical-depth.png)

### Worked Example 4

**Problem.** For V=6 ft/s and y=2 ft, E≈2.56 ft.

**Solution.** Apply the relation and definitions in §17.4; the stated result follows with consistent units and sign convention.

---

## 17.5 Weirs and open-channel flow measurement

Weirs relate upstream head to discharge. The exact coefficient and exponent depend on weir geometry; use the equation supplied in the Handbook or problem.

\[Q=C\,L\,H^{3/2}\]

![FIG-03-17-005: Sharp-crested rectangular weir with upstream head H, crest length L, nappe, and discharge Q.](../figures/FIG-03-17-005-weirs-and-open-channel-flow-measurement.png)

### Worked Example 5

**Problem.** Doubling head increases discharge by 2^(3/2) for a rectangular-weir form.

**Solution.** Apply the relation and definitions in §17.5; the stated result follows with consistent units and sign convention.

---

## 17.6 Momentum function and hydraulic jump

A hydraulic jump converts supercritical flow to subcritical flow with substantial energy dissipation while momentum is approximately conserved across the short jump.

\[\mathrm{Fr}_1>1\rightarrow\text{hydraulic jump}\rightarrow\mathrm{Fr}_2<1\]

![FIG-03-17-006: Hydraulic jump profile with y1, y2, roller, energy loss, and upstream/downstream Froude regimes.](../figures/FIG-03-17-006-momentum-function-and-hydraulic-jump.png)

### Worked Example 6

**Problem.** A supercritical approach flow can be forced through a jump in a stilling basin to dissipate energy.

**Solution.** Apply the relation and definitions in §17.6; the stated result follows with consistent units and sign convention.

---

## 17.7 Channel controls, normal depth, and gradually varied flow

Normal depth follows from the uniform-flow relation. Controls such as gates, weirs, slope changes, and downstream water levels create nonuniform profiles.

\[S_f\approx S_0\quad\text{for uniform flow}\]

![FIG-03-17-007: Channel longitudinal profile showing bed slope, normal depth, control section, and backwater curve.](../figures/FIG-03-17-007-channel-controls-normal-depth-and-gradually-varied-flow.png)

### Worked Example 7

**Problem.** If tailwater rises above normal depth, a backwater profile may develop upstream.

**Solution.** Apply the relation and definitions in §17.7; the stated result follows with consistent units and sign convention.

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

**Using hydraulic radius without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using Manning equation without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using Froude number without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using specific energy without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using weir discharge without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using hydraulic jump without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using channel control without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| hydraulic radius | Concept developed in §17.1; apply with that section's stated assumptions and units. |
| Manning equation | Concept developed in §17.2; apply with that section's stated assumptions and units. |
| Froude number | Concept developed in §17.3; apply with that section's stated assumptions and units. |
| specific energy | Concept developed in §17.4; apply with that section's stated assumptions and units. |
| weir discharge | Concept developed in §17.5; apply with that section's stated assumptions and units. |
| hydraulic jump | Concept developed in §17.6; apply with that section's stated assumptions and units. |
| channel control | Concept developed in §17.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **hydraulic radius** and identify the principal quantity, relation, or decision it organizes.

2. Define **Manning equation** and identify the principal quantity, relation, or decision it organizes.

3. Define **Froude number** and identify the principal quantity, relation, or decision it organizes.

4. Define **specific energy** and identify the principal quantity, relation, or decision it organizes.

5. Define **weir discharge** and identify the principal quantity, relation, or decision it organizes.

6. Define **hydraulic jump** and identify the principal quantity, relation, or decision it organizes.

7. Define **channel control** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **hydraulic radius**?

9. What assumption or unit error is most likely to cause a wrong result when applying **Manning equation**?

10. What assumption or unit error is most likely to cause a wrong result when applying **Froude number**?

11. What assumption or unit error is most likely to cause a wrong result when applying **specific energy**?

12. What assumption or unit error is most likely to cause a wrong result when applying **weir discharge**?

13. What assumption or unit error is most likely to cause a wrong result when applying **hydraulic jump**?

14. What assumption or unit error is most likely to cause a wrong result when applying **channel control**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **hydraulic radius**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **Manning equation**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **Froude number**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **specific energy**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **weir discharge**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **hydraulic jump**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **channel control**?
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

1. **hydraulic radius** is developed in §17.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **Manning equation** is developed in §17.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **Froude number** is developed in §17.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **specific energy** is developed in §17.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **weir discharge** is developed in §17.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **hydraulic jump** is developed in §17.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **channel control** is developed in §17.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **hydraulic radius**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **Manning equation**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **Froude number**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **specific energy**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **weir discharge**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **hydraulic jump**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **channel control**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

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

1. For A=20 ft² and wetted perimeter 12 ft, R=1.667 ft.

2. With n, A, R, and slope given, solve directly for discharge or invert numerically for depth.

3. Fr<1 is subcritical; Fr=1 critical; Fr>1 supercritical.

4. For V=6 ft/s and y=2 ft, E≈2.56 ft.

5. Doubling head increases discharge by 2^(3/2) for a rectangular-weir form.

6. A supercritical approach flow can be forced through a jump in a stilling basin to dissipate energy.

7. If tailwater rises above normal depth, a backwater profile may develop upstream.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §17.1. For A=20 ft² and wetted perimeter 12 ft, R=1.667 ft. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §17.2. With n, A, R, and slope given, solve directly for discharge or invert numerically for depth. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §17.3. Fr<1 is subcritical; Fr=1 critical; Fr>1 supercritical. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §17.4. For V=6 ft/s and y=2 ft, E≈2.56 ft. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §17.5. Doubling head increases discharge by 2^(3/2) for a rectangular-weir form. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §17.6. A supercritical approach flow can be forced through a jump in a stilling basin to dissipate energy. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §17.7. If tailwater rises above normal depth, a backwater profile may develop upstream. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 10 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 10.

- **hydraulic radius:** Open-channel geometry and hydraulic radius
- **Manning equation:** Manning equation and uniform flow
- **Froude number:** Froude number and flow regime
- **specific energy:** Specific energy and critical depth
- **weir discharge:** Weirs and open-channel flow measurement
- **hydraulic jump:** Momentum function and hydraulic jump
- **channel control:** Channel controls, normal depth, and gradually varied flow

---

## What's Next

**Chapter 03-18: Pipe Networks, Water Distribution, Pumps, and Collection Systems**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
