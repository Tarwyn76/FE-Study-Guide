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

**Solution.** Convert quadrant bearing S30°E to azimuth measured clockwise from north. In the southeast quadrant the azimuth is \(180^\circ-30^\circ=150^\circ\). Therefore **S30°E = 150° azimuth**.

---

## 15.2 Traverse coordinates, latitudes, departures, and closure

A traverse converts line length and direction into north-south and east-west components. The sums of components provide a closure check.

\[\Delta N=L\cos\theta,\qquad \Delta E=L\sin\theta\]

![FIG-03-15-002: Closed traverse with line lengths, azimuths, latitudes, departures, and misclosure vector.](../figures/FIG-03-15-002-traverse-coordinates-latitudes-departures-and-closure.png)

### Worked Example 2

**Problem.** For L=100 ft at azimuth 30°, ΔN=86.6 ft and ΔE=50.0 ft.

**Solution.** Resolve the 100-ft line into northing and easting components using \(\Delta N=L\cos\theta\) and \(\Delta E=L\sin\theta\). With \(\theta=30^\circ\), \(\Delta N=100\cos30^\circ=86.6\ \text{ft}\) and \(\Delta E=100\sin30^\circ=50.0\ \text{ft}\). Both components are positive because the line lies in the northeast quadrant.

---

## 15.3 Coordinate systems and horizontal positioning

FE questions may use local coordinates, state-plane style coordinates, or latitude/longitude conceptually. Treat coordinate differences consistently and do not mix angular and planar units.

\[d=\sqrt{(\Delta E)^2+(\Delta N)^2}\]

![FIG-03-15-003: Local northing-easting grid with two control points and coordinate differences.](../figures/FIG-03-15-003-coordinate-systems-and-horizontal-positioning.png)

### Worked Example 3

**Problem.** Points differing by 300 ft east and 400 ft north are 500 ft apart.

**Solution.** Use the coordinate-distance relation \(d=\sqrt{(\Delta E)^2+(\Delta N)^2}\). With \(\Delta E=300\ \text{ft}\) and \(\Delta N=400\ \text{ft}\), \(d=\sqrt{300^2+400^2}=500\ \text{ft}\). This is the familiar 3-4-5 right-triangle proportion.

---

## 15.4 Differential leveling and elevation determination

Differential leveling propagates elevations from a benchmark. A backsight establishes height of instrument; a foresight transfers elevation.

\[\mathrm{HI}=E_{\text{known}}+\mathrm{BS},\qquad E_{\text{next}}=\mathrm{HI}-\mathrm{FS}\]

![FIG-03-15-004: Level setup between benchmark and turning point with backsight, foresight, HI, and elevations.](../figures/FIG-03-15-004-differential-leveling-and-elevation-determination.png)

### Worked Example 4

**Problem.** Benchmark 100.00 ft, BS 4.20 ft, FS 6.35 ft gives next elevation 97.85 ft.

**Solution.** For differential leveling, first compute height of instrument: \(HI=100.00+4.20=104.20\ \text{ft}\). Then subtract the foresight: \(E_{next}=104.20-6.35=97.85\ \text{ft}\). The next point elevation is therefore **97.85 ft**.

---

## 15.5 Grades, profiles, and vertical control

Grade is rise or fall divided by horizontal distance. Keep sign convention explicit, especially when working from stationing.

\[\%G=100\frac{\Delta z}{L}\]

![FIG-03-15-005: Road or pipeline profile with stationing, elevations, tangent grade, and percent-grade annotation.](../figures/FIG-03-15-005-grades-profiles-and-vertical-control.png)

### Worked Example 5

**Problem.** A 3.0 ft rise over 150 ft is a +2.0% grade.

**Solution.** Grade is rise divided by horizontal run times 100 percent. Thus \(g=(3.0/150)\times100=+2.0\%\). The positive sign indicates that elevation increases in the direction of stationing.

---

## 15.6 Area computations from coordinates and offsets

Areas may be found from geometry, coordinates, or numerical approximations. Confirm the polygon closes and maintain consistent coordinate order.

\[A=\frac12\left|\sum x_i y_{i+1}-y_i x_{i+1}\right|\]

![FIG-03-15-006: Irregular parcel with coordinate vertices and shoelace-area orientation.](../figures/FIG-03-15-006-area-computations-from-coordinates-and-offsets.png)

### Worked Example 6

**Problem.** A rectangle with coordinates (0,0), (40,0), (40,25), (0,25) has area 1000 ft².

**Solution.** The coordinates define a rectangle 40 ft by 25 ft. Its area is \(A=40\times25=1000\ \text{ft}^2\); applying the coordinate/shoelace method gives the same result. The polygon should be traversed in a consistent clockwise or counterclockwise order.

---

## 15.7 Earthwork volumes, average end area, prismoidal formula, and mass haul

Earthwork calculations convert cross-sectional areas into volumes. A mass-haul diagram tracks cumulative cut and fill and helps identify balance points.

\[V_{\text{AEA}}=L\frac{A_1+A_2}{2},\qquad V_p=\frac{L}{6}(A_1+4A_m+A_2)\]

![FIG-03-15-007: Cross-sections, average-end-area volume prism, and corresponding mass-haul curve with balance point.](../figures/FIG-03-15-007-earthwork-volumes-average-end-area-prismoidal-formula-and-mass-haul.png)

### Worked Example 7

**Problem.** A1=200 ft², A2=260 ft², L=100 ft gives 23,000 ft³ by average end area.

**Solution.** Use the average-end-area formula \(V=L(A_1+A_2)/2\). Substituting \(L=100\ \text{ft}\), \(A_1=200\ \text{ft}^2\), and \(A_2=260\ \text{ft}^2\) gives \(V=100(200+260)/2=23{,}000\ \text{ft}^3\).

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** Establish the horizontal control before computing the derived quantity. For example, determine coordinate differences or elevations first, then use those results in the area, grade, or earthwork calculation. A quick sketch showing station direction, north/east axes, and cut/fill sign convention prevents the two calculations from using inconsistent reference systems.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the FE Handbook relation and its stated angle, coordinate, and sign conventions. Surveying errors often come from a correct formula paired with the wrong quadrant, azimuth reference, or elevation sign, so the Handbook convention should control the exam calculation.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 9; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-015-03` — Ghilani, C. D. (2022). *Elementary Surveying: An Introduction to Geomatics* (16th ed.). Pearson. ISBN 978-0-13-682282-0. Cited at publication/standard level; no page-level claim.
- `CIV-3-015-06` — Ghilani, C. D. (2022). *Elementary Surveying: An Introduction to Geomatics* (16th ed.). Pearson. ISBN 978-0-13-682282-0. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

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

15. A plan/profile sketch fixes north/east directions, stationing, backsight/foresight roles, and cut-fill geometry before coordinate, leveling, grade, or volume equations are chosen.

16. Use the Handbook surveying relation when available so the azimuth, bearing, coordinate, elevation, and sign conventions match the reference supplied on the FE exam.

17. Surveying work often mixes feet and meters or degrees and angular subdivisions; convert explicitly before combining distances, elevations, and angles in one computation.

18. Use closure and geometry as checks: a traverse should nearly close, an elevation sequence should follow the BS/FS arithmetic, and an area or volume should have a magnitude consistent with the plotted dimensions.

19. **A.** For **Angles, bearings, azimuths, and distance reduction**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Traverse coordinates, latitudes, departures, and closure**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Coordinate systems and horizontal positioning**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Differential leveling and elevation determination**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Grades, profiles, and vertical control**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Area computations from coordinates and offsets**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Earthwork volumes, average end area, prismoidal formula, and mass haul**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Surveying, Leveling, Coordinates, Grades, Earthwork, and Volumes, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Surveying methods that extend beyond the Handbook's tabulated relations remain specification-required learned material and are supported by the chapter's surveying reference rather than assigned a false Handbook page.



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

1. **Independent check for §15.1.** Rework the problem from the stated givens rather than copying the worked-example result. Convert quadrant bearing S30°E to azimuth measured clockwise from north. In the southeast quadrant the azimuth is \(180^\circ-30^\circ=150^\circ\). Therefore **S30°E = 150° azimuth**. **Check:** confirm the final magnitude and units against the physical meaning of §15.1 before accepting the answer.



2. **Independent check for §15.2.** Rework the problem from the stated givens rather than copying the worked-example result. Resolve the 100-ft line into northing and easting components using \(\Delta N=L\cos\theta\) and \(\Delta E=L\sin\theta\). With \(\theta=30^\circ\), \(\Delta N=100\cos30^\circ=86.6\ \text{ft}\) and \(\Delta E=100\sin30^\circ=50.0\ \text{ft}\). Both components are positive because the line lies in the northeast quadrant. **Check:** confirm the final magnitude and units against the physical meaning of §15.2 before accepting the answer.



3. **Independent check for §15.3.** Rework the problem from the stated givens rather than copying the worked-example result. Use the coordinate-distance relation \(d=\sqrt{(\Delta E)^2+(\Delta N)^2}\). With \(\Delta E=300\ \text{ft}\) and \(\Delta N=400\ \text{ft}\), \(d=\sqrt{300^2+400^2}=500\ \text{ft}\). This is the familiar 3-4-5 right-triangle proportion. **Check:** confirm the final magnitude and units against the physical meaning of §15.3 before accepting the answer.



4. **Independent check for §15.4.** Rework the problem from the stated givens rather than copying the worked-example result. For differential leveling, first compute height of instrument: \(HI=100.00+4.20=104.20\ \text{ft}\). Then subtract the foresight: \(E_{next}=104.20-6.35=97.85\ \text{ft}\). The next point elevation is therefore **97.85 ft**. **Check:** confirm the final magnitude and units against the physical meaning of §15.4 before accepting the answer.



5. **Independent check for §15.5.** Rework the problem from the stated givens rather than copying the worked-example result. Grade is rise divided by horizontal run times 100 percent. Thus \(g=(3.0/150)\times100=+2.0\%\). The positive sign indicates that elevation increases in the direction of stationing. **Check:** confirm the final magnitude and units against the physical meaning of §15.5 before accepting the answer.



6. **Independent check for §15.6.** Rework the problem from the stated givens rather than copying the worked-example result. The coordinates define a rectangle 40 ft by 25 ft. Its area is \(A=40\times25=1000\ \text{ft}^2\); applying the coordinate/shoelace method gives the same result. The polygon should be traversed in a consistent clockwise or counterclockwise order. **Check:** confirm the final magnitude and units against the physical meaning of §15.6 before accepting the answer.



7. **Independent check for §15.7.** Rework the problem from the stated givens rather than copying the worked-example result. Use the average-end-area formula \(V=L(A_1+A_2)/2\). Substituting \(L=100\ \text{ft}\), \(A_1=200\ \text{ft}^2\), and \(A_2=260\ \text{ft}^2\) gives \(V=100(200+260)/2=23{,}000\ \text{ft}^3\). **Check:** confirm the final magnitude and units against the physical meaning of §15.7 before accepting the answer.



8. Before accepting a surveying, leveling, coordinates, grades, earthwork, and volumes result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Begin with **FE Civil specification Area 9**, then use the surveying/coordinate or leveling material identified in the chapter ledger. Use the external surveying reference only for the learned portion not printed in Handbook 10.6.

10. For surveying, leveling, coordinates, grades, earthwork, and volumes, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

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
