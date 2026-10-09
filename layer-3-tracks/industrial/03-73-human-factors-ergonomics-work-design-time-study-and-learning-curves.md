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

**Solution.** A usable warning must first be noticed, then correctly interpreted, then mapped to an available response. Increasing loudness or brightness alone is insufficient if the signal is ambiguous, masked, inconsistent with other controls, or provides no actionable guidance.

---

## 73.2 Anthropometry and Percentile Design

Clearance often accommodates larger users; reach often accommodates smaller users; adjustability can cover a broad range.

\\[\\text{design percentile depends on clearance, reach, and adjustability objective}\\]

![FIG-03-73-002: Textbook-quality industrial engineering diagram illustrating anthropometry and percentile design with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-002-anthropometry-and-percentile-design.png)

### Worked Example 2

**Problem.** A doorway should not be designed from only the 5th-percentile stature.

**Solution.** Clearance dimensions are generally designed toward larger users, whereas reach requirements often consider smaller users; adjustability can accommodate a wider population. If stature is tabulated in cm (or in), the selected high-percentile clearance dimension must be carried in that same length unit. Designing a doorway from only 5th-percentile stature would systematically exclude larger people.

---

## 73.3 Biomechanics and Cumulative Trauma

Ergonomic risk rises with force, awkward posture, repetition, vibration, and insufficient recovery.

\\[Risk=f(force,posture,repetition,duration,recovery)\\]

![FIG-03-73-003: Textbook-quality industrial engineering diagram illustrating biomechanics and cumulative trauma with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-003-biomechanics-and-cumulative-trauma.png)

### Worked Example 3

**Problem.** Raising a workpiece can reduce trunk flexion during repetitive assembly.

**Solution.** Raising the workpiece can reduce trunk flexion and the external moment about the low back during repetitive work. A complete ergonomic assessment still considers load, horizontal reach, asymmetry, frequency, duration, coupling, recovery, and population variation.

---

## 73.4 Industrial Hygiene and Noise

Industrial hygiene applies recognition, evaluation, and control to workplace hazards.

\\[\\text{identify}\\rightarrow\\text{assess}\\rightarrow\\text{control}\\rightarrow\\text{verify}\\]

![FIG-03-73-004: Textbook-quality industrial engineering diagram illustrating industrial hygiene and noise with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-004-industrial-hygiene-and-noise.png)

### Worked Example 4

**Problem.** Engineering noise control is preferable to relying only on hearing protection when feasible.

**Solution.** Engineering noise control acts on the source or transmission path and is preferred when feasible because it reduces exposure for multiple workers. Hearing protection remains important but depends on selection, fit, use, and program effectiveness.

---

## 73.5 Methods Analysis and Motion Economy

Methods analysis removes unnecessary movement and improves sequence, workplace arrangement, and tool use.

\\[\\text{document}\\rightarrow\\text{question}\\rightarrow\\text{redesign}\\rightarrow\\text{standardize}\\]

![FIG-03-73-005: Textbook-quality industrial engineering diagram illustrating methods analysis and motion economy with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-005-methods-analysis-and-motion-economy.png)

### Worked Example 5

**Problem.** Combining unnecessary handoffs can reduce travel and handling.

**Solution.** Methods analysis documents the current sequence, questions each operation/transport/delay/inspection/storage step, then eliminates, combines, rearranges, or simplifies work. Removing an unnecessary handoff can reduce travel and handling without increasing operator pace.

---

## 73.6 Time Study, Allowances, and Standard Time

Time study converts observed time to normal time and then applies allowances according to the stated basis.

\\[ST=NT\\times AF\\]

![FIG-03-73-006: Textbook-quality industrial engineering diagram illustrating time study, allowances, and standard time with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-006-time-study-allowances-and-standard-time.png)

### Worked Example 6

**Problem.** NT=10 min and a 15% job-time allowance gives ST=11.5 min.

**Solution.** Standard time is \(ST=NT(1+A)=10(1.15)=\mathbf{11.5\ min}\) when the 15% allowance is stated on a normal-time basis. If an allowance is defined on a different basis, the convention must be adjusted accordingly.

---

## 73.7 Work Sampling and Learning Curves

Work sampling estimates activity proportions; learning curves model task-time reduction with repetition.

\\[T_N=KN^s,\\quad s=\\frac{\\ln(LR)}{\\ln2}\\]

![FIG-03-73-007: Textbook-quality industrial engineering diagram illustrating work sampling and learning curves with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-73-007-work-sampling-and-learning-curves.png)

### Worked Example 7

**Problem.** An 80% learning rate means unit time falls to 80% when cumulative quantity doubles.

**Solution.** With an 80% learning rate, doubling cumulative production multiplies unit time by 0.80. In \(T_N=KN^s\), \(s=\ln(0.80)/\ln2\approx\mathbf{-0.322}\); the negative exponent represents declining time as experience increases.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For this chapter, the FE Reference Handbook relation and variable definitions control whenever the Handbook supplies them. Use the external source set **FREIVALDS, ISO6385, NIOSH_LIFT, NIOSH_NOISE** only for specification-required learned material not fully developed in the Handbook.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 10, 11; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Freivalds, A., & Niebel, B. W. (2014). *Niebel's Methods, Standards, & Work Design* (13th ed.). McGraw-Hill. ISBN 978-0-07-337636-3. Supporting scope: Methods engineering, time study, allowances, work sampling, human factors, ergonomics, and work design.
- ISO. (2016). *Ergonomics principles in the design of work systems* (ISO 6385:2016; confirmed current). Supporting scope: Integrated ergonomics principles for work-system design across the lifecycle.
- Waters, T. R., Putz-Anderson, V., & Garg, A. (1994; revised 2021). *Applications Manual for the Revised NIOSH Lifting Equation*. DHHS (NIOSH) Publication No. 94-110. DOI 10.26616/NIOSHPUB94110revised092021. Supporting scope: Manual-lifting risk assessment and Revised NIOSH Lifting Equation application.
- NIOSH. (1998). *Criteria for a Recommended Standard: Occupational Noise Exposure, Revised Criteria 1998*. DHHS (NIOSH) Publication No. 98-126. Supporting scope: Occupational-noise exposure criteria and hearing-loss prevention.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves**, the model boundary determines what is included in the decision. A valid solution must design for the appropriate population percentile, treat workload/biomechanics/noise as exposure problems, preserve allowance conventions, and check that method improvement does not increase ergonomic risk.

16. Units and operational definitions are part of the model, not formatting details. For **Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves**. The external sources FREIVALDS, ISO6385, NIOSH_LIFT, NIOSH_NOISE support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves** is to set allowance to zero and confirm standard time equals normal time; for a 100% learning rate confirm the learning-curve exponent is zero. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §73.1, **Displays, Controls, Workload, and Usability**, is based on \(\\text{performance}=f(\\text{perception, cognition, control, feedback, workload})\\). Interpret the result within the specific assumptions and system boundary of §73.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §73.2, **Anthropometry and Percentile Design**, is based on \(\\text{design percentile depends on clearance, reach, and adjustability objective}\\). Interpret the result within the specific assumptions and system boundary of §73.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §73.3, **Biomechanics and Cumulative Trauma**, is based on \(Risk=f(force,posture,repetition,duration,recovery)\\). Interpret the result within the specific assumptions and system boundary of §73.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §73.4, **Industrial Hygiene and Noise**, is based on \(\\text{identify}\\rightarrow\\text{assess}\\rightarrow\\text{control}\\rightarrow\\text{verify}\\). Interpret the result within the specific assumptions and system boundary of §73.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §73.5, **Methods Analysis and Motion Economy**, is based on \(\\text{document}\\rightarrow\\text{question}\\rightarrow\\text{redesign}\\rightarrow\\text{standardize}\\). Interpret the result within the specific assumptions and system boundary of §73.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §73.6, **Time Study, Allowances, and Standard Time**, is based on \(ST=NT\\times AF\\). Interpret the result within the specific assumptions and system boundary of §73.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §73.7, **Work Sampling and Learning Curves**, is based on \(T_N=KN^s,\\quad s=\\frac{\\ln(LR)}{\\ln2}\\). Interpret the result within the specific assumptions and system boundary of §73.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves.


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

1. **Independent solution for §73.1 — Displays, Controls, Workload, and Usability.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A usable warning must first be noticed, then correctly interpreted, then mapped to an available response. Increasing loudness or brightness alone is insufficient if the signal is ambiguous, masked, inconsistent with other controls, or provides no actionable guidance.

2. **Independent solution for §73.2 — Anthropometry and Percentile Design.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Clearance dimensions are generally designed toward larger users, whereas reach requirements often consider smaller users; adjustability can accommodate a wider population. If stature is tabulated in cm (or in), the selected high-percentile clearance dimension must be carried in that same length unit. Designing a doorway from only 5th-percentile stature would systematically exclude larger people.

3. **Independent solution for §73.3 — Biomechanics and Cumulative Trauma.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Raising the workpiece can reduce trunk flexion and the external moment about the low back during repetitive work. A complete ergonomic assessment still considers load, horizontal reach, asymmetry, frequency, duration, coupling, recovery, and population variation.

4. **Independent solution for §73.4 — Industrial Hygiene and Noise.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Engineering noise control acts on the source or transmission path and is preferred when feasible because it reduces exposure for multiple workers. Hearing protection remains important but depends on selection, fit, use, and program effectiveness.

5. **Independent solution for §73.5 — Methods Analysis and Motion Economy.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Methods analysis documents the current sequence, questions each operation/transport/delay/inspection/storage step, then eliminates, combines, rearranges, or simplifies work. Removing an unnecessary handoff can reduce travel and handling without increasing operator pace.

6. **Independent solution for §73.6 — Time Study, Allowances, and Standard Time.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Standard time is \(ST=NT(1+A)=10(1.15)=\mathbf{11.5\ min}\) when the 15% allowance is stated on a normal-time basis. If an allowance is defined on a different basis, the convention must be adjusted accordingly.

7. **Independent solution for §73.7 — Work Sampling and Learning Curves.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: With an 80% learning rate, doubling cumulative production multiplies unit time by 0.80. In \(T_N=KN^s\), \(s=\ln(0.80)/\ln2\approx\mathbf{-0.322}\); the negative exponent represents declining time as experience increases.

8. For an integrated **Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves** problem, reject any result that violates this chapter-specific screen: design for the appropriate population percentile, treat workload/biomechanics/noise as exposure problems, preserve allowance conventions, and check that method improvement does not increase ergonomic risk.

9. For **Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **FREIVALDS, ISO6385, NIOSH_LIFT, NIOSH_NOISE** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: set allowance to zero and confirm standard time equals normal time; for a 100% learning rate confirm the learning-curve exponent is zero. The reduced case should behave as stated before the full model is trusted.

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
