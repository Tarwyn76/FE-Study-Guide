---
chapter: "01-15"
title: "Sequences, Series, and Progressions"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-015-01, MATH-1B-015-02, MATH-1B-015-03, MATH-1B-015-04]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-15: Sequences, Series, and Progressions

> *"Add a fixed amount each step and you get a straight line. Multiply by a
> fixed factor each step and you get a curve that either runs away to
> infinity or settles onto a finite number. Almost every staged engineering
> process — a construction schedule, a cascade of amplifier stages, a train
> of settling tanks, a loan repayment — is one of those two patterns. Learn
> the two formulas and you can total up the whole process without adding the
> terms one at a time."*

---

## Before You Start

**Prerequisites:** [01-04 Expressions, Equations, and Inequalities](01-04-expressions-equations-inequalities.md) · [01-05 Exponents, Radicals, and Logarithms](01-05-exponents-radicals-logarithms.md) · [01-06 Functions, Graphs, and Transformations](01-06-functions-graphs-transformations.md)

**Skip if:** You pass the Tier 1B test-out quiz. Verify you can write and
evaluate summation notation, use both arithmetic and geometric term-and-sum
formulas, and state the convergence condition for an infinite geometric
series before skipping. The off-by-one in the term formulas is the most
common rust point.

**Time:** ~50 min read · ~20 min review questions · ~50 min practice problems

---

## On the Board Today

Apprentice, this is the last chapter of Tier 1B. It is also the shortest
conceptual jump you will make in this tier, because you already have the
machinery. A sequence is just a function whose input is restricted to the
positive integers, and you built functions in Chapter 01-06. A geometric
sequence is an exponential function sampled at integer steps, and you built
exponentials in Chapter 01-05.

Two patterns carry nearly all of the engineering weight.

An **arithmetic progression** adds a constant. Pour 12 cubic metres of
concrete today and 3 more each day than the day before. Increase a load in
equal increments. Space stirrups at a uniform pitch. The terms grow linearly,
and the sum grows with the square of the number of terms.

A **geometric progression** multiplies by a constant. Each amplifier stage
multiplies the signal power by a gain factor. Each settling tank removes the
same *fraction* of the remaining solids. Each year a loan balance grows by
one interest factor. The terms grow or decay exponentially, and here is the
part worth remembering: if the ratio is less than one in magnitude, you can
add up *infinitely many* terms and get a finite answer.

That last fact is not a curiosity. It is why a bouncing ball travels a
finite total distance despite bouncing forever in the idealized model, why
an infinite resistor ladder has a finite input resistance, and why the
present worth of a perpetual annuity is a finite number.

We will also set up the summation notation you will read for the rest of the
guide. Every centroid integral, every statistical mean, every mass balance
you meet from Tier 1C onward is written with a sigma or its continuous
cousin. Get comfortable reading it here, where the terms are simple.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 15.1 Distinguish a sequence from a series and identify a general term
* 15.2 Read, write, and evaluate summation notation, including changing
  the index limits
* 15.3 Apply the linearity properties of summation
* 15.4 Identify an arithmetic progression and find its $n$th term and
  partial sum
* 15.5 Identify a geometric progression and find its $n$th term and
  partial sum
* 15.6 State the convergence condition for an infinite geometric series and
  evaluate the sum when it converges
* 15.7 Apply the closed-form sums for $\sum k$, $\sum k^2$, and $\sum k^3$
* 15.8 Use factorial notation
* 15.9 Recognize arithmetic and geometric structure in staged engineering
  processes

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $a_n$ | the $n$th term of a sequence | $n$ is a positive integer |
| $a_1$ | the first term | some texts index from $a_0$; watch for it |
| $n$ | term number, or number of terms | context distinguishes them |
| $d$ | common difference (arithmetic) | $d = a_{n+1} - a_n$ |
| $r$ | common ratio (geometric) | $r = a_{n+1}/a_n$ |
| $S_n$ | sum of the first $n$ terms (partial sum) | a finite number always |
| $S_\infty$ | sum of an infinite series | exists only when it converges |
| $\sum$ | summation operator | "sigma" |
| $k$ | summation index (dummy variable) | also $i$, $j$; never reused as a real quantity |
| $n!$ | $n$ factorial | $n! = n(n-1)(n-2)\cdots(1)$ |

> ---
> **Mentor's Margin**
>
> The summation index is a *dummy variable*. It exists only inside the sum
> and its name carries no meaning: $\sum_{k=1}^{5}k^2$ and
> $\sum_{i=1}^{5}i^2$ are the same number. This matters because in Tier 2
> you will meet sums where $i$ is already spoken for as the imaginary unit or
> the interest rate. Rename the index freely. Nothing depends on the letter.
>
> ---

---

## 15.1 Sequences and Series

A **sequence** is an ordered list of numbers:

$$a_1, \; a_2, \; a_3, \; \ldots, \; a_n, \; \ldots$$

Formally it is a function whose domain is the positive integers. Its graph is
a set of isolated dots, not a curve — nothing exists between $n = 3$ and
$n = 4$.

A **series** is what you get when you *add* the terms of a sequence:

$$a_1 + a_2 + a_3 + \cdots$$

Sequence: a list. Series: a total. Keep them separate in your head, because
the exam asks for both and the formulas are different.

The **general term** (or $n$th term) $a_n$ is a formula that produces any
term you want from its index. For the sequence $3, 7, 11, 15, \ldots$ the
general term is $a_n = 4n - 1$. Check: $a_1 = 3$ ✓, $a_4 = 15$ ✓.

A **finite** sequence stops. An **infinite** sequence does not.

![FIG-01-15-001: Side-by-side plot comparing a continuous function f(x) = 4x - 1 drawn as a smooth line, and the sequence a_n = 4n - 1 drawn as isolated dots at n = 1 through 6 lying on that line, with the gaps between dots emphasized to show the domain restriction to positive integers](../figures/FIG-01-15-001-sequence-vs-function.png)

---

## 15.2 Summation Notation

$$\sum_{k=1}^{n} a_k = a_1 + a_2 + a_3 + \cdots + a_n$$

Read it as: "the sum, as $k$ runs from 1 to $n$, of $a_k$."

Four parts:

- the **operator** $\sum$
- the **index** $k$, with its **lower limit** below and **upper limit** above
- the **summand** $a_k$, the expression being added

The number of terms in $\sum_{k=m}^{n}$ is $n - m + 1$. Not $n - m$. Count
the endpoints.

$$\sum_{k=3}^{9} \quad\text{has}\quad 9 - 3 + 1 = 7 \text{ terms}$$

### Linearity properties

These are the three rules you will use constantly:

$$\boxed{\sum_{k=1}^{n} c\,a_k = c\sum_{k=1}^{n} a_k}$$

