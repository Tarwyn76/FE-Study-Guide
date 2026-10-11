---
chapter: "01-19"
title: "Antiderivatives and the Definite Integral"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-019-01, MATH-1C-019-02, MATH-1C-019-03, MATH-1C-019-04, MATH-1C-019-05]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-19: Antiderivatives and the Definite Integral

> *"Differentiation takes a total and gives you a rate. Integration takes a rate
> and gives you back the total. That is the whole relationship, and it is the
> single most useful fact in engineering mathematics — because rates are what we
> can measure and totals are what we get paid for. A flowmeter reads a rate; the
> bill is for the volume. A load diagram gives force per metre; the reaction is
> the total. Learn to run the machine backward and half of engineering opens
> up."*

---

## Before You Start

**Prerequisites:** [01-05 Exponents, Radicals, and Logarithms](01-05-exponents-radicals-logarithms.md) · [01-07 Polynomials and Their Roots](01-07-polynomials-roots.md) · [01-11 Trigonometry](01-11-trigonometry.md) · [01-15 Sequences, Series, and Progressions](01-15-sequences-series-progressions.md) · [01-16 Limits and Continuity](01-16-limits-continuity.md) · [01-17 The Derivative](01-17-the-derivative.md) · [01-18 Applications of the Derivative](01-18-applications-of-the-derivative.md)

**Skip if:** You pass the Tier 1C test-out quiz. Verify you can integrate a
power including the $n = -1$ exception, carry out a substitution with changed
limits, and state both parts of the Fundamental Theorem before skipping.
Substitution is the most commonly rusty item — specifically, remembering to
convert $dx$ into $du$ rather than just swapping the variable name.

**Time:** ~70 min read · ~25 min review questions · ~75 min practice problems

---

## On the Board Today

Apprentice, we now run the machine in reverse.

Chapter 01-17 answered: given a function, what is its rate of change?
This chapter answers the opposite question: **given a rate of change, what is
the function?** That operation is called **antidifferentiation**, and it is the
first of the two things "integration" means.

The second thing it means looks unrelated. Suppose you want the **area** under a
curve. Rectangles get you an approximation; more and thinner rectangles get you a
better one; a limit gets you the exact answer. That construction is the
**definite integral**, and on its face it has nothing whatever to do with
reversing a derivative.

The astonishing fact — and it genuinely is astonishing, it took mathematics
centuries to find — is that these two operations are the same operation. Reversing
a derivative *computes areas*. Accumulating area *reverses derivatives*. The
statement of that equivalence is the **Fundamental Theorem of Calculus**, and it
is the reason integration is practical rather than an infinite-summation chore.

Here is why an engineer should care, stated without any calculus at all.

You can measure rates. Flowmeters, thermocouples with a gradient, strain gauges,
accelerometers, load cells reading force per unit length — instrumentation
overwhelmingly produces rates and densities, not totals. But the quantities that
matter to a design are totals: the volume that passed, the heat that crossed the
boundary, the reaction force at the support, the distance travelled, the mass in
the vessel, the centroid of the section, the energy consumed over a shift.

Integration is the bridge from what you can measure to what you need to know.
Every one of those totals is an integral of something measurable.

We build antiderivatives first, then the area construction, then the theorem
that connects them, then the one technique — substitution — that makes a large
fraction of real integrals tractable. Areas, volumes, centroids, and the rest of
the applications are Chapter 01-20. This chapter builds the tool.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 19.1 Define an antiderivative and explain why the constant of integration is
  required
* 19.2 Apply the basic integration rules for powers, exponentials, logarithms,
  and trigonometric functions
* 19.3 Handle the $n = -1$ exception to the power rule and explain why the
  absolute value appears
* 19.4 Construct a Riemann sum for a function on an interval and evaluate a
  definite integral as the limit of Riemann sums
* 19.5 Interpret the definite integral as signed area and determine the sign of
  a contribution
* 19.6 Apply the properties of definite integrals, including reversal of limits
  and additivity over subintervals
* 19.7 State both parts of the Fundamental Theorem of Calculus and explain what
  each one does
* 19.8 Evaluate definite integrals using antiderivatives and the evaluation
  notation
* 19.9 Differentiate an accumulation function using the second part of the
  Fundamental Theorem
* 19.10 Integrate by substitution, recognizing when the technique applies
* 19.11 Change the limits of integration when substituting in a definite
  integral
* 19.12 Exploit even and odd symmetry to simplify definite integrals over
  symmetric intervals
* 19.13 Compute the average value of a function over an interval and interpret
  it physically

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $\displaystyle\int f(x)\,dx$ | indefinite integral (antiderivative family) | result is a **family** of functions |
| $\displaystyle\int_a^b f(x)\,dx$ | definite integral from $a$ to $b$ | result is a **number** |
| $C$ | constant of integration | never optional on an indefinite integral |
| $F(x)$ | an antiderivative of $f(x)$ | so $F'(x) = f(x)$ |
| $dx$ | differential of the integration variable | tells you *what* you are integrating with respect to |
| $\big[F(x)\big]_a^b$ | evaluation notation | means $F(b) - F(a)$ |
| $\Delta x$ | width of a subinterval | $= \dfrac{b-a}{n}$ for equal subdivisions |
| $x_k$, $x_k^*$ | subinterval endpoint; sample point in subinterval $k$ | — |
| $n$ | number of subintervals | driven to infinity in the limit |
| $u$ | substitution variable | $u = g(x)$ |
| $\bar{f}$ | average value of $f$ over an interval | a single number |
| $a \to b$ | direction of integration | reversing it flips the sign |

> ---
> **Mentor's Margin**
>
> The two integrals look almost identical and produce completely different kinds
> of object. Keep them straight from the first day.
>
> $\int f(x)\,dx$ has no limits, and its answer is a **family of functions** with
> a $+C$ attached. It is an antiderivative.
>
> $\int_a^b f(x)\,dx$ has limits, and its answer is a **single number**. No $+C$
> — the constant cancels in the subtraction, as we will see.
>
> If you produce a function where a number was asked for, or write $+C$ on a
> definite integral, you have confused the two. The difference is two little
> symbols on the integral sign, and it changes everything about the answer.
>
> ---

---

## 19.1 Antiderivatives and the Constant of Integration

$F$ is an **antiderivative** of $f$ if

$$F'(x) = f(x)$$

For instance, $F(x) = x^3$ is an antiderivative of $f(x) = 3x^2$, because
differentiating $x^3$ gives $3x^2$.

But so is $x^3 + 7$. And $x^3 - 2.5$. And $x^3 + 1000$. The derivative of a
constant is zero (Chapter 01-17), so adding any constant leaves the derivative
untouched.

That is not an inconvenience; it is the complete story. If two functions have the
same derivative everywhere on an interval, they differ by a constant — and this
follows directly from the Mean Value Theorem of Chapter 01-18. Let
$H = F - G$ with $F' = G'$. Then $H' = 0$ everywhere, so by the MVT any two
points give $H(x_2) - H(x_1) = H'(c)(x_2-x_1) = 0$, meaning $H$ never changes
value. $H$ is a constant.

So antiderivatives come in families, each member a vertical translate of the
others:

$$\boxed{\int f(x)\,dx = F(x) + C}$$

The **constant of integration** $C$ is not decoration. Leaving it off is a wrong
answer, because it claims one specific member of the family when the information
given picks out none.

![FIG-01-19-001: A family of five parallel curves y = x³ + C for C = −4, −2, 0, 2, 4, drawn on one set of axes. At a common x-value, a short tangent segment is drawn on each curve; all five tangent segments are visibly parallel, and a callout reads "same slope 3x² on every member". A vertical double-headed arrow between two adjacent curves is labeled "vertical shift = difference in C". Below, a note reads "one derivative, infinitely many antiderivatives".](../figures/FIG-01-19-001-antiderivative-family.png)

### Recovering the constant

Physical problems usually supply one extra fact — an **initial condition** — that
pins $C$ down. That is what makes the family collapse to a single function.

### Worked Example 1 — Antiderivative with an Initial Condition

**Given.** A particle has velocity $v(t) = 6t - 4$ m/s and is at position
$s = 10$ m when $t = 0$.

**Find.** The position function $s(t)$.

**Solution.**

Position is an antiderivative of velocity, since $v = \frac{ds}{dt}$:

$$s(t) = \int (6t-4)\,dt = 3t^2 - 4t + C$$

Apply the initial condition $s(0) = 10$:

$$3(0) - 4(0) + C = 10 \implies C = 10$$

$$\boxed{s(t) = 3t^2 - 4t + 10 \text{ m}}$$

**Check.** Differentiate: $s'(t) = 6t - 4 = v(t)$ ✓ And $s(0) = 10$ ✓

Without the initial condition, every function $3t^2 - 4t + C$ would be an equally
valid velocity match — they all describe the same *motion*, just started from a
different place.

---

## 19.2 The Basic Integration Rules

Every rule below is a derivative rule from Chapter 01-17 read backwards. That is
worth saying plainly: **there is nothing new to learn here**, only a direction to
reverse. Verify any entry by differentiating the right-hand side.

### Linearity

$$\boxed{\int c\,f(x)\,dx = c\int f(x)\,dx \qquad \int \big[f(x) \pm g(x)\big]\,dx = \int f(x)\,dx \pm \int g(x)\,dx}$$

Integration passes through scalar multiples and splits across addition, exactly
as differentiation does. And exactly as with differentiation, it does **not**
pass through products or quotients. There is no "product rule for integrals" that
splits $\int uv\,dx$ into anything simple.

### The power rule

$$\boxed{\int x^n\,dx = \frac{x^{n+1}}{n+1} + C \qquad n \ne -1}$$

Raise the exponent by one, divide by the new exponent. The reverse of "bring down
and reduce."

Check by differentiating: $\frac{d}{dx}\frac{x^{n+1}}{n+1} =
\frac{(n+1)x^n}{n+1} = x^n$ ✓

### The $n = -1$ exception

At $n = -1$ the formula divides by zero, so it cannot apply. The correct
antiderivative comes from the logarithm derivative:

$$\boxed{\int x^{-1}\,dx = \int\frac{1}{x}\,dx = \ln\lvert x\rvert + C}$$

The absolute value matters. $\ln x$ is defined only for $x > 0$, but $\frac{1}{x}$
exists for negative $x$ too, and needs an antiderivative there. For $x < 0$,
differentiating $\ln(-x)$ by the chain rule gives $\frac{-1}{-x} = \frac{1}{x}$ ✓
The absolute value packages both cases in one expression.

### The complete table

| $f(x)$ | $\displaystyle\int f(x)\,dx$ |
|---|---|
| $x^n$, $n \ne -1$ | $\dfrac{x^{n+1}}{n+1} + C$ |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\dfrac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\csc^2 x$ | $-\cot x + C$ |
| $\sec x\tan x$ | $\sec x + C$ |
| $\csc x\cot x$ | $-\csc x + C$ |
| $\dfrac{1}{\sqrt{1-x^2}}$ | $\arcsin x + C$ |
| $\dfrac{1}{1+x^2}$ | $\arctan x + C$ |

> ---
> **Mentor's Margin**
>
> Watch the sign flip in the trigonometric pair. Differentiating cosine
> introduces a minus sign, so integrating sine *inherits* it:
> $\int\sin x\,dx = -\cos x + C$. Meanwhile $\int\cos x\,dx = +\sin x + C$.
>
> That crossed pattern catches people constantly, in both directions. The cure is
> not memorizing harder — it is the five-second check: differentiate your answer
> and see whether you get the integrand back. $\frac{d}{dx}(-\cos x) = +\sin x$ ✓
>
> Integration is the one operation in mathematics whose answer you can always
> verify completely, by hand, in seconds. There is no excuse for a wrong
> integral on an untimed problem, and very little excuse on a timed one.
>
> ---

### Worked Example 2 — Basic Integration

**Find each integral.**

**(a)** $\displaystyle\int\left(4x^3 - \frac{6}{x^2} + \frac{2}{x} - 5\right)dx$

Rewrite as powers first, as in Chapter 01-17:

$$= \int\left(4x^3 - 6x^{-2} + \frac{2}{x} - 5\right)dx$$

$$= 4\cdot\frac{x^4}{4} - 6\cdot\frac{x^{-1}}{-1} + 2\ln\lvert x\rvert - 5x + C$$

$$= \boxed{x^4 + \frac{6}{x} + 2\ln\lvert x\rvert - 5x + C}$$

Note the $\frac{2}{x}$ term went to a logarithm while the $\frac{6}{x^2}$ term
used the ordinary power rule. Only the exponent $-1$ is exceptional.

**Check** by differentiating: $4x^3 - 6x^{-2} + \frac{2}{x} - 5$ ✓

**(b)** $\displaystyle\int\left(3\sqrt{x} + \frac{1}{\sqrt{x}}\right)dx$

$$= \int\left(3x^{1/2} + x^{-1/2}\right)dx = 3\cdot\frac{x^{3/2}}{3/2} + \frac{x^{1/2}}{1/2} + C$$

$$= \boxed{2x^{3/2} + 2\sqrt{x} + C}$$

**(c)** $\displaystyle\int\left(2\sin x - 3e^x + \sec^2 x\right)dx$

$$= \boxed{-2\cos x - 3e^x + \tan x + C}$$

---

## 19.3 The Area Problem and Riemann Sums

Now the second, apparently unrelated question.

What is the area of the region bounded above by $y = f(x)$, below by the $x$-axis,
and on the sides by $x = a$ and $x = b$?

For a rectangle or a triangle you have known the answer since school. For a
region with a curved boundary, you have no formula at all — and this is precisely
the same predicament as Chapter 01-17's slope problem. There, the resolution was
to approximate with something you *could* handle (a secant line), then take a
limit. Here, the same move: approximate with rectangles, then take a limit.

### Building a Riemann sum

Divide $[a,b]$ into $n$ subintervals of equal width

$$\Delta x = \frac{b-a}{n}$$

In each subinterval pick a sample point $x_k^*$, and build a rectangle of height
$f(x_k^*)$ and width $\Delta x$. Sum the rectangle areas:

$$\boxed{\text{Riemann sum} = \sum_{k=1}^{n} f\!\left(x_k^*\right)\Delta x}$$

That is the summation notation from Chapter 01-15, doing real work.

Common choices of sample point:

| Choice | Sample point | Behaviour on an increasing $f$ |
|---|---|---|
| Left endpoint | $x_k^* = a + (k-1)\Delta x$ | underestimates |
| Right endpoint | $x_k^* = a + k\Delta x$ | overestimates |
| Midpoint | $x_k^* = a + \left(k-\tfrac12\right)\Delta x$ | usually most accurate |

![FIG-01-19-002: Four panels showing Riemann approximations to the area under y = x² on [0, 2]. Panel 1: n = 4 left-endpoint rectangles, drawn inside the curve with visible gaps between rectangle tops and the curve, labeled "underestimate". Panel 2: n = 4 right-endpoint rectangles overhanging the curve, labeled "overestimate". Panel 3: n = 4 midpoint rectangles with tops crossing the curve, small over- and under-shoots visibly cancelling. Panel 4: n = 16 right-endpoint rectangles, the stair-step outline now hugging the curve closely, labeled "n → ∞ gives the exact area". Each panel shows Δx labeled on one rectangle base.](../figures/FIG-01-19-002-riemann-sums.png)

### The definite integral

Refine the partition — more rectangles, each thinner. As $n \to \infty$ the sum
converges, and the limit is the **definite integral**:

$$\boxed{\int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{k=1}^{n} f\!\left(x_k^*\right)\Delta x}$$

For a continuous $f$ this limit exists and is independent of which sample points
you chose. The function is then **integrable** on $[a,b]$.

Look at the notation and the correspondence is deliberate: $\int$ is a stretched
S for "sum," $f(x)$ is the rectangle height, and $dx$ is the vanishing width. The
symbol is a picture of its own definition.

> ---
> **Mentor's Margin**
>
> You will not evaluate integrals this way — that is what the Fundamental
> Theorem is for, and the contrast in effort between the next worked example and
> §19.6 is the best advertisement calculus has.
>
> But do not skip the definition, for two reasons. First, every numerical
> integration method you will meet in Chapter 01-37 — trapezoidal rule,
> Simpson's rule — *is* a Riemann-type sum with a smarter rule for the rectangle
> tops. When a real integrand comes from a data table rather than a formula, sums
> are all you have.
>
> Second, the sum is where the physical meaning lives. When you write
> $\int \rho\,dV$ for a mass, you are saying "chop the body into pieces, multiply
> each piece's density by its volume, add them up." The integral sign is
> bookkeeping over that operation. Engineers who understand the sum can set up
> integrals from a physical description; engineers who only know the rules can
> only evaluate integrals somebody else set up.
>
> ---

### Worked Example 3 — A Definite Integral from the Definition

**Given.** Evaluate $\displaystyle\int_0^2 x^2\,dx$ as the limit of right-endpoint
Riemann sums.

**Solution.**

$$\Delta x = \frac{2-0}{n} = \frac{2}{n} \qquad x_k = 0 + k\Delta x = \frac{2k}{n}$$

Rectangle heights:

$$f(x_k) = \left(\frac{2k}{n}\right)^2 = \frac{4k^2}{n^2}$$

The sum:

$$\sum_{k=1}^{n}\frac{4k^2}{n^2}\cdot\frac{2}{n} = \frac{8}{n^3}\sum_{k=1}^{n}k^2$$

Now use the closed-form power sum from Chapter 01-15:

$$\sum_{k=1}^{n}k^2 = \frac{n(n+1)(2n+1)}{6}$$

$$\sum = \frac{8}{n^3}\cdot\frac{n(n+1)(2n+1)}{6} = \frac{8\left(2n^2+3n+1\right)}{6n^2} = \frac{4}{3}\left(2 + \frac{3}{n} + \frac{1}{n^2}\right)$$

Take the limit, using $\frac{1}{n^p} \to 0$ from Chapter 01-16:

$$\int_0^2 x^2\,dx = \lim_{n\to\infty}\frac{4}{3}\left(2 + \frac{3}{n} + \frac{1}{n^2}\right) = \frac{4}{3}(2) = \boxed{\frac{8}{3} \approx 2.667}$$

**Sanity check.** The region is under $y = x^2$ from 0 to 2, inside a
$2\times 4$ bounding rectangle of area 8. Our answer is one third of that, which
is right for a parabola ✓

**Note for later.** Remember the effort this took: a sum formula from one chapter,
a limit from another, and a page of algebra. In §19.6 we will get $\frac{8}{3}$ in
one line.

---

## 19.4 Signed Area and the Properties of Definite Integrals

The definite integral computes **signed** area. Where $f$ is below the axis, the
rectangle heights $f(x_k^*)$ are negative, and those contributions subtract.

| Region | Contribution to $\int_a^b f\,dx$ |
|---|---|
| $f > 0$ | positive |
| $f < 0$ | negative |
| areas equal above and below | cancel to zero |

So $\int_a^b f\,dx$ is *net* area, not total geometric area. For total unsigned
area you integrate $\lvert f\rvert$, which in practice means splitting the
interval at the zeros of $f$ and negating the negative pieces. That distinction
gets full treatment in Chapter 01-20.

![FIG-01-19-003: Graph of a function crossing the x-axis twice on the interval [a, b]. Three regions are shaded and labeled: the first region above the axis shaded light with "+A₁", the middle region below the axis shaded darker with "−A₂", the third region above the axis shaded light with "+A₃". Beneath the plot, two expressions are contrasted: "∫f dx = A₁ − A₂ + A₃ (net)" and "∫|f| dx = A₁ + A₂ + A₃ (total)".](../figures/FIG-01-19-003-signed-area.png)

### Properties

Each follows directly from the Riemann sum definition.

| Property | Statement |
|---|---|
| Zero width | $\displaystyle\int_a^a f(x)\,dx = 0$ |
| Reversal | $\displaystyle\int_b^a f(x)\,dx = -\int_a^b f(x)\,dx$ |
| Constant multiple | $\displaystyle\int_a^b c\,f(x)\,dx = c\int_a^b f(x)\,dx$ |
| Sum | $\displaystyle\int_a^b \big[f \pm g\big]dx = \int_a^b f\,dx \pm \int_a^b g\,dx$ |
| Additivity | $\displaystyle\int_a^b f\,dx = \int_a^c f\,dx + \int_c^b f\,dx$ |
| Constant integrand | $\displaystyle\int_a^b c\,dx = c(b-a)$ |
| Comparison | if $f(x) \le g(x)$ on $[a,b]$, then $\displaystyle\int_a^b f\,dx \le \int_a^b g\,dx$ |

The **additivity** property is the workhorse. It lets you split an integral at any
convenient point — a sign change, a discontinuity, a branch boundary in a
piecewise function, a change of loading on a beam. Note that $c$ need not lie
between $a$ and $b$ for the identity to hold, though it usually does in practice.

The **reversal** property is where sign errors breed. Integrating right-to-left
flips the sign, so always confirm your lower limit is the starting value.

### Symmetry shortcuts

If the interval is symmetric about the origin, symmetry from Chapter 01-06 pays
off directly:

$$\boxed{\int_{-a}^{a} f(x)\,dx = 0 \qquad \text{if } f \text{ is odd } \big(f(-x) = -f(x)\big)}$$

$$\boxed{\int_{-a}^{a} f(x)\,dx = 2\int_0^a f(x)\,dx \qquad \text{if } f \text{ is even } \big(f(-x) = f(x)\big)}$$

The odd case is signed area cancelling exactly. Recognizing it turns some
formidable-looking integrals into the answer zero with no work at all — check
symmetry before you start computing.

---

## 19.5 The Fundamental Theorem of Calculus

Here is the connection. It comes in two parts, and they do different jobs.

### Part 1 — evaluation

> If $f$ is continuous on $[a,b]$ and $F$ is **any** antiderivative of $f$, then
>
> $$\boxed{\int_a^b f(x)\,dx = F(b) - F(a)}$$

To compute an area, find an antiderivative and subtract its values at the
endpoints. No sums, no limits.

Notice that the constant of integration is irrelevant here, which is why definite
integrals carry no $+C$: using $F + C$ instead of $F$ gives
$\big[F(b)+C\big] - \big[F(a)+C\big] = F(b)-F(a)$. The constant cancels. Any
antiderivative works, so take the simplest.

The evaluation notation:

$$\int_a^b f(x)\,dx = \Big[F(x)\Big]_a^b = F(b) - F(a)$$

### Part 2 — differentiation of an accumulation

Define the **accumulation function**, which records area accrued from a fixed
start $a$ up to a moving right end $x$:

$$G(x) = \int_a^x f(t)\,dt$$

Then

> $$\boxed{\frac{d}{dx}\int_a^x f(t)\,dt = f(x)}$$

Differentiating an accumulated total returns the rate that was accumulating.
Part 2 is the formal statement that integration and differentiation are inverse
operations — and it is what *proves* Part 1, by identifying the accumulation
function as an antiderivative.

Note the variable discipline: $t$ is the dummy variable of integration and $x$ is
the limit. Reusing the same letter for both is a common notational error and makes
the expression meaningless.

With the chain rule from Chapter 01-17, a variable upper limit that is itself a
function contributes its derivative:

$$\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f\big(g(x)\big)\cdot g'(x)$$

![FIG-01-19-004: Two-panel figure illustrating the Fundamental Theorem. Left panel: the curve y = f(t) with the region from t = a to a movable position t = x shaded, the shaded area labeled G(x), and a thin vertical strip at the right edge of width dt and height f(x) labeled "new area added = f(x)dx". Right panel: the accumulation function G(x) plotted against x directly below and aligned with the left panel, rising where f is positive and falling where f is negative, with a tangent line drawn at one point labeled "slope = f(x)". A two-way arrow between panels is labeled "differentiate ↓ / integrate ↑".](../figures/FIG-01-19-004-fundamental-theorem.png)

> ---
> **Mentor's Margin**
>
> Sit with the strip in the left panel of that figure for a moment, because it is
> the entire theorem in one picture.
>
> Push the right edge out by a sliver $dx$. The new area added is a thin
> rectangle: height $f(x)$, width $dx$, area $f(x)\,dx$. So the rate at which
> accumulated area grows, per unit of $x$, is $f(x)$.
>
> That is Part 2. Everything else is bookkeeping.
>
> And the engineering reading is identical: if a tank has accumulated volume
> $V(t)$ and inflow $Q(t)$, then $\frac{dV}{dt} = Q$ — the rate the total grows
> is the rate flowing in. You already believed that on physical grounds before
> anyone showed you a theorem. The Fundamental Theorem is the statement that your
> physical intuition was mathematically exact.
>
> ---

