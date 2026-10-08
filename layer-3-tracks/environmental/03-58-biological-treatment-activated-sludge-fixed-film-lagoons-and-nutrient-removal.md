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

**Solution.** Monod kinetics gives \(\mu=\mu_{max}S/(K_s+S)\). At \(S=K_s\), \(\mu=\mu_{max}K_s/(2K_s)=\mathbf{\mu_{max}/2}\).

---

## 58.2 Biomass yield and substrate conversion

Yield links substrate removal to biomass production. Endogenous decay reduces net solids production relative to gross growth.

\[Y=\frac{\text{biomass produced}}{\text{substrate consumed}}\]

![FIG-03-58-002: Substrate mass split into biomass, oxidation products, and residual substrate.](../figures/FIG-03-58-002-biomass-yield-and-substrate-conversion.png)

### Worked Example 2

**Problem.** A yield of 0.5 kg biomass/kg substrate and 100 kg/day substrate consumption gives 50 kg/day gross biomass.

**Solution.** Gross biomass production is \(Y\) times substrate consumed: \((0.5\ {\rm kg\ biomass/kg\ substrate})(100\ {\rm kg/day})=\mathbf{50\ kg/day}\). Net observed production may be lower when decay is included.

---

## 58.3 Activated-sludge process and solids recycle

Activated sludge suspends microorganisms in an aerated reactor and separates biomass in a secondary clarifier. Return activated sludge maintains biomass inventory; waste sludge controls solids age.

\[\text{aeration basin}\rightarrow\text{secondary clarifier}\rightarrow\text{RAS/WAS}\]

![FIG-03-58-003: Aeration basin, secondary clarifier, return activated sludge, waste activated sludge, influent, and effluent.](../figures/FIG-03-58-003-activated-sludge-process-and-solids-recycle.png)

### Worked Example 3

**Problem.** Increasing waste sludge rate generally decreases solids retention time.

**Solution.** Solids retention time is approximately solids inventory divided by solids wasted per time. Increasing the waste-sludge rate increases the denominator and therefore generally **decreases SRT**, all else equal.

---

## 58.4 Solids retention time and hydraulic retention time

Hydraulic retention time and solids retention time are distinct in systems with biomass recycle. SRT strongly influences nitrification and sludge production.

\[\theta_c=\frac{\text{mass of solids in system}}{\text{mass solids wasted per time}}\]

![FIG-03-58-004: Activated-sludge system showing water residence path versus biomass recycle and solids age.](../figures/FIG-03-58-004-solids-retention-time-and-hydraulic-retention-time.png)

### Worked Example 4

**Problem.** A process can have an 8-hour HRT and a 10-day SRT because solids are recycled.

**Solution.** HRT is governed primarily by liquid volume and flow, while SRT tracks retained biomass solids. Clarification and return activated sludge recycle biomass, allowing **8 h HRT** and **10 d SRT** to coexist without contradiction.

---

## 58.5 Fixed-film processes and biofilm transport

Trickling filters and other attached-growth processes retain biomass on media. Performance couples external flow, mass transfer, and biological reaction.

\[\text{bulk substrate}\rightarrow\text{biofilm diffusion}\rightarrow\text{biodegradation}\]

![FIG-03-58-005: Fixed-film media with liquid flow, biofilm thickness, substrate/oxygen gradients, and sloughing.](../figures/FIG-03-58-005-fixed-film-processes-and-biofilm-transport.png)

### Worked Example 5

**Problem.** A thicker biofilm can increase biomass inventory but also increases diffusion distance.

**Solution.** More biofilm thickness can increase total attached biomass, but substrate and oxygen must diffuse farther into the film. Beyond an effective depth, diffusion limitation and inactive regions can reduce the benefit of added thickness.

---

## 58.6 Lagoons, aerobic, anaerobic, and anoxic environments

Biological processes use different electron-acceptor conditions. Aerobic systems use dissolved oxygen; anoxic processes commonly use oxidized nitrogen; anaerobic processes operate without these external oxidants.

\[\text{aerobic}\neq\text{anoxic}\neq\text{anaerobic}\]

![FIG-03-58-006: Treatment basin zones labeled aerobic, anoxic, and anaerobic with representative transformations.](../figures/FIG-03-58-006-lagoons-aerobic-anaerobic-and-anoxic-environments.png)

### Worked Example 6

**Problem.** Denitrification is commonly an anoxic process.

**Solution.** Denitrification uses oxidized nitrogen as an electron acceptor under **anoxic** conditions—little or no dissolved oxygen, but nitrate/nitrite present. This differs from aerobic and strictly anaerobic conditions.

---

## 58.7 Nitrogen and phosphorus removal

Nutrient removal couples nitrification, denitrification, biological phosphorus uptake, chemical precipitation, or combinations of these processes.

\[\text{N/P removal requires the correct sequence of biological/chemical conditions}\]

![FIG-03-58-007: Biological nutrient-removal train with anaerobic/anoxic/aerobic zones and nitrogen/phosphorus pathways.](../figures/FIG-03-58-007-nitrogen-and-phosphorus-removal.png)

### Worked Example 7

**Problem.** Nitrification converts ammonia toward oxidized nitrogen; denitrification removes oxidized nitrogen as gas.

**Solution.** Nitrification oxidizes ammonia toward nitrite/nitrate; denitrification reduces nitrate/nitrite to gaseous nitrogen species. Effective nitrogen removal therefore requires the proper sequence of **aerobic nitrification** and **anoxic denitrification** conditions.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** A negative biomass or substrate concentration indicates that the biological model has been applied outside its feasible range or with an incorrect sign. Recheck growth/decay terms, recycle/waste flows, and solids inventory.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** For **Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal**, the FE Reference Handbook equation, definitions, and unit convention govern whenever the Handbook supplies the needed relation. The external references in this chapter are used for specification-required learned material involving **Monod growth, biomass yield, activated sludge, SRT/HRT, biofilms, and nutrient removal**. If a remembered correlation conflicts with the supplied Handbook equation, use the supplied Handbook relation unless the problem explicitly states a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 12; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required environmental-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects the Handbook and external material into exam-oriented explanations, examples, and checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Metcalf & Eddy/AECOM, Tchobanoglous, G., Stensel, H. D., Tsuchihashi, R., & Burton, F. L. (2014). *Wastewater Engineering: Treatment and Resource Recovery* (5th ed.). McGraw-Hill. ISBN 978-0-07-340118-8. Supporting scope: Wastewater characteristics, physical/chemical treatment, activated sludge, solids recycle, biosolids, residuals, and resource recovery.
- Mihelcic, J. R., & Zimmerman, J. B. (2021). *Environmental Engineering: Fundamentals, Sustainability, Design* (3rd ed.). Wiley. ISBN 978-1-119-60445-7. Supporting scope: Environmental measurements, chemistry, physical processes, biology, risk, water quantity/quality, water treatment, wastewater/stormwater, solid waste, and air quality.

The external references support only the learned/application portion of the Environmental specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal**, the control volume or conceptual boundary determines which sources, sinks, transfers, reactions, and receptors belong in the model. For this chapter specifically, distinguish hrt from srt, close biomass/substrate balances, keep aerobic/anoxic/anaerobic conditions distinct, and verify growth/decay assumptions before interpreting nutrient removal.

16. Concentration and loading answer different questions in **Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal**: concentration is mass per volume, while loading is mass per time. Always convert \(Q\) and \(C\) to compatible units before multiplying them.

17. Use the FE Reference Handbook equation and definitions when it supplies the model for **Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal**. The chapter's external references (METCALF, MIHELCIC) support learned specification content, not a competing exam formula.

18. A physical check is needed because algebra alone can return impossible environmental states. For this chapter, set substrate \(S	o0\) and confirm Monod growth \(\mu	o0\); set \(S=K_s\) and confirm \(\mu=\mu_{max}/2\).

19. **A.** Section §58.1, **Microbial growth, substrate utilization, and Monod kinetics**, is governed by \(\mu=\mu_{max}\frac{S}{K_s+S}\). Use that relation with its own environmental basis and then perform the specific validity check described for §58.1.

20. **A.** Section §58.2, **Biomass yield and substrate conversion**, is governed by \(Y=\frac{\text{biomass produced}}{\text{substrate consumed}}\). Use that relation with its own environmental basis and then perform the specific validity check described for §58.2.

21. **A.** Section §58.3, **Activated-sludge process and solids recycle**, is governed by \(\text{aeration basin}\rightarrow\text{secondary clarifier}\rightarrow\text{RAS/WAS}\). Use that relation with its own environmental basis and then perform the specific validity check described for §58.3.

22. **A.** Section §58.4, **Solids retention time and hydraulic retention time**, is governed by \(\theta_c=\frac{\text{mass of solids in system}}{\text{mass solids wasted per time}}\). Use that relation with its own environmental basis and then perform the specific validity check described for §58.4.

23. **A.** Section §58.5, **Fixed-film processes and biofilm transport**, is governed by \(\text{bulk substrate}\rightarrow\text{biofilm diffusion}\rightarrow\text{biodegradation}\). Use that relation with its own environmental basis and then perform the specific validity check described for §58.5.

