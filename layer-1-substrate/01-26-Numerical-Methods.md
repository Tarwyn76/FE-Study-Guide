---
chapter: "01-26"
title: "Numerical Methods"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-026-01, MATH-1C-026-02, MATH-1C-026-03, MATH-1C-026-04, MATH-1C-026-05, MATH-1C-026-06, MATH-1C-026-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-26: Numerical Methods

> *"An exact answer is not always available, and an approximate answer is not
> automatically a bad one. The engineering question is whether the approximation
> is controlled, checked, and accurate enough for the decision it supports."*

---

## Before You Start

**Prerequisites:** [01-03 Accuracy, Precision, and Significant Figures](01-03-Accuracy-Precision-and-Significant-Figures.md) ·
[01-07 Polynomials and Their Roots](01-07-Polynomials-and-Their-Roots.md) ·
[01-08 Systems of Linear Equations](01-08-Systems-of-Linear-Equations.md) ·
[01-16 Limits and Continuity](01-16-Limits-and-Continuity.md) ·
[01-17 The Derivative](01-17-The-Derivative.md) ·
[01-19 Antiderivatives and the Definite Integral](01-19-Antiderivatives-and-the-Definite-Integral.md) ·
[01-22 Infinite Series and Taylor Expansions](01-22-Infinite-Series-and-Taylor-Expansions.md) ·
[01-23 Partial Derivatives and Vector Calculus](01-23-Partial-Derivatives-and-Vector-Calculus.md) ·
[01-25 Differential Equations](01-25-Differential-Equations.md)

**Skip if:** You pass the Tier 1C test-out quiz and can distinguish truncation
from roundoff error; build first- and second-order finite-difference estimates;
bracket a root and carry out Newton iterations; use Newton's method for a
one-variable minimum; interpolate between tabulated values without confusing
interpolation with extrapolation; apply the composite trapezoidal and Simpson
rules; and march a first-order initial-value problem with Euler's method while
checking step-size sensitivity.

**Time:** About 110–130 min reading and worked examples · 40–50 min review
questions · 70–90 min practice problems.

**Working convention:** Numerical values are carried with guard digits during
the calculation and rounded only for reporting. A computed value is not accepted
because an algorithm stopped; it is accepted only after a residual, bracket,
refinement, conservation, dimensional, or comparison check supports it.

---

## On the Board Today

Apprentice, numerical methods begin where the symbolic tools stop being convenient.

Sometimes the function exists only as measurements. Sometimes the equation has a
root but no useful algebraic solution. Sometimes an integral has no elementary
antiderivative. Sometimes the differential equation is easy to write and difficult
to solve. In each case, the problem becomes a sequence of simpler calculations
that approach the quantity you actually want.

That word **approach** matters. A numerical method produces an approximation.
There are therefore two separate jobs:

1. compute the approximation, and
2. decide whether it is trustworthy.

The second job is what keeps numerical methods from becoming button pushing.

A root finder can converge to the wrong root. A derivative estimate can become
worse when the step is made absurdly small. Simpson's rule can be entered with
the wrong weights. Euler's method can produce an apparently smooth sequence that
is numerically unstable. A residual can be tiny while the actual variable error
is still important in an ill-conditioned problem.

The FE Reference Handbook gives several of the core algorithms directly:
Newton root extraction, Newton minimization, forward rectangular integration,
the trapezoidal rule, Simpson's rule, and Euler's ODE approximation. It does not
supply the judgment that tells you when to trust them. That judgment is the main
purpose of this chapter.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **26.1** Distinguish roundoff, truncation, discretization, and iteration error
* **26.2** Compute absolute error, relative error, residual, and a practical stopping criterion
* **26.3** Approximate first and second derivatives from nearby values using finite differences
* **26.4** Explain why centered differences are generally more accurate than one-sided differences at the same step size
* **26.5** Bracket a continuous-function root and apply the bisection method with a guaranteed interval error bound
* **26.6** Apply Newton's method for root extraction and recognize common failure modes
* **26.7** Apply Newton's method of minimization in one variable and interpret the role of curvature
* **26.8** Perform linear interpolation and distinguish interpolation from extrapolation
* **26.9** Apply forward-rectangle, trapezoidal, and Simpson numerical integration formulas
* **26.10** Enforce the interval-count requirement for composite Simpson's rule
* **26.11** March a first-order initial-value problem with Euler's method and recast a higher-order ODE as a first-order system
* **26.12** Use residual checks, bracketing, step halving, and method comparison to judge numerical convergence

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $x^\*$ | exact or target value | usually unknown in a real numerical problem |
| $x_k$ | numerical estimate at iteration $k$ | $k=0$ is the starting estimate |
| $e_a$ | absolute error | $|x_{\text{approx}}-x^\*|$ when $x^\*$ is known |
| $e_r$ | relative error | $e_a/|x^\*|$ when $x^\*\ne0$ |
| $R_k$ | residual | value of the governing equation evaluated at $x_k$ |
| $h$ | spatial or independent-variable step size | also written $\Delta x$ |
| $\Delta t$ | time step | Euler marching step |
| $f'(x)$ | exact first derivative | when an analytic derivative exists |
| $D_hf$ | finite-difference derivative estimate | notation local to this chapter |
| $[a_k,b_k]$ | bracketing interval | endpoints have opposite function signs |
| $n$ | number of subintervals | Simpson requires even $n$ |
| $I$ | exact integral | numerical rules produce approximations to it |
| $y_k$ | numerical ODE solution at $t_k$ | $t_k=t_0+k\Delta t$ |
| $H$ | Hessian matrix | matrix of second partial derivatives |

**Collision note.** The symbol $h$ is used here for a numerical step size and
elsewhere in the guide for geometric height. Read it from context and units.
Likewise, $R$ may mean residual here and resistance in electrical chapters.

---

## 26.1 Numerical Approximation, Error, and Convergence

An approximation is useful only if you know what kind of error created the gap
between it and the desired value.

### Four error sources

**Roundoff error** comes from finite representation and finite arithmetic.
A calculator cannot store infinitely many digits of $\pi$, $\sqrt2$, or most
decimal fractions.

**Truncation error** comes from replacing an infinite mathematical process with
a finite one. Stopping a Taylor series after four terms is truncation. Replacing
a derivative by a finite difference is truncation.

**Discretization error** is the truncation error associated specifically with
replacing a continuous problem by points or steps. A time-marching solution with
$\Delta t=0.1$ s is a discretized version of a continuous ODE.

**Iteration error** is the remaining error because an iterative algorithm was
stopped before reaching its limiting value.

These sources can interact. Reducing a step size often reduces truncation error
but increases the number of arithmetic operations and may amplify roundoff through
subtraction of nearly equal numbers.

![FIG-01-26-001: Conceptual log-scale error-versus-step-size plot. Truncation error slopes downward as h decreases, roundoff error rises at very small h, and their sum forms a broad U-shaped total-error curve with a marked practical step-size region near the minimum. A side panel distinguishes roundoff, truncation, discretization, and iteration error with one-line definitions.](../figures/FIG-01-26-001-error-versus-step-size.png)

### Error when the exact answer is known

For a benchmark problem,

$$\boxed{e_a=|x_{\text{approx}}-x^\*|}$$

and, when $x^\*\ne0$,

$$\boxed{e_r=\frac{e_a}{|x^\*|}},\qquad
\boxed{e_{\%}=100e_r\%.}$$

But in an actual numerical problem, $x^\*$ is usually unknown. You therefore need
quantities that can be computed without knowing the answer.

### Residual

If the target satisfies

$$f(x^\*)=0,$$

then a numerical estimate $x_k$ has residual

$$\boxed{R_k=f(x_k).}$$

A small residual is evidence that the governing equation is nearly satisfied.

It is **not identical to variable error**. Near a simple root,

$$f(x_k)\approx f'(x^\*)(x_k-x^\*),$$

so

$$x_k-x^\*\approx \frac{R_k}{f'(x^\*)}.$$

If the slope is tiny, a small residual can correspond to a much larger error in
$x$. That is one form of poor conditioning.

### Successive-change criterion

A common practical test is

$$\boxed{|x_{k+1}-x_k|\le \varepsilon_x}$$

or a relative version

$$\boxed{
\frac{|x_{k+1}-x_k|}{\max(1,|x_{k+1}|)}\le\varepsilon_r.
}$$

The $\max(1,|x_{k+1}|)$ form avoids dividing by a value near zero.

Do not rely on only one stopping test. A robust calculation often checks both
successive change **and** residual.

### Step halving

For a grid or step-based method, calculate once with step $h$ and again with
$h/2$. If the two answers move substantially, the coarse result was not converged.

If a method has leading error proportional to $h^p$,

$$E(h)\approx Ch^p,$$

then halving the step should reduce the leading error by approximately

$$\boxed{2^p.}$$

This gives an empirical check even when the exact answer is unavailable.

> ---
> **Mentor's Margin**
>
> "More digits" and "more accurate" are not synonyms. A calculator can display
> twelve digits of a poor approximation. Numerical credibility comes from a
> check: residual, bracket width, repeated calculation at a smaller step, or
> comparison with a method of different order.
>
> ---

---

## 26.2 Finite Differences — Derivatives from Nearby Values

The derivative is a limit. Numerical differentiation stops before the limit and
uses a small but finite spacing.

From Chapter 01-17,

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.$$

Using finite $h$ gives the **forward difference**:

$$\boxed{
f'(x)\approx \frac{f(x+h)-f(x)}{h}.
}$$

Similarly, the **backward difference** is

$$\boxed{
f'(x)\approx \frac{f(x)-f(x-h)}{h}.
}$$

The **centered difference** uses points on both sides:

$$\boxed{
f'(x)\approx \frac{f(x+h)-f(x-h)}{2h}.
}$$

Taylor expansion explains their accuracy. For a smooth function,

$$f(x+h)=f(x)+hf'(x)+\frac{h^2}{2}f''(x)+\frac{h^3}{6}f'''(x)+\cdots$$

and

$$f(x-h)=f(x)-hf'(x)+\frac{h^2}{2}f''(x)-\frac{h^3}{6}f'''(x)+\cdots.$$

Subtracting cancels the even-power terms:

$$f(x+h)-f(x-h)=2hf'(x)+\frac{h^3}{3}f'''(x)+\cdots$$

so the centered formula has leading truncation error proportional to $h^2$,
whereas the forward and backward formulas have leading error proportional to $h$.

That is why centered differences are often much better at the same step size.

### Second derivative

Adding the two Taylor expansions instead gives

$$f(x+h)-2f(x)+f(x-h)=h^2f''(x)+O(h^4),$$

so

$$\boxed{
f''(x)\approx\frac{f(x+h)-2f(x)+f(x-h)}{h^2}.
}$$

![FIG-01-26-002: Smooth curve y=f(x) with the point x marked. Three secant constructions show backward difference through x−h and x, forward difference through x and x+h, and centered difference through x−h and x+h. A tangent at x is drawn for comparison. A lower strip shows the centered second-difference stencil with coefficients 1, −2, 1 over h².](../figures/FIG-01-26-002-finite-difference-stencils.png)

### Worked Example 1 — Forward versus Centered Difference

**Given.** $f(x)=e^x$. Estimate $f'(0)$ using $h=0.10$ with a forward
difference and a centered difference.

**Find.** Both estimates and their errors relative to the exact derivative.

**Approach.** Apply both stencils at the same $h$, then compare with
$f'(0)=e^0=1$.

**Solution.**

Forward:

$$D_h^{(F)}f(0)=\frac{e^{0.1}-1}{0.1}
=\boxed{1.05170918}.$$

Centered:

$$D_h^{(C)}f(0)=\frac{e^{0.1}-e^{-0.1}}{0.2}
=\boxed{1.00166750}.$$

Absolute errors:

$$e_F=0.05170918,$$

$$e_C=0.00166750.$$

The centered error is about 31 times smaller at the same step.

Now halve the step to $h=0.05$:

$$D_{0.05}^{(F)}f(0)=1.02542193,$$

$$D_{0.05}^{(C)}f(0)=1.00041672.$$

The forward error falls by about a factor of 2, consistent with first-order
behavior. The centered error falls by about a factor of 4, consistent with
second-order behavior.

**Check.** Both estimates approach the known exact derivative 1 as the step is
reduced.

### Data at a boundary

Centered differences need a value on each side. At the first measured point in a
table, you may have no value at $x-h$, so a forward difference may be the only
available stencil. At the final point, use a backward difference.

This is not merely a mathematical issue. Sensor data are often finite records with
real endpoints.

---

## 26.3 Root Finding — Bracketing and Newton's Method

A root is a value $x^\*$ satisfying

$$\boxed{f(x^\*)=0.}$$

Chapter 01-07 solved roots algebraically when possible. Numerical root finding
handles equations that resist convenient symbolic solution.

### Bracketing first

If $f$ is continuous and

$$f(a)f(b)<0,$$

the Intermediate Value Theorem guarantees at least one root in $(a,b)$.

That sign change gives you something Newton's method does not: a **guaranteed
bracket**.

### Bisection

For a bracket $[a_k,b_k]$:

1. Compute
   $$c_k=\frac{a_k+b_k}{2}.$$
2. Evaluate $f(c_k)$.
3. Keep the half interval whose endpoints have opposite signs.
4. Repeat.

After $m$ bisections, the interval width is

$$\boxed{
\frac{b_0-a_0}{2^m}.
}$$

If the midpoint is reported, its error is bounded by half that width:

$$\boxed{
|c_m-x^\*|\le \frac{b_0-a_0}{2^{m+1}}.
}$$

Bisection is slow but dependable.

### Newton's method

Newton replaces the curve locally by its tangent. At estimate $x_k$, the tangent
line is

$$y=f(x_k)+f'(x_k)(x-x_k).$$

Set that tangent equal to zero and solve for its x-intercept:

$$0=f(x_k)+f'(x_k)(x_{k+1}-x_k),$$

which gives

$$\boxed{
x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}.
}$$

This is the Newton root-extraction formula printed in the Handbook.

![FIG-01-26-003: Root-finding comparison on one nonlinear curve. Left panel shows a bracket [a,b] with opposite signs and three successive bisection midpoints narrowing onto the root. Right panel shows Newton iterations: from x0 on the curve, a tangent meets the x-axis at x1, then a new tangent at x1 meets at x2 near the root. A footer contrasts "bisection: guaranteed with a valid continuous bracket" and "Newton: usually faster, but start and slope matter".](../figures/FIG-01-26-003-bisection-versus-newton.png)

### Worked Example 2 — Guaranteed Root by Bisection

**Given.**

$$f(x)=x^3-x-2.$$

**Find.** A bracket for the positive root after five bisections starting from
$[1,2]$.

**Approach.** Verify the sign change, then repeatedly retain the half interval
that contains it.

**Solution.**

At the endpoints,

$$f(1)=-2,\qquad f(2)=4,$$

so a root is guaranteed in $[1,2]$.

The midpoint sequence is:

| Step | Midpoint | Sign of $f(c)$ | New bracket |
|---:|---:|---:|---|
| 1 | 1.50000 | − | [1.50000, 2.00000] |
| 2 | 1.75000 | + | [1.50000, 1.75000] |
| 3 | 1.62500 | + | [1.50000, 1.62500] |
| 4 | 1.56250 | + | [1.50000, 1.56250] |
| 5 | 1.53125 | + | [1.50000, 1.53125] |

After five bisections the bracket width is

$$\frac{1}{2^5}=0.03125.$$

If the bracket midpoint is reported,

$$x\approx\frac{1.50000+1.53125}{2}=1.515625,$$

with guaranteed midpoint error no larger than

$$\boxed{0.015625}.$$

**Check.** The retained endpoints still have opposite signs, so the root remains
inside the interval.

### Worked Example 3 — Newton Converges Rapidly

**Given.** Use Newton's method on

$$f(x)=x^3-x-2$$

with $x_0=1.5000$.

**Find.** Three Newton updates.

**Approach.** Use

$$f'(x)=3x^2-1$$

and iterate.

**Solution.**

$$x_{k+1}
=x_k-\frac{x_k^3-x_k-2}{3x_k^2-1}.$$

First update:

$$x_1=1.5000-\frac{-0.1250}{5.7500}
=\boxed{1.52173913}.$$

Second:

$$x_2
=1.52173913-\frac{0.00213693}{5.94707}
=\boxed{1.52137981}.$$

Third:

$$x_3\approx\boxed{1.52137971}.$$

Residual:

$$|f(x_3)|\approx4.5\times10^{-14}.$$

**Check.** The value lies inside the valid bisection bracket and has a tiny
residual.

### When Newton fails

Newton is not a guarantee. Problems include:

**Derivative near zero.**

$$\frac{f(x_k)}{f'(x_k)}$$

can become enormous.

**Poor starting value.** The tangent may jump to a distant root or diverge.

**Oscillation.** Iterates may bounce between values.

**Nonsmooth point.** The derivative may not exist.

**Multiple root.** Standard Newton convergence slows because the derivative also
approaches zero.

A practical hybrid strategy is to bracket first, use Newton for speed, and reject
a Newton step that leaves a trusted bracket.

> ---
> **Mentor's Margin**
>
> Never confuse "the last two iterates agree" with "the equation is solved."
> A spreadsheet formula copied incorrectly can converge beautifully to nonsense.
> Check the residual in the original equation.
>
> ---

---

## 26.4 Newton Minimization and Curvature

Root finding solves

$$f(x)=0.$$

Optimization solves

$$h'(x)=0$$

and then asks whether the stationary point is the desired minimum.

Applying Newton's root method to $h'(x)$ gives

$$\boxed{
x_{k+1}=x_k-\frac{h'(x_k)}{h''(x_k)}.
}$$

The denominator is curvature. Near a well-behaved minimum,

$$h''(x^\*)>0.$$

A tiny or sign-changing second derivative can make the Newton step unreliable.

For several variables, Chapter 01-23 introduced the gradient and Hessian ideas.
The Handbook prints the multivariable Newton minimization structure in matrix form:

$$\boxed{
\mathbf x_{k+1}
=
\mathbf x_k
-
H(\mathbf x_k)^{-1}\nabla h(\mathbf x_k).
}$$

In practice you normally solve

$$H\Delta\mathbf x=-\nabla h$$

for $\Delta\mathbf x$ rather than explicitly forming $H^{-1}$, then use

$$\mathbf x_{k+1}=\mathbf x_k+\Delta\mathbf x.$$

That is numerically preferable and connects directly to the linear-system methods
from Chapter 01-08.

![FIG-01-26-004: Two-panel Newton minimization diagram. Left panel shows a one-dimensional objective h(x) with a local minimum x-star; at x0 the slope h' and curvature h'' determine a Newton step to x1, then x2 near the bottom. Right panel shows a contour map of h(x,y), a gradient arrow at x_k, and a Hessian-adjusted Newton step toward the basin minimum, with the matrix equation H Delta-x = −gradient h printed beside it.](../figures/FIG-01-26-004-newton-minimization.png)

### Worked Example 4 — One-Dimensional Newton Minimization

**Given.**

$$h(x)=x^4-3x^2+2,$$

starting at $x_0=1.5000$.

**Find.** The nearby minimum.

**Approach.** Apply Newton to $h'(x)=0$.

**Solution.**

$$h'(x)=4x^3-6x,$$

$$h''(x)=12x^2-6.$$

The iteration is

$$x_{k+1}
=
x_k-\frac{4x_k^3-6x_k}{12x_k^2-6}.$$

Starting at 1.5000:

$$x_1=1.28571429,$$

$$x_2=1.22882427,$$

$$x_3=1.22476510,$$

$$x_4=1.22474487.$$

The exact stationary value on this side is

$$x=\sqrt{\frac32}=1.22474487\ldots$$

and

$$h''(x)=12\left(\frac32\right)-6=12>0,$$

so it is a local minimum.

**Check.** The stationarity residual $|h'(x_4)|$ is near machine precision, and
the positive second derivative confirms the classification.

### A caution about global claims

Newton minimization finds a nearby stationary point. It does not prove global
optimality.

For this example there are two equal minima at

$$x=\pm\sqrt{\frac32}$$

and a local maximum at $x=0$. Starting on the negative side converges to the
negative minimum.

If the engineering problem has bounds or constraints, inspect them separately.

---

## 26.5 Interpolation and Discrete Data

Engineering data often come as tables:

| $x$ | $y$ |
|---:|---:|
| $x_0$ | $y_0$ |
| $x_1$ | $y_1$ |

If $x$ lies between $x_0$ and $x_1$, the simplest estimate assumes a straight
line between the two data points.

The fraction of the horizontal interval is

$$\lambda=\frac{x-x_0}{x_1-x_0}.$$

Then

$$\boxed{
y(x)\approx y_0+\lambda(y_1-y_0)
}$$

or equivalently

$$\boxed{
y(x)\approx
y_0+
\frac{y_1-y_0}{x_1-x_0}(x-x_0).
}$$

This is **linear interpolation**.

### Interpolation versus extrapolation

**Interpolation:** $x$ lies inside the known data interval.

**Extrapolation:** $x$ lies outside it.

Extrapolation is riskier because the data no longer surround the estimate.
A locally linear trend may bend, saturate, reverse, or hit a physical limit.

![FIG-01-26-005: Data plot with measured points connected locally by a straight interpolation segment between x0 and x1. A target x inside the interval projects to an interpolated y with the fractional distance lambda marked. To the right of x1 the same line is extended as a dashed extrapolation with a warning label "outside measured range — assumption grows stronger".](../figures/FIG-01-26-005-linear-interpolation.png)

### Worked Example 5 — Sensor Calibration

**Given.** A calibration table gives:

| Temperature | Sensor output |
|---:|---:|
| $40.0^\circ\mathrm C$ | 2.18 V |
| $60.0^\circ\mathrm C$ | 2.82 V |

**Find.** The linearly interpolated output at $52.0^\circ\mathrm C$.

**Approach.** Find the fractional distance from 40 to 60 °C and apply the same
fraction to the voltage change.

**Solution.**

$$\lambda=\frac{52-40}{60-40}=\frac{12}{20}=0.60.$$

Voltage change across the interval:

$$2.82-2.18=0.64\ \mathrm V.$$

Therefore

$$V(52)\approx2.18+0.60(0.64)
=\boxed{2.564\ \mathrm V}.$$

**Check.** The answer lies between 2.18 V and 2.82 V and is closer to the upper
value because 52 °C is closer to 60 °C.

### Interpolation is not regression

Interpolation passes through the selected data points. Regression fits a model to
a collection of noisy observations and generally does **not** pass through every
point.

Regression belongs with probability and statistics later in the guide. Do not
use the words interchangeably.

---

## 26.6 Numerical Integration

Chapter 01-19 defined an integral as accumulation. Numerical integration replaces
the continuous area by weighted values of the function.

Let

$$x_k=a+k\Delta x,$$

with

$$\boxed{\Delta x=\frac{b-a}{n}}.$$

### Forward rectangular rule

Use the left endpoint of each interval:

$$\boxed{
\int_a^b f(x)\,dx
\approx
\Delta x\sum_{k=0}^{n-1}f(x_k).
}$$

The Handbook labels this **Euler's or Forward Rectangular Rule**.

### Composite trapezoidal rule

Approximate each interval by a trapezoid:

$$\boxed{
\int_a^b f(x)\,dx
\approx
\frac{\Delta x}{2}
\left[
f(x_0)
+2\sum_{k=1}^{n-1}f(x_k)
+f(x_n)
\right].
}$$

The endpoint weights are 1 and the interior weights are 2.

### Composite Simpson's rule

Simpson fits parabolic pieces. The interval count must be even:

$$\boxed{n=2,4,6,\ldots}$$

and

$$\boxed{
\int_a^b f(x)\,dx
\approx
\frac{\Delta x}{3}
\left[
f(x_0)
+4\sum_{\substack{k=1\\k\text{ odd}}}^{n-1}f(x_k)
+2\sum_{\substack{k=2\\k\text{ even}}}^{n-2}f(x_k)
+f(x_n)
\right].
}$$

The weight pattern is

$$\boxed{1,\ 4,\ 2,\ 4,\ 2,\ldots,\ 4,\ 1.}$$

![FIG-01-26-006: Three aligned panels integrate the same smooth curve over the same equally spaced grid. Left uses forward rectangles, middle uses trapezoids joining adjacent points, and right uses parabolic Simpson segments. Under the panels the composite weight patterns are printed: rectangle all left endpoints, trapezoid 1-2-2-...-2-1, Simpson 1-4-2-4-...-4-1 with "n even" highlighted.](../figures/FIG-01-26-006-numerical-integration-rules.png)

### Worked Example 6 — Three Rules on the Same Integral

**Given.**

$$I=\int_0^2 x^2\,dx,$$

using $n=4$ equal intervals.

**Find.** Forward-rectangle, trapezoidal, and Simpson approximations.

**Approach.** Use the common grid

$$\Delta x=\frac{2-0}{4}=0.5$$

with values:

| $x$ | 0 | 0.5 | 1.0 | 1.5 | 2.0 |
|---:|---:|---:|---:|---:|---:|
| $f=x^2$ | 0 | 0.25 | 1.00 | 2.25 | 4.00 |

**Solution.**

Forward rectangle:

$$I_R
=0.5(0+0.25+1.00+2.25)
=\boxed{1.7500}.$$

Trapezoidal:

$$I_T
=\frac{0.5}{2}
[0+2(0.25+1.00+2.25)+4]
=\boxed{2.7500}.$$

Simpson:

$$I_S
=\frac{0.5}{3}
[0+4(0.25)+2(1.00)+4(2.25)+4]
=\boxed{2.6666667}.$$

Exact:

$$I=\left[\frac{x^3}{3}\right]_0^2
=\frac83
=2.6666667.$$

Simpson is exact here because a quadratic lies within the polynomial class that
the rule integrates exactly.

**Check.** The function is increasing and convex. Left rectangles must
underestimate; the trapezoidal chords lie above a convex curve and overestimate.
The computed values obey both geometric checks.

### Unequally spaced data

The composite formulas above assume a uniform $\Delta x$.

For unequal spacing, apply the trapezoid one interval at a time:

$$\boxed{
I\approx
\sum_{k=0}^{n-1}
\frac{x_{k+1}-x_k}{2}
\left[f(x_k)+f(x_{k+1})\right].
}$$

Do not force unequal data into the uniform-grid formula.

---

## 26.7 Numerical ODEs — Euler Marching and Step-Size Control

For the initial-value problem

$$\frac{dy}{dt}=f(t,y),\qquad y(t_0)=y_0,$$

Euler's method uses the current slope to project one step forward:

$$\boxed{
y_{k+1}=y_k+\Delta t\,f(t_k,y_k).
}$$

This is the formula printed in the Handbook.

It is the tangent-line approximation from Chapter 01-18 applied repeatedly.

![FIG-01-26-007: Slope field for a first-order ODE with an exact solution curve and two Euler approximations from the same initial point. The coarse-step path uses long tangent segments and visibly departs from the curve; the fine-step path uses shorter tangent segments and follows it more closely. An inset shows one update y_(k+1)=y_k+Delta-t f(t_k,y_k).](../figures/FIG-01-26-007-euler-marching-step-size.png)

### Local and accumulated error

One Euler step drops the higher-order Taylor terms:

$$y(t+\Delta t)
=
y(t)+\Delta t\,y'(t)
+\frac{\Delta t^2}{2}y''(\xi).$$

So the **local truncation error per step** is order $(\Delta t)^2$.

Over a fixed interval, the number of steps grows like $1/\Delta t$, so the
accumulated or **global error** is generally order $\Delta t$.

Euler is therefore a **first-order method**.

### Worked Example 7 — Step Size Matters

**Given.**

$$y'=-2y,\qquad y(0)=1.$$

**Find.** Euler estimates at $t=0.6$ using $\Delta t=0.2$ and $\Delta t=0.1$.

**Approach.** Here

$$y_{k+1}=y_k+\Delta t(-2y_k)
=(1-2\Delta t)y_k.$$

**Solution with $\Delta t=0.2$.**

The multiplier is $1-0.4=0.6$.

$$y_1=0.6,$$

$$y_2=0.36,$$

$$y_3=\boxed{0.216}.$$

**Solution with $\Delta t=0.1$.**

The multiplier is $0.8$, and six steps give

$$y_6=(0.8)^6=\boxed{0.262144}.$$

The exact solution from Chapter 01-25 is

$$y=e^{-2t},$$

so

$$y(0.6)=e^{-1.2}\approx\boxed{0.3010}.$$

The smaller step is substantially closer.

**Check.** The exact solution remains positive and decays monotonically.
Both Euler sequences do too for these step sizes.

### Stability is not the same as accuracy

For the test equation

$$y'=\lambda y,$$

Euler gives

$$y_{k+1}=(1+\lambda\Delta t)y_k.$$

If the true solution decays, $\lambda<0$. Euler will decay only if

$$\boxed{|1+\lambda\Delta t|<1.}$$

For the previous equation, $\lambda=-2$, so stability requires

$$|1-2\Delta t|<1
\quad\Longrightarrow\quad
0<\Delta t<1.$$

A step of $\Delta t=1.2$ would give multiplier $-1.4$: the numerical solution
would alternate sign and grow even though the exact solution decays smoothly.

That is a numerical instability, not a physical prediction.

### Higher-order ODEs as first-order systems

The Handbook states that an $n$th-order ODE can be recast as $n$ first-order
equations.

For

$$x''+4x=0,$$

define

$$v=x'.$$

Then

$$\boxed{
x'=v,\qquad v'=-4x.
}$$

Euler updates both states using values from the current step:

$$x_{k+1}=x_k+\Delta t\,v_k,$$

$$v_{k+1}=v_k-4\Delta t\,x_k.$$

### Worked Example 8 — Recasting a Second-Order ODE

**Given.**

$$x''+4x=0,\qquad x(0)=1,\qquad x'(0)=0,$$

with $\Delta t=0.10$.

**Find.** The first two Euler steps.

**Approach.** Set $v=x'$ and march the coupled first-order system.

**Solution.**

Initial state:

$$x_0=1,\qquad v_0=0.$$

Step 1:

$$x_1=x_0+0.1v_0=1.000,$$

$$v_1=v_0-0.4x_0=-0.400.$$

Step 2 uses the step-1 state:

$$x_2=x_1+0.1v_1
=1.000-0.040
=\boxed{0.960},$$

$$v_2=v_1-0.4x_1
=-0.400-0.400
=\boxed{-0.800}.$$

The exact solution is

$$x(t)=\cos(2t),\qquad v(t)=-2\sin(2t).$$

At $t=0.2$,

$$x_{\text{exact}}=\cos0.4\approx0.9211,$$

$$v_{\text{exact}}=-2\sin0.4\approx-0.7788.$$

**Check.** The Euler state has the correct direction of motion but visible
first-order error, as expected for only two relatively coarse steps.

### A practical numerical workflow

For most FE-scale numerical calculations:

1. **State the equation and units.**
2. **Choose the method because its assumptions fit the problem.**
3. **Compute with guard digits.**
4. **Apply a stopping or step-size criterion.**
5. **Check the original equation or data structure.**
6. **Repeat with a smaller step or alternate method when practical.**
7. **Round only the reported result.**

That workflow matters more than memorizing a long catalog of algorithms.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed page 53 contains Taylor's series.
> Printed page 62 is titled *Numerical Methods* and contains difference equations,
> Newton root extraction, and Newton minimization. Printed page 63 contains
> numerical integration and Euler's approximation for ordinary differential
> equations. In the supplied 506-page PDF these correspond to PDF pages 59, 68,
> and 69 respectively.

Use the lookup method from
[00-03 Navigating the FE Reference Handbook](../layer-0-orientation/00-03-navigating-the-fe-reference-book.md):
search the method name, identify the variables and assumptions, then map the
Handbook notation to the problem.

| Handbook heading | Printed page | Verified coverage and its limit |
|---|---:|---|
| Mathematics / Taylor's Series | 53 | Gives the Taylor-series expansion. This supports the truncation arguments used to derive finite-difference accuracy, but the finite-difference formulas in §26.2 were not located there. |
| Mathematics / Numerical Methods / Difference Equations | 62 | Gives a discrete first-order difference relation at equally spaced intervals. It is related to numerical stepping, but it is not a general table of finite-difference derivative stencils. |
| Mathematics / Newton's Method for Root Extraction | 62 | Gives $a^{j+1}=a^j-f(a^j)/f'(a^j)$ and states that the initial estimate must be near enough to cause convergence. |
| Mathematics / Newton's Method of Minimization | 62 | Gives the multivariable Newton update using the gradient and second-derivative matrix. |
| Mathematics / Numerical Integration | 63 | Gives forward rectangular, trapezoidal, and Simpson/parabolic rules, including the requirement that Simpson's $n$ be even. |
| Mathematics / Numerical Solution of Ordinary Differential Equations | 63 | Gives Euler's approximation and states that higher-order ODEs can be recast as systems of first-order equations. |

**Methods developed in this guide.** The explicit forward/backward/centered
finite-difference formulas, bisection procedure and error bound, linear
interpolation formula, residual-plus-step stopping strategy, step-halving check,
Euler stability criterion, and the distinction between interpolation and
regression were not located as general formulas in the supplied numerical-method
pages. They are included because they make the printed algorithms usable and
checkable.

**Notation translation.** The Handbook uses $a^j$ for the $j$th Newton root
estimate. This chapter uses $x_k$. They represent the same iterative role. For
Euler's ODE formula the Handbook writes the state as $x(t)$; this chapter often
uses $y(t)$ to avoid collision with an independent spatial coordinate.

**Know without a lookup:** what an iteration is trying to converge to; why a
residual is not automatically the same as variable error; why a derivative step
can be too small; why Newton can fail; why Simpson requires even $n$; why
interpolation is safer than extrapolation; and why a numerical ODE solution must
be checked for step-size sensitivity and stability.

---

## Where This Goes Wrong

**Treating displayed digits as accuracy.** Ten calculator digits do not establish
ten correct digits.

**Rounding every iteration.** Early rounding contaminates later steps. Carry guard
digits and round only the reported result.

**Using relative error at a zero reference.** Relative error is undefined when
the exact reference is zero. Use absolute error or a problem-specific scale.

**Accepting a small residual without considering slope.** If $f'$ is very small,
a modest variable error can create a tiny residual.

**Making $h$ blindly smaller.** Truncation generally improves, but subtraction of
nearly equal floating-point values can amplify roundoff.

**Using a centered difference at an unavailable point.** A boundary may require
a one-sided stencil.

**Claiming a root from a sign change without continuity.** The Intermediate Value
Theorem requires continuity on the interval.

**Using bisection without opposite signs.** No sign-changing bracket means the
standard guarantee is absent. Even-multiplicity roots may touch zero without
changing sign.

**Dividing by a near-zero Newton derivative.** The update can jump violently.

**Assuming Newton finds the nearest root.** It follows tangent geometry, not a
distance rule.

**Calling a Newton stationary point a minimum automatically.** Check curvature,
bounds, constraints, and competing candidates.

**Interpolating after swapping the fraction.** The fraction must measure how far
the target lies from the lower tabulated point across the full interval.

**Calling extrapolation interpolation.** Outside the data range, the estimate
depends on an unverified continuation of the trend.

**Using uniform-grid composite formulas on unequal spacing.** Either re-grid the
data or integrate interval by interval with the actual widths.

**Forgetting Simpson's even-$n$ requirement.** The 1-4-2-...-4-1 pattern closes
only with an even number of subintervals.

**Confusing number of points with number of intervals.** Five equally spaced
points define four subintervals.

**Updating a coupled Euler system in the wrong order.** All right-hand-side
values for step $k\to k+1$ must come from the same old state unless the method
explicitly says otherwise.

**Assuming a smaller Euler step guarantees stability for every problem.**
Stability depends on the equation and the method. Step reduction helps, but the
admissible region is problem dependent.

---

## Key Terms

| Term | Definition |
|---|---|
| numerical method | finite computational procedure used to approximate a mathematical result |
| approximation | value intended to be close to a target value |
| roundoff error | error from finite numerical representation or arithmetic |
| truncation error | error from terminating an infinite or limiting mathematical process |
| discretization error | truncation error introduced by replacing a continuous problem with discrete points or steps |
| iteration error | remaining error because an iterative sequence is stopped before its limit |
| absolute error | magnitude of approximation minus exact value |
| relative error | absolute error divided by the magnitude of a nonzero exact reference |
| residual | value left when an approximate solution is substituted into the governing equation |
| convergence | tendency of approximations to approach a limiting value as iteration proceeds or discretization is refined |
| stopping criterion | numerical condition used to decide when an iterative computation should stop |
| step halving | repeating a calculation with half the original step to assess sensitivity to discretization |
| finite difference | derivative approximation built from function values at separated points |
| forward difference | one-sided difference using the present and next point |
| backward difference | one-sided difference using the previous and present point |
| centered difference | symmetric difference using points on both sides |
| bracket | interval whose endpoint signs guarantee a continuous-function root inside |
| bisection | root method that repeatedly halves a valid sign-changing bracket |
| Newton's method | tangent-based iteration $x_{k+1}=x_k-f/f'$ for root extraction |
| Newton minimization | Newton iteration applied to stationarity using first and second derivatives |
| interpolation | estimating within the range of known data |
| extrapolation | estimating outside the range of known data |
| forward rectangular rule | numerical integral using the left endpoint of each subinterval |
| trapezoidal rule | numerical integral using straight-line chords between data points |
| Simpson's rule | numerical integral using parabolic weighting over an even number of subintervals |
| Euler's method | first-order ODE marching rule $y_{k+1}=y_k+\Delta t\,f(t_k,y_k)$ |
| local truncation error | error introduced in one numerical step assuming the starting value for that step is exact |
| global error | accumulated difference between the numerical and exact solution after many steps |
| numerical stability | property that numerical errors or perturbations do not grow incompatibly with the modeled solution |

---

## Review Questions

Answer the conceptual questions first. For calculations, show the numerical
sequence or weights rather than reporting only the calculator result.

### Conceptual

1. Distinguish roundoff error from truncation error and give one example of each.
2. Why can decreasing a finite-difference step eventually make a derivative estimate worse?
3. Explain the difference between error and residual. Why is a small residual not always sufficient?
4. What does step halving tell you when the exact answer is unknown?
5. Why does a sign-changing bracket require continuity before it guarantees a root?
6. Compare bisection and Newton's method in terms of guarantee and speed.
7. Why can Newton's method fail when $f'(x_k)$ is near zero?
8. Explain why Newton minimization finds stationary points rather than automatically finding a global minimum.
9. Distinguish interpolation, extrapolation, and regression.
10. Why must composite Simpson's rule use an even number of subintervals?

### Calculation

11. An exact benchmark value is 8.000 and a numerical result is 7.964. Find the absolute and percentage relative error.
12. For $f(x)=\ln x$, estimate $f'(2)$ using a centered difference with $h=0.10$. Compare with the exact value.
13. Use the centered second-difference formula with $h=1$ and the values $f(1)=1$, $f(2)=4$, $f(3)=9$ to estimate $f''(2)$.
14. For $f(x)=x^3-x-2$, show that $[1,2]$ brackets a root and state the maximum midpoint error after 8 bisections.
15. Starting at $x_0=0.7000$, perform two Newton iterations for $f(x)=\cos x-x$.
16. Apply one Newton-minimization step to $h(x)=x^4-3x^2+2$ from $x_0=1.5$.
17. Linearly interpolate between $(20,1.40)$ and $(50,2.15)$ to estimate $y$ at $x=38$.
18. Use the composite trapezoidal rule with $h=1$ on the data $f(0)=1$, $f(1)=2$, $f(2)=5$, $f(3)=10$.
19. Apply two Euler steps with $\Delta t=0.25$ to $y'=t-y$, $y(0)=1$.

### Multiple Choice

20. A centered first-difference formula normally has leading truncation error proportional to:
A) $h^0$  B) $h$  C) $h^2$  D) $h^4$.

21. Bisection requires, for its usual root guarantee:
A) a derivative at both endpoints  
B) a continuous function and opposite endpoint signs  
C) two initial guesses with the same sign  
D) a quadratic function.

22. Newton's root update is:
A) $x_{k+1}=x_k+f'(x_k)$  
B) $x_{k+1}=f(x_k)/f'(x_k)$  
C) $x_{k+1}=x_k-f(x_k)/f'(x_k)$  
D) $x_{k+1}=x_k-f'(x_k)/f(x_k)$.

23. With five equally spaced data points, the number of subintervals is:
A) 3  B) 4  C) 5  D) 6.

24. Which weight pattern corresponds to composite Simpson's rule?
A) 1,1,1,1,1  
B) 1,2,2,2,1  
C) 1,4,2,4,1  
D) 1,3,3,1.

25. Estimating a table value beyond the largest measured input is:
A) interpolation  B) extrapolation  C) differentiation  D) bisection.

26. Euler's method for $y'=f(t,y)$ is:
A) $y_{k+1}=y_k+\Delta t\,f(t_k,y_k)$  
B) $y_{k+1}=f(t_{k+1},y_k)$  
C) $y_{k+1}=y_k/\Delta t$  
D) $y_{k+1}=y_k-\Delta t/f(t_k,y_k)$.

27. For the decaying test equation $y'=\lambda y$ with $\lambda<0$, explicit Euler is stable only when:
A) $|1+\lambda\Delta t|<1$  
B) $\lambda\Delta t>1$  
C) $\Delta t=1$ always  
D) $f'(y)=0$.

---

## Answer Key with Explanations

### Conceptual

1. **Roundoff** comes from finite representation or arithmetic, such as storing
   $\pi$ to a finite number of digits. **Truncation** comes from replacing an
   infinite or limiting process with a finite one, such as using two Taylor terms
   or a finite-difference step. (§26.1)

2. Truncation error generally falls as $h$ shrinks, but floating-point subtraction
   of nearly equal values magnifies roundoff relative to the small numerator.
   Eventually the roundoff contribution can dominate. (§26.1, §26.2)

3. Error measures distance from the unknown exact solution. A residual measures
   how closely the approximate value satisfies the equation. Near a shallow root,
   $x_k-x^\*\approx R_k/f'(x^\*)$, so a small residual can coexist with a larger
   variable error when the derivative is small. (§26.1)

4. It reveals sensitivity to discretization. If halving the step changes the result
   materially, the coarse calculation is not converged. If a method has error
   $Ch^p$, the change also gives evidence of the order $p$. (§26.1)

5. Opposite signs alone do not prevent a discontinuous jump over zero. Continuity
   is the hypothesis that forces the function to pass through every intermediate
   value. (§26.3)

6. Bisection is slower but retains a guaranteed root bracket for a continuous
   sign-changing interval. Newton is usually much faster near a simple root but
   depends on the starting value and derivative behavior. (§26.3)

7. The Newton correction divides by $f'(x_k)$. A near-zero derivative creates a
   huge step that can leave the useful region or jump to another root. (§26.3)

8. The Newton-minimization equation drives $h'$ toward zero. A zero derivative can
   be a minimum, maximum, or other stationary behavior, and local convergence says
   nothing by itself about distant competing minima or boundaries. (§26.4)

9. Interpolation estimates **inside** the known input range. Extrapolation extends
   a trend **outside** that range. Regression fits a model to noisy data and
   generally does not pass through every data point. (§26.5)

10. Simpson combines adjacent subintervals into parabolic panels, so they must come
    in pairs. The composite 1-4-2-...-4-1 weighting therefore requires even $n$.
    (§26.6)

### Calculation

11. Absolute error:

    $$e_a=|7.964-8.000|=\boxed{0.036}.$$

    Relative percentage error:

    $$100\frac{0.036}{8.000}
    =\boxed{0.450\%}.$$

    (§26.1)

12. Centered difference:

    $$f'(2)\approx
    \frac{\ln(2.1)-\ln(1.9)}{0.2}
    =\boxed{0.5004173}.$$

    Exact:

    $$f'(2)=\frac12=0.5000000.$$

    Absolute error is about $4.17\times10^{-4}$. (§26.2)

13.

    $$f''(2)\approx
    \frac{f(3)-2f(2)+f(1)}{1^2}
    =9-8+1
    =\boxed{2}.$$

    For $f=x^2$ this is exact. (§26.2)

14.

    $$f(1)=-2,\qquad f(2)=4,$$

    so continuity of the polynomial and the sign change guarantee a root.
    After 8 bisections, the bracket width is

    $$\frac{1}{2^8}=\frac1{256}.$$

    A reported midpoint has error at most

    $$\boxed{\frac1{512}=0.001953125}.$$

    (§26.3)

15. For $f(x)=\cos x-x$,

    $$f'(x)=-\sin x-1.$$

    Starting at $x_0=0.7000$:

    $$x_1
    =0.7000-\frac{\cos0.7-0.7}{-\sin0.7-1}
    =\boxed{0.73943650},$$

    $$x_2
    =x_1-\frac{\cos x_1-x_1}{-\sin x_1-1}
    =\boxed{0.73908516}.$$

    The root is already stable to about six decimal places. (§26.3)

16.

    $$h'(1.5)=4(1.5)^3-6(1.5)=4.5,$$

    $$h''(1.5)=12(1.5)^2-6=21.$$

    Therefore

    $$x_1=1.5-\frac{4.5}{21}
    =\boxed{1.28571429}.$$

    (§26.4)

17.

    $$\lambda=\frac{38-20}{50-20}=\frac{18}{30}=0.6,$$

    $$y=1.40+0.6(2.15-1.40)
    =1.40+0.45
    =\boxed{1.85}.$$

    (§26.5)

18. Four data points from $x=0$ to 3 define three intervals:

    $$I_T
    =\frac{1}{2}
    [1+2(2+5)+10]
    =\frac12(25)
    =\boxed{12.5}.$$

    (§26.6)

19. Euler:

    $$y_{k+1}=y_k+0.25(t_k-y_k).$$

    At $t_0=0$, $y_0=1$:

    $$y_1=1+0.25(0-1)=0.75.$$

    At $t_1=0.25$:

    $$y_2=0.75+0.25(0.25-0.75)
    =\boxed{0.625}.$$

    (§26.7)

### Multiple Choice

20. **C.** Centered first difference is second order: its leading truncation
    error is proportional to $h^2$. (§26.2)

21. **B.** Continuity plus opposite endpoint signs supplies the standard
    Intermediate Value Theorem guarantee. (§26.3)

22. **C.** Newton follows the x-intercept of the tangent:
    $x_{k+1}=x_k-f/f'$. (§26.3)

23. **B.** Intervals are the gaps between points: five points create four gaps.
    (§26.6)

24. **C.** Simpson's composite weights alternate 4 and 2 between endpoint
    weights of 1. (§26.6)

25. **B.** Outside the measured range is extrapolation. (§26.5)

26. **A.** Euler advances the current value by step size times the current
    derivative. (§26.7)

27. **A.** The numerical amplification factor is $1+\lambda\Delta t$; decay
    requires its magnitude to remain below 1. (§26.7)

---

## Practice Problems

1. **Error measures.** A high-accuracy benchmark is 12.5000 and a numerical
   routine returns 12.4700. Compute absolute and percentage relative error.

2. **Finite difference.** Estimate $d(\ln x)/dx$ at $x=2$ with centered
   differences using $h=0.20$ and $h=0.10$. Compare both with the exact derivative
   and comment on the error reduction.

3. **Newton root.** Solve $\cos x-x=0$ beginning with $x_0=0.7000$. Continue until
   two successive values differ by less than $10^{-6}$ and check the final
   residual.

4. **Bisection.** For $f(x)=x^3-4x-1$, first find a unit-width integer interval
   containing a positive sign-changing root above $x=2$. Perform four bisections
   and report the retained bracket.

5. **Newton minimization.** Minimize
   $$h(x)=x^2+\frac4x,\qquad x>0,$$
   starting from $x_0=1.500$. Perform three Newton-minimization iterations and
   compare with the stationary condition solved analytically.

6. **Interpolation.** A property table lists $P=18.4$ at $T=300$ K and
   $P=22.9$ at $T=360$ K. Estimate $P$ at 342 K by linear interpolation.
   State whether using the same line at 400 K would be interpolation or
   extrapolation.

7. **Unequal-spacing integration.** Measurements are
   $(x,f)=(0,2.0),(1,2.8),(2.5,4.0),(4.0,5.2)$.
   Estimate the integral using interval-by-interval trapezoids.

8. **Composite Simpson.** Approximate
   $$\int_0^\pi\sin x\,dx$$
   using Simpson's rule with $n=4$. Compare with the exact value.

9. **Euler first order.** For
   $$y'=t-y,\qquad y(0)=1,$$
   use $\Delta t=0.25$ to estimate $y(0.5)$. Compare with the exact solution
   $y=t-1+2e^{-t}$.

10. **Euler system.** Recast
    $$x''+4x=0,\qquad x(0)=1,\qquad x'(0)=0$$
    as two first-order equations. With $\Delta t=0.10$, compute the state through
    $t=0.20$ and compare with $x=\cos2t$, $v=-2\sin2t$.

---

## Practice Problem Solutions

1. **Approach.** Use the benchmark as the exact reference.

   $$e_a=|12.4700-12.5000|=\boxed{0.0300}.$$

   $$e_\%=100\frac{0.0300}{12.5000}
   =\boxed{0.240\%}.$$

   **Check.** A difference of three hundredths on a value near 12.5 should be a
   few tenths of one percent. (§26.1)

2. **Approach.** Use

   $$D_hf(2)=\frac{\ln(2+h)-\ln(2-h)}{2h}.$$

   For $h=0.20$:

   $$D_{0.20}f(2)
   =\frac{\ln2.2-\ln1.8}{0.4}
   \approx0.5016767.$$

   Error from the exact $0.5$ is about

   $$1.6767\times10^{-3}.$$

   For $h=0.10$:

   $$D_{0.10}f(2)
   =\frac{\ln2.1-\ln1.9}{0.2}
   \approx\boxed{0.5004173}.$$

   Error is about

   $$4.1729\times10^{-4}.$$

   The error ratio is close to 4, consistent with a second-order centered
   difference when the step is halved. (§26.2)

3. **Approach.** Use

   $$x_{k+1}=x_k-\frac{\cos x_k-x_k}{-\sin x_k-1}.$$

   Starting with $x_0=0.7000$:

   $$x_1=0.7394364978,$$

   $$x_2=0.7390851605,$$

   $$x_3=0.7390851332.$$

   Since

   $$|x_3-x_2|\approx2.73\times10^{-8}<10^{-6},$$

   stop:

   $$\boxed{x\approx0.73908513}.$$

   **Check.**

   $$|\cos x-x|\approx2.2\times10^{-16}.$$

   (§26.3)

4. **Approach.** Evaluate integer endpoints.

   $$f(2)=8-8-1=-1,$$

   $$f(3)=27-12-1=14.$$

   So $[2,3]$ is a valid bracket.

   Bisections:

   - $c_1=2.5$, $f(c_1)=15.625-10-1=4.625>0$ → $[2,2.5]$
   - $c_2=2.25$, $f(c_2)=11.390625-9-1=1.390625>0$ → $[2,2.25]$
   - $c_3=2.125$, $f(c_3)=9.595703-8.5-1=0.095703>0$ → $[2,2.125]$
   - $c_4=2.0625$, $f(c_4)=8.773682-8.25-1=-0.476318<0$

   Therefore

   $$\boxed{[2.0625,\ 2.125]}.$$

   **Check.** The endpoint signs remain opposite. (§26.3)

5. **Approach.**

   $$h'(x)=2x-\frac4{x^2},$$

   $$h''(x)=2+\frac8{x^3}.$$

   Newton:

   $$x_{k+1}
   =x_k-\frac{2x_k-4/x_k^2}{2+8/x_k^3}.$$

   Starting $x_0=1.500$ gives approximately

   $$x_1=1.22033898,$$

   $$x_2=1.25865192,$$

   $$x_3=1.25991977.$$

   Analytically,

   $$2x-\frac4{x^2}=0
   \Longrightarrow 2x^3=4
   \Longrightarrow
   x=\sqrt[3]{2}
   =1.25992105\ldots$$

   Therefore

   $$\boxed{x_{\min}\approx1.25992}.$$

   Since $h''(x)>0$ for $x>0$, this stationary point is the positive-domain
   minimum. (§26.4)

6. **Approach.**

   $$\lambda=\frac{342-300}{360-300}=\frac{42}{60}=0.70.$$

   $$P(342)\approx18.4+0.70(22.9-18.4)
   =18.4+3.15
   =\boxed{21.55}.$$

   Using the same line at 400 K would be **extrapolation**, because 400 K lies
   outside the 300–360 K data range. (§26.5)

7. **Approach.** Use one trapezoid per unequal interval.

   From 0 to 1:

   $$I_1=\frac{1}{2}(2.0+2.8)=2.4.$$

   From 1 to 2.5:

   $$I_2=\frac{1.5}{2}(2.8+4.0)=5.1.$$

   From 2.5 to 4.0:

   $$I_3=\frac{1.5}{2}(4.0+5.2)=6.9.$$

   Total:

   $$\boxed{I\approx14.4}.$$

   Units are function-units times x-units. (§26.6)

8. **Approach.** With $n=4$,

   $$h=\frac{\pi}{4}.$$

   Values:

   $$f_0=0,\quad
   f_1=\frac{\sqrt2}{2},\quad
   f_2=1,\quad
   f_3=\frac{\sqrt2}{2},\quad
   f_4=0.$$

   Simpson:

   $$I_S
   =\frac{\pi/4}{3}
   \left[
   0+4\frac{\sqrt2}{2}
   +2(1)
   +4\frac{\sqrt2}{2}
   +0
   \right]$$

   $$=\boxed{2.00456}.$$

   Exact:

   $$\int_0^\pi\sin x\,dx=2.$$

   Percentage error is about $0.228\%$. (§26.6)

9. **Approach.** Euler with $\Delta t=0.25$:

   $$y_{k+1}=y_k+0.25(t_k-y_k).$$

   Step to 0.25:

   $$y_1=1+0.25(0-1)=0.75.$$

   Step to 0.50:

   $$y_2=0.75+0.25(0.25-0.75)
   =\boxed{0.625}.$$

   Exact:

   $$y(0.5)
   =0.5-1+2e^{-0.5}
   \approx\boxed{0.713061}.$$

   Euler error:

   $$0.625-0.713061=-0.088061.$$

   The coarse Euler method undershoots here. (§26.7)

10. **Approach.** Define $v=x'$:

    $$x'=v,\qquad v'=-4x.$$

    Euler:

    $$x_{k+1}=x_k+0.1v_k,$$

    $$v_{k+1}=v_k-0.4x_k.$$

    Initial:

    $$x_0=1,\qquad v_0=0.$$

    At $t=0.1$:

    $$x_1=1,\qquad v_1=-0.4.$$

    At $t=0.2$:

    $$x_2=1+0.1(-0.4)=\boxed{0.960},$$

    $$v_2=-0.4-0.4(1)=\boxed{-0.800}.$$

    Exact at $t=0.2$:

    $$x=\cos0.4\approx0.921061,$$

    $$v=-2\sin0.4\approx-0.778837.$$

    The errors are visible but consistent with a first-order method at this step.
    (§26.7)

---

## Quick Reference

**Error measures**

$$e_a=|x_{\text{approx}}-x^\*|,$$

$$e_r=\frac{e_a}{|x^\*|}\quad(x^\*\ne0).$$

Residual for a root:

$$R_k=f(x_k).$$

Use residual **and** successive-change or refinement checks when possible.

**Finite differences**

Forward:

$$f'(x)\approx\frac{f(x+h)-f(x)}{h}
\qquad O(h).$$

Backward:

$$f'(x)\approx\frac{f(x)-f(x-h)}{h}
\qquad O(h).$$

Centered:

$$f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
\qquad O(h^2).$$

Second derivative:

$$f''(x)\approx
\frac{f(x+h)-2f(x)+f(x-h)}{h^2}
\qquad O(h^2).$$

**Bisection**

Valid bracket:

$$f(a)f(b)<0$$

with continuity.

After $m$ bisections:

$$\text{width}=\frac{b_0-a_0}{2^m},$$

$$\text{midpoint error}\le
\frac{b_0-a_0}{2^{m+1}}.$$

**Newton root**

$$\boxed{
x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}.
}$$

Check the residual and guard against $f'(x_k)\approx0$.

**Newton minimization**

One variable:

$$\boxed{
x_{k+1}=x_k-\frac{h'(x_k)}{h''(x_k)}.
}$$

Several variables:

$$H\Delta\mathbf x=-\nabla h,\qquad
\mathbf x_{k+1}=\mathbf x_k+\Delta\mathbf x.$$

**Linear interpolation**

$$\boxed{
y=y_0+\frac{x-x_0}{x_1-x_0}(y_1-y_0).
}$$

Inside range = interpolation. Outside range = extrapolation.

**Uniform-grid numerical integration**

$$\Delta x=\frac{b-a}{n}.$$

Forward rectangle:

$$I\approx\Delta x\sum_{k=0}^{n-1}f(x_k).$$

Trapezoid:

$$I\approx
\frac{\Delta x}{2}
[f_0+2f_1+\cdots+2f_{n-1}+f_n].$$

Simpson, **even $n$**:

$$I\approx
\frac{\Delta x}{3}
[f_0+4f_1+2f_2+\cdots+4f_{n-1}+f_n].$$

**Euler ODE**

$$\boxed{
y_{k+1}=y_k+\Delta t\,f(t_k,y_k).
}$$

For $y'=\lambda y$, amplification factor:

$$1+\lambda\Delta t.$$

Decay stability requires

$$|1+\lambda\Delta t|<1.$$

**Numerical check stack**

residual · bracket width · step halving · alternate method · units · physical
bounds · limiting behavior.

---

## What's Next

Numerical methods complete the part of the mathematics sequence that turns a
continuous engineering model into a repeatable computation. You can now take a
formula, table, nonlinear equation, integral, or differential equation and turn it
into an algorithm with a defensible stopping or refinement rule.

The next computational topic is **algorithm and logic development**: expressing
a calculation as a sequence of decisions and repetitions that another person—or
a computer—can execute without guessing. Flowcharts and pseudocode will make the
logic explicit. The numerical methods from this chapter will provide the worked
content: loops for Newton iterations, branch decisions for bisection, even-$n$
checks for Simpson's rule, and termination tests based on residual and tolerance.

Carry one rule forward:

> A calculation is not an algorithm until the stopping condition and failure
> path are defined.

Before leaving, redo Worked Examples 3, 6, and 7 using a spreadsheet or short
script. Do not merely reproduce the final numbers. Build the iteration so that a
changed starting value, interval count, or time step propagates automatically.
That is the bridge from mathematics to algorithmic engineering.

— Your Mentor
