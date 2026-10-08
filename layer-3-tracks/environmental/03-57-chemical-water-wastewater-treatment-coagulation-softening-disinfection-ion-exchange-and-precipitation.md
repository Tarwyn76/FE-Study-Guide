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

**Solution.** Coagulation first destabilizes particles and is paired with rapid mixing to disperse the chemical. Flocculation then uses gentler mixing to promote collisions and growth of settleable floc; reversing those hydraulic roles defeats the intended sequence.

---

## 57.2 Chemical precipitation and solubility control

Chemical precipitation removes dissolved species by converting them to insoluble solids. pH, competing ions, and equilibrium strongly affect performance.

\[\mathrm{IAP}>K_{sp}\Rightarrow\text{precipitation favored}\]

![FIG-03-57-002: Dissolved ions converted to precipitate followed by solids separation.](../figures/FIG-03-57-002-chemical-precipitation-and-solubility-control.png)

### Worked Example 2

**Problem.** Raising pH may promote metal-hydroxide precipitation for some metals.

**Solution.** Precipitation becomes thermodynamically favored when the ion-activity product exceeds the solubility product, \(\mathrm{IAP}>K_{sp}\). Adjusting pH can change species activities and therefore drive metal-hydroxide precipitation for suitable metals.

---

## 57.3 Lime-soda softening

Softening calculations convert calcium, magnesium, alkalinity, and reagent needs to a common equivalent basis. The Handbook includes lime-soda relationships in the Environmental section.

\[\text{hardness components}\rightarrow\text{CaCO}_3\text{ equivalent basis}\]

![FIG-03-57-003: Lime-soda softening process with chemical feed, reaction, precipitation, clarification, and recarbonation.](../figures/FIG-03-57-003-lime-soda-softening.png)

### Worked Example 3

**Problem.** Convert species to mg/L as CaCO3 before summing hardness contributions.

**Solution.** Hardness contributions from different ions must be converted to a common **mg/L as CaCO\(_3\)** equivalent basis before addition. Summing raw mg/L of unlike ions directly would not preserve equivalent charge.

---

## 57.4 Disinfection kinetics and contact concepts

Disinfection depends on disinfectant concentration, contact time, organism susceptibility, temperature, and water chemistry. Hydraulic short-circuiting can reduce effective contact.

\[\text{microbial inactivation}=f(C,t,\text{organism},T,\text{water quality})\]

![FIG-03-57-004: Contact basin with baffling, disinfectant decay, residual, and organism inactivation concept.](../figures/FIG-03-57-004-disinfection-kinetics-and-contact-concepts.png)

### Worked Example 4

**Problem.** Higher disinfectant residual or longer effective contact time generally increases inactivation under the same conditions.

**Solution.** Disinfection performance commonly depends on disinfectant residual and effective contact time, along with organism, temperature, pH, and water quality. Under otherwise equal conditions, increasing effective \(C\) or \(t\) generally increases inactivation.

---

## 57.5 Ion exchange and exchange capacity

Ion-exchange media reversibly trade ions with water until capacity is exhausted, after which regeneration or replacement is required.

\[\text{equivalent ions removed}\le\text{available exchange capacity}\]

![FIG-03-57-005: Ion-exchange column showing service, breakthrough, regeneration, and rinse steps.](../figures/FIG-03-57-005-ion-exchange-and-exchange-capacity.png)

### Worked Example 5

**Problem.** A cation exchanger in sodium form can exchange sodium for hardness ions.

**Solution.** A sodium-form cation exchanger supplies exchange sites occupied by Na\(^+\). Ca\(^{2+}\) and Mg\(^{2+}\) can displace sodium according to equivalent charge capacity, thereby removing hardness until the resin approaches exhaustion.

---

## 57.6 Chemical feed, dose, and solution strength

Chemical feed calculations are mass-rate problems. Distinguish active chemical concentration from solution strength and account for purity when needed.

\[\dot m_{\text{chem}}=Q\,C_{\text{dose}}\]

![FIG-03-57-006: Bulk chemical, dilution/metering pump, process flow, dose, and active-strength calculation.](../figures/FIG-03-57-006-chemical-feed-dose-and-solution-strength.png)

### Worked Example 6

**Problem.** A 10-MGD plant applying 5 mg/L active chemical requires about 417 lb/day active chemical.

**Solution.** Active chemical feed is \(8.34QC=(8.34)(10\ {\rm MGD})(5\ {\rm mg/L})=\mathbf{417\ lb/day}\). If the commercial solution is less than 100% active ingredient, the delivered product mass must be increased accordingly.

---

## 57.7 Chemical-process selection and residuals

Chemical treatment frequently creates residual solids or changes pH/ionic composition. Design must include residual handling and downstream compatibility.

\[\text{treatment benefit}\leftrightarrow\text{chemical use+residual solids+downstream effects}\]

![FIG-03-57-007: Chemical-treatment decision flow linking water chemistry, target contaminant, reagent, residuals, and downstream constraints.](../figures/FIG-03-57-007-chemical-process-selection-and-residuals.png)

### Worked Example 7

**Problem.** Precipitation can remove a dissolved contaminant while creating sludge that requires dewatering/disposal.

**Solution.** Chemical precipitation transfers a dissolved constituent into a particulate residual rather than making its mass disappear. The treatment train therefore must include sludge separation, dewatering, handling, and final management.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** A negative chemical dose or precipitated mass indicates a stoichiometric/speciation error or an impossible target. Recheck equivalent basis, pH-dependent species, active strength, solubility constraints, and residual production.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** For **Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation**, the FE Reference Handbook equation, definitions, and unit convention govern whenever the Handbook supplies the needed relation. The external references in this chapter are used for specification-required learned material involving **coagulation/flocculation, precipitation, softening, disinfection, ion exchange, and chemical feed**. If a remembered correlation conflicts with the supplied Handbook equation, use the supplied Handbook relation unless the problem explicitly states a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 12; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required environmental-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects the Handbook and external material into exam-oriented explanations, examples, and checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Sawyer, C. N., McCarty, P. L., & Parkin, G. F. (2003). *Chemistry for Environmental Engineering and Science* (5th ed.). McGraw-Hill. ISBN 978-0-07-119888-2. Supporting scope: Environmental stoichiometry, acid-base chemistry, oxidation-reduction, solubility/precipitation, partitioning, and reaction chemistry.
- Mihelcic, J. R., & Zimmerman, J. B. (2021). *Environmental Engineering: Fundamentals, Sustainability, Design* (3rd ed.). Wiley. ISBN 978-1-119-60445-7. Supporting scope: Environmental measurements, chemistry, physical processes, biology, risk, water quantity/quality, water treatment, wastewater/stormwater, solid waste, and air quality.
- Metcalf & Eddy/AECOM, Tchobanoglous, G., Stensel, H. D., Tsuchihashi, R., & Burton, F. L. (2014). *Wastewater Engineering: Treatment and Resource Recovery* (5th ed.). McGraw-Hill. ISBN 978-0-07-340118-8. Supporting scope: Wastewater characteristics, physical/chemical treatment, activated sludge, solids recycle, biosolids, residuals, and resource recovery.

The external references support only the learned/application portion of the Environmental specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation**, the control volume or conceptual boundary determines which sources, sinks, transfers, reactions, and receptors belong in the model. For this chapter specifically, use equivalent/stoichiometric basis consistently, verify ph and solubility conditions, convert commercial strength to active chemical, and include sludge/residual mass created by treatment.

16. Concentration and loading answer different questions in **Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation**: concentration is mass per volume, while loading is mass per time. Always convert \(Q\) and \(C\) to compatible units before multiplying them.

17. Use the FE Reference Handbook equation and definitions when it supplies the model for **Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation**. The chapter's external references (SAWYER, MIHELCIC, METCALF) support learned specification content, not a competing exam formula.

18. A physical check is needed because algebra alone can return impossible environmental states. For this chapter, set chemical dose to zero and confirm chemical feed mass is zero; at \(\mathrm{IAP}=K_{sp}\) verify the precipitation criterion is exactly at equilibrium.

19. **A.** Section §57.1, **Coagulation, charge destabilization, and flocculation**, is governed by \(\text{destabilization}\rightarrow\text{collision}\rightarrow\text{floc growth}\). Use that relation with its own environmental basis and then perform the specific validity check described for §57.1.

20. **A.** Section §57.2, **Chemical precipitation and solubility control**, is governed by \(\mathrm{IAP}>K_{sp}\Rightarrow\text{precipitation favored}\). Use that relation with its own environmental basis and then perform the specific validity check described for §57.2.

21. **A.** Section §57.3, **Lime-soda softening**, is governed by \(\text{hardness components}\rightarrow\text{CaCO}_3\text{ equivalent basis}\). Use that relation with its own environmental basis and then perform the specific validity check described for §57.3.

22. **A.** Section §57.4, **Disinfection kinetics and contact concepts**, is governed by \(\text{microbial inactivation}=f(C,t,\text{organism},T,\text{water quality})\). Use that relation with its own environmental basis and then perform the specific validity check described for §57.4.

23. **A.** Section §57.5, **Ion exchange and exchange capacity**, is governed by \(\text{equivalent ions removed}\le\text{available exchange capacity}\). Use that relation with its own environmental basis and then perform the specific validity check described for §57.5.

24. **A.** Section §57.6, **Chemical feed, dose, and solution strength**, is governed by \(\dot m_{\text{chem}}=Q\,C_{\text{dose}}\). Use that relation with its own environmental basis and then perform the specific validity check described for §57.6.

25. **A.** Section §57.7, **Chemical-process selection and residuals**, is governed by \(\text{treatment benefit}\leftrightarrow\text{chemical use+residual solids+downstream effects}\). Use that relation with its own environmental basis and then perform the specific validity check described for §57.7.

26. **A.** An integrated **Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation** solution is acceptable only after the governing balance/model is identified, units are reconciled, and the chapter-specific physical checks are satisfied.

27. **A.** Source ownership is explicit in **Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation**: FE-Handbook-supported material remains tied to the ledger, externally supported content uses SAWYER, MIHELCIC, METCALF, and guide synthesis is labeled as supplemental explanation.


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

1. **Independent recomputation for §57.1 — Coagulation, charge destabilization, and flocculation.** Start from the stated givens rather than the worked-example answer. Coagulation first destabilizes particles and is paired with rapid mixing to disperse the chemical. Flocculation then uses gentler mixing to promote collisions and growth of settleable floc; reversing those hydraulic roles defeats the intended sequence. As a separate check, confirm the result is consistent with the section's physical interpretation.

2. **Independent recomputation for §57.2 — Chemical precipitation and solubility control.** Start from the stated givens rather than the worked-example answer. Precipitation becomes thermodynamically favored when the ion-activity product exceeds the solubility product, \(\mathrm{IAP}>K_{sp}\). Adjusting pH can change species activities and therefore drive metal-hydroxide precipitation for suitable metals. As a separate check, confirm the result is consistent with the section's physical interpretation.

3. **Independent recomputation for §57.3 — Lime-soda softening.** Start from the stated givens rather than the worked-example answer. Hardness contributions from different ions must be converted to a common **mg/L as CaCO\(_3\)** equivalent basis before addition. Summing raw mg/L of unlike ions directly would not preserve equivalent charge. As a separate check, confirm the result is consistent with the section's physical interpretation.

4. **Independent recomputation for §57.4 — Disinfection kinetics and contact concepts.** Start from the stated givens rather than the worked-example answer. Disinfection performance commonly depends on disinfectant residual and effective contact time, along with organism, temperature, pH, and water quality. Under otherwise equal conditions, increasing effective \(C\) or \(t\) generally increases inactivation. As a separate check, confirm the result is consistent with the section's physical interpretation.

5. **Independent recomputation for §57.5 — Ion exchange and exchange capacity.** Start from the stated givens rather than the worked-example answer. A sodium-form cation exchanger supplies exchange sites occupied by Na\(^+\). Ca\(^{2+}\) and Mg\(^{2+}\) can displace sodium according to equivalent charge capacity, thereby removing hardness until the resin approaches exhaustion. As a separate check, confirm the result is consistent with the section's physical interpretation.

6. **Independent recomputation for §57.6 — Chemical feed, dose, and solution strength.** Start from the stated givens rather than the worked-example answer. Active chemical feed is \(8.34QC=(8.34)(10\ {\rm MGD})(5\ {\rm mg/L})=\mathbf{417\ lb/day}\). If the commercial solution is less than 100% active ingredient, the delivered product mass must be increased accordingly. As a separate check, confirm the result is consistent with the section's physical interpretation.

7. **Independent recomputation for §57.7 — Chemical-process selection and residuals.** Start from the stated givens rather than the worked-example answer. Chemical precipitation transfers a dissolved constituent into a particulate residual rather than making its mass disappear. The treatment train therefore must include sludge separation, dewatering, handling, and final management. As a separate check, confirm the result is consistent with the section's physical interpretation.

8. For this chapter, check the result against this failure screen: Use equivalent/stoichiometric basis consistently, verify pH and solubility conditions, convert commercial strength to active chemical, and include sludge/residual mass created by treatment. A result that violates one of those conditions should be rejected even if the arithmetic is internally consistent.

9. For **Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation**, begin with the FE Environmental specification area and Handbook subsection recorded in the ledger. When the atom is `split_required`, use the reconciled external source set **SAWYER, MIHELCIC, METCALF** for the learned portion rather than inventing a Handbook page.

10. A useful limiting case is to set chemical dose to zero and confirm chemical feed mass is zero; at \(\mathrm{IAP}=K_{sp}\) verify the precipitation criterion is exactly at equilibrium. The simplified case should reduce to the stated physical behavior before the full model is trusted.

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
