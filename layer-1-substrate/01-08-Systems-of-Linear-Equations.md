---
chapter: "01-08"
title: "Systems of Linear Equations"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-008-01, MATH-1B-008-02, MATH-1B-008-03]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-08: Systems of Linear Equations

> *"You will never analyze a real structure, circuit, or process with one
> equation. The moment you have two members meeting at a joint, two loops
> in a circuit, two streams mixing in a reactor — you have a system. The
> engineer who can set up and solve systems quickly has a fundamental
> advantage over the one who can only handle one equation at a time."*

---

## Before You Start

**Prerequisites:** [01-04 Expressions, Equations, and Inequalities](01-04-expressions-equations-inequalities.md) · [01-06 Functions, Graphs, and Transformations](01-06-functions-graphs-transformations.md) · [01-07 Polynomials and Their Roots](01-07-polynomials-and-their-roots.md)

01-07 is needed only for the last review question, where a rate problem
produces a quadratic. Everything in the body needs only 01-04 and 01-06.

**Skip if:** You pass the Tier 1B test-out quiz. Verify you can set up and
solve a 3×3 system by elimination before skipping — that's the step most
people haven't practiced recently.

**Time:** ~55 min read · ~25 min review questions · ~55 min practice problems

---

## On the Board Today

Apprentice, every equilibrium problem in Tier 2C — every joint, every truss,
every beam reaction — produces a system of equations. Kirchhoff's voltage and
current laws in Tier 2E produce systems. Mass and energy balances in chemical
and environmental engineering produce systems. The pattern is unavoidable:
multiple conditions constraining multiple unknowns.

Three methods, and you need all three, because each one suits a different
situation.

**Substitution** is what you reach for when one equation already has a
variable isolated, or nearly so. Cheap for small systems, awkward beyond 2×2.

**Elimination**, done systematically, is called **Gaussian elimination** and
it is the workhorse. It requires no inspiration — you follow a procedure and
it terminates. It is also the method that scales, which is why it reappears
in matrix form in Chapter 01-14.

**Cramer's rule** solves for one variable at a time as a ratio of two
determinants. It is the fastest route on a 2×2 system when you need only one
of the two unknowns.

That last one needs a word. Cramer's rule uses determinants, and determinants
belong properly to matrices in Chapter 01-14. But the 2×2 determinant is just
an arithmetic recipe on four numbers — $ad - bc$ — and it stands alone
perfectly well. I define it here from scratch in §8.5. You need nothing from
01-14 to use it, and when 01-14 arrives it will generalize what you already
know rather than introduce it.

One concept before any calculating. A linear system has exactly three
possible outcomes: one solution, no solution, or infinitely many. Recognizing
which one you are looking at *before* you finish solving saves real time, and
the recognition comes from two places — the geometry, and what the algebra
does when you try to eliminate.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 8.1 Classify a linear system as consistent and independent, consistent and
  dependent, or inconsistent
* 8.2 Solve 2×2 systems by substitution and by elimination
* 8.3 Solve 3×3 systems by Gaussian elimination with back substitution
* 8.4 Recognize when a system has no solution or infinitely many solutions
  from algebraic signals, in both 2×2 and 3×3 systems
* 8.5 Evaluate a 2×2 determinant and apply Cramer's rule to a 2×2 system
* 8.6 Set up a system of equations from a physical problem, checking the
  count of unknowns against the count of independent conditions
* 8.7 Verify a solution by substituting into every original equation

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $a_{ij}$ | coefficient in row $i$, column $j$ | first index is the row |
| $[A \mid b]$ | augmented matrix | coefficients, a rule, then constants |
| $R_i$ | row $i$ of an augmented matrix | — |
| $R_i \leftarrow R_i + cR_j$ | replace row $i$ with itself plus $c$ times row $j$ | row operation |
| $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ | determinant of a 2×2 array | a single number, $ad - bc$ |
| $D$, $D_x$, $D_y$ | the three determinants of Cramer's rule | defined in §8.5 |
| $n$ | number of unknowns | — |
| $m$ | number of independent equations | — |

> ---
> **Mentor's Margin**
>
> Watch the brackets. **Single vertical bars** around an array mean its
> determinant — one number. **Square brackets** would mean the array itself —
> a table of numbers. This chapter only ever needs the number, so only
> vertical bars appear. Chapter 01-14 introduces the array as an object in
> its own right and keeps the two notations strictly apart. Conflating them
> is the standard confusion when matrices arrive, and starting out with the
> distinction clear costs you nothing now.
>
> ---

---

## 8.1 What Makes a System Linear

A **linear system** has equations in which every variable appears to the
first power only. No $x^2$, no $xy$, no $\sin x$, no $1/x$. Constants may be
anything at all, including ugly ones — what matters is how the *variables*
appear.

Each such equation describes a flat object: a line in two dimensions, a plane
in three, a hyperplane beyond that. Solving the system means finding where
all of those flat objects meet.

That geometric picture is what makes the three outcomes inevitable.

### The three outcomes

**Consistent and independent** — exactly one solution. The lines or planes
meet at a single point.

**Consistent and dependent** — infinitely many solutions. The equations
describe the same object, or in 3D, three planes sharing a whole line.

**Inconsistent** — no solution. The objects never all meet. In 2D that means
parallel lines.

There is no fourth case. Two distinct straight lines cannot cross twice.

### How to recognize each outcome algebraically

You rarely have the graph in front of you. What you have is the algebra, and
the algebra announces the outcome clearly:

| What happens as you eliminate | Interpretation |
|---|---|
| You isolate a specific variable value | Consistent, independent — one solution |
| An equation reduces to $0 = 0$ | Consistent, dependent — infinite solutions |
| An equation reduces to $0 = k$, $k \ne 0$ | Inconsistent — no solution |

$0 = 5$ is a contradiction. No values of any variables make zero equal five,
so no solution exists. $0 = 0$ is the opposite: a statement so true it is
empty, which means one of your equations carried no information the others
didn't already have.

![FIG-01-08-001: Three panels, each pairing a pair of plotted lines with the algebraic signal that produces it. Left panel 'consistent and independent': two lines of different slope crossing at a single marked point labelled 'one solution', with the elimination result 'you isolate a variable value' printed beneath. Centre panel 'consistent and dependent': a single line drawn heavy with a note that both equations describe it, the second equation shown as a multiple of the first, labelled 'every point on the line is a solution', with the elimination result '0 = 0' printed beneath in a box. Right panel 'inconsistent': two parallel lines with a double-headed arrow marking the constant gap between them and a label 'no intersection anywhere', with the elimination result '0 = k, k nonzero' printed beneath in a box. A footer strip reads 'the algebra and the picture are the same fact — 0 = 0 means the lines coincided, 0 = k means they never met'.](../figures/FIG-01-08-001-three-outcomes-geometric.png)

> ---
> **Mentor's Margin**
>
> In engineering, an inconsistent or dependent system almost always means a
> setup error, not a discovery. If a force balance on a joint hands you
> $0 = 5$, you have a sign error, or you applied one condition twice, or you
> wrote the same equilibrium equation in two disguises. The algebra is
> telling the truth about your equations — they contradict each other. The
> message to hear is *go back and check the setup*. A joint that is genuinely
> in equilibrium has a solution.
>
> The one honest exception is dependency in a structural analysis, which can
> mean your structure is a mechanism — it moves. That is real physics, and
> §8.4 comes back to it.
>
> ---

---

## 8.2 Solving 2×2 Systems

### Method 1 — Substitution

1. Solve one equation for one variable in terms of the other.
2. Substitute that expression into the second equation.
3. Solve the resulting single-variable equation.
4. Back-substitute to get the first variable.
5. **Verify in both original equations.**

Step 1 is where the choice matters. Isolate the variable whose coefficient is
already $1$ if there is one. Isolating a variable with coefficient $7$ gives
you fractions to carry through every subsequent line, and each one is a
chance to slip.

### Worked Example 1 — Substitution

**Given.** Solve:

$$\begin{cases} 2x + y = 7 & (1)\\ 3x - y = 8 & (2) \end{cases}$$

**Solution.**

Step 1 — In equation (1), $y$ has coefficient $1$. Isolate it:

$$y = 7 - 2x$$

Step 2 — Substitute into equation (2):

$$3x - (7 - 2x) = 8$$

Mind the bracket. The minus sign distributes across both terms:

$$3x - 7 + 2x = 8 \implies 5x = 15$$

Step 3 — Solve:

$$x = 3$$

Step 4 — Back-substitute into the isolated form:

$$y = 7 - 2(3) = 1$$

$$\boxed{x = 3, \quad y = 1}$$

Step 5 — Verify in **both** originals:

(1): $2(3) + 1 = 7$ ✓
(2): $3(3) - 1 = 8$ ✓

### Method 2 — Elimination

1. Multiply one or both equations by constants so that one variable's
   coefficients are equal and opposite.
2. Add the equations. That variable vanishes.
3. Solve for the survivor.
4. Back-substitute.
5. Verify in both originals.

Notice the system in Worked Example 1 was already set up for this: $+y$ and
$-y$. Adding equations (1) and (2) directly gives $5x = 15$ in one line. Two
methods, same answer, and which is less work depends entirely on what the
coefficients happen to be.

![FIG-01-08-002: Two parallel columns solving the same system 2x + y = 7 and 3x − y = 8. Left column headed 'substitution': four stacked boxes reading 'isolate y in the first equation, y = 7 − 2x', 'substitute into the second, 3x − (7 − 2x) = 8', 'solve, 5x = 15 so x = 3', 'back-substitute, y = 1'. A margin tag reads 'best when a variable already has coefficient 1'. Right column headed 'elimination': four stacked boxes reading 'the y coefficients are already +1 and −1', 'add the equations, the y terms cancel', 'solve, 5x = 15 so x = 3', 'back-substitute, y = 1'. A margin tag reads 'best when coefficients line up, and it scales to 3x3 and beyond'. Both columns converge on a single shared box at the bottom reading 'verify (3, 1) in BOTH original equations' with two checkmarks. A footer note reads 'same answer, different labour — pick the method the coefficients are offering you'.](../figures/FIG-01-08-002-substitution-versus-elimination.png)

### Worked Example 2 — Elimination in an Equilibrium Problem

**Given.** Two members meet at a pin joint carrying an applied load. Writing
equilibrium in the horizontal and vertical directions gives:

$$3F_1 - 2F_2 = 6 \qquad \text{(horizontal, kN)} \quad (1)$$
$$F_1 + 4F_2 = 16 \qquad \text{(vertical, kN)} \quad (2)$$

Find the member forces $F_1$ and $F_2$.

![FIG-01-08-003: A free-body diagram of a single pin joint drawn as a small circle, with two member forces and one applied load. Force F1 acts along a member directed up and to the right, F2 acts along a member directed up and to the left, and both are drawn as arrows pulling away from the joint with a note 'drawn as tension, positive means tension'. A small set of x and y reference axes sits beside the joint. Two equation strips run alongside: the horizontal strip reads 'sum of forces in x = 0 gives 3F1 − 2F2 = 6' and the vertical strip reads 'sum of forces in y = 0 gives F1 + 4F2 = 16', each with a leader line to the relevant arrow components. A footer note reads 'two independent equilibrium conditions, two unknown member forces — the count matches, so a unique solution exists'.](../figures/FIG-01-08-003-pin-joint-free-body.png)

**Solution.**

Eliminate $F_1$. Its coefficients are $3$ and $1$, so multiply equation (2)
by $-3$:

$$3F_1 - 2F_2 = 6$$
$$-3F_1 - 12F_2 = -48$$

Add:

$$-14F_2 = -42 \implies F_2 = 3$$

Back-substitute into equation (2):

$$F_1 = 16 - 4(3) = 4$$

$$\boxed{F_1 = 4 \text{ kN}, \quad F_2 = 3 \text{ kN}}$$

**Verify:**

(1): $3(4) - 2(3) = 12 - 6 = 6$ ✓
(2): $4 + 4(3) = 16$ ✓

Both positive, so both members are in tension under the sign convention of
the free-body diagram. A negative answer would have been perfectly
acceptable — it would mean compression — but it is worth noticing which you
got.

> ---
> **Mentor's Margin**
>
> Always verify in **both** original equations, never just the one you used
> for back-substitution.
>
> Here is why. Back-substitution takes your computed $F_2$ and the original
> equation (2) and produces $F_1$. Substituting that $F_1$ back into equation
> (2) therefore *cannot* fail — you built it to satisfy that equation. The
> check is circular and catches nothing.
>
> Equation (1) is the one that was never used to construct either answer. It
> is the only real test, and it is the one that catches a sign error in the
> elimination step. Thirty seconds, and it is the highest-value thirty
> seconds in the problem.
>
> ---

---

## 8.3 Solving 3×3 Systems — Gaussian Elimination

Three equations in three unknowns is where ad-hoc methods start costing more
than they save. The systematic approach is **Gaussian elimination**: use row
operations to drive the system into upper triangular form, then
back-substitute from the bottom up.

### The augmented matrix

Writing $x$, $y$, $z$, and the equals signs over and over wastes time and
invites transcription errors. Strip them out and keep only the numbers, in
fixed positions:

$$\begin{cases} 2x + y - z = 8 \\ -3x - y + 2z = -11 \\ -2x + y + 2z = -3 \end{cases} \quad\longrightarrow\quad \left[\begin{array}{ccc|c} 2 & 1 & -1 & 8 \\ -3 & -1 & 2 & -11 \\ -2 & 1 & 2 & -3 \end{array}\right]$$

This is the **augmented matrix** $[A \mid b]$: coefficients on the left of
the rule, constants on the right. Column position now carries the
information that the variable names used to. A missing term must be written
as a $0$ — the columns have to stay aligned or everything downstream is
wrong.

### The three legal row operations

These are the only moves allowed, and each one is reversible, which is
exactly why none of them changes the solution set:

1. **Swap** two rows.
2. **Scale** a row by a nonzero constant.
3. **Add** a multiple of one row to another.

Operation 2 excludes zero for a reason. Multiplying a row by zero is not
reversible — you cannot recover the equation afterwards — and it throws away
a genuine constraint, which enlarges the solution set. It is not a legal row
operation.

### Worked Example 3 — Full 3×3 System

**Given.** Solve:

$$\begin{cases}
2x + y - z = 8 & \quad (1)\\
-3x - y + 2z = -11 & \quad (2)\\
-2x + y + 2z = -3 & \quad (3)
\end{cases}$$

**Solution.**

$$\left[\begin{array}{ccc|c} 2 & 1 & -1 & 8 \\ -3 & -1 & 2 & -11 \\ -2 & 1 & 2 & -3 \end{array}\right]$$

**Step 1 — Clear the first column below the pivot.**

The pivot is the $2$ in the top-left. To clear the $-3$ beneath it without
introducing fractions, scale $R_2$ by $2$ and add $3R_1$. That is two legal
operations performed in one line, which is standard practice:

$$R_2 \leftarrow 2R_2 + 3R_1$$

$$2(-3) + 3(2) = 0 \qquad 2(-1) + 3(1) = 1 \qquad 2(2) + 3(-1) = 1 \qquad 2(-11) + 3(8) = 2$$

For $R_3$, the $-2$ is cleared by adding $R_1$ directly:

$$R_3 \leftarrow R_3 + R_1$$

$$-2 + 2 = 0 \qquad 1 + 1 = 2 \qquad 2 + (-1) = 1 \qquad -3 + 8 = 5$$

$$\left[\begin{array}{ccc|c} 2 & 1 & -1 & 8 \\ 0 & 1 & 1 & 2 \\ 0 & 2 & 1 & 5 \end{array}\right]$$

**Step 2 — Clear the second column below the new pivot.**

$$R_3 \leftarrow R_3 - 2R_2$$

$$0 \qquad 2 - 2(1) = 0 \qquad 1 - 2(1) = -1 \qquad 5 - 2(2) = 1$$

$$\left[\begin{array}{ccc|c} 2 & 1 & -1 & 8 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & -1 & 1 \end{array}\right]$$

Upper triangular. All zeros below the diagonal, and every diagonal entry is
nonzero, which already tells you a unique solution exists.

**Step 3 — Back-substitute, bottom row first.**

Row 3: $\;-z = 1 \implies z = -1$

Row 2: $\;y + z = 2 \implies y + (-1) = 2 \implies y = 3$

Row 1: $\;2x + y - z = 8 \implies 2x + 3 - (-1) = 8 \implies 2x = 4 \implies x = 2$

$$\boxed{x = 2, \quad y = 3, \quad z = -1}$$

**Verify in all three originals:**

(1): $2(2) + 3 - (-1) = 4 + 3 + 1 = 8$ ✓
(2): $-3(2) - 3 + 2(-1) = -6 - 3 - 2 = -11$ ✓
(3): $-2(2) + 3 + 2(-1) = -4 + 3 - 2 = -3$ ✓

![FIG-01-08-004: Four augmented matrices shown left to right for the system 2x + y − z = 8, −3x − y + 2z = −11, −2x + y + 2z = −3, each drawn as a three-by-four grid with a vertical rule before the constant column. Matrix 1 is the starting array. Matrix 2 has zeros in the first column below the pivot, with the operations performed written above the arrow leading to it. Matrix 3 has a zero added in the second column below the pivot. Matrix 4 is the upper triangular result with a shaded staircase of pivots running down the diagonal and a shaded triangle of zeros below it labelled 'all zeros below the diagonal'. A return arrow runs right to left beneath the matrices labelled 'back-substitution: solve the bottom row first, then work upward', with the three results z = −1, then y = 3, then x = 2 tagged at successive rows. A side panel lists the three legal row operations: swap two rows, scale a row by a nonzero constant, add a multiple of one row to another. A footer note reads 'eliminate downward, then substitute upward'.](../figures/FIG-01-08-004-gaussian-elimination-staircase.png)

> ---
> **Mentor's Margin**
>
> Two habits that save time on 3×3 systems.
>
> **Hunt for a leading 1 before you start.** If any row has $1$ as its first
> coefficient, swap it to the top. Clearing a column beneath a pivot of $1$
> needs no scaling and produces no fractions. A row swap is free.
>
> **Work strictly left to right, top to bottom.** Clear all of column 1,
> then all of column 2. Skipping around reintroduces zeros you already
> earned, and that is the most common way a 3×3 turns into a twenty-minute
> problem.
>
> ---

---

## 8.4 Recognizing Special Cases

### Worked Example 4 — No Solution

**Given.** Solve:

$$\begin{cases} x + 2y = 5 \\ 2x + 4y = 7 \end{cases}$$

**Solution.**

Multiply the first equation by $-2$:

$$-2x - 4y = -10$$

Add to the second:

$$(2x + 4y) + (-2x - 4y) = 7 + (-10) \implies 0 = -3$$

A contradiction. **No solution.**

**Why, structurally.** The left sides are proportional — the second is
exactly twice the first. The right sides are not: $7 \ne 2(5)$. Two lines
with identical slope and different intercepts. Parallel, and never meeting.

### Worked Example 5 — Infinitely Many Solutions

**Given.** Solve:

$$\begin{cases} 2x - 4y = 6 \\ -x + 2y = -3 \end{cases}$$

**Solution.**

Multiply the second equation by $2$:

$$-2x + 4y = -6$$

Add to the first:

$$0 = 0$$

Always true. The second equation is $-\tfrac{1}{2}$ times the first — it is
the same line wearing a different coat. **Infinitely many solutions.**

To state the answer, parametrize. From the first equation, $x = 2y + 3$. Let
$y = t$ range over the reals:

$$\text{Solution set: } \{(2t + 3,\; t) : t \in \mathbb{R}\}$$

Every point on that line satisfies both equations.

### The same signals in a 3×3 system

Nothing new happens with three equations. Eliminate as usual, and watch for a
row that goes all-zero on the coefficient side:

$$\left[\begin{array}{ccc|c} \ast & \ast & \ast & \ast \\ 0 & \ast & \ast & \ast \\ 0 & 0 & 0 & 4 \end{array}\right] \qquad \left[\begin{array}{ccc|c} \ast & \ast & \ast & \ast \\ 0 & \ast & \ast & \ast \\ 0 & 0 & 0 & 0 \end{array}\right]$$

The left one reads $0x + 0y + 0z = 4$. Contradiction — **no solution**.

The right one reads $0 = 0$. One equation was redundant, so two independent
equations are constraining three unknowns — **infinitely many solutions**,
forming a line in space.

And if all three diagonal pivots survive nonzero, as in Worked Example 3, the
solution is unique.

![FIG-01-08-005: Four small three-dimensional sketches of plane arrangements, each labelled with its outcome and the elimination signal. Sketch 1: three planes meeting at a single marked point, labelled 'unique solution — a pivot in every column'. Sketch 2: three planes intersecting along a common line, with the line drawn heavy, labelled 'infinitely many solutions — a row becomes all zeros including the constant'. Sketch 3: three parallel planes, labelled 'no solution — a row becomes all zeros with a nonzero constant'. Sketch 4: three planes forming a triangular prism arrangement where each pair meets in a line but no point is common to all three, labelled 'no solution — the pairwise intersections never coincide'. A footer strip reads 'the 3x3 signals are identical to the 2x2 signals — a zero row with a nonzero constant is still a contradiction'.](../figures/FIG-01-08-005-three-planes-outcomes.png)

> ---
> **Mentor's Margin**
>
> On the FE exam, dependent systems rarely appear as "find all solutions."
> They appear as a *classification* question — does this system have a unique
> solution? — because the answer carries physical meaning.
>
> Write equilibrium equations for a structure and get a dependent system, and
> your structure is a **mechanism**: it can move, and the equations cannot
> pin down a single force distribution because there isn't one. Get an
> inconsistent system from the same exercise and you have almost certainly
> made a sign error. Same algebra, two very different conclusions, and
> knowing which signal you saw is what tells them apart.
>
> ---

---

## 8.5 The 2×2 Determinant and Cramer's Rule

### The determinant of a 2×2 array

Take four numbers arranged in a square and enclose them in single vertical
bars. That notation means: compute one specific number from them.

$$\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

Multiply down the main diagonal and keep it. Multiply down the other diagonal
and subtract it. That is the whole definition — this is a self-contained piece
of arithmetic, and it is all you need here.

$$\begin{vmatrix} 4 & -3 \\ 2 & 5 \end{vmatrix} = (4)(5) - (2)(-3) = 20 + 6 = 26$$

The double negative in that second product is where most errors live. Write
the subtraction out before simplifying.

![FIG-01-08-006: A two-by-two array of the four coefficients a1, b1, a2, b2 enclosed in the single vertical bars that denote a determinant. Two diagonal arrows cross the array: a solid arrow from top-left to bottom-right labelled 'main diagonal, multiply and KEEP the sign, a1b2' and a dashed arrow from top-right to bottom-left labelled 'other diagonal, multiply and SUBTRACT, minus a2b1'. The result a1b2 − a2b1 is printed below in a box. Beside it a worked instance shows the array for 4, −3, 2, 5 resolving to 4 times 5 minus 2 times negative 3, equalling 20 plus 6, equalling 26, with a note 'watch the double negative'. A side panel reads 'single vertical bars mean determinant, a single number. Square brackets would mean the matrix itself, a table of numbers — different objects, and Chapter 01-14 separates them properly'.](../figures/FIG-01-08-006-determinant-cross-product-rule.png)

### Cramer's rule

For the system:

$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$$

build three determinants. The first, $D$, is made from the coefficients as
they stand:

$$D = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1$$

The other two come from $D$ by replacing one column with the constants:

$$D_x = \begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix} = c_1 b_2 - c_2 b_1 \qquad D_y = \begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix} = a_1 c_2 - a_2 c_1$$

Then:

$$\boxed{x = \frac{D_x}{D} \qquad y = \frac{D_y}{D}}$$

$D$ sits in the denominator both times, so the rule requires $D \ne 0$.

**And $D = 0$ is informative rather than merely inconvenient.** It says the
coefficient columns are proportional, which is exactly the condition for
parallel or coincident lines. So $D = 0$ means the system is dependent or
inconsistent — no unique solution — and that matches §8.1 exactly. To tell
which, look at the numerators:

- $D = 0$ and any numerator nonzero → **inconsistent**, no solution
- $D = D_x = D_y = 0$ → **dependent**, infinitely many solutions

![FIG-01-08-007: Three determinant arrays in a row for the system a1x + b1y = c1 and a2x + b2y = c2. The left array, labelled D, holds the four coefficients with its two columns tagged 'x-coefficients' and 'y-coefficients'. The centre array, labelled D_x, is the same except the first column has been replaced by the constants c1 and c2, shown shaded, with a curved arrow from a detached constants column into that position labelled 'constants replace the x-column'. The right array, labelled D_y, has the constants shaded in the second column instead, with a matching curved arrow labelled 'constants replace the y-column'. Beneath, the results x = D_x over D and y = D_y over D are boxed. A warning strip reads 'D sits in the denominator both times — if D = 0 the rule cannot be used, and the system is dependent or inconsistent rather than unique'.](../figures/FIG-01-08-007-cramer-column-replacement.png)

> ---
> **Mentor's Margin**
>
> The column-replacement pattern is the thing to hold onto. To solve for a
> variable, replace *that variable's* coefficient column with the constants,
> and divide by the untouched $D$. For $x$, the first column. For $y$, the
> second.
>
> This generalizes without modification. In Chapter 01-14 the same sentence
> applies to a 3×3 system — replace the $z$-column with the constants to get
> $D_z$ — with only the determinant arithmetic getting bigger. Learn the
> pattern now and 01-14 costs you one new recipe instead of a new idea.
>
> The real payoff is selective solving. If a problem asks only for $F_2$ and
> you have two equations, Cramer's rule gets you there with two determinants
> and no back-substitution. Elimination would make you find $F_1$ first
> whether you wanted it or not.
>
> ---

### Worked Example 6 — Cramer's Rule

**Given.** Solve using Cramer's rule:

$$4x - 3y = 11 \qquad 2x + 5y = -1$$

**Solution.**

Identify the pieces: $a_1 = 4$, $b_1 = -3$, $c_1 = 11$, $a_2 = 2$,
$b_2 = 5$, $c_2 = -1$.

$$D = \begin{vmatrix} 4 & -3 \\ 2 & 5 \end{vmatrix} = (4)(5) - (2)(-3) = 20 + 6 = 26$$

Nonzero, so a unique solution exists and the rule applies.

$$D_x = \begin{vmatrix} 11 & -3 \\ -1 & 5 \end{vmatrix} = (11)(5) - (-1)(-3) = 55 - 3 = 52$$

$$D_y = \begin{vmatrix} 4 & 11 \\ 2 & -1 \end{vmatrix} = (4)(-1) - (2)(11) = -4 - 22 = -26$$

$$x = \frac{52}{26} = 2 \qquad y = \frac{-26}{26} = -1$$

$$\boxed{x = 2, \quad y = -1}$$

**Verify:**

$4(2) - 3(-1) = 8 + 3 = 11$ ✓
$2(2) + 5(-1) = 4 - 5 = -1$ ✓

---

## 8.6 Setting Up Systems from Engineering Problems

Everything above is mechanical. This section is not. Once the equations are
on paper, solving them is bookkeeping; getting them onto paper is engineering.

**A systematic approach:**

1. **Name every unknown explicitly.** Write them down with units. Count them.
   Call that $n$.
2. **Write one equation per independent physical condition.** Each distinct
   physical law gives one equation: equilibrium in $x$, equilibrium in $y$,
   the voltage law around loop 1, the voltage law around loop 2, conservation
   of total mass, conservation of one species. Count them. Call that $m$.
3. **Compare $m$ with $n$ before solving.**
   - $m < n$: underdetermined. You are missing a condition — look again
     before you conclude the answer is indeterminate.
   - $m = n$: expect a unique solution, provided the equations are genuinely
     independent.
   - $m > n$: overdetermined. Solve with $n$ of them, then use the leftovers
     to **verify**. Do not silently discard them; a contradiction there means
     a setup error.
4. **Carry units from the first line.** A dimensional mismatch is trivial to
   spot while writing and expensive to find after solving.

Step 2 hides the hard part. "Independent" means the condition genuinely adds
information. Writing the same equilibrium equation twice in different
notation gives you two lines on paper and one equation in substance, and the
algebra will hand you $0 = 0$ to say so.

![FIG-01-08-008: A flowchart beginning with a box 'name every unknown explicitly, count them as n'. An arrow leads to 'write one equation per independent physical condition, count them as m'. A three-way decision diamond follows, comparing m with n. The branch m less than n leads to a box 'underdetermined — infinitely many solutions, look for a condition you have not used'. The branch m equals n leads to a box 'solve — expect a unique solution if the equations are independent'. The branch m greater than n leads to a box 'overdetermined — solve using n of them, then use the extras to verify rather than discarding them'. A parallel side rail running the height of the chart reads 'carry units at every step — a dimensional mismatch shows up while you are writing, not after you have solved'. A footer note reads 'the algebra is mechanical; this counting step is where the engineering judgement lives'.](../figures/FIG-01-08-008-setup-count-method.png)

### Worked Example 7 — Mixture Problem

**Given.** A chemist needs $500$ mL of a $30\%$ acid solution. She has a
$20\%$ stock and a $50\%$ stock. How many mL of each should she mix?

**Solution.**

**Step 1 — Name the unknowns.**

$V_1$ = volume of $20\%$ solution used, in mL
$V_2$ = volume of $50\%$ solution used, in mL

So $n = 2$.

**Step 2 — Independent physical conditions.**

Conservation of total volume:

$$V_1 + V_2 = 500 \quad (1)$$

Conservation of acid. Each term is a volume of acid: a fraction times a
volume of solution gives mL of acid on both sides.

$$0.20 V_1 + 0.50 V_2 = 0.30(500) = 150 \quad (2)$$

So $m = 2$. Matches $n$ — expect a unique solution.

**Step 3 — Solve.** Equation (1) offers a coefficient of $1$, so substitute.

$$V_1 = 500 - V_2$$

$$0.20(500 - V_2) + 0.50V_2 = 150$$
$$100 - 0.20V_2 + 0.50V_2 = 150$$
$$0.30V_2 = 50 \implies V_2 = \frac{50}{0.30} = \frac{500}{3} \approx 166.7 \text{ mL}$$

$$V_1 = 500 - \frac{500}{3} = \frac{1000}{3} \approx 333.3 \text{ mL}$$

$$\boxed{V_1 = \tfrac{1000}{3} \approx 333 \text{ mL of } 20\%, \quad V_2 = \tfrac{500}{3} \approx 167 \text{ mL of } 50\%}$$

**Verify using the exact fractions**, not the rounded values:

(1): $\dfrac{1000}{3} + \dfrac{500}{3} = \dfrac{1500}{3} = 500$ ✓

(2): $0.20\left(\dfrac{1000}{3}\right) + 0.50\left(\dfrac{500}{3}\right) = \dfrac{200}{3} + \dfrac{250}{3} = \dfrac{450}{3} = 150$ ✓

**Sanity check on the answer.** The target $30\%$ sits closer to the $20\%$
stock than to the $50\%$, so most of the mixture should be the weaker
solution. Two-thirds versus one-third. Consistent.

> ---
> **Mentor's Margin**
>
> Verify with exact values and round only at the end. Substituting $333$ and
> $167$ into equation (2) gives $150.1$, not $150$, and now you have to
> decide whether that gap is rounding or a mistake. Substituting the
> fractions gives exactly $150$ and the question never arises.
>
> This matters more than it looks on the exam, where distractors are
> sometimes built from plausible rounding paths. Carry the fraction, round
> once, at the end, to the precision the question asks for.
>
> ---

### Worked Example 8 — Kirchhoff's Laws

**Given.** The two-loop circuit shown. Two loops share a common branch
containing a $2\ \Omega$ resistor.

