---
chapter: "01-22"
title: "Infinite Series and Taylor Expansions"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-022-01, MATH-1C-022-02, MATH-1C-022-03, MATH-1C-022-04, MATH-1C-022-05, MATH-1C-022-06]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-22: Infinite Series and Taylor Expansions

> *"An engineer almost never needs a function. What an engineer needs is a
> polynomial that behaves like the function over the range that matters, because
> polynomials can be differentiated, integrated, solved, and computed, and most
> functions cannot. Taylor's theorem hands you that polynomial and — this is the
> part that makes it engineering rather than mathematics — tells you how wrong it
> is. Every linearization you will ever perform is this chapter, whether anyone
> says so or not."*

---

## Before You Start

**Prerequisites:** [01-05 Exponents, Radicals, and Logarithms](01-05-exponents-radicals-logarithms.md) · [01-07 Polynomials and Their Roots](01-07-polynomials-roots.md) · [01-11 Trigonometry](01-11-trigonometry.md) · [01-15 Sequences, Series, and Progressions](01-15-sequences-series-progressions.md) · [01-16 Limits and Continuity](01-16-limits-continuity.md) · [01-17 The Derivative](01-17-the-derivative.md) · [01-18 Applications of the Derivative](01-18-applications-of-the-derivative.md) · [01-21 Techniques of Integration](01-21-techniques-of-integration.md)

**Skip if:** You pass the Tier 1C test-out quiz. Verify you can determine
convergence with the ratio test, write the Maclaurin series for $e^x$, $\sin x$,
and $\cos x$ from memory, and bound the truncation error of a small-angle
approximation before skipping. The standard expansions are the item worth being
honest about — recognizing them is graded far more often than deriving them, and
recognition requires having them memorized.

**Time:** ~75 min read · ~25 min review questions · ~75 min practice problems

---

## On the Board Today

Apprentice, Chapter 01-15 taught you finite sums and the geometric series.
Chapter 01-21 finished the integration techniques. Both feed into this chapter,
and this chapter is where the whole of calculus collapses into something you can
actually compute with.

Start with the honest version of a question you may not have asked. When your
calculator reports $\sin 0.3 = 0.29552$, where did that come from? There is no
finite formula for a sine. No amount of arithmetic on 0.3 produces 0.29552. So
what is the machine doing?

It is adding up a series:

$$\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$$

Three terms give $0.3 - 0.0045 + 0.00002025 = 0.29552$, correct to five
decimals. The transcendental function has been replaced by a polynomial, and the
polynomial is exact enough that nobody notices the substitution.

That is the idea of the chapter, and it comes in three parts.

**Convergence.** An infinite sum may or may not settle on a finite value. Adding
$1 + \frac{1}{2} + \frac{1}{4} + \cdots$ converges to 2. Adding
$1 + \frac{1}{2} + \frac{1}{3} + \cdots$ grows without bound, slowly but
genuinely without bound. Distinguishing the two cases requires tests, and one of
those tests is an improper integral from Chapter 01-21, which is why this chapter
sits here rather than next to 01-15.

**Taylor expansion.** Given a function and a point, there is a recipe that
generates the polynomial matching it best near that point. The coefficients are
the function's derivatives, which is why we needed Chapter 01-17 first. The
first-degree case is exactly the linear approximation from Chapter 01-18 — we are
generalizing something you already use.

**Truncation error.** You will never sum infinitely many terms. You will cut the
series off, and the difference between your polynomial and the true function is
the truncation error. Bounding it is what separates an approximation you can
defend from a guess. When somebody asks "is small-angle theory valid here," they
are asking for a truncation error bound, and this chapter is how you answer.

A note on exam weight, as in Chapter 01-21. The convergence tests are worth
understanding and are lightly tested. The **standard expansions and the
small-angle approximations are heavily used**, not always in problems labelled
"series" — they appear inside statics, dynamics, circuits, and thermodynamics
problems where a linearization is assumed silently. Drill the expansions. Read
the convergence tests.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 22.1 Distinguish a sequence from a series and define convergence in terms of
  partial sums
* 22.2 Apply the $n$th term test for divergence and explain why it cannot prove
  convergence
* 22.3 Evaluate a convergent geometric series and state its convergence
  condition
* 22.4 Apply the integral test and derive the $p$-series result from it
* 22.5 Apply the comparison test to a series of positive terms
* 22.6 Apply the ratio test, including recognizing the inconclusive case
* 22.7 Apply the alternating series test and distinguish absolute from
  conditional convergence
* 22.8 Determine the radius and interval of convergence of a power series
* 22.9 Construct the Taylor series of a function about a given point
* 22.10 Write the Maclaurin series for $e^x$, $\sin x$, $\cos x$, $\ln(1+x)$,
  $\frac{1}{1-x}$, and $(1+x)^n$ from memory
* 22.11 Bound the truncation error of a Taylor polynomial using the Lagrange
  remainder, and of an alternating series using the first omitted term
* 22.12 Apply small-angle approximations and quantify the angle range over which
  they meet a stated error tolerance
* 22.13 Linearize a nonlinear relationship about an operating point and state the
  range of validity

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $a_n$ | the $n$th term of a sequence or series | — |
| $\displaystyle\sum_{n=1}^{\infty}a_n$ | infinite series | from Chapter 01-15 |
| $S_n$ | $n$th partial sum, $a_1 + \cdots + a_n$ | a finite number |
| $S$ | the sum of the series, $\lim_{n\to\infty}S_n$ | exists only if convergent |
| $r$ | common ratio of a geometric series | converges iff $\lvert r\rvert < 1$ |
| $p$ | exponent in a $p$-series $\sum n^{-p}$ | — |
| $L$ | the limit computed in the ratio test | — |
| $f^{(n)}(a)$ | $n$th derivative of $f$ evaluated at $a$ | $f^{(0)} = f$ |
| $n!$ | factorial, $n(n-1)\cdots(1)$, with $0! = 1$ | from Chapter 01-15 |
| $a$ | the **centre** of a Taylor expansion | not a series term here |
| $R$ | radius of convergence of a power series | a distance in $x$ |
| $P_n(x)$ | Taylor polynomial of degree $n$ | the truncated series |
| $E_n(x)$ | truncation error, $f(x) - P_n(x)$ | written $R_n$ in many texts |
| $c$ | the unknown interior point in the Lagrange remainder | not a constant |
| $\theta$ | angle, **in radians** | non-negotiable in this chapter |

> ---
> **Mentor's Margin**
>
> Three notation cautions, because this chapter recycles letters that already
> mean other things.
>
> **$R$ versus $E_n$.** Most textbooks write the truncation error as $R_n$ for
> "remainder," which collides with $R$ for radius of convergence. I use $E_n$ for
> the error to keep them apart. When you read other sources, check which is
> meant — a subscript almost always indicates the remainder.
>
> **$a$ means the centre.** In the convergence sections $a_n$ is a series term.
> In the Taylor sections $a$ is the point you expand about. Same letter, unrelated
> jobs, and the convention is universal so there is no fixing it. Context is
> unambiguous in practice: if it has a subscript it is a term, if it appears
> inside $(x-a)$ it is the centre.
>
> **Every angle in this chapter is in radians.** The series for $\sin\theta$ is
> false in degrees — flatly, numerically false, not approximately. $\sin 30° =
> 0.5$, while the first series term with $\theta = 30$ gives 30. If a problem
> states degrees, convert before you expand anything. This is the single most
> common way a small-angle calculation goes wrong, and it goes wrong by a factor
> of 57.3.
>
> ---

---

## 22.1 Series, Partial Sums, and Convergence

A **sequence** is an ordered list of numbers. A **series** is what you get when
you add a sequence up. Chapter 01-15 handled the finite case; now the list does
not stop.

Define the **partial sums**:

$$S_1 = a_1, \quad S_2 = a_1 + a_2, \quad \ldots \quad S_n = \sum_{k=1}^{n}a_k$$

Each $S_n$ is an ordinary finite sum, so each is a perfectly well-defined number.
The infinite series is then defined as the **limit of the partial sums**:

$$\boxed{\sum_{n=1}^{\infty}a_n = \lim_{n\to\infty}S_n = S}$$

If that limit exists and is finite, the series **converges** to $S$. Otherwise it
**diverges**.

Notice what this definition accomplishes: it never asks you to perform infinitely
many additions. It asks a limit question about a sequence of finite sums, and
limits are Chapter 01-16 material. Infinite series are not a new kind of
arithmetic; they are a limit wearing a summation sign.

![FIG-01-22-001: Two stacked panels sharing a horizontal n-axis from 1 to 20. Upper panel plots the partial sums of Σ1/2ⁿ as discrete dots rising and levelling off, with a dashed horizontal asymptote at S = 1 labeled "converges to 1" and the vertical gaps between the dots and the asymptote visibly shrinking. Lower panel plots the partial sums of the harmonic series Σ1/n as discrete dots rising steadily with no levelling, annotated "still climbing at n = 20, and at n = 10⁶ — diverges". A note beneath reads "in both cases the terms aₙ → 0".](../figures/FIG-01-22-001-partial-sums.png)

### The $n$th term test for divergence

> If $\displaystyle\lim_{n\to\infty}a_n \ne 0$, the series $\sum a_n$
> **diverges**.

The reasoning is immediate: if the terms do not shrink toward zero, each addition
keeps moving the partial sum by a non-vanishing amount, so the sum cannot settle.

**The converse is false, and this is the trap.** Terms shrinking to zero does
*not* imply convergence. The harmonic series $\sum\frac{1}{n}$ has terms going to
zero and diverges anyway — its terms simply do not shrink fast enough. That is
exactly the lesson of $\int_1^{\infty}\frac{dx}{x}$ diverging in Chapter 01-21,
and the next section makes the connection formal.

So the $n$th term test is a **one-way** test. It can prove divergence. It can
never prove convergence, and "the terms go to zero so it converges" is a wrong
statement.

### Worked Example 1 — The $n$th Term Test

**Determine whether each series diverges by the $n$th term test.**

**(a)** $\displaystyle\sum_{n=1}^{\infty}\frac{n}{n+1}$

$$\lim_{n\to\infty}\frac{n}{n+1} = 1 \ne 0 \implies \boxed{\text{diverges}}$$

The terms approach 1, so the partial sums grow without bound — roughly like $n$.

**(b)** $\displaystyle\sum_{n=1}^{\infty}\frac{3n^2+1}{n^2-4n}$

Divide through by $n^2$, as in Chapter 01-16:

$$\lim_{n\to\infty}\frac{3 + 1/n^2}{1 - 4/n} = 3 \ne 0 \implies \boxed{\text{diverges}}$$

**(c)** $\displaystyle\sum_{n=1}^{\infty}\frac{1}{\sqrt{n}}$

$$\lim_{n\to\infty}\frac{1}{\sqrt{n}} = 0$$

$$\boxed{\text{test is inconclusive}}$$

Not "converges." The test has simply failed to decide. (It happens to diverge, as
the $p$-test in §22.2 will show with $p = \frac{1}{2}$.)

### Geometric series, revisited

From Chapter 01-15, with first term $a$ and common ratio $r$:

$$\boxed{\sum_{n=0}^{\infty}ar^n = \frac{a}{1-r} \qquad \text{for } \lvert r\rvert < 1}$$

For $\lvert r\rvert \ge 1$ it diverges. This is the one series whose sum you can
always write down in closed form, and it turns up constantly — in
perpetuity calculations in engineering economics, in repeated-reflection
problems, and as the comparison standard for other series.

### Worked Example 2 — Geometric Series

**(a)** $\displaystyle\sum_{n=0}^{\infty}0.6^n$

Here $a = 1$, $r = 0.6$, and $\lvert r\rvert < 1$ ✓

$$S = \frac{1}{1-0.6} = \frac{1}{0.4} = \boxed{2.50}$$

**Check numerically.** Partial sums: $1, 1.6, 1.96, 2.176, 2.306, 2.383,
2.430, \ldots$ — climbing toward 2.5 and slowing ✓

**(b)** $\displaystyle\sum_{n=1}^{\infty}\frac{5}{3^n}$

Write out the first term to identify $a$: at $n=1$ the term is $\frac{5}{3}$, and
each subsequent term is $\frac{1}{3}$ of the last.

$$S = \frac{5/3}{1 - 1/3} = \frac{5/3}{2/3} = \boxed{2.50}$$

**(c)** $\displaystyle\sum_{n=0}^{\infty}(1.02)^n$

$\lvert r\rvert = 1.02 > 1$, so $\boxed{\text{diverges}}$. Also caught by the
$n$th term test, since $1.02^n \to \infty$.

---

## 22.2 Tests for Convergence

### The integral test

This is the bridge back to Chapter 01-21. If $f$ is positive, continuous, and
decreasing for $x \ge 1$, and $a_n = f(n)$, then

$$\boxed{\sum_{n=1}^{\infty}a_n \text{ and } \int_1^{\infty}f(x)\,dx \text{ both converge or both diverge}}$$

The picture is the argument. The series is a sum of rectangle areas of width 1 and
height $f(n)$; the integral is the area under the curve. Neither can be finite
while the other is infinite, because each traps the other between two copies of
itself.

**Warning:** the test decides *whether* the series converges. It does **not** give
the sum. The integral's value is not the series' value — they bracket each other
but do not agree.

![FIG-01-22-002: The decreasing curve y = f(x) drawn over 1 ≤ x ≤ 7 with the area beneath it lightly shaded. Superimposed are two sets of unit-width rectangles: one set drawn with heights f(1), f(2), … inscribed to the left of each curve segment so the rectangles sit above the curve, hatched in one direction and labeled "Σ overestimates ∫"; a second set with heights f(2), f(3), … sitting below the curve, hatched the other way and labeled "Σ underestimates ∫". A caption reads "series and integral trap each other — both finite or both infinite" and a smaller note warns "same convergence, different values".](../figures/FIG-01-22-002-integral-test.png)

### The $p$-series

Apply the integral test to $f(x) = x^{-p}$ and the $p$-test from Chapter 01-21
transfers directly:

$$\boxed{\sum_{n=1}^{\infty}\frac{1}{n^p} \quad\begin{cases}\text{converges} & p > 1\\ \text{diverges} & p \le 1\end{cases}}$$

The boundary case $p = 1$ is the **harmonic series**, and it diverges. Worth
sitting with for a moment: the harmonic series diverges so slowly that summing a
million terms gets you only to about 14.4, and reaching 100 requires more terms
than there are atoms in a person. It diverges nonetheless. Numerical evidence
cannot settle a convergence question — only a test can.

### Worked Example 3 — Integral Test

**(a)** $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$

$p = 2 > 1$, so it **converges** by the $p$-test.

Confirm by the integral test, using the Chapter 01-21 result
$\int_1^{\infty}x^{-2}dx = 1$ — finite, so the series converges ✓

Note the series does **not** sum to 1. Its actual sum is
$\frac{\pi^2}{6} = 1.6449$, which the integral test never claimed to provide.

**(b)** $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n\ln n}$

The terms go to zero, so the $n$th term test is useless. Try the integral,
substituting $u = \ln x$, $du = \frac{dx}{x}$:

$$\int_2^{\infty}\frac{dx}{x\ln x} = \lim_{b\to\infty}\Big[\ln\lvert\ln x\rvert\Big]_2^{b} = \lim_{b\to\infty}\Big[\ln(\ln b) - \ln(\ln 2)\Big] = \infty$$

$$\boxed{\text{diverges}}$$

A striking case: the terms shrink faster than $\frac{1}{n}$ and it still
diverges. There is no simple "fast enough" intuition that replaces the test.

### The comparison test

For series of **positive** terms:

- If $a_n \le b_n$ and $\sum b_n$ converges, then $\sum a_n$ converges
- If $a_n \ge b_n$ and $\sum b_n$ diverges, then $\sum a_n$ diverges

Squeeze your series against a known one. The usual comparison standards are
$p$-series and geometric series, which is why those two are worth knowing cold.

### Worked Example 4 — Comparison

**(a)** $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$

For every $n \ge 1$:

$$\frac{1}{n^2+1} < \frac{1}{n^2}$$

and $\sum\frac{1}{n^2}$ converges ($p = 2$), so $\boxed{\text{converges}}$.

**(b)** $\displaystyle\sum_{n=1}^{\infty}\frac{1}{\sqrt{n}-0.5}$ for $n \ge 1$

$$\frac{1}{\sqrt{n}-0.5} > \frac{1}{\sqrt{n}}$$

and $\sum\frac{1}{\sqrt{n}}$ diverges ($p = \frac{1}{2} \le 1$), so
$\boxed{\text{diverges}}$.

Note the direction of each inequality carefully. A comparison in the wrong
direction proves nothing at all: a series smaller than a divergent one may
converge or diverge, and the test is silent.

### The ratio test

The most broadly useful test, and the one that governs power series.

$$L = \lim_{n\to\infty}\left\lvert\frac{a_{n+1}}{a_n}\right\rvert$$

$$\boxed{\begin{cases}L < 1 & \text{converges absolutely}\\ L > 1 & \text{diverges}\\ L = 1 & \text{inconclusive}\end{cases}}$$

The intuition: if consecutive terms settle into a fixed ratio less than one, the
tail behaves like a geometric series with that ratio, and geometric series with
$\lvert r\rvert<1$ converge.

The ratio test is especially effective on factorials and on $n$th powers, because
those simplify enormously in a ratio.

> ---
> **Mentor's Margin**
>
> $L = 1$ means **the test has failed**, not that the series converges and not
> that it diverges. Move to a different test.
>
> And note that $L = 1$ is not a rare edge case. Every $p$-series gives
> $L = 1$:
>
> $$\left\lvert\frac{a_{n+1}}{a_n}\right\rvert = \frac{n^p}{(n+1)^p} = \left(\frac{n}{n+1}\right)^p \to 1$$
>
> for any $p$. So the ratio test cannot distinguish $\sum\frac{1}{n}$ from
> $\sum\frac{1}{n^2}$, one of which diverges and the other converges. That is a
> clean demonstration that no single test suffices, and it explains why $p$-series
> get their own result rather than being handled by the general machinery.
>
> Practical order of attack: check the $n$th term test first, because it is free.
> Recognize $p$-series and geometric series on sight. Reach for the ratio test
> when factorials or $n$th powers appear. Use the integral test when the term
> looks like a function you can integrate. Use comparison when it looks like
> something you already know.
>
> ---

### Worked Example 5 — Ratio Test

**(a)** $\displaystyle\sum_{n=1}^{\infty}\frac{n}{2^n}$

$$\left\lvert\frac{a_{n+1}}{a_n}\right\rvert = \frac{n+1}{2^{n+1}}\cdot\frac{2^n}{n} = \frac{n+1}{2n} \to \frac{1}{2}$$

$L = 0.5 < 1$, so $\boxed{\text{converges}}$.

**(b)** $\displaystyle\sum_{n=0}^{\infty}\frac{1}{n!}$

$$\left\lvert\frac{a_{n+1}}{a_n}\right\rvert = \frac{n!}{(n+1)!} = \frac{1}{n+1} \to 0$$

$L = 0 < 1$, so $\boxed{\text{converges}}$.

This series sums to $e = 2.71828$, as §22.4 will show. The factorial in the
denominator makes it converge very fast, which is why exponentials are cheap to
compute.

**(c)** $\displaystyle\sum_{n=1}^{\infty}\frac{n!}{10^n}$

$$\left\lvert\frac{a_{n+1}}{a_n}\right\rvert = \frac{(n+1)!}{10^{n+1}}\cdot\frac{10^n}{n!} = \frac{n+1}{10} \to \infty$$

$L = \infty > 1$, so $\boxed{\text{diverges}}$. Factorial growth defeats any fixed
exponential, eventually — here from about $n = 10$ onward.

### Alternating series

A series whose terms alternate in sign:

$$\sum_{n=1}^{\infty}(-1)^{n+1}b_n = b_1 - b_2 + b_3 - \cdots \qquad b_n > 0$$

> **Alternating series test.** If $b_n$ is decreasing and $b_n \to 0$, the series
> converges.

Alternation is a powerful stabilizer. The partial sums oscillate above and below
the limit, each overshoot smaller than the last, so they are squeezed onto a
value.

The **alternating harmonic series** demonstrates this:

$$1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots = \ln 2 = 0.6931$$

It converges, while the same terms without alternating signs diverge. A series
that converges but whose absolute values do not is **conditionally convergent**.
When $\sum\lvert a_n\rvert$ converges, the series is **absolutely convergent**,
which is the stronger and better-behaved condition.

### The alternating series error bound

This is the practical payoff, and we will use it repeatedly in §22.5.

> For a convergent alternating series, truncating after $n$ terms leaves an error
> **no larger than the first omitted term**:
>
> $$\boxed{\lvert S - S_n\rvert \le b_{n+1}}$$

One term gives you a rigorous error bound. No other error estimate in this
chapter is that cheap.

---

## 22.3 Power Series

A **power series** centred at $a$ is

$$\sum_{n=0}^{\infty}c_n(x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$$

Now convergence depends on $x$. The set of $x$ for which the series converges is
its **interval of convergence**, and the distance from the centre to the edge of
that interval is the **radius of convergence** $R$.

Find $R$ with the ratio test: set $L < 1$ and solve for $\lvert x - a\rvert$.

The endpoints must be checked **separately**, by substituting each one and testing
the resulting numerical series. The ratio test always gives $L = 1$ at an
endpoint, so it cannot decide them.

![FIG-01-22-003: A horizontal number line with the centre marked at a and two endpoints marked at a − R and a + R. The interval between them is shaded and labeled "converges". The regions outside are labeled "diverges". Vertical double-headed arrows from the centre to each endpoint are both labeled R. Each endpoint carries a question-mark bubble reading "test separately — the ratio test gives L = 1 here". A small inset below shows the specific case of Σ(x−2)ⁿ/(n3ⁿ) with the interval drawn from −1 to 5, the left endpoint drawn as a filled bracket labeled "converges (alternating)" and the right as an open bracket labeled "diverges (harmonic)".](../figures/FIG-01-22-003-interval-of-convergence.png)

### Worked Example 6 — Radius and Interval of Convergence

**Given.** $\displaystyle\sum_{n=1}^{\infty}\frac{(x-2)^n}{n\,3^n}$

**Find.** The radius and interval of convergence.

**Solution.**

**Ratio test.**

$$\left\lvert\frac{a_{n+1}}{a_n}\right\rvert = \left\lvert\frac{(x-2)^{n+1}}{(n+1)3^{n+1}}\cdot\frac{n\,3^n}{(x-2)^n}\right\rvert = \frac{\lvert x-2\rvert}{3}\cdot\frac{n}{n+1}$$

$$L = \lim_{n\to\infty}\frac{\lvert x-2\rvert}{3}\cdot\frac{n}{n+1} = \frac{\lvert x-2\rvert}{3}$$

Require $L < 1$:

$$\lvert x-2\rvert < 3 \implies \boxed{R = 3} \implies -1 < x < 5$$

**Endpoints, tested separately.**

At $x = 5$: the terms become $\frac{3^n}{n\,3^n} = \frac{1}{n}$, the harmonic
series — **diverges**.

At $x = -1$: the terms become $\frac{(-3)^n}{n\,3^n} = \frac{(-1)^n}{n}$, the
alternating harmonic series — **converges**.

$$\boxed{\text{interval of convergence} = [-1, 5)}$$

Note how differently the two endpoints behaved despite being symmetric about the
centre. That asymmetry is entirely normal, and it is why they must be checked one
at a time.

---

## 22.4 Taylor and Maclaurin Series

Now the construction that justifies the chapter.

Suppose we want a polynomial that matches $f$ as closely as possible near a point
$a$. A natural demand: make the polynomial's value, slope, curvature, and every
higher derivative agree with $f$'s at $a$. Working out which coefficients do that
gives the **Taylor series**:

$$\boxed{f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n}$$

Written out:

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$$

When the centre is $a = 0$ it is called a **Maclaurin series**:

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots$$

### Recognizing what you already know

Look at the first two terms:

$$P_1(x) = f(a) + f'(a)(x-a)$$

That is the linear approximation from Chapter 01-18, verbatim. The Taylor series
is that approximation continued — each additional term corrects the previous
polynomial using one more derivative. The degree-1 case uses the slope; the
degree-2 case adds the curvature, which is the $f''$ from Chapter 01-18's
concavity work; and so on.

So you have been using the first term of a Taylor series since Chapter 01-18.
This chapter supplies the rest of them and, crucially, the error bound.

![FIG-01-22-004: Plot of y = sin x over −π ≤ x ≤ π drawn as a heavy solid curve. Superimposed are three lighter curves: P₁ = x (a straight line, tracking the sine only very near the origin before diverging upward), P₃ = x − x³/6 (matching well out to roughly ±1.5 before falling away), and P₅ = x − x³/6 + x⁵/120 (nearly indistinguishable from the sine across most of the interval). Each polynomial is labeled at the point where it visibly departs from the sine. A shaded vertical band around the origin is labeled "all approximations good here"; arrows at both edges are labeled "each added term extends the useful range".](../figures/FIG-01-22-004-taylor-polynomials-sine.png)

### Worked Example 7 — Deriving the Series for $e^x$

**Given.** $f(x) = e^x$, centred at $a = 0$.

**Derive** the Maclaurin series.

**Solution.**

Every derivative of $e^x$ is $e^x$, and $e^0 = 1$, so

$$f^{(n)}(0) = 1 \quad \text{for all } n$$

$$e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!} = \boxed{1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots}$$

**Radius of convergence.** From Worked Example 5(b) the ratio is
$\frac{\lvert x\rvert}{n+1} \to 0$ for **every** $x$, so $R = \infty$. The series
converges for all real $x$.

**Check at $x = 1$.** The series gives
$1 + 1 + 0.5 + 0.16667 + 0.04167 + 0.00833 + 0.00139 + 0.00020 = 2.71826$,
against $e = 2.71828$ ✓ Eight terms, five correct decimals.

### Worked Example 8 — Deriving the Series for $\sin x$

**Given.** $f(x) = \sin x$, centred at $a = 0$.

**Solution.**

Cycle the derivatives, using Chapter 01-17:

| $n$ | $f^{(n)}(x)$ | $f^{(n)}(0)$ |
|---|---|---|
| 0 | $\sin x$ | $0$ |
| 1 | $\cos x$ | $1$ |
| 2 | $-\sin x$ | $0$ |
| 3 | $-\cos x$ | $-1$ |
| 4 | $\sin x$ | $0$ |

The pattern repeats with period 4. Every even derivative vanishes at zero, so only
odd powers survive:

$$\boxed{\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots}$$

**Structural checks.** Sine is an odd function, and the series contains only odd
powers ✓ Consistent with the symmetry classification from Chapter 01-06.
Differentiating the series term by term gives
$1 - \frac{3x^2}{6} + \frac{5x^4}{120} - \cdots = 1 - \frac{x^2}{2!} +
\frac{x^4}{4!} - \cdots$, which is the cosine series ✓ as it must be.

### The standard expansions

Memorize these six. They are the working content of the chapter.

| Function | Series | Valid for |
|---|---|---|
| $e^x$ | $\displaystyle 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$ | all $x$ |
| $\sin x$ | $\displaystyle x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$ | all $x$ |
| $\cos x$ | $\displaystyle 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$ | all $x$ |
| $\ln(1+x)$ | $\displaystyle x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$ | $-1 < x \le 1$ |
| $\dfrac{1}{1-x}$ | $\displaystyle 1 + x + x^2 + x^3 + \cdots$ | $\lvert x\rvert < 1$ |
| $(1+x)^n$ | $\displaystyle 1 + nx + \frac{n(n-1)}{2!}x^2 + \cdots$ | $\lvert x\rvert < 1$ |

Three observations worth carrying:

The $\frac{1}{1-x}$ entry is just the geometric series from §22.1 with $r = x$ —
nothing new, viewed as a power series.

The $(1+x)^n$ entry is the **binomial series**. For a positive integer $n$ it
terminates and reproduces the binomial theorem from Chapter 01-15. For fractional
or negative $n$ it runs forever, which is how you expand things like
$\sqrt{1+x} = (1+x)^{1/2}$.

The $\ln(1+x)$ entry is the narrowest. Its radius is only 1, and it fails
completely at $x = -1$ where the logarithm blows up. Series inherit their
function's trouble spots.

> ---
> **Mentor's Margin**
>
> You do not derive these on an exam. You recognize them.
>
> The derivations above exist so the expansions are not arbitrary strings of
> symbols, and having done them once you will remember the structure rather than
> the characters: sine is odd powers with alternating signs over odd factorials,
> cosine is even powers the same way, the exponential is every power with no sign
> alternation. Three facts, not thirty symbols.
>
> Here is a shortcut worth having, because building new series from old ones is
> far faster than differentiating from scratch. **You may substitute into, add,
> multiply, differentiate, and integrate a known series.** Need $e^{-x^2}$? Put
> $-x^2$ wherever $x$ appears in the exponential series. Need
> $\int e^{-x^2}dx$, which Chapter 01-21 told you has no elementary
> antiderivative? Integrate the series term by term and you have a perfectly
> usable answer as a series. That is how the normal distribution tables in Chapter
> 01-40 were computed.
>
> ---

### Worked Example 9 — Building New Series from Old

**(a)** Find the Maclaurin series for $e^{-2x}$.

Substitute $-2x$ into the exponential series:

$$e^{-2x} = 1 + (-2x) + \frac{(-2x)^2}{2!} + \frac{(-2x)^3}{3!} + \cdots$$

$$= \boxed{1 - 2x + 2x^2 - \frac{4x^3}{3} + \cdots}$$

**(b)** Find the first three nonzero terms for $x\cos x$.

Multiply the cosine series by $x$:

$$x\cos x = x\left(1 - \frac{x^2}{2} + \frac{x^4}{24} - \cdots\right) = \boxed{x - \frac{x^3}{2} + \frac{x^5}{24} - \cdots}$$

**(c)** Find $\sqrt{1.04}$ using the binomial series.

Write $\sqrt{1.04} = (1+0.04)^{1/2}$ and apply the binomial series with
$n = \frac{1}{2}$, $x = 0.04$:

$$\approx 1 + \frac{1}{2}(0.04) + \frac{(0.5)(-0.5)}{2}(0.04)^2 = 1 + 0.02 - 0.0002$$

$$= \boxed{1.01980}$$

**Check.** $\sqrt{1.04} = 1.0198039$ ✓ Two correction terms, six correct digits.

---

## 22.5 Truncation Error

You will always cut the series off. The question is how much that costs.

Write $P_n(x)$ for the Taylor polynomial of degree $n$ and

$$E_n(x) = f(x) - P_n(x)$$

for the **truncation error**. Two ways to bound it.

### The Lagrange remainder

> $$\boxed{E_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1} \qquad \text{for some } c \text{ between } a \text{ and } x}$$

You do not know $c$, and that is fine — you bound $f^{(n+1)}$ over the interval
and get a guaranteed worst case. This works for any Taylor series.

Read the structure: the error carries the factor $(x-a)^{n+1}$, so it shrinks fast
as you approach the centre and grows fast as you leave it. Doubling the distance
from the centre multiplies a degree-1 error by roughly four. That is why
linearizations are local.

### The alternating series bound

For an alternating series, §22.2 already gave the cheap version: the error is no
larger than the **first omitted term**. Since sine, cosine, and $\ln(1+x)$ all
have alternating series, this covers most practical cases in one line.

> ---
> **Mentor's Margin**
>
> One thing to be careful about: the "first omitted term" bound requires
> **alternating** signs. It is not a general rule.
>
> For a series of all-positive terms it fails, and it fails in the dangerous
> direction — it *understates* the error, because every omitted term adds to the
> shortfall rather than partially cancelling the last one. Worked Example 10 shows
> this concretely with $e^{0.5}$, where the first omitted term is 0.0026 and the
> actual error is 0.0029.
>
> So: alternating series, use the first omitted term. Positive series, use the
> Lagrange remainder. Mixing them up produces an error bound that is smaller than
> the error, which is worse than having no bound at all.
>
> ---

### Worked Example 10 — Both Error Bounds

**(a)** Estimate $e^{0.5}$ with four terms and bound the error.

$$P_3(0.5) = 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} = 1 + 0.5 + 0.125 + 0.0208333$$

$$= 1.6458333$$

**Lagrange bound.** With $f^{(4)}(c) = e^c$ and $0 < c < 0.5$, the largest
possible value is $e^{0.5} = 1.6487$:

$$\lvert E_3\rvert \le \frac{1.6487}{4!}(0.5)^4 = \frac{1.6487(0.0625)}{24} = 0.00429$$

**Actual error.** $e^{0.5} = 1.6487213$, so the error is
$1.6487213 - 1.6458333 = 0.00289$.

$$0.00289 \le 0.00429 \;\checkmark$$

The bound holds and is not wildly loose.

**Note the failure of the other rule.** The first omitted term is
$\frac{(0.5)^4}{4!} = 0.00260$, which is **less** than the actual error
0.00289. The series has all positive terms, so the omitted tail accumulates and
the first-term rule does not apply ✓ — exactly as warned.

**(b)** Estimate $\ln(1.1)$ to within $10^{-5}$.

The series $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ with $x = 0.1$
is alternating, so the first omitted term bounds the error.

| Terms kept | Value | First omitted term |
|---|---|---|
| 1 | $0.1$ | $0.005$ |
| 2 | $0.095$ | $0.000333$ |
| 3 | $0.0953333$ | $0.000025$ |
| 4 | $0.0953083$ | $0.000002$ |

Four terms give an error bound of $2\times10^{-6} < 10^{-5}$ ✓

$$\boxed{\ln(1.1) \approx 0.0953083}$$

**Check.** The true value is $0.0953102$, so the actual error is
$1.9\times10^{-6}$, inside the bound ✓ And notice the partial sums straddle the
answer — $0.1$ high, $0.095$ low, $0.09533$ high, $0.09531$ low — which is the
alternating behaviour that makes the bound work.

---

## 22.6 Small-Angle Approximations

The most-used consequence of this chapter, and the one that hides inside other
subjects.

Truncate the trigonometric series after one or two terms:

$$\boxed{\sin\theta \approx \theta \qquad \cos\theta \approx 1 - \frac{\theta^2}{2} \qquad \tan\theta \approx \theta \qquad (\theta \text{ in radians})}$$

A cruder version, $\cos\theta \approx 1$, is sometimes used, and it is worth
knowing which one a derivation assumed.

### How good are they?

Using the alternating series bound, the error in $\sin\theta \approx \theta$ is at
most $\frac{\theta^3}{6}$, so the **relative** error is at most
$\frac{\theta^2}{6}$.

| $\theta$ | radians | $\sin\theta$ | $\theta$ | relative error |
|---|---|---|---|---|
| $5°$ | $0.08727$ | $0.08716$ | $0.08727$ | $0.13\%$ |
| $10°$ | $0.17453$ | $0.17365$ | $0.17453$ | $0.51\%$ |
| $15°$ | $0.26180$ | $0.25882$ | $0.26180$ | $1.15\%$ |
| $30°$ | $0.52360$ | $0.50000$ | $0.52360$ | $4.72\%$ |

**Check the bound against the table.** At $10°$: $\frac{\theta^2}{6} =
\frac{0.030462}{6} = 0.0051 = 0.51\%$ ✓ — the estimate and the actual agree to
two figures, because the next term is tiny.

So the working rule: **$\sin\theta \approx \theta$ is good to about 1% out to
15°, and to about 0.1% out to 5°.** Beyond 15° it degrades quickly, because the
error grows as $\theta^2$.

Adding the cubic term buys a great deal. At $10°$:

$$\theta - \frac{\theta^3}{6} = 0.17453 - 0.00089 = 0.17365$$

against a true value of $0.17365$ — a relative error near $0.0009\%$, roughly 600
times better for one extra term.

![FIG-01-22-005: Semi-log plot with angle in degrees on the horizontal axis from 0 to 40 and relative error on a logarithmic vertical axis from 0.0001% to 10%. Three rising curves are plotted and labeled: "sinθ ≈ θ" rising through 0.13% at 5°, 0.51% at 10°, and 1.15% at 15°; "sinθ ≈ θ − θ³/6" rising far below it; and "cosθ ≈ 1 − θ²/2" also low. A horizontal dashed reference line at 1% is labeled "typical engineering tolerance", with a vertical dropline where the one-term sine curve crosses it, annotated "≈ 14°". A shaded band from 0 to 15° is labeled "small-angle region".](../figures/FIG-01-22-005-small-angle-error.png)

### Worked Example 11 — The Pendulum Linearization

**Given.** A simple pendulum of length $L$ obeys

$$\frac{d^2\theta}{dt^2} + \frac{g}{L}\sin\theta = 0$$

**(a)** Linearize the equation for small $\theta$ and state what it becomes.
**(b)** For $L = 1.20$ m, find the small-angle period.
**(c)** The exact solution gives the period as
$T = T_0\left(1 + \frac{\theta_0^2}{16} + \cdots\right)$, where $\theta_0$ is the
amplitude in radians. Quoting that standard result, estimate the error in the
linear period at amplitudes of $5°$ and $30°$.

**Solution.**

**(a)** Replace $\sin\theta$ by its first Taylor term:

$$\boxed{\frac{d^2\theta}{dt^2} + \frac{g}{L}\theta = 0}$$

The original equation is nonlinear and has no elementary closed-form solution.
The linearized version is the standard linear oscillator, whose solution is a
sinusoid with

$$T_0 = 2\pi\sqrt{\frac{L}{g}}$$

That replacement is the entire reason introductory pendulum theory works, and it
is a single truncated Taylor series.

**(b)**

$$T_0 = 2\pi\sqrt{\frac{1.20}{9.81}} = 2\pi\sqrt{0.122324} = 2\pi(0.349748) = \boxed{2.197 \text{ s}}$$

**(c)** At $\theta_0 = 5° = 0.087266$ rad:

$$\frac{\theta_0^2}{16} = \frac{0.0076154}{16} = 0.000476 = 0.048\%$$

At $\theta_0 = 30° = 0.523599$ rad:

$$\frac{\theta_0^2}{16} = \frac{0.274156}{16} = 0.01713 = 1.71\%$$

$$\boxed{5°: \text{ period underestimated by } 0.05\%; \quad 30°: \text{ by } 1.7\%}$$

**Interpretation.** At small amplitude the linear period is excellent — 0.05% is
below what you could measure with a stopwatch. At $30°$ the linearization
understates the period by 1.7%, or about 38 ms per swing, which accumulates to
roughly a minute of error per day in a pendulum clock. Whether that matters
depends entirely on the application, and the point of this chapter is that you can
*compute* whether it matters rather than guessing.

### Worked Example 12 — Binomial Approximation and the Error Rule

**Given.** The sphere from Chapter 01-18, with $V = \frac{4}{3}\pi r^3$ and radius
measured to $\pm 1.2\%$.

**Show** that the binomial series reproduces the power-law error rule
$\frac{dV}{V} = n\frac{dr}{r}$, and compare the linear estimate to the exact
figure.

**Solution.**

Perturb the radius by a fractional amount $\varepsilon$, so $r \to r(1+\varepsilon)$:

$$V \to \frac{4}{3}\pi r^3(1+\varepsilon)^3 = V(1+\varepsilon)^3$$

Expand by the binomial series with $n = 3$:

$$(1+\varepsilon)^3 = 1 + 3\varepsilon + 3\varepsilon^2 + \varepsilon^3$$

For small $\varepsilon$ the quadratic and cubic terms are negligible:

$$\frac{\Delta V}{V} \approx 3\varepsilon = n\,\frac{\Delta r}{r}$$

which is exactly the rule from Chapter 01-18 ✓ The differential method there and
the series method here are the same first-order truncation.

**Numerically**, with $\varepsilon = 0.012$:

Linear estimate: $3(0.012) = 0.0360 = 3.60\%$

Exact: $(1.012)^3 = 1.036434$, so $3.6434\%$

$$\boxed{\text{linear } 3.60\% \text{ versus exact } 3.64\%}$$

The linear estimate is low by 0.04 percentage points — about 1.2% of the error
itself. And the series tells you exactly where that discrepancy came from: the
neglected $3\varepsilon^2 = 3(0.000144) = 0.000432 = 0.043\%$ term ✓ accounting
for essentially all of it.

**Why this matters.** Chapter 01-18 gave you the differential rule and said it
was valid for small changes. This chapter shows you *what* was dropped and lets
you estimate the cost. For $\varepsilon$ of a few percent the linear rule is
excellent. For $\varepsilon = 0.3$ it would be off by 27% of the answer, and you
would need the quadratic term.

---

## 22.7 Engineering Application: When Is Constant-Rate Filling Valid?

### Worked Example 13 — Linearizing the Tank

**Given.** The tank from Chapters 01-16, 01-17, and 01-19, with

$$h(t) = 4.5\left(1 - e^{-t/6.0}\right) \text{ m}$$

**(a)** Expand $h(t)$ as a Maclaurin series in $t$ through the cubic term.
**(b)** Identify the linear coefficient and check it against Chapter 01-17.
**(c)** Determine how long the constant-rate assumption $h \approx 0.75t$ stays
within 1%.
**(d)** Evaluate the two- and three-term approximations at $t = 1.0$ min.

**Solution.**

**(a)** Let $u = \frac{t}{6.0}$. From the exponential series,

$$e^{-u} = 1 - u + \frac{u^2}{2} - \frac{u^3}{6} + \cdots$$

$$1 - e^{-u} = u - \frac{u^2}{2} + \frac{u^3}{6} - \cdots$$

Substitute $u = \frac{t}{6}$ and multiply by 4.5:

$$h(t) = 4.5\left[\frac{t}{6} - \frac{t^2}{72} + \frac{t^3}{1296} - \cdots\right]$$

$$\boxed{h(t) = 0.750t - 0.0625t^2 + 0.003472t^3 - \cdots}$$

**(b)** The linear coefficient is 0.750 m/min. Chapter 01-17 computed the initial
fill rate as $\frac{dh}{dt}\big|_{t=0} = 0.75$ m/min ✓

That agreement is not a coincidence — it is the definition of the Taylor series.
The coefficient of $t$ **is** $f'(0)$. Every series expansion carries the
derivative information you have already computed, which makes this a free check on
any expansion you produce.

**(c)** The relative error of the one-term approximation is governed by the ratio
of the second term to the first:

$$\text{relative error} \approx \frac{0.0625t^2}{0.750t} = 0.0833t$$

Set this to 0.01:

$$t \approx \frac{0.01}{0.0833} = \boxed{0.12 \text{ min} = 7.2 \text{ s}}$$

**Interpretation, and a generalization.** Constant-rate filling is good to 1% for
only the first seven seconds of a six-minute process. In terms of the time
constant $\tau = 6.0$ min, that is $t \approx 0.02\tau$ — and the general result
behind it is worth extracting:

$$\text{relative error of } 1-e^{-t/\tau} \approx t \approx \frac{t}{2\tau}$$

So a linear approximation to any exponential approach is good to 1% out to about
$0.02\tau$, and to 10% out to about $0.2\tau$. That rule of thumb applies to
capacitor charging, thermal soak, first-order sensor response, and reactor
start-up transients alike.

**(d)** At $t = 1.0$ min the true value is

$$h = 4.5\left(1 - e^{-1/6}\right) = 4.5(1 - 0.846482) = 4.5(0.153518) = 0.690831 \text{ m}$$

| Approximation | Value (m) | Error | Relative |
|---|---|---|---|
| $0.750t$ | $0.750000$ | $+0.05917$ | $8.6\%$ |
| $0.750t - 0.0625t^2$ | $0.687500$ | $-0.00333$ | $0.48\%$ |
| three terms | $0.690972$ | $+0.00014$ | $0.021\%$ |

Each added term cuts the error by more than an order of magnitude, and the errors
alternate in sign — consistent with an alternating series ✓ The 8.6% figure for
the linear term also confirms part (c): at $t = 1.0$ min, the estimate
$0.0833t = 8.3\%$ ✓

![FIG-01-22-006: Plot of h against t from 0 to 3 min. A heavy solid curve shows the exact h = 4.5(1 − e^(−t/6)), rising and beginning to flatten. A straight dashed line through the origin with slope 0.75 is labeled "one term — constant rate", visibly above the curve and diverging. A dashed parabola is labeled "two terms" and tracks the curve closely to about t = 1.5 before bending below it. A narrow shaded vertical strip at the far left, from t = 0 to t = 0.12 min, is labeled "linear within 1% — only 7 s". Vertical error bars at t = 1.0 mark the 8.6% and 0.48% discrepancies.](../figures/FIG-01-22-006-tank-linearization.png)

> ---
> **Mentor's Margin**
>
> That example is the honest version of a habit engineers acquire and rarely
> examine.
>
> "Assume constant rate." "Assume small angles." "Assume the response is linear
> near the operating point." Every one of those phrases is a truncated Taylor
> series, and every one comes with an error that grows as a known power of the
> departure from the centre.
>
> Most of the time the assumption is fine and nobody needs to check. The value of
> this chapter is that when somebody *does* ask — in a design review, in a
> failure investigation, in a report you have to sign — you can produce a number
> instead of a shrug. "Linear to within 1% for the first seven seconds" is an
> engineering statement. "It should be roughly linear at the start" is not.
>
> ---

> **Preview note.** Two places these expansions return. Substituting $j\theta$
> into the exponential series and sorting real from imaginary terms produces
> **Euler's formula**, $e^{j\theta} = \cos\theta + j\sin\theta$, which is the
> foundation of phasor analysis in Chapter 02-63 and of the solution method for
> oscillatory differential equations in Chapter 01-25. And term-by-term
> integration of $e^{-x^2}$ is how the normal distribution tables of Chapter
> 01-40 were generated, since Chapter 01-21 established that no elementary
> antiderivative exists. Nothing in the present chapter depends on either.

---

## As the Handbook States It

> **Handbook 10.6, Mathematics section (begins p. 36)** — series material appears
> in two places. *Progressions and Series*, near the algebra material around
> pp. 38–39, and *Taylor's Series*, with the calculus material around pp. 45–46.

Coverage here is **thin relative to the topic's importance**, and that asymmetry
should shape your preparation.

**What you will find:**

- **Taylor's series**, stated in general form with the remainder
- Arithmetic and geometric progression formulas, including the infinite geometric
  sum $\frac{a}{1-r}$
- The binomial theorem, for integer exponents
- Some tests for series convergence, stated briefly
- Selected identities and sums from Chapter 01-15

**What's not in the Handbook — memorize:**

- **The six standard expansions** in §22.4. The Handbook gives you the general
  Taylor formula but may not print the individual series for $e^x$, $\sin x$,
  $\cos x$, or $\ln(1+x)$. Deriving one under time pressure is a poor use of four
  minutes.
- **The small-angle approximations** and the angle range over which each holds.
  These are used constantly and rarely stated.
- The $n$th term test, and that it cannot prove convergence
- The $p$-series result, including that $p = 1$ diverges
- The integral test, and that it gives convergence but **not** the sum
- The ratio test, and that $L = 1$ is inconclusive
- The alternating series test and the first-omitted-term error bound
- That the first-omitted-term bound requires alternation and fails for positive
  series
- How to find a radius of convergence, and that endpoints need separate testing
- That the degree-1 Taylor polynomial **is** the linear approximation from
  Chapter 01-18
- That you may substitute into, differentiate, and integrate a known series to
  build a new one
- That all series arguments are in **radians**

> ---
> **Mentor's Margin**
>
> Exam strategy, stated plainly.
>
> Series questions on the FE come in two flavours. A small number ask directly
> for a convergence determination or a radius of convergence, and those are
> straightforward if you know the tests. A much larger number use a series result
> *inside* a problem about something else — a small-angle assumption in a
> statics problem, a linearized response in a controls or circuits problem, an
> $e^x \approx 1+x$ in a thermodynamics estimate.
>
> The second category is where the marks are, and it does not announce itself.
> That is why the six expansions and the small-angle rules belong in memory rather
> than in a lookup: you need them at the moment you recognize that a problem has
> handed you a small parameter, and that recognition happens while you are
> thinking about something else entirely.
>
> ---

---

## Where This Goes Wrong

**Concluding convergence because the terms go to zero.** The $n$th term test only
proves divergence. The harmonic series is the standing counterexample.

**Treating $L = 1$ in the ratio test as a result.** It means the test failed. Use
a different test.

**Using degrees in a series.** Every trigonometric expansion in this chapter
requires radians. Degrees give answers wrong by a factor of about 57 on the first
term alone.

**Applying the first-omitted-term error bound to a positive series.** It requires
alternation. On a positive series it understates the error, which is the dangerous
direction.

**Confusing the integral test's integral with the series' sum.** They determine
the same convergence and have different values.
$\sum\frac{1}{n^2} = 1.645$ while $\int_1^{\infty}x^{-2}dx = 1$.

**Forgetting to test the endpoints of an interval of convergence.** The ratio
test gives $L = 1$ there and decides nothing. The two endpoints frequently behave
differently.

**Comparing in the wrong direction.** Smaller than a convergent series proves
convergence; smaller than a divergent one proves nothing.

**Omitting the factorials in a Taylor series.** The coefficient is
$\frac{f^{(n)}(a)}{n!}$, not $f^{(n)}(a)$. Dropping the factorial makes the
series diverge for essentially any $x$.

**Expanding about the wrong centre.** A Maclaurin series is centred at zero and is
a poor approximation far from zero. If the operating point is $x = 5$, expand
about 5, not 0.

**Using a linearization outside its range of validity.** The error grows as
$(x-a)^2$ for a first-degree approximation. Twice as far from the centre is four
times the error.

**Assuming a truncated series inherits the function's behaviour globally.** A
polynomial always runs off to $\pm\infty$; $\sin x$ never leaves $[-1,1]$. Any
Taylor polynomial for sine is badly wrong far from its centre, no matter how many
terms you keep.

**Forgetting the validity interval on $\ln(1+x)$ and $\frac{1}{1-x}$.** Both have
radius 1. Substituting $x = 2$ into either series produces a divergent sum, not an
approximation.

**Assuming every function has a useful Taylor series.** The expansion requires the
derivatives to exist at the centre. A function with a corner or a vertical
tangent there — the $\lvert x\rvert$ and $x^{1/3}$ cases from Chapter 01-17 — has
no Maclaurin series at all.

---

## Key Terms

| Term | Definition |
|---|---|
| Series | The sum of the terms of a sequence |
| Partial sum $S_n$ | The sum of the first $n$ terms; a finite number |
| Converges | The partial sums approach a finite limit |
| Diverges | The partial sums do not approach a finite limit |
| $n$th term test | If $a_n \not\to 0$ the series diverges; proves nothing otherwise |
| Geometric series | $\sum ar^n$; converges to $\frac{a}{1-r}$ when $\lvert r\rvert<1$ |
| Harmonic series | $\sum\frac{1}{n}$; the $p=1$ case, divergent |
| $p$-series | $\sum n^{-p}$; converges iff $p>1$ |
| Integral test | Compares a positive decreasing series with the corresponding improper integral |
| Comparison test | Establishes convergence by bounding against a known series |
| Ratio test | Convergence from $L = \lim\lvert a_{n+1}/a_n\rvert$; inconclusive at $L=1$ |
| Alternating series | A series whose terms alternate in sign |
| Absolutely convergent | $\sum\lvert a_n\rvert$ converges |
| Conditionally convergent | Converges, but not absolutely |
| Power series | $\sum c_n(x-a)^n$ |
| Radius of convergence $R$ | Distance from the centre within which the power series converges |
| Interval of convergence | The full set of $x$ for which it converges, endpoints determined separately |
| Taylor series | $\sum\frac{f^{(n)}(a)}{n!}(x-a)^n$ |
| Maclaurin series | A Taylor series centred at $a = 0$ |
| Taylor polynomial $P_n$ | The series truncated at degree $n$ |
| Truncation error $E_n$ | $f(x) - P_n(x)$ |
| Lagrange remainder | $\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ for some interior $c$ |
| Binomial series | The expansion of $(1+x)^n$ for any real $n$ |
| Small-angle approximation | $\sin\theta\approx\theta$, $\cos\theta\approx1-\frac{\theta^2}{2}$, radians only |
| Linearization | Replacing a function by its degree-1 Taylor polynomial about an operating point |

---

## Review Questions

### Conceptual

1. Define convergence of an infinite series in terms of partial sums. Why does
   the definition never require performing infinitely many additions?
2. Explain why the $n$th term test can prove divergence but never convergence,
   and give the standard counterexample.
3. State the $p$-series result. Why is the $p = 1$ case worth remembering
   separately?
4. The integral test tells you a series converges. Why does it not tell you the
   sum?
5. The ratio test returns $L = 1$ for every $p$-series. What does that tell you
   about the limits of a single convergence test?
6. Explain the difference between absolute and conditional convergence, and give
   an example of each.
7. Why must the endpoints of an interval of convergence be tested separately?
8. Show that the degree-1 Taylor polynomial is identical to the linear
   approximation of Chapter 01-18. What does the degree-2 term add?
9. Why does the truncation error of a first-degree Taylor polynomial grow as the
   square of the distance from the centre?
10. Explain why the first-omitted-term error bound requires an alternating series,
    and what goes wrong if you apply it to a positive series.
11. Why is $\sin\theta \approx \theta$ false if $\theta$ is in degrees?
12. A colleague writes "assume small angles" in a calculation without further
    comment. What two questions should you ask?

### Calculation

13. Determine whether each series converges, and name the test used:
    (a) $\displaystyle\sum_{n=1}^{\infty}\frac{2n}{3n+5}$
    (b) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{3/2}}$
    (c) $\displaystyle\sum_{n=1}^{\infty}\frac{n^2}{2^n}$
    (d) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+3n}$
    (e) $\displaystyle\sum_{n=1}^{\infty}\frac{3^n}{n!}$
    (f) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{\sqrt{n}}$

14. Evaluate each convergent geometric series:
    (a) $\displaystyle\sum_{n=0}^{\infty}\left(\frac{2}{5}\right)^n$
    (b) $\displaystyle\sum_{n=1}^{\infty}\frac{4}{2^n}$
    (c) $\displaystyle\sum_{n=0}^{\infty}3(-0.4)^n$

15. Find the radius and interval of convergence:
    (a) $\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{2^n}$
    (b) $\displaystyle\sum_{n=1}^{\infty}\frac{(x+3)^n}{n}$
    (c) $\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!}$

16. Write the first four nonzero terms of the Maclaurin series for:
    (a) $e^{3x}$
    (b) $\sin 2x$
    (c) $\cos\left(x^2\right)$
    (d) $\ln(1-x)$
    (e) $\frac{1}{1+x}$

17. Find the Taylor series for $f(x) = \sqrt{x}$ centred at $a = 4$, through the
    quadratic term. Use it to estimate $\sqrt{4.3}$ and compare with the exact
    value.

18. Estimate $\cos(0.2)$ using three terms and bound the truncation error two
    ways — by the first omitted term and by the Lagrange remainder. Compare both
    bounds with the actual error.

19. Determine the largest angle, in degrees, for which $\tan\theta \approx \theta$
    is accurate to within 2%.

20. **Engineering application.** A first-order thermal system has
    $T(t) = T_\infty\left(1 - e^{-t/\tau}\right)$ with $T_\infty = 80.0$ °C and
    $\tau = 45$ s.
    (a) Expand $T(t)$ through the quadratic term.
    (b) Identify the initial heating rate from the linear coefficient and confirm
    it by differentiating $T(t)$ directly.
    (c) Determine how long the constant-rate approximation stays within 2%.
    (d) Evaluate the exact and two-term values at $t = 10$ s.

21. **Engineering application.** A cable of length $L$ is stretched nearly
    straight between supports a distance $s$ apart, with sag such that
    $L = s\sqrt{1+k^2}$ where $k$ is a small dimensionless sag parameter.
    (a) Use the binomial series to show that $L \approx s\left(1 +
    \frac{k^2}{2}\right)$.
    (b) For $k = 0.08$, compare the approximate and exact elongation ratios
    $\frac{L-s}{s}$.
    (c) Estimate the value of $k$ at which the approximation errs by 1% of the
    elongation.

22. **Engineering application.** A resistance temperature detector has
    $R(T) = R_0\left(1 + \alpha T + \beta T^2\right)$ with
    $R_0 = 100.0\ \Omega$, $\alpha = 3.90\times10^{-3}$ /°C, and
    $\beta = -5.80\times10^{-7}$ /°C².
    (a) The instrument's linear calibration ignores the $\beta$ term. Express the
    resulting relative error in $R$ as a function of $T$.
    (b) Find the temperature at which the linear calibration errs by 0.1%.
    (c) Comment on whether a linear calibration is defensible over 0 °C to
    200 °C.

### Multiple Choice

23. The series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{0.9}}$:
    A) converges, because the terms approach zero
    B) converges by the ratio test
    C) diverges, because $p \le 1$
    D) converges to $\frac{1}{0.9 - 1}$

24. The Maclaurin series for $\cos x$ begins:
    A) $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$
    B) $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$
    C) $1 + x + \frac{x^2}{2!} + \cdots$
    D) $1 - x + \frac{x^2}{2} - \cdots$

25. For $\theta = 12°$, the relative error in $\sin\theta \approx \theta$ is
    closest to:
    A) $0.07\%$
    B) $0.7\%$
    C) $7\%$
    D) $12\%$

26. The radius of convergence of $\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{4^n}$
    is:
    A) $\frac{1}{4}$
    B) $1$
    C) $4$
    D) infinite

27. The ratio test applied to $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^3}$
    gives $L = 1$. This means:
    A) the series diverges
    B) the series converges
    C) the test is inconclusive and another test is needed
    D) the series converges conditionally

28. Truncating an alternating series after five terms leaves an error that is:
    A) equal to the fifth term
    B) no larger than the sixth term
    C) no larger than the sum of all omitted terms, which cannot be bounded
    D) equal to the Lagrange remainder with $c = 0$

29. A second-order Taylor polynomial about $x = a$ has a truncation error that
    grows, as $x$ moves away from $a$, like:
    A) $(x-a)$
    B) $(x-a)^2$
    C) $(x-a)^3$
    D) $e^{x-a}$

30. Which expansion is valid only for $\lvert x\rvert < 1$?
    A) $e^x$
    B) $\sin x$
    C) $\cos x$
    D) $\frac{1}{1-x}$
**Omitting the factorials in a Taylor series.** The coefficient is
$\frac{f^{(n)}(a)}{n!}$, not $f^{(n)}(a)$. Without the factorials the series does
not converge to the function, and for the exponential it does not converge at all.

**Using $x^n$ when the centre is not zero.** A series about $a$ is built from
powers of $(x-a)$, not powers of $x$. Expanding $\ln x$ about $a=1$ gives
$(x-1) - \frac{(x-1)^2}{2} + \cdots$; writing $x - \frac{x^2}{2}$ instead produces
a series for a different function entirely.

**Assuming every Taylor series converges everywhere.** $e^x$, $\sin x$, and
$\cos x$ do. $\ln(1+x)$ has radius 1, $\frac{1}{1-x}$ has radius 1, and the
binomial series has radius 1. Outside the radius, adding terms makes the answer
**worse**, not better.

**Confusing radius with interval.** $R$ is a distance; the interval is the set of
$x$ values. A series with $R = 2$ centred at $x = 1$ converges on an interval of
total length 4.

**Dropping the $\frac{\theta^2}{2}$ term from cosine when it carries the whole
effect.** The cruder rule $\cos\theta\approx 1$ is sometimes right and sometimes
catastrophic. If the quantity you want is $1 - \cos\theta$, that approximation
returns exactly zero and destroys the answer. Check what the approximation is
being subtracted from.

**Assuming $\tan\theta \approx \theta$ is as accurate as
$\sin\theta \approx \theta$.** It is not. The tangent's relative error is
$\frac{\theta^2}{3}$ against the sine's $\frac{\theta^2}{6}$ — twice as large at
every angle. $\tan\theta\approx\theta$ holds to 1% only out to about $10°$.

**Applying an approximation outside the range where it was validated.** A
linearization good to 1% at $5°$ may be 20% wrong at $40°$. The error grows as a
power of the departure from the centre, so extrapolation degrades quickly rather
than gracefully.

---

## Key Terms

| Term | Definition |
|---|---|
| Sequence | An ordered list of numbers $a_1, a_2, a_3, \ldots$ |
| Series | The sum of a sequence's terms |
| Partial sum $S_n$ | The finite sum of the first $n$ terms |
| Converges | The partial sums approach a finite limit |
| Diverges | The partial sums do not approach a finite limit |
| $n$th term test | If $a_n \not\to 0$ the series diverges; proves divergence only |
| Geometric series | $\sum ar^n$; converges to $\frac{a}{1-r}$ when $\lvert r\rvert < 1$ |
| Harmonic series | $\sum\frac{1}{n}$; diverges despite terms going to zero |
| $p$-series | $\sum n^{-p}$; converges iff $p > 1$ |
| Integral test | Series and $\int f$ share convergence behaviour, not value |
| Comparison test | Squeezes a positive series against a known one |
| Ratio test | $L = \lim\lvert a_{n+1}/a_n\rvert$; $L<1$ converges, $L>1$ diverges, $L=1$ inconclusive |
| Alternating series | Terms alternate in sign |
| Absolute convergence | $\sum\lvert a_n\rvert$ converges; the stronger condition |
| Conditional convergence | $\sum a_n$ converges but $\sum\lvert a_n\rvert$ does not |
| Power series | $\sum c_n(x-a)^n$ |
| Radius of convergence $R$ | Distance from the centre within which the series converges |
| Interval of convergence | The set of $x$ where the series converges; endpoints tested separately |
| Taylor series | $\sum\frac{f^{(n)}(a)}{n!}(x-a)^n$ |
| Maclaurin series | A Taylor series centred at $a = 0$ |
| Centre | The point $a$ about which the expansion is built |
| Taylor polynomial $P_n$ | The series truncated after the degree-$n$ term |
| Truncation error $E_n$ | $f(x) - P_n(x)$ |
| Lagrange remainder | $\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ for some interior $c$ |
| Binomial series | Expansion of $(1+x)^n$; valid for non-integer $n$ with $\lvert x\rvert<1$ |
| Small-angle approximation | $\sin\theta\approx\theta$, $\cos\theta\approx1-\frac{\theta^2}{2}$, $\tan\theta\approx\theta$, radians |
| Linearization | Replacement of a function by its degree-1 Taylor polynomial about an operating point |

---

## Review Questions

### Conceptual

1. Define convergence of an infinite series in terms of partial sums, and explain
   why this definition never requires you to perform infinitely many additions.
2. Explain why the $n$th term test can prove divergence but never convergence.
   Give the standard counterexample.
3. The integral test tells you something and withholds something. State both, and
   illustrate with $\sum\frac{1}{n^2}$.
4. Why is $p = 1$ the boundary case for a $p$-series, and on which side of the
   boundary does it fall?
5. Show that every $p$-series gives $L = 1$ in the ratio test, and explain what
   that demonstrates about the test.
6. Distinguish absolute from conditional convergence, and give one example of
   each.
7. Why must the endpoints of an interval of convergence be tested separately
   rather than settled by the ratio test?
8. Explain the relationship between the degree-1 Taylor polynomial and the linear
   approximation from Chapter 01-18. Are they different results?
9. The Lagrange remainder carries a factor $(x-a)^{n+1}$. Explain what that factor
   implies about the range over which a truncated series is useful.
10. Why does the first-omitted-term error bound fail for a series of positive
    terms, and in which direction does it fail? Why is that direction the
    dangerous one?

### Calculation

11. Determine whether each series converges or diverges, and name the test used:
    (a) $\displaystyle\sum_{n=1}^{\infty}\frac{n}{2n+3}$
    (b) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{1.5}}$
    (c) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{3n-1}$
    (d) $\displaystyle\sum_{n=1}^{\infty}\frac{n^2}{n!}$
    (e) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{\sqrt{n}}$

12. Evaluate, or state that the series diverges:
    (a) $\displaystyle\sum_{n=0}^{\infty}(0.8)^n$
    (b) $\displaystyle\sum_{n=1}^{\infty}4(0.25)^n$
    (c) $\displaystyle\sum_{n=0}^{\infty}3(1.1)^n$

13. Find the radius and interval of convergence:
    (a) $\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!}$
    (b) $\displaystyle\sum_{n=1}^{\infty}\frac{(x-1)^n}{n\,2^n}$
    (c) $\displaystyle\sum_{n=1}^{\infty}n\,x^n$

14. Write the first four nonzero terms of the Maclaurin series:
    (a) $e^{3x}$
    (b) $\cos 2x$
    (c) $xe^x$
    (d) $\ln(1+2x)$

15. Find the Taylor series for $f(x) = \ln x$ about $a = 1$, through the cubic
    term. Verify it against the standard $\ln(1+x)$ expansion.

16. Estimate $\sqrt{1.06}$ using the binomial series with two correction terms,
    and compare with the true value.

17. Estimate $\cos(0.2)$ using three terms. Bound the error with the first
    omitted term and verify the bound holds.

18. Find the largest angle, in degrees, for which $\tan\theta \approx \theta$ is
    accurate to within 0.5%. Verify your answer numerically.

19. **Engineering application.** A capacitor charges according to
    $v(t) = 12\left(1 - e^{-t/0.050}\right)$ V, with $t$ in seconds.
    (a) Expand $v(t)$ as a Maclaurin series through the cubic term.
    (b) Identify the linear coefficient and confirm it against the initial
    derivative.
    (c) Determine how long the constant-rate approximation stays within 2%.
    (d) Evaluate the one-, two-, and three-term approximations at
    $t = 0.010$ s against the exact value.

20. **Engineering application.** A rigid link of length $L = 2.00$ m, initially
    horizontal, is rotated by an angle $\theta$ about one end. The horizontal
    distance between its endpoints shortens by $\Delta = L(1-\cos\theta)$.
    (a) Approximate $\Delta$ using the two-term cosine expansion.
    (b) Evaluate the approximation and the exact value at $\theta = 6.00°$.
    (c) Explain what happens if the cruder approximation $\cos\theta \approx 1$
    is used instead, and what general lesson that carries.

### Multiple Choice

21. The series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^3}$:
    A) diverges by the $n$th term test
    B) converges, since $p = 3 > 1$
    C) diverges, since $p > 1$
    D) convergence cannot be determined

22. In the ratio test, obtaining $L = 1$ means:
    A) the series converges
    B) the series diverges
    C) the test is inconclusive
    D) the series converges conditionally

23. The Maclaurin series for $\cos x$ begins:
    A) $x - \dfrac{x^3}{6} + \cdots$
    B) $1 - x + \dfrac{x^2}{2} - \cdots$
    C) $1 - \dfrac{x^2}{2} + \dfrac{x^4}{24} - \cdots$
    D) $1 + \dfrac{x^2}{2} + \dfrac{x^4}{24} + \cdots$

24. The series $1 + x + x^2 + x^3 + \cdots$ converges to $\dfrac{1}{1-x}$ for:
    A) all real $x$
    B) $\lvert x\rvert < 1$
    C) $x > 0$
    D) $-1 < x \le 1$

25. Using two terms of its Maclaurin series, $\sin(0.1)$ is approximately:
    A) $0.100000$
    B) $0.099833$
    C) $0.099500$
    D) $0.101667$

26. Which expansion has an **infinite** radius of convergence?
    A) $\ln(1+x)$
    B) $\dfrac{1}{1-x}$
    C) $(1+x)^{1/2}$
    D) $\sin x$

27. The bound "error $\le$ first omitted term" applies to:
    A) any convergent series
    B) any Taylor series
    C) convergent alternating series only
    D) series of positive terms only

28. The approximation $\sin\theta \approx \theta$ is accurate to within about 1%
    for angles up to roughly:
    A) $5°$
    B) $15°$
    C) $30°$
    D) $45°$

29. The degree-1 Taylor polynomial of $f$ about $x = a$ is:
    A) the secant line through $a$ and $b$
    B) the tangent line at $a$
    C) the average value of $f$ near $a$
    D) unrelated to the derivative

30. The harmonic series $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$:
    A) converges to 1
    B) converges to $\ln 2$
    C) diverges
    D) converges, since its terms approach zero

---

## Answers to Review Questions

### Conceptual

1. The series is defined as $\lim_{n\to\infty}S_n$, where each $S_n$ is an
   ordinary finite sum. The definition therefore asks a limit question about a
   sequence of finite numbers — Chapter 01-16 machinery — rather than requiring an
   infinite arithmetic operation.
2. If $a_n \not\to 0$, each addition moves the partial sum by a non-vanishing
   amount, so it cannot settle. But terms going to zero says nothing about *how
   fast*, and convergence depends on the rate. The harmonic series has
   $a_n \to 0$ and diverges.
3. It tells you **whether** the series converges. It does **not** give the sum.
   $\int_1^{\infty}x^{-2}dx = 1$ establishes convergence, while the sum is
   $\frac{\pi^2}{6} = 1.645$.
4. $p = 1$ is the boundary because $\int x^{-1}dx$ produces a logarithm, which
   grows without bound while every $p > 1$ produces a bounded power. The boundary
   case **diverges**.
5. $\left\lvert\frac{a_{n+1}}{a_n}\right\rvert = \left(\frac{n}{n+1}\right)^p \to 1$
   for every $p$. So the ratio test cannot distinguish the divergent
   $\sum\frac{1}{n}$ from the convergent $\sum\frac{1}{n^2}$, demonstrating that no
   single test suffices and that $p$-series need their own result.
6. Absolute: $\sum\lvert a_n\rvert$ converges — example $\sum\frac{(-1)^n}{n^2}$.
   Conditional: $\sum a_n$ converges but $\sum\lvert a_n\rvert$ does not — example
   $\sum\frac{(-1)^{n+1}}{n}$, the alternating harmonic series.
7. The ratio test yields $L = 1$ at both endpoints by construction, since the
   radius is defined by $L = 1$. Each endpoint produces a specific numerical series
   requiring its own test, and the two frequently behave differently.
8. They are the same result. $P_1(x) = f(a) + f'(a)(x-a)$ is Chapter 01-18's
   linear approximation verbatim. The Taylor series generalizes it by continuing
   with higher derivatives, and adds an error bound that Chapter 01-18 did not
   supply.
9. Error scales as the $(n+1)$st power of the distance from the centre, so it
   grows rapidly on leaving the centre and shrinks rapidly on approaching it.
   Truncated series are therefore inherently **local** tools, and extrapolation
   degrades by a power law rather than gracefully.
10. It requires alternation, where each omitted term partially cancels the last.
    In a positive series every omitted term adds to the shortfall, so the true
    error exceeds the first omitted term. The bound **understates** the error,
    which is dangerous because it produces false confidence — worse than having no
    bound at all.

### Calculation

11. (a) $a_n \to \frac{1}{2} \ne 0$ — **diverges**, $n$th term test.
    (b) $p = 1.5 > 1$ — **converges**, $p$-test.
    (c) $\frac{1}{3n-1} > \frac{1}{3n}$ and $\sum\frac{1}{3n}$ diverges —
    **diverges**, comparison.
    (d) $\left\lvert\frac{a_{n+1}}{a_n}\right\rvert = \frac{n+1}{n^2} \to 0$ —
    **converges**, ratio test.
    (e) $b_n = \frac{1}{\sqrt{n}}$ decreasing to zero — **converges**
    (conditionally, since $\sum\frac{1}{\sqrt{n}}$ has $p = 0.5$ and diverges),
    alternating series test.

12. (a) $\frac{1}{1-0.8} = \mathbf{5.00}$
    (b) First term $4(0.25) = 1$, ratio $0.25$: $\frac{1}{0.75} = \mathbf{1.333}$
    (c) $r = 1.1 > 1$ — **diverges**

13. (a) Ratio $= \frac{\lvert x\rvert}{n+1} \to 0$ for all $x$: $R = \infty$,
    interval $(-\infty, \infty)$.
    (b) Ratio $\to \frac{\lvert x-1\rvert}{2}$: $R = 2$, so $-1 < x < 3$. At
    $x = 3$: $\sum\frac{1}{n}$ diverges. At $x = -1$: $\sum\frac{(-1)^n}{n}$
    converges. Interval $\mathbf{[-1, 3)}$.
    (c) Ratio $\to \lvert x\rvert$: $R = 1$. Both endpoints give terms that do not
    approach zero, so both diverge. Interval $\mathbf{(-1, 1)}$.

14. (a) $1 + 3x + \frac{9x^2}{2} + \frac{9x^3}{2}$
    (b) $1 - 2x^2 + \frac{2x^4}{3} - \frac{4x^6}{45}$
    (c) $x + x^2 + \frac{x^3}{2} + \frac{x^4}{6}$
    (d) $2x - 2x^2 + \frac{8x^3}{3} - 4x^4$

15. $f(1) = 0$, $f'(1) = 1$, $f''(1) = -1$, $f'''(1) = 2$:

    $$\ln x = (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \cdots$$

    Substituting $u = x - 1$ gives
    $u - \frac{u^2}{2} + \frac{u^3}{3} - \cdots = \ln(1+u)$ ✓ — the same series,
    re-centred.

16. $1 + \frac{1}{2}(0.06) + \frac{(0.5)(-0.5)}{2}(0.06)^2 =
    1 + 0.03 - 0.00045 = \mathbf{1.02955}$.
    True value $1.0295630$; error $1.3\times10^{-5}$ ✓

17. $1 - \frac{0.04}{2} + \frac{0.0016}{24} = \mathbf{0.9800667}$.
    First omitted term $\frac{(0.2)^6}{720} = 8.9\times10^{-8}$.
    True value $0.98006658$, actual error $8.9\times10^{-8}$ — at the bound, as
    expected when the following term is negligible ✓

18. Relative error $\approx \frac{\theta^2}{3} = 0.005 \implies
    \theta = \sqrt{0.015} = 0.1225$ rad $= \mathbf{7.02°}$.
    Verify at $7°$: $\tan 7° = 0.122785$ against $\theta = 0.122173$, relative
    error $0.499\%$ ✓

19. (a) With $u = \frac{t}{0.050} = 20t$:

    $$v(t) = 12\left[20t - 200t^2 + 1333t^3 - \cdots\right] = \mathbf{240t - 2400t^2 + 16{,}000t^3 - \cdots}$$

    (b) Linear coefficient $= 240$ V/s. Directly:
    $\frac{dv}{dt}\big|_0 = \frac{12}{0.050} = 240$ V/s ✓
    (c) Relative error $\approx \frac{2400t^2}{240t} = 10t = 0.02 \implies
    t = \mathbf{0.0020\ s = 2.0\ ms}$. Consistent with the rule
    $t \approx 2\tau(\text{error}) = 2(0.050)(0.02) = 0.0020$ s ✓
    (d) Exact: $12\left(1 - e^{-0.2}\right) = 12(0.181269) = 2.1752$ V

    | Terms | Value (V) | Relative error |
    |---|---|---|
    | 1 | $2.400$ | $+10.3\%$ |
    | 2 | $2.160$ | $-0.70\%$ |
    | 3 | $2.176$ | $+0.035\%$ |

    Errors alternate in sign and shrink by more than an order of magnitude per
    term ✓

20. (a) $\Delta = L(1-\cos\theta) \approx L\left[1 - \left(1 -
    \frac{\theta^2}{2}\right)\right] = \mathbf{\frac{L\theta^2}{2}}$
    (b) $\theta = 6.00° = 0.104720$ rad:

    $$\Delta \approx \frac{2.00(0.0109662)}{2} = 0.010966 \text{ m} = \mathbf{10.97\ mm}$$

    Exact: $2.00(1 - 0.994522) = 0.010956$ m $= \mathbf{10.96}$ mm. Error
    $+0.09\%$ ✓
    (c) $\cos\theta \approx 1$ gives $\Delta = L(1-1) = \mathbf{0}$ — the
    approximation annihilates the entire quantity being computed. **The lesson:**
    when the quantity of interest is a *difference* of nearly equal terms, the
    approximation must be carried to at least one order beyond the cancellation.
    Dropping $\frac{\theta^2}{2}$ is harmless when you want $\cos\theta$ and fatal
    when you want $1 - \cos\theta$.

### Multiple Choice

21. **B** — $p = 3 > 1$, converges.
22. **C** — the test has failed; use another.
23. **C** — even powers, alternating signs, even factorials.
24. **B** — the geometric series with $r = x$.
25. **B** — $0.1 - \frac{0.001}{6} = 0.099833$; true value $0.0998334$.
26. **D** — $\sin x$ converges for all $x$; the other three have $R = 1$.
27. **C** — alternation is required.
28. **B** — about $1.15\%$ at $15°$; the 1% crossing is near $14°$.
29. **B** — $P_1(x) = f(a) + f'(a)(x-a)$ is the tangent line.
30. **C** — diverges, the standard counterexample to answer D's reasoning.

---

## Summary Card

**Convergence**

$$\sum_{n=1}^{\infty}a_n = \lim_{n\to\infty}S_n$$

| Test | Rule |
|---|---|
| $n$th term | $a_n \not\to 0 \implies$ diverges (one-way) |
| Geometric | $\sum ar^n = \frac{a}{1-r}$ for $\lvert r\rvert<1$ |
| $p$-series | $\sum n^{-p}$ converges iff $p > 1$ |
| Integral | same convergence as $\int_1^{\infty}f$, **not** same value |
| Comparison | squeeze against a known series, watch direction |
| Ratio | $L<1$ converges, $L>1$ diverges, $L=1$ inconclusive |
| Alternating | $b_n$ decreasing to 0 $\implies$ converges; error $\le b_{n+1}$ |

**Taylor series**

$$f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n \qquad E_n = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

**The six to memorize** (Maclaurin, $a = 0$)

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \qquad \text{all } x$$
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots \qquad \text{all } x$$
$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots \qquad \text{all } x$$
$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots \qquad -1 < x \le 1$$
$$\frac{1}{1-x} = 1 + x + x^2 + \cdots \qquad \lvert x\rvert < 1$$
$$(1+x)^n = 1 + nx + \frac{n(n-1)}{2!}x^2 + \cdots \qquad \lvert x\rvert < 1$$

**Small angles** — radians only

$$\sin\theta \approx \theta \quad\big(\text{rel. error} \approx \tfrac{\theta^2}{6}\big) \qquad \tan\theta \approx \theta \quad\big(\approx \tfrac{\theta^2}{3}\big) \qquad \cos\theta \approx 1 - \tfrac{\theta^2}{2}$$

| Rule | 1% accurate to |
|---|---|
| $\sin\theta\approx\theta$ | $\approx 14°$ |
| $\tan\theta\approx\theta$ | $\approx 10°$ |

**Exponential approach** — $1 - e^{-t/\tau} \approx \frac{t}{\tau}$ with relative
error $\approx \frac{t}{2\tau}$: good to 1% out to $0.02\tau$, to 10% out to
$0.2\tau$.

**Build new series from old:** substitute, add, multiply, differentiate,
integrate term by term. Faster than differentiating from scratch, and the only
route for integrands with no elementary antiderivative.

---

## Looking Ahead

This chapter closes single-variable calculus. Chapters 01-23 through 01-25 move to
multivariable calculus and differential equations, and three threads from here
continue directly into them.

**The exponential series meets complex numbers.** Substituting $j\theta$ into the
series for $e^x$ and separating real from imaginary parts produces Euler's formula,
$e^{j\theta} = \cos\theta + j\sin\theta$. That identity is the reason exponentials
solve oscillatory differential equations in Chapter 01-25 and the reason phasors
work in Chapter 02-63. It is a direct consequence of the three expansions you
memorized in §22.4.

**Linearization becomes a systematic method.** Here we linearized one function of
one variable. Chapter 01-23 extends the Taylor expansion to functions of several
variables, where the degree-1 term becomes a gradient. That is the tool behind
error propagation with multiple measurements, and behind linearizing a system
about an operating point.

**Series solve differential equations.** When an equation has no closed-form
solution — which is most of the time — assuming a power series solution and solving
for the coefficients is a standard technique. Chapter 01-25 uses it, and it depends
on the convergence machinery from §22.2 to know when the resulting series is
meaningful.

More immediately, the truncation-error habit belongs to you now rather than to
this chapter. Every time a later chapter says "assume small displacements,"
"assume the response is linear," or "neglect second-order terms," it is invoking
§22.5 and §22.6. You are equipped to ask what was dropped and how much it was
worth.
