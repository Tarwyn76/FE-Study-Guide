---
chapter: "01-21"
title: "Techniques of Integration"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-021-01, MATH-1C-021-02, MATH-1C-021-03, MATH-1C-021-04, MATH-1C-021-05, MATH-1C-021-06]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-21: Techniques of Integration

> *"Differentiation is an algorithm. Integration is a search. Every derivative
> you will ever need can be computed by following rules in a fixed order;
> integrals require you to recognize which of half a dozen approaches will open
> the particular lock in front of you. That sounds worse than it is. There are
> only a few locks, they have distinctive shapes, and you can always check your
> answer by differentiating it."*

---

## Before You Start

**Prerequisites:** [01-05 Exponents, Radicals, and Logarithms](01-05-exponents-radicals-logarithms.md) · [01-07 Polynomials and Their Roots](01-07-polynomials-roots.md) · [01-11 Trigonometry](01-11-trigonometry.md) · [01-16 Limits and Continuity](01-16-limits-continuity.md) · [01-17 The Derivative](01-17-the-derivative.md) · [01-18 Applications of the Derivative](01-18-applications-of-the-derivative.md) · [01-19 Antiderivatives and the Definite Integral](01-19-antiderivatives-definite-integral.md)

**Skip if:** You pass the Tier 1C test-out quiz. Verify you can integrate by
parts including a repeated application, decompose a proper rational function
into partial fractions, and determine whether an improper integral converges
before skipping. Partial fractions is the one to be honest with yourself about —
it resurfaces in inverse Laplace transform work later in this tier, and rust
there is expensive.

**Time:** ~80 min read · ~30 min review questions · ~85 min practice problems

---

## On the Board Today

Apprentice, Chapter 01-19 gave you the table and substitution, and Chapter
01-20 spent them on real geometry. Substitution covers a great deal — it is the
single highest-yield technique — but it covers only integrands built like the
chain rule, and plenty are not.

Try $\int x e^x dx$. There is no inner function whose derivative appears as a
factor. Substitution has nothing to grip.

Try $\int \frac{5x-3}{x^2-2x-3}dx$. The numerator is not the derivative of the
denominator, so the logarithm pattern fails.

Try $\int \sqrt{4-x^2}\,dx$. That is the area under a semicircle, so an answer
certainly exists, but no substitution in sight produces it.

Each needs its own technique, and this chapter builds four:

**Integration by parts**, which reverses the product rule. This is the most
generally useful technique after substitution and the one the FE is most likely
to require.

**Trigonometric integrals and trigonometric substitution**, which handle powers
of sine and cosine, and radicals of the form $\sqrt{a^2 \pm x^2}$. The
substitution case is where a right triangle does the bookkeeping for you.

**Partial fractions**, which splits a rational function into pieces the table
can handle. Worth more than its exam weight suggests, because it is the engine
of inverse Laplace transforms.

**Improper integrals**, which extend the definite integral to infinite limits
and to integrands that blow up. These answer questions like "what is the total
volume delivered if the pump runs forever" and "how much energy is in the whole
decaying transient," and the answers are often finite.

A word on exam reality before we start, because it affects how hard you should
drill each of these. The FE leans heavily on the Handbook's integral table, and
that table is generous — many integrals that would require trigonometric
substitution by hand are simply printed as results. So the technique that earns
its keep on exam day is **recognizing which table entry applies**, with
integration by parts as the main by-hand skill. I will flag the practical
weight as we go. Everything here is worth understanding; not everything here is
worth memorizing.

We finish with a strategy section — a decision procedure for looking at an
unfamiliar integral and knowing what to try first. That section is the real
deliverable of the chapter.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 21.1 Derive the integration-by-parts formula from the product rule
* 21.2 Choose $u$ and $dv$ effectively and apply integration by parts
* 21.3 Apply integration by parts repeatedly, and resolve the cyclic case
  algebraically
* 21.4 Apply integration by parts to a definite integral, including the boundary
  term
* 21.5 Integrate odd and even powers of sine and cosine using the appropriate
  identity
* 21.6 Select the correct trigonometric substitution for $\sqrt{a^2-x^2}$,
  $\sqrt{a^2+x^2}$, and $\sqrt{x^2-a^2}$
* 21.7 Use a reference triangle to convert a result back to the original
  variable
* 21.8 Decompose a proper rational function into partial fractions for distinct
  linear, repeated linear, and irreducible quadratic factors
* 21.9 Reduce an improper rational function by polynomial division before
  decomposing
* 21.10 Evaluate improper integrals with infinite limits of integration and
  determine convergence
* 21.11 Evaluate improper integrals with an infinite discontinuity in the
  integrand
* 21.12 Apply the $p$-test for convergence
* 21.13 Select an appropriate technique for an unfamiliar integral using a
  systematic strategy

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $u$, $dv$ | the two parts chosen in integration by parts | $u$ gets differentiated, $dv$ gets integrated |
| $du$, $v$ | the results of that differentiation and integration | — |
| $\big[uv\big]_a^b$ | boundary term in definite integration by parts | evaluated, not integrated |
| $I$ | the unknown integral, treated as an algebraic quantity | used in the cyclic case |
| $a$ | the constant in $\sqrt{a^2 \pm x^2}$ | always taken positive |
| $\theta$ | the substitution variable in a trigonometric substitution | — |
| $A$, $B$, $C$ | unknown constants in a partial fraction decomposition | solved for |
| $p$ | the exponent in the convergence test $\int x^{-p}dx$ | — |
| $\displaystyle\lim_{b\to\infty}$ | the limit defining an improper integral | improper integrals are limits, not integrals |
| $\tau$ | time constant of an exponential decay | seconds |
| converges / diverges | the improper integral has a finite value / does not | — |

> ---
> **Mentor's Margin**
>
> A habit to establish before we start, because it changes how you should feel
> about this entire chapter.
>
> **Every result in this chapter can be verified completely, by hand, in under
> a minute.** Differentiate your answer. If you get the integrand back, you are
> right — not probably right, *right*, because the derivative is unique and
> antiderivatives differ only by a constant.
>
> No other topic in mathematics offers that. When you solve an equation you can
> substitute back, which checks one root. When you integrate, differentiating
> your answer checks the whole thing.
>
> So the correct attitude toward a difficult integral is not anxiety about
> whether you picked the right technique. It is: try something, get an answer,
> differentiate it. If the integrand comes back, the technique was right by
> definition. If it does not, you have learned something specific about where
> the error is. I will check every worked example in this chapter this way, and
> you should check every practice problem the same way.
>
> ---

---

## 21.1 Integration by Parts

### Deriving it

Start with the product rule from Chapter 01-17, written with differentials:

$$d(uv) = u\,dv + v\,du$$

Integrate both sides. The left side integrates trivially — it is already a
differential of something:

$$uv = \int u\,dv + \int v\,du$$

Rearrange:

$$\boxed{\int u\,dv = uv - \int v\,du}$$

That is the whole technique. You are trading one integral for another, and the
entire art lies in making the trade favourable.

### What the trade accomplishes

Substitution reverses the chain rule; integration by parts reverses the product
rule. You split the integrand into two factors, **differentiate one** and
**integrate the other**, and hope the resulting integral $\int v\,du$ is easier
than the one you started with.

Sometimes it is dramatically easier. $\int x e^x dx$ becomes $\int e^x dx$
because differentiating $x$ destroys it. That is the paradigm case: choose $u$
to be the factor that *simplifies* when differentiated.

![FIG-01-21-001: Two-panel figure. Left panel titled "Product rule, forward": the expression uv at top with an arrow down to u·dv + v·du, annotated "differentiating a product gives two terms". Right panel titled "By parts, reversed": the integral ∫u dv at top, with an arrow to the rearranged identity uv − ∫v du, and beneath it a small worked instance showing ∫x·eˣdx with u = x and dv = eˣdx tagged, leading to x·eˣ − ∫eˣdx, with the annotation "the new integral is simpler because du = dx destroyed the x". A horizontal double-headed arrow between panels reads "same identity, read in opposite directions".](../figures/FIG-01-21-001-parts-from-product-rule.png)

### Choosing $u$ and $dv$

Two competing requirements, and they usually agree:

- $u$ should get **simpler** when differentiated
- $dv$ should be something you can actually **integrate**

A priority order that works for the overwhelming majority of cases, remembered
by the acronym **LIATE**. Choose $u$ as the first type present in this list:

