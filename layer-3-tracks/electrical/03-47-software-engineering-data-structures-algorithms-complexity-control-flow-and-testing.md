---
chapter: "03-47"
title: "Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-047-01, ECE-3-047-02, ECE-3-047-03, ECE-3-047-04, ECE-3-047-05, ECE-3-047-06, ECE-3-047-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-47: Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** MATH-1C-027-07 · ECE-3-044-07

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **47.1** Explain and apply **Algorithm specification, correctness, and pseudocode**.
* **47.2** Explain and apply **Arrays, lists, stacks, queues, maps, sets, graphs, and trees**.
* **47.3** Explain and apply **Searching and sorting algorithms**.
* **47.4** Explain and apply **Big-O time complexity**.
* **47.5** Explain and apply **Iteration, conditionals, recursion, and control flow**.
* **47.6** Explain and apply **Graph and tree traversal**.
* **47.7** Explain and apply **Static, dynamic, black-box, and white-box testing**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 47.1 Algorithm specification, correctness, and pseudocode

An algorithm is a precise sequence of steps. Correctness requires that it produce the specified result for valid inputs and handle defined edge/failure cases.

\[\text{input}\rightarrow\text{finite steps}\rightarrow\text{output}\]

![FIG-03-47-001: Pseudocode and flowchart for a simple algorithm with input, decision, loop, and output.](../figures/FIG-03-47-001-algorithm-specification-correctness-and-pseudocode.png)

### Worked Example 1

**Problem.** A sorting algorithm is correct only if its output is ordered and contains exactly the input elements.

**Solution.** Use the relation and model in §47.1, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 47.2 Arrays, lists, stacks, queues, maps, sets, graphs, and trees

Data structures organize data for particular access patterns. Arrays support indexed access; linked lists support link-based insertion; stacks and queues impose order; maps and sets organize keys; graphs and trees represent relationships.

\[\text{choose structure to match access/update operations}\]

![FIG-03-47-002: Array, linked list, stack, queue, map, set, graph, and tree sketches with representative operations.](../figures/FIG-03-47-002-arrays-lists-stacks-queues-maps-sets-graphs-and-trees.png)

### Worked Example 2

**Problem.** Breadth-first search naturally uses a queue; depth-first search can use a stack.

**Solution.** Use the relation and model in §47.2, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 47.3 Searching and sorting algorithms

Algorithm choice depends on data organization, size, update patterns, and required performance. The Handbook names bubble, insertion, merge, heap, quick sort, binary search, and hashing.

\[\text{binary search requires sorted data}\]

![FIG-03-47-003: Conceptual comparison of bubble, merge, quick sort, binary search, and hash lookup.](../figures/FIG-03-47-003-searching-and-sorting-algorithms.png)

### Worked Example 3

**Problem.** Binary search repeatedly discards half of a sorted search interval.

**Solution.** Use the relation and model in §47.3, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 47.4 Big-O time complexity

Big-O describes growth rate as problem size increases, ignoring constant factors and lower-order terms. It is useful for comparing scalability rather than predicting exact runtime.

\[O(1),\ O(\log n),\ O(n),\ O(n\log n),\ O(n^2)\]

![FIG-03-47-004: Growth curves for common Big-O classes versus input size n.](../figures/FIG-03-47-004-big-o-time-complexity.png)

### Worked Example 4

**Problem.** Binary search is O(log n) average/worst on a sorted array, while a simple full scan is O(n).

**Solution.** Use the relation and model in §47.4, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 47.5 Iteration, conditionals, recursion, and control flow

Software implementation is built from control-flow structures that determine execution order. Recursion requires a terminating base case.

\[\text{sequence}+\text{selection}+\text{iteration/recursion}\]

![FIG-03-47-005: Flowchart showing sequence, if/else, loop, function call, and recursive call with base case.](../figures/FIG-03-47-005-iteration-conditionals-recursion-and-control-flow.png)

### Worked Example 5

**Problem.** A loop with no reachable termination condition can run indefinitely.

**Solution.** Use the relation and model in §47.5, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 47.6 Graph and tree traversal

Breadth-first search explores neighbors by layers; depth-first search follows a branch before backtracking. Tree traversal order changes where the root is visited relative to subtrees.

\[\text{BFS}\leftrightarrow\text{queue},\qquad \text{DFS}\leftrightarrow\text{stack/recursion}\]

![FIG-03-47-006: Graph with BFS/DFS visitation orders and binary tree with inorder/preorder/postorder paths.](../figures/FIG-03-47-006-graph-and-tree-traversal.png)

### Worked Example 6

**Problem.** In-order traversal of a binary search tree visits keys in sorted order under standard BST assumptions.

**Solution.** Use the relation and model in §47.6, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

---

## 47.7 Static, dynamic, black-box, and white-box testing

Static testing examines artifacts without executing code; dynamic testing executes software. Black-box testing focuses on externally visible behavior; white-box testing uses internal structure.

\[\text{test evidence}\rightarrow\text{confidence, not proof of absence of defects}\]

![FIG-03-47-007: Two-axis software-testing matrix showing static/dynamic and black-box/white-box approaches with examples.](../figures/FIG-03-47-007-static-dynamic-black-box-and-white-box-testing.png)

### Worked Example 7

**Problem.** A code review is static testing; a unit test that executes a function is dynamic testing.

**Solution.** Use the relation and model in §47.7, then verify the operating region, units, polarity, timing, or logic assumptions that apply.

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

Primary source basis: **FE Electrical and Computer specification Area 17; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** The FE Electrical and Computer specification includes both directly tabulated Handbook material and learned engineering/computing concepts. The chapter does not assign false Handbook pages to material that the specification requires but the Handbook does not directly develop.

---

## Where This Goes Wrong

**Using algorithm outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using data structure outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using search and sort algorithm outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using algorithm complexity outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using software control flow outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using graph traversal outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using software testing outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| algorithm | Concept developed in §47.1; apply with that section's stated model and conventions. |
| data structure | Concept developed in §47.2; apply with that section's stated model and conventions. |
| search and sort algorithm | Concept developed in §47.3; apply with that section's stated model and conventions. |
| algorithm complexity | Concept developed in §47.4; apply with that section's stated model and conventions. |
| software control flow | Concept developed in §47.5; apply with that section's stated model and conventions. |
| graph traversal | Concept developed in §47.6; apply with that section's stated model and conventions. |
| software testing | Concept developed in §47.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **algorithm** and identify the governing relation, state variable, or decision it organizes.

2. Define **data structure** and identify the governing relation, state variable, or decision it organizes.

3. Define **search and sort algorithm** and identify the governing relation, state variable, or decision it organizes.

4. Define **algorithm complexity** and identify the governing relation, state variable, or decision it organizes.

5. Define **software control flow** and identify the governing relation, state variable, or decision it organizes.

6. Define **graph traversal** and identify the governing relation, state variable, or decision it organizes.

7. Define **software testing** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **algorithm**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **data structure**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **search and sort algorithm**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **algorithm complexity**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **software control flow**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **graph traversal**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **software testing**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **algorithm**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **data structure**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **search and sort algorithm**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **algorithm complexity**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **software control flow**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **graph traversal**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **software testing**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **algorithm**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **data structure**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **algorithm** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **data structure** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **search and sort algorithm** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **algorithm complexity** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **software control flow** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **graph traversal** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **software testing** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **algorithm**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **data structure**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **search and sort algorithm**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **algorithm complexity**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **software control flow**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **graph traversal**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **software testing**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

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

1. A sorting algorithm is correct only if its output is ordered and contains exactly the input elements.

2. Breadth-first search naturally uses a queue; depth-first search can use a stack.

3. Binary search repeatedly discards half of a sorted search interval.

4. Binary search is O(log n) average/worst on a sorted array, while a simple full scan is O(n).

5. A loop with no reachable termination condition can run indefinitely.

6. In-order traversal of a binary search tree visits keys in sorted order under standard BST assumptions.

7. A code review is static testing; a unit test that executes a function is dynamic testing.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. Use §47.1. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

2. Use §47.2. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

3. Use §47.3. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

4. Use §47.4. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

5. Use §47.5. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

6. Use §47.6. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

7. Use §47.7. The stated result follows from the displayed relation or state definition; verify that the model assumptions remain satisfied.

8. Check device operating region, saturation/clipping, frequency range, RMS-versus-peak convention, timing constraints, address/bit width, or protocol/software preconditions as applicable.

9. Start with FE Electrical and Computer specification Area 17, then use the Handbook subsection named in the ledger for the specific concept.

10. Test a simple limiting case: zero input, matched load, very low/high frequency, all-zero/all-one logic, minimum/maximum address, or small input size as appropriate. The result should reduce to a physically or logically sensible form.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 17.

- **algorithm:** Algorithm specification, correctness, and pseudocode
- **data structure:** Arrays, lists, stacks, queues, maps, sets, graphs, and trees
- **search and sort algorithm:** Searching and sorting algorithms
- **algorithm complexity:** Big-O time complexity
- **software control flow:** Iteration, conditionals, recursion, and control flow
- **graph traversal:** Graph and tree traversal
- **software testing:** Static, dynamic, black-box, and white-box testing

---

## What's Next

**Environmental Engineering begins at 03-48**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
