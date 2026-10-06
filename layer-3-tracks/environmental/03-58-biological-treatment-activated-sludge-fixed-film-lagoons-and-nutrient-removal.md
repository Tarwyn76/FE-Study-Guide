---
chapter: "03-58"
title: "Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-058-01, ENV-3-058-02, ENV-3-058-03, ENV-3-058-04, ENV-3-058-05, ENV-3-058-06, ENV-3-058-07]
routes: [environmental]
status: drafted
---

# Chapter 03-58: Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** ENV-3-056-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **58.1** Explain and apply **Microbial growth, substrate utilization, and Monod kinetics**.
* **58.2** Explain and apply **Biomass yield and substrate conversion**.
* **58.3** Explain and apply **Activated-sludge process and solids recycle**.
* **58.4** Explain and apply **Solids retention time and hydraulic retention time**.
* **58.5** Explain and apply **Fixed-film processes and biofilm transport**.
* **58.6** Explain and apply **Lagoons, aerobic, anaerobic, and anoxic environments**.
* **58.7** Explain and apply **Nitrogen and phosphorus removal**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 58.1 Microbial growth, substrate utilization, and Monod kinetics

Monod kinetics represent substrate-limited microbial growth. At S=Ks, the growth rate is half the maximum under the simple model.

\[\mu=\mu_{max}\frac{S}{K_s+S}\]

![FIG-03-58-001: Monod growth-rate curve versus limiting substrate with Ks and μmax labeled.](../figures/FIG-03-58-001-microbial-growth-substrate-utilization-and-monod-kinetics.png)

### Worked Example 1

**Problem.** If S=Ks, μ=μmax/2.

**Solution.** Apply the relation and environmental model in §58.1; then verify units, boundary conditions, and physical limits.

---

## 58.2 Biomass yield and substrate conversion

Yield links substrate removal to biomass production. Endogenous decay reduces net solids production relative to gross growth.

\[Y=\frac{\text{biomass produced}}{\text{substrate consumed}}\]

![FIG-03-58-002: Substrate mass split into biomass, oxidation products, and residual substrate.](../figures/FIG-03-58-002-biomass-yield-and-substrate-conversion.png)

### Worked Example 2

**Problem.** A yield of 0.5 kg biomass/kg substrate and 100 kg/day substrate consumption gives 50 kg/day gross biomass.

**Solution.** Apply the relation and environmental model in §58.2; then verify units, boundary conditions, and physical limits.

---

## 58.3 Activated-sludge process and solids recycle

Activated sludge suspends microorganisms in an aerated reactor and separates biomass in a secondary clarifier. Return activated sludge maintains biomass inventory; waste sludge controls solids age.

\[\text{aeration basin}\rightarrow\text{secondary clarifier}\rightarrow\text{RAS/WAS}\]

![FIG-03-58-003: Aeration basin, secondary clarifier, return activated sludge, waste activated sludge, influent, and effluent.](../figures/FIG-03-58-003-activated-sludge-process-and-solids-recycle.png)

### Worked Example 3

**Problem.** Increasing waste sludge rate generally decreases solids retention time.

**Solution.** Apply the relation and environmental model in §58.3; then verify units, boundary conditions, and physical limits.

---

## 58.4 Solids retention time and hydraulic retention time

Hydraulic retention time and solids retention time are distinct in systems with biomass recycle. SRT strongly influences nitrification and sludge production.

\[\theta_c=\frac{\text{mass of solids in system}}{\text{mass solids wasted per time}}\]

![FIG-03-58-004: Activated-sludge system showing water residence path versus biomass recycle and solids age.](../figures/FIG-03-58-004-solids-retention-time-and-hydraulic-retention-time.png)

### Worked Example 4

**Problem.** A process can have an 8-hour HRT and a 10-day SRT because solids are recycled.

**Solution.** Apply the relation and environmental model in §58.4; then verify units, boundary conditions, and physical limits.

---

## 58.5 Fixed-film processes and biofilm transport

Trickling filters and other attached-growth processes retain biomass on media. Performance couples external flow, mass transfer, and biological reaction.

\[\text{bulk substrate}\rightarrow\text{biofilm diffusion}\rightarrow\text{biodegradation}\]

![FIG-03-58-005: Fixed-film media with liquid flow, biofilm thickness, substrate/oxygen gradients, and sloughing.](../figures/FIG-03-58-005-fixed-film-processes-and-biofilm-transport.png)

### Worked Example 5

**Problem.** A thicker biofilm can increase biomass inventory but also increases diffusion distance.

**Solution.** Apply the relation and environmental model in §58.5; then verify units, boundary conditions, and physical limits.

---

## 58.6 Lagoons, aerobic, anaerobic, and anoxic environments

Biological processes use different electron-acceptor conditions. Aerobic systems use dissolved oxygen; anoxic processes commonly use oxidized nitrogen; anaerobic processes operate without these external oxidants.

\[\text{aerobic}\neq\text{anoxic}\neq\text{anaerobic}\]

![FIG-03-58-006: Treatment basin zones labeled aerobic, anoxic, and anaerobic with representative transformations.](../figures/FIG-03-58-006-lagoons-aerobic-anaerobic-and-anoxic-environments.png)

### Worked Example 6

**Problem.** Denitrification is commonly an anoxic process.

**Solution.** Apply the relation and environmental model in §58.6; then verify units, boundary conditions, and physical limits.

---

## 58.7 Nitrogen and phosphorus removal

Nutrient removal couples nitrification, denitrification, biological phosphorus uptake, chemical precipitation, or combinations of these processes.

\[\text{N/P removal requires the correct sequence of biological/chemical conditions}\]

![FIG-03-58-007: Biological nutrient-removal train with anaerobic/anoxic/aerobic zones and nitrogen/phosphorus pathways.](../figures/FIG-03-58-007-nitrogen-and-phosphorus-removal.png)

### Worked Example 7

**Problem.** Nitrification converts ammonia toward oxidized nitrogen; denitrification removes oxidized nitrogen as gas.

**Solution.** Apply the relation and environmental model in §58.7; then verify units, boundary conditions, and physical limits.

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

Primary source basis: **FE Environmental specification Area(s) 12; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** Some Environmental specification topics are directly tabulated in the Handbook, while others require learned engineering knowledge. The chapter keeps those two categories separate.

---

## Where This Goes Wrong

**Using Monod kinetics without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using biological yield coefficient without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using activated sludge without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using solids retention time without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using fixed-film biological treatment without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using biological redox environment without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using biological nutrient removal without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| Monod kinetics | Concept developed in §58.1; apply with that section's stated environmental basis and assumptions. |
| biological yield coefficient | Concept developed in §58.2; apply with that section's stated environmental basis and assumptions. |
| activated sludge | Concept developed in §58.3; apply with that section's stated environmental basis and assumptions. |
| solids retention time | Concept developed in §58.4; apply with that section's stated environmental basis and assumptions. |
| fixed-film biological treatment | Concept developed in §58.5; apply with that section's stated environmental basis and assumptions. |
| biological redox environment | Concept developed in §58.6; apply with that section's stated environmental basis and assumptions. |
| biological nutrient removal | Concept developed in §58.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **Monod kinetics** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **biological yield coefficient** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **activated sludge** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **solids retention time** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **fixed-film biological treatment** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **biological redox environment** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **biological nutrient removal** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **Monod kinetics**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **biological yield coefficient**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **activated sludge**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **solids retention time**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **fixed-film biological treatment**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **biological redox environment**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **biological nutrient removal**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **Monod kinetics**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **biological yield coefficient**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **activated sludge**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **solids retention time**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **fixed-film biological treatment**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **biological redox environment**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **biological nutrient removal**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **Monod kinetics**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **biological yield coefficient**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **Monod kinetics** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **biological yield coefficient** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **activated sludge** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **solids retention time** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **fixed-film biological treatment** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **biological redox environment** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **biological nutrient removal** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **Monod kinetics**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **biological yield coefficient**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **activated sludge**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **solids retention time**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **fixed-film biological treatment**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **biological redox environment**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **biological nutrient removal**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

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

1. If S=Ks, μ=μmax/2.

2. A yield of 0.5 kg biomass/kg substrate and 100 kg/day substrate consumption gives 50 kg/day gross biomass.

3. Increasing waste sludge rate generally decreases solids retention time.

4. A process can have an 8-hour HRT and a 10-day SRT because solids are recycled.

5. A thicker biofilm can increase biomass inventory but also increases diffusion distance.

6. Denitrification is commonly an anoxic process.

7. Nitrification converts ammonia toward oxidized nitrogen; denitrification removes oxidized nitrogen as gas.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §58.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §58.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §58.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §58.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §58.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §58.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §58.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 12, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 12.

- **Monod kinetics:** Microbial growth, substrate utilization, and Monod kinetics
- **biological yield coefficient:** Biomass yield and substrate conversion
- **activated sludge:** Activated-sludge process and solids recycle
- **solids retention time:** Solids retention time and hydraulic retention time
- **fixed-film biological treatment:** Fixed-film processes and biofilm transport
- **biological redox environment:** Lagoons, aerobic, anaerobic, and anoxic environments
- **biological nutrient removal:** Nitrogen and phosphorus removal

---

## What's Next

**Chapter 03-59: Sludge/Biosolids Handling, Water Reuse, and Residuals Management**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
