---
chapter: "03-43"
title: "Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-043-01, ECE-3-043-02, ECE-3-043-03, ECE-3-043-04, ECE-3-043-05, ECE-3-043-06, ECE-3-043-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-43: Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-042-07

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **43.1** Explain and apply **SR, JK, and D flip-flops**.
* **43.2** Explain and apply **Registers, shift registers, and data movement**.
* **43.3** Explain and apply **Synchronous and asynchronous counters**.
* **43.4** Explain and apply **Finite-state-machine representation and design**.
* **43.5** Explain and apply **Programmable logic devices and gate arrays**.
* **43.6** Explain and apply **Setup, hold, clock-to-Q, and timing margin**.
* **43.7** Explain and apply **Asynchronous inputs, metastability, races, and hazards**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 43.1 SR, JK, and D flip-flops

Flip-flops store one bit and update state in relation to a clock or control event. Characteristic tables map current state and inputs to next state.

\[Q_{n+1}=f(Q_n,\text{inputs})\]

![FIG-03-43-001: SR, JK, and D flip-flop symbols with characteristic tables and clocked waveforms.](../figures/FIG-03-43-001-sr-jk-and-d-flip-flops.png)

### Worked Example 1

**Problem.** A D flip-flop transfers D to Q at the active clock event.

**Solution.** Start from the §43.1 relation \(Q_{n+1}=f(Q_n,\text{inputs})\). The statement follows from the physical or logical meaning of **SR, JK, and D flip-flops**: A D flip-flop transfers D to Q at the active clock event. Accept that conclusion only while the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

---

## 43.2 Registers, shift registers, and data movement

Registers group flip-flops to store and move words. Shift registers support serialization, deserialization, delay, and simple sequence generation.

\[\text{state}_{n+1}=\text{shifted state}_n+\text{new input bit}\]

![FIG-03-43-002: Four-stage shift register with serial/parallel inputs and timing sequence.](../figures/FIG-03-43-002-registers-shift-registers-and-data-movement.png)

### Worked Example 2

**Problem.** A 4-bit right-shift register moves each stored bit one position right per active clock.

**Solution.** Start from the §43.2 relation \(\text{state}_{n+1}=\text{shifted state}_n+\text{new input bit}\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: A 4-bit right-shift register moves each stored bit one position right per active clock. Carry the stated units through the calculation and accept the result only after confirming that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

---

## 43.3 Synchronous and asynchronous counters

Counters advance through a defined state sequence. Synchronous counters clock all state elements together; ripple counters propagate transitions stage by stage.

\[N_{\text{states}}\le 2^n\]

![FIG-03-43-003: Three-bit synchronous counter and ripple counter with timing waveforms.](../figures/FIG-03-43-003-synchronous-and-asynchronous-counters.png)

### Worked Example 3

**Problem.** Three flip-flops can represent up to eight binary states.

**Solution.** Start from the §43.3 relation \(N_{\text{states}}\le 2^n\). The statement follows from the physical or logical meaning of **Synchronous and asynchronous counters**: Three flip-flops can represent up to eight binary states. Accept that conclusion only while the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

---

## 43.4 Finite-state-machine representation and design

State diagrams and state tables organize sequential behavior. Moore outputs depend only on state; Mealy outputs can depend on state and current input.

\[\text{present state}+\text{input}\rightarrow\text{next state}+\text{output}\]

![FIG-03-43-004: State diagram and corresponding state table for a simple sequence detector.](../figures/FIG-03-43-004-finite-state-machine-representation-and-design.png)

### Worked Example 4

**Problem.** A traffic-light controller is naturally represented as a finite-state machine.

**Solution.** Start from the §43.4 relation \(\text{present state}+\text{input}\rightarrow\text{next state}+\text{output}\). The statement follows from the physical or logical meaning of **Finite-state-machine representation and design**: A traffic-light controller is naturally represented as a finite-state machine. Accept that conclusion only while the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

---

## 43.5 Programmable logic devices and gate arrays

PLDs and FPGAs implement combinational and sequential logic using configurable logic, interconnect, and storage resources.

\[\text{configured logic resources}\rightarrow\text{implemented digital function}\]

![FIG-03-43-005: FPGA concept with configurable logic blocks, flip-flops, routing, I/O blocks, and clock network.](../figures/FIG-03-43-005-programmable-logic-devices-and-gate-arrays.png)

### Worked Example 5

**Problem.** A complex state machine can be implemented in an FPGA without discrete gate-by-gate wiring.

**Solution.** Start from the §43.5 relation \(\text{configured logic resources}\rightarrow\text{implemented digital function}\). The statement follows from the physical or logical meaning of **Programmable logic devices and gate arrays**: A complex state machine can be implemented in an FPGA without discrete gate-by-gate wiring. Accept that conclusion only while the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

---

## 43.6 Setup, hold, clock-to-Q, and timing margin

Synchronous timing requires data to arrive early enough for setup and remain stable long enough for hold. Maximum delay limits clock frequency; minimum delay is important for hold.

\[T_{clk}\ge t_{CQ}+t_{comb,\max}+t_{setup}\]

![FIG-03-43-006: Register-to-register path with tCQ, combinational delay, setup, hold, and clock skew annotations.](../figures/FIG-03-43-006-setup-hold-clock-to-q-and-timing-margin.png)

### Worked Example 6

**Problem.** Reducing combinational delay can improve setup margin but may worsen hold margin on another path.

**Solution.** Start from the §43.6 relation \(T_{clk}\ge t_{CQ}+t_{comb,\max}+t_{setup}\). The statement follows from the physical or logical meaning of **Setup, hold, clock-to-Q, and timing margin**: Reducing combinational delay can improve setup margin but may worsen hold margin on another path. Accept that conclusion only while the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

---

## 43.7 Asynchronous inputs, metastability, races, and hazards

Inputs not aligned to the receiving clock can violate setup/hold time and produce metastability. Synchronizers reduce, but do not mathematically eliminate, the probability of propagation.

\[\text{asynchronous input}\rightarrow\text{synchronizer}\rightarrow\text{synchronous logic}\]

![FIG-03-43-007: Asynchronous signal entering a two-flop synchronizer with metastable first-stage waveform and resolved second stage.](../figures/FIG-03-43-007-asynchronous-inputs-metastability-races-and-hazards.png)

### Worked Example 7

**Problem.** A two-flip-flop synchronizer is a common method for a single asynchronous control input.

**Solution.** Start from the §43.7 relation \(\text{asynchronous input}\rightarrow\text{synchronizer}\rightarrow\text{synchronous logic}\). The statement follows from the physical or logical meaning of **Asynchronous inputs, metastability, races, and hazards**: A two-flip-flop synchronizer is a common method for a single asynchronous control input. Accept that conclusion only while the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation gives a numerical answer but violates the assumed device region, logic state, or protocol condition. Is the answer valid?

**Solution.** No. In **Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs**, a tidy numerical or logical result is still invalid if it contradicts the model assumptions. A representative failure is a clock period that violates setup time or an asynchronous input used without addressing metastability risk. Return to the applicable section, choose the state/model consistent with the solved quantities, recompute if needed, and confirm that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

### Worked Example 9

**Problem.** A remembered formula differs from the expression printed in the FE Reference Handbook. Which should govern an exam solution?

**Solution.** Use the FE Reference Handbook expression and its definitions as the controlling exam reference unless the problem explicitly defines another model. For **Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs**, match symbols, units, reference directions, RMS/peak or digital conventions, and assumptions to the Handbook first. External references support only specification-required learned concepts that the Handbook does not directly develop.

---

## As the Handbook States It

Primary source basis: **FE Electrical and Computer specification Area 15; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required engineering/computing knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those two bodies of material into exam-oriented explanations and examples; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Harris, S. L., & Harris, D. (2021). *Digital Design and Computer Architecture, RISC-V Edition*. Morgan Kaufmann. ISBN 978-0-12-820064-3. Supporting scope: Combinational/sequential logic, timing, finite-state machines, programmable logic, and digital-system organization.

The external references support only the learned/application portion of the specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using flip-flop state transition outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using shift register outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using digital counter outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using finite state machine outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using programmable logic device outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using sequential timing constraint outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using metastability outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| flip-flop state transition | Concept developed in §43.1; apply with that section's stated model and conventions. |
| shift register | Concept developed in §43.2; apply with that section's stated model and conventions. |
| digital counter | Concept developed in §43.3; apply with that section's stated model and conventions. |
| finite state machine | Concept developed in §43.4; apply with that section's stated model and conventions. |
| programmable logic device | Concept developed in §43.5; apply with that section's stated model and conventions. |
| sequential timing constraint | Concept developed in §43.6; apply with that section's stated model and conventions. |
| metastability | Concept developed in §43.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **flip-flop state transition** and identify the governing relation, state variable, or decision it organizes.

2. Define **shift register** and identify the governing relation, state variable, or decision it organizes.

3. Define **digital counter** and identify the governing relation, state variable, or decision it organizes.

4. Define **finite state machine** and identify the governing relation, state variable, or decision it organizes.

5. Define **programmable logic device** and identify the governing relation, state variable, or decision it organizes.

6. Define **sequential timing constraint** and identify the governing relation, state variable, or decision it organizes.

7. Define **metastability** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **flip-flop state transition**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **shift register**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **digital counter**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **finite state machine**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **programmable logic device**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **sequential timing constraint**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **metastability**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **flip-flop state transition**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **shift register**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **digital counter**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **finite state machine**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **programmable logic device**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **sequential timing constraint**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **metastability**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **flip-flop state transition**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **shift register**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **flip-flop state transition** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **shift register** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **digital counter** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **finite state machine** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **programmable logic device** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **sequential timing constraint** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **metastability** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **flip-flop state transition**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **shift register**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **digital counter**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **finite state machine**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **programmable logic device**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **sequential timing constraint**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **metastability**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

15. In Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs, the same equation or symbol can change meaning when the operating state, abstraction, timing model, or signal convention changes; verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

16. The FE Reference Handbook is the exam reference for Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs. Match its variable definitions and conventions before substitution; external references support only learned material not developed in the Handbook.

17. An algebraically consistent answer can still be invalid in Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs. Reject a result that implies a clock period that violates setup time or an asynchronous input used without addressing metastability risk and reselect the appropriate model or state.

18. A useful independent check for this chapter is to check the slowest path against setup time and the fastest path against hold time. If the result does not reduce correctly, recheck the model, sign convention, and arithmetic.

19. **A.** For **SR, JK, and D flip-flops**, the governing section model is \(Q_{n+1}=f(Q_n,\text{inputs})\). Apply it only with the definitions and assumptions stated in §43.1, then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

20. **A.** For **Registers, shift registers, and data movement**, the governing section model is \(\text{state}_{n+1}=\text{shifted state}_n+\text{new input bit}\). Apply it only with the definitions and assumptions stated in §43.2, then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

21. **A.** For **Synchronous and asynchronous counters**, the governing section model is \(N_{\text{states}}\le 2^n\). Apply it only with the definitions and assumptions stated in §43.3, then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

22. **A.** For **Finite-state-machine representation and design**, the governing section model is \(\text{present state}+\text{input}\rightarrow\text{next state}+\text{output}\). Apply it only with the definitions and assumptions stated in §43.4, then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

23. **A.** For **Programmable logic devices and gate arrays**, the governing section model is \(\text{configured logic resources}\rightarrow\text{implemented digital function}\). Apply it only with the definitions and assumptions stated in §43.5, then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

24. **A.** For **Setup, hold, clock-to-Q, and timing margin**, the governing section model is \(T_{clk}\ge t_{CQ}+t_{comb,\max}+t_{setup}\). Apply it only with the definitions and assumptions stated in §43.6, then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

25. **A.** For **Asynchronous inputs, metastability, races, and hazards**, the governing section model is \(\text{asynchronous input}\rightarrow\text{synchronizer}\rightarrow\text{synchronous logic}\). Apply it only with the definitions and assumptions stated in §43.7, then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

26. **A.** For an integrated Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs problem, separate the physical/logical model from the arithmetic, solve with the relevant section relations, and cross-check the result against the chapter-specific validity conditions.

27. **A.** In **Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs**, the source boundary is explicit: FE-Handbook-supported material remains tied to the ledger, externally supported material uses the chapter references for sequential logic, state machines, and timing (HARRIS), and guide synthesis is identified as supplemental explanation rather than Handbook text.


---

## Practice Problems

1. A D flip-flop transfers D to Q at the active clock event.

2. A 4-bit right-shift register moves each stored bit one position right per active clock.

3. Three flip-flops can represent up to eight binary states.

4. A traffic-light controller is naturally represented as a finite-state machine.

5. A complex state machine can be implemented in an FPGA without discrete gate-by-gate wiring.

6. Reducing combinational delay can improve setup margin but may worsen hold margin on another path.

7. A two-flip-flop synchronizer is a common method for a single asynchronous control input.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. **Independent check for §43.1.** Begin independently with \(Q_{n+1}=f(Q_n,\text{inputs})\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A D flip-flop transfers D to Q at the active clock event. Then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

2. **Independent check for §43.2.** Begin independently with \(\text{state}_{n+1}=\text{shifted state}_n+\text{new input bit}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A 4-bit right-shift register moves each stored bit one position right per active clock. Then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

3. **Independent check for §43.3.** Begin independently with \(N_{\text{states}}\le 2^n\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Three flip-flops can represent up to eight binary states. Then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

4. **Independent check for §43.4.** Begin independently with \(\text{present state}+\text{input}\rightarrow\text{next state}+\text{output}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A traffic-light controller is naturally represented as a finite-state machine. Then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

5. **Independent check for §43.5.** Begin independently with \(\text{configured logic resources}\rightarrow\text{implemented digital function}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A complex state machine can be implemented in an FPGA without discrete gate-by-gate wiring. Then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

6. **Independent check for §43.6.** Begin independently with \(T_{clk}\ge t_{CQ}+t_{comb,\max}+t_{setup}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Reducing combinational delay can improve setup margin but may worsen hold margin on another path. Then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

7. **Independent check for §43.7.** Begin independently with \(\text{asynchronous input}\rightarrow\text{synchronizer}\rightarrow\text{synchronous logic}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A two-flip-flop synchronizer is a common method for a single asynchronous control input. Then verify that the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

8. Check the chapter-specific failure mode first: a clock period that violates setup time or an asynchronous input used without addressing metastability risk. Do not accept the numerical or logical result until the active clock edge, state encoding, setup/hold constraints, and synchronizer assumptions are satisfied.

9. For **Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs**, start with the FE Electrical and Computer specification/Handbook location recorded in the ledger, then use the chapter's reconciled source set for sequential logic, state machines, and timing (HARRIS) when the concept is split-required. That preserves the Handbook-versus-learned-material boundary.

10. Use this limiting check: check the slowest path against setup time and the fastest path against hold time. The simplified case should produce the expected physical, timing, logic, protocol, or complexity behavior before the full solution is trusted.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 15.

- **flip-flop state transition:** SR, JK, and D flip-flops
- **shift register:** Registers, shift registers, and data movement
- **digital counter:** Synchronous and asynchronous counters
- **finite state machine:** Finite-state-machine representation and design
- **programmable logic device:** Programmable logic devices and gate arrays
- **sequential timing constraint:** Setup, hold, clock-to-Q, and timing margin
- **metastability:** Asynchronous inputs, metastability, races, and hazards

---

## What's Next

**Chapter 03-44: Computer Systems — Microprocessors, Memory, and Interfacing**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
