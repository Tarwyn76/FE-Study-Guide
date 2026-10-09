---
chapter: "03-84"
title: "Mechanical Springs"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-084-01, MEC-3-084-02, MEC-3-084-03, MEC-3-084-04, MEC-3-084-05, MEC-3-084-06, MEC-3-084-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-84: Mechanical Springs

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** MAT-2B-016-01 · MECH-2C-022-03

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Mechanical Springs**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **84.1** Explain and apply **Compression-spring shear stress**.
* **84.2** Explain and apply **Compression-spring rate**.
* **84.3** Explain and apply **Series and parallel spring combinations**.
* **84.4** Explain and apply **Spring ends, solid length, pitch, and free length**.
* **84.5** Explain and apply **Spring material strength**.
* **84.6** Explain and apply **Helical torsion springs**.
* **84.7** Explain and apply **Spring energy, buckling, fatigue, and design checks**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 84.1 Compression-spring shear stress

Helical compression springs primarily load the wire in torsion. The Handbook provides a curvature correction factor based on spring index.

\[\tau=K_s\frac{8FD}{\pi d^3}\]

![FIG-03-84-001: Compression spring with F, mean diameter D, wire diameter d, and shear-stress detail.](../figures/FIG-03-84-001-compression-spring-shear-stress.png)

### Worked Example 1

**Problem.** Increasing wire diameter strongly reduces spring shear stress because d appears cubed.

**Solution.** \(\tau=K_s8FD/(\pi d^3)\). Holding \(F,D,K_s\) fixed gives \(\tau\propto d^{-3}\); increasing wire diameter therefore reduces shear stress very strongly.

---

## 84.2 Compression-spring rate

Spring stiffness increases strongly with wire diameter and decreases with coil diameter and active-coil count.

\[k=\frac{Gd^4}{8D^3N}\]

![FIG-03-84-002: Compression spring with free/loaded length and force-deflection line.](../figures/FIG-03-84-002-compression-spring-rate.png)

### Worked Example 2

**Problem.** Doubling active coils halves spring rate.

**Solution.** \(k=Gd^4/(8D^3N)\). With all other quantities fixed, doubling active coils gives \(k_2/k_1=N_1/N_2=1/2\), so spring rate is **halved**.

---

## 84.3 Series and parallel spring combinations

Series combinations soften a system; parallel combinations stiffen it. Compatibility and force distribution determine the correct relation.

\[\frac1{k_{eq}}=\sum\frac1{k_i},\qquad k_{eq}=\sum k_i\]

![FIG-03-84-003: Series and parallel spring arrangements with equivalent stiffness equations.](../figures/FIG-03-84-003-series-and-parallel-spring-combinations.png)

### Worked Example 3

**Problem.** Two identical k springs in parallel give 2k.

**Solution.** For identical springs, parallel deflections are equal and forces add, giving \(k_{eq}=k+k=\mathbf{2k}\). If each spring rate is stated in N/m, the equivalent rate is also in N/m. In series the same force passes through each spring and deflections add, giving \(k_{eq}=k/2\).

---

## 84.4 Spring ends, solid length, pitch, and free length

End style changes total coils, solid length, pitch, and seating behavior. Use the Handbook's end-condition table for the stated spring.

\[L_s\approx N_t d\text{ depending on end style}\]

![FIG-03-84-004: Four common compression-spring end styles with Ne, Nt, L0, Ls, and pitch.](../figures/FIG-03-84-004-spring-ends-solid-length-pitch-and-free-length.png)

### Worked Example 4

**Problem.** Squared-and-ground ends use different free/solid-length relationships than plain ends.

**Solution.** Solid length is set by the number of coils that stack at closure and by wire diameter; end style changes the relation between total coils, active coils, pitch, and free length. Use one consistent end-condition model rather than mixing tabulated formulas.

---

## 84.5 Spring material strength

Spring-wire tensile strength depends on material and wire diameter. Allowable torsional/bending stress is then related to tensile strength by the provided material relation.

\[S_{ut}=\frac{A}{d^m}\]

![FIG-03-84-005: Spring-wire tensile strength versus wire diameter for several common spring materials.](../figures/FIG-03-84-005-spring-material-strength.png)

### Worked Example 5

**Problem.** For the same material coefficients, larger wire diameter generally lowers tabulated minimum tensile strength by the power-law relation.

**Solution.** The empirical strength relation \(S_{ut}=A/d^m\) with \(m>0\) gives decreasing tensile strength as wire diameter increases. The trend is material/process specific and should use the stated coefficients rather than a universal exponent.

---

## 84.6 Helical torsion springs

Helical torsion springs store energy through bending of the wire rather than the same torsional stress state used for compression springs.

