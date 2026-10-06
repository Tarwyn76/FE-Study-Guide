---
chapter: "03-49"
title: "Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-049-01, ENV-3-049-02, ENV-3-049-03, ENV-3-049-04, ENV-3-049-05, ENV-3-049-06, ENV-3-049-07]
routes: [environmental]
status: drafted
---

# Chapter 03-49: Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** ENV-3-048-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **49.1** Explain and apply **Stoichiometry, equivalents, and environmental reaction bookkeeping**.
* **49.2** Explain and apply **Acid-base equilibrium and pH**.
* **49.3** Explain and apply **Oxidation-reduction and electron balance**.
* **49.4** Explain and apply **Precipitation, solubility products, and saturation**.
* **49.5** Explain and apply **pC-pH diagrams and species predominance**.
* **49.6** Explain and apply **Henry law, octanol-water, and soil partitioning**.
* **49.7** Explain and apply **Chemical kinetics and temperature correction**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 49.1 Stoichiometry, equivalents, and environmental reaction bookkeeping

Environmental chemistry calculations often require conversion between mass, moles, equivalents, and concentration before equilibrium or treatment equations are applied.

\[\text{moles}=\frac{m}{MW}\]

![FIG-03-49-001: Reaction stoichiometry flow from mass to moles to equivalents to aqueous concentration.](../figures/FIG-03-49-001-stoichiometry-equivalents-and-environmental-reaction-bookkeeping.png)

### Worked Example 1

**Problem.** 58.5 g NaCl is approximately 1 mol.

**Solution.** Apply the relation and environmental model in §49.1; then verify units, boundary conditions, and physical limits.

---

## 49.2 Acid-base equilibrium and pH

Acid-base problems require charge, mass, and equilibrium relationships. Use activities when the problem requires them; otherwise follow the concentration model supplied.

\[\mathrm{pH}=-\log_{10}[H^+],\qquad K_a=\frac{[H^+][A^-]}{[HA]}\]

![FIG-03-49-002: Acid/base species distribution and pH scale with equilibrium relationship callouts.](../figures/FIG-03-49-002-acid-base-equilibrium-and-ph.png)

### Worked Example 2

**Problem.** If [H+]=10^-6 M, pH=6.

**Solution.** Apply the relation and environmental model in §49.2; then verify units, boundary conditions, and physical limits.

---

## 49.3 Oxidation-reduction and electron balance

Redox equations must conserve both atoms and charge. Environmental redox conditions influence contaminant form, mobility, and treatment response.

\[\text{electrons lost}=\text{electrons gained}\]

![FIG-03-49-003: Oxidation and reduction half-reactions combined by electron balance.](../figures/FIG-03-49-003-oxidation-reduction-and-electron-balance.png)

### Worked Example 3

**Problem.** Oxidation of Fe2+ to Fe3+ releases one electron per iron atom.

**Solution.** Apply the relation and environmental model in §49.3; then verify units, boundary conditions, and physical limits.

---

## 49.4 Precipitation, solubility products, and saturation

Precipitation occurs when the ion activity product exceeds the equilibrium solubility product under the modeled conditions. Common-ion and pH effects can strongly shift solubility.

\[K_{sp}=\prod a_i^{\nu_i}\]

![FIG-03-49-004: Ion activity product versus Ksp with undersaturated, saturated, and supersaturated regions.](../figures/FIG-03-49-004-precipitation-solubility-products-and-saturation.png)

### Worked Example 4

**Problem.** If IAP>Ksp, the solution is supersaturated with respect to the solid.

**Solution.** Apply the relation and environmental model in §49.4; then verify units, boundary conditions, and physical limits.

---

## 49.5 pC-pH diagrams and species predominance

pC-pH diagrams compactly show concentration or predominance relationships across pH. Boundary lines come from equilibrium expressions and mass-balance assumptions.

\[pC=-\log_{10}C\]

![FIG-03-49-005: Representative pC-pH diagram with acid/base species boundaries and labeled predominance regions.](../figures/FIG-03-49-005-pc-ph-diagrams-and-species-predominance.png)

### Worked Example 5

**Problem.** Crossing an acid/base boundary changes which protonation state predominates.

**Solution.** Apply the relation and environmental model in §49.5; then verify units, boundary conditions, and physical limits.

---

## 49.6 Henry law, octanol-water, and soil partitioning

Partition coefficients describe equilibrium preference between phases. Large hydrophobic partition coefficients generally indicate stronger affinity for organic phases than water.

\[K_{ow}=\frac{C_o}{C_w},\qquad K_d=K_{oc}f_{oc}\]

