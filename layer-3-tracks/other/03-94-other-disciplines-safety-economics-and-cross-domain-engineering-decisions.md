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

**Solution.** A fixed guard is an engineering control because it physically prevents contact with the hazard without relying on a worker to remember a rule. Warning signs are administrative controls and generally rank lower in the hierarchy because effectiveness depends more heavily on human behavior.

---

## 94.2 Industrial hygiene, toxicology, and exposure limits

Other Disciplines safety questions may involve chemical, radiation, biological, noise, or gas exposure. Identify route, concentration, duration, and applicable limit basis.

\[\text{dose/exposure}=f(C,t,\text{route},\text{frequency})\]

![FIG-03-94-002: Worker exposure pathways with concentration/time profile, monitoring, limits, and control measures.](../figures/FIG-03-94-002-industrial-hygiene-toxicology-and-exposure-limits.png)

### Worked Example 2

**Problem.** A short-term exposure limit cannot be evaluated using only an 8-hour average if the peak matters.

**Solution.** An 8-hour TWA and a short-term exposure limit answer different questions. A compliant daily average can still contain an unacceptable 15-minute peak, so compare each averaging interval with the corresponding occupational exposure criterion.

---

## 94.3 Pressure relief, emergency shutdown, fire, and electrical safety

Protection layers must match the hazard: pressure relief for overpressure, emergency shutdown for dangerous process states, grounding/overcurrent protection for electrical hazards, and fire prevention/control for combustible systems.

\[\text{hazard}\rightarrow\text{detection}\rightarrow\text{protective action}\rightarrow\text{safe state}\]

![FIG-03-94-003: Process vessel/equipment with relief, shutdown, gas detection, grounding, and fire protection layers.](../figures/FIG-03-94-003-pressure-relief-emergency-shutdown-fire-and-electrical-safety.png)

### Worked Example 3

**Problem.** A relief valve protects pressure equipment from overpressure but does not substitute for eliminating an ignition source.

**Solution.** A relief valve mitigates one consequence—overpressure—by opening a discharge path at its set condition. Ignition control addresses a different hazard pathway. Layered protection requires each safeguard to be credited only for the failure mode it can actually prevent or mitigate.

---

## 94.4 Engineering-economics equivalence and project comparison

Economic decisions require a common time basis. Present worth, annual worth, future worth, rate of return, and benefit-cost methods are alternative comparison frames.

\[PW=\sum_t\frac{CF_t}{(1+i)^t}\]

![FIG-03-94-004: Two alternative project cash-flow diagrams brought to a common economic basis.](../figures/FIG-03-94-004-engineering-economics-equivalence-and-project-comparison.png)

### Worked Example 4

**Problem.** Two projects with unequal lives should not be compared by raw total cash flow alone.

**Solution.** Unequal-life alternatives should be compared on an equivalent economic basis such as present worth over a common study period, annual worth, or repeatability assumptions. Adding undiscounted cash flows ignores both time value and unequal service duration.

---

## 94.5 Uncertainty, expected value, and decision trees

Expected value combines outcomes with probabilities, but risk tolerance, safety constraints, and irreversible consequences may make expected value insufficient by itself.

\[E[X]=\sum p_ix_i\]

![FIG-03-94-005: Decision tree with alternatives, chance nodes, probabilities, outcomes, expected values, and safety constraints.](../figures/FIG-03-94-005-uncertainty-expected-value-and-decision-trees.png)

### Worked Example 5

**Problem.** A low-probability catastrophic safety consequence may dominate a design decision even when expected monetary loss is modest.

**Solution.** Expected monetary value is not a complete safety criterion when consequences are severe, irreversible, or constrained by law/ethics. A low-probability fatal or catastrophic outcome may require risk reduction even when \(p\times\) monetary consequence appears small.

---

## 94.6 Ethics, public protection, and societal impacts

FE ethics questions test professional obligations, conflicts, competence, disclosure, and protection of the public. Technical feasibility or profitability does not override professional duties.

\[\text{engineering decision}\rightarrow\text{public safety+welfare+ethics+law+technical evidence}\]

![FIG-03-94-006: Decision flow from technical issue through code obligations, public welfare, conflict disclosure, escalation, and documentation.](../figures/FIG-03-94-006-ethics-public-protection-and-societal-impacts.png)

### Worked Example 6

**Problem.** An engineer who discovers a material safety defect must address the public-safety implications rather than treating it as only a cost issue.

**Solution.** Professional duty is not reduced to a cost trade. Once a material defect can affect public safety, the engineer must communicate and address the hazard through the applicable professional, organizational, and legal channels rather than suppressing it for schedule or budget reasons.

---

## 94.7 Life-cycle and cross-domain decision synthesis

A sound cross-domain decision integrates technical performance, safety, reliability, environmental impact, maintainability, economics, ethics, and uncertainty across the lifecycle.

\[\text{best decision}\neq\text{minimum first cost alone}\]

![FIG-03-94-007: Multi-criteria lifecycle decision matrix covering performance, safety, reliability, environment, maintainability, cost, and uncertainty.](../figures/FIG-03-94-007-life-cycle-and-cross-domain-decision-synthesis.png)

### Worked Example 7

**Problem.** A cheaper pump with lower efficiency and shorter life can have a higher lifecycle cost and larger environmental impact than a higher first-cost alternative.

**Solution.** Compare the alternatives over the same service function and life. A lower-price pump can lose economically through higher energy use, maintenance, downtime, and earlier replacement; those same inefficiencies can also increase lifecycle resource use and emissions.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A mixed question contains electrical, mechanical, and economic information. Must every datum be used?

**Solution.** No. A safety/economics decision should use only data tied to the hazard, exposure, safeguard, cash-flow, probability, or ethical constraint being evaluated. A datum becomes relevant only when it enters that decision model or a preceding dependency.

### Worked Example 9

**Problem.** You find a familiar equation in memory but a different-looking form in the FE Reference Handbook. What should you do?

**Solution.** For economics, probability, and safety calculations, use the Handbook equation or table whose averaging basis, cash-flow timing, probability definition, or risk metric matches the prompt. External standards supply context, not a reason to override the exam reference.

---

## As the Handbook States It

**Primary source basis:** FE Other Disciplines CBT specification, printed pp. 498–500. Unlike the six discipline-specific FE routes, Other Disciplines has no dedicated discipline section in Handbook 10.6; it relies on the general Handbook sections across the book.

**Source boundary:** **FE-Handbook-supported** material consists of the underlying equations, tables, definitions, and discipline models located in the FE Reference Handbook and recorded in the ledger. **Externally supported** material covers Other Disciplines specification knowledge, application context, standards, and integration details that are not fully developed in the Handbook. **Guide synthesis** is the cross-domain classification, transfer, verification, and exam-strategy workflow created for this supplemental guide; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- National Institute for Occupational Safety and Health. (2024). *Hierarchy of Controls*. Centers for Disease Control and Prevention. Supporting scope: Preferred sequence of elimination, substitution, engineering controls, administrative controls, and PPE.
- National Institute for Occupational Safety and Health. *NIOSH Pocket Guide to Chemical Hazards*, current online edition. Supporting scope: Industrial-hygiene chemical data, RELs/PELs, exposure routes, symptoms, target organs, control information, and measurement methods.
- U.S. Environmental Protection Agency. (2011). *Exposure Factors Handbook: 2011 Edition* (EPA/600/R-09/052F), with subsequent chapter updates where applicable. Supporting scope: Exposure factors, variability/uncertainty, inhalation/ingestion/dermal inputs, body weight, activity patterns, and human-exposure calculations.
- Newnan, D. G., Eschenbach, T. G., Lavelle, J. P., & Lewis, N. A. *Engineering Economic Analysis* (14th ed.). Oxford University Press. Supporting scope: Engineering-economic equivalence, alternative comparison, life-cycle cost, uncertainty, expected value, and economic decision making.
- Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.). Wiley. Supporting scope: Probability, random variables, expected value, statistical inference, uncertainty, and engineering data analysis.
- National Society of Professional Engineers. *NSPE Code of Ethics for Engineers* (rev. July 2019). Supporting scope: Public safety, health and welfare, competence, truthfulness, professional conduct, and engineering ethics.

Because Other Disciplines intentionally integrates material owned by earlier chapters, external references support the learned/application and cross-domain portions only. The FE Reference Handbook remains the exam reference, and the ledger retains the canonical Handbook locations for the underlying equations.

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

15. Safety/economics problems must first be classified as hazard control, exposure assessment, protective-system design, economic comparison, uncertainty, or ethics. That keeps exposure limits, discounted cash-flow equations, and professional-duty rules from being mixed into the wrong decision.

