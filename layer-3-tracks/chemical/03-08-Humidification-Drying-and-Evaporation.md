---
chapter: "03-08"
title: "Humidification, Drying, and Evaporation"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-008-01, CHE-3-008-02, CHE-3-008-03, CHE-3-008-04, CHE-3-008-05, CHE-3-008-06, CHE-3-008-07]
routes: [chemical]
status: drafted
---

# Chapter 03-08: Humidification, Drying, and Evaporation

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 02-49 Gas Mixtures and Psychrometrics · 02-58 Heat Exchangers · 03-01 Process Balances

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

Humidification and drying/evaporation are explicit specification topics. Psychrometric relations and wet-solid equilibrium curves are directly in the Handbook; detailed dryer and evaporator balance workflows are guide-developed from mass/energy conservation.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **8.1** Explain and apply **Humid-Air Variables for Chemical Operations**.
* **8.2** Explain and apply **Humidification and Dehumidification Balances**.
* **8.3** Explain and apply **Moisture Content on Wet and Dry Basis**.
* **8.4** Explain and apply **Drying Rate and Constant/Falling-Rate Concepts**.
* **8.5** Explain and apply **Equilibrium Moisture**.
* **8.6** Explain and apply **Single-Effect Evaporation Balances**.
* **8.7** Explain and apply **Energy Use and Process Selection**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 8.1 Humid-Air Variables for Chemical Operations

Humidification calculations use humidity ratio \(\omega\), relative humidity, dry-bulb temperature, wet-bulb temperature, and dew point. The general Thermodynamics section provides these definitions and psychrometric charts.

On a dry-air basis, water-vapor mass flow is \(\dot m_a\omega\).

\[\omega=0.622\frac{P_v}{P-P_v}\]

![FIG-03-08-001: Psychrometric chart segment identifying dry-bulb, humidity ratio, relative humidity, wet-bulb, and dew point.](../figures/FIG-03-08-001-humid-air-variables-for-chemical-operations.png)

### Worked Example 1

**Problem.** At P=100 kPa, Pv=2 kPa. Find humidity ratio.

**Solution.** ω=0.622(2)/(98)=0.01269 kg/kg dry air.

---

## 8.2 Humidification and Dehumidification Balances

For a steady humidifier, a dry-air balance plus water balance determines moisture addition or removal. Energy balance determines outlet temperature when heat exchange is involved.

Use dry-air flow as the conserved carrier basis because dry air does not condense in ordinary psychrometric problems.

\[\dot m_w=\dot m_a(\omega_2-\omega_1)\]

![FIG-03-08-002: Humidifier with dry-air basis, inlet/outlet humidity ratio, injected water, and heat transfer.](../figures/FIG-03-08-002-humidification-and-dehumidification-balances.png)

### Worked Example 2

**Problem.** Dry air flow is 5 kg/s, humidity ratio rises 0.005. Find water added.

**Solution.** 0.025 kg/s.

---

## 8.3 Moisture Content on Wet and Dry Basis

Drying problems often report moisture either per mass of wet material or per mass of dry solid. These are not numerically interchangeable.

A dry basis is often convenient because dry-solid mass remains constant during moisture removal.

\[X_{db}=\frac{m_w}{m_{dry}},\qquad X_{wb}=\frac{m_w}{m_w+m_{dry}}\]

![FIG-03-08-003: Wet solid decomposed into dry-solid and water masses with wet-basis and dry-basis moisture definitions.](../figures/FIG-03-08-003-moisture-content-on-wet-and-dry-basis.png)

### Worked Example 3

**Problem.** A wet solid has 2 kg water and 8 kg dry solid. Find wet- and dry-basis moisture.

**Solution.** Xwb=0.20; Xdb=0.25.

---

## 8.4 Drying Rate and Constant/Falling-Rate Concepts

**Guide-developed to satisfy the FE Chemical specification.** Drying can exhibit an initial period in which surface conditions control, followed by a falling-rate period as internal moisture transport becomes limiting.

When a problem supplies a drying-rate curve, drying time follows from integrating moisture removed divided by drying rate on a consistent dry-solid/area basis.

\[dt=\frac{m_{dry}}{A}\frac{-dX}{N(X)}\]

![FIG-03-08-004: Drying rate versus moisture content with constant-rate and falling-rate regions and critical moisture content.](../figures/FIG-03-08-004-drying-rate-and-constant-falling-rate-concepts.png)

### Worked Example 4

**Problem.** A dryer removes moisture at constant 0.5 kg/(m²·h) from 100 kg dry solid over 10 m². Find time to remove 25 kg water.

**Solution.** Rate=5 kg/h; time=5 h.

---

## 8.5 Equilibrium Moisture

The Chemical Engineering section supplies equilibrium moisture curves for representative wet solids. At fixed temperature and relative humidity, equilibrium moisture is the limiting moisture approached after long exposure.

Drying cannot reduce material below the equilibrium moisture corresponding to the surrounding gas without changing gas conditions.

\[X^*=X^*(RH,T,\text{material})\]

![FIG-03-08-005: Equilibrium moisture curves versus relative humidity for several materials, emphasizing free versus equilibrium moisture.](../figures/FIG-03-08-005-equilibrium-moisture.png)

### Worked Example 5

**Problem.** What happens when a solid reaches equilibrium moisture for the surrounding gas?

**Solution.** Net drying tends to zero unless gas conditions change.

---

## 8.6 Single-Effect Evaporation Balances

**Specification-required; detailed balance workflow is guide-developed.** Evaporation concentrates a nonvolatile solute by vaporizing solvent. A solute balance determines concentrate flow; an energy balance determines steam or heat duty.

If solute is nonvolatile, all solute leaves in the liquid concentrate.

\[\dot m_F x_F=\dot m_P x_P,\qquad \dot m_V=\dot m_F-\dot m_P\]

![FIG-03-08-006: Single-effect evaporator with feed, concentrate, vapor, heating steam, condensate, and solute balance.](../figures/FIG-03-08-006-single-effect-evaporation-balances.png)

### Worked Example 6

**Problem.** Feed 1000 kg/h at 10 wt% nonvolatile solute is concentrated to 40 wt%. Find product and vapor rates.

**Solution.** Product=100/0.40=250 kg/h; vapor=750 kg/h.

---

## 8.7 Energy Use and Process Selection

Evaporation, drying, and humidification all couple mass transfer with heat transfer. The dominant energy load is often latent heat.

For FE problems, choose the simplest valid basis: dry air for humidification, dry solid for drying, and nonvolatile-solute balance for evaporation. Then apply one energy balance around the device.

\[\text{latent load}\approx \dot m_{\rm phase\ change}\,h_{fg}\]

![FIG-03-08-007: Humidifier, dryer, and evaporator compared by conserved basis, phase-change stream, and dominant heat duty.](../figures/FIG-03-08-007-energy-use-and-process-selection.png)

### Worked Example 7

**Problem.** Why are humidification/drying/evaporation coupled heat and mass transfer problems?

**Solution.** They move a species between phases and generally require latent/sensible heat.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Dry air 2 kg/s increases ω from 0.01 to 0.03. Find water transfer.

**Solution.** 0.04 kg/s.

### Worked Example 9

**Problem.** Feed 500 kg/h at 20% solids to 50% solids. Find water evaporated.

**Solution.** Solids=100 kg/h; product=200 kg/h; evaporated=300 kg/h.

---

## As the Handbook States It

Primary source basis: **FE Chemical specification Area 10F; general Thermodynamics psychrometrics, printed pp. 149–150 and charts pp. 179–180; Chemical Engineering wet-solids equilibrium data, printed p. 257**.

**Source boundary:** Humidification and drying/evaporation are explicit specification topics. Psychrometric relations and wet-solid equilibrium curves are directly in the Handbook; detailed dryer and evaporator balance workflows are guide-developed from mass/energy conservation.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using humid-air process variable without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using humidification balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using solid moisture basis without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using drying-rate curve without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using equilibrium moisture without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using evaporator material balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using coupled heat and mass transfer without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| humid-air process variable | Concept developed in §8.1; apply with the section's stated basis and assumptions. |
| humidification balance | Concept developed in §8.2; apply with the section's stated basis and assumptions. |
| solid moisture basis | Concept developed in §8.3; apply with the section's stated basis and assumptions. |
| drying-rate curve | Concept developed in §8.4; apply with the section's stated basis and assumptions. |
| equilibrium moisture | Concept developed in §8.5; apply with the section's stated basis and assumptions. |
| evaporator material balance | Concept developed in §8.6; apply with the section's stated basis and assumptions. |
| coupled heat and mass transfer | Concept developed in §8.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **humid-air process variable** and state the governing relation or balance.

2. Define **humidification balance** and state the governing relation or balance.

3. Define **solid moisture basis** and state the governing relation or balance.

4. Define **drying-rate curve** and state the governing relation or balance.

5. Define **equilibrium moisture** and state the governing relation or balance.

6. Define **evaporator material balance** and state the governing relation or balance.

7. Define **coupled heat and mass transfer** and state the governing relation or balance.

8. What is the most likely error if **humid-air process variable** is applied before the process basis and boundary are defined?

9. What is the most likely error if **humidification balance** is applied before the process basis and boundary are defined?

10. What is the most likely error if **solid moisture basis** is applied before the process basis and boundary are defined?

11. What is the most likely error if **drying-rate curve** is applied before the process basis and boundary are defined?

12. What is the most likely error if **equilibrium moisture** is applied before the process basis and boundary are defined?

13. What is the most likely error if **evaporator material balance** is applied before the process basis and boundary are defined?

14. What is the most likely error if **coupled heat and mass transfer** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **humid-air process variable**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **humidification balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **solid moisture basis**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **drying-rate curve**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **equilibrium moisture**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **evaporator material balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **coupled heat and mass transfer**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **humid-air process variable**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **humidification balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **humid-air process variable** is developed in §8.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **humidification balance** is developed in §8.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **solid moisture basis** is developed in §8.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **drying-rate curve** is developed in §8.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **equilibrium moisture** is developed in §8.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **evaporator material balance** is developed in §8.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **coupled heat and mass transfer** is developed in §8.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

8. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

9. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

10. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

11. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

12. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

13. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

14. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

15. The material balance determines the amounts and compositions needed for enthalpy and reaction-energy calculations.

16. To verify that the unknowns are matched by independent equations/specifications before algebra begins.

17. Whenever the problem provides the model/data; use that stated relation rather than substituting an unstated correlation.

18. The Handbook intentionally omits some theories and formulas; exam specifications can require knowledge not directly tabulated in it.

19. **A.** The relation or workflow for **humid-air process variable** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **humidification balance** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **solid moisture basis** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **drying-rate curve** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **equilibrium moisture** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **evaporator material balance** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **coupled heat and mass transfer** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **humid-air process variable** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

27. **A.** The relation or workflow for **humidification balance** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. At P=100 kPa, Pv=2 kPa. Find humidity ratio.

2. Dry air flow is 5 kg/s, humidity ratio rises 0.005. Find water added.

3. A wet solid has 2 kg water and 8 kg dry solid. Find wet- and dry-basis moisture.

4. A dryer removes moisture at constant 0.5 kg/(m²·h) from 100 kg dry solid over 10 m². Find time to remove 25 kg water.

5. What happens when a solid reaches equilibrium moisture for the surrounding gas?

6. Feed 1000 kg/h at 10 wt% nonvolatile solute is concentrated to 40 wt%. Find product and vapor rates.

7. Why are humidification/drying/evaporation coupled heat and mass transfer problems?

8. Dry air 2 kg/s increases ω from 0.01 to 0.03. Find water transfer.

9. Feed 500 kg/h at 20% solids to 50% solids. Find water evaporated.

10. If equilibrium moisture increases with relative humidity, what happens to achievable drying at higher RH?


---

## Practice Problem Solutions

1. ω=0.622(2)/(98)=0.01269 kg/kg dry air.

2. 0.025 kg/s.

3. Xwb=0.20; Xdb=0.25.

4. Rate=5 kg/h; time=5 h.

5. Net drying tends to zero unless gas conditions change.

6. Product=100/0.40=250 kg/h; vapor=750 kg/h.

7. They move a species between phases and generally require latent/sensible heat.

8. 0.04 kg/s.

9. Solids=100 kg/h; product=200 kg/h; evaporated=300 kg/h.

10. The minimum attainable moisture rises; drying potential decreases.


---

## Quick Reference

**Source anchor:** FE Chemical specification Area 10F; general Thermodynamics psychrometrics, printed pp. 149–150 and charts pp. 179–180; Chemical Engineering wet-solids equilibrium data, printed p. 257.

- **humid-air process variable:** Humid-Air Variables for Chemical Operations
- **humidification balance:** Humidification and Dehumidification Balances
- **solid moisture basis:** Moisture Content on Wet and Dry Basis
- **drying-rate curve:** Drying Rate and Constant/Falling-Rate Concepts
- **equilibrium moisture:** Equilibrium Moisture
- **evaporator material balance:** Single-Effect Evaporation Balances
- **coupled heat and mass transfer:** Energy Use and Process Selection
---

## What's Next

**03-09 — Particle Characterization, Solids Handling, Size Reduction, and Crystallization**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor