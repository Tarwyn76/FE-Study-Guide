---
chapter: "01-23"
title: "Partial Derivatives and Vector Calculus"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-023-01, MATH-1C-023-02, MATH-1C-023-03, MATH-1C-023-04, MATH-1C-023-05, MATH-1C-023-06, MATH-1C-023-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-23: Partial Derivatives and Vector Calculus

> *"Nothing in engineering depends on one variable. Pressure drop depends on flow
> rate, diameter, roughness, and viscosity. Stress depends on load, area, and
> geometry. Every measurement you combine carries its own uncertainty into the
> result. Single-variable calculus cannot touch any of that. Partial
> differentiation can, and it does it with one idea: hold everything else still
> and differentiate the one thing you are varying."*

---

## Before You Start

**Prerequisites:** [01-09 Lines and Analytic Geometry](01-09-lines-analytic-geometry.md) · [01-11 Trigonometry](01-11-trigonometry.md) · [01-13 Vectors in Two and Three Dimensions](01-13-vectors.md) · [01-16 Limits and Continuity](01-16-limits-continuity.md) · [01-17 The Derivative](01-17-the-derivative.md) · [01-18 Applications of the Derivative](01-18-applications-of-the-derivative.md) · [01-22 Infinite Series and Taylor Expansions](01-22-infinite-series-taylor.md)

**Skip if:** You pass the Tier 1C test-out quiz. Verify you can compute a mixed
second partial, propagate uncertainty through a product of powers using the total
differential, and write the gradient, divergence, and curl from memory before
skipping. The total differential is the item to be honest about — it is the single
most used result in this chapter across all seven disciplines, and it appears
inside problems that never mention partial derivatives.

**Time:** ~85 min read · ~30 min review questions · ~90 min practice problems

---

## On the Board Today

Apprentice, everything through Chapter 01-22 assumed one input and one output.
Real engineering functions do not look like that.

$$Q = \frac{\pi D^2}{4}v \qquad \sigma = \frac{Mc}{I} \qquad P = \frac{V^2}{R} \qquad pV = nRT$$

Four variables, three variables, two variables, four variables. Each of those is a
function of several inputs, and the questions you need to answer about them are
familiar in form but not in machinery.

**How sensitive is the output to each input?** That is a derivative question, but
now there is one derivative per input. Those are the **partial derivatives**, and
computing them requires no new technique at all — you differentiate with respect to
one variable while treating the others as constants, using exactly the rules from
Chapter 01-17.

**How do all the uncertainties combine?** Every measured input carries an error
bar. The **total differential** assembles the individual sensitivities into one
statement about the output's uncertainty, and it is the most practically valuable
result in this chapter. It generalizes the differential from Chapter 01-18 and, as
we will verify, it reproduces the power-law error rule you already met there.

**Which direction is uphill?** For a function of position — a temperature field, a
pressure field, an elevation — the answer is a *vector*, because there are now many
directions to choose from. That vector is the **gradient**, and it points the way
heat flows, water runs, and charge moves.

**What is a vector field doing locally?** Two questions, two answers.
**Divergence** measures whether the field is spreading out from a point — whether
there is a source or a sink there. **Curl** measures whether the field is
circulating around a point. Both are built from partial derivatives combined with
the dot and cross products from Chapter 01-13, and both are the mathematical
content of conservation laws you will meet in fluids, heat transfer, and
electromagnetics.

**Where are the extremes?** Optimization with several variables, including the case
where a **constraint** ties the variables together. That last case — Lagrange
multipliers — is how you minimize material for a fixed volume, or cost for a fixed
capacity.

A note on exam weight. Partial derivatives and the total differential are used
constantly, often without announcement. The gradient, divergence, and curl are
tested at the level of *computing them correctly from a formula in the Handbook*,
and understanding what they mean physically. Lagrange multipliers appear
occasionally. Drill the first two groups.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 23.1 Interpret a function of two variables as a surface and sketch or read its
  level curves
* 23.2 Compute first partial derivatives and state what each one measures
* 23.3 Compute higher-order and mixed partial derivatives, and apply the equality
  of mixed partials
* 23.4 Write the total differential of a function of several variables
* 23.5 Propagate measurement uncertainty through a formula using the total
  differential, and identify which input dominates
* 23.6 Apply the power-law shortcut for uncertainty in a product of powers
* 23.7 Write the equation of a tangent plane and recognize it as the first-order
  multivariable Taylor polynomial
* 23.8 Apply the multivariable chain rule to a related-rates problem
* 23.9 Compute the gradient and state its two defining properties
* 23.10 Compute a directional derivative and relate it to the gradient magnitude
* 23.11 Compute the divergence of a vector field and interpret it as source
  strength
* 23.12 Compute the curl of a vector field and interpret it as local rotation
* 23.13 Locate and classify critical points of a function of two variables using
  the second-derivative test
* 23.14 Solve a constrained optimization problem by the method of Lagrange
  multipliers

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $f(x,y)$, $f(x,y,z)$ | scalar function of several variables | output is a number |
| $\dfrac{\partial f}{\partial x}$, $f_x$ | partial derivative with respect to $x$ | other variables held constant |
| $f_{xx}$, $f_{yy}$ | second partials in the same variable | — |
| $f_{xy}$, $f_{yx}$ | **mixed** second partials | equal for well-behaved $f$ |
| $\partial$ | "partial" — the curly $d$ | signals that other variables are frozen |
| $df$ | total differential of $f$ | sum of all partial contributions |
| $\nabla$ | del operator, $\left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z}\right)$ | pronounced "del" or "nabla" |
| $\nabla f$ | **gradient** of a scalar field | a **vector** |
| $\mathbf{F}$ | vector field, $\mathbf{F} = F_x\hat{\imath} + F_y\hat{\jmath} + F_z\hat{k}$ | — |
| $\nabla\cdot\mathbf{F}$ | **divergence** of a vector field | a **scalar** |
| $\nabla\times\mathbf{F}$ | **curl** of a vector field | a **vector** |
| $D_{\mathbf{u}}f$ | directional derivative of $f$ in direction $\mathbf{u}$ | $\mathbf{u}$ must be a **unit** vector |
| $D$ | discriminant $f_{xx}f_{yy} - f_{xy}^2$ | second-derivative test |
| $\lambda$ | Lagrange multiplier | — |
| $g(x,y) = k$ | constraint equation | — |

> ---
> **Mentor's Margin**
>
> Two notation points that matter more than they look.
>
> **The curly $\partial$ is not decoration.** Writing $\frac{df}{dx}$ when you
> mean $\frac{\partial f}{\partial x}$ is a real error, because the two say
> different things. $\frac{\partial f}{\partial x}$ means "the rate of change of
> $f$ as $x$ varies **and $y$ is held fixed**." $\frac{df}{dx}$ means the total
> rate including whatever $y$ does in response. When $y$ depends on $x$ — which it
> often does in a physical system — those two numbers are different. The symbol
> tells the reader which one you computed.
>
> **Keep the output types straight.** The three vector operators do not all
> produce the same kind of object, and confusing them produces answers that are
> not merely wrong but ungrammatical.
>
> | Operator | Input | Output |
> |---|---|---|
> | gradient $\nabla f$ | scalar field | **vector** |
> | divergence $\nabla\cdot\mathbf{F}$ | vector field | **scalar** |
> | curl $\nabla\times\mathbf{F}$ | vector field | **vector** |
>
> The dot and cross in the notation are your reminders, and they are honest ones:
> Chapter 01-13 established that a dot product returns a scalar and a cross product
> returns a vector. Same rule here. If you report the divergence as a vector, you
> have made a type error and the check is immediate.
>
> ---

---

## 23.1 Functions of Several Variables

A function of two variables assigns a number to each point in a plane. Its graph
is a **surface** in three dimensions: $z = f(x,y)$.

For $f(x,y) = x^2 + y^2$ the surface is a bowl — a paraboloid opening upward, with
its lowest point at the origin.

Surfaces are hard to draw and harder to read. The practical alternative is a
**level curve** (or contour): the set of points where $f$ takes one fixed value.
Setting $x^2+y^2 = c$ gives circles of radius $\sqrt{c}$, so the bowl's contour map
is a set of concentric circles.

You have read contour maps before, under other names. A topographic map shows level
curves of elevation. A weather chart shows isobars — level curves of pressure. A
thermal plot shows isotherms. In every case the spacing carries the information:
**closely spaced contours mean the function is changing fast**, which is exactly
the fact the gradient will make precise in §23.5.

![FIG-01-23-001: Two-panel figure. Left panel shows the surface z = x² + y² drawn in three dimensions as a bowl-shaped paraboloid, with four horizontal cutting planes at z = 1, 4, 9, and 16 slicing through it and the intersection circles traced on each plane. Right panel shows the same information as a flat contour map: four concentric circles labeled with their z-values 1, 4, 9, 16, with radii 1, 2, 3, 4. An annotation notes "contours bunch together where the surface is steep" with an arrow pointing to the closer-spaced outer rings.](../figures/FIG-01-23-001-surface-and-contours.png)

---

## 23.2 Partial Derivatives

Here is the whole idea, and it genuinely is this simple.

To find $\dfrac{\partial f}{\partial x}$: treat $y$ as a **constant** and
differentiate with respect to $x$ using every rule from Chapter 01-17.

To find $\dfrac{\partial f}{\partial y}$: treat $x$ as a constant and differentiate
with respect to $y$.

No new techniques. The product rule, quotient rule, chain rule, and every entry in
the derivative table apply unchanged. The only discipline required is remembering
which letter is frozen.

### What a partial derivative measures

Geometrically, $f_x$ at a point is the slope of the surface in the
$x$-direction — the slope of the curve you get by slicing the surface with a
vertical plane holding $y$ constant. Similarly $f_y$ is the slope along a slice
holding $x$ constant.

Physically, $f_x$ is the **sensitivity** of the output to that one input. If
$\frac{\partial Q}{\partial D} = 0.57$ m²/s, then a one-millimetre change in
diameter changes the flow by $0.57 \times 0.001$ m³/s, with everything else held
where it was. That sensitivity reading is what makes partial derivatives an
engineering tool rather than a formality.

![FIG-01-23-002: A surface z = f(x,y) drawn in three dimensions with a point P marked on it. Two vertical cutting planes pass through P: one holding y constant, producing a trace curve on the surface with a tangent line drawn along it labeled "slope = ∂f/∂x"; the other holding x constant, producing a second trace curve with a tangent line labeled "slope = ∂f/∂y". The two tangent lines are shown meeting at P, and a dashed parallelogram through them indicates the tangent plane they span.](../figures/FIG-01-23-002-partial-derivative-slices.png)

### Worked Example 1 — First Partials

**Given.** $f(x,y) = x^2 y + 3xy^3 - 2y$

**Find.** $f_x$ and $f_y$, and evaluate both at $(2, 1)$.

**Solution.**

**For $f_x$**, treat $y$ as a constant. Then $x^2y$ differentiates to $2xy$ (the
$y$ rides along as a coefficient), $3xy^3$ differentiates to $3y^3$, and $-2y$ is a
constant so it vanishes:

$$f_x = 2xy + 3y^3$$

**For $f_y$**, treat $x$ as a constant. Now $x^2y$ differentiates to $x^2$, $3xy^3$
differentiates to $9xy^2$, and $-2y$ differentiates to $-2$:

$$f_y = x^2 + 9xy^2 - 2$$

**At $(2,1)$:**

$$f_x = 2(2)(1) + 3(1)^3 = 4 + 3 = \boxed{7}$$
$$f_y = (2)^2 + 9(2)(1)^2 - 2 = 4 + 18 - 2 = \boxed{20}$$

**Interpretation.** At the point $(2,1)$ the surface is nearly three times steeper
in the $y$-direction than in the $x$-direction. Moving one unit in $y$ changes $f$
by roughly 20; moving one unit in $x$ changes it by roughly 7.

### Worked Example 2 — Product and Chain Rules Still Apply

**Given.** $f(x,y) = x^3y^2 + e^{xy}$

**Find.** $f_x$ and $f_y$.

**Solution.**

**$f_x$**, with $y$ frozen. The second term needs the chain rule: the inner
function is $xy$, whose derivative with respect to $x$ is $y$:

$$f_x = 3x^2y^2 + y\,e^{xy}$$

**$f_y$**, with $x$ frozen. Now the inner derivative is $x$:

$$f_y = 2x^3y + x\,e^{xy}$$

Note how the frozen variable appears as the chain factor. That is the most common
place to slip: differentiating $e^{xy}$ with respect to $x$ gives $y e^{xy}$, not
$e^{xy}$ and not $xe^{xy}$.

### Higher-order and mixed partials

Differentiate twice. There are four second partials for a function of two
variables:

$$f_{xx} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) \qquad f_{yy} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right)$$

$$f_{xy} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) \qquad f_{yx} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)$$

The last two are the **mixed partials**, and there is a theorem about them:

> **Equality of mixed partials.** If the second partials are continuous, then
> $$\boxed{f_{xy} = f_{yx}}$$

The order of differentiation does not matter. This is not obvious — there is no
reason on inspection why differentiating in $x$ then $y$ should agree with $y$ then
$x$ — and it is enormously convenient. It also gives you a free check: compute both
and confirm they agree.

### Worked Example 3 — Mixed Partials Agree

**Given.** $f(x,y) = x^3y^2 + e^{xy}$, continuing Worked Example 2.

**Verify** that $f_{xy} = f_{yx}$.

**Solution.**

From Worked Example 2, $f_x = 3x^2y^2 + ye^{xy}$. Differentiate with respect to
$y$, using the product rule on the second term:

$$f_{xy} = 6x^2y + \left[e^{xy} + y\cdot xe^{xy}\right] = 6x^2y + e^{xy}(1 + xy)$$

And $f_y = 2x^3y + xe^{xy}$. Differentiate with respect to $x$:

$$f_{yx} = 6x^2y + \left[e^{xy} + x\cdot ye^{xy}\right] = 6x^2y + e^{xy}(1 + xy)$$

$$\boxed{f_{xy} = f_{yx} \;\checkmark}$$

Identical, as the theorem promised. When they do **not** agree, you have made an
algebra error — the theorem holds for essentially every function you will meet in
engineering.

---

## 23.3 The Total Differential and Error Propagation

This is the section that earns the chapter.

### The total differential

Chapter 01-18 gave the single-variable differential $dy = f'(x)\,dx$: a small input
change times the sensitivity gives the output change. With several inputs, each
contributes its own term:

$$\boxed{df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz + \cdots}$$

Read it as an accounting statement. Each input's change is multiplied by that
input's sensitivity, and the contributions add.

### Tangent plane and the first-order Taylor polynomial

Truncating there gives the **tangent plane** at $(a,b)$:

$$\boxed{z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)}$$

Compare with the degree-1 Taylor polynomial from Chapter 01-22:
$P_1(x) = f(a) + f'(a)(x-a)$. Same structure, one term per variable. The tangent
plane **is** the first-order multivariable Taylor expansion, and "linearize about
the operating point" means exactly this in a multi-input system. Everything
Chapter 01-22 said about truncation error applies: the approximation is local, and
its error grows as the square of the departure from $(a,b)$.

![FIG-01-23-003: A curved surface z = f(x,y) with a point P marked on it, and a flat tangent plane drawn touching the surface at P and extending outward. Near P the plane and surface are drawn nearly coincident; toward the edges of the plane a vertical gap opens between the plane and the surface, bracketed and labeled "error grows with distance from P — second order". Two arrows along the plane from P are labeled dx and dy, and a vertical arrow shows the resulting df built from f_x·dx plus f_y·dy.](../figures/FIG-01-23-003-tangent-plane.png)

### Error propagation

Now interpret $dx$, $dy$ as **measurement uncertainties** rather than deliberate
changes. Taking absolute values so that errors accumulate rather than cancel gives
the worst-case bound:

$$\boxed{\lvert df\rvert \le \left\lvert\frac{\partial f}{\partial x}\right\rvert\lvert dx\rvert + \left\lvert\frac{\partial f}{\partial y}\right\rvert\lvert dy\rvert + \cdots}$$

Each term tells you how much of the output uncertainty came from each input, which
is the genuinely useful part: it tells you which instrument to upgrade.

### The power-law shortcut

For a function that is a **product of powers**,

$$f = C\,x^{a}y^{b}z^{c}$$

the relative uncertainties combine with the exponents as weights:

$$\boxed{\frac{\lvert df\rvert}{f} \le \lvert a\rvert\frac{\lvert dx\rvert}{x} + \lvert b\rvert\frac{\lvert dy\rvert}{y} + \lvert c\rvert\frac{\lvert dz\rvert}{z}}$$

This is the multivariable version of the rule from Chapter 01-18, and Chapter 01-22
showed where it comes from — the first-order binomial expansion of
$(1+\varepsilon)^a$. It saves a great deal of work, and it makes the structure
obvious: **an exponent of 2 doubles that input's contribution**, an exponent of
$\frac{1}{2}$ halves it, and a negative exponent contributes just as much as a
positive one of the same size.

### Worked Example 4 — Volume of a Cylinder

**Given.** A cylinder measured as $r = 25.0 \pm 0.3$ mm and $h = 80.0 \pm 0.5$ mm.

**Find.** The volume and its uncertainty, by the total differential and by the
power-law shortcut. Identify which measurement dominates.

**Solution.**

$$V = \pi r^2 h = \pi(25.0)^2(80.0) = \pi(625)(80.0) = \pi(50{,}000) = 157{,}080 \text{ mm}^3$$

**By the total differential.**

$$\frac{\partial V}{\partial r} = 2\pi rh = 2\pi(25.0)(80.0) = 4000\pi = 12{,}566 \text{ mm}^2$$
$$\frac{\partial V}{\partial h} = \pi r^2 = 625\pi = 1963.5 \text{ mm}^2$$

$$\lvert dV\rvert \le 12{,}566(0.3) + 1963.5(0.5) = 3769.9 + 981.7 = 4751.7 \text{ mm}^3$$

$$\boxed{V = 157{,}100 \pm 4800 \text{ mm}^3}$$

**Relative uncertainty.**

$$\frac{4751.7}{157{,}080} = 0.03025 = 3.03\%$$

**By the power-law shortcut.** $V = \pi r^2 h$ has exponents 2 on $r$ and 1 on $h$:

$$\frac{dV}{V} \le 2\left(\frac{0.3}{25.0}\right) + 1\left(\frac{0.5}{80.0}\right) = 2(0.01200) + 0.00625$$

$$= 0.02400 + 0.00625 = 0.03025 = 3.03\% \;\checkmark$$

Identical, in a fraction of the work.

**Which measurement dominates?**

| Input | Relative uncertainty | Weighted contribution | Share of total |
|---|---|---|---|
| $r$ | $1.20\%$ | $2.40\%$ | $79.3\%$ |
| $h$ | $0.63\%$ | $0.63\%$ | $20.7\%$ |

**Interpretation, and this is the engineering content.** The radius is measured
*better* than the height in relative terms — 1.2% against 0.63%... no, read it
again: the radius is measured *worse*, 1.20% against 0.63%. And the squared
dependence then doubles its weight, so the radius accounts for nearly 80% of the
output uncertainty.

The design conclusion follows immediately: **improving the height measurement is
nearly pointless.** Even a perfect height measurement leaves 2.40% uncertainty in
the volume. Halving the radius uncertainty, by contrast, cuts the total to 1.83%.
That kind of ranking is why error propagation is done at all — not to decorate a
result with an error bar, but to decide where to spend money.

### Worked Example 5 — Flow Rate from Diameter and Velocity

**Given.** Flow in a circular pipe, $Q = \frac{\pi D^2}{4}v$, with
$D = 150 \pm 1$ mm and $v = 2.40 \pm 0.05$ m/s.

**Find.** $Q$ and its uncertainty, and the contribution of each input.

**Solution.**

$$Q = \frac{\pi(0.150)^2}{4}(2.40) = \frac{\pi(0.0225)}{4}(2.40) = \frac{\pi(0.0540)}{4} = 0.042412 \text{ m}^3/\text{s}$$

$$Q = 42.4 \text{ L/s}$$

**Power-law shortcut**, exponents 2 on $D$ and 1 on $v$:

$$\frac{dQ}{Q} \le 2\left(\frac{1}{150}\right) + \frac{0.05}{2.40} = 2(0.006667) + 0.020833$$

$$= 0.013333 + 0.020833 = 0.034167 = 3.42\%$$

$$dQ = 0.034167(42.4) = 1.45 \text{ L/s}$$

$$\boxed{Q = 42.4 \pm 1.4 \text{ L/s}}$$

| Input | Relative uncertainty | Weighted | Share |
|---|---|---|---|
| $D$ | $0.67\%$ | $1.33\%$ | $39.0\%$ |
| $v$ | $2.08\%$ | $2.08\%$ | $61.0\%$ |

**Interpretation.** Here the ranking reverses from Worked Example 4. The diameter
is measured far more precisely — 0.67% against 2.08% — and even after the squaring
doubles its weight, the velocity still dominates. Buy a better flowmeter, not a
better calliper.

That the two examples come out opposite ways is the point. **You cannot rank the
inputs by inspection.** The exponent matters and the measurement quality matters,
and only computing both tells you which wins.

> ---
> **Mentor's Margin**
>
> Two things about this section that will serve you beyond the exam.
>
> **First, the total differential gives you the worst case.** Taking absolute
> values assumes every error happens to push the same way, which is conservative
> and sometimes needlessly so. Independent random errors partially cancel, and the
> statistically correct combination is the root-sum-square:
>
> $$\frac{dQ}{Q} \approx \sqrt{(1.333\%)^2 + (2.083\%)^2} = \sqrt{1.777 + 4.339} = 2.47\%$$
>
> against the 3.42% worst case. Which to report depends on whether the
> uncertainties are independent random errors or possible systematic biases.
> Chapter 01-40 develops the statistical version properly; the differential method
> here is the one to use when you need a bound you can defend without assuming
> anything about the error distributions. **Nothing in this chapter depends on that
> later material** — I mention it so you know the 3.42% is a ceiling, not an
> estimate.
>
> **Second, this is the most portable thing in Tier 1C.** Every discipline exam
> has problems where a quantity is computed from several measured inputs, and the
> power-law rule handles a large fraction of them in one line. Memorize it. It is
> not in the Handbook in the form you need it.
>
> ---

---

## 23.4 The Multivariable Chain Rule

When the inputs themselves depend on a further variable — usually time — the
total rate of change collects all the paths:

$$\boxed{\frac{df}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} + \cdots}$$

This is the total differential divided through by $dt$, and it is the multivariable
generalization of the related-rates method from Chapter 01-18. Note the notation
discipline: the left side is an ordinary $d$, because $f$ now depends on the single
variable $t$; the partials on the right stay curly.

### Worked Example 6 — Competing Rates

**Given.** A resistor dissipates $P = \frac{V^2}{R}$. At a given instant
$V = 12.0$ V and is rising at $0.15$ V/s, while $R = 48.0\ \Omega$ and is rising at
$0.60\ \Omega$/s as the resistor heats.

**Find.** $\frac{dP}{dt}$ and interpret it.

**Solution.**

**Partials.**

$$\frac{\partial P}{\partial V} = \frac{2V}{R} = \frac{2(12.0)}{48.0} = 0.500 \text{ W/V}$$

$$\frac{\partial P}{\partial R} = -\frac{V^2}{R^2} = -\frac{144}{2304} = -0.0625 \text{ W}/\Omega$$

**Chain rule.**

$$\frac{dP}{dt} = 0.500(0.15) + (-0.0625)(0.60) = 0.0750 - 0.0375$$

$$= \boxed{+0.0375 \text{ W/s}}$$

**Interpretation.** Two effects oppose each other. Rising voltage pushes power up
at $0.075$ W/s; rising resistance pulls it down at $0.0375$ W/s. The voltage wins
by a factor of two, so power is rising — but at half the rate the voltage change
alone would suggest.

The current power is $P = \frac{144}{48} = 3.00$ W, so the power is climbing at
$1.25\%$ per second. Note that the negative sign on
$\frac{\partial P}{\partial R}$ was essential; dropping it would have given
$0.1125$ W/s, three times too large and in a way that no units check would catch.

---

## 23.5 The Gradient and Directional Derivatives

### The gradient

Collect the partials of a scalar field into a vector:

$$\boxed{\nabla f = \frac{\partial f}{\partial x}\hat{\imath} + \frac{\partial f}{\partial y}\hat{\jmath} + \frac{\partial f}{\partial z}\hat{k}}$$

The gradient has two properties, and together they are why it matters:

**1. It points in the direction of steepest increase.** Of all the directions you
could move from a point, $\nabla f$ is the one along which $f$ grows fastest.

**2. Its magnitude is that maximum rate.** $\lvert\nabla f\rvert$ is the slope in
the steepest direction. No direction gives a larger rate of change.

A consequence worth stating separately: **the gradient is perpendicular to the
level curves**. Moving along a contour, $f$ does not change at all, so the
direction of maximum change must be at right angles to it. That is why a contour
map lets you read gradients by eye — steepest descent runs perpendicular to the
contour lines, and the closer the contours, the larger $\lvert\nabla f\rvert$.

![FIG-01-23-004: A contour map of a scalar field with five nested irregular closed contours labeled with increasing values, tightly spaced on the left side and widely spaced on the right. At six points around the map, gradient vectors are drawn as arrows, each perpendicular to the local contour and pointing toward the higher-valued contour. The arrows on the tightly spaced left side are drawn long and labeled "large |∇f| — steep"; those on the widely spaced right side are drawn short and labeled "small |∇f| — gentle". A note reads "gradient ⊥ contours, pointing uphill".](../figures/FIG-01-23-004-gradient-contours.png)

### Why engineers care

Nearly every transport law in engineering says that something flows **down a
gradient**, at a rate proportional to the gradient's magnitude:

| Law | Statement | Field |
|---|---|---|
| Fourier's law | $\mathbf{q} = -k\nabla T$ | heat flux down a temperature gradient |
| Fick's law | $\mathbf{J} = -D\nabla C$ | mass flux down a concentration gradient |
| Darcy's law | $\mathbf{v} = -K\nabla h$ | groundwater flow down a head gradient |
| Ohm's law (field form) | $\mathbf{E} = -\nabla V$ | electric field down a potential gradient |

The minus sign in each is the physics: things flow from high to low, while the
gradient points from low to high. Memorize the pattern and four laws become one.

### Directional derivatives

To find the rate of change in an arbitrary direction, project the gradient onto
that direction using the dot product from Chapter 01-13:

$$\boxed{D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u} \qquad \text{where } \lvert\mathbf{u}\rvert = 1}$$

The unit requirement is not optional. If $\mathbf{u}$ is not normalized, the answer
is scaled by $\lvert\mathbf{u}\rvert$ and is simply wrong.

Since $\nabla f\cdot\mathbf{u} = \lvert\nabla f\rvert\cos\theta$, the directional
derivative ranges from $+\lvert\nabla f\rvert$ (straight uphill) through zero
(along a contour) to $-\lvert\nabla f\rvert$ (straight downhill). That gives you a
free check: **any directional derivative must have magnitude no greater than
$\lvert\nabla f\rvert$.**

### Worked Example 7 — Gradient and Directional Derivative

**Given.** $f(x,y) = x^2 + 3xy - y^2$ at the point $(1, 2)$.

**Find.** (a) $\nabla f$, (b) the maximum rate of increase and its direction,
(c) the rate of change toward the point $(4, 6)$.

**Solution.**

**(a)**

$$f_x = 2x + 3y \implies f_x(1,2) = 2 + 6 = 8$$
$$f_y = 3x - 2y \implies f_y(1,2) = 3 - 4 = -1$$

$$\boxed{\nabla f = 8\hat{\imath} - \hat{\jmath}}$$

**(b)**

$$\lvert\nabla f\rvert = \sqrt{64 + 1} = \sqrt{65} = \boxed{8.06}$$

Direction, as a unit vector:

$$\hat{\mathbf{u}}_{\max} = \frac{8\hat{\imath} - \hat{\jmath}}{8.062} = \boxed{0.992\hat{\imath} - 0.124\hat{\jmath}}$$

Almost due $+x$, tilted slightly toward $-y$.

**(c)** The direction from $(1,2)$ to $(4,6)$ is $\langle 3, 4\rangle$, with
magnitude $\sqrt{9+16} = 5$. Normalize:

$$\mathbf{u} = \left\langle 0.600,\; 0.800\right\rangle$$

$$D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u} = 8(0.600) + (-1)(0.800) = 4.80 - 0.80 = \boxed{4.00}$$

**Check.** $4.00 \le 8.06$ ✓ The directional derivative cannot exceed the gradient
magnitude, and it does not.

**Interpretation.** Moving toward $(4,6)$ gains height at rate 4.00 per unit
distance — about half the best available rate of 8.06, because that direction is
roughly $60°$ off the steepest line. Confirm:
$\cos^{-1}(4.00/8.06) = \cos^{-1}(0.496) = 60.3°$ ✓

---

## 23.6 Divergence and Curl

Now the operators that act on **vector** fields. Write

$$\mathbf{F} = F_x\hat{\imath} + F_y\hat{\jmath} + F_z\hat{k}$$

### Divergence — a scalar

$$\boxed{\nabla\cdot\mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}}$$

Divergence measures **net outflow per unit volume** at a point. Picture a tiny box
around the point and ask whether more field lines leave than enter.

| Divergence | Meaning |
|---|---|
| $\nabla\cdot\mathbf{F} > 0$ | **source** — field spreading out from the point |
| $\nabla\cdot\mathbf{F} < 0$ | **sink** — field converging on the point |
| $\nabla\cdot\mathbf{F} = 0$ | **solenoidal** — whatever enters, leaves |

The zero case is the important one in practice. For a fluid, $\nabla\cdot\mathbf{v}
= 0$ is the **continuity equation for incompressible flow** — mass cannot
accumulate anywhere. For a magnetic field, $\nabla\cdot\mathbf{B} = 0$ is the
statement that magnetic monopoles do not exist.

### Curl — a vector

$$\boxed{\nabla\times\mathbf{F} = \begin{vmatrix}\hat{\imath} & \hat{\jmath} & \hat{k}\\[1mm] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z}\\[2mm] F_x & F_y & F_z\end{vmatrix}}$$

Expanded, using the determinant machinery from Chapter 01-14 and the cross-product
structure from Chapter 01-13:

$$\nabla\times\mathbf{F} = \left(\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}\right)\hat{\imath} + \left(\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}\right)\hat{\jmath} + \left(\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\right)\hat{k}$$

Curl measures **local rotation**. Drop a tiny paddle wheel into the field: if it
spins, the curl is nonzero, and the curl vector points along the spin axis by the
right-hand rule.

A field with $\nabla\times\mathbf{F} = \mathbf{0}$ is **irrotational**, and that
condition has a consequence worth knowing: an irrotational field is
**conservative**, meaning it can be written as the gradient of a scalar potential.
That is why electrostatic fields have voltages and gravitational fields have
potential energies.

![FIG-01-23-005: Two-panel figure of field-line sketches with small test objects. Left panel titled "Divergence": three sub-sketches — arrows radiating outward from a point labeled "∇·F > 0, source", arrows converging inward labeled "∇·F < 0, sink", and uniform parallel arrows through a small dashed box with equal numbers entering and leaving labeled "∇·F = 0, solenoidal". Right panel titled "Curl": two sub-sketches — a shear field with arrows of increasing length, a small paddle wheel drawn in it shown rotating with a curved arrow and the curl vector drawn out of the page labeled "∇×F ≠ 0"; and a uniform field with an identical paddle wheel drawn stationary labeled "∇×F = 0, irrotational".](../figures/FIG-01-23-005-divergence-curl.png)

### Worked Example 8 — Computing Both

**Given.** $\mathbf{F} = 3x^2y\,\hat{\imath} - 2yz\,\hat{\jmath} + xz^2\,\hat{k}$

**Find.** $\nabla\cdot\mathbf{F}$ and $\nabla\times\mathbf{F}$, both evaluated at
$(1, 2, 1)$.

**Solution.**

**Divergence.** Take each component's partial with respect to its own variable:

$$\frac{\partial}{\partial x}\left(3x^2y\right) = 6xy \qquad \frac{\partial}{\partial y}(-2yz) = -2z \qquad \frac{\partial}{\partial z}\left(xz^2\right) = 2xz$$

$$\nabla\cdot\mathbf{F} = 6xy - 2z + 2xz$$

At $(1,2,1)$: $6(1)(2) - 2(1) + 2(1)(1) = 12 - 2 + 2 = \boxed{12}$

Positive, so the point is a net source.

**Curl.** Work the three components in order.

$\hat{\imath}$: $\dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z}
= 0 - (-2y) = 2y$

$\hat{\jmath}$: $\dfrac{\partial F_x}{\partial z} - \dfrac{\partial F_z}{\partial x}
= 0 - z^2 = -z^2$

$\hat{k}$: $\dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y}
= 0 - 3x^2 = -3x^2$

$$\nabla\times\mathbf{F} = 2y\,\hat{\imath} - z^2\,\hat{\jmath} - 3x^2\,\hat{k}$$

At $(1,2,1)$:

$$\boxed{\nabla\times\mathbf{F} = 4\hat{\imath} - \hat{\jmath} - 3\hat{k}}$$

**Type check.** Divergence came out a single number ✓ Curl came out a vector with
three components ✓ If either had the wrong type, the computation went wrong.

> ---
> **Mentor's Margin**
>
> The curl determinant is where errors live, and there are two of them.
>
> **The middle sign.** Expanding a $3\times3$ determinant along the top row carries
> the alternating pattern $+,-,+$ from Chapter 01-14. So the $\hat{\jmath}$
> component picks up a minus sign, which is why it reads
> $\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}$ — the
> reverse order from what the pattern of the other two components suggests. Write
> the determinant out rather than trying to recall the expanded form, and the sign
> takes care of itself.
>
> **Which partial pairs with which component.** Every term in the curl mixes
> *different* subscripts and variables: $\frac{\partial F_z}{\partial y}$, never
> $\frac{\partial F_z}{\partial z}$. The divergence is the opposite — it uses only
> matching pairs. If you find a matching pair inside a curl, or a mismatched pair
> inside a divergence, you have crossed the two operators.
>
> The Handbook prints both formulas, including the determinant form of the curl.
> Look them up. This is a case where the lookup is fast and the recall is error
> prone, which is exactly when you should use the reference.
>
> ---

---

## 23.7 Optimization with Several Variables

### Critical points

At a local maximum or minimum of a smooth function, the surface is level in
**every** direction, so every partial vanishes:

$$\boxed{f_x = 0 \quad\text{and}\quad f_y = 0}$$

Equivalently $\nabla f = \mathbf{0}$ — there is no uphill direction. Solve that
system for the critical points.

As in Chapter 01-18, a critical point need not be an extremum. But now there is a
new possibility that has no single-variable analogue: a **saddle point**, where the
surface rises in one direction and falls in another. A mountain pass is a saddle —
the lowest point along the ridge and the highest point along the trail.

### The second-derivative test

Form the discriminant

$$\boxed{D = f_{xx}f_{yy} - \left(f_{xy}\right)^2}$$

evaluated at the critical point. Then:

| Condition | Conclusion |
|---|---|
| $D > 0$ and $f_{xx} > 0$ | local **minimum** |
| $D > 0$ and $f_{xx} < 0$ | local **maximum** |
| $D < 0$ | **saddle point** |
| $D = 0$ | test fails — investigate directly |

Note the structure. $D > 0$ says the surface curves the same way in both
directions, and then $f_{xx}$ decides which way — the same role the second
derivative played in Chapter 01-18. $D < 0$ says the curvatures disagree, which is
a saddle.

![FIG-01-23-006: Three three-dimensional surface sketches side by side, each with the critical point marked. Left, labeled "D > 0, f_xx > 0 — local minimum": a bowl opening upward with the point at the bottom, and two cross-section curves drawn through the point both curving upward. Centre, labeled "D > 0, f_xx < 0 — local maximum": a dome with the point at the top and both cross-sections curving downward. Right, labeled "D < 0 — saddle point": a saddle shape with one cross-section curving upward and the perpendicular one curving downward, annotated "curvatures disagree".](../figures/FIG-01-23-006-critical-point-classification.png)

### Worked Example 9 — Locating and Classifying

**Given.** $f(x,y) = x^3 + y^3 - 3xy$

**Find.** All critical points and classify each.

**Solution.**

**Critical points.**

$$f_x = 3x^2 - 3y = 0 \implies y = x^2$$
$$f_y = 3y^2 - 3x = 0 \implies x = y^2$$

Substitute the first into the second:

$$x = \left(x^2\right)^2 = x^4 \implies x^4 - x = 0 \implies x\left(x^3 - 1\right) = 0$$

So $x = 0$ or $x = 1$, giving $y = 0$ and $y = 1$ respectively.

$$\text{critical points: } (0,0) \text{ and } (1,1)$$

**Second partials.**

$$f_{xx} = 6x \qquad f_{yy} = 6y \qquad f_{xy} = -3$$

$$D = (6x)(6y) - (-3)^2 = 36xy - 9$$

**Classify.**

At $(0,0)$: $D = 0 - 9 = -9 < 0 \implies \boxed{\text{saddle point}}$

At $(1,1)$: $D = 36 - 9 = 27 > 0$ and $f_{xx} = 6 > 0 \implies
\boxed{\text{local minimum}}$, with

$$f(1,1) = 1 + 1 - 3 = -1$$

**Check the saddle directly.** Along the line $y = x$ near the origin,
$f = 2x^3 - 3x^2$, which for small $x$ is dominated by $-3x^2 < 0$ — the function
decreases. Along the line $y = -x$, $f = x^3 - x^3 + 3x^2 = 3x^2 > 0$ — the
function increases. Down one way, up the other ✓ A saddle.

### Constrained optimization: Lagrange multipliers

Often the variables are tied together. Minimize material for a **fixed** volume;
maximize capacity for a **fixed** cost. The constraint means you cannot simply set
all the partials to zero, because the unconstrained optimum is not reachable.

The method: to optimize $f(x,y)$ subject to $g(x,y) = k$, solve

$$\boxed{\nabla f = \lambda\nabla g \qquad \text{together with} \qquad g(x,y) = k}$$

The geometric reason is worth carrying, because it makes the method memorable
rather than arbitrary. At the constrained optimum, the level curve of $f$ is
**tangent** to the constraint curve. If they crossed instead, you could slide along
the constraint to a better level curve. Tangent curves have parallel normals, and
the gradients are the normals — hence $\nabla f = \lambda\nabla g$.

The multiplier $\lambda$ is usually a means to an end, not the answer. Solve for
the variables and discard it.

![FIG-01-23-007: A contour map showing several level curves of an objective function f as nested closed curves labeled with increasing values, overlaid with a single heavier constraint curve g = k winding across them. At one point the constraint curve is tangent to a level curve; at that point two arrows are drawn — ∇f and ∇g — shown parallel, and the point is labeled "constrained optimum, ∇f = λ∇g". At a second point where the constraint curve visibly crosses a level curve, the two gradient arrows are drawn non-parallel and an arrow along the constraint is labeled "can still improve — slide this way".](../figures/FIG-01-23-007-lagrange-tangency.png)

### Worked Example 10 — Minimum-Material Tank

**Given.** A closed cylindrical tank must hold $2.00$ m³.

**Find.** The radius and height that minimize surface area, and the resulting area.

**Solution.**

**Objective and constraint.**

$$A = 2\pi r^2 + 2\pi rh \qquad \text{subject to} \qquad V = \pi r^2 h = 2.00$$

**Gradients.**

$$\nabla A = \left\langle 4\pi r + 2\pi h,\; 2\pi r\right\rangle \qquad \nabla V = \left\langle 2\pi rh,\; \pi r^2\right\rangle$$

**Set $\nabla A = \lambda\nabla V$.**

$$4\pi r + 2\pi h = \lambda(2\pi rh) \tag{1}$$
$$2\pi r = \lambda\left(\pi r^2\right) \tag{2}$$

From (2), cancelling $\pi r$ (valid since $r > 0$):

$$2 = \lambda r \implies \lambda = \frac{2}{r}$$

Substitute into (1):

$$4\pi r + 2\pi h = \frac{2}{r}(2\pi rh) = 4\pi h$$

$$4\pi r = 2\pi h \implies \boxed{h = 2r}$$

**The height equals the diameter.** That is the classic result, and it is worth
remembering: the most material-efficient closed cylinder is as tall as it is wide.

**Apply the constraint.**

$$\pi r^2(2r) = 2\pi r^3 = 2.00 \implies r^3 = \frac{1}{\pi} = 0.31831$$

$$r = 0.68278 \text{ m} \qquad h = 1.36556 \text{ m}$$

$$\boxed{r = 0.683 \text{ m}, \quad h = 1.366 \text{ m}}$$

**Surface area.**

$$A = 2\pi(0.68278)^2 + 2\pi(0.68278)(1.36556) = 2\pi(0.46619) + 2\pi(0.93238)$$

$$= 2.9293 + 5.8585 = \boxed{8.79 \text{ m}^2}$$

**Check the constraint.** $\pi(0.46619)(1.36556) = \pi(0.63650) = 2.000$ m³ ✓

**Check against the theoretical floor.** Of all shapes enclosing a given volume,
the sphere has the least surface area. For $V = 2.00$ m³:

$$\frac{4}{3}\pi r^3 = 2.00 \implies r^3 = 0.47746 \implies r = 0.78159 \text{ m}$$

$$A_{\text{sphere}} = 4\pi r^2 = 4\pi(0.61088) = 7.68 \text{ m}^2$$

Our cylinder needs $8.79$ m², which exceeds the sphere's $7.68$ m² by 14.5% ✓ The
answer must be above the spherical floor, and it is — by a plausible margin. A
cylinder coming out *below* the sphere would have been proof of an error.

---

## As the Handbook States It

> **Handbook 10.6, Mathematics section (begins p. 36)** — partial differentiation
> and the vector operators appear in two places. The *Differential Calculus*
> subsection, around pp. 43–45, carries partial derivatives, the total
> differential, and the gradient. The *Vectors* subsection, near the analytic
> geometry material, carries divergence and curl alongside the dot and cross
> products from Chapter 01-13.

Coverage here is **good for the formulas and absent for the judgement**, which is
the usual pattern.

**What's in the Handbook — find it fast:**

- **Partial derivative notation** and the definition
- **The total differential**, stated in the general form
- **The gradient**, with the $\nabla$ operator defined
- **Divergence and curl**, including the determinant form of the curl. This is the
  single most worthwhile lookup in the chapter — the curl expansion is error prone
  from memory and printed correctly in the reference.
- Some vector identities, such as $\nabla\times\nabla f = \mathbf{0}$ and
  $\nabla\cdot(\nabla\times\mathbf{F}) = 0$
- The Laplacian $\nabla^2 f$
- Tests for a maximum, minimum, and saddle point of a function of two variables,
  usually including the discriminant

**What's not in the Handbook — memorize:**

- **The power-law uncertainty rule** $\frac{df}{f} = \sum\lvert n_i\rvert
  \frac{dx_i}{x_i}$. The general total differential is printed; this
  ready-to-use form is not, and it is what you actually need under time pressure.
- That the total differential with absolute values gives a **worst-case** bound,
  not a statistical estimate
- **How to identify which input dominates** an uncertainty, and that you cannot
  rank them by inspection
- That the gradient points in the direction of **steepest increase**, that its
  magnitude is the **maximum rate**, and that it is **perpendicular to level
  curves**
- That transport laws carry a **minus sign**: $\mathbf{q} = -k\nabla T$ and its
  relatives
- That a directional derivative requires a **unit** vector, and that
  $\lvert D_{\mathbf{u}}f\rvert \le \lvert\nabla f\rvert$
- The **output types**: gradient → vector, divergence → scalar, curl → vector
- The physical readings: divergence as source strength, $\nabla\cdot\mathbf{v} = 0$
  as incompressible continuity, curl as local rotation, zero curl as conservative
- That the tangent plane **is** the first-order multivariable Taylor polynomial,
  and inherits the locality warnings from Chapter 01-22
- The **Lagrange condition** $\nabla f = \lambda\nabla g$ and the tangency picture
  behind it
- That $h = 2r$ minimizes the surface area of a closed cylinder — a result worth
  recognizing rather than re-deriving

---

## Where This Goes Wrong

**Using $d$ where $\partial$ belongs.** They mean different things.
$\frac{\partial f}{\partial x}$ freezes the other variables;
$\frac{df}{dx}$ does not.

**Forgetting to freeze the other variable.** Differentiating $x^2y$ with respect
to $x$ gives $2xy$, not $2x$. The frozen variable rides along as a coefficient.

**Dropping the chain factor in a composite.**
$\frac{\partial}{\partial x}e^{xy} = ye^{xy}$. The inner derivative is $y$, not 1.

**Reporting the divergence as a vector or the curl as a scalar.** Check the output
type before anything else. Gradient and curl are vectors; divergence is a scalar.

**Sign error in the middle component of the curl.** The determinant expansion
carries $+,-,+$, so the $\hat{\jmath}$ term is
$\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}$. Write out the
determinant rather than recalling the expansion.

**Pairing matched subscripts inside a curl.** Every curl term mixes different
subscripts and variables. Matching pairs belong to the divergence.

**Failing to normalize the direction vector.** A directional derivative requires
$\lvert\mathbf{u}\rvert = 1$. Using an unnormalized vector scales the answer by its
magnitude.

**Omitting the minus sign in a transport law.** $\mathbf{q} = -k\nabla T$. Heat
flows *down* the gradient; the gradient points *up*. Without the sign, your heat
flows the wrong way.

**Dropping the sign of a negative partial in error propagation or a chain rule.**
For uncertainty, take the absolute value — errors accumulate rather than cancel.
For a rate, **keep** the sign, because the effects genuinely oppose. Confusing
those two conventions is the most common slip in §23.3 and §23.4.

**Ranking uncertainty contributions by inspection.** The exponent and the
measurement quality both matter. Worked Examples 4 and 5 come out opposite ways
with the same formula structure.

**Treating a critical point as an extremum without testing.** Saddle points have
$\nabla f = \mathbf{0}$ too. Run the discriminant.

**Reading $D = 0$ as a conclusion.** It means the test failed. Investigate along
lines through the point, as in Worked Example 9's check.

**Forgetting to apply the constraint in a Lagrange problem.** The condition
$\nabla f = \lambda\nabla g$ alone is underdetermined; you need $g = k$ as well.
The constraint is an equation, not background information.

**Reporting $\lambda$ as the answer.** The multiplier is scaffolding. The answer is
the values of the variables.

**Extrapolating a tangent plane far from the point of tangency.** It is a
first-order Taylor polynomial, and Chapter 01-22's locality warning applies
unchanged: error grows as the square of the distance.

---

## Key Terms

| Term | Definition |
|---|---|
| Function of several variables | Assigns a scalar to each point of a multidimensional domain |
| Surface | The graph $z = f(x,y)$ in three dimensions |
| Level curve / contour | The set where $f$ equals a fixed value |
| Partial derivative | Derivative with respect to one variable, others held constant |
| Mixed partial | Second derivative taken in two different variables |
| Equality of mixed partials | $f_{xy} = f_{yx}$ when the second partials are continuous |
| Total differential | $df = f_x\,dx + f_y\,dy + \cdots$ |
| Error propagation | Using the total differential to bound output uncertainty from input uncertainties |
| Power-law rule | For a product of powers, relative errors add weighted by exponents |
| Tangent plane | The first-order Taylor approximation to a surface at a point |
| Multivariable chain rule | $\frac{df}{dt} = \sum \frac{\partial f}{\partial x_i}\frac{dx_i}{dt}$ |
| Del operator $\nabla$ | The vector of partial derivative operators |
| Gradient | $\nabla f$; a vector pointing in the direction of steepest increase |
| Directional derivative | $D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u}$ with $\mathbf{u}$ a unit vector |
| Divergence | $\nabla\cdot\mathbf{F}$; a scalar measuring net outflow per unit volume |
| Solenoidal | Having zero divergence |
| Curl | $\nabla\times\mathbf{F}$; a vector measuring local rotation |
| Irrotational | Having zero curl; equivalently, conservative |
| Conservative field | Expressible as the gradient of a scalar potential |
| Critical point | A point where every first partial vanishes |
| Saddle point | A critical point that rises in one direction and falls in another |
| Discriminant $D$ | $f_{xx}f_{yy} - f_{xy}^2$; classifies critical points |
| Constrained optimization | Optimizing subject to an equation relating the variables |
| Lagrange multiplier | The scalar $\lambda$ in $\nabla f = \lambda\nabla g$ |

---

## Review Questions

### Conceptual

1. Explain the difference between $\frac{\partial f}{\partial x}$ and
   $\frac{df}{dx}$, and describe a situation where the two differ.
2. State what the equality of mixed partials says, and explain how you can use it
   as a check on your own work.
3. Explain how the tangent plane relates to the multivariable Taylor expansion, and
   what that implies about the range over which it is trustworthy.
4. In an error propagation calculation you take absolute values; in a related-rates
   calculation you keep signs. Explain why the two conventions differ.
5. State the two defining properties of the gradient, and explain why it must be
   perpendicular to the level curves.
6. Why does Fourier's law carry a minus sign?
7. State the output type of the gradient, divergence, and curl, and explain how the
   notation itself tells you each one.
8. Give a physical interpretation of $\nabla\cdot\mathbf{v} = 0$ for a fluid
   velocity field.
9. Describe a saddle point and explain why nothing analogous appears in
   single-variable calculus.
10. Explain the geometric reason behind the Lagrange condition
    $\nabla f = \lambda\nabla g$.

### Calculation

11. For $f(x,y) = 4x^3y^2 - 5xy + 2y^4$, find $f_x$, $f_y$, $f_{xx}$, $f_{yy}$, and
    both mixed partials. Verify they agree.
12. For $f(x,y) = \ln(x^2 + y)$, find $f_x$ and $f_y$ at $(2, 1)$.
13. A rectangular plate is measured as $a = 240 \pm 2$ mm and $b = 120 \pm 1$ mm.
    Find the area and its relative uncertainty, and identify which measurement
    contributes more.
14. Power is computed as $P = I^2R$ with $I = 3.50 \pm 0.04$ A and
    $R = 22.0 \pm 0.3\ \Omega$. Find $P$ and its uncertainty, and give each
    input's share.
15. For $f(x,y) = x^2y - y^3$ at $(3, 1)$: find $\nabla f$, the maximum rate of
    increase, and the directional derivative toward $(3, 5)$.
16. Find $\nabla\cdot\mathbf{F}$ and $\nabla\times\mathbf{F}$ at $(1,1,2)$ for
    $\mathbf{F} = xy\,\hat{\imath} + yz^2\,\hat{\jmath} + z x\,\hat{k}$.
17. Locate and classify all critical points of
    $f(x,y) = x^2 + xy + y^2 - 6x$.
18. A rectangular box with an open top must have volume $32$ m³. Use Lagrange
    multipliers to find the dimensions minimizing surface area.
19. **Engineering application.** Beam deflection at midspan under a central load is
    $\delta = \frac{PL^3}{48EI}$. A beam has $P = 25.0 \pm 0.5$ kN,
    $L = 4.00 \pm 0.01$ m, $E = 200 \pm 5$ GPa, and
    $I = 85.0 \pm 1.5 \times 10^6$ mm⁴.
    (a) Compute $\delta$ in mm.
    (b) Find the relative uncertainty using the power-law rule.
    (c) Rank the four inputs by contribution and state which measurement to
    improve first.

### Multiple Choice

20. For $f(x,y) = x^2y^3$, $f_y$ equals:
    A) $2xy^3$  B) $3x^2y^2$  C) $6xy^2$  D) $2x y^3 + 3x^2y^2$

21. The gradient of a scalar field is:
    A) a scalar  B) a vector  C) a matrix  D) always zero

22. The divergence of a vector field is:
    A) a scalar  B) a vector  C) perpendicular to the field  D) the same as the curl

23. For $V = \pi r^2 h$ with $r$ known to 1% and $h$ to 1%, the worst-case relative
    uncertainty in $V$ is about:
    A) 1%  B) 2%  C) 3%  D) 4%

24. At a critical point with $D = f_{xx}f_{yy} - f_{xy}^2 < 0$, the point is:
    A) a local minimum  B) a local maximum  C) a saddle point  D) undetermined

25. A field with $\nabla\times\mathbf{F} = \mathbf{0}$ is called:
    A) solenoidal  B) irrotational  C) divergent  D) incompressible

26. The directional derivative $D_{\mathbf{u}}f$ is largest when $\mathbf{u}$ is:
    A) perpendicular to $\nabla f$  B) parallel to $\nabla f$  C) along a level
    curve  D) the zero vector

27. In Fourier's law $\mathbf{q} = -k\nabla T$, the minus sign indicates that:
    A) conductivity is negative  B) heat flows toward higher temperature
    C) heat flows down the temperature gradient  D) the gradient is a scalar

---

## Answers to Review Questions

### Conceptual

1. $\frac{\partial f}{\partial x}$ holds the other variables fixed;
   $\frac{df}{dx}$ includes their response. They differ whenever another variable
   depends on $x$ — for instance in Worked Example 6, where both $V$ and $R$ change
   with time and $\frac{dP}{dt}$ collects both effects while
   $\frac{\partial P}{\partial V}$ collects one.
2. $f_{xy} = f_{yx}$ for continuous second partials. Computing both and comparing
   is a free verification: disagreement means an algebra error, since the theorem
   holds for essentially all engineering functions.
3. The tangent plane is the degree-1 multivariable Taylor polynomial. Chapter
   01-22's Lagrange remainder applies, so the error grows as the **square** of the
   distance from the point of tangency — the approximation is strictly local and
   degrades by a power law.
4. Uncertainties could push either way, so the conservative bound assumes they all
   push the same way and adds magnitudes. A rate of change has a definite
   direction, so opposing effects genuinely cancel and the signs must be kept.
   Worked Example 6 would be three times too large with absolute values.
5. It points in the direction of steepest increase, and its magnitude is that
   maximum rate. Along a level curve $f$ does not change, so the direction of
   greatest change must be perpendicular to it.
6. The gradient points toward higher temperature; heat flows toward lower. The
   minus sign reverses the direction so the flux vector points the way energy
   actually moves.
7. Gradient → vector, divergence → scalar, curl → vector. The dot in
   $\nabla\cdot\mathbf{F}$ signals a scalar output and the cross in
   $\nabla\times\mathbf{F}$ a vector output, matching the dot and cross products of
   Chapter 01-13.
8. Net outflow from every point is zero, so mass cannot accumulate anywhere — the
   continuity equation for incompressible flow.
9. A critical point where the surface rises along one direction and falls along a
   perpendicular one. It requires at least two independent directions to exist, and
   a single-variable function has only one.
10. At the constrained optimum the level curve of $f$ is tangent to the constraint
    curve; if they crossed, sliding along the constraint would reach a better level
    curve. Tangent curves share a normal direction, and gradients are normals, so
    the two gradients are parallel.

### Calculation

11. $f_x = 12x^2y^2 - 5y$; $f_y = 8x^3y - 5x + 8y^3$;
    $f_{xx} = 24xy^2$; $f_{yy} = 8x^3 + 24y^2$;
    $f_{xy} = f_{yx} = 24x^2y - 5$ ✓
12. $f_x = \frac{2x}{x^2+y} = \frac{4}{5} = \mathbf{0.800}$;
    $f_y = \frac{1}{x^2+y} = \frac{1}{5} = \mathbf{0.200}$
13. $A = 28{,}800$ mm². $\frac{dA}{A} = \frac{2}{240} + \frac{1}{120} =
    0.00833 + 0.00833 = \mathbf{1.67\%}$, so $dA = 480$ mm². The two contribute
    **equally** — both are measured to the same relative precision and both carry
    exponent 1.
14. $P = (3.50)^2(22.0) = 269.5$ W.
    $\frac{dP}{P} = 2\left(\frac{0.04}{3.50}\right) + \frac{0.3}{22.0} =
    0.02286 + 0.01364 = \mathbf{3.65\%}$, so $dP = 9.8$ W.
    Current: $62.6\%$; resistance: $37.4\%$.
15. $f_x = 2xy = 6$; $f_y = x^2 - 3y^2 = 9 - 3 = 6$. So
    $\nabla f = 6\hat{\imath} + 6\hat{\jmath}$,
    $\lvert\nabla f\rvert = 6\sqrt{2} = \mathbf{8.49}$.
    Toward $(3,5)$ the direction is $\langle 0,4\rangle$, unit vector
    $\langle 0,1\rangle$, so $D_{\mathbf{u}}f = \mathbf{6.00}$. Check:
    $6.00 \le 8.49$ ✓
16. $\nabla\cdot\mathbf{F} = y + z^2 + x = 1 + 4 + 1 = \mathbf{6}$.
    $\nabla\times\mathbf{F}$: $\hat{\imath}$: $0 - 2yz = -2yz = -4$;
    $\hat{\jmath}$: $0 - z = -2$; $\hat{k}$: $0 - x = -1$.
    So $\nabla\times\mathbf{F} = \mathbf{-4\hat{\imath} - 2\hat{\jmath} -
    \hat{k}}$.
17. $f_x = 2x + y - 6 = 0$ and $f_y = x + 2y = 0 \implies x = -2y$. Substituting:
    $-4y + y - 6 = 0 \implies y = -2$, $x = 4$. Critical point $(4,-2)$.
    $f_{xx} = 2$, $f_{yy} = 2$, $f_{xy} = 1$, so $D = 4 - 1 = 3 > 0$ with
    $f_{xx} > 0$: **local minimum**, $f(4,-2) = 16 - 8 + 4 - 24 = -12$.
18. Minimize $A = xy + 2xz + 2yz$ subject to $xyz = 32$. The conditions give
    $x = y = 2z$, so $4z^3 = 32 \implies z = 2$, and
    $\mathbf{x = y = 4\ m}$, $\mathbf{z = 2\ m}$, with
    $A = 16 + 16 + 16 = \mathbf{48\ m^2}$.
19. (a) With $I = 85.0\times10^6$ mm⁴ $= 85.0\times10^{-6}$ m⁴ and
    $E = 200\times10^9$ Pa:

    $$\delta = \frac{25.0\times10^3(4.00)^3}{48\left(200\times10^9\right)\left(85.0\times10^{-6}\right)} = \frac{1.600\times10^6}{8.160\times10^8} = 1.961\times10^{-3}\text{ m} = \mathbf{1.96\ mm}$$

    (b) Exponents are $1, 3, -1, -1$:

    $$\frac{d\delta}{\delta} \le \frac{0.5}{25.0} + 3\left(\frac{0.01}{4.00}\right) + \frac{5}{200} + \frac{1.5}{85.0}$$
    $$= 0.02000 + 0.00750 + 0.02500 + 0.01765 = \mathbf{7.02\%}$$

    So $\delta = 1.96 \pm 0.14$ mm.

    (c) Ranked: $E$ at $35.6\%$, $P$ at $28.5\%$, $I$ at $25.1\%$, $L$ at
    $10.7\%$. **Improve the modulus first.** Note the lesson — length has the
    largest exponent by far, yet contributes least, because it is measured to
    0.25% while the modulus is known only to 2.5%. A large exponent on a
    well-known quantity is harmless; a small exponent on a poorly known one is
    not.

### Multiple Choice

20. **B** — differentiate in $y$ with $x$ frozen.
21. **B** — a vector.
22. **A** — a scalar, as the dot product signals.
23. **C** — $2(1\%) + 1(1\%) = 3\%$.
24. **C** — saddle point.
25. **B** — irrotational; solenoidal and incompressible refer to zero divergence.
26. **B** — parallel to $\nabla f$, giving $D_{\mathbf{u}}f = \lvert\nabla
    f\rvert$.
27. **C** — heat flows down the gradient, opposite to the gradient's direction.

---

## Summary Card

**Partial derivatives** — differentiate in one variable, freeze the rest. All
Chapter 01-17 rules apply. Mixed partials commute: $f_{xy} = f_{yx}$.

**Total differential and error propagation**

$$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \cdots \qquad \lvert df\rvert \le \sum\left\lvert\frac{\partial f}{\partial x_i}\right\rvert\lvert dx_i\rvert$$

**Power-law shortcut** — for $f = Cx^ay^bz^c$:

$$\frac{\lvert df\rvert}{f} \le \lvert a\rvert\frac{\lvert dx\rvert}{x} + \lvert b\rvert\frac{\lvert dy\rvert}{y} + \lvert c\rvert\frac{\lvert dz\rvert}{z}$$

Worst case, not statistical. Rank the terms to find the dominant input.

**Tangent plane** — the first-order Taylor polynomial:

$$z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$

**Chain rule** — $\dfrac{df}{dt} = \sum \dfrac{\partial f}{\partial x_i}\dfrac{dx_i}{dt}$. Keep the signs.

**Vector operators**

| Operator | Formula | Output | Reading |
|---|---|---|---|
| $\nabla f$ | $\left\langle f_x, f_y, f_z\right\rangle$ | vector | steepest increase; $\perp$ contours |
| $\nabla\cdot\mathbf{F}$ | $\frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$ | scalar | source $(+)$, sink $(-)$, solenoidal $(0)$ |
| $\nabla\times\mathbf{F}$ | determinant with $\hat{\imath},\hat{\jmath},\hat{k}$ | vector | local rotation; $\mathbf{0}$ = conservative |

$$D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u}, \quad \lvert\mathbf{u}\rvert = 1, \quad \lvert D_{\mathbf{u}}f\rvert \le \lvert\nabla f\rvert$$

**Transport laws** — all carry a minus sign:
$\mathbf{q} = -k\nabla T$, $\mathbf{J} = -D\nabla C$, $\mathbf{v} = -K\nabla h$,
$\mathbf{E} = -\nabla V$.

**Optimization** — critical points where $\nabla f = \mathbf{0}$, then
$D = f_{xx}f_{yy} - f_{xy}^2$:

| $D$ | $f_{xx}$ | Type |
|---|---|---|
| $>0$ | $>0$ | minimum |
| $>0$ | $<0$ | maximum |
| $<0$ | — | saddle |
| $=0$ | — | test fails |

**Constrained** — solve $\nabla f = \lambda\nabla g$ **together with** $g = k$.
Discard $\lambda$. Closed cylinder of minimum area: $h = 2r$.

---

## Looking Ahead

Three threads leave this chapter.

**Multiple integration** comes next, in Chapter 01-24. Partial differentiation
sliced a multivariable function one direction at a time; double and triple
integrals accumulate over a region instead. That is how the centroid and
second-moment integrals from Chapter 01-20 generalize to shapes that cannot be
described by a single vertical slice.

**Differential equations** follow in Chapter 01-25. An equation relating a
function to its derivatives is the standard form of a physical law, and the
gradient, divergence, and curl assembled here are the building blocks of the
partial differential equations behind heat conduction, fluid flow, and
electromagnetics. You will not solve those in Tier 1C, but you will recognize them.

**The transport laws** recur across every discipline track. Fourier's law appears
in Chapter 02-55, Fick's law in the chemical and environmental tracks, Darcy's law
in the civil and environmental tracks, and $\mathbf{E} = -\nabla V$ in Chapter
02-61. All four are the same statement, and you now know what the statement says.

More immediately, the error propagation habit from §23.3 belongs to you rather
than to this chapter. Every time a later problem hands you measured inputs and asks
for a computed output, the power-law rule tells you how much confidence the answer
deserves — and which measurement to blame.
