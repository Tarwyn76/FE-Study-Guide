---
chapter: "03-40"
title: "Communications — AM, FM, PM, PCM, Bandwidth, and Noise"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-040-01, ECE-3-040-02, ECE-3-040-03, ECE-3-040-04, ECE-3-040-05, ECE-3-040-06, ECE-3-040-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-40: Communications — AM, FM, PM, PCM, Bandwidth, and Noise

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-039-07 · ELEC-2E-062-01

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Communications — AM, FM, PM, PCM, Bandwidth, and Noise**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **40.1** Explain and apply **Baseband signals, carriers, and modulation purpose**.
* **40.2** Explain and apply **Conventional AM, modulation index, and bandwidth**.
* **40.3** Explain and apply **DSB and SSB tradeoffs**.
* **40.4** Explain and apply **Angle modulation, instantaneous frequency, FM, and PM**.
* **40.5** Explain and apply **Carson bandwidth for wideband FM**.
* **40.6** Explain and apply **PCM sampling, quantization, and bit rate**.
* **40.7** Explain and apply **Noise, SNR, decibels, and channel capacity**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 40.1 Baseband signals, carriers, and modulation purpose

Modulation shifts information to a carrier suitable for transmission, sharing spectrum, antenna constraints, or channel characteristics. Amplitude, phase, and frequency modulation alter different carrier parameters.

\[s(t)=A(t)\cos(2\pi f_ct+\phi(t))\]

![FIG-03-40-001: Message, carrier, and representative AM/FM/PM waveforms aligned in time.](../figures/FIG-03-40-001-baseband-signals-carriers-and-modulation-purpose.png)

### Worked Example 1

**Problem.** Changing only carrier amplitude with the message is amplitude modulation.

**Solution.** Start from the §40.1 relation \(s(t)=A(t)\cos(2\pi f_ct+\phi(t))\). The statement follows from the physical or logical meaning of **Baseband signals, carriers, and modulation purpose**: Changing only carrier amplitude with the message is amplitude modulation. Accept that conclusion only while the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

---

## 40.2 Conventional AM, modulation index, and bandwidth

Conventional AM produces carrier plus upper and lower sidebands. Overmodulation in an envelope-detected system causes distortion.

\[x_{AM}(t)=A_c[1+a\,m_n(t)]\cos(2\pi f_ct),\qquad B=2W\]

![FIG-03-40-002: AM time waveform and spectrum showing carrier and upper/lower sidebands.](../figures/FIG-03-40-002-conventional-am-modulation-index-and-bandwidth.png)

### Worked Example 2

**Problem.** A 5-kHz message bandwidth requires 10-kHz ideal AM bandwidth.

**Solution.** Start from the §40.2 relation \(x_{AM}(t)=A_c[1+a\,m_n(t)]\cos(2\pi f_ct),\qquad B=2W\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: A 5-kHz message bandwidth requires 10-kHz ideal AM bandwidth. Carry the stated units through the calculation and accept the result only after confirming that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

---

## 40.3 DSB and SSB tradeoffs

Suppressing the carrier and/or one sideband improves power or bandwidth efficiency at the cost of more demanding coherent demodulation.

\[B_{DSB}=2W,\qquad B_{SSB}=W\]

![FIG-03-40-003: Spectra for conventional AM, DSB-SC, lower SSB, and upper SSB for the same baseband signal.](../figures/FIG-03-40-003-dsb-and-ssb-tradeoffs.png)

### Worked Example 3

**Problem.** A 3-kHz voice channel occupies about 3 kHz in ideal SSB versus 6 kHz in DSB.

**Solution.** Start from the §40.3 relation \(B_{DSB}=2W,\qquad B_{SSB}=W\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: A 3-kHz voice channel occupies about 3 kHz in ideal SSB versus 6 kHz in DSB. Carry the stated units through the calculation and accept the result only after confirming that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

---

## 40.4 Angle modulation, instantaneous frequency, FM, and PM

FM varies instantaneous frequency while PM varies phase directly. Both are angle modulation and maintain constant ideal carrier envelope.

\[\omega_i(t)=\frac{d\theta(t)}{dt}\]

![FIG-03-40-004: Message waveform with corresponding FM instantaneous frequency and PM phase deviation.](../figures/FIG-03-40-004-angle-modulation-instantaneous-frequency-fm-and-pm.png)

### Worked Example 4

**Problem.** A constant message in FM produces a constant frequency offset; in PM it produces a constant phase offset.

**Solution.** Start from the §40.4 relation \(\omega_i(t)=\frac{d\theta(t)}{dt}\). The statement follows from the physical or logical meaning of **Angle modulation, instantaneous frequency, FM, and PM**: A constant message in FM produces a constant frequency offset; in PM it produces a constant phase offset. Accept that conclusion only while the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

---

## 40.5 Carson bandwidth for wideband FM

Wideband FM occupies more bandwidth than narrowband FM. Carson's rule estimates the bandwidth containing about 98% of signal power.

\[B\approx 2(\Delta f+W)=2(D+1)W\]

![FIG-03-40-005: FM spectrum concept with frequency deviation, message bandwidth, and Carson-rule occupied bandwidth.](../figures/FIG-03-40-005-carson-bandwidth-for-wideband-fm.png)

### Worked Example 5

**Problem.** If Δf=75 kHz and W=15 kHz, B≈180 kHz.

**Solution.** Start from the §40.5 relation \(B\approx 2(\Delta f+W)=2(D+1)W\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: If Δf=75 kHz and W=15 kHz, B≈180 kHz. Carry the stated units through the calculation and accept the result only after confirming that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

---

## 40.6 PCM sampling, quantization, and bit rate

PCM samples an analog message, quantizes sample amplitude, and encodes each sample in an n-bit word. More bits increase quantization levels and required bit rate.

\[q=2^n,\qquad R_b\ge 2nW\]

![FIG-03-40-006: Anti-alias filter, sampler, quantizer, encoder, channel, decoder, and reconstruction filter.](../figures/FIG-03-40-006-pcm-sampling-quantization-and-bit-rate.png)

### Worked Example 6

**Problem.** An 8-bit PCM system has 256 quantization levels.

**Solution.** Start from the §40.6 relation \(q=2^n,\qquad R_b\ge 2nW\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: An 8-bit PCM system has 256 quantization levels. Carry the stated units through the calculation and accept the result only after confirming that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

---

## 40.7 Noise, SNR, decibels, and channel capacity

Noise limits reliable communications. SNR may be stated as a linear ratio or in decibels; Shannon capacity gives an upper bound for an idealized noisy channel.

\[C=B\log_2(1+S/N)\]

![FIG-03-40-007: Channel capacity versus SNR for several bandwidths with linear and dB SNR labels.](../figures/FIG-03-40-007-noise-snr-decibels-and-channel-capacity.png)

### Worked Example 7

**Problem.** For B=1 MHz and S/N=15, capacity is 4 Mb/s because log2(16)=4.

**Solution.** Start from the §40.7 relation \(C=B\log_2(1+S/N)\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: For B=1 MHz and S/N=15, capacity is 4 Mb/s because log2(16)=4. Carry the stated units through the calculation and accept the result only after confirming that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation gives a numerical answer but violates the assumed device region, logic state, or protocol condition. Is the answer valid?

**Solution.** No. In **Communications — AM, FM, PM, PCM, Bandwidth, and Noise**, a tidy numerical or logical result is still invalid if it contradicts the model assumptions. A representative failure is an FM/PM bandwidth relation used outside its assumptions or an SNR in dB inserted where a linear ratio is required. Return to the applicable section, choose the state/model consistent with the solved quantities, recompute if needed, and confirm that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

### Worked Example 9

**Problem.** A remembered formula differs from the expression printed in the FE Reference Handbook. Which should govern an exam solution?

**Solution.** Use the FE Reference Handbook expression and its definitions as the controlling exam reference unless the problem explicitly defines another model. For **Communications — AM, FM, PM, PCM, Bandwidth, and Noise**, match symbols, units, reference directions, RMS/peak or digital conventions, and assumptions to the Handbook first. External references support only specification-required learned concepts that the Handbook does not directly develop.

---

## As the Handbook States It

Primary source basis: **FE Electrical and Computer specification Area 13; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required engineering/computing knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those two bodies of material into exam-oriented explanations and examples; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Proakis, J. G., & Salehi, M. (2008). *Digital Communications* (5th ed.). McGraw-Hill. ISBN 978-0-07-295716-7. Supporting scope: Digital modulation, bandwidth, coding, detection, error control, and digital communication systems.

The external references support only the learned/application portion of the specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using modulation concept outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using amplitude modulation outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using sideband modulation outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using angle modulation outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Carson rule outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using pulse-code modulation outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Shannon channel capacity outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| modulation concept | Concept developed in §40.1; apply with that section's stated model and conventions. |
| amplitude modulation | Concept developed in §40.2; apply with that section's stated model and conventions. |
| sideband modulation | Concept developed in §40.3; apply with that section's stated model and conventions. |
| angle modulation | Concept developed in §40.4; apply with that section's stated model and conventions. |
| Carson rule | Concept developed in §40.5; apply with that section's stated model and conventions. |
| pulse-code modulation | Concept developed in §40.6; apply with that section's stated model and conventions. |
| Shannon channel capacity | Concept developed in §40.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **modulation concept** and identify the governing relation, state variable, or decision it organizes.

2. Define **amplitude modulation** and identify the governing relation, state variable, or decision it organizes.

3. Define **sideband modulation** and identify the governing relation, state variable, or decision it organizes.

4. Define **angle modulation** and identify the governing relation, state variable, or decision it organizes.

5. Define **Carson rule** and identify the governing relation, state variable, or decision it organizes.

6. Define **pulse-code modulation** and identify the governing relation, state variable, or decision it organizes.

7. Define **Shannon channel capacity** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **modulation concept**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **amplitude modulation**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **sideband modulation**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **angle modulation**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **Carson rule**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **pulse-code modulation**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **Shannon channel capacity**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **modulation concept**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **amplitude modulation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **sideband modulation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **angle modulation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **Carson rule**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **pulse-code modulation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **Shannon channel capacity**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **modulation concept**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **amplitude modulation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **modulation concept** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **amplitude modulation** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **sideband modulation** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **angle modulation** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **Carson rule** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **pulse-code modulation** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **Shannon channel capacity** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **modulation concept**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **amplitude modulation**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **sideband modulation**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **angle modulation**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **Carson rule**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **pulse-code modulation**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **Shannon channel capacity**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

15. In Communications — AM, FM, PM, PCM, Bandwidth, and Noise, the same equation or symbol can change meaning when the operating state, abstraction, timing model, or signal convention changes; verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

16. The FE Reference Handbook is the exam reference for Communications — AM, FM, PM, PCM, Bandwidth, and Noise. Match its variable definitions and conventions before substitution; external references support only learned material not developed in the Handbook.

17. An algebraically consistent answer can still be invalid in Communications — AM, FM, PM, PCM, Bandwidth, and Noise. Reject a result that implies an FM/PM bandwidth relation used outside its assumptions or an SNR in dB inserted where a linear ratio is required and reselect the appropriate model or state.

18. A useful independent check for this chapter is to let modulation depth or deviation approach zero and verify that the waveform approaches the unmodulated carrier. If the result does not reduce correctly, recheck the model, sign convention, and arithmetic.

19. **A.** For **Baseband signals, carriers, and modulation purpose**, the governing section model is \(s(t)=A(t)\cos(2\pi f_ct+\phi(t))\). Apply it only with the definitions and assumptions stated in §40.1, then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

20. **A.** For **Conventional AM, modulation index, and bandwidth**, the governing section model is \(x_{AM}(t)=A_c[1+a\,m_n(t)]\cos(2\pi f_ct),\qquad B=2W\). Apply it only with the definitions and assumptions stated in §40.2, then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

21. **A.** For **DSB and SSB tradeoffs**, the governing section model is \(B_{DSB}=2W,\qquad B_{SSB}=W\). Apply it only with the definitions and assumptions stated in §40.3, then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

22. **A.** For **Angle modulation, instantaneous frequency, FM, and PM**, the governing section model is \(\omega_i(t)=\frac{d\theta(t)}{dt}\). Apply it only with the definitions and assumptions stated in §40.4, then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

23. **A.** For **Carson bandwidth for wideband FM**, the governing section model is \(B\approx 2(\Delta f+W)=2(D+1)W\). Apply it only with the definitions and assumptions stated in §40.5, then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

24. **A.** For **PCM sampling, quantization, and bit rate**, the governing section model is \(q=2^n,\qquad R_b\ge 2nW\). Apply it only with the definitions and assumptions stated in §40.6, then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

25. **A.** For **Noise, SNR, decibels, and channel capacity**, the governing section model is \(C=B\log_2(1+S/N)\). Apply it only with the definitions and assumptions stated in §40.7, then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

26. **A.** For an integrated Communications — AM, FM, PM, PCM, Bandwidth, and Noise problem, separate the physical/logical model from the arithmetic, solve with the relevant section relations, and cross-check the result against the chapter-specific validity conditions.

27. **A.** In **Communications — AM, FM, PM, PCM, Bandwidth, and Noise**, the source boundary is explicit: FE-Handbook-supported material remains tied to the ledger, externally supported material uses the chapter references for modulation, bandwidth, PCM, and noise (PROAKIS), and guide synthesis is identified as supplemental explanation rather than Handbook text.


---

## Practice Problems

1. Changing only carrier amplitude with the message is amplitude modulation.

2. A 5-kHz message bandwidth requires 10-kHz ideal AM bandwidth.

3. A 3-kHz voice channel occupies about 3 kHz in ideal SSB versus 6 kHz in DSB.

4. A constant message in FM produces a constant frequency offset; in PM it produces a constant phase offset.

5. If Δf=75 kHz and W=15 kHz, B≈180 kHz.

6. An 8-bit PCM system has 256 quantization levels.

7. For B=1 MHz and S/N=15, capacity is 4 Mb/s because log2(16)=4.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. **Independent check for §40.1.** Begin independently with \(s(t)=A(t)\cos(2\pi f_ct+\phi(t))\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Changing only carrier amplitude with the message is amplitude modulation. Then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

2. **Independent check for §40.2.** Begin independently with \(x_{AM}(t)=A_c[1+a\,m_n(t)]\cos(2\pi f_ct),\qquad B=2W\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A 5-kHz message bandwidth requires 10-kHz ideal AM bandwidth. Then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

3. **Independent check for §40.3.** Begin independently with \(B_{DSB}=2W,\qquad B_{SSB}=W\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A 3-kHz voice channel occupies about 3 kHz in ideal SSB versus 6 kHz in DSB. Then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

4. **Independent check for §40.4.** Begin independently with \(\omega_i(t)=\frac{d\theta(t)}{dt}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A constant message in FM produces a constant frequency offset; in PM it produces a constant phase offset. Then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

5. **Independent check for §40.5.** Begin independently with \(B\approx 2(\Delta f+W)=2(D+1)W\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: If Δf=75 kHz and W=15 kHz, B≈180 kHz. Then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

6. **Independent check for §40.6.** Begin independently with \(q=2^n,\qquad R_b\ge 2nW\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: An 8-bit PCM system has 256 quantization levels. Then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

7. **Independent check for §40.7.** Begin independently with \(C=B\log_2(1+S/N)\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: For B=1 MHz and S/N=15, capacity is 4 Mb/s because log2(16)=4. Then verify that the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

8. Check the chapter-specific failure mode first: an FM/PM bandwidth relation used outside its assumptions or an SNR in dB inserted where a linear ratio is required. Do not accept the numerical or logical result until the modulation definition, bandwidth convention, SNR convention, and channel assumptions are the ones used by the relation.

9. For **Communications — AM, FM, PM, PCM, Bandwidth, and Noise**, start with the FE Electrical and Computer specification/Handbook location recorded in the ledger, then use the chapter's reconciled source set for modulation, bandwidth, PCM, and noise (PROAKIS) when the concept is split-required. That preserves the Handbook-versus-learned-material boundary.

10. Use this limiting check: let modulation depth or deviation approach zero and verify that the waveform approaches the unmodulated carrier. The simplified case should produce the expected physical, timing, logic, protocol, or complexity behavior before the full solution is trusted.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 13.

- **modulation concept:** Baseband signals, carriers, and modulation purpose
- **amplitude modulation:** Conventional AM, modulation index, and bandwidth
- **sideband modulation:** DSB and SSB tradeoffs
- **angle modulation:** Angle modulation, instantaneous frequency, FM, and PM
- **Carson rule:** Carson bandwidth for wideband FM
- **pulse-code modulation:** PCM sampling, quantization, and bit rate
- **Shannon channel capacity:** Noise, SNR, decibels, and channel capacity

---

## What's Next

**Chapter 03-41: Multiplexing and Digital Communications**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
