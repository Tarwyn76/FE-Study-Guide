---
chapter: "02-61"
title: "Capacitance, Inductance, and First-Order Transients"
layer: 2
tier: E
template: technical
ledger_ids: [ELEC-2E-061-01, ELEC-2E-061-02, ELEC-2E-061-03, ELEC-2E-061-04, ELEC-2E-061-05, ELEC-2E-061-06, ELEC-2E-061-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-61: Capacitance, Inductance, and First-Order Transients

> *"Electrical problems become much easier when references, topology, energy flow, and the correct steady-state or transient model are established before algebra."*

---

## Before You Start

**Prerequisites:** 02-60 Resistive Circuit Analysis · 01-16 Exponential Functions · 01-25 Differential Equations

**Skip if:** You can identify the governing electrical model, choose correct voltage/current references, use the FE Handbook relation, solve representative FE-level calculations, and verify power, units, and physical behavior.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives capacitor and inductor constitutive relations, stored energy, series/parallel combinations, and RC/RL transient expressions with time constants. Initial/final-value workflow and switching interpretation are guide-developed teaching structure.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **61.1** Explain and apply **Capacitance and Capacitor Current-Voltage Relation**.
* **61.2** Explain and apply **Capacitor Energy and Equivalent Capacitance**.
* **61.3** Explain and apply **Inductance and Inductor Voltage-Current Relation**.
* **61.4** Explain and apply **Inductor Energy and Equivalent Inductance**.
* **61.5** Explain and apply **Switching, Initial Conditions, and Final Values**.
* **61.6** Explain and apply **RC First-Order Transients**.
* **61.7** Explain and apply **RL First-Order Transients**.

---

## Notation Used Here

Voltage polarities and current directions are reference choices. RMS quantities are used for AC power unless otherwise stated. Use SI units unless a problem explicitly supplies another system.

---

## 61.1 Capacitance and Capacitor Current-Voltage Relation

A capacitor stores electric-field energy and relates charge to voltage through \(q=Cv_C\). Its current is proportional to the time derivative of voltage.

An ideal capacitor voltage cannot change instantaneously without infinite current.

\[q=Cv_C,\qquad i_C=C\frac{dv_C}{dt}\]

![FIG-02-61-001: Capacitor symbol with voltage/current reference, plate charge, and electric-field storage.](../figures/FIG-02-61-001-capacitance-and-capacitor-current-voltage-relation.png)

### Worked Example 1

**Problem.** A 10 µF capacitor has 12 V across it. Find charge.

**Solution.** q=CV=120 µC.

---

## 61.2 Capacitor Energy and Equivalent Capacitance

The energy stored in an ideal capacitor is nonnegative and depends on voltage squared. Parallel capacitors add directly; series capacitors combine reciprocally.

Series capacitors carry equal magnitude charge in the ideal two-terminal series chain.

\[W_C=\frac12Cv_C^2,\qquad C_p=\sum C_i,\qquad \frac1{C_s}=\sum\frac1{C_i}\]

![FIG-02-61-002: Series and parallel capacitor combinations with equivalent-capacitance formulas and stored-energy callout.](../figures/FIG-02-61-002-capacitor-energy-and-equivalent-capacitance.png)

### Worked Example 2

**Problem.** A 100 µF capacitor is at 20 V. Find stored energy.

**Solution.** W=0.5CV²=0.020 J.

---

## 61.3 Inductance and Inductor Voltage-Current Relation

An inductor stores magnetic-field energy. Its terminal voltage is proportional to the time derivative of current.

An ideal inductor current cannot change instantaneously without infinite voltage.

\[v_L=L\frac{di_L}{dt}\]

![FIG-02-61-003: Inductor coil with current, flux linkage, voltage polarity, and magnetic-field storage.](../figures/FIG-02-61-003-inductance-and-inductor-voltage-current-relation.png)

### Worked Example 3

**Problem.** Two capacitors 6 µF and 3 µF are in series. Find equivalent capacitance.

**Solution.** Cs=(6×3)/(6+3)=2 µF.

---

## 61.4 Inductor Energy and Equivalent Inductance

Stored magnetic energy is \(W_L=\tfrac12Li^2\). For uncoupled inductors, series inductances add and parallel inductances combine reciprocally.

Mutual coupling changes these simple rules; use them only when coupling is absent or neglected.

\[W_L=\frac12Li_L^2,\qquad L_s=\sum L_i,\qquad \frac1{L_p}=\sum\frac1{L_i}\]

![FIG-02-61-004: Series and parallel uncoupled inductors with equivalent-inductance and energy formulas.](../figures/FIG-02-61-004-inductor-energy-and-equivalent-inductance.png)

### Worked Example 4

**Problem.** A 0.50 H inductor current changes at 4 A/s. Find voltage.

**Solution.** v=L di/dt=2 V.

---

## 61.5 Switching, Initial Conditions, and Final Values

For first-order circuits, determine the storage-variable initial value just before switching and use continuity: capacitor voltage and inductor current carry through the switching instant.

Then determine the long-time DC final value. At DC steady state, an ideal capacitor behaves as an open circuit and an ideal inductor as a short circuit.

\[v_C(0^+)=v_C(0^-),\qquad i_L(0^+)=i_L(0^-)\]

![FIG-02-61-005: RC and RL switching circuits showing pre-switch state, instant after switching, and long-time DC equivalents.](../figures/FIG-02-61-005-switching-initial-conditions-and-final-values.png)

### Worked Example 5

**Problem.** A 2 H inductor carries 3 A. Find stored energy.

**Solution.** W=0.5LI²=9 J.

---

## 61.6 RC First-Order Transients

A first-order RC response moves exponentially from an initial capacitor voltage to a final value with time constant \(\tau=R_{eq}C\), where \(R_{eq}\) is the resistance seen by the capacitor in the natural-response network.

The universal form is final value plus initial error times \(e^{-t/\tau}\).

\[v_C(t)=v_C(\infty)+\big[v_C(0^+)-v_C(\infty)\big]e^{-t/\tau},\qquad \tau=R_{eq}C\]

![FIG-02-61-006: RC charging/discharging exponential with initial value, final value, one time constant, and five time constants.](../figures/FIG-02-61-006-rc-first-order-transients.png)

### Worked Example 6

**Problem.** An RC circuit has Req=20 kΩ and C=50 µF. Find time constant.

**Solution.** τ=RC=1.0 s.

---

## 61.7 RL First-Order Transients

An RL current response has the same first-order exponential structure. The time constant is \(\tau=L/R_{eq}\), with the resistance seen by the inductor in the natural-response network.

Use current continuity at the switching instant and solve the DC final circuit for \(i_L(\infty)\).

\[i_L(t)=i_L(\infty)+\big[i_L(0^+)-i_L(\infty)\big]e^{-t/\tau},\qquad \tau=\frac{L}{R_{eq}}\]

![FIG-02-61-007: RL current rise/decay exponential with initial/final currents and time-constant markers.](../figures/FIG-02-61-007-rl-first-order-transients.png)

### Worked Example 7

**Problem.** An RL circuit has L=2 H and Req=10 Ω. Find time constant.

**Solution.** τ=L/R=0.20 s.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A capacitor moves from 0 V toward 10 V with τ=2 s. Find vC at t=2 s.

**Solution.** v=10(1-e^-1)=6.32 V.

### Worked Example 9

**Problem.** An inductor current decays from 5 A to 0 with τ=0.5 s. Find current at 1.0 s.

**Solution.** i=5e^-2=0.677 A.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Electrical and Computer Engineering, printed pp. 364–367**.

**Source boundary:** The Handbook directly gives capacitor and inductor constitutive relations, stored energy, series/parallel combinations, and RC/RL transient expressions with time constants. Initial/final-value workflow and switching interpretation are guide-developed teaching structure.

---

## Where This Goes Wrong

**Using capacitance without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using capacitor energy and combination without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using inductance without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using inductor energy and combination without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using first-order switching conditions without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using RC transient without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using RL transient without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Skipping a power or conservation check.** A circuit solution should satisfy KCL/KVL where applicable and should not create unexplained power.


---

## Key Terms

| Term | Working definition |
|---|---|
| capacitance | Concept developed in §61.1; use the section definition and stated conditions. |
| capacitor energy and combination | Concept developed in §61.2; use the section definition and stated conditions. |
| inductance | Concept developed in §61.3; use the section definition and stated conditions. |
| inductor energy and combination | Concept developed in §61.4; use the section definition and stated conditions. |
| first-order switching conditions | Concept developed in §61.5; use the section definition and stated conditions. |
| RC transient | Concept developed in §61.6; use the section definition and stated conditions. |
| RL transient | Concept developed in §61.7; use the section definition and stated conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **capacitance** and state its governing equation or condition.

2. Define **capacitor energy and combination** and state its governing equation or condition.

3. Define **inductance** and state its governing equation or condition.

4. Define **inductor energy and combination** and state its governing equation or condition.

5. Define **first-order switching conditions** and state its governing equation or condition.

6. Define **RC transient** and state its governing equation or condition.

7. Define **RL transient** and state its governing equation or condition.

8. What is a common analysis error involving **capacitance**?

9. What is a common analysis error involving **capacitor energy and combination**?

10. What is a common analysis error involving **inductance**?

11. What is a common analysis error involving **inductor energy and combination**?

12. What is a common analysis error involving **first-order switching conditions**?

13. What is a common analysis error involving **RC transient**?

14. What is a common analysis error involving **RL transient**?

15. Why must voltage polarity and current direction be defined before using signed power?

16. What conservation principle should be used as an independent circuit or machine check?

17. When should a Handbook equation be preferred over a remembered shortcut?

18. Why should RMS and peak values not be mixed in AC power or impedance calculations?

### Multiple Choice

19. Which statement is most accurate for **capacitance**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

20. Which statement is most accurate for **capacitor energy and combination**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

21. Which statement is most accurate for **inductance**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

22. Which statement is most accurate for **inductor energy and combination**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

23. Which statement is most accurate for **first-order switching conditions**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

24. Which statement is most accurate for **RC transient**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

25. Which statement is most accurate for **RL transient**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

26. Which statement is most accurate for **capacitance**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

27. Which statement is most accurate for **capacitor energy and combination**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **capacitance** is developed in §61.1. Use the displayed relation together with its stated sign convention and assumptions.

2. **capacitor energy and combination** is developed in §61.2. Use the displayed relation together with its stated sign convention and assumptions.

3. **inductance** is developed in §61.3. Use the displayed relation together with its stated sign convention and assumptions.

4. **inductor energy and combination** is developed in §61.4. Use the displayed relation together with its stated sign convention and assumptions.

5. **first-order switching conditions** is developed in §61.5. Use the displayed relation together with its stated sign convention and assumptions.

6. **RC transient** is developed in §61.6. Use the displayed relation together with its stated sign convention and assumptions.

7. **RL transient** is developed in §61.7. Use the displayed relation together with its stated sign convention and assumptions.

8. Applying **capacitance** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

9. Applying **capacitor energy and combination** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

10. Applying **inductance** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

11. Applying **inductor energy and combination** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

12. Applying **first-order switching conditions** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

13. Applying **RC transient** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

14. Applying **RL transient** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

15. Because the sign of power depends on the chosen voltage/current references and the passive sign convention.

16. Charge/KCL, energy/power balance, and where applicable KVL should close consistently.

17. Whenever the Handbook supplies the relation or when the shortcut's assumptions are uncertain.

18. They represent different magnitudes; mixing them introduces factors such as √2 and gives incorrect power.

19. **A.** The chapter treats **capacitance** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

20. **A.** The chapter treats **capacitor energy and combination** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

21. **A.** The chapter treats **inductance** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

22. **A.** The chapter treats **inductor energy and combination** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

23. **A.** The chapter treats **first-order switching conditions** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

24. **A.** The chapter treats **RC transient** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

25. **A.** The chapter treats **RL transient** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

26. **A.** The chapter treats **capacitance** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

27. **A.** The chapter treats **capacitor energy and combination** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.


---

## Practice Problems

1. A 10 µF capacitor has 12 V across it. Find charge.

2. A 100 µF capacitor is at 20 V. Find stored energy.

3. Two capacitors 6 µF and 3 µF are in series. Find equivalent capacitance.

4. A 0.50 H inductor current changes at 4 A/s. Find voltage.

5. A 2 H inductor carries 3 A. Find stored energy.

6. An RC circuit has Req=20 kΩ and C=50 µF. Find time constant.

7. An RL circuit has L=2 H and Req=10 Ω. Find time constant.

8. A capacitor moves from 0 V toward 10 V with τ=2 s. Find vC at t=2 s.

9. An inductor current decays from 5 A to 0 with τ=0.5 s. Find current at 1.0 s.

10. A capacitor has 7 V immediately before switching. What is vC immediately after switching?


---

## Practice Problem Solutions

1. q=CV=120 µC.

2. W=0.5CV²=0.020 J.

3. Cs=(6×3)/(6+3)=2 µF.

4. v=L di/dt=2 V.

5. W=0.5LI²=9 J.

6. τ=RC=1.0 s.

7. τ=L/R=0.20 s.

8. v=10(1-e^-1)=6.32 V.

9. i=5e^-2=0.677 A.

10. 7 V for an ideal finite-current circuit.


---

## Quick Reference

**Handbook anchor:** Electrical and Computer Engineering, printed pp. 364–367.

- **capacitance:** Capacitance and Capacitor Current-Voltage Relation
- **capacitor energy and combination:** Capacitor Energy and Equivalent Capacitance
- **inductance:** Inductance and Inductor Voltage-Current Relation
- **inductor energy and combination:** Inductor Energy and Equivalent Inductance
- **first-order switching conditions:** Switching, Initial Conditions, and Final Values
- **RC transient:** RC First-Order Transients
- **RL transient:** RL First-Order Transients
---

## What's Next

**02-62 — Sinusoids, Phasors, Impedance, and Resonance**

Carry forward the electrical workflow: define voltage/current references and topology, choose the correct DC/AC or transient model, apply the Handbook relation, and close with conservation and power checks.

— Your Mentor