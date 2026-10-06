---
chapter: "03-56"
title: "Water/Wastewater Characteristics, Loading Rates, and Physical Treatment"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-056-01, ENV-3-056-02, ENV-3-056-03, ENV-3-056-04, ENV-3-056-05, ENV-3-056-06, ENV-3-056-07]
routes: [environmental]
status: drafted
---

# Chapter 03-56: Water/Wastewater Characteristics, Loading Rates, and Physical Treatment

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** ENV-3-048-07

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Water/Wastewater Characteristics, Loading Rates, and Physical Treatment**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **56.1** Explain and apply **Physical, chemical, and biological water-quality characteristics**.
* **56.2** Explain and apply **Mass loading and removal efficiency**.
* **56.3** Explain and apply **Screening, grit removal, and headworks**.
* **56.4** Explain and apply **Sedimentation and clarification**.
* **56.5** Explain and apply **Filtration and granular-media concepts**.
* **56.6** Explain and apply **Adsorption and activated carbon**.
* **56.7** Explain and apply **Membranes, air stripping, and physical-process selection**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 56.1 Physical, chemical, and biological water-quality characteristics

Treatment design begins by characterizing the influent and target effluent. Different parameters require different analytical and treatment approaches.

\[\text{quality}=\{\text{solids, organics, nutrients, microbes, ions, physical properties}\}\]

![FIG-03-56-001: Water/wastewater characteristic categories with representative parameters and treatment relevance.](../figures/FIG-03-56-001-physical-chemical-and-biological-water-quality-characteristics.png)

### Worked Example 1

**Problem.** Turbidity, BOD, ammonia, hardness, and coliform counts represent different water-quality categories.

**Solution.** Apply the relation and environmental model in §56.1; then verify units, boundary conditions, and physical limits.

---

## 56.2 Mass loading and removal efficiency

Removal efficiency is concentration-based only when influent and effluent flow are equal or when the problem defines it that way. Mass-rate removal is more general.

\[\eta=\frac{C_{in}-C_{out}}{C_{in}}\times100\%\]

![FIG-03-56-002: Treatment unit with Qin,Cin,Qout,Cout and mass-loading/removal terms.](../figures/FIG-03-56-002-mass-loading-and-removal-efficiency.png)

### Worked Example 2

**Problem.** 100 mg/L reduced to 20 mg/L gives 80% concentration removal.

**Solution.** Apply the relation and environmental model in §56.2; then verify units, boundary conditions, and physical limits.

---

## 56.3 Screening, grit removal, and headworks

Headworks protect downstream equipment by removing screenings, grit, and debris and by measuring or distributing flow.

\[\text{coarse solids/grit removal precedes downstream treatment}\]

![FIG-03-56-003: Wastewater headworks train with bar screen, comminution option, grit chamber, and flow measurement.](../figures/FIG-03-56-003-screening-grit-removal-and-headworks.png)

### Worked Example 3

**Problem.** Grit removal targets dense inorganic particles rather than dissolved organics.

**Solution.** Apply the relation and environmental model in §56.3; then verify units, boundary conditions, and physical limits.

---

## 56.4 Sedimentation and clarification

Ideal discrete settling performance is often organized around surface overflow rate. Clarifier behavior also depends on particle interactions, sludge zones, and hydraulics.

\[v_o=\frac{Q}{A_s}\]

![FIG-03-56-004: Circular or rectangular clarifier with settling zone, overflow rate, sludge withdrawal, and effluent weir.](../figures/FIG-03-56-004-sedimentation-and-clarification.png)

### Worked Example 4

**Problem.** A flow of 2,000 m³/day over 200 m² gives overflow rate 10 m/day.

**Solution.** Apply the relation and environmental model in §56.4; then verify units, boundary conditions, and physical limits.

---

## 56.5 Filtration and granular-media concepts

Filters remove suspended material by transport and attachment within porous media. Head loss rises as solids accumulate, eventually requiring cleaning/backwash.

\[\text{loading rate}=\frac{Q}{A}\]

![FIG-03-56-005: Rapid granular filter with media layers, underdrain, influent, effluent, and backwash flow.](../figures/FIG-03-56-005-filtration-and-granular-media-concepts.png)

### Worked Example 5

**Problem.** Doubling flow through the same filter area doubles hydraulic loading rate.

**Solution.** Apply the relation and environmental model in §56.5; then verify units, boundary conditions, and physical limits.

---

## 56.6 Adsorption and activated carbon

Activated carbon removes many dissolved organic contaminants by adsorption. Isotherms describe equilibrium loading; breakthrough governs fixed-bed operation.

\[q=\frac{\text{mass adsorbed}}{\text{mass adsorbent}}\]

![FIG-03-56-006: GAC contactor with concentration breakthrough curve and adsorption-zone movement.](../figures/FIG-03-56-006-adsorption-and-activated-carbon.png)

### Worked Example 6

**Problem.** A bed is not fully effective forever; breakthrough advances as adsorption capacity is used.

**Solution.** Apply the relation and environmental model in §56.6; then verify units, boundary conditions, and physical limits.

---

## 56.7 Membranes, air stripping, and physical-process selection

Membranes separate by selective transport and pressure/osmotic driving force; air stripping transfers volatile contaminants from water to gas. Process selection follows contaminant properties and treatment objectives.

\[\text{process selection}=f(\text{contaminant size/volatility/phase, target, fouling, energy})\]

![FIG-03-56-007: Membrane, air stripper, filtration, sedimentation, and adsorption processes mapped to contaminant properties.](../figures/FIG-03-56-007-membranes-air-stripping-and-physical-process-selection.png)

### Worked Example 7

**Problem.** A highly volatile dissolved organic may be more amenable to air stripping than a nonvolatile dissolved salt.

**Solution.** Apply the relation and environmental model in §56.7; then verify units, boundary conditions, and physical limits.

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

Primary source basis: **FE Environmental specification Area(s) 12; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** Some Environmental specification topics are directly tabulated in the Handbook, while others require learned engineering knowledge. The chapter keeps those two categories separate.

---

## Where This Goes Wrong

**Using water and wastewater characteristics without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using treatment removal efficiency without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using wastewater headworks without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using sedimentation without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using granular filtration without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using activated carbon adsorption without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using physical treatment selection without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| water and wastewater characteristics | Concept developed in §56.1; apply with that section's stated environmental basis and assumptions. |
| treatment removal efficiency | Concept developed in §56.2; apply with that section's stated environmental basis and assumptions. |
| wastewater headworks | Concept developed in §56.3; apply with that section's stated environmental basis and assumptions. |
| sedimentation | Concept developed in §56.4; apply with that section's stated environmental basis and assumptions. |
| granular filtration | Concept developed in §56.5; apply with that section's stated environmental basis and assumptions. |
| activated carbon adsorption | Concept developed in §56.6; apply with that section's stated environmental basis and assumptions. |
| physical treatment selection | Concept developed in §56.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **water and wastewater characteristics** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **treatment removal efficiency** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **wastewater headworks** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **sedimentation** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **granular filtration** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **activated carbon adsorption** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **physical treatment selection** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **water and wastewater characteristics**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **treatment removal efficiency**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **wastewater headworks**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **sedimentation**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **granular filtration**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **activated carbon adsorption**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **physical treatment selection**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **water and wastewater characteristics**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **treatment removal efficiency**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **wastewater headworks**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **sedimentation**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **granular filtration**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **activated carbon adsorption**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **physical treatment selection**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **water and wastewater characteristics**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **treatment removal efficiency**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **water and wastewater characteristics** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **treatment removal efficiency** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **wastewater headworks** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **sedimentation** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **granular filtration** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **activated carbon adsorption** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **physical treatment selection** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **water and wastewater characteristics**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **treatment removal efficiency**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **wastewater headworks**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **sedimentation**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **granular filtration**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **activated carbon adsorption**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **physical treatment selection**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

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

1. Turbidity, BOD, ammonia, hardness, and coliform counts represent different water-quality categories.

2. 100 mg/L reduced to 20 mg/L gives 80% concentration removal.

3. Grit removal targets dense inorganic particles rather than dissolved organics.

4. A flow of 2,000 m³/day over 200 m² gives overflow rate 10 m/day.

5. Doubling flow through the same filter area doubles hydraulic loading rate.

6. A bed is not fully effective forever; breakthrough advances as adsorption capacity is used.

7. A highly volatile dissolved organic may be more amenable to air stripping than a nonvolatile dissolved salt.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. Use §56.1. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

2. Use §56.2. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

3. Use §56.3. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

4. Use §56.4. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

5. Use §56.5. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

6. Use §56.6. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

7. Use §56.7. The stated result follows from the displayed relation or process definition; verify the environmental basis and physical constraints.

8. Check dimensions, concentration-versus-loading basis, conservation of mass/energy, sign convention, and whether removal, risk, or efficiency values stay within physically meaningful limits.

9. Start with FE Environmental specification Area(s) 12, then use the Handbook subsection named in the corresponding ledger entry.

10. Test a limiting case such as zero source, zero reaction, complete mixing, no flow, very large residence time, or 0/100% removal as appropriate. The result should reduce to a sensible physical state.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 12.

- **water and wastewater characteristics:** Physical, chemical, and biological water-quality characteristics
- **treatment removal efficiency:** Mass loading and removal efficiency
- **wastewater headworks:** Screening, grit removal, and headworks
- **sedimentation:** Sedimentation and clarification
- **granular filtration:** Filtration and granular-media concepts
- **activated carbon adsorption:** Adsorption and activated carbon
- **physical treatment selection:** Membranes, air stripping, and physical-process selection

---

## What's Next

**Chapter 03-57: Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
