---
chapter: "02-60"
title: "Kirchhoff's Laws and Resistive Circuit Analysis"
layer: 2
tier: E
template: technical
ledger_ids: [ELEC-2E-060-01, ELEC-2E-060-02, ELEC-2E-060-03, ELEC-2E-060-04, ELEC-2E-060-05, ELEC-2E-060-06, ELEC-2E-060-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-60: Kirchhoff's Laws and Resistive Circuit Analysis

> *"Electrical problems become much easier when references, topology, energy flow, and the correct steady-state or transient model are established before algebra."*

---

## Before You Start

**Prerequisites:** 02-59 Electrical Quantities, Ohm's Law, and DC Power · 01-13 Nodal/Loop/Thevenin/Superposition

**Skip if:** You can identify the governing electrical model, choose correct voltage/current references, use the FE Handbook relation, solve representative FE-level calculations, and verify power, units, and physical behavior.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives resistor series/parallel equivalents, Kirchhoff's voltage and current laws, Thévenin and Norton source equivalents, short/open-circuit definitions, and the DC maximum-power-transfer condition. Nodal/mesh workflows are guide-developed applications of KCL/KVL.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **60.1** Explain and apply **Series and Parallel Resistance**.
* **60.2** Explain and apply **Kirchhoff's Current Law**.
* **60.3** Explain and apply **Kirchhoff's Voltage Law**.
* **60.4** Explain and apply **Voltage and Current Dividers**.
* **60.5** Explain and apply **Nodal Analysis with KCL**.
* **60.6** Explain and apply **Mesh and Loop Analysis with KVL**.
* **60.7** Explain and apply **Thévenin, Norton, and Maximum Power Transfer**.

---

## Notation Used Here

Voltage polarities and current directions are reference choices. RMS quantities are used for AC power unless otherwise stated. Use SI units unless a problem explicitly supplies another system.

---

## 60.1 Series and Parallel Resistance

Series resistors carry the same current and add directly. Parallel resistors share the same voltage and combine through reciprocal conductance addition.

Before reducing a network, verify that components truly share a single series path or the same two nodes. Physical drawing placement alone does not determine topology.

\[R_s=\sum_iR_i,\qquad \frac1{R_p}=\sum_i\frac1{R_i}\]

![FIG-02-60-001: Series and parallel resistor networks with current/voltage constraints and equivalent resistance.](../figures/FIG-02-60-001-series-and-parallel-resistance.png)

### Worked Example 1

**Problem.** Find equivalent resistance of 4 Ω, 6 Ω, and 10 Ω in series.

**Solution.** 20 Ω.

---

## 60.2 Kirchhoff's Current Law

KCL is conservation of charge at a node. With no charge accumulation in the ideal lumped-circuit model, algebraic current sum at a node is zero.

Choose a sign convention once—currents entering positive or currents leaving positive—and maintain it through the equation.

\[\sum I_{\rm in}=\sum I_{\rm out}\qquad\text{or}\qquad\sum_k i_k=0\]

![FIG-02-60-002: Circuit node with several branch currents and a KCL equation using one consistent sign convention.](../figures/FIG-02-60-002-kirchhoff-s-current-law.png)

### Worked Example 2

**Problem.** Find equivalent resistance of 6 Ω and 3 Ω in parallel.

**Solution.** 2 Ω.

---

## 60.3 Kirchhoff's Voltage Law

KVL states that the algebraic sum of voltage rises and drops around a closed loop is zero in the lumped-circuit model.

Traverse the loop in either direction. The sign of each term follows how the traversal crosses the element polarity.

\[\sum V_{\rm rises}=\sum V_{\rm drops}\qquad\text{or}\qquad\sum_k v_k=0\]

![FIG-02-60-003: Single circuit loop with source and resistor drops annotated for a clockwise KVL traversal.](../figures/FIG-02-60-003-kirchhoff-s-voltage-law.png)

### Worked Example 3

**Problem.** At a node, 5 A enters and 2 A plus I leave. Find I.

**Solution.** I=3 A.

---

## 60.4 Voltage and Current Dividers

Divider formulas are shortcuts derived from Ohm's law plus series/parallel structure. A voltage divider applies to series elements carrying the same current; a current divider applies to parallel branches sharing the same voltage.

Do not apply a divider formula after a load changes the topology unless the load is included in the equivalent resistance.

\[V_k=V_T\frac{R_k}{\sum R},\qquad I_k=I_T\frac{G_k}{\sum G}\]

![FIG-02-60-004: Loaded voltage divider and parallel current divider with the topology conditions highlighted.](../figures/FIG-02-60-004-voltage-and-current-dividers.png)

### Worked Example 4

**Problem.** A loop contains a 12 V source and 2 Ω + 4 Ω series resistors. Find current.

**Solution.** I=12/6=2 A.

---

## 60.5 Nodal Analysis with KCL

Nodal analysis chooses a reference node, assigns unknown node voltages, and applies KCL using branch currents written in terms of node-voltage differences.

It is especially efficient when the desired outputs are node voltages and the circuit has many parallel branches.

\[\sum_j\frac{V_k-V_j}{R_{kj}}=I_{\rm injected,k}\]

![FIG-02-60-005: Three-node resistive circuit with reference node and KCL equation at an unknown-voltage node.](../figures/FIG-02-60-005-nodal-analysis-with-kcl.png)

### Worked Example 5

**Problem.** A 12 V divider has 2 kΩ on top and 4 kΩ on bottom. Find unloaded output across 4 kΩ.

**Solution.** Vout=12×4/(2+4)=8 V.

---

## 60.6 Mesh and Loop Analysis with KVL

Mesh analysis assigns loop currents to planar meshes and writes KVL around each mesh. A resistor shared by two meshes carries the difference of the two mesh currents.

This method is guide-developed workflow; the governing law is the Handbook KVL relation.

\[\sum R\,I_{\rm mesh}+\sum R(I_{\rm mesh}-I_{\rm adjacent})=\sum V_{\rm sources}\]

![FIG-02-60-006: Two-mesh circuit with shared resistor and clockwise mesh currents.](../figures/FIG-02-60-006-mesh-and-loop-analysis-with-kvl.png)

### Worked Example 6

**Problem.** Node V is connected to 12 V through 3 kΩ and to ground through 6 kΩ. Find V.

**Solution.** (V-12)/3k + V/6k=0 → V=8 V.

---

## 60.7 Thévenin, Norton, and Maximum Power Transfer

Any linear two-terminal network of sources and resistors can be replaced at its terminals by a Thévenin voltage \(V_{oc}\) in series with \(R_{eq}\), or a Norton current \(I_{sc}\) in parallel with the same \(R_{eq}\).

For a purely resistive DC load, maximum power occurs when \(R_L=R_{Th}\). Maximum power transfer is not maximum efficiency.

\[V_{Th}=V_{oc},\qquad I_N=I_{sc},\qquad R_{Th}=R_N,\qquad R_L=R_{Th}\ \text{for max }P_L\]

![FIG-02-60-007: Original two-terminal network beside Thévenin and Norton equivalents and the maximum-power load condition.](../figures/FIG-02-60-007-th-venin-norton-and-maximum-power-transfer.png)

### Worked Example 7

**Problem.** A Thévenin source has VTh=10 V and RTh=5 Ω. Find load for maximum power and maximum load power.

**Solution.** RL=5 Ω; Pmax=VTh²/(4RTh)=5 W.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Convert a Norton source IN=2 A in parallel with RN=4 Ω to Thévenin form.

**Solution.** VTh=IN RN=8 V; RTh=4 Ω.

### Worked Example 9

**Problem.** Two mesh currents I1 and I2 share a 5 Ω resistor. What voltage drop in mesh-1 direction is attributed to the shared resistor?

**Solution.** 5(I1-I2).

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Electrical and Computer Engineering, printed pp. 363–364**.

**Source boundary:** The Handbook directly gives resistor series/parallel equivalents, Kirchhoff's voltage and current laws, Thévenin and Norton source equivalents, short/open-circuit definitions, and the DC maximum-power-transfer condition. Nodal/mesh workflows are guide-developed applications of KCL/KVL.

---

## Where This Goes Wrong

**Using resistive network reduction without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using Kirchhoff current law without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using Kirchhoff voltage law without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using divider rule without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using nodal circuit analysis without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using mesh circuit analysis without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using Thevenin-Norton equivalence without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Skipping a power or conservation check.** A circuit solution should satisfy KCL/KVL where applicable and should not create unexplained power.


---

## Key Terms

| Term | Working definition |
|---|---|
| resistive network reduction | Concept developed in §60.1; use the section definition and stated conditions. |
| Kirchhoff current law | Concept developed in §60.2; use the section definition and stated conditions. |
| Kirchhoff voltage law | Concept developed in §60.3; use the section definition and stated conditions. |
| divider rule | Concept developed in §60.4; use the section definition and stated conditions. |
| nodal circuit analysis | Concept developed in §60.5; use the section definition and stated conditions. |
| mesh circuit analysis | Concept developed in §60.6; use the section definition and stated conditions. |
| Thevenin-Norton equivalence | Concept developed in §60.7; use the section definition and stated conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **resistive network reduction** and state its governing equation or condition.

2. Define **Kirchhoff current law** and state its governing equation or condition.

3. Define **Kirchhoff voltage law** and state its governing equation or condition.

4. Define **divider rule** and state its governing equation or condition.

5. Define **nodal circuit analysis** and state its governing equation or condition.

6. Define **mesh circuit analysis** and state its governing equation or condition.

7. Define **Thevenin-Norton equivalence** and state its governing equation or condition.

8. What is a common analysis error involving **resistive network reduction**?

9. What is a common analysis error involving **Kirchhoff current law**?

10. What is a common analysis error involving **Kirchhoff voltage law**?

11. What is a common analysis error involving **divider rule**?

12. What is a common analysis error involving **nodal circuit analysis**?

13. What is a common analysis error involving **mesh circuit analysis**?

14. What is a common analysis error involving **Thevenin-Norton equivalence**?

15. Why must voltage polarity and current direction be defined before using signed power?

16. What conservation principle should be used as an independent circuit or machine check?

17. When should a Handbook equation be preferred over a remembered shortcut?

18. Why should RMS and peak values not be mixed in AC power or impedance calculations?

### Multiple Choice

19. Which statement is most accurate for **resistive network reduction**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

20. Which statement is most accurate for **Kirchhoff current law**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

21. Which statement is most accurate for **Kirchhoff voltage law**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

22. Which statement is most accurate for **divider rule**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

23. Which statement is most accurate for **nodal circuit analysis**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

24. Which statement is most accurate for **mesh circuit analysis**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

25. Which statement is most accurate for **Thevenin-Norton equivalence**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

26. Which statement is most accurate for **resistive network reduction**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

27. Which statement is most accurate for **Kirchhoff current law**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **resistive network reduction** is developed in §60.1. Use the displayed relation together with its stated sign convention and assumptions.

2. **Kirchhoff current law** is developed in §60.2. Use the displayed relation together with its stated sign convention and assumptions.

3. **Kirchhoff voltage law** is developed in §60.3. Use the displayed relation together with its stated sign convention and assumptions.

4. **divider rule** is developed in §60.4. Use the displayed relation together with its stated sign convention and assumptions.

5. **nodal circuit analysis** is developed in §60.5. Use the displayed relation together with its stated sign convention and assumptions.

6. **mesh circuit analysis** is developed in §60.6. Use the displayed relation together with its stated sign convention and assumptions.

7. **Thevenin-Norton equivalence** is developed in §60.7. Use the displayed relation together with its stated sign convention and assumptions.

8. Applying **resistive network reduction** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

9. Applying **Kirchhoff current law** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

10. Applying **Kirchhoff voltage law** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

11. Applying **divider rule** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

12. Applying **nodal circuit analysis** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

13. Applying **mesh circuit analysis** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

14. Applying **Thevenin-Norton equivalence** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

15. Because the sign of power depends on the chosen voltage/current references and the passive sign convention.

16. Charge/KCL, energy/power balance, and where applicable KVL should close consistently.

17. Whenever the Handbook supplies the relation or when the shortcut's assumptions are uncertain.

18. They represent different magnitudes; mixing them introduces factors such as √2 and gives incorrect power.

19. **A.** The chapter treats **resistive network reduction** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

20. **A.** The chapter treats **Kirchhoff current law** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

21. **A.** The chapter treats **Kirchhoff voltage law** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

22. **A.** The chapter treats **divider rule** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

23. **A.** The chapter treats **nodal circuit analysis** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

24. **A.** The chapter treats **mesh circuit analysis** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

25. **A.** The chapter treats **Thevenin-Norton equivalence** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

26. **A.** The chapter treats **resistive network reduction** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

27. **A.** The chapter treats **Kirchhoff current law** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.


---

## Practice Problems

1. Find equivalent resistance of 4 Ω, 6 Ω, and 10 Ω in series.

2. Find equivalent resistance of 6 Ω and 3 Ω in parallel.

3. At a node, 5 A enters and 2 A plus I leave. Find I.

4. A loop contains a 12 V source and 2 Ω + 4 Ω series resistors. Find current.

5. A 12 V divider has 2 kΩ on top and 4 kΩ on bottom. Find unloaded output across 4 kΩ.

6. Node V is connected to 12 V through 3 kΩ and to ground through 6 kΩ. Find V.

7. A Thévenin source has VTh=10 V and RTh=5 Ω. Find load for maximum power and maximum load power.

8. Convert a Norton source IN=2 A in parallel with RN=4 Ω to Thévenin form.

9. Two mesh currents I1 and I2 share a 5 Ω resistor. What voltage drop in mesh-1 direction is attributed to the shared resistor?

10. A 9 Ω load is connected to a 12 V Thévenin source with 3 Ω internal resistance. Find load current and power.


---

## Practice Problem Solutions

1. 20 Ω.

2. 2 Ω.

3. I=3 A.

4. I=12/6=2 A.

5. Vout=12×4/(2+4)=8 V.

6. (V-12)/3k + V/6k=0 → V=8 V.

7. RL=5 Ω; Pmax=VTh²/(4RTh)=5 W.

8. VTh=IN RN=8 V; RTh=4 Ω.

9. 5(I1-I2).

10. I=12/(3+9)=1 A; PL=9 W.


---

## Quick Reference

**Handbook anchor:** Electrical and Computer Engineering, printed pp. 363–364.

- **resistive network reduction:** Series and Parallel Resistance
- **Kirchhoff current law:** Kirchhoff's Current Law
- **Kirchhoff voltage law:** Kirchhoff's Voltage Law
- **divider rule:** Voltage and Current Dividers
- **nodal circuit analysis:** Nodal Analysis with KCL
- **mesh circuit analysis:** Mesh and Loop Analysis with KVL
- **Thevenin-Norton equivalence:** Thévenin, Norton, and Maximum Power Transfer
---

## What's Next

**02-61 — Capacitance, Inductance, and First-Order Transients**

Carry forward the electrical workflow: define voltage/current references and topology, choose the correct DC/AC or transient model, apply the Handbook relation, and close with conservation and power checks.

— Your Mentor