---
chapter: "03-62"
title: "Data, Logic, Databases, and Engineering Analytics"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-062-01, IND-3-062-02, IND-3-062-03, IND-3-062-04, IND-3-062-05, IND-3-062-06, IND-3-062-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-62: Data, Logic, Databases, and Engineering Analytics

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-047-07 · MATH-1D-033-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Data, Logic, Databases, and Engineering Analytics** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **62.1** Explain and apply **Engineering Data Types, Units, and Data Quality**.
* **62.2** Explain and apply **Relational Databases, Keys, and Engineering Records**.
* **62.3** Explain and apply **Flowcharts, Algorithms, and Decision Logic**.
* **62.4** Explain and apply **Descriptive Analytics and KPI Construction**.
* **62.5** Explain and apply **Exploratory Data Analysis and Visualization**.
* **62.6** Explain and apply **Predictive and Prescriptive Analytics**.
* **62.7** Explain and apply **Analytics Validation and Reproducibility**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 62.1 Engineering Data Types, Units, and Data Quality

Industrial analytics begins by defining data types, units, timestamps, and quality rules. Mixing bases or units can invalidate downstream calculations.

\\[\\text{usable data}=\\text{valid}+\\text{complete}+\\text{consistent}+\\text{traceable}\\]

![FIG-03-62-001: Textbook-quality industrial engineering diagram illustrating engineering data types, units, and data quality with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-62-001-engineering-data-types-units-and-data-quality.png)

### Worked Example 1

**Problem.** Cycle times stored partly in seconds and partly in minutes must be normalized before comparison.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 62.2 Relational Databases, Keys, and Engineering Records

Relational databases organize entities into tables linked by keys. Good schema design reduces duplication and preserves traceability.

\\[\\text{primary key}\\rightarrow\\text{unique row identity}\\]

![FIG-03-62-002: Textbook-quality industrial engineering diagram illustrating relational databases, keys, and engineering records with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-62-002-relational-databases-keys-and-engineering-records.png)

### Worked Example 2

**Problem.** A work-order record can reference MachineID instead of repeating every machine attribute.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 62.3 Flowcharts, Algorithms, and Decision Logic

Flowcharts and pseudocode make engineering logic auditable and reproducible.

\\[\\text{input}\\rightarrow\\text{logic}\\rightarrow\\text{output}\\]

![FIG-03-62-003: Textbook-quality industrial engineering diagram illustrating flowcharts, algorithms, and decision logic with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-62-003-flowcharts-algorithms-and-decision-logic.png)

### Worked Example 3

**Problem.** A defect-screening algorithm should explicitly define the threshold and missing-data rule.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 62.4 Descriptive Analytics and KPI Construction

A KPI requires a defined numerator, denominator, time window, and inclusion rule.

\\[\\mathrm{KPI}=\\frac{\\text{defined performance quantity}}{\\text{defined basis}}\\]

![FIG-03-62-004: Textbook-quality industrial engineering diagram illustrating descriptive analytics and kpi construction with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-62-004-descriptive-analytics-and-kpi-construction.png)

### Worked Example 4

**Problem.** 950 good units from 1000 starts gives 95% first-pass yield.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 62.5 Exploratory Data Analysis and Visualization

Exploratory analysis looks for distributions, trends, outliers, stratification, and relationships before formal modeling.

\\[z=\\frac{x-\\bar x}{s}\\]

![FIG-03-62-005: Textbook-quality industrial engineering diagram illustrating exploratory data analysis and visualization with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-62-005-exploratory-data-analysis-and-visualization.png)

### Worked Example 5

**Problem.** A boxplot by machine can reveal a shift hidden by the plant-wide average.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 62.6 Predictive and Prescriptive Analytics

Predictive analytics estimates likely outcomes; prescriptive analytics selects actions under objectives and constraints.

\\[\\text{prediction estimates outcome; optimization recommends action}\\]

![FIG-03-62-006: Textbook-quality industrial engineering diagram illustrating predictive and prescriptive analytics with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-62-006-predictive-and-prescriptive-analytics.png)

### Worked Example 6

**Problem.** A demand forecast predicts demand; a production plan decides what to make.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 62.7 Analytics Validation and Reproducibility

Industrial analytics should be reproducible, versioned, and validated against the decision being supported.

\\[\\text{question}\\rightarrow\\text{data}\\rightarrow\\text{model}\\rightarrow\\text{validation}\\rightarrow\\text{decision}\\]

![FIG-03-62-007: Textbook-quality industrial engineering diagram illustrating analytics validation and reproducibility with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-62-007-analytics-validation-and-reproducibility.png)

### Worked Example 7

**Problem.** A model that fits historical data but fails on new periods should not be deployed uncritically.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** No. Add the missing operational restriction and re-solve. Mathematical feasibility applies only to the stated model.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** Use the Handbook expression and definitions unless the problem explicitly provides another model.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 6; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

Specification-required management/design topics that are not directly tabulated are identified as learned or guide-developed rather than assigned false Handbook pages.

---

## Where This Goes Wrong

**Using industrial data quality without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial relational database without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial analytics algorithm without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial KPI without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial exploratory data analysis without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using predictive-prescriptive analytics without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using analytics workflow validation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| industrial data quality | Industrial/systems concept developed in §62.1; apply with the stated model assumptions and decision basis. |
| industrial relational database | Industrial/systems concept developed in §62.2; apply with the stated model assumptions and decision basis. |
| industrial analytics algorithm | Industrial/systems concept developed in §62.3; apply with the stated model assumptions and decision basis. |
| industrial KPI | Industrial/systems concept developed in §62.4; apply with the stated model assumptions and decision basis. |
| industrial exploratory data analysis | Industrial/systems concept developed in §62.5; apply with the stated model assumptions and decision basis. |
| predictive-prescriptive analytics | Industrial/systems concept developed in §62.6; apply with the stated model assumptions and decision basis. |
| analytics workflow validation | Industrial/systems concept developed in §62.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **industrial data quality** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **industrial relational database** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **industrial analytics algorithm** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **industrial KPI** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **industrial exploratory data analysis** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **predictive-prescriptive analytics** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **analytics workflow validation** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial data quality**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial relational database**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial analytics algorithm**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial KPI**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial exploratory data analysis**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **predictive-prescriptive analytics**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **analytics workflow validation**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **industrial data quality**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **industrial relational database**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **industrial analytics algorithm**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **industrial KPI**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **industrial exploratory data analysis**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **predictive-prescriptive analytics**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **analytics workflow validation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **industrial data quality**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **industrial relational database**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **industrial data quality** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **industrial relational database** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **industrial analytics algorithm** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **industrial KPI** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **industrial exploratory data analysis** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **predictive-prescriptive analytics** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **analytics workflow validation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **industrial data quality**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **industrial relational database**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **industrial analytics algorithm**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **industrial KPI**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **industrial exploratory data analysis**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **predictive-prescriptive analytics**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **analytics workflow validation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

15. The boundary and objective determine what counts as performance and which constraints matter.

16. Optimization and statistics answer questions inside a model; implementation, causality, and stakeholder objectives still require engineering judgment.

17. The FE Handbook is the supplied reference and its definitions should govern unless the problem explicitly supplies another model.

18. Check feasibility, units, scale, probability bounds, and upstream/downstream effects.

19. **A.** The method depends on assumptions, units, data basis, and decision context.

20. **A.** The method depends on assumptions, units, data basis, and decision context.

21. **A.** The method depends on assumptions, units, data basis, and decision context.

22. **A.** The method depends on assumptions, units, data basis, and decision context.

23. **A.** The method depends on assumptions, units, data basis, and decision context.

24. **A.** The method depends on assumptions, units, data basis, and decision context.

25. **A.** The method depends on assumptions, units, data basis, and decision context.

26. **A.** The method depends on assumptions, units, data basis, and decision context.

27. **A.** The method depends on assumptions, units, data basis, and decision context.


---

## Practice Problems

1. Cycle times stored partly in seconds and partly in minutes must be normalized before comparison.

2. A work-order record can reference MachineID instead of repeating every machine attribute.

3. A defect-screening algorithm should explicitly define the threshold and missing-data rule.

4. 950 good units from 1000 starts gives 95% first-pass yield.

5. A boxplot by machine can reveal a shift hidden by the plant-wide average.

6. A demand forecast predicts demand; a production plan decides what to make.

7. A model that fits historical data but fails on new periods should not be deployed uncritically.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §62.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §62.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §62.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §62.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §62.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §62.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §62.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 6, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 6.

- **industrial data quality:** Engineering Data Types, Units, and Data Quality
- **industrial relational database:** Relational Databases, Keys, and Engineering Records
- **industrial analytics algorithm:** Flowcharts, Algorithms, and Decision Logic
- **industrial KPI:** Descriptive Analytics and KPI Construction
- **industrial exploratory data analysis:** Exploratory Data Analysis and Visualization
- **predictive-prescriptive analytics:** Predictive and Prescriptive Analytics
- **analytics workflow validation:** Analytics Validation and Reproducibility

---

## What's Next

**Chapter 03-63: Linear Programming and Optimization**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
