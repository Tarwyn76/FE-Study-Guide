---
chapter: "03-89"
title: "Hydraulic, Pneumatic, and Electromechanical Components"
layer: 3
tier: null
track: mechanical
template: technical
ledger_ids: [MEC-3-089-01, MEC-3-089-02, MEC-3-089-03, MEC-3-089-04, MEC-3-089-05, MEC-3-089-06, MEC-3-089-07]
routes: [mechanical]
status: drafted
---

# Chapter 03-89: Hydraulic, Pneumatic, and Electromechanical Components

> *"Mechanical design is the disciplined conversion of loads, motion, energy, materials, and interfaces into parts that work repeatedly and can actually be made."*

---

## Before You Start

**Prerequisites:** FLUID-2D-041-01 · ELEC-2E-059-01 · CTRL-2F-069-01 · INST-2F-066-01 · SAFE-2B-019-01

**Route:** FE Mechanical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing mechanical model, apply the relevant Handbook relation or learned design workflow, and verify geometry, operating regime, failure mode, and manufacturability.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Mechanical material under **Hydraulic, Pneumatic, and Electromechanical Components**. Shared mechanics, materials, fluids, thermodynamics, heat transfer, circuits, controls, and statistics are reused through prerequisites rather than duplicated. Mechanical-specific design and application are developed here.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **89.1** Explain and apply **Hydraulic force multiplication**.
* **89.2** Explain and apply **Hydraulic power and flow-speed relationships**.
* **89.3** Explain and apply **Directional, pressure, and flow-control valves**.
* **89.4** Explain and apply **Pneumatic actuators and compressibility**.
* **89.5** Explain and apply **Electric motors as mechanical actuators**.
* **89.6** Explain and apply **Solenoids, relays, clutches, and brakes**.
* **89.7** Explain and apply **Integrated fluid-power/electromechanical control and safety**.

---

## Notation Used Here

Define geometry, loads, positive directions, material properties, operating state, and unit system before substitution. Distinguish nominal from local stress, static from fatigue loading, peak from RMS quantities, and ideal component behavior from service limits.

---

## 89.1 Hydraulic force multiplication

Hydraulic systems use pressurized nearly incompressible fluid to transmit force and power. Cylinder force is pressure times effective piston area.

\[F=pA\]

![FIG-03-89-001: Double-acting hydraulic cylinder with pressure ports, piston areas, force, and motion.](../figures/FIG-03-89-001-hydraulic-force-multiplication.png)

### Worked Example 1

**Problem.** 10 MPa acting on 0.001 m² produces 10 kN ideal force.

**Solution.** \(F=pA=(10\ {\rm MPa})(0.001\ {\rm m^2})=(10\times10^6)(0.001)=\mathbf{10{,}000\ N=10\ kN}\) ideal force.

---

## 89.2 Hydraulic power and flow-speed relationships

Hydraulic actuator speed follows flow rate and area; hydraulic power follows pressure and flow. Efficiency connects hydraulic and shaft/electrical power.

\[P_h=pQ,\qquad v=\frac QA\]

![FIG-03-89-002: Pump-valve-cylinder circuit with pressure, flow, actuator velocity, and power arrows.](../figures/FIG-03-89-002-hydraulic-power-and-flow-speed-relationships.png)

### Worked Example 2

**Problem.** 5 MPa at 0.002 m³/s is 10 kW ideal hydraulic power.

**Solution.** \(P_h=pQ=(5\ {\rm MPa})(0.002\ {\rm m^3/s})=(5\times10^6)(0.002)=\mathbf{10{,}000\ W=10\ kW}\). Actual input power is higher when pump/system efficiency is below unity.

---

## 89.3 Directional, pressure, and flow-control valves

Directional valves route flow, pressure-control valves limit/regulate pressure, and flow-control valves influence actuator speed.

\[\text{valve state determines flow path or restriction}\]

![FIG-03-89-003: Hydraulic schematic with pump, reservoir, relief valve, directional valve, flow control, and cylinder.](../figures/FIG-03-89-003-directional-pressure-and-flow-control-valves.png)

### Worked Example 3

**Problem.** A relief valve protects a hydraulic circuit by opening when pressure reaches its setting.

**Solution.** A relief valve is normally closed below its set pressure and opens a flow path when pressure reaches the setting, limiting further pressure rise by diverting flow. It protects against overpressure but does not replace lockout or stored-energy control.

---

## 89.4 Pneumatic actuators and compressibility

Pneumatic systems use compressed gas and are generally more compliant than hydraulic systems. Pressure losses and compressibility affect force and response.

\[F\approx pA\text{, with compressibility affecting dynamics}\]

![FIG-03-89-004: Compressor, receiver, regulator, valve, and pneumatic cylinder with compressibility callout.](../figures/FIG-03-89-004-pneumatic-actuators-and-compressibility.png)

### Worked Example 4

**Problem.** The same nominal pressure-area product can produce different dynamic behavior in pneumatic versus hydraulic actuators.

**Solution.** Both actuator types can have \(F\approx pA\), but compressed gas stores substantial elastic energy and pressure changes with volume. Pneumatic systems therefore tend to have more compliance and different dynamic response than nearly incompressible hydraulic systems.

---

## 89.5 Electric motors as mechanical actuators

Motors convert electrical power to torque and speed. Mechanical design focuses on required torque-speed envelope, duty, gearing, inertia, and thermal limits.

\[P=T\omega\]

![FIG-03-89-005: Motor torque-speed curve with continuous/intermittent regions and mechanical load line.](../figures/FIG-03-89-005-electric-motors-as-mechanical-actuators.png)

### Worked Example 5

**Problem.** A shaft delivering 20 N·m at 100 rad/s transmits 2 kW.

**Solution.** \(P=T\omega=(20\ {\rm N\,m})(100\ {\rm rad/s})=\mathbf{2000\ W=2.0\ kW}\) mechanical shaft power.

---

## 89.6 Solenoids, relays, clutches, and brakes

Electromechanical components convert electrical control into motion or force. Response time, holding force, duty cycle, and fail-safe state are common design concerns.

\[\text{electrical command}\rightarrow\text{magnetic force/torque}\rightarrow\text{mechanical action}\]

![FIG-03-89-006: Solenoid, relay/contactor, electromagnetic clutch, and brake with input/output variables.](../figures/FIG-03-89-006-solenoids-relays-clutches-and-brakes.png)

### Worked Example 6

**Problem.** A spring-return solenoid can provide a defined de-energized position.

**Solution.** A spring-return solenoid uses stored spring force to drive the mechanism to a defined position after de-energization. Whether that de-energized state is actually safe depends on the full machine hazard analysis and any retained fluid/mechanical energy.

---

## 89.7 Integrated fluid-power/electromechanical control and safety

Modern mechanical systems often combine sensors, controllers, electrical drives, valves, and actuators. The system must be checked for power loss behavior, stored energy, feedback failure, and safe state.

\[\text{command}\rightarrow\text{controller}\rightarrow\text{power element}\rightarrow\text{actuator}\rightarrow\text{feedback}\]

![FIG-03-89-007: Integrated sensor-controller-valve/motor-actuator feedback loop with stored-energy and safe-state callouts.](../figures/FIG-03-89-007-integrated-fluid-power-electromechanical-control-and-safety.png)

### Worked Example 7

**Problem.** A hydraulic accumulator can retain hazardous stored energy even after electrical power is removed.

**Solution.** Electrical power removal does not guarantee zero stored energy. Hydraulic accumulators, trapped pneumatic pressure, raised loads, springs, and rotating inertia can remain hazardous; safe design requires isolation, dissipation/blocking, verification, and appropriate control architecture.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation produces a stress or operating point that violates the model assumption used to obtain it. Is the result acceptable?

**Solution.** No. Component equations do not override system state or safety. Pressure, flow, electrical command, actuator behavior, and retained energy must describe the same operating condition before a fluid-power/electromechanical result is accepted.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern the exam solution?

**Solution.** For **Hydraulic, Pneumatic, and Electromechanical Components**, use the FE Reference Handbook expression, symbols, and unit convention whenever it supplies the required model. The external source set **WHITE, ISO4413, ISO4414, IEC60034** supports specification-required learned/application material that is not fully developed in the Handbook. If a remembered textbook formula conflicts with a supplied Handbook relation, the supplied Handbook relation governs unless the problem explicitly defines another model.

---

## As the Handbook States It

Primary source basis: **FE Mechanical specification Area(s) 14; FE Reference Handbook 10.6 Mechanical Engineering and supporting general sections, with the specific subsection/page identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required mechanical-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, examples, model checks, and design context; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- White, F. M., & Xue, H. *Fluid Mechanics* (9th ed.). McGraw Hill. ISBN 978-1-260-25831-8. Supporting scope: External flow, Reynolds number, boundary layers, drag/lift, dimensional analysis, similarity, and turbomachinery scaling.
- ISO. (2010). *Hydraulic fluid power—General rules and safety requirements for systems and their components* (ISO 4413:2010; confirmed current in 2021). Supporting scope: Hydraulic fluid-power design, component/system rules, stored-energy hazards, and safety requirements.
- ISO. (2010). *Pneumatic fluid power—General rules and safety requirements for systems and their components* (ISO 4414:2010; confirmed current in 2021). Supporting scope: Pneumatic fluid-power system/component rules and safety requirements.
- IEC. (2026). *Rotating electrical machines—Part 1: Rating and performance* (IEC 60034-1:2026). Supporting scope: Ratings and performance requirements for rotating electrical machines, including motor components.

The external references support only the learned/application portion of the FE Mechanical specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using hydraulic actuator outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using hydraulic power outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using hydraulic control valve outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using pneumatic actuator outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using electromechanical actuator outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using electromechanical component outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Using actuation system integration outside its assumptions.** Confirm geometry, load path, material behavior, operating state, unit convention, and whether the selected idealization remains valid.

**Checking strength but not function.** A component can avoid yielding and still fail through deflection, resonance, fatigue, wear, leakage, heat, interference, poor fit, or inability to manufacture/assemble.

**Ignoring interfaces.** Bearings, joints, shafts, seals, actuators, piping, and tolerances fail at interfaces as often as within the nominal component body.

---

## Key Terms

| Term | Working definition |
|---|---|
| hydraulic actuator | Concept developed in §89.1; apply with that section's geometry and operating assumptions. |
| hydraulic power | Concept developed in §89.2; apply with that section's geometry and operating assumptions. |
| hydraulic control valve | Concept developed in §89.3; apply with that section's geometry and operating assumptions. |
| pneumatic actuator | Concept developed in §89.4; apply with that section's geometry and operating assumptions. |
| electromechanical actuator | Concept developed in §89.5; apply with that section's geometry and operating assumptions. |
| electromechanical component | Concept developed in §89.6; apply with that section's geometry and operating assumptions. |
| actuation system integration | Concept developed in §89.7; apply with that section's geometry and operating assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **hydraulic actuator** and identify the governing mechanical relation, failure mode, or design decision.

2. Define **hydraulic power** and identify the governing mechanical relation, failure mode, or design decision.

3. Define **hydraulic control valve** and identify the governing mechanical relation, failure mode, or design decision.

4. Define **pneumatic actuator** and identify the governing mechanical relation, failure mode, or design decision.

5. Define **electromechanical actuator** and identify the governing mechanical relation, failure mode, or design decision.

6. Define **electromechanical component** and identify the governing mechanical relation, failure mode, or design decision.

7. Define **actuation system integration** and identify the governing mechanical relation, failure mode, or design decision.

8. What geometric, material, operating, or model assumption must be checked before applying **hydraulic actuator**?

9. What geometric, material, operating, or model assumption must be checked before applying **hydraulic power**?

10. What geometric, material, operating, or model assumption must be checked before applying **hydraulic control valve**?

11. What geometric, material, operating, or model assumption must be checked before applying **pneumatic actuator**?

12. What geometric, material, operating, or model assumption must be checked before applying **electromechanical actuator**?

13. What geometric, material, operating, or model assumption must be checked before applying **electromechanical component**?

14. What geometric, material, operating, or model assumption must be checked before applying **actuation system integration**?

15. Why should a free-body diagram, kinematic sketch, energy balance, or component load path be drawn before selecting an equation?

16. Why is a numerical stress, temperature, speed, or life result insufficient until the assumed failure/operating model is verified?

17. When the FE Reference Handbook supplies a machine-design equation or table, why should its exact definitions and units govern?

18. Why should a limiting-case, dimensional, and manufacturability check be made after calculation?

### Multiple Choice

19. Which statement is most accurate for **hydraulic actuator**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

20. Which statement is most accurate for **hydraulic power**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

21. Which statement is most accurate for **hydraulic control valve**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

22. Which statement is most accurate for **pneumatic actuator**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

23. Which statement is most accurate for **electromechanical actuator**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

24. Which statement is most accurate for **electromechanical component**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

25. Which statement is most accurate for **actuation system integration**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

26. Which statement is most accurate for **hydraulic actuator**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative

27. Which statement is most accurate for **hydraulic power**?
A) It must be applied within its stated geometry, material, loading, and operating assumptions
B) It is independent of boundary conditions
C) It eliminates the need for a failure or feasibility check
D) It is always qualitative


---

## Answer Key with Explanations

1. **hydraulic actuator** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

2. **hydraulic power** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

3. **hydraulic control valve** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

4. **pneumatic actuator** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

5. **electromechanical actuator** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

6. **electromechanical component** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

7. **actuation system integration** is developed in the matching numbered section. Use the displayed relation or design workflow with the stated assumptions.

8. For **hydraulic actuator**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

9. For **hydraulic power**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

10. For **hydraulic control valve**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

11. For **pneumatic actuator**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

12. For **electromechanical actuator**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

13. For **electromechanical component**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

14. For **actuation system integration**, verify geometry, load direction, material model, units, operating regime, and whether the assumed failure or performance mode remains valid.

15. In **Hydraulic, Pneumatic, and Electromechanical Components**, start from the physical model and system/component state, not from an isolated formula. A valid solution must close hydraulic/pneumatic power and flow relations, match valve/actuator states to the command, include motor/mechanical power conversion, and control stored energy during safe shutdown.

16. Units and sign/reference conventions are part of the model in **Hydraulic, Pneumatic, and Electromechanical Components**. Convert all quantities to a consistent basis before substitution and state whether values are absolute/gauge, static/stagnation, nominal/local, input/output, or other relevant basis.

17. The FE Reference Handbook is the controlling exam reference when it supplies the relation for **Hydraulic, Pneumatic, and Electromechanical Components**. External sources **WHITE, ISO4413, ISO4414, IEC60034** support only the learned material not fully developed in the Handbook.

18. Use a limiting or reversal check before accepting the result: set pressure or flow to zero and confirm hydraulic power becomes zero; set shaft torque or angular speed to zero and confirm mechanical motor output power becomes zero. A failure to reduce correctly indicates a geometry, regime, sign, unit, or model-selection error.

19. **A.** Section §89.1, **Hydraulic force multiplication**, uses \(F=pA\). Apply it only under the geometry/material/operating assumptions stated in §89.1, then compare the result with the physical behavior described there.

20. **A.** Section §89.2, **Hydraulic power and flow-speed relationships**, uses \(P_h=pQ,\qquad v=\frac QA\). Apply it only under the geometry/material/operating assumptions stated in §89.2, then compare the result with the physical behavior described there.

21. **A.** Section §89.3, **Directional, pressure, and flow-control valves**, uses \(\text{valve state determines flow path or restriction}\). Apply it only under the geometry/material/operating assumptions stated in §89.3, then compare the result with the physical behavior described there.

22. **A.** Section §89.4, **Pneumatic actuators and compressibility**, uses \(F\approx pA\text{, with compressibility affecting dynamics}\). Apply it only under the geometry/material/operating assumptions stated in §89.4, then compare the result with the physical behavior described there.

23. **A.** Section §89.5, **Electric motors as mechanical actuators**, uses \(P=T\omega\). Apply it only under the geometry/material/operating assumptions stated in §89.5, then compare the result with the physical behavior described there.

24. **A.** Section §89.6, **Solenoids, relays, clutches, and brakes**, uses \(\text{electrical command}\rightarrow\text{magnetic force/torque}\rightarrow\text{mechanical action}\). Apply it only under the geometry/material/operating assumptions stated in §89.6, then compare the result with the physical behavior described there.

25. **A.** Section §89.7, **Integrated fluid-power/electromechanical control and safety**, uses \(\text{command}\rightarrow\text{controller}\rightarrow\text{power element}\rightarrow\text{actuator}\rightarrow\text{feedback}\). Apply it only under the geometry/material/operating assumptions stated in §89.7, then compare the result with the physical behavior described there.

26. **A.** An integrated **Hydraulic, Pneumatic, and Electromechanical Components** result is acceptable only after the governing physical model, geometry, operating/failure regime, units, and independent plausibility checks agree.

27. **A.** Source ownership is explicit in this chapter: FE-Handbook-supported material remains tied to the ledger; externally supported material uses **WHITE, ISO4413, ISO4414, IEC60034**; guide synthesis is supplemental explanation and exam-oriented workflow.


---

## Practice Problems

1. 10 MPa acting on 0.001 m² produces 10 kN ideal force.

2. 5 MPa at 0.002 m³/s is 10 kW ideal hydraulic power.

3. A relief valve protects a hydraulic circuit by opening when pressure reaches its setting.

4. The same nominal pressure-area product can produce different dynamic behavior in pneumatic versus hydraulic actuators.

5. A shaft delivering 20 N·m at 100 rad/s transmits 2 kW.

6. A spring-return solenoid can provide a defined de-energized position.

7. A hydraulic accumulator can retain hazardous stored energy even after electrical power is removed.

8. Identify one geometry, unit, failure-mode, or operating-regime check that must be completed before accepting the result.

9. Identify the FE Mechanical specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or manufacturability check that could reveal a bad mechanical solution.


---

## Practice Problem Solutions

1. **Independent check for §89.1 — Hydraulic force multiplication.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(F=pA=(10\ {\rm MPa})(0.001\ {\rm m^2})=(10\times10^6)(0.001)=\mathbf{10{,}000\ N=10\ kN}\) ideal force.

2. **Independent check for §89.2 — Hydraulic power and flow-speed relationships.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(P_h=pQ=(5\ {\rm MPa})(0.002\ {\rm m^3/s})=(5\times10^6)(0.002)=\mathbf{10{,}000\ W=10\ kW}\). Actual input power is higher when pump/system efficiency is below unity.

3. **Independent check for §89.3 — Directional, pressure, and flow-control valves.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A relief valve is normally closed below its set pressure and opens a flow path when pressure reaches the setting, limiting further pressure rise by diverting flow. It protects against overpressure but does not replace lockout or stored-energy control.

4. **Independent check for §89.4 — Pneumatic actuators and compressibility.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Both actuator types can have \(F\approx pA\), but compressed gas stores substantial elastic energy and pressure changes with volume. Pneumatic systems therefore tend to have more compliance and different dynamic response than nearly incompressible hydraulic systems.

5. **Independent check for §89.5 — Electric motors as mechanical actuators.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. \(P=T\omega=(20\ {\rm N\,m})(100\ {\rm rad/s})=\mathbf{2000\ W=2.0\ kW}\) mechanical shaft power.

6. **Independent check for §89.6 — Solenoids, relays, clutches, and brakes.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. A spring-return solenoid uses stored spring force to drive the mechanism to a defined position after de-energization. Whether that de-energized state is actually safe depends on the full machine hazard analysis and any retained fluid/mechanical energy.

7. **Independent check for §89.7 — Integrated fluid-power/electromechanical control and safety.** Rebuild the result from the stated givens and governing relation rather than copying a memorized answer. Electrical power removal does not guarantee zero stored energy. Hydraulic accumulators, trapped pneumatic pressure, raised loads, springs, and rotating inertia can remain hazardous; safe design requires isolation, dissipation/blocking, verification, and appropriate control architecture.

8. For **Hydraulic, Pneumatic, and Electromechanical Components**, one required acceptance screen is: close hydraulic/pneumatic power and flow relations, match valve/actuator states to the command, include motor/mechanical power conversion, and control stored energy during safe shutdown. A result that violates this screen must be rejected or recomputed with the proper model.

9. Start with the FE Mechanical specification area and FE Reference Handbook location recorded in the ledger for **Hydraulic, Pneumatic, and Electromechanical Components**. For `split_required` concepts, use **WHITE, ISO4413, ISO4414, IEC60034** for the learned/application portion without inventing a Handbook page or clause.

10. Apply this limiting-case test independently: set pressure or flow to zero and confirm hydraulic power becomes zero; set shaft torque or angular speed to zero and confirm mechanical motor output power becomes zero. If the simplified case does not behave as expected, revisit the setup before trusting the full calculation.

---

## Quick Reference

**Source anchor:** FE Mechanical specification Area(s) 14.

- **hydraulic actuator:** Hydraulic force multiplication
- **hydraulic power:** Hydraulic power and flow-speed relationships
- **hydraulic control valve:** Directional, pressure, and flow-control valves
- **pneumatic actuator:** Pneumatic actuators and compressibility
- **electromechanical actuator:** Electric motors as mechanical actuators
- **electromechanical component:** Solenoids, relays, clutches, and brakes
- **actuation system integration:** Integrated fluid-power/electromechanical control and safety

---

## What's Next

**Chapter 03-90: Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability**

Carry forward the same FE workflow: sketch the system and interfaces, identify loads/motion/energy, define material and operating assumptions, apply the Handbook relation or learned model, and verify failure mode, function, and manufacturability.

— Your Mentor
