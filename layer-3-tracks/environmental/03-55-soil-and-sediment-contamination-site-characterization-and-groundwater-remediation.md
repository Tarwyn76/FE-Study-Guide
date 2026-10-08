---
chapter: "03-55"
title: "Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-055-01, ENV-3-055-02, ENV-3-055-03, ENV-3-055-04, ENV-3-055-05, ENV-3-055-06, ENV-3-055-07]
routes: [environmental]
status: drafted
---

# Chapter 03-55: Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** ENV-3-054-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **55.1** Explain and apply **Contaminant source, vadose zone, and saturated-zone conceptual models**.
* **55.2** Explain and apply **Vadose-zone penetration and retention**.
* **55.3** Explain and apply **Sorption, retardation, and contaminant mobility**.
* **55.4** Explain and apply **Site investigation, sampling, and monitoring networks**.
* **55.5** Explain and apply **Pump-and-treat and hydraulic containment**.
* **55.6** Explain and apply **In-situ treatment and monitored natural attenuation**.
* **55.7** Explain and apply **Remedy selection, performance monitoring, and closure**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 55.1 Contaminant source, vadose zone, and saturated-zone conceptual models

A conceptual site model organizes sources, pathways, media, and receptors before sampling or remediation. It should evolve as evidence changes.

\[\text{source}\rightarrow\text{release}\rightarrow\text{transport}\rightarrow\text{receptor}\]

![FIG-03-55-001: Cross-section showing source area, vadose zone, water table, dissolved plume, vapor pathway, and receptors.](../figures/FIG-03-55-001-contaminant-source-vadose-zone-and-saturated-zone-conceptual-models.png)

### Worked Example 1

**Problem.** A leaking tank above a shallow aquifer can create soil-vapor, soil, and groundwater pathways.

**Solution.** A release from a leaking tank above a shallow aquifer can migrate through the vadose zone, generate soil vapor where volatile constituents are present, contaminate soil, and reach groundwater. The conceptual site model must show each plausible source-pathway-receptor connection separately.

---

## 55.2 Vadose-zone penetration and retention

The Handbook provides a simplified hydrocarbon penetration relation using spill volume, area, and a soil/product retention parameter. It is a screening model, not a complete multiphase transport simulation.

\[D=\frac{V}{A R_v}\]

![FIG-03-55-002: Spill infiltrating through vadose-zone soil with estimated penetration depth D and water table below.](../figures/FIG-03-55-002-vadose-zone-penetration-and-retention.png)

### Worked Example 2

**Problem.** Larger spill volume increases estimated penetration depth when A and Rv are unchanged.

**Solution.** With \(D=V/(AR_v)\), holding footprint area \(A\) and retention term \(R_v\) fixed makes penetration depth directly proportional to spill volume \(V\). A larger spill therefore gives a **larger estimated penetration depth** in this idealization.

---

## 55.3 Sorption, retardation, and contaminant mobility

Sorption slows the dissolved-phase migration of chemicals relative to groundwater under the linear equilibrium model. Larger Kd produces greater retardation.

\[R=1+\frac{\rho_b K_d}{n_e}\]

![FIG-03-55-003: Groundwater and contaminant fronts separated by sorption retardation in a soil column.](../figures/FIG-03-55-003-sorption-retardation-and-contaminant-mobility.png)

### Worked Example 3

**Problem.** If R=5, the idealized contaminant velocity is one-fifth of the groundwater seepage velocity.

**Solution.** Retardation reduces contaminant velocity relative to groundwater: \(v_c=v_s/R\). For \(R=5\), \(v_c=\mathbf{v_s/5}\), so the idealized contaminant front moves at one-fifth the seepage velocity.

---

## 55.4 Site investigation, sampling, and monitoring networks

Sampling locations, depths, media, detection limits, and QA/QC must match the decision being made. More samples do not compensate for a poor conceptual model.

\[\text{data quality objective}\rightarrow\text{sampling design}\rightarrow\text{analysis}\rightarrow\text{conceptual-model update}\]

![FIG-03-55-004: Plan and cross-section of soil borings, monitoring wells, background/upgradient and downgradient locations.](../figures/FIG-03-55-004-site-investigation-sampling-and-monitoring-networks.png)

### Worked Example 4

**Problem.** Monitoring wells should be positioned to characterize background, source, and downgradient plume behavior.

**Solution.** A monitoring network should establish **background/upgradient**, source-area, and **downgradient** conditions, with locations and screened intervals chosen to test the conceptual plume geometry rather than merely filling a regular grid.

---

## 55.5 Pump-and-treat and hydraulic containment

