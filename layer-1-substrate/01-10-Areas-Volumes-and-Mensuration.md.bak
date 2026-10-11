---
chapter: "01-10"
title: "Areas, Volumes, and Mensuration"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-010-01, MATH-1B-010-02, MATH-1B-010-03]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-10: Areas, Volumes, and Mensuration

> *"Before you can calculate stress, you need an area. Before you can
> calculate flow, you need a cross-section. Before you can calculate
> cost, you need a volume. Mensuration isn't glamorous — it's the
> arithmetic of geometry, and it underpins every quantitative engineering
> result."*

---

## Before You Start

**Prerequisites:** [01-09 Analytic Geometry](01-09-analytic-geometry.md)

**Skip if:** You pass the Tier 1B test-out quiz. Confirm you know how to
find the centroid of a composite area before skipping — that calculation
appears in structural and mechanical problems throughout Tier 2.

**Time:** ~45 min read · ~20 min review questions · ~45 min practice problems

---

## On the Board Today

Apprentice, this is a reference chapter more than a conceptual one. The
mensuration formulas are all in the Handbook, pages 41 through 44, and you
should absolutely look them up rather than memorize obscure cases like
the surface area of a frustum of a cone. They're there; use them.

What is worth your attention here is the **strategy**, not the formulas:

**Composite areas** are found by adding and subtracting simpler shapes.
A T-beam cross-section is a rectangle plus a rectangle. A hollow pipe
cross-section is a large circle minus a small circle. You'll see this
pattern constantly in structural and mechanical problems.

**Centroids** of composite shapes follow from the centroid of each component.
The centroid is the balance point — where you'd put a finger to support the
shape. In structural engineering, the centroid determines where the neutral
axis is, which determines how a beam bends. In fluid mechanics, it's the
center of pressure. It's not optional knowledge.

**Unit conversions for area and volume** are the place where Chapter 01-01
comes back to bite people who thought they were done with it. Area
conversions square the linear conversion factor; volume conversions cube
it. The reminder is here because this is the last chance before you
start using areas and volumes in physics problems in Tier 2.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 10.1 Compute the area and perimeter of standard plane figures using
  Handbook formulas
* 10.2 Compute the surface area and volume of standard solids
* 10.3 Find the area and centroid of a composite plane figure
* 10.4 Apply area and volume unit conversions correctly
* 10.5 Compute the volume of a solid of revolution using the disk/washer
  concept (preview; full integration treatment in Chapter 01-22)
* 10.6 Locate the centroid of a standard shape from the Handbook tables

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $A$ | area | m², ft², in², mm² |
| $V$ | volume | m³, ft³, in³ |
| $S$ | surface area | same units as area |
| $\bar{x}, \bar{y}$ | centroid coordinates | $\bar{x}$ is $x$-coordinate of centroid |
| $A_i$ | area of component $i$ | for composite shapes |
| $\bar{x}_i, \bar{y}_i$ | centroid of component $i$ | — |
| $r$ | radius | not a correlation coefficient here |
| $h$ | height | — |
| $b$ | base width | — |
| $l$ | slant height | for cones and pyramids |

---

## 10.1 Plane Figures — Area and Perimeter

All of these are in the Handbook, pp. 41–42. The table below is a
reference and a memory-trigger — look up the exact form in the Handbook
when precision matters.

| Shape | Area | Perimeter | Notes |
|---|---|---|---|
| Rectangle | $bh$ | $2(b+h)$ | — |
| Square | $s^2$ | $4s$ | — |
| Parallelogram | $bh$ | $2(a+b)$ | $h$ = perpendicular height |
| Triangle | $\frac{1}{2}bh$ | $a+b+c$ | any base and corresponding height |
| Equilateral triangle | $\frac{\sqrt{3}}{4}s^2$ | $3s$ | $s$ = side length |
| Trapezoid | $\frac{1}{2}(b_1+b_2)h$ | $b_1+b_2+a+c$ | parallel sides $b_1$, $b_2$ |
| Circle | $\pi r^2$ | $2\pi r$ | — |
| Circular sector | $\frac{1}{2}r^2\theta$ | $r\theta + 2r$ | $\theta$ in **radians** |
| Ellipse | $\pi ab$ | ≈ Ramanujan approx. | semi-axes $a$, $b$ |
| Regular polygon ($n$ sides, length $s$) | $\frac{nbs}{4}\cot\frac{\pi}{n}$ | $ns$ | $b$ = apothem |

> ---
> **Mentor's Margin**
>
> The sector area formula $\frac{1}{2}r^2\theta$ requires $\theta$ in
> radians, not degrees. This is a reliable source of errors because people
> compute the angle in degrees and forget to convert. A sector of 90° is
> $\pi/2$ radians, and the area is $\frac{1}{2}r^2(\pi/2)$, not
> $\frac{1}{2}r^2(90)$. Whenever an arc length or sector area formula
> appears, verify your angle is in radians. Every time.
>
> ---

