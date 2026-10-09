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

**Solution.** Let \(x_1,x_2\) be product quantities. Each resource constraint is written from unit consumption times quantity, for example \(a_{11}x_1+a_{12}x_2\le b_1\), and the objective \(Z=c_1x_1+c_2x_2\) represents contribution, cost, or another defined criterion. Nonnegativity closes the basic LP model.

---

## 63.2 Slack, Surplus, Binding Constraints, and Feasibility

Slack represents unused capacity in a less-than constraint; zero slack indicates a binding constraint.

\\[a_ix+s_i=b_i,\\quad s_i\\ge0\\]

![FIG-03-63-002: Textbook-quality industrial engineering diagram illustrating slack, surplus, binding constraints, and feasibility with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-002-slack-surplus-binding-constraints-and-feasibility.png)

### Worked Example 2

**Problem.** A 100-hour capacity with 92 hours used has 8 hours slack.

**Solution.** Slack is unused capacity. With 100 hr available and 92 hr used, \(s=100-92=\mathbf{8\ hr}\). A positive 8-hr slack means that capacity constraint is nonbinding at this solution.

---

## 63.3 Graphical LP Solution and Corner Points

For two-variable LPs, graph the feasible region and evaluate objective values at relevant corners.

\\[\\text{bounded LP optimum occurs at an extreme point}\\]

![FIG-03-63-003: Textbook-quality industrial engineering diagram illustrating graphical lp solution and corner points with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-003-graphical-lp-solution-and-corner-points.png)

### Worked Example 3

**Problem.** If no point satisfies every constraint, the model is infeasible.

**Solution.** In a two-variable LP, graph every constraint and keep only the common feasible region. If there is **no point** satisfying all constraints simultaneously, the feasible set is empty and the model is **infeasible**; there is no corner point at which an optimum can exist.

---

## 63.4 Duality and Shadow Prices

Dual variables can be interpreted as marginal resource values within a valid sensitivity range.

\\[\\max cx,Ax\\le b\\quad\\leftrightarrow\\quad\\min yb,yA\\ge c\\]

![FIG-03-63-004: Textbook-quality industrial engineering diagram illustrating duality and shadow prices with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-004-duality-and-shadow-prices.png)

### Worked Example 4

**Problem.** A $5/hr shadow price means one more hour of a binding resource can improve objective by about $5 locally.

**Solution.** A shadow price of \$5/hr means that, while the current basis remains valid, increasing the right-hand side of that binding resource by 1 hr changes the optimal objective by about **\$5** in the favorable direction. It is a local marginal value, not an unlimited price.

---

## 63.5 Reduced Cost and Sensitivity

Reduced costs and allowable ranges explain how robust an LP solution is to parameter changes.

\\[\\text{reduced cost}=\\text{objective improvement required for entry}\\]

![FIG-03-63-005: Textbook-quality industrial engineering diagram illustrating reduced cost and sensitivity with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-005-reduced-cost-and-sensitivity.png)

### Worked Example 5

**Problem.** An unused product may require a larger unit contribution before entering the optimal basis.

**Solution.** For a maximization model, a nonbasic variable with unfavorable reduced cost must improve its objective coefficient sufficiently before entering the optimal basis. The allowable coefficient range is therefore a **local sensitivity statement tied to the current basis**, not proof that all other parameter changes leave the solution unchanged.

---

## 63.6 Transportation, Assignment, and Minimum-Cost Flow

Transportation and assignment problems are special network optimization models with flow-conservation constraints.

\\[\\min\\sum_i\\sum_j c_{ij}x_{ij}\\]

![FIG-03-63-006: Textbook-quality industrial engineering diagram illustrating transportation, assignment, and minimum-cost flow with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-006-transportation-assignment-and-minimum-cost-flow.png)

### Worked Example 6

**Problem.** Allocate warehouse shipments to customers while minimizing transportation cost.

**Solution.** The transportation model assigns \(x_{ij}\) from origins \(i\) to destinations \(j\), minimizes \(\sum c_{ij}x_{ij}\), and enforces supply/demand balances. Assignment is the special one-to-one case; minimum-cost flow generalizes the same cost-plus-flow-conservation structure to a network.

---

## 63.7 Optimization Model Verification

An optimum is only optimal for the stated model. Missing integer, policy, or physical constraints can make it unusable.

\\[\\text{valid solution}=\\text{mathematical feasibility}+\\text{model validity}\\]

![FIG-03-63-007: Textbook-quality industrial engineering diagram illustrating optimization model verification with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-63-007-optimization-model-verification.png)

### Worked Example 7

**Problem.** A fractional workforce solution is not implementable if people must be whole.

**Solution.** If a solver returns 3.6 workers but headcount must be integral, the continuous LP result is not directly implementable. Either impose integer variables and re-solve or evaluate nearby feasible integer alternatives; simple rounding can violate capacity or coverage constraints.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Linear Programming and Optimization**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For **Linear Programming and Optimization**, the FE Reference Handbook formulation and variable definitions govern when supplied. Hillier and Lieberman supports the learned material on **linear-programming geometry, duality, reduced cost, sensitivity, transportation, and integrality**. Do not substitute a remembered textbook convention when the problem or Handbook defines a different sign, capacity, or variable basis.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 6; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Hillier, F. S., & Lieberman, G. J. (2021). *Introduction to Operations Research* (11th ed.). McGraw-Hill Education. ISBN 978-1-260-57587-3. Supporting scope: Linear programming, duality/sensitivity, transportation/network models, queueing, inventory, Markov models, and simulation.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Linear Programming and Optimization**, the model boundary determines what is included in the decision. A valid solution must confirm every constraint is satisfied, variable domains are implementable, sensitivity statements remain inside their valid ranges, and the objective represents the actual decision.

