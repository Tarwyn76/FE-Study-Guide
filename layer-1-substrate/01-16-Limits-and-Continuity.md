---
chapter: "01-16"
title: "Limits and Continuity"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-016-01, MATH-1C-016-02, MATH-1C-016-03, MATH-1C-016-04]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-16: Limits and Continuity

> *"A limit answers a question about a place you never actually reach: where
> is this function headed? Not what it equals when it arrives — what it is
> approaching on the way in. Every derivative is a limit. Every integral is a
> limit. Every convergence criterion in every numerical method is a limit.
> This is the concept that turns algebra into calculus, and it is worth an
> hour of your careful attention."*

---

## Before You Start

**Prerequisites:** [01-05 Exponents, Radicals, and Logarithms](01-05-exponents-radicals-logarithms.md) · [01-06 Functions, Graphs, and Transformations](01-06-functions-graphs-transformations.md) · [01-07 Polynomials and Their Roots](01-07-polynomials-roots.md) · [01-11 Trigonometry](01-11-trigonometry.md) · [01-15 Sequences, Series, and Progressions](01-15-sequences-series-progressions.md)

**Skip if:** You pass the Tier 1C test-out quiz. Verify you can resolve a
$0/0$ indeterminate form by factoring and by rationalizing, compare degrees
to find a limit at infinity, and state the three conditions for continuity
before skipping.

**Time:** ~55 min read · ~25 min review questions · ~55 min practice problems

---

## On the Board Today

Apprentice, welcome to Tier 1C. Everything up to now has been algebra,
geometry, and bookkeeping. Sound tools, all of them, and you will keep using
them on every page from here forward. But they share a limitation: they
describe quantities that hold still.

Calculus describes quantities that change. The rate at which a beam's
deflection changes along its length. The rate at which a tank's level changes
with time. The total heat that flows across a surface when the flux varies
from point to point. Those are the questions engineering actually asks, and
answering them requires one new idea.

That idea is the **limit**.

Here is the shape of it. Suppose you want the instantaneous velocity of
something at exactly $t = 3$ seconds. Average velocity over an interval is
easy: distance divided by time. But an *instant* has zero duration, and
dividing by zero is not an operation. So you do the next best thing. You
compute the average velocity over a small interval around $t = 3$. Then a
smaller one. Then smaller still. And you ask: what value are these averages
homing in on?

The answer to that question is the limit. You never divide by zero. You never
actually arrive at the instant. You determine where the sequence of answers is
headed, and you take that destination as the answer.

You have already done this once. In Chapter 01-15 I told you that an infinite
geometric series with $\lvert r \rvert < 1$ "settles onto" the value
$a_1/(1-r)$, and I said the phrase was doing real work that this chapter would
make precise. It is. The partial sums $S_n$ form a sequence, that sequence has
a limit, and the limit is the sum. That was a limit all along; you just did
not have the word.

We also need **continuity** — the property of a function having no breaks,
jumps, or holes. It sounds like a technicality and it is not. Continuity is
the hypothesis that makes root-finding algorithms work, that guarantees a
maximum stress exists somewhere in a loaded member, and that lets you assume
a temperature profile does not teleport from 40 °C to 90 °C without passing
through 65 °C along the way. Discontinuities in engineering models are real
and important, and you need to be able to spot them.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 16.1 State informally what $\lim_{x \to a}f(x) = L$ means and distinguish
  it from $f(a)$
* 16.2 Evaluate one-sided limits and use them to determine whether a
  two-sided limit exists
* 16.3 Identify the three ways a limit can fail to exist
* 16.4 Apply the limit laws for sums, products, quotients, powers, and roots
* 16.5 Evaluate limits by direct substitution, factoring, rationalizing, and
  combining fractions
* 16.6 Recognize the indeterminate form $0/0$ and explain why it requires
  algebraic work
* 16.7 Evaluate limits at infinity for rational and exponential functions and
  locate horizontal asymptotes
* 16.8 Evaluate infinite limits and locate vertical asymptotes
* 16.9 Apply the special trigonometric limits
  $\lim_{\theta \to 0}\frac{\sin\theta}{\theta} = 1$ and
  $\lim_{\theta \to 0}\frac{1 - \cos\theta}{\theta} = 0$
* 16.10 State the three conditions for continuity at a point and classify
  removable, jump, and infinite discontinuities
* 16.11 Determine a parameter value that makes a piecewise function continuous
* 16.12 Apply the Intermediate Value Theorem to establish that a root exists
  within an interval

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $\displaystyle\lim_{x \to a}f(x)$ | the limit of $f$ as $x$ approaches $a$ | $x$ never equals $a$ |
| $x \to a$ | "$x$ approaches $a$" | from both sides |
| $x \to a^-$ | approach from the **left**, $x < a$ | left-hand limit |
| $x \to a^+$ | approach from the **right**, $x > a$ | right-hand limit |
| $L$ | the limiting value | a finite number, when it exists |
| $\infty$, $-\infty$ | unbounded growth, positive or negative | not a number |
| DNE | does not exist | the correct answer when no limit exists |
| $f(a)$ | the **value** of $f$ at $a$ | may differ from the limit, or not exist |
| $\varepsilon$, $\delta$ | tolerance and window in the formal definition | mentioned, not used computationally |

> ---
> **Mentor's Margin**
>
> Write the arrow. $\lim_{x \to 3}$ is a complete instruction; a bare "lim" is
> not. The limit symbol without a stated approach point and approach value is
> like a summation without limits — it does not specify a calculation. This
> matters more than it sounds like it should, because a great many limit
> errors on exams trace back to a student writing $\lim$ once at the start of
> a multi-line derivation and then losing track of what $x$ was approaching by
> line four. Carry the subscript on every line until you evaluate it.
>
> ---

---

## 16.1 The Idea of a Limit

Consider the function

$$f(x) = \frac{x^2 - 9}{x - 3}$$

At $x = 3$ this is $\frac{0}{0}$. Undefined. The function has no value there
— there is a **hole** in its graph at $x = 3$.

But ask a different question. What happens *near* $x = 3$?

| $x$ | $f(x)$ |
|---|---|
| 2.9 | 5.9 |
| 2.99 | 5.99 |
| 2.999 | 5.999 |
| 3 | **undefined** |
| 3.001 | 6.001 |
| 3.01 | 6.01 |
| 3.1 | 6.1 |

From both sides, the values are homing in on 6. They get arbitrarily close to
6 and never stop getting closer. We write

$$\lim_{x \to 3}\frac{x^2-9}{x-3} = 6$$

and read it: "the limit of $f(x)$ as $x$ approaches 3 is 6."

![FIG-01-16-001: Graph of f(x) = (x²−9)/(x−3), which is the line y = x + 3 with an open circle (hole) at the point (3, 6). Dashed arrows along the curve approach the hole from the left and from the right, with horizontal dashed lines from both directions converging on y = 6 on the vertical axis. A callout labels the hole "f(3) undefined" and labels the height "limit = 6".](../figures/FIG-01-16-001-limit-concept.png)

### The critical distinction

$$\lim_{x \to a}f(x) \quad \text{and} \quad f(a) \quad \text{are different questions.}$$

- $f(a)$ asks: what is the function's **value at** $a$?
- $\lim_{x\to a}f(x)$ asks: what value is the function **approaching near** $a$?

The limit deliberately ignores what happens *at* $x = a$. It looks only at
the neighbourhood. In our example $f(3)$ does not exist, and yet the limit is
a perfectly ordinary number.

Three combinations are all possible:

| Situation | Example |
|---|---|
| Limit exists, $f(a)$ does not | $\dfrac{x^2-9}{x-3}$ at $a = 3$ |
| Both exist and are equal | $x^2$ at $a = 3$: both are 9 |
| Both exist and differ | a piecewise function redefined at one point |

That third case is the strangest, and it is the reason continuity gets its own
definition later in this chapter.

### The formal definition, for context

$\lim_{x\to a}f(x) = L$ means: for every tolerance $\varepsilon > 0$, however
small, there is a window $\delta > 0$ around $a$ such that whenever
$0 < \lvert x - a\rvert < \delta$, we have $\lvert f(x) - L\rvert <
\varepsilon$.

In plain terms: name any error budget you like, and I can give you a window
around $a$ inside which the function stays within that budget of $L$.

> ---
> **Mentor's Margin**
>
> You will not be asked to construct an $\varepsilon$–$\delta$ proof on the
> FE. I include the definition because engineers meet the same logical
> structure in specification and tolerance work: "for any required accuracy,
> here is the operating window that achieves it." That is a spec statement,
> and it is the same shape as this definition. Read it once, understand the
> shape, then work with limits the practical way — algebraically.
>
> ---

---

## 16.2 One-Sided Limits

Sometimes a function behaves differently on each side of a point. So we split
the question.

$$\lim_{x \to a^-}f(x) \quad \text{approach from the left } (x < a)$$

$$\lim_{x \to a^+}f(x) \quad \text{approach from the right } (x > a)$$

The relationship to the two-sided limit is the whole point:

$$\boxed{\lim_{x\to a}f(x) = L \iff \lim_{x\to a^-}f(x) = L \;\text{ and }\; \lim_{x\to a^+}f(x) = L}$$

The two-sided limit exists **only if both one-sided limits exist and agree**.
If they disagree, the two-sided limit does not exist.

### Worked Example 1 — One-Sided Limits of a Piecewise Function

**Given.**

$$f(x) = \begin{cases} 2x + 1, & x < 1 \\ 5 - x, & x > 1 \end{cases}$$

**Find.** $\lim_{x\to 1^-}f(x)$, $\lim_{x\to 1^+}f(x)$, and
$\lim_{x\to 1}f(x)$.

**Solution.**

Approaching from the left means $x < 1$, so the first branch applies:

$$\lim_{x\to 1^-}f(x) = 2(1) + 1 = 3$$

Approaching from the right means $x > 1$, so the second branch applies:

$$\lim_{x\to 1^+}f(x) = 5 - 1 = 4$$

The one-sided limits exist but disagree: $3 \ne 4$. Therefore

$$\boxed{\lim_{x\to 1}f(x) \text{ does not exist (DNE)}}$$

**Note.** $f(1)$ also does not exist here, since neither branch includes
$x = 1$. But that is a separate fact. Even if we defined $f(1) = 3.5$, the
two-sided limit would still be DNE, because the limit ignores the value at
the point and only cares that the two approaches disagree.

> ---
> **Mentor's Margin**
>
> One-sided limits are not an academic refinement. Engineering functions are
> full of genuine one-sided behaviour: a material's stress–strain curve has a
> different slope loading than unloading; a valve's flow characteristic
> changes at the point it cracks open; a beam's shear diagram jumps at a point
> load. When a physical quantity behaves differently on either side of a
> threshold, the one-sided limit is the honest description and the two-sided
> limit genuinely does not exist. Do not force a two-sided answer where the
> physics has a corner in it.
>
> ---

---

## 16.3 The Three Ways a Limit Fails

A two-sided limit fails to exist in exactly three ways.

**1. The one-sided limits disagree (a jump).** Worked Example 1 above.

**2. The function grows without bound.** As $x \to 2$, $\frac{1}{(x-2)^2}$
increases past every finite value. There is no finite $L$ to approach. We may
write $\lim_{x\to 2}\frac{1}{(x-2)^2} = \infty$ as a *description of the
behaviour*, but the limit does not exist as a number.

**3. The function oscillates without settling.** As $x \to 0$,
$\sin\!\left(\frac{1}{x}\right)$ swings between $-1$ and $+1$ infinitely
often, no matter how small a window you choose. It never homes in on
anything.

![FIG-01-16-002: Three side-by-side panels titled "Three ways a limit fails". Panel 1 (jump): a piecewise graph with a filled dot at height 3 on the left branch and an open dot at height 4 on the right branch at x = 1, with the vertical gap labeled "one-sided limits disagree". Panel 2 (unbounded): the graph of 1/(x−2)² with a vertical dashed asymptote at x = 2 and both branches sweeping upward off the top of the frame, labeled "grows without bound". Panel 3 (oscillation): the graph of sin(1/x) near x = 0, compressing into ever-tighter oscillations between −1 and +1 as x approaches 0, labeled "never settles".](../figures/FIG-01-16-002-limit-failure-modes.png)

---

## 16.4 The Limit Laws

If $\lim_{x\to a}f(x)$ and $\lim_{x\to a}g(x)$ both exist, then limits
distribute over the ordinary algebraic operations. Let
$L = \lim_{x\to a}f(x)$ and $M = \lim_{x\to a}g(x)$.

| Law | Statement |
|---|---|
| Constant | $\displaystyle\lim_{x\to a}c = c$ |
| Identity | $\displaystyle\lim_{x\to a}x = a$ |
| Scalar multiple | $\displaystyle\lim_{x\to a}c\,f(x) = cL$ |
| Sum / difference | $\displaystyle\lim_{x\to a}\big[f(x) \pm g(x)\big] = L \pm M$ |
| Product | $\displaystyle\lim_{x\to a}\big[f(x)\,g(x)\big] = LM$ |
| Quotient | $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)} = \frac{L}{M}$, **provided** $M \ne 0$ |
| Power | $\displaystyle\lim_{x\to a}\big[f(x)\big]^n = L^n$ |
| Root | $\displaystyle\lim_{x\to a}\sqrt[n]{f(x)} = \sqrt[n]{L}$, provided the root is defined |

Notice the difference from summation notation in Chapter 01-15: limits **do**
distribute over products and quotients, where summations do not. The catch is
the proviso on the quotient law, and that proviso is where all the
interesting work lives.

### Direct substitution

Every polynomial is built from constants, $x$, sums, and products. Applying
the laws repeatedly gives the practical rule:

$$\boxed{\text{For any polynomial } p(x): \quad \lim_{x\to a}p(x) = p(a)}$$

For a rational function $\frac{p(x)}{q(x)}$, the quotient law gives

$$\lim_{x\to a}\frac{p(x)}{q(x)} = \frac{p(a)}{q(a)} \qquad \text{provided } q(a) \ne 0$$

**Try direct substitution first, every time.** It works far more often than
students expect, and it takes five seconds.

---

## 16.5 Indeterminate Forms and How to Resolve Them

Direct substitution fails when it produces $\frac{0}{0}$.

This is an **indeterminate form**. The name is precise: the form $\frac{0}{0}$
does not determine the answer. Different functions producing $\frac{0}{0}$ at
the same point have different limits — some finite, some infinite, some
nonexistent. The symbol tells you nothing except *do more work*.

$$\frac{0}{0} \quad \text{means: the substitution was inconclusive, not that the answer is 0 or 1 or } \infty$$

The cause is always the same: numerator and denominator share a factor that
vanishes at $x = a$. Cancel it and the obstruction disappears.

### Three algebraic techniques

**Technique 1 — Factor and cancel.** For polynomials.

$$\lim_{x\to 2}\frac{x^2-4}{x^2-x-2} = \lim_{x\to 2}\frac{(x-2)(x+2)}{(x-2)(x+1)} = \lim_{x\to 2}\frac{x+2}{x+1} = \frac{4}{3}$$

The cancellation is legitimate because $x \ne 2$ throughout the limit process
— we never evaluate *at* 2, so dividing by $(x-2)$ is never dividing by zero.
This is the single most important thing to understand about why the technique
is valid.

**Technique 2 — Rationalize.** When a square root is present, multiply by the
conjugate.

**Technique 3 — Combine fractions.** When the expression contains a
difference of fractions, put them over a common denominator first.

### Worked Example 2 — Factoring

**Given.** Evaluate $\displaystyle\lim_{x\to -3}\frac{x^2 + x - 6}{x^2 - 9}$.

**Solution.**

Direct substitution: numerator $= 9 - 3 - 6 = 0$; denominator $= 9 - 9 = 0$.
Indeterminate form $\frac{0}{0}$ — proceed algebraically.

Factor both:

$$\frac{x^2+x-6}{x^2-9} = \frac{(x+3)(x-2)}{(x+3)(x-3)}$$

Cancel $(x+3)$, valid since $x \ne -3$ during the approach:

$$\lim_{x\to -3}\frac{x-2}{x-3} = \frac{-3-2}{-3-3} = \frac{-5}{-6} = \boxed{\frac{5}{6}}$$

**Check numerically.** At $x = -3.001$:
numerator $= 9.006 - 3.001 - 6 = 0.005$ (to three figures, $0.005001$);
denominator $= 9.006001 - 9 = 0.006001$. Ratio $= 0.8334$.

And $5/6 = 0.8333$ ✓

### Worked Example 3 — Rationalizing

**Given.** Evaluate $\displaystyle\lim_{x\to 0}\frac{\sqrt{x+4}-2}{x}$.

**Solution.**

Direct substitution gives $\frac{\sqrt{4}-2}{0} = \frac{0}{0}$.
Indeterminate.

Multiply numerator and denominator by the conjugate $\sqrt{x+4}+2$:

$$\frac{\sqrt{x+4}-2}{x}\cdot\frac{\sqrt{x+4}+2}{\sqrt{x+4}+2} = \frac{(x+4) - 4}{x\left(\sqrt{x+4}+2\right)} = \frac{x}{x\left(\sqrt{x+4}+2\right)}$$

Cancel $x$ (valid, since $x \ne 0$ during the approach):

$$\lim_{x\to 0}\frac{1}{\sqrt{x+4}+2} = \frac{1}{\sqrt{4}+2} = \frac{1}{4} = \boxed{0.25}$$

**Check numerically.** At $x = 0.01$: $\sqrt{4.01} = 2.002498$, so the
numerator is $0.002498$ and the quotient is $0.2498$ ✓

### Worked Example 4 — Combining Fractions

**Given.** Evaluate $\displaystyle\lim_{h\to 0}\frac{\frac{1}{4+h} - \frac{1}{4}}{h}$.

**Solution.**

Direct substitution gives $\frac{0}{0}$.

Combine the numerator over the common denominator $4(4+h)$:

$$\frac{1}{4+h} - \frac{1}{4} = \frac{4 - (4+h)}{4(4+h)} = \frac{-h}{4(4+h)}$$

Now divide by $h$, which means multiplying by $\frac{1}{h}$:

$$\frac{-h}{4(4+h)}\cdot\frac{1}{h} = \frac{-1}{4(4+h)}$$

$$\lim_{h\to 0}\frac{-1}{4(4+h)} = \frac{-1}{4(4)} = \boxed{-\frac{1}{16}}$$

> ---
> **Mentor's Margin**
>
> Look closely at the structure of Worked Example 4. It is
> $\frac{f(4+h)-f(4)}{h}$ with $f(x) = \frac{1}{x}$, and we took its limit as
> $h \to 0$. That expression has a name and it is coming in Chapter 01-17: it
> is the **difference quotient**, and its limit is the derivative. Every
> derivative you ever compute is a limit of exactly this form. When you meet
> the derivative rules next chapter and they look like they were handed down
> from nowhere, remember that each one was obtained by doing what we just did
> — algebraically resolving a $0/0$ form.
>
> ---

### A note on L'Hôpital's rule

> **Preview note.** There is a powerful shortcut for indeterminate forms
> called L'Hôpital's rule, which appears in the Handbook. It requires
> derivatives, so it belongs to Chapter 01-18, not here. You do not need it:
> every $0/0$ limit in this chapter is resolvable by factoring,
> rationalizing, or combining fractions, and those techniques will remain
> faster than L'Hôpital's rule for most polynomial and radical cases even
> after you learn it. Nothing in this chapter depends on that later material.

---

## 16.6 Limits at Infinity and Horizontal Asymptotes

Now a different question: what happens as $x$ grows without bound?

$$\lim_{x\to\infty}f(x) = L \quad \text{means } f(x) \text{ approaches } L \text{ as } x \text{ increases without bound}$$

When such a limit exists, the line $y = L$ is a **horizontal asymptote** of
the graph — the same asymptote idea you met with parent functions in Chapter
01-06, now with a precise definition behind it.

The foundational fact:

$$\boxed{\lim_{x\to\infty}\frac{1}{x^n} = 0 \qquad \text{for any } n > 0}$$

### Rational functions: compare the degrees

For a rational function, divide numerator and denominator by the highest
power of $x$ in the **denominator**, then apply the fact above. Doing this in
general yields a rule you should know cold.

Let $p(x)$ have degree $m$ with leading coefficient $a$, and $q(x)$ have
degree $n$ with leading coefficient $b$.

| Case | $\displaystyle\lim_{x\to\infty}\frac{p(x)}{q(x)}$ | Asymptote |
|---|---|---|
| $m < n$ (bottom-heavy) | $0$ | $y = 0$ |
| $m = n$ (balanced) | $\dfrac{a}{b}$ — ratio of leading coefficients | $y = a/b$ |
| $m > n$ (top-heavy) | unbounded; DNE as a finite value | none |

![FIG-01-16-003: Three side-by-side panels each showing a rational function graphed over a wide x-range with a horizontal dashed reference line. Panel 1: (4x+1)/(x²−3) flattening onto y = 0, labeled "degree bottom-heavy, limit 0". Panel 2: (3x²+5x−2)/(7x²−x+4) flattening onto a dashed line at y = 3/7 ≈ 0.4286, labeled "degrees equal, limit = ratio of leading coefficients". Panel 3: (2x³−x)/(5x²+1) rising steadily off the top of the frame with no horizontal asymptote, labeled "degree top-heavy, unbounded".](../figures/FIG-01-16-003-limits-at-infinity.png)

### Worked Example 5 — All Three Degree Cases

**Given.** Evaluate each limit as $x \to \infty$.

**(a)** $\dfrac{4x+1}{x^2-3}$  **(b)** $\dfrac{3x^2+5x-2}{7x^2-x+4}$
**(c)** $\dfrac{2x^3-x}{5x^2+1}$

**Solution.**

**(a)** Divide numerator and denominator by $x^2$:

$$\frac{4x+1}{x^2-3} = \frac{\frac{4}{x} + \frac{1}{x^2}}{1 - \frac{3}{x^2}} \longrightarrow \frac{0 + 0}{1 - 0} = \boxed{0}$$

Degree 1 over degree 2 — bottom-heavy. Horizontal asymptote $y = 0$.

**(b)** Divide by $x^2$:

$$\frac{3 + \frac{5}{x} - \frac{2}{x^2}}{7 - \frac{1}{x} + \frac{4}{x^2}} \longrightarrow \frac{3 - 0 - 0}{7 - 0 + 0} = \boxed{\frac{3}{7} \approx 0.4286}$$

Degrees equal — the ratio of leading coefficients. Horizontal asymptote
$y = 3/7$.

**(c)** Divide by $x^2$:

$$\frac{2x - \frac{1}{x}}{5 + \frac{1}{x^2}} \longrightarrow \frac{\text{unbounded}}{5}$$

The numerator grows without bound. $\boxed{\text{No finite limit; DNE}}$

Degree 3 over degree 2 — top-heavy. No horizontal asymptote.

### Exponential limits

Two you should know without thinking:

$$\lim_{x\to\infty}e^{-x} = 0 \qquad \lim_{x\to\infty}e^{x} = \infty \;(\text{unbounded})$$

The first is the mathematical statement behind the five-tau rule from
Chapter 01-05, and it is what makes the saturating exponential model behave.

### Worked Example 6 — Terminal Behaviour of a Saturating Response

**Given.** A first-order system responds to a step input as

$$v(t) = v_\infty\left(1 - e^{-t/\tau}\right)$$

with $v_\infty = 18$ m/s and $\tau = 4.0$ s.

**(a)** Evaluate $\lim_{t\to\infty}v(t)$ and interpret it.
**(b)** Evaluate $v(t)$ at $t = 5\tau$ and compare to the limit.

**Solution.**

**(a)** As $t \to \infty$, the exponent $-t/\tau \to -\infty$, so
$e^{-t/\tau} \to 0$:

$$\lim_{t\to\infty}v(t) = 18(1 - 0) = \boxed{18 \text{ m/s}}$$

This is the **terminal** or steady-state value. The system approaches 18 m/s
and never exceeds it. Note that it is never *reached* at any finite time —
the limit is the destination, not an attained value. That is precisely the
distinction from §16.1, appearing in a physical setting.

**(b)** At $t = 5\tau = 20$ s:

$$v = 18\left(1 - e^{-5}\right) = 18(1 - 0.0067379) = 18(0.9932621) = 17.879 \text{ m/s}$$

$$\frac{17.879}{18} = 0.9933 = 99.33\% \text{ of terminal}$$

**Interpretation.** The five-tau rule from Chapter 01-05 says a first-order
system reaches about 99.3% of its final value in five time constants. Here is
the arithmetic behind that rule of thumb, and here is the limit that defines
what "final value" means. For engineering purposes 99.3% is
indistinguishable from complete, which is why five time constants is the
standard settling criterion.

---

## 16.7 Infinite Limits and Vertical Asymptotes

When a function grows without bound as $x$ approaches a finite value, we
describe the behaviour with an infinite limit.

$$\lim_{x\to 2}\frac{1}{(x-2)^2} = \infty$$

The line $x = 2$ is a **vertical asymptote**.

Be careful with signs, and use one-sided limits when the two sides differ:

$$\lim_{x\to 2^-}\frac{1}{x-2} = -\infty \qquad \lim_{x\to 2^+}\frac{1}{x-2} = +\infty$$

Approaching 2 from the left, $x - 2$ is a small negative number, so its
reciprocal is a large negative number. From the right, a small positive
number, so a large positive reciprocal. The two sides disagree, so the
two-sided limit does not exist even as $\pm\infty$.

For $\frac{1}{(x-2)^2}$ the denominator is positive on both sides, so both
one-sided limits are $+\infty$ and the two-sided behaviour is consistent.

> ---
> **Mentor's Margin**
>
> $\infty$ is not a number and you may not do arithmetic with it. There is no
> such thing as $\infty - \infty = 0$ or $\frac{\infty}{\infty} = 1$. Those
> are indeterminate forms, exactly like $\frac{0}{0}$: they tell you the
> substitution was inconclusive and nothing more. Writing
> $\lim f(x) = \infty$ is shorthand for "grows without bound," a statement
> about behaviour, not an equation about a quantity. Treat it as a description
> and you will not go wrong.
>
> ---

**A form that is *not* indeterminate:** $\frac{\text{nonzero}}{0}$. If the
numerator approaches a nonzero constant and the denominator approaches zero,
the magnitude grows without bound — that is determinate. Only
$\frac{0}{0}$ requires algebraic resolution. Check the numerator before you
start factoring.

---

## 16.8 The Special Trigonometric Limits

Two limits arise so often that they are worth memorizing outright.

$$\boxed{\lim_{\theta\to 0}\frac{\sin\theta}{\theta} = 1 \qquad (\theta \text{ in radians})}$$

$$\boxed{\lim_{\theta\to 0}\frac{1 - \cos\theta}{\theta} = 0 \qquad (\theta \text{ in radians})}$$

The radian requirement is not negotiable. Both results are false in degrees.
This is one of the concrete reasons calculus uses radians: the formulas come
out clean only in that unit.

The first limit says that for small angles, $\sin\theta \approx \theta$. That
is the **small-angle approximation**, and you will meet it constantly — in
pendulum analysis, in beam slope calculations, in optics, in any linearization
around a small rotation.

![FIG-01-16-004: Two-panel figure. Left panel: graph of y = sin(θ)/θ plotted from θ = −6 to 6 radians, showing the curve peaking near θ = 0 with an open circle (hole) at the point (0, 1), and dashed arrows approaching the hole from both sides converging on y = 1. Right panel: a unit-circle sector with a small angle θ marked, showing the arc length θ, the chord, and the vertical segment sin θ superimposed, with a callout noting that arc and vertical segment become indistinguishable as θ shrinks — the geometric reason the ratio tends to 1.](../figures/FIG-01-16-004-sine-over-theta.png)

### Handling variations

Any limit of the form $\frac{\sin(kx)}{x}$ is managed by forcing the
argument of the sine and the denominator to match.

### Worked Example 7 — Variations on the Sine Limit

**Given.** Evaluate:
**(a)** $\displaystyle\lim_{x\to 0}\frac{\sin 5x}{3x}$
**(b)** $\displaystyle\lim_{\theta\to 0}\frac{1-\cos\theta}{\theta}$ — verify
it algebraically rather than quoting it.

**Solution.**

**(a)** Multiply and divide to make the sine argument match its denominator:

$$\frac{\sin 5x}{3x} = \frac{5}{3}\cdot\frac{\sin 5x}{5x}$$

As $x \to 0$, the quantity $5x \to 0$ as well, so the second factor is
exactly the standard limit with $\theta = 5x$:

$$\lim_{x\to 0}\frac{\sin 5x}{3x} = \frac{5}{3}(1) = \boxed{\frac{5}{3}}$$

**Check numerically.** At $x = 0.001$: $\sin(0.005) = 0.00499998$, and
$3x = 0.003$. Ratio $= 1.6667$. And $5/3 = 1.6667$ ✓

**(b)** Multiply by the conjugate $(1 + \cos\theta)$:

$$\frac{1-\cos\theta}{\theta}\cdot\frac{1+\cos\theta}{1+\cos\theta} = \frac{1-\cos^2\theta}{\theta\left(1+\cos\theta\right)}$$

By the Pythagorean identity from Chapter 01-11, $1 - \cos^2\theta =
\sin^2\theta$:

$$= \frac{\sin^2\theta}{\theta(1+\cos\theta)} = \underbrace{\frac{\sin\theta}{\theta}}_{\to\, 1}\cdot\underbrace{\frac{\sin\theta}{1+\cos\theta}}_{\to\, 0/2\, =\, 0}$$

By the product law:

$$\lim_{\theta\to 0}\frac{1-\cos\theta}{\theta} = (1)(0) = \boxed{0}$$

**Check numerically.** At $\theta = 0.01$ rad: $\cos(0.01) = 0.99995000$, so
the numerator is $0.00005000$ and the quotient is $0.005000$ — small and
heading to 0 ✓

---

## 16.9 Continuity

A function is **continuous at $x = a$** if all three of these hold:

$$\boxed{\begin{aligned} &\text{(1) } f(a) \text{ exists} \\ &\text{(2) } \lim_{x\to a}f(x) \text{ exists} \\ &\text{(3) } \lim_{x\to a}f(x) = f(a)\end{aligned}}$$

Informally: you can draw the graph through $x = a$ without lifting your
pencil. No hole, no jump, no blow-up.

A function is **continuous on an interval** if it is continuous at every point
in that interval.

### Which functions are continuous?

| Family | Continuity |
|---|---|
| Polynomials | continuous everywhere |
| Rational functions | continuous except where the denominator is zero |
| $\sin x$, $\cos x$ | continuous everywhere |
| $\tan x$ | continuous except at odd multiples of $\pi/2$ |
| $e^x$ | continuous everywhere |
| $\ln x$ | continuous for $x > 0$ |
| $\sqrt{x}$ | continuous for $x \ge 0$ |
| Sums, products, quotients, compositions | continuous wherever the pieces are, subject to nonzero denominators |

Most of the time, then, checking continuity is checking for the specific
places where something breaks: a zero denominator, a negative radicand, a
non-positive logarithm argument, or a branch boundary in a piecewise
definition.

### Classifying discontinuities

| Type | What happens | Fixable? |
|---|---|---|
| **Removable** (hole) | limit exists, but $f(a)$ is missing or has the wrong value | Yes — redefine $f(a)$ to equal the limit |
| **Jump** | one-sided limits exist but differ | No |
| **Infinite** | function unbounded near $a$; vertical asymptote | No |

![FIG-01-16-005: Four panels in a row, each a small graph. Panel 1 "Continuous": a smooth unbroken curve passing through a filled dot at x = a. Panel 2 "Removable": the same smooth curve with an open circle at x = a and an arrow labeling "redefine f(a) to fix". Panel 3 "Jump": two branches with a filled dot at one height and an open dot at another height at x = a, vertical gap labeled. Panel 4 "Infinite": a curve with a vertical dashed asymptote at x = a, branches sweeping to +∞ and −∞. Each panel labeled with which of the three continuity conditions fails.](../figures/FIG-01-16-005-discontinuity-types.png)

### Worked Example 8 — Making a Piecewise Function Continuous

**Given.**

$$f(x) = \begin{cases} x^2 + k, & x < 2 \\ 3x - 1, & x \ge 2\end{cases}$$

**Find.** The value of $k$ that makes $f$ continuous at $x = 2$.

**Solution.**

Check the three conditions at $a = 2$.

**Condition 1.** $f(2)$ uses the second branch (it includes $x = 2$):

$$f(2) = 3(2) - 1 = 5$$

Exists ✓

**Condition 2.** The limit exists only if the one-sided limits agree.

$$\lim_{x\to 2^-}f(x) = (2)^2 + k = 4 + k$$

$$\lim_{x\to 2^+}f(x) = 3(2) - 1 = 5$$

**Condition 3.** Setting all three equal:

$$4 + k = 5 \implies \boxed{k = 1}$$

**Verify.** With $k = 1$:

Left limit: $4 + 1 = 5$. Right limit: $5$. Value: $f(2) = 5$.

All three agree, so $f$ is continuous at $x = 2$ ✓

Away from $x = 2$ both branches are polynomials, continuous everywhere, so
$f$ is continuous on all of $\mathbb{R}$.

**What if $k \ne 1$?** Say $k = 3$. Then the left limit is 7, the right limit
is 5, and we have a **jump discontinuity** of size 2 at $x = 2$ — not
removable by any choice of $f(2)$.

---

## 16.10 The Intermediate Value Theorem

This is the one theorem from this chapter that you will use as a working tool
rather than as background.

> **Intermediate Value Theorem (IVT).** If $f$ is continuous on the closed
> interval $[a, b]$, and $N$ is any value between $f(a)$ and $f(b)$, then
> there exists at least one $c$ in $(a, b)$ with $f(c) = N$.

In words: a continuous function cannot skip values. To get from $f(a)$ to
$f(b)$ it must pass through everything in between.

### The root-bracketing corollary

The special case $N = 0$ is the one that matters:

$$\boxed{\text{If } f \text{ is continuous on } [a,b] \text{ and } f(a) \text{ and } f(b) \text{ have opposite signs, then } f \text{ has at least one root in } (a,b).}$$

A sign change brackets a root. That single statement is the foundation of the
bisection method and of every bracketing root-finder you will meet.

![FIG-01-16-006: Two panels. Left panel "Continuous — IVT applies": a smooth curve from a point below the x-axis at (a, f(a)) rising to a point above the x-axis at (b, f(b)), crossing the axis at a marked point c, with f(a) < 0 < f(b) labeled and the crossing labeled "root guaranteed". Right panel "Discontinuous — IVT does not apply": a curve that jumps across the x-axis at a vertical asymptote between a and b, with f(a) < 0 and f(b) > 0 but no crossing point, labeled "sign change without a root".](../figures/FIG-01-16-006-intermediate-value-theorem.png)

### Worked Example 9 — Bracketing the Roots of a Cubic

**Given.** $f(x) = x^3 - 4x + 1$.

**(a)** Show that $f$ has a root in $(1, 2)$.
**(b)** Find two more intervals of unit length that each bracket a root.
**(c)** How many real roots does $f$ have, and how do you know you have found
them all?

**Solution.**

**(a)** $f$ is a polynomial, so it is continuous on every interval — the IVT
hypothesis is satisfied automatically.

$$f(1) = 1 - 4 + 1 = -2$$

$$f(2) = 8 - 8 + 1 = +1$$

Opposite signs. By the IVT there exists $c \in (1,2)$ with $f(c) = 0$ ✓

**(b)** Tabulate:

| $x$ | $f(x) = x^3 - 4x + 1$ | Sign |
|---|---|---|
| $-3$ | $-27 + 12 + 1 = -14$ | $-$ |
| $-2$ | $-8 + 8 + 1 = +1$ | $+$ |
| $-1$ | $-1 + 4 + 1 = +4$ | $+$ |
| $0$ | $+1$ | $+$ |
| $1$ | $-2$ | $-$ |
| $2$ | $+1$ | $+$ |

Sign changes occur across $(-3, -2)$, $(0, 1)$, and $(1, 2)$.

$$\boxed{\text{Roots bracketed in } (-3,-2), \; (0,1), \; \text{and } (1,2)}$$

**(c)** A cubic has exactly three roots counted with multiplicity
(fundamental theorem of algebra, Chapter 01-07). We have located three sign
changes, so all three roots are real, distinct, and accounted for. There can
be no others.

**Check the total.** By Vieta's formulas from Chapter 01-07, the sum of the
roots of $x^3 + 0x^2 - 4x + 1$ is $-\frac{b}{a} = 0$. Our three brackets
suggest roots near $-2.1$, $0.25$, and $1.86$. Sum $\approx 0.01$ — zero to
the precision of our bracketing ✓ And the product of the roots should be
$-\frac{d}{a} = -1$: $(-2.1)(0.25)(1.86) = -0.976 \approx -1$ ✓

> ---
> **Mentor's Margin**
>
> This example is the whole basis of the bisection method, which you will meet
> formally in Chapter 01-26. The algorithm is nothing more than repeated
> application of what we just did: find a sign change, cut the interval in
> half, keep whichever half still has the sign change, repeat. Each step
> halves your uncertainty. The reason it is guaranteed to converge is the IVT,
> and the reason it can fail is the right-hand panel of the figure — a sign
> change across a discontinuity brackets no root at all. Always confirm
> continuity on the bracket before trusting a sign change.
>
> ---

---

## 16.11 Closing the Loop on Chapter 01-15

Recall the geometric partial sum:

$$S_n = \frac{a_1\left(1 - r^n\right)}{1 - r}$$

The sum of the infinite series is *defined* as the limit of the partial sums:

$$S_\infty \equiv \lim_{n\to\infty}S_n = \lim_{n\to\infty}\frac{a_1\left(1-r^n\right)}{1-r}$$

For $\lvert r \rvert < 1$, repeated multiplication by a factor smaller than 1
in magnitude drives $r^n \to 0$, so:

$$S_\infty = \frac{a_1(1 - 0)}{1-r} = \frac{a_1}{1-r} \qquad \checkmark$$

For $\lvert r \rvert > 1$, $r^n$ grows without bound and the limit does not
exist — the series diverges.

That is the rigorous version of "settles onto." The convergence condition
$\lvert r\rvert < 1$ from Chapter 01-15 is exactly the condition under which
$\lim_{n\to\infty}r^n = 0$. Nothing about the formula changed; you now know
what the phrase meant.

---

## As the Handbook States It

> **Handbook 10.6, Mathematics section (begins p. 36)** — limits appear
> within the *Differential Calculus* subsection, approximately pp. 44–45.

The Handbook's treatment of limits is **thin**. It is a formula reference, not
a textbook, and limits are mostly a conceptual prerequisite rather than a
source of formulas. What you will find:

- L'Hôpital's rule for indeterminate forms (requires derivatives — Chapter
  01-18)
- The definition of the derivative as a limit of the difference quotient
- Convergence conditions stated alongside the infinite series formulas

**What's not in the Handbook — memorize:**

Nearly all of this chapter. Specifically:

- The definition of a limit and the distinction between
  $\lim_{x\to a}f(x)$ and $f(a)$
- One-sided limit notation and the requirement that both agree for the
  two-sided limit to exist
- The three failure modes: jump, unbounded, oscillation
- All of the limit laws
- Direct substitution for polynomials and rational functions
- Recognition of $\frac{0}{0}$ as indeterminate, and the factoring,
  rationalizing, and common-denominator techniques for resolving it
- That $\frac{\text{nonzero}}{0}$ is **not** indeterminate
- $\lim_{x\to\infty}\frac{1}{x^n} = 0$
- The degree-comparison rule for rational limits at infinity
- $\lim_{x\to\infty}e^{-x} = 0$
- $\lim_{\theta\to 0}\frac{\sin\theta}{\theta} = 1$ and
  $\lim_{\theta\to 0}\frac{1-\cos\theta}{\theta} = 0$, both **in radians**
- The three conditions for continuity
- The classification of removable, jump, and infinite discontinuities
- The Intermediate Value Theorem and the sign-change root-bracketing
  corollary

> ---
> **Mentor's Margin**
>
> Because the Handbook offers almost nothing here, treat this chapter as a
> memorize chapter and budget your review time accordingly. The good news is
> that limits appear on the exam mostly as *tools inside other problems* —
> resolving an indeterminate form to evaluate a rate, checking whether a model
> has a horizontal asymptote, confirming a root is bracketed — rather than as
> standalone questions. The concepts pay off continuously rather than in one
> place.
>
> While you are in the Mathematics section, confirm the exact page where the
> differential calculus subsection begins and add it to the personal page map
> you started in Chapter 00-03. The page span above is approximate; the
> section start at p. 36 is verified from the table of contents, but the
> subsection location is worth pinning down yourself.
>
> ---

---

## Where This Goes Wrong

**Confusing $\lim_{x\to a}f(x)$ with $f(a)$.** They are different questions
and frequently have different answers. A limit can exist where the function
value does not, and vice versa.

**Reporting $\frac{0}{0}$ as the answer.** It is never an answer. It is a
signal that direct substitution was inconclusive and algebra is required.
Answers of "$0$", "$1$", and "undefined" are all equally wrong when the
correct answer is a number you have not found yet.

**Treating $\frac{\text{nonzero}}{0}$ as indeterminate.** It is not. If the
numerator approaches a nonzero constant, the magnitude grows without bound.
Check the numerator *before* you start factoring — you may be doing algebra
you do not need.

**Cancelling and then worrying about it.** Cancelling $(x-a)$ inside
$\lim_{x\to a}$ is legitimate, because $x$ never equals $a$ during the limit
process. This is not sloppy algebra; it is the whole reason the technique
works. If you are uncomfortable with it, you have not internalized §16.1.

**Doing arithmetic with $\infty$.** $\infty - \infty$, $\frac{\infty}{\infty}$,
and $0 \cdot \infty$ are indeterminate forms, not zero and not one.
$\infty$ is a description of behaviour, not a quantity.

**Using degrees in the sine limit.** $\lim_{\theta\to 0}\frac{\sin\theta}
{\theta} = 1$ holds in **radians only**. In degrees the limit is
$\frac{\pi}{180} \approx 0.01745$. Every calculus formula involving trig
functions assumes radians.

**Forgetting to check both one-sided limits at a piecewise boundary.** The
whole question at a branch boundary is whether the two sides agree.
Evaluating only one branch answers half the question.

**Comparing the wrong degrees at infinity.** The rule compares the degree of
the numerator to the degree of the denominator, and in the equal case uses the
ratio of **leading coefficients**, not of constant terms or of all
coefficients.

**Applying the IVT without checking continuity.** A sign change across a
discontinuity brackets nothing. $f(x) = \frac{1}{x}$ has $f(-1) = -1$ and
$f(1) = +1$ — a sign change with no root anywhere, because $f$ is not
continuous on $[-1, 1]$.

**Expecting the IVT to locate the root or count roots.** It guarantees *at
least one* root exists somewhere in the interval. It does not say where, and
it does not say how many.

**Assuming a removable discontinuity is harmless in a model.** A hole in a
transfer function or a material property at exactly the operating point is a
real modelling problem even though the limit exists. It usually means the
model was derived by cancelling something that is physically meaningful.

---

## Key Terms

| Term | Definition |
|---|---|
| Limit | The value a function approaches as the input approaches a specified point |
| One-sided limit | The limit approaching from only the left ($a^-$) or only the right ($a^+$) |
| DNE | Does not exist; the correct answer when no limit value exists |
| Indeterminate form | An expression such as $0/0$ whose value is not determined by the form alone; requires further work |
| Direct substitution | Evaluating a limit by substituting the approach value; valid for polynomials and for rational functions with nonzero denominator |
| Rationalizing | Multiplying by a conjugate to remove a radical from a numerator or denominator |
| Limit at infinity | The value a function approaches as the input grows without bound |
| Horizontal asymptote | The line $y = L$ when $\lim_{x\to\pm\infty}f(x) = L$ |
| Vertical asymptote | The line $x = a$ when $f$ grows without bound near $a$ |
| Infinite limit | Description of unbounded growth; not a numerical limit value |
| Small-angle approximation | $\sin\theta \approx \theta$ for small $\theta$ in radians; consequence of the standard sine limit |
| Continuity at a point | $f(a)$ exists, the limit exists, and they are equal |
| Removable discontinuity | A hole; the limit exists but $f(a)$ is missing or mismatched; fixable by redefinition |
| Jump discontinuity | One-sided limits exist but differ; not removable |
| Infinite discontinuity | Function unbounded near the point; vertical asymptote; not removable |
| Intermediate Value Theorem | A continuous function on $[a,b]$ attains every value between $f(a)$ and $f(b)$ |
| Root bracketing | Using a sign change of a continuous function to guarantee a root lies in an interval |
| Difference quotient | $\dfrac{f(a+h)-f(a)}{h}$; its limit as $h \to 0$ defines the derivative (Chapter 01-17) |

---

## Review Questions

### Conceptual

1. Explain the difference between $\lim_{x\to 4}f(x)$ and $f(4)$. Give an
   example where the first exists and the second does not.
2. State the relationship between one-sided limits and the two-sided limit.
   Why is the two-sided limit the more demanding requirement?
3. List the three ways a limit can fail to exist and give a short example of
   each.
4. Explain why $\frac{0}{0}$ is called indeterminate. Give two functions that
   both produce $\frac{0}{0}$ at $x = 0$ but have different limits there.
5. Why is it legitimate to cancel the factor $(x-5)$ when evaluating
   $\lim_{x\to 5}\frac{(x-5)(x+2)}{(x-5)}$, even though that factor is zero at
   $x = 5$?
6. State the three conditions for continuity at a point. For each of the three
   discontinuity types, identify which condition fails.
7. Why must $\theta$ be in radians for $\lim_{\theta\to 0}
   \frac{\sin\theta}{\theta} = 1$? What is the limit if $\theta$ is in degrees?
8. State the Intermediate Value Theorem. Then explain why the function
   $f(x) = \frac{1}{x}$ on $[-1, 1]$ does not contradict it, despite having
   $f(-1) < 0 < f(1)$ and no root.
9. A removable discontinuity can be "fixed" by redefining one function value.
   Explain why a jump discontinuity cannot be fixed the same way.
10. In Chapter 01-15 you learned that an infinite geometric series converges
    when $\lvert r\rvert < 1$. Restate that condition as a statement about a
    limit, and explain how the limit produces the sum formula.

### Calculation

11. Evaluate by direct substitution:
    (a) $\displaystyle\lim_{x\to 2}\left(3x^2 - 5x + 4\right)$
    (b) $\displaystyle\lim_{x\to -1}\frac{x^2+3}{x-4}$
    (c) $\displaystyle\lim_{x\to 0}\left(e^x + \cos x\right)$

12. Evaluate by factoring:
    (a) $\displaystyle\lim_{x\to 4}\frac{x^2-16}{x-4}$
    (b) $\displaystyle\lim_{x\to -2}\frac{x^2+5x+6}{x^2-4}$
    (c) $\displaystyle\lim_{x\to 3}\frac{x^3-27}{x-3}$

13. Evaluate by rationalizing:
    (a) $\displaystyle\lim_{x\to 0}\frac{\sqrt{x+9}-3}{x}$
    (b) $\displaystyle\lim_{x\to 5}\frac{x-5}{\sqrt{x-1}-2}$

14. Evaluate by combining fractions:
    (a) $\displaystyle\lim_{h\to 0}\frac{\frac{1}{3+h}-\frac{1}{3}}{h}$
    (b) $\displaystyle\lim_{x\to 1}\left(\frac{1}{x-1} - \frac{2}{x^2-1}\right)$

15. Evaluate each limit as $x \to \infty$ and state the horizontal asymptote
    if one exists:
    (a) $\dfrac{7x^2 - 3x}{2x^2 + 5}$
    (b) $\dfrac{6x + 11}{x^3 - 2}$
    (c) $\dfrac{4x^3 + x}{9x^2 - 1}$
    (d) $\dfrac{\sqrt{9x^2 + 4}}{x}$ for $x > 0$
    (e) $5 + 12e^{-x}$

16. Evaluate the one-sided limits and state whether the two-sided limit
    exists:
    (a) $\displaystyle\lim_{x\to 3^-}\frac{2}{x-3}$ and
    $\displaystyle\lim_{x\to 3^+}\frac{2}{x-3}$
    (b) $\displaystyle\lim_{x\to 0^-}\frac{5}{x^2}$ and
    $\displaystyle\lim_{x\to 0^+}\frac{5}{x^2}$

17. Evaluate:
    (a) $\displaystyle\lim_{x\to 0}\frac{\sin 7x}{x}$
    (b) $\displaystyle\lim_{x\to 0}\frac{\sin 3x}{\sin 8x}$
    (c) $\displaystyle\lim_{\theta\to 0}\frac{\theta}{\tan\theta}$
    (d) $\displaystyle\lim_{\theta\to 0}\frac{1-\cos 2\theta}{\theta}$

18. For each function, find all discontinuities and classify each as
    removable, jump, or infinite:
    (a) $f(x) = \dfrac{x^2-1}{x-1}$
    (b) $f(x) = \dfrac{x+3}{x^2-x-6}$
    (c) $f(x) = \begin{cases} x+2, & x < 0 \\ x^2 - 1, & x \ge 0\end{cases}$

19. Find the value of $c$ that makes each function continuous everywhere:
    (a) $f(x) = \begin{cases} 2x + c, & x < 3 \\ x^2 - 4, & x \ge 3\end{cases}$
    (b) $f(x) = \begin{cases} \dfrac{x^2-25}{x-5}, & x \ne 5 \\[4pt] c, & x = 5\end{cases}$

20. Use the IVT to show each equation has a solution in the stated interval.
    State explicitly why the continuity hypothesis is satisfied.
    (a) $x^3 + x - 6 = 0$ on $[1, 2]$
    (b) $\cos x = x$ on $[0, 1]$ (radians)
    (c) $e^{-x} = x^2$ on $[0, 1]$

21. **Engineering application.** A tank's liquid level responds to a step
    inflow change as $h(t) = 4.5\left(1 - e^{-t/6.0}\right)$ m, with $t$ in
    minutes.
    (a) Find $\lim_{t\to\infty}h(t)$ and state its physical meaning.
    (b) Compute $h$ at $t = \tau$, $t = 3\tau$, and $t = 5\tau$, and express
    each as a percentage of the terminal level.
    (c) Explain why the terminal level is never exactly attained at any finite
    time, and why that does not matter operationally.

22. **Engineering application.** The efficiency of a heat exchanger design is
    modelled as

    $$\eta(A) = \frac{0.82A}{A + 3.4}$$

    where $A$ is the heat transfer area in m².

    (a) Find $\lim_{A\to\infty}\eta(A)$ and interpret it as a design limit.
    (b) At what area does the model reach 90% of that limiting efficiency?
    (c) Is $\eta$ continuous for all physically meaningful $A$ (that is,
    $A > 0$)? Where is the mathematical discontinuity, and why is it
    physically irrelevant?

23. **Engineering application.** A pipe-sizing calculation requires solving
    $f(D) = D^5 - 3.2D - 1.7 = 0$ for the diameter $D$ in metres, with
    $0.5 \le D \le 2.0$.
    (a) Evaluate $f$ at $D = 0.5$, $1.0$, $1.5$, and $2.0$.
    (b) Identify an interval of length 0.5 that brackets a root and justify
    with the IVT.
    (c) Bisect that interval once and state the new, narrower bracket.
    (d) How many more bisections are needed to locate $D$ within $\pm 0.01$ m?

### Multiple Choice

24. $\displaystyle\lim_{x\to 5}\frac{x^2-25}{x-5}$ equals:
    A) $0$
    B) $5$
    C) $10$
    D) Does not exist

25. $\displaystyle\lim_{x\to\infty}\frac{6x^2+2x-1}{3x^2-7}$ equals:
    A) $0$
    B) $2$
    C) $6$
    D) Does not exist

26. $\displaystyle\lim_{x\to\infty}\frac{5x+2}{x^3+1}$ equals:
    A) $0$
    B) $5$
    C) $\infty$
    D) Does not exist

27. $\displaystyle\lim_{\theta\to 0}\frac{\sin 4\theta}{2\theta}$ equals:
    A) $\dfrac{1}{2}$
    B) $1$
    C) $2$
    D) $4$

28. The function $f(x) = \dfrac{x-2}{x^2-4}$ has:
    A) A removable discontinuity at $x = 2$ and an infinite one at $x = -2$
    B) Infinite discontinuities at both $x = 2$ and $x = -2$
    C) A jump discontinuity at $x = 2$
    D) No discontinuities

29. Which condition is **not** required for $f$ to be continuous at $x = a$?
    A) $f(a)$ exists
    B) $\lim_{x\to a}f(x)$ exists
    C) $\lim_{x\to a}f(x) = f(a)$
    D) $f$ is defined on both sides of $a$ by the same formula

30. If $f$ is continuous on $[2, 6]$ with $f(2) = -4$ and $f(6) = 7$, the IVT
    guarantees:
    A) $f$ has exactly one root in $(2,6)$
    B) $f$ has at least one root in $(2,6)$
    C) $f$ is increasing on $(2,6)$
    D) $f(4) = 1.5$

31. The form $\frac{0}{0}$ indicates that:
    A) The limit equals 0
    B) The limit equals 1
    C) The limit does not exist
    D) Direct substitution is inconclusive; further work is required

32. $\displaystyle\lim_{x\to 0^+}\frac{-3}{x}$ equals:
    A) $0$
    B) $-3$
    C) $+\infty$
    D) $-\infty$

---

## Answer Key with Explanations

**1.** $f(4)$ is the function's **value at** $x = 4$;
$\lim_{x\to 4}f(x)$ is the value the function **approaches near** $x = 4$,
deliberately ignoring what happens at 4 itself.

Example where the limit exists but the value does not:
$f(x) = \frac{x^2-16}{x-4}$. At $x = 4$ this is $\frac{0}{0}$, so $f(4)$ does
not exist. But factoring gives $\frac{(x-4)(x+4)}{x-4} = x+4$ for $x \ne 4$,
so $\lim_{x\to 4}f(x) = 8$. (§16.1)

**2.** $\lim_{x\to a}f(x) = L$ if and only if
$\lim_{x\to a^-}f(x) = L$ **and** $\lim_{x\to a^+}f(x) = L$.

The two-sided limit is more demanding because it requires two separate
conditions to hold *and* to agree on the same value. Either one-sided limit
can exist on its own without the other; the two-sided limit needs both plus
their equality. (§16.2)

**3.**
- **Jump:** one-sided limits exist but differ. $f(x) = \frac{\lvert x\rvert}
  {x}$ at $x = 0$: left limit $-1$, right limit $+1$.
- **Unbounded:** the function grows past every finite value.
  $\frac{1}{(x-3)^2}$ at $x = 3$.
- **Oscillation:** the function never settles.
  $\sin\!\left(\frac{1}{x}\right)$ at $x = 0$. (§16.3)

**4.** Indeterminate means the form $\frac{0}{0}$ does not determine the
answer — the same form arises from functions with entirely different limits.
Two examples at $x = 0$:

$$\lim_{x\to 0}\frac{3x}{x} = 3 \qquad \lim_{x\to 0}\frac{x^2}{x} = 0$$

Both are $\frac{0}{0}$ on substitution; the limits are 3 and 0. A third,
$\lim_{x\to 0}\frac{x}{x^2}$, is unbounded. The form alone carries no
information. (§16.5)

**5.** Because the limit process never evaluates the function *at* $x = 5$. It
examines values of $x$ arbitrarily close to 5 but never equal to 5, so
$(x-5) \ne 0$ throughout, and dividing by it is legitimate at every point
being considered. The cancelled expression $x + 2$ agrees with the original
function everywhere except the single excluded point, and since the limit
ignores that point, both have the same limit. (§16.5)

**6.** Continuity at $a$ requires: (1) $f(a)$ exists, (2)
$\lim_{x\to a}f(x)$ exists, (3) they are equal.

- **Removable:** condition (2) holds; (1) or (3) fails. The limit exists but
  the value is missing or mismatched.
- **Jump:** condition (2) fails — the one-sided limits disagree. Condition (1)
  may hold.
- **Infinite:** conditions (1) and (2) both fail — the function is unbounded,
  so there is no value and no finite limit. (§16.9)

**7.** Because the result depends on the unit of angle measure. In radians the
arc length subtended by $\theta$ on a unit circle *is* $\theta$, and the
vertical segment $\sin\theta$ becomes indistinguishable from that arc as
$\theta$ shrinks — hence a ratio of 1.

In degrees, $\theta_{\text{deg}} = \frac{180}{\pi}\theta_{\text{rad}}$, so the
denominator is inflated by $\frac{180}{\pi}$ and

$$\lim_{\theta\to 0}\frac{\sin\theta^\circ}{\theta^\circ} = \frac{\pi}{180} \approx 0.01745$$

Every calculus formula involving trigonometric functions assumes radians for
exactly this reason. (§16.8)

**8.** **IVT:** if $f$ is continuous on $[a,b]$ and $N$ lies between $f(a)$ and
$f(b)$, then $f(c) = N$ for some $c \in (a,b)$.

No contradiction, because $f(x) = \frac{1}{x}$ is **not continuous on
$[-1,1]$** — it has an infinite discontinuity at $x = 0$, which lies inside
the interval. The IVT hypothesis fails, so its conclusion is not claimed. The
function jumps from $-\infty$ to $+\infty$ across the asymptote without
passing through zero. (§16.10)

**9.** A removable discontinuity has a single well-defined limit $L$ at the
point; setting $f(a) = L$ satisfies all three continuity conditions at once.

A jump discontinuity has **two different** one-sided limits. Whatever single
value you assign to $f(a)$, it can equal at most one of them, so condition (3)
fails on the other side. There is no value of $f(a)$ that satisfies both
approaches, because the failure is in condition (2) — the two-sided limit does
not exist at all, and no choice of function value can create one. (§16.9)

**10.** The convergence condition $\lvert r\rvert < 1$ is equivalent to

$$\lim_{n\to\infty}r^n = 0$$

The sum is *defined* as the limit of the partial sums:

$$S_\infty = \lim_{n\to\infty}\frac{a_1(1-r^n)}{1-r} = \frac{a_1(1 - 0)}{1-r} = \frac{a_1}{1-r}$$

The limit does the work: it is what allows the $r^n$ term to be replaced by 0,
producing the closed form. When $\lvert r\rvert \ge 1$ the limit
$\lim_{n\to\infty}r^n$ does not exist (or is unbounded), so no closed form
exists and the series diverges. (§16.11)

**11.**

(a) Polynomial — substitute: $3(4) - 5(2) + 4 = 12 - 10 + 4 = \boxed{6}$

(b) Denominator at $x = -1$ is $-5 \ne 0$, so substitute:
$\dfrac{1+3}{-1-4} = \dfrac{4}{-5} = \boxed{-0.8}$

(c) Both continuous at 0: $e^0 + \cos 0 = 1 + 1 = \boxed{2}$

**12.**

(a) $\dfrac{(x-4)(x+4)}{x-4} \to x+4 \to 4+4 = \boxed{8}$

(b) $\dfrac{(x+2)(x+3)}{(x+2)(x-2)} \to \dfrac{x+3}{x-2} \to
\dfrac{-2+3}{-2-2} = \dfrac{1}{-4} = \boxed{-0.25}$

(c) Difference of cubes: $x^3 - 27 = (x-3)(x^2+3x+9)$

$$\to x^2 + 3x + 9 \to 9 + 9 + 9 = \boxed{27}$$

**13.**

(a) Multiply by $\dfrac{\sqrt{x+9}+3}{\sqrt{x+9}+3}$:

$$\frac{(x+9)-9}{x\left(\sqrt{x+9}+3\right)} = \frac{1}{\sqrt{x+9}+3} \to \frac{1}{3+3} = \boxed{\frac{1}{6}}$$

(b) The radical is in the denominator, so multiply by
$\dfrac{\sqrt{x-1}+2}{\sqrt{x-1}+2}$:

$$\frac{(x-5)\left(\sqrt{x-1}+2\right)}{(x-1)-4} = \frac{(x-5)\left(\sqrt{x-1}+2\right)}{x-5} = \sqrt{x-1}+2$$

$$\to \sqrt{4}+2 = \boxed{4}$$

**14.**

(a) Numerator: $\dfrac{3 - (3+h)}{3(3+h)} = \dfrac{-h}{3(3+h)}$

Divide by $h$: $\dfrac{-1}{3(3+h)} \to \dfrac{-1}{9} = \boxed{-\dfrac{1}{9}}$

(b) Common denominator $x^2 - 1 = (x-1)(x+1)$:

$$\frac{1}{x-1} - \frac{2}{(x-1)(x+1)} = \frac{(x+1) - 2}{(x-1)(x+1)} = \frac{x-1}{(x-1)(x+1)} = \frac{1}{x+1}$$

$$\to \frac{1}{1+1} = \boxed{0.5}$$

**15.**

(a) Degrees equal (2 and 2): ratio of leading coefficients
$= \boxed{\dfrac{7}{2} = 3.5}$. Horizontal asymptote $y = 3.5$.

(b) Bottom-heavy (1 over 3): $\boxed{0}$. Horizontal asymptote $y = 0$.

(c) Top-heavy (3 over 2): grows without bound, $\boxed{\text{DNE}}$. No
horizontal asymptote.

(d) For $x > 0$, divide inside and out by $x$:

$$\frac{\sqrt{9x^2+4}}{x} = \sqrt{\frac{9x^2+4}{x^2}} = \sqrt{9 + \frac{4}{x^2}} \to \sqrt{9} = \boxed{3}$$

Horizontal asymptote $y = 3$.

(e) $e^{-x} \to 0$, so the limit is $5 + 12(0) = \boxed{5}$. Horizontal
asymptote $y = 5$.

**16.**

(a) From the left, $x - 3$ is a small **negative** number, so
$\frac{2}{x-3} \to \boxed{-\infty}$.

From the right, $x - 3$ is a small **positive** number, so
$\boxed{+\infty}$.

The two sides disagree, so the two-sided limit **does not exist**, not even as
$\pm\infty$.

(b) $x^2 > 0$ on both sides, so both one-sided limits are $\boxed{+\infty}$.

Both sides agree in behaviour, so we may write
$\lim_{x\to 0}\frac{5}{x^2} = +\infty$ as a description — though it is still
not a finite limit value.

**17.**

(a) $\dfrac{\sin 7x}{x} = 7\cdot\dfrac{\sin 7x}{7x} \to 7(1) = \boxed{7}$

(b) Force both arguments to match their denominators:

$$\frac{\sin 3x}{\sin 8x} = \frac{\frac{\sin 3x}{3x}\cdot 3x}{\frac{\sin 8x}{8x}\cdot 8x} \to \frac{(1)(3x)}{(1)(8x)} = \boxed{\frac{3}{8} = 0.375}$$

(c) $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$, so

$$\frac{\theta}{\tan\theta} = \frac{\theta\cos\theta}{\sin\theta} = \frac{\theta}{\sin\theta}\cdot\cos\theta \to (1)(1) = \boxed{1}$$

(using that $\frac{\theta}{\sin\theta}$ is the reciprocal of the standard
limit, hence also 1).

(d) Substitute $u = 2\theta$, so $\theta = u/2$ and $u \to 0$:

$$\frac{1-\cos 2\theta}{\theta} = \frac{1-\cos u}{u/2} = 2\cdot\frac{1-\cos u}{u} \to 2(0) = \boxed{0}$$

**18.**

(a) Denominator zero at $x = 1$. Factor:
$\frac{(x-1)(x+1)}{x-1} \to x+1$ for $x \ne 1$. The limit is 2 but $f(1)$ does
not exist.

$$\boxed{\text{Removable discontinuity at } x = 1 \text{ (hole at } (1,2))}$$

(b) $x^2 - x - 6 = (x-3)(x+2)$. Zeros at $x = 3$ and $x = -2$.

At $x = -2$: numerator is $-2+3 = 1 \ne 0$, so the form is
$\frac{1}{0}$ — determinate and unbounded. **Infinite discontinuity.**

At $x = 3$: numerator is $6 \ne 0$, so again $\frac{6}{0}$. **Infinite
discontinuity.**

$$\boxed{\text{Infinite discontinuities at } x = -2 \text{ and } x = 3}$$

(No factor cancels, so neither is removable — a common trap when the numerator
happens to look like one of the factors.)

(c) Check $x = 0$:

Left limit: $0 + 2 = 2$. Right limit: $0 - 1 = -1$. Value: $f(0) = -1$.

One-sided limits differ.

$$\boxed{\text{Jump discontinuity at } x = 0, \text{ jump size } 3}$$

**19.**

(a) Left limit: $2(3) + c = 6 + c$. Right limit and value:
$3^2 - 4 = 5$.

$$6 + c = 5 \implies \boxed{c = -1}$$

(b) For $x \ne 5$: $\frac{(x-5)(x+5)}{x-5} = x+5$, so
$\lim_{x\to 5}f(x) = 10$. Continuity requires $f(5) = 10$:

$$\boxed{c = 10}$$

**20.**

(a) $f(x) = x^3 + x - 6$ is a polynomial, hence continuous on $[1,2]$ —
the hypothesis holds automatically.

$f(1) = 1 + 1 - 6 = -4$; $f(2) = 8 + 2 - 6 = +4$.

Signs differ, so by the IVT there is a root in $(1,2)$ ✓

(b) $g(x) = \cos x - x$ is a difference of two functions continuous
everywhere, hence continuous on $[0,1]$.

$g(0) = 1 - 0 = +1$; $g(1) = \cos(1) - 1 = 0.5403 - 1 = -0.4597$.

Signs differ → a solution to $\cos x = x$ exists in $(0,1)$ ✓

(c) $h(x) = e^{-x} - x^2$ is continuous everywhere ($e^{-x}$ and $x^2$ both
are).

$h(0) = 1 - 0 = +1$; $h(1) = e^{-1} - 1 = 0.3679 - 1 = -0.6321$.

Signs differ → a solution exists in $(0,1)$ ✓

**21.**

Here $\tau = 6.0$ min and the terminal level coefficient is 4.5 m.

(a) $e^{-t/6} \to 0$ as $t \to \infty$:

$$\lim_{t\to\infty}h(t) = 4.5(1-0) = \boxed{4.5 \text{ m}}$$

This is the steady-state level — the depth at which inflow and outflow
balance. The tank approaches it asymptotically from below and never overshoots.

(b)

At $t = \tau = 6.0$ min: $h = 4.5(1 - e^{-1}) = 4.5(1 - 0.36788) =
4.5(0.63212) = 2.845$ m → $\boxed{63.2\%}$

At $t = 3\tau = 18.0$ min: $h = 4.5(1 - e^{-3}) = 4.5(1 - 0.049787) =
4.5(0.950213) = 4.276$ m → $\boxed{95.0\%}$

At $t = 5\tau = 30.0$ min: $h = 4.5(1 - e^{-5}) = 4.5(1 - 0.0067379) =
4.5(0.9932621) = 4.470$ m → $\boxed{99.3\%}$

(c) The factor $e^{-t/\tau}$ is strictly positive for every finite $t$ — an
exponential never actually reaches zero. So $h(t) < 4.5$ m always, and the
terminal level is a limit rather than an attained value.

Operationally it does not matter, because the remaining gap falls below any
measurement resolution long before it matters. At $5\tau$ the shortfall is
$4.5 - 4.470 = 0.030$ m = 30 mm; at $7\tau$ it is
$4.5(e^{-7}) = 4.1$ mm, below the resolution of most level instruments. This
is the reasoning behind the five-tau settling convention from Chapter 01-05.

**22.**

(a) Degrees equal (1 and 1), leading coefficients 0.82 and 1:

$$\lim_{A\to\infty}\frac{0.82A}{A+3.4} = \boxed{0.82}$$

Interpretation: 82% is the **ceiling** on efficiency for this design family.
No amount of added area gets past it — the model has a horizontal asymptote at
$\eta = 0.82$. Diminishing returns are built into the functional form, and
this is the number that tells you when to stop buying area.

(b) Require $\eta = 0.90(0.82) = 0.738$:

$$\frac{0.82A}{A+3.4} = 0.738$$

$$0.82A = 0.738A + 2.5092$$

$$0.082A = 2.5092 \implies A = \boxed{30.6 \text{ m}^2}$$

**Check.** $\eta(30.6) = \frac{0.82(30.6)}{30.6+3.4} = \frac{25.09}{34.0} =
0.738$ ✓ And $0.738/0.82 = 0.900$ ✓

**Design comment.** Reaching 90% of the ceiling takes 30.6 m². Reaching 95%
would require solving $\frac{0.82A}{A+3.4} = 0.779$, giving $A = 64.6$ m² —
more than double the area for five more percentage points. The limit tells you
the ceiling exists; the arithmetic tells you how expensive the last few
percent are.

(c) $\eta$ is a rational function, discontinuous only where the denominator
vanishes: $A + 3.4 = 0 \implies A = -3.4$ m².

That is an **infinite discontinuity** at $A = -3.4$ m², which lies outside the
physical domain — a negative heat transfer area is meaningless. On the
physically meaningful domain $A > 0$ the function is continuous everywhere.

$$\boxed{\text{Continuous for all } A > 0; \text{ discontinuity at } A = -3.4 \text{ m}^2 \text{ is non-physical}}$$

This is worth noticing as a general habit: always check whether a
mathematical discontinuity falls inside or outside the physical domain before
worrying about it.

**23.**

(a) $f(D) = D^5 - 3.2D - 1.7$

$f(0.5) = 0.03125 - 1.6 - 1.7 = -3.269$

$f(1.0) = 1 - 3.2 - 1.7 = -3.900$

$f(1.5) = 7.59375 - 4.8 - 1.7 = +1.094$

$f(2.0) = 32 - 6.4 - 1.7 = +23.900$

(b) $f$ is a polynomial, therefore continuous on $[1.0, 1.5]$ — the IVT
hypothesis is satisfied without further checking.

$f(1.0) = -3.900 < 0$ and $f(1.5) = +1.094 > 0$. Signs differ, so by the IVT
there is at least one root in $(1.0, 1.5)$.

$$\boxed{\text{Root bracketed in } (1.0,\, 1.5)}$$

(c) Midpoint $D = 1.25$:

$$f(1.25) = 1.25^5 - 3.2(1.25) - 1.7 = 3.05176 - 4.0 - 1.7 = -2.648$$

Negative, matching the sign at $D = 1.0$. The sign change is therefore in the
**upper** half:

$$\boxed{\text{New bracket } (1.25,\, 1.5), \text{ width } 0.25}$$

(d) Each bisection halves the bracket width. Starting from the current width
0.25, we need width $\le 2(0.01) = 0.02$ so that the midpoint is within
$\pm 0.01$ of the root.

$$0.25\left(\tfrac12\right)^n \le 0.02 \implies \left(\tfrac12\right)^n \le 0.08$$

Taking logs (Chapter 01-05), and noting $\ln(0.5) < 0$ so the inequality
reverses:

$$n \ge \frac{\ln 0.08}{\ln 0.5} = \frac{-2.5257}{-0.69315} = 3.644$$

$$\boxed{n = 4 \text{ more bisections}}$$

**Check.** After 4 bisections the width is $0.25/16 = 0.015625$, and half of
that is $0.0078 < 0.01$ ✓ After only 3 the width would be $0.03125$, half of
which is $0.0156 > 0.01$ ✗

**24. C — 10.** Factor: $\frac{(x-5)(x+5)}{x-5} \to x+5 \to 10$. Choice D is
the trap of stopping at $\frac{0}{0}$ and declaring failure. (§16.5)

**25. B — 2.** Degrees equal, so take the ratio of leading coefficients:
$\frac{6}{3} = 2$. Choice C uses only the numerator's leading coefficient.
(§16.6)

**26. A — 0.** Bottom-heavy: degree 1 over degree 3. Choice B uses the
leading coefficient as though the degrees were equal. (§16.6)

**27. C — 2.** $\frac{\sin 4\theta}{2\theta} = \frac{4}{2}\cdot
\frac{\sin 4\theta}{4\theta} \to 2(1) = 2$. Choice D forgets the 2 in the
denominator; choice A inverts the ratio. (§16.8)

**28. A.** Factor the denominator: $x^2 - 4 = (x-2)(x+2)$.

$$\frac{x-2}{(x-2)(x+2)} = \frac{1}{x+2} \quad (x \ne 2)$$

At $x = 2$ the factor cancels, the limit is $\frac{1}{4}$, and the
discontinuity is **removable**. At $x = -2$ nothing cancels, the form is
$\frac{-4}{0}$, and the discontinuity is **infinite**. (§16.9)

**29. D.** A function can perfectly well be continuous at a point where the
definition changes formula — Worked Example 8 with $k = 1$ is exactly such a
case. The requirement is that the two formulas *agree in the limit*, not that
there be only one formula. Choices A, B, and C are the three genuine
conditions. (§16.9)

**30. B — at least one root in $(2,6)$.** The IVT guarantees existence, not
uniqueness, so A is too strong. C does not follow — the function could
oscillate. D assumes linearity, which is not given. (§16.10)

**31. D — Direct substitution is inconclusive; further work is required.**
That is the entire meaning of "indeterminate." All of A, B, and C are possible
*outcomes* after doing the algebra, but none is implied by the form itself.
(§16.5)

**32. D — $-\infty$.** Approaching 0 from the right, $x$ is a small positive
number, so $\frac{-3}{x}$ is a large **negative** number. Choice C is the sign
error. (§16.7)

---

## Quick Reference

**Definition and one-sided limits** — *not in the Handbook; memorize*

$$\lim_{x\to a}f(x) = L \iff \lim_{x\to a^-}f(x) = \lim_{x\to a^+}f(x) = L$$

The limit ignores $f(a)$ entirely.

**Failure modes:** one-sided limits disagree · unbounded · oscillates

**Limit laws** (valid when the individual limits exist)

Sum, difference, product, power, root: distribute freely.

Quotient: $\displaystyle\lim\frac{f}{g} = \frac{L}{M}$ **only if** $M \ne 0$.

**Evaluation order**

1. Try **direct substitution.** Polynomials always work; rational functions
   work if the denominator is nonzero.
2. If $\frac{\text{nonzero}}{0}$: **determinate**, unbounded, vertical
   asymptote. Check one-sided signs.
3. If $\frac{0}{0}$: **indeterminate.** Factor, rationalize, or combine
   fractions, then re-substitute.

**Limits at infinity**

$$\lim_{x\to\infty}\frac{1}{x^n} = 0 \;(n>0) \qquad \lim_{x\to\infty}e^{-x} = 0$$

Rational function $\frac{p}{q}$ with $\deg p = m$, $\deg q = n$:

| Case | Limit |
|---|---|
| $m < n$ | $0$ |
| $m = n$ | ratio of leading coefficients |
| $m > n$ | unbounded, DNE |

**Special trig limits — radians only**

$$\lim_{\theta\to 0}\frac{\sin\theta}{\theta} = 1 \qquad \lim_{\theta\to 0}\frac{1-\cos\theta}{\theta} = 0$$

Small-angle approximation: $\sin\theta \approx \theta$

For $\frac{\sin kx}{mx}$: force the argument to match, giving $\frac{k}{m}$.

**Continuity at $x = a$** — all three required

$$f(a) \text{ exists} \quad\wedge\quad \lim_{x\to a}f(x) \text{ exists} \quad\wedge\quad \lim_{x\to a}f(x) = f(a)$$

| Discontinuity | Signature | Removable? |
|---|---|---|
| Removable | limit exists, value missing or mismatched | yes |
| Jump | one-sided limits differ | no |
| Infinite | unbounded near $a$ | no |

**Intermediate Value Theorem**

$f$ continuous on $[a,b]$ ⟹ $f$ attains every value between $f(a)$ and $f(b)$.

**Root bracketing:** continuous $f$ with $f(a)f(b) < 0$ ⟹ at least one root in
$(a,b)$.

Guarantees existence only — not uniqueness, not location.

**Bisection width after $n$ steps:** $w_n = w_0\left(\frac12\right)^n$

**Almost nothing here is in the Handbook.** Memorize all of the above. The
Handbook supplies L'Hôpital's rule (Chapter 01-18) and the limit definition
of the derivative (Chapter 01-17), nothing more.

---

## What's Next

Apprentice, you have the concept that makes calculus possible. A limit lets
you ask what a quantity is approaching without ever requiring it to arrive,
and that sidestep is what lets us divide by an interval that shrinks to
nothing.

In **Chapter 01-17: Derivatives and Differentiation Rules**, we cash it in.
The derivative is the limit of the difference quotient — exactly the structure
of Worked Example 4 in this chapter — and it measures instantaneous rate of
change. Slope of a curve. Velocity from position. Shear from load. Current
from charge. Every one of those is a derivative, and every derivative rule
you will learn was obtained by resolving a $\frac{0}{0}$ form with the
techniques you just practised.

One habit to carry forward: when a derivative rule looks arbitrary, ask what
limit produced it. The answer is always there, and it is always a
cancellation you now know how to do.

Bring the Handbook to the Mathematics section, differential calculus. The
derivative table is where you will be living for the next three chapters.

See you there.

— Your Mentor
