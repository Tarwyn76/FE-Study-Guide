---
chapter: "02-16"
title: "Materials Classes, Structure, and Bonding"
layer: 2
tier: B
template: technical
ledger_ids: [MAT-2B-016-01, MAT-2B-016-02, MAT-2B-016-03, MAT-2B-016-04, MAT-2B-016-05, MAT-2B-016-06, MAT-2B-016-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-16: Materials Classes, Structure, and Bonding

> *"Physical science becomes engineering when the microscopic model, measured property, and safety consequence are connected explicitly."*

---

## Before You Start

**Prerequisites:** 02-11 · 02-15

**Skip if:** You can solve the calculation and scenario checks in this chapter while stating the assumptions and Handbook source used.

**Time:** About 85–115 min reading and worked examples · 40–50 min review questions · 60–80 min practice problems.

---

## On the Board Today

The Handbook directly identifies primary bonds, composite relations, amorphous materials, thermoplastics/thermosets, and several processing concepts. Crystal-structure and defect explanations are guide-developed foundations.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **16.1** Explain and apply **Engineering Material Classes**.
* **16.2** Explain and apply **Bonding as the Structural Foundation**.
* **16.3** Explain and apply **Crystalline Structures — BCC, FCC, and HCP**.
* **16.4** Explain and apply **Defects, Grains, and Grain Boundaries**.
* **16.5** Explain and apply **Amorphous, Semicrystalline, and Polymer Structure**.
* **16.6** Explain and apply **Composite Structure and Rule-of-Mixtures Thinking**.
* **16.7** Explain and apply **Structure, Compatibility, and Service Environment**.

---

## Notation Used Here

Notation is introduced within each section where needed. Use SI units unless a problem or Handbook table specifies another basis.

---

## 16.1 Engineering Material Classes

The broad engineering classes are metals/alloys, ceramics/glasses, polymers, and composites.

Metals typically offer conductivity, toughness, manufacturability, and plastic deformation. Ceramics often provide hardness, chemical stability, and temperature resistance but limited tensile toughness. Polymers offer low density and easy shaping with strong temperature dependence. Composites combine constituents to tailor directional or bulk properties.

These are trends, not guarantees. Always use actual material-property data for final design.

![FIG-02-16-001: Engineering materials family tree dividing metals, ceramics/glasses, polymers, and composites with representative property trends.](../figures/FIG-02-16-001-engineering-material-classes.png)

### Worked Example 1 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **material classes** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 16.2 Bonding as the Structural Foundation

The Handbook's three primary bond types—ionic, covalent, and metallic—provide the microscopic foundation for many material classes.

Metals are dominated by metallic bonding. Many ceramics combine ionic and covalent character. Polymer backbones use covalent bonds while secondary interactions act between chains.

Bonding affects elastic stiffness, melting temperature, thermal expansion, conductivity, and allowable deformation. Structure adds another layer: two materials with similar chemistry can behave differently because their phases, grain sizes, or processing histories differ.

![FIG-02-16-002: Hierarchy diagram bonding -> crystal/molecular structure -> microstructure -> processing -> engineering properties.](../figures/FIG-02-16-002-bonding-as-the-structural-foundation.png)

### Worked Example 2 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **materials bonding** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 16.3 Crystalline Structures — BCC, FCC, and HCP

Many metals form ordered crystals. Three common structures are body-centered cubic (BCC), face-centered cubic (FCC), and hexagonal close-packed (HCP).

The Handbook refers to FCC austenite and BCC ferrite in steel-processing discussion but does not provide a complete crystallography tutorial. The shared-core engineering idea is that crystal geometry influences slip systems, density, diffusion paths, and phase behavior.

You do not need to memorize every metal's structure unless the problem requires it; focus on recognizing structure-property connections.

![FIG-02-16-003: Unit-cell comparison of BCC, FCC, and HCP structures with lattice points and qualitative packing/slip annotations.](../figures/FIG-02-16-003-crystalline-structures-bcc-fcc-and-hcp.png)

### Worked Example 3 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **crystal structures** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 16.4 Defects, Grains, and Grain Boundaries

Real crystals are not perfect. Point defects, dislocations, grain boundaries, and second-phase particles influence strength, diffusion, and corrosion.

Plastic deformation in crystalline metals occurs largely through dislocation motion. Obstacles to that motion can increase strength. Grain boundaries can impede dislocations, provide rapid diffusion paths, and create electrochemical differences.

Microstructure is therefore a design variable controlled through composition and processing.

![FIG-02-16-004: Schematic polycrystal with grains, grain boundaries, vacancies, interstitials, and edge dislocation labeled.](../figures/FIG-02-16-004-defects-grains-and-grain-boundaries.png)

### Worked Example 4 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **defects** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 16.5 Amorphous, Semicrystalline, and Polymer Structure

The Handbook states that glass is amorphous and thermoplastic polymers may be semicrystalline or amorphous. Below the glass-transition temperature \(T_g\), amorphous material behavior becomes more brittle.

Thermoplastics can be melted and reformed; thermosets cannot simply be remelted into a new shape after crosslinking.

Polymer response depends on chain architecture, molecular weight, crystallinity, crosslinking, additives, time, and temperature.

![FIG-02-16-005: Specific-volume or modulus-versus-temperature comparison showing Tg and Tm for amorphous, semicrystalline, and crystalline behavior.](../figures/FIG-02-16-005-amorphous-semicrystalline-and-polymer-structure.png)

### Worked Example 5 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **polymer structure** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 16.6 Composite Structure and Rule-of-Mixtures Thinking

The Handbook provides composite relations based on constituent volume fractions. For density,

\[
\rho_c=\sum f_i\rho_i.
\]

For long aligned fibers loaded along the fiber direction, a rule-of-mixtures form for modulus is

\[
E_c=\sum f_iE_i
\]

under compatible-strain assumptions.

Composite behavior is often anisotropic. Fiber orientation, interface quality, volume fraction, and loading direction must match the formula assumptions.

![FIG-02-16-006: Aligned-fiber composite showing matrix, fibers, longitudinal loading, equal-strain assumption, and volume-fraction rule of mixtures.](../figures/FIG-02-16-006-composite-structure-and-rule-of-mixtures-thinking.png)

### Worked Example 6 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **composites** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 16.7 Structure, Compatibility, and Service Environment

Material selection requires more than mechanical strength. Chemical compatibility, thermal exposure, electrical requirements, radiation, moisture, wear, manufacturability, and joining can determine the best class.

A polymer may be chemically compatible but too soft at service temperature. A metal may have adequate strength but corrode in the fluid. A ceramic may resist heat but fail under impact.

Use structure and bonding to explain behavior, then confirm with service-specific property and compatibility data.

![FIG-02-16-007: Material-class selection matrix crossing mechanical, thermal, chemical, electrical, density, manufacturing, and cost requirements.](../figures/FIG-02-16-007-structure-compatibility-and-service-environment.png)

### Worked Example 7 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **compatibility** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Materials Science/Structure of Matter pp. 117, 124, 127**.

**Source boundary:** The Handbook directly identifies primary bonds, composite relations, amorphous materials, thermoplastics/thermosets, and several processing concepts. Crystal-structure and defect explanations are guide-developed foundations.

---

## Where This Goes Wrong

**Using material classes without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using materials bonding without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using crystal structures without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using defects without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using polymer structure without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using composites without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using compatibility without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Replacing supplied data with a memorized trend.** If the Handbook or problem gives specific property, potential, limit, or compatibility data, use it.


---

## Key Terms

| Term | Working definition |
|---|---|
| metal | Term introduced in this chapter; use the definition and conditions in the owning section. |
| ceramic | Term introduced in this chapter; use the definition and conditions in the owning section. |
| polymer | Term introduced in this chapter; use the definition and conditions in the owning section. |
| composite | Term introduced in this chapter; use the definition and conditions in the owning section. |
| materials bonding | Term introduced in this chapter; use the definition and conditions in the owning section. |
| crystal lattice | Term introduced in this chapter; use the definition and conditions in the owning section. |
| BCC structure | Term introduced in this chapter; use the definition and conditions in the owning section. |
| FCC structure | Term introduced in this chapter; use the definition and conditions in the owning section. |
| HCP structure | Term introduced in this chapter; use the definition and conditions in the owning section. |
| crystal defect | Term introduced in this chapter; use the definition and conditions in the owning section. |
| dislocation | Term introduced in this chapter; use the definition and conditions in the owning section. |
| grain boundary | Term introduced in this chapter; use the definition and conditions in the owning section. |
| microstructure | Term introduced in this chapter; use the definition and conditions in the owning section. |
| amorphous material | Term introduced in this chapter; use the definition and conditions in the owning section. |
| semicrystalline polymer | Term introduced in this chapter; use the definition and conditions in the owning section. |
| thermoplastic | Term introduced in this chapter; use the definition and conditions in the owning section. |
| thermoset | Term introduced in this chapter; use the definition and conditions in the owning section. |
| glass transition temperature | Term introduced in this chapter; use the definition and conditions in the owning section. |
| volume fraction | Term introduced in this chapter; use the definition and conditions in the owning section. |
| rule of mixtures | Term introduced in this chapter; use the definition and conditions in the owning section. |
| anisotropy | Term introduced in this chapter; use the definition and conditions in the owning section. |
| material compatibility | Term introduced in this chapter; use the definition and conditions in the owning section. |
| service environment | Term introduced in this chapter; use the definition and conditions in the owning section. |

---

## Review Questions

### Conceptual and Applied

1. Define **material classes** and state its engineering significance.

2. Define **materials bonding** and state its engineering significance.

3. Define **crystal structures** and state its engineering significance.

4. Define **defects** and state its engineering significance.

5. Define **polymer structure** and state its engineering significance.

6. Define **composites** and state its engineering significance.

7. Define **compatibility** and state its engineering significance.

8. What error is likely if **material classes** is used without checking the problem's state, composition, units, or assumptions?

9. What error is likely if **materials bonding** is used without checking the problem's state, composition, units, or assumptions?

10. What error is likely if **crystal structures** is used without checking the problem's state, composition, units, or assumptions?

11. What error is likely if **defects** is used without checking the problem's state, composition, units, or assumptions?

12. What error is likely if **polymer structure** is used without checking the problem's state, composition, units, or assumptions?

13. What error is likely if **composites** is used without checking the problem's state, composition, units, or assumptions?

14. What error is likely if **compatibility** is used without checking the problem's state, composition, units, or assumptions?

15. Identify one Handbook table, equation, or definition you would locate before solving a representative problem from this chapter.

16. State one physical-reasonableness or dimensional check appropriate to this chapter.

17. Explain when measured or tabulated data should replace a qualitative trend.

18. Give one example of an interpretation in this chapter that is guide-developed rather than a verbatim Handbook rule.

### Multiple Choice

19. Which answer best describes **material classes**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

20. Which answer best describes **materials bonding**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

21. Which answer best describes **crystal structures**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

22. Which answer best describes **defects**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

23. Which answer best describes **polymer structure**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

24. Which answer best describes **composites**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

25. Which answer best describes **compatibility**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

26. Which answer best describes **material classes**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

27. Which answer best describes **materials bonding**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data


---

## Answer Key with Explanations

1. **material classes** is the central concept of §16.1; apply the definition, assumptions, and engineering consequence developed in that section.

2. **materials bonding** is the central concept of §16.2; apply the definition, assumptions, and engineering consequence developed in that section.

3. **crystal structures** is the central concept of §16.3; apply the definition, assumptions, and engineering consequence developed in that section.

4. **defects** is the central concept of §16.4; apply the definition, assumptions, and engineering consequence developed in that section.

5. **polymer structure** is the central concept of §16.5; apply the definition, assumptions, and engineering consequence developed in that section.

6. **composites** is the central concept of §16.6; apply the definition, assumptions, and engineering consequence developed in that section.

7. **compatibility** is the central concept of §16.7; apply the definition, assumptions, and engineering consequence developed in that section.

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

19. **A.** The chapter applies **material classes** only under its stated physical/model assumptions.

20. **A.** The chapter applies **materials bonding** only under its stated physical/model assumptions.

21. **A.** The chapter applies **crystal structures** only under its stated physical/model assumptions.

22. **A.** The chapter applies **defects** only under its stated physical/model assumptions.

23. **A.** The chapter applies **polymer structure** only under its stated physical/model assumptions.

24. **A.** The chapter applies **composites** only under its stated physical/model assumptions.

25. **A.** The chapter applies **compatibility** only under its stated physical/model assumptions.

26. **A.** The chapter applies **material classes** only under its stated physical/model assumptions.

27. **A.** The chapter applies **materials bonding** only under its stated physical/model assumptions.


---

## Practice Problems

1. 1. Name the four broad engineering material classes used in this chapter.

2. 2. Which primary bond is characteristic of metals?

3. 3. Which crystal structure is ferrite (α-iron) identified with in the Handbook: BCC or FCC?

4. 4. Which crystal structure is austenite (γ-iron) identified with?

5. 5. Distinguish thermoplastic from thermoset.

6. 6. If a two-phase composite has volume fractions 0.30 and 0.70 with densities 7800 and 1200 kg/m3, estimate composite density by rule of mixtures.

7. 7. Why can grain boundaries increase strength yet also accelerate diffusion/corrosion in some systems?

8. 8. Define anisotropy.

9. 9. What is Tg?

10. 10. Why should material selection use service-specific property data even when bonding trends are known?


---

## Practice Problem Solutions

1. 1. Metals/alloys, ceramics/glasses, polymers, and composites.

2. 2. Metallic bond.

3. 3. BCC.

4. 4. FCC.

5. 5. Thermoplastics can be melted/reformed; thermosets are crosslinked and do not simply remelt for reshaping.

6. 6. ρ=0.30(7800)+0.70(1200)=3180 kg/m3.

7. 7. Boundaries impede dislocations but can provide high-energy paths/sites for diffusion and electrochemical activity.

8. 8. Properties depend on direction.

9. 9. Glass-transition temperature for amorphous regions.

10. 10. Trends are qualitative; actual composition, processing, temperature, environment, geometry, and failure mode control performance.


---

## Quick Reference

**Handbook anchor:** Materials Science/Structure of Matter pp. 117, 124, 127.

- **material classes:** Engineering Material Classes
- **materials bonding:** Bonding as the Structural Foundation
- **crystal structures:** Crystalline Structures — BCC, FCC, and HCP
- **defects:** Defects, Grains, and Grain Boundaries
- **polymer structure:** Amorphous, Semicrystalline, and Polymer Structure
- **composites:** Composite Structure and Rule-of-Mixtures Thinking
- **compatibility:** Structure, Compatibility, and Service Environment

---

## What's Next

**02-17 — Material Properties and Engineering Selection**

Carry forward the rule: identify the physical model and service condition before selecting the formula, property, or safety control.

— Your Mentor
