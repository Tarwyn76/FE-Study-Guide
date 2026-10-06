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

**Solution.** Apply the relation and model in §76.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 76.2 Instantaneous centers of zero velocity

For planar motion, a rigid body can be viewed instantaneously as rotating about a point with zero velocity. The instantaneous center simplifies velocity ratios but changes location with configuration.

\[v_P=\omega r_{P/IC}\]

![FIG-03-76-002: Four-bar link with perpendicular velocity lines locating the instantaneous center.](../figures/FIG-03-76-002-instantaneous-centers-of-zero-velocity.png)

### Worked Example 2

**Problem.** If a coupler point is 0.30 m from the IC and the link angular speed is 4 rad/s, its speed is 1.2 m/s.

**Solution.** Apply the relation and model in §76.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 76.3 Four-bar linkage geometry and mobility

A four-bar mechanism consists of ground plus three moving links connected by revolute joints. Position analysis is a vector loop-closure problem.

\[L_1+L_2+L_3+L_4\text{ close geometrically around the loop}\]

![FIG-03-76-003: Four-bar crank-rocker mechanism with link lengths, angles, ground pivots, and coupler point.](../figures/FIG-03-76-003-four-bar-linkage-geometry-and-mobility.png)

### Worked Example 3

**Problem.** A valid configuration must satisfy the vector loop closure; arbitrary link angles generally do not.

**Solution.** Apply the relation and model in §76.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 76.4 Slider-crank displacement, velocity, and acceleration

Slider-crank motion converts rotation to reciprocating translation. Differentiate the position constraint for velocity and acceleration when an exact relation is needed.

\[\mathbf r_{crank}+\mathbf r_{rod}=\mathbf r_{slider}\]

![FIG-03-76-004: Crank, connecting rod, slider, crank angle, stroke, and velocity vectors.](../figures/FIG-03-76-004-slider-crank-displacement-velocity-and-acceleration.png)

### Worked Example 4

**Problem.** At top-dead-center the slider velocity is zero even though crank angular speed can be nonzero.

**Solution.** Apply the relation and model in §76.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 76.5 Gear-pair angular speed relationships

External gears reverse direction and scale speed according to tooth count. Idler gears can change direction or spacing without changing the overall magnitude ratio.

\[\frac{\omega_{out}}{\omega_{in}}=-\frac{N_{in}}{N_{out}}\]

![FIG-03-76-005: Two spur gears with tooth counts, pitch circles, rotation directions, and speed ratio.](../figures/FIG-03-76-005-gear-pair-angular-speed-relationships.png)

### Worked Example 5

**Problem.** A 20-tooth driver turning at 1200 rpm drives a 60-tooth gear at 400 rpm in the opposite direction.

**Solution.** Apply the relation and model in §76.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 76.6 Compound and planetary gear trains

Compound trains multiply stage ratios. Planetary trains require relative-motion reasoning because sun, ring, and carrier can all move.

\[m_v=\frac{\prod N_{driven}}{\prod N_{driver}}\]

![FIG-03-76-006: Compound gear train and simple sun-planet-ring carrier set with angular velocities labeled.](../figures/FIG-03-76-006-compound-and-planetary-gear-trains.png)

### Worked Example 6

**Problem.** Two 3:1 reduction stages in series provide 9:1 speed reduction.

**Solution.** Apply the relation and model in §76.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 76.7 Mechanism mobility, interference, and motion verification

A numerical mechanism solution must satisfy link lengths, joint constraints, assembly branch, and motion continuity. Kinematic singularities can produce large velocity ratios.

\[\text{geometry}+\text{constraints}\rightarrow\text{physically possible motion}\]

![FIG-03-76-007: Mechanism swept envelope and a toggle/singularity configuration with transmission angle.](../figures/FIG-03-76-007-mechanism-mobility-interference-and-motion-verification.png)

### Worked Example 7

**Problem.** A calculated position that stretches a rigid link is invalid regardless of algebra.

**Solution.** Apply the relation and model in §76.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

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

1. Use §76.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §76.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §76.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §76.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §76.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §76.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §76.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 7, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

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
