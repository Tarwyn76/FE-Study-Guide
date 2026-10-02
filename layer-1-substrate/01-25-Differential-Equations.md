---
chapter: "01-25"
title: "Differential Equations"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-025-01, MATH-1C-025-02, MATH-1C-025-03, MATH-1C-025-04, MATH-1C-025-05, MATH-1C-025-06, MATH-1C-025-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-25: Differential Equations

> *"A differential equation does not hand you the function. It tells you how the
> function is allowed to change. Your job is to recover the history that obeys
> that rule and the conditions that came with it."*

---

## Before You Start

**Prerequisites:** [01-05 Exponents, Radicals, and Logarithms](01-05-Exponents-Radicals-and-Logarithms.md) ·
[01-06 Functions, Graphs, and Transformations](01-06-Functions-Graphs-and-Transformations.md) ·
[01-07 Polynomials and Their Roots](01-07-Polynomials-and-Their-Roots.md) ·
[01-12 Complex Numbers](01-12-Complex-Numbers.md) ·
[01-17 The Derivative](01-17-The-Derivative.md) ·
[01-19 Antiderivatives and the Definite Integral](01-19-Antiderivatives-and-the-Definite-Integral.md) ·
[01-21 Techniques of Integration](01-21-Techniques-of-Integration.md) ·
[01-22 Infinite Series and Taylor Expansions](01-22-Infinite-Series-and-Taylor-Expansions.md)

**Skip if:** You pass the Tier 1C test-out quiz and can classify an equation by
order, linearity, and forcing; solve separable and first-order linear initial-value
problems; write all three constant-coefficient second-order homogeneous solution
forms; modify a particular-solution trial when resonance occurs; and solve a
simple initial-value problem with a unilateral Laplace transform. If you can
recognize the formulas but cannot explain why a repeated characteristic root
requires a factor of $t$, work this chapter.

**Time:** About 110–130 min reading and worked examples · 40–50 min review
questions · 70–90 min practice problems.

**Working convention:** The independent variable is $t$ unless another variable
is stated. Bare mathematical examples are dimensionless. Engineering models carry
units explicitly. A supplied physical differential equation is treated as a model;
this chapter teaches the mathematics of solving and checking it, not the later
discipline-specific derivation of the model.

---

## On the Board Today

Apprentice, every derivative chapter so far began with a known function and asked
what its rate of change was. Differential equations reverse that direction. The
rate law is known; the function is not.

A capacitor voltage, a tank level, a decaying concentration, a moving mass, and a
temperature can all be unknown functions of time. The governing model may tell you
that the rate is proportional to the present value, that acceleration depends on
position and velocity, or that a forcing input drives the system. The equation
contains the behavior. Initial conditions select the particular history that
actually occurred.

The central habit is **classification before calculation**. Do not start
integrating until you know what kind of equation you have. A method that is exact
for a first-order separable equation may be useless for a second-order linear
forced equation. The characteristic equation works beautifully for constant-
coefficient linear equations and not at all for a nonlinear term like $y^2$.

The working sequence for this chapter is:

> **Classify → choose a method → solve the family → apply conditions → substitute
> back → interpret the result.**

That last substitution is not optional. A differential equation is one of the
few places where you can usually test your entire symbolic answer directly by
putting it back into the original model.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **25.1** Distinguish an ordinary differential equation from a partial
  differential equation and identify an equation's order.
* **25.2** Classify an ODE as linear or nonlinear and, when linear, as homogeneous
  or nonhomogeneous.
* **25.3** Explain the role of initial conditions and verify a proposed solution by
  substitution.
* **25.4** Solve first-order separable initial-value problems, including
  exponential growth and decay.
* **25.5** Solve a first-order linear ODE with an integrating factor.
* **25.6** Identify the steady and transient parts of a stable first-order
  constant-coefficient response and interpret its time constant.
* **25.7** Form and solve the characteristic equation of a second-order linear
  homogeneous ODE with constant coefficients.
* **25.8** Write the distinct-real, repeated-real, and complex-conjugate solution
  forms and apply two initial conditions.
* **25.9** Relate the three root cases to over-, critical-, and underdamped
  response when the equation represents a standard second-order dynamic model.
* **25.10** Construct a particular-solution trial for common forcing functions and
  modify it when resonance occurs.
* **25.11** Write a nonhomogeneous solution as $y=y_h+y_p$ and distinguish
  transient from forced or steady-state behavior where that interpretation is
  valid.
* **25.12** Use unilateral Laplace-transform derivative rules to solve a simple
  initial-value problem with a step input.
* **25.13** Generate a coefficient recurrence for a simple power-series solution.
* **25.14** Select an appropriate solution method and check units, initial
  conditions, and substitution into the original equation.

---

## Notation Used Here

| Symbol | Meaning in this chapter | SI | USCS |
|---|---|---|---|
| $t$ | independent variable, usually time | s when time | s when time |
| $y(t)$ | unknown dependent variable | problem-dependent | problem-dependent |
| $y',y'',y^{(n)}$ | first, second, and $n$th derivatives of $y$ | $[y]/[t]$, $[y]/[t]^2$, ... | same dimensional pattern |
| $g(t)$ | forcing or source term | must match the equation's derivative terms | same dimensional requirement |
| $a,b,b_0,b_1,b_n$ | constant coefficients | coefficient units make all terms compatible | same rule |
| $C,C_1,C_2$ | constants selected by conditions | whatever units make $y$ consistent | same rule |
| $r$ | characteristic root | inverse independent-variable unit when exponent is dimensional | same dimensional role |
| $\alpha,\beta$ | real and imaginary parts of $r=\alpha\pm j\beta$ | inverse independent-variable unit | same |
| $\tau$ | first-order time constant | s | s |
| $K$ | gain in a supplied first-order model | output/input | output/input |
| $u(t)$ | unit-step function | 1 | 1 |
| $\delta(t)$ | unit impulse | $1/\mathrm{s}$ when $t$ is time | $1/\mathrm{s}$ |
| $s$ | unilateral Laplace-transform variable | $1/\mathrm{s}$ when $t$ is time | $1/\mathrm{s}$ |
| $Y(s)$ | Laplace transform of $y(t)$ | $[y]\cdot\mathrm s$ under the usual time transform | same dimensional role |
| $a_n$ | coefficient in a power-series solution | chosen so each term has units of $y$ | same rule |

> **Collision note.** $r$ is a characteristic root here, not a radius. The unit
> step $u(t)$ is a named input function, not the substitution variable $u$ from
> integration. The impulse symbol $\delta(t)$ is unrelated to beam deflection
> notation used later in mechanics. The complex unit remains $j$ as established
> in Chapter 01-12.

> ---
> **Mentor's Margin**
>
> Before solving, read the equation as a sentence. Which derivative is highest?
> Is there a forcing term? Are the coefficients constant? What information is
> supplied at the starting point?
>
> Most wrong differential-equation solutions begin one line before the algebra:
> the wrong method was chosen because the equation was never classified.
>
> ---

---

## 25.1 What a Differential Equation Is

A **differential equation** is an equation containing an unknown function and one
or more of its derivatives. An **ordinary differential equation (ODE)** has one
independent variable. A **partial differential equation (PDE)** has an unknown
function of several independent variables and contains partial derivatives.

For example,

$$\frac{dy}{dt}+3y=6$$

is an ODE because $y$ depends only on $t$, while

$$\frac{\partial T}{\partial t}=\kappa\frac{\partial^2T}{\partial x^2}$$

is a PDE because $T$ depends on at least $x$ and $t$. This chapter solves ODEs.
The PDE example is included only so you can recognize the distinction.

### Order

The **order** is the order of the highest derivative present. Thus

$$y''+4y'+7y=0$$

is second order. A second-order initial-value problem normally requires two
independent conditions to select one member of its two-constant solution family.

### Linear versus nonlinear

An ODE is **linear** in $y$ when $y$ and its derivatives appear only to the first
power, are not multiplied by one another, and have coefficients that depend only
on the independent variable. A general linear $n$th-order ODE has the form

$$a_n(t)y^{(n)}+a_{n-1}(t)y^{(n-1)}+\cdots+a_1(t)y'+a_0(t)y=g(t).$$

Examples of nonlinear terms are $y^2$, $(y')^2$, $yy'$, $\sin y$, and $e^y$.
The equation $t^2y''+ty'+y=0$ is still linear: its coefficients vary with $t$,
but the unknown function and its derivatives remain first power.

For a linear equation, **homogeneous** means the forcing side is zero,
$L[y]=0$. **Nonhomogeneous** means $L[y]=g(t)$ with $g(t)\ne0$.
Do not use "homogeneous" as a synonym for "constant coefficient."

### Initial conditions and initial-value problems

An **initial condition** specifies the function or one of its derivatives at a
particular value of the independent variable. An ODE together with enough such
conditions is an **initial-value problem (IVP)**. For example,

$$y''+4y=0,\qquad y(0)=2,\qquad y'(0)=-1$$

is a second-order IVP.

Conditions do not change the differential equation's solution method. They choose
the constants after the general solution has been found.

![FIG-01-25-001: A decision map classifies differential equations. The first split asks whether the unknown depends on one independent variable or several, leading to ODE or PDE. The ODE branch then asks for order, then linear versus nonlinear. The linear branch splits into homogeneous g(t)=0 and nonhomogeneous g(t)≠0, with a final note to inspect whether coefficients are constant or variable. Small example equations are placed beside each branch.](../figures/FIG-01-25-001-differential-equation-classification.png)

### Worked Example 1 — Classify Before Solving

**Given.** Classify each equation by ODE/PDE, order, linearity, and, when linear,
homogeneous/nonhomogeneous.

1. $y'+3y=e^t$
2. $y''+(y')^2=0$
3. $\partial T/\partial t=\kappa\,\partial^2T/\partial x^2$
4. $t^2y''+ty'+y=0$

**Solution.**

1. **First-order linear nonhomogeneous ODE.**
2. **Second-order nonlinear ODE** because of $(y')^2$.
3. **Second-order linear homogeneous PDE** when $\kappa$ is prescribed independently of $T$.
4. **Second-order linear homogeneous ODE with variable coefficients.**

**Check.** Classification is determined by the structure of the equation, not by
whether the coefficients happen to be numbers.

---

## 25.2 First-Order Separable Equations

A first-order equation is **separable** when it can be written

$$\frac{dy}{dt}=p(t)q(y)$$

and rearranged so all $y$ dependence is on one side and all $t$ dependence on the
other:

$$\frac{dy}{q(y)}=p(t)\,dt.$$

Integrate both sides, then apply the initial condition.

There is one important caution. Dividing by $q(y)$ can remove an **equilibrium
solution** for which $q(y)=0$. Check those values before dividing.

### Exponential growth and decay

The model

$$\frac{dy}{dt}=ky$$

has the solution

$$\boxed{y=C_1e^{kt}}.$$

If $t$ is time, $k$ must have units of inverse time so the exponent $kt$ is
dimensionless. For decay, writing $k=-1/\tau$ gives

$$\boxed{y=y_0e^{-t/\tau}}.$$

After one time constant, the remaining fraction is $e^{-1}=0.3679$.

![FIG-01-25-002: A slope field for y'=-0.5y is shown with short line segments: negative slopes above the t-axis, zero slope on y=0, and positive slopes below it. Several solution curves follow the field, including one starting at y=4 that decays toward zero and one starting below zero that rises toward zero. A vertical marker at one time constant τ=2 shows that the positive solution has fallen to e^-1 of its initial value.](../figures/FIG-01-25-002-separable-decay-slope-field.png)

### Worked Example 2 — Exponential Decay

**Given.** $dy/dt=-0.25y$, $y(0)=80$, with the coefficient in $\mathrm{s^{-1}}$.

**Find.** $y(t)$ and the time at which $y$ reaches one-half its initial value.

**Solution.**

$$\frac{dy}{y}=-0.25\,dt$$

$$\ln|y|=-0.25t+C$$

$$y=C_1e^{-0.25t}.$$

At $t=0$, $C_1=80$, so

$$\boxed{y(t)=80e^{-0.25t}}.$$

For $y=40$,

$$\frac12=e^{-0.25t}\implies
\boxed{t=\frac{\ln2}{0.25}=2.77\ \mathrm s}.$$

**Check.** $y'=-20e^{-0.25t}=-0.25y$, and $y(0)=80$.

---

## 25.3 First-Order Linear Equations

The standard first-order linear form is

$$\boxed{y'+p(t)y=q(t).}$$

A systematic solution uses the **integrating factor**

$$\boxed{\mu(t)=e^{\int p(t)\,dt}.}$$

Multiplying the ODE by $\mu$ makes the left side a product derivative:

$$\mu y'+\mu p y=\frac{d}{dt}(\mu y).$$

Therefore

$$\boxed{y=\frac{1}{\mu}\left(\int \mu q\,dt+C\right).}$$

### Worked Example 3 — A Variable-Coefficient Linear ODE

**Given.** For $t>0$,

$$y'+\frac{1}{t}y=t^2,\qquad y(1)=\frac54.$$

**Solution.**

$$\mu=e^{\int(1/t)dt}=t.$$

Multiplying through gives

$$ty'+y=t^3=(ty)'.$$

Thus

$$ty=\frac{t^4}{4}+C,
\qquad
y=\frac{t^3}{4}+\frac{C}{t}.$$

Using $y(1)=5/4$ gives $C=1$:

$$\boxed{y(t)=\frac{t^3}{4}+\frac1t,\qquad t>0.}$$

**Check.** $y'=3t^2/4-1/t^2$, so
$y'+y/t=t^2$ exactly.

### Constant forcing, transient, and steady state

For constant positive $a$,

$$y'+ay=b$$

has the solution

$$\boxed{y(t)=\frac{b}{a}+\left(y_0-\frac{b}{a}\right)e^{-at}}.$$

The constant $b/a$ is the long-time **steady-state response**. The exponential
term is the **transient response**. With $\tau=1/a$, the transient is
$e^{-t/\tau}$. After one time constant, 36.8% of the initial offset remains and
63.2% of the total transition has been completed.

![FIG-01-25-003: A first-order response begins at y0=1 and approaches the horizontal steady-state line y=3 according to y=3−2e^(−t/τ), with τ=0.5 s. A vertical line at t=τ marks y=2.264 and a bracket shows that 63.2% of the initial-to-final change has occurred. The total response is labeled steady state plus transient, and the shrinking gap to y=3 is labeled proportional to e^(−t/τ).](../figures/FIG-01-25-003-first-order-step-response.png)

### Worked Example 4 — First-Order Step Response

**Given.** $y'+2y=6$, $y(0)=1$.

**Solution.**

$$y_{ss}=3,\qquad \tau=\frac12.$$

The initial offset from steady state is $-2$, so

$$\boxed{y(t)=3-2e^{-2t}}.$$

At $t=\tau=0.5$,

$$y=3-2e^{-1}=2.264.$$

The completed change is $(2.264-1)/(3-1)=0.632$.

**Check.** $y'=4e^{-2t}$, so $y'+2y=6$ and $y(0)=1$.

---
## 25.4 Second-Order Linear Homogeneous Equations

For the constant-coefficient equation

$$\boxed{y''+ay'+by=0}$$

seek an exponential solution $y=Ce^{rt}$. Then

$$y'=rCe^{rt},\qquad y''=r^2Ce^{rt},$$

so substitution gives

$$(r^2+ar+b)Ce^{rt}=0.$$

For a nontrivial solution,

$$\boxed{r^2+ar+b=0}$$

must hold. This is the **characteristic equation**.

| Characteristic roots | Real solution form |
|---|---|
| Distinct real $r_1,r_2$ | $y=C_1e^{r_1t}+C_2e^{r_2t}$ |
| Repeated real $r$ | $y=(C_1+C_2t)e^{rt}$ |
| Complex $\alpha\pm j\beta$ | $y=e^{\alpha t}(C_1\cos\beta t+C_2\sin\beta t)$ |

The extra factor $t$ in the repeated-root case is essential. Without it,
$C_1e^{rt}+C_2e^{rt}$ collapses into one constant times $e^{rt}$ and cannot
provide the two independent constants a second-order solution needs.

### Root type and damping language

For $y''+ay'+by=0$, the discriminant $a^2-4b$ determines the root type. In a
standard stable second-order dynamic interpretation with positive parameters,
these are commonly called:

- $a^2>4b$: **overdamped**,
- $a^2=4b$: **critically damped**,
- $a^2<4b$: **underdamped**.

Those labels are a physical interpretation of the algebraic root cases. The root
classification itself applies whether the dependent variable is displacement,
voltage, temperature, concentration, or something else.

![FIG-01-25-004: Three normalized time-response plots share the same axes and initial displacement. The overdamped curve returns to zero without oscillation using two distinct decaying exponentials; the critically damped curve returns faster without overshoot and is labeled repeated root; the underdamped curve crosses zero repeatedly inside a decaying exponential envelope and is labeled complex-conjugate roots. A small characteristic-root inset shows two negative real roots, one repeated negative root, and a complex pair with negative real part.](../figures/FIG-01-25-004-second-order-root-cases.png)

### Worked Example 5 — Distinct Real Roots and Initial Conditions

**Given.**

$$y''+6y'+8y=0,\qquad y(0)=3,\qquad y'(0)=-8.$$

**Find.** $y(t)$.

**Solution.**

$$r^2+6r+8=0=(r+2)(r+4),$$

so

$$y=C_1e^{-2t}+C_2e^{-4t}.$$

At $t=0$,

$$C_1+C_2=3. \tag{1}$$

Differentiate:

$$y'=-2C_1e^{-2t}-4C_2e^{-4t}.$$

At $t=0$,

$$-2C_1-4C_2=-8. \tag{2}$$

Solving gives $C_1=2$ and $C_2=1$:

$$\boxed{y(t)=2e^{-2t}+e^{-4t}}.$$

**Check.** $y(0)=3$ and $y'(0)=-8$. Each exponential separately satisfies the
ODE because its exponent is a root of the characteristic polynomial.

---

## 25.5 Nonhomogeneous Equations and Particular Solutions

For a linear nonhomogeneous equation

$$L[y]=g(t),$$

the complete solution has the form

$$\boxed{y=y_h+y_p}$$

where $y_h$ solves $L[y_h]=0$ and $y_p$ is any one **particular solution** that
satisfies $L[y_p]=g(t)$.

For constant coefficients, the **method of undetermined coefficients** chooses a
trial from the same functional family as the forcing:

| Forcing $g(t)$ | Typical particular trial |
|---|---|
| constant | $A$ |
| polynomial degree $n$ | polynomial degree $n$ |
| $e^{\lambda t}$ | $Ae^{\lambda t}$ |
| $\cos\omega t$ or $\sin\omega t$ | $A\cos\omega t+B\sin\omega t$ |

If the ordinary trial duplicates part of $y_h$, the forcing is in **resonance**
with a homogeneous mode. Multiply the entire trial by enough powers of $t$ to make
it independent of $y_h$. A simple collision needs one factor of $t$.

### Worked Example 6 — Resonance Changes the Trial

**Given.**

$$y''+4y=8\cos2t.$$

**Find.** The general solution.

**Solution.** The homogeneous characteristic equation is

$$r^2+4=0\implies r=\pm2j,$$

so

$$y_h=C_1\cos2t+C_2\sin2t.$$

A naive trial $A\cos2t+B\sin2t$ duplicates $y_h$. Multiply by $t$. One convenient
trial is

$$y_p=At\sin2t.$$

Then

$$y_p'=A\sin2t+2At\cos2t,$$

$$y_p''=4A\cos2t-4At\sin2t,$$

and therefore

$$y_p''+4y_p=4A\cos2t.$$

Matching the forcing gives $A=2$. Hence

$$\boxed{y=C_1\cos2t+C_2\sin2t+2t\sin2t}.$$

**Check.** The homogeneous terms contribute zero to $y''+4y$, and the particular
term contributes exactly $8\cos2t$.

![FIG-01-25-005: A resonance illustration compares the forcing cos(2t) with a particular response 2t sin(2t). The response oscillates at the same angular frequency inside straight-line envelopes +2t and −2t whose magnitude grows with time. A side annotation shows that the ordinary sinusoidal trial duplicates the homogeneous solution and must be multiplied by t.](../figures/FIG-01-25-005-resonance-particular-solution.png)

### Transient and forced response

When the homogeneous modes decay with time, $y_h$ is the **transient response**:
it contains the influence of the initial conditions and fades away. A bounded
particular solution driven by a continuing input is then the forced or
**steady-state response**. Do not apply those labels mechanically. In the resonant
undamped example above, the particular response grows rather than approaching a
steady amplitude.

---

## 25.6 Laplace Transforms for Initial-Value Problems

The unilateral **Laplace transform** converts a time-domain function into an
algebraic function of $s$:

$$\boxed{F(s)=\mathcal L\{f(t)\}=\int_0^\infty f(t)e^{-st}\,dt.}$$

The practical advantage for an IVP is that differentiation becomes multiplication
by $s$ plus initial-condition terms:

$$\boxed{\mathcal L\{y'\}=sY(s)-y(0)}$$

$$\boxed{\mathcal L\{y''\}=s^2Y(s)-sy(0)-y'(0)}.$$

The unit step and impulse satisfy

$$\mathcal L\{u(t)\}=\frac1s,\qquad
\mathcal L\{\delta(t)\}=1.$$

A reliable Laplace workflow is:

1. transform every term,
2. insert initial conditions immediately,
3. solve algebraically for $Y(s)$,
4. decompose $Y(s)$ as needed,
5. invert term by term,
6. check the initial value and the original ODE.

![FIG-01-25-006: A left-to-right workflow diagram begins with a time-domain initial-value problem, passes through a Laplace-transform block where derivatives become sY minus initial-condition terms, then an algebra block solves for Y(s), a partial-fraction block decomposes it, and an inverse-transform block returns y(t). The initial conditions are shown entering the transform block rather than being applied at the end.](../figures/FIG-01-25-006-laplace-ivp-workflow.png)

### Worked Example 7 — The Same First-Order Response by Laplace Transform

**Given.**

$$y'+2y=6u(t),\qquad y(0)=1.$$

**Find.** $y(t)$ for $t\ge0$.

**Solution.** Transform both sides:

$$sY-1+2Y=\frac6s.$$

Then

$$(s+2)Y=\frac{s+6}{s},$$

so

$$Y=\frac{s+6}{s(s+2)}=\frac3s-\frac2{s+2}.$$

Invert:

$$\boxed{y(t)=3-2e^{-2t}}.$$

This matches Worked Example 4.

**Check.** $y(0^+)=1$, and for $t>0$, $y'+2y=6$. The long-time value is 3.

### Initial- and final-value checks

The Handbook also prints initial- and final-value theorems, with the explicit
qualification that the required limits must exist. They are useful checks, not a
license to assume a final value exists when the time-domain response does not
settle.

---

## 25.7 Power-Series Solutions and Method Selection

Chapter 01-22 promised that series would return as a solution method. Assume

$$y(t)=\sum_{n=0}^\infty a_nt^n.$$

Inside the interval of convergence,

$$y' = \sum_{n=0}^\infty (n+1)a_{n+1}t^n,$$

$$y'' = \sum_{n=0}^\infty (n+2)(n+1)a_{n+2}t^n.$$

Substitute the series into the ODE and make coefficients of equal powers of $t$
match. The differential equation becomes a recurrence for the coefficients.

### Worked Example 8 — The Cosine Series from an ODE

**Given.**

$$y''+y=0,\qquad y(0)=1,\qquad y'(0)=0.$$

**Solution.** Substitution gives

$$\sum_{n=0}^\infty\left[(n+2)(n+1)a_{n+2}+a_n\right]t^n=0.$$

Therefore

$$\boxed{a_{n+2}=-\frac{a_n}{(n+2)(n+1)}}.$$

The initial conditions give $a_0=1$, $a_1=0$. Then

$$a_2=-\frac12,\qquad a_3=0,$$

$$a_4=\frac1{24},\qquad a_5=0,$$

$$a_6=-\frac1{720}.$$

Thus

$$y(t)=1-\frac{t^2}{2!}+\frac{t^4}{4!}-\frac{t^6}{6!}+\cdots
=\boxed{\cos t}.$$

**Check.** $\cos0=1$, $-\sin0=0$, and $y''+y=0$.

![FIG-01-25-007: A coefficient ladder for the power-series solution of y''+y=0 starts with a0=1 and a1=0. Arrows use the recurrence a_(n+2)=−a_n/[(n+2)(n+1)] to generate the even coefficients 1, −1/2!, +1/4!, −1/6!, while the odd branch remains zero. The resulting series is shown converging to the curve y=cos t.](../figures/FIG-01-25-007-power-series-recurrence.png)

### Choosing a method

| Equation pattern | First method to consider |
|---|---|
| $y'=p(t)q(y)$ | separation of variables |
| $y'+p(t)y=q(t)$ | integrating factor |
| constant-coefficient homogeneous linear ODE | characteristic equation |
| constant-coefficient nonhomogeneous ODE with standard forcing | $y_h+y_p$, often undetermined coefficients |
| linear IVP with steps, impulses, or transform-friendly forcing | Laplace transform |
| variable-coefficient equation near a regular expansion point | power series |
| no useful closed form or data-defined model | numerical method — Chapter 01-26 |

> **Preview note.** Chapter 01-26 develops numerical methods, including Euler's
> approximation. The Handbook prints Euler's ODE update on page 63 and notes that
> an $n$th-order ODE can be recast as $n$ first-order equations. Here, use that as
> a map marker rather than a new method to memorize.

### The verification stack

A differential-equation answer can usually be checked four ways:

**1. Substitute into the ODE.** The left and right sides must agree.

**2. Check every supplied condition.** A correct general solution with the wrong
constants is still the wrong IVP solution.

**3. Check units.** Terms added in the ODE must share units. Exponential arguments
must be dimensionless.

**4. Check limiting behavior.** A stable first-order response should approach its
steady value; a decay law with positive time constant should not grow.

---
## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed page 53 begins the Mathematics
> subsection titled *Differential Equations*; printed page 54 continues the
> second-order constant-coefficient cases. Printed page 58 gives unilateral
> Laplace-transform pairs and derivative rules. Printed page 63 gives Euler's
> approximation for numerical ODE solution. In this supplied 506-page PDF those
> are PDF pages 59, 60, 64, and 69 respectively.

Use the search method from
[00-03 Navigating the FE Reference Handbook](../layer-0-orientation/00-03-navigating-the-fe-reference-book.md):
search the equation family or transform name, identify the assumptions, and map
the Handbook's local symbols to the problem before substituting.

| Handbook heading | Printed page | Verified coverage and its limit |
|---|---:|---|
| Mathematics / Differential Equations | 53 | Gives a common constant-coefficient linear $n$th-order form, homogeneous exponential-root solution structure, repeated-root modification, $y=y_h+y_p$, resonance language, several particular-solution trial families, and the first-order homogeneous form $y'+ay=0$ with $y=Ce^{-at}$. |
| Mathematics / Second-Order Linear Homogeneous Differential Equations with Constant Coefficients | 54 | Gives the characteristic equation for $y''+ay'+by=0$ and the distinct-real, repeated-real, and complex-root solution forms, labeled over-, critical-, and underdamped. |
| Mathematics / Laplace Transforms | 58 | Gives the unilateral transform pair, common pairs including impulse, step, ramp, exponentials and damped sine/cosine, derivative-transform rules containing initial conditions, and initial/final value theorems. |
| Mathematics / Numerical Solution of Ordinary Differential Equations | 63 | Gives Euler's approximation and states that higher-order ODEs can be recast as systems of first-order equations. Full numerical-method development is deferred to 01-26. |

**Methods to learn from this guide.** The general separation-of-variables
procedure, the integrating-factor formula, the classification workflow, the
repeated-root independence explanation, the complete undetermined-coefficients
trial-selection procedure, and the power-series recurrence method are not supplied
as step-by-step procedures in the cited Handbook material. The reference gives
valuable solution forms and transform pairs; method recognition remains your job.

**Notation translation.** The Handbook often writes the independent variable as
$x$ in its general ODE form and uses $t$ when discussing transient systems. This
chapter uses $t$ by default. The Handbook's characteristic roots $r_i$ correspond
directly to the $r$ values used here.

**Know without a lookup:** how to classify the equation, when separation is legal,
how an integrating factor is constructed, why a repeated root needs an extra
factor of $t$, when a particular trial collides with $y_h$, and where the initial
conditions enter a Laplace-transform solution.

---

## Where This Goes Wrong

**Solving before classifying.** The characteristic equation is not a universal
ODE method. It belongs to linear constant-coefficient equations.

**Calling every zero-right-side equation "homogeneous" without checking
linearity.** The homogeneous/nonhomogeneous split used here belongs to linear
ODEs. $y'+y^2=0$ is nonlinear even though the right side is zero.

**Losing an equilibrium solution during separation.** Dividing by $q(y)$ assumes
$q(y)\ne0$. Check the zeros of $q$ first.

**Forgetting the integration constant.** A first-order ODE normally needs one
constant before an initial condition is applied. A second-order homogeneous ODE
needs two independent constants.

**Using $e^{rt}$ when coefficients vary with time.** The characteristic-polynomial
construction requires constant coefficients in the form taught here.

**Dropping the $t$ on a repeated root.** $(C_1+C_2)e^{rt}$ contains only one
independent constant. The second solution is $te^{rt}$.

**Leaving a complex pair in complex form when the requested solution is real.**
Use $e^{\alpha t}(C_1\cos\beta t+C_2\sin\beta t)$.

**Choosing a particular trial that duplicates $y_h$.** Multiply the entire trial
by $t$ once for a simple collision, and by a sufficient higher power for repeated
collisions.

**Calling every particular solution "steady state."** It may grow, as the
resonant example does. Steady-state language requires the long-time behavior to
settle appropriately.

**Dropping initial terms in a Laplace derivative.** $\mathcal L\{y'\}=sY-y(0)$,
not merely $sY$. Those terms are the main reason Laplace methods handle IVPs well.

**Using the final-value theorem when no final value exists.** The Handbook itself
qualifies the theorem by assuming the limit exists.

**Putting units inside an exponential.** $e^{-0.25t}$ is meaningful only when
$0.25$ carries reciprocal units matching $t$.

**Matching the wrong powers in a series solution.** Re-index derivatives so every
sum uses the same power $t^n$ before equating coefficients.

---

## Key Terms

| Term | Definition |
|---|---|
| Differential equation | Equation containing an unknown function and one or more of its derivatives |
| Ordinary differential equation (ODE) | Differential equation with one independent variable |
| Partial differential equation (PDE) | Differential equation containing partial derivatives of a function of several independent variables |
| Order | Order of the highest derivative appearing in the differential equation |
| Linear differential equation | Differential equation in which the unknown function and its derivatives appear to first power and are not multiplied together |
| Homogeneous linear differential equation | Linear differential equation with zero forcing term |
| Nonhomogeneous linear differential equation | Linear differential equation with a nonzero forcing term |
| Initial condition | Specified value of the unknown function or one of its derivatives at a particular independent-variable value |
| Initial-value problem (IVP) | Differential equation together with enough initial conditions to select a particular solution |
| Separable equation | First-order ODE that can be rearranged into a function of $y$ times $dy$ equal to a function of the independent variable times its differential |
| Equilibrium solution | Constant solution occurring where the rate law is zero |
| Integrating factor | Multiplying function that converts a first-order linear ODE into a product derivative |
| Time constant | Characteristic time $\tau$ controlling exponential decay or approach to steady state |
| Characteristic equation | Algebraic polynomial obtained by substituting an exponential trial into a constant-coefficient homogeneous linear ODE |
| Homogeneous solution | General solution $y_h$ of the associated zero-forcing linear equation |
| Particular solution | Any one solution $y_p$ that reproduces the specified forcing |
| Complete solution | Sum $y=y_h+y_p$ for a linear nonhomogeneous ODE |
| Transient response | Portion of a response associated with homogeneous modes that often decays with time in a stable system |
| Steady-state response | Long-time response remaining after decaying transients vanish, when such a limit exists |
| Resonance | Collision between a forcing trial and a homogeneous mode requiring modification of the particular-solution trial |
| Unilateral Laplace transform | Transform integrating from $0$ to $\infty$, useful for causal initial-value problems |
| Unit step | Function $u(t)$ that switches from zero to one at the origin in the idealized model |
| Unit impulse | Idealized concentrated input $\delta(t)$ whose transform is 1 |
| Power-series solution | Solution represented locally as a power series whose coefficients satisfy recurrences obtained from the ODE |

---

## Review Questions

Answer conceptual questions before reaching for a calculator. For calculations,
show the classification and check at least the initial conditions or direct
substitution.

### Conceptual

1. What makes an equation an ODE rather than a PDE? Give one example of each.
2. Define the order of a differential equation. Why does a second-order IVP
   normally need two independent initial conditions?
3. State the structural requirements for a differential equation to be linear in
   $y$. Why is $t^2y''+ty'+y=0$ linear but $y''+yy'=0$ nonlinear?
4. In a linear ODE, distinguish homogeneous from nonhomogeneous. Does a zero right
   side make a nonlinear equation "homogeneous" in the sense used in this chapter?
5. Explain why dividing by $q(y)$ while separating variables can lose an
   equilibrium solution.
6. Derive the integrating factor for $y'+p(t)y=q(t)$ and state what it accomplishes.
7. For a stable first-order response, what fraction of the initial offset remains
   after one time constant? What fraction of the transition is complete?
8. Explain why a repeated characteristic root requires $te^{rt}$ as a second
   solution rather than another constant times $e^{rt}$.
9. What does resonance mean in the method of undetermined coefficients, and how
   is the trial modified for a simple collision?
10. Why do Laplace derivative formulas contain initial-condition terms? Where
    should those conditions be inserted in the transform workflow?

### Calculation

11. Solve $y'=-0.4y$, $y(0)=25$, and find $y(5)$.
12. Solve $y'=3t^2$, $y(0)=4$.
13. Solve $y'+2y=8$, $y(0)=0$, and identify the steady value and time constant.
14. For $t>0$, solve $y'+\frac1t y=t^2$, $y(1)=\frac54$.
15. Solve $y''+5y'+6y=0$, $y(0)=2$, $y'(0)=-5$.
16. Solve $y''+4y'+4y=0$, $y(0)=1$, $y'(0)=0$.
17. Solve $y''+2y'+10y=0$, $y(0)=0$, $y'(0)=3$.
18. Find one particular solution of $y''+y=3e^{2t}$.
19. Use a Laplace transform to solve $y'+y=1$, $y(0)=2$ for $t\ge0$.

### Multiple Choice

20. Which equation is nonlinear?
    A) $y''+3y'+2y=0$  B) $ty'+y=t$  C) $y'+y^2=0$  D) $y''+t^2y=\sin t$.
21. The characteristic roots of $y''+6y'+9y=0$ are:
    A) $-3,-3$  B) $3,3$  C) $-6,-9$  D) $\pm3j$.
22. A repeated root $r=-2$ gives which homogeneous solution?
    A) $(C_1+C_2t)e^{-2t}$  B) $C_1e^{-2t}+C_2e^{2t}$
    C) $e^{-2t}(C_1\cos2t+C_2\sin2t)$  D) $C_1+C_2e^{-2t}$.
