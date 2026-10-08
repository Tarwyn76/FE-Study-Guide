---
chapter: "03-22"
title: "Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-022-01, CIV-3-022-02, CIV-3-022-03, CIV-3-022-04, CIV-3-022-05, CIV-3-022-06, CIV-3-022-07]
routes: [civil]
status: drafted
---

# Chapter 03-22: Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** MECH-2C-026-04 · MECH-2C-024-03

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **22.1** Explain and apply **Structural idealization, supports, and degrees of freedom**.
* **22.2** Explain and apply **Determinacy and stability of beams and frames**.
* **22.3** Explain and apply **Truss determinacy and load path**.
* **22.4** Explain and apply **Dead, live, environmental, and moving loads**.
* **22.5** Explain and apply **Tributary area and gravity load paths**.
* **22.6** Explain and apply **Influence lines for reactions and member actions**.
* **22.7** Explain and apply **Load combinations and design-demand organization**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 22.1 Structural idealization, supports, and degrees of freedom

Structural analysis starts with the idealized model: supports, connectivity, load locations, and member behavior. A wrong support model invalidates every later calculation.

\[\sum F_x=0,\qquad \sum F_y=0,\qquad \sum M=0\]

![FIG-03-22-001: Beam and frame support symbols with corresponding restrained degrees of freedom.](../figures/FIG-03-22-001-structural-idealization-supports-and-degrees-of-freedom.png)

### Worked Example 1

**Problem.** A planar pin contributes two reaction components; a roller typically contributes one.

**Solution.** In a planar model, a pin support restrains translation in two directions and therefore contributes two reaction components, while an ideal roller restrains motion normal to its surface and contributes one. These reaction counts are the first step in checking external determinacy.

---

## 22.2 Determinacy and stability of beams and frames

Determinacy is not the same as stability. A structure can have the right reaction count yet still be geometrically unstable.

\[\text{unknown reactions/internal forces}\ \text{vs. independent equilibrium equations}\]

![FIG-03-22-002: Stable, externally unstable, and internally unstable planar structural examples.](../figures/FIG-03-22-002-determinacy-and-stability-of-beams-and-frames.png)

### Worked Example 2

**Problem.** Three independent reaction components can be statically determinate for a stable planar rigid body.

**Solution.** A planar rigid body provides three independent equilibrium equations: \(\sum F_x=0\), \(\sum F_y=0\), and \(\sum M=0\). A stable structure with three independent external reaction components can therefore be externally statically determinate; stability and reaction independence must still be verified.

---

## 22.3 Truss determinacy and load path

For a simple planar truss, the member-joint-reaction count is a useful screening rule. It does not replace a geometric stability check.

\[m+r\stackrel{?}{=}2j\]

![FIG-03-22-003: Planar truss with joints, members, supports, applied load, and highlighted load path.](../figures/FIG-03-22-003-truss-determinacy-and-load-path.png)

### Worked Example 3

**Problem.** If m=11, r=3, j=7, then m+r=14=2j, a candidate for determinate behavior.

**Solution.** For a simple planar truss, compare \(m+r\) with \(2j\). Here \(m+r=11+3=14\) and \(2j=2(7)=14\), so the counting criterion is satisfied. This is only a candidate for determinacy because an unstable member arrangement can satisfy the count and still be a mechanism.

---

## 22.4 Dead, live, environmental, and moving loads

Loads differ in source, variability, and distribution. FE problems may supply load combinations; use the stated combination rather than inventing code factors.

\[w_{\text{total}}=\sum w_i\]

![FIG-03-22-004: Building bay showing dead, live, roof, wind/lateral, and moving-load concepts with tributary areas.](../figures/FIG-03-22-004-dead-live-environmental-and-moving-loads.png)

### Worked Example 4

**Problem.** A 0.15 kip/ft self-weight and 0.60 kip/ft imposed load total 0.75 kip/ft before factors.

**Solution.** Combine the unfactored distributed loads on the same basis: \(w=0.15+0.60=0.75\ \text{kip/ft}\). The unfactored total is therefore **0.75 kip/ft**, equivalent to **750 lbf/ft**. Load factors, if required, are applied afterward according to the specified load combination rather than being mixed into the service-load sum.

---

## 22.5 Tributary area and gravity load paths

Tributary area converts distributed surface loading into beam, girder, or column loads. Follow the load path from slab to supports without double counting.

\[P=qA_t\]

![FIG-03-22-005: Floor framing plan with slab tributary strips to beams and tributary areas to columns.](../figures/FIG-03-22-005-tributary-area-and-gravity-load-paths.png)

### Worked Example 5

**Problem.** q=80 psf over 200 ft² produces 16 kip.

**Solution.** Tributary load is \(P=qA_t\). With \(q=80\ \text{lb/ft}^2\) and \(A_t=200\ \text{ft}^2\), \(P=16{,}000\ \text{lb}=16\ \text{kip}\). The tributary load is therefore **16 kip**, or **16,000 lbf**.

---

## 22.6 Influence lines for reactions and member actions

An influence line shows how a response quantity changes as a unit load moves across a structure. It is different from a shear or moment diagram for a fixed load.

\[\text{response}=\sum P_i\,y_i\]

![FIG-03-22-006: Simply supported beam with moving unit load and reaction/moment influence lines beneath it.](../figures/FIG-03-22-006-influence-lines-for-reactions-and-member-actions.png)

### Worked Example 6

**Problem.** A moving 10-kip load at influence ordinate 0.6 contributes 6 kip to the chosen response.

**Solution.** Influence-line response from a concentrated load is \(P y\). A \(10\)-kip load at ordinate \(0.6\) contributes \(10(0.6)=6\ \text{kip}\) to the selected reaction or internal-force response, with sign determined by the influence-line ordinate.

---

## 22.7 Load combinations and design-demand organization

Load combinations combine factored effects according to the governing design philosophy. On the FE exam, use factors provided by the applicable relation or problem statement.

\[U=\sum \gamma_i Q_i\]

![FIG-03-22-007: Load-combination worksheet linking load cases to factored design demand.](../figures/FIG-03-22-007-load-combinations-and-design-demand-organization.png)

### Worked Example 7

**Problem.** Apply each factor to the correct load type before combining effects.

**Solution.** Form the design demand by applying each prescribed load factor to the corresponding load effect and then summing algebraically. Dead, live, wind, seismic, and other effects are not interchangeable; the correct combination controls only after all applicable combinations are evaluated.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** For a moving-load structural problem, first establish the static load path and support reactions, then use the influence line to place the moving load where it maximizes the requested response. Determinacy and stability should be checked before any influence-line calculation.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook equilibrium, tributary-load, and influence-line relations in their stated sign convention. If a remembered structural formula assumes a different support idealization or positive-moment convention, the Handbook/model definition should govern the exam solution.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 11; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is retained because it is required by the FE Civil specification but needs engineering knowledge beyond what is printed in the Handbook. **Guide synthesis** connects those two sources into exam-oriented workflows and examples; it is not presented as Handbook text.

**External source support for split-required concepts:**
- `CIV-3-022-07` — American Society of Civil Engineers. (2022). *Minimum Design Loads and Associated Criteria for Buildings and Other Structures* (ASCE/SEI 7-22). ASCE. Cited at publication/standard level; no page-level claim.

No external source above is being used to replace the FE Reference Handbook. The external references support only the learned/application portion identified by `split_required: true`.

## Where This Goes Wrong

**Using structural idealization without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using structural determinacy without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using truss load path without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using structural loads without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using tributary area without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using influence line without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using design load combination without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| structural idealization | Concept developed in §22.1; apply with that section's stated assumptions and units. |
| structural determinacy | Concept developed in §22.2; apply with that section's stated assumptions and units. |
| truss load path | Concept developed in §22.3; apply with that section's stated assumptions and units. |
| structural loads | Concept developed in §22.4; apply with that section's stated assumptions and units. |
| tributary area | Concept developed in §22.5; apply with that section's stated assumptions and units. |
| influence line | Concept developed in §22.6; apply with that section's stated assumptions and units. |
| design load combination | Concept developed in §22.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **structural idealization** and identify the principal quantity, relation, or decision it organizes.

2. Define **structural determinacy** and identify the principal quantity, relation, or decision it organizes.

3. Define **truss load path** and identify the principal quantity, relation, or decision it organizes.

4. Define **structural loads** and identify the principal quantity, relation, or decision it organizes.

5. Define **tributary area** and identify the principal quantity, relation, or decision it organizes.

6. Define **influence line** and identify the principal quantity, relation, or decision it organizes.

7. Define **design load combination** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **structural idealization**?

9. What assumption or unit error is most likely to cause a wrong result when applying **structural determinacy**?

10. What assumption or unit error is most likely to cause a wrong result when applying **truss load path**?

11. What assumption or unit error is most likely to cause a wrong result when applying **structural loads**?

12. What assumption or unit error is most likely to cause a wrong result when applying **tributary area**?

13. What assumption or unit error is most likely to cause a wrong result when applying **influence line**?

14. What assumption or unit error is most likely to cause a wrong result when applying **design load combination**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **structural idealization**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **structural determinacy**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **truss load path**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **structural loads**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **tributary area**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **influence line**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **design load combination**?
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

1. **structural idealization** is developed in §22.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **structural determinacy** is developed in §22.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **truss load path** is developed in §22.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **structural loads** is developed in §22.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **tributary area** is developed in §22.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **influence line** is developed in §22.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **design load combination** is developed in §22.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **structural idealization**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **structural determinacy**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **truss load path**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **structural loads**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **tributary area**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **influence line**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **design load combination**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. Draw the free-body diagram and support/member layout first so reaction directions, load paths, joint forces, and the location of the requested influence response are unambiguous.

16. Use the Handbook equilibrium, tributary-load, and influence-line relations when provided because their sign and load conventions define the exam calculation.

17. Structural loads expressed in lb, lbf, kip, psf, or kN must be converted consistently before forces, distributed loads, reactions, and moments are combined.

18. Check global equilibrium and load path: reactions must balance applied forces and moments, and an influence-line response should have the sign expected from the load position.

19. **A.** For **Structural idealization, supports, and degrees of freedom**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

20. **A.** For **Determinacy and stability of beams and frames**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

21. **A.** For **Truss determinacy and load path**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

22. **A.** For **Dead, live, environmental, and moving loads**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

23. **A.** For **Tributary area and gravity load paths**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

24. **A.** For **Influence lines for reactions and member actions**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

25. **A.** For **Load combinations and design-demand organization**, the governing relation or workflow is valid only for its stated variables, units, physical model, and assumptions; those conditions must be checked before accepting the result.

26. **A.** In Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines, dimensional consistency and an independent physical check are the fastest ways to detect a unit, sign, magnitude, or modeling error before accepting the result.

27. **A.** Load-combination material beyond the Handbook's basic structural relations is labeled learned material and supported by ASCE/SEI 7 rather than attributed to an unverified Handbook page.



---

## Practice Problems

1. A planar pin contributes two reaction components; a roller typically contributes one.

2. Three independent reaction components can be statically determinate for a stable planar rigid body.

3. If m=11, r=3, j=7, then m+r=14=2j, a candidate for determinate behavior.

4. A 0.15 kip/ft self-weight and 0.60 kip/ft imposed load total 0.75 kip/ft before factors.

5. q=80 psf over 200 ft² produces 16 kip.

6. A moving 10-kip load at influence ordinate 0.6 contributes 6 kip to the chosen response.

7. Apply each factor to the correct load type before combining effects.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. **Independent check for §22.1.** Rework the problem from the stated givens rather than copying the worked-example result. In a planar model, a pin support restrains translation in two directions and therefore contributes two reaction components, while an ideal roller restrains motion normal to its surface and contributes one. These reaction counts are the first step in checking external determinacy. **Check:** confirm the final magnitude and units against the physical meaning of §22.1 before accepting the answer.



2. **Independent check for §22.2.** Rework the problem from the stated givens rather than copying the worked-example result. A planar rigid body provides three independent equilibrium equations: \(\sum F_x=0\), \(\sum F_y=0\), and \(\sum M=0\). A stable structure with three independent external reaction components can therefore be externally statically determinate; stability and reaction independence must still be verified. **Check:** confirm the final magnitude and units against the physical meaning of §22.2 before accepting the answer.



3. **Independent check for §22.3.** Rework the problem from the stated givens rather than copying the worked-example result. For a simple planar truss, compare \(m+r\) with \(2j\). Here \(m+r=11+3=14\) and \(2j=2(7)=14\), so the counting criterion is satisfied. This is only a candidate for determinacy because an unstable member arrangement can satisfy the count and still be a mechanism. **Check:** confirm the final magnitude and units against the physical meaning of §22.3 before accepting the answer.



4. **Independent check for §22.4.** Rework the problem from the stated givens rather than copying the worked-example result. Combine the unfactored distributed loads on the same basis: \(w=0.15+0.60=0.75\ \text{kip/ft}\). Load factors, if required, are applied afterward according to the specified load combination rather than being mixed into the service-load sum. **Check:** confirm the final magnitude and units against the physical meaning of §22.4 before accepting the answer.



5. **Independent check for §22.5.** Rework the problem from the stated givens rather than copying the worked-example result. Tributary load is \(P=qA_t\). With \(q=80\ \text{lb/ft}^2\) and \(A_t=200\ \text{ft}^2\), \(P=16{,}000\ \text{lb}=16\ \text{kip}\). **Check:** confirm the final magnitude and units against the physical meaning of §22.5 before accepting the answer.



6. **Independent check for §22.6.** Rework the problem from the stated givens rather than copying the worked-example result. Influence-line response from a concentrated load is \(P y\). A \(10\)-kip load at ordinate \(0.6\) contributes \(10(0.6)=6\ \text{kip}\) to the selected reaction or internal-force response, with sign determined by the influence-line ordinate. **Check:** confirm the final magnitude and units against the physical meaning of §22.6 before accepting the answer.



7. **Independent check for §22.7.** Rework the problem from the stated givens rather than copying the worked-example result. Form the design demand by applying each prescribed load factor to the corresponding load effect and then summing algebraically. Dead, live, wind, seismic, and other effects are not interchangeable; the correct combination controls only after all applicable combinations are evaluated. **Check:** confirm the final magnitude and units against the physical meaning of §22.7 before accepting the answer.



8. Before accepting a structural determinacy, stability, loads, load paths, and influence lines result, verify the dimensional units, the chapter-specific sign or direction convention, and that the selected model matches the stated geometry and boundary conditions.

9. Begin with **FE Civil specification Area 11** and the structural-equilibrium/influence material in the ledger; use ASCE/SEI 7 only for the reconciled load-combination portion.

10. For structural determinacy, stability, loads, load paths, and influence lines, a sketch makes the controlling geometry, direction, boundary, load/flow path, or sequence visible before algebra, which often reveals missing data or an impossible assumption immediately.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 11.

- **structural idealization:** Structural idealization, supports, and degrees of freedom
- **structural determinacy:** Determinacy and stability of beams and frames
- **truss load path:** Truss determinacy and load path
- **structural loads:** Dead, live, environmental, and moving loads
- **tributary area:** Tributary area and gravity load paths
- **influence line:** Influence lines for reactions and member actions
- **design load combination:** Load combinations and design-demand organization

---

## What's Next

**Chapter 03-23: Structural Analysis — Beams, Trusses, Frames, and Deflections**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
