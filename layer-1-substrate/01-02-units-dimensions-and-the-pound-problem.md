---
chapter: "01-02"
title: "Units, Dimensions, and the Pound Problem"
layer: 1
tier: A
template: technical
ledger_ids: [MATH-1A-002-01, MATH-1A-002-02, MATH-1A-002-03, MATH-1A-002-04]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-02: Units, Dimensions, and the Pound Problem

> *"The Handbook has several hundred pages. It chose to spend its very first
> half-page telling you that a pound isn't a pound. Somebody at NCEES knows
> exactly where the bodies are buried."*

---

## Before You Start

**Prerequisites:** [01-01 Numbers, Magnitude, and Metric Prefixes](01-01-numbers-magnitude-prefixes.md)

**Skip if:** You pass the Tier 1A test-out quiz. But read §1.6 anyway. I mean
it.

**Time:** ~70 min read · ~30 min review questions · ~60 min practice problems

---

## On the Board Today

Apprentice, this is the most important chapter in Layer 1. I don't say that
about many chapters, so take it seriously.

Two things happen here.

The first is elegant, and I think you'll enjoy it. Every physical quantity has
a **dimension** — a fundamental character, like length or mass or time — and
dimensions have to balance across an equation the way charges balance across a
chemical reaction. That gives you something remarkable: a free error check on
every calculation you will ever perform, for the rest of your career, at zero
cost. Set up an equation whose dimensions don't balance and you know it's
wrong before you plug in a single number. You don't need to know what the
right answer is. You only need to know that this one can't be it.

That's worth an hour of your attention on its own.

The second thing is uglier.

The U.S. Customary System uses the word **pound** for two different physical
quantities. Pound-mass and pound-force. They are not the same thing. They are
not interchangeable. And because engineers in the United States kept both
words and refused to give either one up, there is a conversion constant that
has to appear in equations to make the arithmetic work:

$$g_c = 32.174 \; \frac{\text{lbm} \cdot \text{ft}}{\text{lbf} \cdot \text{s}^2}$$

The Handbook puts that on its **first page**, ahead of everything else in the
entire document, and explicitly warns you not to confuse $g_c$ with local
gravitational acceleration $g$.

NCEES did not put it there by accident.

> **Mentor's Margin:** Here's what makes this the most expensive topic in the
> foundation. It doesn't take points from people who don't understand units.
> It takes points from people who are *certain* they already do. You've been
> converting inches to feet since grade school. You know what a pound is. And
> that confidence is exactly the thing that will cost you, because the trap
> isn't in the conversion — it's in the fact that two different quantities are
> wearing the same name.

So we're going to settle this once, at the bottom of the guide, properly and
completely. Not a rule to memorize. An actual understanding of why the
constant exists and where it has to appear.

Because four hundred pages from now, when you're calculating a pressure drop
in hour five of a six-hour exam, this needs to be automatic.

Get the Handbook open to page 1. Let's go.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 2.1 Distinguish a physical quantity, a dimension, and a unit
* 2.2 Name the seven SI base units and their quantities
* 2.3 Express common derived SI units in terms of base units
* 2.4 Test an equation for dimensional homogeneity and use the result as an
  error check
* 2.5 Convert between units using the factor-label method, carrying units
  through every step
* 2.6 Explain why the pound-mass / pound-force ambiguity exists in structural
  terms, not just as a rule
* 2.7 State the value, units, and meaning of $g_c$, and distinguish it from
  local gravitational acceleration $g$
* 2.8 Apply Newton's second law correctly in USCS units using either the $g_c$
  method or the slug method
* 2.9 Distinguish mass from weight and compute weight at non-standard gravity
* 2.10 Identify the other common equations in which $g_c$ appears
* 2.11 Convert among the four temperature scales, and distinguish a
  temperature value from a temperature difference
* 2.12 Locate and correctly select among the four printed forms of the
  universal gas constant

---

## Notation Used Here

| Symbol | Meaning in this chapter | SI | USCS |
|---|---|---|---|
| $m$ | mass | kg | lbm or slug |
| $F$ | force | N | lbf |
| $a$ | acceleration | m/s² | ft/s² |
| $F_W$ | weight (a force) | N | lbf |
| $g$ | local gravitational acceleration | m/s² | ft/s² |
| $g_c$ | force unit conversion constant | — | 32.174 lbm·ft/(lbf·s²) |
| $\rho$ | density | kg/m³ | lbm/ft³ |
| $SW$ | specific weight | N/m³ | lbf/ft³ |
| $p$ | pressure | Pa | lbf/ft² or psi |
| $h$ | height or depth | m | ft |
| $v$ | speed | m/s | ft/s |
| $T$ | temperature | K or °C | °R or °F |
| $\Delta T$ | temperature difference | K or °C | °R or °F |
| $\bar{R}$ | universal gas constant | see §1.8 | see §1.8 |
| $KE$, $PE$ | kinetic, potential energy | J | ft·lbf |

> **Collision notes.** Three symbols in this chapter carry other meanings
> elsewhere in the guide, and I'm flagging them now so you never get
> ambushed.
>
> **$F_W$ for weight.** Plain $W$ means *work* throughout this guide, because
> that's the more common use across seven disciplines. Weight is a force, so
> it gets a force symbol with a subscript. The Handbook is less careful about
> this; read for context.
>
> **$T$ for temperature.** In Tier 2C, $T_p$ is a period and $T_q$ is a
> torque. In this chapter $T$ is temperature only.
>
> **$\rho$ for density.** In Tier 2E, $\rho_e$ is resistivity; in Tier 1F,
> $r$ is a correlation coefficient. Here $\rho$ is density only.
>
> See [Notation Contract](../meta/notation.md).

---

## 2.1 Quantity, Dimension, Unit

Three words that get used interchangeably in casual speech and must not be
here.

A **physical quantity** is a measurable property of something. The length of a
beam. The mass of a truck. The temperature of a fluid.

A **dimension** is the fundamental character of that quantity, independent of
how you measure it. Length is a dimension. Mass is a dimension. Time is a
dimension.

A **unit** is a specific agreed-upon amount of a dimension, used as a
reference for measurement. The metre and the foot are both units of the
dimension length.

The relationship, stated plainly:

> **The same quantity has one dimension and many possible units.**

A beam that is 4 metres long is also 13.12 feet long, 157.5 inches long, and
$4 \times 10^9$ nanometres long. Four numbers, four units, one dimension:
length.

### The dimensional symbols

Engineering mechanics uses four dimensions constantly and three more
occasionally.

| Dimension | Symbol | SI base unit |
|---|---|---|
| Mass | $M$ | kilogram (kg) |
| Length | $L$ | metre (m) |
| Time | $T$ | second (s) |
| Thermodynamic temperature | $\Theta$ | kelvin (K) |
| Electric current | $I$ | ampere (A) |
| Amount of substance | $N$ | mole (mol) |
| Luminous intensity | $J$ | candela (cd) |

Everything else in engineering is built from these. Everything. Force,
pressure, energy, power, voltage, viscosity — all of them are combinations of
the seven.

> **Mentor's Margin:** That's not a bookkeeping curiosity, it's a deep fact
> about physics, and it's the entire reason dimensional analysis works. There
> is no such thing as a quantity with a genuinely new dimension. Every
> derived quantity you meet for the rest of your career decomposes into these
> seven, which means every equation you write can be checked against them.

---

## 2.2 The SI System

The **International System of Units**, abbreviated **SI** from the French
*Système International*, defines seven base units — one per base dimension —
and derives everything else from them.

### The seven base units

| Quantity | Unit | Symbol |
|---|---|---|
| Mass | kilogram | kg |
| Length | metre | m |
| Time | second | s |
| Thermodynamic temperature | kelvin | K |
| Electric current | ampere | A |
| Amount of substance | mole | mol |
| Luminous intensity | candela | cd |

Note that **the kilogram is the base unit of mass**, not the gram. It is the
only base unit carrying a prefix, which is a historical accident and
occasionally a nuisance.

### Derived units

A derived unit is a combination of base units. Many get their own names, which
is convenient but can obscure what they actually are. Here's the decomposition
for the ones you'll use most.

| Quantity | Unit | Symbol | In base units | Dimensions |
|---|---|---|---|---|
| Force | newton | N | kg·m/s² | $MLT^{-2}$ |
| Pressure, stress | pascal | Pa | kg/(m·s²) | $ML^{-1}T^{-2}$ |
| Energy, work | joule | J | kg·m²/s² | $ML^2T^{-2}$ |
| Power | watt | W | kg·m²/s³ | $ML^2T^{-3}$ |
| Frequency | hertz | Hz | 1/s | $T^{-1}$ |
| Electric charge | coulomb | C | A·s | $IT$ |
| Voltage | volt | V | kg·m²/(A·s³) | $ML^2T^{-3}I^{-1}$ |
| Resistance | ohm | Ω | kg·m²/(A²·s³) | $ML^2T^{-3}I^{-2}$ |
| Capacitance | farad | F | A²·s⁴/(kg·m²) | $M^{-1}L^{-2}T^4I^2$ |

You do not need to memorize that table. You do need to be able to *rebuild*
any row of it from a definition you know:

$$\text{Force} = \text{mass} \times \text{acceleration} \quad \Rightarrow \quad 1 \text{ N} = 1 \text{ kg} \cdot \frac{\text{m}}{\text{s}^2}$$

$$\text{Pressure} = \frac{\text{force}}{\text{area}} \quad \Rightarrow \quad 1 \text{ Pa} = \frac{1 \text{ N}}{1 \text{ m}^2} = \frac{\text{kg}}{\text{m} \cdot \text{s}^2}$$

$$\text{Work} = \text{force} \times \text{distance} \quad \Rightarrow \quad 1 \text{ J} = 1 \text{ N} \cdot \text{m} = \frac{\text{kg} \cdot \text{m}^2}{\text{s}^2}$$

$$\text{Power} = \frac{\text{work}}{\text{time}} \quad \Rightarrow \quad 1 \text{ W} = \frac{1 \text{ J}}{1 \text{ s}} = \frac{\text{kg} \cdot \text{m}^2}{\text{s}^3}$$

That's the skill worth having. Memorizing the table is fragile; rebuilding it
from physics is permanent.

### Why SI is internally clean

Here is the property that matters, and it will matter enormously in §1.6:

> **In SI, mass is a base unit and force is derived from it.**

The newton is *defined* as the force that accelerates one kilogram at one
metre per second squared. So Newton's second law works with no fudge factor at
all:

$$F = ma$$

Substitute kg and m/s², get newtons. No constants. No conversions. Nothing to
remember.

Hold onto that. It's the thing USCS gives up.

---

## 2.3 The USCS System

The **U.S. Customary System** is the other system on your exam. NCEES states
plainly in every specification sheet that the FE uses both.

| Quantity | Unit | Symbol |
|---|---|---|
| Length | foot | ft |
| Time | second | s or sec |
| Force | pound-force | lbf |
| Mass | pound-mass | lbm |
| Mass (coherent) | slug | slug |
| Temperature (absolute) | degree Rankine | °R |
| Temperature (relative) | degree Fahrenheit | °F |

Look at that list carefully. Count the entries for mass and force.

**There are three: pound-force, pound-mass, and slug.**

That is one more than the system needs, and that surplus is the entire source
of the problem we're about to dissect.

### Common USCS derived units

| Quantity | Unit | Note |
|---|---|---|
| Pressure, stress | lbf/in² (psi) | also lbf/ft² (psf) |
| Energy, work | ft·lbf | also Btu for heat |
| Power | ft·lbf/s | also horsepower, hp |
| Density | lbm/ft³ | mass per volume |
| Specific weight | lbf/ft³ | **force** per volume |

