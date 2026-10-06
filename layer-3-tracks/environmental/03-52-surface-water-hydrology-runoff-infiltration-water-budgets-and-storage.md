---
chapter: "03-52"
title: "Surface-Water Hydrology — Runoff, Infiltration, Water Budgets, and Storage"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-052-01, ENV-3-052-02, ENV-3-052-03, ENV-3-052-04, ENV-3-052-05, ENV-3-052-06, ENV-3-052-07]
routes: [environmental]
status: drafted
---

# Chapter 03-52: Surface-Water Hydrology — Runoff, Infiltration, Water Budgets, and Storage

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-016-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Surface-Water Hydrology — Runoff, Infiltration, Water Budgets, and Storage**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **52.1** Explain and apply **Watersheds, precipitation, runoff, and hydrologic control volumes**.
* **52.2** Explain and apply **Rainfall intensity, duration, frequency, and time of concentration**.
* **52.3** Explain and apply **Rational Method runoff**.
* **52.4** Explain and apply **NRCS curve-number runoff**.
* **52.5** Explain and apply **Infiltration, evapotranspiration, and soil-moisture storage**.
* **52.6** Explain and apply **Reservoir, detention, and retention storage sizing**.
* **52.7** Explain and apply **Hydrographs and watershed response checks**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 52.1 Watersheds, precipitation, runoff, and hydrologic control volumes

A watershed water budget accounts for precipitation, runoff, groundwater exchange, evapotranspiration, infiltration, and storage on a consistent time basis.

\[P+Q_{in}+Q_g-Q_{out}-ET-I=\Delta S\]

![FIG-03-52-001: Watershed with precipitation, infiltration, evapotranspiration, surface runoff, groundwater, and storage.](../figures/FIG-03-52-001-watersheds-precipitation-runoff-and-hydrologic-control-volumes.png)

### Worked Example 1

**Problem.** If inputs exceed outputs by 20 mm over a period, storage rises by 20 mm.

**Solution.** Apply the relation and environmental model in §52.1; then verify units, boundary conditions, and physical limits.

---

## 52.2 Rainfall intensity, duration, frequency, and time of concentration

Design runoff depends on storm intensity and duration relative to watershed response. Time of concentration is a key link between rainfall and peak runoff methods.

\[i=i(T_r,t_d)\]

![FIG-03-52-002: IDF curves with time of concentration and selected design intensity.](../figures/FIG-03-52-002-rainfall-intensity-duration-frequency-and-time-of-concentration.png)

### Worked Example 2

**Problem.** For Rational Method design, intensity is commonly selected at a duration tied to time of concentration.

**Solution.** Apply the relation and environmental model in §52.2; then verify units, boundary conditions, and physical limits.

---

## 52.3 Rational Method runoff

The Rational Method estimates peak flow from runoff coefficient, rainfall intensity, and area for suitable small watersheds.

\[Q=CIA\]

![FIG-03-52-003: Developed watershed draining to one outlet with C, I, A, and peak Q.](../figures/FIG-03-52-003-rational-method-runoff.png)

### Worked Example 3

**Problem.** C=0.5, I=4 in/hr, A=20 acres gives 40 cfs in the common U.S. form.

**Solution.** Apply the relation and environmental model in §52.3; then verify units, boundary conditions, and physical limits.

---

## 52.4 NRCS curve-number runoff

The curve-number method relates storm depth and watershed condition to runoff depth. Apply the initial-abstraction threshold before using the runoff expression.

\[Q=\frac{(P-0.2S)^2}{P+0.8S},\qquad S=\frac{1000}{CN}-10\]

![FIG-03-52-004: Rainfall-runoff curves for several CN values with initial abstraction region.](../figures/FIG-03-52-004-nrcs-curve-number-runoff.png)

### Worked Example 4

**Problem.** Higher CN generally produces more runoff from the same rainfall depth.

**Solution.** Apply the relation and environmental model in §52.4; then verify units, boundary conditions, and physical limits.

---

## 52.5 Infiltration, evapotranspiration, and soil-moisture storage

Infiltration, interception, depression storage, and evapotranspiration reduce water available for runoff. The time scale determines which loss terms matter.

\[\text{effective rainfall}=P-\text{abstractions}\]

![FIG-03-52-005: Rainfall hyetograph partitioned into infiltration/abstraction and effective rainfall.](../figures/FIG-03-52-005-infiltration-evapotranspiration-and-soil-moisture-storage.png)

### Worked Example 5

**Problem.** A storm with 50 mm rainfall and 20 mm total abstractions yields 30 mm effective rainfall.

**Solution.** Apply the relation and environmental model in §52.5; then verify units, boundary conditions, and physical limits.

---

## 52.6 Reservoir, detention, and retention storage sizing

Storage is the cumulative difference between inflow and outflow. Detention temporarily stores water and releases it; retention may maintain a permanent pool or retain runoff depending on design context.

\[\Delta S=\int(I-O)\,dt\]

![FIG-03-52-006: Inflow and outflow hydrographs with shaded storage volume and basin stage.](../figures/FIG-03-52-006-reservoir-detention-and-retention-storage-sizing.png)

### Worked Example 6

**Problem.** Maximum required storage occurs at the maximum cumulative inflow-minus-outflow difference.

**Solution.** Apply the relation and environmental model in §52.6; then verify units, boundary conditions, and physical limits.

---

## 52.7 Hydrographs and watershed response checks

A hydrograph contains both timing and volume information. Peak discharge alone cannot establish runoff volume or storage need.

\[\text{runoff volume}=\int Q(t)\,dt\]

![FIG-03-52-007: Two hydrographs with equal volume but different peak and duration, plus rainfall hyetograph.](../figures/FIG-03-52-007-hydrographs-and-watershed-response-checks.png)

### Worked Example 7

**Problem.** A narrow high peak and a broad lower peak can have the same runoff volume.

**Solution.** Apply the relation and environmental model in §52.7; then verify units, boundary conditions, and physical limits.

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

**Using environmental watershed without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using design storm hydrology without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental Rational Method without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental curve-number method without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using surface-water losses without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using surface-water storage sizing without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental runoff hydrograph without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| environmental watershed | Concept developed in §52.1; apply with that section's stated environmental basis and assumptions. |
| design storm hydrology | Concept developed in §52.2; apply with that section's stated environmental basis and assumptions. |
| environmental Rational Method | Concept developed in §52.3; apply with that section's stated environmental basis and assumptions. |
| environmental curve-number method | Concept developed in §52.4; apply with that section's stated environmental basis and assumptions. |
| surface-water losses | Concept developed in §52.5; apply with that section's stated environmental basis and assumptions. |
| surface-water storage sizing | Concept developed in §52.6; apply with that section's stated environmental basis and assumptions. |
| environmental runoff hydrograph | Concept developed in §52.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **environmental watershed** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **design storm hydrology** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **environmental Rational Method** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **environmental curve-number method** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **surface-water losses** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **surface-water storage sizing** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **environmental runoff hydrograph** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental watershed**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **design storm hydrology**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental Rational Method**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental curve-number method**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **surface-water losses**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **surface-water storage sizing**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental runoff hydrograph**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **environmental watershed**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **design storm hydrology**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **environmental Rational Method**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **environmental curve-number method**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **surface-water losses**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **surface-water storage sizing**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **environmental runoff hydrograph**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **environmental watershed**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **design storm hydrology**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **environmental watershed** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **design storm hydrology** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **environmental Rational Method** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **environmental curve-number method** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **surface-water losses** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **surface-water storage sizing** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **environmental runoff hydrograph** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **environmental watershed**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **design storm hydrology**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **environmental Rational Method**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **environmental curve-number method**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **surface-water losses**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **surface-water storage sizing**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **environmental runoff hydrograph**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

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

1. If inputs exceed outputs by 20 mm over a period, storage rises by 20 mm.

2. For Rational Method design, intensity is commonly selected at a duration tied to time of concentration.

3. C=0.5, I=4 in/hr, A=20 acres gives 40 cfs in the common U.S. form.

4. Higher CN generally produces more runoff from the same rainfall depth.

5. A storm with 50 mm rainfall and 20 mm total abstractions yields 30 mm effective rainfall.

6. Maximum required storage occurs at the maximum cumulative inflow-minus-outflow difference.

7. A narrow high peak and a broad lower peak can have the same runoff volume.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §52.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §52.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §52.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §52.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §52.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §52.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §52.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 10, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 10.

- **environmental watershed:** Watersheds, precipitation, runoff, and hydrologic control volumes
- **design storm hydrology:** Rainfall intensity, duration, frequency, and time of concentration
- **environmental Rational Method:** Rational Method runoff
- **environmental curve-number method:** NRCS curve-number runoff
- **surface-water losses:** Infiltration, evapotranspiration, and soil-moisture storage
- **surface-water storage sizing:** Reservoir, detention, and retention storage sizing
- **environmental runoff hydrograph:** Hydrographs and watershed response checks

---

## What's Next

**Chapter 03-53: Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
