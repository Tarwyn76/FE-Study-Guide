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

**Solution.** Annual exceedance probability is approximately \(P=1/T_r\). For a 100-year return period, \(P=1/100=0.01=1\%\) per year. A 100-year designation does not mean the event occurs only once every 100 years.

---

## 19.2 Reservoir and detention continuity

Detention attenuates peaks by temporarily storing inflow and releasing it more slowly. Routing couples storage and outflow relationships through continuity.

\[\frac{dS}{dt}=I-O\]

![FIG-03-19-002: Detention basin with inflow hydrograph, storage, outlet structure, and attenuated outflow hydrograph.](../figures/FIG-03-19-002-reservoir-and-detention-continuity.png)

### Worked Example 2

**Problem.** If inflow exceeds outflow by 20 cfs for 10 min, storage rises by 12,000 ft³.

**Solution.** Use reservoir continuity over the time interval. The net inflow is \(20\ \text{ft}^3/\text{s}\) for \(10\ \text{min}=600\ \text{s}\), so \(\Delta S=(20)(600)=12{,}000\ \text{ft}^3\). Storage therefore increases by **12,000 ft³**.

---

## 19.3 Level-pool routing and storage-indication concepts

Level-pool routing assumes the water surface is essentially horizontal across the reservoir at each time step. Storage and outflow are related to stage.

\[\Delta S\approx \frac{\Delta t}{2}\left[(I_1+I_2)-(O_1+O_2)\right]\]

![FIG-03-19-003: Stage-storage-outflow curves beside a time-step routing table.](../figures/FIG-03-19-003-level-pool-routing-and-storage-indication-concepts.png)

### Worked Example 3

**Problem.** Trapezoidal integration of inflow and outflow gives the storage change over a step.

**Solution.** For a finite routing step, approximate the storage change with trapezoidal integration: \(\Delta S\approx\Delta t[(I_1+I_2)-(O_1+O_2)]/2\). This is the average net inflow over the interval multiplied by the step duration; all flow rates and time units must be compatible.

---

## 19.4 Stormwater detention sizing and outlet control

Peak-flow reduction depends on available storage and the outlet rating. The maximum storage occurs when cumulative inflow minus cumulative outflow is greatest.

\[\Delta S=\int (I-O)\,dt\]

![FIG-03-19-004: Inflow and outflow hydrographs with shaded temporary-storage volume.](../figures/FIG-03-19-004-stormwater-detention-sizing-and-outlet-control.png)

### Worked Example 4

**Problem.** The area between inflow and outflow hydrographs up to their crossing represents stored volume.

**Solution.** Storage accumulation is the time integral of \(I-O\). On superimposed inflow and outflow hydrographs, the signed area between the curves gives the change in storage; positive area while inflow exceeds outflow represents detention volume accumulating in the basin.

---

## 19.5 Spillway discharge and hydraulic control

Spillways safely pass flows that exceed normal outlet capacity. The controlling head must be referenced to the crest or control section defined by the equation.

\[Q=C\,L\,H^{3/2}\]

![FIG-03-19-005: Reservoir cross-section with normal pool, design flood pool, spillway crest, head, and downstream energy dissipation.](../figures/FIG-03-19-005-spillway-discharge-and-hydraulic-control.png)

### Worked Example 5

**Problem.** If head doubles and coefficient remains constant, discharge scales by 2^(3/2).

**Solution.** With \(Q=CLH^{3/2}\), holding \(C\) and \(L\) constant gives \(Q\propto H^{3/2}\). Doubling head produces \(Q_2/Q_1=2^{3/2}\approx2.83\), so spillway discharge becomes about 2.83 times the original value.

---

## 19.6 Dams, freeboard, and flood-control operating concepts

A flood-control structure requires hydraulic capacity plus margin for uncertainty and wave effects. Freeboard is not active storage.

\[\text{freeboard}=z_{\text{crest}}-z_{\text{design water surface}}\]

![FIG-03-19-006: Dam section labeling conservation pool, flood-control pool, spillway, freeboard, and crest elevation.](../figures/FIG-03-19-006-dams-freeboard-and-flood-control-operating-concepts.png)

### Worked Example 6

**Problem.** A crest at 1010 ft and design water surface at 1004 ft provides 6 ft freeboard.

**Solution.** Freeboard is crest elevation minus design water-surface elevation. Thus \(1010-1004=6\ \text{ft}\). The final freeboard is **6 ft** (about **1.83 m**). That vertical safety margin should not be confused with storage depth or spillway head.

---

## 19.7 Stormwater quality and erosion-control integration

Stormwater design addresses both flow and pollutant transport. Temporary and permanent controls may target peak discharge, sediment, floatables, nutrients, or other constituents.

\[\text{load}=Q\,C\]

![FIG-03-19-007: Treatment train from inlet to sediment forebay, detention cell, outlet, and stabilized channel.](../figures/FIG-03-19-007-stormwater-quality-and-erosion-control-integration.png)

### Worked Example 7

**Problem.** At Q=2 m³/s and C=20 mg/L, instantaneous mass rate is 40 g/s.

**Solution.** For a flood-control water-quality screening calculation, first put concentration on a discharge-compatible basis: \(20\ \text{mg/L}=20\ \text{g/m}^3\). The instantaneous constituent flux is then \(\dot m=QC=(2\ \text{m}^3/\text{s})(20\ \text{g/m}^3)=40\ \text{g/s}\). This is a mass rate through the control section, not the mass stored in the basin.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a detention problem, first generate or interpret the inflow hydrograph, then route it through the storage/outflow relation. After peak storage and outflow are known, check spillway capacity and freeboard. Keeping hydrologic input generation separate from hydraulic outlet control prevents double counting.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook relation that corresponds to the routing or hydraulic-control model stated in the problem. Return-period probability, storage continuity, and spillway equations describe different parts of the system and should not be substituted for one another simply because they all involve flood design.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 10; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-019-01` — England, J. F., Jr., Cohn, T. A., Faber, B. A., Stedinger, J. R., Thomas, W. O., Jr., Veilleux, A. G., Kiang, J. E., & Mason, R. R., Jr. (2018). *Guidelines for Determining Flood Flow Frequency—Bulletin 17C* (ver. 1.1, May 2019). U.S. Geological Survey Techniques and Methods, Book 4, Chapter B5. https://doi.org/10.3133/tm4B5 Cited at publication/standard level; no page-level claim.
- `CIV-3-019-02` — Kilgore, R., Atayee, A. T., & Herrmann, G. R. (2024). *Urban Drainage Design* (Hydraulic Engineering Circular No. 22, 4th ed., FHWA-HIF-24-006). Federal Highway Administration. Verified location: Chapter 4, pp. 21–24 for rainfall/IDF/design-storm and runoff concepts; Chapter 10, pp. 182–229 for detention, stage-storage/stage-discharge, routing, and outlet control. U.S. Army Corps of Engineers, Hydrologic Engineering Center. *HEC-HMS Technical Reference Manual* (CPD-74B), current online edition. Cited at publication/standard level; no page-level claim.
- `CIV-3-019-04` — Kilgore, R., Atayee, A. T., & Herrmann, G. R. (2024). *Urban Drainage Design* (Hydraulic Engineering Circular No. 22, 4th ed., FHWA-HIF-24-006). Federal Highway Administration. Verified location: Chapter 4, pp. 21–24 for rainfall/IDF/design-storm and runoff concepts; Chapter 10, pp. 182–229 for detention, stage-storage/stage-discharge, routing, and outlet control.
- `CIV-3-019-06` — U.S. Bureau of Reclamation. (2021). *Design Standards No. 13: Embankment Dams, Chapter 6—Freeboard* (DS-13(6)-2.1, Phase 4 Final). U.S. Department of the Interior. Verified location: Chapter 6, pp. 6-1–6-22; especially §§6.2.1–6.2.3 for minimum, normal, and intermediate freeboard and §6.5 for other freeboard factors.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

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

15. Draw the detention basin, inflow hydrograph, outlet, spillway, stage-storage relation, and routing interval before calculating so storage continuity and hydraulic controls are not conflated.

16. Use the Handbook routing or hydraulic-control equation when it is supplied, and then apply the external detention/freeboard guidance only to the learned design details not contained in the Handbook.

17. Flood-routing work can mix cfs, seconds or hours, acre-feet, cubic feet, and elevations; all flow-time products must be converted to consistent storage-volume units.

18. Check conservation and attenuation: routed storage must stay nonnegative, outflow should follow the outlet rating, and a detention basin intended to attenuate a peak should not produce an unexplained peak larger than inflow.

19. **A.** For **Flood-frequency concepts and design-event selection**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Reservoir and detention continuity**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Level-pool routing and storage-indication concepts**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Stormwater detention sizing and outlet control**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Spillway discharge and hydraulic control**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Dams, freeboard, and flood-control operating concepts**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Stormwater quality and erosion-control integration**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Flood Control, Stormwater Detention, Routing, and Spillways, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Detention, routing, and dam-freeboard details outside Handbook tables are explicitly sourced to FHWA HEC-22 and USBR Design Standards No. 13 instead of being misidentified as Handbook text.



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

1. **Independent check for §19.1.** Rework the problem from the stated givens rather than copying the worked-example result. Annual exceedance probability is approximately \(P=1/T_r\). For a 100-year return period, \(P=1/100=0.01=1\%\) per year. A 100-year designation does not mean the event occurs only once every 100 years. **Check:** confirm the final magnitude and units against the physical meaning of §19.1 before accepting the answer.



2. **Independent check for §19.2.** Rework the problem from the stated givens rather than copying the worked-example result. Use reservoir continuity over the time interval. The net inflow is \(20\ \text{ft}^3/\text{s}\) for \(10\ \text{min}=600\ \text{s}\), so \(\Delta S=(20)(600)=12{,}000\ \text{ft}^3\). Storage therefore increases by **12,000 ft³**. **Check:** confirm the final magnitude and units against the physical meaning of §19.2 before accepting the answer.



3. **Independent check for §19.3.** Rework the problem from the stated givens rather than copying the worked-example result. For a finite routing step, approximate the storage change with trapezoidal integration: \(\Delta S\approx\Delta t[(I_1+I_2)-(O_1+O_2)]/2\). This is the average net inflow over the interval multiplied by the step duration; all flow rates and time units must be compatible. **Check:** confirm the final magnitude and units against the physical meaning of §19.3 before accepting the answer.



4. **Independent check for §19.4.** Rework the problem from the stated givens rather than copying the worked-example result. Storage accumulation is the time integral of \(I-O\). On superimposed inflow and outflow hydrographs, the signed area between the curves gives the change in storage; positive area while inflow exceeds outflow represents detention volume accumulating in the basin. **Check:** confirm the final magnitude and units against the physical meaning of §19.4 before accepting the answer.



5. **Independent check for §19.5.** Rework the problem from the stated givens rather than copying the worked-example result. With \(Q=CLH^{3/2}\), holding \(C\) and \(L\) constant gives \(Q\propto H^{3/2}\). Doubling head produces \(Q_2/Q_1=2^{3/2}\approx2.83\), so spillway discharge becomes about 2.83 times the original value. **Check:** confirm the final magnitude and units against the physical meaning of §19.5 before accepting the answer.



6. **Independent check for §19.6.** Rework the problem from the stated givens rather than copying the worked-example result. Freeboard is crest elevation minus design water-surface elevation. Thus \(1010-1004=6\ \text{ft}\). The **6-ft freeboard** is a vertical safety margin and should not be confused with storage depth or spillway head. **Check:** confirm the final magnitude and units against the physical meaning of §19.6 before accepting the answer.



7. **Independent check for §19.7.** Treat the concentration as a constituent flux through the flood-control section. Convert \(20\ \text{mg/L}\) to \(20\ \text{g/m}^3\), multiply by the \(2\ \text{m}^3/\text{s}\) discharge, and obtain \(40\ \text{g/s}\). The check is that discharge times concentration reduces to mass per time; basin storage would require an additional time integration.



8. Before accepting a flood control, stormwater detention, routing, and spillways result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Start with **FE Civil specification Area 10** and the Handbook hydrology/hydraulics entries in the ledger; use FHWA HEC-22 or USBR freeboard guidance for the reconciled learned-design portion.

10. For flood control, stormwater detention, routing, and spillways, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

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
