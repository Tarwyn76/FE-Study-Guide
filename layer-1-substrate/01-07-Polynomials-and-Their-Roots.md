---
chapter: "01-07"
title: "Polynomials and Their Roots"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-007-01, MATH-1B-007-02, MATH-1B-007-03]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-07: Polynomials and Their Roots

> *"Every time you ask 'at what load does this beam fail?' or 'at what
> frequency does this circuit resonate?' or 'what dimensions minimize
> material cost?', you're asking: where does this polynomial equal zero?
> The roots of polynomials are where the interesting things happen."*

---

## Before You Start

**Prerequisites:** [01-04 Expressions, Equations, and Inequalities](01-04-expressions-equations-inequalities.md) · [01-05 Exponents, Radicals, and Logarithms](01-05-exponents-radicals-logarithms.md) · [01-06 Functions, Graphs, and Transformations](01-06-functions-graphs-transformations.md)

**Skip if:** You pass the Tier 1B test-out quiz. Verify you can apply the
quadratic formula correctly including to equations with complex roots, and
that you understand what the discriminant tells you before skipping.

**Time:** ~55 min read · ~25 min review questions · ~55 min practice problems

---

## On the Board Today

Apprentice, polynomials are the workhorse of algebraic modeling.

They're not exotic. A polynomial is anything of the form:

$$a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0$$

A quadratic equation for a projectile's height. A cubic that describes beam
deflection under load. A fourth-degree polynomial for the natural frequencies
of a two-degree-of-freedom vibrating system. You've been solving polynomials
since middle school; this chapter gives you the complete toolkit.

Two things need serious attention.

**The discriminant.** The quadratic formula always gives an answer. What that
answer means depends on the discriminant $b^2 - 4ac$. When it's negative,
the roots are complex — not an error, but real information about the system's
behavior. A control engineer looking at the characteristic equation of a
system wants complex roots because they indicate oscillation. An error in
the quadratic formula is much more likely to produce a wrong real number than
a wrong complex one, so knowing what kind of answer to expect is your first
check.

**The connection between roots and factors.** If $r$ is a root, then
$(x - r)$ is a factor. Always. That connection — stated as the factor theorem
— is the bridge between the algebraic tool (factoring) and the geometric tool
(finding zeros of the graph), and it's used constantly in partial fractions,
Laplace transforms, and transfer function analysis.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 7.1 Define polynomial, degree, leading coefficient, and identify each in
  a given expression
* 7.2 Perform polynomial addition, subtraction, and multiplication
* 7.3 Perform polynomial long division and synthetic division
* 7.4 Apply the remainder theorem and factor theorem
* 7.5 Solve quadratic equations by factoring, completing the square, and
  the quadratic formula
* 7.6 Interpret the discriminant and predict the nature of quadratic roots
* 7.7 Apply the rational root theorem and Descartes' rule of signs to narrow
  the search for real roots of higher-degree polynomials
* 7.8 Solve polynomial equations by combining root-finding strategies
* 7.9 Recognize the connection between roots, factors, and graph zeros

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $P(x)$ | polynomial in variable $x$ | — |
| $n$ | degree of the polynomial | highest power of $x$ |
| $a_n$ | leading coefficient | coefficient of $x^n$ |
| $a_0$ | constant term | value when $x = 0$ |
| $r$ | root (zero) of $P(x)$ | value where $P(r) = 0$ |
| $\Delta$ | discriminant, $b^2 - 4ac$ | determines root type |
| $i$ | imaginary unit, $i^2 = -1$ | complex roots in §7.5 |

> ---
> **Mentor's Margin**
>
> We've used $j$ as the imaginary unit since Chapter 01-12, matching the
> Handbook's convention for electrical engineering. In mathematics and
> physics, $i$ is standard. Polynomials are a math topic, so this chapter
> uses $i$ consistent with the Handbook's Mathematics section. When we
> reach AC circuits in Chapter 02-63, we switch back to $j$. The symbol is
> different; the mathematics is identical.
>
> ---

---

## 7.1 Polynomial Fundamentals

A **polynomial** in $x$ is an expression of the form:

$$P(x) = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0$$

where:
- $n$ is a non-negative integer (the **degree**)
- $a_n, a_{n-1}, \ldots, a_0$ are real (or complex) constants (the
  **coefficients**)
- $a_n \ne 0$ (the **leading coefficient**)

| Name | Degree | General form |
|---|---|---|
| Constant | 0 | $a_0$ |
| Linear | 1 | $ax + b$ |
| Quadratic | 2 | $ax^2 + bx + c$ |
| Cubic | 3 | $ax^3 + bx^2 + cx + d$ |
| Quartic | 4 | $ax^4 + \cdots$ |

### What makes something a polynomial (and what doesn't)

- Variable exponents must be non-negative integers: $x^{1/2}$,
  $x^{-1}$ are not polynomial terms
- No variables in denominators: $1/(x+1)$ is not a polynomial (it's a
  rational function)
- No variables inside radicals or logarithms as the primary operation

### The fundamental theorem of algebra

> **A polynomial of degree $n$ has exactly $n$ roots**, counting multiplicity
> and including complex roots.

This is a statement about what exists, not about what's easy to find. A
quadratic has 2 roots (both might be equal, or both might be complex). A
cubic has 3 roots. A degree-$n$ polynomial has $n$ roots.

---

## 7.2 Polynomial Arithmetic

**Addition and subtraction:** combine like terms.

$$(3x^3 - 2x + 5) + (x^3 + 4x^2 - 3x - 1) = 4x^3 + 4x^2 - 5x + 4$$

**Multiplication:** distribute each term of one polynomial across every term
of the other.

$$(x^2 + 2)(x - 3) = x^3 - 3x^2 + 2x - 6$$

For higher-degree products, organize by collecting like terms after full
distribution.

---

## 7.3 Polynomial Division

### Long division

Same procedure as integer long division. Works for any polynomial divisor.

**Worked Example 1 — Polynomial Long Division**

**Given.** Divide $P(x) = 2x^3 - 3x^2 + x - 5$ by $D(x) = x - 2$.

**Solution.**

$$\begin{array}{r} 2x^2 + x + 3 \\ x-2 \;\overline{)\; 2x^3 - 3x^2 + x - 5} \\ \underline{2x^3 - 4x^2} \phantom{+ x - 5} \\ x^2 + x \phantom{-5} \\ \underline{x^2 - 2x}\phantom{-5} \\ 3x - 5 \\ \underline{3x - 6} \\ 1 \end{array}$$

Result: $Q(x) = 2x^2 + x + 3$ with remainder $R = 1$.

$$P(x) = (x-2)(2x^2 + x + 3) + 1$$

**Check:** $P(2) = (2-2)(2^2 \cdot 2 + 2 + 3) + 1 = 0 + 1 = 1$.
Direct: $P(2) = 16 - 12 + 2 - 5 = 1$. ✓

### The remainder theorem

> When $P(x)$ is divided by $(x - r)$, the remainder equals $P(r)$.

This is what the check above just demonstrated: the remainder from dividing
by $(x - 2)$ equals $P(2) = 1$.

**Consequence:** If $P(r) = 0$, the remainder is zero, meaning $(x - r)$
divides $P(x)$ exactly. This is the **factor theorem**:

> $(x - r)$ is a factor of $P(x)$ if and only if $P(r) = 0$.

### Synthetic division

A shorthand for dividing by a linear factor $(x - r)$. Write the
coefficients of $P(x)$ in a row, and use $r$ as the divisor.

**Worked Example 2 — Synthetic Division**

**Given.** Divide $P(x) = 3x^4 - 2x^3 + 0 \cdot x^2 + x - 7$ by $(x + 1)$,
i.e., $r = -1$.

Write coefficients: $3, -2, 0, 1, -7$.

$$\begin{array}{c|ccccc} -1 & 3 & -2 & 0 & 1 & -7 \\ & & -3 & 5 & -5 & 4 \\ \hline & 3 & -5 & 5 & -4 & -3 \end{array}$$

Process: bring down 3. Multiply $3 \times (-1) = -3$, write under $-2$. Add:
$-2 + (-3) = -5$. Multiply $-5 \times (-1) = 5$, write under 0. Add:
$0 + 5 = 5$. Continue.

Result: $Q(x) = 3x^3 - 5x^2 + 5x - 4$, remainder $= -3$.

**Check:** $P(-1) = 3(1) - 2(-1) + 0 + (-1) - 7 = 3 + 2 - 1 - 7 = -3$ ✓

> ---
> **Mentor's Margin**
>
> Synthetic division only works when the divisor is a **linear factor**
> $(x - r)$. For any other divisor, use long division. The error I see is
> people applying synthetic division to divide by $x^2 + 1$ or $2x - 3$.
> The first is quadratic — use long division. The second is $2(x - 3/2)$;
> synthetic division with $r = 3/2$ works but then divide the quotient by
> 2 at the end.
>
> ---

---

## 7.4 The Quadratic Equation

A quadratic is any equation of the form:

$$ax^2 + bx + c = 0, \quad a \ne 0$$

Three methods to find roots: factoring (fastest when it works), completing
the square (always works, builds understanding), and the quadratic formula
(always works, most practical).

### Method 1 — Factoring

Find two numbers multiplying to $ac$ and adding to $b$, then split the
middle term.

$$2x^2 + 5x - 3 = 0$$

$ac = -6$. Numbers: $6$ and $-1$ (multiply to $-6$, add to $5$).

$$2x^2 + 6x - x - 3 = 2x(x+3) - 1(x+3) = (2x-1)(x+3) = 0$$

$$x = \frac{1}{2} \quad\text{or}\quad x = -3$$

### Method 2 — Completing the square

Rewrite the quadratic as a perfect square trinomial plus a constant.

$$x^2 + 6x + 5 = 0$$
$$x^2 + 6x = -5$$
$$x^2 + 6x + 9 = -5 + 9 = 4$$
$$(x + 3)^2 = 4$$
$$x + 3 = \pm 2$$
$$x = -1 \quad\text{or}\quad x = -5$$

The key step: take half the coefficient of $x$ (here, $6/2 = 3$), square it
($9$), and add it to both sides.

> ---
> **Mentor's Margin**
>
> Completing the square is worth doing at least twice by hand even if you
> plan to use the quadratic formula thereafter. It's how the quadratic
> formula is derived, and understanding the derivation means you can recover
> the formula if you blank on it during the exam. More practically,
> completing the square is the technique for converting conic section
> equations to standard form (Chapter 01-09) and for solving certain
> integrals (Chapter 01-21). It earns its keep beyond the quadratic.
>
> ---

### Method 3 — The quadratic formula

Derived by completing the square on the general form $ax^2 + bx + c = 0$:

$$\boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}$$

This always works. The only judgment is reading the formula correctly,
particularly the $\pm$ and the placement of $2a$.

> ---
> **Mentor's Margin**
>
> Two common formula errors. First: only partially taking the $\pm$ — writing
> $-b \pm \sqrt{D} / 2a$ instead of $(-b \pm \sqrt{D}) / 2a$. The entire
> numerator is under the denominator. Second: forgetting to compute $2a$ and
> writing $2$ as the denominator when $a \ne 1$. Both produce wrong answers
> that look syntactically reasonable. Write the formula out once with explicit
> parentheses before substituting.
>
> ---

### The discriminant

$$\Delta = b^2 - 4ac$$

Before computing the roots, evaluate the discriminant. It tells you what
kind of answer you'll get.

| $\Delta$ | Nature of roots | Graph behavior |
|---|---|---|
| $\Delta > 0$ | Two distinct real roots | Parabola crosses $x$-axis twice |
| $\Delta = 0$ | One repeated real root (double root) | Parabola tangent to $x$-axis |
| $\Delta < 0$ | Two complex conjugate roots | Parabola doesn't cross $x$-axis |

Complex conjugate roots come in pairs: if $p + qi$ is a root, then $p - qi$
is also a root. Their complex nature is not a sign of an error — it reflects
real physical behavior in systems governed by the equation.

### Worked Example 3 — The Quadratic Formula and Discriminant

**Given.** Solve each quadratic and interpret the discriminant:

(a) $x^2 - 5x + 4 = 0$
(b) $x^2 - 4x + 4 = 0$
(c) $x^2 - 2x + 5 = 0$

**Solution.**

**(a)** $\Delta = 25 - 16 = 9 > 0$. Two real roots.

$$x = \frac{5 \pm \sqrt{9}}{2} = \frac{5 \pm 3}{2} \implies x = 4 \text{ or } x = 1$$

Check by factoring: $(x-4)(x-1) = 0$. ✓

**(b)** $\Delta = 16 - 16 = 0$. One repeated root.

$$x = \frac{4 \pm 0}{2} = 2$$

Double root at $x = 2$. Check: $(x-2)^2 = x^2 - 4x + 4$. ✓

**(c)** $\Delta = 4 - 20 = -16 < 0$. Two complex conjugate roots.

$$x = \frac{2 \pm \sqrt{-16}}{2} = \frac{2 \pm 4i}{2} = 1 \pm 2i$$

Roots: $x = 1 + 2i$ and $x = 1 - 2i$.

**Check:** $(1+2i)^2 - 2(1+2i) + 5 = 1 + 4i - 4 - 2 - 4i + 5 = 0$. ✓

**Physical note on (c):** A quadratic characteristic equation with complex
roots $p \pm qi$ indicates that the system it models undergoes oscillation
at angular frequency $q$ with envelope growth/decay rate $p$. If $p < 0$,
oscillations decay — the system is stable. We'll see this in Chapter 02-33
(vibrations) and Chapter 02-69 (control systems). The complex roots are telling you something true about
the physics, not indicating a calculation error.

---

## 7.5 Vieta's Formulas — Roots Without Solving

For a quadratic $ax^2 + bx + c = 0$ with roots $r_1$ and $r_2$:

$$\boxed{r_1 + r_2 = -\frac{b}{a}} \qquad \boxed{r_1 \cdot r_2 = \frac{c}{a}}$$

These are **Vieta's formulas**. They let you check roots without substituting,
build a polynomial from its roots, or find one root given the other.

For a cubic $ax^3 + bx^2 + cx + d = 0$ with roots $r_1, r_2, r_3$:

$$r_1 + r_2 + r_3 = -\frac{b}{a} \qquad r_1 r_2 + r_1 r_3 + r_2 r_3 = \frac{c}{a} \qquad r_1 r_2 r_3 = -\frac{d}{a}$$

The pattern generalizes: the sum of all roots is $-a_{n-1}/a_n$; the
product of all roots is $(-1)^n a_0/a_n$.

### Worked Example 4 — Using Vieta's

**Given.** A quadratic equation $3x^2 + kx - 12 = 0$ has one root $r_1 = 4$.
Find $k$ and the other root $r_2$.

**Solution.**

Product of roots: $r_1 \cdot r_2 = c/a = -12/3 = -4$.

$$4 \cdot r_2 = -4 \implies r_2 = -1$$

Sum of roots: $r_1 + r_2 = -b/a = -k/3$.

$$4 + (-1) = 3 = -k/3 \implies k = -9$$

**Verify:** $3x^2 - 9x - 12 = 3(x^2 - 3x - 4) = 3(x-4)(x+1) = 0$.
Roots are $4$ and $-1$. ✓

---

## 7.6 Narrowing the Search — Rational Roots and Descartes' Rule

For a quadratic you have a formula. Above degree 2 there is no formula worth
using, and the practical method is: guess a root, verify it, divide it out,
and repeat until what's left is a quadratic.

That works only if the guessing is cheap. Two theorems make it cheap. Neither
one finds a root. Both of them shrink the search before you test anything —
the first by limiting *which* numbers are worth trying, the second by telling
you *how many* roots of each sign exist, so you know when to stop trying.

### The rational root theorem

For a polynomial with **integer** coefficients:

$$P(x) = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0$$

any rational root $p/q$ (in lowest terms) must satisfy:

- $p$ is a factor of $a_0$ (the constant term)
- $q$ is a factor of $a_n$ (the leading coefficient)

So the candidates are every ratio of a factor of $a_0$ to a factor of $a_n$,
taken with both signs. That turns an infinite search into a finite list.

Two limits worth stating plainly. The theorem applies only to **integer**
coefficients — clear fractions first if you have them. And it finds only
**rational** roots. A polynomial can have perfectly good irrational roots
like $2 \pm 2\sqrt{5}$, and no entry on the candidate list will ever produce
them. When every candidate fails, that is the likely reason.

### Descartes' rule of signs

> Write $P(x)$ in descending powers. Then:
>
> - The number of **positive** real roots is the number of sign changes in
>   the coefficients of $P(x)$, **or less than that by an even number**.
> - The number of **negative** real roots is the number of sign changes in
>   the coefficients of $P(-x)$, **or less than that by an even number**.
>
> Both counts include multiplicity.

A **sign change** is any place where consecutive nonzero coefficients differ
in sign. Skip zero coefficients entirely — they neither create nor block a
change.

To build $P(-x)$ you do not need to substitute and expand. Substituting $-x$
negates the odd-power terms and leaves the even-power terms alone, so:

> **Flip the sign of every odd-degree term. Leave the rest.**

Take $P(x) = 2x^3 - x^2 - 7x + 6$, the polynomial from Worked Example 5.

**Positive roots.** Coefficient signs: $+\;-\;-\;+$

$$\underbrace{+ \rightarrow -}_{\text{change 1}} \qquad - \rightarrow - \qquad \underbrace{- \rightarrow +}_{\text{change 2}}$$

Two sign changes, so **2 or 0** positive real roots.

**Negative roots.** Flip the odd-degree terms — the $x^3$ and $x$ terms —
giving $P(-x) = -2x^3 - x^2 + 7x + 6$. Signs: $-\;-\;+\;+$

$$- \rightarrow - \qquad \underbrace{- \rightarrow +}_{\text{change 1}} \qquad + \rightarrow +$$

One sign change, so **exactly 1** negative real root.

### Why "less by an even number"

This clause looks like hedging. It is not — it is the conjugate-pair rule
from §7.4 showing up again.

The degree fixes the total number of roots. Every root is positive real,
negative real, zero, or complex. Complex roots for a real-coefficient
polynomial arrive strictly **in pairs**. So if the actual count of positive
roots falls short of the sign-change count, the missing roots have become
complex, and they can only go missing two at a time.

For $2x^3 - x^2 - 7x + 6$ that gives exactly two possibilities:

| Positive | Negative | Complex | Total |
|---|---|---|---|
| 2 | 1 | 0 | 3 ✓ |
| 0 | 1 | 2 | 3 ✓ |

Nothing else fits degree 3.

![FIG-01-07-010: Upper half: two rows for P(x) = 2x³ − x² − 7x + 6. Top row shows the four coefficients 2, −1, −7, 6 in cells with their signs enlarged beneath as + − − +, and curved arcs above each adjacent pair; the two arcs spanning a sign change are solid and numbered 1 and 2, the arc spanning − to − is dashed and struck through, with the tally '2 changes → 2 or 0 positive roots'. Second row shows P(−x) built by the shortcut, with the odd-degree terms 2x³ and −7x circled and labelled 'flip these' and the even-degree terms labelled 'leave these', producing −2x³ − x² + 7x + 6 with signs − − + + and one solid numbered arc, tally '1 change → exactly 1 negative root'. Lower half: a possibility ledger with columns positive, negative, complex, total, containing the two admissible rows 2-1-0-3 and 0-1-2-3, each totalling the degree 3, with a note reading 'complex roots leave in pairs, which is why the count drops by an even number'. A footer strip reads 'counts of 0 and 1 are exact — you cannot subtract 2 from either'.](../figures/FIG-01-07-010-descartes-sign-counting.png)

Notice which counts are ambiguous and which are not. A count of 2 could be
2 or 0. A count of 3 could be 3 or 1. But **0 and 1 are exact** — you cannot
subtract 2 from either and get a sensible number of roots. Those are the
cases where Descartes hands you certainty rather than a range, and they are
common.

> ---
> **Mentor's Margin**
>
> Three ways this goes wrong.
>
> **Descending order is mandatory.** The rule counts sign changes along the
> powers in order. Shuffle the terms and you get a meaningless number. Write
> the polynomial out properly before counting.
>
> **Only odd-degree terms flip.** Building $P(-x)$ by negating every
> coefficient is the standard error, and it produces a sign-change count that
> is wrong in a way nothing downstream will catch.
>
> **Zero is not counted.** Descartes classifies roots as positive or
> negative, and $x = 0$ is neither. If $a_0 = 0$, factor out the highest
> power of $x$ first — that hands you the zero roots directly and leaves a
> lower-degree polynomial with a nonzero constant term for the rule to work
> on.
>
> ---

### One more illustration

Take $P(x) = x^3 + x^2 + x + 1$.

Signs are $+\;+\;+\;+$ — no changes at all, so **0** positive real roots,
exactly. That much you could have seen directly: every term is positive when
$x > 0$.

Flipping odd-degree terms gives $P(-x) = -x^3 + x^2 - x + 1$, with signs
$-\;+\;-\;+$ — three changes, so **3 or 1** negative real roots.

The polynomial factors as $(x+1)(x^2+1)$, with roots $-1$, $+i$, and $-i$.
One negative real root, two complex. The count came in at 1 rather than 3,
short by exactly 2, and the conjugate pair is where those two went.

### The combined search strategy

Run these in order. Each step makes the next one cheaper.

1. **Factor out any power of $x$.** This extracts the zero roots and lowers
   the degree.
2. **Apply Descartes to $P(x)$ and $P(-x)$.** This is your budget: how many
   positive roots to look for, and how many negative.
3. **Apply the rational root theorem.** This is your candidate list.
4. **Test candidates, simplest first** — whole numbers before fractions.
   Stop testing a sign as soon as its budget is spent.
5. **Divide out each root found** by synthetic division. The degree drops by
   one; re-run Descartes on the reduced polynomial if it helps.
6. **Stop at a quadratic** and use the formula for the last two roots.

![FIG-01-07-006: Worked for P(x) = 2x³ − x² − 7x + 6. Step 1 box: 'factor out any power of x — extracts zero roots', tagged 'a₀ = 6 ≠ 0, nothing to remove'. Step 2 box headed 'Descartes — the budget' splits into two side-by-side cells: one showing the signs of P(x) as + − − + with two change arcs marked and the conclusion '2 or 0 positive', the other showing the signs of P(−x) as − − + + with one change arc and the conclusion 'exactly 1 negative'. Step 3 box headed 'rational root theorem — the candidate list' shows factors of a₀ = 6 as ±1, ±2, ±3, ±6 above factors of a_n = 2 as ±1, ±2, resolving to the twelve candidates ±1, ±2, ±3, ±6, ±1/2, ±3/2. Step 4 box 'test simplest first' with x = 1 highlighted and P(1) = 0 shown, carrying a side note 'stop testing a sign once its budget is spent'. Step 5 box 'divide out by synthetic division, degree drops by one' loops back to step 4 with the note 're-run Descartes on the reduced polynomial if it helps'. An exit arrow leads to a final box 'stop at a quadratic — use the formula'. A footer strip reads 'the rational root theorem says which numbers to try; Descartes says when to stop trying'.](../figures/FIG-01-07-006-combined-root-search.png)

Step 4 is where Descartes pays. The rational root theorem gives you a list
but no stopping rule, so without Descartes you test until the list is
exhausted. With it, you often stop halfway.

### Worked Example 5 — The Full Search

**Given.** Find all real roots of $P(x) = 2x^3 - x^2 - 7x + 6$.

**Solution.**

**Step 1 — Zero roots.** $a_0 = 6 \ne 0$, so $x = 0$ is not a root. Nothing
to factor out.

**Step 2 — Descartes.** From the counting above: **2 or 0** positive real
roots, and **exactly 1** negative real root.

**Step 3 — Candidates.**

Factors of $a_0 = 6$: $\pm 1, \pm 2, \pm 3, \pm 6$.
Factors of $a_n = 2$: $\pm 1, \pm 2$.

Candidates: $\pm 1, \pm 2, \pm 3, \pm 6, \pm\frac{1}{2}, \pm\frac{3}{2}$ —
twelve in all, six positive and six negative.

**Step 4 — Test, positives first.**

$$P(1) = 2 - 1 - 7 + 6 = 0 \;\checkmark$$

Found on the first try. So $(x - 1)$ is a factor, and one of the two
possible positive roots is accounted for.

**Step 5 — Divide it out.**

$$\begin{array}{c|cccc} 1 & 2 & -1 & -7 & 6 \\ & & 2 & 1 & -6 \\ \hline & 2 & 1 & -6 & 0 \end{array}$$

$$P(x) = (x-1)\left(2x^2 + x - 6\right)$$

**Step 6 — Stop at the quadratic.** The remainder is a quadratic, so the
search is over. Factor it: two numbers multiplying to $2 \times (-6) = -12$
and adding to $1$ are $4$ and $-3$.

$$2x^2 + 4x - 3x - 6 = 2x(x+2) - 3(x+2) = (2x-3)(x+2)$$

$$P(x) = (x-1)(2x-3)(x+2)$$

$$\boxed{x = 1, \quad x = \frac{3}{2}, \quad x = -2}$$

**Check against Descartes.** Two positive roots ($1$ and $\frac{3}{2}$) and
one negative root ($-2$). The prediction allowed 2 or 0 positive and exactly
1 negative; the result is the first of the two permitted cases ✓ Had the
count come out as one positive and two negative, that would be a
contradiction and a signal to recheck the arithmetic.

**Check with Vieta's.**

Sum: $1 + \frac{3}{2} + (-2) = \frac{1}{2}$, and $-b/a = -(-1)/2 = \frac{1}{2}$ ✓

Product: $1 \times \frac{3}{2} \times (-2) = -3$, and $-d/a = -6/2 = -3$ ✓

**What the two theorems saved.** Twelve candidates, one substitution. The
rational root theorem reduced an unbounded search to twelve numbers, and
reaching a quadratic after a single successful division ended the search
before any of the remaining eleven had to be tried. On a polynomial where the
first guess misses, Descartes does more visible work: knowing that only one
negative root exists means that once you find it, the five remaining negative
candidates can be dropped without testing.

---

## 7.7 Polynomial Graphs and Root Multiplicity

The **multiplicity** of a root tells you how many times that root appears
(how many times the corresponding factor divides the polynomial).

| Multiplicity | Behavior at the root | Graph crosses or touches? |
|---|---|---|
| Odd (1, 3, 5, …) | Sign of $P(x)$ changes | **Crosses** the $x$-axis |
| Even (2, 4, 6, …) | Sign of $P(x)$ doesn't change | **Touches** and bounces off |

Examples:
- $P(x) = (x-2)$ — root at 2, multiplicity 1, crosses at $(2,0)$
- $P(x) = (x-2)^2$ — root at 2, multiplicity 2, touches at $(2,0)$
- $P(x) = (x-2)^3$ — root at 2, multiplicity 3, crosses but flattens

### End behavior

For large $\lvert x \rvert$, the leading term $a_n x^n$ dominates. The
end behavior depends only on the degree and the sign of $a_n$.
| Degree and sign | Behavior as $x → \pm\infty$|
| $n$ even, $a_n > 0$ | Up on both sides (like $x^2$) |
| $n$ even, $a_n < 0$ | Down on both sides |
| $n$ odd, $a_n > 0$ | Down left, up right (like $x^3$) |
| $n$ odd, $a_n < 0$ | Up left, down right |

Together with root multiplicity, end behavior lets you sketch the shape of
any polynomial graph from its factored form.

### Worked Example 6 — Sketching From Factored Form

**Given.** Sketch the general shape of:

$$P(x) = -2(x+3)(x-1)^2(x-4)$$

**Solution.**

Step 1 — Identify roots and multiplicities.

- $x = -3$: multiplicity 1 (odd) — **crosses**
- $x = 1$: multiplicity 2 (even) — **touches, bounces**
- $x = 4$: multiplicity 1 (odd) — **crosses**

Step 2 — End behavior. Degree = $1 + 2 + 1 = 4$ (even). Leading coefficient:
$-2 \times 1 \times 1 \times 1 = -2 < 0$.

Even degree, negative leading coefficient: **down on both sides**.

Step 3 — $y$-intercept. $P(0) = -2(3)(-1)^2(-4) = -2(3)(1)(-4) = 24$.

Step 4 — Sketch. Starting from the lower left (down), rises to cross at
$x = -3$, curves to touch the axis at $x = 1$ without crossing, falls and
then rises to cross at $x = 4$, then descends to the lower right.

**Check.** Four root appearances (counting multiplicity) for a degree-4
polynomial. ✓ $y$-intercept at 24. ✓

---

## 7.8 Engineering Applications of Polynomial Roots

### Beam natural frequencies

The natural frequencies of a vibrating structure come from setting a
polynomial characteristic equation to zero. For a two-span continuous
beam, the characteristic equation might be a quartic whose four roots give
two pairs of natural frequencies. We'll meet the mechanics in Chapter
02-33; the algebraic structure is exactly what you built here.

### Electrical circuit resonance

For a series RLC circuit, the characteristic equation is quadratic. The
discriminant tells you immediately whether the circuit will oscillate (under-
damped, complex roots) or decay without oscillating (over-damped, real roots)
or sit at the boundary (critically damped, repeated roots).

$$s^2 + \frac{R}{L}s + \frac{1}{LC} = 0$$

The roots are $s = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$ where
$\alpha = R/2L$ and $\omega_0 = 1/\sqrt{LC}$.

When $\omega_0 > \alpha$: complex roots, oscillation. When $\omega_0 <
\alpha$: real roots, exponential decay. This is precisely the discriminant
criterion from §7.4 in physical form.

### Worked Example 7 — Engineering Quadratic

**Given.** A projectile is launched vertically with initial velocity
$v_0 = 30 \text{ m/s}$ from a height $h_0 = 2.0 \text{ m}$ above
the ground. Its height is:

$$h(t) = -4.905t^2 + 30t + 2.0$$

(a) Find the time when $h = 0$ (ground impact).
(b) Find the maximum height.
(c) Interpret the discriminant.

**Solution.**

(a) Set $h = 0$ and apply the quadratic formula.

$a = -4.905$, $b = 30$, $c = 2.0$.

$\Delta = 30^2 - 4(-4.905)(2.0) = 900 + 39.24 = 939.24 > 0$.

Two real roots, as expected (projectile goes up, comes back down).

$$t = \frac{-30 \pm \sqrt{939.24}}{2(-4.905)} = \frac{-30 \pm 30.647}{-9.810}$$

$$t_1 = \frac{-30 + 30.647}{-9.810} = \frac{0.647}{-9.810} = -0.066 \text{ s}$$

$$t_2 = \frac{-30 - 30.647}{-9.810} = \frac{-60.647}{-9.810} = 6.182 \text{ s}$$

The negative root $t_1 = -0.066$ s corresponds to when the projectile
would have been at ground level before launch — physically meaningless
here. Ground impact occurs at $\boxed{t = 6.18 \text{ s}}$.

(b) Maximum height at vertex. For $P(t) = at^2 + bt + c$, the vertex is
at $t = -b/(2a)$:

$$t_{max} = \frac{-30}{2(-4.905)} = \frac{-30}{-9.810} = 3.058 \text{ s}$$

$$h_{max} = -4.905(3.058)^2 + 30(3.058) + 2.0$$
$$= -4.905(9.351) + 91.74 + 2.0$$
$$= -45.87 + 91.74 + 2.0 = \boxed{47.9 \text{ m}}$$

(c) The discriminant $\Delta = 939.24 > 0$ confirms two real roots —
physically, the projectile does cross ground level twice (once on the way
up if you extend the timeline backwards, once on the way down). 

> ---
> **Mentor's Margin**
>
> Notice the negative root $t_1 = -0.066$ s. It's mathematically valid but
> physically extraneous — the problem doesn't exist before $t = 0$. This is
> different from an algebraic extraneous solution (which fails to satisfy the
> equation). The equation is satisfied; the domain restricts what's
> physically meaningful. **After every polynomial solve, check each root
> against the physical context.** Negative time, negative length, and
> negative absolute pressure are common physically extraneous results.
>
> ---

---

## 7.9 Building a Polynomial from Its Roots

Given roots $r_1, r_2, \ldots, r_n$, the polynomial with leading coefficient
$a$ is:

$$P(x) = a(x - r_1)(x - r_2) \cdots (x - r_n)$$

**Complex roots always come in conjugate pairs** when all coefficients are
real. If $3 + 2i$ is a root, so is $3 - 2i$.

### Worked Example 8 — Building a Polynomial

**Given.** Find a polynomial with integer coefficients that has roots
$x = 2$, $x = -1$, and $x = 1 + 3i$.

**Solution.**

Complex roots come in conjugate pairs, so $x = 1 - 3i$ is also a root.
The polynomial is at minimum degree 4.

$$P(x) = (x - 2)(x + 1)(x - (1+3i))(x - (1-3i))$$

Multiply the complex conjugate pair first:

$$(x - (1+3i))(x - (1-3i)) = [(x-1) - 3i][(x-1) + 3i]$$
$$= (x-1)^2 - (3i)^2 = (x-1)^2 + 9 = x^2 - 2x + 1 + 9 = x^2 - 2x + 10$$

Now:

$$(x-2)(x+1) = x^2 - x - 2$$

Multiply the two quadratics:

$$(x^2 - x - 2)(x^2 - 2x + 10)$$

$= x^4 - 2x^3 + 10x^2$
$\quad - x^3 + 2x^2 - 10x$
$\quad - 2x^2 + 4x - 20$

$= x^4 - 3x^3 + 10x^2 + 2x^2 -2x^2 - 10x + 4x - 20$

$x^4$ terms: $x^4$

$x^3$ terms: $-2x^3 - x^3 = -3x^3$

$x^2$ terms: $10x^2 + 2x^2 - 2x^2 = 10x^2$

$x$ terms: $-10x + 4x = -6x$

Constant: $-20$

$$\boxed{P(x) = x^4 - 3x^3 + 10x^2 - 6x - 20}$$

**Verify using Vieta's.** Sum of roots: $2 + (-1) + (1+3i) + (1-3i) = 3$.
Check: $-(-3)/1 = 3$. ✓

Product of roots: $2 \times (-1) \times (1+3i)(1-3i) = (-2)(10) = -20$.
Check: $(-1)^4 \times (-20)/1 = -20$. ✓

---

## As the Handbook States It

> **Handbook 10.6, p. 37** — *Mathematics / Algebra*

The Handbook includes:

- Quadratic formula: $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
- The discriminant and its interpretation
- Basic polynomial definitions

**The Handbook does not include:**

- Synthetic division procedure
- Rational root theorem
- Remainder and factor theorems
- Vieta's formulas
- Root multiplicity and graph behavior rules
- Completing the square procedure
- Descartes' rule of signs

Those are memorize material. The quadratic formula is in the Handbook — but
you should know it cold anyway, because finding and verifying it under time
pressure costs you more than the lookup saves.

**Notation note.** The Handbook writes the quadratic formula exactly as
above. The discriminant $\Delta = b^2 - 4ac$ is defined but the symbol
$\Delta$ is not universally used — some sources write $D$. This guide
uses $\Delta$ throughout.

---

## Where This Goes Wrong

**Wrong denominator in the quadratic formula.** The denominator is $2a$,
not $2$. When $a \ne 1$, writing $2$ gives wrong roots. Write the formula
out completely with $2a$ before substituting.

**Missing the $\pm$.** Both roots must be computed. Forgetting the $\pm$
gives only one root of what may be a two-root equation.

**Treating a negative discriminant as an error.** It isn't. It means two
complex conjugate roots. In a physical system, it means oscillatory behavior.
Write the complex roots and interpret them — don't stop at "no real solution."

**Not simplifying $\sqrt{\Delta}$ before putting it in the formula.**
$\sqrt{48} = 4\sqrt{3}$; leaving it unsimplified hides that the roots may be tidy fractions.

**Synthetic division with a non-monic divisor.** If dividing by $2x - 3$,
synthetic division uses $r = 3/2$ (the root of the divisor), not $r = 3$.
Then divide the quotient polynomial by 2.

**Testing rational root candidates with no stopping rule.** Run Descartes
first. Knowing there is exactly one negative root means you stop testing
negative candidates the moment you find it, rather than working through the
whole list.

**Negating every coefficient to build $P(-x)$.** Only the odd-degree terms
flip. Negating all of them gives a wrong sign-change count with nothing
downstream to catch it.

**Reading a Descartes count as exact when it isn't.** A count of 2 means 2 or
0; a count of 3 means 3 or 1. Only 0 and 1 are exact. Treating "2 sign
changes" as a guarantee of two positive roots will have you hunting for a
root that isn't there.

**Ignoring multiplicity.** A root of multiplicity 2 contributes $(x-r)^2$
to the factored form. Missing this means the degree of your fully-factored
form won't match the original polynomial's degree.

**Discarding physically extraneous roots without checking.** Every root
should be examined against the physical domain. Negative time, negative
mass, negative length — these are invalid physically. A complex root might
also be physically meaningful as oscillation information even if the original
quantity must be real.

**Building a polynomial from complex roots without including the conjugate.**
If all coefficients must be real, complex roots come in conjugate pairs.
Specifying only one of a complex pair produces a polynomial with complex
coefficients.

---

## Key Terms

| Term | Definition |
|---|---|
| Polynomial | Expression $a_n x^n + \cdots + a_0$ with non-negative integer exponents |
| Degree | The highest power of the variable with a nonzero coefficient |
| Leading coefficient | Coefficient of the highest-degree term |
| Root (zero) | A value $r$ where $P(r) = 0$ |
| Multiplicity | How many times a root appears (how many times the corresponding factor divides $P$) |
| Fundamental theorem of algebra | A degree-$n$ polynomial has exactly $n$ roots, counting multiplicity and complex roots |
| Remainder theorem | Remainder when $P(x)$ is divided by $(x-r)$ equals $P(r)$ |
| Factor theorem | $(x-r)$ is a factor of $P(x)$ iff $P(r) = 0$ |
| Synthetic division | Shorthand division algorithm for dividing a polynomial by a linear factor $(x-r)$ |
| Discriminant $\Delta$ | $b^2 - 4ac$; determines the nature of quadratic roots |
| Complex conjugate roots | Roots of the form $p \pm qi$; always appear in pairs when polynomial has real coefficients |
| Completing the square | Rewriting a quadratic as $(x+h)^2 + k$ by adding and subtracting $(b/2a)^2$ |
| Quadratic formula | $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$; always works for quadratics |
| Rational root theorem | For integer-coefficient polynomials, rational roots $p/q$ have $p \mid a_0$ and $q \mid a_n$ |
| Vieta's formulas | Relationships between the roots and coefficients without solving explicitly |
| End behavior | How $P(x)$ behaves as $x \to \pm\infty$; determined by degree and leading coefficient sign |
| Descartes' rule of signs | Sign changes in $P(x)$ bound the positive real roots, and in $P(-x)$ the negative real roots, in each case exactly or less by an even number |
| Sign change | A place where consecutive nonzero coefficients differ in sign; zero coefficients are skipped |
---

## Review Questions

### Conceptual

1. State the fundamental theorem of algebra. What does "counting multiplicity
   and complex roots" mean for a cubic polynomial?
2. What does the discriminant tell you about the roots of a quadratic before
   you compute them? Give the physical interpretation of each case for an
   RLC circuit.
3. Explain the connection between roots and factors stated by the factor
   theorem. Why is this connection useful in engineering?
4. Why do complex roots of a polynomial with real coefficients always come in
   conjugate pairs? Show what goes wrong if they didn't.
5. What does a root of multiplicity 2 look like on a graph, and why?
6. You apply the quadratic formula and get complex roots. Is this an error?
   When is it physically meaningful?
7. The rational root theorem gives you a list of candidates. What do you do
   after you have the list?
8. State Vieta's formulas for a quadratic. Give a situation where they're
   faster than the quadratic formula.

### Calculation

9. Perform each polynomial operation:
   (a) $(3x^3 - x + 4) + (-x^3 + 2x^2 + x - 7)$
   (b) $(2x^2 - 3)(x^2 + x - 1)$
   (c) $(x^3 - 2x^2 + 5x - 3) \div (x - 1)$ using long division

10. Use synthetic division:
    (a) $(2x^4 - 3x^3 + x - 5) \div (x + 2)$
    (b) Verify the remainder using the remainder theorem

11. Evaluate the discriminant and describe the roots (real distinct, real
    repeated, or complex). Then solve:
    (a) $x^2 - 7x + 10 = 0$
    (b) $4x^2 - 12x + 9 = 0$
    (c) $x^2 + 4x + 13 = 0$
    (d) $3x^2 - 5x - 2 = 0$

12. Solve by completing the square:
    (a) $x^2 + 8x + 7 = 0$
    (b) $2x^2 - 12x + 10 = 0$

13. Find all real roots using the rational root theorem plus synthetic division:
    (a) $P(x) = x^3 - 6x^2 + 11x - 6$
    (b) $P(x) = 2x^3 + 3x^2 - 11x - 6$; give a Descarte's prediction of the roots
    (c) $P(x) = x^4 - 5x^2 + 4$

14. A quadratic has roots $r_1 = 3$ and $r_2 = -\frac{1}{2}$ and leading
    coefficient $2$.
    (a) Write the polynomial in factored form, then expanded.
    (b) Verify using Vieta's formulas.

15. Find a polynomial with real coefficients, integer coefficients, and
    minimum degree, having the given roots:
    (a) $x = 5$ (multiplicity 2), $x = -3$
    (b) $x = 2$, $x = 1 + i$
    (c) $x = 0$, $x = -2$, $x = 3 + i$

16. For each polynomial, describe end behavior, identify roots and
    multiplicities, and sketch the general shape:
    (a) $P(x) = (x+2)^2(x-3)$
    (b) $P(x) = -x(x-1)^3(x+2)^2$

17. **Engineering.** A rectangular sheet of metal has dimensions $40$ cm
    by $30$ cm. Equal squares of side $x$ cm are cut from each corner, and
    the sides are folded up to make an open box.
    (a) Write the volume $V(x)$ as a polynomial.
    (b) Find the domain of $x$.
    (c) Find the value of $x$ that maximizes volume. (the maximizing value of
	    $x$ satisfies #3x^2-70x+300=0$; solve it and reject the root outside the domain.)

18. **Engineering.** An RLC series circuit has characteristic equation:

    $$2s^2 + 8s + 10 = 0$$

    (a) Compute the discriminant.
    (b) Find the roots.
    (c) State whether the circuit is underdamped (oscillatory), critically
        damped, or overdamped.
    (d) Write the general solution form implied by the roots.

19. **Engineering.** The deflection of a simply supported beam of length
    $L = 4$ m under a uniformly distributed load produces a deflection
    function whose shape can be approximated by a constructed polynomial that equals
    zero at the supports and at no interior points.

    If the deflection equation is:
    $$y(x) = k \cdot x(L - x)(x^2 - Lx - L^2)$$

    (a) Where are the roots of the polynomial factor $x^2 - Lx - L^2$ for
    $L = 4$? (Use the quadratic formula.)
    (b) Are these roots in the physical domain $[0, 4]$?
    (c) What does that tell you about the beam's deflection in the physical
    domain?

### Multiple Choice

20. The discriminant of $2x^2 + 3x - 5 = 0$ is:
    A) $9$
    B) $31$
    C) $49$
    D) $-31$

21. By the remainder theorem, the remainder when $P(x) = x^3 - 4x + 1$ is
    divided by $(x - 2)$ is:
    A) $0$
    B) $1$
    C) $-1$
    D) $3$

22. The polynomial $P(x) = (x-1)^2(x+3)$ has:
    A) Three distinct real roots
    B) Roots at $x = 1$ and $x = -3$, where $x = 1$ has multiplicity 2
    C) A double root at $x = -3$ and a simple root at $x = 1$
    D) Complex roots only

23. The sum of the roots of $3x^2 - 7x + 4 = 0$ is:
    A) $4/3$
    B) $7/3$
    C) $-7/3$
    D) $-4/3$

24. A polynomial of degree 5 with real coefficients has two complex roots
    $2 \pm 3i$. The minimum number of real roots is:
    A) $0$
    B) $1$
    C) $2$
    D) $3$

25. Synthetic division of $P(x)$ by $(x - r)$ gives a remainder of zero.
    This means:
    A) $P(0) = r$
    B) $r$ is a root of $P(x)$
    C) $r = 0$
    D) $P(x)$ is a constant

26. The end behavior of $P(x) = -3x^4 + 2x^3 - x + 5$ as $x \to +\infty$:
    A) $P(x) \to +\infty$
    B) $P(x) \to -\infty$
    C) $P(x) \to 5$
    D) $P(x)$ oscillates

---

## Answer Key with Explanations

**1.** A degree-$n$ polynomial has exactly $n$ roots counting multiplicity and
including complex roots. For a cubic ($n = 3$): it has exactly 3 roots. Some
may be the same (multiplicity > 1) and some may be complex. For example,
$x^3 - 3x^2 + 4 = (x+1)(x-2)^2$ has three roots: $x = -1$ (once) and
$x = 2$ (twice, multiplicity 2). (§7.1)

**2.** $\Delta > 0$: two distinct real roots. For an RLC circuit, this means
overdamped — the circuit returns to equilibrium without oscillating.
$\Delta = 0$: one repeated real root. Critically damped — returns to
equilibrium as fast as possible without oscillating.
$\Delta < 0$: two complex conjugate roots. Underdamped — oscillates while
decaying. (§7.4)

**3.** By the factor theorem, $(x - r)$ is a factor of $P(x)$ if and only if
$P(r) = 0$. So finding roots is the same as finding linear factors. This is
useful because a factored polynomial immediately shows: where it is zero
(roots), how many times it vanishes there (multiplicity), and what sign it
has between roots. Transfer functions, characteristic equations, and partial
fraction expansions all rely on factored polynomial form. (§7.3)

**4.** For a polynomial with real coefficients, complex roots appear in
conjugate pairs because if $P(p + qi) = 0$ and all coefficients are real,
then taking the complex conjugate of both sides of $P(p+qi) = 0$ gives
$P(p-qi) = 0$ (conjugation distributes through addition and multiplication,
and conjugate of a real number is itself). If they didn't come in pairs,
the polynomial would have odd degree with all remaining roots complex —
impossible because expanding $(x - (p+qi))$ alone gives complex
coefficients, requiring the conjugate factor to restore real coefficients.
(§7.9)

**5.** A root of multiplicity 2 means $(x-r)^2$ divides the polynomial. Near
$r$, $P(x) \approx C(x-r)^2$ — a parabola shape. Since the square is never
negative, the sign of $P$ doesn't change across $r$. The graph touches the
$x$-axis at $r$ and bounces back without crossing. (§7.7)

**6.** No, it's not an error — it's real information. For an RLC circuit with
a quadratic characteristic equation, complex roots $\alpha \pm j\omega$
indicate underdamped oscillation at frequency $\omega$ with exponential
envelope decaying at rate $|\alpha|$. The physical voltages and currents are
real; the complex roots describe the oscillation behavior through the formula
$e^{(\alpha \pm j\omega)t} = e^{\alpha t}(\cos\omega t \pm j\sin\omega t)$.
(§7.4, §7.8)

**7.** After listing candidates, test them by substitution or synthetic
division, simplest first ($\pm 1$ before $\pm 1/2$). When a root is found,
divide it out to reduce the degree. Continue on the reduced polynomial.
Stop when you have a quadratic — apply the quadratic formula for the
remaining two roots. (§7.6)

**8.** Vieta's formulas for a quadratic $ax^2 + bx + c = 0$: sum of roots
$= -b/a$, product of roots $= c/a$. Faster when you know one root and need
the other, or when you need to verify without full substitution. Example:
given roots $r_1 = 4$ and the equation $3x^2 + kx - 12 = 0$, the product
$4 \cdot r_2 = -12/3 = -4$ gives $r_2 = -1$ immediately. (§7.5)

**9.**

(a) $(3-1)x^3 + 2x^2 + (-1+1)x + (4-7) = \boxed{2x^3 + 2x^2 - 3}$

(b) Distribute each term:
$2x^2 \cdot (x^2 + x - 1) = 2x^4 + 2x^3 - 2x^2$
$(-3) \cdot (x^2 + x - 1) = -3x^2 - 3x + 3$

Sum: $\boxed{2x^4 + 2x^3 - 5x^2 - 3x + 3}$

(c) Long division of $x^3 - 2x^2 + 5x - 3$ by $(x-1)$:

$$x^3 - 2x^2 + 5x - 3 = (x-1)(x^2 - x + 4) + 1$$

Check: $P(1) = 1 - 2 + 5 - 3 = 1$ = remainder ✓

Quotient: $\boxed{x^2 - x + 4}$, remainder $1$.

**10.**

(a) Coefficients: $2, -3, 0, 1, -5$. Divide by $(x+2)$, so $r = -2$.

$$\begin{array}{c|ccccc} -2 & 2 & -3 & 0 & 1 & -5 \\ & & -4 & 14 & -28 & 54 \\ \hline & 2 & -7 & 14 & -27 & 49 \end{array}$$

Quotient: $2x^3 - 7x^2 + 14x - 27$, remainder $\boxed{49}$.

(b) $P(-2) = 2(16) - 3(-8) + (-2) - 5 = 32 + 24 - 2 - 5 = 49$ ✓

**11.**

(a) $\Delta = 49 - 40 = 9 > 0$. Two distinct real roots.
$x = \frac{7 \pm 3}{2}$: $\boxed{x = 5 \text{ or } x = 2}$

(b) $\Delta = 144 - 144 = 0$. One repeated real root.
$x = \frac{12}{8} = \boxed{x = \frac{3}{2}}$ (double root)

(c) $\Delta = 16 - 52 = -36 < 0$. Two complex conjugate roots.
$x = \frac{-4 \pm \sqrt{-36}}{2} = \frac{-4 \pm 6i}{2} = \boxed{-2 \pm 3i}$

(d) $\Delta = 25 + 24 = 49 > 0$. Two distinct real roots.
$x = \frac{5 \pm 7}{6}$: $x = 2$ or $x = -\frac{1}{3}$. $\boxed{x = 2 \text{ or } x = -1/3}$

**12.**

(a) $x^2 + 8x = -7$. Half of 8 is 4, square is 16. Add 16:
$(x+4)^2 = 9$. $x + 4 = \pm 3$. $\boxed{x = -1 \text{ or } x = -7}$

(b) Divide by 2: $x^2 - 6x + 5 = 0 \Rightarrow x^2 - 6x = -5$.
Half of 6 is 3, square is 9: $(x-3)^2 = 4$. $x - 3 = \pm 2$.
$\boxed{x = 5 \text{ or } x = 1}$

**13.**

(a) Candidates: $\pm 1, \pm 2, \pm 3, \pm 6$.

$P(1) = 1 - 6 + 11 - 6 = 0$. Factor: $(x-1)$.

Synthetic: quotient $x^2 - 5x + 6 = (x-2)(x-3)$.

$\boxed{x = 1, 2, 3}$

(b) Descarte's predicts exactly 1 positive and 2 or 0 negitive roots

$a_0 = -6$, $a_n = 2$. Candidates: $\pm 1, \pm 2, \pm 3, \pm 6, \pm\frac{1}{2}, \pm\frac{3}{2}$.

$P(-3) = 2(-27) + 3(9) - 11(-3) - 6 = -54 + 27 + 33 - 6 = 0$. Factor: $(x+3)$.

Synthetic with $r = -3$: quotient $2x^2 - 3x - 2 = (2x+1)(x-2)$.

$\boxed{x = -3, \; x = 2, \; x = -\frac{1}{2}}; 1 postive and 2 negitive roots as predicted$

(c) Let $u = x^2$: $u^2 - 5u + 4 = (u-1)(u-4) = 0$.

$x^2 = 1 \Rightarrow x = \pm 1$. $x^2 = 4 \Rightarrow x = \pm 2$.

$\boxed{x = \pm 1, \pm 2}$

**14.**

(a) $P(x) = 2(x-3)(x+\frac{1}{2}) = 2(x-3)\cdot\frac{1}{2}(2x+1) = (x-3)(2x+1)$

Expanded: $2x^2 + x - 6x - 3 = \boxed{2x^2 - 5x - 3}$

(b) Sum: $3 + (-1/2) = 5/2 = -b/a = 5/2$ ✓

Product: $3 \times (-1/2) = -3/2 = c/a = -3/2$ ✓

**15.**

(a) Multiplicity 2 at $x=5$, simple at $x=-3$: $\boxed{(x-5)^2(x+3) = x^3 - 7x^2 - 5x + 75}$

(b) Conjugate of $1+i$ is $1-i$:

$(x-2)(x-(1+i))(x-(1-i)) = (x-2)[(x-1)^2+1] = (x-2)(x^2-2x+2)$

$= x^3 - 2x^2 + 2x - 2x^2 + 4x - 4 = \boxed{x^3 - 4x^2 + 6x - 4}$

(c) Conjugate of $3+i$ is $3-i$. Roots: $0, -2, 3+i, 3-i$.

$(3+i)(3-i)$-pair factor: $(x-(3+i))(x-(3-i)) = (x-3)^2+1 = x^2-6x+10$

$P(x) = x(x+2)(x^2-6x+10)$

$(x)(x+2) = x^2 + 2x$

$(x^2+2x)(x^2-6x+10) = x^4 - 6x^3 + 10x^2 + 2x^3 - 12x^2 + 20x$

$= \boxed{x^4 - 4x^3 - 2x^2 + 20x}$

**16.**

(a) $P(x) = (x+2)^2(x-3)$

Roots: $x = -2$ (mult. 2, touches), $x = 3$ (mult. 1, crosses).
Degree 3, positive leading coefficient: down left, up right.
$y$-intercept: $(−2)^2(−3) = −12$.

Sketch: from lower left, rises and touches axis at $x = -2$, dips below, crosses at $x = 3$, rises to upper right.

(b) $P(x) = -x(x-1)^3(x+2)^2$

Roots: $x = 0$ (mult. 1, crosses), $x = 1$ (mult. 3, crosses — odd),
$x = -2$ (mult. 2, touches).
Degree 6, negative leading coefficient: down on both sides.
$y$-intercept: $0$.

Sketch: from lower left, rises, touches at $x = -2$, crosses zero at $x = 0$, crosses at $x = 1$ (with flattening), falls to lower right.

**17.**

(a) After cutting corners of size $x$ from a $40 \times 30$ sheet:

$$V(x) = x(40 - 2x)(30 - 2x)$$

Expand: $x(1200 - 80x - 60x + 4x^2) = x(1200 - 140x + 4x^2)$

$$\boxed{V(x) = 4x^3 - 140x^2 + 1200x}$$

(b) Domain: $x > 0$, $40 - 2x > 0 \Rightarrow x < 20$, $30 - 2x > 0 \Rightarrow x < 15$.

Most restrictive: $\boxed{0 < x < 15}$

(c) $\dfrac{dV}{dx} = 12x^2 - 280x + 1200 = 0$

Divide by 4: $3x^2 - 70x + 300 = 0$

$$x = \frac{70 \pm \sqrt{4900 - 3600}}{6} = \frac{70 \pm \sqrt{1300}}{6} = \frac{70 \pm 36.06}{6}$$

$x_1 = \frac{70 - 36.06}{6} = \frac{33.94}{6} = \boxed{5.66 \text{ cm}}$

$x_2 = \frac{70 + 36.06}{6} = 17.7 \text{ cm}$ — outside domain, reject.

$V(5.66) = 5.66(40 - 11.32)(30 - 11.32) = 5.66(28.68)(18.68) \approx 3{,}032 \text{ cm}^3$

**18.**

(a) $\Delta = 64 - 4(2)(10) = 64 - 80 = \boxed{-16}$

(b) $s = \dfrac{-8 \pm \sqrt{-16}}{4} = \dfrac{-8 \pm 4i}{4} = \boxed{-2 \pm i}$

(c) $\Delta < 0$: complex roots. The real part is $-2 < 0$, imaginary part is $\pm 1$.

$\boxed{\text{Underdamped}}$ — oscillates with angular frequency $1$ rad/s, decaying at rate $e^{-2t}$.

(d) General solution: $x(t) = e^{-2t}(C_1\cos t + C_2\sin t)$ — decaying oscillation.

**19.**

(a) $x^2 - 4x - 16 = 0$ (with $L = 4$):

$$x = \frac{4 \pm \sqrt{16 + 64}}{2} = \frac{4 \pm \sqrt{80}}{2} = \frac{4 \pm 4\sqrt{5}}{2} = 2 \pm 2\sqrt{5}$$

$x_1 = 2 - 2\sqrt{5} \approx 2 - 4.47 = -2.47$

$x_2 = 2 + 2\sqrt{5} \approx 2 + 4.47 = 6.47$

(b) Physical domain is $[0, 4]$. Neither $-2.47$ nor $6.47$ lies in $[0, 4]$.

(c) The factor $x^2 - Lx - L^2$ has no zeros in the physical domain, so
$y(x) = k \cdot x(L-x)(x^2 - Lx - L^2)$ has zeros only from $x(L-x)$ in
$[0, L]$, i.e., at the supports $x = 0$ and $x = L = 4$ only. The
deflection is zero only at the endpoints, consistent with a simply supported
beam — no internal zero crossings.

**20. C — 49.** $\Delta = 3^2 - 4(2)(-5) = 9 + 40 = 49$.
(A) ignores $4ac$; (B) has a sign error. (§7.4)

**21. B — $1$.** By the remainder theorem: $P(2) = (2)^3 - 4(2) + 1 = 8 - 8 + 1 = 1$. The answer is $\boxed{1}$.

**22. B.** The polynomial has a double root at $x = 1$ (multiplicity 2) and
a simple root at $x = -3$ (multiplicity 1). (A) would require three distinct
roots. (C) reverses which root has which multiplicity. (§7.7)

**23. B — $7/3$.** By Vieta's, sum of roots $= -b/a = -(-7)/3 = 7/3$.
(§7.5)

**24. B — 1.** The two complex roots $2 \pm 3i$ account for 2 of the 5 roots.
Complex roots come in conjugate pairs (already satisfied). Remaining 3 roots
must be real (complex roots come in pairs, so can't have 1 or 3 remaining
complex roots without another pair — leaving an odd number of complex
non-paired roots, impossible for real coefficients). With 3 remaining roots
all real: minimum real roots = 3. 

$\boxed{\text{Answer: B — 1}}$

**25. B — $r$ is a root of $P(x)$.** By the factor theorem, zero remainder
means $(x-r)$ divides $P(x)$ exactly, meaning $P(r) = 0$. (§7.3)

**26. B — $P(x) \to -\infty$.** Degree 4 (even), leading coefficient $-3$
(negative). Even degree, negative leading coefficient: both ends go down.
As $x \to +\infty$: $P(x) \to -\infty$. (§7.7)

---

## Quick Reference

**Polynomial structure**

$P(x) = a_n x^n + \cdots + a_0$, degree $n$, leading coeff $a_n \ne 0$.

**Fundamental theorem:** exactly $n$ roots counting multiplicity and complex.

**Factor and remainder theorems**

$(x-r)$ is a factor $\iff$ $P(r) = 0$. Remainder of $P(x) \div (x-r)$ is $P(r)$.

**Synthetic division** — for linear divisors $(x-r)$ only.

**Quadratic formula** — *Handbook p. 37*

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Discriminant $\Delta = b^2 - 4ac$**

| $\Delta$ | Roots | Physical meaning |
|---|---|---|
| $> 0$ | 2 real distinct | overdamped / two crossings |
| $= 0$ | 1 real repeated | critically damped / tangent |
| $< 0$ | 2 complex conjugate | underdamped / oscillatory |

**Vieta's formulas (quadratic $ax^2+bx+c$)**

$$r_1 + r_2 = -\frac{b}{a} \qquad r_1 r_2 = \frac{c}{a}$$

**Rational root theorem**

Rational root $p/q$: $p \mid a_0$, $q \mid a_n$.

**Descartes' rule of signs**

Positive real roots: sign changes in $P(x)$, or fewer by an even number.
Negative real roots: sign changes in $P(-x)$, or fewer by an even number.
Build $P(-x)$ by flipping odd-degree terms only. Counts of 0 and 1 are exact.

**Root multiplicity and graph**

Odd multiplicity → crosses axis. Even multiplicity → touches and bounces.

**End behavior** (determined by degree and sign of $a_n$ alone)

Even degree, $a_n > 0$: both ends up.
Even degree, $a_n < 0$: both ends down.
Odd degree, $a_n > 0$: down left, up right.
Odd degree, $a_n < 0$: up left, down right.

**Building from roots**

$P(x) = a(x-r_1)(x-r_2)\cdots(x-r_n)$. Complex roots always in conjugate
pairs for real-coefficient polynomials.

**Not in the Handbook — memorize**

Synthetic division · rational root theorem · Vieta's formulas · root
multiplicity rules · end behavior rules · completing the square procedure

---

## What's Next

Apprentice, three chapters into Tier 1B, and the algebraic foundation is
nearly complete.

In **Chapter 01-08: Systems of Equations**, we handle the situation that
arises in virtually every multi-component engineering problem: two or more
equations in two or more unknowns. A structural joint with unknown forces
in three members. A circuit with multiple loops, each giving a Kirchhoff
voltage equation. A heat exchanger with inlet and outlet temperatures
connected by energy balance and rate equations.

The methods — substitution, elimination, and the matrix approach — are
all equivalent, but each has its strengths. Gaussian elimination with back
substitution will reappear in a different form when we reach matrices in
Chapter 01-14 and yet again when we solve truss problems in Chapter 02-24.
It's worth investing in now.

Bring the Handbook to page 37. We'll be there.

See you there.

— Your Mentor
