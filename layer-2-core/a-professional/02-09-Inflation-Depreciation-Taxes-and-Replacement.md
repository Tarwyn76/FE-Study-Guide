---
chapter: "02-09"
title: "Inflation, Depreciation, Taxes, and Replacement"
layer: 2
tier: A
template: technical
ledger_ids: [ECON-2A-009-01, ECON-2A-009-02, ECON-2A-009-03, ECON-2A-009-04, ECON-2A-009-05, ECON-2A-009-06, ECON-2A-009-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-09: Inflation, Depreciation, Taxes, and Replacement

> *"Professional engineering decisions are strongest when the governing duty, assumption, and economic model are all made explicit."*

---

## Before You Start

**Prerequisites:** 02-08

**Skip if:** You can correctly apply every section objective below, including the scenario and calculation checks, without relying on memorized wording alone.

**Time:** About 75–105 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

Engineering decisions often cross many years. Inflation changes purchasing power, depreciation allocates asset cost for accounting and tax purposes, taxes change after-tax cash flow, and replacement decisions compare keeping an existing asset with acquiring another. The Handbook supplies the core inflation, straight-line depreciation, MACRS, book-value, and tax definitions.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **09.1** Explain and apply **Inflation and Dollar Basis**.
* **09.2** Explain and apply **Non-Annual Compounding Review**.
* **09.3** Explain and apply **Straight-Line Depreciation**.
* **09.4** Explain and apply **MACRS Depreciation**.
* **09.5** Explain and apply **Book Value**.
* **09.6** Explain and apply **Taxable Income and After-Tax Cash Flow**.
* **09.7** Explain and apply **Replacement and Capitalized Cost**.

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

## 09.1 Inflation and Dollar Basis

The Handbook gives an inflation-adjusted relationship using interest i and general inflation f. In standard real/market-rate notation, consistency of dollar basis matters more than labels: do not discount constant-dollar cash flows with a market rate that includes inflation unless the model is adjusted consistently.

State whether cash flows include expected inflation.

![FIG-02-09-001: Current/nominal-dollar cash-flow path versus constant/real-dollar path, each paired with a consistent discount rate.](../figures/FIG-02-09-001-inflation-and-dollar-basis.png)

### Worked Example 1 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Inflation**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 09.2 Non-Annual Compounding Review

If nominal annual rate r is compounded m times per year, the effective annual rate is

$$i_e=\left(1+\frac{r}{m}\right)^m-1.$$

Inflation and financing may each be quoted on different bases. Convert rates before combining or comparing them.

![FIG-02-09-002: Rate-basis conversion diagram showing nominal rate r, periodic r/m, and effective annual i_e.](../figures/FIG-02-09-002-non-annual-compounding-review.png)

### Worked Example 2 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Compounding**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 09.3 Straight-Line Depreciation

The Handbook straight-line relation is

$$D_j=\frac{C-S_n}{n},$$

where C is initial cost, $S_n$ is expected salvage value, and n is depreciable life.

The same depreciation amount is assigned each year.

![FIG-02-09-003: Book value declining linearly from initial cost C to salvage S_n over n years.](../figures/FIG-02-09-003-straight-line-depreciation.png)

### Worked Example 3 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **SL depreciation**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 09.4 MACRS Depreciation

For MACRS, the Handbook gives

$$D_j=(\text{factor})C$$

and provides recovery-rate tables for common recovery periods.

MACRS factors are applied to the depreciable basis specified by the problem; do not substitute straight-line logic into a MACRS problem.

![FIG-02-09-004: MACRS annual depreciation bars for a representative recovery period, showing front-loaded factors.](../figures/FIG-02-09-004-macrs-depreciation.png)

### Worked Example 4 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **MACRS**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 09.5 Book Value

The Handbook defines book value as initial cost minus accumulated depreciation:

$$BV_j=C-\sum_{k=1}^{j}D_k.$$

Book value is an accounting value. It need not equal market value.

![FIG-02-09-005: Book value versus time with a separate market-value curve to show they need not coincide.](../figures/FIG-02-09-005-book-value.png)

### Worked Example 5 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Book value**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 09.6 Taxable Income and After-Tax Cash Flow

The Handbook states that taxable income is total income less depreciation and ordinary expenses; capital items are depreciated rather than immediately treated as ordinary expenses.

A simplified tax model is

$$Tax=t(\text{taxable income}),$$

when taxable income is positive and the problem specifies tax rate t.

Follow the problem statement for treatment of losses, salvage, and gains.

![FIG-02-09-006: Revenue -> subtract ordinary expenses -> subtract depreciation -> taxable income -> tax -> after-tax project cash flow.](../figures/FIG-02-09-006-taxable-income-and-after-tax-cash-flow.png)

### Worked Example 6 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Taxes**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 09.7 Replacement and Capitalized Cost

Replacement decisions compare the economic consequences of keeping an existing asset with replacing it. Relevant cash flows include current market value/opportunity cost, operating and maintenance costs, salvage, and replacement cost.

For perpetual uniform annual amount A, the Handbook gives capitalized cost

$$P=\frac{A}{i}.$$

Do not use sunk historical cost as though it were a future cash flow.

![FIG-02-09-007: Defender-versus-challenger comparison showing current market value, future O&M, replacement cost, and salvage; inset shows perpetual A converted to capitalized P=A/i.](../figures/FIG-02-09-007-replacement-and-capitalized-cost.png)

### Worked Example 7 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Replacement**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. The principal Handbook basis for this chapter is **Engineering Economics / Inflation, Depreciation, Taxation, and Capitalized Costs**, printed p. **236–237**. Where the chapter adds interpretation, decision workflow, contract/liability context, or derived relationships not printed explicitly in that section, those additions are guide-developed and should not be mistaken for quoted Handbook language.

---

## Where This Goes Wrong

**Treating Inflation as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Compounding as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating SL depreciation as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating MACRS as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Book value as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Taxes as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Replacement as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Skipping the governing facts.** Professional and economic rules are conditional on the actual scenario, timing, jurisdiction, or cash-flow structure.

---

## Key Terms

| Term | Working definition |
|---|---|
| inflation | Concept developed in this chapter; use the controlling section definition and conditions. |
| constant-dollar cash flow | Concept developed in this chapter; use the controlling section definition and conditions. |
| effective annual rate | Concept developed in this chapter; use the controlling section definition and conditions. |
| straight-line depreciation | Concept developed in this chapter; use the controlling section definition and conditions. |
| MACRS depreciation | Concept developed in this chapter; use the controlling section definition and conditions. |
| book value | Concept developed in this chapter; use the controlling section definition and conditions. |
| taxable income | Concept developed in this chapter; use the controlling section definition and conditions. |
| after-tax cash flow | Concept developed in this chapter; use the controlling section definition and conditions. |
| replacement analysis | Concept developed in this chapter; use the controlling section definition and conditions. |
| capitalized cost | Concept developed in this chapter; use the controlling section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. State the central engineering decision or principle developed in **Inflation and Dollar Basis**.

2. State the central engineering decision or principle developed in **Non-Annual Compounding Review**.

3. State the central engineering decision or principle developed in **Straight-Line Depreciation**.

4. State the central engineering decision or principle developed in **MACRS Depreciation**.

5. State the central engineering decision or principle developed in **Book Value**.

6. State the central engineering decision or principle developed in **Taxable Income and After-Tax Cash Flow**.

7. State the central engineering decision or principle developed in **Replacement and Capitalized Cost**.

8. What common error would result from ignoring the distinction emphasized in **Inflation and Dollar Basis**?

9. What common error would result from ignoring the distinction emphasized in **Non-Annual Compounding Review**?

10. What common error would result from ignoring the distinction emphasized in **Straight-Line Depreciation**?

11. What common error would result from ignoring the distinction emphasized in **MACRS Depreciation**?

12. What common error would result from ignoring the distinction emphasized in **Book Value**?

13. What common error would result from ignoring the distinction emphasized in **Taxable Income and After-Tax Cash Flow**?

14. What common error would result from ignoring the distinction emphasized in **Replacement and Capitalized Cost**?

15. Identify the first fact you would verify before solving a problem from this chapter.

16. Explain why a correct formula or rule can still produce a wrong engineering decision.

17. Describe one reason documentation or an explicit timeline improves the analysis.

18. State one check you would perform before accepting a final answer.

### Multiple Choice

19. Which choice best matches the chapter's use of **Inflation**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

20. Which choice best matches the chapter's use of **Compounding**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

21. Which choice best matches the chapter's use of **SL depreciation**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

22. Which choice best matches the chapter's use of **MACRS**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

23. Which choice best matches the chapter's use of **Book value**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

24. Which choice best matches the chapter's use of **Taxes**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

25. Which choice best matches the chapter's use of **Replacement**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

26. Which choice best matches the chapter's use of **Inflation**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

27. Which choice best matches the chapter's use of **Compounding**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment


---

## Answer Key with Explanations

1. The central principle is **Inflation**. Apply that section's rule to the governing facts and assumptions.

2. The central principle is **Compounding**. Apply that section's rule to the governing facts and assumptions.

3. The central principle is **SL depreciation**. Apply that section's rule to the governing facts and assumptions.

4. The central principle is **MACRS**. Apply that section's rule to the governing facts and assumptions.

5. The central principle is **Book value**. Apply that section's rule to the governing facts and assumptions.

6. The central principle is **Taxes**. Apply that section's rule to the governing facts and assumptions.

7. The central principle is **Replacement**. Apply that section's rule to the governing facts and assumptions.

8. It would apply the wrong professional or economic rule. First distinguish **Inflation** from nearby concepts, then apply it under the section's stated conditions.

9. It would apply the wrong professional or economic rule. First distinguish **Compounding** from nearby concepts, then apply it under the section's stated conditions.

10. It would apply the wrong professional or economic rule. First distinguish **SL depreciation** from nearby concepts, then apply it under the section's stated conditions.

11. It would apply the wrong professional or economic rule. First distinguish **MACRS** from nearby concepts, then apply it under the section's stated conditions.

12. It would apply the wrong professional or economic rule. First distinguish **Book value** from nearby concepts, then apply it under the section's stated conditions.

13. It would apply the wrong professional or economic rule. First distinguish **Taxes** from nearby concepts, then apply it under the section's stated conditions.

14. It would apply the wrong professional or economic rule. First distinguish **Replacement** from nearby concepts, then apply it under the section's stated conditions.

15. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

16. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

17. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

18. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

19. **A.** The chapter uses **Inflation** as the section-specific engineering concept or criterion.

20. **A.** The chapter uses **Compounding** as the section-specific engineering concept or criterion.

21. **A.** The chapter uses **SL depreciation** as the section-specific engineering concept or criterion.

22. **A.** The chapter uses **MACRS** as the section-specific engineering concept or criterion.

23. **A.** The chapter uses **Book value** as the section-specific engineering concept or criterion.

24. **A.** The chapter uses **Taxes** as the section-specific engineering concept or criterion.

25. **A.** The chapter uses **Replacement** as the section-specific engineering concept or criterion.

26. **A.** The chapter uses **Inflation** as the section-specific engineering concept or criterion.

27. **A.** The chapter uses **Compounding** as the section-specific engineering concept or criterion.


---

## Practice Problems

1. Asset cost C=$50,000, salvage=$5,000, life=5 years. Find annual straight-line depreciation.

2. For Problem 1, find book value after 3 years.

3. MACRS factor is 0.32 on a $40,000 basis. Find depreciation for that year.

4. Revenue is $100,000, ordinary expense $55,000, depreciation $15,000. Find taxable income.

5. If tax rate is 25% for Problem 4, find tax.

6. Nominal 9% compounded monthly: find effective annual rate.

7. Explain why book value need not equal market value.

8. Explain why historical purchase price of an existing asset is usually a sunk cost in a replacement decision.

9. Find capitalized present worth of perpetual annual cost $12,000 at 6%.

10. State the consistency rule for inflated versus constant-dollar cash flows.


---

## Practice Problem Solutions

1. $D=(50000-5000)/5=\boxed{9,000}$ per year.

2. $BV=50000-3(9000)=\boxed{23,000}$.

3. $D=0.32(40000)=\boxed{12,800}$.

4. Taxable income $=100000-55000-15000=\boxed{30,000}$.

5. Tax $=0.25(30000)=\boxed{7,500}$.

6. $i_e=(1+0.09/12)^{12}-1=\boxed{9.381\%}$.

7. Book value is accounting basis less accumulated depreciation; market value is what the asset can actually command in the market.

8. The historical outlay cannot be changed by the current decision; relevant comparison uses future/opportunity cash flows such as current market value and future costs.

9. $P=A/i=12000/0.06=\boxed{200,000}$.

10. Use cash flows and discount rates on a consistent inflation basis; do not mix real/constant-dollar cash flows with an incompatible market rate.


---

## Quick Reference

**Handbook anchor:** Engineering Economics / Inflation, Depreciation, Taxation, and Capitalized Costs, printed p. 236–237.

- **Inflation:** inflation
- **Compounding:** effective annual rate
- **SL depreciation:** straight-line depreciation
- **MACRS:** MACRS depreciation
- **Book value:** book value
- **Taxes:** taxable income
- **Replacement:** replacement analysis

---

## What's Next

**02-10 — Economic Decision-Making, Project Selection, and Risk**

Carry forward the rule: identify the engineering question first, then select the professional or economic tool that answers that question.

— Your Mentor
