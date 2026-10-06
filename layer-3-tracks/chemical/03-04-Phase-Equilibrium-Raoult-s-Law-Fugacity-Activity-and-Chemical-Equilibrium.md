---
chapter: "03-04"
title: "Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-004-01, CHE-3-004-02, CHE-3-004-03, CHE-3-004-04, CHE-3-004-05, CHE-3-004-06, CHE-3-004-07]
routes: [chemical]
status: drafted
---

# Chapter 03-04: Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 02-48 Pure Substances and Property Tables · 02-49 Ideal-Gas Mixtures · 02-14 Chemical Equilibrium

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly provides Henry's law, Raoult's law, rigorous fugacity equality, activity-coefficient and fugacity-coefficient forms, phase relations, Gibbs phase rule, reaction extent, and chemical-equilibrium expressions.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **4.1** Explain and apply **Gibbs Phase Rule and Phase Equilibrium**.
* **4.2** Explain and apply **Henry's Law for Dilute Solutes**.
* **4.3** Explain and apply **Raoult's Law and Ideal VLE**.
* **4.4** Explain and apply **K-Values, Bubble Points, and Dew Points**.
* **4.5** Explain and apply **Fugacity Equality for Rigorous Phase Equilibrium**.
* **4.6** Explain and apply **Activity Coefficients and Liquid-Phase Nonideality**.
* **4.7** Explain and apply **Chemical Reaction Equilibrium**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 4.1 Gibbs Phase Rule and Phase Equilibrium

For a nonreacting equilibrium system, Gibbs phase rule relates number of components, phases, and independent intensive degrees of freedom.

Phase equilibrium requires equality of the appropriate chemical potential/fugacity criterion for each component across coexisting phases.

\[P+F=C+2\]

![FIG-03-04-001: Component-phase-degrees-of-freedom map with one- and two-phase examples.](../figures/FIG-03-04-001-gibbs-phase-rule-and-phase-equilibrium.png)

### Worked Example 1

**Problem.** For a nonreacting binary two-phase system, use phase rule to find degrees of freedom.

**Solution.** F=C+2-P=2+2-2=2.

---

## 4.2 Henry's Law for Dilute Solutes

The Handbook gives Henry's law for low-concentration solutes in gas-liquid equilibrium. Partial pressure is proportional to liquid-phase mole fraction through the stated Henry constant convention.

Henry constants appear in multiple unit conventions, so units must be checked before use.

\[p_i=y_iP=H_i x_i\]

![FIG-03-04-002: Dilute gas-solute equilibrium with partial pressure versus liquid mole fraction and Henry-law slope.](../figures/FIG-03-04-002-henry-s-law-for-dilute-solutes.png)

### Worked Example 2

**Problem.** Henry constant is 500 kPa and x=0.002. Find equilibrium gas partial pressure.

**Solution.** p=Hx=1.0 kPa.

---

## 4.3 Raoult's Law and Ideal VLE

For near-ideal liquid mixtures at sufficiently low pressure, Raoult's law relates component partial pressure to liquid mole fraction and pure-component saturation pressure.

Combining with Dalton's law gives \(y_iP=x_iP_i^{sat}\).

\[p_i=x_iP_i^{sat},\qquad y_iP=x_iP_i^{sat}\]

![FIG-03-04-003: Binary ideal-solution bubble/dew representation with liquid composition x and vapor composition y.](../figures/FIG-03-04-003-raoult-s-law-and-ideal-vle.png)

### Worked Example 3

**Problem.** At 80°C, Psat,A=80 kPa and xA=0.4. Raoult partial pressure?

**Solution.** pA=32 kPa.

---

## 4.4 K-Values, Bubble Points, and Dew Points

Define \(K_i=y_i/x_i\). Under ideal Raoult behavior, \(K_i=P_i^{sat}/P\). Bubble-point calculations begin with a liquid composition; dew-point calculations begin with a vapor composition.

At a bubble point \(\sum_i y_i=1\); at a dew point \(\sum_i x_i=1\).

\[K_i=\frac{y_i}{x_i},\qquad \sum_iK_ix_i=1\ \text{(bubble)},\qquad \sum_i\frac{y_i}{K_i}=1\ \text{(dew)}\]

![FIG-03-04-004: Binary mixture showing known liquid composition for bubble point and known vapor composition for dew point.](../figures/FIG-03-04-004-k-values-bubble-points-and-dew-points.png)