That last pair deserves a hard look. Density and specific weight have the same
*shape* — something per cubic foot — but they are different dimensions.
Density is $ML^{-3}$. Specific weight is force per volume, $ML^{-2}T^{-2}$.
Water is 62.4 lbm/ft³ **and** 62.4 lbf/ft³, and the fact that those two
numbers are identical is not a coincidence. It's the whole design intent of
the lbm/lbf system, and it's exactly what makes the system seductive and
dangerous.

We'll get there.

---

## 2.4 Dimensional Homogeneity

Now the elegant part.

> **Every term in a physically valid equation must have the same dimensions.**

This is called **dimensional homogeneity**, and it is not a convention. It's a
requirement. You cannot add a length to a time any more than you can add three
apples to four Tuesdays. The statement would be meaningless.

Two consequences follow, and both are immediately useful.

**Consequence 1: You can check any equation without knowing the answer.**

Reduce every term to base dimensions. If they don't match, the equation is
wrong. Full stop. You don't need to know what the correct equation is — you
only need to know that this one isn't it.

**Consequence 2: Dimensional homogeneity is necessary but not sufficient.**

A dimensionally correct equation *can* still be wrong. A missing factor of 2
or a wrong sign passes the dimensional test cleanly. So homogeneity catches a
whole category of errors and is silent about another. Use it for what it
catches and don't over-trust it.

### Worked Example 1 — Catching a Wrong Equation

**Given.** A candidate writes the period of a simple pendulum as

$$T_p = 2\pi \sqrt{L g}$$

where $L$ is length and $g$ is gravitational acceleration.

**Find.** Whether the equation can be correct.

**Approach.** Reduce both sides to base dimensions and compare.

**Solution.**

Step 1 — Left side. A period is a time.

$$[T_p] = T$$

Step 2 — Right side. The $2\pi$ is dimensionless and can be ignored. Inside
the radical:

$$[L g] = L \cdot \frac{L}{T^2} = \frac{L^2}{T^2}$$

Step 3 — Take the square root.

$$\sqrt{\frac{L^2}{T^2}} = \frac{L}{T}$$

Step 4 — Compare.

$$T \;\ne\; \frac{L}{T}$$

**The equation is wrong.** The right side has the dimensions of a velocity,
not a time.

**Check.** What would work? Try dividing instead of multiplying:

$$\left[\frac{L}{g}\right] = \frac{L}{L/T^2} = T^2 \quad \Rightarrow \quad \sqrt{T^2} = T \;\checkmark$$

So the correct form must be

$$T_p = 2\pi\sqrt{\frac{L}{g}}$$

**What this teaches.** I recovered the correct structure of the equation from
dimensions alone, without remembering it. That won't always work — dimensional
analysis can't produce the $2\pi$ — but it will always tell you which of two
candidate forms is even possible.

> **Mentor's Margin:** This is a genuinely useful exam skill and almost nobody
> trains it. When you're staring at a Handbook equation and can't remember
> whether a term goes in the numerator or the denominator, check the
> dimensions. Thirty seconds, and the answer is unambiguous. It has saved me
> more times than I can count.

### Worked Example 2 — Verifying a Valid Term

**Given.** In fluid mechanics you'll meet the term $\rho v^2$, called dynamic
pressure.

**Find.** Confirm it has the dimensions of pressure.

**Solution.**

Step 1 — Density and velocity in base dimensions.

$$[\rho] = \frac{M}{L^3} \qquad [v] = \frac{L}{T}$$

Step 2 — Form the product.

$$[\rho v^2] = \frac{M}{L^3} \cdot \frac{L^2}{T^2} = \frac{M}{L \, T^2} = M L^{-1} T^{-2}$$

Step 3 — Compare against pressure. Pressure is force per area:

$$[p] = \frac{[F]}{[A]} = \frac{M L T^{-2}}{L^2} = M L^{-1} T^{-2}$$

**They match.** ✓ The term $\rho v^2$ is dimensionally a pressure.

**Check in SI units directly:**

$$\frac{\text{kg}}{\text{m}^3} \cdot \frac{\text{m}^2}{\text{s}^2} = \frac{\text{kg}}{\text{m} \cdot \text{s}^2} = \text{Pa} \;\checkmark$$

**A warning about the USCS version.** Now try that same product in USCS with
density in lbm/ft³:

$$\frac{\text{lbm}}{\text{ft}^3} \cdot \frac{\text{ft}^2}{\text{s}^2} = \frac{\text{lbm}}{\text{ft} \cdot \text{s}^2}$$

That is **not** lbf/ft². To get a pressure in lbf/ft² you have to divide by
$g_c$. This is the first sighting of the animal we're hunting in §1.6, and it
is exactly why the Handbook lists fluid pressure as $p = \rho g h / g_c$ rather
than $p = \rho g h$.

---

## 2.5 Unit Conversion by Dimensional Analysis

The technique is called the **factor-label method**, and it is the only
conversion method you should ever use. Not because it's fast, but because it
cannot go wrong in the direction you're not watching.

### The method

**A conversion factor is a ratio equal to one.** Since $1 \text{ ft} = 12
\text{ in}$, both of these are equal to one:

$$\frac{12 \text{ in}}{1 \text{ ft}} = 1 \qquad \frac{1 \text{ ft}}{12 \text{ in}} = 1$$

Multiplying by one changes nothing about the quantity. So you multiply by
whichever orientation cancels the unit you're leaving and installs the unit
you want.

**Write the units. Cancel them explicitly. If the units don't cancel to what
you wanted, you used the factor upside down.**

That last sentence is the whole value of the method. It converts a
remembering problem into a seeing problem.

> **Mentor's Margin:** Never do a conversion by deciding whether to multiply
> or divide. You will be right most of the time and wrong occasionally, and
> the occasions will be under time pressure. Write the fraction, cancel the
> units, and let the algebra decide. It is not slower once it's a habit, and
> it never fails.

### Worked Example 3 — A Multi-Step SI Conversion

**Given.** A pump delivers $1{,}250 \text{ L/min}$.

**Find.** The flow rate in m³/s.

**Approach.** Two conversions: litres to cubic metres, minutes to seconds.
Chain them and cancel.

**Solution.**

$$1{,}250 \; \frac{\cancel{\text{L}}}{\cancel{\text{min}}} \times \frac{1 \text{ m}^3}{1{,}000 \; \cancel{\text{L}}} \times \frac{1 \; \cancel{\text{min}}}{60 \text{ s}}$$

$$= \frac{1{,}250}{(1{,}000)(60)} \; \frac{\text{m}^3}{\text{s}} = \frac{1{,}250}{60{,}000} = 2.083 \times 10^{-2} \; \frac{\text{m}^3}{\text{s}}$$

$$\boxed{Q_v = 2.08 \times 10^{-2} \text{ m}^3/\text{s}}$$

**Check.** Order of magnitude: 1,250 L is a bit over one cubic metre, delivered
over a minute, so roughly $1/60 \approx 0.017$ m³/s. We got 0.021. Same order.
✓

Note that both L and min cancelled, leaving exactly m³/s. If I'd inverted
either factor, I'd have ended up with something like L²·min/(m³·s), which is
visibly nonsense. **The cancellation is the check.**

### Worked Example 4 — USCS to SI, With a Squared Prefix

**Given.** A hydraulic system operates at $150 \text{ psi}$.

**Find.** The pressure in kPa, two ways: using a single tabulated factor, and
by building the conversion from base factors.

**Solution — Route A, tabulated factor.**

From the Handbook conversion table, $1 \text{ lbf/in}^2 = 6{,}895 \text{ Pa}$.

$$150 \; \cancel{\frac{\text{lbf}}{\text{in}^2}} \times \frac{6{,}895 \text{ Pa}}{1 \; \cancel{\text{lbf/in}^2}} = 1.034 \times 10^6 \text{ Pa}$$

$$\boxed{p = 1{,}034 \text{ kPa} = 1.03 \text{ MPa}}$$

**Solution — Route B, built from base factors.**

Use $1 \text{ lbf} = 4.448 \text{ N}$ and $1 \text{ in} = 0.0254 \text{ m}$.

$$150 \; \frac{\cancel{\text{lbf}}}{\cancel{\text{in}^2}} \times \frac{4.448 \text{ N}}{1 \; \cancel{\text{lbf}}} \times \frac{1 \; \cancel{\text{in}^2}}{(0.0254)^2 \text{ m}^2}$$

Compute the squared term first:

$$(0.0254)^2 = 6.4516 \times 10^{-4}$$

$$= \frac{(150)(4.448)}{6.4516 \times 10^{-4}} \; \frac{\text{N}}{\text{m}^2} = \frac{667.2}{6.4516 \times 10^{-4}} = 1.034 \times 10^6 \text{ Pa}$$

$$\boxed{p = 1{,}034 \text{ kPa}}$$

**Check.** Both routes give 1,034 kPa. ✓

Second check, against a known landmark: atmospheric pressure is about 14.7 psi
and about 101 kPa. So 150 psi is roughly ten atmospheres, which should be
roughly 1,010 kPa. We got 1,034. ✓

**What this teaches.** Two things. First, the squared unit gets the exponent
applied to the conversion factor — $(0.0254)^2$, not $0.0254$ — which is the
same trap as $\text{mm}^2$ from Chapter 01-01. Second, when you have a
tabulated factor, use it; Route B is here to show you the factor isn't magic,
not because you should rebuild it every time.

### Landmark conversions worth knowing cold

The Handbook has a full table on page 3. These particular ones come up often
enough that a lookup is a waste of your seconds.

| From | To | Multiply by |
|---|---|---|
| in | mm | 25.4 (exact) |
| ft | m | 0.3048 (exact) |
| mile | ft | 5,280 (exact) |
| lbf | N | 4.448 |
| lbm | kg | 0.4536 |
| slug | kg | 14.59 |
| psi | kPa | 6.895 |
| atm | kPa | 101.3 |
| atm | psi | 14.70 |
| ft·lbf | J | 1.356 |
| Btu | J | 1,055 |
| hp | W | 745.7 |
| kW | hp | 1.341 |

---

## 2.6 The Pound Problem

Here we are. Read this section twice.

### 2.6.1 Why the problem exists

I want you to understand the *structure* of this, not memorize a rule. Rules
you memorize decay. Structure you understand does not.

Start with a fact about unit systems. To describe mechanics you need three
independent base units — one each for the dimensions of mass, length, and
time. Three. Force is then *derived* from those three, through $F = ma$.

Or you can pick force, length, and time as your three base units, and derive
mass. Either choice works. Both give you a **coherent** system, meaning $F =
ma$ holds with no extra constant.

Now look at the three real systems.

**System 1: SI.** Base units are kilogram (mass), metre, second. Force is
derived: the newton is *defined* as kg·m/s². Three base units, coherent.

$$F = ma \qquad \text{(N, kg, m/s²)}$$

**System 2: USCS with the slug.** Base units are pound-force, foot, second.
Mass is derived: the slug is *defined* as the mass that one pound-force
accelerates at one foot per second squared, so $1 \text{ slug} = 1 \text{
lbf} \cdot \text{s}^2/\text{ft}$. Three base units, coherent.

$$F = ma \qquad \text{(lbf, slug, ft/s²)}$$

**System 3: USCS with both pounds.** Base units are pound-force, pound-mass,
foot, second.

Count them. **Four.**

That's the problem. Four base units for a system that needs three. The pound-
mass and the pound-force were each defined independently, by different
communities, for different reasons, and neither was derived from the other. The
system is **over-determined**.

And when a system is over-determined, $F = ma$ does not hold. You need a
conversion constant to reconcile the redundant definitions.

That constant is $g_c$.

> **Mentor's Margin:** So $g_c$ is not a law of physics. It is not a property
> of gravity. It is scar tissue — the numerical price of a system that kept
> two units where one would do, because engineers in one country liked saying
> "pounds" for both weight and mass and nobody wanted to be the one to give it
> up. Once you see it that way, it stops being mysterious and becomes what it
> actually is: bookkeeping.

### 2.6.2 The definition

The pound-force is defined as the force that accelerates one pound-mass at
$32.174 \text{ ft/s}^2$ — which is standard gravitational acceleration.

$$1 \text{ lbf} = 32.174 \; \frac{\text{lbm} \cdot \text{ft}}{\text{s}^2}$$

Rearranged, that gives the constant:

$$\boxed{g_c = 32.174 \; \frac{\text{lbm} \cdot \text{ft}}{\text{lbf} \cdot \text{s}^2}}$$

The design intent is now visible. **They chose the number so that one
pound-mass weighs one pound-force at standard gravity.** That's convenient at
the grocery store and it's the reason the system survived.

It is also the reason it's dangerous, because it means the two numbers agree
in the most common case and disagree in every other one. A trap that's
invisible until it isn't.

### 2.6.3 $g_c$ is not $g$

The Handbook warns about this explicitly. Take the warning.

| | $g$ | $g_c$ |
|---|---|---|
| **Name** | local gravitational acceleration | force unit conversion constant |
| **Is it a physical quantity?** | Yes | No — it's a bookkeeping factor |
| **Dimensions** | $LT^{-2}$ | $ML \cdot F^{-1} T^{-2}$ |
| **Units** | m/s² or ft/s² | lbm·ft/(lbf·s²) |
| **Does it vary?** | **Yes** — with location | **No** — fixed by definition |
| **Standard value** | 9.807 m/s² or 32.174 ft/s² | 32.174 lbm·ft/(lbf·s²) |
| **Appears in SI?** | Yes | **No** — SI doesn't need it |

Read the "does it vary" row again. That's the operational difference.

$g$ is a measurement. It's about 32.174 ft/s² at sea level on Earth, less at
altitude, about 5.32 ft/s² on the Moon, and 0 in free fall.

$g_c$ is a definition. It is 32.174 lbm·ft/(lbf·s²) everywhere in the
universe, forever, because it's a statement about how two units relate to each
other, not about gravity.

> **Mentor's Margin:** They share the number 32.174 and that is the single
> most confusing coincidence in engineering education. It is not a
> coincidence — the pound-force was *defined* using standard gravity, which is
> why the numbers match. But sharing a number does not make them the same
> thing, any more than 12 inches per foot makes a ruler into a clock. Watch
> the units. The units never lie.

### 2.6.4 Newton's second law in USCS

With $g_c$ in hand, the law becomes:

$$\boxed{F = \frac{ma}{g_c}}$$

with $F$ in lbf, $m$ in lbm, $a$ in ft/s².

Verify the units:

$$\frac{[\text{lbm}] \left[\dfrac{\text{ft}}{\text{s}^2}\right]}{\left[\dfrac{\text{lbm} \cdot \text{ft}}{\text{lbf} \cdot \text{s}^2}\right]} = \cancel{\text{lbm}} \cdot \cancel{\frac{\text{ft}}{\text{s}^2}} \cdot \frac{\text{lbf} \cdot \cancel{\text{s}^2}}{\cancel{\text{lbm}} \cdot \cancel{\text{ft}}} = \text{lbf} \;\checkmark$$

Everything cancels except lbf. That's what dimensional bookkeeping is for.

### Worked Example 5 — Force on an Accelerating Mass

**Given.** A crate of mass $50 \text{ lbm}$ slides on a frictionless
horizontal surface under a horizontal push of $20 \text{ lbf}$.

**Find.** The acceleration, in ft/s².

**Approach.** Solve $F = ma/g_c$ for $a$. Carry every unit.

**Solution.**

Step 1 — Rearrange.

$$a = \frac{F g_c}{m}$$

Step 2 — Substitute with units.

$$a = \frac{(20 \; \cancel{\text{lbf}}) \left(32.174 \; \dfrac{\text{lbm} \cdot \text{ft}}{\cancel{\text{lbf}} \cdot \text{s}^2}\right)}{50 \; \cancel{\text{lbm}}}$$

Step 3 — Compute.

$$a = \frac{(20)(32.174)}{50} = \frac{643.5}{50} = 12.87 \; \frac{\text{ft}}{\text{s}^2}$$

$$\boxed{a = 12.9 \text{ ft/s}^2}$$

**Check — the ratio shortcut.** At standard gravity, 50 lbm weighs 50 lbf. So a
50 lbf push would produce exactly $g = 32.174$ ft/s². We pushed with 20 lbf,
which is $20/50 = 0.400$ of that:

$$a = (0.400)(32.174) = 12.87 \; \text{ft/s}^2 \;\checkmark$$

**Second check — SI.** Convert and redo.

$$m = 50 \text{ lbm} \times 0.4536 \; \frac{\text{kg}}{\text{lbm}} = 22.68 \text{ kg}$$
$$F = 20 \text{ lbf} \times 4.448 \; \frac{\text{N}}{\text{lbf}} = 88.96 \text{ N}$$
$$a = \frac{F}{m} = \frac{88.96}{22.68} = 3.922 \; \frac{\text{m}}{\text{s}^2}$$
$$3.922 \; \frac{\text{m}}{\text{s}^2} \times \frac{1 \text{ ft}}{0.3048 \text{ m}} = 12.87 \; \frac{\text{ft}}{\text{s}^2} \;\checkmark$$

Three independent routes, one answer.

> **Mentor's Margin:** That ratio shortcut is worth committing to memory. In
> the lbm/lbf system, **the ratio of applied force to weight equals the ratio
> of acceleration to $g$.** It's a five-second sanity check on any USCS
> dynamics answer, and it works because the numbers were rigged to make it
> work.

### 2.6.5 The slug alternative

You can dodge $g_c$ entirely by converting mass to slugs first.

$$1 \text{ slug} = 32.174 \text{ lbm}$$

Once mass is in slugs, $F = ma$ holds directly:

$$F = ma \qquad \text{(lbf, slug, ft/s²)}$$

Redo Worked Example 5 this way:

$$m = \frac{50 \; \cancel{\text{lbm}}}{32.174 \; \cancel{\text{lbm}}/\text{slug}} = 1.554 \text{ slug}$$

$$a = \frac{F}{m} = \frac{20 \text{ lbf}}{1.554 \text{ slug}} = 12.87 \; \frac{\text{ft}}{\text{s}^2} \;\checkmark$$

Same answer, and no $g_c$ appeared.

**So which should you use?**

| Method | Use when |
|---|---|
| $g_c$ | The problem gives mass in lbm — which is most of the time |
| slug | The problem gives mass in slugs, or you prefer coherent algebra |

You must be fluent in both, because **the Handbook uses the $g_c$
formulation** and various textbooks use the slug. On exam day you're reading
the Handbook's equations, so $g_c$ is the one to have automatic.

> **Mentor's Margin:** Pick one as your default and *always* start there. I'd
> suggest $g_c$, precisely because the Handbook writes its equations that way
> and matching the reference removes a translation step. Then be able to check
> yourself with the other. What you must never do is switch mid-problem —
> that's how a factor of 32.174 goes missing.

### 2.6.6 Mass versus weight

**Mass** is a property of an object: how much matter it contains, or
equivalently how much it resists acceleration. It does not change with
location.

**Weight** is a force: the gravitational force acting on that mass. It changes
with location because $g$ changes with location.

$$\boxed{F_W = \frac{mg}{g_c}} \qquad \text{(USCS)} \qquad\qquad \boxed{F_W = mg} \qquad \text{(SI)}$$

At standard gravity in USCS, $g = 32.174$ ft/s² and $g_c = 32.174$
lbm·ft/(lbf·s²), so the two numbers cancel:

$$F_W = \frac{m(32.174)}{32.174} = m \quad \text{numerically}$$

**A 50 lbm object weighs 50 lbf at standard gravity.** That is the entire
design goal of the system, achieved.

But move off the Earth's surface and the cancellation stops.

### Worked Example 6 — Weight at Non-Standard Gravity

**Given.** The crate from Worked Example 5, $m = 50 \text{ lbm}$, is taken to
the Moon, where $g = 5.32 \text{ ft/s}^2$.

**Find.** (a) Its mass on the Moon. (b) Its weight on the Moon, in lbf.
(c) The force needed to accelerate it at 12.87 ft/s² on the Moon.

**Solution.**

(a) **Mass does not change with location.**

$$\boxed{m = 50 \text{ lbm}}$$

(b) Weight:

$$F_W = \frac{mg}{g_c} = \frac{(50 \; \cancel{\text{lbm}})\left(5.32 \; \dfrac{\cancel{\text{ft}}}{\cancel{\text{s}^2}}\right)}{32.174 \; \dfrac{\cancel{\text{lbm}} \cdot \cancel{\text{ft}}}{\text{lbf} \cdot \cancel{\text{s}^2}}}$$

$$F_W = \frac{(50)(5.32)}{32.174} = \frac{266}{32.174} = 8.267 \text{ lbf}$$

$$\boxed{F_W = 8.27 \text{ lbf}}$$

(c) The force required to produce a given acceleration:

$$F = \frac{ma}{g_c} = \frac{(50)(12.87)}{32.174} = 20.0 \text{ lbf}$$

$$\boxed{F = 20.0 \text{ lbf}}$$

**Exactly the same as on Earth.**

**Check.** (b) Lunar gravity is about one-sixth Earth's, so the weight should
be about $50/6 = 8.3$ lbf. ✓

**The lesson in part (c).** Notice what did and didn't change. The weight
dropped by a factor of six. The force needed to accelerate the crate
horizontally did not change at all — because $F = ma/g_c$ contains no $g$.

$g_c$ stayed at 32.174 because $g_c$ is a definition. $g$ changed because $g$
is a measurement.

If you had used 5.32 in place of $g_c$, you'd have gotten 121 lbf, wrong by a
factor of six. **That substitution — using local $g$ where $g_c$ belongs — is
the single most common form of this error.**

### 2.6.7 Where else $g_c$ shows up

$g_c$ appears anywhere a mass in lbm meets an acceleration or a force. The
Handbook lists these on page 1, and you should recognize all of them on sight.

| Quantity | USCS form with $g_c$ | Result in |
|---|---|---|
| Newton's second law | $F = \dfrac{ma}{g_c}$ | lbf |
| Weight | $F_W = \dfrac{mg}{g_c}$ | lbf |
| Kinetic energy | $KE = \dfrac{mv^2}{2 g_c}$ | ft·lbf |
| Potential energy | $PE = \dfrac{mgh}{g_c}$ | ft·lbf |
| Fluid pressure | $p = \dfrac{\rho g h}{g_c}$ | lbf/ft² |
| Specific weight | $SW = \dfrac{\rho g}{g_c}$ | lbf/ft³ |
| Shear stress | $\tau = \dfrac{\mu}{g_c}\dfrac{dv}{dy}$ | lbf/ft² |

The Handbook makes a remark about this table that I want you to internalize:

> $g_c$ is frequently **not written explicitly** in engineering equations. Its
> use is nonetheless required to produce a consistent set of units.

That is a warning. You will open textbooks, datasheets, and reference works
that print $KE = \frac{1}{2}mv^2$ with no $g_c$ anywhere — because the author
assumed mass in slugs, or assumed SI, or simply assumed you'd know. **Whether
$g_c$ belongs is determined by what units your numbers are actually in, not by
how the equation was printed.**

The defense is the same as always: carry your units through the arithmetic. If
lbm survives into an answer that should be in lbf, you dropped a $g_c$.

### Worked Example 7 — Kinetic Energy in USCS

**Given.** A car of mass $3{,}000 \text{ lbm}$ travels at $60 \text{ mph}$.

**Find.** Its kinetic energy in ft·lbf.

**Approach.** Convert speed to ft/s, then apply the $g_c$ form.

**Solution.**

Step 1 — Convert the speed.

$$60 \; \frac{\cancel{\text{mi}}}{\cancel{\text{h}}} \times \frac{5{,}280 \text{ ft}}{1 \; \cancel{\text{mi}}} \times \frac{1 \; \cancel{\text{h}}}{3{,}600 \text{ s}} = \frac{(60)(5{,}280)}{3{,}600} = 88.0 \; \frac{\text{ft}}{\text{s}}$$

Step 2 — Apply the equation.

$$KE = \frac{mv^2}{2 g_c} = \frac{(3{,}000 \; \cancel{\text{lbm}})\left(88.0 \; \dfrac{\text{ft}}{\cancel{\text{s}}}\right)^2}{2\left(32.174 \; \dfrac{\cancel{\text{lbm}} \cdot \cancel{\text{ft}}}{\text{lbf} \cdot \cancel{\text{s}^2}}\right)}$$

Step 3 — Compute.

$$KE = \frac{(3{,}000)(7{,}744)}{(2)(32.174)} = \frac{23{,}232{,}000}{64.348} = 3.610 \times 10^5 \text{ ft} \cdot \text{lbf}$$

$$\boxed{KE = 3.61 \times 10^5 \text{ ft} \cdot \text{lbf}}$$

**Check — convert to SI and redo from scratch.**

$$3.610 \times 10^5 \; \cancel{\text{ft} \cdot \text{lbf}} \times \frac{1.356 \text{ J}}{1 \; \cancel{\text{ft} \cdot \text{lbf}}} = 4.90 \times 10^5 \text{ J} = 490 \text{ kJ}$$

Independently in SI:

$$m = 3{,}000 \times 0.4536 = 1{,}361 \text{ kg} \qquad v = 88.0 \times 0.3048 = 26.82 \; \text{m/s}$$

$$KE = \tfrac{1}{2}mv^2 = (0.5)(1{,}361)(26.82)^2 = (0.5)(1{,}361)(719.3) = 4.89 \times 10^5 \text{ J} \;\checkmark$$

Agreement to three figures. ✓

**Note the SI equation had no $g_c$.** SI never needs it. That asymmetry —
$g_c$ in USCS, absent in SI — is worth noticing every single time, because it
reinforces that $g_c$ is an artifact of the unit system rather than of the
physics.

**60 mph = 88 ft/s** is worth memorizing outright. It comes up constantly in
transportation and dynamics problems.

### Worked Example 8 — Fluid Pressure and Specific Weight

**Given.** An open tank holds water to a depth of $30 \text{ ft}$. Take the
density of water as $\rho = 62.4 \text{ lbm/ft}^3$ and standard gravity.

**Find.** (a) The specific weight of water in lbf/ft³. (b) The gage pressure
at the bottom, in lbf/ft². (c) The same pressure in psi.

**Solution.**

(a) Specific weight:

$$SW = \frac{\rho g}{g_c} = \frac{\left(62.4 \; \dfrac{\text{lbm}}{\text{ft}^3}\right)\left(32.174 \; \dfrac{\text{ft}}{\text{s}^2}\right)}{32.174 \; \dfrac{\text{lbm} \cdot \text{ft}}{\text{lbf} \cdot \text{s}^2}}$$

The 32.174s cancel numerically, and the units reduce:

$$SW = 62.4 \; \frac{\text{lbf}}{\text{ft}^3}$$

$$\boxed{SW = 62.4 \text{ lbf/ft}^3}$$

(b) Pressure at depth:

$$p = \frac{\rho g h}{g_c} = SW \cdot h = \left(62.4 \; \frac{\text{lbf}}{\cancel{\text{ft}^3}}\right)(30 \; \cancel{\text{ft}}) = 1{,}872 \; \frac{\text{lbf}}{\text{ft}^2}$$

$$\boxed{p = 1{,}872 \text{ lbf/ft}^2}$$

(c) Convert to psi. There are 144 in² per ft²:

$$1{,}872 \; \frac{\text{lbf}}{\cancel{\text{ft}^2}} \times \frac{1 \; \cancel{\text{ft}^2}}{144 \text{ in}^2} = 13.0 \; \frac{\text{lbf}}{\text{in}^2}$$

$$\boxed{p = 13.0 \text{ psi}}$$

**Check.** Water produces about 0.433 psi per foot of depth — a number worth
knowing.

$$(30 \text{ ft})\left(0.433 \; \frac{\text{psi}}{\text{ft}}\right) = 13.0 \text{ psi} \;\checkmark$$

**Second check.** Convert to SI and verify with $p = \rho g h$:

$$\rho = 1{,}000 \; \text{kg/m}^3 \qquad h = 30 \times 0.3048 = 9.144 \text{ m}$$
$$p = (1{,}000)(9.807)(9.144) = 89{,}680 \text{ Pa} = 89.7 \text{ kPa}$$
$$13.0 \text{ psi} \times 6.895 \; \frac{\text{kPa}}{\text{psi}} = 89.6 \text{ kPa} \;\checkmark$$

**Why part (a) matters more than it looks.** The numerical equality between
density in lbm/ft³ and specific weight in lbf/ft³ *at standard gravity* is the
reason the Handbook can state "one cubic foot of water weighs 62.4 lbf" and
also have you use 62.4 lbm/ft³ as a density. Same number, different quantity,
and the coincidence holds only at standard gravity.

At any other $g$, they part company — and if you've been treating them as
interchangeable rather than understanding why they happened to agree, you'll
be wrong and won't know it.

---

## 2.7 Temperature Scales

Four scales. Two absolute, two relative.

| Scale | Symbol | Type | Zero point |
|---|---|---|---|
| Kelvin | K | Absolute | absolute zero |
| Rankine | °R | Absolute | absolute zero |
| Celsius | °C | Relative | ~water freezing point |
| Fahrenheit | °F | Relative | historical |

**Absolute scales** have their zero at absolute zero, so a temperature on an
absolute scale is a genuine magnitude. Ratios mean something: 400 K really is
twice as hot as 200 K in a thermodynamically meaningful sense.

**Relative scales** put zero somewhere arbitrary and convenient. Ratios on a
relative scale are meaningless: 40 °C is not "twice as hot" as 20 °C in any
physical sense, because the zero point isn't a real zero.

That distinction has a hard practical consequence, and it's the thing this
section exists to teach.

### The four conversions

The Handbook prints these on page 1.

$$^\circ\text{F} = 1.8\,(^\circ\text{C}) + 32$$

$$^\circ\text{C} = \frac{^\circ\text{F} - 32}{1.8}$$

$$^\circ\text{R} = \;^\circ\text{F} + 459.69$$

$$\text{K} = \;^\circ\text{C} + 273.15$$

Two more that follow from those and are worth having:

$$\text{K} = \frac{^\circ\text{R}}{1.8} \qquad\qquad ^\circ\text{R} = 1.8\,(\text{K})$$

### The pairing that matters

Look at how the scales pair up:

| | Absolute | Relative | Offset |
|---|---|---|---|
| **SI-sized degree** | K | °C | 273.15 |
| **USCS-sized degree** | °R | °F | 459.69 |

**Kelvin pairs with Celsius. Rankine pairs with Fahrenheit.** Same degree size
within each pair, different zero point.

That's why the offset conversions are pure addition — no multiplication — while
crossing between the pairs requires the factor of 1.8.

> **Mentor's Margin:** The mistake I see is students memorizing four
> unconnected formulas. Don't. Learn the structure instead: two degree sizes,
> two zero points. Within a degree size you add or subtract an offset. Across
> degree sizes you multiply by 1.8. Four formulas collapse into two ideas, and
> ideas survive exam pressure better than formulas do.

### Temperature value versus temperature difference

**This is the part that costs points.**

A temperature *value* and a temperature *difference* convert differently.

**For a value**, the offset matters:

$$100 \; ^\circ\text{C} = 100 + 273.15 = 373.15 \text{ K}$$

**For a difference**, the offset cancels:

$$\Delta T = 100 \; ^\circ\text{C} - 20 \; ^\circ\text{C} = 80 \; ^\circ\text{C}$$
$$\Delta T = 373.15 \text{ K} - 293.15 \text{ K} = 80 \text{ K}$$

Same number. Because both endpoints shifted by 273.15, the difference didn't
move.

So:

$$\boxed{\Delta T \text{ of } 1 \; ^\circ\text{C} = \Delta T \text{ of } 1 \text{ K}}$$
$$\boxed{\Delta T \text{ of } 1 \; ^\circ\text{F} = \Delta T \text{ of } 1 \; ^\circ\text{R}}$$
$$\boxed{\Delta T \text{ of } 1 \; ^\circ\text{C} = \Delta T \text{ of } 1.8 \; ^\circ\text{F}}$$

Crossing degree sizes still needs the 1.8, because that's about degree size,
not zero point.

### Which does an equation want?

| Equation type | Wants | Why |
|---|---|---|
| Ideal gas law, $pV = mRT$ | **Absolute** | $T$ appears as a magnitude; a relative-scale value would be physically meaningless |
| Radiation, $q = \sigma_{SB} A T^4$ | **Absolute** | Same reason, and the fourth power makes the error catastrophic |
| Conduction, $q = kA \, \Delta T / L$ | **Difference** | Only the difference drives heat flow |
| Thermal expansion, $\delta = \alpha_T L \, \Delta T$ | **Difference** | Same |
| Thermal efficiency, $\eta = 1 - T_L/T_H$ | **Absolute** | It's a ratio, so both must be on an absolute scale |

**The test: does the equation use $T$ or $\Delta T$?** If a bare $T$ appears —
especially raised to a power or inside a ratio — you need an absolute scale.
If only differences appear, either scale in the correct pair works.

> **Mentor's Margin:** The efficiency formula is the classic trap. Someone
> plugs in 500 °C and 30 °C, gets $1 - 30/500 = 0.94$, and reports 94%
> efficiency for a heat engine. The correct calculation with 773 K and 303 K
> gives $1 - 303/773 = 0.61$, or 61%. Wildly different, and the wrong answer
> looks perfectly reasonable on the page. Any time temperature appears in a
> ratio or an exponent, convert to absolute first. No exceptions.

### Worked Example 9 — Value, Difference, and Ratio

**Given.** A heat engine operates between a hot reservoir at $450 \; ^\circ
\text{F}$ and a cold reservoir at $85 \; ^\circ\text{F}$.

**Find.** (a) Both temperatures in °R. (b) Both in K. (c) The temperature
difference in °F, °R, °C, and K. (d) The maximum possible thermal efficiency,
$\eta = 1 - T_L/T_H$. (e) What you'd get by incorrectly using °F in part (d).

**Solution.**

(a) Rankine, by adding the offset:

$$T_H = 450 + 459.69 = 909.7 \; ^\circ\text{R}$$
$$T_L = 85 + 459.69 = 544.7 \; ^\circ\text{R}$$

(b) Kelvin, by dividing Rankine by 1.8:

$$T_H = \frac{909.7}{1.8} = 505.4 \text{ K}$$
$$T_L = \frac{544.7}{1.8} = 302.6 \text{ K}$$

*Cross-check via Celsius:*

$$T_H = \frac{450 - 32}{1.8} = \frac{418}{1.8} = 232.2 \; ^\circ\text{C} \quad \Rightarrow \quad 232.2 + 273.15 = 505.4 \text{ K} \;\checkmark$$

(c) The difference:

$$\Delta T = 450 - 85 = 365 \; ^\circ\text{F}$$

In Rankine, the offsets cancel:

$$\Delta T = 909.7 - 544.7 = 365 \; ^\circ\text{R}$$

Crossing to the SI degree size requires the 1.8:

$$\Delta T = \frac{365}{1.8} = 202.8 \; ^\circ\text{C} = 202.8 \text{ K}$$

$$\boxed{\Delta T = 365 \; ^\circ\text{F} = 365 \; ^\circ\text{R} = 202.8 \; ^\circ\text{C} = 202.8 \text{ K}}$$

(d) Efficiency, using absolute temperatures. Rankine works, since it's a ratio
of absolutes:

$$\eta = 1 - \frac{T_L}{T_H} = 1 - \frac{544.7}{909.7} = 1 - 0.5988 = 0.4012$$

$$\boxed{\eta = 40.1\%}$$

*Check with Kelvin:*

$$\eta = 1 - \frac{302.6}{505.4} = 1 - 0.5988 = 0.4012 \;\checkmark$$

Both absolute scales give the same answer, as they must.

(e) The wrong way:

$$\eta_{\text{wrong}} = 1 - \frac{85}{450} = 1 - 0.1889 = 0.8111 = 81.1\%$$

**Off by a factor of two.** And 81% looks like a plausible efficiency to
anyone not thinking hard, which is precisely why this error survives to the
answer sheet.

**Check.** Part (c) demonstrates the principle cleanly: the °F and °R
differences are *identical* because both scales share a degree size, while
converting to the SI degree required division by 1.8. Values need offsets;
differences don't. ✓

---

## 2.8 Fundamental Constants

The Handbook prints a table of physical constants on page 2. You should know
where it is and, for a handful of entries, know the values cold.

### Values worth memorizing

| Constant | Symbol | Value |
|---|---|---|
| Standard gravity | $g$ | 9.807 m/s² · 32.174 ft/s² |
| Force conversion constant | $g_c$ | 32.174 lbm·ft/(lbf·s²) |
| Speed of light (exact) | $c$ | 299,792,458 m/s |
| Electron charge | $e$ | $1.6022 \times 10^{-19}$ C |
| Stefan-Boltzmann | $\sigma_{SB}$ | $5.67 \times 10^{-8}$ W/(m²·K⁴) |
| Molar volume, ideal gas at 273.15 K and 101.3 kPa | $V_m$ | 22,414 L/kmol |

### The universal gas constant — four printed forms

Here's a trap worth its own subsection. The Handbook prints the universal gas
constant **four times, in four different unit systems.**

| Form | Value | Units |
|---|---|---|
| SI, molar energy | 8,314 | J/(kmol·K) |
| SI, $pV$ form | 8,314 | kPa·m³/(kmol·K) |
| USCS | 1,545 | ft·lbf/(lb mole·°R) |
| Chemistry | 0.08206 | L·atm/(mol·K) |

They are all the same physical constant. They differ only in what units you're
feeding the equation.

**Selecting the right one is entirely a units question.** Look at what units
your pressure, volume, mass, and temperature are in, and pick the form that
makes the equation come out dimensionally clean.

> **Mentor's Margin:** This is where the factor-label method earns its keep
> again. Don't try to remember which form goes with which problem. Write out
> the equation with units attached, try a form, and see whether the units
> cancel. If they don't, you picked the wrong row. Ten seconds to check, and
> you're certain instead of hopeful.

### The bar notation

The Handbook designates the **universal** gas constant $\bar{R}$, and notes
that dividing by molecular weight gives the **specific** gas constant $R$ for a
particular gas:

$$R = \frac{\bar{R}}{MW}$$

It further notes that some disciplines — chemical engineering especially —
write plain $R$ for the universal constant. So the same symbol means different
things depending on which section of the Handbook you're reading.

**This guide uses $\bar{R}$ for universal and $R$ for specific, always.** When
you're reading the Handbook, check the section.

---

## As the Handbook States It

Almost everything in this chapter lives on Handbook pages 1 through 3, which
makes those three pages the densest and most reusable real estate in the entire
document.

> **Handbook 10.6, pp. 1–3** — *Units and Conversion Factors*

**Page 1 — the critical half-page.**

The section opens with "Distinguishing Pound-Force from Pound-Mass" before
anything else. It states:

- The FE and the Handbook both use SI and USCS
- Both force and mass are called *pounds* in USCS, hence lbf and lbm
- The pound-force is defined by $g_c = 32.174$ lbm·ft/(lbf·s²)
- With $g_c$, Newton's second law is written $F = ma/g_c$

It then gives the family of $g_c$ equations — kinetic energy, potential energy,
fluid pressure, specific weight, shear stress — with this remark:

> *"In all these examples, $g_c$ should be regarded as a force unit conversion
> factor. It is frequently not written explicitly in engineering equations.
> However, it is required to produce a consistent set of units."*

And the explicit warning:

> *"Note that the force unit conversion factor $g_c$ should not be confused
> with the local acceleration of gravity $g$, which has different units."*

Also on page 1: the metric prefix table, temperature conversions, and a short
"Commonly Used Equivalents" list — including that one gallon of water weighs
8.34 lbf, one cubic foot of water weighs 62.4 lbf, and one cubic metre of water
has a mass of 1,000 kg.

**Page 2 — significant figures and constants.**

Six numbered rules for significant figures, with the engineering convention of
3 to 4 significant digits in a final answer. Ideal gas constants in all four
forms. The fundamental constants table.

**Page 3 — the conversion table.**

A large two-column table of multiply-by factors. Alphabetical by source unit.
Learn how it's organized so you can scan it fast.

### Notation differences

| Handbook | This guide | Why |
|---|---|---|
| $g_c$ | $g_c$ | Same |
| $g$ | $g$ | Same |
| $\bar{R}$ universal, $R$ specific | Same | Explicit, since some sections use $R$ for universal |
| Uses plain symbols for weight | $F_W$ | $W$ is reserved for work throughout this guide |
| $\rho$ density, $\gamma$ or $SW$ specific weight | $\rho$, $SW$ | Avoids $\gamma$, which is specific heat ratio in Tier 2D |

### The divide, for this chapter

**In the Handbook — find it:**
- Metric prefix table
- Temperature conversion formulas
- $g_c$ definition and its equation family
- Conversion factor table
- Fundamental constants including all four gas constant forms
- Significant figure rules

**In the Handbook but memorize anyway:**
- $g_c = 32.174$ lbm·ft/(lbf·s²)
- $g = 9.807$ m/s² and 32.174 ft/s²
- The four temperature conversions
- Landmark conversions: in→mm, ft→m, lbf→N, lbm→kg, psi→kPa

You will use these constantly. Fifteen seconds per lookup, forty times, is
ten minutes of your working time.

**Not in the Handbook — memorize:**
- The distinction between quantity, dimension, and unit
- Dimensional homogeneity as a principle and as an error check
- The factor-label method
- **Why** $g_c$ exists — the over-determined system argument
- Mass versus weight as concepts
- Temperature value versus temperature difference
- Which equations require absolute temperature

That "why $g_c$ exists" line is the one I care most about. The Handbook gives
you the constant. It does not explain the structure. Understanding the
structure is what makes the constant impossible to misplace.

---

## Where This Goes Wrong

The failure list for this chapter. Read it twice, and again the week before
your exam.

**Substituting $g$ where $g_c$ belongs.** The most expensive error in USCS
mechanics. In Worked Example 6 it produced an answer wrong by a factor of six.
$g$ is a local measurement; $g_c$ is a universal definition. They share the
number 32.174 at standard gravity and share nothing else.

**Treating lbm and lbf as interchangeable.** They agree numerically for weight
at standard gravity. That is the *only* case in which they agree. Anywhere
else — non-standard gravity, or any equation involving acceleration — treating
them as the same quantity introduces a factor of 32.174.

**Dropping $g_c$ because the printed equation didn't show it.** The Handbook
warns you directly that $g_c$ is frequently omitted in print. Whether it
belongs depends on your units, not on the typography. Carry your units; if lbm
survives into an answer that should be lbf, you dropped it.

**Mixing lbm and slug in the same problem.** Pick one method and stay in it.
Switching mid-solution is how a factor of 32.174 vanishes without a trace.

**Using a relative temperature scale where absolute is required.** Ideal gas
law, radiation, thermal efficiency, anything with $T$ raised to a power or
inside a ratio. Worked Example 9 (e) got 81% instead of 40% this way.

**Converting a temperature difference as though it were a value.** A $\Delta T$
of 80 °C is a $\Delta T$ of 80 K, not 353 K. The offsets cancel in a
difference.

**Forgetting the 1.8 when crossing degree sizes.** $\Delta T$ in °C and K are
identical. $\Delta T$ in °C and °F are not — that's a factor of 1.8.

**Not applying the exponent to a squared or cubed conversion factor.** In
Worked Example 4 the in²→m² conversion needed $(0.0254)^2$. Same trap as mm²
from Chapter 01-01, and it shows up in every area and volume conversion.

**Deciding whether to multiply or divide instead of cancelling units.** You
will be right most of the time. The exceptions will occur under time pressure.
Write the fraction and let the cancellation decide.

**Picking the wrong form of the gas constant.** Four printed forms, and only
one makes your particular equation dimensionally clean. Check by cancelling
units, not by memory.

**Confusing density with specific weight.** Water is 62.4 lbm/ft³ *and* 62.4
lbf/ft³, and understanding *why* those numbers agree is the difference between
using them correctly and getting lucky.

---

## Key Terms

| Term | Definition |
|---|---|
| Physical quantity | A measurable property of an object or system |
| Dimension | The fundamental character of a quantity, independent of the unit used |
| Unit | A specific agreed-upon amount of a dimension used as a measurement reference |
| Base unit | One of the seven SI units from which all others are derived |
| Derived unit | A unit formed from combinations of base units |
| SI | International System of Units; mass is a base unit and force is derived |
| USCS | U.S. Customary System of units |
| Coherent system | A unit system in which $F = ma$ holds with no conversion constant |
| Over-determined system | A system with more base units than its dimensions require, forcing a conversion constant |
| Dimensional homogeneity | The requirement that every term in a valid equation share the same dimensions |
| Factor-label method | Unit conversion by multiplying by ratios equal to one, cancelling units explicitly |
| Pound-mass (lbm) | The USCS unit of mass |
| Pound-force (lbf) | The USCS unit of force; defined as the force accelerating 1 lbm at 32.174 ft/s² |
| Slug | The coherent USCS mass unit; 1 slug = 32.174 lbm |
| $g_c$ | Force unit conversion constant, 32.174 lbm·ft/(lbf·s²); fixed by definition |
| $g$ | Local gravitational acceleration; varies with location |
| Standard gravity | 9.807 m/s² or 32.174 ft/s² |
| Mass | Amount of matter; independent of location |
| Weight | The gravitational force on a mass; varies with location |
| Density ($\rho$) | Mass per unit volume |
| Specific weight ($SW$) | Force per unit volume; equals $\rho g / g_c$ in USCS |
| Absolute temperature scale | A scale whose zero is absolute zero: kelvin or Rankine |
| Relative temperature scale | A scale with an arbitrary zero: Celsius or Fahrenheit |
| Temperature difference ($\Delta T$) | A change in temperature; offset-independent within a degree-size pair |
| Universal gas constant ($\bar{R}$) | Gas constant per mole; printed in four unit systems |
| Specific gas constant ($R$) | $\bar{R}$ divided by molecular weight, for a particular gas |

---

## Review Questions

### Conceptual

1. Distinguish a physical quantity, a dimension, and a unit. Give one example
   of a single quantity expressed in three different units.
2. Why is the kilogram, rather than the gram, the SI base unit of mass? What
   makes this slightly awkward?
3. Derive the pascal in terms of SI base units, showing your reasoning from
   the definition of pressure.
4. State the principle of dimensional homogeneity. Explain why it is necessary
   but not sufficient for an equation to be correct.
5. Explain why the factor-label method is more reliable than deciding whether
   to multiply or divide.
6. **Explain, in structural terms, why $g_c$ exists.** Your answer should
   mention how many base units a mechanical system needs and how many the
   lbm/lbf system has.
7. Give three differences between $g$ and $g_c$. Why do they share the number
   32.174?
8. An object is moved from Earth to the Moon. State what happens to its mass,
   its weight, and the force required to accelerate it horizontally at a given
   rate. Justify each.
9. The Handbook notes that $g_c$ is "frequently not written explicitly" in
   engineering equations. What does that mean for you, and what habit protects
   you?
10. Explain the difference between converting a temperature *value* and
    converting a temperature *difference*. Why do the offsets cancel in a
    difference?
11. Give the test for deciding whether an equation requires absolute
    temperature. Name two equations that do and two that don't.
12. Water has a density of 62.4 lbm/ft³ and a specific weight of 62.4 lbf/ft³.
    Explain why these numbers agree, and state the condition under which they
    stop agreeing.
13. The universal gas constant appears in the Handbook in four forms. How do
    you decide which to use?

### Calculation

14. Reduce each to SI base units:
    (a) the joule
    (b) the watt
    (c) the newton
    (d) the pascal

15. Test each equation for dimensional homogeneity and state whether it can be
    correct. If not, suggest a correction.
    (a) $v = at^2$, where $v$ is velocity, $a$ acceleration, $t$ time
    (b) $KE = \tfrac{1}{2}mv^2$
    (c) $p = \rho g h^2$
    (d) $F = \dfrac{mv^2}{r}$, where $r$ is a radius

16. Convert as directed, using the factor-label method:
    (a) $85 \text{ mph}$ to ft/s
    (b) $2{,}400 \text{ ft}^3$ to m³
    (c) $45 \text{ psi}$ to kPa
    (d) $18 \text{ in}^2$ to mm²
    (e) $750 \text{ ft} \cdot \text{lbf}$ to J
    (f) $250 \text{ hp}$ to kW

17. A mass of $180 \text{ lbm}$ rests on a frictionless horizontal surface.
    (a) What is its weight at standard gravity, in lbf?
    (b) A horizontal force of $45 \text{ lbf}$ is applied. Find the
    acceleration in ft/s² using the $g_c$ method.
    (c) Repeat using the slug method.
    (d) Verify using the force-to-weight ratio shortcut.

18. An object has a mass of $25 \text{ lbm}$.
    (a) Its weight at standard gravity, in lbf.
    (b) Its weight on Mars, where $g = 12.2 \text{ ft/s}^2$.
    (c) Its mass on Mars.
    (d) The force required to accelerate it at $8.0 \text{ ft/s}^2$ on Mars.
    (e) The same force requirement on Earth.

19. A truck of mass $12{,}000 \text{ lbm}$ travels at $45 \text{ mph}$.
    (a) Find its kinetic energy in ft·lbf.
    (b) Convert to Btu, given $1 \text{ Btu} = 778 \text{ ft} \cdot \text{lbf}$.
    (c) Verify by converting to SI and recomputing.

20. An open tank contains a fluid of density $55 \text{ lbm/ft}^3$ to a depth
    of $22 \text{ ft}$, at standard gravity.
    (a) Specific weight in lbf/ft³.
    (b) Gage pressure at the bottom in lbf/ft².
    (c) The same in psi.
    (d) Verify by converting to SI.

21. A vessel is heated from $70 \; ^\circ\text{F}$ to $520 \; ^\circ\text{F}$.
    (a) Both temperatures in °R.
    (b) Both in °C.
    (c) Both in K.
    (d) The temperature difference in °F, °R, °C, and K.

22. A heat engine operates between reservoirs at $340 \; ^\circ\text{C}$ and
    $45 \; ^\circ\text{C}$.
    (a) The maximum thermal efficiency, using $\eta = 1 - T_L/T_H$.
    (b) The incorrect result from using Celsius values directly.
    (c) The percentage-point error introduced.

23. A steel rod $4.0 \text{ m}$ long is heated by $\Delta T = 75 \; ^\circ
    \text{C}$. Take $\alpha_T = 1.2 \times 10^{-5} \; ^\circ\text{C}^{-1}$ and
    use $\delta = \alpha_T L \, \Delta T$.
    (a) The elongation in mm.
    (b) Rework in USCS: length $13.12 \text{ ft}$, $\Delta T = 135 \; ^\circ
    \text{F}$, $\alpha_T = 6.67 \times 10^{-6} \; ^\circ\text{F}^{-1}$. Give
    the answer in inches and confirm it agrees.

### Multiple Choice

24. The dimensions of pressure are:
    A) $MLT^{-2}$
    B) $ML^{-1}T^{-2}$
    C) $ML^2T^{-2}$
    D) $ML^{-3}$

25. The value of $g_c$ is:
    A) $9.807 \text{ m/s}^2$
    B) $32.174 \text{ ft/s}^2$
    C) $32.174 \text{ lbm} \cdot \text{ft}/(\text{lbf} \cdot \text{s}^2)$
    D) $32.174 \text{ lbf} \cdot \text{s}^2/(\text{lbm} \cdot \text{ft})$

26. Which statement about $g_c$ is correct?
    A) It varies with altitude
    B) It is fixed by definition and does not vary with location
    C) It equals local gravitational acceleration
    D) It appears in SI equations as well as USCS

27. One slug equals:
    A) $1 \text{ lbm}$
    B) $32.174 \text{ lbm}$
    C) $0.4536 \text{ lbm}$
    D) $32.174 \text{ lbf}$

28. A $60 \text{ lbm}$ object is taken to a location where $g = 16.1 \text{
    ft/s}^2$. Its mass and weight are:
    A) 30 lbm and 30 lbf
    B) 60 lbm and 60 lbf
    C) 60 lbm and 30 lbf
    D) 30 lbm and 60 lbf

29. Newton's second law in USCS with mass in lbm is written:
    A) $F = ma$
    B) $F = ma / g_c$
    C) $F = m a g_c$
    D) $F = m g / a$

30. A temperature difference of $50 \; ^\circ\text{C}$ is equal to a difference
    of:
    A) $50 \text{ K}$
    B) $323 \text{ K}$
    C) $90 \text{ K}$
    D) $122 \text{ K}$

31. A temperature difference of $36 \; ^\circ\text{F}$ equals a difference of:
    A) $36 \; ^\circ\text{C}$
    B) $20 \; ^\circ\text{C}$
    C) $2.2 \; ^\circ\text{C}$
    D) $64.8 \; ^\circ\text{C}$

32. Which equation requires temperature on an absolute scale?
    A) $q = kA \, \Delta T / L$
    B) $\delta = \alpha_T L \, \Delta T$
    C) $\eta = 1 - T_L / T_H$
    D) All temperature equations accept any scale

33. To convert a pressure from lbf/in² to lbf/ft², multiply by:
    A) 12
    B) 144
    C) $1/12$
    D) $1/144$

34. In the equation $p = \rho g h / g_c$, if $\rho$ is in lbm/ft³, $g$ in
    ft/s², and $h$ in ft, the result is in:
    A) lbm/ft²
    B) lbf/ft²
    C) lbf/in²
    D) lbm·ft/s²

35. The specific gas constant $R$ for a particular gas is obtained from the
    universal constant by:
    A) Multiplying by molecular weight
    B) Dividing by molecular weight
    C) Multiplying by $g_c$
    D) Dividing by absolute temperature

---

## Answer Key with Explanations

**1.** A **physical quantity** is a measurable property — the length of a beam.
A **dimension** is its fundamental character independent of measurement —
length, symbol $L$. A **unit** is a specific agreed amount of that dimension —
the metre, the foot, the inch. One quantity, one dimension, many units: a beam
4 m long is also 13.12 ft and 157.5 in. (§2.1)

**2.** Historical accident. The gram was originally defined, but the practical
mass standard was a kilogram artifact, and the kilogram was adopted as the base
unit. The awkwardness is that the kilogram is the only base unit carrying a
prefix, so "kilogram" already includes a $10^3$ before you apply any further
prefixes. (§2.2)

**3.** Pressure is force per area, and force is mass times acceleration:

$$1 \text{ Pa} = \frac{1 \text{ N}}{1 \text{ m}^2} = \frac{1 \text{ kg} \cdot \text{m}/\text{s}^2}{\text{m}^2} = \frac{\text{kg}}{\text{m} \cdot \text{s}^2}$$

Dimensionally $ML^{-1}T^{-2}$. Rebuilding it from the definition is more
durable than memorizing the row. (§2.2)

**4.** Every term in a physically valid equation must have the same dimensions;
you cannot add a length to a time. **Necessary**, because a dimensionally
inhomogeneous equation is certainly wrong. **Not sufficient**, because a
missing factor of 2, a wrong sign, or a wrong dimensionless coefficient all
pass the dimensional test cleanly. It catches one whole class of error and is
silent about another. (§2.4)

**5.** Because it converts a *remembering* problem into a *seeing* problem.
When you write the conversion as a fraction and cancel units explicitly, an
inverted factor produces visibly nonsensical leftover units. Deciding to
multiply or divide relies on judgment, which is reliable most of the time and
fails occasionally — and the occasions arrive under time pressure. (§2.5)

**6.** **A mechanical unit system needs exactly three base units** — one each
for mass, length, and time (or force, length, and time). Force is then derived
through $F = ma$, and the system is coherent, meaning no constant is needed.

SI picks kg, m, s and derives the newton: three base units, coherent. USCS with
the slug picks lbf, ft, s and derives the slug: three base units, coherent.

**USCS with both pounds has four**: lbf, lbm, ft, s. The pound-mass and
pound-force were defined independently, neither derived from the other, so the
system is **over-determined**. When a system has a redundant base unit, $F =
ma$ no longer holds and a conversion constant is required to reconcile the
independent definitions. That constant is $g_c$.

So $g_c$ is not physics. It's the numerical cost of keeping two units where one
would do. (§2.6.1)

**7.** Any three of: (i) $g$ is a physical quantity, $g_c$ is a bookkeeping
factor; (ii) $g$ **varies with location**, $g_c$ is fixed by definition
everywhere; (iii) different units — ft/s² versus lbm·ft/(lbf·s²); (iv) $g$
appears in SI equations, $g_c$ never does; (v) different dimensions — $LT^{-2}$
versus $ML \cdot F^{-1}T^{-2}$.

They share 32.174 because **the pound-force was defined using standard
gravity** — specifically as the force accelerating 1 lbm at 32.174 ft/s². The
shared number is a consequence of that design choice, not evidence that the two
are the same thing. (§2.6.3)

**8.** **Mass: unchanged.** Mass is a property of the object, not of its
location.

**Weight: reduced by roughly a factor of six.** Weight is $F_W = mg/g_c$, and
lunar $g$ is about one-sixth of Earth's.

**Horizontal accelerating force: unchanged.** $F = ma/g_c$ contains no $g$ at
all. Only $g_c$, which is a definition and doesn't vary. See Worked Example 6,
where the required force was 20.0 lbf on both bodies. (§2.6.6)

**9.** It means the *typography of a printed equation does not tell you whether
$g_c$ belongs*. Authors omit it when they've assumed slugs, or assumed SI, or
assumed the reader will supply it. Whether it belongs is determined entirely by
what units your numbers are actually in.

The habit that protects you: **carry units through every step of the
arithmetic.** If lbm survives into a result that should be in lbf, you dropped
a $g_c$. The units tell you what the printed equation didn't. (§2.6.7)

**10.** A **value** must account for the offset between zero points: $100 \;
^\circ\text{C} = 373.15 \text{ K}$. A **difference** does not, because both
endpoints shift by the same offset and the shift cancels in the subtraction:

$$(T_2 + 273.15) - (T_1 + 273.15) = T_2 - T_1$$

So $\Delta T$ of 80 °C is $\Delta T$ of 80 K. Crossing degree *sizes* still
requires the 1.8, since that concerns degree size rather than zero point.
(§2.7)

**11.** **The test: does the equation use a bare $T$ or only $\Delta T$?** A
bare $T$ — especially raised to a power or inside a ratio — requires absolute
scale, because a relative-scale magnitude is physically meaningless there.

Require absolute: ideal gas law $pV = mRT$; radiation $q = \sigma_{SB}AT^4$;
thermal efficiency $\eta = 1 - T_L/T_H$.

Accept differences: conduction $q = kA\,\Delta T/L$; thermal expansion $\delta
= \alpha_T L\,\Delta T$. (§2.7)

**12.** They agree because specific weight is $SW = \rho g / g_c$, and **at
standard gravity $g = 32.174$ ft/s² while $g_c = 32.174$ lbm·ft/(lbf·s²), so
the numbers cancel** and $SW$ takes the same numerical value as $\rho$ with
lbf substituted for lbm. That numerical coincidence is the deliberate design
goal of the lbm/lbf system.

They stop agreeing **at any gravitational acceleration other than standard**.
$g_c$ stays fixed; $g$ changes; the ratio $g/g_c$ is no longer 1. (§2.6.6,
Worked Example 8)

**13.** By **units**. All four forms are the same physical constant expressed
in different unit systems. Look at the units of your pressure, volume, mass
quantity, and temperature, then select the form that makes the equation
dimensionally clean. The reliable procedure is to write the equation with units
attached and confirm they cancel — if they don't, you chose the wrong row.
(§2.8)

**14.**
(a) $1 \text{ J} = 1 \text{ N} \cdot \text{m} = \text{kg} \cdot \text{m}^2/\text{s}^2$
(b) $1 \text{ W} = 1 \text{ J}/\text{s} = \text{kg} \cdot \text{m}^2/\text{s}^3$
(c) $1 \text{ N} = \text{kg} \cdot \text{m}/\text{s}^2$
(d) $1 \text{ Pa} = 1 \text{ N}/\text{m}^2 = \text{kg}/(\text{m} \cdot \text{s}^2)$

**15.**

(a) $[v] = LT^{-1}$. $[at^2] = LT^{-2} \cdot T^2 = L$.
$LT^{-1} \ne L$ — **not homogeneous, cannot be correct.**
Correction: $v = at$, giving $LT^{-2} \cdot T = LT^{-1}$ ✓

(b) $[KE] = ML^2T^{-2}$. $[mv^2] = M \cdot L^2T^{-2} = ML^2T^{-2}$ ✓
**Homogeneous.** (Note this is the SI form; in USCS with lbm you need
$/2g_c$.)

(c) $[p] = ML^{-1}T^{-2}$. $[\rho g h^2] = ML^{-3} \cdot LT^{-2} \cdot L^2 =
MT^{-2}$.
$ML^{-1}T^{-2} \ne MT^{-2}$ — **not homogeneous.**
Correction: $p = \rho g h$, giving $ML^{-3} \cdot LT^{-2} \cdot L =
ML^{-1}T^{-2}$ ✓

(d) $[F] = MLT^{-2}$. $\left[\dfrac{mv^2}{r}\right] = \dfrac{M \cdot L^2T^{-2}}{L} = MLT^{-2}$ ✓
**Homogeneous.** (Centripetal force — you'll meet it in Tier 2C.)

**16.**

(a) $85 \; \dfrac{\cancel{\text{mi}}}{\cancel{\text{h}}} \times \dfrac{5{,}280 \text{ ft}}{\cancel{\text{mi}}} \times \dfrac{\cancel{\text{h}}}{3{,}600 \text{ s}} = \dfrac{(85)(5{,}280)}{3{,}600} = \boxed{124.7 \text{ ft/s}}$

*Check:* 60 mph = 88 ft/s, so 85 mph should be $88 \times 85/60 = 124.7$ ✓

(b) $2{,}400 \; \cancel{\text{ft}^3} \times \left(\dfrac{0.3048 \text{ m}}{\cancel{\text{ft}}}\right)^3 = 2{,}400 \times 0.02832 = \boxed{67.96 \text{ m}^3}$

Note the **cubed** conversion factor: $(0.3048)^3 = 0.02832$.

(c) $45 \; \cancel{\text{psi}} \times \dfrac{6.895 \text{ kPa}}{\cancel{\text{psi}}} = \boxed{310.3 \text{ kPa}}$

(d) $18 \; \cancel{\text{in}^2} \times \left(\dfrac{25.4 \text{ mm}}{\cancel{\text{in}}}\right)^2 = 18 \times 645.16 = \boxed{11{,}613 \text{ mm}^2}$

(e) $750 \; \cancel{\text{ft} \cdot \text{lbf}} \times \dfrac{1.356 \text{ J}}{\cancel{\text{ft} \cdot \text{lbf}}} = \boxed{1{,}017 \text{ J}}$

(f) $250 \; \cancel{\text{hp}} \times \dfrac{745.7 \text{ W}}{\cancel{\text{hp}}} = 186{,}425 \text{ W} = \boxed{186.4 \text{ kW}}$

*Check:* 1 kW ≈ 1.341 hp, so $250/1.341 = 186.4$ kW ✓

**17.**

(a) At standard gravity, $g/g_c = 1$ numerically:

$$F_W = \frac{mg}{g_c} = \frac{(180)(32.174)}{32.174} = \boxed{180 \text{ lbf}}$$

(b) $g_c$ method:

$$a = \frac{Fg_c}{m} = \frac{(45)(32.174)}{180} = \frac{1{,}447.8}{180} = \boxed{8.043 \text{ ft/s}^2}$$

(c) Slug method:

$$m = \frac{180}{32.174} = 5.594 \text{ slug} \qquad a = \frac{45}{5.594} = \boxed{8.045 \text{ ft/s}^2}$$

(d) Ratio shortcut: applied force over weight is $45/180 = 0.250$, so

$$a = (0.250)(32.174) = \boxed{8.044 \text{ ft/s}^2} \;\checkmark$$

Three methods, one answer to three figures.

**18.**

(a) $F_W = \dfrac{(25)(32.174)}{32.174} = \boxed{25.0 \text{ lbf}}$

(b) $F_W = \dfrac{mg}{g_c} = \dfrac{(25)(12.2)}{32.174} = \dfrac{305}{32.174} = \boxed{9.48 \text{ lbf}}$

(c) $\boxed{25 \text{ lbm}}$ — **mass does not change with location.**

(d) $F = \dfrac{ma}{g_c} = \dfrac{(25)(8.0)}{32.174} = \dfrac{200}{32.174} = \boxed{6.22 \text{ lbf}}$

(e) $\boxed{6.22 \text{ lbf}}$ — **identical.** $F = ma/g_c$ contains no $g$.

*Check (b):* Martian gravity is about 38% of Earth's, and $25 \times 0.38 =
9.5$ lbf ✓

**19.**

(a) Speed: $45 \text{ mph} \times \dfrac{88 \text{ ft/s}}{60 \text{ mph}} = 66.0 \text{ ft/s}$

$$KE = \frac{mv^2}{2g_c} = \frac{(12{,}000)(66.0)^2}{2(32.174)} = \frac{(12{,}000)(4{,}356)}{64.348} = \frac{52{,}272{,}000}{64.348}$$

$$\boxed{KE = 8.123 \times 10^5 \text{ ft} \cdot \text{lbf}}$$

(b) $\dfrac{8.123 \times 10^5}{778} = \boxed{1{,}044 \text{ Btu}}$

(c) SI check:

$$m = 12{,}000 \times 0.4536 = 5{,}443 \text{ kg} \qquad v = 66.0 \times 0.3048 = 20.12 \text{ m/s}$$

$$KE = \tfrac{1}{2}(5{,}443)(20.12)^2 = (0.5)(5{,}443)(404.8) = 1.102 \times 10^6 \text{ J}$$

Convert back:

$$8.123 \times 10^5 \; \text{ft} \cdot \text{lbf} \times 1.356 = 1.101 \times 10^6 \text{ J} \;\checkmark$$

**20.**

(a) $SW = \dfrac{\rho g}{g_c} = \dfrac{(55)(32.174)}{32.174} = \boxed{55.0 \text{ lbf/ft}^3}$

(b) $p = SW \cdot h = (55.0)(22) = \boxed{1{,}210 \text{ lbf/ft}^2}$

(c) $\dfrac{1{,}210}{144} = \boxed{8.40 \text{ psi}}$

(d) SI check:

$$\rho = 55 \times \frac{0.4536}{0.02832} = 881.1 \text{ kg/m}^3 \qquad h = 22 \times 0.3048 = 6.706 \text{ m}$$

$$p = \rho g h = (881.1)(9.807)(6.706) = 57{,}930 \text{ Pa} = 57.9 \text{ kPa}$$

$$8.40 \text{ psi} \times 6.895 = 57.9 \text{ kPa} \;\checkmark$$

**21.**

(a) $T_1 = 70 + 459.69 = \boxed{529.7 \; ^\circ\text{R}}$
$T_2 = 520 + 459.69 = \boxed{979.7 \; ^\circ\text{R}}$

(b) $T_1 = \dfrac{70 - 32}{1.8} = \dfrac{38}{1.8} = \boxed{21.1 \; ^\circ\text{C}}$
$T_2 = \dfrac{520 - 32}{1.8} = \dfrac{488}{1.8} = \boxed{271.1 \; ^\circ\text{C}}$

(c) $T_1 = 21.1 + 273.15 = \boxed{294.3 \text{ K}}$
$T_2 = 271.1 + 273.15 = \boxed{544.3 \text{ K}}$

*Check via Rankine:* $529.7/1.8 = 294.3$ K ✓ and $979.7/1.8 = 544.3$ K ✓

(d) $\Delta T = 520 - 70 = \boxed{450 \; ^\circ\text{F}}$

In Rankine, offsets cancel: $979.7 - 529.7 = \boxed{450 \; ^\circ\text{R}}$

Crossing degree size: $\dfrac{450}{1.8} = \boxed{250 \; ^\circ\text{C} = 250 \text{ K}}$

*Check in Celsius directly:* $271.1 - 21.1 = 250$ °C ✓

**22.**

(a) Convert to absolute:

$$T_H = 340 + 273.15 = 613.2 \text{ K} \qquad T_L = 45 + 273.15 = 318.2 \text{ K}$$

$$\eta = 1 - \frac{318.2}{613.2} = 1 - 0.5189 = 0.4811$$

$$\boxed{\eta = 48.1\%}$$

(b) Using Celsius directly:

$$\eta_{\text{wrong}} = 1 - \frac{45}{340} = 1 - 0.1324 = 0.8676 = \boxed{86.8\%}$$

(c) $86.8 - 48.1 = \boxed{38.7 \text{ percentage points}}$

Nearly a factor of two, and 86.8% looks like a plausible efficiency to anyone
not checking. This is exactly the trap from §2.7.

**23.**

(a) $\delta = \alpha_T L \Delta T = (1.2 \times 10^{-5})(4.0)(75) = 3.6 \times 10^{-3} \text{ m} = \boxed{3.6 \text{ mm}}$

(b) $\delta = (6.67 \times 10^{-6})(13.12)(135) = 1.181 \times 10^{-2} \text{ ft}$

$$1.181 \times 10^{-2} \; \cancel{\text{ft}} \times \frac{12 \text{ in}}{\cancel{\text{ft}}} = \boxed{0.1418 \text{ in}}$$

*Check agreement:* $3.6 \text{ mm} \div 25.4 = 0.1417 \text{ in}$ ✓

Note that **both calculations used $\Delta T$ as a difference**, and the USCS
version needed a different $\alpha_T$ because the degree size differs — $6.67
\times 10^{-6} = (1.2 \times 10^{-5})/1.8$. That factor of 1.8 is the degree
size conversion appearing in the material property.

**24. B — $ML^{-1}T^{-2}$.** Pressure is force per area:
$\dfrac{MLT^{-2}}{L^2} = ML^{-1}T^{-2}$. (A) is force, (C) is energy, (D) is
density. (§2.4)

**25. C.** $g_c = 32.174 \text{ lbm} \cdot \text{ft}/(\text{lbf} \cdot
\text{s}^2)$. (A) and (B) are values of $g$, not $g_c$ — they have
acceleration units. (D) is the reciprocal. **The units are what distinguish the
answer**, which is the whole point. (§2.6.2)

**26. B.** Fixed by definition and does not vary with location. (A) and (C)
describe $g$. (D) is wrong — SI is coherent and never needs $g_c$. (§2.6.3)

**27. B — 32.174 lbm.** The slug is the coherent USCS mass unit. (C) is the
lbm-to-kg factor. (D) confuses mass with force. (§2.6.5)

**28. C — 60 lbm and 30 lbf.** Mass is unchanged at 60 lbm. Weight is $F_W =
mg/g_c = (60)(16.1)/32.174 = 30.0$ lbf. Since $g$ here is half standard, the
weight halves while the mass does not. (§2.6.6)

**29. B — $F = ma/g_c$.** With mass in lbm you must divide by $g_c$ to obtain
force in lbf. (A) is correct only with mass in slugs or in SI. (§2.6.4)

**30. A — 50 K.** A *difference* of 50 °C is a difference of 50 K, because the
offsets cancel in a subtraction. (B) treats it as a value. (C) applies the 1.8
factor, which belongs to °F–°C conversion, not °C–K. (§2.7)

**31. B — 20 °C.** Crossing degree sizes requires the 1.8: $36/1.8 = 20$. No
offset applies because this is a difference. (A) ignores the degree-size
difference; (D) multiplies instead of dividing. (§2.7)

**32. C — $\eta = 1 - T_L/T_H$.** Temperature appears as a **ratio**, which
requires both values on an absolute scale. (A) and (B) use only $\Delta T$, so
either scale in the correct pair works. (D) is the misconception this question
exists to test. (§2.7)

**33. B — 144.** There are 12 inches per foot, so $12^2 = 144$ square inches
per square foot. Pressure is force per area, and the *larger* area gives the
larger numeric pressure value, so you multiply. Same squared-conversion trap as
Worked Example 4. (§2.5, Worked Example 8)

**34. B — lbf/ft².** Cancel explicitly:

$$\frac{\dfrac{\text{lbm}}{\text{ft}^3} \cdot \dfrac{\text{ft}}{\text{s}^2} \cdot \text{ft}}{\dfrac{\text{lbm} \cdot \text{ft}}{\text{lbf} \cdot \text{s}^2}} = \frac{\text{lbf}}{\text{ft}^2}$$

Without the $g_c$ you'd be left with lbm/(ft·s²), which is choice (A)'s
territory and not a pressure at all. (§2.6.7)

**35. B — Dividing by molecular weight.** $R = \bar{R}/MW$. Note the notation
caution: some Handbook sections write plain $R$ for the universal constant.
(§2.8)

---

## Quick Reference

**Dimensions**

$$M \text{ mass} \quad L \text{ length} \quad T \text{ time} \quad \Theta \text{ temperature} \quad I \text{ current} \quad N \text{ amount} \quad J \text{ luminous intensity}$$

**Derived units from base**

$$\text{N} = \frac{\text{kg} \cdot \text{m}}{\text{s}^2} \qquad \text{Pa} = \frac{\text{kg}}{\text{m} \cdot \text{s}^2} \qquad \text{J} = \frac{\text{kg} \cdot \text{m}^2}{\text{s}^2} \qquad \text{W} = \frac{\text{kg} \cdot \text{m}^2}{\text{s}^3}$$

**Dimensional homogeneity**

Every term must share dimensions. Necessary, not sufficient. Free error check
on every equation you write.

**Factor-label method**

Write the fraction. Cancel the units. If the leftover units aren't what you
wanted, you inverted a factor. Never decide multiply-versus-divide by judgment.

**THE POUND PROBLEM**

$$\boxed{g_c = 32.174 \; \frac{\text{lbm} \cdot \text{ft}}{\text{lbf} \cdot \text{s}^2}}$$

Exists because lbm/lbf USCS has **four** base units where three suffice. It is
bookkeeping, not physics.

| | $g$ | $g_c$ |
|---|---|---|
| What | local gravity | unit conversion constant |
| Varies? | **yes** | **no** |
| Units | ft/s² | lbm·ft/(lbf·s²) |
| In SI? | yes | **never** |

$$1 \text{ slug} = 32.174 \text{ lbm}$$

**Newton's second law**

| System | Form |
|---|---|
| SI (kg, N) | $F = ma$ |
| USCS (slug, lbf) | $F = ma$ |
| USCS (lbm, lbf) | $F = ma/g_c$ |

**The $g_c$ family** — *Handbook p. 1*

$$F = \frac{ma}{g_c} \qquad F_W = \frac{mg}{g_c} \qquad KE = \frac{mv^2}{2g_c} \qquad PE = \frac{mgh}{g_c}$$

$$p = \frac{\rho g h}{g_c} \qquad SW = \frac{\rho g}{g_c} \qquad \tau = \frac{\mu}{g_c}\frac{dv}{dy}$$

*Frequently omitted in print. Whether it belongs depends on your units, not on
the typography.*

**Ratio shortcut (lbm/lbf only)**

$$\frac{F}{F_W} = \frac{a}{g}$$

**Mass versus weight**

Mass: property of the object, location-independent.
Weight: a force, $F_W = mg/g_c$, location-dependent.
Horizontal accelerating force: contains **no $g$**, so location-independent.

**Temperature**

$$^\circ\text{F} = 1.8(^\circ\text{C}) + 32 \qquad ^\circ\text{C} = \frac{^\circ\text{F} - 32}{1.8}$$

$$^\circ\text{R} = \;^\circ\text{F} + 459.69 \qquad \text{K} = \;^\circ\text{C} + 273.15$$

$$\text{K} = \frac{^\circ\text{R}}{1.8}$$

| | Absolute | Relative | Offset |
|---|---|---|---|
| SI degree | K | °C | 273.15 |
| USCS degree | °R | °F | 459.69 |

**Differences:** $\Delta T$ of 1 °C = 1 K. $\Delta T$ of 1 °F = 1 °R.
$\Delta T$ of 1 °C = 1.8 °F.

**Absolute required** whenever a bare $T$ appears in a power or a ratio: ideal
gas law, radiation, thermal efficiency.

**Landmark conversions**

| From | To | × |
|---|---|---|
| in | mm | 25.4 |
| ft | m | 0.3048 |
| mile | ft | 5,280 |
| lbf | N | 4.448 |
| lbm | kg | 0.4536 |
| slug | kg | 14.59 |
| psi | kPa | 6.895 |
| psi | lbf/ft² | 144 |
| atm | kPa | 101.3 |
| atm | psi | 14.70 |
| ft·lbf | J | 1.356 |
| Btu | ft·lbf | 778 |
| Btu | J | 1,055 |
| hp | W | 745.7 |

**Worth knowing cold**

$$60 \text{ mph} = 88 \text{ ft/s} \qquad \text{water: } 62.4 \; \frac{\text{lbm}}{\text{ft}^3} = 62.4 \; \frac{\text{lbf}}{\text{ft}^3} = 1{,}000 \; \frac{\text{kg}}{\text{m}^3}$$

$$\text{water: } 0.433 \; \frac{\text{psi}}{\text{ft of depth}} \qquad \text{atmosphere} \approx 100 \text{ kPa} \approx 14.7 \text{ psi}$$

**Universal gas constant — four forms, p. 2**

| Value | Units |
|---|---|
| 8,314 | J/(kmol·K) |
| 8,314 | kPa·m³/(kmol·K) |
| 1,545 | ft·lbf/(lb mole·°R) |
| 0.08206 | L·atm/(mol·K) |

$$R = \frac{\bar{R}}{MW}$$

Select by cancelling units, not by memory.

**Not in the Handbook — memorize**

Quantity/dimension/unit distinction · dimensional homogeneity · factor-label
method · **why $g_c$ exists** · mass versus weight as concepts · value versus
difference in temperature · which equations need absolute temperature

---

## What's Next

Apprentice, you've just done the hardest work in Layer 1. Not the most
difficult mathematics — the most consequential bookkeeping. Every mechanics,
fluids, and thermodynamics problem you touch for the rest of this guide runs
through what you just built.

Let me tell you what you should take away, in one sentence: **$g_c$ is not a
rule you memorized, it's a consequence you understand.** A system with four
base units where three would do requires a reconciling constant. That's it.
Understand that and you cannot misplace it, because you know what job it's
doing.

In **Chapter 01-03: Accuracy, Precision, and Significant Figures**, we close
out Tier 1A with the question of how many digits to report — and, more
importantly, what those digits actually claim.

Here's the thing that makes it interesting rather than tedious. Every number in
an engineering calculation carries an implicit statement about its own
reliability. Write 3.5 and you've claimed something different than if you'd
written 3.500. Report a stress to eight digits from inputs known to two and
you've made a claim your data cannot support — which is a small dishonesty,
and one your reviewer will notice.

The Handbook gives six numbered rules for significant figures and states the
engineering convention of three to four digits in a final answer. We'll work
through all six, and I'll show you the specific place where rounding too early
in a multi-step calculation produces an answer that's wrong in the digit you
were reporting.

Then Tier 1A is done, you take the review exam, and we start on algebra.

Bring the Handbook, open to page 2.

See you there.

— Your Mentor