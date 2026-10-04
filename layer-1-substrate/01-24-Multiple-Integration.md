---
chapter: "01-24"
title: "Multiple Integration"
layer: 1
tier: C
template: technical
ledger_ids: [MATH-1C-024-01, MATH-1C-024-02, MATH-1C-024-03, MATH-1C-024-04, MATH-1C-024-05, MATH-1C-024-06, MATH-1C-024-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-24: Multiple Integration

> *"One integral adds along a line. A double integral adds across an area. A
> triple integral adds through a volume. The notation grows by one integral sign;
> the real work is deciding what region those signs mean."*

---

## Before You Start

**Prerequisites:** [01-09 Analytic Geometry](01-09-Analytic-Geometry.md) ·
[01-10 Areas, Volumes, and Mensuration](01-10-Areas-Volumes-and-Mensuration.md) ·
[01-11 Trigonometry](01-11-Trigonometry.md) ·
[01-19 Antiderivatives and the Definite Integral](01-19-Antiderivatives-and-the-Definite-Integral.md) ·
[01-20 Applications of the Definite Integral](01-20-Applications-of-the-Definite-Integral.md) ·
[01-21 Techniques of Integration](01-21-Techniques-of-Integration.md) ·
[01-23 Partial Derivatives and Vector Calculus](01-23-Partial-Derivatives-and-Vector-Calculus.md)

**Skip if:** You pass the Tier 1C test-out quiz and can independently set up a
nonrectangular double integral in either order, explain why polar coordinates
require the factor $r$, compute mass and centroid from a variable density, and
write cylindrical and spherical volume elements without guessing. If you can
perform the integrations but cannot draw the region that produced the limits,
do not skip this chapter.

**Time:** About 100–120 min reading and worked examples · 35–45 min review
questions · 60–90 min practice problems.

**Working convention:** Unless stated otherwise, algebraic examples are
 dimensionless. Engineering examples carry units explicitly. Angles inside
integration formulas are in **radians**. Every multiple integral begins with a
region; the bounds are a description of that region, not bookkeeping added after
the fact.

---

## On the Board Today

Apprentice, Chapter 01-19 taught you to accumulate along one independent
variable. Chapter 01-20 turned that accumulation into area, volume, work, and
other engineering totals. Chapter 01-23 then gave you surfaces, contours, and
functions of several variables.

Now we put those ideas together.

A double integral is not "doing two integrals because the problem looks harder."
It is the limit of adding contributions from **small pieces of area**. A triple
integral does the same through **small pieces of volume**. If the quantity being
added is density, you get mass. If it is height, you get volume. If it is one,
you get the size of the region itself.

That sounds almost too simple, and conceptually it is. The difficulty lives in
three places:

**First, the region.** A double integral over a rectangle has constant bounds. A
curved or triangular region usually does not. The inner limits must trace the
near and far edges of the region for each value of the outer variable.

**Second, the coordinate system.** A circular region is usually ugly in
Cartesian coordinates and natural in polar coordinates. A sphere is the same
story in three dimensions. Choosing coordinates is part of solving the problem.

**Third, the differential element.** Changing coordinates changes the size of
the little area or volume element. In polar coordinates, $dA$ is not simply
$dr\,d\theta$; it is $r\,dr\,d\theta$. That extra factor is geometry, not a
correction factor you bolt on from memory.

The habit for this chapter is therefore:

> **Draw the region → choose coordinates → write the differential element → set
> the bounds → integrate → check against geometry and units.**

Do those in that order and most multiple-integration problems stop being
mysterious.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **24.1** Interpret a double integral as accumulation over area and evaluate an
  iterated integral over a rectangular region.
* **24.2** Describe a two-dimensional region with vertical or horizontal slices
  and set up the corresponding order of integration.
* **24.3** Reverse the order of integration by redrawing and re-describing the
  same region.
* **24.4** Compute area, volume under a surface, and average value with double
  integrals.
* **24.5** Compute mass and centroid of a lamina with variable area density.
* **24.6** Convert a planar integral to polar coordinates and explain the factor
  $r$ in $dA=r\,dr\,d\theta$.
* **24.7** Interpret and evaluate a triple integral over a three-dimensional
  region.
* **24.8** Compute mass and average density from a volume density.
* **24.9** Write cylindrical and spherical coordinate transformations and their
  volume elements.
* **24.10** Use a Jacobian determinant to explain coordinate-change scale
  factors.
* **24.11** Select Cartesian, polar, cylindrical, or spherical coordinates from
  the geometry of a problem.
* **24.12** Check a multiple-integral result using units, symmetry, bounding
  geometry, or a Handbook mensuration formula.

---

## Notation Used Here

| Symbol | Meaning in this chapter | SI | USCS |
|---|---|---|---|
| $D$ | two-dimensional integration region | m² as an area when coordinates are lengths | ft² or in² |
| $E$ | three-dimensional integration region | m³ as a volume when coordinates are lengths | ft³ or in³ |
| $dA$ | differential area element | m² | ft² or in² |
| $dV$ | differential volume element | m³ | ft³ or in³ |
| $f(x,y)$ | scalar field or surface height | problem-dependent | problem-dependent |
| $A(D)$ | area of region $D$ | m² | ft² or in² |
| $V(E)$ | volume of region $E$ | m³ | ft³ or in³ |
| $\rho_A(x,y)$ | mass per unit area of a lamina | kg/m² | slug/ft² or lbm/ft² as specified |
| $\rho_V(x,y,z)$ | mass per unit volume | kg/m³ | slug/ft³ or lbm/ft³ as specified |
| $M$ | total mass | kg | slug or lbm as specified |
| $\bar x,\bar y,\bar z$ | centroid or center-of-mass coordinates | m | ft or in |
| $r,\theta$ | polar/cylindrical radius and azimuth angle | m; rad | ft or in; rad |
| $\varrho,\phi,\theta$ | spherical radius, polar angle from $+z$, azimuth angle | m; rad; rad | ft or in; rad; rad |
| $u,v,w$ | generic transformed coordinates | problem-dependent | problem-dependent |
| $J$ | Jacobian determinant or its absolute value as stated | coordinate-scale dependent | same dimensional role |

> **Collision note.** This chapter uses $\rho_A$ and $\rho_V$ for mass densities.
> The spherical radial coordinate is $\varrho$ to keep it visually distinct from
> density. The symbol $D$ means a planar region here; it is not the
> second-partial discriminant from Chapter 01-23.

> ---
> **Mentor's Margin**
>
> A multiple integral is an accounting system. The integrand tells you **what
> each tiny piece contributes**. The differential tells you **what kind of tiny
> piece you are summing**. The bounds tell you **which pieces exist**.
>
> If those three parts do not describe the same physical or geometric object,
> perfect antiderivatives will still produce the wrong answer.
>
> ---

---

## 24.1 Double Integrals — Accumulation Over Area

Start with a surface $z=f(x,y)$ above a region $D$ in the $xy$-plane. Divide
$D$ into many small patches of area $\Delta A_i$. Pick a point
$(x_i^*,y_i^*)$ in each patch. The sum

$$\sum_i f(x_i^*,y_i^*)\,\Delta A_i$$

adds one contribution from each patch. As the largest patch dimension shrinks
toward zero, the limit is the **double integral**:

$$\boxed{\iint_D f(x,y)\,dA.}$$

This is the two-dimensional version of the Riemann sum from Chapter 01-19.
The interpretation depends on the units of $f$.

| Integrand | Differential | Result |
|---|---|---|
| $1$ | area | area |
| height, m | area, m² | volume, m³ |
| area density, kg/m² | area, m² | mass, kg |
| pressure, N/m² | area, m² | force, N, when the pressure acts normally and only magnitude is required |

The unit multiplication is not optional decoration. It tells you what the
integral can possibly represent.

![FIG-01-24-001: A smooth surface z=f(x,y) above a rectangular xy-region divided into a fine grid. Several representative grid cells are extruded upward into narrow columns whose heights equal f at sample points. A sequence of three panels shows coarse columns, finer columns, and the limiting smooth volume, with the progression sum f(x_i*,y_i*) ΔA_i → double integral over D of f dA. The base patch dimensions Δx and Δy are labeled so ΔA=ΔxΔy. A footer states "double integration adds contributions over area".](../figures/FIG-01-24-001-double-integral-riemann-columns.png)

### Rectangular regions and iterated integrals

For a rectangle

$$D=\{(x,y):a\le x\le b,\ c\le y\le d\},$$

and a continuous function $f$, Fubini's theorem lets us evaluate the double
integral as an **iterated integral**:

$$\boxed{\iint_D f\,dA
=\int_a^b\int_c^d f(x,y)\,dy\,dx
=\int_c^d\int_a^b f(x,y)\,dx\,dy.}$$

For continuous functions on a rectangle, either order gives the same result.
That does **not** mean the intermediate algebra looks the same.

In

$$\int_a^b\left[\int_c^d f(x,y)\,dy\right]dx,$$

$x$ is treated as a constant while the inner $y$ integral is performed. After
that inner integral is evaluated at its $y$ limits, **no $y$ should remain**.
The resulting expression is then integrated with respect to $x$.

### Worked Example 1 — A Rectangular Region

**Given.** Evaluate

$$\iint_D (x+2y)\,dA,$$

where $0\le x\le2$ and $0\le y\le1$.

**Find.** The value of the double integral and verify it in the reverse order.

**Approach.** Integrate with respect to the inner variable while treating the
outer variable as constant. Then reverse the order as an independent algebraic
check.

**Solution.** First use $dy\,dx$:

$$\int_0^2\int_0^1(x+2y)\,dy\,dx.$$

Inner integral:

$$\int_0^1(x+2y)\,dy
=\left[xy+y^2\right]_0^1=x+1.$$

Outer integral:

$$\int_0^2(x+1)\,dx
=\left[\frac{x^2}{2}+x\right]_0^2
=2+2=\boxed{4}.$$

Reverse the order:

$$\int_0^1\int_0^2(x+2y)\,dx\,dy.$$

$$\int_0^2(x+2y)\,dx
=\left[\frac{x^2}{2}+2yx\right]_0^2
=2+4y,$$

so

$$\int_0^1(2+4y)\,dy=[2y+2y^2]_0^1=\boxed{4}.$$

**Check.** Same region, same integrand, two legal orders, same answer. ✓

> ---
> **Mentor's Margin**
>
> The inner variable is temporary. Once you evaluate its limits, it should be
> gone. If you finish the inner $dy$ integral and still have a $y$ in the
> expression, stop. You have not completed the inner integral correctly.
>
> ---

---

## 24.2 General Regions and Choosing the Order

Rectangles are the easy case because every boundary is constant. Engineering
regions are often triangles, parabolic sections, circular pieces, or irregular
areas bounded by curves.

The solution begins with a picture.

### Vertical slices — $dy\,dx$

A region that can be crossed by a single vertical segment for every
$x\in[a,b]$ can be written

$$D=\{(x,y):a\le x\le b,\ g_1(x)\le y\le g_2(x)\}.$$

Then

$$\boxed{\iint_D f\,dA
=\int_a^b\int_{g_1(x)}^{g_2(x)}f(x,y)\,dy\,dx.}$$

Read the inner limits as **bottom to top**.

### Horizontal slices — $dx\,dy$

If horizontal slices are simpler, write

$$D=\{(x,y):c\le y\le d,\ h_1(y)\le x\le h_2(y)\},$$

and

$$\boxed{\iint_D f\,dA
=\int_c^d\int_{h_1(y)}^{h_2(y)}f(x,y)\,dx\,dy.}$$

Read the inner limits as **left to right**.

The inner bounds may depend on the outer variable. The outer bounds cannot
depend on the variable that has already been integrated away.

![FIG-01-24-002: The same region between y=x² and y=2x from x=0 to x=2 is shown in two side-by-side coordinate plots. The left plot uses a representative vertical slice from y=x² up to y=2x and labels the setup 0≤x≤2, x²≤y≤2x, dy dx. The right plot uses a horizontal slice from x=y/2 to x=√y and labels 0≤y≤4, y/2≤x≤√y, dx dy. Arrows emphasize that changing integration order means re-describing the same region, not merely swapping dx and dy.](../figures/FIG-01-24-002-region-order-of-integration.png)

### Worked Example 2 — One Region, Two Orders

**Given.** The region is bounded by

$$y=x^2 \qquad\text{and}\qquad y=2x.$$

**Find.** Its area using $dy\,dx$, then set up and evaluate the same area using
$dx\,dy$.

**Approach.** Find the intersections, draw the region, and derive each set of
bounds from the drawing.

**Solution.** Intersections satisfy

$$x^2=2x\implies x(x-2)=0,$$

so $x=0$ and $x=2$. The corresponding $y$ values are 0 and 4.

### Order 1: vertical slices

For $0\le x\le2$, the parabola is below the line:

$$A=\int_0^2\int_{x^2}^{2x}1\,dy\,dx.$$

The inner integral is the vertical slice height:

$$A=\int_0^2(2x-x^2)\,dx
=\left[x^2-\frac{x^3}{3}\right]_0^2
=4-\frac83
=\boxed{\frac43}.$$

### Order 2: horizontal slices

Solve each boundary for $x$:

$$y=2x\implies x=\frac y2,$$
$$y=x^2\implies x=\sqrt y$$

for this first-quadrant region. From $y=0$ to $y=4$, the line is the left edge
and the parabola is the right edge:

$$A=\int_0^4\int_{y/2}^{\sqrt y}1\,dx\,dy.$$

Thus

$$A=\int_0^4\left(\sqrt y-\frac y2\right)dy
=\left[\frac23y^{3/2}-\frac{y^2}{4}\right]_0^4
=\frac{16}{3}-4
=\boxed{\frac43}.$$

**Check.** A rough bounding rectangle is $2\times4=8$. The curved sliver occupies
only a fraction of it, so $4/3$ is plausible. Both orders agree. ✓

### Reversing the order is geometry, not symbol swapping

Starting from

$$\int_0^2\int_{x^2}^{2x}f(x,y)\,dy\,dx,$$

writing

$$\int_{x^2}^{2x}\int_0^2f(x,y)\,dx\,dy$$

is meaningless: the outer $y$ limits contain $x$, but $x$ is the inner variable
and has no fixed value there. To reverse the order, redraw the region and derive
new bounds.

Some regions cannot be described with one set of horizontal or vertical slices.
Then split the region into two or more simple pieces and add the integrals.

---

## 24.3 Area, Volume, and Average Value

The same double integral changes meaning when the integrand changes.

### Area of a planar region

Set the integrand equal to one:

$$\boxed{A(D)=\iint_D1\,dA.}$$

The units explain it: dimensionless $1$ times area gives area.

### Volume under a surface

If $f(x,y)\ge0$ over $D$ and represents height,

$$\boxed{V=\iint_D f(x,y)\,dA.}$$

This is the direct two-dimensional version of the slicing idea from Chapter
01-20.

If the surface crosses the $xy$-plane, the integral gives **signed** volume.
To obtain total geometric volume, split the region where the sign changes and
use the appropriate positive height on each piece.

### Average value over a region

The one-variable average from Chapter 01-19 divides accumulated value by interval
length. In two dimensions, divide by region area:

$$\boxed{f_{\mathrm{avg}}
=\frac{1}{A(D)}\iint_Df(x,y)\,dA.}$$

The average has the same units as $f$.

![FIG-01-24-003: A tilted plane z=6−x−y sits above the triangular base region x≥0, y≥0, x+y≤2 in the xy-plane. A representative vertical column rises from a small base patch dA to the plane and is labeled dV=z dA. The three triangular base edges and the plane intercept directions are labeled. A second annotation shows total volume as the sum of all columns and average height as V divided by base area.](../figures/FIG-01-24-003-volume-under-surface.png)

### Worked Example 3 — Volume Under a Plane

**Given.** A roof height in metres is modeled by

$$z=6-x-y$$

above the triangular floor region

$$x\ge0,\qquad y\ge0,\qquad x+y\le2,$$

with $x$ and $y$ measured in metres.

**Find.** (a) the volume beneath the roof and above the floor, and (b) the
average roof height.

**Approach.** Describe the triangular base with vertical slices, integrate the
height over area, then divide by base area for the average.

**Solution.** The region is

$$0\le x\le2,\qquad0\le y\le2-x.$$

The volume is

$$V=\int_0^2\int_0^{2-x}(6-x-y)\,dy\,dx.$$

Inner integral:

$$\int_0^{2-x}(6-x-y)\,dy
=(6-x)(2-x)-\frac12(2-x)^2.$$

Simplifying,

$$(6-x)(2-x)-\frac12(2-x)^2
=10-6x+\frac{x^2}{2}.$$

Then

$$V=\int_0^2\left(10-6x+\frac{x^2}{2}\right)dx
=\left[10x-3x^2+\frac{x^3}{6}\right]_0^2$$

$$=20-12+\frac83\cdot\frac12
=8+\frac43
=\boxed{\frac{28}{3}\ \mathrm{m^3}}
\approx9.33\ \mathrm{m^3}.$$

The triangular base area is

$$A(D)=\frac12(2\ \mathrm m)(2\ \mathrm m)=2\ \mathrm{m^2}.$$

Therefore

$$z_{\mathrm{avg}}
=\frac{V}{A(D)}
=\frac{28/3}{2}
=\boxed{\frac{14}{3}\ \mathrm m}
\approx4.67\ \mathrm m.$$

**Check.** Over the triangle, the roof height ranges from 6 m at the origin to
4 m along $x+y=2$. An average of 4.67 m lies between those limits. The volume
must therefore lie between $4(2)=8$ m³ and $6(2)=12$ m³; $9.33$ m³ does. ✓

> ---
> **Mentor's Margin**
>
> A multiple integral should survive a crude bounding check. If the base has
> area 2 m² and every height lies between 4 and 6 m, then the volume **must** lie
> between 8 and 12 m³. That check takes five seconds and catches bad limits,
> wrong signs, and missing factors before they leave the page.
>
> ---

---

## 24.4 Mass, Moments, and Centroid of a Lamina

A **lamina** is a thin two-dimensional body. If its area density varies with
position, write $\rho_A(x,y)$ with units such as kg/m².

A small patch contributes approximately

$$dM=\rho_A(x,y)\,dA.$$

Integrating over the whole region gives mass:

$$\boxed{M=\iint_D\rho_A(x,y)\,dA.}$$

The center of mass is a density-weighted average of position:

$$\boxed{\bar x=\frac1M\iint_Dx\rho_A\,dA,
\qquad
\bar y=\frac1M\iint_Dy\rho_A\,dA.}$$

For uniform density, the constant density cancels and the center of mass becomes
the geometric centroid:

$$\bar x=\frac1A\iint_Dx\,dA,
\qquad
\bar y=\frac1A\iint_Dy\,dA.$$

This is the continuous version of the area-weighted centroid method from Chapter
01-10 and the integral centroid formulas from Chapter 01-20.

![FIG-01-24-004: A rectangular lamina from x=0 to 2 and y=0 to 1 is shaded progressively darker toward increasing x to represent area density ρ_A=2(1+x). The geometric center at (1,0.5) is marked lightly, while the mass centroid at (7/6,0.5) is marked farther to the right. A small patch dA carries label dM=ρ_A dA. Horizontal symmetry is emphasized to show why y-bar remains 0.5 even though x-bar shifts.](../figures/FIG-01-24-004-variable-density-centroid.png)

### Worked Example 4 — Variable-Density Plate

**Given.** A thin rectangular plate occupies

$$0\le x\le2\ \mathrm m,
\qquad0\le y\le1\ \mathrm m,$$

with area density

$$\rho_A(x,y)=2(1+x)\ \mathrm{kg/m^2},$$

where the numerical value of $x$ is measured in metres in the stated formula.

**Find.** Its total mass and center of mass.

**Approach.** Integrate density for mass, then integrate position times density
for the first moments.

**Solution.** Mass:

$$M=\int_0^2\int_0^1 2(1+x)\,dy\,dx.$$

The $y$ integration contributes a factor of 1 m numerically:

$$M=\int_0^2 2(1+x)\,dx
=2\left[x+\frac{x^2}{2}\right]_0^2
=2(2+2)=\boxed{8\ \mathrm{kg}}.$$

For $\bar x$:

$$\bar x
=\frac1{8}\int_0^2\int_0^1x\,2(1+x)\,dy\,dx$$

$$=\frac14\int_0^2(x+x^2)\,dx
=\frac14\left[\frac{x^2}{2}+\frac{x^3}{3}\right]_0^2$$

$$=\frac14\left(2+\frac83\right)
=\boxed{\frac76\ \mathrm m}
\approx1.17\ \mathrm m.$$

For $\bar y$:

$$\bar y
=\frac1{8}\int_0^2\int_0^1y\,2(1+x)\,dy\,dx.$$

Because the density does not vary with $y$, symmetry already predicts
$\bar y=0.5$ m. Evaluating confirms it:

$$\boxed{\bar y=\frac12\ \mathrm m}.$$

**Check.** Uniform density would put $\bar x$ at 1 m. The plate gets denser as
$x$ increases, so the mass centroid must move right. $7/6\approx1.17$ m does. ✓

### Distributed quantities use the same pattern

The structure is broader than mass:

$$\text{total}=\iint_D(\text{quantity per area})\,dA.$$

Pressure load, pollutant deposition, heat generation per area, charge per area,
and probability density all use the same mathematical skeleton when their models
are stated appropriately. The units tell you what total you are computing.

---

## 24.5 Polar Coordinates and the Area Factor

Cartesian coordinates are built for straight boundaries parallel to the axes.
Circular geometry usually asks for polar coordinates:

$$\boxed{x=r\cos\theta,\qquad y=r\sin\theta.}$$

Also,

$$r^2=x^2+y^2.$$

The critical fact is the area element:

$$\boxed{dA=r\,dr\,d\theta.}$$

### Where the factor $r$ comes from

Take a tiny polar patch. Its radial thickness is approximately $dr$. Its angular
side is not $d\theta$ as a length; an angle has no length. At radius $r$, a small
arc length is

$$r\,d\theta.$$

So the patch area is approximately

$$dA\approx(dr)(r\,d\theta)=r\,dr\,d\theta.$$

The farther the patch lies from the origin, the wider the same angular slice
becomes. The factor $r$ accounts for that widening.

![FIG-01-24-005: A small annular-sector area element in polar coordinates is magnified. Its radial thickness is labeled dr and its curved tangential dimension is labeled approximately r dθ. The product r dr dθ is shown as the differential area. Concentric circles and two radial rays illustrate that equal angular widths become physically wider as radius increases. A comparison inset shows that writing dr dθ alone incorrectly treats an angle as a length.](../figures/FIG-01-24-005-polar-area-element.png)

### Common polar regions

**Disk of radius $R$:**

$$0\le r\le R,\qquad0\le\theta\le2\pi.$$

**Annulus $a\le r\le b$:**

$$a\le r\le b,\qquad0\le\theta\le2\pi.$$

**Sector from $\theta_1$ to $\theta_2$:**

$$0\le r\le R,
\qquad\theta_1\le\theta\le\theta_2.$$

Angles are in radians because $s=r\theta$ and therefore the derivation of
$r\,d\theta$ assumes radian measure.

### Worked Example 5 — A Radially Symmetric Integral

**Given.** Let $D$ be the disk $x^2+y^2\le4$.

**Find.**

$$I=\iint_D(x^2+y^2)\,dA,$$

then find the average value of $x^2+y^2$ over the disk.

**Approach.** The region and integrand both depend naturally on radius. Convert
$x^2+y^2$ to $r^2$ and include the polar area factor $r$.

**Solution.** The disk has

$$0\le r\le2,
\qquad0\le\theta\le2\pi.$$

Thus

$$I=\int_0^{2\pi}\int_0^2r^2(r\,dr\,d\theta)
=\int_0^{2\pi}\int_0^2r^3\,dr\,d\theta.$$

$$I=\int_0^{2\pi}\left[\frac{r^4}{4}\right]_0^2d\theta
=\int_0^{2\pi}4\,d\theta
=\boxed{8\pi}.$$

The disk area is $4\pi$, so

$$\left(x^2+y^2\right)_{\mathrm{avg}}
=\frac{8\pi}{4\pi}=\boxed{2}.$$

**Check.** $r^2$ ranges from 0 to 4. An average of 2 lies inside that range. ✓

**Second check.** Compute the area itself in polar coordinates:

$$A=\int_0^{2\pi}\int_0^2r\,dr\,d\theta
=2\pi\left[\frac{r^2}{2}\right]_0^2
=4\pi,$$

matching the circle formula from the Handbook mensuration table. ✓

> ---
> **Mentor's Margin**
>
> The missing-$r$ error is dangerous because the resulting integral often still
> looks clean. Before integrating in polar coordinates, point to the differential
> element and say: **"area gets wider with radius."** If the $r$ is not there,
> your formula does not know that.
>
> ---

---

## 24.6 Triple Integrals — Accumulation Through Volume

A triple integral adds contributions over a three-dimensional region $E$:

$$\boxed{\iiint_Ef(x,y,z)\,dV.}$$

As before, the integrand controls the meaning.

$$\boxed{V(E)=\iiint_E1\,dV}$$

and for volume density $\rho_V$,

$$\boxed{M=\iiint_E\rho_V\,dV.}$$

A Cartesian volume element is

$$\boxed{dV=dx\,dy\,dz}$$

up to the chosen order of integration. On a rectangular box with constant
limits, any order is legal for a continuous integrand. On a general solid, the
bounds must describe how one-dimensional slices fill the solid.

![FIG-01-24-006: A three-dimensional solid is shown sliced first into slabs, then a selected slab into strips, and finally a selected strip into a tiny rectangular box. The differential box dimensions dx, dy, dz are labeled and the progression "solid → slab → strip → dV" is shown beside the nested integral. A second small panel shows that after the innermost z integration, z disappears and the result is a function only of the remaining outer variables.](../figures/FIG-01-24-006-triple-integral-slices.png)

### Center of mass in three dimensions

For total mass $M$,

$$\boxed{\bar x=\frac1M\iiint_Ex\rho_V\,dV,
\quad
\bar y=\frac1M\iiint_Ey\rho_V\,dV,
\quad
\bar z=\frac1M\iiint_Ez\rho_V\,dV.}$$

For uniform density, these reduce to the geometric centroid formulas.

### Worked Example 6 — Density Varying with Height

**Given.** A rectangular solid occupies

$$0\le x\le2\ \mathrm m,
\quad0\le y\le1\ \mathrm m,
\quad0\le z\le1\ \mathrm m.$$

Its volume density is

$$\rho_V(z)=800\ \mathrm{kg/m^3}
+(100\ \mathrm{kg/m^4})z.$$

**Find.** The total mass and vertical center-of-mass coordinate $\bar z$.

**Approach.** Density varies only with $z$, so the $x$ and $y$ integrals produce
the constant base area. Then compute the first moment in $z$.

**Solution.** Mass:

$$M=\int_0^2\int_0^1\int_0^1
\left(800+100z\right)\,dz\,dy\,dx,$$

where the numerical coefficients carry the units shown above.

The $z$ integration gives

$$\int_0^1(800+100z)\,dz=800+50=850\ \mathrm{kg/m^2}$$

for a one-metre vertical column. Multiplying by the 2 m² base area gives

$$\boxed{M=1700\ \mathrm{kg}}.$$

Now the first moment about the $xy$-plane is

$$M\bar z=\iiint_Ez\rho_V\,dV.$$

The base-area factor is again 2 m²:

$$M\bar z
=2\int_0^1z(800+100z)\,dz$$

$$=2\left[400z^2+\frac{100}{3}z^3\right]_0^1
=2\left(400+\frac{100}{3}\right)
=\frac{2600}{3}\ \mathrm{kg\,m}.$$

Therefore

$$\bar z
=\frac{2600/3}{1700}
=\boxed{0.5098\ \mathrm m}.$$

**Check.** Uniform density would put the centroid at 0.500 m. Density increases
with $z$, so the center of mass must shift upward slightly. 0.5098 m does. ✓

The average density is

$$\rho_{\mathrm{avg}}=\frac{M}{V}
=\frac{1700\ \mathrm{kg}}{2\ \mathrm{m^3}}
=850\ \mathrm{kg/m^3},$$

which lies between the bottom value 800 and top value 900 kg/m³. ✓

---

## 24.7 Cylindrical, Spherical, and General Coordinate Changes

Choosing a coordinate system is an engineering decision: use coordinates that
make the boundaries and the integrand simpler **together**.

### Cylindrical coordinates

Cylindrical coordinates are polar coordinates with height added:

$$\boxed{x=r\cos\theta,
\qquad y=r\sin\theta,
\qquad z=z.}$$

The volume element is

$$\boxed{dV=r\,dr\,d\theta\,dz}$$

with order rearranged as convenient, provided the bounds match that order.

Use cylindrical coordinates when the geometry involves cylinders, circular
pipes, disks extruded through height, or expressions such as $x^2+y^2$.

### Spherical coordinates

This chapter uses the convention

$$\boxed{x=\varrho\sin\phi\cos\theta,}$$
$$\boxed{y=\varrho\sin\phi\sin\theta,}$$
$$\boxed{z=\varrho\cos\phi,}$$

where

* $\varrho\ge0$ is distance from the origin,
* $0\le\phi\le\pi$ is measured down from the positive $z$-axis,
* $0\le\theta<2\pi$ is the azimuth angle in the $xy$-plane.

The volume element is

$$\boxed{dV=\varrho^2\sin\phi\,d\varrho\,d\phi\,d\theta.}$$

The $\varrho^2$ appears because two tangential dimensions grow with radius. The
$\sin\phi$ appears because circles of latitude shrink toward the $z$-axis.

Different textbooks sometimes swap the names $\phi$ and $\theta$. The geometry
matters more than the letter. Always identify **which angle is measured from the
positive $z$-axis** before using a spherical formula.

![FIG-01-24-007: Two side-by-side three-dimensional differential elements. Left: a cylindrical wedge with dimensions dr, r dθ, and dz, labeled dV=r dr dθ dz. Right: a spherical wedge with radial thickness dρ, tangential dimensions ρ dφ and ρ sinφ dθ, labeled dV=ρ² sinφ dρ dφ dθ. The spherical diagram explicitly marks φ from the positive z-axis and θ as azimuth in the xy-plane. A footer connects both scale factors to the Jacobian idea: transformed coordinate grids stretch physical area and volume.](../figures/FIG-01-24-007-cylindrical-spherical-elements.png)

### The Jacobian — the general scale factor

Polar, cylindrical, and spherical factors are examples of a broader rule. If

$$x=x(u,v),\qquad y=y(u,v),$$

then a small rectangle $du\,dv$ in the new coordinates generally becomes a
small parallelogram in the $xy$-plane. Its area scale factor is the absolute
value of the **Jacobian determinant**:

$$\boxed{dA=
\left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv}$$

where

$$\frac{\partial(x,y)}{\partial(u,v)}
=
\begin{vmatrix}
\dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v}\\[2mm]
\dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v}
\end{vmatrix}.$$

For polar coordinates,

$$x=r\cos\theta,
\qquad y=r\sin\theta,$$

so

$$\frac{\partial(x,y)}{\partial(r,\theta)}
=
\begin{vmatrix}
\cos\theta & -r\sin\theta\\
\sin\theta & r\cos\theta
\end{vmatrix}
=r(\cos^2\theta+\sin^2\theta)=r.$$

That reproduces $dA=r\,dr\,d\theta$ from the geometric derivation.

In three dimensions, the same idea uses a $3\times3$ Jacobian determinant. For
standard cylindrical and spherical coordinates, use the established volume
elements rather than re-deriving the determinant under exam time pressure.

### Worked Example 7 — Recovering the Sphere Volume

**Given.** A sphere of radius $a$ centered at the origin.

**Find.** Its volume using a triple integral in spherical coordinates.

**Approach.** The boundaries are constant in spherical coordinates, making them
more natural than Cartesian square roots.

**Solution.** The sphere is

$$0\le\varrho\le a,
\qquad0\le\phi\le\pi,
\qquad0\le\theta\le2\pi.$$

Thus

$$V=\int_0^{2\pi}\int_0^\pi\int_0^a
\varrho^2\sin\phi\,d\varrho\,d\phi\,d\theta.$$

Separate the factors:

$$V=
\left[\int_0^a\varrho^2d\varrho\right]
\left[\int_0^\pi\sin\phi\,d\phi\right]
\left[\int_0^{2\pi}d\theta\right].$$

$$V=\left(\frac{a^3}{3}\right)(2)(2\pi)
=\boxed{\frac43\pi a^3}.$$

**Check.** This exactly matches the sphere-volume formula in the Handbook
mensuration table. ✓

### Coordinate-selection workflow

| Geometry / algebra | Usually try first | Why |
|---|---|---|
| rectangle, box, planes parallel to coordinate axes | Cartesian | constant or simple linear bounds |
| disk, annulus, circular sector, $x^2+y^2$ | polar | circular boundaries become constant $r$ |
| cylinder, circular pipe, axial symmetry in 3D | cylindrical | polar cross-section plus $z$ |
| sphere, ball, radial 3D field $x^2+y^2+z^2$ | spherical | spherical boundary becomes constant $\varrho$ |

Do not choose a coordinate system because its name matches the object vaguely.
Choose it because it simplifies **both** the region and the integrand enough to
pay for the transformation.

> ---
> **Mentor's Margin**
>
> There is no prize for staying Cartesian. If a circle forces you to carry
> $\sqrt{R^2-x^2}$ through three lines of algebra, ask whether the geometry is
> telling you to use polar coordinates.
>
> There is also no prize for changing coordinates unnecessarily. A rectangular
> box with a polynomial density is already simple. Transformation is a tool, not
> a ritual.
>
> ---

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. The Mathematics section begins on printed
> page 36. Standard mensuration formulas for areas and volumes appear on printed
> pages 41–44. The definite-integral definition and the standard one-variable
> integration methods appear in the Integral Calculus material beginning around
> printed page 49. A search of the supplied edition's extracted text and relevant
> Mathematics pages did **not locate general double-integral, triple-integral,
> Jacobian, polar-area-element, cylindrical-volume-element, or spherical-volume-
> element formulas**. "Not located" refers to this supplied edition and review;
> it is not a claim about every edition or every discipline-specific formula.

The Handbook is still useful in this chapter because it gives exact independent
checks for many standard regions. Use its tables to check a multiple integral,
not as evidence that the setup procedure has been supplied for you.

| Handbook material | Printed pages | How it helps here |
|---|---:|---|
| Mensuration of Areas and Volumes | 41–44 | Checks areas and volumes of circles, spheres, cylinders, cones, and other standard shapes |
| Integral Calculus | about 49 onward | Supplies the definite-integral foundation and common one-variable integration methods used inside iterated integrals |
| Tables and formulas elsewhere in the Handbook | problem-dependent | May supply a physical density, geometry, or constitutive model; the multiple-integral setup remains your job unless the question provides it |

**Methods to know from this guide:**

- how bounds describe a region,
- vertical versus horizontal slicing,
- reversing integration order by redrawing the region,
- $A=\iint_D1\,dA$,
- $V=\iint_Df\,dA$ for a nonnegative height,
- average value over an area or volume,
- variable-density mass and centroid integrals,
- $dA=r\,dr\,d\theta$,
- cylindrical and spherical volume elements,
- the role of a Jacobian as a geometric scale factor,
- choosing coordinates from geometry.

**What to look up rather than memorize:** standard-shape areas and volumes that
are already tabulated. If the problem asks only for the volume of a sphere,
using the Handbook's $4\pi a^3/3$ is faster than performing a triple integral.
If the problem asks for a distributed quantity inside that sphere, the multiple
integral may be unavoidable.

**Notation translation.** The Handbook's geometric formulas use their own local
letters for radii, dimensions, and volumes. This chapter reserves $r$ for the
polar/cylindrical radius and $\varrho$ for spherical radius. Always map symbols by
meaning before substituting.

---

## Where This Goes Wrong

**Writing limits before drawing the region.** The bounds are the region. Sketch
first, then write the limits from the sketch.

**Treating a double integral as two unrelated integrations.** The inner integral
creates a function of the outer variable. Each stage describes the same region,
not a new problem.

**Leaving the inner variable behind.** After evaluating an inner $dy$ integral,
no $y$ should remain. The same rule applies to every inner variable.

**Putting the wrong curves in the wrong order.** For $dy\,dx$, limits go bottom
to top. For $dx\,dy$, they go left to right. Reversing them changes the sign.

**"Reversing the order" by swapping $dx$ and $dy$.** You must derive a new
geometric description. The old functional bounds generally cannot be reused.

**Failing to split a region.** If a horizontal or vertical line crosses the region
in two separate pieces, one set of inner limits is not enough.

**Forgetting that volume under a surface is signed if the height changes sign.**
Split at the zero set when total geometric volume is requested.

**Forgetting to divide by area or volume for an average.** The integral gives the
total. The average is total divided by the measure of the region.

**Dropping density units.** kg/m² times m² gives kg. kg/m³ times m³ gives kg.
If the units do not collapse to the requested total, the setup is wrong.

**Using geometric centroid formulas for a nonuniform density.** A denser side
pulls the mass centroid toward it. Weight position by density.

**Forgetting the polar $r$.** $dA=dr\,d\theta$ is dimensionally wrong and
geometrically wrong. Use $r\,dr\,d\theta$.

**Using degrees for $\theta$.** The arc relation $ds=r\,d\theta$ assumes radians.
Multiple-integral angular limits therefore use radians.

**Transforming the bounds but not the integrand.** If $x^2+y^2=r^2$, replace it.
Do not carry Cartesian variables into a polar integral unless you have explicitly
written them as functions of the new coordinates.

**Transforming the integrand but not the differential.** The Jacobian factor is
part of the coordinate change. Leaving it out changes the physical size of each
area or volume element.

**Mixing spherical-angle conventions.** Some sources measure $\phi$ from the
$z$-axis; others use it as azimuth. State the convention before using
$\varrho^2\sin\phi$.

**Using symmetry the integrand does not have.** A symmetric region does not make
an asymmetric density symmetric. Check both the region and the integrand before
halving or doubling an integral.

**Ignoring an easier Handbook formula.** If the task is merely the area of a
circle or volume of a sphere, use the reference table. Integration is justified
when the distribution, bounds, or requested derivation requires it.

---

## Key Terms

| Term | Definition |
|---|---|
| Double integral | Limit of sums of an integrand times small area elements over a planar region |
| Iterated integral | Multiple integral evaluated one variable at a time |
| Fubini's theorem | Under suitable conditions, permits evaluation of a multiple integral as iterated integrals and interchange of order |
| Type-I / vertically simple region | Region described by constant $x$ limits and $y$ between two functions of $x$ |
| Type-II / horizontally simple region | Region described by constant $y$ limits and $x$ between two functions of $y$ |
| Order of integration | Sequence in which the variables are integrated |
| Average value over a region | Integral of a field divided by the area or volume of its region |
| Lamina | Thin two-dimensional body modeled by area density |
| Area density | Mass per unit area, $\rho_A$ |
| Volume density | Mass per unit volume, $\rho_V$ |
| Center of mass | Density-weighted average position of a body |
| Polar coordinates | Planar coordinates $(r,\theta)$ with $x=r\cos\theta$, $y=r\sin\theta$ |
| Jacobian | Determinant measuring the local area or volume scale change under a coordinate transformation |
| Triple integral | Limit of sums of an integrand times small volume elements over a solid region |
| Cylindrical coordinates | Three-dimensional coordinates $(r,\theta,z)$ built from polar coordinates and height |
| Spherical coordinates | Three-dimensional coordinates based on radial distance and two angles |
| Differential area element | Infinitesimal area measure, such as $dx\,dy$ or $r\,dr\,d\theta$ |
| Differential volume element | Infinitesimal volume measure, such as $dx\,dy\,dz$, $r\,dr\,d\theta\,dz$, or $\varrho^2\sin\phi\,d\varrho\,d\phi\,d\theta$ |

---

## Review Questions

Answer conceptual questions before using a calculator. For every calculation,
state the region or solid before integrating.

### Conceptual

1. Explain what the integrand, differential element, and bounds each contribute
to the meaning of a double integral.
2. Why can two different orders of integration represent the same region? What
must be changed when the order is reversed?
3. State the vertical-slice and horizontal-slice templates for a planar region.
What geometric direction do the inner limits follow in each?
4. Explain why $A(D)=\iint_D1\,dA$.
5. How is average value over a region related to total accumulation? Why does the
average have the same units as the integrand?
6. Explain why a nonuniform density can move the mass centroid away from the
geometric centroid.
7. Derive the polar area factor $r$ using the approximate dimensions of a small
annular sector.
8. State the cylindrical and spherical volume elements used in this chapter.
What does each extra scale factor represent geometrically?
9. What is a Jacobian, and why is its absolute value used as an area scale factor?
10. Give one example each where Cartesian, polar, cylindrical, and spherical
coordinates are the natural first choice. State why.

### Calculation

11. Evaluate
$$\int_0^2\int_0^1(x+3y)\,dy\,dx.$$

12. For the region bounded by $y=x^2$ and $y=2x$, write area integrals in both
orders and evaluate the area.

13. Find the volume under $z=4-x-y$ above the triangle
$x\ge0$, $y\ge0$, $x+y\le2$.

14. Find the average value of $x^2+y^2$ over the disk $x^2+y^2\le9$.

15. A lamina occupies $0\le x\le2$, $0\le y\le1$ and has
$\rho_A=1+x$ in consistent mass-per-area units. Find total mass and center of
mass.

16. Evaluate
$$\int_0^1\int_0^2\int_0^3(x+y+z)\,dz\,dy\,dx.$$

17. Over the solid cylinder $0\le r\le2$, $0\le\theta\le2\pi$,
$0\le z\le3$, evaluate $\iiint_E z\,dV$ and find the average value of $z$.

18. Use spherical coordinates to show that a uniform sphere of radius $a$ and
constant density $\rho_0$ has mass $\frac43\pi a^3\rho_0$.

19. Under the transformation
$$x=u+v,\qquad y=u-v,$$
find the Jacobian magnitude and the area in the $xy$-plane corresponding to
$0\le u\le1$, $0\le v\le2$.

### Multiple Choice

20. In polar coordinates, the correct area element is:
A) $dr\,d\theta$  B) $r\,dr\,d\theta$  C) $r^2dr\,d\theta$  D) $\sin\theta\,dr\,d\theta$.

21. For $dy\,dx$ over a vertically simple region, the inner limits normally run:
A) left to right  B) right to left  C) bottom to top  D) outer to inner.

22. The integral $\iint_D1\,dA$ gives:
A) perimeter  B) area  C) average height  D) mass regardless of density.

23. A mass centroid differs from a geometric centroid when:
A) the region has curved edges  B) density varies with position
C) Cartesian coordinates are used  D) the region is symmetric.

24. For cylindrical coordinates, the volume element is:
A) $dr\,d\theta\,dz$  B) $r\,dr\,d\theta\,dz$
C) $r^2\sin\theta\,dr\,d\theta\,dz$  D) $dx\,dy\,dz/r$.

25. With $\phi$ measured from the positive $z$-axis, the spherical volume
element is:
A) $\varrho\,d\varrho\,d\phi\,d\theta$
B) $\varrho^2\,d\varrho\,d\phi\,d\theta$
C) $\varrho^2\sin\phi\,d\varrho\,d\phi\,d\theta$
D) $\varrho^2\cos\phi\,d\varrho\,d\phi\,d\theta$.

26. Reversing an integration order generally requires:
A) only swapping $dx$ and $dy$
B) changing only the outer bounds
C) re-describing the same region with new bounds
D) changing the integrand's sign.

27. A Jacobian is needed in a coordinate transformation because:
A) the function becomes discontinuous
B) transformed coordinate cells generally have different physical area or volume
C) all trigonometric substitutions require one
D) it changes the units of the physical quantity being integrated.

---

## Answer Key with Explanations

### Conceptual

1. The integrand is the contribution per differential element, the differential
element says whether the accumulation is over length, area, or volume and includes
any coordinate scale factor, and the bounds select which elements belong to the
region. All three must describe the same model. (§24.1)

2. A region is a geometric set independent of the order used to sweep through it.
Changing order changes which variable defines the inner slice, so the bounds must
be re-derived from the region. The integrand represents the same physical field.
(§24.2)

3. Vertical: $a\le x\le b$, $g_1(x)\le y\le g_2(x)$, with inner limits bottom to
top. Horizontal: $c\le y\le d$, $h_1(y)\le x\le h_2(y)$, with inner limits left
to right. (§24.2)

4. Each area patch contributes $1\cdot dA=dA$. Adding all patches therefore
returns the region's total area. (§24.3)

5. Average value equals total accumulated field divided by region area or volume.
Dividing units such as $(\mathrm K)(\mathrm{m^2})$ by $\mathrm{m^2}$ returns K,
so the average has the field's units. (§24.3)

6. Center of mass weights each position by local density. A denser side contributes
more mass per area and therefore more strongly to the weighted average. (§24.4)

7. A small polar patch has radial side $dr$ and tangential side approximately
$r\,d\theta$, so $dA\approx(dr)(r\,d\theta)=r\,dr\,d\theta$. (§24.5)

8. Cylindrical: $dV=r\,dr\,d\theta\,dz$. Spherical:
$dV=\varrho^2\sin\phi\,d\varrho\,d\phi\,d\theta$. The factors account for the
physical stretching of angular coordinate lines with radius and latitude.
(§24.7)

9. A Jacobian determinant measures the local linear map from transformed
coordinate increments to physical coordinate increments. Its magnitude is used
because physical area is nonnegative even if the coordinate transformation
reverses orientation. (§24.7)

10. Cartesian: a box with planar coordinate-aligned faces. Polar: a disk.
Cylindrical: a pipe or circular cylinder. Spherical: a ball or radially symmetric
3D field. Each choice turns natural boundaries into simple coordinate limits.
(§24.7)

### Calculation

11. Inner integration gives

$$\int_0^1(x+3y)dy=x+\frac32.$$

Then

$$\int_0^2\left(x+\frac32\right)dx
=\left[\frac{x^2}{2}+\frac32x\right]_0^2
=2+3=\boxed{5}.$$

12. Vertical order:

$$A=\int_0^2\int_{x^2}^{2x}1\,dy\,dx.$$

Horizontal order:

$$A=\int_0^4\int_{y/2}^{\sqrt y}1\,dx\,dy.$$

Both give

$$\boxed{A=\frac43}.$$

13. Use $0\le x\le2$, $0\le y\le2-x$:

$$V=\int_0^2\int_0^{2-x}(4-x-y)\,dy\,dx
=\boxed{\frac{16}{3}}.$$

The surface height ranges from 2 to 4 over a base area of 2, so a volume
$5.333\ldots$ lies between the bounds 4 and 8. ✓

14. In polar coordinates,

$$\iint_D(x^2+y^2)dA
=\int_0^{2\pi}\int_0^3r^3drd\theta
=\frac{81\pi}{2}.$$

The disk area is $9\pi$, so

$$\boxed{f_{\mathrm{avg}}=\frac{81\pi/2}{9\pi}=\frac92=4.5}.$$

15. Mass:

$$M=\int_0^2\int_0^1(1+x)\,dy\,dx
=\left[x+\frac{x^2}{2}\right]_0^2=\boxed{4}.$$

Then

$$\bar x=\frac1{4}\int_0^2x(1+x)dx
=\frac14\left(2+\frac83\right)
=\boxed{\frac76},$$

and symmetry in $y$ gives

$$\boxed{\bar y=\frac12}.$$

16. The rectangular box has side lengths 1, 2, 3 and volume 6. Directly,

$$\int_0^1\int_0^2\int_0^3(x+y+z)\,dz\,dy\,dx=\boxed{18}.$$

A check uses averages: $\bar x=0.5$, $\bar y=1$, $\bar z=1.5$, so the average
integrand is 3; $3(6)=18$. ✓

17. Cylindrical volume element gives

$$\iiint_Ez\,dV
=\int_0^{2\pi}\int_0^2\int_0^3zr\,dz\,dr\,d\theta
=\boxed{18\pi}.$$

The cylinder volume is $\pi(2)^2(3)=12\pi$, so

$$\boxed{z_{\mathrm{avg}}=\frac{18\pi}{12\pi}=1.5}.$$

18. With constant density,

$$M=\rho_0\int_0^{2\pi}\int_0^\pi\int_0^a
\varrho^2\sin\phi\,d\varrho\,d\phi\,d\theta$$

$$=\rho_0\left(\frac{a^3}{3}\right)(2)(2\pi)
=\boxed{\frac43\pi a^3\rho_0}.$$

19. The Jacobian is

$$\frac{\partial(x,y)}{\partial(u,v)}
=\begin{vmatrix}1&1\\1&-1\end{vmatrix}=-2,$$

so $|J|=2$. The $uv$ rectangle has area $1\times2=2$, hence the transformed
area is

$$\boxed{A=\int_0^1\int_0^2 2\,dv\,du=4}.$$

### Multiple Choice

20. **B.** Polar coordinate cells widen with radius, so $dA=r\,dr\,d\theta$.
21. **C.** A vertical slice enters at the lower boundary and exits at the upper.
22. **B.** Summing $1\cdot dA$ over a region returns its area.
23. **B.** Variable density changes the weighting of position.
24. **B.** Cylindrical coordinates inherit the polar factor $r$ and add $dz$.
25. **C.** With $\phi$ from $+z$, the standard element is
$\varrho^2\sin\phi\,d\varrho\,d\phi\,d\theta$.
26. **C.** Reversing order is a new geometric description of the same region.
27. **B.** A transformed coordinate rectangle does not generally have physical
area $du\,dv$; the Jacobian supplies the local scale factor.

---

## Practice Problems

Work these on paper before reading the solutions. Draw every nonrectangular region.

1. **Rectangular accumulation.** Evaluate
   $$\int_0^3\int_0^2(2x+y)\,dy\,dx.$$
   Then divide by the rectangle's area to find the average value of $2x+y$.

2. **Reverse the order.** Let
   $$D=\{(x,y):0\le x\le1,\ x^2\le y\le x\}.$$
   (a) Sketch $D$. (b) Rewrite $\iint_Df\,dA$ in the order $dx\,dy$.
   (c) Find the area of $D$.

3. **Volume and average height.** Above the triangular region
   $x\ge0$, $y\ge0$, $x+y\le3$ m, a surface has height
   $z=5\ \mathrm m-(0.5)x-(0.5)y$, with $x,y$ in metres. Find the volume and
   average height.

4. **Variable-density lamina.** A plate occupies
   $0\le x\le1$ m, $0\le y\le2$ m and has
   $$\rho_A=(3+2x)\ \mathrm{kg/m^2}.$$
   Find mass and center of mass.

5. **Annulus.** Use polar coordinates to find the area of
   $$1\le x^2+y^2\le9.$$
   Verify against the difference of two circle areas.

6. **Radial density.** A circular lamina of radius 2 m has area density
   $$\rho_A(r)=(4+r)\ \mathrm{kg/m^2}.$$
   Find its mass and explain qualitatively whether its center of mass moves away
   from the center.

7. **Three-dimensional density.** A $1\times1\times2$ m box occupies
   $0\le x\le1$, $0\le y\le1$, $0\le z\le2$ and has
   $$\rho_V(z)=(600+50z)\ \mathrm{kg/m^3},$$
   with $z$ in metres in the stated model. Find total mass and $\bar z$.

8. **Cylindrical coordinates.** Find
   $$\iiint_E(x^2+y^2)\,dV$$
   over the cylinder $x^2+y^2\le4$, $0\le z\le5$.

9. **Spherical shell.** Use spherical coordinates to find the volume between
   concentric spheres of radii $a$ and $b$, where $0<a<b$.

10. **A nonstandard change of variables.** The ellipse
    $$\frac{x^2}{4}+\frac{y^2}{9}\le1$$
    is generated by $x=2u$, $y=3v$ from the unit disk $u^2+v^2\le1$.
    Use the Jacobian to recover the ellipse area.

---

## Practice Problem Solutions

1. **Approach.** Integrate over the rectangle, then divide by its area.

   $$I=\int_0^3\int_0^2(2x+y)\,dy\,dx.$$

   Inner integration gives $4x+2$, so

   $$I=\int_0^3(4x+2)dx=[2x^2+2x]_0^3=18+6=\boxed{24}.$$

   Rectangle area is $3\times2=6$, so

   $$\boxed{f_{\mathrm{avg}}=24/6=4}.$$

   **Check:** the function is linear; at the rectangle center $(1.5,1)$ its
   value is $2(1.5)+1=4$, matching the average of a linear function over a
   symmetric rectangle. ✓

2. **Approach.** The curves are $y=x^2$ and $y=x$ between 0 and 1. For horizontal
   slices, solve both for $x$.

   From $y=x$, $x=y$. From $y=x^2$ in the first quadrant, $x=\sqrt y$.
   Thus

   $$0\le y\le1,
   \qquad y\le x\le\sqrt y,$$

   so

   $$\boxed{\iint_Df\,dA
   =\int_0^1\int_y^{\sqrt y}f(x,y)\,dx\,dy}.$$

   Area:

   $$A=\int_0^1(x-x^2)dx
   =\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1
   =\boxed{\frac16}.$$

3. **Approach.** Use $0\le x\le3$, $0\le y\le3-x$.

   The volume is

   $$V=\int_0^3\int_0^{3-x}\left(5-\frac{x+y}{2}\right)dy\,dx.$$

   Because the height is a plane, the average over the triangle can also be
   checked from its vertex values: 5, 3.5, 3.5 m. A linear function's average
   over a triangle is the average of its vertex values:

   $$z_{\mathrm{avg}}=\frac{5+3.5+3.5}{3}=4\ \mathrm m.$$

   The base area is $\frac12(3)(3)=4.5$ m², so

   $$\boxed{V=(4.5)(4)=18\ \mathrm{m^3}},
   \qquad\boxed{z_{\mathrm{avg}}=4\ \mathrm m}.$$

   Direct evaluation of the double integral gives the same result. ✓

4. **Approach.** Density varies only with $x$.

   $$M=\int_0^1\int_0^2(3+2x)dy\,dx
   =2\int_0^1(3+2x)dx
   =2[3x+x^2]_0^1=\boxed{8}\ \mathrm{kg}.$$

   $$\bar x
   =\frac1{8}2\int_0^1x(3+2x)dx
   =\frac14\left[\frac32x^2+\frac23x^3\right]_0^1
   =\frac14\left(\frac{13}{6}\right)
   =\boxed{\frac{13}{24}\ \mathrm m}
   \approx0.542\ \mathrm m.$$

   Density is independent of $y$, so

   $$\boxed{\bar y=1.00\ \mathrm m}.$$

   **Check:** density increases to the right, so $\bar x>0.5$ m. ✓

5. The annulus has $1\le r\le3$ and $0\le\theta\le2\pi$:

   $$A=\int_0^{2\pi}\int_1^3r\,dr\,d\theta
   =2\pi\left[\frac{r^2}{2}\right]_1^3
   =\pi(9-1)=\boxed{8\pi}.$$

   Circle check: $\pi(3^2)-\pi(1^2)=8\pi$. ✓

6. **Approach.** Radial density and a circular region make polar coordinates
   natural.

   $$M=\int_0^{2\pi}\int_0^2(4+r)r\,dr\,d\theta.$$

   $$=2\pi\left[2r^2+\frac{r^3}{3}\right]_0^2
   =2\pi\left(8+\frac83\right)
   =\boxed{\frac{64\pi}{3}\ \mathrm{kg}}.$$

   The density increases outward but remains perfectly rotationally symmetric,
   so every outward shift in one direction is balanced by an equal shift in the
   opposite direction. The center of mass remains at the origin. ✓

7. Base area is 1 m². Mass:

   $$M=\int_0^2(600+50z)dz
   =[600z+25z^2]_0^2
   =1200+100=\boxed{1300\ \mathrm{kg}}.$$

   Vertical first moment:

   $$M\bar z=\int_0^2z(600+50z)dz
   =\left[300z^2+\frac{50}{3}z^3\right]_0^2$$

   $$=1200+\frac{400}{3}
   =\frac{4000}{3}\ \mathrm{kg\,m}.$$

   Therefore

   $$\boxed{\bar z=\frac{4000/3}{1300}
   =\frac{40}{39}\ \mathrm m
   \approx1.026\ \mathrm m}.$$

   **Check:** uniform density would give 1.000 m; increasing density with height
   moves the center upward slightly. ✓

8. In cylindrical coordinates, $x^2+y^2=r^2$ and $dV=r\,dr\,d\theta\,dz$:

   $$I=\int_0^5\int_0^{2\pi}\int_0^2r^3\,dr\,d\theta\,dz.$$

   $$I=(5)(2\pi)\left[\frac{r^4}{4}\right]_0^2
   =(5)(2\pi)(4)=\boxed{40\pi}.$$

9. The shell has $a\le\varrho\le b$, $0\le\phi\le\pi$,
   $0\le\theta\le2\pi$:

   $$V=\int_0^{2\pi}\int_0^\pi\int_a^b
   \varrho^2\sin\phi\,d\varrho\,d\phi\,d\theta$$

   $$=2\pi(2)\left[\frac{\varrho^3}{3}\right]_a^b
   =\boxed{\frac{4\pi}{3}(b^3-a^3)}.$$

   **Check:** outer-sphere volume minus inner-sphere volume gives the same formula.

10. The Jacobian is

    $$\frac{\partial(x,y)}{\partial(u,v)}
    =\begin{vmatrix}2&0\\0&3\end{vmatrix}=6.$$

    The unit disk has area $\pi$, so the transformed ellipse has

    $$A=\iint_{u^2+v^2\le1}6\,du\,dv
    =\boxed{6\pi}.$$

    **Check:** the ellipse semiaxes are 2 and 3, and the Handbook formula
    $A=\pi ab$ gives $6\pi$. ✓

---

## Quick Reference

### Double integrals

$$\boxed{\iint_Df(x,y)\,dA}$$

Rectangle:

$$\int_a^b\int_c^df(x,y)\,dy\,dx.$$

Vertically simple region:

$$\boxed{\int_a^b\int_{g_1(x)}^{g_2(x)}f(x,y)\,dy\,dx}$$

Horizontally simple region:

$$\boxed{\int_c^d\int_{h_1(y)}^{h_2(y)}f(x,y)\,dx\,dy}$$

### Geometry and averages

$$\boxed{A(D)=\iint_D1\,dA}$$

$$\boxed{V=\iint_Df(x,y)\,dA\quad(f\ge0)}$$

$$\boxed{f_{\mathrm{avg}}=\frac1{A(D)}\iint_Df\,dA}$$

### Lamina mass and center of mass

$$\boxed{M=\iint_D\rho_A\,dA}$$

$$\boxed{\bar x=\frac1M\iint_Dx\rho_A\,dA,
\qquad
\bar y=\frac1M\iint_Dy\rho_A\,dA}$$

### Polar coordinates

$$x=r\cos\theta,
\qquad y=r\sin\theta,
\qquad x^2+y^2=r^2$$

$$\boxed{dA=r\,dr\,d\theta}$$

### Triple integrals

$$\boxed{\iiint_Ef\,dV}$$

$$\boxed{V(E)=\iiint_E1\,dV}$$

$$\boxed{M=\iiint_E\rho_V\,dV}$$

$$\boxed{\bar x=\frac1M\iiint_Ex\rho_V\,dV,
\quad\bar y=\frac1M\iiint_Ey\rho_V\,dV,
\quad\bar z=\frac1M\iiint_Ez\rho_V\,dV}$$

### Cylindrical coordinates

$$x=r\cos\theta,
\quad y=r\sin\theta,
\quad z=z$$

$$\boxed{dV=r\,dr\,d\theta\,dz}$$

### Spherical coordinates — convention used here

$$x=\varrho\sin\phi\cos\theta,
\quad y=\varrho\sin\phi\sin\theta,
\quad z=\varrho\cos\phi$$

$$\boxed{dV=\varrho^2\sin\phi\,d\varrho\,d\phi\,d\theta}$$

with $\phi$ measured from $+z$ and $\theta$ the azimuth angle.

### General 2D Jacobian

$$\boxed{dA=
\left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv}$$

### Five-step setup check

1. **Draw** the region or solid.
2. **Choose** coordinates that fit the geometry.
3. **Write** the correct $dA$ or $dV$, including the Jacobian factor.
4. **Set** the bounds from inner slice to outer sweep.
5. **Check** units, symmetry, magnitude, and any available Handbook geometry formula.

---

## What's Next

Apprentice, you can now accumulate over lines, areas, and volumes. The integral
has stopped being a one-dimensional operation and become what engineers actually
need it to be: a way to total a distributed quantity over whatever geometry the
problem gives you.

The next chapter, **01-25 Differential Equations**, changes the question. Instead
of being given a function and integrating it, you will be given a relationship
between an unknown function and its derivatives and asked to recover the function.
That is how transient circuits, vibration, thermal response, population models,
and many transport processes are written.

Three habits from this chapter carry directly forward:

**Geometry before algebra.** In a differential equation, the equivalent habit is
model form before solution technique.

**Units as a structural check.** Derivative terms in one equation must have
compatible units, just as an integrand times $dA$ or $dV$ must produce the units
of the requested total.

**Use the reference for formulas, not judgment.** The Handbook gives important
ordinary-differential-equation solution forms and transform tables. You will still
need to recognize the equation, interpret its initial conditions, and choose the
correct method.

Before moving on, redo Worked Example 2 without looking at the bounds, then redo
Worked Example 5 and explain the extra $r$ without saying "because the formula
has one." If you can reconstruct both from geometry, this chapter has done its
job.

— Your Mentor
