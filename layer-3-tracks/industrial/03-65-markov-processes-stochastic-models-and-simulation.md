---
chapter: "03-65"
title: "Markov Processes, Stochastic Models, and Simulation"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-065-01, IND-3-065-02, IND-3-065-03, IND-3-065-04, IND-3-065-05, IND-3-065-06, IND-3-065-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-65: Markov Processes, Stochastic Models, and Simulation

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** MATH-1D-033-07 · IND-3-064-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Markov Processes, Stochastic Models, and Simulation** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **65.1** Explain and apply **Markov States and Transition Probabilities**.
* **65.2** Explain and apply **Transition Matrices**.
* **65.3** Explain and apply **Steady-State Markov Probabilities**.
* **65.4** Explain and apply **Pseudo-Random Number Generation**.
* **65.5** Explain and apply **Inverse-Transform Variate Generation**.
* **65.6** Explain and apply **Discrete-Event Simulation**.
* **65.7** Explain and apply **Simulation Verification and Validation**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 65.1 Markov States and Transition Probabilities

A Markov model represents a system as states connected by transition probabilities under a memoryless assumption.

\\[P_{ij}=P(X_{n+1}=j\\mid X_n=i)\\]

![FIG-03-65-001: Textbook-quality industrial engineering diagram illustrating markov states and transition probabilities with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-001-markov-states-and-transition-probabilities.png)

### Worked Example 1

**Problem.** A machine can be operating, degraded, or failed.

**Solution.** A Markov state must contain enough information for the next-step probabilities to depend only on the current state. For a machine, states such as **operating, degraded, failed** are valid only if transition behavior does not require hidden age/history information that has been omitted.

---

## 65.2 Transition Matrices

State probabilities advance through multiplication by a transition matrix whose rows sum to one.

\\[\\mathbf p_{n+1}=\\mathbf p_nP\\]

![FIG-03-65-002: Textbook-quality industrial engineering diagram illustrating transition matrices with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-002-transition-matrices.png)

### Worked Example 2

**Problem.** Starting from a known state, one-step probabilities equal that row of P.

**Solution.** If the system starts certainly in state \(i\), the initial vector has a 1 in position \(i\). Multiplying \(\mathbf p_0P\) therefore selects row \(i\) of \(P\), so the one-step state probabilities are exactly the transition probabilities from that starting state.

---

## 65.3 Steady-State Markov Probabilities

A stationary distribution gives long-run state proportions when such a distribution exists and is relevant.

\\[\\boldsymbol\\pi=\\boldsymbol\\pi P,\\quad\\sum_i\\pi_i=1\\]

![FIG-03-65-003: Textbook-quality industrial engineering diagram illustrating steady-state markov probabilities with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-003-steady-state-markov-probabilities.png)

### Worked Example 3

**Problem.** A repairable machine can spend 95% of time operating while still transitioning between states.

**Solution.** Steady-state probabilities satisfy \(\boldsymbol\pi=\boldsymbol\pi P\) and sum to 1. A result such as \(\pi_{operating}=0.95\) describes the long-run fraction of time in that state; it does **not** mean the machine never visits degraded or failed states.

---

## 65.4 Pseudo-Random Number Generation

Simulation uses reproducible pseudo-random sequences; seed control supports debugging and comparison.

\\[Z_n=(aZ_{n-1}+C)\\bmod m,\\quad U_n=Z_n/m\\]

![FIG-03-65-004: Textbook-quality industrial engineering diagram illustrating pseudo-random number generation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-004-pseudo-random-number-generation.png)

### Worked Example 4

**Problem.** The same seed and parameters reproduce the same sequence.

**Solution.** A linear congruential generator is deterministic once \(a,C,m,Z_0\) are fixed. Reusing the same seed \(Z_0\) and parameters produces the **same sequence**, which is useful for reproducible debugging but is not evidence of physical randomness.

---

## 65.5 Inverse-Transform Variate Generation

A uniform random number can be mapped through an inverse CDF to sample another distribution.

\\[X=F^{-1}(U)\\]

![FIG-03-65-005: Textbook-quality industrial engineering diagram illustrating inverse-transform variate generation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-005-inverse-transform-variate-generation.png)

### Worked Example 5

**Problem.** An exponential random variate can be generated from a uniform U using the exponential inverse CDF.

**Solution.** For an exponential distribution with rate \(\lambda\), \(F(x)=1-e^{-\lambda x}\). Setting \(U=F(X)\) gives \(X=-\ln(1-U)/\lambda\), commonly written \(X=-\ln U/\lambda\) because \(1-U\) is also uniform on (0,1).

---

## 65.6 Discrete-Event Simulation

Discrete-event simulation advances from event to event while updating queues, resources, and system state.

\\[\\text{clock}\\rightarrow\\text{next event}\\rightarrow\\text{state update}\\]

![FIG-03-65-006: Textbook-quality industrial engineering diagram illustrating discrete-event simulation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-006-discrete-event-simulation.png)

### Worked Example 6

**Problem.** A service model schedules arrival and departure events.

**Solution.** A discrete-event simulation advances the clock directly to the earliest scheduled event. For a queue, an arrival updates queue/server state and schedules a future arrival; when service begins it schedules a departure. The event list therefore drives state transitions without simulating every intervening instant.

---

## 65.7 Simulation Verification and Validation

Verification asks whether the model was implemented correctly; validation asks whether it represents the real system adequately.

\\[\\bar X\\pm t\\frac{s}{\\sqrt n}\\]

![FIG-03-65-007: Textbook-quality industrial engineering diagram illustrating simulation verification and validation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-007-simulation-verification-and-validation.png)

### Worked Example 7

**Problem.** One random replication is not an exact performance prediction.

**Solution.** One replication is one random draw from the simulation experiment. Estimate performance across independent replications using \(\bar X\), \(s\), and a confidence interval such as \(\bar X\pm t\,s/\sqrt n\); precision improves by increasing appropriate replication effort, not by treating one run as exact.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Markov Processes, Stochastic Models, and Simulation**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For this chapter, the FE Reference Handbook relation and variable definitions control whenever the Handbook supplies them. Use the external source set **HILLIER, LAW** only for specification-required learned material not fully developed in the Handbook.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 6; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Hillier, F. S., & Lieberman, G. J. (2021). *Introduction to Operations Research* (11th ed.). McGraw-Hill Education. ISBN 978-1-260-57587-3. Supporting scope: Linear programming, duality/sensitivity, transportation/network models, queueing, inventory, Markov models, and simulation.
- Law, A. M. (2024). *Simulation Modeling and Analysis* (6th ed.). McGraw-Hill. Print ISBN 978-1-264-26824-5. Supporting scope: Discrete-event simulation, random-number/variate generation, input modeling, verification/validation, and output analysis.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using Markov state model without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using Markov transition matrix without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using Markov steady state without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using linear congruential generator without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using inverse transform simulation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using discrete-event simulation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using simulation study validation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| Markov state model | Industrial/systems concept developed in §65.1; apply with the stated model assumptions and decision basis. |
| Markov transition matrix | Industrial/systems concept developed in §65.2; apply with the stated model assumptions and decision basis. |
| Markov steady state | Industrial/systems concept developed in §65.3; apply with the stated model assumptions and decision basis. |
| linear congruential generator | Industrial/systems concept developed in §65.4; apply with the stated model assumptions and decision basis. |
| inverse transform simulation | Industrial/systems concept developed in §65.5; apply with the stated model assumptions and decision basis. |
| discrete-event simulation | Industrial/systems concept developed in §65.6; apply with the stated model assumptions and decision basis. |
| simulation study validation | Industrial/systems concept developed in §65.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **Markov state model** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **Markov transition matrix** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **Markov steady state** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **linear congruential generator** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **inverse transform simulation** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **discrete-event simulation** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **simulation study validation** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **Markov state model**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **Markov transition matrix**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **Markov steady state**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **linear congruential generator**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **inverse transform simulation**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **discrete-event simulation**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **simulation study validation**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **Markov state model**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **Markov transition matrix**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **Markov steady state**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **linear congruential generator**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **inverse transform simulation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **discrete-event simulation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **simulation study validation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **Markov state model**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **Markov transition matrix**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **Markov state model** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **Markov transition matrix** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **Markov steady state** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **linear congruential generator** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **inverse transform simulation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **discrete-event simulation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **simulation study validation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **Markov state model**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **Markov transition matrix**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **Markov steady state**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **linear congruential generator**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **inverse transform simulation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **discrete-event simulation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **simulation study validation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

15. In **Markov Processes, Stochastic Models, and Simulation**, the model boundary determines what is included in the decision. A valid solution must confirm transition rows sum to one, probabilities stay within 0–1, random streams are reproducible when intended, warm-up/replication choices are adequate, and the simulated logic matches the conceptual model.

