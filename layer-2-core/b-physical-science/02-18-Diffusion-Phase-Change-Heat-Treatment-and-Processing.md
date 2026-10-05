---
chapter: "02-18"
title: "Diffusion, Phase Change, Heat Treatment, and Processing"
layer: 2
tier: B
template: technical
ledger_ids: [MAT-2B-018-01, MAT-2B-018-02, MAT-2B-018-03, MAT-2B-018-04, MAT-2B-018-05, MAT-2B-018-06, MAT-2B-018-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-18: Diffusion, Phase Change, Heat Treatment, and Processing

> *"Physical science becomes engineering when the microscopic model, measured property, and safety consequence are connected explicitly."*

---

## Before You Start

**Prerequisites:** 02-17

**Skip if:** You can solve the calculation and scenario checks in this chapter while stating the assumptions and Handbook source used.

**Time:** About 85–115 min reading and worked examples · 40–50 min review questions · 60–80 min practice problems.

---

## On the Board Today

The Handbook directly supplies Arrhenius diffusion coefficient, cold-work/recovery/recrystallization/grain-growth descriptions, quenching/martensite notes, hardenability, binary phase-diagram uses, invariant reactions, lever rule, and iron-iron-carbide diagram.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **18.1** Explain and apply **Diffusion and the Arrhenius Temperature Dependence**.
* **18.2** Explain and apply **Cold Work, Recovery, Recrystallization, and Grain Growth**.
* **18.3** Explain and apply **Binary Phase Diagrams — What They Tell You**.
* **18.4** Explain and apply **The Lever Rule**.
* **18.5** Explain and apply **Invariant Reactions**.
* **18.6** Explain and apply **Iron-Iron Carbide and Steel Transformations**.
* **18.7** Explain and apply **Quenching, Hardenability, and Processing Choice**.

---

## Notation Used Here

Notation is introduced within each section where needed. Use SI units unless a problem or Handbook table specifies another basis.

---

## 18.1 Diffusion and the Arrhenius Temperature Dependence

The Handbook gives the diffusion coefficient

\[
D=D_0e^{-Q/(RT)},
\]

where \(D_0\) is a proportionality constant, \(Q\) activation energy, \(R\) gas constant, and \(T\) absolute temperature.

Because temperature appears in the exponential, diffusion can increase dramatically with temperature.

For two temperatures with the same material mechanism,

\[
\ln\frac{D_2}{D_1}
=-\frac{Q}{R}\left(\frac1{T_2}-\frac1{T_1}\right).
\]

This form avoids needing \(D_0\) when comparing rates.

![FIG-02-18-001: Arrhenius plot of ln D versus 1/T with slope -Q/R and annotations showing faster diffusion at higher temperature.](../figures/FIG-02-18-001-diffusion-and-the-arrhenius-temperature-dependence.png)

### Worked Example 1 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **diffusion** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 18.2 Cold Work, Recovery, Recrystallization, and Grain Growth

The Handbook states that cold working increases strength and lowers ductility. Plastic deformation raises dislocation density and stored strain energy.

On heating, the Handbook describes the sequence:

1. **recovery** — stress relief/rearrangement,
2. **recrystallization** — new low-strain grains form,
3. **grain growth** — grains enlarge with continued thermal exposure.

Hot working allows restoration processes to occur during deformation.

![FIG-02-18-002: Microstructure sequence from cold-worked elongated grains through recovery, recrystallized equiaxed grains, and grain growth.](../figures/FIG-02-18-002-cold-work-recovery-recrystallization-and-grain-growth.png)

### Worked Example 2 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **thermomechanical processing** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 18.3 Binary Phase Diagrams — What They Tell You

The Handbook states that a binary phase diagram allows determination of:

1. phases present at equilibrium,
2. composition of each phase,
3. fraction of each phase.

The axes are typically temperature and overall composition. Single-phase fields contain one stable phase; two-phase fields contain equilibrium mixtures.

A horizontal tie line through a two-phase region gives the phase compositions at its intersections with the boundaries.

![FIG-02-18-003: Generic binary eutectic phase diagram with liquid, alpha, beta, and two-phase regions, tie line, and phase-composition endpoints.](../figures/FIG-02-18-003-binary-phase-diagrams-what-they-tell-you.png)

### Worked Example 3 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **phase diagrams** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 18.4 The Lever Rule

Within a two-phase region, the phase fractions follow the **lever rule**. For an overall composition \(x\) between phase compositions \(x_\alpha\) and \(x_\beta\),

\[
w_\alpha=\frac{x_\beta-x}{x_\beta-x_\alpha},
\qquad
w_\beta=\frac{x-x_\alpha}{x_\beta-x_\alpha}.
\]

The numerator for one phase uses the opposite lever-arm length.

Check that

\[
w_\alpha+w_\beta=1.
\]

![FIG-02-18-004: Tie line in a two-phase region with overall composition x and lever arms labeled to derive alpha and beta mass fractions.](../figures/FIG-02-18-004-the-lever-rule.png)

### Worked Example 4 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **lever rule** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 18.5 Invariant Reactions

The Handbook lists four common binary reactions:

- eutectic: liquid \(\rightarrow\) two solids,
- eutectoid: one solid \(\rightarrow\) two solids,
- peritectic: liquid + solid \(\rightarrow\) solid,
- peritectoid: two solids \(\rightarrow\) solid.

Recognize the phase-state pattern. The exact compositions and temperatures come from the diagram provided.

![FIG-02-18-005: Four mini phase-reaction schematics comparing eutectic, eutectoid, peritectic, and peritectoid transformations.](../figures/FIG-02-18-005-invariant-reactions.png)

### Worked Example 5 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **phase reactions** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 18.6 Iron-Iron Carbide and Steel Transformations

The Handbook includes the iron-iron-carbide diagram and notes that austenite is FCC \(\gamma\) iron, ferrite is BCC \(\alpha\) iron, and cementite is iron carbide.

Steel heat treatment depends on moving through temperature/composition regions and controlling cooling. Slow/equilibrium cooling permits equilibrium phase formation; rapid quenching can suppress equilibrium transformations.

The complete Fe-Fe\(_3\)C diagram is complex. On the FE exam, use the provided diagram rather than trying to reconstruct it from memory.

![FIG-02-18-006: Simplified iron-iron-carbide diagram highlighting ferrite, austenite, cementite, eutectoid region, and cooling-path concept.](../figures/FIG-02-18-006-iron-iron-carbide-and-steel-transformations.png)

### Worked Example 6 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **steel phase transformations** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 18.7 Quenching, Hardenability, and Processing Choice

The Handbook states that quenching is rapid cooling from elevated temperature and can form martensite from austenite rather than equilibrium ferrite/cementite. It also distinguishes **hardness** from **hardenability**—the ease with which hardness can be developed through a section.

Processing changes structure, which changes properties. Engineering heat treatment may combine austenitizing, quenching, tempering, annealing, normalizing, or other cycles depending on the alloy and desired properties.

Use the actual alloy specification and heat-treatment procedure in practice; the FE-level task is to connect processing path to microstructure and property trends.

![FIG-02-18-007: Steel heat-treatment pathway from austenite through slow cooling or quench/temper, showing equilibrium products versus martensite and depth-of-hardening concept.](../figures/FIG-02-18-007-quenching-hardenability-and-processing-choice.png)

### Worked Example 7 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **heat treatment** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Materials Science/Structure of Matter pp. 117, 124–129**.

**Source boundary:** The Handbook directly supplies Arrhenius diffusion coefficient, cold-work/recovery/recrystallization/grain-growth descriptions, quenching/martensite notes, hardenability, binary phase-diagram uses, invariant reactions, lever rule, and iron-iron-carbide diagram.

---

## Where This Goes Wrong

**Using diffusion without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using thermomechanical processing without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using phase diagrams without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using lever rule without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using phase reactions without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using steel phase transformations without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using heat treatment without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Replacing supplied data with a memorized trend.** If the Handbook or problem gives specific property, potential, limit, or compatibility data, use it.


---

## Key Terms

| Term | Working definition |
|---|---|
| diffusion coefficient | Term introduced in this chapter; use the definition and conditions in the owning section. |
| activation energy | Term introduced in this chapter; use the definition and conditions in the owning section. |
| cold working | Term introduced in this chapter; use the definition and conditions in the owning section. |
| recovery | Term introduced in this chapter; use the definition and conditions in the owning section. |
| recrystallization | Term introduced in this chapter; use the definition and conditions in the owning section. |
| grain growth | Term introduced in this chapter; use the definition and conditions in the owning section. |
| hot working | Term introduced in this chapter; use the definition and conditions in the owning section. |
| binary phase diagram | Term introduced in this chapter; use the definition and conditions in the owning section. |
| phase field | Term introduced in this chapter; use the definition and conditions in the owning section. |
| tie line | Term introduced in this chapter; use the definition and conditions in the owning section. |
| lever rule | Term introduced in this chapter; use the definition and conditions in the owning section. |
| phase fraction | Term introduced in this chapter; use the definition and conditions in the owning section. |
| eutectic reaction | Term introduced in this chapter; use the definition and conditions in the owning section. |
| eutectoid reaction | Term introduced in this chapter; use the definition and conditions in the owning section. |
| peritectic reaction | Term introduced in this chapter; use the definition and conditions in the owning section. |
| peritectoid reaction | Term introduced in this chapter; use the definition and conditions in the owning section. |
| austenite | Term introduced in this chapter; use the definition and conditions in the owning section. |
| ferrite | Term introduced in this chapter; use the definition and conditions in the owning section. |
| cementite | Term introduced in this chapter; use the definition and conditions in the owning section. |
| quenching | Term introduced in this chapter; use the definition and conditions in the owning section. |
| martensite | Term introduced in this chapter; use the definition and conditions in the owning section. |
| hardenability | Term introduced in this chapter; use the definition and conditions in the owning section. |
| heat treatment | Term introduced in this chapter; use the definition and conditions in the owning section. |

---

## Review Questions

### Conceptual and Applied

1. Define **diffusion** and state its engineering significance.

2. Define **thermomechanical processing** and state its engineering significance.

3. Define **phase diagrams** and state its engineering significance.

4. Define **lever rule** and state its engineering significance.

5. Define **phase reactions** and state its engineering significance.

6. Define **steel phase transformations** and state its engineering significance.

7. Define **heat treatment** and state its engineering significance.

8. What error is likely if **diffusion** is used without checking the problem's state, composition, units, or assumptions?

9. What error is likely if **thermomechanical processing** is used without checking the problem's state, composition, units, or assumptions?

10. What error is likely if **phase diagrams** is used without checking the problem's state, composition, units, or assumptions?

11. What error is likely if **lever rule** is used without checking the problem's state, composition, units, or assumptions?

12. What error is likely if **phase reactions** is used without checking the problem's state, composition, units, or assumptions?

13. What error is likely if **steel phase transformations** is used without checking the problem's state, composition, units, or assumptions?

14. What error is likely if **heat treatment** is used without checking the problem's state, composition, units, or assumptions?

15. Identify one Handbook table, equation, or definition you would locate before solving a representative problem from this chapter.

16. State one physical-reasonableness or dimensional check appropriate to this chapter.

17. Explain when measured or tabulated data should replace a qualitative trend.

18. Give one example of an interpretation in this chapter that is guide-developed rather than a verbatim Handbook rule.

### Multiple Choice

19. Which answer best describes **diffusion**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

20. Which answer best describes **thermomechanical processing**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

21. Which answer best describes **phase diagrams**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

22. Which answer best describes **lever rule**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

23. Which answer best describes **phase reactions**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

24. Which answer best describes **steel phase transformations**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

25. Which answer best describes **heat treatment**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

26. Which answer best describes **diffusion**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

27. Which answer best describes **thermomechanical processing**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data


---

## Answer Key with Explanations

1. **diffusion** is the central concept of §18.1; apply the definition, assumptions, and engineering consequence developed in that section.

2. **thermomechanical processing** is the central concept of §18.2; apply the definition, assumptions, and engineering consequence developed in that section.

3. **phase diagrams** is the central concept of §18.3; apply the definition, assumptions, and engineering consequence developed in that section.

4. **lever rule** is the central concept of §18.4; apply the definition, assumptions, and engineering consequence developed in that section.

5. **phase reactions** is the central concept of §18.5; apply the definition, assumptions, and engineering consequence developed in that section.

6. **steel phase transformations** is the central concept of §18.6; apply the definition, assumptions, and engineering consequence developed in that section.

7. **heat treatment** is the central concept of §18.7; apply the definition, assumptions, and engineering consequence developed in that section.

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

19. **A.** The chapter applies **diffusion** only under its stated physical/model assumptions.

20. **A.** The chapter applies **thermomechanical processing** only under its stated physical/model assumptions.

21. **A.** The chapter applies **phase diagrams** only under its stated physical/model assumptions.

22. **A.** The chapter applies **lever rule** only under its stated physical/model assumptions.

23. **A.** The chapter applies **phase reactions** only under its stated physical/model assumptions.

24. **A.** The chapter applies **steel phase transformations** only under its stated physical/model assumptions.

25. **A.** The chapter applies **heat treatment** only under its stated physical/model assumptions.

26. **A.** The chapter applies **diffusion** only under its stated physical/model assumptions.

27. **A.** The chapter applies **thermomechanical processing** only under its stated physical/model assumptions.


---

## Practice Problems

1. 1. If Q=120 kJ/mol, compare D2/D1 between 800 K and 1000 K using R=8.314 J/mol·K.

2. 2. State the effect of cold work on strength and ductility.

3. 3. Put recovery, recrystallization, and grain growth in heating order.

4. 4. In a two-phase α+β region, xα=20 wt%B, xβ=80 wt%B, overall x=50 wt%B. Find wα and wβ.

5. 5. Name the reaction liquid → two solids.

6. 6. Name the reaction one solid → two solids.

7. 7. Which phase is FCC iron: ferrite or austenite?

8. 8. What can rapid quenching of austenite form?

9. 9. Distinguish hardness from hardenability.

10. 10. Why must lever-rule calculations use phase-boundary compositions from the tie line at the specified temperature?


---

## Practice Problem Solutions

1. 1. D2/D1=exp[-Q/R(1/T2−1/T1)] = 36.91.

2. 2. Strength generally increases; ductility decreases.

3. 3. Recovery → recrystallization → grain growth.

4. 4. wα=(80−50)/(80−20)=0.50; wβ=(50−20)/(80−20)=0.50.

5. 5. Eutectic reaction.

6. 6. Eutectoid reaction.

7. 7. Austenite.

8. 8. Martensite.

9. 9. Hardness is resistance to penetration; hardenability is the ability/ease of developing hardness through a section during heat treatment.

10. 10. Phase compositions vary with temperature; the tie-line endpoints define the equilibrium phase compositions used by the lever rule.


---

## Quick Reference

**Handbook anchor:** Materials Science/Structure of Matter pp. 117, 124–129.

- **diffusion:** Diffusion and the Arrhenius Temperature Dependence
- **thermomechanical processing:** Cold Work, Recovery, Recrystallization, and Grain Growth
- **phase diagrams:** Binary Phase Diagrams — What They Tell You
- **lever rule:** The Lever Rule
- **phase reactions:** Invariant Reactions
- **steel phase transformations:** Iron-Iron Carbide and Steel Transformations
- **heat treatment:** Quenching, Hardenability, and Processing Choice

---

## What's Next

**02-19 — Safety Systems, Hazard Communication, and Personal Protective Equipment**

Carry forward the rule: identify the physical model and service condition before selecting the formula, property, or safety control.

— Your Mentor
