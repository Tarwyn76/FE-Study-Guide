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

**Solution.** \(\sigma_h=pr/t=(2\ {\rm MPa})(0.5\ {\rm m})/(0.01\ {\rm m})=\mathbf{100\ MPa}\). This thin-wall membrane result requires a sufficiently small wall-thickness-to-radius ratio.

---

## 85.2 Longitudinal stress in cylindrical vessels

Closed-end pressure creates axial force carried by the shell. This gives half the thin-wall hoop stress for a cylinder.

\[\sigma_l=\frac{pr}{2t}\]

![FIG-03-85-002: Pressure-vessel end-cap free-body diagram balancing pressure force and shell longitudinal stress.](../figures/FIG-03-85-002-longitudinal-stress-in-cylindrical-vessels.png)

### Worked Example 2

**Problem.** Using the prior example gives σl=50 MPa.

**Solution.** \(\sigma_l=pr/(2t)=\mathbf{50\ MPa}\) using the same \(p,r,t\). Thus the ideal cylindrical hoop stress is twice the longitudinal membrane stress.

---

## 85.3 Thin spherical pressure vessels

A thin sphere carries equal membrane stress in all tangent directions and is structurally efficient for internal pressure.

\[\sigma=\frac{pr}{2t}\]

![FIG-03-85-003: Cut spherical pressure vessel with membrane stress and pressure resultant.](../figures/FIG-03-85-003-thin-spherical-pressure-vessels.png)

### Worked Example 3

**Problem.** At the same p, r, and t, sphere membrane stress equals the cylindrical longitudinal stress.

**Solution.** A thin spherical vessel has membrane stress \(\sigma=pr/(2t)\), so with the same \(p,r,t\) its ideal membrane stress equals the cylindrical longitudinal stress: **50 MPa** for the preceding values.

---

## 85.4 Piping pressure stress and wall-thickness reasoning

Piping design adds code factors, corrosion allowance, joints, temperature, and loads beyond simple membrane stress. FE problems may isolate the thin-wall mechanical relation.

\[t\gtrsim\frac{pr}{S_{allow}}\text{ in a simplified thin-wall screen}\]

![FIG-03-85-004: Pressurized pipe cross-section with wall thickness, corrosion allowance, and hoop stress.](../figures/FIG-03-85-004-piping-pressure-stress-and-wall-thickness-reasoning.png)

### Worked Example 4

**Problem.** Increasing allowable stress reduces required idealized wall thickness, all else equal.

**Solution.** In the simple thin-wall screening form \(t\sim pr/S_{allow}\), increasing allowable stress decreases the required ideal thickness. A code design must still include the applicable factors, corrosion allowance, joint efficiency, load cases, and minimum-thickness rules.

---

## 85.5 Thermal expansion and restraint in piping

Unrestrained pipe expands thermally without stress; restraint converts expansion into reaction load and stress. Real systems use flexibility, guides, anchors, and expansion devices.

\[\Delta L=\alpha L\Delta T,\qquad \sigma=E\alpha\Delta T\text{ if fully restrained elastically}\]

![FIG-03-85-005: Anchored versus freely expanding pipe with ΔL, thermal strain, and reaction forces.](../figures/FIG-03-85-005-thermal-expansion-and-restraint-in-piping.png)

### Worked Example 5

**Problem.** A freely expanding pipe has thermal strain but ideally no axial thermal stress.

**Solution.** For free expansion, \(\Delta L=\alpha L\Delta T\) and the member develops strain without ideal axial thermal stress. If fully restrained and still elastic, \(\sigma=E\alpha\Delta T\); partial restraint lies between those limiting cases.

---

## 85.6 Nozzles, supports, and combined vessel loads

Real vessels and piping experience support reactions, weight, wind/seismic, nozzle loads, and thermal effects in addition to pressure.

\[\text{combined stress includes pressure plus weight, piping, thermal, and local loads}\]

![FIG-03-85-006: Vertical vessel with supports, nozzle loads, weight, pressure, wind, and thermal expansion arrows.](../figures/FIG-03-85-006-nozzles-supports-and-combined-vessel-loads.png)

### Worked Example 6

**Problem.** A nozzle load can create local bending not represented by simple membrane equations.

**Solution.** Simple membrane pressure stress does not capture local nozzle forces/moments. Connected piping, weight, thermal displacement, and external loads can create local bending and stress intensification that require separate evaluation.

---

## 85.7 Pressure-boundary safety and model validity

FE equations are screening models, not substitutes for pressure-vessel or piping codes. Always check whether thin-wall assumptions and load cases apply.

\[\text{verify thin-wall validity, allowable stress, joints, cyclic loading, temperature, and code requirements}\]

![FIG-03-85-007: Decision flow from geometry and pressure to thin/thick-wall model, load cases, material allowables, and code verification.](../figures/FIG-03-85-007-pressure-boundary-safety-and-model-validity.png)

### Worked Example 7

**Problem.** A thick-walled vessel should not be analyzed with thin-wall membrane equations without justification.

