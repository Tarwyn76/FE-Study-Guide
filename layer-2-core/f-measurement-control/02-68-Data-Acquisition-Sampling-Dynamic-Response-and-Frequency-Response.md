---
chapter: "02-68"
title: "Data Acquisition, Sampling, Dynamic Response, and Frequency Response"
layer: 2
tier: F
template: technical
ledger_ids: [INST-2F-068-01, INST-2F-068-02, INST-2F-068-03, INST-2F-068-04, INST-2F-068-05, INST-2F-068-06, INST-2F-068-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-68: Data Acquisition, Sampling, Dynamic Response, and Frequency Response

> *"Measurement and control fail quietly when the model, calibration, dynamics, or feedback path is assumed instead of checked."*

---

## Before You Start

**Prerequisites:** 02-67 Sensors and Signal Conditioning · 02-61 First-Order Transients · 01-25 Differential Equations

**Skip if:** You can select the correct measurement/control model, use the Handbook relation, solve representative FE-level calculations, and verify calibration, uncertainty, dynamics, sampling, and stability assumptions.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives sampling-frequency and Nyquist criteria, aliasing, A/D resolution and code conversion, signal-conditioning need, first-order and second-order system models, dead time, damping classifications, overshoot/settling metrics, and frequency-response stability concepts.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **68.1** Explain and apply **Data-Acquisition Chain and Sampling Interval**.
* **68.2** Explain and apply **Nyquist Sampling Criterion**.
* **68.3** Explain and apply **Aliasing and Anti-Alias Filtering**.
* **68.4** Explain and apply **Analog-to-Digital Resolution and Codes**.
* **68.5** Explain and apply **First-Order Dynamic Response and Dead Time**.
* **68.6** Explain and apply **Second-Order Dynamic Response**.
* **68.7** Explain and apply **Frequency Response and Measurement Bandwidth**.

---

## Notation Used Here

Use the variable definitions and sign conventions stated in each section. Frequencies may be given in hertz or radians per second; temperatures in sensor equations must use the scale required by the equation. Control transfer functions use the Laplace variable \(s\).

---

## 68.1 Data-Acquisition Chain and Sampling Interval

A data-acquisition system converts a physical signal into a sequence of digital values. The sample interval \(\Delta t\) determines sample frequency.

The acquisition chain typically contains a sensor, conditioning/filtering, sample-and-hold or equivalent ADC front end, digital conversion, and software/storage.

\[f_s=\frac1{\Delta t}\]

![FIG-02-68-001: Sensor-to-signal-conditioning-to-ADC-to-computer DAQ chain with sample interval and sampling clock.](../figures/FIG-02-68-001-data-acquisition-chain-and-sampling-interval.png)

### Worked Example 1

**Problem.** A DAQ samples every 0.002 s. Find sampling frequency.

**Solution.** fs=1/0.002=500 Hz.

---

## 68.2 Nyquist Sampling Criterion

The Handbook states that the sampling rate must exceed twice the highest frequency contained in the measured signal for accurate reconstruction under the sampling-theorem assumptions.

The Handbook labels that highest signal frequency \(f_N\) in this relation. In broader signal-processing usage, 'Nyquist frequency' often means \(f_s/2\); use the Handbook's notation when solving from its formula.

\[f_s>2f_N\]

![FIG-02-68-002: Continuous sinusoid with dense sampling above Nyquist criterion and sample points reconstructing the waveform.](../figures/FIG-02-68-002-nyquist-sampling-criterion.png)

### Worked Example 2

**Problem.** The highest signal frequency is 180 Hz. What minimum sampling rate satisfies the Handbook strict inequality?

**Solution.** fs must be greater than 360 Hz.

---

## 68.3 Aliasing and Anti-Alias Filtering

If the sampling criterion is violated, higher-frequency content can appear as false lower-frequency content in the sampled data. This is aliasing.

Increasing sample rate can help, but practical systems also low-pass filter the analog signal before conversion so frequencies above the intended measurement band do not fold into it.

\[f_{\rm alias}=|f_{\rm signal}-k f_s|\quad\text{for an integer }k\text{ chosen into the observed band}\]

![FIG-02-68-003: High-frequency sinusoid and sparse samples that trace an apparent lower-frequency alias, with pre-ADC low-pass filter shown.](../figures/FIG-02-68-003-aliasing-and-anti-alias-filtering.png)

### Worked Example 3

**Problem.** A 900 Hz tone is sampled at 1000 Hz. Find the first alias in 0–500 Hz.

**Solution.** |900-1·1000|=100 Hz.

---

## 68.4 Analog-to-Digital Resolution and Codes

For an \(n\)-bit ADC over nominal range \([V_L,V_H]\), the Handbook gives voltage resolution as full-scale span divided by \(2^n\). The digital code ranges from \(0\) to \(2^n-1\).

The represented voltage is the low-range value plus code times one voltage-resolution step.

\[\Delta V=\frac{V_H-V_L}{2^n},\qquad V=V_L+N\Delta V\]

![FIG-02-68-004: Analog ramp quantized into n-bit digital codes with LSB resolution and endpoint behavior.](../figures/FIG-02-68-004-analog-to-digital-resolution-and-codes.png)

### Worked Example 4

**Problem.** A 12-bit ADC spans -5 to +5 V. Find resolution.

**Solution.** ΔV=10/4096=2.441 mV/count.

---

## 68.5 First-Order Dynamic Response and Dead Time

The Handbook models a first-order system as gain \(K\) with time constant \(\tau\). A step response approaches its final value exponentially.

A pure time delay \(\theta\) shifts the response in time and appears as \(e^{-\theta s}\) in the transfer function.

\[G(s)=\frac{K}{\tau s+1},\qquad y(t)=y_0e^{-t/\tau}+KM(1-e^{-t/\tau})\]

![FIG-02-68-005: First-order step response with gain, time constant, 63.2% point, and a second curve including dead time.](../figures/FIG-02-68-005-first-order-dynamic-response-and-dead-time.png)

### Worked Example 5

**Problem.** For the ADC in Problem 4, code N=3000. Estimate represented voltage using V=VL+NΔV.

**Solution.** V=-5+3000(10/4096)=2.324 V.

---

## 68.6 Second-Order Dynamic Response

The Handbook's standard second-order model uses steady-state gain \(K\), damping ratio \(\zeta\), and natural frequency \(\omega_n\). Underdamped systems have \(\zeta<1\), critically damped systems \(\zeta=1\), and overdamped systems \(\zeta>1\).

For an underdamped system, overshoot and settling time depend strongly on damping.

\[G(s)=\frac{K\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2},\qquad T_s\approx\frac4{\zeta\omega_n}\]

![FIG-02-68-006: Normalized step responses for underdamped, critically damped, and overdamped systems with overshoot and settling time.](../figures/FIG-02-68-006-second-order-dynamic-response.png)

### Worked Example 6

**Problem.** A first-order instrument has K=2, τ=3 s and receives unit step M=1 from zero. Find output at t=3 s.

**Solution.** y=2(1-e^-1)=1.264.

---

## 68.7 Frequency Response and Measurement Bandwidth

Frequency response evaluates a system by applying sinusoidal behavior across frequency and tracking gain and phase. A measurement system should have adequate bandwidth so its magnitude and phase behavior do not distort the frequencies needed for the engineering decision.

Bode magnitude and phase plots provide a compact representation. Instrument bandwidth should be selected together with sample rate and anti-alias filtering.

\[G(j\omega)=|G(j\omega)|\angle\phi(\omega)\]

![FIG-02-68-007: Measurement-system Bode magnitude and phase plots with usable bandwidth, cutoff region, sample-rate relation, and anti-alias filter.](../figures/FIG-02-68-007-frequency-response-and-measurement-bandwidth.png)

### Worked Example 7

**Problem.** A second-order system has ζ=0.5 and ωn=8 rad/s. Estimate 2% settling time.

**Solution.** Ts≈4/(ζωn)=1.0 s.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A first-order sensor has τ=0.20 s. What fraction of final response is reached after one τ from zero?

**Solution.** 1-e^-1=0.632 or 63.2%.

### Worked Example 9

**Problem.** A first-order sensor with K=1, τ=1 s has dead time θ=2 s. What is output to a unit step at t=1 s?

**Solution.** Zero change from the delayed response; the dynamic response has not started.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Instrumentation, Measurement, and Control, printed pp. 230–234**.

**Source boundary:** The Handbook directly gives sampling-frequency and Nyquist criteria, aliasing, A/D resolution and code conversion, signal-conditioning need, first-order and second-order system models, dead time, damping classifications, overshoot/settling metrics, and frequency-response stability concepts.

---

## Where This Goes Wrong

**Using data acquisition system outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using Nyquist sampling criterion outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using aliasing outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using ADC resolution outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using first-order measurement dynamics outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using second-order dynamic response outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using measurement frequency response outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Confusing a displayed number with a trustworthy measurement.** Resolution, accuracy, precision, calibration, and uncertainty are different properties.

**Ignoring dynamics or stability.** A static calculation cannot establish that a sensor follows a changing signal or that a feedback loop is stable.


---

## Key Terms

| Term | Working definition |
|---|---|
| data acquisition system | Concept developed in §68.1; apply with the section's stated model and assumptions. |
| Nyquist sampling criterion | Concept developed in §68.2; apply with the section's stated model and assumptions. |
| aliasing | Concept developed in §68.3; apply with the section's stated model and assumptions. |
| ADC resolution | Concept developed in §68.4; apply with the section's stated model and assumptions. |
| first-order measurement dynamics | Concept developed in §68.5; apply with the section's stated model and assumptions. |
| second-order dynamic response | Concept developed in §68.6; apply with the section's stated model and assumptions. |
| measurement frequency response | Concept developed in §68.7; apply with the section's stated model and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **data acquisition system** and state its governing relation or operational meaning.

2. Define **Nyquist sampling criterion** and state its governing relation or operational meaning.

3. Define **aliasing** and state its governing relation or operational meaning.

4. Define **ADC resolution** and state its governing relation or operational meaning.

5. Define **first-order measurement dynamics** and state its governing relation or operational meaning.

6. Define **second-order dynamic response** and state its governing relation or operational meaning.

7. Define **measurement frequency response** and state its governing relation or operational meaning.

8. What is a likely engineering error if **data acquisition system** is used without checking its assumptions, reference, bandwidth, or calibration basis?

9. What is a likely engineering error if **Nyquist sampling criterion** is used without checking its assumptions, reference, bandwidth, or calibration basis?

10. What is a likely engineering error if **aliasing** is used without checking its assumptions, reference, bandwidth, or calibration basis?

11. What is a likely engineering error if **ADC resolution** is used without checking its assumptions, reference, bandwidth, or calibration basis?

12. What is a likely engineering error if **first-order measurement dynamics** is used without checking its assumptions, reference, bandwidth, or calibration basis?

13. What is a likely engineering error if **second-order dynamic response** is used without checking its assumptions, reference, bandwidth, or calibration basis?

14. What is a likely engineering error if **measurement frequency response** is used without checking its assumptions, reference, bandwidth, or calibration basis?

15. Why must calibration and uncertainty be distinguished?

16. Why should dynamic response be considered in a measurement or control problem?

17. What independent checks are useful for a measurement/control result?

18. Why should the exact Handbook notation or controller parameterization be checked before substitution?

### Multiple Choice

19. Which statement best describes **data acquisition system**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

20. Which statement best describes **Nyquist sampling criterion**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

21. Which statement best describes **aliasing**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

22. Which statement best describes **ADC resolution**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

23. Which statement best describes **first-order measurement dynamics**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

24. Which statement best describes **second-order dynamic response**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

25. Which statement best describes **measurement frequency response**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

26. Which statement best describes **data acquisition system**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

27. Which statement best describes **Nyquist sampling criterion**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar


---

## Answer Key with Explanations

1. **data acquisition system** is developed in §68.1. Use the displayed relation and the conditions stated there.

2. **Nyquist sampling criterion** is developed in §68.2. Use the displayed relation and the conditions stated there.

3. **aliasing** is developed in §68.3. Use the displayed relation and the conditions stated there.

4. **ADC resolution** is developed in §68.4. Use the displayed relation and the conditions stated there.

5. **first-order measurement dynamics** is developed in §68.5. Use the displayed relation and the conditions stated there.

6. **second-order dynamic response** is developed in §68.6. Use the displayed relation and the conditions stated there.

7. **measurement frequency response** is developed in §68.7. Use the displayed relation and the conditions stated there.

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

1. A DAQ samples every 0.002 s. Find sampling frequency.

2. The highest signal frequency is 180 Hz. What minimum sampling rate satisfies the Handbook strict inequality?

3. A 900 Hz tone is sampled at 1000 Hz. Find the first alias in 0–500 Hz.

4. A 12-bit ADC spans -5 to +5 V. Find resolution.

5. For the ADC in Problem 4, code N=3000. Estimate represented voltage using V=VL+NΔV.

6. A first-order instrument has K=2, τ=3 s and receives unit step M=1 from zero. Find output at t=3 s.

7. A second-order system has ζ=0.5 and ωn=8 rad/s. Estimate 2% settling time.

8. A first-order sensor has τ=0.20 s. What fraction of final response is reached after one τ from zero?

9. A first-order sensor with K=1, τ=1 s has dead time θ=2 s. What is output to a unit step at t=1 s?

10. Why is an anti-alias low-pass filter placed before the ADC?


---

## Practice Problem Solutions

1. fs=1/0.002=500 Hz.

2. fs must be greater than 360 Hz.

3. |900-1·1000|=100 Hz.

4. ΔV=10/4096=2.441 mV/count.

5. V=-5+3000(10/4096)=2.324 V.

6. y=2(1-e^-1)=1.264.

7. Ts≈4/(ζωn)=1.0 s.

8. 1-e^-1=0.632 or 63.2%.

9. Zero change from the delayed response; the dynamic response has not started.

10. Once out-of-band content aliases during sampling, digital processing cannot uniquely recover the original frequency.


---

## Quick Reference

**Handbook anchor:** Instrumentation, Measurement, and Control, printed pp. 230–234.

- **data acquisition system:** Data-Acquisition Chain and Sampling Interval
- **Nyquist sampling criterion:** Nyquist Sampling Criterion
- **aliasing:** Aliasing and Anti-Alias Filtering
- **ADC resolution:** Analog-to-Digital Resolution and Codes
- **first-order measurement dynamics:** First-Order Dynamic Response and Dead Time
- **second-order dynamic response:** Second-Order Dynamic Response
- **measurement frequency response:** Frequency Response and Measurement Bandwidth
---

## What's Next

**02-69 — Transfer Functions and Feedback Control Fundamentals**

Carry forward the measurement-and-control workflow: define the measurand and signal path, establish calibration and uncertainty, identify dynamics and sampling limits, then verify feedback stability and hardware constraints.


— Your Mentor