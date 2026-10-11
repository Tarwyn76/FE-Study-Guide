---
chapter: "01-04"
title: "Expressions, Equations, and Inequalities"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-004-01, MATH-1B-004-02, MATH-1B-004-03]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-04: Expressions, Equations, and Inequalities

> *"You will spend more time manipulating algebra on this exam than doing
> any other single thing. Not because the exam is about algebra — it isn't.
> But because every equation in every discipline is algebra with physics
> poured in. Get the algebra automatic and the physics is all that's left
> to think about."*

---

## Before You Start

**Prerequisites:** [01-01 Numbers, Magnitude, and Metric Prefixes](01-01-numbers-magnitude-prefixes.md) · [01-02 Units, Dimensions, and the Pound Problem](01-02-units-dimensions-pound-problem.md) · [01-03 Accuracy, Precision, and Significant Figures](01-03-accuracy-precision-significant-figures.md)

**Skip if:** You pass the Tier 1B test-out quiz. If you're skipping, make
sure §4.5 on absolute value equations and §4.6 on inequalities read as
familiar — those are the places most people have gaps.

**Time:** ~55 min read · ~25 min review questions · ~55 min practice problems

---

## On the Board Today

Apprentice, algebra is infrastructure. It doesn't appear on the exam as its
own category — there are no chapters in any FE specification labeled
"Algebra." But every statics problem, every circuit problem, every
thermodynamics problem requires you to set up and solve equations. You can
know the physics perfectly and lose points because you made a sign error on
a two-variable system.

This chapter and the five that follow build the algebraic toolkit that every
downstream chapter assumes you have. We're not doing it slowly because it's
hard — we're doing it completely because completeness is the whole point.
A gap in here shows up as an error in chapter 47.

Two things I want you to come out of this chapter able to do automatically:

**Rearrange any equation for any variable without arithmetic errors.** Not
"solve for $x$ when $x$ is alone on one side" — solve for any term in any
position. The exam will hand you $F = ma/g_c$ and ask for $g_c$. Or ask you
to isolate $\mu_k$ from $F_f = \mu_k N$. Or find $R_2$ given
$V_{out}/V_{in} = R_2/(R_1 + R_2)$. These require confident, mechanical
algebraic manipulation.

**Handle inequalities without flipping the sign by accident.** The
multiplication-by-negative rule is the one that fails quietly: the answer
looks plausible, it's just on the wrong side of the inequality. We'll
practice it until it's impossible to miss.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 4.1 Distinguish an expression from an equation from an inequality
* 4.2 Apply the properties of real numbers to simplify expressions
* 4.3 Expand and factor algebraic expressions including difference of
  squares and perfect square trinomials
* 4.4 Isolate any variable in a multi-term equation using legal operations
* 4.5 Solve equations involving absolute values
* 4.6 Solve linear inequalities and express solutions on a number line
  and in interval notation
* 4.7 Solve compound inequalities
* 4.8 Set up an algebraic equation from a physical relationship and solve
  for a specified variable

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $a, b, c$ | constants or known coefficients | — |
| $x, y, z$ | unknown variables | — |
| $\lvert x \rvert$ | absolute value of $x$ | introduced in 01-01 |
| $\in$ | "is an element of" | $x \in \mathbb{R}$ means $x$ is a real number |
| $\mathbb{R}$ | the set of all real numbers | — |
| $(a, b)$ | open interval, $a < x < b$ | endpoints excluded |
| $[a, b]$ | closed interval, $a \le x \le b$ | endpoints included |
| $(a, b]$ | half-open, $a < x \le b$ | — |
| $\infty$ | infinity | not a number; used in interval notation |

No collisions with later chapters. These symbols carry these meanings
throughout the guide.

---

## 4.1 Three Things That Look Similar and Aren't

### Expression

A combination of numbers, variables, and operations. It has a value — or
a range of values — but it makes no claim of equality.

$$3x^2 - 5x + 2 \qquad \frac{a + b}{c} \qquad \sqrt{F_W^2 + F_H^2}$$

You simplify an expression. You don't solve it, because there's nothing to
solve for — no equals sign makes a claim.

### Equation

A statement that two expressions are equal. It may be true, false, or true
only for specific values of the variable.

$$3x^2 - 5x + 2 = 0 \qquad \frac{V}{R} = I \qquad F = \frac{ma}{g_c}$$

You solve an equation for a variable, or rearrange it to isolate a different
variable.

### Inequality

A statement that one expression is greater than, less than, or in a bounded
relationship with another.

$$x > 5 \qquad P \le P_{max} \qquad -10 < T < 150$$

You solve an inequality for a range of values, not a single value.

> ---
> **Mentor's Margin**
>
> The distinction matters operationally. An equation has a solution set that
> may be zero, one, or several specific numbers. An inequality has a solution
> set that is an interval or union of intervals — usually infinitely many
> numbers. Treating an inequality like an equation (solving for a single
> value) is a category error, and the Tier 2 chapters on design and safety
> — where tolerances, allowable stresses, and operating limits live — are
> full of inequalities.
>
> ---

---

## 4.2 Properties of Real Numbers

These are the rules your algebra stands on. Most of them you use
automatically; naming them makes it possible to catch the rare case where
you break one.

| Property | Statement | Example |
|---|---|---|
| **Commutative (add)** | $a + b = b + a$ | $3 + x = x + 3$ |
| **Commutative (mult)** | $ab = ba$ | $4x = x \cdot 4$ |
| **Associative (add)** | $(a+b)+c = a+(b+c)$ | Group additions freely |
| **Associative (mult)** | $(ab)c = a(bc)$ | Group multiplications freely |
| **Distributive** | $a(b+c) = ab + ac$ | The workhorse |
| **Identity (add)** | $a + 0 = a$ | Zero adds nothing |
| **Identity (mult)** | $a \cdot 1 = a$ | One multiplies nothing |
| **Inverse (add)** | $a + (-a) = 0$ | Opposites cancel |
| **Inverse (mult)** | $a \cdot \dfrac{1}{a} = 1$ | Reciprocals cancel |
| **Zero product** | $a \cdot 0 = 0$ | Any factor of zero kills the product |

> ---
> **Mentor's Margin**
>
> The zero product property is worth naming explicitly because it's the
> foundation of factoring to solve equations: if $AB = 0$, then $A = 0$ or
> $B = 0$. We'll use this in Chapter 01-07 on polynomials and throughout
> the guide whenever a product of terms equals zero.
>
> ---

### Like terms

Terms are **like terms** when they have exactly the same variable part —
same variables raised to the same powers.

$$3x^2 \text{ and } -7x^2 \quad \checkmark \quad \text{like terms, both } x^2$$
$$3x^2 \text{ and } 3x \quad \times \quad \text{not like — different exponents}$$
$$5xy \text{ and } 2yx \quad \checkmark \quad \text{like — by commutativity, }xy = yx$$

Only like terms can be combined by addition or subtraction.

$$3x^2 + 7x - 5x^2 + 2 - 3x = (3-5)x^2 + (7-3)x + 2 = -2x^2 + 4x + 2$$

---

## 4.3 Expansion and Factoring

Two operations that are inverses of each other. Expansion opens up a
product. Factoring closes it back.

### Expansion using the distributive property

$$a(b + c + d) = ab + ac + ad$$

$$(a + b)(c + d) = ac + ad + bc + bd$$

The second one is called **FOIL** (First, Outer, Inner, Last) in some
curricula. I'd rather you use "distribute each term of the first factor
across the second" — it generalizes to three or more terms, FOIL doesn't.

### Three special products worth knowing cold

These appear in factored and expanded forms throughout the guide. Recognize
both.

**Difference of squares:**

$$\boxed{a^2 - b^2 = (a+b)(a-b)}$$

**Perfect square trinomial (positive):**

$$\boxed{(a+b)^2 = a^2 + 2ab + b^2}$$

**Perfect square trinomial (negative):**

$$\boxed{(a-b)^2 = a^2 - 2ab + b^2}$$

> ---
> **Mentor's Margin**
>
> The perfect square trinomial is the one people mis-expand most often.
> $(a + b)^2 \ne a^2 + b^2$. That missing middle term $2ab$ has derailed
> countless problems. If you remember only one algebraic identity from this
> chapter, remember that $(a + b)^2$ has three terms, not two. Burn it in.
>
> ---

### Factoring strategies

**Greatest common factor (GCF) first.** Always look for a common factor
before anything else.

$$6x^3 - 4x^2 + 2x = 2x(3x^2 - 2x + 1)$$

**Factor a trinomial $x^2 + bx + c$.** Find two numbers that multiply to
$c$ and add to $b$.

$$x^2 + 5x + 6 = (x+2)(x+3) \quad \text{since } 2 \times 3 = 6, \; 2+3=5$$

**Factor by difference of squares.**

$$4x^2 - 25 = (2x)^2 - 5^2 = (2x+5)(2x-5)$$

**Factor a perfect square trinomial.**

$$x^2 - 10x + 25 = (x-5)^2 \quad \text{since } 5^2 = 25, \; 2(5) = 10$$

### Worked Example 1 — Expansion and Factoring

**Given.** (a) Expand $(3x - 2)^2$. (b) Factor $9y^2 - 6y + 1$. (c) Factor
$16t^2 - 49$.

**Solution.**

(a) Apply the perfect square trinomial formula with $a = 3x$, $b = 2$:

$$(3x - 2)^2 = (3x)^2 - 2(3x)(2) + 2^2 = 9x^2 - 12x + 4$$

**Check:** $(3x-2)(3x-2)$ by FOIL: $9x^2 - 6x - 6x + 4 = 9x^2 - 12x + 4$ ✓

(b) $9y^2 - 6y + 1$: check for perfect square. $\sqrt{9y^2} = 3y$,
$\sqrt{1} = 1$, and $2(3y)(1) = 6y$ — that's the middle term.

$$9y^2 - 6y + 1 = (3y - 1)^2$$

**Check:** $(3y-1)^2 = 9y^2 - 6y + 1$ ✓

(c) Difference of squares: $16t^2 = (4t)^2$, $49 = 7^2$.

$$16t^2 - 49 = (4t + 7)(4t - 7)$$

**Check:** $(4t+7)(4t-7) = 16t^2 - 28t + 28t - 49 = 16t^2 - 49$ ✓

---

## 4.4 Solving Equations — Isolating a Variable

An equation is solved by applying operations that preserve equality. The
governing principle:

> **Whatever you do to one side, you must do to the other.**

Allowed operations:
- Add or subtract the same quantity from both sides
- Multiply or divide both sides by the same **non-zero** quantity
- Take the same function of both sides (square root, square, etc.) — but
  watch for extraneous solutions

### The systematic approach

1. Simplify each side if possible (expand, combine like terms, clear
   fractions)
2. Get all terms involving the target variable on one side
3. Get all other terms on the other side
4. Isolate the variable by dividing, taking roots, or whatever the structure
   requires
5. **Verify** by substituting back into the original equation

That last step. Always. An algebra error in step 2 or 3 produces a clean-
looking "answer" that fails on substitution.

### Worked Example 2 — Single Variable, Linear

**Given.** Solve for $x$: $\quad 3(2x - 4) = 5x + 9$

**Solution.**

Step 1 — Expand:

$$6x - 12 = 5x + 9$$

Step 2 — Collect $x$ terms on the left:

$$6x - 5x = 9 + 12$$

Step 3 — Simplify:

$$x = 21$$

**Verify:** $3(2 \cdot 21 - 4) = 3(38) = 114$. And $5(21) + 9 = 105 + 9 =
114$. ✓

### Worked Example 3 — Rearranging for a Specified Variable

This is the exam skill: rearrange a physics equation for a non-obvious
variable.

**Given.** The voltage divider relation is

$$V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}$$

Solve for $R_1$.

**Approach.** Treat $R_1$ as the unknown. Every other letter is a known
constant for purposes of this rearrangement.

**Solution.**

Step 1 — Multiply both sides by $(R_1 + R_2)$:

$$V_{out}(R_1 + R_2) = V_{in} \cdot R_2$$

Step 2 — Expand:

$$V_{out} R_1 + V_{out} R_2 = V_{in} R_2$$

Step 3 — Isolate the $R_1$ term:

$$V_{out} R_1 = V_{in} R_2 - V_{out} R_2$$

Step 4 — Factor the right side:

$$V_{out} R_1 = R_2(V_{in} - V_{out})$$

Step 5 — Divide:

$$\boxed{R_1 = \frac{R_2(V_{in} - V_{out})}{V_{out}}}$$

**Verify.** Substitute $R_1$ back and confirm you recover $V_{out}$. With
numbers: take $V_{in} = 12$ V, $V_{out} = 4$ V, $R_2 = 6$ kΩ.

$$R_1 = \frac{6(12 - 4)}{4} = \frac{6 \times 8}{4} = 12 \text{ k}\Omega$$

