---
chapter: "03-48"
title: "Population, Demand, Environmental Mass Balances, and Reactor Models"
layer: 3
tier: null
track: environmental
template: technical
ledger_ids: [ENV-3-048-01, ENV-3-048-02, ENV-3-048-03, ENV-3-048-04, ENV-3-048-05, ENV-3-048-06, ENV-3-048-07]
routes: [environmental]
status: drafted
---

# Chapter 03-48: Population, Demand, Environmental Mass Balances, and Reactor Models

> *"Environmental engineering becomes tractable when every source, pathway, control volume, transformation, and receptor is explicit."*

---

## Before You Start

**Prerequisites:** FLUID-2D-043-06

**Route:** FE Environmental. This is a Layer 3 discipline-track chapter.

**Skip if:** You can choose the appropriate environmental control volume or conceptual model, apply the correct Handbook relation or specification-required workflow, carry units consistently, and verify the result against mass/energy conservation and physical limits.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops FE Environmental material under **Population, Demand, Environmental Mass Balances, and Reactor Models**. Handbook equations are used where they are actually provided. Specification-required material that is not directly developed in Handbook 10.6 is identified as learned or guide-developed rather than assigned a false Handbook source.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **48.1** Explain and apply **Population projections and demand forecasting**.
* **48.2** Explain and apply **Control volumes, steady and unsteady environmental mass balances**.
* **48.3** Explain and apply **Concentration-flow loading calculations**.
* **48.4** Explain and apply **Reaction order and environmental decay kinetics**.
* **48.5** Explain and apply **Ideal batch and plug-flow reactors**.
* **48.6** Explain and apply **Completely mixed flow reactors**.
* **48.7** Explain and apply **Reactor selection, residence time, and model verification**.

---

## Notation Used Here

Define the control volume, constituent, phase or environmental medium, time basis, and unit system before calculation. Distinguish concentration from loading, total from dissolved/available fractions, and hydraulic residence time from biological or contaminant age when those differ.

---

## 48.1 Population projections and demand forecasting

Environmental facilities are sized from projected population and per-capita or unit demand. Distinguish arithmetic, geometric, and supplied projection methods, and keep the design horizon explicit.

\[P_t=P_0(1+r)^t,\qquad D=P_t\,d_{pc}\]

![FIG-03-48-001: Population versus time with design horizon and corresponding water, wastewater, solid-waste, and energy demand projections.](../figures/FIG-03-48-001-population-projections-and-demand-forecasting.png)

### Worked Example 1

**Problem.** A population of 50,000 growing at 1.5%/yr for 20 years becomes about 67,300 under geometric growth.

**Solution.** Use geometric growth: \(P_{20}=50{,}000(1+0.015)^{20}=67{,}342\), so the projected population is about **67,300 people**. A design-demand calculation would then multiply this population by the specified per-capita demand.

---

## 48.2 Control volumes, steady and unsteady environmental mass balances

Mass balances are the foundation of fate, treatment, and reactor calculations. Define the control volume, constituent, reaction sign convention, and whether accumulation is zero before solving.

\[\frac{dM}{dt}=\sum \dot M_{in}-\sum \dot M_{out}+rV\]

![FIG-03-48-002: Environmental control volume with flow, concentration, reaction, and accumulation terms.](../figures/FIG-03-48-002-control-volumes-steady-and-unsteady-environmental-mass-balances.png)

### Worked Example 2

**Problem.** At steady state with no reaction, 100 mg/s entering requires 100 mg/s leaving.

**Solution.** At steady state, \(dM/dt=0\). With no reaction, \(rV=0\), so the mass balance reduces to \(\sum \dot M_{in}=\sum \dot M_{out}\). Therefore an inflow of **100 mg/s** requires an outflow of **100 mg/s**.

---

## 48.3 Concentration-flow loading calculations

Loading is mass per time, not concentration. Convert flow and concentration to compatible units before multiplying; in U.S. customary wastewater work, the 8.34 factor often appears with MGD and mg/L.

\[\dot m=QC\]

![FIG-03-48-003: Pipe flow labeled Q and C feeding a daily mass-loading calculation in SI and MGD-mg/L forms.](../figures/FIG-03-48-003-concentration-flow-loading-calculations.png)

### Worked Example 3

**Problem.** 2 MGD at 15 mg/L corresponds to about 250 lb/day.

**Solution.** For wastewater units, \(\dot m=8.34QC\) with \(Q\) in MGD and \(C\) in mg/L. Thus \(\dot m=8.34(2)(15)=250.2\ {\rm lb/day}\), or about **250 lb/day**.

---

## 48.4 Reaction order and environmental decay kinetics

Zero-, first-, and second-order decay have different concentration-time relationships and different units for k. Do not use a first-order exponential unless the process is modeled as first order.

\[r=-kC^n\]

![FIG-03-48-004: Zero-, first-, and second-order concentration decay curves with rate-law forms and k units.](../figures/FIG-03-48-004-reaction-order-and-environmental-decay-kinetics.png)

### Worked Example 4

**Problem.** For first-order decay with k=0.20 day^-1, half-life is ln2/k≈3.47 days.

**Solution.** For first-order decay, \(t_{1/2}=\ln 2/k\). With \(k=0.20\ {\rm day^{-1}}\), \(t_{1/2}=0.693/0.20=3.47\ {\rm days}\).

---

## 48.5 Ideal batch and plug-flow reactors

An ideal batch reactor has no continuous inflow/outflow during reaction; an ideal plug-flow reactor advances material without longitudinal mixing. For first-order decay, batch and PFR residence-time relations have the same exponential form.

\[\theta=\frac{V}{Q}\quad\text{for flowing reactors}\]

![FIG-03-48-005: Batch and plug-flow reactor sketches with concentration profiles and residence-time definitions.](../figures/FIG-03-48-005-ideal-batch-and-plug-flow-reactors.png)

### Worked Example 5

**Problem.** For first-order decay, C/C0=e^{-kθ}.

**Solution.** First-order decay obeys \(dC/dt=-kC\). Integrating from \(C_0\) at \(t=0\) to \(C\) at residence time \(\theta\) gives \(\ln(C/C_0)=-k\theta\), hence **\(C/C_0=e^{-k\theta}\)** for an ideal batch reactor or PFR under this model.

---

## 48.6 Completely mixed flow reactors

A CMFR/CSTR is perfectly mixed, so reactor concentration equals effluent concentration. Mixing changes first-order performance relative to plug flow at the same residence time.

\[C=\frac{C_0}{1+k\theta}\quad\text{for first-order steady decay}\]

![FIG-03-48-006: Completely mixed reactor with influent C0, effluent C, volume V, flow Q, and internal mixing.](../figures/FIG-03-48-006-completely-mixed-flow-reactors.png)

### Worked Example 6

**Problem.** At kθ=1, a first-order CMFR has C/C0=0.5.

**Solution.** For a first-order CMFR, \(C/C_0=1/(1+k\theta)\). Setting \(k\theta=1\) gives \(C/C_0=1/(1+1)=\mathbf{0.50}\). Complete mixing therefore leaves 50% of the influent concentration at this residence-time product.

---

## 48.7 Reactor selection, residence time, and model verification

The most important reactor step is choosing the correct idealization. A correct equation used with the wrong mixing model can be more misleading than a rough calculation with the right model.

\[\text{select reactor model from mixing, flow, reaction order, and steady/unsteady assumptions}\]

![FIG-03-48-007: Decision flowchart for batch, plug-flow, and completely mixed environmental reactor models.](../figures/FIG-03-48-007-reactor-selection-residence-time-and-model-verification.png)

### Worked Example 7

**Problem.** A long narrow contact basin with limited axial mixing is often approximated more closely by plug flow than by complete mix.

**Solution.** A long, narrow basin with little longitudinal mixing better matches the **plug-flow** idealization: fluid elements advance through the basin with limited back-mixing. A completely mixed model would instead assume the effluent concentration exists throughout the entire reactor volume.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A treatment calculation predicts a negative effluent concentration. What does that indicate?

**Solution.** A negative effluent concentration violates the nonnegative concentration bound. Recheck the mass balance, reaction sign, residence time, and kinetic model; a linear removal approximation may have been extrapolated beyond the range where it is physically meaningful.

### Worked Example 9

**Problem.** A remembered environmental correlation differs from the FE Reference Handbook relation. Which should govern the exam solution?

**Solution.** For **Population, Demand, Environmental Mass Balances, and Reactor Models**, the FE Reference Handbook equation, definitions, and unit convention govern whenever the Handbook supplies the needed relation. The external references in this chapter are used for specification-required learned material involving **population projection, conservation balances, pollutant loading, and ideal-reactor models**. If a remembered correlation conflicts with the supplied Handbook equation, use the supplied Handbook relation unless the problem explicitly states a different model.

---

## As the Handbook States It

Primary source basis: **FE Environmental specification Area(s) 5; FE Reference Handbook 10.6 Environmental Engineering, printed pp. 318–360, plus general supporting sections where identified in the ledger.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required environmental-engineering knowledge that is not fully developed in the Handbook. **Guide synthesis** connects the Handbook and external material into exam-oriented explanations, examples, and checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Mihelcic, J. R., & Zimmerman, J. B. (2021). *Environmental Engineering: Fundamentals, Sustainability, Design* (3rd ed.). Wiley. ISBN 978-1-119-60445-7. Supporting scope: Environmental measurements, chemistry, physical processes, biology, risk, water quantity/quality, water treatment, wastewater/stormwater, solid waste, and air quality.
- Metcalf & Eddy/AECOM, Tchobanoglous, G., Stensel, H. D., Tsuchihashi, R., & Burton, F. L. (2014). *Wastewater Engineering: Treatment and Resource Recovery* (5th ed.). McGraw-Hill. ISBN 978-0-07-340118-8. Supporting scope: Wastewater characteristics, physical/chemical treatment, activated sludge, solids recycle, biosolids, residuals, and resource recovery.

The external references support only the learned/application portion of the Environmental specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using environmental demand projection without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental mass balance without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using pollutant loading rate without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental reaction kinetics without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using batch and plug-flow environmental reactor without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using complete-mix flow reactor without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Using environmental reactor selection without defining the environmental basis.** Confirm the control volume, constituent/media, units, time scale, and assumptions before solving.

**Confusing concentration with mass loading.** Always check whether the requested quantity is mass/volume or mass/time.

**Ignoring residual streams or transferred pollution.** Treatment often moves mass from water to sludge, air, spent media, or another phase rather than destroying it.

**Treating every required topic as a Handbook lookup.** The FE Environmental specification includes learned concepts that are not fully tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| environmental demand projection | Concept developed in §48.1; apply with that section's stated environmental basis and assumptions. |
| environmental mass balance | Concept developed in §48.2; apply with that section's stated environmental basis and assumptions. |
| pollutant loading rate | Concept developed in §48.3; apply with that section's stated environmental basis and assumptions. |
| environmental reaction kinetics | Concept developed in §48.4; apply with that section's stated environmental basis and assumptions. |
| batch and plug-flow environmental reactor | Concept developed in §48.5; apply with that section's stated environmental basis and assumptions. |
| complete-mix flow reactor | Concept developed in §48.6; apply with that section's stated environmental basis and assumptions. |
| environmental reactor selection | Concept developed in §48.7; apply with that section's stated environmental basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **environmental demand projection** and identify the governing balance, equilibrium relation, transport model, or design concept.

2. Define **environmental mass balance** and identify the governing balance, equilibrium relation, transport model, or design concept.

3. Define **pollutant loading rate** and identify the governing balance, equilibrium relation, transport model, or design concept.

4. Define **environmental reaction kinetics** and identify the governing balance, equilibrium relation, transport model, or design concept.

5. Define **batch and plug-flow environmental reactor** and identify the governing balance, equilibrium relation, transport model, or design concept.

6. Define **complete-mix flow reactor** and identify the governing balance, equilibrium relation, transport model, or design concept.

7. Define **environmental reactor selection** and identify the governing balance, equilibrium relation, transport model, or design concept.

8. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental demand projection**?

9. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental mass balance**?

10. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **pollutant loading rate**?

11. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental reaction kinetics**?

12. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **batch and plug-flow environmental reactor**?

13. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **complete-mix flow reactor**?

14. What assumption, unit conversion, boundary condition, or process limitation must be checked before applying **environmental reactor selection**?

15. Why should an environmental problem begin with a clearly defined system boundary or conceptual model?

16. Why must concentration and mass loading be kept distinct?

17. When should a Handbook relation be used instead of a remembered correlation?

18. Why is a physical or mass-balance reasonableness check necessary after calculation?

### Multiple Choice

19. Which statement is most accurate for **environmental demand projection**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

20. Which statement is most accurate for **environmental mass balance**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

21. Which statement is most accurate for **pollutant loading rate**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

22. Which statement is most accurate for **environmental reaction kinetics**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

23. Which statement is most accurate for **batch and plug-flow environmental reactor**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

24. Which statement is most accurate for **complete-mix flow reactor**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

25. Which statement is most accurate for **environmental reactor selection**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

26. Which statement is most accurate for **environmental demand projection**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation

27. Which statement is most accurate for **environmental mass balance**?
A) It must be applied with consistent units, boundaries, and process assumptions
B) It is independent of time scale and system definition
C) It replaces conservation of mass or energy
D) It is always a Handbook lookup with no learned interpretation


---

## Answer Key with Explanations

1. **environmental demand projection** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

2. **environmental mass balance** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

3. **pollutant loading rate** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

4. **environmental reaction kinetics** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

5. **batch and plug-flow environmental reactor** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

6. **complete-mix flow reactor** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

7. **environmental reactor selection** is developed in its numbered section. Use the displayed balance, equilibrium, kinetic, transport, or decision relation with the stated assumptions.

8. For **environmental demand projection**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

9. For **environmental mass balance**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

10. For **pollutant loading rate**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

11. For **environmental reaction kinetics**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

12. For **batch and plug-flow environmental reactor**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

13. For **complete-mix flow reactor**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

14. For **environmental reactor selection**, check basis, units, steady/unsteady condition, phase/media, boundary conditions, and whether the selected idealization matches the system.

15. In **Population, Demand, Environmental Mass Balances, and Reactor Models**, the control volume or conceptual boundary determines which sources, sinks, transfers, reactions, and receptors belong in the model. For this chapter specifically, confirm population and flow bases, conservation of mass, nonnegative concentrations, and whether batch, plug-flow, or complete-mix assumptions match the physical reactor.

16. Concentration and loading answer different questions in **Population, Demand, Environmental Mass Balances, and Reactor Models**: concentration is mass per volume, while loading is mass per time. Always convert \(Q\) and \(C\) to compatible units before multiplying them.

17. Use the FE Reference Handbook equation and definitions when it supplies the model for **Population, Demand, Environmental Mass Balances, and Reactor Models**. The chapter's external references (MIHELCIC, METCALF) support learned specification content, not a competing exam formula.

18. A physical check is needed because algebra alone can return impossible environmental states. For this chapter, set reaction rate to zero and verify the reactor balance reduces to pure flow-through conservation; also confirm \(k	heta	o0\) gives \(C/C_0	o1\).

19. **A.** Section §48.1, **Population projections and demand forecasting**, is governed by \(P_t=P_0(1+r)^t,\qquad D=P_t\,d_{pc}\). Use that relation with its own environmental basis and then perform the specific validity check described for §48.1.

20. **A.** Section §48.2, **Control volumes, steady and unsteady environmental mass balances**, is governed by \(\frac{dM}{dt}=\sum \dot M_{in}-\sum \dot M_{out}+rV\). Use that relation with its own environmental basis and then perform the specific validity check described for §48.2.

21. **A.** Section §48.3, **Concentration-flow loading calculations**, is governed by \(\dot m=QC\). Use that relation with its own environmental basis and then perform the specific validity check described for §48.3.

22. **A.** Section §48.4, **Reaction order and environmental decay kinetics**, is governed by \(r=-kC^n\). Use that relation with its own environmental basis and then perform the specific validity check described for §48.4.

23. **A.** Section §48.5, **Ideal batch and plug-flow reactors**, is governed by \(\theta=\frac{V}{Q}\quad\text{for flowing reactors}\). Use that relation with its own environmental basis and then perform the specific validity check described for §48.5.

24. **A.** Section §48.6, **Completely mixed flow reactors**, is governed by \(C=\frac{C_0}{1+k\theta}\quad\text{for first-order steady decay}\). Use that relation with its own environmental basis and then perform the specific validity check described for §48.6.

25. **A.** Section §48.7, **Reactor selection, residence time, and model verification**, is governed by \(\text{select reactor model from mixing, flow, reaction order, and steady/unsteady assumptions}\). Use that relation with its own environmental basis and then perform the specific validity check described for §48.7.

26. **A.** An integrated **Population, Demand, Environmental Mass Balances, and Reactor Models** solution is acceptable only after the governing balance/model is identified, units are reconciled, and the chapter-specific physical checks are satisfied.

27. **A.** Source ownership is explicit in **Population, Demand, Environmental Mass Balances, and Reactor Models**: FE-Handbook-supported material remains tied to the ledger, externally supported content uses MIHELCIC, METCALF, and guide synthesis is labeled as supplemental explanation.


---

## Practice Problems

1. A population of 50,000 growing at 1.5%/yr for 20 years becomes about 67,300 under geometric growth.

2. At steady state with no reaction, 100 mg/s entering requires 100 mg/s leaving.

3. 2 MGD at 15 mg/L corresponds to about 250 lb/day.

4. For first-order decay with k=0.20 day^-1, half-life is ln2/k≈3.47 days.

5. For first-order decay, C/C0=e^{-kθ}.

6. At kθ=1, a first-order CMFR has C/C0=0.5.

7. A long narrow contact basin with limited axial mixing is often approximated more closely by plug flow than by complete mix.

8. Identify one mass-balance, unit, or boundary-condition check that should be completed before accepting the result.

9. Identify the FE Environmental specification area and Handbook section most relevant to this chapter.

10. Give one limiting-case or physical-reasonableness check appropriate to this chapter.


---

## Practice Problem Solutions

1. **Independent recomputation for §48.1 — Population projections and demand forecasting.** Start from the stated givens rather than the worked-example answer. Use geometric growth: \(P_{20}=50{,}000(1+0.015)^{20}=67{,}342\), so the projected population is about **67,300 people**. A design-demand calculation would then multiply this population by the specified per-capita demand. As a separate check, confirm the result is consistent with the section's physical interpretation.

2. **Independent recomputation for §48.2 — Control volumes, steady and unsteady environmental mass balances.** Start from the stated givens rather than the worked-example answer. At steady state, \(dM/dt=0\). With no reaction, \(rV=0\), so the mass balance reduces to \(\sum \dot M_{in}=\sum \dot M_{out}\). Therefore an inflow of **100 mg/s** requires an outflow of **100 mg/s**. As a separate check, confirm the result is consistent with the section's physical interpretation.

3. **Independent recomputation for §48.3 — Concentration-flow loading calculations.** Start from the stated givens rather than the worked-example answer. For wastewater units, \(\dot m=8.34QC\) with \(Q\) in MGD and \(C\) in mg/L. Thus \(\dot m=8.34(2)(15)=250.2\ {\rm lb/day}\), or about **250 lb/day**. As a separate check, confirm the result is consistent with the section's physical interpretation.

4. **Independent recomputation for §48.4 — Reaction order and environmental decay kinetics.** Start from the stated givens rather than the worked-example answer. For first-order decay, \(t_{1/2}=\ln 2/k\). With \(k=0.20\ {\rm day^{-1}}\), \(t_{1/2}=0.693/0.20=3.47\ {\rm days}\). As a separate check, confirm the result is consistent with the section's physical interpretation.

5. **Independent recomputation for §48.5 — Ideal batch and plug-flow reactors.** Start from the stated givens rather than the worked-example answer. First-order decay obeys \(dC/dt=-kC\). Integrating from \(C_0\) at \(t=0\) to \(C\) at residence time \(\theta\) gives \(\ln(C/C_0)=-k\theta\), hence **\(C/C_0=e^{-k\theta}\)** for an ideal batch reactor or PFR under this model. As a separate check, confirm the result is consistent with the section's physical interpretation.

6. **Independent recomputation for §48.6 — Completely mixed flow reactors.** Start from the stated givens rather than the worked-example answer. For a first-order CMFR, \(C/C_0=1/(1+k\theta)\). Setting \(k\theta=1\) gives \(C/C_0=1/(1+1)=\mathbf{0.50}\). Complete mixing therefore leaves 50% of the influent concentration at this residence-time product. As a separate check, confirm the result is consistent with the section's physical interpretation.

7. **Independent recomputation for §48.7 — Reactor selection, residence time, and model verification.** Start from the stated givens rather than the worked-example answer. A long, narrow basin with little longitudinal mixing better matches the **plug-flow** idealization: fluid elements advance through the basin with limited back-mixing. A completely mixed model would instead assume the effluent concentration exists throughout the entire reactor volume. As a separate check, confirm the result is consistent with the section's physical interpretation.

8. For this chapter, check the result against this failure screen: Confirm population and flow bases, conservation of mass, nonnegative concentrations, and whether batch, plug-flow, or complete-mix assumptions match the physical reactor. A result that violates one of those conditions should be rejected even if the arithmetic is internally consistent.

9. For **Population, Demand, Environmental Mass Balances, and Reactor Models**, begin with the FE Environmental specification area and Handbook subsection recorded in the ledger. When the atom is `split_required`, use the reconciled external source set **MIHELCIC, METCALF** for the learned portion rather than inventing a Handbook page.

10. A useful limiting case is to set reaction rate to zero and verify the reactor balance reduces to pure flow-through conservation; also confirm \(k	heta	o0\) gives \(C/C_0	o1\). The simplified case should reduce to the stated physical behavior before the full model is trusted.

---

## Quick Reference

**Source anchor:** FE Environmental specification Area(s) 5.

- **environmental demand projection:** Population projections and demand forecasting
- **environmental mass balance:** Control volumes, steady and unsteady environmental mass balances
- **pollutant loading rate:** Concentration-flow loading calculations
- **environmental reaction kinetics:** Reaction order and environmental decay kinetics
- **batch and plug-flow environmental reactor:** Ideal batch and plug-flow reactors
- **complete-mix flow reactor:** Completely mixed flow reactors
- **environmental reactor selection:** Reactor selection, residence time, and model verification

---

## What's Next

**Chapter 03-49: Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH**

Carry forward the same FE workflow: define the environmental system and constituent, establish units and time basis, choose the Handbook relation or learned model, solve, then close the mass/energy and physical-reasonableness checks.

— Your Mentor
