---
chapter: "03-93"
title: "Other Disciplines Electrical, Instrumentation, and Control Integration"
layer: 3
tier: null
track: other_disciplines
template: integration
ledger_ids: [OTH-3-093-01, OTH-3-093-02, OTH-3-093-03, OTH-3-093-04, OTH-3-093-05, OTH-3-093-06, OTH-3-093-07]
routes: [other_disciplines]
status: drafted
---

# Chapter 03-93: Other Disciplines Electrical, Instrumentation, and Control Integration

> *"The Other Disciplines exam is less about owning one specialty and more about recognizing which engineering model governs the next problem."*

---

## Before You Start

**Prerequisites:** ELEC-2E-059-01 · INST-2F-066-01 · CTRL-2F-069-01 · MEC-3-089-01

**Route:** FE Other Disciplines. This is a Layer 3 integration chapter.

**Ownership rule:** This chapter intentionally does **not** create new owners for statics, dynamics, materials, fluids, thermodynamics, electrical engineering, safety, economics, or other already-registered topics. Its concept atoms own only integration, transfer, and exam-strategy skills.

**Time:** About 75–100 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

This chapter develops **Other Disciplines Electrical, Instrumentation, and Control Integration** as a synthesis layer over prior canonical concepts. The FE Other Disciplines specification spans mathematics, probability/statistics, chemistry, instrumentation/controls, ethics, safety, economics, statics, dynamics, strength of materials, materials, fluid mechanics, basic electrical engineering, and thermodynamics/heat transfer. The track therefore emphasizes selection, transfer, and verification rather than duplicated ownership.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **93.1** Apply **Electrical quantities, power, and safe circuit abstraction** in mixed FE problems.
* **93.2** Apply **Kirchhoff laws, impedance, and AC/DC network solving** in mixed FE problems.
* **93.3** Apply **Electrical power, power factor, and three-phase loads** in mixed FE problems.
* **93.4** Apply **Sensors, range, sensitivity, and signal conditioning** in mixed FE problems.
* **93.5** Apply **Sampling rate, aliasing, filtering, and A/D resolution** in mixed FE problems.
* **93.6** Apply **Feedback, block diagrams, and dynamic response** in mixed FE problems.
* **93.7** Apply **Logic, interlocks, alarms, and fail-safe design** in mixed FE problems.

---

## Notation Used Here

Keep the notation of the underlying canonical discipline. When moving between domains, state the intermediate quantity, its units, and which model produced it before using it as the next model's input.

---

## 93.1 Electrical quantities, power, and safe circuit abstraction

Other Disciplines electrical questions emphasize fundamentals rather than deep electronics. Start by identifying DC, AC, steady-state, transient, single-phase, or three-phase context.

\[V=IR,\qquad P=VI\]

![FIG-03-93-001: Electrical problem classification from source/load type through DC/AC, impedance, power, measurement, and safety checks.](../figures/FIG-03-93-001-electrical-quantities-power-and-safe-circuit-abstraction.png)

### Worked Example 1

**Problem.** A 24-V load drawing 2 A consumes 48 W.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §93.1.

---

## 93.2 Kirchhoff laws, impedance, and AC/DC network solving

Use node/loop laws consistently with complex impedance for sinusoidal steady-state AC. Do not mix RMS and peak values without conversion.

\[\sum V=0,\qquad \sum I=0,\qquad Z=R+jX\]

![FIG-03-93-002: DC and AC circuit examples linked to KCL/KVL, impedance, phasors, and power calculations.](../figures/FIG-03-93-002-kirchhoff-laws-impedance-and-ac-dc-network-solving.png)

### Worked Example 2

**Problem.** A resistor and inductor in series have impedance R+jωL.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §93.2.

---

## 93.3 Electrical power, power factor, and three-phase loads

Power questions may connect motors, heaters, pumps, and process equipment. Apparent, real, and reactive power must remain distinct.

\[P=\sqrt3\,V_LI_L\cos\phi\]

![FIG-03-93-003: Balanced three-phase load with line voltage/current and power triangle tied to a motor-driven process load.](../figures/FIG-03-93-003-electrical-power-power-factor-and-three-phase-loads.png)

### Worked Example 3

**Problem.** A 480-V balanced three-phase motor at 20 A and 0.8 power factor draws about 13.3 kW real power.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §93.3.

---

## 93.4 Sensors, range, sensitivity, and signal conditioning

Measurement problems connect sensor physics to usable electrical signals. Range, sensitivity, linearity, loading, amplification, filtering, and grounding all affect the result.

\[\text{measurand}\rightarrow\text{sensor}\rightarrow\text{conditioning}\rightarrow\text{DAQ}\]

![FIG-03-93-004: Pressure/temperature/pH sensors through transmitter, amplifier/filter, A/D converter, and logging system.](../figures/FIG-03-93-004-sensors-range-sensitivity-and-signal-conditioning.png)

### Worked Example 4

**Problem.** A 0–100 psi transmitter producing 4–20 mA has 0.16 mA/psi sensitivity.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §93.4.

---

## 93.5 Sampling rate, aliasing, filtering, and A/D resolution

DAQ design must sample fast enough to represent the signal and provide enough resolution for the required measurement. Anti-alias filtering belongs before the sampler.

\[f_s>2f_{max},\qquad \Delta=\frac{V_{FS}}{2^N}\]

![FIG-03-93-005: Analog signal through anti-alias filter, sampler, N-bit ADC, digital logger, and reconstructed spectrum.](../figures/FIG-03-93-005-sampling-rate-aliasing-filtering-and-a-d-resolution.png)

### Worked Example 5

**Problem.** A 12-bit ADC over 0–10 V has ideal step size about 2.44 mV.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §93.5.

---

## 93.6 Feedback, block diagrams, and dynamic response

Control questions connect sensors, controllers, actuators, and process dynamics. Negative feedback can reduce sensitivity and tracking error but can destabilize a poorly designed loop.

\[T(s)=\frac{G(s)}{1+G(s)H(s)}\]

![FIG-03-93-006: Closed-loop process with setpoint, controller, actuator, plant, sensor, disturbance, and feedback path.](../figures/FIG-03-93-006-feedback-block-diagrams-and-dynamic-response.png)

### Worked Example 6

**Problem.** Increasing loop gain can reduce steady tracking error while potentially reducing stability margin.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §93.6.

---

## 93.7 Logic, interlocks, alarms, and fail-safe design

Industrial systems use Boolean logic to convert sensor states into alarms, permissives, trips, and safe-state actions. Logic must be interpreted together with sensor failure modes and de-energized states.

\[\text{trip}=\text{hazard condition}\land\text{permissive/interlock logic}\]

![FIG-03-93-007: Cause-and-effect matrix and simple logic diagram for alarm, permissive, and emergency shutdown.](../figures/FIG-03-93-007-logic-interlocks-alarms-and-fail-safe-design.png)

### Worked Example 7

**Problem.** A normally energized trip circuit can be designed so loss of power produces a safe shutdown.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §93.7.

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
| cross-domain electrical model | Synthesis concept in §93.1; coordinates prior canonical owners without duplicating them. |
| circuit synthesis workflow | Synthesis concept in §93.2; coordinates prior canonical owners without duplicating them. |
| cross-domain three-phase power | Synthesis concept in §93.3; coordinates prior canonical owners without duplicating them. |
| instrumentation signal chain | Synthesis concept in §93.4; coordinates prior canonical owners without duplicating them. |
| data acquisition sampling | Synthesis concept in §93.5; coordinates prior canonical owners without duplicating them. |
| cross-domain feedback control | Synthesis concept in §93.6; coordinates prior canonical owners without duplicating them. |
| engineering interlock logic | Synthesis concept in §93.7; coordinates prior canonical owners without duplicating them. |

---

## Review Questions

### Conceptual and Applied

1. Define **cross-domain electrical model** and explain what cross-domain decision or transfer skill it supports.

2. Define **circuit synthesis workflow** and explain what cross-domain decision or transfer skill it supports.

3. Define **cross-domain three-phase power** and explain what cross-domain decision or transfer skill it supports.

4. Define **instrumentation signal chain** and explain what cross-domain decision or transfer skill it supports.

5. Define **data acquisition sampling** and explain what cross-domain decision or transfer skill it supports.

6. Define **cross-domain feedback control** and explain what cross-domain decision or transfer skill it supports.

7. Define **engineering interlock logic** and explain what cross-domain decision or transfer skill it supports.

8. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain electrical model**?

9. What is the most important assumption, boundary, unit, or prior-concept check before applying **circuit synthesis workflow**?

10. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain three-phase power**?

11. What is the most important assumption, boundary, unit, or prior-concept check before applying **instrumentation signal chain**?

12. What is the most important assumption, boundary, unit, or prior-concept check before applying **data acquisition sampling**?

13. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain feedback control**?

14. What is the most important assumption, boundary, unit, or prior-concept check before applying **engineering interlock logic**?

15. Why should an Other Disciplines problem be classified before searching the Handbook?

16. Why is cross-domain synthesis different from creating a new copy of a previously owned concept?

17. What should you do when two equations look plausible but use different assumptions or variable definitions?

18. Why should every final answer receive a units, sign, magnitude, and physical/ethical feasibility check?

### Multiple Choice

19. Which statement is most accurate for **cross-domain electrical model**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

20. Which statement is most accurate for **circuit synthesis workflow**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

21. Which statement is most accurate for **cross-domain three-phase power**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

22. Which statement is most accurate for **instrumentation signal chain**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

23. Which statement is most accurate for **data acquisition sampling**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

24. Which statement is most accurate for **cross-domain feedback control**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

25. Which statement is most accurate for **engineering interlock logic**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

26. Which statement is most accurate for **cross-domain electrical model**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

27. Which statement is most accurate for **circuit synthesis workflow**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation


---

## Answer Key with Explanations

1. **cross-domain electrical model** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

2. **circuit synthesis workflow** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

3. **cross-domain three-phase power** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

4. **instrumentation signal chain** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

5. **data acquisition sampling** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

6. **cross-domain feedback control** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

7. **engineering interlock logic** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

8. For **cross-domain electrical model**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

9. For **circuit synthesis workflow**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

10. For **cross-domain three-phase power**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

11. For **instrumentation signal chain**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

12. For **data acquisition sampling**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

13. For **cross-domain feedback control**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

14. For **engineering interlock logic**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

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

1. A 24-V load drawing 2 A consumes 48 W.

2. A resistor and inductor in series have impedance R+jωL.

3. A 480-V balanced three-phase motor at 20 A and 0.8 power factor draws about 13.3 kW real power.

4. A 0–100 psi transmitter producing 4–20 mA has 0.16 mA/psi sensitivity.

5. A 12-bit ADC over 0–10 V has ideal step size about 2.44 mV.

6. Increasing loop gain can reduce steady tracking error while potentially reducing stability margin.

7. A normally energized trip circuit can be designed so loss of power produces a safe shutdown.

8. For a mixed-domain problem, write the sequence of discipline models you would use and the intermediate quantity passed between each.

9. State the FE Other Disciplines specification page range and explain why there is no dedicated Other Disciplines Handbook section.

10. Give one fast check that would cause you to reject an otherwise algebraically consistent FE answer.


---

## Practice Problem Solutions

1. Use §93.1. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

2. Use §93.2. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

3. Use §93.3. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

4. Use §93.4. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

5. Use §93.5. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

6. Use §93.6. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

7. Use §93.7. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

8. Example structure: electrical input power → motor efficiency → shaft power → pump/fluid model → operating cost. Every arrow must carry a defined quantity and units.

9. The FE Other Disciplines specification is printed on pp. 498–500. The route has no dedicated discipline chapter in Handbook 10.6, so examinees use the relevant general sections instead.

10. Reject answers with impossible units, efficiencies above 100% where not physically meaningful, negative absolute quantities, violated support/device states, broken conservation, or unsafe/unethical implementation assumptions.

---

## Quick Reference

**Source anchor:** FE Other Disciplines CBT specification, printed pp. 498–500.

- **cross-domain electrical model:** Electrical quantities, power, and safe circuit abstraction
- **circuit synthesis workflow:** Kirchhoff laws, impedance, and AC/DC network solving
- **cross-domain three-phase power:** Electrical power, power factor, and three-phase loads
- **instrumentation signal chain:** Sensors, range, sensitivity, and signal conditioning
- **data acquisition sampling:** Sampling rate, aliasing, filtering, and A/D resolution
- **cross-domain feedback control:** Feedback, block diagrams, and dynamic response
- **engineering interlock logic:** Logic, interlocks, alarms, and fail-safe design

---

## What's Next

**Chapter 03-94: Other Disciplines Safety, Economics, and Cross-Domain Engineering Decisions**

For the Other Disciplines route, keep practicing the same transfer loop: classify the problem, locate the canonical model, use the Handbook deliberately, solve with explicit units, then verify the result across domain boundaries.

— Your Mentor
