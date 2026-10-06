---
chapter: "03-72"
title: "Supply Chains, Transportation Networks, Pooling, and Distribution"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-072-01, IND-3-072-02, IND-3-072-03, IND-3-072-04, IND-3-072-05, IND-3-072-06, IND-3-072-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-72: Supply Chains, Transportation Networks, Pooling, and Distribution

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** IND-3-063-07 · IND-3-068-07 · IND-3-071-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Supply Chains, Transportation Networks, Pooling, and Distribution** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **72.1** Explain and apply **Supply-Chain Structure and Flows**.
* **72.2** Explain and apply **Transportation Allocation Models**.
* **72.3** Explain and apply **Supply-Chain Network Design**.
* **72.4** Explain and apply **Risk Pooling and Inventory Aggregation**.
* **72.5** Explain and apply **Multiechelon Distribution**.
* **72.6** Explain and apply **Lead Time, Service, and Resilience**.
* **72.7** Explain and apply **Bullwhip Effect and Information Coordination**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 72.1 Supply-Chain Structure and Flows

Supply chains coordinate material, information, and cash across echelons.

\\[\\text{suppliers}\\rightarrow\\text{plants}\\rightarrow\\text{DCs}\\rightarrow\\text{customers}\\]

![FIG-03-72-001: Textbook-quality industrial engineering diagram illustrating supply-chain structure and flows with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-001-supply-chain-structure-and-flows.png)

### Worked Example 1

**Problem.** A DC stockout can affect many customers even if upstream inventory exists.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 72.2 Transportation Allocation Models

Transportation models allocate supply to demand at minimum shipping cost under balance constraints.

\\[\\min\\sum_i\\sum_j c_{ij}x_{ij}\\]

![FIG-03-72-002: Textbook-quality industrial engineering diagram illustrating transportation allocation models with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-002-transportation-allocation-models.png)

### Worked Example 2

**Problem.** If one lane becomes more expensive, the optimal allocation may shift.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 72.3 Supply-Chain Network Design

Network design chooses facility count, location, capacity, and assignments.

\\[Total\\ cost=facility+transport+inventory+service\\ effects\\]

![FIG-03-72-003: Textbook-quality industrial engineering diagram illustrating supply-chain network design with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-003-supply-chain-network-design.png)

### Worked Example 3

**Problem.** Warehouse consolidation can lower inventory while increasing delivery distance.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 72.4 Risk Pooling and Inventory Aggregation

Pooling independent demand reduces relative uncertainty compared with separate stocks.

\\[\\sigma_{pooled}=\\sqrt{\\sum_i\\sigma_i^2}\\quad\\text{for independent demand}\\]

![FIG-03-72-004: Textbook-quality industrial engineering diagram illustrating risk pooling and inventory aggregation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-004-risk-pooling-and-inventory-aggregation.png)

### Worked Example 4

**Problem.** Two independent σ=10 demands pool to σ≈14.1, not 20.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 72.5 Multiechelon Distribution

Multilevel systems coordinate inventory across plants, central DCs, regional DCs, and customers.

\\[Inventory\\ position=on\\ hand+on\\ order-backorders\\]

![FIG-03-72-005: Textbook-quality industrial engineering diagram illustrating multiechelon distribution with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-005-multiechelon-distribution.png)

### Worked Example 5

**Problem.** A regional replenishment can be constrained by an upstream DC shortage.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 72.6 Lead Time, Service, and Resilience

Resilience balances normal efficiency against disruption tolerance and recovery.

\\[\\text{resilience}=\\text{ability to absorb disruption and recover service}\\]

![FIG-03-72-006: Textbook-quality industrial engineering diagram illustrating lead time, service, and resilience with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-006-lead-time-service-and-resilience.png)

### Worked Example 6

**Problem.** Dual sourcing can cost more normally but reduce single-supplier risk.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 72.7 Bullwhip Effect and Information Coordination

Forecast updating, batching, promotions, allocation, and delay can amplify upstream orders.

\\[Var(orders\\ upstream)>Var(customer\\ demand)\\text{ can occur}\\]

![FIG-03-72-007: Textbook-quality industrial engineering diagram illustrating bullwhip effect and information coordination with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-007-bullwhip-effect-and-information-coordination.png)

### Worked Example 7

**Problem.** Small retail-demand changes can cause larger distributor order swings.

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

Primary source basis: **FE Industrial & Systems specification Area(s) 9; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

Specification-required management/design topics that are not directly tabulated are identified as learned or guide-developed rather than assigned false Handbook pages.

---

## Where This Goes Wrong

**Using supply chain network without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using transportation optimization without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using supply chain network design without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using inventory risk pooling without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using multiechelon distribution without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using supply chain resilience without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using bullwhip effect without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| supply chain network | Industrial/systems concept developed in §72.1; apply with the stated model assumptions and decision basis. |
| transportation optimization | Industrial/systems concept developed in §72.2; apply with the stated model assumptions and decision basis. |
| supply chain network design | Industrial/systems concept developed in §72.3; apply with the stated model assumptions and decision basis. |
| inventory risk pooling | Industrial/systems concept developed in §72.4; apply with the stated model assumptions and decision basis. |
| multiechelon distribution | Industrial/systems concept developed in §72.5; apply with the stated model assumptions and decision basis. |
| supply chain resilience | Industrial/systems concept developed in §72.6; apply with the stated model assumptions and decision basis. |
| bullwhip effect | Industrial/systems concept developed in §72.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **supply chain network** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **transportation optimization** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **supply chain network design** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **inventory risk pooling** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **multiechelon distribution** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **supply chain resilience** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **bullwhip effect** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **supply chain network**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **transportation optimization**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **supply chain network design**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **inventory risk pooling**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **multiechelon distribution**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **supply chain resilience**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **bullwhip effect**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **supply chain network**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **transportation optimization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **supply chain network design**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **inventory risk pooling**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **multiechelon distribution**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **supply chain resilience**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **bullwhip effect**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **supply chain network**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **transportation optimization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **supply chain network** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **transportation optimization** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **supply chain network design** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **inventory risk pooling** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **multiechelon distribution** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **supply chain resilience** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **bullwhip effect** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **supply chain network**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **transportation optimization**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **supply chain network design**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **inventory risk pooling**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **multiechelon distribution**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **supply chain resilience**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **bullwhip effect**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. A DC stockout can affect many customers even if upstream inventory exists.

2. If one lane becomes more expensive, the optimal allocation may shift.

3. Warehouse consolidation can lower inventory while increasing delivery distance.

4. Two independent σ=10 demands pool to σ≈14.1, not 20.

5. A regional replenishment can be constrained by an upstream DC shortage.

6. Dual sourcing can cost more normally but reduce single-supplier risk.

7. Small retail-demand changes can cause larger distributor order swings.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §72.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §72.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §72.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §72.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §72.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §72.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §72.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 9, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 9.

- **supply chain network:** Supply-Chain Structure and Flows
- **transportation optimization:** Transportation Allocation Models
- **supply chain network design:** Supply-Chain Network Design
- **inventory risk pooling:** Risk Pooling and Inventory Aggregation
- **multiechelon distribution:** Multiechelon Distribution
- **supply chain resilience:** Lead Time, Service, and Resilience
- **bullwhip effect:** Bullwhip Effect and Information Coordination

---

## What's Next

**Chapter 03-73: Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
