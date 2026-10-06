---
chapter: "03-20"
title: "Groundwater Flow, Aquifer Properties, Wells, and Drawdown"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-020-01, CIV-3-020-02, CIV-3-020-03, CIV-3-020-04, CIV-3-020-05, CIV-3-020-06, CIV-3-020-07]
routes: [civil]
status: drafted
---

# Chapter 03-20: Groundwater Flow, Aquifer Properties, Wells, and Drawdown

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-016-07

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Groundwater Flow, Aquifer Properties, Wells, and Drawdown**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **20.1** Explain and apply **Darcy law and hydraulic gradient**.
* **20.2** Explain and apply **Hydraulic conductivity, permeability tests, and anisotropy**.
* **20.3** Explain and apply **Aquifer transmissivity and confined flow**.
* **20.4** Explain and apply **Unconfined aquifers and water-table concepts**.
* **20.5** Explain and apply **Well drawdown and radial flow**.
* **20.6** Explain and apply **Multiple wells, superposition, and interference**.
* **20.7** Explain and apply **Seepage, effective stress, and groundwater-structure interaction**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 20.1 Darcy law and hydraulic gradient

Darcy's law relates discharge to hydraulic conductivity, gradient, and area for laminar porous-media flow. The sign of gradient follows the chosen head coordinate.

\[Q=K\,i\,A\]

![FIG-03-20-001: Groundwater flow through soil prism with head difference, length, gradient, K, area, and Q.](../figures/FIG-03-20-001-darcy-law-and-hydraulic-gradient.png)

### Worked Example 1

**Problem.** K=1e-4 m/s, i=0.02, A=50 m² gives Q=1e-4 m³/s.

**Solution.** Apply the relation and definitions in §20.1; the stated result follows with consistent units and sign convention.

---

## 20.2 Hydraulic conductivity, permeability tests, and anisotropy

Laboratory constant-head and falling-head tests infer hydraulic conductivity from measured flow and head change. Field values may differ because of scale and stratification.

\[K=\frac{Q}{iAt}\]

![FIG-03-20-002: Constant-head and falling-head permeability test apparatus side by side.](../figures/FIG-03-20-002-hydraulic-conductivity-permeability-tests-and-anisotropy.png)

### Worked Example 2

**Problem.** Given measured volume, elapsed time, gradient, and area, solve for K with consistent units.

**Solution.** Apply the relation and definitions in §20.2; the stated result follows with consistent units and sign convention.

---

## 20.3 Aquifer transmissivity and confined flow

Transmissivity combines hydraulic conductivity and saturated thickness. It is especially useful for confined-aquifer well relations.

\[T=Kb\]

![FIG-03-20-003: Confined aquifer cross-section with aquitards, thickness b, piezometric surface, and pumping well.](../figures/FIG-03-20-003-aquifer-transmissivity-and-confined-flow.png)

### Worked Example 3

**Problem.** K=30 m/day and b=20 m gives T=600 m²/day.

**Solution.** Apply the relation and definitions in §20.3; the stated result follows with consistent units and sign convention.

---

## 20.4 Unconfined aquifers and water-table concepts

In an unconfined aquifer, the water table is a free surface. Saturated thickness changes as drawdown develops.

\[h=z+\frac{p}{\gamma}\]

![FIG-03-20-004: Unconfined aquifer with water table, recharge, pumping well, and cone of depression.](../figures/FIG-03-20-004-unconfined-aquifers-and-water-table-concepts.png)

### Worked Example 4

**Problem.** At the water table, gauge pressure is approximately zero, so hydraulic head equals elevation head.

**Solution.** Apply the relation and definitions in §20.4; the stated result follows with consistent units and sign convention.

---

## 20.5 Well drawdown and radial flow

Pumping lowers hydraulic head near a well, creating a cone of depression. FE problems may provide the radial-flow relation directly or through the Handbook.

\[s=h_0-h(r)\]

![FIG-03-20-005: Plan and cross-sectional views of a pumping well cone of depression with radius and drawdown labels.](../figures/FIG-03-20-005-well-drawdown-and-radial-flow.png)

### Worked Example 5

**Problem.** If static head is 120 ft and pumping head is 108 ft, drawdown is 12 ft.

**Solution.** Apply the relation and definitions in §20.5; the stated result follows with consistent units and sign convention.

---

## 20.6 Multiple wells, superposition, and interference

When the governing groundwater equation is linear over the modeled range, drawdowns from multiple wells can be superposed approximately.

\[s_{\text{total}}\approx \sum s_i\]

![FIG-03-20-006: Two pumping wells with overlapping cones of depression and a shared observation point.](../figures/FIG-03-20-006-multiple-wells-superposition-and-interference.png)

### Worked Example 6

**Problem.** Two wells causing 3 ft and 5 ft drawdown at a point produce about 8 ft total by superposition.

**Solution.** Apply the relation and definitions in §20.6; the stated result follows with consistent units and sign convention.

---

## 20.7 Seepage, effective stress, and groundwater-structure interaction

Groundwater flow affects uplift, piping, effective stress, and excavation stability. Hydraulic and geotechnical calculations must use the same head reference.

\[i=\frac{\Delta h}{L}\]

![FIG-03-20-007: Flow net beneath a retaining or cutoff structure showing equipotential lines, flow lines, head loss, and exit gradient.](../figures/FIG-03-20-007-seepage-effective-stress-and-groundwater-structure-interaction.png)

### Worked Example 7

**Problem.** A 6 m head drop over 30 m gives gradient 0.20.

**Solution.** Apply the relation and definitions in §20.7; the stated result follows with consistent units and sign convention.

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

**Using Darcy groundwater flow without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using hydraulic conductivity without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using transmissivity without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using unconfined aquifer without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using well drawdown without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using well interference without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using seepage gradient without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| Darcy groundwater flow | Concept developed in §20.1; apply with that section's stated assumptions and units. |
| hydraulic conductivity | Concept developed in §20.2; apply with that section's stated assumptions and units. |
| transmissivity | Concept developed in §20.3; apply with that section's stated assumptions and units. |
| unconfined aquifer | Concept developed in §20.4; apply with that section's stated assumptions and units. |
| well drawdown | Concept developed in §20.5; apply with that section's stated assumptions and units. |
| well interference | Concept developed in §20.6; apply with that section's stated assumptions and units. |
| seepage gradient | Concept developed in §20.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **Darcy groundwater flow** and identify the principal quantity, relation, or decision it organizes.

2. Define **hydraulic conductivity** and identify the principal quantity, relation, or decision it organizes.

3. Define **transmissivity** and identify the principal quantity, relation, or decision it organizes.

4. Define **unconfined aquifer** and identify the principal quantity, relation, or decision it organizes.

5. Define **well drawdown** and identify the principal quantity, relation, or decision it organizes.

6. Define **well interference** and identify the principal quantity, relation, or decision it organizes.

7. Define **seepage gradient** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **Darcy groundwater flow**?

9. What assumption or unit error is most likely to cause a wrong result when applying **hydraulic conductivity**?

10. What assumption or unit error is most likely to cause a wrong result when applying **transmissivity**?

11. What assumption or unit error is most likely to cause a wrong result when applying **unconfined aquifer**?

12. What assumption or unit error is most likely to cause a wrong result when applying **well drawdown**?

13. What assumption or unit error is most likely to cause a wrong result when applying **well interference**?

14. What assumption or unit error is most likely to cause a wrong result when applying **seepage gradient**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **Darcy groundwater flow**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **hydraulic conductivity**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **transmissivity**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **unconfined aquifer**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **well drawdown**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **well interference**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **seepage gradient**?
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

1. **Darcy groundwater flow** is developed in §20.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **hydraulic conductivity** is developed in §20.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **transmissivity** is developed in §20.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **unconfined aquifer** is developed in §20.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **well drawdown** is developed in §20.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **well interference** is developed in §20.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **seepage gradient** is developed in §20.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **Darcy groundwater flow**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **hydraulic conductivity**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **transmissivity**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **unconfined aquifer**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **well drawdown**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **well interference**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **seepage gradient**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

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

1. K=1e-4 m/s, i=0.02, A=50 m² gives Q=1e-4 m³/s.

2. Given measured volume, elapsed time, gradient, and area, solve for K with consistent units.

3. K=30 m/day and b=20 m gives T=600 m²/day.

4. At the water table, gauge pressure is approximately zero, so hydraulic head equals elevation head.

5. If static head is 120 ft and pumping head is 108 ft, drawdown is 12 ft.

6. Two wells causing 3 ft and 5 ft drawdown at a point produce about 8 ft total by superposition.

7. A 6 m head drop over 30 m gives gradient 0.20.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §20.1. K=1e-4 m/s, i=0.02, A=50 m² gives Q=1e-4 m³/s. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §20.2. Given measured volume, elapsed time, gradient, and area, solve for K with consistent units. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §20.3. K=30 m/day and b=20 m gives T=600 m²/day. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §20.4. At the water table, gauge pressure is approximately zero, so hydraulic head equals elevation head. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §20.5. If static head is 120 ft and pumping head is 108 ft, drawdown is 12 ft. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §20.6. Two wells causing 3 ft and 5 ft drawdown at a point produce about 8 ft total by superposition. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §20.7. A 6 m head drop over 30 m gives gradient 0.20. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 10 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 10.

- **Darcy groundwater flow:** Darcy law and hydraulic gradient
- **hydraulic conductivity:** Hydraulic conductivity, permeability tests, and anisotropy
- **transmissivity:** Aquifer transmissivity and confined flow
- **unconfined aquifer:** Unconfined aquifers and water-table concepts
- **well drawdown:** Well drawdown and radial flow
- **well interference:** Multiple wells, superposition, and interference
- **seepage gradient:** Seepage, effective stress, and groundwater-structure interaction

---

## What's Next

**Chapter 03-21: Water Quality and Water/Wastewater Treatment for Civil Applications**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