$$\boxed{\sum_{k=1}^{n} (a_k \pm b_k) = \sum_{k=1}^{n} a_k \pm \sum_{k=1}^{n} b_k}$$

$$\boxed{\sum_{k=1}^{n} c = nc \qquad (c \text{ constant, no } k)}$$

The first two say a summation passes through constants and splits across
addition. The third is the one people get wrong: if the summand does not
contain the index, you are adding the same number $n$ times.

> ---
> **Mentor's Margin**
>
> A summation does **not** pass through a product or a quotient.
> $\sum a_k b_k \ne \left(\sum a_k\right)\left(\sum b_k\right)$, and
> $\sum \frac{1}{a_k} \ne \frac{1}{\sum a_k}$. Only scalar multiples and
> term-by-term addition come out. Test it on two terms if you ever doubt it:
> $\sum_{k=1}^{2} k \cdot k = 1 + 4 = 5$, but
> $\left(\sum k\right)\left(\sum k\right) = 3 \times 3 = 9$. Different.
>
> ---

### Worked Example 1 — Evaluating and Reindexing a Sum

**Given.** Evaluate $\displaystyle\sum_{k=1}^{5}(2k - 3)$ two ways.

**Solution — term by term.**

| $k$ | $2k - 3$ |
|---|---|
| 1 | $-1$ |
| 2 | $1$ |
| 3 | $3$ |
| 4 | $5$ |
| 5 | $7$ |

$$\sum = -1 + 1 + 3 + 5 + 7 = \boxed{15}$$

**Solution — by linearity.**

$$\sum_{k=1}^{5}(2k-3) = 2\sum_{k=1}^{5}k - \sum_{k=1}^{5}3 = 2(1+2+3+4+5) - 5(3) = 2(15) - 15 = 15 \;\checkmark$$

Note the second sum: the summand 3 contains no $k$, so it contributes
$5 \times 3 = 15$, not 3.

**Observation.** The terms $-1, 1, 3, 5, 7$ increase by a constant 2. This is
an arithmetic progression, which is where we go next — and there is a formula
that would have given 15 in one line.

---

## 15.3 Arithmetic Progressions

An **arithmetic progression** (arithmetic sequence) adds a constant
**common difference** $d$ at each step:

$$a_1, \; a_1 + d, \; a_1 + 2d, \; a_1 + 3d, \; \ldots$$

$$\boxed{d = a_{n+1} - a_n \quad \text{(same for every } n)}$$

### The $n$th term

$$\boxed{a_n = a_1 + (n-1)d}$$

The coefficient is $(n-1)$, not $n$. The first term takes zero steps; the
second takes one. Getting this wrong shifts every answer by one $d$.

### The partial sum

$$\boxed{S_n = \frac{n(a_1 + a_n)}{2} = \frac{n\big[2a_1 + (n-1)d\big]}{2}}$$

Use the first form when you know both endpoints, the second when you know
$a_1$ and $d$.

**Why it works.** Pair the first term with the last, the second with the
second-to-last, and so on. Each pair sums to $a_1 + a_n$, because as you move
one step forward from the front you move one step back from the rear, and the
two $d$'s cancel. There are $n/2$ such pairs. Hence $S_n = \frac{n}{2}(a_1 +
a_n)$.

![FIG-01-15-002: Gauss pairing visual. The arithmetic series 4 + 7 + 10 + 13 + 16 + 19 written in a row, with curved arrows pairing first-with-last, second-with-fifth, third-with-fourth, each pair labeled with the identical sum 23, and the total shown as 3 pairs times 23 = 69](../figures/FIG-01-15-002-arithmetic-pairing.png)

That reasoning gives you the two special cases worth knowing cold:

$$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$$

$$\sum_{k=1}^{n} (2k-1) = n^2 \qquad \text{(sum of the first } n \text{ odd numbers)}$$

### Worked Example 2 — Construction Schedule

**Given.** A concrete placement schedule pours 12 m³ on day 1 and increases
the daily volume by 3 m³ each day thereafter.

**(a)** How much is poured on day 15?
**(b)** What is the total poured through day 15?
**(c)** On what day does the cumulative total first exceed 1000 m³?

**Solution.**

$a_1 = 12$ m³, $d = 3$ m³/day.

**(a)** $a_{15} = 12 + (15-1)(3) = 12 + 42 = \boxed{54 \text{ m}^3}$

**(b)** $S_{15} = \dfrac{15(12 + 54)}{2} = \dfrac{15(66)}{2} = 15(33) = \boxed{495 \text{ m}^3}$

**(c)** Set $S_n > 1000$ using the second sum form:

$$\frac{n\big[2(12) + (n-1)(3)\big]}{2} > 1000$$

$$n\big[24 + 3n - 3\big] > 2000$$

$$n(3n + 21) > 2000$$

$$3n^2 + 21n - 2000 > 0$$

Quadratic formula (Chapter 01-07):

$$n = \frac{-21 + \sqrt{441 + 4(3)(2000)}}{2(3)} = \frac{-21 + \sqrt{24{,}441}}{6}$$

$$\sqrt{24{,}441} = 156.34 \implies n = \frac{135.34}{6} = 22.56$$

Since $n$ must be a whole number of days, the total first exceeds 1000 m³ on
$\boxed{\text{day } 23}$.

**Check.** $S_{22} = \dfrac{22[24 + 21(3)]}{2} = 11(24 + 63) = 11(87) = 957$ m³
— under 1000.

$S_{23} = \dfrac{23[24 + 22(3)]}{2} = \dfrac{23(90)}{2} = 23(45) = 1035$ m³
— over 1000 ✓

> ---
> **Mentor's Margin**
>
> Part (c) is worth noticing as a pattern, not just an answer. A word problem
> about a staged process turned into a quadratic inequality, which you solved
> with the tools from Chapter 01-04 and 01-07. This is what the substrate
> tier is for. From here on, new material will mostly be new *physics*
> wrapped around algebra you already own.
>
> ---

---

## 15.4 Geometric Progressions

A **geometric progression** multiplies by a constant **common ratio** $r$ at
each step:

$$a_1, \; a_1r, \; a_1r^2, \; a_1r^3, \; \ldots$$

$$\boxed{r = \frac{a_{n+1}}{a_n} \quad \text{(same for every } n)}$$

### The $n$th term

$$\boxed{a_n = a_1 r^{\,n-1}}$$

Again the exponent is $n-1$. The first term has $r$ raised to the zero power.

### The partial sum

$$\boxed{S_n = \frac{a_1\left(1 - r^n\right)}{1 - r} \qquad (r \ne 1)}$$

An equivalent form, sometimes tidier when $r > 1$:

$$S_n = \frac{a_1\left(r^n - 1\right)}{r - 1}$$

They are the same expression with numerator and denominator both negated. Use
whichever avoids a negative in the denominator.

If $r = 1$, every term equals $a_1$ and $S_n = na_1$. The formula above
divides by zero in that case, which is the algebra telling you the progression
is not really geometric in any useful sense — it is constant.

### Behaviour of the terms

| Ratio | Term behaviour |
|---|---|
| $r > 1$ | grows without bound |
| $r = 1$ | constant |
| $0 < r < 1$ | decays toward zero, all terms positive |
| $-1 < r < 0$ | decays toward zero, alternating sign |
| $r = -1$ | alternates between $a_1$ and $-a_1$ forever |
| $r < -1$ | grows without bound, alternating sign |

![FIG-01-15-003: Two panels comparing progressions. Left panel: arithmetic progression a_n = 4 + 3(n-1) plotted as dots lying on a straight line. Right panel: geometric progression a_n = 4(1.5)^(n-1) plotted as dots on an upward-curving exponential, with a second dotted series for r = 0.6 decaying toward zero, all three labeled](../figures/FIG-01-15-003-arithmetic-vs-geometric.png)

### Worked Example 3 — Cascaded Signal Stages

**Given.** A signal enters a chain of attenuating stages at 40 mW. Each stage
passes 85% of the power it receives.

**(a)** What power leaves the sixth stage?
**(b)** How much total power has been dissipated after six stages?

**Solution.**

Define the power *entering* stage 1 as $a_1 = 40$ mW. Then the power entering
stage $n$ is $a_n = 40(0.85)^{n-1}$, and the power *leaving* stage 6 is the
power entering a hypothetical stage 7:

**(a)**

$$P_{\text{out}} = 40(0.85)^6$$

$(0.85)^2 = 0.7225$, $(0.85)^3 = 0.614125$, $(0.85)^6 = (0.614125)^2 = 0.377150$

$$P_{\text{out}} = 40(0.377150) = \boxed{15.09 \text{ mW}}$$

**(b)** Total dissipated is simply input minus output:

$$P_{\text{diss}} = 40 - 15.09 = \boxed{24.91 \text{ mW}}$$

**Cross-check with the series.** Each stage dissipates 15% of what it
receives, so the dissipations form a geometric progression with first term
$40(0.15) = 6$ mW and ratio $0.85$:

$$S_6 = \frac{6\left(1 - 0.85^6\right)}{1 - 0.85} = \frac{6(1 - 0.377150)}{0.15} = \frac{6(0.622850)}{0.15} = \frac{3.73710}{0.15} = 24.91 \text{ mW} \;\checkmark$$

Two independent routes to 24.91 mW. That agreement is the check.

> ---
> **Mentor's Margin**
>
> The indexing trap in part (a) is the single most common error in geometric
> problems. "After six stages" is $a_1 r^6$, not $a_1 r^5$, because $a_1$ is
> the value *before any stage acts*. The formula $a_n = a_1 r^{n-1}$ is
> correct as written; the trouble is deciding what $n$ means in the word
> problem. Fix it by writing out the first two or three terms explicitly and
> labelling them with the physical situation before you touch the formula.
> Five seconds of bookkeeping beats a factor of $r$ in the wrong direction.
>
> ---

---

## 15.5 Infinite Geometric Series

Now the interesting part. Add infinitely many terms of a geometric
progression:

$$a_1 + a_1r + a_1r^2 + a_1r^3 + \cdots$$

Look at the partial sum formula:

$$S_n = \frac{a_1(1 - r^n)}{1 - r}$$

If $\lvert r \rvert < 1$, then $r^n$ shrinks toward zero as $n$ grows. The
numerator settles onto $a_1(1 - 0) = a_1$, and the whole partial sum settles
onto a finite value:

$$\boxed{S_\infty = \frac{a_1}{1 - r} \qquad \text{valid only if } \lvert r \rvert < 1}$$

If $\lvert r \rvert \ge 1$, the term $r^n$ does not shrink, the partial sums
grow without bound (or oscillate forever), and the series **diverges** — no
finite sum exists.

| Condition | Behaviour | $S_\infty$ |
|---|---|---|
| $\lvert r \rvert < 1$ | **converges** | $\dfrac{a_1}{1-r}$ |
| $\lvert r \rvert \ge 1$ | **diverges** | does not exist |

![FIG-01-15-004: Two-panel convergence plot. Left: partial sums S_n for a_1 = 8, r = 0.5 plotted against n for n = 1 to 10, rising and flattening onto a horizontal dashed asymptote labeled S_infinity = 16. Right: partial sums for a_1 = 8, r = 1.2 rising steeply off the top of the frame with the label DIVERGES and no asymptote](../figures/FIG-01-15-004-geometric-convergence.png)

> **Preview note.** The phrase "settles onto" is doing real work here, and it
> is made precise by the idea of a **limit**, which is Chapter 01-16. Nothing
> in this section depends on the formal definition — the geometric formula
> above is exact and complete on its own. Chapter 01-16 will simply give a
> rigorous name to what you are seeing in the left panel of the figure.

> ---
> **Mentor's Margin**
>
> Check the convergence condition *before* you use the formula, every time.
> $S_\infty = a_1/(1-r)$ will cheerfully return a number for $r = 2$ — it
> gives $-a_1$, which is nonsense for a series of positive terms growing
> without bound. The formula has no way to warn you. You are the warning. If
> $\lvert r\rvert \ge 1$, the answer is "diverges," and on a multiple-choice
> exam that is often one of the options.
>
> Worth knowing as a fact: not every series with terms shrinking to zero
> converges. The harmonic series $1 + \frac12 + \frac13 + \frac14 + \cdots$
> has terms going to zero and still diverges. Proving that needs tools from
> Tier 1C, so take it on faith for now. It matters because it kills the
> tempting shortcut "terms get small, therefore the sum is finite." That
> shortcut is false in general. It is true for geometric series specifically,
> which is why the geometric case gets its own formula.
>
> ---

### Worked Example 4 — Total Distance of a Bouncing Ball

**Given.** A ball is dropped from 2.4 m. Each bounce returns it to 65% of its
previous peak height.

**Find.** The total vertical distance travelled before it comes to rest.

**Approach.** The initial drop is travelled once. Every bounce after that is
travelled twice — up and back down. So:

$$D = h_0 + 2\big(h_0 r + h_0 r^2 + h_0 r^3 + \cdots\big)$$

The bracketed part is an infinite geometric series with first term $h_0 r$
and ratio $r$.

**Solution.**

$h_0 = 2.4$ m, $r = 0.65$. Since $\lvert 0.65\rvert < 1$, the series
converges.

$$\sum_{\text{bounce peaks}} = \frac{h_0 r}{1 - r} = \frac{2.4(0.65)}{0.35} = \frac{1.56}{0.35} = 4.4571 \text{ m}$$

$$D = 2.4 + 2(4.4571) = 2.4 + 8.9143 = \boxed{11.31 \text{ m}}$$

**Check.** The answer must exceed the initial drop of 2.4 m, and it should be
finite despite infinitely many bounces ✓. Sanity bound: if the ball returned
to 100% height it would bounce forever and travel infinitely far; at 65% the
total is a little over four times the drop height, which is reasonable for a
moderately lossy bounce.

**Physical note.** The idealized model has infinitely many bounces in a
finite total *distance* — and, it turns out, a finite total *time*. The model
breaks down at small amplitudes where the ball simply stops, but the
geometric total is an excellent estimate of the real distance.

### Worked Example 5 — Multi-Stage Settling (Preview of Tier 2)

**Given.** Wastewater enters a train of five identical settling stages at
480 mg/L suspended solids. Each stage removes 35% of the solids reaching it.

**(a)** What concentration leaves stage 5?
**(b)** What total concentration has been removed?

**Solution.**

Each stage passes 65% of what it receives, so $r = 0.65$.

**(a)**

$$C_{\text{out}} = 480(0.65)^5$$

$(0.65)^2 = 0.4225$, $(0.65)^4 = 0.4225^2 = 0.178506$, $(0.65)^5 = 0.178506(0.65) = 0.116029$

$$C_{\text{out}} = 480(0.116029) = \boxed{55.69 \text{ mg/L}}$$

**(b)** By mass balance:

$$C_{\text{removed}} = 480 - 55.69 = \boxed{424.3 \text{ mg/L}}$$

**Cross-check with the series.** Stage-by-stage removals form a geometric
progression: first removal $= 480(0.35) = 168$ mg/L, ratio $0.65$.

$$S_5 = \frac{168\left(1 - 0.65^5\right)}{1 - 0.65} = \frac{168(1 - 0.116029)}{0.35} = \frac{168(0.883971)}{0.35} = \frac{148.507}{0.35} = 424.3 \text{ mg/L} \;\checkmark$$

> **Preview note.** Chapter 02-79 treats multi-stage separation processes
> properly, with mass balances written per stage and non-identical stage
> efficiencies. The geometric structure you just used is the special case
> where every stage has the same efficiency. Nothing here depends on that
> chapter; this is where the tool gets used.

---

## 15.6 Closed-Form Power Sums

Three sums appear often enough to memorize:

$$\boxed{\sum_{k=1}^{n} k = \frac{n(n+1)}{2}}$$

$$\boxed{\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}}$$

$$\boxed{\sum_{k=1}^{n} k^3 = \left[\frac{n(n+1)}{2}\right]^2 = \left(\sum_{k=1}^{n}k\right)^2}$$

The third is a pleasant accident: the sum of cubes is the square of the sum.

Combined with linearity, these handle any polynomial summand.

### Worked Example 6 — Polynomial Summand

**Given.** Evaluate $\displaystyle\sum_{k=1}^{20}\left(3k^2 - 2k + 5\right)$.

**Solution.** Split by linearity:

$$= 3\sum_{k=1}^{20}k^2 - 2\sum_{k=1}^{20}k + \sum_{k=1}^{20}5$$

$$\sum_{k=1}^{20}k^2 = \frac{20(21)(41)}{6} = \frac{17{,}220}{6} = 2870$$

$$\sum_{k=1}^{20}k = \frac{20(21)}{2} = 210$$

$$\sum_{k=1}^{20}5 = 20(5) = 100$$

$$= 3(2870) - 2(210) + 100 = 8610 - 420 + 100 = \boxed{8290}$$

**Check on the magnitude.** The dominant term is $3k^2$, whose average over
$k = 1$ to $20$ is roughly $3(2870)/20 = 430$ per term, giving about $8600$
before the corrections. Our answer of 8290 sits just below that ✓

---

## 15.7 Factorial Notation

For a positive integer $n$:

$$\boxed{n! = n(n-1)(n-2)\cdots(3)(2)(1)}$$

$$\boxed{0! = 1 \quad \text{(by definition)}}$$

| $n$ | $n!$ |
|---|---|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 7 | 5040 |
| 8 | 40,320 |

The useful recursive property:

$$n! = n \cdot (n-1)!$$

Use it to cancel rather than expanding. For instance:

$$\frac{10!}{8!} = \frac{10 \cdot 9 \cdot 8!}{8!} = 10 \cdot 9 = 90$$

Never compute $10! = 3{,}628{,}800$ and then divide. Cancel first.

> ---
> **Mentor's Margin**
>
> $0! = 1$ looks arbitrary and is not. It is the value that makes the
> counting formulas work without special cases — there is exactly one way to
> arrange zero objects, namely doing nothing. You will need it in Chapter
> 01-38 when combinations and permutations arrive, where $\binom{n}{n} =
> \frac{n!}{n!\,0!}$ must equal 1. Memorize it as a definition and move on.
>
> ---

---

## As the Handbook States It

> **Handbook 10.6, pp. 38–39** — *Mathematics / Progressions and Series*

The Handbook includes:

- Arithmetic progression: $n$th term and sum formulas
- Geometric progression: $n$th term and sum formulas
- Infinite geometric series sum with the $\lvert r \rvert < 1$ condition
- The closed-form power sums $\sum k$, $\sum k^2$, $\sum k^3$
- Summation notation conventions

**What's in the Handbook — find it fast:**

Both progression families with all four formulas are tabulated together, so
one lookup gets you everything. If you blank on whether the exponent is
$n$ or $n-1$, the printed formula settles it.

**What's not in the Handbook — memorize:**

- Factorial notation and $0! = 1$
- The linearity properties of summation, including
  $\sum_{k=1}^{n}c = nc$
- That a summation does **not** distribute over products or quotients
- The term count $n - m + 1$ for limits from $m$ to $n$
- The distinction between a sequence and a series
- The behaviour table for geometric terms by ratio range
- That terms shrinking to zero does not by itself guarantee convergence
  (the harmonic series counterexample)
- The procedure for identifying which physical stage corresponds to which
  index in a word problem

> ---
> **Mentor's Margin**
>
> Confirm the exact page for Progressions and Series in your copy of the
> Handbook and add it to the personal page map you started in Chapter 00-03.
> The page numbers in this guide were taken from the Handbook 10.6 table of
> contents, and the Mathematics section spans roughly pp. 36–63, so the
> subsection location is worth verifying once yourself rather than trusting
> it under time pressure.
>
> ---

---

## Where This Goes Wrong

**Off-by-one in the term formula.** Both $a_n = a_1 + (n-1)d$ and
$a_n = a_1r^{n-1}$ use $n-1$, not $n$. The first term takes zero steps from
itself. Writing $a_1r^n$ shifts your whole answer by one factor of $r$.

**Miscounting terms between limits.** $\sum_{k=3}^{9}$ has $9-3+1 = 7$ terms.
Subtracting the limits gives 6 and is wrong.

**Summing a constant as if it were one term.** $\sum_{k=1}^{n}c = nc$. The
summand does not need to contain the index for the sum to have $n$ terms.

**Distributing a summation over a product.**
$\sum a_kb_k \ne (\sum a_k)(\sum b_k)$. Only scalar multiples and
term-by-term sums separate.

**Using $S_\infty = a_1/(1-r)$ when $\lvert r\rvert \ge 1$.** The formula
returns a plausible-looking number and it is meaningless. Check the ratio
first; if $\lvert r \rvert \ge 1$, the answer is "diverges."

**Assuming shrinking terms imply a finite sum.** True for geometric series,
false in general. The harmonic series is the standard counterexample.

**Confusing the sequence with the series.** "Find the 12th term" and "find
the sum of the first 12 terms" are different questions with different
formulas. Read which one is being asked.

**Misidentifying the physical index.** In staged processes, decide explicitly
whether "after $n$ stages" means $a_n$ or $a_{n+1}$ before applying a formula.
Write out the first two terms with physical labels.

**Mixing up $d$ and $r$.** An arithmetic progression has a common
*difference* found by subtraction; a geometric one has a common *ratio* found
by division. Test which is constant before choosing a formula — compute both
$a_2 - a_1$ and $a_2/a_1$, then check against $a_3$.

**Expanding factorials before cancelling.** $\frac{12!}{10!} = 12 \times 11 =
132$. Computing $12!$ first is slow and invites arithmetic errors.

---

## Key Terms

| Term | Definition |
|---|---|
| Sequence | An ordered list of numbers; a function on the positive integers |
| Series | The sum of the terms of a sequence |
| General term $a_n$ | Formula giving the $n$th term from its index |
| Summation notation | $\sum_{k=m}^{n}a_k$; compact notation for a sum |
| Index (dummy variable) | The counter $k$ in a summation; its name carries no meaning |
| Arithmetic progression | Sequence with a constant common difference between consecutive terms |
| Common difference $d$ | $a_{n+1} - a_n$; constant for an arithmetic progression |
| Geometric progression | Sequence with a constant common ratio between consecutive terms |
| Common ratio $r$ | $a_{n+1}/a_n$; constant for a geometric progression |
| Partial sum $S_n$ | Sum of the first $n$ terms of a series |
| Convergent series | Series whose partial sums settle onto a finite value |
| Divergent series | Series whose partial sums do not settle onto a finite value |
| Factorial $n!$ | Product of all positive integers up to $n$; $0! = 1$ by definition |

---

## Review Questions

### Conceptual

1. Explain the difference between a sequence and a series. Which one does
   $S_n$ refer to?
2. Why does the arithmetic $n$th term formula use $(n-1)d$ rather than $nd$?
3. State the convergence condition for an infinite geometric series and
   explain, using the partial sum formula, why that condition is what it is.
4. A colleague argues that because the terms $\frac{1}{k}$ shrink toward
   zero, the series $\sum \frac{1}{k}$ must have a finite sum. Is the
   reasoning valid? What is the correct conclusion?
5. Given a sequence $5, 15, 45, 135, \ldots$, describe the test you would
   run to decide whether it is arithmetic, geometric, or neither.
6. A signal chain has five identical amplifier stages, each providing 6 dB of
   power gain. Explain why the gains add in decibels but the power ratios
   multiply, and identify which quantity forms an arithmetic progression and
   which forms a geometric one.
7. Why is $0!$ defined as 1 rather than 0?
8. A summation is applied to the expression $a_k b_k$. Explain why
   $\sum a_kb_k$ cannot be split into $\left(\sum a_k\right)\left(\sum
   b_k\right)$, and give a two-term numerical counterexample.

### Calculation

9. Evaluate:
   (a) $\displaystyle\sum_{k=1}^{6}(3k + 2)$
   (b) $\displaystyle\sum_{k=3}^{9}(4k + 1)$
   (c) $\displaystyle\sum_{k=1}^{15}k^2$
   (d) $\displaystyle\sum_{k=1}^{4}\left(k^3 - 2k\right)$
   (e) $\displaystyle\sum_{k=1}^{25}7$

10. An arithmetic progression has $a_1 = 7$ and $d = -3$.
    (a) Find $a_{20}$.
    (b) Find $S_{20}$.
    (c) Find the first term that is negative and state its index.

11. A geometric progression has $a_1 = 2$ and $r = 3$.
    (a) Find $a_8$.
    (b) Find $S_8$.
    (c) Does $S_\infty$ exist? Justify.

12. A geometric progression has $a_1 = 100$ and $a_5 = 6.25$, with all terms
    positive.
    (a) Find $r$.
    (b) Find $a_{10}$.
    (c) Find $S_\infty$.

13. Determine whether each infinite geometric series converges. If it does,
    find its sum.
    (a) $18 + 6 + 2 + \cdots$
    (b) $5 - 10 + 20 - 40 + \cdots$
    (c) $9 - 3 + 1 - \tfrac13 + \cdots$
    (d) $4 + 4.4 + 4.84 + \cdots$

14. Compare growth. For $a_1 = 2$ in both cases, an arithmetic progression has
    $d = 5$ and a geometric progression has $r = 1.5$.
    (a) Compute $S_{10}$ for each. Which is larger?
    (b) Compute $S_{12}$ for each. Which is larger now?
    (c) Explain the reversal in one sentence.

15. Simplify without expanding the factorials:
    (a) $\dfrac{12!}{10!}$
    (b) $\dfrac{8!}{3!\,5!}$
    (c) $\dfrac{(n+1)!}{(n-1)!}$

16. **Engineering application.** A pile-driving log records 42 mm of
    penetration on the first blow, decreasing by 2 mm on each subsequent
    blow.
    (a) Write the general term.
    (b) How deep is the pile after 15 blows?
    (c) On which blow does the model predict zero penetration, and what does
    that tell you about the model's range of validity?

17. **Engineering application.** A five-stage aeration train receives water
    containing 620 mg/L of a volatile compound. Each stage strips 28% of the
    compound reaching it.
    (a) What concentration leaves the final stage?
    (b) What total concentration was stripped?
    (c) Verify (b) by summing the stage-by-stage removals as a geometric
    series.
    (d) How many stages would be needed to reach 100 mg/L or below?

18. **Engineering application (economics preview).** An annual payment of
    \$5000 is made at the end of each year for 8 years. At an interest rate
    of 6% per year, the present worth of the payment made at the end of year
    $k$ is $5000(1.06)^{-k}$.
    (a) Show that the eight present worths form a geometric progression and
    identify $a_1$ and $r$.
    (b) Compute the total present worth using the finite geometric sum
    formula.
    (c) Confirm your result matches the standard form
    $P = A\dfrac{1 - (1+i)^{-n}}{i}$.

