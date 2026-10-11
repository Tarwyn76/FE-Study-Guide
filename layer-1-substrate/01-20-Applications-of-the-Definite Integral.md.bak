---
chapter: "01-20"
title: "Applications of the Definite Integral"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-020-01, MATH-1C-020-02, MATH-1C-020-03, MATH-1C-020-04, MATH-1C-020-05, MATH-1C-020-06]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-20: Applications of the Definite Integral

> *"Every integral in this chapter is the same instruction: chop the thing into
> slices, work out what one slice contributes, add up the contributions. Area,
> volume, arc length, centroid, moment of inertia, work, RMS value — one method,
> seven answers. Learn to write down the contribution of a single slice and the
> integral writes itself."*

---

## Before You Start

**Prerequisites:** [01-06 Functions, Graphs, and Transformations](01-06-functions-graphs-transformations.md) · [01-09 Lines and Analytic Geometry](01-09-lines-analytic-geometry.md) · [01-11 Trigonometry](01-11-trigonometry.md) · [01-17 The Derivative](01-17-the-derivative.md) · [01-18 Applications of the Derivative](01-18-applications-of-the-derivative.md) · [01-19 Antiderivatives and the Definite Integral](01-19-antiderivatives-definite-integral.md)

**Skip if:** You pass the Tier 1C test-out quiz. Verify you can set up an area
between two curves including the decision to integrate in $x$ or $y$, choose
correctly between the washer and shell methods, and compute a centroid and a
second moment by integration before skipping. The centroid and second-moment
integrals are the highest-value items here for every discipline — do not skip
those on the strength of remembering the formulas from a table.

**Time:** ~80 min read · ~30 min review questions · ~90 min practice problems

---

## On the Board Today

Apprentice, Chapter 01-19 built the machine. This is the chapter where it earns
its keep, and it is the most directly useful chapter in Tier 1C.

Here is the one idea, stated once, because every section below is a special case
of it.

**Chop, contribute, sum.** Take the quantity you want. Slice the object into
pieces so thin that within one piece nothing varies appreciably. Write down what
that single piece contributes to the total — a rectangle's area, a disc's volume,
a segment's length, a slice's weight times its lift. Then integrate, which is the
formal instruction to add up all the contributions as the slices become
infinitesimally thin.

That is the whole method. The differences between the sections are differences in
what one slice contributes, and nothing else.

Why this matters more than the individual formulas: on the FE, and in practice,
the formulas for standard shapes are tabulated. Centroids of triangles,
semicircles, and parabolic spandrels are printed in the Handbook. Second moments
of rectangles and circles are printed. What is *not* printed is the centroid of
the section you actually designed, or the volume of the vessel geometry your
client specified, or the work to pump down the tank in front of you. For those you
set up an integral, and setting it up requires knowing where the tabulated
formulas came from.

We will build seven applications:

**Area between curves**, which is also the honest treatment of the net-versus-total
distinction I raised in Chapter 01-19.

**Volume**, by discs, washers, and shells.

**Arc length and surface area**, where the Pythagorean theorem meets the
derivative.

**Centroids**, the geometric centre of an area — required before you can find a
single reaction force in statics.

**Second moments of area**, the geometric property that determines how stiff a
beam is and how a column buckles. Along with the parallel axis theorem, which is
how tabulated values get moved to the axis you care about.

**Work by a variable force**, including the pumping problems that combine
integration with fluid weight.

**Root-mean-square value**, which is what an AC voltmeter reads and why the
mains is quoted at 120 V when its peak is 170 V.

Every one of these appears on the FE. Several appear on all seven discipline
exams.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 20.1 Compute the area between two curves, integrating with respect to $x$ or
  $y$ as appropriate
* 20.2 Split an integral at intersection points when the upper and lower curves
  exchange roles
* 20.3 Distinguish net and total accumulation, and compute total distance
  travelled from a velocity function
* 20.4 Compute volumes by slicing, using the disc and washer methods
* 20.5 Compute volumes by the shell method and choose between shells and washers
* 20.6 Compute arc length and the surface area of a solid of revolution
* 20.7 Compute the centroid of a plane area by integration and verify against
  tabulated results
* 20.8 Compute first moments of area and relate them to the centroid
* 20.9 Compute second moments of area about a stated axis
* 20.10 Apply the parallel axis theorem to transfer a second moment between
  parallel axes
* 20.11 Compute work done by a variable force, including spring and pumping
  problems
* 20.12 Compute the root-mean-square value of a periodic function and explain
  its physical meaning
* 20.13 Set up an integral from a physical description by identifying the
  contribution of a single slice

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $dA$ | area of one thin slice | $= (\text{height})\,dx$ or $(\text{width})\,dy$ |
| $dV$ | volume of one thin slice | disc, washer, or shell |
| $A$, $V$ | total area, total volume | — |
| $L$ | arc length | — |
| $S$ | surface area of revolution | — |
| $\bar{x}$, $\bar{y}$ | centroid coordinates | read "x-bar", "y-bar" |
| $Q_x$, $Q_y$ | first moment of area about the $x$- and $y$-axis | $Q_x = \int y\,dA$ |
| $I_x$, $I_y$ | second moment of area about the $x$- and $y$-axis | also called moment of inertia of the area |
| $\bar{I}$ | second moment about a **centroidal** axis | the tabulated value |
| $d$ | perpendicular distance between parallel axes | parallel axis theorem |
| $W$ | work | joules, N·m |
| $F(x)$ | force as a function of position | — |
| $k$ | spring constant | N/m |
| $\rho$ | mass density | kg/m³ |
| $\gamma = \rho g$ | weight density (specific weight) | N/m³; 9810 N/m³ for water |
| $f_{\text{rms}}$ | root-mean-square value of $f$ | — |
| $T$ | period of a periodic function | — |

> ---
> **Mentor's Margin**
>
> A warning about one phrase, because it causes genuine confusion and the FE will
> not clarify it for you.
>
> **"Moment of inertia" means two different things.** The *mass* moment of
> inertia, which appears in dynamics as $I = \int r^2\,dm$, has units of kg·m² and
> governs rotational acceleration. The *area* moment of inertia, which appears in
> mechanics of materials as $I = \int y^2\,dA$, has units of m⁴ (or far more often
> mm⁴) and governs bending stiffness. They are structurally analogous integrals
> and physically unrelated quantities.
>
> This chapter computes the **area** moment, which is more properly called the
> **second moment of area**. I will use that name, and I recommend you do too.
> When you meet "moment of inertia" in a problem statement, check the units: m⁴
> means area, kg·m² means mass. The units settle it every time.
>
> ---

---

## 20.1 Area Between Curves

For a single curve above the axis, Chapter 01-19 gave the area as
$\int_a^b f(x)\,dx$. Between two curves, the slice contribution changes but
nothing else does.

Slice vertically. One slice is a rectangle of width $dx$ whose height is the
vertical gap between the curves:

$$dA = \big[\,y_{\text{top}} - y_{\text{bottom}}\,\big]\,dx$$

$$\boxed{A = \int_a^b \big[\,f(x) - g(x)\,\big]\,dx \qquad \text{where } f \ge g \text{ on } [a,b]}$$

The limits $a$ and $b$ are usually the **intersection points**, which you find by
setting $f(x) = g(x)$ and solving — the polynomial root work from Chapter 01-07.

Note that this works regardless of whether either curve is above the axis. If both
are negative, the difference $f - g$ is still the positive vertical gap. The axis
plays no role at all, which is a simplification over the single-curve case.

![FIG-01-20-001: Region between the parabola y = x² and the line y = x + 2, shaded, over the interval from x = −1 to x = 2. The two intersection points are marked with dots and labeled (−1, 1) and (2, 4). One representative vertical slice is drawn inside the region as a narrow rectangle, with its width labeled dx, its top edge touching the line and labeled y_top = x + 2, and its bottom edge touching the parabola and labeled y_bottom = x². A bracket spans the slice height labeled "height = (x + 2) − x²".](../figures/FIG-01-20-001-area-between-curves.png)

### Worked Example 1 — Area Between a Line and a Parabola

**Given.** The region bounded by $y = x^2$ and $y = x + 2$.

**Find.** Its area.

**Solution.**

**Intersections.** Set the curves equal:

$$x^2 = x + 2 \implies x^2 - x - 2 = 0 \implies (x-2)(x+1) = 0$$

$$x = -1 \text{ and } x = 2$$

**Which is on top?** Test a convenient interior point, $x = 0$: the line gives
$y = 2$, the parabola gives $y = 0$. The **line** is on top throughout, and it
must be — two curves cannot swap positions without crossing, and there are no
crossings between $-1$ and $2$.

**Integrate.**

$$A = \int_{-1}^{2}\Big[(x+2) - x^2\Big]dx = \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^{2}$$

At $x = 2$: $2 + 4 - \frac{8}{3} = 6 - 2.6667 = 3.3333$

At $x = -1$: $0.5 - 2 + \frac{1}{3} = -1.1667$

$$A = 3.3333 - (-1.1667) = \boxed{4.50}$$

**Check by bounding.** The region fits inside a bounding box from $x = -1$ to
$x = 2$ and $y = 0$ to $y = 4$, area $3 \times 4 = 12$. Our answer is 37.5% of
that, plausible for a lens-shaped region occupying the middle of the box ✓

> ---
> **Mentor's Margin**
>
> Always determine which curve is on top by testing an actual point, and never by
> intuition about which function "grows faster." Growth rates tell you about
> behaviour far from the origin; they say nothing about a bounded interval.
>
> If you get the order backwards, your area comes out negative. That is a
> diagnostic, not a disaster — take the absolute value and note that you had the
> curves reversed. But a negative area in a chain of calculations you do not
> check will propagate silently, so test the point.
>
> ---

### When the curves cross inside the interval

If $f$ and $g$ exchange positions, a single integral computes the *net* signed
difference and the crossing regions partially cancel. For geometric area you must
split at the crossing, using the additivity property from Chapter 01-19, and take
each piece with its own top curve.

### Worked Example 2 — Curves That Cross

**Given.** The region between $y = x^3$ and $y = x$ on $[-1, 1]$.

**Find.** The total geometric area.

**Solution.**

**Intersections.** $x^3 = x \implies x(x^2-1) = 0 \implies x = -1, 0, 1$. There is
a crossing at $x = 0$, interior to the interval, so a split is mandatory.

**Determine the top curve on each piece.**

On $(0,1)$, test $x = 0.5$: $x = 0.5$, $x^3 = 0.125$. The **line** $y = x$ is on
top.

On $(-1,0)$, test $x = -0.5$: $x = -0.5$, $x^3 = -0.125$. The **cubic** is on top.

**Integrate each piece.**

$$A_1 = \int_0^1\left(x - x^3\right)dx = \left[\frac{x^2}{2} - \frac{x^4}{4}\right]_0^1 = 0.5 - 0.25 = 0.25$$

$$A_2 = \int_{-1}^{0}\left(x^3 - x\right)dx = \left[\frac{x^4}{4} - \frac{x^2}{2}\right]_{-1}^{0} = 0 - \left(0.25 - 0.5\right) = 0.25$$

$$A = 0.25 + 0.25 = \boxed{0.500}$$

**Check by symmetry.** Both $x^3$ and $x$ are odd functions, so the configuration
is symmetric about the origin and the two pieces must be equal ✓ Recognizing that
in advance halves the work: compute $A_1$ and double it.

**What a single integral would have given.**

$$\int_{-1}^{1}\left(x - x^3\right)dx = 0$$

because the integrand is odd. That zero is the correct *net* signed difference and
a completely wrong answer for the area. This is why the split is not optional.

### Integrating with respect to $y$

Sometimes horizontal slices are far easier. One slice is then a rectangle of
height $dy$ whose width is the horizontal gap:

$$\boxed{A = \int_c^d \big[\,x_{\text{right}} - x_{\text{left}}\,\big]\,dy}$$

Use $dy$ when the region's left and right boundaries are single functions of $y$
but its top or bottom boundary would require splitting into multiple functions of
$x$.

### Worked Example 3 — Choosing the Slice Direction

**Given.** The region bounded by $x = y^2$ and $x = 4$.

**Find.** Its area, and explain the choice of slice direction.

**Solution — horizontal slices.**

The boundaries are already expressed as $x$ in terms of $y$. Intersections:

$$y^2 = 4 \implies y = \pm 2$$

Right boundary $x = 4$, left boundary $x = y^2$:

$$A = \int_{-2}^{2}\left(4 - y^2\right)dy$$

The integrand is even, so use the symmetry shortcut from Chapter 01-19:

$$= 2\int_0^2\left(4-y^2\right)dy = 2\left[4y - \frac{y^3}{3}\right]_0^2 = 2\left(8 - \frac{8}{3}\right) = 2\left(5.3333\right)$$

$$A = \boxed{10.67 = \frac{32}{3}}$$

**Why not vertical slices?** Solving $x = y^2$ for $y$ gives $y = \pm\sqrt{x}$ —
**two** functions. A vertical slice runs from the lower branch to the upper
branch, so you would need

$$A = \int_0^4\left[\sqrt{x} - \left(-\sqrt{x}\right)\right]dx = \int_0^4 2\sqrt{x}\,dx = 2\left[\frac{2}{3}x^{3/2}\right]_0^4 = \frac{4}{3}(8) = \frac{32}{3} \;\checkmark$$

Same answer, and in this case not much harder. But the general point stands: when
a boundary is a sideways parabola, horizontal slices treat it as one function
while vertical slices force you to handle two branches. Look at the region and
pick the direction with fewer pieces.

![FIG-01-20-002: Two panels of the same region bounded by x = y² and the vertical line x = 4. Left panel titled "horizontal slices — one function": a representative horizontal rectangle inside the region with height dy, left edge on the parabola labeled x = y², right edge on the line labeled x = 4, and a bracket labeled "width = 4 − y²". Right panel titled "vertical slices — two branches": a representative vertical rectangle with width dx, top edge on the upper branch labeled y = +√x, bottom edge on the lower branch labeled y = −√x, with a note "one slice spans two functions".](../figures/FIG-01-20-002-slice-direction.png)

---

## 20.2 Net Versus Total: Distance Travelled

Chapter 01-19 promised this section, and it is a two-line consequence of what we
have just done.

For a particle with velocity $v(t)$ on $[t_1, t_2]$:

$$\boxed{\text{displacement} = \int_{t_1}^{t_2} v(t)\,dt \qquad \text{(net, signed)}}$$

$$\boxed{\text{total distance} = \int_{t_1}^{t_2}\big\lvert v(t)\big\rvert\,dt \qquad \text{(unsigned)}}$$

Compute the second by splitting at the zeros of $v$ — where the particle reverses
direction — and negating the intervals where $v < 0$.

### Worked Example 4 — Displacement Versus Distance

**Given.** The particle from Chapters 01-17 and 01-19 with
$v(t) = 3t^2 - 12t + 9$ m/s on $0 \le t \le 4$ s.

**Find.** Displacement and total distance travelled.

**Solution.**

**Where does $v$ change sign?** From Chapter 01-17, $v = 3(t-1)(t-3)$, so
$v = 0$ at $t = 1$ s and $t = 3$ s, and $v < 0$ on $(1,3)$.

**Displacement** — one integral, no splitting:

$$\int_0^4\left(3t^2-12t+9\right)dt = \Big[t^3 - 6t^2 + 9t\Big]_0^4 = (64-96+36) - 0 = \boxed{4.00 \text{ m}}$$

**Total distance** — split at 1 and 3, using the antiderivative
$s(t) = t^3-6t^2+9t$ throughout:

$$s(0) = 0, \quad s(1) = 4, \quad s(3) = 0, \quad s(4) = 4$$

| Interval | $\Delta s$ | Distance covered |
|---|---|---|
| $[0,1]$ | $4 - 0 = +4$ | $4$ m forward |
| $[1,3]$ | $0 - 4 = -4$ | $4$ m backward |
| $[3,4]$ | $4 - 0 = +4$ | $4$ m forward |

$$\text{total distance} = 4 + 4 + 4 = \boxed{12.0 \text{ m}}$$

**Interpretation.** The particle advances 4 m, retreats 4 m to the origin, then
advances 4 m again. It ends 4 m from where it started having travelled 12 m — an
odometer reads 12, a GPS displacement reads 4. Both numbers are correct answers to
different questions.

**Cross-check against Chapter 01-19.** There we found the average velocity over
$[0,4]$ to be 1.00 m/s, which is displacement over time: $4/4 = 1$ ✓ Note that
average *speed* is different: $12/4 = 3.00$ m/s. Average velocity uses net
displacement, average speed uses total distance.

---

## 20.3 Volume by Slicing: Discs and Washers

A solid can be sliced into thin plates. If a plate at position $x$ has
cross-sectional area $A(x)$ and thickness $dx$, its volume contribution is

$$dV = A(x)\,dx \implies \boxed{V = \int_a^b A(x)\,dx}$$

That is the general slicing formula, and everything below is a special case where
we know what $A(x)$ is.

### The disc method

Revolve a region around an axis and each slice sweeps out a circular disc. If the
slice extends a distance $r$ from the axis:

$$A = \pi r^2 \implies \boxed{V = \pi\int_a^b \big[r(x)\big]^2\,dx}$$

For revolution about the $x$-axis with the region running from the axis up to
$y = f(x)$, the radius is simply $r = f(x)$.

### The washer method

If the region does not touch the axis, each slice sweeps out an annulus — a washer
— with an outer and an inner radius:

$$A = \pi\left(r_{\text{out}}^2 - r_{\text{in}}^2\right) \implies \boxed{V = \pi\int_a^b\left[r_{\text{out}}^2 - r_{\text{in}}^2\right]dx}$$

![FIG-01-20-003: Two panels. Left panel titled "Disc": the region under y = √x from x = 0 to 4 shown above the x-axis, with one vertical slice highlighted, and beside it a three-dimensional sketch of the slice revolved about the x-axis into a solid circular disc of radius r = f(x) and thickness dx, labeled "A = πr²". Right panel titled "Washer": the region between y = 2x (outer) and y = x² (inner) with one vertical slice highlighted spanning from the lower to the upper curve, and beside it a three-dimensional sketch of the revolved slice as an annulus with outer radius 2x and inner radius x², the hole through the middle clearly shown, labeled "A = π(r_out² − r_in²)".](../figures/FIG-01-20-003-disc-washer.png)

> ---
> **Mentor's Margin**
>
> The error that swallows washer problems: writing
> $\left(r_{\text{out}} - r_{\text{in}}\right)^2$ instead of
> $r_{\text{out}}^2 - r_{\text{in}}^2$. Those are not equal and the difference is
> not small.
>
> Square each radius **first**, then subtract. The physical reason is that you are
> subtracting two *areas*, not squaring a difference of two lengths. If you keep
> the annulus picture in mind — a big circle with a small circle punched out — the
> algebra follows from the geometry and you will not confuse them.
>
> ---

### Worked Example 5 — Disc and Washer

**(a)** The region under $y = \sqrt{x}$ from $x = 0$ to $x = 4$ is revolved about
the $x$-axis. Find the volume.

The region touches the axis, so use discs with $r = \sqrt{x}$:

$$V = \pi\int_0^4\left(\sqrt{x}\right)^2 dx = \pi\int_0^4 x\,dx = \pi\left[\frac{x^2}{2}\right]_0^4 = \pi(8) = \boxed{25.1}$$

**Check by bounding.** The solid fits inside a cylinder of radius
$\sqrt{4} = 2$ and length 4, volume $\pi(4)(4) = 16\pi = 50.3$. Our answer is
exactly half that. For a solid whose radius grows as $\sqrt{x}$ — filling out
early and staying nearly full — half the bounding cylinder is reasonable ✓

**(b)** The region between $y = x^2$ and $y = 2x$ is revolved about the $x$-axis.
Find the volume.

**Intersections.** $x^2 = 2x \implies x(x-2) = 0 \implies x = 0, 2$.

**Which is farther from the axis?** At $x = 1$: the line gives 2, the parabola
gives 1. The **line** is the outer boundary.

$$V = \pi\int_0^2\left[(2x)^2 - \left(x^2\right)^2\right]dx = \pi\int_0^2\left(4x^2 - x^4\right)dx$$

$$= \pi\left[\frac{4x^3}{3} - \frac{x^5}{5}\right]_0^2 = \pi\left[\frac{32}{3} - \frac{32}{5}\right] = 32\pi\left(\frac{5-3}{15}\right) = \frac{64\pi}{15}$$

$$V = \boxed{13.4}$$

**Check.** The outer solid alone (the cone swept by $y = 2x$) has volume
$\frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(16)(2) = 33.5$, and the inner solid swept
by $y = x^2$ has volume $\pi\int_0^2 x^4 dx = \pi(32/5) = 20.1$. Difference:
$33.5 - 20.1 = 13.4$ ✓ Subtracting the two solids gives the same answer as
integrating the washer, as it must.

---

## 20.4 Volume by Shells

Sometimes the slice, when revolved, is not a disc but a thin cylindrical tube.
That happens when the slice is **parallel** to the axis of revolution rather than
perpendicular to it.

Unroll a thin cylindrical shell of radius $r$, height $h$, and thickness $dr$ and
you get a flat sheet of dimensions $2\pi r$ by $h$ by $dr$:

$$dV = 2\pi r h\,dr \implies \boxed{V = 2\pi\int_a^b r(x)\,h(x)\,dx}$$

For revolution about the $y$-axis using vertical slices, $r = x$ and $h$ is the
height of the region at that $x$.

![FIG-01-20-004: Left: the region between y = 2x and y = x² for 0 ≤ x ≤ 2, with one vertical slice highlighted at position x, its height labeled h = 2x − x² and width dx. Centre: a three-dimensional sketch of that slice revolved about the y-axis into a thin-walled cylindrical tube, with radius x and height h marked, the wall thickness labeled dx. Right: the same shell shown unrolled flat into a rectangular sheet with dimensions labeled 2πx (length), h (height), and dx (thickness), and the formula dV = 2πxh·dx printed beneath.](../figures/FIG-01-20-004-shell-method.png)

### Choosing between washers and shells

| Situation | Preferred method |
|---|---|
| Slices **perpendicular** to the axis | discs or washers |
| Slices **parallel** to the axis | shells |
| Region defined by $y = f(x)$, revolved about the $y$-axis | shells (avoids solving for $x$) |
| Region defined by $y = f(x)$, revolved about the $x$-axis | discs or washers |
| Either works | pick the one whose integrand you can actually integrate |

Both methods always give the same volume. The choice is entirely about which
integral is easier to evaluate — and occasionally, which one is possible at all
with the techniques you have.

### Worked Example 6 — Shells, With a Washer Cross-Check

**Given.** The region between $y = 2x$ and $y = x^2$ is revolved about the
**$y$-axis**.

**Find.** The volume, by shells and independently by washers.

**Solution — shells.**

Vertical slices are parallel to the $y$-axis ✓ Radius $r = x$; height is the
vertical gap $h = 2x - x^2$; limits $x = 0$ to $2$.

$$V = 2\pi\int_0^2 x\left(2x - x^2\right)dx = 2\pi\int_0^2\left(2x^2 - x^3\right)dx$$

$$= 2\pi\left[\frac{2x^3}{3} - \frac{x^4}{4}\right]_0^2 = 2\pi\left[\frac{16}{3} - 4\right] = 2\pi\left(\frac{16-12}{3}\right) = \frac{8\pi}{3}$$

$$V = \boxed{8.38}$$

**Check — washers in $y$.**

Now slices must be horizontal (perpendicular to the $y$-axis), so express both
boundaries as functions of $y$. From $y = 2x$: $x = y/2$. From $y = x^2$:
$x = \sqrt{y}$. The curves meet at $y = 0$ and $y = 4$.

At $y = 1$: $y/2 = 0.5$ and $\sqrt{y} = 1$. So $x = \sqrt{y}$ is the **outer**
radius and $x = y/2$ is the inner.

$$V = \pi\int_0^4\left[\left(\sqrt{y}\right)^2 - \left(\frac{y}{2}\right)^2\right]dy = \pi\int_0^4\left(y - \frac{y^2}{4}\right)dy$$

$$= \pi\left[\frac{y^2}{2} - \frac{y^3}{12}\right]_0^4 = \pi\left[8 - \frac{64}{12}\right] = \pi\left(8 - 5.3333\right) = \pi(2.6667) = \frac{8\pi}{3} \;\checkmark$$

Identical. Note that the shell integral required no algebraic inversion of either
curve, while the washer integral required solving both for $x$. That is the usual
reason to prefer shells for revolution about the $y$-axis.

---

## 20.5 Arc Length and Surface Area

### Arc length

Slice the curve into short pieces. Over a piece so short that the curve is
effectively straight, the Pythagorean theorem gives the length:

$$dL = \sqrt{(dx)^2 + (dy)^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\;dx$$

$$\boxed{L = \int_a^b\sqrt{1 + \big[f'(x)\big]^2}\;dx}$$

![FIG-01-20-005: A smooth curve with one short segment magnified in an inset. The inset shows a right triangle whose horizontal leg is labeled dx, vertical leg labeled dy, and hypotenuse labeled dL lying along the curve, with the annotation "dL = √(dx² + dy²)" and beneath it "= √(1 + (dy/dx)²) dx". A dashed line indicates that over an infinitesimal span the curve and the hypotenuse coincide.](../figures/FIG-01-20-005-arc-length-element.png)

> ---
> **Mentor's Margin**
>
> Arc length integrands are usually ugly. The square root of one plus a squared
> derivative rarely has an elementary antiderivative — even for something as
> simple as $y = x^2$, the arc length integral requires techniques beyond this
> tier.
>
> So the examples in textbooks and on exams are the handful of functions
> contrived to make the radicand a perfect square. Do not read that as
> representative. In practice, arc lengths are computed numerically, and Chapter
> 01-37 gives you the tools. What matters here is that you can *set up* the
> integral correctly, because a numerical method still needs the right integrand.
>
> ---

### Worked Example 7 — Arc Length

**Given.** $y = \frac{2}{3}x^{3/2}$ from $x = 0$ to $x = 3$.

**Find.** The arc length.

**Solution.**

$$\frac{dy}{dx} = \frac{2}{3}\cdot\frac{3}{2}x^{1/2} = x^{1/2} \implies \left(\frac{dy}{dx}\right)^2 = x$$

The radicand becomes $1 + x$ — this function was chosen precisely so that it
would:

$$L = \int_0^3\sqrt{1+x}\;dx$$

Substitute $u = 1+x$, $du = dx$, with limits $u = 1$ to $u = 4$:

$$= \int_1^4 u^{1/2}du = \left[\frac{2}{3}u^{3/2}\right]_1^4 = \frac{2}{3}(8 - 1) = \frac{14}{3}$$

$$L = \boxed{4.67}$$

**Check against the chord.** The endpoints are $(0,0)$ and
$\left(3, \frac{2}{3}(3)^{3/2}\right) = (3, 3.464)$. The straight-line distance is

$$\sqrt{9 + 12.0} = \sqrt{21.0} = 4.583$$

The arc must be longer than the chord, and $4.667 > 4.583$ ✓ — longer by about
1.8%, which is right for a gently curving arc. This chord comparison is the
standard sanity check on any arc length, and it costs one square root.

### Surface area of revolution

Revolve the curve rather than the region. Each arc element sweeps out a thin band
— a frustum strip — of circumference $2\pi r$ and slant width $dL$:

$$\boxed{S = 2\pi\int_a^b r\sqrt{1 + \big[f'(x)\big]^2}\;dx}$$

For revolution about the $x$-axis, $r = f(x)$.

The distinction from the volume formulas matters: volume uses the *perpendicular*
thickness $dx$, while surface area uses the *slant* length $dL$. Using $dx$ in a
surface area integral understates the answer.

### Worked Example 8 — Surface Area, Verified Against a Known Formula

**Given.** The line $y = \frac{x}{2}$ from $x = 0$ to $x = 4$, revolved about the
$x$-axis. This generates a cone of base radius 2 and height 4.

**Find.** The lateral surface area by integration, and verify against the
elementary cone formula.

**Solution.**

$$\frac{dy}{dx} = \frac{1}{2} \implies \sqrt{1 + \frac{1}{4}} = \sqrt{1.25} = 1.11803$$

The radicand is constant here, which is what makes a cone tractable:

$$S = 2\pi\int_0^4\frac{x}{2}(1.11803)\,dx = 2\pi(0.559017)\left[\frac{x^2}{2}\right]_0^4$$

$$= 2\pi(0.559017)(8) = 2\pi(4.47214) = \boxed{28.1}$$

**Verify with the cone formula** $S = \pi r \ell$, where $\ell$ is the slant
height:

$$\ell = \sqrt{r^2 + h^2} = \sqrt{4 + 16} = \sqrt{20} = 4.47214$$

$$S = \pi(2)(4.47214) = 28.10 \;\checkmark$$

Exact agreement. And notice where the slant height appeared in the integral: the
factor $\sqrt{1 + (dy/dx)^2}$ *is* the slant-to-horizontal ratio, and integrating
it recovered $\ell$ automatically. That is the geometric content of the formula.

**What the wrong integral would give.** Omitting the radical:
$2\pi\int_0^4\frac{x}{2}dx = 2\pi(4) = 25.1$ — an 11% understatement. The radical
is not a refinement.

---

## 20.6 Centroids and First Moments of Area

This section and the next are the ones your statics and mechanics chapters cannot
proceed without.

### First moment of area

The **first moment** of an area about an axis weights each piece of area by its
distance from that axis:

$$\boxed{Q_x = \int y\,dA \qquad Q_y = \int x\,dA}$$

Note the crossed subscripts: $Q_x$, the moment about the $x$-axis, involves the
$y$-distance. The subscript names the axis, and the distance is measured
perpendicular to it. This convention trips people up and it is universal, so learn
it as written.

Units are length cubed — mm³ for a plane area in mm².

### Centroid

The **centroid** is the area-weighted average position — the geometric centre:

$$\boxed{\bar{x} = \frac{Q_y}{A} = \frac{\int x\,dA}{A} \qquad \bar{y} = \frac{Q_x}{A} = \frac{\int y\,dA}{A}}$$

Equivalently, $Q_y = A\bar{x}$ and $Q_x = A\bar{y}$: the first moment equals the
total area times the centroidal distance. That form is the one you will use to
combine composite shapes.

### Setting up the integrals with vertical slices

For a region between $y = f(x)$ above and $y = g(x)$ below, take a vertical slice
at position $x$:

$$dA = \big[f(x) - g(x)\big]dx$$

The slice's own centroid is at its horizontal position $x$ and at its mid-height
$\frac{f(x)+g(x)}{2}$. So:

$$\boxed{\bar{x} = \frac{1}{A}\int_a^b x\big[f - g\big]dx \qquad \bar{y} = \frac{1}{A}\int_a^b \frac{f+g}{2}\big[f-g\big]dx}$$

![FIG-01-20-006: The region under y = x² from x = 0 to 3, bounded below by the x-axis, shaded. A representative vertical slice is drawn with width dx and height x², and a dot at the slice's own centroid is marked at height x²/2 with a label "slice centroid at mid-height y = x²/2". The overall centroid of the region is marked with a crosshair symbol at (2.25, 2.70) and labeled. Dashed lines drop from the centroid to both axes showing x̄ = 2.25 and ȳ = 2.70. A note reads "centroid lies inside the region, low and to the right — where the area is".](../figures/FIG-01-20-006-centroid-integration.png)

> ---
> **Mentor's Margin**
>
> Two things about $\bar{y}$ that cause errors.
>
> First, the $\frac{f+g}{2}$ factor. Each slice contributes its area at its **own
> centroid height**, which is the middle of the slice, not the top. Writing
> $\int f\cdot f\,dx$ instead of $\int\frac{f}{2}\cdot f\,dx$ doubles your answer
> for a region sitting on the $x$-axis.
>
> Second, a check that costs nothing: **the centroid must lie inside the region's
> bounding box**, and for a convex region, inside the region itself. If you
> compute a centroid outside the shape you have made an algebra error. (For a
> genuinely non-convex shape — an L-section, a channel — the centroid can fall
> outside the material, but it will still be inside the bounding box. Use the box
> as the test.)
>
> ---

### Worked Example 9 — Centroid of a Parabolic Spandrel

**Given.** The region bounded above by $y = x^2$, below by the $x$-axis, on the
right by $x = 3$.

**Find.** The area and the centroid.

**Solution.**

**Area.**

$$A = \int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = 9.00$$

**Horizontal centroid.** Here $f = x^2$ and $g = 0$:

$$Q_y = \int_0^3 x\left(x^2\right)dx = \left[\frac{x^4}{4}\right]_0^3 = \frac{81}{4} = 20.25$$

$$\bar{x} = \frac{20.25}{9.00} = 2.25$$

**Vertical centroid.** The slice mid-height is $\frac{x^2 + 0}{2} = \frac{x^2}{2}$:

$$Q_x = \int_0^3\frac{x^2}{2}\left(x^2\right)dx = \frac{1}{2}\int_0^3 x^4\,dx = \frac{1}{2}\left[\frac{x^5}{5}\right]_0^3 = \frac{243}{10} = 24.30$$

$$\bar{y} = \frac{24.30}{9.00} = 2.70$$

$$\boxed{A = 9.00, \quad \bar{x} = 2.25, \quad \bar{y} = 2.70}$$

**Check against the Handbook table.** The parabolic spandrel with base $b$ and
height $h$ is a tabulated shape with

$$A = \frac{bh}{3} \qquad \bar{x} = \frac{3b}{4} \qquad \bar{y} = \frac{3h}{10}$$

Here $b = 3$ and $h = 3^2 = 9$:

$$A = \frac{3(9)}{3} = 9 \;\checkmark \qquad \bar{x} = \frac{3(3)}{4} = 2.25 \;\checkmark \qquad \bar{y} = \frac{3(9)}{10} = 2.70 \;\checkmark$$

All three match exactly. **This is worth doing at least once yourself**, because
it demonstrates that the tabulated values you will lean on during the exam are
nothing more than these integrals, evaluated in advance by somebody else.

**Bounding-box check.** The region lies in $0 \le x \le 3$, $0 \le y \le 9$, and
$(2.25, 2.70)$ is inside ✓ The centroid sits well right of centre and well below
mid-height, which matches the shape — nearly all the area is bunched near
$x = 3$ and near the bottom.

---

## 20.7 Second Moments of Area and the Parallel Axis Theorem

### Second moment of area

The **second moment** weights each element of area by the **square** of its
distance from the axis:

$$\boxed{I_x = \int y^2\,dA \qquad I_y = \int x^2\,dA}$$

Units are length to the fourth power — mm⁴ almost always, because section
properties in engineering practice are quoted in mm⁴ or in⁴.

Two properties to internalize:

**$I$ is always positive.** The distance is squared, so nothing cancels. Unlike a
first moment, a second moment cannot be zero for a real area and cannot be
negative.

**Distant area counts disproportionately.** Doubling a distance quadruples its
contribution. This is why an I-beam puts material in flanges far from the centre,
and why a beam twice as deep is eight times as stiff in bending — the depth enters
cubed after the integration.

### Worked Example 10 — Rectangle About Two Axes

**Given.** A rectangle of width $b$ and height $h$.

**Find.** $I$ about its base, and $\bar{I}$ about its horizontal centroidal axis.

**Solution.**

Slice horizontally: a strip at height $y$ has $dA = b\,dy$.

**About the base**, measuring $y$ from the base, $0 \le y \le h$:

$$I_{\text{base}} = \int_0^h y^2 b\,dy = b\left[\frac{y^3}{3}\right]_0^h = \boxed{\frac{bh^3}{3}}$$

**About the centroidal axis**, measuring $y$ from mid-height,
$-\frac{h}{2} \le y \le \frac{h}{2}$:

$$\bar{I} = \int_{-h/2}^{h/2} y^2 b\,dy = b\left[\frac{y^3}{3}\right]_{-h/2}^{h/2} = \frac{b}{3}\left(\frac{h^3}{8} + \frac{h^3}{8}\right) = \boxed{\frac{bh^3}{12}}$$

The integrand $y^2$ is even, so the symmetry shortcut applies:
$2\int_0^{h/2}y^2b\,dy = 2b\frac{h^3}{24} = \frac{bh^3}{12}$ ✓

**Note the ratio.** $I_{\text{base}} = 4\bar{I}$ for any rectangle. The centroidal
axis always gives the *smallest* second moment of any parallel axis, which the
next result explains.

### The parallel axis theorem

$$\boxed{I = \bar{I} + A d^2}$$

where $\bar{I}$ is the second moment about the **centroidal** axis, $A$ is the
area, and $d$ is the perpendicular distance to the parallel axis of interest.

The $Ad^2$ term is always positive, which proves the observation above: the
centroidal axis minimizes $I$.

**Verify on the rectangle.** From the centroidal axis to the base,
$d = \frac{h}{2}$:

$$I_{\text{base}} = \frac{bh^3}{12} + (bh)\left(\frac{h}{2}\right)^2 = \frac{bh^3}{12} + \frac{bh^3}{4} = \frac{bh^3 + 3bh^3}{12} = \frac{bh^3}{3} \;\checkmark$$

Matches the direct integration exactly.

![FIG-01-20-007: A rectangle of width b and height h shown in elevation. A dashed horizontal line through mid-height is labeled "centroidal axis, Ī = bh³/12" and a solid horizontal line along the bottom edge is labeled "base axis, I = bh³/3". A vertical double-headed arrow between the two axes is labeled d = h/2. A representative horizontal strip of thickness dy is drawn inside the rectangle with its distance y from the centroidal axis marked. Beside the figure, the transfer is written out: bh³/12 + (bh)(h/2)² = bh³/3, with the note "the Ad² term is always positive — the centroidal axis gives the minimum".](../figures/FIG-01-20-007-parallel-axis-theorem.png)

> ---
> **Mentor's Margin**
>
> The parallel axis theorem is how tabulated values become useful, and the
> direction of use matters.
>
> The Handbook tabulates $\bar{I}$ — the **centroidal** value — for standard
> shapes. Real sections are assemblies of those shapes whose individual centroids
> do not coincide with the assembly's centroid. So the working procedure for a
> composite section is: find the assembly centroid using first moments, then
> transfer each piece's $\bar{I}$ to that common axis with $+Ad^2$, then add.
>
> Two failure modes, both common. **Transferring from the wrong starting axis**:
> the theorem requires $\bar{I}$ about the piece's own centroid, not about some
> other convenient axis. And **forgetting a transfer term** for a piece whose
> centroid happens to be close to the assembly centroid — close is not zero, and
> $d^2$ grows fast.
>
> The full composite-section procedure belongs to Chapter 02-49 and the statics
> chapters of Tier 2A. What you need from this chapter is the integral that
> produces $\bar{I}$ in the first place, and the transfer relation. Nothing here
> depends on that later material.
>
> ---

### Worked Example 11 — Numerical Second Moments

**Given.** A rectangular section 100 mm wide by 200 mm deep.

**Find.** $\bar{I}$ about the horizontal centroidal axis, $I$ about the base, and
the effect of doubling the depth.

**Solution.**

**Centroidal.**

$$\bar{I} = \frac{bh^3}{12} = \frac{100(200)^3}{12} = \frac{100\left(8.00\times10^6\right)}{12} = \frac{8.00\times10^8}{12}$$

$$\bar{I} = \boxed{66.7\times10^6 \text{ mm}^4}$$

**About the base**, by the parallel axis theorem with $A = 20{,}000$ mm² and
$d = 100$ mm:

$$I = 66.7\times10^6 + 20{,}000(100)^2 = 66.7\times10^6 + 200\times10^6$$

$$I = \boxed{267\times10^6 \text{ mm}^4}$$

Check against $\frac{bh^3}{3} = \frac{8.00\times10^8}{3} = 267\times10^6$ ✓

**Doubling the depth to 400 mm.**

$$\bar{I} = \frac{100(400)^3}{12} = \frac{100\left(6.40\times10^7\right)}{12} = 533\times10^6 \text{ mm}^4$$

That is **eight times** the original, from doubling one dimension. The cube on $h$
is why: $2^3 = 8$.

**Compare to doubling the width instead.** $\frac{200(200)^3}{12} =
133\times10^6$ mm⁴ — only double. Same added material, one quarter the benefit.

**Interpretation.** For bending stiffness, depth is worth vastly more than width.
That single fact, which fell out of an exponent in an integral, explains why floor
joists are installed on edge rather than flat, and it is the beginning of section
design.

---

## 20.8 Work by a Variable Force

Constant force times distance gives work. When the force varies with position,
slice the displacement into pieces over which the force is effectively constant:

$$dW = F(x)\,dx \implies \boxed{W = \int_a^b F(x)\,dx}$$

Units: N·m = J.

### Springs

Hooke's law gives the force required to hold a spring at extension $x$:

$$F = kx$$

so

$$W = \int_{x_1}^{x_2}kx\,dx = \frac{k}{2}\left(x_2^2 - x_1^2\right)$$

### Worked Example 12 — Spring Work

**Given.** A spring with $k = 250$ N/m.

**(a)** Work to stretch it from its free length to 0.15 m.
**(b)** Work to stretch it further, from 0.15 m to 0.25 m.
**(c)** Comment on the comparison.

**Solution.**

**(a)**

$$W = \int_0^{0.15}250x\,dx = 125\left[x^2\right]_0^{0.15} = 125(0.0225) = \boxed{2.81 \text{ J}}$$

**(b)**

$$W = 125\left(0.25^2 - 0.15^2\right) = 125(0.0625 - 0.0225) = 125(0.0400) = \boxed{5.00 \text{ J}}$$

**(c)** The second stretch covers a **shorter** distance — 0.10 m against 0.15 m —
yet requires nearly **twice** the work. Because the force grows linearly with
extension, the work grows quadratically, so later increments of stretch cost far
more than early ones. Reporting work as "force times distance" using either the
initial or the final force would be wrong in both directions; the integral is
required.

**Check.** Total work to 0.25 m directly: $125(0.0625) = 7.81$ J. And
$2.81 + 5.00 = 7.81$ J ✓ The additivity property from Chapter 01-19 holds, as it
must.

### Pumping a fluid

Here the slicing is over the fluid, not over a displacement. A horizontal slice of
liquid at height $y$ has:

- volume $dV = A(y)\,dy$, where $A(y)$ is the cross-sectional area at that height
- weight $\gamma\,dV$, where $\gamma = \rho g$ is the weight density
- lift distance $\big(y_{\text{destination}} - y\big)$

$$\boxed{W = \gamma\int \big(y_{\text{dest}} - y\big)A(y)\,dy}$$

For water, $\gamma = \rho g = 1000(9.81) = 9810$ N/m³.

![FIG-01-20-008: Cross-section of a vertical cylindrical tank of radius 1.5 m and height 4.0 m, filled with water shown shaded. A representative horizontal slice of the water is drawn at height y above the base, with its thickness labeled dy and its face labeled "area πr² = 7.069 m²". A vertical arrow runs from the slice up to the tank rim, labeled "lift distance = 4.0 − y". Beside the figure the slice contribution is written: dW = γ(4.0 − y)(πr²)dy. A dashed horizontal line at y = 2.0 m is labeled "centroid of the water — the shortcut lift distance".](../figures/FIG-01-20-008-pumping-work.png)

### Worked Example 13 — Pumping a Cylindrical Tank

**Given.** A vertical cylindrical tank, radius 1.5 m and height 4.0 m, is full of
water. Water is to be pumped out over the top rim.

**Find.** The work required, and verify by an independent route.

**Solution.**

Measure $y$ upward from the tank floor, $0 \le y \le 4.0$ m.

Cross-sectional area is constant:

$$A = \pi r^2 = \pi(1.5)^2 = \pi(2.25) = 7.0686 \text{ m}^2$$

Each slice must be lifted to $y = 4.0$, a distance of $(4.0 - y)$.

$$W = \gamma\int_0^{4.0}(4.0 - y)(7.0686)\,dy = 9810(7.0686)\int_0^{4.0}(4.0-y)\,dy$$

$$9810(7.0686) = 69{,}343 \text{ N/m}$$

$$\int_0^{4.0}(4.0-y)\,dy = \left[4.0y - \frac{y^2}{2}\right]_0^{4.0} = 16.0 - 8.0 = 8.00 \text{ m}^2$$

$$W = 69{,}343(8.00) = 554{,}740 \text{ J}$$

$$W = \boxed{555 \text{ kJ}}$$

**Verify by the centroid shortcut.** Because every particle of water must be
lifted, and lifting is linear in distance, the total work equals the total weight
times the lift distance of the **centroid**. The centroid of a full cylinder is at
mid-height, $y = 2.0$ m, so the centroid lift is $4.0 - 2.0 = 2.0$ m.

$$\text{total weight} = \gamma V = 9810\left[\pi(2.25)(4.0)\right] = 9810(28.274) = 277{,}370 \text{ N}$$

$$W = 277{,}370(2.00) = 554{,}740 \text{ J} \;\checkmark$$

Exact agreement.

**Units check.** $\frac{\text{N}}{\text{m}^3}\cdot\text{m}\cdot\text{m}^2\cdot
\text{m} = \text{N}\cdot\text{m} = \text{J}$ ✓

> ---
> **Mentor's Margin**
>
> The centroid shortcut in that verification is worth keeping, and worth knowing
> its limits.
>
> It works whenever the lift distance is **linear** in position, which it is for
> pumping to a fixed level. Total weight times centroid lift, done. That makes it
> an excellent check on any pumping integral, and for a uniform cross-section it
> is faster than the integral.
>
> It fails as soon as the cross-section varies *and* you want the centroid without
> computing it — because then finding the centroid is itself an integral, and you
> have saved nothing. It also fails if the destination height varies, or if the
> tank is only partly full and you must first locate the free surface.
>
> Use it as a check, always. Use it as a primary method only for uniform tanks.
>
> ---

---

## 20.9 Root-Mean-Square Value

Chapter 01-19 gave the average value of a function. For an alternating quantity
that average is often useless: a full cycle of a sine wave has average zero, yet a
120 V outlet plainly delivers power.

The resolution is to average the **square** — which is always positive — and then
take the square root to return to the original units:

$$\boxed{f_{\text{rms}} = \sqrt{\frac{1}{T}\int_0^T \big[f(t)\big]^2 dt}}$$

Read the name backwards and it is the recipe: **square** the function, take its
**mean**, take the **root**.

### Why it is the right average

Power in a resistor goes as the square of voltage or current. So the RMS value is
precisely the constant DC value that would deliver the same average power. That is
what makes it the physically meaningful average, and what an AC meter is
calibrated to display.

### Worked Example 14 — RMS of a Sinusoid

**Given.** $v(t) = V_m\sin(\omega t)$ with peak $V_m = 170$ V, over one full
period $T = \frac{2\pi}{\omega}$.

**(a)** Show the RMS value is $\frac{V_m}{\sqrt{2}}$.
**(b)** Evaluate it.
**(c)** Confirm the simple average over a period is zero.

**Solution.**

**(a)** Mean of the square:

$$\frac{1}{T}\int_0^T V_m^2\sin^2(\omega t)\,dt$$

The integrand $\sin^2$ is handled with the power-reduction identity from Chapter
01-11:

$$\sin^2\theta = \frac{1 - \cos 2\theta}{2}$$

$$= \frac{V_m^2}{T}\int_0^T\frac{1 - \cos(2\omega t)}{2}\,dt = \frac{V_m^2}{2T}\left[t - \frac{\sin(2\omega t)}{2\omega}\right]_0^T$$

At $t = T = \frac{2\pi}{\omega}$ the argument $2\omega T = 4\pi$, and
$\sin 4\pi = 0$. At $t = 0$, $\sin 0 = 0$. So the sine term contributes nothing —
it integrates to zero over any whole number of half-cycles:

$$= \frac{V_m^2}{2T}(T) = \frac{V_m^2}{2}$$

Take the root:

$$v_{\text{rms}} = \sqrt{\frac{V_m^2}{2}} = \boxed{\frac{V_m}{\sqrt{2}}}$$

**(b)**

$$v_{\text{rms}} = \frac{170}{\sqrt{2}} = \frac{170}{1.41421} = \boxed{120.2 \text{ V}}$$

Which is why household mains in North America is described as 120 V while an
oscilloscope shows peaks near 170 V. The two numbers describe the same waveform.

**(c)** Simple average over a period:

$$\bar{v} = \frac{1}{T}\int_0^T V_m\sin(\omega t)\,dt = \frac{V_m}{T}\left[\frac{-\cos(\omega t)}{\omega}\right]_0^T = \frac{V_m}{\omega T}\left(-\cos 2\pi + \cos 0\right)$$

$$= \frac{V_m}{\omega T}(-1 + 1) = \boxed{0}$$

Exactly zero, as the signed-area argument from Chapter 01-19 requires — the
positive and negative half-cycles cancel. This is the concrete case where the
ordinary average carries no useful information and the RMS value does.

> **Preview note.** The factor $\frac{1}{\sqrt{2}} = 0.7071$ applies **only** to a
> pure sinusoid. A square wave has $f_{\text{rms}} = V_m$; a triangular wave has
> $\frac{V_m}{\sqrt{3}}$. Each comes from evaluating the same integral for that
> waveform. Chapter 02-63 develops AC circuit analysis on an RMS basis and treats
> non-sinusoidal waveforms. Nothing here depends on that chapter; the integral
> above is complete on its own.

---

## As the Handbook States It

> **Handbook 10.6** — the material for this chapter is spread across **three**
> separate places, which is worth knowing before the exam rather than during it.
>
> **Mathematics section (begins p. 36)** — *Integral Calculus*, approximately
> pp. 46–48: the integral table, average value, and the standard application
> formulas.
>
> **Mensuration of areas and volumes** — in the Mathematics section: areas,
> perimeters, volumes, and surface areas of standard plane figures and solids.
>
> **Statics section** — centroid and second-moment tables for standard shapes,
> and the parallel axis theorem.

**What's in the Handbook — find it fast:**

- **Centroid tables** for the standard shapes: rectangle, triangle, circle,
  semicircle, quarter circle, circular sector, parabolic and semiparabolic
  spandrels. These give $A$, $\bar{x}$, $\bar{y}$ directly.
- **Second-moment tables** for the same shapes, giving $\bar{I}$ about centroidal
  axes and often about other convenient axes as well.
- **The parallel axis theorem**, stated as $I = \bar{I} + Ad^2$ or in the
  equivalent notation $I_x = I_{xc} + d_x^2 A$.
- **Mensuration formulas** — cone, sphere, cylinder, frustum, paraboloid volumes
  and surface areas. Use these constantly for volume and pumping problems, and as
  independent checks on volume integrals.
- **Arc length and surface of revolution** formulas.
- Work and energy relations, in the Statics/Dynamics sections.

**A strategy note.** For any FE problem involving a *standard* shape, the
tabulated value beats the integral every time — the table is exact and takes ten
seconds. Reach for the integral when the shape is not tabulated, or when the
problem explicitly asks you to derive rather than look up. Knowing which situation
you are in is the skill.

**What's not in the Handbook — memorize:**

- The general slicing principle: identify the contribution of one slice, then
  integrate
- The area between curves as $\int\big[y_{\text{top}} - y_{\text{bottom}}\big]dx$,
  and the horizontal-slice alternative
- That you must **split at intersections** when curves cross
- The distinction between net accumulation and total accumulation, and that total
  distance requires $\int\lvert v\rvert dt$
- Which method to choose for volumes: slices perpendicular to the axis → discs or
  washers; slices parallel to the axis → shells
- That the washer integrand is $r_{\text{out}}^2 - r_{\text{in}}^2$, not
  $(r_{\text{out}} - r_{\text{in}})^2$
- The shell volume element $dV = 2\pi rh\,dr$
- That surface area uses the **slant** length $dL$ while volume uses the
  perpendicular thickness $dx$
- The chord comparison as a check on arc length
- The crossed-subscript convention: $Q_x = \int y\,dA$, $I_x = \int y^2\,dA$
- The $\frac{f+g}{2}$ slice-centroid factor in the $\bar{y}$ integral
- That the centroid must lie within the region's bounding box
- That $I$ is always positive and that the centroidal axis minimizes it
- The $h^3$ dependence of $\bar{I}$ on depth, and its design consequence
- $\gamma_{\text{water}} = 9810$ N/m³
- The centroid shortcut for pumping work, and its limitation to linear lift
- The RMS definition, and that $\frac{1}{\sqrt{2}}$ is specific to sinusoids

> ---
> **Mentor's Margin**
>
> Locate the centroid and second-moment tables now, before you need them under
> time pressure, and add both to the personal page map you started in Chapter
> 00-03. They live in the Statics section rather than in Mathematics, which
> surprises people mid-exam — the natural instinct is to search Mathematics, and
> that costs a minute you do not have.
>
> The page numbers I have given for the Mathematics subsections are approximate.
> The section start at p. 36 is verified from the table of contents; the
> subsection locations and the Statics table pages are worth confirming yourself
> in your own copy.
>
> ---

---

## Where This Goes Wrong

**Getting the order of the curves backwards.** $\int(g - f)$ instead of
$\int(f - g)$ produces a negative area. Test an interior point to establish which
curve is on top.

**Failing to split where curves cross.** A single integral across a crossing
computes net signed difference, and the pieces cancel. Find all intersections
inside the interval and split at each.

**Reporting displacement when total distance was asked.** Split at the zeros of
the rate and take absolute values.

**Choosing the harder slice direction.** If a boundary is a sideways parabola or
otherwise multivalued in $x$, horizontal slices are usually simpler. Check both
before committing.

**Writing $(r_{\text{out}} - r_{\text{in}})^2$ in a washer integral.** Square
each radius, then subtract. These are areas being subtracted, not lengths.

**Mixing up shell and washer geometry.** A slice perpendicular to the axis sweeps
a disc or washer; a slice parallel to the axis sweeps a shell. Sketch the slice and
the axis before choosing.

**Using the wrong variable in a shell integral.** Revolving about the $y$-axis
with vertical slices gives $r = x$ and $h$ the vertical extent. Revolving about
the $x$-axis with horizontal slices gives $r = y$ and $h$ the horizontal extent.

**Omitting the radical in arc length or surface area.** The factor
$\sqrt{1 + (f')^2}$ is not a correction term; leaving it out understates the answer
substantially, as Worked Example 8 showed.

**Using $dx$ instead of $dL$ in a surface area integral.** Surface area follows
the slant, volume follows the perpendicular thickness.

**Reversing the subscript convention.** $Q_x$ and $I_x$ are moments *about* the
$x$-axis and use the $y$-distance. The subscript names the axis, not the
coordinate in the integrand.

**Omitting the $\frac{1}{2}$ in the $\bar{y}$ integral.** A slice contributes its
area at its own mid-height. For a region on the $x$-axis, forgetting this doubles
your $\bar{y}$.

**Computing a centroid outside the bounding box.** That is an arithmetic error, not
an unusual shape. Check it every time.

**Transferring a second moment from a non-centroidal axis.** The parallel axis
theorem requires $\bar{I}$ about the shape's own centroid as the starting point.
Transferring from an arbitrary axis gives a wrong answer.

**Subtracting instead of adding the transfer term.** $I = \bar{I} + Ad^2$. The
term is always positive because $d$ is squared. If you find yourself needing a
smaller value than $\bar{I}$, you have the theorem backwards — the centroidal axis
is the minimum.

**Confusing area and mass moments of inertia.** Check the units: m⁴ is area,
kg·m² is mass. They are different quantities in different problems.

**Using force times distance for a variable force.** If $F$ depends on position,
integrate. Neither the initial nor the final force gives the right answer, and
neither does their average unless the force is exactly linear.

**Using the wrong lift distance in a pumping problem.** The lift is
$y_{\text{destination}} - y_{\text{slice}}$, and it varies with the slice. Using
the total tank height for every slice overstates the work.

**Applying $\frac{1}{\sqrt{2}}$ to a non-sinusoidal waveform.** That factor is
specific to pure sinusoids. Other waveforms require evaluating the RMS integral for
that waveform.

**Reporting an average of zero for an alternating quantity and stopping there.**
The simple average is genuinely zero and genuinely uninformative. If the question
concerns power, effective voltage, or heating, the RMS value is what is wanted.

---

## Key Terms

| Term | Definition |
|---|---|
| Slicing principle | Setting up an integral by identifying the contribution of one thin slice |
| Area between curves | $\int\big[y_{\text{top}} - y_{\text{bottom}}\big]dx$, or the horizontal analogue |
| Disc method | Volume by revolution using slices perpendicular to the axis that touch it; $dV = \pi r^2 dx$ |
| Washer method | Disc method with a hole; $dV = \pi\left(r_{\text{out}}^2 - r_{\text{in}}^2\right)dx$ |
| Shell method | Volume by revolution using slices parallel to the axis; $dV = 2\pi rh\,dr$ |
| Arc length | $\int\sqrt{1 + (f')^2}\,dx$; the length along a curve |
| Surface of revolution | $2\pi\int r\sqrt{1+(f')^2}\,dx$; area swept by revolving a curve |
| First moment of area | $Q_x = \int y\,dA$; area weighted by distance from an axis; units L³ |
| Centroid | Area-weighted average position; $\bar{y} = Q_x/A$ |
| Second moment of area | $I_x = \int y^2\,dA$; area weighted by squared distance; units L⁴ |
| Area moment of inertia | Synonym for second moment of area; units m⁴ — distinct from mass moment of inertia |
| Centroidal axis | An axis through the centroid; gives the minimum second moment among parallel axes |
| Parallel axis theorem | $I = \bar{I} + Ad^2$; transfers a second moment to a parallel axis |
| Weight density | $\gamma = \rho g$; 9810 N/m³ for water |
| Work by a variable force | $W = \int F(x)\,dx$ |
| Root-mean-square (RMS) | $\sqrt{\frac{1}{T}\int_0^T f^2 dt}$; the equivalent constant for power purposes |

---

## Review Questions

### Conceptual

1. State the slicing principle in your own words, and explain how the area,
   volume, and work integrals in this chapter are all instances of it.
2. Explain why the area-between-curves formula works even when both curves lie
   below the $x$-axis.
3. Two curves cross inside the interval of interest. Explain what a single
   unsplit integral computes and why it is not the geometric area.
4. Describe a region for which horizontal slices are clearly easier than vertical
   slices, and say why.
5. A particle's velocity changes sign during an interval. Explain the difference
   between the two integrals that produce displacement and total distance.
6. Explain the difference between the disc, washer, and shell methods in terms of
   the orientation of the slice relative to the axis of revolution.
7. Why is the washer integrand $r_{\text{out}}^2 - r_{\text{in}}^2$ rather than
   $\left(r_{\text{out}} - r_{\text{in}}\right)^2$?
8. Why does the arc length formula contain a square root, and what geometric
   theorem produces it?
9. Explain why a surface-of-revolution integral uses $dL$ while a volume integral
   uses $dx$.
10. Explain the crossed-subscript convention in $Q_x = \int y\,dA$ and
    $I_x = \int y^2\,dA$.
11. Why must the factor $\frac{f+g}{2}$ appear in the $\bar{y}$ integral for a
    region between two curves?
12. Explain why the second moment of area is always positive while a first moment
    can be zero or negative.
13. Using the parallel axis theorem, explain why the centroidal axis gives the
    smallest second moment of any parallel axis.
14. A designer proposes doubling a beam's width to double its bending stiffness.
    Comment, with reference to the $bh^3$ dependence, and state what you would
    recommend instead.
15. Explain why the average value of a full cycle of a sinusoid is zero while its
    RMS value is not, and state which one an AC voltmeter displays.
16. State the centroid shortcut for pumping work, explain why it is valid, and
    give one situation in which it would not help.

### Calculation

17. Find the area of the region bounded by:
    (a) $y = 4 - x^2$ and $y = 0$
    (b) $y = x^2$ and $y = 4x$
    (c) $y = \sqrt{x}$ and $y = x$
    (d) $y = x^3$ and $y = 4x$ — note the crossing at the origin

18. Find the area bounded by $x = y^2 - 2$ and $x = y$, integrating with respect
    to $y$.

19. A particle has velocity $v(t) = t^2 - 4t + 3$ m/s on $0 \le t \le 4$ s.
    (a) Find the displacement.
    (b) Find the total distance travelled.
    (c) Find the average velocity and the average speed.

20. Find the volume generated by revolving each region about the stated axis:
    (a) the region under $y = x^2$ from $0$ to $2$, about the $x$-axis
    (b) the region under $y = \sqrt{x}$ from $0$ to $9$, about the $x$-axis
    (c) the region between $y = x$ and $y = x^2$, about the $x$-axis
    (d) the region under $y = x^2$ from $0$ to $2$, about the $y$-axis, using
    shells

21. The region bounded by $y = 4 - x^2$ and the $x$-axis is revolved about the
    $y$-axis. Find the volume two ways — by shells and by discs in $y$ — and
    confirm agreement.

22. Find the arc length of $y = \frac{2}{3}\left(x^2+1\right)^{3/2}$ from
    $x = 0$ to $x = 2$. (Hint: the radicand becomes a perfect square.)

23. The line $y = 3x$ from $x = 0$ to $x = 2$ is revolved about the $x$-axis. Find
    the lateral surface area by integration and verify against the cone formula
    $S = \pi r\ell$.

24. Find the area and centroid of the region bounded by:
    (a) $y = x$, $y = 0$, $x = 4$ — verify against the triangle formula
    (b) $y = x^3$, $y = 0$, $x = 2$
    (c) $y = 4 - x^2$ and $y = 0$ — use symmetry for $\bar{x}$

25. For a triangle of base $b$ and height $h$ with its base on the $x$-axis and
    its apex directly above the left end:
    (a) Find $A$ by integration.
    (b) Find $\bar{x}$ and $\bar{y}$ by integration.
    (c) Verify against the tabulated triangle centroid.

26. For a rectangle of width 60 mm and depth 150 mm:
    (a) Find $\bar{I}$ about the horizontal centroidal axis.
    (b) Find $I$ about the base by the parallel axis theorem.
    (c) Verify (b) by direct integration.
    (d) Find $\bar{I}$ about the vertical centroidal axis and comment on which
    orientation is stiffer in bending.

27. Find $\bar{I}$ about the horizontal centroidal axis for a triangle of base $b$
    and height $h$ with its base horizontal, by integration. Verify against the
    tabulated $\frac{bh^3}{36}$.

28. A spring requires 4.0 J of work to stretch it 0.20 m from its free length.
    (a) Find $k$.
    (b) Find the work to stretch it from 0.20 m to 0.35 m.
    (c) Find the total work to stretch it to 0.35 m and confirm additivity.

29. **Engineering application.** A vertical cylindrical tank of diameter 3.0 m and
    height 5.0 m is filled with water to a depth of 4.0 m.
    (a) Find the work to pump all the water to the tank rim.
    (b) Find the work to pump it to a point 2.0 m above the rim.
    (c) Verify (a) using the centroid shortcut.

30. **Engineering application.** A conical tank, apex down, has top radius 2.0 m
    and depth 3.0 m, and is full of water.
    (a) Set up the work integral to pump all the water to the top rim, showing the
    similar-triangles step.
    (b) Evaluate it.
    (c) Verify using the centroid shortcut, given that the centroid of a full cone
    with apex down lies at three quarters of the depth above the apex.

31. **Engineering application.** A beam of rectangular cross-section 120 mm wide by
    300 mm deep is being considered.
    (a) Find $\bar{I}$ about the horizontal centroidal axis.
    (b) A designer proposes reducing the depth to 250 mm and increasing the width
    to 173 mm, keeping the cross-sectional area essentially unchanged. Find the new
    $\bar{I}$ and the percentage change.
    (c) Comment on the design implication.

32. **Engineering application.** A triangular waveform rises linearly from $0$ to
    $V_m$ over $0 \le t \le \frac{T}{2}$ and falls linearly back to zero over
    $\frac{T}{2} \le t \le T$.
    (a) Find the simple average value over one period.
    (b) Find the RMS value by integration, exploiting symmetry.
    (c) Compare the ratio $\frac{f_{\text{rms}}}{V_m}$ to the sinusoidal value
    $0.7071$ and comment.

### Multiple Choice

33. The area between $y = x^2$ and $y = 2x$ is:
    A) $\dfrac{2}{3}$
    B) $\dfrac{4}{3}$
    C) $\dfrac{8}{3}$
    D) $4$

34. The volume generated by revolving the region under $y = x$ from $0$ to $3$
    about the $x$-axis is:
    A) $3\pi$
    B) $9\pi$
    C) $18\pi$
    D) $27\pi$

35. The shell-method volume element is:
    A) $\pi r^2 dx$
    B) $2\pi r h\,dr$
    C) $\pi\left(r_{\text{out}}^2 - r_{\text{in}}^2\right)dx$
    D) $2\pi r^2 dr$

36. The second moment of area of a rectangle about its horizontal centroidal axis
    is:
    A) $\dfrac{bh^3}{3}$
    B) $\dfrac{bh^3}{12}$
    C) $\dfrac{bh^3}{36}$
    D) $\dfrac{b^3h}{12}$

37. The parallel axis theorem states:
    A) $I = \bar{I} - Ad^2$
    B) $I = \bar{I} + Ad^2$
    C) $I = \bar{I} + Ad$
    D) $\bar{I} = I + Ad^2$

38. Doubling the depth of a rectangular beam section multiplies its centroidal
    second moment by:
    A) $2$
    B) $4$
    C) $8$
    D) $16$

39. The centroid of the region under $y = x^2$ from $0$ to $b$, bounded below by
    the $x$-axis, has $\bar{x}$ equal to:
    A) $\dfrac{b}{2}$
    B) $\dfrac{2b}{3}$
    C) $\dfrac{3b}{4}$
    D) $\dfrac{4b}{5}$

40. The RMS value of a sinusoid with peak amplitude $A$ is:
    A) $\dfrac{A}{2}$
    B) $\dfrac{A}{\sqrt{2}}$
    C) $\dfrac{2A}{\pi}$
    D) $A\sqrt{2}$

41. The work to stretch a spring of constant $k$ from $x_1$ to $x_2$ is:
    A) $k(x_2 - x_1)$
    B) $\dfrac{k}{2}(x_2 - x_1)^2$
    C) $\dfrac{k}{2}\left(x_2^2 - x_1^2\right)$
    D) $kx_2^2$

42. Total distance travelled by a particle whose velocity changes sign is found
    from:
    A) $\displaystyle\int_{t_1}^{t_2} v\,dt$
    B) $\displaystyle\int_{t_1}^{t_2}\lvert v\rvert\,dt$
    C) $s(t_2) - s(t_1)$
    D) $\bar{v}\left(t_2 - t_1\right)$

---

## Answer Key with Explanations

**1.** Every integral in the chapter has the form: identify a thin slice, write
what that one slice contributes to the total, integrate to add the contributions.
Area — the slice is a rectangle contributing $(\text{height})dx$. Volume — the
slice is a disc, washer, or shell contributing its own volume. Work — the slice is
an increment of displacement contributing $F\,dx$, or a layer of fluid contributing
$(\text{weight})\times(\text{lift})$. The integral sign is bookkeeping over the
addition; the physics or geometry is entirely in the slice contribution. (§20.1)

**2.** Because the formula uses the vertical **gap** between the curves, not their
distance from the axis. If $f \ge g$, then $f - g > 0$ regardless of whether either
is positive. Two curves both at negative $y$ still have a positive separation. The
$x$-axis plays no role, which makes the two-curve case simpler than the
single-curve case rather than harder. (§20.1)

**3.** An unsplit integral computes the **net signed** difference, in which regions
where $f > g$ contribute positively and regions where $g > f$ contribute
negatively. Those contributions partially or completely cancel. Worked Example 2 is
the extreme case: the net is exactly zero while the geometric area is 0.5. For
geometric area, split at each crossing and take the correct top curve on each
piece. (§20.1)

**4.** Any region whose left and right boundaries are single-valued functions of
$y$ while its upper or lower boundary requires two functions of $x$. The standard
case is a sideways parabola such as $x = y^2$ bounded by a vertical line: a
horizontal slice runs from the parabola to the line, one function each, while a
vertical slice spans from the lower branch $y = -\sqrt{x}$ to the upper branch
$y = +\sqrt{x}$ — two functions for one slice. Choose the direction that needs
fewer pieces. (§20.1)

**5.** $\int v\,dt$ gives **displacement**: intervals of negative velocity subtract,
so forward and backward motion cancel. $\int\lvert v\rvert dt$ gives **total
distance**: every interval contributes positively, so the two motions add. The
first is what a GPS start-to-finish measurement reports; the second is what an
odometer reads. Compute the second by splitting at the zeros of $v$ and negating the
negative intervals. (§20.2)

**6.** It is entirely about slice orientation relative to the axis of revolution.

**Perpendicular** to the axis, touching it: the slice sweeps a solid **disc**.

**Perpendicular** to the axis, not touching it: the slice sweeps a **washer**, an
annulus with a hole.

**Parallel** to the axis: the slice sweeps a **cylindrical shell**, a thin-walled
tube.

Both approaches give the same volume; the choice is about which integral you can
evaluate. (§20.3, §20.4)

**7.** Because you are subtracting two **areas**, not squaring a difference of two
lengths. The annulus is a circle of area $\pi r_{\text{out}}^2$ with a circle of
area $\pi r_{\text{in}}^2$ removed. Numerically with $r_{\text{out}} = 3$ and
$r_{\text{in}} = 1$: the correct value is $\pi(9-1) = 8\pi$, while
$\pi(3-1)^2 = 4\pi$. Off by a factor of two, and the discrepancy grows as the radii
converge. (§20.3)

**8.** Because a short piece of curve is the hypotenuse of a right triangle with
legs $dx$ and $dy$, and the **Pythagorean theorem** gives its length as
$\sqrt{(dx)^2 + (dy)^2}$. Factoring $dx$ out of the radical produces
$\sqrt{1 + (dy/dx)^2}\,dx$. The square root is the Pythagorean theorem, nothing
more. (§20.5)

**9.** A volume slice is a plate of **thickness** $dx$ measured perpendicular to
its face, so its volume is (face area)$\times dx$. A surface band follows the
**surface**, whose width is measured along the slant, so it is
(circumference)$\times dL$. Worked Example 8 quantifies the difference: on a cone
of radius 2 and height 4, using $dx$ gives 25.1 against the correct 28.1, an 11%
understatement. The steeper the curve, the larger the discrepancy. (§20.5)

**10.** The subscript names the **axis about which the moment is taken**, and the
distance in the integrand is measured **perpendicular** to that axis. Distance from
the $x$-axis is $y$, so $Q_x = \int y\,dA$ and $I_x = \int y^2\,dA$. Distance from
the $y$-axis is $x$, so $Q_y = \int x\,dA$ and $I_y = \int x^2\,dA$. The convention
looks crossed but is consistent, and it is universal in engineering references.
(§20.6, §20.7)

**11.** Because a slice contributes its area at its **own centroid height**, which
is the midpoint of the slice, not its top. A vertical slice spanning from $g$ up to
$f$ has its centre at $\frac{f+g}{2}$. So the contribution to the first moment is
$\frac{f+g}{2}\big[f-g\big]dx$. Omitting the factor of one half for a region
sitting on the $x$-axis exactly doubles $\bar{y}$. (§20.6)

**12.** The second moment integrand contains $y^2$, which is non-negative
everywhere, so every element of a real area contributes positively and nothing can
cancel. The first moment integrand contains $y$ to the first power, which is
negative below the axis, so contributions can cancel — and they cancel exactly when
the axis passes through the centroid, which is the defining property of the
centroid. (§20.6, §20.7)

**13.** The theorem is $I = \bar{I} + Ad^2$. Both $A$ and $d^2$ are non-negative,
so the transfer term can never reduce the value: $I \ge \bar{I}$ for every parallel
axis, with equality only when $d = 0$, which is the centroidal axis itself.
Therefore the centroidal axis is the unique minimizer. (§20.7)

**14.** The proposal is inefficient. From $\bar{I} = \frac{bh^3}{12}$, stiffness is
**linear** in width and **cubic** in depth. Doubling $b$ doubles $\bar{I}$;
doubling $h$ multiplies it by eight. For the same added material, depth delivers
four times the benefit at this scale.

The recommendation is to increase depth instead, subject to the practical limits —
clearance, and lateral-torsional stability, since a very deep narrow section
becomes prone to buckling sideways. This is precisely why floor joists are
installed on edge rather than laid flat, and why I-beams push material into flanges
at maximum distance from the neutral axis. (§20.7)

**15.** Over a full cycle the sinusoid spends equal time equally far above and below
zero, so the signed area cancels exactly and the simple average is zero. That
number is correct and useless — it tells you nothing about the waveform's ability
to deliver power.

The RMS value squares first, which makes every contribution positive, so no
cancellation occurs. It is the physically meaningful average because resistive
power goes as the square of voltage or current, making the RMS value the equivalent
constant DC value for heating purposes.

An AC voltmeter displays the **RMS** value. (§20.9)

**16.** The shortcut is: $W = (\text{total weight}) \times (\text{lift distance of
the centroid})$.

It is valid because the lift distance is a **linear** function of position, so the
sum of (weight)$\times$(individual lift) equals (total weight)$\times$(average
lift), and the weighted average lift is by definition the centroid lift.

It does not help when the cross-section varies and the centroid is not already
known, because locating the centroid is then itself an integral of comparable
difficulty — you would be trading one integral for another. It also fails if the
destination height varies with the slice. (§20.8)

**17.**

**(a)** Roots of $4 - x^2 = 0$ are $x = \pm 2$. Even integrand:

$$A = \int_{-2}^{2}\left(4-x^2\right)dx = 2\int_0^2\left(4-x^2\right)dx = 2\left[4x - \frac{x^3}{3}\right]_0^2 = 2\left(8 - \frac{8}{3}\right) = \boxed{\frac{32}{3} = 10.67}$$

**(b)** $x^2 = 4x \implies x = 0, 4$. Test $x = 1$: line 4, parabola 1 — line on
top.

$$A = \int_0^4\left(4x - x^2\right)dx = \left[2x^2 - \frac{x^3}{3}\right]_0^4 = 32 - \frac{64}{3} = \boxed{\frac{32}{3} = 10.67}$$

**(c)** $\sqrt{x} = x \implies x = x^2 \implies x = 0, 1$. Test $x = 0.25$:
$\sqrt{x} = 0.5$, $x = 0.25$ — the radical is on top.

$$A = \int_0^1\left(x^{1/2} - x\right)dx = \left[\frac{2}{3}x^{3/2} - \frac{x^2}{2}\right]_0^1 = \frac{2}{3} - \frac{1}{2} = \boxed{\frac{1}{6} = 0.1667}$$

**(d)** $x^3 = 4x \implies x\left(x^2-4\right) = 0 \implies x = -2, 0, 2$. There is
a crossing at the origin, so split.

On $(0,2)$, test $x = 1$: $4x = 4$, $x^3 = 1$ — the line is on top.
On $(-2,0)$, test $x = -1$: $4x = -4$, $x^3 = -1$ — the cubic is on top.

Both integrands are even in the sense that the configuration is symmetric about the
origin (both functions odd), so compute one piece and double:

$$A_1 = \int_0^2\left(4x - x^3\right)dx = \left[2x^2 - \frac{x^4}{4}\right]_0^2 = 8 - 4 = 4$$

$$A = 2(4) = \boxed{8.00}$$

**18.** Intersections: $y^2 - 2 = y \implies y^2 - y - 2 = 0 \implies (y-2)(y+1) = 0$,
so $y = -1, 2$.

Test $y = 0$: the line gives $x = 0$, the parabola gives $x = -2$. The **line** is
on the right.

$$A = \int_{-1}^{2}\left[y - \left(y^2-2\right)\right]dy = \int_{-1}^{2}\left(y + 2 - y^2\right)dy$$

This is the same integrand as Worked Example 1, so

$$A = \boxed{4.50}$$

**19.**

Factor the velocity: $v = t^2 - 4t + 3 = (t-1)(t-3)$, zero at $t = 1$ and $t = 3$,
negative on $(1,3)$.

Antiderivative: $s(t) = \frac{t^3}{3} - 2t^2 + 3t$.

$$s(0) = 0 \qquad s(1) = \frac{1}{3} - 2 + 3 = 1.3333$$
$$s(3) = 9 - 18 + 9 = 0 \qquad s(4) = \frac{64}{3} - 32 + 12 = 21.333 - 20 = 1.3333$$

**(a)** Displacement $= s(4) - s(0) = \boxed{1.33 \text{ m}}$

**(b)**

| Interval | $\Delta s$ | Distance |
|---|---|---|
| $[0,1]$ | $+1.3333$ | $1.3333$ |
| $[1,3]$ | $-1.3333$ | $1.3333$ |
| $[3,4]$ | $+1.3333$ | $1.3333$ |

Total distance $= 3(1.3333) = \boxed{4.00 \text{ m}}$

**(c)** Average velocity $= \frac{1.3333}{4} = \boxed{0.333 \text{ m/s}}$;
average speed $= \frac{4.00}{4} = \boxed{1.00 \text{ m/s}}$

**20.**

**(a)** Discs, $r = x^2$:

$$V = \pi\int_0^2 x^4 dx = \pi\left[\frac{x^5}{5}\right]_0^2 = \frac{32\pi}{5} = \boxed{20.1}$$

**(b)** Discs, $r = \sqrt{x}$:

$$V = \pi\int_0^9 x\,dx = \pi\left[\frac{x^2}{2}\right]_0^9 = \frac{81\pi}{2} = \boxed{127}$$

**(c)** $x = x^2$ at $x = 0, 1$; the line is outer.

$$V = \pi\int_0^1\left(x^2 - x^4\right)dx = \pi\left[\frac{x^3}{3} - \frac{x^5}{5}\right]_0^1 = \pi\left(\frac{1}{3}-\frac{1}{5}\right) = \frac{2\pi}{15} = \boxed{0.419}$$

**(d)** Shells, $r = x$, $h = x^2$:

$$V = 2\pi\int_0^2 x\left(x^2\right)dx = 2\pi\left[\frac{x^4}{4}\right]_0^2 = 2\pi(4) = 8\pi = \boxed{25.1}$$

**21.**

**Shells.** $r = x$, $h = 4 - x^2$, from $x = 0$ to $2$ (the right half generates
the whole solid):

$$V = 2\pi\int_0^2 x\left(4-x^2\right)dx = 2\pi\int_0^2\left(4x - x^3\right)dx = 2\pi\left[2x^2 - \frac{x^4}{4}\right]_0^2$$

$$= 2\pi(8-4) = 8\pi = \boxed{25.1}$$

**Discs in $y$.** From $y = 4-x^2$, $x^2 = 4 - y$, so $r^2 = 4-y$, for
$0 \le y \le 4$:

$$V = \pi\int_0^4(4-y)\,dy = \pi\left[4y - \frac{y^2}{2}\right]_0^4 = \pi(16-8) = 8\pi \;\checkmark$$

Agreement confirmed.

**22.**

$$\frac{dy}{dx} = \frac{2}{3}\cdot\frac{3}{2}\left(x^2+1\right)^{1/2}(2x) = 2x\left(x^2+1\right)^{1/2}$$

$$\left(\frac{dy}{dx}\right)^2 = 4x^2\left(x^2+1\right) = 4x^4 + 4x^2$$

$$1 + 4x^4 + 4x^2 = \left(2x^2+1\right)^2$$

The radicand is a perfect square, as promised:

$$L = \int_0^2\left(2x^2+1\right)dx = \left[\frac{2x^3}{3} + x\right]_0^2 = \frac{16}{3} + 2 = \boxed{7.33}$$

**Chord check.** Endpoints $(0, \frac{2}{3})$ and
$\left(2, \frac{2}{3}(5)^{3/2}\right) = (2, 7.454)$. Chord length
$\sqrt{4 + 46.02} = \sqrt{50.02} = 7.072$. Arc $7.333 > 7.072$ ✓

**23.**

$$\frac{dy}{dx} = 3 \implies \sqrt{1+9} = \sqrt{10} = 3.16228$$

$$S = 2\pi\int_0^2 3x(3.16228)\,dx = 2\pi(9.48683)\left[\frac{x^2}{2}\right]_0^2 = 2\pi(9.48683)(2)$$

$$S = 2\pi(18.9737) = \boxed{119.2}$$

**Verify.** At $x = 2$, $r = 6$; height $h = 2$; slant
$\ell = \sqrt{36+4} = \sqrt{40} = 6.32456$.

$$S = \pi r\ell = \pi(6)(6.32456) = 119.2 \;\checkmark$$

**24.**

**(a)** $A = \int_0^4 x\,dx = 8$.

$$\bar{x} = \frac{1}{8}\int_0^4 x(x)\,dx = \frac{1}{8}\left[\frac{x^3}{3}\right]_0^4 = \frac{64/3}{8} = \frac{8}{3} = 2.667$$

$$\bar{y} = \frac{1}{8}\int_0^4\frac{x}{2}(x)\,dx = \frac{1}{8}\cdot\frac{1}{2}\left[\frac{x^3}{3}\right]_0^4 = \frac{64/6}{8} = \frac{4}{3} = 1.333$$

$$\boxed{A = 8.00, \; \bar{x} = 2.67, \; \bar{y} = 1.33}$$

**Verify against the triangle.** Base 4, height 4, so $A = \frac{1}{2}(4)(4) = 8$ ✓
The centroid of a triangle lies one third of the way from any side toward the
opposite vertex. Measuring from the vertical side $x = 4$: $\bar{x} = 4 - \frac{4}{3}
= \frac{8}{3}$ ✓ Measuring from the base: $\bar{y} = \frac{4}{3}$ ✓

**(b)** $A = \int_0^2 x^3 dx = \left[\frac{x^4}{4}\right]_0^2 = 4$.

$$\bar{x} = \frac{1}{4}\int_0^2 x^4 dx = \frac{1}{4}\cdot\frac{32}{5} = \frac{8}{5} = 1.600$$

$$\bar{y} = \frac{1}{4}\int_0^2\frac{x^3}{2}\left(x^3\right)dx = \frac{1}{8}\left[\frac{x^7}{7}\right]_0^2 = \frac{128/7}{8} = \frac{16}{7} = 2.286$$

$$\boxed{A = 4.00, \; \bar{x} = 1.60, \; \bar{y} = 2.29}$$

Bounding box is $0 \le x \le 2$, $0 \le y \le 8$; the centroid is inside ✓

**(c)** From 17(a), $A = \frac{32}{3} = 10.667$.

By symmetry about the $y$-axis, $\bar{x} = 0$.

$$\bar{y} = \frac{1}{A}\int_{-2}^{2}\frac{4-x^2}{2}\left(4-x^2\right)dx = \frac{1}{2A}\int_{-2}^{2}\left(4-x^2\right)^2 dx$$

The integrand is even:

$$\int_{-2}^{2}\left(16 - 8x^2 + x^4\right)dx = 2\left[16x - \frac{8x^3}{3} + \frac{x^5}{5}\right]_0^2 = 2\left(32 - \frac{64}{3} + \frac{32}{5}\right)$$

$$= 2\left(32 - 21.3333 + 6.4\right) = 2(17.0667) = 34.1333$$

$$\bar{y} = \frac{34.1333}{2(10.667)} = \frac{34.1333}{21.333} = 1.600$$

$$\boxed{\bar{x} = 0, \; \bar{y} = 1.60}$$

Sanity: the maximum height is 4, and 1.60 is below mid-height, correct for a region
that narrows toward the top ✓

**25.**

Place the apex above the left end, so the hypotenuse runs from $(0,h)$ down to
$(b,0)$:

$$y = h\left(1 - \frac{x}{b}\right)$$

**(a)**

$$A = \int_0^b h\left(1-\frac{x}{b}\right)dx = h\left[x - \frac{x^2}{2b}\right]_0^b = h\left(b - \frac{b}{2}\right) = \boxed{\frac{bh}{2}}$$

**(b)**

$$Q_y = \int_0^b x\,h\left(1-\frac{x}{b}\right)dx = h\left[\frac{x^2}{2} - \frac{x^3}{3b}\right]_0^b = h\left(\frac{b^2}{2} - \frac{b^2}{3}\right) = \frac{hb^2}{6}$$

$$\bar{x} = \frac{hb^2/6}{bh/2} = \boxed{\frac{b}{3}}$$

$$Q_x = \int_0^b\frac{y}{2}(y)\,dx = \frac{h^2}{2}\int_0^b\left(1-\frac{x}{b}\right)^2 dx$$

Substituting $u = 1 - \frac{x}{b}$, $du = -\frac{dx}{b}$, limits $u = 1$ to $0$:

$$= \frac{h^2}{2}(b)\int_0^1 u^2 du = \frac{h^2 b}{2}\cdot\frac{1}{3} = \frac{bh^2}{6}$$

$$\bar{y} = \frac{bh^2/6}{bh/2} = \boxed{\frac{h}{3}}$$

**(c)** The tabulated triangle centroid lies one third of the way from each side
toward the opposite vertex. Measuring from the left edge, $\bar{x} = \frac{b}{3}$ ✓
Measuring from the base, $\bar{y} = \frac{h}{3}$ ✓ Both match.

**26.**

$b = 60$ mm, $h = 150$ mm, $A = 9000$ mm².

**(a)** $h^3 = 150^3 = 3.375\times10^6$

$$\bar{I} = \frac{60\left(3.375\times10^6\right)}{12} = \frac{2.025\times10^8}{12} = \boxed{16.9\times10^6 \text{ mm}^4}$$

**(b)** $d = 75$ mm:

$$I = 16.875\times10^6 + 9000(75)^2 = 16.875\times10^6 + 50.625\times10^6 = \boxed{67.5\times10^6 \text{ mm}^4}$$

**(c)** $\frac{bh^3}{3} = \frac{2.025\times10^8}{3} = 67.5\times10^6$ mm⁴ ✓

**(d)** About the vertical centroidal axis the roles of $b$ and $h$ swap:

$$\bar{I}_y = \frac{hb^3}{12} = \frac{150(60)^3}{12} = \frac{150\left(2.16\times10^5\right)}{12} = \frac{3.24\times10^7}{12} = 2.70\times10^6 \text{ mm}^4$$

Bending about the **horizontal** centroidal axis — that is, with the 150 mm
dimension vertical, the member on edge — gives $16.9\times10^6$ mm⁴ against
$2.70\times10^6$ mm⁴, a factor of 6.25 stiffer. Orientation alone changes bending
stiffness by more than sixfold with no change of material. The ratio is
$\left(\frac{150}{60}\right)^2 = 6.25$, which is the general result for a
rectangle.

**27.**

Place the base on the $x$-axis with the apex above. At height $y$ the width tapers
linearly from $b$ at $y = 0$ to zero at $y = h$:

$$w(y) = b\left(1 - \frac{y}{h}\right)$$

First locate the centroid, which from Question 25 is at $\bar{y} = \frac{h}{3}$.

**Second moment about the base:**

$$I_{\text{base}} = \int_0^h y^2 b\left(1-\frac{y}{h}\right)dy = b\int_0^h\left(y^2 - \frac{y^3}{h}\right)dy = b\left[\frac{y^3}{3} - \frac{y^4}{4h}\right]_0^h$$

$$= b\left(\frac{h^3}{3} - \frac{h^3}{4}\right) = bh^3\left(\frac{4-3}{12}\right) = \frac{bh^3}{12}$$

**Transfer to the centroidal axis** using the parallel axis theorem in reverse,
with $A = \frac{bh}{2}$ and $d = \frac{h}{3}$:

$$\bar{I} = I_{\text{base}} - Ad^2 = \frac{bh^3}{12} - \frac{bh}{2}\cdot\frac{h^2}{9} = \frac{bh^3}{12} - \frac{bh^3}{18}$$

Common denominator 36:

$$= \frac{3bh^3 - 2bh^3}{36} = \boxed{\frac{bh^3}{36}}$$

Matches the tabulated value ✓

Note that this is the one legitimate use of the theorem "in reverse" — subtracting
$Ad^2$ to move *toward* the centroidal axis. It is valid because you know the
starting axis is parallel to the centroidal axis at a known distance. It remains
wrong to transfer between two arbitrary non-centroidal axes in a single step.

**28.**

**(a)** $W = \frac{k}{2}x^2 \implies 4.0 = \frac{k}{2}(0.20)^2 = 0.020k$

$$k = \frac{4.0}{0.020} = \boxed{200 \text{ N/m}}$$

**(b)**

$$W = \frac{200}{2}\left(0.35^2 - 0.20^2\right) = 100(0.1225 - 0.0400) = 100(0.0825) = \boxed{8.25 \text{ J}}$$

**(c)** Total to 0.35 m: $100(0.1225) = 12.25$ J. And $4.00 + 8.25 = 12.25$ J ✓

Note again that the second, shorter stretch of 0.15 m costs more than twice the
first stretch of 0.20 m.

**29.**

$r = 1.5$ m, so $A = \pi(2.25) = 7.06858$ m². Water fills $0 \le y \le 4.0$ m; the
rim is at $y = 5.0$ m.

$$\gamma A = 9810(7.06858) = 69{,}342.8 \text{ N/m}$$

**(a)** Lift to the rim is $(5.0 - y)$:

$$\int_0^{4.0}(5.0-y)\,dy = \left[5.0y - \frac{y^2}{2}\right]_0^{4.0} = 20.0 - 8.0 = 12.0 \text{ m}^2$$

$$W = 69{,}342.8(12.0) = 832{,}114 \text{ J} = \boxed{832 \text{ kJ}}$$

**(b)** Destination now $y = 7.0$ m:

$$\int_0^{4.0}(7.0-y)\,dy = 28.0 - 8.0 = 20.0 \text{ m}^2$$

$$W = 69{,}342.8(20.0) = 1{,}386{,}856 \text{ J} = \boxed{1387 \text{ kJ}}$$

**(c)** Water volume $= 7.06858(4.0) = 28.2743$ m³; weight
$= 9810(28.2743) = 277{,}371$ N. Centroid at $y = 2.0$ m, so the lift is
$5.0 - 2.0 = 3.0$ m:

$$W = 277{,}371(3.0) = 832{,}114 \text{ J} \;\checkmark$$

Exact agreement with (a).

**30.**

**(a)** Measure $y$ upward from the apex. By similar triangles, the water radius at
height $y$ is

$$\frac{r}{y} = \frac{2.0}{3.0} \implies r = \frac{2y}{3}$$

Slice area:

$$A(y) = \pi r^2 = \pi\frac{4y^2}{9}$$

Lift to the rim at $y = 3.0$: distance $(3.0 - y)$.

$$W = \gamma\int_0^{3.0}(3.0-y)\,\pi\frac{4y^2}{9}\,dy$$

**(b)**

$$= 9810\cdot\frac{4\pi}{9}\int_0^{3.0}\left(3.0y^2 - y^3\right)dy$$

$$\frac{4\pi}{9} = 1.396263 \implies 9810(1.396263) = 13{,}697.3$$

$$\int_0^{3.0}\left(3y^2 - y^3\right)dy = \left[y^3 - \frac{y^4}{4}\right]_0^{3.0} = 27.0 - 20.25 = 6.75$$

$$W = 13{,}697.3(6.75) = 92{,}457 \text{ J} = \boxed{92.5 \text{ kJ}}$$

**(c)** Cone volume $= \frac{1}{3}\pi(2.0)^2(3.0) = \frac{1}{3}\pi(12.0) =
12.5664$ m³; weight $= 9810(12.5664) = 123{,}276$ N.

Centroid at three quarters of the depth above the apex: $y = 0.75(3.0) = 2.25$ m,
so the lift is $3.0 - 2.25 = 0.75$ m.

$$W = 123{,}276(0.75) = 92{,}457 \text{ J} \;\checkmark$$

Exact agreement.

**Worth noting.** The cone requires only 92.5 kJ where a cylinder of the same
radius and depth would require far more — because most of a cone's water sits near
the top and needs almost no lifting. Comparing: a cylinder of radius 2.0 m and
depth 3.0 m holds $\pi(4)(3) = 37.70$ m³, weighing 369,830 N, with centroid at
1.5 m and lift 1.5 m, giving 555 kJ. Six times the work for three times the water,
because the geometry puts the cylinder's water lower down.

**31.**

**(a)** $b = 120$ mm, $h = 300$ mm. $h^3 = 2.70\times10^7$:

$$\bar{I} = \frac{120\left(2.70\times10^7\right)}{12} = \frac{3.24\times10^9}{12} = \boxed{270\times10^6 \text{ mm}^4}$$

**(b)** $b = 173$ mm, $h = 250$ mm. Check the area first:
$173(250) = 43{,}250$ mm² against the original $120(300) = 36{,}000$ mm². These are
not equal — the proposal as stated increases material by 20%, so the comparison is
not like-for-like. Note that and proceed with the arithmetic as asked.

$h^3 = 1.5625\times10^7$:

$$\bar{I} = \frac{173\left(1.5625\times10^7\right)}{12} = \frac{2.70313\times10^9}{12} = 225\times10^6 \text{ mm}^4$$

$$\text{change} = \frac{225 - 270}{270} = -0.167 = \boxed{-16.7\%}$$

**(c)** The proposal loses 16.7% of the bending stiffness **while using 20% more
material**. That is a clearly bad trade, and the arithmetic explains why: the 50 mm
reduction in depth costs more than the 53 mm increase in width can recover, because
depth enters cubed and width only linearly.

For a genuinely area-neutral comparison, keeping $bh = 36{,}000$ mm² with
$h = 250$ mm requires $b = 144$ mm, giving

$$\bar{I} = \frac{144\left(1.5625\times10^7\right)}{12} = 187.5\times10^6 \text{ mm}^4$$

a 30.6% loss for the same material. Either way the conclusion holds: **when
material is fixed, spend it on depth.** Reducing depth to gain width is always a
losing exchange for bending stiffness.

**32.**

**(a)** The waveform is a triangle of peak $V_m$ over base $T$. Its average is the
area under one period divided by $T$. Area $= \frac{1}{2}(T)(V_m)$:

$$\bar{v} = \frac{\frac{1}{2}TV_m}{T} = \boxed{\frac{V_m}{2} = 0.500V_m}$$

Note this waveform never goes negative, so its simple average is not zero — unlike
the sinusoid of Worked Example 14.

**(b)** By symmetry the two halves contribute equally to the mean square, so
compute the rising half and it represents the whole. On $0 \le t \le \frac{T}{2}$:

$$v(t) = \frac{2V_m}{T}t$$

$$\frac{1}{T}\int_0^T v^2 dt = \frac{2}{T}\int_0^{T/2}\frac{4V_m^2}{T^2}t^2\,dt = \frac{8V_m^2}{T^3}\left[\frac{t^3}{3}\right]_0^{T/2}$$

$$= \frac{8V_m^2}{T^3}\cdot\frac{T^3}{24} = \frac{V_m^2}{3}$$

$$v_{\text{rms}} = \boxed{\frac{V_m}{\sqrt{3}} = 0.577V_m}$$

**(c)** The triangular ratio is $0.577$ against the sinusoidal $0.707$. The
triangle has the lower RMS value for the same peak, because it spends more of its
period at small amplitudes — it passes through the peak instantaneously, while a
sinusoid lingers near its crest.

The practical consequence: **the factor $0.707$ is not a universal conversion from
peak to RMS.** It is specific to sinusoids. Applying it to a triangular waveform
overstates the RMS value by 22.5%, and therefore overstates delivered power by
about 50%, since power goes as the square.

**33. B — $\frac{4}{3}$.** Intersections at $x = 0$ and $x = 2$; the line is on
top.

$$\int_0^2\left(2x - x^2\right)dx = \left[x^2 - \frac{x^3}{3}\right]_0^2 = 4 - \frac{8}{3} = \frac{4}{3}$$

Choice C, $\frac{8}{3}$, is $\int x^2 dx$ alone — the area under the parabola
rather than between the curves. (§20.1)

**34. B — $9\pi$.** Discs with $r = x$:

$$\pi\int_0^3 x^2 dx = \pi\left[\frac{x^3}{3}\right]_0^3 = 9\pi$$

This is the cone of radius 3 and height 3; check with $\frac{1}{3}\pi r^2 h =
\frac{1}{3}\pi(9)(3) = 9\pi$ ✓ Choice D, $27\pi$, omits the one third — it is the
enclosing cylinder. (§20.3)

**35. B — $2\pi rh\,dr$.** Choice A is the disc element, choice C the washer
element. Choice D has the wrong power of $r$ and would not have units of volume
when integrated. (§20.4)

**36. B — $\frac{bh^3}{12}$.** Choice A is about the base, choice C is the
centroidal value for a **triangle**, and choice D is the centroidal second moment
about the **vertical** axis. All four appear in the Handbook tables, so read which
shape and which axis the question specifies. (§20.7)

**37. B — $I = \bar{I} + Ad^2$.** The transfer term is added and $d$ is squared. Choice
A has the sign backwards, which would make some second moments negative. Choice C
omits the square. Choice D has the roles of $I$ and $\bar{I}$ reversed, which would
make the centroidal axis the maximum rather than the minimum. (§20.7)

**38. C — 8.** $\bar{I} = \frac{bh^3}{12}$ and $2^3 = 8$. Choice A is the effect of
doubling the **width**; choice B would be the case if $h$ entered squared. (§20.7)

**39. C — $\frac{3b}{4}$.**

$$\bar{x} = \frac{\int_0^b x\left(x^2\right)dx}{\int_0^b x^2 dx} = \frac{b^4/4}{b^3/3} = \frac{3b}{4}$$

Choice A, $\frac{b}{2}$, would be correct for a rectangle. The centroid of the
parabolic spandrel sits right of centre because the area bunches toward $x = b$.
(§20.6)

**40. B — $\frac{A}{\sqrt{2}}$.** From Worked Example 14. Choice C, $\frac{2A}{\pi}$,
is the **average of a rectified** sinusoid — a real quantity, and a distractor
worth recognizing, since it is what a simple rectifier-and-averaging meter actually
measures before being scaled to read RMS. (§20.9)

**41. C — $\frac{k}{2}\left(x_2^2 - x_1^2\right)$.**

$$\int_{x_1}^{x_2}kx\,dx = \frac{k}{2}\left[x^2\right]_{x_1}^{x_2}$$

Choice B is the very common error of squaring the displacement rather than
differencing the squares. Test both with $k = 200$, $x_1 = 0.20$, $x_2 = 0.35$ from
Question 28: choice C gives 8.25 J, choice B gives $100(0.15)^2 = 2.25$ J. Not
close. (§20.8)

**42. B — $\int\lvert v\rvert dt$.** Choices A and C both give displacement, and
they are equal to each other by the Fundamental Theorem. Choice D also gives
displacement, since $\bar{v}$ is defined as displacement over elapsed time.
Three distractors, all the same wrong quantity. (§20.2)

---

## Quick Reference

**Area** — *Handbook, Integral Calculus*

$$A = \int_a^b\big[y_{\text{top}} - y_{\text{bottom}}\big]dx \qquad A = \int_c^d\big[x_{\text{right}} - x_{\text{left}}\big]dy$$

Split at every intersection interior to the interval.

**Net versus total**

$$\text{net} = \int v\,dt \qquad \text{total} = \int\lvert v\rvert\,dt$$

**Volume**

| Method | Element | Use when |
|---|---|---|
| Disc | $dV = \pi r^2\,dx$ | slice ⟂ axis, touching it |
| Washer | $dV = \pi\left(r_{\text{out}}^2 - r_{\text{in}}^2\right)dx$ | slice ⟂ axis, not touching |
| Shell | $dV = 2\pi rh\,dr$ | slice ∥ axis |
| General slicing | $dV = A(x)\,dx$ | cross-section known |

**Arc length and surface**

$$L = \int_a^b\sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx \qquad S = 2\pi\int_a^b r\sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$$

Check any arc length against the chord: the arc must be longer.

**Centroid and first moment**

$$Q_x = \int y\,dA = A\bar{y} \qquad Q_y = \int x\,dA = A\bar{x}$$

With vertical slices between $f$ (top) and $g$ (bottom):

$$\bar{x} = \frac{1}{A}\int x\big[f-g\big]dx \qquad \bar{y} = \frac{1}{A}\int\frac{f+g}{2}\big[f-g\big]dx$$

Units of $Q$: L³. The centroid must lie in the bounding box.

**Second moment of area**

$$I_x = \int y^2\,dA \qquad I_y = \int x^2\,dA \qquad \boxed{I = \bar{I} + Ad^2}$$

Units: L⁴. Always positive. The centroidal axis is the minimum.

| Shape | $\bar{I}$ about horizontal centroidal axis |
|---|---|
| Rectangle $b\times h$ | $\dfrac{bh^3}{12}$ |
| Rectangle, about base | $\dfrac{bh^3}{3}$ |
| Triangle, base $b$ | $\dfrac{bh^3}{36}$ |
| Circle, diameter $d$ | $\dfrac{\pi d^4}{64}$ |

Depth enters **cubed**: doubling $h$ multiplies $\bar{I}$ by 8.

**Work**

$$W = \int_a^b F(x)\,dx \qquad \text{spring: } W = \frac{k}{2}\left(x_2^2 - x_1^2\right)$$

$$\text{pumping: } W = \gamma\int\big(y_{\text{dest}} - y\big)A(y)\,dy$$

$\gamma_{\text{water}} = 9810$ N/m³. Check against
(total weight)$\times$(centroid lift).

**RMS**

$$f_{\text{rms}} = \sqrt{\frac{1}{T}\int_0^T f^2\,dt}$$

| Waveform | $f_{\text{rms}}$ |
|---|---|
| Sinusoid, peak $A$ | $\dfrac{A}{\sqrt{2}} = 0.707A$ |
| Triangle, peak $A$ | $\dfrac{A}{\sqrt{3}} = 0.577A$ |
| Square, peak $A$ | $A$ |

The 0.707 factor is **sinusoid-specific**.

---

## Looking Ahead

Chapter 01-21 returns to integration technique. Substitution handles compositions,
but it fails on products such as $\int xe^x dx$ and on rational functions with
factorable denominators. That chapter builds integration by parts and partial
fractions, which together close most of the remaining gap — and integration by
parts, in particular, is what makes the arc length and surface area integrals of
this chapter tractable for a wider class of curves.

The applications you have built here do not change. Only the toolkit for evaluating
them grows.

