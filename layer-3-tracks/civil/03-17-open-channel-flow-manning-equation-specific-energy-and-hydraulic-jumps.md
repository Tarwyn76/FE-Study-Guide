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

**Solution.** Hydraulic radius is \(R=A/P_w\). With \(A=20\ \text{ft}^2\) and wetted perimeter \(P_w=12\ \text{ft}\), \(R=20/12=1.667\ \text{ft}\). Do not substitute top width for wetted perimeter.

---

## 17.2 Manning equation and uniform flow

Manning flow assumes approximately uniform, steady open-channel flow. Use the coefficient appropriate to the unit system.

\[Q=\frac{1.49}{n}AR^{2/3}S^{1/2}\quad\text{(USCS)}\]

![FIG-03-17-002: Prismatic channel on slope with energy grade line and variables n, A, R, S, and Q.](../figures/FIG-03-17-002-manning-equation-and-uniform-flow.png)

### Worked Example 2

**Problem.** With n, A, R, and slope given, solve directly for discharge or invert numerically for depth.

**Solution.** Manning's equation relates \(Q\) to roughness \(n\), flow area \(A\), hydraulic radius \(R\), and energy slope \(S\). If depth is known, compute \(A\) and \(R\) and solve directly for \(Q\); if discharge is known and depth is unknown, depth appears inside both \(A\) and \(R\), so an iterative or numerical solution is normally required.

---

## 17.3 Froude number and flow regime

Froude number distinguishes subcritical, critical, and supercritical open-channel flow. Hydraulic depth is area divided by top width.

\[\mathrm{Fr}=\frac{V}{\sqrt{gD_h}}\]

![FIG-03-17-003: Three channel profiles illustrating subcritical, critical, and supercritical flow with Froude numbers.](../figures/FIG-03-17-003-froude-number-and-flow-regime.png)

### Worked Example 3

**Problem.** Fr<1 is subcritical; Fr=1 critical; Fr>1 supercritical.

**Solution.** The Froude number compares inertial and gravity-wave effects. \(Fr<1\) indicates subcritical flow, \(Fr=1\) critical flow, and \(Fr>1\) supercritical flow. The classification determines how disturbances propagate and is central to evaluating transitions and hydraulic jumps.

---

## 17.4 Specific energy and critical depth

Specific energy is measured relative to the channel bottom. At a given discharge, minimum specific energy corresponds to critical flow.

\[E=y+\frac{V^2}{2g}\]

![FIG-03-17-004: Specific-energy curve E versus depth with critical depth and alternate depths labeled.](../figures/FIG-03-17-004-specific-energy-and-critical-depth.png)

### Worked Example 4

**Problem.** For V=6 ft/s and y=2 ft, E≈2.56 ft.

**Solution.** Specific energy is \(E=y+V^2/(2g)\). With \(y=2\ \text{ft}\), \(V=6\ \text{ft/s}\), and \(g=32.2\ \text{ft/s}^2\), the velocity head is \(36/(64.4)=0.559\ \text{ft}\), so \(E\approx2.56\ \text{ft}\).

---

## 17.5 Weirs and open-channel flow measurement

Weirs relate upstream head to discharge. The exact coefficient and exponent depend on weir geometry; use the equation supplied in the Handbook or problem.

\[Q=C\,L\,H^{3/2}\]

![FIG-03-17-005: Sharp-crested rectangular weir with upstream head H, crest length L, nappe, and discharge Q.](../figures/FIG-03-17-005-weirs-and-open-channel-flow-measurement.png)

### Worked Example 5

**Problem.** Doubling head increases discharge by 2^(3/2) for a rectangular-weir form.

**Solution.** For a rectangular-weir relation \(Q\propto H^{3/2}\). If the head doubles, \(Q_2/Q_1=(2H/H)^{3/2}=2^{3/2}\approx2.83\). Thus the discharge increases by about a factor of **2.83**, not merely by a factor of two.

---

## 17.6 Momentum function and hydraulic jump

A hydraulic jump converts supercritical flow to subcritical flow with substantial energy dissipation while momentum is approximately conserved across the short jump.

\[\mathrm{Fr}_1>1\rightarrow\text{hydraulic jump}\rightarrow\mathrm{Fr}_2<1\]

![FIG-03-17-006: Hydraulic jump profile with y1, y2, roller, energy loss, and upstream/downstream Froude regimes.](../figures/FIG-03-17-006-momentum-function-and-hydraulic-jump.png)

### Worked Example 6

**Problem.** A supercritical approach flow can be forced through a jump in a stilling basin to dissipate energy.

**Solution.** A hydraulic jump occurs when supercritical flow transitions to subcritical flow, converting part of the kinetic energy into turbulence and heat. A stilling basin deliberately provides the geometry and tailwater condition needed to force and contain that jump so downstream erosion is reduced.

---

## 17.7 Channel controls, normal depth, and gradually varied flow

Normal depth follows from the uniform-flow relation. Controls such as gates, weirs, slope changes, and downstream water levels create nonuniform profiles.

\[S_f\approx S_0\quad\text{for uniform flow}\]

![FIG-03-17-007: Channel longitudinal profile showing bed slope, normal depth, control section, and backwater curve.](../figures/FIG-03-17-007-channel-controls-normal-depth-and-gradually-varied-flow.png)

### Worked Example 7

**Problem.** If tailwater rises above normal depth, a backwater profile may develop upstream.

