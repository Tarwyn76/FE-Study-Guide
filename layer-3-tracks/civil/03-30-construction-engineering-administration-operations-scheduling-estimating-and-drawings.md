---
chapter: "03-30"
title: "Construction Engineering — Administration, Operations, Scheduling, Estimating, and Drawings"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-030-01, CIV-3-030-02, CIV-3-030-03, CIV-3-030-04, CIV-3-030-05, CIV-3-030-06, CIV-3-030-07]
routes: [civil]
status: drafted
---

# Chapter 03-30: Construction Engineering — Administration, Operations, Scheduling, Estimating, and Drawings

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** ECON-2A-005-01

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Construction Engineering — Administration, Operations, Scheduling, Estimating, and Drawings**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **30.1** Explain and apply **Project delivery, contracts, procurement, and administration**.
* **30.2** Explain and apply **Construction safety, means and methods, and temporary works**.
* **30.3** Explain and apply **Equipment production and productivity analysis**.
* **30.4** Explain and apply **Network scheduling, precedence, and critical path**.
* **30.5** Explain and apply **Earned value and project controls**.
* **30.6** Explain and apply **Quantity takeoff and construction estimating**.
* **30.7** Explain and apply **Engineering drawings, sections, scales, and coordination**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 30.1 Project delivery, contracts, procurement, and administration

Construction administration coordinates contractual responsibilities, submittals, changes, payments, documentation, and delivery method constraints.

\[\text{scope}+\text{time}+\text{cost}+\text{quality}+\text{risk}\]

![FIG-03-30-001: Comparison of design-bid-build, design-build, and construction-manager relationships.](../figures/FIG-03-30-001-project-delivery-contracts-procurement-and-administration.png)

### Worked Example 1

**Problem.** A design-bid-build project separates designer and constructor contracts with the owner.

**Solution.** Design-bid-build uses separate contractual relationships: the owner contracts with the designer for design services and separately with the contractor for construction after bidding. This separation differs from design-build, where design and construction responsibility are combined under one entity.

---

## 30.2 Construction safety, means and methods, and temporary works

Construction means and methods govern how work is performed. Safety planning, temporary works, access, and sequencing can control feasibility.

\[\text{risk}=\text{likelihood}\times\text{consequence}\]

![FIG-03-30-002: Construction site showing excavation protection, crane swing, access route, temporary erosion control, and exclusion zones.](../figures/FIG-03-30-002-construction-safety-means-and-methods-and-temporary-works.png)

### Worked Example 2

**Problem.** A safe excavation plan must address soil, depth, surcharge, access, and protective system.

**Solution.** Excavation safety depends on more than depth. The plan must consider soil classification, excavation geometry, surcharge loads, groundwater, adjacent structures, access/egress, and the required protective system such as sloping, benching, shoring, or shielding.

---

## 30.3 Equipment production and productivity analysis

Equipment cycles, utilization, crew balance, and delays control production. Compare units carefully before translating production into duration or cost.

\[\text{production rate}=\frac{\text{quantity}}{\text{time}}\]

![FIG-03-30-003: Earthmoving production cycle with load, haul, dump, return, and cycle-time components.](../figures/FIG-03-30-003-equipment-production-and-productivity-analysis.png)

### Worked Example 3

**Problem.** A crew placing 240 yd³ in 8 hr averages 30 yd³/hr.

**Solution.** Average production rate is quantity divided by time. \(240\ \text{yd}^3/8\ \text{hr}=30\ \text{yd}^3/\text{hr}\). The final production rate is **30 yd³/hr** (approximately **22.9 m^3/h**). This is an average crew production rate over the stated shift and does not by itself include utilization or delay factors.

---

## 30.4 Network scheduling, precedence, and critical path

Critical-path scheduling computes early and late dates from activity logic. Zero-total-float activities form at least one critical path.

\[\text{total float}=LS-ES=LF-EF\]

![FIG-03-30-004: Activity-on-node schedule network with durations, ES/EF/LS/LF, and highlighted critical path.](../figures/FIG-03-30-004-network-scheduling-precedence-and-critical-path.png)

### Worked Example 4

**Problem.** An activity with ES=5 days and LS=5 days has zero total float.

**Solution.** Total float may be computed as \(TF=LS-ES\) when durations are unchanged. With \(LS=5\) days and \(ES=5\) days, \(TF=0\) days, so the activity is critical under the current schedule logic.

---

## 30.5 Earned value and project controls

Earned value separates planned work, performed work, and actual cost. Sign conventions indicate favorable or unfavorable variance.

\[CV=EV-AC,\qquad SV=EV-PV\]

![FIG-03-30-005: Planned value, earned value, and actual cost curves over project time with variance callouts.](../figures/FIG-03-30-005-earned-value-and-project-controls.png)

### Worked Example 5

**Problem.** EV=90k and AC=100k gives CV=-10k, over budget.

**Solution.** Cost variance is \(CV=EV-AC\). With \(EV=\$90{,}000\) and \(AC=\$100{,}000\), \(CV=-\$10{,}000\). A negative cost variance indicates the work accomplished has cost more than its earned value, so the project is over budget for that measure.

