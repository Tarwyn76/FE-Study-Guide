---
chapter: "02-70"
title: "PID Control, Stability, and Control-Loop Hardware"
layer: 2
tier: F
template: technical
ledger_ids: [CTRL-2F-070-01, CTRL-2F-070-02, CTRL-2F-070-03, CTRL-2F-070-04, CTRL-2F-070-05, CTRL-2F-070-06, CTRL-2F-070-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-70: PID Control, Stability, and Control-Loop Hardware

> *"Measurement and control fail quietly when the model, calibration, dynamics, or feedback path is assumed instead of checked."*

---

## Before You Start

**Prerequisites:** 02-69 Feedback Control Fundamentals · 02-67 Sensors and Signal Conditioning · 02-65 Motors and Electromechanical Conversion

**Skip if:** You can select the correct measurement/control model, use the Handbook relation, solve representative FE-level calculations, and verify calibration, uncertainty, dynamics, sampling, and stability assumptions.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives PID and lead/lag controller forms, gain and phase margins, feedback-system definitions, and first-/second-order response metrics. Controller-action interpretation, tuning tradeoffs, saturation/anti-windup, and loop-hardware integration are guide-developed engineering applications.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **70.1** Explain and apply **Proportional Control**.
* **70.2** Explain and apply **Integral Control**.
* **70.3** Explain and apply **Derivative Control**.
* **70.4** Explain and apply **PID Controller Form and Parameter Mapping**.
* **70.5** Explain and apply **Stability, Damping, and Tuning Tradeoffs**.
* **70.6** Explain and apply **Lead/Lag Compensation and Loop-Shaping Context**.
* **70.7** Explain and apply **Control-Loop Hardware and Practical Limits**.

---

## Notation Used Here

Use the variable definitions and sign conventions stated in each section. Frequencies may be given in hertz or radians per second; temperatures in sensor equations must use the scale required by the equation. Control transfer functions use the Laplace variable \(s\).

---

## 70.1 Proportional Control

Proportional action produces a controller output proportional to the present error. Increasing proportional gain usually increases loop responsiveness and reduces some steady-state error, but excessive gain can create oscillation or instability.

A P-only controller does not automatically eliminate steady-state offset for every plant/input class.

\[u_P(t)=K_Pe(t)\]

![FIG-02-70-001: Closed loop with proportional controller and step responses for low, moderate, and excessive proportional gain.](../figures/FIG-02-70-001-proportional-control.png)

### Worked Example 1

**Problem.** A P controller has Kp=4 and instantaneous error 2 units. Find proportional output contribution.

**Solution.** uP=8 output units.

---

## 70.2 Integral Control

Integral action accumulates error over time. It can remove steady-state offset for many constant-reference problems because persistent error continues to change controller output.

The tradeoff is additional phase lag and the possibility of slow oscillation or overshoot if integral action is too aggressive.

\[u_I(t)=K_I\int_0^t e(\tau)\,d\tau\]

![FIG-02-70-002: Error signal integrated over time with comparison of offset removal and slower/oscillatory response.](../figures/FIG-02-70-002-integral-control.png)

### Worked Example 2

**Problem.** An integral controller has Ki=0.5 output/(unit·s) and constant error 3 units for 4 s starting from zero integral. Find contribution.

**Solution.** uI=Ki·e·t=0.5·3·4=6.

---

## 70.3 Derivative Control

Derivative action responds to the rate of change of error, providing anticipatory damping in an ideal model. Because differentiation amplifies high-frequency measurement noise, practical derivative action is usually filtered.

Derivative action alone does not drive a constant error to zero.

\[u_D(t)=K_D\frac{de(t)}{dt}\]

![FIG-02-70-003: Noisy error signal entering derivative path with unfiltered amplification and filtered practical derivative response.](../figures/FIG-02-70-003-derivative-control.png)

### Worked Example 3

**Problem.** A derivative controller has Kd=2 output·s/unit and error slope -0.5 unit/s. Find contribution.

**Solution.** uD=2(-0.5)=-1.

---

## 70.4 PID Controller Form and Parameter Mapping

The Handbook gives a PID controller transfer function in gain/time-constant form. The parallel form is equivalent after mapping \(K_P=K\), \(K_I=K/T_I\), and \(K_D=KT_D\).

Always determine which parameterization a problem or controller uses before inserting values.

\[G_C(s)=K\left(1+\frac1{T_Is}+T_Ds\right)=K_P+\frac{K_I}{s}+K_Ds\]

![FIG-02-70-004: Parallel P-I-D branches summed into controller output with mapping between gain/time constants and parallel gains.](../figures/FIG-02-70-004-pid-controller-form-and-parameter-mapping.png)

### Worked Example 4

**Problem.** Map K=3, TI=6 s, TD=0.5 s to parallel PID gains.

**Solution.** Kp=3; Ki=K/TI=0.5 s^-1 equivalent gain; Kd=KTD=1.5 s.

---

## 70.5 Stability, Damping, and Tuning Tradeoffs

Controller tuning changes closed-loop poles, damping, bandwidth, overshoot, settling time, and stability margins. Faster is not always better.

Use pole locations, step-response metrics, and gain/phase margins together. A tuning change that reduces rise time but collapses phase margin may make the loop fragile.

\[\text{tuning}\Rightarrow\{\text{poles, }\zeta,\omega_n,GM,PM,\text{error}\}\]

![FIG-02-70-005: Control tuning tradeoff chart linking gain changes to rise time, overshoot, settling, steady-state error, and stability margins.](../figures/FIG-02-70-005-stability-damping-and-tuning-tradeoffs.png)

### Worked Example 5

**Problem.** A second-order closed-loop approximation has ζ=0.4 and ωn=5 rad/s. Estimate 2% settling time.

**Solution.** Ts≈4/(0.4·5)=2.0 s.

---

## 70.6 Lead/Lag Compensation and Loop-Shaping Context

The Handbook gives a lead/lag compensator form \(K(1+sT_1)/(1+sT_2)\). Lead compensation is commonly used to add phase and improve speed/stability margin; lag compensation is commonly used to increase low-frequency gain and improve steady-state accuracy.

The exact effect depends on \(T_1/T_2\) and the existing plant frequency response.

\[G_C(s)=K\frac{1+sT_1}{1+sT_2}\]

![FIG-02-70-006: Lead and lag compensator pole-zero placement with qualitative Bode magnitude/phase effects.](../figures/FIG-02-70-006-lead-lag-compensation-and-loop-shaping-context.png)

### Worked Example 6

**Problem.** A lead/lag compensator is K(1+sT1)/(1+sT2). If T1>T2, which qualitative compensation is commonly intended?

**Solution.** Lead compensation: adds positive phase over a frequency band and can improve speed/phase margin.

---

## 70.7 Control-Loop Hardware and Practical Limits

A real feedback loop contains a reference/setpoint, controller, actuator or final control element, plant/process, sensor/transmitter, signal conditioning, and often a data-acquisition or communications interface.

Practical loops also face actuator saturation, deadband, sensor noise, time delay, quantization, and finite sample rate. Integral windup can occur when the actuator saturates while the integrator continues accumulating error; anti-windup is a guide-developed mitigation strategy. Hardware limitations must be included before claiming a controller design is complete.

\[\text{setpoint}\rightarrow\text{controller}\rightarrow\text{actuator}\rightarrow\text{plant}\rightarrow\text{sensor}\rightarrow\text{feedback}\]

![FIG-02-70-007: Industrial feedback loop with controller, actuator/final control element, process, sensor/transmitter, conditioning/DAQ, saturation and noise callouts.](../figures/FIG-02-70-007-control-loop-hardware-and-practical-limits.png)

### Worked Example 7

**Problem.** Name the primary physical blocks in a practical feedback loop.

**Solution.** Setpoint/reference, controller, actuator/final element, plant/process, sensor/transmitter, conditioning/feedback path.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Why can integral windup occur?

**Solution.** Actuator saturation prevents requested output while the integrator continues accumulating error.

### Worked Example 9

**Problem.** Why is ideal derivative action sensitive to measurement noise?

**Solution.** Differentiation magnifies rapid/high-frequency variations.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Instrumentation, Measurement, and Control, printed pp. 231–234**.

**Source boundary:** The Handbook directly gives PID and lead/lag controller forms, gain and phase margins, feedback-system definitions, and first-/second-order response metrics. Controller-action interpretation, tuning tradeoffs, saturation/anti-windup, and loop-hardware integration are guide-developed engineering applications.

---

## Where This Goes Wrong

**Using proportional control outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using integral control outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using derivative control outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using PID controller outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using PID tuning tradeoff outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using lead-lag compensation outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using control-loop hardware outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Confusing a displayed number with a trustworthy measurement.** Resolution, accuracy, precision, calibration, and uncertainty are different properties.

**Ignoring dynamics or stability.** A static calculation cannot establish that a sensor follows a changing signal or that a feedback loop is stable.


---

## Key Terms

| Term | Working definition |
|---|---|
| proportional control | Concept developed in §70.1; apply with the section's stated model and assumptions. |
| integral control | Concept developed in §70.2; apply with the section's stated model and assumptions. |
| derivative control | Concept developed in §70.3; apply with the section's stated model and assumptions. |
| PID controller | Concept developed in §70.4; apply with the section's stated model and assumptions. |
| PID tuning tradeoff | Concept developed in §70.5; apply with the section's stated model and assumptions. |
| lead-lag compensation | Concept developed in §70.6; apply with the section's stated model and assumptions. |
| control-loop hardware | Concept developed in §70.7; apply with the section's stated model and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **proportional control** and state its governing relation or operational meaning.

2. Define **integral control** and state its governing relation or operational meaning.

3. Define **derivative control** and state its governing relation or operational meaning.

4. Define **PID controller** and state its governing relation or operational meaning.

5. Define **PID tuning tradeoff** and state its governing relation or operational meaning.

6. Define **lead-lag compensation** and state its governing relation or operational meaning.

7. Define **control-loop hardware** and state its governing relation or operational meaning.

8. What is a likely engineering error if **proportional control** is used without checking its assumptions, reference, bandwidth, or calibration basis?

9. What is a likely engineering error if **integral control** is used without checking its assumptions, reference, bandwidth, or calibration basis?

10. What is a likely engineering error if **derivative control** is used without checking its assumptions, reference, bandwidth, or calibration basis?

11. What is a likely engineering error if **PID controller** is used without checking its assumptions, reference, bandwidth, or calibration basis?

12. What is a likely engineering error if **PID tuning tradeoff** is used without checking its assumptions, reference, bandwidth, or calibration basis?

13. What is a likely engineering error if **lead-lag compensation** is used without checking its assumptions, reference, bandwidth, or calibration basis?

14. What is a likely engineering error if **control-loop hardware** is used without checking its assumptions, reference, bandwidth, or calibration basis?

15. Why must calibration and uncertainty be distinguished?

16. Why should dynamic response be considered in a measurement or control problem?

17. What independent checks are useful for a measurement/control result?

18. Why should the exact Handbook notation or controller parameterization be checked before substitution?

### Multiple Choice

19. Which statement best describes **proportional control**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

20. Which statement best describes **integral control**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

21. Which statement best describes **derivative control**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

22. Which statement best describes **PID controller**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

23. Which statement best describes **PID tuning tradeoff**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

24. Which statement best describes **lead-lag compensation**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

25. Which statement best describes **control-loop hardware**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

26. Which statement best describes **proportional control**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

27. Which statement best describes **integral control**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar


---

## Answer Key with Explanations

1. **proportional control** is developed in §70.1. Use the displayed relation and the conditions stated there.

2. **integral control** is developed in §70.2. Use the displayed relation and the conditions stated there.

3. **derivative control** is developed in §70.3. Use the displayed relation and the conditions stated there.

4. **PID controller** is developed in §70.4. Use the displayed relation and the conditions stated there.

5. **PID tuning tradeoff** is developed in §70.5. Use the displayed relation and the conditions stated there.

6. **lead-lag compensation** is developed in §70.6. Use the displayed relation and the conditions stated there.

7. **control-loop hardware** is developed in §70.7. Use the displayed relation and the conditions stated there.

8. The numerical calculation may be valid algebraically but represent the wrong measurand, dynamic model, signal band, or control configuration. Establish the model and references first.

9. The numerical calculation may be valid algebraically but represent the wrong measurand, dynamic model, signal band, or control configuration. Establish the model and references first.

10. The numerical calculation may be valid algebraically but represent the wrong measurand, dynamic model, signal band, or control configuration. Establish the model and references first.

11. The numerical calculation may be valid algebraically but represent the wrong measurand, dynamic model, signal band, or control configuration. Establish the model and references first.

12. The numerical calculation may be valid algebraically but represent the wrong measurand, dynamic model, signal band, or control configuration. Establish the model and references first.

13. The numerical calculation may be valid algebraically but represent the wrong measurand, dynamic model, signal band, or control configuration. Establish the model and references first.

14. The numerical calculation may be valid algebraically but represent the wrong measurand, dynamic model, signal band, or control configuration. Establish the model and references first.

15. Calibration establishes comparison to reference values; uncertainty quantifies doubt in the reported result. Calibration can reduce bias but does not make uncertainty zero.

16. A sensor or plant may not follow a changing input instantaneously; lag, damping, and bandwidth can change the observed or controlled response.

17. Check units, limiting behavior, signal range, conservation/physical plausibility, pole stability, and whether sampling/bandwidth assumptions are satisfied.

18. Different sources can use different definitions for gain, time constants, signs, and frequency terms; the mapping must be established first.

19. **A.** Measurement and control quantities are meaningful only with their stated reference, dynamic model, signal conditions, and assumptions.

20. **A.** Measurement and control quantities are meaningful only with their stated reference, dynamic model, signal conditions, and assumptions.

21. **A.** Measurement and control quantities are meaningful only with their stated reference, dynamic model, signal conditions, and assumptions.

22. **A.** Measurement and control quantities are meaningful only with their stated reference, dynamic model, signal conditions, and assumptions.

23. **A.** Measurement and control quantities are meaningful only with their stated reference, dynamic model, signal conditions, and assumptions.

24. **A.** Measurement and control quantities are meaningful only with their stated reference, dynamic model, signal conditions, and assumptions.

25. **A.** Measurement and control quantities are meaningful only with their stated reference, dynamic model, signal conditions, and assumptions.

26. **A.** Measurement and control quantities are meaningful only with their stated reference, dynamic model, signal conditions, and assumptions.

27. **A.** Measurement and control quantities are meaningful only with their stated reference, dynamic model, signal conditions, and assumptions.


---

## Practice Problems

1. A P controller has Kp=4 and instantaneous error 2 units. Find proportional output contribution.

2. An integral controller has Ki=0.5 output/(unit·s) and constant error 3 units for 4 s starting from zero integral. Find contribution.

3. A derivative controller has Kd=2 output·s/unit and error slope -0.5 unit/s. Find contribution.

4. Map K=3, TI=6 s, TD=0.5 s to parallel PID gains.

5. A second-order closed-loop approximation has ζ=0.4 and ωn=5 rad/s. Estimate 2% settling time.

6. A lead/lag compensator is K(1+sT1)/(1+sT2). If T1>T2, which qualitative compensation is commonly intended?

7. Name the primary physical blocks in a practical feedback loop.

8. Why can integral windup occur?

9. Why is ideal derivative action sensitive to measurement noise?

10. If a tuning change makes rise time faster but phase margin much smaller, what engineering concern increases?


---

## Practice Problem Solutions

1. uP=8 output units.

2. uI=Ki·e·t=0.5·3·4=6.

3. uD=2(-0.5)=-1.

4. Kp=3; Ki=K/TI=0.5 s^-1 equivalent gain; Kd=KTD=1.5 s.

5. Ts≈4/(0.4·5)=2.0 s.

6. Lead compensation: adds positive phase over a frequency band and can improve speed/phase margin.

7. Setpoint/reference, controller, actuator/final element, plant/process, sensor/transmitter, conditioning/feedback path.

8. Actuator saturation prevents requested output while the integrator continues accumulating error.

9. Differentiation magnifies rapid/high-frequency variations.

10. Reduced robustness and greater risk of oscillation/instability.


---

## Quick Reference

**Handbook anchor:** Instrumentation, Measurement, and Control, printed pp. 231–234.

- **proportional control:** Proportional Control
- **integral control:** Integral Control
- **derivative control:** Derivative Control
- **PID controller:** PID Controller Form and Parameter Mapping
- **PID tuning tradeoff:** Stability, Damping, and Tuning Tradeoffs
- **lead-lag compensation:** Lead/Lag Compensation and Loop-Shaping Context
- **control-loop hardware:** Control-Loop Hardware and Practical Limits
---

## What's Next

**Layer 2 complete — proceed to the Layer 3 chapter map**

Carry forward the measurement-and-control workflow: define the measurand and signal path, establish calibration and uncertainty, identify dynamics and sampling limits, then verify feedback stability and hardware constraints.


— Your Mentor