![FIG-03-49-006: Contaminant partitioning among air, water, soil organic carbon, and biota with Henry, Kow, Koc, and BCF labels.](../figures/FIG-03-49-006-henry-law-octanol-water-and-soil-partitioning.png)

### Worked Example 6

**Problem.** If Koc=500 L/kg and foc=0.02, Kd=10 L/kg.

**Solution.** Apply the relation and environmental model in §49.6; then verify units, boundary conditions, and physical limits.

---

## 49.7 Chemical kinetics and temperature correction

Reaction rates usually change with temperature. The Handbook supplies representative theta factors for BOD, reaeration, and biological processes; use the factor appropriate to the process.

\[k_T=k_{20}\theta^{T-20}\]

![FIG-03-49-007: Rate constant versus temperature with k20 reference and theta correction.](../figures/FIG-03-49-007-chemical-kinetics-and-temperature-correction.png)

### Worked Example 7

**Problem.** For θ>1, a process rate generally increases as temperature rises above 20°C.

**Solution.** Apply the relation and environmental model in §49.7; then verify units, boundary conditions, and physical limits.

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

Primary source basis: **FE Environmental specification Area(s) 6; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** Some Environmental specification topics are directly tabulated in the Handbook, while others require learned engineering knowledge. The chapter keeps those two categories separate.

---

## Where This Goes Wrong

**Using environmental stoichiometry without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental acid-base equilibrium without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental redox reaction without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using precipitation equilibrium without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using pC-pH diagram without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using multimedia partitioning without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental kinetic temperature correction without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| environmental stoichiometry | Concept developed in §49.1; apply with that section's stated environmental basis and assumptions. |
| environmental acid-base equilibrium | Concept developed in §49.2; apply with that section's stated environmental basis and assumptions. |
| environmental redox reaction | Concept developed in §49.3; apply with that section's stated environmental basis and assumptions. |
| precipitation equilibrium | Concept developed in §49.4; apply with that section's stated environmental basis and assumptions. |
| pC-pH diagram | Concept developed in §49.5; apply with that section's stated environmental basis and assumptions. |
| multimedia partitioning | Concept developed in §49.6; apply with that section's stated environmental basis and assumptions. |
| environmental kinetic temperature correction | Concept developed in §49.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **environmental stoichiometry** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **environmental acid-base equilibrium** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **environmental redox reaction** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **precipitation equilibrium** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **pC-pH diagram** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **multimedia partitioning** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **environmental kinetic temperature correction** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental stoichiometry**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental acid-base equilibrium**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental redox reaction**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **precipitation equilibrium**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **pC-pH diagram**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **multimedia partitioning**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental kinetic temperature correction**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **environmental stoichiometry**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **environmental acid-base equilibrium**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **environmental redox reaction**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **precipitation equilibrium**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **pC-pH diagram**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **multimedia partitioning**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **environmental kinetic temperature correction**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **environmental stoichiometry**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **environmental acid-base equilibrium**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **environmental stoichiometry** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **environmental acid-base equilibrium** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **environmental redox reaction** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **precipitation equilibrium** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **pC-pH diagram** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **multimedia partitioning** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **environmental kinetic temperature correction** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **environmental stoichiometry**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **environmental acid-base equilibrium**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **environmental redox reaction**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **precipitation equilibrium**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **pC-pH diagram**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **multimedia partitioning**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **environmental kinetic temperature correction**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

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

1. 58.5 g NaCl is approximately 1 mol.

2. If [H+]=10^-6 M, pH=6.

3. Oxidation of Fe2+ to Fe3+ releases one electron per iron atom.

4. If IAP>Ksp, the solution is supersaturated with respect to the solid.

5. Crossing an acid/base boundary changes which protonation state predominates.

6. If Koc=500 L/kg and foc=0.02, Kd=10 L/kg.

7. For θ>1, a process rate generally increases as temperature rises above 20°C.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §49.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §49.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §49.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §49.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §49.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §49.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §49.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 6, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 6.

- **environmental stoichiometry:** Stoichiometry, equivalents, and environmental reaction bookkeeping
- **environmental acid-base equilibrium:** Acid-base equilibrium and pH
- **environmental redox reaction:** Oxidation-reduction and electron balance
- **precipitation equilibrium:** Precipitation, solubility products, and saturation
- **pC-pH diagram:** pC-pH diagrams and species predominance
- **multimedia partitioning:** Henry law, octanol-water, and soil partitioning
- **environmental kinetic temperature correction:** Chemical kinetics and temperature correction

---

## What's Next

**Chapter 03-50: Health Hazards, Exposure Pathways, Toxicology, and Risk Assessment**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
