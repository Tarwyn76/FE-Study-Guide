---
chapter: "03-10"
title: "Reaction Kinetics, Rate Laws, and Arrhenius Behavior"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-010-01, CHE-3-010-02, CHE-3-010-03, CHE-3-010-04, CHE-3-010-05, CHE-3-010-06, CHE-3-010-07]
routes: [chemical]
status: drafted
---

# Chapter 03-10: Reaction Kinetics, Rate Laws, and Arrhenius Behavior

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 03-03 Reactive Material Balances · 01-25 Differential Equations

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines reaction rate, power-law order, Arrhenius temperature dependence, integrated zero/first/second-order batch relations, reversible and shifting-order forms, Michaelis–Menten behavior, and multiple-reaction yield/selectivity.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **10.1** Explain and apply **Reaction-Rate Definition**.
* **10.2** Explain and apply **Power-Law Rate Laws and Reaction Order**.
* **10.3** Explain and apply **Integrated Zero-, First-, and Second-Order Batch Kinetics**.
* **10.4** Explain and apply **Arrhenius Temperature Dependence**.
* **10.5** Explain and apply **Reversible Reactions and Approach to Equilibrium**.
* **10.6** Explain and apply **Michaelis–Menten and Saturating Kinetics**.
* **10.7** Explain and apply **Parallel and Series Reaction Networks**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 10.1 Reaction-Rate Definition

The Handbook defines species reaction rate as moles formed per unit time per unit reactor volume. For a disappearing reactant A, \(-r_A\) is positive.

Rate can be written in concentration form for a constant-volume batch reactor or in molar-flow form for a flow reactor.

\[-r_A=-\frac1V\frac{dN_A}{dt}\]

![FIG-03-10-001: Batch reactor volume with decreasing reactant moles and positive disappearance rate.](../figures/FIG-03-10-001-reaction-rate-definition.png)

### Worked Example 1

**Problem.** NA decreases 10 mol in a 2 L reactor over 5 min. Find average -rA.

**Solution.** 10/(2×5)=1 mol/(L·min).

---

<!-- VERIFY id="WE-03-10-001-rate" expr="10/(2*5)" expected="1" units="mol/(L*min)" atol="1e-9" rtol="1e-9" -->

## 10.2 Power-Law Rate Laws and Reaction Order

A common empirical form is \(-r_A=kC_A^xC_B^y\). Order with respect to each reactant is the exponent, and overall order is their sum.

Reaction order is obtained from kinetics; it need not equal stoichiometric coefficients unless an elementary mechanism justifies that relation.

\[-r_A=kC_A^xC_B^y,\qquad n=x+y\]

![FIG-03-10-002: Rate-law diagram showing concentration exponents and a log-rate versus log-concentration slope interpretation.](../figures/FIG-03-10-002-power-law-rate-laws-and-reaction-order.png)

### Worked Example 2

**Problem.** Rate law is k CA^2 CB. What is overall order?

**Solution.** 3.

---

<!-- VERIFY id="WE-03-10-002-order" expr="2+1" expected="3" units="dimensionless" atol="1e-9" rtol="1e-9" -->

**Why this works.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. In this example, the stated setup (“Problem. Rate law is k CA^2 CB. What is overall order? Solution. 3”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## 10.3 Integrated Zero-, First-, and Second-Order Batch Kinetics

For constant-volume batch reactors, the Handbook provides integrated concentration or conversion relations for zero-, first-, and second-order irreversible reactions.

Recognize the characteristic linear plots: \(C_A\) vs \(t\) for zero order, \(\ln C_A\) vs \(t\) for first order, and \(1/C_A\) vs \(t\) for second order.

\[\begin{aligned}0^\text{th}:&\ C_A=C_{A0}-kt\\1^\text{st}:&\ \ln(C_A/C_{A0})=-kt\\2^\text{nd}:&\ 1/C_A-1/C_{A0}=kt\end{aligned}\]

![FIG-03-10-003: Three panels showing linearized zero-, first-, and second-order batch kinetic plots.](../figures/FIG-03-10-003-integrated-zero-first-and-second-order-batch-kinetics.png)

### Worked Example 3

**Problem.** First-order k=0.2 min^-1. Find fraction remaining after 5 min.

**Solution.** CA/CA0=e^-1=0.3679.

---

<!-- VERIFY id="WE-03-10-003-fraction" expr="exp(-0.2*5)" expected="0.3679" units="dimensionless" atol="0.00005" rtol="1e-9" -->

## 10.4 Arrhenius Temperature Dependence

The Arrhenius equation relates rate constant to absolute temperature through activation energy. A plot of \(\ln k\) versus \(1/T\) has slope \(-E_a/R\).

Even a modest temperature increase can strongly increase rate when activation energy is large.

\[k=Ae^{-E_a/(RT)},\qquad \ln\frac{k_2}{k_1}=-\frac{E_a}{R}\left(\frac1{T_2}-\frac1{T_1}\right)\]

![FIG-03-10-004: Arrhenius plot of ln k versus inverse absolute temperature with slope minus Ea/R.](../figures/FIG-03-10-004-arrhenius-temperature-dependence.png)

### Worked Example 4

**Problem.** k1=0.10 s^-1 at T1 and Ea=50 kJ/mol. Qualitatively what happens to k if T increases?

**Solution.** k increases exponentially.

---

**Why this works.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. In this example, the stated setup (“Problem. k1=0.10 s^-1 at T1 and Ea=50 kJ/mol. Qualitatively what happens to k if T increases? Solution. k increases exponentially”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## 10.5 Reversible Reactions and Approach to Equilibrium

For reversible reactions, net rate is forward rate minus reverse rate. At equilibrium the two rates are equal and net rate is zero.

The Handbook gives a first-order reversible form and identifies equilibrium conversion.

\[r_{\rm net}=r_f-r_r,\qquad r_{\rm net}=0\ \text{at equilibrium}\]

![FIG-03-10-005: Forward and reverse rate curves versus conversion intersecting at equilibrium conversion.](../figures/FIG-03-10-005-reversible-reactions-and-approach-to-equilibrium.png)

### Worked Example 5

**Problem.** At equilibrium, what is net rate of a reversible reaction?

**Solution.** Zero.

---

**Why this works.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. In this example, the stated setup (“Problem. At equilibrium, what is net rate of a reversible reaction? Solution. Zero”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## 10.6 Michaelis–Menten and Saturating Kinetics

The Handbook gives the Michaelis–Menten form for enzyme-catalyzed reactions. At low substrate concentration, rate is approximately first order in substrate; at high concentration, rate approaches \(V_{\max}\).

This saturation behavior is also representative of some surface-catalyzed kinetic forms.

\[r=\frac{V_{\max}C_S}{K_m+C_S}\]

![FIG-03-10-006: Michaelis-Menten rate versus substrate concentration showing low-concentration slope, Km, and Vmax plateau.](../figures/FIG-03-10-006-michaelis-menten-and-saturating-kinetics.png)

### Worked Example 6

**Problem.** For Michaelis-Menten, C=Km. What fraction of Vmax is rate?

**Solution.** 1/2.

---

<!-- VERIFY id="WE-03-10-006-vmaxfrac" expr="1/(1+1)" expected="0.5" units="dimensionless" atol="1e-9" rtol="1e-9" -->

## 10.7 Parallel and Series Reaction Networks

Desired-product yield depends on competition among reaction pathways. The Handbook gives definitions and formulas for parallel reactions and sequential first-order reactions.

For parallel power-law reactions, operating concentration and temperature can affect selectivity if the pathways have different orders or activation energies.

\[S_{D/U}=\frac{\text{moles desired product formed}}{\text{moles undesired product formed}}\]

![FIG-03-10-007: Parallel A-to-D/A-to-U and series A-to-D-to-U reaction networks with selectivity/yield labels.](../figures/FIG-03-10-007-parallel-and-series-reaction-networks.png)

### Worked Example 7

**Problem.** D/U selectivity is 5. If 10 mol U forms, how much D forms?

**Solution.** 50 mol.

---

<!-- VERIFY id="WE-03-10-007-D" expr="5*10" expected="50" units="mol" atol="1e-9" rtol="1e-9" -->

**Why this works.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. In this example, the stated setup (“Problem. D/U selectivity is 5. If 10 mol U forms, how much D forms? Solution. 50 mol”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## Integrated Worked Examples

### Worked Example 8

**Problem.** Zero-order reaction k=2 mol/(L·min), CA0=10 mol/L. Time to depletion?

**Solution.** 5 min.

<!-- VERIFY id="WE-03-10-008-time" expr="10/2" expected="5" units="min" atol="1e-9" rtol="1e-9" -->

**Why this works.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. In this example, the stated setup (“Problem. Zero-order reaction k=2 mol/(L·min), CA0=10 mol/L. Time to depletion? Solution. 5 min”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
### Worked Example 9

**Problem.** Second-order k=0.1 L/(mol·min), CA0=2 mol/L. Find CA after 5 min.

**Solution.** 1/CA=1/2+0.1×5=1 → CA=1 mol/L.

---

<!-- VERIFY id="WE-03-10-009-CA" expr="1/(1/2+0.1*5)" expected="1" units="mol/L" atol="1e-9" rtol="1e-9" -->

## As the Handbook States It

Primary source basis: **Chemical Engineering, printed pp. 243–247; FE Chemical specification Area 12A–D and 12F**.

**Source boundary:** The Handbook directly defines reaction rate, power-law order, Arrhenius temperature dependence, integrated zero/first/second-order batch relations, reversible and shifting-order forms, Michaelis–Menten behavior, and multiple-reaction yield/selectivity.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using reaction rate without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using reaction order without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using integrated reaction kinetics without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using Arrhenius kinetics without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using reversible reaction kinetics without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using Michaelis-Menten kinetics without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using reaction-network selectivity without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| reaction rate | Concept developed in §10.1; apply with the section's stated basis and assumptions. |
| reaction order | Concept developed in §10.2; apply with the section's stated basis and assumptions. |
| integrated reaction kinetics | Concept developed in §10.3; apply with the section's stated basis and assumptions. |
| Arrhenius kinetics | Concept developed in §10.4; apply with the section's stated basis and assumptions. |
| reversible reaction kinetics | Concept developed in §10.5; apply with the section's stated basis and assumptions. |
| Michaelis-Menten kinetics | Concept developed in §10.6; apply with the section's stated basis and assumptions. |
| reaction-network selectivity | Concept developed in §10.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **reaction rate** and state the governing relation or balance.

2. Define **reaction order** and state the governing relation or balance.

3. Define **integrated reaction kinetics** and state the governing relation or balance.

4. Define **Arrhenius kinetics** and state the governing relation or balance.

5. Define **reversible reaction kinetics** and state the governing relation or balance.

6. Define **Michaelis-Menten kinetics** and state the governing relation or balance.

7. Define **reaction-network selectivity** and state the governing relation or balance.

8. What is the most likely error if **reaction rate** is applied before the process basis and boundary are defined?

9. What is the most likely error if **reaction order** is applied before the process basis and boundary are defined?

10. What is the most likely error if **integrated reaction kinetics** is applied before the process basis and boundary are defined?

11. What is the most likely error if **Arrhenius kinetics** is applied before the process basis and boundary are defined?

12. What is the most likely error if **reversible reaction kinetics** is applied before the process basis and boundary are defined?

13. What is the most likely error if **Michaelis-Menten kinetics** is applied before the process basis and boundary are defined?

14. What is the most likely error if **reaction-network selectivity** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **reaction rate**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **reaction order**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **integrated reaction kinetics**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **Arrhenius kinetics**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **reversible reaction kinetics**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **Michaelis-Menten kinetics**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **reaction-network selectivity**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **reaction rate**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **reaction order**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **reaction rate** is developed in §10.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **reaction order** is developed in §10.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **integrated reaction kinetics** is developed in §10.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **Arrhenius kinetics** is developed in §10.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **reversible reaction kinetics** is developed in §10.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **Michaelis-Menten kinetics** is developed in §10.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **reaction-network selectivity** is developed in §10.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.
8. Applying **reaction rate** before the process basis and system boundary are fixed can infer the wrong reaction order or evaluate a rate constant at a temperature inconsistent with the stated Arrhenius model. In this chapter, kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant. Define the basis, boundary, known streams or states, and independent specifications first; then apply the reaction rate relation to that defined system.

9. Applying **reaction order** before the process basis and system boundary are fixed can infer the wrong reaction order or evaluate a rate constant at a temperature inconsistent with the stated Arrhenius model. In this chapter, kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant. Define the basis, boundary, known streams or states, and independent specifications first; then apply the reaction order relation to that defined system.

10. Applying **integrated reaction kinetics** before the process basis and system boundary are fixed can infer the wrong reaction order or evaluate a rate constant at a temperature inconsistent with the stated Arrhenius model. In this chapter, kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant. Define the basis, boundary, known streams or states, and independent specifications first; then apply the integrated reaction kinetics relation to that defined system.

11. Applying **Arrhenius kinetics** before the process basis and system boundary are fixed can infer the wrong reaction order or evaluate a rate constant at a temperature inconsistent with the stated Arrhenius model. In this chapter, kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant. Define the basis, boundary, known streams or states, and independent specifications first; then apply the Arrhenius kinetics relation to that defined system.

12. Applying **reversible reaction kinetics** before the process basis and system boundary are fixed can infer the wrong reaction order or evaluate a rate constant at a temperature inconsistent with the stated Arrhenius model. In this chapter, kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant. Define the basis, boundary, known streams or states, and independent specifications first; then apply the reversible reaction kinetics relation to that defined system.

13. Applying **Michaelis-Menten kinetics** before the process basis and system boundary are fixed can infer the wrong reaction order or evaluate a rate constant at a temperature inconsistent with the stated Arrhenius model. In this chapter, kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant. Define the basis, boundary, known streams or states, and independent specifications first; then apply the Michaelis-Menten kinetics relation to that defined system.

14. Applying **reaction-network selectivity** before the process basis and system boundary are fixed can infer the wrong reaction order or evaluate a rate constant at a temperature inconsistent with the stated Arrhenius model. In this chapter, kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant. Define the basis, boundary, known streams or states, and independent specifications first; then apply the reaction-network selectivity relation to that defined system.

15. Close the material balance first because it establishes the flow rates and compositions that the energy balance must use. For this chapter, kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant; without those material quantities, enthalpy, heat duty, reaction energy, or phase-change terms can be attached to the wrong amount of material.

16. A degrees-of-freedom check compares the number of unknowns with the number of independent balances, constitutive relations, equilibrium or rate equations, and specifications. For 03-10, this prevents algebra from starting before the kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant are sufficiently defined and exposes redundant or missing equations.

17. Use a relation supplied in the FE problem whenever it defines the model or data for that question. That stated relation controls the calculation even if another correlation is familiar; in 03-10, substituting an unstated model can change the assumptions behind the kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant.

18. Separate Handbook-supported material from specification-required or externally supported material so the learner knows what may be looked up and what must be understood independently. In 03-10, the distinction matters because the kinetic calculations depend on the rate-law form, reaction order, concentration or pressure basis, and temperature-dependent rate constant can include methods or assumptions that are required by the exam specification but are not fully tabulated in the Handbook.


19. **A.** The relation or workflow for **reaction rate** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **reaction order** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **integrated reaction kinetics** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **Arrhenius kinetics** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **reversible reaction kinetics** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **Michaelis-Menten kinetics** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **reaction-network selectivity** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **reaction rate** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

27. **A.** The relation or workflow for **reaction order** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. NA decreases 10 mol in a 2 L reactor over 5 min. Find average -rA.

2. Rate law is k CA^2 CB. What is overall order?

3. First-order k=0.2 min^-1. Find fraction remaining after 5 min.

4. k1=0.10 s^-1 at T1 and Ea=50 kJ/mol. Qualitatively what happens to k if T increases?

5. At equilibrium, what is net rate of a reversible reaction?

6. For Michaelis-Menten, C=Km. What fraction of Vmax is rate?

7. D/U selectivity is 5. If 10 mol U forms, how much D forms?

8. Zero-order reaction k=2 mol/(L·min), CA0=10 mol/L. Time to depletion?

9. Second-order k=0.1 L/(mol·min), CA0=2 mol/L. Find CA after 5 min.

10. What kinetic quantity is obtained from slope of ln k versus 1/T?


---

## Practice Problem Solutions

1. 10/(2×5)=1 mol/(L·min).

2. 3.

   **Explanation.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. The question is framed around “Rate law is k CA^2 CB. What is overall order?.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

3. CA/CA0=e^-1=0.3679.

   **Explanation.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. The question is framed around “First-order k=0.2 min^-1. Find fraction remaining after 5 min.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

4. k increases exponentially.

   **Explanation.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. The question is framed around “k1=0.10 s^-1 at T1 and Ea=50 kJ/mol. Qualitatively what happens to k if T increases?.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

5. Zero.

   **Explanation.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. The question is framed around “At equilibrium, what is net rate of a reversible reaction?.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

6. 1/2.

   **Explanation.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. The question is framed around “For Michaelis-Menten, C=Km. What fraction of Vmax is rate?.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

7. 50 mol.

   **Explanation.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. The question is framed around “D/U selectivity is 5. If 10 mol U forms, how much D forms?.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

8. 5 min.

   **Explanation.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. The question is framed around “Zero-order reaction k=2 mol/(L·min), CA0=10 mol/L. Time to depletion?.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

9. 1/CA=1/2+0.1×5=1 → CA=1 mol/L.

10. -Ea/R.


---

   **Explanation.** Apply the stated rate law with the correct reaction order and concentration or partial-pressure basis, then account for temperature through the kinetic parameter. The question is framed around “What kinetic quantity is obtained from slope of ln k versus 1/T? ---.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

## Quick Reference

**Source anchor:** Chemical Engineering, printed pp. 243–247; FE Chemical specification Area 12A–D and 12F.

- **reaction rate:** Reaction-Rate Definition
- **reaction order:** Power-Law Rate Laws and Reaction Order
- **integrated reaction kinetics:** Integrated Zero-, First-, and Second-Order Batch Kinetics
- **Arrhenius kinetics:** Arrhenius Temperature Dependence
- **reversible reaction kinetics:** Reversible Reactions and Approach to Equilibrium
- **Michaelis-Menten kinetics:** Michaelis–Menten and Saturating Kinetics
- **reaction-network selectivity:** Parallel and Series Reaction Networks
---

## What's Next

**03-11 — Reactor Design — Batch, CSTR, PFR, Multiple Reactions, and Catalysis**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor