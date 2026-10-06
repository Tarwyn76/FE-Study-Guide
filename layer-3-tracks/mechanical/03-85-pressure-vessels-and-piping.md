---
chapter: "03-85"
title: "Pressure Vessels and Piping"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-085-01, MEC-3-085-02, MEC-3-085-03, MEC-3-085-04, MEC-3-085-05, MEC-3-085-06, MEC-3-085-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-85: Pressure Vessels and Piping

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MECH-2C-022-03 · MAT-2B-016-01

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Pressure Vessels and Piping**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **85.1** Explain and apply **Thin-walled cylindrical hoop stress**.
* **85.2** Explain and apply **Longitudinal stress in cylindrical vessels**.
* **85.3** Explain and apply **Thin spherical pressure vessels**.
* **85.4** Explain and apply **Piping pressure stress and wall-thickness reasoning**.
* **85.5** Explain and apply **Thermal expansion and restraint in piping**.
* **85.6** Explain and apply **Nozzles, supports, and combined vessel loads**.
* **85.7** Explain and apply **Pressure-boundary safety and model validity**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 85.1 Thin-walled cylindrical hoop stress

For a thin-walled closed cylinder, hoop stress is twice the longitudinal membrane stress. Thin-wall assumptions require wall thickness small relative to radius.

\[\sigma_h=\frac{pr}{t}\]

![FIG-03-85-001: Thin cylindrical pressure vessel cut showing internal pressure, hoop stress, longitudinal stress, r, and t.](../figures/FIG-03-85-001-thin-walled-cylindrical-hoop-stress.png)

### Worked Example 1

**Problem.** p=2 MPa, r=0.5 m, t=0.01 m gives σh=100 MPa.

**Solution.** Apply the relation and model in §85.1; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 85.2 Longitudinal stress in cylindrical vessels

Closed-end pressure creates axial force carried by the shell. This gives half the thin-wall hoop stress for a cylinder.

\[\sigma_l=\frac{pr}{2t}\]

![FIG-03-85-002: Pressure-vessel end-cap free-body diagram balancing pressure force and shell longitudinal stress.](../figures/FIG-03-85-002-longitudinal-stress-in-cylindrical-vessels.png)

### Worked Example 2

**Problem.** Using the prior example gives σl=50 MPa.

**Solution.** Apply the relation and model in §85.2; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 85.3 Thin spherical pressure vessels

A thin sphere carries equal membrane stress in all tangent directions and is structurally efficient for internal pressure.

\[\sigma=\frac{pr}{2t}\]

![FIG-03-85-003: Cut spherical pressure vessel with membrane stress and pressure resultant.](../figures/FIG-03-85-003-thin-spherical-pressure-vessels.png)

### Worked Example 3

**Problem.** At the same p, r, and t, sphere membrane stress equals the cylindrical longitudinal stress.

**Solution.** Apply the relation and model in §85.3; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 85.4 Piping pressure stress and wall-thickness reasoning

Piping design adds code factors, corrosion allowance, joints, temperature, and loads beyond simple membrane stress. FE problems may isolate the thin-wall mechanical relation.

\[t\gtrsim\frac{pr}{S_{allow}}\text{ in a simplified thin-wall screen}\]

![FIG-03-85-004: Pressurized pipe cross-section with wall thickness, corrosion allowance, and hoop stress.](../figures/FIG-03-85-004-piping-pressure-stress-and-wall-thickness-reasoning.png)

### Worked Example 4

**Problem.** Increasing allowable stress reduces required idealized wall thickness, all else equal.

**Solution.** Apply the relation and model in §85.4; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 85.5 Thermal expansion and restraint in piping

Unrestrained pipe expands thermally without stress; restraint converts expansion into reaction load and stress. Real systems use flexibility, guides, anchors, and expansion devices.

\[\Delta L=\alpha L\Delta T,\qquad \sigma=E\alpha\Delta T\text{ if fully restrained elastically}\]

![FIG-03-85-005: Anchored versus freely expanding pipe with ΔL, thermal strain, and reaction forces.](../figures/FIG-03-85-005-thermal-expansion-and-restraint-in-piping.png)

### Worked Example 5

**Problem.** A freely expanding pipe has thermal strain but ideally no axial thermal stress.

**Solution.** Apply the relation and model in §85.5; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 85.6 Nozzles, supports, and combined vessel loads

Real vessels and piping experience support reactions, weight, wind/seismic, nozzle loads, and thermal effects in addition to pressure.

\[\text{combined stress includes pressure plus weight, piping, thermal, and local loads}\]

![FIG-03-85-006: Vertical vessel with supports, nozzle loads, weight, pressure, wind, and thermal expansion arrows.](../figures/FIG-03-85-006-nozzles-supports-and-combined-vessel-loads.png)

### Worked Example 6

**Problem.** A nozzle load can create local bending not represented by simple membrane equations.

**Solution.** Apply the relation and model in §85.6; then verify geometry, units, operating regime, and the relevant failure/performance check.

---

## 85.7 Pressure-boundary safety and model validity

FE equations are screening models, not substitutes for pressure-vessel or piping codes. Always check whether thin-wall assumptions and load cases apply.

