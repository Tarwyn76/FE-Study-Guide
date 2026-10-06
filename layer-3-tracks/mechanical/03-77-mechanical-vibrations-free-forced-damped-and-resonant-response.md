---
chapter: "03-77"
title: "Mechanical Vibrations — Free, Forced, Damped, and Resonant Response"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-077-01, MEC-3-077-02, MEC-3-077-03, MEC-3-077-04, MEC-3-077-05, MEC-3-077-06, MEC-3-077-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-77: Mechanical Vibrations — Free, Forced, Damped, and Resonant Response

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MECH-2C-022-03

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Mechanical Vibrations — Free, Forced, Damped, and Resonant Response**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **77.1** Explain and apply **Single-degree-of-freedom mass-spring model**.
* **77.2** Explain and apply **Damped free vibration**.
* **77.3** Explain and apply **Logarithmic decrement and decay measurement**.
* **77.4** Explain and apply **Harmonic forced vibration**.
* **77.5** Explain and apply **Resonance and dynamic amplification**.
* **77.6** Explain and apply **Base excitation and vibration isolation**.
* **77.7** Explain and apply **Vibration model selection and resonance avoidance**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 77.1 Single-degree-of-freedom mass-spring model

The undamped SDOF oscillator is the base vibration model. Natural frequency depends on stiffness and mass, not vibration amplitude for a linear model.

\[\omega_n=\sqrt{\frac{k}{m}},\qquad f_n=\frac{\omega_n}{2\pi}\]

![FIG-03-77-001: Mass-spring oscillator with displacement, stiffness, mass, and free-vibration waveform.](../figures/FIG-03-77-001-single-degree-of-freedom-mass-spring-model.png)

### Worked Example 1

**Problem.** m=4 kg and k=400 N/m gives ωn=10 rad/s.

**Solution.** Apply the relation and model in §77.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 77.2 Damped free vibration

Viscous damping controls decay and response type. Underdamped systems oscillate with a damped natural frequency; critical damping is the fastest nonoscillatory return in the ideal model.

\[\zeta=\frac{c}{2\sqrt{km}}\]

![FIG-03-77-002: Underdamped, critically damped, and overdamped free responses on the same axes.](../figures/FIG-03-77-002-damped-free-vibration.png)

### Worked Example 2

**Problem.** ζ=0.2 is underdamped.

**Solution.** Apply the relation and model in §77.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 77.3 Logarithmic decrement and decay measurement

Successive peak amplitudes can be used to estimate damping for an underdamped system.

\[\delta=\ln\!\left(\frac{x_n}{x_{n+1}}\right)\]

![FIG-03-77-003: Measured vibration decay with successive peaks xn and xn+1 marked.](../figures/FIG-03-77-003-logarithmic-decrement-and-decay-measurement.png)

### Worked Example 3

**Problem.** If successive peaks are 10 mm and 8 mm, δ=ln(1.25)=0.223.

**Solution.** Apply the relation and model in §77.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 77.4 Harmonic forced vibration

Steady harmonic response depends on forcing frequency relative to natural frequency and on damping. Near resonance, dynamic amplification can become large.

\[r=\frac{\omega}{\omega_n}\]

![FIG-03-77-004: Forced SDOF oscillator and amplitude ratio versus frequency ratio for several damping ratios.](../figures/FIG-03-77-004-harmonic-forced-vibration.png)

### Worked Example 4

**Problem.** A forcing frequency equal to the undamped natural frequency gives r=1.

**Solution.** Apply the relation and model in §77.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 77.5 Resonance and dynamic amplification

Dynamic magnification shows why small periodic forces can produce large motion near resonance. Damping limits the resonant peak.

\[M=\frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}\]

![FIG-03-77-005: Magnification-factor curves versus r for several damping ratios.](../figures/FIG-03-77-005-resonance-and-dynamic-amplification.png)

### Worked Example 5

**Problem.** At r≈1, increasing ζ reduces peak response.

**Solution.** Apply the relation and model in §77.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 77.6 Base excitation and vibration isolation

Isolation mounts reduce transmitted vibration when the system operates in the isolation region; poor frequency selection can amplify motion instead.

\[\text{isolation improves when excitation frequency is sufficiently above } \omega_n\]

![FIG-03-77-006: Machine on isolators with transmissibility versus frequency ratio.](../figures/FIG-03-77-006-base-excitation-and-vibration-isolation.png)

### Worked Example 6

**Problem.** A soft mount may lower natural frequency enough to move a machine operating frequency into the isolation region.

**Solution.** Apply the relation and model in §77.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 77.7 Vibration model selection and resonance avoidance

Real machines can have multiple modes, nonlinear stiffness, and nonviscous damping. FE models are idealized, but the engineering check is still whether forcing and natural frequencies create unacceptable response.

\[\text{operating frequencies should be separated from damaging resonances}\]

![FIG-03-77-007: Operating excitation lines and natural-frequency bands versus speed with resonance crossings highlighted.](../figures/FIG-03-77-007-vibration-model-selection-and-resonance-avoidance.png)

### Worked Example 7

**Problem.** Changing mass or stiffness can shift a resonance away from operating speed.

**Solution.** Apply the relation and model in §77.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. Select the correct model or failure/operating region and solve again. Algebra does not override geometry, material behavior, or component-state validity.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** Use the Handbook expression and its definitions unless the problem explicitly provides another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 7; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** The Mechanical specification includes both directly tabulated Handbook equations and learned design concepts. This chapter does not assign invented Handbook pages to specification-required material that is not directly tabulated.

---

## Where This Goes Wrong

**Using natural frequency outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using damping ratio outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using logarithmic decrement outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using frequency ratio outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using dynamic magnification outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using vibration isolation outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using vibration design check outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| natural frequency | Concept developed in §77.1; apply with that section's geometry and operating assumptions. |
| damping ratio | Concept developed in §77.2; apply with that section's geometry and operating assumptions. |
| logarithmic decrement | Concept developed in §77.3; apply with that section's geometry and operating assumptions. |
| frequency ratio | Concept developed in §77.4; apply with that section's geometry and operating assumptions. |
| dynamic magnification | Concept developed in §77.5; apply with that section's geometry and operating assumptions. |
| vibration isolation | Concept developed in §77.6; apply with that section's geometry and operating assumptions. |
| vibration design check | Concept developed in §77.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **natural frequency** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **damping ratio** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **logarithmic decrement** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **frequency ratio** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **dynamic magnification** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **vibration isolation** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **vibration design check** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **natural frequency**?

9. What geometric, material, operating, or model assumption must be checked before applying **damping ratio**?

10. What geometric, material, operating, or model assumption must be checked before applying **logarithmic decrement**?

11. What geometric, material, operating, or model assumption must be checked before applying **frequency ratio**?

12. What geometric, material, operating, or model assumption must be checked before applying **dynamic magnification**?

13. What geometric, material, operating, or model assumption must be checked before applying **vibration isolation**?

14. What geometric, material, operating, or model assumption must be checked before applying **vibration design check**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **natural frequency**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **damping ratio**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **logarithmic decrement**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **frequency ratio**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **dynamic magnification**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **vibration isolation**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **vibration design check**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **natural frequency**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **damping ratio**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **natural frequency** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **damping ratio** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **logarithmic decrement** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **frequency ratio** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **dynamic magnification** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **vibration isolation** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **vibration design check** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **natural frequency**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **damping ratio**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **logarithmic decrement**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **frequency ratio**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **dynamic magnification**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **vibration isolation**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **vibration design check**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

15. The sketch exposes supports, force directions, geometry, constraints, energy/flow paths, and missing load cases before algebra obscures them.

16. Mechanical equations are model-dependent. The result must remain compatible with yielding/buckling/fatigue, flow regime, thermal state, contact, or kinematic constraints.

17. The Handbook is the supplied exam reference; its definitions, correction factors, unit conventions, and tables should govern unless the problem explicitly supplies another relation.

18. These checks catch impossible motion, unit errors, invalid thin-wall or linear assumptions, unrealistic stresses, interference, and parts that cannot be manufactured or assembled.

19. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

20. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

21. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

22. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

23. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

24. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

25. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

26. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.

27. **A.** The relation depends on its geometry, loading, material/operating assumptions, and unit convention.


---

## Practice Problems

1. m=4 kg and k=400 N/m gives ωn=10 rad/s.

2. ζ=0.2 is underdamped.

3. If successive peaks are 10 mm and 8 mm, δ=ln(1.25)=0.223.

4. A forcing frequency equal to the undamped natural frequency gives r=1.

5. At r≈1, increasing ζ reduces peak response.

6. A soft mount may lower natural frequency enough to move a machine operating frequency into the isolation region.

7. Changing mass or stiffness can shift a resonance away from operating speed.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. Use §77.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §77.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §77.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §77.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §77.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §77.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §77.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 7, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 7.

- **natural frequency:** Single-degree-of-freedom mass-spring model
- **damping ratio:** Damped free vibration
- **logarithmic decrement:** Logarithmic decrement and decay measurement
- **frequency ratio:** Harmonic forced vibration
- **dynamic magnification:** Resonance and dynamic amplification
- **vibration isolation:** Base excitation and vibration isolation
- **vibration design check:** Vibration model selection and resonance avoidance

---

## What's Next

**Chapter 03-78: Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
