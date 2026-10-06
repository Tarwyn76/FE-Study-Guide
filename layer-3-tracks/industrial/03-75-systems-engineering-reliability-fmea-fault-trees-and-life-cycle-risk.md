---
chapter: "03-75"
title: "Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-075-01, IND-3-075-02, IND-3-075-03, IND-3-075-04, IND-3-075-05, IND-3-075-06, IND-3-075-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-75: Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** IND-3-074-07 · ECON-2A-005-06

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **75.1** Explain and apply **Requirements, Verification, and Validation**.
* **75.2** Explain and apply **Functional Analysis and Interfaces**.
* **75.3** Explain and apply **Configuration Management and Change Control**.
* **75.4** Explain and apply **FMEA and Risk Prioritization**.
* **75.5** Explain and apply **Fault-Tree Analysis**.
* **75.6** Explain and apply **Series and Parallel Reliability**.
* **75.7** Explain and apply **Availability, Maintainability, and Life-Cycle Risk**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 75.1 Requirements, Verification, and Validation

Requirements should be clear and testable. Verification checks conformance; validation checks fitness for intended use.

\\[Need\\rightarrow Requirement\\rightarrow Design\\rightarrow Verification/Validation\\]

![FIG-03-75-001: Textbook-quality industrial engineering diagram illustrating requirements, verification, and validation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-001-requirements-verification-and-validation.png)

### Worked Example 1

**Problem.** “Easy to use” needs measurable criteria to become a testable requirement.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 75.2 Functional Analysis and Interfaces

Functional decomposition separates what the system must do from how it is implemented and clarifies interfaces.

\\[Mission\\rightarrow Functions\\rightarrow Subfunctions\\rightarrow Components\\]

![FIG-03-75-002: Textbook-quality industrial engineering diagram illustrating functional analysis and interfaces with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-002-functional-analysis-and-interfaces.png)

### Worked Example 2

**Problem.** A power subsystem requirement must specify interfaces to the loads it serves.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 75.3 Configuration Management and Change Control

Configuration management preserves coherent versions and interfaces through controlled change.

\\[Baseline\\rightarrow Change\\ proposal\\rightarrow Impact\\ review\\rightarrow Approved\\ baseline\\]

![FIG-03-75-003: Textbook-quality industrial engineering diagram illustrating configuration management and change control with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-003-configuration-management-and-change-control.png)

### Worked Example 3

**Problem.** Changing a drawing without its interface specification creates inconsistency.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 75.4 FMEA and Risk Prioritization

FMEA identifies failure modes, effects, causes, controls, and actions. RPN is a prioritization aid, not the only decision rule.

\\[RPN=S\\times O\\times D\\]

![FIG-03-75-004: Textbook-quality industrial engineering diagram illustrating fmea and risk prioritization with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-004-fmea-and-risk-prioritization.png)

### Worked Example 4

**Problem.** A severe safety failure deserves attention even when occurrence is low.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 75.5 Fault-Tree Analysis

Fault trees represent top-event logic with AND/OR gates and basic events.

\\[P(A\\cap B)=P(A)P(B)\\text{ for independent events}\\]

![FIG-03-75-005: Textbook-quality industrial engineering diagram illustrating fault-tree analysis with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-005-fault-tree-analysis.png)

### Worked Example 5

**Problem.** An OR gate occurs if either input event occurs.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 75.6 Series and Parallel Reliability

Series systems require all components to work; parallel redundancy can preserve function when one branch fails.

\\[R_s=\\prod_iR_i,\\quad R_p=1-\\prod_i(1-R_i)\\]

![FIG-03-75-006: Textbook-quality industrial engineering diagram illustrating series and parallel reliability with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-006-series-and-parallel-reliability.png)

### Worked Example 6

**Problem.** Two independent 0.9 components in series give reliability 0.81.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 75.7 Availability, Maintainability, and Life-Cycle Risk

Availability depends on both reliability and restoration time. Life-cycle engineering integrates reliability, support, cost, safety, obsolescence, and retirement.

\\[A=\\frac{MTBF}{MTBF+MTTR}\\]

![FIG-03-75-007: Textbook-quality industrial engineering diagram illustrating availability, maintainability, and life-cycle risk with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-007-availability-maintainability-and-life-cycle-risk.png)

### Worked Example 7

**Problem.** Reducing MTTR improves availability even if MTBF is unchanged.

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

Primary source basis: **FE Industrial & Systems specification Area(s) 13; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

Specification-required management/design topics that are not directly tabulated are identified as learned or guide-developed rather than assigned false Handbook pages.

---

## Where This Goes Wrong

**Using systems engineering requirements without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using systems functional analysis without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using configuration management without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using failure modes and effects analysis without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using fault tree analysis without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using system reliability without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using system availability without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| systems engineering requirements | Industrial/systems concept developed in §75.1; apply with the stated model assumptions and decision basis. |
| systems functional analysis | Industrial/systems concept developed in §75.2; apply with the stated model assumptions and decision basis. |
| configuration management | Industrial/systems concept developed in §75.3; apply with the stated model assumptions and decision basis. |
| failure modes and effects analysis | Industrial/systems concept developed in §75.4; apply with the stated model assumptions and decision basis. |
| fault tree analysis | Industrial/systems concept developed in §75.5; apply with the stated model assumptions and decision basis. |
| system reliability | Industrial/systems concept developed in §75.6; apply with the stated model assumptions and decision basis. |
| system availability | Industrial/systems concept developed in §75.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **systems engineering requirements** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **systems functional analysis** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **configuration management** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **failure modes and effects analysis** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **fault tree analysis** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **system reliability** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **system availability** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **systems engineering requirements**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **systems functional analysis**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **configuration management**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **failure modes and effects analysis**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **fault tree analysis**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **system reliability**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **system availability**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **systems engineering requirements**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **systems functional analysis**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **configuration management**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **failure modes and effects analysis**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **fault tree analysis**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **system reliability**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **system availability**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **systems engineering requirements**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **systems functional analysis**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **systems engineering requirements** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **systems functional analysis** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **configuration management** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **failure modes and effects analysis** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **fault tree analysis** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **system reliability** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **system availability** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **systems engineering requirements**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **systems functional analysis**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **configuration management**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **failure modes and effects analysis**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **fault tree analysis**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **system reliability**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **system availability**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. “Easy to use” needs measurable criteria to become a testable requirement.

2. A power subsystem requirement must specify interfaces to the loads it serves.

3. Changing a drawing without its interface specification creates inconsistency.

4. A severe safety failure deserves attention even when occurrence is low.

5. An OR gate occurs if either input event occurs.

6. Two independent 0.9 components in series give reliability 0.81.

7. Reducing MTTR improves availability even if MTBF is unchanged.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §75.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §75.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §75.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §75.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §75.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §75.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §75.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 13, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 13.

- **systems engineering requirements:** Requirements, Verification, and Validation
- **systems functional analysis:** Functional Analysis and Interfaces
- **configuration management:** Configuration Management and Change Control
- **failure modes and effects analysis:** FMEA and Risk Prioritization
- **fault tree analysis:** Fault-Tree Analysis
- **system reliability:** Series and Parallel Reliability
- **system availability:** Availability, Maintainability, and Life-Cycle Risk

---

## What's Next

**Mechanical Engineering begins at 03-76**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
