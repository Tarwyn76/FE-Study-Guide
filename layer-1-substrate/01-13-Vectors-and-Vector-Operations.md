---
chapter: "01-13"
title: "Vectors and Vector Operations"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-013-01, MATH-1B-013-02, MATH-1B-013-03, MATH-1B-013-04]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-13: Vectors and Vector Operations

> *"A scalar tells you how much. A vector tells you how much and which way.
> Force is a vector. Velocity is a vector. Every time you decompose a load,
> find a resultant, or compute a torque, you are doing vector algebra. The
> notation makes it systematic. The cross product makes it three-dimensional.
> Together they handle everything mechanics can throw at you."*

---

## Before You Start

**Prerequisites:** [01-09 Analytic Geometry](01-09-analytic-geometry.md) · [01-11 Trigonometry](01-11-trigonometry.md) · [01-12 Complex Numbers](01-12-complex-numbers.md)

**Skip if:** You pass the Tier 1B test-out quiz. Verify you can compute dot
products, cross products, and unit vectors in 3D before skipping — 3D cross
products are the place most people have rust.

**Time:** ~60 min read · ~25 min review questions · ~60 min practice problems

---

## On the Board Today

Apprentice, you've been doing two-dimensional vector work since Chapter
01-11: decomposing forces into components, finding resultants. This chapter
formalizes that work and extends it into three dimensions.

Two operations are central.

The **dot product** tells you about parallelism. It gives you the projection
of one vector onto another — how much of the first vector acts in the
direction of the second. This is how you find the component of a force along
an inclined surface, the work done by a force, and whether two vectors are
perpendicular.

The **cross product** tells you about perpendicularity. It gives you a new
vector perpendicular to both inputs, with magnitude equal to the area of the
parallelogram they span. This is how you calculate moments (torques), find a
normal to a surface, and determine the direction of a magnetic force on a
current-carrying conductor.

These two products appear in virtually every Tier 2C problem involving forces
and moments. Get them automatic here and Tier 2C becomes about physics, not
computation.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 13.1 Distinguish scalar and vector quantities and represent vectors in
  component form
* 13.2 Add and subtract vectors geometrically and algebraically
* 13.3 Find the magnitude of a vector and compute a unit vector
* 13.4 Resolve a vector into rectangular components in 2D and 3D
* 13.5 Compute the dot product and use it to find the angle between vectors
  and projections
* 13.6 Test vectors for perpendicularity and parallelism using the dot product
* 13.7 Compute the cross product using the determinant method
* 13.8 Use the cross product to find a moment and a unit normal
* 13.9 Apply the scalar and vector triple products

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $\vec{A}$, $\mathbf{A}$ | vector $A$ | both notations used; bold preferred in display |
| $\lvert\vec{A}\rvert$ or $A$ | magnitude of $\vec{A}$ | scalar, always $\ge 0$ |
| $\hat{A}$ | unit vector in direction of $\vec{A}$ | $\lvert\hat{A}\rvert = 1$ |
| $\hat{\imath}$, $\hat{\jmath}$, $\hat{k}$ | unit vectors along $x$, $y$, $z$ axes | right-hand coordinate system |
| $A_x, A_y, A_z$ | scalar components of $\vec{A}$ | may be negative |
| $\vec{A} \cdot \vec{B}$ | dot product | result is a scalar |
| $\vec{A} \times \vec{B}$ | cross product | result is a vector |

> ---
> **Mentor's Margin**
>
> Two notation systems for vectors exist side by side in engineering:
> arrow notation ($\vec{A}$) and bold notation (**A**). This guide uses
> arrows in prose and bold in display equations, matching the Handbook's
> practice. Some instructors and texts use only bold; some use only arrows.
> Both mean the same thing. The magnitude is always the plain letter without
> decoration: $A = \lvert\vec{A}\rvert$.
>
> ---

---

## 13.1 Scalars and Vectors

A **scalar** is a quantity fully described by a single number and a unit.
Mass, temperature, time, energy, speed.

A **vector** is a quantity that requires both a magnitude and a direction.
Force, displacement, velocity, acceleration, moment.

Geometrically, a vector is an arrow: length proportional to magnitude,
pointing in the specified direction.

Algebraically, a vector is represented by its **components**: the projections
onto the coordinate axes.

$$\vec{A} = A_x\hat{\imath} + A_y\hat{\jmath} + A_z\hat{k}$$

where $\hat{\imath}$, $\hat{\jmath}$, $\hat{k}$ are unit vectors along the
positive $x$, $y$, $z$ axes.

![FIG-01-13-001: 3D coordinate system showing a vector A decomposed into components Ax, Ay, Az along the x, y, z axes, with unit vectors i-hat, j-hat, k-hat labeled and the right-hand rule orientation shown](../figures/FIG-01-13-001-vector-components-3d.png)

---

## 13.2 Vector Addition and Subtraction

**Geometrically:** place the tail of the second vector at the tip of the
first. The resultant runs from the tail of the first to the tip of the
second. This is the **tip-to-tail rule** (also called the parallelogram law
when applied to vectors sharing a tail).

**Algebraically:** add or subtract corresponding components.

$$\vec{A} + \vec{B} = (A_x+B_x)\hat{\imath} + (A_y+B_y)\hat{\jmath} + (A_z+B_z)\hat{k}$$

$$\vec{A} - \vec{B} = (A_x-B_x)\hat{\imath} + (A_y-B_y)\hat{\jmath} + (A_z-B_z)\hat{k}$$

**Scalar multiplication:** scales the magnitude, reverses direction if
negative.

$$c\vec{A} = cA_x\hat{\imath} + cA_y\hat{\jmath} + cA_z\hat{k}$$

![FIG-01-13-002: Vector addition diagram showing two methods: tip-to-tail on the left, and parallelogram method on the right, both producing the same resultant vector](../figures/FIG-01-13-002-vector-addition.png)

---

## 13.3 Magnitude and Unit Vectors

**Magnitude:**

$$\boxed{\lvert\vec{A}\rvert = \sqrt{A_x^2 + A_y^2 + A_z^2}}$$

This is the Pythagorean theorem extended to 3D — the same formula as the
3D distance from Chapter 01-09.

**Unit vector** in the direction of $\vec{A}$:

$$\boxed{\hat{A} = \frac{\vec{A}}{\lvert\vec{A}\rvert} = \frac{A_x\hat{\imath} + A_y\hat{\jmath} + A_z\hat{k}}{\sqrt{A_x^2+A_y^2+A_z^2}}}$$

A unit vector has magnitude exactly 1. It carries direction only, with no
magnitude information. Multiplying a unit vector by a scalar gives a vector
with that scalar as its magnitude in the unit vector's direction.

**Direction cosines:** for a vector in 3D, the angles it makes with each
axis:

$$\cos\alpha = \frac{A_x}{A} \qquad \cos\beta = \frac{A_y}{A} \qquad \cos\gamma = \frac{A_z}{A}$$

where $\alpha$, $\beta$, $\gamma$ are the angles with the $x$, $y$, $z$
axes respectively.

$$\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$$

This is the 3D analogue of $\sin^2\theta + \cos^2\theta = 1$.

### Worked Example 1 — Magnitude, Unit Vector, Direction Cosines

**Given.** $\vec{F} = 3\hat{\imath} - 4\hat{\jmath} + 12\hat{k}$ kN.

**(a)** Find the magnitude.
**(b)** Find the unit vector.
**(c)** Find the direction cosines and verify.

**Solution.**

(a) $F = \sqrt{9 + 16 + 144} = \sqrt{169} = \boxed{13 \text{ kN}}$

(b) $\hat{F} = \dfrac{3\hat{\imath} - 4\hat{\jmath} + 12\hat{k}}{13} =
\boxed{\tfrac{3}{13}\hat{\imath} - \tfrac{4}{13}\hat{\jmath} + \tfrac{12}{13}\hat{k}}$

(c) $\cos\alpha = 3/13$, $\cos\beta = -4/13$, $\cos\gamma = 12/13$

Verify: $(3/13)^2 + (-4/13)^2 + (12/13)^2 = (9+16+144)/169 = 169/169 = 1$ ✓

---

## 13.4 The Dot Product

The **dot product** (scalar product) of two vectors:

$$\boxed{\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z}$$

The result is a **scalar** — not a vector.

Geometric interpretation:

$$\boxed{\vec{A} \cdot \vec{B} = \lvert\vec{A}\rvert\lvert\vec{B}\rvert\cos\theta}$$

where $\theta$ is the angle between the vectors $(0 \le \theta \le 180°)$.

![FIG-01-13-003: Dot product geometry showing two vectors A and B with the angle theta between them, and the projection of B onto A labeled as |B|cos(theta)](../figures/FIG-01-13-003-dot-product-geometry.png)

### Applications of the dot product

**Angle between vectors:**

$$\cos\theta = \frac{\vec{A}\cdot\vec{B}}{\lvert\vec{A}\rvert\lvert\vec{B}\rvert}$$

**Perpendicularity test:** if $\vec{A} \cdot \vec{B} = 0$ and neither is the
zero vector, then $\vec{A} \perp \vec{B}$ (since $\cos 90° = 0$).

**Parallelism test:** if $\vec{A} \times \vec{B} = \vec{0}$, then $\vec{A}
\parallel \vec{B}$. Equivalently, the dot product equals $\pm AB$ (since
$\cos 0° = 1$ and $\cos 180° = -1$).

**Projection of $\vec{B}$ onto $\vec{A}$** (scalar projection):

$$\text{comp}_{\vec{A}}\vec{B} = \frac{\vec{A}\cdot\vec{B}}{\lvert\vec{A}\rvert} = \lvert\vec{B}\rvert\cos\theta$$

**Vector projection of $\vec{B}$ onto $\vec{A}$:**

$$\text{proj}_{\vec{A}}\vec{B} = \left(\frac{\vec{A}\cdot\vec{B}}{\lvert\vec{A}\rvert^2}\right)\vec{A} = (\vec{B}\cdot\hat{A})\hat{A}$$

> ---
> **Mentor's Margin**
>
> The projection formula is the one that matters most in mechanics. The
> component of a force along a ramp is the scalar projection of the force
> vector onto the unit vector along the ramp. The work done by a force over
> a displacement is $W = \vec{F}\cdot\vec{d}$ — the dot product — because
> only the component of force along the displacement does work. Know this
> connection and the dot product stops being abstract.
>
> ---

