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

**Solution.** At fixed temperature and pressure, ideal-gas conversion from ppb to mass concentration is proportional to molecular weight. Therefore two gases at the same ppb have different mg/m³ values, with the **higher-MW gas having the higher mass concentration**.

---

## 60.2 Emission factors and source loading

Emission inventories combine source activity with emission factors or measured stack rates. Control efficiency must be applied on a consistent mass basis.

\[\dot m=EF\times \text{activity rate}\]

![FIG-03-60-002: Source activity flowing through emission factor and control efficiency to stack mass-emission rate.](../figures/FIG-03-60-002-emission-factors-and-source-loading.png)

### Worked Example 2

**Problem.** 100 units/hr at 0.2 kg/unit gives 20 kg/hr uncontrolled emission.

**Solution.** Emission rate equals emission factor times activity: \((0.2\ {\rm kg/unit})(100\ {\rm units/hr})=\mathbf{20\ kg/hr}\). Controls would be applied afterward if the stated factor is uncontrolled.

---

## 60.3 Atmospheric stability and lapse rates

Atmospheric stability controls vertical mixing. The Handbook compares environmental lapse rate with the dry adiabatic lapse rate and provides stability-class guidance.

\[\Gamma=\frac{\Delta T}{\Delta z}\]

![FIG-03-60-003: Temperature-versus-height profiles for stable, neutral, and unstable atmospheres.](../figures/FIG-03-60-003-atmospheric-stability-and-lapse-rates.png)

### Worked Example 3

**Problem.** Stable conditions suppress vertical mixing more than unstable conditions.

**Solution.** Stable stratification resists vertical displacement and suppresses turbulent mixing, so vertical dispersion is generally smaller than under unstable conditions for otherwise comparable meteorology.

---

## 60.4 Gaussian plume dispersion

The Gaussian plume model estimates steady-state concentration downwind of a continuous point source under idealized meteorological assumptions. Effective stack height includes plume rise.

\[C(x,y,z)=\frac{Q}{2\pi u\sigma_y\sigma_z}(\cdots)\]

![FIG-03-60-004: Gaussian plume from an elevated stack with x,y,z axes, σy, σz, wind, stack height, and receptor.](../figures/FIG-03-60-004-gaussian-plume-dispersion.png)

### Worked Example 4

**Problem.** Increasing wind speed lowers concentration in the simple model when other variables are unchanged.

**Solution.** In the simplified Gaussian plume form, centerline concentration contains a \(1/u\) dependence when source strength and dispersion parameters are treated as fixed. Increasing wind speed therefore **lowers predicted concentration** in that simplified comparison.

---

## 60.5 Indoor-air mass balance and ventilation

Indoor concentration reflects outdoor input, indoor sources, ventilation, removal, and accumulation. At steady state, accumulation vanishes.

\[V\frac{dC_i}{dt}=Q(C_o-C_i)+S-kVC_i\]

![FIG-03-60-005: Single-zone room with outdoor air, exhaust, internal source, removal, and transient concentration response.](../figures/FIG-03-60-005-indoor-air-mass-balance-and-ventilation.png)

### Worked Example 5

**Problem.** Increasing clean ventilation lowers steady indoor concentration for a fixed indoor source when outdoor concentration is lower.

**Solution.** At steady state, \(C_i=(QC_o+S)/(Q+kV)\). If outdoor concentration is below the indoor level produced by the source, increasing clean ventilation \(Q\) drives the indoor concentration downward toward the outdoor value.

---

## 60.6 Gas-phase control — absorption, adsorption, biofiltration, and oxidation

Gas controls are selected from contaminant solubility, reactivity, concentration, temperature, and flow. Scrubbers, adsorbers, biofilters, thermal/catalytic oxidizers have different strengths.

\[\text{gas contaminant}\rightarrow\text{mass transfer/reaction}\rightarrow\text{controlled exhaust}\]

![FIG-03-60-006: Four gas-control concepts: scrubber, adsorber, biofilter, and thermal/catalytic oxidizer.](../figures/FIG-03-60-006-gas-phase-control-absorption-adsorption-biofiltration-and-oxidation.png)

### Worked Example 6

**Problem.** A highly soluble acid gas is often amenable to wet scrubbing.

**Solution.** A highly soluble acid gas has a strong tendency to transfer into an appropriate scrubbing liquid, making **wet absorption/scrubbing** a plausible control. Reagent chemistry and mass-transfer limitations still determine actual performance.

---

## 60.7 Particle control — cyclones, baghouses, and electrostatic precipitators

Particle-control devices separate particles by inertia, filtration, or electrostatic migration. Device efficiency depends strongly on particle properties and operating conditions.

\[\eta_{\mathrm{ESP}}=1-e^{-WA/Q}\]

![FIG-03-60-007: Cyclone, baghouse, and electrostatic precipitator with particle-size/collection mechanism comparison.](../figures/FIG-03-60-007-particle-control-cyclones-baghouses-and-electrostatic-precipitators.png)

### Worked Example 7

**Problem.** Increasing ESP collection area A raises ideal Deutsch-Anderson efficiency when W and Q are unchanged.

**Solution.** Deutsch-Anderson gives \(\eta=1-e^{-WA/Q}\). Increasing collection area \(A\) increases \(WA/Q\), makes the exponential term smaller, and therefore **increases the ideal collection efficiency**.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** A negative physical concentration can arise from a sign error in source/removal terms or an overextended steady-state model. Recheck emission rate, background concentration, ventilation, deposition/reaction losses, and unit conversions.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** For **Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control**, the FE Reference Handbook equation, definitions, and unit convention govern whenever the Handbook supplies the needed relation. The external references in this chapter are used for specification-required learned material involving **emission factors, atmospheric/indoor dispersion, gas absorption, filtration, and electrostatic precipitation**. If a remembered correlation conflicts with the supplied Handbook equation, use the supplied Handbook relation unless the problem explicitly states a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 13; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required environmental-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects the Handbook and external material into exam-oriented explanations, examples, and checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Cooper, C. D., & Alley, F. C. (2011). *Air Pollution Control: A Design Approach* (4th ed.). Waveland Press. ISBN 978-1-57766-678-3. Supporting scope: Air-pollution emissions, dispersion, gas/particle control, scrubbers, adsorption, cyclones, filters, and electrostatic precipitation.
- Mihelcic, J. R., & Zimmerman, J. B. (2021). *Environmental Engineering: Fundamentals, Sustainability, Design* (3rd ed.). Wiley. ISBN 978-1-119-60445-7. Supporting scope: Environmental measurements, chemistry, physical processes, biology, risk, water quantity/quality, water treatment, wastewater/stormwater, solid waste, and air quality.

The external references support only the learned/application portion of the Environmental specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control**, the control volume or conceptual boundary determines which sources, sinks, transfers, reactions, and receptors belong in the model. For this chapter specifically, check standard-state basis for gas concentrations, source versus controlled emission factor, meteorological stability, conservation in the indoor-air balance, and collection efficiency bounds from 0–1.

16. Concentration and loading answer different questions in **Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control**: concentration is mass per volume, while loading is mass per time. Always convert \(Q\) and \(C\) to compatible units before multiplying them.

17. Use the FE Reference Handbook equation and definitions when it supplies the model for **Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control**. The chapter's external references (COOPER_ALLEY, MIHELCIC) support learned specification content, not a competing exam formula.

18. A physical check is needed because algebra alone can return impossible environmental states. For this chapter, set source \(S=0\) in the indoor-air balance and confirm the steady concentration tends toward the outdoor/background value as clean ventilation dominates.

19. **A.** Section §60.1, **Air-pollutant concentration units and standard conditions**, is governed by \(C_{\mathrm{mg/m^3}}\propto \frac{\mathrm{ppb}\,MW\,P}{RT}\). Use that relation with its own environmental basis and then perform the specific validity check described for §60.1.

20. **A.** Section §60.2, **Emission factors and source loading**, is governed by \(\dot m=EF\times \text{activity rate}\). Use that relation with its own environmental basis and then perform the specific validity check described for §60.2.

21. **A.** Section §60.3, **Atmospheric stability and lapse rates**, is governed by \(\Gamma=\frac{\Delta T}{\Delta z}\). Use that relation with its own environmental basis and then perform the specific validity check described for §60.3.

22. **A.** Section §60.4, **Gaussian plume dispersion**, is governed by \(C(x,y,z)=\frac{Q}{2\pi u\sigma_y\sigma_z}(\cdots)\). Use that relation with its own environmental basis and then perform the specific validity check described for §60.4.

23. **A.** Section §60.5, **Indoor-air mass balance and ventilation**, is governed by \(V\frac{dC_i}{dt}=Q(C_o-C_i)+S-kVC_i\). Use that relation with its own environmental basis and then perform the specific validity check described for §60.5.

24. **A.** Section §60.6, **Gas-phase control — absorption, adsorption, biofiltration, and oxidation**, is governed by \(\text{gas contaminant}\rightarrow\text{mass transfer/reaction}\rightarrow\text{controlled exhaust}\). Use that relation with its own environmental basis and then perform the specific validity check described for §60.6.

25. **A.** Section §60.7, **Particle control — cyclones, baghouses, and electrostatic precipitators**, is governed by \(\eta_{\mathrm{ESP}}=1-e^{-WA/Q}\). Use that relation with its own environmental basis and then perform the specific validity check described for §60.7.

26. **A.** An integrated **Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control** solution is acceptable only after the governing balance/model is identified, units are reconciled, and the chapter-specific physical checks are satisfied.

27. **A.** Source ownership is explicit in **Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control**: FE-Handbook-supported material remains tied to the ledger, externally supported content uses COOPER_ALLEY, MIHELCIC, and guide synthesis is labeled as supplemental explanation.


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

1. **Independent recomputation for §60.1 — Air-pollutant concentration units and standard conditions.** Start from the stated givens rather than the worked-example answer. At fixed temperature and pressure, ideal-gas conversion from ppb to mass concentration is proportional to molecular weight. Therefore two gases at the same ppb have different mg/m³ values, with the **higher-MW gas having the higher mass concentration**. As a separate check, confirm the result is consistent with the section's physical interpretation.

2. **Independent recomputation for §60.2 — Emission factors and source loading.** Start from the stated givens rather than the worked-example answer. Emission rate equals emission factor times activity: \((0.2\ {\rm kg/unit})(100\ {\rm units/hr})=\mathbf{20\ kg/hr}\). Controls would be applied afterward if the stated factor is uncontrolled. As a separate check, confirm the result is consistent with the section's physical interpretation.

3. **Independent recomputation for §60.3 — Atmospheric stability and lapse rates.** Start from the stated givens rather than the worked-example answer. Stable stratification resists vertical displacement and suppresses turbulent mixing, so vertical dispersion is generally smaller than under unstable conditions for otherwise comparable meteorology. As a separate check, confirm the result is consistent with the section's physical interpretation.

4. **Independent recomputation for §60.4 — Gaussian plume dispersion.** Start from the stated givens rather than the worked-example answer. In the simplified Gaussian plume form, centerline concentration contains a \(1/u\) dependence when source strength and dispersion parameters are treated as fixed. Increasing wind speed therefore **lowers predicted concentration** in that simplified comparison. As a separate check, confirm the result is consistent with the section's physical interpretation.

5. **Independent recomputation for §60.5 — Indoor-air mass balance and ventilation.** Start from the stated givens rather than the worked-example answer. At steady state, \(C_i=(QC_o+S)/(Q+kV)\). If outdoor concentration is below the indoor level produced by the source, increasing clean ventilation \(Q\) drives the indoor concentration downward toward the outdoor value. As a separate check, confirm the result is consistent with the section's physical interpretation.

6. **Independent recomputation for §60.6 — Gas-phase control — absorption, adsorption, biofiltration, and oxidation.** Start from the stated givens rather than the worked-example answer. A highly soluble acid gas has a strong tendency to transfer into an appropriate scrubbing liquid, making **wet absorption/scrubbing** a plausible control. Reagent chemistry and mass-transfer limitations still determine actual performance. As a separate check, confirm the result is consistent with the section's physical interpretation.

7. **Independent recomputation for §60.7 — Particle control — cyclones, baghouses, and electrostatic precipitators.** Start from the stated givens rather than the worked-example answer. Deutsch-Anderson gives \(\eta=1-e^{-WA/Q}\). Increasing collection area \(A\) increases \(WA/Q\), makes the exponential term smaller, and therefore **increases the ideal collection efficiency**. As a separate check, confirm the result is consistent with the section's physical interpretation.

8. For this chapter, check the result against this failure screen: Check standard-state basis for gas concentrations, source versus controlled emission factor, meteorological stability, conservation in the indoor-air balance, and collection efficiency bounds from 0–1. A result that violates one of those conditions should be rejected even if the arithmetic is internally consistent.

9. For **Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control**, begin with the FE Environmental specification area and Handbook subsection recorded in the ledger. When the atom is `split_required`, use the reconciled external source set **COOPER_ALLEY, MIHELCIC** for the learned portion rather than inventing a Handbook page.

10. A useful limiting case is to set source \(S=0\) in the indoor-air balance and confirm the steady concentration tends toward the outdoor/background value as clean ventilation dominates. The simplified case should reduce to the stated physical behavior before the full model is trusted.

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