$$V_{out} = 12 \cdot \frac{6}{12 + 6} = 12 \cdot \frac{6}{18} = 12 \cdot \frac{1}{3} = 4 \text{ V} \;\checkmark$$

> ---
> **Mentor's Margin**
>
> Notice that Step 4 — factoring $R_2$ out of the right side — is the step
> people skip. Without it, you'd have $V_{out}R_1 = V_{in}R_2 - V_{out}R_2$
> and might try to divide by $V_{out}$ to get $R_1 = V_{in}R_2/V_{out} - R_2$,
> which is correct but ugly. Factoring first gives you a cleaner, more
> verifiable form. In a longer calculation, cleaner forms catch more errors.
>
> ---

### Worked Example 4 — Clearing Fractions First

Equations with multiple fractions become much easier when you multiply
through by the common denominator before solving.

**Given.** Solve for $x$:

$$\frac{x}{3} - \frac{x-2}{4} = 1$$

**Solution.**

Step 1 — LCD of 3 and 4 is 12. Multiply every term by 12:

$$12 \cdot \frac{x}{3} - 12 \cdot \frac{x-2}{4} = 12 \cdot 1$$

$$4x - 3(x - 2) = 12$$

Step 2 — Expand:

$$4x - 3x + 6 = 12$$

Step 3 — Simplify and solve:

$$x + 6 = 12 \implies x = 6$$

**Verify:** $\dfrac{6}{3} - \dfrac{6-2}{4} = 2 - 1 = 1$ ✓

### Worked Example 5 — Physics Equation, Explicit Solve

**Given.** From the ideal gas law:

$$pV = mRT$$

Solve for $T$. Then given $p = 150 \text{ kPa}$, $V = 2.0 \text{ m}^3$,
$m = 3.5 \text{ kg}$, and $R = 0.287 \text{ kJ/(kg·K)}$, find $T$ in
kelvin.

**Solution.**

Divide both sides by $mR$:

$$T = \frac{pV}{mR}$$

Substitute, keeping units:

$$T = \frac{(150 \text{ kPa})(2.0 \text{ m}^3)}{(3.5 \text{ kg})(0.287 \text{ kJ/(kg·K)})}$$

Note: $1 \text{ kPa} \cdot \text{m}^3 = 1 \text{ kJ}$, so the units work out:

$$T = \frac{300 \text{ kJ}}{1.0045 \text{ kJ/K}} = 298.6 \text{ K}$$

$$\boxed{T \approx 299 \text{ K} \approx 26 \; ^\circ\text{C}}$$

**Check.** Room temperature is about 293 K. A pressure of 150 kPa is slightly
above atmospheric at 101 kPa, and the volume of 2.0 m³ with 3.5 kg of air is
consistent with near-room conditions. ✓

> ---
> **Mentor's Margin**
>
> The specific gas constant $R = 0.287$ kJ/(kg·K) is for air. The ideal gas
> law and the gas constant appear in Tier 2D and in many FE problems. Know
> that this constant exists, that its value for air is approximately 0.287,
> and that you need it in the right units for whatever unit system the problem
> uses. The full treatment is in Chapter 01-02 (four forms of $\bar{R}$) and
> Tier 2D.
>
> ---

---

## 4.5 Absolute Value Equations

The absolute value $\lvert x \rvert$ equals $x$ if $x \ge 0$ and $-x$ if
$x < 0$. Geometrically, it's the distance from $x$ to zero on the number
line.

**Key property:** $\lvert x \rvert = a$ (where $a > 0$) means $x = a$ or
$x = -a$.

That's where the two-case structure comes from. The expression inside the
absolute value could be positive (and equal to $a$) or negative (and equal
to $-a$, whose absolute value is $a$).

### The method

$$\lvert f(x) \rvert = a \implies f(x) = a \quad \text{or} \quad f(x) = -a$$

Solve both, then verify both solutions in the original equation.

**Note:** $\lvert f(x) \rvert = a$ has no solution when $a < 0$, because
absolute value is never negative.

### Worked Example 6 — Absolute Value Equation

**Given.** Solve: $\lvert 2x - 3 \rvert = 7$

**Solution.**

Two cases:

**Case 1:** $2x - 3 = 7$
$$2x = 10 \implies x = 5$$

**Case 2:** $2x - 3 = -7$
$$2x = -4 \implies x = -2$$

**Verify both:**

$x = 5$: $\lvert 2(5) - 3 \rvert = \lvert 7 \rvert = 7$ ✓

$x = -2$: $\lvert 2(-2) - 3 \rvert = \lvert -7 \rvert = 7$ ✓

$$\boxed{x = 5 \quad \text{or} \quad x = -2}$$

**Geometric interpretation.** The two solutions are 5 and $-2$, and the expression $2x - 3$ equals 0 when $x = 1.5$. The solutions 5 and $-2$ are each 3.5 units away from the point where $x = 1.5$, since the distance of 7 applies to the expression $2x-3$ and the coeefficient 2 halves it on the x-axis.
That's not a coincidence — it's what absolute value distance means.

### Worked Example 7 — No Solution and One Solution Cases

**Given.** Solve: (a) $\lvert 3x + 1 \rvert = -4$ (b) $\lvert x - 2 \rvert = 0$

**Solution.**

(a) The right side is negative. Absolute value is never negative.

$$\boxed{\text{No solution.}}$$

(b) $\lvert x - 2 \rvert = 0$ only when $x - 2 = 0$, so $x = 2$. The "two
cases" both give the same equation when the right side is zero.

$$\boxed{x = 2}$$

---

## 4.6 Linear Inequalities

Solving a linear inequality uses the same operations as solving an equation,
with one critical difference.

> **Multiplying or dividing by a negative number reverses the inequality
> direction.**

$$2 < 6 \implies -2 > -6 \quad \text{(divided both sides by } -1\text{)}$$

Every other operation — adding, subtracting, multiplying or dividing by a
positive — preserves direction.

> ---
> **Mentor's Margin**
>
> This is the rule that fails silently. The arithmetic is correct, the sign
> of the answer is correct, but the solution is the complement of what it
> should be. And because an inequality answer is a region rather than a
> point, a direction flip is hard to spot unless you verify with a test
> value. Always do. Pick a number inside your claimed solution region and
> confirm it satisfies the original inequality. Pick one outside and confirm
> it doesn't.
>
> ---

### Worked Example 8 — Linear Inequality with Direction Flip

**Given.** Solve: $-3x + 2 > 11$. Express the solution in inequality
notation, interval notation, and on a number line.

**Solution.**

Step 1 — Subtract 2 from both sides (no direction change):

$$-3x > 9$$

Step 2 — Divide by $-3$. **Direction reverses.**

$$x < -3$$

**Inequality notation:** $x < -3$

**Interval notation:** $(-\infty, -3)$

**Number line:** open circle at $-3$, arrow extending left.

**Verify with a test value.** Pick $x = -5$ (inside the claimed solution):

$$-3(-5) + 2 = 15 + 2 = 17 > 11 \;\checkmark$$

Pick $x = 0$ (outside the claimed solution):

$$-3(0) + 2 = 2 \not> 11 \;\checkmark \quad \text{(correctly not a solution)}$$

---

## 4.7 Interval Notation

Clean shorthand for writing solution sets of inequalities. The exam uses it;
so do most engineering references. Know it cold.

| Condition | Inequality | Interval notation | Number line |
|---|---|---|---|
| $a < x < b$ | Strict double | $(a, b)$ | Open circles at both |
| $a \le x \le b$ | Non-strict double | $[a, b]$ | Closed circles at both |
| $a < x \le b$ | Mixed | $(a, b]$ | Open at $a$, closed at $b$ |
| $x > a$ | Unbounded right | $(a, +\infty)$ | Open circle at $a$, right arrow |
| $x \ge a$ | Unbounded right, inclusive | $[a, +\infty)$ | Closed circle at $a$, right arrow |
| $x < a$ | Unbounded left | $(-\infty, a)$ | Left arrow, open circle at $a$ |

Rules:
- **Parenthesis** means the endpoint is **excluded** (strict inequality)
- **Bracket** means the endpoint is **included** (non-strict inequality)
- $\infty$ and $-\infty$ **always** take parentheses — infinity is not a
  number and can never be reached

---

## 4.8 Compound Inequalities

Two inequalities connected by "and" (intersection) or "or" (union).

### "And" — both must be satisfied simultaneously

$$-2 < x \le 5 \qquad \text{meaning} \qquad x > -2 \quad\text{AND}\quad x \le 5$$

This is a bounded interval: $(-2, 5]$.

**Solving:** operate on all three parts simultaneously.

$$-2 \le 3x - 1 < 8$$

Add 1 to all three parts: $-1 \le 3x < 9$

Divide all three parts by 3 (positive, no flip): $-\frac{1}{3} \le x < 3$

Interval notation: $\left[-\frac{1}{3}, 3\right)$

### "Or" — either condition sufficient

$$x < -1 \quad\text{OR}\quad x \ge 4$$

Interval notation: $(-\infty, -1) \cup [4, +\infty)$

The union symbol $\cup$ joins the two intervals. The solution is not a single
interval — it's two separate pieces.

### Worked Example 9 — Compound Inequality

**Given.** Solve and express in interval notation:

$$-3 \le \frac{2x + 1}{5} < 3$$

**Solution.**

Step 1 — Multiply all three parts by 5 (positive, no flip):

$$-15 \le 2x + 1 < 15$$

Step 2 — Subtract 1 from all three parts:

$$-16 \le 2x < 14$$

Step 3 — Divide by 2 (positive, no flip):

$$-8 \le x < 7$$

$$\boxed{[-8, 7)}$$

**Verify with test values:**

- $x = 0$: $\frac{1}{5} = 0.2$. Is $-3 \le 0.2 < 3$? ✓
- $x = -8$: $\frac{-15}{5} = -3$. Is $-3 \le -3 < 3$? ✓ (closed bracket)
- $x = 7$: $\frac{15}{5} = 3$. Is $-3 \le 3 < 3$? $3 < 3$ is false. ✓
  (open bracket correctly excludes this endpoint)

> ---
> **Mentor's Margin**
>
> That third test value is the important one. You're checking that the open
> bracket is in the right place — confirming that the boundary value is *not*
> a solution. Half the interval notation errors on exams come from putting a
> bracket where a parenthesis belongs or vice versa. The test-value check
> is how you verify the boundary type, not just the value.
>
> ---

---

## 4.9 Setting Up Equations From Physical Relationships

This is where algebra meets engineering: reading a problem, identifying the
relevant relationship, and building the equation before solving it. Done
poorly, this step is the source of errors that survive all the algebra to
produce a confidently wrong answer.

**A systematic method:**

1. **Identify what you're solving for.** Name it. If the problem doesn't
   assign it a symbol, assign one yourself.
2. **Identify what you're given.** List every quantity and its units.
3. **Identify the governing relationship.** What physical principle or
   definition connects them?
4. **Write the equation in its standard form first**, then rearrange for
   your unknown.
5. **Carry units through the solution.**

The most common error at step 3: grabbing an equation that *looks* right
without checking whether its assumptions apply to your situation. The
dimensional homogeneity check from Chapter 01-02 runs here as a sanity
check.

### Worked Example 10 — Setting Up and Solving

**Given.** A concrete mix has a unit weight of $150 \text{ lbf/ft}^3$. A
rectangular footing is $6.0 \text{ ft} \times 4.0 \text{ ft} \times 2.0 \text{
ft}$ thick. What is its total weight?

**Given:** unit weight $SW = 150 \text{ lbf/ft}^3$, dimensions as stated.

**Find:** total weight.

**Governing relationship:** weight equals specific weight times volume.

$$F_W = SW \cdot V$$

**Setup:**

$$V = (6.0)(4.0)(2.0) = 48.0 \text{ ft}^3$$

$$F_W = \left(150 \; \frac{\text{lbf}}{\cancel{\text{ft}^3}}\right)(48.0 \; \cancel{\text{ft}^3}) = 7{,}200 \text{ lbf}$$

$$\boxed{F_W = 7{,}200 \text{ lbf} = 7.2 \text{ kip}}$$

**Check.** Dimensional analysis: lbf/ft³ × ft³ = lbf. ✓ A 48 ft³ block of
concrete at 150 lbf/ft³ weighing 7,200 lbf (about 3.6 tons) is physically
reasonable. ✓

*(Note: 1 kip = 1,000 lbf, a unit used commonly in structural engineering.)*

### Worked Example 11 — Inequality in Engineering Context

**Given.** A cable has a safe working load (SWL) of $8{,}500 \text{ lbf}$.
A safety factor of at least 4 must be applied, meaning the actual load the
cable carries must not exceed one-quarter of the SWL.

(a) Write and solve an inequality for the maximum allowable working load
$F_{work}$.

(b) If a load of $1{,}800 \text{ lbf}$ must be lifted, is the cable safe?

