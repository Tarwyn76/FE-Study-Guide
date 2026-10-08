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

**Solution.** The molecular weight of NaCl is about \(58.44\ {\rm g/mol}\). Thus \(n=58.5/58.44=1.001\ {\rm mol}\), so **58.5 g NaCl is approximately 1 mol**.

---

## 49.2 Acid-base equilibrium and pH

Acid-base problems require charge, mass, and equilibrium relationships. Use activities when the problem requires them; otherwise follow the concentration model supplied.

\[\mathrm{pH}=-\log_{10}[H^+],\qquad K_a=\frac{[H^+][A^-]}{[HA]}\]

![FIG-03-49-002: Acid/base species distribution and pH scale with equilibrium relationship callouts.](../figures/FIG-03-49-002-acid-base-equilibrium-and-ph.png)

### Worked Example 2

**Problem.** If [H+]=10^-6 M, pH=6.

**Solution.** \(\mathrm{pH}=-\log_{10}[H^+]=-\log_{10}(10^{-6})=\mathbf{6}\). The result assumes concentration is being used as the activity approximation appropriate to the exercise.

---

## 49.3 Oxidation-reduction and electron balance

Redox equations must conserve both atoms and charge. Environmental redox conditions influence contaminant form, mobility, and treatment response.

\[\text{electrons lost}=\text{electrons gained}\]

![FIG-03-49-003: Oxidation and reduction half-reactions combined by electron balance.](../figures/FIG-03-49-003-oxidation-reduction-and-electron-balance.png)

### Worked Example 3

**Problem.** Oxidation of Fe2+ to Fe3+ releases one electron per iron atom.

**Solution.** The oxidation half-reaction is \(\mathrm{Fe^{2+}\rightarrow Fe^{3+}+e^-}\). The oxidation state rises by one, so **one electron is released per Fe atom** and electron balance must be preserved when combining half-reactions.

---

## 49.4 Precipitation, solubility products, and saturation

Precipitation occurs when the ion activity product exceeds the equilibrium solubility product under the modeled conditions. Common-ion and pH effects can strongly shift solubility.

\[K_{sp}=\prod a_i^{\nu_i}\]

![FIG-03-49-004: Ion activity product versus Ksp with undersaturated, saturated, and supersaturated regions.](../figures/FIG-03-49-004-precipitation-solubility-products-and-saturation.png)

### Worked Example 4

**Problem.** If IAP>Ksp, the solution is supersaturated with respect to the solid.

**Solution.** Compare the ion-activity product to the solubility product. If \(\mathrm{IAP}>K_{sp}\), the saturation ratio exceeds one and the solution is **supersaturated**; precipitation is thermodynamically favored until equilibrium is approached.

---

## 49.5 pC-pH diagrams and species predominance

pC-pH diagrams compactly show concentration or predominance relationships across pH. Boundary lines come from equilibrium expressions and mass-balance assumptions.

\[pC=-\log_{10}C\]

![FIG-03-49-005: Representative pC-pH diagram with acid/base species boundaries and labeled predominance regions.](../figures/FIG-03-49-005-pc-ph-diagrams-and-species-predominance.png)

### Worked Example 5

**Problem.** Crossing an acid/base boundary changes which protonation state predominates.

**Solution.** For a simple conjugate acid-base pair, the predominance boundary occurs near \(\mathrm{pH}=pK_a\). Crossing that boundary changes whether the protonated or deprotonated form is dominant, which is exactly what a pC-pH predominance diagram is intended to show.

---

## 49.6 Henry law, octanol-water, and soil partitioning

Partition coefficients describe equilibrium preference between phases. Large hydrophobic partition coefficients generally indicate stronger affinity for organic phases than water.

\[K_{ow}=\frac{C_o}{C_w},\qquad K_d=K_{oc}f_{oc}\]

![FIG-03-49-006: Contaminant partitioning among air, water, soil organic carbon, and biota with Henry, Kow, Koc, and BCF labels.](../figures/FIG-03-49-006-henry-law-octanol-water-and-soil-partitioning.png)

### Worked Example 6

**Problem.** If Koc=500 L/kg and foc=0.02, Kd=10 L/kg.

**Solution.** Soil-water partitioning is \(K_d=K_{oc}f_{oc}\). Therefore \(K_d=(500\ {\rm L/kg})(0.02)=\mathbf{10\ L/kg}\). The organic-carbon fraction must be entered as 0.02, not 2.

---

## 49.7 Chemical kinetics and temperature correction

