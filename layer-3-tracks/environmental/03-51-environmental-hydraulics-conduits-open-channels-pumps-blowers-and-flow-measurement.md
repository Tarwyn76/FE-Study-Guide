---
chapter: "03-51"
title: "Environmental Hydraulics — Conduits, Open Channels, Pumps, Blowers, and Flow Measurement"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-051-01, ENV-3-051-02, ENV-3-051-03, ENV-3-051-04, ENV-3-051-05, ENV-3-051-06, ENV-3-051-07]
routes: [environmental]
status: drafted
---

# Chapter 03-51: Environmental Hydraulics — Conduits, Open Channels, Pumps, Blowers, and Flow Measurement

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** FLUID-2D-044-07 · FLUID-2D-046-06

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Environmental Hydraulics — Conduits, Open Channels, Pumps, Blowers, and Flow Measurement**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **51.1** Explain and apply **Fluid statics and environmental pressure calculations**.
* **51.2** Explain and apply **Closed conduits and Darcy-Weisbach loss**.
* **51.3** Explain and apply **Hazen-Williams and water-system sizing**.
* **51.4** Explain and apply **Open-channel flow and Manning equation**.
* **51.5** Explain and apply **Pumps, operating points, and efficiency**.
* **51.6** Explain and apply **Blowers and gas-handling power**.
* **51.7** Explain and apply **Weirs, orifices, flumes, and environmental flow measurement**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 51.1 Fluid statics and environmental pressure calculations

Pressure in tanks, basins, pipes, and treatment vessels follows hydrostatic principles when fluid acceleration is negligible.

\[p=\gamma h\]

![FIG-03-51-001: Treatment basin with pressure distribution, free surface, and force on a submerged gate.](../figures/FIG-03-51-001-fluid-statics-and-environmental-pressure-calculations.png)

### Worked Example 1

**Problem.** 10 m of water head corresponds to about 98.1 kPa gauge pressure.

**Solution.** Apply the relation and environmental model in §51.1; then verify units, boundary conditions, and physical limits.

---

## 51.2 Closed conduits and Darcy-Weisbach loss

Environmental pipe systems combine continuity, energy, friction, and minor losses. Verify Darcy versus Fanning friction factor conventions.

\[h_f=f\frac{L}{D}\frac{V^2}{2g}\]

![FIG-03-51-002: Water/wastewater force main with fittings and HGL/EGL head-loss profile.](../figures/FIG-03-51-002-closed-conduits-and-darcy-weisbach-loss.png)

### Worked Example 2

**Problem.** Doubling velocity increases Darcy-Weisbach loss by approximately four if f is unchanged.

**Solution.** Apply the relation and environmental model in §51.2; then verify units, boundary conditions, and physical limits.

---

## 51.3 Hazen-Williams and water-system sizing

Hazen-Williams is frequently used for water conveyance. Use the Handbook's unit-specific constant and do not mix SI and US customary forms.

\[h_f\propto \frac{LQ^{1.852}}{C^{1.852}D^{4.87}}\]

![FIG-03-51-003: Head-loss curves versus flow for several pipe diameters and C values.](../figures/FIG-03-51-003-hazen-williams-and-water-system-sizing.png)

### Worked Example 3

**Problem.** Increasing diameter substantially reduces head loss for fixed flow.

**Solution.** Apply the relation and environmental model in §51.3; then verify units, boundary conditions, and physical limits.

---

## 51.4 Open-channel flow and Manning equation

Open channels in treatment and stormwater systems are commonly analyzed with Manning's equation under near-uniform conditions.

\[Q=\frac{1}{n}AR^{2/3}S^{1/2}\quad\text{SI}\]

![FIG-03-51-004: Trapezoidal channel with A, wetted perimeter, hydraulic radius, slope, and flow depth.](../figures/FIG-03-51-004-open-channel-flow-and-manning-equation.png)

### Worked Example 4

**Problem.** For fixed geometry and roughness, discharge scales with square root of slope.

**Solution.** Apply the relation and environmental model in §51.4; then verify units, boundary conditions, and physical limits.

---

## 51.5 Pumps, operating points, and efficiency

Pump selection requires matching the pump curve to the system curve. Parallel and series arrangements alter flow/head capability differently.

\[P_{in}=\frac{\gamma QH}{\eta}\]

![FIG-03-51-005: Pump and system curves plus series and parallel pump combinations.](../figures/FIG-03-51-005-pumps-operating-points-and-efficiency.png)

### Worked Example 5

**Problem.** Two identical pumps in series ideally add head at the same flow; in parallel they add flow at similar head.

**Solution.** Apply the relation and environmental model in §51.5; then verify units, boundary conditions, and physical limits.

---

## 51.6 Blowers and gas-handling power