\[\text{verify thin-wall validity, allowable stress, joints, cyclic loading, temperature, and code requirements}\]

![FIG-03-85-007: Decision flow from geometry and pressure to thin/thick-wall model, load cases, material allowables, and code verification.](../figures/FIG-03-85-007-pressure-boundary-safety-and-model-validity.png)

### Worked Example 7

**Problem.** A thick-walled vessel should not be analyzed with thin-wall membrane equations without justification.

**Solution.** Apply the relation and model in §85.7; then verify geometry, units, operating regime, and the relevant failure/performance check.

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

**Using cylindrical hoop stress outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using cylindrical longitudinal stress outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using spherical pressure vessel outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using pipe pressure design outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using piping thermal stress outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using vessel combined loading outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using pressure vessel design check outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| cylindrical hoop stress | Concept developed in §85.1; apply with that section's geometry and operating assumptions. |
| cylindrical longitudinal stress | Concept developed in §85.2; apply with that section's geometry and operating assumptions. |
| spherical pressure vessel | Concept developed in §85.3; apply with that section's geometry and operating assumptions. |
| pipe pressure design | Concept developed in §85.4; apply with that section's geometry and operating assumptions. |
| piping thermal stress | Concept developed in §85.5; apply with that section's geometry and operating assumptions. |
| vessel combined loading | Concept developed in §85.6; apply with that section's geometry and operating assumptions. |
| pressure vessel design check | Concept developed in §85.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **cylindrical hoop stress** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **cylindrical longitudinal stress** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **spherical pressure vessel** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **pipe pressure design** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **piping thermal stress** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **vessel combined loading** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **pressure vessel design check** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **cylindrical hoop stress**?

9. What geometric, material, operating, or model assumption must be checked before applying **cylindrical longitudinal stress**?

10. What geometric, material, operating, or model assumption must be checked before applying **spherical pressure vessel**?

11. What geometric, material, operating, or model assumption must be checked before applying **pipe pressure design**?

12. What geometric, material, operating, or model assumption must be checked before applying **piping thermal stress**?

13. What geometric, material, operating, or model assumption must be checked before applying **vessel combined loading**?

14. What geometric, material, operating, or model assumption must be checked before applying **pressure vessel design check**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **cylindrical hoop stress**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **cylindrical longitudinal stress**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **spherical pressure vessel**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **pipe pressure design**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **piping thermal stress**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **vessel combined loading**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **pressure vessel design check**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **cylindrical hoop stress**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **cylindrical longitudinal stress**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **cylindrical hoop stress** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **cylindrical longitudinal stress** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **spherical pressure vessel** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **pipe pressure design** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **piping thermal stress** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **vessel combined loading** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **pressure vessel design check** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **cylindrical hoop stress**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **cylindrical longitudinal stress**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **spherical pressure vessel**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **pipe pressure design**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **piping thermal stress**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **vessel combined loading**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **pressure vessel design check**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

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

1. p=2 MPa, r=0.5 m, t=0.01 m gives σh=100 MPa.

2. Using the prior example gives σl=50 MPa.

3. At the same p, r, and t, sphere membrane stress equals the cylindrical longitudinal stress.

4. Increasing allowable stress reduces required idealized wall thickness, all else equal.

5. A freely expanding pipe has thermal strain but ideally no axial thermal stress.

6. A nozzle load can create local bending not represented by simple membrane equations.

7. A thick-walled vessel should not be analyzed with thin-wall membrane equations without justification.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. Use §85.1. Apply the stated relation/workflow, then verify model validity and physical feasibility.

2. Use §85.2. Apply the stated relation/workflow, then verify model validity and physical feasibility.

3. Use §85.3. Apply the stated relation/workflow, then verify model validity and physical feasibility.

4. Use §85.4. Apply the stated relation/workflow, then verify model validity and physical feasibility.

5. Use §85.5. Apply the stated relation/workflow, then verify model validity and physical feasibility.

6. Use §85.6. Apply the stated relation/workflow, then verify model validity and physical feasibility.

7. Use §85.7. Apply the stated relation/workflow, then verify model validity and physical feasibility.

8. Check dimensions, load direction, support/interface assumptions, material regime, fatigue/static basis, operating speed/temperature/pressure, and any geometric validity limit such as thin-wall or small-deflection assumptions.

9. Start with FE Mechanical specification Area(s) 14, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a simple limit such as zero load, very large stiffness, matched speed ratio, zero pressure, zero damping, or maximum/minimum fit. Confirm the result trends in the physically expected direction and remains manufacturable.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 14.

- **cylindrical hoop stress:** Thin-walled cylindrical hoop stress
- **cylindrical longitudinal stress:** Longitudinal stress in cylindrical vessels
- **spherical pressure vessel:** Thin spherical pressure vessels
- **pipe pressure design:** Piping pressure stress and wall-thickness reasoning
- **piping thermal stress:** Thermal expansion and restraint in piping
- **vessel combined loading:** Nozzles, supports, and combined vessel loads
- **pressure vessel design check:** Pressure-boundary safety and model validity

---

## What's Next

**Chapter 03-86: Bearings and Lubrication**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