23. For $y'+4y=12$, the steady value is:
    A) 48  B) 16  C) 4  D) 3.
24. If $g(t)=5\cos3t$ and $\pm3j$ are not characteristic roots, a suitable
    particular trial begins as:
    A) $A\cos3t+B\sin3t$  B) $Ae^{3t}$  C) $At^3$  D) $A/t$.
25. $\mathcal L\{y'\}$ equals:
    A) $sY$  B) $sY-y(0)$  C) $Y/s$  D) $s^2Y-y'(0)$.
26. For $y'=ky$ with $k<0$, the magnitude of $y$ for nonzero initial value:
    A) grows exponentially  B) remains constant  C) decays exponentially
    D) must oscillate.
27. The recurrence $a_{n+2}=-a_n/[(n+2)(n+1)]$ with $a_0=1,a_1=0$ generates:
    A) $e^t$  B) $\sin t$  C) $\cos t$  D) $1/(1-t)$.

---

## Answer Key with Explanations

### Conceptual

1. An ODE has one independent variable and ordinary derivatives, for example
   $y'+2y=0$. A PDE has a function of several independent variables and partial
   derivatives, for example $T_t=\kappa T_{xx}$. (§25.1)
2. Order is the highest derivative order. A second-order general solution normally
   contains two independent constants, so two independent conditions are needed to
   determine them. (§25.1, §25.4)
3. Linearity requires $y$ and its derivatives to first power, no products among
   them, and coefficients depending only on the independent variable.
   $t^2y''+ty'+y=0$ satisfies that structure; $yy'$ is nonlinear. (§25.1)
4. Homogeneous means the forcing term of a linear equation is zero;
   nonhomogeneous means it is nonzero. A nonlinear zero-right-side equation is
   still nonlinear. (§25.1)
5. If $q(y_*)=0$, then $y=y_*$ may be a constant solution. Dividing by $q(y)$
   excludes that value from the algebra, so it must be checked first. (§25.2)
6. $\mu=e^{\int p(t)dt}$. It makes
   $\mu y'+\mu p y=(\mu y)'$, converting the ODE to one directly integrable
   derivative. (§25.3)
7. $e^{-1}=36.8\%$ remains; $1-e^{-1}=63.2\%$ is complete. (§25.3)
8. Two constants multiplying the same $e^{rt}$ combine into one. $te^{rt}$ is a
   linearly independent second solution. (§25.4)
9. Resonance occurs when the ordinary particular trial duplicates a homogeneous
   mode. Multiply the whole trial by $t$ once for a simple collision. (§25.5)
10. Transforming a derivative produces boundary terms containing the initial
    values. Insert them during the transform step, before solving for $Y(s)$.
    (§25.6)

### Calculation

11. $\boxed{y=25e^{-0.4t}}$. At $t=5$,
    $y=25e^{-2}=\boxed{3.38}$. (§25.2)
12. $y=t^3+C$ and $y(0)=4$, so $\boxed{y=t^3+4}$. (§25.2)
13. $y_{ss}=8/2=4$, $\tau=1/2$, and
    $\boxed{y=4(1-e^{-2t})}$. (§25.3)
14. $\mu=t$, so $(ty)'=t^3$ and
    $y=t^3/4+C/t$. The condition gives $C=1$:
    $\boxed{y=t^3/4+1/t}$ for $t>0$. (§25.3)
15. Roots are $-2,-3$. Conditions give $C_1=C_2=1$:
    $\boxed{y=e^{-2t}+e^{-3t}}$. (§25.4)
16. The repeated root is $-2$. Conditions give $C_1=1,C_2=2$:
    $\boxed{y=(1+2t)e^{-2t}}$. (§25.4)
17. Roots are $-1\pm3j$. Conditions give $C_1=0,C_2=1$:
    $\boxed{y=e^{-t}\sin3t}$. (§25.4)
18. Try $y_p=Ae^{2t}$. Then $(4A+A)e^{2t}=3e^{2t}$, so
    $\boxed{y_p=(3/5)e^{2t}}$. (§25.5)
19. $sY-2+Y=1/s$, so
    $Y=(2s+1)/[s(s+1)]=1/s+1/(s+1)$. Therefore
    $\boxed{y=1+e^{-t}}$. (§25.6)

### Multiple Choice

20. **C.** The $y^2$ term makes the equation nonlinear. (§25.1)
21. **A.** $(r+3)^2=0$. (§25.4)
22. **A.** A repeated root requires the independent factor $t e^{-2t}$. (§25.4)
23. **D.** $y_{ss}=b/a=12/4=3$. (§25.3)
24. **A.** Sinusoidal forcing requires both sine and cosine in the ordinary trial.
    (§25.5)
25. **B.** $\mathcal L\{y'\}=sY-y(0)$. (§25.6)
26. **C.** Negative $k$ produces exponential decay. (§25.2)
27. **C.** The recurrence generates the cosine series. (§25.7)

---
## Practice Problems

Work these without the solutions first. State the equation class before choosing a
method.

1. **Classification.** Classify each as ODE/PDE, order, linear/nonlinear, and
   homogeneous/nonhomogeneous when linear:
   (a) $y''-4y'+4y=t$,
   (b) $y'+ty^2=0$,
   (c) $\partial C/\partial t=D\,\partial^2C/\partial x^2$,
   (d) $t^3y''+y=0$.
2. **Approach to ambient.** A supplied first-order model is
   $dy/dt=-0.30(y-20)$ with $y(0)=100$. Find $y(t)$ and the time when $y=40$.
3. **Variable-coefficient first order.** For $t>0$, solve
   $y'+(1/t)y=t^2$, $y(1)=5/4$.
4. **Distinct roots.** Solve
   $y''+5y'+6y=0$, $y(0)=2$, $y'(0)=-5$.
5. **Repeated root.** Solve
   $y''+4y'+4y=0$, $y(0)=1$, $y'(0)=0$.
6. **Complex roots.** Solve
   $y''+2y'+10y=0$, $y(0)=0$, $y'(0)=3$.
7. **Forced second order.** Solve the IVP
   $y''+3y'+2y=4$, $y(0)=0$, $y'(0)=0$.
8. **Laplace step response.** Use a Laplace transform to solve
   $y'+3y=6u(t)$, $y(0)=0$.
9. **Series solution.** For $y''+4y=0$, $y(0)=1$, $y'(0)=0$, derive the recurrence
   and write terms through $t^6$. Identify the familiar closed form.
10. **Supplied first-order engineering model.** A sensor follows
    $\tau\,dy/dt+y=Kx_0$ after a constant input is applied at $t=0$. Let
    $\tau=4.00\ \mathrm s$, $Kx_0=10.0$ output units, and $y(0)=2.00$ output
    units. Find $y(t)$ and the time required to complete 95% of the total
    initial-to-final change.

---

## Practice Problem Solutions

1. **Classification.** (a) second-order linear nonhomogeneous ODE; (b) first-order
   nonlinear ODE because of $y^2$; (c) second-order linear homogeneous PDE when
   $D$ is prescribed independently of $C$; (d) second-order linear homogeneous ODE
   with variable coefficient. **Check:** coefficient variation does not by itself
   make an equation nonlinear. (§25.1)

2. Let $z=y-20$. Then $z'=-0.30z$ and $z(0)=80$, so

   $$\boxed{y=20+80e^{-0.30t}}.$$

   Set $y=40$:

   $$20=80e^{-0.30t}\implies e^{-0.30t}=0.25,$$

   $$\boxed{t=\frac{\ln4}{0.30}=4.62}$$

   in the time unit used by the model. **Check:** the solution approaches 20 from
   above and starts at 100. (§25.2, §25.3)

3. $\mu=t$, giving $(ty)'=t^3$. Therefore

   $$y=\frac{t^3}{4}+\frac Ct.$$

   $y(1)=5/4$ gives $C=1$:

   $$\boxed{y=\frac{t^3}{4}+\frac1t,\quad t>0}.$$

   **Check:** substitution returns $t^2$. (§25.3)

4. Roots are $-2,-3$, so

   $$y=C_1e^{-2t}+C_2e^{-3t}.$$

   The conditions give $C_1=C_2=1$:

   $$\boxed{y=e^{-2t}+e^{-3t}}.$$

   (§25.4)

5. The repeated root is $-2$:

   $$y=(C_1+C_2t)e^{-2t}.$$

   Conditions give $C_1=1,C_2=2$:

   $$\boxed{y=(1+2t)e^{-2t}}.$$

   (§25.4)

6. Roots are $-1\pm3j$:

   $$y=e^{-t}(C_1\cos3t+C_2\sin3t).$$

   Conditions give $C_1=0,C_2=1$:

   $$\boxed{y=e^{-t}\sin3t}.$$

   **Check:** $y'(0)=3$. (§25.4)

7. Homogeneous roots are $-1,-2$, so

   $$y_h=C_1e^{-t}+C_2e^{-2t}.$$

   For constant forcing, try $y_p=A$. Then $2A=4$, so $A=2$. Thus

   $$y=2+C_1e^{-t}+C_2e^{-2t}.$$

   $y(0)=0$ gives $C_1+C_2=-2$. The derivative condition gives
   $-C_1-2C_2=0$. Hence $C_1=-4,C_2=2$:

   $$\boxed{y=2-4e^{-t}+2e^{-2t}}.$$

   **Check:** $y\to2$ and both initial conditions are satisfied. (§25.5)

8. Transform:

   $$sY+3Y=\frac6s,$$

   $$Y=\frac6{s(s+3)}=\frac2s-\frac2{s+3}.$$

   Therefore

   $$\boxed{y=2(1-e^{-3t})}.$$

   **Check:** $y(0)=0$ and $y\to2=6/3$. (§25.6)

9. Substitution into $y''+4y=0$ gives

   $$\boxed{a_{n+2}=-\frac{4a_n}{(n+2)(n+1)}}.$$

   With $a_0=1,a_1=0$,

   $$a_2=-2,\qquad a_4=\frac23,\qquad a_6=-\frac4{45}.$$

   Hence

   $$\boxed{y=1-2t^2+\frac23t^4-\frac4{45}t^6+\cdots=\cos2t}.$$

   (§25.7)

10. The steady value is $10.0$ and the initial offset is $-8.00$, so

    $$\boxed{y(t)=10.0-8.00e^{-t/4.00}}.$$

    Completing 95% of the transition means 5% of the initial offset remains:

    $$e^{-t/4}=0.05,$$

    $$\boxed{t=-4\ln(0.05)=11.98\ \mathrm s\approx12.0\ \mathrm s}.$$

    **Check:** $y(0)=2.00$, $y\to10.0$, and $t/(4.00\ \mathrm s)$ is
    dimensionless. (§25.3)

---

## Quick Reference

**Classify first**

- ODE: one independent variable; PDE: several independent variables with partial derivatives.
- Order = highest derivative order.
- Linear: $y$ and derivatives first power, no products among them.
- Linear homogeneous: forcing is zero; nonhomogeneous: forcing is nonzero.

**Separable first order**

$$\frac{dy}{dt}=p(t)q(y)
\quad\Longrightarrow\quad
\frac{dy}{q(y)}=p(t)dt.$$

Check $q(y)=0$ equilibrium solutions before dividing.

**First-order linear**

$$y'+p(t)y=q(t),\qquad
\mu=e^{\int p(t)dt},\qquad
(\mu y)'=\mu q.$$

For $y'+ay=b$ with $a>0$:

$$y=\frac ba+\left(y_0-\frac ba\right)e^{-at},\qquad \tau=\frac1a.$$

**Second-order homogeneous constant coefficients**

$$y''+ay'+by=0\quad\Rightarrow\quad r^2+ar+b=0.$$

Distinct real:

$$y=C_1e^{r_1t}+C_2e^{r_2t}.$$

Repeated real:

$$y=(C_1+C_2t)e^{rt}.$$

Complex $\alpha\pm j\beta$:

$$y=e^{\alpha t}(C_1\cos\beta t+C_2\sin\beta t).$$

**Nonhomogeneous**

$$\boxed{y=y_h+y_p}$$

If the particular trial overlaps $y_h$, multiply the full trial by a sufficient
power of $t$.

**Laplace derivative rules**

$$\mathcal L\{y'\}=sY-y(0),$$

$$\mathcal L\{y''\}=s^2Y-sy(0)-y'(0).$$

$$\mathcal L\{u(t)\}=\frac1s,\qquad \mathcal L\{\delta(t)\}=1.$$

**Series recurrence pattern**

Assume $y=\sum a_nt^n$, differentiate, align all sums to the same power $t^n$,
and equate coefficients.

**Final check:** substitute into the ODE · satisfy every condition · verify units ·
inspect limiting behavior.

---

## What's Next

You now have the analytical side of differential equations: recognize the model,
select a solution family, enforce initial conditions, and verify the result.
That is enough for a large class of FE-scale transient and dynamic problems.

The next chapter, **01-26 Numerical Methods**, handles the cases where algebra does
not close cleanly or where the problem gives data rather than a convenient
formula. Newton's method turns nonlinear equations into iterations. Finite
differences turn derivatives into computable approximations. Euler's method and
related updates march a differential equation forward step by step. Numerical
integration replaces an unavailable antiderivative with weighted sums.

Bring two habits from this chapter with you. First, an iterative result still has
to satisfy the original model to an acceptable tolerance. Second, step size is
not merely a calculator setting; it controls approximation error and sometimes
stability.

Before moving on, solve Review Questions 15, 16, and 17 consecutively without the
table. If you can identify the root type and write the correct real solution form
before doing any arithmetic, the characteristic-equation framework is in place.

— Your Mentor