![FIG-01-08-009: Schematic of a two-loop resistive circuit sharing a common branch. The left loop contains a 12 volt source and a 5 ohm resistor; the right loop contains an 8 volt source and a 3 ohm resistor; the shared middle branch contains a 2 ohm resistor. Current I1 is arrowed clockwise in the left loop, I2 arrowed counter-clockwise in the right loop, and I3 arrowed downward through the shared branch, with the upper junction of the shared branch circled and labelled 'node'. Three annotation strips run beside the schematic: 'KVL around loop 1 gives 5I1 + 2I3 = 12', 'KVL around loop 2 gives 3I2 + 2I3 = 8', and 'KCL at the node gives I1 + I2 = I3'. A footer note reads 'three unknown currents, three independent conditions — two loop equations and one node equation'.](../figures/FIG-01-08-009-two-loop-circuit.png)

Kirchhoff's voltage law around each loop, and the current law at the node,
give:

$$5I_1 + 2I_3 = 12 \quad \text{(loop 1)} \quad (1)$$
$$3I_2 + 2I_3 = 8 \quad \text{(loop 2)} \quad (2)$$
$$I_1 + I_2 = I_3 \quad \text{(node)} \quad (3)$$

Find $I_1$, $I_2$, $I_3$ in amperes.

You are not expected to derive these here — circuit analysis is Tier 2E. What
this example asks is the algebra: three unknowns, three independent
conditions, solve.

**Solution.**

Equation (3) is already an isolation, so substitute $I_3 = I_1 + I_2$ into
both loop equations and reduce a 3×3 to a 2×2:

$$5I_1 + 2(I_1 + I_2) = 12 \implies 7I_1 + 2I_2 = 12 \quad (A)$$
$$3I_2 + 2(I_1 + I_2) = 8 \implies 2I_1 + 5I_2 = 8 \quad (B)$$

Eliminate $I_2$. Multiply (A) by $5$ and (B) by $2$:

$$35I_1 + 10I_2 = 60$$
$$4I_1 + 10I_2 = 16$$

Subtract the second from the first:

$$31I_1 = 44 \implies I_1 = \frac{44}{31} \approx 1.419 \text{ A}$$

From (B):

$$5I_2 = 8 - 2\left(\frac{44}{31}\right) = \frac{248 - 88}{31} = \frac{160}{31} \implies I_2 = \frac{32}{31} \approx 1.032 \text{ A}$$

From (3):

$$I_3 = \frac{44}{31} + \frac{32}{31} = \frac{76}{31} \approx 2.452 \text{ A}$$

$$\boxed{I_1 \approx 1.42 \text{ A}, \quad I_2 \approx 1.03 \text{ A}, \quad I_3 \approx 2.45 \text{ A}}$$

**Verify in all three originals, exactly:**

(1): $5\left(\dfrac{44}{31}\right) + 2\left(\dfrac{76}{31}\right) = \dfrac{220 + 152}{31} = \dfrac{372}{31} = 12$ ✓

(2): $3\left(\dfrac{32}{31}\right) + 2\left(\dfrac{76}{31}\right) = \dfrac{96 + 152}{31} = \dfrac{248}{31} = 8$ ✓

(3): $\dfrac{44}{31} + \dfrac{32}{31} = \dfrac{76}{31}$ ✓

**Sanity check.** All three currents are positive, so every assumed direction
in the figure was right. $I_3$ is the largest, which it must be — it carries
the sum of the other two.

> ---
> **Mentor's Margin**
>
> Notice the move that made this easy. Equation (3) gave one variable in
> terms of the others for free, so substituting it collapsed a 3×3 into a
> 2×2 before any elimination started.
>
> Look for that. Node equations in circuits, and geometric constraints in
> mechanics, are frequently of the form "this unknown is the sum of those
> two." Spend the substitution first and you do materially less work than
> running full Gaussian elimination on the original three.
>
> ---

---

## As the Handbook States It

> **Handbook 10.6, p. 37** — *Mathematics / Algebra*

The Handbook includes:

- The general form of a system of two linear equations
- Solution by determinants (Cramer's rule), for the 2×2 and 3×3 cases
- The 2×2 determinant, defined as $ad - bc$

**The Handbook does not include:**

- Gaussian elimination as a procedure
- Augmented matrix notation
- Row operation notation
- The classification into consistent, dependent, and inconsistent
- Any guidance on setting up a system from a physical situation

**Notation note.** The Handbook writes the 2×2 determinant as

$$\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

which is the notation used here. The 3×3 determinant expansion appears there
too; Chapter 01-14 works with it properly.

**Worth knowing about this page.** Cramer's rule being in the Handbook has a
practical consequence: on a two-equation problem you can look up the method
rather than recall it. Gaussian elimination is not there, and neither is the
setup methodology, so those must come from memory. Plan your studying
accordingly — the things that are absent from the Handbook are the things
worth over-learning.

---

## Where This Goes Wrong

**Verifying in only one equation.** Back-substitution into the equation you
solved from cannot fail — you constructed the answer to satisfy it. Substitute
into every original equation, including the ones you never used.

**Sign errors when subtracting equations.** Every term in the subtracted
equation flips, and forgetting one term is the single most common error in
this chapter. The defence: multiply that equation by $-1$ first, write it out,
then add. All the sign changes happen in one visible step instead of in your
head.

**Dropping a zero from the augmented matrix.** A missing term must be written
as $0$. Omitting it shifts every later coefficient one column left, and every
subsequent operation is then wrong in a way that still looks tidy.

**Reading $0 = 0$ as "no solution."** It means the opposite — infinitely many.
The no-solution signal is $0 = k$ with $k \ne 0$.

**Multiplying a row by zero.** Not a legal row operation. It is irreversible
and it discards a constraint, which changes the solution set.

**Replacing the wrong column in Cramer's rule.** For $x$, the constants go
into the first column. For $y$, the second. Swapping them returns the other
variable's value, which is an error that verifies cleanly against the wrong
equation and is therefore easy to miss.

**Using Cramer's rule without checking $D$ first.** Compute $D$ before
anything else. If it is zero, the rule does not apply, and the useful
question becomes *which* degenerate case you have.

**Isolating the awkward variable for substitution.** If any variable has
coefficient $1$, isolate that one. Isolating a variable with coefficient $7$
carries a fraction through every following line.

**Overdetermined systems with the extras thrown away.** Extra equations are
free verification. Discarding them hides contradictions that would have told
you the setup was wrong.

**Unit inconsistency across a single equation.** Both sides need the same
units, and every term within a side needs them too. In Worked Example 7,
every term of equation (2) is a volume of acid in mL — if one term had been a
percentage, the equation would be meaningless no matter how well it solves.

**Rounding before verifying.** Verify with exact values, round once at the
end. Rounding first creates small residuals that you then have to classify as
harmless or not.

---

## Key Terms

| Term | Definition |
|---|---|
| Linear system | A set of equations in which each variable appears only to the first power |
| Consistent system | Has at least one solution |
| Inconsistent system | Has no solution; the equations contradict each other |
| Independent system | Has exactly one solution |
| Dependent system | Has infinitely many solutions; the equations describe the same geometric object |
| Substitution | Solving by isolating one variable and replacing it in another equation |
| Elimination | Solving by adding multiples of equations so that a variable cancels |
| Gaussian elimination | Systematic reduction to upper triangular form using row operations |
| Augmented matrix | The coefficient array extended with the constant column, $[A \mid b]$ |
| Row operation | Swap, nonzero scaling, or adding a multiple of one row to another; preserves the solution set |
| Pivot | The leading nonzero entry of a row, used to clear the entries below it |
| Upper triangular form | All entries below the main diagonal are zero |
| Back-substitution | Solving from the bottom row upward once upper triangular form is reached |
| Determinant (2×2) | The number $ad - bc$ computed from a 2×2 array, written with single vertical bars |
| Cramer's rule | Solution as ratios of determinants: $x = D_x/D$, $y = D_y/D$ |
| Parametric solution | A solution written in terms of a free parameter, used for dependent systems |
| Underdetermined | Fewer independent equations than unknowns |
| Overdetermined | More equations than unknowns; the extras serve as verification |

---

## Review Questions

### Conceptual

1. What are the three possible outcomes when solving a linear system?
   Describe what each looks like geometrically for a 2×2 system, and give
   the algebraic signal for each.
2. During elimination you reach $0 = -7$. What does that mean about the
   system? What would $0 = 0$ have meant instead?
3. In Cramer's rule, what does $D = 0$ mean? Does it always mean there is
   no solution?
4. Why must you verify a solution in all original equations rather than just
   the one you used for back-substitution? Explain what the second kind of
   check can catch that the first cannot.
5. A force-equilibrium analysis produces an inconsistent system. What does
   that almost certainly indicate? Name the one case where a degenerate
   system is telling you something physically real instead.
6. Explain why a unique solution requires as many independent equations as
   unknowns.
7. Why is multiplying a row by zero excluded from the list of legal row
   operations, when multiplying by $3$ or by $-\tfrac{1}{2}$ is allowed?

### Calculation

8. Solve by substitution and verify in both equations:
   (a) $x + 2y = 10$ and $3x - y = 9$
   (b) $2x - 3y = 4$ and $x = 2y - 1$

9. Solve by elimination and verify in both equations:
   (a) $4x + 3y = 24$ and $2x - 5y = -14$
   (b) $5x - 2y = 9$ and $3x + 7y = -11$

10. Solve by Cramer's rule. Compute $D$ first and state what it tells you
    before going further.
    (a) $3x + y = 9$ and $x - 2y = -4$
    (b) $6x - 5y = 23$ and $4x + 3y = 9$

11. Solve by Gaussian elimination, showing the augmented matrix at each
    stage:
    (a) $\begin{cases} x + y + z = 6 \\ 2x - y + 3z = 9 \\ -x + 2y - z = 0 \end{cases}$
    (b) $\begin{cases} 2x + y - z = 8 \\ x + 3y + 2z = 4 \\ 3x - y + z = 7 \end{cases}$

12. Classify each system **without** fully solving it, and justify:
    (a) $3x - 6y = 9$ and $-x + 2y = -3$
    (b) $2x + 4y = 8$ and $x + 2y = 6$
    (c) $x - y = 4$ and $2x + y = 11$

13. **Engineering.** A resistor network produces the system

    $$\begin{cases}
    R_1 + R_2 = 12 \\
    2R_1 + R_3 = 14 \\
    R_2 + 2R_3 = 20
    \end{cases}$$

    with all values in kilohms. Find $R_1$, $R_2$, $R_3$, and verify in all
    three equations.

14. **Engineering.** Two pipes feed a tank. Pipe A fills it at rate $r_A$
    tanks per hour, pipe B at rate $r_B$.

    - Running together they fill the tank in $4$ hours.
    - Pipe A alone fills it $6$ hours faster than pipe B alone.

    (a) Write both conditions as equations. Use the fill *times*
    $T_A = 1/r_A$ and $T_B = 1/r_B$ as your unknowns rather than the rates,
    and explain why that choice makes the algebra easier.
    (b) Solve. You will get a quadratic (Chapter 01-07); both roots are
    mathematically valid, so check each against the physical domain.
    (c) How long does pipe A alone take?

15. **Engineering.** Two members meet at a pin joint. Resolving the applied
    load into components gives:

    $$F_1\cos 30° + F_2\cos 60° = P_x$$
    $$F_1\sin 30° + F_2\sin 60° = P_y$$

    For $P_x = 5$ kN and $P_y = 10$ kN, find $F_1$ and $F_2$. Use these
    values as given numbers — no trigonometry is required here, only the
    algebra:

    $$\cos 30° = \sin 60° = \frac{\sqrt{3}}{2} \qquad \sin 30° = \cos 60° = \frac{1}{2}$$

    Keep $\sqrt{3}$ exact until the final step. Interpret the sign of each
    answer.

### Multiple Choice

16. During elimination, the equation $0 = 5$ appears. This means:
    A) The system has infinitely many solutions
    B) One variable equals 5
    C) The system has no solution
    D) An arithmetic error must have been made

17. For the system $ax + by = e$ and $cx + dy = f$, Cramer's rule gives $x$
    as:
    A) $\dfrac{ed - bf}{ad - bc}$
    B) $\dfrac{ad - bc}{ed - bf}$
    C) $\dfrac{af - ce}{ad - bc}$
    D) $\dfrac{eb - fa}{ad - bc}$

18. The system $3x - 6y = 9$ and $-x + 2y = -3$ is:
    A) Consistent and independent
    B) Consistent and dependent
    C) Inconsistent
    D) Indeterminate without solving

19. A unique solution to a system in 4 unknowns requires how many
    independent equations?
    A) 2
    B) 3
    C) 4
    D) 5

20. Which operation on an augmented matrix does **not** preserve the
    solution set?
    A) Swapping two rows
    B) Multiplying a row by zero
    C) Adding a multiple of one row to another
    D) Multiplying a row by $-2$

21. After Gaussian elimination a 3×3 system has bottom row
    $[\,0 \;\; 0 \;\; 0 \mid 0\,]$. The system:
    A) Has no solution
    B) Has exactly one solution
    C) Has infinitely many solutions
    D) Has exactly three solutions

22. For a 2×2 system, $D = 0$ and $D_x = 6$. The system is:
    A) Consistent and independent
    B) Consistent and dependent
    C) Inconsistent
    D) Solvable, with $x = 6$

---

## Answer Key with Explanations

**1.** Three outcomes.

**Consistent and independent** — one solution. Two lines of different slope
crossing at a point. Signal: elimination isolates a variable value.

**Consistent and dependent** — infinitely many solutions. One line, described
twice, because one equation is a multiple of the other. Signal: an equation
reduces to $0 = 0$.

**Inconsistent** — no solution. Two parallel lines. Signal: an equation
reduces to $0 = k$ with $k \ne 0$. (§8.1)

**2.** $0 = -7$ is a contradiction; nothing can satisfy it, so the system is
**inconsistent** with no solution, and the lines are parallel. $0 = 0$ is
vacuously true, which means one equation duplicated information already in
another — the system is **consistent and dependent**, with infinitely many
solutions. (§8.4)

**3.** $D = 0$ puts a zero in the denominator, so Cramer's rule cannot be
applied. Structurally it means the coefficient columns are proportional,
which is the condition for parallel or coincident lines — so the system has
no unique solution. It does **not** by itself mean no solution. Check the
numerators: if $D = 0$ with any numerator nonzero, the system is
inconsistent; if $D = D_x = D_y = 0$, it is dependent with infinitely many
solutions. (§8.5)

**4.** Back-substitution derives the remaining variable *from* one of the
equations. Substituting the result back into that same equation is circular —
it will confirm as long as your arithmetic was internally consistent, whatever
errors preceded it.

The equations that were never used to construct the answer are the only
independent test. They catch sign errors made during elimination, a
mis-scaled row, and transcription slips in the augmented matrix. All of those
produce a self-consistent wrong answer that the circular check passes
happily. (§8.2, §8.3)

**5.** Almost certainly a setup error: a sign error, a condition applied
twice, or the same equilibrium equation written twice in different form. A
joint genuinely in equilibrium has a solution, so contradiction means the
equations misrepresent the physics.

The real exception is **dependency**, not inconsistency. A dependent
equilibrium system can mean the structure is a mechanism — it can move, and
no unique force distribution exists. That is physics, not an error. The
distinction is the signal: $0 = k$ means check your work, $0 = 0$ means check
your structure. (§8.1, §8.4)

**6.** Each unknown contributes one degree of freedom. Each independent
equation removes one. With $n$ unknowns and fewer than $n$ independent
equations, degrees of freedom survive and the solution set is a line, plane,
or hyperplane — infinitely many points. With $n$ independent equations
against $n$ unknowns, all degrees of freedom are consumed and exactly one
point remains.

The word *independent* is doing real work. Three equations in three unknowns
where one is the sum of the other two supply only two independent constraints
and leave one degree of freedom. (§8.1, §8.6)