### Worked Example 4 — The Same Integral, Instantly

**Given.** Evaluate $\displaystyle\int_0^2 x^2\,dx$ using the Fundamental
Theorem.

**Solution.**

An antiderivative of $x^2$ is $F(x) = \frac{x^3}{3}$.

$$\int_0^2 x^2\,dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3} - 0 = \boxed{\frac{8}{3} \approx 2.667}$$

Compare with Worked Example 3: same answer, one line instead of a page. That
contrast is the entire value of the theorem.

### Worked Example 5 — Definite Integrals

**Evaluate each.**

**(a)** $\displaystyle\int_1^4\left(3x^2 - 2x + 1\right)dx$

$$= \Big[x^3 - x^2 + x\Big]_1^4 = (64 - 16 + 4) - (1 - 1 + 1) = 52 - 1 = \boxed{51}$$

**(b)** $\displaystyle\int_0^{\pi/2}\sin x\,dx$

$$= \Big[-\cos x\Big]_0^{\pi/2} = -\cos\frac{\pi}{2} - \left(-\cos 0\right) = 0 + 1 = \boxed{1}$$

**(c)** $\displaystyle\int_1^e\frac{1}{x}\,dx$

$$= \Big[\ln\lvert x\rvert\Big]_1^e = \ln e - \ln 1 = 1 - 0 = \boxed{1}$$

A tidy result, and it is essentially the defining property of $e$ from Chapter
01-05: $e$ is the number you must integrate $\frac{1}{x}$ up to, starting from 1,
to accumulate exactly one unit of area.

**(d)** $\displaystyle\int_{-2}^{2}x^3\,dx$

Check symmetry first: $f(-x) = -x^3 = -f(x)$, so $f$ is **odd**, and the interval
is symmetric.

$$= \boxed{0}$$

Verify the long way: $\left[\frac{x^4}{4}\right]_{-2}^{2} = 4 - 4 = 0$ ✓ The
symmetry check took two seconds.

### Worked Example 6 — Part 2 in Use

**Find each derivative.**

**(a)** $\dfrac{d}{dx}\displaystyle\int_2^x \sqrt{t^3+1}\,dt$

Part 2 applies directly — substitute $x$ for $t$:

$$= \boxed{\sqrt{x^3+1}}$$

No antiderivative was needed, and in fact $\sqrt{t^3+1}$ has no elementary
antiderivative. Part 2 sidesteps that entirely.

**(b)** $\dfrac{d}{dx}\displaystyle\int_0^{x^2}\cos t\,dt$

The upper limit is $g(x) = x^2$, so the chain rule contributes $g'(x) = 2x$:

$$= \cos\left(x^2\right)\cdot 2x = \boxed{2x\cos\left(x^2\right)}$$

**Check independently.** Here the antiderivative *is* elementary:
$\int_0^{x^2}\cos t\,dt = \big[\sin t\big]_0^{x^2} = \sin(x^2)$. Differentiating
by the chain rule gives $2x\cos(x^2)$ ✓

---

## 19.6 Integration by Substitution

The rules in §19.2 handle only bare functions. Real integrands are compositions,
and for those we need the reverse of the chain rule.

Recall the chain rule produced an extra factor — the inner derivative. So
integration must *look for* that factor and absorb it.

**The method.** To evaluate $\int f\big(g(x)\big)g'(x)\,dx$:

1. Choose $u = g(x)$, the inner function
2. Compute $du = g'(x)\,dx$
3. Rewrite the **entire** integrand in terms of $u$, including the differential
4. Integrate with respect to $u$
5. Substitute back $u = g(x)$

$$\boxed{\int f\big(g(x)\big)g'(x)\,dx = \int f(u)\,du}$$

Substitution works when the integrand contains an inner function **and** a factor
that is (or is a constant multiple of) that inner function's derivative. Spotting
that pairing is the skill.

![FIG-01-19-005: Two-column comparison diagram. Left column headed "Chain rule (forward)" shows sin(x²) with an arrow down to 2x·cos(x²), annotated "differentiating produces the inner derivative 2x as an extra factor". Right column headed "Substitution (reverse)" shows 2x·cos(x²)dx with an arrow down through an intermediate box "u = x², du = 2x dx" to cos(u)du, then to sin(u) + C, then back-substituted to sin(x²) + C, annotated "absorb the inner derivative into du". A horizontal double arrow between the columns is labeled "inverse operations".](../figures/FIG-01-19-005-substitution-mechanism.png)

> ---
> **Mentor's Margin**
>
> The error that defines this topic: swapping the variable name without
> converting the differential. Writing $\int 2x\cos(x^2)dx$ as
> $\int 2x\cos u\,dx$ accomplishes nothing — the integral is now in two
> variables and cannot be evaluated.
>
> The rule is absolute. **Every $x$ must go, including the one hiding in $dx$.**
> If any $x$ survives the substitution, either your choice of $u$ was wrong or the
> integrand is not a substitution candidate at all. That surviving $x$ is
> diagnostic; treat it as a signal to stop and reconsider, not as something to
> push through.
>
> As for choosing $u$: try the innermost function — what is inside the parentheses,
> under the radical, in the exponent, or in the denominator. Then check whether its
> derivative appears as a factor elsewhere. That check is quick, and if it fails you
> have lost ten seconds rather than half a page.
>
> ---

### Worked Example 7 — Substitution, Four Cases

**(a)** $\displaystyle\int 2x\left(x^2+1\right)^5 dx$

Let $u = x^2+1$, so $du = 2x\,dx$. The factor $2x\,dx$ is present exactly:

$$= \int u^5\,du = \frac{u^6}{6} + C = \boxed{\frac{\left(x^2+1\right)^6}{6} + C}$$

**Check.** Differentiating gives $\frac{6(x^2+1)^5(2x)}{6} = 2x(x^2+1)^5$ ✓

**(b)** $\displaystyle\int \frac{x}{\sqrt{x^2+9}}\,dx$

Let $u = x^2+9$, so $du = 2x\,dx$, meaning $x\,dx = \frac{1}{2}du$. The integrand
has $x\,dx$, off by the constant $\frac{1}{2}$ — and constants are always
adjustable:

$$= \int\frac{1}{\sqrt{u}}\cdot\frac{1}{2}du = \frac{1}{2}\int u^{-1/2}du = \frac{1}{2}\left(2u^{1/2}\right) + C = \boxed{\sqrt{x^2+9} + C}$$

**Check.** $\frac{d}{dx}(x^2+9)^{1/2} = \frac{1}{2}(x^2+9)^{-1/2}(2x) =
\frac{x}{\sqrt{x^2+9}}$ ✓

**(c)** $\displaystyle\int x\,e^{x^2}dx$

Let $u = x^2$, $du = 2x\,dx$, so $x\,dx = \frac{1}{2}du$:

$$= \frac{1}{2}\int e^u\,du = \frac{1}{2}e^u + C = \boxed{\frac{1}{2}e^{x^2} + C}$$

**(d)** $\displaystyle\int\tan x\,dx$

Not obviously a substitution — until you rewrite it. $\tan x =
\frac{\sin x}{\cos x}$, and the numerator is (to a sign) the derivative of the
denominator.

Let $u = \cos x$, so $du = -\sin x\,dx$, meaning $\sin x\,dx = -du$:

$$= \int\frac{-du}{u} = -\ln\lvert u\rvert + C = \boxed{-\ln\lvert\cos x\rvert + C}$$

**Check.** $\frac{d}{dx}\left(-\ln\lvert\cos x\rvert\right) =
-\frac{-\sin x}{\cos x} = \tan x$ ✓

Part (d) illustrates the pattern worth naming: whenever the integrand is a
fraction whose numerator is the derivative of its denominator, the answer is a
logarithm.

$$\int\frac{g'(x)}{g(x)}\,dx = \ln\lvert g(x)\rvert + C$$

### Definite integrals with substitution

Two valid routes, and one is safer.

**Route 1 — change the limits.** Convert the $x$-limits into $u$-limits using
$u = g(x)$, then evaluate entirely in $u$. Never substitute back.

**Route 2 — back-substitute.** Find the antiderivative in $x$, then apply the
original limits.

Route 1 is preferable, and the reason is practical: with Route 2 it is very easy
to apply the $x$-limits to a $u$-expression, which is silently wrong. Route 1
makes that impossible, because once the limits are converted the variable $x$ has
disappeared from the problem entirely.

### Worked Example 8 — Definite Integral by Substitution

**Given.** Evaluate $\displaystyle\int_0^1 x\left(x^2+1\right)^3 dx$.

**Solution — Route 1, changing limits.**

Let $u = x^2+1$, so $du = 2x\,dx$ and $x\,dx = \frac{1}{2}du$.

Convert the limits:

$$x = 0 \implies u = 0 + 1 = 1$$
$$x = 1 \implies u = 1 + 1 = 2$$

$$\int_0^1 x\left(x^2+1\right)^3dx = \frac{1}{2}\int_1^2 u^3\,du = \frac{1}{2}\left[\frac{u^4}{4}\right]_1^2$$

$$= \frac{1}{8}\left(16 - 1\right) = \boxed{\frac{15}{8} = 1.875}$$

**Check — Route 2.** The antiderivative in $x$ is
$\frac{(x^2+1)^4}{8}$:

$$\left[\frac{\left(x^2+1\right)^4}{8}\right]_0^1 = \frac{16}{8} - \frac{1}{8} = \frac{15}{8} \;\checkmark$$

Both routes agree. Note how Route 1 never required writing $(x^2+1)^4$ at all.

---

## 19.7 Average Value of a Function

The mean of a finite list is the sum divided by the count. For a function on an
interval there are infinitely many values, so the sum becomes an integral and the
count becomes the interval width:

$$\boxed{\bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx}$$

Rearranged, this says something geometrically clean:

$$\bar{f}\cdot(b-a) = \int_a^b f(x)\,dx$$

The average value is the height of the rectangle over $[a,b]$ having the **same
area** as the region under the curve. Whatever the curve does, level it off to a
constant height enclosing the same total.

![FIG-01-19-006: Curve y = f(x) over [a, b] with the region beneath it shaded light. A horizontal line at height f̄ is drawn across the interval, forming a rectangle outlined in bold. Where the curve rises above the line, the excess area is hatched and labeled "+"; where the curve dips below, the deficit is hatched and labeled "−", with a callout "excess and deficit are equal". Both areas are labeled equal, and the identity f̄·(b−a) = ∫f dx is printed beneath.](../figures/FIG-01-19-006-average-value.png)

The **Mean Value Theorem for Integrals** states that a continuous $f$ actually
*attains* its average value somewhere: there is a $c$ in $[a,b]$ with
$f(c) = \bar{f}$. That is the integral analogue of the MVT from Chapter 01-18,
and it is why the curve must cross the level line in the figure.

### Worked Example 9 — Average Value, Two Interpretations

**Given.** The particle from Chapter 01-17 with $s(t) = t^3 - 6t^2 + 9t$ m and
$v(t) = 3t^2 - 12t + 9$ m/s, over $0 \le t \le 4$ s.

**(a)** Find the average velocity by integration.
**(b)** Confirm it using displacement over elapsed time.

**Solution.**

**(a)**

$$\bar{v} = \frac{1}{4-0}\int_0^4\left(3t^2 - 12t + 9\right)dt = \frac{1}{4}\Big[t^3 - 6t^2 + 9t\Big]_0^4$$

$$= \frac{1}{4}\Big[(64 - 96 + 36) - 0\Big] = \frac{4}{4} = \boxed{1.00 \text{ m/s}}$$

**(b)** Average velocity is displacement divided by elapsed time:

$$\bar{v} = \frac{s(4) - s(0)}{4 - 0} = \frac{4 - 0}{4} = 1.00 \text{ m/s} \;\checkmark$$

These are not two coincidentally equal calculations — they are the same
calculation. The antiderivative of $v$ **is** $s$, so the Fundamental Theorem
turns the integral in (a) into the difference quotient in (b). And that difference
quotient is exactly the average rate of change from the Mean Value Theorem in
Chapter 01-18. The MVT for derivatives and the average value of a function are the
same statement viewed from two sides.

**Worth noting.** The particle's average velocity is $+1.00$ m/s even though it
spent the interval $1 < t < 3$ moving backward. Average velocity uses net
displacement; total distance travelled would be larger. That is the signed-area
distinction from §19.4 appearing in physical form, and Chapter 01-20 handles it
properly.

---

## 19.8 Engineering Application: Total from a Rate

### Worked Example 10 — Volume Delivered from a Flow Rate

**Given.** The tank from Chapters 01-16 and 01-17 has level
$h(t) = 4.5\left(1-e^{-t/6.0}\right)$ m and level rate
$\frac{dh}{dt} = 0.75\,e^{-t/6.0}$ m/min.

**(a)** Integrate the rate from $t = 0$ to $t = 12$ min and interpret the result.
**(b)** Confirm using the level function directly.
**(c)** Find the average filling rate over that interval.

**Solution.**

**(a)** Substitute $u = -t/6.0$, so $du = -\frac{1}{6}dt$ and $dt = -6\,du$.
Rather than change limits here, take the antiderivative directly — a standard
result worth knowing is $\int e^{kt}dt = \frac{1}{k}e^{kt} + C$:

$$\int_0^{12}0.75\,e^{-t/6.0}\,dt = 0.75\left[\frac{e^{-t/6.0}}{-1/6}\right]_0^{12} = -4.5\left[e^{-t/6.0}\right]_0^{12}$$

$$= -4.5\left(e^{-2} - e^{0}\right) = -4.5\left(0.135335 - 1\right) = -4.5(-0.864665)$$

$$= \boxed{3.891 \text{ m}}$$

**Interpretation.** This is the **total rise in level** over the twelve minutes.
The units confirm it: integrating m/min against dt in min yields metres ✓ We
integrated a rate and obtained a total.

**(b)** Directly from the level function:

$$h(12) - h(0) = 4.5\left(1 - e^{-2}\right) - 0 = 4.5(0.864665) = 3.891 \text{ m} \;\checkmark$$

Identical, and necessarily so — that is Part 1 of the Fundamental Theorem, since
$h$ is an antiderivative of $\frac{dh}{dt}$. The check is not independent
confirmation so much as a demonstration that the theorem does what it claims.

**(c)**

$$\overline{\left(\frac{dh}{dt}\right)} = \frac{3.891}{12 - 0} = \boxed{0.324 \text{ m/min}}$$

**Cross-check against Chapter 01-17.** The instantaneous rate was 0.75 m/min at
$t = 0$ and 0.276 m/min at $t = 6$. An average of 0.324 m/min over $[0,12]$ sits
between those, closer to the later value because the rate decays and spends most
of the interval low ✓ And by the Mean Value Theorem for Integrals the rate equals
0.324 m/min at some instant: solving $0.75e^{-t/6} = 0.324$ gives
$t = -6\ln(0.432) = 5.04$ min, comfortably inside the interval ✓

> ---
> **Mentor's Margin**
>
> That worked example is the template for an enormous class of engineering
> calculations, and it is worth stating in general terms.
>
> $$\text{total} = \int \text{rate}\;dt$$
>
> Volume from flow rate. Charge from current. Energy from power. Mass from mass
> flow. Impulse from force. Distance from speed. Heat from heat flux.
>
> Every one of those is the same integral wearing different units, and the units
> tell you which. If you integrate m³/s against seconds you get m³. If you
> integrate watts against seconds you get joules. Check the units of your answer
> and you will know immediately whether you integrated the right quantity against
> the right variable.
>
> The reverse habit is just as valuable: when a problem gives you a rate and asks
> for a total, the word "integrate" should arrive before you have finished
> reading the question.
>
> ---

---

## As the Handbook States It

> **Handbook 10.6, Mathematics section (begins p. 36)** — integration appears in
> the *Integral Calculus* subsection, approximately pp. 46–48.

The Handbook's integral coverage is **strong** — the table of integrals is one of
the most valuable pages in the reference for exam purposes.

What you will find:

- A table of indefinite integrals covering powers, $\frac{1}{x}$, exponentials
  with base $e$ and base $a$, all the standard trigonometric forms, and the
  inverse trigonometric results
- The constant of integration $C$ shown explicitly
- Integration by substitution, stated as a method
- Integration by parts (Chapter 01-21 — not needed yet)
- The Fundamental Theorem, generally in the evaluation form
- Average value of a function
- Some specialized forms including $\int\frac{dx}{a^2+x^2}$ and radical
  denominators

**What's in the Handbook — find it fast:**

The integral table. Locate it in your first Handbook practice session and put it
on your personal page map from Chapter 00-03. You will use it more than any other
page in Mathematics. Note that the entries are *indefinite* integrals — you supply
the limits and the subtraction.

**What's not in the Handbook — memorize:**

- That the constant of integration is mandatory on an indefinite integral, and
  absent on a definite one
- The Riemann sum definition of the definite integral
- The interpretation of $\int_a^b f\,dx$ as **signed** area, and the distinction
  between net and total area
- All of the definite-integral properties, especially reversal
  ($\int_b^a = -\int_a^b$) and additivity
- The even/odd symmetry shortcuts on symmetric intervals
- **Part 2** of the Fundamental Theorem, $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$,
  and its chain-rule extension for a variable upper limit
- The substitution procedure in full, particularly that $dx$ must be converted
  into $du$
- That definite-integral limits must be changed when substituting, if you do not
  back-substitute
- The pattern $\int\frac{g'}{g}dx = \ln\lvert g\rvert + C$
- The units rule: integrating a rate against its variable yields a total
- That $\frac{d}{dh}$ of a volume is an area, and the reverse — a free structural
  check

> ---
> **Mentor's Margin**
>
> Even with the table printed, memorize the common integrals: powers,
> $\frac{1}{x}$, $e^{kx}$, $\sin$, $\cos$. Those five cover the large majority of
> what the exam asks, they appear inside problems from every discipline, and a
> lookup costs fifteen to twenty seconds each time.
>
> Look up the rare forms — inverse trig results, the radical denominators, the
> secant and cosecant families. Know the common five cold.
>
> One more piece of exam strategy. Substitution is not in the Handbook as a
> worked procedure, only as a named method, and it is required constantly. Drill
> it until choosing $u$ is a reflex rather than a search. That single technique
> unlocks more FE integrals than any other item in this chapter.
>
> ---

---

## Where This Goes Wrong

**Omitting the constant of integration.** $\int 2x\,dx = x^2 + C$. Without the
$+C$ the answer is incomplete and graded wrong.

**Writing $+C$ on a definite integral.** A definite integral is a number. The
constant cancels in the subtraction.

**Applying the power rule at $n = -1$.** $\int x^{-1}dx = \ln\lvert x\rvert + C$,
not $\frac{x^0}{0}$. Check the exponent before applying the rule.

**Dropping the absolute value in the logarithm.** $\ln\lvert x\rvert$, not
$\ln x$. The integrand $\frac{1}{x}$ exists for negative $x$ and needs an
antiderivative there.

**Sign errors in the trig integrals.** $\int\sin x\,dx = -\cos x + C$ and
$\int\cos x\,dx = +\sin x + C$. Differentiate your answer to check; it takes
seconds.

**Inventing a product rule for integrals.** There is none.
$\int f g\,dx \ne \left(\int f\,dx\right)\left(\int g\,dx\right)$. Linearity
covers sums and scalar multiples only.

**Substituting the variable but not the differential.** Every $x$ must be
converted, including the one in $dx$. A surviving $x$ means the substitution has
failed.

**Forgetting to change limits on a definite substitution.** Either convert the
limits to $u$-values or back-substitute to $x$ first. Applying $x$-limits to a
$u$-expression is wrong and produces a plausible-looking number.

**Choosing $u$ without checking for its derivative.** Substitution requires
$g'(x)$ to appear as a factor, up to a constant. If it does not, this is not the
right technique.

**Reversing the limits without flipping the sign.**
$\int_b^a = -\int_a^b$. Confirm which endpoint is the lower limit.

**Reporting net area when total area was asked.** A region below the axis
contributes negatively. If the question asks for the area of a region, split at
the zeros and negate the negative pieces.

**Reusing the integration variable as a limit.** In
$\int_a^x f(t)\,dt$, the dummy variable must differ from the limit. Writing
$\int_a^x f(x)\,dx$ is meaningless.

**Forgetting the chain factor in Part 2.** With a variable upper limit
$g(x)$, the derivative is $f\big(g(x)\big)\cdot g'(x)$. The inner derivative does
not disappear just because an integral is involved.

**Integrating against the wrong variable.** $\int Q\,dt$ gives volume;
$\int Q\,dx$ gives something with no physical meaning. The differential declares
what you are accumulating over — check that it matches the physical question.

---

## Key Terms

| Term | Definition |
|---|---|
| Antiderivative | A function $F$ with $F' = f$ |
| Indefinite integral | $\int f\,dx$; the family of all antiderivatives, written with $+C$ |
| Constant of integration | The arbitrary constant $C$ distinguishing members of the antiderivative family |
| Initial condition | A known function value used to determine $C$ |
| Riemann sum | $\sum f(x_k^*)\Delta x$; a rectangle-based approximation to area |
| Partition | The division of $[a,b]$ into subintervals |
| Sample point | The $x$-value in each subinterval that sets the rectangle height |
| Definite integral | $\int_a^b f\,dx$; the limit of Riemann sums as $n \to \infty$; a number |
| Integrable | Having a definite integral that exists; guaranteed for continuous functions |
| Signed area | Area counted positive above the axis and negative below |
| Net area | The signed total, as computed by $\int_a^b f\,dx$ |
| Total area | The unsigned total, computed by integrating $\lvert f\rvert$ |
| Additivity | $\int_a^b = \int_a^c + \int_c^b$; the property permitting an integral to be split |
| Fundamental Theorem, Part 1 | $\int_a^b f\,dx = F(b) - F(a)$ for any antiderivative $F$ |
| Fundamental Theorem, Part 2 | $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ |
| Accumulation function | $G(x) = \int_a^x f(t)\,dt$; total accrued from $a$ up to $x$ |
| Evaluation notation | $\big[F(x)\big]_a^b$, meaning $F(b) - F(a)$ |
| Substitution | Integration technique reversing the chain rule via $u = g(x)$ |
| Average value | $\bar{f} = \frac{1}{b-a}\int_a^b f\,dx$; the constant height enclosing the same area |
| MVT for Integrals | A continuous function attains its average value at some interior point |

---

## Review Questions

### Conceptual

1. Explain why an indefinite integral requires a constant of integration but a
   definite integral does not.
2. Two functions have the same derivative on an interval. What can you conclude
   about them, and which theorem from Chapter 01-18 justifies it?
3. Why does the power rule for integration fail at $n = -1$, and what is the
   correct antiderivative there? Explain the absolute value.
4. Describe how a Riemann sum approximates area and what happens in the limit.
   Why does the choice of sample point stop mattering?
5. Explain the difference between net area and total area, and describe how you
   would compute each for a function that crosses the axis twice on $[a,b]$.
6. State both parts of the Fundamental Theorem of Calculus and describe what
   each part is used for.
7. Explain, using the thin-strip argument, why differentiating an accumulation
   function returns the integrand.
8. Why must every $x$ — including the one in $dx$ — be converted during a
   substitution?
9. Give a physical interpretation of the average value formula using velocity and
   displacement.
10. A problem gives you a flow rate in L/s as a function of time in seconds and
    asks for the volume delivered. State the integral and its units before
    computing anything.

### Calculation

11. Evaluate each indefinite integral:
    (a) $\displaystyle\int\left(6x^2 - \frac{4}{x^3} + \frac{3}{x}\right)dx$
    (b) $\displaystyle\int\left(5\sqrt[3]{x} - 2e^x\right)dx$
    (c) $\displaystyle\int\left(4\cos x - \sec^2 x\right)dx$
    (d) $\displaystyle\int\frac{x^2 - 3x + 1}{x}\,dx$

12. Find $f(x)$ given $f'(x) = 4x - 3$ and $f(2) = 5$.

13. Evaluate each definite integral:
    (a) $\displaystyle\int_1^3\left(2x^2 - x\right)dx$
    (b) $\displaystyle\int_0^{\pi}\sin x\,dx$
    (c) $\displaystyle\int_1^{e^2}\frac{1}{x}\,dx$
    (d) $\displaystyle\int_{-3}^{3}\left(x^5 - 2x\right)dx$ — use symmetry
    (e) $\displaystyle\int_{-2}^{2}\left(x^2 + 1\right)dx$ — use symmetry

14. Evaluate $\displaystyle\int_0^3 (2x+1)\,dx$ two ways: as the limit of
    right-endpoint Riemann sums, and by the Fundamental Theorem.

15. Integrate by substitution:
    (a) $\displaystyle\int 3x^2\left(x^3-4\right)^7 dx$
    (b) $\displaystyle\int\frac{2x}{x^2+5}\,dx$
    (c) $\displaystyle\int \sin x\cos^4 x\,dx$
    (d) $\displaystyle\int e^{4t}\,dt$
    (e) $\displaystyle\int\frac{\ln x}{x}\,dx$

16. Evaluate by substitution with changed limits:
    (a) $\displaystyle\int_0^2 x\sqrt{x^2+5}\,dx$
    (b) $\displaystyle\int_0^{\pi/2}\cos x\,\sin^3 x\,dx$

17. Differentiate each:
    (a) $\dfrac{d}{dx}\displaystyle\int_1^x\frac{1}{1+t^4}\,dt$
    (b) $\dfrac{d}{dx}\displaystyle\int_0^{3x}\sqrt{t+1}\,dt$

18. Find the average value of $f(x) = x^2$ on $[0,3]$, and find the point where
    the function attains it.

19. **Engineering application.** A pump delivers at a declining rate
    $Q(t) = 18e^{-t/25}$ L/s, with $t$ in seconds.
    (a) Write the integral for total volume delivered in the first 60 s, with
    units.
    (b) Evaluate it.
    (c) Find the average flow rate over that interval.
    (d) Determine the total volume the pump would deliver if run indefinitely,
    and explain why that is finite.

20. **Engineering application.** A beam carries a distributed load
    $w(x) = 4 + 0.5x^2$ kN/m over its 6.0 m length, with $x$ measured from the
    left end.
    (a) Find the total load on the beam by integration, with units.
    (b) Find the average load intensity.
    (c) At what position does the load intensity equal its average value?

### Multiple Choice

21. $\displaystyle\int 3x^2\,dx$ equals:
    A) $6x + C$
    B) $x^3 + C$
    C) $3x^3 + C$
    D) $\dfrac{3x^3}{2} + C$

22. $\displaystyle\int\frac{1}{x}\,dx$ equals:
    A) $\dfrac{x^0}{0} + C$
    B) $-x^{-2} + C$
    C) $\ln\lvert x\rvert + C$
    D) $\dfrac{1}{2x^2} + C$

23. $\displaystyle\int_0^{\pi/2}\cos x\,dx$ equals:
    A) $0$
    B) $1$
    C) $-1$
    D) $\pi/2$

24. $\displaystyle\int_{-4}^{4}x^7\,dx$ equals:
    A) $0$
    B) $4096$
    C) $8192$
    D) $2048$

25. $\dfrac{d}{dx}\displaystyle\int_2^x e^{t^2}dt$ equals:
    A) $e^{x^2} - e^4$
    B) $2xe^{x^2}$
    C) $e^{x^2}$
    D) $\dfrac{e^{x^2}}{2x}$

26. If $\displaystyle\int_a^b f(x)\,dx = 12$, then
    $\displaystyle\int_b^a f(x)\,dx$ equals:
    A) $12$
    B) $-12$
    C) $0$
    D) Cannot be determined

27. The average value of $f$ on $[a,b]$ is:
    A) $\dfrac{f(a)+f(b)}{2}$
    B) $\displaystyle\int_a^b f\,dx$
    C) $\dfrac{1}{b-a}\displaystyle\int_a^b f\,dx$
    D) $(b-a)\displaystyle\int_a^b f\,dx$

---

## Answer Key with Explanations

**1.** Differentiating destroys additive constants, so infinitely many functions
share one derivative; the indefinite integral must represent all of them, hence
$+C$. A definite integral subtracts two values of an antiderivative, and
$[F(b)+C] - [F(a)+C] = F(b)-F(a)$ — the constant cancels, so it is omitted.
(§19.1, §19.5)

**2.** They differ by a constant. Justified by the **Mean Value Theorem**: if
$H = F-G$ has $H' = 0$ everywhere, then for any two points
$H(x_2)-H(x_1) = H'(c)(x_2-x_1) = 0$, so $H$ never changes value. (§19.1)

**3.** The formula $\frac{x^{n+1}}{n+1}$ divides by $n+1$, which is zero at
$n=-1$. The correct result is $\ln\lvert x\rvert + C$. The absolute value is
needed because $\frac{1}{x}$ is defined for negative $x$ while $\ln x$ is not;
for $x<0$, $\frac{d}{dx}\ln(-x) = \frac{-1}{-x} = \frac{1}{x}$ ✓ so
$\ln\lvert x\rvert$ covers both signs. (§19.2)

**4.** Divide $[a,b]$ into $n$ subintervals, build a rectangle on each with height
given by the function at some sample point, and sum the areas. As $n\to\infty$
each rectangle's width $\to 0$ and the stair-step outline converges on the curve.
The sample point stops mattering because within a shrinking subinterval a
continuous function's values all converge to the same limit — left, right, and
midpoint heights become indistinguishable. (§19.3)

**5.** Net area counts regions below the axis as negative and is what
$\int_a^b f\,dx$ returns. Total area counts all regions positively. To compute
total area, find the zeros of $f$, split the interval there using additivity, and
negate the integrals over intervals where $f<0$. (§19.4)

**6.** **Part 1:** $\int_a^b f\,dx = F(b)-F(a)$ for any antiderivative $F$ — used
to *evaluate* definite integrals without sums. **Part 2:**
$\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ — used to *differentiate* accumulation
functions, and it establishes that integration and differentiation are inverse
operations. (§19.5)

**7.** Push the upper limit from $x$ to $x+dx$. The added region is a strip of
height $f(x)$ and width $dx$, so the added area is $f(x)\,dx$. Dividing by $dx$
gives the rate of area accumulation as $f(x)$, which is precisely
$\frac{dG}{dx} = f(x)$. (§19.5)

**8.** Because $\int \cdots dx$ and $\int\cdots du$ are different operations. The
differential specifies the variable of accumulation, and $du = g'(x)dx$ means
$dx$ and $du$ differ by the factor $g'(x)$. Leaving $dx$ in place while writing
the integrand in $u$ produces a two-variable expression with no defined value.
(§19.6)

**9.** $\bar{v} = \frac{1}{b-a}\int_a^b v\,dt$. By Part 1, the integral equals
$s(b)-s(a)$, the net displacement. So the formula reads: average velocity is
displacement divided by elapsed time — the elementary definition. The integral
formula and the elementary one are the same statement. (§19.7)

**10.** $V = \displaystyle\int_{t_1}^{t_2}Q(t)\,dt$. Units:
$\left(\text{L/s}\right)(\text{s}) = \text{L}$ ✓ (§19.8)

**11.**

(a) $6\cdot\frac{x^3}{3} - 4\cdot\frac{x^{-2}}{-2} + 3\ln\lvert x\rvert + C =
\boxed{2x^3 + \frac{2}{x^2} + 3\ln\lvert x\rvert + C}$

(b) $5\cdot\frac{x^{4/3}}{4/3} - 2e^x + C =
\boxed{\frac{15}{4}x^{4/3} - 2e^x + C}$

(c) $\boxed{4\sin x - \tan x + C}$

(d) Divide through first: $x - 3 + \frac{1}{x}$, so
$\boxed{\frac{x^2}{2} - 3x + \ln\lvert x\rvert + C}$

**12.** $f(x) = 2x^2 - 3x + C$. Then $f(2) = 8 - 6 + C = 5 \implies C = 3$.

$$\boxed{f(x) = 2x^2 - 3x + 3}$$

**13.**

(a) $\left[\frac{2x^3}{3} - \frac{x^2}{2}\right]_1^3 = \left(18 - 4.5\right) -
\left(\frac{2}{3} - 0.5\right) = 13.5 - 0.1667 = \boxed{13.33}$
(exactly $\frac{40}{3}$)

(b) $\big[-\cos x\big]_0^{\pi} = -(-1) + 1 = \boxed{2}$

(c) $\big[\ln x\big]_1^{e^2} = 2 - 0 = \boxed{2}$

(d) Both $x^5$ and $-2x$ are odd, so the integrand is odd on a symmetric
interval: $\boxed{0}$

(e) $x^2+1$ is even, so $= 2\int_0^2(x^2+1)dx =
2\left[\frac{x^3}{3}+x\right]_0^2 = 2\left(\frac{8}{3}+2\right) =
2\left(\frac{14}{3}\right) = \boxed{\frac{28}{3} \approx 9.333}$

**14.** **Riemann sum.** $\Delta x = \frac{3}{n}$, $x_k = \frac{3k}{n}$,
$f(x_k) = \frac{6k}{n}+1$.

$$\sum_{k=1}^{n}\left(\frac{6k}{n}+1\right)\frac{3}{n} = \frac{18}{n^2}\sum k + \frac{3}{n}\sum 1 = \frac{18}{n^2}\cdot\frac{n(n+1)}{2} + 3$$

$$= \frac{9(n+1)}{n} + 3 = 9 + \frac{9}{n} + 3 \longrightarrow \boxed{12}$$

**FTC.** $\big[x^2+x\big]_0^3 = 9+3 = 12$ ✓

**15.**

(a) $u = x^3-4$, $du = 3x^2dx$: $\int u^7du =
\boxed{\frac{\left(x^3-4\right)^8}{8} + C}$

(b) $u = x^2+5$, $du = 2x\,dx$: $\int\frac{du}{u} =
\boxed{\ln\left(x^2+5\right) + C}$ (the argument is always positive, so the
absolute value is unnecessary here)

(c) $u = \cos x$, $du = -\sin x\,dx$: $-\int u^4du =
\boxed{-\frac{\cos^5 x}{5} + C}$

(d) $u = 4t$, $du = 4\,dt$: $\frac{1}{4}\int e^u du =
\boxed{\frac{1}{4}e^{4t} + C}$

(e) $u = \ln x$, $du = \frac{dx}{x}$: $\int u\,du =
\boxed{\frac{\left(\ln x\right)^2}{2} + C}$

**16.**

(a) $u = x^2+5$, $x\,dx = \frac{1}{2}du$. Limits: $x=0 \to u=5$;
$x=2 \to u=9$.

$$\frac{1}{2}\int_5^9 u^{1/2}du = \frac{1}{2}\left[\frac{2u^{3/2}}{3}\right]_5^9 = \frac{1}{3}\left(27 - 5\sqrt{5}\right)$$

$5\sqrt{5} = 11.1803$, so $= \frac{15.8197}{3} = \boxed{5.273}$

(b) $u = \sin x$, $du = \cos x\,dx$. Limits: $x=0 \to u=0$;
$x=\pi/2 \to u=1$.

$$\int_0^1 u^3du = \left[\frac{u^4}{4}\right]_0^1 = \boxed{0.250}$$

**17.**

(a) Part 2 directly: $\boxed{\dfrac{1}{1+x^4}}$

(b) Upper limit $3x$, so multiply by its derivative 3:
$\boxed{3\sqrt{3x+1}}$

**18.** $\bar{f} = \frac{1}{3}\int_0^3 x^2dx = \frac{1}{3}\cdot\frac{27}{3} =
\boxed{3}$

Attained where $x^2 = 3$, so $x = \sqrt{3} = \boxed{1.732}$, which lies in
$[0,3]$ ✓ as the MVT for Integrals requires.

**19.**

(a) $V = \displaystyle\int_0^{60}18e^{-t/25}\,dt$; units
$(\text{L/s})(\text{s}) = \text{L}$

(b) $= 18\left[\frac{e^{-t/25}}{-1/25}\right]_0^{60} =
-450\left[e^{-t/25}\right]_0^{60} = -450\left(e^{-2.4}-1\right)$

$e^{-2.4} = 0.0907180$, so $= -450(-0.909282) = \boxed{409.2 \text{ L}}$

(c) $\bar{Q} = \frac{409.2}{60} = \boxed{6.82 \text{ L/s}}$

(d) $\displaystyle\int_0^{\infty}18e^{-t/25}dt = -450\left(0 - 1\right) =
\boxed{450 \text{ L}}$

Finite because $e^{-t/25} \to 0$ as $t\to\infty$ (Chapter 01-16), so the
accumulated area converges. The rate decays fast enough that the total is
bounded — the same mechanism that made the infinite geometric series of Chapter
01-15 converge.

**Consistency check.** 409.2 L of the eventual 450 L arrives in the first 60 s,
which is 90.9%. Since $60 = 2.4\tau$ with $\tau = 25$ s, and
$1 - e^{-2.4} = 0.909$ ✓

**20.**

(a) $W = \displaystyle\int_0^{6}\left(4+0.5x^2\right)dx =
\left[4x + \frac{x^3}{6}\right]_0^6 = 24 + 36 = \boxed{60.0 \text{ kN}}$

Units: $(\text{kN/m})(\text{m}) = \text{kN}$ ✓

(b) $\bar{w} = \frac{60.0}{6.0} = \boxed{10.0 \text{ kN/m}}$

(c) Set $4 + 0.5x^2 = 10.0$:

$$0.5x^2 = 6.0 \implies x^2 = 12.0 \implies x = \boxed{3.46 \text{ m}}$$

Inside $[0,6]$ ✓ Note it sits right of midspan, because the load intensity
increases toward the right end.

**21. B — $x^3+C$.** $\int 3x^2dx = 3\cdot\frac{x^3}{3} = x^3+C$. Choice A
differentiates instead of integrating; C forgets to divide by the new exponent.
(§19.2)

**22. C — $\ln\lvert x\rvert + C$.** The $n=-1$ exception. Choice A applies the
power rule illegally. (§19.2)

**23. B — 1.** $\big[\sin x\big]_0^{\pi/2} = 1-0 = 1$. (§19.5)

**24. A — 0.** $x^7$ is odd and the interval is symmetric about the origin.
(§19.4)

**25. C — $e^{x^2}$.** Part 2 with upper limit exactly $x$, so no chain factor.
Choice B wrongly applies a chain factor; choice A tries to evaluate an
antiderivative that does not exist in elementary form. (§19.5)

**26. B — $-12$.** Reversing the limits flips the sign. (§19.4)

**27. C.** Average value is the integral divided by the interval width. Choice A
is the average of the endpoint values, which is generally different. (§19.7)

---

## Quick Reference

**Indefinite integral** — antiderivative family, always $+C$ — *Handbook p. 46*

$$\int x^n dx = \frac{x^{n+1}}{n+1}+C \;(n\ne -1) \qquad \int\frac{dx}{x} = \ln\lvert x\rvert + C$$

$$\int e^x dx = e^x + C \qquad \int\sin x\,dx = -\cos x + C \qquad \int\cos x\,dx = \sin x + C$$

**Definite integral** — a number, no $C$

$$\int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{k=1}^n f\!\left(x_k^*\right)\Delta x, \qquad \Delta x = \frac{b-a}{n}$$

**Fundamental Theorem**

$$\int_a^b f\,dx = F(b)-F(a) \qquad \frac{d}{dx}\int_a^x f(t)\,dt = f(x)$$

$$\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f\big(g(x)\big)g'(x)$$

**Properties**

$$\int_b^a = -\int_a^b \qquad \int_a^b = \int_a^c + \int_c^b \qquad \int_a^a = 0$$

$$\int_{-a}^{a} f\,dx = 0 \;(f \text{ odd}) \qquad \int_{-a}^{a}f\,dx = 2\int_0^a f\,dx \;(f \text{ even})$$

**Substitution**

$$u = g(x), \quad du = g'(x)\,dx, \quad \text{convert limits or back-substitute}$$

$$\int\frac{g'(x)}{g(x)}dx = \ln\lvert g(x)\rvert + C$$

**Average value**

$$\bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx$$

**Total from a rate**

$$\text{total} = \int \text{rate}\;d(\text{variable})$$

---

## Where We Go From Here

**Next:** [01-20 Applications of Integration](01-20-applications-of-integration.md)
— areas between curves, volumes of revolution, arc length, centroids, and work.
Everything you compute there uses the machinery built here; what changes is
learning to set up the integral from a physical description.

**This chapter is used by:** 01-20 (all applications) · 01-21 (advanced
integration techniques) · 01-24 (differential equations) · 01-32 (multiple
integrals) · 01-37 (numerical integration) · 01-39 (continuous probability
distributions) · 02-27 (centroids and moments of inertia) · 02-49 (beam shear and
moment diagrams) · 02-58 (heat transfer) · 02-64 (RMS values in AC circuits) ·
02-74 (continuous compounding)