### Worked Example 4

**Problem.** Binary liquid has xA=0.4, KA=1.5, KB=0.667. Check bubble criterion ΣKx if xB=0.6.

**Solution.** 1.5(0.4)+0.667(0.6)=1.0002≈1; near bubble condition.

---

## 4.5 Fugacity Equality for Rigorous Phase Equilibrium

The Handbook's rigorous VLE criterion is equality of component fugacity between vapor and liquid phases. Vapor fugacity commonly uses a fugacity coefficient; liquid fugacity commonly uses activity coefficient and a pure-liquid reference fugacity.

At low pressure and near-ideal behavior, these corrections approach unity and the rigorous form reduces toward Raoult's law.

\[\hat f_i^V=\hat f_i^L,\qquad \hat f_i^V=y_i\phi_iP,\qquad \hat f_i^L=x_i\gamma_i f_i^L\]

![FIG-03-04-005: Vapor and liquid fugacity expressions meeting at equilibrium, with phi and gamma corrections.](../figures/FIG-03-04-005-fugacity-equality-for-rigorous-phase-equilibrium.png)

### Worked Example 5

**Problem.** At low pressure, φ≈1 and γ≈1. What rigorous VLE form does fugacity equality approach?

**Solution.** Raoult's law: yiP≈xiPisat.

---

## 4.6 Activity Coefficients and Liquid-Phase Nonideality

The activity coefficient \(\gamma_i\) corrects liquid-phase nonideality. The Handbook gives a Van Laar form for binary systems.

Values near one indicate near-ideal liquid behavior. Large deviations from one mean Raoult's-law predictions may be poor without an activity model.

\[\hat f_i^L=x_i\gamma_i f_i^L\]

![FIG-03-04-006: Binary-mixture activity coefficients versus composition, showing ideal gamma=1 and nonideal deviations.](../figures/FIG-03-04-006-activity-coefficients-and-liquid-phase-nonideality.png)

### Worked Example 6

**Problem.** If γA=2 at given x, is liquid more or less ideal than γA=1?

**Solution.** More nonideal; activity is twice xi on the chosen standard-state basis.

---

## 4.7 Chemical Reaction Equilibrium

For a reacting mixture, equilibrium is determined by standard Gibbs energy change and activities through the equilibrium constant.

The reaction quotient has the same activity-product structure; equilibrium occurs when the quotient equals \(K\).

\[\Delta G^\circ=-RT\ln K,\qquad K=\prod_i a_i^{\nu_i}\]

![FIG-03-04-007: Reaction-coordinate diagram with Gibbs-energy minimum and activity-based equilibrium constant expression.](../figures/FIG-03-04-007-chemical-reaction-equilibrium.png)

### Worked Example 7

**Problem.** If ΔG°=-RT ln K and K>1, what sign is ΔG°?

**Solution.** Negative.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** For yA=0.6 and xA=0.3, find K-value.

**Solution.** K=2.

### Worked Example 9

**Problem.** At a dew point with yA=0.5, KA=2 and KB=0.5, evaluate Σy/K.

**Solution.** 0.5/2+0.5/0.5=1.25, so the assumed state is not the dew point.

---

## As the Handbook States It

Primary source basis: **Thermodynamics, printed pp. 153–156; FE Chemical specification Area 7F–G**.

**Source boundary:** The Handbook directly provides Henry's law, Raoult's law, rigorous fugacity equality, activity-coefficient and fugacity-coefficient forms, phase relations, Gibbs phase rule, reaction extent, and chemical-equilibrium expressions.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using Gibbs phase rule without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using Henry-law equilibrium without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using Raoult-law VLE without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using phase-equilibrium K value without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using fugacity phase equilibrium without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using activity coefficient without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using chemical reaction equilibrium without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| Gibbs phase rule | Concept developed in §4.1; apply with the section's stated basis and assumptions. |
| Henry-law equilibrium | Concept developed in §4.2; apply with the section's stated basis and assumptions. |
| Raoult-law VLE | Concept developed in §4.3; apply with the section's stated basis and assumptions. |
| phase-equilibrium K value | Concept developed in §4.4; apply with the section's stated basis and assumptions. |
| fugacity phase equilibrium | Concept developed in §4.5; apply with the section's stated basis and assumptions. |
| activity coefficient | Concept developed in §4.6; apply with the section's stated basis and assumptions. |
| chemical reaction equilibrium | Concept developed in §4.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **Gibbs phase rule** and state the governing relation or balance.

2. Define **Henry-law equilibrium** and state the governing relation or balance.

3. Define **Raoult-law VLE** and state the governing relation or balance.

4. Define **phase-equilibrium K value** and state the governing relation or balance.

5. Define **fugacity phase equilibrium** and state the governing relation or balance.

6. Define **activity coefficient** and state the governing relation or balance.

7. Define **chemical reaction equilibrium** and state the governing relation or balance.

8. What is the most likely error if **Gibbs phase rule** is applied before the process basis and boundary are defined?

9. What is the most likely error if **Henry-law equilibrium** is applied before the process basis and boundary are defined?

10. What is the most likely error if **Raoult-law VLE** is applied before the process basis and boundary are defined?

11. What is the most likely error if **phase-equilibrium K value** is applied before the process basis and boundary are defined?

12. What is the most likely error if **fugacity phase equilibrium** is applied before the process basis and boundary are defined?

13. What is the most likely error if **activity coefficient** is applied before the process basis and boundary are defined?

14. What is the most likely error if **chemical reaction equilibrium** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **Gibbs phase rule**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **Henry-law equilibrium**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **Raoult-law VLE**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **phase-equilibrium K value**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **fugacity phase equilibrium**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **activity coefficient**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **chemical reaction equilibrium**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **Gibbs phase rule**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **Henry-law equilibrium**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **Gibbs phase rule** is developed in §4.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **Henry-law equilibrium** is developed in §4.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **Raoult-law VLE** is developed in §4.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **phase-equilibrium K value** is developed in §4.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **fugacity phase equilibrium** is developed in §4.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **activity coefficient** is developed in §4.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **chemical reaction equilibrium** is developed in §4.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

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

19. **A.** The relation or workflow for **Gibbs phase rule** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **Henry-law equilibrium** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **Raoult-law VLE** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **phase-equilibrium K value** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **fugacity phase equilibrium** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **activity coefficient** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **chemical reaction equilibrium** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **Gibbs phase rule** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

27. **A.** The relation or workflow for **Henry-law equilibrium** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. For a nonreacting binary two-phase system, use phase rule to find degrees of freedom.

2. Henry constant is 500 kPa and x=0.002. Find equilibrium gas partial pressure.

3. At 80°C, Psat,A=80 kPa and xA=0.4. Raoult partial pressure?

4. Binary liquid has xA=0.4, KA=1.5, KB=0.667. Check bubble criterion ΣKx if xB=0.6.

5. At low pressure, φ≈1 and γ≈1. What rigorous VLE form does fugacity equality approach?

6. If γA=2 at given x, is liquid more or less ideal than γA=1?

7. If ΔG°=-RT ln K and K>1, what sign is ΔG°?

8. For yA=0.6 and xA=0.3, find K-value.

9. At a dew point with yA=0.5, KA=2 and KB=0.5, evaluate Σy/K.

10. What equality defines phase equilibrium rigorously for each component?


---

## Practice Problem Solutions

1. F=C+2-P=2+2-2=2.

2. p=Hx=1.0 kPa.

3. pA=32 kPa.

4. 1.5(0.4)+0.667(0.6)=1.0002≈1; near bubble condition.

5. Raoult's law: yiP≈xiPisat.

6. More nonideal; activity is twice xi on the chosen standard-state basis.

7. Negative.

8. K=2.

9. 0.5/2+0.5/0.5=1.25, so the assumed state is not the dew point.

10. Equal component fugacity in each phase.


---

## Quick Reference

**Source anchor:** Thermodynamics, printed pp. 153–156; FE Chemical specification Area 7F–G.

- **Gibbs phase rule:** Gibbs Phase Rule and Phase Equilibrium
- **Henry-law equilibrium:** Henry's Law for Dilute Solutes
- **Raoult-law VLE:** Raoult's Law and Ideal VLE
- **phase-equilibrium K value:** K-Values, Bubble Points, and Dew Points
- **fugacity phase equilibrium:** Fugacity Equality for Rigorous Phase Equilibrium
- **activity coefficient:** Activity Coefficients and Liquid-Phase Nonideality
- **chemical reaction equilibrium:** Chemical Reaction Equilibrium
---

## What's Next

**03-05 — Molecular Diffusion and Convective Mass Transfer**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor