---
chapter: "01-09"
title: "Analytic Geometry"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-009-01, MATH-1B-009-02, MATH-1B-009-03]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-09: Analytic Geometry

> *"Descartes gave us coordinate geometry and in doing so connected every
> algebraic equation to a shape and every shape to an algebra. That union
> is why a structural engineer can describe a parabolic arch with an
> equation, a surveyor can compute a distance from coordinates, and a
> circuit analyst can find a resonant frequency geometrically. The same
> mathematics speaks all those languages."*

---

## Before You Start

**Prerequisites:** [01-04 Expressions, Equations, and Inequalities](01-04-expressions-equations-inequalities.md) · [01-06 Functions, Graphs, and Transformations](01-06-functions-graphs-transformations.md) · [01-07 Polynomials and Their Roots](01-07-polynomials-and-their-roots.md) · [01-08 Systems of Linear Equations](01-08-systems-of-linear-equations.md)

From 01-07 you need **completing the square** (§7.4) — it is the engine of
this entire chapter. From 01-08 you need **Gaussian elimination**, used once,
to find a circle through three given points.

**Skip if:** You pass the Tier 1B test-out quiz. Before skipping, verify you
can convert a general second-degree equation to standard form by completing
the square, and state from memory which conic has $c^2 = a^2 - b^2$ and which
has $c^2 = a^2 + b^2$. Those two are where the marks are lost.

**Time:** ~60 min read · ~25 min review questions · ~60 min practice problems

---

## On the Board Today

Apprentice, this is where algebra and geometry formally shake hands. Every
equation has a shape; every shape has an equation. What we build here is the
vocabulary that lets you move between them without stopping to think.

Here is the practical stake. The Handbook gives you standard-form equations
and parameter formulas for every shape in this chapter, laid out in tables.
What it will not do is tell you *which* table you need. A problem hands you
$9x^2 - 4y^2 + 36x + 8y - 4 = 0$ and asks for the asymptotes. Before you can
use any formula, you have to look at that and know — in about two seconds —
that it is a hyperbola, and that getting the asymptotes means completing the
square to find the centre first. Recognition is the skill the Handbook cannot
supply.

The shapes that actually turn up: **lines** everywhere; **circles** in
cross-sections, turning radii, and Mohr's circle later on; **parabolas** in
loaded cables, arches, projectile paths, and reflectors; **ellipses** in
pressure-vessel cross-sections and tunnel profiles; **hyperbolas** less often,
though cooling towers and some navigation problems are genuinely hyperbolic.

One organizing idea before we start. Those four curves are not four unrelated
facts to memorize. They are four slices of the same cone, and a single number
— the **eccentricity** — orders them along a continuum. I'll work through them
one at a time and then, in §9.8, show you the thread that connects them. That
section is the one that makes the rest stick.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 9.1 Find the equation of a line from two points, from a point and a slope,
  or from a point and a parallel or perpendicular condition; compute the
  distance from a point to a line and the angle between two lines
* 9.2 Compute the distance between two points and the midpoint of a segment,
  in two and three dimensions
* 9.3 Describe the four conic sections as slices of a cone and state what
  distinguishes them
* 9.4 Write the equation of a circle in standard form, and convert a general
  equation to standard form by completing the square
* 9.5 Identify the vertex, focus, directrix, axis, and opening direction of a
  parabola from its equation
* 9.6 Identify the centre, axes, vertices, and foci of an ellipse, and apply
  $c^2 = a^2 - b^2$
* 9.7 Identify the centre, vertices, foci, and asymptotes of a hyperbola, and
  apply $c^2 = a^2 + b^2$
* 9.8 Define eccentricity and use it to classify and compare all four conics
* 9.9 Classify any second-degree equation by inspection and reduce it to
  standard form

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $(x_1, y_1)$, $(x_2, y_2)$ | specific named points | — |
| $m$ | slope of a line | — |
| $d$ | distance | — |
| $r$ | radius of a circle | **not** resistance or correlation here |
| $(h, k)$ | centre of a circle or ellipse; vertex of a parabola | — |
| $p$ | directed distance from parabola vertex to focus | **not** pressure here |
| $a$ | semi-major axis (ellipse) or semi-transverse axis (hyperbola) | always the larger for an ellipse |
| $b$ | semi-minor axis (ellipse) or semi-conjugate axis (hyperbola) | — |
| $c$ | focal distance from centre | $c^2 = a^2 - b^2$ ellipse, $c^2 = a^2 + b^2$ hyperbola |
| $e$ | eccentricity, $c/a$ | **not** Euler's number here |
| $A, B, C, D, E, F$ | coefficients of the general second-degree equation | §9.9 |

> ---
> **Mentor's Margin**
>
> Three collisions in one chapter, which is the most of any chapter in Tier 1.
>
> $r$ is a radius here. Not resistance, not the correlation coefficient of
> Tier 1F, not the position vector of Chapter 01-13.
>
> $e$ is eccentricity here, a number between 0 and infinity. It is **not**
> Euler's number $2.718\ldots$, which has appeared in every chapter since
> 01-05. Nothing in the notation distinguishes them; only context does. When
> you see $e = 0.8$ you are reading about an ellipse.
>
> $p$ is the vertex-to-focus distance. Not pressure, not momentum.
>
> The per-chapter notation banner exists precisely for chapters like this one.
> Read it rather than assuming.
>
> ---

---

## 9.1 Lines

The most fundamental object, and the one you will write most often. Three
forms, each earning its place.

### Slope-intercept form

$$\boxed{y = mx + b}$$

$m$ is the slope, $b$ the $y$-intercept. Best when you already have both, or
when you want to read them off at a glance.

### Point-slope form

$$\boxed{y - y_1 = m(x - x_1)}$$

Best when you have any one point $(x_1, y_1)$ and the slope. This is the
workhorse — most problems hand you exactly that, and this form needs no
rearranging to use.

### General form

$$\boxed{Ax + By + C = 0}$$

Conventionally with $A$, $B$, $C$ integers and $A \ge 0$. Two reasons it
matters: it is the only one of the three that can express a **vertical line**,
and it is the form the point-to-line distance formula requires.

A vertical line through $x = a$ is written $x = a$; its slope is **undefined**,
because the run is zero and you cannot divide by it. A horizontal line through
$y = b$ is $y = b$, slope zero. Undefined and zero are different things, and
mixing them up is a reliable way to lose a mark.

### Computing slope from two points

$$\boxed{m = \frac{y_2 - y_1}{x_2 - x_1}}$$

Rise over run. Take the points in either order — both differences flip sign
and the ratio is unchanged — but take them in the *same* order top and bottom.

![FIG-01-09-001: Upper part: a single line plotted on axes with a slope triangle drawn on it, the horizontal leg labelled 'run, x2 − x1' and the vertical leg labelled 'rise, y2 − y1', with the two defining points marked and the ratio m = rise over run printed beside it. The y-intercept is marked with a filled dot and labelled b. Lower part: three boxes, each holding one form of the line equation with a tag stating when to reach for it. Box 1, y = mx + b, tagged 'slope-intercept — when you have the slope and the y-intercept, or want to read them off'. Box 2, y − y1 = m(x − x1), tagged 'point-slope — when you have any one point and the slope; the fastest route in most problems'. Box 3, Ax + By + C = 0, tagged 'general — the only form that handles a vertical line, and the form the point-to-line distance formula needs'. A footer strip shows two degenerate cases side by side: a vertical line labelled 'x = a, slope undefined, run is zero' and a horizontal line labelled 'y = b, slope zero, rise is zero'.](../figures/FIG-01-09-001-line-forms-and-slope.png)

### Parallel and perpendicular

**Parallel lines** have equal slopes: $m_1 = m_2$.

**Perpendicular lines** have slopes that are negative reciprocals:

$$\boxed{m_1 m_2 = -1} \qquad \text{equivalently} \qquad m_2 = -\frac{1}{m_1}$$

That rule is worth understanding rather than memorizing, because "negative
reciprocal" gets truncated to "negative" under time pressure.

Here is why both halves are needed. A slope is a triangle: run $a$ across,
rise $b$ up, so $m = b/a$. Rotate that triangle a quarter turn
counter-clockwise. The run that pointed right now points up, so the old run
$a$ becomes the new **rise** $a$. The rise that pointed up now points left, so
the old rise $b$ becomes a new run of $-b$. The rotated slope is therefore

$$\frac{\text{new rise}}{\text{new run}} = \frac{a}{-b} = -\frac{1}{b/a} = -\frac{1}{m}$$

The **reciprocal** appears because run and rise trade places. The **minus
sign** appears because the run reverses direction. Negating alone gives you
neither, and it describes a line that is not perpendicular to anything you
asked about.

![FIG-01-09-002: Two panels. Left panel 'parallel': two lines drawn with identical slope triangles, both with run 3 and rise 2, the triangles shaded to show they are congruent, labelled 'same triangle, same slope, m1 = m2 — the lines never meet'. Right panel 'perpendicular': one slope triangle with run 3 and rise 2 drawn solid, and the same triangle rotated a quarter turn counter-clockwise drawn dashed beside it, with a curved rotation arrow between them labelled 'rotate the triangle 90 degrees'. The rotated triangle is annotated to show the original run of 3 has become a rise of 3 and the original rise of 2 has become a run of negative 2, giving the new slope as 3 divided by negative 2. Below, the general statement: a triangle with run a and rise b rotates to run negative b and rise a, so the slope goes from b over a to a over negative b, which is negative one over the original slope. The identity m1 times m2 equals negative 1 is boxed. A footer note reads 'the reciprocal comes from run and rise trading places; the minus sign comes from the run reversing direction — negating alone gives neither'.](../figures/FIG-01-09-002-perpendicular-slope-rotation.png)


### Distance from a point to a line

The perpendicular distance from $(x_0, y_0)$ to the line $Ax + By + C = 0$:

$$\boxed{d = \frac{\lvert Ax_0 + By_0 + C \rvert}{\sqrt{A^2 + B^2}}}$$

Two things about using it. The line **must** be in general form, with
everything moved to one side — feeding it $y = mx + b$ directly gives nonsense.
And the absolute value is not decoration: distance is never negative, and the
expression inside is negative for points on one side of the line.

A numerator of zero is meaningful rather than an error. It says the point
satisfies the equation, so the point lies *on* the line and the distance is
genuinely zero.

![FIG-01-09-003: A line drawn on axes labelled with its general form Ax + By + C = 0, and an external point marked and labelled with coordinates x-nought, y-nought. Several dashed segments run from the point to various places on the line, each labelled with its length, and the shortest of them is drawn solid and heavy, meeting the line at a right angle marked with a small square, labelled 'the perpendicular segment is the distance — every other route is longer'. The formula d equals the absolute value of A x-nought plus B y-nought plus C, all over the square root of A squared plus B squared, is printed beside it with two leader lines: one to the numerator reading 'substitute the point into the left side of the equation; absolute value because distance has no sign', and one to the denominator reading 'depends only on the line, not the point'. A side note reads 'a numerator of zero means the point satisfies the equation — it is ON the line, distance zero'.](../figures/FIG-01-09-003-point-to-line-distance.png)

### Worked Example 1 — Line Equations

**Given.**

(a) Find the equation of the line through $(2, -1)$ and $(5, 5)$.
(b) Find the equation of the line through $(-3, 4)$ perpendicular to
$y = 2x - 7$.
(c) Find the distance from $(3, -2)$ to the line $3x - 4y + 5 = 0$.


**Solution.**

**(a)** Slope first:

$$m = \frac{5 - (-1)}{5 - 2} = \frac{6}{3} = 2$$

Point-slope through $(2, -1)$:

$$y - (-1) = 2(x - 2) \implies y + 1 = 2x - 4 \implies \boxed{y = 2x - 5}$$

*Check both given points:* at $x = 2$, $y = -1$ ✓; at $x = 5$, $y = 5$ ✓.

**(b)** The given line has $m_1 = 2$, so the perpendicular slope is
$m_2 = -\tfrac{1}{2}$.

$$y - 4 = -\tfrac{1}{2}(x + 3) \implies y = -\tfrac{1}{2}x - \tfrac{3}{2} + 4$$

$$\boxed{y = -\tfrac{1}{2}x + \tfrac{5}{2}} \qquad \text{or} \qquad x + 2y - 5 = 0$$

*Check:* $m_1 m_2 = 2 \times (-\tfrac{1}{2}) = -1$ ✓. At $x = -3$:
$y = \tfrac{3}{2} + \tfrac{5}{2} = 4$ ✓.

**(c)** Already in general form, with $A = 3$, $B = -4$, $C = 5$:

$$d = \frac{\lvert 3(3) + (-4)(-2) + 5 \rvert}{\sqrt{3^2 + (-4)^2}} = \frac{\lvert 9 + 8 + 5 \rvert}{\sqrt{25}} = \frac{22}{5} = \boxed{4.4}$$

Watch the $(-4)(-2) = +8$. A sign slip there gives $6/5$, which is a
plausible-looking wrong answer.

**(d)** $m_1 = 2$, $m_2 = -\tfrac{1}{3}$:

$$\tan\theta = \left\lvert \frac{-\tfrac{1}{3} - 2}{1 + 2\left(-\tfrac{1}{3}\right)} \right\rvert = \left\lvert \frac{-\tfrac{7}{3}}{\tfrac{1}{3}} \right\rvert = 7$$

$$\theta = \arctan 7 = \boxed{81.9°}$$

*Sanity check:* one line rises steeply, the other falls gently, so a large
acute angle is right. Had the answer come out near $0°$ or above $90°$, the
formula was misapplied.

---

## 9.2 Distance and Midpoint

### Distance between two points

$$\boxed{d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}}$$

This is not a new fact to memorize — it is the Pythagorean theorem wearing
coordinates. Drop a horizontal leg and a vertical leg from your two points and
you have a right triangle whose legs are the coordinate differences and whose
hypotenuse is the distance you want.

Because both differences are squared, their signs are irrelevant. Subtract in
whichever order you like.

### Midpoint

$$\boxed{M = \left(\frac{x_1 + x_2}{2},\; \frac{y_1 + y_2}{2}\right)}$$

Average the coordinates, one axis at a time. That is all it is.

### Three dimensions

$$\boxed{d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}}$$

Same construction, one more squared difference under the root. Chapter 01-13
will recast this as the magnitude of a difference of position vectors, but the
formula is complete and usable exactly as written.

![FIG-01-09-004: Two points plotted on axes and joined by a straight segment, with a right triangle completed beneath by dropping a horizontal leg and a vertical leg. The horizontal leg is labelled with the difference in x, the vertical leg with the difference in y, and the right angle is marked with a small square. The segment itself is labelled as the hypotenuse, with the Pythagorean statement d squared equals the x-difference squared plus the y-difference squared printed alongside and the distance formula boxed beneath it. The midpoint of the segment is marked with an open dot, with dashed guides dropping to each axis at the average of the two x-coordinates and the average of the two y-coordinates respectively, labelled 'the midpoint is just the average of the coordinates, taken one axis at a time'. An inset in the corner shows the three-dimensional extension with a box drawn in perspective, its space diagonal marked, labelled 'in three dimensions add a z-difference squared under the same root'.](../figures/FIG-01-09-004-distance-midpoint-pythagoras.png)

---

## 9.3 The Conic Family

Before the individual shapes, the thing that makes them one topic.

Take two cones joined tip to tip, extending forever in both directions. Slice
that surface with a flat plane. The curve you get depends only on how the
plane is tilted:

- Cut **perpendicular** to the axis → a **circle**
- Tilt it somewhat → an **ellipse**
- Tilt it until it is exactly **parallel to the cone's side** → a **parabola**
- Tilt it further, steeply enough to cut both cones → a **hyperbola**, in two
  branches

These four are the **conic sections**, and that shared origin is why they
share so much algebraic structure: all four are second-degree equations in
$x$ and $y$, nothing more.

![FIG-01-09-005: A double cone drawn in perspective, joined at its apex, with four cutting planes shown slicing it at different angles and the resulting cross-section curve drawn beside each. Cut 1 is horizontal, perpendicular to the axis, producing a circle. Cut 2 is tilted moderately, producing an ellipse. Cut 3 is tilted exactly parallel to the cone's side, producing a parabola, with the parallelism marked by a small equal-angle notation. Cut 4 is steep enough to pass through both halves of the double cone, producing the two branches of a hyperbola. Each cut is tagged with its resulting curve name and its eccentricity: circle e = 0, ellipse e between 0 and 1, parabola e = 1 exactly, hyperbola e greater than 1. A footer strip reads 'one surface, four curves — the only thing that changes is the tilt of the cut, which is why a single parameter e orders all four'.](../figures/FIG-01-09-005-conic-sections-from-cone.png)

Each conic also has a **focus-based definition**, and these are what the
standard-form equations are built from:

| Conic | Defining condition |
|---|---|
| Circle | Distance to the centre is constant |
| Parabola | Distance to a focus equals distance to a directrix line |
| Ellipse | **Sum** of distances to two foci is constant |
| Hyperbola | Absolute **difference** of distances to two foci is constant |

Notice the ellipse and hyperbola differ by one word: sum versus difference.
That single swap is what turns a closed loop into two opening branches, and it
is what flips the sign in $c^2 = a^2 \mp b^2$ later on.

§9.8 returns to tie all four together with one parameter. Work through the
shapes first.

---

## 9.4 Circles

### Standard form

Centre $(h, k)$, radius $r$:

$$\boxed{(x - h)^2 + (y - k)^2 = r^2}$$

Read it as the distance formula rearranged: the set of points whose distance
from $(h,k)$ equals $r$. That is the definition, made algebraic.

Two reliable traps. The centre is $(h, k)$ with the signs **flipped** from
what appears in the equation — $(x+5)^2$ means $h = -5$. And the right-hand
side is $r^2$, not $r$; a right side of 16 means a radius of 4.

### General form and the conversion

Expanding the standard form and collecting terms gives

$$x^2 + y^2 + Dx + Ey + F = 0$$

which is how circles usually arrive in problems. Note that $x^2$ and $y^2$
both have coefficient $1$. If a problem hands you $2x^2 + 2y^2 + \ldots = 0$,
divide the whole equation by 2 before doing anything else. Skipping that step
is the single most common error in this section.

To convert general → standard, **complete the square** in $x$ and in $y$
separately, exactly as in §7.4. Group by variable, take half of each linear
coefficient, square it, and add it to *both* sides.

![FIG-01-09-006: A three-stage left-to-right transformation of x squared plus y squared minus 6x plus 4y minus 3 equals 0 into standard form. Stage 1 shows the general equation with the x-terms shaded one tone and the y-terms another, annotated 'group by variable, move the constant right'. Stage 2 shows the two groups in parentheses with the completing constants being added, 9 for the x-group and 4 for the y-group, each shown entering both sides of the equation via paired arrows, annotated 'half the linear coefficient, squared — and it must go on BOTH sides'. Stage 3 shows the standard form, x minus 3 all squared plus y plus 2 all squared equals 16, with leader lines to a small plot beside it marking the centre at the point 3, negative 2 and the radius drawn as an arrow of length 4 to the circle. A warning strip beneath reads 'the right side is r squared, not r — here 16 means a radius of 4'. A second warning reads 'if the x squared and y squared coefficients are not 1, divide the whole equation through first'.](../figures/FIG-01-09-006-circle-completing-square.png)

### When it isn't a circle

After completing the square you have $(x-h)^2 + (y-k)^2 = R$ for some number
$R$. Three cases:

- $R > 0$ → a genuine circle, $r = \sqrt{R}$
- $R = 0$ → a **single point** at $(h,k)$, nothing else satisfies it
- $R < 0$ → **no graph at all**; a sum of two squares cannot be negative

These are the **degenerate** cases. They are rare on the exam, but a negative
right side means "no such circle," not "take the root anyway."

### Worked Example 2 — Circle Identification

**Given.**
(a) Write the equation of the circle centred at $(3, -2)$ with radius 5.
(b) Find the centre and radius of $x^2 + y^2 - 6x + 4y - 3 = 0$.

**Solution.**

**(a)** Substitute into standard form, minding the signs:

$$\boxed{(x-3)^2 + (y+2)^2 = 25}$$

**(b)** Coefficients on $x^2$ and $y^2$ are both 1, so no division needed.
Group and move the constant:

$$(x^2 - 6x) + (y^2 + 4y) = 3$$

Half of $-6$ is $-3$, squared is $9$. Half of $4$ is $2$, squared is $4$. Add
both to both sides:

$$(x^2 - 6x + 9) + (y^2 + 4y + 4) = 3 + 9 + 4$$

$$(x-3)^2 + (y+2)^2 = 16$$

$$\boxed{\text{Centre } (3, -2), \quad r = \sqrt{16} = 4}$$

*Check.* The point $(3+4, -2) = (7,-2)$ should lie on the circle. In the
original equation: $49 + 4 - 42 - 8 - 3 = 0$ ✓

### Worked Example 3 — Circle Through Three Points

Three points that are not collinear determine exactly one circle. Finding it
uses the general form and the elimination from Chapter 01-08.

**Given.** Find the circle through $(0,0)$, $(6,0)$, and $(0,8)$.

**Solution.**

Start from $x^2 + y^2 + Dx + Ey + F = 0$ and substitute each point to get
three equations in the three unknowns $D$, $E$, $F$.

From $(0,0)$:

$$0 + 0 + 0 + 0 + F = 0 \implies F = 0$$

From $(6,0)$:

$$36 + 0 + 6D + 0 + F = 0 \implies 6D = -36 \implies D = -6$$

From $(0,8)$:

$$0 + 64 + 0 + 8E + F = 0 \implies 8E = -64 \implies E = -8$$

So $x^2 + y^2 - 6x - 8y = 0$. Complete the square:

$$(x^2 - 6x + 9) + (y^2 - 8y + 16) = 0 + 9 + 16$$

$$\boxed{(x-3)^2 + (y-4)^2 = 25} \qquad \text{centre } (3,4), \; r = 5$$

*Independent check.* These three points form a right triangle with its right
angle at the origin. A right angle inscribed in a circle always subtends a
diameter, so the segment from $(6,0)$ to $(0,8)$ must be a diameter. Its
length is $\sqrt{36+64} = 10$, giving $r = 5$ ✓, and its midpoint is
$(3,4)$ ✓ — the centre, by a completely different route.

> ---
> **Mentor's Margin**
>
> That example was engineered to be easy: each point killed all but one
> unknown, so no elimination was needed. Choose three less convenient points
> and you get a genuine $3\times3$ system requiring the full Gaussian
> treatment from §8.3. The *method* is identical either way — substitute three
> points, solve for $D$, $E$, $F$, complete the square. Only the arithmetic
> changes.
>
> Also note what the check bought. Two independent routes to the same centre
> and radius is far stronger evidence than re-running the same algebra twice.
> Build the habit of looking for a second route on any answer you distrust.
>
> ---

---

## 9.5 Parabolas

A **parabola** is the set of points equidistant from a fixed point, the
**focus**, and a fixed line, the **directrix**.

### Standard forms

**Vertical axis** — opens up or down:

$$\boxed{(x - h)^2 = 4p(y - k)}$$

- Vertex $(h, k)$; axis of symmetry $x = h$
- Focus $(h,\; k + p)$; directrix $y = k - p$
- Opens **up** if $p > 0$, **down** if $p < 0$

**Horizontal axis** — opens left or right:

$$\boxed{(y - k)^2 = 4p(x - h)}$$

- Vertex $(h, k)$; axis of symmetry $y = k$
- Focus $(h + p,\; k)$; directrix $x = h - p$
- Opens **right** if $p > 0$, **left** if $p < 0$

The rule for which variable is squared: **the squared variable is the one that
does not move along the axis.** In $(x-h)^2 = 4p(y-k)$, $y$ runs along the
axis and $x$ is squared, so the axis is vertical.

![FIG-01-09-007: Main panel: a parabola opening upward with vertex marked at the point h, k. The focus is marked with a filled dot inside the curve at h, k plus p, and the directrix is drawn as a dashed horizontal line below the vertex at y equals k minus p. A double-headed arrow from vertex to focus is labelled p, and an identical arrow from vertex down to the directrix is labelled p, with a note 'the vertex sits exactly halfway between focus and directrix'. A sample point on the curve has two equal-length segments drawn from it, one to the focus and one perpendicular to the directrix, both tick-marked to show equality and labelled 'every point on the curve is equidistant from focus and directrix — that IS the definition'. A vertical dashed line through the vertex is labelled 'axis of symmetry, x = h'. Side panel: four small sketches showing the four orientations, each with its equation and sign condition — x minus h squared equals 4p times y minus k with p positive opening up, the same with p negative opening down, y minus k squared equals 4p times x minus h with p positive opening right, the same with p negative opening left. A footer strip reads 'the curve always opens TOWARD the focus and away from the directrix — that one sentence replaces four sign rules'.](../figures/FIG-01-09-007-parabola-anatomy.png)

> ---
> **Mentor's Margin**
>
> Do not memorize four sign rules. Memorize one sentence: **the parabola
> opens toward the focus and away from the directrix.**
>
> $p$ is the *directed* distance from vertex to focus. Positive $p$ puts the
> focus above the vertex (vertical case) or to its right (horizontal case), so
> that is the way the curve opens. Negative $p$ puts it below or left. The
> directrix always sits $p$ units on the opposite side, with the vertex exactly
> halfway between.
>
> Get $p$'s sign, place the focus, and the opening direction follows without
> any further recall.
>
> ---

### The reflective property

Any ray travelling parallel to the axis, on striking the parabola, reflects
straight through the focus. Run it backwards and a source at the focus emits a
parallel beam.

This is not a coincidence — it follows from the focus-directrix definition —
and it is the entire reason parabolic shapes are used for satellite dishes,
solar collectors, radio telescopes, and headlight reflectors. The receiver goes
at the focus because that is the one point where all incoming parallel energy
arrives.

![FIG-01-09-008: A parabola drawn opening rightward, representing a dish in cross-section, with its focus marked by a filled dot and labelled 'receiver here'. Five parallel rays enter from the left travelling parallel to the axis of symmetry, strike the curve at five different points, and reflect, with every reflected ray drawn converging on the focus. At one strike point the local tangent line is drawn dashed with the incoming and outgoing angles marked equal to each other, labelled 'angle in equals angle out, measured from the tangent'. A caption reads 'parallel rays in, all through the focus — this is why the receiver goes at the focus and nowhere else'. A side note reads 'run it backwards and a source at the focus emits a parallel beam, which is the headlight and searchlight case'.](../figures/FIG-01-09-008-parabola-reflective-property.png)

### Engineering context

A cable carrying a **uniformly distributed load along its horizontal span** —
a suspension bridge deck, for instance — hangs in a parabola. A cable carrying
only its own weight hangs in a catenary, which is a different curve, though the
two are close for shallow sags. Parabolic arches carry distributed vertical
load efficiently for the same reason.

### Worked Example 4 — Parabolic Cable

**Given.** A cable hangs with its lowest point at the origin and passes
through $(120, 15)$, with $x$ and $y$ in feet. Write its equation and locate
the focus.

**Solution.**

Lowest point at the origin means vertex $(0,0)$, opening upward, vertical
axis:

$$x^2 = 4py$$

Substitute the known point:

$$(120)^2 = 4p(15) \implies 14{,}400 = 60p \implies p = 240 \text{ ft}$$

$$\boxed{x^2 = 960y}$$

Focus at $(0, 240)$ — 240 ft above the low point.

*Check:* at $x = 120$, $y = 14{,}400/960 = 15$ ✓

*Sanity check:* $p$ is large compared with the 15 ft sag, which is what a very
shallow parabola should give. A sharply curved parabola has a focus close to
its vertex; a nearly flat one has a distant focus.

---

## 9.6 Ellipses

An **ellipse** is the set of points for which the **sum** of the distances to
two fixed foci is constant. That constant equals $2a$, which is why the string
construction works: pin two ends, pull a loop taut with a pencil, and the
pencil traces an ellipse.

### Standard form, centre at the origin

**Horizontal major axis** (wider than tall):

$$\boxed{\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1}$$

**Vertical major axis** (taller than wide):

$$\boxed{\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1}$$

The convention is that $a$ is **always** the semi-major axis, so $a > b$
always. Which form you have is therefore settled by one question: **which
denominator is larger?** The larger denominator sits under the variable the
ellipse is longer along.

### Centre at $(h,k)$

$$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1 \qquad \text{(horizontal major axis)}$$

### Key parameters

$$\boxed{c^2 = a^2 - b^2}$$

| Feature | Horizontal major | Vertical major |
|---|---|---|
| Centre | $(h,k)$ | $(h,k)$ |
| Major vertices | $(h \pm a,\; k)$ | $(h,\; k \pm a)$ |
| Minor co-vertices | $(h,\; k \pm b)$ | $(h \pm b,\; k)$ |
| Foci | $(h \pm c,\; k)$ | $(h,\; k \pm c)$ |

The foci always lie **on the major axis**, inside the curve.

Why the minus sign? Look at the right triangle with legs $b$ and $c$ and
hypotenuse $a$, running from a focus to a co-vertex. Pythagoras gives
$a^2 = b^2 + c^2$, which rearranges to $c^2 = a^2 - b^2$. Since $a$ is the
hypotenuse, $c < a$ necessarily — and that is exactly the statement that the
foci sit inside the vertices.

![FIG-01-09-009: Main panel: an ellipse with horizontal major axis, centred at the origin. The semi-major axis a is drawn as an arrow from centre to the right vertex, the semi-minor axis b as an arrow from centre up to the co-vertex, and the focal distance c as a shorter arrow from centre to the right focus, which is marked with a filled dot inside the curve. Both foci are shown. A right triangle is drawn with legs b vertical and c horizontal and hypotenuse a running from a focus to a co-vertex, shaded and labelled 'a is the hypotenuse, so a squared equals b squared plus c squared, which rearranges to c squared equals a squared minus b squared'. A sample point on the curve has two segments drawn to the two foci, labelled with lengths that sum to 2a, annotated 'the sum of the two distances is constant and equals 2a — the string construction'. Side panel: the two standard forms shown stacked, one with a squared under x squared for a horizontal major axis and one with a squared under y squared for a vertical major axis, with a note 'a is always the larger, so the LARGER DENOMINATOR sits under the axis the ellipse is longer along'. A footer strip reads 'foci lie inside the curve, always closer to the centre than the vertices, so c is less than a'.](../figures/FIG-01-09-009-ellipse-anatomy.png)

### Area

$$A = \pi a b$$

A satisfying formula: setting $a = b = r$ recovers $\pi r^2$. The *perimeter*
of an ellipse has no closed form at all; the Handbook gives an approximation,
and Chapter 01-10 handles mensuration properly.

### Worked Example 5 — Elliptical Cross-Section

**Given.** A pressure vessel has an elliptical cross-section with horizontal
semi-major axis $a = 5$ m and semi-minor axis $b = 3$ m.

(a) Write the equation, centred at the origin.
(b) Locate the foci.
(c) Find the eccentricity.
(d) Find the cross-sectional area.

**Solution.**

**(a)** Major axis is horizontal, so $a^2 = 25$ goes under $x^2$:

$$\boxed{\frac{x^2}{25} + \frac{y^2}{9} = 1}$$

**(b)** $c^2 = a^2 - b^2 = 25 - 9 = 16$, so $c = 4$, and the foci lie on the
major axis:

$$\boxed{(\pm 4,\; 0)}$$

**(c)** $e = c/a = 4/5 = \boxed{0.80}$

**(d)** $A = \pi(5)(3) = 15\pi \approx \boxed{47.1 \text{ m}^2}$

*Checks.* At $x = 5$: $y = 0$ ✓, the vertex. At $x = 0$: $y = \pm 3$ ✓, the
co-vertices. And $c = 4 < a = 5$, so the foci are inside the curve ✓.

---

## 9.7 Hyperbolas

A **hyperbola** is the set of points for which the absolute **difference** of
distances to two foci is constant — the ellipse definition with "sum" replaced
by "difference." One word, and the closed loop becomes two branches opening
away from each other.

### Standard forms

**Horizontal transverse axis** — branches open left and right:

$$\boxed{\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1}$$

**Vertical transverse axis** — branches open up and down:

$$\boxed{\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1}$$

The rule that matters: **whichever squared term is positive names the axis the
branches open along, and its denominator is $a^2$.** For a hyperbola $a$ is
not "the bigger one" — that convention belongs to the ellipse. Here $a$ is
simply whatever sits under the positive term, and $b$ may well exceed it.

### Key parameters

$$\boxed{c^2 = a^2 + b^2}$$

| Feature | Horizontal transverse | Vertical transverse |
|---|---|---|
| Centre | $(h,k)$ | $(h,k)$ |
| Vertices | $(h \pm a,\; k)$ | $(h,\; k \pm a)$ |
| Foci | $(h \pm c,\; k)$ | $(h,\; k \pm c)$ |
| Asymptotes | $y - k = \pm\dfrac{b}{a}(x-h)$ | $y - k = \pm\dfrac{a}{b}(x-h)$ |

**Plus**, not minus, and here is why. Draw a rectangle centred at $(h,k)$,
$2a$ wide and $2b$ tall. The right triangle formed by half-width $a$ and
half-height $b$ has hypotenuse $\sqrt{a^2+b^2}$ — and that is $c$. Because $c$
is the hypotenuse this time, $c > a$ necessarily, which says the foci lie
**outside** the vertices. Compare the ellipse, where $a$ was the hypotenuse
and the foci fell inside. Same triangle, different corner labelled $c$, and
the sign follows.

### Asymptotes and how to sketch

Extend the diagonals of that rectangle and you have the asymptotes. The
branches hug them without ever touching. Practically: draw the box, draw its
diagonals, mark the vertices, and sketch each branch from its vertex out along
the diagonals.

For the horizontal form the asymptote slopes are $\pm b/a$; for the vertical
form they are $\pm a/b$. Both are "rise of the box over run of the box," so
you can read them off the sketch rather than recalling which fraction goes
where.

![FIG-01-09-010: Main panel: a hyperbola with horizontal transverse axis, both branches drawn, centred at the origin. The vertices are marked at plus and minus a on the horizontal axis, and the foci at plus and minus c, drawn beyond the vertices and labelled 'foci lie OUTSIDE the vertices, so c is greater than a'. A dashed rectangle is drawn centred at the origin with half-width a and half-height b, and the two asymptotes are drawn as dashed lines through its opposite corners, labelled with slopes plus and minus b over a, annotated 'draw the box, draw its diagonals, and the branches follow'. A right triangle is shaded inside the box with legs a and b and hypotenuse c, labelled 'c is the hypotenuse here, so c squared equals a squared PLUS b squared — the opposite arrangement from the ellipse'. Side panel: the two standard forms, x squared over a squared minus y squared over b squared equals 1 opening left and right, and y squared over a squared minus x squared over b squared equals 1 opening up and down, with a note 'whichever squared term is POSITIVE names the axis the branches open along, and its denominator is a squared'. A footer strip reads 'a sits under the positive term in both forms — it is never simply the first denominator'.](../figures/FIG-01-09-010-hyperbola-anatomy.png)

### Worked Example 6 — Cooling Tower Profile

Natural-draught cooling towers are hyperboloids of revolution: every vertical
cross-section through the axis is a hyperbola. The shape is chosen because it
accelerates the rising air while remaining a thin, stable shell.

**Given.** A tower's narrowest point — the waist — is 60 m in diameter. At
80 m above the waist the diameter is 100 m. Take the origin at the waist, $x$
horizontal, $y$ vertical.

(a) Write the equation of the cross-section.
(b) Find the diameter 40 m above the waist.
(c) Find the eccentricity.

**Solution.**

**(a)** The waist is the narrowest horizontal extent, so the branches open
left and right and the transverse axis is horizontal. The vertices sit at the
waist edges, $x = \pm 30$, giving $a = 30$:

$$\frac{x^2}{900} - \frac{y^2}{b^2} = 1$$

At $y = 80$ the diameter is 100, so $x = 50$:

$$\frac{2500}{900} - \frac{6400}{b^2} = 1 \implies \frac{6400}{b^2} = \frac{2500 - 900}{900} = \frac{1600}{900}$$

$$b^2 = \frac{6400 \times 900}{1600} = 3600 \implies b = 60$$

$$\boxed{\frac{x^2}{900} - \frac{y^2}{3600} = 1}$$

**(b)** At $y = 40$:

$$\frac{x^2}{900} = 1 + \frac{1600}{3600} = 1 + \frac{4}{9} = \frac{13}{9}$$

$$x^2 = 900 \times \frac{13}{9} = 1300 \implies x = \sqrt{1300} \approx 36.06 \text{ m}$$

Diameter $\approx \boxed{72.1 \text{ m}}$

**(c)** $c^2 = a^2 + b^2 = 900 + 3600 = 4500$, so $c = 30\sqrt5 \approx 67.1$.

$$e = \frac{c}{a} = \frac{30\sqrt5}{30} = \sqrt5 \approx \boxed{2.24}$$

*Sanity checks.* The diameter at 40 m (72.1 m) falls between the waist
diameter (60 m) and the diameter at 80 m (100 m) ✓, and it is nearer the waist
value — correct, because a hyperbola flares slowly near its vertex and then
accelerates. The eccentricity exceeds 1, as it must for any hyperbola ✓.

---

## 9.8 Eccentricity — The Thread Through All Four

Every conic carries a single number that says how far it departs from being a
circle.

$$\boxed{e = \frac{c}{a}}$$

for ellipses and hyperbolas. More generally, and this is the definition that
covers all four cases at once:

> For any point on a conic, $e$ is the ratio of its distance to the focus to
> its distance to the directrix. That ratio is the same for every point on the
> curve.

Read the parabola definition from §9.5 in that light — equidistant from focus
and directrix — and you get $e = 1$ immediately, with no calculation.

| Conic | Eccentricity | Why |
|---|---|---|
| Circle | $e = 0$ | Foci coincide with the centre, so $c = 0$ |
| Ellipse | $0 < e < 1$ | Foci inside, so $c < a$ |
| Parabola | $e = 1$ exactly | Focus and directrix distances are equal by definition |
| Hyperbola | $e > 1$ | Foci outside the vertices, so $c > a$ |

![FIG-01-09-011: A horizontal axis labelled eccentricity e, running from 0 on the left past 1 in the centre to values above 2 on the right. Four marked positions each carry a small curve sketch drawn above the axis. At e equals 0 exactly, a circle, tagged 'foci coincide with the centre, c = 0'. Across the open interval from 0 to 1, three ellipse sketches of increasing elongation are shown left to right, the leftmost nearly circular and the rightmost strongly flattened, tagged 'the closer e gets to 1, the more elongated', with e = c over a printed beneath. At e equals 1 exactly, a parabola, tagged 'the boundary case — the curve no longer closes'. To the right of 1, two hyperbola sketches are shown, the one nearer 1 with narrow branches and the one further right with wide branches, tagged 'branches open wider as e grows', with e = c over a printed beneath. Beneath the whole axis a single unifying statement is printed: for any conic, e equals the distance from a point on the curve to the focus divided by the distance from that point to the directrix. A footer note reads 'one number orders all four shapes, and it matches the tilt of the cone cut'.](../figures/FIG-01-09-011-eccentricity-spectrum.png)

> ---
> **Mentor's Margin**
>
> Eccentricity is the payoff for treating the conics as one family. It is a
> continuum, not four boxes: push an ellipse's eccentricity toward 1 and it
> flattens until, at exactly 1, it stops closing and becomes a parabola; push
> past 1 and it splits into hyperbola branches. That is the same progression as
> tilting the cutting plane in §9.3, now expressed as a number.
>
> One genuine use on the exam: eccentricity is a fast consistency check. Work
> out $e = 1.4$ for something you have called an ellipse and you have made an
> error — either in the arithmetic or in the identification.
>
> And once more: this $e$ is not $2.718\ldots$
>
> ---

---

## 9.9 Identifying a Conic from Its Equation

The general second-degree equation in two variables:

$$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$$

### When there is no $xy$ term ($B = 0$)

This is nearly every exam case, and classification takes seconds:

| Condition on $A$ and $C$ | Conic |
|---|---|
| Exactly one of them is zero | **Parabola** |
| Opposite signs | **Hyperbola** |
| Same sign, equal values | **Circle** |
| Same sign, different values | **Ellipse** |

Work down the list in that order. Look for a zero first, then compare signs,
then compare magnitudes.

![FIG-01-09-012: A flowchart starting from the general second-degree equation A x squared plus B x y plus C y squared plus D x plus E y plus F equals 0. First decision diamond: is there an x y term, B not equal to zero. The yes branch leads to a side box reading 'the conic is rotated; classify by the discriminant B squared minus 4AC — positive gives hyperbola, zero gives parabola, negative gives ellipse or circle', tagged 'rare on the exam'. The no branch continues to a second decision diamond: is exactly one of A or C zero. Its yes branch leads to a box 'PARABOLA — one squared term only', with a caution tag 'if the matching linear term is also zero the result is degenerate, a pair of lines or nothing'. Its no branch reaches a third diamond: do A and C have the same sign. The no branch leads to 'HYPERBOLA — opposite signs'. The yes branch reaches a fourth diamond: does A equal C. Its yes branch leads to 'CIRCLE — equal coefficients', its no branch to 'ELLIPSE — same sign, different magnitude'. A terminal strip beneath the circle and ellipse boxes reads 'then complete the square in each variable to find the centre; a right side that comes out zero is a single point and a negative right side is no graph at all'. A footer note reads 'classify first, complete the square second — knowing the shape tells you what parameters to go looking for'.](../figures/FIG-01-09-012-conic-identification-flowchart.png)

### When there is an $xy$ term ($B \ne 0$)

The conic is rotated relative to the axes. Classify with the **discriminant**:

$$B^2 - 4AC \quad \begin{cases} > 0 & \text{hyperbola} \\ = 0 & \text{parabola} \\ < 0 & \text{ellipse or circle} \end{cases}$$

This appears in the Handbook. It is uncommon on the exam, and you are not
expected to find the rotation angle — only to name the shape.

### Then complete the square

Classification tells you *what* to look for; completing the square finds it.
For a hyperbola you want the centre, $a$, $b$, and the asymptotes. For an
ellipse, the centre and both semi-axes. Doing these in the other order wastes
effort, because you won't know which parameters matter.

### Worked Example 7 — Full Identification

**Given.** Identify and fully characterize:

$$4x^2 - 9y^2 + 8x + 36y - 68 = 0$$

**Solution.**

**Step 1 — Classify.** No $xy$ term. $A = 4$ and $C = -9$ have **opposite
signs** → **hyperbola**. Now I know to go looking for a centre, $a$, $b$, and
asymptotes.

**Step 2 — Group and factor out the leading coefficients.**

$$4(x^2 + 2x) - 9(y^2 - 4y) = 68$$

**Step 3 — Complete each square, tracking what the factored coefficients do
to the right side.** Adding 1 inside the first bracket adds $4(1) = 4$ to the
left; adding 4 inside the second adds $-9(4) = -36$:

$$4(x^2 + 2x + 1) - 9(y^2 - 4y + 4) = 68 + 4 - 36$$

$$4(x+1)^2 - 9(y-2)^2 = 36$$

**Step 4 — Divide through to make the right side 1.**

$$\boxed{\frac{(x+1)^2}{9} - \frac{(y-2)^2}{4} = 1}$$

**Step 5 — Read off the parameters.** The positive term is in $x$, so the
transverse axis is horizontal and $a^2 = 9$:

- Centre $(-1, 2)$
- $a = 3$, $b = 2$
- Vertices $(-1 \pm 3,\; 2)$, i.e. $(2, 2)$ and $(-4, 2)$
- $c^2 = 9 + 4 = 13$, so $c = \sqrt{13} \approx 3.61$
- Foci $(-1 \pm \sqrt{13},\; 2)$
- Asymptotes $y - 2 = \pm\tfrac{2}{3}(x+1)$
- $e = c/a = \sqrt{13}/3 \approx 1.20$

*Checks.* $c > a$ ✓, as required for a hyperbola. $e > 1$ ✓, consistent.
And substituting the vertex $(2,2)$ into the original equation:
$4(4) - 9(4) + 8(2) + 36(2) - 68 = 16 - 36 + 16 + 72 - 68 = 0$ ✓

> ---
> **Mentor's Margin**
>
> Step 3 is where this goes wrong for most people. When you factor a
> coefficient out front, the constant you add *inside* the bracket gets
> multiplied by that coefficient before it lands on the right side. Adding 4
> inside a bracket multiplied by $-9$ contributes $-36$, not $+4$ and not
> $-9$.
>
> The safest habit: write the multiplication out explicitly on the right side
> before combining, as I did above. Two extra symbols, and it removes the
> most error-prone step in the chapter.
>
> ---

---

## As the Handbook States It

> **Handbook 10.6, pp. 37–40** — *Mathematics / Analytic Geometry*

The Handbook provides:

- Straight-line equations in all three forms, with slope relationships
- The angle between two lines
- Distance from a point to a line
- The distance formula
- Standard-form equations for circle, parabola, ellipse, and hyperbola, with
  their parameter relations
- Eccentricity definitions
- The $B^2 - 4AC$ discriminant for rotated conics

**The Handbook does not provide:**

- Any derivation from the focus-directrix definitions
- The procedure for completing the square
- Rules for classifying a general equation by inspecting $A$ and $C$
- How to find a conic from geometric conditions — a circle through three
  points, a parabola from vertex and a passing point, and so on
- The reflective property of the parabola

Those are memorize-and-practise material. Note the pattern, which holds across
the whole Handbook: it stores **formulas**, not **methods**. Anything
procedural has to come from you.

**Notation note.** The Handbook uses $(h,k)$ for centres and vertices, $a \ge b$
for the ellipse, and $c^2 = a^2 - b^2$ for ellipses against $c^2 = a^2 + b^2$
for hyperbolas — all matching this chapter. Match its notation in final
answers.

**A caveat on page numbers.** Section and page references track the Handbook
edition. Verify them against the version you will actually sit with, since
NCEES renumbers between editions.

---

## Where This Goes Wrong

**Using $c^2 = a^2 - b^2$ for a hyperbola.** Ellipse subtracts, hyperbola
adds. If you can only hold one of them, hold the reason: for an ellipse $a$ is
the hypotenuse of the $a$-$b$-$c$ triangle, so $c$ comes out smaller and the
foci sit inside. For a hyperbola $c$ is the hypotenuse, so $c$ comes out larger
and the foci sit outside.

**Reading the right side of a circle equation as $r$.** In
$(x-h)^2 + (y-k)^2 = 25$ the radius is 5.

**Flipping the sign of the centre.** $(x+5)^2 + (y-3)^2 = 4$ has centre
$(-5, 3)$. The standard form contains minus signs, so a visible plus means a
negative coordinate.

**Completing the square on one side only.** Whatever you add on the left must
be added on the right.

**Forgetting that a factored-out coefficient multiplies what you add.** In
$-9(y^2 - 4y)$, adding 4 inside contributes $-36$ to the right side. See Worked
Example 7.

**Failing to divide through when $x^2$ and $y^2$ coefficients aren't 1.**
$2x^2 + 2y^2 - 12x + 8y - 24 = 0$ must be divided by 2 before completing the
square.

**Assuming $a > b$ for a hyperbola.** That convention is the ellipse's. For a
hyperbola, $a^2$ is whatever sits under the **positive** term, and $b$ may be
larger.

**Taking the major axis from term order rather than denominator size.** In
$x^2/9 + y^2/25 = 1$ the major axis is **vertical**, because 25 > 9. Position
in the equation means nothing.

**Getting a parabola's direction backwards.** It opens toward the focus, away
from the directrix. Locate the focus from the sign of $p$ and the direction
follows — you never need to recall four separate sign rules.

**Using $c^2 = a^2 - b^2$ on a hyperbola.** Ellipse: minus. Hyperbola: plus.
The reliable way to keep them apart is the triangle. For an ellipse $a$ is the
hypotenuse, so $c$ comes out smaller than $a$ and the foci fall inside the
vertices. For a hyperbola $c$ is the hypotenuse, so $c$ comes out larger than
$a$ and the foci fall outside. Draw the triangle, see which side is longest,
and the sign is decided.

**Assuming $a$ is the larger denominator on a hyperbola.** That convention
belongs to the ellipse alone. On a hyperbola, $a^2$ is whatever sits under the
**positive** term, and $b$ may easily be larger. In
$\frac{y^2}{4} - \frac{x^2}{21} = 1$ you have $a = 2$ and $b = \sqrt{21}$, and
reading $a$ as the bigger number puts the vertices, foci, and asymptotes all
in the wrong places at once.

**Identifying an ellipse's major axis from the order of the terms.** It is set
by the **larger denominator**, not by which variable is written first. In
$\frac{x^2}{9} + \frac{y^2}{25} = 1$ the major axis is vertical, despite $x$
appearing first.

**Forgetting to divide through when the squared coefficients aren't 1.** Before
completing the square on $2x^2 + 2y^2 - 12x + 8y - 24 = 0$, divide the whole
equation by 2. Completing the square with a coefficient still attached gives a
wrong centre and a wrong radius.

**Dropping the absolute value in the point-to-line distance formula.** The
expression inside is negative for every point on one side of the line.
Distance is not.

**Feeding slope-intercept form into the point-to-line distance formula.** It
needs $Ax + By + C = 0$, with everything collected on one side. Rearrange
first.

**Reading the centre with the wrong signs.** $(x+5)^2 + (y-2)^2 = 36$ has
centre $(-5, +2)$. The standard form is written with minus signs, so the
values that appear are already negated.

**Treating a degenerate result as an error.** After completing the square, a
right-hand side of zero means a single point, and a negative right-hand side
means no graph at all. Both are legitimate answers. Taking the square root of
a negative right side to force a radius out of it is not.

**Assuming every hanging cable is a parabola.** A cable under a load
distributed uniformly along the *horizontal span* hangs in a parabola. A cable
carrying only its own weight hangs in a catenary. The two are close for shallow
sags and genuinely different for deep ones.

---

## Key Terms

| Term | Definition |
|---|---|
| Slope | Rise over run, $m = (y_2-y_1)/(x_2-x_1)$; undefined for a vertical line |
| Slope-intercept form | $y = mx + b$ |
| Point-slope form | $y - y_1 = m(x - x_1)$ |
| General form (line) | $Ax + By + C = 0$; the only form that expresses a vertical line |
| Parallel lines | Equal slopes, $m_1 = m_2$ |
| Perpendicular lines | Negative reciprocal slopes, $m_1m_2 = -1$ |
| Point-to-line distance | $d = \lvert Ax_0+By_0+C\rvert / \sqrt{A^2+B^2}$; the perpendicular distance |
| Distance formula | $d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$; Pythagoras in coordinates |
| Midpoint | The coordinate-wise average of two points |
| Conic section | A curve formed by slicing a double cone with a plane |
| Circle | $(x-h)^2+(y-k)^2=r^2$; points at constant distance from a centre |
| Degenerate conic | A point, a line, a line pair, or no graph — what a conic equation gives when its parameters collapse |
| Parabola | $(x-h)^2=4p(y-k)$ or $(y-k)^2=4p(x-h)$; points equidistant from a focus and a directrix |
| Focus | The fixed point in a conic's defining condition |
| Directrix | The fixed line in the parabola's defining condition |
| $p$ (parabola) | Directed distance from vertex to focus; its sign gives the opening direction |
| Axis of symmetry | The line through the vertex about which a parabola is symmetric |
| Ellipse | $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$; the **sum** of distances to two foci is constant, equal to $2a$ |
| Semi-major axis $a$ | Half the longer axis of an ellipse; always the larger of $a$ and $b$ |
| Semi-minor axis $b$ | Half the shorter axis of an ellipse |
| Focal distance $c$ | Centre-to-focus distance; $c^2 = a^2-b^2$ (ellipse), $c^2 = a^2+b^2$ (hyperbola) |
| Hyperbola | $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$; the absolute **difference** of distances to two foci is constant |
| Transverse axis | The axis of a hyperbola through both vertices and both foci |
| Asymptote | A line the hyperbola approaches without reaching; the diagonals of the central box |
| Eccentricity $e$ | $c/a$; orders the conics — $0$ circle, $0<e<1$ ellipse, $e=1$ parabola, $e>1$ hyperbola |
| Completing the square | The technique that converts a general second-degree equation to standard form |

---

## Review Questions

### Conceptual

1. Describe how each of the four conic sections arises as a slice of a double
   cone. What single property of the cutting plane determines which one you
   get?

2. Explain why the slope of a perpendicular line is the *negative reciprocal*
   rather than just the negative. Your answer should account for both the
   reciprocal and the minus sign.

3. In $(x-h)^2 = 4p(y-k)$, what does the sign of $p$ determine, and what single
   sentence lets you get it right without memorizing separate cases?

4. An ellipse has $c^2 = a^2 - b^2$ and a hyperbola has $c^2 = a^2 + b^2$.
   Explain the difference using the right triangle in each case, and say what
   it implies about where the foci sit relative to the vertices.

5. Define eccentricity, and state its value or range for each of the four
   conics. Why does a single number manage to order all four?

6. A satellite dish has a parabolic cross-section. Why must the receiver sit
   at the focus and nowhere else?

7. After completing the square on a circle equation you get
   $(x-2)^2 + (y+1)^2 = 0$. What is the graph? What if the right-hand side had
   been $-4$?

8. For the ellipse, $a$ is by convention the larger of $a$ and $b$. Explain why
   that convention does **not** carry over to the hyperbola, and state what
   identifies $a$ there instead.

### Calculation

9. Find the equation of each line:
   (a) Through $(-1, 3)$ and $(4, -7)$
   (b) Through $(5, 2)$ with slope $-\tfrac{3}{4}$
   (c) Through $(2, 6)$ parallel to $3x - 2y = 8$
   (d) Through $(2, 6)$ perpendicular to $3x - 2y = 8$

10. Find the distance and the midpoint:
    (a) Between $(-3, 4)$ and $(5, -2)$
    (b) Between $(0, 0)$ and $(7, 24)$
    (c) Between $(1, -2, 3)$ and $(4, 2, 15)$ — distance only

11. Find the distance from the point to the line:
    (a) $(1, 2)$ and $4x + 3y - 10 = 0$
    (b) $(-2, 5)$ and $x - 2y + 3 = 0$
    (c) $(12, 9)$ and $3x + 4y - 24 = 0$

12. Convert to standard form and state the centre and radius:
    (a) $x^2 + y^2 - 8x + 6y + 16 = 0$
    (b) $x^2 + y^2 + 10x - 4y - 7 = 0$
    (c) $2x^2 + 2y^2 - 12x + 8y - 24 = 0$
    (d) $x^2 + y^2 - 4x + 2y + 5 = 0$

13. Find the equation of the circle:
    (a) Centre $(4, -3)$, radius $\sqrt{7}$
    (b) Centre $(-2, 1)$, passing through $(3, 5)$
    (c) Diameter endpoints $(-4, 2)$ and $(6, -8)$
    (d) Through $(0,0)$, $(4,0)$, and $(0,-6)$

14. Convert to standard form, name the conic, and give the centre or vertex
    plus all key parameters:
    (a) $y^2 - 8x - 6y + 17 = 0$
    (b) $4x^2 + 9y^2 - 16x + 18y - 11 = 0$
    (c) $9x^2 - 4y^2 + 36x + 8y - 4 = 0$

15. Find the equation of the parabola:
    (a) Vertex $(0,0)$, focus $(0,-3)$
    (b) Vertex $(2,-1)$, opening right, passing through $(6, 3)$
    (c) Focus $(0, 5)$, directrix $y = -5$

16. Find the equation of the ellipse, and its eccentricity:
    (a) Centre $(0,0)$, vertices $(\pm 6, 0)$, co-vertices $(0, \pm 4)$
    (b) Centre $(1,-2)$, $a = 5$ horizontal, $b = 3$
    (c) Foci $(0, \pm 4)$, major vertices $(0, \pm 5)$

17. Find the equation of the hyperbola, plus its foci and eccentricity:
    (a) Centre $(0,0)$, vertices $(\pm 3, 0)$, asymptotes $y = \pm\tfrac{4}{3}x$
    (b) Centre $(0,0)$, vertices $(0, \pm 2)$, foci $(0, \pm 5)$

18. Classify each by inspection, **without** completing the square:
    (a) $3x^2 + 3y^2 - 12x + 6y - 1 = 0$
    (b) $x^2 + 5y^2 + 2x - 20y = 0$
    (c) $2x^2 - 7y^2 + 4x = 9$
    (d) $y^2 + 6x - 4y + 10 = 0$
    (e) $x^2 + y^2 + 2x - 4y + 9 = 0$

19. **Engineering.** A parabolic arch bridge is 40 m wide at its base and 10 m
    high at the centre. Put the origin at the crown.
    (a) Write the equation of the arch.
    (b) Find the height of the arch 8 m horizontally from the centre.
    (c) At what horizontal distance from the centre is the arch exactly 6 m
    high?
    (d) Where is the focus?

20. **Engineering.** A tunnel has a semi-elliptical cross-section, 10 m wide at
    the road surface and 4 m high at the crown. Put the origin at the midpoint
    of the road surface.
    (a) Write the equation, with its domain restriction.
    (b) A truck is 3.2 m wide. What is the greatest height that clears the
    tunnel at the truck's outer edge?
    (c) A vehicle is 3.5 m tall. What is the greatest width that clears?

### Multiple Choice

21. The slope of a line perpendicular to $2x - 5y = 10$ is:
    A) $\tfrac{2}{5}$  B) $-\tfrac{2}{5}$  C) $\tfrac{5}{2}$  D) $-\tfrac{5}{2}$

22. The centre of the circle $x^2 + y^2 - 4x + 6y = 3$ is:
    A) $(2, -3)$  B) $(-2, 3)$  C) $(4, -6)$  D) $(-4, 6)$

23. Which equation represents a parabola?
    A) $x^2 + y^2 = 16$  B) $x^2 + 4y^2 = 16$  C) $x^2 - y^2 = 16$
    D) $x^2 - 4y = 16$

24. The foci of $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ are at:
    A) $(\pm 5, 0)$  B) $(0, \pm 4)$  C) $(\pm 3, 0)$  D) $(0, \pm 3)$

25. For $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$, the asymptotes are:
    A) $y = \pm\tfrac{3}{4}x$  B) $y = \pm\tfrac{4}{3}x$
    C) $y = \pm\tfrac{9}{16}x$  D) $y = \pm 3x$

26. A circle has diameter endpoints $(1, 3)$ and $(7, -1)$. Its centre is:
    A) $(3, 1)$  B) $(4, 1)$  C) $(4, -1)$  D) $(8, 2)$

27. The distance from $(0,0)$ to the line $3x + 4y - 15 = 0$ is:
    A) $3$  B) $5$  C) $15$  D) $\sqrt{15}$

28. The eccentricity of a parabola is:
    A) $0$  B) between $0$ and $1$  C) exactly $1$  D) greater than $1$

29. For $\dfrac{y^2}{16} - \dfrac{x^2}{9} = 1$, the vertices are at:
    A) $(\pm 4, 0)$  B) $(0, \pm 4)$  C) $(\pm 3, 0)$  D) $(0, \pm 3)$

30. Completing the square on a second-degree equation gives
    $(x-1)^2 + (y+2)^2 = -9$. The graph is:
    A) A circle of radius $3$  B) A circle of radius $9$
    C) The single point $(1,-2)$  D) Nothing — no points satisfy it

---

## Answer Key with Explanations

**1.** Slice a double cone with a plane. Perpendicular to the axis gives a
**circle**; a moderate tilt gives an **ellipse**; a tilt exactly parallel to
the cone's side gives a **parabola**; a tilt steep enough to cut both halves
gives a **hyperbola** in two branches. The single determining property is the
**tilt of the cutting plane** relative to the cone's side. (§9.3)

**2.** A slope is a triangle with run $a$ and rise $b$, so $m = b/a$. Rotating
that triangle a quarter turn sends the run to the rise position and the rise to
the run position, which produces the **reciprocal**; and the run reverses
direction in doing so, which produces the **minus sign**. The rotated slope is
$a/(-b) = -1/m$. Negating alone gives $-b/a$, which is a reflection, not a
rotation — a different line entirely, and not perpendicular. (§9.1)

