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

**Solution.** Turbidity is primarily a physical/optical characteristic; BOD reflects biodegradable organic demand; ammonia is a nutrient/reduced nitrogen species; hardness is largely an inorganic-ion characteristic; and coliform counts are microbiological indicators. Treating them as one interchangeable 'water quality' metric would obscure process selection.

---

## 56.2 Mass loading and removal efficiency

Removal efficiency is concentration-based only when influent and effluent flow are equal or when the problem defines it that way. Mass-rate removal is more general.

\[\eta=\frac{C_{in}-C_{out}}{C_{in}}\times100\%\]

![FIG-03-56-002: Treatment unit with Qin,Cin,Qout,Cout and mass-loading/removal terms.](../figures/FIG-03-56-002-mass-loading-and-removal-efficiency.png)

### Worked Example 2

**Problem.** 100 mg/L reduced to 20 mg/L gives 80% concentration removal.

**Solution.** Removal efficiency is \(\eta=(100\ {\rm mg/L}-20\ {\rm mg/L})/(100\ {\rm mg/L})\times100\%=\mathbf{80\%}\). This is concentration removal and assumes influent and effluent flows are comparable for the stated calculation.

---

## 56.3 Screening, grit removal, and headworks

Headworks protect downstream equipment by removing screenings, grit, and debris and by measuring or distributing flow.

\[\text{coarse solids/grit removal precedes downstream treatment}\]

![FIG-03-56-003: Wastewater headworks train with bar screen, comminution option, grit chamber, and flow measurement.](../figures/FIG-03-56-003-screening-grit-removal-and-headworks.png)

### Worked Example 3

**Problem.** Grit removal targets dense inorganic particles rather than dissolved organics.

**Solution.** Grit chambers target dense, settleable inorganic material such as sand and gravel so it does not abrade or accumulate in downstream equipment. They are not intended to remove dissolved organic matter.

---

## 56.4 Sedimentation and clarification

Ideal discrete settling performance is often organized around surface overflow rate. Clarifier behavior also depends on particle interactions, sludge zones, and hydraulics.

\[v_o=\frac{Q}{A_s}\]

![FIG-03-56-004: Circular or rectangular clarifier with settling zone, overflow rate, sludge withdrawal, and effluent weir.](../figures/FIG-03-56-004-sedimentation-and-clarification.png)

### Worked Example 4

**Problem.** A flow of 2,000 m³/day over 200 m² gives overflow rate 10 m/day.

**Solution.** Surface overflow rate is \(v_o=Q/A_s=(2000\ {\rm m^3/day})/(200\ {\rm m^2})=\mathbf{10\ m/day}\). The area is plan surface area, not tank sidewall area.

---

## 56.5 Filtration and granular-media concepts

Filters remove suspended material by transport and attachment within porous media. Head loss rises as solids accumulate, eventually requiring cleaning/backwash.

\[\text{loading rate}=\frac{Q}{A}\]

![FIG-03-56-005: Rapid granular filter with media layers, underdrain, influent, effluent, and backwash flow.](../figures/FIG-03-56-005-filtration-and-granular-media-concepts.png)

### Worked Example 5

**Problem.** Doubling flow through the same filter area doubles hydraulic loading rate.

**Solution.** Hydraulic loading is \(Q/A\). If filter area stays fixed and flow doubles, the loading rate also **doubles**, which can change head loss, run length, and effluent quality.

---

## 56.6 Adsorption and activated carbon

Activated carbon removes many dissolved organic contaminants by adsorption. Isotherms describe equilibrium loading; breakthrough governs fixed-bed operation.

\[q=\frac{\text{mass adsorbed}}{\text{mass adsorbent}}\]

![FIG-03-56-006: GAC contactor with concentration breakthrough curve and adsorption-zone movement.](../figures/FIG-03-56-006-adsorption-and-activated-carbon.png)

### Worked Example 6

**Problem.** A bed is not fully effective forever; breakthrough advances as adsorption capacity is used.

**Solution.** Adsorbent capacity is finite. As upstream sites are occupied, the mass-transfer zone advances through the bed until contaminant appears at the effluent—**breakthrough**—so a fixed bed cannot be assumed fully effective indefinitely.

---

## 56.7 Membranes, air stripping, and physical-process selection

Membranes separate by selective transport and pressure/osmotic driving force; air stripping transfers volatile contaminants from water to gas. Process selection follows contaminant properties and treatment objectives.

\[\text{process selection}=f(\text{contaminant size/volatility/phase, target, fouling, energy})\]

![FIG-03-56-007: Membrane, air stripper, filtration, sedimentation, and adsorption processes mapped to contaminant properties.](../figures/FIG-03-56-007-membranes-air-stripping-and-physical-process-selection.png)

### Worked Example 7

**Problem.** A highly volatile dissolved organic may be more amenable to air stripping than a nonvolatile dissolved salt.

**Solution.** Air stripping is favored for sufficiently volatile compounds that partition from water to gas. A nonvolatile dissolved salt has little tendency to transfer to air and therefore requires a different separation mechanism.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** A negative effluent concentration or removal above 100% is impossible for a simple concentration-removal calculation. Recheck flow basis, influent/effluent units, residual streams, and whether the selected process relation applies.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** For **Water/Wastewater Characteristics, Loading Rates, and Physical Treatment**, the FE Reference Handbook equation, definitions, and unit convention govern whenever the Handbook supplies the needed relation. The external references in this chapter are used for specification-required learned material involving **water-quality characteristics, physical treatment, clarification, filtration, adsorption, and stripping**. If a remembered correlation conflicts with the supplied Handbook equation, use the supplied Handbook relation unless the problem explicitly states a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 12; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required environmental-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects the Handbook and external material into exam-oriented explanations, examples, and checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Mihelcic, J. R., & Zimmerman, J. B. (2021). *Environmental Engineering: Fundamentals, Sustainability, Design* (3rd ed.). Wiley. ISBN 978-1-119-60445-7. Supporting scope: Environmental measurements, chemistry, physical processes, biology, risk, water quantity/quality, water treatment, wastewater/stormwater, solid waste, and air quality.
- Metcalf & Eddy/AECOM, Tchobanoglous, G., Stensel, H. D., Tsuchihashi, R., & Burton, F. L. (2014). *Wastewater Engineering: Treatment and Resource Recovery* (5th ed.). McGraw-Hill. ISBN 978-0-07-340118-8. Supporting scope: Wastewater characteristics, physical/chemical treatment, activated sludge, solids recycle, biosolids, residuals, and resource recovery.

The external references support only the learned/application portion of the Environmental specification. They do not replace the FE Reference Handbook as the exam reference.

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

15. In **Water/Wastewater Characteristics, Loading Rates, and Physical Treatment**, the control volume or conceptual boundary determines which sources, sinks, transfers, reactions, and receptors belong in the model. For this chapter specifically, check influent/effluent flow basis, loading units, surface/filtration area definitions, removal bounds from 0–100%, and whether the contaminant property matches the selected physical process.

16. Concentration and loading answer different questions in **Water/Wastewater Characteristics, Loading Rates, and Physical Treatment**: concentration is mass per volume, while loading is mass per time. Always convert \(Q\) and \(C\) to compatible units before multiplying them.

17. Use the FE Reference Handbook equation and definitions when it supplies the model for **Water/Wastewater Characteristics, Loading Rates, and Physical Treatment**. The chapter's external references (MIHELCIC, METCALF) support learned specification content, not a competing exam formula.

18. A physical check is needed because algebra alone can return impossible environmental states. For this chapter, set \(C_{out}=C_{in}\) and confirm removal is 0%; set \(C_{out}=0\) and confirm the ideal concentration-removal expression gives 100%.

19. **A.** Section §56.1, **Physical, chemical, and biological water-quality characteristics**, is governed by \(\text{quality}=\{\text{solids, organics, nutrients, microbes, ions, physical properties}\}\). Use that relation with its own environmental basis and then perform the specific validity check described for §56.1.

20. **A.** Section §56.2, **Mass loading and removal efficiency**, is governed by \(\eta=\frac{C_{in}-C_{out}}{C_{in}}\times100\%\). Use that relation with its own environmental basis and then perform the specific validity check described for §56.2.

21. **A.** Section §56.3, **Screening, grit removal, and headworks**, is governed by \(\text{coarse solids/grit removal precedes downstream treatment}\). Use that relation with its own environmental basis and then perform the specific validity check described for §56.3.

22. **A.** Section §56.4, **Sedimentation and clarification**, is governed by \(v_o=\frac{Q}{A_s}\). Use that relation with its own environmental basis and then perform the specific validity check described for §56.4.

23. **A.** Section §56.5, **Filtration and granular-media concepts**, is governed by \(\text{loading rate}=\frac{Q}{A}\). Use that relation with its own environmental basis and then perform the specific validity check described for §56.5.

24. **A.** Section §56.6, **Adsorption and activated carbon**, is governed by \(q=\frac{\text{mass adsorbed}}{\text{mass adsorbent}}\). Use that relation with its own environmental basis and then perform the specific validity check described for §56.6.

25. **A.** Section §56.7, **Membranes, air stripping, and physical-process selection**, is governed by \(\text{process selection}=f(\text{contaminant size/volatility/phase, target, fouling, energy})\). Use that relation with its own environmental basis and then perform the specific validity check described for §56.7.

26. **A.** An integrated **Water/Wastewater Characteristics, Loading Rates, and Physical Treatment** solution is acceptable only after the governing balance/model is identified, units are reconciled, and the chapter-specific physical checks are satisfied.

27. **A.** Source ownership is explicit in **Water/Wastewater Characteristics, Loading Rates, and Physical Treatment**: FE-Handbook-supported material remains tied to the ledger, externally supported content uses MIHELCIC, METCALF, and guide synthesis is labeled as supplemental explanation.


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

1. **Independent recomputation for §56.1 — Physical, chemical, and biological water-quality characteristics.** Start from the stated givens rather than the worked-example answer. Turbidity is primarily a physical/optical characteristic; BOD reflects biodegradable organic demand; ammonia is a nutrient/reduced nitrogen species; hardness is largely an inorganic-ion characteristic; and coliform counts are microbiological indicators. Treating them as one interchangeable 'water quality' metric would obscure process selection. As a separate check, confirm the result is consistent with the section's physical interpretation.

2. **Independent recomputation for §56.2 — Mass loading and removal efficiency.** Start from the stated givens rather than the worked-example answer. Removal efficiency is \(\eta=(100-20)/100\times100\%=\mathbf{80\%}\). This is concentration removal and assumes influent and effluent flows are comparable for the stated calculation. As a separate check, confirm the result is consistent with the section's physical interpretation.

3. **Independent recomputation for §56.3 — Screening, grit removal, and headworks.** Start from the stated givens rather than the worked-example answer. Grit chambers target dense, settleable inorganic material such as sand and gravel so it does not abrade or accumulate in downstream equipment. They are not intended to remove dissolved organic matter. As a separate check, confirm the result is consistent with the section's physical interpretation.

4. **Independent recomputation for §56.4 — Sedimentation and clarification.** Start from the stated givens rather than the worked-example answer. Surface overflow rate is \(v_o=Q/A_s=(2000\ {\rm m^3/day})/(200\ {\rm m^2})=\mathbf{10\ m/day}\). The area is plan surface area, not tank sidewall area. As a separate check, confirm the result is consistent with the section's physical interpretation.

5. **Independent recomputation for §56.5 — Filtration and granular-media concepts.** Start from the stated givens rather than the worked-example answer. Hydraulic loading is \(Q/A\). If filter area stays fixed and flow doubles, the loading rate also **doubles**, which can change head loss, run length, and effluent quality. As a separate check, confirm the result is consistent with the section's physical interpretation.

6. **Independent recomputation for §56.6 — Adsorption and activated carbon.** Start from the stated givens rather than the worked-example answer. Adsorbent capacity is finite. As upstream sites are occupied, the mass-transfer zone advances through the bed until contaminant appears at the effluent—**breakthrough**—so a fixed bed cannot be assumed fully effective indefinitely. As a separate check, confirm the result is consistent with the section's physical interpretation.

7. **Independent recomputation for §56.7 — Membranes, air stripping, and physical-process selection.** Start from the stated givens rather than the worked-example answer. Air stripping is favored for sufficiently volatile compounds that partition from water to gas. A nonvolatile dissolved salt has little tendency to transfer to air and therefore requires a different separation mechanism. As a separate check, confirm the result is consistent with the section's physical interpretation.

8. For this chapter, check the result against this failure screen: Check influent/effluent flow basis, loading units, surface/filtration area definitions, removal bounds from 0–100%, and whether the contaminant property matches the selected physical process. A result that violates one of those conditions should be rejected even if the arithmetic is internally consistent.

9. For **Water/Wastewater Characteristics, Loading Rates, and Physical Treatment**, begin with the FE Environmental specification area and Handbook subsection recorded in the ledger. When the atom is `split_required`, use the reconciled external source set **MIHELCIC, METCALF** for the learned portion rather than inventing a Handbook page.

10. A useful limiting case is to set \(C_{out}=C_{in}\) and confirm removal is 0%; set \(C_{out}=0\) and confirm the ideal concentration-removal expression gives 100%. The simplified case should reduce to the stated physical behavior before the full model is trusted.

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
