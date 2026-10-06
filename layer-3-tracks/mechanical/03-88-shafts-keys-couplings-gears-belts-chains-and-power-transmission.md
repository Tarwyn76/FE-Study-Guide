---
chapter: "03-88"
title: "Shafts, Keys, Couplings, Gears, Belts, Chains, and Power Transmission"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-088-01, MEC-3-088-02, MEC-3-088-03, MEC-3-088-04, MEC-3-088-05, MEC-3-088-06, MEC-3-088-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-88: Shafts, Keys, Couplings, Gears, Belts, Chains, and Power Transmission

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MEC-3-076-07 · MEC-3-078-07

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Shafts, Keys, Couplings, Gears, Belts, Chains, and Power Transmission**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **88.1** Explain and apply **Shaft bending, torsion, and combined stress**.
* **88.2** Explain and apply **Fatigue design of rotating shafts**.
* **88.3** Explain and apply **Keys, splines, and couplings**.
* **88.4** Explain and apply **Spur-gear geometry and pitch relationships**.
* **88.5** Explain and apply **Gear forces and power transmission**.
* **88.6** Explain and apply **Lewis bending equation and gear-tooth strength**.
* **88.7** Explain and apply **Belts, chains, speed ratio, and transmission selection**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 88.1 Shaft bending, torsion, and combined stress

Shafts commonly carry bending and torque simultaneously. Combined-stress criteria convert these components into a design stress or required diameter.

\[\tau_{max}\sim \frac{16T}{\pi d^3},\qquad \sigma_b\sim\frac{32M}{\pi d^3}\]

![FIG-03-88-001: Stepped shaft with bearings, gear forces, bending moment, torque diagram, and critical section.](../figures/FIG-03-88-001-shaft-bending-torsion-and-combined-stress.png)

### Worked Example 1

**Problem.** Increasing shaft diameter strongly reduces bending and torsional stress because stress scales roughly with 1/d^3.

**Solution.** Apply the relation and model in §88.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 88.2 Fatigue design of rotating shafts

Rotating shafts often experience alternating bending plus steady or fluctuating torque. Fatigue design requires separating mean and alternating components and applying notch factors.

\[d^3\propto n\sqrt{\left(\frac{K_fM_a}{S_e}+\frac{M_m}{S_y}\right)^2+\left(\frac{K_{fs}T_a}{S_e}+\frac{T_m}{S_y}\right)^2}\]

![FIG-03-88-002: Rotating shaft stress history and mean/alternating bending-torque components.](../figures/FIG-03-88-002-fatigue-design-of-rotating-shafts.png)

### Worked Example 2

**Problem.** A stationary transverse load on a rotating shaft creates fully reversed bending at a material point.

**Solution.** Apply the relation and model in §88.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 88.3 Keys, splines, and couplings

Keys, splines, and couplings transmit torque between shafts and hubs while allowing selected assembly, alignment, or flexibility characteristics.

\[\text{torque transmitted by shear/bearing through the connection}\]

![FIG-03-88-003: Keyed joint, spline, rigid coupling, and flexible coupling with torque path.](../figures/FIG-03-88-003-keys-splines-and-couplings.png)

### Worked Example 3

**Problem.** A key must be checked for both shear and bearing/crushing under transmitted torque.

**Solution.** Apply the relation and model in §88.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 88.4 Spur-gear geometry and pitch relationships

Gear pitch geometry links tooth count, pitch diameter, circular pitch, module, and center distance. Mating gears must share compatible tooth geometry.

\[p_c=\frac{\pi d}{N},\qquad m=\frac dN\]

![FIG-03-88-004: Involute spur-gear pair labeling pitch circles, module, circular pitch, pressure angle, and center distance.](../figures/FIG-03-88-004-spur-gear-geometry-and-pitch-relationships.png)

### Worked Example 4

**Problem.** A 40-tooth gear with module 2 mm has pitch diameter 80 mm.

**Solution.** Apply the relation and model in §88.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 88.5 Gear forces and power transmission

Only the tangential tooth-force component transmits torque; the radial component loads shafts and bearings.

\[W_r=W_t\tan\phi,\qquad T=\frac{W_td}{2}\]

![FIG-03-88-005: Spur gear tooth line of action with W, Wt, Wr, pressure angle, and shaft torque.](../figures/FIG-03-88-005-gear-forces-and-power-transmission.png)

### Worked Example 5

**Problem.** For fixed torque, increasing pitch diameter reduces tangential tooth force.

**Solution.** Apply the relation and model in §88.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 88.6 Lewis bending equation and gear-tooth strength

The Lewis equation idealizes a gear tooth as a beam and estimates bending capacity from face width, tooth size, and form factor.

\[W_t=F Y\frac{1}{P}\sigma_{allow}\text{ in equivalent form}\]

