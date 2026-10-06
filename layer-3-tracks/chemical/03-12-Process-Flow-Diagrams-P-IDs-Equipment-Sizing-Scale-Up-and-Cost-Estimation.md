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

## 12.2 Piping and Instrumentation Diagrams

**Specification-required; not directly tabulated in the Chemical Engineering Handbook pages.** A P&ID adds piping, valves, instruments, control loops, equipment tags, and interlocks needed to describe process control and safeguarding.

A P&ID contains much more implementation detail than a PFD but still does not replace fabrication drawings or control-system logic documentation.

\[\text{P&ID: equipment + piping + valves + instruments + control/safety loops}\]

![FIG-03-12-002: Simplified vessel control P&ID with level transmitter/controller, control valve, pressure relief, isolation valves, and equipment tags.](../figures/FIG-03-12-002-piping-and-instrumentation-diagrams.png)

### Worked Example 2

**Problem.** What drawing adds control valves and instrument loops?

**Solution.** P&ID.

---

## 12.3 Equipment Selection and First-Pass Sizing

**Specification-required; guide-developed workflow.** First-pass equipment selection starts with duty: flow, phase, temperature, pressure, heat load, separation target, or reaction volume.

Sizing then applies the governing balance or rate relation—for example \(Q=UA\Delta T_{lm}\), \(V=F_{A0}\int dX/(-r_A)\), or \(Q=Av\)—using design margins only when stated.

\[\text{required duty}\rightarrow\text{governing equation}\rightarrow\text{size}\rightarrow\text{check constraints}\]

![FIG-03-12-003: Decision path from process duty to pump, exchanger, vessel, reactor, or separator size and design constraints.](../figures/FIG-03-12-003-equipment-selection-and-first-pass-sizing.png)

### Worked Example 3

**Problem.** A heat exchanger duty is 500 kW, U=1 kW/(m²·K), corrected ΔTlm=25 K. Find area.

**Solution.** A=500/(1×25)=20 m².

---

## 12.4 Scale-Up and Similarity

**Specification-required; only partly supported by Handbook cost scaling.** Geometric scale-up does not guarantee equal heat transfer, mixing, pressure drop, or reaction performance. Identify the physical similarity criterion that must be preserved.

Depending on the equipment, relevant groups may include Reynolds, Froude, power number, residence time, or heat/mass-transfer correlations supplied by the problem.

\[\text{scale-up requires preserving the controlling dimensionless or rate criterion}\]

![FIG-03-12-004: Lab, pilot, and plant vessels with geometric scale ratio and competing Reynolds/Froude/heat-transfer constraints.](../figures/FIG-03-12-004-scale-up-and-similarity.png)

### Worked Example 4

**Problem.** Why is geometric scale-up alone insufficient for mixing equipment?

**Solution.** Hydrodynamic similarity such as Reynolds/Froude/power number may change.

---

## 12.5 Cost Indexes

The Handbook provides the cost-index relation for updating a historical equipment cost to a new year.

Both costs must refer to comparable scope; a purchase-cost index should not be used to convert directly to total installed plant cost without an installation model.

\[C_{\rm current}=C_{\rm old}\frac{I_{\rm current}}{I_{\rm old}}\]

![FIG-03-12-005: Historical equipment cost updated by ratio of current and historical cost indices.](../figures/FIG-03-12-005-cost-indexes.png)

### Worked Example 5

**Problem.** Old equipment cost is $200,000 at index 500; new index is 650. Find updated cost.

**Solution.** $260,000.

---

## 12.6 Capacity Scaling and Lang Factors

The Handbook uses a power law to scale the cost of similar equipment between capacities and tabulates representative exponents. It also provides Lang factors for estimating fixed and total capital investment from purchased-equipment cost.

These are screening-level methods, not detailed bid estimates.

\[\frac{C_2}{C_1}=\left(\frac{S_2}{S_1}\right)^n\]

![FIG-03-12-006: Log-log equipment cost versus capacity with exponent n and Lang-factor step from purchased cost to capital investment.](../figures/FIG-03-12-006-capacity-scaling-and-lang-factors.png)

### Worked Example 6

**Problem.** A similar unit doubles capacity with n=0.6. Find cost ratio.

**Solution.** 2^0.6=1.516.

---

## 12.7 Estimate Classes, Uncertainty, and Economic Screening

The Handbook classifies estimates from early screening/feasibility through more detailed bid/check estimates, with increasing project definition and preparation effort.

Match economic precision to design maturity. A Class 5 screening estimate should not be presented with the apparent precision of a detailed deterministic estimate.

\[\text{greater project definition}\Rightarrow\text{narrower expected estimate range and greater preparation effort}\]

![FIG-03-12-007: Estimate classes 5 through 1 plotted against project definition, expected accuracy range, and preparation effort.](../figures/FIG-03-12-007-estimate-classes-uncertainty-and-economic-screening.png)

### Worked Example 7

**Problem.** Which estimate class has the least project definition in the Handbook table?

**Solution.** Class 5.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Purchased-equipment cost is $1.0M and a screening Lang factor is 5.0. Estimate fixed capital.

**Solution.** $5.0M.

### Worked Example 9

**Problem.** If project definition increases, what generally happens to expected estimate range?

**Solution.** It narrows while preparation effort rises.

---

## As the Handbook States It

Primary source basis: **FE Chemical specification Area 14A–E; Chemical Engineering cost-estimation tables, printed pp. 262–264; general Engineering Economics, printed pp. 235–242**.

**Source boundary:** The specification explicitly requires PFDs, P&IDs, equipment selection, sizing/scale-up, cost estimation, optimization, sustainability, and design standards. Handbook pp. 262–264 directly support cost indices, Lang factors, cost-capacity scaling, and estimate classes; PFD/P&ID conventions and most sizing/scale-up workflow are not directly tabulated and are guide-developed.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

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

8. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

9. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

10. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

11. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

12. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

13. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

14. The calculation can use inconsistent flow/composition bases, omit an internal/external stream, or apply the wrong equilibrium/rate model. Define the process basis and boundary first.

15. The material balance determines the amounts and compositions needed for enthalpy and reaction-energy calculations.

16. To verify that the unknowns are matched by independent equations/specifications before algebra begins.

17. Whenever the problem provides the model/data; use that stated relation rather than substituting an unstated correlation.

18. The Handbook intentionally omits some theories and formulas; exam specifications can require knowledge not directly tabulated in it.

19. **A.** The relation or workflow for **process flow diagram** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

20. **A.** The relation or workflow for **piping and instrumentation diagram** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

21. **A.** The relation or workflow for **equipment first-pass sizing** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

22. **A.** The relation or workflow for **process equipment scale-up** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

23. **A.** The relation or workflow for **chemical cost index** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

24. **A.** The relation or workflow for **equipment cost-capacity scaling** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

25. **A.** The relation or workflow for **chemical cost estimate class** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

26. **A.** The relation or workflow for **process flow diagram** depends on the process basis, boundary, phase/equilibrium model, and assumptions.

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

3. A=500/(1×25)=20 m².

4. Hydrodynamic similarity such as Reynolds/Froude/power number may change.

5. $260,000.

6. 2^0.6=1.516.

7. Class 5.

8. $5.0M.

9. It narrows while preparation effort rises.

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