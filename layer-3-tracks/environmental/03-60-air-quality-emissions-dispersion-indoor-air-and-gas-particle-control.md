---
chapter: "03-60"
title: "Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-060-01, ENV-3-060-02, ENV-3-060-03, ENV-3-060-04, ENV-3-060-05, ENV-3-060-06, ENV-3-060-07]
routes: [environmental]
status: drafted
---

# Chapter 03-60: Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** ENV-3-048-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **60.1** Explain and apply **Air-pollutant concentration units and standard conditions**.
* **60.2** Explain and apply **Emission factors and source loading**.
* **60.3** Explain and apply **Atmospheric stability and lapse rates**.
* **60.4** Explain and apply **Gaussian plume dispersion**.
* **60.5** Explain and apply **Indoor-air mass balance and ventilation**.
* **60.6** Explain and apply **Gas-phase control — absorption, adsorption, biofiltration, and oxidation**.
* **60.7** Explain and apply **Particle control — cyclones, baghouses, and electrostatic precipitators**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 60.1 Air-pollutant concentration units and standard conditions

Gas concentration conversions depend on temperature, pressure, and molecular weight. Do not treat ppm/ppb by volume as fixed mass concentration independent of conditions.

\[C_{\mathrm{mg/m^3}}\propto \frac{\mathrm{ppb}\,MW\,P}{RT}\]

![FIG-03-60-001: Gas parcel with ppm/ppb, molecular weight, temperature, pressure, and mg/m³ conversion path.](../figures/FIG-03-60-001-air-pollutant-concentration-units-and-standard-conditions.png)

### Worked Example 1

**Problem.** For the same ppb concentration, a higher molecular-weight gas has a higher mass concentration at the same T and P.

**Solution.** Apply the relation and environmental model in §60.1; then verify units, boundary conditions, and physical limits.

---

## 60.2 Emission factors and source loading

Emission inventories combine source activity with emission factors or measured stack rates. Control efficiency must be applied on a consistent mass basis.

\[\dot m=EF\times \text{activity rate}\]

![FIG-03-60-002: Source activity flowing through emission factor and control efficiency to stack mass-emission rate.](../figures/FIG-03-60-002-emission-factors-and-source-loading.png)

### Worked Example 2

**Problem.** 100 units/hr at 0.2 kg/unit gives 20 kg/hr uncontrolled emission.

**Solution.** Apply the relation and environmental model in §60.2; then verify units, boundary conditions, and physical limits.

---

## 60.3 Atmospheric stability and lapse rates

Atmospheric stability controls vertical mixing. The Handbook compares environmental lapse rate with the dry adiabatic lapse rate and provides stability-class guidance.

\[\Gamma=\frac{\Delta T}{\Delta z}\]

![FIG-03-60-003: Temperature-versus-height profiles for stable, neutral, and unstable atmospheres.](../figures/FIG-03-60-003-atmospheric-stability-and-lapse-rates.png)

### Worked Example 3

**Problem.** Stable conditions suppress vertical mixing more than unstable conditions.

**Solution.** Apply the relation and environmental model in §60.3; then verify units, boundary conditions, and physical limits.

---

## 60.4 Gaussian plume dispersion

The Gaussian plume model estimates steady-state concentration downwind of a continuous point source under idealized meteorological assumptions. Effective stack height includes plume rise.

\[C(x,y,z)=\frac{Q}{2\pi u\sigma_y\sigma_z}(\cdots)\]

![FIG-03-60-004: Gaussian plume from an elevated stack with x,y,z axes, σy, σz, wind, stack height, and receptor.](../figures/FIG-03-60-004-gaussian-plume-dispersion.png)

### Worked Example 4

**Problem.** Increasing wind speed lowers concentration in the simple model when other variables are unchanged.

**Solution.** Apply the relation and environmental model in §60.4; then verify units, boundary conditions, and physical limits.

---

## 60.5 Indoor-air mass balance and ventilation

Indoor concentration reflects outdoor input, indoor sources, ventilation, removal, and accumulation. At steady state, accumulation vanishes.

\[V\frac{dC_i}{dt}=Q(C_o-C_i)+S-kVC_i\]

![FIG-03-60-005: Single-zone room with outdoor air, exhaust, internal source, removal, and transient concentration response.](../figures/FIG-03-60-005-indoor-air-mass-balance-and-ventilation.png)

### Worked Example 5

**Problem.** Increasing clean ventilation lowers steady indoor concentration for a fixed indoor source when outdoor concentration is lower.

**Solution.** Apply the relation and environmental model in §60.5; then verify units, boundary conditions, and physical limits.

---

## 60.6 Gas-phase control — absorption, adsorption, biofiltration, and oxidation

Gas controls are selected from contaminant solubility, reactivity, concentration, temperature, and flow. Scrubbers, adsorbers, biofilters, thermal/catalytic oxidizers have different strengths.

\[\text{gas contaminant}\rightarrow\text{mass transfer/reaction}\rightarrow\text{controlled exhaust}\]

![FIG-03-60-006: Four gas-control concepts: scrubber, adsorber, biofilter, and thermal/catalytic oxidizer.](../figures/FIG-03-60-006-gas-phase-control-absorption-adsorption-biofiltration-and-oxidation.png)

### Worked Example 6

**Problem.** A highly soluble acid gas is often amenable to wet scrubbing.

**Solution.** Apply the relation and environmental model in §60.6; then verify units, boundary conditions, and physical limits.

---

## 60.7 Particle control — cyclones, baghouses, and electrostatic precipitators

Particle-control devices separate particles by inertia, filtration, or electrostatic migration. Device efficiency depends strongly on particle properties and operating conditions.

\[\eta_{\mathrm{ESP}}=1-e^{-WA/Q}\]

![FIG-03-60-007: Cyclone, baghouse, and electrostatic precipitator with particle-size/collection mechanism comparison.](../figures/FIG-03-60-007-particle-control-cyclones-baghouses-and-electrostatic-precipitators.png)

### Worked Example 7

**Problem.** Increasing ESP collection area A raises ideal Deutsch-Anderson efficiency when W and Q are unchanged.

**Solution.** Apply the relation and environmental model in §60.7; then verify units, boundary conditions, and physical limits.

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

Primary source basis: **FE Environmental specification Area(s) 13; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** Some Environmental specification topics are directly tabulated in the Handbook, while others require learned engineering knowledge. The chapter keeps those two categories separate.

---

## Where This Goes Wrong

**Using air concentration conversion without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using air emission rate without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using atmospheric stability without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using Gaussian plume model without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using indoor air quality mass balance without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using air gas control without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using particulate air control without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| air concentration conversion | Concept developed in §60.1; apply with that section's stated environmental basis and assumptions. |
| air emission rate | Concept developed in §60.2; apply with that section's stated environmental basis and assumptions. |
| atmospheric stability | Concept developed in §60.3; apply with that section's stated environmental basis and assumptions. |
| Gaussian plume model | Concept developed in §60.4; apply with that section's stated environmental basis and assumptions. |
| indoor air quality mass balance | Concept developed in §60.5; apply with that section's stated environmental basis and assumptions. |
| air gas control | Concept developed in §60.6; apply with that section's stated environmental basis and assumptions. |
| particulate air control | Concept developed in §60.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **air concentration conversion** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **air emission rate** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **atmospheric stability** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **Gaussian plume model** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **indoor air quality mass balance** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **air gas control** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **particulate air control** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **air concentration conversion**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **air emission rate**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **atmospheric stability**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **Gaussian plume model**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **indoor air quality mass balance**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **air gas control**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **particulate air control**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **air concentration conversion**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **air emission rate**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **atmospheric stability**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **Gaussian plume model**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **indoor air quality mass balance**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **air gas control**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **particulate air control**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **air concentration conversion**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **air emission rate**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **air concentration conversion** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **air emission rate** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **atmospheric stability** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **Gaussian plume model** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **indoor air quality mass balance** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **air gas control** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **particulate air control** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **air concentration conversion**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **air emission rate**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **atmospheric stability**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **Gaussian plume model**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **indoor air quality mass balance**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **air gas control**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **particulate air control**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

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

1. For the same ppb concentration, a higher molecular-weight gas has a higher mass concentration at the same T and P.

2. 100 units/hr at 0.2 kg/unit gives 20 kg/hr uncontrolled emission.

3. Stable conditions suppress vertical mixing more than unstable conditions.

4. Increasing wind speed lowers concentration in the simple model when other variables are unchanged.

5. Increasing clean ventilation lowers steady indoor concentration for a fixed indoor source when outdoor concentration is lower.

6. A highly soluble acid gas is often amenable to wet scrubbing.

7. Increasing ESP collection area A raises ideal Deutsch-Anderson efficiency when W and Q are unchanged.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §60.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §60.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §60.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §60.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §60.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §60.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §60.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 13, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 13.

- **air concentration conversion:** Air-pollutant concentration units and standard conditions
- **air emission rate:** Emission factors and source loading
- **atmospheric stability:** Atmospheric stability and lapse rates
- **Gaussian plume model:** Gaussian plume dispersion
- **indoor air quality mass balance:** Indoor-air mass balance and ventilation
- **air gas control:** Gas-phase control — absorption, adsorption, biofiltration, and oxidation
- **particulate air control:** Particle control — cyclones, baghouses, and electrostatic precipitators

---

## What's Next

**Chapter 03-61: Solid and Hazardous Waste, Landfills, Treatment, and Energy-Environment Impacts**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
