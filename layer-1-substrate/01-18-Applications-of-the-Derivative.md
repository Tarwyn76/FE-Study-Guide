---
chapter: "01-18"
title: "Applications of the Derivative"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-018-01, MATH-1C-018-02, MATH-1C-018-03, MATH-1C-018-04, MATH-1C-018-05]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-18: Applications of the Derivative

> *"Chapter 01-17 gave you a machine that computes rates. This chapter is what
> the machine is for. Where is the stress highest? What diameter costs least?
> How fast is the level dropping right now? How much does a 1% measurement
> error cost me in the answer? Every one of those is a derivative question, and
> engineering asks them all day long. The mathematics is already built. What
> remains is learning to recognize the question."*

---

## Before You Start

**Prerequisites:** [01-07 Polynomials and Their Roots](01-07-polynomials-roots.md) · [01-09 Lines and Analytic Geometry](01-09-lines-analytic-geometry.md) · [01-11 Trigonometry](01-11-trigonometry.md) · [01-16 Limits and Continuity](01-16-limits-continuity.md) · [01-17 The Derivative](01-17-the-derivative.md)

**Skip if:** You pass the Tier 1C test-out quiz. Verify you can classify
critical points with both derivative tests, set up and solve a constrained
optimization problem from a word description, and complete a related-rates
problem including the units of the answer before skipping. Related rates is the
most commonly rusty item here — the calculus is trivial and the setup is not.

**Time:** ~70 min read · ~30 min review questions · ~80 min practice problems

---

## On the Board Today

Apprentice, you can now differentiate. That was the hard part, and it is done.

What follows is the payoff, and it comes in five distinct uses. They look
unrelated at first and they are all the same idea seen from different angles.

**Extrema.** The derivative is zero where the curve is flat, and a curve is
flat at its peaks and valleys. So setting $f' = 0$ finds the maximum and
minimum of anything you can write down. That is the whole basis of design
optimization: minimum weight, minimum cost, maximum efficiency, maximum power.
When a client asks for the best design, they are asking you to find where a
derivative vanishes.

**Curve behaviour.** The sign of $f'$ tells you whether a quantity is rising or
falling. The sign of $f''$ tells you how it is bending. Together they let you
sketch or interpret a curve without plotting a single point — which matters when
you need to know the *shape* of a response, not just its values.

**Related rates.** When two quantities are geometrically or physically linked,
their rates are linked too, and the chain rule is the link. A tank's level and
its volume are related; therefore the rate of level change and the rate of
volume change are related. This is where the chain rule stops being an algebra
exercise and starts being a modelling tool.

**Indeterminate limits.** L'Hôpital's rule finally arrives. I promised it in
Chapter 01-16 and deferred it because it needs derivatives. It is a genuine
shortcut, and it is in the Handbook.

**Linear approximation and error.** Near any point, a differentiable function
looks like its tangent line. That single fact lets you estimate values without
recomputing, and — far more importantly for engineering — lets you propagate
measurement uncertainty through a calculation. If your diameter measurement is
good to 1%, how good is your flow rate? That is a derivative question, and the
answer is often uncomfortable.

One theorem underpins the first two uses, so we start there.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 18.1 State the Mean Value Theorem and explain what it guarantees
* 18.2 Determine intervals where a function increases and decreases from the
  sign of $f'$
* 18.3 Locate critical points and classify them with the first derivative test
* 18.4 Apply the second derivative test and recognize when it is inconclusive
* 18.5 Determine concavity and locate inflection points from $f''$
* 18.6 Find absolute extrema on a closed interval using the closed-interval
  method
* 18.7 Sketch a curve from information carried by $f'$ and $f''$
* 18.8 Set up and solve constrained optimization problems, including
  identifying the objective function and the constraint
* 18.9 Verify that an optimization result is a minimum or maximum rather than
  assuming it
* 18.10 Set up and solve related-rates problems, including correct signs and
  units
* 18.11 Apply L'Hôpital's rule to $0/0$ and $\infty/\infty$ forms, and convert
  other indeterminate forms into one of those two
* 18.12 Use the tangent line to make linear approximations and estimate
  function values
* 18.13 Propagate measurement uncertainty through a calculation using
  differentials, and compute relative error for power-law relationships

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $f'$, $f''$ | first and second derivatives | as in Chapter 01-17 |
| critical point | a point where $f' = 0$ or $f'$ is undefined | interior to the domain |
| $[a,b]$ | closed interval, endpoints included | required for the closed-interval method |
| $(a,b)$ | open interval, endpoints excluded | — |
| $\Delta x$, $\Delta y$ | actual finite changes | measured or exact |
| $dx$, $dy$ | differentials | the linear estimate of the change |
| $\dfrac{dy}{y}$ | relative (fractional) change | multiply by 100 for percent |
| $c$ | the point guaranteed by the Mean Value Theorem | not a constant here |

> ---
> **Mentor's Margin**
>
> Two words that get confused, and the distinction is graded on the exam.
>
> A **local** (relative) extremum is the highest or lowest value in some small
> neighbourhood. There can be many.
>
> An **absolute** (global) extremum is the highest or lowest value on the
> entire domain or interval under consideration. There is at most one of each
> value.
>
> A local maximum need not be the absolute maximum, and the absolute maximum on
> a closed interval is frequently at an **endpoint**, where the derivative tells
> you nothing at all. Read the question. "Find the local maxima" and "find the
> maximum value on $[0,5]$" are different tasks with different procedures.
>
> ---

---

## 18.1 The Mean Value Theorem

Everything in the next three sections rests on one theorem, so it is worth
thirty seconds.

> **Mean Value Theorem (MVT).** If $f$ is continuous on $[a,b]$ and
> differentiable on $(a,b)$, then there exists at least one $c$ in $(a,b)$ with
>
> $$f'(c) = \frac{f(b) - f(a)}{b - a}$$

In words: somewhere inside the interval, the instantaneous rate of change
equals the average rate of change over the whole interval.

The physical reading is immediate. If you cover 180 km in 2 hours, your average
speed was 90 km/h, and at some instant your speedometer read exactly 90 km/h.
It could not have stayed below 90 the whole way and still covered the distance.

