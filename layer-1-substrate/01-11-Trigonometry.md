---
chapter: "01-11"
title: "Trigonometry"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-011-01, MATH-1B-011-02, MATH-1B-011-03, MATH-1B-011-04, MATH-1B-011-05]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-11: Trigonometry

> *"Every force has a direction. Every direction has an angle. Every angle
> has a sine and a cosine. You cannot decompose a force, find a resultant,
> analyze a truss, or read a phasor without trigonometry. It isn't one tool
> in the kit — it's the language the kit is written in."*

---

## Before You Start

**Prerequisites:** [01-09 Analytic Geometry](01-09-analytic-geometry.md) —
§9.1 slope, parallel and perpendicular conditions, in particular ·
[01-10 Areas, Volumes, and Mensuration](01-10-areas-volumes-mensuration.md)

**Skip if:** You pass the Tier 1B test-out quiz. Verify you know the law
of sines and cosines and all the major identities before skipping — those
are the gaps that surface unexpectedly in Tier 2C problems.

**Time:** ~75 min read · ~30 min review questions · ~65 min practice problems

---

## On the Board Today

Apprentice, trigonometry is the grammar of force analysis. I want to be
clear about what that means before we start.

When you see a cable at an angle, you need to know how much of its tension
acts horizontally and how much acts vertically. That's sine and cosine.
When you have a triangle with a known side and two angles and you need the
third side, that's the law of sines. When you have two sides and an angle
and need the third side, that's the law of cosines. When you have AC
voltage and current 90° apart and need the combined impedance, that's
exactly the same geometry with different physical labels.

We're going to build trig the way it should be built: from the unit circle,
not from the right triangle. The right triangle is the special case. The
unit circle is the general case, and it's what makes trig work for any
angle — not just ones between 0° and 90°.

Then we'll cover the identities. Not all of them — the ones you'll actually
use. The Pythagorean identities, the double-angle formulas, the sum and
difference formulas. Each one with the derivation or the memory hook, so
you can rebuild it rather than just recite it.

We close by tying trig back to Chapter 01-09. The slope you learned there
is a tangent in disguise, and once you see that, the angle between any two
lines follows in one step.

![FIG-01-11-001: Unit circle diagram with labeled coordinates at key angles (0°, 30°, 45°, 60°, 90°, 120°, 135°, 150°, 180°, 210°, 225°, 240°, 270°, 300°, 315°, 330°), showing (cos θ, sin θ) at each point](../figures/FIG-01-11-001-unit-circle.png)

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 11.1 Convert between degrees and radians
* 11.2 Define sine, cosine, and tangent from the unit circle, and evaluate
  all six trig functions for standard angles without a calculator
* 11.3 Recognize and apply the signs of trig functions in all four
  quadrants using CAST and reference angles
* 11.4 State, derive, and apply the Pythagorean identities
* 11.5 Solve right triangles completely
* 11.6 Apply the law of sines, including recognizing the ambiguous case
* 11.7 Apply the law of cosines
* 11.8 State the sum, difference, double-angle, and power-reduction
  formulas and use them to find exact values
* 11.9 Apply inverse trig functions with the correct quadrant correction
* 11.10 Find the angle of inclination of a line and the acute angle between
  two lines from their slopes
* 11.11 Apply trigonometry to force decomposition and vector addition

Objective numbers match section numbers throughout.

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $\theta$, $\phi$, $\beta$ | angles | radians or degrees |
| $\alpha$ | angle of inclination of a line | measured counterclockwise from the positive $x$-axis, $0° \le \alpha < 180°$ |
| $\sin\theta$, $\cos\theta$, $\tan\theta$ | primary trig functions | — |
| $\csc\theta$, $\sec\theta$, $\cot\theta$ | reciprocal trig functions | — |
| $a$, $b$, $c$ | side lengths of a triangle | $c$ opposite angle $C$ |
| $A$, $B$, $C$ | angles of a triangle | $A + B + C = 180°$ |
| $m$, $m_1$, $m_2$ | slopes of lines | from 01-09 §9.1 |
| $L_1$, $L_2$ | labels for two lines | — |
| rad | radians | — |

> ---
> **Mentor's Margin**
>
> The Handbook uses degrees for most FE problems and radians for calculus
> and wave formulas. Your calculator must be in the right mode before every
> trig calculation. Check it. The error of computing $\sin(30)$ in radian
> mode (which gives $\sin(30 \text{ rad}) = -0.988$, not $0.5$) is common,
> quiet, and produces a plausible-looking wrong answer. Degree mode for
> force problems. Radian mode for calculus. Know which you need before
> you press any key.
>
> ---

---

## 11.1 Angles — Degrees and Radians

An angle measures the amount of rotation between two rays sharing a common
endpoint.

**Degrees** divide a full rotation into 360 equal parts. This is the
familiar unit.

**Radians** measure the angle by the arc length it subtends on a unit
circle. A full circle has circumference $2\pi$, so a full rotation is
$2\pi$ radians.

### The conversion

$$\boxed{1 \text{ rad} = \frac{180°}{\pi} \approx 57.296° \qquad 1° = \frac{\pi}{180} \text{ rad}}$$

To convert degrees to radians: multiply by $\dfrac{\pi}{180}$.

To convert radians to degrees: multiply by $\dfrac{180}{\pi}$.

### Standard angles you must know in both units

| Degrees | Radians | Note |
|---|---|---|
| 0° | 0 | — |
| 30° | $\pi/6$ | — |
| 45° | $\pi/4$ | — |
| 60° | $\pi/3$ | — |
| 90° | $\pi/2$ | — |
| 120° | $2\pi/3$ | — |
| 180° | $\pi$ | — |
| 270° | $3\pi/2$ | — |
| 360° | $2\pi$ | — |

> ---
> **Mentor's Margin**
>
> The memory trick for the multiples of 30° and 45° in radians: the
> denominator is either 6 (for 30° multiples) or 4 (for 45° multiples).
> Count the numerator like steps: 30° = π/6, 60° = 2π/6 = π/3, 90° = 3π/6
> = π/2. Same pattern for the 45° series. Once you see the denominator
> pattern, you never need to compute the conversion for a standard angle
> again.
>
> One place this hides in the Handbook: the conversion is **not** in the
> trigonometry section. It lives in Units and Conversion Factors on p. 3,
> as "radian → 180/π → degree." If you go hunting on p. 39 you will not
> find it.
>
> ---

---

## 11.2 The Unit Circle Definition

A **unit circle** is a circle of radius 1 centered at the origin. Any
point on it can be written as $(\cos\theta, \sin\theta)$, where $\theta$ is
the angle measured counterclockwise from the positive $x$-axis.

That is the definition:

$$\boxed{\cos\theta = x\text{-coordinate on the unit circle} \qquad \sin\theta = y\text{-coordinate}}$$

From these two, all others follow:

$$\tan\theta = \frac{\sin\theta}{\cos\theta} \qquad \cot\theta = \frac{\cos\theta}{\sin\theta}$$

$$\sec\theta = \frac{1}{\cos\theta} \qquad \csc\theta = \frac{1}{\sin\theta}$$

### Why the unit circle, not the right triangle?

The right triangle definition — opposite/hypotenuse, adjacent/hypotenuse —
only works for angles between 0° and 90°. The unit circle definition works
for any angle: negative angles, angles greater than 360°, the 270° angle
you'll meet in AC circuit analysis.

The right triangle is a special case of the unit circle when $\theta$ is in
the first quadrant. Everything you know about right-triangle trig is still
true — it's just not the whole picture.

> ---
> **Mentor's Margin**
>
> Be aware of a mismatch here. The Handbook defines trigonometry **only**
> from the right triangle (p. 39: $\sin\theta = y/r$, $\cos\theta = x/r$,
> $\tan\theta = y/x$, with a single right-triangle figure). There is no unit
> circle diagram in the Handbook and no table of standard angle values.
>
> That does not make the unit circle the wrong way to learn this. It makes it
> the way you learn it *once* so you never need the lookup. But it does mean
> the standard angle values are on you: the Handbook will not hand you
> $\sin 30° = 1/2$ on exam day.
>
> ---

### The values at standard angles

These must be automatic. No calculator, and no Handbook.

| $\theta$ | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|---|---|---|---|
| 0° | 0 | 1 | 0 |
| 30° | $\tfrac{1}{2}$ | $\tfrac{\sqrt{3}}{2}$ | $\tfrac{1}{\sqrt{3}} = \tfrac{\sqrt{3}}{3}$ |
| 45° | $\tfrac{\sqrt{2}}{2}$ | $\tfrac{\sqrt{2}}{2}$ | 1 |
| 60° | $\tfrac{\sqrt{3}}{2}$ | $\tfrac{1}{2}$ | $\sqrt{3}$ |
| 90° | 1 | 0 | undefined |
| 180° | 0 | $-1$ | 0 |
| 270° | $-1$ | 0 | undefined |

### The memory pattern

Look at the sine column from 0° to 90°:

$$0, \quad \tfrac{1}{2}, \quad \tfrac{\sqrt{2}}{2}, \quad \tfrac{\sqrt{3}}{2}, \quad 1$$

This can be written as:

$$\frac{\sqrt{0}}{2}, \quad \frac{\sqrt{1}}{2}, \quad \frac{\sqrt{2}}{2}, \quad \frac{\sqrt{3}}{2}, \quad \frac{\sqrt{4}}{2}$$

The numerator pattern is $\sqrt{0}, \sqrt{1}, \sqrt{2}, \sqrt{3}, \sqrt{4}$.
The cosine is the same sequence in reverse. This is not a coincidence —
sine and cosine are reflections of each other.

![FIG-01-11-002: Standard angle table shown as a visual grid with the sine and cosine values filled in using the square-root pattern, color-coded to show the symmetry between sin and cos](../figures/FIG-01-11-002-standard-angle-table.png)

---

## 11.3 Signs by Quadrant — CAST

In quadrants II, III, and IV, some trig functions are negative. The acronym
CAST tells you which are positive in each quadrant, reading counterclockwise
from quadrant IV:

| Quadrant | Angle range | Positive functions | CAST letter |
|---|---|---|---|
| I | 0° to 90° | All | A (All) |
| II | 90° to 180° | Sine only | S |
| III | 180° to 270° | Tangent only | T |
| IV | 270° to 360° | Cosine only | C |

![FIG-01-11-003: CAST diagram: coordinate plane divided into four quadrants with CAST letters placed in quadrants IV, I, II, III respectively (counterclockwise from lower-right). Each quadrant shows which functions are positive.](../figures/FIG-01-11-003-cast-diagram.png)

**Using CAST:** to evaluate $\sin(150°)$:

1. 150° is in Quadrant II — only sine is positive there.
2. The reference angle is $180° - 150° = 30°$.
3. $\sin(30°) = 1/2$.
4. Since sine is positive in Q II: $\sin(150°) = +1/2$.

**Reference angle:** the acute angle between the terminal side and the
nearest $x$-axis. Compute the trig function at the reference angle, then
apply the sign from CAST.

### Worked Example 1 — Evaluating Trig Functions in Any Quadrant

**Given.** Evaluate without a calculator: $\cos(225°)$, $\tan(300°)$,
$\sin(-60°)$.

**Solution.**

**(a) $\cos(225°)$**

225° is in Quadrant III (between 180° and 270°). CAST: only tangent is
positive in Q III.

Reference angle: $225° - 180° = 45°$.

$\cos(45°) = \sqrt{2}/2$. Cosine is negative in Q III:

$$\cos(225°) = -\frac{\sqrt{2}}{2}$$

**(b) $\tan(300°)$**

300° is in Quadrant IV (between 270° and 360°). CAST: only cosine is
positive in Q IV — tangent is negative.

Reference angle: $360° - 300° = 60°$.

$\tan(60°) = \sqrt{3}$. Tangent is negative in Q IV:

$$\tan(300°) = -\sqrt{3}$$

**(c) $\sin(-60°)$**

Negative angles rotate clockwise. $-60°$ is in Quadrant IV.

Reference angle: $60°$. $\sin(60°) = \sqrt{3}/2$. Sine is negative in Q IV:

$$\sin(-60°) = -\frac{\sqrt{3}}{2}$$

**Check using symmetry.** Sine is an odd function: $\sin(-\theta) =
-\sin(\theta)$. So $\sin(-60°) = -\sin(60°) = -\sqrt{3}/2$. ✓

---

## 11.4 The Pythagorean Identities

Derived directly from $x^2 + y^2 = 1$ on the unit circle — no memorization
required if you understand the source.

Since $\cos\theta = x$ and $\sin\theta = y$:

$$\boxed{\sin^2\theta + \cos^2\theta = 1}$$

Divide through by $\cos^2\theta$:

$$\boxed{\tan^2\theta + 1 = \sec^2\theta}$$

Divide through by $\sin^2\theta$:

$$\boxed{1 + \cot^2\theta = \csc^2\theta}$$

> ---
> **Mentor's Margin**
>
> Only the first one needs memorizing. The other two are derived in five
> seconds by dividing the first one. If you blank on $\tan^2\theta + 1 =
> \sec^2\theta$ mid-exam, write $\sin^2 + \cos^2 = 1$ and divide by
> $\cos^2$. Done. This is why deriving from first principles beats
> memorizing: the derivation is always available even when the formula isn't.
>
> All three are printed in the Handbook on p. 40 if you want to confirm
> rather than derive.
>
> ---

---

## 11.5 Solving Right Triangles

A right triangle has sides $a$, $b$ (legs) and $c$ (hypotenuse), with the
right angle opposite $c$.

$$c^2 = a^2 + b^2 \qquad \text{(Pythagorean theorem)}$$

For angle $\theta$ opposite side $a$:

$$\sin\theta = \frac{a}{c} \qquad \cos\theta = \frac{b}{c} \qquad \tan\theta = \frac{a}{b}$$

**SOH-CAH-TOA:** Sine = Opposite/Hypotenuse, Cosine = Adjacent/Hypotenuse,
Tangent = Opposite/Adjacent.

![FIG-01-11-004: Right triangle with labeled sides a (opposite), b (adjacent), c (hypotenuse) and angle theta, showing SOH-CAH-TOA annotations](../figures/FIG-01-11-004-right-triangle.png)

"Solving a right triangle" means finding all three sides and both acute
angles when given enough information (two sides, or one side and one acute
angle).

### Worked Example 2 — Right Triangle, Force Decomposition

**Given.** A 500 N force acts at 35° above the horizontal. Find the
horizontal and vertical components.

**Approach.** The force and its components form a right triangle. The 500 N
is the hypotenuse; 35° is the angle from horizontal.

**Solution.**

Horizontal component (adjacent to 35°):

$$F_x = 500 \cos(35°) = 500(0.8192) = \boxed{409.6 \text{ N}}$$

Vertical component (opposite to 35°):

$$F_y = 500 \sin(35°) = 500(0.5736) = \boxed{286.8 \text{ N}}$$

**Check.** Recombine with the Pythagorean theorem:

$$\sqrt{409.6^2 + 286.8^2} = \sqrt{167{,}772 + 82{,}254} = \sqrt{250{,}026} = 500.0 \text{ N} \;\checkmark$$

**Check the angle:** $\arctan(286.8/409.6) = \arctan(0.7002) = 35.0°$ ✓

Both checks recover the inputs, which is what a check is for: it confirms
you resolved along the right axes, not just that you multiplied correctly.

---

## 11.6 The Law of Sines

For any triangle with sides $a$, $b$, $c$ opposite angles $A$, $B$, $C$:

$$\boxed{\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}}$$

![FIG-01-11-005: General triangle with sides a, b, c and angles A, B, C labeled, showing the law of sines relationship](../figures/FIG-01-11-005-law-of-sines-triangle.png)

**Use when you know:** two angles and any side (AAS or ASA), or two sides
and a non-included angle (SSA — but watch for the ambiguous case).

### The ambiguous case (SSA)

When you know sides $a$ and $b$ and angle $A$ (not the included angle), there
may be zero, one, or two valid triangles. The conditions depend on whether
$A$ is acute:

**If $A$ is acute:**

- $a < b \sin A$ — no solution (side $a$ is too short to reach the base)
- $a = b \sin A$ — exactly one solution, a right triangle
- $b \sin A < a < b$ — **two** solutions, the ambiguous case
- $a \ge b$ — exactly one solution

**If $A$ is right or obtuse:**

- $a > b$ — exactly one solution
- $a \le b$ — no solution

The two-solution case can only arise with an acute $A$. An obtuse angle is
already the largest in the triangle, so its opposite side must be the
longest, which leaves no room for a second configuration.

> ---
> **Mentor's Margin**
>
> The ambiguous case shows up in truss problems and surveying. If you apply
> the law of sines and your calculator gives you an angle, always ask: is
> there a second angle in the supplement $(180° - \theta)$ that also fits
> the given information? For the FE, the geometry of the problem usually
> makes only one answer physically meaningful, but you need to check.
>
> ---

### Worked Example 3 — Law of Sines

**Given.** A triangle has $A = 45°$, $B = 70°$, and $a = 12$ cm.
Find side $b$.

**Solution.**

First find $C = 180° - 45° - 70° = 65°$.

Apply the law of sines:

$$\frac{b}{\sin B} = \frac{a}{\sin A} \implies b = a \cdot \frac{\sin B}{\sin A} = 12 \cdot \frac{\sin 70°}{\sin 45°}$$

$$b = 12 \cdot \frac{0.9397}{0.7071} = 12 \times 1.329 = \boxed{15.94 \text{ cm}}$$

**Check.** The larger side sits opposite the larger angle. Angle $B = 70°$
exceeds angle $A = 45°$, so side $b$ must exceed side $a$. It does:
$15.94 > 12$ ✓

---

## 11.7 The Law of Cosines

For any triangle:

$$\boxed{c^2 = a^2 + b^2 - 2ab\cos C}$$

(Also holds with any permutation of the sides and their opposite angles.
The Handbook prints all three forms on p. 39.)

**Use when you know:** three sides (SSS), or two sides and the included
angle (SAS).

**Note:** When $C = 90°$, $\cos C = 0$ and the formula reduces to the
Pythagorean theorem. The law of cosines is the general case.

### Worked Example 4 — Law of Cosines

**Given.** Two forces of 8 kN and 6 kN act at an angle of 110° between them.
Find the resultant magnitude.

**Approach.** Add the forces head to tail. The second force is redrawn from
the tip of the first, so the angle *inside* the resulting triangle is the
supplement of the angle between the vectors: $180° - 110° = 70°$. The
resultant is the closing side.

**Solution.**

$$R^2 = 8^2 + 6^2 - 2(8)(6)\cos(70°)$$
$$= 64 + 36 - 96(0.3420) = 100 - 32.83 = 67.17$$
$$R = \sqrt{67.17} = \boxed{8.20 \text{ kN}}$$

**Check by components.** Put $F_1$ along the $x$-axis and $F_2$ at 110°:

$$R_x = 8 + 6\cos(110°) = 8 - 2.05 = 5.95 \text{ kN}$$
$$R_y = 0 + 6\sin(110°) = 5.64 \text{ kN}$$
$$R = \sqrt{5.95^2 + 5.64^2} = \sqrt{67.17} = 8.20 \text{ kN} \;\checkmark$$

**Bracket the answer.** Aligned (0°) the forces sum to 14 kN. Perpendicular
(90°) they give $\sqrt{64+36} = 10$ kN. Directly opposed (180°) they give
$8 - 6 = 2$ kN. The resultant falls monotonically as the angle opens, so a
110° answer must land between 10 kN and 2 kN. It does. ✓

> ---
> **Mentor's Margin**
>
> Two forms, one result. Using the **triangle** angle (70° here), the law of
> cosines subtracts: $R^2 = a^2+b^2-2ab\cos 70°$. Using the angle **between
> the vectors** (110°), the sign flips to add: $R^2 = a^2+b^2+2ab\cos 110°$.
> Since $\cos 110° = -\cos 70°$, both give 67.17. Pick one form and state
> which angle you are using before you substitute. Mixing them applies the
> negative twice and inflates the resultant to 11.53 kN — a number that
> exceeds the perpendicular case and is therefore impossible.
>
> That is the real lesson. The bracket check catches the error without your
> needing to spot the sign mistake. Trust the bracket over the algebra.
>
> ---

---

## 11.8 Trig Identities — The Working Set

Not a complete list — the ones that appear on FE problems and in downstream
chapters. The Handbook's full set is on p. 40.

### Sum and difference formulas

$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$$

$$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$$

$$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$$

> ---
> **Mentor's Margin**
>
> The cosine sum formula has a sign reversal: $\cos(\alpha + \beta)$ uses
> $-$ on the right, not $+$. This is the identity people most often get
> backwards. Remember it this way: cosine "disagrees" — the sign on the
> right is opposite the sign in the argument. Sine "agrees" — same signs
> on both sides.
>
> Hold on to the tangent difference formula. It is the entire derivation of
> §11.10.
>
> ---

### Double-angle formulas

$$\sin(2\theta) = 2\sin\theta\cos\theta$$

$$\cos(2\theta) = \cos^2\theta - \sin^2\theta = 1 - 2\sin^2\theta = 2\cos^2\theta - 1$$

$$\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}$$

These are special cases of the sum formulas with $\alpha = \beta = \theta$.
If you blank on a double-angle formula, derive it from the sum formula in
ten seconds.

### Power-reduction forms (used in integration, Tier 1C)

$$\sin^2\theta = \frac{1 - \cos(2\theta)}{2} \qquad \cos^2\theta = \frac{1 + \cos(2\theta)}{2}$$

Rearranged from the double-angle cosine. The Handbook (p. 40) lists the
**half-angle** forms instead:

$$\sin(\alpha/2) = \pm\sqrt{\frac{1-\cos\alpha}{2}} \qquad \cos(\alpha/2) = \pm\sqrt{\frac{1+\cos\alpha}{2}}$$

Same identities. Set $\alpha = 2\theta$ and square to convert between them.
Know both shapes so you recognize the Handbook entry under exam pressure.

### Worked Example 5 — Using Identities to Find an Exact Value

**Given.** Find $\sin(75°)$ exactly without a calculator.

**Approach.** $75° = 45° + 30°$. Apply the sum formula.

**Solution.**

$$\sin(75°) = \sin(45° + 30°) = \sin 45°\cos 30° + \cos 45°\sin 30°$$

$$= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2}$$

$$= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \boxed{\frac{\sqrt{6} + \sqrt{2}}{4}}$$

**Check.** Numerically: $\sqrt{6} \approx 2.449$, $\sqrt{2} \approx 1.414$.
Sum $\approx 3.863$. Divided by 4: $\approx 0.9659$.

Calculator: $\sin(75°) = 0.9659$ ✓

---

## 11.9 Inverse Trig Functions

The inverse trig functions answer "what angle has this trig value?"

$$\theta = \arcsin(x) = \sin^{-1}(x) \implies \sin\theta = x$$

Defined on restricted domains so they're single-valued:

| Function | Output range | Notes |
|---|---|---|
| $\arcsin$ | $[-90°, 90°]$ | — |
| $\arccos$ | $[0°, 180°]$ | — |
| $\arctan$ | $(-90°, 90°)$ | — |

> ---
> **Mentor's Margin**
>
> $\arctan$ is the one you use most in engineering — finding the angle of a
> resultant force, finding a phase angle, computing a slope. Two things to
> check every time: (1) which quadrant are you actually in? $\arctan$ only
> returns values between $-90°$ and $90°$, so if your vector is in Q III or
> Q II, you need to add $180°$ to the raw $\arctan$ result. Many calculators
> have an `atan2(y, x)` function that handles all four quadrants
> automatically. Know whether yours does. (2) Degree mode — same warning as
> always.
>
> ---

### Worked Example 6 — Finding an Angle From Components

**Given.** A force has components $F_x = -350$ N and $F_y = 280$ N.
Find the angle it makes with the positive $x$-axis.

**Solution.**

Raw $\arctan$:

$$\theta_{raw} = \arctan\left(\frac{F_y}{F_x}\right) = \arctan\left(\frac{280}{-350}\right) = \arctan(-0.8) = -38.7°$$

But $F_x < 0$ and $F_y > 0$: the vector is in **Quadrant II**, not
Quadrant IV.

Correct angle:

$$\theta = -38.7° + 180° = \boxed{141.3°}$$

**Check.** In Q II, the angle should be between 90° and 180°. ✓

At 141.3°: $\cos(141.3°) = -0.780$ and $F \cdot (-0.780) = F_x$, so
$F = 350/0.780 = 449$ N. Also $F_y = 449 \sin(141.3°) = 449(0.625) = 280.6$
N ✓

---

## 11.10 Angle of Inclination and the Angle Between Two Lines

Chapter 01-09 defined slope as rise over run. With tangent now available,
that definition reveals what it always was: a tangent.

### Angle of inclination

The **angle of inclination** $\alpha$ of a line is the angle it makes with
the positive $x$-axis, measured counterclockwise, with $0° \le \alpha < 180°$.

Drop a right triangle onto any segment of the line. The run is the adjacent
side, the rise is the opposite side, and by SOH-CAH-TOA:

$$\boxed{\tan\alpha = m}$$

Slope and inclination carry the same information in different units. A slope
of 1 is 45°. A slope of 0 is horizontal. A vertical line has $\alpha = 90°$
and no slope at all, which is exactly why 01-09 insisted that vertical lines
have undefined slope — $\tan 90°$ does not exist.

To recover $\alpha$ from $m$, take $\arctan m$ and add 180° if the result is
negative, bringing it into the $[0°, 180°)$ range. This is the same quadrant
correction as §11.9, applied to lines instead of vectors.

### The angle between two lines

Two intersecting lines form two pairs of supplementary angles. "The angle
between them" conventionally means the **acute** one.

Let $L_1$ and $L_2$ have inclinations $\alpha_1$ and $\alpha_2$. The angle
between them is the difference $\alpha_2 - \alpha_1$, so apply the tangent
difference formula from §11.8:

$$\tan(\alpha_2 - \alpha_1) = \frac{\tan\alpha_2 - \tan\alpha_1}{1 + \tan\alpha_1\tan\alpha_2}$$

Substitute $\tan\alpha_1 = m_1$ and $\tan\alpha_2 = m_2$, then take the
absolute value to select the acute angle:

$$\boxed{\tan\theta = \left\lvert \frac{m_2 - m_1}{1 + m_1 m_2} \right\rvert}$$

No new machinery. This is the tangent difference identity wearing slopes
instead of angles.

![FIG-01-11-007: Two intersecting lines L1 and L2 on coordinate axes, with inclination angles alpha-1 and alpha-2 marked from the positive x-axis, and the acute angle theta between the lines marked at the intersection. Shows theta = alpha-2 minus alpha-1.](../figures/FIG-01-11-007-angle-between-lines.png)

### The two special cases are built in

Both limits from 01-09 §9.1 fall out of the formula, which is a solid check
that you have written it down correctly:

| Condition | Formula behavior | Result |
|---|---|---|
| $m_1 = m_2$ (parallel) | Numerator zero | $\tan\theta = 0$, so $\theta = 0°$ |
| $m_1 m_2 = -1$ (perpendicular) | Denominator zero | $\tan\theta$ undefined, so $\theta = 90°$ |

You now have the perpendicularity rule twice over: as the memorized
negative-reciprocal condition, and as a degenerate case of a single formula.

> ---
> **Mentor's Margin**
>
> The Handbook prints this on **p. 37**, under *Straight Line* — not in the
> trigonometry section where you would look for it. And it prints it as
>
> $$\alpha = \arctan\left[\frac{m_2-m_1}{1+m_2m_1}\right]$$
>
> **without** the absolute value. That form returns a signed angle whose sign
> depends only on which line you happened to label first. Take the absolute
> value of the argument whenever the problem asks for the acute angle, which
> is nearly always. Two things to carry into the exam: the page number, and
> the fact that the bars are yours to add.
>
> ---

### Worked Example 7 — Angle Between Two Lines

**Given.** Find the acute angle between $L_1: x - 2y + 4 = 0$ and
$L_2: 3x + y - 6 = 0$.

**Solution.**

Solve each for $y$ to read the slopes:

$$L_1: \; y = \tfrac{1}{2}x + 2 \implies m_1 = \tfrac{1}{2}$$
$$L_2: \; y = -3x + 6 \implies m_2 = -3$$

Apply the formula:

$$\tan\theta = \left\lvert \frac{m_2 - m_1}{1 + m_1 m_2} \right\rvert
= \left\lvert \frac{-3 - \tfrac{1}{2}}{1 + \left(\tfrac{1}{2}\right)(-3)} \right\rvert
= \left\lvert \frac{-\tfrac{7}{2}}{-\tfrac{1}{2}} \right\rvert = 7$$

$$\theta = \arctan 7 = \boxed{81.9°}$$

**Check by inclination angles.** Take the long road and confirm:

$$\alpha_1 = \arctan\left(\tfrac{1}{2}\right) = 26.57°$$
$$\alpha_2 = \arctan(-3) = -71.57° \implies -71.57° + 180° = 108.43°$$
$$\alpha_2 - \alpha_1 = 108.43° - 26.57° = 81.87° \;\checkmark$$

The two routes agree, as they must — the formula *is* the difference of
inclinations, repackaged so you never have to find either one.

**Sanity check.** The slopes are neither equal nor negative reciprocals
$\left(\tfrac{1}{2} \times -3 = -\tfrac{3}{2} \ne -1\right)$, so the answer
must fall strictly between 0° and 90°. It does, and it sits near the upper
end — consistent with one line rising gently while the other falls steeply.

### Worked Example 8 — Why the Absolute Value Matters

**Given.** Find the acute angle between $L_1: y = 2x$ and $L_2: y = x + 3$.

**Solution.**

Taking the lines in the order given, $m_1 = 2$ and $m_2 = 1$:

$$\frac{m_2 - m_1}{1 + m_1 m_2} = \frac{1 - 2}{1 + 2} = -\frac{1}{3}$$

Read directly, that gives $\arctan\left(-\tfrac{1}{3}\right) = -18.4°$, or
equivalently the obtuse angle $161.6°$. Both describe real angles in the
figure — two intersecting lines form two pairs of supplementary angles — but
neither is the acute angle asked for. The absolute value selects it:

$$\tan\theta = \left\lvert -\tfrac{1}{3} \right\rvert = \tfrac{1}{3}
\implies \theta = \boxed{18.4°}$$

**Check.** $\alpha_1 = \arctan 2 = 63.43°$, $\alpha_2 = \arctan 1 = 45°$, and
$63.43° - 45° = 18.43°$ ✓

**Why the sign is meaningless here.** Swap the labels — call the second line
$L_1$ — and the expression flips to $+\tfrac{1}{3}$. Nothing about the
geometry changed. That arbitrariness is precisely what the absolute value
removes.

### When one line is vertical

The formula needs both slopes, so it cannot be used when either line is
vertical. Work from inclination angles instead, using $\alpha = 90°$ for the
vertical line.

For $L_1: x = 4$ and $L_2: y = x$:

$$\alpha_1 = 90°, \quad \alpha_2 = 45° \implies \theta = 90° - 45° = \boxed{45°}$$

If the difference comes out obtuse, take its supplement to get the acute
angle.

---

## 11.11 Trig in Engineering — Force Analysis

This is the application that ties everything together.

A force $\vec{F}$ at angle $\theta$ from the positive $x$-axis has
components:

$$F_x = F\cos\theta \qquad F_y = F\sin\theta$$

Conversely, given components:

$$F = \sqrt{F_x^2 + F_y^2} \qquad \theta = \arctan\!\left(\frac{F_y}{F_x}\right) \;\text{(with quadrant check)}$$

For a system of $n$ concurrent forces, the resultant components are:

$$R_x = \sum_{i=1}^n F_{i,x} \qquad R_y = \sum_{i=1}^n F_{i,y}$$

![FIG-01-11-006: Force vector decomposition diagram showing a force F at angle theta resolved into horizontal component F_x = F cos theta and vertical component F_y = F sin theta](../figures/FIG-01-11-006-force-decomposition.png)

### Worked Example 9 — Resultant of Three Forces

**Given.** Three forces act on a pin: $F_1 = 400$ N at $30°$,
$F_2 = 300$ N at $120°$, $F_3 = 250$ N at $225°$. Find the resultant.

**Solution.**

Decompose each force:

| Force | $F\cos\theta$ | $F\sin\theta$ |
|---|---|---|
| $F_1 = 400$ N, $30°$ | $400\cos 30° = 346.4$ | $400\sin 30° = 200.0$ |
| $F_2 = 300$ N, $120°$ | $300\cos 120° = -150.0$ | $300\sin 120° = 259.8$ |
| $F_3 = 250$ N, $225°$ | $250\cos 225° = -176.8$ | $250\sin 225° = -176.8$ |
| **Sum** | **$R_x = 19.6$ N** | **$R_y = 283.0$ N** |

Resultant magnitude:

$$R = \sqrt{19.6^2 + 283.0^2} = \sqrt{384 + 80{,}089} = \sqrt{80{,}473} = \boxed{283.7 \text{ N}}$$

Resultant angle:

$$\theta = \arctan\!\left(\frac{283.0}{19.6}\right) = \arctan(14.44) = 86.0°$$

Since $R_x > 0$ and $R_y > 0$: Q I, no correction needed.

$$\boxed{R = 283.7 \text{ N} \text{ at } 86.0°}$$

**Check.** $R_y \gg R_x$, so the resultant should be nearly vertical —
86° is close to 90°. ✓ Also: $283.7 \cos(86°) = 283.7(0.0698) = 19.8 \approx
R_x = 19.6$ ✓

---

## As the Handbook States It

> **Handbook 10.6, pp. 39–40** — *Mathematics / Trigonometry*
> **Handbook 10.6, p. 37** — *Mathematics / Straight Line* (angle between lines)
> **Handbook 10.6, p. 3** — *Units and Conversion Factors* (degree-radian)

The trigonometry content is split across three places, and knowing which is
which saves you real time on exam day.

**Page 39 — Trigonometry**

- Definitions of all six trig functions, from a **right triangle only**:
  $\sin\theta = y/r$, $\cos\theta = x/r$, $\tan\theta = y/x$,
  $\cot\theta = x/y$, $\csc\theta = r/y$, $\sec\theta = r/x$
- Law of sines
- Law of cosines, all three permutations
- Euler's identity and complex roots (Chapter 01-12 territory)

**Page 40 — Identities**

- Cofunction relations: $\cos\theta = \sin(\theta + \pi/2)$, and similar
- Reciprocal and quotient identities
- All three Pythagorean identities
- Sum and difference formulas for sine, cosine, tangent, and cotangent
- Double-angle formulas for sine, cosine, tangent, and cotangent
- Half-angle formulas, in **radical** form
- Product-to-sum and sum-to-product identities

**Page 37 — Straight Line**

- The angle between two lines, printed **without** an absolute value
- Slope, slope-intercept, point-slope, general form, perpendicularity —
  everything from 01-09 §9.1

**Page 3 — Units and Conversion Factors**

- Radian-to-degree and revolution-to-radian conversion

**What's not in the Handbook — memorize:**

- The unit circle. It is not drawn anywhere in the Handbook
- The standard angle value table, and the $\sqrt{n}/2$ memory pattern
- The CAST rule for quadrant signs
- SOH-CAH-TOA as a procedure
- Reference angles as a procedure
- The ambiguous case conditions for the law of sines
- How to correct $\arctan$ for quadrant
- $\tan\alpha = m$ for the angle of inclination
- The absolute value on the angle-between-lines formula
- The decompose-and-sum procedure for force resultants
- Power-reduction forms, unless you can convert from the half-angle radicals
  on the spot

That list is longer than the Handbook's trigonometry section. Trigonometry
is one of the subjects where the reference does the least for you, which is
exactly why we built it from the unit circle rather than handing you a table.

---

## Where This Goes Wrong

**Calculator mode.** Check before every trig calculation. Degree and radian
mode produce completely different numbers, and both look plausible.

**Arctan quadrant error.** $\arctan$ returns values only between $-90°$ and
$90°$. A force in Q II or Q III requires adding $180°$ to the raw result.
Always draw the vector or check the signs of the components.

**Law of cosines included angle.** The angle $C$ in $c^2 = a^2 + b^2 -
2ab\cos C$ is the angle *between* sides $a$ and $b$ — the included angle,
opposite the side $c$ you're solving for. Using the wrong angle is the most
common error with this law.

**Mixing the two law-of-cosines forms.** With the angle *between* two force
vectors, either subtract the supplement's cosine or add that angle's cosine.
Never subtract the between-vectors cosine — that applies the negative twice.
At 110° the two correct routes both give 8.20 kN; the mixed version gives
11.53 kN, which exceeds the perpendicular case and is impossible. Bracket
every resultant against the aligned and opposed extremes.

**Dropping the absolute value on the angle between two lines.** The Handbook
prints the formula without it, and the unbarred expression can be negative,
which returns a signed or obtuse angle instead of the acute one. The sign
depends only on which line you labeled first, so it carries no geometric
meaning.

**Using the angle-between-lines formula on a vertical line.** It needs both
slopes, and a vertical line has none. Switch to inclination angles with
$\alpha = 90°$.

**SOH-CAH-TOA with the wrong side labeled.** Adjacent and opposite depend
on *which angle* you're working with. Re-label the triangle for each angle.

**Missing the negative sign in $\cos(\alpha + \beta)$.** The cosine sum
formula has a minus on the right. The sine sum formula has the same sign.
"Cosine disagrees."

**Assuming the ambiguous case whenever you see SSA.** Two solutions require
an acute given angle. If the given angle is right or obtuse, there is at
most one triangle.

**$\sin^2\theta$ notation.** This means $(\sin\theta)^2$, not
$\sin(\theta^2)$. They are different. The convention is universal in
engineering but trips people coming from certain calculator notations.

---

## Key Terms

| Term | Definition |
|---|---|
| Radian | Unit of angle; 1 rad = 180°/π; a full circle = 2π rad |
| Unit circle | Circle of radius 1; point on it at angle θ is (cos θ, sin θ) |
| SOH-CAH-TOA | Mnemonic for right-triangle definitions: sin = opp/hyp, cos = adj/hyp, tan = opp/adj |
| Reference angle | The acute angle between the terminal side and the nearest x-axis |
| CAST rule | Mnemonic for which trig functions are positive in each quadrant |
| Pythagorean identity | $\sin^2\theta + \cos^2\theta = 1$; source of two derived identities |
| Law of sines | $a/\sin A = b/\sin B = c/\sin C$; used for AAS, ASA, SSA |
| Law of cosines | $c^2 = a^2 + b^2 - 2ab\cos C$; used for SAS, SSS |
| Ambiguous case | The SSA configuration with an acute given angle where two valid triangles may exist |
| Sum formula | Identity for sin or cos of the sum of two angles |
| Double-angle formula | Identity for sin or cos of twice an angle; derived from sum formula |
| Power-reduction form | $\sin^2\theta = (1-\cos 2\theta)/2$; the double-angle cosine rearranged, equivalent to the Handbook's half-angle radicals |
| Inverse trig function | Gives the angle whose trig value equals the argument; arcsin, arccos, arctan |
| Angle of inclination | The angle α a line makes with the positive x-axis, $0° \le \alpha < 180°$; satisfies $\tan\alpha = m$ |
| Angle between two lines | The acute angle θ at the intersection of two lines; $\tan\theta = \lvert (m_2-m_1)/(1+m_1m_2)\rvert$ |
| Force decomposition | Resolving a force into components along coordinate axes using cos and sin |

---

## Review Questions

### Conceptual

1. Explain why the unit circle definition of sine and cosine is more general
   than the right-triangle definition.
2. State the CAST rule and explain the physical meaning: what does it tell
   you about a trig function at a given quadrant?
3. You compute $\arctan(F_y/F_x)$ and get $-38.7°$. The force has $F_x < 0$
   and $F_y > 0$. What is the correct angle, and why?
4. Explain the difference between the law of sines and the law of cosines:
   what information do you need to apply each?
5. Derive the formula $\cos(2\theta) = \cos^2\theta - \sin^2\theta$ from the
   sum formula for cosine. Show every step.
6. In the law of cosines $c^2 = a^2 + b^2 - 2ab\cos C$, what is $C$? Why
   is this important to identify correctly?
7. Explain why $\tan\alpha = m$ relates a line's slope to its angle of
   inclination. Your answer should say what happens for a vertical line and
   why that matches what 01-09 said about vertical slopes.
8. Derive $\tan\theta = \lvert (m_2-m_1)/(1+m_1m_2)\rvert$ from the tangent
   difference formula, and explain what the absolute value accomplishes.
   Then show that the parallel and perpendicular conditions from 01-09 §9.1
   are both special cases.

### Calculation

9. Convert to radians: (a) 150° (b) 270° (c) 72°

10. Convert to degrees: (a) $5\pi/6$ (b) $7\pi/4$ (c) $2.4$ rad

11. Evaluate without a calculator:
    (a) $\sin(210°)$
    (b) $\cos(315°)$
    (c) $\tan(150°)$
    (d) $\sin(-90°)$
    (e) $\cos(4\pi/3)$

12. Verify the Pythagorean identity at $\theta = 60°$:
    (a) $\sin^2(60°) + \cos^2(60°) = 1$
    (b) $\tan^2(60°) + 1 = \sec^2(60°)$

13. Solve each right triangle (find all missing sides and angles):
    (a) $a = 5$, $b = 12$; find $c$, $A$, $B$
    (b) $c = 20$, $A = 37°$; find $a$, $b$, $B$

14. Apply the law of sines or cosines as appropriate:
    (a) $A = 50°$, $B = 65°$, $a = 18$. Find $b$ and $c$.
    (b) $a = 10$, $b = 14$, $C = 40°$. Find $c$, then $A$ and $B$.
    (c) $a = 7$, $b = 5$, $c = 8$. Find all angles.

15. Find exact values using identities:
    (a) $\cos(105°)$ using $105° = 60° + 45°$
    (b) $\sin(15°)$ using $15° = 45° - 30°$
    (c) $\sin(2\theta)$ when $\sin\theta = 3/5$ and $\theta$ is in Q I

16. Find the angle of inclination of each line:
    (a) $y = 3x - 4$
    (b) $2x + 5y = 10$
    (c) $x = 7$

17. Find the acute angle between each pair of lines:
    (a) $y = 4x - 1$ and $y = -x + 2$
    (b) $2x + y = 5$ and $x - 3y = 6$
    (c) $x = -2$ and $y = -x + 7$
    (d) $3x - y = 1$ and $x + 3y = 12$

18. **Engineering application.** A roof truss has a rafter making a 28° angle
    with the horizontal. The rafter length is 6.5 m.
    (a) Find the horizontal span covered by the rafter.
    (b) Find the vertical rise.
    (c) A load of 12 kN acts vertically downward at the midpoint of the
    rafter. Resolve it into components parallel and perpendicular to
    the rafter.

19. **Engineering application.** Three concurrent forces act at a joint:
    $F_1 = 200$ N at 0°, $F_2 = 350$ N at 135°, $F_3 = 175$ N at 260°.
    (a) Find the resultant components $R_x$ and $R_y$.
    (b) Find the resultant magnitude and direction.

20. **Engineering application.** Two straight roadway segments meet at a
    survey point. One rises 1 m for every 8 m of horizontal run; the other
    falls 1 m for every 3 m of run.
    (a) Find each segment's angle of inclination.
    (b) Find the acute angle at which they meet.

### Multiple Choice

21. $\cos(240°)$ equals:
    A) $\sqrt{3}/2$
    B) $-\sqrt{3}/2$
    C) $1/2$
    D) $-1/2$

22. The law of cosines reduces to the Pythagorean theorem when:
    A) All three sides are equal
    B) The angle C equals 90°
    C) The angle C equals 45°
    D) Sides a and b are equal

23. Which combination of known information requires the law of cosines?
    A) Two angles and one side
    B) Two sides and the non-included angle
    C) Two sides and the included angle
    D) Three angles

24. $\arctan(-1)$ equals:
    A) $45°$
    B) $-45°$
    C) $135°$
    D) $-135°$

25. A 400 N force at 25° above horizontal has a vertical component of
    approximately:
    A) $169$ N
    B) $363$ N
    C) $219$ N
    D) $345$ N

26. The identity $\tan^2\theta + 1 = \sec^2\theta$ is derived by:
    A) Direct definition of tangent and secant
    B) Dividing $\sin^2\theta + \cos^2\theta = 1$ by $\cos^2\theta$
    C) Using the sum formula with $\alpha = \beta = \theta$
    D) It cannot be derived; it must be memorized

27. The acute angle between two lines with slopes $-2$ and $3$ is:
    A) $45°$
    B) $63.4°$
    C) $90°$
    D) $135°$

28. A line has an angle of inclination of 120°. Its slope is:
    A) $\sqrt{3}$
    B) $-\sqrt{3}$
    C) $1/\sqrt{3}$
    D) $-1/\sqrt{3}$

---

## Answer Key with Explanations

**1.** The right-triangle definition requires the angle to be between 0° and
90° so both legs are positive. The unit circle places a point at
$(\cos\theta, \sin\theta)$ for *any* angle — negative, greater than 360°,
or in any quadrant. The right-triangle definition is the restriction of the
unit circle definition to the first quadrant. Engineering problems
constantly use angles outside 0°–90°: 270° in circuit analysis, 120° in
three-phase power, obtuse angles in force analysis. (§11.2)

**2.** CAST states which trig functions are positive in each quadrant,
counterclockwise from Q IV: Cosine positive (Q IV), All positive (Q I),
Sine positive (Q II), Tangent positive (Q III). Physically: in Q I all
coordinates are positive so all functions are positive. In Q II, $x < 0$ so
cosine and tangent are negative, but $y > 0$ so sine is positive. In Q III,
both coordinates are negative, but their ratio $y/x$ is positive so tangent
is positive. In Q IV, $x > 0$ and $y < 0$, so cosine is positive but sine
and tangent are negative. (§11.3)

**3.** The correct angle is $-38.7° + 180° = 141.3°$. The $\arctan$ function
always returns values in the range $(-90°, 90°)$ — it cannot distinguish
Q II from Q IV. With $F_x < 0$ and $F_y > 0$, the vector is in Q II. Adding
$180°$ rotates from the Q IV answer to the Q II answer with the same
$y/x$ ratio. (§11.9, Worked Example 6)

**4.** Law of sines requires a side-angle pair: you must know at least one
angle and its opposite side simultaneously. It's used for AAS, ASA, and
SSA configurations. Law of cosines is used when you don't have a side-angle
pair: specifically for SAS (two sides and the included angle) and SSS (all
three sides). Equivalently: use law of cosines when the law of sines gives
you $a/\sin A$ with both $a$ and $A$ unknown. (§11.6, §11.7)

**5.** Starting from $\cos(\alpha + \beta) = \cos\alpha\cos\beta -
\sin\alpha\sin\beta$, set $\alpha = \beta = \theta$:

$$\cos(2\theta) = \cos\theta\cos\theta - \sin\theta\sin\theta = \cos^2\theta - \sin^2\theta$$

Alternative forms follow from the Pythagorean identity: replace $\sin^2\theta
= 1 - \cos^2\theta$ to get $2\cos^2\theta - 1$, or replace $\cos^2\theta = 1
- \sin^2\theta$ to get $1 - 2\sin^2\theta$. (§11.8)

**6.** $C$ is the angle **between** sides $a$ and $b$ — the included angle,
which is directly opposite the side $c$ you're solving for. Using the wrong
angle is the most common error with this law. Always label the triangle
explicitly: side $c$ opposite angle $C$, side $a$ opposite angle $A$, side
$b$ opposite angle $B$. (§11.7)

**7.** Drop a right triangle onto any segment of the line. The horizontal leg
is the run, the vertical leg is the rise, and the angle at the base is the
inclination $\alpha$. By SOH-CAH-TOA, $\tan\alpha = \text{opposite} /
\text{adjacent} = \text{rise}/\text{run} = m$. Slope and inclination are the
same information in different units.

For a vertical line the run is zero, so the ratio rise/run is undefined —
and correspondingly $\alpha = 90°$, where $\tan 90°$ does not exist. The two
statements are the same fact: 01-09 said vertical lines have undefined slope,
and trigonometry says $\tan 90°$ is undefined. (§11.10)

**8.** Two lines with inclinations $\alpha_1$ and $\alpha_2$ meet at an angle
equal to the difference $\alpha_2 - \alpha_1$. Apply the tangent difference
formula:

$$\tan(\alpha_2 - \alpha_1) = \frac{\tan\alpha_2 - \tan\alpha_1}{1 + \tan\alpha_1\tan\alpha_2} = \frac{m_2 - m_1}{1 + m_1m_2}$$

using $\tan\alpha = m$ from §11.10.

**The absolute value** selects the acute angle. Two intersecting lines form
two supplementary pairs; the unbarred expression returns whichever one
corresponds to the labeling order you chose, which may be negative or
obtuse. Since swapping the labels $L_1 \leftrightarrow L_2$ negates the
expression without changing the geometry, the sign carries no information
and the bars discard it.

**Special cases.** If $m_1 = m_2$ the numerator vanishes, giving
$\tan\theta = 0$ and $\theta = 0°$ — the parallel condition. If
$m_1m_2 = -1$ the denominator vanishes, $\tan\theta$ is undefined, and
$\theta = 90°$ — the perpendicular condition. Both rules from 01-09 §9.1 are
degenerate cases of this one formula. (§11.10)

**9.**
(a) $150° \times \pi/180 = 5\pi/6$ rad
(b) $270° \times \pi/180 = 3\pi/2$ rad
(c) $72° \times \pi/180 = 2\pi/5$ rad

**10.**
(a) $5\pi/6 \times 180/\pi = 150°$
(b) $7\pi/4 \times 180/\pi = 315°$
(c) $2.4 \times 180/\pi = 137.5°$

**11.**

(a) 210° in Q III, reference angle 30°. Sine negative in Q III:
$\sin(210°) = -1/2$

(b) 315° in Q IV, reference angle 45°. Cosine positive in Q IV:
$\cos(315°) = \sqrt{2}/2$

(c) 150° in Q II, reference angle 30°. Tangent negative in Q II:
$\tan(150°) = -1/\sqrt{3} = -\sqrt{3}/3$

(d) $\sin(-90°) = -\sin(90°) = -1$ (sine is odd)

(e) $4\pi/3 = 240°$, Q III, reference angle 60°. Cosine negative in Q III:
$\cos(4\pi/3) = -1/2$

**12.**
(a) $(\sqrt{3}/2)^2 + (1/2)^2 = 3/4 + 1/4 = 1$ ✓
(b) $(\sqrt{3})^2 + 1 = 3 + 1 = 4$. $\sec(60°) = 1/\cos(60°) = 2$.
$\sec^2(60°) = 4$ ✓

**13.**

(a) $c = \sqrt{25+144} = \sqrt{169} = 13$.
$A = \arctan(5/12) = 22.6°$. $B = 90° - 22.6° = 67.4°$

(b) $a = 20\sin(37°) = 20(0.6018) = 12.04$.
$b = 20\cos(37°) = 20(0.7986) = 15.97$.
$B = 90° - 37° = 53°$

*Check:* $12.04^2 + 15.97^2 = 145.0 + 255.0 = 400 = 20^2$ ✓

**14.**

(a) $C = 180° - 50° - 65° = 65°$.

$$b = 18\,\frac{\sin 65°}{\sin 50°} = 18\,\frac{0.9063}{0.7660} = 21.3$$

Since $C = 65° = B$, the triangle is isosceles and $c = b = 21.3$. ✓

(b) $c^2 = 10^2 + 14^2 - 2(10)(14)\cos(40°) = 100 + 196 - 280(0.7660) =
296 - 214.5 = 81.5$. $c = \sqrt{81.5} = 9.03$

$\sin A = 10\sin(40°)/9.03 = 10(0.6428)/9.03 = 0.7117$. $A = 45.4°$

$B = 180° - 40° - 45.4° = 94.6°$

*Check:* $B$ is the largest angle and $b = 14$ is the longest side ✓

(c) Using law of cosines to find angle $A$ first:
$a^2 = b^2 + c^2 - 2bc\cos A \Rightarrow 49 = 25 + 64 - 80\cos A \Rightarrow
\cos A = 40/80 = 0.500 \Rightarrow A = 60°$

$\sin B = 5\sin(60°)/7 = 4.330/7 = 0.6186 \Rightarrow B = 38.2°$

$C = 180° - 60° - 38.2° = 81.8°$

*Check:* $\sin(81.8°) \approx 0.990$; $8/\sin(81.8°) = 8.08$;
$7/\sin(60°) = 8.08$ ✓

**15.**

(a) $\cos(105°) = \cos(60°+45°) = \cos 60°\cos 45° - \sin 60°\sin 45°$
$= (1/2)(\sqrt{2}/2) - (\sqrt{3}/2)(\sqrt{2}/2) = (\sqrt{2} - \sqrt{6})/4$

(b) $\sin(15°) = \sin(45°-30°) = \sin 45°\cos 30° - \cos 45°\sin 30°$
$= (\sqrt{2}/2)(\sqrt{3}/2) - (\sqrt{2}/2)(1/2) = (\sqrt{6}-\sqrt{2})/4$

(c) In Q I with $\sin\theta = 3/5$: $\cos\theta = 4/5$ (Pythagorean).
$\sin(2\theta) = 2\sin\theta\cos\theta = 2(3/5)(4/5) = 24/25$

**16.**

(a) $m = 3$, so $\alpha = \arctan 3 = \boxed{71.6°}$

(b) $y = -\tfrac{2}{5}x + 2$, so $m = -0.4$ and
$\arctan(-0.4) = -21.8°$. Add 180° to land in $[0°, 180°)$:
$\alpha = \boxed{158.2°}$

(c) Vertical line, no slope. $\alpha = \boxed{90°}$

**17.**

(a) $m_1 = 4$, $m_2 = -1$:

$$\tan\theta = \left\lvert \frac{-1-4}{1+(4)(-1)} \right\rvert = \left\lvert \frac{-5}{-3} \right\rvert = \frac{5}{3} \implies \theta = \boxed{59.0°}$$

*Check:* $\alpha_1 = \arctan 4 = 75.96°$, $\alpha_2 = \arctan(-1) + 180° =
135°$; difference $= 59.04°$ ✓

(b) $2x + y = 5 \Rightarrow m_1 = -2$; $x - 3y = 6 \Rightarrow
y = \tfrac{1}{3}x - 2 \Rightarrow m_2 = \tfrac{1}{3}$:

$$\tan\theta = \left\lvert \frac{\tfrac{1}{3}-(-2)}{1+(-2)\left(\tfrac{1}{3}\right)} \right\rvert = \left\lvert \frac{\tfrac{7}{3}}{\tfrac{1}{3}} \right\rvert = 7 \implies \theta = \boxed{81.9°}$$

*Check:* $\alpha_1 = \arctan(-2) + 180° = 116.57°$,
$\alpha_2 = \arctan(1/3) = 18.43°$; difference $= 98.13°$, which is obtuse,
so the acute angle is $180° - 98.13° = 81.87°$ ✓ This is the case the
absolute value handles for you.

(c) $L_1$ is vertical: $\alpha_1 = 90°$. $L_2$ has $m = -1$, so
$\alpha_2 = 135°$:

$$\theta = 135° - 90° = \boxed{45°}$$

The formula cannot be used here — $m_1$ does not exist.

(d) $3x - y = 1 \Rightarrow m_1 = 3$; $x + 3y = 12 \Rightarrow
m_2 = -\tfrac{1}{3}$. Note $m_1m_2 = -1$, so the denominator is
$1 + (-1) = 0$, $\tan\theta$ is undefined, and

$$\theta = \boxed{90°}$$

The lines are perpendicular, which the negative-reciprocal test from 01-09
confirms directly.

**18.**

(a) Horizontal span: $6.5\cos(28°) = 6.5(0.8829) = \boxed{5.74 \text{ m}}$

(b) Vertical rise: $6.5\sin(28°) = 6.5(0.4695) = \boxed{3.05 \text{ m}}$

(c) The 12 kN acts vertically. The rafter axis is 28° from horizontal, so the
angle between the load direction and the rafter axis is $90° - 28° = 62°$.

Perpendicular to rafter: $12\cos(28°) = 12(0.8829) = \boxed{10.59 \text{ kN}}$

Parallel to rafter: $12\sin(28°) = 12(0.4695) = \boxed{5.63 \text{ kN}}$

*Check:* $\sqrt{10.59^2 + 5.63^2} = \sqrt{112.1 + 31.7} = \sqrt{143.8} =
11.99 \approx 12$ kN ✓ The perpendicular component dominates because the
rafter is shallow — at 0° pitch the load would be entirely perpendicular.

*Alternative route:* perpendicular $= 12\sin(62°) = 10.59$, parallel
$= 12\cos(62°) = 5.63$. Same answers ✓

**19.**

| Force | $F_x$ | $F_y$ |
|---|---|---|
| $F_1 = 200$ N, $0°$ | $200.0$ | $0$ |
| $F_2 = 350$ N, $135°$ | $350\cos(135°) = -247.5$ | $350\sin(135°) = 247.5$ |
| $F_3 = 175$ N, $260°$ | $175\cos(260°) = -30.4$ | $175\sin(260°) = -172.4$ |
| **Sum** | **$R_x = -77.9$** | **$R_y = 75.1$** |

$R = \sqrt{(-77.9)^2 + (75.1)^2} = \sqrt{6{,}068 + 5{,}640} = \sqrt{11{,}708} = \boxed{108.2 \text{ N}}$

$\theta_{raw} = \arctan(75.1/(-77.9)) = \arctan(-0.964) = -44.0°$

$R_x < 0$ and $R_y > 0$: Q II. $\theta = -44.0° + 180° = \boxed{136.0°}$

*Check:* $R_x$ and $R_y$ are nearly equal in magnitude with opposite signs,
so the resultant should sit near 135°. It does ✓

**20.**

(a) Rising segment: $m_1 = 1/8 = 0.125$, so
$\alpha_1 = \arctan(0.125) = \boxed{7.1°}$

Falling segment: $m_2 = -1/3 = -0.3333$, so
$\arctan(-0.3333) = -18.4°$, and $\alpha_2 = -18.4° + 180° = \boxed{161.6°}$

(b) $$\tan\theta = \left\lvert \frac{-\tfrac{1}{3} - \tfrac{1}{8}}{1 + \left(\tfrac{1}{8}\right)\left(-\tfrac{1}{3}\right)} \right\rvert = \left\lvert \frac{-0.4583}{0.9583} \right\rvert = 0.4783$$

$$\theta = \arctan(0.4783) = \boxed{25.6°}$$

*Check:* $\alpha_2 - \alpha_1 = 161.6° - 7.1° = 154.5°$, obtuse, so the acute
angle is $180° - 154.5° = 25.5°$ ✓ (small rounding difference)

Sanity: one segment rises about 7° and the other falls about 18°, so the
total turn between them is roughly 25°. ✓

**21. D — $-1/2$.** 240° in Q III, reference angle 60°. Only tangent is
positive in Q III. $\cos(60°) = 1/2$, so $\cos(240°) = -1/2$. (§11.3)

**22. B — The angle C equals 90°.** When $C = 90°$, $\cos C = 0$ and the
$-2ab\cos C$ term vanishes, leaving $c^2 = a^2 + b^2$. (§11.7)

**23. C — Two sides and the included angle (SAS).** The included angle is
directly between the two known sides. The other combination, two sides and
a non-included angle (SSA), uses the law of sines — with the ambiguous case
warning. (§11.6, §11.7)

**24. B — $-45°$.** $\arctan(-1)$ returns the angle in $(-90°, 90°)$ whose
tangent equals $-1$. That's $-45°$ (in Q IV). Note: if the actual vector
were in Q II, where tangent is also $-1$ (tangent of 135°), $\arctan$ would
still return $-45°$ and you'd need to add $180°$. Context determines which
is correct. (§11.9)

**25. A — $169$ N.** $F_y = 400\sin(25°) = 400(0.4226) = 169.0$ N. Note:
$400\cos(25°) = 362.5$ N is the horizontal component (choice B). (§11.11,
Worked Example 2)

**26. B — Dividing $\sin^2\theta + \cos^2\theta = 1$ by $\cos^2\theta$.**
The entire family of Pythagorean identities is derived by dividing the
fundamental one. (§11.4)

**27. A — $45°$.** With $m_1 = -2$ and $m_2 = 3$:

$$\frac{m_2-m_1}{1+m_1m_2} = \frac{3-(-2)}{1+(-2)(3)} = \frac{5}{-5} = -1$$

The absolute value gives $\tan\theta = 1$, so $\theta = 45°$. Choice (D),
135°, is what you get by reading $\arctan(-1) = -45°$ and converting to a
positive angle — the supplement, not the acute angle. The bars exist
precisely to eliminate this. Choice (C) would require $m_1m_2 = -1$, but
$(-2)(3) = -6$. (§11.10, Worked Example 8)

**28. B — $-\sqrt{3}$.** $m = \tan\alpha = \tan(120°)$. 120° is in Q II with
reference angle 60°, and tangent is negative in Q II, so
$\tan(120°) = -\tan(60°) = -\sqrt{3}$. Choice (A) drops the quadrant sign;
(C) and (D) invert the ratio. (§11.10, §11.3)

---

## Quick Reference

**Degree-radian conversion** — *Handbook p. 3 (Units and Conversion Factors)*

$$1° = \frac{\pi}{180} \text{ rad} \qquad 1 \text{ rad} = \frac{180°}{\pi} \approx 57.3°$$

**Standard angles** — *not in the Handbook; memorize*

| ° | rad | sin | cos | tan |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 |
| 30 | π/6 | 1/2 | √3/2 | 1/√3 |
| 45 | π/4 | √2/2 | √2/2 | 1 |
| 60 | π/3 | √3/2 | 1/2 | √3 |
| 90 | π/2 | 1 | 0 | — |

Sine pattern: $\sqrt{0}/2, \sqrt{1}/2, \sqrt{2}/2, \sqrt{3}/2, \sqrt{4}/2$.
Cosine is the reverse.

**CAST rule** (positive functions by quadrant) — *not in the Handbook*

Q I: All · Q II: Sine · Q III: Tangent · Q IV: Cosine

**Right triangle definitions** — *Handbook p. 39*

$$\sin\theta = \frac{y}{r} \qquad \cos\theta = \frac{x}{r} \qquad \tan\theta = \frac{y}{x}$$

**Pythagorean identities** — *Handbook p. 40*

$$\sin^2\theta + \cos^2\theta = 1 \qquad \tan^2\theta + 1 = \sec^2\theta \qquad 1 + \cot^2\theta = \csc^2\theta$$

**Laws for any triangle** — *Handbook p. 39*

$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} \qquad c^2 = a^2 + b^2 - 2ab\cos C$$

Ambiguous case (SSA) needs an **acute** given angle to admit two triangles.

**Sum formulas** — *Handbook p. 40*

$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$$
$$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$$
$$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$$

Cosine "disagrees": sign on right is opposite the sign in argument.

**Double-angle** — *Handbook p. 40*

$$\sin 2\theta = 2\sin\theta\cos\theta \qquad \cos 2\theta = \cos^2\theta - \sin^2\theta$$

**Power reduction** — *Handbook p. 40 gives the half-angle radical form*

$$\sin^2\theta = \frac{1-\cos 2\theta}{2} \qquad \cos^2\theta = \frac{1+\cos 2\theta}{2}$$

**Lines and angles** — *Handbook p. 37 (Straight Line), absolute value omitted there*

$$\tan\alpha = m \qquad \tan\theta = \left\lvert \frac{m_2-m_1}{1+m_1m_2} \right\rvert$$

Parallel: numerator zero, $\theta = 0°$. Perpendicular: denominator zero,
$\theta = 90°$. Vertical line: use $\alpha = 90°$ and take differences.

**Force decomposition and resultant** — *not in the Handbook as a procedure*

$$F_x = F\cos\theta \quad F_y = F\sin\theta \quad R = \sqrt{R_x^2+R_y^2} \quad \theta = \arctan(R_y/R_x) + \text{quadrant correction}$$

**Not in the Handbook — memorize**

The unit circle · standard angle values and the $\sqrt{n}/2$ pattern ·
CAST rule · SOH-CAH-TOA as a procedure · reference angles · arctan quadrant
correction · ambiguous case conditions · $\tan\alpha = m$ · the absolute
value on the angle-between-lines formula · decompose-and-sum procedure

---

## What's Next

Apprentice, trigonometry done. You can find any angle, any side, decompose
any force, recognize the sign of any trig function at a glance, and read a
slope as an angle.

In **Chapter 01-12: Complex Numbers**, the real and imaginary axes combine
into a single plane, and Euler's identity ties together the exponential
function from Chapter 01-05 with the trig functions you just mastered.
The rectangular and polar forms of complex numbers are the language of
AC circuit phasors, vibration analysis, and control systems — and they're
exactly the coordinate geometry of this chapter extended by one dimension.

The conversion $\theta = \arctan(b/a)$ that turns a complex number into polar
form is the same quadrant-corrected arctangent you used for force resultants
in §11.11. Different labels, identical arithmetic.

Bring the Handbook to **pages 38–39**. Algebra of Complex Numbers and the
Polar Coordinate System are on p. 38; Euler's Identity and complex roots are
on p. 39, sharing a page with the trigonometry you just finished.

See you there.

— Your Mentor