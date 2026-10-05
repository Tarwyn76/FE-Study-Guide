---
chapter: "02-06"
title: "Annual Worth, Capital Recovery, and Gradient Series"
layer: 2
tier: A
template: technical
ledger_ids: [ECON-2A-006-01, ECON-2A-006-02, ECON-2A-006-03, ECON-2A-006-04, ECON-2A-006-05, ECON-2A-006-06, ECON-2A-006-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-06: Annual Worth, Capital Recovery, and Gradient Series

> *"Professional engineering decisions are strongest when the governing duty, assumption, and economic model are all made explicit."*

---

## Before You Start

**Prerequisites:** 02-05

**Skip if:** You can correctly apply every section objective below, including the scenario and calculation checks, without relying on memorized wording alone.

**Time:** About 75–105 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

Annual worth converts a project's equivalent value into a uniform amount per period. Capital recovery converts present cost into an equivalent uniform series, while sinking-fund and gradient factors handle recurring and systematically changing cash flows.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **06.1** Explain and apply **Annual Worth as an Equivalence Measure**.
* **06.2** Explain and apply **Capital Recovery**.
* **06.3** Explain and apply **Sinking Fund**.
* **06.4** Explain and apply **Arithmetic Gradients**.
* **06.5** Explain and apply **Gradient Conversion Factors**.
* **06.6** Explain and apply **Equivalent Annual Cost**.
* **06.7** Explain and apply **Timing and Sign Checks**.

---

## Notation Used Here

| Symbol | Meaning |
|---|---|
| $P$ | present worth/value |
| $F$ | future worth/value |
| $A$ | uniform end-of-period amount |
| $G$ | arithmetic gradient amount |
| $i$ | interest rate per period |
| $n$ | number of periods |
| $C$ | cost |
| $B$ | benefit |


---

## 06.1 Annual Worth as an Equivalence Measure

Annual worth expresses all project cash flows as one equivalent uniform amount A over the study period.

If present worth P is known,

$$A=P(A/P,i,n).$$

If the project is benefit-producing, a larger net annual worth is generally preferred; for cost-only alternatives, compare equivalent annual costs.

![FIG-02-06-001: Irregular project cash flows converted to equal annual amounts A.](../figures/FIG-02-06-001-annual-worth-as-an-equivalence-measure.png)

### Worked Example 1 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **AW**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 06.2 Capital Recovery

The capital-recovery factor converts present amount P to equal end-of-period amounts A:

$$A=P(A/P,i,n)
=P\frac{i(1+i)^n}{(1+i)^n-1}.$$

If salvage exists, treat it separately or use an equivalent derived form.

![FIG-02-06-002: Initial investment P transformed into n equal capital-recovery payments A.](../figures/FIG-02-06-002-capital-recovery.png)

### Worked Example 2 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **CR**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 06.3 Sinking Fund

The sinking-fund factor determines the uniform deposit required to accumulate future amount F:

$$A=F(A/F,i,n)
=F\frac{i}{(1+i)^n-1}.$$

This is the inverse direction of the uniform-series compound-amount factor.

![FIG-02-06-003: Equal deposits A accumulating to future target F.](../figures/FIG-02-06-003-sinking-fund.png)

### Worked Example 3 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **SF**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 06.4 Arithmetic Gradients

An arithmetic gradient changes by constant amount G from one period to the next. In the Handbook convention, the gradient component is zero in period 1, G in period 2, 2G in period 3, and so on.

The total cash flow may combine a base uniform series A with a gradient series G.

![FIG-02-06-004: Cash flows increasing by constant G each period: 0, G, 2G, 3G relative to a base series.](../figures/FIG-02-06-004-arithmetic-gradients.png)

### Worked Example 4 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Gradient**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 06.5 Gradient Conversion Factors

The Handbook provides P/G, F/G, and A/G factors. For annual equivalent of a gradient,

$$A_G=G(A/G,i,n)
=G\left[\frac{1}{i}-\frac{n}{(1+i)^n-1}\right].$$

Use the factor only after confirming the timing convention.

![FIG-02-06-005: Gradient G converted to P, F, or equivalent annual A using Handbook factors.](../figures/FIG-02-06-005-gradient-conversion-factors.png)

### Worked Example 5 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Gradient factors**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 06.6 Equivalent Annual Cost

Equivalent annual cost combines capital recovery, annual operating cost, recurring maintenance, and annualized salvage effects.

A common structure is

$$EAC=CR+O\&M+\text{other annual equivalents}.$$

Annualization is especially useful when alternatives have different first costs but provide comparable service over the chosen analysis framework.

![FIG-02-06-006: Annual cost stack: capital recovery + O&M + annualized maintenance - annualized salvage.](../figures/FIG-02-06-006-equivalent-annual-cost.png)

### Worked Example 6 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **EAC**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 06.7 Timing and Sign Checks

Uniform-series factors assume end-of-period cash flows. Gradient factors use a specific zero-at-period-1 convention. If a cash flow starts immediately or is delayed, shift it before applying the factor.

A correct formula with the wrong timeline is still a wrong solution.

![FIG-02-06-007: Correct versus shifted gradient timeline highlighting period-1 zero-gradient convention.](../figures/FIG-02-06-007-timing-and-sign-checks.png)

### Worked Example 7 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Timing**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. The principal Handbook basis for this chapter is **Engineering Economics / Uniform Series and Uniform Gradient Factors**, printed p. **235**. Where the chapter adds interpretation, decision workflow, contract/liability context, or derived relationships not printed explicitly in that section, those additions are guide-developed and should not be mistaken for quoted Handbook language.

---

## Where This Goes Wrong

**Treating AW as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating CR as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating SF as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Gradient as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Gradient factors as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating EAC as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Timing as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Skipping the governing facts.** Professional and economic rules are conditional on the actual scenario, timing, jurisdiction, or cash-flow structure.

---

## Key Terms

| Term | Working definition |
|---|---|
| annual worth | Concept developed in this chapter; use the controlling section definition and conditions. |
| capital recovery | Concept developed in this chapter; use the controlling section definition and conditions. |
| sinking fund | Concept developed in this chapter; use the controlling section definition and conditions. |
| arithmetic gradient | Concept developed in this chapter; use the controlling section definition and conditions. |
| gradient factor | Concept developed in this chapter; use the controlling section definition and conditions. |
| equivalent annual cost | Concept developed in this chapter; use the controlling section definition and conditions. |
| gradient timing convention | Concept developed in this chapter; use the controlling section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. State the central engineering decision or principle developed in **Annual Worth as an Equivalence Measure**.

2. State the central engineering decision or principle developed in **Capital Recovery**.

3. State the central engineering decision or principle developed in **Sinking Fund**.

4. State the central engineering decision or principle developed in **Arithmetic Gradients**.

5. State the central engineering decision or principle developed in **Gradient Conversion Factors**.

6. State the central engineering decision or principle developed in **Equivalent Annual Cost**.

7. State the central engineering decision or principle developed in **Timing and Sign Checks**.

8. What common error would result from ignoring the distinction emphasized in **Annual Worth as an Equivalence Measure**?

9. What common error would result from ignoring the distinction emphasized in **Capital Recovery**?

10. What common error would result from ignoring the distinction emphasized in **Sinking Fund**?

11. What common error would result from ignoring the distinction emphasized in **Arithmetic Gradients**?

12. What common error would result from ignoring the distinction emphasized in **Gradient Conversion Factors**?

13. What common error would result from ignoring the distinction emphasized in **Equivalent Annual Cost**?

14. What common error would result from ignoring the distinction emphasized in **Timing and Sign Checks**?

15. Identify the first fact you would verify before solving a problem from this chapter.

16. Explain why a correct formula or rule can still produce a wrong engineering decision.

17. Describe one reason documentation or an explicit timeline improves the analysis.

18. State one check you would perform before accepting a final answer.

### Multiple Choice

19. Which choice best matches the chapter's use of **AW**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

20. Which choice best matches the chapter's use of **CR**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

21. Which choice best matches the chapter's use of **SF**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

22. Which choice best matches the chapter's use of **Gradient**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

23. Which choice best matches the chapter's use of **Gradient factors**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

24. Which choice best matches the chapter's use of **EAC**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

25. Which choice best matches the chapter's use of **Timing**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

26. Which choice best matches the chapter's use of **AW**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

27. Which choice best matches the chapter's use of **CR**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment


---

## Answer Key with Explanations

1. The central principle is **AW**. Apply that section's rule to the governing facts and assumptions.

2. The central principle is **CR**. Apply that section's rule to the governing facts and assumptions.

3. The central principle is **SF**. Apply that section's rule to the governing facts and assumptions.

4. The central principle is **Gradient**. Apply that section's rule to the governing facts and assumptions.

5. The central principle is **Gradient factors**. Apply that section's rule to the governing facts and assumptions.

6. The central principle is **EAC**. Apply that section's rule to the governing facts and assumptions.

7. The central principle is **Timing**. Apply that section's rule to the governing facts and assumptions.

8. It would apply the wrong professional or economic rule. First distinguish **AW** from nearby concepts, then apply it under the section's stated conditions.

9. It would apply the wrong professional or economic rule. First distinguish **CR** from nearby concepts, then apply it under the section's stated conditions.

10. It would apply the wrong professional or economic rule. First distinguish **SF** from nearby concepts, then apply it under the section's stated conditions.

11. It would apply the wrong professional or economic rule. First distinguish **Gradient** from nearby concepts, then apply it under the section's stated conditions.

12. It would apply the wrong professional or economic rule. First distinguish **Gradient factors** from nearby concepts, then apply it under the section's stated conditions.

13. It would apply the wrong professional or economic rule. First distinguish **EAC** from nearby concepts, then apply it under the section's stated conditions.

14. It would apply the wrong professional or economic rule. First distinguish **Timing** from nearby concepts, then apply it under the section's stated conditions.

15. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

16. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

17. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

18. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

19. **A.** The chapter uses **AW** as the section-specific engineering concept or criterion.

20. **A.** The chapter uses **CR** as the section-specific engineering concept or criterion.

21. **A.** The chapter uses **SF** as the section-specific engineering concept or criterion.

22. **A.** The chapter uses **Gradient** as the section-specific engineering concept or criterion.

23. **A.** The chapter uses **Gradient factors** as the section-specific engineering concept or criterion.

24. **A.** The chapter uses **EAC** as the section-specific engineering concept or criterion.

25. **A.** The chapter uses **Timing** as the section-specific engineering concept or criterion.

26. **A.** The chapter uses **AW** as the section-specific engineering concept or criterion.

27. **A.** The chapter uses **CR** as the section-specific engineering concept or criterion.


---

## Practice Problems

1. Find annual equivalent of P=$20,000 over 5 years at 6%.

2. Find annual deposit needed to accumulate F=$10,000 in 4 years at 5%.

3. Find A/G for i=8%, n=5 and G=$500.

4. A machine costs $30,000 and has annual O&M $4,000 over 6 years at 7%, no salvage. Find EAC.

5. Repeat Problem 4 with $6,000 salvage at year 6.

6. State the timing of an arithmetic gradient's first G increment.

7. Explain capital recovery.

8. Explain sinking fund.

9. Why can an immediate year-0 annual payment not be inserted directly into an ordinary end-of-year A series?

10. Identify the Handbook factor that converts G to A.


---

## Practice Problem Solutions

1. $A=20000(A/P)=\boxed{4,747.93}$.

2. $A=10000(A/F)=\boxed{2,320.12}$.

3. $(A/G)=1/i-n/[(1+i)^n-1]=1.8465$, so $A_G=\boxed{923.24}$.

4. $EAC=30000(A/P,7\%,6)+4000=\boxed{10,293.87}$.

5. Subtract salvage annual equivalent: $EAC=\boxed{9,455.10}$.

6. The pure gradient component is 0 in period 1, G in period 2, 2G in period 3, etc.

7. Capital recovery is the uniform annual amount equivalent to a present investment over n periods at i.

8. Sinking fund is the uniform periodic deposit needed to accumulate a specified future amount.

9. Ordinary A-series factors assume end-of-period 1 through n timing; year-0 must be handled separately or shifted.

10. $(A/G,i,n)$.


---

## Quick Reference

**Handbook anchor:** Engineering Economics / Uniform Series and Uniform Gradient Factors, printed p. 235.

- **AW:** annual worth
- **CR:** capital recovery
- **SF:** sinking fund
- **Gradient:** arithmetic gradient
- **Gradient factors:** gradient factor
- **EAC:** equivalent annual cost
- **Timing:** gradient timing convention

---

## What's Next

**02-07 — Rate of Return and Minimum Attractive Rate of Return**

Carry forward the rule: identify the engineering question first, then select the professional or economic tool that answers that question.

— Your Mentor
