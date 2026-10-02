---
chapter: "01-27"
title: "Algorithm and Logic Development"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-027-01, MATH-1C-027-02, MATH-1C-027-03, MATH-1C-027-04, MATH-1C-027-05, MATH-1C-027-06, MATH-1C-027-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-27: Algorithm and Logic Development

> *"A correct calculation solves one case. A correct algorithm explains how to
> solve every case in the class—and what to do when the assumptions fail."*

---

## Before You Start

**Prerequisites:** [01-04 Expressions, Equations, and Inequalities](01-04-Expressions-Equations-and-Inequalities.md) ·
[01-06 Functions, Graphs, and Transformations](01-06-Functions-Graphs-and-Transformations.md) ·
[01-08 Systems of Linear Equations](01-08-Systems-of-Linear-Equations.md) ·
[01-16 Limits and Continuity](01-16-Limits-and-Continuity.md) ·
[01-26 Numerical Methods](01-26-Numerical-Methods.md)

**Skip if:** You can convert a verbal engineering procedure into a flowchart and
language-neutral pseudocode; distinguish assignment from comparison; trace a
conditional or loop by hand; identify off-by-one and nontermination errors;
write guarded Newton, bisection, Simpson, and Euler algorithms; define inputs,
outputs, preconditions, and stopping conditions; and compare simple algorithms
using order-of-growth reasoning.

**Time:** About 100–120 min reading and worked examples · 40–50 min review
questions · 60–80 min practice problems.

**Working convention:** Pseudocode in this chapter is intentionally
language-neutral. Where the FE Reference Handbook supplies pseudocode conventions,
this chapter follows them when practical: `=` means assignment, `==` means
comparison, `<>` means not equal, and the words `and` and `or` are used for
Boolean operators. Unless a problem explicitly says otherwise, array indices are
treated as beginning at 1 when demonstrating the Handbook convention.

---

## On the Board Today

Apprentice, you already know how to perform calculations. This chapter asks a
different question:

**Could another person—or a computer—perform the same calculation correctly from
your instructions alone?**

If the answer depends on "you know what I meant," you do not yet have an
algorithm.

A usable algorithm must make the hidden decisions visible:

- What information comes in?
- What result must come out?
- What assumptions must be true before the procedure starts?
- What happens first?
- Where can the path branch?
- What repeats?
- What makes the repetition stop?
- What happens when the expected condition is not met?
- How do you know the answer is credible?

Those questions connect directly to Chapter 01-26. Newton's method is not merely

$$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}.$$

An executable Newton algorithm also needs an initial estimate, a tolerance, a
maximum iteration count, a derivative guard, a convergence test, a failure path,
and a returned status.

The formula is mathematics.

The guarded sequence of decisions is an algorithm.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **27.1** Define an algorithm by its inputs, outputs, sequence, decisions, repetition, and termination
* **27.2** State useful preconditions, postconditions, and failure conditions for an engineering calculation
* **27.3** Read and construct flowcharts using standard start/stop, process, input/output, and decision symbols
* **27.4** Translate a flowchart into clear language-neutral pseudocode
* **27.5** Distinguish assignment from equality comparison and trace variable state through a procedure
* **27.6** Construct Boolean conditions using comparison operators, `and`, `or`, and logically complete branches
* **27.7** Use `for`, `while`, and post-test loops appropriately and identify off-by-one errors
* **27.8** Use counters, accumulators, flags, and sentinels without corrupting loop state
* **27.9** Add tolerance, iteration-limit, and validity guards to numerical algorithms
* **27.10** Convert bisection, Newton iteration, Simpson integration, and Euler marching into pseudocode
* **27.11** Design test cases that exercise nominal, boundary, invalid-input, and failure paths
* **27.12** Compare simple algorithms using order-of-growth reasoning and distinguish correctness from efficiency

---

## Notation Used Here

| Symbol / form | Meaning in this chapter | Notes |
|---|---|---|
| `x = expression` | assignment | store the value of the expression in `x` |
| `x == y` | equality comparison | Boolean result |
| `x <> y` | not-equal comparison | Handbook pseudocode convention |
| `<, <=, >, >=` | comparison operators | result is Boolean |
| `and`, `or` | logical conjunction / disjunction | evaluate conditions, not arithmetic |
| `if ... then` | conditional branch | executes only when condition is true |
| `else` | alternate branch | paired with an `if` |
| `for` | count-controlled loop | preferred when iteration count is known |
| `while` | pre-test loop | may execute zero times |
| `do ... while` | post-test loop | executes at least once |
| `k` | loop or iteration index | local meaning |
| `count` | number of qualifying events | initialize deliberately |
| `sum` | accumulator | initialize before the loop |
| `tol` | numerical tolerance | must be positive |
| `maxIter` | maximum allowed iterations | prevents uncontrolled looping |
| `status` | outcome flag or label | e.g. `"converged"` or `"failed"` |
| $O(g(n))$ | order of growth | asymptotic scaling, not an exact runtime |

**Collision note.** `=` is used for mathematical equality in equations throughout
the guide, but in the Handbook's pseudocode convention it means **assignment**.
When reading pseudocode, interpret symbols according to the code context.

---

## 27.1 From a Calculation to an Algorithm

An **algorithm** is a finite, unambiguous procedure that transforms specified
inputs into specified outputs.

A useful engineering algorithm has more structure than a list of formulas.

### The contract

Before writing steps, define four things.

**Inputs:** What values enter the procedure?

**Outputs:** What values or decisions must be returned?

**Preconditions:** What must already be true?

**Postconditions:** What must be true when the algorithm reports success?

Suppose the task is to compute the volume of a cylinder.

Inputs:

$$r,\ h$$

Output:

$$V$$

Preconditions:

$$r\ge0,\qquad h\ge0.$$

Procedure:

$$V=\pi r^2h.$$

Postcondition:

$$V\ge0$$

with units of length cubed.

That is already better than writing only the formula, because negative geometric
dimensions now have a defined response instead of silently producing a number.

### Failure is part of the design

An algorithm that can encounter invalid input but has no invalid-input path is
incomplete.

For the cylinder example:

```text
if r < 0 or h < 0 then
    status = "invalid geometry"
    stop
end if

V = pi * r * r * h
status = "ok"
```

The failure condition is not an inconvenience added after the math. It is part of
the specification.

![FIG-01-27-001: An algorithm contract diagram with four labeled boxes arranged left to right: Inputs and Preconditions feed a central Procedure box, which feeds Outputs and Postconditions. A red side branch from the Procedure box leads to Failure Status. The worked cylinder example is embedded below: inputs r and h; precondition r≥0 and h≥0; process V=πr²h; output V; postcondition V≥0 with volume units.](../figures/FIG-01-27-001-algorithm-contract.png)

### Worked Example 1 — Turn a Formula into a Guarded Procedure

**Given.** A circular cross-section has diameter $d$ and carries axial load $F$.
Compute average normal stress

$$\sigma=\frac{F}{A},\qquad A=\frac{\pi d^2}{4}.$$

**Find.** A guarded algorithm specification.

**Approach.** Identify the physical invalid case before performing division.

**Solution.**

Inputs:

- `F`
- `d`

Precondition:

$$d>0.$$

Pseudocode:

```text
procedure axialStress(F: float; d: float)

    if d <= 0 then
        write("invalid diameter")
        return
    end if

    A = pi * d * d / 4
    sigma = F / A

    write(sigma)

end procedure
```

**Check.** Division by zero is impossible on the success path. The sign of
$\sigma$ is allowed to follow the sign convention assigned to $F$.

> ---
> **Mentor's Margin**
>
> A precondition is not merely something you hope is true. Either the problem
> guarantees it, or your algorithm checks it.
>
> ---

---

## 27.2 Flowcharts — Making Control Flow Visible

A **flowchart** is a graphical representation of control flow.

The Handbook's Electrical and Computer Engineering section includes a
*Flowchart Definition* showing standard symbols for process/operation,
start-or-stop point, data input/output, document, database, and decision.

For general FE algorithm problems, four shapes do most of the work:

| Shape | Meaning | Typical content |
|---|---|---|
| rounded terminal | start / stop | `START`, `END` |
| rectangle | process | assignment or calculation |
| parallelogram | input / output | read or display data |
| diamond | decision | yes/no or true/false condition |

Arrows show the order of execution.

### Decisions need labeled exits

A decision diamond should ask a question with unambiguous outgoing paths.

Good:

> `d > 0 ?`

with branches labeled **Yes** and **No**.

Weak:

> `Check diameter`

That is an instruction, not a condition.

### A flowchart is not a poster

Do not put the entire derivation inside one process rectangle.

The value of a flowchart is the path:

1. start,
2. read,
3. validate,
4. compute,
5. branch if needed,
6. report,
7. stop.

![FIG-01-27-002: A textbook flowchart-symbol reference. Four large symbols are shown with labels: rounded terminal START/STOP, rectangle PROCESS, parallelogram DATA I/O, and diamond DECISION. Beneath them a complete example reads diameter d, tests d>0, sends the No branch to "report invalid input" and STOP, and sends the Yes branch to "A=πd²/4; sigma=F/A", then output sigma and STOP. All decision exits are explicitly labeled Yes/No.](../figures/FIG-01-27-002-flowchart-symbols-and-guard.png)

### Worked Example 2 — Flowchart Logic for a Temperature Status

**Given.** A machine temperature $T$ is classified:

- below 70 °C: normal,
- 70 °C through 89 °C: caution,
- 90 °C or above: trip.

**Find.** A logically complete decision structure.

**Approach.** Test thresholds from highest consequence downward.

**Solution.**

```text
read(T)

if T >= 90 then
    status = "trip"
else if T >= 70 then
    status = "caution"
else
    status = "normal"
end if

write(status)
```

Why does the middle branch not need `T < 90` explicitly?

Because reaching it already means the first condition `T >= 90` was false.

Therefore the path itself establishes

$$T<90.$$

Combined with `T >= 70`, the middle branch represents

$$70\le T<90.$$

**Boundary check.**

- $T=69.9$ → normal
- $T=70.0$ → caution
- $T=89.9$ → caution
- $T=90.0$ → trip

Testing exact boundaries is mandatory whenever inequalities define categories.

---

## 27.3 Pseudocode and State Tracing

**Pseudocode** expresses algorithm structure without tying the reader to a
specific programming language.

The Handbook explicitly says its software code is pseudocode rather than a
specific language. Its listed conventions include:

- no end-of-line punctuation such as semicolons,
- comments indicated by `--`,
- `if` statements with `if` and `then`,
- loop structures closed with an `end ...` form,
- `=` for assignment,
- `==` for comparison,
- `<>` for not equal,
- logical `and` and `or` written as words,
- array indices in square brackets,
- arrays beginning at 1 unless otherwise specified.

This chapter uses that style where it improves FE familiarity.

### Assignment changes state

Consider:

```text
x = 5
x = x + 2
```

The second line does **not** claim the mathematical equation

$$x=x+2.$$

It means:

1. evaluate the current value of `x + 2`,
2. obtain 7,
3. replace the stored value of `x` with 7.

The variable state has changed.

### Trace tables

A **trace table** records variable values after each significant step.

Example:

```text
sum = 0

for k = 1 to 4
    sum = sum + k * k
end for
```

Trace:

| Iteration | $k$ | old `sum` | added $k^2$ | new `sum` |
|---:|---:|---:|---:|---:|
| start | — | — | — | 0 |
| 1 | 1 | 0 | 1 | 1 |
| 2 | 2 | 1 | 4 | 5 |
| 3 | 3 | 5 | 9 | 14 |
| 4 | 4 | 14 | 16 | 30 |

Final:

$$\boxed{\texttt{sum}=30}.$$

![FIG-01-27-003: A split instructional figure. Left side shows pseudocode for sum=0 and a for-loop k=1 to 4 adding k². Right side is a trace table with rows for k=1,2,3,4 and accumulator values 1,5,14,30. A callout contrasts assignment "sum = sum + k²" with comparison "sum == 30" and states that assignment changes stored state while comparison returns true or false.](../figures/FIG-01-27-003-pseudocode-trace-table.png)

### Worked Example 3 — Trace Before You Calculate

**Given.**

```text
x = 3
y = 8

x = x + y
y = x - y
x = x - y
```

**Find.** Final `x` and `y`.

**Solution.**

| Step | `x` | `y` |
|---|---:|---:|
| initial | 3 | 8 |
| `x = x + y` | 11 | 8 |
| `y = x - y` | 11 | 3 |
| `x = x - y` | 8 | 3 |

Therefore

$$\boxed{x=8,\qquad y=3}.$$

The procedure swaps the two values without a temporary variable.

**Check.** The set of values remains $\{3,8\}$; only their locations change.

---

## 27.4 Boolean Logic and Branch Design

A **Boolean expression** evaluates to either true or false.

Examples:

```text
T >= 90
d > 0
abs(residual) <= tol
k < maxIter
```

### Compound conditions

`and` requires both conditions to be true.

```text
x >= 0 and x <= 10
```

represents

$$0\le x\le10.$$

`or` requires at least one condition to be true.

```text
pressure < Pmin or pressure > Pmax
```

identifies a value outside the allowed interval.

### Complementary conditions

Negating

```text
x >= 0 and x <= 10
```

gives

```text
x < 0 or x > 10
```

The logical connector changes. This is De Morgan's law in operational form.

### Complete branching

A good branch structure covers every possible input exactly as intended.

Suppose a measurement error magnitude $e$ is classified:

- pass if $e\le0.5$,
- review if $0.5<e\le1.0$,
- fail if $e>1.0$.

A safe structure is:

```text
if e <= 0.5 then
    result = "pass"
else if e <= 1.0 then
    result = "review"
else
    result = "fail"
end if
```

Because branches are tested in order, there is no gap and no overlap.

![FIG-01-27-004: A number line from 0 to above 1.0 is partitioned at 0.5 and 1.0 into PASS, REVIEW, and FAIL regions. Above it, a three-branch pseudocode decision ladder shows if e<=0.5, else if e<=1.0, else. Boundary markers at exactly 0.5 and 1.0 are emphasized. A small inset shows De Morgan equivalence: NOT(x>=0 AND x<=10) becomes x<0 OR x>10.](../figures/FIG-01-27-004-boolean-branches-boundaries.png)

### Worked Example 4 — Build the Condition, Not the Story

**Given.** A pump is allowed to run only when:

- tank level $L$ is at least 20%,
- discharge pressure $P$ is below 900 kPa,
- emergency stop `EStop` is false.

**Find.** The Boolean run condition.

**Solution.**

```text
runAllowed =
    (L >= 20) and
    (P < 900) and
    (EStop == false)
```

Equivalent stop logic is:

```text
stopRequired =
    (L < 20) or
    (P >= 900) or
    (EStop == true)
```

**Check.** Each safe requirement is necessary, so the run condition uses `and`.
Any one unsafe state must stop operation, so the stop condition uses `or`.

---

## 27.5 Iteration — Repetition with a Defined Exit

Loops express repeated work.

### `for` loop — known count

Use a `for` loop when the number of passes is known from the problem.

```text
sum = 0

for k = 1 to n
    sum = sum + x[k]
end for
```

This executes exactly $n$ times.

### `while` loop — condition checked first

Use a `while` loop when continuation depends on a condition.

```text
while abs(residual) > tol
    ...
end while
```

A `while` loop may execute zero times.

### Post-test loop — execute at least once

A post-test structure is appropriate when one calculation must occur before the
stopping condition can be evaluated.

Conceptually:

```text
do
    update estimate
    compute error
while error > tol
```

### Counters and accumulators

A **counter** tracks how many times something happened.

```text
count = count + 1
```

An **accumulator** combines a sequence of values.

```text
sum = sum + value
```

Initialize both deliberately.

### Off-by-one errors

Suppose five points are

$$x_1,x_2,x_3,x_4,x_5.$$

There are five points but only four adjacent intervals.

A loop over intervals should be

```text
for k = 1 to 4
    use x[k] and x[k+1]
end for
```

not `1 to 5`, because `x[6]` would be requested on the last pass.

![FIG-01-27-005: Three side-by-side loop flow diagrams. FOR shows initialize k, body, increment k, and known-count test. WHILE shows condition before body and a possible zero-pass path. DO-WHILE shows body before the condition and guarantees at least one pass. Below, a five-point array x[1] through x[5] is connected by four interval brackets, with a warning that looping k=1 through 5 and accessing x[k+1] requests nonexistent x[6].](../figures/FIG-01-27-005-loop-structures-off-by-one.png)

### Worked Example 5 — Average Only the Valid Measurements

**Given.** Measurements are stored in `x[1]` through `x[n]`. A value is valid
only when $0\le x\le100$.

**Find.** Pseudocode that returns the mean of valid values or reports that no
valid values exist.

**Solution.**

```text
sum = 0
count = 0

for k = 1 to n

    if x[k] >= 0 and x[k] <= 100 then
        sum = sum + x[k]
        count = count + 1
    end if

end for

if count == 0 then
    write("no valid measurements")
else
    average = sum / count
    write(average)
end if
```

The division occurs only after `count == 0` has been excluded.

**Check.** Invalid values affect neither the numerator nor denominator.

> ---
> **Mentor's Margin**
>
> Most loop defects are not advanced mathematics. They are boundary mistakes:
> the wrong first index, the wrong last index, an accumulator initialized in
> the wrong place, or a condition that can never become false.
>
> ---

---

## 27.6 Turning Numerical Methods into Algorithms

Chapter 01-26 supplied numerical formulas. Here we add executable control logic.

### Newton root extraction

The mathematical update is

$$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}.$$

A robust algorithm also needs:

- initial value,
- `tol`,
- `maxIter`,
- derivative guard,
- residual test,
- iteration count,
- failure status.

Pseudocode:

```text
x = x0
status = "not converged"

for k = 1 to maxIter

    fx = f(x)

    if abs(fx) <= tol then
        status = "converged"
        exit for
    end if

    dfx = df(x)

    if abs(dfx) <= derivativeTol then
        status = "derivative too small"
        exit for
    end if

    x = x - fx / dfx

end for

write(x; status; k)
```

### Worked Example 6 — Trace a Guarded Newton Algorithm

Use

$$f(x)=x^2-2,\qquad f'(x)=2x,$$

with

$$x_0=1.5,\qquad \texttt{tol}=10^{-6}.$$

Iterations:

| $k$ | $x_k$ | $f(x_k)$ |
|---:|---:|---:|
| 0 | 1.500000000 | 0.250000000 |
| 1 | 1.416666667 | 0.006944444 |
| 2 | 1.414215686 | 0.000006007 |
| 3 | 1.414213562 | about $4.5\times10^{-12}$ |

The final residual satisfies the tolerance, so the returned status is
`"converged"`.

### Bisection needs a different guard

Bisection begins by validating the bracket.

```text
fa = f(a)
fb = f(b)

if fa == 0 then
    return a
end if

if fb == 0 then
    return b
end if

if fa * fb > 0 then
    write("invalid bracket")
    return
end if
```

Only after that should the loop begin.

### Simpson needs an even-interval guard

```text
if n <= 0 or n mod 2 <> 0 then
    write("Simpson requires positive even n")
    return
end if
```

Then the weights can be assigned by index parity.

### Euler needs step-count consistency

For a requested final time $t_f$,

$$N=\frac{t_f-t_0}{\Delta t}$$

must correspond to the intended number of full steps—or the algorithm must define
what happens to a leftover partial interval.

![FIG-01-27-006: A guarded numerical-algorithm flowchart centered on Newton iteration. START leads to read x0, tol, maxIter; evaluate residual; if residual small go to CONVERGED; otherwise evaluate derivative; if derivative too small go to FAILURE; otherwise perform Newton update and increment iteration. A max-iteration decision either loops back or exits with NOT CONVERGED. Along the bottom are smaller guard boxes for bisection "opposite signs?", Simpson "n positive and even?", and Euler "step count reaches requested final time?".](../figures/FIG-01-27-006-guarded-numerical-algorithm.png)

### Worked Example 7 — Simpson as Pseudocode

For equally spaced data $f[1]$ through $f[n+1]$ with even `n`:

```text
if n <= 0 or n mod 2 <> 0 then
    write("invalid n")
    return
end if

h = (b - a) / n
weightedSum = f[1] + f[n+1]

for i = 2 to n

    if i mod 2 == 0 then
        weightedSum = weightedSum + 4 * f[i]
    else
        weightedSum = weightedSum + 2 * f[i]
    end if

end for

I = h * weightedSum / 3
write(I)
```

Why is the parity pattern attached to the **point index** this way?

With one-based storage:

- `f[1]` is the left endpoint,
- `f[2]` is the first interior point and receives weight 4,
- `f[3]` receives weight 2,
- and so on.

For $n=4$, the five point weights become

$$1,\ 4,\ 2,\ 4,\ 1.$$

The algorithm reproduces the Chapter 01-26 formula.

---

## 27.7 Verification, Testing, and Efficiency

A plausible output is not proof of a correct algorithm.

Testing should be planned.

### Four minimum test classes

**1. Nominal case**

A normal input with a known or independently checkable answer.

**2. Boundary case**

A value exactly at a decision threshold.

Examples:

- `T = 70`
- `T = 90`
- `n = 2` for Simpson
- residual exactly equal to tolerance

**3. Invalid-input case**

Examples:

- negative diameter,
- odd `n` for Simpson,
- `tol <= 0`,
- bisection endpoints with the same sign.

**4. Failure-path case**

Examples:

- Newton derivative nearly zero,
- maximum iteration count reached,
- no valid measurements in a filtered average.

A test suite that checks only normal values does not test the algorithm's logic.

### Invariants

A useful **invariant** is something that should remain true throughout an
iteration.

For bisection:

$$\boxed{f(a_k)f(b_k)\le0}$$

should remain true after every valid update.

For a count of accepted measurements:

$$0\le\texttt{count}\le k$$

after processing $k$ entries.

An invariant is a powerful debugging tool because it detects corruption before
the final answer is reached.

### Efficiency and Big-O

The Handbook's Electrical and Computer Engineering section introduces **Big-O**
as a way to compare how algorithm cost grows with problem size.

Common orders:

| Order | Typical growth | Example idea |
|---|---|---|
| $O(1)$ | constant | one indexed lookup |
| $O(\log n)$ | grows slowly | repeated halving |
| $O(n)$ | proportional to data count | single pass through an array |
| $O(n\log n)$ | between linear and quadratic | efficient comparison sorting |
| $O(n^2)$ | proportional to all pairs / nested passes | simple double loop |

Big-O does **not** give exact runtime. It suppresses constant factors and lower
order terms to describe large-$n$ growth.

![FIG-01-27-007: A two-part verification and efficiency figure. Left: a test matrix with four rows—nominal, boundary, invalid input, failure path—and columns for input, expected path, expected result. Right: order-of-growth curves O(1), O(log n), O(n), O(n log n), O(n²) on common axes, with repeated halving visually associated with logarithmic growth and a single pass associated with linear growth.](../figures/FIG-01-27-007-testing-and-complexity.png)

### Worked Example 8 — Linear Search versus Repeated Halving

Suppose a sorted table contains approximately

$$n=1{,}000{,}000$$

entries.

A worst-case linear scan may inspect about

$$\boxed{1{,}000{,}000}$$

entries.

A binary-search style repeated halving needs about

$$\log_2(1{,}000{,}000)\approx19.93,$$

so roughly

$$\boxed{20}$$

halving decisions.

This does not mean every $O(\log n)$ implementation is always faster for every
small problem. It means the growth rate is dramatically better as $n$ becomes
large.

### Correctness before efficiency

An $O(\log n)$ algorithm that returns the wrong answer is not superior to an
$O(n)$ algorithm that returns the right one.

Use this priority:

1. define the problem,
2. make the algorithm correct,
3. verify edge cases,
4. then improve efficiency if it matters.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. The Mechanical FE exam specification in the
> appendix explicitly lists **Algorithm and logic development (e.g., flowcharts,
> pseudocode)** under Mathematics. The Electrical and Computer Engineering section
> provides software pseudocode syntax guidance on printed page 417 and a flowchart
> symbol definition on printed page 418. The ECE section also introduces Big-O
> algorithm efficiency on page 417.

The Handbook support for this chapter is unusual: the **exam specification**
establishes that algorithm and logic development is an assessed topic for at least
the Mechanical route, while the most explicit pseudocode and flowchart conventions
appear in the Electrical and Computer Engineering discipline section.

| Handbook material | Printed page | Verified coverage and its limit |
|---|---:|---|
| Mechanical FE Exam Specifications / Mathematics | appendix, near p. 495 | Explicitly lists algorithm and logic development with flowcharts and pseudocode as examples |
| Electrical and Computer Engineering / Algorithm Efficiency | 417 | Defines Big-O use for algorithm efficiency and gives example average/worst-case orders |
| Electrical and Computer Engineering / Software Syntax Guidelines | 417–418 | States that code is pseudocode, not a specific language; provides assignment, comparison, logical, array, loop, procedure, and I/O conventions |
| Electrical and Computer Engineering / Flowchart Definition | 418 | Shows symbols for process/operation, start/stop, data I/O, document, database, and decision |

**Important scope note.** The software-syntax table is located in the
Electrical and Computer Engineering section. A problem for another discipline may
use simpler or explicitly supplied conventions. Use the notation stated in the
question when it conflicts with a local convention.

**Methods developed in this guide.** The general algorithm-contract framework,
precondition/postcondition language, trace-table method, branch-boundary testing,
loop-invariant checks, guarded numerical templates, and the four-part minimum test
suite are instructional structures used here to make the Handbook material
operational. They are not claimed as verbatim Handbook procedures.

**Know without a lookup:**

- sequence, selection, and iteration,
- assignment versus comparison,
- how `and` differs from `or`,
- how to trace changing variable state,
- why loops need a termination condition,
- why array limits cause off-by-one errors,
- why a numerical iteration needs both a success test and a failure limit,
- and why test cases must include boundaries and invalid inputs.

---

## Where This Goes Wrong

**Writing mathematics instead of an algorithm.** A formula with no input,
validation, stopping rule, or output path is incomplete as executable logic.

**Using ambiguous verbs.** "Check the pressure" does not say what comparison is
performed or what happens next.

**Confusing `=` with `==`.** In the Handbook pseudocode convention, `=` assigns
and `==` compares.

**Testing thresholds in the wrong order.** If a broad condition is tested before
a narrower severe condition, the severe branch may never be reached.

**Leaving gaps at boundaries.** Conditions such as `x < 10` followed by
`x > 10` never classify `x == 10`.

**Creating overlapping categories accidentally.** Independent `if` statements can
execute more than one branch when `else if` was intended.

**Forgetting to initialize an accumulator.** `sum = sum + value` is undefined if
`sum` has no starting value.

**Resetting an accumulator inside the loop.** If `sum = 0` occurs on every pass,
the algorithm remembers only the latest value.

**Using the wrong loop bound.** `1 to n` points does not imply `1 to n`
adjacent intervals.

**Changing the loop-control variable accidentally.** Modifying `k` inside a
count-controlled loop can skip or repeat data.

**Writing a `while` condition that never changes.** If nothing in the body can
make the condition false, the algorithm does not terminate.

**Using exact floating-point equality for convergence.** Numerical algorithms
normally stop on a tolerance, not `residual == 0`.

**Using tolerance with no iteration cap.** A pathological case can loop forever.

**Using a maximum iteration count with no success test.** Reaching `maxIter` is a
failure status, not evidence of convergence.

**Failing to validate a bracket.** Bisection without opposite signs loses its
usual root guarantee.

**Running Simpson with odd `n`.** The algorithm should reject the input before
computing weights.

**Testing only the nominal case.** Most logic bugs live at boundaries and failure
paths.

**Optimizing before verifying correctness.** Faster wrong answers remain wrong.

---

## Key Terms

| Term | Definition |
|---|---|
| algorithm | finite, unambiguous procedure that transforms inputs into outputs |
| input | information supplied to an algorithm |
| output | information returned by an algorithm |
| precondition | condition that must hold before successful execution is valid |
| postcondition | condition guaranteed after successful completion |
| failure condition | condition that prevents normal successful completion |
| control flow | order in which algorithm steps execute |
| flowchart | graphical representation of control flow |
| process block | flowchart symbol for a calculation or operation |
| decision block | flowchart symbol that selects a path based on a Boolean condition |
| pseudocode | language-neutral notation for algorithm structure |
| assignment | operation that stores a value in a variable |
| comparison | operation that evaluates a relationship as true or false |
| Boolean expression | expression whose value is true or false |
| branch | alternate execution path selected by a condition |
| iteration | repeated execution of a block of steps |
| loop | control structure that performs iteration |
| counter | variable that records a number of events or passes |
| accumulator | variable that combines values across iterations |
| sentinel | distinguished value or condition used to signal termination |
| flag | variable used to record a state or condition |
| off-by-one error | loop or indexing defect caused by one too many or one too few iterations |
| termination condition | condition that stops an iterative procedure |
| maximum iteration count | hard limit that prevents uncontrolled iteration |
| trace table | table of variable states used to follow an algorithm step by step |
| invariant | property intended to remain true through an iterative process |
| test case | selected input with an expected path or result |
| boundary case | test at or immediately around a decision threshold |
| Big-O notation | asymptotic description of how algorithm resource use grows with input size |
| linear-time algorithm | algorithm with order $O(n)$ |
| logarithmic-time algorithm | algorithm with order $O(\log n)$ |

---

## Review Questions

### Conceptual

1. What makes a procedure an algorithm rather than merely a formula?
2. Distinguish a precondition from a postcondition.
3. Why should an algorithm define a failure path?
4. Name the four core flowchart symbols emphasized in this chapter and state their purposes.
5. In Handbook-style pseudocode, what is the difference between `=` and `==`?
6. Explain the difference between `and` and `or` in a compound Boolean expression.
7. Why can an ordered `if / else if / else` ladder be safer than several independent `if` statements for exclusive categories?
8. When is a `for` loop preferable to a `while` loop?
9. Why does a numerical iteration need both a tolerance and a maximum iteration count?
10. What is an invariant, and how can it help detect an algorithm defect?

### Trace and Calculation

11. Trace:
    ```text
    x = 4
    y = 3
    x = x * y
    y = x - y
    ```
    Find final `x` and `y`.

12. Trace:
    ```text
    sum = 0
    for k = 1 to 5
        sum = sum + k
    end for
    ```
    Find final `sum`.

13. Five data points are stored in `x[1]` through `x[5]`. How many adjacent
    intervals exist, and what loop range should be used if each pass accesses
    `x[k]` and `x[k+1]`?

14. Write a Boolean expression that is true only when
    $-2\le x<5$.

15. Write the logical complement of:
    ```text
    pressure >= 200 and pressure <= 500
    ```

16. A loop begins with `count = 0` and increments `count` once for each valid
    measurement. After processing 12 measurements, what bounds must the invariant
    place on `count`?

17. A guarded Newton method uses `tol = 1e-6` and current residual
    $3.2\times10^{-7}$. Should it update again if residual tolerance alone controls
    success?

18. Composite Simpson integration receives `n = 7`. What should a correct
    algorithm do before evaluating the weighted sum?

19. A sorted list contains approximately $2^{15}$ entries. About how many
    repeated-halving decisions are needed in an ideal binary-search style
    procedure?

### Multiple Choice

20. Which flowchart symbol normally represents a decision?
A) rectangle  B) diamond  C) parallelogram  D) rounded terminal.

21. Which statement changes the stored value of `x`?
A) `x == 5`  B) `x >= 5`  C) `x = 5`  D) `x <> 5`.

22. A loop whose body may execute zero times is most naturally:
A) `while`  B) post-test `do ... while`  C) unconditional loop only  D) none.

23. Which is the best guard before calculating `sigma = F/A`?
A) `A == 0 then continue`  
B) `if A <= 0 then report invalid input`  
C) `if F == 0 then stop`  
D) no guard is needed.

24. Which test case is most likely to expose an inequality-boundary defect?
A) a typical middle-range value  
B) a random decimal value  
C) a value exactly equal to the threshold  
D) a very large unrelated value.

25. A single pass through all $n$ array entries is typically:
A) $O(1)$  B) $O(\log n)$  C) $O(n)$  D) $O(n^2)$.

26. Repeatedly halving a search interval is associated with:
A) $O(\log n)$  B) $O(n)$  C) $O(n^2)$  D) $O(2^n)$.

27. Reaching `maxIter` while the residual is still above tolerance should return:
A) converged  
B) exact  
C) a failure or not-converged status  
D) the residual set to zero.

---

## Answer Key with Explanations

### Conceptual

1. An algorithm specifies a finite, unambiguous sequence that transforms defined
   inputs into outputs and makes decisions, repetition, termination, and failure
   behavior explicit. A formula may be one step inside that procedure. (§27.1)

2. A **precondition** must hold before the normal procedure is valid. A
   **postcondition** is guaranteed after successful completion. (§27.1)

3. Real inputs can violate assumptions and iterative methods can fail. Without a
   failure path the procedure may divide by zero, index invalid data, loop forever,
   or report an untrustworthy value as valid. (§27.1)

4. Rounded terminal = start/stop; rectangle = process/calculation; parallelogram =
   input/output; diamond = decision. (§27.2)

5. In the Handbook pseudocode convention, `=` assigns a value to a variable;
   `==` compares two values and returns true or false. (§27.3)

6. `and` is true only when both operands are true. `or` is true when at least one
   operand is true. (§27.4)

7. An ordered ladder takes exactly one path once a condition succeeds. Independent
   `if` statements may allow multiple overlapping categories to execute. (§27.4)

8. Use `for` when the number of repetitions is known from the problem. Use
   `while` when continuation depends on a condition whose satisfaction count is
   not known beforehand. (§27.5)

9. Tolerance defines success; `maxIter` prevents nontermination when success does
   not occur. They solve different problems. (§27.6)

10. An invariant is a property intended to remain true throughout iteration. If it
    becomes false, the algorithm state has violated an assumption before the final
    answer is reached. (§27.7)

### Trace and Calculation

11.

    Initial: `x=4`, `y=3`.

    After `x = x * y`:

    $$x=12,\qquad y=3.$$

    After `y = x - y`:

    $$\boxed{x=12,\qquad y=9}.$$

    (§27.3)

12.

    $$0+1+2+3+4+5=\boxed{15}.$$

    (§27.5)

13. Five points create four adjacent intervals. Use

    ```text
    for k = 1 to 4
    ```

    so the largest second index is `x[5]`. (§27.5)

14.

    ```text
    x >= -2 and x < 5
    ```

    (§27.4)

15. By De Morgan's law:

    ```text
    pressure < 200 or pressure > 500
    ```

    (§27.4)

16. After 12 processed measurements,

    $$\boxed{0\le\texttt{count}\le12}.$$

    (§27.7)

17. Yes. Since

    $$3.2\times10^{-7}<10^{-6},$$

    the residual criterion is satisfied, so the algorithm should return success
    before another Newton update. (§27.6)

18. Reject the input or return an invalid-`n` status because composite Simpson's
    rule requires a positive **even** number of subintervals. (§27.6)

19.

    $$\log_2(2^{15})=15.$$

    Approximately

    $$\boxed{15}$$

    halving decisions. (§27.7)

### Multiple Choice

20. **B — diamond.** (§27.2)

21. **C — `x = 5`.** It assigns the value 5. (§27.3)

22. **A — `while`.** Its condition is checked before the first body execution.
    (§27.5)

23. **B.** A nonpositive area is invalid for this physical cross-section and must
    be rejected before division. (§27.1)

24. **C.** Exact threshold values expose incorrect `<` versus `<=` choices.
    (§27.7)

25. **C — $O(n)$.** One pass scales proportionally with the number of entries.
    (§27.7)

26. **A — $O(\log n)$.** Each decision removes roughly half the remaining search
    space. (§27.7)

27. **C.** The hard iteration limit was reached before the success condition, so
    the status is not converged. (§27.6)

---

## Practice Problems

1. **Guarded geometry algorithm.** Write pseudocode that reads width `b` and
   height `h`, rejects nonpositive dimensions, computes rectangle area and
   perimeter, and reports both.

2. **Boundary classification.** Write pseudocode for:
   - `LOW` if $x<10$,
   - `NORMAL` if $10\le x\le20$,
   - `HIGH` if $x>20$.
   Then state the outputs at $x=9.999$, $10$, $20$, and $20.001$.

3. **Trace table.** Trace:
   ```text
   product = 1
   for k = 1 to 4
       product = product * (k + 1)
   end for
   ```
   Find final `product`.

4. **Filtered average.** Write pseudocode that averages only strictly positive
   values in an array and reports `"no positive data"` when none qualify.

5. **Bisection guard.** Write the initialization and validation logic for a
   bisection algorithm, including exact-root endpoint checks and invalid-bracket
   detection.

6. **Newton guard.** Write pseudocode for Newton root finding with:
   `x0`, `tol`, `derivativeTol`, and `maxIter`.
   Return both the numerical estimate and a status string.

7. **Simpson weights.** For `n=6`, list the seven composite-Simpson weights and
   describe pseudocode logic that generates the interior weights.

8. **Euler loop.** Write pseudocode to solve
   $$y'=-3y,\qquad y(0)=2$$
   from $t=0$ to $t=0.4$ with $\Delta t=0.1$. Trace all four steps.

9. **Testing plan.** Design four test cases—nominal, boundary, invalid input, and
   failure path—for the guarded Newton algorithm.

10. **Efficiency.** For $n=1024$, compare the rough work of:
    - a linear scan,
    - repeated halving.
    State the associated Big-O orders.

---

## Practice Problem Solutions

1. **Guarded geometry algorithm**

   ```text
   read(b; h)

   if b <= 0 or h <= 0 then
       write("invalid dimensions")
       return
   end if

   A = b * h
   P = 2 * (b + h)

   write(A; P)
   ```

   **Check.** The normal path guarantees $A>0$ and $P>0$. (§27.1)

2. **Boundary classification**

   ```text
   if x < 10 then
       status = "LOW"
   else if x <= 20 then
       status = "NORMAL"
   else
       status = "HIGH"
   end if
   ```

   Results:

   - 9.999 → `LOW`
   - 10 → `NORMAL`
   - 20 → `NORMAL`
   - 20.001 → `HIGH`

   The exact boundaries are covered once each. (§27.4)

3. **Trace**

   Initial `product=1`.

   | $k$ | factor $k+1$ | new product |
   |---:|---:|---:|
   | 1 | 2 | 2 |
   | 2 | 3 | 6 |
   | 3 | 4 | 24 |
   | 4 | 5 | 120 |

   $$\boxed{\texttt{product}=120}.$$

   (§27.3, §27.5)

4. **Filtered average**

   ```text
   sum = 0
   count = 0

   for k = 1 to n
       if x[k] > 0 then
           sum = sum + x[k]
           count = count + 1
       end if
   end for

   if count == 0 then
       write("no positive data")
   else
       average = sum / count
       write(average)
   end if
   ```

   **Check.** Division occurs only when at least one positive value was accepted.
   (§27.5)

5. **Bisection guard**

   ```text
   fa = f(a)
   fb = f(b)

   if fa == 0 then
       write(a; "exact endpoint root")
       return
   end if

   if fb == 0 then
       write(b; "exact endpoint root")
       return
   end if

   if fa * fb > 0 then
       write("invalid bracket")
       return
   end if
   ```

   After this block, the standard bisection loop may begin. (§27.6)

6. **Guarded Newton**

   ```text
   x = x0
   status = "not converged"

   for k = 1 to maxIter

       fx = f(x)

       if abs(fx) <= tol then
           status = "converged"
           exit for
       end if

       dfx = df(x)

       if abs(dfx) <= derivativeTol then
           status = "derivative too small"
           exit for
       end if

       x = x - fx / dfx

   end for

   write(x; status)
   ```

   If the loop reaches its end without meeting either exit condition, the status
   remains `"not converged"`. (§27.6)

7. **Simpson weights**

   For $n=6$, seven point weights are

   $$\boxed{1,\ 4,\ 2,\ 4,\ 2,\ 4,\ 1}.$$

   With one-based storage:

   ```text
   for i = 2 to n
       if i mod 2 == 0 then
           weight = 4
       else
           weight = 2
       end if
   end for
   ```

   Endpoints are handled separately with weight 1. (§27.6)

8. **Euler loop**

   Update:

   $$y_{k+1}=y_k+0.1(-3y_k)=0.7y_k.$$

   Starting $y_0=2$:

   $$y_1=1.4,$$

   $$y_2=0.98,$$

   $$y_3=0.686,$$

   $$y_4=\boxed{0.4802}.$$

   Pseudocode:

   ```text
   t = 0
   y = 2

   for k = 1 to 4
       y = y + 0.1 * (-3 * y)
       t = t + 0.1
   end for
   ```

   **Check.** Four steps of 0.1 reach $t=0.4$. (§27.6)

9. **Testing plan**

   One valid set:

   - **Nominal:** a function and start value known to converge normally.
   - **Boundary:** choose an initial residual exactly equal to `tol`.
   - **Invalid input:** `tol <= 0` or `maxIter <= 0`.
   - **Failure path:** choose a case where `abs(df(x)) <= derivativeTol` before
     convergence.

   Each case targets a different control path. (§27.7)

10. **Efficiency**

    Linear scan:

    $$\boxed{\text{about }1024\text{ inspections}},\qquad O(n).$$

    Repeated halving:

    $$\log_2(1024)=10,$$

    so approximately

    $$\boxed{10\text{ decisions}},\qquad O(\log n).$$

    The comparison is about growth with problem size, not exact machine time.
    (§27.7)

---

## Quick Reference

**Algorithm contract**

inputs → preconditions → procedure → outputs → postconditions  
plus explicit failure paths.

**Core flowchart shapes**

- rounded terminal: start / stop
- rectangle: process
- parallelogram: input / output
- diamond: decision

**Handbook-style pseudocode**

```text
x = expression      -- assignment
x == y              -- comparison
x <> y              -- not equal
condition1 and condition2
condition1 or condition2
```

**Branching**

```text
if condition1 then
    ...
else if condition2 then
    ...
else
    ...
end if
```

Order branches from the condition structure you actually intend.

**Known-count loop**

```text
for k = 1 to n
    ...
end for
```

**Condition-controlled loop**

```text
while condition
    ...
end while
```

**Accumulator**

```text
sum = 0
sum = sum + value
```

**Counter**

```text
count = 0
count = count + 1
```

**Numerical-iteration minimum guard set**

- valid inputs,
- success tolerance,
- derivative / denominator / bracket checks as applicable,
- maximum iteration count,
- returned status,
- final residual or other credibility check.

**Testing minimum**

nominal · boundary · invalid input · failure path.

**Common growth orders**

$$O(1),\quad O(\log n),\quad O(n),\quad O(n\log n),\quad O(n^2).$$

Correctness comes before optimization.

---

## What's Next

This chapter closes the computational-method sequence that began with symbolic
mathematics and ended with numerical algorithms. You can now express not only
**what** calculation should be performed, but also **how** a repeatable procedure
should validate inputs, choose branches, iterate, stop, and report failure.

The next major Layer 1 block moves into **probability and statistics**. That
material will add a different kind of reasoning: instead of numerical error caused
by an approximation method, the quantities themselves may be random or uncertain.
The guide already reserves later statistical treatment for measurement uncertainty,
so do not import those assumptions backward into the deterministic algorithms
here.

Carry one discipline with you:

> Before trusting an answer, test the path that produced it.

A calculator result can be checked against an equation. An algorithm must also be
checked against its boundaries, failure modes, and termination logic.

— Your Mentor
