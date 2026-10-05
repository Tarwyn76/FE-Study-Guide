---
chapter: "02-04"
title: "Cash Flows, Interest, and Economic Equivalence"
layer: 2
tier: A
template: technical
ledger_ids: [ECON-2A-004-01, ECON-2A-004-02, ECON-2A-004-03, ECON-2A-004-04, ECON-2A-004-05, ECON-2A-004-06, ECON-2A-004-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-04: Cash Flows, Interest, and Economic Equivalence

> *"Professional engineering decisions are strongest when the governing duty, assumption, and economic model are all made explicit."*

---

## Before You Start

**Prerequisites:** 01-05 · 02-03

**Skip if:** You can correctly apply every section objective below, including the scenario and calculation checks, without relying on memorized wording alone.

**Time:** About 75–105 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

Engineering economics converts cash flows occurring at different times into comparable values. The Handbook supplies the standard interest factors, symbols, and non-annual compounding relation. This chapter establishes the time-value-of-money model that every later Tier 2A economics chapter uses.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **04.1** Explain and apply **Cash-Flow Diagrams and Sign Convention**.
* **04.2** Explain and apply **Interest and Compounding**.
* **04.3** Explain and apply **Economic Equivalence**.
* **04.4** Explain and apply **Nominal and Effective Interest**.
* **04.5** Explain and apply **Factor Notation**.
* **04.6** Explain and apply **Multiple Cash Flows**.
* **04.7** Explain and apply **Model Discipline and Common Errors**.

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

## 04.1 Cash-Flow Diagrams and Sign Convention

A cash-flow diagram places receipts and disbursements on a time axis. Choose a viewpoint and keep it consistent. A common convention is positive for receipts and negative for costs, but the arithmetic works with any consistent convention.

Time zero is the present. End-of-period convention means a cash flow labeled at year 3 occurs at the end of the third period unless the problem states otherwise.

Before choosing a factor, draw the timeline.

![FIG-02-04-001: Engineering cash-flow timeline with time 0 through n, upward receipt arrows, downward cost arrows, and labels P, F, and A.](../figures/FIG-02-04-001-cash-flow-diagrams-and-sign-convention.png)

### Worked Example 1 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Cash flows**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 04.2 Interest and Compounding

Interest is the price of using money over time. Under compound interest, each period earns interest on the accumulated balance.

For present amount P, periodic rate i, and n periods,

$$F=P(1+i)^n.$$

The reciprocal relation is

$$P=F(1+i)^{-n}.$$

These are the Handbook F/P and P/F factors.

![FIG-02-04-002: Compound-growth curve comparing present P and future F after n periods, with recurrence balance_{k+1}=balance_k(1+i).](../figures/FIG-02-04-002-interest-and-compounding.png)

### Worked Example 2 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Interest**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 04.3 Economic Equivalence

Two cash-flow patterns are economically equivalent at a stated interest rate when they have the same value at a common point in time.

Equivalence depends on the interest rate. Two alternatives equal at 5% need not be equal at 10%.

The reliable method is: choose a comparison date, move every cash flow to that date using the same rate, then compare.

![FIG-02-04-003: Two different cash-flow timelines converging to the same present-worth node at a specified interest rate.](../figures/FIG-02-04-003-economic-equivalence.png)

### Worked Example 3 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Equivalence**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 04.4 Nominal and Effective Interest

When interest is compounded m times per year at nominal annual rate r, the periodic rate is r/m. The Handbook gives the effective annual rate as

$$i_e=\left(1+\frac{r}{m}\right)^m-1.$$

Effective rate is the one-year growth rate after accounting for intra-year compounding.

![FIG-02-04-004: Nominal-versus-effective interest diagram showing r split into m compounding periods and annual accumulation to 1+i_e.](../figures/FIG-02-04-004-nominal-and-effective-interest.png)

### Worked Example 4 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Effective rate**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 04.5 Factor Notation

The Handbook notation

$$(F/P,i,n)$$

means the factor that converts P to F. Read the slash as "given": F given P.

Similarly, $(P/F,i,n)$ converts a known future amount to present worth. Later chapters use A/P, P/A, F/A, A/F, and gradient factors.

Factor notation prevents memorizing isolated formulas without understanding the direction of conversion.

![FIG-02-04-005: Factor-conversion map with P, F, A, and G nodes and arrows labeled F/P, P/F, A/P, P/A, F/A, A/F, and gradient factors.](../figures/FIG-02-04-005-factor-notation.png)

### Worked Example 5 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Factors**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 04.6 Multiple Cash Flows

For an irregular series, move each cash flow individually to the comparison date and sum algebraically.

For present worth,

$$P=\sum_{t=0}^{n}\frac{C_t}{(1+i)^t}.$$

This summation is a direct application of the single-payment present-worth factor.

![FIG-02-04-006: Irregular cash-flow timeline with different positive and negative amounts discounted individually to time zero and summed.](../figures/FIG-02-04-006-multiple-cash-flows.png)

### Worked Example 6 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Irregular series**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 04.7 Model Discipline and Common Errors

Match the interest period to the cash-flow period. Do not use an annual rate directly with monthly n unless the rate has been converted consistently.

Do not mix nominal and effective rates. Do not shift some cash flows to time zero and others to year n unless you then convert them to the same comparison date.

The most important check is dimensional in time: rate period and cash-flow period must agree.

![FIG-02-04-007: Pre-calculation checklist: viewpoint/signs, timeline, rate period, number of periods, common comparison date, correct factor direction.](../figures/FIG-02-04-007-model-discipline-and-common-errors.png)

### Worked Example 7 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Checks**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. The principal Handbook basis for this chapter is **Engineering Economics / Factors and Non-Annual Compounding**, printed p. **235–236**. Where the chapter adds interpretation, decision workflow, contract/liability context, or derived relationships not printed explicitly in that section, those additions are guide-developed and should not be mistaken for quoted Handbook language.

---

## Where This Goes Wrong

**Treating Cash flows as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Interest as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Equivalence as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Effective rate as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Factors as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Irregular series as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Checks as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Skipping the governing facts.** Professional and economic rules are conditional on the actual scenario, timing, jurisdiction, or cash-flow structure.

---

## Key Terms

| Term | Working definition |
|---|---|
| cash-flow diagram | Concept developed in this chapter; use the controlling section definition and conditions. |
| cash-flow sign convention | Concept developed in this chapter; use the controlling section definition and conditions. |
| compound interest | Concept developed in this chapter; use the controlling section definition and conditions. |
| interest period | Concept developed in this chapter; use the controlling section definition and conditions. |
| economic equivalence | Concept developed in this chapter; use the controlling section definition and conditions. |
| comparison date | Concept developed in this chapter; use the controlling section definition and conditions. |
| nominal annual rate | Concept developed in this chapter; use the controlling section definition and conditions. |
| effective annual rate | Concept developed in this chapter; use the controlling section definition and conditions. |
| engineering-economy factor notation | Concept developed in this chapter; use the controlling section definition and conditions. |
| irregular cash-flow series | Concept developed in this chapter; use the controlling section definition and conditions. |
| interest-period consistency | Concept developed in this chapter; use the controlling section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. State the central engineering decision or principle developed in **Cash-Flow Diagrams and Sign Convention**.

2. State the central engineering decision or principle developed in **Interest and Compounding**.

3. State the central engineering decision or principle developed in **Economic Equivalence**.

4. State the central engineering decision or principle developed in **Nominal and Effective Interest**.

5. State the central engineering decision or principle developed in **Factor Notation**.

6. State the central engineering decision or principle developed in **Multiple Cash Flows**.

7. State the central engineering decision or principle developed in **Model Discipline and Common Errors**.

8. What common error would result from ignoring the distinction emphasized in **Cash-Flow Diagrams and Sign Convention**?

9. What common error would result from ignoring the distinction emphasized in **Interest and Compounding**?

10. What common error would result from ignoring the distinction emphasized in **Economic Equivalence**?

11. What common error would result from ignoring the distinction emphasized in **Nominal and Effective Interest**?

12. What common error would result from ignoring the distinction emphasized in **Factor Notation**?

13. What common error would result from ignoring the distinction emphasized in **Multiple Cash Flows**?

14. What common error would result from ignoring the distinction emphasized in **Model Discipline and Common Errors**?

15. Identify the first fact you would verify before solving a problem from this chapter.

16. Explain why a correct formula or rule can still produce a wrong engineering decision.

17. Describe one reason documentation or an explicit timeline improves the analysis.

18. State one check you would perform before accepting a final answer.

### Multiple Choice

19. Which choice best matches the chapter's use of **Cash flows**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

20. Which choice best matches the chapter's use of **Interest**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

21. Which choice best matches the chapter's use of **Equivalence**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

22. Which choice best matches the chapter's use of **Effective rate**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

23. Which choice best matches the chapter's use of **Factors**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

24. Which choice best matches the chapter's use of **Irregular series**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

25. Which choice best matches the chapter's use of **Checks**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

26. Which choice best matches the chapter's use of **Cash flows**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

27. Which choice best matches the chapter's use of **Interest**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment


---

## Answer Key with Explanations

1. The central principle is **Cash flows**. Apply that section's rule to the governing facts and assumptions.

2. The central principle is **Interest**. Apply that section's rule to the governing facts and assumptions.

3. The central principle is **Equivalence**. Apply that section's rule to the governing facts and assumptions.

4. The central principle is **Effective rate**. Apply that section's rule to the governing facts and assumptions.

5. The central principle is **Factors**. Apply that section's rule to the governing facts and assumptions.

6. The central principle is **Irregular series**. Apply that section's rule to the governing facts and assumptions.

7. The central principle is **Checks**. Apply that section's rule to the governing facts and assumptions.

8. It would apply the wrong professional or economic rule. First distinguish **Cash flows** from nearby concepts, then apply it under the section's stated conditions.

9. It would apply the wrong professional or economic rule. First distinguish **Interest** from nearby concepts, then apply it under the section's stated conditions.

10. It would apply the wrong professional or economic rule. First distinguish **Equivalence** from nearby concepts, then apply it under the section's stated conditions.

11. It would apply the wrong professional or economic rule. First distinguish **Effective rate** from nearby concepts, then apply it under the section's stated conditions.

12. It would apply the wrong professional or economic rule. First distinguish **Factors** from nearby concepts, then apply it under the section's stated conditions.

13. It would apply the wrong professional or economic rule. First distinguish **Irregular series** from nearby concepts, then apply it under the section's stated conditions.

14. It would apply the wrong professional or economic rule. First distinguish **Checks** from nearby concepts, then apply it under the section's stated conditions.

15. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

16. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

17. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

18. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

19. **A.** The chapter uses **Cash flows** as the section-specific engineering concept or criterion.

20. **A.** The chapter uses **Interest** as the section-specific engineering concept or criterion.

21. **A.** The chapter uses **Equivalence** as the section-specific engineering concept or criterion.

22. **A.** The chapter uses **Effective rate** as the section-specific engineering concept or criterion.

23. **A.** The chapter uses **Factors** as the section-specific engineering concept or criterion.

24. **A.** The chapter uses **Irregular series** as the section-specific engineering concept or criterion.

25. **A.** The chapter uses **Checks** as the section-specific engineering concept or criterion.

26. **A.** The chapter uses **Cash flows** as the section-specific engineering concept or criterion.

27. **A.** The chapter uses **Interest** as the section-specific engineering concept or criterion.


---

## Practice Problems

1. Invest $5,000 at 6% annually for 4 years. Find F.

2. Find P equivalent to $10,000 received in 5 years at 8%.

3. A nominal 12% rate compounds monthly. Find the effective annual rate.

4. Cash flows are +$2,000 at year 1 and +$3,000 at year 3. Find present worth at 5%.

5. Explain why a 1% monthly rate should not be paired with n=5 years without conversion.

6. Determine whether $1,000 now and $1,338.23 in 5 years are equivalent at 6%.

7. A cost of $4,000 occurs at year 2. Express its value at year 6 at 7%.

8. State the factor notation that converts future F to present P.

9. Explain what economic equivalence means.

10. List the five timeline checks you should make before calculation.


---

## Practice Problem Solutions

1. $F=5000(1.06)^4=\boxed{6,312.38}$.

2. $P=10000/(1.08)^5=\boxed{6,805.83}$.

3. $i_e=(1+0.12/12)^{12}-1=\boxed{12.683\%}$.

4. $P=2000/1.05+3000/1.05^3=\boxed{4,496.27}$.

5. The interest period and n-period must match; convert both to monthly or both to annual basis.

6. $1000(1.06)^5=1,338.23$, so the stated future amount is essentially equivalent apart from rounding.

7. Move four periods forward: $F=4000(1.07)^4=\boxed{5,243.18}$ cost magnitude.

8. $(P/F,i,n)$.

9. Different cash-flow patterns are economically equivalent when they have equal value at a common date for the stated interest rate.

10. Viewpoint/signs; time zero; cash-flow timing; rate period; number of periods/common comparison date.


---

## Quick Reference

**Handbook anchor:** Engineering Economics / Factors and Non-Annual Compounding, printed p. 235–236.

- **Cash flows:** cash-flow diagram
- **Interest:** compound interest
- **Equivalence:** economic equivalence
- **Effective rate:** nominal annual rate
- **Factors:** engineering-economy factor notation
- **Irregular series:** irregular cash-flow series
- **Checks:** interest-period consistency

---

## What's Next

**02-05 — Present Worth and Future Worth**

Carry forward the rule: identify the engineering question first, then select the professional or economic tool that answers that question.

— Your Mentor
