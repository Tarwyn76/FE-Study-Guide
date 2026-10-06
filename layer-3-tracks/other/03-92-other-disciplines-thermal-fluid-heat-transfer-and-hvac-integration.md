---
chapter: "03-92"
title: "Other Disciplines Thermal, Fluid, Heat-Transfer, and HVAC Integration"
layer: 3
tier: null
track: other_disciplines
template: integration
ledger_ids: [OTH-3-092-01, OTH-3-092-02, OTH-3-092-03, OTH-3-092-04, OTH-3-092-05, OTH-3-092-06, OTH-3-092-07]
routes: [other_disciplines]
status: drafted
---

# Chapter 03-92: Other Disciplines Thermal, Fluid, Heat-Transfer, and HVAC Integration

> *"The Other Disciplines exam is less about owning one specialty and more about recognizing which engineering model governs the next problem."*

---

## Before You Start

**Prerequisites:** FLUID-2D-041-01 · THERMO-2D-047-01 · HT-2D-055-01 · MEC-3-080-01 · MEC-3-081-01 · MEC-3-082-01 · MEC-3-083-01

**Route:** FE Other Disciplines. This is a Layer 3 integration chapter.

**Ownership rule:** This chapter intentionally does **not** create new owners for statics, dynamics, materials, fluids, thermodynamics, electrical engineering, safety, economics, or other already-registered topics. Its concept atoms own only integration, transfer, and exam-strategy skills.

**Time:** About 75–100 min reading and worked examples · 35–45 min review questions · 55–75 min practice problems.

---

## On the Board Today

This chapter develops **Other Disciplines Thermal, Fluid, Heat-Transfer, and HVAC Integration** as a synthesis layer over prior canonical concepts. The FE Other Disciplines specification spans mathematics, probability/statistics, chemistry, instrumentation/controls, ethics, safety, economics, statics, dynamics, strength of materials, materials, fluid mechanics, basic electrical engineering, and thermodynamics/heat transfer. The track therefore emphasizes selection, transfer, and verification rather than duplicated ownership.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **92.1** Apply **Control-volume mass and energy balance selection** in mixed FE problems.
* **92.2** Apply **Fluid property, Reynolds number, and regime selection** in mixed FE problems.
* **92.3** Apply **Pipe-flow energy, losses, pumps, and system curves** in mixed FE problems.
* **92.4** Apply **Convection linked to external/internal flow** in mixed FE problems.
* **92.5** Apply **Conduction, convection, radiation, and thermal-resistance networks** in mixed FE problems.
* **92.6** Apply **Thermodynamic cycles and component performance** in mixed FE problems.
* **92.7** Apply **Psychrometrics, HVAC, combustion, and integrated thermal checks** in mixed FE problems.

---

## Notation Used Here

Keep the notation of the underlying canonical discipline. When moving between domains, state the intermediate quantity, its units, and which model produced it before using it as the next model's input.

---

## 92.1 Control-volume mass and energy balance selection

Thermal-fluid problems often hinge on choosing closed-system versus control-volume analysis and deciding which energy terms are negligible.

\[\frac{dE_{CV}}{dt}=\dot Q-\dot W+\sum\dot m\left(h+\frac{V^2}{2}+gz\right)_{in}-\sum\dot m\left(h+\frac{V^2}{2}+gz\right)_{out}\]

![FIG-03-92-001: Generic thermal-fluid control volume showing mass flow, heat, shaft work, pressure, elevation, and velocity terms.](../figures/FIG-03-92-001-control-volume-mass-and-energy-balance-selection.png)

### Worked Example 1

**Problem.** A steady insulated nozzle with no shaft work converts enthalpy primarily into kinetic energy.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §92.1.

---

## 92.2 Fluid property, Reynolds number, and regime selection

Before selecting friction, drag, heat-transfer, or pressure-drop relations, identify whether the fluid model and flow regime match the correlation.

\[\mathrm{Re}=\frac{\rho VD}{\mu}\]

![FIG-03-92-002: Temperature-dependent fluid properties feeding Reynolds number and laminar/transitional/turbulent model selection.](../figures/FIG-03-92-002-fluid-property-reynolds-number-and-regime-selection.png)

### Worked Example 2

**Problem.** A viscosity change caused by temperature can move a pipe-flow calculation between laminar and turbulent regimes.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §92.2.

---

## 92.3 Pipe-flow energy, losses, pumps, and system curves

A complete fluid-transport problem links Bernoulli/energy balance, distributed/minor losses, pump head, and flow continuity.

\[\frac{p_1}{\gamma}+z_1+\frac{V_1^2}{2g}+h_p=\frac{p_2}{\gamma}+z_2+\frac{V_2^2}{2g}+h_L\]

![FIG-03-92-003: Reservoir-pump-pipe-valve system with HGL/EGL and pump/system curve intersection.](../figures/FIG-03-92-003-pipe-flow-energy-losses-pumps-and-system-curves.png)

### Worked Example 3

**Problem.** Increasing pump speed can move the operating point because both pump and system behavior determine actual flow.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §92.3.

---

## 92.4 Convection linked to external/internal flow

Convective heat-transfer coefficients are not arbitrary constants; they arise from fluid properties, velocity, geometry, and flow regime.

\[\dot Q=hA(T_s-T_\infty),\qquad \mathrm{Nu}=f(\mathrm{Re},\mathrm{Pr},\text{geometry})\]

![FIG-03-92-004: Fluid-flow regime leading through Re/Pr to Nu, h, and convective heat transfer on a surface.](../figures/FIG-03-92-004-convection-linked-to-external-internal-flow.png)

### Worked Example 4

**Problem.** Increasing air speed over a hot surface usually increases h and heat transfer, but the correct correlation must match geometry and regime.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §92.4.

---

## 92.5 Conduction, convection, radiation, and thermal-resistance networks

Multimode heat-transfer problems can often be organized as thermal resistances when assumptions permit. Radiation may require nonlinear temperature dependence rather than a constant resistance.

\[\dot Q=\frac{\Delta T}{R_{th}},\qquad R_{conv}=\frac1{hA}\]

![FIG-03-92-005: Composite wall/cylinder thermal-resistance network including conduction, convection, and radiation branches.](../figures/FIG-03-92-005-conduction-convection-radiation-and-thermal-resistance-networks.png)

### Worked Example 5

**Problem.** Insulation adds conduction resistance but also changes outer area and convection/radiation conditions.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §92.5.

---

## 92.6 Thermodynamic cycles and component performance

Cycle questions combine component energy balances with state-property diagrams. Know whether the device is a turbine, compressor, pump, throttling valve, heat exchanger, refrigerator, or heat pump.

\[\eta_{th}=\frac{W_{net}}{Q_{in}},\qquad \mathrm{COP_R}=\frac{Q_L}{W_{in}}\]

![FIG-03-92-006: Power-cycle and refrigeration-cycle diagrams with component energy directions and T-s/P-h plots.](../figures/FIG-03-92-006-thermodynamic-cycles-and-component-performance.png)

### Worked Example 6

**Problem.** A throttling valve changes pressure without producing shaft work in the ideal steady model and is approximately isenthalpic.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §92.6.

---

## 92.7 Psychrometrics, HVAC, combustion, and integrated thermal checks

Other Disciplines thermal questions may combine moist-air properties, combustion products, energy balance, and heat transfer. Keep dry-air, water-vapor, fuel, and product bases explicit.

\[\text{state properties}+\text{mass balance}+\text{energy balance}\rightarrow\text{HVAC/combustion result}\]

![FIG-03-92-007: Integrated HVAC/combustion workflow linking psychrometrics, combustion basis, heat loads, and equipment performance.](../figures/FIG-03-92-007-psychrometrics-hvac-combustion-and-integrated-thermal-checks.png)

### Worked Example 7

**Problem.** Mixing two moist-air streams requires both dry-air mass and enthalpy/humidity-ratio balances.

**Solution.** Identify the governing prior concept, apply its model with consistent units, then perform the cross-domain verification described in §92.7.

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
| thermal-fluid control-volume synthesis | Synthesis concept in §92.1; coordinates prior canonical owners without duplicating them. |
| cross-domain flow-regime selection | Synthesis concept in §92.2; coordinates prior canonical owners without duplicating them. |
| integrated pipe-system analysis | Synthesis concept in §92.3; coordinates prior canonical owners without duplicating them. |
| flow-to-convection integration | Synthesis concept in §92.4; coordinates prior canonical owners without duplicating them. |
| thermal resistance network | Synthesis concept in §92.5; coordinates prior canonical owners without duplicating them. |
| thermal cycle integration | Synthesis concept in §92.6; coordinates prior canonical owners without duplicating them. |
| thermal systems synthesis | Synthesis concept in §92.7; coordinates prior canonical owners without duplicating them. |

---

## Review Questions

### Conceptual and Applied

1. Define **thermal-fluid control-volume synthesis** and explain what cross-domain decision or transfer skill it supports.

2. Define **cross-domain flow-regime selection** and explain what cross-domain decision or transfer skill it supports.

3. Define **integrated pipe-system analysis** and explain what cross-domain decision or transfer skill it supports.

4. Define **flow-to-convection integration** and explain what cross-domain decision or transfer skill it supports.

5. Define **thermal resistance network** and explain what cross-domain decision or transfer skill it supports.

6. Define **thermal cycle integration** and explain what cross-domain decision or transfer skill it supports.

7. Define **thermal systems synthesis** and explain what cross-domain decision or transfer skill it supports.

8. What is the most important assumption, boundary, unit, or prior-concept check before applying **thermal-fluid control-volume synthesis**?

9. What is the most important assumption, boundary, unit, or prior-concept check before applying **cross-domain flow-regime selection**?

10. What is the most important assumption, boundary, unit, or prior-concept check before applying **integrated pipe-system analysis**?

11. What is the most important assumption, boundary, unit, or prior-concept check before applying **flow-to-convection integration**?

12. What is the most important assumption, boundary, unit, or prior-concept check before applying **thermal resistance network**?

13. What is the most important assumption, boundary, unit, or prior-concept check before applying **thermal cycle integration**?

14. What is the most important assumption, boundary, unit, or prior-concept check before applying **thermal systems synthesis**?

15. Why should an Other Disciplines problem be classified before searching the Handbook?

16. Why is cross-domain synthesis different from creating a new copy of a previously owned concept?

17. What should you do when two equations look plausible but use different assumptions or variable definitions?

18. Why should every final answer receive a units, sign, magnitude, and physical/ethical feasibility check?

### Multiple Choice

19. Which statement is most accurate for **thermal-fluid control-volume synthesis**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

20. Which statement is most accurate for **cross-domain flow-regime selection**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

21. Which statement is most accurate for **integrated pipe-system analysis**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

22. Which statement is most accurate for **flow-to-convection integration**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

23. Which statement is most accurate for **thermal resistance network**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

24. Which statement is most accurate for **thermal cycle integration**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

25. Which statement is most accurate for **thermal systems synthesis**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

26. Which statement is most accurate for **thermal-fluid control-volume synthesis**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation

27. Which statement is most accurate for **cross-domain flow-regime selection**?
A) It coordinates earlier canonical concepts without duplicating ownership
B) It replaces all discipline-specific prerequisites
C) It eliminates the need to check units and assumptions
D) It is unrelated to Handbook navigation


---

## Answer Key with Explanations

1. **thermal-fluid control-volume synthesis** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

2. **cross-domain flow-regime selection** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

3. **integrated pipe-system analysis** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

4. **flow-to-convection integration** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

5. **thermal resistance network** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

6. **thermal cycle integration** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

7. **thermal systems synthesis** is an integration skill developed in its numbered section. It coordinates prior canonical concepts rather than re-owning the underlying discipline topic.

8. For **thermal-fluid control-volume synthesis**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

9. For **cross-domain flow-regime selection**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

10. For **integrated pipe-system analysis**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

11. For **flow-to-convection integration**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

12. For **thermal resistance network**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

13. For **thermal cycle integration**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

14. For **thermal systems synthesis**, check the controlling domain, system boundary, units, model assumptions, and the prerequisite concept being reused.

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

1. A steady insulated nozzle with no shaft work converts enthalpy primarily into kinetic energy.

2. A viscosity change caused by temperature can move a pipe-flow calculation between laminar and turbulent regimes.

3. Increasing pump speed can move the operating point because both pump and system behavior determine actual flow.

4. Increasing air speed over a hot surface usually increases h and heat transfer, but the correct correlation must match geometry and regime.

5. Insulation adds conduction resistance but also changes outer area and convection/radiation conditions.

6. A throttling valve changes pressure without producing shaft work in the ideal steady model and is approximately isenthalpic.

7. Mixing two moist-air streams requires both dry-air mass and enthalpy/humidity-ratio balances.

8. For a mixed-domain problem, write the sequence of discipline models you would use and the intermediate quantity passed between each.

9. State the FE Other Disciplines specification page range and explain why there is no dedicated Other Disciplines Handbook section.

10. Give one fast check that would cause you to reject an otherwise algebraically consistent FE answer.


---

## Practice Problem Solutions

1. Use §92.1. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

2. Use §92.2. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

3. Use §92.3. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

4. Use §92.4. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

5. Use §92.5. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

6. Use §92.6. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

7. Use §92.7. Identify the canonical prerequisite, solve with that model, and carry only verified intermediate quantities into the next domain.

8. Example structure: electrical input power → motor efficiency → shaft power → pump/fluid model → operating cost. Every arrow must carry a defined quantity and units.

9. The FE Other Disciplines specification is printed on pp. 498–500. The route has no dedicated discipline chapter in Handbook 10.6, so examinees use the relevant general sections instead.

10. Reject answers with impossible units, efficiencies above 100% where not physically meaningful, negative absolute quantities, violated support/device states, broken conservation, or unsafe/unethical implementation assumptions.

---

## Quick Reference

**Source anchor:** FE Other Disciplines CBT specification, printed pp. 498–500.

- **thermal-fluid control-volume synthesis:** Control-volume mass and energy balance selection
- **cross-domain flow-regime selection:** Fluid property, Reynolds number, and regime selection
- **integrated pipe-system analysis:** Pipe-flow energy, losses, pumps, and system curves
- **flow-to-convection integration:** Convection linked to external/internal flow
- **thermal resistance network:** Conduction, convection, radiation, and thermal-resistance networks
- **thermal cycle integration:** Thermodynamic cycles and component performance
- **thermal systems synthesis:** Psychrometrics, HVAC, combustion, and integrated thermal checks

---

## What's Next

**Chapter 03-93: Other Disciplines Electrical, Instrumentation, and Control Integration**

For the Other Disciplines route, keep practicing the same transfer loop: classify the problem, locate the canonical model, use the Handbook deliberately, solve with explicit units, then verify the result across domain boundaries.

— Your Mentor