**Solution.** When downstream tailwater exceeds the normal-depth condition, the downstream control raises the water surface upstream. The resulting gradually varied profile is a backwater curve; its exact classification depends on channel slope and the relative positions of normal and critical depth.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** First establish the flow regime with depth, velocity, and Froude number; then apply the appropriate energy, momentum, or Manning relation. Mixing a gradually varied-flow assumption with a rapid hydraulic-jump relation in the same step is a common error, so identify the control section and regime before calculating.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook form and coefficient for the chosen unit system. Open-channel formulas often contain empirical coefficients that differ between SI and U.S. customary units, so a remembered version should not override the supplied Handbook relation.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 10; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-017-07` — U.S. Army Corps of Engineers, Hydrologic Engineering Center. *HEC-RAS Hydraulic Reference Manual*, Version 6.6. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

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

15. Draw the channel cross-section and water surface before solving so flow area, top width, wetted perimeter, hydraulic radius, depth, and control location are defined consistently.

16. Use the Handbook open-channel relation when provided because Manning coefficients, hydraulic-radius definitions, and unit-system constants must match the supplied reference.

17. Open-channel calculations can mix feet, meters, cfs, and m³/s; explicit conversion is required before velocity, discharge, energy, or Froude-number calculations are combined.

18. Check the implied regime and geometry: depth and velocity must be positive, Froude classification should agree with the assumed flow state, and the computed water surface should be compatible with the channel control.

19. **A.** For **Open-channel geometry and hydraulic radius**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Manning equation and uniform flow**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Froude number and flow regime**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Specific energy and critical depth**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Weirs and open-channel flow measurement**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Momentum function and hydraulic jump**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Channel controls, normal depth, and gradually varied flow**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Open-Channel Flow — Manning Equation, Specific Energy, and Hydraulic Jumps, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Gradually varied-flow and control details not fully printed in Handbook 10.6 are treated as learned material and supported by the HEC-RAS hydraulic reference rather than by an invented page citation.



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

1. **Independent check for §17.1.** Rework the problem from the stated givens rather than copying the worked-example result. Hydraulic radius is \(R=A/P_w\). With \(A=20\ \text{ft}^2\) and wetted perimeter \(P_w=12\ \text{ft}\), \(R=20/12=1.667\ \text{ft}\). Do not substitute top width for wetted perimeter. **Check:** confirm the final magnitude and units against the physical meaning of §17.1 before accepting the answer.



2. **Independent check for §17.2.** Rework the problem from the stated givens rather than copying the worked-example result. Manning's equation relates \(Q\) to roughness \(n\), flow area \(A\), hydraulic radius \(R\), and energy slope \(S\). If depth is known, compute \(A\) and \(R\) and solve directly for \(Q\); if discharge is known and depth is unknown, depth appears inside both \(A\) and \(R\), so an iterative or numerical solution is normally required. **Check:** confirm the final magnitude and units against the physical meaning of §17.2 before accepting the answer.



3. **Independent check for §17.3.** Rework the problem from the stated givens rather than copying the worked-example result. The Froude number compares inertial and gravity-wave effects. \(Fr<1\) indicates subcritical flow, \(Fr=1\) critical flow, and \(Fr>1\) supercritical flow. The classification determines how disturbances propagate and is central to evaluating transitions and hydraulic jumps. **Check:** confirm the final magnitude and units against the physical meaning of §17.3 before accepting the answer.



4. **Independent check for §17.4.** Rework the problem from the stated givens rather than copying the worked-example result. Specific energy is \(E=y+V^2/(2g)\). With \(y=2\ \text{ft}\), \(V=6\ \text{ft/s}\), and \(g=32.2\ \text{ft/s}^2\), the velocity head is \(36/(64.4)=0.559\ \text{ft}\), so \(E\approx2.56\ \text{ft}\). **Check:** confirm the final magnitude and units against the physical meaning of §17.4 before accepting the answer.



5. **Independent check for §17.5.** Rework the problem from the stated givens rather than copying the worked-example result. For a rectangular-weir relation \(Q\propto H^{3/2}\). If the head doubles, \(Q_2/Q_1=(2H/H)^{3/2}=2^{3/2}\approx2.83\). Thus the discharge increases by about a factor of **2.83**, not merely by a factor of two. **Check:** confirm the final magnitude and units against the physical meaning of §17.5 before accepting the answer.



6. **Independent check for §17.6.** Rework the problem from the stated givens rather than copying the worked-example result. A hydraulic jump occurs when supercritical flow transitions to subcritical flow, converting part of the kinetic energy into turbulence and heat. A stilling basin deliberately provides the geometry and tailwater condition needed to force and contain that jump so downstream erosion is reduced. **Check:** confirm the final magnitude and units against the physical meaning of §17.6 before accepting the answer.



7. **Independent check for §17.7.** Rework the problem from the stated givens rather than copying the worked-example result. When downstream tailwater exceeds the normal-depth condition, the downstream control raises the water surface upstream. The resulting gradually varied profile is a backwater curve; its exact classification depends on channel slope and the relative positions of normal and critical depth. **Check:** confirm the final magnitude and units against the physical meaning of §17.7 before accepting the answer.



8. Before accepting a open-channel flow — manning equation, specific energy, and hydraulic jumps result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Use **FE Civil specification Area 10** first, followed by the Handbook open-channel-flow relations in the ledger; use HEC-RAS only for the reconciled learned/application portion.

10. For open-channel flow — manning equation, specific energy, and hydraulic jumps, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

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
