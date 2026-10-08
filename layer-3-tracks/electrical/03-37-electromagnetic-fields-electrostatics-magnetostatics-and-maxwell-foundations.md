---
chapter: "03-37"
title: "Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations"
layer: 3
tier: null
track: electrical_and_computer
template: technical
ledger_ids: [ECE-3-037-01, ECE-3-037-02, ECE-3-037-03, ECE-3-037-04, ECE-3-037-05, ECE-3-037-06, ECE-3-037-07]
routes: [electrical_and_computer]
status: drafted
---

# Chapter 03-37: Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations

> *"Electrical and computer engineering becomes tractable when the abstraction level, operating region, signals, and interfaces are explicit."*

---

## Before You Start

**Prerequisites:** ELEC-2E-064-04

**Route:** FE Electrical and Computer. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct device/system abstraction, choose the governing Handbook relation or specification-required workflow, solve representative FE-level problems, and verify that the result satisfies the assumed operating region or logic/protocol model.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Electrical and Computer material under **Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations**. It builds on the Layer 1 mathematical substrate and Layer 2 circuit, instrumentation, and control foundation rather than reteaching them. Handbook-supported equations are separated from specification-required learned material that is not directly tabulated in Handbook 10.6.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **37.1** Explain and apply **Coulomb force and electric field intensity**.
* **37.2** Explain and apply **Electric flux density, Gauss law, and symmetry**.
* **37.3** Explain and apply **Electric potential, work, capacitance, and stored energy**.
* **37.4** Explain and apply **Magnetic field around currents and force on conductors**.
* **37.5** Explain and apply **Magnetic flux, inductance, and magnetic energy**.
* **37.6** Explain and apply **Faraday law and electromagnetic induction**.
* **37.7** Explain and apply **Maxwell equations as the electromagnetic foundation**.

---

## Notation Used Here

Use the variable definitions local to each section. Distinguish instantaneous, peak, RMS, average, phasor, bit/word, state, and packet quantities. For semiconductor and amplifier calculations, verify the device operating region after solving; for digital/network/software problems, verify the assumed logic, timing, protocol, or data-structure model.

---

## 37.1 Coulomb force and electric field intensity

Electrostatic field problems require direction as well as magnitude. Superposition applies vectorially when multiple charges contribute.

\[\mathbf E=\frac{Q}{4\pi\varepsilon r^2}\mathbf a_r,\qquad \mathbf F=Q_t\mathbf E\]

![FIG-03-37-001: Point charges with electric-field vectors, unit radial direction, and superposition at an observation point.](../figures/FIG-03-37-001-coulomb-force-and-electric-field-intensity.png)

### Worked Example 1

**Problem.** Doubling distance from a point charge reduces field magnitude by a factor of four.

**Solution.** Start from the §37.1 relation \(\mathbf E=\frac{Q}{4\pi\varepsilon r^2}\mathbf a_r,\qquad \mathbf F=Q_t\mathbf E\). The statement follows from the physical or logical meaning of **Coulomb force and electric field intensity**: Doubling distance from a point charge reduces field magnitude by a factor of four. Accept that conclusion only while the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

---

## 37.2 Electric flux density, Gauss law, and symmetry

Gauss law is most useful when symmetry makes field magnitude constant over a suitable Gaussian surface.

\[\oint_S \mathbf D\cdot d\mathbf S=Q_{\text{encl}},\qquad \mathbf D=\varepsilon\mathbf E\]

![FIG-03-37-002: Spherical, cylindrical, and pillbox Gaussian surfaces matched to point, line, and sheet charge symmetries.](../figures/FIG-03-37-002-electric-flux-density-gauss-law-and-symmetry.png)

### Worked Example 2

**Problem.** For a spherically symmetric point charge, choose a spherical Gaussian surface centered on the charge.

**Solution.** Start from the §37.2 relation \(\oint_S \mathbf D\cdot d\mathbf S=Q_{\text{encl}},\qquad \mathbf D=\varepsilon\mathbf E\). The statement follows from the physical or logical meaning of **Electric flux density, Gauss law, and symmetry**: For a spherically symmetric point charge, choose a spherical Gaussian surface centered on the charge. Accept that conclusion only while the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

---

## 37.3 Electric potential, work, capacitance, and stored energy

Potential difference is energy per unit charge. Capacitors store energy in the electric field and geometry/permittivity set capacitance.

