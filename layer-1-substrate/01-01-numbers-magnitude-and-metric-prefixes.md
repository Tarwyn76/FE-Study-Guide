---
chapter: "01-01"
title: "Numbers, Magnitude, and Metric Prefixes"
layer: 1
tier: A
template: technical
ledger_ids: [MATH-1A-001-01, MATH-1A-001-02, MATH-1A-001-03]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: revised
---

# Chapter 01-01: Numbers, Magnitude, and Metric Prefixes

> *"The engineer who can't tell a micro from a nano will eventually design
> something that fails by a factor of a thousand. Usually on paper. Sometimes
> not."*

---

## Before You Start

**Prerequisites:** Layer 0 (Chapters 00-01 through 00-03). No technical
prerequisites — this chapter starts from arithmetic.

**Skip if:** You pass the Tier 1A test-out quiz. Every route includes this
chapter, but nobody needs to read what they already know.

**Time:** ~45 min read · ~50 min review questions

---

## On the Board Today

Apprentice, sit down. We're starting at the bottom.

I know how this looks. Chapter one of an engineering exam guide and we're
talking about place value and scientific notation. You've got a high school
diploma. You can multiply. This feels like an insult.

It isn't, and let me tell you why.

Engineering quantities span an absurd range. The charge on an electron is
about $1.6 \times 10^{-19}$ coulombs. The elastic modulus of steel is about
$2 \times 10^{11}$ pascals. That's thirty orders of magnitude between two
numbers you'll both use before you're through this guide. Thirty. If those
were distances, one would be smaller than an atom and the other would reach
past the sun.

Working fluently across that range is not a mathematical skill. It's a
*bookkeeping* skill. And here's the thing about bookkeeping errors: they
don't feel like errors. When you set up a stress calculation correctly,
choose the right equation, and substitute correctly — but write nano where
you meant micro — you get an answer that's wrong by a factor of a thousand
and looks completely reasonable on the page.

> ---
> **Mentor's Margin**
>
> I spent twenty years around medicine. The most dangerous drug errors were
> never the exotic ones. They were decimal points. A ten-fold overdose looks
> exactly like a correct dose written by someone in a hurry. Engineering has
> the same failure mode and the same remedy: a system so automatic that you
> can't get it wrong even when tired.
>
> ---

That's what this chapter builds. Not new mathematics — a *system*. By the end
you'll move between $10^{-12}$ and $10^{12}$ without thinking about it, which
is exactly how often you should think about it: never.

One more thing before we start. Notice something about this chapter's
contents: almost none of it is in the Handbook. Scientific notation isn't in
there. Order of operations isn't in there. These are exactly the "basic
theories, conversions, formulas, and definitions examinees are expected to
know" that the Handbook told us it left out, back in 00-03 §0.2.

The metric prefixes *are* in there, on page 1. We'll talk about why you
should memorize them anyway.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **LO-1** Classify a number as integer, rational, irrational, or real
* **LO-2** Apply the order of operations correctly to a multi-term expression
* **LO-3** Write any number in scientific notation and convert back to
  decimal form
* **LO-4** Multiply and divide quantities expressed in scientific notation
* **LO-5** Add and subtract quantities in scientific notation by matching
  exponents first
* **LO-6** State the order of magnitude of a quantity and use it to
  sanity-check a result
* **LO-7** Recall the metric prefixes from atto through exa with symbols and
  powers of ten
* **LO-8** Convert a quantity between any two metric prefixes without error
* **LO-9** Express a quantity in engineering notation
* **LO-10** Recognize the prefix errors that most commonly cost exam points

---

## Notation Used Here

| Symbol | Meaning in this chapter | SI | USCS |
|---|---|---|---|
| $N$ | mantissa (coefficient) in scientific notation, $1 \le \lvert N \rvert < 10$ | — | — |
| $x$ | exponent, a power of ten | — | — |
| $\lvert a \rvert$ | absolute value of $a$ | — | — |

No physical quantities are *defined* in this chapter. Where a worked example
uses $\sigma$, $A$, $V$, $D$, or $Q_v$, those are illustrative mentions in
the sense of 00-01 §0.6 — borrowed to give the arithmetic something to be
about. Each gets its real definition in its own chapter, and nothing here
depends on knowing what they mean.

---

## 1.1 Kinds of Numbers

Quick vocabulary pass. You use these words already; I want us using them the
same way.

| Type | Definition | Examples |
|---|---|---|
| **Integer** | A whole number, positive, negative, or zero | $-3$, $0$, $7$, $110$ |
| **Rational** | Expressible as a ratio of two integers | $\tfrac{1}{2}$, $-\tfrac{7}{3}$, $0.25$, $4$ |
| **Irrational** | A real number not expressible as such a ratio | $\pi$, $e$, $\sqrt{2}$ |
| **Real** | Any rational or irrational number | all of the above |

![FIG-01-01-001: Nested-set diagram showing integers inside rationals inside reals, with irrationals occupying the remainder of the reals — pi, e, and root two labelled in the irrational region, and root nine labelled inside the integers to show that a radical sign does not make a number irrational](../figures/FIG-01-01-001-number-sets.png)

Two notes with practical weight.

**Every integer is rational.** $4 = \tfrac{4}{1}$. And every terminating or
repeating decimal is rational. $0.25 = \tfrac{1}{4}$; $0.\overline{3} =
\tfrac{1}{3}$. The converse does not hold — $\tfrac{1}{3}$ is rational but
its decimal form never terminates.

**Irrational numbers never terminate and never repeat.** This is why $\pi$
gets truncated in every calculation you'll ever do, and why *when* you
truncate matters. Round $\pi$ to 3.14 at the start of a five-step
calculation and the error compounds through every step. Carry full precision
and round once at the end.

> ---
> **Mentor's Margin**
>
> Use your calculator's $\pi$ key. Every time. Not 3.14, not 3.1416. The key
> exists so that you never introduce an avoidable error, and it costs you
> exactly one keystroke.
>
> ---

We'll meet **complex numbers** in Chapter 01-12. They're not real numbers,
and they matter enormously for AC circuits and vibration. Not yet.

---

## 1.2 Order of Operations

There is one correct order for evaluating an expression, and ambiguity here
produces wrong answers that look right.

The order:

1. **Parentheses** and other grouping symbols, innermost first
2. **Exponents** and roots
3. **Multiplication and division**, left to right
4. **Addition and subtraction**, left to right

Two details that trip people:

**Multiplication and division have equal precedence**, evaluated left to
right. So $12 \div 3 \times 2$ is not $12 \div 6 = 2$. It is $4 \times 2 =
8$. Same for addition and subtraction.

**A fraction bar is a grouping symbol.** When you write

$$\frac{a + b}{c + d}$$

the numerator and denominator are each implicitly parenthesized. Enter that
into a calculator as written — `a + b / c + d` — and you'll get something
else entirely. You must key it as `(a + b) / (c + d)`.

> ---
> **Mentor's Margin**
>
> This is the single most common calculator error I've seen, and it survives
> into professional practice. Any time you transcribe a fraction into a
> calculator, put parentheses around the whole numerator and the whole
> denominator. Every time. Even when you're sure you don't need them. The
> habit costs four keystrokes and saves you a career's worth of silent
> errors.
>
> ---

### Worked Example 1 — Order of Operations

**Given.** Evaluate:

$$\frac{3 + 2 \times 4^2}{5 - 3}$$

**Find.** The numeric value.

**Approach.** Treat numerator and denominator as separately grouped. Inside
each, apply the order of operations.

**Solution.**

Step 1 — Numerator, exponent first.

$$4^2 = 16$$

Step 2 — Numerator, multiplication before addition.

$$2 \times 16 = 32$$
$$3 + 32 = 35$$

Step 3 — Denominator.

$$5 - 3 = 2$$

Step 4 — Divide.

$$\frac{35}{2} = 17.5$$

**Check.** Rough estimate: the numerator is dominated by $2 \times 16 = 32$,
so it's a bit over 30. Divided by 2, that's a bit over 15. Our answer of
17.5 sits in that range. ✓

Two wrong answers worth knowing, because each comes from a specific mistake:

**40** — adding before multiplying in the numerator. $(3 + 2) \times 16 = 80$,
then $80 \div 2 = 40$.

**6.4** — ignoring the grouping implied by the fraction bar, and evaluating
$3 + 2 \times 4^2 \div 5 - 3$ instead. That gives $3 + 6.4 - 3 = 6.4$. This
is exactly what an unparenthesized calculator entry produces.

---

## 1.3 Scientific Notation

Here's the tool that makes the thirty-order-of-magnitude problem manageable.

Any number can be written as:

$$N \times 10^x$$

where $N$ is the **mantissa**, with $1 \le \lvert N \rvert < 10$, and $x$ is
the **exponent**, an integer.

That constraint on $N$ is what makes the form useful. Exactly one digit
before the decimal point means every number has exactly one scientific
notation representation, so two numbers can be compared at a glance. (Zero is
the one exception. No mantissa in the range $1 \le \lvert N \rvert < 10$ can
produce it, so zero is just written 0.)

| Decimal | Scientific notation |
|---|---|
| $1{,}000$ | $1 \times 10^3$ |
| $4{,}700$ | $4.7 \times 10^3$ |
| $93{,}000{,}000$ | $9.3 \times 10^7$ |
| $1$ | $1 \times 10^0$ |
| $0.001$ | $1 \times 10^{-3}$ |
| $0.0000625$ | $6.25 \times 10^{-5}$ |
| $-2{,}200$ | $-2.2 \times 10^3$ |

### Reading the exponent

The exponent tells you how far to move the decimal point.

**Positive exponent → move right.** The number gets larger.

$$4.7 \times 10^6 \;\rightarrow\; 4{,}700{,}000$$

Six places right. Count them.

**Negative exponent → move left.** The number gets smaller.

$$4.7 \times 10^{-6} \;\rightarrow\; 0.0000047$$

Six places left.

**Zero exponent → don't move.** $10^0 = 1$, and anything times one is
itself.

### Converting to scientific notation

**Move the decimal point until exactly one nonzero digit sits to its left.
Count the moves. Moving left gives a positive exponent; moving right gives a
negative one.**

$93{,}000{,}000$ — the decimal is implicitly after the last zero. Move it
left seven places to sit after the 9. Seven moves left → exponent $+7$.

$$93{,}000{,}000 = 9.3 \times 10^7$$

$0.0000625$ — move right five places to sit after the 6. Five moves right →
exponent $-5$.

$$0.0000625 = 6.25 \times 10^{-5}$$

> ---
> **Mentor's Margin**
>
> The direction rule feels backwards to everyone at first, so here's the
> reasoning instead of the rule. You're not changing the number, only how
> it's written. Moving the decimal left makes the mantissa *smaller*, so the
> exponent must get *larger* to compensate. Small mantissa, big exponent.
> Understand it that way and you'll never have to remember which direction
> is positive.
>
> ---

### Multiplication and division

**Multiplication: multiply the mantissas, add the exponents.**

$$(N_1 \times 10^{x_1})(N_2 \times 10^{x_2}) = (N_1 N_2) \times 10^{x_1 + x_2}$$

**Division: divide the mantissas, subtract the exponents.**

$$\frac{N_1 \times 10^{x_1}}{N_2 \times 10^{x_2}} = \left(\frac{N_1}{N_2}\right) \times 10^{x_1 - x_2}$$

After either operation, **renormalize** if the mantissa has left the range
$1 \le \lvert N \rvert < 10$.

### Worked Example 2 — Multiplication and Division

**Given.** Evaluate, expressing each answer in proper scientific notation:

(a) $(4 \times 10^6)(2 \times 10^{-3})$
(b) $\dfrac{8 \times 10^8}{4 \times 10^2}$
(c) $(3 \times 10^{-5})(5 \times 10^{-4})$
(d) $\dfrac{1.44 \times 10^{-3}}{1.2 \times 10^{-6}}$

**Solution.**

(a) Mantissas: $4 \times 2 = 8$. Exponents: $6 + (-3) = 3$.

$$\boxed{8 \times 10^3}$$

Mantissa is in range. No renormalization needed.

(b) Mantissas: $8 \div 4 = 2$. Exponents: $8 - 2 = 6$.

$$\boxed{2 \times 10^6}$$

(c) Mantissas: $3 \times 5 = 15$. Exponents: $-5 + (-4) = -9$.

$$15 \times 10^{-9}$$

Mantissa 15 is out of range. Renormalize: $15 = 1.5 \times 10^1$, so

$$1.5 \times 10^1 \times 10^{-9} = \boxed{1.5 \times 10^{-8}}$$

(d) Mantissas: $1.44 \div 1.2 = 1.2$. Exponents: $-3 - (-6) = -3 + 6 = 3$.

$$\boxed{1.2 \times 10^3}$$

**Check.** Verify (d) by converting to decimal and dividing:
$1.44 \times 10^{-3} = 0.00144$ and $1.2 \times 10^{-6} = 0.0000012$.

$$\frac{0.00144}{0.0000012} = 1{,}200 = 1.2 \times 10^3 \;\checkmark$$

Verify (c) similarly: $(0.00003)(0.0005) = 0.000000015 = 1.5 \times 10^{-8}$.
✓

Part (d) is the one to watch. **Subtracting a negative exponent adds.** Sign
errors on exponent arithmetic are extremely common, and they produce answers
wrong by many orders of magnitude.

### Addition and subtraction

This one has a different rule, and it's the rule people skip.

**You cannot add or subtract until the exponents match.**

$$N_1 \times 10^{x} + N_2 \times 10^{x} = (N_1 + N_2) \times 10^{x}$$

Notice that the exponent $x$ is the *same* in both terms. That's what makes
the step legal — $10^x$ is a common factor you can pull out front. When the
exponents differ, there's no common factor and nothing to pull out.

So the procedure is: **rewrite one term so both exponents agree, then add the
mantissas.** Rewriting means deliberately leaving proper scientific notation
for a moment, which is fine. You renormalize at the end.

$$3 \times 10^5 + 4 \times 10^4 = 3 \times 10^5 + 0.4 \times 10^5 = 3.4 \times 10^5$$

**It is not $7 \times 10^5$.** That's the error, and it's off by a factor of
about two.

> ---
> **Mentor's Margin**
>
> You already know this rule in a different costume. You would never add
> 5 kΩ and 300 Ω and report 305 of anything. You'd convert one to the other's
> unit first. Matching exponents *is* converting to a common unit. Every time
> you're tempted to just add the mantissas, ask yourself whether you'd add
> the numbers if they had different prefixes on them. Same question, same
> answer.
>
> ---

### Worked Example 3 — Addition and Subtraction

**Given.** Evaluate, expressing each answer in proper scientific notation:

(a) $3 \times 10^5 + 4 \times 10^4$
(b) $6.2 \times 10^{-3} - 8.0 \times 10^{-4}$
(c) $9.5 \times 10^6 + 7.0 \times 10^6$

**Approach.** Match exponents, combine mantissas, renormalize if needed,
verify in decimal form.

**Solution.**

(a) Exponents differ. Rewrite the second term to match the first:
$4 \times 10^4 = 0.4 \times 10^5$.

$$3 \times 10^5 + 0.4 \times 10^5 = 3.4 \times 10^5$$

$$\boxed{3.4 \times 10^5}$$

*Check.* $300{,}000 + 40{,}000 = 340{,}000 = 3.4 \times 10^5$ ✓

(b) Rewrite: $8.0 \times 10^{-4} = 0.80 \times 10^{-3}$.

$$6.2 \times 10^{-3} - 0.80 \times 10^{-3} = 5.4 \times 10^{-3}$$

$$\boxed{5.4 \times 10^{-3}}$$

*Check.* $0.0062 - 0.00080 = 0.0054$ ✓

(c) Exponents already match. Add mantissas directly.

$$9.5 + 7.0 = 16.5 \;\rightarrow\; 16.5 \times 10^6$$

Mantissa out of range. Renormalize:

$$\boxed{1.65 \times 10^7}$$

*Check.* $9{,}500{,}000 + 7{,}000{,}000 = 16{,}500{,}000 = 1.65 \times 10^7$ ✓

Part (c) is the reminder that renormalization applies to sums too, not just
products.

### Your calculator

Every approved scientific calculator has an exponent-entry key, marked
`EE`, `EXP`, or `×10ˣ`.

To enter $4.7 \times 10^{-6}$: press `4.7`, then the exponent key, then `6`,
then the sign-change key. **Do not** press `× 10 ^ −6`.

> ---
> **Mentor's Margin**
>
> Pressing `4.7 × 10 EE −6` gives you $4.7 \times 10 \times 10^{-6}$, which
> is ten times too large. I've watched this error destroy an otherwise
> perfect solution. Learn your calculator's exponent key and use it
> exclusively. Then verify with a known case: enter $1 \times 10^3$ and
> confirm the display reads 1,000, not 10,000.
>
> ---

---

## 1.4 Orders of Magnitude

The **order of magnitude** of a quantity is the power of ten nearest its
size. It's a deliberately crude measure, and its crudeness is the point.

| Quantity | Value | Order of magnitude |
|---|---|---|
| Electron charge | $1.6 \times 10^{-19}$ C | $10^{-19}$ |
| Diameter of a human hair | $\sim 7 \times 10^{-5}$ m | $10^{-4}$ |
| Standard gravity | $9.807$ m/s² | $10^1$ |
| Atmospheric pressure | $1.013 \times 10^5$ Pa | $10^5$ |
| Elastic modulus of steel | $\sim 2 \times 10^{11}$ Pa | $10^{11}$ |

Convention: if the mantissa is below about 3, the order of magnitude is the
exponent; above that, round up. So $7 \times 10^{-5}$ is closer to $10^{-4}$
than to $10^{-5}$. (The exact crossover is $\sqrt{10} \approx 3.16$, which is
where a mantissa sits equally far from both powers of ten on a log scale. Use
3; nothing here depends on the third digit.) Don't get precious about the
boundary — the whole tool is approximate.

### Why this matters on the exam

**Order of magnitude is your error detector.**

Estimate the answer to one significant figure *before* you compute it.
Then compare. If your computed answer is off from your estimate by a factor
of a thousand, you have a prefix error. If it's off by ten, you have a
decimal error. If it matches, you probably did it right.

This takes fifteen seconds and catches the class of error that is otherwise
invisible.

### Worked Example 4 — Estimation as a Check

**Given.** A steel member with cross-sectional area $5{,}600 \text{ mm}^2$
carries an axial load of $840 \text{ kN}$. The axial stress is the load
divided by the area.

**Find.** The stress in pascals and in megapascals. Estimate first, then
compute.

**Approach.** Convert both quantities to base SI units, estimate to one
significant figure, then compute exactly and compare.

**Solution.**

Step 1 — Convert to base units.

$$840 \text{ kN} = 840 \times 10^3 \text{ N} = 8.40 \times 10^5 \text{ N}$$

$$5{,}600 \text{ mm}^2 = 5{,}600 \times 10^{-6} \text{ m}^2 = 5.60 \times 10^{-3} \text{ m}^2$$

Note the area conversion. A millimetre is $10^{-3}$ m, so a *square*
millimetre is $(10^{-3})^2 = 10^{-6}$ m². Squaring the prefix squares the
power of ten.

Step 2 — Estimate first.

$$\frac{8 \times 10^5}{6 \times 10^{-3}} \approx 1.3 \times 10^{8} \text{ Pa}$$

So expect something around $10^8$ Pa.

Step 3 — Compute.

$$\sigma = \frac{8.40 \times 10^5 \text{ N}}{5.60 \times 10^{-3} \text{ m}^2} = 1.50 \times 10^8 \text{ N/m}^2 = 1.50 \times 10^8 \text{ Pa}$$

Step 4 — Express with a prefix.

$$1.50 \times 10^8 \text{ Pa} = 150 \times 10^6 \text{ Pa} = 150 \text{ MPa}$$

**Check.** Computed $1.50 \times 10^8$ against estimate $1.3 \times 10^8$ —
same order of magnitude, and the estimate was low because we rounded 5.60
up to 6. ✓

Independent sanity check: structural steel yields somewhere around 250 MPa,
and 150 MPa is a plausible working stress below that. If we'd gotten 150 kPa
or 150 GPa, the physics would be telling us we made a bookkeeping error. ✓

> ---
> **Mentor's Margin**
>
> That last check is the one that matters most, and it's not a math check —
> it's an engineering check. Once you know that steel yields in the hundreds
> of MPa, that concrete compressive strength lives in the tens of MPa, and
> that atmospheric pressure is about 100 kPa, you have a physical intuition
> that catches errors no arithmetic review would. Build that library of
> reference magnitudes deliberately as you go through this guide.
>
> ---

**Watch the squared prefix.** That $\text{mm}^2 \rightarrow \text{m}^2$
conversion is $10^{-6}$, not $10^{-3}$. Getting it wrong gives 150 kPa
instead of 150 MPa — off by a thousand, and completely plausible-looking on
the page. Cubic prefixes cube: $\text{mm}^3 \rightarrow \text{m}^3$ is
$10^{-9}$.

---

## 1.5 Metric Prefixes

Instead of writing $10^6$ ohms, we write **megohm**. Instead of $10^{-3}$
amperes, **milliampere**. The prefixes are the working shorthand of the
entire profession.

Here is the full set as the Handbook gives it.

| Multiple | Prefix | Symbol |
|---|---|---|
| $10^{18}$ | exa | E |
| $10^{15}$ | peta | P |
| **$10^{12}$** | **tera** | **T** |
| **$10^{9}$** | **giga** | **G** |
| **$10^{6}$** | **mega** | **M** |
| **$10^{3}$** | **kilo** | **k** |
| $10^{2}$ | hecto | h |
| $10^{1}$ | deka | da |
| $10^{-1}$ | deci | d |
| $10^{-2}$ | centi | c |
| **$10^{-3}$** | **milli** | **m** |
| **$10^{-6}$** | **micro** | **µ** |
| **$10^{-9}$** | **nano** | **n** |
| **$10^{-12}$** | **pico** | **p** |
| $10^{-15}$ | femto | f |
| $10^{-18}$ | atto | a |

**Memorize the bolded rows — tera, giga, mega, kilo, milli, micro, nano,
pico.** Those eight cover the overwhelming majority of engineering work.
Learn the rest by recognition.

![FIG-01-01-002: Vertical ladder of the sixteen metric prefixes from exa at the top to atto at the bottom, each rung labelled with prefix name, symbol, and power of ten, with the eight high-frequency rungs from tera to pico highlighted as the memorization band](../figures/FIG-01-01-002-prefix-ladder.png)

### Symbol details that matter

**Case is not optional.** `M` is mega, $10^6$. `m` is milli, $10^{-3}$. They
differ by a factor of one billion. Writing `10 MA` when you mean `10 mA` is
not a typo — it's a different quantity by nine orders of magnitude.

**Capital letters for $10^6$ and above; lowercase below.** With one
exception: kilo is lowercase `k`, even though it's $10^3$. There's no reason;
it's just history. Note also that `K` uppercase means kelvin, the temperature
unit.

**Micro is the Greek letter mu, µ.** In plain text you'll see it written
`u` — as in `uF` for microfarad. Read it as micro.

**Deka is `da`, two letters.** The only two-letter prefix symbol.

### Engineering notation

**Engineering notation** is scientific notation restricted to exponents that
are multiples of three, so every value maps directly onto a prefix.

| Scientific | Engineering | With prefix |
|---|---|---|
| $1.5 \times 10^8$ Pa | $150 \times 10^6$ Pa | $150$ MPa |
| $4.7 \times 10^3$ Ω | $4.7 \times 10^3$ Ω | $4.7$ kΩ |
| $2.2 \times 10^{-5}$ F | $22 \times 10^{-6}$ F | $22$ µF |
| $6.8 \times 10^{-10}$ F | $680 \times 10^{-12}$ F | $680$ pF |

Because exponents come in steps of three, the mantissa in engineering
notation ranges from 1 up to 1000 rather than 1 up to 10.

Most calculators have an engineering-notation display mode. **Find it and
use it.** It does this conversion for you, which removes an entire category
of error.

### Converting between prefixes

The rule, and then the reasoning.

**Rule: to a larger prefix, the number gets smaller. To a smaller prefix,
the number gets larger.**

**Reasoning: the physical quantity doesn't change. If the unit gets bigger,
you need fewer of them.**

| From | To | Shift | Result |
|---|---|---|---|
| $4{,}700$ Ω | kΩ | 3 left | $4.7$ kΩ |
| $2.2$ MΩ | kΩ | 3 right | $2{,}200$ kΩ |
| $0.47$ µF | pF | 6 right | $470{,}000$ pF |
| $15$ mm | µm | 3 right | $15{,}000$ µm |
| $4.7$ GPa | MPa | 3 right | $4{,}700$ MPa |
| $250{,}000$ Pa | kPa | 3 left | $250$ kPa |

![FIG-01-01-003: Two-directional arrow diagram over the prefix ladder — an upward arrow labelled "larger prefix, smaller number" and a downward arrow labelled "smaller prefix, larger number" — with the worked conversion 4,700 ohms to 4.7 kilohms traced as an example](../figures/FIG-01-01-003-prefix-direction.png)

### Worked Example 5 — A Prefix Chain

**Given.** A capacitance of $0.0000000047 \text{ F}$.

**Find.** Express it in scientific notation, then in engineering notation,
then with the most natural prefix. Also express it in picofarads.

**Solution.**

Step 1 — Scientific notation. Move the decimal right nine places to sit
after the 4.

$$0.0000000047 \text{ F} = 4.7 \times 10^{-9} \text{ F}$$

Step 2 — Engineering notation. The exponent $-9$ is already a multiple of
three, so nothing changes.

$$4.7 \times 10^{-9} \text{ F}$$

Step 3 — Apply the prefix. $10^{-9}$ is nano.

$$\boxed{4.7 \text{ nF}}$$

Step 4 — Convert to picofarads. Pico is $10^{-12}$, which is *smaller* than
nano, so the number gets *larger*. From $10^{-9}$ to $10^{-12}$ is three
steps down, so shift the decimal three places right.

$$4.7 \text{ nF} = 4{,}700 \text{ pF}$$

**Check.** Verify by returning to base units:

$$4{,}700 \text{ pF} = 4{,}700 \times 10^{-12} \text{ F} = 4.7 \times 10^{3} \times 10^{-12} \text{ F} = 4.7 \times 10^{-9} \text{ F} \;\checkmark$$

Matches Step 1. ✓

> ---
> **Mentor's Margin**
>
> Always verify a prefix conversion by taking the result back to base units.
> It takes ten seconds and it catches the direction errors, which are the
> only errors people actually make here. Nobody miscounts three places.
> Everybody occasionally counts them the wrong way.
>
> ---

---

## As the Handbook States It

**Metric prefixes — in the Handbook.**

> **Handbook, p. 1** — *Units and Conversion Factors*

The complete prefix table appears on the first page of the Handbook, in the
"METRIC PREFIXES" block, with columns for Multiple, Prefix, and Symbol,
running from $10^{-18}$ atto through $10^{18}$ exa.

**So why memorize them?**

Because a lookup costs you fifteen to twenty seconds, and you will need
prefixes on a large fraction of the questions on your exam. Twenty seconds
times forty questions is thirteen minutes — about four and a half questions'
worth of working time, spent retrieving something you could know cold.

Look up what you use rarely. Memorize what you use constantly. Prefixes are
firmly in the second category, and 00-03 §0.2 calls this exact case out as
the clearest example of material that's in the Handbook and still worth
knowing cold.

**Also on page 1, worth knowing where to find:**

- **Temperature conversions.** Four relationships connecting °F, °C, °R, and
  K. We'll use them properly in Chapter 01-02.
- **Commonly used equivalents.** A short list of water densities and weights
  in both unit systems.
- **The customary treatment of force and mass**, with its conversion
  constant. That's Chapter 01-02, and it's the most important half-page in
  the document.

> **Preview note.** The two customary units at issue on that half-page are
> pound-mass and pound-force, and the constant connecting them is written
> $g_c$. Chapter 01-02 develops all three from nothing and explains why the
> constant has to exist. You don't need any of it here.

**Scientific notation, order of operations, and orders of magnitude — NOT in
the Handbook.**

These are not tabulated anywhere. They are exactly the "basic theories,
conversions, formulas, and definitions examinees are expected to know" that
the Handbook's introduction says have been omitted.

**You must know this chapter's non-prefix content cold.** There is no page to
turn to.

**Notation note.** The Handbook writes micro as the Greek letter µ. Some
datasheets and older sources write `u`. This guide uses µ throughout.

---

## Source Verification

> **Source verification.** The metric prefix table, the temperature
> conversions, the commonly used equivalents, and the customary
> force-and-mass constant are all located on page 1 of *FE Reference
> Handbook* edition 10.6, transcribed from that edition. **Page numbers
> change between editions.** Confirm the edition designated for your exam
> administration at ncees.org, and confirm that page 1 still carries all
> four blocks, before you commit the location to memory. The quoted
> statement about omitted basic theories is from the Handbook's
> Introduction; see 00-03 §0.1 for the full citation and the caveat that the
> Introduction is among the pages excluded from the exam-day PDF.

---

## Worked Examples

### Worked Example 6 — Mixed Prefixes in One Calculation

**Given.** A resistor of $4.7 \text{ k}\Omega$ carries a current of
$250 \text{ µA}$. The voltage across a resistor is the product of resistance
and current.

**Find.** The voltage, expressed with an appropriate prefix.

**Approach.** Convert both quantities to base units, multiply, then apply the
most natural prefix. Estimate first.

**Solution.**

Step 1 — Convert to base units.

$$4.7 \text{ k}\Omega = 4.7 \times 10^3 \; \Omega$$
$$250 \text{ µA} = 250 \times 10^{-6} \text{ A} = 2.50 \times 10^{-4} \text{ A}$$

Step 2 — Estimate. Roughly $5 \times 10^3$ times $2.5 \times 10^{-4}$, which
is about $12 \times 10^{-1} \approx 1$. Expect something near 1 volt.

Step 3 — Compute.

$$V = (4.7 \times 10^3)(2.50 \times 10^{-4})$$

Mantissas: $4.7 \times 2.50 = 11.75$. Exponents: $3 + (-4) = -1$.

$$V = 11.75 \times 10^{-1} \text{ V}$$

Step 4 — Renormalize, then round to three significant figures.

$$11.75 \times 10^{-1} \text{ V} = 1.175 \text{ V} \;\rightarrow\; \boxed{1.18 \text{ V}}$$

**Check.** Estimate said "near 1 volt"; we got 1.18 V. ✓

Alternative check using prefix arithmetic directly: kilo times micro is
$10^3 \times 10^{-6} = 10^{-3}$, which is milli. So $4.7 \times 250 = 1{,}175$
in millivolts, which is $1{,}175 \text{ mV} = 1.175 \text{ V} \rightarrow
1.18 \text{ V}$. ✓ Same answer by a different route, rounded the same way at
the same point.

That second method is worth learning. **Prefix pairs combine predictably:**

| Product | Net power | Net prefix |
|---|---|---|
| kilo × milli | $10^3 \times 10^{-3} = 10^0$ | none |
| kilo × micro | $10^3 \times 10^{-6} = 10^{-3}$ | milli |
| mega × micro | $10^6 \times 10^{-6} = 10^0$ | none |
| mega × nano | $10^6 \times 10^{-9} = 10^{-3}$ | milli |
| kilo ÷ milli | $10^3 \div 10^{-3} = 10^6$ | mega |

### Worked Example 7 — Squared and Cubed Prefixes

**Given.** A rectangular duct measures $450 \text{ mm}$ by $300 \text{ mm}$.

**Find.** (a) The cross-sectional area in m². (b) If air flows through at an
average velocity of $8.5 \text{ m/s}$, the volumetric flow rate in m³/s and
in L/s. Note that $1 \text{ m}^3 = 1{,}000 \text{ L}$.

**Solution.**

(a) Step 1 — Convert dimensions to metres.

$$450 \text{ mm} = 0.450 \text{ m}$$
$$300 \text{ mm} = 0.300 \text{ m}$$

Step 2 — Area.

$$A = (0.450)(0.300) = 0.135 \text{ m}^2$$

Cross-check via the squared prefix. In mm²:

$$A = (450)(300) = 135{,}000 \text{ mm}^2$$

$$135{,}000 \text{ mm}^2 \times \frac{10^{-6} \text{ m}^2}{1 \text{ mm}^2} = 0.135 \text{ m}^2 \;\checkmark$$

Both routes agree, confirming the $10^{-6}$ factor.

![FIG-01-01-004: Three stacked panels showing a 1 mm length beside a 1 m length, then a 1 mm square inside a 1 m square, then a 1 mm cube inside a 1 m cube — each panel annotated with the corresponding factor of ten to the minus three, minus six, and minus nine, making visible that the prefix exponent multiplies by the power](../figures/FIG-01-01-004-squared-cubed-prefix.png)

(b) Step 3 — Volumetric flow rate.

$$Q_v = A \times v = (0.135 \text{ m}^2)(8.5 \text{ m/s}) = 1.1475 \text{ m}^3/\text{s}$$

Step 4 — Convert to litres per second, carrying full precision.

$$1.1475 \frac{\text{m}^3}{\text{s}} \times \frac{1{,}000 \text{ L}}{1 \text{ m}^3} = 1{,}147.5 \text{ L/s}$$

Step 5 — Round both forms to three significant figures, the precision of the
given velocity.

$$\boxed{Q_v = 1.15 \text{ m}^3/\text{s} = 1.15 \times 10^3 \text{ L/s} = 1{,}150 \text{ L/s}}$$

**Check.** Dimensional reasoning: area (m²) times velocity (m/s) gives m³/s.
✓ Magnitude: a duct roughly half a metre square, with air moving at about
8 m/s, moving about one cubic metre per second — that's physically sensible.
✓ Both reported forms carry three significant figures, so they describe the
same quantity at the same precision. ✓

**Where this would go wrong.** Using $10^{-3}$ instead of $10^{-6}$ for the
mm²-to-m² conversion gives $135 \text{ m}^2$ — a duct the size of a tennis
court. The magnitude is absurd, and that absurdity is your protection. But
notice that the *arithmetic* was flawless. Nothing in the calculation would
have flagged the error. Only asking "is a duct that size physically
reasonable?" catches it.

> ---
> **Mentor's Margin**
>
> This is why I insist on the Check step in every single worked example. Not
> because I think you can't multiply. Because the errors that survive careful
> arithmetic are exactly the errors that arithmetic can't catch. The only
> defense is a habit of asking whether the answer makes physical sense.
>
> ---