---

## 30.6 Quantity takeoff and construction estimating

Estimating starts with scope and measured quantities, then applies labor, equipment, material, subcontract, and indirect costs.

\[\text{cost}=\sum (\text{quantity}\times\text{unit cost})+\text{indirects}\]

![FIG-03-30-006: Drawing quantity callouts flowing into takeoff, unit-price estimate, indirects, contingency, and total.](../figures/FIG-03-30-006-quantity-takeoff-and-construction-estimating.png)

### Worked Example 6

**Problem.** 500 ft of pipe at $42/ft has $21,000 direct line-item cost before adders.

**Solution.** Direct line-item cost is quantity times unit price: \(500\ \text{ft}\times\$42/\text{ft}=\$21{,}000\). This is the direct item cost before mobilization, overhead, contingency, profit, or other project adders.

---

## 30.7 Engineering drawings, sections, scales, and coordination

Plans, elevations, sections, details, schedules, notes, and specifications must be read together. A detail can override a general graphic indication when explicitly referenced.

\[\text{actual length}=\text{drawing length}\times\text{scale factor}\]

![FIG-03-30-007: Coordinated plan, section, detail bubble, schedule, dimensions, and specification reference for one construction element.](../figures/FIG-03-30-007-engineering-drawings-sections-scales-and-coordination.png)

### Worked Example 7

**Problem.** At 1/4 in = 1 ft, a 6-in drawing length represents 24 ft.

**Solution.** At a scale of \(1/4\ \text{in}=1\ \text{ft}\), each drawing inch represents \(1/(1/4)=4\ \text{ft}\). Therefore a 6-in drawing length represents \(6(4)=24\ \text{ft}\) in the field.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a construction-planning problem, establish the work quantity and method first, convert them into production rate and duration, then place the activity into the schedule and cost framework. Keeping quantity takeoff, productivity, schedule logic, and earned-value metrics distinct prevents circular calculations.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook equation or definition for the requested metric—production, float, earned value, estimating, or scale—and preserve its sign convention. Construction metrics often use similar abbreviations with different meanings, so the Handbook definition should control the exam solution.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 14; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** Some Civil specification topics are directly tabulated in the Handbook; others are named by the specification but require learned engineering knowledge. This chapter does not imply that every workflow, code provision, or design factor is printed in the Handbook.

Where the FE specification requires a topic that is not directly developed in the Handbook, the ledger marks it **specification-required / guide-developed** rather than inventing a Handbook citation.

---

## Where This Goes Wrong

**Using construction project administration without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using construction operations without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using construction productivity without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using critical path method without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using earned value management without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using construction estimate without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using construction drawing interpretation without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| construction project administration | Concept developed in §30.1; apply with that section's stated assumptions and units. |
| construction operations | Concept developed in §30.2; apply with that section's stated assumptions and units. |
| construction productivity | Concept developed in §30.3; apply with that section's stated assumptions and units. |
| critical path method | Concept developed in §30.4; apply with that section's stated assumptions and units. |
| earned value management | Concept developed in §30.5; apply with that section's stated assumptions and units. |
| construction estimate | Concept developed in §30.6; apply with that section's stated assumptions and units. |
| construction drawing interpretation | Concept developed in §30.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **construction project administration** and identify the principal quantity, relation, or decision it organizes.

2. Define **construction operations** and identify the principal quantity, relation, or decision it organizes.

3. Define **construction productivity** and identify the principal quantity, relation, or decision it organizes.

4. Define **critical path method** and identify the principal quantity, relation, or decision it organizes.

5. Define **earned value management** and identify the principal quantity, relation, or decision it organizes.

6. Define **construction estimate** and identify the principal quantity, relation, or decision it organizes.

7. Define **construction drawing interpretation** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **construction project administration**?

9. What assumption or unit error is most likely to cause a wrong result when applying **construction operations**?

10. What assumption or unit error is most likely to cause a wrong result when applying **construction productivity**?

11. What assumption or unit error is most likely to cause a wrong result when applying **critical path method**?

12. What assumption or unit error is most likely to cause a wrong result when applying **earned value management**?

13. What assumption or unit error is most likely to cause a wrong result when applying **construction estimate**?

14. What assumption or unit error is most likely to cause a wrong result when applying **construction drawing interpretation**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **construction project administration**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **construction operations**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **construction productivity**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **critical path method**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **earned value management**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **construction estimate**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **construction drawing interpretation**?
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

1. **construction project administration** is developed in §30.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **construction operations** is developed in §30.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **construction productivity** is developed in §30.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **critical path method** is developed in §30.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **earned value management** is developed in §30.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **construction estimate** is developed in §30.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **construction drawing interpretation** is developed in §30.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **construction project administration**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **construction operations**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **construction productivity**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **critical path method**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **earned value management**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **construction estimate**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **construction drawing interpretation**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. Draw the activity network, site operation, quantity takeoff, or contractual relationship before calculating so precedence, work scope, production quantity, and responsibility are defined correctly.

16. Use the Handbook schedule, estimating, earned-value, or scale definition when provided because the sign convention and metric definition determine how float and cost/schedule variances are interpreted.

17. Construction problems can mix days, hours, feet, cubic yards, dollars, and production rates; convert the time and quantity bases before comparing productivity, duration, or cost.

18. Check schedule and cost logic: critical activities should have zero total float under the current network, production rate times duration should reproduce quantity, and earned-value variance signs should match the stated performance.

19. **A.** For **Project delivery, contracts, procurement, and administration**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Construction safety, means and methods, and temporary works**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Equipment production and productivity analysis**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Network scheduling, precedence, and critical path**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Earned value and project controls**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Quantity takeoff and construction estimating**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Engineering drawings, sections, scales, and coordination**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Construction Engineering — Administration, Operations, Scheduling, Estimating, and Drawings, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Core construction metrics are tied to the FE Handbook and ledger; delivery-method or administration discussion beyond those definitions is labeled learned material or guide synthesis rather than given an unsupported Handbook citation.



---

## Practice Problems

1. A design-bid-build project separates designer and constructor contracts with the owner.

2. A safe excavation plan must address soil, depth, surcharge, access, and protective system.

3. A crew placing 240 yd³ in 8 hr averages 30 yd³/hr.

4. An activity with ES=5 days and LS=5 days has zero total float.

5. EV=90k and AC=100k gives CV=-10k, over budget.

6. 500 ft of pipe at $42/ft has $21,000 direct line-item cost before adders.

7. At 1/4 in = 1 ft, a 6-in drawing length represents 24 ft.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. **Independent check for §30.1.** Rework the problem from the stated givens rather than copying the worked-example result. Design-bid-build uses separate contractual relationships: the owner contracts with the designer for design services and separately with the contractor for construction after bidding. This separation differs from design-build, where design and construction responsibility are combined under one entity. **Check:** confirm the final magnitude and units against the physical meaning of §30.1 before accepting the answer.



2. **Independent check for §30.2.** Rework the problem from the stated givens rather than copying the worked-example result. Excavation safety depends on more than depth. The plan must consider soil classification, excavation geometry, surcharge loads, groundwater, adjacent structures, access/egress, and the required protective system such as sloping, benching, shoring, or shielding. **Check:** confirm the final magnitude and units against the physical meaning of §30.2 before accepting the answer.



3. **Independent check for §30.3.** Rework the problem from the stated givens rather than copying the worked-example result. Average production rate is quantity divided by time. \(240\ \text{yd}^3/8\ \text{hr}=30\ \text{yd}^3/\text{hr}\). This is an average crew production rate over the stated shift and does not by itself include utilization or delay factors. **Check:** confirm the final magnitude and units against the physical meaning of §30.3 before accepting the answer.



4. **Independent check for §30.4.** Rework the problem from the stated givens rather than copying the worked-example result. Total float may be computed as \(TF=LS-ES\) when durations are unchanged. With \(LS=5\) days and \(ES=5\) days, \(TF=0\) days, so the activity is critical under the current schedule logic. **Check:** confirm the final magnitude and units against the physical meaning of §30.4 before accepting the answer.



5. **Independent check for §30.5.** Rework the problem from the stated givens rather than copying the worked-example result. Cost variance is \(CV=EV-AC\). With \(EV=\$90{,}000\) and \(AC=\$100{,}000\), \(CV=-\$10{,}000\). A negative cost variance indicates the work accomplished has cost more than its earned value, so the project is over budget for that measure. **Check:** confirm the final magnitude and units against the physical meaning of §30.5 before accepting the answer.



6. **Independent check for §30.6.** Rework the problem from the stated givens rather than copying the worked-example result. Direct line-item cost is quantity times unit price: \(500\ \text{ft}\times\$42/\text{ft}=\$21{,}000\). This is the direct item cost before mobilization, overhead, contingency, profit, or other project adders. **Check:** confirm the final magnitude and units against the physical meaning of §30.6 before accepting the answer.



7. **Independent check for §30.7.** Rework the problem from the stated givens rather than copying the worked-example result. At a scale of \(1/4\ \text{in}=1\ \text{ft}\), each drawing inch represents \(1/(1/4)=4\ \text{ft}\). Therefore a 6-in drawing length represents \(6(4)=24\ \text{ft}\) in the field. **Check:** confirm the final magnitude and units against the physical meaning of §30.7 before accepting the answer.



8. Before accepting a construction engineering — administration, operations, scheduling, estimating, and drawings result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Begin with **FE Civil specification Area 14** and the construction/scheduling/estimating definition recorded in the ledger; keep any delivery-method or administration knowledge clearly labeled when it is outside Handbook tables.

10. For construction engineering — administration, operations, scheduling, estimating, and drawings, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 14.

- **construction project administration:** Project delivery, contracts, procurement, and administration
- **construction operations:** Construction safety, means and methods, and temporary works
- **construction productivity:** Equipment production and productivity analysis
- **critical path method:** Network scheduling, precedence, and critical path
- **earned value management:** Earned value and project controls
- **construction estimate:** Quantity takeoff and construction estimating
- **construction drawing interpretation:** Engineering drawings, sections, scales, and coordination

---

## What's Next

**Electrical & Computer Engineering begins at 03-31**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
