---
chapter: "03-71"
title: "Facility Location, Layout, Capacity, and Material Handling"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-071-01, IND-3-071-02, IND-3-071-03, IND-3-071-04, IND-3-071-05, IND-3-071-06, IND-3-071-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-71: Facility Location, Layout, Capacity, and Material Handling

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** IND-3-063-07 · IND-3-069-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Facility Location, Layout, Capacity, and Material Handling** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **71.1** Explain and apply **From-To Charts and Load-Distance**.
* **71.2** Explain and apply **Euclidean, Rectilinear, and Chebyshev Distance**.
* **71.3** Explain and apply **Product, Process, Cellular, and Fixed-Position Layouts**.
* **71.4** Explain and apply **Plant Location Models**.
* **71.5** Explain and apply **Machine Requirements and Capacity**.
* **71.6** Explain and apply **Labor and Crew Requirements**.
* **71.7** Explain and apply **Material-Handling System Selection**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 71.1 From-To Charts and Load-Distance

From-to analysis combines movement frequency/volume and distance to compare layouts.

\\[LD=\\sum_{i,j}F_{ij}D_{ij}\\]

![FIG-03-71-001: Textbook-quality industrial engineering diagram illustrating from-to charts and load-distance with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-001-from-to-charts-and-load-distance.png)

### Worked Example 1

**Problem.** Bringing a high-flow department pair closer can reduce total handling distance.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 71.2 Euclidean, Rectilinear, and Chebyshev Distance

Distance metric must match physical movement constraints.

\\[D_E=\\sqrt{(\\Delta x)^2+(\\Delta y)^2},\\quad D_R=|\\Delta x|+|\\Delta y|\\]

![FIG-03-71-002: Textbook-quality industrial engineering diagram illustrating euclidean, rectilinear, and chebyshev distance with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-002-euclidean-rectilinear-and-chebyshev-distance.png)

### Worked Example 2

**Problem.** (0,0) to (3,4) is 5 Euclidean and 7 rectilinear.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 71.3 Product, Process, Cellular, and Fixed-Position Layouts

Layout types serve different volume-variety and movement patterns.

\\[\\text{layout}=f(\\text{volume, variety, flow, flexibility})\\]

![FIG-03-71-003: Textbook-quality industrial engineering diagram illustrating product, process, cellular, and fixed-position layouts with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-003-product-process-cellular-and-fixed-position-layouts.png)

### Worked Example 3

**Problem.** High-volume repetitive assembly often favors product layout.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 71.4 Plant Location Models

Facility location balances fixed opening cost and customer supply cost.

\\[\\min\\sum_jf_jx_j+\\sum_i\\sum_jc_{ij}y_{ij}\\]

![FIG-03-71-004: Textbook-quality industrial engineering diagram illustrating plant location models with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-004-plant-location-models.png)

### Worked Example 4

**Problem.** Opening another site can reduce shipping cost while increasing fixed cost.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 71.5 Machine Requirements and Capacity

Machine requirements are workload divided by available productive time.

\\[M_j=\\sum_i\\frac{P_{ij}T_{ij}}{C_{ij}}\\]

![FIG-03-71-005: Textbook-quality industrial engineering diagram illustrating machine requirements and capacity with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-005-machine-requirements-and-capacity.png)

### Worked Example 5

**Problem.** 1000 pieces/day at 0.1 hr each with 20 available hr/day requires 5 machines.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 71.6 Labor and Crew Requirements

Crew sizing follows required labor content divided by available labor time with appropriate allowance assumptions.

\\[A_j=\\sum_i\\frac{P_{ij}T_{ij}}{C_{ij}}\\]

![FIG-03-71-006: Textbook-quality industrial engineering diagram illustrating labor and crew requirements with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-006-labor-and-crew-requirements.png)

### Worked Example 6

**Problem.** 4800 labor-min/day with 400 usable min/person requires 12 people.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 71.7 Material-Handling System Selection

Conveyors, forklifts, AGVs, cranes, and manual handling suit different movement patterns.

\\[\\text{choice}=f(\\text{load, distance, frequency, path, flexibility, safety})\\]

![FIG-03-71-007: Textbook-quality industrial engineering diagram illustrating material-handling system selection with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-007-material-handling-system-selection.png)

### Worked Example 7

**Problem.** A fixed conveyor suits stable repetitive flow better than frequently changing routes.

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

**Using facility flow analysis without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using facility distance metric without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using facility layout type without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using facility location optimization without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using machine requirement calculation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using people requirement calculation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using material handling system selection without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| facility flow analysis | Industrial/systems concept developed in §71.1; apply with the stated model assumptions and decision basis. |
| facility distance metric | Industrial/systems concept developed in §71.2; apply with the stated model assumptions and decision basis. |
| facility layout type | Industrial/systems concept developed in §71.3; apply with the stated model assumptions and decision basis. |
| facility location optimization | Industrial/systems concept developed in §71.4; apply with the stated model assumptions and decision basis. |
| machine requirement calculation | Industrial/systems concept developed in §71.5; apply with the stated model assumptions and decision basis. |
| people requirement calculation | Industrial/systems concept developed in §71.6; apply with the stated model assumptions and decision basis. |
| material handling system selection | Industrial/systems concept developed in §71.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **facility flow analysis** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **facility distance metric** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **facility layout type** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **facility location optimization** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **machine requirement calculation** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **people requirement calculation** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **material handling system selection** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **facility flow analysis**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **facility distance metric**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **facility layout type**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **facility location optimization**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **machine requirement calculation**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **people requirement calculation**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **material handling system selection**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **facility flow analysis**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **facility distance metric**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **facility layout type**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **facility location optimization**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **machine requirement calculation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **people requirement calculation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **material handling system selection**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **facility flow analysis**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **facility distance metric**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **facility flow analysis** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **facility distance metric** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **facility layout type** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **facility location optimization** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **machine requirement calculation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **people requirement calculation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **material handling system selection** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **facility flow analysis**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **facility distance metric**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **facility layout type**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **facility location optimization**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **machine requirement calculation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **people requirement calculation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **material handling system selection**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. Bringing a high-flow department pair closer can reduce total handling distance.

2. (0,0) to (3,4) is 5 Euclidean and 7 rectilinear.

3. High-volume repetitive assembly often favors product layout.

4. Opening another site can reduce shipping cost while increasing fixed cost.

5. 1000 pieces/day at 0.1 hr each with 20 available hr/day requires 5 machines.

6. 4800 labor-min/day with 400 usable min/person requires 12 people.

7. A fixed conveyor suits stable repetitive flow better than frequently changing routes.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §71.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §71.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §71.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §71.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §71.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §71.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §71.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 9, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 9.

- **facility flow analysis:** From-To Charts and Load-Distance
- **facility distance metric:** Euclidean, Rectilinear, and Chebyshev Distance
- **facility layout type:** Product, Process, Cellular, and Fixed-Position Layouts
- **facility location optimization:** Plant Location Models
- **machine requirement calculation:** Machine Requirements and Capacity
- **people requirement calculation:** Labor and Crew Requirements
- **material handling system selection:** Material-Handling System Selection

---

## What's Next

**Chapter 03-72: Supply Chains, Transportation Networks, Pooling, and Distribution**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
