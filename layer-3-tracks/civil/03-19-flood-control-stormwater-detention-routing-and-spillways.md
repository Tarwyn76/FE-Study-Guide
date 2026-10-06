---
chapter: "03-19"
title: "Flood Control, Stormwater Detention, Routing, and Spillways"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-019-01, CIV-3-019-02, CIV-3-019-03, CIV-3-019-04, CIV-3-019-05, CIV-3-019-06, CIV-3-019-07]
routes: [civil]
status: drafted
---

# Chapter 03-19: Flood Control, Stormwater Detention, Routing, and Spillways

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-016-07

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Flood Control, Stormwater Detention, Routing, and Spillways**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **19.1** Explain and apply **Flood-frequency concepts and design-event selection**.
* **19.2** Explain and apply **Reservoir and detention continuity**.
* **19.3** Explain and apply **Level-pool routing and storage-indication concepts**.
* **19.4** Explain and apply **Stormwater detention sizing and outlet control**.
* **19.5** Explain and apply **Spillway discharge and hydraulic control**.
* **19.6** Explain and apply **Dams, freeboard, and flood-control operating concepts**.
* **19.7** Explain and apply **Stormwater quality and erosion-control integration**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 19.1 Flood-frequency concepts and design-event selection

Return period is the reciprocal of annual exceedance probability under the usual stationary interpretation. It does not mean an event occurs exactly once every T years.

\[P_{\text{annual exceedance}}=\frac{1}{T_r}\]

![FIG-03-19-001: Annual exceedance probability versus return period with common design events marked.](../figures/FIG-03-19-001-flood-frequency-concepts-and-design-event-selection.png)

### Worked Example 1

**Problem.** A 100-year event has 1% annual exceedance probability.

**Solution.** Apply the relation and definitions in §19.1; the stated result follows with consistent units and sign convention.

---

## 19.2 Reservoir and detention continuity

Detention attenuates peaks by temporarily storing inflow and releasing it more slowly. Routing couples storage and outflow relationships through continuity.

\[\frac{dS}{dt}=I-O\]

![FIG-03-19-002: Detention basin with inflow hydrograph, storage, outlet structure, and attenuated outflow hydrograph.](../figures/FIG-03-19-002-reservoir-and-detention-continuity.png)

### Worked Example 2

**Problem.** If inflow exceeds outflow by 20 cfs for 10 min, storage rises by 12,000 ft³.

**Solution.** Apply the relation and definitions in §19.2; the stated result follows with consistent units and sign convention.

---

## 19.3 Level-pool routing and storage-indication concepts

Level-pool routing assumes the water surface is essentially horizontal across the reservoir at each time step. Storage and outflow are related to stage.

\[\Delta S\approx \frac{\Delta t}{2}\left[(I_1+I_2)-(O_1+O_2)\right]\]

![FIG-03-19-003: Stage-storage-outflow curves beside a time-step routing table.](../figures/FIG-03-19-003-level-pool-routing-and-storage-indication-concepts.png)

### Worked Example 3

**Problem.** Trapezoidal integration of inflow and outflow gives the storage change over a step.

**Solution.** Apply the relation and definitions in §19.3; the stated result follows with consistent units and sign convention.

---

## 19.4 Stormwater detention sizing and outlet control

Peak-flow reduction depends on available storage and the outlet rating. The maximum storage occurs when cumulative inflow minus cumulative outflow is greatest.

\[\Delta S=\int (I-O)\,dt\]

![FIG-03-19-004: Inflow and outflow hydrographs with shaded temporary-storage volume.](../figures/FIG-03-19-004-stormwater-detention-sizing-and-outlet-control.png)

### Worked Example 4

**Problem.** The area between inflow and outflow hydrographs up to their crossing represents stored volume.

**Solution.** Apply the relation and definitions in §19.4; the stated result follows with consistent units and sign convention.

---

## 19.5 Spillway discharge and hydraulic control

Spillways safely pass flows that exceed normal outlet capacity. The controlling head must be referenced to the crest or control section defined by the equation.

\[Q=C\,L\,H^{3/2}\]

![FIG-03-19-005: Reservoir cross-section with normal pool, design flood pool, spillway crest, head, and downstream energy dissipation.](../figures/FIG-03-19-005-spillway-discharge-and-hydraulic-control.png)

### Worked Example 5

**Problem.** If head doubles and coefficient remains constant, discharge scales by 2^(3/2).

**Solution.** Apply the relation and definitions in §19.5; the stated result follows with consistent units and sign convention.

---

## 19.6 Dams, freeboard, and flood-control operating concepts

A flood-control structure requires hydraulic capacity plus margin for uncertainty and wave effects. Freeboard is not active storage.

\[\text{freeboard}=z_{\text{crest}}-z_{\text{design water surface}}\]

![FIG-03-19-006: Dam section labeling conservation pool, flood-control pool, spillway, freeboard, and crest elevation.](../figures/FIG-03-19-006-dams-freeboard-and-flood-control-operating-concepts.png)

### Worked Example 6

**Problem.** A crest at 1010 ft and design water surface at 1004 ft provides 6 ft freeboard.

