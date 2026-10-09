---
chapter: "03-78"
title: "Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-078-01, MEC-3-078-02, MEC-3-078-03, MEC-3-078-04, MEC-3-078-05, MEC-3-078-06, MEC-3-078-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-78: Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MAT-2B-016-01 · MECH-2C-022-03

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **78.1** Explain and apply **Stress concentration and notch effects**.
* **78.2** Explain and apply **Ductile failure — maximum shear and distortion energy**.
* **78.3** Explain and apply **Brittle failure concepts**.
* **78.4** Explain and apply **Fatigue life, alternating and mean stress**.
* **78.5** Explain and apply **S-N behavior and endurance limits**.
* **78.6** Explain and apply **Fracture mechanics concepts**.
* **78.7** Explain and apply **Creep and time-dependent failure**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 78.1 Stress concentration and notch effects

Geometric discontinuities raise local stress. The theoretical concentration factor comes from elastic geometry; fatigue sensitivity determines how fully the notch affects fatigue strength.

\[\sigma_{max}=K_t\sigma_{nom}\]

![FIG-03-78-001: Stepped shaft with stress-flow lines and nominal versus peak stress.](../figures/FIG-03-78-001-stress-concentration-and-notch-effects.png)

### Worked Example 1

**Problem.** Kt=2.0 and nominal stress 80 MPa gives local elastic stress 160 MPa.

**Solution.** \(\sigma_{max}=K_t\sigma_{nom}=(2.0)(80\ {\rm MPa})=\mathbf{160\ MPa}\). This is the elastic local peak associated with the notch model; fatigue sensitivity can require a separate \(K_f\) treatment.

---

## 78.2 Ductile failure — maximum shear and distortion energy

Ductile static design commonly uses maximum-shear-stress or distortion-energy criteria under multiaxial stress.

\[\sigma_{vm}\le \frac{S_y}{n}\]

![FIG-03-78-002: Tresca and von Mises failure envelopes in principal-stress space.](../figures/FIG-03-78-002-ductile-failure-maximum-shear-and-distortion-energy.png)

### Worked Example 2

**Problem.** A uniaxial tensile stress has von Mises stress equal to the tensile stress magnitude.

**Solution.** For uniaxial tension the principal stresses are \((\sigma,0,0)\). Substitution into the distortion-energy relation gives \(\sigma_{vm}=|\sigma|\), so the von Mises equivalent stress equals the tensile-stress magnitude.

---

## 78.3 Brittle failure concepts

Brittle materials fail with limited plastic redistribution. Principal stresses and unequal tensile/compressive strengths are important.

\[\text{compare principal tensile/compressive stresses to brittle strengths}\]

![FIG-03-78-003: Brittle failure envelope with unequal tensile and compressive strength limits.](../figures/FIG-03-78-003-brittle-failure-concepts.png)

### Worked Example 3

**Problem.** A compressive stress state can be less critical than an equal tensile state for many brittle materials.

**Solution.** Brittle materials often have much lower tensile than compressive strength because cracks open in tension but tend to close in compression. Failure assessment therefore tracks principal tensile and compressive stresses separately rather than using a ductile-yield criterion blindly.

---

## 78.4 Fatigue life, alternating and mean stress

Fatigue depends on cyclic amplitude, mean stress, stress concentration, material condition, and life target. Separate alternating and mean components before using a design line.

\[\sigma_a=\frac{\sigma_{max}-\sigma_{min}}2,\quad \sigma_m=\frac{\sigma_{max}+\sigma_{min}}2\]

![FIG-03-78-004: Stress-time cycle showing max, min, mean, amplitude, and R ratio.](../figures/FIG-03-78-004-fatigue-life-alternating-and-mean-stress.png)

### Worked Example 4

**Problem.** Stress cycling between 20 and 100 MPa has σa=40 MPa and σm=60 MPa.

**Solution.** \(\sigma_a=(100-20)/2=\mathbf{40\ MPa}\) and \(\sigma_m=(100+20)/2=\mathbf{60\ MPa}\). The same stress history can therefore have both alternating and nonzero mean components.

---

## 78.5 S-N behavior and endurance limits

An S-N curve relates cyclic stress amplitude to cycles to failure. Some steels exhibit an endurance-limit concept; many materials do not.

\[\text{stress amplitude}=f(N)\]

![FIG-03-78-005: Log-scale S-N curves for steel with endurance region and aluminum without a sharp plateau.](../figures/FIG-03-78-005-s-n-behavior-and-endurance-limits.png)

### Worked Example 5

**Problem.** Reducing alternating stress generally increases fatigue life.

**Solution.** An S-N curve relates cyclic stress amplitude to cycles to failure. Moving to a lower alternating stress generally shifts the intersection to a larger \(N\), so expected fatigue life increases, subject to material/environment/mean-stress effects.

---

## 78.6 Fracture mechanics concepts

Fracture mechanics links flaw size, stress, geometry, and fracture toughness. Crack growth can become unstable when stress intensity reaches material toughness.

\[K_I=Y\sigma\sqrt{\pi a}\]

![FIG-03-78-006: Cracked plate with crack length a, applied stress, geometry factor, and KI/KIC concept.](../figures/FIG-03-78-006-fracture-mechanics-concepts.png)

### Worked Example 6

**Problem.** At fixed stress, increasing crack size raises KI.

**Solution.** \(K_I=Y\sigma\sqrt{\pi a}\). With \(Y\) and \(\sigma\) fixed, \(K_I\propto\sqrt a\); increasing crack size therefore increases the crack-tip driving force and moves the component closer to fracture toughness.

---

## 78.7 Creep and time-dependent failure

Creep is time-dependent deformation under sustained load, especially important at elevated temperature. Primary, secondary, and tertiary stages have distinct strain-rate behavior.

\[\epsilon=\epsilon(t,\sigma,T)\]

![FIG-03-78-007: Creep strain versus time showing primary, secondary, and tertiary stages.](../figures/FIG-03-78-007-creep-and-time-dependent-failure.png)

### Worked Example 7

**Problem.** A turbine component at high temperature can accumulate creep even below room-temperature yield strength.

**Solution.** Creep is time- and temperature-dependent deformation. At sufficiently high homologous temperature, a component can accumulate creep strain under a sustained stress below its room-temperature yield strength; ordinary short-time yield checks do not bound that failure mode.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. Failure criteria must match material behavior and loading. A stress state that violates yield, fatigue, fracture, or creep assumptions cannot be rescued by algebra; use the appropriate failure model and safety factor.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **SHIGLEY** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 8, 9, 14; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Nisbett, K. J., & Budynas, R. G. *Shigley's Mechanical Engineering Design* (2024 Release). McGraw Hill. ISBN 978-1-265-47269-6. Supporting scope: Failure theories, fatigue, springs, pressure-vessel screening, bearings, fasteners, shafts, keys, couplings, gears, and machine-element design.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using stress concentration factor outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using von Mises failure criterion outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using brittle failure criterion outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using fatigue stress components outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using S-N fatigue curve outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using stress intensity factor outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using creep outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| stress concentration factor | Concept developed in §78.1; apply with that section's geometry and operating assumptions. |
| von Mises failure criterion | Concept developed in §78.2; apply with that section's geometry and operating assumptions. |
| brittle failure criterion | Concept developed in §78.3; apply with that section's geometry and operating assumptions. |
| fatigue stress components | Concept developed in §78.4; apply with that section's geometry and operating assumptions. |
| S-N fatigue curve | Concept developed in §78.5; apply with that section's geometry and operating assumptions. |
| stress intensity factor | Concept developed in §78.6; apply with that section's geometry and operating assumptions. |
| creep | Concept developed in §78.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **stress concentration factor** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **von Mises failure criterion** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **brittle failure criterion** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **fatigue stress components** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **S-N fatigue curve** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **stress intensity factor** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **creep** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **stress concentration factor**?

9. What geometric, material, operating, or model assumption must be checked before applying **von Mises failure criterion**?

10. What geometric, material, operating, or model assumption must be checked before applying **brittle failure criterion**?

11. What geometric, material, operating, or model assumption must be checked before applying **fatigue stress components**?

12. What geometric, material, operating, or model assumption must be checked before applying **S-N fatigue curve**?

13. What geometric, material, operating, or model assumption must be checked before applying **stress intensity factor**?

14. What geometric, material, operating, or model assumption must be checked before applying **creep**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **stress concentration factor**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **von Mises failure criterion**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **brittle failure criterion**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **fatigue stress components**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **S-N fatigue curve**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **stress intensity factor**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **creep**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **stress concentration factor**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **von Mises failure criterion**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **stress concentration factor** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **von Mises failure criterion** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **brittle failure criterion** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **fatigue stress components** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **S-N fatigue curve** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **stress intensity factor** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **creep** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **stress concentration factor**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **von Mises failure criterion**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **brittle failure criterion**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **fatigue stress components**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **S-N fatigue curve**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **stress intensity factor**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **creep**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

15. In **Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep**, start from the physical model and system/component state, not from an isolated formula. A valid solution must match the criterion to ductile/brittle/fatigue/fracture/creep behavior, distinguish nominal from local stress, and keep alternating/mean stress definitions consistent.

16. Units and sign/reference conventions are part of the model in **Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep**. External sources **SHIGLEY** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: set \(K_t=1\) and confirm local elastic stress reduces to nominal stress; for \(\sigma_{max}=\sigma_{min}\), confirm alternating stress becomes zero. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §78.1, **Stress concentration and notch effects**, uses \(\sigma_{max}=K_t\sigma_{nom}\). Apply it only under the geometry/material/operating assumptions stated in §78.1, then compare the result with the physical behavior described there.

20. **A.** Section §78.2, **Ductile failure — maximum shear and distortion energy**, uses \(\sigma_{vm}\le \frac{S_y}{n}\). Apply it only under the geometry/material/operating assumptions stated in §78.2, then compare the result with the physical behavior described there.

21. **A.** Section §78.3, **Brittle failure concepts**, uses \(\text{compare principal tensile/compressive stresses to brittle strengths}\). Apply it only under the geometry/material/operating assumptions stated in §78.3, then compare the result with the physical behavior described there.

22. **A.** Section §78.4, **Fatigue life, alternating and mean stress**, uses \(\sigma_a=\frac{\sigma_{max}-\sigma_{min}}2,\quad \sigma_m=\frac{\sigma_{max}+\sigma_{min}}2\). Apply it only under the geometry/material/operating assumptions stated in §78.4, then compare the result with the physical behavior described there.

23. **A.** Section §78.5, **S-N behavior and endurance limits**, uses \(\text{stress amplitude}=f(N)\). Apply it only under the geometry/material/operating assumptions stated in §78.5, then compare the result with the physical behavior described there.

24. **A.** Section §78.6, **Fracture mechanics concepts**, uses \(K_I=Y\sigma\sqrt{\pi a}\). Apply it only under the geometry/material/operating assumptions stated in §78.6, then compare the result with the physical behavior described there.

25. **A.** Section §78.7, **Creep and time-dependent failure**, uses \(\epsilon=\epsilon(t,\sigma,T)\). Apply it only under the geometry/material/operating assumptions stated in §78.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** In this failure-analysis chapter, FE-Handbook-supported stress relations stay tied to the ledger; Shigley supplies the learned stress-concentration, ductile-failure, and fatigue context, while guide synthesis connects those models to FE-style checks.


---

## Practice Problems

1. Kt=2.0 and nominal stress 80 MPa gives local elastic stress 160 MPa.

2. A uniaxial tensile stress has von Mises stress equal to the tensile stress magnitude.

3. A compressive stress state can be less critical than an equal tensile state for many brittle materials.

4. Stress cycling between 20 and 100 MPa has σa=40 MPa and σm=60 MPa.

5. Reducing alternating stress generally increases fatigue life.

6. At fixed stress, increasing crack size raises KI.

7. A turbine component at high temperature can accumulate creep even below room-temperature yield strength.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. **Independent check for §78.1 — Stress concentration and notch effects.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\sigma_{max}=K_t\sigma_{nom}=(2.0)(80\ {\rm MPa})=\mathbf{160\ MPa}\). This is the elastic local peak associated with the notch model; fatigue sensitivity can require a separate \(K_f\) treatment.

2. **Independent check for §78.2 — Ductile failure — maximum shear and distortion energy.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For uniaxial tension the principal stresses are \((\sigma,0,0)\). Substitution into the distortion-energy relation gives \(\sigma_{vm}=|\sigma|\), so the von Mises equivalent stress equals the tensile-stress magnitude.

3. **Independent check for §78.3 — Brittle failure concepts.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Brittle materials often have much lower tensile than compressive strength because cracks open in tension but tend to close in compression. Failure assessment therefore tracks principal tensile and compressive stresses separately rather than using a ductile-yield criterion blindly.

4. **Independent check for §78.4 — Fatigue life, alternating and mean stress.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\sigma_a=(100-20)/2=\mathbf{40\ MPa}\) and \(\sigma_m=(100+20)/2=\mathbf{60\ MPa}\). The same stress history can therefore have both alternating and nonzero mean components.

5. **Independent check for §78.5 — S-N behavior and endurance limits.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. An S-N curve relates cyclic stress amplitude to cycles to failure. Moving to a lower alternating stress generally shifts the intersection to a larger \(N\), so expected fatigue life increases, subject to material/environment/mean-stress effects.

6. **Independent check for §78.6 — Fracture mechanics concepts.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(K_I=Y\sigma\sqrt{\pi a}\). With \(Y\) and \(\sigma\) fixed, \(K_I\propto\sqrt a\); increasing crack size therefore increases the crack-tip driving force and moves the component closer to fracture toughness.

7. **Independent check for §78.7 — Creep and time-dependent failure.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Creep is time- and temperature-dependent deformation. At sufficiently high homologous temperature, a component can accumulate creep strain under a sustained stress below its room-temperature yield strength; ordinary short-time yield checks do not bound that failure mode.

8. For **Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep**, one required acceptance screen is: match the criterion to ductile/brittle/fatigue/fracture/creep behavior, distinguish nominal from local stress, and keep alternating/mean stress definitions consistent. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep**. For `split_required` concepts, use **SHIGLEY** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: set \(K_t=1\) and confirm local elastic stress reduces to nominal stress; for \(\sigma_{max}=\sigma_{min}\), confirm alternating stress becomes zero. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 8, 9, 14.

- **stress concentration factor:** Stress concentration and notch effects
- **von Mises failure criterion:** Ductile failure — maximum shear and distortion energy
- **brittle failure criterion:** Brittle failure concepts
- **fatigue stress components:** Fatigue life, alternating and mean stress
- **S-N fatigue curve:** S-N behavior and endurance limits
- **stress intensity factor:** Fracture mechanics concepts
- **creep:** Creep and time-dependent failure

---

## What's Next

**Chapter 03-79: Manufacturing Processes, Material Processing, Heat Treatment, and Selection**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
