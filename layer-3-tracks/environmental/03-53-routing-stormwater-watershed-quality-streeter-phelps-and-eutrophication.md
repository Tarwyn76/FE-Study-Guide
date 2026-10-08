---
chapter: "03-53"
title: "Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-053-01, ENV-3-053-02, ENV-3-053-03, ENV-3-053-04, ENV-3-053-05, ENV-3-053-06, ENV-3-053-07]
routes: [environmental]
status: drafted
---

# Chapter 03-53: Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** ENV-3-052-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **53.1** Explain and apply **Reservoir routing by continuity**.
* **53.2** Explain and apply **Channel routing concepts**.
* **53.3** Explain and apply **Stormwater pollutant loading and best-management concepts**.
* **53.4** Explain and apply **Erosion, sediment transport, and channel stability concepts**.
* **53.5** Explain and apply **BOD exertion and stream oxygen demand**.
* **53.6** Explain and apply **Streeter–Phelps dissolved-oxygen sag**.
* **53.7** Explain and apply **Eutrophication, nutrients, and receiving-water response**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 53.1 Reservoir routing by continuity

Routing translates an inflow hydrograph through storage and outlet behavior to produce an outflow hydrograph. Storage and outflow are linked through stage relationships.

\[\frac{dS}{dt}=I-O\]

![FIG-03-53-001: Level-pool reservoir with inflow/outflow hydrographs and stage-storage-outflow curves.](../figures/FIG-03-53-001-reservoir-routing-by-continuity.png)

### Worked Example 1

**Problem.** When inflow exceeds outflow, reservoir storage increases.

**Solution.** Reservoir continuity is \(dS/dt=I-O\). Whenever \(I>O\), the derivative is positive, so **storage increases**; when outflow exceeds inflow, storage decreases.

---

## 53.2 Channel routing concepts

Channel routing accounts for travel time and temporary channel storage. The exact method may be supplied by the problem; preserve mass continuity regardless of method.

\[\text{inflow hydrograph}\rightarrow\text{translation+attenuation}\rightarrow\text{outflow hydrograph}\]

![FIG-03-53-002: Upstream and downstream hydrographs along a river reach showing translation and attenuation.](../figures/FIG-03-53-002-channel-routing-concepts.png)

### Worked Example 2

**Problem.** A routed downstream hydrograph generally peaks later than the upstream hydrograph.

**Solution.** Routing redistributes a hydrograph in time and usually attenuates it. Storage and travel time cause the downstream peak to occur **later**, and often lower, than the corresponding upstream peak.

---

## 53.3 Stormwater pollutant loading and best-management concepts

Stormwater quality depends on runoff volume, concentration, land use, sediment transport, and control practices. Flow reduction and pollutant removal are related but not identical objectives.

\[\dot m=QC\]

![FIG-03-53-003: Urban drainage system with source controls, swale, forebay, detention, wetland, and receiving water.](../figures/FIG-03-53-003-stormwater-pollutant-loading-and-best-management-concepts.png)

### Worked Example 3

**Problem.** At 5 m³/s and 2 mg/L, instantaneous pollutant load is 10 g/s.

**Solution.** \(\dot m=QC=(5\ {\rm m^3/s})(2\ {\rm mg/L})\). Since \(1\ {\rm mg/L}=1\ {\rm g/m^3}\), the concentration is \(2\ {\rm g/m^3}\), giving \(\dot m=\mathbf{10\ g/s}\).

---

## 53.4 Erosion, sediment transport, and channel stability concepts

Erosion and channel stability depend on hydraulic forcing and material resistance. Stabilization may reduce velocity, protect surfaces, or restore vegetation.

\[\text{erosion risk}=f(\text{flow shear, soil, slope, cover, duration})\]

![FIG-03-53-004: Watershed slope and stream reach showing erosion sources, sediment transport, deposition, and stabilization measures.](../figures/FIG-03-53-004-erosion-sediment-transport-and-channel-stability-concepts.png)

### Worked Example 4

**Problem.** Increasing bare-soil exposure generally increases erosion risk under the same runoff.

**Solution.** Removing protective cover exposes soil to raindrop impact and flowing-water shear. With the same slope and runoff forcing, greater bare-soil exposure therefore generally **increases erosion and sediment-yield risk**.

---

## 53.5 BOD exertion and stream oxygen demand

BOD exertion describes oxygen demand realized over time as biodegradable material decays. Ultimate BOD exceeds the BOD exerted at finite time.

\[\mathrm{BOD}_t=L_0(1-e^{-kt})\]

![FIG-03-53-005: BOD exerted and remaining ultimate BOD versus time.](../figures/FIG-03-53-005-bod-exertion-and-stream-oxygen-demand.png)

### Worked Example 5

**Problem.** At t=0, exerted BOD is zero in the ideal first-order model.

**Solution.** \(\mathrm{BOD}_t=L_0(1-e^{-kt})\). At \(t=0\ {\rm day}\), \(e^0=1\), so \(\mathrm{BOD}_0=L_0(1-1)=\mathbf{0\ mg/L}\) exerted BOD: no ultimate demand has yet been exerted at the initial instant.

---

## 53.6 Streeter–Phelps dissolved-oxygen sag

The Streeter–Phelps model balances deoxygenation and reaeration to estimate dissolved-oxygen deficit downstream of a waste discharge.

\[\mathrm{DO}=\mathrm{DO}_{sat}-D\]

![FIG-03-53-006: River downstream distance/time with BOD decay, oxygen deficit, DO sag, and critical point.](../figures/FIG-03-53-006-streeter-phelps-dissolved-oxygen-sag.png)

### Worked Example 6

**Problem.** The critical point occurs where the oxygen deficit reaches its maximum.

**Solution.** In a Streeter-Phelps oxygen-sag calculation, the critical location/time corresponds to the **maximum oxygen deficit**, so \(dD/dt=0\) at the critical point; equivalently, the deoxygenation and reaeration contributions balance there.

---

## 53.7 Eutrophication, nutrients, and receiving-water response

Excess nutrient loading can stimulate algal productivity, alter clarity, and contribute to oxygen depletion when biomass decays. Hydrology, light, temperature, and nutrient limitation all influence response.

\[\text{nutrient loading}\uparrow\Rightarrow\text{productivity/oxygen impacts may increase}\]

![FIG-03-53-007: Nutrient loading, algal growth, settling, decomposition, oxygen depletion, and internal recycling cycle.](../figures/FIG-03-53-007-eutrophication-nutrients-and-receiving-water-response.png)

### Worked Example 7

**Problem.** Reducing a limiting nutrient can reduce eutrophication pressure even when total water volume is unchanged.

**Solution.** Eutrophication responds strongly to nutrient loading. If a nutrient is limiting, reducing its load can reduce algal productivity and associated oxygen impacts even though the receiving-water volume itself is unchanged.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** A negative pollutant concentration or impossible oxygen result indicates a balance/kinetics problem. Check the routing interval, reaction signs, saturation limit, deoxygenation/re-aeration terms, and units before accepting the result.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** For **Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication**, the FE Reference Handbook equation, definitions, and unit convention govern whenever the Handbook supplies the needed relation. The external references in this chapter are used for specification-required learned material involving **reservoir/channel routing, watershed loading, BOD/DO response, and eutrophication**. If a remembered correlation conflicts with the supplied Handbook equation, use the supplied Handbook relation unless the problem explicitly states a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 10; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required environmental-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects the Handbook and external material into exam-oriented explanations, examples, and checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- U.S. Army Corps of Engineers, Hydrologic Engineering Center. *HEC-HMS Technical Reference Manual* (CPD-74B), current online edition. Supporting scope: Precipitation-runoff transformation, loss methods, hydrographs, channel/reservoir routing, and hydrologic-model assumptions.
- Chapra, S. C. (1997). *Surface Water-Quality Modeling*. McGraw-Hill. ISBN 978-0-07-115242-6. Supporting scope: Surface-water mass balances, dissolved oxygen, Streeter-Phelps behavior, eutrophication, kinetics, and contaminant fate.
- Mihelcic, J. R., & Zimmerman, J. B. (2021). *Environmental Engineering: Fundamentals, Sustainability, Design* (3rd ed.). Wiley. ISBN 978-1-119-60445-7. Supporting scope: Environmental measurements, chemistry, physical processes, biology, risk, water quantity/quality, water treatment, wastewater/stormwater, solid waste, and air quality.

The external references support only the learned/application portion of the Environmental specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using environmental reservoir routing without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental channel routing without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using stormwater quality loading without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using watershed erosion control without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using BOD exertion without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using Streeter-Phelps oxygen sag without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using eutrophication without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| environmental reservoir routing | Concept developed in §53.1; apply with that section's stated environmental basis and assumptions. |
| environmental channel routing | Concept developed in §53.2; apply with that section's stated environmental basis and assumptions. |
| stormwater quality loading | Concept developed in §53.3; apply with that section's stated environmental basis and assumptions. |
| watershed erosion control | Concept developed in §53.4; apply with that section's stated environmental basis and assumptions. |
| BOD exertion | Concept developed in §53.5; apply with that section's stated environmental basis and assumptions. |
| Streeter-Phelps oxygen sag | Concept developed in §53.6; apply with that section's stated environmental basis and assumptions. |
| eutrophication | Concept developed in §53.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **environmental reservoir routing** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **environmental channel routing** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **stormwater quality loading** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **watershed erosion control** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **BOD exertion** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **Streeter-Phelps oxygen sag** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **eutrophication** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental reservoir routing**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental channel routing**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **stormwater quality loading**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **watershed erosion control**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **BOD exertion**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **Streeter-Phelps oxygen sag**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **eutrophication**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **environmental reservoir routing**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **environmental channel routing**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **stormwater quality loading**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **watershed erosion control**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **BOD exertion**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **Streeter-Phelps oxygen sag**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **eutrophication**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **environmental reservoir routing**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **environmental channel routing**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **environmental reservoir routing** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **environmental channel routing** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **stormwater quality loading** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **watershed erosion control** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **BOD exertion** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **Streeter-Phelps oxygen sag** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **eutrophication** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **environmental reservoir routing**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **environmental channel routing**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **stormwater quality loading**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **watershed erosion control**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **BOD exertion**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **Streeter-Phelps oxygen sag**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **eutrophication**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

15. In **Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication**, the control volume or conceptual boundary determines which sources, sinks, transfers, reactions, and receptors belong in the model. For this chapter specifically, close continuity through each routing step, keep mass loading distinct from concentration, enforce nonnegative do/bod quantities, and test whether nutrient/erosion assumptions match the receiving system.

16. Concentration and loading answer different questions in **Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication**: concentration is mass per volume, while loading is mass per time. Always convert \(Q\) and \(C\) to compatible units before multiplying them.

17. Use the FE Reference Handbook equation and definitions when it supplies the model for **Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication**. The chapter's external references (HECHMS, CHAPRA, MIHELCIC) support learned specification content, not a competing exam formula.

18. A physical check is needed because algebra alone can return impossible environmental states. For this chapter, set \(I=O\) and confirm reservoir storage is constant; set \(t=0\) and confirm exerted first-order BOD is zero.

19. **A.** Section §53.1, **Reservoir routing by continuity**, is governed by \(\frac{dS}{dt}=I-O\). Use that relation with its own environmental basis and then perform the specific validity check described for §53.1.

20. **A.** Section §53.2, **Channel routing concepts**, is governed by \(\text{inflow hydrograph}\rightarrow\text{translation+attenuation}\rightarrow\text{outflow hydrograph}\). Use that relation with its own environmental basis and then perform the specific validity check described for §53.2.

21. **A.** Section §53.3, **Stormwater pollutant loading and best-management concepts**, is governed by \(\dot m=QC\). Use that relation with its own environmental basis and then perform the specific validity check described for §53.3.

22. **A.** Section §53.4, **Erosion, sediment transport, and channel stability concepts**, is governed by \(\text{erosion risk}=f(\text{flow shear, soil, slope, cover, duration})\). Use that relation with its own environmental basis and then perform the specific validity check described for §53.4.

23. **A.** Section §53.5, **BOD exertion and stream oxygen demand**, is governed by \(\mathrm{BOD}_t=L_0(1-e^{-kt})\). Use that relation with its own environmental basis and then perform the specific validity check described for §53.5.

24. **A.** Section §53.6, **Streeter–Phelps dissolved-oxygen sag**, is governed by \(\mathrm{DO}=\mathrm{DO}_{sat}-D\). Use that relation with its own environmental basis and then perform the specific validity check described for §53.6.

25. **A.** Section §53.7, **Eutrophication, nutrients, and receiving-water response**, is governed by \(\text{nutrient loading}\uparrow\Rightarrow\text{productivity/oxygen impacts may increase}\). Use that relation with its own environmental basis and then perform the specific validity check described for §53.7.

26. **A.** An integrated **Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication** solution is acceptable only after the governing balance/model is identified, units are reconciled, and the chapter-specific physical checks are satisfied.

27. **A.** Source ownership is explicit in **Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication**: FE-Handbook-supported material remains tied to the ledger, externally supported content uses HECHMS, CHAPRA, MIHELCIC, and guide synthesis is labeled as supplemental explanation.


---

## Practice Problems

1. When inflow exceeds outflow, reservoir storage increases.

2. A routed downstream hydrograph generally peaks later than the upstream hydrograph.

3. At 5 m³/s and 2 mg/L, instantaneous pollutant load is 10 g/s.

4. Increasing bare-soil exposure generally increases erosion risk under the same runoff.

5. At t=0, exerted BOD is zero in the ideal first-order model.

6. The critical point occurs where the oxygen deficit reaches its maximum.

7. Reducing a limiting nutrient can reduce eutrophication pressure even when total water volume is unchanged.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. **Independent recomputation for §53.1 — Reservoir routing by continuity.** Start from the stated givens rather than the worked-example answer. Reservoir continuity is \(dS/dt=I-O\). Whenever \(I>O\), the derivative is positive, so **storage increases**; when outflow exceeds inflow, storage decreases. As a separate check, confirm the result is consistent with the section's physical interpretation.

2. **Independent recomputation for §53.2 — Channel routing concepts.** Start from the stated givens rather than the worked-example answer. Routing redistributes a hydrograph in time and usually attenuates it. Storage and travel time cause the downstream peak to occur **later**, and often lower, than the corresponding upstream peak. As a separate check, confirm the result is consistent with the section's physical interpretation.

3. **Independent recomputation for §53.3 — Stormwater pollutant loading and best-management concepts.** Start from the stated givens rather than the worked-example answer. \(\dot m=QC=(5\ {\rm m^3/s})(2\ {\rm mg/L})\). Since \(1\ {\rm mg/L}=1\ {\rm g/m^3}\), the concentration is \(2\ {\rm g/m^3}\), giving \(\dot m=\mathbf{10\ g/s}\). As a separate check, confirm the result is consistent with the section's physical interpretation.

4. **Independent recomputation for §53.4 — Erosion, sediment transport, and channel stability concepts.** Start from the stated givens rather than the worked-example answer. Removing protective cover exposes soil to raindrop impact and flowing-water shear. With the same slope and runoff forcing, greater bare-soil exposure therefore generally **increases erosion and sediment-yield risk**. As a separate check, confirm the result is consistent with the section's physical interpretation.

5. **Independent recomputation for §53.5 — BOD exertion and stream oxygen demand.** Start from the stated givens rather than the worked-example answer. \(\mathrm{BOD}_t=L_0(1-e^{-kt})\). At \(t=0\), \(e^0=1\), so \(\mathrm{BOD}_0=L_0(1-1)=\mathbf{0}\): no ultimate demand has yet been exerted at the initial instant. As a separate check, confirm the result is consistent with the section's physical interpretation.

6. **Independent recomputation for §53.6 — Streeter–Phelps dissolved-oxygen sag.** Start from the stated givens rather than the worked-example answer. In a Streeter-Phelps oxygen-sag calculation, the critical location/time corresponds to the **maximum oxygen deficit**, so \(dD/dt=0\) at the critical point; equivalently, the deoxygenation and reaeration contributions balance there. As a separate check, confirm the result is consistent with the section's physical interpretation.

7. **Independent recomputation for §53.7 — Eutrophication, nutrients, and receiving-water response.** Start from the stated givens rather than the worked-example answer. Eutrophication responds strongly to nutrient loading. If a nutrient is limiting, reducing its load can reduce algal productivity and associated oxygen impacts even though the receiving-water volume itself is unchanged. As a separate check, confirm the result is consistent with the section's physical interpretation.

8. For this chapter, check the result against this failure screen: Close continuity through each routing step, keep mass loading distinct from concentration, enforce nonnegative DO/BOD quantities, and test whether nutrient/erosion assumptions match the receiving system. A result that violates one of those conditions should be rejected even if the arithmetic is internally consistent.

9. For **Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication**, begin with the FE Environmental specification area and Handbook subsection recorded in the ledger. When the atom is `split_required`, use the reconciled external source set **HECHMS, CHAPRA, MIHELCIC** for the learned portion rather than inventing a Handbook page.

10. A useful limiting case is to set \(I=O\) and confirm reservoir storage is constant; set \(t=0\) and confirm exerted first-order BOD is zero. The simplified case should reduce to the stated physical behavior before the full model is trusted.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 10.

- **environmental reservoir routing:** Reservoir routing by continuity
- **environmental channel routing:** Channel routing concepts
- **stormwater quality loading:** Stormwater pollutant loading and best-management concepts
- **watershed erosion control:** Erosion, sediment transport, and channel stability concepts
- **BOD exertion:** BOD exertion and stream oxygen demand
- **Streeter-Phelps oxygen sag:** Streeter–Phelps dissolved-oxygen sag
- **eutrophication:** Eutrophication, nutrients, and receiving-water response

---

## What's Next

**Chapter 03-54: Groundwater Flow, Aquifer Tests, Wells, and Drawdown**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
