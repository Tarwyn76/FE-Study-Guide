---
chapter: "02-69"
title: "Transfer Functions and Feedback Control Fundamentals"
layer: 2
tier: F
template: technical
ledger_ids: [CTRL-2F-069-01, CTRL-2F-069-02, CTRL-2F-069-03, CTRL-2F-069-04, CTRL-2F-069-05, CTRL-2F-069-06, CTRL-2F-069-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-69: Transfer Functions and Feedback Control Fundamentals

> *"Measurement and control fail quietly when the model, calibration, dynamics, or feedback path is assumed instead of checked."*

---

## Before You Start

**Prerequisites:** 02-68 Dynamic and Frequency Response · 01-25 Differential Equations

**Skip if:** You can select the correct measurement/control model, use the Handbook relation, solve representative FE-level calculations, and verify calibration, uncertainty, dynamics, sampling, and stability assumptions.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines the linear time-invariant transfer-function form, poles and zeros, a classical negative-feedback block diagram, open-loop transfer function, closed-loop characteristic equation, steady-state/DC-gain analysis, system-type error behavior, gain/phase margins, and first-/second-order models.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **69.1** Explain and apply **Transfer Functions, Poles, and Zeros**.
* **69.2** Explain and apply **Block Diagrams, Summing Junctions, and Signal Flow**.
* **69.3** Explain and apply **Open-Loop and Closed-Loop Transfer Functions**.
* **69.4** Explain and apply **Disturbance Response and Feedback Rejection**.
* **69.5** Explain and apply **Characteristic Equation and Pole Stability**.
* **69.6** Explain and apply **Steady-State Gain and Error**.
* **69.7** Explain and apply **Frequency Response, Gain Margin, and Phase Margin**.

---

## Notation Used Here

Use the variable definitions and sign conventions stated in each section. Frequencies may be given in hertz or radians per second; temperatures in sensor equations must use the scale required by the equation. Control transfer functions use the Laplace variable \(s\).

---

## 69.1 Transfer Functions, Poles, and Zeros

For a linear time-invariant model with zero initial conditions, the transfer function is the ratio of output transform to input transform and can be written as numerator polynomial over denominator polynomial.

Zeros are roots of the numerator; poles are roots of the denominator. Pole locations strongly govern natural dynamics and stability.

\[G(s)=\frac{Y(s)}{X(s)}=K\frac{\prod_m(s-z_m)}{\prod_n(s-p_n)}\]

![FIG-02-69-001: Transfer-function block with factored numerator/denominator and corresponding poles/zeros plotted in the complex s-plane.](../figures/FIG-02-69-001-transfer-functions-poles-and-zeros.png)

### Worked Example 1

**Problem.** For G(s)=10(s+2)/[(s+1)(s+5)], identify zero and poles.

**Solution.** Zero z=-2; poles p=-1 and -5.

---

## 69.2 Block Diagrams, Summing Junctions, and Signal Flow

A control block diagram represents signal transformations and algebraic summing points. Blocks carry transfer functions; arrows carry signals.

The diagram must preserve sign at each summing junction. A minus sign on the feedback input creates negative feedback.

\[Y(s)=G(s)X(s)\quad\text{for a single block}\]

![FIG-02-69-002: Reference, summing junction, controller, plant, sensor feedback, output, and disturbance signal in a classical loop.](../figures/FIG-02-69-002-block-diagrams-summing-junctions-and-signal-flow.png)

### Worked Example 2

**Problem.** A block G=4 receives X=3. Find output in the static algebraic analogy.

**Solution.** Y=GX=12.

---

## 69.3 Open-Loop and Closed-Loop Transfer Functions

For the Handbook's classical loop, the product around the feedback path is the open-loop transfer function. Closing the feedback loop changes the reference-to-output transfer by the denominator \(1+L(s)\).

Negative feedback can reduce sensitivity to plant variation and disturbances, but only if the resulting closed loop remains stable.

\[L(s)=G_1(s)G_2(s)H(s),\qquad \frac{Y}{R}=\frac{G_1G_2}{1+G_1G_2H}\]

![FIG-02-69-003: Open-loop product highlighted around a negative-feedback loop and the equivalent closed-loop transfer-function expression.](../figures/FIG-02-69-003-open-loop-and-closed-loop-transfer-functions.png)

### Worked Example 3

**Problem.** For unity feedback G(s)=K/(s+2), write closed-loop reference transfer function.

**Solution.** T(s)=K/(s+2+K).

---

## 69.4 Disturbance Response and Feedback Rejection

A disturbance entering the plant path reaches the output through a different numerator but shares the same closed-loop denominator. Increasing loop gain can reduce certain low-frequency disturbances, but may also reduce stability margin.

The exact disturbance path depends on where the disturbance enters the block diagram.

\[\frac{Y(s)}{L_d(s)}=\frac{G_2(s)}{1+G_1(s)G_2(s)H(s)}\quad\text{for the Handbook diagram}\]

![FIG-02-69-004: Negative-feedback loop with disturbance injected before the plant and separate reference and disturbance transfer paths.](../figures/FIG-02-69-004-disturbance-response-and-feedback-rejection.png)

### Worked Example 4

**Problem.** In the Handbook disturbance configuration, if G1=2, G2=5, H=1, find reference closed-loop gain and disturbance closed-loop gain at a frequency where these are real constants.

**Solution.** Y/R=10/(1+10)=0.909; Y/L=5/(1+10)=0.455.

---

## 69.5 Characteristic Equation and Pole Stability

Closed-loop poles are roots of the characteristic equation. The Handbook gives \(1+G_1G_2H=0\) for the classical negative-feedback loop.

For continuous-time LTI systems, poles in the open left half-plane correspond to decaying natural modes. Poles in the right half-plane produce growing modes.

\[1+L(s)=0\]

![FIG-02-69-005: Complex s-plane with stable left-half-plane poles, marginal imaginary-axis cases, and unstable right-half-plane poles.](../figures/FIG-02-69-005-characteristic-equation-and-pole-stability.png)

### Worked Example 5

**Problem.** For L(s)=K/(s+1), write the characteristic equation.

**Solution.** 1+K/(s+1)=0 → s+1+K=0.

---

## 69.6 Steady-State Gain and Error

The Handbook gives DC gain as \(\lim_{s\to0}G(s)\) when the relevant poles satisfy the stated stability conditions. In unity feedback, system type determines whether step, ramp, and acceleration inputs produce zero, finite, or infinite steady-state error.

This chapter emphasizes recognizing the error class before substituting constants from a table.

\[G(0)=\lim_{s\to0}G(s)\]

![FIG-02-69-006: Unity-feedback system with type 0, 1, and 2 rows showing qualitative step/ramp/acceleration steady-state error behavior.](../figures/FIG-02-69-006-steady-state-gain-and-error.png)

### Worked Example 6

**Problem.** For G(s)=5/(2s+1), find DC gain.

**Solution.** G(0)=5.

---

## 69.7 Frequency Response, Gain Margin, and Phase Margin

The Handbook uses frequency response to assess dynamic performance and relative stability. Gain margin measures additional gain required to reach instability at the \(-180^\circ\) phase crossing; phase margin measures additional phase lag to reach instability at the unity-gain crossing.

Positive margins are generally associated with a stable buffer against modeling and operating variation, but acceptable design values depend on the application.

\[GM_{\rm dB}=-20\log_{10}|G(j\omega_{180})|,\qquad PM=180^\circ+\angle G(j\omega_{0dB})\]

![FIG-02-69-007: Bode magnitude and phase plots with zero-dB crossover, minus-180-degree phase crossing, gain margin, and phase margin.](../figures/FIG-02-69-007-frequency-response-gain-margin-and-phase-margin.png)

### Worked Example 7

**Problem.** At the -180° phase crossing, |G|=0.25. Find gain margin in dB.

**Solution.** GM=-20log10(0.25)=12.04 dB.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** At the 0 dB gain crossover, phase is -135°. Find phase margin.

**Solution.** PM=180-135=45°.

### Worked Example 9

**Problem.** Where must continuous-time closed-loop poles lie for asymptotic stability?

**Solution.** In the open left half of the s-plane.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Instrumentation, Measurement, and Control, printed pp. 231–234**.

**Source boundary:** The Handbook directly defines the linear time-invariant transfer-function form, poles and zeros, a classical negative-feedback block diagram, open-loop transfer function, closed-loop characteristic equation, steady-state/DC-gain analysis, system-type error behavior, gain/phase margins, and first-/second-order models.

---

## Where This Goes Wrong

**Using transfer function outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using control block diagram outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using closed-loop transfer function outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using disturbance rejection outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using closed-loop characteristic equation outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using steady-state control error outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using stability margins outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Confusing a displayed number with a trustworthy measurement.** Resolution, accuracy, precision, calibration, and uncertainty are different properties.

**Ignoring dynamics or stability.** A static calculation cannot establish that a sensor follows a changing signal or that a feedback loop is stable.


---

## Key Terms

| Term | Working definition |
|---|---|
| transfer function | Concept developed in §69.1; apply with the section's stated model and assumptions. |
| control block diagram | Concept developed in §69.2; apply with the section's stated model and assumptions. |
| closed-loop transfer function | Concept developed in §69.3; apply with the section's stated model and assumptions. |
| disturbance rejection | Concept developed in §69.4; apply with the section's stated model and assumptions. |
| closed-loop characteristic equation | Concept developed in §69.5; apply with the section's stated model and assumptions. |
| steady-state control error | Concept developed in §69.6; apply with the section's stated model and assumptions. |
| stability margins | Concept developed in §69.7; apply with the section's stated model and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **transfer function** and state its governing relation or operational meaning.

2. Define **control block diagram** and state its governing relation or operational meaning.

3. Define **closed-loop transfer function** and state its governing relation or operational meaning.

4. Define **disturbance rejection** and state its governing relation or operational meaning.

5. Define **closed-loop characteristic equation** and state its governing relation or operational meaning.

6. Define **steady-state control error** and state its governing relation or operational meaning.

7. Define **stability margins** and state its governing relation or operational meaning.

8. What is a likely engineering error if **transfer function** is used without checking its assumptions, reference, bandwidth, or calibration basis?

9. What is a likely engineering error if **control block diagram** is used without checking its assumptions, reference, bandwidth, or calibration basis?

10. What is a likely engineering error if **closed-loop transfer function** is used without checking its assumptions, reference, bandwidth, or calibration basis?

11. What is a likely engineering error if **disturbance rejection** is used without checking its assumptions, reference, bandwidth, or calibration basis?

12. What is a likely engineering error if **closed-loop characteristic equation** is used without checking its assumptions, reference, bandwidth, or calibration basis?

13. What is a likely engineering error if **steady-state control error** is used without checking its assumptions, reference, bandwidth, or calibration basis?

14. What is a likely engineering error if **stability margins** is used without checking its assumptions, reference, bandwidth, or calibration basis?

15. Why must calibration and uncertainty be distinguished?

16. Why should dynamic response be considered in a measurement or control problem?

17. What independent checks are useful for a measurement/control result?

18. Why should the exact Handbook notation or controller parameterization be checked before substitution?

### Multiple Choice

19. Which statement best describes **transfer function**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

20. Which statement best describes **control block diagram**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

21. Which statement best describes **closed-loop transfer function**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

22. Which statement best describes **disturbance rejection**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

23. Which statement best describes **closed-loop characteristic equation**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

24. Which statement best describes **steady-state control error**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

25. Which statement best describes **stability margins**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

26. Which statement best describes **transfer function**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

27. Which statement best describes **control block diagram**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar


---

## Answer Key with Explanations

1. **transfer function** is developed in §69.1. Use the displayed relation and the conditions stated there.

2. **control block diagram** is developed in §69.2. Use the displayed relation and the conditions stated there.

3. **closed-loop transfer function** is developed in §69.3. Use the displayed relation and the conditions stated there.

4. **disturbance rejection** is developed in §69.4. Use the displayed relation and the conditions stated there.

5. **closed-loop characteristic equation** is developed in §69.5. Use the displayed relation and the conditions stated there.

6. **steady-state control error** is developed in §69.6. Use the displayed relation and the conditions stated there.

7. **stability margins** is developed in §69.7. Use the displayed relation and the conditions stated there.

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

1. For G(s)=10(s+2)/[(s+1)(s+5)], identify zero and poles.

2. A block G=4 receives X=3. Find output in the static algebraic analogy.

3. For unity feedback G(s)=K/(s+2), write closed-loop reference transfer function.

4. In the Handbook disturbance configuration, if G1=2, G2=5, H=1, find reference closed-loop gain and disturbance closed-loop gain at a frequency where these are real constants.

5. For L(s)=K/(s+1), write the characteristic equation.

6. For G(s)=5/(2s+1), find DC gain.

7. At the -180° phase crossing, |G|=0.25. Find gain margin in dB.

8. At the 0 dB gain crossover, phase is -135°. Find phase margin.

9. Where must continuous-time closed-loop poles lie for asymptotic stability?

10. Qualitatively, what steady-state ramp error does a type-0 unity-feedback system have under the Handbook table?


---

## Practice Problem Solutions

1. Zero z=-2; poles p=-1 and -5.

2. Y=GX=12.

3. T(s)=K/(s+2+K).

4. Y/R=10/(1+10)=0.909; Y/L=5/(1+10)=0.455.

5. 1+K/(s+1)=0 → s+1+K=0.

6. G(0)=5.

7. GM=-20log10(0.25)=12.04 dB.

8. PM=180-135=45°.

9. In the open left half of the s-plane.

10. Infinite.


---

## Quick Reference

**Handbook anchor:** Instrumentation, Measurement, and Control, printed pp. 231–234.

- **transfer function:** Transfer Functions, Poles, and Zeros
- **control block diagram:** Block Diagrams, Summing Junctions, and Signal Flow
- **closed-loop transfer function:** Open-Loop and Closed-Loop Transfer Functions
- **disturbance rejection:** Disturbance Response and Feedback Rejection
- **closed-loop characteristic equation:** Characteristic Equation and Pole Stability
- **steady-state control error:** Steady-State Gain and Error
- **stability margins:** Frequency Response, Gain Margin, and Phase Margin
---

## What's Next

**02-70 — PID Control, Stability, and Control-Loop Hardware**

Carry forward the measurement-and-control workflow: define the measurand and signal path, establish calibration and uncertainty, identify dynamics and sampling limits, then verify feedback stability and hardware constraints.


— Your Mentor