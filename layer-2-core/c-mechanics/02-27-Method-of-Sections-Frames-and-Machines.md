---
chapter: "02-27"
title: "Method of Sections, Frames, and Machines"
layer: 2
tier: C
template: technical
ledger_ids: [MECH-2C-027-01, MECH-2C-027-02, MECH-2C-027-03, MECH-2C-027-04, MECH-2C-027-05, MECH-2C-027-06, MECH-2C-027-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 02-27: Method of Sections, Frames, and Machines

> *"In mechanics, the equation is usually the easy part. The model, sign convention, and free-body diagram decide whether the equation means anything."*

---

## Before You Start

**Prerequisites:** 02-24 Method of Joints · 02-26 Rigid-Body Equilibrium

**Skip if:** You can build the governing mechanics model, select the correct equations, solve representative FE-level problems, and independently check signs, units, and physical plausibility.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

The Handbook directly describes the truss method of sections and two-force bodies. Frame/machine member-isolation workflow is guide-developed statics application.

---

## Learning Objectives

By the end of this chapter, you will be able to:* **27.1** Explain and apply **Method of Sections — Why Cut the Truss**.
* **27.2** Explain and apply **Choosing the Cut and Moment Center**.
* **27.3** Explain and apply **Tension and Compression from a Section**.
* **27.4** Explain and apply **Frames versus Trusses**.
* **27.5** Explain and apply **Machines and Force Transmission**.
* **27.6** Explain and apply **Internal Pin Forces and Member Isolation**.
* **27.7** Explain and apply **Solution Order and Verification**.

---

## Notation Used Here

Use the sign convention and coordinate system stated in each section. Forces are vectors; moments/torques follow the selected positive rotational sense; SI units are used unless the problem states otherwise.

---

## 27.1 Method of Sections — Why Cut the Truss

The method of sections finds selected member forces without solving every joint. Cut through the truss to expose the desired members, isolate one side, and apply rigid-body equilibrium.

For a planar truss, choose a cut that passes through no more than three unknown member forces whenever possible.

\[\sum F_x=0,\quad\sum F_y=0,\quad\sum M_O=0\]

![FIG-02-27-001: Truss cut through three members with one side isolated as an FBD.](../figures/FIG-02-27-001-method-of-sections-why-cut-the-truss.png)

### Worked Example 1

**Problem.** A truss cut exposes three unknown members. How many planar equilibrium equations can the isolated section use?

**Solution.** Three. A planar rigid-body section has three independent equilibrium equations: ΣFx=0, ΣFy=0, and ΣM=0. A cut exposing at most three unknown member forces can therefore be solved directly when the equations are independent.

---

## 27.2 Choosing the Cut and Moment Center

A good cut exposes the target member and allows a moment center at the intersection of two other cut-member lines. Their moments vanish, leaving one unknown directly solvable.

If two cut members are parallel, choose equations that exploit their geometry rather than forcing a complicated simultaneous solution.

\[\sum M_P=0\Rightarrow \text{one cut-member force}\]

![FIG-02-27-002: Section with two cut-member lines intersecting at P, eliminating both from moment equation.](../figures/FIG-02-27-002-choosing-the-cut-and-moment-center.png)

### Worked Example 2

**Problem.** Why choose a moment center at the intersection of two cut-member lines?

**Solution.** Their moments vanish, allowing the third force to be solved directly. For a moment taken about the intersection of two unknown cut-member lines, those two forces have zero moment arms. The moment equation then contains the third cut force without the other two unknowns.

---

## 27.3 Tension and Compression from a Section

Assume cut-member forces act in tension, pulling away from the cut face. A positive solution confirms tension; a negative result indicates compression.

For the opposite isolated half, all exposed internal member-force arrows reverse by action-reaction.

\[F_{\rm assumed\ tension}<0\Rightarrow\text{compression}\]

![FIG-02-27-003: Opposite sides of same truss cut with equal-and-opposite exposed member forces.](../figures/FIG-02-27-003-tension-and-compression-from-a-section.png)

### Worked Example 3

**Problem.** A cut-member force assumed tensile solves negative. Interpret it.

**Solution.** Compression. Tension is commonly assumed by drawing the cut-member force away from the cut. A negative result reverses the assumed sense, so the actual member is in compression.

---

## 27.4 Frames versus Trusses

A frame contains members that may carry more than two forces and can transmit shear and moment through their connections. Truss members under the ideal model are two-force axial members.

Therefore a frame is solved by isolating individual members and applying rigid-body equilibrium, not by assuming every member force is axial.

\[\text{frame member: }\sum F_x=\sum F_y=\sum M=0\]

![FIG-02-27-004: Pin-jointed truss member versus multi-force frame member with several loads/reactions.](../figures/FIG-02-27-004-frames-versus-trusses.png)

### Worked Example 4

**Problem.** What distinguishes a frame member from an ideal truss member?

**Solution.** A frame member may be a multi-force member carrying shear and moment; an ideal truss member is axial two-force. An ideal truss member is a two-force member and carries only axial load. A frame member may have three or more forces and can therefore carry axial force, shear, and bending moment.

---

## 27.5 Machines and Force Transmission

A machine is an assembly designed to transmit or modify forces. Statics analysis often isolates each moving link at an instant when inertia is neglected or when a separate dynamics model is not required.

Pins transmit equal-and-opposite forces between connected members. Two-force links can simplify multi-member machine analysis significantly.

\[\mathbf F_{A\to B}=-\mathbf F_{B\to A}\]

![FIG-02-27-005: Simple lever-link machine with member-by-member FBDs and pin action-reaction forces.](../figures/FIG-02-27-005-machines-and-force-transmission.png)

### Worked Example 5

**Problem.** What force relation acts at an internal pin between two isolated members?

**Solution.** Equal and opposite pin-force components. The internal pin interaction forms a Newton's third-law pair. When the two connected members are isolated separately, the pin-force components on one member are equal in magnitude and opposite in direction to those on the other.

---

## 27.6 Internal Pin Forces and Member Isolation

When a frame or machine is separated at an internal pin, introduce two unknown pin-force components on one member and equal-and-opposite components on the connected member.

Do not also draw the internal pin force on a combined FBD that includes both members; it is internal to that larger system.

\[A_x,A_y\text{ on member 1}\leftrightarrow -A_x,-A_y\text{ on member 2}\]

![FIG-02-27-006: Two connected members separated at pin A with opposing Ax, Ay force components.](../figures/FIG-02-27-006-internal-pin-forces-and-member-isolation.png)

### Worked Example 6

**Problem.** Should an internal pin force be shown on an FBD of the entire assembly containing both connected members?

**Solution.** No; it is internal to that system. For an FBD of the entire assembly, forces at a connection between included members are internal and cancel as a pair. They appear only when the system is cut so that the connected members are analyzed separately.

---

## 27.7 Solution Order and Verification

Use the whole-assembly FBD for external reactions, then isolate members with the fewest unknowns. Recognize two-force members before adding unnecessary reaction components.

At the end, check each member independently and verify action-reaction consistency at every internal connection.

\[\sum\mathbf F=\mathbf0,\qquad\sum M=0\text{ for each isolated member}\]

![FIG-02-27-007: Frames/machines solution order: whole assembly -> reactions -> two-force members -> individual members -> pin-force checks.](../figures/FIG-02-27-007-solution-order-and-verification.png)

### Worked Example 7

**Problem.** What is the first useful analysis step for many frames/machines?

**Solution.** Whole-assembly FBD to find external support reactions. A whole-assembly FBD exposes the external loads and support reactions while internal pin forces cancel. Solving those external reactions first usually reduces the unknowns when individual members are then isolated.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** Why identify two-force members early?

**Solution.** Their force direction becomes known along the member axis, reducing unknown components. A two-force member has a known force line along its axis even when the magnitude is unknown. Recognizing it early converts two possible component unknowns into one scalar member force.

### Worked Example 9

**Problem.** What is a machine in statics context?

**Solution.** An assembly intended to transmit or modify forces; individual members are isolated and equilibrated. In statics, a machine is an assembly whose connected members transmit or modify forces. Analysis proceeds by isolating the entire assembly and then individual members so internal interaction forces can be solved.

---

## As the Handbook States It

### Source Boundary

- **FE-Handbook-supported** — For concepts marked `in_handbook` in the ledger, the cited FE Reference Handbook section/page supplies the formula, table, definition, or exam-scope anchor used by this chapter.
- **Externally supported** — Engineering LibreTexts, Mechanics Map (Moore, 2nd ed.) (https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_Map_%28Moore_2nd_Edition%29) supports method of sections, frames and machines, member isolation, pin forces, and solution order.
- **Guide synthesis** — Worked-example sequencing, engineering interpretation, exam strategy, comparison heuristics, checklists, and explanatory derivations beyond the cited source statements are instructional synthesis developed for this guide.


Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Principal source anchor: **Statics, printed p. 98**.

**Source boundary:** The Handbook directly describes the truss method of sections and two-force bodies. Frame/machine member-isolation workflow is guide-developed statics application.

---

## Where This Goes Wrong

**Applying method of sections before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying section-cut strategy before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying section force sign before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying frame before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying machine member before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying internal pin force before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Applying member-by-member equilibrium before the model is defined.** Establish the body/system, geometry, axes, sign convention, and applicable assumptions first.

**Treating a negative result as automatically wrong.** For an assumed vector direction, a negative value often means the actual direction is opposite; check whether the physical contact/member can support that sense.


---

## Key Terms

| Term | Working definition |
|---|---|
| method of sections | Concept developed in §27.1; apply only under that section's model assumptions. |
| section-cut strategy | Concept developed in §27.2; apply only under that section's model assumptions. |
| section force sign | Concept developed in §27.3; apply only under that section's model assumptions. |
| frame | Concept developed in §27.4; apply only under that section's model assumptions. |
| machine member | Concept developed in §27.5; apply only under that section's model assumptions. |
| internal pin force | Concept developed in §27.6; apply only under that section's model assumptions. |
| member-by-member equilibrium | Concept developed in §27.7; apply only under that section's model assumptions. |

---

## Review Questions

### Conceptual and Applied

1. Define **method of sections** and state the governing relation or modeling rule.

2. Define **section-cut strategy** and state the governing relation or modeling rule.

3. Define **section force sign** and state the governing relation or modeling rule.

4. Define **frame** and state the governing relation or modeling rule.

5. Define **machine member** and state the governing relation or modeling rule.

6. Define **internal pin force** and state the governing relation or modeling rule.

7. Define **member-by-member equilibrium** and state the governing relation or modeling rule.

8. What error is likely if **method of sections** is applied before the body, coordinate system, or sign convention is established?

9. What error is likely if **section-cut strategy** is applied before the body, coordinate system, or sign convention is established?

10. What error is likely if **section force sign** is applied before the body, coordinate system, or sign convention is established?

11. What error is likely if **frame** is applied before the body, coordinate system, or sign convention is established?

12. What error is likely if **machine member** is applied before the body, coordinate system, or sign convention is established?

13. What error is likely if **internal pin force** is applied before the body, coordinate system, or sign convention is established?

14. What error is likely if **member-by-member equilibrium** is applied before the body, coordinate system, or sign convention is established?

15. What diagram or state description should be created before solving a representative problem from this chapter?

16. Give one independent equilibrium, unit, limiting-case, or physical plausibility check.

17. When does a negative solved value simply reverse an assumed direction?

18. Why should the Handbook sign convention be checked before comparing formulas or diagrams?

### Multiple Choice

19. Which statement best describes **method of sections**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

20. Which statement best describes **section-cut strategy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

21. Which statement best describes **section force sign**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

22. Which statement best describes **frame**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

23. Which statement best describes **machine member**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

24. Which statement best describes **internal pin force**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

25. Which statement best describes **member-by-member equilibrium**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

26. Which statement best describes **method of sections**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model

27. Which statement best describes **section-cut strategy**?
A) It is applied only after the mechanics model and assumptions are defined
B) It is independent of geometry and sign convention
C) It is only a unit conversion
D) It replaces the need for an FBD or kinematic model


---

## Answer Key with Explanations

1. **method of sections** is developed in §27.1; use the displayed relation together with that section's geometry, sign convention, and assumptions.

2. **section-cut strategy** is developed in §27.2; use the displayed relation together with that section's geometry, sign convention, and assumptions.

3. **section force sign** is developed in §27.3; use the displayed relation together with that section's geometry, sign convention, and assumptions.

4. **frame** is developed in §27.4; use the displayed relation together with that section's geometry, sign convention, and assumptions.

5. **machine member** is developed in §27.5; use the displayed relation together with that section's geometry, sign convention, and assumptions.

6. **internal pin force** is developed in §27.6; use the displayed relation together with that section's geometry, sign convention, and assumptions.

7. **member-by-member equilibrium** is developed in §27.7; use the displayed relation together with that section's geometry, sign convention, and assumptions.

8. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **method of sections**.

9. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **section-cut strategy**.

10. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **section force sign**.

11. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **frame**.

12. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **machine member**.

13. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **internal pin force**.

14. The mechanics model can be wrong even if the algebra is correct. Establish the FBD/kinematics/stress state first, then apply **member-by-member equilibrium**.

15. Define the body or system, draw the chapter-specific model for **Chapter 02-27: Method of Sections, Frames, and Machines**, and label the coordinates, geometry, loads, and unknowns needed by the governing equations. This prevents algebra from being applied to an incomplete physical model.

16. Use an independent check appropriate to **Chapter 02-27: Method of Sections, Frames, and Machines**: substitute the solved values back into the governing equations, verify units and signs, and confirm that the result is physically plausible for the stated geometry and constraints.

17. A negative solved value reverses an assumed vector sense only when the underlying support, contact, or member can physically act in that opposite sense. In **Chapter 02-27: Method of Sections, Frames, and Machines**, also check whether a one-way constraint instead implies separation, slackness, or a changed contact state.

18. The Handbook and the chapter must use the same coordinate and sign convention before formulas or diagrams are compared. For **Chapter 02-27: Method of Sections, Frames, and Machines**, reversing an axis or moment sense changes component signs without changing the underlying mechanics.

19. **A.** The nineteenth review item tests **method of sections** in **Chapter 02-27: Method of Sections, Frames, and Machines**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

20. **A.** The twentieth review item tests **section-cut strategy** in **Chapter 02-27: Method of Sections, Frames, and Machines**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

21. **A.** The twenty-first review item tests **section force sign** in **Chapter 02-27: Method of Sections, Frames, and Machines**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

22. **A.** The twenty-second review item tests **frame** in **Chapter 02-27: Method of Sections, Frames, and Machines**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

23. **A.** The twenty-third review item tests **machine member** in **Chapter 02-27: Method of Sections, Frames, and Machines**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

24. **A.** The twenty-fourth review item tests **internal pin force** in **Chapter 02-27: Method of Sections, Frames, and Machines**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

25. **A.** The twenty-fifth review item tests **member-by-member equilibrium** in **Chapter 02-27: Method of Sections, Frames, and Machines**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention.

26. **A.** The twenty-sixth review item tests **method of sections** in **Chapter 02-27: Method of Sections, Frames, and Machines**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention. This application check also tests whether the model assumptions are established before any numerical or symbolic manipulation.

27. **A.** The twenty-seventh review item tests **section-cut strategy** in **Chapter 02-27: Method of Sections, Frames, and Machines**. The correct choice is the one consistent with the stated body/system, geometry, loading, constraints, and sign convention. This final application check emphasizes that a valid mechanics relation cannot replace the diagram, geometry, and constraints that define the problem.

---

## Practice Problems

1. A truss cut exposes three unknown members. How many planar equilibrium equations can the isolated section use?

2. Why choose a moment center at the intersection of two cut-member lines?

3. A cut-member force assumed tensile solves negative. Interpret it.

4. What distinguishes a frame member from an ideal truss member?

5. What force relation acts at an internal pin between two isolated members?

6. Should an internal pin force be shown on an FBD of the entire assembly containing both connected members?

7. What is the first useful analysis step for many frames/machines?

8. Why identify two-force members early?

9. What is a machine in statics context?

10. How is a section result checked?


---

## Practice Problem Solutions

