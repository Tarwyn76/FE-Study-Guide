---
chapter: "02-59"
title: "Electrical Quantities, Ohm's Law, and DC Power"
layer: 2
tier: E
template: technical
ledger_ids: [ELEC-2E-059-01, ELEC-2E-059-02, ELEC-2E-059-03, ELEC-2E-059-04, ELEC-2E-059-05, ELEC-2E-059-06, ELEC-2E-059-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-59: Electrical Quantities, Ohm's Law, and DC Power

> *"Electrical problems become much easier when references, topology, energy flow, and the correct steady-state or transient model are established before algebra."*

---

## Before You Start

**Prerequisites:** 01-02 Units and Dimensions · 02-17 Material Properties and Engineering Selection

**Skip if:** You can identify the governing electrical model, choose correct voltage/current references, use the FE Handbook relation, solve representative FE-level calculations, and verify power, units, and physical behavior.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly defines electrical units, voltage, current, magnetic/electric field context, resistivity, resistance, temperature dependence, Ohm's law, and resistive power relations. Sign-convention and source/load interpretation are guide-developed applications.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **59.1** Explain and apply **Charge and Electric Current**.
* **59.2** Explain and apply **Voltage and Electric Potential Difference**.
* **59.3** Explain and apply **Resistance, Resistivity, and Conductance**.
* **59.4** Explain and apply **Ohm's Law and the Passive Sign Convention**.
* **59.5** Explain and apply **Temperature Dependence of Resistance**.
* **59.6** Explain and apply **DC Power in Resistive Elements**.
* **59.7** Explain and apply **Electrical Energy and Source-Load Checks**.

---

## Notation Used Here

Voltage polarities and current directions are reference choices. RMS quantities are used for AC power unless otherwise stated. Use SI units unless a problem explicitly supplies another system.

---

## 59.1 Charge and Electric Current

Electric charge is measured in coulombs. Current is the time rate of charge transport through a surface. A constant current is written \(I\); a time-varying current is \(i(t)\).

Conventional current direction follows positive-charge motion. Electron drift in metals is opposite conventional current, but circuit analysis normally uses conventional current.

\[i(t)=\frac{dq(t)}{dt}\]

![FIG-02-59-001: Conductor cross-section with conventional current direction, electron drift direction, and charge crossing a reference surface.](../figures/FIG-02-59-001-charge-and-electric-current.png)

### Worked Example 1

**Problem.** A steady current of 2 A flows for 15 s. How much charge passes a reference surface?

**Solution.** q=It=30 C.

---

## 59.2 Voltage and Electric Potential Difference

Voltage is energy or work per unit charge between two points. It is always defined between two nodes and therefore requires a polarity reference.

A positive value means the named positive terminal is at higher electric potential than the named negative terminal according to the chosen reference.

\[V=\frac{W}{Q}\]

![FIG-02-59-002: Two circuit nodes with polarity marks and voltage defined as work per unit charge.](../figures/FIG-02-59-002-voltage-and-electric-potential-difference.png)

### Worked Example 2

**Problem.** Moving 24 J of energy per 3 C of charge requires what voltage?

**Solution.** V=W/Q=8 V.

---

## 59.3 Resistance, Resistivity, and Conductance

Resistance relates material resistivity and geometry. For a uniform conductor, longer length increases resistance and larger cross-sectional area decreases it. Conductance is the reciprocal of resistance.

Resistivity is a material property; resistance is a property of a specific piece of material and geometry.

\[R=\rho\frac{L}{A},\qquad G=\frac{1}{R}\]

![FIG-02-59-003: Uniform conductor labeled length L, area A, resistivity rho, resistance R, and conductance G.](../figures/FIG-02-59-003-resistance-resistivity-and-conductance.png)

### Worked Example 3

**Problem.** Copper wire has ρ=1.72×10^-8 Ω·m, L=10 m, A=1.0 mm². Find resistance.

**Solution.** A=1.0×10^-6 m²; R=ρL/A=0.172 Ω.

---

## 59.4 Ohm's Law and the Passive Sign Convention

For an ohmic resistor, voltage and current are related linearly by \(V=IR\). The passive sign convention places current entering the terminal marked positive for the element voltage.

Under the passive convention, positive \(p=vi\) means the element absorbs power. If current enters the negative terminal, the element delivers power under the same voltage reference.

\[V=IR,\qquad p=vi\]

![FIG-02-59-004: Resistor shown with passive sign convention and alternative source-delivery current direction.](../figures/FIG-02-59-004-ohm-s-law-and-the-passive-sign-convention.png)

### Worked Example 4

**Problem.** A 12 V source is applied to a 6 Ω resistor. Find current.

**Solution.** I=V/R=2 A.

---

## 59.5 Temperature Dependence of Resistance

For metallic conductors over the range represented by the Handbook relation, resistance changes approximately linearly with temperature using a temperature coefficient \(\alpha\).

Use the stated reference resistance \(R_0\) and reference temperature \(T_0\). The linear relation is an approximation over an appropriate temperature range.

\[R=R_0\left[1+\alpha(T-T_0)\right]\]

![FIG-02-59-005: Resistance versus temperature for a metallic conductor with reference point R0 at T0 and slope set by alpha.](../figures/FIG-02-59-005-temperature-dependence-of-resistance.png)

### Worked Example 5

**Problem.** A 10 Ω resistor at 20°C has α=0.004/°C. Estimate resistance at 70°C.

**Solution.** R=10[1+0.004(50)]=12 Ω.

---

## 59.6 DC Power in Resistive Elements

Electrical power is the rate of energy transfer. Combining \(P=VI\) with Ohm's law gives convenient resistor forms.

Use \(I^2R\) or \(V^2/R\) only when \(V\) and \(I\) refer to the same resistor.

\[P=VI=I^2R=\frac{V^2}{R}\]

![FIG-02-59-006: Resistor with voltage/current labels and three equivalent DC power expressions.](../figures/FIG-02-59-006-dc-power-in-resistive-elements.png)

### Worked Example 6

**Problem.** A 24 V load draws 3 A. Find power.

**Solution.** P=VI=72 W.

---

## 59.7 Electrical Energy and Source-Load Checks

Energy delivered or absorbed over time is the integral of power. For constant DC power, \(E=Pt\).

A source can absorb or deliver power depending on operating condition. Always use reference polarity and current direction rather than assuming a labeled 'source' must be delivering energy.

\[E=\int p(t)\,dt,\qquad E=Pt\ \text{for constant DC power}\]

![FIG-02-59-007: DC source and load with signed power arrows showing delivered and absorbed energy.](../figures/FIG-02-59-007-electrical-energy-and-source-load-checks.png)

### Worked Example 7

**Problem.** A 100 W load runs 5 h. Find energy in kWh and joules.

**Solution.** 0.500 kWh = 1.80 MJ.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A 4 Ω resistor carries 5 A. Find power by I²R.

**Solution.** P=25×4=100 W.

### Worked Example 9

**Problem.** A 20 Ω resistor has 10 V across it. Find power by V²/R.

**Solution.** P=100/20=5 W.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Electrical and Computer Engineering, printed pp. 361–363**.

**Source boundary:** The Handbook directly defines electrical units, voltage, current, magnetic/electric field context, resistivity, resistance, temperature dependence, Ohm's law, and resistive power relations. Sign-convention and source/load interpretation are guide-developed applications.

---

## Where This Goes Wrong

**Using electric charge and current without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using electric potential difference without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using electrical resistance without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using Ohm's law without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using resistance temperature coefficient without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using resistive DC power without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Using electrical energy balance without the required reference or assumptions.** Check polarity/current direction, topology, frequency or time-domain condition, and whether the component/model is idealized.

**Skipping a power or conservation check.** A circuit solution should satisfy KCL/KVL where applicable and should not create unexplained power.


---

## Key Terms

| Term | Working definition |
|---|---|
| electric charge and current | Concept developed in §59.1; use the section definition and stated conditions. |
| electric potential difference | Concept developed in §59.2; use the section definition and stated conditions. |
| electrical resistance | Concept developed in §59.3; use the section definition and stated conditions. |
| Ohm's law | Concept developed in §59.4; use the section definition and stated conditions. |
| resistance temperature coefficient | Concept developed in §59.5; use the section definition and stated conditions. |
| resistive DC power | Concept developed in §59.6; use the section definition and stated conditions. |
| electrical energy balance | Concept developed in §59.7; use the section definition and stated conditions. |

---

## Review Questions

### Conceptual and Applied

1. Define **electric charge and current** and state its governing equation or condition.

2. Define **electric potential difference** and state its governing equation or condition.

3. Define **electrical resistance** and state its governing equation or condition.

4. Define **Ohm's law** and state its governing equation or condition.

5. Define **resistance temperature coefficient** and state its governing equation or condition.

6. Define **resistive DC power** and state its governing equation or condition.

7. Define **electrical energy balance** and state its governing equation or condition.

8. What is a common analysis error involving **electric charge and current**?

9. What is a common analysis error involving **electric potential difference**?

10. What is a common analysis error involving **electrical resistance**?

11. What is a common analysis error involving **Ohm's law**?

12. What is a common analysis error involving **resistance temperature coefficient**?

13. What is a common analysis error involving **resistive DC power**?

14. What is a common analysis error involving **electrical energy balance**?

15. Why must voltage polarity and current direction be defined before using signed power?

16. What conservation principle should be used as an independent circuit or machine check?

17. When should a Handbook equation be preferred over a remembered shortcut?

18. Why should RMS and peak values not be mixed in AC power or impedance calculations?

### Multiple Choice

19. Which statement is most accurate for **electric charge and current**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

20. Which statement is most accurate for **electric potential difference**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

21. Which statement is most accurate for **electrical resistance**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

22. Which statement is most accurate for **Ohm's law**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

23. Which statement is most accurate for **resistance temperature coefficient**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

24. Which statement is most accurate for **resistive DC power**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

25. Which statement is most accurate for **electrical energy balance**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

26. Which statement is most accurate for **electric charge and current**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws

27. Which statement is most accurate for **electric potential difference**?
A) It must be used with its defined reference and assumptions
B) It is independent of topology and frequency
C) It always represents a scalar DC quantity
D) It replaces conservation laws


