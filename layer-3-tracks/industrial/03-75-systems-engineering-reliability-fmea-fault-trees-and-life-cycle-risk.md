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

**Solution.** 'Easy to use' is not directly verifiable. Convert the need into measurable requirements such as task-completion time, error rate, training limit, accessibility criterion, or user-success percentage under defined conditions, then trace verification evidence back to each requirement.

---

## 75.2 Functional Analysis and Interfaces

Functional decomposition separates what the system must do from how it is implemented and clarifies interfaces.

\\[Mission\\rightarrow Functions\\rightarrow Subfunctions\\rightarrow Components\\]

![FIG-03-75-002: Textbook-quality industrial engineering diagram illustrating functional analysis and interfaces with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-002-functional-analysis-and-interfaces.png)

### Worked Example 2

**Problem.** A power subsystem requirement must specify interfaces to the loads it serves.

**Solution.** Functional analysis decomposes mission capability into functions and subfunctions before allocating them to solution elements. Interfaces must specify what crosses the boundary—power, data, material, mechanical loads, timing, environment, or other exchanges—so local designs remain compatible.

---

## 75.3 Configuration Management and Change Control

Configuration management preserves coherent versions and interfaces through controlled change.

\\[Baseline\\rightarrow Change\\ proposal\\rightarrow Impact\\ review\\rightarrow Approved\\ baseline\\]

![FIG-03-75-003: Textbook-quality industrial engineering diagram illustrating configuration management and change control with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-003-configuration-management-and-change-control.png)

### Worked Example 3

**Problem.** Changing a drawing without its interface specification creates inconsistency.

**Solution.** Configuration management preserves consistency among requirements, interfaces, drawings, software, test evidence, and approved baselines. A drawing change that bypasses impact review can create an interface mismatch even if the changed component itself is correct.

---

## 75.4 FMEA and Risk Prioritization

FMEA identifies failure modes, effects, causes, controls, and actions. RPN is a prioritization aid, not the only decision rule.

\\[RPN=S\\times O\\times D\\]

![FIG-03-75-004: Textbook-quality industrial engineering diagram illustrating fmea and risk prioritization with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-004-fmea-and-risk-prioritization.png)

### Worked Example 4

**Problem.** A severe safety failure deserves attention even when occurrence is low.

**Solution.** An RPN is one possible prioritization aid, \(RPN=S\times O\times D\), but severity must not be hidden by multiplication. IEC 60812 explicitly permits different prioritization approaches; a low-occurrence catastrophic hazard can still require action despite a moderate numeric RPN.

---

## 75.5 Fault-Tree Analysis

Fault trees represent top-event logic with AND/OR gates and basic events.

\\[P(A\\cap B)=P(A)P(B)\\text{ for independent events}\\]

![FIG-03-75-005: Textbook-quality industrial engineering diagram illustrating fault-tree analysis with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-005-fault-tree-analysis.png)

### Worked Example 5

**Problem.** An OR gate occurs if either input event occurs.

**Solution.** For independent basic events A and B, an AND gate probability is \(P(A\cap B)=P(A)P(B)\). An OR gate occurs if either input occurs; for independent inputs its exact probability is \(1-[1-P(A)][1-P(B)]\), not simply the sum when overlap is non-negligible.

---

## 75.6 Series and Parallel Reliability

Series systems require all components to work; parallel redundancy can preserve function when one branch fails.

\\[R_s=\\prod_iR_i,\\quad R_p=1-\\prod_i(1-R_i)\\]

![FIG-03-75-006: Textbook-quality industrial engineering diagram illustrating series and parallel reliability with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-006-series-and-parallel-reliability.png)

### Worked Example 6

**Problem.** Two independent 0.9 components in series give reliability 0.81.

**Solution.** Two independent components of reliability 0.9 in series give \(R_s=0.9(0.9)=\mathbf{0.81}\). The same two in active parallel give \(R_p=1-(0.1)(0.1)=\mathbf{0.99}\), assuming either component can satisfy the function and failures are independent.

---

## 75.7 Availability, Maintainability, and Life-Cycle Risk

Availability depends on both reliability and restoration time. Life-cycle engineering integrates reliability, support, cost, safety, obsolescence, and retirement.

\\[A=\\frac{MTBF}{MTBF+MTTR}\\]

![FIG-03-75-007: Textbook-quality industrial engineering diagram illustrating availability, maintainability, and life-cycle risk with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-75-007-availability-maintainability-and-life-cycle-risk.png)

### Worked Example 7

**Problem.** Reducing MTTR improves availability even if MTBF is unchanged.

**Solution.** Availability is \(A=MTBF/(MTBF+MTTR)\). Reducing MTTR lowers the downtime term, so availability increases even if MTBF is unchanged. Life-cycle risk also depends on failure consequences, support resources, detection, maintenance policy, logistics, and changing operational context.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For this chapter, the FE Reference Handbook relation and variable definitions control whenever the Handbook supplies them. Use the external source set **INCOSE5, IEC60812, IEC61025** only for specification-required learned material not fully developed in the Handbook.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 13; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- INCOSE. (2023). *Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities* (5th ed.). Wiley. ISBN 978-1-119-81429-0. Supporting scope: Requirements, lifecycle processes, verification/validation, interfaces, configuration, risk, reliability/maintainability integration, and systems engineering practice.
- IEC. (2018). *Failure modes and effects analysis (FMEA and FMECA)* (IEC 60812:2018). Supporting scope: Planning, performing, documenting, maintaining, and prioritizing FMEA/FMECA analyses.
- IEC. (2006). *Fault tree analysis (FTA)* (IEC 61025:2006, Ed. 2.0; stability date 2029). Supporting scope: Fault-tree-analysis assumptions, events, gates, failure modes, symbols, and analysis procedure.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk**, the model boundary determines what is included in the decision. A valid solution must make requirements measurable and traceable, preserve interface/configuration consistency, treat FMEA/FTA assumptions explicitly, avoid assuming failure independence without basis, and distinguish reliability from availability.

16. Units and operational definitions are part of the model, not formatting details. For **Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk**. The external sources INCOSE5, IEC60812, IEC61025 support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk** is to set MTTR to zero and confirm ideal inherent availability approaches 1; set one series component reliability to zero and confirm series-system reliability becomes zero. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §75.1, **Requirements, Verification, and Validation**, is based on \(Need\\rightarrow Requirement\\rightarrow Design\\rightarrow Verification/Validation\\). Interpret the result within the specific assumptions and system boundary of §75.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §75.2, **Functional Analysis and Interfaces**, is based on \(Mission\\rightarrow Functions\\rightarrow Subfunctions\\rightarrow Components\\). Interpret the result within the specific assumptions and system boundary of §75.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §75.3, **Configuration Management and Change Control**, is based on \(Baseline\\rightarrow Change\\ proposal\\rightarrow Impact\\ review\\rightarrow Approved\\ baseline\\). Interpret the result within the specific assumptions and system boundary of §75.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §75.4, **FMEA and Risk Prioritization**, is based on \(RPN=S\\times O\\times D\\). Interpret the result within the specific assumptions and system boundary of §75.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §75.5, **Fault-Tree Analysis**, is based on \(P(A\\cap B)=P(A)P(B)\\text{ for independent events}\\). Interpret the result within the specific assumptions and system boundary of §75.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §75.6, **Series and Parallel Reliability**, is based on \(R_s=\\prod_iR_i,\\quad R_p=1-\\prod_i(1-R_i)\\). Interpret the result within the specific assumptions and system boundary of §75.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §75.7, **Availability, Maintainability, and Life-Cycle Risk**, is based on \(A=\\frac{MTBF}{MTBF+MTTR}\\). Interpret the result within the specific assumptions and system boundary of §75.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk.


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

1. **Independent solution for §75.1 — Requirements, Verification, and Validation.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: 'Easy to use' is not directly verifiable. Convert the need into measurable requirements such as task-completion time, error rate, training limit, accessibility criterion, or user-success percentage under defined conditions, then trace verification evidence back to each requirement.

2. **Independent solution for §75.2 — Functional Analysis and Interfaces.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Functional analysis decomposes mission capability into functions and subfunctions before allocating them to solution elements. Interfaces must specify what crosses the boundary—power, data, material, mechanical loads, timing, environment, or other exchanges—so local designs remain compatible.

3. **Independent solution for §75.3 — Configuration Management and Change Control.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Configuration management preserves consistency among requirements, interfaces, drawings, software, test evidence, and approved baselines. A drawing change that bypasses impact review can create an interface mismatch even if the changed component itself is correct.

4. **Independent solution for §75.4 — FMEA and Risk Prioritization.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: An RPN is one possible prioritization aid, \(RPN=S\times O\times D\), but severity must not be hidden by multiplication. IEC 60812 explicitly permits different prioritization approaches; a low-occurrence catastrophic hazard can still require action despite a moderate numeric RPN.

5. **Independent solution for §75.5 — Fault-Tree Analysis.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: For independent basic events A and B, an AND gate probability is \(P(A\cap B)=P(A)P(B)\). An OR gate occurs if either input occurs; for independent inputs its exact probability is \(1-[1-P(A)][1-P(B)]\), not simply the sum when overlap is non-negligible.

6. **Independent solution for §75.6 — Series and Parallel Reliability.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Two independent components of reliability 0.9 in series give \(R_s=0.9(0.9)=\mathbf{0.81}\). The same two in active parallel give \(R_p=1-(0.1)(0.1)=\mathbf{0.99}\), assuming either component can satisfy the function and failures are independent.

7. **Independent solution for §75.7 — Availability, Maintainability, and Life-Cycle Risk.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Availability is \(A=MTBF/(MTBF+MTTR)\). Reducing MTTR lowers the downtime term, so availability increases even if MTBF is unchanged. Life-cycle risk also depends on failure consequences, support resources, detection, maintenance policy, logistics, and changing operational context.

8. For an integrated **Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk** problem, reject any result that violates this chapter-specific screen: make requirements measurable and traceable, preserve interface/configuration consistency, treat FMEA/FTA assumptions explicitly, avoid assuming failure independence without basis, and distinguish reliability from availability.

9. For **Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **INCOSE5, IEC60812, IEC61025** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: set MTTR to zero and confirm ideal inherent availability approaches 1; set one series component reliability to zero and confirm series-system reliability becomes zero. The reduced case should behave as stated before the full model is trusted.

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
