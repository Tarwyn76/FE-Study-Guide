---
chapter: "03-02"
title: "Recycle, Bypass, Purge, and Unsteady Material Balances"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-002-01, CHE-3-002-02, CHE-3-002-03, CHE-3-002-04, CHE-3-002-05, CHE-3-002-06, CHE-3-002-07]
routes: [chemical]
status: drafted
---

# Chapter 03-02: Recycle, Bypass, Purge, and Unsteady Material Balances

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 03-01 Material and Energy Balances — Single Units and Process Flowsheets

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

Recycle, bypass, purge, and unsteady balances are explicit FE Chemical specification topics. Their detailed process-balance development here is guide-developed; the Handbook does not provide a dedicated formula set for these topics.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **2.1** Explain and apply **Recycle Streams and Overall Balances**.
* **2.2** Explain and apply **Recycle Ratio and Single-Pass versus Overall Performance**.
* **2.3** Explain and apply **Bypass Streams**.
* **2.4** Explain and apply **Purge Streams and Inert Accumulation**.
* **2.5** Explain and apply **General Unsteady Material Balance**.
* **2.6** Explain and apply **Well-Mixed Tank Transients**.
* **2.7** Explain and apply **Cut-Set Strategy for Complex Recycle Networks**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 2.1 Recycle Streams and Overall Balances

A recycle returns part of a downstream stream to an upstream unit. Recycle can increase conversion per fresh-feed pass, improve separation, or moderate operating conditions.

For an overall boundary drawn around the entire recycle loop, the internal recycle crosses the boundary zero times and cancels from the overall balance. Solve external fresh feed and product flows first whenever possible.

\[\text{overall balance: fresh feed}=\text{products+waste at steady state}\]

![FIG-03-02-001: Process with reactor, separator, recycle stream, fresh feed, product, and an overall boundary that excludes the internal recycle.](../figures/FIG-03-02-001-recycle-streams-and-overall-balances.png)

### Worked Example 1

**Problem.** Fresh feed is 100 kmol/h and recycle is 50 kmol/h. Find recycle ratio R=recycle/fresh.

**Solution.** For **Recycle Streams and Overall Balances**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 100, 50, R=0.50. This is the section-specific result for Fresh feed kmol recycle kmol recycle ratio. The stated units/basis (kmol/h, mol/h) are retained.

---

## 2.2 Recycle Ratio and Single-Pass versus Overall Performance

Recycle ratio may be defined as recycle flow divided by fresh feed or by another stated reference flow. Always use the problem's definition.

Single-pass conversion concerns material entering one reactor pass. Overall conversion concerns fresh reactant entering the process. They are different when unreacted material is recycled.

\[R=\frac{\dot n_{\rm recycle}}{\dot n_{\rm fresh}},\qquad X_{\rm overall}=\frac{\text{fresh reactant consumed}}{\text{fresh reactant fed}}\]

![FIG-03-02-002: Fresh feed, reactor feed, reactor effluent, recycle, and product showing single-pass versus overall conversion.](../figures/FIG-03-02-002-recycle-ratio-and-single-pass-versus-overall-performance.png)

### Worked Example 2

**Problem.** Fresh A feed is 100 mol/h; 90 mol/h is consumed overall. Find overall conversion.

**Solution.** For **Recycle Ratio and Single-Pass versus Overall Performance**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 100, 90, 90%. This is the section-specific result for Fresh feed mol mol consumed overall overall. The stated units/basis (mol/h, s) are retained.

---

## 2.3 Bypass Streams

A bypass sends part of a feed around a unit and recombines it later. Bypass is often used to control final temperature, concentration, or humidity.

The bypass stream has the same composition and state as the stream at the split point unless another device changes it.

\[\dot n_{\rm feed}=\dot n_{\rm processed}+\dot n_{\rm bypass}\]

![FIG-03-02-003: Feed split into process branch and bypass branch, then remixed to meet a target composition or temperature.](../figures/FIG-03-02-003-bypass-streams.png)

### Worked Example 3

**Problem.** A 100 kg/h feed is bypassed 30%. Find bypass and processed flows.

**Solution.** For **Bypass Streams**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 100, 30%, 30 and 70 kg/h. This is the section-specific result for kg feed bypassed bypass processed flows. The stated units/basis (kg/h, s) are retained.

---

## 2.4 Purge Streams and Inert Accumulation

A purge removes part of a recycle stream to prevent buildup of inert or undesired species. At steady state, an inert that enters only with fresh feed must leave through product and purge paths.

If the product contains negligible inert, the inert balance often determines the required purge directly.

\[\dot n_{I,\rm fresh}=\dot n_{I,\rm purge}+\dot n_{I,\rm product}\]

![FIG-03-02-004: Recycle loop containing an inert species with a purge split used to prevent inert accumulation.](../figures/FIG-03-02-004-purge-streams-and-inert-accumulation.png)

### Worked Example 4

**Problem.** An inert enters at 2 kmol/h and leaves only in a purge stream that is 10 mol% inert. Find total purge flow.

**Solution.** For **Purge Streams and Inert Accumulation**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 2, 10, 20 kmol/h. This is the section-specific result for inert enters kmol leaves only purge stream. The stated units/basis (kmol/h, mol/h) are retained.

---

## 2.5 General Unsteady Material Balance

For an unsteady control volume, accumulation is not zero. The governing accounting form is accumulation = input − output + generation − consumption.

For a nonreacting species, generation and consumption terms vanish.

\[\frac{dN_i}{dt}=\sum \dot n_{i,\rm in}-\sum \dot n_{i,\rm out}+r_{i,\rm gen}V\]

![FIG-03-02-005: Tank with varying inventory, inlet/outlet streams, and an accumulation term.](../figures/FIG-03-02-005-general-unsteady-material-balance.png)

### Worked Example 5

**Problem.** A tank has inlet 5 kg/min and outlet 3 kg/min with no reaction. Find accumulation rate.

**Solution.** For **General Unsteady Material Balance**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 5, 3, +2 kg/min. This is the section-specific result for tank has inlet kg min outlet kg. The stated units/basis (kg/min, min) are retained.

---

## 2.6 Well-Mixed Tank Transients

For a perfectly mixed tank, the outlet composition equals the tank composition. If volume is constant, a species balance can often be written directly on concentration.

The resulting first-order differential equation has the same exponential structure developed earlier for first-order dynamic systems.

\[V\frac{dC}{dt}=Q_{\rm in}C_{\rm in}-Q_{\rm out}C\]

![FIG-03-02-006: Constant-volume mixed tank with inlet concentration step and exponential outlet concentration response.](../figures/FIG-03-02-006-well-mixed-tank-transients.png)

### Worked Example 6

**Problem.** A constant-volume mixed tank has Q=10 L/min, V=100 L, Cin steps from 0 to 1 mol/L. Find time constant.

**Solution.** For **Well-Mixed Tank Transients**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) Q=10, V=100, τ=V/Q=10 min. This is the section-specific result for constant-volume mixed tank has min Cin steps. The stated units/basis (L/min, mol/L) are retained.

---

## 2.7 Cut-Set Strategy for Complex Recycle Networks

Complex process networks are easier when solved from the outside inward. First draw an overall boundary; next choose a cut that crosses the fewest unknown internal streams; finally solve individual units.

A good cut-set exposes specifications such as separator recovery, reactor conversion, or purge fraction without introducing unnecessary recycle unknowns.

\[\text{overall}\rightarrow\text{section balances}\rightarrow\text{unit balances}\]

![FIG-03-02-007: Multiunit recycle network with several candidate balance boundaries and the preferred minimal-unknown cut.](../figures/FIG-03-02-007-cut-set-strategy-for-complex-recycle-networks.png)

### Worked Example 7

**Problem.** Why should an overall balance around a recycle loop be used first?

**Solution.** For **Cut-Set Strategy for Complex Recycle Networks**, It eliminates the internal recycle unknown. This follows because complex process networks are easier when solved from the outside inward.. That physical distinction controls the result for should overall balance around recycle loop be.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A recycle process fresh feed is 20 kmol/h, product 18, purge 2. Verify steady total balance.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) 20, 18, 2, 20=18+2; balanced. This is the section-specific result for recycle process fresh feed kmol product purge. The stated units/basis (kmol/h, mol/h) are retained.

### Worked Example 9

**Problem.** A mixed tank with τ=5 min starts at C=0 and sees Cin=2 mol/L. Find C at t=5 min.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) =5, C=0, Cin=2, C=2(1-e^-1)=1.264 mol/L. This is the section-specific result for mixed tank min starts sees Cin mol. The stated units/basis (mol/L, min) are retained.

---

## As the Handbook States It

Primary source basis: **FE Chemical specification, Area 8B and 8E. The Handbook does not tabulate recycle/purge or general unsteady chemical-process material-balance formulas.**.

