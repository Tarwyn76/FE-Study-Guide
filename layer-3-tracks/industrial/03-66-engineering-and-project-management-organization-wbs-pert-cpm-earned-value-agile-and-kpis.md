---
chapter: "03-66"
title: "Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-066-01, IND-3-066-02, IND-3-066-03, IND-3-066-04, IND-3-066-05, IND-3-066-06, IND-3-066-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-66: Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** ECON-2A-005-06 · CIV-3-030-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **66.1** Explain and apply **Organization, Responsibility, and Motivation**.
* **66.2** Explain and apply **Work Breakdown Structures**.
* **66.3** Explain and apply **Critical Path Method**.
* **66.4** Explain and apply **PERT Duration and Uncertainty**.
* **66.5** Explain and apply **Earned Value Management**.
* **66.6** Explain and apply **Agile Project Management**.
* **66.7** Explain and apply **KPIs and Balanced Scorecards**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 66.1 Organization, Responsibility, and Motivation

Functional, projectized, and matrix organizations distribute authority differently.

\\[\\text{strategy}\\rightarrow\\text{structure}\\rightarrow\\text{responsibility}\\]

![FIG-03-66-001: Textbook-quality industrial engineering diagram illustrating organization, responsibility, and motivation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-001-organization-responsibility-and-motivation.png)

### Worked Example 1

**Problem.** In a matrix, a project manager can share authority with functional managers.

**Solution.** In a matrix organization, the project manager coordinates scope, schedule, integration, and project priorities while functional managers retain discipline resources and technical authority. The shared-authority arrangement must therefore define escalation and responsibility rather than assume a single chain of command.

---

## 66.2 Work Breakdown Structures

A WBS decomposes project scope into manageable deliverables and work packages.

\\[\\text{scope}\\rightarrow\\text{deliverables}\\rightarrow\\text{work packages}\\]

![FIG-03-66-002: Textbook-quality industrial engineering diagram illustrating work breakdown structures with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-002-work-breakdown-structures.png)

### Worked Example 2

**Problem.** Design, procurement, installation, and commissioning can be separate deliverables.

**Solution.** A WBS decomposes **scope**, not calendar time. For an equipment project, design, procurement, installation, and commissioning can each be deliverables, then be decomposed into work packages that are small enough to estimate, assign, monitor, and control.

---

## 66.3 Critical Path Method

CPM identifies the longest path through a deterministic activity network.

\\[T=\\sum_{(i,j)\\in CP}d_{ij}\\]

![FIG-03-66-003: Textbook-quality industrial engineering diagram illustrating critical path method with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-003-critical-path-method.png)

### Worked Example 3

**Problem.** Zero-total-float activities lie on at least one critical path.

**Solution.** The project duration is governed by the longest-duration path through the precedence network. Activities with zero total float lie on at least one critical path; delaying one without offsetting action delays the current project completion date.

---

## 66.4 PERT Duration and Uncertainty

PERT uses optimistic, most-likely, and pessimistic estimates to approximate activity uncertainty.

\\[\\mu=\\frac{a+4m+b}{6},\\quad\\sigma=\\frac{b-a}{6}\\]

![FIG-03-66-004: Textbook-quality industrial engineering diagram illustrating pert duration and uncertainty with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-004-pert-duration-and-uncertainty.png)

### Worked Example 4

**Problem.** a=2, m=5, b=8 gives expected duration 5.

**Solution.** PERT expected duration is \(\mu=(a+4m+b)/6=(2+4(5)+8)/6=30/6=\mathbf{5\ days}\). The standard deviation is \(\sigma=(8-2)/6=\mathbf{1\ day}\) under the three-point approximation.

---

## 66.5 Earned Value Management

Earned value separates planned work, completed work value, and actual cost.

\\[CV=EV-AC,\\quad SV=EV-PV\\]

![FIG-03-66-005: Textbook-quality industrial engineering diagram illustrating earned value management with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-005-earned-value-management.png)

### Worked Example 5

**Problem.** EV=80 and AC=100 gives CV=-20.

**Solution.** Cost variance is \(CV=EV-AC=80-100=\mathbf{-20}\). A negative CV means the value of completed work is 20 cost units below the amount spent—i.e., the project is over cost relative to earned value at that status date.

---

## 66.6 Agile Project Management

Agile methods use short iterative cycles and frequent stakeholder feedback while retaining quality and risk obligations.

\\[\\text{iteration}\\rightarrow\\text{increment}\\rightarrow\\text{feedback}\\]

![FIG-03-66-006: Textbook-quality industrial engineering diagram illustrating agile project management with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-006-agile-project-management.png)

### Worked Example 6

**Problem.** A sprint review can expose changed requirements early.

**Solution.** A sprint review creates a short feedback loop: stakeholders inspect the increment, compare it with current needs, and update the backlog or priorities. The benefit is earlier discovery of changed requirements, not elimination of planning or governance.

---

## 66.7 KPIs and Balanced Scorecards

Balanced performance measurement avoids optimizing cost or throughput while ignoring quality, people, or customer outcomes.

\\[\\text{metric}\\rightarrow\\text{objective}\\rightarrow\\text{decision}\\]

![FIG-03-66-007: Textbook-quality industrial engineering diagram illustrating kpis and balanced scorecards with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-66-007-kpis-and-balanced-scorecards.png)

### Worked Example 7

**Problem.** A throughput increase paired with higher defects is not an unqualified improvement.

**Solution.** A throughput KPI cannot be interpreted alone. If throughput rises while defect rate, injury risk, overtime, or customer returns worsen, the balanced performance picture may have deteriorated. Link each metric to the objective and monitor counter-metrics.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For this chapter, the FE Reference Handbook relation and variable definitions control whenever the Handbook supplies them. Use the external source set **PMBOK8** only for specification-required learned material not fully developed in the Handbook.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 7; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Project Management Institute. (2025). *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)* (8th ed.), including *The Standard for Project Management*. ANSI/PMI 99-001-2025. Supporting scope: Project governance, scope/WBS, scheduling, earned value/performance measurement, adaptive approaches, and metrics.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using engineering management organization without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using work breakdown structure without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial critical path method without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using PERT project duration without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial earned value without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using agile engineering project management without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using management performance measurement without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| engineering management organization | Industrial/systems concept developed in §66.1; apply with the stated model assumptions and decision basis. |
| work breakdown structure | Industrial/systems concept developed in §66.2; apply with the stated model assumptions and decision basis. |
| industrial critical path method | Industrial/systems concept developed in §66.3; apply with the stated model assumptions and decision basis. |
| PERT project duration | Industrial/systems concept developed in §66.4; apply with the stated model assumptions and decision basis. |
| industrial earned value | Industrial/systems concept developed in §66.5; apply with the stated model assumptions and decision basis. |
| agile engineering project management | Industrial/systems concept developed in §66.6; apply with the stated model assumptions and decision basis. |
| management performance measurement | Industrial/systems concept developed in §66.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **engineering management organization** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **work breakdown structure** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **industrial critical path method** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **PERT project duration** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **industrial earned value** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **agile engineering project management** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **management performance measurement** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **engineering management organization**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **work breakdown structure**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial critical path method**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **PERT project duration**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial earned value**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **agile engineering project management**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **management performance measurement**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **engineering management organization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **work breakdown structure**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **industrial critical path method**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **PERT project duration**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **industrial earned value**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **agile engineering project management**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **management performance measurement**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **engineering management organization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **work breakdown structure**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **engineering management organization** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **work breakdown structure** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **industrial critical path method** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **PERT project duration** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **industrial earned value** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **agile engineering project management** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **management performance measurement** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **engineering management organization**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **work breakdown structure**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **industrial critical path method**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **PERT project duration**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **industrial earned value**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **agile engineering project management**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **management performance measurement**, verify data basis, units, capacity/probability conditions, and operational feasibility.

15. In **Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs**, the model boundary determines what is included in the decision. A valid solution must trace scope to work packages, respect precedence, distinguish EV/PV/AC, state the schedule/cost status date, and avoid treating agile feedback or KPIs as substitutes for governance.

16. Units and operational definitions are part of the model, not formatting details. For **Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs**. The external sources PMBOK8 support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs** is to set EV=AC and confirm cost variance is zero; remove a critical-path activity duration and confirm project duration cannot increase. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §66.1, **Organization, Responsibility, and Motivation**, is based on \(\\text{strategy}\\rightarrow\\text{structure}\\rightarrow\\text{responsibility}\\). Interpret the result within the specific assumptions and system boundary of §66.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §66.2, **Work Breakdown Structures**, is based on \(\\text{scope}\\rightarrow\\text{deliverables}\\rightarrow\\text{work packages}\\). Interpret the result within the specific assumptions and system boundary of §66.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §66.3, **Critical Path Method**, is based on \(T=\\sum_{(i,j)\\in CP}d_{ij}\\). Interpret the result within the specific assumptions and system boundary of §66.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §66.4, **PERT Duration and Uncertainty**, is based on \(\\mu=\\frac{a+4m+b}{6},\\quad\\sigma=\\frac{b-a}{6}\\). Interpret the result within the specific assumptions and system boundary of §66.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §66.5, **Earned Value Management**, is based on \(CV=EV-AC,\\quad SV=EV-PV\\). Interpret the result within the specific assumptions and system boundary of §66.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §66.6, **Agile Project Management**, is based on \(\\text{iteration}\\rightarrow\\text{increment}\\rightarrow\\text{feedback}\\). Interpret the result within the specific assumptions and system boundary of §66.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §66.7, **KPIs and Balanced Scorecards**, is based on \(\\text{metric}\\rightarrow\\text{objective}\\rightarrow\\text{decision}\\). Interpret the result within the specific assumptions and system boundary of §66.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs.


---

## Practice Problems

1. In a matrix, a project manager can share authority with functional managers.

2. Design, procurement, installation, and commissioning can be separate deliverables.

3. Zero-total-float activities lie on at least one critical path.

4. a=2, m=5, b=8 gives expected duration 5.

5. EV=80 and AC=100 gives CV=-20.

6. A sprint review can expose changed requirements early.

7. A throughput increase paired with higher defects is not an unqualified improvement.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. **Independent solution for §66.1 — Organization, Responsibility, and Motivation.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: In a matrix organization, the project manager coordinates scope, schedule, integration, and project priorities while functional managers retain discipline resources and technical authority. The shared-authority arrangement must therefore define escalation and responsibility rather than assume a single chain of command.

2. **Independent solution for §66.2 — Work Breakdown Structures.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A WBS decomposes **scope**, not calendar time. For an equipment project, design, procurement, installation, and commissioning can each be deliverables, then be decomposed into work packages that are small enough to estimate, assign, monitor, and control.

3. **Independent solution for §66.3 — Critical Path Method.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: The project duration is governed by the longest-duration path through the precedence network. Activities with zero total float lie on at least one critical path; delaying one without offsetting action delays the current project completion date.

4. **Independent solution for §66.4 — PERT Duration and Uncertainty.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: PERT expected duration is \(\mu=(a+4m+b)/6=(2+4(5)+8)/6=30/6=\mathbf{5\ days}\). The standard deviation is \(\sigma=(8-2)/6=\mathbf{1\ day}\) under the three-point approximation.

5. **Independent solution for §66.5 — Earned Value Management.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Cost variance is \(CV=EV-AC=80-100=\mathbf{-20}\). A negative CV means the value of completed work is 20 cost units below the amount spent—i.e., the project is over cost relative to earned value at that status date.

6. **Independent solution for §66.6 — Agile Project Management.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A sprint review creates a short feedback loop: stakeholders inspect the increment, compare it with current needs, and update the backlog or priorities. The benefit is earlier discovery of changed requirements, not elimination of planning or governance.

7. **Independent solution for §66.7 — KPIs and Balanced Scorecards.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A throughput KPI cannot be interpreted alone. If throughput rises while defect rate, injury risk, overtime, or customer returns worsen, the balanced performance picture may have deteriorated. Link each metric to the objective and monitor counter-metrics.

8. For an integrated **Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs** problem, reject any result that violates this chapter-specific screen: trace scope to work packages, respect precedence, distinguish EV/PV/AC, state the schedule/cost status date, and avoid treating agile feedback or KPIs as substitutes for governance.

9. For **Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **PMBOK8** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: set EV=AC and confirm cost variance is zero; remove a critical-path activity duration and confirm project duration cannot increase. The reduced case should behave as stated before the full model is trusted.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 7.

- **engineering management organization:** Organization, Responsibility, and Motivation
- **work breakdown structure:** Work Breakdown Structures
- **industrial critical path method:** Critical Path Method
- **PERT project duration:** PERT Duration and Uncertainty
- **industrial earned value:** Earned Value Management
- **agile engineering project management:** Agile Project Management
- **management performance measurement:** KPIs and Balanced Scorecards

---

## What's Next

**Chapter 03-67: Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
