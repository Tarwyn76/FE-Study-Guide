---
chapter: "02-66"
title: "Measurement Systems, Calibration, Accuracy, and Uncertainty"
layer: 2
tier: F
template: technical
ledger_ids: [INST-2F-066-01, INST-2F-066-02, INST-2F-066-03, INST-2F-066-04, INST-2F-066-05, INST-2F-066-06, INST-2F-066-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-66: Measurement Systems, Calibration, Accuracy, and Uncertainty

> *"Measurement and control fail quietly when the model, calibration, dynamics, or feedback path is assumed instead of checked."*

---

## Before You Start

**Prerequisites:** 01-36 Measurement Uncertainty and Statistical Error Propagation · 02-59 Electrical Quantities

**Skip if:** You can select the correct measurement/control model, use the Handbook relation, solve representative FE-level calculations, and verify calibration, uncertainty, dynamics, sampling, and stability assumptions.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines calibration, transducer sensitivity, measurement accuracy, measurement precision, and measurement uncertainty, and gives the Kline–McClintock uncertainty relation. This chapter integrates those definitions into a measurement-system workflow while preserving Chapter 01-36 as the primary development of uncertainty propagation.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **66.1** Explain and apply **The Measurement Chain and the Measurand**.
* **66.2** Explain and apply **Calibration Against Reference Values**.
* **66.3** Explain and apply **Transducer Sensitivity**.
* **66.4** Explain and apply **Accuracy and Precision**.
* **66.5** Explain and apply **Error, Uncertainty, and Kline–McClintock Propagation**.
* **66.6** Explain and apply **Range, Resolution, Sensitivity, and Uncertainty Are Different**.
* **66.7** Explain and apply **Measurement Planning and Reporting**.

---

## Notation Used Here

Use the variable definitions and sign conventions stated in each section. Frequencies may be given in hertz or radians per second; temperatures in sensor equations must use the scale required by the equation. Control transfer functions use the Laplace variable \(s\).

---

## 66.1 The Measurement Chain and the Measurand

A measurement system begins with a **measurand**—the physical quantity intended to be measured. The Handbook's instrumentation diagram then follows the quantity through a transducer element, signal conditioning, and a useful output such as a display, recorder, or computer.

Each stage can affect the reported result. A correct measurement therefore requires more than selecting a sensor; it requires defining the measurand, the operating range, the environment, and how the electrical output will be interpreted.

\[\text{measurand}\rightarrow\text{transducer}\rightarrow\text{signal conditioning}\rightarrow\text{output}\]

![FIG-02-66-001: Measurement chain from physical measurand through transducer and signal conditioning to recorder/computer/display, with possible uncertainty contributions at each stage.](../figures/FIG-02-66-001-the-measurement-chain-and-the-measurand.png)

### Worked Example 1

**Problem.** A pressure transducer produces 1.0 V at 0 kPa and 5.0 V at 200 kPa. Find sensitivity.

**Solution.** S=(5-1)/(200-0)=0.020 V/kPa.

---

## 66.2 Calibration Against Reference Values

The Handbook defines calibration as comparison of an instrument's output with accepted input reference values, including evaluation of associated uncertainties.

Calibration is not simply 'adjusting the zero.' A calibration may reveal offset, scale-factor error, nonlinearity, or drift. Adjustment may follow calibration, but the comparison and documented relationship between reference input and instrument output are the central measurement tasks.

\[\text{calibration: reference input}\longleftrightarrow\text{instrument indication}\]

![FIG-02-66-002: Reference standard applied across several input values, measured instrument outputs, and a calibration curve with offset and slope error.](../figures/FIG-02-66-002-calibration-against-reference-values.png)

### Worked Example 2

**Problem.** A calibrated reference is 100.00 °C and an instrument reads 100.80 °C. Find signed error measured minus reference.

**Solution.** e=+0.80 °C.

---

## 66.3 Transducer Sensitivity

The Handbook defines transducer sensitivity as the ratio of change in electrical output to change in the physical parameter being measured.

Sensitivity describes slope, not accuracy. A highly sensitive device can still be biased, nonlinear, noisy, or poorly calibrated.

\[S=\frac{\Delta(\text{electrical output})}{\Delta(\text{physical input})}\]

![FIG-02-66-003: Input-output graph showing sensitivity as slope and contrasting high sensitivity with offset error.](../figures/FIG-02-66-003-transducer-sensitivity.png)

### Worked Example 3

**Problem.** Five repeated measurements cluster within 0.02 units but are all 0.5 unit high. Are they precise, accurate, both, or neither?

**Solution.** Precise but inaccurate/biased relative to the reference.

---

## 66.4 Accuracy and Precision

The Handbook defines **accuracy** as closeness of agreement between a measured value and the true quantity value, and **precision** as closeness of agreement among replicate measurements under specified conditions.

A measurement set can be precise but inaccurate if it is tightly clustered around a biased value. It can also be relatively accurate on average while having poor precision.

\[\text{accuracy}\ne\text{precision}\]

![FIG-02-66-004: Four target-style panels distinguishing accurate/precise, accurate/imprecise, precise/biased, and neither.](../figures/FIG-02-66-004-accuracy-and-precision.png)

### Worked Example 4

**Problem.** A result R=xy uses x=10±0.2 and y=5±0.1 with uncorrelated standard uncertainties. Estimate wR.

**Solution.** ∂R/∂x=y=5 and ∂R/∂y=x=10; wR=sqrt[(5·0.2)^2+(10·0.1)^2]=1.414.

---

## 66.5 Error, Uncertainty, and Kline–McClintock Propagation

Chapter 01-36 established the distinction: error is a signed difference from a reference; uncertainty quantifies how well the result is known.

For a calculated result \(R=f(x_1,\ldots,x_n)\) from uncorrelated input uncertainties, the Handbook gives the Kline–McClintock root-sum-square sensitivity relation. This chapter uses that method but does not re-own it.

\[w_R=\sqrt{\sum_i\left(\frac{\partial R}{\partial x_i}w_i\right)^2}\]

![FIG-02-66-005: Measurement chain feeding a calculated result with input uncertainties and sensitivity coefficients combining by RSS.](../figures/FIG-02-66-005-error-uncertainty-and-kline-mcclintock-propagation.png)

### Worked Example 5

**Problem.** An instrument range is 0–100 V with 0.1 V display increments. State the nominal display resolution.

**Solution.** 0.1 V.

---

## 66.6 Range, Resolution, Sensitivity, and Uncertainty Are Different

A measurement system's **range** describes the interval it can accept, **resolution** describes the smallest represented step or increment, **sensitivity** describes output change per input change, and **uncertainty** describes doubt in the reported value.

These quantities are related in design but are not interchangeable. A digital display can show many digits while the underlying uncertainty remains much larger than one displayed count.

\[\text{resolution}\not\equiv\text{accuracy}\not\equiv\text{uncertainty}\]

![FIG-02-66-006: Single instrument specification panel separating range, sensitivity slope, digital resolution, accuracy band, and uncertainty interval.](../figures/FIG-02-66-006-range-resolution-sensitivity-and-uncertainty-are-different.png)

### Worked Example 6

**Problem.** A sensor has twice the sensitivity after a redesign. Does that alone prove twice the accuracy?

**Solution.** No. Sensitivity is slope; accuracy depends on agreement with the reference and other errors.

---

## 66.7 Measurement Planning and Reporting

A defensible measurement report identifies the measurand, instrument and range, calibration basis, sampling or test conditions, result, units, and uncertainty basis.

Before accepting a result, check whether the instrument range was exceeded, whether the sensor perturbed the system, whether calibration conditions match use conditions, and whether the uncertainty is adequate for the engineering decision.

\[\text{define}\rightarrow\text{calibrate}\rightarrow\text{measure}\rightarrow\text{check}\rightarrow\text{report with uncertainty}\]

![FIG-02-66-007: Measurement workflow from measurand definition through calibration, acquisition, validation, uncertainty evaluation, and reporting.](../figures/FIG-02-66-007-measurement-planning-and-reporting.png)

### Worked Example 7

**Problem.** List the minimum elements of a defensible measurement report.

**Solution.** Measurand/result, units, instrument/range, calibration/reference basis, conditions, uncertainty basis, and important assumptions.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A 12-bit converter spans 0–10 V. Estimate one-count resolution.

**Solution.** 10/4096=2.441 mV.

### Worked Example 9

**Problem.** If a result is 25.0±0.4 kPa with expanded uncertainty k=2, what is the associated standard uncertainty if U=ku?

**Solution.** u=0.2 kPa.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Instrumentation, Measurement, and Control, printed pp. 225 and 231; Engineering Probability and Statistics, printed pp. 69–70**.

**Source boundary:** The Handbook directly defines calibration, transducer sensitivity, measurement accuracy, measurement precision, and measurement uncertainty, and gives the Kline–McClintock uncertainty relation. This chapter integrates those definitions into a measurement-system workflow while preserving Chapter 01-36 as the primary development of uncertainty propagation.

---

## Where This Goes Wrong

**Using measurement chain outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using calibration process outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using transducer sensitivity outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using measurement quality outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using measurement uncertainty application outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using measurement resolution distinction outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using measurement reporting workflow outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Confusing a displayed number with a trustworthy measurement.** Resolution, accuracy, precision, calibration, and uncertainty are different properties.

**Ignoring dynamics or stability.** A static calculation cannot establish that a sensor follows a changing signal or that a feedback loop is stable.


---

## Key Terms

| Term | Working definition |
|---|---|
| measurement chain | Concept developed in §66.1; apply with the section's stated model and assumptions. |
| calibration process | Concept developed in §66.2; apply with the section's stated model and assumptions. |
| transducer sensitivity | Concept developed in §66.3; apply with the section's stated model and assumptions. |
| measurement quality | Concept developed in §66.4; apply with the section's stated model and assumptions. |
| measurement uncertainty application | Concept developed in §66.5; apply with the section's stated model and assumptions. |
| measurement resolution distinction | Concept developed in §66.6; apply with the section's stated model and assumptions. |
| measurement reporting workflow | Concept developed in §66.7; apply with the section's stated model and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **measurement chain** and state its governing relation or operational meaning.

2. Define **calibration process** and state its governing relation or operational meaning.

3. Define **transducer sensitivity** and state its governing relation or operational meaning.

4. Define **measurement quality** and state its governing relation or operational meaning.

5. Define **measurement uncertainty application** and state its governing relation or operational meaning.

6. Define **measurement resolution distinction** and state its governing relation or operational meaning.

7. Define **measurement reporting workflow** and state its governing relation or operational meaning.

8. What is a likely engineering error if **measurement chain** is used without checking its assumptions, reference, bandwidth, or calibration basis?

9. What is a likely engineering error if **calibration process** is used without checking its assumptions, reference, bandwidth, or calibration basis?

10. What is a likely engineering error if **transducer sensitivity** is used without checking its assumptions, reference, bandwidth, or calibration basis?

11. What is a likely engineering error if **measurement quality** is used without checking its assumptions, reference, bandwidth, or calibration basis?

12. What is a likely engineering error if **measurement uncertainty application** is used without checking its assumptions, reference, bandwidth, or calibration basis?

13. What is a likely engineering error if **measurement resolution distinction** is used without checking its assumptions, reference, bandwidth, or calibration basis?

14. What is a likely engineering error if **measurement reporting workflow** is used without checking its assumptions, reference, bandwidth, or calibration basis?

15. Why must calibration and uncertainty be distinguished?

16. Why should dynamic response be considered in a measurement or control problem?

17. What independent checks are useful for a measurement/control result?

18. Why should the exact Handbook notation or controller parameterization be checked before substitution?

### Multiple Choice

19. Which statement best describes **measurement chain**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

20. Which statement best describes **calibration process**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

21. Which statement best describes **transducer sensitivity**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

22. Which statement best describes **measurement quality**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

23. Which statement best describes **measurement uncertainty application**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

24. Which statement best describes **measurement resolution distinction**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

25. Which statement best describes **measurement reporting workflow**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

26. Which statement best describes **measurement chain**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

27. Which statement best describes **calibration process**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar


---

## Answer Key with Explanations

1. **measurement chain** is developed in §66.1. Use the displayed relation and the conditions stated there.

2. **calibration process** is developed in §66.2. Use the displayed relation and the conditions stated there.

3. **transducer sensitivity** is developed in §66.3. Use the displayed relation and the conditions stated there.

4. **measurement quality** is developed in §66.4. Use the displayed relation and the conditions stated there.

5. **measurement uncertainty application** is developed in §66.5. Use the displayed relation and the conditions stated there.

6. **measurement resolution distinction** is developed in §66.6. Use the displayed relation and the conditions stated there.

7. **measurement reporting workflow** is developed in §66.7. Use the displayed relation and the conditions stated there.

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

1. A pressure transducer produces 1.0 V at 0 kPa and 5.0 V at 200 kPa. Find sensitivity.

2. A calibrated reference is 100.00 °C and an instrument reads 100.80 °C. Find signed error measured minus reference.

3. Five repeated measurements cluster within 0.02 units but are all 0.5 unit high. Are they precise, accurate, both, or neither?

4. A result R=xy uses x=10±0.2 and y=5±0.1 with uncorrelated standard uncertainties. Estimate wR.

5. An instrument range is 0–100 V with 0.1 V display increments. State the nominal display resolution.

6. A sensor has twice the sensitivity after a redesign. Does that alone prove twice the accuracy?

7. List the minimum elements of a defensible measurement report.

8. A 12-bit converter spans 0–10 V. Estimate one-count resolution.

9. If a result is 25.0±0.4 kPa with expanded uncertainty k=2, what is the associated standard uncertainty if U=ku?

10. Why can extra displayed digits be misleading?


---

## Practice Problem Solutions

1. S=(5-1)/(200-0)=0.020 V/kPa.

2. e=+0.80 °C.

3. Precise but inaccurate/biased relative to the reference.

4. ∂R/∂x=y=5 and ∂R/∂y=x=10; wR=sqrt[(5·0.2)^2+(10·0.1)^2]=1.414.

5. 0.1 V.

6. No. Sensitivity is slope; accuracy depends on agreement with the reference and other errors.

7. Measurand/result, units, instrument/range, calibration/reference basis, conditions, uncertainty basis, and important assumptions.

8. 10/4096=2.441 mV.

9. u=0.2 kPa.

10. Display resolution can be much finer than actual accuracy or measurement uncertainty.


---

## Quick Reference

**Handbook anchor:** Instrumentation, Measurement, and Control, printed pp. 225 and 231; Engineering Probability and Statistics, printed pp. 69–70.

- **measurement chain:** The Measurement Chain and the Measurand
- **calibration process:** Calibration Against Reference Values
- **transducer sensitivity:** Transducer Sensitivity
- **measurement quality:** Accuracy and Precision
- **measurement uncertainty application:** Error, Uncertainty, and Kline–McClintock Propagation
- **measurement resolution distinction:** Range, Resolution, Sensitivity, and Uncertainty Are Different
- **measurement reporting workflow:** Measurement Planning and Reporting
---

## What's Next

**02-67 — Sensors, Transducers, Bridges, and Signal Conditioning**

Carry forward the measurement-and-control workflow: define the measurand and signal path, establish calibration and uncertainty, identify dynamics and sampling limits, then verify feedback stability and hardware constraints.


— Your Mentor