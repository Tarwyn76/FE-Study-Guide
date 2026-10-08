---
chapter: "03-25"
title: "Steel Design — Tension Members, Beams, Columns, and Connections"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-025-01, CIV-3-025-02, CIV-3-025-03, CIV-3-025-04, CIV-3-025-05, CIV-3-025-06, CIV-3-025-07]
routes: [civil]
status: drafted
---

# Chapter 03-25: Steel Design — Tension Members, Beams, Columns, and Connections

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-024-07

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Steel Design — Tension Members, Beams, Columns, and Connections**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **25.1** Explain and apply **Steel design philosophies and limit states**.
* **25.2** Explain and apply **Tension-member yielding and fracture**.
* **25.3** Explain and apply **Bolted and welded connection concepts**.
* **25.4** Explain and apply **Steel beam flexure and lateral-torsional buckling**.
* **25.5** Explain and apply **Beam shear and serviceability**.
* **25.6** Explain and apply **Steel column compression strength**.
* **25.7** Explain and apply **Section selection and handbook-table use**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 25.1 Steel design philosophies and limit states

Steel design compares factored demand with design resistance. Identify the controlling limit state rather than assuming yielding always governs.

\[\phi R_n\ge U\]

![FIG-03-25-001: Steel design flow from demand to candidate limit states and controlling design strength.](../figures/FIG-03-25-001-steel-design-philosophies-and-limit-states.png)

### Worked Example 1

**Problem.** If φRn=180 kip and demand is 165 kip, the checked limit state passes.

**Solution.** The strength check is \(\phi R_n\ge U\). Here the available design strength is \(180\ \text{kip}\) and the factored demand is \(165\ \text{kip}\), so \(180\ge165\) and the checked limit state passes with a 15-kip margin.

---

## 25.2 Tension-member yielding and fracture

Gross-section yielding and effective-net-section fracture are distinct tension limit states. Holes and shear lag can reduce effective area.

\[\phi T_n=\min(\phi F_yA_g,\ \phi F_uA_e)\]

![FIG-03-25-002: Plate tension member with bolt holes showing gross section, net section, and effective net area concept.](../figures/FIG-03-25-002-tension-member-yielding-and-fracture.png)

### Worked Example 2

**Problem.** A bolted connection may have a smaller net area than gross area, causing fracture to control.

**Solution.** A tension member must be checked for both gross-section yielding and net/effective-section fracture. Bolt holes reduce the net area, so the fracture strength based on \(F_uA_e\) can be less than the yielding strength based on \(F_yA_g\) even when the gross section is adequate.

---

## 25.3 Bolted and welded connection concepts

Connections can be governed by fastener shear, bearing, block shear, weld strength, or connected-member rupture/yielding.

\[\text{connection strength}=\min(\text{bolt/weld/member limit states})\]

![FIG-03-25-003: Bolted lap connection and fillet-welded connection with primary limit-state callouts.](../figures/FIG-03-25-003-bolted-and-welded-connection-concepts.png)

### Worked Example 3

**Problem.** A stronger bolt does not prevent net-section fracture of the plate.

**Solution.** Connection design is governed by the weakest applicable limit state. Increasing bolt strength may raise bolt shear or bearing capacity, but it does not increase the plate net area; therefore net-section fracture of the connected member can still control.

---

## 25.4 Steel beam flexure and lateral-torsional buckling

Beam flexural strength depends on section compactness, unbraced length, yielding, and lateral-torsional buckling.

\[\phi M_n\ge M_u\]

![FIG-03-25-004: W-shape beam with unbraced length and exaggerated lateral-torsional buckling deformation.](../figures/FIG-03-25-004-steel-beam-flexure-and-lateral-torsional-buckling.png)

### Worked Example 4

**Problem.** Increasing unbraced length can reduce available moment strength.

**Solution.** Lateral-torsional buckling resistance generally decreases as the unbraced length of the compression flange increases. Thus a beam that is adequate when continuously braced can have a lower available moment strength when the lateral bracing spacing is increased.

---

## 25.5 Beam shear and serviceability

Shear strength and deflection are separate checks. A beam can satisfy strength but fail a serviceability requirement.

\[\phi V_n\ge V_u\]

![FIG-03-25-005: Beam cross-section and span with separate flexure, shear, and deflection check callouts.](../figures/FIG-03-25-005-beam-shear-and-serviceability.png)

### Worked Example 5

**Problem.** A shallow long-span beam may be deflection-controlled even when flexural strength is adequate.

**Solution.** Strength and serviceability are separate checks. A beam may satisfy \(\phi M_n\ge M_u\) and \(\phi V_n\ge V_u\) yet still deflect excessively under service loads, especially when the member is shallow or the span is long.

---

## 25.6 Steel column compression strength

Column design uses critical stress based on slenderness and material properties. The weakest buckling axis can control.

\[\phi P_n=\phi F_{cr}A_g\]

![FIG-03-25-006: W-shape column with x/y buckling axes and critical-stress versus slenderness chart.](../figures/FIG-03-25-006-steel-column-compression-strength.png)

### Worked Example 6

**Problem.** Compare KL/r about both principal axes before selecting the governing Fcr.

**Solution.** Column slenderness must be checked about both principal axes because \(KL/r\) depends on effective length and radius of gyration. Compute the slenderness for each axis and use the axis producing the smaller compression strength or larger controlling slenderness.

---

## 25.7 Section selection and handbook-table use

FE problems may rely on handbook tabulations for W-shape dimensions, properties, and available strength. Read the exact table heading and units.

\[\text{select section so all required checks pass}\]

![FIG-03-25-007: Annotated W-shape table excerpt concept showing A, Ix, Sx, rx, ry, and available strength columns.](../figures/FIG-03-25-007-section-selection-and-handbook-table-use.png)

### Worked Example 7

**Problem.** A section with adequate moment strength may still require a larger Ix for deflection.

**Solution.** Section selection is iterative. A shape that passes flexure may fail shear, lateral-torsional buckling, column strength, connection geometry, or deflection. If deflection controls, a section with larger \(I_x\) may be required even when nominal moment strength is already sufficient.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a steel member problem, identify all relevant limit states before calculating. Compute factored demand, evaluate gross/net section or flexural/compression strength as applicable, and then perform the serviceability check. The smallest available strength or most restrictive service criterion governs.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook steel-design equations and tabulated properties that match the member and limit state being checked. Remembered code expressions can differ by edition, resistance factor, or effective-area definition, so the supplied Handbook form should control the exam solution.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 11; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-025-05` — American Institute of Steel Construction. (2022). *Specification for Structural Steel Buildings* (ANSI/AISC 360-22). AISC. See also *Steel Construction Manual*, 16th ed. (2023). Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

## Where This Goes Wrong

**Using steel limit state without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using steel tension member without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using steel connection without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using steel beam flexure without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using steel beam shear without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using steel column design without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using steel section selection without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| steel limit state | Concept developed in §25.1; apply with that section's stated assumptions and units. |
| steel tension member | Concept developed in §25.2; apply with that section's stated assumptions and units. |
| steel connection | Concept developed in §25.3; apply with that section's stated assumptions and units. |
| steel beam flexure | Concept developed in §25.4; apply with that section's stated assumptions and units. |
| steel beam shear | Concept developed in §25.5; apply with that section's stated assumptions and units. |
| steel column design | Concept developed in §25.6; apply with that section's stated assumptions and units. |
| steel section selection | Concept developed in §25.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **steel limit state** and identify the principal quantity, relation, or decision it organizes.

2. Define **steel tension member** and identify the principal quantity, relation, or decision it organizes.

3. Define **steel connection** and identify the principal quantity, relation, or decision it organizes.

4. Define **steel beam flexure** and identify the principal quantity, relation, or decision it organizes.

5. Define **steel beam shear** and identify the principal quantity, relation, or decision it organizes.

6. Define **steel column design** and identify the principal quantity, relation, or decision it organizes.

7. Define **steel section selection** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **steel limit state**?

9. What assumption or unit error is most likely to cause a wrong result when applying **steel tension member**?

10. What assumption or unit error is most likely to cause a wrong result when applying **steel connection**?

11. What assumption or unit error is most likely to cause a wrong result when applying **steel beam flexure**?

12. What assumption or unit error is most likely to cause a wrong result when applying **steel beam shear**?

13. What assumption or unit error is most likely to cause a wrong result when applying **steel column design**?

14. What assumption or unit error is most likely to cause a wrong result when applying **steel section selection**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **steel limit state**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **steel tension member**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **steel connection**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **steel beam flexure**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **steel beam shear**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **steel column design**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **steel section selection**?
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

1. **steel limit state** is developed in §25.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **steel tension member** is developed in §25.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **steel connection** is developed in §25.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **steel beam flexure** is developed in §25.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **steel beam shear** is developed in §25.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **steel column design** is developed in §25.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **steel section selection** is developed in §25.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **steel limit state**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **steel tension member**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **steel connection**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **steel beam flexure**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **steel beam shear**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **steel column design**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **steel section selection**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. Draw the steel member and connection with load path, unbraced length, gross/net sections, and connection geometry before selecting the controlling limit-state equations.

16. Use the Handbook steel relation for the requested limit state, while code-specific learned details are checked against the cited AISC specification rather than a remembered equation from another edition.

17. Keep ksi, psi, kip, lbf, inches, and section-property units consistent before combining stress, area, shear, moment, and column-strength terms.

18. Check the governing limit state and margin: available strength must exceed factored demand, and a member that passes strength still requires any stated serviceability or stability check.

19. **A.** For **Steel design philosophies and limit states**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Tension-member yielding and fracture**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Bolted and welded connection concepts**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Steel beam flexure and lateral-torsional buckling**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Beam shear and serviceability**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Steel column compression strength**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Section selection and handbook-table use**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Steel Design — Tension Members, Beams, Columns, and Connections, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Steel-design details beyond the FE Handbook are explicitly supported by ANSI/AISC 360-22 and the Steel Construction Manual, not by a fabricated Handbook citation.



---

## Practice Problems

1. If φRn=180 kip and demand is 165 kip, the checked limit state passes.

2. A bolted connection may have a smaller net area than gross area, causing fracture to control.

3. A stronger bolt does not prevent net-section fracture of the plate.

4. Increasing unbraced length can reduce available moment strength.

5. A shallow long-span beam may be deflection-controlled even when flexural strength is adequate.

6. Compare KL/r about both principal axes before selecting the governing Fcr.

7. A section with adequate moment strength may still require a larger Ix for deflection.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. **Independent check for §25.1.** Rework the problem from the stated givens rather than copying the worked-example result. The strength check is \(\phi R_n\ge U\). Here the available design strength is \(180\ \text{kip}\) and the factored demand is \(165\ \text{kip}\), so \(180\ge165\) and the checked limit state passes with a 15-kip margin. **Check:** confirm the final magnitude and units against the physical meaning of §25.1 before accepting the answer.



2. **Independent check for §25.2.** Rework the problem from the stated givens rather than copying the worked-example result. A tension member must be checked for both gross-section yielding and net/effective-section fracture. Bolt holes reduce the net area, so the fracture strength based on \(F_uA_e\) can be less than the yielding strength based on \(F_yA_g\) even when the gross section is adequate. **Check:** confirm the final magnitude and units against the physical meaning of §25.2 before accepting the answer.



3. **Independent check for §25.3.** Rework the problem from the stated givens rather than copying the worked-example result. Connection design is governed by the weakest applicable limit state. Increasing bolt strength may raise bolt shear or bearing capacity, but it does not increase the plate net area; therefore net-section fracture of the connected member can still control. **Check:** confirm the final magnitude and units against the physical meaning of §25.3 before accepting the answer.



4. **Independent check for §25.4.** Rework the problem from the stated givens rather than copying the worked-example result. Lateral-torsional buckling resistance generally decreases as the unbraced length of the compression flange increases. Thus a beam that is adequate when continuously braced can have a lower available moment strength when the lateral bracing spacing is increased. **Check:** confirm the final magnitude and units against the physical meaning of §25.4 before accepting the answer.



5. **Independent check for §25.5.** Rework the problem from the stated givens rather than copying the worked-example result. Strength and serviceability are separate checks. A beam may satisfy \(\phi M_n\ge M_u\) and \(\phi V_n\ge V_u\) yet still deflect excessively under service loads, especially when the member is shallow or the span is long. **Check:** confirm the final magnitude and units against the physical meaning of §25.5 before accepting the answer.



6. **Independent check for §25.6.** Rework the problem from the stated givens rather than copying the worked-example result. Column slenderness must be checked about both principal axes because \(KL/r\) depends on effective length and radius of gyration. Compute the slenderness for each axis and use the axis producing the smaller compression strength or larger controlling slenderness. **Check:** confirm the final magnitude and units against the physical meaning of §25.6 before accepting the answer.



7. **Independent check for §25.7.** Rework the problem from the stated givens rather than copying the worked-example result. Section selection is iterative. A shape that passes flexure may fail shear, lateral-torsional buckling, column strength, connection geometry, or deflection. If deflection controls, a section with larger \(I_x\) may be required even when nominal moment strength is already sufficient. **Check:** confirm the final magnitude and units against the physical meaning of §25.7 before accepting the answer.



8. Before accepting a steel design — tension members, beams, columns, and connections result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Start with **FE Civil specification Area 11** and the Handbook steel/member relations recorded in the ledger; use AISC only for the reconciled code-level learned material.

10. For steel design — tension members, beams, columns, and connections, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 11.

- **steel limit state:** Steel design philosophies and limit states
- **steel tension member:** Tension-member yielding and fracture
- **steel connection:** Bolted and welded connection concepts
- **steel beam flexure:** Steel beam flexure and lateral-torsional buckling
- **steel beam shear:** Beam shear and serviceability
- **steel column design:** Steel column compression strength
- **steel section selection:** Section selection and handbook-table use

---

## What's Next

**Chapter 03-26: Reinforced Concrete Design — Beams and Columns**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