Reaction rates usually change with temperature. The Handbook supplies representative theta factors for BOD, reaeration, and biological processes; use the factor appropriate to the process.

\[k_T=k_{20}\theta^{T-20}\]

![FIG-03-49-007: Rate constant versus temperature with k20 reference and theta correction.](../figures/FIG-03-49-007-chemical-kinetics-and-temperature-correction.png)

### Worked Example 7

**Problem.** For θ>1, a process rate generally increases as temperature rises above 20°C.

**Solution.** With \(k_T=k_{20}\theta^{T-20}\), if \(\theta>1\) and \(T>20^\circ{\rm C}\), then the exponent is positive and \(\theta^{T-20}>1\). Therefore **\(k_T>k_{20}\)** under the empirical temperature-correction model.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** A negative concentration usually indicates an algebraic/speciation setup error or misuse of an equilibrium approximation. Check charge/mass balance, logarithms, activity assumptions, and whether a precipitated or alternative species should have been included.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** For **Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH**, the FE Reference Handbook equation, definitions, and unit convention govern whenever the Handbook supplies the needed relation. The external references in this chapter are used for specification-required learned material involving **aqueous stoichiometry, acid-base/redox equilibrium, solubility, partitioning, and environmental kinetics**. If a remembered correlation conflicts with the supplied Handbook equation, use the supplied Handbook relation unless the problem explicitly states a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 6; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required environmental-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects the Handbook and external material into exam-oriented explanations, examples, and checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Sawyer, C. N., McCarty, P. L., & Parkin, G. F. (2003). *Chemistry for Environmental Engineering and Science* (5th ed.). McGraw-Hill. ISBN 978-0-07-119888-2. Supporting scope: Environmental stoichiometry, acid-base chemistry, oxidation-reduction, solubility/precipitation, partitioning, and reaction chemistry.
- Mihelcic, J. R., & Zimmerman, J. B. (2021). *Environmental Engineering: Fundamentals, Sustainability, Design* (3rd ed.). Wiley. ISBN 978-1-119-60445-7. Supporting scope: Environmental measurements, chemistry, physical processes, biology, risk, water quantity/quality, water treatment, wastewater/stormwater, solid waste, and air quality.

The external references support only the learned/application portion of the Environmental specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH**, the control volume or conceptual boundary determines which sources, sinks, transfers, reactions, and receptors belong in the model. For this chapter specifically, check charge/mass balance, activity-versus-concentration assumptions, saturation ratio, species predominance, and that logarithm arguments are positive and dimensionally appropriate.

16. Concentration and loading answer different questions in **Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH**: concentration is mass per volume, while loading is mass per time. Always convert \(Q\) and \(C\) to compatible units before multiplying them.

17. Use the FE Reference Handbook equation and definitions when it supplies the model for **Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH**. The chapter's external references (SAWYER, MIHELCIC) support learned specification content, not a competing exam formula.

18. A physical check is needed because algebra alone can return impossible environmental states. For this chapter, at \([H^+]=10^{-7}\) M under the simplified dilute-water convention, verify pH 7; at \(\mathrm{IAP}=K_{sp}\), verify saturation equilibrium.

19. **A.** Section §49.1, **Stoichiometry, equivalents, and environmental reaction bookkeeping**, is governed by \(\text{moles}=\frac{m}{MW}\). Use that relation with its own environmental basis and then perform the specific validity check described for §49.1.

20. **A.** Section §49.2, **Acid-base equilibrium and pH**, is governed by \(\mathrm{pH}=-\log_{10}[H^+],\qquad K_a=\frac{[H^+][A^-]}{[HA]}\). Use that relation with its own environmental basis and then perform the specific validity check described for §49.2.

21. **A.** Section §49.3, **Oxidation-reduction and electron balance**, is governed by \(\text{electrons lost}=\text{electrons gained}\). Use that relation with its own environmental basis and then perform the specific validity check described for §49.3.

22. **A.** Section §49.4, **Precipitation, solubility products, and saturation**, is governed by \(K_{sp}=\prod a_i^{\nu_i}\). Use that relation with its own environmental basis and then perform the specific validity check described for §49.4.

23. **A.** Section §49.5, **pC-pH diagrams and species predominance**, is governed by \(pC=-\log_{10}C\). Use that relation with its own environmental basis and then perform the specific validity check described for §49.5.

24. **A.** Section §49.6, **Henry law, octanol-water, and soil partitioning**, is governed by \(K_{ow}=\frac{C_o}{C_w},\qquad K_d=K_{oc}f_{oc}\). Use that relation with its own environmental basis and then perform the specific validity check described for §49.6.

25. **A.** Section §49.7, **Chemical kinetics and temperature correction**, is governed by \(k_T=k_{20}\theta^{T-20}\). Use that relation with its own environmental basis and then perform the specific validity check described for §49.7.

26. **A.** An integrated **Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH** solution is acceptable only after the governing balance/model is identified, units are reconciled, and the chapter-specific physical checks are satisfied.

27. **A.** Source ownership is explicit in **Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH**: FE-Handbook-supported material remains tied to the ledger, externally supported content uses SAWYER, MIHELCIC, and guide synthesis is labeled as supplemental explanation.


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

1. **Independent recomputation for §49.1 — Stoichiometry, equivalents, and environmental reaction bookkeeping.** Start from the stated givens rather than the worked-example answer. The molecular weight of NaCl is about \(58.44\ {\rm g/mol}\). Thus \(n=58.5/58.44=1.001\ {\rm mol}\), so **58.5 g NaCl is approximately 1 mol**. As a separate check, confirm the result is consistent with the section's physical interpretation.

2. **Independent recomputation for §49.2 — Acid-base equilibrium and pH.** Start from the stated givens rather than the worked-example answer. \(\mathrm{pH}=-\log_{10}[H^+]=-\log_{10}(10^{-6})=\mathbf{6}\). The result assumes concentration is being used as the activity approximation appropriate to the exercise. As a separate check, confirm the result is consistent with the section's physical interpretation.

3. **Independent recomputation for §49.3 — Oxidation-reduction and electron balance.** Start from the stated givens rather than the worked-example answer. The oxidation half-reaction is \(\mathrm{Fe^{2+}\rightarrow Fe^{3+}+e^-}\). The oxidation state rises by one, so **one electron is released per Fe atom** and electron balance must be preserved when combining half-reactions. As a separate check, confirm the result is consistent with the section's physical interpretation.

4. **Independent recomputation for §49.4 — Precipitation, solubility products, and saturation.** Start from the stated givens rather than the worked-example answer. Compare the ion-activity product to the solubility product. If \(\mathrm{IAP}>K_{sp}\), the saturation ratio exceeds one and the solution is **supersaturated**; precipitation is thermodynamically favored until equilibrium is approached. As a separate check, confirm the result is consistent with the section's physical interpretation.

5. **Independent recomputation for §49.5 — pC-pH diagrams and species predominance.** Start from the stated givens rather than the worked-example answer. For a simple conjugate acid-base pair, the predominance boundary occurs near \(\mathrm{pH}=pK_a\). Crossing that boundary changes whether the protonated or deprotonated form is dominant, which is exactly what a pC-pH predominance diagram is intended to show. As a separate check, confirm the result is consistent with the section's physical interpretation.

6. **Independent recomputation for §49.6 — Henry law, octanol-water, and soil partitioning.** Start from the stated givens rather than the worked-example answer. Soil-water partitioning is \(K_d=K_{oc}f_{oc}\). Therefore \(K_d=(500\ {\rm L/kg})(0.02)=\mathbf{10\ L/kg}\). The organic-carbon fraction must be entered as 0.02, not 2. As a separate check, confirm the result is consistent with the section's physical interpretation.

7. **Independent recomputation for §49.7 — Chemical kinetics and temperature correction.** Start from the stated givens rather than the worked-example answer. With \(k_T=k_{20}\theta^{T-20}\), if \(\theta>1\) and \(T>20^\circ{\rm C}\), then the exponent is positive and \(\theta^{T-20}>1\). Therefore **\(k_T>k_{20}\)** under the empirical temperature-correction model. As a separate check, confirm the result is consistent with the section's physical interpretation.

8. For this chapter, check the result against this failure screen: Check charge/mass balance, activity-versus-concentration assumptions, saturation ratio, species predominance, and that logarithm arguments are positive and dimensionally appropriate. A result that violates one of those conditions should be rejected even if the arithmetic is internally consistent.

9. For **Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH**, begin with the FE Environmental specification area and Handbook subsection recorded in the ledger. When the atom is `split_required`, use the reconciled external source set **SAWYER, MIHELCIC** for the learned portion rather than inventing a Handbook page.

10. A useful limiting case is to at \([H^+]=10^{-7}\) M under the simplified dilute-water convention, verify pH 7; at \(\mathrm{IAP}=K_{sp}\), verify saturation equilibrium. The simplified case should reduce to the stated physical behavior before the full model is trusted.

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
