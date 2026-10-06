---
chapter: "03-39"
title: "Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-039-01, ECE-3-039-02, ECE-3-039-03, ECE-3-039-04, ECE-3-039-05, ECE-3-039-06, ECE-3-039-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-39: Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** CTRL-2F-069-01 · INST-2F-068-02 · MATH-1C-025-06

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **39.1** Explain and apply **LTI systems, impulse response, and convolution**.
* **39.2** Explain and apply **Fourier transform pairs and frequency-domain response**.
* **39.3** Explain and apply **Fourier series and harmonic content**.
* **39.4** Explain and apply **Transfer functions, poles, zeros, and frequency response**.
* **39.5** Explain and apply **Bode magnitude and phase approximations**.
* **39.6** Explain and apply **Sampling, Nyquist criterion, and aliasing**.
* **39.7** Explain and apply **Digital filters, difference equations, and z transforms**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 39.1 LTI systems, impulse response, and convolution

A linear time-invariant system is completely characterized by its impulse response. Convolution computes the response to an arbitrary input.

\[y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau\]

![FIG-03-39-001: Input signal, impulse response, flip-shift-multiply integration concept, and resulting convolution output.](../figures/FIG-03-39-001-lti-systems-impulse-response-and-convolution.png)

### Worked Example 1

**Problem.** If h(t)=δ(t-t0), the output is a delayed copy x(t-t0).

**Solution.** Use the relation and model in §39.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 39.2 Fourier transform pairs and frequency-domain response

The Fourier transform converts convolution in time to multiplication in frequency. This is central to filter and communications analysis.

\[Y(f)=H(f)X(f)\]

![FIG-03-39-002: Block diagram linking x(t), h(t), y(t) with X(f), H(f), and Y(f)=H(f)X(f).](../figures/FIG-03-39-002-fourier-transform-pairs-and-frequency-domain-response.png)

### Worked Example 2

**Problem.** A frequency component where H(f)=0 is removed from the output.

**Solution.** Use the relation and model in §39.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 39.3 Fourier series and harmonic content

Periodic signals can be decomposed into DC and harmonic components. Parseval's relation links signal power to Fourier coefficients.

\[x(t)=\sum_{n=-\infty}^{\infty}X_n e^{j2\pi n f_0t}\]

![FIG-03-39-003: Periodic nonsinusoidal waveform with corresponding discrete harmonic spectrum.](../figures/FIG-03-39-003-fourier-series-and-harmonic-content.png)

### Worked Example 3

**Problem.** A square wave contains a fundamental plus harmonics even though its time waveform is not sinusoidal.

**Solution.** Use the relation and model in §39.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 39.4 Transfer functions, poles, zeros, and frequency response

A transfer function encodes system dynamics under stated initial-condition conventions. Poles drive natural response and stability; zeros shape transmission.

\[H(s)=\frac{Y(s)}{X(s)}\]

![FIG-03-39-004: Transfer-function block with pole-zero plot and corresponding time/frequency-response features.](../figures/FIG-03-39-004-transfer-functions-poles-zeros-and-frequency-response.png)

### Worked Example 4

**Problem.** A pole closer to the imaginary axis generally corresponds to a slower decaying mode than a far-left pole.

**Solution.** Use the relation and model in §39.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 39.5 Bode magnitude and phase approximations

Bode plots display frequency response on logarithmic frequency scales. First-order poles and zeros contribute characteristic slope and phase transitions.

\[\mathrm{dB}=20\log_{10}|H(j\omega)|\]

![FIG-03-39-005: Magnitude and phase Bode plots for gain, pole, and zero factors with asymptotic slopes.](../figures/FIG-03-39-005-bode-magnitude-and-phase-approximations.png)

### Worked Example 5

**Problem.** A single first-order pole contributes approximately -20 dB/decade well above its corner frequency.

**Solution.** Use the relation and model in §39.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 39.6 Sampling, Nyquist criterion, and aliasing

A bandlimited low-pass signal can be ideally reconstructed from uniform samples when the sampling frequency exceeds twice its highest frequency. Undersampling causes spectral overlap and aliasing.

\[f_s>2W\]

![FIG-03-39-006: Time samples and replicated frequency spectra illustrating adequate sampling versus aliasing.](../figures/FIG-03-39-006-sampling-nyquist-criterion-and-aliasing.png)

### Worked Example 6

**Problem.** A 4-kHz bandlimited message requires sampling above 8 kHz under the ideal criterion.

**Solution.** Use the relation and model in §39.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 39.7 Digital filters, difference equations, and z transforms

Discrete-time LTI systems may be represented by difference equations, impulse responses, and z-domain transfer functions. FIR and IIR structures differ in impulse-response duration and feedback structure.

\[H(z)=\frac{Y(z)}{X(z)}\]

![FIG-03-39-007: Difference-equation block diagram with delay elements, FIR/IIR paths, and corresponding z-domain transfer function.](../figures/FIG-03-39-007-digital-filters-difference-equations-and-z-transforms.png)

### Worked Example 7

**Problem.** A pure delay y[n]=x[n-1] has transfer function z^-1.

**Solution.** Use the relation and model in §39.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation gives a numerical answer but violates the assumed device region, logic state, or protocol condition. Is the answer valid?

**Solution.** No. Re-select the appropriate piecewise model or system state and solve again. Algebraic consistency does not override the model's validity conditions.

### Worked Example 9

**Problem.** A remembered formula differs from the expression printed in the FE Reference Handbook. Which should govern an exam solution?

**Solution.** Use the Handbook expression and its definitions unless the problem explicitly supplies a different model.

---

## As the Handbook States It

Primary source basis: **FE Electrical and Computer specification Area 7–8; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using continuous-time convolution outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Fourier transform system response outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Fourier series outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using linear-system transfer function outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Bode plot outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Nyquist sampling criterion outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using digital filter transfer function outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| continuous-time convolution | Concept developed in §39.1; apply with that section's stated model and conventions. |
| Fourier transform system response | Concept developed in §39.2; apply with that section's stated model and conventions. |
| Fourier series | Concept developed in §39.3; apply with that section's stated model and conventions. |
| linear-system transfer function | Concept developed in §39.4; apply with that section's stated model and conventions. |
| Bode plot | Concept developed in §39.5; apply with that section's stated model and conventions. |
| Nyquist sampling criterion | Concept developed in §39.6; apply with that section's stated model and conventions. |
| digital filter transfer function | Concept developed in §39.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **continuous-time convolution** and identify the governing relation, state variable, or decision it organizes.

2. Define **Fourier transform system response** and identify the governing relation, state variable, or decision it organizes.

3. Define **Fourier series** and identify the governing relation, state variable, or decision it organizes.

4. Define **linear-system transfer function** and identify the governing relation, state variable, or decision it organizes.

5. Define **Bode plot** and identify the governing relation, state variable, or decision it organizes.

6. Define **Nyquist sampling criterion** and identify the governing relation, state variable, or decision it organizes.

7. Define **digital filter transfer function** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **continuous-time convolution**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **Fourier transform system response**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **Fourier series**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **linear-system transfer function**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **Bode plot**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **Nyquist sampling criterion**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **digital filter transfer function**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **continuous-time convolution**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **Fourier transform system response**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **Fourier series**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **linear-system transfer function**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **Bode plot**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **Nyquist sampling criterion**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **digital filter transfer function**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **continuous-time convolution**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **Fourier transform system response**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **continuous-time convolution** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **Fourier transform system response** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **Fourier series** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **linear-system transfer function** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **Bode plot** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **Nyquist sampling criterion** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **digital filter transfer function** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **continuous-time convolution**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **Fourier transform system response**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **Fourier series**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **linear-system transfer function**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **Bode plot**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **Nyquist sampling criterion**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **digital filter transfer function**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

15. The same symbol or equation can represent different physical behavior outside its valid device region, frequency range, timing model, or protocol abstraction.

16. The Handbook is the exam reference; using its definitions prevents hidden differences in constants, RMS/peak values, sign convention, or model form.

17. Algebra can be internally consistent while predicting an impossible device state, voltage, timing relationship, address range, or complexity claim. The physical/logical model must also be satisfied.

18. Limiting cases and order-of-magnitude checks expose sign errors, impossible gains, invalid probabilities, unrealistic timing, and model misuse.

19. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

20. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

21. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

22. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

23. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

24. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

25. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

26. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.

27. **A.** The relation or workflow depends on the stated model, operating region, units, and conventions.


---

## Practice Problems

1. If h(t)=δ(t-t0), the output is a delayed copy x(t-t0).

2. A frequency component where H(f)=0 is removed from the output.

3. A square wave contains a fundamental plus harmonics even though its time waveform is not sinusoidal.

4. A pole closer to the imaginary axis generally corresponds to a slower decaying mode than a far-left pole.

5. A single first-order pole contributes approximately -20 dB/decade well above its corner frequency.

6. A 4-kHz bandlimited message requires sampling above 8 kHz under the ideal criterion.

7. A pure delay y[n]=x[n-1] has transfer function z^-1.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §39.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §39.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §39.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §39.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §39.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §39.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §39.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 7–8, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 7–8.

- **continuous-time convolution:** LTI systems, impulse response, and convolution
- **Fourier transform system response:** Fourier transform pairs and frequency-domain response
- **Fourier series:** Fourier series and harmonic content
- **linear-system transfer function:** Transfer functions, poles, zeros, and frequency response
- **Bode plot:** Bode magnitude and phase approximations
- **Nyquist sampling criterion:** Sampling, Nyquist criterion, and aliasing
- **digital filter transfer function:** Digital filters, difference equations, and z transforms

---

## What's Next

**Chapter 03-40: Communications — AM, FM, PM, PCM, Bandwidth, and Noise**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
