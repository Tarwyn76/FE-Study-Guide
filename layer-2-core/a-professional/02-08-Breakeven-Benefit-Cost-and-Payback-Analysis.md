---
chapter: "02-08"
title: "Breakeven, Benefit-Cost, and Payback Analysis"
layer: 2
tier: A
template: technical
ledger_ids: [ECON-2A-008-01, ECON-2A-008-02, ECON-2A-008-03, ECON-2A-008-04, ECON-2A-008-05, ECON-2A-008-06, ECON-2A-008-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-08: Breakeven, Benefit-Cost, and Payback Analysis

> *"Professional engineering decisions are strongest when the governing duty, assumption, and economic model are all made explicit."*

---

## Before You Start

**Prerequisites:** 02-07

**Skip if:** You can correctly apply every section objective below, including the scenario and calculation checks, without relying on memorized wording alone.

**Time:** About 75–105 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

Breakeven, benefit-cost, and payback are compact decision tools with different purposes. Breakeven solves for the value that makes alternatives equal, benefit-cost compares equivalent benefits and costs, and payback measures how long benefits take to recover an investment. None should be used outside the question it actually answers.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **08.1** Explain and apply **Breakeven as Equality**.
* **08.2** Explain and apply **Fixed and Variable Cost Model**.
* **08.3** Explain and apply **Revenue Breakeven**.
* **08.4** Explain and apply **Benefit-Cost Analysis**.
* **08.5** Explain and apply **Payback Period**.
* **08.6** Explain and apply **Choosing the Right Metric**.
* **08.7** Explain and apply **Limitations and Sensitivity**.

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

## 08.1 Breakeven as Equality

The Handbook defines breakeven as the value of a variable that makes two alternatives equally economical while other variables are held constant.

Set the alternatives equal and solve for the unknown:

$$EC_A(x)=EC_B(x).$$

The unknown might be production volume, operating hours, unit price, or service life.

![FIG-02-08-001: Two cost lines crossing at breakeven quantity Q_BE, with lower-cost regions labeled for each alternative.](../figures/FIG-02-08-001-breakeven-as-equality.png)

### Worked Example 1 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Breakeven**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 08.2 Fixed and Variable Cost Model

A common linear cost model is

$$C=F+vQ,$$

where F is fixed cost, v is variable cost per unit, and Q is quantity.

For two alternatives,

$$F_A+v_AQ=F_B+v_BQ,$$

so

$$Q_{BE}=\frac{F_B-F_A}{v_A-v_B},$$

when the denominator is nonzero.

![FIG-02-08-002: Fixed-plus-variable cost lines showing intercepts F_A/F_B and slopes v_A/v_B.](../figures/FIG-02-08-002-fixed-and-variable-cost-model.png)

### Worked Example 2 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Cost-volume**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 08.3 Revenue Breakeven

With revenue $R=pQ$ and cost $C=F+vQ$, break-even quantity satisfies

$$pQ=F+vQ,$$

giving

$$Q_{BE}=\frac{F}{p-v}.$$

The denominator is contribution margin per unit.

![FIG-02-08-003: Revenue and total-cost lines crossing at Q_BE with fixed-cost intercept.](../figures/FIG-02-08-003-revenue-breakeven.png)

### Worked Example 3 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Revenue BE**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 08.4 Benefit-Cost Analysis

The Handbook states that benefits should exceed estimated costs:

$$B-C\ge0$$

or

$$\frac{B}{C}\ge1.$$

Benefits and costs must be expressed on an equivalent economic basis before forming the comparison.

![FIG-02-08-004: Equivalent present worth benefits and costs feeding B-C and B/C decision tests.](../figures/FIG-02-08-004-benefit-cost-analysis.png)

### Worked Example 4 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **B/C**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 08.5 Payback Period

The Handbook defines payback period as the time required for profit or other benefits to equal the investment cost.

Simple payback often ignores the time value of money unless the problem explicitly uses discounted payback. Therefore payback is a liquidity/recovery measure, not a complete profitability criterion.

![FIG-02-08-005: Cumulative cash-flow curve crossing zero at payback time.](../figures/FIG-02-08-005-payback-period.png)

### Worked Example 5 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Payback**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 08.6 Choosing the Right Metric

Use breakeven when the question asks for the threshold value of a variable. Use B/C when the problem is structured around equivalent benefits and costs. Use payback when recovery time matters.

Do not compare a payback period numerically with a rate of return; they are different quantities.

![FIG-02-08-006: Decision tree selecting breakeven, B/C, payback, PW/AW, or ROR based on question type.](../figures/FIG-02-08-006-choosing-the-right-metric.png)

### Worked Example 6 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Metric choice**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 08.7 Limitations and Sensitivity

All three methods depend on assumptions. A breakeven point moves when fixed or variable costs change. B/C changes with discount rate and classification of items as benefits or costs. Payback can ignore cash flows after recovery.

Sensitivity analysis should test the variables that materially influence the decision.

![FIG-02-08-007: Sensitivity plot showing breakeven threshold shifting as variable cost changes, with callouts for assumption dependence.](../figures/FIG-02-08-007-limitations-and-sensitivity.png)

### Worked Example 7 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Sensitivity**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. The principal Handbook basis for this chapter is **Engineering Economics / Breakeven, Payback, and Benefit-Cost Analysis**, printed p. **236–237**. Where the chapter adds interpretation, decision workflow, contract/liability context, or derived relationships not printed explicitly in that section, those additions are guide-developed and should not be mistaken for quoted Handbook language.

---

## Where This Goes Wrong

**Treating Breakeven as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Cost-volume as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Revenue BE as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating B/C as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Payback as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Metric choice as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Sensitivity as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Skipping the governing facts.** Professional and economic rules are conditional on the actual scenario, timing, jurisdiction, or cash-flow structure.

---

## Key Terms

| Term | Working definition |
|---|---|
| breakeven point | Concept developed in this chapter; use the controlling section definition and conditions. |
| fixed cost | Concept developed in this chapter; use the controlling section definition and conditions. |
| variable cost | Concept developed in this chapter; use the controlling section definition and conditions. |
| contribution margin | Concept developed in this chapter; use the controlling section definition and conditions. |
| benefit-cost ratio | Concept developed in this chapter; use the controlling section definition and conditions. |
| payback period | Concept developed in this chapter; use the controlling section definition and conditions. |
| economic screening metric | Concept developed in this chapter; use the controlling section definition and conditions. |
| economic sensitivity | Concept developed in this chapter; use the controlling section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. State the central engineering decision or principle developed in **Breakeven as Equality**.

2. State the central engineering decision or principle developed in **Fixed and Variable Cost Model**.

3. State the central engineering decision or principle developed in **Revenue Breakeven**.

4. State the central engineering decision or principle developed in **Benefit-Cost Analysis**.

5. State the central engineering decision or principle developed in **Payback Period**.

6. State the central engineering decision or principle developed in **Choosing the Right Metric**.

7. State the central engineering decision or principle developed in **Limitations and Sensitivity**.

8. What common error would result from ignoring the distinction emphasized in **Breakeven as Equality**?

9. What common error would result from ignoring the distinction emphasized in **Fixed and Variable Cost Model**?

10. What common error would result from ignoring the distinction emphasized in **Revenue Breakeven**?

11. What common error would result from ignoring the distinction emphasized in **Benefit-Cost Analysis**?

12. What common error would result from ignoring the distinction emphasized in **Payback Period**?

13. What common error would result from ignoring the distinction emphasized in **Choosing the Right Metric**?

14. What common error would result from ignoring the distinction emphasized in **Limitations and Sensitivity**?

15. Identify the first fact you would verify before solving a problem from this chapter.

16. Explain why a correct formula or rule can still produce a wrong engineering decision.

17. Describe one reason documentation or an explicit timeline improves the analysis.

18. State one check you would perform before accepting a final answer.

### Multiple Choice

19. Which choice best matches the chapter's use of **Breakeven**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

20. Which choice best matches the chapter's use of **Cost-volume**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

21. Which choice best matches the chapter's use of **Revenue BE**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

22. Which choice best matches the chapter's use of **B/C**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

23. Which choice best matches the chapter's use of **Payback**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

24. Which choice best matches the chapter's use of **Metric choice**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

25. Which choice best matches the chapter's use of **Sensitivity**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

26. Which choice best matches the chapter's use of **Breakeven**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

27. Which choice best matches the chapter's use of **Cost-volume**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment


---

## Answer Key with Explanations

1. The central principle is **Breakeven**. Apply that section's rule to the governing facts and assumptions.

2. The central principle is **Cost-volume**. Apply that section's rule to the governing facts and assumptions.

3. The central principle is **Revenue BE**. Apply that section's rule to the governing facts and assumptions.

4. The central principle is **B/C**. Apply that section's rule to the governing facts and assumptions.

5. The central principle is **Payback**. Apply that section's rule to the governing facts and assumptions.

6. The central principle is **Metric choice**. Apply that section's rule to the governing facts and assumptions.

7. The central principle is **Sensitivity**. Apply that section's rule to the governing facts and assumptions.

8. It would apply the wrong professional or economic rule. First distinguish **Breakeven** from nearby concepts, then apply it under the section's stated conditions.

9. It would apply the wrong professional or economic rule. First distinguish **Cost-volume** from nearby concepts, then apply it under the section's stated conditions.

10. It would apply the wrong professional or economic rule. First distinguish **Revenue BE** from nearby concepts, then apply it under the section's stated conditions.

11. It would apply the wrong professional or economic rule. First distinguish **B/C** from nearby concepts, then apply it under the section's stated conditions.

12. It would apply the wrong professional or economic rule. First distinguish **Payback** from nearby concepts, then apply it under the section's stated conditions.

13. It would apply the wrong professional or economic rule. First distinguish **Metric choice** from nearby concepts, then apply it under the section's stated conditions.

14. It would apply the wrong professional or economic rule. First distinguish **Sensitivity** from nearby concepts, then apply it under the section's stated conditions.

15. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

16. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

17. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

18. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

19. **A.** The chapter uses **Breakeven** as the section-specific engineering concept or criterion.

20. **A.** The chapter uses **Cost-volume** as the section-specific engineering concept or criterion.

21. **A.** The chapter uses **Revenue BE** as the section-specific engineering concept or criterion.

22. **A.** The chapter uses **B/C** as the section-specific engineering concept or criterion.

23. **A.** The chapter uses **Payback** as the section-specific engineering concept or criterion.

24. **A.** The chapter uses **Metric choice** as the section-specific engineering concept or criterion.

25. **A.** The chapter uses **Sensitivity** as the section-specific engineering concept or criterion.

26. **A.** The chapter uses **Breakeven** as the section-specific engineering concept or criterion.

27. **A.** The chapter uses **Cost-volume** as the section-specific engineering concept or criterion.


---

## Practice Problems

1. Alternative A costs 20,000 + 5Q; B costs 40,000 + 3Q. Find breakeven Q.

2. Product sells for $50/unit, variable cost $30/unit, fixed cost $100,000. Find revenue breakeven quantity.

3. Equivalent benefits are $120,000 and costs $100,000. Find B-C and B/C.

4. Initial cost is $60,000 and annual undiscounted benefit is $15,000. Find simple payback.

5. Explain why simple payback can mis-rank long-lived projects.

6. Which metric answers 'At what annual production does alternative B become cheaper?'

7. Which metric answers 'How many years until initial cost is recovered?'

8. If B/C=0.92, what does the Handbook criterion indicate?

9. If B-C=0, what economic condition exists?

10. Name two inputs worth sensitivity-testing in a breakeven analysis.


---

## Practice Problem Solutions

1. Set equal: $20000+5Q=40000+3Q$, so $Q=\boxed{10,000}$ units.

2. $Q=100000/(50-30)=\boxed{5,000}$ units.

3. $B-C=\boxed{20,000}$ and $B/C=\boxed{1.20}$.

4. $60000/15000=\boxed{4}$ years.

5. It ignores cash flows after payback and commonly ignores time value of money.

6. Breakeven analysis.

7. Payback period.

8. Benefits are less than equivalent costs under the stated comparison; it fails the $B/C\ge1$ test.

9. Breakeven/economic equivalence of benefits and costs.

10. Fixed cost and variable cost are two direct examples; price, utilization, and service life may also matter.


---

## Quick Reference

**Handbook anchor:** Engineering Economics / Breakeven, Payback, and Benefit-Cost Analysis, printed p. 236–237.

- **Breakeven:** breakeven point
- **Cost-volume:** fixed cost
- **Revenue BE:** contribution margin
- **B/C:** benefit-cost ratio
- **Payback:** payback period
- **Metric choice:** economic screening metric
- **Sensitivity:** economic sensitivity

---

## What's Next

**02-09 — Inflation, Depreciation, Taxes, and Replacement**

Carry forward the rule: identify the engineering question first, then select the professional or economic tool that answers that question.

— Your Mentor
