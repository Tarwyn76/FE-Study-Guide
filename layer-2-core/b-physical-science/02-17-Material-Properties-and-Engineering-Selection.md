---
chapter: "02-17"
title: "Material Properties and Engineering Selection"
layer: 2
tier: B
template: technical
ledger_ids: [MAT-2B-017-01, MAT-2B-017-02, MAT-2B-017-03, MAT-2B-017-04, MAT-2B-017-05, MAT-2B-017-06, MAT-2B-017-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-17: Material Properties and Engineering Selection

> *"Physical science becomes engineering when the microscopic model, measured property, and safety consequence are connected explicitly."*

---

## Before You Start

**Prerequisites:** 02-16

**Skip if:** You can solve the calculation and scenario checks in this chapter while stating the assumptions and Handbook source used.

**Time:** About 85–115 min reading and worked examples · 40–50 min review questions · 60–80 min practice problems.

---

## On the Board Today

The Handbook directly supplies electrical properties, strain relations, mechanical-property and failure formulas/tables, concrete behavior, polymer thermal behavior, and thermal-property definitions. Selection methodology is guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **17.1** Explain and apply **Stress, Strain, and the Stress-Strain Curve**.
* **17.2** Explain and apply **Ductility, Toughness, Hardness, and Impact**.
* **17.3** Explain and apply **Fracture, Fatigue, and Creep**.
* **17.4** Explain and apply **Electrical Properties**.
* **17.5** Explain and apply **Thermal Properties**.
* **17.6** Explain and apply **Physical and Chemical Properties**.
* **17.7** Explain and apply **Materials Selection as a Constraint-and-Objective Problem**.

---

## Notation Used Here

Notation is introduced within each section where needed. Use SI units unless a problem or Handbook table specifies another basis.

---

## 17.1 Stress, Strain, and the Stress-Strain Curve

Engineering strain is

\[
\varepsilon=\frac{\Delta L}{L_0}.
\]

The Handbook also relates true strain to engineering strain:

\[
\varepsilon_T=\ln(1+\varepsilon).
\]

A tensile stress-strain curve identifies elastic response, yielding, plastic deformation, ultimate tensile strength, and fracture. The slope of the linear elastic region is Young's modulus \(E\).

Strength and stiffness are different: strength concerns stress level at yielding/failure; stiffness concerns elastic deformation per unit stress.

![FIG-02-17-001: Annotated engineering stress-strain curve marking elastic region, modulus slope, yield, strain hardening, UTS, necking, and fracture.](../figures/FIG-02-17-001-stress-strain-and-the-stress-strain-curve.png)

### Worked Example 1 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **stress-strain behavior** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 17.2 Ductility, Toughness, Hardness, and Impact

**Ductility** describes permanent deformation before fracture. **Toughness** is the energy absorbed before fracture and corresponds qualitatively to area under the stress-strain curve.

The Handbook defines hardness as resistance to penetration and gives an approximate relation between Brinell hardness and tensile strength for plain carbon steels. It also describes the Charpy impact test and ductile-to-brittle transition.

Hardness is not the same as toughness; a very hard material can be brittle.

![FIG-02-17-002: Property comparison showing stiffness, strength, ductility, toughness, and hardness on stress-strain and indentation/impact sketches.](../figures/FIG-02-17-002-ductility-toughness-hardness-and-impact.png)

### Worked Example 2 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **mechanical properties** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 17.3 Fracture, Fatigue, and Creep

Fracture mechanics relates applied stress, crack size, geometry, and fracture toughness. The Handbook identifies \(K_{IC}\) as a critical stress-intensity material property.

**Fatigue** is failure under repeated/cyclic loading, often at stress below monotonic tensile strength. **Creep** is time-dependent deformation under sustained load, especially at elevated temperature.

Failure mode must be matched to service history. A static strength check does not automatically protect against fatigue, creep, or brittle fracture.

![FIG-02-17-003: Three-panel failure mechanisms: crack-driven fracture with KIC, S-N fatigue curve, and creep strain versus time.](../figures/FIG-02-17-003-fracture-fatigue-and-creep.png)

### Worked Example 3 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **failure modes** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 17.4 Electrical Properties

The Handbook gives resistivity relation

\[
\rho=\frac{RA}{L}
\]

or equivalently

\[
R=\rho\frac{L}{A}.
\]

Conductivity is the reciprocal:

\[
\sigma_e=\frac{1}{\rho}.
\]

For a parallel-plate capacitor,

\[
C=\frac{\varepsilon A}{d}.
\]

Electrical selection considers conductor versus insulator behavior, dielectric strength, temperature, frequency, and environmental stability.

![FIG-02-17-004: Electrical property diagram linking resistivity/conductivity to conductor geometry and permittivity to parallel-plate capacitance.](../figures/FIG-02-17-004-electrical-properties.png)

### Worked Example 4 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **electrical properties** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 17.5 Thermal Properties

The Handbook defines thermal expansion through

\[
\varepsilon=\alpha\Delta T,
\]

for unconstrained linear thermal strain. It also defines specific heat/heat capacity and thermal diffusivity.

Thermal conductivity \(k\) controls steady conduction response; thermal diffusivity combines conductivity with heat capacity and density to characterize how rapidly temperature disturbances propagate.

Material selection for thermal service may require balancing low expansion, high conductivity, thermal-shock resistance, and temperature capability.

![FIG-02-17-005: Thermal-properties map showing expansion, conductivity, heat capacity, and diffusivity with representative engineering applications.](../figures/FIG-02-17-005-thermal-properties.png)

### Worked Example 5 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **thermal properties** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 17.6 Physical and Chemical Properties

Density influences weight, inertia, buoyancy, and specific property measures such as strength-to-weight ratio. Melting temperature constrains service and manufacturing processes. Chemical resistance and corrosion behavior determine compatibility with fluids and atmospheres.

No single property should dominate selection without checking the complete service envelope.

A useful design concept is **specific strength**:

\[
\text{specific strength}=\frac{\text{strength}}{\rho},
\]

which compares strength per unit density.

![FIG-02-17-006: Property chart comparing density, strength, temperature capability, and chemical resistance across material classes.](../figures/FIG-02-17-006-physical-and-chemical-properties.png)

### Worked Example 6 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **physical properties** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 17.7 Materials Selection as a Constraint-and-Objective Problem

A structured selection process is:

1. translate design requirements into material constraints;
2. eliminate materials that fail mandatory constraints;
3. rank survivors using objectives such as mass, cost, stiffness, conductivity, or life;
4. check processing, joining, availability, compatibility, and failure modes;
5. validate with application-specific data and standards.

The Handbook provides properties; the engineering decision is matching those properties to the service.

![FIG-02-17-007: Materials-selection flowchart from functional requirements to constraints, screening, ranking, processing/compatibility checks, and final validation.](../figures/FIG-02-17-007-materials-selection-as-a-constraint-and-objective-problem.png)

### Worked Example 7 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **materials selection** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Materials Science/Structure of Matter pp. 118–128**.

**Source boundary:** The Handbook directly supplies electrical properties, strain relations, mechanical-property and failure formulas/tables, concrete behavior, polymer thermal behavior, and thermal-property definitions. Selection methodology is guide-developed.

---

## Where This Goes Wrong

**Using stress-strain behavior without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using mechanical properties without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using failure modes without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using electrical properties without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using thermal properties without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using physical properties without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using materials selection without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Replacing supplied data with a memorized trend.** If the Handbook or problem gives specific property, potential, limit, or compatibility data, use it.


---

## Key Terms

| Term | Working definition |
|---|---|
| engineering strain | Term introduced in this chapter; use the definition and conditions in the owning section. |
| true strain | Term introduced in this chapter; use the definition and conditions in the owning section. |
| Young modulus | Term introduced in this chapter; use the definition and conditions in the owning section. |
| yield strength | Term introduced in this chapter; use the definition and conditions in the owning section. |
| ultimate tensile strength | Term introduced in this chapter; use the definition and conditions in the owning section. |
| ductility | Term introduced in this chapter; use the definition and conditions in the owning section. |
| toughness | Term introduced in this chapter; use the definition and conditions in the owning section. |
| hardness | Term introduced in this chapter; use the definition and conditions in the owning section. |
| Charpy impact test | Term introduced in this chapter; use the definition and conditions in the owning section. |
| fracture toughness | Term introduced in this chapter; use the definition and conditions in the owning section. |
| fatigue | Term introduced in this chapter; use the definition and conditions in the owning section. |
| creep | Term introduced in this chapter; use the definition and conditions in the owning section. |
| resistivity | Term introduced in this chapter; use the definition and conditions in the owning section. |
| electrical conductivity | Term introduced in this chapter; use the definition and conditions in the owning section. |
| permittivity | Term introduced in this chapter; use the definition and conditions in the owning section. |
| dielectric | Term introduced in this chapter; use the definition and conditions in the owning section. |
| thermal expansion coefficient | Term introduced in this chapter; use the definition and conditions in the owning section. |
| specific heat | Term introduced in this chapter; use the definition and conditions in the owning section. |
| thermal diffusivity | Term introduced in this chapter; use the definition and conditions in the owning section. |
| thermal conductivity | Term introduced in this chapter; use the definition and conditions in the owning section. |
| density | Term introduced in this chapter; use the definition and conditions in the owning section. |
| specific strength | Term introduced in this chapter; use the definition and conditions in the owning section. |
| chemical resistance | Term introduced in this chapter; use the definition and conditions in the owning section. |
| materials selection | Term introduced in this chapter; use the definition and conditions in the owning section. |
| material constraint | Term introduced in this chapter; use the definition and conditions in the owning section. |
| selection objective | Term introduced in this chapter; use the definition and conditions in the owning section. |

---

## Review Questions

### Conceptual and Applied

1. Define **stress-strain behavior** and state its engineering significance.

2. Define **mechanical properties** and state its engineering significance.

3. Define **failure modes** and state its engineering significance.

4. Define **electrical properties** and state its engineering significance.

5. Define **thermal properties** and state its engineering significance.

6. Define **physical properties** and state its engineering significance.

7. Define **materials selection** and state its engineering significance.

8. What error is likely if **stress-strain behavior** is used without checking the problem's state, composition, units, or assumptions?

9. What error is likely if **mechanical properties** is used without checking the problem's state, composition, units, or assumptions?

10. What error is likely if **failure modes** is used without checking the problem's state, composition, units, or assumptions?

11. What error is likely if **electrical properties** is used without checking the problem's state, composition, units, or assumptions?

12. What error is likely if **thermal properties** is used without checking the problem's state, composition, units, or assumptions?

13. What error is likely if **physical properties** is used without checking the problem's state, composition, units, or assumptions?

14. What error is likely if **materials selection** is used without checking the problem's state, composition, units, or assumptions?

15. Identify one Handbook table, equation, or definition you would locate before solving a representative problem from this chapter.

16. State one physical-reasonableness or dimensional check appropriate to this chapter.

17. Explain when measured or tabulated data should replace a qualitative trend.

18. Give one example of an interpretation in this chapter that is guide-developed rather than a verbatim Handbook rule.

### Multiple Choice

19. Which answer best describes **stress-strain behavior**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

20. Which answer best describes **mechanical properties**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

21. Which answer best describes **failure modes**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

22. Which answer best describes **electrical properties**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

23. Which answer best describes **thermal properties**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

24. Which answer best describes **physical properties**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

25. Which answer best describes **materials selection**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

26. Which answer best describes **stress-strain behavior**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

27. Which answer best describes **mechanical properties**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data


---

## Answer Key with Explanations

1. **stress-strain behavior** is the central concept of §17.1; apply the definition, assumptions, and engineering consequence developed in that section.

2. **mechanical properties** is the central concept of §17.2; apply the definition, assumptions, and engineering consequence developed in that section.

3. **failure modes** is the central concept of §17.3; apply the definition, assumptions, and engineering consequence developed in that section.

4. **electrical properties** is the central concept of §17.4; apply the definition, assumptions, and engineering consequence developed in that section.

5. **thermal properties** is the central concept of §17.5; apply the definition, assumptions, and engineering consequence developed in that section.

6. **physical properties** is the central concept of §17.6; apply the definition, assumptions, and engineering consequence developed in that section.

7. **materials selection** is the central concept of §17.7; apply the definition, assumptions, and engineering consequence developed in that section.

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

19. **A.** The chapter applies **stress-strain behavior** only under its stated physical/model assumptions.

20. **A.** The chapter applies **mechanical properties** only under its stated physical/model assumptions.

21. **A.** The chapter applies **failure modes** only under its stated physical/model assumptions.

22. **A.** The chapter applies **electrical properties** only under its stated physical/model assumptions.

23. **A.** The chapter applies **thermal properties** only under its stated physical/model assumptions.

24. **A.** The chapter applies **physical properties** only under its stated physical/model assumptions.

25. **A.** The chapter applies **materials selection** only under its stated physical/model assumptions.

26. **A.** The chapter applies **stress-strain behavior** only under its stated physical/model assumptions.

27. **A.** The chapter applies **mechanical properties** only under its stated physical/model assumptions.


---

## Practice Problems

1. 1. A 2.00 m bar elongates 1.0 mm. Find engineering strain.

2. 2. If engineering strain is 0.10, find true strain ln(1+ε).

3. 3. Distinguish strength from stiffness.

4. 4. A conductor has R=0.20 Ω, A=2.0 mm2, L=10 m. Find resistivity in Ω·m.

5. 5. If resistivity is 1.7×10−8 Ω·m, find conductivity.

6. 6. A material has α=12×10−6 /K and ΔT=80 K. Find free thermal strain.

7. 7. If E=200 GPa and elastic strain=0.001, estimate stress.

8. 8. Which property measures resistance to penetration?

9. 9. Which failure mechanism is associated with repeated cyclic loading?

10. 10. Why is a low-density material not automatically the best lightweight choice?


---

## Practice Problem Solutions

1. 1. ε=0.001/2.00=5.0×10−4.

2. 2. εT=ln(1.10)=0.09531.

3. 3. Strength is stress capacity before yielding/failure; stiffness is resistance to elastic deformation, quantified by modulus.

4. 4. A=2.0×10−6 m2; ρ=RA/L=0.20(2.0×10−6)/10=4.0×10−8 Ω·m.

5. 5. σe=1/ρ=5.88×10^7 S/m.

6. 6. ε=αΔT=12×10−6×80=9.6×10−4.

7. 7. σ=Eε=200 GPa×0.001=200 MPa.

8. 8. Hardness.

9. 9. Fatigue.

10. 10. Selection depends on specific stiffness/strength, durability, temperature, manufacturing, cost, and failure requirements, not density alone.


---

## Quick Reference

**Handbook anchor:** Materials Science/Structure of Matter pp. 118–128.

- **stress-strain behavior:** Stress, Strain, and the Stress-Strain Curve
- **mechanical properties:** Ductility, Toughness, Hardness, and Impact
- **failure modes:** Fracture, Fatigue, and Creep
- **electrical properties:** Electrical Properties
- **thermal properties:** Thermal Properties
- **physical properties:** Physical and Chemical Properties
- **materials selection:** Materials Selection as a Constraint-and-Objective Problem

---

## What's Next

**02-18 — Diffusion, Phase Change, Heat Treatment, and Processing**

Carry forward the rule: identify the physical model and service condition before selecting the formula, property, or safety control.

— Your Mentor
