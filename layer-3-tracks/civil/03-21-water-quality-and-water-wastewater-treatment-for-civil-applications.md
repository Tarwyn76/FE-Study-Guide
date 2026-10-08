---
chapter: "03-21"
title: "Water Quality and Water/Wastewater Treatment for Civil Applications"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-021-01, CIV-3-021-02, CIV-3-021-03, CIV-3-021-04, CIV-3-021-05, CIV-3-021-06, CIV-3-021-07]
routes: [civil]
status: drafted
---

# Chapter 03-21: Water Quality and Water/Wastewater Treatment for Civil Applications

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-016-07

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Water Quality and Water/Wastewater Treatment for Civil Applications**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **21.1** Explain and apply **Water-quality concentration, loading, and mass balance**.
* **21.2** Explain and apply **Basic water chemistry — pH, alkalinity, hardness, and equilibrium concepts**.
* **21.3** Explain and apply **Water-quality sampling, testing, and standards**.
* **21.4** Explain and apply **Drinking-water treatment train**.
* **21.5** Explain and apply **Softening and hardness-removal concepts**.
* **21.6** Explain and apply **Wastewater biological treatment and oxygen demand**.
* **21.7** Explain and apply **Civil water-quality decisions and process selection**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 21.1 Water-quality concentration, loading, and mass balance

Water-quality calculations begin with a mass balance. Convert concentrations and flows before multiplying, and distinguish mass rate from concentration.

\[\dot m=QC\]

![FIG-03-21-001: Completely mixed water-quality control volume with influent, effluent, source/sink, Q, and C labels.](../figures/FIG-03-21-001-water-quality-concentration-loading-and-mass-balance.png)

### Worked Example 1

**Problem.** Q=0.5 m³/s and C=10 mg/L gives 5 g/s.

**Solution.** For treatment-process loading, convert the influent concentration first: \(10\ \text{mg/L}=10\ \text{g/m}^3\). Then \(\dot m=QC=(0.5\ \text{m}^3/\text{s})(10\ \text{g/m}^3)=5\ \text{g/s}\). The **5 g/s** value is the contaminant mass entering the treatment process each second and is the basis for a subsequent removal-load calculation.

---

## 21.2 Basic water chemistry — pH, alkalinity, hardness, and equilibrium concepts

Civil FE problems may require basic chemistry interpretation even when detailed equilibrium is outside the Civil handbook section. Use the Environmental section when applicable.

\[\mathrm{pH}=-\log_{10}[H^+]\]

![FIG-03-21-002: pH scale with acidic, neutral, and basic ranges plus hardness/alkalinity concept callouts.](../figures/FIG-03-21-002-basic-water-chemistry-ph-alkalinity-hardness-and-equilibrium-concepts.png)

### Worked Example 2

**Problem.** If [H+]=1e-7 mol/L, pH=7.

**Solution.** Use \(\mathrm{pH}=-\log_{10}[H^+]\). With \([H^+]=1\times10^{-7}\ \text{mol/L}\), \(\mathrm{pH}=-\log_{10}(10^{-7})=7\).

---

## 21.3 Water-quality sampling, testing, and standards

Sampling plans must match the question being asked. A grab sample represents one time and location; composites represent an averaged condition.

\[\bar C=\frac{1}{n}\sum C_i\]

![FIG-03-21-003: Sampling points along a treatment train with grab versus composite sample concepts.](../figures/FIG-03-21-003-water-quality-sampling-testing-and-standards.png)

### Worked Example 3

**Problem.** Three equal-weight samples at 8, 10, and 12 mg/L average 10 mg/L.

**Solution.** For equal-weight samples, the arithmetic mean applies: \(\bar C=(8+10+12)/3=30/3=10\ \text{mg/L}\). If sample volumes or time intervals were unequal, a weighted average could be required instead.

---

## 21.4 Drinking-water treatment train

Conventional drinking-water treatment removes particles and pathogens through sequential unit processes. Some sources require softening or advanced treatment.

\[\text{coagulation}\rightarrow\text{flocculation}\rightarrow\text{sedimentation}\rightarrow\text{filtration}\rightarrow\text{disinfection}\]

![FIG-03-21-004: Conventional drinking-water treatment train from raw-water intake through distribution.](../figures/FIG-03-21-004-drinking-water-treatment-train.png)

### Worked Example 4

**Problem.** Turbidity removal is primarily associated with coagulation/flocculation, sedimentation, and filtration.

**Solution.** The conventional turbidity-removal train is coagulation, flocculation, sedimentation, and filtration. Coagulation destabilizes particles, flocculation builds settleable flocs, sedimentation removes much of the suspended mass, and filtration captures remaining particles. Disinfection serves a different primary purpose: pathogen inactivation.

---

## 21.5 Softening and hardness-removal concepts

Softening reduces calcium and magnesium hardness. FE questions often emphasize equivalent-concentration bookkeeping rather than detailed plant design.

\[\text{hardness as CaCO}_3=\text{equivalent concentration basis}\]

![FIG-03-21-005: Lime-soda softening concept showing chemical addition, precipitation, settling, and recarbonation.](../figures/FIG-03-21-005-softening-and-hardness-removal-concepts.png)

### Worked Example 5

**Problem.** Convert all hardness species to a common CaCO3 equivalent basis before summing.

**Solution.** Hardness species must be converted to an equivalent concentration on a common CaCO₃ basis before addition. This puts ions with different valence and molar mass on the same equivalent-weight basis, allowing total hardness to be summed consistently.

---

## 21.6 Wastewater biological treatment and oxygen demand

Biological treatment uses microorganisms to remove biodegradable organics. Recognize the roles of BOD, aeration, solids separation, and sludge recycle.

\[\text{substrate}+\text{O}_2\rightarrow\text{biomass}+\text{CO}_2+\text{H}_2\text{O}\]

![FIG-03-21-006: Activated-sludge process with aeration basin, secondary clarifier, return sludge, waste sludge, and effluent.](../figures/FIG-03-21-006-wastewater-biological-treatment-and-oxygen-demand.png)

### Worked Example 6

**Problem.** Higher biodegradable loading generally increases oxygen demand.

**Solution.** Biodegradable organic matter consumes oxygen during biological oxidation and biomass synthesis. Therefore, all else equal, a higher biodegradable substrate loading increases the oxygen requirement of an aerobic treatment process and can raise aeration demand.

---

## 21.7 Civil water-quality decisions and process selection

Treatment selection is driven by influent quality, target quality, residuals management, reliability, and applicable standards. Do not infer that one unit process removes every contaminant.

\[\text{required removal}=C_{\text{in}}-C_{\text{target}}\]

![FIG-03-21-007: Decision matrix linking contaminant classes to representative treatment processes and residual streams.](../figures/FIG-03-21-007-civil-water-quality-decisions-and-process-selection.png)

### Worked Example 7

**Problem.** If influent is 12 mg/L and target is 3 mg/L, required reduction is 9 mg/L.

**Solution.** Required concentration reduction is \(C_{in}-C_{target}=12-3=9\ \text{mg/L}\). As a fraction of the influent concentration, the removal efficiency is \(9/12=0.75\), or **75%**, if the problem also asks for percent removal.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a treatment problem, first perform the mass or concentration balance to determine the required removal, then select the process capable of achieving that removal for the contaminant type. Chemical-equilibrium quantities, solids removal, and biological oxygen demand should be kept conceptually separate.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the FE Handbook relation for the calculation being asked—mass balance, pH, hardness, or treatment sizing—and then apply learned process-selection knowledge separately. Do not treat a process-flow sequence as though it were itself a numerical Handbook equation.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 10; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-021-01` — Davis, M. L. (2020). *Water and Wastewater Engineering: Design Principles and Practice* (2nd ed.). McGraw Hill. ISBN 978-1-260-13227-4. Cited at publication/standard level; no page-level claim.
- `CIV-3-021-02` — Davis, M. L. (2020). *Water and Wastewater Engineering: Design Principles and Practice* (2nd ed.). McGraw Hill. ISBN 978-1-260-13227-4. Cited at publication/standard level; no page-level claim.
- `CIV-3-021-04` — Davis, M. L. (2020). *Water and Wastewater Engineering: Design Principles and Practice* (2nd ed.). McGraw Hill. ISBN 978-1-260-13227-4. Cited at publication/standard level; no page-level claim.
- `CIV-3-021-06` — Metcalf & Eddy/AECOM, Tchobanoglous, G., Stensel, H. D., Tsuchihashi, R., & Burton, F. L. (2014). *Wastewater Engineering: Treatment and Resource Recovery* (5th ed.). McGraw Hill. ISBN 978-0-07-340118-8. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

## Where This Goes Wrong

**Using water-quality load without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using basic water chemistry without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using water-quality testing without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using drinking water treatment without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using water softening without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using biological wastewater treatment without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using treatment process selection without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| water-quality load | Concept developed in §21.1; apply with that section's stated assumptions and units. |
| basic water chemistry | Concept developed in §21.2; apply with that section's stated assumptions and units. |
| water-quality testing | Concept developed in §21.3; apply with that section's stated assumptions and units. |
| drinking water treatment | Concept developed in §21.4; apply with that section's stated assumptions and units. |
| water softening | Concept developed in §21.5; apply with that section's stated assumptions and units. |
| biological wastewater treatment | Concept developed in §21.6; apply with that section's stated assumptions and units. |
| treatment process selection | Concept developed in §21.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **water-quality load** and identify the principal quantity, relation, or decision it organizes.

2. Define **basic water chemistry** and identify the principal quantity, relation, or decision it organizes.

3. Define **water-quality testing** and identify the principal quantity, relation, or decision it organizes.

4. Define **drinking water treatment** and identify the principal quantity, relation, or decision it organizes.

5. Define **water softening** and identify the principal quantity, relation, or decision it organizes.

6. Define **biological wastewater treatment** and identify the principal quantity, relation, or decision it organizes.

7. Define **treatment process selection** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **water-quality load**?

9. What assumption or unit error is most likely to cause a wrong result when applying **basic water chemistry**?

10. What assumption or unit error is most likely to cause a wrong result when applying **water-quality testing**?

11. What assumption or unit error is most likely to cause a wrong result when applying **drinking water treatment**?

12. What assumption or unit error is most likely to cause a wrong result when applying **water softening**?

13. What assumption or unit error is most likely to cause a wrong result when applying **biological wastewater treatment**?

14. What assumption or unit error is most likely to cause a wrong result when applying **treatment process selection**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **water-quality load**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **basic water chemistry**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **water-quality testing**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **drinking water treatment**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **water softening**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **biological wastewater treatment**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **treatment process selection**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept


26. Which check is most useful immediately before accepting a numerical answer?
A) Dimensional consistency and physical reasonableness
B) Replacing the stated geometry with a standard case
C) Dropping signs and directions
D) Assuming every quantity is SI

27. When a Civil specification topic is not fully tabulated in Handbook 10.6, the guide should:
A) Identify it as specification-required / learned material
B) Invent a Handbook page reference
C) Omit the topic
D) Treat it as optional


---

## Answer Key with Explanations

1. **water-quality load** is developed in §21.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **basic water chemistry** is developed in §21.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **water-quality testing** is developed in §21.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **drinking water treatment** is developed in §21.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **water softening** is developed in §21.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **biological wastewater treatment** is developed in §21.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **treatment process selection** is developed in §21.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **water-quality load**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **basic water chemistry**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **water-quality testing**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **drinking water treatment**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **water softening**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **biological wastewater treatment**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **treatment process selection**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. Draw the treatment-process control volume and identify influent, effluent, recycle, reaction, and removal terms before selecting a mass-balance or chemistry relation.

16. Use the Handbook mass-balance, pH, or water-quality relation when supplied, then apply process-selection knowledge separately rather than substituting a remembered treatment rule for the reference equation.

17. Concentration and flow must be on compatible bases: mg/L, g/m³, L/s, and m³/s require explicit conversion before mass loading or removal rate is calculated.

18. Check treatment bounds: concentrations and loads cannot be negative, percent removal should remain between 0 and 100 percent, and an effluent target must be lower than influent when removal is claimed.

19. **A.** For **Water-quality concentration, loading, and mass balance**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Basic water chemistry — pH, alkalinity, hardness, and equilibrium concepts**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Water-quality sampling, testing, and standards**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Drinking-water treatment train**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Softening and hardness-removal concepts**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Wastewater biological treatment and oxygen demand**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Civil water-quality decisions and process selection**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Water Quality and Water/Wastewater Treatment for Civil Applications, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Water/wastewater process-selection and biological-treatment details beyond Handbook formulas are labeled learned material and supported by the reconciled Davis and Metcalf & Eddy references.



---

## Practice Problems

1. Q=0.5 m³/s and C=10 mg/L gives 5 g/s.

2. If [H+]=1e-7 mol/L, pH=7.

3. Three equal-weight samples at 8, 10, and 12 mg/L average 10 mg/L.

4. Turbidity removal is primarily associated with coagulation/flocculation, sedimentation, and filtration.

5. Convert all hardness species to a common CaCO3 equivalent basis before summing.

6. Higher biodegradable loading generally increases oxygen demand.

7. If influent is 12 mg/L and target is 3 mg/L, required reduction is 9 mg/L.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. **Independent check for §21.1.** Use the influent flow and concentration as a treatment loading calculation: \(10\ \text{mg/L}=10\ \text{g/m}^3\), so \(QC=(0.5)(10)=5\ \text{g/s}\). Verify the units collapse to mass per time and distinguish this influent load from the amount actually removed by the process.



2. **Independent check for §21.2.** Rework the problem from the stated givens rather than copying the worked-example result. Use \(\mathrm{pH}=-\log_{10}[H^+]\). With \([H^+]=1\times10^{-7}\ \text{mol/L}\), \(\mathrm{pH}=-\log_{10}(10^{-7})=7\). **Check:** confirm the final magnitude and units against the physical meaning of §21.2 before accepting the answer.



3. **Independent check for §21.3.** Rework the problem from the stated givens rather than copying the worked-example result. For equal-weight samples, the arithmetic mean applies: \(\bar C=(8+10+12)/3=30/3=10\ \text{mg/L}\). If sample volumes or time intervals were unequal, a weighted average could be required instead. **Check:** confirm the final magnitude and units against the physical meaning of §21.3 before accepting the answer.



4. **Independent check for §21.4.** Rework the problem from the stated givens rather than copying the worked-example result. The conventional turbidity-removal train is coagulation, flocculation, sedimentation, and filtration. Coagulation destabilizes particles, flocculation builds settleable flocs, sedimentation removes much of the suspended mass, and filtration captures remaining particles. Disinfection serves a different primary purpose: pathogen inactivation. **Check:** confirm the final magnitude and units against the physical meaning of §21.4 before accepting the answer.



5. **Independent check for §21.5.** Rework the problem from the stated givens rather than copying the worked-example result. Hardness species must be converted to an equivalent concentration on a common CaCO₃ basis before addition. This puts ions with different valence and molar mass on the same equivalent-weight basis, allowing total hardness to be summed consistently. **Check:** confirm the final magnitude and units against the physical meaning of §21.5 before accepting the answer.



6. **Independent check for §21.6.** Rework the problem from the stated givens rather than copying the worked-example result. Biodegradable organic matter consumes oxygen during biological oxidation and biomass synthesis. Therefore, all else equal, a higher biodegradable substrate loading increases the oxygen requirement of an aerobic treatment process and can raise aeration demand. **Check:** confirm the final magnitude and units against the physical meaning of §21.6 before accepting the answer.



7. **Independent check for §21.7.** Rework the problem from the stated givens rather than copying the worked-example result. Required concentration reduction is \(C_{in}-C_{target}=12-3=9\ \text{mg/L}\). As a fraction of the influent concentration, the removal efficiency is \(9/12=0.75\), or **75%**, if the problem also asks for percent removal. **Check:** confirm the final magnitude and units against the physical meaning of §21.7 before accepting the answer.



8. Before accepting a water quality and water/wastewater treatment for civil applications result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Start with **FE Civil specification Area 10** and the Handbook water-quality/mass-balance entries in the ledger; use Davis or Metcalf & Eddy for the reconciled learned treatment-process material.

10. For water quality and water/wastewater treatment for civil applications, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 10.

- **water-quality load:** Water-quality concentration, loading, and mass balance
- **basic water chemistry:** Basic water chemistry — pH, alkalinity, hardness, and equilibrium concepts
- **water-quality testing:** Water-quality sampling, testing, and standards
- **drinking water treatment:** Drinking-water treatment train
- **water softening:** Softening and hardness-removal concepts
- **biological wastewater treatment:** Wastewater biological treatment and oxygen demand
- **treatment process selection:** Civil water-quality decisions and process selection

---

## What's Next

**Chapter 03-22: Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
