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

**Solution.** Treat the bracket and moving mass as coupled but distinct models. Draw the bracket FBD and solve its support reactions from equilibrium; represent the mass interaction using the appropriate dynamic force from its acceleration. Transfer only the interface force between models, with one consistent sign convention.

---

## 91.2 Coupling statics to internal forces and stress

Support reactions do not finish the problem. Convert external loads into internal axial force, shear, bending moment, or torque at the critical section before choosing a stress relation.

\[\text{external loads}\rightarrow V,M,T,N\rightarrow\sigma,\tau\]

![FIG-03-91-002: Cantilever from applied load through reactions to shear/moment diagrams and critical-section stress distribution.](../figures/FIG-03-91-002-coupling-statics-to-internal-forces-and-stress.png)

### Worked Example 2

**Problem.** A transverse load on a cantilever creates both shear and bending moment; bending stress often governs near the fixed end.

**Solution.** For the cantilever, first recover the internal resultants at the section of interest. A transverse tip load produces shear \(V\) and bending moment \(M\); then use the applicable shear- and bending-stress relations. Near the fixed end, \(M\) is largest, so bending stress commonly controls.

---

## 91.3 Coupling kinematics, dynamics, work-energy, and power

The same motion can often be solved by force-acceleration, impulse-momentum, or work-energy. Choose the method that minimizes unknowns and matches the requested quantity.

\[\sum\mathbf F=m\mathbf a,\qquad T_1+V_1+W_{1\to2}=T_2+V_2,\qquad P=\mathbf F\cdot\mathbf v\]

![FIG-03-91-003: Decision tree comparing Newton's second law, work-energy, impulse-momentum, and power for a moving mechanical system.](../figures/FIG-03-91-003-coupling-kinematics-dynamics-work-energy-and-power.png)

### Worked Example 3

**Problem.** If only speeds before and after a conservative motion are needed, work-energy may be shorter than solving acceleration as a function of position.

**Solution.** Work-energy is efficient when the unknown is speed rather than the time history. Write \(T_1+V_1+W_{nc}=T_2+V_2\), include only forces that do work in the chosen system, and solve directly for the final speed instead of first finding \(a(x)\) and integrating the motion.

---

## 91.4 Stress transformation and failure screening

Other Disciplines questions may stop at stress transformation or continue into yielding, fracture, fatigue, or buckling. Do not compare a raw component stress to the wrong material limit.

\[\text{multiaxial stress}\rightarrow\text{principal stresses/von Mises}\rightarrow\text{allowable or failure criterion}\]

![FIG-03-91-004: Combined loading mapped through stress state, Mohr/principal stresses, ductile/brittle criteria, fatigue and buckling branches.](../figures/FIG-03-91-004-stress-transformation-and-failure-screening.png)

### Worked Example 4

**Problem.** A ductile shaft under bending and torsion should be reduced to an appropriate equivalent-stress measure before comparison with yield strength.

**Solution.** Bending creates normal stress and torque creates shear stress. Evaluate both at the same material point, transform or combine them into the required principal/von-Mises measure, and compare that equivalent stress with the ductile yield criterion using the stated factor of safety.

---

## 91.5 Materials properties tied to mechanical performance

Material tables become useful when tied to a failure or performance mode. Stiffness, strength, toughness, density, thermal expansion, corrosion behavior, and temperature capability answer different design questions.

\[\text{response}=f(E,G,\nu,S_y,S_u,K_{IC},\alpha,\rho,\text{environment})\]

![FIG-03-91-005: Material-property map linking modulus to deflection, yield to static strength, toughness to fracture, alpha to thermal strain, and density to weight.](../figures/FIG-03-91-005-materials-properties-tied-to-mechanical-performance.png)

### Worked Example 5

**Problem.** Changing from steel to aluminum may reduce mass while increasing elastic deflection if geometry is unchanged.

**Solution.** With unchanged geometry and load, elastic deflection scales roughly with \(1/E\), while mass scales with density. Aluminum therefore can reduce weight because of lower \(
ho\) yet increase deflection because its \(E\) is substantially lower than steel's; strength must be checked separately.

---

## 91.6 Columns, stability, and geometric nonlinearity screening

A member can fail by instability before material yield. Slenderness, effective length, end conditions, and stiffness determine whether Euler-style buckling is relevant.

\[P_{cr}=\frac{\pi^2EI}{(KL)^2}\]

![FIG-03-91-006: Short, intermediate, and slender compression members with yielding versus buckling screening.](../figures/FIG-03-91-006-columns-stability-and-geometric-nonlinearity-screening.png)

### Worked Example 6

**Problem.** Doubling effective length reduces ideal Euler buckling load by a factor of four.

**Solution.** Euler buckling gives \(P_{cr}=\pi^2EI/(KL)^2\). Replacing \(KL\) by \(2KL\) makes the denominator four times larger, so the ideal critical load becomes \(P_{cr}/4\). This is a stability effect, not a material-yield calculation.

---

## 91.7 Integrated mechanics reasonableness and unit strategy

The Other Disciplines route rewards fast switching among mechanics topics. A compact verification routine prevents using a correct formula on the wrong body, axis, or failure mode.

\[[\mathrm{LHS}]=[\mathrm{RHS}],\qquad \mathbf R_F=\sum\mathbf F-m\mathbf a,\qquad R_M=\sum M_G-I_G\alpha\]

![FIG-03-91-007: Mechanics synthesis checklist covering FBD, reactions, internal resultants, constitutive law, failure mode, and units.](../figures/FIG-03-91-007-integrated-mechanics-reasonableness-and-unit-strategy.png)

### Worked Example 7

**Problem.** A negative support reaction can be physically valid, but only if the support can actually act in that direction.

**Solution.** The algebraic sign of a reaction is referenced to the assumed direction. A negative result means the actual force acts opposite that assumption; it is physically admissible only if the support can supply force in that direction. A cable or unilateral contact, for example, cannot push.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A mixed question contains electrical, mechanical, and economic information. Must every datum be used?

**Solution.** No. In a mechanics/materials synthesis question, keep only data that affect the current free-body, motion, stress, deformation, stability, or material check. For example, motor voltage is irrelevant to a bracket stress calculation unless it is first needed to determine the transmitted mechanical load.

### Worked Example 9

**Problem.** You find a familiar equation in memory but a different-looking form in the FE Reference Handbook. What should you do?

**Solution.** Use the Handbook form that matches the selected mechanics model and its sign/variable definitions. A memorized beam, energy, or failure equation is acceptable only after you verify that its loading case, coordinate system, and assumptions are identical to the Handbook/problem setup.

---

## As the Handbook States It

**Primary source basis:** FE Other Disciplines CBT specification, printed pp. 498–500. Unlike the six discipline-specific FE routes, Other Disciplines has no dedicated discipline section in Handbook 10.6; it relies on the general Handbook sections across the book.

**Source boundary:** **FE-Handbook-supported** material consists of the underlying equations, tables, definitions, and discipline models located in the FE Reference Handbook and recorded in the ledger. **Externally supported** material covers Other Disciplines specification knowledge, application context, standards, and integration details that are not fully developed in the Handbook. **Guide synthesis** is the cross-domain classification, transfer, verification, and exam-strategy workflow created for this supplemental guide; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Hibbeler, R. C. (2022). *Engineering Mechanics: Statics & Dynamics* (15th ed.). Pearson. ISBN 978-0-13-751472-4. Supporting scope: Free-body diagrams, equilibrium, internal resultants, kinematics, kinetics, work-energy, impulse-momentum, and engineering mechanics modeling.
- Hibbeler, R. C. (2022). *Mechanics of Materials* (11th ed.). Pearson. ISBN 978-0-13-760561-3. Supporting scope: Axial/torsional/bending stress, stress transformation, combined loading, deflection, columns, buckling, and mechanics-of-materials design checks.
- Nisbett, K. J., & Budynas, R. G. *Shigley's Mechanical Engineering Design* (2024 Release). McGraw Hill. ISBN 978-1-265-47269-6. Supporting scope: Failure theories, fatigue, materials/design properties, stress concentrations, stability screening, and machine-design context.
- Callister, W. D., Jr., & Rethwisch, D. G. (2018). *Materials Science and Engineering: An Introduction* (10th ed.). Wiley. ISBN 978-1-119-40549-8. Supporting scope: Structure-property relations for metals, ceramics, polymers, and composites; mechanical properties, processing, and materials selection.

Because Other Disciplines intentionally integrates material owned by earlier chapters, external references support the learned/application and cross-domain portions only. The FE Reference Handbook remains the exam reference, and the ledger retains the canonical Handbook locations for the underlying equations.

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

15. Classify the problem first so you know whether the governing object is a particle, rigid body, beam/shaft, column, or material failure state. That classification determines the correct Handbook section and prevents combining equations from incompatible mechanical models.

16. The underlying statics, dynamics, stress, and materials relations already have canonical owners earlier in the guide. This chapter adds the transfer logic between them—such as reaction → internal force → stress—not a second independent version of those equations.

17. Compare the free-body definition, coordinate/sign convention, loading case, constitutive assumptions, and variable meanings. Use the relation whose assumptions match the actual structure or motion, even if another remembered form looks algebraically familiar.

18. Mechanics answers can be numerically tidy yet physically impossible. Units, reaction direction, load path, stress sign/magnitude, stability, and material limits provide independent checks that expose the wrong body, wrong section, or wrong failure mode.

19. **A.** Start by choosing the correct physical body and free-body diagram, then decide whether equilibrium or dynamics supplies the interface loads. Cross-domain mechanics begins with the load path, not with a stress equation.

20. **A.** External reactions are not yet stresses. Resolve them into internal \(N,V,M,T\) at the section and only then apply the matching normal/shear stress relation with the actual cross-section properties.

21. **A.** Kinematics describes motion, dynamics relates forces to acceleration, and work-energy connects force work to speed/energy. Choose the shortest model that directly contains the requested quantity and known data.

22. **A.** Multiaxial stress must be reduced using the material-appropriate failure measure. For a ductile metal, principal stresses or von Mises stress are commonly compared with yield after the component stresses are formed consistently.

23. **A.** Mechanical response depends on both geometry/load and properties such as \(E,G,
u,S_y,S_u,K_{IC},\alpha,
ho\). A material substitution can improve one metric, such as mass, while degrading stiffness, fatigue, fracture, or thermal response.

24. **A.** Column buckling is a stability limit governed strongly by \(EI\), end condition, and effective length. A member can buckle at a load below its material yield load, so strength and stability must be checked separately.

25. **A.** A synthesis check verifies dimensions, sign, support/load-path feasibility, limiting behavior, and the relevant failure mode. Passing the algebra alone is not enough when the result contradicts the physical restraints or material behavior.

26. **A.** When several mechanics routes are possible, choose the body and unknown first, then use equilibrium, dynamics, or energy only if it actually contains the requested quantity and available data. This prevents solving the wrong mechanical subsystem correctly.

27. **A.** The load-path chain should be explicit: applied load → support/internal resultant → section stress/deformation → failure or serviceability check. Skipping an intermediate step is a common way to attach the right stress formula to the wrong load.


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

1. Apply the §91.1 model independently. Start by choosing the correct physical body and free-body diagram, then decide whether equilibrium or dynamics supplies the interface loads. Cross-domain mechanics begins with the load path, not with a stress equation. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

2. Apply the §91.2 model independently. External reactions are not yet stresses. Resolve them into internal \(N,V,M,T\) at the section and only then apply the matching normal/shear stress relation with the actual cross-section properties. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

3. Apply the §91.3 model independently. Kinematics describes motion, dynamics relates forces to acceleration, and work-energy connects force work to speed/energy. Choose the shortest model that directly contains the requested quantity and known data. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

4. Apply the §91.4 model independently. Multiaxial stress must be reduced using the material-appropriate failure measure. For a ductile metal, principal stresses or von Mises stress are commonly compared with yield after the component stresses are formed consistently. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

5. Apply the §91.5 model independently. Mechanical response depends on both geometry/load and properties such as \(E,G,
u,S_y,S_u,K_{IC},\alpha,
ho\). A material substitution can improve one metric, such as mass, while degrading stiffness, fatigue, fracture, or thermal response. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

6. Apply the §91.6 model independently. Column buckling is a stability limit governed strongly by \(EI\), end condition, and effective length. A member can buckle at a load below its material yield load, so strength and stability must be checked separately. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

7. Apply the §91.7 model independently. A synthesis check verifies dimensions, sign, support/load-path feasibility, limiting behavior, and the relevant failure mode. Passing the algebra alone is not enough when the result contradicts the physical restraints or material behavior. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

8. Write the mechanics dependency chain explicitly—for example support equilibrium → section \(N,V,M,T\) → stress state → failure/stability/material check. Record the interface force, moment, stress, or displacement passed between stages with sign and units.

9. Use the FE Other Disciplines specification at printed pp. 498–500 for scope. There is no separate Other Disciplines formula section because this route intentionally draws equations from the general discipline sections of the FE Reference Handbook.

10. Reject the answer immediately if the support/load path is impossible—for example a cable carrying compression, a contact surface pulling, or an equilibrium solution whose forces do not close.

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
