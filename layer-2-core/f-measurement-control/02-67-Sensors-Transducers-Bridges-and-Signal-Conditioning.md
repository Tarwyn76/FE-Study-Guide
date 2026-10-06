---
chapter: "02-67"
title: "Sensors, Transducers, Bridges, and Signal Conditioning"
layer: 2
tier: F
template: technical
ledger_ids: [INST-2F-067-01, INST-2F-067-02, INST-2F-067-03, INST-2F-067-04, INST-2F-067-05, INST-2F-067-06, INST-2F-067-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-67: Sensors, Transducers, Bridges, and Signal Conditioning

> *"Measurement and control fail quietly when the model, calibration, dynamics, or feedback path is assumed instead of checked."*

---

## Before You Start

**Prerequisites:** 02-66 Measurement Systems and Calibration · 02-59 Resistance and Voltage · 02-60 Resistive Circuit Analysis

**Skip if:** You can select the correct measurement/control model, use the Handbook relation, solve representative FE-level calculations, and verify calibration, uncertainty, dynamics, sampling, and stability assumptions.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly covers RTDs, thermistors, thermocouples, strain gauges, piezoresistive and piezoelectric effects, Wheatstone bridges, pressure sensors, pH sensors, chemical sensors, and signal conditioning. Practical wiring and selection guidance is guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **67.1** Explain and apply **Resistance Temperature Detectors — RTDs**.
* **67.2** Explain and apply **Thermistors**.
* **67.3** Explain and apply **Thermocouples and the Seebeck Effect**.
* **67.4** Explain and apply **Strain Gauges, Piezoresistive, and Piezoelectric Transducers**.
* **67.5** Explain and apply **Wheatstone Bridges**.
* **67.6** Explain and apply **Pressure, pH, and Chemical Sensors**.
* **67.7** Explain and apply **Signal Conditioning**.

---

## Notation Used Here

Use the variable definitions and sign conventions stated in each section. Frequencies may be given in hertz or radians per second; temperatures in sensor equations must use the scale required by the equation. Control transfer functions use the Laplace variable \(s\).

---

## 67.1 Resistance Temperature Detectors — RTDs

An RTD relates temperature to resistance, commonly using platinum. The Handbook gives a linear resistance-temperature relation referenced to \(R_0\) at \(T_0\).

RTDs are resistive sensors, so the measurement circuit must supply excitation and infer resistance without excessive self-heating or lead-resistance error.

\[R_T=R_0\left[1+\alpha(T-T_0)\right]\]

![FIG-02-67-001: Platinum RTD element connected to a resistance-measurement circuit with reference temperature and linear R-T graph.](../figures/FIG-02-67-001-resistance-temperature-detectors-rtds.png)

### Worked Example 1

**Problem.** A Pt100 RTD has R0=100 Ω at 0°C and α=0.00385/°C. Find R at 100°C using the linear Handbook relation.

**Solution.** R=100[1+0.00385(100)]=138.5 Ω.

---

## 67.2 Thermistors

Thermistors are commonly semiconductor temperature sensors with a negative temperature coefficient. The Handbook gives an exponential beta model and the Steinhart–Hart equation for more precise conversion.

Temperature in the exponential and Steinhart–Hart relations is absolute temperature.

\[R=R_0\exp\left[\beta\left(\frac1T-\frac1{T_0}\right)\right]\]

![FIG-02-67-002: NTC thermistor resistance versus absolute temperature with steep nonlinear decrease.](../figures/FIG-02-67-002-thermistors.png)

### Worked Example 2

**Problem.** An NTC thermistor has R0=10 kΩ at T0=298.15 K and β=3950 K. Estimate R at 323.15 K.

**Solution.** R=10000 exp[3950(1/323.15-1/298.15)]≈3.59 kΩ.

---

## 67.3 Thermocouples and the Seebeck Effect

A thermocouple uses two dissimilar conductors and the Seebeck effect to sense a temperature difference between a measurement junction and a reference junction.

The Handbook supplies common J, K, T, and E material combinations and temperature ranges. Because the output depends on temperature difference, reference-junction compensation is part of practical thermocouple measurement.

\[V_{TC}\propto T_{\rm measurement}-T_{\rm reference}\]

![FIG-02-67-003: Two dissimilar-metal junctions showing measurement junction, reference junction, polarity, and millivolt output.](../figures/FIG-02-67-003-thermocouples-and-the-seebeck-effect.png)

### Worked Example 3

**Problem.** A thermocouple sensitivity is approximated as 41 µV/°C and junction difference is 100°C. Estimate output.

**Solution.** 4.1 mV.

---

## 67.4 Strain Gauges, Piezoresistive, and Piezoelectric Transducers

A resistive strain gauge changes resistance with mechanical strain. The Handbook defines gauge factor as fractional resistance change divided by strain.

Piezoresistive materials can have much larger gauge factors than metallic gauges. Piezoelectric materials convert mechanical deformation to electrical charge and are especially useful for dynamic force, pressure, and vibration measurements.

\[GF=\frac{\Delta R/R}{\varepsilon}\]

![FIG-02-67-004: Metallic strain gauge on a loaded member beside piezoresistive and piezoelectric transducer concepts.](../figures/FIG-02-67-004-strain-gauges-piezoresistive-and-piezoelectric-transducers.png)

### Worked Example 4

**Problem.** A metallic strain gauge has GF=2.0 and strain 500 µε. Find ΔR/R.

**Solution.** ΔR/R=GF·ε=2(500×10^-6)=0.001.

---

## 67.5 Wheatstone Bridges

The Wheatstone bridge converts small resistance changes into a measurable differential voltage. It is balanced when the resistor ratios satisfy the Handbook condition and the bridge output is zero.

For one small resistance change in an otherwise equal bridge, the Handbook gives the quarter-bridge approximation \(V_o\approx(\Delta R/4R)V_s\).

\[\frac{R_3}{R_1}=\frac{R_4}{R_2}\Rightarrow V_o=0,\qquad V_o\approx\frac{\Delta R}{4R}V_s\]

![FIG-02-67-005: Four-resistor Wheatstone bridge with excitation and output, balanced condition, and one active strain gauge.](../figures/FIG-02-67-005-wheatstone-bridges.png)

### Worked Example 5

**Problem.** A 350 Ω gauge has ΔR/R=0.001 in a quarter bridge with Vs=5 V. Estimate bridge output.

**Solution.** Vo≈(0.001/4)(5)=1.25 mV.

---

## 67.6 Pressure, pH, and Chemical Sensors

The Handbook classifies pressure measurements as absolute, gauge, and differential, and notes that many pressure transducers infer pressure from membrane strain. It also gives a pH-electrode relation and examples of electrochemical, semiconductor, optical, catalytic, and other chemical sensors.

The governing transduction principle must match the measurand and environment.

\[E_{el}=E_0-S(pH_a-pH_i)\]

![FIG-02-67-006: Pressure diaphragm, pH electrode, and chemical-sensor family tree with absolute/gauge/differential pressure references.](../figures/FIG-02-67-006-pressure-ph-and-chemical-sensors.png)

### Worked Example 6

**Problem.** Classify a pressure reading referenced to atmosphere.

**Solution.** Gauge pressure.

---

## 67.7 Signal Conditioning

The Handbook states that signal conditioning is often required to reduce measurement errors and prevent alias frequencies from being measured. Conditioning can include amplification, attenuation, filtering, isolation, bridge completion, excitation, and conversion.

The conditioner should make the signal compatible with the acquisition system without destroying information in the measurement band.

\[\text{sensor output}\rightarrow\text{condition}\rightarrow\text{ADC/display/controller}\]

![FIG-02-67-007: Low-level sensor output passing through excitation, bridge/amplifier, filter, isolation, and ADC/interface blocks.](../figures/FIG-02-67-007-signal-conditioning.png)

### Worked Example 7

**Problem.** Why is signal conditioning often needed before an ADC?

**Solution.** To amplify/scale/filter/isolate/complete excitation so the signal fits the ADC and high-frequency content does not alias.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A pressure sensor reports 250 kPa absolute when atmosphere is 100 kPa. Find gauge pressure.

**Solution.** 150 kPa.

### Worked Example 9

**Problem.** A pH electrode has E0=0, S=59 mV/pH, pHi=7 and pHa=5. Find Eel from the Handbook form.

**Solution.** Eel=0-59(5-7)=+118 mV.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Instrumentation, Measurement, and Control, printed pp. 225–231**.

**Source boundary:** The Handbook directly covers RTDs, thermistors, thermocouples, strain gauges, piezoresistive and piezoelectric effects, Wheatstone bridges, pressure sensors, pH sensors, chemical sensors, and signal conditioning. Practical wiring and selection guidance is guide-developed.

---

## Where This Goes Wrong

**Using resistance temperature detector outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using thermistor outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using thermocouple outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using strain transducer outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using Wheatstone bridge outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using process sensor selection outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Using signal conditioning outside its measurement or control assumptions.** Check the measurand, calibration basis, signal range, sampling/bandwidth, dynamic model, and feedback configuration before applying the relation.

**Confusing a displayed number with a trustworthy measurement.** Resolution, accuracy, precision, calibration, and uncertainty are different properties.

**Ignoring dynamics or stability.** A static calculation cannot establish that a sensor follows a changing signal or that a feedback loop is stable.


---

## Key Terms

| Term | Working definition |
|---|---|
| resistance temperature detector | Concept developed in §67.1; apply with the section's stated model and assumptions. |
| thermistor | Concept developed in §67.2; apply with the section's stated model and assumptions. |
| thermocouple | Concept developed in §67.3; apply with the section's stated model and assumptions. |
| strain transducer | Concept developed in §67.4; apply with the section's stated model and assumptions. |
| Wheatstone bridge | Concept developed in §67.5; apply with the section's stated model and assumptions. |
| process sensor selection | Concept developed in §67.6; apply with the section's stated model and assumptions. |
| signal conditioning | Concept developed in §67.7; apply with the section's stated model and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **resistance temperature detector** and state its governing relation or operational meaning.

2. Define **thermistor** and state its governing relation or operational meaning.

3. Define **thermocouple** and state its governing relation or operational meaning.

4. Define **strain transducer** and state its governing relation or operational meaning.

5. Define **Wheatstone bridge** and state its governing relation or operational meaning.

6. Define **process sensor selection** and state its governing relation or operational meaning.

7. Define **signal conditioning** and state its governing relation or operational meaning.

8. What is a likely engineering error if **resistance temperature detector** is used without checking its assumptions, reference, bandwidth, or calibration basis?

9. What is a likely engineering error if **thermistor** is used without checking its assumptions, reference, bandwidth, or calibration basis?

10. What is a likely engineering error if **thermocouple** is used without checking its assumptions, reference, bandwidth, or calibration basis?

11. What is a likely engineering error if **strain transducer** is used without checking its assumptions, reference, bandwidth, or calibration basis?

12. What is a likely engineering error if **Wheatstone bridge** is used without checking its assumptions, reference, bandwidth, or calibration basis?

13. What is a likely engineering error if **process sensor selection** is used without checking its assumptions, reference, bandwidth, or calibration basis?

14. What is a likely engineering error if **signal conditioning** is used without checking its assumptions, reference, bandwidth, or calibration basis?

15. Why must calibration and uncertainty be distinguished?

16. Why should dynamic response be considered in a measurement or control problem?

17. What independent checks are useful for a measurement/control result?

18. Why should the exact Handbook notation or controller parameterization be checked before substitution?

### Multiple Choice

19. Which statement best describes **resistance temperature detector**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

20. Which statement best describes **thermistor**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

21. Which statement best describes **thermocouple**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

22. Which statement best describes **strain transducer**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

23. Which statement best describes **Wheatstone bridge**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

24. Which statement best describes **process sensor selection**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

25. Which statement best describes **signal conditioning**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

26. Which statement best describes **resistance temperature detector**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar

27. Which statement best describes **thermistor**?
A) Its meaning depends on a defined measurement/control model and assumptions
B) It is independent of calibration and dynamics
C) It replaces physical validation
D) It is always a static scalar


---

## Answer Key with Explanations

1. **resistance temperature detector** is developed in §67.1. Use the displayed relation and the conditions stated there.

2. **thermistor** is developed in §67.2. Use the displayed relation and the conditions stated there.

3. **thermocouple** is developed in §67.3. Use the displayed relation and the conditions stated there.

4. **strain transducer** is developed in §67.4. Use the displayed relation and the conditions stated there.

5. **Wheatstone bridge** is developed in §67.5. Use the displayed relation and the conditions stated there.

6. **process sensor selection** is developed in §67.6. Use the displayed relation and the conditions stated there.

7. **signal conditioning** is developed in §67.7. Use the displayed relation and the conditions stated there.

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

1. A Pt100 RTD has R0=100 Ω at 0°C and α=0.00385/°C. Find R at 100°C using the linear Handbook relation.

2. An NTC thermistor has R0=10 kΩ at T0=298.15 K and β=3950 K. Estimate R at 323.15 K.

3. A thermocouple sensitivity is approximated as 41 µV/°C and junction difference is 100°C. Estimate output.

4. A metallic strain gauge has GF=2.0 and strain 500 µε. Find ΔR/R.

5. A 350 Ω gauge has ΔR/R=0.001 in a quarter bridge with Vs=5 V. Estimate bridge output.

6. Classify a pressure reading referenced to atmosphere.

7. Why is signal conditioning often needed before an ADC?

8. A pressure sensor reports 250 kPa absolute when atmosphere is 100 kPa. Find gauge pressure.

9. A pH electrode has E0=0, S=59 mV/pH, pHi=7 and pHa=5. Find Eel from the Handbook form.

10. Why is a piezoelectric transducer generally better for dynamic than static force measurement?


---

## Practice Problem Solutions

1. R=100[1+0.00385(100)]=138.5 Ω.

2. R=10000 exp[3950(1/323.15-1/298.15)]≈3.59 kΩ.

3. 4.1 mV.

4. ΔR/R=GF·ε=2(500×10^-6)=0.001.

5. Vo≈(0.001/4)(5)=1.25 mV.

6. Gauge pressure.

7. To amplify/scale/filter/isolate/complete excitation so the signal fits the ADC and high-frequency content does not alias.

8. 150 kPa.

9. Eel=0-59(5-7)=+118 mV.

10. Its charge output is produced by changing deformation and practical leakage makes long-term static measurement difficult.


---

## Quick Reference

**Handbook anchor:** Instrumentation, Measurement, and Control, printed pp. 225–231.

- **resistance temperature detector:** Resistance Temperature Detectors — RTDs
- **thermistor:** Thermistors
- **thermocouple:** Thermocouples and the Seebeck Effect
- **strain transducer:** Strain Gauges, Piezoresistive, and Piezoelectric Transducers
- **Wheatstone bridge:** Wheatstone Bridges
- **process sensor selection:** Pressure, pH, and Chemical Sensors
- **signal conditioning:** Signal Conditioning
---

## What's Next

**02-68 — Data Acquisition, Sampling, Dynamic Response, and Frequency Response**

Carry forward the measurement-and-control workflow: define the measurand and signal path, establish calibration and uncertainty, identify dynamics and sampling limits, then verify feedback stability and hardware constraints.


— Your Mentor