---

## Where This Goes Wrong

The specific failures that cost exam points on this material.

**Case error on the prefix symbol.** `M` is mega, $10^6$. `m` is milli,
$10^{-3}$. A factor of $10^9$ between them. Write your prefixes carefully on
scratch paper — this error is nearly invisible once it's on the page.

**Squared and cubed prefixes.** $1 \text{ mm}^2 = 10^{-6} \text{ m}^2$, not
$10^{-3}$. $1 \text{ mm}^3 = 10^{-9} \text{ m}^3$. The prefix exponent gets
multiplied by the power. Every area and volume conversion is a place this can
bite you, and area conversions appear constantly in stress, pressure, and
flow problems.

**Adding without matching exponents.** $3 \times 10^5 + 4 \times 10^4$ is
$3.4 \times 10^5$, not $7 \times 10^5$. Multiplication lets you combine
exponents freely; addition does not. Match first, then add.

**Converting in the wrong direction.** Nobody miscounts three decimal places.
Everybody occasionally counts them backwards. The fix is mechanical: after
every conversion, take the result back to base units and confirm you land
where you started.

**Calculator exponent entry.** Pressing `× 10` before the exponent key gives
an answer ten times too large. Use the `EE` / `EXP` / `×10ˣ` key alone.
Verify your calculator's behavior once, deliberately, with a known value.

**Missing parentheses on a fraction.** A fraction bar groups its entire
numerator and its entire denominator. Transcribing $\frac{a+b}{c+d}$ as
`a + b / c + d` computes something else. Parenthesize both, always.

**Sign errors in exponent arithmetic.** Subtracting a negative exponent adds.
$-3 - (-6) = +3$. This one produces answers wrong by many orders of magnitude
and it happens under time pressure.

**Rounding $\pi$ early.** Use the calculator's $\pi$ key. Truncating to 3.14
at step one of a five-step calculation compounds the error through every
subsequent step.

**Forgetting to renormalize.** $15 \times 10^{-9}$ is a correct value but not
proper scientific notation. It's $1.5 \times 10^{-8}$. On a fill-in-the-blank
question where the expected form matters, this can cost you.

**Skipping the estimate.** Fifteen seconds of one-significant-figure
estimation before you compute catches every prefix and decimal error you
would otherwise ship. It is the highest return on time investment available
anywhere in this exam.

---

## Key Terms

| Term | Definition |
|---|---|
| Integer | A whole number: positive, negative, or zero |
| Rational number | A number expressible as a ratio of two integers |
| Irrational number | A real number not expressible as a ratio of integers; never terminates or repeats |
| Real number | Any rational or irrational number |
| Absolute value | The magnitude of a number without regard to sign |
| Order of operations | Parentheses, exponents, multiplication and division left to right, addition and subtraction left to right |
| Scientific notation | A number written as $N \times 10^x$ with $1 \le \lvert N \rvert < 10$ |
| Mantissa | The coefficient $N$ in scientific notation |
| Exponent | The power of ten $x$ in scientific notation |
| Matching exponents | Rewriting one term of a sum so both terms share the same power of ten, which is required before adding or subtracting |
| Renormalize | Adjust a mantissa back into the range $1 \le \lvert N \rvert < 10$ after arithmetic |
| Order of magnitude | The nearest power of ten to a quantity's size; used for estimation and error checking |
| Engineering notation | Scientific notation restricted to exponents that are multiples of three |
| SI prefix | A standardized multiplier symbol such as k, M, m, or µ |
| Squared prefix | A prefix applied to a squared unit; its power of ten is doubled |

---

## Review Questions

### Conceptual

1. Is every terminating decimal a rational number? Is every rational number a
   terminating decimal? Justify both answers with an example, and state the
   practical consequence for how you handle $\pi$ in a multi-step
   calculation.
2. Why does engineering use scientific notation instead of writing numbers
   out in full? Give a specific example from the quantities named in this
   chapter.
3. Explain the reasoning behind the direction rule for scientific notation:
   why does moving the decimal point left produce a *larger* exponent?
4. Why is a fraction bar considered a grouping symbol? What goes wrong if you
   ignore that when using a calculator?
5. Why must exponents match before you add two numbers in scientific
   notation, when no such requirement applies to multiplying them?
6. Explain why $1 \text{ mm}^2$ equals $10^{-6} \text{ m}^2$ rather than
   $10^{-3} \text{ m}^2$. State the general rule for a prefix raised to a
   power.
7. When converting from a smaller prefix to a larger one, does the numeric
   value get larger or smaller? Justify your answer using the physical
   quantity rather than the rule.
8. The metric prefixes are printed in the Handbook. Give the argument for
   memorizing them anyway, in terms of exam time.
9. Scientific notation, order of operations, and orders of magnitude are
   *not* in the Handbook. What does that fact obligate you to do, and what
   does it tell you about how NCEES thinks about this material?
10. Explain how an order-of-magnitude estimate protects you from an error that
    careful arithmetic cannot catch. Use the duct example from Worked
    Example 7.
11. `M` and `m` differ by what factor? Why is this the most dangerous
    notation error in the entire chapter?

### Calculation

12. Classify each number as integer, rational, irrational, and/or real. List
    every category that applies.
    (a) $-7$
    (b) $0.625$
    (c) $\sqrt{9}$
    (d) $\pi$
    (e) $\tfrac{2}{3}$
    (f) $e$

13. Convert each to scientific notation:
    (a) $186{,}000$
    (b) $0.00000725$
    (c) $47{,}000{,}000{,}000$
    (d) $-0.0034$
    (e) $9.807$

14. Convert each to decimal form:
    (a) $6.02 \times 10^{23}$
    (b) $1.6 \times 10^{-19}$
    (c) $3.25 \times 10^4$
    (d) $8 \times 10^{-1}$

15. Evaluate, expressing each answer in proper scientific notation:
    (a) $(6 \times 10^4)(3 \times 10^{-7})$
    (b) $\dfrac{9.6 \times 10^{-5}}{1.2 \times 10^{-8}}$
    (c) $(2.5 \times 10^{-3})(4.0 \times 10^{-4})$
    (d) $\dfrac{4.2 \times 10^{6}}{7.0 \times 10^{9}}$

16. Evaluate, expressing each answer in proper scientific notation:
    (a) $5 \times 10^6 + 3 \times 10^5$
    (b) $7.5 \times 10^{-4} - 2.5 \times 10^{-5}$
    (c) $8.0 \times 10^3 + 9.0 \times 10^3$
    (d) $2.2 \times 10^{-6} + 470 \times 10^{-9}$

17. Evaluate, applying the order of operations correctly:
    (a) $\dfrac{7 + 3 \times 2^3}{8 - 6}$
    (b) $24 \div 6 \times 2$
    (c) $5 + 2(9 - 3^2)$
    (d) $\dfrac{(4 + 2)^2}{3 \times 4 - 6}$

18. Express each with the most natural single prefix:
    (a) $0.00047$ F
    (b) $8{,}200{,}000$ Ω
    (c) $0.000000015$ s
    (d) $3{,}400$ N
    (e) $0.025$ m

19. Convert as directed:
    (a) $2.2$ MΩ to kΩ
    (b) $0.68$ µF to pF
    (c) $450$ mm to µm
    (d) $12$ GPa to MPa
    (e) $7{,}500$ nF to µF

20. A rectangular steel bar has a cross section $25 \text{ mm}$ by
    $60 \text{ mm}$ and carries an axial tensile load of $180 \text{ kN}$.
    (a) Before computing anything, estimate the axial stress to one
    significant figure.
    (b) Find the cross-sectional area in m².
    (c) Find the axial stress in Pa.
    (d) Express the stress in MPa, and state whether it agrees with your
    estimate from (a).

21. A capacitor of $220 \text{ nF}$ is charged to $50 \text{ V}$. The stored
    charge is the product of capacitance and voltage.
    (a) Find the charge in coulombs, in scientific notation.
    (b) Express it with the most natural prefix.

22. A circular pipe has an inside diameter of $150 \text{ mm}$. Water flows
    through it at an average velocity of $2.4 \text{ m/s}$. The area of a
    circle is $\pi D^2 / 4$.
    (a) Find the cross-sectional area in m².
    (b) Find the volumetric flow rate in m³/s.
    (c) Convert to L/s, given $1 \text{ m}^3 = 1{,}000 \text{ L}$.
    (d) Check your answer for physical reasonableness.

23. State the order of magnitude of each:
    (a) $4.7 \times 10^{-8}$
    (b) $8.9 \times 10^{5}$
    (c) $0.00023$
    (d) $62{,}400$

### Multiple Choice

24. The number $0.00000082$ written in scientific notation is:
    A) $8.2 \times 10^{-6}$
    B) $8.2 \times 10^{-7}$
    C) $82 \times 10^{-8}$
    D) $0.82 \times 10^{-6}$