| Priority | Type | Example | Why it makes a good $u$ |
|---|---|---|---|
| **L** | Logarithmic | $\ln x$ | derivative $\frac{1}{x}$ is algebraic — a big simplification |
| **I** | Inverse trigonometric | $\arctan x$ | derivative is algebraic |
| **A** | Algebraic | $x^2$, $3x$ | derivative reduces the degree |
| **T** | Trigonometric | $\sin x$ | derivative is no simpler, but no worse |
| **E** | Exponential | $e^{3x}$ | derivative is no simpler; easy to integrate, so make it $dv$ |

Whatever is left over becomes $dv$, and the $dx$ always goes with $dv$.

> ---
> **Mentor's Margin**
>
> LIATE is a heuristic, not a theorem, and it is worth knowing why it works
> rather than just obeying it.
>
> The list is ordered by how much a function *improves* under
> differentiation. A logarithm improves enormously — $\ln x$ becomes
> $\frac{1}{x}$, which the power rule handles. A polynomial improves modestly —
> degree drops by one, and enough repetitions will kill it entirely. A sine
> becomes a cosine, no better and no worse. An exponential becomes itself, no
> improvement at all.
>
> So put the biggest improver in the $u$ slot, where differentiation acts on
> it, and put the function that is easiest to integrate in the $dv$ slot. When
> those two instructions conflict — which is rare — the "can I integrate $dv$"
> requirement wins, because an unintegrable $dv$ stops you dead while a poor
> choice of $u$ merely wastes a line.
>
> And if your first attempt makes the integral worse, that is information.
> Swap the choices and try again. You have lost thirty seconds.
>
> ---

### Worked Example 1 — The Paradigm Case

**Given.** $\displaystyle\int x e^x dx$

**Solution.**

By LIATE, the algebraic factor outranks the exponential, so

$$u = x \implies du = dx$$
$$dv = e^x dx \implies v = e^x$$

Apply the formula:

$$\int x e^x dx = x e^x - \int e^x dx = x e^x - e^x + C = \boxed{e^x(x-1) + C}$$

**Check by differentiating.** Using the product rule:

$$\frac{d}{dx}\Big[e^x(x-1)\Big] = e^x(x-1) + e^x(1) = e^x(x - 1 + 1) = x e^x \;\checkmark$$

**What the wrong choice would have given.** Take $u = e^x$ and
$dv = x\,dx$ instead, so $v = \frac{x^2}{2}$:

$$= \frac{x^2 e^x}{2} - \frac{1}{2}\int x^2 e^x dx$$

Valid, but the new integral has a *higher* power of $x$ than the original. The
trade went the wrong way. That is the signature of a bad choice, and the cure is
to swap and restart.

### Worked Example 2 — Integrating a Logarithm

**Given.** $\displaystyle\int \ln x\,dx$

**Solution.**

There is only one factor, which looks like a problem — until you notice that
$dx$ can serve as $dv$ all by itself.

$$u = \ln x \implies du = \frac{dx}{x}$$
$$dv = dx \implies v = x$$

$$\int\ln x\,dx = x\ln x - \int x\cdot\frac{dx}{x} = x\ln x - \int dx$$

$$= \boxed{x\ln x - x + C}$$

**Check.** $\frac{d}{dx}\big(x\ln x - x\big) = \ln x + x\cdot\frac{1}{x} - 1 =
\ln x + 1 - 1 = \ln x$ ✓

This result is worth memorizing outright. It appears often, and the trick that
produces it — taking $dv = dx$ — is the standard move for integrating any
function whose derivative is simpler than itself.

### Repeated application

If one pass leaves an integral of the same species but lower degree, apply the
technique again. A polynomial of degree $n$ against a sine or exponential needs
$n$ passes.

### Worked Example 3 — Parts Applied Twice

**Given.** $\displaystyle\int x^2\sin x\,dx$

**Solution.**

**First pass.** Algebraic beats trigonometric:

$$u = x^2, \quad du = 2x\,dx$$
$$dv = \sin x\,dx, \quad v = -\cos x$$

$$\int x^2\sin x\,dx = -x^2\cos x + \int 2x\cos x\,dx$$

Note the sign: $-\int v\,du = -\int(-\cos x)(2x\,dx) = +\int 2x\cos x\,dx$.

**Second pass** on $\int 2x\cos x\,dx$:

$$u = 2x, \quad du = 2\,dx$$
$$dv = \cos x\,dx, \quad v = \sin x$$

$$\int 2x\cos x\,dx = 2x\sin x - \int 2\sin x\,dx = 2x\sin x + 2\cos x$$

**Assemble.**

$$\boxed{\int x^2\sin x\,dx = -x^2\cos x + 2x\sin x + 2\cos x + C}$$

**Check.** Differentiate term by term:

$$\frac{d}{dx}\left(-x^2\cos x\right) = -2x\cos x + x^2\sin x$$
$$\frac{d}{dx}\left(2x\sin x\right) = 2\sin x + 2x\cos x$$
$$\frac{d}{dx}\left(2\cos x\right) = -2\sin x$$

Sum: $-2x\cos x + x^2\sin x + 2\sin x + 2x\cos x - 2\sin x = x^2\sin x$ ✓

Four terms cancelled in pairs, which is the usual pattern when checking a
repeated-parts result. If nothing cancels, look for a sign error.

### The cyclic case

Some integrals return to themselves after two passes. That looks like failure
and is actually the solution — you get an **equation** for the integral, which
you solve algebraically.

### Worked Example 4 — Solving for the Integral

**Given.** $\displaystyle I = \int e^x\sin x\,dx$

**Solution.**

**First pass.** By LIATE, trigonometric outranks exponential, so $u = \sin x$:

$$u = \sin x, \quad du = \cos x\,dx$$
$$dv = e^x dx, \quad v = e^x$$

$$I = e^x\sin x - \int e^x\cos x\,dx$$

**Second pass** on $\int e^x\cos x\,dx$, keeping the same choice of role —
this consistency is essential:

$$u = \cos x, \quad du = -\sin x\,dx$$
$$dv = e^x dx, \quad v = e^x$$

$$\int e^x\cos x\,dx = e^x\cos x + \int e^x\sin x\,dx = e^x\cos x + I$$

**Substitute back.**

$$I = e^x\sin x - \Big[e^x\cos x + I\Big] = e^x\sin x - e^x\cos x - I$$

Now treat $I$ as an unknown and solve:

$$2I = e^x\left(\sin x - \cos x\right)$$

$$\boxed{I = \frac{e^x\left(\sin x - \cos x\right)}{2} + C}$$

**Check.**

$$\frac{d}{dx}\left[\frac{e^x(\sin x - \cos x)}{2}\right] = \frac{e^x(\sin x - \cos x) + e^x(\cos x + \sin x)}{2} = \frac{2e^x\sin x}{2} = e^x\sin x \;\checkmark$$

> ---
> **Mentor's Margin**
>
> The cyclic case has one trap that ruins it, and it is worth naming precisely.
>
> On the second pass you **must keep the same assignment of roles**. If the
> first pass put the trigonometric factor in $u$, the second pass must too. Swap
> them and the second pass exactly undoes the first, you arrive at the tautology
> $I = I$, and you have proved nothing.
>
> Students who hit $I = I$ usually conclude that parts does not work here. It
> does. Go back and check that both passes differentiated the same species of
> factor.
>
> This integral family is not academic, incidentally. $e^{-\alpha t}\sin\omega t$
> is a damped oscillation — the response of essentially every underdamped
> mechanical or electrical system to a disturbance. Integrating it gives the
> accumulated response, and you will meet it again in differential equations and
> in transient circuit analysis.
>
> ---

### Definite integrals by parts

The boundary term is evaluated rather than carried:

$$\boxed{\int_a^b u\,dv = \Big[uv\Big]_a^b - \int_a^b v\,du}$$

### Worked Example 5 — Definite Parts

**Given.** $\displaystyle\int_0^1 x e^{2x}dx$

**Solution.**

$$u = x, \quad du = dx$$
$$dv = e^{2x}dx, \quad v = \frac{e^{2x}}{2}$$

$$\int_0^1 x e^{2x}dx = \left[\frac{xe^{2x}}{2}\right]_0^1 - \int_0^1\frac{e^{2x}}{2}dx$$

Boundary term: $\frac{1\cdot e^2}{2} - 0 = \frac{e^2}{2}$

Remaining integral: $\frac{1}{2}\left[\frac{e^{2x}}{2}\right]_0^1 =
\frac{e^2}{4} - \frac{1}{4}$

$$= \frac{e^2}{2} - \frac{e^2}{4} + \frac{1}{4} = \frac{e^2}{4} + \frac{1}{4} = \frac{e^2+1}{4}$$

With $e^2 = 7.389056$:

$$= \frac{8.389056}{4} = \boxed{2.0973}$$

**Check by bounding.** On $[0,1]$ the integrand $xe^{2x}$ runs from 0 to
$e^2 = 7.389$, and it is increasing and concave up. The trapezoidal estimate
$\frac{0 + 7.389}{2}(1) = 3.69$ overestimates a concave-up function's integral,
and our 2.097 is comfortably below it ✓ The midpoint estimate
$0.5e^{1} = 1.359$ underestimates, and 2.097 sits between the two ✓

---

## 21.2 Trigonometric Integrals

Powers and products of trigonometric functions yield to the identities from
Chapter 01-11, used to reshape the integrand into something substitution can
handle.

### Odd powers — peel one off

If **either** sine or cosine appears to an **odd** power, split off one factor
and convert the rest using $\sin^2\theta + \cos^2\theta = 1$. The peeled factor
becomes the $du$.

### Worked Example 6 — Odd Power

**Given.** $\displaystyle\int\sin^3 x\cos^2 x\,dx$

**Solution.**

Sine appears to an odd power. Peel one sine off and convert the remaining
$\sin^2 x$:

$$\sin^3 x = \sin^2 x\cdot\sin x = \left(1 - \cos^2 x\right)\sin x$$

$$\int\left(1-\cos^2 x\right)\cos^2 x\,\sin x\,dx$$

Now substitute $u = \cos x$, so $du = -\sin x\,dx$ and $\sin x\,dx = -du$:

$$= \int\left(1-u^2\right)u^2(-du) = -\int\left(u^2 - u^4\right)du = -\frac{u^3}{3} + \frac{u^5}{5} + C$$

$$= \boxed{-\frac{\cos^3 x}{3} + \frac{\cos^5 x}{5} + C}$$

**Check.**

$$\frac{d}{dx}\left[-\frac{\cos^3x}{3}\right] = -\frac{3\cos^2x(-\sin x)}{3} = \cos^2x\sin x$$
$$\frac{d}{dx}\left[\frac{\cos^5x}{5}\right] = \frac{5\cos^4x(-\sin x)}{5} = -\cos^4x\sin x$$

Sum: $\cos^2x\sin x - \cos^4x\sin x = \sin x\cos^2x\left(1 - \cos^2x\right) =
\sin^3x\cos^2x$ ✓

### Even powers — use power reduction

When **all** powers are even, there is no factor to peel. Use the power-reduction
identities from Chapter 01-11:

$$\sin^2\theta = \frac{1-\cos 2\theta}{2} \qquad \cos^2\theta = \frac{1+\cos 2\theta}{2}$$

### Worked Example 7 — Even Power, With an RMS Cross-Check

**Given.** $\displaystyle\int_0^{\pi/2}\sin^2 x\,dx$

**Solution.**

$$= \int_0^{\pi/2}\frac{1-\cos 2x}{2}dx = \frac{1}{2}\left[x - \frac{\sin 2x}{2}\right]_0^{\pi/2}$$

At $x = \frac{\pi}{2}$: $\sin\pi = 0$, so the bracket is $\frac{\pi}{2}$.
At $x = 0$: both terms vanish.

$$= \frac{1}{2}\cdot\frac{\pi}{2} = \boxed{\frac{\pi}{4} \approx 0.7854}$$

**Cross-check against Chapter 01-20.** The average value of $\sin^2 x$ over
$\left[0, \frac{\pi}{2}\right]$ is

$$\frac{1}{\pi/2}\cdot\frac{\pi}{4} = \frac{1}{2}$$

exactly one half. That is precisely the fact that made the RMS value of a
sinusoid come out to $\frac{V_m}{\sqrt{2}}$ in Worked Example 14 of Chapter
01-20: the mean of the square is $\frac{V_m^2}{2}$, and the root of that is
$\frac{V_m}{\sqrt{2}}$ ✓ Same integral, met from a different direction.

---

## 21.3 Trigonometric Substitution

Radicals of the form $\sqrt{a^2 \pm x^2}$ and $\sqrt{x^2 - a^2}$ resist ordinary
substitution because there is no inner derivative to absorb. The fix is to
*introduce* a trigonometric variable chosen so that a Pythagorean identity
eliminates the radical.

| Radical | Substitution | Identity used | Radical becomes |
|---|---|---|---|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1-\sin^2 = \cos^2$ | $a\cos\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1+\tan^2 = \sec^2$ | $a\sec\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2-1 = \tan^2$ | $a\tan\theta$ |

The pattern is worth reading rather than memorizing: in each case the
substitution is chosen so the identity turns a sum or difference of squares into
a single perfect square, and the square root then comes off cleanly.

### The reference triangle

Converting back to $x$ at the end is where errors happen, and a **reference
triangle** eliminates them. Draw the right triangle implied by the
substitution, label its sides from the Pythagorean theorem, and read off any
trigonometric function of $\theta$ you need.

![FIG-01-21-002: Three right triangles side by side, one per substitution case. Left, labeled "x = a sinθ": hypotenuse a, side opposite θ equal to x, adjacent side √(a² − x²), with sinθ = x/a annotated. Centre, labeled "x = a tanθ": adjacent side a, opposite side x, hypotenuse √(a² + x²), with tanθ = x/a annotated. Right, labeled "x = a secθ": hypotenuse x, adjacent side a, opposite side √(x² − a²), with secθ = x/a annotated. Beneath each triangle, the radical that the substitution eliminates is printed in a box, and a note reads "read any trig function of θ directly off the triangle".](../figures/FIG-01-21-002-reference-triangles.png)

### Worked Example 8 — Sine Case, Verified Geometrically

**Given.** $\displaystyle\int\sqrt{4-x^2}\,dx$

**Solution.**

Here $a = 2$. Substitute $x = 2\sin\theta$, so $dx = 2\cos\theta\,d\theta$ and

$$\sqrt{4 - 4\sin^2\theta} = 2\sqrt{1-\sin^2\theta} = 2\cos\theta$$

$$\int\sqrt{4-x^2}\,dx = \int 2\cos\theta\cdot 2\cos\theta\,d\theta = 4\int\cos^2\theta\,d\theta$$

An even power — use power reduction, as in §21.2:

$$= 4\int\frac{1+\cos 2\theta}{2}d\theta = 2\theta + \sin 2\theta + C$$

Now convert back. Use the double-angle identity from Chapter 01-11,
$\sin 2\theta = 2\sin\theta\cos\theta$, and read the triangle: with
$\sin\theta = \frac{x}{2}$, the adjacent side is $\sqrt{4-x^2}$, so
$\cos\theta = \frac{\sqrt{4-x^2}}{2}$.

$$\sin 2\theta = 2\cdot\frac{x}{2}\cdot\frac{\sqrt{4-x^2}}{2} = \frac{x\sqrt{4-x^2}}{2}$$

And $\theta = \arcsin\frac{x}{2}$:

$$\boxed{\int\sqrt{4-x^2}\,dx = 2\arcsin\frac{x}{2} + \frac{x\sqrt{4-x^2}}{2} + C}$$

**Check geometrically.** The curve $y = \sqrt{4-x^2}$ is the upper half of the
circle $x^2+y^2 = 4$, so $\int_0^2\sqrt{4-x^2}\,dx$ is a **quarter circle** of
radius 2:

$$\text{exact area} = \frac{\pi r^2}{4} = \frac{4\pi}{4} = \pi$$

From our antiderivative, at $x = 2$: $2\arcsin(1) + 0 = 2\cdot\frac{\pi}{2} =
\pi$. At $x = 0$: both terms are zero.

$$\int_0^2\sqrt{4-x^2}\,dx = \pi \;\checkmark$$

Exact agreement with elementary geometry. That is the strongest possible check
on a trigonometric substitution, and it is available whenever the radical
describes a circle.

### Worked Example 9 — Tangent Case

**Given.** $\displaystyle\int\frac{dx}{\left(x^2+9\right)^{3/2}}$

**Solution.**

Here $a = 3$ and the form is $\sqrt{a^2+x^2}$ raised to a power, so substitute
$x = 3\tan\theta$, $dx = 3\sec^2\theta\,d\theta$:

$$\left(x^2+9\right)^{3/2} = \left(9\tan^2\theta + 9\right)^{3/2} = \left[9\sec^2\theta\right]^{3/2} = 27\sec^3\theta$$

$$\int\frac{3\sec^2\theta\,d\theta}{27\sec^3\theta} = \frac{1}{9}\int\frac{d\theta}{\sec\theta} = \frac{1}{9}\int\cos\theta\,d\theta = \frac{\sin\theta}{9} + C$$

