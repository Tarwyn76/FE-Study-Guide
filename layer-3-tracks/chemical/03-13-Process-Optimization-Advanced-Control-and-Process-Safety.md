---
chapter: "03-13"
title: "Process Optimization, Advanced Control, and Process Safety"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-013-01, CHE-3-013-02, CHE-3-013-03, CHE-3-013-04, CHE-3-013-05, CHE-3-013-06, CHE-3-013-07]
routes: [chemical]
status: drafted
---

# Chapter 03-13: Process Optimization, Advanced Control, and Process Safety

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 03-12 Process Design and Cost Estimation · 02-70 PID Control · 02-19 Safety Systems · 02-20 Fire/Explosion Hazards · 02-21 Toxicology and Compatibility

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The FE Chemical specification explicitly requires optimization, sustainability, process control strategies/hardware, and process safety methods including HAZOP, LOPA, fault/event trees, relief, inerting, and runaway-reaction concepts. The Handbook's general sections support control and safety fundamentals but do not supply detailed formula sets for every named process-safety method; those portions are guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **13.1** Explain and apply **Process Optimization — Objective Functions and Constraints**.
* **13.2** Explain and apply **Sustainability, Efficiency, and Inherently Safer Design**.
* **13.3** Explain and apply **Feedback, Feedforward, Cascade, and Ratio Control**.
* **13.4** Explain and apply **Process Dynamics and Controller Tuning**.
* **13.5** Explain and apply **Control Valves, DCS/PLC, Alarms, and Interlocks**.
* **13.6** Explain and apply **HAZOP, LOPA, Fault Trees, and Event Trees**.
* **13.7** Explain and apply **Relief, Inerting, Runaway Reactions, and Protection Layers**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 13.1 Process Optimization — Objective Functions and Constraints

A process optimization problem requires an objective such as minimum cost, maximum profit, minimum energy use, or maximum yield, together with physical, safety, quality, and regulatory constraints.

The optimum is not necessarily the unconstrained maximum of one performance metric; constraints define the feasible region.

\[\min/\max\ f(\mathbf x)\quad\text{subject to}\quad g_j(\mathbf x)\le0,\ h_k(\mathbf x)=0\]

![FIG-03-13-001: Contour map of process objective with feasible region bounded by capacity, safety, quality, and environmental constraints.](../figures/FIG-03-13-001-process-optimization-objective-functions-and-constraints.png)

### Worked Example 1

**Problem.** An objective is to minimize energy while product purity must be ≥99%. Classify purity statement.

**Solution.** A constraint.

---

## 13.2 Sustainability, Efficiency, and Inherently Safer Design

The specification explicitly names sustainability, efficiency, green engineering, and inherently safer design. These should be treated as design constraints and objectives, not post-design decorations.

Inherently safer strategies seek to eliminate or reduce hazards by choices such as smaller inventories, less hazardous materials, milder conditions, and simpler process configurations before relying on add-on protection.

\[\text{inherent prevention}\rightarrow\text{passive protection}\rightarrow\text{active protection}\rightarrow\text{procedural controls}\]

![FIG-03-13-002: Process-design hierarchy from hazard elimination/minimization through passive, active, and procedural protection layers.](../figures/FIG-03-13-002-sustainability-efficiency-and-inherently-safer-design.png)

### Worked Example 2

**Problem.** Name one inherently safer strategy.

**Solution.** Minimize inventory, substitute less hazardous material, moderate conditions, or simplify.

---

## 13.3 Feedback, Feedforward, Cascade, and Ratio Control

Feedback responds to measured error after a disturbance affects the controlled variable. Feedforward acts from a measured disturbance before the controlled variable moves. Cascade uses an inner loop to reject secondary disturbances rapidly. Ratio control maintains a proportional relationship between streams.

These strategies are explicitly named in the FE Chemical specification; use the general control-system relationships from Layer 2F as the mathematical foundation.

\[\text{ratio setpoint: }\dot m_2=R\,\dot m_1\]

![FIG-03-13-003: Four small block diagrams comparing feedback, feedforward, cascade, and ratio control in chemical-process examples.](../figures/FIG-03-13-003-feedback-feedforward-cascade-and-ratio-control.png)

### Worked Example 3

**Problem.** A ratio controller maintains B/A=2.5 and A=4 kg/s. Find B setpoint.

**Solution.** 10 kg/s.

---

## 13.4 Process Dynamics and Controller Tuning

First- and second-order process dynamics, time delay, stability, damping, and transfer functions are specification topics and are developed in Layer 2F. Chemical-process control applies those models to temperature, pressure, level, composition, and flow loops.

Tuning must respect actuator limits, process dead time, measurement noise, and safety constraints.