16. The component risk, economics, probability, and ethics concepts are sourced elsewhere; this chapter combines them when one engineering choice has several consequences. Integration is therefore about trade-space structure and constraints rather than duplicating each specialty model.

17. Match the averaging period, exposure route, cash-flow timing, probability model, and legal/ethical constraint before choosing among plausible equations. A TWA, STEL, present-worth factor, or expected-value model is valid only for its own defined basis.

18. A decision can fail even when the arithmetic is right. Check exposure limits, safeguard independence, probability bounds, equivalent economic basis, public-safety obligations, and lifecycle consequences before accepting the preferred alternative.

19. **A.** Hazard control should preferentially remove or reduce the hazard at its source through elimination, substitution, or engineering controls before relying on procedures or PPE. The chosen control must address the actual exposure pathway.

20. **A.** Exposure assessment requires concentration/intensity, duration, frequency, route, and the averaging period tied to the applicable limit or toxicity metric. A single average cannot represent every acute and chronic criterion.

21. **A.** Relief, shutdown, fire protection, electrical protection, and similar safeguards are engineered layers with specific initiating conditions and failure modes. Credit only safeguards that are independent enough and actually act on the scenario being evaluated.

22. **A.** Economic comparison requires equivalent service and time basis. Discounted present/annual worth, replacement assumptions, and operating costs are needed before alternatives with different timing or lives can be compared fairly.

23. **A.** Expected value is useful for uncertain outcomes, but decision trees must retain conditional probabilities and consequence structure. Safety/legal constraints may dominate even when expected monetary value favors a riskier alternative.

24. **A.** Professional judgment is bounded by protection of the public, competence, truthful communication, and applicable law/standards. Cost or schedule pressure does not cancel those duties.

25. **A.** Lifecycle decisions combine acquisition, energy, maintenance, reliability, safety, environmental burden, and end-of-life effects. The least first-cost option is not automatically the best engineering choice.

26. **A.** A hazard-control decision should document the hazard, exposure path, selected layer of control, residual risk, and verification method. A lower-ranked control is not equivalent to eliminating or engineering out the hazard merely because it is cheaper.

27. **A.** Exposure assessment must distinguish concentration from dose, acute from chronic averaging periods, and legal limits from recommended or risk-based values. Those distinctions determine which number can be compared with which criterion.


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

1. Apply the §94.1 model independently. Hazard control should preferentially remove or reduce the hazard at its source through elimination, substitution, or engineering controls before relying on procedures or PPE. The chosen control must address the actual exposure pathway. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

2. Apply the §94.2 model independently. Exposure assessment requires concentration/intensity, duration, frequency, route, and the averaging period tied to the applicable limit or toxicity metric. A single average cannot represent every acute and chronic criterion. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

3. Apply the §94.3 model independently. Relief, shutdown, fire protection, electrical protection, and similar safeguards are engineered layers with specific initiating conditions and failure modes. Credit only safeguards that are independent enough and actually act on the scenario being evaluated. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

4. Apply the §94.4 model independently. Economic comparison requires equivalent service and time basis. Discounted present/annual worth, replacement assumptions, and operating costs are needed before alternatives with different timing or lives can be compared fairly. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

5. Apply the §94.5 model independently. Expected value is useful for uncertain outcomes, but decision trees must retain conditional probabilities and consequence structure. Safety/legal constraints may dominate even when expected monetary value favors a riskier alternative. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

6. Apply the §94.6 model independently. Professional judgment is bounded by protection of the public, competence, truthful communication, and applicable law/standards. Cost or schedule pressure does not cancel those duties. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

7. Apply the §94.7 model independently. Lifecycle decisions combine acquisition, energy, maintenance, reliability, safety, environmental burden, and end-of-life effects. The least first-cost option is not automatically the best engineering choice. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

8. For a cross-domain decision, sequence hazard/exposure identification → safeguard or design alternatives → probability/consequence assessment → equivalent economic comparison → ethics/legal/public-safety constraint check. Some constraints can eliminate an option before cost comparison.

9. The specification defines Other Disciplines on printed pp. 498–500; safety, probability, economics, and ethics material is distributed through the general Handbook sections instead of being repeated in a separate Other Disciplines section.

10. Reject an economically attractive option if it violates a safety limit, depends on an invalid probability, ignores a required safeguard, or conflicts with the engineer's duty to protect the public.

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