16. Units and operational definitions are part of the model, not formatting details. For **Markov Processes, Stochastic Models, and Simulation**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Markov Processes, Stochastic Models, and Simulation**. The external sources HILLIER, LAW support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Markov Processes, Stochastic Models, and Simulation** is to sum every transition row to 1 and reuse the same random seed to confirm the same pseudo-random sequence is reproduced. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §65.1, **Markov States and Transition Probabilities**, is based on \(P_{ij}=P(X_{n+1}=j\\mid X_n=i)\\). Interpret the result within the specific assumptions and system boundary of §65.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §65.2, **Transition Matrices**, is based on \(\\mathbf p_{n+1}=\\mathbf p_nP\\). Interpret the result within the specific assumptions and system boundary of §65.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §65.3, **Steady-State Markov Probabilities**, is based on \(\\boldsymbol\\pi=\\boldsymbol\\pi P,\\quad\\sum_i\\pi_i=1\\). Interpret the result within the specific assumptions and system boundary of §65.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §65.4, **Pseudo-Random Number Generation**, is based on \(Z_n=(aZ_{n-1}+C)\\bmod m,\\quad U_n=Z_n/m\\). Interpret the result within the specific assumptions and system boundary of §65.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §65.5, **Inverse-Transform Variate Generation**, is based on \(X=F^{-1}(U)\\). Interpret the result within the specific assumptions and system boundary of §65.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §65.6, **Discrete-Event Simulation**, is based on \(\\text{clock}\\rightarrow\\text{next event}\\rightarrow\\text{state update}\\). Interpret the result within the specific assumptions and system boundary of §65.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §65.7, **Simulation Verification and Validation**, is based on \(\\bar X\\pm t\\frac{s}{\\sqrt n}\\). Interpret the result within the specific assumptions and system boundary of §65.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Markov Processes, Stochastic Models, and Simulation decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Markov Processes, Stochastic Models, and Simulation.


---

## Practice Problems

1. A machine can be operating, degraded, or failed.

2. Starting from a known state, one-step probabilities equal that row of P.

3. A repairable machine can spend 95% of time operating while still transitioning between states.

4. The same seed and parameters reproduce the same sequence.

5. An exponential random variate can be generated from a uniform U using the exponential inverse CDF.

6. A service model schedules arrival and departure events.

7. One random replication is not an exact performance prediction.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. **Independent solution for §65.1 — Markov States and Transition Probabilities.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A Markov state must contain enough information for the next-step probabilities to depend only on the current state. For a machine, states such as **operating, degraded, failed** are valid only if transition behavior does not require hidden age/history information that has been omitted.

2. **Independent solution for §65.2 — Transition Matrices.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: If the system starts certainly in state \(i\), the initial vector has a 1 in position \(i\). Multiplying \(\mathbf p_0P\) therefore selects row \(i\) of \(P\), so the one-step state probabilities are exactly the transition probabilities from that starting state.

3. **Independent solution for §65.3 — Steady-State Markov Probabilities.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Steady-state probabilities satisfy \(\boldsymbol\pi=\boldsymbol\pi P\) and sum to 1. A result such as \(\pi_{operating}=0.95\) describes the long-run fraction of time in that state; it does **not** mean the machine never visits degraded or failed states.

4. **Independent solution for §65.4 — Pseudo-Random Number Generation.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A linear congruential generator is deterministic once \(a,C,m,Z_0\) are fixed. Reusing the same seed \(Z_0\) and parameters produces the **same sequence**, which is useful for reproducible debugging but is not evidence of physical randomness.

5. **Independent solution for §65.5 — Inverse-Transform Variate Generation.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: For an exponential distribution with rate \(\lambda\), \(F(x)=1-e^{-\lambda x}\). Setting \(U=F(X)\) gives \(X=-\ln(1-U)/\lambda\), commonly written \(X=-\ln U/\lambda\) because \(1-U\) is also uniform on (0,1).

6. **Independent solution for §65.6 — Discrete-Event Simulation.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A discrete-event simulation advances the clock directly to the earliest scheduled event. For a queue, an arrival updates queue/server state and schedules a future arrival; when service begins it schedules a departure. The event list therefore drives state transitions without simulating every intervening instant.

7. **Independent solution for §65.7 — Simulation Verification and Validation.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: One replication is one random draw from the simulation experiment. Estimate performance across independent replications using \(\bar X\), \(s\), and a confidence interval such as \(\bar X\pm t\,s/\sqrt n\); precision improves by increasing appropriate replication effort, not by treating one run as exact.

8. For an integrated **Markov Processes, Stochastic Models, and Simulation** problem, reject any result that violates this chapter-specific screen: confirm transition rows sum to one, probabilities stay within 0–1, random streams are reproducible when intended, warm-up/replication choices are adequate, and the simulated logic matches the conceptual model.

9. For **Markov Processes, Stochastic Models, and Simulation**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **HILLIER, LAW** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: sum every transition row to 1 and reuse the same random seed to confirm the same pseudo-random sequence is reproduced. The reduced case should behave as stated before the full model is trusted.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 6.

- **Markov state model:** Markov States and Transition Probabilities
- **Markov transition matrix:** Transition Matrices
- **Markov steady state:** Steady-State Markov Probabilities
- **linear congruential generator:** Pseudo-Random Number Generation
- **inverse transform simulation:** Inverse-Transform Variate Generation
- **discrete-event simulation:** Discrete-Event Simulation
- **simulation study validation:** Simulation Verification and Validation

---

## What's Next

**Chapter 03-66: Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
