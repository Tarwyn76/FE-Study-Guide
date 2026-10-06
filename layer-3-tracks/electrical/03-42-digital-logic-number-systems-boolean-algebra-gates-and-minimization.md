---
chapter: "03-42"
title: "Digital Logic — Number Systems, Boolean Algebra, Gates, and Minimization"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-042-01, ECE-3-042-02, ECE-3-042-03, ECE-3-042-04, ECE-3-042-05, ECE-3-042-06, ECE-3-042-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-42: Digital Logic — Number Systems, Boolean Algebra, Gates, and Minimization

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** MATH-1C-027-04

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Digital Logic — Number Systems, Boolean Algebra, Gates, and Minimization**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **42.1** Explain and apply **Binary, hexadecimal, signed numbers, and two's complement**.
* **42.2** Explain and apply **Boolean operations and truth tables**.
* **42.3** Explain and apply **De Morgan laws, NAND, and NOR universality**.
* **42.4** Explain and apply **Canonical SOP/POS, minterms, and maxterms**.
* **42.5** Explain and apply **Karnaugh maps and logic minimization**.
* **42.6** Explain and apply **Combinational circuits — adders, multiplexers, decoders**.
* **42.7** Explain and apply **Propagation delay, hazards, and combinational timing**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 42.1 Binary, hexadecimal, signed numbers, and two's complement

Digital systems use positional number systems and finite-width signed representations. Two's complement makes addition/subtraction hardware simple but imposes a fixed representable range.

\[\text{two's complement}(M)=2^N-M\]

![FIG-03-42-001: Binary, decimal, hexadecimal, and two's-complement conversions with bit weights.](../figures/FIG-03-42-001-binary-hexadecimal-signed-numbers-and-two-s-complement.png)

### Worked Example 1

**Problem.** For 8-bit two's complement, -1 is 11111111.

**Solution.** Use the relation and model in §42.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 42.2 Boolean operations and truth tables

Boolean variables take two logic values. Truth tables define the exact function independent of how the circuit is implemented.

\[C=A\cdot B,\qquad C=A+B,\qquad C=A\oplus B\]

![FIG-03-42-002: AND, OR, XOR, and NOT gates with symbols and truth tables.](../figures/FIG-03-42-002-boolean-operations-and-truth-tables.png)

### Worked Example 2

**Problem.** XOR is 1 when its two inputs differ.

**Solution.** Use the relation and model in §42.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 42.3 De Morgan laws, NAND, and NOR universality

De Morgan's theorems move inversions across AND/OR operations and underpin NAND/NOR implementations. Track bubbles carefully when transforming logic.

\[\overline{AB}=\bar A+\bar B,\qquad \overline{A+B}=\bar A\bar B\]

![FIG-03-42-003: Equivalent gate networks illustrating De Morgan transformations and NAND/NOR realization.](../figures/FIG-03-42-003-de-morgan-laws-nand-and-nor-universality.png)

### Worked Example 3

**Problem.** The complement of A+B is A-bar times B-bar.

**Solution.** Use the relation and model in §42.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 42.4 Canonical SOP/POS, minterms, and maxterms

Canonical forms provide a systematic bridge between truth tables and Boolean expressions. Each minterm corresponds to one input combination where a function is 1.

\[F=\sum m(\cdots),\qquad G=\prod M(\cdots)\]

![FIG-03-42-004: Truth table linked to minterm numbers and canonical SOP expression.](../figures/FIG-03-42-004-canonical-sop-pos-minterms-and-maxterms.png)

### Worked Example 4

**Problem.** A three-variable truth table has eight possible minterms.

**Solution.** Use the relation and model in §42.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 42.5 Karnaugh maps and logic minimization

K-maps simplify logic by combining adjacent minterms that differ in only one variable. Larger valid groups eliminate more literals.

\[\text{group adjacent 1s in powers of two}\]

![FIG-03-42-005: Four-variable Karnaugh map with 1-, 2-, 4-, and 8-cell group examples.](../figures/FIG-03-42-005-karnaugh-maps-and-logic-minimization.png)

### Worked Example 5

**Problem.** A group of four adjacent cells eliminates two variables from a four-variable minterm expression.

**Solution.** Use the relation and model in §42.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 42.6 Combinational circuits — adders, multiplexers, decoders

Combinational outputs depend only on present inputs. Common structures such as adders, multiplexers, encoders, and decoders are built from Boolean functions.

\[\mathbf y=f(\mathbf x)\]

![FIG-03-42-006: Half/full adder, multiplexer, decoder, and encoder block diagrams with truth-table snippets.](../figures/FIG-03-42-006-combinational-circuits-adders-multiplexers-decoders.png)

### Worked Example 6

**Problem.** A 2-to-1 multiplexer selects one of two data inputs using one select bit.

**Solution.** Use the relation and model in §42.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 42.7 Propagation delay, hazards, and combinational timing

Real gates do not switch instantaneously. Unequal path delays can produce glitches even when the final Boolean value is correct.

\[t_{pd,\text{path}}\approx\sum t_{pd,\text{gates}}\]

![FIG-03-42-007: Logic network with two reconvergent paths and timing diagram showing a static hazard glitch.](../figures/FIG-03-42-007-propagation-delay-hazards-and-combinational-timing.png)

### Worked Example 7

**Problem.** Two paths with different gate counts can create a transient hazard during an input transition.

**Solution.** Use the relation and model in §42.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

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

Primary source basis: **FE Electrical and Computer specification Area 15; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using binary number representation outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Boolean logic outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using De Morgan transformation outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using canonical switching form outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Karnaugh map minimization outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using combinational logic circuit outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using logic propagation delay outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| binary number representation | Concept developed in §42.1; apply with that section's stated model and conventions. |
| Boolean logic | Concept developed in §42.2; apply with that section's stated model and conventions. |
| De Morgan transformation | Concept developed in §42.3; apply with that section's stated model and conventions. |
| canonical switching form | Concept developed in §42.4; apply with that section's stated model and conventions. |
| Karnaugh map minimization | Concept developed in §42.5; apply with that section's stated model and conventions. |
| combinational logic circuit | Concept developed in §42.6; apply with that section's stated model and conventions. |
| logic propagation delay | Concept developed in §42.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **binary number representation** and identify the governing relation, state variable, or decision it organizes.

2. Define **Boolean logic** and identify the governing relation, state variable, or decision it organizes.

3. Define **De Morgan transformation** and identify the governing relation, state variable, or decision it organizes.

4. Define **canonical switching form** and identify the governing relation, state variable, or decision it organizes.

5. Define **Karnaugh map minimization** and identify the governing relation, state variable, or decision it organizes.

6. Define **combinational logic circuit** and identify the governing relation, state variable, or decision it organizes.

7. Define **logic propagation delay** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **binary number representation**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **Boolean logic**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **De Morgan transformation**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **canonical switching form**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **Karnaugh map minimization**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **combinational logic circuit**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **logic propagation delay**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **binary number representation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **Boolean logic**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **De Morgan transformation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **canonical switching form**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **Karnaugh map minimization**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **combinational logic circuit**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **logic propagation delay**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **binary number representation**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **Boolean logic**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **binary number representation** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **Boolean logic** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **De Morgan transformation** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **canonical switching form** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **Karnaugh map minimization** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **combinational logic circuit** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **logic propagation delay** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **binary number representation**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **Boolean logic**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **De Morgan transformation**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **canonical switching form**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **Karnaugh map minimization**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **combinational logic circuit**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **logic propagation delay**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

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

1. For 8-bit two's complement, -1 is 11111111.

2. XOR is 1 when its two inputs differ.

3. The complement of A+B is A-bar times B-bar.

4. A three-variable truth table has eight possible minterms.

5. A group of four adjacent cells eliminates two variables from a four-variable minterm expression.

6. A 2-to-1 multiplexer selects one of two data inputs using one select bit.

7. Two paths with different gate counts can create a transient hazard during an input transition.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §42.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §42.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §42.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §42.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §42.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §42.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §42.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 15, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 15.

- **binary number representation:** Binary, hexadecimal, signed numbers, and two's complement
- **Boolean logic:** Boolean operations and truth tables
- **De Morgan transformation:** De Morgan laws, NAND, and NOR universality
- **canonical switching form:** Canonical SOP/POS, minterms, and maxterms
- **Karnaugh map minimization:** Karnaugh maps and logic minimization
- **combinational logic circuit:** Combinational circuits — adders, multiplexers, decoders
- **logic propagation delay:** Propagation delay, hazards, and combinational timing

---

## What's Next

**Chapter 03-43: Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
