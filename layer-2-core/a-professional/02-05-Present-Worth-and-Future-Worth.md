---
chapter: "02-05"
title: "Present Worth and Future Worth"
layer: 2
tier: A
template: technical
ledger_ids: [ECON-2A-005-01, ECON-2A-005-02, ECON-2A-005-03, ECON-2A-005-04, ECON-2A-005-05, ECON-2A-005-06, ECON-2A-005-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-05: Present Worth and Future Worth

> *"Professional engineering decisions are strongest when the governing duty, assumption, and economic model are all made explicit."*

---

## Before You Start

**Prerequisites:** 02-04

**Skip if:** You can correctly apply every section objective below, including the scenario and calculation checks, without relying on memorized wording alone.

**Time:** About 75–105 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

Present worth and future worth place alternatives on a common monetary basis. The Handbook supplies single-payment and uniform-series factors. The engineering task is to identify the cash-flow pattern, choose the comparison date, and apply the correct direction of conversion.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **05.1** Explain and apply **Single-Payment Present Worth**.
* **05.2** Explain and apply **Single-Payment Future Worth**.
* **05.3** Explain and apply **Uniform-Series Future Worth**.
* **05.4** Explain and apply **Uniform-Series Present Worth**.
* **05.5** Explain and apply **Mixed Cash-Flow Present Worth**.
* **05.6** Explain and apply **Comparing Alternatives by Present Worth**.
* **05.7** Explain and apply **Future Worth as an Equivalent Criterion**.

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

## 05.1 Single-Payment Present Worth

For a future amount F received n periods from now,

$$P=F(P/F,i,n)=F(1+i)^{-n}.$$

Present worth discounts the future amount because money available earlier can earn interest.

![FIG-02-05-001: Future amount F at year n discounted by P/F arrow to present P.](../figures/FIG-02-05-001-single-payment-present-worth.png)

### Worked Example 1 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Single PW**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 05.2 Single-Payment Future Worth

For present amount P,

$$F=P(F/P,i,n)=P(1+i)^n.$$

Future worth accumulates a present amount to the chosen future date.

![FIG-02-05-002: Present P compounded by F/P arrow to F at year n.](../figures/FIG-02-05-002-single-payment-future-worth.png)

### Worked Example 2 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Single FW**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 05.3 Uniform-Series Future Worth

For equal end-of-period payments A over n periods,

$$F=A(F/A,i,n)=A\frac{(1+i)^n-1}{i}.$$

The final payment occurs at the same date as F and therefore earns no additional period of interest.

![FIG-02-05-003: Uniform series A at ends of periods 1 through n accumulated to F at period n.](../figures/FIG-02-05-003-uniform-series-future-worth.png)

### Worked Example 3 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Series FW**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 05.4 Uniform-Series Present Worth

The present worth of a uniform end-of-period series is

$$P=A(P/A,i,n)
=A\frac{(1+i)^n-1}{i(1+i)^n}.$$

This is one of the most frequently used engineering-economy relations.

![FIG-02-05-004: Uniform A series discounted to a single P at time zero.](../figures/FIG-02-05-004-uniform-series-present-worth.png)

### Worked Example 4 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Series PW**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 05.5 Mixed Cash-Flow Present Worth

Real alternatives often combine first cost, annual operating cost, periodic maintenance, salvage, and revenue.

Calculate present worth by converting each component separately:

$$PW=\sum P_k.$$

Keep signs visible rather than hiding them inside prose.

![FIG-02-05-005: Mixed project cash flow with first cost, annual O&M, overhaul, and salvage all converted to PW.](../figures/FIG-02-05-005-mixed-cash-flow-present-worth.png)

### Worked Example 5 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Mixed PW**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 05.6 Comparing Alternatives by Present Worth

For mutually exclusive alternatives evaluated over a common study period, convert all relevant cash flows to present worth at the MARR and choose according to the problem's objective.

For cost-only alternatives with equal service, the lower equivalent cost is preferred. For net-benefit alternatives, the larger net present worth is preferred.

Do not compare first cost alone when future costs differ.

![FIG-02-05-006: Two alternatives with different timing converted to comparable PW columns.](../figures/FIG-02-05-006-comparing-alternatives-by-present-worth.png)

### Worked Example 6 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Comparison**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 05.7 Future Worth as an Equivalent Criterion

Future worth uses the same equivalence principle as present worth. If every cash flow is moved consistently to the same future date at the same rate, alternative ranking is equivalent to present-worth ranking.

Choose the criterion that makes the cash-flow pattern easiest to evaluate.

![FIG-02-05-007: Present-worth and future-worth comparison paths demonstrating identical ranking when same i and study period are used.](../figures/FIG-02-05-007-future-worth-as-an-equivalent-criterion.png)

### Worked Example 7 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **FW criterion**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. The principal Handbook basis for this chapter is **Engineering Economics / Single Payment and Uniform Series Factors**, printed p. **235**. Where the chapter adds interpretation, decision workflow, contract/liability context, or derived relationships not printed explicitly in that section, those additions are guide-developed and should not be mistaken for quoted Handbook language.

---

## Where This Goes Wrong

**Treating Single PW as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Single FW as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Series FW as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Series PW as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Mixed PW as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Comparison as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating FW criterion as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Skipping the governing facts.** Professional and economic rules are conditional on the actual scenario, timing, jurisdiction, or cash-flow structure.

---

## Key Terms

| Term | Working definition |
|---|---|
| single-payment present worth | Concept developed in this chapter; use the controlling section definition and conditions. |
| single-payment future worth | Concept developed in this chapter; use the controlling section definition and conditions. |
| uniform series | Concept developed in this chapter; use the controlling section definition and conditions. |
| uniform-series present worth | Concept developed in this chapter; use the controlling section definition and conditions. |
| net present worth | Concept developed in this chapter; use the controlling section definition and conditions. |
| present-worth comparison | Concept developed in this chapter; use the controlling section definition and conditions. |
| future-worth comparison | Concept developed in this chapter; use the controlling section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. State the central engineering decision or principle developed in **Single-Payment Present Worth**.

2. State the central engineering decision or principle developed in **Single-Payment Future Worth**.

3. State the central engineering decision or principle developed in **Uniform-Series Future Worth**.

4. State the central engineering decision or principle developed in **Uniform-Series Present Worth**.

5. State the central engineering decision or principle developed in **Mixed Cash-Flow Present Worth**.

6. State the central engineering decision or principle developed in **Comparing Alternatives by Present Worth**.

7. State the central engineering decision or principle developed in **Future Worth as an Equivalent Criterion**.

8. What common error would result from ignoring the distinction emphasized in **Single-Payment Present Worth**?

9. What common error would result from ignoring the distinction emphasized in **Single-Payment Future Worth**?

10. What common error would result from ignoring the distinction emphasized in **Uniform-Series Future Worth**?

11. What common error would result from ignoring the distinction emphasized in **Uniform-Series Present Worth**?

12. What common error would result from ignoring the distinction emphasized in **Mixed Cash-Flow Present Worth**?

13. What common error would result from ignoring the distinction emphasized in **Comparing Alternatives by Present Worth**?

14. What common error would result from ignoring the distinction emphasized in **Future Worth as an Equivalent Criterion**?

15. Identify the first fact you would verify before solving a problem from this chapter.

16. Explain why a correct formula or rule can still produce a wrong engineering decision.

17. Describe one reason documentation or an explicit timeline improves the analysis.

18. State one check you would perform before accepting a final answer.

### Multiple Choice

19. Which choice best matches the chapter's use of **Single PW**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

20. Which choice best matches the chapter's use of **Single FW**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

21. Which choice best matches the chapter's use of **Series FW**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

22. Which choice best matches the chapter's use of **Series PW**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

23. Which choice best matches the chapter's use of **Mixed PW**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

24. Which choice best matches the chapter's use of **Comparison**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

25. Which choice best matches the chapter's use of **FW criterion**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

26. Which choice best matches the chapter's use of **Single PW**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

27. Which choice best matches the chapter's use of **Single FW**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment


---

## Answer Key with Explanations

1. The central principle is **Single PW**. Apply that section's rule to the governing facts and assumptions.

2. The central principle is **Single FW**. Apply that section's rule to the governing facts and assumptions.

3. The central principle is **Series FW**. Apply that section's rule to the governing facts and assumptions.

4. The central principle is **Series PW**. Apply that section's rule to the governing facts and assumptions.

5. The central principle is **Mixed PW**. Apply that section's rule to the governing facts and assumptions.

6. The central principle is **Comparison**. Apply that section's rule to the governing facts and assumptions.

7. The central principle is **FW criterion**. Apply that section's rule to the governing facts and assumptions.

8. It would apply the wrong professional or economic rule. First distinguish **Single PW** from nearby concepts, then apply it under the section's stated conditions.

9. It would apply the wrong professional or economic rule. First distinguish **Single FW** from nearby concepts, then apply it under the section's stated conditions.

10. It would apply the wrong professional or economic rule. First distinguish **Series FW** from nearby concepts, then apply it under the section's stated conditions.

11. It would apply the wrong professional or economic rule. First distinguish **Series PW** from nearby concepts, then apply it under the section's stated conditions.

12. It would apply the wrong professional or economic rule. First distinguish **Mixed PW** from nearby concepts, then apply it under the section's stated conditions.

13. It would apply the wrong professional or economic rule. First distinguish **Comparison** from nearby concepts, then apply it under the section's stated conditions.

14. It would apply the wrong professional or economic rule. First distinguish **FW criterion** from nearby concepts, then apply it under the section's stated conditions.

15. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

16. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

17. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

18. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

19. **A.** The chapter uses **Single PW** as the section-specific engineering concept or criterion.

20. **A.** The chapter uses **Single FW** as the section-specific engineering concept or criterion.

21. **A.** The chapter uses **Series FW** as the section-specific engineering concept or criterion.

22. **A.** The chapter uses **Series PW** as the section-specific engineering concept or criterion.

23. **A.** The chapter uses **Mixed PW** as the section-specific engineering concept or criterion.

24. **A.** The chapter uses **Comparison** as the section-specific engineering concept or criterion.

25. **A.** The chapter uses **FW criterion** as the section-specific engineering concept or criterion.

26. **A.** The chapter uses **Single PW** as the section-specific engineering concept or criterion.

27. **A.** The chapter uses **Single FW** as the section-specific engineering concept or criterion.


---

## Practice Problems

1. Find PW of $12,000 due in 6 years at 7%.

2. Find FW of $8,000 invested for 5 years at 5%.

3. Find PW of $2,000 paid annually for 4 years at 6%.

4. Find FW of $1,500 deposited annually for 5 years at 4%.

5. A project costs $10,000 now and returns $3,000 annually for 5 years at 8%. Find net PW.

6. Add a $2,000 salvage at year 5 to Problem 5 and recompute PW.

7. Explain why first cost alone cannot compare two alternatives with different O&M costs.

8. State the factor converting A to P.

9. State the factor converting A to F.

10. Explain why PW and FW rankings agree when applied consistently.


---

## Practice Problem Solutions

1. $P=12000/(1.07)^6=\boxed{7,996.11}$.

2. $F=8000(1.05)^5=\boxed{10,210.25}$.

3. $P=2000[(1.06)^4-1]/[0.06(1.06)^4]=\boxed{6,930.21}$.

4. $F=1500[(1.04)^5-1]/0.04=\boxed{8,124.48}$.

5. Net $PW=-10000+3000(P/A,8\%,5)=\boxed{1,978.13}$.

6. Add $2000/(1.08)^5$; net $PW=\boxed{3,339.30}$.

7. Economic comparison must include all relevant equivalent cash flows, not only acquisition cost.

8. $(P/A,i,n)$.

9. $(F/A,i,n)$.

10. Multiplying every equivalent present value by the same positive $(F/P,i,n)$ factor preserves ranking.


---

## Quick Reference

**Handbook anchor:** Engineering Economics / Single Payment and Uniform Series Factors, printed p. 235.

- **Single PW:** single-payment present worth
- **Single FW:** single-payment future worth
- **Series FW:** uniform series
- **Series PW:** uniform-series present worth
- **Mixed PW:** net present worth
- **Comparison:** present-worth comparison
- **FW criterion:** future-worth comparison

---

## What's Next

**02-06 — Annual Worth, Capital Recovery, and Gradient Series**

Carry forward the rule: identify the engineering question first, then select the professional or economic tool that answers that question.

— Your Mentor
