---
chapter: "02-13"
title: "Solutions, Concentration, Acids, Bases, and pH"
layer: 2
tier: B
template: technical
ledger_ids: [SCI-2B-013-01, SCI-2B-013-02, SCI-2B-013-03, SCI-2B-013-04, SCI-2B-013-05, SCI-2B-013-06, SCI-2B-013-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-13: Solutions, Concentration, Acids, Bases, and pH

> *"Physical science becomes engineering when the microscopic model, measured property, and safety consequence are connected explicitly."*

---

## Before You Start

**Prerequisites:** 02-12 · 01-06

**Skip if:** You can solve the calculation and scenario checks in this chapter while stating the assumptions and Handbook source used.

**Time:** About 85–115 min reading and worked examples · 40–50 min review questions · 60–80 min practice problems.

---

## On the Board Today

The Handbook directly defines molarity, molality, normality, pH, acid/base pH regions, water ion product, Ka/pKa, solubility product, and boiling/freezing-point effects. Buffer equations and titration workflow are guide-developed background.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **13.1** Explain and apply **Molarity, Molality, and Normality**.
* **13.2** Explain and apply **Dilution and Mixing**.
* **13.3** Explain and apply **Acids, Bases, pH, and pOH**.
* **13.4** Explain and apply **Weak Acids, Ka, and pKa**.
* **13.5** Explain and apply **Buffers and Titration Logic**.
* **13.6** Explain and apply **Solubility Product and Precipitation**.
* **13.7** Explain and apply **Colligative Effects and Concentration Checks**.

---

## Notation Used Here

Notation is introduced within each section where needed. Use SI units unless a problem or Handbook table specifies another basis.

---

## 13.1 Molarity, Molality, and Normality

The Handbook defines three common concentration measures.

**Molarity**:

\[
M=\frac{\text{mol solute}}{\text{L solution}}.
\]

**Molality**:

\[
m=\frac{\text{mol solute}}{\text{kg solvent}}.
\]

**Normality** is the molarity multiplied by the number of reactive equivalents per mole for the reaction being considered.

Molarity depends on solution volume and therefore can vary slightly with temperature. Molality is mass-based and does not depend on thermal expansion of the solution volume. Normality is reaction-dependent: the same substance can have different normality interpretations for different reactions.

![FIG-02-13-001: Three concentration boxes comparing molarity, molality, and normality with numerators, denominators, and dependence on reaction or temperature.](../figures/FIG-02-13-001-molarity-molality-and-normality.png)

### Worked Example 1 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **solution concentration** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 13.2 Dilution and Mixing

Dilution conserves moles of solute when no reaction occurs. For a single-solute dilution,

\[
M_1V_1=M_2V_2.
\]

This equation assumes the same solute before and after dilution and additive/conventional solution-volume treatment appropriate to the problem.

For mixing streams with no reaction, calculate total moles of solute and divide by final solution volume:

\[
M_f=\frac{\sum M_iV_i}{V_f}.
\]

If a chemical reaction occurs during mixing, stoichiometry must be completed before the final concentration calculation.

![FIG-02-13-002: Two solution streams with labeled M and V entering a mixing vessel, showing mole balance and final molarity.](../figures/FIG-02-13-002-dilution-and-mixing.png)

### Worked Example 2 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **dilution** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 13.3 Acids, Bases, pH, and pOH

The Handbook gives

\[
pH=-\log_{10}[H^+].
\]

For water at the standard reference condition used in the Handbook,

\[
[H^+][OH^-]=10^{-14},
\]

so

\[
pH+pOH=14.
\]

Acidic aqueous solutions have \(pH<7\), basic solutions have \(pH>7\), and neutral water is near pH 7 at the stated condition.

Because pH is logarithmic, a change of one pH unit corresponds to a factor of ten in hydrogen-ion concentration.

![FIG-02-13-003: Logarithmic pH scale from acidic through neutral to basic with hydrogen-ion concentrations labeled by powers of ten.](../figures/FIG-02-13-003-acids-bases-ph-and-poh.png)

### Worked Example 3 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **pH** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 13.4 Weak Acids, Ka, and pKa

For weak acid

\[
HA\rightleftharpoons H^++A^-,
\]

the Handbook gives the acid-dissociation constant form

\[
K_a=\frac{[H^+][A^-]}{[HA]}
\]

and

\[
pK_a=-\log_{10}K_a.
\]

A smaller \(pK_a\) corresponds to larger \(K_a\) and stronger acid behavior within a comparable family.

When equilibrium concentrations are required, use an ICE table—initial, change, equilibrium—to connect stoichiometry with the equilibrium expression.

![FIG-02-13-004: Weak-acid equilibrium with an ICE table showing initial, change, and equilibrium concentrations feeding the Ka expression.](../figures/FIG-02-13-004-weak-acids-ka-and-pka.png)

### Worked Example 4 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **acid equilibrium** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 13.5 Buffers and Titration Logic

A buffer contains a weak acid/base pair that resists pH change by consuming added acid or base. The Henderson-Hasselbalch form,

\[
pH=pK_a+\log\frac{[A^-]}{[HA]},
\]

is a guide-developed relation useful when the assumptions are satisfied.

In a titration, first perform reaction stoichiometry. Before equivalence, the remaining weak species and conjugate partner may form a buffer. At equivalence, the conjugate species controls pH. Beyond equivalence, excess strong titrant often dominates.

Do not insert initial concentrations into an equilibrium equation before accounting for the stoichiometric reaction.

![FIG-02-13-005: Generic weak-acid/strong-base titration curve showing buffer region, half-equivalence where pH=pKa, equivalence point, and excess-base region.](../figures/FIG-02-13-005-buffers-and-titration-logic.png)

### Worked Example 5 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **buffers** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 13.6 Solubility Product and Precipitation

For slightly soluble salt

\[
A_mB_n\rightleftharpoons mA^{n+}+nB^{m-},
\]

the Handbook gives a solubility-product expression of the form

\[
K_{sp}=[A^{n+}]^m[B^{m-}]^n.
\]

Compare the **ion product** \(Q\) with \(K_{sp}\):

- \(Q<K_{sp}\): unsaturated relative to the solid,
- \(Q=K_{sp}\): equilibrium/saturation,
- \(Q>K_{sp}\): precipitation is thermodynamically favored.

Account for stoichiometric exponents carefully.

![FIG-02-13-006: Precipitation decision diagram comparing Q with Ksp and showing unsaturated, saturated, and precipitation regions.](../figures/FIG-02-13-006-solubility-product-and-precipitation.png)

### Worked Example 6 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **solubility** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 13.7 Colligative Effects and Concentration Checks

The Handbook notes that a nonvolatile solute raises boiling point and lowers freezing point. The magnitude depends on the number of dissolved particles and solution concentration.

Even when a detailed colligative-property formula is supplied in a problem, concentration units still matter. Molarity, molality, and mole fraction are not interchangeable.

Final checks for solution problems should include: correct basis, correct reaction before dilution/equilibrium, logarithm sign, physically possible concentration, and consistent units.

![FIG-02-13-007: Pure-solvent versus solution phase-change sketch showing boiling-point elevation and freezing-point depression.](../figures/FIG-02-13-007-colligative-effects-and-concentration-checks.png)

### Worked Example 7 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **colligative effects** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Chemistry and Biology pp. 86–87**.

**Source boundary:** The Handbook directly defines molarity, molality, normality, pH, acid/base pH regions, water ion product, Ka/pKa, solubility product, and boiling/freezing-point effects. Buffer equations and titration workflow are guide-developed background.

---

## Where This Goes Wrong

**Using solution concentration without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using dilution without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using pH without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using acid equilibrium without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using buffers without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using solubility without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using colligative effects without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Replacing supplied data with a memorized trend.** If the Handbook or problem gives specific property, potential, limit, or compatibility data, use it.


---

## Key Terms

| Term | Working definition |
|---|---|
| molarity | Term introduced in this chapter; use the definition and conditions in the owning section. |
| molality | Term introduced in this chapter; use the definition and conditions in the owning section. |
| normality | Term introduced in this chapter; use the definition and conditions in the owning section. |
| dilution equation | Term introduced in this chapter; use the definition and conditions in the owning section. |
| solution mixing | Term introduced in this chapter; use the definition and conditions in the owning section. |
| pH | Term introduced in this chapter; use the definition and conditions in the owning section. |
| pOH | Term introduced in this chapter; use the definition and conditions in the owning section. |
| water ion product | Term introduced in this chapter; use the definition and conditions in the owning section. |
| acid dissociation constant | Term introduced in this chapter; use the definition and conditions in the owning section. |
| pKa | Term introduced in this chapter; use the definition and conditions in the owning section. |
| ICE table | Term introduced in this chapter; use the definition and conditions in the owning section. |
| buffer | Term introduced in this chapter; use the definition and conditions in the owning section. |
| Henderson-Hasselbalch relation | Term introduced in this chapter; use the definition and conditions in the owning section. |
| equivalence point | Term introduced in this chapter; use the definition and conditions in the owning section. |
| solubility product | Term introduced in this chapter; use the definition and conditions in the owning section. |
| ion product | Term introduced in this chapter; use the definition and conditions in the owning section. |
| precipitation condition | Term introduced in this chapter; use the definition and conditions in the owning section. |
| boiling-point elevation | Term introduced in this chapter; use the definition and conditions in the owning section. |
| freezing-point depression | Term introduced in this chapter; use the definition and conditions in the owning section. |

---

## Review Questions

### Conceptual and Applied

1. Define **solution concentration** and state its engineering significance.

2. Define **dilution** and state its engineering significance.

3. Define **pH** and state its engineering significance.

4. Define **acid equilibrium** and state its engineering significance.

5. Define **buffers** and state its engineering significance.

6. Define **solubility** and state its engineering significance.

7. Define **colligative effects** and state its engineering significance.

8. What error is likely if **solution concentration** is used without checking the problem's state, composition, units, or assumptions?

9. What error is likely if **dilution** is used without checking the problem's state, composition, units, or assumptions?

10. What error is likely if **pH** is used without checking the problem's state, composition, units, or assumptions?

11. What error is likely if **acid equilibrium** is used without checking the problem's state, composition, units, or assumptions?

12. What error is likely if **buffers** is used without checking the problem's state, composition, units, or assumptions?

13. What error is likely if **solubility** is used without checking the problem's state, composition, units, or assumptions?

14. What error is likely if **colligative effects** is used without checking the problem's state, composition, units, or assumptions?

15. Identify one Handbook table, equation, or definition you would locate before solving a representative problem from this chapter.

16. State one physical-reasonableness or dimensional check appropriate to this chapter.

17. Explain when measured or tabulated data should replace a qualitative trend.

18. Give one example of an interpretation in this chapter that is guide-developed rather than a verbatim Handbook rule.

### Multiple Choice

19. Which answer best describes **solution concentration**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

20. Which answer best describes **dilution**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

21. Which answer best describes **pH**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

22. Which answer best describes **acid equilibrium**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

23. Which answer best describes **buffers**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

24. Which answer best describes **solubility**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

25. Which answer best describes **colligative effects**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

26. Which answer best describes **solution concentration**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

27. Which answer best describes **dilution**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data


---

## Answer Key with Explanations

1. **solution concentration** is the central concept of §13.1; apply the definition, assumptions, and engineering consequence developed in that section.

2. **dilution** is the central concept of §13.2; apply the definition, assumptions, and engineering consequence developed in that section.

3. **pH** is the central concept of §13.3; apply the definition, assumptions, and engineering consequence developed in that section.

4. **acid equilibrium** is the central concept of §13.4; apply the definition, assumptions, and engineering consequence developed in that section.

5. **buffers** is the central concept of §13.5; apply the definition, assumptions, and engineering consequence developed in that section.

6. **solubility** is the central concept of §13.6; apply the definition, assumptions, and engineering consequence developed in that section.

7. **colligative effects** is the central concept of §13.7; apply the definition, assumptions, and engineering consequence developed in that section.

8. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

9. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

10. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

11. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

12. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

13. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

14. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

15. Use the Handbook source identified in the chapter, then verify dimensions/physical bounds; supplied data controls over remembered trends. Guide-developed interpretations are explicitly identified in the source-boundary note.

16. Use the Handbook source identified in the chapter, then verify dimensions/physical bounds; supplied data controls over remembered trends. Guide-developed interpretations are explicitly identified in the source-boundary note.

17. Use the Handbook source identified in the chapter, then verify dimensions/physical bounds; supplied data controls over remembered trends. Guide-developed interpretations are explicitly identified in the source-boundary note.

18. Use the Handbook source identified in the chapter, then verify dimensions/physical bounds; supplied data controls over remembered trends. Guide-developed interpretations are explicitly identified in the source-boundary note.

19. **A.** The chapter applies **solution concentration** only under its stated physical/model assumptions.

20. **A.** The chapter applies **dilution** only under its stated physical/model assumptions.

21. **A.** The chapter applies **pH** only under its stated physical/model assumptions.

22. **A.** The chapter applies **acid equilibrium** only under its stated physical/model assumptions.

23. **A.** The chapter applies **buffers** only under its stated physical/model assumptions.

24. **A.** The chapter applies **solubility** only under its stated physical/model assumptions.

25. **A.** The chapter applies **colligative effects** only under its stated physical/model assumptions.

26. **A.** The chapter applies **solution concentration** only under its stated physical/model assumptions.

27. **A.** The chapter applies **dilution** only under its stated physical/model assumptions.


---

## Practice Problems

1. 1. Find molarity of 0.50 mol solute in 2.00 L solution.

2. 2. How many moles are in 250 mL of 0.80 M solution?

3. 3. Dilute 100 mL of 2.0 M solution to 500 mL. Find final molarity.

4. 4. Find pH when [H+]=1.0×10−3 M.

5. 5. Find [H+] for pH 5.20.

6. 6. At the Handbook water reference condition, find pOH for pH 9.30.

7. 7. If Ka=1.8×10−5, find pKa.

8. 8. For equal concentrations of HA and A− in a buffer, what does Henderson-Hasselbalch predict for pH relative to pKa?

9. 9. If Qsp<Ksp, is precipitation thermodynamically required?

10. 10. Explain the difference between molarity and molality.


---

## Practice Problem Solutions

1. 1. M=0.50/2.00=0.250 M.

2. 2. n=0.80×0.250=0.200 mol.

3. 3. M2=M1V1/V2=2.0(100/500)=0.40 M.

4. 4. pH=3.00.

5. 5. [H+]=10^−5.20=6.31×10^−6 M.

6. 6. pOH=14−9.30=4.70.

7. 7. pKa=−log10(1.8×10^−5)=4.745.

8. 8. pH=pKa because log([A−]/[HA])=log(1)=0.

9. 9. No. Qsp<Ksp corresponds to an unsaturated state relative to that solid.

10. 10. Molarity is mol/L solution; molality is mol/kg solvent.


---

## Quick Reference

**Handbook anchor:** Chemistry and Biology pp. 86–87.

- **solution concentration:** Molarity, Molality, and Normality
- **dilution:** Dilution and Mixing
- **pH:** Acids, Bases, pH, and pOH
- **acid equilibrium:** Weak Acids, Ka, and pKa
- **buffers:** Buffers and Titration Logic
- **solubility:** Solubility Product and Precipitation
- **colligative effects:** Colligative Effects and Concentration Checks

---

## What's Next

**02-14 — Chemical Equilibrium, Electrochemistry, and Corrosion**

Carry forward the rule: identify the physical model and service condition before selecting the formula, property, or safety control.

— Your Mentor
