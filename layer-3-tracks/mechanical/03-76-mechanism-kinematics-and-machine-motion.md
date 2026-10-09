---
chapter: "03-76"
title: "Mechanism Kinematics and Machine Motion"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-076-01, MEC-3-076-02, MEC-3-076-03, MEC-3-076-04, MEC-3-076-05, MEC-3-076-06, MEC-3-076-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-76: Mechanism Kinematics and Machine Motion

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MECH-2C-022-03

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Mechanism Kinematics and Machine Motion**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **76.1** Explain and apply **Rigid-body translation and rotation review**.
* **76.2** Explain and apply **Instantaneous centers of zero velocity**.
* **76.3** Explain and apply **Four-bar linkage geometry and mobility**.
* **76.4** Explain and apply **Slider-crank displacement, velocity, and acceleration**.
* **76.5** Explain and apply **Gear-pair angular speed relationships**.
* **76.6** Explain and apply **Compound and planetary gear trains**.
* **76.7** Explain and apply **Mechanism mobility, interference, and motion verification**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 76.1 Rigid-body translation and rotation review

Mechanism analysis builds on rigid-body kinematics. Points on the same rigid link share angular velocity but generally have different linear velocities.

\[\mathbf v_B=\mathbf v_A+\boldsymbol\omega\times\mathbf r_{B/A}\]

![FIG-03-76-001: Rotating rigid link with two points, position vector, angular velocity, and tangential velocities.](../figures/FIG-03-76-001-rigid-body-translation-and-rotation-review.png)

### Worked Example 1

**Problem.** A point 0.20 m from a fixed pivot on a link rotating at 10 rad/s has speed 2.0 m/s.

**Solution.** For fixed-axis rotation the speed magnitude is \(v=\omega r=(10\ {\rm rad/s})(0.20\ {\rm m})=\mathbf{2.0\ m/s}\). The velocity is tangent to the circular path, perpendicular to the radius.

---

## 76.2 Instantaneous centers of zero velocity

For planar motion, a rigid body can be viewed instantaneously as rotating about a point with zero velocity. The instantaneous center simplifies velocity ratios but changes location with configuration.

\[v_P=\omega r_{P/IC}\]

![FIG-03-76-002: Four-bar link with perpendicular velocity lines locating the instantaneous center.](../figures/FIG-03-76-002-instantaneous-centers-of-zero-velocity.png)

### Worked Example 2

**Problem.** If a coupler point is 0.30 m from the IC and the link angular speed is 4 rad/s, its speed is 1.2 m/s.

**Solution.** Using the instantaneous center, \(v_P=\omega r_{P/IC}=(4\ {\rm rad/s})(0.30\ {\rm m})=\mathbf{1.2\ m/s}\). The direction is perpendicular to the line from the IC to the point.

---

## 76.3 Four-bar linkage geometry and mobility

A four-bar mechanism consists of ground plus three moving links connected by revolute joints. Position analysis is a vector loop-closure problem.

\[L_1+L_2+L_3+L_4\text{ close geometrically around the loop}\]

![FIG-03-76-003: Four-bar crank-rocker mechanism with link lengths, angles, ground pivots, and coupler point.](../figures/FIG-03-76-003-four-bar-linkage-geometry-and-mobility.png)

### Worked Example 3

**Problem.** A valid configuration must satisfy the vector loop closure; arbitrary link angles generally do not.

**Solution.** The link vectors must form a closed polygon: \(\mathbf r_1+\mathbf r_2+\mathbf r_3+\mathbf r_4=\mathbf0\) when written with consistent directions. Arbitrary angles that do not satisfy both x- and y-component closure do not describe a possible four-bar configuration.

---

## 76.4 Slider-crank displacement, velocity, and acceleration

Slider-crank motion converts rotation to reciprocating translation. Differentiate the position constraint for velocity and acceleration when an exact relation is needed.

\[\mathbf r_{crank}+\mathbf r_{rod}=\mathbf r_{slider}\]

![FIG-03-76-004: Crank, connecting rod, slider, crank angle, stroke, and velocity vectors.](../figures/FIG-03-76-004-slider-crank-displacement-velocity-and-acceleration.png)

### Worked Example 4

**Problem.** At top-dead-center the slider velocity is zero even though crank angular speed can be nonzero.

**Solution.** At top-dead-center the crank and connecting rod are collinear with the slider axis. The instantaneous slider displacement is at an extremum, so \(dx/dt=\mathbf0\) even though the crank can have nonzero \(\omega\); the slider acceleration need not be zero.

---

## 76.5 Gear-pair angular speed relationships

External gears reverse direction and scale speed according to tooth count. Idler gears can change direction or spacing without changing the overall magnitude ratio.

\[\frac{\omega_{out}}{\omega_{in}}=-\frac{N_{in}}{N_{out}}\]

![FIG-03-76-005: Two spur gears with tooth counts, pitch circles, rotation directions, and speed ratio.](../figures/FIG-03-76-005-gear-pair-angular-speed-relationships.png)

### Worked Example 5

**Problem.** A 20-tooth driver turning at 1200 rpm drives a 60-tooth gear at 400 rpm in the opposite direction.

**Solution.** For external gears, \(\omega_{out}/\omega_{in}=-N_{in}/N_{out}=-(20/60)\). Thus \(\omega_{out}=-(20/60)(1200)=\mathbf{-400\ rpm}\): 400 rpm in the opposite direction.

---

## 76.6 Compound and planetary gear trains

Compound trains multiply stage ratios. Planetary trains require relative-motion reasoning because sun, ring, and carrier can all move.

\[m_v=\frac{\prod N_{driven}}{\prod N_{driver}}\]

![FIG-03-76-006: Compound gear train and simple sun-planet-ring carrier set with angular velocities labeled.](../figures/FIG-03-76-006-compound-and-planetary-gear-trains.png)

### Worked Example 6

**Problem.** Two 3:1 reduction stages in series provide 9:1 speed reduction.

**Solution.** Stage ratios multiply. Two 3:1 reductions give \(3\times3=\mathbf{9:1}\), so the final speed magnitude is one-ninth of the input speed. If speed is expressed in rpm, \(n_{out}=n_{in}/9\); the 9:1 ratio itself is dimensionless.

---

## 76.7 Mechanism mobility, interference, and motion verification

A numerical mechanism solution must satisfy link lengths, joint constraints, assembly branch, and motion continuity. Kinematic singularities can produce large velocity ratios.

\[\text{geometry}+\text{constraints}\rightarrow\text{physically possible motion}\]

![FIG-03-76-007: Mechanism swept envelope and a toggle/singularity configuration with transmission angle.](../figures/FIG-03-76-007-mechanism-mobility-interference-and-motion-verification.png)

### Worked Example 7

**Problem.** A calculated position that stretches a rigid link is invalid regardless of algebra.

**Solution.** A rigid link must preserve its specified length. If a computed configuration changes the distance between its joints, the geometry violates the rigid-body constraint; the algebraic root must be rejected and the compatible configuration solved instead.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. A mechanism solution that violates fixed link lengths or loop closure is not a physically admissible configuration. Rebuild the vector loop and choose the compatible root before using velocity or acceleration relations.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Mechanism Kinematics and Machine Motion**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **NORTON** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 7; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Norton, R. L. (2020). *Design of Machinery* (6th ed.). McGraw Hill. ISBN 978-1-260-11331-0. Supporting scope: Mechanism kinematics, linkages, slider-cranks, gear trains, motion analysis, and machine dynamics.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using rigid-body planar kinematics outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using instantaneous center outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using four-bar linkage outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using slider-crank mechanism outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using gear velocity ratio outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using compound and planetary gear train outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using mechanism motion verification outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| rigid-body planar kinematics | Concept developed in §76.1; apply with that section's geometry and operating assumptions. |
| instantaneous center | Concept developed in §76.2; apply with that section's geometry and operating assumptions. |
| four-bar linkage | Concept developed in §76.3; apply with that section's geometry and operating assumptions. |
| slider-crank mechanism | Concept developed in §76.4; apply with that section's geometry and operating assumptions. |
| gear velocity ratio | Concept developed in §76.5; apply with that section's geometry and operating assumptions. |
| compound and planetary gear train | Concept developed in §76.6; apply with that section's geometry and operating assumptions. |
| mechanism motion verification | Concept developed in §76.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **rigid-body planar kinematics** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **instantaneous center** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **four-bar linkage** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **slider-crank mechanism** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **gear velocity ratio** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **compound and planetary gear train** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **mechanism motion verification** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **rigid-body planar kinematics**?

