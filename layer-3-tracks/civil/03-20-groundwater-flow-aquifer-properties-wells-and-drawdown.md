---
chapter: "03-20"
title: "Groundwater Flow, Aquifer Properties, Wells, and Drawdown"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-020-01, CIV-3-020-02, CIV-3-020-03, CIV-3-020-04, CIV-3-020-05, CIV-3-020-06, CIV-3-020-07]
routes: [civil]
status: drafted
---

# Chapter 03-20: Groundwater Flow, Aquifer Properties, Wells, and Drawdown

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** CIV-3-016-07

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Groundwater Flow, Aquifer Properties, Wells, and Drawdown**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **20.1** Explain and apply **Darcy law and hydraulic gradient**.
* **20.2** Explain and apply **Hydraulic conductivity, permeability tests, and anisotropy**.
* **20.3** Explain and apply **Aquifer transmissivity and confined flow**.
* **20.4** Explain and apply **Unconfined aquifers and water-table concepts**.
* **20.5** Explain and apply **Well drawdown and radial flow**.
* **20.6** Explain and apply **Multiple wells, superposition, and interference**.
* **20.7** Explain and apply **Seepage, effective stress, and groundwater-structure interaction**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 20.1 Darcy law and hydraulic gradient

Darcy's law relates discharge to hydraulic conductivity, gradient, and area for laminar porous-media flow. The sign of gradient follows the chosen head coordinate.

\[Q=K\,i\,A\]

![FIG-03-20-001: Groundwater flow through soil prism with head difference, length, gradient, K, area, and Q.](../figures/FIG-03-20-001-darcy-law-and-hydraulic-gradient.png)

### Worked Example 1

**Problem.** K=1e-4 m/s, i=0.02, A=50 m² gives Q=1e-4 m³/s.

**Solution.** Darcy's law is \(Q=KiA\). Substituting \(K=1\times10^{-4}\ \text{m/s}\), \(i=0.02\), and \(A=50\ \text{m}^2\) gives \(Q=(10^{-4})(0.02)(50)=1.0\times10^{-4}\ \text{m}^3/\text{s}\).

---

## 20.2 Hydraulic conductivity, permeability tests, and anisotropy

Laboratory constant-head and falling-head tests infer hydraulic conductivity from measured flow and head change. Field values may differ because of scale and stratification.

\[K=\frac{Q}{iAt}\]

![FIG-03-20-002: Constant-head and falling-head permeability test apparatus side by side.](../figures/FIG-03-20-002-hydraulic-conductivity-permeability-tests-and-anisotropy.png)

### Worked Example 2

**Problem.** Given measured volume, elapsed time, gradient, and area, solve for K with consistent units.

**Solution.** For a constant-head style calculation, determine discharge rate from measured volume divided by elapsed time, then rearrange Darcy's law: \(K=Q/(iA)\). If a measured volume \(V\) is supplied instead of \(Q\), use \(K=V/(t\,iA)\). Convert time, length, and volume to one consistent unit system before substitution.

---

## 20.3 Aquifer transmissivity and confined flow

Transmissivity combines hydraulic conductivity and saturated thickness. It is especially useful for confined-aquifer well relations.

\[T=Kb\]

![FIG-03-20-003: Confined aquifer cross-section with aquitards, thickness b, piezometric surface, and pumping well.](../figures/FIG-03-20-003-aquifer-transmissivity-and-confined-flow.png)

### Worked Example 3

**Problem.** K=30 m/day and b=20 m gives T=600 m²/day.

**Solution.** Transmissivity is \(T=Kb\). With \(K=30\ \text{m/day}\) and saturated thickness \(b=20\ \text{m}\), \(T=30(20)=600\ \text{m}^2/\text{day}\).

---

## 20.4 Unconfined aquifers and water-table concepts

In an unconfined aquifer, the water table is a free surface. Saturated thickness changes as drawdown develops.

\[h=z+\frac{p}{\gamma}\]

![FIG-03-20-004: Unconfined aquifer with water table, recharge, pumping well, and cone of depression.](../figures/FIG-03-20-004-unconfined-aquifers-and-water-table-concepts.png)

### Worked Example 4

**Problem.** At the water table, gauge pressure is approximately zero, so hydraulic head equals elevation head.

**Solution.** Hydraulic head is \(h=z+p/\gamma\). At the water table the pore pressure is atmospheric, so gauge pressure is approximately zero and \(p/\gamma=0\). Therefore the hydraulic head at the water table is approximately equal to the elevation head \(z\).

---

## 20.5 Well drawdown and radial flow

Pumping lowers hydraulic head near a well, creating a cone of depression. FE problems may provide the radial-flow relation directly or through the Handbook.

\[s=h_0-h(r)\]

![FIG-03-20-005: Plan and cross-sectional views of a pumping well cone of depression with radius and drawdown labels.](../figures/FIG-03-20-005-well-drawdown-and-radial-flow.png)

### Worked Example 5

**Problem.** If static head is 120 ft and pumping head is 108 ft, drawdown is 12 ft.

**Solution.** Drawdown is the difference between static and pumping head: \(s=h_0-h(r)\). With \(h_0=120\ \text{ft}\) and pumping head \(108\ \text{ft}\), \(s=120-108=12\ \text{ft}\).

---

## 20.6 Multiple wells, superposition, and interference

When the governing groundwater equation is linear over the modeled range, drawdowns from multiple wells can be superposed approximately.

\[s_{\text{total}}\approx \sum s_i\]

![FIG-03-20-006: Two pumping wells with overlapping cones of depression and a shared observation point.](../figures/FIG-03-20-006-multiple-wells-superposition-and-interference.png)

### Worked Example 6

**Problem.** Two wells causing 3 ft and 5 ft drawdown at a point produce about 8 ft total by superposition.

**Solution.** Under linear confined-aquifer assumptions, drawdowns from multiple wells may be superposed. At the point of interest, \(s_{total}=3+5=8\ \text{ft}\). This approximation depends on the individual solutions being based on compatible aquifer assumptions.

---

## 20.7 Seepage, effective stress, and groundwater-structure interaction

Groundwater flow affects uplift, piping, effective stress, and excavation stability. Hydraulic and geotechnical calculations must use the same head reference.

\[i=\frac{\Delta h}{L}\]

![FIG-03-20-007: Flow net beneath a retaining or cutoff structure showing equipotential lines, flow lines, head loss, and exit gradient.](../figures/FIG-03-20-007-seepage-effective-stress-and-groundwater-structure-interaction.png)

### Worked Example 7

**Problem.** A 6 m head drop over 30 m gives gradient 0.20.

**Solution.** Hydraulic gradient is head loss per flow-path length: \(i=\Delta h/L\). Thus \(i=6/30=0.20\). The gradient is dimensionless because both quantities are lengths.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a well/seepage problem, first establish the aquifer geometry and hydraulic gradient, then use Darcy flow or the applicable radial-flow relation. If more than one well acts on the same point, compute each drawdown using the same datum and assumptions before superposing them.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook groundwater relation that matches the aquifer model—Darcy flow, confined flow, unconfined flow, or well drawdown. A remembered equation with a different logarithm base, geometry factor, or unit convention can change the answer materially.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 10; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-020-04` — Fitts, C. R. (2022). *Groundwater Science* (3rd ed.). Elsevier. ISBN 978-0-12-811455-1. Cited at publication/standard level; no page-level claim.
- `CIV-3-020-06` — Fitts, C. R. (2022). *Groundwater Science* (3rd ed.). Elsevier. ISBN 978-0-12-811455-1. Cited at publication/standard level; no page-level claim.
- `CIV-3-020-07` — Fitts, C. R. (2022). *Groundwater Science* (3rd ed.). Elsevier. ISBN 978-0-12-811455-1. Cited at publication/standard level; no page-level claim. Das, B. M. (2022). *Principles of Geotechnical Engineering* (10th ed.). Cengage. ISBN 978-0-357-42047-8. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

## Where This Goes Wrong

**Using Darcy groundwater flow without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using hydraulic conductivity without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using transmissivity without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using unconfined aquifer without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using well drawdown without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using well interference without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using seepage gradient without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| Darcy groundwater flow | Concept developed in §20.1; apply with that section's stated assumptions and units. |
| hydraulic conductivity | Concept developed in §20.2; apply with that section's stated assumptions and units. |
| transmissivity | Concept developed in §20.3; apply with that section's stated assumptions and units. |
| unconfined aquifer | Concept developed in §20.4; apply with that section's stated assumptions and units. |
| well drawdown | Concept developed in §20.5; apply with that section's stated assumptions and units. |
| well interference | Concept developed in §20.6; apply with that section's stated assumptions and units. |
| seepage gradient | Concept developed in §20.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **Darcy groundwater flow** and identify the principal quantity, relation, or decision it organizes.

2. Define **hydraulic conductivity** and identify the principal quantity, relation, or decision it organizes.

3. Define **transmissivity** and identify the principal quantity, relation, or decision it organizes.

4. Define **unconfined aquifer** and identify the principal quantity, relation, or decision it organizes.

5. Define **well drawdown** and identify the principal quantity, relation, or decision it organizes.

6. Define **well interference** and identify the principal quantity, relation, or decision it organizes.

7. Define **seepage gradient** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **Darcy groundwater flow**?

9. What assumption or unit error is most likely to cause a wrong result when applying **hydraulic conductivity**?

10. What assumption or unit error is most likely to cause a wrong result when applying **transmissivity**?

11. What assumption or unit error is most likely to cause a wrong result when applying **unconfined aquifer**?

12. What assumption or unit error is most likely to cause a wrong result when applying **well drawdown**?

13. What assumption or unit error is most likely to cause a wrong result when applying **well interference**?

14. What assumption or unit error is most likely to cause a wrong result when applying **seepage gradient**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **Darcy groundwater flow**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **hydraulic conductivity**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **transmissivity**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **unconfined aquifer**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **well drawdown**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **well interference**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **seepage gradient**?
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

1. **Darcy groundwater flow** is developed in §20.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **hydraulic conductivity** is developed in §20.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **transmissivity** is developed in §20.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **unconfined aquifer** is developed in §20.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **well drawdown** is developed in §20.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **well interference** is developed in §20.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **seepage gradient** is developed in §20.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **Darcy groundwater flow**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **hydraulic conductivity**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **transmissivity**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **unconfined aquifer**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **well drawdown**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **well interference**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **seepage gradient**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. Sketch the aquifer boundaries, saturated thickness, wells, observation point, and hydraulic-head datum first so the selected Darcy or well-flow model matches the actual geometry.

16. Use the Handbook groundwater relation when available because confined, unconfined, and radial-flow equations differ in geometry assumptions, logarithm form, and variable definitions.

17. Hydraulic conductivity may be given in m/day, ft/day, or m/s while head and radius use separate length units; convert to one consistent system before computing discharge or drawdown.

18. Check the hydraulic pattern: head should decline toward a pumping well, drawdown should be nonnegative for pumping, and computed flow direction should follow the hydraulic gradient.

19. **A.** For **Darcy law and hydraulic gradient**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Hydraulic conductivity, permeability tests, and anisotropy**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Aquifer transmissivity and confined flow**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Unconfined aquifers and water-table concepts**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Well drawdown and radial flow**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Multiple wells, superposition, and interference**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Seepage, effective stress, and groundwater-structure interaction**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Groundwater Flow, Aquifer Properties, Wells, and Drawdown, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Aquifer and multiple-well application details beyond Handbook equations are labeled learned material and supported by the reconciled groundwater reference instead of an invented Handbook location.



---

## Practice Problems

1. K=1e-4 m/s, i=0.02, A=50 m² gives Q=1e-4 m³/s.

2. Given measured volume, elapsed time, gradient, and area, solve for K with consistent units.

3. K=30 m/day and b=20 m gives T=600 m²/day.

4. At the water table, gauge pressure is approximately zero, so hydraulic head equals elevation head.

5. If static head is 120 ft and pumping head is 108 ft, drawdown is 12 ft.

6. Two wells causing 3 ft and 5 ft drawdown at a point produce about 8 ft total by superposition.

7. A 6 m head drop over 30 m gives gradient 0.20.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. **Independent check for §20.1.** Rework the problem from the stated givens rather than copying the worked-example result. Darcy's law is \(Q=KiA\). Substituting \(K=1\times10^{-4}\ \text{m/s}\), \(i=0.02\), and \(A=50\ \text{m}^2\) gives \(Q=(10^{-4})(0.02)(50)=1.0\times10^{-4}\ \text{m}^3/\text{s}\). **Check:** confirm the final magnitude and units against the physical meaning of §20.1 before accepting the answer.



2. **Independent check for §20.2.** Rework the problem from the stated givens rather than copying the worked-example result. For a constant-head style calculation, determine discharge rate from measured volume divided by elapsed time, then rearrange Darcy's law: \(K=Q/(iA)\). If a measured volume \(V\) is supplied instead of \(Q\), use \(K=V/(t\,iA)\). Convert time, length, and volume to one consistent unit system before substitution. **Check:** confirm the final magnitude and units against the physical meaning of §20.2 before accepting the answer.



3. **Independent check for §20.3.** Rework the problem from the stated givens rather than copying the worked-example result. Transmissivity is \(T=Kb\). With \(K=30\ \text{m/day}\) and saturated thickness \(b=20\ \text{m}\), \(T=30(20)=600\ \text{m}^2/\text{day}\). **Check:** confirm the final magnitude and units against the physical meaning of §20.3 before accepting the answer.



4. **Independent check for §20.4.** Rework the problem from the stated givens rather than copying the worked-example result. Hydraulic head is \(h=z+p/\gamma\). At the water table the pore pressure is atmospheric, so gauge pressure is approximately zero and \(p/\gamma=0\). Therefore the hydraulic head at the water table is approximately equal to the elevation head \(z\). **Check:** confirm the final magnitude and units against the physical meaning of §20.4 before accepting the answer.



5. **Independent check for §20.5.** Rework the problem from the stated givens rather than copying the worked-example result. Drawdown is the difference between static and pumping head: \(s=h_0-h(r)\). With \(h_0=120\ \text{ft}\) and pumping head \(108\ \text{ft}\), \(s=120-108=12\ \text{ft}\). **Check:** confirm the final magnitude and units against the physical meaning of §20.5 before accepting the answer.



6. **Independent check for §20.6.** Rework the problem from the stated givens rather than copying the worked-example result. Under linear confined-aquifer assumptions, drawdowns from multiple wells may be superposed. At the point of interest, \(s_{total}=3+5=8\ \text{ft}\). This approximation depends on the individual solutions being based on compatible aquifer assumptions. **Check:** confirm the final magnitude and units against the physical meaning of §20.6 before accepting the answer.



7. **Independent check for §20.7.** Rework the problem from the stated givens rather than copying the worked-example result. Hydraulic gradient is head loss per flow-path length: \(i=\Delta h/L\). Thus \(i=6/30=0.20\). The gradient is dimensionless because both quantities are lengths. **Check:** confirm the final magnitude and units against the physical meaning of §20.7 before accepting the answer.



8. Before accepting a groundwater flow, aquifer properties, wells, and drawdown result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Begin with **FE Civil specification Area 10** and the groundwater/Darcy relation cited in the ledger; use the external groundwater text only for the split-required aquifer and well-analysis detail.

10. For groundwater flow, aquifer properties, wells, and drawdown, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 10.

- **Darcy groundwater flow:** Darcy law and hydraulic gradient
- **hydraulic conductivity:** Hydraulic conductivity, permeability tests, and anisotropy
- **transmissivity:** Aquifer transmissivity and confined flow
- **unconfined aquifer:** Unconfined aquifers and water-table concepts
- **well drawdown:** Well drawdown and radial flow
- **well interference:** Multiple wells, superposition, and interference
- **seepage gradient:** Seepage, effective stress, and groundwater-structure interaction

---

## What's Next

**Chapter 03-21: Water Quality and Water/Wastewater Treatment for Civil Applications**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
