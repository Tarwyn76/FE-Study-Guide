---
chapter: "01-06"
title: "Functions, Graphs, and Transformations"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-006-01, MATH-1B-006-02, MATH-1B-006-03]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-06: Functions, Graphs, and Transformations

> *"Every engineering graph is a compressed argument. A stress-strain curve
> says: here is how this material behaves under load. A frequency response
> says: here is what this circuit does to a signal. You can read the numbers
> off the axes, or you can read the shape — and the shape is worth ten times
> the numbers because it tells you what happens everywhere, not just where
> you measured."*

---

## Before You Start

**Prerequisites:** [01-04 Expressions, Equations, and Inequalities](01-04-expressions-equations-inequalities.md) · [01-05 Exponents, Radicals, and Logarithms](01-05-exponents-radicals-logarithms.md)

**Skip if:** You pass the Tier 1B test-out quiz. But verify you can
recognize a graph's transformation from its equation before skipping — that
skill shows up in every chapter that plots a physical relationship.

**Time:** ~55 min read · ~25 min review questions · ~55 min practice problems

---

## On the Board Today

Apprentice, we're building visual literacy here. Not artistry — the practical
ability to look at an equation and know what its graph looks like, and to
look at a graph and know what equation produced it.

Here's why this matters more than you might think. When you're at hour four
of the FE exam and you see a circuit with an RC time constant, you'll meet
an equation like $V(t) = 24(1 - e^{-t/\tau})$. There's a graph in the
Handbook. If you can see instantly that this is an exponential *rise* toward
24 V (not a decay, not an oscillation), you've verified your setup in two
seconds without calculating anything. When you miss that and set up the wrong
equation, no amount of correct arithmetic recovers it.

That two-second check is function literacy. This chapter builds it.

Three things are happening:

**Function fundamentals** — domain, range, composition, inverse. These are
the vocabulary every downstream chapter uses without pause.

**A library of parent functions** — the basic shapes. Not memorized as
arbitrary facts but understood from the equations that generate them.

**Transformations** — the six operations that shift, stretch, reflect, and
compress any parent function. Master these and you know what every function
in the library looks like when it's been modified.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 6.1 Define a function and distinguish it from a general relation
* 6.2 Determine the domain and range of a function from its equation or
  graph
* 6.3 Evaluate and interpret composite functions
* 6.4 Find the inverse of a function algebraically and graphically
* 6.5 Recognize and sketch the eight parent functions
* 6.6 Apply the six transformation rules to predict graph shapes from
  equations
* 6.7 Interpret engineering graphs using function concepts
* 6.8 Distinguish even and odd functions from equations and graphs

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $f(x)$ | function $f$ evaluated at $x$ | $f$ is the function; $f(x)$ is its value |
| $f \circ g$ | composite function, $f(g(x))$ | read "f of g" |
| $f^{-1}(x)$ | inverse function of $f$ | not $1/f(x)$ |
| $D_f$ | domain of $f$ | set of valid inputs |
| $R_f$ | range of $f$ | set of possible outputs |
| $\mathbb{R}$ | all real numbers | $(-\infty, +\infty)$ |

> ---
> **Mentor's Margin**
>
> The notation $f^{-1}(x)$ is a source of real confusion. It means the
> *inverse function* of $f$ — the function that undoes $f$. It does **not**
> mean $1/f(x)$. The reciprocal of $f$ is written $[f(x)]^{-1}$ or
> $1/f(x)$. When you see $\sin^{-1}(x)$ on a calculator, it means the
> inverse sine function (arcsine), not $1/\sin(x)$. This distinction
> matters enormously in Tier 1C and every chapter involving trig.
>
> ---

---

## 6.1 Functions

A **function** is a rule that assigns to each input exactly one output.

More precisely: $f$ is a function from set $A$ to set $B$ if for every
element $x$ in $A$, there is exactly one element $f(x)$ in $B$.

**The key word is "exactly one."** An input can have only one output. Two
different inputs can share the same output — that's fine. But one input
producing two outputs violates the definition.

### The vertical line test

On a graph: a curve represents a function if and only if **every vertical
line crosses it at most once**.

A circle fails this test — most vertical lines cross it twice. A parabola
opening up passes — every vertical line crosses it at most once.

### Domain and range

**Domain $D_f$:** the set of all valid inputs. What values of $x$ are
allowed?

**Range $R_f$:** the set of all possible outputs. What values can $f(x)$
actually produce?

**Finding the domain:** identify what would make the function undefined or
imaginary:
- Division by zero: exclude values where the denominator is zero
- Even roots of negative numbers: require the radicand $\ge 0$
- Logarithms: require the argument $> 0$
- Physical context: often further restricts the mathematical domain

**Finding the range:** think about what outputs are possible given the domain.
This can require more analysis — we'll develop systematic tools in Chapters
01-16 (limits) and 01-17 (derivatives).

### Worked Example 1 — Domain and Range

**Given.** Find the domain and range of:
(a) $f(x) = \sqrt{4 - x^2}$
(b) $g(x) = \dfrac{x + 1}{x^2 - 9}$
(c) $h(x) = \ln(2x - 6)$

**Solution.**

(a) Even root requires radicand $\ge 0$:
$$4 - x^2 \ge 0 \implies x^2 \le 4 \implies -2 \le x \le 2$$

Domain: $[-2, 2]$.

For range: at $x = 0$, $f = 2$ (maximum). At $x = \pm 2$, $f = 0$
(minimum). The function traces a semicircle above the $x$-axis.

Range: $[0, 2]$.

(b) Denominator $= 0$ when $x^2 - 9 = 0$, i.e., $x = \pm 3$. Exclude both.

Domain: $(-\infty, -3) \cup (-3, 3) \cup (3, +\infty)$.

Range: all real numbers (the function can produce any value by choosing
appropriate $x$).

Range: $\mathbb{R}$.

(c) Logarithm requires argument $> 0$:
$$2x - 6 > 0 \implies x > 3$$

Domain: $(3, +\infty)$.

As $x \to 3^+$, $\ln(2x-6) \to -\infty$. As $x \to \infty$,
$\ln(2x-6) \to +\infty$.

Range: $\mathbb{R}$.

**Check (a) geometrically:** $y = \sqrt{4 - x^2}$ means $y^2 = 4 - x^2$,
so $x^2 + y^2 = 4$ — a circle of radius 2. With $y \ge 0$, it's the upper
semicircle, confirming domain $[-2,2]$ and range $[0,2]$. ✓

---

## 6.2 Composite Functions

**Composition** means the output of one function becomes the input of
another.

$$(f \circ g)(x) = f(g(x))$$

Read: apply $g$ first, then apply $f$ to the result.

Order matters: $(f \circ g)(x) \ne (g \circ f)(x)$ in general.

### Worked Example 2 — Composition

**Given.** $f(x) = x^2 + 1$ and $g(x) = \sqrt{x}$. Find $(f \circ g)(x)$
and $(g \circ f)(x)$. State the domain of each.

**Solution.**

$(f \circ g)(x) = f(g(x)) = f(\sqrt{x}) = (\sqrt{x})^2 + 1 = x + 1$

Domain: $g$ requires $x \ge 0$, so domain of $f \circ g$ is $[0, +\infty)$.

$(g \circ f)(x) = g(f(x)) = g(x^2 + 1) = \sqrt{x^2 + 1}$

Domain: $x^2 + 1 \ge 1 > 0$ for all real $x$, so domain is $\mathbb{R}$.

**Check:** At $x = 4$: $(f \circ g)(4) = 4 + 1 = 5$; and directly:
$g(4) = 2$, $f(2) = 5$. ✓

$(g \circ f)(4) = \sqrt{17}$; and directly: $f(4) = 17$, $g(17) = \sqrt{17}$.✓

> ---
> **Mentor's Margin**
>
> Composition appears explicitly in FE problems whenever one physical
> quantity feeds into another. Temperature depends on position, and
> viscosity depends on temperature — so viscosity as a function of position
> is a composition. The concept is also essential for the chain rule in
> calculus (Chapter 01-17), where you differentiate $f(g(x))$ by working
> outward layer by layer. Getting comfortable with composition now pays off
> in every calculus chapter.
>
> ---

---

## 6.3 Inverse Functions

The **inverse function** $f^{-1}$ undoes $f$:

$$f^{-1}(f(x)) = x \qquad\text{and}\qquad f(f^{-1}(x)) = x$$

**When does an inverse exist?** When $f$ is **one-to-one**: no two inputs
produce the same output. Graphically, the function passes the **horizontal
line test** — every horizontal line crosses the graph at most once.

### Finding an inverse algebraically

1. Write $y = f(x)$
2. Swap $x$ and $y$
3. Solve for $y$
4. Replace $y$ with $f^{-1}(x)$

### Graphical relationship

The graph of $f^{-1}$ is the **reflection of the graph of $f$** across the
line $y = x$. Domains and ranges swap: the domain of $f^{-1}$ is the range
of $f$, and vice versa.

### Worked Example 3 — Finding an Inverse

**Given.** Find $f^{-1}(x)$ for $f(x) = \dfrac{3x - 2}{x + 1}$, $x \ne -1$.
Verify.

**Solution.**

Step 1 — Write $y = f(x)$:

$$y = \frac{3x - 2}{x + 1}$$

Step 2 — Swap $x$ and $y$:

$$x = \frac{3y - 2}{y + 1}$$

Step 3 — Solve for $y$:

$$x(y + 1) = 3y - 2$$
$$xy + x = 3y - 2$$
$$xy - 3y = -2 - x$$
$$y(x - 3) = -(2 + x)$$
$$y = \frac{-(2+x)}{x-3} = \frac{x+2}{3-x}$$

$$\boxed{f^{-1}(x) = \frac{x + 2}{3 - x}, \quad x \ne 3}$$

**Verify:** $f(f^{-1}(x))$ should equal $x$.

Let $u = f^{-1}(x) = (x+2)/(3-x)$.

$$f(u) = \frac{3u - 2}{u + 1} = \frac{3\cdot\frac{x+2}{3-x} - 2}{\frac{x+2}{3-x} + 1}$$

Multiply numerator and denominator by $(3-x)$:

$$= \frac{3(x+2) - 2(3-x)}{(x+2) + (3-x)} = \frac{3x+6-6+2x}{5} = \frac{5x}{5} = x \;\checkmark$$

---

## 6.4 Even and Odd Functions

**Even function:** $f(-x) = f(x)$ for all $x$ in the domain.
- Graph is symmetric about the $y$-axis.
- Examples: $x^2$, $x^4$, $\cos x$, $\lvert x \rvert$

**Odd function:** $f(-x) = -f(x)$ for all $x$ in the domain.
- Graph has 180° rotational symmetry about the origin.
- Examples: $x$, $x^3$, $\sin x$, $\tan x$

Most functions are neither even nor odd. Test by substituting $-x$ and
comparing.

> ---
> **Mentor's Margin**
>
> Even/odd symmetry is not just a classification exercise. In signal
> processing, the Fourier series of an even function contains only cosine
> terms and the series of an odd function contains only sine terms —
> knowing the symmetry halves the work. In structural mechanics, the
> symmetry of a loading case determines which modes are excited. You'll see
> this in Tier 2D (heat transfer with symmetric boundary conditions) and
> Tier 2E (signal analysis). The concept earns its keep.
>
> ---

---

## 6.5 The Parent Functions — Eight Shapes to Know

These are the basic building blocks. Everything else is a transformation of
one of these.

### 1. Linear: $f(x) = x$

Straight line through the origin, slope 1.
Domain: $\mathbb{R}$. Range: $\mathbb{R}$.
Odd function.

General form: $f(x) = mx + b$ — slope $m$, $y$-intercept $b$.
Every proportional physical relationship (Ohm's law, Hooke's law, stress
vs. strain in the elastic range) is linear.

### 2. Quadratic: $f(x) = x^2$

Parabola opening upward, vertex at origin.
Domain: $\mathbb{R}$. Range: $[0, +\infty)$.
Even function.

Any quantity proportional to a squared term: kinetic energy $KE = mv^2/2$,
centripetal force $F = mv^2/r$, drag force $F_D \propto v^2$.

### 3. Cubic: $f(x) = x^3$

S-shaped curve through origin.
Domain: $\mathbb{R}$. Range: $\mathbb{R}$.
Odd function.

Appears in beam deflection (which involves $x^3$ and $x^4$ terms) and in
fluid flow formulations.

### 4. Square root: $f(x) = \sqrt{x}$

Starts at origin, grows slowly, always $\ge 0$.
Domain: $[0, +\infty)$. Range: $[0, +\infty)$.
Neither even nor odd.

Natural frequency $\omega_n \propto \sqrt{k/m}$. Discharge velocity
$v = \sqrt{2gh}$ (Torricelli).

### 5. Absolute value: $f(x) = \lvert x \rvert$

V-shape with vertex at origin.
Domain: $\mathbb{R}$. Range: $[0, +\infty)$.
Even function.

Appears whenever magnitude without direction matters: error magnitude,
displacement from equilibrium.

### 6. Reciprocal: $f(x) = 1/x$

Two-branch hyperbola in quadrants 1 and 3.
Domain: $(-\infty,0) \cup (0,+\infty)$. Range: same.
Vertical asymptote at $x = 0$; horizontal asymptote at $y = 0$.
Odd function.

Resistance in parallel: $1/R_T = \sum 1/R_i$. Capacitance in series:
$1/C_T = \sum 1/C_i$.

### 7. Exponential: $f(x) = e^x$

Always positive, through $(0,1)$, horizontal asymptote at $y = 0$ as
$x \to -\infty$.
Domain: $\mathbb{R}$. Range: $(0, +\infty)$.

Every transient — RC decay, RL circuit, heat transfer — uses $e^x$ or
$e^{-x}$.

### 8. Logarithm: $f(x) = \ln x$

Passes through $(1, 0)$, vertical asymptote at $x = 0$.
Domain: $(0, +\infty)$. Range: $\mathbb{R}$.
Inverse of $e^x$.

Decibels, pH, Richter scale, entropy, half-life time calculations.

---

## 6.6 Transformations — The Six Operations

Given a parent function $f(x)$, these six operations produce all related
functions. Every graph in engineering is either a parent function or a
parent function with some combination of these applied.

I'll state them in table form, then derive each from first principles.

| Transformation | Equation form | Effect on graph |
|---|---|---|
| Vertical shift up $k$ | $f(x) + k$ | Move up $k$ units |
| Vertical shift down $k$ | $f(x) - k$ | Move down $k$ units |
| Horizontal shift right $h$ | $f(x - h)$ | Move right $h$ units |
| Horizontal shift left $h$ | $f(x + h)$ | Move left $h$ units |
| Vertical stretch by $a$ | $a \cdot f(x)$, $a > 1$ | Taller by factor $a$ |
| Vertical compression by $a$ | $a \cdot f(x)$, $0 < a < 1$ | Shorter by factor $a$ |
| Horizontal compression by $b$ | $f(bx)$, $b > 1$ | Narrower by factor $b$ |
| Horizontal stretch by $b$ | $f(bx)$, $0 < b < 1$ | Wider by factor $b$ |
| Reflection across $x$-axis | $-f(x)$ | Flip vertically |
| Reflection across $y$-axis | $f(-x)$ | Flip horizontally |

### The principle behind each

**Vertical shift:** Adding $k$ outside the function adds $k$ to every output.
Every point moves straight up by $k$ (or down if $k < 0$).

**Horizontal shift:** $f(x - h)$ reaches its value at $x = h$ that $f$
reached at $x = 0$. The $-h$ inside shifts right by $h$. The sign is
backwards from what people expect, and this is the most common source of
error.

> ---
> **Mentor's Margin**
>
> The horizontal shift direction is worth spending a minute on. Why does
> $f(x-3)$ shift *right* by 3 instead of left? Because: to get the same
> output that $f$ had at $x = 0$, you now need to plug in $x = 3$, so the
> "action" of the function has moved 3 units to the right. Think of it as:
> where did the reference point go? That's where the graph went.
>
> ---

**Vertical stretch/compression:** Multiplying $f(x)$ by $a > 0$ scales all
outputs. Points on the $x$-axis ($f(x) = 0$) stay fixed; all others move.

**Horizontal stretch/compression:** Replacing $x$ with $bx$ compresses
horizontally when $b > 1$ (the same outputs occur at $x/b$ instead of $x$)
and stretches when $b < 1$.

**Reflections:**
- $-f(x)$: negate every output → flip across $x$-axis
- $f(-x)$: negate every input → flip across $y$-axis

### The general form

$$g(x) = a \cdot f(b(x - h)) + k$$

- $h$: horizontal shift (right if positive)
- $k$: vertical shift (up if positive)
- $a$: vertical scale ($|a| > 1$ stretches, $0 < |a| < 1$ compresses,
  negative $a$ reflects across $x$-axis)
- $b$: horizontal scale ($|b| > 1$ compresses, $0 < |b| < 1$ stretches,
  negative $b$ reflects across $y$-axis)

### Worked Example 4 — Reading a Transformed Function

**Given.** Without calculating values, describe the graph of:

$$g(x) = -3\sqrt{x + 2} + 1$$

**Solution.**

Parent function: $f(x) = \sqrt{x}$.

Identify transformations from $g(x) = -3 \cdot f(x + 2) + 1$:

1. $f(x + 2)$: horizontal shift **left** by 2 (note: $+2$ inside means left)
2. $\times(-3)$: vertical stretch by 3, then **reflect across the $x$-axis**
   (negative factor)
3. $+1$: vertical shift **up** by 1

**Resulting graph:**
- Parent $\sqrt{x}$ starts at origin and grows right. After shift left 2,
  it starts at $(-2, 0)$.
- After reflection and stretch: starts at $(-2, 0)$, curves **downward**
  (instead of upward), three times as steep.
- After shift up 1: starts at $(-2, 1)$, curves down.

**Key points:**
- Starting point (previously at origin): $(-2, 1)$
- At $x = -1$ (1 right of start): $g(-1) = -3\sqrt{1} + 1 = -2$
- At $x = 2$ (4 right of start): $g(2) = -3\sqrt{4} + 1 = -5$

**Domain:** $x + 2 \ge 0 \Rightarrow x \ge -2$, so $[-2, +\infty)$.
**Range:** starts at 1, decreases without bound, so $(-\infty, 1]$.

**Check:** The reflection makes the range go downward from the starting
point, consistent with $(-\infty, 1]$. ✓

### Worked Example 5 — Engineering Context

**Given.** A capacitor charges toward its supply voltage following:

$$V(t) = V_{max}\left(1 - e^{-t/\tau}\right)$$

(a) Identify the parent function and transformations.
(b) State the domain, range, and key values.
(c) Sketch the general shape without computing specific values.

**Solution.**

(a) Parent function: $f(t) = e^t$.

Transformations applied to $e^t$:

- Replace $t$ with $-t/\tau$: horizontal compression by $1/\tau$ and
  reflection across vertical axis
- Negate: $-e^{-t/\tau}$ — reflects across horizontal axis
- Add 1: shifts up by 1, giving $(1 - e^{-t/\tau})$
- Multiply by $V_{max}$: vertical stretch by $V_{max}$

(b) Physical domain: $t \ge 0$ (time starts at 0).

At $t = 0$: $V(0) = V_{max}(1 - e^0) = V_{max}(1-1) = 0$.
As $t \to \infty$: $e^{-t/\tau} \to 0$, so $V \to V_{max}$.
At $t = \tau$: $V = V_{max}(1 - e^{-1}) = 0.632 \, V_{max}$.

Range: $[0, V_{max})$ — asymptotically approaches but never quite reaches
$V_{max}$.

(c) Shape: starts at 0, rises rapidly at first, then curves to approach
$V_{max}$ asymptotically. This is the **saturating exponential** —
the signature shape of all charging/filling/warming processes in first-order
systems.

> ---
> **Mentor's Margin**
>
> Know this shape cold. The decaying exponential $Ae^{-t/\tau}$ and the
> saturating exponential $A(1 - e^{-t/\tau})$ are the two waveforms you will
> encounter most often in electrical, mechanical, and thermal transients.
> They are reflections and shifts of the same parent function. When you read
> a problem and see an RC circuit being charged, picture the saturating form.
> When you see a capacitor discharging, picture the decaying form. Getting
> the shape right before you calculate anything eliminates the most common
> setup error.
>
> ---

---

## 6.7 Piecewise Functions

A **piecewise function** uses different formulas on different parts of its
domain.

$$f(x) = \begin{cases} x^2 & x < 0 \\ 2x + 1 & 0 \le x \le 3 \\ 10 & x > 3 \end{cases}$$

Each piece has its own formula and its own domain restriction. When
evaluating, first determine which piece's domain contains your input, then
apply that formula.

Piecewise functions appear in:
- **Piecewise-linear stress-strain curves** — elastic range (linear),
  plastic range (different slope or nonlinear)
- **Safety factor limits** — one formula for normal operation, another
  for overload
- **Signal clipping** — constant output when signal exceeds a threshold
- **Ramp inputs** — zero before a trigger, linear after

### Worked Example 6 — Evaluating and Graphing a Piecewise Function

**Given.** $f(x) = \begin{cases} -x + 2 & x < 1 \\ x^2 - 1 & x \ge 1
\end{cases}$

Find $f(-2)$, $f(1)$, $f(3)$. Then describe continuity at $x = 1$.

**Solution.**

$f(-2)$: $-2 < 1$, use first piece: $f(-2) = -(-2) + 2 = 4$.

$f(1)$: $1 \ge 1$, use second piece: $f(1) = 1^2 - 1 = 0$.

$f(3)$: $3 \ge 1$, use second piece: $f(3) = 9 - 1 = 8$.

**Continuity at $x = 1$:** evaluate each branch at the boundary and compare.

approaching 1 from below, first piece:
$(-x + 2) = -1 + 2 = 1$

at and above 1, second piece):
$(x^2 - 1) = 1^2 - 1 = 0$.

Since $1 \ne 0$, the graph breaks.

---

## 6.8 Reading Engineering Graphs

This is where the chapter becomes directly practical for exam day.

### The Moody diagram

A log-log plot of friction factor versus Reynolds number for pipe flow
(Chapter 02-44). The log-log scale linearizes power-law relationships —
on log-log paper, $y = kx^n$ plots as a straight line with slope $n$.
Being able to read a log-log graph and extract a slope or an asymptote is a
fundamental skill.

### Frequency response plots (Bode plots)

Log-frequency on the horizontal axis, gain in dB on the vertical axis.
A first-order system rolls off at 20 dB/decade. A second-order system at
40 dB/decade. The shape tells you the system order before you look at a
single number.

### Stress-strain curves

Linear (elastic) region followed by a nonlinear (plastic) region. Two
different slopes, two different functional forms. The yield point is the
transition — a piecewise function with a corner or a smooth curve between
pieces depending on the material.

### What to read from any graph

1. **Domain and range** — what values appear on the axes, and what region
   is shaded or plotted?
2. **Asymptotes** — does the curve approach a boundary without touching?
3. **Symmetry** — even or odd? Any other symmetry axis?
4. **Key points** — intercepts, maxima, minima, inflection points.
5. **Shape family** — which parent function does this most resemble?
6. **Transformations** — what shifts, scales, or reflections from the parent?

> ---
> **Mentor's Margin**
>
> On the exam, when you're given a graph and asked a question about a
> function value, the fastest approach is often to read the value directly
> from the graph rather than computing. Not always possible — sometimes the
> precision isn't there — but sometimes the answer is immediately visible and
> computing wastes time. Build the habit of looking before calculating.
>
> ---

---

## As the Handbook States It

The Handbook's **Mathematics** section (p. 36) contains:

> **Handbook 10.6, pp. 36–38** — *Mathematics / Analytic Geometry and
> Algebra*

The Handbook includes:
- Straight-line equations (slope-intercept, point-slope, general form)
- Definitions of domain and range (implicitly through function notation)
- Basic function forms: linear, quadratic, exponential, logarithmic

The Handbook does **not** include:
- Transformation rules (the six operations)
- Composite or inverse function procedures
- Even/odd function definitions
- Piecewise function notation

Those are entirely in the memorize category.

**Notation note.** The Handbook writes functions using standard $f(x)$
notation throughout the Mathematics section. The notation for composite and
inverse functions uses the same conventions as this guide.

---

## Where This Goes Wrong

**Horizontal shift direction.** $f(x + h)$ shifts *left* by $h$ (not right).
$f(x - h)$ shifts *right* by $h$. The sign inside the argument is backwards
from the shift direction. Verify by finding where the reference point (like
the vertex or zero) moved.

**$f^{-1}(x)$ means the inverse function, not $1/f(x)$.** Two completely
different things. $\sin^{-1}(x)$ is arcsine, not $1/\sin(x) = \csc(x)$.

**Forgetting to check domain when composing.** The domain of $f \circ g$ is
not automatically the domain of $g$. It's the subset of $g$'s domain for
which $g(x)$ falls in $f$'s domain.

**Applying transformations in the wrong order.** Horizontal transformations
happen inside the function argument. Apply in the order: horizontal shift,
then horizontal scale, then vertical scale, then vertical shift.

**Missing the negative domain.** When finding the domain of even roots,
forgetting to include the check for negative radicands. When finding the
domain of logarithms, forgetting the argument must be strictly positive.

**Vertical line test versus horizontal line test.** Vertical line test checks
whether a graph is a function. Horizontal line test checks whether a function
is one-to-one (and therefore has an inverse). These are different tests for
different questions.

**Even/odd test at $x = 0$ only.** Testing $f(-x) = f(x)$ at one point
doesn't prove the function is even. You need to verify the identity for all
$x$ in the domain. Confirm algebraically.

---

## Key Terms

| Term | Definition |
|---|---|
| Function | A rule assigning exactly one output to each input |
| Vertical line test | A graph represents a function iff no vertical line crosses it more than once |
| Domain | The set of all valid inputs |
| Range | The set of all possible outputs |
| Composite function | $(f \circ g)(x) = f(g(x))$; apply $g$ first, then $f$ |
| One-to-one function | A function where every output corresponds to exactly one input |
| Horizontal line test | A function has an inverse iff no horizontal line crosses its graph more than once |
| Inverse function | $f^{-1}$ undoes $f$: $f^{-1}(f(x)) = x$ |
| Vertical shift | Adding/subtracting a constant outside the function |
| Horizontal shift | Adding/subtracting a constant inside the function argument |
| Vertical stretch/compression | Multiplying the function by a constant $\lvert a \rvert > 1$ or $< 1$ |
| Horizontal stretch/compression | Multiplying the argument by a constant $\lvert b \rvert > 1$ or $< 1$ |
| Reflection across $x$-axis | Negating the function: $-f(x)$ |
| Reflection across $y$-axis | Negating the argument: $f(-x)$ |
| Even function | $f(-x) = f(x)$; symmetric about $y$-axis |
| Odd function | $f(-x) = -f(x)$; 180° rotational symmetry about origin |
| Piecewise function | Different formulas applied on different parts of the domain |
| Asymptote | A line the graph approaches but does not reach |
| Parent function | One of the eight basic function shapes from which others are built by transformation |
| Saturating exponential | $A(1 - e^{-t/\tau})$; approaches $A$ asymptotically; shape of charging/warming processes |

---

## Review Questions

### Conceptual

1. State the definition of a function and explain why the vertical line test
   works.
2. Explain the difference between $f^{-1}(x)$ and $[f(x)]^{-1}$.
3. State the horizontal shift rule and explain why $f(x-3)$ shifts right
   (not left) by 3.
4. How does reflecting $f(x)$ across the $x$-axis differ from reflecting
   it across the $y$-axis? Give an equation for each.
5. What is the horizontal line test, and what does it determine?
6. Describe the difference in shape between $Ae^{-t/\tau}$ and
   $A(1 - e^{-t/\tau})$. What physical processes produce each shape?
7. Explain what a piecewise function is and give one engineering example.
8. How do you determine the domain of a function containing a square root?
   A logarithm? A fraction?

### Calculation

9. Find the domain and range of each:
   (a) $f(x) = \dfrac{1}{\sqrt{x-4}}$
   (b) $g(x) = \ln(9 - x^2)$
   (c) $h(x) = \dfrac{x-2}{x^2 + x - 6}$

10. Given $f(x) = 2x - 1$ and $g(x) = x^2 + 3$, find:
    (a) $(f \circ g)(2)$
    (b) $(g \circ f)(2)$
    (c) $(f \circ g)(x)$ as a simplified expression
    (d) $(g \circ f)(x)$ as a simplified expression

11. Find $f^{-1}(x)$ for each and state the domain restriction:
    (a) $f(x) = 5x - 3$
    (b) $f(x) = x^2 - 4$, for $x \ge 0$
    (c) $f(x) = e^{2x}$
    (d) $f(x) = \ln(x - 1)$

12. Determine whether each function is even, odd, or neither:
    (a) $f(x) = x^4 - 3x^2 + 1$
    (b) $g(x) = x^3 - 5x$
    (c) $h(x) = x^2 + x$
    (d) $p(x) = \dfrac{x}{x^2 + 1}$

13. Describe the transformations applied to the parent function, then state
    the domain and range:
    (a) $f(x) = (x - 3)^2 + 4$
    (b) $g(x) = -2\lvert x + 1 \rvert - 3$
    (c) $h(x) = 3e^{-2x}$
    (d) $p(x) = \ln(x + 5) - 2$

14. Write the equation for each described transformation of the given parent:
    (a) $f(x) = x^2$: shift right 4, shift down 3
    (b) $f(x) = \sqrt{x}$: reflect across $x$-axis, stretch vertically by 2,
        shift left 1
    (c) $f(x) = 1/x$: compress horizontally by factor 3, shift up 5
    (d) $f(x) = e^x$: reflect across $y$-axis, shift up 2

15. For $f(x) = \begin{cases} x+3 & x < 0 \\ x^2 & 0 \le x \le 2 \\
    3 & x > 2 \end{cases}$, find $f(-3)$, $f(0)$, $f(2)$, $f(4)$.
    Check continuity at $x = 0$ and $x = 2$.

16. **Engineering application.** A material's stress-strain behavior is:

    $$\sigma(x) = \begin{cases} 200x & 0 \le x \le 0.001 \\
    0.2 + 50(x - 0.001) & 0.001 < x \le 0.01 \end{cases}$$

    where $\sigma$ is stress in GPa and $x$ is strain (dimensionless).

    (a) What is the stress at a strain of 0.0005?
    (b) At a strain of 0.005?
    (c) What is the elastic modulus (slope of the first piece) in GPa?
    (d) At what strain does the material yield (transition between pieces)?

17. **Engineering application.** An RC circuit charges as
    $V(t) = 12(1 - e^{-t/0.03})$ volts.

    (a) What is the supply voltage?
    (b) What is the time constant?
    (c) What transformations were applied to $f(t) = e^t$ to produce this?
    (d) At what time is $V = 10$ V? (Solve exactly, then numerically.)

### Multiple Choice

18. The domain of $f(x) = \sqrt{x^2 - 16}$ is:
    A) $[-4, 4]$
    B) $(-4, 4)$
    C) $(-\infty, -4] \cup [4, +\infty)$
    D) $(-\infty, +\infty)$

19. If $f(x) = x + 2$ and $g(x) = x^2$, then $(f \circ g)(3)$ equals:
    A) $11$
    B) $25$
    C) $9$
    D) $7$

20. The graph of $f(x+3) - 2$ is the graph of $f(x)$ shifted:
    A) Right 3, up 2
    B) Left 3, down 2
    C) Right 3, down 2
    D) Left 3, up 2

21. $f(x) = x^5 - 3x^3 + x$ is:
    A) Even
    B) Odd
    C) Neither even nor odd
    D) Both even and odd

22. Which parent function has a vertical asymptote at $x = 0$ and a
    horizontal asymptote at $y = 0$?
    A) $f(x) = x^2$
    B) $f(x) = \sqrt{x}$
    C) $f(x) = 1/x$
    D) $f(x) = \ln x$

23. The function $g(x) = -f(2x)$ applies which transformations to $f$?
    A) Reflect across $x$-axis; stretch horizontally by 2
    B) Reflect across $x$-axis; compress horizontally by 2
    C) Reflect across $y$-axis; stretch horizontally by 2
    D) Reflect across $y$-axis; compress horizontally by 2

24. The range of $f(x) = 3 - e^x$ is:
    A) $(0, +\infty)$
    B) $(-\infty, 3)$
    C) $(-\infty, 3]$
    D) $\mathbb{R}$

---

## Answer Key with Explanations

**1.** A function assigns exactly one output to each input in the domain. The
vertical line test works because a vertical line at any $x$ value asks: "how
many outputs does this input produce?" If the line crosses the graph twice,
the same $x$ produces two $y$-values — violating the definition. (§6.1)

**2.** $f^{-1}(x)$ is the **inverse function** of $f$: it undoes $f$, so
$f^{-1}(f(x)) = x$. For example, if $f(x) = e^x$, then $f^{-1}(x) = \ln x$.
$[f(x)]^{-1}$ is the **reciprocal** of $f$'s output: $1/f(x)$. For the same
example, $[f(x)]^{-1} = e^{-x}$. These are completely different functions.
(§6.3)

**3.** $f(x-3)$ produces the value that $f$ would have at $x = 0$ when $x =
3$. In other words, the reference point of $f$ has moved 3 units to the
right. The $-3$ inside subtracts from the input, so the function's "action"
is delayed until $x$ reaches 3. For $f(x+h)$: to get the output that $f$
produces at $x = 0$, set $x + h = 0$, so $x = -h$ — the shift is left by
$h$. (§6.6)

**4.** Reflecting across the $x$-axis negates every output: $-f(x)$. Every
point moves straight up or down. The $x$-intercepts stay fixed. Reflecting
across the $y$-axis negates every input: $f(-x)$. Every point moves left
or right. The $y$-intercept stays fixed. (§6.6)

**5.** The horizontal line test determines whether a function is one-to-one.
A function is one-to-one iff no horizontal line crosses its graph more than
once. This matters because a function has an inverse only if it's one-to-one.
(§6.3)

**6.** $Ae^{-t/\tau}$ starts at $A$ when $t = 0$ and **decays toward zero**
asymptotically — the shape of capacitor discharge, cooling, radioactive
decay, step-down response. $A(1 - e^{-t/\tau})$ starts at 0 and **rises
toward $A$** asymptotically — the shape of capacitor charging, warming,
step-up response. One is the reflection and shift of the other via
$A - Ae^{-t/\tau} = A(1 - e^{-t/\tau})$. (§6.6, Worked Example 5)

**7.** A piecewise function uses different formulas on different subsets of
its domain. Engineering example: the elastic-plastic stress-strain curve —
linear (Hooke's law) for strain below yield, nonlinear or constant above
yield. (§6.7)

**8.** Square root: set radicand $\ge 0$ and solve. Logarithm: set argument
$> 0$ (strict) and solve. Fraction: set denominator $\ne 0$ and solve.
Combine all restrictions for a function involving multiple such expressions.
(§6.1)

**9.**

(a) Need $x - 4 > 0$ (strict, because of the denominator): $x > 4$.
Domain: $(4, +\infty)$.
As $x \to 4^+$, $f \to +\infty$. As $x \to \infty$, $f \to 0^+$.
Range: $(0, +\infty)$.

(b) Need $9 - x^2 > 0$: $x^2 < 9$, so $-3 < x < 3$.
Domain: $(-3, 3)$.
At $x = 0$: $\ln 9 \approx 2.2$ (max). As $x \to \pm 3$: $\ln(0^+) \to
-\infty$.
Range: $(-\infty, \ln 9]$.

(c) $x^2 + x - 6 = (x+3)(x-2) = 0$ at $x = -3$ or $x = 2$. Also note
$x = 2$ makes the numerator $(2-2) = 0$, so $h(2) = 0/0$. Exclude $x = -3$ and
$x = 2$.
Domain: $(-\infty, -3) \cup (-3, 2) \cup (2, +\infty)$.
Range: $\mathbb{R} exculding 0 and \setminus \{1/5\}$

**10.**

(a) $(f \circ g)(2) = f(g(2)) = f(4+3) = f(7) = 2(7)-1 = \boxed{13}$

(b) $(g \circ f)(2) = g(f(2)) = g(3) = 9+3 = \boxed{12}$

(c) $(f \circ g)(x) = f(x^2+3) = 2(x^2+3) - 1 = \boxed{2x^2 + 5}$

(d) $(g \circ f)(x) = g(2x-1) = (2x-1)^2 + 3 = 4x^2 - 4x + 1 + 3 =
\boxed{4x^2 - 4x + 4}$

**11.**

(a) $y = 5x - 3 \Rightarrow x = 5y - 3 \Rightarrow y = (x+3)/5$.
$f^{-1}(x) = (x+3)/5$. Domain: $\mathbb{R}$.

(b) $y = x^2 - 4$, $x \ge 0 \Rightarrow x = y + 4 \Rightarrow x = \sqrt{y+4}$
(positive root since $x \ge 0$). $f^{-1}(x) = \sqrt{x+4}$.
Domain: $x \ge -4$, i.e., $[-4, +\infty)$.

(c) $y = e^{2x} \Rightarrow \ln y = 2x \Rightarrow x = \frac{\ln y}{2}$.
$f^{-1}(x) = \frac{\ln x}{2}$.
Domain: $x > 0$.

(d) $y = \ln(x-1) \Rightarrow e^y = x-1 \Rightarrow x = e^y + 1$.
$f^{-1}(x) = e^x + 1$.
Domain: $\mathbb{R}$ (all real $x$ are valid inputs to $e^x$).

**12.**

(a) $f(-x) = (-x)^4 - 3(-x)^2 + 1 = x^4 - 3x^2 + 1 = f(x)$. **Even.**

(b) $g(-x) = (-x)^3 - 5(-x) = -x^3 + 5x = -(x^3 - 5x) = -g(x)$. **Odd.**

(c) $h(-x) = (-x)^2 + (-x) = x^2 - x$. This equals $h(x) = x^2 + x$ only
if $-x = x$, i.e., $x = 0$. Not true for all $x$. Also $-h(x) = -x^2 - x
\ne x^2 - x$. **Neither.**

(d) $p(-x) = \frac{-x}{(-x)^2 + 1} = \frac{-x}{x^2+1} = -p(x)$. **Odd.**

**13.**

(a) $f(x) = (x-3)^2 + 4$: parent $x^2$, shift right 3, shift up 4.
Domain: $\mathbb{R}$. Range: $[4, +\infty)$ (vertex at $(3,4)$).

(b) $g(x) = -2|x+1| - 3$: parent $|x|$, shift left 1, stretch vertically
by 2, reflect across $x$-axis, shift down 3.
Domain: $\mathbb{R}$. Range: $(-\infty, -3]$ (vertex at $(-1, -3)$,
opening downward).

(c) $h(x) = 3e^{-2x}$: parent $e^x$, reflect across $y$-axis (making
$e^{-x}$), compress horizontally by 2 (making $e^{-2x}$), stretch
vertically by 3.
Domain: $\mathbb{R}$. Range: $(0, +\infty)$.

(d) $p(x) = \ln(x+5) - 2$: parent $\ln x$, shift left 5, shift down 2.
Domain: $x + 5 > 0 \Rightarrow x > -5$, so $(-5, +\infty)$.
Range: $\mathbb{R}$.

**14.**

(a) $(x-4)^2 - 3$

(b) $-2\sqrt{x+1}$

(c) $1/(3x) + 5$.

(d) $e^{-x} + 2$

**15.**

$f(-3)$: $-3 < 0$, first piece: $-3 + 3 = \boxed{0}$

$f(0)$: $0 \le 0 \le 2$, second piece: $0^2 = \boxed{0}$

$f(2)$: $0 \le 2 \le 2$, second piece: $2^2 = \boxed{4}$

$f(4)$: $4 > 2$, third piece: $\boxed{3}$

**Continuity at $x = 0$:**
From the left: $\(x+3) = 0+3 = 3, f(0)=3$.
From the right: $0^2 = 0$, $f(0) = 0$.
$3 \ne 0$.

**Continuity at $x = 2$:**
From the left: $ x^2 = 4$, $f(2) = 4$.
From the right $3 = 3$.
$4 \ne 3$.

**16.**

(a) Strain $= 0.0005 \le 0.001$: first piece.
$\sigma = 200(0.0005) = \boxed{0.1 \text{ GPa} = 100 \text{ MPa}}$

(b) Strain $= 0.005 > 0.001$: second piece.
$\sigma = 0.2 + 50(0.005 - 0.001) = 0.2 + 50(0.004) = 0.2 + 0.2 =
\boxed{0.4 \text{ GPa}}$

(c) Elastic modulus is the slope of the first piece: $\boxed{200 \text{ GPa}}$

(d) The transition occurs at strain $= \boxed{0.001}$.

*Check:* The two pieces at the boundary: first gives $200(0.001) = 0.2$
GPa; second gives $0.2 + 50(0) = 0.2$ GPa. They agree — the function is
continuous at the yield point. ✓

**17.**

(a) Supply voltage = $\boxed{12 \text{ V}}$ (the asymptotic limit)

(b) Time constant $\tau = \boxed{0.03 \text{ s} = 30 \text{ ms}}$

(c) Start with $e^t$:
- Replace $t$ with $-t/0.03$: reflect across vertical axis, compress
  horizontally
- Negate: $-e^{-t/0.03}$ — reflect across horizontal axis
- Add 1: shift up 1 → $(1 - e^{-t/0.03})$
- Multiply by 12: stretch vertically by 12

(d) $10 = 12(1 - e^{-t/0.03})$

$\dfrac{10}{12} = 1 - e^{-t/0.03}$

$e^{-t/0.03} = 1 - \dfrac{10}{12} = \dfrac{1}{6}$

$-\dfrac{t}{0.03} = \ln\!\left(\dfrac{1}{6}\right) = -\ln 6$

$t = 0.03\ln 6 = 0.03(1.7918) = \boxed{0.0538 \text{ s} \approx 53.8 \text{ ms}}$

Check: $V(0.0538) = 12(1 - e^{-1.7918}) = 12(1 - 1/6) = 12(5/6) = 10$ V ✓

**18. C — $(-\infty, -4] \cup [4, +\infty)$.** Need $x^2 - 16 \ge 0$, so
$x^2 \ge 16$, meaning $|x| \ge 4$. (A) is the wrong region — it's where
the radicand is *negative*. (§6.1)

**19. A — 11.** $(f \circ g)(3) = f(g(3)) = f(9) = 9 + 2 = 11$. Apply $g$
first (square), then $f$ (add 2). (B) would be $(g \circ f)(3) = g(5) = 25$.
(§6.2)

**20. B — Left 3, down 2.** $f(x+3)$ shifts left 3 (positive inside means
left). Subtracting 2 outside shifts down 2. (§6.6)

**21. B — Odd.** $f(-x) = (-x)^5 - 3(-x)^3 + (-x) = -x^5 + 3x^3 - x =
-(x^5 - 3x^3 + x) = -f(x)$. All terms have odd powers, so the function is
odd. (§6.4)

**22. C — $f(x) = 1/x$.** The reciprocal function has a vertical asymptote
at $x = 0$ (denominator zero) and a horizontal asymptote at $y = 0$ (output
approaches zero as $x \to \pm\infty$). $\ln x$ has a vertical asymptote at
$x = 0$ but no horizontal asymptote. (§6.5)

**23. B — Reflect across $x$-axis; compress horizontally by 2.** The
negative outside negates outputs = reflects across $x$-axis. The $2x$
inside means $f$ evaluated at $2x$, which compresses the graph horizontally
by factor 2 (same values occur at half the $x$-distance). (§6.6)

**24. B — $(-\infty, 3)$.** $e^x > 0$ for all $x$, so $-e^x < 0$, giving
$3 - e^x < 3$. The output approaches 3 asymptotically as $x \to -\infty$
but never reaches it — hence open parenthesis at 3. (C) would be wrong
because 3 is not achievable. (§6.5, §6.6)

---

## Quick Reference

**Function fundamentals**

- Exactly one output per input
- Domain: valid inputs · Range: possible outputs
- Vertical line test: function? · Horizontal line test: one-to-one?

**Composition:** $(f \circ g)(x) = f(g(x))$ — apply $g$ first

**Inverse:** swap $x$ and $y$, solve for $y$. Domains and ranges swap.
$f^{-1}(x) \ne 1/f(x)$.

**Even/odd:** $f(-x) = f(x)$ even; $f(-x) = -f(x)$ odd

**Parent functions**

| Name | Equation | Key shape feature |
|---|---|---|
| Linear | $x$ | Line through origin |
| Quadratic | $x^2$ | Upward parabola |
| Cubic | $x^3$ | S-curve |
| Square root | $\sqrt{x}$ | Right half, grows slowly |
| Absolute value | $\|x\|$ | V-shape |
| Reciprocal | $1/x$ | Two-branch hyperbola |
| Exponential | $e^x$ | Always positive, asymptote $y=0$ left |
| Logarithm | $\ln x$ | Asymptote $x=0$, passes $(1,0)$ |

**Transformations — $g(x) = a \cdot f(b(x-h)) + k$**

| Parameter | Effect |
|---|---|
| $+k$ outside | up $k$ |
| $-k$ outside | down $k$ |
| $x - h$ inside | right $h$ |
| $x + h$ inside | left $h$ |
| $\lvert a \rvert > 1$ | vertical stretch |
| $0 < \lvert a \rvert < 1$ | vertical compression |
| $-a$ | reflect across $x$-axis |
| $b > 1$ | horizontal compression |
| $0 < b < 1$ | horizontal stretch |
| $f(-x)$ | reflect across $y$-axis |

**Key engineering shapes**

$$Ae^{-t/\tau}: \text{decay from } A \text{ toward 0}$$
$$A(1-e^{-t/\tau}): \text{rise from 0 toward } A$$

**Not in the Handbook — memorize**

Transformation rules · composite/inverse procedures · even/odd definitions ·
piecewise notation · parent function shapes

---

## What's Next

Apprentice, you now have a visual language for functions. Every equation
you'll encounter from here on has a shape, and you can read it.

In **Chapter 01-07: Polynomials and Their Roots**, we add the largest single
family of functions in engineering mathematics. Every algebraic equation that
arises from equilibrium, energy balance, or geometric constraint is a
polynomial at its core. The quadratic formula is in there, along with the
rational root theorem and synthetic division — tools for finding when a
polynomial equals zero, which is the fundamental question in structural
failure analysis, circuit frequency response, and control system stability.

Bring the Handbook to page 37. We're about to use it.

See you there.

— Your Mentor
