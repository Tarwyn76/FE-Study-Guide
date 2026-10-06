---
chapter: "03-05"
title: "Molecular Diffusion and Convective Mass Transfer"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-005-01, CHE-3-005-02, CHE-3-005-03, CHE-3-005-04, CHE-3-005-05, CHE-3-005-06, CHE-3-005-07]
routes: [chemical]
status: drafted
---

# Chapter 03-05: Molecular Diffusion and Convective Mass Transfer

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 02-45 Internal Flow · 02-57 Convection · 02-18 Diffusion and Processing

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly provides Fick's laws, error-function diffusion, gas/liquid diffusion forms, stagnant-gas and equimolar counterdiffusion, two-film theory, overall mass-transfer coefficients, Sherwood correlations, and heat/mass/momentum analogies.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **5.1** Explain and apply **Fick's First Law**.
* **5.2** Explain and apply **Fick's Second Law and Unsteady Diffusion**.
* **5.3** Explain and apply **Diffusion of A Through Stagnant B**.
* **5.4** Explain and apply **Equimolar Counter-Diffusion**.
* **5.5** Explain and apply **Two-Film Theory**.
* **5.6** Explain and apply **Overall Mass-Transfer Coefficients**.
* **5.7** Explain and apply **Sherwood Correlations and Transport Analogies**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 5.1 Fick's First Law

Fick's first law relates diffusive flux to concentration gradient. The negative sign indicates diffusion down the concentration gradient.

The Handbook defines a diffusion coefficient with units of area per time.

\[J_A=-D_{AB}\frac{dC_A}{dx}\]

![FIG-03-05-001: Concentration profile across a film with diffusive flux from high to low concentration.](../figures/FIG-03-05-001-fick-s-first-law.png)

### Worked Example 1

**Problem.** D=1e-9 m²/s and dC/dx=-2e6 mol/m⁴. Find J.

**Solution.** J=-D dC/dx=0.002 mol/(m²·s).

---

## 5.2 Fick's Second Law and Unsteady Diffusion

For one-dimensional diffusion with constant diffusivity and no reaction, the concentration field follows the diffusion equation. The Handbook gives an error-function solution for a semi-infinite medium with a suddenly imposed surface concentration.

The relevant diffusion length grows approximately with \(\sqrt{Dt}\).

\[\frac{\partial C}{\partial t}=D\frac{\partial^2C}{\partial x^2}\]

![FIG-03-05-002: Semi-infinite slab with surface concentration step and concentration profiles broadening with time.](../figures/FIG-03-05-002-fick-s-second-law-and-unsteady-diffusion.png)

### Worked Example 2

**Problem.** For diffusion length estimate sqrt(Dt), D=1e-10 m²/s and t=10,000 s. Find scale.

**Solution.** sqrt(1e-6)=0.001 m=1 mm.

---

## 5.3 Diffusion of A Through Stagnant B

For a gas A diffusing through stagnant gas B, bulk molar motion changes the relation from simple equimolar diffusion. The Handbook uses a log-mean partial pressure of B.

This case appears in evaporation through a stagnant gas film.

\[N_A=\frac{D_{AB}P}{RT(z_2-z_1)}\frac{p_{A1}-p_{A2}}{(p_B)_{lm}}\]

![FIG-03-05-003: Species A diffusing through a stagnant B film with endpoint partial pressures and log-mean B pressure.](../figures/FIG-03-05-003-diffusion-of-a-through-stagnant-b.png)

### Worked Example 3

**Problem.** State why stagnant-B diffusion differs from equimolar counterdiffusion.

**Solution.** There is net molar bulk motion when B has zero molar flux.

---

## 5.4 Equimolar Counter-Diffusion

When A and B diffuse in opposite directions with equal molar rates, total molar flux is zero and the expression simplifies.

The concentration or partial-pressure profile is linear when diffusivity and other properties are constant.

\[N_A=-N_B=\frac{D_{AB}}{RT}\frac{p_{A1}-p_{A2}}{z_2-z_1}\]

![FIG-03-05-004: Binary gas film with equal opposite molar fluxes and linear partial-pressure profiles.](../figures/FIG-03-05-004-equimolar-counter-diffusion.png)

### Worked Example 4

**Problem.** For equimolar diffusion, D=2e-5, Δp=10 kPa, T=300 K, L=0.01 m. Estimate NA.

**Solution.** NA=DΔp/(RTL)=2e-5×10000/(8.314×300×0.01)=0.00802 mol/(m²·s).

---

## 5.5 Two-Film Theory

Two-film theory places gas-side and liquid-side resistances in thin layers adjacent to the interface. Interfacial compositions are in equilibrium, while bulk phases may not be.

Mass flux can be expressed with gas-side or liquid-side individual coefficients.

\[N_A=k_G'(p_{AG}-p_{Ai})=k_L'(C_{Ai}-C_{AL})\]

![FIG-03-05-005: Gas-liquid interface with gas film, liquid film, bulk compositions, interfacial equilibrium values, and flux.](../figures/FIG-03-05-005-two-film-theory.png)

### Worked Example 5

**Problem.** kg'=0.10 mol/(m²·s·kPa), bulk-interface Δp=2 kPa. Find flux.

**Solution.** NA=0.20 mol/(m²·s).

---

## 5.6 Overall Mass-Transfer Coefficients

Overall coefficients eliminate the unknown interface composition by combining phase resistances with the equilibrium relation. For Henry-law equilibrium, the Handbook gives reciprocal-resistance forms.

The controlling resistance is the larger resistance after both are expressed on the same basis.

\[\frac1{K_G'}=\frac1{k_G'}+\frac{H}{k_L'},\qquad \frac1{K_L'}=\frac1{Hk_G'}+\frac1{k_L'}\]

![FIG-03-05-006: Gas-side and liquid-side mass-transfer resistances in series with Henry-law coupling.](../figures/FIG-03-05-006-overall-mass-transfer-coefficients.png)

### Worked Example 6

**Problem.** 1/kG=2 and H/kL=8 in common reciprocal units. What fraction of total resistance is liquid-side?

**Solution.** 8/(2+8)=80%.

---

## 5.7 Sherwood Correlations and Transport Analogies

The Handbook defines Sherwood, Schmidt, Reynolds, Nusselt, Prandtl, and Stanton numbers and gives turbulent transport analogies.

Use the correlation only within its stated geometry and regime. Heat-transfer intuition is useful because momentum, heat, and mass transfer share similar gradient and coefficient structures.

\[Sh=\frac{k_mD}{D_{AB}},\qquad Sc=\frac{\mu}{\rho D_{AB}}\]

![FIG-03-05-007: Parallel momentum, heat, and mass-transfer boundary layers with Re/Pr/Sc and Nu/Sh analogies.](../figures/FIG-03-05-007-sherwood-correlations-and-transport-analogies.png)

### Worked Example 7

**Problem.** D=0.05 m, km=0.02 m/s, DAB=1e-5 m²/s. Find Sherwood number.

**Solution.** Sh=kmD/DAB=100.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** If concentration profile is flat, what is Fickian diffusive flux?

**Solution.** Zero.

### Worked Example 9

**Problem.** If both individual phase resistances halve, what happens qualitatively to overall K?

**Solution.** Overall resistance halves, so K approximately doubles.

---

## As the Handbook States It

Primary source basis: **Chemical Engineering, printed pp. 247–255; FE Chemical specification Area 10A–B**.

**Source boundary:** The Handbook directly provides Fick's laws, error-function diffusion, gas/liquid diffusion forms, stagnant-gas and equimolar counterdiffusion, two-film theory, overall mass-transfer coefficients, Sherwood correlations, and heat/mass/momentum analogies.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using Fick first law without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using unsteady molecular diffusion without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using stagnant-gas diffusion without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using equimolar counterdiffusion without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using two-film mass transfer without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using overall mass-transfer coefficient without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using Sherwood mass-transfer correlation without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| Fick first law | Concept developed in §5.1; apply with the section's stated basis and assumptions. |
| unsteady molecular diffusion | Concept developed in §5.2; apply with the section's stated basis and assumptions. |
| stagnant-gas diffusion | Concept developed in §5.3; apply with the section's stated basis and assumptions. |
| equimolar counterdiffusion | Concept developed in §5.4; apply with the section's stated basis and assumptions. |
| two-film mass transfer | Concept developed in §5.5; apply with the section's stated basis and assumptions. |
| overall mass-transfer coefficient | Concept developed in §5.6; apply with the section's stated basis and assumptions. |
| Sherwood mass-transfer correlation | Concept developed in §5.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **Fick first law** and state the governing relation or balance.

2. Define **unsteady molecular diffusion** and state the governing relation or balance.

3. Define **stagnant-gas diffusion** and state the governing relation or balance.

4. Define **equimolar counterdiffusion** and state the governing relation or balance.

5. Define **two-film mass transfer** and state the governing relation or balance.

