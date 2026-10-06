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

By the end of this chapter, you will be able to:

* **4.1** Explain and apply **Gibbs Phase Rule and Phase Equilibrium**.
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

**Solution.** For **Gibbs Phase Rule and Phase Equilibrium**, F=C+2-P=2+2-2=2. This follows because for a nonreacting equilibrium system, Gibbs phase rule relates number of components, phases, and independent intensive degrees of freedom.. That physical distinction controls the result for nonreacting binary two-phase system use phase rule.

---

## 4.2 Henry's Law for Dilute Solutes

The Handbook gives Henry's law for low-concentration solutes in gas-liquid equilibrium. Partial pressure is proportional to liquid-phase mole fraction through the stated Henry constant convention.

Henry constants appear in multiple unit conventions, so units must be checked before use.

\[p_i=y_iP=H_i x_i\]

![FIG-03-04-002: Dilute gas-solute equilibrium with partial pressure versus liquid mole fraction and Henry-law slope.](../figures/FIG-03-04-002-henry-s-law-for-dilute-solutes.png)

### Worked Example 2

**Problem.** Henry constant is 500 kPa and x=0.002. Find equilibrium gas partial pressure.

**Solution.** For **Henry's Law for Dilute Solutes**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) x=0.002, p=Hx=1.0 kPa. This is the section-specific result for Henry constant kPa equilibrium gas partial pressure. The stated units/basis (kPa, Pa) are retained.

---

## 4.3 Raoult's Law and Ideal VLE

For near-ideal liquid mixtures at sufficiently low pressure, Raoult's law relates component partial pressure to liquid mole fraction and pure-component saturation pressure.

Combining with Dalton's law gives \(y_iP=x_iP_i^{sat}\).

\[p_i=x_iP_i^{sat},\qquad y_iP=x_iP_i^{sat}\]

![FIG-03-04-003: Binary ideal-solution bubble/dew representation with liquid composition x and vapor composition y.](../figures/FIG-03-04-003-raoult-s-law-and-ideal-vle.png)

### Worked Example 3

**Problem.** At 80°C, Psat,A=80 kPa and xA=0.4. Raoult partial pressure?

**Solution.** For **Raoult's Law and Ideal VLE**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) A=80, xA=0.4, pA=32 kPa. This is the section-specific result for Psat kPa xA Raoult partial pressure. The stated units/basis (kPa, Pa) are retained.

---

## 4.4 K-Values, Bubble Points, and Dew Points

Define \(K_i=y_i/x_i\). Under ideal Raoult behavior, \(K_i=P_i^{sat}/P\). Bubble-point calculations begin with a liquid composition; dew-point calculations begin with a vapor composition.

At a bubble point \(\sum_i y_i=1\); at a dew point \(\sum_i x_i=1\).

\[K_i=\frac{y_i}{x_i},\qquad \sum_iK_ix_i=1\ \text{(bubble)},\qquad \sum_i\frac{y_i}{K_i}=1\ \text{(dew)}\]

![FIG-03-04-004: Binary mixture showing known liquid composition for bubble point and known vapor composition for dew point.](../figures/FIG-03-04-004-k-values-bubble-points-and-dew-points.png)

### Worked Example 4

**Problem.** Binary liquid has xA=0.4, KA=1.5, KB=0.667. Check bubble criterion ΣKx if xB=0.6.

**Solution.** For **K-Values, Bubble Points, and Dew Points**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) xA=0.4, KA=1.5, KB=0.667, 1.5(0.4)+0.667(0.6)=1.0002≈1; near bubble condition. This is the section-specific result for Binary liquid has xA KA KB Check. The stated units/basis (s, h) are retained.

---

## 4.5 Fugacity Equality for Rigorous Phase Equilibrium

The Handbook's rigorous VLE criterion is equality of component fugacity between vapor and liquid phases. Vapor fugacity commonly uses a fugacity coefficient; liquid fugacity commonly uses activity coefficient and a pure-liquid reference fugacity.

At low pressure and near-ideal behavior, these corrections approach unity and the rigorous form reduces toward Raoult's law.

\[\hat f_i^V=\hat f_i^L,\qquad \hat f_i^V=y_i\phi_iP,\qquad \hat f_i^L=x_i\gamma_i f_i^L\]

![FIG-03-04-005: Vapor and liquid fugacity expressions meeting at equilibrium, with phi and gamma corrections.](../figures/FIG-03-04-005-fugacity-equality-for-rigorous-phase-equilibrium.png)

### Worked Example 5

**Problem.** At low pressure, φ≈1 and γ≈1. What rigorous VLE form does fugacity equality approach?

**Solution.** For **Fugacity Equality for Rigorous Phase Equilibrium**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) ≈1, ≈1, Raoult's law: yiP≈xiPisat. This is the section-specific result for low pressure rigorous VLE form does fugacity. The stated units/basis (s, h) are retained.

---

## 4.6 Activity Coefficients and Liquid-Phase Nonideality

The activity coefficient \(\gamma_i\) corrects liquid-phase nonideality. The Handbook gives a Van Laar form for binary systems.

Values near one indicate near-ideal liquid behavior. Large deviations from one mean Raoult's-law predictions may be poor without an activity model.

\[\hat f_i^L=x_i\gamma_i f_i^L\]

![FIG-03-04-006: Binary-mixture activity coefficients versus composition, showing ideal gamma=1 and nonideal deviations.](../figures/FIG-03-04-006-activity-coefficients-and-liquid-phase-nonideality.png)

### Worked Example 6

**Problem.** If γA=2 at given x, is liquid more or less ideal than γA=1?

**Solution.** For **Activity Coefficients and Liquid-Phase Nonideality**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) A=2, A=1, More nonideal; activity is twice xi on the chosen standard-state basis. This is the section-specific result for given liquid more less ideal than. The stated units/basis (s, h) are retained.

---

## 4.7 Chemical Reaction Equilibrium

For a reacting mixture, equilibrium is determined by standard Gibbs energy change and activities through the equilibrium constant.

The reaction quotient has the same activity-product structure; equilibrium occurs when the quotient equals \(K\).

\[\Delta G^\circ=-RT\ln K,\qquad K=\prod_i a_i^{\nu_i}\]

![FIG-03-04-007: Reaction-coordinate diagram with Gibbs-energy minimum and activity-based equilibrium constant expression.](../figures/FIG-03-04-007-chemical-reaction-equilibrium.png)

### Worked Example 7

**Problem.** If ΔG°=-RT ln K and K>1, what sign is ΔG°?

**Solution.** For **Chemical Reaction Equilibrium**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) K>1, Negative. This is the section-specific result for RT ln sign. The stated units/basis (s, h) are retained.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** For yA=0.6 and xA=0.3, find K-value.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) yA=0.6, xA=0.3, K=2. This is the section-specific result for yA xA K-value.

### Worked Example 9

**Problem.** At a dew point with yA=0.5, KA=2 and KB=0.5, evaluate Σy/K.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) yA=0.5, KA=2, KB=0.5, 0.5/2+0.5/0.5=1.25, so the assumed state is not the dew point. This is the section-specific result for dew point yA KA KB evaluate. The stated units/basis (h) are retained.

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

1. **Gibbs Phase Rule and Phase Equilibrium.** For a nonreacting equilibrium system, Gibbs phase rule relates number of components, phases, and independent intensive degrees of freedom. In Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium, this is the definition or balance being tested by Question 1.

2. **Henry's Law for Dilute Solutes.** The Handbook gives Henry's law for low-concentration solutes in gas-liquid equilibrium. In Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium, this is the definition or balance being tested by Question 2.

3. **Raoult's Law and Ideal VLE.** For near-ideal liquid mixtures at sufficiently low pressure, Raoult's law relates component partial pressure to liquid mole fraction and pure-component saturation pressure. In Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium, this is the definition or balance being tested by Question 3.

4. **K-Values, Bubble Points, and Dew Points.** Bubble-point calculations begin with a liquid composition; dew-point calculations begin with a vapor composition. In Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium, this is the definition or balance being tested by Question 4.

5. **Fugacity Equality for Rigorous Phase Equilibrium.** The Handbook's rigorous VLE criterion is equality of component fugacity between vapor and liquid phases. In Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium, this is the definition or balance being tested by Question 5.

6. **Activity Coefficients and Liquid-Phase Nonideality.** The Handbook gives a Van Laar form for binary systems. In Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium, this is the definition or balance being tested by Question 6.

7. **Chemical Reaction Equilibrium.** For a reacting mixture, equilibrium is determined by standard Gibbs energy change and activities through the equilibrium constant. In Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium, this is the definition or balance being tested by Question 7.

8. For **Gibbs Phase Rule and Phase Equilibrium**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For a nonreacting equilibrium system, Gibbs phase rule relates number of components, phases, and independent intensive degrees of freedom. This is the specific failure mode emphasized in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.

9. For **Henry's Law for Dilute Solutes**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook gives Henry's law for low-concentration solutes in gas-liquid equilibrium. This is the specific failure mode emphasized in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.

10. For **Raoult's Law and Ideal VLE**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For near-ideal liquid mixtures at sufficiently low pressure, Raoult's law relates component partial pressure to liquid mole fraction and pure-component saturation pressure. This is the specific failure mode emphasized in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.

11. For **K-Values, Bubble Points, and Dew Points**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Bubble-point calculations begin with a liquid composition; dew-point calculations begin with a vapor composition. This is the specific failure mode emphasized in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.

12. For **Fugacity Equality for Rigorous Phase Equilibrium**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook's rigorous VLE criterion is equality of component fugacity between vapor and liquid phases. This is the specific failure mode emphasized in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.

13. For **Activity Coefficients and Liquid-Phase Nonideality**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook gives a Van Laar form for binary systems. This is the specific failure mode emphasized in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.

14. For **Chemical Reaction Equilibrium**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For a reacting mixture, equilibrium is determined by standard Gibbs energy change and activities through the equilibrium constant. This is the specific failure mode emphasized in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.

15. In **Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium**, close the material balance first because stream amounts and compositions feed the later energy calculation. Otherwise enthalpy and duty terms may be evaluated for unresolved streams.

16. For **Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium**, a degrees-of-freedom check counts unknowns against independent equations before solving. Zero indicates a closed problem; a positive count signals missing independent information.

17. In **Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium**, a relation supplied by the FE problem defines the intended model for that question. A remembered correlation can carry different assumptions, coefficients, validity limits, or reference states.

18. For **Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium**, separating Handbook-supported material from specification-required learned material distinguishes lookup knowledge from material the guide develops. That boundary prevents guide-developed content from being presented as Handbook text.

19. **A.** For **Gibbs Phase Rule and Phase Equilibrium**, the relation is meaningful only with the correct basis and physical assumptions. For a nonreacting equilibrium system, Gibbs phase rule relates number of components, phases, and independent intensive degrees of freedom. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

20. **A.** For **Henry's Law for Dilute Solutes**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook gives Henry's law for low-concentration solutes in gas-liquid equilibrium. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

21. **A.** For **Raoult's Law and Ideal VLE**, the relation is meaningful only with the correct basis and physical assumptions. For near-ideal liquid mixtures at sufficiently low pressure, Raoult's law relates component partial pressure to liquid mole fraction and pure-component saturation pressure. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

22. **A.** For **K-Values, Bubble Points, and Dew Points**, the relation is meaningful only with the correct basis and physical assumptions. Bubble-point calculations begin with a liquid composition; dew-point calculations begin with a vapor composition. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

23. **A.** For **Fugacity Equality for Rigorous Phase Equilibrium**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook's rigorous VLE criterion is equality of component fugacity between vapor and liquid phases. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

24. **A.** For **Activity Coefficients and Liquid-Phase Nonideality**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook gives a Van Laar form for binary systems. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

25. **A.** For **Chemical Reaction Equilibrium**, the relation is meaningful only with the correct basis and physical assumptions. For a reacting mixture, equilibrium is determined by standard Gibbs energy change and activities through the equilibrium constant. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

26. **A.** This later check revisits **Gibbs Phase Rule and Phase Equilibrium** from a different review position. For a nonreacting equilibrium system, Gibbs phase rule relates number of components, phases, and independent intensive degrees of freedom. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.

27. **A.** This later check revisits **Henry's Law for Dilute Solutes** from a different review position. The Handbook gives Henry's law for low-concentration solutes in gas-liquid equilibrium. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.


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

1. For the practice case involving **nonreacting binary two-phase system use phase rule**, F=C+2-P=2+2-2=2. This is the chapter-specific distinction required by Practice Problem 1 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.

2. For the practice case involving **Henry constant kPa equilibrium gas partial pressure**, Using x=0.002, p=Hx=1.0 kPa. This completes Practice Problem 2 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium. The original kPa, Pa basis is preserved.

3. For the practice case involving **Psat kPa xA Raoult partial pressure**, Using A=80, xA=0.4, pA=32 kPa. This completes Practice Problem 3 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium. The original kPa, Pa basis is preserved.

4. For the practice case involving **Binary liquid has xA KA KB Check**, Using xA=0.4, KA=1.5, KB=0.667, 1.5(0.4)+0.667(0.6)=1.0002≈1; near bubble condition. This completes Practice Problem 4 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium. The original s, h basis is preserved.

5. For the practice case involving **low pressure rigorous VLE form does fugacity**, Using ≈1, ≈1, Raoult's law: yiP≈xiPisat. This completes Practice Problem 5 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium. The original s, h basis is preserved.

6. For the practice case involving **given liquid more less ideal than**, Using A=2, A=1, More nonideal; activity is twice xi on the chosen standard-state basis. This completes Practice Problem 6 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium. The original s, h basis is preserved.

7. For the practice case involving **RT ln sign**, Using K>1, Negative. This completes Practice Problem 7 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium. The original s, h basis is preserved.

8. For the practice case involving **yA xA K-value**, Using yA=0.6, xA=0.3, K=2. This completes Practice Problem 8 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.

9. For the practice case involving **dew point yA KA KB evaluate**, Using yA=0.5, KA=2, KB=0.5, 0.5/2+0.5/0.5=1.25, so the assumed state is not the dew point. This completes Practice Problem 9 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium. The original h basis is preserved.

10. For the practice case involving **equality defines phase equilibrium rigorously each component**, Equal component fugacity in each phase. This is the chapter-specific distinction required by Practice Problem 10 in Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium.


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
