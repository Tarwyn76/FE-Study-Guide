---
chapter: "03-41"
title: "Multiplexing and Digital Communications"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-041-01, ECE-3-041-02, ECE-3-041-03, ECE-3-041-04, ECE-3-041-05, ECE-3-041-06, ECE-3-041-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-41: Multiplexing and Digital Communications

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-040-07

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Multiplexing and Digital Communications**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **41.1** Explain and apply **Time-, frequency-, and code-division multiplexing**.
* **41.2** Explain and apply **Binary data rate, symbol rate, and modulation alphabet**.
* **41.3** Explain and apply **Digital modulation concepts — ASK, FSK, PSK, and QAM**.
* **41.4** Explain and apply **Error detection — parity and CRC**.
* **41.5** Explain and apply **Forward error correction and redundancy**.
* **41.6** Explain and apply **Transmission, propagation, queueing, and processing delay**.
* **41.7** Explain and apply **Reliable transmission, ARQ, sliding windows, and throughput**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 41.1 Time-, frequency-, and code-division multiplexing

Multiplexing allows several information streams to share a channel by assigning orthogonal or separable resources. The receiver must know how to separate the streams.

\[\text{shared channel resource}\rightarrow\text{separated by time, frequency, or code}\]

![FIG-03-41-001: Three-panel TDM, FDM, and CDM resource allocation diagrams.](../figures/FIG-03-41-001-time-frequency-and-code-division-multiplexing.png)

### Worked Example 1

**Problem.** TDM assigns different time slots; FDM assigns different frequency bands.

**Solution.** Use the relation and model in §41.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 41.2 Binary data rate, symbol rate, and modulation alphabet

An M-ary symbol carries log2(M) bits when symbols are used equiprobably. Symbol rate and bit rate are therefore not generally the same.

\[R_b=R_s\log_2 M\]

![FIG-03-41-002: Bit groups mapped to M-ary symbols with bit rate, symbol rate, and constellation examples.](../figures/FIG-03-41-002-binary-data-rate-symbol-rate-and-modulation-alphabet.png)

### Worked Example 2

**Problem.** QPSK has M=4 and ideally carries 2 bits per symbol.

**Solution.** Use the relation and model in §41.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 41.3 Digital modulation concepts — ASK, FSK, PSK, and QAM

Digital modulation maps bits to discrete carrier states. ASK varies amplitude, FSK frequency, PSK phase, and QAM combines amplitude and phase.

\[\text{symbol}\rightarrow\text{amplitude/frequency/phase state}\]

![FIG-03-41-003: ASK, FSK, BPSK/QPSK, and QAM constellation/waveform examples.](../figures/FIG-03-41-003-digital-modulation-concepts-ask-fsk-psk-and-qam.png)

### Worked Example 3

**Problem.** BPSK uses two carrier phases to represent one bit per symbol.

**Solution.** Use the relation and model in §41.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 41.4 Error detection — parity and CRC

Parity detects certain bit errors with minimal overhead; CRC treats bit strings as polynomials and is much stronger for burst-error detection.

\[\frac{T(x)+E(x)}{G(x)}\rightarrow 0\text{ remainder for a valid CRC check}\]

![FIG-03-41-004: Frame with payload, CRC remainder generation, noisy channel, and receiver syndrome check.](../figures/FIG-03-41-004-error-detection-parity-and-crc.png)

### Worked Example 4

**Problem.** A single parity bit can detect any odd number of bit flips but cannot correct them.

**Solution.** Use the relation and model in §41.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 41.5 Forward error correction and redundancy

Error-correcting codes add structured redundancy so a receiver can infer and correct some channel errors. Hamming, block, and Reed-Solomon codes are named in the Handbook.

\[\text{redundancy}\uparrow \Rightarrow \text{error-correction capability}\uparrow\text{, with rate cost}\]

![FIG-03-41-005: Codewords in Hamming-space concept with error radius and received word.](../figures/FIG-03-41-005-forward-error-correction-and-redundancy.png)

### Worked Example 5

**Problem.** Correction requires more redundancy than mere detection for the same error pattern class.

**Solution.** Use the relation and model in §41.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 41.6 Transmission, propagation, queueing, and processing delay

Digital communication over networks accumulates several distinct delays. Packet length and link rate set transmission delay; physical distance and propagation speed set propagation delay.

\[d_{trans}=\frac{L}{R},\qquad d_{prop}=\frac{d}{s}\]

![FIG-03-41-006: Packet timeline showing processing, queueing, transmission, and propagation delay components.](../figures/FIG-03-41-006-transmission-propagation-queueing-and-processing-delay.png)

### Worked Example 6

**Problem.** A 1-Mbit packet on a 10-Mbit/s link has 0.1-s transmission delay.

**Solution.** Use the relation and model in §41.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 41.7 Reliable transmission, ARQ, sliding windows, and throughput

ARQ retransmits frames when errors or timeouts occur. Sliding-window protocols permit multiple unacknowledged frames, improving utilization on long-delay paths.

\[U_{\text{stop-wait}}\approx \frac{d_{trans}}{D}\]

![FIG-03-41-007: Stop-and-wait and sliding-window sequence diagrams with packet, ACK/NAK, timeout, and retransmission.](../figures/FIG-03-41-007-reliable-transmission-arq-sliding-windows-and-throughput.png)

### Worked Example 7

**Problem.** Stop-and-wait utilization becomes poor when propagation delay greatly exceeds transmission delay.

**Solution.** Use the relation and model in §41.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

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

Primary source basis: **FE Electrical and Computer specification Area 13; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using multiplexing outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using digital symbol rate outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using digital modulation outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using error detection coding outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using error correction coding outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using network communication delay outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using automatic repeat request outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| multiplexing | Concept developed in §41.1; apply with that section's stated model and conventions. |
| digital symbol rate | Concept developed in §41.2; apply with that section's stated model and conventions. |
| digital modulation | Concept developed in §41.3; apply with that section's stated model and conventions. |
| error detection coding | Concept developed in §41.4; apply with that section's stated model and conventions. |
| error correction coding | Concept developed in §41.5; apply with that section's stated model and conventions. |
| network communication delay | Concept developed in §41.6; apply with that section's stated model and conventions. |
| automatic repeat request | Concept developed in §41.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **multiplexing** and identify the governing relation, state variable, or decision it organizes.

2. Define **digital symbol rate** and identify the governing relation, state variable, or decision it organizes.

3. Define **digital modulation** and identify the governing relation, state variable, or decision it organizes.

4. Define **error detection coding** and identify the governing relation, state variable, or decision it organizes.

5. Define **error correction coding** and identify the governing relation, state variable, or decision it organizes.

6. Define **network communication delay** and identify the governing relation, state variable, or decision it organizes.

7. Define **automatic repeat request** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **multiplexing**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **digital symbol rate**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **digital modulation**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **error detection coding**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **error correction coding**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **network communication delay**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **automatic repeat request**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **multiplexing**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **digital symbol rate**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **digital modulation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **error detection coding**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **error correction coding**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **network communication delay**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **automatic repeat request**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **multiplexing**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **digital symbol rate**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **multiplexing** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **digital symbol rate** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **digital modulation** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **error detection coding** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **error correction coding** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **network communication delay** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **automatic repeat request** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **multiplexing**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **digital symbol rate**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **digital modulation**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **error detection coding**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **error correction coding**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **network communication delay**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **automatic repeat request**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

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

1. TDM assigns different time slots; FDM assigns different frequency bands.

2. QPSK has M=4 and ideally carries 2 bits per symbol.

3. BPSK uses two carrier phases to represent one bit per symbol.

4. A single parity bit can detect any odd number of bit flips but cannot correct them.

5. Correction requires more redundancy than mere detection for the same error pattern class.

6. A 1-Mbit packet on a 10-Mbit/s link has 0.1-s transmission delay.

7. Stop-and-wait utilization becomes poor when propagation delay greatly exceeds transmission delay.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §41.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §41.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §41.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §41.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §41.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §41.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §41.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 13, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 13.

- **multiplexing:** Time-, frequency-, and code-division multiplexing
- **digital symbol rate:** Binary data rate, symbol rate, and modulation alphabet
- **digital modulation:** Digital modulation concepts — ASK, FSK, PSK, and QAM
- **error detection coding:** Error detection — parity and CRC
- **error correction coding:** Forward error correction and redundancy
- **network communication delay:** Transmission, propagation, queueing, and processing delay
- **automatic repeat request:** Reliable transmission, ARQ, sliding windows, and throughput

---

## What's Next

**Chapter 03-42: Digital Logic — Number Systems, Boolean Algebra, Gates, and Minimization**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