**Solution.**

(a) Safety factor inequality:

$$F_{work} \le \frac{SWL}{4} = \frac{8{,}500}{4} = 2{,}125 \text{ lbf}$$

$$\boxed{F_{work} \le 2{,}125 \text{ lbf}}$$

Interval notation: $(0, 2{,}125]$ lbf. (Load must be positive.)

(b) $1{,}800 \text{ lbf} \le 2{,}125 \text{ lbf}$. ✓ **Safe.**

**Check.** The safety factor is $8{,}500 / 1{,}800 = 4.72$, which exceeds 4. ✓

> ---
> **Mentor's Margin**
>
> Safety factors appear throughout structural, mechanical, and chemical
> engineering. They're always expressed as a ratio, and the logic is always
> the same: actual applied quantity $\le$ rated quantity / safety factor. You
> will solve inequalities like this in Tier 2C, Tier 2D, and every discipline
> track. The algebra is trivial once you've set it up correctly; the discipline
> is in recognizing the inequality structure and writing the safe direction.
>
> ---

---

## As the Handbook States It

Algebraic manipulation is **not** in the Handbook. No rearrangement rules, no
factoring identities, no inequality-solving procedures. This is the "basic
theories and definitions examinees are expected to know" category — entirely
memorize material.

However, every physics equation in the Handbook is subject to rearrangement,
and your fluency here determines how fast you can work with them. In that
indirect sense, this chapter underpins every other Handbook section.

**Two notation items to flag:**

The Handbook uses $\le$ and $\ge$ throughout for allowable limits in
engineering formulas — particularly in safety, structural, and thermal
sections. Recognizing these as non-strict inequalities (endpoints included)
is important for correct interpretation of design limits.

The Handbook uses the symbol $\lvert \cdot \rvert$ for absolute value
consistently. It also uses magnitude bars the same way — $\lvert \vec{F}
\rvert$ means the magnitude of force vector $\vec{F}$. Context distinguishes
them; we'll formalize the vector usage in Chapter 01-13.

---

## Where This Goes Wrong

**Forgetting to reverse the inequality when multiplying or dividing by a
negative.** Silent error, plausible-looking answer on the wrong side. Test
with a specific value every time you complete an inequality.

**$(a+b)^2 = a^2 + b^2$.** Missing the middle term $2ab$ is one of the
most common algebraic errors across all engineering calculations. There are
three terms on the right, not two.

**Adding a term to the numerator only.** When you add something to both
sides of an equation that has a fraction, the addition applies to the
*entire* expression on that side, not just to the numerator. Multiplying
through by the LCD first avoids this class of error.

**Not verifying the solution.** Substituting back takes 30 seconds and
catches the majority of sign and arithmetic errors.

**Using two cases but only checking one.** Both solutions of an absolute
value equation must be verified — especially in applied problems where
a negative solution may be physically meaningless.

**$\lvert a \rvert = b$ having a solution when $b < 0$.** Absolute value
is never negative. When the right side is negative, there is no solution.
Don't set up cases for a problem that has no answer.

**Interval notation bracket/parenthesis confusion.** The test: is the
boundary value itself a valid solution? If yes, bracket. If no, parenthesis.
Verify the boundary values directly.

**Setting up the wrong equation.** Step 3 of the setup method — identifying
the governing relationship — is where the engineering error happens. The
algebra might be perfect on the wrong equation. Check dimensional
homogeneity before solving, and verify the magnitude of the result against
physical intuition after.

---

## Key Terms

| Term | Definition |
|---|---|
| Expression | A combination of numbers, variables, and operations; has a value but no equality claim |
| Equation | A statement of equality between two expressions; solved for specific values |
| Inequality | A statement of ordering between two expressions; solved for a range of values |
| Like terms | Terms with identical variable parts (same variables, same exponents) |
| Distributive property | $a(b+c) = ab + ac$; the foundation of expansion and factoring |
| Difference of squares | $a^2 - b^2 = (a+b)(a-b)$ |
| Perfect square trinomial | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ |
| Isolate | To rearrange an equation so a specified variable appears alone on one side |
| Extraneous solution | A value that satisfies a transformed equation but not the original |
| Absolute value | $\lvert x \rvert$; distance from zero; never negative |
| Inequality direction | The sense ($<$, $>$, $\le$, $\ge$) of an inequality; reverses when multiplied or divided by a negative |
| Interval notation | Compact representation of a solution region using parentheses and brackets |
| Open interval | $(a,b)$; excludes endpoints; corresponds to strict inequalities |
| Closed interval | $[a,b]$; includes endpoints; corresponds to non-strict inequalities |
| Compound inequality | Two inequalities connected by "and" (intersection) or "or" (union) |
| Union ($\cup$) | The set containing elements from either set |
| Safety factor | Ratio of rated strength to applied load; working load must satisfy an inequality |

---

## Review Questions

### Conceptual

1. Distinguish an expression, an equation, and an inequality. Give an
   example of each that uses the same variable $F$.
2. Why does multiplying both sides of an inequality by a negative number
   reverse the direction? Demonstrate with a concrete numeric example.
3. State the difference-of-squares factoring identity and give two examples
   of expressions that factor this way.
4. Why does $(a + b)^2 \ne a^2 + b^2$? Show what term is missing and
   explain where it comes from.
5. An absolute value equation $\lvert f(x) \rvert = k$ has two cases.
   For what value of $k$ does it have exactly one solution? For what
   values has it no solution?
6. In interval notation, what is the difference between $(2, 7)$ and
   $[2, 7]$? Give an inequality corresponding to each.
7. You solve an inequality and get $x \le -5$. Describe the test-value
   check you'd run to verify the answer.
8. Explain step 3 of the equation-setup method — identifying the governing
   relationship. Why is getting this step wrong more dangerous than making
   an algebra error?

### Calculation

9. Simplify:
   (a) $4x^2 - 3x + 7 - x^2 + 5x - 2$
   (b) $3a(2a - 4) - 2a(a + 1)$
   (c) $(2x + 3y)(x - y) + (x + y)^2$

10. Expand:
    (a) $(4x - 1)^2$
    (b) $(3m + 2n)(3m - 2n)$
    (c) $(x + 2)(x^2 - 2x + 4)$

11. Factor completely:
    (a) $25x^2 - 40x + 16$
    (b) $36z^2 - 121$
    (c) $12t^3 - 27t$
    (d) $x^2 + 7x + 12$

12. Solve for $x$ and verify:
    (a) $5(x - 3) = 2x + 9$
    (b) $\dfrac{x+4}{3} = \dfrac{x-1}{5}$
    (c) $\dfrac{2x}{3} + \dfrac{x-1}{4} = 2$

13. Solve each equation for the specified variable:
    (a) $F = ma/g_c$, for $m$
    (b) $P = IV$, for $I$
    (c) $A = \pi r^2$, for $r$
    (d) $PV = mRT$, for $R$

14. Solve each equation for the specified variable:
    (a) $\dfrac{1}{R_T} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$, for $R_T$
    (b) $\eta = 1 - \dfrac{T_L}{T_H}$, for $T_H$
    (c) $V_{out} = V_{in} \dfrac{R_2}{R_1 + R_2}$, for $R_2$
    (d) $f_r = \dfrac{1}{2\pi\sqrt{LC}}$, for $C$

15. Solve:
    (a) $\lvert 4x + 8 \rvert = 20$
    (b) $\lvert 3 - 2x \rvert = 9$
    (c) $\lvert x + 1 \rvert + 3 = 10$
    (d) $\lvert 5x - 3 \rvert = -2$

16. Solve each inequality and express in both inequality and interval
    notation. Verify with a test value.
    (a) $4x - 7 > 5$
    (b) $-2x + 3 \le 11$
    (c) $3(x + 4) \ge 2(x - 1)$
    (d) $\dfrac{x}{4} - 2 < 1$

17. Solve each compound inequality and express in interval notation:
    (a) $-4 \le 3x - 1 < 8$
    (b) $0 \le \dfrac{2x + 6}{4} \le 5$
    (c) $x + 2 < -1$ or $x - 3 > 2$

18. **Engineering application.** A pump delivers water at a volumetric
    flow rate $Q_v \; [\text{m}^3/\text{s}]$ against a pressure differential
    $\Delta p \; [\text{Pa}]$. The hydraulic power is $\dot{W}_h = Q_v \Delta p$.

    (a) Rearrange for $Q_v$.
    (b) A pump delivers $7.5 \text{ kW}$ of hydraulic power. The operating
    pressure differential is $250 \text{ kPa}$. Find $Q_v$ in m³/s.
    (c) Express $Q_v$ in L/s.
    (d) For the pump to stay within its rated power of $9.0 \text{ kW}$,
    write and solve an inequality for the maximum allowable $Q_v$ at
    the same $\Delta p$.

19. **Engineering application.** A steel tension member must carry a
    factored load of $P = 120 \text{ kN}$. The allowable tensile stress is
    $\sigma_{allow} = 165 \text{ MPa}$. The required area is $A \ge P /
    \sigma_{allow}$.

    (a) Compute the minimum required cross-sectional area in mm².
    (b) A circular rod will be used. The area of a circle is $A = \pi d^2/4$.
    Write an inequality for the minimum required diameter $d$ in mm.
    (c) Solve the inequality for $d$.

### Multiple Choice

20. Which of the following is an expression rather than an equation?
    A) $3x - 5 = 0$
    B) $3x - 5 > 0$
    C) $3x - 5$
    D) $3x - 5 \le 0$

21. $(2a - 3b)^2$ expands to:
    A) $4a^2 - 9b^2$
    B) $4a^2 - 6ab + 9b^2$
    C) $4a^2 - 12ab + 9b^2$
    D) $4a^2 + 12ab + 9b^2$

22. The solution to $-5x + 3 > 18$ is:
    A) $x > -3$
    B) $x < -3$
    C) $x > 3$
    D) $x < 3$

23. The interval $[-3, 7)$ corresponds to which inequality?
    A) $-3 \le x \le 7$
    B) $-3 < x < 7$
    C) $-3 \le x < 7$
    D) $-3 < x \le 7$

24. The equation $\lvert 2x - 1 \rvert = -5$ has:
    A) One solution
    B) Two solutions
    C) No solution
    D) Infinitely many solutions

25. Solving $PV = nRT$ for $T$ gives:
    A) $T = PVnR$
    B) $T = \dfrac{nR}{PV}$
    C) $T = \dfrac{PV}{nR}$
    D) $T = PV - nR$

26. The solution set of $x - 4 < -1$ OR $x + 1 > 6$ in interval notation
    is:
    A) $(3, 5)$
    B) $(-\infty, 3) \cup (5, +\infty)$
    C) $(-\infty, 3) \cup [5, +\infty)$
    D) $(3, +\infty)$

---

## Answer Key with Explanations

**1.** An **expression** has no equality claim: $F^2 + 2F$. An **equation**
claims two expressions are equal: $F = ma/g_c$. An **inequality** states an
ordering: $F \le F_{allow}$. The same variable can appear in all three; the
difference is in the symbol connecting the two sides. (§4.1)

**2.** Concrete example: $2 < 6$. Multiply both sides by $-1$: $-2$ and $-6$.
On the number line, $-6$ is to the left of $-2$, so $-2 > -6$. The direction
reversed. Algebraic reason: the number line is a mirror — multiplying by a
negative reflects both sides, swapping their relative positions. (§4.6)

**3.** $a^2 - b^2 = (a+b)(a-b)$. Two examples: $x^2 - 16 = (x+4)(x-4)$;
$9m^2 - 25n^2 = (3m + 5n)(3m - 5n)$. The pattern to recognize: a difference,
both terms perfect squares. (§4.3)

**4.** $(a+b)^2 = (a+b)(a+b) = a^2 + ab + ab + b^2 = a^2 + 2ab + b^2$. The
missing term is $2ab$, which comes from the two cross-products when distributing.
Writing $(a+b)^2 = a^2 + b^2$ skips both cross terms. (§4.3)

**5.** When $k = 0$, $\lvert f(x) \rvert = 0$ has exactly one solution (the
value where $f(x) = 0$, because the two cases both give $f(x) = 0$). When
$k < 0$, there is no solution — absolute value is never negative. (§4.5)

**6.** $(2, 7)$ means $2 < x < 7$ — strict inequalities, endpoints excluded.
$[2, 7]$ means $2 \le x \le 7$ — non-strict, endpoints included. The
parenthesis/bracket encoding is exact: parenthesis = excluded, bracket =
included. (§4.7)

**7.** Pick a value clearly inside the claimed region, say $x = -7$ (which
satisfies $x \le -5$). Substitute into the original inequality and verify it
holds. Then pick a value outside, say $x = 0$, and verify it *doesn't* hold.
If both checks pass, the direction and boundary are correct. (§4.6)

**8.** Because an algebra error produces a wrong numeric answer that could
still be close to a distractor. A wrong governing equation produces an answer
with a completely different physical meaning — and it may match a distractor
that was crafted to catch exactly that error. The equation itself can be
checked dimensionally, and the magnitude of the result checked physically.
Neither catches an algebra error; both catch a wrong setup. (§4.9)

**9.**

(a) Collect like terms:
$(4-1)x^2 + (-3+5)x + (7-2) = \boxed{3x^2 + 2x + 5}$

(b) Distribute:
$6a^2 - 12a - 2a^2 - 2a = \boxed{4a^2 - 14a}$

(c) First product: $2x^2 - 2xy + 3xy - 3y^2 = 2x^2 + xy - 3y^2$.
Second: $x^2 + 2xy + y^2$.
Sum: $(2+1)x^2 + (1+2)xy + (-3+1)y^2 = \boxed{3x^2 + 3xy - 2y^2}$

**10.**

(a) $(4x-1)^2 = 16x^2 - 8x + 1$

(b) $(3m+2n)(3m-2n) = (3m)^2 - (2n)^2 = \boxed{9m^2 - 4n^2}$

(c) $(x+2)(x^2 - 2x + 4)$: distribute $x$: $x^3 - 2x^2 + 4x$. Distribute
$+2$: $2x^2 - 4x + 8$. Sum: $\boxed{x^3 + 8}$.

*Note: this is the sum of cubes pattern $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$
with $a = x$, $b = 2$. You'll see it again in Chapter 01-07.*

**11.**

(a) $25x^2 - 40x + 16$: check perfect square. $\sqrt{25x^2} = 5x$,
$\sqrt{16} = 4$, $2(5x)(4) = 40x$. ✓

$$\boxed{(5x-4)^2}$$

(b) $36z^2 - 121 = (6z)^2 - 11^2 = \boxed{(6z+11)(6z-11)}$

(c) $12t^3 - 27t$: GCF first: $3t(4t^2 - 9)$. Then difference of squares:

$$\boxed{3t(2t+3)(2t-3)}$$

(d) Find two numbers multiplying to 12 and adding to 7: 3 and 4.

$$\boxed{(x+3)(x+4)}$$

**12.**

(a) $5x - 15 = 2x + 9 \Rightarrow 3x = 24 \Rightarrow x = 8$.

Verify: $5(5) = 25$, $2(8)+9 = 25$ ✓. $\boxed{x = 8}$

(b) Cross-multiply: $5(x+4) = 3(x-1) \Rightarrow 5x+20 = 3x-3 \Rightarrow
2x = -23 \Rightarrow x = -11.5$.

Verify: $\frac{-7.5}{3} = -2.5$ and $\frac{-12.5}{5} = -2.5$ ✓.
$\boxed{x = -11.5}$

(c) LCD = 12. Multiply through: $8x + 3(x-1) = 24 \Rightarrow 8x + 3x - 3 =
24 \Rightarrow 11x = 27 \Rightarrow x = 27/11$.

Verify: $\frac{2(27/11)}{3} + \frac{(27/11)-1}{4} = \frac{18}{11} +
\frac{16/11}{4} = \frac{18}{11} + \frac{4}{11} = \frac{22}{11} = 2$ ✓.
$\boxed{x = 27/11 \approx 2.45}$

**13.**

(a) $m = \dfrac{Fg_c}{a}$

(b) $I = \dfrac{P}{V}$

(c) $r = \sqrt{\dfrac{A}{\pi}}$

(d) $R = \dfrac{PV}{mT}$

**14.**

(a) Multiply both sides by $R_T R_1 R_2$:
$R_1 R_2 = R_T R_2 + R_T R_1 = R_T(R_1 + R_2)$

$$\boxed{R_T = \frac{R_1 R_2}{R_1 + R_2}}$$

(b) $\eta = 1 - T_L/T_H \Rightarrow T_L/T_H = 1 - \eta \Rightarrow$

$$\boxed{T_H = \frac{T_L}{1 - \eta}}$$

(c) $V_{out}(R_1 + R_2) = V_{in}R_2 \Rightarrow V_{out}R_1 = V_{in}R_2 -
V_{out}R_2 = R_2(V_{in} - V_{out})$

$$\boxed{R_2 = \frac{V_{out}R_1}{V_{in} - V_{out}}}$$

(d) $f_r = \dfrac{1}{2\pi\sqrt{LC}} \Rightarrow 2\pi\sqrt{LC} = \dfrac{1}{f_r}
\Rightarrow \sqrt{LC} = \dfrac{1}{2\pi f_r} \Rightarrow LC =
\dfrac{1}{4\pi^2 f_r^2} \Rightarrow$

$$\boxed{C = \frac{1}{4\pi^2 f_r^2 L}}$$

**15.**

(a) $4x + 8 = 20 \Rightarrow x = 3$, or $4x + 8 = -20 \Rightarrow x = -7$.

Verify: $|12+8| = 20$ ✓, $|-28+8| = 20$ ✓. $\boxed{x = 3 \text{ or } x = -7}$

(b) $3-2x = 9 \Rightarrow x = -3$, or $3-2x = -9 \Rightarrow x = 6$.

Verify: $|3+6| = 9$ ✓, $|3-12| = 9$ ✓. $\boxed{x = -3 \text{ or } x = 6}$

(c) Isolate the absolute value first: $|x+1| = 7$.

$x+1 = 7 \Rightarrow x = 6$, or $x+1 = -7 \Rightarrow x = -8$.

$\boxed{x = 6 \text{ or } x = -8}$

(d) Right side is $-2 < 0$. No solution. $\boxed{\text{No solution.}}$

**16.**

(a) $4x > 12 \Rightarrow x > 3$. Interval: $(3, +\infty)$.

Test: $x = 4$: $4(4)-7 = 9 > 5$ ✓. $x = 0$: $-7 \not> 5$ ✓.

(b) $-2x \le 8 \Rightarrow x \ge -4$ (flip on divide by $-2$). Interval: $[-4, +\infty)$.

Test: $x = 0$: $3 \le 11$ ✓. $x = -5$: $13 \not\le 11$ ✓.

(c) $3x + 12 \ge 2x - 2 \Rightarrow x \ge -14$. Interval: $[-14, +\infty)$.

Test: $x = 0$: $12 \ge -2$ ✓. $x = -15$: $3(-11) = -33$ and $2(-17) = -34$;
$-33 \ge -34$ ✓ but $-15 \ge -14$? No — verify boundary: $x = -14$:
$3(-10)=-30$ and $2(-15)=-30$; $-30 \ge -30$ ✓.

(d) $\dfrac{x}{4} < 3 \Rightarrow x < 12$. Interval: $(-\infty, 12)$.

Test: $x = 0$: $-2 < 1$ ✓. $x = 16$: $4-2=2 \not< 1$ ✓.

**17.**

(a) $-4 \le 3x-1 < 8 \Rightarrow -3 \le 3x < 9 \Rightarrow -1 \le x < 3$.

$$\boxed{[-1, 3)}$$

(b) Multiply by 4: $0 \le 2x+6 \le 20$. Subtract 6: $-6 \le 2x \le 14$.
Divide by 2: $-3 \le x \le 7$.

$$\boxed{[-3, 7]}$$

(c) $x+2 < -1 \Rightarrow x < -3$, or $x-3 > 2 \Rightarrow x > 5$.

$$\boxed{(-\infty, -3) \cup (5, +\infty)}$$

**18.**

(a) $Q_v = \dfrac{\dot{W}_h}{\Delta p}$

(b) Convert: $7.5 \text{ kW} = 7{,}500 \text{ W} = 7{,}500 \text{ N·m/s}$;
$\Delta p = 250{,}000 \text{ Pa} = 250{,}000 \text{ N/m}^2$.

$$Q_v = \frac{7{,}500}{250{,}000} = 0.030 \text{ m}^3/\text{s}$$

(c) $0.030 \text{ m}^3/\text{s} \times 1{,}000 = \boxed{30 \text{ L/s}}$

(d) $Q_v \le \dfrac{9{,}000}{250{,}000} = 0.036 \text{ m}^3/\text{s} = 36 \text{ L/s}$

$$\boxed{Q_v \le 0.036 \text{ m}^3/\text{s}}$$

**19.**

(a) $A \ge \dfrac{120 \text{ kN}}{165 \text{ MPa}} = \dfrac{120{,}000 \text{ N}}{165 \text{ N/mm}^2} = 727 \text{ mm}^2$

(b) $\dfrac{\pi d^2}{4} \ge 727 \text{ mm}^2$

(c) $d^2 \ge \dfrac{4 \times 727}{\pi} = \dfrac{2{,}908}{3.1416} = 925.3 \text{ mm}^2$

$$d \ge \sqrt{925.3} = 30.4 \text{ mm}$$

$$\boxed{d \ge 30.4 \text{ mm}}$$

Note: taking the square root of both sides of a non-negative inequality
preserves the direction because $\sqrt{\cdot}$ is an increasing function.

**20. C.** An expression has no relational symbol — it's just $3x - 5$.
(A) is an equation, (B) and (D) are inequalities. (§4.1)

**21. C — $4a^2 - 12ab + 9b^2$.** $(2a-3b)^2 = (2a)^2 - 2(2a)(3b) + (3b)^2
= 4a^2 - 12ab + 9b^2$. (A) uses difference-of-squares, not perfect square.
(B) has $-6ab$ instead of $-12ab$. (§4.3)

**22. B — $x < -3$.** $-5x > 15 \Rightarrow x < -3$ (flip on divide by $-5$).
The direction reversal is the trap that makes (A) a distractor. (§4.6)

**23. C — $-3 \le x < 7$.** Bracket at $-3$ means included ($\le$);
parenthesis at $7$ means excluded ($<$). (§4.7)

**24. C — No solution.** Absolute value is never negative; no value of $x$
can make $\lvert 2x-1 \rvert = -5$ true. (§4.5)

**25. C — $T = PV/(nR)$.** Divide both sides by $nR$. (§4.4)

**26. B — $(-\infty, 3) \cup (5, +\infty)$.** $x-4 < -1 \Rightarrow x < 3$
and $x+1 > 6 \Rightarrow x > 5$. Both endpoints are strict (open circles,
parentheses). (§4.8, correct choice C has a bracket which would be wrong
since both inequalities are strict.) The correct answer is **B**. (§4.7)

---

## Quick Reference

**Three structures**

| | Symbol | Solved for |
|---|---|---|
| Expression | none | value or simplified form |
| Equation | $=$ | specific values |
| Inequality | $<, >, \le, \ge$ | range of values |

**Special products — memorize**

$$a^2 - b^2 = (a+b)(a-b)$$
$$(a+b)^2 = a^2 + 2ab + b^2$$
$$(a-b)^2 = a^2 - 2ab + b^2$$

**Equation-solving principle**

Same operation to both sides. Operations that preserve equality: $+, -, \times
c, \div c$ (where $c \ne 0$). Verify by substitution.

**Absolute value equations**

$$\lvert f(x) \rvert = a \implies f(x) = a \text{ or } f(x) = -a \quad (a > 0)$$

No solution when $a < 0$. One solution when $a = 0$.

**Inequality direction reversal**

Flip direction when multiplying or dividing by a **negative**. All other
operations preserve direction.

**Interval notation**

| Notation | Meaning | Boundaries |
|---|---|---|
| $(a,b)$ | $a < x < b$ | Both excluded |
| $[a,b]$ | $a \le x \le b$ | Both included |
| $(a,+\infty)$ | $x > a$ | Left excluded, $\infty$ always excluded |
| $(-\infty, a]$ | $x \le a$ | Right included, $-\infty$ always excluded |

**Compound inequalities**

- "And" → solve simultaneously → single interval or empty set
- "Or" → solve separately → union of intervals $\cup$

**Setup method for engineering equations**

1. Name the unknown
2. List givens with units
3. Identify governing relationship (check dimensions)
4. Write standard form, then rearrange
5. Carry units through the solution

**Not in the Handbook — memorize entirely:**

All algebraic properties and identities · inequality direction rule ·
absolute value case structure · interval notation · equation setup method

---

## What's Next

Apprentice, one chapter into Tier 1B. Algebra is the language; now we add
more vocabulary.

In **Chapter 01-05: Exponents, Radicals, and Logarithms**, we build the three
families of operations that the earlier chapters borrowed without fully
defining. You've been using $10^x$ since Chapter 01-01 and $\pi$ since
birth — now we work out the complete algebra of exponential and logarithmic
functions, including the natural logarithm and Euler's number $e$.

This one shows up constantly: exponential decay in RC circuits, logarithmic
relationships in decibel calculations, natural log in thermodynamic efficiency
and reaction kinetics. It's not optional material for any discipline.

Bring the Handbook open to the Mathematics section, page 36. That's where
the exponential and logarithmic identities live.

See you there.

— Your Mentor