**3.** The sign of $p$ determines the **opening direction**: $p > 0$ opens up
(vertical case) or right (horizontal case), $p < 0$ opens down or left. The
sentence that replaces all four rules: **the parabola opens toward the focus
and away from the directrix.** Since the focus sits at $(h, k+p)$, the sign of
$p$ places the focus, and the curve follows it. (§9.5)

**4.** **Ellipse:** the right triangle has legs $b$ and $c$ and hypotenuse $a$,
running from a focus to a co-vertex. So $a^2 = b^2 + c^2$, giving
$c^2 = a^2 - b^2$. Because $a$ is the hypotenuse, $c < a$ — the foci lie
**inside** the vertices. **Hyperbola:** the triangle has legs $a$ and $b$ with
$c$ as the hypotenuse, so $c^2 = a^2 + b^2$ and $c > a$ — the foci lie
**outside** the vertices. Same triangle, different side labelled $c$. (§9.6,
§9.7)

**5.** $e = c/a$. Circle $e = 0$ (the foci coincide with the centre, so
$c = 0$); ellipse $0 < e < 1$; parabola $e = 1$ exactly; hyperbola $e > 1$. One
number manages it because all four are slices of the same cone, and $e$ is a
direct measure of the cutting plane's tilt. Equivalently, for every conic $e$
is the ratio of the distance from a point on the curve to the focus over the
distance from that point to the directrix — one definition, four outcomes.
(§9.8)

**6.** By the reflective property, every ray arriving parallel to the axis
reflects through the focus. The focus is the unique point at which all that
incoming parallel energy converges, so a receiver anywhere else collects only a
fraction of it. The property is a consequence of the focus-directrix
definition, not an accident of the shape. (§9.5)

**7.** $(x-2)^2 + (y+1)^2 = 0$ requires both squares to vanish at once, so the
graph is the **single point** $(2,-1)$. With $-4$ on the right there is **no
graph at all** — a sum of two squares cannot be negative. Both are degenerate
cases, and neither is an arithmetic error. (§9.4)

**8.** For an ellipse the two axes are unambiguously longer and shorter, so
naming the longer one $a$ costs nothing. A hyperbola has no "longer axis" of
that kind: one direction contains the vertices and the other does not, and the
box half-dimensions $a$ and $b$ are unrelated in size. What identifies $a$ is
that **$a^2$ sits under the positive term**. In
$\frac{y^2}{4} - \frac{x^2}{21} = 1$, $a = 2$ and $b = \sqrt{21} \approx 4.58$.
(§9.7)

**9.**

(a) $m = \dfrac{-7-3}{4-(-1)} = \dfrac{-10}{5} = -2$; through $(-1,3)$:
$y - 3 = -2(x+1)$

$$\boxed{y = -2x + 1}$$

*Check at $(4,-7)$:* $-8 + 1 = -7$ ✓

(b) $y - 2 = -\tfrac{3}{4}(x-5) \implies y = -\tfrac{3}{4}x + \tfrac{15}{4} + 2$

$$\boxed{y = -\tfrac{3}{4}x + \tfrac{23}{4}}$$

*Check at $x = 5$:* $-\tfrac{15}{4} + \tfrac{23}{4} = 2$ ✓

(c) $3x - 2y = 8 \implies y = \tfrac{3}{2}x - 4$, so $m = \tfrac{3}{2}$.
Parallel through $(2,6)$: $y - 6 = \tfrac{3}{2}(x-2)$

$$\boxed{y = \tfrac{3}{2}x + 3}$$

(d) Perpendicular slope $-\tfrac{2}{3}$: $y - 6 = -\tfrac{2}{3}(x-2)$

$$\boxed{y = -\tfrac{2}{3}x + \tfrac{22}{3}}$$

*Check:* $\tfrac{3}{2} \times \left(-\tfrac{2}{3}\right) = -1$ ✓, and at
$x = 2$, $y = -\tfrac{4}{3} + \tfrac{22}{3} = 6$ ✓

**10.**

(a) $d = \sqrt{8^2 + (-6)^2} = \sqrt{64+36} = \boxed{10}$;
$M = \left(\tfrac{-3+5}{2}, \tfrac{4-2}{2}\right) = \boxed{(1,1)}$

(b) $d = \sqrt{49 + 576} = \sqrt{625} = \boxed{25}$; $M = \boxed{(3.5,\, 12)}$

(c) Differences $3$, $4$, $12$:
$d = \sqrt{9 + 16 + 144} = \sqrt{169} = \boxed{13}$

**11.**

(a) $d = \dfrac{\lvert 4(1)+3(2)-10 \rvert}{\sqrt{16+9}} = \dfrac{0}{5} = \boxed{0}$

A numerator of zero is not an error — the point **lies on** the line. Confirm:
$4 + 6 - 10 = 0$ ✓

(b) $d = \dfrac{\lvert -2 - 10 + 3 \rvert}{\sqrt{1+4}} = \dfrac{9}{\sqrt 5} = \dfrac{9\sqrt 5}{5} \approx \boxed{4.02}$

(c) $d = \dfrac{\lvert 36 + 36 - 24 \rvert}{\sqrt{9+16}} = \dfrac{48}{5} = \boxed{9.6}$

**12.**

(a) $(x^2-8x) + (y^2+6y) = -16$; add $16$ and $9$ to both sides:

$$(x-4)^2 + (y+3)^2 = -16 + 16 + 9 = 9$$

$$\boxed{\text{Centre } (4,-3), \; r = 3}$$

(b) $(x^2+10x) + (y^2-4y) = 7$; add $25$ and $4$:

$$(x+5)^2 + (y-2)^2 = 36 \implies \boxed{\text{Centre } (-5,2), \; r = 6}$$

(c) **Divide by 2 first:** $x^2 + y^2 - 6x + 4y - 12 = 0$. Then add $9$ and
$4$:

$$(x-3)^2 + (y+2)^2 = 25 \implies \boxed{\text{Centre } (3,-2), \; r = 5}$$

(d) $(x^2-4x) + (y^2+2y) = -5$; add $4$ and $1$:

$$(x-2)^2 + (y+1)^2 = -5 + 4 + 1 = 0$$

$$\boxed{\text{Degenerate — the single point } (2,-1)}$$

**13.**

(a) $\boxed{(x-4)^2 + (y+3)^2 = 7}$

(b) $r = \sqrt{(3+2)^2 + (5-1)^2} = \sqrt{25+16} = \sqrt{41}$

$$\boxed{(x+2)^2 + (y-1)^2 = 41}$$

(c) Centre is the midpoint: $\left(\tfrac{-4+6}{2}, \tfrac{2-8}{2}\right) = (1,-3)$.
Radius is half the diameter:
$r = \tfrac{1}{2}\sqrt{100+100} = \tfrac{1}{2}\left(10\sqrt2\right) = 5\sqrt2$,
so $r^2 = 50$.

$$\boxed{(x-1)^2 + (y+3)^2 = 50}$$

(d) From $x^2+y^2+Dx+Ey+F = 0$. At $(0,0)$: $F = 0$. At $(4,0)$:
$16 + 4D = 0 \implies D = -4$. At $(0,-6)$: $36 - 6E = 0 \implies E = 6$.

$$x^2+y^2-4x+6y = 0 \implies (x-2)^2+(y+3)^2 = 4 + 9 = 13$$

$$\boxed{(x-2)^2 + (y+3)^2 = 13, \quad \text{centre } (2,-3), \; r = \sqrt{13}}$$

*Second route:* the three points form a right angle at the origin, so the
segment from $(4,0)$ to $(0,-6)$ is a diameter. Its length is
$\sqrt{16+36} = \sqrt{52} = 2\sqrt{13}$, giving $r = \sqrt{13}$ ✓, and its
midpoint is $(2,-3)$ ✓

**14.**

(a) Only $y$ is squared, so a parabola with horizontal axis. Group the
$y$-terms:

$$(y^2 - 6y) = 8x - 17 \implies (y-3)^2 - 9 = 8x - 17 \implies (y-3)^2 = 8(x-1)$$

**Parabola.** Vertex $(1,3)$; $4p = 8$ so $p = 2$; opens **right**; focus
$(3,3)$; directrix $x = -1$; axis $y = 3$; $e = 1$.

(b) Both squared, same sign, unequal coefficients — an ellipse.

$$4(x^2-4x) + 9(y^2+2y) = 11$$
$$4\left[(x-2)^2 - 4\right] + 9\left[(y+1)^2 - 1\right] = 11$$
$$4(x-2)^2 + 9(y+1)^2 = 11 + 16 + 9 = 36$$
$$\frac{(x-2)^2}{9} + \frac{(y+1)^2}{4} = 1$$

**Ellipse.** Centre $(2,-1)$; $a = 3$ horizontal, $b = 2$; vertices
$(5,-1)$ and $(-1,-1)$; co-vertices $(2,1)$ and $(2,-3)$;
$c^2 = 9-4 = 5$, $c = \sqrt5 \approx 2.236$; foci $(2 \pm \sqrt5,\, -1)$;
$e = \sqrt5/3 \approx 0.745$; area $= \pi(3)(2) = 6\pi \approx 18.8$.

(c) Opposite signs — a hyperbola. Watch the sign when factoring $-4$ out of the
$y$-terms:

$$9(x^2+4x) - 4(y^2-2y) = 4$$
$$9\left[(x+2)^2-4\right] - 4\left[(y-1)^2-1\right] = 4$$
$$9(x+2)^2 - 36 - 4(y-1)^2 + 4 = 4$$
$$9(x+2)^2 - 4(y-1)^2 = 36$$
$$\frac{(x+2)^2}{4} - \frac{(y-1)^2}{9} = 1$$

**Hyperbola.** Centre $(-2,1)$; the positive term is in $x$, so the transverse
axis is horizontal with $a = 2$, $b = 3$; vertices $(0,1)$ and $(-4,1)$;
$c^2 = 4+9 = 13$, $c = \sqrt{13} \approx 3.606$; foci
$(-2 \pm \sqrt{13},\, 1)$; asymptotes $y - 1 = \pm\tfrac{3}{2}(x+2)$;
$e = \sqrt{13}/2 \approx 1.803$.

Note $b > a$ here, which is entirely normal for a hyperbola.

**15.**

(a) Focus below the vertex, so vertical axis with $p = -3$:

$$x^2 = 4(-3)y \implies \boxed{x^2 = -12y}$$

(b) Opens right from vertex $(2,-1)$: $(y+1)^2 = 4p(x-2)$. Through $(6,3)$:

$$(3+1)^2 = 4p(6-2) \implies 16 = 16p \implies p = 1$$

$$\boxed{(y+1)^2 = 4(x-2)}$$

Focus $(3,-1)$, directrix $x = 1$. *Check at $(6,3)$:* $16 = 4(4)$ ✓

(c) The vertex is halfway between focus and directrix, at $(0,0)$, and
$p = 5$:

$$\boxed{x^2 = 20y}$$

**16.**

(a) $a = 6$ horizontal, $b = 4$:

$$\boxed{\frac{x^2}{36} + \frac{y^2}{16} = 1}$$

$c^2 = 36-16 = 20$, $c = 2\sqrt5 \approx 4.47$;
$e = 2\sqrt5/6 = \sqrt5/3 \approx \boxed{0.745}$

(b) $$\boxed{\frac{(x-1)^2}{25} + \frac{(y+2)^2}{9} = 1}$$

$c^2 = 25-9 = 16$, $c = 4$; foci $(1\pm4,\,-2)$, i.e. $(5,-2)$ and $(-3,-2)$;
$e = 4/5 = \boxed{0.80}$

(c) Foci and vertices both on the $y$-axis, so the major axis is **vertical**
with $a = 5$ and $c = 4$, giving $b^2 = 25-16 = 9$:

$$\boxed{\frac{x^2}{9} + \frac{y^2}{25} = 1}, \qquad e = \frac{4}{5} = \boxed{0.80}$$

Note the larger denominator sits under $y^2$ even though $x$ is written first.

**17.**

(a) $a = 3$, transverse axis horizontal. Asymptote slope $b/a = 4/3$ gives
$b = 4$:

$$\boxed{\frac{x^2}{9} - \frac{y^2}{16} = 1}$$

$c^2 = 9+16 = 25$, $c = 5$; foci $\boxed{(\pm5,\,0)}$;
$e = 5/3 \approx \boxed{1.667}$

(b) Vertices and foci on the $y$-axis, so the positive term is $y^2$ with
$a = 2$; $c = 5$ gives $b^2 = 25-4 = 21$:

$$\boxed{\frac{y^2}{4} - \frac{x^2}{21} = 1}$$

Foci $(0,\pm5)$; asymptotes $y = \pm\tfrac{2}{\sqrt{21}}x \approx \pm 0.436x$;
$e = 5/2 = \boxed{2.5}$

Here $b = \sqrt{21} \approx 4.58$ exceeds $a = 2$ — the ellipse convention does
not apply.

**18.**

(a) $A = C = 3$ → **circle** (or a degenerate point/empty set)
(b) $A = 1$, $C = 5$, same sign but unequal → **ellipse**
(c) $A = 2$, $C = -7$, opposite signs → **hyperbola**
(d) $A = 0$, $C = 1$, exactly one squared term, and the $x$ term survives →
**parabola**
(e) $A = C = 1$ suggests a circle, but completing the square gives
$(x+1)^2+(y-2)^2 = -9+1+4 = -4$ → **no graph**, a degenerate case

(§9.9)

**19.**

(a) Vertex at the crown, so the parabola opens **downward** with vertex
$(0,0)$. The base is 40 m wide and 10 m below the crown, giving the points
$(\pm 20,\, -10)$. From $x^2 = 4py$:

$$(20)^2 = 4p(-10) \implies 400 = -40p \implies p = -10$$

$$\boxed{x^2 = -40y}$$

(b) At $x = 8$: $64 = -40y \implies y = -1.6$ m, i.e. 1.6 m below the crown.

$$\text{Height} = 10 - 1.6 = \boxed{8.4 \text{ m}}$$

(c) Height 6 m means $y = -(10-6) = -4$:

$$x^2 = -40(-4) = 160 \implies x = 4\sqrt{10} \approx \boxed{12.6 \text{ m}}$$

(d) $p = -10$, so the focus is 10 m **below** the crown at $\boxed{(0,-10)}$ —
which happens to be exactly at road level here.

*Checks.* At $x = 0$, $y = 0$ (the crown) ✓. At $x = 20$, $y = -10$ (the
base) ✓. Part (b) gives 8.4 m, less than the 10 m crown height and more than
zero ✓. Part (c) gives 12.6 m, which sits between the 8 m of part (b) and the
20 m half-span, consistent with height falling as you move outward ✓.

**20.**

(a) Semi-axes: horizontal $a = 10/2 = 5$ m, vertical $b = 4$ m. Only the upper
half is tunnel:

$$\boxed{\frac{x^2}{25} + \frac{y^2}{16} = 1, \quad y \ge 0}$$

(b) The truck's edge is at $x = 1.6$ m:

$$\frac{(1.6)^2}{25} + \frac{y^2}{16} = 1 \implies \frac{2.56}{25} = 0.1024$$

$$\frac{y^2}{16} = 0.8976 \implies y^2 = 14.362 \implies y = \boxed{3.79 \text{ m}}$$

(c) Set $y = 3.5$:

$$\frac{x^2}{25} + \frac{12.25}{16} = 1 \implies \frac{x^2}{25} = 1 - 0.765625 = 0.234375$$

$$x^2 = 5.8594 \implies x = 2.42 \text{ m}$$

Width is $2x = \boxed{4.84 \text{ m}}$

*Checks.* At $x = 0$: $y = 4$ m, the full crown height ✓. At $x = 5$: $y = 0$,
the road surface at the tunnel wall ✓. In (b), 3.79 m is just under the 4 m
crown, which is right for an edge only 32 % of the way out ✓. In (c), the
available width at 3.5 m height is 4.84 m, comfortably less than the 10 m at
road level ✓. Real clearance design would subtract a safety margin from both
answers.

**21. D — $-\tfrac{5}{2}$.** $2x-5y = 10$ gives $y = \tfrac{2}{5}x - 2$, so
$m = \tfrac{2}{5}$ and the negative reciprocal is $-\tfrac{5}{2}$. (B) negates
without taking the reciprocal; (C) takes the reciprocal without negating.
(§9.1)

**22. A — $(2,-3)$.** $(x^2-4x)+(y^2+6y) = 3$, so
$(x-2)^2+(y+3)^2 = 3+4+9 = 16$. Centre $(2,-3)$, radius 4. (B) fails to flip
the signs from the standard form. (§9.4)

**23. D — $x^2 - 4y = 16$.** Rearranged, $x^2 = 4(y+4)$ — one squared term
only. (A) is a circle, (B) an ellipse, (C) a hyperbola. (§9.9)

**24. C — $(\pm3, 0)$.** $a^2 = 25$, $b^2 = 16$, so $c^2 = 25-16 = 9$ and
$c = 3$. The larger denominator is under $x^2$, so the major axis is horizontal
and the foci lie on it. (A) gives the vertices, not the foci. (§9.6)

**25. B — $y = \pm\tfrac{4}{3}x$.** $a = 3$, $b = 4$, and for the horizontal
form the asymptote slopes are $\pm b/a = \pm\tfrac{4}{3}$. (A) inverts the
ratio; (C) uses the squares instead of the roots. (§9.7)

**26. B — $(4,1)$.** Midpoint:
$\left(\tfrac{1+7}{2}, \tfrac{3-1}{2}\right) = (4,1)$. (D) forgets to halve.
(§9.2)

**27. A — $3$.**
$d = \dfrac{\lvert 3(0)+4(0)-15\rvert}{\sqrt{9+16}} = \dfrac{15}{5} = 3$. The
absolute value turns $-15$ into $15$. (§9.1)

**28. C — exactly $1$.** The parabola is the boundary case between the closed
ellipse ($e<1$) and the open hyperbola ($e>1$). It is the only conic with a
single fixed eccentricity. (§9.8)

**29. B — $(0,\pm4)$.** The positive term is $y^2$, so the transverse axis is
vertical and $a^2 = 16$ gives $a = 4$. Vertices sit on the transverse axis at
$(0,\pm4)$. (A) and (C) put them on the wrong axis; (D) reads $a$ from the
negative term's denominator. (§9.7)

**30. D — nothing.** A sum of two squares cannot be negative, so no real point
satisfies the equation. (A) and (B) take a root of a negative right side; (C)
would require a right side of exactly zero. (§9.4)

---

## Quick Reference

**Lines** — *Handbook p. 37*

$$y = mx + b \qquad y - y_1 = m(x - x_1) \qquad Ax + By + C = 0$$

$$m = \frac{y_2-y_1}{x_2-x_1} \qquad m_\parallel = m \qquad m_\perp = -\frac{1}{m} \qquad d = \frac{\lvert Ax_0+By_0+C\rvert}{\sqrt{A^2+B^2}}$$

Vertical line $x = a$, slope undefined. Horizontal line $y = b$, slope zero.

**Distance and midpoint**

$$d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2} \qquad M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$$

$$d_{3D} = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}$$

**Conic standard forms** — *Handbook pp. 38–40*

| Shape | Equation | Parameters |
|---|---|---|
| Circle | $(x-h)^2+(y-k)^2=r^2$ | centre $(h,k)$, radius $r$; right side is $r^2$ |
| Parabola, vertical axis | $(x-h)^2=4p(y-k)$ | vertex $(h,k)$, focus $(h,k+p)$, directrix $y=k-p$ |
| Parabola, horizontal axis | $(y-k)^2=4p(x-h)$ | vertex $(h,k)$, focus $(h+p,k)$, directrix $x=h-p$ |
| Ellipse, horizontal major | $\dfrac{(x-h)^2}{a^2}+\dfrac{(y-k)^2}{b^2}=1$ | $a>b$, $c^2=a^2-b^2$, foci $(h\pm c,k)$, area $\pi ab$ |
| Hyperbola, horizontal transverse | $\dfrac{(x-h)^2}{a^2}-\dfrac{(y-k)^2}{b^2}=1$ | $c^2=a^2+b^2$, foci $(h\pm c,k)$, asymptotes $y-k=\pm\frac{b}{a}(x-h)$ |

**The two that get confused**

$$\text{Ellipse: } c^2 = a^2 - b^2, \quad c < a, \quad \text{foci INSIDE the vertices}$$
$$\text{Hyperbola: } c^2 = a^2 + b^2, \quad c > a, \quad \text{foci OUTSIDE the vertices}$$

Ellipse — $a$ is the larger of $a$ and $b$.
Hyperbola — $a^2$ sits under the **positive** term, whatever its size.

**Eccentricity**

$$e = \frac{c}{a} \qquad \text{circle } 0 \;\cdot\; \text{ellipse } 0<e<1 \;\cdot\; \text{parabola } 1 \;\cdot\; \text{hyperbola } e>1$$

**Classification, no $xy$ term**

$A = C$ → circle · same sign, $A \ne C$ → ellipse · one of $A$, $C$ zero →
parabola · opposite signs → hyperbola.

After completing the square on a circle: right side $>0$ circle, $=0$ a single
point, $<0$ no graph.

**Not in the Handbook — memorize**

Completing the square as a procedure · conic classification by inspection ·
the perpendicular-slope rule · building a conic from geometric conditions ·
the three-point circle method · degenerate-case interpretation

---

## What's Next

Apprentice, analytic geometry is done. Every shape the Handbook tabulates now
has an equation you can write, and every second-degree equation has a shape you
can name on sight. That recognition is the part no reference table supplies.

In **Chapter 01-10: Areas, Volumes, and Mensuration**, we finish the geometric
toolkit in three dimensions — spheres, cylinders, cones, prisms, frusta, and
composite shapes. It is the most directly practical geometry in the guide: pipe
volumes, tank capacities, structural cross-sections, and the centroids that
determine where a load actually acts. The ellipse area you met in §9.6 is the
first entry in a much longer table.

Then **Chapter 01-11** introduces trigonometry properly — built from the unit
circle and the right triangle rather than handed to you as a list. Sine, cosine,
tangent, the laws of sines and cosines, and the identities. Every force
resolution in Tier 2C runs through it, and so does every calculation involving
an angle.

Bring the Handbook to pages 41–44 for the mensuration tables.

See you there.

— Your Mentor
