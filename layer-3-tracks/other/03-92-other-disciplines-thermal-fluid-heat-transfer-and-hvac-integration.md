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

**Solution.** For a steady, adiabatic nozzle with no shaft work and negligible potential-energy change, the steady-flow energy equation reduces to \(h_1+V_1^2/2=h_2+V_2^2/2\). The enthalpy drop therefore appears primarily as increased kinetic energy.

---

## 92.2 Fluid property, Reynolds number, and regime selection

Before selecting friction, drag, heat-transfer, or pressure-drop relations, identify whether the fluid model and flow regime match the correlation.

\[\mathrm{Re}=\frac{\rho VD}{\mu}\]

![FIG-03-92-002: Temperature-dependent fluid properties feeding Reynolds number and laminar/transitional/turbulent model selection.](../figures/FIG-03-92-002-fluid-property-reynolds-number-and-regime-selection.png)

### Worked Example 2

**Problem.** A viscosity change caused by temperature can move a pipe-flow calculation between laminar and turbulent regimes.

**Solution.** Reynolds number is \(\mathrm{Re}=
ho VD/\mu\). Because viscosity can change strongly with temperature, a temperature change can shift \(\mathrm{Re}\) across the laminar/transition/turbulent boundaries even when pipe diameter and bulk velocity are unchanged.

---

## 92.3 Pipe-flow energy, losses, pumps, and system curves

A complete fluid-transport problem links Bernoulli/energy balance, distributed/minor losses, pump head, and flow continuity.

\[\frac{p_1}{\gamma}+z_1+\frac{V_1^2}{2g}+h_p=\frac{p_2}{\gamma}+z_2+\frac{V_2^2}{2g}+h_L\]

![FIG-03-92-003: Reservoir-pump-pipe-valve system with HGL/EGL and pump/system curve intersection.](../figures/FIG-03-92-003-pipe-flow-energy-losses-pumps-and-system-curves.png)

### Worked Example 3

**Problem.** Increasing pump speed can move the operating point because both pump and system behavior determine actual flow.

**Solution.** The actual operating point is the intersection of the pump curve and the system curve, not a pump property alone. Changing pump speed shifts the pump curve through the affinity laws; the resulting flow must then be found where the shifted pump head again equals the system head requirement.

---

## 92.4 Convection linked to external/internal flow

Convective heat-transfer coefficients are not arbitrary constants; they arise from fluid properties, velocity, geometry, and flow regime.

\[\dot Q=hA(T_s-T_\infty),\qquad \mathrm{Nu}=f(\mathrm{Re},\mathrm{Pr},\text{geometry})\]

![FIG-03-92-004: Fluid-flow regime leading through Re/Pr to Nu, h, and convective heat transfer on a surface.](../figures/FIG-03-92-004-convection-linked-to-external-internal-flow.png)

### Worked Example 4

**Problem.** Increasing air speed over a hot surface usually increases h and heat transfer, but the correct correlation must match geometry and regime.

**Solution.** For external or internal forced convection, increasing velocity usually raises Reynolds number and often raises the convective coefficient \(h\). The numerical change must come from a Nusselt correlation valid for the actual geometry, entrance/development condition, and flow regime.

---

## 92.5 Conduction, convection, radiation, and thermal-resistance networks

Multimode heat-transfer problems can often be organized as thermal resistances when assumptions permit. Radiation may require nonlinear temperature dependence rather than a constant resistance.

\[\dot Q=\frac{\Delta T}{R_{th}},\qquad R_{conv}=\frac1{hA}\]

![FIG-03-92-005: Composite wall/cylinder thermal-resistance network including conduction, convection, and radiation branches.](../figures/FIG-03-92-005-conduction-convection-radiation-and-thermal-resistance-networks.png)

### Worked Example 5

**Problem.** Insulation adds conduction resistance but also changes outer area and convection/radiation conditions.

**Solution.** Adding insulation increases conduction resistance, but cylindrical or spherical systems also change outer area and therefore the convection/radiation terms. Build the entire resistance network with the new geometry before concluding how total heat loss changes.

---

## 92.6 Thermodynamic cycles and component performance

Cycle questions combine component energy balances with state-property diagrams. Know whether the device is a turbine, compressor, pump, throttling valve, heat exchanger, refrigerator, or heat pump.

\[\eta_{th}=\frac{W_{net}}{Q_{in}},\qquad \mathrm{COP_R}=\frac{Q_L}{W_{in}}\]

