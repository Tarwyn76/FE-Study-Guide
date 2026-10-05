---
chapter: "02-07"
title: "Rate of Return and Minimum Attractive Rate of Return"
layer: 2
tier: A
template: technical
ledger_ids: [ECON-2A-007-01, ECON-2A-007-02, ECON-2A-007-03, ECON-2A-007-04, ECON-2A-007-05, ECON-2A-007-06, ECON-2A-007-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-07: Rate of Return and Minimum Attractive Rate of Return

> *"Professional engineering decisions are strongest when the governing duty, assumption, and economic model are all made explicit."*

---

## Before You Start

**Prerequisites:** 02-06

**Skip if:** You can correctly apply every section objective below, including the scenario and calculation checks, without relying on memorized wording alone.

**Time:** About 75–105 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

Rate of return is the interest rate that makes an investment's equivalent benefits and costs balance. MARR is the minimum rate the decision maker is willing to accept. The distinction is simple but essential: ROR describes the project; MARR is the decision threshold.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **07.1** Explain and apply **Meaning of Rate of Return**.
* **07.2** Explain and apply **Minimum Attractive Rate of Return**.
* **07.3** Explain and apply **Solving for ROR**.
* **07.4** Explain and apply **Conventional versus Nonconventional Cash Flows**.
* **07.5** Explain and apply **Incremental Comparison**.
* **07.6** Explain and apply **ROR and Present Worth Consistency**.
* **07.7** Explain and apply **Decision Limits**.

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

## 07.1 Meaning of Rate of Return

The Handbook defines rate of return as the interest rate that makes benefits and costs equal.

For a cash-flow series $C_t$, the rate i* satisfies

$$0=\sum_{t=0}^{n}\frac{C_t}{(1+i^*)^t}.$$

This is the internal-rate-of-return condition for a conventional project.

![FIG-02-07-001: Present worth versus interest rate curve crossing zero at the project rate of return.](../figures/FIG-02-07-001-meaning-of-rate-of-return.png)

### Worked Example 1 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **ROR**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 07.2 Minimum Attractive Rate of Return

MARR is the minimum acceptable or attractive rate of return specified by the decision maker.

A project with return below MARR is economically unattractive under the stated criterion. A project above MARR may be acceptable, subject to risk, constraints, and comparison with alternatives.

![FIG-02-07-002: Rate scale with project ROR compared to MARR threshold.](../figures/FIG-02-07-002-minimum-attractive-rate-of-return.png)

### Worked Example 2 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **MARR**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 07.3 Solving for ROR

Simple one-payment problems can be solved algebraically. More complex cash flows usually require trial-and-error, interpolation, a financial function, or numerical root finding.

Always verify that the solution actually makes present worth approximately zero.

![FIG-02-07-003: ROR solution workflow: write PW(i)=0 -> bracket root -> solve/interpolate -> substitute to verify.](../figures/FIG-02-07-003-solving-for-ror.png)

### Worked Example 3 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Solving ROR**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 07.4 Conventional versus Nonconventional Cash Flows

A conventional investment has one initial sign followed by cash flows of the opposite sign. Nonconventional patterns can change sign more than once.

Multiple sign changes can produce multiple mathematical rates of return or no useful unique rate. In such cases, present worth at MARR is often clearer.

![FIG-02-07-004: Conventional cash flow with one sign change versus nonconventional with multiple sign changes and possible multiple PW zero crossings.](../figures/FIG-02-07-004-conventional-versus-nonconventional-cash-flows.png)

### Worked Example 4 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Multiple roots**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 07.5 Incremental Comparison

For mutually exclusive alternatives, comparing each alternative's standalone ROR can give a misleading ranking. Incremental analysis evaluates the additional investment required to move from a lower-cost alternative to a higher-cost alternative.

The incremental cash flow is compared with MARR to determine whether the extra investment is justified.

![FIG-02-07-005: Alternative B minus Alternative A cash-flow timeline feeding incremental ROR decision against MARR.](../figures/FIG-02-07-005-incremental-comparison.png)

### Worked Example 5 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Incremental**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 07.6 ROR and Present Worth Consistency

For a conventional cash flow with a unique ROR, if ROR exceeds MARR, present worth evaluated at MARR is positive. If ROR is below MARR, present worth is negative.

This relationship is a useful reasonableness check.

![FIG-02-07-006: PW-vs-i curve with zero at ROR and vertical MARR line showing positive or negative PW region.](../figures/FIG-02-07-006-ror-and-present-worth-consistency.png)

### Worked Example 6 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Consistency**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 07.7 Decision Limits

ROR is a compact performance measure, but it does not directly show project scale. A small project can have a high ROR and create less total economic value than a larger project.

Use the decision criterion appropriate to the problem, and do not turn one metric into a universal ranking rule.

![FIG-02-07-007: Small high-ROR project versus larger lower-ROR project with greater net present value, illustrating metric scale limitation.](../figures/FIG-02-07-007-decision-limits.png)

### Worked Example 7 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Limits**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. The principal Handbook basis for this chapter is **Engineering Economics / Rate-of-Return**, printed p. **236**. Where the chapter adds interpretation, decision workflow, contract/liability context, or derived relationships not printed explicitly in that section, those additions are guide-developed and should not be mistaken for quoted Handbook language.

---

## Where This Goes Wrong

**Treating ROR as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating MARR as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Solving ROR as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Multiple roots as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Incremental as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Consistency as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Limits as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Skipping the governing facts.** Professional and economic rules are conditional on the actual scenario, timing, jurisdiction, or cash-flow structure.

---

## Key Terms

| Term | Working definition |
|---|---|
| rate of return | Concept developed in this chapter; use the controlling section definition and conditions. |
| minimum attractive rate of return | Concept developed in this chapter; use the controlling section definition and conditions. |
| ROR root | Concept developed in this chapter; use the controlling section definition and conditions. |
| nonconventional cash flow | Concept developed in this chapter; use the controlling section definition and conditions. |
| incremental rate of return | Concept developed in this chapter; use the controlling section definition and conditions. |
| ROR-PW consistency | Concept developed in this chapter; use the controlling section definition and conditions. |
| rate-of-return limitation | Concept developed in this chapter; use the controlling section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. State the central engineering decision or principle developed in **Meaning of Rate of Return**.

2. State the central engineering decision or principle developed in **Minimum Attractive Rate of Return**.

3. State the central engineering decision or principle developed in **Solving for ROR**.

4. State the central engineering decision or principle developed in **Conventional versus Nonconventional Cash Flows**.

5. State the central engineering decision or principle developed in **Incremental Comparison**.

6. State the central engineering decision or principle developed in **ROR and Present Worth Consistency**.

7. State the central engineering decision or principle developed in **Decision Limits**.

8. What common error would result from ignoring the distinction emphasized in **Meaning of Rate of Return**?

9. What common error would result from ignoring the distinction emphasized in **Minimum Attractive Rate of Return**?

10. What common error would result from ignoring the distinction emphasized in **Solving for ROR**?

11. What common error would result from ignoring the distinction emphasized in **Conventional versus Nonconventional Cash Flows**?

12. What common error would result from ignoring the distinction emphasized in **Incremental Comparison**?

13. What common error would result from ignoring the distinction emphasized in **ROR and Present Worth Consistency**?

14. What common error would result from ignoring the distinction emphasized in **Decision Limits**?

15. Identify the first fact you would verify before solving a problem from this chapter.

16. Explain why a correct formula or rule can still produce a wrong engineering decision.

17. Describe one reason documentation or an explicit timeline improves the analysis.

18. State one check you would perform before accepting a final answer.

### Multiple Choice

19. Which choice best matches the chapter's use of **ROR**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

20. Which choice best matches the chapter's use of **MARR**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

21. Which choice best matches the chapter's use of **Solving ROR**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

22. Which choice best matches the chapter's use of **Multiple roots**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

23. Which choice best matches the chapter's use of **Incremental**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

24. Which choice best matches the chapter's use of **Consistency**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

25. Which choice best matches the chapter's use of **Limits**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

26. Which choice best matches the chapter's use of **ROR**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

27. Which choice best matches the chapter's use of **MARR**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment


---

## Answer Key with Explanations

1. The central principle is **ROR**. Apply that section's rule to the governing facts and assumptions.

2. The central principle is **MARR**. Apply that section's rule to the governing facts and assumptions.

3. The central principle is **Solving ROR**. Apply that section's rule to the governing facts and assumptions.

4. The central principle is **Multiple roots**. Apply that section's rule to the governing facts and assumptions.

5. The central principle is **Incremental**. Apply that section's rule to the governing facts and assumptions.

6. The central principle is **Consistency**. Apply that section's rule to the governing facts and assumptions.

7. The central principle is **Limits**. Apply that section's rule to the governing facts and assumptions.

8. It would apply the wrong professional or economic rule. First distinguish **ROR** from nearby concepts, then apply it under the section's stated conditions.

9. It would apply the wrong professional or economic rule. First distinguish **MARR** from nearby concepts, then apply it under the section's stated conditions.

10. It would apply the wrong professional or economic rule. First distinguish **Solving ROR** from nearby concepts, then apply it under the section's stated conditions.

11. It would apply the wrong professional or economic rule. First distinguish **Multiple roots** from nearby concepts, then apply it under the section's stated conditions.

12. It would apply the wrong professional or economic rule. First distinguish **Incremental** from nearby concepts, then apply it under the section's stated conditions.

13. It would apply the wrong professional or economic rule. First distinguish **Consistency** from nearby concepts, then apply it under the section's stated conditions.

14. It would apply the wrong professional or economic rule. First distinguish **Limits** from nearby concepts, then apply it under the section's stated conditions.

15. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

16. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

17. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

18. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

19. **A.** The chapter uses **ROR** as the section-specific engineering concept or criterion.

20. **A.** The chapter uses **MARR** as the section-specific engineering concept or criterion.

21. **A.** The chapter uses **Solving ROR** as the section-specific engineering concept or criterion.

22. **A.** The chapter uses **Multiple roots** as the section-specific engineering concept or criterion.

23. **A.** The chapter uses **Incremental** as the section-specific engineering concept or criterion.

24. **A.** The chapter uses **Consistency** as the section-specific engineering concept or criterion.

25. **A.** The chapter uses **Limits** as the section-specific engineering concept or criterion.

26. **A.** The chapter uses **ROR** as the section-specific engineering concept or criterion.

27. **A.** The chapter uses **MARR** as the section-specific engineering concept or criterion.


---

## Practice Problems

1. An investment of $10,000 returns $13,310 in 3 years. Find ROR.

2. A project costs $5,000 and returns $2,000 annually for 3 years. Write the ROR equation.

3. For Problem 2, estimate whether ROR is above or below 10% by evaluating PW at 10%.

4. If project ROR is 14% and MARR is 10%, state the conventional accept/reject result.

5. If ROR is 8% and MARR 12%, state the result.

6. Explain why nonconventional cash flows can have multiple ROR roots.

7. Explain why mutually exclusive projects should not always be ranked by standalone ROR.

8. Define incremental ROR.

9. State the ROR-PW consistency rule for conventional cash flows.

10. Explain one limitation of ROR.


---

## Practice Problem Solutions

1. $(1+i)^3=13310/10000=1.331$, so $i=\boxed{10\%}$.

2. $0=-5000+2000(P/A,i,3)$.

3. $PW=-5000+2000((1.1**3-1)/(0.10*1.1**3))=\boxed{-26.30}$; positive PW means ROR is above 10%.

4. Accept under the simple conventional ROR criterion because ROR > MARR.

5. Reject under that criterion because ROR < MARR.

6. Multiple cash-flow sign changes can make the PW polynomial cross zero more than once.

7. ROR ignores scale and can mis-rank the value of extra investment; use incremental analysis or PW/AW.

8. It is the ROR of the difference in cash flows between two mutually exclusive alternatives.

9. For a unique conventional ROR: at MARR below ROR, PW is positive; above ROR, PW is negative.

10. It does not directly measure project scale or total value and may be ambiguous for nonconventional cash flows.


---

## Quick Reference

**Handbook anchor:** Engineering Economics / Rate-of-Return, printed p. 236.

- **ROR:** rate of return
- **MARR:** minimum attractive rate of return
- **Solving ROR:** ROR root
- **Multiple roots:** nonconventional cash flow
- **Incremental:** incremental rate of return
- **Consistency:** ROR-PW consistency
- **Limits:** rate-of-return limitation

---

## What's Next

**02-08 — Breakeven, Benefit-Cost, and Payback Analysis**

Carry forward the rule: identify the engineering question first, then select the professional or economic tool that answers that question.

— Your Mentor