**7.** Legality comes down to reversibility. Scaling by $3$ is undone by
scaling by $\tfrac{1}{3}$, so no information is lost and the solution set is
untouched. Scaling by zero cannot be undone — the row becomes $0 = 0$ and the
original equation is unrecoverable. A constraint has been discarded, so the
new system generally has *more* solutions than the old one, which is exactly
what "preserves the solution set" forbids. (§8.3)

**8.**

(a) From equation 1: $x = 10 - 2y$. Substitute into equation 2:

$$3(10 - 2y) - y = 9 \implies 30 - 7y = 9 \implies 7y = 21 \implies y = 3$$

$$x = 10 - 2(3) = 4$$

$$\boxed{x = 4, \; y = 3}$$

Verify: $4 + 2(3) = 10$ ✓ and $3(4) - 3 = 9$ ✓

(b) $x = 2y - 1$ is already isolated. Substitute:

$$2(2y - 1) - 3y = 4 \implies 4y - 2 - 3y = 4 \implies y = 6$$

$$x = 2(6) - 1 = 11$$

$$\boxed{x = 11, \; y = 6}$$

Verify: $2(11) - 3(6) = 22 - 18 = 4$ ✓ and $11 = 2(6) - 1$ ✓

**9.**

(a) Multiply equation 2 by $-2$: $-4x + 10y = 28$. Add to equation 1:

$$13y = 52 \implies y = 4$$

From equation 1: $4x = 24 - 3(4) = 12$, so $x = 3$.

$$\boxed{x = 3, \; y = 4}$$

Verify: $4(3) + 3(4) = 24$ ✓ and $2(3) - 5(4) = 6 - 20 = -14$ ✓

(b) Eliminate $y$. Multiply equation 1 by $7$ and equation 2 by $2$:

$$35x - 14y = 63$$
$$6x + 14y = -22$$

Add: $41x = 41$, so $x = 1$.

From equation 1: $-2y = 9 - 5 = 4$, so $y = -2$.

$$\boxed{x = 1, \; y = -2}$$

Verify: $5(1) - 2(-2) = 5 + 4 = 9$ ✓ and $3(1) + 7(-2) = 3 - 14 = -11$ ✓

**10.**

(a) $D = (3)(-2) - (1)(1) = -6 - 1 = -7$. Nonzero, so a unique solution
exists.

$$D_x = (9)(-2) - (-4)(1) = -18 + 4 = -14 \qquad D_y = (3)(-4) - (1)(9) = -12 - 9 = -21$$

$$x = \frac{-14}{-7} = 2 \qquad y = \frac{-21}{-7} = 3$$

$$\boxed{x = 2, \; y = 3}$$

Verify: $3(2) + 3 = 9$ ✓ and $2 - 2(3) = -4$ ✓

(b) $D = (6)(3) - (4)(-5) = 18 + 20 = 38$. Nonzero — unique solution.

$$D_x = (23)(3) - (9)(-5) = 69 + 45 = 114 \qquad D_y = (6)(9) - (4)(23) = 54 - 92 = -38$$

$$x = \frac{114}{38} = 3 \qquad y = \frac{-38}{38} = -1$$

$$\boxed{x = 3, \; y = -1}$$

Verify: $6(3) - 5(-1) = 18 + 5 = 23$ ✓ and $4(3) + 3(-1) = 12 - 3 = 9$ ✓

**11.**

(a) The first row already has a leading $1$, so no swap is needed.

$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 2 & -1 & 3 & 9 \\ -1 & 2 & -1 & 0 \end{array}\right]$$

$R_2 \leftarrow R_2 - 2R_1$ gives $[\,0 \;\; -3 \;\; 1 \mid -3\,]$
$R_3 \leftarrow R_3 + R_1$ gives $[\,0 \;\;\;\; 3 \;\; 0 \mid \;\;\; 6\,]$

$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & -3 & 1 & -3 \\ 0 & 3 & 0 & 6 \end{array}\right]$$

Row 3 happens to give $y$ directly: $3y = 6$, so $y = 2$.

From row 2: $-3(2) + z = -3 \implies z = 3$.
From row 1: $x + 2 + 3 = 6 \implies x = 1$.

$$\boxed{x = 1, \; y = 2, \; z = 3}$$

Verify: $1 + 2 + 3 = 6$ ✓; $2(1) - 2 + 3(3) = 2 - 2 + 9 = 9$ ✓;
$-1 + 2(2) - 3 = -1 + 4 - 3 = 0$ ✓

(b) Swap $R_1$ and $R_2$ to get a leading $1$ and avoid fractions:

$$\left[\begin{array}{ccc|c} 1 & 3 & 2 & 4 \\ 2 & 1 & -1 & 8 \\ 3 & -1 & 1 & 7 \end{array}\right]$$

$R_2 \leftarrow R_2 - 2R_1$ gives $[\,0 \;\; -5 \;\; -5 \mid \;\;\; 0\,]$
$R_3 \leftarrow R_3 - 3R_1$ gives $[\,0 \;\; -10 \;\; -5 \mid -5\,]$

$$\left[\begin{array}{ccc|c} 1 & 3 & 2 & 4 \\ 0 & -5 & -5 & 0 \\ 0 & -10 & -5 & -5 \end{array}\right]$$

$R_3 \leftarrow R_3 - 2R_2$ gives $[\,0 \;\; 0 \;\; 5 \mid -5\,]$

$$\left[\begin{array}{ccc|c} 1 & 3 & 2 & 4 \\ 0 & -5 & -5 & 0 \\ 0 & 0 & 5 & -5 \end{array}\right]$$

Row 3: $5z = -5 \implies z = -1$.
Row 2: $-5y - 5(-1) = 0 \implies -5y = -5 \implies y = 1$.
Row 1: $x + 3(1) + 2(-1) = 4 \implies x + 1 = 4 \implies x = 3$.

$$\boxed{x = 3, \; y = 1, \; z = -1}$$

Verify: $2(3) + 1 - (-1) = 6 + 1 + 1 = 8$ ✓;
$3 + 3(1) + 2(-1) = 3 + 3 - 2 = 4$ ✓;
$3(3) - 1 + (-1) = 9 - 1 - 1 = 7$ ✓

**12.**

(a) Multiply the second equation by $-3$: $3x - 6y = 9$ — **identical** to
the first, constants included. Same line. **Consistent and dependent**,
infinitely many solutions.

(b) Multiply the second equation by $2$: $2x + 4y = 12$. Left side matches
the first equation; right side does not ($12 \ne 8$). Same slope, different
intercept. **Inconsistent**, no solution.

(c) The coefficient ratios differ — $1:-1$ against $2:1$ — so the lines have
different slopes and must cross exactly once. **Consistent and independent**.
Solving confirms $(5, 1)$, but the classification did not require it.

**13.** From equation 1: $R_1 = 12 - R_2$.

Substitute into equation 2:

$$2(12 - R_2) + R_3 = 14 \implies 24 - 2R_2 + R_3 = 14 \implies R_3 = 2R_2 - 10$$

Substitute that into equation 3:

$$R_2 + 2(2R_2 - 10) = 20 \implies 5R_2 - 20 = 20 \implies R_2 = 8$$

$$R_3 = 2(8) - 10 = 6 \qquad R_1 = 12 - 8 = 4$$

$$\boxed{R_1 = 4 \text{ k}\Omega, \quad R_2 = 8 \text{ k}\Omega, \quad R_3 = 6 \text{ k}\Omega}$$

Verify: $4 + 8 = 12$ ✓; $2(4) + 6 = 14$ ✓; $8 + 2(6) = 20$ ✓

All three positive, as resistances must be.

**14.**

(a) Working in times rather than rates is the whole trick. The second
condition — "A is 6 hours faster" — is a statement about *times*, and in
terms of times it is linear:

$$T_A = T_B - 6$$

In terms of rates it would be $1/r_A = 1/r_B - 6$, with unknowns in
denominators. Choosing $T_A$ and $T_B$ keeps that condition clean and pushes
the nonlinearity into the other equation, where it is easier to handle.

The first condition says the rates add, and rate is the reciprocal of time:

$$\frac{1}{T_A} + \frac{1}{T_B} = \frac{1}{4}$$

(b) Substitute $T_A = T_B - 6$:

$$\frac{1}{T_B - 6} + \frac{1}{T_B} = \frac{1}{4}$$

Multiply through by $4T_B(T_B - 6)$:

$$4T_B + 4(T_B - 6) = T_B(T_B - 6)$$
$$8T_B - 24 = T_B^2 - 6T_B$$
$$T_B^2 - 14T_B + 24 = 0$$
$$(T_B - 12)(T_B - 2) = 0$$

$T_B = 12$ or $T_B = 2$. Both satisfy the quadratic; the physics decides.

$T_B = 2$ gives $T_A = 2 - 6 = -4$ hours. Negative time — **physically
extraneous**, reject.

$T_B = 12$ gives $T_A = 6$ hours. Both positive, so this is the answer.

$$r_A = \tfrac{1}{6}, \qquad r_B = \tfrac{1}{12} \text{ tanks per hour}$$

(c) Pipe A alone takes $\boxed{6 \text{ hours}}$.

Verify: $\tfrac{1}{6} + \tfrac{1}{12} = \tfrac{2}{12} + \tfrac{1}{12} =
\tfrac{3}{12} = \tfrac{1}{4}$, so together they fill in $4$ hours ✓ And
$6 = 12 - 6$ ✓

Note the pattern from Chapter 01-07: the algebra produced two valid roots
and the physical domain eliminated one. Always check.

**15.** Substituting the given values:

$$\frac{\sqrt{3}}{2}F_1 + \frac{1}{2}F_2 = 5 \quad (1)$$
$$\frac{1}{2}F_1 + \frac{\sqrt{3}}{2}F_2 = 10 \quad (2)$$

Multiply equation (1) by $\sqrt{3}$, which makes the $F_2$ coefficients
match:

$$\frac{3}{2}F_1 + \frac{\sqrt{3}}{2}F_2 = 5\sqrt{3}$$

Subtract equation (2):

$$\left(\frac{3}{2} - \frac{1}{2}\right)F_1 = 5\sqrt{3} - 10 \implies F_1 = 5\sqrt{3} - 10$$

$$F_1 \approx 8.66 - 10 = -1.34 \text{ kN}$$

For $F_2$, from equation (1):

$$\frac{1}{2}F_2 = 5 - \frac{\sqrt{3}}{2}\left(5\sqrt{3} - 10\right) = 5 - \frac{15 - 10\sqrt{3}}{2} = \frac{10 - 15 + 10\sqrt{3}}{2} = \frac{10\sqrt{3} - 5}{2}$$

$$F_2 = 10\sqrt{3} - 5 \approx 17.32 - 5 = 12.32 \text{ kN}$$

$$\boxed{F_1 = 5\sqrt{3} - 10 \approx -1.34 \text{ kN}, \quad F_2 = 10\sqrt{3} - 5 \approx 12.32 \text{ kN}}$$

Verify exactly:

(1): $\dfrac{\sqrt{3}}{2}(5\sqrt{3} - 10) + \dfrac{1}{2}(10\sqrt{3} - 5) =
\dfrac{15 - 10\sqrt{3} + 10\sqrt{3} - 5}{2} = \dfrac{10}{2} = 5$ ✓

(2): $\dfrac{1}{2}(5\sqrt{3} - 10) + \dfrac{\sqrt{3}}{2}(10\sqrt{3} - 5) =
\dfrac{5\sqrt{3} - 10 + 30 - 5\sqrt{3}}{2} = \dfrac{20}{2} = 10$ ✓

**Interpretation of the signs.** Under the convention that positive means
tension, $F_2$ is in tension and $F_1$, being negative, is in **compression**.
This is not an error and needs no fixing — it means the assumed direction for
$F_1$ in the free-body diagram was opposite to the actual force. The magnitude
$1.34$ kN is correct; only the arrow was drawn the wrong way.

Contrast this with question 14, where a negative answer was physically
impossible and had to be rejected. A negative *time* is meaningless. A
negative *force* under a sign convention is meaningful. Knowing which
situation you are in is the judgement the sign check requires.

**16. C — no solution.** $0 = 5$ is a contradiction; no assignment of the
variables satisfies it. (D) is tempting but wrong — a contradiction is a
legitimate outcome, and inconsistent systems exist. (§8.4)

**17. A.** $D_x$ replaces the $x$-coefficient column with the constants:

$$D_x = \begin{vmatrix} e & b \\ f & d \end{vmatrix} = ed - fb$$

and $D = ad - bc$, so $x = (ed - bf)/(ad - bc)$. (C) is $y$, formed by
replacing the second column instead. (D) reverses both products in the
numerator, a sign error. (B) inverts the ratio. (§8.5)

**18. B — consistent and dependent.** Multiplying the second equation by
$-3$ reproduces the first exactly. One line described twice; infinitely many
solutions. (§8.4)

**19. C — 4.** A unique solution needs as many independent equations as
unknowns. Fewer leaves degrees of freedom; more is permissible but redundant.
(§8.1, §8.6)

**20. B — multiplying a row by zero.** It is irreversible and discards a
constraint, so the solution set can grow. The other three are the legal row
operations, and each has an inverse of the same kind. (§8.3)

**21. C — infinitely many solutions.** That row reads $0 = 0$: one equation
was redundant, so two independent equations constrain three unknowns and one
degree of freedom survives. The solution set is a line in space. A bottom row
of $[\,0\;0\;0 \mid 4\,]$ would have been (A) instead. (§8.4)

**22. C — inconsistent.** $D = 0$ rules out a unique solution, so (A) is out.
With a numerator nonzero, the degenerate case is the contradictory one: no
solution. Dependency would require $D = D_x = D_y = 0$. (D) misreads $D_x$ as
a value of $x$ — it is a determinant, and dividing it by $D = 0$ is exactly
what cannot be done. (§8.5)

---

## Quick Reference

**Three outcomes**

| Algebra signal | Geometric picture | Solutions |
|---|---|---|
| A variable value is isolated | Intersect at one point | Unique |
| $0 = 0$ | Same line or plane | Infinite |
| $0 = k$, $k \ne 0$ | Parallel; never meet | None |

**Legal row operations**

Swap two rows · scale a row by a **nonzero** constant · add a multiple of one
row to another. Never scale by zero.

**Gaussian elimination**

Build $[A \mid b]$, using $0$ for every missing term. Swap a leading $1$ to
the top if one is available. Clear column 1 below the pivot, then column 2.
Reach upper triangular form, then back-substitute from the bottom row upward.

**2×2 determinant**

$$\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

**Cramer's rule (2×2)** — *Handbook p. 37*

$$D = a_1b_2 - a_2b_1 \qquad x = \frac{D_x}{D} \qquad y = \frac{D_y}{D}$$

$D_x$: constants replace the $x$-column. $D_y$: constants replace the
$y$-column. Compute $D$ first.

$D = 0$ with a nonzero numerator → inconsistent.
$D = D_x = D_y = 0$ → dependent.

**Setup method**

Count unknowns $n$ → count independent conditions $m$ → compare:
$m < n$ underdetermined, $m = n$ expect unique, $m > n$ solve with $n$ and
verify with the rest. Carry units throughout. Verify in every original
equation, using exact values.

**Not in the Handbook — memorize**

Gaussian elimination · augmented matrix and row operation notation ·
inconsistent versus dependent recognition · setup methodology

---

## What's Next

Apprentice, systems are done. You now have the algebraic machinery for every
multi-variable problem in this guide, and — worth noticing — you have already
met the augmented matrix, row operations, and the determinant. Chapter 01-14
will not introduce those. It will generalize them.

In **Chapter 01-09: Analytic Geometry**, we move from equations to shapes:
lines, circles, parabolas, and ellipses as geometric objects defined by
equations. That connects the function work from Chapter 01-06 to the
geometric formulas in the Handbook, and to the coordinate geometry that runs
through surveying, structural layout, and every Tier 2C problem involving a
distance, an angle, or a centroid.

Chapter 01-10 then extends this into three dimensions and introduces vectors
properly — the language of force, velocity, and field throughout all of
Tier 2.

Bring the Handbook to page 37. The Analytic Geometry section starts there.

See you there.

— Your Mentor