1. Three. A planar rigid-body section has three independent equilibrium equations: ΣFx=0, ΣFy=0, and ΣM=0. A cut exposing at most three unknown member forces can therefore be solved directly when the equations are independent. Practice check: this conclusion follows from the governing model used in **Chapter 02-27: Method of Sections, Frames, and Machines**; verify the assumed direction/sign and confirm the result satisfies the relevant equilibrium or compatibility condition.
2. Their moments vanish, allowing the third force to be solved directly. For a moment taken about the intersection of two unknown cut-member lines, those two forces have zero moment arms. The moment equation then contains the third cut force without the other two unknowns. Practice check: this conclusion follows from the governing model used in **Chapter 02-27: Method of Sections, Frames, and Machines**; verify the assumed direction/sign and confirm the result satisfies the relevant equilibrium or compatibility condition.
3. Compression. Tension is commonly assumed by drawing the cut-member force away from the cut. A negative result reverses the assumed sense, so the actual member is in compression. Practice check: this conclusion follows from the governing model used in **Chapter 02-27: Method of Sections, Frames, and Machines**; verify the assumed direction/sign and confirm the result satisfies the relevant equilibrium or compatibility condition.
4. A frame member may be a multi-force member carrying shear and moment; an ideal truss member is axial two-force. An ideal truss member is a two-force member and carries only axial load. A frame member may have three or more forces and can therefore carry axial force, shear, and bending moment. Practice check: this conclusion follows from the governing model used in **Chapter 02-27: Method of Sections, Frames, and Machines**; verify the assumed direction/sign and confirm the result satisfies the relevant equilibrium or compatibility condition.
5. Equal and opposite pin-force components. The internal pin interaction forms a Newton's third-law pair. When the two connected members are isolated separately, the pin-force components on one member are equal in magnitude and opposite in direction to those on the other. Practice check: this conclusion follows from the governing model used in **Chapter 02-27: Method of Sections, Frames, and Machines**; verify the assumed direction/sign and confirm the result satisfies the relevant equilibrium or compatibility condition.
6. No; it is internal to that system. For an FBD of the entire assembly, forces at a connection between included members are internal and cancel as a pair. They appear only when the system is cut so that the connected members are analyzed separately. Practice check: this conclusion follows from the governing model used in **Chapter 02-27: Method of Sections, Frames, and Machines**; verify the assumed direction/sign and confirm the result satisfies the relevant equilibrium or compatibility condition.
7. Whole-assembly FBD to find external support reactions. A whole-assembly FBD exposes the external loads and support reactions while internal pin forces cancel. Solving those external reactions first usually reduces the unknowns when individual members are then isolated. Practice check: this conclusion follows from the governing model used in **Chapter 02-27: Method of Sections, Frames, and Machines**; verify the assumed direction/sign and confirm the result satisfies the relevant equilibrium or compatibility condition.
8. Their force direction becomes known along the member axis, reducing unknown components. A two-force member has a known force line along its axis even when the magnitude is unknown. Recognizing it early converts two possible component unknowns into one scalar member force. Practice check: this conclusion follows from the governing model used in **Chapter 02-27: Method of Sections, Frames, and Machines**; verify the assumed direction/sign and confirm the result satisfies the relevant equilibrium or compatibility condition.
9. An assembly intended to transmit or modify forces; individual members are isolated and equilibrated. In statics, a machine is an assembly whose connected members transmit or modify forces. Analysis proceeds by isolating the entire assembly and then individual members so internal interaction forces can be solved. Practice check: this conclusion follows from the governing model used in **Chapter 02-27: Method of Sections, Frames, and Machines**; verify the assumed direction/sign and confirm the result satisfies the relevant equilibrium or compatibility condition.
10. Verify equilibrium of the isolated section and consistency with the opposite side/action-reaction.

---

## Quick Reference

**Handbook anchor:** Statics, printed p. 98.

- **method of sections:** Method of Sections — Why Cut the Truss
- **section-cut strategy:** Choosing the Cut and Moment Center
- **section force sign:** Tension and Compression from a Section
- **frame:** Frames versus Trusses
- **machine member:** Machines and Force Transmission
- **internal pin force:** Internal Pin Forces and Member Isolation
- **member-by-member equilibrium:** Solution Order and Verification
---

## What's Next

**02-28 — Distributed Loads, Centroids, and Centers of Gravity**

Carry forward the mechanics workflow: isolate the system, draw the model, choose coordinates/signs, write the governing equations, solve, then verify the physical result.

— Your Mentor