9. What geometric, material, operating, or model assumption must be checked before applying **instantaneous center**?

10. What geometric, material, operating, or model assumption must be checked before applying **four-bar linkage**?

11. What geometric, material, operating, or model assumption must be checked before applying **slider-crank mechanism**?

12. What geometric, material, operating, or model assumption must be checked before applying **gear velocity ratio**?

13. What geometric, material, operating, or model assumption must be checked before applying **compound and planetary gear train**?

14. What geometric, material, operating, or model assumption must be checked before applying **mechanism motion verification**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **rigid-body planar kinematics**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **instantaneous center**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **four-bar linkage**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **slider-crank mechanism**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **gear velocity ratio**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **compound and planetary gear train**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **mechanism motion verification**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **rigid-body planar kinematics**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **instantaneous center**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **rigid-body planar kinematics** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **instantaneous center** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **four-bar linkage** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **slider-crank mechanism** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **gear velocity ratio** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **compound and planetary gear train** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **mechanism motion verification** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **rigid-body planar kinematics**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **instantaneous center**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **four-bar linkage**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **slider-crank mechanism**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **gear velocity ratio**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **compound and planetary gear train**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **mechanism motion verification**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

15. In **Mechanism Kinematics and Machine Motion**, start from the physical model and system/component state, not from an isolated formula. A valid solution must preserve rigid link lengths, close every kinematic loop, use the correct gear sign/ratio, and reject alternate mathematical roots that cannot assemble physically.

16. Units and sign/reference conventions are part of the model in **Mechanism Kinematics and Machine Motion**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Mechanism Kinematics and Machine Motion**. External sources **NORTON** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: let one angular speed approach zero and confirm the associated rigid-body point velocities reduce consistently while link lengths remain unchanged. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §76.1, **Rigid-body translation and rotation review**, uses \(\mathbf v_B=\mathbf v_A+\boldsymbol\omega\times\mathbf r_{B/A}\). Apply it only under the geometry/material/operating assumptions stated in §76.1, then compare the result with the physical behavior described there.

20. **A.** Section §76.2, **Instantaneous centers of zero velocity**, uses \(v_P=\omega r_{P/IC}\). Apply it only under the geometry/material/operating assumptions stated in §76.2, then compare the result with the physical behavior described there.

21. **A.** Section §76.3, **Four-bar linkage geometry and mobility**, uses \(L_1+L_2+L_3+L_4\text{ close geometrically around the loop}\). Apply it only under the geometry/material/operating assumptions stated in §76.3, then compare the result with the physical behavior described there.

22. **A.** Section §76.4, **Slider-crank displacement, velocity, and acceleration**, uses \(\mathbf r_{crank}+\mathbf r_{rod}=\mathbf r_{slider}\). Apply it only under the geometry/material/operating assumptions stated in §76.4, then compare the result with the physical behavior described there.

23. **A.** Section §76.5, **Gear-pair angular speed relationships**, uses \(\frac{\omega_{out}}{\omega_{in}}=-\frac{N_{in}}{N_{out}}\). Apply it only under the geometry/material/operating assumptions stated in §76.5, then compare the result with the physical behavior described there.

24. **A.** Section §76.6, **Compound and planetary gear trains**, uses \(m_v=\frac{\prod N_{driven}}{\prod N_{driver}}\). Apply it only under the geometry/material/operating assumptions stated in §76.6, then compare the result with the physical behavior described there.

25. **A.** Section §76.7, **Mechanism mobility, interference, and motion verification**, uses \(\text{geometry}+\text{constraints}\rightarrow\text{physically possible motion}\). Apply it only under the geometry/material/operating assumptions stated in §76.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Mechanism Kinematics and Machine Motion** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **NORTON**; guide synthesis is supplemental explanation and exam-oriented workflow.


---

## Practice Problems

1. A point 0.20 m from a fixed pivot on a link rotating at 10 rad/s has speed 2.0 m/s.

2. If a coupler point is 0.30 m from the IC and the link angular speed is 4 rad/s, its speed is 1.2 m/s.

3. A valid configuration must satisfy the vector loop closure; arbitrary link angles generally do not.

4. At top-dead-center the slider velocity is zero even though crank angular speed can be nonzero.

5. A 20-tooth driver turning at 1200 rpm drives a 60-tooth gear at 400 rpm in the opposite direction.

6. Two 3:1 reduction stages in series provide 9:1 speed reduction.

7. A calculated position that stretches a rigid link is invalid regardless of algebra.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. **Independent check for §76.1 — Rigid-body translation and rotation review.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For fixed-axis rotation the speed magnitude is \(v=\omega r=(10\ {\rm rad/s})(0.20\ {\rm m})=\mathbf{2.0\ m/s}\). The velocity is tangent to the circular path, perpendicular to the radius.

2. **Independent check for §76.2 — Instantaneous centers of zero velocity.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Using the instantaneous center, \(v_P=\omega r_{P/IC}=(4\ {\rm rad/s})(0.30\ {\rm m})=\mathbf{1.2\ m/s}\). The direction is perpendicular to the line from the IC to the point.

3. **Independent check for §76.3 — Four-bar linkage geometry and mobility.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. The link vectors must form a closed polygon: \(\mathbf r_1+\mathbf r_2+\mathbf r_3+\mathbf r_4=\mathbf0\) when written with consistent directions. Arbitrary angles that do not satisfy both x- and y-component closure do not describe a possible four-bar configuration.

4. **Independent check for §76.4 — Slider-crank displacement, velocity, and acceleration.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. At top-dead-center the crank and connecting rod are collinear with the slider axis. The instantaneous slider displacement is at an extremum, so \(dx/dt=\mathbf0\) even though the crank can have nonzero \(\omega\); the slider acceleration need not be zero.

5. **Independent check for §76.5 — Gear-pair angular speed relationships.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For external gears, \(\omega_{out}/\omega_{in}=-N_{in}/N_{out}=-(20/60)\). Thus \(\omega_{out}=-(20/60)(1200)=\mathbf{-400\ rpm}\): 400 rpm in the opposite direction.

6. **Independent check for §76.6 — Compound and planetary gear trains.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Stage ratios multiply. Two 3:1 reductions give \(3\times3=\mathbf{9:1}\), so the final speed magnitude is one-ninth of the input speed, neglecting slip/compliance.

7. **Independent check for §76.7 — Mechanism mobility, interference, and motion verification.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A rigid link must preserve its specified length. If a computed configuration changes the distance between its joints, the geometry violates the rigid-body constraint; the algebraic root must be rejected and the compatible configuration solved instead.

8. For **Mechanism Kinematics and Machine Motion**, one required acceptance screen is: preserve rigid link lengths, close every kinematic loop, use the correct gear sign/ratio, and reject alternate mathematical roots that cannot assemble physically. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Mechanism Kinematics and Machine Motion**. For `split_required` concepts, use **NORTON** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: let one angular speed approach zero and confirm the associated rigid-body point velocities reduce consistently while link lengths remain unchanged. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 7.

- **rigid-body planar kinematics:** Rigid-body translation and rotation review
- **instantaneous center:** Instantaneous centers of zero velocity
- **four-bar linkage:** Four-bar linkage geometry and mobility
- **slider-crank mechanism:** Slider-crank displacement, velocity, and acceleration
- **gear velocity ratio:** Gear-pair angular speed relationships
- **compound and planetary gear train:** Compound and planetary gear trains
- **mechanism motion verification:** Mechanism mobility, interference, and motion verification

---

## What's Next

**Chapter 03-77: Mechanical Vibrations — Free, Forced, Damped, and Resonant Response**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
