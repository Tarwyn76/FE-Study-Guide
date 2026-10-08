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

**Solution.** Start from the §39.1 relation \(y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: If h(t)=δ(t-t0), the output is a delayed copy x(t-t0). Carry the stated units through the calculation and accept the result only after confirming that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

---

## 39.2 Fourier transform pairs and frequency-domain response

The Fourier transform converts convolution in time to multiplication in frequency. This is central to filter and communications analysis.

\[Y(f)=H(f)X(f)\]

![FIG-03-39-002: Block diagram linking x(t), h(t), y(t) with X(f), H(f), and Y(f)=H(f)X(f).](../figures/FIG-03-39-002-fourier-transform-pairs-and-frequency-domain-response.png)

### Worked Example 2

**Problem.** A frequency component where H(f)=0 is removed from the output.

**Solution.** Start from the §39.2 relation \(Y(f)=H(f)X(f)\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: A frequency component where H(f)=0 is removed from the output. Carry the stated units through the calculation and accept the result only after confirming that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

---

## 39.3 Fourier series and harmonic content

Periodic signals can be decomposed into DC and harmonic components. Parseval's relation links signal power to Fourier coefficients.

\[x(t)=\sum_{n=-\infty}^{\infty}X_n e^{j2\pi n f_0t}\]

![FIG-03-39-003: Periodic nonsinusoidal waveform with corresponding discrete harmonic spectrum.](../figures/FIG-03-39-003-fourier-series-and-harmonic-content.png)

### Worked Example 3

**Problem.** A square wave contains a fundamental plus harmonics even though its time waveform is not sinusoidal.

**Solution.** Start from the §39.3 relation \(x(t)=\sum_{n=-\infty}^{\infty}X_n e^{j2\pi n f_0t}\). The statement follows from the physical or logical meaning of **Fourier series and harmonic content**: A square wave contains a fundamental plus harmonics even though its time waveform is not sinusoidal. Accept that conclusion only while the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

---

## 39.4 Transfer functions, poles, zeros, and frequency response

A transfer function encodes system dynamics under stated initial-condition conventions. Poles drive natural response and stability; zeros shape transmission.

\[H(s)=\frac{Y(s)}{X(s)}\]

![FIG-03-39-004: Transfer-function block with pole-zero plot and corresponding time/frequency-response features.](../figures/FIG-03-39-004-transfer-functions-poles-zeros-and-frequency-response.png)

### Worked Example 4

**Problem.** A pole closer to the imaginary axis generally corresponds to a slower decaying mode than a far-left pole.

**Solution.** Start from the §39.4 relation \(H(s)=\frac{Y(s)}{X(s)}\). The statement follows from the physical or logical meaning of **Transfer functions, poles, zeros, and frequency response**: A pole closer to the imaginary axis generally corresponds to a slower decaying mode than a far-left pole. Accept that conclusion only while the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

---

## 39.5 Bode magnitude and phase approximations

Bode plots display frequency response on logarithmic frequency scales. First-order poles and zeros contribute characteristic slope and phase transitions.

\[\mathrm{dB}=20\log_{10}|H(j\omega)|\]

![FIG-03-39-005: Magnitude and phase Bode plots for gain, pole, and zero factors with asymptotic slopes.](../figures/FIG-03-39-005-bode-magnitude-and-phase-approximations.png)

### Worked Example 5

**Problem.** A single first-order pole contributes approximately -20 dB/decade well above its corner frequency.

**Solution.** Start from the §39.5 relation \(\mathrm{dB}=20\log_{10}|H(j\omega)|\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: A single first-order pole contributes approximately -20 dB/decade well above its corner frequency. Carry the stated units through the calculation and accept the result only after confirming that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

---

## 39.6 Sampling, Nyquist criterion, and aliasing

A bandlimited low-pass signal can be ideally reconstructed from uniform samples when the sampling frequency exceeds twice its highest frequency. Undersampling causes spectral overlap and aliasing.

\[f_s>2W\]

![FIG-03-39-006: Time samples and replicated frequency spectra illustrating adequate sampling versus aliasing.](../figures/FIG-03-39-006-sampling-nyquist-criterion-and-aliasing.png)

### Worked Example 6

**Problem.** A 4-kHz bandlimited message requires sampling above 8 kHz under the ideal criterion.

**Solution.** Start from the §39.6 relation \(f_s>2W\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: A 4-kHz bandlimited message requires sampling above 8 kHz under the ideal criterion. Carry the stated units through the calculation and accept the result only after confirming that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

---

## 39.7 Digital filters, difference equations, and z transforms

Discrete-time LTI systems may be represented by difference equations, impulse responses, and z-domain transfer functions. FIR and IIR structures differ in impulse-response duration and feedback structure.

\[H(z)=\frac{Y(z)}{X(z)}\]

![FIG-03-39-007: Difference-equation block diagram with delay elements, FIR/IIR paths, and corresponding z-domain transfer function.](../figures/FIG-03-39-007-digital-filters-difference-equations-and-z-transforms.png)

### Worked Example 7

**Problem.** A pure delay y[n]=x[n-1] has transfer function z^-1.

**Solution.** Start from the §39.7 relation \(H(z)=\frac{Y(z)}{X(z)}\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: A pure delay y[n]=x[n-1] has transfer function z^-1. Carry the stated units through the calculation and accept the result only after confirming that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation gives a numerical answer but violates the assumed device region, logic state, or protocol condition. Is the answer valid?

**Solution.** No. In **Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models**, a tidy numerical or logical result is still invalid if it contradicts the model assumptions. A representative failure is a sampling result below the Nyquist requirement or a stability inference made from the wrong transform/model assumptions. Return to the applicable section, choose the state/model consistent with the solved quantities, recompute if needed, and confirm that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

### Worked Example 9

**Problem.** A remembered formula differs from the expression printed in the FE Reference Handbook. Which should govern an exam solution?

**Solution.** Use the FE Reference Handbook expression and its definitions as the controlling exam reference unless the problem explicitly defines another model. For **Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models**, match symbols, units, reference directions, RMS/peak or digital conventions, and assumptions to the Handbook first. External references support only specification-required learned concepts that the Handbook does not directly develop.

---

## As the Handbook States It

Primary source basis: **FE Electrical and Computer specification Area 7–8; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required engineering/computing knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those two bodies of material into exam-oriented explanations and examples; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Oppenheim, A. V., Willsky, A. S., & Nawab, S. H. (1996). *Signals and Systems* (2nd ed.). Prentice Hall/Pearson. ISBN 978-0-13-814757-0. Supporting scope: LTI systems, convolution, Fourier methods, sampling, transform models, and discrete-time systems.
- Dorf, R. C., & Bishop, R. H. (2021). *Modern Control Systems* (14th ed.). Pearson. Supporting scope: Transfer functions, poles, zeros, frequency response, Bode methods, and feedback-system interpretation.

The external references support only the learned/application portion of the specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models, the same equation or symbol can change meaning when the operating state, abstraction, timing model, or signal convention changes; verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

16. The FE Reference Handbook is the exam reference for Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models. Match its variable definitions and conventions before substitution; external references support only learned material not developed in the Handbook.

17. An algebraically consistent answer can still be invalid in Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models. Reject a result that implies a sampling result below the Nyquist requirement or a stability inference made from the wrong transform/model assumptions and reselect the appropriate model or state.

18. A useful independent check for this chapter is to apply an impulse or single sinusoid and verify that the LTI response reduces to the expected impulse/frequency response. If the result does not reduce correctly, recheck the model, sign convention, and arithmetic.

19. **A.** For **LTI systems, impulse response, and convolution**, the governing section model is \(y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau\). Apply it only with the definitions and assumptions stated in §39.1, then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

20. **A.** For **Fourier transform pairs and frequency-domain response**, the governing section model is \(Y(f)=H(f)X(f)\). Apply it only with the definitions and assumptions stated in §39.2, then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

21. **A.** For **Fourier series and harmonic content**, the governing section model is \(x(t)=\sum_{n=-\infty}^{\infty}X_n e^{j2\pi n f_0t}\). Apply it only with the definitions and assumptions stated in §39.3, then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

22. **A.** For **Transfer functions, poles, zeros, and frequency response**, the governing section model is \(H(s)=\frac{Y(s)}{X(s)}\). Apply it only with the definitions and assumptions stated in §39.4, then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

23. **A.** For **Bode magnitude and phase approximations**, the governing section model is \(\mathrm{dB}=20\log_{10}|H(j\omega)|\). Apply it only with the definitions and assumptions stated in §39.5, then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

24. **A.** For **Sampling, Nyquist criterion, and aliasing**, the governing section model is \(f_s>2W\). Apply it only with the definitions and assumptions stated in §39.6, then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

25. **A.** For **Digital filters, difference equations, and z transforms**, the governing section model is \(H(z)=\frac{Y(z)}{X(z)}\). Apply it only with the definitions and assumptions stated in §39.7, then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

26. **A.** For an integrated Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models problem, separate the physical/logical model from the arithmetic, solve with the relevant section relations, and cross-check the result against the chapter-specific validity conditions.

27. **A.** In **Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models**, the source boundary is explicit: FE-Handbook-supported material remains tied to the ledger, externally supported material uses the chapter references for signals, transforms, and frequency-response/control interpretation (OPPENHEIM / DORF), and guide synthesis is identified as supplemental explanation rather than Handbook text.


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

1. **Independent check for §39.1.** Begin independently with \(y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: If h(t)=δ(t-t0), the output is a delayed copy x(t-t0). Then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

2. **Independent check for §39.2.** Begin independently with \(Y(f)=H(f)X(f)\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A frequency component where H(f)=0 is removed from the output. Then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

3. **Independent check for §39.3.** Begin independently with \(x(t)=\sum_{n=-\infty}^{\infty}X_n e^{j2\pi n f_0t}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A square wave contains a fundamental plus harmonics even though its time waveform is not sinusoidal. Then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

4. **Independent check for §39.4.** Begin independently with \(H(s)=\frac{Y(s)}{X(s)}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A pole closer to the imaginary axis generally corresponds to a slower decaying mode than a far-left pole. Then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

5. **Independent check for §39.5.** Begin independently with \(\mathrm{dB}=20\log_{10}|H(j\omega)|\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A single first-order pole contributes approximately -20 dB/decade well above its corner frequency. Then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

6. **Independent check for §39.6.** Begin independently with \(f_s>2W\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A 4-kHz bandlimited message requires sampling above 8 kHz under the ideal criterion. Then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

7. **Independent check for §39.7.** Begin independently with \(H(z)=\frac{Y(z)}{X(z)}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A pure delay y[n]=x[n-1] has transfer function z^-1. Then verify that the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

8. Check the chapter-specific failure mode first: a sampling result below the Nyquist requirement or a stability inference made from the wrong transform/model assumptions. Do not accept the numerical or logical result until the LTI/transform assumptions, stability interpretation, and sampling conditions match the stated signal model.

9. For **Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models**, start with the FE Electrical and Computer specification/Handbook location recorded in the ledger, then use the chapter's reconciled source set for signals, transforms, and frequency-response/control interpretation (OPPENHEIM / DORF) when the concept is split-required. That preserves the Handbook-versus-learned-material boundary.

10. Use this limiting check: apply an impulse or single sinusoid and verify that the LTI response reduces to the expected impulse/frequency response. The simplified case should produce the expected physical, timing, logic, protocol, or complexity behavior before the full solution is trusted.

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
