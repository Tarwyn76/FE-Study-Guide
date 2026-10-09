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

**Solution.** \(\omega_n=\sqrt{k/m}=\sqrt{400/4}=\mathbf{10\ rad/s}\). The corresponding natural frequency is \(f_n=\omega_n/(2\pi)=\mathbf{1.59\ Hz}\).

---

## 77.2 Damped free vibration

Viscous damping controls decay and response type. Underdamped systems oscillate with a damped natural frequency; critical damping is the fastest nonoscillatory return in the ideal model.

\[\zeta=\frac{c}{2\sqrt{km}}\]

![FIG-03-77-002: Underdamped, critically damped, and overdamped free responses on the same axes.](../figures/FIG-03-77-002-damped-free-vibration.png)

### Worked Example 2

**Problem.** ζ=0.2 is underdamped.

**Solution.** \(\zeta=0.20<1\), so the response is **underdamped** and oscillatory. Its damped natural frequency is \(\omega_d=\omega_n\sqrt{1-\zeta^2}\approx0.980\,\omega_n\).

---

## 77.3 Logarithmic decrement and decay measurement

Successive peak amplitudes can be used to estimate damping for an underdamped system.

\[\delta=\ln\!\left(\frac{x_n}{x_{n+1}}\right)\]

![FIG-03-77-003: Measured vibration decay with successive peaks xn and xn+1 marked.](../figures/FIG-03-77-003-logarithmic-decrement-and-decay-measurement.png)

### Worked Example 3

**Problem.** If successive peaks are 10 mm and 8 mm, δ=ln(1.25)=0.223.

**Solution.** \(\delta=\ln(x_n/x_{n+1})=\ln(10/8)=\ln(1.25)=\mathbf{0.223}\). A positive decrement means the measured free-vibration peaks are decaying.

---

## 77.4 Harmonic forced vibration

Steady harmonic response depends on forcing frequency relative to natural frequency and on damping. Near resonance, dynamic amplification can become large.

\[r=\frac{\omega}{\omega_n}\]

![FIG-03-77-004: Forced SDOF oscillator and amplitude ratio versus frequency ratio for several damping ratios.](../figures/FIG-03-77-004-harmonic-forced-vibration.png)

### Worked Example 4

**Problem.** A forcing frequency equal to the undamped natural frequency gives r=1.

**Solution.** The frequency ratio is \(r=\omega/\omega_n\). Because both \(\omega\) and \(\omega_n\) are measured on the same angular-frequency basis (rad/s), equal values give \(\mathbf{r=1.00}\), the resonance neighborhood for the linear SDOF model.

---

## 77.5 Resonance and dynamic amplification

Dynamic magnification shows why small periodic forces can produce large motion near resonance. Damping limits the resonant peak.

\[M=\frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}\]

![FIG-03-77-005: Magnification-factor curves versus r for several damping ratios.](../figures/FIG-03-77-005-resonance-and-dynamic-amplification.png)

### Worked Example 5

**Problem.** At r≈1, increasing ζ reduces peak response.

**Solution.** At \(r=1\), \(M=1/(2\zeta)\) for the stated force-excited SDOF expression. Increasing \(\zeta\) increases the denominator, so the resonance peak **decreases**.

---

## 77.6 Base excitation and vibration isolation

Isolation mounts reduce transmitted vibration when the system operates in the isolation region; poor frequency selection can amplify motion instead.

\[\text{isolation improves when excitation frequency is sufficiently above } \omega_n\]

![FIG-03-77-006: Machine on isolators with transmissibility versus frequency ratio.](../figures/FIG-03-77-006-base-excitation-and-vibration-isolation.png)

### Worked Example 6

**Problem.** A soft mount may lower natural frequency enough to move a machine operating frequency into the isolation region.

**Solution.** Softening the mount lowers \(\omega_n=\sqrt{k/m}\), which raises the operating ratio \(r=\omega/\omega_n\). When the ratio is sufficiently above the resonance region, transmissibility can fall below unity and the mount acts as an isolator.

---

## 77.7 Vibration model selection and resonance avoidance

Real machines can have multiple modes, nonlinear stiffness, and nonviscous damping. FE models are idealized, but the engineering check is still whether forcing and natural frequencies create unacceptable response.

\[\text{operating frequencies should be separated from damaging resonances}\]

![FIG-03-77-007: Operating excitation lines and natural-frequency bands versus speed with resonance crossings highlighted.](../figures/FIG-03-77-007-vibration-model-selection-and-resonance-avoidance.png)

### Worked Example 7

**Problem.** Changing mass or stiffness can shift a resonance away from operating speed.

**Solution.** Because \(\omega_n=\sqrt{k/m}\), increasing mass lowers natural frequency and increasing stiffness raises it. Either change can move a structural resonance away from a fixed operating speed, but the resulting static deflection, loads, and isolation behavior must also be checked.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. A vibration result is invalid if the assumed damping/forcing model contradicts the solved regime—for example, using an undamped resonance expression after damping has been specified. Re-select the transfer function and recompute.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Mechanical Vibrations — Free, Forced, Damped, and Resonant Response**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **RAO** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 7; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Rao, S. S. (2022). *Mechanical Vibrations* (6th ed.). Pearson. eText ISBN 978-0-13-751528-8. Supporting scope: Free, damped, and forced vibration; resonance; vibration isolation; and SDOF/MDOF modeling.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Mechanical Vibrations — Free, Forced, Damped, and Resonant Response**, start from the physical model and system/component state, not from an isolated formula. A valid solution must identify free versus forced response, damping regime, frequency ratio, and whether the chosen transfer/amplification expression matches the excitation model.

16. Units and sign/reference conventions are part of the model in **Mechanical Vibrations — Free, Forced, Damped, and Resonant Response**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Mechanical Vibrations — Free, Forced, Damped, and Resonant Response**. External sources **RAO** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: let damping approach zero away from resonance and confirm the damped response approaches the undamped expression; at \(r=1\), confirm increasing damping lowers the peak. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §77.1, **Single-degree-of-freedom mass-spring model**, uses \(\omega_n=\sqrt{\frac{k}{m}},\qquad f_n=\frac{\omega_n}{2\pi}\). Apply it only under the geometry/material/operating assumptions stated in §77.1, then compare the result with the physical behavior described there.

20. **A.** Section §77.2, **Damped free vibration**, uses \(\zeta=\frac{c}{2\sqrt{km}}\). Apply it only under the geometry/material/operating assumptions stated in §77.2, then compare the result with the physical behavior described there.

21. **A.** Section §77.3, **Logarithmic decrement and decay measurement**, uses \(\delta=\ln\!\left(\frac{x_n}{x_{n+1}}\right)\). Apply it only under the geometry/material/operating assumptions stated in §77.3, then compare the result with the physical behavior described there.

22. **A.** Section §77.4, **Harmonic forced vibration**, uses \(r=\frac{\omega}{\omega_n}\). Apply it only under the geometry/material/operating assumptions stated in §77.4, then compare the result with the physical behavior described there.

23. **A.** Section §77.5, **Resonance and dynamic amplification**, uses \(M=\frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}\). Apply it only under the geometry/material/operating assumptions stated in §77.5, then compare the result with the physical behavior described there.

24. **A.** Section §77.6, **Base excitation and vibration isolation**, uses \(\text{isolation improves when excitation frequency is sufficiently above } \omega_n\). Apply it only under the geometry/material/operating assumptions stated in §77.6, then compare the result with the physical behavior described there.

25. **A.** Section §77.7, **Vibration model selection and resonance avoidance**, uses \(\text{operating frequencies should be separated from damaging resonances}\). Apply it only under the geometry/material/operating assumptions stated in §77.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Mechanical Vibrations — Free, Forced, Damped, and Resonant Response** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **RAO**; guide synthesis is supplemental explanation and exam-oriented workflow.


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

1. **Independent check for §77.1 — Single-degree-of-freedom mass-spring model.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\omega_n=\sqrt{k/m}=\sqrt{400/4}=\mathbf{10\ rad/s}\). The corresponding natural frequency is \(f_n=\omega_n/(2\pi)=\mathbf{1.59\ Hz}\).

2. **Independent check for §77.2 — Damped free vibration.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\zeta=0.20<1\), so the response is **underdamped** and oscillatory. Its damped natural frequency is \(\omega_d=\omega_n\sqrt{1-\zeta^2}\approx0.980\,\omega_n\).

3. **Independent check for §77.3 — Logarithmic decrement and decay measurement.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\delta=\ln(x_n/x_{n+1})=\ln(10/8)=\ln(1.25)=\mathbf{0.223}\). A positive decrement means the measured free-vibration peaks are decaying.

4. **Independent check for §77.4 — Harmonic forced vibration.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. The frequency ratio is \(r=\omega/\omega_n\). Equal forcing and undamped natural frequencies give \(\mathbf{r=1}\), the resonance neighborhood for the linear SDOF model.

5. **Independent check for §77.5 — Resonance and dynamic amplification.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. At \(r=1\), \(M=1/(2\zeta)\) for the stated force-excited SDOF expression. Increasing \(\zeta\) increases the denominator, so the resonance peak **decreases**.

6. **Independent check for §77.6 — Base excitation and vibration isolation.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Softening the mount lowers \(\omega_n=\sqrt{k/m}\), which raises the operating ratio \(r=\omega/\omega_n\). When the ratio is sufficiently above the resonance region, transmissibility can fall below unity and the mount acts as an isolator.

7. **Independent check for §77.7 — Vibration model selection and resonance avoidance.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Because \(\omega_n=\sqrt{k/m}\), increasing mass lowers natural frequency and increasing stiffness raises it. Either change can move a structural resonance away from a fixed operating speed, but the resulting static deflection, loads, and isolation behavior must also be checked.

8. For **Mechanical Vibrations — Free, Forced, Damped, and Resonant Response**, one required acceptance screen is: identify free versus forced response, damping regime, frequency ratio, and whether the chosen transfer/amplification expression matches the excitation model. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Mechanical Vibrations — Free, Forced, Damped, and Resonant Response**. For `split_required` concepts, use **RAO** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: let damping approach zero away from resonance and confirm the damped response approaches the undamped expression; at \(r=1\), confirm increasing damping lowers the peak. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

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