\[G_p(s)\approx \frac{Ke^{-\theta s}}{\tau s+1}\quad\text{for a common first-order-plus-dead-time approximation}\]

![FIG-03-13-004: First-order-plus-dead-time process response with PID controller, control valve, sensor, and actuator saturation.](../figures/FIG-03-13-004-process-dynamics-and-controller-tuning.png)

### Worked Example 4

**Problem.** A process has K=2, τ=5 min, θ=1 min in FOPDT form. Identify gain, time constant, and dead time.

**Solution.** K=2; τ=5 min; θ=1 min.

---

## 13.5 Control Valves, DCS/PLC, Alarms, and Interlocks

The FE Chemical specification explicitly includes sensors, control valves, distributed control systems, programmable logic controllers, alarms, and interlocks.

A regulatory control loop maintains normal operation; an interlock or safety action is intended to force a defined safe response when a hazardous condition is detected. Control and protection functions should not be assumed equivalent.

\[\text{sensor}\rightarrow\text{logic/controller}\rightarrow\text{final element}\]

![FIG-03-13-005: Process transmitter, DCS regulatory loop, PLC/interlock path, alarm, shutdown valve, and independent relief layer.](../figures/FIG-03-13-005-control-valves-dcs-plc-alarms-and-interlocks.png)

### Worked Example 5

**Problem.** What is the difference between a regulatory control loop and a safety interlock?

**Solution.** Control maintains normal operation; an interlock forces a defined protective action on hazardous conditions.

---

## 13.6 HAZOP, LOPA, Fault Trees, and Event Trees

**Specification-required; detailed methodology is guide-developed.** HAZOP systematically asks how process variables can deviate from design intent. LOPA estimates risk reduction from independent protection layers. Fault trees work backward from an undesired top event; event trees work forward from an initiating event through success/failure branches.

These tools organize reasoning about causes, consequences, and safeguards; they do not replace sound process design.

\[\text{risk}\approx\text{initiating-event frequency}\times\text{conditional consequence probability}\]

![FIG-03-13-006: HAZOP deviation table, LOPA protection layers, compact fault tree, and event tree shown as four linked safety-analysis views.](../figures/FIG-03-13-006-hazop-lopa-fault-trees-and-event-trees.png)

### Worked Example 6

**Problem.** Does a fault tree generally reason backward from a top event or forward from an initiator?

**Solution.** Backward from a top event.

---

## 13.7 Relief, Inerting, Runaway Reactions, and Protection Layers

The FE Chemical specification includes over/underpressure protection, relief, redundant control, inerting, runaway reactions, and compatibility. General Handbook safety material provides the hazard foundation; detailed sizing correlations are not supplied for all cases.

A relief device limits pressure but does not prevent the initiating event. Inerting reduces oxidizer concentration. Runaway prevention requires recognizing heat-generation versus heat-removal behavior and ensuring independent protective layers where consequences demand them.

\[\text{safe design}=\text{inherent measures}+\text{control}+\text{interlocks}+\text{relief/containment}+\text{procedures}\]

![FIG-03-13-007: Reactor with normal control, high-high trip, inerting, emergency cooling, relief device, containment, and procedural layers.](../figures/FIG-03-13-007-relief-inerting-runaway-reactions-and-protection-layers.png)

### Worked Example 7

**Problem.** Does a relief valve eliminate the initiating cause of overpressure?

**Solution.** No; it limits pressure/consequence after overpressure develops.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A feedforward controller requires measurement of what?

**Solution.** A disturbance variable before its effect reaches the controlled variable.

### Worked Example 9

**Problem.** What hazard is reduced by inerting?

**Solution.** Oxidation/combustion hazard by lowering oxidizer concentration.

---

## As the Handbook States It

Primary source basis: **FE Chemical specification Areas 14D–E, 15A–C, and 16A–F; general Instrumentation, Measurement, and Control, printed pp. 225–234; general Safety, printed pp. 15–35**.

**Source boundary:** The FE Chemical specification explicitly requires optimization, sustainability, process control strategies/hardware, and process safety methods including HAZOP, LOPA, fault/event trees, relief, inerting, and runaway-reaction concepts. The Handbook's general sections support control and safety fundamentals but do not supply detailed formula sets for every named process-safety method; those portions are guide-developed.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using process optimization problem without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using inherently safer process design without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using process control strategy without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using chemical process dynamics without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using process control and interlock hardware without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using process hazard analysis without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using process safety protection layers without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| process optimization problem | Concept developed in §13.1; apply with the section's stated basis and assumptions. |
| inherently safer process design | Concept developed in §13.2; apply with the section's stated basis and assumptions. |
| process control strategy | Concept developed in §13.3; apply with the section's stated basis and assumptions. |
| chemical process dynamics | Concept developed in §13.4; apply with the section's stated basis and assumptions. |
| process control and interlock hardware | Concept developed in §13.5; apply with the section's stated basis and assumptions. |
| process hazard analysis | Concept developed in §13.6; apply with the section's stated basis and assumptions. |
| process safety protection layers | Concept developed in §13.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **process optimization problem** and state the governing relation or balance.

