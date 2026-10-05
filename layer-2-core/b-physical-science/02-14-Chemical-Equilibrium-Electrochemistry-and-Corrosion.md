---
chapter: "02-14"
title: "Chemical Equilibrium, Electrochemistry, and Corrosion"
layer: 2
tier: B
template: technical
ledger_ids: [SCI-2B-014-01, SCI-2B-014-02, SCI-2B-014-03, SCI-2B-014-04, SCI-2B-014-05, SCI-2B-014-06, SCI-2B-014-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-14: Chemical Equilibrium, Electrochemistry, and Corrosion

> *"Physical science becomes engineering when the microscopic model, measured property, and safety consequence are connected explicitly."*

---

## Before You Start

**Prerequisites:** 02-13

**Skip if:** You can solve the calculation and scenario checks in this chapter while stating the assumptions and Handbook source used.

**Time:** About 85–115 min reading and worked examples · 40–50 min review questions · 60–80 min practice problems.

---

## On the Board Today

The Handbook directly provides equilibrium-constant structure, catalyst note, Ksp, Faraday's equation, Nernst equation, electrochemical definitions and standard oxidation potentials, and corrosion-cell requirements. Le Chatelier interpretation and corrosion-control examples are guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **14.1** Explain and apply **Chemical Equilibrium and the Equilibrium Constant**.
* **14.2** Explain and apply **Disturbance, Temperature, and Catalysts**.
* **14.3** Explain and apply **Oxidation and Reduction**.
* **14.4** Explain and apply **Cell Potentials and Spontaneity**.
* **14.5** Explain and apply **The Nernst Equation**.
* **14.6** Explain and apply **Faraday's Equation and Electrolysis**.
* **14.7** Explain and apply **Corrosion Cells and Corrosion Control**.

---

## Notation Used Here

Notation is introduced within each section where needed. Use SI units unless a problem or Handbook table specifies another basis.

---

## 14.1 Chemical Equilibrium and the Equilibrium Constant

For reaction

\[
aA+bB\rightleftharpoons cC+dD,
\]

the Handbook gives an equilibrium-constant form based on thermodynamic activities:

\[
K=\frac{[C]^c[D]^d}{[A]^a[B]^b}.
\]

For dilute solutions, concentration may approximate activity when the problem permits. Pure solids and pure liquids have activity approximately 1 and therefore do not appear explicitly in the concentration-form equilibrium expression.

The value of \(K\) describes the equilibrium composition tendency at the specified temperature; it is not a reaction rate.

![FIG-02-14-001: Reversible reaction with equilibrium-constant numerator/denominator mapping and activity rules for gases, dilute solutes, solids, and liquids.](../figures/FIG-02-14-001-chemical-equilibrium-and-the-equilibrium-constant.png)

### Worked Example 1 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **equilibrium constant** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 14.2 Disturbance, Temperature, and Catalysts

Le Chatelier reasoning predicts the direction a system shifts after concentration, pressure, or temperature changes. This qualitative framework is guide-developed; the Handbook directly notes one especially important point:

> a catalyst changes reaction rate but does not change the position of equilibrium.

A catalyst can help the system reach equilibrium faster, but it does not alter \(K\) at fixed temperature.

Temperature is different because changing temperature changes the thermodynamic equilibrium constant. Treat heat as a reactant for endothermic reactions and as a product for exothermic reactions when using qualitative shift reasoning.

![FIG-02-14-002: Equilibrium response chart for concentration, pressure, temperature, and catalyst, emphasizing that catalysts change rate but not equilibrium position.](../figures/FIG-02-14-002-disturbance-temperature-and-catalysts.png)

### Worked Example 2 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **equilibrium disturbance** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 14.3 Oxidation and Reduction

The Handbook defines:

- **oxidation** — loss of electrons,
- **reduction** — gain of electrons,
- **anode** — electrode where oxidation occurs,
- **cathode** — electrode where reduction occurs.

A memory aid is OIL RIG: Oxidation Is Loss, Reduction Is Gain.

Oxidation states provide bookkeeping for electron transfer. In a balanced redox reaction, electrons lost by oxidation equal electrons gained by reduction.

![FIG-02-14-003: Redox schematic showing electron flow from anode/oxidation half-cell to cathode/reduction half-cell, with OIL RIG callout.](../figures/FIG-02-14-003-oxidation-and-reduction.png)

### Worked Example 3 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **redox** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 14.4 Cell Potentials and Spontaneity

The Handbook's corrosion table lists **standard oxidation potentials** with reactions written as oxidation half-cells. This convention matters because many chemistry texts instead tabulate reduction potentials.

When combining half-cells, reverse the sign if you reverse a tabulated half-reaction. The overall cell potential is the algebraic sum of the selected half-cell potentials using one consistent convention.

A positive cell potential for the overall reaction as written indicates thermodynamic spontaneity under the specified standard-state convention.

![FIG-02-14-004: Galvanic-cell diagram with anode/cathode, electron path, ion bridge, and a sign-convention box contrasting oxidation-potential and reduction-potential tables.](../figures/FIG-02-14-004-cell-potentials-and-spontaneity.png)

### Worked Example 4 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **cell potential** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 14.5 The Nernst Equation

The Handbook gives the Nernst relation for nonstandard electrochemical conditions. In general form,

\[
E=E^\circ-\frac{RT}{nF}\ln Q,
\]

with the reaction quotient \(Q\) constructed from the balanced cell reaction.

The number \(n\) is the number of electrons transferred in the balanced reaction. Do not use an unbalanced half-reaction electron count if the full cell reaction requires multiplication.

Nernst calculations connect concentration, temperature, and cell voltage.

![FIG-02-14-005: Nernst equation annotated with E°, R, T, n, F, and reaction quotient Q, plus a concentration-cell example.](../figures/FIG-02-14-005-the-nernst-equation.png)

### Worked Example 5 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **Nernst equation** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 14.6 Faraday's Equation and Electrolysis

The Handbook gives Faraday's equation in the form

\[
m=\frac{QM}{zF},
\]

where \(m\) is deposited/liberated mass, \(Q\) is charge, \(M\) is molar mass, \(z\) is electron valence number, and

\[
F=96{,}485\ \text{C/mol e}^-.
\]

Because \(Q=It\),

\[
m=\frac{ItM}{zF}.
\]

Check that current is in amperes and time in seconds so charge is coulombs.

![FIG-02-14-006: Electrolysis calculation chain current × time -> charge -> moles of electrons -> moles of deposited species -> mass.](../figures/FIG-02-14-006-faraday-s-equation-and-electrolysis.png)

### Worked Example 6 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **Faraday electrolysis** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 14.7 Corrosion Cells and Corrosion Control

The Materials Science section states that corrosion requires an anode and cathode in electrical contact in the presence of an electrolyte.

At the anode, metal oxidation occurs:

\[
M^0\rightarrow M^{n+}+ne^-.
\]

Control strategies interrupt one or more requirements of the corrosion cell or shift electrochemical behavior. Common engineering approaches include coatings, material selection, electrical isolation of dissimilar metals, cathodic protection, inhibitors, and environmental control.

Corrosion control must consider the actual environment; a material resistant to one chemical may fail rapidly in another.

![FIG-02-14-007: Corrosion cell on two dissimilar metals in electrolyte showing anodic metal loss, cathodic reaction, electron path, ion path, and control options such as coating and electrical isolation.](../figures/FIG-02-14-007-corrosion-cells-and-corrosion-control.png)

### Worked Example 7 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **corrosion** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Chemistry and Biology pp. 86–87, 93; Materials Science/Structure of Matter p. 117**.

**Source boundary:** The Handbook directly provides equilibrium-constant structure, catalyst note, Ksp, Faraday's equation, Nernst equation, electrochemical definitions and standard oxidation potentials, and corrosion-cell requirements. Le Chatelier interpretation and corrosion-control examples are guide-developed.

---

## Where This Goes Wrong

**Using equilibrium constant without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using equilibrium disturbance without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using redox without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using cell potential without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using Nernst equation without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using Faraday electrolysis without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using corrosion without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Replacing supplied data with a memorized trend.** If the Handbook or problem gives specific property, potential, limit, or compatibility data, use it.


---

## Key Terms

| Term | Working definition |
|---|---|
| equilibrium constant | Term introduced in this chapter; use the definition and conditions in the owning section. |
| reaction quotient | Term introduced in this chapter; use the definition and conditions in the owning section. |
| Le Chatelier principle | Term introduced in this chapter; use the definition and conditions in the owning section. |
| catalyst | Term introduced in this chapter; use the definition and conditions in the owning section. |
| oxidation | Term introduced in this chapter; use the definition and conditions in the owning section. |
| reduction | Term introduced in this chapter; use the definition and conditions in the owning section. |
| anode | Term introduced in this chapter; use the definition and conditions in the owning section. |
| cathode | Term introduced in this chapter; use the definition and conditions in the owning section. |
| oxidation state | Term introduced in this chapter; use the definition and conditions in the owning section. |
| standard cell potential | Term introduced in this chapter; use the definition and conditions in the owning section. |
| oxidation potential | Term introduced in this chapter; use the definition and conditions in the owning section. |
| Nernst equation | Term introduced in this chapter; use the definition and conditions in the owning section. |
| Faraday constant | Term introduced in this chapter; use the definition and conditions in the owning section. |
| electrolysis mass | Term introduced in this chapter; use the definition and conditions in the owning section. |
| corrosion cell | Term introduced in this chapter; use the definition and conditions in the owning section. |
| galvanic corrosion | Term introduced in this chapter; use the definition and conditions in the owning section. |
| cathodic protection | Term introduced in this chapter; use the definition and conditions in the owning section. |

---

## Review Questions

### Conceptual and Applied

1. Define **equilibrium constant** and state its engineering significance.

2. Define **equilibrium disturbance** and state its engineering significance.

3. Define **redox** and state its engineering significance.

4. Define **cell potential** and state its engineering significance.

5. Define **Nernst equation** and state its engineering significance.

6. Define **Faraday electrolysis** and state its engineering significance.

7. Define **corrosion** and state its engineering significance.

8. What error is likely if **equilibrium constant** is used without checking the problem's state, composition, units, or assumptions?

9. What error is likely if **equilibrium disturbance** is used without checking the problem's state, composition, units, or assumptions?

10. What error is likely if **redox** is used without checking the problem's state, composition, units, or assumptions?

11. What error is likely if **cell potential** is used without checking the problem's state, composition, units, or assumptions?

12. What error is likely if **Nernst equation** is used without checking the problem's state, composition, units, or assumptions?

13. What error is likely if **Faraday electrolysis** is used without checking the problem's state, composition, units, or assumptions?

14. What error is likely if **corrosion** is used without checking the problem's state, composition, units, or assumptions?

15. Identify one Handbook table, equation, or definition you would locate before solving a representative problem from this chapter.

16. State one physical-reasonableness or dimensional check appropriate to this chapter.

17. Explain when measured or tabulated data should replace a qualitative trend.

18. Give one example of an interpretation in this chapter that is guide-developed rather than a verbatim Handbook rule.

### Multiple Choice

19. Which answer best describes **equilibrium constant**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

20. Which answer best describes **equilibrium disturbance**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

21. Which answer best describes **redox**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

22. Which answer best describes **cell potential**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

23. Which answer best describes **Nernst equation**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

24. Which answer best describes **Faraday electrolysis**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

25. Which answer best describes **corrosion**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

26. Which answer best describes **equilibrium constant**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

27. Which answer best describes **equilibrium disturbance**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data


---

## Answer Key with Explanations

1. **equilibrium constant** is the central concept of §14.1; apply the definition, assumptions, and engineering consequence developed in that section.

2. **equilibrium disturbance** is the central concept of §14.2; apply the definition, assumptions, and engineering consequence developed in that section.

3. **redox** is the central concept of §14.3; apply the definition, assumptions, and engineering consequence developed in that section.

4. **cell potential** is the central concept of §14.4; apply the definition, assumptions, and engineering consequence developed in that section.

5. **Nernst equation** is the central concept of §14.5; apply the definition, assumptions, and engineering consequence developed in that section.

6. **Faraday electrolysis** is the central concept of §14.6; apply the definition, assumptions, and engineering consequence developed in that section.

7. **corrosion** is the central concept of §14.7; apply the definition, assumptions, and engineering consequence developed in that section.

8. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

9. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

10. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

11. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

12. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

13. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

14. The wrong model or data may be applied. The section requires checking the governing conditions before calculation or qualitative prediction.

15. Use the Handbook source identified in the chapter, then verify dimensions/physical bounds; supplied data controls over remembered trends. Guide-developed interpretations are explicitly identified in the source-boundary note.

16. Use the Handbook source identified in the chapter, then verify dimensions/physical bounds; supplied data controls over remembered trends. Guide-developed interpretations are explicitly identified in the source-boundary note.

17. Use the Handbook source identified in the chapter, then verify dimensions/physical bounds; supplied data controls over remembered trends. Guide-developed interpretations are explicitly identified in the source-boundary note.

18. Use the Handbook source identified in the chapter, then verify dimensions/physical bounds; supplied data controls over remembered trends. Guide-developed interpretations are explicitly identified in the source-boundary note.

19. **A.** The chapter applies **equilibrium constant** only under its stated physical/model assumptions.

20. **A.** The chapter applies **equilibrium disturbance** only under its stated physical/model assumptions.

21. **A.** The chapter applies **redox** only under its stated physical/model assumptions.

22. **A.** The chapter applies **cell potential** only under its stated physical/model assumptions.

23. **A.** The chapter applies **Nernst equation** only under its stated physical/model assumptions.

24. **A.** The chapter applies **Faraday electrolysis** only under its stated physical/model assumptions.

25. **A.** The chapter applies **corrosion** only under its stated physical/model assumptions.

26. **A.** The chapter applies **equilibrium constant** only under its stated physical/model assumptions.

27. **A.** The chapter applies **equilibrium disturbance** only under its stated physical/model assumptions.


---

## Practice Problems

1. 1. For A ⇌ B with K=[B]/[A], if [A]=0.20 and [B]=0.80 at equilibrium, find K.

2. 2. Does a catalyst change the equilibrium constant at fixed temperature?

3. 3. Identify oxidation and reduction in Zn → Zn2+ + 2e− and Cu2+ + 2e− → Cu.

4. 4. If E°oxidation(Zn)=+0.763 V and E°reduction(Cu)=+0.337 V, find E°cell using consistent signs.

5. 5. In the Nernst equation, what does n represent?

6. 6. A 2.0 A current flows for 30 min. Find charge Q.

7. 7. Using Q from Problem 6, Cu2+ plating (z=2), M=63.546 g/mol, F=96485 C/mol, find deposited Cu mass.

8. 8. State the three physical requirements for an electrochemical corrosion cell emphasized by the Handbook.

9. 9. Which metal is sacrificed in galvanic corrosion: the anode or cathode?

10. 10. Name two corrosion-control strategies that break or alter the corrosion cell.


---

## Practice Problem Solutions

1. 1. K=0.80/0.20=4.

2. 2. No. It changes rate, not equilibrium position/K at fixed temperature.

3. 3. Zn is oxidized; Cu2+ is reduced.

4. 4. E°cell=0.763+0.337=1.100 V.

5. 5. Number of electrons transferred in the balanced cell reaction.

6. 6. Q=It=2.0×(30×60)=3600 C.

7. 7. m=QM/(zF)=3600×63.546/(2×96485)=1.185 g.

8. 8. An anode, a cathode, electrical contact, and an electrolyte are required; the core corrosion-cell conditions include both electrodes electrically connected in electrolyte.

9. 9. The anode is oxidized/consumed.

10. 10. Examples: coating, electrical isolation, cathodic protection, inhibitors, or environmental control.


---

## Quick Reference

**Handbook anchor:** Chemistry and Biology pp. 86–87, 93; Materials Science/Structure of Matter p. 117.

- **equilibrium constant:** Chemical Equilibrium and the Equilibrium Constant
- **equilibrium disturbance:** Disturbance, Temperature, and Catalysts
- **redox:** Oxidation and Reduction
- **cell potential:** Cell Potentials and Spontaneity
- **Nernst equation:** The Nernst Equation
- **Faraday electrolysis:** Faraday's Equation and Electrolysis
- **corrosion:** Corrosion Cells and Corrosion Control

---

## What's Next

**02-15 — Organic Chemistry and Biological Systems**

Carry forward the rule: identify the physical model and service condition before selecting the formula, property, or safety control.

— Your Mentor