### Worked Example 2 — Dot Product and Angle

**Given.** $\vec{A} = 2\hat{\imath} - \hat{\jmath} + 3\hat{k}$ and
$\vec{B} = -\hat{\imath} + 4\hat{\jmath} + 2\hat{k}$.

**(a)** Compute $\vec{A}\cdot\vec{B}$.
**(b)** Find the angle between them.
**(c)** Find the scalar projection of $\vec{B}$ onto $\vec{A}$.

**Solution.**

(a) $\vec{A}\cdot\vec{B} = (2)(-1) + (-1)(4) + (3)(2) = -2 - 4 + 6 =
\boxed{0}$

(b) $\vec{A}\cdot\vec{B} = 0$ with neither being the zero vector, so:

$$\theta = 90° \qquad \vec{A} \perp \vec{B} \;\checkmark$$

(c) Scalar projection of $\vec{B}$ onto $\vec{A}$:

$A = \sqrt{4+1+9} = \sqrt{14}$

$\text{comp}_{\vec{A}}\vec{B} = \frac{0}{\sqrt{14}} = 0$

This makes sense: if $\vec{B}$ is perpendicular to $\vec{A}$, it has zero
component along $\vec{A}$.

### Worked Example 3 — Work Done by a Force

**Given.** A force $\vec{F} = (5\hat{\imath} + 3\hat{\jmath} - 2\hat{k})$ kN
acts on an object. The object moves along displacement $\vec{d} = (4\hat{\imath}
- \hat{\jmath} + 6\hat{k})$ m.

**Find.** The work done by $\vec{F}$.

**Solution.**

$$W = \vec{F}\cdot\vec{d} = (5)(4) + (3)(-1) + (-2)(6) = 20 - 3 - 12 = \boxed{5 \text{ kN·m} = 5 \text{ kJ}}$$

**Check.** Units: kN × m = kJ ✓. The work is positive, meaning $\vec{F}$
has a net component in the direction of motion.

---

## 13.5 The Cross Product

The **cross product** (vector product) of two vectors:

$$\vec{A} \times \vec{B} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix}$$

Expanding the determinant:

$$\boxed{\vec{A} \times \vec{B} = (A_yB_z - A_zB_y)\hat{\imath} - (A_xB_z - A_zB_x)\hat{\jmath} + (A_xB_y - A_yB_x)\hat{k}}$$

The result is a **vector** — perpendicular to both $\vec{A}$ and $\vec{B}$.

![FIG-01-13-004: Cross product illustration showing vectors A and B in a plane, the resulting cross product vector A×B perpendicular to that plane, the right-hand rule hand gesture, and the parallelogram with area |A||B|sin(theta)](../figures/FIG-01-13-004-cross-product-geometry.png)

### Geometric interpretation

$$\lvert\vec{A}\times\vec{B}\rvert = \lvert\vec{A}\rvert\lvert\vec{B}\rvert\sin\theta$$

The magnitude equals the area of the parallelogram formed by $\vec{A}$ and
$\vec{B}$. The direction is perpendicular to both, determined by the
**right-hand rule**: curl the fingers of the right hand from $\vec{A}$ toward
$\vec{B}$; the thumb points in the direction of $\vec{A}\times\vec{B}$.

### Key properties

$$\vec{A}\times\vec{B} = -(\vec{B}\times\vec{A}) \quad \text{(anti-commutative)}$$

$$\vec{A}\times\vec{A} = \vec{0} \quad \text{(zero for parallel vectors, since }\sin 0° = 0)$$

$$\hat{\imath}\times\hat{\jmath} = \hat{k} \qquad \hat{\jmath}\times\hat{k} = \hat{\imath} \qquad \hat{k}\times\hat{\imath} = \hat{\jmath}$$

(Cyclic: $i \to j \to k \to i$ is positive. Reverse direction is negative.)

> ---
> **Mentor's Margin**
>
> The determinant expansion is the systematic method. Write the $3 \times 3$
> determinant with the unit vectors in the top row, $\vec{A}$ in the second
> row, $\vec{B}$ in the third. Expand along the top row. The middle term has
> a minus sign — that's the determinant cofactor sign for the center element.
> If you skip that minus sign, your $\hat{\jmath}$ component will have the
> wrong sign. Write it out explicitly every time until it's automatic.
>
> ---

### Worked Example 4 — Moment of a Force

**Given.** A force $\vec{F} = (0\hat{\imath} - 5\hat{\jmath} + 0\hat{k})$ kN
acts at point $(3, 0, 4)$ m from the origin.

**Find.** The moment $\vec{M}$ about the origin.

**Approach.** The moment of a force about a point is $\vec{M} = \vec{r}
\times \vec{F}$, where $\vec{r}$ is the position vector from the moment
point to the force application point.

**Solution.**

$$\vec{r} = 3\hat{\imath} + 0\hat{\jmath} + 4\hat{k}$$

$$\vec{M} = \vec{r}\times\vec{F} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 3 & 0 & 4 \\ 0 & -5 & 0 \end{vmatrix}$$

Expand:

$\hat{\imath}$: $(0)(0) - (4)(-5) = 0 + 20 = 20$

$\hat{\jmath}$: $-[(3)(0) - (4)(0)] = -[0-0] = 0$

$\hat{k}$: $(3)(-5) - (0)(0) = -15$

$$\vec{M} = 20\hat{\imath} + 0\hat{\jmath} - 15\hat{k} = \boxed{(20\hat{\imath} - 15\hat{k}) \text{ kN·m}}$$

Magnitude: $M = \sqrt{400+225} = \sqrt{625} = 25$ kN·m

**Check.** For a purely downward force ($-y$ direction) applied at a point
in the $xz$-plane, the moment should have no $\hat{\jmath}$ component —
it should lie in the $xz$-plane. ✓

Also verify with magnitude formula: $M = rF\sin\theta$ where $r = \lvert
\vec{r}\rvert = \sqrt{9+0+16} = 5$ m, $F = 5$ kN, and $\theta$ is the angle
between $\vec{r}$ and $\vec{F}$.

$\vec{r}\cdot\vec{F} = (3)(0)+(0)(-5)+(4)(0) = 0$, so $\theta = 90°$,
$\sin\theta = 1$.

$M = 5 \times 5 \times 1 = 25$ kN·m ✓

---

## 13.6 Triple Products

### Scalar triple product

$$\vec{A}\cdot(\vec{B}\times\vec{C}) = \begin{vmatrix} A_x & A_y & A_z \\ B_x & B_y & B_z \\ C_x & C_y & C_z \end{vmatrix}$$

The result is a scalar. Its absolute value equals the volume of the
parallelepiped (3D parallelogram-box) formed by the three vectors.

If the scalar triple product is zero, the three vectors are **coplanar**
(all lie in the same plane).

### Vector triple product

$$\vec{A}\times(\vec{B}\times\vec{C}) = \vec{B}(\vec{A}\cdot\vec{C}) - \vec{C}(\vec{A}\cdot\vec{B})$$

This is the "BAC-CAB" rule. Useful in deriving electromagnetic and fluid
mechanics relations; the FE rarely requires direct computation of this.

---

## 13.7 Vectors in 2D — Connection to Previous Chapters

In two dimensions, $\vec{A} = A_x\hat{\imath} + A_y\hat{\jmath}$.

This is identical to the complex number $A_x + jA_y$. The magnitude is the
modulus; the angle from the positive $x$-axis is the argument.

The force decomposition from Chapter 01-11 is vector addition:

$$\vec{R} = \sum_i \vec{F}_i = \left(\sum_i F_{ix}\right)\hat{\imath} + \left(\sum_i F_{iy}\right)\hat{\jmath}$$

Every force problem you solved in Chapter 01-11 was vector addition in
component form. This chapter simply names it and extends it to 3D with the
additional operations.

---

## As the Handbook States It

> **Handbook 10.6, pp. 37–38** — *Mathematics / Vectors*

The Handbook includes:

- Component form $A_x\hat{\imath} + A_y\hat{\jmath} + A_z\hat{k}$
- Magnitude formula
- Unit vector formula
- Dot product: both component and geometric forms
- Angle between vectors formula
- Cross product: both determinant and geometric forms
- Right-hand rule description
- Scalar triple product

**What's not in the Handbook — memorize:**

- The cyclic unit vector cross products: $\hat{\imath}\times\hat{\jmath} =
  \hat{k}$, etc.
- Direction cosine relation $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$
- The moment formula $\vec{M} = \vec{r}\times\vec{F}$
- How to interpret the dot product as work or projection
- The scalar triple product as coplanarity test

---

## Where This Goes Wrong

**Cross product sign error on the $\hat{\jmath}$ term.** The middle element
of a 3×3 determinant expansion carries a minus sign. Writing the cross product
determinant and forgetting the $-\hat{\jmath}$ sign is the single most common
vector error.

**Cross product direction (non-commutativity).** $\vec{A}\times\vec{B} =
-(\vec{B}\times\vec{A})$. Order matters. Reversing the order reverses the
direction of the result. In moment calculations, always use $\vec{r}\times
\vec{F}$, not $\vec{F}\times\vec{r}$.

**Confusing dot and cross product.** Dot product: scalar, measures
parallelism. Cross product: vector, measures perpendicularity. They are not
interchangeable.

**Magnitude of a cross product vs the cross product itself.** The formula
$\lvert\vec{A}\times\vec{B}\rvert = AB\sin\theta$ gives the *magnitude*, not
the vector. Computing the magnitude without computing the direction loses the
orientation information needed for moment direction.

**Unit vector computation with the wrong magnitude.** Dividing by the wrong
value (e.g., one component instead of the full magnitude) produces a vector
that isn't actually a unit vector. Always verify: $\lvert\hat{A}\rvert = 1$
after computing.

**2D problems with a $z$-component sneaking in.** If $\vec{F}$ and $\vec{r}$
are both in the $xy$-plane ($z=0$), the cross product moment has only a
$\hat{k}$ component. That is correct and expected — moments about an in-plane
axis point out of plane.

---

## Key Terms

| Term | Definition |
|---|---|
| Scalar | A quantity described by magnitude only |
| Vector | A quantity described by both magnitude and direction |
| Component | Projection of a vector onto a coordinate axis; a scalar |
| Unit vector $\hat{A}$ | A vector with magnitude exactly 1; carries direction only |
| Direction cosines | Cosines of the angles a vector makes with the coordinate axes |
| Dot product | $\vec{A}\cdot\vec{B} = AB\cos\theta$; scalar result; measures parallelism |
| Cross product | $\vec{A}\times\vec{B}$; vector result perpendicular to both; magnitude $AB\sin\theta$ |
| Right-hand rule | Convention for cross product direction: curl fingers from $\vec{A}$ to $\vec{B}$, thumb points in $\vec{A}\times\vec{B}$ direction |
| Scalar projection | Component of $\vec{B}$ along $\vec{A}$: $\vec{A}\cdot\vec{B}/\lvert\vec{A}\rvert$ |
| Vector projection | Component of $\vec{B}$ along $\vec{A}$ expressed as a vector |
| Moment (torque) | $\vec{M} = \vec{r}\times\vec{F}$; a cross product; units N·m or ft·lbf |
| Scalar triple product | $\vec{A}\cdot(\vec{B}\times\vec{C})$; scalar equal to parallelepiped volume; zero if coplanar |
| Coplanar | Three vectors lying in the same plane; their scalar triple product is zero |

---

## Review Questions

### Conceptual

1. What is the fundamental difference between a scalar and a vector? Give
   two examples of each from engineering.
2. Explain what a unit vector is and why it's useful in force analysis.
3. The dot product of two vectors equals zero. What does this tell you about
   their geometric relationship?
4. Explain why $\vec{A}\times\vec{B} = -\vec{B}\times\vec{A}$. What
   physically changes when you reverse the order?
5. In the moment formula $\vec{M} = \vec{r}\times\vec{F}$, what does $\vec{r}$
   represent, and why does the cross product give the moment?
6. The scalar triple product of three vectors equals zero. What does this
   mean geometrically?

### Calculation

7. For $\vec{A} = 4\hat{\imath} - 3\hat{\jmath} + 0\hat{k}$ and
   $\vec{B} = -\hat{\imath} + 2\hat{\jmath} + 5\hat{k}$:
   (a) $\vec{A} + \vec{B}$
   (b) $3\vec{A} - 2\vec{B}$
   (c) $\lvert\vec{A}\rvert$ and $\lvert\vec{B}\rvert$
   (d) Unit vector $\hat{A}$

8. Find the direction cosines of $\vec{F} = 6\hat{\imath} - 2\hat{\jmath}
   + 9\hat{k}$ kN and verify they satisfy the direction cosine identity.

9. Compute the dot product and find the angle between:
   (a) $\vec{A} = 2\hat{\imath} + 3\hat{\jmath}$ and
       $\vec{B} = -3\hat{\imath} + 2\hat{\jmath}$
   (b) $\vec{A} = \hat{\imath} + \hat{\jmath} + \hat{k}$ and
       $\vec{B} = 2\hat{\imath} - \hat{\jmath} + 3\hat{k}$

10. Find the scalar and vector projections of $\vec{B}$ onto $\vec{A}$:
    $\vec{A} = 3\hat{\imath} + 4\hat{\jmath}$, $\vec{B} = 5\hat{\imath}
    + 0\hat{\jmath}$

11. Compute the cross products:
    (a) $\vec{A} = 2\hat{\imath} + \hat{\jmath} - \hat{k}$ and
        $\vec{B} = \hat{\imath} - 2\hat{\jmath} + 3\hat{k}$
    (b) $\vec{A} = 3\hat{\imath} + 0\hat{\jmath} + 0\hat{k}$ and
        $\vec{B} = 0\hat{\imath} + 4\hat{\jmath} + 0\hat{k}$
    (c) Verify (b) using the unit vector cyclic rule.

12. **Engineering.** A force $\vec{F} = (8\hat{\imath} - 6\hat{\jmath}
    + 0\hat{k})$ kN is applied at position $\vec{r} = (2\hat{\imath} +
    3\hat{\jmath} + 0\hat{k})$ m from the origin.
    (a) Find the moment vector $\vec{M} = \vec{r}\times\vec{F}$.
    (b) Find the magnitude of the moment.
    (c) What direction does the moment vector point, and what does that mean
    physically?

13. **Engineering.** Three concurrent forces act at a joint:
    $\vec{F}_1 = (10\hat{\imath} + 0\hat{\jmath} + 0\hat{k})$ kN,
    $\vec{F}_2 = (-4\hat{\imath} + 8\hat{\jmath} + 2\hat{k})$ kN,
    $\vec{F}_3 = (-6\hat{\imath} - 8\hat{\jmath} + 0\hat{k})$ kN.
    (a) Find the resultant force vector.
    (b) Find its magnitude and direction.
    (c) Is the system in equilibrium? Justify.

14. **Engineering.** A cable runs from point $A(0, 0, 0)$ to point
    $B(4, 3, 12)$ m and carries a tension of $260$ N.
    (a) Find the unit vector along the cable from $A$ to $B$.
    (b) Write the force vector in component form.
    (c) Find the component of this force along the direction
    $\hat{u} = (1/\sqrt{2})\hat{\imath} + (1/\sqrt{2})\hat{\jmath}$.

### Multiple Choice

15. The dot product $\vec{A}\cdot\vec{B}$ is zero when:
    A) $\lvert\vec{A}\rvert = \lvert\vec{B}\rvert$
    B) $\vec{A}$ and $\vec{B}$ are parallel
    C) $\vec{A}$ and $\vec{B}$ are perpendicular
    D) $\vec{A}$ and $\vec{B}$ point in opposite directions

16. $\hat{\jmath}\times\hat{k}$ equals:
    A) $\hat{\imath}$
    B) $-\hat{\imath}$
    C) $\hat{k}$
    D) $-\hat{k}$

17. The magnitude of $\vec{A}\times\vec{B}$ equals:
    A) $AB\cos\theta$
    B) $AB\sin\theta$
    C) $\vec{A}\cdot\vec{B}$
    D) $\lvert\vec{A}\rvert + \lvert\vec{B}\rvert$

18. The cross product $\vec{A}\times\vec{A}$ equals:
    A) $\lvert\vec{A}\rvert^2$
    B) $\lvert\vec{A}\rvert^2\hat{A}$
    C) $1$
    D) $\vec{0}$

19. The work done by force $\vec{F}$ over displacement $\vec{d}$ is:
    A) $\vec{F}\times\vec{d}$
    B) $\vec{F}\cdot\vec{d}$
    C) $\lvert\vec{F}\rvert\lvert\vec{d}\rvert$
    D) $\lvert\vec{F}\times\vec{d}\rvert$

20. A unit vector in the direction of $\vec{A} = 3\hat{\imath} + 4\hat{\jmath}$
    is:
    A) $3\hat{\imath} + 4\hat{\jmath}$
    B) $\tfrac{3}{5}\hat{\imath} + \tfrac{4}{5}\hat{\jmath}$
    C) $\tfrac{1}{3}\hat{\imath} + \tfrac{1}{4}\hat{\jmath}$
    D) $\tfrac{3}{7}\hat{\imath} + \tfrac{4}{7}\hat{\jmath}$

---

## Answer Key with Explanations

**1.** A scalar has only magnitude: temperature (25°C), mass (50 kg), time
(3 s), energy (100 J). A vector has magnitude and direction: force (500 N
upward), velocity (30 m/s east), moment (200 N·m counterclockwise about the
$z$-axis), displacement (5 m at 30° from horizontal). The key test: does it
make physical sense to ask "in which direction?" If yes, it's a vector. (§13.1)

**2.** A unit vector has magnitude exactly 1 and carries direction only. It's
useful for two reasons: (1) multiplying a unit vector by a scalar gives a
vector with that scalar as the magnitude in the unit vector's direction —
useful for writing a force once its direction is known; (2) the dot product
of any vector with a unit vector gives the scalar projection of that vector
along the unit direction. (§13.3)

**3.** Two non-zero vectors with zero dot product are perpendicular
($\theta = 90°$, since $\cos 90° = 0$). If either vector is the zero vector,
no geometric conclusion follows. (§13.4)

**4.** $\vec{A}\times\vec{B} = -\vec{B}\times\vec{A}$ because the cross
product obeys the right-hand rule: curl from first to second vector. Reversing
the order reverses the direction of the curl, which reverses the thumb
direction, giving the opposite vector. Physically: if $\vec{A}\times\vec{B}$
points out of the page, then $\vec{B}\times\vec{A}$ points into it. In moment
calculations, this means the sign (clockwise vs counterclockwise) of the
moment depends on using $\vec{r}\times\vec{F}$ consistently, not
$\vec{F}\times\vec{r}$. (§13.5)

**5.** $\vec{r}$ is the position vector from the reference point (about which
you're taking the moment) to the point where the force is applied. The cross
product gives a vector perpendicular to both $\vec{r}$ and $\vec{F}$, whose
magnitude $rF\sin\theta$ equals the perpendicular distance $d = r\sin\theta$
times the force $F$ — which is the classic definition of moment ($M = Fd$).
The direction of the cross product encodes the axis of rotation and its sense
(right-hand rule). (§13.5, Worked Example 4)

**6.** The scalar triple product equals the volume of the parallelepiped
spanned by the three vectors. If it equals zero, the parallelepiped has
zero volume, meaning the three vectors all lie in the same plane — they are
coplanar. (§13.6)

**7.**

(a) $(4-1)\hat{\imath} + (-3+2)\hat{\jmath} + (0+5)\hat{k} =
\boxed{3\hat{\imath} - \hat{\jmath} + 5\hat{k}}$

(b) $3(4\hat{\imath}-3\hat{\jmath}) - 2(-\hat{\imath}+2\hat{\jmath}+5\hat{k})
= 12\hat{\imath}-9\hat{\jmath} + 2\hat{\imath}-4\hat{\jmath}-10\hat{k}$
$= \boxed{14\hat{\imath} - 13\hat{\jmath} - 10\hat{k}}$

(c) $A = \sqrt{16+9+0} = 5$. $B = \sqrt{1+4+25} = \sqrt{30}$.

(d) $\hat{A} = \frac{4\hat{\imath}-3\hat{\jmath}}{5} =
\boxed{0.8\hat{\imath} - 0.6\hat{\jmath}}$

Check: $\sqrt{0.64+0.36} = 1$ ✓

**8.** $F = \sqrt{36+4+81} = \sqrt{121} = 11$ kN.

$\cos\alpha = 6/11$, $\cos\beta = -2/11$, $\cos\gamma = 9/11$

Verify: $(6/11)^2 + (-2/11)^2 + (9/11)^2 = (36+4+81)/121 = 121/121 = 1$ ✓

**9.**

(a) $\vec{A}\cdot\vec{B} = (2)(-3)+(3)(2) = -6+6 = 0$.

$\theta = 90°$ — vectors are perpendicular. ✓

(b) $\vec{A}\cdot\vec{B} = (1)(2)+(1)(-1)+(1)(3) = 2-1+3 = 4$.

$A = \sqrt{3}$, $B = \sqrt{4+1+9} = \sqrt{14}$.

$\cos\theta = 4/(\sqrt{3}\cdot\sqrt{14}) = 4/\sqrt{42} = 0.6172$.

$\theta = \arccos(0.6172) = \boxed{51.9°}$

**10.** $\vec{A}\cdot\vec{B} = (3)(5)+(4)(0) = 15$. $A = \sqrt{9+16} = 5$.

Scalar projection: $15/5 = \boxed{3}$

Vector projection: $(15/25)(3\hat{\imath}+4\hat{\jmath}) = (3/5)(3\hat{\imath}+4\hat{\jmath})$
$= \boxed{1.8\hat{\imath}+2.4\hat{\jmath}}$

Check: $\lvert 1.8\hat{\imath}+2.4\hat{\jmath}\rvert = \sqrt{3.24+5.76} = \sqrt{9} = 3$ ✓

**11.**

(a) $\vec{A}\times\vec{B} = \begin{vmatrix}\hat{\imath}&\hat{\jmath}&\hat{k}\\
2&1&-1\\1&-2&3\end{vmatrix}$

$\hat{\imath}$: $(1)(3)-(-1)(-2) = 3-2 = 1$

$\hat{\jmath}$: $-[(2)(3)-(-1)(1)] = -[6+1] = -7$

$\hat{k}$: $(2)(-2)-(1)(1) = -4-1 = -5$

$\vec{A}\times\vec{B} = \boxed{\hat{\imath} - 7\hat{\jmath} - 5\hat{k}}$

Check: $(\hat{\imath}-7\hat{\jmath}-5\hat{k})\cdot(2\hat{\imath}+\hat{\jmath}
-\hat{k}) = 2-7+5 = 0$ ✓ (perpendicular to $\vec{A}$)

$(\hat{\imath}-7\hat{\jmath}-5\hat{k})\cdot(\hat{\imath}-2\hat{\jmath}+3\hat{k})
= 1+14-15 = 0$ ✓ (perpendicular to $\vec{B}$)

(b) $\vec{A}\times\vec{B} = \begin{vmatrix}\hat{\imath}&\hat{\jmath}&\hat{k}\\
3&0&0\\0&4&0\end{vmatrix}$

$\hat{\imath}$: $(0)(0)-(0)(4) = 0$

$\hat{\jmath}$: $-[(3)(0)-(0)(0)] = 0$

$\hat{k}$: $(3)(4)-(0)(0) = 12$

$\vec{A}\times\vec{B} = \boxed{12\hat{k}}$

(c) Cyclic rule: $\vec{A} = 3\hat{\imath}$, $\vec{B} = 4\hat{\jmath}$.

$\hat{\imath}\times\hat{\jmath} = \hat{k}$, so $3\hat{\imath}\times 4\hat{\jmath}
= 12(\hat{\imath}\times\hat{\jmath}) = 12\hat{k}$ ✓

**12.**

(a) $\vec{M} = \vec{r}\times\vec{F} = \begin{vmatrix}\hat{\imath}&\hat{\jmath}
&\hat{k}\\2&3&0\\8&-6&0\end{vmatrix}$

$\hat{\imath}$: $(3)(0)-(0)(-6) = 0$

$\hat{\jmath}$: $-[(2)(0)-(0)(8)] = 0$

$\hat{k}$: $(2)(-6)-(3)(8) = -12-24 = -36$

$\vec{M} = \boxed{-36\hat{k} \text{ kN·m}}$

(b) $M = 36$ kN·m

(c) The moment vector points in the $-\hat{k}$ direction (into the page for
a standard $xy$-plane view). Physically, this means the force creates a
**clockwise** rotation about the origin when viewed from above ($+z$ direction).

**13.**

(a) $\vec{R} = (10-4-6)\hat{\imath}+(0+8-8)\hat{\jmath}+(0+2+0)\hat{k}
= \boxed{0\hat{\imath}+0\hat{\jmath}+2\hat{k}}$ kN

(b) $R = 2$ kN in the $+z$ direction.

(c) **Not in equilibrium** — the resultant is 2 kN in the $z$-direction.
For equilibrium, the resultant must be zero in all three components. The
$x$ and $y$ components cancel, but the $z$ component does not.

**14.**

(a) $\vec{AB} = (4-0)\hat{\imath}+(3-0)\hat{\jmath}+(12-0)\hat{k} =
4\hat{\imath}+3\hat{\jmath}+12\hat{k}$

$\lvert\vec{AB}\rvert = \sqrt{16+9+144} = \sqrt{169} = 13$ m

$\hat{u}_{AB} = \dfrac{4\hat{\imath}+3\hat{\jmath}+12\hat{k}}{13} =
\boxed{\tfrac{4}{13}\hat{\imath}+\tfrac{3}{13}\hat{\jmath}+\tfrac{12}{13}\hat{k}}$

(b) $\vec{F} = 260\hat{u}_{AB} = 260\left(\tfrac{4}{13}\hat{\imath}+
\tfrac{3}{13}\hat{\jmath}+\tfrac{12}{13}\hat{k}\right) =
\boxed{80\hat{\imath}+60\hat{\jmath}+240\hat{k}}$ N

(c) Scalar projection onto $\hat{u} = \frac{1}{\sqrt{2}}\hat{\imath}+
\frac{1}{\sqrt{2}}\hat{\jmath}$:

$\vec{F}\cdot\hat{u} = \frac{80}{\sqrt{2}}+\frac{60}{\sqrt{2}}+0 =
\frac{140}{\sqrt{2}} = \frac{140\sqrt{2}}{2} = \boxed{98.99 \text{ N} \approx 99.0 \text{ N}}$

**15. C — perpendicular.** $\vec{A}\cdot\vec{B} = AB\cos\theta = 0$ when
$\cos\theta = 0$, i.e., $\theta = 90°$. (§13.4)

**16. A — $\hat{\imath}$.** Following the cyclic rule: $\hat{\imath}\to
\hat{\jmath}\to\hat{k}\to\hat{\imath}$. So $\hat{\jmath}\times\hat{k} =
\hat{\imath}$. (§13.5)

**17. B — $AB\sin\theta$.** The magnitude of the cross product is
$\lvert\vec{A}\rvert\lvert\vec{B}\rvert\sin\theta$. (A) is the dot product
formula. (§13.5)

**18. D — $\vec{0}$.** Any vector crossed with itself gives the zero vector,
since $\sin 0° = 0$ (the angle between a vector and itself is 0°). (§13.5)

**19. B — $\vec{F}\cdot\vec{d}$.** Work is the dot product of force and
displacement: $W = \vec{F}\cdot\vec{d} = Fd\cos\theta$. Only the component
of force along the displacement does work. (§13.4, Worked Example 3)

**20. B — $\tfrac{3}{5}\hat{\imath}+\tfrac{4}{5}\hat{\jmath}$.** Magnitude
$= \sqrt{9+16} = 5$. Divide each component by 5. (C) divides each component
by itself individually (wrong). (D) uses the wrong magnitude of 7. (§13.3)

---

## Quick Reference

**Magnitude and unit vector**

$$\lvert\vec{A}\rvert = \sqrt{A_x^2+A_y^2+A_z^2} \qquad \hat{A} = \frac{\vec{A}}{\lvert\vec{A}\rvert}$$

$$\cos^2\alpha+\cos^2\beta+\cos^2\gamma = 1$$

**Dot product** — *Handbook p. 37*

$$\vec{A}\cdot\vec{B} = A_xB_x+A_yB_y+A_zB_z = AB\cos\theta$$

$$\cos\theta = \frac{\vec{A}\cdot\vec{B}}{AB} \qquad \vec{A}\perp\vec{B} \iff \vec{A}\cdot\vec{B}=0$$

Scalar projection of $\vec{B}$ onto $\vec{A}$: $\;\vec{A}\cdot\vec{B}/A$

Work: $W = \vec{F}\cdot\vec{d}$

**Cross product** — *Handbook p. 37–38*

$$\vec{A}\times\vec{B} = \begin{vmatrix}\hat{\imath}&\hat{\jmath}&\hat{k}\\A_x&A_y&A_z\\B_x&B_y&B_z\end{vmatrix}$$

$$\lvert\vec{A}\times\vec{B}\rvert = AB\sin\theta \qquad \vec{A}\times\vec{B} = -\vec{B}\times\vec{A}$$

Cyclic: $\hat{\imath}\times\hat{\jmath}=\hat{k}$, $\;\hat{\jmath}\times\hat{k}=\hat{\imath}$,
$\;\hat{k}\times\hat{\imath}=\hat{\jmath}$

Moment: $\vec{M} = \vec{r}\times\vec{F}$

**Not in the Handbook — memorize**

Unit vector cyclic cross products · direction cosine identity · moment
formula interpretation · coplanarity test · dot product as work/projection

---

## What's Next

Apprentice, vectors done. Magnitude, direction, dot product, cross product,
moments. These are the tools Tier 2C will use without pause.

One chapter left in Tier 1B.

In **Chapter 01-14: Matrices and Linear Algebra**, we formalize what you
started in Chapter 01-08 (systems of linear equations) and give it the
notation that makes large systems tractable. Matrix multiplication, the
determinant, Cramer's rule for 3×3 systems, eigenvalues and eigenvectors.
The determinant is what you've already been computing for cross products;
now it becomes a standalone tool for solving systems and finding critical
values.

Then Tier 1B is done. Twelve of Tier 1B's fourteen chapters are behind you,
and the tier review exam is waiting.

Bring the Handbook to page 36.

See you there.

— Your Mentor