**Source boundary:** Recycle, bypass, purge, and unsteady balances are explicit FE Chemical specification topics. Their detailed process-balance development here is guide-developed; the Handbook does not provide a dedicated formula set for these topics.

**External source support:** Felder, Rousseau, and Bullard, *Elementary Principles of Chemical Processes*, 4th ed. (2016): multiple-unit processes pp. 116–122; recycle pp. 122–129; bypass p. 129; purging pp. 153–161; transient process balances pp. 570–591; and single well-mixed process units pp. 579–581. The chapter's cut-set/recycle-network strategy is additionally supported by Loh, H. T., Foo, D. C. Y., Short, M., & Isafiade, A. J. (2022), *Simultaneous Optimization of Mass Exchanger Networks and Direct Reuse/Recycle Networks*, DOI 10.1007/s41660-022-00288-6. The FE-study workflow remains a guide synthesis based on that network-optimization reference plus the Felder recycle-balance framework.

**Classification:** The FE Chemical specification establishes required coverage; these detailed workflows are **specification-required, externally supported**, not FE-Handbook lookup formulas.

Where the FE specification requires material not directly developed in the Handbook, this chapter now distinguishes **FE-Handbook-supported**, **specification-required / externally supported**, and **guide synthesis based on cited sources**.

---

## Where This Goes Wrong

**Using recycle stream without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using recycle ratio and overall conversion without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using bypass stream without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using purge balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using unsteady material balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using well-mixed tank transient without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using recycle-network solution strategy without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| recycle stream | Concept developed in §2.1; apply with the section's stated basis and assumptions. |
| recycle ratio and overall conversion | Concept developed in §2.2; apply with the section's stated basis and assumptions. |
| bypass stream | Concept developed in §2.3; apply with the section's stated basis and assumptions. |
| purge balance | Concept developed in §2.4; apply with the section's stated basis and assumptions. |
| unsteady material balance | Concept developed in §2.5; apply with the section's stated basis and assumptions. |
| well-mixed tank transient | Concept developed in §2.6; apply with the section's stated basis and assumptions. |
| recycle-network solution strategy | Concept developed in §2.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **recycle stream** and state the governing relation or balance.

2. Define **recycle ratio and overall conversion** and state the governing relation or balance.

3. Define **bypass stream** and state the governing relation or balance.

4. Define **purge balance** and state the governing relation or balance.

5. Define **unsteady material balance** and state the governing relation or balance.

6. Define **well-mixed tank transient** and state the governing relation or balance.

7. Define **recycle-network solution strategy** and state the governing relation or balance.

8. What is the most likely error if **recycle stream** is applied before the process basis and boundary are defined?

9. What is the most likely error if **recycle ratio and overall conversion** is applied before the process basis and boundary are defined?

10. What is the most likely error if **bypass stream** is applied before the process basis and boundary are defined?

11. What is the most likely error if **purge balance** is applied before the process basis and boundary are defined?

12. What is the most likely error if **unsteady material balance** is applied before the process basis and boundary are defined?

13. What is the most likely error if **well-mixed tank transient** is applied before the process basis and boundary are defined?

14. What is the most likely error if **recycle-network solution strategy** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **recycle stream**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **recycle ratio and overall conversion**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **bypass stream**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **purge balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **unsteady material balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **well-mixed tank transient**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **recycle-network solution strategy**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **recycle stream**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **recycle ratio and overall conversion**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **Recycle Streams and Overall Balances.** A recycle returns part of a downstream stream to an upstream unit. In Recycle, Bypass, Purge, and Unsteady Material Balances, this is the definition or balance being tested by Question 1.

2. **Recycle Ratio and Single-Pass versus Overall Performance.** Recycle ratio may be defined as recycle flow divided by fresh feed or by another stated reference flow. In Recycle, Bypass, Purge, and Unsteady Material Balances, this is the definition or balance being tested by Question 2.

3. **Bypass Streams.** A bypass sends part of a feed around a unit and recombines it later. In Recycle, Bypass, Purge, and Unsteady Material Balances, this is the definition or balance being tested by Question 3.

4. **Purge Streams and Inert Accumulation.** A purge removes part of a recycle stream to prevent buildup of inert or undesired species. In Recycle, Bypass, Purge, and Unsteady Material Balances, this is the definition or balance being tested by Question 4.

5. **General Unsteady Material Balance.** For an unsteady control volume, accumulation is not zero. In Recycle, Bypass, Purge, and Unsteady Material Balances, this is the definition or balance being tested by Question 5.

6. **Well-Mixed Tank Transients.** For a perfectly mixed tank, the outlet composition equals the tank composition. In Recycle, Bypass, Purge, and Unsteady Material Balances, this is the definition or balance being tested by Question 6.

7. **Cut-Set Strategy for Complex Recycle Networks.** Complex process networks are easier when solved from the outside inward. In Recycle, Bypass, Purge, and Unsteady Material Balances, this is the definition or balance being tested by Question 7.

8. For **Recycle Streams and Overall Balances**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A recycle returns part of a downstream stream to an upstream unit. This is the specific failure mode emphasized in Recycle, Bypass, Purge, and Unsteady Material Balances.

9. For **Recycle Ratio and Single-Pass versus Overall Performance**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Recycle ratio may be defined as recycle flow divided by fresh feed or by another stated reference flow. This is the specific failure mode emphasized in Recycle, Bypass, Purge, and Unsteady Material Balances.

10. For **Bypass Streams**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A bypass sends part of a feed around a unit and recombines it later. This is the specific failure mode emphasized in Recycle, Bypass, Purge, and Unsteady Material Balances.

11. For **Purge Streams and Inert Accumulation**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A purge removes part of a recycle stream to prevent buildup of inert or undesired species. This is the specific failure mode emphasized in Recycle, Bypass, Purge, and Unsteady Material Balances.

12. For **General Unsteady Material Balance**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For an unsteady control volume, accumulation is not zero. This is the specific failure mode emphasized in Recycle, Bypass, Purge, and Unsteady Material Balances.

13. For **Well-Mixed Tank Transients**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For a perfectly mixed tank, the outlet composition equals the tank composition. This is the specific failure mode emphasized in Recycle, Bypass, Purge, and Unsteady Material Balances.

14. For **Cut-Set Strategy for Complex Recycle Networks**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Complex process networks are easier when solved from the outside inward. This is the specific failure mode emphasized in Recycle, Bypass, Purge, and Unsteady Material Balances.

15. In **Recycle, Bypass, Purge, and Unsteady Material Balances**, close the material balance first because stream amounts and compositions feed the later energy calculation. Otherwise enthalpy and duty terms may be evaluated for unresolved streams.

16. For **Recycle, Bypass, Purge, and Unsteady Material Balances**, a degrees-of-freedom check counts unknowns against independent equations before solving. Zero indicates a closed problem; a positive count signals missing independent information.

17. In **Recycle, Bypass, Purge, and Unsteady Material Balances**, a relation supplied by the FE problem defines the intended model for that question. A remembered correlation can carry different assumptions, coefficients, validity limits, or reference states.

18. For **Recycle, Bypass, Purge, and Unsteady Material Balances**, separating Handbook-supported material from specification-required learned material distinguishes lookup knowledge from material the guide develops. That boundary prevents guide-developed content from being presented as Handbook text.

19. **A.** For **Recycle Streams and Overall Balances**, the relation is meaningful only with the correct basis and physical assumptions. A recycle returns part of a downstream stream to an upstream unit. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

20. **A.** For **Recycle Ratio and Single-Pass versus Overall Performance**, the relation is meaningful only with the correct basis and physical assumptions. Recycle ratio may be defined as recycle flow divided by fresh feed or by another stated reference flow. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

21. **A.** For **Bypass Streams**, the relation is meaningful only with the correct basis and physical assumptions. A bypass sends part of a feed around a unit and recombines it later. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

22. **A.** For **Purge Streams and Inert Accumulation**, the relation is meaningful only with the correct basis and physical assumptions. A purge removes part of a recycle stream to prevent buildup of inert or undesired species. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

23. **A.** For **General Unsteady Material Balance**, the relation is meaningful only with the correct basis and physical assumptions. For an unsteady control volume, accumulation is not zero. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

24. **A.** For **Well-Mixed Tank Transients**, the relation is meaningful only with the correct basis and physical assumptions. For a perfectly mixed tank, the outlet composition equals the tank composition. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

25. **A.** For **Cut-Set Strategy for Complex Recycle Networks**, the relation is meaningful only with the correct basis and physical assumptions. Complex process networks are easier when solved from the outside inward. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

26. **A.** This later check revisits **Recycle Streams and Overall Balances** from a different review position. A recycle returns part of a downstream stream to an upstream unit. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.

27. **A.** This later check revisits **Recycle Ratio and Single-Pass versus Overall Performance** from a different review position. Recycle ratio may be defined as recycle flow divided by fresh feed or by another stated reference flow. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.


---

