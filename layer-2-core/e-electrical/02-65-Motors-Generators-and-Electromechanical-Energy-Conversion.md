---
chapter: "02-65"
title: "Motors, Generators, and Electromechanical Energy Conversion"
layer: 2
tier: E
template: technical
ledger_ids: [ELEC-2E-065-01, ELEC-2E-065-02, ELEC-2E-065-03, ELEC-2E-065-04, ELEC-2E-065-05, ELEC-2E-065-06, ELEC-2E-065-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-65: Motors, Generators, and Electromechanical Energy Conversion

> *"Electrical problems become much easier when references, topology, energy flow, and the correct steady-state or transient model are established before algebra."*

---

## Before You Start

**Prerequisites:** 02-63 AC Power and Three-Phase Systems · 02-64 Magnetics and Transformers · 02-34 Work, Energy, and Power

**Skip if:** You can identify the governing electrical model, choose correct voltage/current references, use the FE Handbook relation, solve representative FE-level calculations, and verify power, units, and physical behavior.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives rotating-machine efficiency and losses, mechanical torque-power-speed relations, synchronous speed, synchronous-machine power relations, induction-machine slip and torque-speed context, DC-machine voltage/flux/torque relations, and servomotor/generator relationships.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **65.1** Explain and apply **Rotating-Machine Power Flow, Losses, and Efficiency**.
* **65.2** Explain and apply **Torque, Speed, and Mechanical Power**.
* **65.3** Explain and apply **Synchronous Speed and AC Machine Families**.
* **65.4** Explain and apply **Synchronous Machines and Power Angle**.
* **65.5** Explain and apply **Induction Machines — Slip and Torque-Speed Behavior**.
* **65.6** Explain and apply **DC Machines — Back EMF, Flux, and Torque**.
* **65.7** Explain and apply **Servomotors, Tachogenerators, and Conversion Checks**.

---

## Notation Used Here

Voltage polarities and current directions are reference choices. RMS quantities are used for AC power unless otherwise stated. Use SI units unless a problem explicitly supplies another system.

---

## 65.1 Rotating-Machine Power Flow, Losses, and Efficiency

A motor converts electrical input to mechanical output; a generator converts mechanical input to electrical output. Machine losses include copper, core, friction/windage, and stray components.

Efficiency is output divided by input and must be based on the correct input/output energy domains.

\[\eta=\frac{P_{out}}{P_{in}},\qquad P_{out}=P_{in}-P_{loss}\]

![FIG-02-65-001: Motor and generator power-flow diagrams with copper, core, friction/windage, and stray losses.](../figures/FIG-02-65-001-rotating-machine-power-flow-losses-and-efficiency.png)

### Worked Example 1

**Problem.** A motor takes 10 kW electrical input and delivers 8.5 kW mechanical output. Find efficiency and losses.

**Solution.** η=85%; losses=1.5 kW.

---

## 65.2 Torque, Speed, and Mechanical Power

Mechanical power in a rotating shaft is torque times angular speed. Convert rpm to rad/s before using SI torque-power equations.

At fixed power, torque and speed are inversely related.

\[P_m=T\omega_m,\qquad \omega_m=\frac{2\pi n}{60}\]

![FIG-02-65-002: Rotating shaft labeled torque, rpm, angular speed, and mechanical power.](../figures/FIG-02-65-002-torque-speed-and-mechanical-power.png)

### Worked Example 2

**Problem.** A shaft delivers 20 N·m at 1800 rpm. Find mechanical power.

**Solution.** ω=2π(1800)/60=188.5 rad/s; P=3.77 kW.

---

## 65.3 Synchronous Speed and AC Machine Families

The rotating magnetic field of an AC machine has synchronous speed determined by supply frequency and number of poles.

Synchronous machines operate at synchronous speed in steady operation; induction-machine rotors normally run below synchronous speed in motoring operation.

\[n_s=\frac{120f}{p}\ \text{rpm}\]

![FIG-02-65-003: Chart linking line frequency, pole count, and synchronous speed with synchronous and induction rotor speeds.](../figures/FIG-02-65-003-synchronous-speed-and-ac-machine-families.png)

### Worked Example 3

**Problem.** Find synchronous speed for 60 Hz, 4 poles.

**Solution.** ns=120f/p=1800 rpm.

---

## 65.4 Synchronous Machines and Power Angle

The Handbook models a Y-connected synchronous machine with internal induced voltage \(E_a\), synchronous reactance \(X_s\), armature resistance, and torque/power angle \(\delta\).

When armature resistance is neglected, developed power varies approximately with \(\sin\delta\) for fixed voltage magnitudes.

\[P_d\approx 3\frac{E_aV_a}{X_s}\sin\delta\]

![FIG-02-65-004: Synchronous-machine equivalent circuit and power-versus-angle sine curve.](../figures/FIG-02-65-004-synchronous-machines-and-power-angle.png)

### Worked Example 4

**Problem.** A synchronous machine has Ea=240 V phase, Va=230 V phase, Xs=2 Ω, δ=20°, neglect Ra. Find developed 3φ power.

**Solution.** P=3(EaVa/Xs)sinδ≈28.3 kW.

---

## 65.5 Induction Machines — Slip and Torque-Speed Behavior

Induction-machine slip measures the fractional difference between synchronous speed and rotor speed. At synchronous speed, slip is zero.

The Handbook includes a representative torque-speed curve with starting torque, breakdown region, and normal operating region.

\[s=\frac{n_s-n}{n_s}\]

![FIG-02-65-005: Induction-motor torque-speed curve labeled synchronous speed, slip, starting torque, and breakdown torque.](../figures/FIG-02-65-005-induction-machines-slip-and-torque-speed-behavior.png)

### Worked Example 5

**Problem.** An induction motor has ns=1800 rpm and n=1746 rpm. Find slip.

**Solution.** s=(1800-1746)/1800=0.030=3.0%.

---

## 65.6 DC Machines — Back EMF, Flux, and Torque

The Handbook represents DC-machine armature voltage with resistance, inductance, and a speed-dependent induced voltage. Neglecting saturation, field flux is proportional to field current.

Mechanical power and torque are proportional to armature current and flux under the stated model.

\[V_a=K_an\Phi,\qquad P_m=V_aI_a,\qquad T_m=\frac{60}{2\pi}K_a\Phi I_a\]

![FIG-02-65-006: DC motor/generator armature and field circuits with back EMF, current, flux, torque, and speed.](../figures/FIG-02-65-006-dc-machines-back-emf-flux-and-torque.png)

### Worked Example 6

**Problem.** A PM DC motor has KE=0.20 V/(rad/s), R=1 Ω, V=24 V and ω=100 rad/s. Find current; if KT=0.20 N·m/A, find torque.

**Solution.** I=(24-20)/1=4 A; T=0.8 N·m.

---

## 65.7 Servomotors, Tachogenerators, and Conversion Checks

The Handbook gives an idealized permanent-magnet DC motor relation \(V=IR+K_E\omega\) and torque \(T=K_TI\), with \(K_T=K_E\) in consistent SI units. A permanent-magnet generator can produce a speed-proportional voltage for tachometry.

For any electromechanical device, verify electrical input/output power, mechanical \(T\omega\), losses, and efficiency are mutually consistent.

\[V=IR+K_E\omega,\qquad T=K_TI,\qquad K_T=K_E\ \text{in consistent SI units}\]

![FIG-02-65-007: Permanent-magnet DC motor speed-torque line with electrical equation and tachogenerator conversion direction.](../figures/FIG-02-65-007-servomotors-tachogenerators-and-conversion-checks.png)

### Worked Example 7

**Problem.** A generator receives 5 kW mechanical input at 90% efficiency. Find electrical output.

**Solution.** 4.5 kW.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** For a 50 Hz, 6-pole AC machine, find synchronous speed.

**Solution.** ns=120(50)/6=1000 rpm.

### Worked Example 9

**Problem.** An induction motor runs at 970 rpm on a 1000 rpm synchronous field. Find slip.

**Solution.** 3.0%.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Electrical and Computer Engineering, printed pp. 370–373**.

**Source boundary:** The Handbook directly gives rotating-machine efficiency and losses, mechanical torque-power-speed relations, synchronous speed, synchronous-machine power relations, induction-machine slip and torque-speed context, DC-machine voltage/flux/torque relations, and servomotor/generator relationships.

---

## Where This Goes Wrong

**Using rotating-machine efficiency without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using electromechanical torque and speed without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using synchronous speed without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using synchronous-machine power angle without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using induction-machine slip without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using DC machine electromechanics without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using servomotor electromechanical model without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Skipping a power or conservation check.** A circuit solution should satisfy KCL/KVL where applicable and should not create unexplained power.


---

## Key Terms

| Term | Working definition |
|---|---|
| rotating-machine efficiency | Concept developed in §65.1; use the section definition and stated conditions. |
| electromechanical torque and speed | Concept developed in §65.2; use the section definition and stated conditions. |
| synchronous speed | Concept developed in §65.3; use the section definition and stated conditions. |
| synchronous-machine power angle | Concept developed in §65.4; use the section definition and stated conditions. |
| induction-machine slip | Concept developed in §65.5; use the section definition and stated conditions. |
| DC machine electromechanics | Concept developed in §65.6; use the section definition and stated conditions. |
| servomotor electromechanical model | Concept developed in §65.7; use the section definition and stated conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **rotating-machine efficiency** and state its governing equation or condition.

2. Define **electromechanical torque and speed** and state its governing equation or condition.

3. Define **synchronous speed** and state its governing equation or condition.

4. Define **synchronous-machine power angle** and state its governing equation or condition.

5. Define **induction-machine slip** and state its governing equation or condition.

6. Define **DC machine electromechanics** and state its governing equation or condition.

7. Define **servomotor electromechanical model** and state its governing equation or condition.

8. What is a common analysis error involving **rotating-machine efficiency**?

9. What is a common analysis error involving **electromechanical torque and speed**?

10. What is a common analysis error involving **synchronous speed**?

11. What is a common analysis error involving **synchronous-machine power angle**?

12. What is a common analysis error involving **induction-machine slip**?

13. What is a common analysis error involving **DC machine electromechanics**?

14. What is a common analysis error involving **servomotor electromechanical model**?

15. Why must voltage polarity and current direction be defined before using signed power?

16. What conservation principle should be used as an independent circuit or machine check?

17. When should a Handbook equation be preferred over a remembered shortcut?

18. Why should RMS and peak values not be mixed in AC power or impedance calculations?

### Multiple Choice

19. Which statement is most accurate for **rotating-machine efficiency**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

20. Which statement is most accurate for **electromechanical torque and speed**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

21. Which statement is most accurate for **synchronous speed**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

22. Which statement is most accurate for **synchronous-machine power angle**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

23. Which statement is most accurate for **induction-machine slip**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

24. Which statement is most accurate for **DC machine electromechanics**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

25. Which statement is most accurate for **servomotor electromechanical model**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

26. Which statement is most accurate for **rotating-machine efficiency**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

27. Which statement is most accurate for **electromechanical torque and speed**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **rotating-machine efficiency** is developed in §65.1. Use the displayed relation together with its stated sign convention and assumptions.

2. **electromechanical torque and speed** is developed in §65.2. Use the displayed relation together with its stated sign convention and assumptions.

3. **synchronous speed** is developed in §65.3. Use the displayed relation together with its stated sign convention and assumptions.

4. **synchronous-machine power angle** is developed in §65.4. Use the displayed relation together with its stated sign convention and assumptions.

5. **induction-machine slip** is developed in §65.5. Use the displayed relation together with its stated sign convention and assumptions.

6. **DC machine electromechanics** is developed in §65.6. Use the displayed relation together with its stated sign convention and assumptions.

7. **servomotor electromechanical model** is developed in §65.7. Use the displayed relation together with its stated sign convention and assumptions.

8. Applying **rotating-machine efficiency** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

9. Applying **electromechanical torque and speed** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

10. Applying **synchronous speed** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

11. Applying **synchronous-machine power angle** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

12. Applying **induction-machine slip** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

13. Applying **DC machine electromechanics** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

14. Applying **servomotor electromechanical model** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

15. Because the sign of power depends on the chosen voltage/current references and the passive sign convention.

16. Charge/KCL, energy/power balance, and where applicable KVL should close consistently.

17. Whenever the Handbook supplies the relation or when the shortcut's assumptions are uncertain.

18. They represent different magnitudes; mixing them introduces factors such as √2 and gives incorrect power.

19. **A.** The chapter treats **rotating-machine efficiency** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

20. **A.** The chapter treats **electromechanical torque and speed** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

21. **A.** The chapter treats **synchronous speed** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

22. **A.** The chapter treats **synchronous-machine power angle** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

23. **A.** The chapter treats **induction-machine slip** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

24. **A.** The chapter treats **DC machine electromechanics** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

25. **A.** The chapter treats **servomotor electromechanical model** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

26. **A.** The chapter treats **rotating-machine efficiency** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

27. **A.** The chapter treats **electromechanical torque and speed** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.


---

## Practice Problems

1. A motor takes 10 kW electrical input and delivers 8.5 kW mechanical output. Find efficiency and losses.

2. A shaft delivers 20 N·m at 1800 rpm. Find mechanical power.

3. Find synchronous speed for 60 Hz, 4 poles.

4. A synchronous machine has Ea=240 V phase, Va=230 V phase, Xs=2 Ω, δ=20°, neglect Ra. Find developed 3φ power.

5. An induction motor has ns=1800 rpm and n=1746 rpm. Find slip.

6. A PM DC motor has KE=0.20 V/(rad/s), R=1 Ω, V=24 V and ω=100 rad/s. Find current; if KT=0.20 N·m/A, find torque.

7. A generator receives 5 kW mechanical input at 90% efficiency. Find electrical output.

8. For a 50 Hz, 6-pole AC machine, find synchronous speed.

9. An induction motor runs at 970 rpm on a 1000 rpm synchronous field. Find slip.

10. Why can a motor and generator use the same electromechanical principles?


---

## Practice Problem Solutions

1. η=85%; losses=1.5 kW.

2. ω=2π(1800)/60=188.5 rad/s; P=3.77 kW.

3. ns=120f/p=1800 rpm.

4. P=3(EaVa/Xs)sinδ≈28.3 kW.

5. s=(1800-1746)/1800=0.030=3.0%.

6. I=(24-20)/1=4 A; T=0.8 N·m.

7. 4.5 kW.

8. ns=120(50)/6=1000 rpm.

9. 3.0%.

10. Energy conversion is reversible in principle; power-flow direction distinguishes motor from generator operation.


---

## Quick Reference

**Handbook anchor:** Electrical and Computer Engineering, printed pp. 370–373.

- **rotating-machine efficiency:** Rotating-Machine Power Flow, Losses, and Efficiency
- **electromechanical torque and speed:** Torque, Speed, and Mechanical Power
- **synchronous speed:** Synchronous Speed and AC Machine Families
- **synchronous-machine power angle:** Synchronous Machines and Power Angle
- **induction-machine slip:** Induction Machines — Slip and Torque-Speed Behavior
- **DC machine electromechanics:** DC Machines — Back EMF, Flux, and Torque
- **servomotor electromechanical model:** Servomotors, Tachogenerators, and Conversion Checks
---

## What's Next

**02-66 — Measurement Systems, Calibration, Accuracy, and Uncertainty**

Carry forward the electrical workflow: define voltage/current references and topology, choose the correct DC/AC or transient model, apply the Handbook relation, and close with conservation and power checks.

— Your Mentor