---
chapter: "03-06"
title: "Distillation and Equilibrium-Stage Methods"
layer: 3
tier: null
track: chemical
template: technical
ledger_ids: [CHE-3-006-01, CHE-3-006-02, CHE-3-006-03, CHE-3-006-04, CHE-3-006-05, CHE-3-006-06, CHE-3-006-07]
routes: [chemical]
status: drafted
---

# Chapter 03-06: Distillation and Equilibrium-Stage Methods

> *"Chemical engineering becomes tractable when every stream, phase, reaction, and energy term has an explicit basis."*

---

## Before You Start

**Prerequisites:** 03-04 Phase Equilibrium · 03-01 Material Balances

**Route:** FE Chemical. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the correct process boundary and basis, choose the governing balance/equilibrium/rate relation, solve representative FE-level calculations, and state whether the needed relation is directly available in the Handbook.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly provides flash and Rayleigh balances, binary continuous-distillation balances and operating lines, reflux ratio, q-line behavior, a McCabe–Thiele VLE diagram, and Murphree plate efficiency.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **6.1** Explain and apply **Flash Distillation**.
* **6.2** Explain and apply **Differential or Rayleigh Distillation**.
* **6.3** Explain and apply **Continuous Column Overall and Component Balances**.
* **6.4** Explain and apply **Rectifying and Stripping Operating Lines**.
* **6.5** Explain and apply **Feed Condition and the q-Line**.
* **6.6** Explain and apply **McCabe–Thiele Stage Stepping**.
* **6.7** Explain and apply **Murphree Efficiency and Real Stages**.

---

## Notation Used Here

Chemical-process calculations may use mass, molar, or component-flow bases. Keep the chosen basis explicit and do not mix mass fractions with mole fractions. Absolute temperature is required where thermodynamic or kinetic equations require it.

---

## 6.1 Flash Distillation

A flash drum produces equilibrium vapor and liquid from one feed. At steady state, total and component balances combine with an equilibrium relation \(y_i=K_ix_i\).

For a binary ideal flash, one composition variable and vapor fraction can often be solved from balances and \(K\)-values.

\[F=V+L,\qquad Fz_i=Vy_i+Lx_i\]

![FIG-03-06-001: Feed entering equilibrium flash drum with vapor and liquid outlets and component balance labels.](../figures/FIG-03-06-001-flash-distillation.png)

### Worked Example 1

**Problem.** Flash feed F=100 kmol/h produces V=40. Find L.

**Solution.** For **Flash Distillation**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) F=100, V=40, 60 kmol/h. This is the section-specific result for Flash feed kmol produces. The stated units/basis (kmol/h, mol/h) are retained.

---

## 6.2 Differential or Rayleigh Distillation

In differential batch distillation, vapor is removed as it forms, so the still composition changes continuously. The Handbook gives the Rayleigh integral connecting remaining liquid amount and composition.

The equilibrium relation \(y(x)\) must be known or modeled.

\[\ln\frac{W}{W_0}=\int_{x_0}^{x}\frac{dx}{y-x}\]

![FIG-03-06-002: Batch still with changing pot composition, vapor withdrawal, and trajectory along VLE relation.](../figures/FIG-03-06-002-differential-or-rayleigh-distillation.png)

### Worked Example 2

**Problem.** Flash: F=100, zA=0.5, V=40, yA=0.8. Find xA in liquid.

**Solution.** For **Differential or Rayleigh Distillation**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) F=100, zA=0.5, V=40, 50=32+60x → x=0.30. This is the section-specific result for Flash zA yA xA liquid. The stated units/basis (s, h) are retained.

---

## 6.3 Continuous Column Overall and Component Balances

For a binary column, the external balance is \(F=D+B\) and \(Fz_F=Dx_D+Bx_B\). These balances determine product rates once product compositions are specified.

Internal stage balances generate operating lines.

\[F=D+B,\qquad Fz_F=Dx_D+Bx_B\]

![FIG-03-06-003: Binary distillation column with feed, distillate, bottoms, reflux, reboil, and overall/component balances.](../figures/FIG-03-06-003-continuous-column-overall-and-component-balances.png)

### Worked Example 3

**Problem.** Continuous column F=100, D=40. Find B.

**Solution.** For **Continuous Column Overall and Component Balances**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) F=100, D=40, 60. This is the section-specific result for Continuous column. The stated units/basis (s) are retained.

---

## 6.4 Rectifying and Stripping Operating Lines

Under constant molal overflow, the rectifying and stripping sections each have linear operating relations in \(x-y\) space.

The rectifying line is tied to reflux ratio and distillate composition. The stripping line is tied to bottoms flow and composition.

\[y_{n+1}=\frac{R_D}{R_D+1}x_n+\frac{x_D}{R_D+1}\]

![FIG-03-06-004: Binary x-y diagram showing equilibrium curve, rectifying line, stripping line, and feed intersection.](../figures/FIG-03-06-004-rectifying-and-stripping-operating-lines.png)

### Worked Example 4

**Problem.** For RD=3 and xD=0.9, write rectifying line.

**Solution.** For **Rectifying and Stripping Operating Lines**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) RD=3, xD=0.9, y=3/4 x + 0.9/4 =0.75x+0.225. This is the section-specific result for RD xD write rectifying line.

---

## 6.5 Feed Condition and the q-Line

The q-line represents feed thermal condition. Saturated liquid gives a vertical q-line; saturated vapor gives a horizontal q-line. Two-phase and subcooled/superheated feeds produce other slopes.

The q-line slope is \(q/(q-1)\).

\[\text{slope}_{q}=\frac{q}{q-1}\]

![FIG-03-06-005: Family of q-lines for saturated liquid, two-phase, saturated vapor, subcooled liquid, and superheated vapor.](../figures/FIG-03-06-005-feed-condition-and-the-q-line.png)

### Worked Example 5

**Problem.** What is q-line slope for q=1?

**Solution.** For **Feed Condition and the q-Line**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) q=1, Infinite/vertical. This is the section-specific result for q-line slope. The stated units/basis (s, h) are retained.

---

## 6.6 McCabe–Thiele Stage Stepping

The McCabe–Thiele method alternates horizontal equilibrium moves and vertical operating-line moves between \(x_D\) and \(x_B\). Each step corresponds to an ideal equilibrium stage under the method's assumptions.

Minimum reflux occurs when the operating construction pinches the equilibrium curve and ideal-stage count tends toward infinity.

\[\text{stage count by alternating equilibrium and operating-line steps}\]

![FIG-03-06-006: Binary x-y equilibrium plot with operating lines and staircase stage construction.](../figures/FIG-03-06-006-mccabe-thiele-stage-stepping.png)

### Worked Example 6

**Problem.** Why does minimum reflux imply infinite theoretical stages?

**Solution.** For **McCabe–Thiele Stage Stepping**, The operating construction pinches the equilibrium curve, driving local mass-transfer/stage progress to zero. This follows because the McCabe–Thiele method alternates horizontal equilibrium moves and vertical operating-line moves between \(x_D\) and \(x_B\).. That physical distinction controls the result for does minimum reflux imply infinite theoretical stages.

---

## 6.7 Murphree Efficiency and Real Stages

Real trays may not achieve full equilibrium. The Handbook gives Murphree vapor efficiency based on actual vapor composition change relative to the equilibrium change possible from the leaving liquid.

Efficiency converts ideal-stage performance into a more realistic tray requirement when the stated approximation is appropriate.

\[E_{MV}=\frac{y_n-y_{n+1}}{y_n^*-y_{n+1}}\]

![FIG-03-06-007: One distillation tray with entering/leaving vapor compositions, leaving liquid equilibrium value, and Murphree efficiency.](../figures/FIG-03-06-007-murphree-efficiency-and-real-stages.png)

