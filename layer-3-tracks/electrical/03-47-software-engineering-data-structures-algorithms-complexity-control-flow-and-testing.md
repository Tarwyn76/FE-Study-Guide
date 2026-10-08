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

**Solution.** Start from the §47.1 relation \(\text{input}\rightarrow\text{finite steps}\rightarrow\text{output}\). The statement follows from the physical or logical meaning of **Algorithm specification, correctness, and pseudocode**: A sorting algorithm is correct only if its output is ordered and contains exactly the input elements. Accept that conclusion only while the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

---

## 47.2 Arrays, lists, stacks, queues, maps, sets, graphs, and trees

Data structures organize data for particular access patterns. Arrays support indexed access; linked lists support link-based insertion; stacks and queues impose order; maps and sets organize keys; graphs and trees represent relationships.

\[\text{choose structure to match access/update operations}\]

![FIG-03-47-002: Array, linked list, stack, queue, map, set, graph, and tree sketches with representative operations.](../figures/FIG-03-47-002-arrays-lists-stacks-queues-maps-sets-graphs-and-trees.png)

### Worked Example 2

**Problem.** Breadth-first search naturally uses a queue; depth-first search can use a stack.

**Solution.** Start from the §47.2 relation \(\text{choose structure to match access/update operations}\). The statement follows from the physical or logical meaning of **Arrays, lists, stacks, queues, maps, sets, graphs, and trees**: Breadth-first search naturally uses a queue; depth-first search can use a stack. Accept that conclusion only while the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

---

## 47.3 Searching and sorting algorithms

Algorithm choice depends on data organization, size, update patterns, and required performance. The Handbook names bubble, insertion, merge, heap, quick sort, binary search, and hashing.

\[\text{binary search requires sorted data}\]

![FIG-03-47-003: Conceptual comparison of bubble, merge, quick sort, binary search, and hash lookup.](../figures/FIG-03-47-003-searching-and-sorting-algorithms.png)

### Worked Example 3

**Problem.** Binary search repeatedly discards half of a sorted search interval.

**Solution.** Start from the §47.3 relation \(\text{binary search requires sorted data}\). The statement follows from the physical or logical meaning of **Searching and sorting algorithms**: Binary search repeatedly discards half of a sorted search interval. Accept that conclusion only while the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

---

## 47.4 Big-O time complexity

Big-O describes growth rate as problem size increases, ignoring constant factors and lower-order terms. It is useful for comparing scalability rather than predicting exact runtime.

\[O(1),\ O(\log n),\ O(n),\ O(n\log n),\ O(n^2)\]

![FIG-03-47-004: Growth curves for common Big-O classes versus input size n.](../figures/FIG-03-47-004-big-o-time-complexity.png)

### Worked Example 4

**Problem.** Binary search is O(log n) average/worst on a sorted array, while a simple full scan is O(n).

**Solution.** Start from the §47.4 relation \(O(1),\ O(\log n),\ O(n),\ O(n\log n),\ O(n^2)\). The statement follows from the physical or logical meaning of **Big-O time complexity**: Binary search is O(log n) average/worst on a sorted array, while a simple full scan is O(n). Accept that conclusion only while the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

---

## 47.5 Iteration, conditionals, recursion, and control flow

Software implementation is built from control-flow structures that determine execution order. Recursion requires a terminating base case.

\[\text{sequence}+\text{selection}+\text{iteration/recursion}\]

![FIG-03-47-005: Flowchart showing sequence, if/else, loop, function call, and recursive call with base case.](../figures/FIG-03-47-005-iteration-conditionals-recursion-and-control-flow.png)

### Worked Example 5

**Problem.** A loop with no reachable termination condition can run indefinitely.

**Solution.** Start from the §47.5 relation \(\text{sequence}+\text{selection}+\text{iteration/recursion}\). The statement follows from the physical or logical meaning of **Iteration, conditionals, recursion, and control flow**: A loop with no reachable termination condition can run indefinitely. Accept that conclusion only while the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

---

## 47.6 Graph and tree traversal

Breadth-first search explores neighbors by layers; depth-first search follows a branch before backtracking. Tree traversal order changes where the root is visited relative to subtrees.

\[\text{BFS}\leftrightarrow\text{queue},\qquad \text{DFS}\leftrightarrow\text{stack/recursion}\]

![FIG-03-47-006: Graph with BFS/DFS visitation orders and binary tree with inorder/preorder/postorder paths.](../figures/FIG-03-47-006-graph-and-tree-traversal.png)

### Worked Example 6

**Problem.** In-order traversal of a binary search tree visits keys in sorted order under standard BST assumptions.

**Solution.** Start from the §47.6 relation \(\text{BFS}\leftrightarrow\text{queue},\qquad \text{DFS}\leftrightarrow\text{stack/recursion}\). The statement follows from the physical or logical meaning of **Graph and tree traversal**: In-order traversal of a binary search tree visits keys in sorted order under standard BST assumptions. Accept that conclusion only while the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

---

## 47.7 Static, dynamic, black-box, and white-box testing

Static testing examines artifacts without executing code; dynamic testing executes software. Black-box testing focuses on externally visible behavior; white-box testing uses internal structure.

\[\text{test evidence}\rightarrow\text{confidence, not proof of absence of defects}\]

![FIG-03-47-007: Two-axis software-testing matrix showing static/dynamic and black-box/white-box approaches with examples.](../figures/FIG-03-47-007-static-dynamic-black-box-and-white-box-testing.png)

### Worked Example 7

**Problem.** A code review is static testing; a unit test that executes a function is dynamic testing.

**Solution.** Start from the §47.7 relation \(\text{test evidence}\rightarrow\text{confidence, not proof of absence of defects}\). The statement follows from the physical or logical meaning of **Static, dynamic, black-box, and white-box testing**: A code review is static testing; a unit test that executes a function is dynamic testing. Accept that conclusion only while the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation gives a numerical answer but violates the assumed device region, logic state, or protocol condition. Is the answer valid?

**Solution.** No. In **Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing**, a tidy numerical or logical result is still invalid if it contradicts the model assumptions. A representative failure is binary search applied to unsorted data, an algorithm claimed correct without its invariant, or a test result treated as proof of defect absence. Return to the applicable section, choose the state/model consistent with the solved quantities, recompute if needed, and confirm that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

### Worked Example 9

**Problem.** A remembered formula differs from the expression printed in the FE Reference Handbook. Which should govern an exam solution?

**Solution.** Use the FE Reference Handbook expression and its definitions as the controlling exam reference unless the problem explicitly defines another model. For **Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing**, match symbols, units, reference directions, RMS/peak or digital conventions, and assumptions to the Handbook first. External references support only specification-required learned concepts that the Handbook does not directly develop.

---

## As the Handbook States It

Primary source basis: **FE Electrical and Computer specification Area 17; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required engineering/computing knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those two bodies of material into exam-oriented explanations and examples; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. ISBN 978-0-262-04630-5. Supporting scope: Algorithms, asymptotic complexity, searching, sorting, data structures, trees, and graph algorithms.
- ISO/IEC/IEEE. (2022). *Software and systems engineering—Software testing—Part 1: General concepts* (ISO/IEC/IEEE 29119-1:2022). Supporting scope: General concepts and terminology for software testing.

The external references support only the learned/application portion of the specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing, the same equation or symbol can change meaning when the operating state, abstraction, timing model, or signal convention changes; verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

16. The FE Reference Handbook is the exam reference for Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing. Match its variable definitions and conventions before substitution; external references support only learned material not developed in the Handbook.

17. An algebraically consistent answer can still be invalid in Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing. Reject a result that implies binary search applied to unsorted data, an algorithm claimed correct without its invariant, or a test result treated as proof of defect absence and reselect the appropriate model or state.

18. A useful independent check for this chapter is to use n=0, n=1, or an already sorted/minimal input and verify the result and complexity interpretation remain sensible. If the result does not reduce correctly, recheck the model, sign convention, and arithmetic.

19. **A.** For **Algorithm specification, correctness, and pseudocode**, the governing section model is \(\text{input}\rightarrow\text{finite steps}\rightarrow\text{output}\). Apply it only with the definitions and assumptions stated in §47.1, then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

20. **A.** For **Arrays, lists, stacks, queues, maps, sets, graphs, and trees**, the governing section model is \(\text{choose structure to match access/update operations}\). Apply it only with the definitions and assumptions stated in §47.2, then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

21. **A.** For **Searching and sorting algorithms**, the governing section model is \(\text{binary search requires sorted data}\). Apply it only with the definitions and assumptions stated in §47.3, then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

22. **A.** For **Big-O time complexity**, the governing section model is \(O(1),\ O(\log n),\ O(n),\ O(n\log n),\ O(n^2)\). Apply it only with the definitions and assumptions stated in §47.4, then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

23. **A.** For **Iteration, conditionals, recursion, and control flow**, the governing section model is \(\text{sequence}+\text{selection}+\text{iteration/recursion}\). Apply it only with the definitions and assumptions stated in §47.5, then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

24. **A.** For **Graph and tree traversal**, the governing section model is \(\text{BFS}\leftrightarrow\text{queue},\qquad \text{DFS}\leftrightarrow\text{stack/recursion}\). Apply it only with the definitions and assumptions stated in §47.6, then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

25. **A.** For **Static, dynamic, black-box, and white-box testing**, the governing section model is \(\text{test evidence}\rightarrow\text{confidence, not proof of absence of defects}\). Apply it only with the definitions and assumptions stated in §47.7, then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

26. **A.** For an integrated Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing problem, separate the physical/logical model from the arithmetic, solve with the relevant section relations, and cross-check the result against the chapter-specific validity conditions.

27. **A.** In **Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing**, the source boundary is explicit: FE-Handbook-supported material remains tied to the ledger, externally supported material uses the chapter references for algorithms, data structures, complexity, and software testing (CLRS / ISO29119), and guide synthesis is identified as supplemental explanation rather than Handbook text.


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

1. **Independent check for §47.1.** Begin independently with \(\text{input}\rightarrow\text{finite steps}\rightarrow\text{output}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A sorting algorithm is correct only if its output is ordered and contains exactly the input elements. Then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

2. **Independent check for §47.2.** Begin independently with \(\text{choose structure to match access/update operations}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Breadth-first search naturally uses a queue; depth-first search can use a stack. Then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

3. **Independent check for §47.3.** Begin independently with \(\text{binary search requires sorted data}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Binary search repeatedly discards half of a sorted search interval. Then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

4. **Independent check for §47.4.** Begin independently with \(O(1),\ O(\log n),\ O(n),\ O(n\log n),\ O(n^2)\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Binary search is O(log n) average/worst on a sorted array, while a simple full scan is O(n). Then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

5. **Independent check for §47.5.** Begin independently with \(\text{sequence}+\text{selection}+\text{iteration/recursion}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A loop with no reachable termination condition can run indefinitely. Then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

6. **Independent check for §47.6.** Begin independently with \(\text{BFS}\leftrightarrow\text{queue},\qquad \text{DFS}\leftrightarrow\text{stack/recursion}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: In-order traversal of a binary search tree visits keys in sorted order under standard BST assumptions. Then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

7. **Independent check for §47.7.** Begin independently with \(\text{test evidence}\rightarrow\text{confidence, not proof of absence of defects}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A code review is static testing; a unit test that executes a function is dynamic testing. Then verify that the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

8. Check the chapter-specific failure mode first: binary search applied to unsorted data, an algorithm claimed correct without its invariant, or a test result treated as proof of defect absence. Do not accept the numerical or logical result until the data-structure preconditions, algorithm invariant, complexity model, and testing terminology match the problem.

9. For **Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing**, start with the FE Electrical and Computer specification/Handbook location recorded in the ledger, then use the chapter's reconciled source set for algorithms, data structures, complexity, and software testing (CLRS / ISO29119) when the concept is split-required. That preserves the Handbook-versus-learned-material boundary.

10. Use this limiting check: use n=0, n=1, or an already sorted/minimal input and verify the result and complexity interpretation remain sensible. The simplified case should produce the expected physical, timing, logic, protocol, or complexity behavior before the full solution is trusted.

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
