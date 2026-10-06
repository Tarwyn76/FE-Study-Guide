---
chapter: "02-34"
title: "Work, Energy, and Power"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-034-01, MECH-2C-034-02, MECH-2C-034-03, MECH-2C-034-04, MECH-2C-034-05, MECH-2C-034-06, MECH-2C-034-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-34: Work, Energy, and Power

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-33 Particle Kinetics · 01-21 Integration

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly gives particle/rigid-body kinetic energy, gravitational and elastic potential energy, work, power, efficiency, conservation of energy, and elastic strain energy.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **34.1** Explain and apply **Work of a Force**.
* **34.2** Explain and apply **Kinetic Energy**.
* **34.3** Explain and apply **Gravitational Potential Energy**.
* **34.4** Explain and apply **Elastic Potential Energy**.
* **34.5** Explain and apply **Work-Energy Equation**.
* **34.6** Explain and apply **Power and Efficiency**.
* **34.7** Explain and apply **Elastic Strain Energy**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 34.1 Work of a Force

Work measures force acting through displacement. The Handbook defines

\[
U=\int \mathbf F\cdot d\mathbf r.
\]

Only the component of force along the differential displacement performs work. A force perpendicular to motion does no instantaneous work.

\[U_{1\to2}=\int_1^2\mathbf F\cdot d\mathbf r\]

![FIG-02-34-001: Force acting along curved displacement with dot-product projection.](../figures/FIG-02-34-001-work-of-a-force.png)

### Worked Example 1

**Problem.** A 50-N constant force acts through 4 m in its direction. Find work.

**Solution.** U=200 J.

---

## 34.2 Kinetic Energy

For a particle,

\[
T=rac12mv^2.
\]

Kinetic energy is scalar; direction of velocity does not appear directly. For rigid bodies, translational and rotational parts are added.

\[T_{\rm particle}=\tfrac12mv^2\]

![FIG-02-34-002: Moving particle with mass m and speed v connected to scalar kinetic energy.](../figures/FIG-02-34-002-kinetic-energy.png)

### Worked Example 2

**Problem.** A 2-kg particle moves at 5 m/s. Find kinetic energy.

**Solution.** T=0.5(2)(25)=25 J.

---

## 34.3 Gravitational Potential Energy

Near Earth's surface with constant \(g\), gravitational potential energy is \(V_g=mgh\) relative to a chosen datum.

Only changes in potential energy affect energy equations; the zero datum is arbitrary if used consistently.

\[V_g=mgh\]

![FIG-02-34-003: Mass at elevations h1 and h2 above an arbitrary datum.](../figures/FIG-02-34-003-gravitational-potential-energy.png)

### Worked Example 3

**Problem.** A 3-kg mass rises 2 m. Find ΔVg using g=9.81.

**Solution.** ΔV=3(9.81)(2)=58.86 J.

---

## 34.4 Elastic Potential Energy

A linear spring stores

\[
V_e=rac12ks^2
\]

relative to its undeformed length. Spring force is \(F_s=ks\), opposite the displacement from equilibrium when sign is included in the force law.

\[F_s=ks,\qquad V_e=\tfrac12ks^2\]

![FIG-02-34-004: Linear spring stretched from undeformed length with force-displacement graph and area as energy.](../figures/FIG-02-34-004-elastic-potential-energy.png)

### Worked Example 4

**Problem.** A spring k=400 N/m is compressed 0.10 m. Find stored energy.

**Solution.** V=0.5(400)(0.1²)=2 J.

---

## 34.5 Work-Energy Equation

For conservative systems, total kinetic plus potential energy is conserved. Nonconservative work is added explicitly.

This method often avoids solving for acceleration and time.

\[T_2+V_2=T_1+V_1+U_{1\to2}^{\rm nonconservative}\]

![FIG-02-34-005: Energy-state bars at positions 1 and 2 with nonconservative work transfer.](../figures/FIG-02-34-005-work-energy-equation.png)

### Worked Example 5

**Problem.** A force of 100 N acts on a point moving 3 m/s in same direction. Find power.

**Solution.** P=300 W.

---

## 34.6 Power and Efficiency

Power is the time rate of doing work. For a force acting at a point moving with velocity \(\mathbf v\),

\[
P=\mathbf F\cdot\mathbf v.
\]

For a rotating torque, \(P=T\omega\). Efficiency compares useful output to input.

\[P=\frac{dU}{dt}=\mathbf F\cdot\mathbf v,\qquad \eta=\frac{P_{\rm out}}{P_{\rm in}}\]

![FIG-02-34-006: Translational F·v and rotational Tω power examples with efficiency block.](../figures/FIG-02-34-006-power-and-efficiency.png)

### Worked Example 6

**Problem.** A shaft transmits 20 N·m at 100 rad/s. Find power.

**Solution.** P=Tω=2000 W.

---

## 34.7 Elastic Strain Energy

Within the linear elastic range, the Mechanics of Materials section gives strain energy for an axially loaded member.

This bridges dynamics energy methods to structural deformation.

\[U=\frac12P\delta,\qquad u=\frac{\sigma^2}{2E}\]

![FIG-02-34-007: Linear load-deformation graph with triangular area equal to elastic strain energy.](../figures/FIG-02-34-007-elastic-strain-energy.png)

### Worked Example 7

**Problem.** If input power is 5 kW and output is 4 kW, find efficiency.

**Solution.** η=0.80=80%.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** What sign does friction work usually have when it dissipates energy?

**Solution.** Negative.

### Worked Example 9

**Problem.** Why can energy methods avoid solving time?

**Solution.** They relate states through work and energy without requiring the detailed time history.

---

## As the Handbook States It

Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Dynamics, printed pp. 107–108; Mechanics of Materials p. 138**.

**Source boundary:** The Handbook directly gives particle/rigid-body kinetic energy, gravitational and elastic potential energy, work, power, efficiency, conservation of energy, and elastic strain energy.

---

## Where This Goes Wrong

**Applying work before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying kinetic energy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying gravitational potential energy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying elastic potential energy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying work-energy principle before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying power before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying strain energy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| work | Concept developed in §34.1; apply only under that section's model assumptions. |
| kinetic energy | Concept developed in §34.2; apply only under that section's model assumptions. |
| gravitational potential energy | Concept developed in §34.3; apply only under that section's model assumptions. |
| elastic potential energy | Concept developed in §34.4; apply only under that section's model assumptions. |
| work-energy principle | Concept developed in §34.5; apply only under that section's model assumptions. |
| power | Concept developed in §34.6; apply only under that section's model assumptions. |
| strain energy | Concept developed in §34.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **work** and state the governing relation or modeling rule.

2. Define **kinetic energy** and state the governing relation or modeling rule.

3. Define **gravitational potential energy** and state the governing relation or modeling rule.

4. Define **elastic potential energy** and state the governing relation or modeling rule.

5. Define **work-energy principle** and state the governing relation or modeling rule.

6. Define **power** and state the governing relation or modeling rule.

7. Define **strain energy** and state the governing relation or modeling rule.

8. What error is likely if **work** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **kinetic energy** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **gravitational potential energy** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **elastic potential energy** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **work-energy principle** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **power** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **strain energy** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **work**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **kinetic energy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **gravitational potential energy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **elastic potential energy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **work-energy principle**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **power**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **strain energy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **work**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **kinetic energy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **work** is developed in §34.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **kinetic energy** is developed in §34.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **gravitational potential energy** is developed in §34.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **elastic potential energy** is developed in §34.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **work-energy principle** is developed in §34.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **power** is developed in §34.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **strain energy** is developed in §34.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **work**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **kinetic energy**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **gravitational potential energy**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **elastic potential energy**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **work-energy principle**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **power**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **strain energy**.

15. Define the system and axes first, then use residual equilibrium, units, known limiting behavior, or constitutive/kinematic constraints to check the answer. Negative values often reverse an assumed vector sense when the physical model still permits that direction.

16. Define the system and axes first, then use residual equilibrium, units, known limiting behavior, or constitutive/kinematic constraints to check the answer. Negative values often reverse an assumed vector sense when the physical model still permits that direction.

17. Define the system and axes first, then use residual equilibrium, units, known limiting behavior, or constitutive/kinematic constraints to check the answer. Negative values often reverse an assumed vector sense when the physical model still permits that direction.

18. Define the system and axes first, then use residual equilibrium, units, known limiting behavior, or constitutive/kinematic constraints to check the answer. Negative values often reverse an assumed vector sense when the physical model still permits that direction.

19. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

20. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

21. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

22. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

23. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

24. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

25. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

26. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.

27. **A.** Mechanics relations are conditional on the selected body, coordinates, geometry, loading, and constitutive assumptions.


---

## Practice Problems

1. A 50-N constant force acts through 4 m in its direction. Find work.

2. A 2-kg particle moves at 5 m/s. Find kinetic energy.

3. A 3-kg mass rises 2 m. Find ΔVg using g=9.81.

4. A spring k=400 N/m is compressed 0.10 m. Find stored energy.

5. A force of 100 N acts on a point moving 3 m/s in same direction. Find power.

6. A shaft transmits 20 N·m at 100 rad/s. Find power.

7. If input power is 5 kW and output is 4 kW, find efficiency.

8. What sign does friction work usually have when it dissipates energy?

9. Why can energy methods avoid solving time?

10. For a linear elastic axial member reaching P=10 kN at δ=2 mm, find strain energy.


---

## Practice Problem Solutions

1. U=200 J.

2. T=0.5(2)(25)=25 J.

3. ΔV=3(9.81)(2)=58.86 J.

4. V=0.5(400)(0.1²)=2 J.

5. P=300 W.

6. P=Tω=2000 W.

7. η=0.80=80%.

8. Negative.

9. They relate states through work and energy without requiring the detailed time history.

10. U=0.5 Pδ=0.5(10000)(0.002)=10 J.


---

## Quick Reference

**Handbook anchor:** Dynamics, printed pp. 107–108; Mechanics of Materials p. 138.

- **work:** Work of a Force
- **kinetic energy:** Kinetic Energy
- **gravitational potential energy:** Gravitational Potential Energy
- **elastic potential energy:** Elastic Potential Energy
- **work-energy principle:** Work-Energy Equation
- **power:** Power and Efficiency
- **strain energy:** Elastic Strain Energy
---

## What's Next

**02-35 — Impulse, Momentum, and Impact**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor