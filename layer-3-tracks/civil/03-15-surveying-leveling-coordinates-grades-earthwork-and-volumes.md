---
chapter: "03-15"
title: "Surveying, Leveling, Coordinates, Grades, Earthwork, and Volumes"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-015-01, CIV-3-015-02, CIV-3-015-03, CIV-3-015-04, CIV-3-015-05, CIV-3-015-06, CIV-3-015-07]
routes: [civil]
status: drafted
---

# Chapter 03-15: Surveying, Leveling, Coordinates, Grades, Earthwork, and Volumes

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** MATH-1A-004-01

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Surveying, Leveling, Coordinates, Grades, Earthwork, and Volumes**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **15.1** Explain and apply **Angles, bearings, azimuths, and distance reduction**.
* **15.2** Explain and apply **Traverse coordinates, latitudes, departures, and closure**.
* **15.3** Explain and apply **Coordinate systems and horizontal positioning**.
* **15.4** Explain and apply **Differential leveling and elevation determination**.
* **15.5** Explain and apply **Grades, profiles, and vertical control**.
* **15.6** Explain and apply **Area computations from coordinates and offsets**.
* **15.7** Explain and apply **Earthwork volumes, average end area, prismoidal formula, and mass haul**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 15.1 Angles, bearings, azimuths, and distance reduction

Survey directions must be carried in one convention at a time. Bearings are quadrant-based; azimuths are measured clockwise from north. Convert before combining.

\[\text{azimuth}=0^\circ\text{ to }360^\circ\]

![FIG-03-15-001: Plan-view compass showing bearings and azimuths for the same line.](../figures/FIG-03-15-001-angles-bearings-azimuths-and-distance-reduction.png)

### Worked Example 1

**Problem.** Bearing S30°E corresponds to azimuth 150°.

**Solution.** Apply the relation and definitions in §15.1; the stated result follows with consistent units and sign convention.

---

## 15.2 Traverse coordinates, latitudes, departures, and closure

A traverse converts line length and direction into north-south and east-west components. The sums of components provide a closure check.

\[\Delta N=L\cos\theta,\qquad \Delta E=L\sin\theta\]

![FIG-03-15-002: Closed traverse with line lengths, azimuths, latitudes, departures, and misclosure vector.](../figures/FIG-03-15-002-traverse-coordinates-latitudes-departures-and-closure.png)

### Worked Example 2

**Problem.** For L=100 ft at azimuth 30°, ΔN=86.6 ft and ΔE=50.0 ft.

**Solution.** Apply the relation and definitions in §15.2; the stated result follows with consistent units and sign convention.

---

## 15.3 Coordinate systems and horizontal positioning

FE questions may use local coordinates, state-plane style coordinates, or latitude/longitude conceptually. Treat coordinate differences consistently and do not mix angular and planar units.

\[d=\sqrt{(\Delta E)^2+(\Delta N)^2}\]

![FIG-03-15-003: Local northing-easting grid with two control points and coordinate differences.](../figures/FIG-03-15-003-coordinate-systems-and-horizontal-positioning.png)

### Worked Example 3

**Problem.** Points differing by 300 ft east and 400 ft north are 500 ft apart.

**Solution.** Apply the relation and definitions in §15.3; the stated result follows with consistent units and sign convention.

---

## 15.4 Differential leveling and elevation determination

Differential leveling propagates elevations from a benchmark. A backsight establishes height of instrument; a foresight transfers elevation.

\[\mathrm{HI}=E_{\text{known}}+\mathrm{BS},\qquad E_{\text{next}}=\mathrm{HI}-\mathrm{FS}\]

![FIG-03-15-004: Level setup between benchmark and turning point with backsight, foresight, HI, and elevations.](../figures/FIG-03-15-004-differential-leveling-and-elevation-determination.png)

### Worked Example 4

**Problem.** Benchmark 100.00 ft, BS 4.20 ft, FS 6.35 ft gives next elevation 97.85 ft.

**Solution.** Apply the relation and definitions in §15.4; the stated result follows with consistent units and sign convention.

---

## 15.5 Grades, profiles, and vertical control

Grade is rise or fall divided by horizontal distance. Keep sign convention explicit, especially when working from stationing.

\[\%G=100\frac{\Delta z}{L}\]

![FIG-03-15-005: Road or pipeline profile with stationing, elevations, tangent grade, and percent-grade annotation.](../figures/FIG-03-15-005-grades-profiles-and-vertical-control.png)

### Worked Example 5

**Problem.** A 3.0 ft rise over 150 ft is a +2.0% grade.

**Solution.** Apply the relation and definitions in §15.5; the stated result follows with consistent units and sign convention.

---

## 15.6 Area computations from coordinates and offsets

Areas may be found from geometry, coordinates, or numerical approximations. Confirm the polygon closes and maintain consistent coordinate order.

\[A=\frac12\left|\sum x_i y_{i+1}-y_i x_{i+1}\right|\]

![FIG-03-15-006: Irregular parcel with coordinate vertices and shoelace-area orientation.](../figures/FIG-03-15-006-area-computations-from-coordinates-and-offsets.png)

### Worked Example 6

**Problem.** A rectangle with coordinates (0,0), (40,0), (40,25), (0,25) has area 1000 ft².

**Solution.** Apply the relation and definitions in §15.6; the stated result follows with consistent units and sign convention.

---

## 15.7 Earthwork volumes, average end area, prismoidal formula, and mass haul

Earthwork calculations convert cross-sectional areas into volumes. A mass-haul diagram tracks cumulative cut and fill and helps identify balance points.

\[V_{\text{AEA}}=L\frac{A_1+A_2}{2},\qquad V_p=\frac{L}{6}(A_1+4A_m+A_2)\]

![FIG-03-15-007: Cross-sections, average-end-area volume prism, and corresponding mass-haul curve with balance point.](../figures/FIG-03-15-007-earthwork-volumes-average-end-area-prismoidal-formula-and-mass-haul.png)

### Worked Example 7

**Problem.** A1=200 ft², A2=260 ft², L=100 ft gives 23,000 ft³ by average end area.

**Solution.** Apply the relation and definitions in §15.7; the stated result follows with consistent units and sign convention.

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

Primary source basis: **FE Civil specification Area 9; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** Some Civil specification topics are directly tabulated in the Handbook; others are named by the specification but require learned engineering knowledge. This chapter does not imply that every workflow, code provision, or design factor is printed in the Handbook.

Where the FE specification requires a topic that is not directly developed in the Handbook, the ledger marks it **specification-required / guide-developed** rather than inventing a Handbook citation.

---

## Where This Goes Wrong

**Using survey direction system without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using traverse closure without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using survey coordinate system without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using differential leveling without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using percent grade without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using surveyed area without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using earthwork volume without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| survey direction system | Concept developed in §15.1; apply with that section's stated assumptions and units. |
| traverse closure | Concept developed in §15.2; apply with that section's stated assumptions and units. |
| survey coordinate system | Concept developed in §15.3; apply with that section's stated assumptions and units. |
| differential leveling | Concept developed in §15.4; apply with that section's stated assumptions and units. |
| percent grade | Concept developed in §15.5; apply with that section's stated assumptions and units. |
| surveyed area | Concept developed in §15.6; apply with that section's stated assumptions and units. |
| earthwork volume | Concept developed in §15.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **survey direction system** and identify the principal quantity, relation, or decision it organizes.

2. Define **traverse closure** and identify the principal quantity, relation, or decision it organizes.

3. Define **survey coordinate system** and identify the principal quantity, relation, or decision it organizes.

4. Define **differential leveling** and identify the principal quantity, relation, or decision it organizes.

5. Define **percent grade** and identify the principal quantity, relation, or decision it organizes.

6. Define **surveyed area** and identify the principal quantity, relation, or decision it organizes.

7. Define **earthwork volume** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **survey direction system**?

9. What assumption or unit error is most likely to cause a wrong result when applying **traverse closure**?

10. What assumption or unit error is most likely to cause a wrong result when applying **survey coordinate system**?

11. What assumption or unit error is most likely to cause a wrong result when applying **differential leveling**?

12. What assumption or unit error is most likely to cause a wrong result when applying **percent grade**?

13. What assumption or unit error is most likely to cause a wrong result when applying **surveyed area**?

14. What assumption or unit error is most likely to cause a wrong result when applying **earthwork volume**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **survey direction system**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **traverse closure**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **survey coordinate system**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **differential leveling**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **percent grade**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **surveyed area**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **earthwork volume**?
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

1. **survey direction system** is developed in §15.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **traverse closure** is developed in §15.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **survey coordinate system** is developed in §15.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **differential leveling** is developed in §15.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **percent grade** is developed in §15.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **surveyed area** is developed in §15.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **earthwork volume** is developed in §15.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **survey direction system**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **traverse closure**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **survey coordinate system**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **differential leveling**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **percent grade**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **surveyed area**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **earthwork volume**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

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

1. Bearing S30°E corresponds to azimuth 150°.

2. For L=100 ft at azimuth 30°, ΔN=86.6 ft and ΔE=50.0 ft.

3. Points differing by 300 ft east and 400 ft north are 500 ft apart.

4. Benchmark 100.00 ft, BS 4.20 ft, FS 6.35 ft gives next elevation 97.85 ft.

5. A 3.0 ft rise over 150 ft is a +2.0% grade.

6. A rectangle with coordinates (0,0), (40,0), (40,25), (0,25) has area 1000 ft².

7. A1=200 ft², A2=260 ft², L=100 ft gives 23,000 ft³ by average end area.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §15.1. Bearing S30°E corresponds to azimuth 150°. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §15.2. For L=100 ft at azimuth 30°, ΔN=86.6 ft and ΔE=50.0 ft. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §15.3. Points differing by 300 ft east and 400 ft north are 500 ft apart. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §15.4. Benchmark 100.00 ft, BS 4.20 ft, FS 6.35 ft gives next elevation 97.85 ft. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §15.5. A 3.0 ft rise over 150 ft is a +2.0% grade. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §15.6. A rectangle with coordinates (0,0), (40,0), (40,25), (0,25) has area 1000 ft². The calculation or classification follows from the displayed section relation and the stated data.

7. Use §15.7. A1=200 ft², A2=260 ft², L=100 ft gives 23,000 ft³ by average end area. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 9 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 9.

- **survey direction system:** Angles, bearings, azimuths, and distance reduction
- **traverse closure:** Traverse coordinates, latitudes, departures, and closure
- **survey coordinate system:** Coordinate systems and horizontal positioning
- **differential leveling:** Differential leveling and elevation determination
- **percent grade:** Grades, profiles, and vertical control
- **surveyed area:** Area computations from coordinates and offsets
- **earthwork volume:** Earthwork volumes, average end area, prismoidal formula, and mass haul

---

## What's Next

**Chapter 03-16: Hydrology — Rainfall, Infiltration, Runoff, Watersheds, and Hydrographs**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