Pump-and-treat uses groundwater extraction to remove dissolved mass and/or control plume migration. Capture-zone design depends on hydrogeology and pumping.

\[\text{extraction}\rightarrow\text{treatment}\rightarrow\text{discharge/reuse}\]

![FIG-03-55-005: Extraction wells, treatment system, clean-water discharge, and capture zone around a plume.](../figures/FIG-03-55-005-pump-and-treat-and-hydraulic-containment.png)

### Worked Example 5

**Problem.** A containment system can reduce downgradient migration even if contaminant mass removal is slow.

**Solution.** Hydraulic containment can control plume migration by changing groundwater gradients and capturing contaminated flow. It may therefore protect downgradient receptors even when contaminant mass removal is slow and cleanup requires long operation.

---

## 55.6 In-situ treatment and monitored natural attenuation

In-situ methods treat contaminants without excavating all media. Options may include bioremediation, chemical oxidation/reduction, air sparging, soil-vapor extraction, or natural attenuation with monitoring.

\[\text{remediation}=f(\text{contaminant, geology, geochemistry, access, time})\]

![FIG-03-55-006: Matrix mapping contaminant/media conditions to representative in-situ remediation approaches.](../figures/FIG-03-55-006-in-situ-treatment-and-monitored-natural-attenuation.png)

### Worked Example 6

**Problem.** An oxygen-limited biodegradable plume may respond to enhanced bioremediation if delivery is feasible.

**Solution.** If biodegradation is feasible but electron acceptor or donor delivery is limiting, enhanced bioremediation can improve reaction conditions. Feasibility still depends on contaminant degradability, hydrogeology, geochemistry, distribution of amendments, and monitoring.

---

## 55.7 Remedy selection, performance monitoring, and closure

Remedy selection balances protectiveness, implementability, time, cost, residual risk, and long-term stewardship. Performance monitoring confirms whether the conceptual model and remedy remain valid.

\[\text{baseline}\rightarrow\text{remedy}\rightarrow\text{monitor}\rightarrow\text{compare to objectives}\]

![FIG-03-55-007: Remediation lifecycle from investigation through remedy selection, construction, monitoring, optimization, and closure.](../figures/FIG-03-55-007-remedy-selection-performance-monitoring-and-closure.png)

### Worked Example 7

**Problem.** A falling concentration trend alone may be insufficient if plume extent continues to expand.

**Solution.** A falling concentration at one well is not sufficient evidence of remedy completion. Plume footprint, mass flux, rebound, daughter products, and downgradient trends must also support the conclusion that objectives are being met.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** A remediation calculation that predicts negative mass or concentration has exceeded the physical bounds of its conceptual model. Recheck source mass, retardation/decay assumptions, extraction rates, and whether rebound or inaccessible mass was omitted.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** For **Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation**, the FE Reference Handbook equation, definitions, and unit convention govern whenever the Handbook supplies the needed relation. The external references in this chapter are used for specification-required learned material involving **vadose/saturated transport, retardation, monitoring networks, hydraulic containment, and groundwater remediation**. If a remembered correlation conflicts with the supplied Handbook equation, use the supplied Handbook relation unless the problem explicitly states a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 11, 14; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required environmental-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects the Handbook and external material into exam-oriented explanations, examples, and checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Fitts, C. R. (2023). *Groundwater Science* (3rd ed.). Elsevier. ISBN 978-0-12-811455-1. Supporting scope: Aquifer properties, Darcy flow, hydraulic head, wells, drawdown, aquifer tests, contaminant transport, and groundwater modeling.
- U.S. Environmental Protection Agency. *Groundwater Technologies*. Superfund technical guidance and information, current online resource. Supporting scope: Groundwater characterization, pump-and-treat, in-situ treatment, monitored natural attenuation, containment, and remediation monitoring.

The external references support only the learned/application portion of the Environmental specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using contaminated-site conceptual model without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using vadose-zone penetration without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using groundwater retardation factor without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental site characterization without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using pump-and-treat remediation without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using in-situ remediation without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using remediation performance without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| contaminated-site conceptual model | Concept developed in §55.1; apply with that section's stated environmental basis and assumptions. |
| vadose-zone penetration | Concept developed in §55.2; apply with that section's stated environmental basis and assumptions. |
| groundwater retardation factor | Concept developed in §55.3; apply with that section's stated environmental basis and assumptions. |
| environmental site characterization | Concept developed in §55.4; apply with that section's stated environmental basis and assumptions. |
| pump-and-treat remediation | Concept developed in §55.5; apply with that section's stated environmental basis and assumptions. |
| in-situ remediation | Concept developed in §55.6; apply with that section's stated environmental basis and assumptions. |
| remediation performance | Concept developed in §55.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **contaminated-site conceptual model** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **vadose-zone penetration** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **groundwater retardation factor** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **environmental site characterization** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **pump-and-treat remediation** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **in-situ remediation** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **remediation performance** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **contaminated-site conceptual model**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **vadose-zone penetration**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **groundwater retardation factor**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental site characterization**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **pump-and-treat remediation**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **in-situ remediation**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **remediation performance**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **contaminated-site conceptual model**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **vadose-zone penetration**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **groundwater retardation factor**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **environmental site characterization**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **pump-and-treat remediation**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **in-situ remediation**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **remediation performance**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **contaminated-site conceptual model**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **vadose-zone penetration**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **contaminated-site conceptual model** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **vadose-zone penetration** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **groundwater retardation factor** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **environmental site characterization** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **pump-and-treat remediation** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **in-situ remediation** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **remediation performance** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **contaminated-site conceptual model**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **vadose-zone penetration**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **groundwater retardation factor**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **environmental site characterization**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **pump-and-treat remediation**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **in-situ remediation**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **remediation performance**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

15. In **Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation**, the control volume or conceptual boundary determines which sources, sinks, transfers, reactions, and receptors belong in the model. For this chapter specifically, check the conceptual site model, source mass, hydrostratigraphy, retardation/decay assumptions, monitoring coverage, and whether remedy performance is evaluated by plume behavior as well as point concentrations.

16. Concentration and loading answer different questions in **Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation**: concentration is mass per volume, while loading is mass per time. Always convert \(Q\) and \(C\) to compatible units before multiplying them.

17. Use the FE Reference Handbook equation and definitions when it supplies the model for **Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation**. The chapter's external references (FITTS, EPA_GW) support learned specification content, not a competing exam formula.

18. A physical check is needed because algebra alone can return impossible environmental states. For this chapter, set sorption \(K_d\) to zero and confirm retardation approaches one; remove the source and verify no new contaminant mass is generated by the transport model.

19. **A.** Section §55.1, **Contaminant source, vadose zone, and saturated-zone conceptual models**, is governed by \(\text{source}\rightarrow\text{release}\rightarrow\text{transport}\rightarrow\text{receptor}\). Use that relation with its own environmental basis and then perform the specific validity check described for §55.1.

20. **A.** Section §55.2, **Vadose-zone penetration and retention**, is governed by \(D=\frac{V}{A R_v}\). Use that relation with its own environmental basis and then perform the specific validity check described for §55.2.

21. **A.** Section §55.3, **Sorption, retardation, and contaminant mobility**, is governed by \(R=1+\frac{\rho_b K_d}{n_e}\). Use that relation with its own environmental basis and then perform the specific validity check described for §55.3.

22. **A.** Section §55.4, **Site investigation, sampling, and monitoring networks**, is governed by \(\text{data quality objective}\rightarrow\text{sampling design}\rightarrow\text{analysis}\rightarrow\text{conceptual-model update}\). Use that relation with its own environmental basis and then perform the specific validity check described for §55.4.

23. **A.** Section §55.5, **Pump-and-treat and hydraulic containment**, is governed by \(\text{extraction}\rightarrow\text{treatment}\rightarrow\text{discharge/reuse}\). Use that relation with its own environmental basis and then perform the specific validity check described for §55.5.

24. **A.** Section §55.6, **In-situ treatment and monitored natural attenuation**, is governed by \(\text{remediation}=f(\text{contaminant, geology, geochemistry, access, time})\). Use that relation with its own environmental basis and then perform the specific validity check described for §55.6.

25. **A.** Section §55.7, **Remedy selection, performance monitoring, and closure**, is governed by \(\text{baseline}\rightarrow\text{remedy}\rightarrow\text{monitor}\rightarrow\text{compare to objectives}\). Use that relation with its own environmental basis and then perform the specific validity check described for §55.7.

26. **A.** An integrated **Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation** solution is acceptable only after the governing balance/model is identified, units are reconciled, and the chapter-specific physical checks are satisfied.

27. **A.** Source ownership is explicit in **Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation**: FE-Handbook-supported material remains tied to the ledger, externally supported content uses FITTS, EPA_GW, and guide synthesis is labeled as supplemental explanation.


---

## Practice Problems

1. A leaking tank above a shallow aquifer can create soil-vapor, soil, and groundwater pathways.

2. Larger spill volume increases estimated penetration depth when A and Rv are unchanged.

3. If R=5, the idealized contaminant velocity is one-fifth of the groundwater seepage velocity.

4. Monitoring wells should be positioned to characterize background, source, and downgradient plume behavior.

5. A containment system can reduce downgradient migration even if contaminant mass removal is slow.

6. An oxygen-limited biodegradable plume may respond to enhanced bioremediation if delivery is feasible.

7. A falling concentration trend alone may be insufficient if plume extent continues to expand.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. **Independent recomputation for §55.1 — Contaminant source, vadose zone, and saturated-zone conceptual models.** Start from the stated givens rather than the worked-example answer. A release from a leaking tank above a shallow aquifer can migrate through the vadose zone, generate soil vapor where volatile constituents are present, contaminate soil, and reach groundwater. The conceptual site model must show each plausible source-pathway-receptor connection separately. As a separate check, confirm the result is consistent with the section's physical interpretation.

2. **Independent recomputation for §55.2 — Vadose-zone penetration and retention.** Start from the stated givens rather than the worked-example answer. With \(D=V/(AR_v)\), holding footprint area \(A\) and retention term \(R_v\) fixed makes penetration depth directly proportional to spill volume \(V\). A larger spill therefore gives a **larger estimated penetration depth** in this idealization. As a separate check, confirm the result is consistent with the section's physical interpretation.

3. **Independent recomputation for §55.3 — Sorption, retardation, and contaminant mobility.** Start from the stated givens rather than the worked-example answer. Retardation reduces contaminant velocity relative to groundwater: \(v_c=v_s/R\). For \(R=5\), \(v_c=\mathbf{v_s/5}\), so the idealized contaminant front moves at one-fifth the seepage velocity. As a separate check, confirm the result is consistent with the section's physical interpretation.

4. **Independent recomputation for §55.4 — Site investigation, sampling, and monitoring networks.** Start from the stated givens rather than the worked-example answer. A monitoring network should establish **background/upgradient**, source-area, and **downgradient** conditions, with locations and screened intervals chosen to test the conceptual plume geometry rather than merely filling a regular grid. As a separate check, confirm the result is consistent with the section's physical interpretation.

5. **Independent recomputation for §55.5 — Pump-and-treat and hydraulic containment.** Start from the stated givens rather than the worked-example answer. Hydraulic containment can control plume migration by changing groundwater gradients and capturing contaminated flow. It may therefore protect downgradient receptors even when contaminant mass removal is slow and cleanup requires long operation. As a separate check, confirm the result is consistent with the section's physical interpretation.

6. **Independent recomputation for §55.6 — In-situ treatment and monitored natural attenuation.** Start from the stated givens rather than the worked-example answer. If biodegradation is feasible but electron acceptor or donor delivery is limiting, enhanced bioremediation can improve reaction conditions. Feasibility still depends on contaminant degradability, hydrogeology, geochemistry, distribution of amendments, and monitoring. As a separate check, confirm the result is consistent with the section's physical interpretation.

7. **Independent recomputation for §55.7 — Remedy selection, performance monitoring, and closure.** Start from the stated givens rather than the worked-example answer. A falling concentration at one well is not sufficient evidence of remedy completion. Plume footprint, mass flux, rebound, daughter products, and downgradient trends must also support the conclusion that objectives are being met. As a separate check, confirm the result is consistent with the section's physical interpretation.

8. For this chapter, check the result against this failure screen: Check the conceptual site model, source mass, hydrostratigraphy, retardation/decay assumptions, monitoring coverage, and whether remedy performance is evaluated by plume behavior as well as point concentrations. A result that violates one of those conditions should be rejected even if the arithmetic is internally consistent.

9. For **Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation**, begin with the FE Environmental specification area and Handbook subsection recorded in the ledger. When the atom is `split_required`, use the reconciled external source set **FITTS, EPA_GW** for the learned portion rather than inventing a Handbook page.

10. A useful limiting case is to set sorption \(K_d\) to zero and confirm retardation approaches one; remove the source and verify no new contaminant mass is generated by the transport model. The simplified case should reduce to the stated physical behavior before the full model is trusted.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 11, 14.

- **contaminated-site conceptual model:** Contaminant source, vadose zone, and saturated-zone conceptual models
- **vadose-zone penetration:** Vadose-zone penetration and retention
- **groundwater retardation factor:** Sorption, retardation, and contaminant mobility
- **environmental site characterization:** Site investigation, sampling, and monitoring networks
- **pump-and-treat remediation:** Pump-and-treat and hydraulic containment
- **in-situ remediation:** In-situ treatment and monitored natural attenuation
- **remediation performance:** Remedy selection, performance monitoring, and closure

---

## What's Next

**Chapter 03-56: Water/Wastewater Characteristics, Loading Rates, and Physical Treatment**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
