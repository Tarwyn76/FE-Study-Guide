---
chapter: "03-57"
title: "Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-057-01, ENV-3-057-02, ENV-3-057-03, ENV-3-057-04, ENV-3-057-05, ENV-3-057-06, ENV-3-057-07]
routes: [environmental]
status: drafted
---

# Chapter 03-57: Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** ENV-3-049-07 · ENV-3-056-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **57.1** Explain and apply **Coagulation, charge destabilization, and flocculation**.
* **57.2** Explain and apply **Chemical precipitation and solubility control**.
* **57.3** Explain and apply **Lime-soda softening**.
* **57.4** Explain and apply **Disinfection kinetics and contact concepts**.
* **57.5** Explain and apply **Ion exchange and exchange capacity**.
* **57.6** Explain and apply **Chemical feed, dose, and solution strength**.
* **57.7** Explain and apply **Chemical-process selection and residuals**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 57.1 Coagulation, charge destabilization, and flocculation

Coagulation destabilizes colloids; flocculation provides controlled mixing so particles collide and grow into settleable flocs.

\[\text{destabilization}\rightarrow\text{collision}\rightarrow\text{floc growth}\]

![FIG-03-57-001: Rapid mix, coagulant addition, flocculation basins, and enlarged floc formation.](../figures/FIG-03-57-001-coagulation-charge-destabilization-and-flocculation.png)

### Worked Example 1

**Problem.** Coagulant addition and rapid mixing precede gentler flocculation.

**Solution.** Apply the relation and environmental model in §57.1; then verify units, boundary conditions, and physical limits.

---

## 57.2 Chemical precipitation and solubility control

Chemical precipitation removes dissolved species by converting them to insoluble solids. pH, competing ions, and equilibrium strongly affect performance.

\[\mathrm{IAP}>K_{sp}\Rightarrow\text{precipitation favored}\]

![FIG-03-57-002: Dissolved ions converted to precipitate followed by solids separation.](../figures/FIG-03-57-002-chemical-precipitation-and-solubility-control.png)

### Worked Example 2

**Problem.** Raising pH may promote metal-hydroxide precipitation for some metals.

**Solution.** Apply the relation and environmental model in §57.2; then verify units, boundary conditions, and physical limits.

---

## 57.3 Lime-soda softening

Softening calculations convert calcium, magnesium, alkalinity, and reagent needs to a common equivalent basis. The Handbook includes lime-soda relationships in the Environmental section.

\[\text{hardness components}\rightarrow\text{CaCO}_3\text{ equivalent basis}\]

![FIG-03-57-003: Lime-soda softening process with chemical feed, reaction, precipitation, clarification, and recarbonation.](../figures/FIG-03-57-003-lime-soda-softening.png)

### Worked Example 3

**Problem.** Convert species to mg/L as CaCO3 before summing hardness contributions.

**Solution.** Apply the relation and environmental model in §57.3; then verify units, boundary conditions, and physical limits.

---

## 57.4 Disinfection kinetics and contact concepts

Disinfection depends on disinfectant concentration, contact time, organism susceptibility, temperature, and water chemistry. Hydraulic short-circuiting can reduce effective contact.

\[\text{microbial inactivation}=f(C,t,\text{organism},T,\text{water quality})\]

![FIG-03-57-004: Contact basin with baffling, disinfectant decay, residual, and organism inactivation concept.](../figures/FIG-03-57-004-disinfection-kinetics-and-contact-concepts.png)

### Worked Example 4

**Problem.** Higher disinfectant residual or longer effective contact time generally increases inactivation under the same conditions.

**Solution.** Apply the relation and environmental model in §57.4; then verify units, boundary conditions, and physical limits.

---

## 57.5 Ion exchange and exchange capacity

Ion-exchange media reversibly trade ions with water until capacity is exhausted, after which regeneration or replacement is required.

\[\text{equivalent ions removed}\le\text{available exchange capacity}\]

![FIG-03-57-005: Ion-exchange column showing service, breakthrough, regeneration, and rinse steps.](../figures/FIG-03-57-005-ion-exchange-and-exchange-capacity.png)

### Worked Example 5

**Problem.** A cation exchanger in sodium form can exchange sodium for hardness ions.

**Solution.** Apply the relation and environmental model in §57.5; then verify units, boundary conditions, and physical limits.

---

## 57.6 Chemical feed, dose, and solution strength

Chemical feed calculations are mass-rate problems. Distinguish active chemical concentration from solution strength and account for purity when needed.

\[\dot m_{\text{chem}}=Q\,C_{\text{dose}}\]

![FIG-03-57-006: Bulk chemical, dilution/metering pump, process flow, dose, and active-strength calculation.](../figures/FIG-03-57-006-chemical-feed-dose-and-solution-strength.png)

### Worked Example 6

**Problem.** A 10-MGD plant applying 5 mg/L active chemical requires about 417 lb/day active chemical.

**Solution.** Apply the relation and environmental model in §57.6; then verify units, boundary conditions, and physical limits.

---

## 57.7 Chemical-process selection and residuals

Chemical treatment frequently creates residual solids or changes pH/ionic composition. Design must include residual handling and downstream compatibility.

\[\text{treatment benefit}\leftrightarrow\text{chemical use+residual solids+downstream effects}\]

![FIG-03-57-007: Chemical-treatment decision flow linking water chemistry, target contaminant, reagent, residuals, and downstream constraints.](../figures/FIG-03-57-007-chemical-process-selection-and-residuals.png)

### Worked Example 7

**Problem.** Precipitation can remove a dissolved contaminant while creating sludge that requires dewatering/disposal.

**Solution.** Apply the relation and environmental model in §57.7; then verify units, boundary conditions, and physical limits.

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

**Using coagulation and flocculation without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using chemical precipitation treatment without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using lime-soda softening without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using disinfection without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using ion exchange without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using chemical dose without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using chemical-treatment selection without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| coagulation and flocculation | Concept developed in §57.1; apply with that section's stated environmental basis and assumptions. |
| chemical precipitation treatment | Concept developed in §57.2; apply with that section's stated environmental basis and assumptions. |
| lime-soda softening | Concept developed in §57.3; apply with that section's stated environmental basis and assumptions. |
| disinfection | Concept developed in §57.4; apply with that section's stated environmental basis and assumptions. |
| ion exchange | Concept developed in §57.5; apply with that section's stated environmental basis and assumptions. |
| chemical dose | Concept developed in §57.6; apply with that section's stated environmental basis and assumptions. |
| chemical-treatment selection | Concept developed in §57.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **coagulation and flocculation** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **chemical precipitation treatment** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **lime-soda softening** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **disinfection** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **ion exchange** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **chemical dose** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **chemical-treatment selection** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **coagulation and flocculation**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **chemical precipitation treatment**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **lime-soda softening**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **disinfection**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **ion exchange**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **chemical dose**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **chemical-treatment selection**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **coagulation and flocculation**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **chemical precipitation treatment**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **lime-soda softening**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **disinfection**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **ion exchange**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **chemical dose**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **chemical-treatment selection**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **coagulation and flocculation**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **chemical precipitation treatment**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **coagulation and flocculation** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **chemical precipitation treatment** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **lime-soda softening** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **disinfection** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **ion exchange** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **chemical dose** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **chemical-treatment selection** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **coagulation and flocculation**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **chemical precipitation treatment**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **lime-soda softening**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **disinfection**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **ion exchange**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **chemical dose**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **chemical-treatment selection**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

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

1. Coagulant addition and rapid mixing precede gentler flocculation.

2. Raising pH may promote metal-hydroxide precipitation for some metals.

3. Convert species to mg/L as CaCO3 before summing hardness contributions.

4. Higher disinfectant residual or longer effective contact time generally increases inactivation under the same conditions.

5. A cation exchanger in sodium form can exchange sodium for hardness ions.

6. A 10-MGD plant applying 5 mg/L active chemical requires about 417 lb/day active chemical.

7. Precipitation can remove a dissolved contaminant while creating sludge that requires dewatering/disposal.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §57.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §57.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §57.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §57.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §57.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §57.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §57.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 12, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 12.

- **coagulation and flocculation:** Coagulation, charge destabilization, and flocculation
- **chemical precipitation treatment:** Chemical precipitation and solubility control
- **lime-soda softening:** Lime-soda softening
- **disinfection:** Disinfection kinetics and contact concepts
- **ion exchange:** Ion exchange and exchange capacity
- **chemical dose:** Chemical feed, dose, and solution strength
- **chemical-treatment selection:** Chemical-process selection and residuals

---

## What's Next

**Chapter 03-58: Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
