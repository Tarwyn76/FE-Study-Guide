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

**Solution.** For one server, \(\rho=\lambda/\mu=(8\ {\rm hr^{-1}})/(10\ {\rm hr^{-1}})=\mathbf{0.80}\). Because \(\rho<1\), the basic steady-state stability condition is satisfied; 80% is the long-run busy fraction under the model assumptions.

---

## 64.2 Little's Law

Little’s law links average number in system to throughput and average time when the averaging basis is consistent.

\\[L=\\lambda W,\\qquad L_q=\\lambda W_q\\]

![FIG-03-64-002: Textbook-quality industrial engineering diagram illustrating little's law with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-002-little-s-law.png)

### Worked Example 2

**Problem.** 20 customers/hr with W=0.25 hr gives L=5.

**Solution.** Little's Law gives \(L=\lambda W=(20\ {\rm customers/hr})(0.25\ {\rm hr})=\mathbf{5\ customers}\). The 0.25 hr is 15 min, and the units reduce correctly to customers.

---

## 64.3 M/M/1 Queue

The M/M/1 model assumes Poisson arrivals, exponential service, and one server. Delay grows rapidly as utilization approaches one.

\\[W=\\frac{1}{\\mu-\\lambda},\\quad L=\\frac{\\lambda}{\\mu-\\lambda}\\]

![FIG-03-64-003: Textbook-quality industrial engineering diagram illustrating m/m/1 queue with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-003-m-m-1-queue.png)

### Worked Example 3

**Problem.** λ=4/hr and μ=5/hr gives W=1 hr.

**Solution.** For M/M/1, \(W=1/(\mu-\lambda)=1/(5-4)=\mathbf{1\ hr}\). Then \(L=\lambda W=(4\ {\rm hr^{-1}})(1\ {\rm hr})=\mathbf{4\ customers}\). The result becomes large because utilization is \(4/5=0.8\).

---

## 64.4 Finite-Capacity Queues

Finite capacity causes some attempted arrivals to be blocked, reducing effective throughput.

\\[\\lambda_e=\\lambda(1-P_M)\\]

![FIG-03-64-004: Textbook-quality industrial engineering diagram illustrating finite-capacity queues with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-004-finite-capacity-queues.png)

### Worked Example 4

**Problem.** If 10% are blocked, effective throughput is 0.9λ.

**Solution.** With finite capacity, only admitted arrivals contribute to throughput. If \(P_M=0.10\), then \(\lambda_e=\lambda(1-P_M)=0.90\lambda\). For example, an offered \(10\ {\rm customers/hr}\) yields **9 customers/hr** effective throughput.

---

## 64.5 Service-Time Variability

At the same mean service rate, larger service-time variance produces more waiting.

\\[L_q=\\frac{\\lambda^2\\sigma_s^2+\\rho^2}{2(1-\\rho)}\\]

![FIG-03-64-005: Textbook-quality industrial engineering diagram illustrating service-time variability with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-005-service-time-variability.png)

### Worked Example 5

**Problem.** Reducing service-time variability can improve queue performance without changing mean capacity.

**Solution.** At equal mean service time, greater service-time variance increases queueing because long services create more residual work seen by subsequent arrivals. Reducing \(\sigma_s^2\) therefore lowers \(L_q\) in the stated variability-sensitive relation even though \(\mu\) is unchanged.

---

## 64.6 Multiple-Server Queues

Multiple parallel servers share arrivals and often reduce wait time compared with one heavily loaded server.

\\[\\rho=\\frac{\\lambda}{s\\mu}<1\\]

![FIG-03-64-006: Textbook-quality industrial engineering diagram illustrating multiple-server queues with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-006-multiple-server-queues.png)

### Worked Example 6

**Problem.** Two servers at 6/hr each provide 12/hr nominal capacity.

**Solution.** Two servers each serving \(6\ {\rm customers/hr}\) provide \(s\mu=2(6)=\mathbf{12\ customers/hr}\) nominal capacity. The steady-state utilization is \(\rho=\lambda/12\), so a long-run stable model requires \(\lambda<12\ {\rm customers/hr}\).

---

## 64.7 Service-System Design Tradeoffs

Queue design balances staffing/capacity against delay, congestion, and service targets.

\\[\\text{total cost}=\\text{capacity cost}+\\text{waiting cost}\\]

![FIG-03-64-007: Textbook-quality industrial engineering diagram illustrating service-system design tradeoffs with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-64-007-service-system-design-tradeoffs.png)

### Worked Example 7

**Problem.** Adding a server can sharply reduce waiting but may be uneconomic at low demand.

**Solution.** An extra server raises capacity cost but can reduce waiting cost nonlinearly, especially near high utilization. Compare the incremental server cost with the monetary/service value of the reduced \(L_q\), \(W_q\), abandonment, or lost demand rather than minimizing waiting alone.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Queueing Models and Service Systems**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For **Queueing Models and Service Systems**, the FE Reference Handbook formulation and variable definitions govern when supplied. Hillier and Lieberman supports the learned material on **queue stability, Little's Law, M/M/1 behavior, finite capacity, service variability, and multiple servers**. Do not substitute a remembered textbook convention when the problem or Handbook defines a different sign, capacity, or variable basis.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 6; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Hillier, F. S., & Lieberman, G. J. (2021). *Introduction to Operations Research* (11th ed.). McGraw-Hill Education. ISBN 978-1-260-57587-3. Supporting scope: Linear programming, duality/sensitivity, transportation/network models, queueing, inventory, Markov models, and simulation.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Queueing Models and Service Systems**, the model boundary determines what is included in the decision. A valid solution must require stable utilization for steady-state formulas, keep arrival/service units consistent, distinguish offered from effective arrivals, and test waiting results against physical capacity.

16. Units and operational definitions are part of the model, not formatting details. For **Queueing Models and Service Systems**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Queueing Models and Service Systems**. The external sources HILLIER support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Queueing Models and Service Systems** is to let \(\lambda	o0\) and confirm waiting approaches the service-time limit; let \(\lambda	o\mu^-\) in M/M/1 and confirm waiting grows without bound. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §64.1, **Arrival Rate, Service Rate, Utilization, and Stability**, is based on \(\\rho=\\frac{\\lambda}{s\\mu}\\). Interpret the result within the specific assumptions and system boundary of §64.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §64.2, **Little's Law**, is based on \(L=\\lambda W,\\qquad L_q=\\lambda W_q\\). Interpret the result within the specific assumptions and system boundary of §64.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §64.3, **M/M/1 Queue**, is based on \(W=\\frac{1}{\\mu-\\lambda},\\quad L=\\frac{\\lambda}{\\mu-\\lambda}\\). Interpret the result within the specific assumptions and system boundary of §64.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §64.4, **Finite-Capacity Queues**, is based on \(\\lambda_e=\\lambda(1-P_M)\\). Interpret the result within the specific assumptions and system boundary of §64.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §64.5, **Service-Time Variability**, is based on \(L_q=\\frac{\\lambda^2\\sigma_s^2+\\rho^2}{2(1-\\rho)}\\). Interpret the result within the specific assumptions and system boundary of §64.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §64.6, **Multiple-Server Queues**, is based on \(\\rho=\\frac{\\lambda}{s\\mu}<1\\). Interpret the result within the specific assumptions and system boundary of §64.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §64.7, **Service-System Design Tradeoffs**, is based on \(\\text{total cost}=\\text{capacity cost}+\\text{waiting cost}\\). Interpret the result within the specific assumptions and system boundary of §64.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Queueing Models and Service Systems decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Queueing Models and Service Systems.


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

1. **Independent solution for §64.1 — Arrival Rate, Service Rate, Utilization, and Stability.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: For one server, \(\rho=\lambda/\mu=(8\ {\rm hr^{-1}})/(10\ {\rm hr^{-1}})=\mathbf{0.80}\). Because \(\rho<1\), the basic steady-state stability condition is satisfied; 80% is the long-run busy fraction under the model assumptions.

2. **Independent solution for §64.2 — Little's Law.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Little's Law gives \(L=\lambda W=(20\ {\rm customers/hr})(0.25\ {\rm hr})=\mathbf{5\ customers}\). The 0.25 hr is 15 min, and the units reduce correctly to customers.

3. **Independent solution for §64.3 — M/M/1 Queue.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: For M/M/1, \(W=1/(\mu-\lambda)=1/(5-4)=\mathbf{1\ hr}\). Then \(L=\lambda W=(4\ {\rm hr^{-1}})(1\ {\rm hr})=\mathbf{4\ customers}\). The result becomes large because utilization is \(4/5=0.8\).

4. **Independent solution for §64.4 — Finite-Capacity Queues.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: With finite capacity, only admitted arrivals contribute to throughput. If \(P_M=0.10\), then \(\lambda_e=\lambda(1-P_M)=0.90\lambda\). For example, an offered \(10\ {\rm customers/hr}\) yields **9 customers/hr** effective throughput.

5. **Independent solution for §64.5 — Service-Time Variability.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: At equal mean service time, greater service-time variance increases queueing because long services create more residual work seen by subsequent arrivals. Reducing \(\sigma_s^2\) therefore lowers \(L_q\) in the stated variability-sensitive relation even though \(\mu\) is unchanged.

6. **Independent solution for §64.6 — Multiple-Server Queues.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Two servers each serving \(6\ {\rm customers/hr}\) provide \(s\mu=2(6)=\mathbf{12\ customers/hr}\) nominal capacity. The steady-state utilization is \(\rho=\lambda/12\), so a long-run stable model requires \(\lambda<12\ {\rm customers/hr}\).

7. **Independent solution for §64.7 — Service-System Design Tradeoffs.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: An extra server raises capacity cost but can reduce waiting cost nonlinearly, especially near high utilization. Compare the incremental server cost with the monetary/service value of the reduced \(L_q\), \(W_q\), abandonment, or lost demand rather than minimizing waiting alone.

8. For an integrated **Queueing Models and Service Systems** problem, reject any result that violates this chapter-specific screen: require stable utilization for steady-state formulas, keep arrival/service units consistent, distinguish offered from effective arrivals, and test waiting results against physical capacity.

9. For **Queueing Models and Service Systems**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **HILLIER** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: let \(\lambda	o0\) and confirm waiting approaches the service-time limit; let \(\lambda	o\mu^-\) in M/M/1 and confirm waiting grows without bound. The reduced case should behave as stated before the full model is trusted.

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
