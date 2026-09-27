---
chapter: "01-17"
title: "The Derivative"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-017-01, MATH-1C-017-02, MATH-1C-017-03, MATH-1C-017-04, MATH-1C-017-05]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-17: The Derivative

> *"A derivative is a rate. Nothing more mysterious than that. How fast the
> level rises, how sharply the beam bends, how steeply the pressure drops for
> one more litre per second. Engineering runs on rates, because the question
> is almost never 'what is the value' — it is 'what happens if I change
> something.' The derivative is the answer to that question, and this chapter
> is where you learn to compute it without thinking about it."*

---

## Before You Start

**Prerequisites:** [01-05 Exponents, Radicals, and Logarithms](01-05-exponents-radicals-logarithms.md) · [01-06 Functions, Graphs, and Transformations](01-06-functions-graphs-transformations.md) · [01-07 Polynomials and Their Roots](01-07-polynomials-roots.md) · [01-11 Trigonometry](01-11-trigonometry.md) · [01-16 Limits and Continuity](01-16-limits-continuity.md)

**Skip if:** You pass the Tier 1C test-out quiz. Verify you can apply the
product, quotient, and chain rules to a composite expression, differentiate
implicitly, and state the derivatives of all six trig functions before
skipping. The chain rule buried two layers deep is the most common rust point.

**Time:** ~70 min read · ~30 min review questions · ~70 min practice problems

---

## On the Board Today

Apprentice, at the end of Chapter 01-16 I pointed at a particular limit and
told you it had a name. Here it is again:

$$\lim_{h\to 0}\frac{f(a+h) - f(a)}{h}$$

We evaluated one of these by combining fractions and got $-\frac{1}{16}$. What
we actually computed, without saying so, was the derivative of $\frac{1}{x}$
at $x = 4$. Every derivative in this chapter — every one in the whole guide —
is a limit of that form. The rules we are about to build are not new
mathematics. They are the results of doing that limit once, in general, so
that you never have to do it again.

Here is why this matters more than any single formula.

The derivative is a **rate of change**, and it is the quantity engineering
actually asks about. Not "what is the deflection" but "how fast is the
deflection growing as I move along the beam." Not "what is the pressure drop"
but "how much more pressure drop do I pay for one more litre per second." Not
"what is the concentration" but "how fast is it falling." Design work is
almost entirely about sensitivity — how the output responds when you nudge the
input — and sensitivity is a derivative.

The derivative also has a clean geometric meaning: it is the **slope of the
tangent line**. That picture is worth carrying, because it makes the algebra
intuitive. A large derivative means a steep curve. A zero derivative means a
flat spot, which is where maxima and minima live. A negative derivative means
the function is falling. You can read a great deal off a graph once you know
what the derivative is looking at.

We will build the definition, establish the geometric and physical readings,
then develop the rules: power, product, quotient, chain. Then the derivatives
of the trig, exponential, and logarithmic functions. Then implicit
differentiation and higher-order derivatives.

By the end you should be able to differentiate essentially anything the FE
puts in front of you, mechanically and quickly. The applications — finding
maxima, related rates, curve sketching — are Chapter 01-18. This chapter is
about building the tool.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 17.1 Write the difference quotient for a function and use it to compute a
  derivative from the definition
* 17.2 Interpret the derivative as the slope of the tangent line and find
  equations of tangent and normal lines
* 17.3 Interpret the derivative as a rate of change and determine its units
* 17.4 Use Leibniz, Lagrange, and dot notation interchangeably
* 17.5 State the relationship between differentiability and continuity and
  identify points where a function fails to be differentiable
* 17.6 Apply the constant, power, constant-multiple, and sum rules
* 17.7 Apply the product rule
* 17.8 Apply the quotient rule
* 17.9 Apply the chain rule, including to nested compositions
* 17.10 Differentiate all six trigonometric functions and the three principal
  inverse trigonometric functions
* 17.11 Differentiate exponential and logarithmic functions with any base
* 17.12 Compute higher-order derivatives and interpret the second derivative
* 17.13 Differentiate implicitly and use the technique to obtain derivatives of
  inverse functions

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $f'(x)$ | derivative of $f$ with respect to $x$ | Lagrange notation |
| $\dfrac{dy}{dx}$ | derivative of $y$ with respect to $x$ | Leibniz notation |
| $\dfrac{d}{dx}[\;\cdot\;]$ | "take the derivative with respect to $x$ of" | operator form |
| $\dot{y}$, $\ddot{y}$ | first and second derivative **with respect to time** | Newton/dot notation |
| $h$ or $\Delta x$ | the increment in the independent variable | shrinks to zero in the limit |
| $\Delta y$ | the corresponding increment in $y$ | $= f(x+h) - f(x)$ |
| $f''(x)$, $\dfrac{d^2y}{dx^2}$ | second derivative | — |
| $f^{(n)}(x)$, $\dfrac{d^ny}{dx^n}$ | $n$th derivative | primes get unreadable past three |
| $u$, $v$ | intermediate functions in product, quotient, chain rules | — |
| $m_{\text{tan}}$, $m_{\text{norm}}$ | slopes of the tangent and normal lines | — |

> ---
> **Mentor's Margin**
>
> The three notations are not competing conventions to pick between — each one
> is better at a different job, and you need all three.
>
> Lagrange's $f'(x)$ is compact and reads well when you are stating rules:
> $(uv)' = u'v + uv'$ is easier to hold in your head than the Leibniz version.
>
> Leibniz's $\frac{dy}{dx}$ carries the variables with it, which is why every
> engineering equation you will ever meet uses it. It tells you what is being
> differentiated with respect to what, and it makes the units obvious:
> $\frac{dh}{dt}$ in metres per second, $\frac{dP}{dQ}$ in kPa per litre per
> second. When a beam equation reads $EI\frac{d^2v}{dx^2} = M$, the notation
> is doing real work — it tells you the differentiation is along the beam, not
> in time.
>
> Newton's $\dot{y}$ means specifically the time derivative, and it appears
> throughout dynamics and control. When you see a dot, the variable is time.
>
> ---

---

## 17.1 The Difference Quotient

Start with the honest question: what is the slope of a curve?

For a straight line the answer is easy and you have had it since Chapter
01-09: rise over run, the same everywhere. For a curve the slope changes from
point to point, so "the slope of the curve" is not a well-posed question. "The
slope of the curve **at a point**" is.

Take a point $(a, f(a))$ on the curve, and a second point a distance $h$ away
at $(a+h, f(a+h))$. The line through the two is a **secant line**, and its
slope is straightforward:

$$m_{\text{sec}} = \frac{f(a+h) - f(a)}{h} = \frac{\Delta y}{\Delta x}$$

This expression is called the **difference quotient**. It is an *average* rate
of change over the interval from $a$ to $a+h$.

Now shrink $h$. The second point slides toward the first, the secant line
pivots, and the average rate of change over a shrinking interval becomes the
instantaneous rate of change at the point. You cannot set $h = 0$ — that gives
$\frac{0}{0}$, and Chapter 01-16 taught you exactly what to do with that. Take
the limit.

$$\boxed{f'(a) = \lim_{h\to 0}\frac{f(a+h) - f(a)}{h}}$$

When this limit exists, $f$ is **differentiable at $a$** and $f'(a)$ is the
**derivative** of $f$ at $a$.

![FIG-01-17-001: Curve y = f(x) with a fixed point P at (a, f(a)) and three successively closer points Q₁, Q₂, Q₃ at (a+h, f(a+h)) for decreasing h. Three secant lines PQ₁, PQ₂, PQ₃ are drawn in progressively lighter dashes, pivoting toward a solid tangent line at P. Each secant is labeled with its slope Δy/Δx, and the tangent is labeled f'(a). A callout notes "h shrinks; secant → tangent".](../figures/FIG-01-17-001-secant-to-tangent.png)

Leaving $a$ as a variable gives the **derivative function**:

$$f'(x) = \lim_{h\to 0}\frac{f(x+h) - f(x)}{h}$$

This is a new function, defined wherever the limit exists, whose value at each
point is the slope of the original curve there.

### Worked Example 1 — Derivative from the Definition

**Given.** $f(x) = 3x^2 - 5x + 2$.

**Find.** $f'(x)$ from the definition, then $f'(2)$.

**Solution.**

Build $f(x+h)$ first, carefully:

$$f(x+h) = 3(x+h)^2 - 5(x+h) + 2$$

$$= 3\left(x^2 + 2xh + h^2\right) - 5x - 5h + 2$$

$$= 3x^2 + 6xh + 3h^2 - 5x - 5h + 2$$

Subtract $f(x) = 3x^2 - 5x + 2$. Every term without an $h$ cancels — it must,
or the difference quotient could not have a limit:

$$f(x+h) - f(x) = 6xh + 3h^2 - 5h$$

Factor out $h$:

$$= h\left(6x + 3h - 5\right)$$

Divide by $h$. This is the cancellation that resolves the $\frac{0}{0}$, and
it is legitimate because $h \ne 0$ throughout the limit process:

$$\frac{f(x+h)-f(x)}{h} = 6x + 3h - 5$$

Now the limit is direct substitution:

$$f'(x) = \lim_{h\to 0}\left(6x + 3h - 5\right) = \boxed{6x - 5}$$

At $x = 2$:

$$f'(2) = 12 - 5 = \boxed{7}$$

**Check numerically.** $f(2) = 12 - 10 + 2 = 4$.

$f(2.001) = 3(4.004001) - 5(2.001) + 2 = 12.012003 - 10.005 + 2 = 4.007003$

$$\frac{4.007003 - 4}{0.001} = \frac{0.007003}{0.001} = 7.003$$

Close to 7, and the small excess is the $3h$ term we discarded in the limit:
$3(0.001) = 0.003$ ✓ The agreement is exact to the term we can account for,
which is a stronger check than mere proximity.

> ---
> **Mentor's Margin**
>
> Notice the structure of that calculation, because every derivative from the
> definition follows it: expand $f(x+h)$, subtract $f(x)$ so the $h$-free terms
> cancel, factor $h$ out of what remains, cancel it, then substitute $h = 0$.
> Four steps, always the same.
>
> You will not compute many derivatives this way in practice — the rules in
> §17.4 onward are far faster. But the FE has been known to ask conceptual
> questions about the definition, and more importantly, understanding that
> every rule *came from* this process is what keeps the rules from feeling
> arbitrary. When you meet the product rule and it looks strange, remember
> somebody did this limit once and that is what came out.
>
> ---

---

## 17.2 Geometric Meaning: Tangent and Normal Lines

The derivative $f'(a)$ is the **slope of the line tangent to the curve
$y = f(x)$ at $x = a$**.

That gives you the tangent line immediately, using point-slope form from
Chapter 01-09:

$$\boxed{\text{Tangent at } x = a: \quad y - f(a) = f'(a)\,(x - a)}$$

The **normal line** is perpendicular to the tangent at the same point. From
Chapter 01-09, perpendicular slopes are negative reciprocals:

$$\boxed{m_{\text{norm}} = -\frac{1}{f'(a)} \qquad (f'(a) \ne 0)}$$

Reading a graph:

| $f'$ at a point | Curve behaviour there |
|---|---|
| $f' > 0$ | rising (increasing) |
| $f' < 0$ | falling (decreasing) |
| $f' = 0$ | horizontal tangent — a flat spot |
| $f'$ large in magnitude | steep |
| $f'$ small in magnitude | nearly flat |

![FIG-01-17-002: Two vertically stacked, x-aligned plots. Top: a curve f(x) with a local maximum and a local minimum, with tangent lines drawn at four marked points — one on a rising stretch, one at the maximum (horizontal), one on a falling stretch, one at the minimum (horizontal). Bottom: the derivative f'(x) plotted on the same x-axis, crossing zero exactly below each horizontal tangent, positive where f rises and negative where f falls. Vertical dashed guide lines connect the four marked points between the two plots.](../figures/FIG-01-17-002-derivative-as-slope.png)

That figure is worth studying for a minute. The derivative crossing zero
corresponds exactly to the original curve having a horizontal tangent. That
correspondence is the entire basis of finding maxima and minima, which is
Chapter 01-18.

### Worked Example 2 — Tangent and Normal Lines

**Given.** $f(x) = x^3 - 2x$ at the point where $x = 2$. Take as given that
$f'(x) = 3x^2 - 2$ — we establish the power rule in §17.4 and this is an
instance of it.

**Find.** The tangent line and the normal line at $x = 2$.

**Solution.**

Point on the curve:

$$f(2) = 8 - 4 = 4 \implies (2, 4)$$

Slope of the tangent:

$$f'(2) = 3(4) - 2 = 10$$

Tangent line:

$$y - 4 = 10(x - 2) \implies \boxed{y = 10x - 16}$$

Normal slope:

$$m_{\text{norm}} = -\frac{1}{10} = -0.1$$

Normal line:

$$y - 4 = -0.1(x-2) \implies \boxed{y = -0.1x + 4.2}$$

**Check.** Both lines must pass through $(2,4)$.

Tangent: $10(2) - 16 = 4$ ✓

Normal: $-0.1(2) + 4.2 = -0.2 + 4.2 = 4$ ✓

And the slopes must satisfy $m_{\text{tan}} \cdot m_{\text{norm}} = -1$:
$(10)(-0.1) = -1$ ✓

---

## 17.3 Physical Meaning: Rate of Change, and Its Units

$\frac{dy}{dx}$ is the rate at which $y$ changes per unit change in $x$. Its
units follow mechanically:

$$\boxed{\left[\frac{dy}{dx}\right] = \frac{[y]}{[x]}}$$

| Derivative | Physical name | Units |
|---|---|---|
| $\dfrac{ds}{dt}$ | velocity | m/s |
| $\dfrac{dv}{dt}$ | acceleration | m/s² |
| $\dfrac{dh}{dt}$ | rate of level change | m/min |
| $\dfrac{dQ}{dt}$ | volumetric flow rate | m³/s |
| $\dfrac{dT}{dx}$ | temperature gradient | °C/m |
| $\dfrac{dP}{dQ}$ | pressure-drop sensitivity | kPa per L/s |
| $\dfrac{dC}{dt}$ | reaction rate | mol/(L·s) |

> ---
> **Mentor's Margin**
>
> The units rule is one of the best error checks in all of calculus, and it
> costs nothing. If you differentiate a deflection in millimetres with respect
> to a position in metres and your answer comes out in newtons, you have made
> an algebra error — not a units error, an *algebra* error. The units are
> telling you the expression is wrong.
>
> Combine this with the dimensional homogeneity habit from Chapter 01-02 and
> you have two independent checks on every rate you compute. Use them. On a
> timed exam the twenty seconds a units check costs is the cheapest insurance
> available.
>
> ---

### Worked Example 3 — Rate of Change with Units

**Given.** The tank level from Chapter 01-16, responding to a step inflow:

$$h(t) = 4.5\left(1 - e^{-t/6.0}\right) \text{ m}, \qquad t \text{ in minutes}$$

**(a)** Find $\dfrac{dh}{dt}$ and state its units. (Take as given
$\frac{d}{dt}e^{kt} = ke^{kt}$, established in §17.7.)
**(b)** Evaluate the filling rate at $t = 0$ and at $t = 6.0$ min.
**(c)** Explain the trend in one sentence.

**Solution.**

**(a)**

$$\frac{dh}{dt} = 4.5\cdot\frac{d}{dt}\left(1 - e^{-t/6.0}\right) = 4.5\left(0 - \left(-\tfrac{1}{6.0}\right)e^{-t/6.0}\right)$$

$$\frac{dh}{dt} = \frac{4.5}{6.0}e^{-t/6.0} = \boxed{0.75\,e^{-t/6.0} \text{ m/min}}$$

Units check: $[h] = $ m and $[t] = $ min, so $\left[\frac{dh}{dt}\right] = $
m/min ✓ And the constant $4.5/6.0$ carries units m/min directly, since 4.5 is
in metres and 6.0 is in minutes. The exponential is dimensionless ✓

**(b)**

At $t = 0$: $\dfrac{dh}{dt} = 0.75(1) = \boxed{0.75 \text{ m/min}}$

At $t = 6.0$ min (one time constant): $e^{-1} = 0.367879$

$$\frac{dh}{dt} = 0.75(0.367879) = \boxed{0.276 \text{ m/min}}$$

**(c)** The filling rate is maximum at the instant the inflow steps up and
decays exponentially thereafter, because as the level rises the outflow rises
with it and the net accumulation shrinks — which is precisely why the level
approaches 4.5 m asymptotically rather than overshooting.

**Cross-check against Chapter 01-16.** There we found the terminal level is
4.5 m and the level reaches 99.3% of it at $t = 5\tau$. Consistent: the rate
at $t = 5\tau$ is $0.75e^{-5} = 0.0051$ m/min, essentially zero. The level has
stopped changing, which is what "terminal" means ✓

---

## 17.4 Differentiability and Continuity

The two are related but not equivalent, and the direction of the implication
matters.

$$\boxed{\text{differentiable at } a \implies \text{continuous at } a}$$

$$\boxed{\text{continuous at } a \;\not\Longrightarrow\; \text{differentiable at } a}$$

Differentiability is the **stronger** condition. A function can be perfectly
continuous and still fail to have a derivative.

### The four ways differentiability fails

| Failure | Example | What the graph does |
|---|---|---|
| **Corner** | $\lvert x\rvert$ at $x = 0$ | abrupt change of slope; one-sided derivatives differ |
| **Cusp** | $x^{2/3}$ at $x = 0$ | slopes run to $+\infty$ and $-\infty$ |
| **Vertical tangent** | $x^{1/3}$ at $x = 0$ | tangent is vertical; slope undefined |
| **Discontinuity** | any jump or hole | no tangent to speak of |

![FIG-01-17-003: Four small panels in a row, each showing a curve near a marked point x = a. Panel 1 "Corner — |x|": a V shape with the vertex at the origin, two tangent lines of slope −1 and +1 drawn on either side, labeled "left and right derivatives differ". Panel 2 "Cusp — x^(2/3)": a sharp upward point at the origin with near-vertical tangents on both sides pointing opposite ways. Panel 3 "Vertical tangent — x^(1/3)": an S-shaped curve through the origin with a vertical dashed tangent line, labeled "slope undefined". Panel 4 "Discontinuity": a jump, with a filled dot and an open dot at different heights, labeled "not continuous, so not differentiable".](../figures/FIG-01-17-003-non-differentiable-points.png)

For $\lvert x \rvert$ at zero, the one-sided derivatives are

$$\lim_{h\to 0^-}\frac{\lvert h\rvert - 0}{h} = \frac{-h}{h} = -1 \qquad \lim_{h\to 0^+}\frac{\lvert h\rvert}{h} = \frac{h}{h} = +1$$

They disagree, so by the two-sided limit rule from Chapter 01-16 the
derivative does not exist. The function is continuous there — you can draw it
without lifting your pencil — but it has a corner, and a corner has no single
tangent line.

> ---
> **Mentor's Margin**
>
> Corners are not pathological curiosities. They are all over engineering.
> A shear diagram has a corner at every point load. A stress–strain curve has
> a corner at the yield point. A control signal that saturates has a corner at
> the saturation limit. Absolute value and $\max/\min$ operations produce
> corners by construction.
>
> The practical consequence: when you differentiate a piecewise model, check
> the branch boundaries separately. The derivative may genuinely not exist
> there, and reporting a value anyway is claiming smoothness the physics does
> not have.
>
> ---

---

## 17.5 The Basic Rules

Now the machinery. Each of these was obtained once by doing the limit from
§17.1 in general; from here on you apply the result.

### Constant rule

$$\boxed{\frac{d}{dx}(c) = 0}$$

A constant function has a horizontal graph, so its slope is zero everywhere.

### Power rule

$$\boxed{\frac{d}{dx}\left(x^n\right) = n\,x^{\,n-1}} \qquad \text{for any real } n$$

Bring the exponent down as a multiplier, then reduce the exponent by one.

Verify it for $n = 2$ from the definition:

$$\frac{(x+h)^2 - x^2}{h} = \frac{x^2 + 2xh + h^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h \longrightarrow 2x \;\checkmark$$

And for $n = 3$:

$$\frac{(x+h)^3 - x^3}{h} = \frac{3x^2h + 3xh^2 + h^3}{h} = 3x^2 + 3xh + h^2 \longrightarrow 3x^2 \;\checkmark$$

> ---
> **Mentor's Margin**
>
> The general proof of the power rule for arbitrary integer $n$ needs the
> binomial expansion of $(x+h)^n$, which we have not built — it depends on
> combinations, and those arrive in Chapter 01-38. So take the general
> statement as an established fact rather than something proved here. You can
> verify it yourself for $n = 4, 5$ by direct expansion if the pattern does not
> feel solid, and the two cases above already show the mechanism clearly: the
> $x^n$ terms cancel, exactly one surviving term has a single $h$ in it, and
> every other term has $h^2$ or higher and dies in the limit.
>
> The rule holds for negative and fractional exponents too, which is what
> makes it so useful. Those cases need a slightly different argument, but the
> formula is identical.
>
> ---

The power rule covers far more than polynomials once you rewrite radicals and
reciprocals as powers — the habit from Chapter 01-05:

| Expression | Rewritten | Derivative |
|---|---|---|
| $\sqrt{x}$ | $x^{1/2}$ | $\tfrac12 x^{-1/2} = \dfrac{1}{2\sqrt{x}}$ |
| $\dfrac{1}{x}$ | $x^{-1}$ | $-x^{-2} = -\dfrac{1}{x^2}$ |
| $\dfrac{1}{x^3}$ | $x^{-3}$ | $-3x^{-4} = -\dfrac{3}{x^4}$ |
| $\sqrt[3]{x^2}$ | $x^{2/3}$ | $\tfrac23 x^{-1/3}$ |

### Constant-multiple and sum rules

$$\boxed{\frac{d}{dx}\left[c\,f(x)\right] = c\,f'(x)}$$

$$\boxed{\frac{d}{dx}\left[f(x) \pm g(x)\right] = f'(x) \pm g'(x)}$$

Differentiation is **linear** — it passes through scalar multiples and splits
across addition. This is the same linearity structure you met for summation in
Chapter 01-15, and it has the same limitation: it does **not** pass through
products or quotients. Those need their own rules.

### Worked Example 4 — Basic Rules Combined

**Given.** $y = 5x^4 - \dfrac{3}{x^2} + 2\sqrt{x} - 7$

**Find.** $\dfrac{dy}{dx}$

**Solution.**

Rewrite everything as a power first:

$$y = 5x^4 - 3x^{-2} + 2x^{1/2} - 7$$

Differentiate term by term:

$$\frac{dy}{dx} = 5(4)x^3 - 3(-2)x^{-3} + 2\left(\tfrac12\right)x^{-1/2} - 0$$

$$= 20x^3 + 6x^{-3} + x^{-1/2}$$

$$= \boxed{20x^3 + \frac{6}{x^3} + \frac{1}{\sqrt{x}}}$$

**Check at $x = 1$.** $\frac{dy}{dx}\big|_{1} = 20 + 6 + 1 = 27$.

Numerically: $y(1) = 5 - 3 + 2 - 7 = -3$.

$y(1.001) = 5(1.004006) - 3(0.998002) + 2(1.0004999) - 7$
$= 5.020030 - 2.994006 + 2.001000 - 7 = -2.972976$

$$\frac{-2.972976 - (-3)}{0.001} = \frac{0.027024}{0.001} = 27.02 \;\checkmark$$

---

## 17.6 Product, Quotient, and Chain Rules

These three are where derivative work actually happens, and the chain rule is
the one that separates fluent from halting.

### Product rule

$$\boxed{\frac{d}{dx}(uv) = u'v + uv'}$$

Derivative of the first times the second, plus the first times the derivative
of the second.

Note what it is **not**: $\frac{d}{dx}(uv) \ne u'v'$. Test it on $u = v = x$:
the product is $x^2$ with derivative $2x$, but $u'v' = 1$. Different.

### Quotient rule

$$\boxed{\frac{d}{dx}\left(\frac{u}{v}\right) = \frac{u'v - uv'}{v^2}}$$

The order in the numerator matters — it is $u'v$ minus $uv'$, not the reverse.
The mnemonic that survives exam pressure: *bottom times derivative of top,
minus top times derivative of bottom, all over bottom squared.*

### Chain rule

For a composite function $y = f\big(g(x)\big)$:

$$\boxed{\frac{dy}{dx} = f'\big(g(x)\big)\cdot g'(x)}$$

Or in Leibniz notation, with $u = g(x)$:

$$\boxed{\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dx}}$$

Differentiate the outer function, leaving the inner one alone, then multiply
by the derivative of the inner function.

The Leibniz form is worth staring at, because it looks like the $du$ cancels
— and while that is not a rigorous argument, it is an excellent memory device
and it generalizes correctly to longer chains:

$$\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dv}\cdot\frac{dv}{dx}$$

![FIG-01-17-004: Chain rule as nested layers. The expression sin³(2x+1) drawn as three concentric rounded boxes: innermost box labeled "inner: 2x+1, derivative 2", middle box labeled "middle: sin(u), derivative cos(u)", outer box labeled "outer: (·)³, derivative 3(·)²". To the right, the three derivative factors are shown multiplied together in order — 3sin²(2x+1) · cos(2x+1) · 2 — with arrows connecting each factor back to its layer, and the final result 6sin²(2x+1)cos(2x+1) boxed below.](../figures/FIG-01-17-004-chain-rule-layers.png)

> ---
> **Mentor's Margin**
>
> The chain rule is the rule people get wrong, and the failure is almost never
> the formula — it is not noticing a composition is present. $\sin(3x)$ is a
> composition. $e^{-2t}$ is a composition. $(5x^2-3)^4$ is a composition.
> $\sqrt{x^2+1}$ is a composition. Every one of them needs the inner
> derivative multiplied on, and forgetting it drops a constant factor.
>
> Build this habit: before differentiating anything, ask *is there a function
> inside another function?* If yes, identify the layers explicitly — write them
> down as $u = \ldots$ — and peel from the outside in. Once the layers are on
> paper the rule is mechanical. The error happens when you try to do it in your
> head.
>
> ---

### Worked Example 5 — Product Rule, with an Independent Check

**Given.** $y = \left(3x^2+1\right)\left(x^3-4x\right)$

**Find.** $\dfrac{dy}{dx}$ two ways.

**Solution — product rule.**

$$u = 3x^2+1, \quad u' = 6x$$
$$v = x^3-4x, \quad v' = 3x^2-4$$

$$\frac{dy}{dx} = 6x\left(x^3-4x\right) + \left(3x^2+1\right)\left(3x^2-4\right)$$

$$= 6x^4 - 24x^2 + \left(9x^4 - 12x^2 + 3x^2 - 4\right)$$

$$= 6x^4 - 24x^2 + 9x^4 - 9x^2 - 4$$

$$= \boxed{15x^4 - 33x^2 - 4}$$

**Check — expand first, then differentiate.**

$$y = 3x^5 - 12x^3 + x^3 - 4x = 3x^5 - 11x^3 - 4x$$

$$\frac{dy}{dx} = 15x^4 - 33x^2 - 4 \;\checkmark$$

Identical. For a product of two polynomials you can always expand instead, and
sometimes should. For a product involving a trig or exponential factor you
cannot, which is why the rule earns its place.

### Worked Example 6 — Quotient Rule

**Given.** $y = \dfrac{2x-1}{x^2+3}$

**Find.** $\dfrac{dy}{dx}$, then evaluate at $x = 0$.

**Solution.**

$$u = 2x-1, \quad u' = 2$$
$$v = x^2+3, \quad v' = 2x$$

$$\frac{dy}{dx} = \frac{2\left(x^2+3\right) - (2x-1)(2x)}{\left(x^2+3\right)^2}$$

$$= \frac{2x^2 + 6 - \left(4x^2 - 2x\right)}{\left(x^2+3\right)^2}$$

$$= \boxed{\frac{-2x^2 + 2x + 6}{\left(x^2+3\right)^2}}$$

At $x = 0$:

$$\frac{dy}{dx}\bigg|_{0} = \frac{6}{9} = \frac{2}{3} \approx 0.6667$$

**Check numerically.** $y(0) = \frac{-1}{3} = -0.333333$

$y(0.001) = \dfrac{0.002 - 1}{3.000001} = \dfrac{-0.998}{3.000001} = -0.332666$

$$\frac{-0.332666 - (-0.333333)}{0.001} = \frac{0.000667}{0.001} = 0.667 \;\checkmark$$

### Worked Example 7 — Chain Rule, Three Cases

**Find each derivative.**

**(a)** $y = \left(5x^2-3\right)^4$

Layers: outer is $(\;)^4$, inner is $5x^2-3$ with derivative $10x$.

$$\frac{dy}{dx} = 4\left(5x^2-3\right)^3(10x) = \boxed{40x\left(5x^2-3\right)^3}$$

**(b)** $y = \sqrt{3x^2+1}$

Rewrite as $\left(3x^2+1\right)^{1/2}$. Inner derivative is $6x$.

$$\frac{dy}{dx} = \tfrac12\left(3x^2+1\right)^{-1/2}(6x) = \boxed{\frac{3x}{\sqrt{3x^2+1}}}$$

**(c)** $y = \sin^3(2x+1)$ — a three-layer chain.

This is $\big[\sin(2x+1)\big]^3$. Peel from outside in:

- outer $(\;)^3$ → $3\big[\sin(2x+1)\big]^2$
- middle $\sin(\;)$ → $\cos(2x+1)$
- inner $2x+1$ → $2$

$$\frac{dy}{dx} = 3\sin^2(2x+1)\cdot\cos(2x+1)\cdot 2 = \boxed{6\sin^2(2x+1)\cos(2x+1)}$$

(The trig derivatives come in §17.7; the chain structure is the point here.)

---

## 17.7 Derivatives of the Transcendental Functions

### Trigonometric functions

$$\boxed{\frac{d}{dx}\sin x = \cos x \qquad \frac{d}{dx}\cos x = -\sin x}$$

**In radians only.** These are false in degrees, for exactly the reason the
special limits in Chapter 01-16 required radians.

Here is the derivation, because it is the cleanest payoff of that chapter.
Using the sum formula for sine from Chapter 01-11:

$$\frac{\sin(x+h) - \sin x}{h} = \frac{\sin x\cos h + \cos x\sin h - \sin x}{h}$$

Group the $\sin x$ terms:

$$= \sin x\left(\frac{\cos h - 1}{h}\right) + \cos x\left(\frac{\sin h}{h}\right)$$

Now take $h \to 0$. The first bracket is $-\frac{1-\cos h}{h} \to -0 = 0$, and
the second is $\frac{\sin h}{h} \to 1$. Both from §16.8:

$$\frac{d}{dx}\sin x = \sin x(0) + \cos x(1) = \cos x \;\checkmark$$

Those two special limits existed for this.

The remaining four follow from the quotient rule. For tangent:

$$\frac{d}{dx}\tan x = \frac{d}{dx}\frac{\sin x}{\cos x} = \frac{\cos x\cos x - \sin x(-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x$$

using the Pythagorean identity from Chapter 01-11. The full table:

| $f(x)$ | $f'(x)$ |
|---|---|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sec x$ | $\sec x\tan x$ |
| $\csc x$ | $-\csc x\cot x$ |

The pattern: every **co**-function derivative carries a minus sign. Cosine,
cotangent, cosecant — all negative. That is the whole memory device.

### Inverse trigonometric functions

$$\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}} \qquad \frac{d}{dx}\arccos x = \frac{-1}{\sqrt{1-x^2}} \qquad \frac{d}{dx}\arctan x = \frac{1}{1+x^2}$$

Again the co-function carries the minus sign. Note that these are **algebraic**
functions — no trig appears in the results, which is initially surprising and
turns out to be extremely useful in integration.

### Exponential functions

$$\boxed{\frac{d}{dx}e^x = e^x}$$

The exponential with base $e$ is its own derivative. That property is what
makes $e$ the natural base and it is essentially the definition of $e$ — the
unique base for which

$$\lim_{h\to 0}\frac{e^h - 1}{h} = 1$$

Feed that into the difference quotient:

$$\frac{e^{x+h} - e^x}{h} = e^x\left(\frac{e^h-1}{h}\right) \longrightarrow e^x(1) = e^x \;\checkmark$$

For a general base, from Chapter 01-05's change-of-base relation
$a^x = e^{x\ln a}$, the chain rule gives:

$$\boxed{\frac{d}{dx}a^x = a^x\ln a}$$

With $a = e$ we get $\ln e = 1$ and recover the special case.

### Logarithmic functions

$$\boxed{\frac{d}{dx}\ln x = \frac{1}{x} \qquad (x > 0)}$$

$$\frac{d}{dx}\log_a x = \frac{1}{x\ln a}$$

We derive the first of these in §17.9 using implicit differentiation, which is
the honest way to get it.

### The chain rule versions

In practice you almost never differentiate a bare $\sin x$ or $e^x$. You
differentiate $\sin(\omega t + \phi)$ and $e^{-t/\tau}$. So learn the composite
forms directly:

$$\frac{d}{dx}\sin u = \cos u \cdot u' \qquad \frac{d}{dx}e^u = e^u \cdot u' \qquad \frac{d}{dx}\ln u = \frac{u'}{u}$$

The logarithm form is worth noting separately: the derivative of a log is
*inner derivative over inner function*. It comes up constantly.

### Worked Example 8 — Combined Rules

**Find each derivative.**

**(a)** $y = x^2e^{3x}$ — product with a chain inside

$$u = x^2, \; u' = 2x \qquad v = e^{3x}, \; v' = 3e^{3x}$$

$$\frac{dy}{dx} = 2xe^{3x} + x^2\left(3e^{3x}\right) = \boxed{xe^{3x}(2+3x)}$$

**(b)** $y = e^{-2x}\sin(4x)$ — product, chain in both factors

$$u = e^{-2x}, \; u' = -2e^{-2x} \qquad v = \sin 4x, \; v' = 4\cos 4x$$

$$\frac{dy}{dx} = -2e^{-2x}\sin 4x + e^{-2x}\left(4\cos 4x\right) = \boxed{e^{-2x}\left(4\cos 4x - 2\sin 4x\right)}$$

**(c)** $y = \ln\left(x^2+1\right)$

Inner derivative over inner function:

$$\frac{dy}{dx} = \boxed{\frac{2x}{x^2+1}}$$

**(d)** $y = \ln(\cos x)$

$$\frac{dy}{dx} = \frac{-\sin x}{\cos x} = \boxed{-\tan x}$$

**(e)** $y = \ln(5x)$ — a deliberate trap

Chain rule: $\frac{5}{5x} = \frac{1}{x}$.

Or use the log law from Chapter 01-05 first: $\ln(5x) = \ln 5 + \ln x$, and
$\ln 5$ is a constant with derivative zero, so $\frac{dy}{dx} = \frac{1}{x}$.

$$\boxed{\frac{1}{x}}$$

Both routes agree. A multiplicative constant inside a logarithm has **no
effect** on the derivative, which surprises people. The log law explains why.

---

## 17.8 Higher-Order Derivatives

Differentiate the derivative and you get the **second derivative**:

$$f''(x) = \frac{d}{dx}\left[f'(x)\right] = \frac{d^2y}{dx^2}$$

Keep going for third, fourth, and beyond. Past three primes the notation
becomes unreadable, so switch to $f^{(4)}(x)$ or $\frac{d^4y}{dx^4}$.

### What the second derivative means

| Reading | Interpretation |
|---|---|
| Geometric | rate of change of the slope — **concavity** |
| $f'' > 0$ | concave up (curve holds water) |
| $f'' < 0$ | concave down (curve spills water) |
| Physical, with $t$ | acceleration, when the first derivative is velocity |

### The kinematic chain

$$\text{position } s(t) \;\xrightarrow{\;d/dt\;}\; \text{velocity } v(t) \;\xrightarrow{\;d/dt\;}\; \text{acceleration } a(t)$$

$$v = \frac{ds}{dt} = \dot{s} \qquad a = \frac{dv}{dt} = \frac{d^2s}{dt^2} = \ddot{s}$$

![FIG-01-17-005: Three vertically stacked, t-aligned plots for s(t) = t³ − 6t² + 9t on 0 ≤ t ≤ 4. Top: position s(t), showing a local maximum at t = 1 and a local minimum at t = 3. Middle: velocity v(t) = 3t² − 12t + 9, a parabola crossing zero at t = 1 and t = 3, negative between them. Bottom: acceleration a(t) = 6t − 12, a straight line crossing zero at t = 2. Vertical dashed guide lines at t = 1, 2, 3 run through all three panels, with annotations: "v = 0 at the turning points of s" and "a = 0 where v is at its minimum".](../figures/FIG-01-17-005-position-velocity-acceleration.png)

### Worked Example 9 — Kinematics

**Given.** A particle moves along a line with position
$s(t) = t^3 - 6t^2 + 9t$ metres, $t$ in seconds.

**(a)** Find $v(t)$ and $a(t)$ with units.
**(b)** When is the particle momentarily at rest?
**(c)** When is the acceleration zero, and what is the velocity there?
**(d)** Over what interval is the particle moving backward?

**Solution.**

**(a)**

$$v(t) = \frac{ds}{dt} = 3t^2 - 12t + 9 \text{ m/s}$$

$$a(t) = \frac{dv}{dt} = 6t - 12 \text{ m/s}^2$$

Units: $[s] = $ m, $[t] = $ s, so $[v] = $ m/s and $[a] = $ m/s² ✓

**(b)** At rest means $v = 0$:

$$3t^2 - 12t + 9 = 0 \implies t^2 - 4t + 3 = 0 \implies (t-1)(t-3) = 0$$

$$\boxed{t = 1 \text{ s and } t = 3 \text{ s}}$$

**(c)** $a = 0$ when $6t - 12 = 0$, so $t = 2$ s.

$$v(2) = 3(4) - 24 + 9 = 12 - 24 + 9 = -3 \text{ m/s}$$

$$\boxed{t = 2 \text{ s}, \; v = -3 \text{ m/s}}$$

At $t = 2$ the particle is moving backward at its fastest — acceleration zero
marks the extreme of velocity, which is exactly the pattern the figure shows.

**(d)** Moving backward means $v < 0$. The parabola $3(t-1)(t-3)$ opens upward
with roots at 1 and 3, so it is negative between them:

$$\boxed{1 \text{ s} < t < 3 \text{ s}}$$

**Check.** $v(2) = -3 < 0$ ✓ (inside the interval), and $v(0) = 9 > 0$,
$v(4) = 48 - 48 + 9 = 9 > 0$ ✓ (outside it).

**Positions at the turning points.** $s(1) = 1 - 6 + 9 = 4$ m and
$s(3) = 27 - 54 + 27 = 0$ m. The particle advances to 4 m, reverses back to
the origin, then advances again — consistent with the top panel of the figure.

> ---
> **Mentor's Margin**
>
> Worked Example 9 is the whole of one-dimensional kinematics, and you will
> redo this exact calculation many times in Tier 2C. Notice that no physics
> was required — only differentiation and the quadratic formula from Chapter
> 01-07. The physics is entirely in the interpretation: which derivative is
> velocity, what "at rest" means, what sign tells you about direction.
>
> That is the pattern for the rest of the guide. The mathematics is built. New
> chapters supply new physical meaning for tools you already own.
>
> ---

> **Preview note.** Higher derivatives chain further than three in beam
> theory. Deflection differentiates to slope, slope to curvature (which is
> proportional to bending moment), moment to shear, shear to distributed load —
> five related functions connected by successive derivatives. Chapter 02-49
> develops that relationship properly. Nothing here depends on it; it is
> mentioned so you know the second derivative is not the end of the line.

---

## 17.9 Implicit Differentiation

Sometimes $y$ is not given explicitly as a function of $x$. The circle

$$x^2 + y^2 = 25$$

defines $y$ in terms of $x$ but does not isolate it, and solving for $y$
requires splitting into two branches with a $\pm$. Implicit differentiation
avoids that entirely.

**The method.** Differentiate both sides with respect to $x$, treating $y$ as
a function of $x$. Every time you differentiate a term containing $y$, the
chain rule contributes a factor $\frac{dy}{dx}$. Then solve algebraically for
$\frac{dy}{dx}$.

For the circle:

$$\frac{d}{dx}\left(x^2\right) + \frac{d}{dx}\left(y^2\right) = \frac{d}{dx}(25)$$

$$2x + 2y\frac{dy}{dx} = 0$$

$$\frac{dy}{dx} = -\frac{x}{y}$$

At the point $(3, 4)$: $\frac{dy}{dx} = -\frac{3}{4}$.

**Check explicitly.** On the upper branch $y = \sqrt{25-x^2}$, the chain rule
gives $\frac{dy}{dx} = \frac{-x}{\sqrt{25-x^2}}$, which at $x = 3$ is
$\frac{-3}{4}$ ✓ Same answer, considerably more work.

> ---
> **Mentor's Margin**
>
> The single point to internalize: $\frac{d}{dx}\left(y^2\right) = 2y
> \frac{dy}{dx}$, **not** $2y$. The extra factor is the chain rule, because $y$
> is a function of $x$, not an independent variable. Forgetting it is the only
> real error mode in implicit differentiation, and it is worth writing the
> $\frac{dy}{dx}$ factor out explicitly every single time until the habit is
> automatic.
>
> ---

### Deriving the logarithm derivative

Implicit differentiation is how we honestly obtain $\frac{d}{dx}\ln x$.

Let $y = \ln x$. By the definition of the logarithm from Chapter 01-05, this
is equivalent to

$$e^y = x$$

Differentiate both sides with respect to $x$:

$$e^y\frac{dy}{dx} = 1$$

$$\frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x}$$

since $e^y = x$. Hence

$$\frac{d}{dx}\ln x = \frac{1}{x} \;\checkmark$$

The same trick — write the inverse relation, differentiate implicitly, back-
substitute — produces every inverse-function derivative, including the inverse
trig formulas in §17.7.

### Worked Example 10 — Implicit Differentiation

**Given.** $x^3 + y^3 = 6xy$ (the folium of Descartes).

**(a)** Find $\dfrac{dy}{dx}$.
**(b)** Find the slope of the tangent at the point $(3, 3)$.

**Solution.**

**(a)** Differentiate both sides. The right side needs the product rule:

$$3x^2 + 3y^2\frac{dy}{dx} = 6\left(1\cdot y + x\frac{dy}{dx}\right)$$

$$3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$$

Collect the $\frac{dy}{dx}$ terms on one side:

$$3y^2\frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^2$$

$$\frac{dy}{dx}\left(3y^2 - 6x\right) = 6y - 3x^2$$

$$\frac{dy}{dx} = \frac{6y-3x^2}{3y^2-6x} = \boxed{\frac{2y-x^2}{y^2-2x}}$$

**(b)** First confirm $(3,3)$ is on the curve:

$$27 + 27 = 54 \qquad 6(3)(3) = 54 \;\checkmark$$

$$\frac{dy}{dx}\bigg|_{(3,3)} = \frac{2(3) - 9}{9 - 2(3)} = \frac{6-9}{9-6} = \frac{-3}{3} = \boxed{-1}$$

The tangent at $(3,3)$ has slope $-1$.

---

## 17.10 Engineering Sensitivity: A Worked Application

### Worked Example 11 — Pressure-Drop Sensitivity

**Given.** Pressure drop through a length of pipe follows an empirical power
law

$$\Delta P = k\,Q^{1.85}$$

with $k = 0.42$ kPa/(L/s)$^{1.85}$ and design flow $Q = 12$ L/s.

**(a)** Compute $\Delta P$ at the design flow.
**(b)** Compute $\dfrac{d(\Delta P)}{dQ}$ at the design flow, with units.
**(c)** Estimate the additional pressure drop if flow increases by
0.5 L/s.
**(d)** Verify (b) using the power-law sensitivity relationship.

**Solution.**

**(a)** $\ln 12 = 2.484907$, so $12^{1.85} = e^{1.85(2.484907)} =
e^{4.597078} = 99.20$

$$\Delta P = 0.42(99.20) = \boxed{41.66 \text{ kPa}}$$

**(b)** Power rule:

$$\frac{d(\Delta P)}{dQ} = 1.85\,k\,Q^{0.85} = 1.85(0.42)(12)^{0.85}$$

$12^{0.85} = e^{0.85(2.484907)} = e^{2.112171} = 8.267$

$$= 0.777(8.267) = \boxed{6.42 \text{ kPa per L/s}}$$

Units: $[\Delta P]/[Q] = $ kPa/(L/s) ✓

**(c)** Linear estimate using the derivative:

$$\Delta(\Delta P) \approx \frac{d(\Delta P)}{dQ}\cdot\Delta Q = 6.42(0.5) = \boxed{3.21 \text{ kPa}}$$

**Compare with the exact recomputation.** At $Q = 12.5$ L/s:
$\ln 12.5 = 2.525729$, $12.5^{1.85} = e^{4.672599} = 106.98$

$$\Delta P = 0.42(106.98) = 44.93 \text{ kPa}$$

Exact increase: $44.93 - 41.66 = 3.27$ kPa.

The linear estimate of 3.21 kPa is within 2% — good, because the increment is
small relative to the operating point. The estimate is slightly low because
the function is concave up, so the tangent line sits below the curve.

**(d)** For any power law $y = kx^n$, the derivative and the average ratio are
related by exactly the exponent:

$$\frac{dy/dx}{y/x} = \frac{nkx^{n-1}}{kx^{n-1}} = n$$

Here: $\dfrac{\Delta P}{Q} = \dfrac{41.66}{12} = 3.472$ kPa per L/s, and

$$1.85 \times 3.472 = 6.42 \text{ kPa per L/s} \;\checkmark$$

This confirms (b) by a completely independent route, and it is a check worth
knowing: for any power law, the derivative equals the exponent times the
secant ratio through the origin.

---

## As the Handbook States It

> **Handbook 10.6, Mathematics section (begins p. 36)** — differentiation
> appears in the *Differential Calculus* subsection, approximately pp. 44–46.

The Handbook's derivative coverage is **good** — considerably better than its
coverage of limits. What you will find:

- The definition of the derivative as the limit of the difference quotient
- The derivative as the slope of the tangent line
- A table of derivatives covering: constants, powers, sums, products,
  quotients, the chain rule, all six trigonometric functions, the three
  principal inverse trigonometric functions, exponentials with base $e$ and
  base $a$, and logarithms with base $e$ and base $a$
- Implicit differentiation
- Higher-order derivative notation

**What's in the Handbook — find it fast:**

The derivative table is the single most-consulted page in the Mathematics
section. If you blank on $\frac{d}{dx}\sec x$ or on the sign in the quotient
rule, it is printed. Locate this table during your first Handbook practice
session and put it on your personal page map — you will return to it
repeatedly.

**What's not in the Handbook — memorize:**

- The units rule $\left[\frac{dy}{dx}\right] = \frac{[y]}{[x]}$ as an error
  check
- That differentiability implies continuity but not conversely
- The four failure modes: corner, cusp, vertical tangent, discontinuity
- The interpretation table for $f' > 0$, $f' < 0$, $f' = 0$
- The interpretation of $f''$ as concavity
- The kinematic chain $s \to v \to a$ and which derivative is which
- The tangent and normal line construction from a point and a slope
- The co-function minus-sign pattern in the trig derivative table
- The procedure for peeling a multi-layer chain rule
- That a multiplicative constant inside a logarithm does not affect the
  derivative
- The power-law sensitivity relation $\frac{dy/dx}{y/x} = n$
- The linear-estimate use of a derivative,
  $\Delta y \approx \frac{dy}{dx}\Delta x$

> ---
> **Mentor's Margin**
>
> Even with the table printed in the Handbook, memorize the common derivatives
> anyway — powers, $\sin$, $\cos$, $e^x$, $\ln x$, and all three of product,
> quotient, chain. A lookup costs fifteen to twenty seconds, and derivatives
> appear inside problems from a dozen different subject areas. If you look up
> $\frac{d}{dx}\sin x$ every time you need it, you will spend several minutes
> across the exam on something you could know instantly.
>
> Look up the rare ones — $\csc$, $\cot$, the inverse trig formulas. Know the
> common ones cold. That split is the right use of the Handbook.
>
> ---

---

## Where This Goes Wrong

**Forgetting the chain rule on a composition.** $\frac{d}{dx}\sin(3x)$ is
$3\cos(3x)$, not $\cos(3x)$. Any function inside another function contributes
its own derivative as a multiplicative factor. This is the number one
derivative error, by a wide margin.

**Using $u'v'$ for a product.** The product rule is $u'v + uv'$. Two terms,
not one. Test on $x \cdot x$ if you ever doubt it.

**Reversing the quotient rule numerator.** It is $u'v - uv'$. Getting the
order backwards flips the sign of the entire answer.

**Forgetting to square the denominator in the quotient rule.** The
denominator of the result is $v^2$, not $v$.

**Degrees instead of radians in trig derivatives.** $\frac{d}{dx}\sin x =
\cos x$ holds only in radians. In degrees an extra factor of $\frac{\pi}{180}$
appears. Every calculus formula involving trig assumes radians.

**Dropping the $\frac{dy}{dx}$ factor in implicit differentiation.**
$\frac{d}{dx}(y^3) = 3y^2\frac{dy}{dx}$. The chain rule applies because $y$
depends on $x$.

**Differentiating a constant to something other than zero.** $\frac{d}{dx}(7)
= 0$. Also $\frac{d}{dx}(\ln 5) = 0$ and $\frac{d}{dx}(e^2) = 0$ — these are
numbers, not functions of $x$.

**Confusing $\frac{d}{dx}a^x$ with $\frac{d}{dx}x^a$.** The first has the
variable in the exponent: $a^x\ln a$. The second has it in the base:
$ax^{a-1}$. Completely different rules. Check where the $x$ is before choosing.

**Assuming continuity guarantees differentiability.** $\lvert x\rvert$ is
continuous at zero and not differentiable there. The implication runs one way
only.

**Reporting a derivative at a corner.** If a piecewise model has a genuine
corner at a branch boundary, the derivative does not exist there. Check both
one-sided derivatives before answering.

**Units mismatch.** If $\frac{dy}{dx}$ does not come out in $[y]/[x]$, the
algebra is wrong. Use this check.

**Treating $\frac{dy}{dx}$ as a fraction to be split.** It is a single
symbol denoting a limit, not a ratio of two quantities $dy$ and $dx$. The
Leibniz notation is suggestive and the suggestion is often useful, but $dy$
and $dx$ are not numbers you can manipulate independently at this stage.

**Stopping at the first derivative when the question asks for acceleration.**
Acceleration is the *second* derivative of position. Read what is being asked.

---

## Key Terms

| Term | Definition |
|---|---|
| Difference quotient | $\dfrac{f(x+h)-f(x)}{h}$; the average rate of change over an interval |
| Derivative | The limit of the difference quotient as $h \to 0$; the instantaneous rate of change |
| Differentiable at a point | The defining limit exists at that point |
| Secant line | Line through two points on a curve; its slope is the difference quotient |
| Tangent line | Line touching the curve at one point with slope $f'(a)$ |
| Normal line | Line perpendicular to the tangent at the point of tangency |
| Leibniz notation | $\dfrac{dy}{dx}$; carries the variables and hence the units |
| Lagrange notation | $f'(x)$; compact, best for stating rules |
| Dot notation | $\dot{y}$; specifically a derivative with respect to time |
| Corner | Point where left and right derivatives exist but differ; not differentiable |
| Cusp | Point where the slopes run to $+\infty$ and $-\infty$; not differentiable |
| Power rule | $\dfrac{d}{dx}x^n = nx^{n-1}$ for any real $n$ |
| Product rule | $(uv)' = u'v + uv'$ |
| Quotient rule | $\left(\dfrac{u}{v}\right)' = \dfrac{u'v-uv'}{v^2}$ |
| Chain rule | $\dfrac{dy}{dx} = \dfrac{dy}{du}\dfrac{du}{dx}$; for composite functions |
| Second derivative | Derivative of the derivative; measures concavity, or acceleration in time |
| Concave up / down | $f'' > 0$ / $f'' < 0$; curvature direction |
| Implicit differentiation | Differentiating a relation without solving for $y$ first; each $y$ term contributes $\frac{dy}{dx}$ |
| Sensitivity | A derivative read as the change in output per unit change in input |
| Linear estimate | $\Delta y \approx \dfrac{dy}{dx}\Delta x$; the tangent-line approximation to a small change |

---

## Review Questions

### Conceptual

1. Write the difference quotient for a general function $f$ at the point $a$.
   Explain what quantity it represents before the limit is taken, and what
   changes when the limit is taken.
2. Explain the geometric relationship between the secant lines and the
   tangent line as $h \to 0$.
3. State the units of $\frac{dT}{dx}$ if $T$ is temperature in °C and $x$ is
   position in metres. Explain why this is a useful error check.
4. A function is continuous at $x = 3$. Can you conclude it is differentiable
   there? A function is differentiable at $x = 3$. Can you conclude it is
   continuous there? Justify both answers.
5. Give an engineering example of a function with a genuine corner, and
   explain what the corner means physically.
6. Explain why $\frac{d}{dx}(uv) \ne u'v'$, using a specific two-function
   counterexample.
7. Explain in words what the chain rule instructs you to do, and state the
   most common way it is misapplied.
8. Why is the derivative of $e^x$ equal to $e^x$? What property of the number
   $e$ makes this true?
9. In implicit differentiation, explain why $\frac{d}{dx}(y^2) = 2y
   \frac{dy}{dx}$ rather than $2y$.
10. A particle's position is $s(t)$. State which derivative gives velocity and
    which gives acceleration, and explain what it means physically when the
    second derivative is zero but the first is not.

### Calculation

11. Compute each derivative from the definition:
    (a) $f(x) = 4x^2 + x$
    (b) $f(x) = \dfrac{1}{x+2}$

12. Differentiate using the basic rules:
    (a) $y = 7x^5 - 4x^3 + 2x - 9$
    (b) $y = \dfrac{4}{x^3} + 3\sqrt{x}$
    (c) $y = \dfrac{2x^4 - 6x^2}{x}$ (simplify before differentiating)
    (d) $y = \sqrt[3]{x^4}$

13. Apply the product rule:
    (a) $y = \left(x^2+3\right)\left(2x-5\right)$ — then check by expanding
    (b) $y = x\ln x$
    (c) $y = e^{2x}\cos x$

14. Apply the quotient rule:
    (a) $y = \dfrac{x^2}{x-1}$
    (b) $y = \dfrac{\sin x}{x}$
    (c) $y = \dfrac{e^x}{x^2+1}$

15. Apply the chain rule:
    (a) $y = \left(4x^3 - 1\right)^5$
    (b) $y = \sqrt{5x+2}$
    (c) $y = e^{-3x^2}$
    (d) $y = \cos(7x - 4)$
    (e) $y = \ln\left(3x^2+5\right)$
    (f) $y = \tan^2(3x)$

16. Differentiate:
    (a) $y = \sin x\cos x$ — then simplify using an identity from Chapter
    01-11 and differentiate the simplified form as a check
    (b) $y = \dfrac{1}{\sin x}$ — two ways: quotient rule, and as $\csc x$
    (c) $y = 4^x$
    (d) $y = \log_{10}x$
    (e) $y = \arctan(2x)$

17. Find the equations of the tangent and normal lines:
    (a) $y = x^2 - 3x$ at $x = 2$
    (b) $y = e^{-x}$ at $x = 0$
    (c) $y = \ln x$ at $x = 1$

18. Compute the indicated higher derivatives:
    (a) $y = x^5 - 3x^2$; find $y'$, $y''$, $y'''$, $y^{(4)}$
    (b) $y = \sin(2x)$; find $y''$
    (c) $y = e^{-4t}$; find $\ddot{y}$

19. Differentiate implicitly and find $\frac{dy}{dx}$:
    (a) $x^2 - 3xy + y^2 = 7$
    (b) $\sin y = x$ — then use the result to derive
    $\frac{d}{dx}\arcsin x$
    (c) $xe^y = 4$

20. **Engineering application.** A cantilever beam's deflection is modelled
    along its length by

    $$v(x) = -\frac{w}{24EI}\left(x^4 - 4Lx^3 + 6L^2x^2\right)$$

    Treat $w$, $E$, $I$, and $L$ as constants.

    (a) Find $\dfrac{dv}{dx}$, the slope of the deflected shape.
    (b) Find $\dfrac{d^2v}{dx^2}$.
    (c) Evaluate both at $x = 0$ and state what the values tell you about the
    support condition there.
    (d) Evaluate $\dfrac{d^2v}{dx^2}$ at $x = L$ and comment.

21. **Engineering application.** A first-order sensor responds to a step
    input as

    $$y(t) = 24\left(1 - e^{-t/0.35}\right) \text{ mV}, \qquad t \text{ in seconds}$$

    (a) Find $\dfrac{dy}{dt}$ with units.
    (b) Find the initial slope at $t = 0$.
    (c) Show that the tangent line at $t = 0$ reaches the terminal value of
    24 mV at exactly $t = \tau = 0.35$ s. (This is a standard graphical method
    for measuring a time constant from a recorded response.)
    (d) Find the rate of change at $t = 3\tau$ and express it as a percentage
    of the initial rate.

22. **Engineering application.** Head loss in a fitting varies with velocity
    as $h_L = 0.65\,\dfrac{V^2}{2g}$ with $g = 9.81$ m/s², $V$ in m/s, $h_L$
    in metres.

    (a) Find $\dfrac{dh_L}{dV}$ with units.
    (b) Evaluate at $V = 2.4$ m/s.
    (c) Use a linear estimate to predict the change in head loss if velocity
    rises to 2.6 m/s, then compare with the exact recomputation.
    (d) Verify (b) using the power-law sensitivity relation.

23. **Engineering application.** The concentration of a reactant decays as
    $C(t) = 0.80e^{-0.15t}$ mol/L with $t$ in minutes.

    (a) Find the reaction rate $\dfrac{dC}{dt}$ with units.
    (b) Evaluate the rate at $t = 0$ and $t = 10$ min.
    (c) Show that $\dfrac{dC}{dt} = -0.15\,C$, and state in words what that
    relationship means about the decay process.

### Multiple Choice

24. $\dfrac{d}{dx}\left(4x^3 - 2x\right)$ equals:
    A) $12x^2 - 2$
    B) $12x^2 - 2x$
    C) $4x^2 - 2$
    D) $12x^3 - 2$

25. $\dfrac{d}{dx}\sin(3x)$ equals:
    A) $\cos(3x)$
    B) $3\cos(3x)$
    C) $-3\cos(3x)$
    D) $3\sin(3x)$

26. If $f(x) = xe^x$, then $f'(x)$ equals:
    A) $e^x$
    B) $xe^x$
    C) $e^x(1+x)$
    D) $e^x(1-x)$

27. $\dfrac{d}{dx}\ln(5x)$ equals:
    A) $\dfrac{5}{x}$
    B) $\dfrac{1}{5x}$
    C) $\dfrac{1}{x}$
    D) $\dfrac{\ln 5}{x}$

28. A function that is continuous at $x = a$ is:
    A) necessarily differentiable at $a$
    B) not necessarily differentiable at $a$
    C) necessarily discontinuous somewhere else
    D) necessarily equal to its limit at every other point

29. If $s(t)$ is position, then acceleration is:
    A) $\dfrac{ds}{dt}$
    B) $\dfrac{d^2s}{dt^2}$
    C) $\displaystyle\int s\,dt$
    D) $\dfrac{s}{t^2}$

30. $\dfrac{d}{dx}\tan x$ equals:
    A) $\sec x\tan x$
    B) $-\csc^2 x$
    C) $\sec^2 x$
    D) $\cot x$

31. For $y = \dfrac{u}{v}$, the quotient rule gives $\dfrac{dy}{dx}$ equal to:
    A) $\dfrac{u'v + uv'}{v^2}$
    B) $\dfrac{u'v - uv'}{v^2}$
    C) $\dfrac{uv' - u'v}{v^2}$
    D) $\dfrac{u'}{v'}$

---

## Answer Key with Explanations

**1.** The difference quotient is

$$\frac{f(a+h) - f(a)}{h}$$

Before the limit it represents the **average** rate of change of $f$ over the
interval from $a$ to $a+h$ — equivalently, the slope of the secant line
joining the two points on the graph. Taking the limit as $h \to 0$ shrinks the
interval to a single point, converting the average rate into the
**instantaneous** rate at $a$, and converting the secant slope into the
tangent slope. The limit is essential because setting $h = 0$ directly gives
$\frac{0}{0}$. (§17.1)

**2.** As $h$ shrinks, the second point slides along the curve toward the
fixed point. Each secant line through the two points has a slope closer to
the tangent slope, and the secant lines pivot about the fixed point. In the
limit the two points coincide and the secant line becomes the tangent — the
unique line touching the curve at that point with the curve's own slope.
(§17.1, §17.2)

**3.** Units are °C/m — degrees Celsius per metre, a temperature gradient. The
check is useful because it is independent of the algebra: if you differentiate
a temperature profile and the result does not come out in °C/m, you have made
an algebraic error somewhere, and you know it before using the result. The
rule is $\left[\frac{dy}{dx}\right] = \frac{[y]}{[x]}$ always. (§17.3)

**4.** Continuity at $x = 3$ does **not** imply differentiability there.
$f(x) = \lvert x - 3\rvert$ is continuous at 3 and has a corner, so no
derivative exists. Differentiability at $x = 3$ **does** imply continuity
there — the implication runs one way. Differentiability is the stronger
condition. (§17.4)

**5.** Several valid answers. A shear diagram has a corner (in fact a jump in
the diagram itself, and a corner in the moment diagram) at every concentrated
load. A stress–strain curve has a corner at the yield point where the slope
drops abruptly from the elastic modulus to the much smaller plastic slope. A
saturating control signal has corners at the saturation limits.

Physically the corner means the *rate* changes abruptly — the material's
stiffness, or the system's responsiveness, switches to a different value at
that threshold. The derivative genuinely does not exist there, and a model
that smooths it over is hiding real behaviour. (§17.4)

**6.** Take $u = v = x$. Then $uv = x^2$ with derivative $2x$. But
$u'v' = (1)(1) = 1$. These disagree for every $x$ except $x = \frac12$.

The correct product rule gives $u'v + uv' = (1)(x) + (x)(1) = 2x$ ✓ The reason
the naive version fails is that changing a product changes it through *both*
factors, and both contributions must be counted. (§17.6)

**7.** The chain rule instructs: differentiate the outer function while leaving
the inner function untouched, then multiply by the derivative of the inner
function. For nested compositions, repeat from the outside in and multiply all
the factors together.

The most common misapplication is **not noticing a composition is present**
and omitting the inner derivative entirely. $\frac{d}{dx}\sin(3x) = 3\cos(3x)$;
writing $\cos(3x)$ drops the factor of 3. Expressions like $e^{-2t}$,
$(x^2+1)^5$, and $\sqrt{3x}$ are all compositions and all need the extra
factor. (§17.6)

**8.** Because $e$ is *defined* as the base for which

$$\lim_{h\to 0}\frac{e^h - 1}{h} = 1$$

Substituting into the difference quotient:

$$\frac{e^{x+h}-e^x}{h} = \frac{e^x\left(e^h - 1\right)}{h} = e^x\cdot\frac{e^h-1}{h} \longrightarrow e^x(1) = e^x$$

The factor $e^x$ comes out because $e^{x+h} = e^xe^h$ (the exponent law from
Chapter 01-05), and the remaining limit is 1 by the defining property. For any
other base $a$ that limit equals $\ln a$ instead of 1, which is where the
extra factor in $\frac{d}{dx}a^x = a^x\ln a$ comes from. (§17.7)

**9.** Because in implicit differentiation $y$ is understood to be a function
of $x$, not an independent variable. So $y^2$ is a composition: the outer
function is $(\;)^2$ and the inner function is $y(x)$. The chain rule then
requires multiplying by the derivative of the inner function, which is
$\frac{dy}{dx}$:

$$\frac{d}{dx}\left(y^2\right) = 2y\cdot\frac{dy}{dx}$$

Writing $2y$ alone would be correct only if we were differentiating with
respect to $y$. (§17.9)

**10.** Velocity is the **first** derivative, $v = \frac{ds}{dt}$.
Acceleration is the **second**, $a = \frac{d^2s}{dt^2}$.

If $a = 0$ but $v \ne 0$, the particle is moving at constant velocity — it is
still going somewhere, but its speed and direction are not changing at that
instant. On a velocity-versus-time plot this is the moment the curve is flat,
which means velocity is at a local maximum or minimum. In Worked Example 9
this occurred at $t = 2$ s, where the particle was moving backward at its
fastest rate of 3 m/s. (§17.8)

**11.**

**(a)** $f(x) = 4x^2 + x$

$$f(x+h) = 4\left(x^2+2xh+h^2\right) + x + h = 4x^2 + 8xh + 4h^2 + x + h$$

$$f(x+h) - f(x) = 8xh + 4h^2 + h = h(8x + 4h + 1)$$

$$\frac{f(x+h)-f(x)}{h} = 8x + 4h + 1 \longrightarrow \boxed{8x+1}$$

Check with the power rule: $8x + 1$ ✓

**(b)** $f(x) = \dfrac{1}{x+2}$

$$f(x+h) - f(x) = \frac{1}{x+h+2} - \frac{1}{x+2} = \frac{(x+2)-(x+h+2)}{(x+h+2)(x+2)} = \frac{-h}{(x+h+2)(x+2)}$$

Divide by $h$:

$$\frac{-1}{(x+h+2)(x+2)} \longrightarrow \frac{-1}{(x+2)^2} = \boxed{-\frac{1}{(x+2)^2}}$$

Check with the power and chain rules: $\frac{d}{dx}(x+2)^{-1} = -(x+2)^{-2}(1)$ ✓

**12.**

**(a)** $\boxed{35x^4 - 12x^2 + 2}$

**(b)** Rewrite: $y = 4x^{-3} + 3x^{1/2}$

$$\frac{dy}{dx} = -12x^{-4} + \tfrac32 x^{-1/2} = \boxed{-\frac{12}{x^4} + \frac{3}{2\sqrt{x}}}$$

**(c)** Simplify first: $y = 2x^3 - 6x$ (valid for $x \ne 0$)

$$\frac{dy}{dx} = \boxed{6x^2 - 6}$$

Doing this with the quotient rule gives the same answer with considerably more
work — always simplify before differentiating when you can.

**(d)** $y = x^{4/3}$

$$\frac{dy}{dx} = \tfrac43 x^{1/3} = \boxed{\frac{4\sqrt[3]{x}}{3}}$$

**13.**

**(a)** $u = x^2+3$, $u' = 2x$; $v = 2x-5$, $v' = 2$

$$\frac{dy}{dx} = 2x(2x-5) + \left(x^2+3\right)(2) = 4x^2 - 10x + 2x^2 + 6 = \boxed{6x^2 - 10x + 6}$$

Check by expanding: $y = 2x^3 - 5x^2 + 6x - 15$, so
$\frac{dy}{dx} = 6x^2 - 10x + 6$ ✓

**(b)** $u = x$, $u' = 1$; $v = \ln x$, $v' = \frac1x$

$$\frac{dy}{dx} = \ln x + x\left(\frac1x\right) = \boxed{\ln x + 1}$$

**(c)** $u = e^{2x}$, $u' = 2e^{2x}$; $v = \cos x$, $v' = -\sin x$

$$\frac{dy}{dx} = 2e^{2x}\cos x - e^{2x}\sin x = \boxed{e^{2x}\left(2\cos x - \sin x\right)}$$

**14.**

**(a)** $u = x^2$, $u' = 2x$; $v = x-1$, $v' = 1$

$$\frac{dy}{dx} = \frac{2x(x-1) - x^2(1)}{(x-1)^2} = \frac{2x^2-2x-x^2}{(x-1)^2} = \boxed{\frac{x^2-2x}{(x-1)^2} = \frac{x(x-2)}{(x-1)^2}}$$

**(b)** $$\frac{dy}{dx} = \frac{x\cos x - \sin x}{x^2}$$

$$\boxed{\frac{x\cos x - \sin x}{x^2}}$$

**(c)** $$\frac{dy}{dx} = \frac{e^x\left(x^2+1\right) - e^x(2x)}{\left(x^2+1\right)^2} = \boxed{\frac{e^x\left(x^2-2x+1\right)}{\left(x^2+1\right)^2} = \frac{e^x(x-1)^2}{\left(x^2+1\right)^2}}$$

**15.**

**(a)** $\frac{dy}{dx} = 5\left(4x^3-1\right)^4\left(12x^2\right) =
\boxed{60x^2\left(4x^3-1\right)^4}$

**(b)** $y = (5x+2)^{1/2}$;
$\frac{dy}{dx} = \tfrac12(5x+2)^{-1/2}(5) = \boxed{\dfrac{5}{2\sqrt{5x+2}}}$

**(c)** $\frac{dy}{dx} = e^{-3x^2}(-6x) = \boxed{-6xe^{-3x^2}}$

**(d)** $\frac{dy}{dx} = -\sin(7x-4)(7) = \boxed{-7\sin(7x-4)}$

**(e)** Inner derivative over inner function:
$\boxed{\dfrac{6x}{3x^2+5}}$

**(f)** $y = \left[\tan(3x)\right]^2$; three layers:

$$\frac{dy}{dx} = 2\tan(3x)\cdot\sec^2(3x)\cdot 3 = \boxed{6\tan(3x)\sec^2(3x)}$$

**16.**

**(a)** Product rule:

$$\frac{dy}{dx} = \cos x\cos x + \sin x(-\sin x) = \cos^2 x - \sin^2 x$$

By the double-angle identity from Chapter 01-11 this is $\boxed{\cos 2x}$.

Check via the simplified form: $\sin x\cos x = \frac12\sin 2x$, so

$$\frac{dy}{dx} = \tfrac12\cos(2x)(2) = \cos 2x \;\checkmark$$

**(b)** Quotient rule on $\dfrac{1}{\sin x}$:

$$\frac{dy}{dx} = \frac{0 \cdot \sin x - 1 \cdot \cos x}{\sin^2 x} = \frac{-\cos x}{\sin^2 x}$$

As $\csc x$: $\frac{d}{dx}\csc x = -\csc x\cot x = -\frac{1}{\sin x}\cdot
\frac{\cos x}{\sin x} = \frac{-\cos x}{\sin^2 x}$ ✓

$$\boxed{-\csc x\cot x = \frac{-\cos x}{\sin^2 x}}$$

**(c)** $\boxed{4^x\ln 4}$

**(d)** $\boxed{\dfrac{1}{x\ln 10}}$

**(e)** $\frac{dy}{dx} = \dfrac{1}{1+(2x)^2}\cdot 2 = \boxed{\dfrac{2}{1+4x^2}}$

**17.**

**(a)** $y(2) = 4 - 6 = -2$; $y' = 2x - 3$, so $y'(2) = 1$

Tangent: $y + 2 = 1(x-2) \implies \boxed{y = x - 4}$

Normal: slope $-1$, so $y + 2 = -1(x-2) \implies \boxed{y = -x}$

Check both pass through $(2,-2)$: $2-4 = -2$ ✓; $-2$ ✓

**(b)** $y(0) = 1$; $y' = -e^{-x}$, so $y'(0) = -1$

Tangent: $y - 1 = -1(x-0) \implies \boxed{y = 1 - x}$

Normal: slope $+1$, so $\boxed{y = x + 1}$

**(c)** $y(1) = 0$; $y' = \frac1x$, so $y'(1) = 1$

Tangent: $y - 0 = 1(x-1) \implies \boxed{y = x - 1}$

Normal: slope $-1$, so $y = -(x-1) \implies \boxed{y = 1 - x}$

**18.**

**(a)** $y' = 5x^4 - 6x$; $y'' = 20x^3 - 6$; $y''' = 60x^2$;
$y^{(4)} = \boxed{120x}$ (with the earlier three as shown)

**(b)** $y' = 2\cos 2x$; $y'' = -4\sin 2x$

$$\boxed{y'' = -4\sin 2x = -4y}$$

Note that $y'' = -4y$. Any sinusoid satisfies a relationship of this form, and
it is the reason sinusoids are the natural solutions of vibration problems.

**(c)** $\dot{y} = -4e^{-4t}$; $\ddot{y} = \boxed{16e^{-4t}}$

**19.**

**(a)** Differentiate, using the product rule on the $3xy$ term:

$$2x - 3\left(y + x\frac{dy}{dx}\right) + 2y\frac{dy}{dx} = 0$$

$$2x - 3y - 3x\frac{dy}{dx} + 2y\frac{dy}{dx} = 0$$

$$\frac{dy}{dx}\left(2y - 3x\right) = 3y - 2x$$

$$\boxed{\frac{dy}{dx} = \frac{3y-2x}{2y-3x}}$$

**(b)** $\sin y = x$. Differentiate:

$$\cos y\frac{dy}{dx} = 1 \implies \frac{dy}{dx} = \frac{1}{\cos y}$$

Since $y = \arcsin x$, we need $\cos y$ in terms of $x$. From the Pythagorean
identity, $\cos y = \sqrt{1 - \sin^2 y} = \sqrt{1-x^2}$ — positive, because
$\arcsin$ has range $[-90°, 90°]$ where cosine is non-negative (Chapter 01-11).

$$\boxed{\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}} \;\checkmark$$

This matches the table in §17.7, now derived rather than asserted.

**(c)** $xe^y = 4$. Product rule on the left:

$$e^y + xe^y\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{e^y}{xe^y} = \boxed{-\frac{1}{x}}$$

Check explicitly: $e^y = 4/x$, so $y = \ln 4 - \ln x$, giving
$\frac{dy}{dx} = -\frac1x$ ✓

**20.**

**(a)** Differentiate term by term, treating $\frac{w}{24EI}$ as a constant:

$$\frac{dv}{dx} = -\frac{w}{24EI}\left(4x^3 - 12Lx^2 + 12L^2x\right)$$

$$= \boxed{-\frac{w}{6EI}\left(x^3 - 3Lx^2 + 3L^2x\right)}$$

**(b)** $$\frac{d^2v}{dx^2} = -\frac{w}{6EI}\left(3x^2 - 6Lx + 3L^2\right) = \boxed{-\frac{w}{2EI}\left(x^2 - 2Lx + L^2\right) = -\frac{w}{2EI}(x-L)^2}$$

**(c)** At $x = 0$:

$$\frac{dv}{dx}\bigg|_0 = -\frac{w}{6EI}(0) = 0 \qquad v(0) = 0$$

Both the deflection and the slope are zero at $x = 0$. A support that permits
neither displacement nor rotation is a **fixed** (built-in) support — which is
exactly what "cantilever" means. The mathematics of the model encodes the
boundary condition.

$$\frac{d^2v}{dx^2}\bigg|_0 = -\frac{w}{2EI}(0-L)^2 = -\frac{wL^2}{2EI}$$

Nonzero and largest in magnitude here.

**(d)** At $x = L$:

$$\frac{d^2v}{dx^2}\bigg|_L = -\frac{w}{2EI}(L-L)^2 = \boxed{0}$$

The second derivative vanishes at the free end. Since curvature is
proportional to bending moment, this says the bending moment is zero at a free
end — which is correct, because there is nothing beyond the tip to resist.
The second derivative is maximum at the fixed support and zero at the free
tip, matching the physical expectation that a cantilever is most heavily
stressed where it is anchored.

**21.**

**(a)** $$\frac{dy}{dt} = 24\cdot\frac{1}{0.35}e^{-t/0.35} = \boxed{68.57\,e^{-t/0.35} \text{ mV/s}}$$

Units: mV/s ✓ (24 mV divided by 0.35 s)

**(b)** At $t = 0$: $\boxed{68.57 \text{ mV/s}}$

**(c)** The tangent at $t = 0$ passes through $(0, 0)$ with slope 68.57 mV/s:

$$y_{\text{tan}}(t) = 68.57\,t$$

Set equal to the terminal value 24 mV:

$$68.57\,t = 24 \implies t = \frac{24}{68.57} = 0.350 \text{ s} = \tau \;\checkmark$$

Algebraically this is guaranteed: the initial slope is $\frac{y_\infty}{\tau}$,
so the tangent reaches $y_\infty$ after exactly $\tau$. This is the standard
graphical method for reading a time constant off a recorded step response —
draw the initial tangent, find where it crosses the final value, read $\tau$
on the time axis.

**(d)** At $t = 3\tau$: $e^{-3} = 0.049787$

$$\frac{dy}{dt} = 68.57(0.049787) = \boxed{3.41 \text{ mV/s}}$$

As a percentage of the initial rate: $e^{-3} = \boxed{4.98\%}$

The rate has fallen to about 5% of its initial value after three time
constants — consistent with the response being about 95% complete there.

**22.**

**(a)** $h_L = \dfrac{0.65}{2(9.81)}V^2 = 0.033129\,V^2$

$$\frac{dh_L}{dV} = 0.066259\,V \quad \boxed{\text{units: m per (m/s), i.e. s}}$$

The units simplify to seconds, which looks odd but is correct: metres of head
per metre-per-second of velocity.

**(b)** At $V = 2.4$ m/s:

$$\frac{dh_L}{dV} = 0.066259(2.4) = \boxed{0.15902 \text{ s}}$$

**(c)** Linear estimate with $\Delta V = 0.2$ m/s:

$$\Delta h_L \approx 0.15902(0.2) = \boxed{0.03180 \text{ m}}$$

Exact recomputation:

$$h_L(2.4) = 0.033129(5.76) = 0.190823 \text{ m}$$
$$h_L(2.6) = 0.033129(6.76) = 0.223952 \text{ m}$$
$$\Delta h_L = 0.033129 \text{ m}$$

The estimate of 0.03180 m is 4.0% low. The function is concave up (a
parabola), so the tangent line underestimates — same behaviour as Worked
Example 11.

**(d)** Power-law relation with $n = 2$:

$$\frac{h_L}{V} = \frac{0.190823}{2.4} = 0.0795$$

$$2 \times 0.0795 = 0.1590 \text{ s} \;\checkmark$$

Matches (b) exactly.

**23.**

**(a)** $$\frac{dC}{dt} = 0.80(-0.15)e^{-0.15t} = \boxed{-0.12\,e^{-0.15t} \text{ mol/(L·min)}}$$

Negative, as it must be for a decaying concentration.

**(b)** At $t = 0$: $\boxed{-0.12 \text{ mol/(L·min)}}$

At $t = 10$ min: $e^{-1.5} = 0.223130$

$$\frac{dC}{dt} = -0.12(0.223130) = \boxed{-0.02678 \text{ mol/(L·min)}}$$

**(c)** Since $C = 0.80e^{-0.15t}$:

$$-0.15\,C = -0.15\left(0.80e^{-0.15t}\right) = -0.12e^{-0.15t} = \frac{dC}{dt} \;\checkmark$$

In words: **the rate of decay is proportional to the amount remaining.** The
more reactant is present, the faster it disappears; as it depletes, the rate
slows in exact proportion. This is the defining characteristic of a
first-order process, and it is why the solution is an exponential. Every
first-order decay in engineering — radioactive decay, first-order reactions,
capacitor discharge, Newton's law of cooling — obeys a relationship of this
form.

**24. A — $12x^2 - 2$.** Power rule term by term: $\frac{d}{dx}4x^3 = 12x^2$
and $\frac{d}{dx}(-2x) = -2$. Choice B fails to reduce the exponent on the
second term; choice D fails to reduce it on the first. (§17.5)

**25. B — $3\cos(3x)$.** Chain rule: outer derivative $\cos(3x)$ times inner
derivative 3. Choice A is the classic omission of the inner derivative — the
most common derivative error there is. (§17.6, §17.7)

**26. C — $e^x(1+x)$.** Product rule with $u = x$, $v = e^x$:
$f' = (1)e^x + x(e^x) = e^x + xe^x = e^x(1+x)$. Choice A and B are the two
halves of the correct answer, each on its own. (§17.6)

**27. C — $\dfrac{1}{x}$.** Two routes agree. Chain rule:
$\frac{5}{5x} = \frac1x$. Or apply the log law first:
$\ln(5x) = \ln 5 + \ln x$, and $\ln 5$ is a constant, so the derivative is
$\frac1x$. A multiplicative constant inside a logarithm has no effect on the
derivative. Choice A forgets to include the 5 in the denominator; choice B
inverts the chain rule. (§17.7)

**28. B — not necessarily differentiable at $a$.** Continuity is the weaker
condition. $\lvert x - a\rvert$ is continuous at $a$ with a corner there, so
no derivative exists. The implication runs the other way: differentiable
$\Rightarrow$ continuous. (§17.4)

**29. B — $\dfrac{d^2s}{dt^2}$.** Velocity is the first derivative of
position; acceleration is the derivative of velocity, hence the second
derivative of position. Choice A is velocity. (§17.8)

**30. C — $\sec^2 x$.** Derived by the quotient rule on
$\frac{\sin x}{\cos x}$ together with the Pythagorean identity. Choice A is
$\frac{d}{dx}\sec x$; choice B is $\frac{d}{dx}\cot x$. (§17.7)

**31. B — $\dfrac{u'v - uv'}{v^2}$.** Choice A has the product-rule sign
(plus instead of minus); choice C has the numerator order reversed, which
flips the sign of the whole result; choice D is not a valid rule at all.
(§17.6)

---

## Quick Reference

**Definition** — *Handbook, Differential Calculus*

$$f'(x) = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h} \qquad \left[\frac{dy}{dx}\right] = \frac{[y]}{[x]}$$

**Tangent and normal at $x = a$**

$$y - f(a) = f'(a)(x-a) \qquad m_{\text{norm}} = -\frac{1}{f'(a)}$$

**Reading the derivative**

| $f'$ | $f$ | | $f''$ | $f$ |
|---|---|---|---|---|
| $> 0$ | rising | | $> 0$ | concave up |
| $< 0$ | falling | | $< 0$ | concave down |
| $= 0$ | flat spot | | | |

**Basic rules** — *Handbook, derivative table*

$$\frac{d}{dx}c = 0 \qquad \frac{d}{dx}x^n = nx^{n-1} \qquad \frac{d}{dx}\left[cf\right] = cf'$$

$$\frac{d}{dx}\left[f \pm g\right] = f' \pm g'$$

**The three rules that matter**

$$(uv)' = u'v + uv' \qquad \left(\frac{u}{v}\right)' = \frac{u'v-uv'}{v^2} \qquad \frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dx}$$

**Transcendental derivatives** — *Handbook, derivative table*

| $f$ | $f'$ | | $f$ | $f'$ |
|---|---|---|---|---|
| $\sin x$ | $\cos x$ | | $e^x$ | $e^x$ |
| $\cos x$ | $-\sin x$ | | $a^x$ | $a^x\ln a$ |
| $\tan x$ | $\sec^2 x$ | | $\ln x$ | $1/x$ |
| $\cot x$ | $-\csc^2 x$ | | $\log_a x$ | $1/(x\ln a)$ |
| $\sec x$ | $\sec x\tan x$ | | $\arcsin x$ | $1/\sqrt{1-x^2}$ |
| $\csc x$ | $-\csc x\cot x$ | | $\arccos x$ | $-1/\sqrt{1-x^2}$ |
| | | | $\arctan x$ | $1/(1+x^2)$ |

Co-functions carry the minus sign. **Radians only.**

**Chain rule forms — use these directly**

$$\frac{d}{dx}\sin u = u'\cos u \qquad \frac{d}{dx}e^u = u'e^u \qquad \frac{d}{dx}\ln u = \frac{u'}{u} \qquad \frac{d}{dx}u^n = nu^{n-1}u'$$

**Implicit differentiation**

Differentiate both sides with respect to $x$; each $y$ term contributes a
factor $\frac{dy}{dx}$; solve algebraically.

$$\frac{d}{dx}\left(y^n\right) = ny^{n-1}\frac{dy}{dx}$$

**Kinematics**

$$v = \frac{ds}{dt} = \dot{s} \qquad a = \frac{dv}{dt} = \frac{d^2s}{dt^2} = \ddot{s}$$

**Linear estimate and power-law sensitivity**

$$\Delta y \approx \frac{dy}{dx}\Delta x \qquad \text{for } y = kx^n: \; \frac{dy/dx}{y/x} = n$$

**Not in the Handbook — memorize**

Units rule as an error check · differentiable ⟹ continuous (not conversely) ·
the four non-differentiability modes · $f'$ and $f''$ interpretation tables ·
kinematic chain · tangent/normal construction · co-function sign pattern ·
multi-layer chain peeling procedure · constant inside a log is irrelevant ·
power-law sensitivity relation · linear estimate

---

## What's Next

Apprentice, you can differentiate. Powers, products, quotients, chains,
trig, exponentials, logs, implicit relations, higher orders. That is the
computational core of differential calculus and it is now yours.

In **Chapter 01-18: Applications of the Derivative**, we put it to work. The
fact that $f' = 0$ at a flat spot becomes a method for finding maxima and
minima — which is how you find the maximum stress in a member, the most
economical pipe diameter, the peak of a response curve. The second derivative
distinguishes a peak from a valley. Related rates connect one changing
quantity to another through a geometric constraint, which is how you turn "the
tank is filling at 3 L/s" into "the level is rising at 4 mm/s." And
L'Hôpital's rule finally arrives, giving you a derivative-based shortcut for
the indeterminate forms you resolved algebraically in Chapter 01-16.

One structural note. Chapter 01-18 is where the substrate starts paying real
dividends, because optimization problems are the first place you will solve a
recognizably *engineering* question end to end using nothing but tools from
Tier 1. Read a word problem, build a function, differentiate, set to zero,
verify with the second derivative, check the units. That whole sequence uses
Chapters 01-02 through 01-17 and nothing else.

Bring the Handbook open to the derivative table. You will want it beside you.

See you there.

— Your Mentor