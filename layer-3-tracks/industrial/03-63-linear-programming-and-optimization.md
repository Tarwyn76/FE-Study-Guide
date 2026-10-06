---
chapter: "03-63"
title: "Linear Programming and Optimization"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-063-01, IND-3-063-02, IND-3-063-03, IND-3-063-04, IND-3-063-05, IND-3-063-06, IND-3-063-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-63: Linear Programming and Optimization

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** ECON-2A-005-06 · MATH-1D-033-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Linear Programming and Optimization** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **63.1** Explain and apply **Decision Variables, Objectives, and Constraints**.
* **63.2** Explain and apply **Slack, Surplus, Binding Constraints, and Feasibility**.
* **63.3** Explain and apply **Graphical LP Solution and Corner Points**.
* **63.4** Explain and apply **Duality and Shadow Prices**.
* **63.5** Explain and apply **Reduced Cost and Sensitivity**.
* **63.6** Explain and apply **Transportation, Assignment, and Minimum-Cost Flow**.
* **63.7** Explain and apply **Optimization Model Verification**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 63.1 Decision Variables, Objectives, and Constraints

Linear programming models a linear objective subject to linear constraints. Formulation is often the hardest part.

\\[\\max Z=cx\\quad\\text{s.t. }Ax\\le b,\\ x\\ge0\\]

![FIG-03-63-001: Textbook-quality industrial engineering diagram illustrating decision variables, objectives, and constraints with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-001-decision-variables-objectives-and-constraints.png)

### Worked Example 1

**Problem.** Product quantities x1 and x2 can be constrained by available labor and material.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 63.2 Slack, Surplus, Binding Constraints, and Feasibility

Slack represents unused capacity in a less-than constraint; zero slack indicates a binding constraint.

\\[a_ix+s_i=b_i,\\quad s_i\\ge0\\]

![FIG-03-63-002: Textbook-quality industrial engineering diagram illustrating slack, surplus, binding constraints, and feasibility with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-002-slack-surplus-binding-constraints-and-feasibility.png)

### Worked Example 2

**Problem.** A 100-hour capacity with 92 hours used has 8 hours slack.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 63.3 Graphical LP Solution and Corner Points

For two-variable LPs, graph the feasible region and evaluate objective values at relevant corners.

\\[\\text{bounded LP optimum occurs at an extreme point}\\]

![FIG-03-63-003: Textbook-quality industrial engineering diagram illustrating graphical lp solution and corner points with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-003-graphical-lp-solution-and-corner-points.png)

### Worked Example 3

**Problem.** If no point satisfies every constraint, the model is infeasible.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 63.4 Duality and Shadow Prices

Dual variables can be interpreted as marginal resource values within a valid sensitivity range.

\\[\\max cx,Ax\\le b\\quad\\leftrightarrow\\quad\\min yb,yA\\ge c\\]

![FIG-03-63-004: Textbook-quality industrial engineering diagram illustrating duality and shadow prices with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-004-duality-and-shadow-prices.png)

### Worked Example 4

**Problem.** A $5/hr shadow price means one more hour of a binding resource can improve objective by about $5 locally.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 63.5 Reduced Cost and Sensitivity

Reduced costs and allowable ranges explain how robust an LP solution is to parameter changes.

\\[\\text{reduced cost}=\\text{objective improvement required for entry}\\]

![FIG-03-63-005: Textbook-quality industrial engineering diagram illustrating reduced cost and sensitivity with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-005-reduced-cost-and-sensitivity.png)

### Worked Example 5

**Problem.** An unused product may require a larger unit contribution before entering the optimal basis.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 63.6 Transportation, Assignment, and Minimum-Cost Flow

Transportation and assignment problems are special network optimization models with flow-conservation constraints.

\\[\\min\\sum_i\\sum_j c_{ij}x_{ij}\\]

![FIG-03-63-006: Textbook-quality industrial engineering diagram illustrating transportation, assignment, and minimum-cost flow with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-006-transportation-assignment-and-minimum-cost-flow.png)

### Worked Example 6

**Problem.** Allocate warehouse shipments to customers while minimizing transportation cost.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 63.7 Optimization Model Verification

An optimum is only optimal for the stated model. Missing integer, policy, or physical constraints can make it unusable.

\\[\\text{valid solution}=\\text{mathematical feasibility}+\\text{model validity}\\]

![FIG-03-63-007: Textbook-quality industrial engineering diagram illustrating optimization model verification with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-007-optimization-model-verification.png)

### Worked Example 7

**Problem.** A fractional workforce solution is not implementable if people must be whole.

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

**Using linear programming formulation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using linear programming slack without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using linear programming corner solution without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using linear programming dual price without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using linear programming reduced cost without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using minimum-cost network flow without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using optimization solution validation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| linear programming formulation | Industrial/systems concept developed in §63.1; apply with the stated model assumptions and decision basis. |
| linear programming slack | Industrial/systems concept developed in §63.2; apply with the stated model assumptions and decision basis. |
| linear programming corner solution | Industrial/systems concept developed in §63.3; apply with the stated model assumptions and decision basis. |
| linear programming dual price | Industrial/systems concept developed in §63.4; apply with the stated model assumptions and decision basis. |
| linear programming reduced cost | Industrial/systems concept developed in §63.5; apply with the stated model assumptions and decision basis. |
| minimum-cost network flow | Industrial/systems concept developed in §63.6; apply with the stated model assumptions and decision basis. |
| optimization solution validation | Industrial/systems concept developed in §63.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **linear programming formulation** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **linear programming slack** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **linear programming corner solution** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **linear programming dual price** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **linear programming reduced cost** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **minimum-cost network flow** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **optimization solution validation** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **linear programming formulation**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **linear programming slack**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **linear programming corner solution**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **linear programming dual price**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **linear programming reduced cost**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **minimum-cost network flow**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **optimization solution validation**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **linear programming formulation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **linear programming slack**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **linear programming corner solution**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **linear programming dual price**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **linear programming reduced cost**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **minimum-cost network flow**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **optimization solution validation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **linear programming formulation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **linear programming slack**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **linear programming formulation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **linear programming slack** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **linear programming corner solution** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **linear programming dual price** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **linear programming reduced cost** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **minimum-cost network flow** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **optimization solution validation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **linear programming formulation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **linear programming slack**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **linear programming corner solution**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **linear programming dual price**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **linear programming reduced cost**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **minimum-cost network flow**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **optimization solution validation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. Product quantities x1 and x2 can be constrained by available labor and material.

2. A 100-hour capacity with 92 hours used has 8 hours slack.

3. If no point satisfies every constraint, the model is infeasible.

4. A $5/hr shadow price means one more hour of a binding resource can improve objective by about $5 locally.

5. An unused product may require a larger unit contribution before entering the optimal basis.

6. Allocate warehouse shipments to customers while minimizing transportation cost.

7. A fractional workforce solution is not implementable if people must be whole.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §63.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §63.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §63.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §63.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §63.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §63.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §63.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 6, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 6.

- **linear programming formulation:** Decision Variables, Objectives, and Constraints
- **linear programming slack:** Slack, Surplus, Binding Constraints, and Feasibility
- **linear programming corner solution:** Graphical LP Solution and Corner Points
- **linear programming dual price:** Duality and Shadow Prices
- **linear programming reduced cost:** Reduced Cost and Sensitivity
- **minimum-cost network flow:** Transportation, Assignment, and Minimum-Cost Flow
- **optimization solution validation:** Optimization Model Verification

---

## What's Next

**Chapter 03-64: Queueing Models and Service Systems**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