![FIG-01-18-001: Curve y = f(x) over the interval [a, b] with a secant line drawn between the endpoints (a, f(a)) and (b, f(b)). A tangent line parallel to the secant is drawn at an interior point c, with both slopes labeled — the secant as [f(b) − f(a)]/(b − a) and the tangent as f'(c) — and a note "same slope, guaranteed to exist somewhere in (a, b)". Vertical dashed line drops from the tangency point to c on the axis.](../figures/FIG-01-18-001-mean-value-theorem.png)

### Why it matters here

The MVT is what licenses the sign test you are about to use. Suppose
$f' > 0$ everywhere on an interval. Take any two points $x_1 < x_2$ in it. By
the MVT there is a $c$ between them with

$$f'(c) = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$$

The left side is positive, and the denominator on the right is positive, so
$f(x_2) > f(x_1)$. The function increases. That is the proof, and it is short,
but without the MVT the connection between "positive derivative" and
"increasing function" would be an assumption rather than a fact.

**Rolle's Theorem** is the special case $f(a) = f(b)$, which forces
$f'(c) = 0$: a function that returns to the same value must have a flat spot in
between.

### Worked Example 1 — Verifying the MVT

**Given.** $f(x) = x^2$ on $[1, 4]$.

**Find.** The value of $c$ guaranteed by the MVT.

**Solution.**

$f$ is a polynomial, so it is continuous and differentiable everywhere — both
hypotheses hold automatically.

Average rate of change:

$$\frac{f(4) - f(1)}{4 - 1} = \frac{16 - 1}{3} = 5$$

Set $f'(c) = 5$ with $f'(x) = 2x$:

$$2c = 5 \implies \boxed{c = 2.5}$$

And $2.5$ lies in $(1,4)$ ✓ as the theorem promises.

---

## 18.2 Increasing, Decreasing, and Critical Points

### The sign of the first derivative

| On an interval | The function |
|---|---|
| $f'(x) > 0$ | increases |
| $f'(x) < 0$ | decreases |
| $f'(x) = 0$ throughout | is constant |

A **critical point** of $f$ is an interior point of the domain where

$$f'(x) = 0 \qquad \text{or} \qquad f'(x) \text{ does not exist}$$

The second clause matters. A corner is a critical point — $\lvert x\rvert$ has
its minimum at $x = 0$, where the derivative does not exist. If you only solve
$f' = 0$, you will miss extrema at corners and cusps, and Chapter 01-17 told you
those are all over engineering models.

### Fermat's principle for extrema

If $f$ has a local extremum at an interior point $c$, then $c$ is a critical
point.

**The converse is false**, and this is the trap. $f' = 0$ does not guarantee an
extremum. Consider $f(x) = x^3$ at $x = 0$: the derivative is zero, the tangent
is horizontal, and the function marches straight through — no maximum, no
minimum. It is a flat spot on a rising curve.

![FIG-01-18-002: Four panels labeled "f'(c) = 0 — four possibilities". Panel 1: a smooth peak, horizontal tangent at the top, labeled "local maximum, f' goes + to −". Panel 2: a smooth valley, horizontal tangent at the bottom, labeled "local minimum, f' goes − to +". Panel 3: the curve y = x³ near the origin with a horizontal tangent at (0,0) and the curve continuing upward on both sides, labeled "neither — f' stays positive". Panel 4: the V shape of |x| at the origin, labeled "local minimum, but f' does not exist — still a critical point". Below each panel, a small sign strip shows the sign of f' on either side.](../figures/FIG-01-18-002-critical-point-types.png)

### The first derivative test

Find the critical points. Then check the **sign of $f'$** on each side.

| $f'$ changes | Conclusion at that point |
|---|---|
| $+ \to -$ | local **maximum** |
| $- \to +$ | local **minimum** |
| no change | neither |

The reliable way to organize this is a **sign chart**: mark the critical points
on a number line, then test one convenient value of $f'$ in each interval
between them.

![FIG-01-18-003: A number line for f'(x) = 3(x − 3)(x + 1) with critical points marked at x = −1 and x = 3. Three intervals labeled with a test value and the resulting sign: x = −2 gives +, x = 0 gives −, x = 4 gives +. Below the line, arrows show the behaviour of f: rising, falling, rising. The two critical points are annotated "local max" and "local min". Beside the chart, the factored form is shown with each factor's sign tabulated per interval.](../figures/FIG-01-18-003-sign-chart.png)

### Worked Example 2 — First Derivative Test

**Given.** $f(x) = x^3 - 3x^2 - 9x + 5$

**Find.** Intervals of increase and decrease, and all local extrema.

**Solution.**

$$f'(x) = 3x^2 - 6x - 9 = 3\left(x^2 - 2x - 3\right) = 3(x-3)(x+1)$$

Critical points: $x = -1$ and $x = 3$. The derivative is a polynomial, defined
everywhere, so there are no others.

Sign chart — test one point per interval:

| Interval | Test $x$ | $f'(x) = 3(x-3)(x+1)$ | Sign | $f$ |
|---|---|---|---|---|
| $(-\infty, -1)$ | $-2$ | $3(-5)(-1) = 15$ | $+$ | increasing |
| $(-1, 3)$ | $0$ | $3(-3)(1) = -9$ | $-$ | decreasing |
| $(3, \infty)$ | $4$ | $3(1)(5) = 15$ | $+$ | increasing |

$$\boxed{\text{Increasing on } (-\infty,-1) \text{ and } (3,\infty); \text{ decreasing on } (-1,3)}$$

At $x = -1$ the derivative goes $+ \to -$: local **maximum**.

$$f(-1) = -1 - 3 + 9 + 5 = 10$$

At $x = 3$ the derivative goes $- \to +$: local **minimum**.

$$f(3) = 27 - 27 - 27 + 5 = -22$$

$$\boxed{\text{Local max } (-1, 10); \quad \text{local min } (3, -22)}$$

---

## 18.3 Concavity, Inflection Points, and the Second Derivative Test

### The sign of the second derivative

$f''$ is the rate of change of the slope, so it describes **bending**.

| On an interval | Concavity | Shape |
|---|---|---|
| $f'' > 0$ | concave **up** | holds water; slope increasing |
| $f'' < 0$ | concave **down** | spills water; slope decreasing |

An **inflection point** is where concavity changes. Two conditions:

$$f''(x) = 0 \text{ or undefined} \qquad \textbf{and} \qquad f'' \text{ actually changes sign there}$$

Both are required. $f(x) = x^4$ has $f''(0) = 0$ but $f'' = 12x^2 \ge 0$ on both
sides — no sign change, no inflection point.

![FIG-01-18-004: A single S-shaped curve with the left portion shaded and labeled "concave down, f'' < 0" and the right portion labeled "concave up, f'' > 0", separated by a vertical dashed line at the inflection point, which is marked with a dot and labeled. Small tangent lines drawn at three points on each side illustrate slopes decreasing on the left and increasing on the right. A second small panel beside it shows y = x⁴ near the origin with f''(0) = 0 marked and the annotation "no sign change — not an inflection point".](../figures/FIG-01-18-004-concavity-inflection.png)

### The second derivative test

At a critical point $c$ where $f'(c) = 0$:

| $f''(c)$ | Conclusion |
|---|---|
| $f''(c) < 0$ | local **maximum** (concave down at a flat spot) |
| $f''(c) > 0$ | local **minimum** (concave up at a flat spot) |
| $f''(c) = 0$ | **inconclusive** — fall back on the first derivative test |

This is usually faster than a sign chart, because it needs one evaluation
instead of a table. Two limitations: it says nothing when $f''(c) = 0$, and it
does not apply at all where $f'$ is undefined.

> ---
> **Mentor's Margin**
>
> Use the second derivative test first — it is one substitution. When it returns
> zero, do not guess. Fall back on the first derivative test, which always
> works.
>
> The classic pair that makes the point: $f(x) = x^4$ has $f''(0) = 0$ and a
> genuine minimum at the origin. $f(x) = x^3$ has $f''(0) = 0$ and no extremum
> at all. Same inconclusive test result, opposite answers. That is why "$f'' = 0$
> so it must be an inflection point" is wrong reasoning.
>
> ---

### Worked Example 3 — Concavity and the Second Derivative Test

**Given.** The same $f(x) = x^3 - 3x^2 - 9x + 5$.

**(a)** Find intervals of concavity and any inflection point.
**(b)** Reclassify the critical points using the second derivative test and
confirm agreement with Worked Example 2.

**Solution.**

**(a)** From $f'(x) = 3x^2 - 6x - 9$:

$$f''(x) = 6x - 6 = 6(x-1)$$

$f'' = 0$ at $x = 1$.

| Interval | Test $x$ | $f''$ | Concavity |
|---|---|---|---|
| $(-\infty, 1)$ | $0$ | $-6$ | down |
| $(1, \infty)$ | $2$ | $+6$ | up |

The sign changes, so $x = 1$ is a genuine inflection point.

$$f(1) = 1 - 3 - 9 + 5 = -6$$

$$\boxed{\text{Concave down on } (-\infty,1), \text{ up on } (1,\infty); \text{ inflection at } (1,-6)}$$

**(b)**

$$f''(-1) = 6(-1) - 6 = -12 < 0 \implies \text{local maximum} \;\checkmark$$

$$f''(3) = 6(3) - 6 = +12 > 0 \implies \text{local minimum} \;\checkmark$$

Both agree with the first derivative test, at a fraction of the work.

### Worked Example 4 — When the Second Derivative Test Fails

**Given.** $f(x) = x^4$.

**Classify** the critical point at $x = 0$.

**Solution.**

$$f'(x) = 4x^3 \implies f'(0) = 0 \quad \text{(critical point)}$$

$$f''(x) = 12x^2 \implies f''(0) = 0 \quad \text{(inconclusive)}$$

Fall back on the first derivative test with $f' = 4x^3$:

| Interval | Test $x$ | $f'$ | Sign |
|---|---|---|---|
| $(-\infty,0)$ | $-1$ | $-4$ | $-$ |
| $(0,\infty)$ | $1$ | $+4$ | $+$ |

The derivative changes $- \to +$, so

$$\boxed{x = 0 \text{ is a local (and absolute) minimum}, \; f(0) = 0}$$

Compare $g(x) = x^3$: also $g'(0) = g''(0) = 0$, but $g' = 3x^2$ is positive on
both sides — no sign change, **no extremum**. Identical inconclusive test
result, opposite conclusion.

---

## 18.4 Absolute Extrema on a Closed Interval

> **Extreme Value Theorem.** A continuous function on a **closed** interval
> $[a,b]$ attains both an absolute maximum and an absolute minimum somewhere on
> that interval.

Both hypotheses are load-bearing. Drop continuity, or open the interval, and
the guarantee vanishes: $f(x) = x$ on $(0,1)$ has neither an absolute maximum
nor an absolute minimum, because it never reaches its endpoints.

### The closed-interval method

Three steps, and no derivative tests required:

1. Find all critical points in $(a,b)$
2. Evaluate $f$ at those critical points **and at both endpoints**
3. The largest value is the absolute maximum, the smallest the absolute minimum

You do not classify anything. You compare a finite list of numbers.

> ---
> **Mentor's Margin**
>
> Forgetting the endpoints is the most common error in this procedure, and it is
> particularly costly because the endpoint is frequently the answer. Physically
> that makes sense: a constrained design often performs best at the edge of its
> allowable range, not in the interior. The maximum stress in a member is
> usually at a support. The maximum efficiency of a pump within its allowable
> speed range may well be at the speed limit.
>
> Write the endpoint values down first, before you differentiate anything. Then
> you cannot forget them.
>
> ---

### Worked Example 5 — Closed-Interval Method

**Given.** $f(x) = x^3 - 3x^2 - 9x + 5$ on $[-2, 4]$.

**Find.** The absolute maximum and minimum.

**Solution.**

**Endpoints first.**

$$f(-2) = -8 - 12 + 18 + 5 = 3$$

$$f(4) = 64 - 48 - 36 + 5 = -15$$

**Critical points** (from Worked Example 2): $x = -1$ and $x = 3$, both inside
$(-2,4)$ ✓

$$f(-1) = 10 \qquad f(3) = -22$$

**Compare all four:**

| $x$ | $f(x)$ | |
|---|---|---|
| $-2$ | $3$ | endpoint |
| $-1$ | $10$ | critical |
| $3$ | $-22$ | critical |
| $4$ | $-15$ | endpoint |

$$\boxed{\text{Absolute max } 10 \text{ at } x = -1; \quad \text{absolute min } -22 \text{ at } x = 3}$$

Here both extrema happen to be interior. Change the interval to $[-2, 6]$ and
$f(6) = 216 - 108 - 54 + 5 = 59$, which makes the right endpoint the absolute
maximum instead. The answer depends on the interval, which is exactly why the
endpoints must be checked every time.

---

## 18.5 Curve Sketching

Assembling everything from $f$, $f'$, and $f''$ gives a complete picture of a
function's shape. The checklist:

1. **Domain** — where is $f$ defined?
2. **Intercepts** — set $x = 0$, then set $f(x) = 0$
3. **Asymptotes** — vertical where the denominator vanishes; horizontal from
   $\lim_{x\to\pm\infty}f(x)$ (Chapter 01-16)
4. **$f'$** — critical points, intervals of increase and decrease, local extrema
5. **$f''$** — concavity intervals, inflection points
6. **Plot** the key points and connect them respecting the slope and bending
   information

### Worked Example 6 — Complete Sketch

**Given.** $f(x) = x^3 - 3x^2 - 9x + 5$ once more.

**Assemble** the full description.

**Solution.**

**Domain.** All real numbers (polynomial).

**Intercepts.** $f(0) = 5$, so the $y$-intercept is $(0, 5)$. The $x$-intercepts
require solving a cubic; from the sign changes $f(-2) = 3 > 0$, $f(-1) = 10 > 0$,
$f(0) = 5 > 0$, $f(1) = -6 < 0$ and $f(4) = -15 < 0$, $f(5) = 125 - 75 - 45 + 5
= 10 > 0$, the Intermediate Value Theorem (Chapter 01-16) brackets roots in
$(0,1)$ and $(4,5)$. A third root lies below $-2$: $f(-3) = -27 - 27 + 27 + 5 =
-22 < 0$, so a root is in $(-3,-2)$. Three real roots, as a cubic with two
distinct extrema straddling the axis must have.

**Asymptotes.** None. Polynomials have no asymptotes;
$f \to -\infty$ as $x \to -\infty$ and $f \to +\infty$ as $x \to +\infty$.

**From $f'$.** Increasing on $(-\infty,-1)$ and $(3,\infty)$, decreasing on
$(-1,3)$. Local max $(-1, 10)$, local min $(3,-22)$.

**From $f''$.** Concave down on $(-\infty,1)$, up on $(1,\infty)$. Inflection at
$(1, -6)$.

**Sanity check on internal consistency.** The local max at $x=-1$ sits in the
concave-down region ✓ — a peak must be. The local min at $x=3$ sits in the
concave-up region ✓. The inflection at $x=1$ lies between them ✓, which it must
for a cubic. Note also that $x = 1$ is exactly the midpoint of $-1$ and $3$;
that is a general property of cubics, whose inflection point always bisects the
two critical points.

![FIG-01-18-005: Fully annotated sketch of f(x) = x³ − 3x² − 9x + 5 over roughly −3 ≤ x ≤ 5. Marked and labeled: y-intercept (0,5); local maximum (−1,10) with a horizontal tangent segment; local minimum (3,−22) with a horizontal tangent segment; inflection point (1,−6) with a dot and a short tangent segment; three x-axis crossings marked with open brackets in (−3,−2), (0,1), (4,5). The curve is shaded lightly in two bands labeled "concave down" left of x = 1 and "concave up" right of x = 1. Arrows along the curve indicate increasing, decreasing, increasing.](../figures/FIG-01-18-005-complete-curve-sketch.png)

---

## 18.6 Optimization

This is the application that pays your salary. The procedure:

1. **Identify the objective** — the quantity to be maximized or minimized.
   Write it as an equation.
2. **Identify the constraint** — the relationship that ties the variables
   together. Write it as an equation.
3. **Reduce to one variable** — solve the constraint for one variable and
   substitute into the objective.
4. **State the feasible domain** — physical limits on the remaining variable.
5. **Differentiate and set to zero.** Solve.
6. **Verify** it is the extremum you want, using the second derivative test or a
   sign chart. **Check the endpoints of the feasible domain.**
7. **Answer the question asked**, with units.

Step 6 is the one people skip. A critical point is not automatically a minimum.

> ---
> **Mentor's Margin**
>
> Steps 1 and 2 are the whole difficulty. Once you have a single-variable
> function the calculus is mechanical, and you have already done harder algebra
> than this.
>
> The discipline that makes setup reliable: draw the figure, label every
> dimension with a symbol, then write two sentences in plain words — "I want to
> minimize the surface area" and "the volume must equal 32 cubic metres" — before
> writing any equation. The first sentence is the objective, the second is the
> constraint. Students who go straight to equations reliably mix the two up, and
> then optimize the constraint by mistake.
>
> ---

### Worked Example 7 — Minimum Material for an Open Tank

**Given.** An open-top tank with a **square base** must hold 32 m³. Sheet
material cost is proportional to total surface area.

**Find.** The dimensions that minimize material, and the resulting area.

**Solution.**

Let $x$ be the base edge and $h$ the height, both in metres.

**Objective** — minimize surface area. Open top means base plus four sides:

$$A = x^2 + 4xh$$

**Constraint** — the volume is fixed:

$$x^2 h = 32$$

**Reduce.** Solve the constraint for $h$ and substitute:

$$h = \frac{32}{x^2} \implies A(x) = x^2 + 4x\left(\frac{32}{x^2}\right) = x^2 + \frac{128}{x}$$

**Feasible domain.** $x > 0$. Note $A \to \infty$ at both ends of that domain
(as $x \to 0^+$ the $128/x$ term blows up; as $x \to \infty$ the $x^2$ term
does), so an interior minimum must exist.

**Differentiate.** Rewrite as $A = x^2 + 128x^{-1}$:

$$A'(x) = 2x - \frac{128}{x^2}$$

Set to zero:

$$2x = \frac{128}{x^2} \implies 2x^3 = 128 \implies x^3 = 64 \implies x = 4 \text{ m}$$

**Verify.**

$$A''(x) = 2 + \frac{256}{x^3} \implies A''(4) = 2 + \frac{256}{64} = 6 > 0$$

Concave up, so this is a **minimum** ✓

**Answer.**

$$h = \frac{32}{16} = 2 \text{ m}$$

$$A = 16 + \frac{128}{4} = 16 + 32 = 48 \text{ m}^2$$

$$\boxed{4.00 \text{ m} \times 4.00 \text{ m base}, \; 2.00 \text{ m deep}; \; A = 48.0 \text{ m}^2}$$

**Check the constraint.** $V = 4^2(2) = 32$ m³ ✓

**Worth noticing.** The optimum has $h = x/2$ — the height is half the base
edge. That proportion is independent of the volume, which you can confirm by
redoing the algebra with a symbolic $V$. Optimal designs frequently come out as
fixed *proportions* rather than fixed dimensions, and that is a much more useful
result than any single number.

![FIG-01-18-006: Two-part figure. Left: an isometric sketch of an open-top square-base tank with the base edge labeled x on two sides and the height labeled h, the open top indicated by a dashed rim, and callouts "base area x²" and "four sides, each xh". Right: the plot of A(x) = x² + 128/x for 0 < x ≤ 10, a U-shaped curve with a vertical asymptote behaviour near x = 0, the minimum marked at (4, 48) with a horizontal tangent, and dashed guide lines to both axes.](../figures/FIG-01-18-006-tank-optimization.png)

### Worked Example 8 — Maximum Power Transfer

**Given.** A source of open-circuit voltage $V = 24$ V and internal resistance
$R_s = 8\ \Omega$ drives a load $R_L$. The power delivered to the load is

$$P = I^2 R_L \qquad \text{with} \qquad I = \frac{V}{R_s + R_L}$$

**Find.** The load resistance that maximizes delivered power, and that maximum
power.

**Solution.**

Substitute for $I$ to get a single-variable function:

$$P(R_L) = \frac{V^2 R_L}{\left(R_s + R_L\right)^2}$$

Differentiate with the quotient rule, treating $u = V^2R_L$ and
$v = (R_s+R_L)^2$:

$$\frac{dP}{dR_L} = \frac{V^2\left(R_s+R_L\right)^2 - V^2R_L\cdot 2\left(R_s+R_L\right)}{\left(R_s+R_L\right)^4}$$

Cancel one factor of $(R_s+R_L)$ from numerator and denominator:

$$= \frac{V^2\left[\left(R_s+R_L\right) - 2R_L\right]}{\left(R_s+R_L\right)^3} = \frac{V^2\left(R_s - R_L\right)}{\left(R_s+R_L\right)^3}$$

Set to zero. The denominator is positive for positive resistances, so:

$$R_s - R_L = 0 \implies \boxed{R_L = R_s = 8\ \Omega}$$

**Verify with a sign test** — easier here than a second derivative. The
denominator is always positive, so the sign of $\frac{dP}{dR_L}$ is the sign of
$(R_s - R_L)$:

| $R_L$ | $R_s - R_L$ | $dP/dR_L$ | $P$ |
|---|---|---|---|
| $< 8\ \Omega$ | $+$ | $+$ | increasing |
| $> 8\ \Omega$ | $-$ | $-$ | decreasing |

Changes $+ \to -$: a **maximum** ✓

**Maximum power.**

$$P_{\max} = \frac{(24)^2(8)}{(8+8)^2} = \frac{576(8)}{256} = \frac{4608}{256} = \boxed{18.0 \text{ W}}$$

**Independent check.** Setting $R_L = R_s$ in the general expression gives

$$P_{\max} = \frac{V^2R_s}{\left(2R_s\right)^2} = \frac{V^2}{4R_s} = \frac{576}{32} = 18.0 \text{ W} \;\checkmark$$

**Interpretation.** Power delivered to the load is maximized when the load
resistance matches the source resistance. At that operating point the source
dissipates the same 18 W internally, so the efficiency is only 50% — maximum
*power transfer* and maximum *efficiency* are different objectives with
different answers, and confusing them is a real design error.

> **Preview note.** This result is the **maximum power transfer theorem**, and
> Chapter 02-63 develops it properly in the context of AC circuits, where the
> matching condition involves complex impedance and the conjugate. Nothing here
> depends on that. What matters now is the method: an objective function, a
> substitution, a derivative set to zero, and a verification.

---

## 18.7 Related Rates

When two quantities are linked by an equation, their **rates** are linked by the
derivative of that equation with respect to time.

The procedure:

1. **Draw and label.** Identify which quantities vary with time.
2. **Write the relating equation** — geometry, or a physical law.
3. **Eliminate variables** you have no rate information about, using the
   geometry, **before** differentiating.
4. **Differentiate both sides with respect to $t$**, implicitly. Every varying
   quantity contributes its own rate by the chain rule.
5. **Substitute** the instantaneous values and known rates.
6. **Solve** for the unknown rate. Check the sign and the units.

> ---
> **Mentor's Margin**
>
> Two rules that prevent nearly every related-rates error.
>
> **Substitute numbers only at step 5, never before.** If you plug $h = 2$ into
> the volume equation and *then* differentiate, you are differentiating a
> constant and you will get zero. The relating equation must stay symbolic
> through the differentiation. This is the single most common failure in the
> whole topic.
>
> **Signs carry meaning.** A quantity that is decreasing has a negative rate.
> Draining means $\frac{dV}{dt} < 0$. If you enter a drain rate as positive, your
> level will come out rising. State the sign convention explicitly when you write
> the given rates down, and check that your answer's sign matches physical sense.
>
> ---

### Worked Example 9 — Draining Conical Tank

**Given.** A tank shaped as a cone with its apex down has top radius 3.0 m and
depth 4.0 m. Water drains at 0.60 m³/min.

**Find.** The rate at which the water level falls when the depth is 2.0 m.

**Solution.**

**Label.** Let $h$ be the water depth and $r$ the radius of the water surface;
both vary with time. Given $\frac{dV}{dt} = -0.60$ m³/min — negative, because
the volume is decreasing. Find $\frac{dh}{dt}$ when $h = 2.0$ m.

**Relating equation.** The volume of a cone (Handbook, mensuration):

$$V = \frac{1}{3}\pi r^2 h$$

**Eliminate $r$.** We have no information about $\frac{dr}{dt}$, so $r$ must go.
The water cone is similar to the tank cone, so the radius-to-depth ratio is
fixed:

$$\frac{r}{h} = \frac{3.0}{4.0} = 0.75 \implies r = 0.75h$$

Substitute **before** differentiating:

$$V = \frac{1}{3}\pi\left(0.75h\right)^2 h = \frac{1}{3}\pi\left(0.5625\right)h^3 = 0.1875\pi h^3$$

**Differentiate with respect to $t$.** By the chain rule, $\frac{d}{dt}h^3 =
3h^2\frac{dh}{dt}$:

$$\frac{dV}{dt} = 0.5625\pi h^2\frac{dh}{dt}$$

**Substitute** $h = 2.0$ m and $\frac{dV}{dt} = -0.60$ m³/min:

$$-0.60 = 0.5625\pi(4.0)\frac{dh}{dt} = 7.0686\frac{dh}{dt}$$

$$\frac{dh}{dt} = \frac{-0.60}{7.0686} = \boxed{-0.0849 \text{ m/min}}$$

The level is falling at 8.49 cm/min. Negative sign ✓ — the tank is draining.

**Units check.** $\frac{\text{m}^3/\text{min}}{\text{m}^2} = $ m/min ✓

**Structural check.** The coefficient $0.5625\pi h^2$ at $h = 2$ evaluates to
$0.5625\pi(4) = 2.25\pi = 7.0686$ m². And the water surface radius at that depth
is $r = 0.75(2) = 1.5$ m, giving surface area $\pi(1.5)^2 = 2.25\pi = 7.0686$
m² — identical. That is not a coincidence: $\frac{dV}{dh}$ **is** the surface
area, because raising the level by $dh$ adds a thin disc of volume
$(\text{area})\,dh$. Worth remembering as a check on any tank problem.

![FIG-01-18-007: Cross-section of an inverted cone tank, apex at bottom. Full tank dimensions labeled: top radius 3.0 m, depth 4.0 m. Water surface drawn partway up at depth h with surface radius r, the water region shaded. Dashed similar-triangle construction lines show r/h = 3/4. Arrows indicate outflow at the apex labeled dV/dt = −0.60 m³/min and a downward arrow at the surface labeled dh/dt = ?. A callout notes "dV/dh = surface area πr²".](../figures/FIG-01-18-007-conical-tank-related-rates.png)

### Worked Example 10 — Isothermal Compression

**Given.** A gas is compressed at constant temperature, so pressure and volume
satisfy $PV = C$ for a constant $C$. At an instant when $P = 240$ kPa and
$V = 0.500$ m³, the volume is decreasing at 0.020 m³/s.

**Find.** The rate of pressure change at that instant.

**Solution.**

**Relating equation.** $PV = C$, with both $P$ and $V$ varying in time.

**Differentiate with respect to $t$** — the left side needs the **product
rule**:

$$P\frac{dV}{dt} + V\frac{dP}{dt} = 0$$

**Solve** for the unknown rate:

$$\frac{dP}{dt} = -\frac{P}{V}\cdot\frac{dV}{dt}$$

**Substitute** with $\frac{dV}{dt} = -0.020$ m³/s (negative — compressing):

$$\frac{dP}{dt} = -\frac{240}{0.500}(-0.020) = -480(-0.020) = \boxed{+9.60 \text{ kPa/s}}$$

Positive ✓ — compressing a gas raises its pressure, as it must.

**Units check.** $\frac{\text{kPa}}{\text{m}^3}\cdot\frac{\text{m}^3}{\text{s}} =
\frac{\text{kPa}}{\text{s}}$ ✓

**Relative-rate form.** Dividing the differentiated equation through by $PV$
gives a tidier statement:

$$\frac{1}{P}\frac{dP}{dt} + \frac{1}{V}\frac{dV}{dt} = 0 \implies \frac{dP/dt}{P} = -\frac{dV/dt}{V}$$

The fractional rate of pressure rise equals the fractional rate of volume
decrease. Check: $\frac{9.60}{240} = 0.0400$ per second and
$\frac{0.020}{0.500} = 0.0400$ per second ✓ Equal, as required.

---

## 18.8 L'Hôpital's Rule

The shortcut I promised in Chapter 01-16.

> **L'Hôpital's Rule.** If $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)}$ produces
> the indeterminate form $\dfrac{0}{0}$ or $\dfrac{\infty}{\infty}$, and $f$ and
> $g$ are differentiable near $a$ with $g'(x) \ne 0$, then
>
> $$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$
>
> provided the limit on the right exists or is infinite.

Differentiate **numerator and denominator separately**. This is not the quotient
rule and it does not resemble it.

Repeat as necessary: if the new quotient is still indeterminate, apply the rule
again.

> ---
> **Mentor's Margin**
>
> Two disciplines, both non-negotiable.
>
> **Confirm the form before applying the rule.** L'Hôpital's rule applies only
> to $\frac{0}{0}$ and $\frac{\infty}{\infty}$. Applying it to a determinate
> quotient produces a wrong answer confidently. Consider
> $\lim_{x\to 1}\frac{x^2+3}{x+1}$: direct substitution gives $\frac{4}{2} = 2$,
> which is correct and final. Differentiating anyway gives $\frac{2x}{1} = 2$ at
> $x=1$ — coincidentally the same, which is worse than being wrong, because it
> teaches you a bad habit. Try $\lim_{x\to 1}\frac{x^2+3}{x+3}$: the true answer
> is $\frac{4}{4} = 1$, while the illegal differentiation gives $\frac{2}{1} = 2$.
> Wrong.
>
> **Stop as soon as the form becomes determinate.** Applying the rule one extra
> time after the indeterminacy clears will give you a wrong answer. Re-check the
> form after every application.
>
> And keep the Chapter 01-16 techniques. Factoring
> $\frac{x^2-9}{x-3}$ is faster than differentiating it, and for a
> straightforward polynomial ratio it always will be.
>
> ---

### Converting other indeterminate forms

L'Hôpital's rule handles only two forms. The others must be rewritten first.

| Form | Conversion |
|---|---|
| $0 \cdot \infty$ | rewrite one factor as a reciprocal to make $\frac{0}{0}$ or $\frac{\infty}{\infty}$ |
| $\infty - \infty$ | combine over a common denominator |
| $0^0$, $1^\infty$, $\infty^0$ | take logarithms, evaluate, then exponentiate the result |

### Worked Example 11 — Four Applications

**(a)** $\displaystyle\lim_{x\to 0}\frac{\sin 5x}{3x}$

Form: $\frac{0}{0}$ ✓ Differentiate top and bottom separately:

$$= \lim_{x\to 0}\frac{5\cos 5x}{3} = \frac{5(1)}{3} = \boxed{\frac{5}{3}}$$

This is the same result we obtained in Chapter 01-16 by forcing the standard
sine limit — and considerably faster. Agreement confirms both methods ✓

**(b)** $\displaystyle\lim_{x\to 0}\frac{e^{2x} - 1 - 2x}{x^2}$

Form: $\frac{1 - 1 - 0}{0} = \frac{0}{0}$ ✓

$$= \lim_{x\to 0}\frac{2e^{2x} - 2}{2x}$$

Still $\frac{0}{0}$ — apply again:

$$= \lim_{x\to 0}\frac{4e^{2x}}{2} = \frac{4}{2} = \boxed{2}$$

**(c)** $\displaystyle\lim_{x\to\infty}\frac{\ln x}{x}$

Form: $\frac{\infty}{\infty}$ ✓

$$= \lim_{x\to\infty}\frac{1/x}{1} = \lim_{x\to\infty}\frac{1}{x} = \boxed{0}$$

The logarithm grows without bound, but more slowly than $x$ does. This is the
precise statement of a fact worth carrying: **logarithmic growth is slower than
any positive power of $x$.**

**(d)** $\displaystyle\lim_{x\to 0^+}x\ln x$

Form: $0 \cdot (-\infty)$ — not directly eligible. Rewrite the $x$ as a
reciprocal:

$$x\ln x = \frac{\ln x}{1/x}$$

Now the form is $\frac{-\infty}{\infty}$ ✓

$$= \lim_{x\to 0^+}\frac{1/x}{-1/x^2} = \lim_{x\to 0^+}\left(\frac{1}{x}\cdot\left(-x^2\right)\right) = \lim_{x\to 0^+}(-x) = \boxed{0}$$

**Check numerically.** At $x = 0.001$: $x\ln x = 0.001(-6.9078) = -0.0069$ —
small and heading to zero ✓

---

## 18.9 Linear Approximation, Differentials, and Error Propagation

Near a point, a differentiable function is nearly its own tangent line. That is
the content of the whole section, and it has two very different uses.

### Linear approximation

$$\boxed{f(x) \approx f(a) + f'(a)\,(x-a) \qquad \text{for } x \text{ near } a}$$

The right side is exactly the tangent line from Chapter 01-17. Using it in place
of $f$ is called **linearizing** about $a$.

### Differentials

Writing $dx$ for a small change in the input and $dy$ for the resulting
estimated change in the output:

$$\boxed{dy = f'(x)\,dx}$$

$dy$ is the change *along the tangent line*; $\Delta y$ is the true change along
the curve. They differ by an amount that shrinks faster than $dx$ does, which is
why the approximation is good for small increments and degrades for large ones.

![FIG-01-18-008: Curve y = f(x) with a tangent line drawn at the point (a, f(a)). A horizontal increment from a to a + Δx is marked at the bottom. Two vertical segments are drawn at x = a + Δx: a shorter one from the horizontal level f(a) up to the tangent line, labeled dy, and a taller one from f(a) up to the curve, labeled Δy. The small vertical gap between the tangent line and the curve is bracketed and labeled "error, shrinks faster than Δx". A note reads "concave up here, so dy underestimates Δy".](../figures/FIG-01-18-008-differential-vs-actual.png)

### Error propagation — the engineering use

This is what differentials are actually for. If a measured input $x$ carries
uncertainty $dx$, the computed output $y = f(x)$ carries uncertainty

$$dy = f'(x)\,dx$$

and the **relative** uncertainty is

$$\frac{dy}{y} = \frac{f'(x)}{f(x)}\,dx$$

For the power-law relationships that dominate engineering correlations, this
collapses to something you should know by heart. If $y = kx^n$, then from
Chapter 01-17's sensitivity result:

$$\boxed{\frac{dy}{y} = n\,\frac{dx}{x}}$$

**A relative error in the input is multiplied by the exponent.** A 1% error in a
diameter produces a 3% error in a volume, a 2.5% error in a weir flow, a 4.75%
error in a turbulent friction-based head loss. The exponent is the amplification
factor.

> ---
> **Mentor's Margin**
>
> This is the most immediately useful result in the chapter, and it is worth
> internalizing as a reflex rather than a formula.
>
> When someone hands you a measurement and asks for a computed quantity, look at
> the exponent. If the relationship is cubic, your input tolerance is tripled on
> the way out. That determines whether the measurement method is adequate before
> you take a single reading — and it occasionally tells you that the precision
> being requested is impossible with the instrument available.
>
> The reverse reasoning is just as valuable: if a specification requires the
> output to 2% and the exponent is 2.5, you need the input to better than 0.8%.
> That is a purchasing decision derived from a derivative.
>
> ---

### Worked Example 12 — Linear Approximation

**Given.** Estimate $\sqrt[3]{8.06}$ without a root key.

**Solution.**

Take $f(x) = x^{1/3}$ and linearize about $a = 8$, where the cube root is exact.

$$f(8) = 2 \qquad f'(x) = \tfrac13 x^{-2/3} \implies f'(8) = \frac{1}{3(4)} = \frac{1}{12} = 0.08333$$

$$f(8.06) \approx 2 + 0.08333(0.06) = 2 + 0.005000 = \boxed{2.00500}$$

**Compare to the exact value.** $\ln 8.06 = 2.0869135$, so
$8.06^{1/3} = e^{0.6956378} = 2.004987$.

Error: $0.000013$, or about 0.0006% ✓ Excellent, because 0.06 is a small
increment relative to 8.

### Worked Example 13 — Error Propagation in a Sphere

**Given.** A spherical vessel's inside radius is measured as
$r = 25.0 \pm 0.3$ mm.

**(a)** Compute the volume and its absolute uncertainty using differentials.
**(b)** Compute the relative uncertainty two ways.

**Solution.**

**(a)** $V = \frac{4}{3}\pi r^3$, so

$$\frac{dV}{dr} = 4\pi r^2$$

Volume:

$$V = \frac{4}{3}\pi(25.0)^3 = \frac{4}{3}\pi(15{,}625) = 65{,}449.85 \text{ mm}^3$$

Sensitivity at $r = 25.0$ mm:

$$\frac{dV}{dr} = 4\pi(625) = 7853.98 \text{ mm}^2$$

Uncertainty:

$$dV = 7853.98(0.3) = \boxed{2356 \text{ mm}^3}$$

$$V = 65{,}450 \pm 2360 \text{ mm}^3$$

Note the units: $\frac{dV}{dr}$ came out in mm², which is exactly
$\frac{\text{mm}^3}{\text{mm}}$ ✓ And it equals the sphere's surface area
$4\pi r^2$ — the same "derivative of volume is surface area" structure that
appeared in the conical tank.

**(b) Route 1** — divide:

$$\frac{dV}{V} = \frac{2356}{65{,}450} = 0.0360 = 3.60\%$$

**Route 2** — the power-law rule with $n = 3$:

$$\frac{dV}{V} = 3\frac{dr}{r} = 3\left(\frac{0.3}{25.0}\right) = 3(0.0120) = 0.0360 = 3.60\% \;\checkmark$$

**Interpretation.** A radius measured to 1.2% yields a volume known only to
3.6%. If the application needs the volume to 2%, the radius must be measured to
better than 0.67% — that is $\pm 0.17$ mm, and it dictates the instrument.

> **Preview note.** Chapter 01-40 treats uncertainty statistically, where
> independent errors combine in quadrature (as a root-sum-of-squares) rather
> than adding directly, and Chapter 02-73 applies that to instrumentation. The
> differential method here gives the sensitivity of each contribution, which is
> the input the statistical treatment needs. Nothing in this chapter depends on
> that later material.

---

## As the Handbook States It

> **Handbook 10.6, Mathematics section (begins p. 36)** — these applications
> appear within the *Differential Calculus* subsection, approximately
> pp. 44–46.

The Handbook's coverage here is **selective**. It carries the tests and the
rule, and nothing about procedure.

What you will find:

- **Test for a maximum:** $f'(a) = 0$ and $f''(a) < 0$
- **Test for a minimum:** $f'(a) = 0$ and $f''(a) > 0$
- **Test for a point of inflection:** $f''(a) = 0$ with a sign change
- **L'Hôpital's rule**, including the note that it may be applied repeatedly
- Curvature formulas, if a problem needs them
- Mensuration formulas for areas and volumes, in a separate section — you will
  need these constantly for optimization and related rates, so know where they
  are

**What's not in the Handbook — memorize:**

- The definition of a critical point, **including** the "$f'$ undefined" case
- The first derivative test and the sign-chart procedure
- That $f'(c) = 0$ does **not** imply an extremum
- That the second derivative test is **inconclusive** when $f''(c) = 0$, and
  that you must then fall back on the first derivative test
- The Extreme Value Theorem and the closed-interval method — in particular,
  that **endpoints must be evaluated**
- The Mean Value Theorem and Rolle's Theorem
- The complete curve-sketching checklist
- The full optimization procedure: objective, constraint, reduce, domain,
  differentiate, **verify**, answer
- The related-rates procedure, especially *eliminate extra variables before
  differentiating* and *substitute numbers only at the end*
- That L'Hôpital's rule applies **only** to $\frac{0}{0}$ and
  $\frac{\infty}{\infty}$, and how to convert the other forms
- Linear approximation $f(x) \approx f(a) + f'(a)(x-a)$
- The differential relation $dy = f'(x)\,dx$
- The power-law error rule $\frac{dy}{y} = n\frac{dx}{x}$
- That $\frac{dV}{dh}$ for a tank is the liquid surface area — a free check on
  related-rates setups

> ---
> **Mentor's Margin**
>
> The Handbook gives you the two-line max/min test and L'Hôpital's rule. It does
> not give you the setup, and setup is where these problems are won or lost. An
> FE optimization question is roughly 80% translating words into an objective and
> a constraint, 15% algebra, and 5% calculus. The lookup will not help with the
> 80%.
>
> So practise the setup specifically. Work optimization and related-rates
> problems until the first two steps are automatic, and do not skip drawing the
> figure — on a computer-based exam, sketch it on your scratch paper anyway. The
> thirty seconds spent labelling a diagram is the highest-return thirty seconds
> available on these problems.
>
> ---

---

## Where This Goes Wrong

**Assuming $f'(c) = 0$ means an extremum.** $x^3$ at the origin is the
counterexample. Always classify, either with $f''$ or with a sign chart.

**Missing critical points where $f'$ is undefined.** Corners and cusps are
critical points. Solving $f' = 0$ alone finds only some of them.

**Forgetting the endpoints in a closed-interval problem.** The absolute
extremum is frequently at an endpoint, where no derivative test applies. Write
the endpoint values down first.

**Concluding "inflection point" from $f'' = 0$ alone.** The sign must actually
change. $x^4$ has $f''(0) = 0$ and no inflection point.

**Treating an inconclusive second derivative test as an answer.** $f''(c) = 0$
tells you nothing. Fall back to the first derivative test.

**Optimizing the constraint instead of the objective.** Identify both in words
before writing equations. Minimizing the volume of a fixed-volume tank is not a
question.

**Skipping the verification step in optimization.** A critical point may be a
maximum when you wanted a minimum, or neither. On a design problem this is not
an academic slip.

**Substituting numerical values before differentiating in a related-rates
problem.** Plug $h = 2$ into $V$ and you have differentiated a constant. Keep
the relating equation symbolic until step 5.

**Failing to eliminate a variable with no known rate.** In the conical tank, you
must use similar triangles to remove $r$ before differentiating, or you end up
with two unknown rates and one equation.

**Sign errors on rates.** Draining, cooling, compressing, and decelerating are
all negative rates. Declare the sign convention when you list the givens, and
check that your answer's sign is physically sensible.

**Applying L'Hôpital's rule to a determinate form.** Confirm $\frac{0}{0}$ or
$\frac{\infty}{\infty}$ first. Otherwise the rule gives a confidently wrong
answer.

**Applying L'Hôpital's rule to $0\cdot\infty$ or $\infty - \infty$ directly.**
Convert first. Only two forms are eligible.

**Applying L'Hôpital's rule one time too many.** Re-check the form after each
application and stop when it is determinate.

**Using the quotient rule when applying L'Hôpital's rule.** Differentiate the
numerator and the denominator *separately*. The rule does not involve the
quotient rule at all.

**Using linear approximation across a large increment.** The tangent-line
estimate degrades as the increment grows, and it degrades faster where the
curvature is high. Small increments only.

**Forgetting that relative errors are amplified by the exponent.** A 1% radius
error is a 3% volume error. Neglecting this understates uncertainty, sometimes
badly.

---

## Key Terms

| Term | Definition |
|---|---|
| Mean Value Theorem | On $[a,b]$, a continuous and differentiable function has some interior point where the instantaneous rate equals the average rate |
| Rolle's Theorem | Special case of the MVT with $f(a) = f(b)$, forcing $f'(c) = 0$ |
| Critical point | Interior point where $f' = 0$ or $f'$ does not exist |
| Local (relative) extremum | Highest or lowest value in a neighbourhood of a point |
| Absolute (global) extremum | Highest or lowest value on the whole interval or domain |
| First derivative test | Classifying a critical point by the sign change of $f'$ across it |
| Second derivative test | Classifying a critical point by the sign of $f''$ at it; inconclusive if $f'' = 0$ |
| Concave up / down | $f'' > 0$ / $f'' < 0$; slope increasing / decreasing |
| Inflection point | Point where concavity changes sign |
| Extreme Value Theorem | A continuous function on a closed interval attains both an absolute max and an absolute min |
| Closed-interval method | Comparing $f$ at all critical points and both endpoints to find absolute extrema |
| Objective function | The quantity to be maximized or minimized in an optimization problem |
| Constraint | The relationship restricting the variables in an optimization problem |
| Related rates | Linked time rates of change, obtained by differentiating a relating equation with respect to $t$ |
| L'Hôpital's rule | For $0/0$ or $\infty/\infty$, the limit of a quotient equals the limit of the quotient of derivatives |
| Linear approximation | Replacing $f$ near a point by its tangent line |
| Linearization | The process of forming that tangent-line replacement |
| Differential $dy$ | The tangent-line estimate $f'(x)\,dx$ of a small change in $f$ |
| Relative error | $dy/y$; the fractional uncertainty, often expressed as a percentage |
| Error propagation | Determining output uncertainty from input uncertainty using derivatives |

---

## Review Questions

### Conceptual

1. State the Mean Value Theorem and give a physical interpretation using
   distance and speed.
2. Explain why $f'(c) = 0$ does not guarantee a local extremum at $c$. Give an
   example.
3. Give an example of a function with a local minimum at a point where the
   derivative does not exist. Why is that point still a critical point?
4. Both $x^3$ and $x^4$ have $f'(0) = f''(0) = 0$. One has an extremum at the
   origin and one does not. Explain how you would tell them apart and what that
   says about the second derivative test.
5. Why must endpoints be checked in the closed-interval method, when the
   derivative tests do not apply there? Give a physical situation where the
   optimum is at a boundary.
6. In an optimization problem, distinguish the objective function from the
   constraint. What goes wrong if they are swapped?
7. In a related-rates problem, explain why numerical values must not be
   substituted before differentiating. What specifically goes wrong?
8. State the two indeterminate forms to which L'Hôpital's rule applies
   directly, and describe how you would handle $\infty - \infty$.
9. A colleague evaluates $\lim_{x\to 2}\frac{x^2+1}{x+2}$ by differentiating
   numerator and denominator. Is the method valid here? What is the correct
   answer, and what does the illegal method give?
10. Explain, using the power-law error rule, why measuring a diameter to
    tolerance $\pm 1\%$ is inadequate if a volume is needed to $\pm 2\%$.

### Calculation

11. For $f(x) = 2x^3 - 9x^2 + 12x - 3$:
    (a) Find all critical points.
    (b) Determine intervals of increase and decrease.
    (c) Classify each critical point using the second derivative test.
    (d) Find any inflection point.
    (e) State the concavity intervals.

12. Find the absolute maximum and minimum of $f(x) = x^4 - 8x^2 + 3$ on
    $[-1, 3]$. State where each occurs.

13. Find the absolute extrema of $f(x) = \dfrac{x}{x^2+1}$ on $[0, 3]$.

14. For $f(x) = x^{2/3}$, show that $x = 0$ is a critical point even though
    $f'(0)$ does not exist, and classify it.

15. A **closed** cylindrical can must hold 1000 cm³. Find the radius and height
    that minimize total surface area, and the resulting area. Verify it is a
    minimum. Comment on the relationship between the optimal height and
    diameter.

16. A rectangular field is to be fenced on three sides, with the fourth side
    formed by an existing straight wall. If 240 m of fencing is available, find
    the dimensions that maximize the enclosed area, and that maximum area.
    Verify it is a maximum.

17. A 5.0 m ladder leans against a vertical wall. The base is pulled away from
    the wall at 0.40 m/s.
    (a) How fast is the top descending when the base is 3.0 m from the wall?
    (b) What happens to that rate as the base approaches 5.0 m, and what does
    that tell you about the model?

18. Sand falls onto a conical pile at 2.0 m³/min. The pile maintains a shape in
    which its height always equals its base radius.
    (a) How fast is the height increasing when the pile is 3.0 m tall?
    (b) Verify your setup using the "$dV/dh$ equals surface area" check.

19. A spherical balloon is inflated at 40 cm³/s.
    (a) How fast is the radius increasing when $r = 10$ cm?
    (b) How fast is the surface area increasing at that instant?

20. Evaluate using L'Hôpital's rule, confirming the form each time:
    (a) $\displaystyle\lim_{x\to 0}\frac{1-\cos x}{x^2}$
    (b) $\displaystyle\lim_{x\to\infty}\frac{x^2}{e^x}$
    (c) $\displaystyle\lim_{x\to 0}\frac{\tan x - x}{x^3}$
    (d) $\displaystyle\lim_{x\to\infty}\frac{3x^2 - 5x}{7x^2 + 2}$ — and state
    whether the rule was the fastest route.

21. Use linear approximation to estimate each value, then compare to the exact
    result:
    (a) $\sqrt{50}$, linearizing about $a = 49$
    (b) $e^{0.04}$, linearizing about $a = 0$
    (c) $\sin(0.10)$ rad, linearizing about $a = 0$

22. **Engineering application.** Flow over a rectangular weir follows
    $Q = 1.84\,L\,H^{1.5}$ with $Q$ in m³/s, crest length $L$ in m, and head
    $H$ in m. For $L = 2.50$ m and $H = 0.320$ m:
    (a) Compute $Q$.
    (b) Compute $\dfrac{dQ}{dH}$ with units.
    (c) If $H$ is measured to $\pm 0.005$ m, find the absolute and relative
    uncertainty in $Q$.
    (d) Verify the relative uncertainty using the power-law rule.
    (e) To what tolerance must $H$ be measured for $Q$ to be known to $\pm 1\%$?

23. **Engineering application.** The cost of operating a pipeline is modelled as

    $$C(D) = \frac{4800}{D^5} + 320D^2$$

    with $C$ in dollars per year and $D$ the diameter in metres, valid for
    $0.10 \le D \le 1.00$ m. The first term is pumping energy (which falls
    steeply with diameter) and the second is annualized pipe cost.

    (a) Find the diameter that minimizes total cost.
    (b) Compute the minimum annual cost.
    (c) Verify it is a minimum.
    (d) Check the endpoints of the feasible range and confirm the interior point
    is the true optimum.

24. **Engineering application.** A rectangular open channel has cross-sectional
    area $A = 6.0$ m² and wetted perimeter $P = b + 2y$, where $b$ is the bottom
    width and $y$ the depth, with $by = 6.0$. Hydraulic efficiency is maximized
    when the wetted perimeter is minimized.
    (a) Find the $b$ and $y$ that minimize $P$.
    (b) Compute the minimum wetted perimeter.
    (c) Verify it is a minimum.
    (d) Express the result as a ratio $b/y$ and comment.

### Multiple Choice

25. If $f'(c) = 0$ and $f''(c) < 0$, then at $x = c$ the function has a:
    A) Local minimum
    B) Local maximum
    C) Inflection point
    D) Vertical tangent

