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

**Solution.** Inventory located upstream cannot instantly satisfy a downstream stockout. A distribution-center shortage can interrupt service to many customers until replenishment traverses the remaining lead time, so echelon position and response time matter in addition to total network inventory.

---

## 72.2 Transportation Allocation Models

Transportation models allocate supply to demand at minimum shipping cost under balance constraints.

\\[\\min\\sum_i\\sum_j c_{ij}x_{ij}\\]

![FIG-03-72-002: Textbook-quality industrial engineering diagram illustrating transportation allocation models with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-002-transportation-allocation-models.png)

### Worked Example 2

**Problem.** If one lane becomes more expensive, the optimal allocation may shift.

**Solution.** The transportation LP minimizes \(\sum c_{ij}x_{ij}\) subject to source supply and destination demand constraints. If one lane's unit cost rises, the current basis may cease to be optimal and flow can shift to alternate lanes with available supply/demand capacity.

---

## 72.3 Supply-Chain Network Design

Network design chooses facility count, location, capacity, and assignments.

\\[Total\\ cost=facility+transport+inventory+service\\ effects\\]

![FIG-03-72-003: Textbook-quality industrial engineering diagram illustrating supply-chain network design with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-003-supply-chain-network-design.png)

### Worked Example 3

**Problem.** Warehouse consolidation can lower inventory while increasing delivery distance.

**Solution.** Consolidating warehouses can reduce safety-stock duplication through pooling but may lengthen delivery distances or response times. Network design therefore evaluates facility fixed cost, transportation, inventory, capacity, and service simultaneously.

---

## 72.4 Risk Pooling and Inventory Aggregation

Pooling independent demand reduces relative uncertainty compared with separate stocks.

\\[\\sigma_{pooled}=\\sqrt{\\sum_i\\sigma_i^2}\\quad\\text{for independent demand}\\]

![FIG-03-72-004: Textbook-quality industrial engineering diagram illustrating risk pooling and inventory aggregation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-004-risk-pooling-and-inventory-aggregation.png)

### Worked Example 4

**Problem.** Two independent σ=10 demands pool to σ≈14.1, not 20.

**Solution.** For two independent demands with \(\sigma_1=\sigma_2=10\), pooled standard deviation is \(\sqrt{10^2+10^2}=\sqrt{200}=\mathbf{14.14}\), less than the separate sum 20. Correlation would change the pooling benefit.

---

## 72.5 Multiechelon Distribution

Multilevel systems coordinate inventory across plants, central DCs, regional DCs, and customers.

\\[Inventory\\ position=on\\ hand+on\\ order-backorders\\]

![FIG-03-72-005: Textbook-quality industrial engineering diagram illustrating multiechelon distribution with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-005-multiechelon-distribution.png)

### Worked Example 5

**Problem.** A regional replenishment can be constrained by an upstream DC shortage.

**Solution.** Inventory position is on-hand plus on-order minus backorders. A regional location may appear to need replenishment while the upstream distribution center is itself constrained, so multiechelon decisions must respect upstream availability and lead times.

---

## 72.6 Lead Time, Service, and Resilience

Resilience balances normal efficiency against disruption tolerance and recovery.

\\[\\text{resilience}=\\text{ability to absorb disruption and recover service}\\]

![FIG-03-72-006: Textbook-quality industrial engineering diagram illustrating lead time, service, and resilience with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-006-lead-time-service-and-resilience.png)

### Worked Example 6

**Problem.** Dual sourcing can cost more normally but reduce single-supplier risk.

**Solution.** Dual sourcing can increase normal procurement/coordination cost but reduce exposure to a single supplier's outage. Resilience analysis weighs disruption probability/impact, recovery time, substitutability, lead time, and service consequences rather than unit price alone.

---

## 72.7 Bullwhip Effect and Information Coordination

Forecast updating, batching, promotions, allocation, and delay can amplify upstream orders.

\\[Var(orders\\ upstream)>Var(customer\\ demand)\\text{ can occur}\\]

![FIG-03-72-007: Textbook-quality industrial engineering diagram illustrating bullwhip effect and information coordination with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-72-007-bullwhip-effect-and-information-coordination.png)

### Worked Example 7

**Problem.** Small retail-demand changes can cause larger distributor order swings.

**Solution.** The bullwhip effect is amplification of order variability upstream relative to customer demand. Forecast updating, batching, rationing/gaming, promotions, and long lead times can contribute; sharing demand information and reducing delay/batching can dampen amplification.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Supply Chains, Transportation Networks, Pooling, and Distribution**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For this chapter, the FE Reference Handbook relation and variable definitions control whenever the Handbook supplies them. Use the external source set **CHOPRA8, HILLIER** only for specification-required learned material not fully developed in the Handbook.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 9; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Chopra, S. (2025). *Supply Chain Management: Strategy, Planning, and Operation* (8th ed.). Pearson. ISBN 978-0-13-535029-4. Supporting scope: Supply-chain network design, inventory, transportation, information, sourcing, pooling, resilience, and coordination.
- Hillier, F. S., & Lieberman, G. J. (2021). *Introduction to Operations Research* (11th ed.). McGraw-Hill Education. ISBN 978-1-260-57587-3. Supporting scope: Linear programming, duality/sensitivity, transportation/network models, queueing, inventory, Markov models, and simulation.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Supply Chains, Transportation Networks, Pooling, and Distribution**, the model boundary determines what is included in the decision. A valid solution must balance supply and demand, include facility/inventory/transport/service tradeoffs, model correlation when pooling demand, preserve echelon inventory logic, and distinguish resilience from lowest normal cost.