### Worked Example 7

**Problem.** yn=0.70, yn+1=0.50, yn*=0.80. Find Murphree vapor efficiency.

**Solution.** For **Murphree Efficiency and Real Stages**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) yn=0.70, =0.50, =0.80, E=(0.70-0.50)/(0.80-0.50)=0.667. This is the section-specific result for yn yn yn Murphree vapor efficiency. The stated units/basis (h) are retained.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Overall binary balance: F=100, z=0.5, xD=0.9, xB=0.1. Find D and B.

**Solution.** For **Integrated Worked Examples**, identify the requested quantity and keep the problem definition unchanged. With the given condition(s) F=100, z=0.5, xD=0.9, D=50; B=50. This is the section-specific result for Overall binary balance xD xB.

### Worked Example 9

**Problem.** At total reflux, what happens to external product withdrawal in ideal analysis?

**Solution.** For **Integrated Worked Examples**, Distillate and bottoms withdrawals go to zero; internal reflux is maximal. This follows because the section distinguishes the governing physical behavior from the alternatives. That physical distinction controls the result for total reflux happens external product withdrawal ideal.

---

## As the Handbook States It

Primary source basis: **Chemical Engineering, printed pp. 250–252; FE Chemical specification Area 10C–E**.

**Source boundary:** The Handbook directly provides flash and Rayleigh balances, binary continuous-distillation balances and operating lines, reflux ratio, q-line behavior, a McCabe–Thiele VLE diagram, and Murphree plate efficiency.

Where the FE specification requires a topic that is not directly developed in the Handbook, this chapter marks that material as **specification-required / guide-developed** rather than implying that the formula or workflow is printed in the Handbook.

---

## Where This Goes Wrong

**Using flash distillation without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using Rayleigh distillation without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using continuous distillation balance without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using distillation operating line without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using distillation q-line without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using McCabe-Thiele method without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Using Murphree plate efficiency without a defined basis.** Confirm stream basis, phase, steady/unsteady condition, reaction/equilibrium model, and units before calculation.

**Solving equations before drawing the process.** A labeled flowsheet, balance boundary, and degrees-of-freedom check usually expose the intended solution path.

**Assuming the Handbook contains every required relation.** The FE Chemical specification includes learned material not fully tabulated in Handbook 10.6; those items are explicitly identified in this guide.

---

## Key Terms

| Term | Working definition |
|---|---|
| flash distillation | Concept developed in §6.1; apply with the section's stated basis and assumptions. |
| Rayleigh distillation | Concept developed in §6.2; apply with the section's stated basis and assumptions. |
| continuous distillation balance | Concept developed in §6.3; apply with the section's stated basis and assumptions. |
| distillation operating line | Concept developed in §6.4; apply with the section's stated basis and assumptions. |
| distillation q-line | Concept developed in §6.5; apply with the section's stated basis and assumptions. |
| McCabe-Thiele method | Concept developed in §6.6; apply with the section's stated basis and assumptions. |
| Murphree plate efficiency | Concept developed in §6.7; apply with the section's stated basis and assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **flash distillation** and state the governing relation or balance.

2. Define **Rayleigh distillation** and state the governing relation or balance.

3. Define **continuous distillation balance** and state the governing relation or balance.

4. Define **distillation operating line** and state the governing relation or balance.

5. Define **distillation q-line** and state the governing relation or balance.

6. Define **McCabe-Thiele method** and state the governing relation or balance.

7. Define **Murphree plate efficiency** and state the governing relation or balance.

8. What is the most likely error if **flash distillation** is applied before the process basis and boundary are defined?

9. What is the most likely error if **Rayleigh distillation** is applied before the process basis and boundary are defined?

10. What is the most likely error if **continuous distillation balance** is applied before the process basis and boundary are defined?

11. What is the most likely error if **distillation operating line** is applied before the process basis and boundary are defined?

12. What is the most likely error if **distillation q-line** is applied before the process basis and boundary are defined?

13. What is the most likely error if **McCabe-Thiele method** is applied before the process basis and boundary are defined?

14. What is the most likely error if **Murphree plate efficiency** is applied before the process basis and boundary are defined?

15. Why should a material balance normally be closed before a process energy balance?

16. What is the purpose of a degrees-of-freedom check?

17. When should a relation supplied by an FE problem override a remembered correlation?

18. Why must Handbook-supported content be separated from specification-required learned content?

### Multiple Choice

19. Which statement is most accurate for **flash distillation**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

20. Which statement is most accurate for **Rayleigh distillation**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

21. Which statement is most accurate for **continuous distillation balance**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

22. Which statement is most accurate for **distillation operating line**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

23. Which statement is most accurate for **distillation q-line**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

24. Which statement is most accurate for **McCabe-Thiele method**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

25. Which statement is most accurate for **Murphree plate efficiency**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

26. Which statement is most accurate for **flash distillation**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook

27. Which statement is most accurate for **Rayleigh distillation**?
A) It must be applied with the correct process basis and physical assumptions
B) It is independent of composition and phase
C) It replaces material/energy conservation
D) It is always directly tabulated in the Handbook


---

## Answer Key with Explanations

1. **Flash Distillation.** A flash drum produces equilibrium vapor and liquid from one feed. In Distillation and Equilibrium-Stage Methods, this is the definition or balance being tested by Question 1.

2. **Differential or Rayleigh Distillation.** In differential batch distillation, vapor is removed as it forms, so the still composition changes continuously. In Distillation and Equilibrium-Stage Methods, this is the definition or balance being tested by Question 2.

3. **Continuous Column Overall and Component Balances.** For a binary column, the external balance is \(F=D+B\) and \(Fz_F=Dx_D+Bx_B\). In Distillation and Equilibrium-Stage Methods, this is the definition or balance being tested by Question 3.

4. **Rectifying and Stripping Operating Lines.** Under constant molal overflow, the rectifying and stripping sections each have linear operating relations in \(x-y\) space. In Distillation and Equilibrium-Stage Methods, this is the definition or balance being tested by Question 4.

5. **Feed Condition and the q-Line.** Saturated liquid gives a vertical q-line; saturated vapor gives a horizontal q-line. In Distillation and Equilibrium-Stage Methods, this is the definition or balance being tested by Question 5.

6. **McCabe–Thiele Stage Stepping.** The McCabe–Thiele method alternates horizontal equilibrium moves and vertical operating-line moves between \(x_D\) and \(x_B\). In Distillation and Equilibrium-Stage Methods, this is the definition or balance being tested by Question 6.

7. **Murphree Efficiency and Real Stages.** The Handbook gives Murphree vapor efficiency based on actual vapor composition change relative to the equilibrium change possible from the leaving liquid. In Distillation and Equilibrium-Stage Methods, this is the definition or balance being tested by Question 7.

8. For **Flash Distillation**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. A flash drum produces equilibrium vapor and liquid from one feed. This is the specific failure mode emphasized in Distillation and Equilibrium-Stage Methods.

9. For **Differential or Rayleigh Distillation**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. In differential batch distillation, vapor is removed as it forms, so the still composition changes continuously. This is the specific failure mode emphasized in Distillation and Equilibrium-Stage Methods.

10. For **Continuous Column Overall and Component Balances**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. For a binary column, the external balance is \(F=D+B\) and \(Fz_F=Dx_D+Bx_B\). This is the specific failure mode emphasized in Distillation and Equilibrium-Stage Methods.

11. For **Rectifying and Stripping Operating Lines**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Under constant molal overflow, the rectifying and stripping sections each have linear operating relations in \(x-y\) space. This is the specific failure mode emphasized in Distillation and Equilibrium-Stage Methods.

12. For **Feed Condition and the q-Line**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. Saturated liquid gives a vertical q-line; saturated vapor gives a horizontal q-line. This is the specific failure mode emphasized in Distillation and Equilibrium-Stage Methods.

13. For **McCabe–Thiele Stage Stepping**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The McCabe–Thiele method alternates horizontal equilibrium moves and vertical operating-line moves between \(x_D\) and \(x_B\). This is the specific failure mode emphasized in Distillation and Equilibrium-Stage Methods.

14. For **Murphree Efficiency and Real Stages**, an undefined basis, boundary, phase, or model can invalidate the setup before any arithmetic begins. The Handbook gives Murphree vapor efficiency based on actual vapor composition change relative to the equilibrium change possible from the leaving liquid. This is the specific failure mode emphasized in Distillation and Equilibrium-Stage Methods.

15. In **Distillation and Equilibrium-Stage Methods**, close the material balance first because stream amounts and compositions feed the later energy calculation. Otherwise enthalpy and duty terms may be evaluated for unresolved streams.

16. For **Distillation and Equilibrium-Stage Methods**, a degrees-of-freedom check counts unknowns against independent equations before solving. Zero indicates a closed problem; a positive count signals missing independent information.

17. In **Distillation and Equilibrium-Stage Methods**, a relation supplied by the FE problem defines the intended model for that question. A remembered correlation can carry different assumptions, coefficients, validity limits, or reference states.

18. For **Distillation and Equilibrium-Stage Methods**, separating Handbook-supported material from specification-required learned material distinguishes lookup knowledge from material the guide develops. That boundary prevents guide-developed content from being presented as Handbook text.

19. **A.** For **Flash Distillation**, the relation is meaningful only with the correct basis and physical assumptions. A flash drum produces equilibrium vapor and liquid from one feed. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

20. **A.** For **Differential or Rayleigh Distillation**, the relation is meaningful only with the correct basis and physical assumptions. In differential batch distillation, vapor is removed as it forms, so the still composition changes continuously. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

21. **A.** For **Continuous Column Overall and Component Balances**, the relation is meaningful only with the correct basis and physical assumptions. For a binary column, the external balance is \(F=D+B\) and \(Fz_F=Dx_D+Bx_B\). Choices B–D incorrectly detach the concept from the defined system or conservation framework.

22. **A.** For **Rectifying and Stripping Operating Lines**, the relation is meaningful only with the correct basis and physical assumptions. Under constant molal overflow, the rectifying and stripping sections each have linear operating relations in \(x-y\) space. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

23. **A.** For **Feed Condition and the q-Line**, the relation is meaningful only with the correct basis and physical assumptions. Saturated liquid gives a vertical q-line; saturated vapor gives a horizontal q-line. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

24. **A.** For **McCabe–Thiele Stage Stepping**, the relation is meaningful only with the correct basis and physical assumptions. The McCabe–Thiele method alternates horizontal equilibrium moves and vertical operating-line moves between \(x_D\) and \(x_B\). Choices B–D incorrectly detach the concept from the defined system or conservation framework.

25. **A.** For **Murphree Efficiency and Real Stages**, the relation is meaningful only with the correct basis and physical assumptions. The Handbook gives Murphree vapor efficiency based on actual vapor composition change relative to the equilibrium change possible from the leaving liquid. Choices B–D incorrectly detach the concept from the defined system or conservation framework.

26. **A.** This later check revisits **Flash Distillation** from a different review position. A flash drum produces equilibrium vapor and liquid from one feed. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.

27. **A.** This later check revisits **Differential or Rayleigh Distillation** from a different review position. In differential batch distillation, vapor is removed as it forms, so the still composition changes continuously. The correct choice remains A because the concept still depends on the defined basis and physical assumptions.


---

## Practice Problems

1. Flash feed F=100 kmol/h produces V=40. Find L.

2. Flash: F=100, zA=0.5, V=40, yA=0.8. Find xA in liquid.

3. Continuous column F=100, D=40. Find B.

4. For RD=3 and xD=0.9, write rectifying line.

5. What is q-line slope for q=1?

6. Why does minimum reflux imply infinite theoretical stages?

7. yn=0.70, yn+1=0.50, yn*=0.80. Find Murphree vapor efficiency.

8. Overall binary balance: F=100, z=0.5, xD=0.9, xB=0.1. Find D and B.

9. At total reflux, what happens to external product withdrawal in ideal analysis?

10. If a feed is saturated vapor, what is q?


---

## Practice Problem Solutions

1. For the practice case involving **Flash feed kmol produces**, Using F=100, V=40, 60 kmol/h. This completes Practice Problem 1 in Distillation and Equilibrium-Stage Methods. The original kmol/h, mol/h basis is preserved.

2. For the practice case involving **Flash zA yA xA liquid**, Using F=100, zA=0.5, V=40, 50=32+60x → x=0.30. This completes Practice Problem 2 in Distillation and Equilibrium-Stage Methods. The original s, h basis is preserved.

3. For the practice case involving **Continuous column**, Using F=100, D=40, 60. This completes Practice Problem 3 in Distillation and Equilibrium-Stage Methods. The original s basis is preserved.

4. For the practice case involving **RD xD write rectifying line**, Using RD=3, xD=0.9, y=3/4 x + 0.9/4 =0.75x+0.225. This completes Practice Problem 4 in Distillation and Equilibrium-Stage Methods.

5. For the practice case involving **q-line slope**, Using q=1, Infinite/vertical. This completes Practice Problem 5 in Distillation and Equilibrium-Stage Methods. The original s, h basis is preserved.

6. For the practice case involving **does minimum reflux imply infinite theoretical stages**, The operating construction pinches the equilibrium curve, driving local mass-transfer/stage progress to zero. This is the chapter-specific distinction required by Practice Problem 6 in Distillation and Equilibrium-Stage Methods.

7. For the practice case involving **yn yn yn Murphree vapor efficiency**, Using yn=0.70, =0.50, =0.80, E=(0.70-0.50)/(0.80-0.50)=0.667. This completes Practice Problem 7 in Distillation and Equilibrium-Stage Methods. The original h basis is preserved.

8. For the practice case involving **Overall binary balance xD xB**, Using F=100, z=0.5, xD=0.9, D=50; B=50. This completes Practice Problem 8 in Distillation and Equilibrium-Stage Methods.

9. For the practice case involving **total reflux happens external product withdrawal ideal**, Distillate and bottoms withdrawals go to zero; internal reflux is maximal. This is the chapter-specific distinction required by Practice Problem 9 in Distillation and Equilibrium-Stage Methods.

10. For the practice case involving **feed saturated vapor**, q=0. This is the chapter-specific distinction required by Practice Problem 10 in Distillation and Equilibrium-Stage Methods.


---

## Quick Reference

**Source anchor:** Chemical Engineering, printed pp. 250–252; FE Chemical specification Area 10C–E.

- **flash distillation:** Flash Distillation
- **Rayleigh distillation:** Differential or Rayleigh Distillation
- **continuous distillation balance:** Continuous Column Overall and Component Balances
- **distillation operating line:** Rectifying and Stripping Operating Lines
- **distillation q-line:** Feed Condition and the q-Line
- **McCabe-Thiele method:** McCabe–Thiele Stage Stepping
- **Murphree plate efficiency:** Murphree Efficiency and Real Stages
---

## What's Next

**03-07 — Absorption, Extraction, Adsorption, and Membrane Separations**

Carry forward the Chemical-track workflow: establish a basis and boundary, close material balances, apply the correct equilibrium/rate/transport model, then close energy, economics, control, and safety checks as needed.

— Your Mentor
