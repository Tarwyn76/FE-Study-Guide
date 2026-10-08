---
chapter: "03-54"
title: "Groundwater Flow, Aquifer Tests, Wells, and Drawdown"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-054-01, ENV-3-054-02, ENV-3-054-03, ENV-3-054-04, ENV-3-054-05, ENV-3-054-06, ENV-3-054-07]
routes: [environmental]
status: drafted
---

# Chapter 03-54: Groundwater Flow, Aquifer Tests, Wells, and Drawdown

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-020-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Groundwater Flow, Aquifer Tests, Wells, and Drawdown**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **54.1** Explain and apply **Aquifer properties, porosity, and hydraulic conductivity**.
* **54.2** Explain and apply **Darcy law and groundwater velocity**.
* **54.3** Explain and apply **Hydraulic head and gradient**.
* **54.4** Explain and apply **Pumping wells and drawdown**.
* **54.5** Explain and apply **Steady radial-flow well relations**.
* **54.6** Explain and apply **Transient aquifer tests — Theis and Jacob concepts**.
* **54.7** Explain and apply **Specific capacity, interference, and groundwater system checks**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 54.1 Aquifer properties, porosity, and hydraulic conductivity

Groundwater systems are described by porosity, effective porosity, hydraulic conductivity, saturated thickness, transmissivity, and storage properties.

\[n=\frac{V_v}{V},\qquad T=Kb\]

![FIG-03-54-001: Confined and unconfined aquifer sections with porosity, K, b, T, and water-level surfaces.](../figures/FIG-03-54-001-aquifer-properties-porosity-and-hydraulic-conductivity.png)

### Worked Example 1

**Problem.** K=20 m/day and b=15 m gives T=300 m²/day.

**Solution.** Transmissivity is \(T=Kb=(20\ {\rm m/day})(15\ {\rm m})=\mathbf{300\ m^2/day}\). It represents the aquifer's capacity to transmit water through its saturated thickness.

---

## 54.2 Darcy law and groundwater velocity

Darcy flux is discharge divided by gross area; seepage or average linear velocity accounts for effective porosity. These are not the same quantity.

\[Q=KiA,\qquad v_s=\frac{Ki}{n_e}\]

![FIG-03-54-002: Porous medium with hydraulic gradient, Darcy flux, effective porosity, and seepage velocity.](../figures/FIG-03-54-002-darcy-law-and-groundwater-velocity.png)

### Worked Example 2

**Problem.** If Ki=0.3 m/day and ne=0.25, seepage velocity is 1.2 m/day.

**Solution.** Seepage velocity is \(v_s=Ki/n_e\). Given \(Ki=0.3\ {\rm m/day}\) and \(n_e=0.25\), \(v_s=0.3/0.25=\mathbf{1.2\ m/day}\).

---

## 54.3 Hydraulic head and gradient

Groundwater flows from higher hydraulic head toward lower hydraulic head. Elevation and pressure head must share a common datum.

\[i=\frac{\Delta h}{L}\]

![FIG-03-54-003: Piezometers across an aquifer with head contours and groundwater-flow direction.](../figures/FIG-03-54-003-hydraulic-head-and-gradient.png)

### Worked Example 3

**Problem.** A 2-m head drop over 100 m gives i=0.02.

**Solution.** Hydraulic gradient is head change divided by flow-path length: \(i=\Delta h/L=2/100=\mathbf{0.02}\). It is dimensionless when head and distance use the same length unit.

---

## 54.4 Pumping wells and drawdown

Pumping creates a cone of depression. Drawdown varies with pumping rate, aquifer properties, time, distance, and boundary conditions.

\[s=h_0-h\]

![FIG-03-54-004: Pumping well and observation wells across a cone of depression.](../figures/FIG-03-54-004-pumping-wells-and-drawdown.png)

### Worked Example 4

**Problem.** Static head 50 m and pumping head 44 m gives drawdown 6 m.

**Solution.** Drawdown is \(s=h_0-h=50-44=\mathbf{6\ m}\). The positive value indicates that pumping lowered hydraulic head by 6 m relative to static conditions.

---

## 54.5 Steady radial-flow well relations

Thiem/Dupuit-style steady relations connect pumping rate to head differences and radial distance. Use the confined or unconfined form supplied by the problem.

\[Q\propto \frac{T(h_1-h_2)}{\ln(r_2/r_1)}\]

![FIG-03-54-005: Steady radial head profile to a pumping well with r1, r2, h1, h2, and T.](../figures/FIG-03-54-005-steady-radial-flow-well-relations.png)

### Worked Example 5

**Problem.** Greater transmissivity produces less drawdown for the same pumping rate and geometry.

**Solution.** In the steady radial-flow relation, drawdown required to sustain a given \(Q\) is inversely related to transmissivity \(T\). Thus, for the same pumping rate and geometry, **larger \(T\) produces less drawdown**.

---

## 54.6 Transient aquifer tests — Theis and Jacob concepts

Transient pumping tests infer transmissivity and storage from drawdown versus time/distance. Theis and Cooper-Jacob methods are specification topics; use the relation supplied when detailed constants are needed.

\[\text{drawdown}=f(Q,T,S,r,t)\]

![FIG-03-54-006: Semilog drawdown versus time plot with pumping well, observation well, and transmissivity/storage interpretation.](../figures/FIG-03-54-006-transient-aquifer-tests-theis-and-jacob-concepts.png)

### Worked Example 6

**Problem.** At a fixed observation point, drawdown generally increases after pumping begins until boundaries or steady conditions alter the trend.

**Solution.** The Theis solution makes drawdown a function of \(Q,T,S,r,t\). At a fixed observation point after pumping starts, drawdown generally increases with time until boundaries, recharge, leakage, or a new steady/quasi-steady regime changes that trend.

---

## 54.7 Specific capacity, interference, and groundwater system checks

Specific capacity is a practical well-performance measure. Nearby pumping wells can interfere because their cones of depression overlap.

\[\text{specific capacity}=\frac{Q}{s}\]

![FIG-03-54-007: Multiple wells with overlapping cones of depression and specific-capacity labels.](../figures/FIG-03-54-007-specific-capacity-interference-and-groundwater-system-checks.png)

### Worked Example 7

**Problem.** A well pumping 600 gpm with 20 ft drawdown has specific capacity 30 gpm/ft.

**Solution.** Specific capacity is \(Q/s=(600\ {\rm gpm})/(20\ {\rm ft})=\mathbf{30\ gpm/ft}\). It is a performance index tied to the test conditions, not a universal aquifer constant.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** A drawdown sign inconsistent with pumping or a negative transmissivity is a model/setup failure. Recheck head datum, observation radius, pumping sign, logarithm arguments, and aquifer assumptions.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** For **Groundwater Flow, Aquifer Tests, Wells, and Drawdown**, the FE Reference Handbook equation, definitions, and unit convention govern whenever the Handbook supplies the needed relation. The external references in this chapter are used for specification-required learned material involving **Darcy flow, head gradients, pumping wells, transient aquifer response, and specific capacity**. If a remembered correlation conflicts with the supplied Handbook equation, use the supplied Handbook relation unless the problem explicitly states a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 11; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required environmental-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects the Handbook and external material into exam-oriented explanations, examples, and checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Fitts, C. R. (2023). *Groundwater Science* (3rd ed.). Elsevier. ISBN 978-0-12-811455-1. Supporting scope: Aquifer properties, Darcy flow, hydraulic head, wells, drawdown, aquifer tests, contaminant transport, and groundwater modeling.

The external references support only the learned/application portion of the Environmental specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using environmental aquifer properties without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental Darcy flow without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using groundwater hydraulic gradient without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental well drawdown without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using steady groundwater well flow without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using transient aquifer test without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using well specific capacity without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| environmental aquifer properties | Concept developed in §54.1; apply with that section's stated environmental basis and assumptions. |
| environmental Darcy flow | Concept developed in §54.2; apply with that section's stated environmental basis and assumptions. |
| groundwater hydraulic gradient | Concept developed in §54.3; apply with that section's stated environmental basis and assumptions. |
| environmental well drawdown | Concept developed in §54.4; apply with that section's stated environmental basis and assumptions. |
| steady groundwater well flow | Concept developed in §54.5; apply with that section's stated environmental basis and assumptions. |
| transient aquifer test | Concept developed in §54.6; apply with that section's stated environmental basis and assumptions. |
| well specific capacity | Concept developed in §54.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **environmental aquifer properties** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **environmental Darcy flow** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **groundwater hydraulic gradient** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **environmental well drawdown** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **steady groundwater well flow** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **transient aquifer test** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **well specific capacity** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental aquifer properties**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental Darcy flow**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **groundwater hydraulic gradient**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental well drawdown**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **steady groundwater well flow**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **transient aquifer test**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **well specific capacity**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **environmental aquifer properties**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **environmental Darcy flow**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **groundwater hydraulic gradient**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **environmental well drawdown**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **steady groundwater well flow**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **transient aquifer test**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **well specific capacity**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **environmental aquifer properties**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **environmental Darcy flow**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **environmental aquifer properties** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **environmental Darcy flow** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **groundwater hydraulic gradient** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **environmental well drawdown** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **steady groundwater well flow** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **transient aquifer test** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **well specific capacity** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **environmental aquifer properties**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **environmental Darcy flow**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **groundwater hydraulic gradient**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **environmental well drawdown**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **steady groundwater well flow**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **transient aquifer test**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **well specific capacity**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

15. In **Groundwater Flow, Aquifer Tests, Wells, and Drawdown**, the control volume or conceptual boundary determines which sources, sinks, transfers, reactions, and receptors belong in the model. For this chapter specifically, check head datum, gradient direction, aquifer type, radius/time domain, transmissivity/storativity positivity, and whether well-interference or boundaries invalidate the assumed solution.

16. Concentration and loading answer different questions in **Groundwater Flow, Aquifer Tests, Wells, and Drawdown**: concentration is mass per volume, while loading is mass per time. Always convert \(Q\) and \(C\) to compatible units before multiplying them.

17. Use the FE Reference Handbook equation and definitions when it supplies the model for **Groundwater Flow, Aquifer Tests, Wells, and Drawdown**. The chapter's external references (FITTS) support learned specification content, not a competing exam formula.

18. A physical check is needed because algebra alone can return impossible environmental states. For this chapter, set hydraulic gradient to zero and confirm Darcy flow is zero; set pumping rate toward zero and confirm pumping-induced drawdown approaches zero.

19. **A.** Section §54.1, **Aquifer properties, porosity, and hydraulic conductivity**, is governed by \(n=\frac{V_v}{V},\qquad T=Kb\). Use that relation with its own environmental basis and then perform the specific validity check described for §54.1.

20. **A.** Section §54.2, **Darcy law and groundwater velocity**, is governed by \(Q=KiA,\qquad v_s=\frac{Ki}{n_e}\). Use that relation with its own environmental basis and then perform the specific validity check described for §54.2.

21. **A.** Section §54.3, **Hydraulic head and gradient**, is governed by \(i=\frac{\Delta h}{L}\). Use that relation with its own environmental basis and then perform the specific validity check described for §54.3.

22. **A.** Section §54.4, **Pumping wells and drawdown**, is governed by \(s=h_0-h\). Use that relation with its own environmental basis and then perform the specific validity check described for §54.4.

23. **A.** Section §54.5, **Steady radial-flow well relations**, is governed by \(Q\propto \frac{T(h_1-h_2)}{\ln(r_2/r_1)}\). Use that relation with its own environmental basis and then perform the specific validity check described for §54.5.

24. **A.** Section §54.6, **Transient aquifer tests — Theis and Jacob concepts**, is governed by \(\text{drawdown}=f(Q,T,S,r,t)\). Use that relation with its own environmental basis and then perform the specific validity check described for §54.6.

25. **A.** Section §54.7, **Specific capacity, interference, and groundwater system checks**, is governed by \(\text{specific capacity}=\frac{Q}{s}\). Use that relation with its own environmental basis and then perform the specific validity check described for §54.7.

26. **A.** An integrated **Groundwater Flow, Aquifer Tests, Wells, and Drawdown** solution is acceptable only after the governing balance/model is identified, units are reconciled, and the chapter-specific physical checks are satisfied.

27. **A.** Source ownership is explicit in **Groundwater Flow, Aquifer Tests, Wells, and Drawdown**: FE-Handbook-supported material remains tied to the ledger, externally supported content uses FITTS, and guide synthesis is labeled as supplemental explanation.


---

## Practice Problems

1. K=20 m/day and b=15 m gives T=300 m²/day.

2. If Ki=0.3 m/day and ne=0.25, seepage velocity is 1.2 m/day.

3. A 2-m head drop over 100 m gives i=0.02.

4. Static head 50 m and pumping head 44 m gives drawdown 6 m.

5. Greater transmissivity produces less drawdown for the same pumping rate and geometry.

6. At a fixed observation point, drawdown generally increases after pumping begins until boundaries or steady conditions alter the trend.

7. A well pumping 600 gpm with 20 ft drawdown has specific capacity 30 gpm/ft.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. **Independent recomputation for §54.1 — Aquifer properties, porosity, and hydraulic conductivity.** Start from the stated givens rather than the worked-example answer. Transmissivity is \(T=Kb=(20\ {\rm m/day})(15\ {\rm m})=\mathbf{300\ m^2/day}\). It represents the aquifer's capacity to transmit water through its saturated thickness. As a separate check, confirm the result is consistent with the section's physical interpretation.

2. **Independent recomputation for §54.2 — Darcy law and groundwater velocity.** Start from the stated givens rather than the worked-example answer. Seepage velocity is \(v_s=Ki/n_e\). Given \(Ki=0.3\ {\rm m/day}\) and \(n_e=0.25\), \(v_s=0.3/0.25=\mathbf{1.2\ m/day}\). As a separate check, confirm the result is consistent with the section's physical interpretation.

3. **Independent recomputation for §54.3 — Hydraulic head and gradient.** Start from the stated givens rather than the worked-example answer. Hydraulic gradient is head change divided by flow-path length: \(i=\Delta h/L=2/100=\mathbf{0.02}\). It is dimensionless when head and distance use the same length unit. As a separate check, confirm the result is consistent with the section's physical interpretation.

4. **Independent recomputation for §54.4 — Pumping wells and drawdown.** Start from the stated givens rather than the worked-example answer. Drawdown is \(s=h_0-h=50-44=\mathbf{6\ m}\). The positive value indicates that pumping lowered hydraulic head by 6 m relative to static conditions. As a separate check, confirm the result is consistent with the section's physical interpretation.

5. **Independent recomputation for §54.5 — Steady radial-flow well relations.** Start from the stated givens rather than the worked-example answer. In the steady radial-flow relation, drawdown required to sustain a given \(Q\) is inversely related to transmissivity \(T\). Thus, for the same pumping rate and geometry, **larger \(T\) produces less drawdown**. As a separate check, confirm the result is consistent with the section's physical interpretation.

6. **Independent recomputation for §54.6 — Transient aquifer tests — Theis and Jacob concepts.** Start from the stated givens rather than the worked-example answer. The Theis solution makes drawdown a function of \(Q,T,S,r,t\). At a fixed observation point after pumping starts, drawdown generally increases with time until boundaries, recharge, leakage, or a new steady/quasi-steady regime changes that trend. As a separate check, confirm the result is consistent with the section's physical interpretation.

7. **Independent recomputation for §54.7 — Specific capacity, interference, and groundwater system checks.** Start from the stated givens rather than the worked-example answer. Specific capacity is \(Q/s=(600\ {\rm gpm})/(20\ {\rm ft})=\mathbf{30\ gpm/ft}\). It is a performance index tied to the test conditions, not a universal aquifer constant. As a separate check, confirm the result is consistent with the section's physical interpretation.

8. For this chapter, check the result against this failure screen: Check head datum, gradient direction, aquifer type, radius/time domain, transmissivity/storativity positivity, and whether well-interference or boundaries invalidate the assumed solution. A result that violates one of those conditions should be rejected even if the arithmetic is internally consistent.

9. For **Groundwater Flow, Aquifer Tests, Wells, and Drawdown**, begin with the FE Environmental specification area and Handbook subsection recorded in the ledger. When the atom is `split_required`, use the reconciled external source set **FITTS** for the learned portion rather than inventing a Handbook page.

10. A useful limiting case is to set hydraulic gradient to zero and confirm Darcy flow is zero; set pumping rate toward zero and confirm pumping-induced drawdown approaches zero. The simplified case should reduce to the stated physical behavior before the full model is trusted.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 11.

- **environmental aquifer properties:** Aquifer properties, porosity, and hydraulic conductivity
- **environmental Darcy flow:** Darcy law and groundwater velocity
- **groundwater hydraulic gradient:** Hydraulic head and gradient
- **environmental well drawdown:** Pumping wells and drawdown
- **steady groundwater well flow:** Steady radial-flow well relations
- **transient aquifer test:** Transient aquifer tests — Theis and Jacob concepts
- **well specific capacity:** Specific capacity, interference, and groundwater system checks

---

## What's Next

**Chapter 03-55: Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