## Practice Problems

1. Fresh feed is 100 kmol/h and recycle is 50 kmol/h. Find recycle ratio R=recycle/fresh.

2. Fresh A feed is 100 mol/h; 90 mol/h is consumed overall. Find overall conversion.

3. A 100 kg/h feed is bypassed 30%. Find bypass and processed flows.

4. An inert enters at 2 kmol/h and leaves only in a purge stream that is 10 mol% inert. Find total purge flow.

5. A tank has inlet 5 kg/min and outlet 3 kg/min with no reaction. Find accumulation rate.

6. A constant-volume mixed tank has Q=10 L/min, V=100 L, Cin steps from 0 to 1 mol/L. Find time constant.

7. Why should an overall balance around a recycle loop be used first?

8. A recycle process fresh feed is 20 kmol/h, product 18, purge 2. Verify steady total balance.

9. A mixed tank with τ=5 min starts at C=0 and sees Cin=2 mol/L. Find C at t=5 min.

10. If an inert enters at 1 kmol/h and purge gas is 5 mol% inert with no inert in product, find purge flow.


---

## Practice Problem Solutions

1. For the practice case involving **Fresh feed kmol recycle kmol recycle ratio**, Using 100, 50, R=0.50. This completes Practice Problem 1 in Recycle, Bypass, Purge, and Unsteady Material Balances. The original kmol/h, mol/h basis is preserved.

2. For the practice case involving **Fresh feed mol mol consumed overall overall**, Using 100, 90, 90%. This completes Practice Problem 2 in Recycle, Bypass, Purge, and Unsteady Material Balances. The original mol/h, s basis is preserved.

3. For the practice case involving **kg feed bypassed bypass processed flows**, Using 100, 30%, 30 and 70 kg/h. This completes Practice Problem 3 in Recycle, Bypass, Purge, and Unsteady Material Balances. The original kg/h, s basis is preserved.

4. For the practice case involving **inert enters kmol leaves only purge stream**, Using 2, 10, 20 kmol/h. This completes Practice Problem 4 in Recycle, Bypass, Purge, and Unsteady Material Balances. The original kmol/h, mol/h basis is preserved.

5. For the practice case involving **tank has inlet kg min outlet kg**, Using 5, 3, +2 kg/min. This completes Practice Problem 5 in Recycle, Bypass, Purge, and Unsteady Material Balances. The original kg/min, min basis is preserved.

6. For the practice case involving **constant-volume mixed tank has min Cin steps**, Using Q=10, V=100, τ=V/Q=10 min. This completes Practice Problem 6 in Recycle, Bypass, Purge, and Unsteady Material Balances. The original L/min, mol/L basis is preserved.

7. For the practice case involving **should overall balance around recycle loop be**, It eliminates the internal recycle unknown. This is the chapter-specific distinction required by Practice Problem 7 in Recycle, Bypass, Purge, and Unsteady Material Balances.

8. For the practice case involving **recycle process fresh feed kmol product purge**, Using 20, 18, 2, 20=18+2; balanced. This completes Practice Problem 8 in Recycle, Bypass, Purge, and Unsteady Material Balances. The original kmol/h, mol/h basis is preserved.

9. For the practice case involving **mixed tank min starts sees Cin mol**, Using =5, C=0, Cin=2, C=2(1-e^-1)=1.264 mol/L. This completes Practice Problem 9 in Recycle, Bypass, Purge, and Unsteady Material Balances. The original mol/L, min basis is preserved.

10. For the practice case involving **inert enters kmol purge gas mol inert**, Using 1, 5, 20 kmol/h. This completes Practice Problem 10 in Recycle, Bypass, Purge, and Unsteady Material Balances. The original kmol/h, mol/h basis is preserved.


---

## Quick Reference

**Source anchor:** FE Chemical specification, Area 8B and 8E. The Handbook does not tabulate recycle/purge or general unsteady chemical-process material-balance formulas..

- **recycle stream:** Recycle Streams and Overall Balances
- **recycle ratio and overall conversion:** Recycle Ratio and Single-Pass versus Overall Performance
- **bypass stream:** Bypass Streams
- **purge balance:** Purge Streams and Inert Accumulation
- **unsteady material balance:** General Unsteady Material Balance
- **well-mixed tank transient:** Well-Mixed Tank Transients
- **recycle-network solution strategy:** Cut-Set Strategy for Complex Recycle Networks
---

## What's Next

**03-03 — Reactive Material Balances, Combustion, and Heats of Reaction**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor
