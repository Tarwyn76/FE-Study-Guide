---
chapter: "03-44"
title: "Computer Systems — Microprocessors, Memory, and Interfacing"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-044-01, ECE-3-044-02, ECE-3-044-03, ECE-3-044-04, ECE-3-044-05, ECE-3-044-06, ECE-3-044-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-44: Computer Systems — Microprocessors, Memory, and Interfacing

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ECE-3-043-07 · MATH-1C-027-01

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Computer Systems — Microprocessors, Memory, and Interfacing**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **44.1** Explain and apply **Processor datapath, control, and instruction execution**.
* **44.2** Explain and apply **Harvard and von Neumann organization**.
* **44.3** Explain and apply **RAM, ROM, cache, and storage hierarchy**.
* **44.4** Explain and apply **Cache size, associativity, and address fields**.
* **44.5** Explain and apply **Cache replacement and write policies**.
* **44.6** Explain and apply **Memory-mapped I/O, buses, and peripheral interfacing**.
* **44.7** Explain and apply **Multicore, threading, and concurrency concepts**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 44.1 Processor datapath, control, and instruction execution

A processor combines datapath resources with control logic to execute instructions. Architectural details vary, but instruction flow, registers, ALU operations, and memory access remain core concepts.

\[\text{fetch}\rightarrow\text{decode}\rightarrow\text{execute}\rightarrow\text{memory/writeback}\]

![FIG-03-44-001: Simplified CPU datapath with program counter, instruction memory, register file, ALU, data memory, and control signals.](../figures/FIG-03-44-001-processor-datapath-control-and-instruction-execution.png)

### Worked Example 1

**Problem.** An arithmetic instruction typically reads operands, executes in the ALU, and writes a result.

**Solution.** Use the relation and model in §44.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 44.2 Harvard and von Neumann organization

Harvard architecture separates instruction and data memories/paths, while von Neumann organization shares a memory space/path conceptually. Many real processors blend these ideas.

\[\text{instruction memory path}\neq\text{data memory path}\]

![FIG-03-44-002: Harvard and von Neumann architecture block diagrams shown side by side.](../figures/FIG-03-44-002-harvard-and-von-neumann-organization.png)

### Worked Example 2

**Problem.** Separate instruction and data paths can permit concurrent instruction fetch and data access.

**Solution.** Use the relation and model in §44.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 44.3 RAM, ROM, cache, and storage hierarchy

Memory hierarchy trades capacity, latency, cost, and volatility. Cache reduces average access time by exploiting locality.

\[\text{speed}\uparrow\ \text{usually as capacity}\downarrow\text{ near the CPU}\]

![FIG-03-44-003: Memory hierarchy pyramid from registers and caches through RAM and nonvolatile storage.](../figures/FIG-03-44-003-ram-rom-cache-and-storage-hierarchy.png)

### Worked Example 3

**Problem.** L1 cache is typically smaller and faster than main memory.

**Solution.** Use the relation and model in §44.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 44.4 Cache size, associativity, and address fields

Cache addresses divide into tag, index, and block-offset fields. Associativity changes how many candidate lines can hold a block for a given set.

\[C=SAB,\quad b_{\text{offset}}=\log_2 B,\quad b_{\text{index}}=\log_2 S\]

![FIG-03-44-004: CPU address split into tag/index/offset plus direct-mapped and set-associative cache examples.](../figures/FIG-03-44-004-cache-size-associativity-and-address-fields.png)

### Worked Example 4

**Problem.** A 64-byte block requires 6 block-offset bits.

**Solution.** Use the relation and model in §44.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 44.5 Cache replacement and write policies

Replacement policies such as LRU and FIFO choose victims; write-through and write-back determine when main memory is updated.

\[\text{miss}+\text{full candidate set}\rightarrow\text{replacement policy}\]

![FIG-03-44-005: Cache hit/miss flow showing replacement and write-through/write-back decisions.](../figures/FIG-03-44-005-cache-replacement-and-write-policies.png)

### Worked Example 5

**Problem.** A dirty line in a write-back cache must be written to memory before eviction.

**Solution.** Use the relation and model in §44.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 44.6 Memory-mapped I/O, buses, and peripheral interfacing

Interfacing connects processors to sensors, converters, storage, and communications peripherals. Addressing, timing, signal levels, and protocol behavior must all match.

\[\text{processor bus}\leftrightarrow\text{address/data/control}\leftrightarrow\text{peripheral}\]

![FIG-03-44-006: Microprocessor connected to memory, GPIO, ADC, timer, and serial peripheral through address/data/control buses.](../figures/FIG-03-44-006-memory-mapped-i-o-buses-and-peripheral-interfacing.png)

### Worked Example 6

**Problem.** A memory-mapped peripheral register is accessed using address-space operations defined by the processor architecture.

**Solution.** Use the relation and model in §44.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 44.7 Multicore, threading, and concurrency concepts

Multiple cores can execute instructions concurrently, while software threads share process resources according to the operating system and runtime model. Shared caches and synchronization affect performance.

\[\text{parallel speedup limited by serial work and shared-resource effects}\]

![FIG-03-44-007: Dual-core processor with private L1 caches, shared L2 cache, memory interface, and software threads mapped to cores.](../figures/FIG-03-44-007-multicore-threading-and-concurrency-concepts.png)

### Worked Example 7

**Problem.** Two cores do not automatically halve runtime for a program that cannot execute its work in parallel.

**Solution.** Use the relation and model in §44.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

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

Primary source basis: **FE Electrical and Computer specification Area 16; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using microprocessor datapath outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Harvard architecture outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using memory hierarchy outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using cache organization outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using cache policy outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using computer interfacing outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using multicore processing outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| microprocessor datapath | Concept developed in §44.1; apply with that section's stated model and conventions. |
| Harvard architecture | Concept developed in §44.2; apply with that section's stated model and conventions. |
| memory hierarchy | Concept developed in §44.3; apply with that section's stated model and conventions. |
| cache organization | Concept developed in §44.4; apply with that section's stated model and conventions. |
| cache policy | Concept developed in §44.5; apply with that section's stated model and conventions. |
| computer interfacing | Concept developed in §44.6; apply with that section's stated model and conventions. |
| multicore processing | Concept developed in §44.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **microprocessor datapath** and identify the governing relation, state variable, or decision it organizes.

2. Define **Harvard architecture** and identify the governing relation, state variable, or decision it organizes.

3. Define **memory hierarchy** and identify the governing relation, state variable, or decision it organizes.

4. Define **cache organization** and identify the governing relation, state variable, or decision it organizes.

5. Define **cache policy** and identify the governing relation, state variable, or decision it organizes.

6. Define **computer interfacing** and identify the governing relation, state variable, or decision it organizes.

7. Define **multicore processing** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **microprocessor datapath**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **Harvard architecture**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **memory hierarchy**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **cache organization**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **cache policy**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **computer interfacing**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **multicore processing**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **microprocessor datapath**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **Harvard architecture**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **memory hierarchy**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **cache organization**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **cache policy**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **computer interfacing**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **multicore processing**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **microprocessor datapath**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **Harvard architecture**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **microprocessor datapath** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **Harvard architecture** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **memory hierarchy** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **cache organization** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **cache policy** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **computer interfacing** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **multicore processing** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **microprocessor datapath**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **Harvard architecture**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **memory hierarchy**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **cache organization**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **cache policy**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **computer interfacing**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **multicore processing**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

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

1. An arithmetic instruction typically reads operands, executes in the ALU, and writes a result.

2. Separate instruction and data paths can permit concurrent instruction fetch and data access.

3. L1 cache is typically smaller and faster than main memory.

4. A 64-byte block requires 6 block-offset bits.

5. A dirty line in a write-back cache must be written to memory before eviction.

6. A memory-mapped peripheral register is accessed using address-space operations defined by the processor architecture.

7. Two cores do not automatically halve runtime for a program that cannot execute its work in parallel.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §44.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §44.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §44.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §44.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §44.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §44.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §44.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 16, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 16.

- **microprocessor datapath:** Processor datapath, control, and instruction execution
- **Harvard architecture:** Harvard and von Neumann organization
- **memory hierarchy:** RAM, ROM, cache, and storage hierarchy
- **cache organization:** Cache size, associativity, and address fields
- **cache policy:** Cache replacement and write policies
- **computer interfacing:** Memory-mapped I/O, buses, and peripheral interfacing
- **multicore processing:** Multicore, threading, and concurrency concepts

---

## What's Next

**Chapter 03-45: Computer Networks — Routing, Switching, Topologies, and TCP/IP**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
