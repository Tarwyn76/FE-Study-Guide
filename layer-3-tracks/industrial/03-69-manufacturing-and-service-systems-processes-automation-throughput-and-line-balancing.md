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

**Solution.** High-volume, low-variety parts often justify dedicated tooling or forming because tooling/setup cost can be spread over many units. Low-volume/high-variety work more often favors flexible processes such as general-purpose machining.

---

## 69.2 Throughput, WIP, and Flow Time

Production/service flow obeys Little’s law when the same system boundary and averaging basis are used.

\\[WIP=Throughput\\times Flow\\ Time\\]

![FIG-03-69-002: Textbook-quality industrial engineering diagram illustrating throughput, wip, and flow time with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-002-throughput-wip-and-flow-time.png)

### Worked Example 2

**Problem.** 20 units/hr and 0.5 hr flow time gives WIP 10.

**Solution.** Little's Law for a stable production system gives \(WIP=Throughput\times FlowTime=(20\ {\rm units/hr})(0.5\ {\rm hr})=\mathbf{10\ units}\). The relation links average long-run quantities measured on the same system boundary.

---

## 69.3 Capacity, Utilization, and Efficiency

Capacity metrics depend on the denominator chosen: design, effective, scheduled, or demonstrated capacity.

\\[Utilization=\\frac{actual\\ output}{defined\\ capacity}\\]

![FIG-03-69-003: Textbook-quality industrial engineering diagram illustrating capacity, utilization, and efficiency with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-003-capacity-utilization-and-efficiency.png)

### Worked Example 3

**Problem.** 80 units/hr on a 100-unit/hr design basis is 80% utilization.

**Solution.** Utilization is actual output divided by the defined capacity basis: \((80\ {\rm units/hr})/(100\ {\rm units/hr})=\mathbf{0.80=80\%}\). The units cancel, but the denominator still must be identified as design, effective, rated, or another stated capacity basis.

---

## 69.4 Automation and Human-Machine Allocation

Automation can improve repeatability and rate but introduces capital, integration, maintenance, and flexibility tradeoffs.

\\[\\text{automation decision}=f(\\text{technical, economic, safety, flexibility})\\]

![FIG-03-69-004: Textbook-quality industrial engineering diagram illustrating automation and human-machine allocation with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-004-automation-and-human-machine-allocation.png)

### Worked Example 4

**Problem.** A robot may handle repetitive hazardous transfer while operators manage exceptions.

**Solution.** Automating a repetitive hazardous transfer can remove workers from routine exposure while preserving human oversight for exceptions, setup, recovery, and judgment. The decision should include safety, reliability, economics, maintainability, and flexibility.

---

## 69.5 Line Cycle Time and Minimum Stations

Line balancing assigns tasks to stations while respecting precedence and cycle-time limits.

\\[CT=\\frac{OT}{OR},\\quad N_{min}=\\frac{\\sum t_i}{CT}\\]

![FIG-03-69-005: Textbook-quality industrial engineering diagram illustrating line cycle time and minimum stations with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-005-line-cycle-time-and-minimum-stations.png)

### Worked Example 5

**Problem.** 480 min/day and 240 units/day gives CT=2 min/unit.

**Solution.** Cycle time is \(CT=480\ {\rm min/day}/240\ {\rm units/day}=\mathbf{2\ min/unit}\). Minimum station count is then \(\lceil\sum t_i/CT\rceil\), with precedence constraints determining whether that theoretical minimum is achievable.

---

## 69.6 Line Efficiency and Idle Time

Balance efficiency compares useful assigned task time with total available station time per cycle.

\\[\\eta=\\frac{\\sum t_i}{NCT}\\]

![FIG-03-69-006: Textbook-quality industrial engineering diagram illustrating line efficiency and idle time with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-006-line-efficiency-and-idle-time.png)

### Worked Example 6

**Problem.** 18 min task content across 5 stations at CT=4 min gives 90%.

**Solution.** Line efficiency is \(\eta=\sum t_i/(NCT)=18/[5(4)]=18/20=\mathbf{0.90=90\%}\). Total idle time per cycle is \(NCT-\sum t_i=20-18=\mathbf{2\ min/cycle}\).

---

## 69.7 Energy Performance in Production

Energy management should normalize consumption to production/service output where appropriate.

\\[Energy\\ intensity=\\frac{energy\\ input}{useful\\ output}\\]

![FIG-03-69-007: Textbook-quality industrial engineering diagram illustrating energy performance in production with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-69-007-energy-performance-in-production.png)

### Worked Example 7

**Problem.** Same energy with 20% more good output improves energy intensity.

**Solution.** Energy intensity is energy per good unit. If energy input is unchanged and good output increases 20%, the new intensity is \(1/1.2=\mathbf{0.833}\) of the old value—about a **16.7% reduction**.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For this chapter, the FE Reference Handbook relation and variable definitions control whenever the Handbook supplies them. Use the external source set **HOPP, KALPAKJIAN9** only for specification-required learned material not fully developed in the Handbook.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 8; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Hopp, W. J., & Spearman, M. L. (2008). *Factory Physics* (3rd ed.). Waveland Press. ISBN 978-1-57766-739-1. Supporting scope: Throughput, WIP, cycle time, variability, bottlenecks, pull systems, capacity, inventory, and manufacturing-system behavior.
- Kalpakjian, S., & Schmid, S. R. (2025). *Manufacturing Engineering and Technology* (9th ed.). Pearson. Supporting scope: Manufacturing processes, process selection, production technology, automation, and manufacturing systems.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing**, the model boundary determines what is included in the decision. A valid solution must define the production boundary, distinguish design/effective capacity, keep time bases consistent, satisfy precedence in line balancing, and measure good output rather than gross activity.

16. Units and operational definitions are part of the model, not formatting details. For **Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing**. The external sources HOPP, KALPAKJIAN9 support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing** is to set flow time to zero and confirm WIP approaches zero for finite throughput; set line idle time to zero and confirm line efficiency approaches 100%. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §69.1, **Manufacturing Process Selection**, is based on \(\\text{process}=f(\\text{material, geometry, tolerance, volume, cost})\\). Interpret the result within the specific assumptions and system boundary of §69.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §69.2, **Throughput, WIP, and Flow Time**, is based on \(WIP=Throughput\\times Flow\\ Time\\). Interpret the result within the specific assumptions and system boundary of §69.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §69.3, **Capacity, Utilization, and Efficiency**, is based on \(Utilization=\\frac{actual\\ output}{defined\\ capacity}\\). Interpret the result within the specific assumptions and system boundary of §69.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §69.4, **Automation and Human-Machine Allocation**, is based on \(\\text{automation decision}=f(\\text{technical, economic, safety, flexibility})\\). Interpret the result within the specific assumptions and system boundary of §69.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §69.5, **Line Cycle Time and Minimum Stations**, is based on \(CT=\\frac{OT}{OR},\\quad N_{min}=\\frac{\\sum t_i}{CT}\\). Interpret the result within the specific assumptions and system boundary of §69.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §69.6, **Line Efficiency and Idle Time**, is based on \(\\eta=\\frac{\\sum t_i}{NCT}\\). Interpret the result within the specific assumptions and system boundary of §69.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §69.7, **Energy Performance in Production**, is based on \(Energy\\ intensity=\\frac{energy\\ input}{useful\\ output}\\). Interpret the result within the specific assumptions and system boundary of §69.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing.


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

1. **Independent solution for §69.1 — Manufacturing Process Selection.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: High-volume, low-variety parts often justify dedicated tooling or forming because tooling/setup cost can be spread over many units. Low-volume/high-variety work more often favors flexible processes such as general-purpose machining.

2. **Independent solution for §69.2 — Throughput, WIP, and Flow Time.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Little's Law for a stable production system gives \(WIP=Throughput\times FlowTime=(20\ {\rm units/hr})(0.5\ {\rm hr})=\mathbf{10\ units}\). The relation links average long-run quantities measured on the same system boundary.

3. **Independent solution for §69.3 — Capacity, Utilization, and Efficiency.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Utilization is actual output divided by the defined capacity basis: \((80\ {\rm units/hr})/(100\ {\rm units/hr})=\mathbf{0.80=80\%}\). The units cancel, but the denominator still must be identified as design, effective, rated, or another stated capacity basis.

4. **Independent solution for §69.4 — Automation and Human-Machine Allocation.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Automating a repetitive hazardous transfer can remove workers from routine exposure while preserving human oversight for exceptions, setup, recovery, and judgment. The decision should include safety, reliability, economics, maintainability, and flexibility.

5. **Independent solution for §69.5 — Line Cycle Time and Minimum Stations.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Cycle time is \(CT=480\ {\rm min/day}/240\ {\rm units/day}=\mathbf{2\ min/unit}\). Minimum station count is then \(\lceil\sum t_i/CT\rceil\), with precedence constraints determining whether that theoretical minimum is achievable.

6. **Independent solution for §69.6 — Line Efficiency and Idle Time.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Line efficiency is \(\eta=\sum t_i/(NCT)=18/[5(4)]=18/20=\mathbf{0.90=90\%}\). Total idle time per cycle is \(NCT-\sum t_i=20-18=\mathbf{2\ min/cycle}\).

7. **Independent solution for §69.7 — Energy Performance in Production.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Energy intensity is energy per good unit. If energy input is unchanged and good output increases 20%, the new intensity is \(1/1.2=\mathbf{0.833}\) of the old value—about a **16.7% reduction**.

8. For an integrated **Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing** problem, reject any result that violates this chapter-specific screen: define the production boundary, distinguish design/effective capacity, keep time bases consistent, satisfy precedence in line balancing, and measure good output rather than gross activity.

9. For **Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **HOPP, KALPAKJIAN9** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: set flow time to zero and confirm WIP approaches zero for finite throughput; set line idle time to zero and confirm line efficiency approaches 100%. The reduced case should behave as stated before the full model is trusted.

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
