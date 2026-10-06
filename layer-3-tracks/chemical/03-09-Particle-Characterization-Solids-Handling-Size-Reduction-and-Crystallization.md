---
chapter: "03-09"
title: "Particle Characterization, Solids Handling, Size Reduction, and Crystallization"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-009-01, CHE-3-009-02, CHE-3-009-03, CHE-3-009-04, CHE-3-009-05, CHE-3-009-06, CHE-3-009-07]
routes: [chemical]
status: drafted
---

# Chapter 03-09: Particle Characterization, Solids Handling, Size Reduction, and Crystallization

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 02-18 Phase Change and Processing · 03-01 Process Balances

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly provides particle-size operation ranges, sieve conversion, particle-size distributions and mean diameters, size-reduction equipment selection, classifier tables, angle of repose, wet-solid equilibrium curves, and a crystallization phase diagram.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **9.1** Explain and apply **Particle Size Distributions**.
* **9.2** Explain and apply **Mean Particle Diameters**.
* **9.3** Explain and apply **Sieve Analysis and Mesh Conversion**.
* **9.4** Explain and apply **Crushing and Grinding**.
* **9.5** Explain and apply **Classification and Separation of Solids**.
* **9.6** Explain and apply **Bulk Solids, Angle of Repose, Transport, and Storage**.
* **9.7** Explain and apply **Crystallization and Phase Diagrams**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 9.1 Particle Size Distributions

A particle-size distribution (PSD) may be represented by a density function or cumulative fraction. Number-based and mass/volume-based PSDs weight particle populations differently.

Always identify whether a reported cumulative distribution is number, mass, or volume based.

\[F(x)=\int_0^x f(\xi)\,d\xi\]

![FIG-03-09-001: Differential and cumulative particle-size distributions with number and mass bases distinguished.](../figures/FIG-03-09-001-particle-size-distributions.png)

### Worked Example 1

**Problem.** A cumulative PSD says 70% mass is below 100 µm. What fraction is above 100 µm?

**Solution.** 30%.

---

## 9.2 Mean Particle Diameters

The Handbook gives several mean diameters because no single average preserves every physical property. Number mean emphasizes particle count; Sauter mean preserves surface-area-to-volume behavior and is important in transfer operations.

Use the mean diameter definition specified in the problem rather than an arithmetic mean by habit.

\[d_{32}=\frac{\sum n_i d_i^3}{\sum n_i d_i^2}\]

![FIG-03-09-002: Same PSD annotated with number mean, Sauter mean, and volume mean and their physical interpretations.](../figures/FIG-03-09-002-mean-particle-diameters.png)

### Worked Example 2

**Problem.** Why is Sauter mean relevant to transfer?

**Solution.** It preserves surface-area-to-volume behavior.

---

## 9.3 Sieve Analysis and Mesh Conversion

The Handbook provides a mesh-to-micron conversion table and indicates that a plus sign means retained on a sieve while a minus sign means passing.

A size fraction such as \(-20+40\) mesh means the material passes the 20-mesh sieve and is retained on the 40-mesh sieve.

\[\text{sieve fraction}=\frac{\text{mass in size interval}}{\text{total sample mass}}\]

![FIG-03-09-003: Stacked sieves with decreasing openings, retained masses, and interpretation of plus/minus mesh notation.](../figures/FIG-03-09-003-sieve-analysis-and-mesh-conversion.png)

### Worked Example 3

**Problem.** A 200 g sieve sample retains 30 g in one interval. Find interval mass fraction.

**Solution.** 0.15.

---

## 9.4 Crushing and Grinding

The Handbook tabulates feed/product size ranges, reduction ratios, and candidate equipment for crushing, grinding, and disintegration.

Equipment selection depends on feed size, desired product size, hardness, throughput, and whether the operation is coarse or fine.

\[\text{reduction ratio}\approx \frac{d_{\rm feed}}{d_{\rm product}}\]

![FIG-03-09-004: Feed-size to product-size map connecting crushing/grinding ranges to jaw, roll, media, and high-speed mills.](../figures/FIG-03-09-004-crushing-and-grinding.png)

### Worked Example 4

**Problem.** Feed size is 20 mm and product size 2 mm. Estimate reduction ratio.

**Solution.** 10.

---

## 9.5 Classification and Separation of Solids

The Handbook lists wet and dry classifiers such as sloping-tank classifiers, hydrocyclones, and other devices across particle-size ranges.

Classification separates by settling, centrifugal action, density, size, magnetic/electrical properties, or surface behavior depending on the equipment.

\[\text{classifier performance depends on particle size, density, fluid, and operating field}\]

![FIG-03-09-005: Hydrocyclone and settling classifier with feed, coarse underflow, fine overflow, and particle trajectories.](../figures/FIG-03-09-005-classification-and-separation-of-solids.png)

### Worked Example 5

**Problem.** What outlet of a hydrocyclone commonly carries coarser/denser solids?

**Solution.** Underflow.

---

## 9.6 Bulk Solids, Angle of Repose, Transport, and Storage

Angle of repose describes the stable free-surface slope of a granular pile and influences hopper and storage design. The FE specification also includes belts, pneumatic transport, slurries, tanks, and hoppers.

Detailed conveying correlations are not tabulated in the Chemical Engineering section; use supplied data when a problem goes beyond basic geometry and balance calculations.

\[\tan\theta_r=\frac{h}{r}\quad\text{for a simple conical pile geometry}\]

![FIG-03-09-006: Conical pile and hopper showing angle of repose, pile height/radius, and flow versus arching concerns.](../figures/FIG-03-09-006-bulk-solids-angle-of-repose-transport-and-storage.png)

### Worked Example 6

**Problem.** A conical pile has h=1.0 m and radius 2.0 m. Find angle of repose.

**Solution.** θ=atan(0.5)=26.6°.

---

## 9.7 Crystallization and Phase Diagrams

Crystallization separates a solid phase from solution by changing temperature, solvent amount, or composition. The Handbook provides an example hydrate-formation phase diagram with single- and two-phase regions.

Use the phase diagram to identify stable solid form and equilibrium liquid composition, then apply total and solute balances to determine crystal yield.

\[\text{solute in feed}=\text{solute in mother liquor}+\text{solute in crystals}\]

![FIG-03-09-007: Solubility/phase diagram with cooling path and mass balance between crystals and mother liquor.](../figures/FIG-03-09-007-crystallization-and-phase-diagrams.png)

### Worked Example 7

**Problem.** A crystallizer feed has 100 kg solute; mother liquor contains 30 kg solute. Find solute in crystals.

**Solution.** 70 kg, assuming no other solute outlet.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What does '-20+40 mesh' mean?

**Solution.** Passes 20-mesh and is retained on 40-mesh.

### Worked Example 9

**Problem.** Why do number- and mass-based PSD means differ?

**Solution.** Large particles contribute far more mass/volume per particle.

---

## As the Handbook States It

Primary source basis: **Chemical Engineering, printed pp. 256–262; FE Chemical specification Area 11**.

**Source boundary:** The Handbook directly provides particle-size operation ranges, sieve conversion, particle-size distributions and mean diameters, size-reduction equipment selection, classifier tables, angle of repose, wet-solid equilibrium curves, and a crystallization phase diagram.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using particle-size distribution without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using Sauter mean diameter without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using sieve analysis without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using size reduction without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using solids classification without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using angle of repose without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using crystallization phase balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| particle-size distribution | Concept developed in §9.1; apply with the section's stated basis and assumptions. |
| Sauter mean diameter | Concept developed in §9.2; apply with the section's stated basis and assumptions. |
| sieve analysis | Concept developed in §9.3; apply with the section's stated basis and assumptions. |
| size reduction | Concept developed in §9.4; apply with the section's stated basis and assumptions. |
| solids classification | Concept developed in §9.5; apply with the section's stated basis and assumptions. |
| angle of repose | Concept developed in §9.6; apply with the section's stated basis and assumptions. |
| crystallization phase balance | Concept developed in §9.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **particle-size distribution** and state the governing relation or balance.