---

## Answer Key with Explanations

1. **electric charge and current** is developed in §59.1. Use the displayed relation together with its stated sign convention and assumptions.

2. **electric potential difference** is developed in §59.2. Use the displayed relation together with its stated sign convention and assumptions.

3. **electrical resistance** is developed in §59.3. Use the displayed relation together with its stated sign convention and assumptions.

4. **Ohm's law** is developed in §59.4. Use the displayed relation together with its stated sign convention and assumptions.

5. **resistance temperature coefficient** is developed in §59.5. Use the displayed relation together with its stated sign convention and assumptions.

6. **resistive DC power** is developed in §59.6. Use the displayed relation together with its stated sign convention and assumptions.

7. **electrical energy balance** is developed in §59.7. Use the displayed relation together with its stated sign convention and assumptions.

8. Applying **electric charge and current** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

9. Applying **electric potential difference** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

10. Applying **electrical resistance** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

11. Applying **Ohm's law** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

12. Applying **resistance temperature coefficient** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

13. Applying **resistive DC power** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

14. Applying **electrical energy balance** without checking topology, reference direction, steady/transient condition, RMS/peak basis, or machine/circuit assumptions can produce a formally calculated but physically wrong result.

15. Because the sign of power depends on the chosen voltage/current references and the passive sign convention.

16. Charge/KCL, energy/power balance, and where applicable KVL should close consistently.

17. Whenever the Handbook supplies the relation or when the shortcut's assumptions are uncertain.

18. They represent different magnitudes; mixing them introduces factors such as √2 and gives incorrect power.

19. **A.** The chapter treats **electric charge and current** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

20. **A.** The chapter treats **electric potential difference** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

21. **A.** The chapter treats **electrical resistance** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

22. **A.** The chapter treats **Ohm's law** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

23. **A.** The chapter treats **resistance temperature coefficient** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

24. **A.** The chapter treats **resistive DC power** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

25. **A.** The chapter treats **electrical energy balance** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

26. **A.** The chapter treats **electric charge and current** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.

27. **A.** The chapter treats **electric potential difference** as valid only with the required reference directions, circuit topology, frequency/state assumptions, and units.


---

## Practice Problems

1. A steady current of 2 A flows for 15 s. How much charge passes a reference surface?

2. Moving 24 J of energy per 3 C of charge requires what voltage?

3. Copper wire has ρ=1.72×10^-8 Ω·m, L=10 m, A=1.0 mm². Find resistance.

4. A 12 V source is applied to a 6 Ω resistor. Find current.

5. A 10 Ω resistor at 20°C has α=0.004/°C. Estimate resistance at 70°C.

6. A 24 V load draws 3 A. Find power.

7. A 100 W load runs 5 h. Find energy in kWh and joules.

8. A 4 Ω resistor carries 5 A. Find power by I²R.

9. A 20 Ω resistor has 10 V across it. Find power by V²/R.

10. Under the passive sign convention, p=-50 W. Is the element absorbing or delivering power?


---

## Practice Problem Solutions

1. q=It=30 C.

2. V=W/Q=8 V.

3. A=1.0×10^-6 m²; R=ρL/A=0.172 Ω.

4. I=V/R=2 A.

5. R=10[1+0.004(50)]=12 Ω.

6. P=VI=72 W.

7. 0.500 kWh = 1.80 MJ.

8. P=25×4=100 W.

9. P=100/20=5 W.

10. Delivering 50 W.


---

## Quick Reference

**Handbook anchor:** Electrical and Computer Engineering, printed pp. 361–363.

- **electric charge and current:** Charge and Electric Current
- **electric potential difference:** Voltage and Electric Potential Difference
- **electrical resistance:** Resistance, Resistivity, and Conductance
- **Ohm's law:** Ohm's Law and the Passive Sign Convention
- **resistance temperature coefficient:** Temperature Dependence of Resistance
- **resistive DC power:** DC Power in Resistive Elements
- **electrical energy balance:** Electrical Energy and Source-Load Checks
---

## What's Next

**02-60 — Kirchhoff's Laws and Resistive Circuit Analysis**

Carry forward the electrical workflow: define voltage/current references and topology, choose the correct DC/AC or transient model, apply the Handbook relation, and close with conservation and power checks.

— Your Mentor