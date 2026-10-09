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

**Solution.** Load-distance is \(LD=\sum F_{ij}D_{ij}\). Because each pair's contribution is flow times distance, reducing distance for a high-flow pair typically produces a larger LD reduction than moving a rarely interacting pair the same distance.

---

## 71.2 Euclidean, Rectilinear, and Chebyshev Distance

Distance metric must match physical movement constraints.

\\[D_E=\\sqrt{(\\Delta x)^2+(\\Delta y)^2},\\quad D_R=|\\Delta x|+|\\Delta y|\\]

![FIG-03-71-002: Textbook-quality industrial engineering diagram illustrating euclidean, rectilinear, and chebyshev distance with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-002-euclidean-rectilinear-and-chebyshev-distance.png)

### Worked Example 2

**Problem.** (0,0) to (3,4) is 5 Euclidean and 7 rectilinear.

**Solution.** From \((0,0)\) to \((3,4)\), Euclidean distance is \(\sqrt{3^2+4^2}=\mathbf{5}\) distance units; rectilinear distance is \(|3|+|4|=\mathbf{7}\). Choose the metric that matches permitted travel paths.

---

## 71.3 Product, Process, Cellular, and Fixed-Position Layouts

Layout types serve different volume-variety and movement patterns.

\\[\\text{layout}=f(\\text{volume, variety, flow, flexibility})\\]

![FIG-03-71-003: Textbook-quality industrial engineering diagram illustrating product, process, cellular, and fixed-position layouts with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-003-product-process-cellular-and-fixed-position-layouts.png)

### Worked Example 3

**Problem.** High-volume repetitive assembly often favors product layout.

**Solution.** A product layout aligns resources with a repetitive flow and is favored by high volume/low variety. Process layouts group similar functions and provide more routing flexibility for high-variety work; cellular layouts seek family flow, while fixed-position layouts keep the product stationary.

---

## 71.4 Plant Location Models

Facility location balances fixed opening cost and customer supply cost.

\\[\\min\\sum_jf_jx_j+\\sum_i\\sum_jc_{ij}y_{ij}\\]

![FIG-03-71-004: Textbook-quality industrial engineering diagram illustrating plant location models with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-004-plant-location-models.png)

### Worked Example 4

**Problem.** Opening another site can reduce shipping cost while increasing fixed cost.

**Solution.** A facility-location model trades opening cost against assignment/transport cost. Opening an additional facility can reduce \(c_{ij}y_{ij}\) by shortening routes while adding a fixed \(f_j\); the economically preferred network minimizes the combined cost while meeting demand/capacity constraints.

---

## 71.5 Machine Requirements and Capacity

Machine requirements are workload divided by available productive time.

\\[M_j=\\sum_i\\frac{P_{ij}T_{ij}}{C_{ij}}\\]

![FIG-03-71-005: Textbook-quality industrial engineering diagram illustrating machine requirements and capacity with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-005-machine-requirements-and-capacity.png)

### Worked Example 5

**Problem.** 1000 pieces/day at 0.1 hr each with 20 available hr/day requires 5 machines.

**Solution.** Machine requirement is workload divided by usable machine capacity: \(1000(0.1\ {\rm hr})/(20\ {\rm hr/day})=100/20=\mathbf{5\ machines}\). Round upward when a fractional machine cannot satisfy the required workload.

---

## 71.6 Labor and Crew Requirements

Crew sizing follows required labor content divided by available labor time with appropriate allowance assumptions.

\\[A_j=\\sum_i\\frac{P_{ij}T_{ij}}{C_{ij}}\\]

![FIG-03-71-006: Textbook-quality industrial engineering diagram illustrating labor and crew requirements with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-006-labor-and-crew-requirements.png)

### Worked Example 6

**Problem.** 4800 labor-min/day with 400 usable min/person requires 12 people.

**Solution.** Required labor is \(4800\ {\rm min/day}/(400\ {\rm min/person\cdot day})=\mathbf{12\ people}\). The usable-time denominator should already reflect the allowance/utilization assumptions intended by the problem.

---

## 71.7 Material-Handling System Selection

Conveyors, forklifts, AGVs, cranes, and manual handling suit different movement patterns.

\\[\\text{choice}=f(\\text{load, distance, frequency, path, flexibility, safety})\\]

![FIG-03-71-007: Textbook-quality industrial engineering diagram illustrating material-handling system selection with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-71-007-material-handling-system-selection.png)

### Worked Example 7

**Problem.** A fixed conveyor suits stable repetitive flow better than frequently changing routes.

**Solution.** A fixed conveyor fits high-frequency, stable, repeatable paths because it offers high flow with limited routing flexibility. Forklifts, carts, AGVs/AMRs, cranes, or other systems may be better when load form, path variability, volume, interface, safety, or expansion needs differ.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Facility Location, Layout, Capacity, and Material Handling**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For this chapter, the FE Reference Handbook relation and variable definitions control whenever the Handbook supplies them. Use the external source set **TOMPKINS** only for specification-required learned material not fully developed in the Handbook.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 9; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Tompkins, J. A., White, J. A., Bozer, Y. A., & Tanchoco, J. M. A. (2010/2014 electronic issue). *Facilities Planning* (4th ed.). Wiley. ISBN 978-0-470-44404-7. Supporting scope: Facility location/layout, flow, capacity, material handling, and quantitative facilities-planning methods.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Facility Location, Layout, Capacity, and Material Handling**, the model boundary determines what is included in the decision. A valid solution must use the correct distance metric, maintain facility/machine/labor capacity feasibility, round indivisible resources upward when needed, and match handling equipment to the actual load/path/frequency/safety environment.

16. Units and operational definitions are part of the model, not formatting details. For **Facility Location, Layout, Capacity, and Material Handling**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Facility Location, Layout, Capacity, and Material Handling**. The external sources TOMPKINS support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Facility Location, Layout, Capacity, and Material Handling** is to co-locate two departments and confirm their pairwise distance contribution to load-distance becomes zero. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §71.1, **From-To Charts and Load-Distance**, is based on \(LD=\\sum_{i,j}F_{ij}D_{ij}\\). Interpret the result within the specific assumptions and system boundary of §71.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §71.2, **Euclidean, Rectilinear, and Chebyshev Distance**, is based on \(D_E=\\sqrt{(\\Delta x)^2+(\\Delta y)^2},\\quad D_R=|\\Delta x|+|\\Delta y|\\). Interpret the result within the specific assumptions and system boundary of §71.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §71.3, **Product, Process, Cellular, and Fixed-Position Layouts**, is based on \(\\text{layout}=f(\\text{volume, variety, flow, flexibility})\\). Interpret the result within the specific assumptions and system boundary of §71.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §71.4, **Plant Location Models**, is based on \(\\min\\sum_jf_jx_j+\\sum_i\\sum_jc_{ij}y_{ij}\\). Interpret the result within the specific assumptions and system boundary of §71.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §71.5, **Machine Requirements and Capacity**, is based on \(M_j=\\sum_i\\frac{P_{ij}T_{ij}}{C_{ij}}\\). Interpret the result within the specific assumptions and system boundary of §71.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §71.6, **Labor and Crew Requirements**, is based on \(A_j=\\sum_i\\frac{P_{ij}T_{ij}}{C_{ij}}\\). Interpret the result within the specific assumptions and system boundary of §71.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §71.7, **Material-Handling System Selection**, is based on \(\\text{choice}=f(\\text{load, distance, frequency, path, flexibility, safety})\\). Interpret the result within the specific assumptions and system boundary of §71.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Facility Location, Layout, Capacity, and Material Handling decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Facility Location, Layout, Capacity, and Material Handling.


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

1. **Independent solution for §71.1 — From-To Charts and Load-Distance.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Load-distance is \(LD=\sum F_{ij}D_{ij}\). Because each pair's contribution is flow times distance, reducing distance for a high-flow pair typically produces a larger LD reduction than moving a rarely interacting pair the same distance.

2. **Independent solution for §71.2 — Euclidean, Rectilinear, and Chebyshev Distance.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: From \((0,0)\) to \((3,4)\), Euclidean distance is \(\sqrt{3^2+4^2}=\mathbf{5}\) distance units; rectilinear distance is \(|3|+|4|=\mathbf{7}\). Choose the metric that matches permitted travel paths.

3. **Independent solution for §71.3 — Product, Process, Cellular, and Fixed-Position Layouts.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A product layout aligns resources with a repetitive flow and is favored by high volume/low variety. Process layouts group similar functions and provide more routing flexibility for high-variety work; cellular layouts seek family flow, while fixed-position layouts keep the product stationary.

4. **Independent solution for §71.4 — Plant Location Models.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A facility-location model trades opening cost against assignment/transport cost. Opening an additional facility can reduce \(c_{ij}y_{ij}\) by shortening routes while adding a fixed \(f_j\); the economically preferred network minimizes the combined cost while meeting demand/capacity constraints.

5. **Independent solution for §71.5 — Machine Requirements and Capacity.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Machine requirement is workload divided by usable machine capacity: \(1000(0.1\ {\rm hr})/(20\ {\rm hr/day})=100/20=\mathbf{5\ machines}\). Round upward when a fractional machine cannot satisfy the required workload.

6. **Independent solution for §71.6 — Labor and Crew Requirements.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Required labor is \(4800\ {\rm min/day}/(400\ {\rm min/person\cdot day})=\mathbf{12\ people}\). The usable-time denominator should already reflect the allowance/utilization assumptions intended by the problem.

7. **Independent solution for §71.7 — Material-Handling System Selection.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A fixed conveyor fits high-frequency, stable, repeatable paths because it offers high flow with limited routing flexibility. Forklifts, carts, AGVs/AMRs, cranes, or other systems may be better when load form, path variability, volume, interface, safety, or expansion needs differ.

8. For an integrated **Facility Location, Layout, Capacity, and Material Handling** problem, reject any result that violates this chapter-specific screen: use the correct distance metric, maintain facility/machine/labor capacity feasibility, round indivisible resources upward when needed, and match handling equipment to the actual load/path/frequency/safety environment.

9. For **Facility Location, Layout, Capacity, and Material Handling**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **TOMPKINS** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: co-locate two departments and confirm their pairwise distance contribution to load-distance becomes zero. The reduced case should behave as stated before the full model is trusted.

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