**Solution.** Apply the relation and definitions in §19.6; the stated result follows with consistent units and sign convention.

---

## 19.7 Stormwater quality and erosion-control integration

Stormwater design addresses both flow and pollutant transport. Temporary and permanent controls may target peak discharge, sediment, floatables, nutrients, or other constituents.

\[\text{load}=Q\,C\]

![FIG-03-19-007: Treatment train from inlet to sediment forebay, detention cell, outlet, and stabilized channel.](../figures/FIG-03-19-007-stormwater-quality-and-erosion-control-integration.png)

### Worked Example 7

**Problem.** At Q=2 m³/s and C=20 mg/L, instantaneous mass rate is 40 g/s.

**Solution.** Apply the relation and definitions in §19.7; the stated result follows with consistent units and sign convention.

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

**Using design flood without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using reservoir routing continuity without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using level-pool routing without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using stormwater detention without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using spillway discharge without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using flood-control storage without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using stormwater quality control without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| design flood | Concept developed in §19.1; apply with that section's stated assumptions and units. |
| reservoir routing continuity | Concept developed in §19.2; apply with that section's stated assumptions and units. |
| level-pool routing | Concept developed in §19.3; apply with that section's stated assumptions and units. |
| stormwater detention | Concept developed in §19.4; apply with that section's stated assumptions and units. |
| spillway discharge | Concept developed in §19.5; apply with that section's stated assumptions and units. |
| flood-control storage | Concept developed in §19.6; apply with that section's stated assumptions and units. |
| stormwater quality control | Concept developed in §19.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **design flood** and identify the principal quantity, relation, or decision it organizes.

2. Define **reservoir routing continuity** and identify the principal quantity, relation, or decision it organizes.

3. Define **level-pool routing** and identify the principal quantity, relation, or decision it organizes.

4. Define **stormwater detention** and identify the principal quantity, relation, or decision it organizes.

5. Define **spillway discharge** and identify the principal quantity, relation, or decision it organizes.

6. Define **flood-control storage** and identify the principal quantity, relation, or decision it organizes.

7. Define **stormwater quality control** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **design flood**?

9. What assumption or unit error is most likely to cause a wrong result when applying **reservoir routing continuity**?

10. What assumption or unit error is most likely to cause a wrong result when applying **level-pool routing**?

11. What assumption or unit error is most likely to cause a wrong result when applying **stormwater detention**?

12. What assumption or unit error is most likely to cause a wrong result when applying **spillway discharge**?

13. What assumption or unit error is most likely to cause a wrong result when applying **flood-control storage**?

14. What assumption or unit error is most likely to cause a wrong result when applying **stormwater quality control**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **design flood**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **reservoir routing continuity**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **level-pool routing**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **stormwater detention**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **spillway discharge**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **flood-control storage**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **stormwater quality control**?
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

1. **design flood** is developed in §19.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **reservoir routing continuity** is developed in §19.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **level-pool routing** is developed in §19.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **stormwater detention** is developed in §19.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **spillway discharge** is developed in §19.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **flood-control storage** is developed in §19.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **stormwater quality control** is developed in §19.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **design flood**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **reservoir routing continuity**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **level-pool routing**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **stormwater detention**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **spillway discharge**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **flood-control storage**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **stormwater quality control**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

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

1. A 100-year event has 1% annual exceedance probability.

2. If inflow exceeds outflow by 20 cfs for 10 min, storage rises by 12,000 ft³.

3. Trapezoidal integration of inflow and outflow gives the storage change over a step.

4. The area between inflow and outflow hydrographs up to their crossing represents stored volume.

5. If head doubles and coefficient remains constant, discharge scales by 2^(3/2).

6. A crest at 1010 ft and design water surface at 1004 ft provides 6 ft freeboard.

7. At Q=2 m³/s and C=20 mg/L, instantaneous mass rate is 40 g/s.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §19.1. A 100-year event has 1% annual exceedance probability. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §19.2. If inflow exceeds outflow by 20 cfs for 10 min, storage rises by 12,000 ft³. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §19.3. Trapezoidal integration of inflow and outflow gives the storage change over a step. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §19.4. The area between inflow and outflow hydrographs up to their crossing represents stored volume. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §19.5. If head doubles and coefficient remains constant, discharge scales by 2^(3/2). The calculation or classification follows from the displayed section relation and the stated data.

6. Use §19.6. A crest at 1010 ft and design water surface at 1004 ft provides 6 ft freeboard. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §19.7. At Q=2 m³/s and C=20 mg/L, instantaneous mass rate is 40 g/s. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 10 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 10.

- **design flood:** Flood-frequency concepts and design-event selection
- **reservoir routing continuity:** Reservoir and detention continuity
- **level-pool routing:** Level-pool routing and storage-indication concepts
- **stormwater detention:** Stormwater detention sizing and outlet control
- **spillway discharge:** Spillway discharge and hydraulic control
- **flood-control storage:** Dams, freeboard, and flood-control operating concepts
- **stormwater quality control:** Stormwater quality and erosion-control integration

---

## What's Next

**Chapter 03-20: Groundwater Flow, Aquifer Properties, Wells, and Drawdown**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