\[\sigma=K_i\frac{32Fr}{\pi d^3},\qquad Fr=k\theta\]

![FIG-03-84-006: Helical torsion spring with arm load F, radius r, rotation θ, and wire/coil dimensions.](../figures/FIG-03-84-006-helical-torsion-springs.png)

### Worked Example 6

**Problem.** Doubling moment Fr doubles bending stress under the linear formula.

**Solution.** For the stated torsion-spring relation, bending stress is proportional to applied moment \(Fr\). Doubling that moment with geometry unchanged therefore **doubles** the calculated stress.

---

## 84.7 Spring energy, buckling, fatigue, and design checks

A practical spring design also checks deflection range, solid height, buckling, surge, fatigue, and geometric manufacturability.

\[U=\frac12kx^2\]

![FIG-03-84-007: Spring design envelope showing operating load range, solid height, buckling slenderness, and fatigue cycle.](../figures/FIG-03-84-007-spring-energy-buckling-fatigue-and-design-checks.png)

### Worked Example 7

**Problem.** A compression spring must retain clearance before solid height at maximum service deflection.

**Solution.** Stored energy is \(U=\tfrac12kx^2\), but a usable compression spring must also avoid solid height, buckling, fatigue overstress, and loss of required clearance. Energy capacity alone is not a complete design check.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. A spring that reaches solid height, buckles, or exceeds fatigue/static limits is not acceptable even if its rate equation is correct. Re-size geometry/material and repeat all design checks.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Mechanical Springs**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **SHIGLEY** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 14; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Nisbett, K. J., & Budynas, R. G. *Shigley's Mechanical Engineering Design* (2024 Release). McGraw Hill. ISBN 978-1-265-47269-6. Supporting scope: Failure theories, fatigue, springs, pressure-vessel screening, bearings, fasteners, shafts, keys, couplings, gears, and machine-element design.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using compression spring stress outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using compression spring rate outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using equivalent spring stiffness outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using compression spring geometry outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using spring wire strength outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using torsion spring outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using spring design verification outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| compression spring stress | Concept developed in §84.1; apply with that section's geometry and operating assumptions. |
| compression spring rate | Concept developed in §84.2; apply with that section's geometry and operating assumptions. |
| equivalent spring stiffness | Concept developed in §84.3; apply with that section's geometry and operating assumptions. |
| compression spring geometry | Concept developed in §84.4; apply with that section's geometry and operating assumptions. |
| spring wire strength | Concept developed in §84.5; apply with that section's geometry and operating assumptions. |
| torsion spring | Concept developed in §84.6; apply with that section's geometry and operating assumptions. |
| spring design verification | Concept developed in §84.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **compression spring stress** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **compression spring rate** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **equivalent spring stiffness** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **compression spring geometry** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **spring wire strength** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **torsion spring** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **spring design verification** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **compression spring stress**?

9. What geometric, material, operating, or model assumption must be checked before applying **compression spring rate**?

10. What geometric, material, operating, or model assumption must be checked before applying **equivalent spring stiffness**?

11. What geometric, material, operating, or model assumption must be checked before applying **compression spring geometry**?

12. What geometric, material, operating, or model assumption must be checked before applying **spring wire strength**?

13. What geometric, material, operating, or model assumption must be checked before applying **torsion spring**?

14. What geometric, material, operating, or model assumption must be checked before applying **spring design verification**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **compression spring stress**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **compression spring rate**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **equivalent spring stiffness**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **compression spring geometry**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **spring wire strength**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **torsion spring**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **spring design verification**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **compression spring stress**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **compression spring rate**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **compression spring stress** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **compression spring rate** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **equivalent spring stiffness** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **compression spring geometry** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **spring wire strength** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **torsion spring** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **spring design verification** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **compression spring stress**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **compression spring rate**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **equivalent spring stiffness**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **compression spring geometry**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **spring wire strength**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **torsion spring**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **spring design verification**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

15. In **Mechanical Springs**, start from the physical model and system/component state, not from an isolated formula. A valid solution must check wire stress/rate, solid height and clearance, buckling, fatigue, end condition, and material strength rather than accepting spring rate alone.

16. Units and sign/reference conventions are part of the model in **Mechanical Springs**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Mechanical Springs**. External sources **SHIGLEY** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: double the active coil count and confirm rate halves; let spring deflection go to zero and confirm stored energy goes to zero. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §84.1, **Compression-spring shear stress**, uses \(\tau=K_s\frac{8FD}{\pi d^3}\). Apply it only under the geometry/material/operating assumptions stated in §84.1, then compare the result with the physical behavior described there.

20. **A.** Section §84.2, **Compression-spring rate**, uses \(k=\frac{Gd^4}{8D^3N}\). Apply it only under the geometry/material/operating assumptions stated in §84.2, then compare the result with the physical behavior described there.

21. **A.** Section §84.3, **Series and parallel spring combinations**, uses \(\frac1{k_{eq}}=\sum\frac1{k_i},\qquad k_{eq}=\sum k_i\). Apply it only under the geometry/material/operating assumptions stated in §84.3, then compare the result with the physical behavior described there.

22. **A.** Section §84.4, **Spring ends, solid length, pitch, and free length**, uses \(L_s\approx N_t d\text{ depending on end style}\). Apply it only under the geometry/material/operating assumptions stated in §84.4, then compare the result with the physical behavior described there.

23. **A.** Section §84.5, **Spring material strength**, uses \(S_{ut}=\frac{A}{d^m}\). Apply it only under the geometry/material/operating assumptions stated in §84.5, then compare the result with the physical behavior described there.

24. **A.** Section §84.6, **Helical torsion springs**, uses \(\sigma=K_i\frac{32Fr}{\pi d^3},\qquad Fr=k\theta\). Apply it only under the geometry/material/operating assumptions stated in §84.6, then compare the result with the physical behavior described there.

25. **A.** Section §84.7, **Spring energy, buckling, fatigue, and design checks**, uses \(U=\frac12kx^2\). Apply it only under the geometry/material/operating assumptions stated in §84.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Mechanical Springs** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** In the spring chapter, Handbook-supported spring relations remain the exam basis; Shigley supports learned fatigue, buckling, solid-height, and design-check material, while guide synthesis organizes the verification workflow.


---

## Practice Problems

1. Increasing wire diameter strongly reduces spring shear stress because d appears cubed.

2. Doubling active coils halves spring rate.

3. Two identical k springs in parallel give 2k.

4. Squared-and-ground ends use different free/solid-length relationships than plain ends.

5. For the same material coefficients, larger wire diameter generally lowers tabulated minimum tensile strength by the power-law relation.

6. Doubling moment Fr doubles bending stress under the linear formula.

7. A compression spring must retain clearance before solid height at maximum service deflection.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. **Independent check for §84.1 — Compression-spring shear stress.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(\tau=K_s8FD/(\pi d^3)\). Holding \(F,D,K_s\) fixed gives \(\tau\propto d^{-3}\); increasing wire diameter therefore reduces shear stress very strongly.

2. **Independent check for §84.2 — Compression-spring rate.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(k=Gd^4/(8D^3N)\). With all other quantities fixed, doubling active coils gives \(k_2/k_1=N_1/N_2=1/2\), so spring rate is **halved**.

3. **Independent check for §84.3 — Series and parallel spring combinations.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For identical springs, parallel deflections are equal and forces add, giving \(k_{eq}=k+k=\mathbf{2k}\). In series the same force passes through each spring and deflections add, giving \(k_{eq}=k/2\).

4. **Independent check for §84.4 — Spring ends, solid length, pitch, and free length.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Solid length is set by the number of coils that stack at closure and by wire diameter; end style changes the relation between total coils, active coils, pitch, and free length. Use one consistent end-condition model rather than mixing tabulated formulas.

5. **Independent check for §84.5 — Spring material strength.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. The empirical strength relation \(S_{ut}=A/d^m\) with \(m>0\) gives decreasing tensile strength as wire diameter increases. The trend is material/process specific and should use the stated coefficients rather than a universal exponent.

6. **Independent check for §84.6 — Helical torsion springs.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. For the stated torsion-spring relation, bending stress is proportional to applied moment \(Fr\). Doubling that moment with geometry unchanged therefore **doubles** the calculated stress.

7. **Independent check for §84.7 — Spring energy, buckling, fatigue, and design checks.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Stored energy is \(U=\tfrac12kx^2\), but a usable compression spring must also avoid solid height, buckling, fatigue overstress, and loss of required clearance. Energy capacity alone is not a complete design check.

8. For **Mechanical Springs**, one required acceptance screen is: check wire stress/rate, solid height and clearance, buckling, fatigue, end condition, and material strength rather than accepting spring rate alone. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Mechanical Springs**. For `split_required` concepts, use **SHIGLEY** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: double the active coil count and confirm rate halves; let spring deflection go to zero and confirm stored energy goes to zero. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 14.

- **compression spring stress:** Compression-spring shear stress
- **compression spring rate:** Compression-spring rate
- **equivalent spring stiffness:** Series and parallel spring combinations
- **compression spring geometry:** Spring ends, solid length, pitch, and free length
- **spring wire strength:** Spring material strength
- **torsion spring:** Helical torsion springs
- **spring design verification:** Spring energy, buckling, fatigue, and design checks

---

## What's Next

**Chapter 03-85: Pressure Vessels and Piping**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