### Heron's formula — triangle area from three sides

When you have three sides $a$, $b$, $c$ but no height:

$$s = \frac{a+b+c}{2} \quad \text{(semi-perimeter)}$$

$$A = \sqrt{s(s-a)(s-b)(s-c)}$$

This is in the Handbook. It appears in surveying and structural geometry
problems where you have coordinate points and need an enclosed area.

---

## 10.2 Solids — Surface Area and Volume

| Shape | Volume | Surface area | Notes |
|---|---|---|---|
| Rectangular prism | $lbh$ | $2(lb+lh+bh)$ | — |
| Cube | $s^3$ | $6s^2$ | — |
| Right circular cylinder | $\pi r^2 h$ | $2\pi r h + 2\pi r^2$ | lateral + two caps |
| Hollow cylinder | $\pi(r_o^2-r_i^2)h$ | — | pipe/tube; $r_o$ outer, $r_i$ inner |
| Sphere | $\frac{4}{3}\pi r^3$ | $4\pi r^2$ | — |
| Right circular cone | $\frac{1}{3}\pi r^2 h$ | $\pi r l + \pi r^2$ | $l=\sqrt{r^2+h^2}$ = slant height |
| Frustum of cone | $\frac{\pi h}{3}(r_1^2+r_1r_2+r_2^2)$ | $\pi l(r_1+r_2)+\pi(r_1^2+r_2^2)$ | $l=\sqrt{h^2+(r_1-r_2)^2}$ |
| Pyramid | $\frac{1}{3}A_{base}h$ | varies | any base |
| Torus (donut) | $2\pi^2 Rr^2$ | $4\pi^2 Rr$ | $R$ = ring radius, $r$ = tube radius |

> ---
> **Mentor's Margin**
>
> Three formulas worth knowing cold without looking them up, because
> they appear so often in FE problems:
>
> **Cylinder:** $V = \pi r^2 h$. Volume of a pipe, a tank, a piston bore.
>
> **Sphere:** $V = \frac{4}{3}\pi r^3$. Volume of a tank head, a
> spherical pressure vessel.
>
> **Cone is one-third the cylinder:** $V = \frac{1}{3}\pi r^2 h$.
> A cone with the same base and height as a cylinder holds one-third the
> volume. That relationship — cone is $1/3$ cylinder, pyramid is $1/3$
> prism — is easy to recall because it comes from integration, which you'll
> see in Chapter 01-22.
>
> ---

### Worked Example 1 — Hollow Cylinder Volume

**Given.** A steel pipe has outer diameter $OD = 6$ in and wall thickness
$t = 0.25$ in. Find the cross-sectional area and the volume of a 10-ft
length.

**Solution.**

Inner diameter: $ID = OD - 2t = 6 - 0.50 = 5.5$ in.

$r_o = 3.0$ in, $r_i = 2.75$ in.

Cross-sectional area:

$$A = \pi(r_o^2 - r_i^2) = \pi(9.00 - 7.5625) = \pi(1.4375) = 4.515 \text{ in}^2$$

Volume for 10 ft = 120 in length:

$$V = A \cdot L = 4.515 \times 120 = 541.8 \text{ in}^3$$

**Convert to ft³:** $1 \text{ ft}^3 = 1728 \text{ in}^3$

$$V = \frac{541.8}{1728} = \boxed{0.314 \text{ ft}^3}$$

**Check order of magnitude:** a 6-inch pipe, 1-inch thick steel... a circle of
area $\approx \pi(3)^2 = 28$ in² minus inner $\approx \pi(2.75)^2 = 23.8$
in² gives about 4.5 in² cross-section. At 10 feet = 120 inches: $4.5 \times
120 = 540$ in³ ≈ 0.31 ft³. ✓

---

## 10.3 Centroids

The **centroid** of a shape is its geometric center — the point where the
shape would balance on a pin. For uniform-density shapes, the centroid
coincides with the center of mass.

### Centroid of standard shapes

These are in the Handbook, pp. 42–44 (Table of Geometric Properties).

| Shape | $\bar{x}$ | $\bar{y}$ | Reference point |
|---|---|---|---|
| Rectangle $b \times h$ | $b/2$ | $h/2$ | corner |
| Right triangle (legs along axes) | $b/3$ | $h/3$ | right-angle corner |
| Circle radius $r$ | center | center | — |
| Semicircle radius $r$ | 0 | $4r/(3\pi)$ | diameter center |
| Quarter-circle | $4r/(3\pi)$ | $4r/(3\pi)$ | center of full circle |

The semicircle centroid $\bar{y} = 4r/(3\pi) \approx 0.424r$ — it sits
about 42% of the radius up from the diameter. This appears in calculations
involving circular tanks and structural arches.

### Centroid of a composite shape

The centroid of a composite shape is the **area-weighted average** of the
centroids of its parts:

$$\boxed{\bar{x} = \frac{\sum A_i \bar{x}_i}{\sum A_i} \qquad \bar{y} = \frac{\sum A_i \bar{y}_i}{\sum A_i}}$$

For a **removed area** (hole), subtract it: assign a negative area.

### The composite centroid table

Organize every problem in this format:

| Component | $A_i$ | $\bar{x}_i$ | $\bar{y}_i$ | $A_i\bar{x}_i$ | $A_i\bar{y}_i$ |
|---|---|---|---|---|---|
| Shape 1 | — | — | — | — | — |
| Shape 2 | — | — | — | — | — |
| Hole (–) | $-A_h$ | $\bar{x}_h$ | $\bar{y}_h$ | $-A_h\bar{x}_h$ | $-A_h\bar{y}_h$ |
| **Total** | $\Sigma A_i$ | — | — | $\Sigma A_i\bar{x}_i$ | $\Sigma A_i\bar{y}_i$ |

$$\bar{x} = \frac{\Sigma A_i\bar{x}_i}{\Sigma A_i} \qquad \bar{y} = \frac{\Sigma A_i\bar{y}_i}{\Sigma A_i}$$

### Worked Example 2 — Composite Centroid

**Given.** Find the centroid of the T-section shown. All dimensions in mm.

- Wide flange: 120 mm wide × 20 mm tall, bottom of shape
- Web: 20 mm wide × 80 mm tall, centered on flange, above flange

*(Coordinate origin at bottom-left corner of flange.)*

**Solution.**

Set up the table. Define $y$ measured from the bottom.

| Component | $A_i$ (mm²) | $\bar{y}_i$ (mm) | $A_i\bar{y}_i$ (mm³) |
|---|---|---|---|
| Flange: $120 \times 20$ | 2,400 | 10 | 24,000 |
| Web: $20 \times 80$ | 1,600 | $20 + 40 = 60$ | 96,000 |
| **Total** | **4,000** | — | **120,000** |

$$\bar{y} = \frac{120{,}000}{4{,}000} = 30 \text{ mm from the bottom}$$

For $\bar{x}$: by symmetry (both shapes centered at $x = 60$ mm):
$\bar{x} = 60$ mm from the left edge.

$$\boxed{\bar{x} = 60 \text{ mm}, \quad \bar{y} = 30 \text{ mm from bottom}}$$

**Check.** The centroid at $\bar{y} = 30$ mm sits inside the web
($y = 20$ to $100$ mm), closer to the flange where most material is.
The flange carries 2,400 mm² at $y = 10$ mm; the web carries 1,600 mm²
at $y = 60$ mm. Weighted average should be below 40 mm (the midpoint of
the web), which 30 mm is. ✓

> ---
> **Mentor's Margin**
>
> The T-section centroid calculation is foundational for beam bending in
> Tier 2C. Once you have $\bar{y}$, the distance from the centroid to the
> outermost fiber — called $c$ — determines the maximum bending stress via
> $\sigma = Mc/I$. If you get the centroid wrong, the stress calculation
> is wrong, which is why the table method matters: it's systematic and
> checkable rather than approximate and intuitive.
>
> ---

### Worked Example 3 — Composite Area With a Hole

**Given.** A rectangular plate $200 \times 300$ mm has a circular hole of
radius 40 mm centered at $(100, 120)$ from the bottom-left corner. Find
the area and centroid.

**Solution.**

| Component | $A_i$ (mm²) | $\bar{x}_i$ (mm) | $\bar{y}_i$ (mm) | $A_i\bar{x}_i$ | $A_i\bar{y}_i$ |
|---|---|---|---|---|---|
| Rectangle | 60,000 | 100 | 150 | 6,000,000 | 9,000,000 |
| Circle (–) | $-\pi(1600)=-5,027$ | 100 | 120 | $-502,700$ | $-603,200$ |
| **Total** | **54,973** | — | — | **5,497,300** | **8,396,800** |

$$\bar{x} = \frac{5{,}497{,}300}{54{,}973} = 100.0 \text{ mm}$$

$$\bar{y} = \frac{8{,}396{,}800}{54{,}973} = 152.7 \text{ mm}$$

$$\boxed{A = 54{,}973 \text{ mm}^2, \quad \bar{x} = 100 \text{ mm}, \quad \bar{y} = 152.7 \text{ mm}}$$

**Check.** $\bar{x} = 100$ mm — the shape is symmetric about $x = 100$,
so this is expected. ✓

$\bar{y}$ shifted slightly upward from 150 mm (the unperforated centroid)
because the hole at $y = 120$ mm removes material below center, pulling
the centroid upward. The shift from 150 to 152.7 mm is small because
the hole is small relative to the total area: $5,027/60,000 \approx 8\%$.
A small hole causes a small shift. ✓

---

## 10.4 Unit Conversions for Area and Volume

Building on Chapter 01-01, but now applied to the specific conversions
that appear most often in FE problems.

### Area conversions (square the linear factor)

| From | To | Multiply by |
|---|---|---|
| ft² | in² | $144 = 12^2$ |
| in² | ft² | $1/144$ |
| m² | mm² | $10^6 = (10^3)^2$ |
| mm² | m² | $10^{-6}$ |
| ft² | m² | $0.09290 = (0.3048)^2$ |
| in² | mm² | $645.2 = (25.4)^2$ |
| mm² | in² | $0.001550$ |

### Volume conversions (cube the linear factor)

| From | To | Multiply by |
|---|---|---|
| ft³ | in³ | $1{,}728 = 12^3$ |
| in³ | ft³ | $1/1728$ |
| m³ | mm³ | $10^9 = (10^3)^3$ |
| m³ | L | $1{,}000$ |
| L | m³ | $0.001$ |
| ft³ | gal (US) | $7.481$ |
| gal (US) | L | $3.785$ |
| in³ | mL | $16.39$ |

> ---
> **Mentor's Margin**
>
> The gallon conversions appear in fluid flow, tank-sizing, and
> hydraulics problems. Know that 1 gallon of water weighs 8.34 lbf
> and 1 cubic foot of water weighs 62.4 lbf — both are in the
> Handbook's Commonly Used Equivalents on page 1, and both come up
> constantly in Civil and Environmental problems.
>
> ---

---

## 10.5 Solids of Revolution — Preview

A **solid of revolution** is formed by rotating a plane figure about an
axis.

**Pappus's theorem** (in the Handbook): the volume of a solid of
revolution equals the area of the generating region multiplied by the
distance traveled by its centroid:

$$\boxed{V = 2\pi \bar{r} A}$$

where $\bar{r}$ is the distance from the centroid of the region to the
axis of rotation.

This is remarkably powerful — it lets you find the volume of a torus, a
pipe bend, or a donut-shaped tank without integration:

**Torus:** rotate a circle of radius $r$ about an axis at distance $R$
from the circle's center. Area $= \pi r^2$, centroid distance $= R$.

$$V_{torus} = 2\pi R \cdot \pi r^2 = 2\pi^2 R r^2$$

which matches the formula in the table above. ✓

The full treatment — using integration to compute volumes directly —
is in Chapter 01-22.

---

## As the Handbook States It

> **Handbook 10.6, pp. 41–44** — *Mathematics / Mensuration of Areas
> and Volumes*

The Handbook provides complete tables covering:

- All standard plane figures with area and perimeter formulas
- All standard solids with volume and surface area formulas
- Table of centroids for standard plane figures
- Heron's formula
- Pappus's theorem

**This is one of the richest sections in the Handbook for FE purposes.**
Learn the section structure so you can navigate it in under 20 seconds.
The tables are organized: plane figures first (areas), then solids (volumes),
then centroids.

**What's not in the Handbook:**

- Composite centroid calculation procedure (it's implied but not stated
  step-by-step)
- Area-weighted average formula in symbolic form
- The table method for composite shapes

Those are the procedural skills that turn the Handbook's reference data
into computed answers.

**Important units note.** The Handbook uses both SI and USCS throughout
its mensuration tables. Some formulas are given in both systems, some in
only one. The first-page conversion table handles what the mensuration
section doesn't explicitly convert. Carry units and the conversions will
tell you what's needed.

---

## Where This Goes Wrong

**Forgetting to square or cube conversion factors.** $1 \text{ ft}^2 \ne
12 \text{ in}^2$. It's $144 \text{ in}^2$. $1 \text{ ft}^3 \ne 12
\text{ in}^3$. It's $1{,}728 \text{ in}^3$. Every area conversion squares
the linear factor; every volume conversion cubes it.

**Using degrees in the sector area formula.** $A = \frac{1}{2}r^2\theta$
requires $\theta$ in radians. Convert first.

**Centroid of a right triangle.** The centroid is at $b/3$ from the
vertical leg and $h/3$ from the horizontal leg — one-third of each leg
measured from the right-angle corner, not the midpoint.

**Centroid of a semicircle.** $\bar{y} = 4r/(3\pi) \approx 0.424r$ from
the diameter, not $r/2$. People assume it's at the midpoint of the radius.
It isn't — it's closer to the diameter than to the top.

**Using outer radius instead of inner in the hollow cylinder formula.**
The cross-sectional area is $\pi(r_o^2 - r_i^2)$, not $\pi r_o^2$.

**Sign error on a hole.** A removed area contributes a *negative* $A_i$
in the composite centroid formula. Forgetting the negative sign shifts
the centroid toward the hole rather than away from it.

**Mixing units within a single calculation.** If you're computing a
centroid with some dimensions in inches and others in feet without
converting, the result is meaningless. Pick one unit system at the start
and convert everything.

**Slant height versus vertical height in cones.** The volume formula uses
the perpendicular height $h$. The lateral surface area formula uses the
slant height $l = \sqrt{r^2 + h^2}$. Plugging $h$ where $l$ belongs
(or vice versa) is a common error.

---

## Key Terms

| Term | Definition |
|---|---|
| Mensuration | The study and computation of areas, volumes, and surface areas of geometric figures |
| Centroid | The geometric center of a shape; the area-weighted average position |
| Composite shape | A shape built from multiple simpler shapes added or subtracted |
| Semi-perimeter | $s = (a+b+c)/2$; used in Heron's formula |
| Slant height | The distance along the side of a cone from base edge to apex; $l = \sqrt{r^2+h^2}$ |
| Frustum | The portion of a cone or pyramid between two parallel planes cutting it |
| Solid of revolution | A solid generated by rotating a plane figure about an axis |
| Pappus's theorem | Volume of revolution = $2\pi\bar{r}A$; area of generator × distance traveled by centroid |
| Torus | A donut-shaped surface of revolution; a circle rotated about a non-intersecting axis |
| Sector | A "pie slice" of a circle, bounded by two radii and an arc |

---

## Review Questions

### Conceptual

1. Why does converting an area measurement from ft² to in² require
   multiplying by $144$ rather than $12$?
2. The centroid of a right triangle is at $b/3$ and $h/3$. Explain
   geometrically why it's one-third of the way, not halfway.
3. In a composite centroid calculation, you have a shape with a hole.
   How do you handle the hole algebraically?
4. Pappus's theorem says volume = $2\pi\bar{r}A$. State what each
   symbol represents and give one example of its use.
5. Why does the cone formula $V = \frac{1}{3}\pi r^2 h$ have a factor
   of one-third? (Hint: think about comparing to a cylinder.)

### Calculation

6. Find the area and perimeter of:
   (a) A trapezoid with parallel sides 8 cm and 14 cm, height 6 cm,
   and non-parallel sides 7 cm each
   (b) A circular sector with radius 5 m and central angle 72°

7. Find the volume and total surface area of:
   (a) A cylinder with radius 3 m and height 8 m
   (b) A sphere with diameter 10 cm
   (c) A cone with base radius 4 in and height 9 in

8. Find the area and centroid coordinates ($\bar{x}$, $\bar{y}$) of
   each composite shape. Place the origin at the bottom-left corner
   unless stated otherwise.

   (a) An L-section: a rectangle 60 mm × 100 mm (full height), with
   another rectangle 80 mm × 40 mm attached to the right of the
   bottom of the first (total bottom width = 140 mm).

   (b) A rectangle 10 in × 6 in with a semicircular notch of radius
   2 in removed from the center of the top edge.

9. A hollow rectangular section has outer dimensions 200 mm × 300 mm
   and inner dimensions 160 mm × 260 mm (centered).
   (a) Find the cross-sectional area.
   (b) Find the centroid.
   (c) Explain why the centroid is at the geometric center without
   calculating.

10. Convert:
    (a) $2.5 \text{ ft}^2$ to in²
    (b) $750 \text{ mm}^2$ to cm²
    (c) $0.5 \text{ ft}^3$ to gallons
    (d) $200 \text{ mL}$ to in³

11. A cylindrical water tank has inner diameter 4 m and height 5 m.
    (a) Volume in m³.
    (b) Volume in liters.
    (c) Mass of water when full (density of water = 1,000 kg/m³) in
    tonnes (1 tonne = 1,000 kg).
    (d) Weight in kN (use $g = 9.807$ m/s²).

12. **Engineering.** A T-beam (floor joist) has the following dimensions:
    - Flange: 600 mm wide × 100 mm thick (bottom of effective section)
    - Web: 200 mm wide × 400 mm tall (above flange)

    (a) Find the total cross-sectional area.
    (b) Find the centroid height $\bar{y}$ measured from the bottom of
    the flange.
    (c) Find the distance $c_1$ from the centroid to the bottom fiber and
    $c_2$ from the centroid to the top fiber.

13. **Engineering.** A pipe of outer diameter 12 in and inner diameter
    10.5 in carries water.
    (a) Cross-sectional flow area in in².
    (b) If the water velocity is 4 ft/s, find the volumetric flow rate
    $Q = Av$ in ft³/s and in gallons per minute (gpm; use 1 ft³/s =
    449 gpm).

### Multiple Choice

14. The area of a circle with diameter 10 m is approximately:
    A) $31.4 \text{ m}^2$
    B) $78.5 \text{ m}^2$
    C) $100 \text{ m}^2$
    D) $314 \text{ m}^2$

15. The centroid of a rectangle of width $b$ and height $h$ measured from
    the bottom-left corner is at:
    A) $(b/3, h/3)$
    B) $(b/2, h/3)$
    C) $(b/2, h/2)$
    D) $(b/3, h/2)$

16. A composite area has two components: Area 1 = 400 mm² with centroid at
    $\bar{y}_1 = 20$ mm, and Area 2 = 600 mm² with centroid at $\bar{y}_2
    = 50$ mm. The composite centroid $\bar{y}$ is:
    A) 35 mm
    B) 38 mm
    C) 40 mm
    D) 42 mm

17. Converting $1 \text{ m}^3$ to liters gives:
    A) $100$ L
    B) $1{,}000$ L
    C) $10{,}000$ L
    D) $100{,}000$ L

18. A solid cone has the same base and height as a cylinder. The ratio of
    their volumes (cone/cylinder) is:
    A) $1/4$
    B) $1/3$
    C) $1/2$
    D) $2/3$

---

## Answer Key with Explanations

**1.** Because area has dimensions of length². Converting 1 ft to 12 in
and squaring gives $(1 \text{ ft})^2 = (12 \text{ in})^2 = 144 \text{ in}^2$.
The conversion factor is squared because both dimensions of the area are
in feet, and each must convert. $1 \text{ ft}^2 \times (12 \text{ in/ft})^2
= 144 \text{ in}^2$. (§10.4)

**2.** The centroid divides the area of the triangle equally in a specific
sense — it's the balance point. For a right triangle with legs along the
axes, the centroid can be found by noting that a horizontal strip at height
$y$ has width proportional to $(h-y)/h \cdot b$, which decreases linearly
from $b$ at the base to 0 at the apex. The weighted average of $y$ over
this distribution gives $\bar{y} = h/3$, not $h/2$, because more area is
concentrated near the base where the strips are wider. (§10.3)

**3.** Treat the hole as a component with a negative area. In the centroid
formula $\bar{y} = \Sigma A_i\bar{y}_i / \Sigma A_i$, include the hole with
$A_h$ carrying a minus sign in both numerator and denominator. This is
equivalent to saying: the composite area equals the unperforated shape minus
the removed material. (§10.3)

**4.** In $V = 2\pi\bar{r}A$: $A$ is the area of the plane figure being
rotated; $\bar{r}$ is the distance from the figure's centroid to the axis
of rotation; $2\pi\bar{r}$ is the distance the centroid travels in one full
revolution. Example: a torus — rotate a circle of area $\pi r^2$ with
centroid at distance $R$ from the axis. $V = 2\pi R \cdot \pi r^2 =
2\pi^2Rr^2$. (§10.5)

**5.** Consider filling a cylinder and cone with the same base radius and
height. The cone's sloping walls mean each horizontal slice is smaller —
specifically, at height $z$ from the base, the cone's cross-section has
radius $r(1 - z/h)$, which is less than $r$ for any $z > 0$. When you
integrate the area over the height, the $1/3$ factor appears naturally.
Equivalently, three identical cones can be rearranged to fill one cylinder
of the same base and height — the factor of 1/3 is exact. (§10.2)

**6.**

(a) Area of trapezoid: $A = \frac{1}{2}(8+14)(6) = \frac{1}{2}(22)(6) =
\boxed{66 \text{ cm}^2}$

Perimeter: $P = 8 + 14 + 7 + 7 = \boxed{36 \text{ cm}}$

(b) Convert 72° to radians: $72° \times \pi/180 = 2\pi/5 = 1.2566$ rad

Area: $A = \frac{1}{2}r^2\theta = \frac{1}{2}(25)(1.2566) = \boxed{15.7 \text{ m}^2}$

Arc length: $s = r\theta = 5(1.2566) = 6.283$ m
Perimeter: $P = s + 2r = 6.283 + 10 = \boxed{16.3 \text{ m}}$

**7.**

(a) $V = \pi(9)(8) = 72\pi \approx \boxed{226 \text{ m}^3}$

$S = 2\pi rh + 2\pi r^2 = 2\pi(3)(8) + 2\pi(9) = 48\pi + 18\pi = 66\pi \approx \boxed{207 \text{ m}^2}$

(b) $r = 5$ cm: $V = \frac{4}{3}\pi(125) = \frac{500\pi}{3} \approx \boxed{524 \text{ cm}^3}$

$S = 4\pi(25) = 100\pi \approx \boxed{314 \text{ cm}^2}$

(c) $l = \sqrt{16+81} = \sqrt{97} \approx 9.849$ in

$V = \frac{1}{3}\pi(16)(9) = 48\pi \approx \boxed{150.8 \text{ in}^3}$

$S_{lateral} = \pi r l = \pi(4)(9.849) = 39.40\pi \approx 123.7$ in²

$S_{total} = \pi r l + \pi r^2 = 123.7 + 50.3 = \boxed{174 \text{ in}^2}$

**8.**

(a) Coordinates measured from bottom-left corner of the full bounding
rectangle.

Component 1 (tall left rectangle): $60 \times 100 = 6{,}000$ mm²,
centroid at $(30, 50)$.

Component 2 (short right rectangle): $80 \times 40 = 3{,}200$ mm²,
centroid at $(60 + 40, 20) = (100, 20)$.

| Component | $A$ | $\bar{x}$ | $\bar{y}$ | $A\bar{x}$ | $A\bar{y}$ |
|---|---|---|---|---|---|
| Tall rect. | 6,000 | 30 | 50 | 180,000 | 300,000 |
| Short rect. | 3,200 | 100 | 20 | 320,000 | 64,000 |
| **Total** | **9,200** | | | **500,000** | **364,000** |

$\bar{x} = 500{,}000/9{,}200 = 54.35$ mm
$\bar{y} = 364{,}000/9{,}200 = 39.57$ mm

$\boxed{A = 9{,}200 \text{ mm}^2, \quad \bar{x} = 54.3 \text{ mm}, \quad \bar{y} = 39.6 \text{ mm}}$

(b) Rectangle $10 \times 6 = 60$ in², centroid at $(5, 3)$.

Semicircle at center of top edge: center of full circle would be at
$(5, 6)$; semicircle opens downward. Area $= \frac{1}{2}\pi(4) = 2\pi =
6.283$ in².

Centroid of downward semicircle: the flat side is at $y = 6$ (top edge),
opening downward, centroid is $4r/(3\pi) = 8/(3\pi) = 0.849$ in below
the flat side.

$\bar{y}_{semicircle} = 6 - 0.849 = 5.151$ in from bottom.

| Component | $A$ | $\bar{x}$ | $\bar{y}$ | $A\bar{x}$ | $A\bar{y}$ |
|---|---|---|---|---|---|
| Rectangle | 60 | 5 | 3 | 300 | 180 |
| Semicircle (–) | $-6.283$ | 5 | 5.151 | $-31.42$ | $-32.36$ |
| **Total** | **53.717** | | | **268.58** | **147.64** |

$\bar{x} = 268.58/53.717 = 5.00$ in (by symmetry)
$\bar{y} = 147.64/53.717 = 2.748$ in

$\boxed{A = 53.7 \text{ in}^2, \quad \bar{x} = 5.00 \text{ in}, \quad \bar{y} = 2.75 \text{ in}}$

Note $\bar{y} < 3$ in (the unperforated centroid) because the notch removes
material from the top, pulling the centroid downward. ✓

**9.**

(a) $A = (200)(300) - (160)(260) = 60{,}000 - 41{,}600 = \boxed{18{,}400 \text{ mm}^2}$

(b) $\bar{x} = 100$ mm, $\bar{y} = 150$ mm — the geometric center.

(c) The shape is doubly symmetric about both $x = 100$ mm and $y = 150$ mm.
For any symmetric shape, the centroid lies on each axis of symmetry. The
intersection of two perpendicular axes of symmetry is the geometric center.
No calculation needed for a symmetric hollow section. (§10.3)

**10.**

(a) $2.5 \times 144 = \boxed{360 \text{ in}^2}$

(b) $1 \text{ cm} = 10 \text{ mm}$, so $1 \text{ cm}^2 = 100 \text{ mm}^2$.
$750/100 = \boxed{7.50 \text{ cm}^2}$

(c) $0.5 \times 7.481 = \boxed{3.74 \text{ gal}}$

(d) $200 \text{ mL} \div 16.39 \text{ mL/in}^3 = \boxed{12.20 \text{ in}^3}$

**11.**

(a) $r = 2$ m: $V = \pi(4)(5) = 20\pi \approx \boxed{62.83 \text{ m}^3}$

(b) $62.83 \text{ m}^3 \times 1{,}000 \text{ L/m}^3 = \boxed{62{,}830 \text{ L}}$

(c) $m = \rho V = 1{,}000 \times 62.83 = 62{,}830 \text{ kg} = \boxed{62.83 \text{ tonnes}}$

(d) $F_W = mg = 62{,}830 \times 9.807 = 616{,}100 \text{ N} = \boxed{616.1 \text{ kN}}$

**12.**

(a) $A = (600)(100) + (200)(400) = 60{,}000 + 80{,}000 = \boxed{140{,}000 \text{ mm}^2}$

(b) Centroid of flange: $\bar{y}_1 = 50$ mm (midpoint of flange).
Centroid of web: $\bar{y}_2 = 100 + 200 = 300$ mm (100 mm above top of
flange + half the web height).

| Component | $A$ (mm²) | $\bar{y}$ (mm) | $A\bar{y}$ (mm³) |
|---|---|---|---|
| Flange | 60,000 | 50 | 3,000,000 |
| Web | 80,000 | 300 | 24,000,000 |
| **Total** | **140,000** | | **27,000,000** |

$\bar{y} = 27{,}000{,}000 / 140{,}000 = \boxed{192.9 \text{ mm from bottom of flange}}$

(c) $c_1 = \bar{y} = 192.9$ mm (to bottom fiber)

Total height = $100 + 400 = 500$ mm.

$c_2 = 500 - 192.9 = \boxed{307.1 \text{ mm to top fiber}}$

**Check:** $c_1 + c_2 = 192.9 + 307.1 = 500$ mm = total height ✓

**13.**

(a) $r_o = 6$ in, $r_i = 5.25$ in.

$A = \pi(36 - 27.5625) = \pi(8.4375) = \boxed{26.51 \text{ in}^2}$

(b) $Q = Av = 26.51 \times 4 = 106.0$ in²·ft/s.

Convert: $106.0 \text{ in}^2 \times \frac{1 \text{ ft}^2}{144 \text{ in}^2} \times 4 \text{ ft/s} = 2.944$ ft²·ft/s... 

Actually $Q = A \times v$ where both must be in consistent units.

$A = 26.51 \text{ in}^2 \div 144 = 0.1841 \text{ ft}^2$

$Q = 0.1841 \text{ ft}^2 \times 4 \text{ ft/s} = \boxed{0.736 \text{ ft}^3/\text{s}}$

In gpm: $0.736 \times 449 = \boxed{330.4 \text{ gpm}}$

**14. B — $78.5 \text{ m}^2$.** $r = 5$ m: $A = \pi(25) = 78.54$ m².
(A) would be for radius 5 but using diameter as radius. (§10.1)

**15. C — $(b/2, h/2)$.** The centroid of a **rectangle** is at the
geometric center: halfway along each dimension. (A) and (D) apply to a
right triangle. (§10.3)

**16. B — 38 mm.** $\bar{y} = (400 \times 20 + 600 \times 50)/(400+600) =
(8{,}000 + 30{,}000)/1{,}000 = 38{,}000/1{,}000 = 38$ mm. The larger area
(600 mm²) at $y = 50$ pulls the centroid above the simple average of 35 mm.
(§10.3)

**17. B — 1,000 L.** $1 \text{ m}^3 = 1{,}000 \text{ L}$ by definition
(1 liter = 1 dm³ = $0.001 \text{ m}^3$). (§10.4)

**18. B — 1/3.** $V_{cone} = \frac{1}{3}\pi r^2 h$ and $V_{cylinder} =
\pi r^2 h$, so the ratio is exactly $1/3$. (§10.2)

---

## Quick Reference

**Common areas** — *Handbook pp. 41–42*

$$A_{rect} = bh \qquad A_{tri} = \tfrac{1}{2}bh \qquad A_{trap} = \tfrac{1}{2}(b_1+b_2)h$$

$$A_{circle} = \pi r^2 \qquad A_{sector} = \tfrac{1}{2}r^2\theta \;(\theta \text{ in rad})$$

**Common volumes** — *Handbook pp. 42–43*

$$V_{cyl} = \pi r^2 h \qquad V_{sphere} = \tfrac{4}{3}\pi r^3 \qquad V_{cone} = \tfrac{1}{3}\pi r^2 h$$

$$V_{hollow\,cyl} = \pi(r_o^2-r_i^2)h$$

**Key centroids** — *Handbook p. 43–44*

$$\bar{y}_{rect} = h/2 \qquad \bar{y}_{tri} = h/3 \quad \text{from base} \qquad \bar{y}_{semicircle} = 4r/(3\pi)$$

**Composite centroid formula**

$$\bar{x} = \frac{\sum A_i\bar{x}_i}{\sum A_i} \qquad \bar{y} = \frac{\sum A_i\bar{y}_i}{\sum A_i}$$

Holes: assign negative $A_i$.

**Unit conversions**

Area: square the linear factor. $1\text{ ft}^2 = 144\text{ in}^2$; $1\text{ m}^2 = 10^6\text{ mm}^2$

Volume: cube the linear factor. $1\text{ ft}^3 = 1{,}728\text{ in}^3$; $1\text{ m}^3 = 1{,}000\text{ L}$

**Pappus's theorem**

$$V = 2\pi\bar{r}A$$

**Not in the Handbook — memorize**

Composite centroid procedure · area-weighted average formula · hole-as-negative-area rule · squared/cubed conversion rule

---

## What's Next

Apprentice, mensuration is complete. You can find the area, volume, and
centroid of any shape the FE will give you, composite or solid.

In **Chapter 01-11: Trigonometry**, we build the mathematical tools for
working with angles and triangles — sine, cosine, tangent, the Pythagorean
identity, the laws of sines and cosines. Every force decomposition in Tier
2C starts here. Every AC phasor in Tier 2E starts here. Every slope angle
in surveying starts here.

Then in Chapter 01-12, we extend trigonometry into the complex plane with
complex numbers in rectangular and polar form. Euler's identity will make
an appearance and tie together the exponential function from Chapter 01-05
with the trigonometric functions from Chapter 01-11.

Bring the Handbook to page 39, the Trigonometry section.

See you there.

— Your Mentor