2. Define **Sauter mean diameter** and state the governing relation or balance.

3. Define **sieve analysis** and state the governing relation or balance.

4. Define **size reduction** and state the governing relation or balance.

5. Define **solids classification** and state the governing relation or balance.

6. Define **angle of repose** and state the governing relation or balance.

7. Define **crystallization phase balance** and state the governing relation or balance.

8. What is the most likely error if **particle-size distribution** is applied before the process basis and boundary are defined?

9. What is the most likely error if **Sauter mean diameter** is applied before the process basis and boundary are defined?

10. What is the most likely error if **sieve analysis** is applied before the process basis and boundary are defined?

11. What is the most likely error if **size reduction** is applied before the process basis and boundary are defined?

12. What is the most likely error if **solids classification** is applied before the process basis and boundary are defined?

13. What is the most likely error if **angle of repose** is applied before the process basis and boundary are defined?

14. What is the most likely error if **crystallization phase balance** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **particle-size distribution**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **Sauter mean diameter**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **sieve analysis**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **size reduction**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **solids classification**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **angle of repose**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **crystallization phase balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **particle-size distribution**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **Sauter mean diameter**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **particle-size distribution** is developed in §9.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **Sauter mean diameter** is developed in §9.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **sieve analysis** is developed in §9.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **size reduction** is developed in §9.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **solids classification** is developed in §9.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **angle of repose** is developed in §9.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **crystallization phase balance** is developed in §9.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

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

19. **A.** The relation or workflow for **particle-size distribution** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **Sauter mean diameter** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **sieve analysis** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **size reduction** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **solids classification** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **angle of repose** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **crystallization phase balance** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **particle-size distribution** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

27. **A.** The relation or workflow for **Sauter mean diameter** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. A cumulative PSD says 70% mass is below 100 µm. What fraction is above 100 µm?

2. Why is Sauter mean relevant to transfer?

3. A 200 g sieve sample retains 30 g in one interval. Find interval mass fraction.

4. Feed size is 20 mm and product size 2 mm. Estimate reduction ratio.

5. What outlet of a hydrocyclone commonly carries coarser/denser solids?

6. A conical pile has h=1.0 m and radius 2.0 m. Find angle of repose.

7. A crystallizer feed has 100 kg solute; mother liquor contains 30 kg solute. Find solute in crystals.

8. What does '-20+40 mesh' mean?

9. Why do number- and mass-based PSD means differ?

10. If cooling moves a solution from one liquid region into liquid+solid region, what operation is indicated?


---

## Practice Problem Solutions

1. 30%.

2. It preserves surface-area-to-volume behavior.

3. 0.15.

4. 10.

5. Underflow.

6. θ=atan(0.5)=26.6°.

7. 70 kg, assuming no other solute outlet.

8. Passes 20-mesh and is retained on 40-mesh.

9. Large particles contribute far more mass/volume per particle.

10. Crystallization/solid precipitation.


---

## Quick Reference

**Source anchor:** Chemical Engineering, printed pp. 256–262; FE Chemical specification Area 11.

- **particle-size distribution:** Particle Size Distributions
- **Sauter mean diameter:** Mean Particle Diameters
- **sieve analysis:** Sieve Analysis and Mesh Conversion
- **size reduction:** Crushing and Grinding
- **solids classification:** Classification and Separation of Solids
- **angle of repose:** Bulk Solids, Angle of Repose, Transport, and Storage
- **crystallization phase balance:** Crystallization and Phase Diagrams
---

## What's Next

**03-10 — Reaction Kinetics, Rate Laws, and Arrhenius Behavior**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor