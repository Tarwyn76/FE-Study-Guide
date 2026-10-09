---
chapter: "03-79"
title: "Manufacturing Processes, Material Processing, Heat Treatment, and Selection"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-079-01, MEC-3-079-02, MEC-3-079-03, MEC-3-079-04, MEC-3-079-05, MEC-3-079-06, MEC-3-079-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-79: Manufacturing Processes, Material Processing, Heat Treatment, and Selection

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MAT-2B-016-01

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Manufacturing Processes, Material Processing, Heat Treatment, and Selection**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **79.1** Explain and apply **Casting process selection and defects**.
* **79.2** Explain and apply **Machining mechanics and cutting parameters**.
* **79.3** Explain and apply **Taylor tool-life relation**.
* **79.4** Explain and apply **Metal forming and plastic deformation**.
* **79.5** Explain and apply **Phase diagrams and heat treatment**.
* **79.6** Explain and apply **Polymers, composites, and engineered materials**.
* **79.7** Explain and apply **Materials selection, corrosion, and manufacturability**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 79.1 Casting process selection and defects

Casting creates near-net shapes from molten material. Mold type, solidification, feeding, and cooling affect shrinkage, porosity, and surface quality.

\[\text{process choice}=f(\text{alloy, size, geometry, surface, quantity})\]

![FIG-03-79-001: Sand casting with sprue, runner, gate, mold cavity, riser, and common defect locations.](../figures/FIG-03-79-001-casting-process-selection-and-defects.png)

### Worked Example 1

**Problem.** A riser supplies liquid metal to compensate for solidification shrinkage.

**Solution.** A riser is a reservoir of liquid metal connected to the casting. As the casting contracts during solidification, the riser feeds liquid into the shrinking region so the casting is less likely to form internal shrinkage voids.

---

## 79.2 Machining mechanics and cutting parameters

Machining performance depends on cutting speed, feed, depth of cut, tool/work material, rigidity, and coolant. Increasing removal rate can reduce tool life or quality.

\[V=\pi DN,\qquad \mathrm{MRR}\sim\text{speed}\times\text{feed}\times\text{depth}\]

![FIG-03-79-002: Turning operation with cutting speed, feed, depth of cut, chip, tool, and workpiece.](../figures/FIG-03-79-002-machining-mechanics-and-cutting-parameters.png)

### Worked Example 2

**Problem.** Doubling spindle speed doubles surface speed for the same diameter.

**Solution.** Surface speed is \(V=\pi DN\). Holding diameter \(D\) fixed while doubling spindle speed \(N\) gives \(V_2/V_1=2\), so the cutting speed **doubles**.

---

## 79.3 Taylor tool-life relation

Taylor's relation captures the strong tradeoff between cutting speed and tool life for a given tool/work combination.

\[VT^n=C\]

![FIG-03-79-003: Log-log cutting speed versus tool life with Taylor slope and operating points.](../figures/FIG-03-79-003-taylor-tool-life-relation.png)

### Worked Example 3

**Problem.** If n>0, increasing V decreases T.

**Solution.** From \(VT^n=C\), \(T=(C/V)^{1/n}\). For \(n>0\), increasing cutting speed increases the denominator and therefore **decreases tool life**, often strongly because the exponent \(1/n\) is large.

---

## 79.4 Metal forming and plastic deformation

Rolling, forging, extrusion, and drawing reshape ductile metals through plastic flow. Friction, strain path, temperature, and work hardening matter.

\[\text{forming requires stress beyond yield while controlling fracture and springback}\]

![FIG-03-79-004: Rolling, forging, extrusion, and drawing process schematics.](../figures/FIG-03-79-004-metal-forming-and-plastic-deformation.png)

### Worked Example 4

**Problem.** Hot working generally reduces flow stress and can permit larger deformation.

**Solution.** Hot working occurs at elevated temperature where recovery/recrystallization can reduce flow stress and permit larger plastic strains before fracture. The benefit is not free: oxidation, scale, dimensional accuracy, and grain/microstructure effects still matter.

---

## 79.5 Phase diagrams and heat treatment

Equilibrium phase diagrams show stable phase fields; heat treatment deliberately controls time-temperature history to obtain desired microstructures and properties.

\[\text{microstructure}=f(\text{composition, temperature, time, cooling path})\]

![FIG-03-79-005: Simplified binary phase diagram alongside heat-treatment time-temperature path.](../figures/FIG-03-79-005-phase-diagrams-and-heat-treatment.png)

### Worked Example 5

**Problem.** Rapid quenching can suppress equilibrium transformation and create harder microstructures in appropriate steels.

**Solution.** In suitable steels, rapid quenching suppresses slower diffusional transformations and can form a hard nonequilibrium microstructure such as martensite. The result depends on alloy composition, austenitizing condition, section size, cooling rate, and subsequent tempering.

---

## 79.6 Polymers, composites, and engineered materials

Mechanical design may favor polymers or composites for corrosion resistance, weight, damping, manufacturability, or directional properties.

\[\text{specific property}=\frac{\text{property}}{\rho}\]

![FIG-03-79-006: Material selection map comparing metals, polymers, ceramics, and composites by stiffness, density, temperature, and cost.](../figures/FIG-03-79-006-polymers-composites-and-engineered-materials.png)

### Worked Example 6

**Problem.** A composite may have high specific stiffness even if its absolute modulus is below steel.

**Solution.** Specific stiffness is \(E/\rho\). A composite with a lower absolute modulus than steel can still have a larger stiffness-to-weight ratio if its density is sufficiently lower; this is why specific properties matter in weight-sensitive design.

---

## 79.7 Materials selection, corrosion, and manufacturability

A material is acceptable only when its properties, environment, processing route, joining method, and lifecycle requirements are compatible.

\[\text{selection}=f(\text{loads, environment, process, life, cost, availability})\]

![FIG-03-79-007: Mechanical material-selection flowchart integrating loads, environment, manufacturing, corrosion, life, and cost.](../figures/FIG-03-79-007-materials-selection-corrosion-and-manufacturability.png)

### Worked Example 7

**Problem.** High strength does not compensate for unacceptable corrosion in the intended environment.

**Solution.** Materials selection is a constrained problem. A high-strength material that corrodes unacceptably in the service environment fails the durability requirement, so strength alone cannot justify selection without corrosion protection or a different material/process.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. A manufacturing result is not acceptable if the selected process cannot produce the material/geometry/tolerance or if the assumed microstructure is incompatible with the thermal history. Process and material constraints govern.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Manufacturing Processes, Material Processing, Heat Treatment, and Selection**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **KALPAKJIAN, CALLISTER** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 9; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Kalpakjian, S., & Schmid, S. R. (2026). *Manufacturing Engineering and Technology* (9th ed.). Pearson. Print ISBN 978-0-13-824022-6. Supporting scope: Casting, machining, forming, heat treatment, manufacturing processes, process selection, and manufacturability.
- Callister, W. D., Jr., & Rethwisch, D. G. (2018). *Materials Science and Engineering: An Introduction* (10th ed.). Wiley. ISBN 978-1-119-40549-8. Supporting scope: Phase diagrams, heat treatment, polymers, composites, structure-property relations, and materials selection.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using casting process outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using machining speed and feed outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using Taylor tool life outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using metal forming outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using phase transformation and heat treatment outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using engineered material selection outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using mechanical material selection outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| casting process | Concept developed in §79.1; apply with that section's geometry and operating assumptions. |
| machining speed and feed | Concept developed in §79.2; apply with that section's geometry and operating assumptions. |
| Taylor tool life | Concept developed in §79.3; apply with that section's geometry and operating assumptions. |
| metal forming | Concept developed in §79.4; apply with that section's geometry and operating assumptions. |
| phase transformation and heat treatment | Concept developed in §79.5; apply with that section's geometry and operating assumptions. |
| engineered material selection | Concept developed in §79.6; apply with that section's geometry and operating assumptions. |
| mechanical material selection | Concept developed in §79.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **casting process** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **machining speed and feed** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **Taylor tool life** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **metal forming** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **phase transformation and heat treatment** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **engineered material selection** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **mechanical material selection** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **casting process**?

9. What geometric, material, operating, or model assumption must be checked before applying **machining speed and feed**?

10. What geometric, material, operating, or model assumption must be checked before applying **Taylor tool life**?

11. What geometric, material, operating, or model assumption must be checked before applying **metal forming**?

12. What geometric, material, operating, or model assumption must be checked before applying **phase transformation and heat treatment**?

13. What geometric, material, operating, or model assumption must be checked before applying **engineered material selection**?

14. What geometric, material, operating, or model assumption must be checked before applying **mechanical material selection**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **casting process**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **machining speed and feed**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **Taylor tool life**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **metal forming**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **phase transformation and heat treatment**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **engineered material selection**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **mechanical material selection**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **casting process**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **machining speed and feed**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **casting process** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **machining speed and feed** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **Taylor tool life** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **metal forming** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **phase transformation and heat treatment** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **engineered material selection** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **mechanical material selection** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **casting process**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **machining speed and feed**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **Taylor tool life**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **metal forming**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **phase transformation and heat treatment**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **engineered material selection**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **mechanical material selection**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

15. In **Manufacturing Processes, Material Processing, Heat Treatment, and Selection**, start from the physical model and system/component state, not from an isolated formula. A valid solution must match process capability to geometry/material/tolerance, keep cutting and thermal-history variables consistent, and verify that the selected microstructure/material survives the service environment.

16. Units and sign/reference conventions are part of the model in **Manufacturing Processes, Material Processing, Heat Treatment, and Selection**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Manufacturing Processes, Material Processing, Heat Treatment, and Selection**. External sources **KALPAKJIAN, CALLISTER** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: hold diameter fixed and double spindle speed to confirm cutting speed doubles; in the Taylor relation, increase cutting speed and confirm predicted tool life falls. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §79.1, **Casting process selection and defects**, uses \(\text{process choice}=f(\text{alloy, size, geometry, surface, quantity})\). Apply it only under the geometry/material/operating assumptions stated in §79.1, then compare the result with the physical behavior described there.

20. **A.** Section §79.2, **Machining mechanics and cutting parameters**, uses \(V=\pi DN,\qquad \mathrm{MRR}\sim\text{speed}\times\text{feed}\times\text{depth}\). Apply it only under the geometry/material/operating assumptions stated in §79.2, then compare the result with the physical behavior described there.

21. **A.** Section §79.3, **Taylor tool-life relation**, uses \(VT^n=C\). Apply it only under the geometry/material/operating assumptions stated in §79.3, then compare the result with the physical behavior described there.

22. **A.** Section §79.4, **Metal forming and plastic deformation**, uses \(\text{forming requires stress beyond yield while controlling fracture and springback}\). Apply it only under the geometry/material/operating assumptions stated in §79.4, then compare the result with the physical behavior described there.

23. **A.** Section §79.5, **Phase diagrams and heat treatment**, uses \(\text{microstructure}=f(\text{composition, temperature, time, cooling path})\). Apply it only under the geometry/material/operating assumptions stated in §79.5, then compare the result with the physical behavior described there.

24. **A.** Section §79.6, **Polymers, composites, and engineered materials**, uses \(\text{specific property}=\frac{\text{property}}{\rho}\). Apply it only under the geometry/material/operating assumptions stated in §79.6, then compare the result with the physical behavior described there.

25. **A.** Section §79.7, **Materials selection, corrosion, and manufacturability**, uses \(\text{selection}=f(\text{loads, environment, process, life, cost, availability})\). Apply it only under the geometry/material/operating assumptions stated in §79.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Manufacturing Processes, Material Processing, Heat Treatment, and Selection** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **KALPAKJIAN, CALLISTER**; guide synthesis is supplemental explanation and exam-oriented workflow.


---

## Practice Problems

1. A riser supplies liquid metal to compensate for solidification shrinkage.

2. Doubling spindle speed doubles surface speed for the same diameter.

3. If n>0, increasing V decreases T.

4. Hot working generally reduces flow stress and can permit larger deformation.

5. Rapid quenching can suppress equilibrium transformation and create harder microstructures in appropriate steels.

6. A composite may have high specific stiffness even if its absolute modulus is below steel.

7. High strength does not compensate for unacceptable corrosion in the intended environment.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. **Independent check for §79.1 — Casting process selection and defects.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A riser is a reservoir of liquid metal connected to the casting. As the casting contracts during solidification, the riser feeds liquid into the shrinking region so the casting is less likely to form internal shrinkage voids.

2. **Independent check for §79.2 — Machining mechanics and cutting parameters.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Surface speed is \(V=\pi DN\). Holding diameter \(D\) fixed while doubling spindle speed \(N\) gives \(V_2/V_1=2\), so the cutting speed **doubles**.

3. **Independent check for §79.3 — Taylor tool-life relation.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. From \(VT^n=C\), \(T=(C/V)^{1/n}\). For \(n>0\), increasing cutting speed increases the denominator and therefore **decreases tool life**, often strongly because the exponent \(1/n\) is large.

4. **Independent check for §79.4 — Metal forming and plastic deformation.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Hot working occurs at elevated temperature where recovery/recrystallization can reduce flow stress and permit larger plastic strains before fracture. The benefit is not free: oxidation, scale, dimensional accuracy, and grain/microstructure effects still matter.

5. **Independent check for §79.5 — Phase diagrams and heat treatment.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. In suitable steels, rapid quenching suppresses slower diffusional transformations and can form a hard nonequilibrium microstructure such as martensite. The result depends on alloy composition, austenitizing condition, section size, cooling rate, and subsequent tempering.

6. **Independent check for §79.6 — Polymers, composites, and engineered materials.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Specific stiffness is \(E/\rho\). A composite with a lower absolute modulus than steel can still have a larger stiffness-to-weight ratio if its density is sufficiently lower; this is why specific properties matter in weight-sensitive design.

7. **Independent check for §79.7 — Materials selection, corrosion, and manufacturability.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Materials selection is a constrained problem. A high-strength material that corrodes unacceptably in the service environment fails the durability requirement, so strength alone cannot justify selection without corrosion protection or a different material/process.

8. For **Manufacturing Processes, Material Processing, Heat Treatment, and Selection**, one required acceptance screen is: match process capability to geometry/material/tolerance, keep cutting and thermal-history variables consistent, and verify that the selected microstructure/material survives the service environment. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Manufacturing Processes, Material Processing, Heat Treatment, and Selection**. For `split_required` concepts, use **KALPAKJIAN, CALLISTER** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: hold diameter fixed and double spindle speed to confirm cutting speed doubles; in the Taylor relation, increase cutting speed and confirm predicted tool life falls. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 9.

- **casting process:** Casting process selection and defects
- **machining speed and feed:** Machining mechanics and cutting parameters
- **Taylor tool life:** Taylor tool-life relation
- **metal forming:** Metal forming and plastic deformation
- **phase transformation and heat treatment:** Phase diagrams and heat treatment
- **engineered material selection:** Polymers, composites, and engineered materials
- **mechanical material selection:** Materials selection, corrosion, and manufacturability

---

## What's Next

**Chapter 03-80: External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