### Multiple Choice

19. The 12th term of the sequence $5, 9, 13, 17, \ldots$ is:
    A) 45
    B) 49
    C) 53
    D) 48

20. $\displaystyle\sum_{k=1}^{30}k$ equals:
    A) 435
    B) 450
    C) 465
    D) 930

21. The 5th term of a geometric progression with $a_1 = 3$ and $r = -2$ is:
    A) $-48$
    B) 48
    C) $-96$
    D) 96

22. The sum $8 + 4 + 2 + 1 + \cdots$ equals:
    A) 15
    B) 16
    C) 32
    D) Diverges

23. Which infinite geometric series diverges?
    A) $a_1 = 10$, $r = 0.95$
    B) $a_1 = 10$, $r = -0.5$
    C) $a_1 = 10$, $r = 1.05$
    D) $a_1 = 100$, $r = 0.01$

24. $\displaystyle\sum_{k=1}^{n}c$, where $c$ is a constant, equals:
    A) $c$
    B) $nc$
    C) $c^n$
    D) $\dfrac{n(n+1)c}{2}$

25. $6!$ equals:
    A) 120
    B) 360
    C) 720
    D) 5040

26. Which formula gives the sum of the first $n$ terms of an arithmetic
    progression?
    A) $\dfrac{a_1(1-r^n)}{1-r}$
    B) $a_1 + (n-1)d$
    C) $\dfrac{n(a_1 + a_n)}{2}$
    D) $\dfrac{a_1}{1-r}$

---

## Answer Key with Explanations

**1.** A **sequence** is an ordered list of numbers; a **series** is the sum
of those numbers. $S_n$ refers to the series — specifically the sum of the
first $n$ terms of the sequence. The sequence $2, 4, 6, 8$ has fourth term
$a_4 = 8$; the corresponding series has $S_4 = 20$. Different questions,
different formulas. (§15.1)

**2.** Because the first term requires zero steps of size $d$. Going from
$a_1$ to $a_2$ is one step, to $a_3$ is two steps, and to $a_n$ is $n-1$
steps. Substituting $n = 1$ into $a_1 + (n-1)d$ gives $a_1 + 0 = a_1$ ✓,
whereas $a_1 + nd$ would give $a_1 + d$, which is the second term. (§15.3)

**3.** Converges if and only if $\lvert r \rvert < 1$, and then
$S_\infty = a_1/(1-r)$.

From the partial sum $S_n = \dfrac{a_1(1-r^n)}{1-r}$, the only $n$-dependence
is the $r^n$ term. When $\lvert r\rvert < 1$, repeated multiplication by a
factor smaller than 1 in magnitude drives $r^n$ toward zero, so the numerator
settles onto $a_1$ and the whole expression settles onto $a_1/(1-r)$. When
$\lvert r\rvert > 1$, $r^n$ grows without bound and so does $S_n$. When
$r = 1$ the formula is undefined and every term equals $a_1$, so
$S_n = na_1$ grows without bound. When $r = -1$ the partial sums oscillate
between $a_1$ and 0 forever and never settle. (§15.5)

**4.** The reasoning is **not valid**. Terms shrinking toward zero is
necessary for convergence but not sufficient. The harmonic series
$\sum \frac{1}{k}$ is the standard counterexample: its terms go to zero and
it diverges anyway. The correct conclusion is that you cannot decide
convergence from term behaviour alone in general. Geometric series are the
special case where the ratio condition settles it completely, which is why
they get their own formula. (§15.5)

**5.** Compute both the successive difference and the successive ratio, then
check whether either is constant across more than one pair.

Differences: $15-5 = 10$, $45-15 = 30$. Not constant → not arithmetic.

Ratios: $15/5 = 3$, $45/15 = 3$, $135/45 = 3$. Constant → **geometric** with
$r = 3$.

Checking two pairs rather than one matters: a single pair cannot distinguish
the two patterns. (§15.3, §15.4)

**6.** Decibels are logarithmic (Chapter 01-05): a power ratio $G$
corresponds to $10\log_{10}G$ dB. Cascaded stages multiply power ratios, and
the logarithm of a product is the sum of the logarithms, so the dB values
add.

The **dB gains** form an arithmetic progression: cumulative gain after $n$
stages is $6n$ dB — a constant 6 dB added per stage.

The **power ratios** form a geometric progression: each 6 dB corresponds to a
power factor of $10^{0.6} = 3.981$, so cumulative ratio after $n$ stages is
$(3.981)^n$ — a constant factor multiplied per stage.

For five stages: 30 dB total, a power ratio of $10^{3.0} = 1000$.
(§15.3, §15.4)

**7.** Because it is the value that makes the counting and series formulas
work without special-casing. There is exactly one arrangement of zero
objects — do nothing — so the count is 1, not 0. It also preserves the
recursion $n! = n(n-1)!$ at $n=1$: $1! = 1 \cdot 0! = 1 \cdot 1 = 1$ ✓. If
$0!$ were 0, that recursion and every combination formula containing $0!$ in
a denominator would break. (§15.7)

**8.** Because a summation is repeated addition, and addition does not
distribute over multiplication. Expanding both sides makes the mismatch
plain: the left side contains only the "matched" products $a_1b_1 + a_2b_2$,
while the right side contains all cross terms $a_1b_1 + a_1b_2 + a_2b_1 +
a_2b_2$.

Counterexample with $a_k = b_k = k$ and $n = 2$:

$$\sum_{k=1}^{2}k \cdot k = 1 + 4 = 5$$

$$\left(\sum_{k=1}^{2}k\right)\left(\sum_{k=1}^{2}k\right) = (3)(3) = 9$$

$5 \ne 9$. (§15.2)

**9.**

(a) $3\sum_{k=1}^{6}k + \sum_{k=1}^{6}2 = 3\left(\frac{6 \cdot 7}{2}\right) +
6(2) = 3(21) + 12 = \boxed{75}$

(b) Terms for $k = 3$ to $9$: $13, 17, 21, 25, 29, 33, 37$. Arithmetic with
$n = 9 - 3 + 1 = 7$ terms.

$$S = \frac{7(13 + 37)}{2} = \frac{7(50)}{2} = \boxed{175}$$

(c) $\dfrac{15(16)(31)}{6} = \dfrac{7440}{6} = \boxed{1240}$

(d) $\sum_{k=1}^{4}k^3 - 2\sum_{k=1}^{4}k = \left[\frac{4 \cdot 5}{2}\right]^2
- 2\left(\frac{4 \cdot 5}{2}\right) = 100 - 20 = \boxed{80}$

Verify term by term: $(1-2)+(8-4)+(27-6)+(64-8) = -1+4+21+56 = 80$ ✓

(e) $25(7) = \boxed{175}$

**10.**

(a) $a_{20} = 7 + 19(-3) = 7 - 57 = \boxed{-50}$

(b) $S_{20} = \dfrac{20(7 + (-50))}{2} = 10(-43) = \boxed{-430}$

(c) Set $a_n < 0$: $7 + (n-1)(-3) < 0 \implies 7 - 3n + 3 < 0 \implies
10 < 3n \implies n > 3.33$

First negative term is at $n = 4$: $a_4 = 7 + 3(-3) = 7 - 9 = \boxed{-2}$

Check $a_3 = 7 + 2(-3) = 1 > 0$ ✓

**11.**

(a) $a_8 = 2(3)^7 = 2(2187) = \boxed{4374}$

(b) $S_8 = \dfrac{2\left(1 - 3^8\right)}{1 - 3} = \dfrac{2(1 - 6561)}{-2} =
\dfrac{2(-6560)}{-2} = \boxed{6560}$

(c) **No.** $\lvert r \rvert = 3 \ge 1$, so the series diverges. The terms
grow without bound and no finite sum exists.

**12.**

(a) $a_5 = a_1r^4 \implies 6.25 = 100r^4 \implies r^4 = 0.0625$

$r = \pm(0.0625)^{1/4} = \pm 0.5$. All terms positive requires $r = \boxed{0.5}$

(b) $a_{10} = 100(0.5)^9 = \dfrac{100}{512} = \boxed{0.1953}$

(c) $\lvert 0.5\rvert < 1$, so it converges:

$$S_\infty = \frac{100}{1 - 0.5} = \boxed{200}$$

**13.**

(a) $r = 6/18 = 1/3$. $\lvert r\rvert < 1$ → **converges**.

$$S_\infty = \frac{18}{1 - 1/3} = \frac{18}{2/3} = \boxed{27}$$

(b) $r = -10/5 = -2$. $\lvert r\rvert = 2 \ge 1$ → **diverges**. No sum.

(c) $r = -3/9 = -1/3$. $\lvert r\rvert < 1$ → **converges**.

$$S_\infty = \frac{9}{1 - (-1/3)} = \frac{9}{4/3} = \boxed{6.75}$$

(d) $r = 4.4/4 = 1.1$. $\lvert r\rvert \ge 1$ → **diverges**. No sum.

**14.**

(a) Arithmetic, $a_1 = 2$, $d = 5$:

$a_{10} = 2 + 9(5) = 47$, so $S_{10} = \dfrac{10(2 + 47)}{2} = 5(49) = 245$

Geometric, $a_1 = 2$, $r = 1.5$: $1.5^{10} = 57.665$

$$S_{10} = \frac{2\left(1 - 57.665\right)}{1 - 1.5} = \frac{2(-56.665)}{-0.5} = 226.66$$

**Arithmetic is larger** at $n = 10$: $245 > 226.66$

(b) $a_{12} = 2 + 11(5) = 57$, so $S_{12} = \dfrac{12(2+57)}{2} = 6(59) = 354$

$1.5^{12} = 129.746$

$$S_{12} = \frac{2(1 - 129.746)}{-0.5} = \frac{2(-128.746)}{-0.5} = 514.98$$

**Geometric is larger** at $n = 12$: $514.98 > 354$

(c) Geometric growth eventually overtakes arithmetic growth no matter how
large the common difference, because a constant multiplicative factor
compounds while a constant additive increment does not.

**15.**

(a) $\dfrac{12!}{10!} = 12 \cdot 11 = \boxed{132}$

(b) $\dfrac{8!}{3!\,5!} = \dfrac{8 \cdot 7 \cdot 6 \cdot 5!}{6 \cdot 5!} =
\dfrac{336}{6} = \boxed{56}$

(c) $\dfrac{(n+1)!}{(n-1)!} = \dfrac{(n+1)(n)(n-1)!}{(n-1)!} =
\boxed{n(n+1)}$

**16.**

(a) Arithmetic with $a_1 = 42$ mm, $d = -2$ mm:

$$a_n = 42 - 2(n-1) = \boxed{44 - 2n \text{ mm}}$$

(b) $a_{15} = 44 - 30 = 14$ mm

$$S_{15} = \frac{15(42 + 14)}{2} = \frac{15(56)}{2} = 15(28) = \boxed{420 \text{ mm}}$$

(c) Set $a_n = 0$: $44 - 2n = 0 \implies n = 22$.

The model predicts zero penetration on blow 22 and **negative** penetration
after that, which is physically impossible — a pile does not rise out of the
ground when struck. The linear-decrease model is therefore valid only for
roughly the first 20 blows. Real driving resistance approaches an asymptote
rather than crossing zero, so an exponential-decay (geometric) model is
usually the better long-run description. This is exactly the
physics-extraneous root situation from Chapter 01-07: the algebra returns a
value the physics rejects.

**17.**

Each stage passes $1 - 0.28 = 0.72$, so $r = 0.72$.

(a) $(0.72)^2 = 0.5184$, $(0.72)^4 = 0.5184^2 = 0.268739$,
$(0.72)^5 = 0.268739(0.72) = 0.193492$

$$C_{\text{out}} = 620(0.193492) = \boxed{120.0 \text{ mg/L}}$$

(b) $C_{\text{stripped}} = 620 - 120.0 = \boxed{500.0 \text{ mg/L}}$

(c) Stage-by-stage removals are geometric with $a_1 = 620(0.28) = 173.6$ mg/L
and $r = 0.72$:

$$S_5 = \frac{173.6\left(1 - 0.72^5\right)}{1 - 0.72} = \frac{173.6(1 - 0.193492)}{0.28} = \frac{173.6(0.806508)}{0.28}$$

$$= \frac{140.010}{0.28} = 500.0 \text{ mg/L} \;\checkmark$$

Agrees with (b).

(d) Require $620(0.72)^n \le 100$:

$$(0.72)^n \le 0.161290$$

Take natural logs (Chapter 01-05), remembering that $\ln(0.72) < 0$ so the
inequality reverses on division:

$$n \ge \frac{\ln(0.161290)}{\ln(0.72)} = \frac{-1.8245}{-0.3285} = 5.554$$

$$\boxed{n = 6 \text{ stages}}$$

Check: $620(0.72)^6 = 620(0.139314) = 86.4$ mg/L ≤ 100 ✓, while five stages
gave 120.0 mg/L > 100.

**18.**

(a) The present worths are:

$$5000(1.06)^{-1}, \; 5000(1.06)^{-2}, \; \ldots, \; 5000(1.06)^{-8}$$

Each is the previous one multiplied by $(1.06)^{-1}$, so this is geometric
with

$$a_1 = \frac{5000}{1.06} = 4716.98 \qquad r = \frac{1}{1.06} = 0.943396$$

(b) $1.06^8$: $1.06^2 = 1.1236$, $1.06^4 = 1.1236^2 = 1.262477$,
$1.06^8 = 1.262477^2 = 1.593848$

So $r^8 = (1.06)^{-8} = 0.627412$.

$$S_8 = \frac{4716.98\left(1 - 0.627412\right)}{1 - 0.943396} = \frac{4716.98(0.372588)}{0.056604}$$

$$= \frac{1757.53}{0.056604} = \boxed{\$31{,}049}$$

(c) Standard form:

$$P = 5000\,\frac{1 - (1.06)^{-8}}{0.06} = 5000\,\frac{0.372588}{0.06} = 5000(6.20980) = \$31{,}049 \;\checkmark$$

The two agree exactly, because the standard annuity formula *is* the finite
geometric sum with $a_1 = A/(1+i)$ and $r = 1/(1+i)$, algebraically
rearranged. The engineering-economics factor tables you will meet in Chapter
02-74 are tabulated values of $\frac{1-(1+i)^{-n}}{i}$ — nothing more than
this geometric series.

**19. B — 49.** Arithmetic with $a_1 = 5$, $d = 4$.
$a_{12} = 5 + 11(4) = 5 + 44 = 49$. Choice D, 48, is the classic off-by-one
from using $12d$ instead of $11d$... which actually gives 53 (choice C).
Choice A comes from $a_1 = 5$ with $d = 4$ and only 10 steps. (§15.3)

**20. C — 465.** $\sum_{k=1}^{30}k = \dfrac{30(31)}{2} = \dfrac{930}{2} = 465$.
Choice D is the un-halved $n(n+1)$. (§15.6)

**21. B — 48.** $a_5 = 3(-2)^4 = 3(16) = 48$. The exponent is $n-1 = 4$, which
is even, so the sign is positive. Choice A, $-48$, comes from using an odd
exponent; choice D, 96, from $n = 5$ as the exponent. (§15.4)

**22. B — 16.** Geometric with $a_1 = 8$, $r = 0.5$. Since
$\lvert r\rvert < 1$ it converges:
$S_\infty = \dfrac{8}{1 - 0.5} = 16$. (§15.5)

**23. C — $a_1 = 10$, $r = 1.05$.** Only this option has
$\lvert r\rvert \ge 1$. Note that A converges despite $r$ being very close to
1 — the sum is $10/0.05 = 200$, large but finite. B converges with an
alternating sign: $10/1.5 = 6.67$. (§15.5)

**24. B — $nc$.** The summand contains no index, so you add the constant $c$
a total of $n$ times. Choice A treats it as a single term; choice D is
$c\sum k$, which would be correct only if the summand were $ck$. (§15.2)

**25. C — 720.** $6! = 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 720$.
Choice A is $5!$; choice D is $7!$. (§15.7)

**26. C — $\dfrac{n(a_1+a_n)}{2}$.** Choice A is the finite geometric sum,
choice B is the arithmetic $n$th term (not a sum), and choice D is the
infinite geometric sum. Reading the question for "sum" versus "term" is the
whole task here. (§15.3)

---

## Quick Reference

**Summation notation** — *Handbook p. 38*

$$\sum_{k=m}^{n} a_k \qquad \text{number of terms} = n - m + 1$$

$$\sum c\,a_k = c\sum a_k \qquad \sum(a_k \pm b_k) = \sum a_k \pm \sum b_k \qquad \sum_{k=1}^{n} c = nc$$

Does **not** distribute over products or quotients.

**Arithmetic progression** — *Handbook p. 38*

$$d = a_{n+1} - a_n \qquad a_n = a_1 + (n-1)d$$

$$S_n = \frac{n(a_1 + a_n)}{2} = \frac{n\big[2a_1 + (n-1)d\big]}{2}$$

**Geometric progression** — *Handbook p. 38*

$$r = \frac{a_{n+1}}{a_n} \qquad a_n = a_1 r^{\,n-1}$$

$$S_n = \frac{a_1\left(1 - r^n\right)}{1 - r} \qquad (r \ne 1)$$

$$S_\infty = \frac{a_1}{1 - r} \qquad \text{only if } \lvert r \rvert < 1$$

**Convergence test for geometric series**

| $\lvert r \rvert$ | Result |
|---|---|
| $< 1$ | converges to $a_1/(1-r)$ |
| $\ge 1$ | diverges — no finite sum |

Shrinking terms alone do **not** guarantee convergence (harmonic series).

**Power sums** — *Handbook p. 39*

$$\sum_{k=1}^{n}k = \frac{n(n+1)}{2} \qquad \sum_{k=1}^{n}k^2 = \frac{n(n+1)(2n+1)}{6} \qquad \sum_{k=1}^{n}k^3 = \left[\frac{n(n+1)}{2}\right]^2$$

$$\sum_{k=1}^{n}(2k-1) = n^2$$

**Factorials**

$$n! = n(n-1)! \qquad 0! = 1$$

$$1,\;1,\;2,\;6,\;24,\;120,\;720,\;5040,\;40{,}320 \quad (n = 0 \ldots 8)$$

Cancel before expanding: $\dfrac{12!}{10!} = 12 \cdot 11 = 132$.

**Not in the Handbook — memorize**

Factorial notation and $0! = 1$ · summation linearity including
$\sum c = nc$ · non-distribution over products · term count $n-m+1$ ·
sequence versus series distinction · geometric term behaviour by ratio range ·
shrinking terms do not imply convergence · index-to-stage mapping procedure
for word problems

---

## What's Next

Apprentice, that closes Tier 1B. Take stock of what you now hold: algebra,
functions, polynomials and their roots, linear systems, analytic geometry,
mensuration, trigonometry, complex numbers, vectors, matrices and
eigenvalues, and now sequences and series. That is the complete algebraic and
geometric substrate. Every remaining chapter in this guide builds on it and
nothing else precedes it.

Before moving on, take the **Tier 1B review exam** in the appendices. It runs
across all twelve chapters of this tier, and it is the checkpoint that
matters — Tier 1C assumes fluency, not familiarity, with everything above.

In **Chapter 01-16: Limits and Continuity**, Tier 1C opens with the idea you
have been circling for two chapters. When we said the partial sums of a
convergent geometric series "settle onto" $a_1/(1-r)$, and when we sketched
asymptotes in Chapter 01-06, we were describing limits without defining them.
Chapter 01-16 defines the limit precisely, and everything in calculus follows
from it: the derivative is a limit of slopes, the integral is a limit of
sums. Those sums will be the ones you just learned to write with sigma
notation.

Bring the Handbook to page 45. Differential calculus begins there.

See you there.

— Your Mentor