2. Define **inherently safer process design** and state the governing relation or balance.

3. Define **process control strategy** and state the governing relation or balance.

4. Define **chemical process dynamics** and state the governing relation or balance.

5. Define **process control and interlock hardware** and state the governing relation or balance.

6. Define **process hazard analysis** and state the governing relation or balance.

7. Define **process safety protection layers** and state the governing relation or balance.

8. What is the most likely error if **process optimization problem** is applied before the process basis and boundary are defined?

9. What is the most likely error if **inherently safer process design** is applied before the process basis and boundary are defined?

10. What is the most likely error if **process control strategy** is applied before the process basis and boundary are defined?

11. What is the most likely error if **chemical process dynamics** is applied before the process basis and boundary are defined?

12. What is the most likely error if **process control and interlock hardware** is applied before the process basis and boundary are defined?

13. What is the most likely error if **process hazard analysis** is applied before the process basis and boundary are defined?

14. What is the most likely error if **process safety protection layers** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **process optimization problem**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **inherently safer process design**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **process control strategy**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **chemical process dynamics**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **process control and interlock hardware**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **process hazard analysis**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **process safety protection layers**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **process optimization problem**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **inherently safer process design**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **process optimization problem** is developed in §13.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **inherently safer process design** is developed in §13.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **process control strategy** is developed in §13.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **chemical process dynamics** is developed in §13.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **process control and interlock hardware** is developed in §13.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **process hazard analysis** is developed in §13.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **process safety protection layers** is developed in §13.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

8. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

9. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

10. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

11. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

12. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

13. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

14. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

15. The material balance determines the amounts and compositions needed for enthalpy and reaction-energy calculations.

16. To verify that the unknowns are matched by independent equations/specifications before algebra begins.

17. Whenever the problem provides the model/data; use that stated relation rather than substituting an unstated correlation.

18. The Handbook intentionally omits some theories and formulas; exam specifications can require knowledge not directly tabulated in it.

19. **A.** The relation or workflow for **process optimization problem** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **inherently safer process design** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **process control strategy** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **chemical process dynamics** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **process control and interlock hardware** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **process hazard analysis** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **process safety protection layers** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **process optimization problem** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

27. **A.** The relation or workflow for **inherently safer process design** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. An objective is to minimize energy while product purity must be ≥99%. Classify purity statement.

2. Name one inherently safer strategy.

3. A ratio controller maintains B/A=2.5 and A=4 kg/s. Find B setpoint.

4. A process has K=2, τ=5 min, θ=1 min in FOPDT form. Identify gain, time constant, and dead time.

5. What is the difference between a regulatory control loop and a safety interlock?

6. Does a fault tree generally reason backward from a top event or forward from an initiator?

7. Does a relief valve eliminate the initiating cause of overpressure?

8. A feedforward controller requires measurement of what?

9. What hazard is reduced by inerting?

10. If controller tuning increases speed but causes very low phase margin, what concern rises?


---

## Practice Problem Solutions

1. A constraint.

2. Minimize inventory, substitute less hazardous material, moderate conditions, or simplify.

3. 10 kg/s.

4. K=2; τ=5 min; θ=1 min.

5. Control maintains normal operation; an interlock forces a defined protective action on hazardous conditions.

6. Backward from a top event.

7. No; it limits pressure/consequence after overpressure develops.

8. A disturbance variable before its effect reaches the controlled variable.

9. Oxidation/combustion hazard by lowering oxidizer concentration.

10. Fragility, oscillation, and instability risk.


---

## Quick Reference

**Source anchor:** FE Chemical specification Areas 14D–E, 15A–C, and 16A–F; general Instrumentation, Measurement, and Control, printed pp. 225–234; general Safety, printed pp. 15–35.

- **process optimization problem:** Process Optimization — Objective Functions and Constraints
- **inherently safer process design:** Sustainability, Efficiency, and Inherently Safer Design
- **process control strategy:** Feedback, Feedforward, Cascade, and Ratio Control
- **chemical process dynamics:** Process Dynamics and Controller Tuning
- **process control and interlock hardware:** Control Valves, DCS/PLC, Alarms, and Interlocks
- **process hazard analysis:** HAZOP, LOPA, Fault Trees, and Event Trees
- **process safety protection layers:** Relief, Inerting, Runaway Reactions, and Protection Layers
---

## What's Next

**Chemical track complete — next planned Layer 3 track is Civil Engineering, beginning at 03-14**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor