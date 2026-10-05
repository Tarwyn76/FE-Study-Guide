---
chapter: "02-11"
title: "Atomic Structure, Bonding, and the Periodic Table"
layer: 2
tier: B
template: technical
ledger_ids: [SCI-2B-011-01, SCI-2B-011-02, SCI-2B-011-03, SCI-2B-011-04, SCI-2B-011-05, SCI-2B-011-06, SCI-2B-011-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-11: Atomic Structure, Bonding, and the Periodic Table

> *"Physical science becomes engineering when the microscopic model, measured property, and safety consequence are connected explicitly."*

---

## Before You Start

**Prerequisites:** 01-01 · 01-05

**Skip if:** You can solve the calculation and scenario checks in this chapter while stating the assumptions and Handbook source used.

**Time:** About 85–115 min reading and worked examples · 40–50 min review questions · 60–80 min practice problems.

---

## On the Board Today

The Handbook directly supplies atomic number, Avogadro's number, a periodic table, and the three primary bond classes. Electron-configuration detail and periodic-trend interpretation are guide-developed background expected for FE chemistry/materials questions.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **11.1** Explain and apply **Atoms, Atomic Number, and Isotopes**.
* **11.2** Explain and apply **Electrons, Valence, and Ion Formation**.
* **11.3** Explain and apply **Reading the Periodic Table**.
* **11.4** Explain and apply **Periodic Trends for Engineering Reasoning**.
* **11.5** Explain and apply **Primary Bonds — Ionic, Covalent, and Metallic**.
* **11.6** Explain and apply **Secondary Interactions and Molecular Polarity**.
* **11.7** Explain and apply **From Bonding to Engineering Properties**.

---

## Notation Used Here

Notation is introduced within each section where needed. Use SI units unless a problem or Handbook table specifies another basis.

---

## 11.1 Atoms, Atomic Number, and Isotopes

An atom contains a positively charged nucleus surrounded by electrons. The **atomic number** \(Z\) is the number of protons in the nucleus; the Handbook states this definition explicitly. For a neutral atom, the number of electrons equals \(Z\).

Atoms of the same element may contain different numbers of neutrons. These are **isotopes**. The mass number \(A\) is the total number of protons and neutrons,

\[
A=Z+N
\]

where \(N\) is the neutron count. Ions form when electrons are gained or lost; changing the electron count changes charge but not the element's identity.

For FE work, distinguish three different quantities that are often confused: atomic number identifies the element, mass number identifies an isotope, and atomic weight on the periodic table is an abundance-weighted average for naturally occurring isotopes.

![FIG-02-11-001: Cutaway atomic model showing nucleus with protons and neutrons, electron cloud, and callouts distinguishing atomic number Z, mass number A, neutron number N, and ionic charge.](../figures/FIG-02-11-001-atoms-atomic-number-and-isotopes.png)

### Worked Example 1 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **atomic number** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 11.2 Electrons, Valence, and Ion Formation

Chemical behavior is controlled primarily by electrons, especially the outer or **valence electrons**. A detailed quantum treatment is beyond the shared-core scope, but the engineering use is straightforward: atoms tend to form bonds or ions in ways that produce lower-energy electron arrangements.

Metals commonly lose valence electrons and form positive ions, or **cations**. Nonmetals commonly gain electrons and form negative ions, or **anions**. The charge on a monatomic ion determines the ratio required for an electrically neutral ionic compound.

Example: magnesium commonly forms \(Mg^{2+}\) and chlorine forms \(Cl^-\). Charge neutrality requires

\[
Mg^{2+}+2Cl^-\rightarrow MgCl_2.
\]

Valence is also central to oxidation-reduction and normality calculations later in Tier 2B.

![FIG-02-11-002: Electron-shell style diagram contrasting a metal losing valence electrons to form a cation and a nonmetal gaining electrons to form an anion, followed by charge-neutral compound formation.](../figures/FIG-02-11-002-electrons-valence-and-ion-formation.png)

### Worked Example 2 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **valence electrons** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 11.3 Reading the Periodic Table

The Handbook periodic table gives atomic number, chemical symbol, and atomic weight for each element. Periods run horizontally and groups run vertically. Elements in the same group tend to share valence-electron patterns and therefore similar chemical behavior.

Useful broad families include alkali metals, alkaline-earth metals, transition metals, halogens, and noble gases. The FE exam may provide enough information in the question to avoid memorizing every group, but you should be able to navigate the table quickly.

A periodic-table lookup often supplies the molar mass needed for stoichiometry. For a compound, add the atomic weights of all atoms in the chemical formula.

![FIG-02-11-003: Annotated periodic table highlighting periods, major groups, metals, metalloids, nonmetals, halogens, and noble gases, with one element box enlarged to show atomic number, symbol, and atomic weight.](../figures/FIG-02-11-003-reading-the-periodic-table.png)

### Worked Example 3 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **periodic table** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 11.4 Periodic Trends for Engineering Reasoning

The Handbook does not print a table of periodic trends, but FE chemistry questions may rely on basic trends. Across a period, effective nuclear attraction generally increases, so atomic radius tends to decrease while ionization energy and electronegativity tend to increase. Down a group, additional electron shells generally increase atomic radius.

These trends are qualitative—not exact laws for every element. Their value is comparative reasoning: which atom is likely to form a positive ion, which bond is likely to be polar, or which element is more metallic.

When a question provides measured data, use the data. Use periodic trends only when the problem is asking for qualitative prediction.

![FIG-02-11-004: Periodic table overlaid with arrows showing general increases in atomic radius, ionization energy, electronegativity, and metallic character.](../figures/FIG-02-11-004-periodic-trends-for-engineering-reasoning.png)

### Worked Example 4 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **periodic trends** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 11.5 Primary Bonds — Ionic, Covalent, and Metallic

The Materials Science section of the Handbook explicitly identifies three **primary bonds**:

- **ionic** — typical of salts and metal oxides,
- **covalent** — important within molecules and polymer chains,
- **metallic** — characteristic of metals.

Ionic bonding arises from electrostatic attraction between oppositely charged ions. Covalent bonding involves shared electron pairs and tends to be directional. Metallic bonding is often modeled as positive ion cores surrounded by delocalized electrons.

Bond type helps explain engineering behavior. Strong directional bonds can produce high stiffness but limited plasticity; metallic bonding supports electrical conduction and plastic deformation; ionic solids may have high melting temperatures yet be brittle.

![FIG-02-11-005: Three-panel atomic-scale comparison of ionic, covalent, and metallic bonding with electron transfer, electron sharing, and delocalized-electron sea representations.](../figures/FIG-02-11-005-primary-bonds-ionic-covalent-and-metallic.png)

### Worked Example 5 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **primary bonds** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 11.6 Secondary Interactions and Molecular Polarity

Secondary interactions are weaker than primary bonds but can strongly influence boiling point, polymer behavior, adhesion, and solubility. Common categories include dipole-dipole attraction, hydrogen bonding, and dispersion forces.

A bond is **polar** when electrons are shared unequally. A molecule may contain polar bonds yet have little net molecular polarity if the geometry cancels bond dipoles.

For engineering use, polarity helps predict compatibility: polar substances tend to interact more strongly with other polar substances, while nonpolar substances often dissolve more readily in nonpolar media. This is a guide-developed bridge between chemistry and materials selection.

![FIG-02-11-006: Polarity diagram showing nonpolar bond, polar bond with partial charges, a polar molecule with net dipole, and a symmetric molecule whose bond dipoles cancel.](../figures/FIG-02-11-006-secondary-interactions-and-molecular-polarity.png)

### Worked Example 6 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **molecular polarity** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 11.7 From Bonding to Engineering Properties

Atomic bonding is not merely microscopic description; it is one of the reasons materials behave differently.

Metals generally combine electrical/thermal conductivity with ductility because metallic bonding permits electron mobility and nondirectional slip. Ceramics often contain ionic and covalent bonding, contributing to stiffness, temperature resistance, and brittleness. Polymers rely on covalent chains plus weaker interactions between chains, producing strong temperature dependence. Composites deliberately combine phases to obtain a property combination unavailable from one material alone.

Use bonding as a causal explanation, not as a substitute for property data. Final material selection still depends on measured mechanical, thermal, electrical, chemical, manufacturing, and economic requirements.

![FIG-02-11-007: Materials map linking dominant bond types to metals, ceramics, polymers, and representative conductivity, stiffness, ductility, and temperature-resistance trends.](../figures/FIG-02-11-007-from-bonding-to-engineering-properties.png)

### Worked Example 7 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **bond-property link** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Chemistry and Biology pp. 86, 89; Materials Science/Structure of Matter p. 117**.

**Source boundary:** The Handbook directly supplies atomic number, Avogadro's number, a periodic table, and the three primary bond classes. Electron-configuration detail and periodic-trend interpretation are guide-developed background expected for FE chemistry/materials questions.

---

## Where This Goes Wrong

**Using atomic number without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using valence electrons without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using periodic table without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using periodic trends without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using primary bonds without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using molecular polarity without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using bond-property link without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Replacing supplied data with a memorized trend.** If the Handbook or problem gives specific property, potential, limit, or compatibility data, use it.


---

## Key Terms

| Term | Working definition |
|---|---|
| atomic number | Term introduced in this chapter; use the definition and conditions in the owning section. |
| isotope | Term introduced in this chapter; use the definition and conditions in the owning section. |
| mass number | Term introduced in this chapter; use the definition and conditions in the owning section. |
| valence electron | Term introduced in this chapter; use the definition and conditions in the owning section. |
| cation | Term introduced in this chapter; use the definition and conditions in the owning section. |
| anion | Term introduced in this chapter; use the definition and conditions in the owning section. |
| charge neutrality | Term introduced in this chapter; use the definition and conditions in the owning section. |
| periodic-table group | Term introduced in this chapter; use the definition and conditions in the owning section. |
| periodic-table period | Term introduced in this chapter; use the definition and conditions in the owning section. |
| molar mass | Term introduced in this chapter; use the definition and conditions in the owning section. |
| atomic radius trend | Term introduced in this chapter; use the definition and conditions in the owning section. |
| ionization energy trend | Term introduced in this chapter; use the definition and conditions in the owning section. |
| electronegativity trend | Term introduced in this chapter; use the definition and conditions in the owning section. |
| ionic bond | Term introduced in this chapter; use the definition and conditions in the owning section. |
| covalent bond | Term introduced in this chapter; use the definition and conditions in the owning section. |
| metallic bond | Term introduced in this chapter; use the definition and conditions in the owning section. |
| bond polarity | Term introduced in this chapter; use the definition and conditions in the owning section. |
| molecular polarity | Term introduced in this chapter; use the definition and conditions in the owning section. |
| secondary interaction | Term introduced in this chapter; use the definition and conditions in the owning section. |
| bond-property relationship | Term introduced in this chapter; use the definition and conditions in the owning section. |

---

## Review Questions

### Conceptual and Applied

1. Define **atomic number** and state its engineering significance.

2. Define **valence electrons** and state its engineering significance.

3. Define **periodic table** and state its engineering significance.

4. Define **periodic trends** and state its engineering significance.

5. Define **primary bonds** and state its engineering significance.

6. Define **molecular polarity** and state its engineering significance.

7. Define **bond-property link** and state its engineering significance.

8. What error is likely if **atomic number** is used without checking the problem's state, composition, units, or assumptions?

9. What error is likely if **valence electrons** is used without checking the problem's state, composition, units, or assumptions?

10. What error is likely if **periodic table** is used without checking the problem's state, composition, units, or assumptions?

11. What error is likely if **periodic trends** is used without checking the problem's state, composition, units, or assumptions?

12. What error is likely if **primary bonds** is used without checking the problem's state, composition, units, or assumptions?

13. What error is likely if **molecular polarity** is used without checking the problem's state, composition, units, or assumptions?

14. What error is likely if **bond-property link** is used without checking the problem's state, composition, units, or assumptions?

15. Identify one Handbook table, equation, or definition you would locate before solving a representative problem from this chapter.

16. State one physical-reasonableness or dimensional check appropriate to this chapter.

17. Explain when measured or tabulated data should replace a qualitative trend.

18. Give one example of an interpretation in this chapter that is guide-developed rather than a verbatim Handbook rule.

### Multiple Choice

19. Which answer best describes **atomic number**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

20. Which answer best describes **valence electrons**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

21. Which answer best describes **periodic table**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

22. Which answer best describes **periodic trends**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

23. Which answer best describes **primary bonds**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

24. Which answer best describes **molecular polarity**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

25. Which answer best describes **bond-property link**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

26. Which answer best describes **atomic number**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

27. Which answer best describes **valence electrons**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data


---

## Answer Key with Explanations

1. **atomic number** is the central concept of §11.1; apply the definition, assumptions, and engineering consequence developed in that section.

2. **valence electrons** is the central concept of §11.2; apply the definition, assumptions, and engineering consequence developed in that section.

3. **periodic table** is the central concept of §11.3; apply the definition, assumptions, and engineering consequence developed in that section.

4. **periodic trends** is the central concept of §11.4; apply the definition, assumptions, and engineering consequence developed in that section.

5. **primary bonds** is the central concept of §11.5; apply the definition, assumptions, and engineering consequence developed in that section.

6. **molecular polarity** is the central concept of §11.6; apply the definition, assumptions, and engineering consequence developed in that section.

7. **bond-property link** is the central concept of §11.7; apply the definition, assumptions, and engineering consequence developed in that section.

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

19. **A.** The chapter applies **atomic number** only under its stated physical/model assumptions.

20. **A.** The chapter applies **valence electrons** only under its stated physical/model assumptions.

21. **A.** The chapter applies **periodic table** only under its stated physical/model assumptions.

22. **A.** The chapter applies **periodic trends** only under its stated physical/model assumptions.

23. **A.** The chapter applies **primary bonds** only under its stated physical/model assumptions.

24. **A.** The chapter applies **molecular polarity** only under its stated physical/model assumptions.

25. **A.** The chapter applies **bond-property link** only under its stated physical/model assumptions.

26. **A.** The chapter applies **atomic number** only under its stated physical/model assumptions.

27. **A.** The chapter applies **valence electrons** only under its stated physical/model assumptions.


---

## Practice Problems

1. 1. An atom has atomic number 17 and mass number 37. Find protons, neutrons, and electrons for the neutral atom.

2. 2. The atom in Problem 1 gains one electron. State its ion charge and electron count.

3. 3. Using approximate atomic weights H=1.008 and O=15.999, find the molar mass of H2O.

4. 4. Magnesium forms Mg2+ and oxygen forms O2−. Write the neutral compound formula.

5. 5. Classify the dominant primary bond in NaCl, diamond, and copper.

6. 6. Which is generally more electronegative: an element near the upper-right or lower-left of the periodic table?

7. 7. Explain why metallic bonding supports electrical conductivity.

8. 8. Distinguish atomic number from atomic weight.

9. 9. A molecule contains polar bonds arranged symmetrically so their dipoles cancel. Is the molecule necessarily strongly polar?

10. 10. Give one reason a polymer and a ceramic can have very different mechanical behavior even when both contain strong covalent bonds.


---

## Practice Problem Solutions

1. 1. Protons = 17; neutrons = 37−17 = 20; neutral electrons = 17.

2. 2. One extra electron gives charge −1 and 18 electrons.

3. 3. M = 2(1.008)+15.999 = 18.015 g/mol.

4. 4. MgO.

5. 5. NaCl: ionic; diamond: covalent; copper: metallic.

6. 6. Upper-right, in the general periodic trend excluding noble-gas complications.

7. 7. Metallic bonding includes delocalized electrons that can move through the solid.

8. 8. Atomic number is proton count; atomic weight is an isotope-abundance-weighted average mass on the periodic table.

9. 9. No. Molecular geometry can cancel bond dipoles, giving small or zero net molecular dipole.

10. 10. Structure and secondary interactions differ; polymers use long-chain architecture and weaker interchain interactions, while ceramics form extended networks/crystals.


---

## Quick Reference

**Handbook anchor:** Chemistry and Biology pp. 86, 89; Materials Science/Structure of Matter p. 117.

- **atomic number:** Atoms, Atomic Number, and Isotopes
- **valence electrons:** Electrons, Valence, and Ion Formation
- **periodic table:** Reading the Periodic Table
- **periodic trends:** Periodic Trends for Engineering Reasoning
- **primary bonds:** Primary Bonds — Ionic, Covalent, and Metallic
- **molecular polarity:** Secondary Interactions and Molecular Polarity
- **bond-property link:** From Bonding to Engineering Properties

---

## What's Next

**02-12 — Chemical Quantities, Stoichiometry, and Reaction Balancing**

Carry forward the rule: identify the physical model and service condition before selecting the formula, property, or safety control.

— Your Mentor