**Solution.** Thin-wall equations are screening relations, not universal vessel rules. Verify geometry validity, material allowable stress, temperature, joints, cyclic service, openings/local loads, and the applicable pressure-vessel or piping code before release.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. A pressure-boundary result is invalid when thin-wall assumptions, temperature, local loads, fatigue, or code requirements are violated. Use the appropriate vessel/piping method rather than extrapolating a membrane formula.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Pressure Vessels and Piping**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **SHIGLEY, BPVCVIII, B313** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 14; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Nisbett, K. J., & Budynas, R. G. *Shigley's Mechanical Engineering Design* (2024 Release). McGraw Hill. ISBN 978-1-265-47269-6. Supporting scope: Failure theories, fatigue, springs, pressure-vessel screening, bearings, fasteners, shafts, keys, couplings, gears, and machine-element design.
- ASME. (2025). *Boiler and Pressure Vessel Code, Section VIII—Rules for Construction of Pressure Vessels, Division 1*. Supporting scope: Pressure-vessel construction requirements, pressure boundary design context, materials, fabrication, examination, and testing.
- ASME. (2024). *Process Piping* (ASME B31.3-2024). Supporting scope: Process piping materials, design, flexibility, fabrication, assembly, examination, inspection, and testing.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Pressure Vessels and Piping**, start from the physical model and system/component state, not from an isolated formula. A valid solution must verify thin-wall applicability, pressure/temperature/material basis, thermal restraint, local/nozzle/piping loads, and the applicable pressure-boundary code.

16. Units and sign/reference conventions are part of the model in **Pressure Vessels and Piping**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Pressure Vessels and Piping**. External sources **SHIGLEY, BPVCVIII, B313** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: halve internal pressure and confirm ideal thin-wall membrane stresses halve; remove restraint and confirm ideal thermal stress falls to zero while free expansion remains. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §85.1, **Thin-walled cylindrical hoop stress**, uses \(\sigma_h=\frac{pr}{t}\). Apply it only under the geometry/material/operating assumptions stated in §85.1, then compare the result with the physical behavior described there.

20. **A.** Section §85.2, **Longitudinal stress in cylindrical vessels**, uses \(\sigma_l=\frac{pr}{2t}\). Apply it only under the geometry/material/operating assumptions stated in §85.2, then compare the result with the physical behavior described there.

21. **A.** Section §85.3, **Thin spherical pressure vessels**, uses \(\sigma=\frac{pr}{2t}\). Apply it only under the geometry/material/operating assumptions stated in §85.3, then compare the result with the physical behavior described there.

22. **A.** Section §85.4, **Piping pressure stress and wall-thickness reasoning**, uses \(t\gtrsim\frac{pr}{S_{allow}}\text{ in a simplified thin-wall screen}\). Apply it only under the geometry/material/operating assumptions stated in §85.4, then compare the result with the physical behavior described there.

23. **A.** Section §85.5, **Thermal expansion and restraint in piping**, uses \(\Delta L=\alpha L\Delta T,\qquad \sigma=E\alpha\Delta T\text{ if fully restrained elastically}\). Apply it only under the geometry/material/operating assumptions stated in §85.5, then compare the result with the physical behavior described there.

24. **A.** Section §85.6, **Nozzles, supports, and combined vessel loads**, uses \(\text{combined stress includes pressure plus weight, piping, thermal, and local loads}\). Apply it only under the geometry/material/operating assumptions stated in §85.6, then compare the result with the physical behavior described there.

25. **A.** Section §85.7, **Pressure-boundary safety and model validity**, uses \(\text{verify thin-wall validity, allowable stress, joints, cyclic loading, temperature, and code requirements}\). Apply it only under the geometry/material/operating assumptions stated in §85.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Pressure Vessels and Piping** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **SHIGLEY, BPVCVIII, B313**; guide synthesis is supplemental explanation and exam-oriented workflow.


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

1. **Independent check for §85.1 — Thin-walled cylindrical hoop stress.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\sigma_h=pr/t=(2\ {\rm MPa})(0.5\ {\rm m})/(0.01\ {\rm m})=\mathbf{100\ MPa}\). This thin-wall membrane result requires a sufficiently small wall-thickness-to-radius ratio.

2. **Independent check for §85.2 — Longitudinal stress in cylindrical vessels.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\sigma_l=pr/(2t)=\mathbf{50\ MPa}\) using the same \(p,r,t\). Thus the ideal cylindrical hoop stress is twice the longitudinal membrane stress.

3. **Independent check for §85.3 — Thin spherical pressure vessels.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A thin spherical vessel has membrane stress \(\sigma=pr/(2t)\), so with the same \(p,r,t\) its ideal membrane stress equals the cylindrical longitudinal stress: **50 MPa** for the preceding values.

4. **Independent check for §85.4 — Piping pressure stress and wall-thickness reasoning.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. In the simple thin-wall screening form \(t\sim pr/S_{allow}\), increasing allowable stress decreases the required ideal thickness. A code design must still include the applicable factors, corrosion allowance, joint efficiency, load cases, and minimum-thickness rules.

5. **Independent check for §85.5 — Thermal expansion and restraint in piping.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For free expansion, \(\Delta L=\alpha L\Delta T\) and the member develops strain without ideal axial thermal stress. If fully restrained and still elastic, \(\sigma=E\alpha\Delta T\); partial restraint lies between those limiting cases.

6. **Independent check for §85.6 — Nozzles, supports, and combined vessel loads.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Simple membrane pressure stress does not capture local nozzle forces/moments. Connected piping, weight, thermal displacement, and external loads can create local bending and stress intensification that require separate evaluation.

7. **Independent check for §85.7 — Pressure-boundary safety and model validity.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Thin-wall equations are screening relations, not universal vessel rules. Verify geometry validity, material allowable stress, temperature, joints, cyclic service, openings/local loads, and the applicable pressure-vessel or piping code before release.

8. For **Pressure Vessels and Piping**, one required acceptance screen is: verify thin-wall applicability, pressure/temperature/material basis, thermal restraint, local/nozzle/piping loads, and the applicable pressure-boundary code. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Pressure Vessels and Piping**. For `split_required` concepts, use **SHIGLEY, BPVCVIII, B313** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: halve internal pressure and confirm ideal thin-wall membrane stresses halve; remove restraint and confirm ideal thermal stress falls to zero while free expansion remains. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

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
