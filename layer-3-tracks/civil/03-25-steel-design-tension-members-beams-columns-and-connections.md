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

**Solution.** Apply the relation and definitions in §25.1; the stated result follows with consistent units and sign convention.

---

## 25.2 Tension-member yielding and fracture

Gross-section yielding and effective-net-section fracture are distinct tension limit states. Holes and shear lag can reduce effective area.

\[\phi T_n=\min(\phi F_yA_g,\ \phi F_uA_e)\]

![FIG-03-25-002: Plate tension member with bolt holes showing gross section, net section, and effective net area concept.](../figures/FIG-03-25-002-tension-member-yielding-and-fracture.png)

### Worked Example 2

**Problem.** A bolted connection may have a smaller net area than gross area, causing fracture to control.

**Solution.** Apply the relation and definitions in §25.2; the stated result follows with consistent units and sign convention.

---

## 25.3 Bolted and welded connection concepts

Connections can be governed by fastener shear, bearing, block shear, weld strength, or connected-member rupture/yielding.

\[\text{connection strength}=\min(\text{bolt/weld/member limit states})\]

![FIG-03-25-003: Bolted lap connection and fillet-welded connection with primary limit-state callouts.](../figures/FIG-03-25-003-bolted-and-welded-connection-concepts.png)

### Worked Example 3

**Problem.** A stronger bolt does not prevent net-section fracture of the plate.

**Solution.** Apply the relation and definitions in §25.3; the stated result follows with consistent units and sign convention.

---

## 25.4 Steel beam flexure and lateral-torsional buckling

Beam flexural strength depends on section compactness, unbraced length, yielding, and lateral-torsional buckling.

\[\phi M_n\ge M_u\]

![FIG-03-25-004: W-shape beam with unbraced length and exaggerated lateral-torsional buckling deformation.](../figures/FIG-03-25-004-steel-beam-flexure-and-lateral-torsional-buckling.png)

### Worked Example 4

**Problem.** Increasing unbraced length can reduce available moment strength.

**Solution.** Apply the relation and definitions in §25.4; the stated result follows with consistent units and sign convention.

---

## 25.5 Beam shear and serviceability

Shear strength and deflection are separate checks. A beam can satisfy strength but fail a serviceability requirement.

\[\phi V_n\ge V_u\]

![FIG-03-25-005: Beam cross-section and span with separate flexure, shear, and deflection check callouts.](../figures/FIG-03-25-005-beam-shear-and-serviceability.png)

### Worked Example 5

**Problem.** A shallow long-span beam may be deflection-controlled even when flexural strength is adequate.

**Solution.** Apply the relation and definitions in §25.5; the stated result follows with consistent units and sign convention.

---

## 25.6 Steel column compression strength

Column design uses critical stress based on slenderness and material properties. The weakest buckling axis can control.

\[\phi P_n=\phi F_{cr}A_g\]

![FIG-03-25-006: W-shape column with x/y buckling axes and critical-stress versus slenderness chart.](../figures/FIG-03-25-006-steel-column-compression-strength.png)

### Worked Example 6

**Problem.** Compare KL/r about both principal axes before selecting the governing Fcr.

**Solution.** Apply the relation and definitions in §25.6; the stated result follows with consistent units and sign convention.

---

## 25.7 Section selection and handbook-table use

FE problems may rely on handbook tabulations for W-shape dimensions, properties, and available strength. Read the exact table heading and units.

\[\text{select section so all required checks pass}\]

![FIG-03-25-007: Annotated W-shape table excerpt concept showing A, Ix, Sx, rx, ry, and available strength columns.](../figures/FIG-03-25-007-section-selection-and-handbook-table-use.png)

### Worked Example 7

**Problem.** A section with adequate moment strength may still require a larger Ix for deflection.

**Solution.** Apply the relation and definitions in §25.7; the stated result follows with consistent units and sign convention.

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

1. Use §25.1. If φRn=180 kip and demand is 165 kip, the checked limit state passes. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §25.2. A bolted connection may have a smaller net area than gross area, causing fracture to control. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §25.3. A stronger bolt does not prevent net-section fracture of the plate. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §25.4. Increasing unbraced length can reduce available moment strength. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §25.5. A shallow long-span beam may be deflection-controlled even when flexural strength is adequate. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §25.6. Compare KL/r about both principal axes before selecting the governing Fcr. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §25.7. A section with adequate moment strength may still require a larger Ix for deflection. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 11 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

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