![FIG-03-88-006: Single gear tooth modeled as a cantilever with tangential load, face width, and Lewis form factor.](../figures/FIG-03-88-006-lewis-bending-equation-and-gear-tooth-strength.png)

### Worked Example 6

**Problem.** Larger face width increases tooth bending capacity under the simplified relation.

**Solution.** Apply the relation and model in §88.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 88.7 Belts, chains, speed ratio, and transmission selection

Belt and chain drives provide flexible center distance and speed reduction/increase. Belts can slip and absorb shock; chains provide positive engagement but require lubrication/alignment.

\[\frac{\omega_2}{\omega_1}\approx\frac{D_1}{D_2}\]

![FIG-03-88-007: Open belt, timing belt, roller chain, and sprocket systems with speed ratios and tension sides.](../figures/FIG-03-88-007-belts-chains-speed-ratio-and-transmission-selection.png)

### Worked Example 7

**Problem.** A 2-in driver pulley and 6-in driven pulley give approximately 3:1 speed reduction without slip.

**Solution.** Apply the relation and model in §88.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

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

Primary source basis: **FE Mechanical specification Area(s) 14; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** The Mechanical specification includes both directly tabulated Handbook equations and learned design concepts. This chapter does not assign invented Handbook pages to specification-required material that is not directly tabulated.

---

## Where This Goes Wrong

**Using shaft combined loading outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using shaft fatigue design outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using shaft-hub connection outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using spur gear geometry outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using spur gear tooth force outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using Lewis gear tooth bending outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using belt and chain drive outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| shaft combined loading | Concept developed in §88.1; apply with that section's geometry and operating assumptions. |
| shaft fatigue design | Concept developed in §88.2; apply with that section's geometry and operating assumptions. |
| shaft-hub connection | Concept developed in §88.3; apply with that section's geometry and operating assumptions. |
| spur gear geometry | Concept developed in §88.4; apply with that section's geometry and operating assumptions. |
| spur gear tooth force | Concept developed in §88.5; apply with that section's geometry and operating assumptions. |
| Lewis gear tooth bending | Concept developed in §88.6; apply with that section's geometry and operating assumptions. |
| belt and chain drive | Concept developed in §88.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **shaft combined loading** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **shaft fatigue design** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **shaft-hub connection** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **spur gear geometry** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **spur gear tooth force** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **Lewis gear tooth bending** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **belt and chain drive** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **shaft combined loading**?

9. What geometric, material, operating, or model assumption must be checked before applying **shaft fatigue design**?

10. What geometric, material, operating, or model assumption must be checked before applying **shaft-hub connection**?

11. What geometric, material, operating, or model assumption must be checked before applying **spur gear geometry**?

12. What geometric, material, operating, or model assumption must be checked before applying **spur gear tooth force**?

13. What geometric, material, operating, or model assumption must be checked before applying **Lewis gear tooth bending**?

14. What geometric, material, operating, or model assumption must be checked before applying **belt and chain drive**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **shaft combined loading**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **shaft fatigue design**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **shaft-hub connection**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **spur gear geometry**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **spur gear tooth force**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **Lewis gear tooth bending**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **belt and chain drive**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **shaft combined loading**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **shaft fatigue design**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **shaft combined loading** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **shaft fatigue design** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **shaft-hub connection** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **spur gear geometry** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **spur gear tooth force** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **Lewis gear tooth bending** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **belt and chain drive** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **shaft combined loading**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **shaft fatigue design**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **shaft-hub connection**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **spur gear geometry**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **spur gear tooth force**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **Lewis gear tooth bending**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **belt and chain drive**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

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

1. Increasing shaft diameter strongly reduces bending and torsional stress because stress scales roughly with 1/d^3.

2. A stationary transverse load on a rotating shaft creates fully reversed bending at a material point.

3. A key must be checked for both shear and bearing/crushing under transmitted torque.

4. A 40-tooth gear with module 2 mm has pitch diameter 80 mm.

5. For fixed torque, increasing pitch diameter reduces tangential tooth force.

6. Larger face width increases tooth bending capacity under the simplified relation.

7. A 2-in driver pulley and 6-in driven pulley give approximately 3:1 speed reduction without slip.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. Use §88.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §88.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §88.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §88.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §88.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §88.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §88.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 14, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 14.

- **shaft combined loading:** Shaft bending, torsion, and combined stress
- **shaft fatigue design:** Fatigue design of rotating shafts
- **shaft-hub connection:** Keys, splines, and couplings
- **spur gear geometry:** Spur-gear geometry and pitch relationships
- **spur gear tooth force:** Gear forces and power transmission
- **Lewis gear tooth bending:** Lewis bending equation and gear-tooth strength
- **belt and chain drive:** Belts, chains, speed ratio, and transmission selection

---

## What's Next

**Chapter 03-89: Hydraulic, Pneumatic, and Electromechanical Components**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
