---
chapter: "02-20"
title: "Fire, Explosion, Electrical, and Confined-Space Hazards"
layer: 2
tier: B
template: technical
ledger_ids: [SAFE-2B-020-01, SAFE-2B-020-02, SAFE-2B-020-03, SAFE-2B-020-04, SAFE-2B-020-05, SAFE-2B-020-06, SAFE-2B-020-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-20: Fire, Explosion, Electrical, and Confined-Space Hazards

> *"Physical science becomes engineering when the microscopic model, measured property, and safety consequence are connected explicitly."*

---

## Before You Start

**Prerequisites:** 02-19

**Skip if:** You can solve the calculation and scenario checks in this chapter while stating the assumptions and Handbook source used.

**Time:** About 85–115 min reading and worked examples · 40–50 min review questions · 60–80 min practice problems.

---

## On the Board Today

The Handbook directly supplies flammability definitions/LFL/UFL, Le Chatelier mixture rule, LOC/AIT definitions, confined-space criteria and gas notes, and electrical-shock current effects. Fire tetrahedron, lockout/tagout, and general prevention hierarchy are guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **20.1** Explain and apply **Combustion and the Flammable Range**.
* **20.2** Explain and apply **Autoignition and Limiting Oxygen Concentration**.
* **20.3** Explain and apply **Flammable Gas Mixtures — Le Chatelier's Rule**.
* **20.4** Explain and apply **Confined Spaces and Permit-Required Hazards**.
* **20.5** Explain and apply **Gas Detection and Sensor Placement**.
* **20.6** Explain and apply **Electrical Shock Hazards**.
* **20.7** Explain and apply **Energy Isolation and Integrated Hazard Control**.

---

## Notation Used Here

Notation is introduced within each section where needed. Use SI units unless a problem or Handbook table specifies another basis.

---

## 20.1 Combustion and the Flammable Range

A vapor-air mixture burns only over a concentration range bounded by the **lower flammability limit** (LFL) and **upper flammability limit** (UFL), also called LEL and UEL.

Below the LFL the mixture is too lean; above the UFL it is too rich to support flame propagation under the stated conditions.

Flammability limits depend on temperature, pressure, oxidizer concentration, and mixture composition. Do not treat a tabulated value as universal outside its test basis.

![FIG-02-20-001: Fuel concentration axis showing too-lean region, flammable region between LFL/UFL, and too-rich region.](../figures/FIG-02-20-001-combustion-and-the-flammable-range.png)

### Worked Example 1 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **flammability range** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 20.2 Autoignition and Limiting Oxygen Concentration

The Handbook defines **autoignition temperature (AIT)** as the minimum temperature above which no external ignition source is required to initiate combustion.

It defines **limiting oxygen concentration (LOC)** as the oxygen concentration below which combustion is not possible for the stated system.

Inerting reduces oxygen concentration, while temperature control helps avoid autoignition. Both require validated process data and controls.

![FIG-02-20-002: Combustion envelope plotting fuel concentration and temperature/oxygen effects, with LFL/UFL, AIT, and LOC boundaries.](../figures/FIG-02-20-002-autoignition-and-limiting-oxygen-concentration.png)

### Worked Example 2 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **AIT and LOC** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 20.3 Flammable Gas Mixtures — Le Chatelier's Rule

The Handbook gives an empirical rule for mixtures of flammable gases. In fuel-mixture form,

\[
LFL_m=\frac{100}{\sum_i C_{fi}/LFL_i},
\]

where \(C_{fi}\) is the volume percent of fuel component \(i\) in the fuel mixture.

Use consistent percent units. The rule estimates the lower limit for the combined fuel mixture; it does not predict all explosion behavior.

![FIG-02-20-003: Two fuel components with individual LFLs combined through Le Chatelier reciprocal-sum equation to produce mixture LFL.](../figures/FIG-02-20-003-flammable-gas-mixtures-le-chatelier-s-rule.png)

### Worked Example 3 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **mixture LFL** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 20.4 Confined Spaces and Permit-Required Hazards

The Handbook describes confined spaces as spaces with limited/restricted entry or exit and not designed for continuous occupancy. Permit-required spaces may contain hazardous atmospheres, engulfment hazards, inwardly converging geometry, or other serious hazards.

Examples include tanks, bins, pits, silos, process vessels, vaults, and pipelines.

Entry planning must address isolation, atmospheric testing, ventilation, communication, rescue, and other requirements of the applicable standard.

![FIG-02-20-004: Confined-space entry schematic with isolation, ventilation, atmospheric monitor, attendant, entrant, communication, and rescue provisions.](../figures/FIG-02-20-004-confined-spaces-and-permit-required-hazards.png)

### Worked Example 4 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **confined space** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 20.5 Gas Detection and Sensor Placement

The Handbook notes that sensor placement should consider gas molecular weight relative to air and source location. It gives examples: methane is lighter than air, while carbon dioxide and hydrogen sulfide may accumulate low.

Real airflow, temperature, turbulence, process release point, and enclosure geometry can dominate simple density reasoning.

A multi-gas monitor often checks oxygen plus combustible and toxic gases. Follow the instrument's calibration, bump-test, alarm, and sampling requirements.

![FIG-02-20-005: Vertical confined-space section showing possible high/low gas accumulation zones and multi-level sampling points, with airflow/source-location caveat.](../figures/FIG-02-20-005-gas-detection-and-sensor-placement.png)

### Worked Example 5 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **gas monitoring** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 20.6 Electrical Shock Hazards

The Handbook provides a table of probable human-body effects versus current. Effects progress from perception around the milliampere level through loss of muscular control, respiratory arrest, ventricular fibrillation, burns, and cardiac arrest at higher currents.

Voltage alone does not determine injury; current path, skin/contact resistance, duration, frequency, and body condition matter.

Engineering controls include de-energization, guarding, insulation, grounding/bonding, protective devices, safe approach boundaries, and appropriate PPE.

![FIG-02-20-006: Current-through-body severity chart using the Handbook current ranges, with qualitative effects from perception through fibrillation and severe burns.](../figures/FIG-02-20-006-electrical-shock-hazards.png)

### Worked Example 6 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **electrical safety** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 20.7 Energy Isolation and Integrated Hazard Control

Lockout/tagout (LOTO) is a guide-developed safety framework for controlling hazardous energy during servicing and maintenance. The core sequence is identify energy sources, shut down, isolate, apply locks/tags, dissipate stored energy, verify zero-energy state, perform work, and restore under controlled procedure.

Fire, confined-space, and electrical hazards often overlap. A tank entry may involve flammable vapor, oxygen deficiency, agitator energy, static ignition, and electrical equipment simultaneously.

The safest plan treats hazards as a system rather than as isolated checklist items.

![FIG-02-20-007: LOTO and confined-space integrated isolation flow showing electrical, pressure, mechanical, chemical, and thermal energy sources verified before work.](../figures/FIG-02-20-007-energy-isolation-and-integrated-hazard-control.png)

### Worked Example 7 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **energy isolation** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Safety pp. 21–23**.

**Source boundary:** The Handbook directly supplies flammability definitions/LFL/UFL, Le Chatelier mixture rule, LOC/AIT definitions, confined-space criteria and gas notes, and electrical-shock current effects. Fire tetrahedron, lockout/tagout, and general prevention hierarchy are guide-developed.

---

## Where This Goes Wrong

**Using flammability range without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using AIT and LOC without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using mixture LFL without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using confined space without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using gas monitoring without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using electrical safety without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using energy isolation without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Replacing supplied data with a memorized trend.** If the Handbook or problem gives specific property, potential, limit, or compatibility data, use it.


---

## Key Terms

| Term | Working definition |
|---|---|
| lower flammability limit | Term introduced in this chapter; use the definition and conditions in the owning section. |
| upper flammability limit | Term introduced in this chapter; use the definition and conditions in the owning section. |
| flammable range | Term introduced in this chapter; use the definition and conditions in the owning section. |
| autoignition temperature | Term introduced in this chapter; use the definition and conditions in the owning section. |
| limiting oxygen concentration | Term introduced in this chapter; use the definition and conditions in the owning section. |
| Le Chatelier flammability rule | Term introduced in this chapter; use the definition and conditions in the owning section. |
| mixture LFL | Term introduced in this chapter; use the definition and conditions in the owning section. |
| confined space | Term introduced in this chapter; use the definition and conditions in the owning section. |
| permit-required confined space | Term introduced in this chapter; use the definition and conditions in the owning section. |
| gas detector | Term introduced in this chapter; use the definition and conditions in the owning section. |
| sensor placement | Term introduced in this chapter; use the definition and conditions in the owning section. |
| oxygen deficiency | Term introduced in this chapter; use the definition and conditions in the owning section. |
| electric shock | Term introduced in this chapter; use the definition and conditions in the owning section. |
| let-go current | Term introduced in this chapter; use the definition and conditions in the owning section. |
| ventricular fibrillation | Term introduced in this chapter; use the definition and conditions in the owning section. |
| lockout tagout | Term introduced in this chapter; use the definition and conditions in the owning section. |
| hazardous energy isolation | Term introduced in this chapter; use the definition and conditions in the owning section. |

---

## Review Questions

### Conceptual and Applied

1. Define **flammability range** and state its engineering significance.

2. Define **AIT and LOC** and state its engineering significance.

3. Define **mixture LFL** and state its engineering significance.

4. Define **confined space** and state its engineering significance.

5. Define **gas monitoring** and state its engineering significance.

6. Define **electrical safety** and state its engineering significance.

7. Define **energy isolation** and state its engineering significance.

8. What error is likely if **flammability range** is used without checking the problem's state, composition, units, or assumptions?

9. What error is likely if **AIT and LOC** is used without checking the problem's state, composition, units, or assumptions?

10. What error is likely if **mixture LFL** is used without checking the problem's state, composition, units, or assumptions?

11. What error is likely if **confined space** is used without checking the problem's state, composition, units, or assumptions?

12. What error is likely if **gas monitoring** is used without checking the problem's state, composition, units, or assumptions?

13. What error is likely if **electrical safety** is used without checking the problem's state, composition, units, or assumptions?

14. What error is likely if **energy isolation** is used without checking the problem's state, composition, units, or assumptions?

15. Identify one Handbook table, equation, or definition you would locate before solving a representative problem from this chapter.

16. State one physical-reasonableness or dimensional check appropriate to this chapter.

17. Explain when measured or tabulated data should replace a qualitative trend.

18. Give one example of an interpretation in this chapter that is guide-developed rather than a verbatim Handbook rule.

### Multiple Choice

19. Which answer best describes **flammability range**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

20. Which answer best describes **AIT and LOC**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

21. Which answer best describes **mixture LFL**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

22. Which answer best describes **confined space**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

23. Which answer best describes **gas monitoring**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

24. Which answer best describes **electrical safety**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

25. Which answer best describes **energy isolation**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

26. Which answer best describes **flammability range**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

27. Which answer best describes **AIT and LOC**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data


---

## Answer Key with Explanations

1. **flammability range** is the central concept of §20.1; apply the definition, assumptions, and engineering consequence developed in that section.

2. **AIT and LOC** is the central concept of §20.2; apply the definition, assumptions, and engineering consequence developed in that section.

3. **mixture LFL** is the central concept of §20.3; apply the definition, assumptions, and engineering consequence developed in that section.

4. **confined space** is the central concept of §20.4; apply the definition, assumptions, and engineering consequence developed in that section.

5. **gas monitoring** is the central concept of §20.5; apply the definition, assumptions, and engineering consequence developed in that section.

6. **electrical safety** is the central concept of §20.6; apply the definition, assumptions, and engineering consequence developed in that section.

7. **energy isolation** is the central concept of §20.7; apply the definition, assumptions, and engineering consequence developed in that section.

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

19. **A.** The chapter applies **flammability range** only under its stated physical/model assumptions.

20. **A.** The chapter applies **AIT and LOC** only under its stated physical/model assumptions.

21. **A.** The chapter applies **mixture LFL** only under its stated physical/model assumptions.

22. **A.** The chapter applies **confined space** only under its stated physical/model assumptions.

23. **A.** The chapter applies **gas monitoring** only under its stated physical/model assumptions.

24. **A.** The chapter applies **electrical safety** only under its stated physical/model assumptions.

25. **A.** The chapter applies **energy isolation** only under its stated physical/model assumptions.

26. **A.** The chapter applies **flammability range** only under its stated physical/model assumptions.

27. **A.** The chapter applies **AIT and LOC** only under its stated physical/model assumptions.


---

## Practice Problems

1. 1. A gas has LFL=4% and UFL=15%. Classify mixtures at 2%, 8%, and 20%.

2. 2. Define AIT.

3. 3. Define LOC.

4. 4. A fuel blend contains 40% fuel A with LFL 2% and 60% fuel B with LFL 5%. Estimate mixture LFL using Le Chatelier's rule.

5. 5. Give two characteristics that make a space permit-required under the Handbook description.

6. 6. Why can gas molecular weight alone be insufficient for deciding sensor location?

7. 7. Which Handbook gas is lighter than air: methane or carbon dioxide?

8. 8. Which Handbook gas can accumulate low and has a rotten-egg odor at low concentration: H2S or methane?

9. 9. Why is de-energization preferable to relying only on electrical PPE when feasible?

10. 10. State the purpose of verifying a zero-energy state during LOTO.


---

## Practice Problem Solutions

1. 1. 2%: below LFL/too lean; 8%: within flammable range; 20%: above UFL/too rich under the stated conditions.

2. 2. Lowest temperature above which no external ignition source is required for ignition under the stated test basis.

3. 3. Oxygen concentration below which combustion is not possible for the stated system.

4. 4. LFLm=100/[40/2+60/5]=100/32=3.125 vol%.

5. 5. Any two: hazardous atmosphere, engulfment potential, trapping/asphyxiating geometry, or other serious recognized hazard.

6. 6. Airflow, turbulence, temperature, release source, and enclosure geometry can dominate simple density stratification.

7. 7. Methane.

8. 8. Hydrogen sulfide.

9. 9. Removing hazardous energy reduces the source risk rather than relying on a barrier worn by the worker.

10. 10. Confirm isolation and stored-energy control are effective before contact/work begins.


---

## Quick Reference

**Handbook anchor:** Safety pp. 21–23.

- **flammability range:** Combustion and the Flammable Range
- **AIT and LOC:** Autoignition and Limiting Oxygen Concentration
- **mixture LFL:** Flammable Gas Mixtures — Le Chatelier's Rule
- **confined space:** Confined Spaces and Permit-Required Hazards
- **gas monitoring:** Gas Detection and Sensor Placement
- **electrical safety:** Electrical Shock Hazards
- **energy isolation:** Energy Isolation and Integrated Hazard Control

---

## What's Next

**02-21 — Toxicology, Exposure Limits, Risk, and Chemical Compatibility**

Carry forward the rule: identify the physical model and service condition before selecting the formula, property, or safety control.

— Your Mentor
