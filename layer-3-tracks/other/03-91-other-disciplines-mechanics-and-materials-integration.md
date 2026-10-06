---
chapter: "03-91"
title: "Other Disciplines Mechanics and Materials Integration"
layer: 3
tier: null
track: other_disciplines
template: integration
ledger_ids: [OTH-3-091-01, OTH-3-091-02, OTH-3-091-03, OTH-3-091-04, OTH-3-091-05, OTH-3-091-06, OTH-3-091-07]
routes: [other_disciplines]
status: drafted
---

# Chapter 03-91: Other Disciplines Mechanics and Materials Integration

> *"The Other Disciplines exam is less about owning one specialty and more about recognizing which engineering model governs the next problem."*

---

## Before You Start

**Prerequisites:** MECH-2C-023-01 · MECH-2C-022-03 · MAT-2B-016-01 · MEC-3-077-01 · MEC-3-078-01

**Route:** FE Other Disciplines. This is a Layer 3 integration chapter.

**Ownership rule:** This chapter intentionally does **not** create new owners for statics, dynamics, materials, fluids, thermodynamics, electrical engineering, safety, economics, or other already-registered topics. Its concept atoms own only integration, transfer, and exam-strategy skills.

**Time:** About 75–100 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

This chapter develops **Other Disciplines Mechanics and Materials Integration** as a synthesis layer over prior canonical concepts. The FE Other Disciplines specification spans mathematics, probability/statistics, chemistry, instrumentation/controls, ethics, safety, economics, statics, dynamics, strength of materials, materials, fluid mechanics, basic electrical engineering, and thermodynamics/heat transfer. The track therefore emphasizes selection, transfer, and verification rather than duplicated ownership.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **91.1** Apply **From word problem to free-body diagram and load path** in mixed FE problems.
* **91.2** Apply **Coupling statics to internal forces and stress** in mixed FE problems.
* **91.3** Apply **Coupling kinematics, dynamics, work-energy, and power** in mixed FE problems.
* **91.4** Apply **Stress transformation and failure screening** in mixed FE problems.
* **91.5** Apply **Materials properties tied to mechanical performance** in mixed FE problems.
* **91.6** Apply **Columns, stability, and geometric nonlinearity screening** in mixed FE problems.
* **91.7** Apply **Integrated mechanics reasonableness and unit strategy** in mixed FE problems.

---

## Notation Used Here

Keep the notation of the underlying canonical discipline. When moving between domains, state the intermediate quantity, its units, and which model produced it before using it as the next model's input.

---

## 91.1 From word problem to free-body diagram and load path

Other Disciplines mechanics questions often combine statics, dynamics, and strength of materials in one prompt. The first task is deciding what body to isolate, which loads are external, and whether acceleration is negligible.

\[\text{physical system}\rightarrow\text{FBD}\rightarrow\text{equilibrium/dynamics}\rightarrow\text{stress/deformation check}\]

![FIG-03-91-001: Word problem transformed into system boundary, FBD, load path, equilibrium/dynamics choice, and stress/deformation checks.](../figures/FIG-03-91-001-from-word-problem-to-free-body-diagram-and-load-path.png)

### Worked Example 1

**Problem.** A supported bracket with an attached moving mass may require a static support-reaction model for the bracket plus a dynamic force model for the mass.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §91.1.

---

## 91.2 Coupling statics to internal forces and stress

Support reactions do not finish the problem. Convert external loads into internal axial force, shear, bending moment, or torque at the critical section before choosing a stress relation.

\[\text{external loads}\rightarrow V,M,T,N\rightarrow\sigma,\tau\]

![FIG-03-91-002: Cantilever from applied load through reactions to shear/moment diagrams and critical-section stress distribution.](../figures/FIG-03-91-002-coupling-statics-to-internal-forces-and-stress.png)

### Worked Example 2

**Problem.** A transverse load on a cantilever creates both shear and bending moment; bending stress often governs near the fixed end.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §91.2.

---

## 91.3 Coupling kinematics, dynamics, work-energy, and power

The same motion can often be solved by force-acceleration, impulse-momentum, or work-energy. Choose the method that minimizes unknowns and matches the requested quantity.

\[\sum\mathbf F=m\mathbf a,\qquad T_1+V_1+W_{1\to2}=T_2+V_2,\qquad P=\mathbf F\cdot\mathbf v\]

![FIG-03-91-003: Decision tree comparing Newton's second law, work-energy, impulse-momentum, and power for a moving mechanical system.](../figures/FIG-03-91-003-coupling-kinematics-dynamics-work-energy-and-power.png)

### Worked Example 3

**Problem.** If only speeds before and after a conservative motion are needed, work-energy may be shorter than solving acceleration as a function of position.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §91.3.

---

## 91.4 Stress transformation and failure screening

Other Disciplines questions may stop at stress transformation or continue into yielding, fracture, fatigue, or buckling. Do not compare a raw component stress to the wrong material limit.

\[\text{multiaxial stress}\rightarrow\text{principal stresses/von Mises}\rightarrow\text{allowable or failure criterion}\]

![FIG-03-91-004: Combined loading mapped through stress state, Mohr/principal stresses, ductile/brittle criteria, fatigue and buckling branches.](../figures/FIG-03-91-004-stress-transformation-and-failure-screening.png)

### Worked Example 4

**Problem.** A ductile shaft under bending and torsion should be reduced to an appropriate equivalent-stress measure before comparison with yield strength.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §91.4.

---

## 91.5 Materials properties tied to mechanical performance

Material tables become useful when tied to a failure or performance mode. Stiffness, strength, toughness, density, thermal expansion, corrosion behavior, and temperature capability answer different design questions.

\[\text{response}=f(E,G,\nu,S_y,S_u,K_{IC},\alpha,\rho,\text{environment})\]

![FIG-03-91-005: Material-property map linking modulus to deflection, yield to static strength, toughness to fracture, alpha to thermal strain, and density to weight.](../figures/FIG-03-91-005-materials-properties-tied-to-mechanical-performance.png)

### Worked Example 5

**Problem.** Changing from steel to aluminum may reduce mass while increasing elastic deflection if geometry is unchanged.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §91.5.

---

## 91.6 Columns, stability, and geometric nonlinearity screening

A member can fail by instability before material yield. Slenderness, effective length, end conditions, and stiffness determine whether Euler-style buckling is relevant.

\[P_{cr}=\frac{\pi^2EI}{(KL)^2}\]

![FIG-03-91-006: Short, intermediate, and slender compression members with yielding versus buckling screening.](../figures/FIG-03-91-006-columns-stability-and-geometric-nonlinearity-screening.png)

### Worked Example 6

**Problem.** Doubling effective length reduces ideal Euler buckling load by a factor of four.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §91.6.

---

## 91.7 Integrated mechanics reasonableness and unit strategy

The Other Disciplines route rewards fast switching among mechanics topics. A compact verification routine prevents using a correct formula on the wrong body, axis, or failure mode.

\[\text{answer check}=\text{units}+\text{sign}+\text{load path}+\text{limiting case}+\text{failure mode}\]

![FIG-03-91-007: Mechanics synthesis checklist covering FBD, reactions, internal resultants, constitutive law, failure mode, and units.](../figures/FIG-03-91-007-integrated-mechanics-reasonableness-and-unit-strategy.png)

### Worked Example 7

**Problem.** A negative support reaction can be physically valid, but only if the support can actually act in that direction.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §91.7.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A mixed question contains electrical, mechanical, and economic information. Must every datum be used?

**Solution.** No. First identify the requested quantity and governing model. Use only the data needed for the current stage, then carry the resulting intermediate quantity—clearly labeled with units—into the next stage if required.

### Worked Example 9

**Problem.** You find a familiar equation in memory but a different-looking form in the FE Reference Handbook. What should you do?

**Solution.** Use the Handbook form after checking its definitions and assumptions. Do not force a remembered formula onto a problem merely because it resembles the topic.

---

## As the Handbook States It

**Primary source basis:** FE Other Disciplines CBT specification, printed pp. 498–500. Unlike the six discipline-specific FE routes, Other Disciplines has no dedicated discipline section in Handbook 10.6; it relies on the general Handbook sections across the book.

**Source boundary:** The integration workflow, classification strategy, and cross-domain transfer methods are guide-developed. Underlying equations remain owned and sourced by their canonical earlier chapters.

---

## Where This Goes Wrong

**Re-owning a shared concept.** This track must point back to the existing owner rather than creating a second independent definition of the same method.

**Using every number because it was supplied.** Mixed FE questions can include distractors; the requested quantity and governing model determine relevance.

**Losing units at domain boundaries.** Intermediate power, force, flow, concentration, temperature, or cost quantities must carry explicit units into the next calculation.

**Treating the Handbook search as the first reasoning step.** Classify the physics/discipline first, then search targeted terms.

---

## Key Terms

| Term | Integration role |
|---|---|
| cross-domain mechanics model selection | Synthesis concept in §91.1; coordinates prior canonical owners without duplicating them. |
| load-path-to-stress integration | Synthesis concept in §91.2; coordinates prior canonical owners without duplicating them. |
| motion-force-energy integration | Synthesis concept in §91.3; coordinates prior canonical owners without duplicating them. |
| integrated failure screening | Synthesis concept in §91.4; coordinates prior canonical owners without duplicating them. |
| mechanics-materials linkage | Synthesis concept in §91.5; coordinates prior canonical owners without duplicating them. |
| cross-domain stability check | Synthesis concept in §91.6; coordinates prior canonical owners without duplicating them. |
| mechanics synthesis check | Synthesis concept in §91.7; coordinates prior canonical owners without duplicating them. |

---

## Review Questions

### Conceptual and Applied

1. Define **cross-domain mechanics model selection** and explain what cross-domain decision or transfer skill it supports.

2. Define **load-path-to-stress integration** and explain what cross-domain decision or transfer skill it supports.

3. Define **motion-force-energy integration** and explain what cross-domain decision or transfer skill it supports.

4. Define **integrated failure screening** and explain what cross-domain decision or transfer skill it supports.

5. Define **mechanics-materials linkage** and explain what cross-domain decision or transfer skill it supports.

6. Define **cross-domain stability check** and explain what cross-domain decision or transfer skill it supports.

7. Define **mechanics synthesis check** and explain what cross-domain decision or transfer skill it supports.

8. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain mechanics model selection**?

9. What is the most important assumption, boundary, unit, or prior-concept check before applying **load-path-to-stress integration**?

10. What is the most important assumption, boundary, unit, or prior-concept check before applying **motion-force-energy integration**?

11. What is the most important assumption, boundary, unit, or prior-concept check before applying **integrated failure screening**?

12. What is the most important assumption, boundary, unit, or prior-concept check before applying **mechanics-materials linkage**?

13. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain stability check**?

14. What is the most important assumption, boundary, unit, or prior-concept check before applying **mechanics synthesis check**?

15. Why should an Other Disciplines problem be classified before searching the Handbook?

16. Why is cross-domain synthesis different from creating a new copy of a previously owned concept?

17. What should you do when two equations look plausible but use different assumptions or variable definitions?

18. Why should every final answer receive a units, sign, magnitude, and physical/ethical feasibility check?

### Multiple Choice

19. Which statement is most accurate for **cross-domain mechanics model selection**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

20. Which statement is most accurate for **load-path-to-stress integration**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

21. Which statement is most accurate for **motion-force-energy integration**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

22. Which statement is most accurate for **integrated failure screening**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

23. Which statement is most accurate for **mechanics-materials linkage**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

24. Which statement is most accurate for **cross-domain stability check**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

25. Which statement is most accurate for **mechanics synthesis check**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

26. Which statement is most accurate for **cross-domain mechanics model selection**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

27. Which statement is most accurate for **load-path-to-stress integration**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation


---

## Answer Key with Explanations

1. **cross-domain mechanics model selection** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

2. **load-path-to-stress integration** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

3. **motion-force-energy integration** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

4. **integrated failure screening** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

5. **mechanics-materials linkage** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

6. **cross-domain stability check** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

7. **mechanics synthesis check** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

8. For **cross-domain mechanics model selection**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

9. For **load-path-to-stress integration**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

10. For **motion-force-energy integration**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

11. For **integrated failure screening**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

12. For **mechanics-materials linkage**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

13. For **cross-domain stability check**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

14. For **mechanics synthesis check**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

15. Classification narrows the search space and prevents using a familiar equation from the wrong discipline or physical model.

16. The canonical concept already exists in an earlier layer/track; the integration atom teaches when and how to reuse it in a mixed problem.

17. Compare variable definitions, units, boundary conditions, and operating assumptions. Use the relation that matches the actual problem and Handbook context.

18. These checks catch wrong-domain solutions, hidden conversion errors, impossible signs or efficiencies, and decisions that violate physical, safety, or professional constraints.

19. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

20. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

21. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

22. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

23. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

24. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

25. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

26. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

27. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.


---

## Practice Problems

1. A supported bracket with an attached moving mass may require a static support-reaction model for the bracket plus a dynamic force model for the mass.

2. A transverse load on a cantilever creates both shear and bending moment; bending stress often governs near the fixed end.

3. If only speeds before and after a conservative motion are needed, work-energy may be shorter than solving acceleration as a function of position.

4. A ductile shaft under bending and torsion should be reduced to an appropriate equivalent-stress measure before comparison with yield strength.

5. Changing from steel to aluminum may reduce mass while increasing elastic deflection if geometry is unchanged.

6. Doubling effective length reduces ideal Euler buckling load by a factor of four.

7. A negative support reaction can be physically valid, but only if the support can actually act in that direction.

8. For a mixed-domain problem, write the sequence of discipline models you would use and the intermediate quantity passed between each.

9. State the FE Other Disciplines specification page range and explain why there is no dedicated Other Disciplines Handbook section.

10. Give one fast check that would cause you to reject an otherwise algebraically consistent FE answer.


---

## Practice Problem Solutions

1. Use §91.1. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

2. Use §91.2. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

3. Use §91.3. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

4. Use §91.4. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

5. Use §91.5. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

6. Use §91.6. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

7. Use §91.7. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

8. Example structure: electrical input power → motor efficiency → shaft power → pump/fluid model → operating cost. Every arrow must carry a defined quantity and units.

9. The FE Other Disciplines specification is printed on pp. 498–500. The route has no dedicated discipline chapter in Handbook 10.6, so examinees use the relevant general sections instead.

10. Reject answers with impossible units, efficiencies above 100% where not physically meaningful, negative absolute quantities, violated support/device states, broken conservation, or unsafe/unethical implementation assumptions.

---

## Quick Reference

**Source anchor:** FE Other Disciplines CBT specification, printed pp. 498–500.

- **cross-domain mechanics model selection:** From word problem to free-body diagram and load path
- **load-path-to-stress integration:** Coupling statics to internal forces and stress
- **motion-force-energy integration:** Coupling kinematics, dynamics, work-energy, and power
- **integrated failure screening:** Stress transformation and failure screening
- **mechanics-materials linkage:** Materials properties tied to mechanical performance
- **cross-domain stability check:** Columns, stability, and geometric nonlinearity screening
- **mechanics synthesis check:** Integrated mechanics reasonableness and unit strategy

---

## What's Next

**Chapter 03-92: Other Disciplines Thermal, Fluid, Heat-Transfer, and HVAC Integration**

For the Other Disciplines route, keep practicing the same transfer loop: classify the problem, locate the canonical model, use the Handbook deliberately, solve with explicit units, then verify the result across domain boundaries.

— Your Mentor
