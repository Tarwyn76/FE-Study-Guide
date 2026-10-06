---
chapter: "03-70"
title: "Lean Systems, Process Improvement, Sustainability, and Value Engineering"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-070-01, IND-3-070-02, IND-3-070-03, IND-3-070-04, IND-3-070-05, IND-3-070-06, IND-3-070-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-70: Lean Systems, Process Improvement, Sustainability, and Value Engineering

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** IND-3-069-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Lean Systems, Process Improvement, Sustainability, and Value Engineering** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **70.1** Explain and apply **Value-Added and Non-Value-Added Time**.
* **70.2** Explain and apply **Lean Waste Identification**.
* **70.3** Explain and apply **Pull Systems, Takt Time, and Kanban**.
* **70.4** Explain and apply **PDCA and DMAIC Improvement Cycles**.
* **70.5** Explain and apply **Value Engineering**.
* **70.6** Explain and apply **Sustainable Production and Resource Efficiency**.
* **70.7** Explain and apply **Improvement Validation and System Effects**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 70.1 Value-Added and Non-Value-Added Time

Lean analysis distinguishes required value-producing work from delay and waste.

\\[Lead\\ time=VA\\ time+waiting+transport+rework+other\\ delay\\]

![FIG-03-70-001: Textbook-quality industrial engineering diagram illustrating value-added and non-value-added time with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-70-001-value-added-and-non-value-added-time.png)

### Worked Example 1

**Problem.** Two days of queue between two five-minute operations adds lead time, not processing value.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 70.2 Lean Waste Identification

Waste categories include defects, overproduction, waiting, unused talent, transportation, inventory, motion, and overprocessing.

\\[\\text{waste reduction}\\rightarrow\\text{less non-value resource use}\\]

![FIG-03-70-002: Textbook-quality industrial engineering diagram illustrating lean waste identification with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-70-002-lean-waste-identification.png)

### Worked Example 2

**Problem.** Moving a frequently used tool closer reduces unnecessary motion.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 70.3 Pull Systems, Takt Time, and Kanban

Pull systems replenish from downstream consumption; takt time states the customer-demand rhythm.

\\[Takt=\\frac{available\\ production\\ time}{customer\\ demand}\\]

![FIG-03-70-003: Textbook-quality industrial engineering diagram illustrating pull systems, takt time, and kanban with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-70-003-pull-systems-takt-time-and-kanban.png)

### Worked Example 3

**Problem.** 420 minutes for 210 units gives takt 2 min/unit.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 70.4 PDCA and DMAIC Improvement Cycles

Structured improvement prevents solution jumping by using baseline evidence and controlled follow-through.

\\[\\text{define/plan}\\rightarrow\\text{measure/do}\\rightarrow\\text{analyze/check}\\rightarrow\\text{improve/act}\\]

![FIG-03-70-004: Textbook-quality industrial engineering diagram illustrating pdca and dmaic improvement cycles with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-70-004-pdca-and-dmaic-improvement-cycles.png)

### Worked Example 4

**Problem.** Measure baseline defects before changing the process if you want to verify improvement.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 70.5 Value Engineering

Value engineering seeks required function at lower lifecycle cost without degrading needed performance or safety.

\\[Value=\\frac{Function}{Life-cycle\\ Cost}\\]

![FIG-03-70-005: Textbook-quality industrial engineering diagram illustrating value engineering with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-70-005-value-engineering.png)

### Worked Example 5

**Problem.** A cheaper component is not better value if it cannot meet required function.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 70.6 Sustainable Production and Resource Efficiency

Sustainable production integrates resource use, emissions, waste, lifecycle, and economic performance.

\\[Resource\\ intensity=\\frac{energy/material/water/waste}{useful\\ output}\\]

![FIG-03-70-006: Textbook-quality industrial engineering diagram illustrating sustainable production and resource efficiency with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-70-006-sustainable-production-and-resource-efficiency.png)

### Worked Example 6

**Problem.** Reducing scrap improves material efficiency and cost per good unit.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 70.7 Improvement Validation and System Effects

Local optimization can shift problems elsewhere. Validate results across the whole system.

\\[\\text{improvement must hold across throughput, quality, safety, cost, and downstream effects}\\]

![FIG-03-70-007: Textbook-quality industrial engineering diagram illustrating improvement validation and system effects with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-70-007-improvement-validation-and-system-effects.png)

### Worked Example 7

**Problem.** Higher machine speed can reduce cycle time but increase defects or starve downstream work.

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

**Using lean value stream without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using lean waste identification without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using pull production system without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using continuous process improvement without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using value engineering without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using sustainable production system without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using process-improvement validation without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| lean value stream | Industrial/systems concept developed in §70.1; apply with the stated model assumptions and decision basis. |
| lean waste identification | Industrial/systems concept developed in §70.2; apply with the stated model assumptions and decision basis. |
| pull production system | Industrial/systems concept developed in §70.3; apply with the stated model assumptions and decision basis. |
| continuous process improvement | Industrial/systems concept developed in §70.4; apply with the stated model assumptions and decision basis. |
| value engineering | Industrial/systems concept developed in §70.5; apply with the stated model assumptions and decision basis. |
| sustainable production system | Industrial/systems concept developed in §70.6; apply with the stated model assumptions and decision basis. |
| process-improvement validation | Industrial/systems concept developed in §70.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **lean value stream** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **lean waste identification** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **pull production system** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **continuous process improvement** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **value engineering** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **sustainable production system** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **process-improvement validation** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **lean value stream**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **lean waste identification**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **pull production system**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **continuous process improvement**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **value engineering**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **sustainable production system**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **process-improvement validation**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **lean value stream**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **lean waste identification**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **pull production system**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **continuous process improvement**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **value engineering**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **sustainable production system**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **process-improvement validation**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **lean value stream**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **lean waste identification**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **lean value stream** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **lean waste identification** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **pull production system** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **continuous process improvement** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **value engineering** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **sustainable production system** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **process-improvement validation** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **lean value stream**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **lean waste identification**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **pull production system**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **continuous process improvement**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **value engineering**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **sustainable production system**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **process-improvement validation**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. Two days of queue between two five-minute operations adds lead time, not processing value.

2. Moving a frequently used tool closer reduces unnecessary motion.

3. 420 minutes for 210 units gives takt 2 min/unit.

4. Measure baseline defects before changing the process if you want to verify improvement.

5. A cheaper component is not better value if it cannot meet required function.

6. Reducing scrap improves material efficiency and cost per good unit.

7. Higher machine speed can reduce cycle time but increase defects or starve downstream work.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §70.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §70.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §70.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §70.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §70.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §70.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §70.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 8, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 8.

- **lean value stream:** Value-Added and Non-Value-Added Time
- **lean waste identification:** Lean Waste Identification
- **pull production system:** Pull Systems, Takt Time, and Kanban
- **continuous process improvement:** PDCA and DMAIC Improvement Cycles
- **value engineering:** Value Engineering
- **sustainable production system:** Sustainable Production and Resource Efficiency
- **process-improvement validation:** Improvement Validation and System Effects

---

## What's Next

**Chapter 03-71: Facility Location, Layout, Capacity, and Material Handling**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
