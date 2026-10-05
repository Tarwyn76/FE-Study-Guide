---
chapter: "02-10"
title: "Economic Decision-Making, Project Selection, and Risk"
layer: 2
tier: A
template: technical
ledger_ids: [ECON-2A-010-01, ECON-2A-010-02, ECON-2A-010-03, ECON-2A-010-04, ECON-2A-010-05, ECON-2A-010-06, ECON-2A-010-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-10: Economic Decision-Making, Project Selection, and Risk

> *"Professional engineering decisions are strongest when the governing duty, assumption, and economic model are all made explicit."*

---

## Before You Start

**Prerequisites:** 02-09 · 01-37

**Skip if:** You can correctly apply every section objective below, including the scenario and calculation checks, without relying on memorized wording alone.

**Time:** About 75–105 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

The last Tier 2A chapter integrates equivalence, MARR, uncertainty, and project selection. The Handbook gives decision-tree symbols and expected-value structure. The engineering task is to combine economic criteria with risk, unequal lives, constraints, and non-economic requirements without pretending that one number answers every decision.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **10.1** Explain and apply **Mutually Exclusive and Independent Projects**.
* **10.2** Explain and apply **Common Study Period and Unequal Lives**.
* **10.3** Explain and apply **Economic Decision Trees**.
* **10.4** Explain and apply **Expected Monetary Value**.
* **10.5** Explain and apply **Project Selection Under a Budget**.
* **10.6** Explain and apply **Sensitivity and Scenario Analysis**.
* **10.7** Explain and apply **Integrated Decision Rule**.

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

## 10.1 Mutually Exclusive and Independent Projects

Independent projects can be accepted or rejected separately subject to resources and constraints. Mutually exclusive alternatives compete for the same need; selecting one excludes the others.

This distinction determines whether you compare each project to a minimum criterion or compare alternatives directly.

![FIG-02-10-001: Independent project set with separate accept/reject branches versus mutually exclusive alternatives feeding one selection node.](../figures/FIG-02-10-001-mutually-exclusive-and-independent-projects.png)

### Worked Example 1 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Project type**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 10.2 Common Study Period and Unequal Lives

Alternatives with unequal lives require a consistent comparison framework. Depending on assumptions, methods include repeatability to a common multiple, coterminated study period, or equivalent annual worth.

Do not silently compare five years of one alternative with ten years of another as though the service provided were identical.

![FIG-02-10-002: Two unequal-life alternatives extended or annualized to a common study basis.](../figures/FIG-02-10-002-common-study-period-and-unequal-lives.png)

### Worked Example 2 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Unequal lives**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 10.3 Economic Decision Trees

The Handbook distinguishes decision nodes, chance nodes, and outcome nodes. Decision nodes represent choices controlled by the decision maker. Chance nodes represent uncertain events with stated probabilities.

Expected value at a chance node is

$$EV=\sum p_i C_i.$$

Work backward from outcomes through chance nodes to decision nodes.

![FIG-02-10-003: Economic decision tree with square decision node, circular chance nodes, probabilities, payoff outcomes, and backward-induction EV labels.](../figures/FIG-02-10-003-economic-decision-trees.png)

### Worked Example 3 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Decision trees**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 10.4 Expected Monetary Value

Expected monetary value summarizes repeated probabilistic outcomes into a probability-weighted average. It is useful when the objective is expected economic performance and probabilities are credible.

It does not measure worst-case consequence, variance, or risk tolerance. Chapter 01-37 developed those distinctions; this section applies them to engineering economics.

![FIG-02-10-004: Two alternatives with equal expected monetary value but different outcome distributions to show that EV alone does not capture risk.](../figures/FIG-02-10-004-expected-monetary-value.png)

### Worked Example 4 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **EMV**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 10.5 Project Selection Under a Budget

When capital is limited, the decision becomes constrained selection rather than independent accept/reject screening. A project that is economically attractive alone can be excluded because another portfolio creates more value within the budget.

For small exam problems, compare feasible combinations explicitly.

![FIG-02-10-005: Project-selection table listing cost, PW/annual worth, and feasible portfolios under a fixed capital budget.](../figures/FIG-02-10-005-project-selection-under-a-budget.png)

### Worked Example 5 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Capital rationing**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 10.6 Sensitivity and Scenario Analysis

Sensitivity analysis varies one uncertain input to find how the decision changes. Scenario analysis changes a coherent set of inputs together.

Identify breakpoints where the preferred alternative switches. These thresholds often communicate more than a single best-estimate answer.

![FIG-02-10-006: Two alternative PW lines versus an uncertain variable crossing at a decision breakpoint; low/base/high scenarios marked.](../figures/FIG-02-10-006-sensitivity-and-scenario-analysis.png)

### Worked Example 6 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Sensitivity**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## 10.7 Integrated Decision Rule

A disciplined project-selection sequence is:

1. verify technical feasibility and mandatory safety/legal constraints;
2. define alternatives and study period;
3. construct consistent cash flows;
4. select the economic criterion and MARR;
5. incorporate uncertainty and risk where material;
6. compare feasible alternatives;
7. document assumptions and decision rationale.

Economic attractiveness never overrides a mandatory safety, ethical, or legal requirement.

![FIG-02-10-007: Integrated project-selection workflow beginning with safety/legal feasibility gate, then cash-flow modeling, equivalence analysis, risk/sensitivity, alternative comparison, and documented decision.](../figures/FIG-02-10-007-integrated-decision-rule.png)

### Worked Example 7 — Read the Model Before Calculating

Identify the cash-flow pattern, comparison date, rate basis, and sign convention. Then apply **Integration**. A numerical result is valid only when every cash flow has been placed on the same economic basis.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. The principal Handbook basis for this chapter is **Engineering Economics / Economic Decision Trees and Project Comparison**, printed p. **236–237**. Where the chapter adds interpretation, decision workflow, contract/liability context, or derived relationships not printed explicitly in that section, those additions are guide-developed and should not be mistaken for quoted Handbook language.

---

## Where This Goes Wrong

**Treating Project type as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Unequal lives as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Decision trees as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating EMV as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Capital rationing as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Sensitivity as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Treating Integration as a label instead of a decision rule.** Identify the assumptions and authority that make it applicable.

**Skipping the governing facts.** Professional and economic rules are conditional on the actual scenario, timing, jurisdiction, or cash-flow structure.

---

## Key Terms

| Term | Working definition |
|---|---|
| mutually exclusive alternatives | Concept developed in this chapter; use the controlling section definition and conditions. |
| independent projects | Concept developed in this chapter; use the controlling section definition and conditions. |
| common study period | Concept developed in this chapter; use the controlling section definition and conditions. |
| decision node | Concept developed in this chapter; use the controlling section definition and conditions. |
| chance node | Concept developed in this chapter; use the controlling section definition and conditions. |
| outcome node | Concept developed in this chapter; use the controlling section definition and conditions. |
| expected monetary value | Concept developed in this chapter; use the controlling section definition and conditions. |
| capital rationing | Concept developed in this chapter; use the controlling section definition and conditions. |
| scenario analysis | Concept developed in this chapter; use the controlling section definition and conditions. |
| decision breakpoint | Concept developed in this chapter; use the controlling section definition and conditions. |
| integrated engineering-economic decision | Concept developed in this chapter; use the controlling section definition and conditions. |

---

## Review Questions

### Conceptual and Applied

1. State the central engineering decision or principle developed in **Mutually Exclusive and Independent Projects**.

2. State the central engineering decision or principle developed in **Common Study Period and Unequal Lives**.

3. State the central engineering decision or principle developed in **Economic Decision Trees**.

4. State the central engineering decision or principle developed in **Expected Monetary Value**.

5. State the central engineering decision or principle developed in **Project Selection Under a Budget**.

6. State the central engineering decision or principle developed in **Sensitivity and Scenario Analysis**.

7. State the central engineering decision or principle developed in **Integrated Decision Rule**.

8. What common error would result from ignoring the distinction emphasized in **Mutually Exclusive and Independent Projects**?

9. What common error would result from ignoring the distinction emphasized in **Common Study Period and Unequal Lives**?

10. What common error would result from ignoring the distinction emphasized in **Economic Decision Trees**?

11. What common error would result from ignoring the distinction emphasized in **Expected Monetary Value**?

12. What common error would result from ignoring the distinction emphasized in **Project Selection Under a Budget**?

13. What common error would result from ignoring the distinction emphasized in **Sensitivity and Scenario Analysis**?

14. What common error would result from ignoring the distinction emphasized in **Integrated Decision Rule**?

15. Identify the first fact you would verify before solving a problem from this chapter.

16. Explain why a correct formula or rule can still produce a wrong engineering decision.

17. Describe one reason documentation or an explicit timeline improves the analysis.

18. State one check you would perform before accepting a final answer.

### Multiple Choice

19. Which choice best matches the chapter's use of **Project type**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

20. Which choice best matches the chapter's use of **Unequal lives**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

21. Which choice best matches the chapter's use of **Decision trees**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

22. Which choice best matches the chapter's use of **EMV**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

23. Which choice best matches the chapter's use of **Capital rationing**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

24. Which choice best matches the chapter's use of **Sensitivity**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

25. Which choice best matches the chapter's use of **Integration**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

26. Which choice best matches the chapter's use of **Project type**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment

27. Which choice best matches the chapter's use of **Unequal lives**?
A) The section-specific engineering concept or criterion
B) An unrelated calculation method
C) A guaranteed outcome
D) A substitute for engineering judgment


---

## Answer Key with Explanations

1. The central principle is **Project type**. Apply that section's rule to the governing facts and assumptions.

2. The central principle is **Unequal lives**. Apply that section's rule to the governing facts and assumptions.

3. The central principle is **Decision trees**. Apply that section's rule to the governing facts and assumptions.

4. The central principle is **EMV**. Apply that section's rule to the governing facts and assumptions.

5. The central principle is **Capital rationing**. Apply that section's rule to the governing facts and assumptions.

6. The central principle is **Sensitivity**. Apply that section's rule to the governing facts and assumptions.

7. The central principle is **Integration**. Apply that section's rule to the governing facts and assumptions.

8. It would apply the wrong professional or economic rule. First distinguish **Project type** from nearby concepts, then apply it under the section's stated conditions.

9. It would apply the wrong professional or economic rule. First distinguish **Unequal lives** from nearby concepts, then apply it under the section's stated conditions.

10. It would apply the wrong professional or economic rule. First distinguish **Decision trees** from nearby concepts, then apply it under the section's stated conditions.

11. It would apply the wrong professional or economic rule. First distinguish **EMV** from nearby concepts, then apply it under the section's stated conditions.

12. It would apply the wrong professional or economic rule. First distinguish **Capital rationing** from nearby concepts, then apply it under the section's stated conditions.

13. It would apply the wrong professional or economic rule. First distinguish **Sensitivity** from nearby concepts, then apply it under the section's stated conditions.

14. It would apply the wrong professional or economic rule. First distinguish **Integration** from nearby concepts, then apply it under the section's stated conditions.

15. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

16. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

17. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

18. Verify the governing assumptions, authority, timing, units, or factual basis first; then confirm the selected rule answers the actual engineering question.

19. **A.** The chapter uses **Project type** as the section-specific engineering concept or criterion.

20. **A.** The chapter uses **Unequal lives** as the section-specific engineering concept or criterion.

21. **A.** The chapter uses **Decision trees** as the section-specific engineering concept or criterion.

22. **A.** The chapter uses **EMV** as the section-specific engineering concept or criterion.

23. **A.** The chapter uses **Capital rationing** as the section-specific engineering concept or criterion.

24. **A.** The chapter uses **Sensitivity** as the section-specific engineering concept or criterion.

25. **A.** The chapter uses **Integration** as the section-specific engineering concept or criterion.

26. **A.** The chapter uses **Project type** as the section-specific engineering concept or criterion.

27. **A.** The chapter uses **Unequal lives** as the section-specific engineering concept or criterion.


---

## Practice Problems

1. A chance node has outcomes $100k with p=.4 and $20k with p=.6. Find EV.

2. Alternative A has EV=$60k; B has EV=$55k. If objective is expected monetary value only, which ranks higher?

3. Explain why equal EV does not imply equal risk.

4. Two alternatives have 4-year and 6-year lives. What issue must be resolved before direct PW comparison?

5. Define mutually exclusive alternatives.

6. Define independent projects.

7. A $100k capital budget allows projects X ($60k, PW benefit $20k), Y ($50k, $18k), Z ($40k, $14k). Which two-project feasible portfolio has highest total PW benefit?

8. What is a decision breakpoint?

9. Why must mandatory safety/legal constraints be checked before economic ranking?

10. Describe backward evaluation of a decision tree.


---

## Practice Problem Solutions

1. $EV=0.4(100)+0.6(20)=\boxed{52}$ thousand dollars.

2. A, if expected monetary value is the sole stated criterion and both are otherwise feasible.

3. EV is an average; distributions can differ in spread, downside, and tail consequence.

4. Establish a common study-period or annual-worth/repeatability framework consistent with the service assumptions.

5. Choosing one excludes the others because they satisfy the same need or compete for the same decision.

6. They can be accepted or rejected separately, subject to resource constraints.

7. X+Z costs $100k and gives $34k; Y+Z costs $90k and gives $32k; X+Y is infeasible. Choose $\boxed{X+Z}$.

8. The input value at which the preferred alternative changes.

9. Economic attractiveness cannot authorize an unsafe, unethical, or illegal alternative.

10. Compute expected values at chance nodes from outcomes, then compare available branch values at decision nodes moving backward toward the root.


---

## Quick Reference

**Handbook anchor:** Engineering Economics / Economic Decision Trees and Project Comparison, printed p. 236–237.

- **Project type:** mutually exclusive alternatives
- **Unequal lives:** common study period
- **Decision trees:** decision node
- **EMV:** expected monetary value
- **Capital rationing:** capital rationing
- **Sensitivity:** scenario analysis
- **Integration:** integrated engineering-economic decision

---

## What's Next

**02-11 — Atomic Structure, Bonding, and the Periodic Table**

Carry forward the rule: identify the engineering question first, then select the professional or economic tool that answers that question.

— Your Mentor