25. The SI prefix "pico" represents a multiplier of:
    A) $10^{-6}$
    B) $10^{-9}$
    C) $10^{-12}$
    D) $10^{-15}$

26. The quantity $1 \text{ mm}^3$ is equal to:
    A) $10^{-3} \text{ m}^3$
    B) $10^{-6} \text{ m}^3$
    C) $10^{-9} \text{ m}^3$
    D) $10^{-12} \text{ m}^3$

27. Evaluate $18 \div 3 \times 2$:
    A) $3$
    B) $12$
    C) $27$
    D) $108$

28. The product $(5 \times 10^{-4})(6 \times 10^{-3})$ equals:
    A) $3.0 \times 10^{-6}$
    B) $3.0 \times 10^{-7}$
    C) $30 \times 10^{-7}$
    D) $1.1 \times 10^{-6}$

29. A resistance of $4{,}700{,}000 \; \Omega$ is most naturally written as:
    A) $4{,}700 \text{ k}\Omega$
    B) $4.7 \text{ M}\Omega$
    C) $0.0047 \text{ G}\Omega$
    D) $47 \times 10^5 \; \Omega$

30. Which of the following prefixes uses a capital letter as its symbol?
    A) kilo
    B) milli
    C) mega
    D) nano

31. A quantity is converted from micro to nano. The numeric value:
    A) Increases by a factor of 1,000
    B) Decreases by a factor of 1,000
    C) Increases by a factor of 1,000,000
    D) Remains unchanged

32. Which of these expressions is a correct calculator entry for
    $\dfrac{a+b}{c+d}$?
    A) `a + b / c + d`
    B) `(a + b) / c + d`
    C) `a + b / (c + d)`
    D) `(a + b) / (c + d)`

33. Engineering notation differs from scientific notation in that:
    A) The mantissa must be between 1 and 10
    B) The exponent must be a multiple of three
    C) Negative exponents are not permitted
    D) The mantissa must be an integer

34. Which of the following numbers is irrational?
    A) $0.25$
    B) $\tfrac{22}{7}$
    C) $\sqrt{2}$
    D) $-3$

35. The sum $3 \times 10^5 + 4 \times 10^4$ equals:
    A) $7 \times 10^5$
    B) $7 \times 10^9$
    C) $3.4 \times 10^5$
    D) $1.2 \times 10^{10}$

---

## Answer Key with Explanations

**1.** Yes to the first, no to the second. Every terminating decimal is
rational — $0.625 = \tfrac{5}{8}$ — and so is every *repeating* decimal.
But not every rational number terminates: $\tfrac{1}{3} = 0.\overline{3}$
runs forever. What distinguishes an irrational number is that it neither
terminates nor repeats, which is the case for $\pi$. Practical consequence:
$\pi$ can never be entered exactly, so any decimal you type is already an
approximation. Carry it at full calculator precision using the $\pi$ key and
round once, at the end. Truncating to 3.14 at step one of a multi-step
calculation propagates that error through every subsequent step. (§1.1)

**2.** Because engineering quantities span roughly thirty orders of magnitude,
and writing long strings of zeros invites transcription error while
communicating nothing. Example from this chapter: the elastic modulus of
steel is about $2 \times 10^{11}$ Pa, which written out is 200,000,000,000 Pa
— eleven zeros nobody can reliably count. Scientific notation makes the
magnitude explicit in a single digit. (§1.3)

**3.** Because the value of the number doesn't change — only its
representation. Moving the decimal left makes the mantissa *smaller*, so the
exponent must grow *larger* to compensate and preserve the product. Small
mantissa, big exponent. Understanding it this way removes the need to
memorize a direction. (§1.3)

**4.** Because everything above the bar is implicitly parenthesized, and so
is everything below it. Ignoring that on a calculator means
$\frac{a+b}{c+d}$ gets computed as $a + \frac{b}{c} + d$, which is a
different quantity entirely. The fix is to parenthesize the whole numerator
and the whole denominator, every time. (§1.2)

**5.** Because multiplication and addition treat the power of ten
differently. In a product, the laws of exponents let you combine
$10^{x_1} \times 10^{x_2}$ into $10^{x_1 + x_2}$ regardless of the two
exponents. In a sum, $10^x$ can only be factored out front if *both* terms
carry the same $10^x$ — otherwise there is no common factor and the mantissas
aren't like terms. The familiar version of this rule is unit conversion: you
wouldn't add 5 kΩ and 300 Ω and report 305 of anything. Matching exponents is
the same operation as converting to a common unit. (§1.3)

**6.** Because the prefix is inside the squaring operation. $1 \text{ mm} =
10^{-3} \text{ m}$, so $1 \text{ mm}^2 = (10^{-3} \text{ m})^2 = 10^{-6}
\text{ m}^2$. **General rule: when a prefixed unit is raised to a power, the
prefix's exponent is multiplied by that power.** Cubed prefixes triple:
$1 \text{ mm}^3 = 10^{-9} \text{ m}^3$. (§1.4, §1.5)

**7.** The numeric value gets **smaller**. Justification from the physical
quantity: the quantity itself is unchanged, but a larger unit means you need
fewer of them to express the same amount. 4,700 ohms is 4.7 kilohms because a
kilohm is a bigger unit than an ohm. (§1.5)

**8.** A Handbook lookup costs fifteen to twenty seconds. Prefixes appear on a
large fraction of exam questions — say forty of them. At twenty seconds each
that's about thirteen minutes, or roughly four and a half questions' worth of
working time, spent retrieving something you could have known cold. **Look up
what you use rarely; memorize what you use constantly.** (§As the Handbook
States It, 00-03 §0.2)

**9.** It obligates you to know that material cold, because there is no page
to turn to. What it tells you about NCEES's thinking: these are exactly the
"basic theories, conversions, formulas, and definitions examinees are
expected to know" that the Handbook's introduction says have been
deliberately omitted. The omission is a statement that this material is
considered prerequisite to engineering, not part of engineering reference.
(§As the Handbook States It, 00-03 §0.2)

**10.** In Worked Example 7, using $10^{-3}$ instead of $10^{-6}$ for the
mm²-to-m² conversion produces a duct cross section of $135 \text{ m}^2$ —
about the area of a tennis court. The *arithmetic in that calculation is
flawless*; nothing internal to the computation flags the error. Only asking
whether a duct of that size is physically plausible catches it. An
order-of-magnitude estimate made before computing gives you an independent
expectation to compare against, which is the only mechanism that detects this
class of error. (§1.4, Worked Example 7)

**11.** They differ by a factor of $10^9$: `M` is mega ($10^6$) and `m` is
milli ($10^{-3}$), so $10^6 / 10^{-3} = 10^9$. It's the most dangerous error
because it is nearly invisible once written — a hurried capital and a
lowercase letter look similar on scratch paper, the resulting number looks
perfectly reasonable, and there is no arithmetic check that will catch it.
(§1.5)

**12.**
(a) $-7$ — integer, rational, real
(b) $0.625$ — rational, real (it equals $\tfrac{5}{8}$)
(c) $\sqrt{9} = 3$ — integer, rational, real
(d) $\pi$ — irrational, real
(e) $\tfrac{2}{3}$ — rational, real
(f) $e$ — irrational, real

Part (c) is the trap. A square root sign doesn't make a number irrational;
$\sqrt{9}$ is just 3. It's $\sqrt{2}$ that's irrational, because 2 isn't a
perfect square. Note also that every entry on this list is real — the
categories nest rather than compete. (§1.1)

**13.**
(a) $186{,}000 = 1.86 \times 10^5$
(b) $0.00000725 = 7.25 \times 10^{-6}$
(c) $47{,}000{,}000{,}000 = 4.7 \times 10^{10}$
(d) $-0.0034 = -3.4 \times 10^{-3}$
(e) $9.807 = 9.807 \times 10^0$

Part (e) is a legitimate test: a number already between 1 and 10 has exponent
zero. Writing $9.807 \times 10^0$ is correct, though in practice you'd just
write 9.807.

**14.**
(a) $6.02 \times 10^{23} = 602{,}000{,}000{,}000{,}000{,}000{,}000{,}000$
(b) $1.6 \times 10^{-19} = 0.00000000000000000016$
(c) $3.25 \times 10^4 = 32{,}500$
(d) $8 \times 10^{-1} = 0.8$

**15.**

(a) Mantissas: $6 \times 3 = 18$. Exponents: $4 + (-7) = -3$.
$18 \times 10^{-3}$, renormalize → $\boxed{1.8 \times 10^{-2}}$

(b) Mantissas: $9.6 \div 1.2 = 8.0$. Exponents: $-5 - (-8) = -5 + 8 = 3$.
$\boxed{8.0 \times 10^3}$

