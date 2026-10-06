---
chapter: "02-64"
title: "Magnetics and Transformers"
layer: 2
tier: E
template: technical
ledger_ids: [ELEC-2E-064-01, ELEC-2E-064-02, ELEC-2E-064-03, ELEC-2E-064-04, ELEC-2E-064-05, ELEC-2E-064-06, ELEC-2E-064-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-64: Magnetics and Transformers

> *"Electrical problems become much easier when references, topology, energy flow, and the correct steady-state or transient model are established before algebra."*

---

## Before You Start

**Prerequisites:** 02-61 Inductance · 02-63 Three-Phase Systems

**Skip if:** You can identify the governing electrical model, choose correct voltage/current references, use the FE Handbook relation, solve representative FE-level calculations, and verify power, units, and physical behavior.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives magnetic field strength/flux-density context, force on a current-carrying conductor, Faraday's law, reluctance and inductance relations, ideal-transformer turns/current/impedance ratios, and common three-phase transformer connection diagrams.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **64.1** Explain and apply **Magnetic Field, Flux Density, and Permeability**.
* **64.2** Explain and apply **Force on a Current-Carrying Conductor**.
* **64.3** Explain and apply **Faraday's Law and Lenz's Law**.
* **64.4** Explain and apply **Reluctance, Flux Linkage, and Inductance**.
* **64.5** Explain and apply **Ideal Transformer Turns and Current Ratios**.
* **64.6** Explain and apply **Reflected Impedance**.
* **64.7** Explain and apply **Three-Phase Transformer Connections**.

---

## Notation Used Here

Voltage polarities and current directions are reference choices. RMS quantities are used for AC power unless otherwise stated. Use SI units unless a problem explicitly supplies another system.

---

## 64.1 Magnetic Field, Flux Density, and Permeability

Current produces magnetic field intensity \(H\), while magnetic flux density is related by \(B=\mu H\) for a linear material. Magnetic flux is the surface integral of \(B\).

Permeability describes how strongly a material supports magnetic flux for a given field intensity.

\[\mathbf B=\mu\mathbf H,\qquad \Phi=\int_S\mathbf B\cdot d\mathbf S\]

![FIG-02-64-001: Current-carrying conductor and magnetic core showing H, B, flux Phi, and permeability.](../figures/FIG-02-64-001-magnetic-field-flux-density-and-permeability.png)

### Worked Example 1

**Problem.** A linear magnetic material has μ=2.0×10^-3 H/m and H=500 A/m. Find B.

**Solution.** B=μH=1.0 T.

---

## 64.2 Force on a Current-Carrying Conductor

A current-carrying conductor in a magnetic flux density experiences force according to the vector cross product \( \mathbf F=I\mathbf L\times\mathbf B\).

Magnitude depends on conductor length in the field and the sine of the angle between current direction and \(B\).

\[\mathbf F=I\mathbf L\times\mathbf B,\qquad F=ILB\sin\theta\]

![FIG-02-64-002: Straight conductor in uniform magnetic field with current, force, and cross-product directions.](../figures/FIG-02-64-002-force-on-a-current-carrying-conductor.png)

### Worked Example 2

**Problem.** A 0.50 m conductor carries 10 A perpendicular to B=0.8 T. Find force.

**Solution.** F=ILB=4 N.

---

## 64.3 Faraday's Law and Lenz's Law

A changing magnetic flux linking a coil induces voltage. The negative sign in Faraday's law represents Lenz's law: induced effects oppose the change that produced them.

Induced voltage increases with turns count and rate of flux change.

\[v=-N\frac{d\Phi}{dt}\]

![FIG-02-64-003: Coil linked by changing magnetic flux with induced voltage polarity illustrating Lenz's law.](../figures/FIG-02-64-003-faraday-s-law-and-lenz-s-law.png)

### Worked Example 3

**Problem.** A 200-turn coil experiences flux change 3 mWb to 1 mWb in 0.01 s. Find induced-voltage magnitude.

**Solution.** |v|=N|ΔΦ/Δt|=200(0.002/0.01)=40 V.

---

## 64.4 Reluctance, Flux Linkage, and Inductance

A simple magnetic circuit can be represented by reluctance \(\mathcal R=\ell/(\mu A)\). For the idealized coil/core relation in the Handbook, inductance is \(L=N^2/\mathcal R\).

Air gaps can dominate reluctance because air has much lower permeability than ferromagnetic core material.

\[\mathcal R=\frac{\ell}{\mu A},\qquad L=\frac{N^2}{\mathcal R}\]

![FIG-02-64-004: Magnetic core with mean path length, cross-section, coil turns, flux, and reluctance analogy.](../figures/FIG-02-64-004-reluctance-flux-linkage-and-inductance.png)

### Worked Example 4

**Problem.** A magnetic path has l=0.20 m, μ=1.0×10^-3 H/m, A=4×10^-4 m². Find reluctance.

**Solution.** Rmag=l/(μA)=5.0×10^5 H^-1.

---

## 64.5 Ideal Transformer Turns and Current Ratios

For an ideal transformer, voltage ratio equals turns ratio, while current ratio is inverse. Ideal input and output apparent power are equal.

Define \(a=N_P/N_S\) and apply the polarity/dot convention supplied by the problem.

\[\frac{V_P}{V_S}=a=\frac{N_P}{N_S},\qquad \frac{I_P}{I_S}=\frac1a\]

![FIG-02-64-005: Ideal transformer with primary/secondary turns, voltage/current polarities, and turns ratio.](../figures/FIG-02-64-005-ideal-transformer-turns-and-current-ratios.png)

### Worked Example 5

**Problem.** An ideal transformer has NP=1000, NS=250, VP=480 V. Find VS.

**Solution.** a=4; VS=120 V.

---

## 64.6 Reflected Impedance

A load impedance connected to the secondary appears at the primary multiplied by the square of the turns ratio.

This is why transformers can match impedances as well as step voltage up or down.

\[Z_P=a^2Z_S\]

![FIG-02-64-006: Secondary load reflected through an ideal transformer to an equivalent primary impedance.](../figures/FIG-02-64-006-reflected-impedance.png)

### Worked Example 6

**Problem.** For the transformer in Problem 5, a 12 Ω secondary load is connected. Find reflected primary impedance.

**Solution.** ZP=a²ZS=16×12=192 Ω.

---

## 64.7 Three-Phase Transformer Connections

The Handbook shows wye-wye, wye-delta, delta-wye, and delta-delta connection diagrams. Connection choice affects neutral availability, line/phase ratios, and phase displacement.

Detailed grounding, harmonic, and protection design is outside this chapter; use the diagram and ratio information explicitly provided for FE-level problems.

\[\text{connection determines line/phase mapping and possible phase shift}\]

![FIG-02-64-007: Four panels comparing wye-wye, wye-delta, delta-wye, and delta-delta transformer connections.](../figures/FIG-02-64-007-three-phase-transformer-connections.png)

### Worked Example 7

**Problem.** Name the four common three-phase transformer connection families shown in the Handbook.

**Solution.** Wye-wye, wye-delta, delta-wye, delta-delta.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** An ideal transformer has VP/VS=5. If secondary current is 10 A, find primary current.

**Solution.** IP=IS/5=2 A.

### Worked Example 9

**Problem.** If a core air gap is added, what usually happens to reluctance?

**Solution.** It increases strongly because air permeability is much lower.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Electrical and Computer Engineering, printed pp. 362, 364, and 369–370**.

**Source boundary:** The Handbook directly gives magnetic field strength/flux-density context, force on a current-carrying conductor, Faraday's law, reluctance and inductance relations, ideal-transformer turns/current/impedance ratios, and common three-phase transformer connection diagrams.

---

## Where This Goes Wrong

**Using magnetic flux without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using magnetic force on conductor without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using Faraday induction without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using magnetic reluctance without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using ideal transformer without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using reflected impedance without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using three-phase transformer connection without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Skipping a power or conservation check.** A circuit solution should satisfy KCL/KVL where applicable and should not create unexplained power.


---

## Key Terms

| Term | Working definition |
|---|---|
| magnetic flux | Concept developed in §64.1; use the section definition and stated conditions. |
| magnetic force on conductor | Concept developed in §64.2; use the section definition and stated conditions. |
| Faraday induction | Concept developed in §64.3; use the section definition and stated conditions. |
| magnetic reluctance | Concept developed in §64.4; use the section definition and stated conditions. |
| ideal transformer | Concept developed in §64.5; use the section definition and stated conditions. |
| reflected impedance | Concept developed in §64.6; use the section definition and stated conditions. |
| three-phase transformer connection | Concept developed in §64.7; use the section definition and stated conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **magnetic flux** and state its governing equation or condition.

2. Define **magnetic force on conductor** and state its governing equation or condition.

3. Define **Faraday induction** and state its governing equation or condition.

4. Define **magnetic reluctance** and state its governing equation or condition.

5. Define **ideal transformer** and state its governing equation or condition.

6. Define **reflected impedance** and state its governing equation or condition.

7. Define **three-phase transformer connection** and state its governing equation or condition.

8. What is a common analysis error involving **magnetic flux**?

9. What is a common analysis error involving **magnetic force on conductor**?

10. What is a common analysis error involving **Faraday induction**?

11. What is a common analysis error involving **magnetic reluctance**?

12. What is a common analysis error involving **ideal transformer**?

13. What is a common analysis error involving **reflected impedance**?

14. What is a common analysis error involving **three-phase transformer connection**?

15. Why must voltage polarity and current direction be defined before using signed power?

16. What conservation principle should be used as an independent circuit or machine check?

17. When should a Handbook equation be preferred over a remembered shortcut?

18. Why should RMS and peak values not be mixed in AC power or impedance calculations?

### Multiple Choice

19. Which statement is most accurate for **magnetic flux**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

20. Which statement is most accurate for **magnetic force on conductor**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

21. Which statement is most accurate for **Faraday induction**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

22. Which statement is most accurate for **magnetic reluctance**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

23. Which statement is most accurate for **ideal transformer**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

24. Which statement is most accurate for **reflected impedance**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

25. Which statement is most accurate for **three-phase transformer connection**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

26. Which statement is most accurate for **magnetic flux**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

27. Which statement is most accurate for **magnetic force on conductor**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **magnetic flux** is developed in §64.1. Use the displayed relation together with its stated sign convention and assumptions.

2. **magnetic force on conductor** is developed in §64.2. Use the displayed relation together with its stated sign convention and assumptions.

3. **Faraday induction** is developed in §64.3. Use the displayed relation together with its stated sign convention and assumptions.

4. **magnetic reluctance** is developed in §64.4. Use the displayed relation together with its stated sign convention and assumptions.

5. **ideal transformer** is developed in §64.5. Use the displayed relation together with its stated sign convention and assumptions.

6. **reflected impedance** is developed in §64.6. Use the displayed relation together with its stated sign convention and assumptions.

7. **three-phase transformer connection** is developed in §64.7. Use the displayed relation together with its stated sign convention and assumptions.

8. Applying **magnetic flux** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

9. Applying **magnetic force on conductor** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

10. Applying **Faraday induction** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

11. Applying **magnetic reluctance** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

12. Applying **ideal transformer** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

13. Applying **reflected impedance** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

14. Applying **three-phase transformer connection** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

15. Because the sign of power depends on the chosen voltage/current references and the passive sign convention.

16. Charge/KCL, energy/power balance, and where applicable KVL should close consistently.

17. Whenever the Handbook supplies the relation or when the shortcut's assumptions are uncertain.

18. They represent different magnitudes; mixing them introduces factors such as √2 and gives incorrect power.

19. **A.** The chapter treats **magnetic flux** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

20. **A.** The chapter treats **magnetic force on conductor** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

21. **A.** The chapter treats **Faraday induction** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

22. **A.** The chapter treats **magnetic reluctance** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

23. **A.** The chapter treats **ideal transformer** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

24. **A.** The chapter treats **reflected impedance** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

25. **A.** The chapter treats **three-phase transformer connection** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

26. **A.** The chapter treats **magnetic flux** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

27. **A.** The chapter treats **magnetic force on conductor** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.


---

## Practice Problems

1. A linear magnetic material has μ=2.0×10^-3 H/m and H=500 A/m. Find B.

2. A 0.50 m conductor carries 10 A perpendicular to B=0.8 T. Find force.

3. A 200-turn coil experiences flux change 3 mWb to 1 mWb in 0.01 s. Find induced-voltage magnitude.

4. A magnetic path has l=0.20 m, μ=1.0×10^-3 H/m, A=4×10^-4 m². Find reluctance.

5. An ideal transformer has NP=1000, NS=250, VP=480 V. Find VS.

6. For the transformer in Problem 5, a 12 Ω secondary load is connected. Find reflected primary impedance.

7. Name the four common three-phase transformer connection families shown in the Handbook.

8. An ideal transformer has VP/VS=5. If secondary current is 10 A, find primary current.

9. If a core air gap is added, what usually happens to reluctance?

10. What does the negative sign in Faraday's law represent?


---

## Practice Problem Solutions

1. B=μH=1.0 T.

2. F=ILB=4 N.

3. |v|=N|ΔΦ/Δt|=200(0.002/0.01)=40 V.

4. Rmag=l/(μA)=5.0×10^5 H^-1.

5. a=4; VS=120 V.

6. ZP=a²ZS=16×12=192 Ω.

7. Wye-wye, wye-delta, delta-wye, delta-delta.

8. IP=IS/5=2 A.

9. It increases strongly because air permeability is much lower.

10. Lenz's law: induced effects oppose the change in flux.


---

## Quick Reference

**Handbook anchor:** Electrical and Computer Engineering, printed pp. 362, 364, and 369–370.

- **magnetic flux:** Magnetic Field, Flux Density, and Permeability
- **magnetic force on conductor:** Force on a Current-Carrying Conductor
- **Faraday induction:** Faraday's Law and Lenz's Law
- **magnetic reluctance:** Reluctance, Flux Linkage, and Inductance
- **ideal transformer:** Ideal Transformer Turns and Current Ratios
- **reflected impedance:** Reflected Impedance
- **three-phase transformer connection:** Three-Phase Transformer Connections
---

## What's Next

**02-65 — Motors, Generators, and Electromechanical Energy Conversion**

Carry forward the electrical workflow: define voltage/current references and topology, choose the correct DC/AC or transient model, apply the Handbook relation, and close with conservation and power checks.

— Your Mentor