Blowers supply air for aeration, stripping, combustion, and gas handling. Compressibility may matter at larger pressure ratios; use the model provided by the problem.

\[P\approx \frac{Q\,\Delta p}{\eta}\]

![FIG-03-51-006: Aeration blower feeding diffusers with inlet/outlet pressure and efficiency labels.](../figures/FIG-03-51-006-blowers-and-gas-handling-power.png)

### Worked Example 6

**Problem.** At the same flow and pressure rise, lower efficiency requires higher shaft power.

**Solution.** Apply the relation and environmental model in §51.6; then verify units, boundary conditions, and physical limits.

---

## 51.7 Weirs, orifices, flumes, and environmental flow measurement

Environmental flow measurement commonly uses head-discharge devices. The coefficient and exponent depend on device geometry; use the supplied/Handbook relation.

\[Q=C\,H^n\]

![FIG-03-51-007: Rectangular weir, V-notch weir, orifice, and Parshall-flume style flow measurement sketches.](../figures/FIG-03-51-007-weirs-orifices-flumes-and-environmental-flow-measurement.png)

### Worked Example 7

**Problem.** For a rectangular-weir form with exponent 3/2, doubling head multiplies flow by 2^(3/2).

**Solution.** Apply the relation and environmental model in §51.7; then verify units, boundary conditions, and physical limits.

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

Primary source basis: **FE Environmental specification Area(s) 8; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** Some Environmental specification topics are directly tabulated in the Handbook, while others require learned engineering knowledge. The chapter keeps those two categories separate.

---

## Where This Goes Wrong

**Using environmental fluid statics without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental pipe head loss without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental Hazen-Williams relation without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental Manning flow without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental pump operating point without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental blower without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental flow measurement without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| environmental fluid statics | Concept developed in §51.1; apply with that section's stated environmental basis and assumptions. |
| environmental pipe head loss | Concept developed in §51.2; apply with that section's stated environmental basis and assumptions. |
| environmental Hazen-Williams relation | Concept developed in §51.3; apply with that section's stated environmental basis and assumptions. |
| environmental Manning flow | Concept developed in §51.4; apply with that section's stated environmental basis and assumptions. |
| environmental pump operating point | Concept developed in §51.5; apply with that section's stated environmental basis and assumptions. |
| environmental blower | Concept developed in §51.6; apply with that section's stated environmental basis and assumptions. |
| environmental flow measurement | Concept developed in §51.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **environmental fluid statics** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **environmental pipe head loss** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **environmental Hazen-Williams relation** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **environmental Manning flow** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **environmental pump operating point** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **environmental blower** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **environmental flow measurement** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental fluid statics**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental pipe head loss**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental Hazen-Williams relation**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental Manning flow**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental pump operating point**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental blower**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental flow measurement**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **environmental fluid statics**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **environmental pipe head loss**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **environmental Hazen-Williams relation**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **environmental Manning flow**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **environmental pump operating point**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **environmental blower**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **environmental flow measurement**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **environmental fluid statics**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **environmental pipe head loss**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **environmental fluid statics** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **environmental pipe head loss** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **environmental Hazen-Williams relation** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **environmental Manning flow** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **environmental pump operating point** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **environmental blower** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **environmental flow measurement** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **environmental fluid statics**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **environmental pipe head loss**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **environmental Hazen-Williams relation**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **environmental Manning flow**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **environmental pump operating point**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **environmental blower**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **environmental flow measurement**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

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

1. 10 m of water head corresponds to about 98.1 kPa gauge pressure.

2. Doubling velocity increases Darcy-Weisbach loss by approximately four if f is unchanged.

3. Increasing diameter substantially reduces head loss for fixed flow.

4. For fixed geometry and roughness, discharge scales with square root of slope.

5. Two identical pumps in series ideally add head at the same flow; in parallel they add flow at similar head.

6. At the same flow and pressure rise, lower efficiency requires higher shaft power.

7. For a rectangular-weir form with exponent 3/2, doubling head multiplies flow by 2^(3/2).

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §51.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §51.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §51.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §51.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §51.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §51.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §51.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 8, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 8.

- **environmental fluid statics:** Fluid statics and environmental pressure calculations
- **environmental pipe head loss:** Closed conduits and Darcy-Weisbach loss
- **environmental Hazen-Williams relation:** Hazen-Williams and water-system sizing
- **environmental Manning flow:** Open-channel flow and Manning equation
- **environmental pump operating point:** Pumps, operating points, and efficiency
- **environmental blower:** Blowers and gas-handling power
- **environmental flow measurement:** Weirs, orifices, flumes, and environmental flow measurement

---

## What's Next

**Chapter 03-52: Surface-Water Hydrology — Runoff, Infiltration, Water Budgets, and Storage**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
