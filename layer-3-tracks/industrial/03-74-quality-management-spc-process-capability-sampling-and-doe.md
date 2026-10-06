---
chapter: "03-74"
title: "Quality Management, SPC, Process Capability, Sampling, and DOE"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-074-01, IND-3-074-02, IND-3-074-03, IND-3-074-04, IND-3-074-05, IND-3-074-06, IND-3-074-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-74: Quality Management, SPC, Process Capability, Sampling, and DOE

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** MATH-1D-033-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Quality Management, SPC, Process Capability, Sampling, and DOE** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **74.1** Explain and apply **Quality Planning, Assurance, Control, and Improvement**.
* **74.2** Explain and apply **QFD and House of Quality**.
* **74.3** Explain and apply **Cause-and-Effect and Taguchi Loss**.
* **74.4** Explain and apply **Control Charts and SPC**.
* **74.5** Explain and apply **Process Capability Cp and Cpk**.
* **74.6** Explain and apply **Acceptance Sampling and OC Curves**.
* **74.7** Explain and apply **Factorial DOE, Interactions, and ANOVA**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 74.1 Quality Planning, Assurance, Control, and Improvement

Inspection alone is not a quality system; quality spans requirements, process control, verification, corrective action, and improvement.

\\[Quality=plan+assure+control+improve\\]

![FIG-03-74-001: Textbook-quality industrial engineering diagram illustrating quality planning, assurance, control, and improvement with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-74-001-quality-planning-assurance-control-and-improvement.png)

### Worked Example 1

**Problem.** A capable process still needs measurement and control to sustain performance.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 74.2 QFD and House of Quality

QFD translates customer needs into measurable engineering characteristics and priorities.

\\[Customer\\ needs\\rightarrow Engineering\\ characteristics\\]

![FIG-03-74-002: Textbook-quality industrial engineering diagram illustrating qfd and house of quality with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-74-002-qfd-and-house-of-quality.png)

### Worked Example 2

**Problem.** A desire for quiet operation can map to a sound-pressure requirement.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 74.3 Cause-and-Effect and Taguchi Loss

Cause-and-effect tools organize possible variation sources; Taguchi loss emphasizes loss from deviation from target.

\\[L(y)=k(y-T)^2\\]

![FIG-03-74-003: Textbook-quality industrial engineering diagram illustrating cause-and-effect and taguchi loss with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-74-003-cause-and-effect-and-taguchi-loss.png)

### Worked Example 3

**Problem.** Two parts within specification can have different expected loss if one is farther from target.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 74.4 Control Charts and SPC

Control charts distinguish common-cause behavior from evidence of special causes.

\\[UCL=CL+3\\sigma_{stat},\\quad LCL=CL-3\\sigma_{stat}\\]

![FIG-03-74-004: Textbook-quality industrial engineering diagram illustrating control charts and spc with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-74-004-control-charts-and-spc.png)

### Worked Example 4

**Problem.** A point beyond UCL triggers investigation even if the item is still within specification.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 74.5 Process Capability Cp and Cpk

Cp measures potential centered capability; Cpk also reflects centering.

\\[C_p=\\frac{USL-LSL}{6\\sigma},\\quad C_{pk}=\\min(\\frac{USL-\\mu}{3\\sigma},\\frac{\\mu-LSL}{3\\sigma})\\]

![FIG-03-74-005: Textbook-quality industrial engineering diagram illustrating process capability cp and cpk with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-74-005-process-capability-cp-and-cpk.png)

### Worked Example 5

**Problem.** For a centered process, Cp=Cpk.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 74.6 Acceptance Sampling and OC Curves

Acceptance sampling makes lot decisions from samples; the OC curve shows acceptance probability versus incoming defect fraction.

\\[P_a=P(\\text{lot accepted}\\mid p)\\]

![FIG-03-74-006: Textbook-quality industrial engineering diagram illustrating acceptance sampling and oc curves with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-74-006-acceptance-sampling-and-oc-curves.png)

### Worked Example 6

**Problem.** A stricter plan reduces acceptance of poor lots but may reject more good lots.

**Solution.** Apply the relation or workflow above, then verify assumptions, units, feasibility, and system-level interpretation.

---

## 74.7 Factorial DOE, Interactions, and ANOVA

Factorial experiments estimate main effects and interactions efficiently; ANOVA partitions variation.

\\[E_i=\\bar Y_{i,+}-\\bar Y_{i,-}\\]

![FIG-03-74-007: Textbook-quality industrial engineering diagram illustrating factorial doe, interactions, and anova with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-74-007-factorial-doe-interactions-and-anova.png)

### Worked Example 7

**Problem.** An interaction means one factor’s effect depends on another factor’s level.

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

Primary source basis: **FE Industrial & Systems specification Area(s) 12; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

Specification-required management/design topics that are not directly tabulated are identified as learned or guide-developed rather than assigned false Handbook pages.

---

## Where This Goes Wrong

**Using industrial quality system without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using quality function deployment without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using quality loss function without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using statistical process control without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using process capability index without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using acceptance sampling OC curve without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using industrial factorial design without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| industrial quality system | Industrial/systems concept developed in §74.1; apply with the stated model assumptions and decision basis. |
| quality function deployment | Industrial/systems concept developed in §74.2; apply with the stated model assumptions and decision basis. |
| quality loss function | Industrial/systems concept developed in §74.3; apply with the stated model assumptions and decision basis. |
| statistical process control | Industrial/systems concept developed in §74.4; apply with the stated model assumptions and decision basis. |
| process capability index | Industrial/systems concept developed in §74.5; apply with the stated model assumptions and decision basis. |
| acceptance sampling OC curve | Industrial/systems concept developed in §74.6; apply with the stated model assumptions and decision basis. |
| industrial factorial design | Industrial/systems concept developed in §74.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **industrial quality system** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **quality function deployment** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **quality loss function** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **statistical process control** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **process capability index** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **acceptance sampling OC curve** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **industrial factorial design** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial quality system**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **quality function deployment**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **quality loss function**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **statistical process control**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **process capability index**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **acceptance sampling OC curve**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial factorial design**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **industrial quality system**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **quality function deployment**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **quality loss function**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **statistical process control**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **process capability index**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **acceptance sampling OC curve**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **industrial factorial design**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **industrial quality system**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **quality function deployment**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **industrial quality system** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **quality function deployment** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **quality loss function** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **statistical process control** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **process capability index** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **acceptance sampling OC curve** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **industrial factorial design** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **industrial quality system**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **quality function deployment**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **quality loss function**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **statistical process control**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **process capability index**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **acceptance sampling OC curve**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **industrial factorial design**, verify data basis, units, capacity/probability conditions, and operational feasibility.

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

1. A capable process still needs measurement and control to sustain performance.

2. A desire for quiet operation can map to a sound-pressure requirement.

3. Two parts within specification can have different expected loss if one is farther from target.

4. A point beyond UCL triggers investigation even if the item is still within specification.

5. For a centered process, Cp=Cpk.

6. A stricter plan reduces acceptance of poor lots but may reject more good lots.

7. An interaction means one factor’s effect depends on another factor’s level.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. Use §74.1. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

2. Use §74.2. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

3. Use §74.3. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

4. Use §74.4. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

5. Use §74.5. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

6. Use §74.6. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

7. Use §74.7. Apply the stated relation/workflow and verify feasibility, assumptions, and operational meaning.

8. Check units, probability bounds, utilization/stability, integer or physical constraints, denominator definitions, and model assumptions.

9. Start with FE Industrial & Systems specification Area(s) 12, then use the corresponding Handbook subsection where one exists.

10. Compare the result against upstream/downstream throughput, quality, inventory, safety, staffing, cost, and service.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 12.

- **industrial quality system:** Quality Planning, Assurance, Control, and Improvement
- **quality function deployment:** QFD and House of Quality
- **quality loss function:** Cause-and-Effect and Taguchi Loss
- **statistical process control:** Control Charts and SPC
- **process capability index:** Process Capability Cp and Cpk
- **acceptance sampling OC curve:** Acceptance Sampling and OC Curves
- **industrial factorial design:** Factorial DOE, Interactions, and ANOVA

---

## What's Next

**Chapter 03-75: Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
