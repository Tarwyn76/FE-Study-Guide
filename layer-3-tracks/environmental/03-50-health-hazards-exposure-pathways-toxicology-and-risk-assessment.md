---
chapter: "03-50"
title: "Health Hazards, Exposure Pathways, Toxicology, and Risk Assessment"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-050-01, ENV-3-050-02, ENV-3-050-03, ENV-3-050-04, ENV-3-050-05, ENV-3-050-06, ENV-3-050-07]
routes: [environmental]
status: drafted
---

# Chapter 03-50: Health Hazards, Exposure Pathways, Toxicology, and Risk Assessment

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** SAFE-2B-019-01 · SAFE-2B-021-03 · SAFE-2B-021-04

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Health Hazards, Exposure Pathways, Toxicology, and Risk Assessment**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **50.1** Explain and apply **Hazard, exposure, dose, and risk distinctions**.
* **50.2** Explain and apply **Ingestion, inhalation, and dermal dose**.
* **50.3** Explain and apply **Noncarcinogenic hazard quotient and hazard index**.
* **50.4** Explain and apply **Carcinogenic risk**.
* **50.5** Explain and apply **Dose-response, threshold, and uncertainty concepts**.
* **50.6** Explain and apply **Occupational exposure, PPE, and noise**.
* **50.7** Explain and apply **Risk characterization and uncertainty communication**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 50.1 Hazard, exposure, dose, and risk distinctions

A hazardous substance creates risk only when an exposure pathway connects source and receptor. Separate intrinsic hazard from actual exposure and dose.

\[\text{source}\rightarrow\text{transport}\rightarrow\text{exposure point}\rightarrow\text{route}\rightarrow\text{receptor}\]

![FIG-03-50-001: Source-to-receptor exposure pathway showing release, transport, exposure point, route, and receptor.](../figures/FIG-03-50-001-hazard-exposure-dose-and-risk-distinctions.png)

### Worked Example 1

**Problem.** A contaminant sealed in an inaccessible vessel may be hazardous but present little current exposure.

**Solution.** Apply the relation and environmental model in §50.1; then verify units, boundary conditions, and physical limits.

---

## 50.2 Ingestion, inhalation, and dermal dose

Risk calculations normalize chemical intake by body weight and averaging time. The exact exposure-factor form depends on route and problem statement.

\[\mathrm{CDI}=\frac{C\,IR\,EF\,ED}{BW\,AT}\]

![FIG-03-50-002: Exposure-factor diagram linking concentration, intake rate, frequency, duration, body weight, and averaging time.](../figures/FIG-03-50-002-ingestion-inhalation-and-dermal-dose.png)

### Worked Example 2

**Problem.** Doubling concentration doubles chronic daily intake if all other exposure factors are unchanged.

**Solution.** Apply the relation and environmental model in §50.2; then verify units, boundary conditions, and physical limits.

---

## 50.3 Noncarcinogenic hazard quotient and hazard index

For noncarcinogenic effects, hazard quotient compares estimated dose to a reference dose. Hazard index aggregates relevant hazard quotients for a receptor/effect grouping.

\[HQ=\frac{\mathrm{CDI}}{\mathrm{RfD}},\qquad HI=\sum HQ_i\]

![FIG-03-50-003: Multiple exposure pathways contributing HQ values that sum to a hazard index.](../figures/FIG-03-50-003-noncarcinogenic-hazard-quotient-and-hazard-index.png)

### Worked Example 3

**Problem.** CDI equal to RfD gives HQ=1.

**Solution.** Apply the relation and environmental model in §50.3; then verify units, boundary conditions, and physical limits.

---

## 50.4 Carcinogenic risk

Carcinogenic risk is commonly estimated as lifetime average daily dose times slope factor within the low-dose model assumed by the problem.

\[\text{Risk}=\mathrm{LADD}\times SF\]

![FIG-03-50-004: Low-dose linear cancer-risk model with slope factor and a sample LADD-to-risk calculation.](../figures/FIG-03-50-004-carcinogenic-risk.png)

### Worked Example 4

**Problem.** Halving LADD halves estimated risk when slope factor is unchanged.

**Solution.** Apply the relation and environmental model in §50.4; then verify units, boundary conditions, and physical limits.

---

## 50.5 Dose-response, threshold, and uncertainty concepts

Dose-response relationships may be treated differently for carcinogenic and noncarcinogenic endpoints. Uncertainty factors reflect incomplete toxicological knowledge and population variability.

\[\text{response}=f(\text{dose})\]

![FIG-03-50-005: Threshold-style and low-dose linear dose-response curves with uncertainty bands.](../figures/FIG-03-50-005-dose-response-threshold-and-uncertainty-concepts.png)

### Worked Example 5

**Problem.** A reference dose is not a sharp boundary between safe and harmful outcomes.

**Solution.** Apply the relation and environmental model in §50.5; then verify units, boundary conditions, and physical limits.

---

## 50.6 Occupational exposure, PPE, and noise

Occupational health questions may involve chemical exposure, noise, and PPE. PPE is a control layer, not a substitute for feasible higher-order controls.

\[\text{control hierarchy: eliminate/substitute}\rightarrow\text{engineering}\rightarrow\text{administrative}\rightarrow\text{PPE}\]

![FIG-03-50-006: Environmental/occupational control hierarchy with noise and chemical exposure examples.](../figures/FIG-03-50-006-occupational-exposure-ppe-and-noise.png)

### Worked Example 6

**Problem.** Enclosing a noisy machine is an engineering control; hearing protection is PPE.

**Solution.** Apply the relation and environmental model in §50.6; then verify units, boundary conditions, and physical limits.

---

## 50.7 Risk characterization and uncertainty communication

Risk characterization combines the major assessment components and states assumptions, uncertainty, and sensitive populations. A single number without context is incomplete.

\[\text{risk characterization}=\text{hazard}+\text{dose-response}+\text{exposure}+\text{uncertainty}\]

![FIG-03-50-007: Four-step environmental risk assessment with uncertainty and risk-management interface.](../figures/FIG-03-50-007-risk-characterization-and-uncertainty-communication.png)

### Worked Example 7

**Problem.** Report both the central estimate and the assumptions that materially control it.

**Solution.** Apply the relation and environmental model in §50.7; then verify units, boundary conditions, and physical limits.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** The algebra or model assumptions are invalid for that condition. Recheck the balance, reaction/order assumptions, time basis, units, and any zero-concentration limiting condition.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** Use the Handbook relation and its definitions unless the problem explicitly supplies a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 7; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** Some Environmental specification topics are directly tabulated in the Handbook, while others require learned engineering knowledge. The chapter keeps those two categories separate.

---

## Where This Goes Wrong

**Using environmental exposure pathway without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using chronic daily intake without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using noncarcinogenic hazard quotient without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using carcinogenic risk without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using dose-response relationship without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using occupational environmental health without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental risk characterization without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| environmental exposure pathway | Concept developed in §50.1; apply with that section's stated environmental basis and assumptions. |
| chronic daily intake | Concept developed in §50.2; apply with that section's stated environmental basis and assumptions. |
| noncarcinogenic hazard quotient | Concept developed in §50.3; apply with that section's stated environmental basis and assumptions. |
| carcinogenic risk | Concept developed in §50.4; apply with that section's stated environmental basis and assumptions. |
| dose-response relationship | Concept developed in §50.5; apply with that section's stated environmental basis and assumptions. |
| occupational environmental health | Concept developed in §50.6; apply with that section's stated environmental basis and assumptions. |
| environmental risk characterization | Concept developed in §50.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **environmental exposure pathway** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **chronic daily intake** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **noncarcinogenic hazard quotient** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **carcinogenic risk** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **dose-response relationship** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **occupational environmental health** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **environmental risk characterization** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental exposure pathway**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **chronic daily intake**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **noncarcinogenic hazard quotient**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **carcinogenic risk**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **dose-response relationship**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **occupational environmental health**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental risk characterization**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **environmental exposure pathway**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **chronic daily intake**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **noncarcinogenic hazard quotient**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **carcinogenic risk**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **dose-response relationship**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **occupational environmental health**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **environmental risk characterization**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **environmental exposure pathway**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **chronic daily intake**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **environmental exposure pathway** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **chronic daily intake** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **noncarcinogenic hazard quotient** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **carcinogenic risk** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **dose-response relationship** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **occupational environmental health** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **environmental risk characterization** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **environmental exposure pathway**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **chronic daily intake**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **noncarcinogenic hazard quotient**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **carcinogenic risk**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **dose-response relationship**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **occupational environmental health**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **environmental risk characterization**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

15. The boundary determines what enters, leaves, accumulates, reacts, or transfers between media. Without it, terms are easily omitted or double counted.

16. Concentration is mass per volume; loading is mass per time. A low concentration at very high flow can still create a large load.

17. The FE Handbook is the supplied exam reference. Its variable definitions and unit conventions should govern unless the problem explicitly provides another relation.

18. A mass/energy balance and physical check can reveal impossible signs, removal above 100%, negative concentrations, unrealistic flows, or model misuse.

19. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

20. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

21. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

22. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

23. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

24. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

25. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

26. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.

27. **A.** The method depends on consistent units, boundaries, process assumptions, and the intended environmental model.


---

## Practice Problems

1. A contaminant sealed in an inaccessible vessel may be hazardous but present little current exposure.

2. Doubling concentration doubles chronic daily intake if all other exposure factors are unchanged.

3. CDI equal to RfD gives HQ=1.

4. Halving LADD halves estimated risk when slope factor is unchanged.

5. A reference dose is not a sharp boundary between safe and harmful outcomes.

6. Enclosing a noisy machine is an engineering control; hearing protection is PPE.

7. Report both the central estimate and the assumptions that materially control it.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §50.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §50.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §50.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §50.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §50.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §50.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §50.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 7, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 7.

- **environmental exposure pathway:** Hazard, exposure, dose, and risk distinctions
- **chronic daily intake:** Ingestion, inhalation, and dermal dose
- **noncarcinogenic hazard quotient:** Noncarcinogenic hazard quotient and hazard index
- **carcinogenic risk:** Carcinogenic risk
- **dose-response relationship:** Dose-response, threshold, and uncertainty concepts
- **occupational environmental health:** Occupational exposure, PPE, and noise
- **environmental risk characterization:** Risk characterization and uncertainty communication

---

## What's Next

**Chapter 03-51: Environmental Hydraulics — Conduits, Open Channels, Pumps, Blowers, and Flow Measurement**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