*Note the sign handling.* Subtracting $-8$ adds 8.

(c) Mantissas: $2.5 \times 4.0 = 10.0$. Exponents: $-3 + (-4) = -7$.
$10.0 \times 10^{-7}$, renormalize → $\boxed{1.0 \times 10^{-6}}$

(d) Mantissas: $4.2 \div 7.0 = 0.60$. Exponents: $6 - 9 = -3$.
$0.60 \times 10^{-3}$, renormalize → $\boxed{6.0 \times 10^{-4}}$

*Check (d) by decimal:* $4{,}200{,}000 \div 7{,}000{,}000{,}000 = 0.0006 =
6.0 \times 10^{-4}$ ✓

**16.**

(a) Match exponents: $3 \times 10^5 = 0.3 \times 10^6$.

$$5 + 0.3 = 5.3 \;\rightarrow\; \boxed{5.3 \times 10^6}$$

*Check:* $5{,}000{,}000 + 300{,}000 = 5{,}300{,}000$ ✓

(b) Match exponents: $2.5 \times 10^{-5} = 0.25 \times 10^{-4}$.

$$7.5 - 0.25 = 7.25 \;\rightarrow\; \boxed{7.25 \times 10^{-4}}$$

*Check:* $0.00075 - 0.000025 = 0.000725$ ✓

(c) Exponents already match.

$$8.0 + 9.0 = 17.0 \;\rightarrow\; 17.0 \times 10^3 \;\rightarrow\; \boxed{1.70 \times 10^4}$$

*Check:* $8{,}000 + 9{,}000 = 17{,}000$ ✓ Renormalization required, even
though nothing was multiplied.

(d) The second term isn't in proper scientific notation to begin with, which
is a hint about the intended route. Match to $10^{-6}$:
$470 \times 10^{-9} = 0.47 \times 10^{-6}$.

$$2.2 + 0.47 = 2.67 \;\rightarrow\; \boxed{2.67 \times 10^{-6}}$$

*Check:* $0.0000022 + 0.00000047 = 0.00000267$ ✓

Read in prefixes, part (d) says 2.2 µF plus 470 nF is 2.67 µF — which is
exactly the kΩ-plus-Ω reasoning from §1.3, wearing different units.

**17.**

(a) Numerator: $2^3 = 8$, then $3 \times 8 = 24$, then $7 + 24 = 31$.
Denominator: $8 - 6 = 2$.

$$\frac{31}{2} = \boxed{15.5}$$

(b) Equal precedence, left to right: $24 \div 6 = 4$, then $4 \times 2 =
\boxed{8}$

Not 2. Division does not bind tighter than multiplication.

(c) Inside the parentheses first, and *inside* that, the exponent:
$3^2 = 9$, so $9 - 9 = 0$. Then $2(0) = 0$, then $5 + 0 = \boxed{5}$

(d) Numerator: $(4+2)^2 = 6^2 = 36$. Denominator: $3 \times 4 = 12$, then
$12 - 6 = 6$.

$$\frac{36}{6} = \boxed{6}$$

**18.**
(a) $0.00047 \text{ F} = 4.7 \times 10^{-4} \text{ F} = 470 \times 10^{-6}
\text{ F} = \boxed{470 \text{ µF}}$
(b) $8{,}200{,}000 \; \Omega = 8.2 \times 10^6 \; \Omega = \boxed{8.2
\text{ M}\Omega}$
(c) $0.000000015 \text{ s} = 1.5 \times 10^{-8} \text{ s} = 15 \times
10^{-9} \text{ s} = \boxed{15 \text{ ns}}$
(d) $3{,}400 \text{ N} = 3.4 \times 10^3 \text{ N} = \boxed{3.4 \text{ kN}}$
(e) $0.025 \text{ m} = 25 \times 10^{-3} \text{ m} = \boxed{25 \text{ mm}}$

Parts (a) and (c) require engineering notation as an intermediate step,
because the scientific-notation exponent isn't a multiple of three.

**19.**
(a) Mega to kilo: from $10^6$ to $10^3$, a smaller prefix, so the number gets
larger. Shift 3 right: $\boxed{2{,}200 \text{ k}\Omega}$
(b) Micro to pico: from $10^{-6}$ to $10^{-12}$, six steps smaller. Shift 6
right: $\boxed{680{,}000 \text{ pF}}$
(c) Milli to micro: three steps smaller. Shift 3 right: $\boxed{450{,}000
\text{ µm}}$
(d) Giga to mega: three steps smaller. Shift 3 right: $\boxed{12{,}000
\text{ MPa}}$
(e) Nano to micro: from $10^{-9}$ to $10^{-6}$, a *larger* prefix, so the
number gets smaller. Shift 3 left: $\boxed{7.5 \text{ µF}}$

*Check (e) in base units:* $7.5 \text{ µF} = 7.5 \times 10^{-6} \text{ F} =
7{,}500 \times 10^{-9} \text{ F} = 7{,}500 \text{ nF}$ ✓

**20.**

(a) **Estimate first.** Load $\approx 2 \times 10^5$ N. Area: $25 \times 60 =
1{,}500 \text{ mm}^2$, and $1{,}500 \times 10^{-6} \approx 1.5 \times 10^{-3}
\text{ m}^2$. Ratio:

$$\frac{2 \times 10^5}{1.5 \times 10^{-3}} \approx 1.3 \times 10^8 \text{ Pa}$$

Expect roughly $10^8$ Pa, so a little over 100 MPa.

(b) Convert dimensions: $25 \text{ mm} = 0.025 \text{ m}$, $60 \text{ mm} =
0.060 \text{ m}$.

$$A = (0.025)(0.060) = 1.5 \times 10^{-3} \text{ m}^2$$

*Cross-check via the squared prefix:* $A = 25 \times 60 = 1{,}500 \text{
mm}^2$, and $1{,}500 \times 10^{-6} = 1.5 \times 10^{-3} \text{ m}^2$ ✓

(c) $180 \text{ kN} = 1.80 \times 10^5 \text{ N}$

$$\sigma = \frac{1.80 \times 10^5 \text{ N}}{1.5 \times 10^{-3} \text{ m}^2} = 1.20 \times 10^8 \text{ Pa}$$

(d) $1.20 \times 10^8 \text{ Pa} = 120 \times 10^6 \text{ Pa} = \boxed{120
\text{ MPa}}$

**Agreement:** computed $1.20 \times 10^8$ against the estimate $1.3 \times
10^8$ from part (a). Same order of magnitude, and the estimate ran slightly
high because the load was rounded up. ✓ Independent physical check: 120 MPa
is a plausible working stress for structural steel, which yields in the
vicinity of 250 MPa. ✓

**21.**

(a) $220 \text{ nF} = 2.20 \times 10^{-7} \text{ F}$

$$Q = CV = (2.20 \times 10^{-7})(50) = (2.20 \times 10^{-7})(5.0 \times 10^1)$$

Mantissas: $2.20 \times 5.0 = 11.0$. Exponents: $-7 + 1 = -6$.

$$Q = 11.0 \times 10^{-6} \text{ C} = \boxed{1.10 \times 10^{-5} \text{ C}}$$

(b) $1.10 \times 10^{-5} \text{ C} = 11.0 \times 10^{-6} \text{ C} =
\boxed{11.0 \text{ µC}}$

*Check via the prefix-pair method:* nano times no prefix is nano, so
$220 \times 50 = 11{,}000$ in nanocoulombs, which is $11{,}000 \text{ nC} =
11.0 \text{ µC}$ ✓

**22.**

(a) $D = 150 \text{ mm} = 0.150 \text{ m}$

$$A = \frac{\pi D^2}{4} = \frac{\pi (0.150)^2}{4} = \frac{\pi (0.0225)}{4} = \frac{0.070686}{4} = 1.767 \times 10^{-2} \text{ m}^2$$

(b)

$$Q_v = Av = (1.767 \times 10^{-2})(2.4) = 4.241 \times 10^{-2} \text{ m}^3/\text{s}$$

Three significant figures: $\boxed{4.24 \times 10^{-2} \text{ m}^3/\text{s}}$

(c)

$$4.241 \times 10^{-2} \frac{\text{m}^3}{\text{s}} \times \frac{1{,}000 \text{ L}}{1 \text{ m}^3} = \boxed{42.4 \text{ L/s}}$$

(d) **Physical check.** A 150 mm pipe is roughly a 6-inch water main. Water at
2.4 m/s is a normal design velocity for such a line — municipal systems
typically run somewhere in the 1 to 3 m/s range. And 42.4 L/s works out to
about 670 gallons per minute, a sensible flow for a 6-inch main. Everything
reconciles. ✓

*Note:* $\pi$ was carried at full calculator precision and rounded only at
the end. Truncating to 3.14 at the start would have shifted the result
slightly — not enough to matter here, but the habit matters when a
calculation runs longer.

