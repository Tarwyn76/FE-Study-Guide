---
chapter: "02-63"
title: "AC Power, Power Factor, and Three-Phase Systems"
layer: 2
tier: E
template: technical
ledger_ids: [ELEC-2E-063-01, ELEC-2E-063-02, ELEC-2E-063-03, ELEC-2E-063-04, ELEC-2E-063-05, ELEC-2E-063-06, ELEC-2E-063-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-63: AC Power, Power Factor, and Three-Phase Systems

> *"Electrical problems become much easier when references, topology, energy flow, and the correct steady-state or transient model are established before algebra."*

---

## Before You Start

**Prerequisites:** 02-62 Sinusoids, Phasors, and Impedance

**Skip if:** You can identify the governing electrical model, choose correct voltage/current references, use the FE Handbook relation, solve representative FE-level calculations, and verify power, units, and physical behavior.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives real, reactive, apparent, and complex power; leading/lagging power factor; balanced three-phase relationships and power; delta-wye impedance conversion; positive phase-sequence phasors; and ideal transformer material beginning on p. 369. Power-factor correction design is a guide-developed application.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **63.1** Explain and apply **Real, Reactive, Apparent, and Complex Power**.
* **63.2** Explain and apply **Power Factor — Leading and Lagging**.
* **63.3** Explain and apply **Power-Factor Correction**.
* **63.4** Explain and apply **Balanced Three-Phase Sources and Phase Sequence**.
* **63.5** Explain and apply **Wye Line-to-Phase Relationships**.
* **63.6** Explain and apply **Delta Line-to-Phase Relationships**.
* **63.7** Explain and apply **Balanced Three-Phase Power**.

---

## Notation Used Here

Voltage polarities and current directions are reference choices. RMS quantities are used for AC power unless otherwise stated. Use SI units unless a problem explicitly supplies another system.

---

## 63.1 Real, Reactive, Apparent, and Complex Power

For sinusoidal steady state using RMS phasors, real power \(P\) represents average energy conversion, reactive power \(Q\) represents cyclic exchange with fields, and apparent power magnitude is \(|S|=VI\).

Complex power combines them as \(S=P+jQ\).

\[\underline S=\underline V\underline I^*=P+jQ,\qquad P=VI\cos\theta,\qquad Q=VI\sin\theta\]

![FIG-02-63-001: Complex-power triangle with P, Q, |S|, and power-factor angle theta.](../figures/FIG-02-63-001-real-reactive-apparent-and-complex-power.png)

### Worked Example 1

**Problem.** A load takes 120 V RMS, 10 A RMS at pf=0.8 lagging. Find P, Q, and |S|.

**Solution.** |S|=1200 VA; P=960 W; Q=720 var.

---

## 63.2 Power Factor — Leading and Lagging

Power factor is \(P/|S|=\cos\theta\), where \(\theta\) is measured from voltage to current under the Handbook convention. Inductive loads commonly have lagging current; capacitive loads commonly have leading current.

Power factor carries both magnitude and lead/lag information.

\[pf=\cos\theta=\frac{P}{|S|}\]

![FIG-02-63-002: Voltage/current phasors for lagging and leading power factor beside corresponding power triangles.](../figures/FIG-02-63-002-power-factor-leading-and-lagging.png)

### Worked Example 2

**Problem.** A 5 kW load operates at pf=0.60 lagging. Find apparent power.

**Solution.** S=P/pf=8.33 kVA.

---

## 63.3 Power-Factor Correction

Power-factor correction commonly adds capacitive reactive power to offset inductive load VAR demand while leaving real power approximately unchanged.

For a desired final power factor, compute the original and target reactive powers from \(Q=P\tan\theta\), then size compensation for the difference.

\[Q_C=P\left(\tan\theta_1-\tan\theta_2\right)\]

![FIG-02-63-003: Inductive load with shunt capacitor and before/after power triangles.](../figures/FIG-02-63-003-power-factor-correction.png)

### Worked Example 3

**Problem.** A 10 kW load improves from pf=0.70 to 0.95 lagging. Find required capacitor reactive power magnitude.

**Solution.** Qc=P[tan(cos^-1 .70)-tan(cos^-1 .95)]≈6.92 kVAR.

---

## 63.4 Balanced Three-Phase Sources and Phase Sequence

A balanced three-phase source has equal-magnitude phase voltages separated by \(120^\circ\). Positive phase sequence is commonly written \(a\)-\(b\)-\(c\).

Balanced systems permit one-phase analysis followed by a factor of three for total complex power.

\[\underline V_{an}=V_P\angle0^\circ,\quad \underline V_{bn}=V_P\angle-120^\circ,\quad \underline V_{cn}=V_P\angle120^\circ\]

![FIG-02-63-004: Three equal phase-voltage phasors 120 degrees apart with positive abc phase sequence.](../figures/FIG-02-63-004-balanced-three-phase-sources-and-phase-sequence.png)

### Worked Example 4

**Problem.** A balanced positive-sequence set has Van=120∠0° V. State Vbn and Vcn.

**Solution.** Vbn=120∠-120° V; Vcn=120∠120° V.

---

## 63.5 Wye Line-to-Phase Relationships

For a balanced wye connection, line current equals phase current. Line-to-line voltage magnitude is \(\sqrt3\) times line-to-neutral phase voltage and is phase-shifted by \(30^\circ\) relative to the corresponding phase voltage.

Use line quantities and phase quantities deliberately; do not substitute one for the other.

\[I_L=I_P,\qquad V_L=\sqrt3\,V_P\]

![FIG-02-63-005: Balanced wye source/load showing line-to-neutral phase voltage, line-to-line voltage, and line current.](../figures/FIG-02-63-005-wye-line-to-phase-relationships.png)

### Worked Example 5

**Problem.** Balanced wye load has phase voltage 277 V. Find line voltage.

**Solution.** VL=√3×277=479.8 V.

---

## 63.6 Delta Line-to-Phase Relationships

For a balanced delta connection, line voltage equals phase voltage. Line current magnitude is \(\sqrt3\) times phase current.

A balanced delta impedance can be converted to an equivalent wye with \(Z_\Delta=3Z_Y\).

\[V_L=V_P,\qquad I_L=\sqrt3\,I_P,\qquad Z_\Delta=3Z_Y\]

![FIG-02-63-006: Balanced delta load showing phase current, line current, line voltage, and delta-to-wye conversion.](../figures/FIG-02-63-006-delta-line-to-phase-relationships.png)

### Worked Example 6

**Problem.** Balanced delta load has phase current 20 A. Find line current.

**Solution.** IL=√3×20=34.64 A.

---

## 63.7 Balanced Three-Phase Power

For either balanced wye or balanced delta loads, total complex power can be written in terms of line quantities. Real and reactive power follow from the load power-factor angle.

This line formula avoids separately solving three identical phases once the system is known to be balanced.

\[|S_{3\phi}|=\sqrt3\,V_LI_L,\qquad P_{3\phi}=\sqrt3\,V_LI_L\cos\theta,\qquad Q_{3\phi}=\sqrt3\,V_LI_L\sin\theta\]

![FIG-02-63-007: Balanced three-phase source and load with line voltage/current and total P-Q-S relationships.](../figures/FIG-02-63-007-balanced-three-phase-power.png)

### Worked Example 7

**Problem.** Balanced 3φ load has VL=480 V, IL=30 A, pf=0.90. Find real power.

**Solution.** P=√3(480)(30)(0.90)=22.45 kW.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Balanced 3φ load has VL=208 V and IL=15 A. Find apparent power.

**Solution.** S=√3×208×15=5.40 kVA.

### Worked Example 9

**Problem.** A delta impedance is 12+j6 Ω per phase. Find equivalent wye impedance.

**Solution.** ZY=ZΔ/3=4+j2 Ω.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Electrical and Computer Engineering, printed pp. 368–370**.

**Source boundary:** The Handbook directly gives real, reactive, apparent, and complex power; leading/lagging power factor; balanced three-phase relationships and power; delta-wye impedance conversion; positive phase-sequence phasors; and ideal transformer material beginning on p. 369. Power-factor correction design is a guide-developed application.

---

## Where This Goes Wrong

**Using complex power without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using power factor without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using power-factor correction without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using balanced three-phase system without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using wye connection without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using delta connection without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using three-phase power without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Skipping a power or conservation check.** A circuit solution should satisfy KCL/KVL where applicable and should not create unexplained power.


---

## Key Terms

| Term | Working definition |
|---|---|
| complex power | Concept developed in §63.1; use the section definition and stated conditions. |
| power factor | Concept developed in §63.2; use the section definition and stated conditions. |
| power-factor correction | Concept developed in §63.3; use the section definition and stated conditions. |
| balanced three-phase system | Concept developed in §63.4; use the section definition and stated conditions. |
| wye connection | Concept developed in §63.5; use the section definition and stated conditions. |
| delta connection | Concept developed in §63.6; use the section definition and stated conditions. |
| three-phase power | Concept developed in §63.7; use the section definition and stated conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **complex power** and state its governing equation or condition.

2. Define **power factor** and state its governing equation or condition.

3. Define **power-factor correction** and state its governing equation or condition.

4. Define **balanced three-phase system** and state its governing equation or condition.

5. Define **wye connection** and state its governing equation or condition.

6. Define **delta connection** and state its governing equation or condition.

7. Define **three-phase power** and state its governing equation or condition.

8. What is a common analysis error involving **complex power**?

9. What is a common analysis error involving **power factor**?

10. What is a common analysis error involving **power-factor correction**?

11. What is a common analysis error involving **balanced three-phase system**?

12. What is a common analysis error involving **wye connection**?

13. What is a common analysis error involving **delta connection**?

14. What is a common analysis error involving **three-phase power**?

15. Why must voltage polarity and current direction be defined before using signed power?

16. What conservation principle should be used as an independent circuit or machine check?

17. When should a Handbook equation be preferred over a remembered shortcut?

18. Why should RMS and peak values not be mixed in AC power or impedance calculations?

### Multiple Choice

19. Which statement is most accurate for **complex power**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

20. Which statement is most accurate for **power factor**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

21. Which statement is most accurate for **power-factor correction**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

22. Which statement is most accurate for **balanced three-phase system**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

23. Which statement is most accurate for **wye connection**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

24. Which statement is most accurate for **delta connection**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

25. Which statement is most accurate for **three-phase power**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

26. Which statement is most accurate for **complex power**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

27. Which statement is most accurate for **power factor**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **complex power** is developed in §63.1. Use the displayed relation together with its stated sign convention and assumptions.

2. **power factor** is developed in §63.2. Use the displayed relation together with its stated sign convention and assumptions.

3. **power-factor correction** is developed in §63.3. Use the displayed relation together with its stated sign convention and assumptions.

4. **balanced three-phase system** is developed in §63.4. Use the displayed relation together with its stated sign convention and assumptions.

5. **wye connection** is developed in §63.5. Use the displayed relation together with its stated sign convention and assumptions.

6. **delta connection** is developed in §63.6. Use the displayed relation together with its stated sign convention and assumptions.

7. **three-phase power** is developed in §63.7. Use the displayed relation together with its stated sign convention and assumptions.

8. Applying **complex power** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

9. Applying **power factor** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

10. Applying **power-factor correction** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

11. Applying **balanced three-phase system** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

12. Applying **wye connection** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

13. Applying **delta connection** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

14. Applying **three-phase power** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

15. Because the sign of power depends on the chosen voltage/current references and the passive sign convention.

16. Charge/KCL, energy/power balance, and where applicable KVL should close consistently.

17. Whenever the Handbook supplies the relation or when the shortcut's assumptions are uncertain.

18. They represent different magnitudes; mixing them introduces factors such as √2 and gives incorrect power.

19. **A.** The chapter treats **complex power** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

20. **A.** The chapter treats **power factor** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

21. **A.** The chapter treats **power-factor correction** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

22. **A.** The chapter treats **balanced three-phase system** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

23. **A.** The chapter treats **wye connection** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

24. **A.** The chapter treats **delta connection** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

25. **A.** The chapter treats **three-phase power** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

26. **A.** The chapter treats **complex power** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

27. **A.** The chapter treats **power factor** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.


---

## Practice Problems

1. A load takes 120 V RMS, 10 A RMS at pf=0.8 lagging. Find P, Q, and |S|.

2. A 5 kW load operates at pf=0.60 lagging. Find apparent power.

3. A 10 kW load improves from pf=0.70 to 0.95 lagging. Find required capacitor reactive power magnitude.

4. A balanced positive-sequence set has Van=120∠0° V. State Vbn and Vcn.

5. Balanced wye load has phase voltage 277 V. Find line voltage.

6. Balanced delta load has phase current 20 A. Find line current.

7. Balanced 3φ load has VL=480 V, IL=30 A, pf=0.90. Find real power.

8. Balanced 3φ load has VL=208 V and IL=15 A. Find apparent power.

9. A delta impedance is 12+j6 Ω per phase. Find equivalent wye impedance.

10. Does a purely capacitive load have leading or lagging current?


---

## Practice Problem Solutions

1. |S|=1200 VA; P=960 W; Q=720 var.

2. S=P/pf=8.33 kVA.

3. Qc=P[tan(cos^-1 .70)-tan(cos^-1 .95)]≈6.92 kVAR.

4. Vbn=120∠-120° V; Vcn=120∠120° V.

5. VL=√3×277=479.8 V.

6. IL=√3×20=34.64 A.

7. P=√3(480)(30)(0.90)=22.45 kW.

8. S=√3×208×15=5.40 kVA.

9. ZY=ZΔ/3=4+j2 Ω.

10. Current leads voltage; leading power factor.


---

## Quick Reference

**Handbook anchor:** Electrical and Computer Engineering, printed pp. 368–370.

- **complex power:** Real, Reactive, Apparent, and Complex Power
- **power factor:** Power Factor — Leading and Lagging
- **power-factor correction:** Power-Factor Correction
- **balanced three-phase system:** Balanced Three-Phase Sources and Phase Sequence
- **wye connection:** Wye Line-to-Phase Relationships
- **delta connection:** Delta Line-to-Phase Relationships
- **three-phase power:** Balanced Three-Phase Power
---

## What's Next

**02-64 — Magnetics and Transformers**

Carry forward the electrical workflow: define voltage/current references and topology, choose the correct DC/AC or transient model, apply the Handbook relation, and close with conservation and power checks.

— Your Mentor