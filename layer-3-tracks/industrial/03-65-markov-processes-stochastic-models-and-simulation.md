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

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 65.2 Transition Matrices

State probabilities advance through multiplication by a transition matrix whose rows sum to one.

\\[\\mathbf p_{n+1}=\\mathbf p_nP\\]

![FIG-03-65-002: Textbook-quality industrial engineering diagram illustrating transition matrices with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-002-transition-matrices.png)

### Worked Example 2

**Problem.** Starting from a known state, one-step probabilities equal that row of P.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 65.3 Steady-State Markov Probabilities

A stationary distribution gives long-run state proportions when such a distribution exists and is relevant.

\\[\\boldsymbol\\pi=\\boldsymbol\\pi P,\\quad\\sum_i\\pi_i=1\\]

![FIG-03-65-003: Textbook-quality industrial engineering diagram illustrating steady-state markov probabilities with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-003-steady-state-markov-probabilities.png)

### Worked Example 3

**Problem.** A repairable machine can spend 95% of time operating while still transitioning between states.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 65.4 Pseudo-Random Number Generation

Simulation uses reproducible pseudo-random sequences; seed control supports debugging and comparison.

\\[Z_n=(aZ_{n-1}+C)\\bmod m,\\quad U_n=Z_n/m\\]

![FIG-03-65-004: Textbook-quality industrial engineering diagram illustrating pseudo-random number generation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-004-pseudo-random-number-generation.png)

### Worked Example 4

**Problem.** The same seed and parameters reproduce the same sequence.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 65.5 Inverse-Transform Variate Generation

A uniform random number can be mapped through an inverse CDF to sample another distribution.

\\[X=F^{-1}(U)\\]

![FIG-03-65-005: Textbook-quality industrial engineering diagram illustrating inverse-transform variate generation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-005-inverse-transform-variate-generation.png)

### Worked Example 5

**Problem.** An exponential random variate can be generated from a uniform U using the exponential inverse CDF.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 65.6 Discrete-Event Simulation

Discrete-event simulation advances from event to event while updating queues, resources, and system state.

\\[\\text{clock}\\rightarrow\\text{next event}\\rightarrow\\text{state update}\\]

![FIG-03-65-006: Textbook-quality industrial engineering diagram illustrating discrete-event simulation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-006-discrete-event-simulation.png)

### Worked Example 6

**Problem.** A service model schedules arrival and departure events.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 65.7 Simulation Verification and Validation

Verification asks whether the model was implemented correctly; validation asks whether it represents the real system adequately.

\\[\\bar X\\pm t\\frac{s}{\\sqrt n}\\]

![FIG-03-65-007: Textbook-quality industrial engineering diagram illustrating simulation verification and validation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-65-007-simulation-verification-and-validation.png)

### Worked Example 7

**Problem.** One random replication is not an exact performance prediction.

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

1. Use §65.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §65.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §65.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §65.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §65.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §65.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §65.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 6, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

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