![FIG-03-92-006: Power-cycle and refrigeration-cycle diagrams with component energy directions and T-s/P-h plots.](../figures/FIG-03-92-006-thermodynamic-cycles-and-component-performance.png)

### Worked Example 6

**Problem.** A throttling valve changes pressure without producing shaft work in the ideal steady model and is approximately isenthalpic.

**Solution.** For an ideal steady throttling device with negligible heat transfer, shaft work, and kinetic/potential changes, the energy balance gives \(h_1\approx h_2\). Pressure falls while enthalpy remains approximately constant; temperature need not remain constant.

---

## 92.7 Psychrometrics, HVAC, combustion, and integrated thermal checks

Other Disciplines thermal questions may combine moist-air properties, combustion products, energy balance, and heat transfer. Keep dry-air, water-vapor, fuel, and product bases explicit.

\[\sum \dot m_{da,in}=\sum \dot m_{da,out},\qquad \sum \dot m_{da}\omega_{in}+\dot m_{w,in}=\sum \dot m_{da}\omega_{out}+\dot m_{w,out},\qquad \dot Q-\dot W+\sum \dot m h_{in}-\sum \dot m h_{out}=0\]

![FIG-03-92-007: Integrated HVAC/combustion workflow linking psychrometrics, combustion basis, heat loads, and equipment performance.](../figures/FIG-03-92-007-psychrometrics-hvac-combustion-and-integrated-thermal-checks.png)

### Worked Example 7

**Problem.** Mixing two moist-air streams requires both dry-air mass and enthalpy/humidity-ratio balances.

**Solution.** For adiabatic mixing of two moist-air streams, conserve dry-air mass first, then water vapor and enthalpy on a dry-air basis. The outlet humidity ratio and enthalpy must satisfy both balances and correspond to a physically valid psychrometric state.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A mixed question contains electrical, mechanical, and economic information. Must every datum be used?

**Solution.** No. Thermal-fluid synthesis is staged. Use the quantities needed to establish state, mass flow, energy transfer, pressure loss, or heat-transfer coefficient; discard unrelated electrical/economic data until a later stage actually requires the resulting heat rate, shaft power, or flow.

### Worked Example 9

**Problem.** You find a familiar equation in memory but a different-looking form in the FE Reference Handbook. What should you do?

**Solution.** Prefer the Handbook relation for the identified fluid, thermodynamic, heat-transfer, or psychrometric regime. Similar-looking correlations can embed different characteristic lengths, property temperatures, or reference states, so reconcile definitions before substituting.

---

## As the Handbook States It

**Primary source basis:** FE Other Disciplines CBT specification, printed pp. 498–500. Unlike the six discipline-specific FE routes, Other Disciplines has no dedicated discipline section in Handbook 10.6; it relies on the general Handbook sections across the book.

**Source boundary:** **FE-Handbook-supported** material consists of the underlying equations, tables, definitions, and discipline models located in the FE Reference Handbook and recorded in the ledger. **Externally supported** material covers Other Disciplines specification knowledge, application context, standards, and integration details that are not fully developed in the Handbook. **Guide synthesis** is the cross-domain classification, transfer, verification, and exam-strategy workflow created for this supplemental guide; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- White, F. M., & Xue, H. *Fluid Mechanics* (9th ed.). McGraw Hill. ISBN 978-1-260-25831-8. Supporting scope: Fluid properties, Reynolds number, internal/external flow, losses, dimensional analysis, and convection-relevant flow behavior.
- ASHRAE. (2025). *2025 ASHRAE Handbook—Fundamentals*, SI edition. ISBN 978-1-964173-11-5. Supporting scope: Psychrometrics, thermodynamics, fluid flow, heat transfer, controls, loads, and HVAC&R fundamentals.
- Turns, S. R., & Haworth, D. C. (2021). *An Introduction to Combustion: Concepts and Applications* (4th ed.). McGraw Hill. ISBN 978-1-260-47769-6. Supporting scope: Combustion stoichiometry, theoretical/excess air, products, heating values, flame temperature, and emissions.

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

15. Thermal-fluid classification identifies whether the problem is a control volume, internal/external flow, heat-transfer resistance, cycle component, psychrometric process, or combustion balance. That decision sharply narrows the relevant Handbook equations and property data.

16. Mass conservation, energy conservation, Reynolds-number relations, convection correlations, and cycle equations remain owned by their earlier technical chapters. The synthesis layer teaches how outputs such as mass flow, \(h\), or shaft work become inputs to the next thermal-fluid stage.

17. Check reference state, steady/transient assumption, compressibility, flow regime, geometry, property basis, and whether the equation uses total/static or dry-air/wet-air quantities. The correct relation is the one whose regime matches the actual process.

18. A final thermal-fluid result should satisfy conservation, dimensional consistency, feasible temperature/pressure/state limits, and efficiency/COP direction. Those checks catch impossible negative absolute states, wrong property bases, and correlations used outside their regimes.

19. **A.** A control-volume thermal problem begins with mass and energy balances and the correct steady/transient terms. Kinetic, potential, shaft-work, and heat-transfer terms are kept or neglected only after the device model justifies it.

20. **A.** Reynolds number links velocity, length, density, and viscosity to regime selection. Because correlations and friction factors depend on regime, property evaluation and characteristic length must be established before using downstream formulas.

21. **A.** Pipe-system flow is set by the simultaneous pump and system behavior. Bernoulli/mechanical-energy terms, head losses, static lift, and pump head must share one datum and sign convention before an operating point is meaningful.

22. **A.** Convection requires both a flow model and a heat-transfer correlation. Reynolds/Prandtl behavior, geometry, boundary condition, and development length determine which Nusselt relation can be used to obtain \(h\).

23. **A.** Thermal-resistance networks convert conduction and convection paths into a common heat-rate model. Series/parallel construction must follow the real heat-flow path, including area changes and radiation when it is significant.

24. **A.** Cycle performance is determined by component states and energy transfers. Turbine, compressor, pump, condenser, boiler, or refrigeration relations must use the correct input/output enthalpies and efficiency definitions for that component.

25. **A.** HVAC/combustion synthesis keeps dry-air, water-vapor, fuel, oxidizer, and product bases explicit. Moist-air and combustion balances must close mass and energy simultaneously before equipment performance can be evaluated.

26. **A.** In a thermal-fluid control-volume problem, write the complete balance before deleting terms. Only then justify steady state, adiabatic behavior, negligible kinetic/potential energy, or zero shaft work from the device description.

27. **A.** Flow-regime selection is upstream of friction and convection correlations. Evaluate properties on the specified basis, calculate the relevant dimensionless groups, and only then choose the correlation whose geometry and regime match.


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

1. Apply the §92.1 model independently. A control-volume thermal problem begins with mass and energy balances and the correct steady/transient terms. Kinetic, potential, shaft-work, and heat-transfer terms are kept or neglected only after the device model justifies it. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

2. Apply the §92.2 model independently. Reynolds number links velocity, length, density, and viscosity to regime selection. Because correlations and friction factors depend on regime, property evaluation and characteristic length must be established before using downstream formulas. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

3. Apply the §92.3 model independently. Pipe-system flow is set by the simultaneous pump and system behavior. Bernoulli/mechanical-energy terms, head losses, static lift, and pump head must share one datum and sign convention before an operating point is meaningful. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

4. Apply the §92.4 model independently. Convection requires both a flow model and a heat-transfer correlation. Reynolds/Prandtl behavior, geometry, boundary condition, and development length determine which Nusselt relation can be used to obtain \(h\). Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

5. Apply the §92.5 model independently. Thermal-resistance networks convert conduction and convection paths into a common heat-rate model. Series/parallel construction must follow the real heat-flow path, including area changes and radiation when it is significant. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

6. Apply the §92.6 model independently. Cycle performance is determined by component states and energy transfers. Turbine, compressor, pump, condenser, boiler, or refrigeration relations must use the correct input/output enthalpies and efficiency definitions for that component. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

7. Apply the §92.7 model independently. HVAC/combustion synthesis keeps dry-air, water-vapor, fuel, oxidizer, and product bases explicit. Moist-air and combustion balances must close mass and energy simultaneously before equipment performance can be evaluated. Use the stated example as a qualitative/numerical check, but rebuild the reasoning from the governing relation.

8. A typical chain is thermodynamic state/control volume → mass/energy rate → pipe or fan/pump operating point → heat-transfer coefficient/load → HVAC or combustion equipment result. Carry each \( \dot m, h, Q, \dot Q,\) or \(W\) value on one declared basis.

9. The Other Disciplines scope is on printed pp. 498–500 of the specification, while the equations come from the Handbook's general thermodynamics, fluid mechanics, heat-transfer, and related sections rather than a dedicated Other Disciplines chapter.

10. Reject a result that violates a physical state or conservation bound—for example negative absolute temperature, efficiency above unity for a heat engine, or an outlet mass/energy balance that does not close.

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
