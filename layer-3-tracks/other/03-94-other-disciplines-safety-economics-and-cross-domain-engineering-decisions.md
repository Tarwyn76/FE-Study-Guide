---
chapter: "03-94"
title: "Other Disciplines Safety, Economics, and Cross-Domain Engineering Decisions"
layer: 3
tier: null
track: other_disciplines
template: integration
ledger_ids: [OTH-3-094-01, OTH-3-094-02, OTH-3-094-03, OTH-3-094-04, OTH-3-094-05, OTH-3-094-06, OTH-3-094-07]
routes: [other_disciplines]
status: drafted
---

# Chapter 03-94: Other Disciplines Safety, Economics, and Cross-Domain Engineering Decisions

> *"The Other Disciplines exam is less about owning one specialty and more about recognizing which engineering model governs the next problem."*

---

## Before You Start

**Prerequisites:** SAFE-2B-019-01 · ECON-2A-004-01 · MATH-1A-001-01 · PROF-2A-001-01

**Route:** FE Other Disciplines. This is a Layer 3 integration chapter.

**Ownership rule:** This chapter intentionally does **not** create new owners for statics, dynamics, materials, fluids, thermodynamics, electrical engineering, safety, economics, or other already-registered topics. Its concept atoms own only integration, transfer, and exam-strategy skills.

**Time:** About 75–100 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

This chapter develops **Other Disciplines Safety, Economics, and Cross-Domain Engineering Decisions** as a synthesis layer over prior canonical concepts. The FE Other Disciplines specification spans mathematics, probability/statistics, chemistry, instrumentation/controls, ethics, safety, economics, statics, dynamics, strength of materials, materials, fluid mechanics, basic electrical engineering, and thermodynamics/heat transfer. The track therefore emphasizes selection, transfer, and verification rather than duplicated ownership.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **94.1** Apply **Hazard identification and hierarchy of controls** in mixed FE problems.
* **94.2** Apply **Industrial hygiene, toxicology, and exposure limits** in mixed FE problems.
* **94.3** Apply **Pressure relief, emergency shutdown, fire, and electrical safety** in mixed FE problems.
* **94.4** Apply **Engineering-economics equivalence and project comparison** in mixed FE problems.
* **94.5** Apply **Uncertainty, expected value, and decision trees** in mixed FE problems.
* **94.6** Apply **Ethics, public protection, and societal impacts** in mixed FE problems.
* **94.7** Apply **Life-cycle and cross-domain decision synthesis** in mixed FE problems.

---

## Notation Used Here

Keep the notation of the underlying canonical discipline. When moving between domains, state the intermediate quantity, its units, and which model produced it before using it as the next model's input.

---

## 94.1 Hazard identification and hierarchy of controls

Safety decisions should control hazards at the source where practical rather than relying only on worker behavior or PPE.

\[\text{eliminate/substitute}\rightarrow\text{engineering}\rightarrow\text{administrative}\rightarrow\text{PPE}\]

![FIG-03-94-001: Hierarchy of controls with mechanical, chemical, electrical, and confined-space examples.](../figures/FIG-03-94-001-hazard-identification-and-hierarchy-of-controls.png)

### Worked Example 1

**Problem.** A fixed machine guard is generally a stronger control than warning signage alone.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §94.1.

---

## 94.2 Industrial hygiene, toxicology, and exposure limits

Other Disciplines safety questions may involve chemical, radiation, biological, noise, or gas exposure. Identify route, concentration, duration, and applicable limit basis.

\[\text{dose/exposure}=f(C,t,\text{route},\text{frequency})\]

![FIG-03-94-002: Worker exposure pathways with concentration/time profile, monitoring, limits, and control measures.](../figures/FIG-03-94-002-industrial-hygiene-toxicology-and-exposure-limits.png)

### Worked Example 2

**Problem.** A short-term exposure limit cannot be evaluated using only an 8-hour average if the peak matters.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §94.2.

---

## 94.3 Pressure relief, emergency shutdown, fire, and electrical safety

Protection layers must match the hazard: pressure relief for overpressure, emergency shutdown for dangerous process states, grounding/overcurrent protection for electrical hazards, and fire prevention/control for combustible systems.

\[\text{hazard}\rightarrow\text{detection}\rightarrow\text{protective action}\rightarrow\text{safe state}\]

![FIG-03-94-003: Process vessel/equipment with relief, shutdown, gas detection, grounding, and fire protection layers.](../figures/FIG-03-94-003-pressure-relief-emergency-shutdown-fire-and-electrical-safety.png)

### Worked Example 3

**Problem.** A relief valve protects pressure equipment from overpressure but does not substitute for eliminating an ignition source.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §94.3.

---

## 94.4 Engineering-economics equivalence and project comparison

Economic decisions require a common time basis. Present worth, annual worth, future worth, rate of return, and benefit-cost methods are alternative comparison frames.

\[PW=\sum_t\frac{CF_t}{(1+i)^t}\]

![FIG-03-94-004: Two alternative project cash-flow diagrams brought to a common economic basis.](../figures/FIG-03-94-004-engineering-economics-equivalence-and-project-comparison.png)

### Worked Example 4

**Problem.** Two projects with unequal lives should not be compared by raw total cash flow alone.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §94.4.

---

## 94.5 Uncertainty, expected value, and decision trees

Expected value combines outcomes with probabilities, but risk tolerance, safety constraints, and irreversible consequences may make expected value insufficient by itself.

\[E[X]=\sum p_ix_i\]

![FIG-03-94-005: Decision tree with alternatives, chance nodes, probabilities, outcomes, expected values, and safety constraints.](../figures/FIG-03-94-005-uncertainty-expected-value-and-decision-trees.png)

### Worked Example 5

**Problem.** A low-probability catastrophic safety consequence may dominate a design decision even when expected monetary loss is modest.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §94.5.

---

## 94.6 Ethics, public protection, and societal impacts

FE ethics questions test professional obligations, conflicts, competence, disclosure, and protection of the public. Technical feasibility or profitability does not override professional duties.

\[\text{engineering decision}\rightarrow\text{public safety+welfare+ethics+law+technical evidence}\]

![FIG-03-94-006: Decision flow from technical issue through code obligations, public welfare, conflict disclosure, escalation, and documentation.](../figures/FIG-03-94-006-ethics-public-protection-and-societal-impacts.png)

### Worked Example 6

**Problem.** An engineer who discovers a material safety defect must address the public-safety implications rather than treating it as only a cost issue.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §94.6.

---

## 94.7 Life-cycle and cross-domain decision synthesis

A sound cross-domain decision integrates technical performance, safety, reliability, environmental impact, maintainability, economics, ethics, and uncertainty across the lifecycle.

\[\text{best decision}\neq\text{minimum first cost alone}\]

![FIG-03-94-007: Multi-criteria lifecycle decision matrix covering performance, safety, reliability, environment, maintainability, cost, and uncertainty.](../figures/FIG-03-94-007-life-cycle-and-cross-domain-decision-synthesis.png)

### Worked Example 7

**Problem.** A cheaper pump with lower efficiency and shorter life can have a higher lifecycle cost and larger environmental impact than a higher first-cost alternative.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §94.7.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A mixed question contains electrical, mechanical, and economic information. Must every datum be used?

**Solution.** No. First identify the requested quantity and governing model. Use only the data needed for the current stage, then carry the resulting intermediate quantity—clearly labeled with units—into the next stage if required.

### Worked Example 9

**Problem.** You find a familiar equation in memory but a different-looking form in the FE Reference Handbook. What should you do?

**Solution.** Use the Handbook form after checking its definitions and assumptions. Do not force a remembered formula onto a problem merely because it resembles the topic.

---

## As the Handbook States It

**Primary source basis:** FE Other Disciplines CBT specification, printed pp. 498–500. Unlike the six discipline-specific FE routes, Other Disciplines has no dedicated discipline section in Handbook 10.6; it relies on the general Handbook sections across the book.

**Source boundary:** The integration workflow, classification strategy, and cross-domain transfer methods are guide-developed. Underlying equations remain owned and sourced by their canonical earlier chapters.

---

## Where This Goes Wrong

**Re-owning a shared concept.** This track must point back to the existing owner rather than creating a second independent definition of the same method.

**Using every number because it was supplied.** Mixed FE questions can include distractors; the requested quantity and governing model determine relevance.

**Losing units at domain boundaries.** Intermediate power, force, flow, concentration, temperature, or cost quantities must carry explicit units into the next calculation.

**Treating the Handbook search as the first reasoning step.** Classify the physics/discipline first, then search targeted terms.

---

## Key Terms

| Term | Integration role |
|---|---|
| cross-domain hazard control | Synthesis concept in §94.1; coordinates prior canonical owners without duplicating them. |
| cross-domain exposure assessment | Synthesis concept in §94.2; coordinates prior canonical owners without duplicating them. |
| engineered safety protection | Synthesis concept in §94.3; coordinates prior canonical owners without duplicating them. |
| cross-domain economic comparison | Synthesis concept in §94.4; coordinates prior canonical owners without duplicating them. |
| engineering decision under uncertainty | Synthesis concept in §94.5; coordinates prior canonical owners without duplicating them. |
| cross-domain professional judgment | Synthesis concept in §94.6; coordinates prior canonical owners without duplicating them. |
| life-cycle engineering decision | Synthesis concept in §94.7; coordinates prior canonical owners without duplicating them. |

---

## Review Questions

### Conceptual and Applied

1. Define **cross-domain hazard control** and explain what cross-domain decision or transfer skill it supports.

2. Define **cross-domain exposure assessment** and explain what cross-domain decision or transfer skill it supports.

3. Define **engineered safety protection** and explain what cross-domain decision or transfer skill it supports.

4. Define **cross-domain economic comparison** and explain what cross-domain decision or transfer skill it supports.

5. Define **engineering decision under uncertainty** and explain what cross-domain decision or transfer skill it supports.

6. Define **cross-domain professional judgment** and explain what cross-domain decision or transfer skill it supports.

7. Define **life-cycle engineering decision** and explain what cross-domain decision or transfer skill it supports.

8. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain hazard control**?

9. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain exposure assessment**?

10. What is the most important assumption, boundary, unit, or prior-concept check before applying **engineered safety protection**?

11. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain economic comparison**?

12. What is the most important assumption, boundary, unit, or prior-concept check before applying **engineering decision under uncertainty**?

13. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain professional judgment**?

14. What is the most important assumption, boundary, unit, or prior-concept check before applying **life-cycle engineering decision**?

15. Why should an Other Disciplines problem be classified before searching the Handbook?

16. Why is cross-domain synthesis different from creating a new copy of a previously owned concept?

17. What should you do when two equations look plausible but use different assumptions or variable definitions?

18. Why should every final answer receive a units, sign, magnitude, and physical/ethical feasibility check?

### Multiple Choice

19. Which statement is most accurate for **cross-domain hazard control**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

20. Which statement is most accurate for **cross-domain exposure assessment**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

21. Which statement is most accurate for **engineered safety protection**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

22. Which statement is most accurate for **cross-domain economic comparison**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

23. Which statement is most accurate for **engineering decision under uncertainty**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

24. Which statement is most accurate for **cross-domain professional judgment**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

25. Which statement is most accurate for **life-cycle engineering decision**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

26. Which statement is most accurate for **cross-domain hazard control**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

27. Which statement is most accurate for **cross-domain exposure assessment**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation


---

## Answer Key with Explanations

1. **cross-domain hazard control** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

2. **cross-domain exposure assessment** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

3. **engineered safety protection** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

4. **cross-domain economic comparison** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

5. **engineering decision under uncertainty** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

6. **cross-domain professional judgment** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

7. **life-cycle engineering decision** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

8. For **cross-domain hazard control**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

9. For **cross-domain exposure assessment**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

10. For **engineered safety protection**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

11. For **cross-domain economic comparison**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

12. For **engineering decision under uncertainty**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

13. For **cross-domain professional judgment**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

14. For **life-cycle engineering decision**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

15. Classification narrows the search space and prevents using a familiar equation from the wrong discipline or physical model.

16. The canonical concept already exists in an earlier layer/track; the integration atom teaches when and how to reuse it in a mixed problem.

17. Compare variable definitions, units, boundary conditions, and operating assumptions. Use the relation that matches the actual problem and Handbook context.

18. These checks catch wrong-domain solutions, hidden conversion errors, impossible signs or efficiencies, and decisions that violate physical, safety, or professional constraints.

19. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

20. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

21. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

22. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

23. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

24. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

25. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

26. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.

27. **A.** The integration concept coordinates earlier canonical owners and still requires assumption and unit checks.


---

## Practice Problems

1. A fixed machine guard is generally a stronger control than warning signage alone.

2. A short-term exposure limit cannot be evaluated using only an 8-hour average if the peak matters.

3. A relief valve protects pressure equipment from overpressure but does not substitute for eliminating an ignition source.

4. Two projects with unequal lives should not be compared by raw total cash flow alone.

5. A low-probability catastrophic safety consequence may dominate a design decision even when expected monetary loss is modest.

6. An engineer who discovers a material safety defect must address the public-safety implications rather than treating it as only a cost issue.

7. A cheaper pump with lower efficiency and shorter life can have a higher lifecycle cost and larger environmental impact than a higher first-cost alternative.

8. For a mixed-domain problem, write the sequence of discipline models you would use and the intermediate quantity passed between each.

9. State the FE Other Disciplines specification page range and explain why there is no dedicated Other Disciplines Handbook section.

10. Give one fast check that would cause you to reject an otherwise algebraically consistent FE answer.


---

## Practice Problem Solutions

1. Use §94.1. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

2. Use §94.2. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

3. Use §94.3. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

4. Use §94.4. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

5. Use §94.5. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

6. Use §94.6. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

7. Use §94.7. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

8. Example structure: electrical input power → motor efficiency → shaft power → pump/fluid model → operating cost. Every arrow must carry a defined quantity and units.

9. The FE Other Disciplines specification is printed on pp. 498–500. The route has no dedicated discipline chapter in Handbook 10.6, so examinees use the relevant general sections instead.

10. Reject answers with impossible units, efficiencies above 100% where not physically meaningful, negative absolute quantities, violated support/device states, broken conservation, or unsafe/unethical implementation assumptions.

---

## Quick Reference

**Source anchor:** FE Other Disciplines CBT specification, printed pp. 498–500.

- **cross-domain hazard control:** Hazard identification and hierarchy of controls
- **cross-domain exposure assessment:** Industrial hygiene, toxicology, and exposure limits
- **engineered safety protection:** Pressure relief, emergency shutdown, fire, and electrical safety
- **cross-domain economic comparison:** Engineering-economics equivalence and project comparison
- **engineering decision under uncertainty:** Uncertainty, expected value, and decision trees
- **cross-domain professional judgment:** Ethics, public protection, and societal impacts
- **life-cycle engineering decision:** Life-cycle and cross-domain decision synthesis

---

## What's Next

**Chapter 03-95: Other Disciplines Mixed FE Synthesis and Handbook Strategy**

For the Other Disciplines route, keep practicing the same transfer loop: classify the problem, locate the canonical model, use the Handbook deliberately, solve with explicit units, then verify the result across domain boundaries.

— Your Mentor
