---
chapter: "03-73"
title: "Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-073-01, IND-3-073-02, IND-3-073-03, IND-3-073-04, IND-3-073-05, IND-3-073-06, IND-3-073-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-73: Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** SAFE-2B-019-07 · MATH-1D-033-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **73.1** Explain and apply **Displays, Controls, Workload, and Usability**.
* **73.2** Explain and apply **Anthropometry and Percentile Design**.
* **73.3** Explain and apply **Biomechanics and Cumulative Trauma**.
* **73.4** Explain and apply **Industrial Hygiene and Noise**.
* **73.5** Explain and apply **Methods Analysis and Motion Economy**.
* **73.6** Explain and apply **Time Study, Allowances, and Standard Time**.
* **73.7** Explain and apply **Work Sampling and Learning Curves**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 73.1 Displays, Controls, Workload, and Usability

Human factors designs systems around human capabilities and limitations.

\\[\\text{performance}=f(\\text{perception, cognition, control, feedback, workload})\\]

![FIG-03-73-001: Textbook-quality industrial engineering diagram illustrating displays, controls, workload, and usability with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-001-displays-controls-workload-and-usability.png)

### Worked Example 1

**Problem.** A warning should be detectable, interpretable, and linked to a useful response.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 73.2 Anthropometry and Percentile Design

Clearance often accommodates larger users; reach often accommodates smaller users; adjustability can cover a broad range.

\\[\\text{design percentile depends on clearance, reach, and adjustability objective}\\]

![FIG-03-73-002: Textbook-quality industrial engineering diagram illustrating anthropometry and percentile design with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-002-anthropometry-and-percentile-design.png)

### Worked Example 2

**Problem.** A doorway should not be designed from only the 5th-percentile stature.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 73.3 Biomechanics and Cumulative Trauma

Ergonomic risk rises with force, awkward posture, repetition, vibration, and insufficient recovery.

\\[Risk=f(force,posture,repetition,duration,recovery)\\]

![FIG-03-73-003: Textbook-quality industrial engineering diagram illustrating biomechanics and cumulative trauma with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-003-biomechanics-and-cumulative-trauma.png)

### Worked Example 3

**Problem.** Raising a workpiece can reduce trunk flexion during repetitive assembly.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 73.4 Industrial Hygiene and Noise

Industrial hygiene applies recognition, evaluation, and control to workplace hazards.

\\[\\text{identify}\\rightarrow\\text{assess}\\rightarrow\\text{control}\\rightarrow\\text{verify}\\]

![FIG-03-73-004: Textbook-quality industrial engineering diagram illustrating industrial hygiene and noise with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-004-industrial-hygiene-and-noise.png)

### Worked Example 4

**Problem.** Engineering noise control is preferable to relying only on hearing protection when feasible.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 73.5 Methods Analysis and Motion Economy

Methods analysis removes unnecessary movement and improves sequence, workplace arrangement, and tool use.

\\[\\text{document}\\rightarrow\\text{question}\\rightarrow\\text{redesign}\\rightarrow\\text{standardize}\\]

![FIG-03-73-005: Textbook-quality industrial engineering diagram illustrating methods analysis and motion economy with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-005-methods-analysis-and-motion-economy.png)

### Worked Example 5

**Problem.** Combining unnecessary handoffs can reduce travel and handling.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 73.6 Time Study, Allowances, and Standard Time

Time study converts observed time to normal time and then applies allowances according to the stated basis.

\\[ST=NT\\times AF\\]

![FIG-03-73-006: Textbook-quality industrial engineering diagram illustrating time study, allowances, and standard time with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-006-time-study-allowances-and-standard-time.png)

### Worked Example 6

**Problem.** NT=10 min and a 15% job-time allowance gives ST=11.5 min.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 73.7 Work Sampling and Learning Curves

Work sampling estimates activity proportions; learning curves model task-time reduction with repetition.

\\[T_N=KN^s,\\quad s=\\frac{\\ln(LR)}{\\ln2}\\]

![FIG-03-73-007: Textbook-quality industrial engineering diagram illustrating work sampling and learning curves with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-007-work-sampling-and-learning-curves.png)

### Worked Example 7

**Problem.** An 80% learning rate means unit time falls to 80% when cumulative quantity doubles.

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

Primary source basis: **FE Industrial & Systems specification Area(s) 10, 11; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

Specification-required management/design topics that are not directly tabulated are identified as learned or guide-developed rather than assigned false Handbook pages.

---

## Where This Goes Wrong

**Using human factors engineering without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using anthropometric workplace design without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using ergonomic biomechanical risk without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial hygiene exposure without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using methods analysis without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using standard time determination without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial learning curve without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| human factors engineering | Industrial/systems concept developed in §73.1; apply with the stated model assumptions and decision basis. |
| anthropometric workplace design | Industrial/systems concept developed in §73.2; apply with the stated model assumptions and decision basis. |
| ergonomic biomechanical risk | Industrial/systems concept developed in §73.3; apply with the stated model assumptions and decision basis. |
| industrial hygiene exposure | Industrial/systems concept developed in §73.4; apply with the stated model assumptions and decision basis. |
| methods analysis | Industrial/systems concept developed in §73.5; apply with the stated model assumptions and decision basis. |
| standard time determination | Industrial/systems concept developed in §73.6; apply with the stated model assumptions and decision basis. |
| industrial learning curve | Industrial/systems concept developed in §73.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **human factors engineering** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **anthropometric workplace design** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **ergonomic biomechanical risk** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **industrial hygiene exposure** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **methods analysis** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **standard time determination** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **industrial learning curve** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **human factors engineering**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **anthropometric workplace design**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **ergonomic biomechanical risk**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial hygiene exposure**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **methods analysis**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **standard time determination**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial learning curve**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **human factors engineering**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **anthropometric workplace design**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **ergonomic biomechanical risk**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **industrial hygiene exposure**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **methods analysis**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **standard time determination**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **industrial learning curve**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **human factors engineering**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **anthropometric workplace design**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **human factors engineering** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **anthropometric workplace design** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **ergonomic biomechanical risk** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **industrial hygiene exposure** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **methods analysis** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **standard time determination** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **industrial learning curve** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **human factors engineering**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **anthropometric workplace design**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **ergonomic biomechanical risk**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **industrial hygiene exposure**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **methods analysis**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **standard time determination**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **industrial learning curve**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. A warning should be detectable, interpretable, and linked to a useful response.

2. A doorway should not be designed from only the 5th-percentile stature.

3. Raising a workpiece can reduce trunk flexion during repetitive assembly.

4. Engineering noise control is preferable to relying only on hearing protection when feasible.

5. Combining unnecessary handoffs can reduce travel and handling.

6. NT=10 min and a 15% job-time allowance gives ST=11.5 min.

7. An 80% learning rate means unit time falls to 80% when cumulative quantity doubles.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §73.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §73.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §73.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §73.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §73.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §73.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §73.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 10, 11, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 10, 11.

- **human factors engineering:** Displays, Controls, Workload, and Usability
- **anthropometric workplace design:** Anthropometry and Percentile Design
- **ergonomic biomechanical risk:** Biomechanics and Cumulative Trauma
- **industrial hygiene exposure:** Industrial Hygiene and Noise
- **methods analysis:** Methods Analysis and Motion Economy
- **standard time determination:** Time Study, Allowances, and Standard Time
- **industrial learning curve:** Work Sampling and Learning Curves

---

## What's Next

**Chapter 03-74: Quality Management, SPC, Process Capability, Sampling, and DOE**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
