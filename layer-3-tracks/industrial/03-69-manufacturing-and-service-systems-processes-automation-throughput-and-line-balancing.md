---
chapter: "03-69"
title: "Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-069-01, IND-3-069-02, IND-3-069-03, IND-3-069-04, IND-3-069-05, IND-3-069-06, IND-3-069-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-69: Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** IND-3-068-07 · MAT-2B-017-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **69.1** Explain and apply **Manufacturing Process Selection**.
* **69.2** Explain and apply **Throughput, WIP, and Flow Time**.
* **69.3** Explain and apply **Capacity, Utilization, and Efficiency**.
* **69.4** Explain and apply **Automation and Human-Machine Allocation**.
* **69.5** Explain and apply **Line Cycle Time and Minimum Stations**.
* **69.6** Explain and apply **Line Efficiency and Idle Time**.
* **69.7** Explain and apply **Energy Performance in Production**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 69.1 Manufacturing Process Selection

Process selection balances capability, tooling, rate, quality, material, and cost.

\\[\\text{process}=f(\\text{material, geometry, tolerance, volume, cost})\\]

![FIG-03-69-001: Textbook-quality industrial engineering diagram illustrating manufacturing process selection with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-001-manufacturing-process-selection.png)

### Worked Example 1

**Problem.** High-volume simple parts can favor forming over extensive machining.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 69.2 Throughput, WIP, and Flow Time

Production/service flow obeys Little’s law when the same system boundary and averaging basis are used.

\\[WIP=Throughput\\times Flow\\ Time\\]

![FIG-03-69-002: Textbook-quality industrial engineering diagram illustrating throughput, wip, and flow time with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-002-throughput-wip-and-flow-time.png)

### Worked Example 2

**Problem.** 20 units/hr and 0.5 hr flow time gives WIP 10.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 69.3 Capacity, Utilization, and Efficiency

Capacity metrics depend on the denominator chosen: design, effective, scheduled, or demonstrated capacity.

\\[Utilization=\\frac{actual\\ output}{defined\\ capacity}\\]

![FIG-03-69-003: Textbook-quality industrial engineering diagram illustrating capacity, utilization, and efficiency with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-003-capacity-utilization-and-efficiency.png)

### Worked Example 3

**Problem.** 80 units/hr on a 100-unit/hr design basis is 80% utilization.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 69.4 Automation and Human-Machine Allocation

Automation can improve repeatability and rate but introduces capital, integration, maintenance, and flexibility tradeoffs.

\\[\\text{automation decision}=f(\\text{technical, economic, safety, flexibility})\\]

![FIG-03-69-004: Textbook-quality industrial engineering diagram illustrating automation and human-machine allocation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-004-automation-and-human-machine-allocation.png)

### Worked Example 4

**Problem.** A robot may handle repetitive hazardous transfer while operators manage exceptions.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 69.5 Line Cycle Time and Minimum Stations

Line balancing assigns tasks to stations while respecting precedence and cycle-time limits.

\\[CT=\\frac{OT}{OR},\\quad N_{min}=\\frac{\\sum t_i}{CT}\\]

![FIG-03-69-005: Textbook-quality industrial engineering diagram illustrating line cycle time and minimum stations with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-005-line-cycle-time-and-minimum-stations.png)

### Worked Example 5

**Problem.** 480 min/day and 240 units/day gives CT=2 min/unit.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 69.6 Line Efficiency and Idle Time

Balance efficiency compares useful assigned task time with total available station time per cycle.

\\[\\eta=\\frac{\\sum t_i}{NCT}\\]

![FIG-03-69-006: Textbook-quality industrial engineering diagram illustrating line efficiency and idle time with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-006-line-efficiency-and-idle-time.png)

### Worked Example 6

**Problem.** 18 min task content across 5 stations at CT=4 min gives 90%.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 69.7 Energy Performance in Production

Energy management should normalize consumption to production/service output where appropriate.

\\[Energy\\ intensity=\\frac{energy\\ input}{useful\\ output}\\]

![FIG-03-69-007: Textbook-quality industrial engineering diagram illustrating energy performance in production with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-007-energy-performance-in-production.png)

### Worked Example 7

**Problem.** Same energy with 20% more good output improves energy intensity.

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

Primary source basis: **FE Industrial & Systems specification Area(s) 8; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

Specification-required management/design topics that are not directly tabulated are identified as learned or guide-developed rather than assigned false Handbook pages.

---

## Where This Goes Wrong

**Using industrial manufacturing process selection without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using manufacturing flow performance without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using production capacity utilization without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial automation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using line balancing without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using line balance efficiency without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial energy intensity without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| industrial manufacturing process selection | Industrial/systems concept developed in §69.1; apply with the stated model assumptions and decision basis. |
| manufacturing flow performance | Industrial/systems concept developed in §69.2; apply with the stated model assumptions and decision basis. |
| production capacity utilization | Industrial/systems concept developed in §69.3; apply with the stated model assumptions and decision basis. |
| industrial automation | Industrial/systems concept developed in §69.4; apply with the stated model assumptions and decision basis. |
| line balancing | Industrial/systems concept developed in §69.5; apply with the stated model assumptions and decision basis. |
| line balance efficiency | Industrial/systems concept developed in §69.6; apply with the stated model assumptions and decision basis. |
| industrial energy intensity | Industrial/systems concept developed in §69.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **industrial manufacturing process selection** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **manufacturing flow performance** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **production capacity utilization** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **industrial automation** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **line balancing** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **line balance efficiency** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **industrial energy intensity** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial manufacturing process selection**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **manufacturing flow performance**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **production capacity utilization**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial automation**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **line balancing**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **line balance efficiency**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial energy intensity**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **industrial manufacturing process selection**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **manufacturing flow performance**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **production capacity utilization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **industrial automation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **line balancing**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **line balance efficiency**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **industrial energy intensity**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **industrial manufacturing process selection**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **manufacturing flow performance**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **industrial manufacturing process selection** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **manufacturing flow performance** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **production capacity utilization** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **industrial automation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **line balancing** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **line balance efficiency** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **industrial energy intensity** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **industrial manufacturing process selection**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **manufacturing flow performance**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **production capacity utilization**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **industrial automation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **line balancing**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **line balance efficiency**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **industrial energy intensity**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. High-volume simple parts can favor forming over extensive machining.

2. 20 units/hr and 0.5 hr flow time gives WIP 10.

3. 80 units/hr on a 100-unit/hr design basis is 80% utilization.

4. A robot may handle repetitive hazardous transfer while operators manage exceptions.

5. 480 min/day and 240 units/day gives CT=2 min/unit.

6. 18 min task content across 5 stations at CT=4 min gives 90%.

7. Same energy with 20% more good output improves energy intensity.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §69.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §69.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §69.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §69.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §69.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §69.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §69.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 8, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 8.

- **industrial manufacturing process selection:** Manufacturing Process Selection
- **manufacturing flow performance:** Throughput, WIP, and Flow Time
- **production capacity utilization:** Capacity, Utilization, and Efficiency
- **industrial automation:** Automation and Human-Machine Allocation
- **line balancing:** Line Cycle Time and Minimum Stations
- **line balance efficiency:** Line Efficiency and Idle Time
- **industrial energy intensity:** Energy Performance in Production

---

## What's Next

**Chapter 03-70: Lean Systems, Process Improvement, Sustainability, and Value Engineering**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