26. The function $f(x) = x^3 - 12x$ has local extrema at:
    A) $x = 0$ only
    B) $x = \pm 2$
    C) $x = \pm 4$
    D) $x = \pm\sqrt{12}$

27. $f(x) = x^3 - 6x^2 + 5$ is concave up for:
    A) $x < 2$
    B) $x > 2$
    C) $x < 0$
    D) all $x$

28. The absolute maximum of $f(x) = 4x - x^2$ on $[0, 3]$ is:
    A) $0$
    B) $3$
    C) $4$
    D) $8$

29. $\displaystyle\lim_{x\to 0}\frac{e^{3x}-1}{x}$ equals:
    A) $0$
    B) $1$
    C) $3$
    D) Does not exist

30. L'Hôpital's rule may be applied directly to:
    A) $\dfrac{0}{0}$ and $\dfrac{\infty}{\infty}$ only
    B) Any quotient
    C) $0 \cdot \infty$ and $\infty - \infty$
    D) Any limit that is hard to evaluate

31. A cube's edge is measured to within 2%. The percentage uncertainty in its
    computed volume is approximately:
    A) 2%
    B) 4%
    C) 6%
    D) 8%

32. Water drains from a tank so that the volume decreases at a constant rate.
    As the tank empties, if the cross-sectional area at the water surface
    decreases, the rate at which the level falls:
    A) Stays constant
    B) Increases in magnitude
    C) Decreases in magnitude
    D) Becomes zero

---

## Answer Key with Explanations

**1.** If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, there
exists $c \in (a,b)$ with $f'(c) = \frac{f(b)-f(a)}{b-a}$. Physically: if you
travel 180 km in 2 hours, your average speed is 90 km/h, and at some instant
your speedometer read exactly 90 km/h. You cannot stay strictly below the
average and still cover the distance. (§18.1)

**2.** A horizontal tangent can occur on a curve that is still rising or falling
through the point — a flat spot rather than a turning point. The standard
example is $f(x) = x^3$ at $x = 0$: $f'(0) = 0$, but $f' = 3x^2 > 0$ on both
sides, so the function increases straight through. No extremum. (§18.2)

**3.** $f(x) = \lvert x\rvert$ at $x = 0$. The one-sided derivatives are $-1$
and $+1$, so $f'(0)$ does not exist, yet $f(0) = 0$ is the absolute minimum. It
is a critical point because the definition includes points where the derivative
fails to exist, not merely where it is zero. Corners are common in engineering
models — shear diagrams at point loads, saturating control signals — so this
clause is not an edge case. (§18.2)

**4.** Use the first derivative test.

For $x^4$: $f' = 4x^3$ is negative for $x<0$, positive for $x>0$ — sign change
$- \to +$, so a **minimum**.

For $x^3$: $f' = 3x^2$ is positive on both sides — no sign change, so **no
extremum**.

The lesson: $f''(c) = 0$ carries no information. Two functions with identical
inconclusive test results have opposite behaviour, so the second derivative test
must be abandoned rather than interpreted when it returns zero. (§18.3)

**5.** The derivative tests locate *interior* extrema. On a closed interval the
absolute extremum may occur at a boundary where the function is still rising or
falling — the interval simply stops. Physically, a constrained design often
performs best at the edge of its allowable range: maximum flow at the maximum
allowable pump speed, maximum stress at a support, maximum load at the rated
limit. (§18.4)

**6.** The **objective** is the quantity being optimized — what you want made
largest or smallest. The **constraint** is the fixed requirement linking the
variables. If they are swapped you optimize the wrong thing, and typically the
"problem" is vacuous: minimizing the volume of a tank whose volume is specified
as 32 m³ has no content. Write both in plain words before writing equations.
(§18.6)

**7.** Because a substituted value is a constant, and the derivative of a
constant is zero. If you put $h = 2$ into $V = 0.1875\pi h^3$ to get
$V = 4.712$ m³ and then differentiate, you get $\frac{dV}{dt} = 0$ — the
equation has lost its ability to describe change. The relating equation must
remain symbolic through the differentiation, and numbers enter only at the
substitution step. (§18.7)

**8.** Directly eligible: $\frac{0}{0}$ and $\frac{\infty}{\infty}$.

For $\infty - \infty$, combine the terms over a common denominator, which
typically produces $\frac{0}{0}$. For example
$\frac{1}{x-1} - \frac{2}{x^2-1}$ becomes
$\frac{(x+1)-2}{x^2-1} = \frac{x-1}{x^2-1}$, now a $\frac{0}{0}$ form at
$x = 1$ (and in fact resolvable by cancelling, without the rule at all).
(§18.8)

**9.** **Not valid.** Direct substitution gives $\frac{4+1}{2+2} = \frac{5}{4} =
1.25$ — a determinate form and the correct answer.

The illegal differentiation gives $\frac{2x}{1}$, which at $x = 2$ is $4$.
Wrong by a factor of more than three. L'Hôpital's rule is a statement about
indeterminate forms only; applied elsewhere it computes something unrelated to
the limit. (§18.8)

**10.** Volume varies as the cube of diameter, so by the power-law rule
$\frac{dV}{V} = 3\frac{dD}{D}$. A $\pm 1\%$ diameter tolerance produces a
$\pm 3\%$ volume uncertainty, which exceeds the $\pm 2\%$ requirement. To reach
$\pm 2\%$ on the volume, the diameter must be held to
$\frac{2\%}{3} = 0.67\%$. (§18.9)

**11.**

(a) $f'(x) = 6x^2 - 18x + 12 = 6\left(x^2-3x+2\right) = 6(x-1)(x-2)$

$$\boxed{x = 1 \text{ and } x = 2}$$

(b) Test values: $f'(0) = 12 > 0$; $f'(1.5) = 6(0.5)(-0.5) = -1.5 < 0$;
$f'(3) = 6(2)(1) = 12 > 0$.

$$\boxed{\text{Increasing on } (-\infty,1) \text{ and } (2,\infty); \text{ decreasing on } (1,2)}$$

(c) $f''(x) = 12x - 18$

$f''(1) = -6 < 0$ → local **maximum**, $f(1) = 2 - 9 + 12 - 3 = 2$

$f''(2) = +6 > 0$ → local **minimum**, $f(2) = 16 - 36 + 24 - 3 = 1$

$$\boxed{\text{Local max } (1,2); \text{ local min } (2,1)}$$

(d) $f'' = 0$ at $x = 1.5$, and $f''$ changes from negative to positive there ✓

$$f(1.5) = 2(3.375) - 9(2.25) + 18 - 3 = 6.75 - 20.25 + 15 = 1.5$$

$$\boxed{\text{Inflection at } (1.5, 1.5)}$$

(e) $\boxed{\text{Concave down on } (-\infty, 1.5), \text{ up on } (1.5,\infty)}$

Consistency check: the max at $x=1$ lies in the concave-down region ✓, the min
at $x=2$ in the concave-up region ✓, and $x = 1.5$ bisects them ✓ — the cubic
property noted in Worked Example 6.

**12.** $f'(x) = 4x^3 - 16x = 4x\left(x^2-4\right) = 4x(x-2)(x+2)$

Critical points $x = 0, \pm 2$. Only $x = 0$ and $x = 2$ lie in $[-1,3]$;
$x = -2$ is outside.

| $x$ | $f(x) = x^4 - 8x^2 + 3$ | |
|---|---|---|
| $-1$ | $1 - 8 + 3 = -4$ | endpoint |
| $0$ | $3$ | critical |
| $2$ | $16 - 32 + 3 = -13$ | critical |
| $3$ | $81 - 72 + 3 = 12$ | endpoint |

$$\boxed{\text{Absolute max } 12 \text{ at } x = 3; \quad \text{absolute min } -13 \text{ at } x = 2}$$

Note the absolute maximum is at an **endpoint**, where no derivative test would
have found it.

**13.** Quotient rule:

$$f'(x) = \frac{1\left(x^2+1\right) - x(2x)}{\left(x^2+1\right)^2} = \frac{1-x^2}{\left(x^2+1\right)^2}$$

Zero when $x^2 = 1$, so $x = 1$ (taking the root in $[0,3]$).

| $x$ | $f(x) = \frac{x}{x^2+1}$ | |
|---|---|---|
| $0$ | $0$ | endpoint |
| $1$ | $\frac{1}{2} = 0.500$ | critical |
| $3$ | $\frac{3}{10} = 0.300$ | endpoint |

$$\boxed{\text{Absolute max } 0.500 \text{ at } x = 1; \quad \text{absolute min } 0 \text{ at } x = 0}$$

**14.** $f'(x) = \frac{2}{3}x^{-1/3} = \frac{2}{3\sqrt[3]{x}}$, which is
undefined at $x = 0$. By the definition, $x = 0$ is therefore a critical point.

Sign of $f'$: for $x < 0$, $\sqrt[3]{x} < 0$ so $f' < 0$; for $x > 0$, $f' > 0$.

Change $- \to +$, so

$$\boxed{x = 0 \text{ is a local (and absolute) minimum}, \; f(0) = 0}$$

This is a **cusp** — the slopes run to $-\infty$ and $+\infty$ on either side —
one of the four non-differentiable point types from Chapter 01-17.

**15.** Let $r$ be the radius and $h$ the height, in cm.

**Objective:** minimize $A = 2\pi r^2 + 2\pi rh$ (two ends plus the wall).

**Constraint:** $\pi r^2 h = 1000$, so $h = \frac{1000}{\pi r^2}$.

**Reduce:**

$$A(r) = 2\pi r^2 + 2\pi r\left(\frac{1000}{\pi r^2}\right) = 2\pi r^2 + \frac{2000}{r}$$

**Differentiate:**

$$A'(r) = 4\pi r - \frac{2000}{r^2} = 0 \implies 4\pi r^3 = 2000 \implies r^3 = \frac{500}{\pi} = 159.155$$

$$r = 5.4193 \text{ cm}$$

**Verify:** $A''(r) = 4\pi + \frac{4000}{r^3} = 12.566 + \frac{4000}{159.155} =
12.566 + 25.13 = 37.70 > 0$ → **minimum** ✓

**Height:** $r^2 = 29.369$, so

$$h = \frac{1000}{\pi(29.369)} = \frac{1000}{92.267} = 10.839 \text{ cm}$$

**Area:**

$$A = 2\pi(29.369) + \frac{2000}{5.4193} = 184.53 + 369.05 = 553.6 \text{ cm}^2$$

$$\boxed{r = 5.42 \text{ cm}, \; h = 10.84 \text{ cm}, \; A = 554 \text{ cm}^2}$$

**Comment.** $h = 10.839 = 2(5.4193) = 2r$ — the optimal height equals the
**diameter**. The minimum-material closed can is as tall as it is wide, a
proportion independent of the specified volume. (Real cans are not this shape,
because material cost is not the only consideration: seams, stacking, shelf
appearance, and printing area all matter. That gap between the mathematical
optimum and the manufactured product is worth remembering — the objective
function you write down is a model of the real objective, not the real
objective.)

**Constraint check:** $\pi(29.369)(10.839) = 1000.0$ cm³ ✓

**16.** Let $x$ be the length parallel to the wall and $y$ each of the two
perpendicular sides.

**Objective:** maximize $A = xy$.

**Constraint:** fencing on three sides, $x + 2y = 240$.

**Reduce:** $x = 240 - 2y$, so

$$A(y) = (240-2y)y = 240y - 2y^2$$

**Feasible domain:** $0 < y < 120$.

**Differentiate:**

$$A'(y) = 240 - 4y = 0 \implies y = 60 \text{ m}$$

**Verify:** $A'' = -4 < 0$ → **maximum** ✓

$$x = 240 - 120 = 120 \text{ m}$$

$$A = 120(60) = 7200 \text{ m}^2$$

$$\boxed{120 \text{ m} \times 60 \text{ m}; \; A = 7200 \text{ m}^2}$$

**Check the endpoints:** $A(0) = 0$ and $A(120) = 0$, both less than 7200 ✓ The
interior critical point is the true maximum.

**Note the proportion:** the side parallel to the wall is twice each
perpendicular side. Equivalently, exactly half the fencing goes to the single
long side.

**17.** Let $x$ be the base distance from the wall and $y$ the height of the top.

**Relating equation:** $x^2 + y^2 = 25$ (fixed ladder length).

**Differentiate with respect to $t$:**

$$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0 \implies \frac{dy}{dt} = -\frac{x}{y}\cdot\frac{dx}{dt}$$

(a) At $x = 3.0$ m: $y = \sqrt{25-9} = 4.0$ m. With $\frac{dx}{dt} = +0.40$ m/s:

$$\frac{dy}{dt} = -\frac{3.0}{4.0}(0.40) = \boxed{-0.30 \text{ m/s}}$$

The top descends at 0.30 m/s. Negative ✓

(b) As $x \to 5.0$ m, $y \to 0$ and the factor $\frac{x}{y}$ grows without
bound, so $\frac{dy}{dt} \to -\infty$. The model predicts the top falling at
unbounded speed.

That is physically impossible, so the model has broken down. The idealization
that fails is the assumption that the ladder's top stays in contact with the
wall while the base moves at constant speed — near the end the ladder separates
from the wall and simply falls under gravity. This is the same lesson as the
pile-driving model in Chapter 01-15 and the extraneous roots in Chapter 01-07:
the mathematics returns an answer the physics rejects, and recognizing the
domain of validity is part of the engineering.

**18.** With $h = r$:

$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi h^3$$

(a) Differentiate with respect to $t$:

$$\frac{dV}{dt} = \pi h^2\frac{dh}{dt}$$

At $h = 3.0$ m with $\frac{dV}{dt} = +2.0$ m³/min:

$$2.0 = \pi(9.0)\frac{dh}{dt} = 28.274\frac{dh}{dt}$$

$$\frac{dh}{dt} = \frac{2.0}{28.274} = \boxed{0.0707 \text{ m/min}}$$

Positive ✓ — the pile is growing. Units:
$\frac{\text{m}^3/\text{min}}{\text{m}^2} = $ m/min ✓

(b) $\frac{dV}{dh} = \pi h^2$. At $h = 3.0$ m the base radius is also 3.0 m, so
the base area is $\pi(3.0)^2 = 9\pi = 28.274$ m² — identical to $\frac{dV}{dh}$
✓ The check confirms the setup.

**19.** $V = \frac{4}{3}\pi r^3$ and $S = 4\pi r^2$.

(a)

$$\frac{dV}{dt} = 4\pi r^2\frac{dr}{dt}$$

At $r = 10$ cm: $4\pi(100) = 1256.6$ cm².

$$\frac{dr}{dt} = \frac{40}{1256.6} = \boxed{0.0318 \text{ cm/s}}$$

(b)

$$\frac{dS}{dt} = 8\pi r\frac{dr}{dt} = 8\pi(10)(0.0318) = 251.33(0.0318) = \boxed{8.00 \text{ cm}^2/\text{s}}$$

**Elegant check.** Combining the two relations symbolically:

$$\frac{dS}{dt} = 8\pi r\cdot\frac{dV/dt}{4\pi r^2} = \frac{2}{r}\frac{dV}{dt} = \frac{2}{10}(40) = 8.00 \text{ cm}^2/\text{s} \;\checkmark$$

**20.**

(a) Form $\frac{0}{0}$ ✓

$$\lim_{x\to 0}\frac{\sin x}{2x} \quad \text{— still } \tfrac{0}{0}, \text{ apply again}$$

$$\lim_{x\to 0}\frac{\cos x}{2} = \boxed{\frac{1}{2}}$$

(b) Form $\frac{\infty}{\infty}$ ✓

$$\lim_{x\to\infty}\frac{2x}{e^x} \quad \text{— still } \tfrac{\infty}{\infty}$$

$$\lim_{x\to\infty}\frac{2}{e^x} = \boxed{0}$$

Exponential growth beats any polynomial. Worth carrying as a fact.

(c) Form $\frac{0}{0}$ ✓

$$\lim_{x\to 0}\frac{\sec^2 x - 1}{3x^2}$$

By the Pythagorean identity (Chapter 01-11), $\sec^2 x - 1 = \tan^2 x$:

$$= \lim_{x\to 0}\frac{\tan^2 x}{3x^2} = \frac{1}{3}\lim_{x\to 0}\left(\frac{\tan x}{x}\right)^2 = \frac{1}{3}(1)^2 = \boxed{\frac{1}{3}}$$

using $\lim_{x\to 0}\frac{\tan x}{x} = 1$, which follows from the standard sine
limit of Chapter 01-16 since $\frac{\tan x}{x} = \frac{\sin x}{x}\cdot
\frac{1}{\cos x} \to 1 \cdot 1$.

(d) Form $\frac{\infty}{\infty}$ ✓ Applying the rule twice:

$$\lim_{x\to\infty}\frac{6x-5}{14x} \longrightarrow \lim_{x\to\infty}\frac{6}{14} = \boxed{\frac{3}{7}}$$

**Not the fastest route.** The degree-comparison rule from Chapter 01-16 gives
the ratio of leading coefficients, $\frac{3}{7}$, in a single glance. Use the
older tool when it applies.

**21.**

(a) $f(x) = \sqrt{x}$, $a = 49$: $f(49) = 7$, $f'(49) = \frac{1}{2(7)} =
0.071429$

$$\sqrt{50} \approx 7 + 0.071429(1) = 7.07143$$

Exact: $7.0710678$. Error $0.00036$, about 0.005% ✓

(b) $f(x) = e^x$, $a = 0$: $f(0) = 1$, $f'(0) = 1$

$$e^{0.04} \approx 1 + 1(0.04) = 1.04000$$

Exact: $1.0408108$. Error $0.00081$, about 0.078% ✓

(c) $f(x) = \sin x$, $a = 0$: $f(0) = 0$, $f'(0) = \cos 0 = 1$

$$\sin(0.10) \approx 0 + 1(0.10) = 0.10000$$

Exact: $0.0998334$. Error $0.00017$, about 0.17% ✓

Part (c) *is* the small-angle approximation $\sin\theta \approx \theta$ from
Chapter 01-16, now derived as a linearization. The two accounts agree, as they
must — one came from the limit $\frac{\sin\theta}{\theta} \to 1$, the other from
the tangent line at the origin having slope 1.

**22.**

(a) $H^{1.5} = (0.320)^{1.5}$. $\ln 0.320 = -1.139434$, so
$H^{1.5} = e^{1.5(-1.139434)} = e^{-1.709151} = 0.181019$

$$Q = 1.84(2.50)(0.181019) = 4.60(0.181019) = \boxed{0.8327 \text{ m}^3/\text{s}}$$

(b)

$$\frac{dQ}{dH} = 1.84(2.50)(1.5)H^{0.5} = 6.90\sqrt{0.320} = 6.90(0.565685) = \boxed{3.903 \text{ m}^2/\text{s}}$$

Units: $\frac{\text{m}^3/\text{s}}{\text{m}} = $ m²/s ✓

(c)

$$dQ = 3.903(0.005) = \boxed{0.0195 \text{ m}^3/\text{s}}$$

$$\frac{dQ}{Q} = \frac{0.0195}{0.8327} = 0.02343 = \boxed{2.34\%}$$

(d) Power-law rule with $n = 1.5$:

$$\frac{dQ}{Q} = 1.5\frac{dH}{H} = 1.5\left(\frac{0.005}{0.320}\right) = 1.5(0.015625) = 0.02344 = 2.34\% \;\checkmark$$

(e) Require $\frac{dQ}{Q} \le 0.01$:

$$\frac{dH}{H} \le \frac{0.01}{1.5} = 0.006667$$

$$dH \le 0.006667(0.320) = \boxed{0.0021 \text{ m} = 2.1 \text{ mm}}$$

The head must be measured to about $\pm 2$ mm — roughly twice as tight as the
$\pm 5$ mm assumed. That is an instrumentation decision produced entirely by a
derivative.

**23.**

(a) Rewrite as $C(D) = 4800D^{-5} + 320D^2$:

$$C'(D) = -24{,}000D^{-6} + 640D = 0$$

$$640D = \frac{24{,}000}{D^6} \implies D^7 = \frac{24{,}000}{640} = 37.5$$

$$D = 37.5^{1/7}$$

$\ln 37.5 = 3.624341$, divided by 7 gives $0.517763$, and
$e^{0.517763} = 1.6784$.

$$\boxed{D = 1.678 \text{ m}}$$

But the feasible range is $0.10 \le D \le 1.00$ m, and $1.678$ m lies
**outside** it. There is no interior critical point.

(b)–(d) With no interior critical point, the minimum must be at an endpoint.
Since $C'(D) < 0$ throughout the feasible range (the pumping term dominates
below the unconstrained optimum), $C$ is decreasing on $[0.10, 1.00]$ and the
minimum is at the **upper** endpoint $D = 1.00$ m.

$$C(1.00) = \frac{4800}{1} + 320(1) = \boxed{\$5120 \text{ per year}}$$

Confirming the sign of $C'$ at the upper endpoint:

$$C'(1.00) = -24{,}000 + 640 = -23{,}360 < 0 \;\checkmark$$

Still decreasing at $D = 1.00$ m, so cost would continue to fall if larger pipe
were permitted.

For contrast, the lower endpoint:

$$C(0.10) = \frac{4800}{10^{-5}} + 320(0.01) = 480{,}000{,}000 + 3.2 \approx \$4.8\times 10^8$$

— catastrophically expensive, as the $D^{-5}$ term demands.

**This problem is a deliberate trap, and the lesson is the point.** Setting
$C' = 0$ produced a mathematically valid answer that is physically inadmissible.
Had you skipped the domain check and reported $D = 1.68$ m, you would have
specified a pipe outside the allowable range. The feasible-domain and
endpoint-check steps of the optimization procedure exist precisely for this,
and they are the steps most often skipped.

**24.**

(a) **Objective:** minimize $P = b + 2y$.

**Constraint:** $by = 6.0$, so $b = \frac{6.0}{y}$.

**Reduce:**

$$P(y) = \frac{6.0}{y} + 2y$$

**Differentiate:**

$$P'(y) = -\frac{6.0}{y^2} + 2 = 0 \implies y^2 = 3.0 \implies y = \sqrt{3.0} = 1.7321 \text{ m}$$

$$b = \frac{6.0}{1.7321} = 3.4641 \text{ m}$$

$$\boxed{b = 3.464 \text{ m}, \; y = 1.732 \text{ m}}$$

(b)

$$P = 3.4641 + 2(1.7321) = 3.4641 + 3.4641 = \boxed{6.928 \text{ m}}$$

(c) $P''(y) = \frac{12.0}{y^3} = \frac{12.0}{5.196} = 2.309 > 0$ →
**minimum** ✓

(d)

$$\frac{b}{y} = \frac{3.4641}{1.7321} = \boxed{2.00}$$

The most hydraulically efficient rectangular channel is **twice as wide as it is
deep**, independent of the required area — you can confirm that by redoing the
algebra with a symbolic $A$, which gives $y = \sqrt{A/2}$ and $b = 2y$ always.
Equivalently, the depth is half the width, and the two side contributions
$2y$ exactly equal the bottom contribution $b$ at the optimum, which is visible
in the arithmetic of part (b).

This is the same phenomenon as the $h = x/2$ tank and the $h = 2r$ can: optimal
designs emerge as fixed proportions rather than fixed sizes. Chapter 02-59
develops the general best-hydraulic-section results for other channel shapes.

**25. B — Local maximum.** $f' = 0$ gives a horizontal tangent; $f'' < 0$ means
concave down. A flat spot on a concave-down curve is a peak. (§18.3)

**26. B — $x = \pm 2$.** $f'(x) = 3x^2 - 12 = 3(x^2-4) = 0$ gives $x = \pm 2$.
Choice C mistakenly solves $x^2 = 16$; choice D solves $x^2 = 12$, which comes
from dropping the factor of 3 incorrectly. (§18.2)

**27. B — $x > 2$.** $f'' = 6x - 12 > 0$ when $x > 2$. Choice A is the
concave-down region. (§18.3)

**28. C — 4.** $f'(x) = 4 - 2x = 0$ at $x = 2$, giving $f(2) = 8 - 4 = 4$.
Endpoints: $f(0) = 0$ and $f(3) = 12 - 9 = 3$. The largest of $\{0, 4, 3\}$ is
4. Choice D is the value of $4x$ at $x=2$ without subtracting $x^2$. (§18.4)

**29. C — 3.** Form $\frac{0}{0}$ ✓ L'Hôpital gives
$\lim_{x\to 0}\frac{3e^{3x}}{1} = 3$. Choice B is the answer you would get by
dropping the chain rule factor. (§18.8)

**30. A — $\frac{0}{0}$ and $\frac{\infty}{\infty}$ only.** The forms in choice
C must be algebraically converted first. Choices B and D describe how the rule
is frequently misapplied. (§18.8)

**31. C — 6%.** Volume varies as the cube of the edge, so
$\frac{dV}{V} = 3\frac{dx}{x} = 3(2\%) = 6\%$. Choice A ignores the
amplification; choice B is the surface-area answer (exponent 2). (§18.9)

**32. B — Increases in magnitude.** Since $\frac{dV}{dh}$ equals the surface
area $A$, we have $\frac{dh}{dt} = \frac{1}{A}\frac{dV}{dt}$. With
$\frac{dV}{dt}$ constant and $A$ shrinking, the magnitude of $\frac{dh}{dt}$
grows — the level falls faster and faster. This is exactly the conical-tank
behaviour of Worked Example 9, where the surface area shrinks as the tank
empties. (§18.7)

---

## Quick Reference

**Mean Value Theorem** — *not in Handbook*

$$f'(c) = \frac{f(b)-f(a)}{b-a} \quad \text{for some } c \in (a,b)$$

**Critical point** — *not in Handbook*

$$f'(x) = 0 \quad \text{or} \quad f'(x) \text{ undefined}$$

**First derivative test** — *not in Handbook*

| $f'$ across $c$ | At $c$ |
|---|---|
| $+ \to -$ | local max |
| $- \to +$ | local min |
| no change | neither |

**Second derivative test** — *Handbook, Differential Calculus*

| $f''(c)$ with $f'(c)=0$ | At $c$ |
|---|---|
| $< 0$ | local max |
| $> 0$ | local min |
| $= 0$ | inconclusive — use first derivative test |

**Concavity** — *Handbook, Differential Calculus*

$$f'' > 0 \text{ concave up} \qquad f'' < 0 \text{ concave down}$$

$$\text{inflection: } f'' = 0 \textbf{ and } f'' \text{ changes sign}$$

**Closed-interval method** — *not in Handbook*

Compare $f$ at all critical points **and both endpoints**. Largest is the
absolute max, smallest the absolute min.

**Optimization procedure** — *not in Handbook*

objective → constraint → reduce to one variable → state feasible domain →
$f' = 0$ → **verify** → check endpoints → answer with units

**Related-rates procedure** — *not in Handbook*

draw and label → relating equation → eliminate variables with no known rate →
differentiate w.r.t. $t$ → substitute values **last** → check sign and units

$$\frac{dV}{dh} = \text{liquid surface area} \quad \text{(tank check)}$$

**L'Hôpital's rule** — *Handbook, Differential Calculus*

$$\lim\frac{f}{g} = \lim\frac{f'}{g'} \qquad \text{for } \tfrac{0}{0} \text{ or } \tfrac{\infty}{\infty} \text{ only}$$

Convert $0\cdot\infty$ by reciprocal; $\infty-\infty$ by common denominator;
$0^0$, $1^\infty$, $\infty^0$ by logarithms. Re-check the form after each
application.

**Linear approximation** — *not in Handbook*

$$f(x) \approx f(a) + f'(a)(x-a)$$

**Differentials and error propagation** — *not in Handbook*

$$dy = f'(x)\,dx \qquad \frac{dy}{y} = \frac{f'(x)}{f(x)}dx$$

$$\boxed{y = kx^n \implies \frac{dy}{y} = n\frac{dx}{x}}$$

**Growth-rate hierarchy** — *not in Handbook*

$$\ln x \; \ll \; x^p \; \ll \; e^x \qquad \text{as } x \to \infty \; (p > 0)$$

---

## What's Next

Chapter 01-19 turns the process around. Instead of asking "given a function,
what is its rate of change," it asks "given a rate of change, what is the
function" — antiderivatives and the indefinite integral. Every technique in this
chapter runs forward from a function to its derivative; integration runs
backward, and it is how you recover total accumulated quantities from rates.
Deflection from curvature, volume from flow, work from force, charge from
current.

The two operations are inverses, and Chapter 01-21 proves it.