16. Units and operational definitions are part of the model, not formatting details. For **Linear Programming and Optimization**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Linear Programming and Optimization**. The external sources HILLIER support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Linear Programming and Optimization** is to set a resource RHS large enough to be nonbinding and confirm its slack becomes positive and its local shadow value falls to zero in the new optimum. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §63.1, **Decision Variables, Objectives, and Constraints**, is based on \(\\max Z=cx\\quad\\text{s.t. }Ax\\le b,\\ x\\ge0\\). Interpret the result within the specific assumptions and system boundary of §63.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §63.2, **Slack, Surplus, Binding Constraints, and Feasibility**, is based on \(a_ix+s_i=b_i,\\quad s_i\\ge0\\). Interpret the result within the specific assumptions and system boundary of §63.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §63.3, **Graphical LP Solution and Corner Points**, is based on \(\\text{bounded LP optimum occurs at an extreme point}\\). Interpret the result within the specific assumptions and system boundary of §63.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §63.4, **Duality and Shadow Prices**, is based on \(\\max cx,Ax\\le b\\quad\\leftrightarrow\\quad\\min yb,yA\\ge c\\). Interpret the result within the specific assumptions and system boundary of §63.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §63.5, **Reduced Cost and Sensitivity**, is based on \(\\text{reduced cost}=\\text{objective improvement required for entry}\\). Interpret the result within the specific assumptions and system boundary of §63.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §63.6, **Transportation, Assignment, and Minimum-Cost Flow**, is based on \(\\min\\sum_i\\sum_j c_{ij}x_{ij}\\). Interpret the result within the specific assumptions and system boundary of §63.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §63.7, **Optimization Model Verification**, is based on \(\\text{valid solution}=\\text{mathematical feasibility}+\\text{model validity}\\). Interpret the result within the specific assumptions and system boundary of §63.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Linear Programming and Optimization decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Linear Programming and Optimization.


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

1. **Independent solution for §63.1 — Decision Variables, Objectives, and Constraints.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Let \(x_1,x_2\) be product quantities. Each resource constraint is written from unit consumption times quantity, for example \(a_{11}x_1+a_{12}x_2\le b_1\), and the objective \(Z=c_1x_1+c_2x_2\) represents contribution, cost, or another defined criterion. Nonnegativity closes the basic LP model.

2. **Independent solution for §63.2 — Slack, Surplus, Binding Constraints, and Feasibility.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Slack is unused capacity. With 100 hr available and 92 hr used, \(s=100-92=\mathbf{8\ hr}\). A positive 8-hr slack means that capacity constraint is nonbinding at this solution.

3. **Independent solution for §63.3 — Graphical LP Solution and Corner Points.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: In a two-variable LP, graph every constraint and keep only the common feasible region. If there is **no point** satisfying all constraints simultaneously, the feasible set is empty and the model is **infeasible**; there is no corner point at which an optimum can exist.

4. **Independent solution for §63.4 — Duality and Shadow Prices.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A shadow price of \$5/hr means that, while the current basis remains valid, increasing the right-hand side of that binding resource by 1 hr changes the optimal objective by about **\$5** in the favorable direction. It is a local marginal value, not an unlimited price.

5. **Independent solution for §63.5 — Reduced Cost and Sensitivity.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: For a maximization model, a nonbasic variable with unfavorable reduced cost must improve its objective coefficient sufficiently before entering the optimal basis. The allowable coefficient range is therefore a **local sensitivity statement tied to the current basis**, not proof that all other parameter changes leave the solution unchanged.

6. **Independent solution for §63.6 — Transportation, Assignment, and Minimum-Cost Flow.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: The transportation model assigns \(x_{ij}\) from origins \(i\) to destinations \(j\), minimizes \(\sum c_{ij}x_{ij}\), and enforces supply/demand balances. Assignment is the special one-to-one case; minimum-cost flow generalizes the same cost-plus-flow-conservation structure to a network.

7. **Independent solution for §63.7 — Optimization Model Verification.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: If a solver returns 3.6 workers but headcount must be integral, the continuous LP result is not directly implementable. Either impose integer variables and re-solve or evaluate nearby feasible integer alternatives; simple rounding can violate capacity or coverage constraints.

8. For an integrated **Linear Programming and Optimization** problem, reject any result that violates this chapter-specific screen: confirm every constraint is satisfied, variable domains are implementable, sensitivity statements remain inside their valid ranges, and the objective represents the actual decision.

9. For **Linear Programming and Optimization**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **HILLIER** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: set a resource RHS large enough to be nonbinding and confirm its slack becomes positive and its local shadow value falls to zero in the new optimum. The reduced case should behave as stated before the full model is trusted.

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
