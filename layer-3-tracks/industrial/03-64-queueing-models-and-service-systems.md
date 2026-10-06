---
chapter: "03-64"
title: "Queueing Models and Service Systems"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-064-01, IND-3-064-02, IND-3-064-03, IND-3-064-04, IND-3-064-05, IND-3-064-06, IND-3-064-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-64: Queueing Models and Service Systems

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** MATH-1D-033-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Queueing Models and Service Systems** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **64.1** Explain and apply **Arrival Rate, Service Rate, Utilization, and Stability**.
* **64.2** Explain and apply **Little's Law**.
* **64.3** Explain and apply **M/M/1 Queue**.
* **64.4** Explain and apply **Finite-Capacity Queues**.
* **64.5** Explain and apply **Service-Time Variability**.
* **64.6** Explain and apply **Multiple-Server Queues**.
* **64.7** Explain and apply **Service-System Design Tradeoffs**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 64.1 Arrival Rate, Service Rate, Utilization, and Stability

Queue performance depends strongly on utilization; steady unconstrained queues require adequate service capacity.

\\[\\rho=\\frac{\\lambda}{s\\mu}\\]

![FIG-03-64-001: Textbook-quality industrial engineering diagram illustrating arrival rate, service rate, utilization, and stability with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-001-arrival-rate-service-rate-utilization-and-stability.png)

### Worked Example 1

**Problem.** With one server, λ=8/hr and μ=10/hr gives ρ=0.8.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 64.2 Little's Law

Little’s law links average number in system to throughput and average time when the averaging basis is consistent.

\\[L=\\lambda W,\\qquad L_q=\\lambda W_q\\]

![FIG-03-64-002: Textbook-quality industrial engineering diagram illustrating little's law with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-002-little-s-law.png)

### Worked Example 2

**Problem.** 20 customers/hr with W=0.25 hr gives L=5.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 64.3 M/M/1 Queue

The M/M/1 model assumes Poisson arrivals, exponential service, and one server. Delay grows rapidly as utilization approaches one.

\\[W=\\frac{1}{\\mu-\\lambda},\\quad L=\\frac{\\lambda}{\\mu-\\lambda}\\]

![FIG-03-64-003: Textbook-quality industrial engineering diagram illustrating m/m/1 queue with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-003-m-m-1-queue.png)

### Worked Example 3

**Problem.** λ=4/hr and μ=5/hr gives W=1 hr.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 64.4 Finite-Capacity Queues

Finite capacity causes some attempted arrivals to be blocked, reducing effective throughput.

\\[\\lambda_e=\\lambda(1-P_M)\\]

![FIG-03-64-004: Textbook-quality industrial engineering diagram illustrating finite-capacity queues with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-004-finite-capacity-queues.png)

### Worked Example 4

**Problem.** If 10% are blocked, effective throughput is 0.9λ.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 64.5 Service-Time Variability

At the same mean service rate, larger service-time variance produces more waiting.

\\[L_q=\\frac{\\lambda^2\\sigma_s^2+\\rho^2}{2(1-\\rho)}\\]

![FIG-03-64-005: Textbook-quality industrial engineering diagram illustrating service-time variability with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-005-service-time-variability.png)

### Worked Example 5

**Problem.** Reducing service-time variability can improve queue performance without changing mean capacity.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 64.6 Multiple-Server Queues

Multiple parallel servers share arrivals and often reduce wait time compared with one heavily loaded server.

\\[\\rho=\\frac{\\lambda}{s\\mu}<1\\]

![FIG-03-64-006: Textbook-quality industrial engineering diagram illustrating multiple-server queues with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-006-multiple-server-queues.png)

### Worked Example 6

**Problem.** Two servers at 6/hr each provide 12/hr nominal capacity.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 64.7 Service-System Design Tradeoffs

Queue design balances staffing/capacity against delay, congestion, and service targets.

\\[\\text{total cost}=\\text{capacity cost}+\\text{waiting cost}\\]

![FIG-03-64-007: Textbook-quality industrial engineering diagram illustrating service-system design tradeoffs with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-007-service-system-design-tradeoffs.png)

### Worked Example 7

**Problem.** Adding a server can sharply reduce waiting but may be uneconomic at low demand.

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

**Using queue utilization without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using Little law without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using M/M/1 queue without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using finite-capacity queue without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using M/G/1 queue without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using multiple-server queue without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using service-system queue design without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| queue utilization | Industrial/systems concept developed in §64.1; apply with the stated model assumptions and decision basis. |
| Little law | Industrial/systems concept developed in §64.2; apply with the stated model assumptions and decision basis. |
| M/M/1 queue | Industrial/systems concept developed in §64.3; apply with the stated model assumptions and decision basis. |
| finite-capacity queue | Industrial/systems concept developed in §64.4; apply with the stated model assumptions and decision basis. |
| M/G/1 queue | Industrial/systems concept developed in §64.5; apply with the stated model assumptions and decision basis. |
| multiple-server queue | Industrial/systems concept developed in §64.6; apply with the stated model assumptions and decision basis. |
| service-system queue design | Industrial/systems concept developed in §64.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **queue utilization** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **Little law** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **M/M/1 queue** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **finite-capacity queue** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **M/G/1 queue** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **multiple-server queue** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **service-system queue design** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **queue utilization**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **Little law**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **M/M/1 queue**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **finite-capacity queue**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **M/G/1 queue**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **multiple-server queue**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **service-system queue design**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **queue utilization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **Little law**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **M/M/1 queue**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **finite-capacity queue**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **M/G/1 queue**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **multiple-server queue**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **service-system queue design**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **queue utilization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **Little law**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **queue utilization** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **Little law** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **M/M/1 queue** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **finite-capacity queue** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **M/G/1 queue** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **multiple-server queue** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **service-system queue design** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **queue utilization**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **Little law**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **M/M/1 queue**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **finite-capacity queue**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **M/G/1 queue**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **multiple-server queue**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **service-system queue design**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. With one server, λ=8/hr and μ=10/hr gives ρ=0.8.

2. 20 customers/hr with W=0.25 hr gives L=5.

3. λ=4/hr and μ=5/hr gives W=1 hr.

4. If 10% are blocked, effective throughput is 0.9λ.

5. Reducing service-time variability can improve queue performance without changing mean capacity.

6. Two servers at 6/hr each provide 12/hr nominal capacity.

7. Adding a server can sharply reduce waiting but may be uneconomic at low demand.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §64.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §64.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §64.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §64.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §64.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §64.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §64.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 6, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 6.

- **queue utilization:** Arrival Rate, Service Rate, Utilization, and Stability
- **Little law:** Little's Law
- **M/M/1 queue:** M/M/1 Queue
- **finite-capacity queue:** Finite-Capacity Queues
- **M/G/1 queue:** Service-Time Variability
- **multiple-server queue:** Multiple-Server Queues
- **service-system queue design:** Service-System Design Tradeoffs

---

## What's Next

**Chapter 03-65: Markov Processes, Stochastic Models, and Simulation**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