**23.**
(a) $4.7 \times 10^{-8}$: mantissa above 3, round up → $\boxed{10^{-7}}$
(b) $8.9 \times 10^{5}$: mantissa above 3, round up → $\boxed{10^{6}}$
(c) $0.00023 = 2.3 \times 10^{-4}$: mantissa below 3 → $\boxed{10^{-4}}$
(d) $62{,}400 = 6.24 \times 10^4$: mantissa above 3, round up →
$\boxed{10^{5}}$

Don't agonize over the boundary. The tool is deliberately crude, and its
whole purpose is to be fast.

**24. B — $8.2 \times 10^{-7}$.** Count the decimal moves: from $0.00000082$
to $8.2$ requires seven places right, giving exponent $-7$. (A) has the wrong
count by one, which is the error you'd make rushing. (C) and (D) both carry
the *correct value* but improper mantissas — 82 and 0.82 fall outside
$1 \le \lvert N \rvert < 10$ — and on a question that asks for scientific
notation specifically, form is what's being tested. (§1.3)

**25. C — $10^{-12}$.** Micro is $10^{-6}$, nano is $10^{-9}$, pico is
$10^{-12}$, femto is $10^{-15}$. Every distractor here is a real prefix one
or two rungs away, which is exactly how a recall question on an ordered
table gets built. (§1.5)

**26. C — $10^{-9} \text{ m}^3$.** The prefix exponent multiplies by the
power: $(10^{-3})^3 = 10^{-9}$. (A) treats the prefix as unaffected by
cubing, which is the error itself. (B) is the *squared* conversion, and it's
the most tempting wrong answer because $10^{-6}$ is correct for mm² and gets
misremembered as the general prefix-to-power factor. (D) doubles the cube.
(§1.4, §1.5)

**27. B — 12.** $18 \div 3 = 6$, then $6 \times 2 = 12$, left to right. (A)
results from evaluating $3 \times 2$ first, giving $18 \div 6 = 3$, which
incorrectly treats multiplication as binding tighter than division — they
have equal precedence. (C) multiplies everything, (D) is $18 \times 3 \times
2$. (§1.2)

**28. A — $3.0 \times 10^{-6}$.** Mantissas: $5 \times 6 = 30$. Exponents:
$-4 + (-3) = -7$. That gives $30 \times 10^{-7}$, which renormalizes to
$3.0 \times 10^{-6}$. (C) is that same value left unrenormalized, so it's
numerically right and formally wrong — the distractor exists to catch exactly
that. (B) forgets to renormalize *and* keeps the mantissa at 3, and (D) is
arithmetic noise. (§1.3)

**29. B — $4.7 \text{ M}\Omega$.** All four choices are numerically equal;
the question asks which is *most natural*. Engineering convention puts the
mantissa between 1 and 1000, which 4.7 satisfies. (A) at 4,700 and (C) at
0.0047 are both legal but awkward, and (D) isn't engineering notation at all
since $10^5$ is not a multiple of three. (§1.5)

**30. C — mega.** Prefixes for $10^6$ and above use capitals: M, G, T, P, E.
Below that, lowercase — with kilo as the notable exception, using lowercase
`k` despite being $10^3$, which is why (A) is the distractor most people
hesitate over. (§1.5)

**31. A — increases by a factor of 1,000.** Nano ($10^{-9}$) is a *smaller*
unit than micro ($10^{-6}$), so you need more of them: the numeric value
grows. (B) inverts the direction, which is the single most common prefix
error. (C) applies six steps instead of three. (§1.5)

**32. D — `(a + b) / (c + d)`.** The fraction bar groups the entire numerator
and the entire denominator, so both need parentheses. (A) computes
$a + \frac{b}{c} + d$. (B) and (C) each parenthesize one side and leave the
other exposed, which is the half-remembered version of the habit and still
gives a wrong answer. (§1.2)

**33. B — the exponent must be a multiple of three.** That's what makes every
value map onto a prefix. (A) describes *scientific* notation, so it's the
right statement about the wrong form — in engineering notation the mantissa
runs from 1 up to 1000. (C) is false: $680$ pF is $680 \times 10^{-12}$. (D)
is false: $4.7$ kΩ. (§1.5)

**34. C — $\sqrt{2}$.** Irrational: it neither terminates nor repeats. (A) is
$\tfrac{1}{4}$. (B) is the classic trap — $\tfrac{22}{7}$ is a rational
*approximation* to $\pi$, and being a ratio of two integers is precisely what
makes it rational no matter what it approximates. (D) is an integer, hence
rational. (§1.1)

**35. C — $3.4 \times 10^5$.** Match exponents first: $4 \times 10^4 =
0.4 \times 10^5$, then $3 + 0.4 = 3.4$. (A) adds the mantissas without
matching, which is the error this question exists to catch, and it's wrong by
roughly a factor of two. (B) adds the exponents as though the terms were
being multiplied. (D) does both wrong things at once. (§1.3)

---

## Quick Reference

**Scientific notation**

$$N \times 10^x, \qquad 1 \le \lvert N \rvert < 10$$

Decimal left → exponent up. Decimal right → exponent down. Small mantissa,
big exponent.

| Operation | Mantissas | Exponents |
|---|---|---|
| Multiply | multiply | **add** |
| Divide | divide | **subtract** |
| Add / subtract | add / subtract | **must already match** |

Renormalize whenever the mantissa leaves $1 \le \lvert N \rvert < 10$ — after
sums as well as products.

**Metric prefixes — memorize these eight**

| T | G | M | k | m | µ | n | p |
|---|---|---|---|---|---|---|---|
| $10^{12}$ | $10^{9}$ | $10^{6}$ | $10^{3}$ | $10^{-3}$ | $10^{-6}$ | $10^{-9}$ | $10^{-12}$ |

Capitals at $10^6$ and above; lowercase below; kilo is lowercase `k`. `M` and
`m` differ by $10^9$.

Full table: Handbook p. 1. Memorize anyway — the lookup costs more than the
knowledge.

**Engineering notation**

Exponent restricted to multiples of three, so every value maps onto a prefix.
Mantissa runs 1 to 1000. Use your calculator's ENG display mode.

**Prefix conversion**

Larger prefix → smaller number. Smaller prefix → larger number. The quantity
doesn't change; a bigger unit means you need fewer of them.

**Always verify by returning to base units.**

**Powers of prefixed units**

$$1 \text{ mm}^2 = 10^{-6} \text{ m}^2 \qquad 1 \text{ mm}^3 = 10^{-9} \text{ m}^3$$

The prefix exponent multiplies by the power. Squared doubles, cubed triples.

**Order of operations**

Parentheses → exponents → multiply/divide left to right → add/subtract left
to right. Multiplication and division have **equal** precedence. A fraction
bar groups both the whole numerator and the whole denominator:
`(a + b) / (c + d)`.

**Order of magnitude**

Nearest power of ten. Mantissa below ~3 → keep the exponent; above → round
up.

**Estimate to one significant figure before you compute.** Off by 1000 → a
prefix error. Off by 10 → a decimal error.

**Reference magnitudes worth carrying**

| Quantity | Magnitude |
|---|---|
| Atmospheric pressure | ~100 kPa |
| Concrete compressive strength | tens of MPa |
| Structural steel yield | ~250 MPa |
| Steel elastic modulus | ~200 GPa |
| Standard gravity | 9.807 m/s² |

**Calculator discipline**

`EE` / `EXP` / `×10ˣ` alone, never `× 10` first. Use the $\pi$ key. Round
once, at the end. Parenthesize every transcribed fraction.

---

## What's Next

Apprentice, you now have the bookkeeping system. Thirty orders of magnitude,
and you can move across all of them without dropping a factor of a thousand.
That isn't engineering yet — but every piece of engineering that follows sits
on top of it, and the errors it prevents are the ones that would otherwise
have survived every check you know how to run.

Notice what you actually built here. Not new mathematics. A set of habits:
estimate before you compute, renormalize before you report, verify a
conversion by going back to base units, and ask whether the number is
physically ridiculous before you write it down. Those four habits will catch
more exam errors than any formula in this guide.

In **Chapter 01-02: Units, Dimensions, and the Pound-Mass Problem**, we take
on the single highest-leverage topic in the entire foundation. You'll learn
what a base unit is and what a derived unit is, how to convert anything into
anything with the factor-label method, and then the thing the Handbook puts
on its very first page and this chapter has twice pointed at and declined to
explain: what pound-mass and pound-force actually are, why they aren't the
same thing, and why customary-unit mechanics needs a conversion constant
that SI does not.

That distinction costs more exam points than any other topic in Layer 1. We
are going to make it permanent.

Bring your calculator. Bring the Handbook, still open to page 1.

See you there.

— Your Mentor