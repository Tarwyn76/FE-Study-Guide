---
chapter: "01-12"
title: "Complex Numbers"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-012-01, MATH-1B-012-02, MATH-1B-012-03]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-12: Complex Numbers

> *"Euler's identity — $e^{j\pi} + 1 = 0$ — connects five of the most
> fundamental constants in mathematics in one equation. It is not a
> curiosity. It is the reason AC circuit analysis works, the reason
> vibrating systems have natural frequencies, and the reason the Fourier
> transform exists. Complex numbers aren't complicated. They're just the
> plane."*

---

## Before You Start

**Prerequisites:** [01-05 Exponents, Radicals, and Logarithms](01-05-exponents-radicals-logarithms.md) · [01-07 Polynomials and Their Roots](01-07-polynomials-roots.md) · [01-11 Trigonometry](01-11-trigonometry.md)

**Skip if:** You pass the Tier 1B test-out quiz. Confirm you can convert
between rectangular and polar form, multiply and divide in polar form, and
state Euler's identity before skipping.

**Time:** ~55 min read · ~25 min review questions · ~55 min practice problems

---

## On the Board Today

Apprentice, you met complex numbers briefly in Chapter 01-07 when quadratic
equations produced $\sqrt{-1}$. We called them roots, noted they came in
conjugate pairs, and moved on. Now we build the full toolkit.

Here's what complex numbers actually are: points in a two-dimensional plane,
where one axis is the real line you already know and the other is
perpendicular to it. The imaginary axis. Together they form the **complex
plane**, and every complex number is just a point on it.

That's the entire concept. Two-dimensional numbers. Once you see them that
way, the algebra becomes geometry — which is exactly how engineers use them.

An AC voltage can be represented as a point rotating around the origin of
the complex plane. Its projection onto the real axis is what you measure
with a voltmeter. The phase angle is the angle from the real axis. The
phasor representation of AC circuits is nothing but complex numbers in
polar form.

The Fourier transform, which decomposes any signal into its frequency
components, is an integral over complex exponentials.

The natural frequencies of a structure are the roots of a characteristic
polynomial — which are often complex, and the imaginary part is the
oscillation frequency.

All of that starts here.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 12.1 Define the imaginary unit $j$ and perform arithmetic with $j$
* 12.2 Write complex numbers in rectangular form and identify real and
  imaginary parts
* 12.3 Add, subtract, multiply, and divide complex numbers in rectangular
  form
* 12.4 Compute the complex conjugate and use it for division
* 12.5 Convert between rectangular and polar form
* 12.6 State and apply Euler's identity
* 12.7 Multiply and divide complex numbers in polar form
* 12.8 Find powers and roots using De Moivre's theorem
* 12.9 Recognize the phasor representation of AC signals

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $j$ | imaginary unit, $j^2 = -1$ | Handbook convention; physics uses $i$ |
| $z$ | a complex number | — |
| $a$ | real part of $z$, $\text{Re}(z)$ | — |
| $b$ | imaginary part of $z$, $\text{Im}(z)$ | — |
| $\lvert z \rvert$ or $r$ | modulus (magnitude) of $z$ | — |
| $\theta$ or $\angle\theta$ | argument (angle) of $z$ | in radians or degrees |
| $z^*$ or $\bar{z}$ | complex conjugate of $z$ | — |

> ---
> **Mentor's Margin**
>
> This guide uses $j$, matching the Handbook and electrical engineering
> convention. Physics and pure mathematics use $i$. If you read a physics
> text or a math textbook, replace every $j$ in your head with $i$. The
> algebra is identical; only the letter changes. The Handbook flags this
> convention explicitly on page 38.
>
> ---

---

## 12.1 The Imaginary Unit

The imaginary unit $j$ is defined by:

$$\boxed{j^2 = -1 \qquad j = \sqrt{-1}}$$

Powers of $j$ cycle with period 4:

$$j^0 = 1 \qquad j^1 = j \qquad j^2 = -1 \qquad j^3 = -j \qquad j^4 = 1 \qquad \ldots$$

To find $j^n$ for any positive integer $n$: divide $n$ by 4 and look at the
remainder.

$$j^{47} = j^{4(11)+3} = (j^4)^{11} \cdot j^3 = 1^{11} \cdot (-j) = -j$$

---

## 12.2 Rectangular Form

A **complex number** in rectangular form:

$$\boxed{z = a + jb}$$

where $a$ is the **real part** and $b$ is the **imaginary part** (both real
numbers).

On the **complex plane** (also called the Argand diagram): $a$ is the
horizontal coordinate and $b$ is the vertical coordinate.

![FIG-01-12-001: Complex plane (Argand diagram) showing point z = a + jb plotted as a point with real axis horizontal and imaginary axis vertical; modulus r shown as the distance from origin, angle theta shown from positive real axis](../figures/FIG-01-12-001-complex-plane.png)

### Arithmetic in rectangular form

**Addition/subtraction:** add or subtract real and imaginary parts separately.

$$(a + jb) \pm (c + jd) = (a \pm c) + j(b \pm d)$$

**Multiplication:** expand and collect, using $j^2 = -1$.

$$(a + jb)(c + jd) = ac + jad + jbc + j^2bd = (ac - bd) + j(ad + bc)$$

**Complex conjugate:** reverse the sign of the imaginary part.

$$z = a + jb \implies z^* = a - jb$$

Key property: $z \cdot z^* = a^2 + b^2 = \lvert z \rvert^2$ (always real and
non-negative).

**Division:** multiply numerator and denominator by the conjugate of the
denominator.

$$\frac{z_1}{z_2} = \frac{a+jb}{c+jd} \cdot \frac{c-jd}{c-jd} = \frac{(ac+bd) + j(bc-ad)}{c^2+d^2}$$

> ---
> **Mentor's Margin**
>
> Division by a complex number *always* uses the conjugate. Never try to
> divide by splitting the fraction — $\frac{a+jb}{c+jd} \ne \frac{a}{c} +
> j\frac{b}{d}$. That is not a valid algebraic step. Multiply by
> $(c-jd)/(c-jd)$ and the denominator becomes real. Then the division is
> straightforward.
>
> ---

### Worked Example 1 — Rectangular Arithmetic

**Given.** $z_1 = 3 + 4j$ and $z_2 = 1 - 2j$. Find:
(a) $z_1 + z_2$, (b) $z_1 \cdot z_2$, (c) $z_1 / z_2$.

**Solution.**

(a) $(3 + 1) + j(4 + (-2)) = \boxed{4 + 2j}$

(b) $(3)(1) + (3)(-2j) + (4j)(1) + (4j)(-2j)$
$= 3 - 6j + 4j - 8j^2 = 3 - 2j - 8(-1) = 3 + 8 - 2j = \boxed{11 - 2j}$

(c) Multiply by conjugate of denominator:

$$\frac{3+4j}{1-2j} \cdot \frac{1+2j}{1+2j} = \frac{(3)(1)+(3)(2j)+(4j)(1)+(4j)(2j)}{1^2+2^2}$$

$$= \frac{3 + 6j + 4j + 8j^2}{5} = \frac{3 - 8 + 10j}{5} = \frac{-5 + 10j}{5} = \boxed{-1 + 2j}$$

**Check (c).** Verify: $(-1+2j)(1-2j) = -1+2j+2j-4j^2 = -1+4j+4 = 3+4j = z_1$ ✓

---

## 12.3 Polar Form and the Modulus

Every complex number $z = a + jb$ has a magnitude (modulus) and an angle
(argument):

$$\boxed{r = \lvert z \rvert = \sqrt{a^2 + b^2} \qquad \theta = \arg(z) = \arctan\!\left(\frac{b}{a}\right) + \text{quadrant correction}}$$

In polar form:

$$\boxed{z = r\angle\theta \quad \text{or} \quad z = r(\cos\theta + j\sin\theta)}$$

The Handbook writes the angle notation as $r\angle\theta$.

Converting back to rectangular:

$$a = r\cos\theta \qquad b = r\sin\theta$$

![FIG-01-12-002: Conversion diagram between rectangular (a + jb) and polar (r∠θ) forms, showing the right triangle relationship: r = sqrt(a² + b²), θ = arctan(b/a), a = r cosθ, b = r sinθ](../figures/FIG-01-12-002-rectangular-polar-conversion.png)

### Worked Example 2 — Converting Between Forms

**Given.** Convert: (a) $z = 3 + 4j$ to polar. (b) $z = 5\angle(-37°)$ to
rectangular.

**Solution.**

(a) $r = \sqrt{9 + 16} = \sqrt{25} = 5$.

$\theta = \arctan(4/3) = 53.1°$. Both $a > 0$ and $b > 0$: Q I, no
correction.

$$\boxed{z = 5\angle 53.1°}$$

(b) $a = 5\cos(-37°) = 5(0.7986) = 3.993 \approx 4.00$

$b = 5\sin(-37°) = 5(-0.6018) = -3.009 \approx -3.01$

$$\boxed{z = 4.00 - 3.01j}$$

**Check (b).** $\sqrt{4^2 + 3.01^2} = \sqrt{16 + 9.06} = \sqrt{25.06} \approx
5$ ✓

---

## 12.4 Euler's Identity

This is the most important equation in this chapter.

$$\boxed{e^{j\theta} = \cos\theta + j\sin\theta}$$

This is **Euler's formula**. It says the complex exponential is a unit
vector at angle $\theta$ on the complex plane.

Setting $\theta = \pi$:

$$e^{j\pi} = \cos\pi + j\sin\pi = -1 + j(0) = -1$$

$$\boxed{e^{j\pi} + 1 = 0}$$

That's **Euler's identity** — the famous result connecting $e$, $\pi$, $j$,
1, and 0 in one equation.

More practically, Euler's formula gives the third notation for complex
numbers:

$$z = re^{j\theta} = r(\cos\theta + j\sin\theta) = r\angle\theta$$

All three are equivalent. In most FE problems, you'll use the $\angle$
notation for ease. In calculus and differential equations, $e^{j\theta}$
is indispensable.

> ---
> **Mentor's Margin**
>
> The reason Euler's formula is true is that the power series for $e^x$,
> evaluated at $x = j\theta$, separates into the power series for
> $\cos\theta$ (real terms) and $j\sin\theta$ (imaginary terms). This isn't
> a coincidence — it's the bridge between the exponential function and
> trigonometry that makes complex analysis possible. We'll use the power
> series in Chapter 01-27 (Laplace transforms) and Chapter 01-28 (Fourier
> transforms). For now, treat it as a fact: $e^{j\theta}$ lands on the unit
> circle at angle $\theta$.
>
> ---

---

## 12.5 Multiplication and Division in Polar Form

In polar form, multiplication and division become elegant:

$$\boxed{z_1 \cdot z_2 = r_1 r_2 \angle(\theta_1 + \theta_2)}$$

$$\boxed{\frac{z_1}{z_2} = \frac{r_1}{r_2}\angle(\theta_1 - \theta_2)}$$

**Multiply the moduli, add the angles. Divide the moduli, subtract the
angles.**

This is why polar form is preferred for multiplication and division, and
rectangular form is preferred for addition and subtraction.

### Worked Example 3 — Polar Multiplication and Division

**Given.** $z_1 = 4\angle 30°$ and $z_2 = 2\angle 75°$.

(a) $z_1 \cdot z_2$. (b) $z_1 / z_2$. (c) $z_1^2$.

**Solution.**

(a) $z_1 z_2 = (4)(2)\angle(30° + 75°) = \boxed{8\angle 105°}$

(b) $z_1/z_2 = (4/2)\angle(30° - 75°) = \boxed{2\angle(-45°)}$

(c) $z_1^2 = (4)^2\angle(2 \times 30°) = \boxed{16\angle 60°}$

**Check (c) using rectangular:**

$z_1 = 4\cos30° + 4j\sin30° = 3.464 + 2j$

$z_1^2 = (3.464 + 2j)^2 = 12.0 + 13.856j + 4j^2 = 8.0 + 13.856j$

Convert back: $r = \sqrt{64 + 192} = \sqrt{256} = 16$ ✓

$\theta = \arctan(13.856/8.0) = \arctan(1.732) = 60°$ ✓

---

## 12.6 De Moivre's Theorem

For integer powers:

$$\boxed{(r\angle\theta)^n = r^n\angle(n\theta)}$$

Or equivalently:

$$(\cos\theta + j\sin\theta)^n = \cos(n\theta) + j\sin(n\theta)$$

**For roots:** the $n$th roots of $r\angle\theta$ are:

$$z_k = r^{1/n}\angle\!\left(\frac{\theta + 360°k}{n}\right) \quad k = 0, 1, 2, \ldots, n-1$$

There are exactly $n$ distinct $n$th roots, equally spaced around a circle
of radius $r^{1/n}$.

### Worked Example 4 — Finding Cube Roots

**Given.** Find all cube roots of $8$.

**Solution.**

Write $8 = 8\angle 0°$ (modulus 8, angle 0°).

The three cube roots have modulus $8^{1/3} = 2$ and angles:

$$\theta_k = \frac{0° + 360°k}{3} = 120°k \quad k = 0, 1, 2$$

$$z_0 = 2\angle 0° = 2 \qquad z_1 = 2\angle 120° \qquad z_2 = 2\angle 240°$$

In rectangular form:

$z_0 = 2$ (the real cube root)

$z_1 = 2(\cos 120° + j\sin 120°) = 2(-1/2 + j\sqrt{3}/2) = -1 + j\sqrt{3}$

$z_2 = 2(\cos 240° + j\sin 240°) = 2(-1/2 - j\sqrt{3}/2) = -1 - j\sqrt{3}$

**Check $z_1$:** $(-1+j\sqrt{3})^3$. Let me verify via modulus: $\lvert z_1
\rvert = \sqrt{1+3} = 2$, and $\lvert z_1^3 \rvert = 2^3 = 8$ ✓. Angle of
$z_1^3 = 3 \times 120° = 360° = 0°$ ✓, so $z_1^3 = 8\angle 0° = 8$ ✓.

---

## 12.7 Phasors — The Engineering Application

In AC circuit analysis, a sinusoidal voltage at frequency $f$:

$$v(t) = V_m \cos(\omega t + \phi)$$

is represented as a **phasor**:

$$\mathbf{V} = V_m \angle\phi$$

The phasor captures the amplitude and phase. The time variation $e^{j\omega t}$
is understood and dropped.

![FIG-01-12-003: Phasor diagram showing two phasors V1 and V2 on the complex plane with their sum phasor, angles from the real axis, and the relationship to the time-domain waveforms drawn alongside](../figures/FIG-01-12-003-phasor-diagram.png)

**Phasor addition:** use rectangular form.

**Phasor multiplication (impedances):** use polar form.

For a resistor, inductor, and capacitor at angular frequency $\omega$:

| Element | Impedance | Phasor form |
|---|---|---|
| Resistor $R$ | $R$ | $R\angle 0°$ |
| Inductor $L$ | $j\omega L$ | $\omega L\angle 90°$ |
| Capacitor $C$ | $\dfrac{1}{j\omega C}$ | $\dfrac{1}{\omega C}\angle(-90°)$ |

*(Full AC circuit analysis is in Chapter 02-64. These are preview notes.)*

> ---
> **Mentor's Margin**
>
> The $j$ in $j\omega L$ is not algebraic decoration — it means the inductor
> voltage leads the current by 90° on the complex plane. The $-j$ in
> $1/(j\omega C)$ means the capacitor voltage lags the current by 90°.
> Remember "ELI the ICE man" from the CETa foundation — Voltage leads
> current in an inductive circuit (ELI), current leads voltage in a
> capacitive circuit (ICE). Complex impedances make that phase relationship
> algebraic, which is exactly why phasors are useful.
>
> ---

---

## As the Handbook States It

> **Handbook 10.6, pp. 38–39** — *Mathematics / Algebra / Complex Numbers*

The Handbook includes:

- Definition of $j$ and rectangular form $a + jb$
- Modulus: $\lvert z \rvert = \sqrt{a^2 + b^2}$
- Argument: $\theta = \arctan(b/a)$ with the note to use all four quadrants
- Polar form: $r\angle\theta$ and $r(\cos\theta + j\sin\theta)$
- Euler's formula: $e^{j\theta} = \cos\theta + j\sin\theta$
- Multiplication: magnitudes multiply, angles add
- Division: magnitudes divide, angles subtract
- Complex conjugate
- Powers via De Moivre's theorem

**Notation note.** The Handbook uses both $j$ and $\theta$ in radians for
the Euler formula and states explicitly that "some disciplines use $i$."
This guide uses $j$ throughout.

**What's not in the Handbook — memorize:**

- The powers-of-$j$ cycle
- The procedure for division using conjugate multiplication
- The $n$th root formula with $k = 0, 1, \ldots, n-1$
- The phasor representation and what phase angle physically means

---

## Where This Goes Wrong

**$j^2$ treated as $+1$.** $j^2 = -1$. Every time. This is the definition.
Writing $(jb)^2 = b^2$ instead of $-b^2$ collapses complex arithmetic into
garbage.

**Forgetting the quadrant correction when computing the argument.** Same
issue as arctan in Chapter 01-11. $a < 0$ means you're not in Q I or Q IV —
add $180°$ to the raw arctan result.

**Dividing by a complex number without multiplying by the conjugate.**
$1/(a + jb) \ne 1/a + 1/(jb)$. Multiply top and bottom by $(a - jb)$.

**Mixing rectangular and polar operations.** Add and subtract in rectangular.
Multiply and divide in polar. Switching forms mid-calculation without
converting is a reliable source of errors.

**Losing track of the imaginary part.** When expanding $(a+jb)(c+jd)$, the
term $j^2bd$ becomes $-bd$ and is real, not imaginary. It moves to the real
part. Missing this gives a wrong real part.

**De Moivre's roots: using only $k = 0$.** There are $n$ distinct $n$th roots.
$k = 0$ gives one of them. The rest are at $+360°/n$ angular intervals. In
characteristic equation problems, all roots are needed.

**Phase angle in the wrong quadrant.** A phasor at 200° and a phasor at
$-160°$ are the same phasor (differ by 360°). The Handbook and most circuit
analyses express phase angles in $(-180°, 180°]$.

---

## Key Terms

| Term | Definition |
|---|---|
| Imaginary unit $j$ | Defined by $j^2 = -1$; $j = \sqrt{-1}$ |
| Complex number | $z = a + jb$ where $a$ (real part) and $b$ (imaginary part) are real numbers |
| Complex plane | Two-dimensional plane with real horizontal axis and imaginary vertical axis |
| Modulus $\lvert z \rvert$ | Distance from origin: $\sqrt{a^2 + b^2}$; also called magnitude |
| Argument $\theta$ | Angle from positive real axis; $\arctan(b/a)$ with quadrant correction |
| Rectangular form | $z = a + jb$; preferred for addition and subtraction |
| Polar form | $z = r\angle\theta$ or $re^{j\theta}$; preferred for multiplication and division |
| Complex conjugate $z^*$ | $a - jb$; reverses the sign of the imaginary part |
| Euler's formula | $e^{j\theta} = \cos\theta + j\sin\theta$; connects exponential and trig functions |
| Euler's identity | $e^{j\pi} + 1 = 0$; special case of Euler's formula at $\theta = \pi$ |
| De Moivre's theorem | $(r\angle\theta)^n = r^n\angle(n\theta)$; extends to $n$th roots |
| Phasor | Complex number representing amplitude and phase of a sinusoidal signal; time variation suppressed |
| Argand diagram | Another name for the complex plane |

---

## Review Questions

### Conceptual

1. What is $j^2$? What is $j^3$? Explain the four-cycle pattern for powers
   of $j$.
2. Why is division by a complex number performed by multiplying numerator
   and denominator by the conjugate of the denominator?
3. State Euler's formula. What does it mean geometrically — what curve does
   $e^{j\theta}$ trace as $\theta$ increases from 0 to $2\pi$?
4. When should you use rectangular form and when polar form for complex
   arithmetic? Explain why each form is preferred for its operation.
5. A complex number has modulus 3 and argument $-90°$. What is it in
   rectangular form without a calculator?
6. Explain why De Moivre's theorem gives $n$ distinct $n$th roots, not just
   one. Where are they located relative to each other on the complex plane?
7. In AC circuit analysis, what physical quantities do the modulus and
   argument of a phasor represent?

### Calculation

8. Compute each power of $j$ without a calculator:
   (a) $j^{13}$ (b) $j^{38}$ (c) $j^{101}$ (d) $j^{-3}$

9. Perform each operation in rectangular form:
   (a) $(5 - 2j) + (-3 + 7j)$
   (b) $(2 + 3j)(4 - j)$
   (c) $(1 + j)^2$
   (d) $\dfrac{2 + 5j}{3 - 4j}$
   (e) $\dfrac{1}{j}$
   (f) $\dfrac{3 + j}{j}$

10. Find the modulus and argument of each:
    (a) $z = -4 + 4j$
    (b) $z = -5 - 5\sqrt{3}\,j$
    (c) $z = 6j$
    (d) $z = -7$

11. Convert to polar form $r\angle\theta$ with $\theta \in (-180°, 180°]$:
    (a) $z = 1 + \sqrt{3}\,j$
    (b) $z = -3 - 3j$
    (c) $z = 5 - 12j$

12. Convert to rectangular form:
    (a) $z = 4\angle 120°$
    (b) $z = 3\angle(-150°)$
    (c) $z = 2\angle 45°$

13. Perform in polar form:
    (a) $(3\angle 40°)(5\angle 70°)$
    (b) $\dfrac{12\angle 200°}{4\angle 80°}$
    (c) $(2\angle 30°)^4$

14. Find all indicated roots and express in both polar and rectangular form:
    (a) Square roots of $4j$
    (b) Cube roots of $-27$
    (c) Fourth roots of $16\angle 0°$

15. Verify Euler's formula numerically at $\theta = \pi/3$:
    (a) Compute $e^{j\pi/3}$ using $\cos(\pi/3) + j\sin(\pi/3)$.
    (b) Show that $\lvert e^{j\pi/3} \rvert = 1$.
    (c) Express the result in rectangular form using exact values.

16. **Engineering application.** An AC circuit has:
    - Source voltage phasor: $\mathbf{V}_s = 120\angle 0°$ V
    - Impedance: $\mathbf{Z} = 30 + 40j \;\Omega$

    (a) Convert $\mathbf{Z}$ to polar form.
    (b) Find the current phasor $\mathbf{I} = \mathbf{V}_s / \mathbf{Z}$
    in polar form.
    (c) Convert $\mathbf{I}$ to rectangular form.
    (d) Find the voltage across the resistor: $\mathbf{V}_R = \mathbf{I}
    \times R$ where $R = 30\;\Omega$.
    (e) Find the voltage across the inductor: $\mathbf{V}_L = \mathbf{I}
    \times j40$.

17. **Engineering application.** Two AC voltages are:
    $v_1(t) = 100\cos(\omega t + 30°)$ V and $v_2(t) = 80\cos(\omega t - 45°)$ V.

    (a) Write their phasors $\mathbf{V}_1$ and $\mathbf{V}_2$.
    (b) Find the phasor of the sum $\mathbf{V}_s = \mathbf{V}_1 + \mathbf{V}_2$.
    (c) Convert the sum to polar form and write the corresponding
    time-domain expression $v_s(t)$.

### Multiple Choice

18. $j^{22}$ equals:
    A) $1$
    B) $j$
    C) $-1$
    D) $-j$

19. The complex conjugate of $3 - 5j$ is:
    A) $-3 + 5j$
    B) $3 + 5j$
    C) $5 - 3j$
    D) $-3 - 5j$

20. The modulus of $z = 5 - 12j$ is:
    A) $7$
    B) $13$
    C) $17$
    D) $\sqrt{119}$

21. In polar form, $(2\angle 30°)^3$ equals:
    A) $6\angle 90°$
    B) $6\angle 30°$
    C) $8\angle 90°$
    D) $8\angle 30°$

22. $e^{j\pi/2}$ equals:
    A) $-1$
    B) $1$
    C) $j$
    D) $-j$

23. Which form is preferred for dividing two complex numbers?
    A) Rectangular, using the quotient rule
    B) Polar, by dividing moduli and subtracting angles
    C) Either form gives the same computation effort
    D) Exponential form only

24. A phasor $\mathbf{V} = 50\angle(-30°)$ V represents a sinusoid with:
    A) Amplitude 50 V, lagging the reference by 30°
    B) Amplitude 50 V, leading the reference by 30°
    C) RMS value 50 V, lagging by 30°
    D) Peak-to-peak value 50 V, lagging by 30°

25. The product $(z)(z^*)$ always equals:
    A) $\lvert z \rvert$
    B) $\lvert z \rvert^2$
    C) $z^2$
    D) $2\,\text{Re}(z)$

---

## Answer Key with Explanations

**1.** $j^2 = -1$ by definition. $j^3 = j^2 \cdot j = -j$. The cycle:
$j^0=1, j^1=j, j^2=-1, j^3=-j, j^4=1$ and repeats. To find $j^n$: divide
$n$ by 4 and use the remainder: remainder 0 → 1, remainder 1 → $j$,
remainder 2 → $-1$, remainder 3 → $-j$. (§12.1)

**2.** Because a real denominator is required for the final rectangular form.
$(a+jb)/(c+jd)$ has a complex denominator; multiplying by $(c-jd)/(c-jd) = 1$
converts the denominator to $c^2+d^2$, which is real, making division
straightforward. Any other approach either changes the value of the expression
or leaves a complex denominator. (§12.2)

**3.** Euler's formula: $e^{j\theta} = \cos\theta + j\sin\theta$. Geometrically,
as $\theta$ increases from 0 to $2\pi$, the point $(\cos\theta, \sin\theta)$
traces the **unit circle** counterclockwise. At $\theta = 0$: point $(1,0)$.
At $\theta = \pi/2$: point $(0,1) = j$. At $\theta = \pi$: point $(-1,0) = -1$.
At $\theta = 2\pi$: back to $(1,0)$. The complex exponential is a point rotating
on the unit circle. (§12.4)

**4.** **Rectangular** for addition and subtraction — you just add or subtract
the real and imaginary parts directly. **Polar** for multiplication and
division — moduli multiply/divide and angles add/subtract, which is far
simpler than expanding rectangular products or applying the conjugate method
repeatedly. Converting between forms takes seconds and is worth it to use
the right form for each operation. (§12.5)

**5.** Modulus 3, argument $-90°$. Converting:
$a = 3\cos(-90°) = 3(0) = 0$ and $b = 3\sin(-90°) = 3(-1) = -3$.
So $z = 0 - 3j = \boxed{-3j}$. (§12.3)

**6.** De Moivre's theorem for the $n$th root of $r\angle\theta$ gives angles
$(\theta + 360°k)/n$ for $k = 0, 1, \ldots, n-1$. Each value of $k$ gives a
different angle, and there are exactly $n$ of them before the pattern repeats
(adding another $360°$ to the numerator returns to the starting angle). They
are equally spaced by $360°/n$ around a circle of radius $r^{1/n}$. For
example, cube roots are $120°$ apart; square roots are $180°$ apart. (§12.6)

**7.** The **modulus** represents the amplitude of the sinusoid (peak value).
The **argument** represents the phase angle — how much the sinusoid leads or
lags a chosen reference. A positive angle means leading; a negative angle
means lagging. (§12.7)

**8.**

(a) $j^{13}$: $13 = 4(3) + 1$; remainder 1 → $\boxed{j}$

(b) $j^{38}$: $38 = 4(9) + 2$; remainder 2 → $\boxed{-1}$

(c) $j^{101}$: $101 = 4(25) + 1$; remainder 1 → $\boxed{j}$

(d) $j^{-3}$: $j^{-3} = 1/j^3 = 1/(-j) = -1/j \cdot (j/j) = -j/j^2 = -j/(-1) = \boxed{j}$

Alternatively: $j^{-3} = j^{4-3} \cdot j^{-4} = j^1 \cdot 1 = j$ (since
$j^4 = 1$).

**9.**

(a) $(5-3) + (-2+7)j = \boxed{2 + 5j}$

(b) $2(4) + 2(-j) + 3j(4) + 3j(-j) = 8 - 2j + 12j - 3j^2 = 8+3+10j =
\boxed{11 + 10j}$

(c) $(1+j)^2 = 1 + 2j + j^2 = 1 + 2j - 1 = \boxed{2j}$

(d) $\dfrac{2+5j}{3-4j} \cdot \dfrac{3+4j}{3+4j} = \dfrac{6 + 8j + 15j + 20j^2}{9+16}
= \dfrac{6-20+(8+15)j}{25} = \dfrac{-14 + 23j}{25} = \boxed{-0.56 + 0.92j}$

(e) $\dfrac{1}{j} \cdot \dfrac{-j}{-j} = \dfrac{-j}{-j^2} = \dfrac{-j}{1} =
\boxed{-j}$

(f) $\dfrac{3+j}{j} \cdot \dfrac{-j}{-j} = \dfrac{-3j - j^2}{-j^2} =
\dfrac{-3j+1}{1} = \boxed{1 - 3j}$

**10.**

(a) $r = \sqrt{16+16} = \sqrt{32} = 4\sqrt{2}$.
$\theta$: $a=-4 < 0$, $b=4 > 0$ → Q II.
$\theta = \arctan(4/(-4)) + 180° = -45° + 180° = \boxed{135°}$

(b) $r = \sqrt{25 + 75} = \sqrt{100} = 10$.
$a=-5<0$, $b=-5\sqrt{3}<0$ → Q III.
$\theta = \arctan\!\left(\frac{-5\sqrt{3}}{-5}\right) + 180° = \arctan(\sqrt{3}) + 180°
= 60° + 180° = \boxed{240°}$

Or equivalently $-120°$ in the range $(-180°, 180°]$: $\boxed{-120°}$.

(c) $r = 6$. The point $(0, 6)$ lies on the positive imaginary axis:
$\theta = \boxed{90°}$

(d) $r = 7$. The point $(-7, 0)$ lies on the negative real axis:
$\theta = \boxed{180°}$

**11.**

(a) $r = \sqrt{1+3} = 2$. $\theta = \arctan(\sqrt{3}/1) = 60°$; Q I, no correction.
$\boxed{2\angle 60°}$

(b) $r = \sqrt{9+9} = 3\sqrt{2}$. Q III: $\theta = \arctan(1) + 180° = 45°+180°
= 225°$. In $(-180°,180°]$: $225°-360° = -135°$.
$\boxed{3\sqrt{2}\angle(-135°)}$

(c) $r = \sqrt{25+144} = \sqrt{169} = 13$. Q IV: $\theta = \arctan(-12/5) =
-67.4°$.
$\boxed{13\angle(-67.4°)}$

**12.**

(a) $4\cos120° + 4j\sin120° = 4(-1/2) + 4j(\sqrt{3}/2) = \boxed{-2 + 2\sqrt{3}\,j}$

(b) $3\cos(-150°) + 3j\sin(-150°) = 3(-\sqrt{3}/2) + 3j(-1/2) =
\boxed{-\frac{3\sqrt{3}}{2} - \frac{3}{2}j}$

(c) $2\cos45° + 2j\sin45° = 2(\sqrt{2}/2) + 2j(\sqrt{2}/2) =
\boxed{\sqrt{2} + \sqrt{2}\,j}$

**13.**

(a) $3 \times 5 \angle(40°+70°) = \boxed{15\angle 110°}$

(b) $\dfrac{12}{4}\angle(200°-80°) = \boxed{3\angle 120°}$

(c) $2^4\angle(4 \times 30°) = \boxed{16\angle 120°}$

**14.**

**(a) Square roots of $4j$.**

Write $4j = 4\angle 90°$.

$r^{1/2} = \sqrt{4} = 2$. Angles: $(90° + 360°k)/2$ for $k = 0, 1$.

$z_0 = 2\angle 45° = 2(\cos45°+j\sin45°) = \sqrt{2}+j\sqrt{2}$

$z_1 = 2\angle 225° = 2\angle(-135°) = -\sqrt{2}-j\sqrt{2}$

$$\boxed{z_0 = \sqrt{2}+j\sqrt{2}, \quad z_1 = -\sqrt{2}-j\sqrt{2}}$$

Verify $z_0^2$: $(\sqrt{2}+j\sqrt{2})^2 = 2 + 2 \cdot \sqrt{2} \cdot j\sqrt{2}
+ j^2 \cdot 2 = 2 + 4j - 2 = 4j$ ✓

**(b) Cube roots of $-27$.**

$-27 = 27\angle 180°$.

$r^{1/3} = 3$. Angles: $(180°+360°k)/3$ for $k = 0,1,2$.

$z_0 = 3\angle 60° = 3/2 + j3\sqrt{3}/2$

$z_1 = 3\angle 180° = -3$

$z_2 = 3\angle 300° = 3\angle(-60°) = 3/2 - j3\sqrt{3}/2$

$$\boxed{z_0 = \tfrac{3}{2}+j\tfrac{3\sqrt{3}}{2}, \quad z_1 = -3, \quad z_2 = \tfrac{3}{2}-j\tfrac{3\sqrt{3}}{2}}$$

Check $z_1^3 = (-3)^3 = -27$ ✓

**(c) Fourth roots of $16\angle 0°$.**

$r^{1/4} = 16^{1/4} = 2$. Angles: $(0°+360°k)/4 = 90°k$ for $k=0,1,2,3$.

$z_0 = 2\angle 0° = 2$

$z_1 = 2\angle 90° = 2j$

$z_2 = 2\angle 180° = -2$

$z_3 = 2\angle 270° = -2j$

$$\boxed{z_0 = 2, \quad z_1 = 2j, \quad z_2 = -2, \quad z_3 = -2j}$$

These are the four roots on a circle of radius 2, spaced 90° apart. ✓

**15.**

(a) $e^{j\pi/3} = \cos(\pi/3) + j\sin(\pi/3) = \dfrac{1}{2} + j\dfrac{\sqrt{3}}{2}$

(b) $\left\lvert\dfrac{1}{2} + j\dfrac{\sqrt{3}}{2}\right\rvert = \sqrt{(1/2)^2
+ (\sqrt{3}/2)^2} = \sqrt{1/4 + 3/4} = \sqrt{1} = 1$ ✓

(c) Exact rectangular form: $\boxed{\dfrac{1}{2} + j\dfrac{\sqrt{3}}{2}}$

**16.**

(a) $\lvert\mathbf{Z}\rvert = \sqrt{30^2+40^2} = \sqrt{900+1600} = \sqrt{2500}
= 50\;\Omega$.
$\theta_Z = \arctan(40/30) = \arctan(1.333) = 53.13°$; Q I.

$$\boxed{\mathbf{Z} = 50\angle 53.13°\;\Omega}$$

(b) $\mathbf{I} = \dfrac{120\angle 0°}{50\angle 53.13°} = \dfrac{120}{50}
\angle(0°-53.13°) = \boxed{2.4\angle(-53.13°)\;\text{A}}$

(c) $\mathbf{I} = 2.4\cos(-53.13°) + j\cdot 2.4\sin(-53.13°)$
$= 2.4(0.6) + j\cdot 2.4(-0.8) = \boxed{1.44 - 1.92j\;\text{A}}$

(d) $\mathbf{V}_R = \mathbf{I} \times R = (1.44-1.92j)(30) = \boxed{43.2-57.6j\;\text{V}}$

Or in polar: $2.4\angle(-53.13°) \times 30\angle 0° = 72\angle(-53.13°)$ V ✓

(e) $\mathbf{V}_L = \mathbf{I} \times j40 = (1.44-1.92j)(j40)$
$= 57.6j - 76.8j^2 = 57.6j + 76.8 = \boxed{76.8 + 57.6j\;\text{V}}$

Or in polar: $2.4\angle(-53.13°) \times 40\angle 90° = 96\angle 36.87°$ V

Convert: $96\cos(36.87°) + 96j\sin(36.87°) = 96(0.800) + 96j(0.600) =
76.8 + 57.6j$ ✓

**Check.** $\mathbf{V}_R + \mathbf{V}_L = (43.2-57.6j) + (76.8+57.6j) =
120 + 0j = 120\angle 0° = \mathbf{V}_s$ ✓ Kirchhoff's voltage law is satisfied.

**17.**

(a) $\mathbf{V}_1 = 100\angle 30°\;\text{V}$, $\mathbf{V}_2 = 80\angle(-45°)\;\text{V}$

(b) Convert to rectangular to add:

$\mathbf{V}_1 = 100\cos30° + j100\sin30° = 86.60 + 50.00j$

$\mathbf{V}_2 = 80\cos(-45°) + j80\sin(-45°) = 56.57 - 56.57j$

$\mathbf{V}_s = (86.60+56.57) + j(50.00-56.57) = 143.17 - 6.57j$

(c) $\lvert\mathbf{V}_s\rvert = \sqrt{143.17^2+6.57^2} = \sqrt{20{,}498+43.2}
= \sqrt{20{,}541} = 143.3\;\text{V}$

$\theta_s = \arctan(-6.57/143.17) = \arctan(-0.0459) = -2.63°$; Q IV
(both components: real positive, imaginary negative), no further correction.

$$\mathbf{V}_s = 143.3\angle(-2.63°)\;\text{V}$$

$$\boxed{v_s(t) = 143.3\cos(\omega t - 2.63°)\;\text{V}}$$

**Check.** At $t=0$: $v_1(0) = 100\cos30° = 86.6$ V, $v_2(0) = 80\cos(-45°)
= 56.6$ V. Sum $= 143.2$ V. And $v_s(0) = 143.3\cos(-2.63°) = 143.3(0.999)
= 143.1$ V ✓

**18. C — $-1$.** $22 = 4(5)+2$; remainder 2 → $j^2 = -1$. (§12.1)

**19. B — $3 + 5j$.** The conjugate reverses the sign of the imaginary part
only. $\overline{3-5j} = 3+5j$. (§12.2)

**20. B — 13.** $\lvert 5-12j\rvert = \sqrt{25+144} = \sqrt{169} = 13$. This
is the 5-12-13 Pythagorean triple. (§12.3)

**21. C — $8\angle 90°$.** $2^3 = 8$ and $3 \times 30° = 90°$. (A) uses
wrong modulus; (B) and (D) don't apply De Moivre correctly. (§12.6)

**22. C — $j$.** $e^{j\pi/2} = \cos(\pi/2) + j\sin(\pi/2) = 0 + j(1) = j$.
Geometrically: angle $\pi/2 = 90°$ lands at the top of the unit circle,
which is the point $j$. (§12.4)

**23. B — Polar form.** Division in polar form requires only one division
(moduli) and one subtraction (angles). Division in rectangular form requires
multiplying by the conjugate, expanding, and simplifying — considerably more
work. (§12.5)

**24. A — Amplitude 50 V, lagging the reference by 30°.** The modulus of
a voltage phasor is the amplitude (peak value, not RMS). A negative phase
angle means the sinusoid lags the reference cosine by 30°. (§12.7)

**25. B — $\lvert z \rvert^2$.** $z \cdot z^* = (a+jb)(a-jb) = a^2 - j^2b^2
= a^2 + b^2 = \lvert z\rvert^2$. This is always real and non-negative.
(§12.2)

---

## Quick Reference

**Imaginary unit** — *Handbook p. 38*

$$j^2 = -1 \qquad j^3 = -j \qquad j^4 = 1$$

Powers cycle with period 4: remainder of $n \div 4$ → $\{1, j, -1, -j\}$

**Rectangular form**

$$z = a + jb \qquad \text{Re}(z)=a \qquad \text{Im}(z)=b$$

$$z \cdot z^* = a^2+b^2 = \lvert z\rvert^2 \qquad \frac{z_1}{z_2} = \frac{z_1 z_2^*}{\lvert z_2\rvert^2}$$

**Polar form** — *Handbook p. 38*

$$\lvert z\rvert = r = \sqrt{a^2+b^2} \qquad \theta = \arctan(b/a) + \text{quadrant correction}$$

$$z = r\angle\theta = r(\cos\theta + j\sin\theta) = re^{j\theta}$$

$$a = r\cos\theta \qquad b = r\sin\theta$$

**Operations**

| Operation | Preferred form | Rule |
|---|---|---|
| Add/subtract | Rectangular | Add real and imaginary parts |
| Multiply | Polar | $r_1 r_2 \angle(\theta_1+\theta_2)$ |
| Divide | Polar | $(r_1/r_2)\angle(\theta_1-\theta_2)$ |
| Power $n$ | Polar | $r^n\angle(n\theta)$ |
| $n$th root | Polar | $r^{1/n}\angle\!\left(\dfrac{\theta+360°k}{n}\right)$, $k=0,\ldots,n-1$ |

**Euler's formula** — *Handbook p. 38*

$$e^{j\theta} = \cos\theta + j\sin\theta \qquad e^{j\pi}+1=0$$

**Phasor shorthand**

$$v(t) = V_m\cos(\omega t+\phi) \;\longleftrightarrow\; \mathbf{V} = V_m\angle\phi$$

Impedances: $R\angle 0°$, $\;\omega L\angle 90°$, $\;\dfrac{1}{\omega C}\angle(-90°)$

**Not in the Handbook — memorize**

Powers-of-$j$ cycle · conjugate-multiplication division procedure ·
$n$th root formula with all $k$ values · phasor physical interpretation ·
quadrant correction for argument

---

## What's Next

Apprentice, complex numbers done. You now have the algebra of the complex
plane — rectangular form for adding, polar form for multiplying, Euler's
formula tying it all together.

In **Chapter 01-13: Vectors and Vector Operations**, we move into three
dimensions. A vector is a quantity with both magnitude and direction —
force, velocity, moment, field. The dot product gives you projections and
work. The cross product gives you moments and normals. Every statics
problem in Tier 2C and every field problem in Tier 2E uses the tools you'll
build in this chapter.

There's a satisfying connection to what you just learned: a 2D vector in
the $xy$-plane is a complex number. The magnitude and direction angle are
exactly the modulus and argument. What makes vectors more general is the
third dimension and the vector products — operations that don't have
complex-number analogues.

Bring the Handbook to page 37. The vector section begins there.

See you there.

— Your Mentor