From the reference triangle with $\tan\theta = \frac{x}{3}$: opposite $= x$,
adjacent $= 3$, hypotenuse $= \sqrt{x^2+9}$, so
$\sin\theta = \frac{x}{\sqrt{x^2+9}}$.

$$\boxed{\int\frac{dx}{\left(x^2+9\right)^{3/2}} = \frac{x}{9\sqrt{x^2+9}} + C}$$

**Check.** Differentiate using the product and chain rules, writing the answer
as $\frac{1}{9}x\left(x^2+9\right)^{-1/2}$:

$$\frac{1}{9}\left[\left(x^2+9\right)^{-1/2} + x\left(-\tfrac12\right)\left(x^2+9\right)^{-3/2}(2x)\right]$$

$$= \frac{1}{9}\left(x^2+9\right)^{-3/2}\Big[\left(x^2+9\right) - x^2\Big] = \frac{1}{9}\left(x^2+9\right)^{-3/2}(9) = \frac{1}{\left(x^2+9\right)^{3/2}} \;\checkmark$$

> ---
> **Mentor's Margin**
>
> Honest assessment of exam weight, because this technique costs more to learn
> than it returns on the FE.
>
> The Handbook's integral table already contains the standard results for
> $\frac{1}{\sqrt{a^2-x^2}}$, $\frac{1}{a^2+x^2}$, and several related forms. If
> an exam problem needs one of those, you look it up in fifteen seconds. Carrying
> out a full trigonometric substitution under exam time pressure is almost never
> the right play.
>
> So learn this technique to the level of **recognition**: see a
> $\sqrt{a^2-x^2}$ and know that the answer involves an arcsine, see a
> $\frac{1}{a^2+x^2}$ and know it involves an arctangent. That recognition helps
> you find the right table entry, which is the actual exam skill.
>
> Understand the mechanism once, work a few by hand so the table entries are not
> magic, then rely on the table. Spend the drill time you save on integration by
> parts and partial fractions, which pay better.
>
> ---

---

## 21.4 Partial Fractions

A rational function — a polynomial over a polynomial — can usually be split into
a sum of simpler fractions, each of which the table handles. The method reverses
the algebra of combining fractions over a common denominator.

### Prerequisites for the method

Two conditions must hold before you decompose:

**The fraction must be proper.** The numerator's degree must be strictly less
than the denominator's. If not, divide first — polynomial long division gives a
polynomial plus a proper remainder fraction.

**The denominator must be factored.** Use the root-finding and factoring
techniques from Chapter 01-07.

### The decomposition forms

| Denominator factor | Contributes to the decomposition |
|---|---|
| distinct linear $(x-r)$ | $\dfrac{A}{x-r}$ |
| repeated linear $(x-r)^n$ | $\dfrac{A_1}{x-r} + \dfrac{A_2}{(x-r)^2} + \cdots + \dfrac{A_n}{(x-r)^n}$ |
| irreducible quadratic $\left(x^2+bx+c\right)$ | $\dfrac{Ax+B}{x^2+bx+c}$ |
| repeated irreducible quadratic | one such term per power |

Note the pattern: a repeated factor needs **every** power from 1 up to $n$, and
an irreducible quadratic needs a **linear** numerator, not a constant.

![FIG-01-21-003: Flow diagram for partial fractions. Top box: "rational function N(x)/D(x)". First decision diamond: "is deg N < deg D?" — the "no" branch leads to a box "polynomial long division → quotient + proper remainder" which feeds back in; the "yes" branch continues down. Second box: "factor D(x) completely". Then three parallel branches labeled by factor type — distinct linear, repeated linear, irreducible quadratic — each showing its template term. All three converge into a box "solve for constants: substitute convenient roots, or equate coefficients". Final box: "integrate each term — logarithms, powers, arctangents".](../figures/FIG-01-21-003-partial-fractions-flow.png)

### Solving for the constants

Two methods, and they combine well:

**Substitute convenient values.** Clear the denominators, then substitute each
root of the denominator. Each substitution kills all terms but one, isolating a
single constant. Fast and clean for distinct linear factors.

**Equate coefficients.** Expand both sides and match coefficients of like powers,
producing a linear system. Necessary for quadratic factors, where no real
substitution isolates the constants.

### Worked Example 10 — Distinct Linear Factors

**Given.** $\displaystyle\int\frac{5x-3}{x^2-2x-3}\,dx$

**Solution.**

**Check proper.** Numerator degree 1, denominator degree 2 ✓

**Factor.** $x^2-2x-3 = (x-3)(x+1)$

**Set up the decomposition.**

$$\frac{5x-3}{(x-3)(x+1)} = \frac{A}{x-3} + \frac{B}{x+1}$$

**Clear denominators.**

$$5x - 3 = A(x+1) + B(x-3)$$

**Substitute the roots.**

At $x = 3$: $15 - 3 = A(4) + B(0) \implies 12 = 4A \implies A = 3$

At $x = -1$: $-5-3 = A(0) + B(-4) \implies -8 = -4B \implies B = 2$

**Integrate.**

$$\int\left(\frac{3}{x-3} + \frac{2}{x+1}\right)dx = \boxed{3\ln\lvert x-3\rvert + 2\ln\lvert x+1\rvert + C}$$

**Check the decomposition algebraically** before trusting the integral:

$$\frac{3}{x-3} + \frac{2}{x+1} = \frac{3(x+1) + 2(x-3)}{(x-3)(x+1)} = \frac{3x+3+2x-6}{x^2-2x-3} = \frac{5x-3}{x^2-2x-3} \;\checkmark$$

**Check the integral by differentiating.**
$\frac{3}{x-3} + \frac{2}{x+1}$, which we have just shown equals the
integrand ✓

Note the absolute values on both logarithms — the $n = -1$ discipline from
Chapter 01-19 applies to every term.

### Worked Example 11 — Repeated Linear Factor

**Given.** $\displaystyle\int\frac{x+4}{x^2+2x+1}\,dx$

**Solution.**

**Factor.** $x^2+2x+1 = (x+1)^2$ — a repeated linear factor.

Here the numerator is simple enough for a direct rewrite, which is faster than
setting up constants. Write $x + 4 = (x+1) + 3$:

$$\frac{x+4}{(x+1)^2} = \frac{(x+1) + 3}{(x+1)^2} = \frac{1}{x+1} + \frac{3}{(x+1)^2}$$

$$\int\left[\frac{1}{x+1} + 3(x+1)^{-2}\right]dx = \ln\lvert x+1\rvert + 3\cdot\frac{(x+1)^{-1}}{-1} + C$$

$$= \boxed{\ln\lvert x+1\rvert - \frac{3}{x+1} + C}$$

**Check.**

$$\frac{d}{dx}\left[\ln\lvert x+1\rvert - 3(x+1)^{-1}\right] = \frac{1}{x+1} + 3(x+1)^{-2} = \frac{(x+1) + 3}{(x+1)^2} = \frac{x+4}{(x+1)^2} \;\checkmark$$

**The systematic route, for comparison.** Setting
$\frac{x+4}{(x+1)^2} = \frac{A}{x+1} + \frac{B}{(x+1)^2}$ and clearing gives
$x + 4 = A(x+1) + B$. At $x = -1$: $3 = B$. Matching the $x$ coefficient:
$A = 1$. Same result ✓ Use the systematic route when the rewrite is not obvious.

> ---
> **Mentor's Margin**
>
> The error that defines repeated factors: writing only
> $\frac{A}{(x+1)^2}$ and omitting the $\frac{A_1}{x+1}$ term.
>
> Count the unknowns against the degree. A denominator of degree 2 requires two
> unknown constants to represent a general numerator of degree 1. One term gives
> you one constant, which cannot possibly match an arbitrary linear numerator.
> The decomposition would be under-determined, and the algebra will fail —
> usually by producing an inconsistent system, which is at least an honest
> failure.
>
> The general rule: **the number of unknown constants must equal the degree of
> the denominator.** Count them before you start solving. That single check
> catches nearly every setup error in this topic.
>
> ---

### Worked Example 12 — Irreducible Quadratic

**Given.** $\displaystyle\int\frac{2x+1}{x\left(x^2+1\right)}\,dx$

**Solution.**

**Factors.** $x$ is linear; $x^2+1$ has no real roots (its discriminant is
negative, by Chapter 01-07), so it is irreducible and takes a linear numerator.

$$\frac{2x+1}{x\left(x^2+1\right)} = \frac{A}{x} + \frac{Bx+C}{x^2+1}$$

Three unknowns for a degree-3 denominator ✓

**Clear denominators.**

$$2x+1 = A\left(x^2+1\right) + (Bx+C)x = Ax^2 + A + Bx^2 + Cx$$

**Equate coefficients.**

| Power | Left | Right | Result |
|---|---|---|---|
| $x^2$ | $0$ | $A + B$ | $B = -A$ |
| $x^1$ | $2$ | $C$ | $C = 2$ |
| $x^0$ | $1$ | $A$ | $A = 1$ |

So $A = 1$, $B = -1$, $C = 2$.

**Integrate.**

$$\int\left[\frac{1}{x} + \frac{-x+2}{x^2+1}\right]dx = \int\frac{dx}{x} - \int\frac{x\,dx}{x^2+1} + 2\int\frac{dx}{x^2+1}$$

The three pieces, in order: a logarithm; a substitution $u = x^2+1$ giving
$\frac{1}{2}\ln\lvert u\rvert$; and a table arctangent.

$$= \boxed{\ln\lvert x\rvert - \frac{1}{2}\ln\left(x^2+1\right) + 2\arctan x + C}$$

**Check.**

$$\frac{1}{x} - \frac{1}{2}\cdot\frac{2x}{x^2+1} + \frac{2}{1+x^2} = \frac{1}{x} - \frac{x}{x^2+1} + \frac{2}{x^2+1}$$

$$= \frac{1}{x} + \frac{2-x}{x^2+1} = \frac{\left(x^2+1\right) + x(2-x)}{x\left(x^2+1\right)} = \frac{x^2+1+2x-x^2}{x\left(x^2+1\right)} = \frac{2x+1}{x\left(x^2+1\right)} \;\checkmark$$

Note the pattern worth carrying: a linear numerator over an irreducible
quadratic splits into a **logarithm** piece (the part proportional to the
denominator's derivative) and an **arctangent** piece (the constant remainder).
Every such term does.

> **Preview note.** Partial fractions carries more weight than its share of
> integration problems suggests, because it is the standard tool for **inverse
> Laplace transforms** later in Tier 1C. There you will take a transfer function
> — a ratio of polynomials in $s$ — decompose it exactly as we have here, and
> read each term's time-domain counterpart off a table. The decomposition skill
> transfers unchanged; only the table on the far side differs. If you invest in
> one technique from this chapter beyond parts, invest in this one. Nothing in
> the present chapter depends on that later material.

---

## 21.5 Improper Integrals

Chapter 01-19 defined $\int_a^b f\,dx$ for a finite interval and a bounded
integrand. Two extensions matter in engineering, and both are handled by taking
a limit.

### Type 1 — infinite limit of integration

$$\boxed{\int_a^{\infty}f(x)\,dx = \lim_{b\to\infty}\int_a^b f(x)\,dx}$$

If the limit exists and is finite, the integral **converges** to that value. If
not, it **diverges**.

For both limits infinite, split at any convenient point and require **both**
halves to converge independently.

### Type 2 — infinite discontinuity in the integrand

If $f$ blows up at an endpoint, approach that endpoint with a limit. For a
singularity at $x = a$:

$$\int_a^b f(x)\,dx = \lim_{t\to a^+}\int_t^b f(x)\,dx$$

If the singularity is *interior* to the interval, split there and treat each
side separately.

> ---
> **Mentor's Margin**
>
> Write the limit. Every time.
>
> $\infty$ is not a number, and substituting it into an antiderivative as
> though it were is how people conclude that divergent integrals converge. The
> notation $\big[F(x)\big]_1^{\infty}$ has no meaning until you interpret it as
> $\lim_{b\to\infty}\big[F(b) - F(1)\big]$.
>
> In practice you will often evaluate these by inspection once you are fluent —
> looking at $e^{-b}$ and knowing it goes to zero. That is fine. But on an exam,
> and in any calculation you will have to defend, write the limit symbol. It
> costs three characters and it forces you to actually ask whether the limit
> exists, which is the entire question being posed.
>
> The same discipline applies to Type 2. A singularity hiding *inside* the
> interval is the nastier case, because the ordinary evaluation notation
> produces a confident, finite, completely wrong number. Check whether your
> integrand is bounded on the interval **before** you apply the Fundamental
> Theorem. The Fundamental Theorem requires continuity, and it is not optional.
>
> ---

### Worked Example 13 — Convergent and Divergent

**(a)** $\displaystyle\int_1^{\infty}\frac{dx}{x^2}$

$$= \lim_{b\to\infty}\int_1^b x^{-2}dx = \lim_{b\to\infty}\left[-\frac{1}{x}\right]_1^b = \lim_{b\to\infty}\left(-\frac{1}{b} + 1\right)$$

$$= 0 + 1 = \boxed{1 \quad \text{converges}}$$

**(b)** $\displaystyle\int_1^{\infty}\frac{dx}{x}$

$$= \lim_{b\to\infty}\Big[\ln\lvert x\rvert\Big]_1^b = \lim_{b\to\infty}\left(\ln b - 0\right) = \infty$$

$$\boxed{\text{diverges}}$$

**(c)** $\displaystyle\int_0^1\frac{dx}{\sqrt{x}}$ — Type 2, singular at $x = 0$

$$= \lim_{t\to 0^+}\int_t^1 x^{-1/2}dx = \lim_{t\to 0^+}\left[2\sqrt{x}\right]_t^1 = \lim_{t\to 0^+}\left(2 - 2\sqrt{t}\right)$$

$$= \boxed{2 \quad \text{converges}}$$

**Reflect on (a) versus (b).** Both integrands shrink to zero as $x$ grows, and
their graphs look similar. One encloses a finite area over an infinite interval;
the other does not. The difference is entirely in *how fast* the decay happens,
and the boundary between the two behaviours is sharp.

![FIG-01-21-004: Two side-by-side plots on identical axes over 1 ≤ x ≤ 12, both with the region under the curve shaded and the shading fading off to the right edge with an arrow indicating continuation to infinity. Left plot, y = 1/x², annotated "area = 1, converges" with the curve dropping steeply. Right plot, y = 1/x, annotated "area infinite, diverges" with the curve dropping more gently. Between them a vertical divider carries the p-test summary: "∫₁^∞ x^(−p) dx converges if p > 1, diverges if p ≤ 1". A note beneath reads "both integrands → 0; only the rate of decay decides".](../figures/FIG-01-21-004-improper-convergence.png)

### The $p$-test

The general result behind that comparison:

$$\boxed{\int_1^{\infty}\frac{dx}{x^p} \quad \begin{cases}\text{converges to } \dfrac{1}{p-1} & p > 1\\[2mm] \text{diverges} & p \le 1\end{cases}}$$

And near a singularity at the origin, the test inverts:

$$\boxed{\int_0^{1}\frac{dx}{x^p} \quad \begin{cases}\text{converges to } \dfrac{1}{1-p} & p < 1\\[2mm] \text{diverges} & p \ge 1\end{cases}}$$

The two are worth holding together, because the inversion is counterintuitive
and the boundary case $p = 1$ diverges in both. Check the results in Worked
Example 13 against both tests: (a) has $p = 2 > 1$ ✓ converges to
$\frac{1}{2-1} = 1$ ✓; (b) has $p = 1$ ✓ diverges; (c) has $p = \frac{1}{2} < 1$
✓ converges to $\frac{1}{1-0.5} = 2$ ✓

### Worked Example 14 — Total Volume from a Decaying Flow

**Given.** The pump from Chapter 01-19 delivers $Q(t) = 18e^{-t/25}$ L/s, with
$t$ in seconds.

**Find.** The total volume delivered if the pump runs indefinitely, and explain
why the answer is finite.

**Solution.**

$$V = \int_0^{\infty}18e^{-t/25}dt = \lim_{b\to\infty}18\left[\frac{e^{-t/25}}{-1/25}\right]_0^b = \lim_{b\to\infty}\left(-450\right)\left[e^{-t/25}\right]_0^b$$

$$= -450\lim_{b\to\infty}\left(e^{-b/25} - 1\right) = -450(0 - 1) = \boxed{450 \text{ L}}$$

**Units check.** $\frac{\text{L}}{\text{s}}\cdot\text{s} = $ L ✓

**Why finite?** The flow decays exponentially, and exponential decay is fast
enough that the accumulated total converges. The general result is worth
extracting:

$$\int_0^{\infty}Q_0 e^{-t/\tau}dt = Q_0\tau$$

Total delivered volume equals the **initial rate times the time constant**.
Here: $18(25) = 450$ L ✓ That is a relationship worth memorizing — it turns a
family of exponential-decay integrals into a one-line multiplication.

**Cross-check against the finite case.** Chapter 01-19 asked for the volume in
the first 60 s. That is

$$450\left(1 - e^{-60/25}\right) = 450\left(1 - e^{-2.4}\right) = 450(1 - 0.090718) = 450(0.909282) = 409.2 \text{ L}$$

So 91% of the eventual total arrives in the first 60 s, which is $2.4\tau$.
Consistent with the rule of thumb from Chapter 01-16 that an exponential process
is substantially complete after a few time constants ✓

---

## 21.6 A Strategy for Integration

This is the section to return to when an unfamiliar integral appears. Work down
the list; stop at the first thing that applies.

**1. Simplify the integrand algebraically first.** Expand products, divide
through, split a sum over a common denominator, apply a trigonometric identity.
A surprising number of intimidating integrals collapse to table entries after
one line of algebra.

**2. Look for a table entry.** The Handbook's integral table is broad. Check it
before doing any work.

**3. Try substitution.** Is there an inner function whose derivative appears as
a factor, up to a constant? This is the highest-yield technique and the cheapest
to test.

**4. Classify the integrand and match the technique.**

| If the integrand is | Try |
|---|---|
| a product of unlike species ($x e^x$, $x\sin x$, $x\ln x$) | integration by parts |
| a lone logarithm or inverse trig function | parts with $dv = dx$ |
| powers of sine and cosine, one odd | peel one factor, substitute |
| powers of sine and cosine, all even | power-reduction identities |
| $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$, $\sqrt{x^2-a^2}$ | table first, then trig substitution |
| a rational function | partial fractions (divide first if improper) |
| $\frac{g'}{g}$ | logarithm, directly |

**5. Check the limits.** Infinite limit, or unbounded integrand anywhere on the
interval? It is improper — write the limit.

**6. Differentiate your answer.** Always.

![FIG-01-21-005: A vertical decision flowchart titled "which technique?". Starting box: "unfamiliar integral". Sequential decision diamonds, each with a "yes" branch exiting right to a labeled technique box and a "no" branch continuing down: "can algebra simplify it?" → simplify and restart; "is it in the table?" → look it up; "inner function with its derivative present?" → substitution; "product of unlike species?" → by parts; "powers of sin/cos?" → identities; "radical of a² ± x²?" → trig substitution; "rational function?" → partial fractions. The bottom box reads "no elementary antiderivative — use numerical methods (Ch 01-37)". A final box across the base, connected to every technique box by dashed lines, reads "differentiate your answer to verify".](../figures/FIG-01-21-005-integration-strategy.png)

> ---
> **Mentor's Margin**
>
> One thing to accept, because it is true and nobody says it early enough.
>
> **Most functions have no elementary antiderivative.** Not "are hard to
> integrate" — have none, provably, no matter how clever you are. $e^{-x^2}$,
> whose integral defines the normal distribution you will meet in Chapter 01-40.
> $\frac{\sin x}{x}$. $\sqrt{1+x^4}$, which is an ordinary arc length integrand.
> These are not exotic; the first two are among the most important functions in
> engineering.
>
> This is not a gap in your technique. It is a fact about the elementary
> functions, and it is why numerical integration in Chapter 01-37 is not a
> fallback for the lazy — it is the primary method for a large fraction of real
> integrals, and the only method for some.
>
> So when an integral resists everything on the list, consider that it may
> genuinely have no closed form. Set it up correctly, then integrate it
> numerically. Setting it up correctly is the part that requires you.
>
> ---

---

## 21.7 Engineering Application: Impulse of a Force Pulse

### Worked Example 15 — Combining Four Chapters

**Given.** A short-duration impact generates a force

$$F(t) = F_0\left(\frac{t}{\tau}\right)e^{-t/\tau}$$

with $F_0 = 500$ N and $\tau = 0.040$ s.

**(a)** Find the time of peak force and the peak value.
**(b)** Find the total impulse $J = \int_0^{\infty}F\,dt$.
**(c)** Determine the fraction of the total impulse delivered in the first
$0.040$ s.

**Solution.**

**(a) Peak force** — an optimization from Chapter 01-18. Differentiate using the
product rule, with $F = \frac{F_0}{\tau}te^{-t/\tau}$:

$$\frac{dF}{dt} = \frac{F_0}{\tau}\left[e^{-t/\tau} + t\left(-\frac{1}{\tau}\right)e^{-t/\tau}\right] = \frac{F_0}{\tau}e^{-t/\tau}\left(1 - \frac{t}{\tau}\right)$$

Set to zero. The exponential never vanishes, so:

$$1 - \frac{t}{\tau} = 0 \implies t = \tau = \boxed{0.040 \text{ s}}$$

**Verify it is a maximum** by a sign test on $\frac{dF}{dt}$, whose sign is the
sign of $\left(1-\frac{t}{\tau}\right)$:

| $t$ | $1 - t/\tau$ | $dF/dt$ |
|---|---|---|
| $< \tau$ | $+$ | rising |
| $> \tau$ | $-$ | falling |

Changes $+ \to -$: a maximum ✓

$$F_{\max} = F_0(1)e^{-1} = 500(0.367879) = \boxed{184 \text{ N}}$$

Note that the peak force is only 37% of the nominal $F_0$ — the scale constant
is not the peak.

**(b) Total impulse** — improper integral requiring integration by parts.

$$J = \int_0^{\infty}\frac{F_0}{\tau}t e^{-t/\tau}dt$$

Evaluate $\int_0^{\infty}te^{-at}dt$ with $a = \frac{1}{\tau}$, by parts:

$$u = t, \quad du = dt$$
$$dv = e^{-at}dt, \quad v = -\frac{e^{-at}}{a}$$

$$\int_0^{b}te^{-at}dt = \left[-\frac{te^{-at}}{a}\right]_0^{b} + \frac{1}{a}\int_0^{b}e^{-at}dt$$

The boundary term at $b$ is $-\frac{be^{-ab}}{a}$, and as $b\to\infty$ this
goes to **zero** — because an exponential decay beats linear growth, which is
exactly the $\frac{\infty}{\infty}$ result L'Hôpital's rule gave us in Chapter
01-18. The term at $t = 0$ is zero outright.

$$= \frac{1}{a}\lim_{b\to\infty}\left[-\frac{e^{-at}}{a}\right]_0^{b} = \frac{1}{a}\cdot\frac{1}{a} = \frac{1}{a^2} = \tau^2$$

So:

$$J = \frac{F_0}{\tau}\cdot\tau^2 = F_0\tau = 500(0.040) = \boxed{20.0 \text{ N}\cdot\text{s}}$$

**Units check.** N·s is the unit of impulse, and equals kg·m/s — a momentum ✓

**Structural check.** $J = F_0\tau$ is tidy, and it must be dimensionally: the
only way to combine a force and a time into an impulse. Compare with the
result in Worked Example 14, where a simple exponential gave
$Q_0\tau$. The extra $t/\tau$ factor here did not change the form of the answer,
only which constant appears.

**(c) Fraction delivered by $t = \tau$.**

Using the antiderivative from (b) with $a = \frac{1}{\tau}$, evaluated at a
finite limit:

$$\int_0^{\tau}te^{-t/\tau}dt = \left[-\tau te^{-t/\tau}\right]_0^{\tau} + \tau\int_0^{\tau}e^{-t/\tau}dt$$

$$= -\tau^2 e^{-1} + \tau\left[-\tau e^{-t/\tau}\right]_0^{\tau} = -\tau^2 e^{-1} - \tau^2\left(e^{-1} - 1\right)$$

$$= \tau^2\left(1 - 2e^{-1}\right) = \tau^2\left(1 - 0.735759\right) = 0.264241\,\tau^2$$

Against the total $\tau^2$:

$$\text{fraction} = \boxed{26.4\%}$$

**Interpretation.** The force peaks at $t = \tau$, yet only about a quarter of
the impulse has been delivered by then. Nearly three quarters arrives during the
decaying tail. That is a genuinely useful thing to know about impact loading: the
peak force tells you about local damage, while the impulse — which governs the
change in momentum — is dominated by the part of the event that happens *after*
the peak.

![FIG-01-21-006: Plot of F(t) = 500(t/0.04)e^(−t/0.04) N against t from 0 to 0.25 s. The curve rises steeply from the origin to a marked peak at (0.040, 184) with a horizontal tangent segment and label "F_max = 184 N at t = τ", then decays with a long tail approaching zero. The region under the curve from 0 to τ is shaded dark and labeled "26.4% of impulse"; the region from τ onward is shaded light and labeled "73.6% of impulse", with an arrow indicating continuation to infinity. A dashed horizontal line at F₀ = 500 N is labeled "scale constant F₀ — not the peak".](../figures/FIG-01-21-006-force-pulse-impulse.png)

---

## As the Handbook States It

> **Handbook 10.6, Mathematics section (begins p. 36)** — these techniques
> appear in the *Integral Calculus* subsection, approximately pp. 46–48,
> alongside the material from Chapter 01-19.

The Handbook's coverage here is **partial**, and the split is worth knowing
before exam day.

**What's in the Handbook — find it fast:**

- **Integration by parts**, stated as $\int u\,dv = uv - \int v\,du$. The
  formula is printed; the choice of $u$ and $dv$ is yours.
- **The integral table**, which already contains many results that would
  otherwise require trigonometric substitution — the arcsine and arctangent
  forms in particular. Check the table before starting any substitution.
- **Standard forms with radical and quadratic denominators**, including
  $\int\frac{dx}{a^2+x^2}$ and related entries.
- **Trigonometric identities**, in the algebra and trigonometry portion of the
  Mathematics section. The power-reduction and double-angle identities you need
  for §21.2 are printed there, so you need not memorize them — but you do need
  to know they exist and which one to reach for.

**What's not in the Handbook — memorize:**

- The **LIATE** priority for choosing $u$, and the underlying reasoning
- How to resolve the **cyclic case** by treating the integral as an algebraic
  unknown, and the requirement to keep role assignments consistent between
  passes
- The trick of taking $dv = dx$ to integrate a lone logarithm or inverse
  trigonometric function
- $\int\ln x\,dx = x\ln x - x + C$
- The **odd/even strategy** for powers of sine and cosine: peel one factor if a
  power is odd, use power reduction if all are even
- Which **trigonometric substitution** matches each radical, and the reference
  triangle method for converting back
- The full **partial fractions** procedure: check proper, factor, choose the
  correct template per factor type, count that the number of constants equals
  the denominator's degree
- That a **repeated** factor requires every power from 1 to $n$, and an
  **irreducible quadratic** requires a linear numerator
- That an **improper integral is a limit**, and the limit must be written
- The **$p$-test** in both its forms, at infinity and at a singularity
- That an **interior singularity** must be split and that the Fundamental
  Theorem does not apply across one
- $\int_0^{\infty}Q_0e^{-t/\tau}dt = Q_0\tau$ and
  $\int_0^{\infty}te^{-t/\tau}dt = \tau^2$
- The **strategy order** from §21.6
- That many functions have **no elementary antiderivative**, so numerical
  methods are a primary tool and not a concession

> ---
> **Mentor's Margin**
>
> Exam strategy for this chapter, stated bluntly.
>
> **Integration by parts is the one to drill.** It is printed in the Handbook as
> a formula, which means the exam can reasonably expect you to execute it, and
> execution requires a good choice of $u$ that the Handbook cannot make for you.
> Work enough of these that LIATE is a reflex.
>
> **Partial fractions is second**, and its real payoff is later, in Laplace
> transform work.
>
> **Trigonometric substitution is third, and distantly.** Learn to recognize the
> radical forms so you can find the right table entry. Do not spend hours
> becoming fluent at executing the substitution by hand.
>
> **Improper integrals are worth the small investment** they require, because the
> convergence question is conceptual rather than computational and shows up in
> problems about totals over unbounded time.
>
> Budget your practice accordingly. There is more material in this chapter than
> the FE will ask about, and I would rather tell you that than have you allocate
> a week to trigonometric substitution.
>
> ---

---

## Where This Goes Wrong

**Choosing $u$ and $dv$ backwards.** If the new integral is worse than the
original — higher degree, more complicated — swap the choices and restart. A bad
choice is not wrong, just unproductive.

**Sign errors in the parts formula.** It is $uv - \int v\,du$. When $v$ is
itself negative, as with $v = -\cos x$, the two minus signs combine to a plus.
Write the intermediate step out rather than doing it mentally.

**Swapping roles between passes in the cyclic case.** Both passes must
differentiate the same species of factor. Swapping produces the useless
identity $I = I$.

**Forgetting to solve for $I$ in the cyclic case.** When the original integral
reappears, you have an equation, not a dead end. Collect and divide.

**Omitting the boundary term in definite parts.** $\big[uv\big]_a^b$ is
evaluated and kept. Dropping it discards a real contribution.

**Peeling the wrong factor in a trigonometric integral.** Peel from the function
with the **odd** power, so that the remaining even power converts cleanly via
the Pythagorean identity.

**Attempting to peel when all powers are even.** There is nothing to peel. Use
power reduction.

**Choosing the wrong trigonometric substitution.** Match the radical to the
identity: difference of squares with $x$ second takes sine; sum of squares takes
tangent; difference with $x$ first takes secant.

**Failing to convert back to the original variable.** An answer in $\theta$ is
not an answer. Use the reference triangle.

**Decomposing an improper rational function.** If the numerator's degree is not
strictly less than the denominator's, divide first. Skipping this produces an
inconsistent system.

**Omitting lower-power terms for a repeated factor.** $(x+1)^3$ in the
denominator needs three terms, with denominators $(x+1)$, $(x+1)^2$, and
$(x+1)^3$.

**Using a constant numerator over an irreducible quadratic.** It must be
$\frac{Ax+B}{x^2+bx+c}$. A bare constant cannot represent the general case.

**Miscounting the constants.** The number of unknowns must equal the degree of
the denominator. Count before solving.

**Dropping absolute values in the logarithms.** Every partial-fraction
logarithm needs $\ln\lvert\cdot\rvert$, for the reason given in Chapter 01-19.

**Substituting $\infty$ into an antiderivative.** Write the limit. $\infty$ is
not a value.

**Missing an interior singularity.** Check whether the integrand is bounded
everywhere on the interval *before* applying the Fundamental Theorem. An
unnoticed interior blow-up yields a finite, confident, wrong answer.

**Concluding convergence because the integrand tends to zero.**
$\frac{1}{x} \to 0$ and $\int_1^{\infty}\frac{dx}{x}$ diverges anyway. The rate
of decay decides, and the $p$-test is the arbiter.

**Inverting the $p$-test.** At infinity, large $p$ converges. At a singularity,
small $p$ converges. The boundary $p = 1$ diverges in both cases.

**Assuming an antiderivative exists.** Many integrands have no elementary
antiderivative. If nothing on the strategy list applies, the honest answer may
be a numerical one.

---

## Key Terms

| Term | Definition |
|---|---|
| Integration by parts | Technique reversing the product rule: $\int u\,dv = uv - \int v\,du$ |
| LIATE | Priority order for selecting $u$: logarithmic, inverse trig, algebraic, trigonometric, exponential |
| Boundary term | The $\big[uv\big]_a^b$ contribution in definite integration by parts |
| Cyclic integral | One that reproduces itself after repeated parts, solved algebraically |
| Power reduction | Identities expressing $\sin^2$ and $\cos^2$ in terms of $\cos 2\theta$ |
| Trigonometric substitution | Introducing $x = a\sin\theta$, $a\tan\theta$, or $a\sec\theta$ to eliminate a radical |
| Reference triangle | Right triangle encoding a substitution, used to convert results back to $x$ |
| Rational function | A ratio of polynomials |
| Proper fraction | One whose numerator degree is less than its denominator degree |
| Partial fractions | Decomposition of a proper rational function into a sum of simpler fractions |
| Irreducible quadratic | A quadratic with no real roots; takes a linear numerator in a decomposition |
| Improper integral | One with an infinite limit of integration or an unbounded integrand |
| Converges | The defining limit exists and is finite |
| Diverges | The defining limit does not exist or is infinite |
| $p$-test | Convergence criterion for $\int x^{-p}dx$ at infinity ($p>1$) or at a singularity ($p<1$) |
| Elementary function | One built from powers, roots, exponentials, logarithms, and trigonometric functions |

---

## Review Questions

### Conceptual

1. Derive the integration-by-parts formula from the product rule. State which
   part of the integrand gets differentiated and which gets integrated.
2. Explain the reasoning behind the LIATE ordering. Why does a logarithm
   outrank a polynomial as a choice of $u$?
3. You apply integration by parts and the new integral is more complicated than
   the original. What has gone wrong, and what should you do?
4. In the cyclic case, why must the role assignment stay the same on the second
   pass? What happens if it does not?
5. Explain why $\int\ln x\,dx$ can be done by parts even though the integrand
   appears to have only one factor.
6. Given $\int\sin^4x\cos^3x\,dx$, state which function to peel a factor from
   and why.
7. Why does the substitution $x = a\tan\theta$ eliminate the radical in
   $\sqrt{a^2+x^2}$? Identify the identity doing the work.
8. State the two conditions a rational function must satisfy before you attempt
   a partial fraction decomposition, and what to do if each fails.
9. Explain why $(x-2)^3$ in a denominator requires three terms rather than one.
   Use the counting rule in your explanation.
10. Both $\frac{1}{x}$ and $\frac{1}{x^2}$ tend to zero as $x\to\infty$, yet
    only one has a convergent integral on $[1,\infty)$. Explain what
    distinguishes them.
11. Why must an improper integral be written as a limit rather than evaluated by
    substituting $\infty$?
12. A student evaluates $\int_{-1}^{1}\frac{dx}{x^2}$ as
    $\left[-\frac{1}{x}\right]_{-1}^{1} = -1 - 1 = -2$. Identify two things
    wrong with this, and give the correct treatment.
13. Explain what it means for a function to have no elementary antiderivative,
    and name two engineering-relevant examples.

### Calculation

14. Integrate by parts:
    (a) $\displaystyle\int x e^{-3x}dx$
    (b) $\displaystyle\int x\cos x\,dx$
    (c) $\displaystyle\int x\ln x\,dx$
    (d) $\displaystyle\int \arctan x\,dx$

15. Apply parts twice:
    (a) $\displaystyle\int x^2 e^{x}dx$
    (b) $\displaystyle\int \left(\ln x\right)^2 dx$

16. Resolve the cyclic case: $\displaystyle\int e^{-2t}\cos(3t)\,dt$

17. Evaluate the definite integrals:
    (a) $\displaystyle\int_0^{\pi}x\sin x\,dx$
    (b) $\displaystyle\int_1^{e}\ln x\,dx$

18. Trigonometric integrals:
    (a) $\displaystyle\int\cos^3 x\,dx$
    (b) $\displaystyle\int\sin^2 x\cos^2 x\,dx$
    (c) $\displaystyle\int_0^{\pi}\sin^2 x\,dx$

19. Trigonometric substitution:
    (a) $\displaystyle\int\frac{dx}{\sqrt{9-x^2}}$ — then locate the
    corresponding Handbook table entry and compare
    (b) $\displaystyle\int\sqrt{25-x^2}\,dx$, then use it to evaluate
    $\displaystyle\int_0^5\sqrt{25-x^2}\,dx$ and check against the area of a
    quarter circle

20. Partial fractions:
    (a) $\displaystyle\int\frac{dx}{x^2-4}$
    (b) $\displaystyle\int\frac{3x+11}{x^2-x-6}dx$
    (c) $\displaystyle\int\frac{2x-1}{(x-1)^2}dx$
    (d) $\displaystyle\int\frac{x^2+1}{x\left(x^2+4\right)}dx$

21. Reduce first, then decompose:
    $\displaystyle\int\frac{x^2+3x+1}{x^2-1}dx$

22. Determine convergence and evaluate where possible:
    (a) $\displaystyle\int_1^{\infty}\frac{dx}{x^3}$
    (b) $\displaystyle\int_1^{\infty}\frac{dx}{\sqrt{x}}$
    (c) $\displaystyle\int_0^{\infty}e^{-4t}dt$
    (d) $\displaystyle\int_0^{1}\frac{dx}{x^{2/3}}$
    (e) $\displaystyle\int_0^{2}\frac{dx}{x-2}$

23. **Engineering application.** A capacitor discharge produces current
    $i(t) = 2.5e^{-t/0.020}$ A, with $t$ in seconds.
    (a) Write the integral for total charge delivered as $t\to\infty$, with
    units.
    (b) Evaluate it using the $Q_0\tau$ relation, then verify by carrying out
    the improper integral.
    (c) Find the fraction of the total charge delivered in the first 20 ms.
    (d) The energy dissipated in a $15\ \Omega$ resistor is
    $\int_0^{\infty}i^2R\,dt$. Evaluate it, and note the time constant of the
    squared current compared with the current itself.

24. **Engineering application.** A tapered column has cross-sectional area
    $A(x) = 0.040e^{-x/6.0}$ m², with $x$ in metres measured from the base and
    total height 4.0 m. The material has weight density
    $\gamma = 24{,}000$ N/m³.
    (a) Set up and evaluate the integral for the total weight.
    (b) Find the height of the centroid of the volume, which requires
    $\int x A(x)\,dx$ — integrate by parts.
    (c) State the units at each step and confirm they are consistent.

### Multiple Choice

25. $\displaystyle\int x\sin x\,dx$ equals:
    A) $-x\cos x + \sin x + C$
    B) $x\cos x - \sin x + C$
    C) $-x\cos x - \sin x + C$
    D) $\dfrac{x^2}{2}(-\cos x) + C$

26. In applying parts to $\displaystyle\int x^2\ln x\,dx$, the best choice of
    $u$ is:
    A) $x^2$
    B) $\ln x$
    C) $x^2\ln x$
    D) $dx$

27. The correct substitution for $\displaystyle\int\frac{dx}{\sqrt{x^2-16}}$ is:
    A) $x = 4\sin\theta$
    B) $x = 4\tan\theta$
    C) $x = 4\sec\theta$
    D) $u = x^2 - 16$

28. The partial fraction decomposition of
    $\dfrac{3x}{(x-1)^2(x+2)}$ requires how many unknown constants?
    A) 2
    B) 3
    C) 4
    D) 6

29. $\displaystyle\int_1^{\infty}\frac{dx}{x^{1.5}}$:
    A) diverges
    B) converges to 1
    C) converges to 2
    D) converges to 0.5

30. $\displaystyle\int_0^{\infty}5e^{-t/8}dt$ equals:
    A) $5$
    B) $8$
    C) $40$
    D) diverges

31. Which integrand has **no** elementary antiderivative?
    A) $xe^{x}$
    B) $e^{-x^2}$
    C) $\dfrac{1}{x^2-1}$
    D) $x\ln x$

---

## Summary Card

**Integration by parts**

$$\int u\,dv = uv - \int v\,du \qquad \int_a^b u\,dv = \Big[uv\Big]_a^b - \int_a^b v\,du$$

Choose $u$ by **LIATE**: Logarithmic, Inverse trig, Algebraic, Trigonometric,
Exponential. Cyclic case: solve algebraically for $I$, keeping roles consistent
across passes. Lone logarithm or inverse trig: take $dv = dx$.

$$\int\ln x\,dx = x\ln x - x + C$$

**Trigonometric integrals**

Odd power present → peel one factor, convert the rest with
$\sin^2+\cos^2 = 1$, substitute.
All powers even → power reduction:
$\sin^2\theta = \frac{1-\cos2\theta}{2}$, $\cos^2\theta = \frac{1+\cos2\theta}{2}$.

**Trigonometric substitution**

| Radical | Substitute | Becomes |
|---|---|---|
| $\sqrt{a^2-x^2}$ | $x = a\sin\theta$ | $a\cos\theta$ |
| $\sqrt{a^2+x^2}$ | $x = a\tan\theta$ | $a\sec\theta$ |
| $\sqrt{x^2-a^2}$ | $x = a\sec\theta$ | $a\tan\theta$ |

Convert back with the reference triangle. Check the Handbook table first.

**Partial fractions**

Require **proper** (else divide) and **factored**. Number of constants = degree
of denominator.

| Factor | Template |
|---|---|
| $(x-r)$ | $\frac{A}{x-r}$ |
| $(x-r)^n$ | every power from 1 to $n$ |
| irreducible $x^2+bx+c$ | $\frac{Ax+B}{x^2+bx+c}$ |

Linear over irreducible quadratic → a logarithm piece plus an arctangent piece.

**Improper integrals** — always write the limit.

$$\int_a^{\infty}f\,dx = \lim_{b\to\infty}\int_a^b f\,dx$$

$p$-test: $\int_1^{\infty}x^{-p}dx$ converges iff $p>1$;
$\int_0^{1}x^{-p}dx$ converges iff $p<1$. Both diverge at $p=1$.
Interior singularity → split; the Fundamental Theorem does not cross one.

**Exponential results worth memorizing**

$$\int_0^{\infty}Q_0e^{-t/\tau}dt = Q_0\tau \qquad \int_0^{\infty}te^{-t/\tau}dt = \tau^2$$

**Strategy order**

Simplify algebraically → check the table → substitution → classify and match
(parts, identities, trig sub, partial fractions) → check for impropriety →
**differentiate to verify**.

Many integrands have no elementary antiderivative. Set those up correctly and
integrate numerically (Chapter 01-37).

---

*Next: [Chapter 01-22 — Partial Derivatives and Multivariable Calculus](01-22-partial-derivatives.md)*