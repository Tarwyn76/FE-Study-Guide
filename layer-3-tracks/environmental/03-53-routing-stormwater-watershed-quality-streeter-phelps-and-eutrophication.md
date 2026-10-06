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

**Solution.** Apply the relation and environmental model in §53.1; then verify units, boundary conditions, and physical limits.

---

## 53.2 Channel routing concepts

Channel routing accounts for travel time and temporary channel storage. The exact method may be supplied by the problem; preserve mass continuity regardless of method.

\[\text{inflow hydrograph}\rightarrow\text{translation+attenuation}\rightarrow\text{outflow hydrograph}\]

![FIG-03-53-002: Upstream and downstream hydrographs along a river reach showing translation and attenuation.](../figures/FIG-03-53-002-channel-routing-concepts.png)

### Worked Example 2

**Problem.** A routed downstream hydrograph generally peaks later than the upstream hydrograph.

**Solution.** Apply the relation and environmental model in §53.2; then verify units, boundary conditions, and physical limits.

---

## 53.3 Stormwater pollutant loading and best-management concepts

Stormwater quality depends on runoff volume, concentration, land use, sediment transport, and control practices. Flow reduction and pollutant removal are related but not identical objectives.

\[\dot m=QC\]

![FIG-03-53-003: Urban drainage system with source controls, swale, forebay, detention, wetland, and receiving water.](../figures/FIG-03-53-003-stormwater-pollutant-loading-and-best-management-concepts.png)

### Worked Example 3

**Problem.** At 5 m³/s and 2 mg/L, instantaneous pollutant load is 10 g/s.

**Solution.** Apply the relation and environmental model in §53.3; then verify units, boundary conditions, and physical limits.

---

## 53.4 Erosion, sediment transport, and channel stability concepts

Erosion and channel stability depend on hydraulic forcing and material resistance. Stabilization may reduce velocity, protect surfaces, or restore vegetation.

\[\text{erosion risk}=f(\text{flow shear, soil, slope, cover, duration})\]

![FIG-03-53-004: Watershed slope and stream reach showing erosion sources, sediment transport, deposition, and stabilization measures.](../figures/FIG-03-53-004-erosion-sediment-transport-and-channel-stability-concepts.png)

### Worked Example 4

**Problem.** Increasing bare-soil exposure generally increases erosion risk under the same runoff.

**Solution.** Apply the relation and environmental model in §53.4; then verify units, boundary conditions, and physical limits.

---

## 53.5 BOD exertion and stream oxygen demand

BOD exertion describes oxygen demand realized over time as biodegradable material decays. Ultimate BOD exceeds the BOD exerted at finite time.

\[\mathrm{BOD}_t=L_0(1-e^{-kt})\]

![FIG-03-53-005: BOD exerted and remaining ultimate BOD versus time.](../figures/FIG-03-53-005-bod-exertion-and-stream-oxygen-demand.png)

### Worked Example 5

**Problem.** At t=0, exerted BOD is zero in the ideal first-order model.

**Solution.** Apply the relation and environmental model in §53.5; then verify units, boundary conditions, and physical limits.

---

## 53.6 Streeter–Phelps dissolved-oxygen sag

The Streeter–Phelps model balances deoxygenation and reaeration to estimate dissolved-oxygen deficit downstream of a waste discharge.

\[\mathrm{DO}=\mathrm{DO}_{sat}-D\]

![FIG-03-53-006: River downstream distance/time with BOD decay, oxygen deficit, DO sag, and critical point.](../figures/FIG-03-53-006-streeter-phelps-dissolved-oxygen-sag.png)

### Worked Example 6

**Problem.** The critical point occurs where the oxygen deficit reaches its maximum.

**Solution.** Apply the relation and environmental model in §53.6; then verify units, boundary conditions, and physical limits.

---

## 53.7 Eutrophication, nutrients, and receiving-water response

Excess nutrient loading can stimulate algal productivity, alter clarity, and contribute to oxygen depletion when biomass decays. Hydrology, light, temperature, and nutrient limitation all influence response.

\[\text{nutrient loading}\uparrow\Rightarrow\text{productivity/oxygen impacts may increase}\]

![FIG-03-53-007: Nutrient loading, algal growth, settling, decomposition, oxygen depletion, and internal recycling cycle.](../figures/FIG-03-53-007-eutrophication-nutrients-and-receiving-water-response.png)

### Worked Example 7

**Problem.** Reducing a limiting nutrient can reduce eutrophication pressure even when total water volume is unchanged.

**Solution.** Apply the relation and environmental model in §53.7; then verify units, boundary conditions, and physical limits.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** The algebra or model assumptions are invalid for that condition. Recheck the balance, reaction/order assumptions, time basis, units, and any zero-concentration limiting condition.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** Use the Handbook relation and its definitions unless the problem explicitly supplies a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 10; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** Some Environmental specification topics are directly tabulated in the Handbook, while others require learned engineering knowledge. The chapter keeps those two categories separate.

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

15. The boundary determines what enters, leaves, accumulates, reacts, or transfers between media. Without it, terms are easily omitted or double counted.

16. Concentration is mass per volume; loading is mass per time. A low concentration at very high flow can still create a large load.

17. The FE Handbook is the supplied exam reference. Its variable definitions and unit conventions should govern unless the problem explicitly provides another relation.

18. A mass/energy balance and physical check can reveal impossible signs, removal above 100%, negative concentrations, unrealistic flows, or model misuse.

19. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

20. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

21. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

22. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

23. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

24. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

25. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

26. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

27. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.


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

1. Use §53.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §53.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §53.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §53.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §53.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §53.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §53.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 10, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

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
