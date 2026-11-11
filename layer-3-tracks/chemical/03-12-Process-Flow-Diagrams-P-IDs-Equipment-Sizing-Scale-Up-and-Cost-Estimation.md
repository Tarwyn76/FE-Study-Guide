---
chapter: "03-12"
title: "Process Flow Diagrams, P&IDs, Equipment Sizing, Scale-Up, and Cost Estimation"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-012-01, CHE-3-012-02, CHE-3-012-03, CHE-3-012-04, CHE-3-012-05, CHE-3-012-06, CHE-3-012-07]
routes: [chemical]
status: drafted
---

# Chapter 03-12: Process Flow Diagrams, P&IDs, Equipment Sizing, Scale-Up, and Cost Estimation

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 03-01 Process Flowsheets · 02-10 Economic Decision-Making · 02-66 Measurement Systems

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The specification explicitly requires PFDs, P&IDs, equipment selection, sizing/scale-up, cost estimation, optimization, sustainability, and design standards. Handbook pp. 262–264 directly support cost indices, Lang factors, cost-capacity scaling, and estimate classes; PFD/P&ID conventions and most sizing/scale-up workflow are not directly tabulated and are guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **12.1** Explain and apply **Process Flow Diagrams**.
* **12.2** Explain and apply **Piping and Instrumentation Diagrams**.
* **12.3** Explain and apply **Equipment Selection and First-Pass Sizing**.
* **12.4** Explain and apply **Scale-Up and Similarity**.
* **12.5** Explain and apply **Cost Indexes**.
* **12.6** Explain and apply **Capacity Scaling and Lang Factors**.
* **12.7** Explain and apply **Estimate Classes, Uncertainty, and Economic Screening**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 12.1 Process Flow Diagrams

**Specification-required; not directly tabulated in the Chemical Engineering Handbook pages.** A PFD shows major process equipment, principal process streams, stream numbering, key operating conditions, and major utilities.

A PFD is intended for process understanding and balance calculations, not detailed construction or instrument wiring.

\[\text{PFD: major equipment + numbered process streams + principal conditions}\]

![FIG-03-12-001: Chemical-process PFD with feed, pump, heat exchanger, reactor, separator, recycle, stream numbers, and key T/P/flow annotations.](../figures/FIG-03-12-001-process-flow-diagrams.png)

### Worked Example 1

**Problem.** What belongs on a PFD but not necessarily detailed valve-by-valve piping?

**Solution.** Major equipment, principal streams, key conditions and flows.

---

**Why this works.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. In this example, the stated setup (“Problem. What belongs on a PFD but not necessarily detailed valve-by-valve piping? Solution. Major equipment, principal streams, key conditions and flows”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## 12.2 Piping and Instrumentation Diagrams

**Specification-required; not directly tabulated in the Chemical Engineering Handbook pages.** A P&ID adds piping, valves, instruments, control loops, equipment tags, and interlocks needed to describe process control and safeguarding.

A P&ID contains much more implementation detail than a PFD but still does not replace fabrication drawings or control-system logic documentation.

\[\text{P&ID: equipment + piping + valves + instruments + control/safety loops}\]

![FIG-03-12-002: Simplified vessel control P&ID with level transmitter/controller, control valve, pressure relief, isolation valves, and equipment tags.](../figures/FIG-03-12-002-piping-and-instrumentation-diagrams.png)

### Worked Example 2

**Problem.** What drawing adds control valves and instrument loops?

**Solution.** P&ID.

---

**Why this works.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. In this example, the stated setup (“Problem. What drawing adds control valves and instrument loops? Solution. P&ID”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## 12.3 Equipment Selection and First-Pass Sizing

**Specification-required; guide-developed workflow.** First-pass equipment selection starts with duty: flow, phase, temperature, pressure, heat load, separation target, or reaction volume.

Sizing then applies the governing balance or rate relation—for example \(Q=UA\Delta T_{lm}\), \(V=F_{A0}\int dX/(-r_A)\), or \(Q=Av\)—using design margins only when stated.

\[\text{required duty}\rightarrow\text{governing equation}\rightarrow\text{size}\rightarrow\text{check constraints}\]

![FIG-03-12-003: Decision path from process duty to pump, exchanger, vessel, reactor, or separator size and design constraints.](../figures/FIG-03-12-003-equipment-selection-and-first-pass-sizing.png)

### Worked Example 3

**Problem.** A heat exchanger duty is 500 kW, U=1 kW/(m²·K), corrected ΔTlm=25 K. Find area.

**Solution.** A=500/(1×25)=20 m².

---

<!-- VERIFY id="WE-03-12-003-area" expr="500/(1*25)" expected="20" units="m2" atol="1e-9" rtol="1e-9" -->

## 12.4 Scale-Up and Similarity

**Specification-required; only partly supported by Handbook cost scaling.** Geometric scale-up does not guarantee equal heat transfer, mixing, pressure drop, or reaction performance. Identify the physical similarity criterion that must be preserved.

Depending on the equipment, relevant groups may include Reynolds, Froude, power number, residence time, or heat/mass-transfer correlations supplied by the problem.

\[\text{scale-up requires preserving the controlling dimensionless or rate criterion}\]

![FIG-03-12-004: Lab, pilot, and plant vessels with geometric scale ratio and competing Reynolds/Froude/heat-transfer constraints.](../figures/FIG-03-12-004-scale-up-and-similarity.png)

### Worked Example 4

**Problem.** Why is geometric scale-up alone insufficient for mixing equipment?

**Solution.** Hydrodynamic similarity such as Reynolds/Froude/power number may change.

---

**Why this works.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. In this example, the stated setup (“Problem. Why is geometric scale-up alone insufficient for mixing equipment? Solution. Hydrodynamic similarity such as Reynolds/Froude/power number may chan”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## 12.5 Cost Indexes

The Handbook provides the cost-index relation for updating a historical equipment cost to a new year.

Both costs must refer to comparable scope; a purchase-cost index should not be used to convert directly to total installed plant cost without an installation model.

\[C_{\rm current}=C_{\rm old}\frac{I_{\rm current}}{I_{\rm old}}\]

![FIG-03-12-005: Historical equipment cost updated by ratio of current and historical cost indices.](../figures/FIG-03-12-005-cost-indexes.png)

### Worked Example 5

**Problem.** Old equipment cost is $200,000 at index 500; new index is 650. Find updated cost.

**Solution.** $260,000.

---

<!-- VERIFY id="WE-03-12-005-cost" expr="200000*650/500" expected="260000" units="USD" atol="0.5" rtol="1e-9" -->

## 12.6 Capacity Scaling and Lang Factors

The Handbook uses a power law to scale the cost of similar equipment between capacities and tabulates representative exponents. It also provides Lang factors for estimating fixed and total capital investment from purchased-equipment cost.

These are screening-level methods, not detailed bid estimates.

\[\frac{C_2}{C_1}=\left(\frac{S_2}{S_1}\right)^n\]

![FIG-03-12-006: Log-log equipment cost versus capacity with exponent n and Lang-factor step from purchased cost to capital investment.](../figures/FIG-03-12-006-capacity-scaling-and-lang-factors.png)

### Worked Example 6

**Problem.** A similar unit doubles capacity with n=0.6. Find cost ratio.

**Solution.** 2^0.6=1.516.

---

<!-- VERIFY id="WE-03-12-006-ratio" expr="2**0.6" expected="1.516" units="dimensionless" atol="0.0005" rtol="1e-9" -->

## 12.7 Estimate Classes, Uncertainty, and Economic Screening

The Handbook classifies estimates from early screening/feasibility through more detailed bid/check estimates, with increasing project definition and preparation effort.

Match economic precision to design maturity. A Class 5 screening estimate should not be presented with the apparent precision of a detailed deterministic estimate.

\[\text{greater project definition}\Rightarrow\text{narrower expected estimate range and greater preparation effort}\]

![FIG-03-12-007: Estimate classes 5 through 1 plotted against project definition, expected accuracy range, and preparation effort.](../figures/FIG-03-12-007-estimate-classes-uncertainty-and-economic-screening.png)

### Worked Example 7

**Problem.** Which estimate class has the least project definition in the Handbook table?

**Solution.** Class 5.

---

**Why this works.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. In this example, the stated setup (“Problem. Which estimate class has the least project definition in the Handbook table? Solution. Class 5”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## Integrated Worked Examples

### Worked Example 8

**Problem.** Purchased-equipment cost is $1.0M and a screening Lang factor is 5.0. Estimate fixed capital.

**Solution.** $5.0M.

<!-- VERIFY id="WE-03-12-008-capital" expr="1000000*5" expected="5000000" units="USD" atol="0.5" rtol="1e-9" -->

**Why this works.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. In this example, the stated setup (“Problem. Purchased-equipment cost is 1.0M and a screening Lang factor is 5.0. Estimate fixed capital. Solution. 5.0M”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
### Worked Example 9

**Problem.** If project definition increases, what generally happens to expected estimate range?

**Solution.** It narrows while preparation effort rises.

---

**Why this works.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. In this example, the stated setup (“Problem. If project definition increases, what generally happens to expected estimate range? Solution. It narrows while preparation effort rises”) fixes the applicable data and assumptions. Checking the final value against those assumptions and its units confirms that the result is physically and mathematically consistent.
## As the Handbook States It

Primary source basis: **FE Chemical specification Area 14A–E; Chemical Engineering cost-estimation tables, printed pp. 262–264; general Engineering Economics, printed pp. 235–242**.

**Source boundary:** The specification explicitly requires PFDs, P&IDs, equipment selection, sizing/scale-up, cost estimation, optimization, sustainability, and design standards. Handbook pp. 262–264 directly support cost indices, Lang factors, cost-capacity scaling, and estimate classes; PFD/P&ID conventions and most sizing/scale-up workflow are not directly tabulated and are guide-developed.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---



### Source Boundary

- **FE-Handbook-supported** — Equations, definitions, tables, and relations explicitly identified in this Handbook section are supported by the cited FE Reference Handbook location recorded for the chapter/concept.
- **Externally supported** — Material extending beyond the Handbook is supported by the external-source provenance recorded in the concept ledger and the Chemical Track References and Sources register.
- **Guide synthesis** — Explanatory sequencing, worked-example framing, exam-navigation advice, and connections among separately sourced concepts are guide-developed synthesis unless separately attributed.

## Where This Goes Wrong

**Using process flow diagram without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using piping and instrumentation diagram without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using equipment first-pass sizing without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using process equipment scale-up without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using chemical cost index without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using equipment cost-capacity scaling without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using chemical cost estimate class without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| process flow diagram | Concept developed in §12.1; apply with the section's stated basis and assumptions. |
| piping and instrumentation diagram | Concept developed in §12.2; apply with the section's stated basis and assumptions. |
| equipment first-pass sizing | Concept developed in §12.3; apply with the section's stated basis and assumptions. |
| process equipment scale-up | Concept developed in §12.4; apply with the section's stated basis and assumptions. |
| chemical cost index | Concept developed in §12.5; apply with the section's stated basis and assumptions. |
| equipment cost-capacity scaling | Concept developed in §12.6; apply with the section's stated basis and assumptions. |
| chemical cost estimate class | Concept developed in §12.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **process flow diagram** and state the governing relation or balance.

2. Define **piping and instrumentation diagram** and state the governing relation or balance.

3. Define **equipment first-pass sizing** and state the governing relation or balance.

4. Define **process equipment scale-up** and state the governing relation or balance.

5. Define **chemical cost index** and state the governing relation or balance.

6. Define **equipment cost-capacity scaling** and state the governing relation or balance.

7. Define **chemical cost estimate class** and state the governing relation or balance.

8. What is the most likely error if **process flow diagram** is applied before the process basis and boundary are defined?

9. What is the most likely error if **piping and instrumentation diagram** is applied before the process basis and boundary are defined?

10. What is the most likely error if **equipment first-pass sizing** is applied before the process basis and boundary are defined?

11. What is the most likely error if **process equipment scale-up** is applied before the process basis and boundary are defined?

12. What is the most likely error if **chemical cost index** is applied before the process basis and boundary are defined?

13. What is the most likely error if **equipment cost-capacity scaling** is applied before the process basis and boundary are defined?

14. What is the most likely error if **chemical cost estimate class** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **process flow diagram**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **piping and instrumentation diagram**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **equipment first-pass sizing**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **process equipment scale-up**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **chemical cost index**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **equipment cost-capacity scaling**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **chemical cost estimate class**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **process flow diagram**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **piping and instrumentation diagram**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **process flow diagram** is developed in §12.1. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

2. **piping and instrumentation diagram** is developed in §12.2. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

3. **equipment first-pass sizing** is developed in §12.3. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

4. **process equipment scale-up** is developed in §12.4. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

5. **chemical cost index** is developed in §12.5. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

6. **equipment cost-capacity scaling** is developed in §12.6. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.

7. **chemical cost estimate class** is developed in §12.7. Apply the displayed relation only with the section's basis, phase, equilibrium, and steady/unsteady assumptions.
8. Applying **process flow diagram** before the process basis and system boundary are fixed can size equipment from the wrong duty or flow basis, or compare costs that use inconsistent scale, year, or capacity assumptions. In this chapter, process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis. Define the basis, boundary, known streams or states, and independent specifications first; then apply the process flow diagram relation to that defined system.

9. Applying **piping and instrumentation diagram** before the process basis and system boundary are fixed can size equipment from the wrong duty or flow basis, or compare costs that use inconsistent scale, year, or capacity assumptions. In this chapter, process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis. Define the basis, boundary, known streams or states, and independent specifications first; then apply the piping and instrumentation diagram relation to that defined system.

10. Applying **equipment first-pass sizing** before the process basis and system boundary are fixed can size equipment from the wrong duty or flow basis, or compare costs that use inconsistent scale, year, or capacity assumptions. In this chapter, process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis. Define the basis, boundary, known streams or states, and independent specifications first; then apply the equipment first-pass sizing relation to that defined system.

11. Applying **process equipment scale-up** before the process basis and system boundary are fixed can size equipment from the wrong duty or flow basis, or compare costs that use inconsistent scale, year, or capacity assumptions. In this chapter, process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis. Define the basis, boundary, known streams or states, and independent specifications first; then apply the process equipment scale-up relation to that defined system.

12. Applying **chemical cost index** before the process basis and system boundary are fixed can size equipment from the wrong duty or flow basis, or compare costs that use inconsistent scale, year, or capacity assumptions. In this chapter, process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis. Define the basis, boundary, known streams or states, and independent specifications first; then apply the chemical cost index relation to that defined system.

13. Applying **equipment cost-capacity scaling** before the process basis and system boundary are fixed can size equipment from the wrong duty or flow basis, or compare costs that use inconsistent scale, year, or capacity assumptions. In this chapter, process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis. Define the basis, boundary, known streams or states, and independent specifications first; then apply the equipment cost-capacity scaling relation to that defined system.

14. Applying **chemical cost estimate class** before the process basis and system boundary are fixed can size equipment from the wrong duty or flow basis, or compare costs that use inconsistent scale, year, or capacity assumptions. In this chapter, process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis. Define the basis, boundary, known streams or states, and independent specifications first; then apply the chemical cost estimate class relation to that defined system.

15. Close the material balance first because it establishes the flow rates and compositions that the energy balance must use. For this chapter, process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis; without those material quantities, enthalpy, heat duty, reaction energy, or phase-change terms can be attached to the wrong amount of material.

16. A degrees-of-freedom check compares the number of unknowns with the number of independent balances, constitutive relations, equilibrium or rate equations, and specifications. For 03-12, this prevents algebra from starting before the process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis are sufficiently defined and exposes redundant or missing equations.

17. Use a relation supplied in the FE problem whenever it defines the model or data for that question. That stated relation controls the calculation even if another correlation is familiar; in 03-12, substituting an unstated model can change the assumptions behind the process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis.

18. Separate Handbook-supported material from specification-required or externally supported material so the learner knows what may be looked up and what must be understood independently. In 03-12, the distinction matters because the process design links flowsheet and P&ID information to equipment duty, sizing, scale-up assumptions, and a defined cost basis can include methods or assumptions that are required by the exam specification but are not fully tabulated in the Handbook.


19. **A.** The relation or workflow for **process flow diagram** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **piping and instrumentation diagram** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **equipment first-pass sizing** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **process equipment scale-up** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **chemical cost index** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **equipment cost-capacity scaling** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **chemical cost estimate class** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **process flow diagram** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

   **Item-specific check.** The prompt here asks “Which statement is most accurate for process flow diagram? A) It must be applied with the correct process basis and physical assumptions B) It is independent of composition and pha.” This explanation applies to that specific condition; verify the result against the variables, assumptions, and units given in this item.

27. **A.** The relation or workflow for **piping and instrumentation diagram** depends on the process basis, boundary, phase/equilibrium model, and assumptions.


---

## Practice Problems

1. What belongs on a PFD but not necessarily detailed valve-by-valve piping?

2. What drawing adds control valves and instrument loops?

3. A heat exchanger duty is 500 kW, U=1 kW/(m²·K), corrected ΔTlm=25 K. Find area.

4. Why is geometric scale-up alone insufficient for mixing equipment?

5. Old equipment cost is $200,000 at index 500; new index is 650. Find updated cost.

6. A similar unit doubles capacity with n=0.6. Find cost ratio.

7. Which estimate class has the least project definition in the Handbook table?

8. Purchased-equipment cost is $1.0M and a screening Lang factor is 5.0. Estimate fixed capital.

9. If project definition increases, what generally happens to expected estimate range?

10. Why should a screening estimate not be reported to excessive significant digits?


---

## Practice Problem Solutions

1. Major equipment, principal streams, key conditions and flows.

2. P&ID.

   **Explanation.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. The question is framed around “What drawing adds control valves and instrument loops?.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

3. A=500/(1×25)=20 m².

   **Explanation.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. The question is framed around “A heat exchanger duty is 500 kW, U=1 kW/(m²·K), corrected ΔTlm=25 K. Find area.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

4. Hydrodynamic similarity such as Reynolds/Froude/power number may change.

5. $260,000.

   **Explanation.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. The question is framed around “Old equipment cost is 200,000 at index 500; new index is 650. Find updated cost.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

6. 2^0.6=1.516.

   **Explanation.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. The question is framed around “A similar unit doubles capacity with n=0.6. Find cost ratio.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

7. Class 5.

   **Explanation.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. The question is framed around “Which estimate class has the least project definition in the Handbook table?.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

8. $5.0M.

   **Explanation.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. The question is framed around “Purchased-equipment cost is 1.0M and a screening Lang factor is 5.0. Estimate fixed capital.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

9. It narrows while preparation effort rises.

   **Explanation.** Trace the result from the flowsheet or P&ID assumptions through equipment duty, sizing or scale-up relation, and the stated cost basis. The question is framed around “If project definition increases, what generally happens to expected estimate range?.” This check ties the stated answer to the governing model and the problem data, and it provides a basis for verifying sign, units, or logical consistency.

10. The method's uncertainty is much larger than those digits imply.


---

## Quick Reference

**Source anchor:** FE Chemical specification Area 14A–E; Chemical Engineering cost-estimation tables, printed pp. 262–264; general Engineering Economics, printed pp. 235–242.

- **process flow diagram:** Process Flow Diagrams
- **piping and instrumentation diagram:** Piping and Instrumentation Diagrams
- **equipment first-pass sizing:** Equipment Selection and First-Pass Sizing
- **process equipment scale-up:** Scale-Up and Similarity
- **chemical cost index:** Cost Indexes
- **equipment cost-capacity scaling:** Capacity Scaling and Lang Factors
- **chemical cost estimate class:** Estimate Classes, Uncertainty, and Economic Screening
---

## What's Next

**03-13 — Process Optimization, Advanced Control, and Process Safety**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor