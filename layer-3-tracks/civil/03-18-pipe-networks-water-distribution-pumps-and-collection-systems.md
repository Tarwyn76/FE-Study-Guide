---
chapter: "03-18"
title: "Pipe Networks, Water Distribution, Pumps, and Collection Systems"
layer: 3
tier: null
track: civil
template: technical
ledger_ids: [CIV-3-018-01, CIV-3-018-02, CIV-3-018-03, CIV-3-018-04, CIV-3-018-05, CIV-3-018-06, CIV-3-018-07]
routes: [civil]
status: drafted
---

# Chapter 03-18: Pipe Networks, Water Distribution, Pumps, and Collection Systems

> *"Civil engineering problems become manageable when the geometry, loads or flows, material model, and boundary conditions are made explicit."*

---

## Before You Start

**Prerequisites:** FLUID-2D-044-02 · FLUID-2D-046-05

**Route:** FE Civil. This is a Layer 3 discipline-track chapter.

**Skip if:** You can identify the governing civil-engineering model, select the correct Handbook relation or specification-required workflow, carry units consistently, and complete representative FE-level calculations without prompting.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops the FE Civil topics grouped under **Pipe Networks, Water Distribution, Pumps, and Collection Systems**. It builds on the shared Layer 1–2 foundation rather than reteaching it. Handbook-supported equations are identified as such; specification-required material that is not directly tabulated in Handbook 10.6 is marked as guide-developed.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **18.1** Explain and apply **Pipe energy equation and hydraulic grade line**.
* **18.2** Explain and apply **Darcy-Weisbach and minor losses**.
* **18.3** Explain and apply **Hazen-Williams water-distribution relation**.
* **18.4** Explain and apply **Network continuity and loop energy balance**.
* **18.5** Explain and apply **Pump head, power, efficiency, and operating point**.
* **18.6** Explain and apply **Water distribution storage, pressure, and service constraints**.
* **18.7** Explain and apply **Gravity collection systems and sewer flow concepts**.

---

## Notation Used Here

Use one unit system at a time. Define positive directions, reference elevations, load/flow signs, and geometric variables before substituting numbers. Symbols may change meaning between civil subdisciplines; the local section definition governs.

---

## 18.1 Pipe energy equation and hydraulic grade line

Closed-conduit systems are solved by combining conservation of energy with continuity. Distinguish the hydraulic grade line from the energy grade line.

\[\frac{p_1}{\gamma}+z_1+\frac{V_1^2}{2g}+h_p=\frac{p_2}{\gamma}+z_2+\frac{V_2^2}{2g}+h_L+h_t\]

![FIG-03-18-001: Pipe between reservoirs showing HGL, EGL, pump head, minor losses, and friction loss.](../figures/FIG-03-18-001-pipe-energy-equation-and-hydraulic-grade-line.png)

### Worked Example 1

**Problem.** Between equal-diameter reservoirs with no pump, elevation difference is consumed by head loss.

**Solution.** Apply the relation and definitions in §18.1; the stated result follows with consistent units and sign convention.

---

## 18.2 Darcy-Weisbach and minor losses

Major and minor losses both scale with velocity head. Verify whether the friction factor is Darcy or Fanning before substitution.

\[h_L=f\frac{L}{D}\frac{V^2}{2g}+\sum K\frac{V^2}{2g}\]

![FIG-03-18-002: Pipe run with fittings, valves, entrance, exit, and distributed friction-loss annotations.](../figures/FIG-03-18-002-darcy-weisbach-and-minor-losses.png)

### Worked Example 2

**Problem.** If K_total=4 and V²/(2g)=1.2 ft, minor loss is 4.8 ft.

**Solution.** Apply the relation and definitions in §18.2; the stated result follows with consistent units and sign convention.

---

## 18.3 Hazen-Williams water-distribution relation

Hazen-Williams is commonly used for water-distribution calculations. Use the Handbook form and unit constants exactly as printed.

\[h_f\propto \frac{LQ^{1.852}}{C^{1.852}D^{4.87}}\]

![FIG-03-18-003: Head-loss versus flow curves for several pipe diameters using Hazen-Williams behavior.](../figures/FIG-03-18-003-hazen-williams-water-distribution-relation.png)

### Worked Example 3

**Problem.** Increasing diameter strongly reduces head loss because diameter appears to a high exponent.

**Solution.** Apply the relation and definitions in §18.3; the stated result follows with consistent units and sign convention.

---

## 18.4 Network continuity and loop energy balance

Network solutions must satisfy continuity at every junction and energy consistency around loops. Flow directions may be assumed and corrected.

\[\sum Q_{\text{node}}=0,\qquad \sum h_L{}_{\text{loop}}=0\]

![FIG-03-18-004: Looped water-distribution network with junction demands, assumed flow arrows, reservoirs, and a pump.](../figures/FIG-03-18-004-network-continuity-and-loop-energy-balance.png)

### Worked Example 4

**Problem.** At a junction with 3 cfs and 5 cfs entering, an 8 cfs outflow balances continuity.

**Solution.** Apply the relation and definitions in §18.4; the stated result follows with consistent units and sign convention.

---

## 18.5 Pump head, power, efficiency, and operating point

The system operating point occurs where the pump curve intersects the system curve. Efficiency converts hydraulic power to required input power.

\[P_{\text{in}}=\frac{\gamma QH_p}{\eta}\]

![FIG-03-18-005: Pump curve and system curve intersecting at operating point, with efficiency region labeled.](../figures/FIG-03-18-005-pump-head-power-efficiency-and-operating-point.png)

### Worked Example 5

**Problem.** γQH=50 hp hydraulic and η=0.80 requires 62.5 hp input.

**Solution.** Apply the relation and definitions in §18.5; the stated result follows with consistent units and sign convention.

---

## 18.6 Water distribution storage, pressure, and service constraints

Distribution systems must maintain usable pressure while meeting demand and fire-flow conditions. Elevation and head loss directly affect pressure.

\[p=\gamma h\]

![FIG-03-18-006: Elevated tank and distribution main across varying ground elevations with pressure heads at nodes.](../figures/FIG-03-18-006-water-distribution-storage-pressure-and-service-constraints.png)

### Worked Example 6

**Problem.** A 100-ft water head corresponds to about 43.3 psi.

**Solution.** Apply the relation and definitions in §18.6; the stated result follows with consistent units and sign convention.

---

## 18.7 Gravity collection systems and sewer flow concepts

Sanitary and storm collection systems combine continuity with open-channel or partially full conduit behavior. Grade, capacity, and minimum velocity are linked.

\[Q=VA\]

![FIG-03-18-007: Gravity sewer network with manholes, slopes, inflows, and downstream interceptor.](../figures/FIG-03-18-007-gravity-collection-systems-and-sewer-flow-concepts.png)

### Worked Example 7

**Problem.** A 4 ft² flowing area at 3 ft/s conveys 12 cfs.

**Solution.** Apply the relation and definitions in §18.7; the stated result follows with consistent units and sign convention.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A problem combines two ideas from this chapter. What should be done before calculation?

**Solution.** Draw the system, identify the requested quantity, establish units and sign conventions, and list the governing relations before substituting numbers.

### Worked Example 9

**Problem.** A remembered equation differs from the FE Reference Handbook form. Which should govern the exam solution?

**Solution.** Use the Handbook form and its unit convention unless the problem explicitly supplies a different relation.

---

## As the Handbook States It

Primary source basis: **FE Civil specification Area 10; FE Reference Handbook 10.6 Civil Engineering and supporting general sections cited below.**

**Source boundary:** Some Civil specification topics are directly tabulated in the Handbook; others are named by the specification but require learned engineering knowledge. This chapter does not imply that every workflow, code provision, or design factor is printed in the Handbook.

Where the FE specification requires a topic that is not directly developed in the Handbook, the ledger marks it **specification-required / guide-developed** rather than inventing a Handbook citation.

---

## Where This Goes Wrong

**Using pipe energy equation without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using pipe head loss without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using Hazen-Williams equation without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using pipe network without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using pump operating point without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using water distribution service without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Using collection system hydraulics without its assumptions.** Confirm the geometry, boundary conditions, unit system, and meaning of each variable before calculation.

**Solving before sketching the system.** A quick civil-engineering sketch often exposes the controlling geometry, load path, hydraulic grade, soil profile, or construction sequence.

**Treating every required Civil topic as a Handbook lookup.** The FE Civil specification includes learned material not completely tabulated in Handbook 10.6.

---

## Key Terms

| Term | Working definition |
|---|---|
| pipe energy equation | Concept developed in §18.1; apply with that section's stated assumptions and units. |
| pipe head loss | Concept developed in §18.2; apply with that section's stated assumptions and units. |
| Hazen-Williams equation | Concept developed in §18.3; apply with that section's stated assumptions and units. |
| pipe network | Concept developed in §18.4; apply with that section's stated assumptions and units. |
| pump operating point | Concept developed in §18.5; apply with that section's stated assumptions and units. |
| water distribution service | Concept developed in §18.6; apply with that section's stated assumptions and units. |
| collection system hydraulics | Concept developed in §18.7; apply with that section's stated assumptions and units. |

---

## Review Questions

### Conceptual and Applied

1. Define **pipe energy equation** and identify the principal quantity, relation, or decision it organizes.

2. Define **pipe head loss** and identify the principal quantity, relation, or decision it organizes.

3. Define **Hazen-Williams equation** and identify the principal quantity, relation, or decision it organizes.

4. Define **pipe network** and identify the principal quantity, relation, or decision it organizes.

5. Define **pump operating point** and identify the principal quantity, relation, or decision it organizes.

6. Define **water distribution service** and identify the principal quantity, relation, or decision it organizes.

7. Define **collection system hydraulics** and identify the principal quantity, relation, or decision it organizes.

8. What assumption or unit error is most likely to cause a wrong result when applying **pipe energy equation**?

9. What assumption or unit error is most likely to cause a wrong result when applying **pipe head loss**?

10. What assumption or unit error is most likely to cause a wrong result when applying **Hazen-Williams equation**?

11. What assumption or unit error is most likely to cause a wrong result when applying **pipe network**?

12. What assumption or unit error is most likely to cause a wrong result when applying **pump operating point**?

13. What assumption or unit error is most likely to cause a wrong result when applying **water distribution service**?

14. What assumption or unit error is most likely to cause a wrong result when applying **collection system hydraulics**?

15. Why should the physical model or control volume be drawn before selecting an equation?

16. When should a relation supplied in the FE Reference Handbook be preferred over a remembered version?

17. Why should SI and U.S. customary units not be mixed inside one equation without explicit conversion?

18. What is the purpose of an independent reasonableness check after the numerical solution?

### Multiple Choice

19. Which statement is most accurate for **pipe energy equation**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

20. Which statement is most accurate for **pipe head loss**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

21. Which statement is most accurate for **Hazen-Williams equation**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

22. Which statement is most accurate for **pipe network**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

23. Which statement is most accurate for **pump operating point**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

24. Which statement is most accurate for **water distribution service**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept

25. Which statement is most accurate for **collection system hydraulics**?
A) It must be applied with the stated units, assumptions, and boundary conditions
B) It is independent of geometry and units
C) It replaces equilibrium or conservation
D) It is always a purely qualitative concept


26. Which check is most useful immediately before accepting a numerical answer?
A) Dimensional consistency and physical reasonableness
B) Replacing the stated geometry with a standard case
C) Dropping signs and directions
D) Assuming every quantity is SI

27. When a Civil specification topic is not fully tabulated in Handbook 10.6, the guide should:
A) Identify it as specification-required / learned material
B) Invent a Handbook page reference
C) Omit the topic
D) Treat it as optional


---

## Answer Key with Explanations

1. **pipe energy equation** is developed in §18.1. Use the displayed relation or decision sequence with the section's stated assumptions and units.

2. **pipe head loss** is developed in §18.2. Use the displayed relation or decision sequence with the section's stated assumptions and units.

3. **Hazen-Williams equation** is developed in §18.3. Use the displayed relation or decision sequence with the section's stated assumptions and units.

4. **pipe network** is developed in §18.4. Use the displayed relation or decision sequence with the section's stated assumptions and units.

5. **pump operating point** is developed in §18.5. Use the displayed relation or decision sequence with the section's stated assumptions and units.

6. **water distribution service** is developed in §18.6. Use the displayed relation or decision sequence with the section's stated assumptions and units.

7. **collection system hydraulics** is developed in §18.7. Use the displayed relation or decision sequence with the section's stated assumptions and units.

8. For **pipe energy equation**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

9. For **pipe head loss**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

10. For **Hazen-Williams equation**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

11. For **pipe network**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

12. For **pump operating point**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

13. For **water distribution service**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

14. For **collection system hydraulics**, common failures are wrong units, wrong sign convention, wrong geometry/boundary condition, or using a relation outside its assumptions.

15. The sketch exposes geometry, boundaries, loads/flows, signs, and missing data before algebra begins.

16. Use the Handbook form when it is available because the FE exam supplies that reference and its constants/unit conventions govern the problem.

17. Mixed unit systems create hidden conversion errors and can invalidate dimensional consistency.

18. A reasonableness check can catch sign, magnitude, boundary-condition, and unit errors that algebra alone does not reveal.

19. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

20. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

21. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

22. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

23. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

24. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

25. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

26. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.

27. **A.** The relation or workflow depends on the stated units, assumptions, geometry, and boundary conditions.



---

## Practice Problems

1. Between equal-diameter reservoirs with no pump, elevation difference is consumed by head loss.

2. If K_total=4 and V²/(2g)=1.2 ft, minor loss is 4.8 ft.

3. Increasing diameter strongly reduces head loss because diameter appears to a high exponent.

4. At a junction with 3 cfs and 5 cfs entering, an 8 cfs outflow balances continuity.

5. γQH=50 hp hydraulic and η=0.80 requires 62.5 hp input.

6. A 100-ft water head corresponds to about 43.3 psi.

7. A 4 ft² flowing area at 3 ft/s conveys 12 cfs.

8. Identify one unit or sign-convention check that should be completed before accepting the answer.

9. Name the Handbook section or specification area you would consult first for this chapter's governing relation.

10. Explain in one sentence why a physically reasonable sketch can reveal an error before calculation.


---

## Practice Problem Solutions

1. Use §18.1. Between equal-diameter reservoirs with no pump, elevation difference is consumed by head loss. The calculation or classification follows from the displayed section relation and the stated data.

2. Use §18.2. If K_total=4 and V²/(2g)=1.2 ft, minor loss is 4.8 ft. The calculation or classification follows from the displayed section relation and the stated data.

3. Use §18.3. Increasing diameter strongly reduces head loss because diameter appears to a high exponent. The calculation or classification follows from the displayed section relation and the stated data.

4. Use §18.4. At a junction with 3 cfs and 5 cfs entering, an 8 cfs outflow balances continuity. The calculation or classification follows from the displayed section relation and the stated data.

5. Use §18.5. γQH=50 hp hydraulic and η=0.80 requires 62.5 hp input. The calculation or classification follows from the displayed section relation and the stated data.

6. Use §18.6. A 100-ft water head corresponds to about 43.3 psi. The calculation or classification follows from the displayed section relation and the stated data.

7. Use §18.7. A 4 ft² flowing area at 3 ft/s conveys 12 cfs. The calculation or classification follows from the displayed section relation and the stated data.

8. Check dimensions, unit conversion, sign convention, and whether the selected relation's assumptions match the physical situation.

9. Start with FE Civil specification Area 10 and the Handbook sections identified in **As the Handbook States It** and the ledger entries for this chapter.

10. A sketch exposes incompatible geometry, impossible flow/load directions, missing reactions/boundaries, and double-counted or omitted terms.

---

## Quick Reference

**Source anchor:** FE Civil specification Area 10.

- **pipe energy equation:** Pipe energy equation and hydraulic grade line
- **pipe head loss:** Darcy-Weisbach and minor losses
- **Hazen-Williams equation:** Hazen-Williams water-distribution relation
- **pipe network:** Network continuity and loop energy balance
- **pump operating point:** Pump head, power, efficiency, and operating point
- **water distribution service:** Water distribution storage, pressure, and service constraints
- **collection system hydraulics:** Gravity collection systems and sewer flow concepts

---

## What's Next

**Chapter 03-19: Flood Control, Stormwater Detention, Routing, and Spillways**

Carry forward the same FE workflow: sketch first, define units and sign conventions, choose the governing Handbook relation or learned workflow, solve, then perform an independent physical reasonableness check.

— Your Mentor
