---
chapter: "03-66"
title: "Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-066-01, IND-3-066-02, IND-3-066-03, IND-3-066-04, IND-3-066-05, IND-3-066-06, IND-3-066-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-66: Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** ECON-2A-005-06 · CIV-3-030-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **66.1** Explain and apply **Organization, Responsibility, and Motivation**.
* **66.2** Explain and apply **Work Breakdown Structures**.
* **66.3** Explain and apply **Critical Path Method**.
* **66.4** Explain and apply **PERT Duration and Uncertainty**.
* **66.5** Explain and apply **Earned Value Management**.
* **66.6** Explain and apply **Agile Project Management**.
* **66.7** Explain and apply **KPIs and Balanced Scorecards**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 66.1 Organization, Responsibility, and Motivation

Functional, projectized, and matrix organizations distribute authority differently.

\\[\\text{strategy}\\rightarrow\\text{structure}\\rightarrow\\text{responsibility}\\]

![FIG-03-66-001: Textbook-quality industrial engineering diagram illustrating organization, responsibility, and motivation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-001-organization-responsibility-and-motivation.png)

### Worked Example 1

**Problem.** In a matrix, a project manager can share authority with functional managers.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 66.2 Work Breakdown Structures

A WBS decomposes project scope into manageable deliverables and work packages.

\\[\\text{scope}\\rightarrow\\text{deliverables}\\rightarrow\\text{work packages}\\]

![FIG-03-66-002: Textbook-quality industrial engineering diagram illustrating work breakdown structures with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-002-work-breakdown-structures.png)

### Worked Example 2

**Problem.** Design, procurement, installation, and commissioning can be separate deliverables.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 66.3 Critical Path Method

CPM identifies the longest path through a deterministic activity network.

\\[T=\\sum_{(i,j)\\in CP}d_{ij}\\]

![FIG-03-66-003: Textbook-quality industrial engineering diagram illustrating critical path method with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-003-critical-path-method.png)

### Worked Example 3

**Problem.** Zero-total-float activities lie on at least one critical path.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 66.4 PERT Duration and Uncertainty

PERT uses optimistic, most-likely, and pessimistic estimates to approximate activity uncertainty.

\\[\\mu=\\frac{a+4m+b}{6},\\quad\\sigma=\\frac{b-a}{6}\\]

![FIG-03-66-004: Textbook-quality industrial engineering diagram illustrating pert duration and uncertainty with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-004-pert-duration-and-uncertainty.png)

### Worked Example 4

**Problem.** a=2, m=5, b=8 gives expected duration 5.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 66.5 Earned Value Management

Earned value separates planned work, completed work value, and actual cost.

\\[CV=EV-AC,\\quad SV=EV-PV\\]

![FIG-03-66-005: Textbook-quality industrial engineering diagram illustrating earned value management with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-005-earned-value-management.png)

### Worked Example 5

**Problem.** EV=80 and AC=100 gives CV=-20.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 66.6 Agile Project Management

Agile methods use short iterative cycles and frequent stakeholder feedback while retaining quality and risk obligations.

\\[\\text{iteration}\\rightarrow\\text{increment}\\rightarrow\\text{feedback}\\]

![FIG-03-66-006: Textbook-quality industrial engineering diagram illustrating agile project management with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-006-agile-project-management.png)

### Worked Example 6

**Problem.** A sprint review can expose changed requirements early.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 66.7 KPIs and Balanced Scorecards

Balanced performance measurement avoids optimizing cost or throughput while ignoring quality, people, or customer outcomes.

\\[\\text{metric}\\rightarrow\\text{objective}\\rightarrow\\text{decision}\\]

![FIG-03-66-007: Textbook-quality industrial engineering diagram illustrating kpis and balanced scorecards with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-007-kpis-and-balanced-scorecards.png)

### Worked Example 7

**Problem.** A throughput increase paired with higher defects is not an unqualified improvement.

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

Primary source basis: **FE Industrial & Systems specification Area(s) 7; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

Specification-required management/design topics that are not directly tabulated are identified as learned or guide-developed rather than assigned false Handbook pages.

---

## Where This Goes Wrong

**Using engineering management organization without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using work breakdown structure without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial critical path method without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using PERT project duration without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial earned value without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using agile engineering project management without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using management performance measurement without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| engineering management organization | Industrial/systems concept developed in §66.1; apply with the stated model assumptions and decision basis. |
| work breakdown structure | Industrial/systems concept developed in §66.2; apply with the stated model assumptions and decision basis. |
| industrial critical path method | Industrial/systems concept developed in §66.3; apply with the stated model assumptions and decision basis. |
| PERT project duration | Industrial/systems concept developed in §66.4; apply with the stated model assumptions and decision basis. |
| industrial earned value | Industrial/systems concept developed in §66.5; apply with the stated model assumptions and decision basis. |
| agile engineering project management | Industrial/systems concept developed in §66.6; apply with the stated model assumptions and decision basis. |
| management performance measurement | Industrial/systems concept developed in §66.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **engineering management organization** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **work breakdown structure** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **industrial critical path method** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **PERT project duration** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **industrial earned value** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **agile engineering project management** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **management performance measurement** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **engineering management organization**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **work breakdown structure**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial critical path method**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **PERT project duration**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial earned value**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **agile engineering project management**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **management performance measurement**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **engineering management organization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **work breakdown structure**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **industrial critical path method**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **PERT project duration**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **industrial earned value**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **agile engineering project management**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **management performance measurement**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **engineering management organization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **work breakdown structure**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **engineering management organization** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **work breakdown structure** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **industrial critical path method** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **PERT project duration** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **industrial earned value** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **agile engineering project management** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **management performance measurement** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **engineering management organization**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **work breakdown structure**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **industrial critical path method**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **PERT project duration**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **industrial earned value**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **agile engineering project management**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **management performance measurement**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. In a matrix, a project manager can share authority with functional managers.

2. Design, procurement, installation, and commissioning can be separate deliverables.

3. Zero-total-float activities lie on at least one critical path.

4. a=2, m=5, b=8 gives expected duration 5.

5. EV=80 and AC=100 gives CV=-20.

6. A sprint review can expose changed requirements early.

7. A throughput increase paired with higher defects is not an unqualified improvement.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §66.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §66.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §66.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §66.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §66.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §66.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §66.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 7, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 7.

- **engineering management organization:** Organization, Responsibility, and Motivation
- **work breakdown structure:** Work Breakdown Structures
- **industrial critical path method:** Critical Path Method
- **PERT project duration:** PERT Duration and Uncertainty
- **industrial earned value:** Earned Value Management
- **agile engineering project management:** Agile Project Management
- **management performance measurement:** KPIs and Balanced Scorecards

---

## What's Next

**Chapter 03-67: Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
