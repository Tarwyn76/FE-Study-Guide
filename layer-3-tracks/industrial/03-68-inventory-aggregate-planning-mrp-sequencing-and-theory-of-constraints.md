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

**Solution.** EOQ varies with the square root of annual demand. If \(D\) doubles, \(Q_2^*/Q_1^*=\sqrt{2D/D}=\sqrt2=\mathbf{1.414}\); EOQ rises about 41.4%, not 100%.

---

## 68.2 Finite-Production Lot Sizing

Finite replenishment reduces peak inventory relative to instantaneous replenishment when R>D.

\\[Q^*=\\sqrt{\\frac{2AD}{h(1-D/R)}}\\]

![FIG-03-68-002: Textbook-quality industrial engineering diagram illustrating finite-production lot sizing with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-002-finite-production-lot-sizing.png)

### Worked Example 2

**Problem.** As R becomes very large, the result approaches EOQ.

**Solution.** In the finite-production lot model, the correction is \(1-D/R\). As production rate \(R\to\infty\), \(D/R\to0\), so the denominator approaches \(h\) and the expression reduces to the basic **EOQ** formula.

---

## 68.3 Reorder Point and Safety Stock

Reorder point covers expected lead-time demand plus safety stock selected for uncertainty/service.

\\[ROP=\\bar d_L+SS\\]

![FIG-03-68-003: Textbook-quality industrial engineering diagram illustrating reorder point and safety stock with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-003-reorder-point-and-safety-stock.png)

### Worked Example 3

**Problem.** 200 expected lead-time demand plus 50 safety stock gives ROP 250.

**Solution.** Reorder point is expected lead-time demand plus safety stock: \(ROP=200+50=\mathbf{250\ units}\). Inventory position, not merely shelf quantity, is normally compared with the reorder trigger.

---

## 68.4 Aggregate Production Planning

Aggregate planning balances workforce, overtime, inventory, backlog, and subcontracting over medium horizons.

\\[\\text{demand}=\\text{production}+\\text{inventory/backlog change}+\\text{other supply}\\]

![FIG-03-68-004: Textbook-quality industrial engineering diagram illustrating aggregate production planning with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-004-aggregate-production-planning.png)

### Worked Example 4

**Problem.** A level plan keeps production steadier and absorbs demand variation in inventory.

**Solution.** A level aggregate plan keeps the production rate comparatively stable. When demand is below production, inventory grows; when demand exceeds production, inventory is consumed or backlog develops. The tradeoff is workforce/production stability versus inventory/backlog cost.

---

## 68.5 Material Requirements Planning

MRP explodes demand through the bill of materials and offsets orders by lead time.

\\[\\text{gross requirements}-\\text{available/scheduled supply}=\\text{net requirements}\\]

![FIG-03-68-005: Textbook-quality industrial engineering diagram illustrating material requirements planning with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-005-material-requirements-planning.png)

### Worked Example 5

**Problem.** Ten parents needing two components each create gross demand of 20 components.

**Solution.** Gross component demand follows the bill of material. Ten parent units requiring two components each create \(10(2)=\mathbf{20\ components}\) before subtracting on-hand inventory or scheduled receipts to determine net requirements.

---

## 68.6 Johnson's Two-Machine Rule

Johnson’s rule gives a minimum-makespan sequence for the classic two-machine flow-shop assumptions.

\\[\\text{smallest M1 time}\\rightarrow\\text{early; smallest M2 time}\\rightarrow\\text{late}\\]

![FIG-03-68-006: Textbook-quality industrial engineering diagram illustrating johnson's two-machine rule with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-006-johnson-s-two-machine-rule.png)

### Worked Example 6

**Problem.** If the smallest remaining time is on machine 1, place that job earliest.

**Solution.** Johnson's rule repeatedly finds the smallest unscheduled processing time. If that smallest time is on machine 1, place the job in the earliest open sequence position; if it is on machine 2, place it in the latest open position.

---

## 68.7 Theory of Constraints

TOC focuses improvement on the current bottleneck rather than maximizing every resource independently.

\\[\\text{system throughput is limited by the active constraint}\\]

![FIG-03-68-007: Textbook-quality industrial engineering diagram illustrating theory of constraints with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-68-007-theory-of-constraints.png)

### Worked Example 7

**Problem.** Speeding a nonbottleneck does not raise system throughput when the bottleneck is unchanged.

**Solution.** If a bottleneck is already limiting system flow, increasing capacity at a nonbottleneck does not raise system throughput. Improvement effort should elevate or better exploit the active constraint, then reassess because the constraint may move.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For this chapter, the FE Reference Handbook relation and variable definitions control whenever the Handbook supplies them. Use the external source set **RUSSELL_TAYLOR, HOPP** only for specification-required learned material not fully developed in the Handbook.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 8; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Russell, R. S., & Taylor, B. W. (2023). *Operations and Supply Chain Management* (11th ed.). Wiley. ISBN 978-1-119-90567-7. Supporting scope: Operations planning, inventory, MRP, sequencing, lean systems, capacity, location, layout, quality, and supply-chain operations.
- Hopp, W. J., & Spearman, M. L. (2008). *Factory Physics* (3rd ed.). Waveland Press. ISBN 978-1-57766-739-1. Supporting scope: Throughput, WIP, cycle time, variability, bottlenecks, pull systems, capacity, inventory, and manufacturing-system behavior.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints**, the model boundary determines what is included in the decision. A valid solution must keep annual demand/holding/setup bases consistent, distinguish gross from net MRP requirements, respect finite-production assumptions and sequence rules, and locate the actual constraint.

16. Units and operational definitions are part of the model, not formatting details. For **Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints**. The external sources RUSSELL_TAYLOR, HOPP support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints** is to let finite production rate \(R	o\infty\) and confirm EPQ approaches EOQ; set safety stock to zero and confirm ROP becomes expected lead-time demand. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §68.1, **Economic Order Quantity**, is based on \(Q^*=\\sqrt{\\frac{2AD}{h}}\\). Interpret the result within the specific assumptions and system boundary of §68.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §68.2, **Finite-Production Lot Sizing**, is based on \(Q^*=\\sqrt{\\frac{2AD}{h(1-D/R)}}\\). Interpret the result within the specific assumptions and system boundary of §68.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §68.3, **Reorder Point and Safety Stock**, is based on \(ROP=\\bar d_L+SS\\). Interpret the result within the specific assumptions and system boundary of §68.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §68.4, **Aggregate Production Planning**, is based on \(\\text{demand}=\\text{production}+\\text{inventory/backlog change}+\\text{other supply}\\). Interpret the result within the specific assumptions and system boundary of §68.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §68.5, **Material Requirements Planning**, is based on \(\\text{gross requirements}-\\text{available/scheduled supply}=\\text{net requirements}\\). Interpret the result within the specific assumptions and system boundary of §68.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §68.6, **Johnson's Two-Machine Rule**, is based on \(\\text{smallest M1 time}\\rightarrow\\text{early; smallest M2 time}\\rightarrow\\text{late}\\). Interpret the result within the specific assumptions and system boundary of §68.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §68.7, **Theory of Constraints**, is based on \(\\text{system throughput is limited by the active constraint}\\). Interpret the result within the specific assumptions and system boundary of §68.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints.


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

1. **Independent solution for §68.1 — Economic Order Quantity.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: EOQ varies with the square root of annual demand. If \(D\) doubles, \(Q_2^*/Q_1^*=\sqrt{2D/D}=\sqrt2=\mathbf{1.414}\); EOQ rises about 41.4%, not 100%.

2. **Independent solution for §68.2 — Finite-Production Lot Sizing.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: In the finite-production lot model, the correction is \(1-D/R\). As production rate \(R\to\infty\), \(D/R\to0\), so the denominator approaches \(h\) and the expression reduces to the basic **EOQ** formula.

3. **Independent solution for §68.3 — Reorder Point and Safety Stock.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Reorder point is expected lead-time demand plus safety stock: \(ROP=200+50=\mathbf{250\ units}\). Inventory position, not merely shelf quantity, is normally compared with the reorder trigger.

4. **Independent solution for §68.4 — Aggregate Production Planning.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A level aggregate plan keeps the production rate comparatively stable. When demand is below production, inventory grows; when demand exceeds production, inventory is consumed or backlog develops. The tradeoff is workforce/production stability versus inventory/backlog cost.

5. **Independent solution for §68.5 — Material Requirements Planning.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Gross component demand follows the bill of material. Ten parent units requiring two components each create \(10(2)=\mathbf{20\ components}\) before subtracting on-hand inventory or scheduled receipts to determine net requirements.

6. **Independent solution for §68.6 — Johnson's Two-Machine Rule.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Johnson's rule repeatedly finds the smallest unscheduled processing time. If that smallest time is on machine 1, place the job in the earliest open sequence position; if it is on machine 2, place it in the latest open position.

7. **Independent solution for §68.7 — Theory of Constraints.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: If a bottleneck is already limiting system flow, increasing capacity at a nonbottleneck does not raise system throughput. Improvement effort should elevate or better exploit the active constraint, then reassess because the constraint may move.

8. For an integrated **Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints** problem, reject any result that violates this chapter-specific screen: keep annual demand/holding/setup bases consistent, distinguish gross from net MRP requirements, respect finite-production assumptions and sequence rules, and locate the actual constraint.

9. For **Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **RUSSELL_TAYLOR, HOPP** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: let finite production rate \(R	o\infty\) and confirm EPQ approaches EOQ; set safety stock to zero and confirm ROP becomes expected lead-time demand. The reduced case should behave as stated before the full model is trusted.

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