16. Units and operational definitions are part of the model, not formatting details. For **Supply Chains, Transportation Networks, Pooling, and Distribution**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Supply Chains, Transportation Networks, Pooling, and Distribution**. The external sources CHOPRA8, HILLIER support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Supply Chains, Transportation Networks, Pooling, and Distribution** is to set independent demand variance of one pooled location to zero and confirm pooled variance reduces to the remaining variance; set one lane prohibitively costly and confirm an optimal model avoids it if alternatives are feasible. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §72.1, **Supply-Chain Structure and Flows**, is based on \(\\text{suppliers}\\rightarrow\\text{plants}\\rightarrow\\text{DCs}\\rightarrow\\text{customers}\\). Interpret the result within the specific assumptions and system boundary of §72.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §72.2, **Transportation Allocation Models**, is based on \(\\min\\sum_i\\sum_j c_{ij}x_{ij}\\). Interpret the result within the specific assumptions and system boundary of §72.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §72.3, **Supply-Chain Network Design**, is based on \(Total\\ cost=facility+transport+inventory+service\\ effects\\). Interpret the result within the specific assumptions and system boundary of §72.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §72.4, **Risk Pooling and Inventory Aggregation**, is based on \(\\sigma_{pooled}=\\sqrt{\\sum_i\\sigma_i^2}\\quad\\text{for independent demand}\\). Interpret the result within the specific assumptions and system boundary of §72.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §72.5, **Multiechelon Distribution**, is based on \(Inventory\\ position=on\\ hand+on\\ order-backorders\\). Interpret the result within the specific assumptions and system boundary of §72.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §72.6, **Lead Time, Service, and Resilience**, is based on \(\\text{resilience}=\\text{ability to absorb disruption and recover service}\\). Interpret the result within the specific assumptions and system boundary of §72.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §72.7, **Bullwhip Effect and Information Coordination**, is based on \(Var(orders\\ upstream)>Var(customer\\ demand)\\text{ can occur}\\). Interpret the result within the specific assumptions and system boundary of §72.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Supply Chains, Transportation Networks, Pooling, and Distribution decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Supply Chains, Transportation Networks, Pooling, and Distribution.


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

1. **Independent solution for §72.1 — Supply-Chain Structure and Flows.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Inventory located upstream cannot instantly satisfy a downstream stockout. A distribution-center shortage can interrupt service to many customers until replenishment traverses the remaining lead time, so echelon position and response time matter in addition to total network inventory.

2. **Independent solution for §72.2 — Transportation Allocation Models.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: The transportation LP minimizes \(\sum c_{ij}x_{ij}\) subject to source supply and destination demand constraints. If one lane's unit cost rises, the current basis may cease to be optimal and flow can shift to alternate lanes with available supply/demand capacity.

3. **Independent solution for §72.3 — Supply-Chain Network Design.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Consolidating warehouses can reduce safety-stock duplication through pooling but may lengthen delivery distances or response times. Network design therefore evaluates facility fixed cost, transportation, inventory, capacity, and service simultaneously.

4. **Independent solution for §72.4 — Risk Pooling and Inventory Aggregation.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: For two independent demands with \(\sigma_1=\sigma_2=10\), pooled standard deviation is \(\sqrt{10^2+10^2}=\sqrt{200}=\mathbf{14.14}\), less than the separate sum 20. Correlation would change the pooling benefit.

5. **Independent solution for §72.5 — Multiechelon Distribution.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Inventory position is on-hand plus on-order minus backorders. A regional location may appear to need replenishment while the upstream distribution center is itself constrained, so multiechelon decisions must respect upstream availability and lead times.

6. **Independent solution for §72.6 — Lead Time, Service, and Resilience.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Dual sourcing can increase normal procurement/coordination cost but reduce exposure to a single supplier's outage. Resilience analysis weighs disruption probability/impact, recovery time, substitutability, lead time, and service consequences rather than unit price alone.

7. **Independent solution for §72.7 — Bullwhip Effect and Information Coordination.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: The bullwhip effect is amplification of order variability upstream relative to customer demand. Forecast updating, batching, rationing/gaming, promotions, and long lead times can contribute; sharing demand information and reducing delay/batching can dampen amplification.

8. For an integrated **Supply Chains, Transportation Networks, Pooling, and Distribution** problem, reject any result that violates this chapter-specific screen: balance supply and demand, include facility/inventory/transport/service tradeoffs, model correlation when pooling demand, preserve echelon inventory logic, and distinguish resilience from lowest normal cost.

9. For **Supply Chains, Transportation Networks, Pooling, and Distribution**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **CHOPRA8, HILLIER** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: set independent demand variance of one pooled location to zero and confirm pooled variance reduces to the remaining variance; set one lane prohibitively costly and confirm an optimal model avoids it if alternatives are feasible. The reduced case should behave as stated before the full model is trusted.

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
