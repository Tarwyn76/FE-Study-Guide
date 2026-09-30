---
chapter: "01-23"
title: "Partial Derivatives and Vector Calculus"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-023-01, MATH-1C-023-02, MATH-1C-023-03, MATH-1C-023-04, MATH-1C-023-05, MATH-1C-023-06, MATH-1C-023-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: revised
---

# Chapter 01-23: Partial Derivatives and Vector Calculus

> *"A result can depend on several measurements, and each measurement can move
> it a different way. Before you decide which input matters most, ask what changes
> when you move that input and hold the others still. That is the question a
> partial derivative answers."*

---

## Before You Start

**Prerequisites:** [01-06 Functions, Graphs, and Transformations](01-06-Functions-Graphs-and-Transformations.md) · [01-09 Analytic Geometry](01-09-Analytic-Geometry.md) · [01-11 Trigonometry](01-11-Trigonometry.md) · [01-13 Vectors and Vector Operations](01-13-Vectors-and-Vector-Operations.md) · [01-14 Matrices, Determinants, and Eigenvalues](01-14-Matrices-Determinants-and-Eigenvalues.md) · [01-16 Limits and Continuity](01-16-Limits-and-Continuity.md) · [01-17 The Derivative](01-17-The-Derivative.md) · [01-18 Applications of the Derivative](01-18-Applications-of-the-Derivative.md) · [01-22 Infinite Series and Taylor Expansions](01-22-Infinite-Series-and-Taylor-Expansions.md)

**Skip if:** You pass the Tier 1C test-out quiz and can independently compute mixed
partials, estimate uncertainty with a total differential, normalize a direction
vector, and distinguish gradient, divergence, and curl. Also check that you can
classify a two-variable critical point and set up an equality constraint. If any
one of those is unfamiliar, work its section before moving on.

**Time:** About 100–120 min reading and worked examples · 40–50 min review
questions · 60–90 min practice problems. Split the work into two sittings if needed.

**Working convention:** Bare algebraic examples use dimensionless variables.
Engineering problems state their units and supply the physical model. You are
responsible for differentiating that model, not for knowing an untaught circuit,
heat-transfer, or beam-theory derivation.

---

## On the Board Today

Apprentice, a cylinder's volume depends on its radius **and** its height. A
calculated electrical power can change because a voltage changes, a resistance
changes, or both change together. A temperature map has an uphill direction at
each location, and that direction need not follow either coordinate axis.

The single-variable derivative from Chapter 01-17 still does the work. We need
to organize it so that several inputs can share the same output.

**First, one input at a time.** A partial derivative measures the sensitivity to
one input while the others stay fixed. The differentiation rules do not change.

**Then, all the inputs together.** The total differential combines small input
changes. It gives us a local approximation and a way to estimate how measurement
uncertainties affect a computed result. Keep those two words together: *local
approximation*. A first-order estimate is not an exact tolerance guarantee.

**Then, direction.** For an output that varies with position, the gradient points
toward the fastest increase. A directional derivative tells you what happens
along the particular direction you choose.

**Then, a field of arrows.** Divergence measures local net outflow; curl measures
local rotation. Their formulas look similar enough to confuse under pressure,
so we will build the distinction before using them.

**Finally, a design choice.** We will locate maxima, minima, and saddle points,
then minimize material while keeping a tank's volume fixed. That constraint
changes which moves are allowed, and the mathematics has to respect it.

The habit running through the chapter is the same one you already know: state
what is held fixed, carry the units, and check whether the answer makes physical
and mathematical sense.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 23.1 Interpret a function of two variables as a surface and read its level curves.
* 23.2 Compute first partial derivatives and state what each measures.
* 23.3 Compute higher-order and mixed partials and state the condition that permits interchange.
* 23.4 Write the total differential of a function of several variables.
* 23.5 Estimate propagated measurement uncertainty and identify the dominant input.
* 23.6 Apply the power-law uncertainty shortcut and recognize its first-order limits.
* 23.7 Write a tangent plane and use it as a local first-order Taylor approximation.
* 23.8 Apply the multivariable chain rule to a related-rates problem.
* 23.9 Compute a gradient and explain its direction and magnitude.
* 23.10 Compute a directional derivative using a unit vector.
* 23.11 Compute divergence and interpret its sign and units.
* 23.12 Compute curl, interpret local rotation, and state when zero curl implies a conservative field.
* 23.13 Locate and classify two-variable critical points and recognize an inconclusive test.
* 23.14 Set up and check a constrained optimization using Lagrange multipliers.

---

## Notation Used Here

In the units below, $[f]$ means the units of the function's output and $[x]$ the
units of its input. A derivative has output units divided by input units. The
symbol $1$ means dimensionless; “operator” means that no standalone physical unit
is assigned. Cartesian spatial coordinates use the same length unit on every axis.

| Symbol | Meaning in this chapter | SI | USCS |
|---|---|---|---|
| $x,y,z$; $a,b$ | coordinates or named inputs; $a,b$ also identify an expansion point | m for spatial coordinates; otherwise stated | ft or in for spatial coordinates; otherwise stated |
| $f,g$; $f_0$ | scalar functions; nominal output $f_0$ | problem-dependent | problem-dependent |
| $f_x,f_y,f_{xx},f_{xy}$ | first and second partial derivatives | $[f]/[x]$, $[f]/[x]^2$, $[f]/([x][y])$ as appropriate | same dimensional ratios |
| $\partial,\nabla$ | partial-derivative and del operators | operator | operator |
| $dx,dy,df$; $\Delta x,\Delta f$ | differential increments; finite changes | corresponding input or output unit | corresponding input or output unit |
| $\varepsilon_x,\varepsilon_f^{(1)}$ | nonnegative input tolerance; first-order output uncertainty estimate | corresponding input or output unit | corresponding input or output unit |
| $\nabla f,D_{\mathbf u}f$ | gradient and derivative in a unit direction | $[f]/\mathrm{m}$ for spatial inputs | $[f]/\mathrm{ft}$ for spatial inputs |
| $\mathbf u,\hat{\imath},\hat{\jmath},\hat{k}$ | unit direction and Cartesian basis vectors | 1 | 1 |
| $\mathbf F,\mathbf v$; $F_x,F_y,F_z$ | vector field, velocity field, and scalar components | field-dependent; velocity m/s | field-dependent; velocity ft/s |
| $\nabla\cdot\mathbf F,\nabla\times\mathbf F$ | divergence and curl | $[\mathbf F]/\mathrm{m}$ | $[\mathbf F]/\mathrm{ft}$ |
| $\Psi$ | scalar potential satisfying $\mathbf F=\nabla\Psi$ | $[\mathbf F]\,\mathrm{m}$ | $[\mathbf F]\,\mathrm{ft}$ |
| $D$ | second-partial discriminant $f_{xx}f_{yy}-f_{xy}^2$ | $[f]^2/([x]^2[y]^2)$ | same dimensional ratio |
| $\lambda_L,c_0$ | Lagrange multiplier; fixed value in $g=c_0$ | $[f]/[g]$; $[g]$ | same dimensional ratios |
| $r,h,d_p,L$ | radius, height, pipe diameter, and length | m or mm | ft or in |
| $A,V,Q_v$ | area, volume, and volumetric flow rate | m², m³, m³/s | ft², ft³, ft³/s |
| $P_w,U_V,R_e,I_e$ | electrical power, voltage, resistance, current in supplied models | W, V, Ω, A | W, V, Ω, A |
| $t$ | time | s | s |
| $T,\mathbf q,k$ | temperature, heat flux, positive thermal conductivity in a supplied model | K or °C; W/m²; W/(m·K) | °F; Btu/(h·ft²); Btu/(h·ft·°F) |
| $F_L,E,I_A,\delta$ | load, elastic modulus, second moment of area, beam deflection in a supplied model | N, Pa, m⁴, m | lbf, psi, in⁴, in when inch units are used |
| $\theta$ | angle between directions | rad | rad |
| $C,p,q,s$ | fixed coefficient and exponents in a product of powers | coefficient units make the model consistent; exponents 1 | same rule |

> **Collision note.** $D$ is the second-partial discriminant, not a diameter,
> determinant, or diffusivity. Pipe diameter is $d_p$. The local multiplier is
> $\lambda_L$; a reference may print $\lambda$ for the same quantity. Volume is
> $V$, power is $P_w$, flow rate is $Q_v$, and the supplied circuit models use
> $U_V,R_e,I_e$ to avoid assigning several meanings to $V,R,I$. $E$ means elastic
> modulus and $I_A$ a second moment of area. $k$ means thermal conductivity;
> $\hat{k}$ is a unit vector. See the [Notation Contract](../meta/notation.md).

> ---
> **Mentor's Margin**
>
> The curly $\partial$ is not decoration. It tells you that the other independent
> inputs are frozen. An ordinary $d$ describes a total change along the path the
> inputs actually follow. Before you differentiate, say aloud which question you
> are answering.
>
> Keep the output types straight, too: a gradient is a **vector**, divergence a
> **scalar**, and curl a **vector**. The dot and cross symbols preserve the output
> types you learned in Chapter 01-13. Check the type before checking the arithmetic.
>
> ---

---

## 23.1 Functions of Several Variables

A **function of several variables** assigns one output to each allowed combination
of inputs. Its domain is the set of allowed combinations. For example,
$f(x,y)=\ln(x^2+y)$ requires $x^2+y>0$; not every pair is admissible.
This is the [domain idea from 01-06](01-06-Functions-Graphs-and-Transformations.md)
with an extra input.

The graph of $z=f(x,y)$ is a **surface**. For $f(x,y)=x^2+y^2$, it is an
upward-opening bowl. When the inputs are position coordinates and the output is
one number at each position, we call the function a **scalar field**. Temperature
in a room is one example: each location has one temperature.

A **level curve**, also called a **contour**, joins the points where the function
has one fixed value. Setting $x^2+y^2=c_0$ gives a circle of radius $\sqrt{c_0}$
when $c_0>0$. At $c_0=0$ the level set is just the origin; negative levels do not
occur for this bowl.

For levels $1,2,3,4$, the radii are $1,\sqrt2,\sqrt3,2$. The outward gaps shrink
because the bowl gets steeper as you move outward. **Compare contour spacing only
when the change in the labeled value is the same.** Levels $1,4,9,16$ would instead
give equally spaced radii $1,2,3,4$; their unequal height increments prevent the
same spacing comparison.

A contour map is a compact way to read a surface. Closely spaced **equal-increment**
contours indicate a larger rate of change across them. Moving along one contour
leaves the output unchanged. We will turn those observations into calculations
in §23.5.

![FIG-01-23-001: Two panels show the dimensionless surface z=x²+y² and its contour map. The surface is cut by four horizontal planes at z=1,2,3,4. The matching map has four circles of radii 1, √2, √3, and 2 labeled with those levels. The equal height increments produce progressively smaller outward radial gaps, illustrating increasing steepness. Line styles and labels distinguish the levels without relying on color.](../figures/FIG-01-23-001-surface-and-contours.png)

---

## 23.2 Partial Derivatives

The new discipline is choosing which input is allowed to move.

To find $\dfrac{\partial f}{\partial x}$: treat $y$ as a **constant** and
differentiate with respect to $x$ using every rule from Chapter 01-17.

To find $\dfrac{\partial f}{\partial y}$: treat $x$ as a constant and differentiate
with respect to $y$.

The product rule, quotient rule, chain rule, and every entry in
the derivative table apply unchanged. The only discipline required is remembering
which letter is frozen.

The limit definition from [01-17 The Derivative](01-17-The-Derivative.md)
makes the instruction precise:

$$f_x(a,b)=\lim_{\Delta x\to0}\frac{f(a+\Delta x,b)-f(a,b)}{\Delta x}.$$

Only the first input changes. Interchange the roles of the inputs to define
$f_y(a,b)$. The usual limit must exist for that partial derivative to exist.

### What a partial derivative measures

Geometrically, $f_x$ at a point is the slope of the surface in the
$x$-direction — the slope of the curve you get by slicing the surface with a
vertical plane holding $y$ constant. Similarly $f_y$ is the slope along a slice
holding $x$ constant.

Physically, $f_x$ is the **sensitivity** of the output to that one input. If a flow model has $\partial Q_v/\partial d_p=0.57\ \mathrm{m^2/s}$,
a small diameter increase of $0.001\ \mathrm m$ produces an estimated flow
increase of $0.00057\ \mathrm{m^3/s}$, with the other inputs held fixed. That sensitivity reading is what makes partial derivatives an
engineering tool rather than a formality.

![FIG-01-23-002: A surface z = f(x,y) drawn in three dimensions with a point P marked on it. Two vertical cutting planes pass through P: one holding y constant, producing a trace curve on the surface with a tangent line drawn along it labeled "slope = ∂f/∂x"; the other holding x constant, producing a second trace curve with a tangent line labeled "slope = ∂f/∂y". The two tangent lines are shown meeting at P, and a dashed parallelogram through them indicates the tangent plane they span.](../figures/FIG-01-23-002-partial-derivative-slices.png)

### Worked Example 1 — First Partials

**Given.** $f(x,y) = x^2 y + 3xy^3 - 2y$

**Find.** $f_x$ and $f_y$, and evaluate both at $(2, 1)$.

**Approach.** Freeze one input at a time, differentiate each term, then substitute the point. Check with small coordinate changes.

**Solution.**

**1. For $f_x$**, treat $y$ as a constant. Then $x^2y$ differentiates to $2xy$ (the
$y$ rides along as a coefficient), $3xy^3$ differentiates to $3y^3$, and $-2y$ is a
constant so it vanishes:

$$f_x = 2xy + 3y^3$$

**2. For $f_y$**, treat $x$ as a constant. Now $x^2y$ differentiates to $x^2$, $3xy^3$
differentiates to $9xy^2$, and $-2y$ differentiates to $-2$:

$$f_y = x^2 + 9xy^2 - 2$$

**3. At $(2,1)$:**

$$f_x = 2(2)(1) + 3(1)^3 = 4 + 3 = \boxed{7}$$
$$f_y = (2)^2 + 9(2)(1)^2 - 2 = 4 + 18 - 2 = \boxed{20}$$

**Interpretation.** At the point $(2,1)$ the surface is nearly three times steeper
in the $y$-direction than in the $x$-direction. These are **local rates**.
For a sufficiently small increment, $\Delta f\approx20\Delta y$ with $x$ fixed,
or $\Delta f\approx7\Delta x$ with $y$ fixed. A whole-unit step need not be small.

**Check.** With $y=1$, $f(2.001,1)-f(2,1)=0.007001$,
close to $7(0.001)=0.007$. With $x=2$,
$f(2,1.001)-f(2,1)=0.020018006$, close to $20(0.001)=0.020$.
These finite changes check the local slopes without claiming exact equality.


### Worked Example 2 — Product and Chain Rules Still Apply

**Given.** $f(x,y) = x^3y^2 + e^{xy}$

**Find.** $f_x$ and $f_y$.

**Approach.** Use the power rule on the polynomial and the single-variable chain rule on the exponential, holding the other input fixed.

**Solution.**

**1. $f_x$**, with $y$ frozen. The second term needs the chain rule: the inner
function is $xy$, whose derivative with respect to $x$ is $y$:

$$f_x = 3x^2y^2 + y\,e^{xy}$$

**2. $f_y$**, with $x$ frozen. Now the inner derivative is $x$:

$$f_y = 2x^3y + x\,e^{xy}$$

Note how the frozen variable appears as the chain factor. That is the most common
place to slip: differentiating $e^{xy}$ with respect to $x$ gives $y e^{xy}$, not
$e^{xy}$ and not $xe^{xy}$.

**Check.** At $y=0$, the function is the constant 1 as $x$ varies,
so $f_x(x,0)=0$, which the formula gives. At $x=0$, it is the constant
1 as $y$ varies, and the formula gives $f_y(0,y)=0$ as required.


### Higher-order and mixed partials

Differentiate twice. There are four second partials for a function of two
variables:

$$f_{xx} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) \qquad f_{yy} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right)$$

$$f_{xy} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) \qquad f_{yx} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)$$

The last two are the **mixed partials**, and there is a theorem about them:

> **Equality of mixed partials.** If the second partials are continuous in a neighborhood of the point, then
> $$\boxed{f_{xy} = f_{yx}}$$

Under that condition, the order of differentiation does not matter. There is no
reason on inspection why differentiating in $x$ then $y$ should agree with $y$ then
$x$ — and it is enormously convenient. It also gives you a free check: compute both
and confirm they agree.

### Worked Example 3 — Mixed Partials Agree

**Given.** $f(x,y) = x^3y^2 + e^{xy}$, continuing Worked Example 2.

**Find.** Both mixed partials and determine whether they agree.

**Approach.** Differentiate each first partial in the other variable. Use the product rule on the variable multiplying the exponential.

**Solution.**

**1. Differentiate $f_x$ in $y$.** From Worked Example 2, $f_x = 3x^2y^2 + ye^{xy}$. Differentiate with respect to
$y$, using the product rule on the second term:

$$f_{xy} = 6x^2y + \left[e^{xy} + y\cdot xe^{xy}\right] = 6x^2y + e^{xy}(1 + xy)$$

**2. Differentiate $f_y$ in $x$.** And $f_y = 2x^3y + xe^{xy}$. Differentiate with respect to $x$:

$$f_{yx} = 6x^2y + \left[e^{xy} + x\cdot ye^{xy}\right] = 6x^2y + e^{xy}(1 + xy)$$

$$\boxed{f_{xy} = f_{yx} \;\checkmark}$$

Here the polynomial and exponential terms have continuous derivatives
everywhere, so the theorem applies. If the formulas disagree in this example,
check the algebra. For a piecewise or singular function, check the continuity
condition before assuming the partials must agree.

**Check.** Both independent routes give the same expression.
At $(0,0)$, each evaluates to 1; the polynomial contributions vanish and
the product-rule derivative of the exponential contribution remains.

---


## 23.3 The Total Differential and Error Propagation

Apprentice, this is where a collection of derivatives becomes a decision about
measurements. Each input has a sensitivity and a possible change. Multiplying
those two quantities puts every contribution into the output's units.

### The total differential

Assume $f$ is differentiable near the nominal inputs. Continuous first partials
in a neighborhood are a sufficient condition. Merely having two partials at one
point is not enough to guarantee a tangent plane.

The [single-variable linearization from 01-18](01-18-Applications-of-the-Derivative.md)
uses sensitivity times a small input change. For two inputs, change the first
while holding the second fixed, then change the second. To first order the
contributions add:

$$\Delta f\approx f_x(a,b)\Delta x+f_y(a,b)\Delta y.$$

The linear expression on the right defines the **total differential**:

$$\boxed{df=f_x\,dx+f_y\,dy+f_z\,dz+\cdots.}$$

Evaluate the partials at the nominal point. The equation defining $df$ is exact;
using $df$ to estimate the finite change $\Delta f$ is an approximation.

### Tangent plane and the first-order Taylor polynomial

At $(a,b)$, the **tangent plane** has the correct height and the correct slope in
each coordinate direction:

$$\boxed{z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b).}$$

Compare this with the degree-1 Taylor polynomial in
[01-22 Infinite Series and Taylor Expansions](01-22-Infinite-Series-and-Taylor-Expansions.md).
There is now one first-order term per input. If the second partials remain bounded
near the point, the neglected terms are at most of second order in a small
displacement. For two dimensionless inputs, with continuous second partials, the leading omitted expression (evaluated at the base point) is

$$\frac12\left[f_{xx}(\Delta x)^2+2f_{xy}\Delta x\Delta y+f_{yy}(\Delta y)^2\right].$$

This explains the locality warning: doubling a small step generally makes its
leading quadratic error four times as large. Some directions or functions have
cancellations, and a function consisting only of a constant and linear terms has zero error. “Second order” does not mean
that every error is exactly proportional to distance squared.

![FIG-01-23-003: A smooth curved surface and its tangent plane meet at a marked point P. The plane matches the surface closely near P and separates farther away. Horizontal input increments Δx and Δy identify a nearby point; the plane's output change df is distinguished from the true surface change Δf. A vertical bracket marks the approximation error, described as second order for bounded second partials and sufficiently small steps.](../figures/FIG-01-23-003-tangent-plane.png)

### Worked Example 4 — A Tangent Plane You Can Check

**Given.** The dimensionless surface $f(x,y)=x^2+xy+y^2$ near $(1,2)$.

**Find.** Its tangent plane and an estimate of $f(1.02,1.97)$.

**Approach.** Evaluate the output and both slopes at the base point. Apply the
small input changes to those slopes, then compare with direct substitution.

**Solution.**

1. Evaluate the base value and slopes:

   $$f(1,2)=7,\qquad f_x=2x+y=4,\qquad f_y=x+2y=5.$$

2. Write the plane using those fixed slopes:

   $$z=7+4(x-1)+5(y-2).$$

3. Insert $\Delta x=0.02$ and $\Delta y=-0.03$:

   $$df=4(0.02)+5(-0.03)=-0.07,\qquad \boxed{f(1.02,1.97)\approx6.93.}$$

**Check.** Direct substitution gives $1.0404+2.0094+3.8809=6.9307$.
The error is $0.0007$, exactly the omitted quadratic contribution
$(0.02)^2+(0.02)(-0.03)+(-0.03)^2$. The decrease has the expected sign: the
negative $y$ contribution exceeds the positive $x$ contribution.

### Error propagation

Use the [measurement-error idea from 01-18](01-18-Applications-of-the-Derivative.md)
with several inputs. Let $\varepsilon_x,\varepsilon_y$ be nonnegative bounds on
the input deviations: $|dx|\le\varepsilon_x$ and $|dy|\le\varepsilon_y$.
The triangle inequality gives a bound for the **linearized** output change:

$$|df|\le |f_x|\varepsilon_x+|f_y|\varepsilon_y+\cdots.$$

Define the first-order uncertainty estimate by

$$\boxed{\varepsilon_f^{(1)}=\sum_i\left|\frac{\partial f}{\partial x_i}\right|\varepsilon_{x_i}.}$$

It assumes the input deviations can combine in the most unfavorable direction.
No probability distribution is assumed. For a nonlinear function this is **not
automatically a rigorous bound on the finite error**: the derivatives vary over
the tolerance range and the neglected terms may increase the true deviation.
If a guaranteed tolerance is required, evaluate attainable extremes or bound the
derivatives over the entire allowed input range.

Each summand has output units and estimates that input's contribution. Divide it
by $\varepsilon_f^{(1)}$ to obtain its share. This is how you decide which
measurement improvement would help most.

### The power-law shortcut

Assume the inputs are nonzero, remain in a domain where the real powers are
differentiable, and have small relative uncertainties. Let the coefficient be
exact in the supplied model:

$$f=Cx^py^qz^s.$$

Differentiate with respect to one input at a time and divide by $f$:

$$\frac{f_x}{f}=\frac{p}{x},\qquad
\frac{f_y}{f}=\frac{q}{y},\qquad
\frac{f_z}{f}=\frac{s}{z}.$$

Substitution into the differential gives

$$\frac{df}{f}=p\frac{dx}{x}+q\frac{dy}{y}+s\frac{dz}{z}.$$

Take magnitudes for the uncertainty estimate:

$$\boxed{\frac{\varepsilon_f^{(1)}}{|f_0|}
=|p|\frac{\varepsilon_x}{|x|}+|q|\frac{\varepsilon_y}{|y|}
+|s|\frac{\varepsilon_z}{|z|}.}$$

An exponent of 2 doubles that input's relative contribution; an exponent of
$-1$ has the same uncertainty weight as $+1$. The signs still matter for a
known directional change. If the coefficient $C$ also has uncertainty, add its
relative contribution. Do not use the shortcut across zero or outside the model's domain.

### Worked Example 5 — Volume of a Cylinder

**Given.** $r=25.0\pm0.3\ \mathrm{mm}$ and $h=80.0\pm0.5\ \mathrm{mm}$.
Use $V=\pi r^2h$; the stated input tolerances may vary independently.

**Find.** The volume, its first-order uncertainty estimate, and the dominant input.

**Approach.** Compute nominal volume, form each absolute sensitivity contribution,
and compare with the power-law shortcut. Check the finite upper endpoint.

**Solution.**

1. Compute the nominal volume:

   $$V_0=\pi(25.0\ \mathrm{mm})^2(80.0\ \mathrm{mm})
   =157079.63\ \mathrm{mm^3}.$$

2. Compute the partials and their tolerance contributions:

   $$V_r=2\pi rh=12566.37\ \mathrm{mm^2},\qquad
   V_h=\pi r^2=1963.50\ \mathrm{mm^2},$$

   $$\varepsilon_V^{(1)}=(12566.37\ \mathrm{mm^2})(0.3\ \mathrm{mm})
   +(1963.50\ \mathrm{mm^2})(0.5\ \mathrm{mm})
   =4751.66\ \mathrm{mm^3}.$$

3. Verify the relative estimate using the exponents:

   $$\frac{\varepsilon_V^{(1)}}{V_0}=2\frac{0.3}{25.0}+\frac{0.5}{80.0}
   =0.03025=3.025\%.$$

   Report the approximate first-order result as
   $\boxed{V\approx(157100\pm4800)\ \mathrm{mm^3}}$.

| Input | Relative tolerance | Weighted contribution | Share of linearized total |
|---|---|---|---|
| Radius | 1.20% | 2.40% | 79.3% |
| Height | 0.625% | 0.625% | 20.7% |

The radius measurement is less precise in relative terms and has twice the
exponent. Halving its tolerance reduces the estimate to
$1.20\%+0.625\%=1.825\%$. A perfect height measurement alone leaves 2.40%.
Improve the radius first if the measurement cost is comparable.

**Check.** The exact upper endpoint is $\pi(25.3)^2(80.5)$, which is **3.05449%**
above nominal. This is slightly larger than 3.025%, as the positive higher-order
terms predict. The differential estimate is useful, but the endpoint calculation
is the stronger tolerance check.

### Worked Example 6 — Flow Rate from Diameter and Velocity

**Given.** The supplied flow model is $Q_v=(\pi d_p^2/4)v$, with
$d_p=150\pm1\ \mathrm{mm}$ and average speed $v=2.40\pm0.05\ \mathrm{m/s}$.

**Find.** The flow rate, first-order uncertainty, and each input's contribution.

**Approach.** Convert diameter to metres before computing flow. Weight its
relative tolerance by 2 and the speed's by 1.

**Solution.**

1. Compute nominal flow:

   $$Q_{v,0}=\frac{\pi(0.150\ \mathrm m)^2}{4}(2.40\ \mathrm{m/s})
   =0.0424115\ \mathrm{m^3/s}=42.4115\ \mathrm{L/s}.$$

2. Compute relative and absolute first-order uncertainty:

   $$\frac{\varepsilon_{Q_v}^{(1)}}{Q_{v,0}}
   =2\frac{1}{150}+\frac{0.05}{2.40}
   =0.0341667=3.41667\%,$$

   $$\varepsilon_{Q_v}^{(1)}=1.4491\ \mathrm{L/s},\qquad
   \boxed{Q_v\approx(42.4\pm1.4)\ \mathrm{L/s}.}$$

3. Compare the weighted contributions: diameter contributes 1.33333 percentage
   points, or 39.0% of the total; speed contributes 2.08333 points, or 61.0%.

Here speed dominates even though diameter is squared. The exponent and the
measurement quality must both be included.

**Check.** Area times speed has units $\mathrm{m^2}\,\mathrm{m/s}
=\mathrm{m^3/s}$. The direct upper endpoint, using $0.151\ \mathrm m$ and
$2.45\ \mathrm{m/s}$, is 3.44898% above nominal, close to and slightly above
the first-order estimate.

> ---
> **Mentor's Margin**
>
> “Worst case” needs a qualifier here: worst case **for the first-order model**.
> A nominal slope does not know how much the slope changes farther away. If the
> tolerance is large, the model is strongly curved, or the nominal derivative
> vanishes, check the finite range directly.
>
> For example, $f(x)=x^2$ has zero derivative at zero. A first-order calculation
> predicts zero change there, yet an input error of size $\varepsilon_x$ can
> produce an output change of $\varepsilon_x^2$. The missing effect is second order.
>
> Statistical uncertainty is a different question. A stated tolerance is not
> automatically a standard deviation, and averaging assumptions do not belong in
> this calculation unless the problem supplies them.
>
> ---

---

## 23.4 The Multivariable Chain Rule

Suppose several inputs change with time. Each contributes its own rate to the
output, and those contributions can oppose one another. Keep the signs.

Assume $f$ is differentiable in its inputs and the inputs are differentiable
functions of time. Divide the small-change relation by $\Delta t$ and take the
limit. Each input change per unit time becomes its derivative:

$$\boxed{\frac{df}{dt}=
\frac{\partial f}{\partial x}\frac{dx}{dt}
+\frac{\partial f}{\partial y}\frac{dy}{dt}
+\frac{\partial f}{\partial z}\frac{dz}{dt}.}$$

This **multivariable chain rule** extends the related-rates method from
[01-18 Applications of the Derivative](01-18-Applications-of-the-Derivative.md).
The left side uses ordinary $d$ because the path has one independent variable,
$t$. The partials on the right describe separate input sensitivities.
If the model also depends explicitly on time, add $\partial f/\partial t$.

### Worked Example 7 — Competing Rates

**Given.** A supplied resistor model is $P_w=U_V^2/R_e$. At one instant,
$U_V=12.0\ \mathrm V$, $dU_V/dt=0.15\ \mathrm{V/s}$,
$R_e=48.0\ \Omega$, and $dR_e/dt=0.60\ \Omega/\mathrm s$.

**Find.** The instantaneous power rate.

**Approach.** Differentiate with respect to each input, multiply by that input's
signed time rate, and add. Increasing resistance lowers power at fixed voltage.

**Solution.**

1. Evaluate the two sensitivities:

   $$\frac{\partial P_w}{\partial U_V}=\frac{2U_V}{R_e}
   =0.500\ \mathrm{W/V},\qquad
   \frac{\partial P_w}{\partial R_e}=-\frac{U_V^2}{R_e^2}
   =-0.0625\ \mathrm{W}/\Omega.$$

2. Combine the rates:

   $$\frac{dP_w}{dt}=(0.500\ \mathrm{W/V})(0.15\ \mathrm{V/s})
   +(-0.0625\ \mathrm{W}/\Omega)(0.60\ \Omega/\mathrm s)
   =\boxed{+0.0375\ \mathrm{W/s}}.$$

Voltage contributes $+0.0750\ \mathrm{W/s}$; resistance contributes
$-0.0375\ \mathrm{W/s}$. The net power is increasing.

**Check.** Nominal power is $3.00\ \mathrm W$. The signed relative-rate form gives

$$\frac{1}{P_w}\frac{dP_w}{dt}
=2\frac{0.15}{12.0}-\frac{0.60}{48.0}
=0.0125\ \mathrm{s^{-1}},$$

and $(3.00\ \mathrm W)(0.0125\ \mathrm{s^{-1}})=0.0375\ \mathrm{W/s}$.
Taking absolute values would instead give $0.1125\ \mathrm{W/s}$, which answers
the wrong question.

---

## 23.5 The Gradient and Directional Derivatives

### The gradient

A temperature map tells you the uphill slope in each coordinate direction.
To combine those slopes into one directional instruction, collect the partials
into a vector. The **del operator**, $\nabla$, is the shorthand vector of
Cartesian differentiation operators:

$$\nabla=\left\langle\frac{\partial}{\partial x},
\frac{\partial}{\partial y},\frac{\partial}{\partial z}\right\rangle.$$

Applied to a differentiable scalar field, it produces the **gradient**:

$$\boxed{\nabla f = \frac{\partial f}{\partial x}\hat{\imath} + \frac{\partial f}{\partial y}\hat{\jmath} + \frac{\partial f}{\partial z}\hat{k}}$$

Where the gradient is nonzero, it has two properties:

**1. It points in the direction of steepest increase.** Of all the directions you
could move from a point, $\nabla f$ is the one along which $f$ grows fastest.

**2. Its magnitude is that maximum rate.** $\lvert\nabla f\rvert$ is the slope in
the steepest direction. No direction gives a larger rate of change.

To justify both statements, use the
[dot product from 01-13](01-13-Vectors-and-Vector-Operations.md).
A small displacement of length $d\ell$ in a unit direction $\mathbf u$ has
coordinate increments $\mathbf u\,d\ell$. Substituting into $df$ gives
$df=(\nabla f\cdot\mathbf u)d\ell$.
The dot product is $|\nabla f|\cos\theta$; its largest value occurs at $\theta=0$.

The gradient is also **perpendicular to a regular level curve**. Along such a
curve, $df=0$, so its tangent direction has zero dot product with $\nabla f$.
This proves perpendicularity where the gradient is nonzero. Compare slopes by
contour spacing only when the contour value increments are equal.

If $\nabla f=\mathbf0$, every first-order directional derivative is zero.
There is then no unique steepest first-order direction. Higher-order behavior
still matters, as the bowl and saddle examples in §23.7 will show.

![FIG-01-23-004: A contour map of a scalar field with five nested irregular closed contours labeled with equally spaced increasing values, tightly spaced on the left side and widely spaced on the right. At six points around the map, gradient vectors are drawn as arrows, each perpendicular to the local contour and pointing toward the higher-valued contour. The arrows on the tightly spaced left side are drawn long and labeled "large |∇f| — steep"; those on the widely spaced right side are drawn short and labeled "small |∇f| — gentle". A note reads "gradient ⊥ contours, pointing uphill".](../figures/FIG-01-23-004-gradient-contours.png)

### Why engineers care

Here is a supplied engineering model, with the physical quantities defined so
that no heat-transfer prerequisite is needed. Let $T$ be temperature,
$\mathbf q$ the heat crossing a unit area per unit time, and $k>0$ a constant
thermal conductivity. In a material with the same conductivity in every direction,
Fourier's conduction model is

$$\mathbf q=-k\nabla T.$$

The gradient points toward higher temperature. The minus sign makes the modeled
heat flux point toward lower temperature. With $\nabla T$ in $\mathrm{K/m}$ and
$k$ in $\mathrm{W/(m\cdot K)}$, the flux has units $\mathrm{W/m^2}$.
A temperature difference of $1\ \mathrm K$ equals a difference of $1\,^\circ\mathrm C$.

The mathematics is the lesson here: a vector made from local sensitivities can
describe both a direction and a rate. The physical validity and limitations of a
particular transport model must be established separately.

---

### Directional derivatives

To find the rate of change in an arbitrary direction, project the gradient onto
that direction using the dot product from [01-13 Vectors and Vector Operations](01-13-Vectors-and-Vector-Operations.md):

$$\boxed{D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u} \qquad \text{where } \lvert\mathbf{u}\rvert = 1}$$

The unit requirement is not optional. If $\mathbf{u}$ is not normalized, the answer
is scaled by $\lvert\mathbf{u}\rvert$ and is not the rate per unit distance.

Since $\nabla f\cdot\mathbf{u} = \lvert\nabla f\rvert\cos\theta$, the directional
derivative ranges from $+\lvert\nabla f\rvert$ (straight uphill) through zero
(along a contour) to $-\lvert\nabla f\rvert$ (straight downhill). That gives you a
free check: **any directional derivative must have magnitude no greater than
$\lvert\nabla f\rvert$.**

### Worked Example 8 — Gradient and Directional Derivative

**Given.** $f(x,y) = x^2 + 3xy - y^2$ at the point $(1, 2)$.

**Find.** (a) $\nabla f$, (b) the maximum rate of increase and its direction,
(c) the rate of change toward the point $(4, 6)$.

**Approach.** Compute the gradient first. Its magnitude gives the maximum rate; normalize the displacement before taking the requested dot product.

**Solution.**

**1. Gradient.**

$$f_x = 2x + 3y \implies f_x(1,2) = 2 + 6 = 8$$
$$f_y = 3x - 2y \implies f_y(1,2) = 3 - 4 = -1$$

$$\boxed{\nabla f = 8\hat{\imath} - \hat{\jmath}}$$

**2. Maximum rate and direction.**

$$\lvert\nabla f\rvert = \sqrt{64 + 1} = \sqrt{65} = \boxed{8.06}$$

Direction, as a unit vector:

$$\hat{\mathbf{u}}_{\max} = \frac{8\hat{\imath} - \hat{\jmath}}{8.062} = \boxed{0.992\hat{\imath} - 0.124\hat{\jmath}}$$

Almost due $+x$, tilted slightly toward $-y$.

**3. Requested direction.** The direction from $(1,2)$ to $(4,6)$ is $\langle 3, 4\rangle$, with
magnitude $\sqrt{9+16} = 5$. Normalize:

$$\mathbf{u} = \left\langle 0.600,\; 0.800\right\rangle$$

$$D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u} = 8(0.600) + (-1)(0.800) = 4.80 - 0.80 = \boxed{4.00}$$

**Check.** $4.00 \le 8.06$ ✓ The directional derivative cannot exceed the gradient
magnitude, and it does not.

**Interpretation.** Moving toward $(4,6)$ gains height at rate 4.00 per unit
distance — about half the best available rate of 8.06, because that direction is
roughly $60°$ off the steepest line. Confirm:
$\cos^{-1}(4.00/8.06) = \cos^{-1}(0.496) = 60.3°$ ✓

---

## 23.6 Divergence and Curl

A **vector field** assigns a vector to each position: a velocity arrow at every
point in a moving fluid is one example. Its components are ordinary scalar
functions. Write

$$\mathbf{F} = F_x\hat{\imath} + F_y\hat{\jmath} + F_z\hat{k}$$

### Divergence — a scalar

$$\boxed{\nabla\cdot\mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}}$$

Divergence measures local **net outward flux per unit volume**. Here flux means
the field component normal to a face, multiplied by that face's area. For velocity,
that product is a volume flow rate.

Picture a small box with side lengths $\Delta x,\Delta y,\Delta z$. The difference
between the right-face and left-face contributions is approximately
$(\partial F_x/\partial x)\Delta x\Delta y\Delta z$. The other two pairs of
faces contribute the corresponding $y$ and $z$ terms. Divide by box volume and
shrink the box: their sum is the divergence.

Field-line sketches illustrate direction, but counting drawn arrows is not a
quantitative flux calculation. The components and their changes determine the result.

| Divergence | Meaning |
|---|---|
| $\nabla\cdot\mathbf{F} > 0$ | **source** — field spreading out from the point |
| $\nabla\cdot\mathbf{F} < 0$ | **sink** — field converging on the point |
| $\nabla\cdot\mathbf{F} = 0$ | **solenoidal** — whatever enters, leaves |

For a velocity field, divergence has units $\mathrm{s^{-1}}$.
Zero divergence means no local volumetric expansion or contraction. For a
constant-density fluid with no mass sources, this is the incompressible
mass-conservation condition. Zero divergence alone is not a complete statement
about mass accumulation when density varies.

### Curl — a vector

$$\boxed{\nabla\times\mathbf{F} = \begin{vmatrix}\hat{\imath} & \hat{\jmath} & \hat{k}\\[1mm] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z}\\[2mm] F_x & F_y & F_z\end{vmatrix}}$$

Expanded, using the determinant machinery from [01-14 Matrices, Determinants, and Eigenvalues](01-14-Matrices-Determinants-and-Eigenvalues.md) and the cross-product
structure from [01-13 Vectors and Vector Operations](01-13-Vectors-and-Vector-Operations.md):

$$\nabla\times\mathbf{F} = \left(\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}\right)\hat{\imath} + \left(\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}\right)\hat{\jmath} + \left(\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\right)\hat{k}$$

Curl measures **local rotation**. Drop a tiny paddle wheel into the field: if it
spins, the curl is nonzero, and the curl vector points along the spin axis by the
right-hand rule.

For a velocity field, curl also has units $\mathrm{s^{-1}}$ and measures twice
the local rigid-body angular-velocity vector. For example, the planar velocity
field $\mathbf v=\langle-y,x,0\rangle\,\mathrm{s^{-1}}$, with coordinates in metres,
has curl $2\hat{k}\,\mathrm{s^{-1}}$, consistent with counterclockwise rotation
at $1\ \mathrm{rad/s}$ viewed from the positive $z$ side.

A field with zero curl is **irrotational**. A **conservative field** is one that
can be written $\mathbf F=\nabla\Psi$ for a single scalar function $\Psi$ throughout
its domain; $\Psi$ is a **scalar potential**.

These statements need conditions before you call them equivalent. If the field
has continuous first partials on an open **simply connected domain**, zero curl
implies that it is conservative. Simply connected means that every closed loop
can be continuously contracted to a point without leaving the domain. An ordinary
open ball qualifies; a plane with its center removed does not. A hole or an
excluded singularity can prevent a global potential even when curl vanishes
everywhere the field is defined.

In the other direction, a gradient field formed from a potential with continuous
second partials has zero curl: each component cancels a pair of equal mixed
partials. For instance, $\Psi=x^2y+z^2$ gives
$\nabla\Psi=\langle2xy,x^2,2z\rangle$, whose curl is zero everywhere. Its domain
is all of three-dimensional space, so there is no domain obstruction.

![FIG-01-23-005: Two-panel figure of field-line sketches with small test objects. Left panel titled "Divergence": three sub-sketches — arrows radiating outward from a point labeled "∇·F > 0, source", arrows converging inward labeled "∇·F < 0, sink", and uniform parallel arrows through a small dashed box with equal numbers entering and leaving labeled "∇·F = 0, solenoidal". Right panel titled "Curl": two sub-sketches — a shear field with arrows of increasing length, a small paddle wheel drawn in it shown rotating with a curved arrow and the curl vector drawn out of the page labeled "∇×F ≠ 0"; and a uniform field with an identical paddle wheel drawn stationary labeled "∇×F = 0, irrotational".](../figures/FIG-01-23-005-divergence-curl.png)

### Worked Example 9 — Computing Both

**Given.** $\mathbf{F} = 3x^2y\,\hat{\imath} - 2yz\,\hat{\jmath} + xz^2\,\hat{k}$

**Find.** $\nabla\cdot\mathbf{F}$ and $\nabla\times\mathbf{F}$, both evaluated at
$(1, 2, 1)$.

**Approach.** Differentiate matching components for divergence and cross components for curl. Evaluate only after forming the operator expressions.

**Solution.**

**1. Divergence.** Take each component's partial with respect to its own variable:

$$\frac{\partial}{\partial x}\left(3x^2y\right) = 6xy \qquad \frac{\partial}{\partial y}(-2yz) = -2z \qquad \frac{\partial}{\partial z}\left(xz^2\right) = 2xz$$

$$\nabla\cdot\mathbf{F} = 6xy - 2z + 2xz$$

At $(1,2,1)$: $6(1)(2) - 2(1) + 2(1)(1) = 12 - 2 + 2 = \boxed{12}$

Positive, so the point is a net source.

**2. Curl.** Work the three components in order.

$\hat{\imath}$: $\dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z}
= 0 - (-2y) = 2y$

$\hat{\jmath}$: $\dfrac{\partial F_x}{\partial z} - \dfrac{\partial F_z}{\partial x}
= 0 - z^2 = -z^2$

$\hat{k}$: $\dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y}
= 0 - 3x^2 = -3x^2$

$$\nabla\times\mathbf{F} = 2y\,\hat{\imath} - z^2\,\hat{\jmath} - 3x^2\,\hat{k}$$

At $(1,2,1)$:

$$\boxed{\nabla\times\mathbf{F} = 4\hat{\imath} - \hat{\jmath} - 3\hat{k}}$$

**Check.** Divergence came out a single number ✓ Curl came out a vector with
three components ✓ If either had the wrong type, the computation went wrong.

> ---
> **Mentor's Margin**
>
> The curl determinant is where errors live, and there are two of them.
>
> **The middle sign.** Expanding a $3\times3$ determinant along the top row carries
> the alternating pattern $+,-,+$ from Chapter 01-14. So the $\hat{\jmath}$
> component picks up a minus sign, which is why it reads
> $\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}$ — the
> reverse order from what the pattern of the other two components suggests. Write
> the determinant out rather than trying to recall the expanded form, and the sign
> takes care of itself.
>
> **Which partial pairs with which component.** Every term in the curl mixes
> *different* subscripts and variables: $\frac{\partial F_z}{\partial y}$, never
> $\frac{\partial F_z}{\partial z}$. The divergence is the opposite — it uses only
> matching pairs. If you find a matching pair inside a curl, or a mismatched pair
> inside a divergence, you have crossed the two operators.
>
> Practice locating the vector-operator formulas in your assigned reference.
> Compare its component order with your own before substituting values. A short
> lookup is useful only when you know what each entry means.
>
> ---

---

## 23.7 Optimization with Several Variables

### Critical points

At an interior local maximum or minimum of a differentiable function, the surface is level in
**every** direction, so every partial vanishes:

$$\boxed{f_x = 0 \quad\text{and}\quad f_y = 0}$$

Equivalently $\nabla f = \mathbf{0}$ — there is no uphill direction. Solve that
system for the stationary critical points. More generally, an interior point
where a first derivative fails to exist is also a candidate requiring direct
inspection. Boundary points require a separate check.

As in Chapter 01-18, a critical point need not be an extremum. But now there is a
new possibility that has no single-variable analogue: a **saddle point**, where the
surface rises in one direction and falls in another. A mountain pass is a saddle —
the lowest point along the ridge and the highest point along the trail.

### The second-derivative test

Assume the second partials are continuous near the stationary point. Form the
**second-partial discriminant**

$$\boxed{D = f_{xx}f_{yy} - \left(f_{xy}\right)^2}$$

evaluated at the critical point. Then:

| Condition | Conclusion |
|---|---|
| $D > 0$ and $f_{xx} > 0$ | local **minimum** |
| $D > 0$ and $f_{xx} < 0$ | local **maximum** |
| $D < 0$ | **saddle point** |
| $D = 0$ | test fails — investigate directly |

The second-order change near a stationary point is governed by
$f_{xx}(\Delta x)^2+2f_{xy}\Delta x\Delta y+f_{yy}(\Delta y)^2$.
When $f_{xx}\ne0$, completing the square rewrites this expression as

$$f_{xx}\left(\Delta x+\frac{f_{xy}}{f_{xx}}\Delta y\right)^2
+\frac{D}{f_{xx}}(\Delta y)^2.$$

If $D>0$, both squared terms have the sign of $f_{xx}$: upward change gives a
minimum and downward change a maximum. If $D<0$, directions of opposite change
exist, giving a saddle. The standard test also covers $f_{xx}=0$ when $D<0$.

When $D=0$, higher-order terms decide. At the origin, $x^4+y^4$ has a minimum,
$-x^4-y^4$ has a maximum, and $x^4-y^4$ has a saddle; all three give $D=0$.
Finding one path up and another down proves a saddle. Testing a few lines that
all go up does **not** prove a minimum over all possible approaches.

![FIG-01-23-006: Three three-dimensional surface sketches side by side, each with the critical point marked. Left, labeled "D > 0, f_xx > 0 — local minimum": a bowl opening upward with the point at the bottom, and two cross-section curves drawn through the point both curving upward. Centre, labeled "D > 0, f_xx < 0 — local maximum": a dome with the point at the top and both cross-sections curving downward. Right, labeled "D < 0 — saddle point": a saddle shape with one cross-section curving upward and the perpendicular one curving downward, annotated "curvatures disagree".](../figures/FIG-01-23-006-critical-point-classification.png)

### Worked Example 10 — Locating and Classifying

**Given.** $f(x,y) = x^3 + y^3 - 3xy$

**Find.** All critical points and classify each.

**Approach.** Solve both first-partial equations simultaneously, evaluate the second-partial discriminant at each solution, and test the saddle directly.

**Solution.**

**1. Critical points.**

$$f_x = 3x^2 - 3y = 0 \implies y = x^2$$
$$f_y = 3y^2 - 3x = 0 \implies x = y^2$$

Substitute the first into the second:

$$x = \left(x^2\right)^2 = x^4 \implies x^4 - x = 0 \implies x\left(x^3 - 1\right) = 0$$

So $x = 0$ or $x = 1$, giving $y = 0$ and $y = 1$ respectively.

$$\text{critical points: } (0,0) \text{ and } (1,1)$$

**2. Second partials.**

$$f_{xx} = 6x \qquad f_{yy} = 6y \qquad f_{xy} = -3$$

$$D = (6x)(6y) - (-3)^2 = 36xy - 9$$

**3. Classify.**

At $(0,0)$: $D = 0 - 9 = -9 < 0 \implies \boxed{\text{saddle point}}$

At $(1,1)$: $D = 36 - 9 = 27 > 0$ and $f_{xx} = 6 > 0 \implies
\boxed{\text{local minimum}}$, with

$$f(1,1) = 1 + 1 - 3 = -1$$

**Check the saddle directly.** Along the line $y = x$ near the origin,
$f = 2x^3 - 3x^2$, which for small $x$ is dominated by $-3x^2 < 0$ — the function
decreases. Along the line $y = -x$, $f = x^3 - x^3 + 3x^2 = 3x^2 > 0$ — the
function increases. Down one way, up the other ✓ A saddle.

### Constrained optimization: Lagrange multipliers

A constraint restricts which moves are allowed. At the best feasible point, you
may be unable to improve the objective **along the constraint**, even though it
could improve if you were free to leave it.

Let the objective $f$ and constraint function $g$ have continuous first partials.
At a constrained optimum on the smooth curve $g(x,y)=c_0$, assume
$\nabla g\ne\mathbf0$. Then the **Lagrange multiplier** condition is

$$\boxed{\nabla f=\lambda_L\nabla g,\qquad g=c_0.}$$

To see why, move along the constraint in a unit tangent direction. The constraint
does not change, so that tangent is perpendicular to $\nabla g$. At an optimum
the objective's directional derivative along the same tangent is zero. Thus
$\nabla f$ is also normal to the constraint; the two gradients are parallel
(or $\nabla f=\mathbf0$), which introduces the scalar multiplier $\lambda_L$.

Solve the component equations **and** the constraint. The solutions are
candidates, not automatically minima or maxima. Compare objective values and
check allowed boundaries, endpoints, and points where $\nabla g=\mathbf0$.
The same method extends to three inputs with one smooth constraint surface.

The multiplier can have a useful sensitivity interpretation in later work.
Here the requested design variables are the answer; do not stop after finding
$\lambda_L$.

![FIG-01-23-007: Equal-increment level curves of an objective function are crossed by a heavier smooth constraint curve g=c₀. At a regular candidate optimum the constraint is tangent to a level curve and nonzero gradient arrows ∇f and ∇g are parallel, labeled ∇f=λ_L∇g. At a crossing elsewhere, a tangent arrow along the constraint shows a feasible direction in which the objective changes. The drawing illustrates a necessary condition; the candidate still needs classification.](../figures/FIG-01-23-007-lagrange-tangency.png)

---

### Worked Example 11 — Minimum-Material Tank

**Given.** A closed cylindrical tank must hold $2.00$ m³.

**Find.** The radius and height that minimize surface area, and the resulting area.

**Approach.** Write area as the objective and volume as the constraint. Solve their Lagrange equations, then verify both feasibility and minimality.

**Solution.**

**1. Objective and constraint.**

$$A = 2\pi r^2 + 2\pi rh \qquad \text{subject to} \qquad V = \pi r^2 h = 2.00\ \mathrm{m^3}$$

**2. Gradients.**

$$\nabla A = \left\langle 4\pi r + 2\pi h,\; 2\pi r\right\rangle \qquad \nabla V = \left\langle 2\pi rh,\; \pi r^2\right\rangle$$

**3. Set $\nabla A = \lambda_L\nabla V$.**

$$4\pi r + 2\pi h = \lambda_L(2\pi rh) \tag{1}$$
$$2\pi r = \lambda_L\left(\pi r^2\right) \tag{2}$$

From (2), cancelling $\pi r$ (valid since $r > 0$):

$$2 = \lambda_L r \implies \lambda_L = \frac{2}{r}$$

Substitute into (1):

$$4\pi r + 2\pi h = \frac{2}{r}(2\pi rh) = 4\pi h$$

$$4\pi r = 2\pi h \implies \boxed{h = 2r}$$

**The height equals the diameter.** That is the classic result, and it is worth
remembering: the most material-efficient closed cylinder is as tall as it is wide.

**4. Apply the constraint.**

$$\pi r^2(2r) = 2\pi r^3 = 2.00 \implies r^3 = \frac{1}{\pi} = 0.31831$$

$$r = 0.68278 \text{ m} \qquad h = 1.36556 \text{ m}$$

$$\boxed{r = 0.683\ \mathrm m,\quad h = 1.37\ \mathrm m}$$

**5. Surface area.** With $h=2r$,

$$A=6\pi r^2=6\pi(0.682784\ \mathrm m)^2
\approx8.78755\ \mathrm{m^2}\approx\boxed{8.79\ \mathrm{m^2}}.$$

**Check the constraint.** Using unrounded dimensions,
$\pi(0.6827840633\ \mathrm m)^2(1.3655681265\ \mathrm m)
\approx2.00000\ \mathrm{m^3}$, matching the required volume.

**Check that it is a minimum.** Eliminate $h$ using the fixed volume
$V_0=2.00\ \mathrm{m^3}$:

$$A(r)=2\pi r^2+\frac{2V_0}{r},\qquad
A'(r)=4\pi r-\frac{2V_0}{r^2},\qquad
A''(r)=4\pi+\frac{4V_0}{r^3}>0\quad(r>0).$$

The area tends to infinity as $r$ tends to zero or grows without bound. The
single stationary point is therefore the global minimum among positive-radius
closed cylinders of this volume. This check establishes the conclusion instead
of assuming that a Lagrange solution must be a minimum.

---

## As the Handbook States It

> **Source verification.** This guide's working edition is Handbook 10.6.
> Its PDF was not available for direct page verification during this revision.
> The formulas below are this chapter's reference forms, not asserted quotations
> or verified page transcriptions. Confirm their location and printed notation
> in the edition assigned to your exam. NCEES provides the Handbook through
> [MyNCEES](https://ncees.org/exams/fe-exam/).

Use the lookup method from
[00-03 Navigating the FE Reference Handbook](../layer-0-orientation/00-03-navigating-the-fe-reference-book.md):
search a distinctive term, identify the variables, and check the assumptions
before substituting values. Do not memorize an inferred page number.

| Search term | Form to recognize | What you must supply |
|---|---|---|
| Partial derivative | $f_x=\partial f/\partial x$ | which other inputs are fixed |
| Total differential | $df=f_xdx+f_ydy+f_zdz$ | nominal evaluation point and signed increments |
| Gradient | $\nabla f=\langle f_x,f_y,f_z\rangle$ | scalar input and consistent coordinate units |
| Directional derivative | $D_{\mathbf u}f=\nabla f\cdot\mathbf u$ | a unit direction vector |
| Divergence | $\nabla\cdot\mathbf F=(F_x)_x+(F_y)_y+(F_z)_z$ | matching component and differentiation variable |
| Curl | determinant with basis vectors, derivative operators, and field components | component order and the middle minus sign |
| Two-variable extrema | $D=f_{xx}f_{yy}-f_{xy}^2$ | a stationary point and the sign of $f_{xx}$ |
| Lagrange multipliers | $\nabla f=\lambda\nabla g$ with $g=c_0$ | the constraint, allowed domain, and candidate checks |

**Notation translation.** This chapter prints $\lambda_L$ to distinguish the
Lagrange multiplier from other uses of $\lambda$. Its algebraic role is unchanged.
A reference that prints a vector field as $P\hat{\imath}+Q\hat{\jmath}+R\hat{k}$
means the three component functions called $F_x,F_y,F_z$ here; those letters do
not automatically mean pressure, heat, or resistance.

**Know without a lookup:** what is held fixed; why uncertainty magnitudes and
signed rates are different; the first-order limitation of a differential estimate;
the need to normalize a direction; the three operator output types; and why
stationary and Lagrange points must be checked. These are study priorities,
not unverified claims that a formula is absent from the Handbook.

---

## Where This Goes Wrong

**Treating the frozen variable as zero.** In $f_x$ for $x^2y$, the answer is
$2xy$, not $2x$. The value of $y$ stays in the coefficient.

**Dropping the inner derivative.** $\partial(e^{xy})/\partial x=ye^{xy}$.
The inner derivative is $y$ because $y$ is held constant.

**Interchanging mixed partials without checking conditions.** Continuous second
partials near the point are a sufficient condition. A singularity or piecewise
definition deserves inspection.

**Using $df$ as an exact finite change.** The differential is a linear model.
Its uncertainty sum bounds that model, not automatically the nonlinear output
over a finite interval. Worked Example 5 shows the difference.

**Dividing by a nominal zero.** Relative uncertainty and the power-law shortcut
need nonzero nominal quantities. Near zero, use an absolute-error analysis.

**Adding magnitudes in a rates problem.** For a first-order worst-case uncertainty
estimate, take magnitudes. For a known change or time rate, keep signs. Worked
Example 7 would be three times too large if both contributions were made positive.

**Ranking inputs using only their exponents.** Multiply each exponent's magnitude
by its input's relative tolerance. Worked Examples 5 and 6 have different
dominant measurements despite the same squared-dimension structure.

**Reading unequal contour intervals as equal.** Spacing alone is meaningful only
after you compare the labels. Equal-radius circles on a paraboloid can have very
different height increments.

**Forgetting the unit direction.** Divide a direction vector by its magnitude
before taking the dot product. Check
$|D_{\mathbf u}f|\le|\nabla f|$.

**Giving a zero gradient a direction.** A zero vector cannot be normalized.
All first-order directional derivatives are zero there; inspect higher-order
behavior before claiming a maximum or minimum.

**Confusing the three output types.** Gradient: vector. Divergence: scalar.
Curl: vector. A type error is enough to reject an answer.

**Pairing the wrong subscripts.** Divergence uses matching pairs. Curl mixes
different component and coordinate indices, with the middle determinant sign
reversed.

**Assuming zero curl always gives a global potential.** Check smoothness and the
domain. An excluded hole or singularity can invalidate the implication.

**Treating $D=0$ as “saddle.”** It means the second-derivative test is inconclusive.
Higher-order terms may give a minimum, maximum, or saddle. Two paths with opposite
signs prove a saddle; a few favorable paths do not prove a minimum.

**Ignoring boundaries.** The zero-gradient test concerns differentiable interior
points. Absolute extrema can occur on boundaries or at nonsmooth points.

**Stopping at the Lagrange equations.** Include the constraint, check its gradient,
and establish whether each admissible candidate gives the required optimum.
Report the requested dimensions or output, not just the multiplier.

---

## Key Terms

| Term | Definition |
|---|---|
| Function of several variables | A scalar-valued function of two or more independent inputs |
| Surface | The graph $z=f(x,y)$ in three dimensions |
| Level curve / contour | Points in the input plane where the function has one fixed value |
| Scalar field | A scalar-valued function of position |
| Partial derivative | Rate with respect to one input while the other independent inputs are fixed |
| Mixed partial | A second derivative taken with respect to two different inputs |
| Equality of mixed partials | Interchanging differentiation order gives the same result when the appropriate second partials are continuous nearby |
| Total differential | The linear output change $df=\sum f_{x_i}\,dx_i$ |
| Power-law rule | First-order relative uncertainty in a product of powers is the sum of relative input tolerances weighted by exponent magnitudes |
| Tangent plane | Plane matching a differentiable surface's value and first-order slopes at a point |
| Multivariable chain rule | Total rate found by adding each input sensitivity multiplied by that input's rate |
| Del operator | Cartesian vector of partial-derivative operators, written $\nabla$ |
| Gradient | Vector of a scalar field's partials; where nonzero, its direction and magnitude give steepest first-order increase |
| Directional derivative | Rate per unit distance in a specified unit direction |
| Vector field | A function assigning a vector to each point in its domain |
| Divergence | Scalar measuring local net outward flux per unit volume |
| Solenoidal | Having zero divergence |
| Curl | Vector measuring local circulation density; for velocity, twice the local angular-velocity vector |
| Irrotational | Having zero curl |
| Conservative field | A vector field expressible as the gradient of a single scalar potential over its domain |
| Scalar potential | A scalar function $\Psi$ whose gradient produces a specified conservative field |
| Simply connected domain | A connected region in which every closed loop can contract to a point while staying inside the region |
| Multivariable critical point | An interior point where the gradient is zero or a needed first partial does not exist |
| Saddle point | A stationary point with both higher and lower nearby function values |
| Second-partial discriminant | $D=f_{xx}f_{yy}-f_{xy}^2$, used at a stationary point in the two-variable second-derivative test |
| Constrained optimization | Maximizing or minimizing an objective while satisfying restrictions on the inputs |
| Lagrange multiplier | Scalar relating the objective and constraint gradients at a regular constrained candidate |

For earlier vocabulary, revisit error propagation, linearization, and critical
points in [01-18](01-18-Applications-of-the-Derivative.md), and unit vectors in
[01-13](01-13-Vectors-and-Vector-Operations.md).

---

## Review Questions

Answer the conceptual questions before using a calculator. For calculations,
state the model, carry the units, and include a check. Use first-order uncertainty
estimates unless the question explicitly asks for finite endpoints.

### Conceptual

1. Explain the difference between $\partial f/\partial x$ and $df/dx$ when
   another input depends on $x$. Give a short example.
2. State a sufficient condition for equality of mixed partials. How does that
   theorem help you check a calculation, and when should you be cautious?
3. Explain how a tangent plane relates to Taylor approximation. Under what
   smoothness condition can its error be bounded by a second-order quantity nearby?
4. Write the total differential of $f(x,y,z)$. Explain why a known change keeps
   signs while a first-order worst-case uncertainty estimate adds magnitudes.
5. State the direction and magnitude properties of a nonzero gradient. What
   changes when the gradient is zero?
6. For $f(x,y)=x^2+y^2$, describe the surface and its level curves. Explain why
   comparing the spacing of levels $1,4,9,16$ does not directly show the steepening
   that equal-increment contour spacing shows.
7. State the output type of gradient, divergence, and curl. What additional
   conditions let you infer a conservative field from zero curl?
8. Interpret $\nabla\cdot\mathbf v=0$ for a velocity field. Why is a statement
   about mass accumulation incomplete if density is allowed to vary?
9. Describe a saddle point. Does $D=0$ prove that a point is a saddle? Explain.
10. Explain the geometric reason for $\nabla f=\lambda_L\nabla g$ at a regular
    constrained optimum. Why must the candidate still be checked?

### Calculation

11. For $f(x,y)=4x^3y^2-5xy+2y^4$, find $f_x,f_y,f_{xx},f_{yy}$ and both mixed
    partials. Verify that the mixed partials agree.
12. For $f(x,y)=\ln(x^2+y)$, find $f_x,f_y$ at $(2,1)$, write the tangent plane,
    and estimate $f(2.02,0.99)$. State the domain condition and check the estimate
    by direct substitution.
13. A plate has dimensions $a=240\pm2\ \mathrm{mm}$ and $b=120\pm1\ \mathrm{mm}$.
    Find its area, first-order relative uncertainty, and each input's share.
14. Use the supplied model $P_w=I_e^2R_e$, with
    $I_e=3.50\pm0.04\ \mathrm A$ and $R_e=22.0\pm0.3\ \Omega$.
    (a) Find power and first-order uncertainty, including input shares.
    (b) Separately, at those nominal values, let
    $dI_e/dt=0.020\ \mathrm{A/s}$ and $dR_e/dt=-0.10\ \Omega/\mathrm s$.
    Find the signed power rate.
15. For $f(x,y)=x^2y-y^3$ at $(3,1)$, find the gradient, maximum rate of increase,
    and directional derivative toward $(3,5)$.
16. Find divergence and curl at $(1,1,2)$ for
    $\mathbf F=xy\,\hat{\imath}+yz^2\,\hat{\jmath}+zx\,\hat{k}$.
17. Locate and classify all critical points of $f(x,y)=x^2+xy+y^2-6x$.
18. An open-top rectangular box must hold $32\ \mathrm{m^3}$. Use Lagrange
    multipliers to find the positive dimensions minimizing material area.
19. **Supplied engineering model.** For a simply supported beam with a central
    point load, use $\delta=F_LL^3/(48EI_A)$ without deriving beam theory.
    Here $F_L$ is force, $E$ elastic modulus, and $I_A$ the second moment of area
    introduced in 01-20. The data are $F_L=25.0\pm0.5\ \mathrm{kN}$,
    $L=4.00\pm0.01\ \mathrm m$, $E=200\pm5\ \mathrm{GPa}$, and
    $I_A=(85.0\pm1.5)\times10^6\ \mathrm{mm^4}$.
    Find deflection in millimetres, its first-order relative uncertainty,
    and the ranking of the four uncertainty contributions.

### Multiple Choice

20. For $f(x,y)=x^2y^3$, $f_y$ equals:
    A) $2xy^3$  B) $3x^2y^2$  C) $6xy^2$  D) $2xy^3+3x^2y^2$.

21. The gradient of a differentiable scalar field is:
    A) a scalar  B) a vector  C) a matrix  D) always zero.

22. The divergence of a differentiable vector field is:
    A) a scalar  B) a vector  C) necessarily perpendicular to the field  D) its curl.

23. For $V=\pi r^2h$, with radius and height each having 1% tolerances, the
    first-order worst-case relative uncertainty estimate is:
    A) 1%  B) 2%  C) 3%  D) 4%.

24. At a stationary point of a function with continuous second partials, $D<0$
    indicates:
    A) local minimum  B) local maximum  C) saddle point  D) an inconclusive test.

25. A field with zero curl is called:
    A) solenoidal  B) irrotational  C) divergent  D) incompressible.

26. Where $\nabla f\ne\mathbf0$, the directional derivative is greatest when
    the **unit** direction vector points:
    A) perpendicular to $\nabla f$  B) in the same direction as $\nabla f$
    C) along a level curve  D) opposite to $\nabla f$.

27. In the supplied model $\mathbf q=-k\nabla T$ with $k>0$, the minus sign means:
    A) conductivity is negative  B) heat flows toward higher temperature
    C) heat flows toward lower temperature  D) the gradient is a scalar.

---

## Answer Key with Explanations

### Conceptual

1. A partial derivative freezes the other independent inputs. A total derivative
   follows their actual dependence. With $f(x,y)=xy$ and $y=x$,
   $\partial f/\partial x=y$, but along that path $f=x^2$ and $df/dx=2x$.
   At $x=y=1$, the rates are 1 and 2 respectively. (§23.2, §23.4)
2. Continuous second partials in a neighborhood are sufficient. Under that
   condition, $f_{xy}=f_{yx}$, so independent calculations should agree.
   Disagreement in the smooth polynomial/exponential examples signals an error;
   a piecewise definition or singularity first requires checking the condition.
   (§23.2)
3. It keeps the function value and all first-order terms. Bounded second partials
   nearby give a second-order error bound for small displacements. The error may
   be smaller through cancellation, and the approximation is not automatically
   reliable far from the base point. (§23.3)
4. $df=f_xdx+f_ydy+f_zdz$. Known signed changes can cancel. A first-order
   worst-case estimate instead permits each input deviation to push the output
   in the unfavorable direction and uses
   $\varepsilon_f^{(1)}=|f_x|\varepsilon_x+|f_y|\varepsilon_y+|f_z|\varepsilon_z$.
   This bounds the linearized change, not necessarily the finite nonlinear error.
   (§23.3, §23.4)
5. The nonzero gradient points in the direction of greatest first-order increase;
   its magnitude is that maximum rate. A tangent to a level curve has zero dot
   product with it. At a zero gradient, all first-order directional derivatives
   vanish and no unique gradient direction exists. (§23.5)
6. The surface is an upward-opening paraboloid. Positive level curves are circles
   of radius $\sqrt{c_0}$. Levels $1,4,9,16$ have radii $1,2,3,4$, so their radial
   gaps are equal while their height gaps are not. Equal height increments are
   needed for a direct spacing comparison of steepness. (§23.1)
7. Gradient and curl are vectors; divergence is a scalar. Zero curl implies a
   global scalar potential when the field has continuous first partials on an
   open simply connected domain. Omitting the domain condition can make the
   conclusion false. (§23.5, §23.6)
8. It means no local volumetric expansion or contraction. For constant density
   and no mass sources, it expresses incompressible mass conservation. With
   variable density, density changes and transport also affect mass accumulation.
   (§23.6)
9. A saddle has both higher and lower nearby values despite a stationary point.
   $D=0$ is inconclusive: $x^4+y^4$, $-x^4-y^4$, and $x^4-y^4$ give a minimum,
   maximum, and saddle respectively at the origin, all with $D=0$. (§23.7)
10. Feasible tangent directions are perpendicular to $\nabla g$. At an optimum,
    the objective has zero derivative in those directions too, making its gradient
    parallel to $\nabla g$ or zero. The condition assumes a regular constraint
    point and finds candidates; it does not distinguish maxima, minima, or other
    stationary behavior along the constraint. (§23.7)

### Calculation

11. Freeze the other input for each derivative:

    $$f_x=12x^2y^2-5y,\qquad f_y=8x^3y-5x+8y^3,$$
    $$f_{xx}=24xy^2,\qquad f_{yy}=8x^3+24y^2,$$
    $$\boxed{f_{xy}=f_{yx}=24x^2y-5.}$$

    **Check:** the function is polynomial, so the mixed-partial condition holds
    everywhere, and the two routes agree. (§23.2)

12. The domain requires $x^2+y>0$. Differentiation gives

    $$f_x=\frac{2x}{x^2+y},\quad f_y=\frac1{x^2+y},\quad
    f_x(2,1)=0.8,\quad f_y(2,1)=0.2.$$

    The plane is $z=\ln5+0.8(x-2)+0.2(y-1)$. Thus

    $$\boxed{f(2.02,0.99)\approx\ln5+0.8(0.02)+0.2(-0.01)
    =\ln5+0.014\approx1.62344.}$$

    **Check:** the exact value is $\ln(5.0704)\approx1.62342$, within about
    $0.00002$ of the estimate, and both points lie in the domain. (§23.2, §23.3)

13. $A_0=(240)(120)=28800\ \mathrm{mm^2}$. Then

    $$\frac{\varepsilon_A^{(1)}}{A_0}=\frac2{240}+\frac1{120}
    =\frac1{60}=1.6667\%,\qquad
    \boxed{\varepsilon_A^{(1)}=480\ \mathrm{mm^2}}.$$

    Both inputs contribute 50%. **Check:** the direct differential is
    $(120\ \mathrm{mm})(2\ \mathrm{mm})+(240\ \mathrm{mm})(1\ \mathrm{mm})$,
    also $480\ \mathrm{mm^2}$. (§23.3)

14. (a) $P_{w,0}=(3.50)^2(22.0)=269.5\ \mathrm W$.

    $$\frac{\varepsilon_{P_w}^{(1)}}{P_{w,0}}
    =2\frac{0.04}{3.50}+\frac{0.3}{22.0}
    =0.0364935=3.64935\%,$$
    $$\boxed{\varepsilon_{P_w}^{(1)}=9.835\ \mathrm W\approx9.8\ \mathrm W}.$$

    Current supplies 62.6% and resistance 37.4% of the first-order total.
    **Check:** their absolute contributions are
    $(2I_eR_e)\varepsilon_{I_e}=6.160\ \mathrm W$ and
    $I_e^2\varepsilon_{R_e}=3.675\ \mathrm W$, summing to $9.835\ \mathrm W$.

    (b) Keep the signs of the time rates:

    $$\frac{dP_w}{dt}=2I_eR_e\frac{dI_e}{dt}
    +I_e^2\frac{dR_e}{dt}
    =3.080-1.225=\boxed{1.855\ \mathrm{W/s}}.$$

    Increasing current wins over decreasing resistance; the net is positive.
    (§23.3, §23.4)

15. $f_x=2xy$ and $f_y=x^2-3y^2$, so
    $\boxed{\nabla f(3,1)=\langle6,6\rangle}$ and
    $\boxed{|\nabla f|=6\sqrt2\approx8.49}$.
    The direction toward $(3,5)$ is $\langle0,4\rangle$, whose unit vector is
    $\langle0,1\rangle$. The directional derivative is $\boxed{6}$.
    **Check:** $|6|\le6\sqrt2$. (§23.5)

16. Differentiate matching components for divergence:
    $\nabla\cdot\mathbf F=y+z^2+x$, giving $\boxed{6}$.
    For curl,

    $$\nabla\times\mathbf F
    =\langle-2yz,-z,-x\rangle,\qquad
    \boxed{\nabla\times\mathbf F(1,1,2)=\langle-4,-2,-1\rangle}.$$

    **Check:** divergence is scalar and curl is vector. The middle curl component
    is $(F_x)_z-(F_z)_x=0-z$, confirming its sign. (§23.6)

17. Solve $2x+y-6=0$ and $x+2y=0$: $(x,y)=(4,-2)$.
    Here $f_{xx}=f_{yy}=2$, $f_{xy}=1$, and $D=3>0$.
    The point is a minimum with $\boxed{f(4,-2)=-12}$.
    **Check:** writing $u=x-4$ and $v=y+2$ gives
    $f+12=(u+v/2)^2+3v^2/4\ge0$, proving this minimum is global. (§23.7)

18. Let $x,y$ be the base dimensions and $z$ the height, all positive.
    The objective is $A=xy+2xz+2yz$ and the constraint is $xyz=32\ \mathrm{m^3}$.
    Lagrange gives

    $$y+2z=\lambda_L yz,\quad x+2z=\lambda_L xz,\quad
    2x+2y=\lambda_L xy.$$

    Multiplying the first two equations by $x$ and $y$ shows $x=y$.
    The third then gives $\lambda_L=4/x$; the first gives $x=2z$.
    Hence $4z^3=32$ in metre units:

    $$\boxed{x=y=4\ \mathrm m,\quad z=2\ \mathrm m,\quad A=48\ \mathrm{m^2}}.$$

    **Check:** volume is $4(4)(2)=32\ \mathrm{m^3}$. For fixed base product,
    $(x-y)^2\ge0$ makes $x+y$ smallest at $x=y$. Among square bases,
    $A(x)=x^2+128/x$ in consistent metre units has
    $A''(x)=2+256/x^3>0$ and diverges at either positive-domain extreme.
    The candidate is the global minimum. (§23.7)

19. First convert $I_A=85.0\times10^{-6}\ \mathrm{m^4}$ and
    $E=200\times10^9\ \mathrm{N/m^2}$. Then

    $$\delta_0=\frac{(25.0\times10^3)(4.00)^3}
    {48(200\times10^9)(85.0\times10^{-6})}
    =0.00196078\ \mathrm m=\boxed{1.96078\ \mathrm{mm}}.$$

    The exponent weights are $1,3,1,1$ in magnitude:

    $$\frac{\varepsilon_\delta^{(1)}}{\delta_0}
    =\frac{0.5}{25.0}+3\frac{0.01}{4.00}+\frac5{200}+\frac{1.5}{85.0}
    =0.0701471=\boxed{7.01471\%}.$$

    Thus $\varepsilon_\delta^{(1)}\approx0.13755\ \mathrm{mm}$ and the rounded
    first-order result is $(1.96\pm0.14)\ \mathrm{mm}$.
    Ranking: $E$ contributes 35.6%, load 28.5%, $I_A$ 25.2%, and length 10.7%.
    Improve the modulus estimate first if comparable improvements cost the same.
    **Check:** the model's units reduce to
    $(\mathrm N\,\mathrm{m^3})/[(\mathrm{N/m^2})\mathrm{m^4}]=\mathrm m$.
    The exponent of 3 does not make length dominant because its relative
    tolerance is much smaller. (§23.3)

### Multiple Choice

20. **B.** Hold $x^2$ fixed and differentiate $y^3$ to $3y^2$.
    A is $f_x$; C is the mixed partial $f_{xy}$; D adds two different first
    partials and is not the requested derivative. (§23.2)
21. **B.** The gradient collects coordinate sensitivities into a vector.
    A omits direction, C is a different kind of object, and D is true only
    at special points or for a constant field. (§23.5)
22. **A.** Divergence adds three scalar partial derivatives.
    B and C incorrectly assign it a vector direction; D confuses the dot and
    cross operations and their output types. (§23.6)
23. **C.** The first-order estimate is $2(1\%)+1(1\%)=3\%$.
    A omits contributions, B ignores the radius exponent, and D adds an
    unsupported extra percentage point. The exact finite upper deviation is
    $(1.01)^3-1=3.0301\%$, reinforcing the first-order qualification. (§23.3)
24. **C.** Negative discriminant gives quadratic changes of opposite signs
    along suitable directions. A and B require positive $D$ with the appropriate
    sign of $f_{xx}$; D describes the zero-discriminant case. (§23.7)
25. **B.** Irrotational means zero curl. Solenoidal means zero divergence;
    incompressible concerns a velocity field's volume changes. Neither follows
    merely from zero curl. “Divergent” is not the name for this condition. (§23.6)
26. **B.** The dot product is greatest when $\cos\theta=1$.
    A and C give zero at a regular contour; D gives the most negative derivative.
    The nonzero-gradient condition prevents an undefined preferred direction.
    (§23.5)
27. **C.** $\nabla T$ points toward higher temperature, so $-k\nabla T$ points
    toward lower temperature when $k>0$. A contradicts the given coefficient,
    B reverses the physical direction, and D gives the wrong output type. (§23.5)

---

## Practice Problems

Work these on paper before reading the solutions. The physical models are
supplied. Use their stated units consistently; numerical coordinate values refer
to those units. First-order uncertainty estimates do not replace finite-range
tolerance checks.

1. **Temperature sensitivities — SI.** A plate has
   $T(x,y)=20\,^\circ\mathrm C+(3\ \mathrm{K/m^2})x^2
   +(2\ \mathrm{K/m^2})xy-(1\ \mathrm{K/m^2})y^2$.
   At $(1,2)\ \mathrm m$, find $T$, $T_x$, $T_y$, both mixed partials, and
   a unit direction along which the first-order temperature change is zero.
2. **Surface approximation — SI.** A height model is
   $z=x^2/(4\ \mathrm m)+y^2/(2\ \mathrm m)$.
   Find the tangent plane at $(x,y)=(2,1)\ \mathrm m$.
   Estimate the height at $(2.04,0.98)\ \mathrm m$ and compare with the exact value.
3. **Tank-volume uncertainty — USCS.** A cylinder has
   $r=1.50\pm0.01\ \mathrm{ft}$ and $h=4.00\pm0.02\ \mathrm{ft}$.
   Find nominal volume, first-order uncertainty, and each input's share.
   Compare the relative estimate with the exact upper endpoint.
4. **Changing cylinder — SI.** At one instant, $r=0.250\ \mathrm m$,
   $h=1.20\ \mathrm m$, $dr/dt=0.0020\ \mathrm{m/s}$, and
   $dh/dt=-0.0050\ \mathrm{m/s}$. Find $dV/dt$ for $V=\pi r^2h$ and identify
   which effect wins.
5. **Direction matters — USCS.** Let
   $T(x,y)=68\,^\circ\mathrm F+(4\,^\circ\mathrm{F/ft})x
   -(3\,^\circ\mathrm{F/ft})y$.
   Find the temperature rate per foot when moving from the origin toward
   $(3,4)\ \mathrm{ft}$, the maximum rate, and its unit direction.
6. **A supplied heat-flux model — SI.** Let
   $T(x,y)=300\ \mathrm K+(2\ \mathrm{K/m^2})x^2
   +(3\ \mathrm{K/m^2})y^2$ and
   $\mathbf q=-k\nabla T$, with $k=15\ \mathrm{W/(m\cdot K)}$.
   Find heat flux at $(1,2)\ \mathrm m$, its magnitude, and its unit direction.
7. **Expansion without spin — USCS.** Coordinates are in feet and
   $\mathbf v=\langle(2\ \mathrm{s^{-1}})x,
   -(1\ \mathrm{s^{-1}})y,(0.5\ \mathrm{s^{-1}})z\rangle$.
   Compute divergence and curl. Is the field solenoidal? Is it irrotational?
8. **Spin without expansion — SI.** Coordinates are in metres and
   $\mathbf v=\langle-(3\ \mathrm{s^{-1}})y,
   (3\ \mathrm{s^{-1}})x,0\rangle$.
   Find velocity at $(2,1,0)\ \mathrm m$, divergence, curl, and the local
   angular-velocity vector.
9. **An open box — USCS.** A rectangular box with no lid must hold
   $108\ \mathrm{ft^3}$. With uniform material thickness and no allowance for
   seams or waste, find the positive dimensions minimizing material area.
   Use Lagrange multipliers and verify the minimum.
10. **Largest inscribed rectangle — SI.** A rectangle centered at the origin has
    vertices $(\pm x,\pm y)$ and lies inside a circle of radius $4\ \mathrm m$,
    with $x,y>0$. Maximize its area using the boundary constraint
    $x^2+y^2=16\ \mathrm{m^2}$. Find the full side lengths and area, and
    prove that your candidate is a global maximum.

---

## Practice Problem Solutions

1. **Approach.** Differentiate the supplied temperature model, evaluate the
   sensitivities, then choose a direction perpendicular to the gradient.

   **Solution.** Substitution gives $T=20+3+4-4=23\,^\circ\mathrm C$.
   The derivatives are

   $$T_x=(6\ \mathrm{K/m^2})x+(2\ \mathrm{K/m^2})y,\qquad
   T_y=(2\ \mathrm{K/m^2})x-(2\ \mathrm{K/m^2})y.$$

   At the point, $\nabla T=\langle10,-2\rangle\ \mathrm{K/m}$ and
   $T_{xy}=T_{yx}=2\ \mathrm{K/m^2}$.
   A perpendicular unit direction is
   $\boxed{\mathbf u=\langle1,5\rangle/\sqrt{26}}$ (its negative also works).
   **Check.** $\nabla T\cdot\mathbf u=(10-10)/\sqrt{26}=0\ \mathrm{K/m}$,
   and $|\mathbf u|=1$. Celsius temperature differences and kelvin differences
   have equal size. (§23.2, §23.5)

2. **Approach.** Evaluate height and slopes at the base point, keeping their
   units. Compare the local plane with direct substitution.

   **Solution.** The base height is $1.50\ \mathrm m$.
   The slopes are $z_x=x/(2\ \mathrm m)=1$ and
   $z_y=y/(1\ \mathrm m)=1$, both dimensionless there. Thus

   $$\boxed{z_{\mathrm{plane}}=1.50\ \mathrm m
   +(x-2.00\ \mathrm m)+(y-1.00\ \mathrm m).}$$

   The prediction is $1.50+0.04-0.02=\boxed{1.52\ \mathrm m}$.
   **Check.** The exact height is
   $2.04^2/4+0.98^2/2=1.5206\ \mathrm m$.
   The error is $0.0006\ \mathrm m=0.6\ \mathrm{mm}$, equal to
   $(0.04\ \mathrm m)^2/(4\ \mathrm m)
   +(-0.02\ \mathrm m)^2/(2\ \mathrm m)$. (§23.3)

3. **Approach.** Use the radius exponent 2 and height exponent 1. Then increase
   both positive inputs to their upper endpoints for an exact comparison.

   **Solution.**

   $$V_0=\pi(1.50\ \mathrm{ft})^2(4.00\ \mathrm{ft})
   =28.2743\ \mathrm{ft^3},$$
   $$\frac{\varepsilon_V^{(1)}}{V_0}
   =2\frac{0.01}{1.50}+\frac{0.02}{4.00}
   =0.0183333,$$
   $$\boxed{\varepsilon_V^{(1)}=0.51836\ \mathrm{ft^3},\quad
   V\approx(28.27\pm0.52)\ \mathrm{ft^3}.}$$

   Radius contributes 72.7% and height 27.3%.
   **Check.** The exact relative upper deviation is
   $(1.51/1.50)^2(4.02/4.00)-1=1.84447\%$,
   slightly above the first-order 1.83333%. No mass/force conversion is involved;
   this is purely a geometric volume model. (§23.3)

4. **Approach.** Add the signed radius and height contributions to the volume rate.

   **Solution.**

   $$\frac{dV}{dt}=2\pi rh\frac{dr}{dt}+\pi r^2\frac{dh}{dt}$$
   $$=2\pi(0.250)(1.20)(0.0020)+\pi(0.250)^2(-0.0050)
   =0.0008875\pi\ \mathrm{m^3/s}$$
   $$\boxed{\frac{dV}{dt}=0.0027882\ \mathrm{m^3/s}\approx2.79\ \mathrm{L/s}.}$$

   **Check.** The positive radius term is $0.0037699\ \mathrm{m^3/s}$;
   the negative height term is $-0.00098175\ \mathrm{m^3/s}$.
   Their sum is positive, so the widening cylinder gains volume despite becoming
   shorter. Each term is an area times a length rate. (§23.4)

5. **Approach.** Normalize the displacement from the origin before taking its
   dot product with the constant gradient.

   **Solution.** $\nabla T=\langle4,-3\rangle\,^\circ\mathrm{F/ft}$.
   Toward $(3,4)$, $\mathbf u=\langle3/5,4/5\rangle$, so

   $$D_{\mathbf u}T=4(3/5)-3(4/5)=\boxed{0\,^\circ\mathrm{F/ft}}.$$

   The maximum rate is
   $\boxed{|\nabla T|=5\,^\circ\mathrm{F/ft}}$, in unit direction
   $\boxed{\langle4/5,-3/5\rangle}$.
   **Check.** Direct substitution at $(3,4)\ \mathrm{ft}$ gives
   $68+12-12=68\,^\circ\mathrm F$, unchanged from the origin. Because the field
   is affine, this entire straight path has zero change, not just zero local rate.
   (§23.5)

6. **Approach.** Compute the temperature gradient, then multiply by $-k$.

   **Solution.** At $(1,2)\ \mathrm m$,
   $\nabla T=\langle4,12\rangle\ \mathrm{K/m}$.

   $$\boxed{\mathbf q=\langle-60,-180\rangle\ \mathrm{W/m^2}},\qquad
   \boxed{|\mathbf q|=\sqrt{36000}=189.74\ \mathrm{W/m^2}}.$$

   Its unit direction is
   $\boxed{\langle-1,-3\rangle/\sqrt{10}}$.
   **Check.** The direction is opposite the temperature gradient, its norm is
   one, and conductivity times temperature gradient gives
   $\mathrm{W/m^2}$ as required. (§23.5)

7. **Approach.** Use matching derivatives for divergence and cross derivatives
   for curl; each component depends only on its matching coordinate.

   **Solution.**

   $$\boxed{\nabla\cdot\mathbf v=2-1+0.5=1.5\ \mathrm{s^{-1}}},\qquad
   \boxed{\nabla\times\mathbf v=\mathbf0\ \mathrm{s^{-1}}}.$$

   The field is **not solenoidal** but is **irrotational**.
   **Check.** Every cross derivative is zero. The positive divergence describes
   local expansion; zero curl says that expansion need not involve local spin.
   Differentiating ft/s with respect to ft leaves $\mathrm{s^{-1}}$. (§23.6)

8. **Approach.** Substitute for velocity, then differentiate the field before
   substituting for its operators.

   **Solution.** At $(2,1,0)\ \mathrm m$,
   $\boxed{\mathbf v=\langle-3,6,0\rangle\ \mathrm{m/s}}$.
   All matching derivatives vanish, so divergence is zero.
   The only nonzero curl component is

   $$\frac{\partial v_y}{\partial x}-\frac{\partial v_x}{\partial y}
   =3-(-3)=6\ \mathrm{s^{-1}}.$$

   Therefore
   $\boxed{\nabla\times\mathbf v=6\hat{k}\ \mathrm{s^{-1}}}$ and the local
   angular-velocity vector is $\boxed{3\hat{k}\ \mathrm{rad/s}}$.
   **Check.** A point on the positive $x$ axis moves toward positive $y$,
   consistent with the positive $z$ rotation direction. Zero divergence and
   nonzero curl can occur together. (§23.6)

9. **Approach.** Include the base and four sides, but no lid. Use the volume
   equation together with the three Lagrange component equations.

   **Solution.** For base dimensions $x,y$ and height $z$,
   $A=xy+2xz+2yz$ and $xyz=108\ \mathrm{ft^3}$. The equations are

   $$y+2z=\lambda_L yz,\quad x+2z=\lambda_L xz,\quad
   2x+2y=\lambda_L xy.$$

   Multiplying the first two by $x$ and $y$ and subtracting gives $x=y$.
   The third then gives $\lambda_L=4/x$; substitution into the first gives
   $x=2z$. Consequently $4z^3=108\ \mathrm{ft^3}$:

   $$\boxed{x=y=6\ \mathrm{ft},\qquad z=3\ \mathrm{ft},\qquad
   A=108\ \mathrm{ft^2}.}$$

   **Check.** Volume is $6(6)(3)=108\ \mathrm{ft^3}$.
   For any fixed height, a square base minimizes the side-area contribution
   because $(x-y)^2\ge0$ implies $x+y\ge2\sqrt{xy}$.
   On square bases, $A(x)=x^2+432/x$ in consistent foot units has
   $A''(x)=2+864/x^3>0$ and grows without bound at either positive-domain extreme.
   The stationary dimensions give the global minimum. (§23.7)

10. **Approach.** The full rectangle area is $A=4xy$, not $xy$.
    At a maximum it reaches the circle; otherwise scaling both positive
    dimensions upward would increase area while remaining feasible.

    **Solution.** Let $g=x^2+y^2$. Lagrange gives

    $$4y=2\lambda_L x,\qquad4x=2\lambda_L y,\qquad
    x^2+y^2=16\ \mathrm{m^2}.$$

    For positive $x,y$, the first two imply $x=y$ and $\lambda_L=2$.
    Thus $x=y=2\sqrt2\ \mathrm m$ and

    $$\boxed{\text{full sides}=4\sqrt2\ \mathrm m\approx5.657\ \mathrm m,\qquad
    A_{\max}=32\ \mathrm{m^2}.}$$

    **Check.** From $(x-y)^2\ge0$, $2xy\le x^2+y^2\le16\ \mathrm{m^2}$;
    hence $4xy\le32\ \mathrm{m^2}$ throughout the feasible disk.
    The candidate achieves this upper bound. Boundary-axis cases have zero area.
    (§23.7)

---

## Source References

The derivations and exercises above are presented in the guide's own notation.
For independent mathematical reference and additional illustrations:

- OpenStax, *Calculus Volume 3*, [4.4, Tangent Planes and Linear Approximations](https://openstax.org/books/calculus-volume-3/pages/4-4-tangent-planes-and-linear-approximations).
- OpenStax, *Calculus Volume 3*, [4.6, Directional Derivatives and the Gradient](https://openstax.org/books/calculus-volume-3/pages/4-6-directional-derivatives-and-the-gradient).
- OpenStax, *Calculus Volume 3*, [4.8, Lagrange Multipliers](https://openstax.org/books/calculus-volume-3/pages/4-8-lagrange-multipliers).
- OpenStax, *Calculus Volume 3*, [6.5, Divergence and Curl](https://openstax.org/books/calculus-volume-3/pages/6-5-divergence-and-curl).
- NCEES, [FE exam and reference-handbook access](https://ncees.org/exams/fe-exam/).
  This source establishes where to obtain the assigned reference; it does not
  verify the page locations or coverage of individual formulas in this draft.

---

## Quick Reference

**Partials:** freeze all other independent inputs. Continuous second partials
nearby permit $f_{xy}=f_{yx}$.

**Local change and tangent plane** — evaluate partials at the base point:

$$df=f_xdx+f_ydy+f_zdz,\qquad
z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b).$$

$df$ estimates $\Delta f$. Bounded second partials give a second-order remainder
bound nearby; the approximation can fail for large steps.

**First-order uncertainty estimate:**

$$\varepsilon_f^{(1)}=\sum_i|f_{x_i}|\varepsilon_{x_i}.$$

For nonzero inputs and $f=Cx^py^qz^s$ with exact $C$,

$$\frac{\varepsilon_f^{(1)}}{|f_0|}
=|p|\frac{\varepsilon_x}{|x|}+|q|\frac{\varepsilon_y}{|y|}
+|s|\frac{\varepsilon_z}{|z|}.$$

This is not automatically an exact finite-error bound. Rank the weighted terms,
not just the exponents.

**Chain rule:** $\displaystyle df/dt=\sum_i f_{x_i}\,dx_i/dt$.
Keep signs; add $\partial f/\partial t$ if the model has explicit time dependence.

| Operator | Formula | Output |
|---|---|---|
| Gradient | $\nabla f=\langle f_x,f_y,f_z\rangle$ | vector |
| Divergence | $\nabla\cdot\mathbf F=(F_x)_x+(F_y)_y+(F_z)_z$ | scalar |
| Curl | $\nabla\times\mathbf F=\langle(F_z)_y-(F_y)_z,(F_x)_z-(F_z)_x,(F_y)_x-(F_x)_y\rangle$ | vector |

$$D_{\mathbf u}f=\nabla f\cdot\mathbf u,\qquad
|\mathbf u|=1,\qquad |D_{\mathbf u}f|\le|\nabla f|.$$

A nonzero gradient points toward steepest increase and is normal to a regular
contour. Zero divergence means solenoidal; zero curl means irrotational.
Zero curl implies a conservative field under the smoothness and domain
conditions stated in §23.6.

**Stationary points:** solve $f_x=f_y=0$ and evaluate $D=f_{xx}f_{yy}-f_{xy}^2$.

| Condition | Conclusion |
|---|---|
| $D>0,\ f_{xx}>0$ | local minimum |
| $D>0,\ f_{xx}<0$ | local maximum |
| $D<0$ | saddle |
| $D=0$ | inconclusive |

**One smooth equality constraint:**
$\nabla f=\lambda_L\nabla g$ **and** $g=c_0$, with $\nabla g\ne\mathbf0$.
Classify candidates and inspect allowed boundaries and singular points.
Minimum-area closed cylinder at fixed volume: $h=2r$.

---

## What's Next

You have extended differentiation from one changing input to several. You can
separate sensitivities, recombine actual changes, estimate measurement effects,
and ask what a field is doing at one location. You can also distinguish a
promising design candidate from a verified optimum.

The next chapter, **01-24 Multiple Integration**, turns from local rates
to accumulation over regions. The surfaces and level curves from §23.1 give us
a way to picture the regions before setting up the sums. Keep that geometric
picture; it will matter as much as the integration technique.

### Going further — optional

Differential equations later describe unknown functions through their rates of
change. Heat transfer, fluid flow, and electrical fields reuse the gradient,
divergence, and curl. Statistical uncertainty methods later add information about
measurement distributions and dependence. These are destinations, not prerequisites
for the calculations you have just completed.

Before leaving, do Practice Problems 3 and 4 back to back. One asks how uncertain
an output might be; the other asks which way it is actually changing. If you can
explain why one uses magnitudes and the other keeps signs, you have learned the
distinction that makes this chapter useful.

Bring that habit to the next page.

See you there.
