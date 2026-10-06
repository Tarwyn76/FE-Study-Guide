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

By the end of this chapter, you will be able to:

* **10.1** Explain and apply **Reaction-Rate Definition**.
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

**Solution.** For **Reaction-Rate Definition**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 10, 2, 5, 10/(2×5)=1 mol/(L·min). This is the section-specific result for NA decreases mol reactor over min average. The stated units/basis (min, s) are retained.

---

## 10.2 Power-Law Rate Laws and Reaction Order

A common empirical form is \(-r_A=kC_A^xC_B^y\). Order with respect to each reactant is the exponent, and overall order is their sum.

Reaction order is obtained from kinetics; it need not equal stoichiometric coefficients unless an elementary mechanism justifies that relation.

\[-r_A=kC_A^xC_B^y,\qquad n=x+y\]

![FIG-03-10-002: Rate-law diagram showing concentration exponents and a log-rate versus log-concentration slope interpretation.](../figures/FIG-03-10-002-power-law-rate-laws-and-reaction-order.png)

### Worked Example 2

**Problem.** Rate law is k CA^2 CB. What is overall order?

**Solution.** For **Power-Law Rate Laws and Reaction Order**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 2, 3. This is the section-specific result for Rate law CA CB overall order. The stated units/basis (s, h) are retained.

---

## 10.3 Integrated Zero-, First-, and Second-Order Batch Kinetics

For constant-volume batch reactors, the Handbook provides integrated concentration or conversion relations for zero-, first-, and second-order irreversible reactions.

Recognize the characteristic linear plots: \(C_A\) vs \(t\) for zero order, \(\ln C_A\) vs \(t\) for first order, and \(1/C_A\) vs \(t\) for second order.

\[\begin{aligned}0^\text{th}:&\ C_A=C_{A0}-kt\\1^\text{st}:&\ \ln(C_A/C_{A0})=-kt\\2^\text{nd}:&\ 1/C_A-1/C_{A0}=kt\end{aligned}\]

![FIG-03-10-003: Three panels showing linearized zero-, first-, and second-order batch kinetic plots.](../figures/FIG-03-10-003-integrated-zero-first-and-second-order-batch-kinetics.png)

### Worked Example 3

**Problem.** First-order k=0.2 min^-1. Find fraction remaining after 5 min.

**Solution.** For **Integrated Zero-, First-, and Second-Order Batch Kinetics**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) k=0.2, CA/CA0=e^-1=0.3679. This is the section-specific result for First-order min fraction remaining after min. The stated units/basis (min^-1, min) are retained.

---

## 10.4 Arrhenius Temperature Dependence

The Arrhenius equation relates rate constant to absolute temperature through activation energy. A plot of \(\ln k\) versus \(1/T\) has slope \(-E_a/R\).

Even a modest temperature increase can strongly increase rate when activation energy is large.

\[k=Ae^{-E_a/(RT)},\qquad \ln\frac{k_2}{k_1}=-\frac{E_a}{R}\left(\frac1{T_2}-\frac1{T_1}\right)\]

![FIG-03-10-004: Arrhenius plot of ln k versus inverse absolute temperature with slope minus Ea/R.](../figures/FIG-03-10-004-arrhenius-temperature-dependence.png)

### Worked Example 4

**Problem.** k1=0.10 s^-1 at T1 and Ea=50 kJ/mol. Qualitatively what happens to k if T increases?

**Solution.** For **Arrhenius Temperature Dependence**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) k1=0.10, Ea=50, k increases exponentially. This is the section-specific result for Ea kJ mol Qualitatively happens increases. The stated units/basis (kJ/mol, s^-1) are retained.

---

## 10.5 Reversible Reactions and Approach to Equilibrium

For reversible reactions, net rate is forward rate minus reverse rate. At equilibrium the two rates are equal and net rate is zero.

The Handbook gives a first-order reversible form and identifies equilibrium conversion.

\[r_{\rm net}=r_f-r_r,\qquad r_{\rm net}=0\ \text{at equilibrium}\]

![FIG-03-10-005: Forward and reverse rate curves versus conversion intersecting at equilibrium conversion.](../figures/FIG-03-10-005-reversible-reactions-and-approach-to-equilibrium.png)

### Worked Example 5

**Problem.** At equilibrium, what is net rate of a reversible reaction?

**Solution.** For **Reversible Reactions and Approach to Equilibrium**, Zero. This follows because for reversible reactions, net rate is forward rate minus reverse rate.. That physical distinction controls the result for equilibrium net rate reversible reaction.

---

## 10.6 Michaelis–Menten and Saturating Kinetics

The Handbook gives the Michaelis–Menten form for enzyme-catalyzed reactions. At low substrate concentration, rate is approximately first order in substrate; at high concentration, rate approaches \(V_{\max}\).

This saturation behavior is also representative of some surface-catalyzed kinetic forms.

\[r=\frac{V_{\max}C_S}{K_m+C_S}\]

![FIG-03-10-006: Michaelis-Menten rate versus substrate concentration showing low-concentration slope, Km, and Vmax plateau.](../figures/FIG-03-10-006-michaelis-menten-and-saturating-kinetics.png)

### Worked Example 6

**Problem.** For Michaelis-Menten, C=Km. What fraction of Vmax is rate?

**Solution.** For **Michaelis–Menten and Saturating Kinetics**, 1/2. This follows because the Handbook gives the Michaelis–Menten form for enzyme-catalyzed reactions.. That physical distinction controls the result for Michaelis-Menten Km fraction Vmax rate.

---

## 10.7 Parallel and Series Reaction Networks

Desired-product yield depends on competition among reaction pathways. The Handbook gives definitions and formulas for parallel reactions and sequential first-order reactions.

For parallel power-law reactions, operating concentration and temperature can affect selectivity if the pathways have different orders or activation energies.

\[S_{D/U}=\frac{\text{moles desired product formed}}{\text{moles undesired product formed}}\]

![FIG-03-10-007: Parallel A-to-D/A-to-U and series A-to-D-to-U reaction networks with selectivity/yield labels.](../figures/FIG-03-10-007-parallel-and-series-reaction-networks.png)

### Worked Example 7

**Problem.** D/U selectivity is 5. If 10 mol U forms, how much D forms?

**Solution.** For **Parallel and Series Reaction Networks**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 5, 10, 50 mol. This is the section-specific result for selectivity mol forms much forms. The stated units/basis (s, h) are retained.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Zero-order reaction k=2 mol/(L·min), CA0=10 mol/L. Time to depletion?

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) k=2, CA0=10, 5 min. This is the section-specific result for Zero-order reaction mol min CA mol Time. The stated units/basis (mol/L, min) are retained.

### Worked Example 9

**Problem.** Second-order k=0.1 L/(mol·min), CA0=2 mol/L. Find CA after 5 min.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) k=0.1, CA0=2, 1/CA=1/2+0.1×5=1 → CA=1 mol/L. This is the section-specific result for Second-order mol min CA mol CA after. The stated units/basis (mol/L, min) are retained.

---

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

1. **Reaction-Rate Definition.** The Handbook defines species reaction rate as moles formed per unit time per unit reactor volume. In Reaction Kinetics, Rate Laws, and Arrhenius Behavior, this is the definition or balance being tested by Question 1.

2. **Power-Law Rate Laws and Reaction Order.** Order with respect to each reactant is the exponent, and overall order is their sum. In Reaction Kinetics, Rate Laws, and Arrhenius Behavior, this is the definition or balance being tested by Question 2.

3. **Integrated Zero-, First-, and Second-Order Batch Kinetics.** For constant-volume batch reactors, the Handbook provides integrated concentration or conversion relations for zero-, first-, and second-order irreversible reactions. In Reaction Kinetics, Rate Laws, and Arrhenius Behavior, this is the definition or balance being tested by Question 3.

4. **Arrhenius Temperature Dependence.** The Arrhenius equation relates rate constant to absolute temperature through activation energy. In Reaction Kinetics, Rate Laws, and Arrhenius Behavior, this is the definition or balance being tested by Question 4.

5. **Reversible Reactions and Approach to Equilibrium.** For reversible reactions, net rate is forward rate minus reverse rate. In Reaction Kinetics, Rate Laws, and Arrhenius Behavior, this is the definition or balance being tested by Question 5.

6. **Michaelis–Menten and Saturating Kinetics.** The Handbook gives the Michaelis–Menten form for enzyme-catalyzed reactions. In Reaction Kinetics, Rate Laws, and Arrhenius Behavior, this is the definition or balance being tested by Question 6.

7. **Parallel and Series Reaction Networks.** Desired-product yield depends on competition among reaction pathways. In Reaction Kinetics, Rate Laws, and Arrhenius Behavior, this is the definition or balance being tested by Question 7.

8. For **Reaction-Rate Definition**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook defines species reaction rate as moles formed per unit time per unit reactor volume. This is the specific failure mode emphasized in Reaction Kinetics, Rate Laws, and Arrhenius Behavior.

9. For **Power-Law Rate Laws and Reaction Order**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Order with respect to each reactant is the exponent, and overall order is their sum. This is the specific failure mode emphasized in Reaction Kinetics, Rate Laws, and Arrhenius Behavior.

10. For **Integrated Zero-, First-, and Second-Order Batch Kinetics**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For constant-volume batch reactors, the Handbook provides integrated concentration or conversion relations for zero-, first-, and second-order irreversible reactions. This is the specific failure mode emphasized in Reaction Kinetics, Rate Laws, and Arrhenius Behavior.

11. For **Arrhenius Temperature Dependence**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Arrhenius equation relates rate constant to absolute temperature through activation energy. This is the specific failure mode emphasized in Reaction Kinetics, Rate Laws, and Arrhenius Behavior.

12. For **Reversible Reactions and Approach to Equilibrium**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For reversible reactions, net rate is forward rate minus reverse rate. This is the specific failure mode emphasized in Reaction Kinetics, Rate Laws, and Arrhenius Behavior.

13. For **Michaelis–Menten and Saturating Kinetics**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook gives the Michaelis–Menten form for enzyme-catalyzed reactions. This is the specific failure mode emphasized in Reaction Kinetics, Rate Laws, and Arrhenius Behavior.

14. For **Parallel and Series Reaction Networks**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Desired-product yield depends on competition among reaction pathways. This is the specific failure mode emphasized in Reaction Kinetics, Rate Laws, and Arrhenius Behavior.

15. In **Reaction Kinetics, Rate Laws, and Arrhenius Behavior**, close the material balance first because stream amounts and compositions feed the later energy calculation. Otherwise enthalpy and duty terms may be evaluated for unresolved streams.

16. For **Reaction Kinetics, Rate Laws, and Arrhenius Behavior**, a degrees-of-freedom check counts unknowns against independent equations before solving. Zero indicates a closed problem; a positive count signals missing independent information.

17. In **Reaction Kinetics, Rate Laws, and Arrhenius Behavior**, a relation supplied by the FE problem defines the intended model for that question. A remembered correlation can carry different assumptions, coefficients, validity limits, or reference states.

18. For **Reaction Kinetics, Rate Laws, and Arrhenius Behavior**, separating Handbook-supported material from specification-required learned material distinguishes lookup knowledge from material the guide develops. That boundary prevents guide-developed content from being presented as Handbook text.

19. **A.** For **Reaction-Rate Definition**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook defines species reaction rate as moles formed per unit time per unit reactor volume. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

20. **A.** For **Power-Law Rate Laws and Reaction Order**, the relation is meaningful only with the correct basis and physical assumptions. Order with respect to each reactant is the exponent, and overall order is their sum. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

21. **A.** For **Integrated Zero-, First-, and Second-Order Batch Kinetics**, the relation is meaningful only with the correct basis and physical assumptions. For constant-volume batch reactors, the Handbook provides integrated concentration or conversion relations for zero-, first-, and second-order irreversible reactions. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

22. **A.** For **Arrhenius Temperature Dependence**, the relation is meaningful only with the correct basis and physical assumptions. The Arrhenius equation relates rate constant to absolute temperature through activation energy. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

23. **A.** For **Reversible Reactions and Approach to Equilibrium**, the relation is meaningful only with the correct basis and physical assumptions. For reversible reactions, net rate is forward rate minus reverse rate. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

24. **A.** For **Michaelis–Menten and Saturating Kinetics**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook gives the Michaelis–Menten form for enzyme-catalyzed reactions. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

25. **A.** For **Parallel and Series Reaction Networks**, the relation is meaningful only with the correct basis and physical assumptions. Desired-product yield depends on competition among reaction pathways. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

26. **A.** This later check revisits **Reaction-Rate Definition** from a different review position. The Handbook defines species reaction rate as moles formed per unit time per unit reactor volume. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.

27. **A.** This later check revisits **Power-Law Rate Laws and Reaction Order** from a different review position. Order with respect to each reactant is the exponent, and overall order is their sum. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.


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

1. For the practice case involving **NA decreases mol reactor over min average**, Using 10, 2, 5, 10/(2×5)=1 mol/(L·min). This completes Practice Problem 1 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior. The original min, s basis is preserved.

2. For the practice case involving **Rate law CA CB overall order**, Using 2, 3. This completes Practice Problem 2 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior. The original s, h basis is preserved.

3. For the practice case involving **First-order min fraction remaining after min**, Using k=0.2, CA/CA0=e^-1=0.3679. This completes Practice Problem 3 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior. The original min^-1, min basis is preserved.

4. For the practice case involving **Ea kJ mol Qualitatively happens increases**, Using k1=0.10, Ea=50, k increases exponentially. This completes Practice Problem 4 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior. The original kJ/mol, s^-1 basis is preserved.

5. For the practice case involving **equilibrium net rate reversible reaction**, Zero. This is the chapter-specific distinction required by Practice Problem 5 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior.

6. For the practice case involving **Michaelis-Menten Km fraction Vmax rate**, 1/2. This is the chapter-specific distinction required by Practice Problem 6 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior.

7. For the practice case involving **selectivity mol forms much forms**, Using 5, 10, 50 mol. This completes Practice Problem 7 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior. The original s, h basis is preserved.

8. For the practice case involving **Zero-order reaction mol min CA mol Time**, Using k=2, CA0=10, 5 min. This completes Practice Problem 8 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior. The original mol/L, min basis is preserved.

9. For the practice case involving **Second-order mol min CA mol CA after**, Using k=0.1, CA0=2, 1/CA=1/2+0.1×5=1 → CA=1 mol/L. This completes Practice Problem 9 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior. The original mol/L, min basis is preserved.

10. For the practice case involving **kinetic quantity obtained from slope ln versus**, Using 1, -Ea/R. This completes Practice Problem 10 in Reaction Kinetics, Rate Laws, and Arrhenius Behavior. The original s, h basis is preserved.


---

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
