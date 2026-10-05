---
chapter: "02-21"
title: "Toxicology, Exposure Limits, Risk, and Chemical Compatibility"
layer: 2
tier: B
template: technical
ledger_ids: [SAFE-2B-021-01, SAFE-2B-021-02, SAFE-2B-021-03, SAFE-2B-021-04, SAFE-2B-021-05, SAFE-2B-021-06, SAFE-2B-021-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-21: Toxicology, Exposure Limits, Risk, and Chemical Compatibility

> *"Physical science becomes engineering when the microscopic model, measured property, and safety consequence are connected explicitly."*

---

## Before You Start

**Prerequisites:** 02-20 · 01-28

**Skip if:** You can solve the calculation and scenario checks in this chapter while stating the assumptions and Handbook source used.

**Time:** About 85–115 min reading and worked examples · 40–50 min review questions · 60–80 min practice problems.

---

## On the Board Today

The Handbook directly supplies dose-response definitions, LD50/LC50, chemical interaction types, exposure-limit examples, carcinogenic risk relation, noncarcinogen hazard index/RfD/NOAEL relations, and chemical compatibility/corrosion charts. Detailed exposure assessment workflow is guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **21.1** Explain and apply **Dose-Response, LD50, and LC50**.
* **21.2** Explain and apply **Exposure Routes, Dose, and Chronic Daily Intake**.
* **21.3** Explain and apply **Carcinogenic Risk**.
* **21.4** Explain and apply **Noncarcinogenic Risk — RfD and Hazard Index**.
* **21.5** Explain and apply **Workplace Exposure Limits**.
* **21.6** Explain and apply **Chemical Interaction Effects**.
* **21.7** Explain and apply **Chemical Compatibility and Storage Segregation**.

---

## Notation Used Here

Notation is introduced within each section where needed. Use SI units unless a problem or Handbook table specifies another basis.

---

## 21.1 Dose-Response, LD50, and LC50

A dose-response curve relates administered dose to the fraction of a test population experiencing a defined response.

The Handbook defines:

- \(LD_{50}\): median lethal dose expected to kill 50% of a test group, commonly by oral/dermal exposure,
- \(LC_{50}\): median lethal concentration in air expected to kill 50% under the specified exposure duration.

Lower LD50 does not mean "more dangerous in every situation"; toxicity must be combined with realistic exposure.

![FIG-02-21-001: Sigmoidal dose-response curve on log-dose axis with LD10 and LD50 marked and separate LC50 air-exposure concept.](../figures/FIG-02-21-001-dose-response-ld50-and-lc50.png)

### Worked Example 1 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **acute toxicity** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 21.2 Exposure Routes, Dose, and Chronic Daily Intake

Exposure may occur by inhalation, ingestion, dermal contact, or other routes. Dose normalizes chemical intake to body mass and time.

The Handbook expresses dose generically as chemical mass divided by body weight and exposure time. Environmental risk calculations often use chronic daily intake (CDI).

A complete exposure assessment requires concentration, contact rate, frequency, duration, body weight, and averaging time appropriate to the model.

![FIG-02-21-002: Source-to-receptor pathway showing source, transport medium, exposure point, inhalation/ingestion/dermal route, intake, and dose.](../figures/FIG-02-21-002-exposure-routes-dose-and-chronic-daily-intake.png)

### Worked Example 2 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **exposure assessment** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 21.3 Carcinogenic Risk

The Handbook gives the carcinogenic risk relation

\[
Risk=CDI\times CSF,
\]

where \(CSF\) is the cancer slope factor.

The Handbook notes an EPA risk-management range of \(10^{-4}\) to \(10^{-6}\) in the context presented.

This relation is model-specific. Use the units and averaging basis supplied in the problem and do not mix noncarcinogenic reference-dose methods with cancer-slope-factor calculations.

![FIG-02-21-003: Linear low-dose carcinogenic risk model showing CDI multiplied by CSF to obtain incremental risk.](../figures/FIG-02-21-003-carcinogenic-risk.png)

### Worked Example 3 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **cancer risk** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 21.4 Noncarcinogenic Risk — RfD and Hazard Index

For noncarcinogens the Handbook gives

\[
HI=\frac{CDI}{RfD}.
\]

It notes that \(HI>1\) represents the possibility of adverse effects in the stated framework.

The reference dose may be estimated from a no-observed-adverse-effect level:

\[
RfD=\frac{NOAEL}{UF},
\]

where \(UF\) is a total uncertainty factor.

A hazard index is not a probability of illness; it is a screening ratio.

![FIG-02-21-004: NOAEL divided by uncertainty factor to RfD, then CDI/RfD to hazard index, with HI=1 screening boundary.](../figures/FIG-02-21-004-noncarcinogenic-risk-rfd-and-hazard-index.png)

### Worked Example 4 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **noncarcinogen risk** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 21.5 Workplace Exposure Limits

The Handbook provides example workplace exposure levels and defines threshold limit value (TLV) in its source context. SDS Section 8 may list OSHA permissible exposure limits (PELs), TLVs, engineering controls, and PPE.

Exposure limits can differ by agency, averaging time, ceiling/short-term basis, and revision date. Always identify which limit the problem gives.

A measured concentration below one limit is not automatically below every applicable occupational limit.

![FIG-02-21-005: Exposure-limit chart comparing TWA, short-term, and ceiling concepts with a concentration-versus-time trace.](../figures/FIG-02-21-005-workplace-exposure-limits.png)

### Worked Example 5 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **exposure limits** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 21.6 Chemical Interaction Effects

The Handbook distinguishes:

- **additive** effects — combined effect equals sum of individual effects,
- **synergistic** effects — combined effect exceeds simple addition,
- **antagonistic** effects — combined effect is less than simple addition.

Mixture exposure cannot always be evaluated by examining each chemical independently. The interaction mechanism and target organ matter.

If the problem supplies a specific mixture formula or interaction factor, use it rather than assuming additivity.

![FIG-02-21-006: Three interaction panels comparing additive, synergistic, and antagonistic combined toxicity using simple numeric examples.](../figures/FIG-02-21-006-chemical-interaction-effects.png)

### Worked Example 6 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **chemical interactions** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## 21.7 Chemical Compatibility and Storage Segregation

The Handbook includes a chemical-compatibility chart and detailed corrosion/compatibility data for construction materials.

Compatibility questions include two different ideas:

1. **reactive compatibility** — can two chemicals safely contact or be stored together?
2. **materials compatibility** — can the container, gasket, piping, lining, or PPE resist the chemical under the actual concentration and temperature?

Never infer compatibility from chemical family name alone. Use verified compatibility data at the actual service condition.

![FIG-02-21-007: Chemical compatibility matrix with reaction codes plus a separate material-compatibility panel showing concentration and temperature dependence.](../figures/FIG-02-21-007-chemical-compatibility-and-storage-segregation.png)

### Worked Example 7 — Model Check

Before calculation, identify the governing state, composition, reaction, exposure route, or material service condition. Then apply **chemical compatibility** only within those assumptions. Use Handbook/problem data when supplied instead of substituting a remembered trend.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Safety pp. 23–28**.

**Source boundary:** The Handbook directly supplies dose-response definitions, LD50/LC50, chemical interaction types, exposure-limit examples, carcinogenic risk relation, noncarcinogen hazard index/RfD/NOAEL relations, and chemical compatibility/corrosion charts. Detailed exposure assessment workflow is guide-developed.

---

## Where This Goes Wrong

**Using acute toxicity without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using exposure assessment without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using cancer risk without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using noncarcinogen risk without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using exposure limits without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using chemical interactions without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Using chemical compatibility without its conditions.** Check the state, units, composition, reaction basis, service environment, or exposure assumptions first.

**Replacing supplied data with a memorized trend.** If the Handbook or problem gives specific property, potential, limit, or compatibility data, use it.


---

## Key Terms

| Term | Working definition |
|---|---|
| dose-response curve | Term introduced in this chapter; use the definition and conditions in the owning section. |
| LD50 | Term introduced in this chapter; use the definition and conditions in the owning section. |
| LC50 | Term introduced in this chapter; use the definition and conditions in the owning section. |
| exposure route | Term introduced in this chapter; use the definition and conditions in the owning section. |
| dose | Term introduced in this chapter; use the definition and conditions in the owning section. |
| chronic daily intake | Term introduced in this chapter; use the definition and conditions in the owning section. |
| cancer slope factor | Term introduced in this chapter; use the definition and conditions in the owning section. |
| carcinogenic risk | Term introduced in this chapter; use the definition and conditions in the owning section. |
| hazard index | Term introduced in this chapter; use the definition and conditions in the owning section. |
| reference dose | Term introduced in this chapter; use the definition and conditions in the owning section. |
| NOAEL | Term introduced in this chapter; use the definition and conditions in the owning section. |
| uncertainty factor | Term introduced in this chapter; use the definition and conditions in the owning section. |
| permissible exposure limit | Term introduced in this chapter; use the definition and conditions in the owning section. |
| threshold limit value | Term introduced in this chapter; use the definition and conditions in the owning section. |
| time-weighted average | Term introduced in this chapter; use the definition and conditions in the owning section. |
| additive effect | Term introduced in this chapter; use the definition and conditions in the owning section. |
| synergistic effect | Term introduced in this chapter; use the definition and conditions in the owning section. |
| antagonistic effect | Term introduced in this chapter; use the definition and conditions in the owning section. |
| reactive compatibility | Term introduced in this chapter; use the definition and conditions in the owning section. |
| materials compatibility | Term introduced in this chapter; use the definition and conditions in the owning section. |
| storage segregation | Term introduced in this chapter; use the definition and conditions in the owning section. |

---

## Review Questions

### Conceptual and Applied

1. Define **acute toxicity** and state its engineering significance.

2. Define **exposure assessment** and state its engineering significance.

3. Define **cancer risk** and state its engineering significance.

4. Define **noncarcinogen risk** and state its engineering significance.

5. Define **exposure limits** and state its engineering significance.

6. Define **chemical interactions** and state its engineering significance.

7. Define **chemical compatibility** and state its engineering significance.

8. What error is likely if **acute toxicity** is used without checking the problem's state, composition, units, or assumptions?

9. What error is likely if **exposure assessment** is used without checking the problem's state, composition, units, or assumptions?

10. What error is likely if **cancer risk** is used without checking the problem's state, composition, units, or assumptions?

11. What error is likely if **noncarcinogen risk** is used without checking the problem's state, composition, units, or assumptions?

12. What error is likely if **exposure limits** is used without checking the problem's state, composition, units, or assumptions?

13. What error is likely if **chemical interactions** is used without checking the problem's state, composition, units, or assumptions?

14. What error is likely if **chemical compatibility** is used without checking the problem's state, composition, units, or assumptions?

15. Identify one Handbook table, equation, or definition you would locate before solving a representative problem from this chapter.

16. State one physical-reasonableness or dimensional check appropriate to this chapter.

17. Explain when measured or tabulated data should replace a qualitative trend.

18. Give one example of an interpretation in this chapter that is guide-developed rather than a verbatim Handbook rule.

### Multiple Choice

19. Which answer best describes **acute toxicity**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

20. Which answer best describes **exposure assessment**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

21. Which answer best describes **cancer risk**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

22. Which answer best describes **noncarcinogen risk**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

23. Which answer best describes **exposure limits**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

24. Which answer best describes **chemical interactions**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

25. Which answer best describes **chemical compatibility**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

26. Which answer best describes **acute toxicity**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data

27. Which answer best describes **exposure assessment**?
A) A conditional engineering concept used under stated assumptions
B) A universal rule independent of conditions
C) A unit-conversion constant only
D) A substitute for verified data


---

## Answer Key with Explanations

1. **acute toxicity** is the central concept of §21.1; apply the definition, assumptions, and engineering consequence developed in that section.

2. **exposure assessment** is the central concept of §21.2; apply the definition, assumptions, and engineering consequence developed in that section.

3. **cancer risk** is the central concept of §21.3; apply the definition, assumptions, and engineering consequence developed in that section.

4. **noncarcinogen risk** is the central concept of §21.4; apply the definition, assumptions, and engineering consequence developed in that section.

5. **exposure limits** is the central concept of §21.5; apply the definition, assumptions, and engineering consequence developed in that section.

6. **chemical interactions** is the central concept of §21.6; apply the definition, assumptions, and engineering consequence developed in that section.

7. **chemical compatibility** is the central concept of §21.7; apply the definition, assumptions, and engineering consequence developed in that section.

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

19. **A.** The chapter applies **acute toxicity** only under its stated physical/model assumptions.

20. **A.** The chapter applies **exposure assessment** only under its stated physical/model assumptions.

21. **A.** The chapter applies **cancer risk** only under its stated physical/model assumptions.

22. **A.** The chapter applies **noncarcinogen risk** only under its stated physical/model assumptions.

23. **A.** The chapter applies **exposure limits** only under its stated physical/model assumptions.

24. **A.** The chapter applies **chemical interactions** only under its stated physical/model assumptions.

25. **A.** The chapter applies **chemical compatibility** only under its stated physical/model assumptions.

26. **A.** The chapter applies **acute toxicity** only under its stated physical/model assumptions.

27. **A.** The chapter applies **exposure assessment** only under its stated physical/model assumptions.


---

## Practice Problems

1. 1. Which indicates greater acute toxicity in an LD50 comparison: 5 mg/kg or 500 mg/kg?

2. 2. Define LC50.

3. 3. If CDI=2×10−6 mg/kg·day and CSF=0.5 (mg/kg·day)−1, find modeled carcinogenic risk.

4. 4. If NOAEL=20 mg/kg·day and UF=100, find RfD.

5. 5. If CDI=0.05 mg/kg·day and RfD=0.20 mg/kg·day, find HI.

6. 6. Interpret HI=2.0 using the Handbook screening statement.

7. 7. Classify combined toxicity 2+3=5, 2+3=20, and 6+6=8 as additive, synergistic, or antagonistic.

8. 8. Distinguish PEL from TLV conceptually.

9. 9. Why must chemical compatibility be checked at actual concentration and temperature?

10. 10. What is the difference between reactive compatibility and materials compatibility?


---

## Practice Problem Solutions

1. 1. 5 mg/kg, because a lower median lethal dose indicates greater acute toxicity under comparable test conditions.

2. 2. Median lethal airborne concentration expected to kill 50% of a test group under the specified exposure duration.

3. 3. Risk=2×10−6×0.5=1×10−6.

4. 4. RfD=20/100=0.20 mg/kg·day.

5. 5. HI=0.05/0.20=0.25.

6. 6. It exceeds 1, indicating the possibility of adverse effects under the Handbook screening framework; it is not a probability.

7. 7. Additive; synergistic; antagonistic.

8. 8. PEL is an OSHA regulatory exposure limit; TLV is a threshold guideline from a different authority/source context. Use the limit specified by the problem.

9. 9. Corrosion, permeation, swelling, reaction rate, and decomposition can change strongly with concentration and temperature.

10. 10. Reactive compatibility asks whether chemicals can contact/mix safely; materials compatibility asks whether equipment/PPE materials resist the chemical service.


---

## Quick Reference

**Handbook anchor:** Safety pp. 23–28.

- **acute toxicity:** Dose-Response, LD50, and LC50
- **exposure assessment:** Exposure Routes, Dose, and Chronic Daily Intake
- **cancer risk:** Carcinogenic Risk
- **noncarcinogen risk:** Noncarcinogenic Risk — RfD and Hazard Index
- **exposure limits:** Workplace Exposure Limits
- **chemical interactions:** Chemical Interaction Effects
- **chemical compatibility:** Chemical Compatibility and Storage Segregation

---

## What's Next

**02-22 — Constructing a Free-Body Diagram**

Carry forward the rule: identify the physical model and service condition before selecting the formula, property, or safety control.

— Your Mentor
