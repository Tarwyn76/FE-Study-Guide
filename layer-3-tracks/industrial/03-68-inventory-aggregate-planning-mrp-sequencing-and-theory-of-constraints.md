---
chapter: "03-68"
title: "Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-068-01, IND-3-068-02, IND-3-068-03, IND-3-068-04, IND-3-068-05, IND-3-068-06, IND-3-068-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-68: Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** IND-3-067-07 · ECON-2A-005-06

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **68.1** Explain and apply **Economic Order Quantity**.
* **68.2** Explain and apply **Finite-Production Lot Sizing**.
* **68.3** Explain and apply **Reorder Point and Safety Stock**.
* **68.4** Explain and apply **Aggregate Production Planning**.
* **68.5** Explain and apply **Material Requirements Planning**.
* **68.6** Explain and apply **Johnson's Two-Machine Rule**.
* **68.7** Explain and apply **Theory of Constraints**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 68.1 Economic Order Quantity

EOQ balances ordering/setup cost against holding cost under restrictive assumptions.

\\[Q^*=\\sqrt{\\frac{2AD}{h}}\\]

![FIG-03-68-001: Textbook-quality industrial engineering diagram illustrating economic order quantity with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-001-economic-order-quantity.png)

### Worked Example 1

**Problem.** Doubling annual demand increases EOQ by √2.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 68.2 Finite-Production Lot Sizing

Finite replenishment reduces peak inventory relative to instantaneous replenishment when R>D.

\\[Q^*=\\sqrt{\\frac{2AD}{h(1-D/R)}}\\]

![FIG-03-68-002: Textbook-quality industrial engineering diagram illustrating finite-production lot sizing with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-002-finite-production-lot-sizing.png)

### Worked Example 2

**Problem.** As R becomes very large, the result approaches EOQ.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 68.3 Reorder Point and Safety Stock

Reorder point covers expected lead-time demand plus safety stock selected for uncertainty/service.

\\[ROP=\\bar d_L+SS\\]

![FIG-03-68-003: Textbook-quality industrial engineering diagram illustrating reorder point and safety stock with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-003-reorder-point-and-safety-stock.png)

### Worked Example 3

**Problem.** 200 expected lead-time demand plus 50 safety stock gives ROP 250.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 68.4 Aggregate Production Planning

Aggregate planning balances workforce, overtime, inventory, backlog, and subcontracting over medium horizons.

\\[\\text{demand}=\\text{production}+\\text{inventory/backlog change}+\\text{other supply}\\]

![FIG-03-68-004: Textbook-quality industrial engineering diagram illustrating aggregate production planning with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-004-aggregate-production-planning.png)

### Worked Example 4

**Problem.** A level plan keeps production steadier and absorbs demand variation in inventory.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 68.5 Material Requirements Planning

MRP explodes demand through the bill of materials and offsets orders by lead time.

\\[\\text{gross requirements}-\\text{available/scheduled supply}=\\text{net requirements}\\]

![FIG-03-68-005: Textbook-quality industrial engineering diagram illustrating material requirements planning with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-005-material-requirements-planning.png)

### Worked Example 5

**Problem.** Ten parents needing two components each create gross demand of 20 components.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 68.6 Johnson's Two-Machine Rule

Johnson’s rule gives a minimum-makespan sequence for the classic two-machine flow-shop assumptions.

\\[\\text{smallest M1 time}\\rightarrow\\text{early; smallest M2 time}\\rightarrow\\text{late}\\]

![FIG-03-68-006: Textbook-quality industrial engineering diagram illustrating johnson's two-machine rule with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-006-johnson-s-two-machine-rule.png)

### Worked Example 6

**Problem.** If the smallest remaining time is on machine 1, place that job earliest.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 68.7 Theory of Constraints

TOC focuses improvement on the current bottleneck rather than maximizing every resource independently.

\\[\\text{system throughput is limited by the active constraint}\\]

![FIG-03-68-007: Textbook-quality industrial engineering diagram illustrating theory of constraints with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-007-theory-of-constraints.png)

### Worked Example 7

**Problem.** Speeding a nonbottleneck does not raise system throughput when the bottleneck is unchanged.

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

Primary source basis: **FE Industrial & Systems specification Area(s) 8; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

Specification-required management/design topics that are not directly tabulated are identified as learned or guide-developed rather than assigned false Handbook pages.

---

## Where This Goes Wrong

**Using economic order quantity without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using economic manufacturing quantity without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using inventory reorder point without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using aggregate production plan without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using material requirements planning without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using Johnson sequencing rule without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using theory of constraints bottleneck without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| economic order quantity | Industrial/systems concept developed in §68.1; apply with the stated model assumptions and decision basis. |
| economic manufacturing quantity | Industrial/systems concept developed in §68.2; apply with the stated model assumptions and decision basis. |
| inventory reorder point | Industrial/systems concept developed in §68.3; apply with the stated model assumptions and decision basis. |
| aggregate production plan | Industrial/systems concept developed in §68.4; apply with the stated model assumptions and decision basis. |
| material requirements planning | Industrial/systems concept developed in §68.5; apply with the stated model assumptions and decision basis. |
| Johnson sequencing rule | Industrial/systems concept developed in §68.6; apply with the stated model assumptions and decision basis. |
| theory of constraints bottleneck | Industrial/systems concept developed in §68.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **economic order quantity** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **economic manufacturing quantity** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **inventory reorder point** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **aggregate production plan** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **material requirements planning** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **Johnson sequencing rule** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **theory of constraints bottleneck** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **economic order quantity**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **economic manufacturing quantity**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **inventory reorder point**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **aggregate production plan**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **material requirements planning**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **Johnson sequencing rule**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **theory of constraints bottleneck**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **economic order quantity**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **economic manufacturing quantity**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **inventory reorder point**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **aggregate production plan**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **material requirements planning**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **Johnson sequencing rule**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **theory of constraints bottleneck**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **economic order quantity**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **economic manufacturing quantity**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **economic order quantity** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **economic manufacturing quantity** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **inventory reorder point** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **aggregate production plan** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **material requirements planning** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **Johnson sequencing rule** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **theory of constraints bottleneck** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **economic order quantity**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **economic manufacturing quantity**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **inventory reorder point**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **aggregate production plan**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **material requirements planning**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **Johnson sequencing rule**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **theory of constraints bottleneck**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. Doubling annual demand increases EOQ by √2.

2. As R becomes very large, the result approaches EOQ.

3. 200 expected lead-time demand plus 50 safety stock gives ROP 250.

4. A level plan keeps production steadier and absorbs demand variation in inventory.

5. Ten parents needing two components each create gross demand of 20 components.

6. If the smallest remaining time is on machine 1, place that job earliest.

7. Speeding a nonbottleneck does not raise system throughput when the bottleneck is unchanged.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §68.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §68.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §68.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §68.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §68.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §68.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §68.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 8, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 8.

- **economic order quantity:** Economic Order Quantity
- **economic manufacturing quantity:** Finite-Production Lot Sizing
- **inventory reorder point:** Reorder Point and Safety Stock
- **aggregate production plan:** Aggregate Production Planning
- **material requirements planning:** Material Requirements Planning
- **Johnson sequencing rule:** Johnson's Two-Machine Rule
- **theory of constraints bottleneck:** Theory of Constraints

---

## What's Next

**Chapter 03-69: Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