\[V_{12}=-\int_1^2 \mathbf E\cdot d\mathbf l,\qquad W_E=\frac12CV^2\]

![FIG-03-37-003: Parallel-plate capacitor with E field, voltage, plate charge, dielectric, and stored-energy callout.](../figures/FIG-03-37-003-electric-potential-work-capacitance-and-stored-energy.png)

### Worked Example 3

**Problem.** A 10-μF capacitor at 20 V stores 2.0 mJ.

**Solution.** Start from the §37.3 relation \(V_{12}=-\int_1^2 \mathbf E\cdot d\mathbf l,\qquad W_E=\frac12CV^2\). Substitute or interpret the stated quantities using that model; the calculation reproduces the stated result: A 10-μF capacitor at 20 V stores 2.0 mJ. Carry the stated units through the calculation and accept the result only after confirming that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

---

## 37.4 Magnetic field around currents and force on conductors

Current creates magnetic field circulation according to the right-hand rule. Magnetic force direction follows the vector cross product.

\[\mathbf H=\frac{I}{2\pi r}\mathbf a_\phi,\qquad \mathbf F=I\mathbf L\times\mathbf B\]

![FIG-03-37-004: Straight conductor with circular H field plus a current-carrying segment in uniform B showing force direction.](../figures/FIG-03-37-004-magnetic-field-around-currents-and-force-on-conductors.png)

### Worked Example 4

**Problem.** Reversing current reverses force direction for a fixed magnetic field.

**Solution.** Start from the §37.4 relation \(\mathbf H=\frac{I}{2\pi r}\mathbf a_\phi,\qquad \mathbf F=I\mathbf L\times\mathbf B\). The statement follows from the physical or logical meaning of **Magnetic field around currents and force on conductors**: Reversing current reverses force direction for a fixed magnetic field. Accept that conclusion only while the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

---

## 37.5 Magnetic flux, inductance, and magnetic energy

Flux linkage connects field quantities to circuit inductance. Core permeability and magnetic path geometry strongly influence inductance.

\[N\Phi=Li,\qquad W_H=\frac12Li^2\]

![FIG-03-37-005: Coil on magnetic core with flux path, reluctance, cross-section, permeability, and flux linkage.](../figures/FIG-03-37-005-magnetic-flux-inductance-and-magnetic-energy.png)

### Worked Example 5

**Problem.** Doubling current doubles flux linkage in a linear inductor and quadruples stored magnetic energy.

**Solution.** Start from the §37.5 relation \(N\Phi=Li,\qquad W_H=\frac12Li^2\). The statement follows from the physical or logical meaning of **Magnetic flux, inductance, and magnetic energy**: Doubling current doubles flux linkage in a linear inductor and quadruples stored magnetic energy. Accept that conclusion only while the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

---

## 37.6 Faraday law and electromagnetic induction

Time-varying magnetic flux induces voltage. The negative sign embodies Lenz's law: induced effects oppose the change that produced them.

\[v=-N\frac{d\Phi}{dt}\]

![FIG-03-37-006: Coil and changing magnetic flux with induced voltage polarity determined by Lenz's law.](../figures/FIG-03-37-006-faraday-law-and-electromagnetic-induction.png)

### Worked Example 6

**Problem.** A constant flux produces zero induced voltage.

**Solution.** Start from the §37.6 relation \(v=-N\frac{d\Phi}{dt}\). The statement follows from the physical or logical meaning of **Faraday law and electromagnetic induction**: A constant flux produces zero induced voltage. Accept that conclusion only while the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

---

## 37.7 Maxwell equations as the electromagnetic foundation

Maxwell's equations unify electrostatics, magnetostatics, induction, and wave propagation. For the FE exam, recognize what each relation says physically and how it links field sources and time variation.

\[\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},\qquad \nabla\times\mathbf H=\mathbf J+\frac{\partial\mathbf D}{\partial t}\]

![FIG-03-37-007: Concept map connecting charges, currents, E, D, B, H, divergence laws, curl laws, and electromagnetic waves.](../figures/FIG-03-37-007-maxwell-equations-as-the-electromagnetic-foundation.png)

### Worked Example 7

**Problem.** A time-varying magnetic field produces a circulating electric field through Faraday's law.

**Solution.** Start from the §37.7 relation \(\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},\qquad \nabla\times\mathbf H=\mathbf J+\frac{\partial\mathbf D}{\partial t}\). The statement follows from the physical or logical meaning of **Maxwell equations as the electromagnetic foundation**: A time-varying magnetic field produces a circulating electric field through Faraday's law. Accept that conclusion only while the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A calculation gives a numerical answer but violates the assumed device region, logic state, or protocol condition. Is the answer valid?

**Solution.** No. In **Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations**, a tidy numerical or logical result is still invalid if it contradicts the model assumptions. A representative failure is a symmetry-based field result used where the geometry does not have the required symmetry. Return to the applicable section, choose the state/model consistent with the solved quantities, recompute if needed, and confirm that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

### Worked Example 9

**Problem.** A remembered formula differs from the expression printed in the FE Reference Handbook. Which should govern an exam solution?

**Solution.** Use the FE Reference Handbook expression and its definitions as the controlling exam reference unless the problem explicitly defines another model. For **Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations**, match symbols, units, reference directions, RMS/peak or digital conventions, and assumptions to the Handbook first. External references support only specification-required learned concepts that the Handbook does not directly develop.

---

## As the Handbook States It

Primary source basis: **FE Electrical and Computer specification Area 11; FE Reference Handbook 10.6 Electrical and Computer Engineering, printed pp. 361–421, with the specific Handbook subsections identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required engineering/computing knowledge that is not fully developed in the Handbook. **Guide synthesis** connects those two bodies of material into exam-oriented explanations and examples; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Griffiths, D. J. (2023). *Introduction to Electrodynamics* (5th ed.). Cambridge University Press. ISBN 978-1-009-39775-9. DOI: 10.1017/9781009397735. Supporting scope: Electrostatics, magnetostatics, induction, Maxwell equations, and electromagnetic waves.

The external references support only the learned/application portion of the specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using electric field intensity outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Gauss law outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using electrostatic potential outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using magnetic field strength outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using magnetic flux linkage outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Faraday law outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Using Maxwell equations outside its model.** Confirm the operating region, frequency/timing range, abstraction level, polarity/sign convention, and units or logic representation before calculation.

**Failing to verify the assumed state after solving.** Diodes/transistors, feedback amplifiers, switching converters, logic circuits, protocols, and algorithms all have state or validity conditions that must be checked.

**Treating every specification topic as a Handbook lookup.** Some ECE topics are explicitly required by the exam specification but are learned concepts rather than formula-table entries.

---

## Key Terms

| Term | Working definition |
|---|---|
| electric field intensity | Concept developed in §37.1; apply with that section's stated model and conventions. |
| Gauss law | Concept developed in §37.2; apply with that section's stated model and conventions. |
| electrostatic potential | Concept developed in §37.3; apply with that section's stated model and conventions. |
| magnetic field strength | Concept developed in §37.4; apply with that section's stated model and conventions. |
| magnetic flux linkage | Concept developed in §37.5; apply with that section's stated model and conventions. |
| Faraday law | Concept developed in §37.6; apply with that section's stated model and conventions. |
| Maxwell equations | Concept developed in §37.7; apply with that section's stated model and conventions. |

---

## Review Questions

### Conceptual and Applied

1. Define **electric field intensity** and identify the governing relation, state variable, or decision it organizes.

2. Define **Gauss law** and identify the governing relation, state variable, or decision it organizes.

3. Define **electrostatic potential** and identify the governing relation, state variable, or decision it organizes.

4. Define **magnetic field strength** and identify the governing relation, state variable, or decision it organizes.

5. Define **magnetic flux linkage** and identify the governing relation, state variable, or decision it organizes.

6. Define **Faraday law** and identify the governing relation, state variable, or decision it organizes.

7. Define **Maxwell equations** and identify the governing relation, state variable, or decision it organizes.

8. What assumption, operating region, unit convention, or model limitation must be checked before using **electric field intensity**?

9. What assumption, operating region, unit convention, or model limitation must be checked before using **Gauss law**?

10. What assumption, operating region, unit convention, or model limitation must be checked before using **electrostatic potential**?

11. What assumption, operating region, unit convention, or model limitation must be checked before using **magnetic field strength**?

12. What assumption, operating region, unit convention, or model limitation must be checked before using **magnetic flux linkage**?

13. What assumption, operating region, unit convention, or model limitation must be checked before using **Faraday law**?

14. What assumption, operating region, unit convention, or model limitation must be checked before using **Maxwell equations**?

15. Why should an electrical/computer engineering model be checked for its operating region or abstraction level before calculation?

16. When the FE Reference Handbook supplies a relation, why should its exact variable definitions and unit convention govern the exam solution?

17. What is the difference between a physically impossible numerical answer and a mathematically consistent one?

18. Why is an independent limiting-case or order-of-magnitude check useful?

### Multiple Choice

19. Which statement is most accurate for **electric field intensity**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

20. Which statement is most accurate for **Gauss law**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

21. Which statement is most accurate for **electrostatic potential**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

22. Which statement is most accurate for **magnetic field strength**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

23. Which statement is most accurate for **magnetic flux linkage**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

24. Which statement is most accurate for **Faraday law**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

25. Which statement is most accurate for **Maxwell equations**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

26. Which statement is most accurate for **electric field intensity**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept

27. Which statement is most accurate for **Gauss law**?
A) It must be applied within its stated model, operating region, and unit/logic conventions
B) It is independent of boundary conditions and abstraction level
C) It replaces conservation, circuit laws, or logic definitions
D) It is always only a qualitative concept


---

## Answer Key with Explanations

1. **electric field intensity** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

2. **Gauss law** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

3. **electrostatic potential** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

4. **magnetic field strength** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

5. **magnetic flux linkage** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

6. **Faraday law** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

7. **Maxwell equations** is developed in the matching numbered section. Use its displayed relation or state/logic definition only under the stated assumptions.

8. For **electric field intensity**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

9. For **Gauss law**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

10. For **electrostatic potential**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

11. For **magnetic field strength**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

12. For **magnetic flux linkage**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

13. For **Faraday law**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

14. For **Maxwell equations**, verify operating region/model validity, units or logic levels, sign/polarity convention, and loading or boundary conditions before accepting the result.

15. In Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations, the same equation or symbol can change meaning when the operating state, abstraction, timing model, or signal convention changes; verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

16. The FE Reference Handbook is the exam reference for Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations. Match its variable definitions and conventions before substitution; external references support only learned material not developed in the Handbook.

17. An algebraically consistent answer can still be invalid in Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations. Reject a result that implies a symmetry-based field result used where the geometry does not have the required symmetry and reselect the appropriate model or state.

18. A useful independent check for this chapter is to increase distance from an isolated point source and verify the inverse-square electric-field trend. If the result does not reduce correctly, recheck the model, sign convention, and arithmetic.

19. **A.** For **Coulomb force and electric field intensity**, the governing section model is \(\mathbf E=\frac{Q}{4\pi\varepsilon r^2}\mathbf a_r,\qquad \mathbf F=Q_t\mathbf E\). Apply it only with the definitions and assumptions stated in §37.1, then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

20. **A.** For **Electric flux density, Gauss law, and symmetry**, the governing section model is \(\oint_S \mathbf D\cdot d\mathbf S=Q_{\text{encl}},\qquad \mathbf D=\varepsilon\mathbf E\). Apply it only with the definitions and assumptions stated in §37.2, then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

21. **A.** For **Electric potential, work, capacitance, and stored energy**, the governing section model is \(V_{12}=-\int_1^2 \mathbf E\cdot d\mathbf l,\qquad W_E=\frac12CV^2\). Apply it only with the definitions and assumptions stated in §37.3, then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

22. **A.** For **Magnetic field around currents and force on conductors**, the governing section model is \(\mathbf H=\frac{I}{2\pi r}\mathbf a_\phi,\qquad \mathbf F=I\mathbf L\times\mathbf B\). Apply it only with the definitions and assumptions stated in §37.4, then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

23. **A.** For **Magnetic flux, inductance, and magnetic energy**, the governing section model is \(N\Phi=Li,\qquad W_H=\frac12Li^2\). Apply it only with the definitions and assumptions stated in §37.5, then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

24. **A.** For **Faraday law and electromagnetic induction**, the governing section model is \(v=-N\frac{d\Phi}{dt}\). Apply it only with the definitions and assumptions stated in §37.6, then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

25. **A.** For **Maxwell equations as the electromagnetic foundation**, the governing section model is \(\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},\qquad \nabla\times\mathbf H=\mathbf J+\frac{\partial\mathbf D}{\partial t}\). Apply it only with the definitions and assumptions stated in §37.7, then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

26. **A.** For an integrated Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations problem, separate the physical/logical model from the arithmetic, solve with the relevant section relations, and cross-check the result against the chapter-specific validity conditions.

27. **A.** In **Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations**, the source boundary is explicit: FE-Handbook-supported material remains tied to the ledger, externally supported material uses the chapter references for electrostatic, magnetic, and Maxwell-field foundations (GRIFFITHS), and guide synthesis is identified as supplemental explanation rather than Handbook text.


---

## Practice Problems

1. Doubling distance from a point charge reduces field magnitude by a factor of four.

2. For a spherically symmetric point charge, choose a spherical Gaussian surface centered on the charge.

3. A 10-μF capacitor at 20 V stores 2.0 mJ.

4. Reversing current reverses force direction for a fixed magnetic field.

5. Doubling current doubles flux linkage in a linear inductor and quadruples stored magnetic energy.

6. A constant flux produces zero induced voltage.

7. A time-varying magnetic field produces a circulating electric field through Faraday's law.

8. State one model-validity check that should be made before accepting an answer in this chapter.

9. Identify the FE Reference Handbook subsection or specification area you would consult first for this chapter.

10. Give one limiting-case, timing, logic, or order-of-magnitude check that can reveal a bad solution.


---

## Practice Problem Solutions

1. **Independent check for §37.1.** Begin independently with \(\mathbf E=\frac{Q}{4\pi\varepsilon r^2}\mathbf a_r,\qquad \mathbf F=Q_t\mathbf E\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Doubling distance from a point charge reduces field magnitude by a factor of four. Then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

2. **Independent check for §37.2.** Begin independently with \(\oint_S \mathbf D\cdot d\mathbf S=Q_{\text{encl}},\qquad \mathbf D=\varepsilon\mathbf E\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: For a spherically symmetric point charge, choose a spherical Gaussian surface centered on the charge. Then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

3. **Independent check for §37.3.** Begin independently with \(V_{12}=-\int_1^2 \mathbf E\cdot d\mathbf l,\qquad W_E=\frac12CV^2\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A 10-μF capacitor at 20 V stores 2.0 mJ. Then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

4. **Independent check for §37.4.** Begin independently with \(\mathbf H=\frac{I}{2\pi r}\mathbf a_\phi,\qquad \mathbf F=I\mathbf L\times\mathbf B\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Reversing current reverses force direction for a fixed magnetic field. Then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

5. **Independent check for §37.5.** Begin independently with \(N\Phi=Li,\qquad W_H=\frac12Li^2\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: Doubling current doubles flux linkage in a linear inductor and quadruples stored magnetic energy. Then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

6. **Independent check for §37.6.** Begin independently with \(v=-N\frac{d\Phi}{dt}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A constant flux produces zero induced voltage. Then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

7. **Independent check for §37.7.** Begin independently with \(\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},\qquad \nabla\times\mathbf H=\mathbf J+\frac{\partial\mathbf D}{\partial t}\), rather than copying the worked-example conclusion. Applying it to the practice statement gives the same result or interpretation: A time-varying magnetic field produces a circulating electric field through Faraday's law. Then verify that the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

8. Check the chapter-specific failure mode first: a symmetry-based field result used where the geometry does not have the required symmetry. Do not accept the numerical or logical result until the stated field symmetry, material assumptions, orientation, and SI units match the electromagnetic model.

9. For **Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations**, start with the FE Electrical and Computer specification/Handbook location recorded in the ledger, then use the chapter's reconciled source set for electrostatic, magnetic, and Maxwell-field foundations (GRIFFITHS) when the concept is split-required. That preserves the Handbook-versus-learned-material boundary.

10. Use this limiting check: increase distance from an isolated point source and verify the inverse-square electric-field trend. The simplified case should produce the expected physical, timing, logic, protocol, or complexity behavior before the full solution is trusted.

---

## Quick Reference

**Source anchor:** FE Electrical and Computer specification Area 11.

- **electric field intensity:** Coulomb force and electric field intensity
- **Gauss law:** Electric flux density, Gauss law, and symmetry
- **electrostatic potential:** Electric potential, work, capacitance, and stored energy
- **magnetic field strength:** Magnetic field around currents and force on conductors
- **magnetic flux linkage:** Magnetic flux, inductance, and magnetic energy
- **Faraday law:** Faraday law and electromagnetic induction
- **Maxwell equations:** Maxwell equations as the electromagnetic foundation

---

## What's Next

**Chapter 03-38: Electromagnetic Waves and Transmission Lines**

Carry forward the same FE workflow: identify the abstraction and operating state, define signs/units/logic representation, select the Handbook relation or learned method, solve, and verify the result against model validity and limiting cases.

— Your Mentor