24. **A.** Section §58.6, **Lagoons, aerobic, anaerobic, and anoxic environments**, is governed by \(\text{aerobic}\neq\text{anoxic}\neq\text{anaerobic}\). Use that relation with its own environmental basis and then perform the specific validity check described for §58.6.

25. **A.** Section §58.7, **Nitrogen and phosphorus removal**, is governed by \(\text{N/P removal requires the correct sequence of biological/chemical conditions}\). Use that relation with its own environmental basis and then perform the specific validity check described for §58.7.

26. **A.** An integrated **Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal** solution is acceptable only after the governing balance/model is identified, units are reconciled, and the chapter-specific physical checks are satisfied.

27. **A.** Source ownership is explicit in **Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal**: FE-Handbook-supported material remains tied to the ledger, externally supported content uses METCALF, MIHELCIC, and guide synthesis is labeled as supplemental explanation.


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

1. **Independent recomputation for §58.1 — Microbial growth, substrate utilization, and Monod kinetics.** Start from the stated givens rather than the worked-example answer. Monod kinetics gives \(\mu=\mu_{max}S/(K_s+S)\). At \(S=K_s\), \(\mu=\mu_{max}K_s/(2K_s)=\mathbf{\mu_{max}/2}\). As a separate check, confirm the result is consistent with the section's physical interpretation.

2. **Independent recomputation for §58.2 — Biomass yield and substrate conversion.** Start from the stated givens rather than the worked-example answer. Gross biomass production is \(Y\) times substrate consumed: \((0.5\ {\rm kg\ biomass/kg\ substrate})(100\ {\rm kg/day})=\mathbf{50\ kg/day}\). Net observed production may be lower when decay is included. As a separate check, confirm the result is consistent with the section's physical interpretation.

3. **Independent recomputation for §58.3 — Activated-sludge process and solids recycle.** Start from the stated givens rather than the worked-example answer. Solids retention time is approximately solids inventory divided by solids wasted per time. Increasing the waste-sludge rate increases the denominator and therefore generally **decreases SRT**, all else equal. As a separate check, confirm the result is consistent with the section's physical interpretation.

4. **Independent recomputation for §58.4 — Solids retention time and hydraulic retention time.** Start from the stated givens rather than the worked-example answer. HRT is governed primarily by liquid volume and flow, while SRT tracks retained biomass solids. Clarification and return activated sludge recycle biomass, allowing **8 h HRT** and **10 d SRT** to coexist without contradiction. As a separate check, confirm the result is consistent with the section's physical interpretation.

5. **Independent recomputation for §58.5 — Fixed-film processes and biofilm transport.** Start from the stated givens rather than the worked-example answer. More biofilm thickness can increase total attached biomass, but substrate and oxygen must diffuse farther into the film. Beyond an effective depth, diffusion limitation and inactive regions can reduce the benefit of added thickness. As a separate check, confirm the result is consistent with the section's physical interpretation.

6. **Independent recomputation for §58.6 — Lagoons, aerobic, anaerobic, and anoxic environments.** Start from the stated givens rather than the worked-example answer. Denitrification uses oxidized nitrogen as an electron acceptor under **anoxic** conditions—little or no dissolved oxygen, but nitrate/nitrite present. This differs from aerobic and strictly anaerobic conditions. As a separate check, confirm the result is consistent with the section's physical interpretation.

7. **Independent recomputation for §58.7 — Nitrogen and phosphorus removal.** Start from the stated givens rather than the worked-example answer. Nitrification oxidizes ammonia toward nitrite/nitrate; denitrification reduces nitrate/nitrite to gaseous nitrogen species. Effective nitrogen removal therefore requires the proper sequence of **aerobic nitrification** and **anoxic denitrification** conditions. As a separate check, confirm the result is consistent with the section's physical interpretation.

8. For this chapter, check the result against this failure screen: Distinguish HRT from SRT, close biomass/substrate balances, keep aerobic/anoxic/anaerobic conditions distinct, and verify growth/decay assumptions before interpreting nutrient removal. A result that violates one of those conditions should be rejected even if the arithmetic is internally consistent.

9. For **Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal**, begin with the FE Environmental specification area and Handbook subsection recorded in the ledger. When the atom is `split_required`, use the reconciled external source set **METCALF, MIHELCIC** for the learned portion rather than inventing a Handbook page.

10. A useful limiting case is to set substrate \(S	o0\) and confirm Monod growth \(\mu	o0\); set \(S=K_s\) and confirm \(\mu=\mu_{max}/2\). The simplified case should reduce to the stated physical behavior before the full model is trusted.

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