6. Define **overall mass-transfer coefficient** and state the governing relation or balance.

7. Define **Sherwood mass-transfer correlation** and state the governing relation or balance.

8. What is the most likely error if **Fick first law** is applied before the process basis and boundary are defined?

9. What is the most likely error if **unsteady molecular diffusion** is applied before the process basis and boundary are defined?

10. What is the most likely error if **stagnant-gas diffusion** is applied before the process basis and boundary are defined?

11. What is the most likely error if **equimolar counterdiffusion** is applied before the process basis and boundary are defined?

12. What is the most likely error if **two-film mass transfer** is applied before the process basis and boundary are defined?

13. What is the most likely error if **overall mass-transfer coefficient** is applied before the process basis and boundary are defined?

14. What is the most likely error if **Sherwood mass-transfer correlation** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **Fick first law**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **unsteady molecular diffusion**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **stagnant-gas diffusion**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **equimolar counterdiffusion**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **two-film mass transfer**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **overall mass-transfer coefficient**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **Sherwood mass-transfer correlation**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **Fick first law**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **unsteady molecular diffusion**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **Fick first law** is developed in §5.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **unsteady molecular diffusion** is developed in §5.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **stagnant-gas diffusion** is developed in §5.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **equimolar counterdiffusion** is developed in §5.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **two-film mass transfer** is developed in §5.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **overall mass-transfer coefficient** is developed in §5.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **Sherwood mass-transfer correlation** is developed in §5.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

8. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

9. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

10. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

11. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

12. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

13. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

14. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

15. The material balance determines the amounts and compositions needed for enthalpy and reaction-energy calculations.

16. To verify that the unknowns are matched by independent equations/specifications before algebra begins.

17. Whenever the problem provides the model/data; use that stated relation rather than substituting an unstated correlation.

18. The Handbook intentionally omits some theories and formulas; exam specifications can require knowledge not directly tabulated in it.

19. **A.** The relation or workflow for **Fick first law** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **unsteady molecular diffusion** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **stagnant-gas diffusion** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **equimolar counterdiffusion** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **two-film mass transfer** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **overall mass-transfer coefficient** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **Sherwood mass-transfer correlation** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **Fick first law** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

27. **A.** The relation or workflow for **unsteady molecular diffusion** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. D=1e-9 m²/s and dC/dx=-2e6 mol/m⁴. Find J.

2. For diffusion length estimate sqrt(Dt), D=1e-10 m²/s and t=10,000 s. Find scale.

3. State why stagnant-B diffusion differs from equimolar counterdiffusion.

4. For equimolar diffusion, D=2e-5, Δp=10 kPa, T=300 K, L=0.01 m. Estimate NA.

5. kg'=0.10 mol/(m²·s·kPa), bulk-interface Δp=2 kPa. Find flux.

6. 1/kG=2 and H/kL=8 in common reciprocal units. What fraction of total resistance is liquid-side?

7. D=0.05 m, km=0.02 m/s, DAB=1e-5 m²/s. Find Sherwood number.

8. If concentration profile is flat, what is Fickian diffusive flux?

9. If both individual phase resistances halve, what happens qualitatively to overall K?

10. Which dimensionless group compares momentum to mass diffusivity?


---

## Practice Problem Solutions

1. J=-D dC/dx=0.002 mol/(m²·s).

2. sqrt(1e-6)=0.001 m=1 mm.

3. There is net molar bulk motion when B has zero molar flux.

4. NA=DΔp/(RTL)=2e-5×10000/(8.314×300×0.01)=0.00802 mol/(m²·s).

5. NA=0.20 mol/(m²·s).

6. 8/(2+8)=80%.

7. Sh=kmD/DAB=100.

8. Zero.

9. Overall resistance halves, so K approximately doubles.

10. Schmidt number.


---

## Quick Reference

**Source anchor:** Chemical Engineering, printed pp. 247–255; FE Chemical specification Area 10A–B.

- **Fick first law:** Fick's First Law
- **unsteady molecular diffusion:** Fick's Second Law and Unsteady Diffusion
- **stagnant-gas diffusion:** Diffusion of A Through Stagnant B
- **equimolar counterdiffusion:** Equimolar Counter-Diffusion
- **two-film mass transfer:** Two-Film Theory
- **overall mass-transfer coefficient:** Overall Mass-Transfer Coefficients
- **Sherwood mass-transfer correlation:** Sherwood Correlations and Transport Analogies
---

## What's Next

**03-06 — Distillation and Equilibrium-Stage Methods**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor