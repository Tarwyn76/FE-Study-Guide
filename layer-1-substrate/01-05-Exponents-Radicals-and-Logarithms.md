---
chapter: "01-05"
title: "Exponents, Radicals, and Logarithms"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-005-01, MATH-1B-005-02, MATH-1B-005-03]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-05: Exponents, Radicals, and Logarithms

> *"Engineering is full of quantities that grow or decay exponentially — RC
> circuits, radioactive material, bacterial populations, compound interest.
> The logarithm is the tool that tames them: it turns multiplication into
> addition and exponentiation into multiplication. Master this and you have
> the key to half the differential equations you'll meet."*

---

## Before You Start

**Prerequisites:** [01-04 Expressions, Equations, and Inequalities](01-04-expressions-equations-inequalities.md)

**Skip if:** You pass the Tier 1B test-out quiz. But confirm you can derive
the change-of-base formula and work with $e$ before skipping — those are the
gaps most people have after high school.

**Time:** ~60 min read · ~25 min review questions · ~60 min practice problems

---

## On the Board Today

Apprentice, exponents and logarithms are one of those topics where half the
class thinks they know it and half those people are wrong in ways they don't
know about.

Here's how it usually breaks. The rules for integer exponents feel solid.
Multiplying powers, dividing powers, raising a power to a power — you learned
those in middle school and they stuck. Then someone introduced fractional
exponents and everything started feeling shaky. Then logarithms arrived and
a lot of people checked out. Then someone defined $e \approx 2.718$ and
called it a "natural" base and the room went quiet.

Today we're going to build the whole structure from the rules you already
know, extending each one to fractional and negative exponents, and then
showing that the logarithm is simply the inverse of the exponential — nothing
more mysterious than asking "what power did I have to raise the base to in
order to get this number?"

Two things will immediately be useful when we're done:

Every **decibel calculation** you'll make — in acoustics, RF, signal
processing — is a logarithm.

Every **transient circuit** (RC charging, RL circuit response, exponential
decay of pressure or temperature) uses $e^{-t/\tau}$. Understanding that
expression requires understanding both the exponential and the natural
logarithm.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 5.1 Apply the seven laws of exponents to simplify expressions with
  integer, fractional, and negative exponents
* 5.2 Convert between radical notation and fractional exponent notation
* 5.3 Simplify expressions containing radicals
* 5.4 Define the exponential function $b^x$ for any base $b > 0$, $b \ne 1$
* 5.5 Define $e$ and the natural exponential function $e^x$
* 5.6 Solve exponential equations by matching bases and by using logarithms
* 5.7 Define the logarithm as the inverse of the exponential
* 5.8 Apply the four laws of logarithms to expand and compress expressions
* 5.9 Evaluate common logarithms (base 10) and natural logarithms (base $e$)
* 5.10 Apply the change-of-base formula
* 5.11 Solve logarithmic equations
* 5.12 Recognize and apply exponential and logarithmic models in engineering
  contexts

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $b^x$ | $b$ raised to power $x$ | $b > 0$, $b \ne 1$ for exponential/log purposes |
| $\sqrt[n]{x}$ | $n$th root of $x$ | same as $x^{1/n}$ |
| $e$ | Euler's number, $\approx 2.71828...$ | irrational, defined precisely in §5.3 |
| $\ln x$ | natural logarithm of $x$, base $e$ | — |
| $\log x$ or $\log_{10} x$ | common logarithm, base 10 | Handbook uses $\log_{10}$ |
| $\log_b x$ | logarithm of $x$ to base $b$ | — |
| $\exp(x)$ | same as $e^x$ | used when exponent is complex expression |
| $\tau$ | time constant of an exponential | introduced here; used throughout Tier 2 |

> ---
> **Mentor's Margin**
>
> The Handbook uses $\log_{10}$ for the base-10 logarithm and $\ln$ for the
> natural logarithm, which is the same convention as this guide. Some older
> engineering texts write $\log$ for the natural log (especially in
> thermodynamics). If you ever see $\log$ without a base in an engineering
> formula, check whether the author meant base-10 or base-$e$ — context and
> units will usually tell you.
>
> ---

---

## 5.1 Laws of Exponents

These seven rules are the complete set. Everything you need to simplify any
exponential expression follows from them.

| Law | Statement | Example |
|---|---|---|
| Product | $b^m \cdot b^n = b^{m+n}$ | $x^3 \cdot x^4 = x^7$ |
| Quotient | $\dfrac{b^m}{b^n} = b^{m-n}$ | $\dfrac{x^5}{x^2} = x^3$ |
| Power of a power | $(b^m)^n = b^{mn}$ | $(x^3)^4 = x^{12}$ |
| Power of a product | $(ab)^n = a^n b^n$ | $(2x)^3 = 8x^3$ |
| Power of a quotient | $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ | $\left(\dfrac{x}{3}\right)^2 = \dfrac{x^2}{9}$ |
| Zero exponent | $b^0 = 1$ ($b \ne 0$) | $7^0 = 1$, $(3x)^0 = 1$ |
| Negative exponent | $b^{-n} = \dfrac{1}{b^n}$ | $x^{-3} = \dfrac{1}{x^3}$ |

Three of these cause trouble and deserve extra attention.

### The zero exponent

$b^0 = 1$ for any non-zero $b$. The reason isn't magic: it's the quotient
rule with equal exponents.

$$b^0 = b^{n-n} = \frac{b^n}{b^n} = 1$$

### Negative exponents

$b^{-n}$ does not mean "make the result negative." It means "put the factor
in the denominator."

$$x^{-3} = \frac{1}{x^3} \qquad \frac{1}{x^{-3}} = x^3 \qquad 4^{-2} = \frac{1}{16}$$

> ---
> **Mentor's Margin**
>
> The negative exponent is the source of a whole family of prefix errors.
> $10^{-3}$ is *not* $-1000$. It is $\frac{1}{1000}$. Every milli, micro,
> nano, and pico in Chapter 01-01 is a negative power of 10. Combining
> negative exponents in arithmetic is one of the highest-frequency errors
> in engineering calculations. If a result comes out with the wrong sign on
> a power of ten, this rule is where to look.
>
> ---

### Power of a power

$(b^m)^n = b^{mn}$. The exponents multiply — they don't add.

$$(x^3)^4 = x^{12} \quad \text{not } x^7$$

$(x^7$ would come from $x^3 \cdot x^4$ — using the product rule, not the
power-of-a-power rule. Keep them separate.)

### Worked Example 1 — Simplifying With Multiple Laws

**Given.** Simplify, expressing the result with positive exponents:

$$\frac{(3x^2 y^{-1})^3}{9x^{-4}y^2}$$

**Solution.**

Step 1 — Apply power-of-a-product to the numerator:

$$(3x^2 y^{-1})^3 = 3^3 \cdot (x^2)^3 \cdot (y^{-1})^3 = 27 x^6 y^{-3}$$

Step 2 — Divide:

$$\frac{27 x^6 y^{-3}}{9 x^{-4} y^2}$$

Step 3 — Divide coefficients; apply quotient rule to each variable:

$$= 3 \cdot x^{6-(-4)} \cdot y^{-3-2} = 3 x^{10} y^{-5}$$

Step 4 — Convert negative exponent:

$$\boxed{= \frac{3x^{10}}{y^5}}$$

**Check.** Substitute $x = 1$, $y = 1$: numerator is $(3 \cdot 1 \cdot 1)^3
= 27$; denominator is $9 \cdot 1 \cdot 1 = 9$; ratio is 3. Result at $x=1$,
$y=1$: $3(1)^{10}/(1)^5 = 3$. ✓

---

## 5.2 Fractional Exponents and Radicals

This is where integer exponent rules extend to cover roots.

### The definition

$$\boxed{b^{1/n} = \sqrt[n]{b}}$$

The $n$th root is the $1/n$ power. Reason: if $b^{1/n}$ raised to the $n$th
power should give $b$, then $(b^{1/n})^n = b^{n/n} = b^1 = b$ by the power-
of-a-power rule. The definition is forced by consistency with the laws we
already have.

More generally:

$$\boxed{b^{m/n} = \left(\sqrt[n]{b}\right)^m = \sqrt[n]{b^m}}$$

Either order works — root first, then power, or power first, then root. Root
first usually involves smaller intermediate numbers.

### Common fractional exponents

| Fractional exponent | Radical | Example |
|---|---|---|
| $b^{1/2}$ | $\sqrt{b}$ | $16^{1/2} = 4$ |
| $b^{1/3}$ | $\sqrt[3]{b}$ | $27^{1/3} = 3$ |
| $b^{2/3}$ | $\left(\sqrt[3]{b}\right)^2$ | $8^{2/3} = (2)^2 = 4$ |
| $b^{3/2}$ | $\left(\sqrt{b}\right)^3$ | $4^{3/2} = (2)^3 = 8$ |
| $b^{-1/2}$ | $\dfrac{1}{\sqrt{b}}$ | $9^{-1/2} = \dfrac{1}{3}$ |

### Simplifying radicals

**Factor out perfect squares (or perfect $n$th powers).**

$$\sqrt{48} = \sqrt{16 \cdot 3} = \sqrt{16}\cdot\sqrt{3} = 4\sqrt{3}$$

$$\sqrt[3]{54} = \sqrt[3]{27 \cdot 2} = 3\sqrt[3]{2}$$

**Rationalize denominators** — remove radicals from denominators by
multiplying by the conjugate or by the radical itself.

$$\frac{5}{\sqrt{3}} = \frac{5}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{3}$$

$$\frac{3}{2 + \sqrt{5}} = \frac{3}{2+\sqrt{5}} \cdot \frac{2-\sqrt{5}}{2-\sqrt{5}} = \frac{3(2-\sqrt{5})}{4 - 5} = \frac{3(2-\sqrt{5})}{-1} = -3(2-\sqrt{5})$$

> ---
> **Mentor's Margin**
>
> Rationalizing a denominator isn't just an aesthetic exercise. Handbook
> formulas often produce expressions like $1/\sqrt{LC}$ or $1/\sqrt{2}$, and
> comparing your answer to a Handbook form or a multiple-choice option
> requires writing them in the same form. If one answer choice is
> $\sqrt{3}/3$ and another is $1/\sqrt{3}$, they're equal — and knowing that
> saves you from second-guessing a correct answer.
>
> ---

### Worked Example 2 — Fractional Exponents in an Engineering Formula

**Given.** The natural frequency of a simple spring-mass system is:

$$\omega_n = \sqrt{\frac{k_s}{m}}$$

where $k_s$ is the spring constant in N/m and $m$ is mass in kg. Express
$\omega_n$ using fractional exponent notation, then verify the units.

**Solution.**

$$\omega_n = \left(\frac{k_s}{m}\right)^{1/2}$$

Units check:

$$\left[\frac{\text{N/m}}{\text{kg}}\right]^{1/2} = \left[\frac{\text{kg/s}^2}{\text{kg}}\right]^{1/2} = \left[\frac{1}{\text{s}^2}\right]^{1/2} = \frac{1}{\text{s}} = \text{rad/s}$$

**Check.** Angular frequency has units of radians per second. The dimensional
analysis confirms the formula is at least dimensionally consistent. ✓

*(This equation will appear in full context in Chapter 02-33 on vibrations.
For now, treat it as a fractional-exponent and dimensional exercise.)*

---

## 5.3 The Exponential Function

An **exponential function** has the variable in the exponent:

$$f(x) = b^x \qquad b > 0, \; b \ne 1$$

The base $b$ is constant; the exponent $x$ varies. This is opposite to a
power function like $f(x) = x^2$, where the base varies and the exponent
is fixed.

### Behavior

For $b > 1$ (growth): as $x$ increases, $b^x$ increases rapidly — faster
than any polynomial.

For $0 < b < 1$ (decay): as $x$ increases, $b^x$ decreases toward zero.

Both pass through $(0, 1)$, since $b^0 = 1$ for all valid bases.

### Euler's number $e$

Among all possible bases, one is special: $e \approx 2.71828...$

The precise definition is:

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n$$

It arises naturally wherever a quantity grows or decays at a rate proportional
to its current size. Population growth, radioactive decay, capacitor charging,
heat transfer, compound interest — all governed by $e^x$.

Why $e$ specifically? Because it's the unique base for which the exponential
function is its own derivative:

$$\frac{d}{dx}\left(e^x\right) = e^x$$

>**Preview Note**
That self-referential property is what makes differential equations involving
exponential growth and decay so tractable. We'll use it properly when we get
to calculus in Tier 1C; for now, take it as the reason $e$ appears constantly
in science and engineering.

> ---
> **Mentor's Margin**
>
> The value $e = 2.71828...$ appears in your calculator as its own key.
> Use it. Like $\pi$, it's irrational and you should never truncate it to
> 2.718 at the start of a calculation. More importantly: any time you see
> an exponential in an engineering formula, ask whether the base is $e$ or
> 10 or something else. RC circuit transients use $e$. Decibels use 10.
> Confusing them produces an answer wrong by a factor unrelated to a prefix
> slip — it's quiet and hard to trace.
>
> ---

### The natural exponential in engineering

The expression you'll see most often:

$$f(t) = A \, e^{-t/\tau}$$

where $A$ is the initial value and $\tau$ (tau) is the **time constant** —
the time at which the function has decayed to $1/e \approx 36.8\%$ of its
initial value.

| Time elapsed | Value |
|---|---|
| $t = 0$ | $A$ |
| $t = \tau$ | $A/e \approx 0.368A$ |
| $t = 2\tau$ | $A/e^2 \approx 0.135A$ |
| $t = 5\tau$ | $A/e^5 \approx 0.0067A$ |

**The 5-tau rule:** After $5\tau$, the exponential is within 0.7% of its
final value. Engineers treat this as "fully decayed" or "fully settled" in
most practical situations.

These numbers — 36.8% at one time constant, essentially complete at five —
appear in RC circuit analysis (Chapter 02-63), thermal systems (Chapter
02-55), and every first-order transient you'll meet in Tier 2.

---

## 5.4 Logarithms

The **logarithm base $b$** is the inverse function of $b^x$:

$$\boxed{\log_b x = y \quad \Longleftrightarrow \quad b^y = x}$$

Read: "log base $b$ of $x$ equals $y$" means "$b$ raised to the power $y$
gives $x$."

That's it. The logarithm answers the question: **what power do I raise $b$
to in order to get $x$?**

### Special cases that must be automatic

$$\log_b 1 = 0 \quad\text{(since } b^0 = 1\text{)}$$
$$\log_b b = 1 \quad\text{(since } b^1 = b\text{)}$$
$$\log_b b^x = x \quad\text{(inverse function, cancels)}$$
$$b^{\log_b x} = x \quad\text{(inverse function, cancels)}$$

The last two are the cancellation identities. When the base of an exponential
matches the base of a logarithm, they cancel. This is exactly how you solve
exponential equations.

### The two special bases

**Base 10 — the common logarithm:**

$$\log_{10} x = \log x$$

When you see $\log$ with no base specified in a Handbook formula, it means
$\log_{10}$. This is the base used in decibel calculations, pH, the Richter
scale, and any engineering formula where "log" appears unqualified.

**Base $e$ — the natural logarithm:**

$$\log_e x = \ln x$$

Used in calculus, differential equations, thermodynamics (entropy), reaction
kinetics, and anywhere exponential growth or decay models appear.

### Worked Example 3 — Evaluating Logarithms Without a Calculator

**Given.** Evaluate: (a) $\log_2 32$ (b) $\log_3 \frac{1}{27}$
(c) $\log_{10} 0.001$ (d) $\ln e^5$

**Approach.** Convert to the exponential form $b^y = x$ and identify the
exponent.

**Solution.**

(a) $\log_2 32$: ask "2 to what power equals 32?"
$2^5 = 32 \Rightarrow \boxed{\log_2 32 = 5}$

(b) $\log_3 \tfrac{1}{27}$: ask "3 to what power equals $1/27$?"
$3^{-3} = 1/27 \Rightarrow \boxed{\log_3 \tfrac{1}{27} = -3}$

(c) $\log_{10} 0.001$: $0.001 = 10^{-3} \Rightarrow \boxed{\log_{10} 0.001 = -3}$

(d) $\ln e^5$: the cancellation identity. $\log_e e^5 = 5 \Rightarrow
\boxed{\ln e^5 = 5}$

**Check.** Every answer can be verified by raising the base to the answer:
$2^5 = 32$ ✓, $3^{-3} = 1/27$ ✓, $10^{-3} = 0.001$ ✓, $e^5 = e^5$ ✓.

---

## 5.5 Laws of Logarithms

Four laws, all derived from the exponent laws. The derivations are short and
help with memory.

### Law 1 — Product rule

$$\boxed{\log_b(xy) = \log_b x + \log_b y}$$

Derivation: let $\log_b x = m$ and $\log_b y = n$. Then $x = b^m$ and
$y = b^n$. So $xy = b^m \cdot b^n = b^{m+n}$. Taking $\log_b$ of both sides:
$\log_b(xy) = m + n = \log_b x + \log_b y$. QED.

**The logarithm of a product equals the sum of logarithms.** This is what
makes logarithms useful for computation: multiplication becomes addition.

### Law 2 — Quotient rule

$$\boxed{\log_b\frac{x}{y} = \log_b x - \log_b y}$$

Same derivation with division: $x/y = b^m/b^n = b^{m-n}$.

### Law 3 — Power rule

$$\boxed{\log_b(x^r) = r \log_b x}$$

Derivation: let $\log_b x = m$, so $x = b^m$. Then $x^r = b^{mr}$. Taking
$\log_b$: $\log_b(x^r) = mr = r\log_b x$. QED.

**The power inside a logarithm comes out front as a multiplier.** This is
the law that makes decibel calculations natural and that solves exponential
equations when bases can't be matched by inspection.

### Law 4 — Change of base

$$\boxed{\log_b x = \frac{\ln x}{\ln b} = \frac{\log_{10} x}{\log_{10} b}}$$

Your calculator has $\ln$ and $\log_{10}$ buttons. It probably does not have
a $\log_2$ button. The change-of-base formula lets you evaluate any
logarithm using the two bases your calculator has.

> ---
> **Mentor's Margin**
>
> Derive the change-of-base formula yourself once so you remember it in terms
> of structure rather than symbol arrangement. Set $y = \log_b x$, so
> $b^y = x$. Take $\ln$ of both sides: $\ln(b^y) = \ln x$. Apply the power
> rule: $y \ln b = \ln x$. Divide: $y = \ln x / \ln b$. That's the formula,
> and now you can rebuild it any time you need it.
>
> ---

### What you can't do

These are the most common invalid "laws" that people invent:

$$\log_b(x + y) \ne \log_b x + \log_b y \qquad \text{(no sum rule for log)}$$

$$\log_b(x + y) \ne (\log_b x)(\log_b y) \qquad \text{(not a product either)}$$

$$\frac{\log_b x}{\log_b y} \ne \log_b\frac{x}{y} \qquad \text{(quotient rule is subtraction, not division)}$$

$$(\log_b x)^r \ne r\log_b x \qquad \text{(power rule applies inside the log, not outside)}$$

The last one is particularly sneaky. $\log_b(x^r) = r \log_b x$ because the
power is *inside* the logarithm. If the power is *outside*, $(\log_b x)^r$
means the logarithm raised to a power, which is different and has no
simplification.

---

## 5.6 Solving Exponential Equations

Two strategies, depending on whether you can match bases.

### Strategy 1 — Match bases by inspection

If both sides can be expressed with the same base, set the exponents equal.

$$2^{3x} = 16 = 2^4 \implies 3x = 4 \implies x = \frac{4}{3}$$

$$9^x = 27 \implies (3^2)^x = 3^3 \implies 2x = 3 \implies x = \frac{3}{2}$$

### Strategy 2 — Take a logarithm of both sides

When bases can't be matched, take $\ln$ (or $\log_{10}$) of both sides and
apply the power rule.

$$5^x = 80$$
$$\ln(5^x) = \ln 80$$
$$x \ln 5 = \ln 80$$
$$x = \frac{\ln 80}{\ln 5} = \frac{4.382}{1.609} = 2.723$$

**Check:** $5^{2.723} = e^{2.723 \ln 5} = e^{4.382} = 80.0$ ✓

### Worked Example 4 — Exponential Decay Problem

**Given.** A capacitor discharges through a resistor. Its voltage follows:

$$V(t) = V_0 \, e^{-t/\tau}$$

where $V_0 = 24 \text{ V}$ and $\tau = 0.050 \text{ s}$.

(a) Find $V$ at $t = 0.10$ s.
(b) Find the time at which $V = 5.0$ V.
(c) Find the time at which the capacitor has discharged to 1% of its initial
voltage.

**Solution.**

(a) Substitute directly:

$$V(0.10) = 24 \, e^{-0.10/0.050} = 24 \, e^{-2} = 24(0.1353) = \boxed{3.25 \text{ V}}$$

Note: $t = 0.10$ s $= 2\tau$. The table in §5.3 predicted $\approx 13.5\%$
of initial, and $0.135 \times 24 = 3.24$ V. ✓

(b) Solve for $t$ when $V = 5.0$:

$$5.0 = 24 \, e^{-t/0.050}$$

Divide both sides by 24:

$$e^{-t/0.050} = \frac{5.0}{24} = 0.2083$$

Take $\ln$ of both sides (cancellation identity on left side after rearranging):

$$-\frac{t}{0.050} = \ln(0.2083) = -1.568$$

$$t = 0.050 \times 1.568 = \boxed{0.0784 \text{ s} \approx 78.4 \text{ ms}}$$

**Check.** At $t = \tau = 0.050$ s: $V = 24/e = 8.83$ V. At $t = 78.4$ ms
$= 1.57\tau$: voltage should be between $8.83$ V (at $\tau$) and $3.25$ V
(at $2\tau$), and 5.0 V sits in that range. ✓

(c) 1% of initial: $V = 0.01 \times 24 = 0.24$ V:

$$0.24 = 24 \, e^{-t/0.050}$$

$$e^{-t/0.050} = 0.01$$

$$-\frac{t}{0.050} = \ln(0.01) = -4.605$$

$$t = 0.050 \times 4.605 = \boxed{0.230 \text{ s} = 4.6\tau}$$

**Check.** Consistent with the 5-tau rule: at $5\tau = 0.250$ s, the voltage
is $24e^{-5} = 0.162$ V, which is about 0.67% — less than 1%. At $4.6\tau$
the voltage is about 1% as calculated. ✓

---

## 5.7 Solving Logarithmic Equations

Two strategies, paralleling the exponential case.

### Strategy 1 — Consolidate to a single logarithm, then convert

$$\log_3(x + 4) = 2$$
$$x + 4 = 3^2 = 9$$
$$x = 5$$

**Verify:** $\log_3(5 + 4) = \log_3 9 = 2$ ✓

If both sides have logarithms of the same base, set the arguments equal:

$$\log_5 x = \log_5(3x - 8) \implies x = 3x - 8 \implies x = 4$$

**Verify:** $\log_5 4 = \log_5(12 - 8) = \log_5 4$ ✓

### Strategy 2 — Use laws to consolidate first, then convert

$$\ln x + \ln(x - 3) = \ln 10$$
$$\ln[x(x-3)] = \ln 10$$
$$x(x-3) = 10$$
$$x^2 - 3x - 10 = 0$$
$$(x-5)(x+2) = 0$$
$$x = 5 \quad \text{or} \quad x = -2$$

**Check both solutions in the original equation**, because logarithms are
only defined for positive arguments.

$x = 5$: $\ln 5 + \ln 2 = \ln 10$ ✓ (valid)

$x = -2$: $\ln(-2)$ is undefined. ✗ (extraneous)

$$\boxed{x = 5}$$

> ---
> **Mentor's Margin**
>
> Extraneous solutions from logarithmic equations are not rare edge cases.
> Whenever you solve a logarithmic equation by combining logs and solving
> the resulting polynomial, **verify every solution in the original
> equation**. A negative argument to a logarithm produces a result that
> technically doesn't exist. Always check.
>
> ---

---

## 5.8 Engineering Applications of Logarithms

### Decibels — base-10 logarithm applied

**Power ratio in dB:**

$$\text{dB} = 10 \log_{10}\frac{P_2}{P_1}$$

**Voltage ratio in dB** (when both measured across equal impedances):

$$\text{dB} = 20 \log_{10}\frac{V_2}{V_1}$$

The factor of 20 instead of 10 comes from the power-rule: $P \propto V^2$,
so $10\log(V^2/V_1^2) = 10 \cdot 2\log(V/V_1) = 20\log(V/V_1)$.

### Worked Example 5 — Decibels and Back

**Given.** (a) A signal amplifier increases power from 2 mW to 400 mW.
Find the gain in dB. (b) A cable attenuates a signal by 12 dB. If the input
is 1.0 V, find the output voltage.

**Solution.**

(a) $\text{dB} = 10\log_{10}(400/2) = 10\log_{10}(200) = 10(2.301) =
\boxed{23.0 \text{ dB}}$

*Check:* +10 dB = ×10, +3 dB ≈ ×2. So +23 dB ≈ ×10 × 10 × 2 = ×200. ✓

(b) $-12 = 20\log_{10}(V_{out}/1.0)$

$$\log_{10}(V_{out}) = \frac{-12}{20} = -0.60$$

$$V_{out} = 10^{-0.60} = 0.251 \text{ V}$$

$$\boxed{V_{out} \approx 0.251 \text{ V}}$$

*Check:* $-6$ dB halves voltage (since $20\log_{10}(0.5) = -6.02$ dB).
Two 6 dB attenuations give $-12$ dB and $0.5 \times 0.5 = 0.25$ V. ✓

### The pH example — logarithmic compression of scale

$$\text{pH} = -\log_{10}[\text{H}^+]$$

where $[\text{H}^+]$ is hydrogen ion concentration in mol/L. This compresses a
range from $10^{-14}$ to $10^0$ mol/L into a 0–14 scale. The negative sign
makes pH increase as $[\text{H}^+]$ decreases (becomes less acidic).

This isn't directly tested on most FE exams, but it appears in the Chemistry
and Environmental Engineering sections and demonstrates the same logarithmic
compression used in decibels, the Richter scale, and many sensor calibrations.

### The exponential growth/decay model

Engineering problems involving first-order processes — population, radioactive
decay, heat transfer to/from an environment, charging/discharging — follow:

$$\frac{dN}{dt} = \pm kN \implies N(t) = N_0 e^{\pm kt}$$

The sign determines growth or decay. The constant $k$ is either stated or
derived from a known condition. Solving for the constant from two data points
uses logarithms:

$$k = \frac{\ln(N_1/N_0)}{t_1 - t_0}$$

We'll derive this properly in Chapter 01-25 (first-order ODEs). For now,
recognize the form: wherever you see a ratio inside a logarithm set equal to
a product involving time, you're looking at an exponential model.

---

## As the Handbook States It

The Handbook's **Mathematics** section (starting p. 36) contains:

> **Handbook 10.6, p. 37** — *Algebra*

The Handbook lists:

- Laws of exponents (product, quotient, power of a power, zero, negative)
- Logarithm laws (product, quotient, power, change of base)
- The relationships $\ln x = \log_e x$ and $\log x = \log_{10} x$
- The conversion $\ln x = \log_{10}x / \log_{10}e = \log_{10}x / 0.43429$

That last item is the change-of-base formula written in a specific form for
converting between $\ln$ and $\log_{10}$. Note the conversion factor:

$$\log_{10}e \approx 0.43429 \qquad \ln 10 \approx 2.3026$$

These reciprocals are used when you need to convert a natural log result to
a common log or vice versa.

**Notation to check:** The Handbook writes $\log_{10}$ consistently for the
base-10 logarithm, not unqualified $\log$. In the Handbook's mathematics
section, follow its notation.

**What's in the Handbook:** all four logarithm laws, the exponent laws, the
conversion factor between $\ln$ and $\log_{10}$.

**What's not in the Handbook — memorize:**
- The meaning of $e$ and why it's the natural base
- The 5-tau rule for exponential decay
- The decibel formulas (these appear in the Electrical section of the
  Handbook, not in Mathematics — and you use them constantly)
- The strategy for solving exponential and logarithmic equations
- What an extraneous solution is and why it occurs in log equations

---

## Where This Goes Wrong

**Negative exponent meaning "negative result."** $4^{-2} = 1/16$, not $-16$.
A negative exponent puts the factor in the denominator.

**Adding exponents when taking a power of a power.** $(x^3)^4 = x^{12}$,
not $x^7$. Product rule adds exponents; power-of-a-power multiplies them.

**Applying $(a+b)^n = a^n + b^n$.** This is wrong except when $n = 1$. In
particular: $\sqrt{a+b} \ne \sqrt{a} + \sqrt{b}$, which derails many
quadratic and radical simplifications.

**Forgetting the middle term in $(a+b)^2$.** Three terms, not two.

**Confusing $\log(xy)$ with $(\log x)(\log y)$.** The product rule says
log of a product equals the *sum* of logs. The product of logs has no
simplification.

**Using $e = 2.718$ as a truncated value early in a multi-step problem.**
Use the $e$ key. The error compounds in exponential calculations faster than
in most others because the variable is in the exponent.

**Confusing base-10 and base-$e$ logarithms.** $\log$ and $\ln$ are
different functions. In decibels, you use $\log_{10}$. In ODE solutions and
RC transients, you use $\ln$. Mixing them introduces a factor of
$\ln 10 \approx 2.303$.

**Not checking for extraneous solutions in log equations.** Any solution that
would produce a negative argument to a logarithm is invalid. The equation
might factor to produce it; always substitute back.

**Forgetting that $\log_b b^x = x$ and $b^{\log_b x} = x$.** These
cancellation identities are the mechanism for solving both exponential and
logarithmic equations, and they come up constantly.

**Misidentifying the time constant $\tau$.** In $e^{-t/\tau}$, the time
constant is $\tau$, not the coefficient in the exponent. If the exponent is
$-3t$, then $\tau = 1/3$. The value at $t = \tau$ is $e^{-1} \approx 36.8\%$
of the initial value, not 63.2% — that's the value at $t = \tau$ of the
*rising* form $1 - e^{-t/\tau}$.

---

## Key Terms

| Term | Definition |
|---|---|
| Base | The number being raised to a power in $b^x$ |
| Exponent | The power to which the base is raised |
| Fractional exponent | An exponent of the form $m/n$; $b^{m/n} = (\sqrt[n]{b})^m$ |
| Radical | Expression involving a root: $\sqrt[n]{x} = x^{1/n}$ |
| Rationalize | Remove radicals from a denominator by multiplying by a suitable expression |
| Conjugate | The expression $(a - b)$ paired with $(a + b)$; their product eliminates radicals |
| Exponential function | $f(x) = b^x$ where $b > 0$, $b \ne 1$ |
| Euler's number $e$ | $\approx 2.71828$; the natural base; defined by $e = \lim_{n\to\infty}(1+1/n)^n$ |
| Time constant $\tau$ | In $Ae^{-t/\tau}$, the time for the quantity to decay to $1/e \approx 36.8\%$ of $A$ |
| 5-tau rule | After $5\tau$, an exponential decay is within $\approx 0.7\%$ of its final value |
| Logarithm | $\log_b x = y$ means $b^y = x$; asks "what power of $b$ gives $x$?" |
| Common logarithm | $\log_{10} x$; written $\log$ without base in most engineering formulas |
| Natural logarithm | $\log_e x = \ln x$; inverse of $e^x$ |
| Change-of-base formula | $\log_b x = \ln x / \ln b = \log_{10} x / \log_{10} b$ |
| Extraneous solution | A value that satisfies a transformed equation but not the original |
| Decibel (dB) | $10\log_{10}(P_2/P_1)$ for power ratios; $20\log_{10}(V_2/V_1)$ for voltage |

---

## Review Questions

### Conceptual

1. State the seven laws of exponents. For each, give an example showing a
   mistake that results from confusing it with a different law.
2. Explain why $b^{1/n} = \sqrt[n]{b}$ using the power-of-a-power law.
   Don't quote it — derive it.
3. What makes $e$ special as a base for exponential functions? State the
   property that defines it.
4. Restate the four laws of logarithms in plain language, without symbols.
5. Why does a logarithmic equation potentially produce extraneous solutions?
   What check eliminates them?
6. $\log_b(x + y)$ does not simplify like $\log_b(xy)$. Explain why the
   product rule of logarithms does not apply to a sum inside the log.
7. What is a time constant? What fraction of the initial value remains after
   one time constant? After three time constants?
8. Why does the decibel formula for voltage have a coefficient of 20 rather
   than 10? Show the derivation from the power formula.

### Calculation

9. Simplify, leaving the result with positive exponents only:
   (a) $(2x^{-3}y^2)^4$
   (b) $\dfrac{x^{1/2} \cdot x^{2/3}}{x^{1/6}}$
   (c) $\left(\dfrac{4a^2}{b^{-1}}\right)^{1/2}$
   (d) $\dfrac{(3m^2n^{-1})^3}{(m^{-1}n^2)^2}$

10. Evaluate without a calculator:
    (a) $8^{2/3}$
    (b) $16^{-3/4}$
    (c) $\left(\dfrac{27}{8}\right)^{2/3}$
    (d) $32^{0.4}$

11. Simplify each radical:
    (a) $\sqrt{72}$
    (b) $\sqrt[3]{250}$
    (c) $\dfrac{6}{\sqrt{5}}$ (rationalized form)
    (d) $\dfrac{4}{3 - \sqrt{2}}$ (rationalized form)

12. Evaluate without a calculator:
    (a) $\log_2 64$
    (b) $\log_5 \dfrac{1}{125}$
    (c) $\log_{10} 10{,}000$
    (d) $\ln e^{-3}$
    (e) $\log_4 2$
    (f) $\log_9 27$

13. Use logarithm laws to expand into a sum/difference:
    (a) $\log\dfrac{x^3 y}{z^2}$
    (b) $\ln\sqrt{\dfrac{a^2 b}{c^3}}$

14. Use logarithm laws to write as a single logarithm:
    (a) $2\log x - \frac{1}{2}\log y + 3\log z$
    (b) $\frac{1}{3}(\ln a - 2\ln b)$

15. Solve each exponential equation:
    (a) $3^{2x-1} = 81$
    (b) $5^x = 200$
    (c) $e^{3x} = 45$
    (d) $4 \cdot 2^{x/3} = 100$

16. Solve each logarithmic equation, checking for extraneous solutions:
    (a) $\log_2(x + 5) = 4$
    (b) $\ln(2x - 1) = 3$
    (c) $\log(x) + \log(x - 3) = 1$
    (d) $\ln(x+2) - \ln(x-1) = \ln 4$

17. **Engineering application.** An RC circuit has a time constant
    $\tau = 0.025$ s. The capacitor voltage starts at $V_0 = 36$ V and
    decays as $V(t) = 36e^{-t/\tau}$.
    (a) What is $V$ at $t = 0.025$ s?
    (b) At $t = 0.075$ s?
    (c) At what time has $V$ fallen to 10% of its initial value?
    (d) At what time has $V$ fallen to 2.0 V?

18. **Engineering application.** A signal chain has the following stages:
    preamplifier gain $+22$ dB, cable loss $-4$ dB, amplifier gain $+18$ dB,
    filter insertion loss $-2$ dB.
    (a) Total gain in dB.
    (b) If the input signal power is $P_{in} = 0.5$ mW, find the output
    power in mW.
    (c) If the input signal voltage across a $50 \; \Omega$ impedance is
    $8$ mV, find the output voltage.

19. **Engineering application.** Radioactive material decays exponentially.
    A sample of 500 g of a substance has a half-life of 30 years, meaning
    it decays to half its mass in 30 years.
    (a) Write the decay equation $m(t) = m_0 e^{-kt}$, finding $k$.
    (b) How much remains after 90 years?
    (c) How long until only 50 g remains?

### Multiple Choice

20. $\left(\dfrac{x^3}{y^{-2}}\right)^2$ simplifies to:
    A) $\dfrac{x^6}{y^4}$
    B) $x^6 y^4$
    C) $\dfrac{x^5}{y^{-4}}$
    D) $x^6 y^{-4}$

21. $\log_b(x^3 y^{1/2})$ equals:
    A) $\dfrac{3\log_b x}{\frac{1}{2}\log_b y}$
    B) $3\log_b x + \dfrac{1}{2}\log_b y$
    C) $3\log_b x \cdot \dfrac{1}{2}\log_b y$
    D) $3\log_b(xy)$

22. The solution to $\ln(x^2 - 4) = \ln(3x)$ is:
    A) $x = 4$ only
    B) $x = 4$ or $x = -1$
    C) $x = 4$ or $x = 1$
    D) $x = -1$ only

23. If $e^{-t/\tau} = 0.368$, then $t$ equals:
    A) $0$
    B) $\tau/e$
    C) $\tau$
    D) $5\tau$

24. A +6 dB power gain corresponds to a power ratio of approximately:
    A) $2\times$
    B) $4\times$
    C) $6\times$
    D) $10\times$

25. $\log_6 36$ equals:
    A) $1$
    B) $2$
    C) $6$
    D) $\ln 36 / \ln 10$

26. The change-of-base formula states $\log_b x$ equals:
    A) $b \log x$
    B) $\log b \cdot \log x$
    C) $\dfrac{\log x}{\log b}$
    D) $\dfrac{\log b}{\log x}$

---

## Answer Key with Explanations

**1.** Laws with illustrative confusions:
- *Product* $b^m b^n = b^{m+n}$: confusion is $b^m b^n = b^{mn}$ (multiplying exponents instead of adding).
- *Quotient* $b^m/b^n = b^{m-n}$: confusion is dividing exponents instead of subtracting.
- *Power of a power* $(b^m)^n = b^{mn}$: confusion is $b^{m+n}$ (adding instead of multiplying).
- *Zero exponent* $b^0 = 1$: confusion is $b^0 = 0$.
- *Negative exponent* $b^{-n} = 1/b^n$: confusion is $b^{-n} = -b^n$ (making the result negative).
- *Power of a product* $(ab)^n = a^n b^n$: confusion is $(ab)^n = a^n b$ (forgetting both factors get the exponent).
- *Power of a quotient* $(a/b)^n = a^n/b^n$: confusion is $a^n/b$ (forgetting the denominator also gets the exponent). (§5.1)

**2.** If we define $b^{1/n}$ consistently with the power-of-a-power law, then $(b^{1/n})^n = b^{(1/n) \cdot n} = b^1 = b$. So $b^{1/n}$ is a number which, when raised to the $n$th power, gives $b$. That is exactly the definition of the $n$th root: $\sqrt[n]{b}$. Therefore $b^{1/n} = \sqrt[n]{b}$. The definition is forced by consistency with the existing laws; it's not an independent rule. (§5.2)

**3.** $e$ is the unique positive number such that $d(e^x)/dx = e^x$ — the exponential function is its own derivative. Equivalently, $e = \lim_{n \to \infty}(1 + 1/n)^n$. It's the natural base because it arises wherever a quantity's rate of change is proportional to its current value, which describes an enormous range of physical processes. (§5.3)

**4.**
- *Product rule:* the log of a product equals the sum of the logs.
- *Quotient rule:* the log of a quotient equals the difference of the logs.
- *Power rule:* the log of something raised to a power equals that power times the log.
- *Change of base:* any log can be computed by dividing the log of the argument by the log of the base, using any convenient base. (§5.5)

**5.** When you combine logarithms and solve the resulting polynomial, you may get solutions that make the original logarithm argument zero or negative. Those solutions are algebraically valid for the polynomial but physically invalid for the logarithm, which is only defined for positive arguments. They're called extraneous solutions, and checking means substituting back into the *original* equation (before any log laws were applied) and verifying all log arguments are positive. (§5.7)

**6.** The product rule derives from the exponent product rule: $\log_b(xy) = \log_b(b^m \cdot b^n) = \log_b(b^{m+n}) = m+n$, where $x = b^m$ and $y = b^n$. There's no corresponding rule for addition inside the log because $b^m + b^n$ is not a simple power of $b$. The product rule works because multiplication of exponentials adds exponents; addition of exponentials has no such simplification. (§5.5)

**7.** A time constant $\tau$ is the parameter in $Ae^{-t/\tau}$ representing the time for the quantity to decay to $1/e \approx 36.8\%$ of its initial value $A$. After one time constant: $\approx 36.8\%$ remains. After two: $\approx 13.5\%$. After three: $\approx 5.0\%$. After five: $\approx 0.67\%$ (essentially zero for engineering purposes). (§5.3)

**8.** Power is proportional to voltage squared: $P \propto V^2$. So the power ratio is:
$$\frac{P_2}{P_1} = \frac{V_2^2}{V_1^2} = \left(\frac{V_2}{V_1}\right)^2$$
Applying the dB power formula:
$$\text{dB} = 10\log_{10}\left(\frac{V_2}{V_1}\right)^2 = 10 \cdot 2\log_{10}\frac{V_2}{V_1} = 20\log_{10}\frac{V_2}{V_1}$$
The factor of 2 from the power rule generates the coefficient of 20. (§5.8)

**9.**

(a) $(2x^{-3}y^2)^4 = 2^4 x^{-12} y^8 = \dfrac{16y^8}{x^{12}}$

(b) $x^{1/2} \cdot x^{2/3} = x^{1/2 + 2/3} = x^{3/6 + 4/6} = x^{7/6}$.
Then $x^{7/6} / x^{1/6} = x^{7/6 - 1/6} = \boxed{x^1 = x}$

(c) $\left(\dfrac{4a^2}{b^{-1}}\right)^{1/2} = \left(4a^2 b\right)^{1/2} = \sqrt{4} \cdot a^{2 \cdot 1/2} \cdot b^{1/2} = \boxed{2a\sqrt{b}}$

(d) Numerator: $(3m^2n^{-1})^3 = 27m^6n^{-3}$.
Denominator: $(m^{-1}n^2)^2 = m^{-2}n^4$.
Ratio: $\dfrac{27m^6n^{-3}}{m^{-2}n^4} = 27m^{6-(-2)}n^{-3-4} = 27m^8n^{-7} = \boxed{\dfrac{27m^8}{n^7}}$

**10.**

(a) $8^{2/3} = (\sqrt[3]{8})^2 = 2^2 = \boxed{4}$

(b) $16^{-3/4} = 1/(16^{3/4}) = 1/(\sqrt[4]{16})^3 = 1/2^3 = \boxed{1/8}$

(c) $(27/8)^{2/3} = (3/2)^2 = \boxed{9/4}$

(d) $32^{0.4} = 32^{2/5} = (\sqrt[5]{32})^2 = 2^2 = \boxed{4}$

**11.**

(a) $\sqrt{72} = \sqrt{36 \cdot 2} = 6\sqrt{2}$

(b) $\sqrt[3]{250} = \sqrt[3]{125 \cdot 2} = 5\sqrt[3]{2}$

(c) $\dfrac{6}{\sqrt{5}} \cdot \dfrac{\sqrt{5}}{\sqrt{5}} = \dfrac{6\sqrt{5}}{5}$

(d) $\dfrac{4}{3-\sqrt{2}} \cdot \dfrac{3+\sqrt{2}}{3+\sqrt{2}} = \dfrac{4(3+\sqrt{2})}{9-2} = \dfrac{4(3+\sqrt{2})}{7} = \boxed{\dfrac{12 + 4\sqrt{2}}{7}}$

**12.**

(a) $2^6 = 64 \Rightarrow \boxed{6}$

(b) $5^{-3} = 1/125 \Rightarrow \boxed{-3}$

(c) $10^4 = 10{,}000 \Rightarrow \boxed{4}$

(d) $\ln e^{-3} = -3$ (cancellation identity) $\Rightarrow \boxed{-3}$

(e) $\log_4 2$: $4^x = 2 \Rightarrow (2^2)^x = 2^1 \Rightarrow 2x = 1 \Rightarrow x = \boxed{1/2}$

(f) $\log_9 27$: $9^x = 27 \Rightarrow (3^2)^x = 3^3 \Rightarrow 2x = 3 \Rightarrow x = \boxed{3/2}$

**13.**

(a) $\log\dfrac{x^3 y}{z^2} = \log(x^3 y) - \log(z^2) = \log x^3 + \log y - 2\log z = \boxed{3\log x + \log y - 2\log z}$

(b) $\ln\sqrt{\dfrac{a^2 b}{c^3}} = \dfrac{1}{2}\ln\dfrac{a^2 b}{c^3} = \dfrac{1}{2}(2\ln a + \ln b - 3\ln c) = \boxed{\ln a + \dfrac{1}{2}\ln b - \dfrac{3}{2}\ln c}$

**14.**

(a) $2\log x - \frac{1}{2}\log y + 3\log z = \log x^2 - \log y^{1/2} + \log z^3 = \boxed{\log\dfrac{x^2 z^3}{\sqrt{y}}}$

(b) $\dfrac{1}{3}(\ln a - 2\ln b) = \dfrac{1}{3}\ln\dfrac{a}{b^2} = \boxed{\ln\left(\dfrac{a}{b^2}\right)^{1/3}}$ or equivalently $\ln\sqrt[3]{a/b^2}$

**15.**

(a) $3^{2x-1} = 81 = 3^4 \Rightarrow 2x-1 = 4 \Rightarrow x = 5/2$. Verify: $3^4 = 81$ ✓. $\boxed{x = 5/2}$

(b) $\ln 5^x = \ln 200 \Rightarrow x\ln 5 = \ln 200 \Rightarrow x = \ln 200/\ln 5 = 5.298/1.609 = \boxed{3.29}$

Check: $5^{3.29} = e^{3.29\ln 5} = e^{5.29} = 199.5 \approx 200$ ✓

(c) $3x = \ln 45 \Rightarrow x = \ln 45/3 = 3.807/3 = \boxed{1.27}$

(d) $2^{x/3} = 25 \Rightarrow (x/3)\ln 2 = \ln 25 \Rightarrow x/3 = \ln 25/\ln 2 = 4.644 \Rightarrow \boxed{x = 13.9}$

**16.**

(a) $x + 5 = 2^4 = 16 \Rightarrow x = 11$. Check: $\log_2(16) = 4$ ✓. $\boxed{x = 11}$

(b) $2x - 1 = e^3 \Rightarrow x = (e^3 + 1)/2 = (20.09 + 1)/2 = \boxed{10.54}$

Check: $\ln(20.08) = 3.00$ ✓

(c) $\log(x(x-3)) = 1 \Rightarrow x^2 - 3x = 10 \Rightarrow x^2 - 3x - 10 = 0 \Rightarrow (x-5)(x+2) = 0$

$x = 5$: both $\log 5$ and $\log 2$ defined ✓
$x = -2$: $\log(-2)$ undefined — extraneous ✗

$\boxed{x = 5}$

(d) $\ln\dfrac{x+2}{x-1} = \ln 4 \Rightarrow \dfrac{x+2}{x-1} = 4 \Rightarrow x+2 = 4x-4 \Rightarrow 3x = 6 \Rightarrow x = 2$

Check: $\ln 4 - \ln 1 = \ln 4$ ✓ (and both arguments positive) $\boxed{x = 2}$

**17.**

(a) $V(0.025) = 36e^{-0.025/0.025} = 36e^{-1} = 36/e = \boxed{13.2 \text{ V}}$ ($\approx 36.8\%$ of 36 V ✓)

(b) $V(0.075) = 36e^{-3} = 36/e^3 = 36/20.09 = \boxed{1.79 \text{ V}}$ ($\approx 5.0\%$ of 36 V ✓)

(c) $0.10 \times 36 = 3.6 = 36e^{-t/0.025}$

$e^{-t/0.025} = 0.10 \Rightarrow -t/0.025 = \ln(0.10) = -2.303$

$t = 0.025 \times 2.303 = \boxed{0.0576 \text{ s} = 57.6 \text{ ms} = 2.30\tau}$

(d) $2.0 = 36e^{-t/0.025} \Rightarrow e^{-t/0.025} = 0.05556$

$-t/0.025 = \ln(0.05556) = -2.890 \Rightarrow t = 0.025 \times 2.890 = \boxed{0.0722 \text{ s} = 72.2 \text{ ms}}$

**18.**

(a) Total gain $= +22 - 4 + 18 - 2 = \boxed{+34 \text{ dB}}$

(b) $34 = 10\log_{10}(P_{out}/0.5)$

$\log_{10}(P_{out}/0.5) = 3.4$

$P_{out}/0.5 = 10^{3.4} = 2{,}512$

$P_{out} = 2{,}512 \times 0.5 = \boxed{1{,}256 \text{ mW} = 1.26 \text{ W}}$

Check: +30 dB = ×1000, +34 dB = ×2512; $0.5 \times 2512 = 1256$ mW ✓

(c) $34 = 20\log_{10}(V_{out}/0.008)$

$\log_{10}(V_{out}/0.008) = 1.7$

$V_{out}/0.008 = 10^{1.7} = 50.12$

$V_{out} = 0.008 \times 50.12 = \boxed{0.401 \text{ V} = 401 \text{ mV}}$

**19.**

(a) At $t = 30$: $m(30) = 250$ g (half of 500 g).

$250 = 500e^{-30k} \Rightarrow e^{-30k} = 0.5 \Rightarrow -30k = \ln(0.5) = -0.6931$

$k = 0.6931/30 = \boxed{0.02310 \text{ yr}^{-1}}$

$m(t) = 500e^{-0.02310t}$ g

(b) $m(90) = 500e^{-0.02310 \times 90} = 500e^{-2.079} = 500 \times 0.1250 = \boxed{62.5 \text{ g}}$

Check: 90 years = 3 half-lives. $500 \to 250 \to 125 \to 62.5$ g ✓

(c) $50 = 500e^{-0.02310t} \Rightarrow e^{-0.02310t} = 0.10$

$-0.02310t = \ln(0.10) = -2.303$

$t = 2.303/0.02310 = \boxed{99.7 \text{ yr}}$

Check: 50 g is $1/10$ of 500 g. After $\log_2(10) = 3.32$ half-lives:
$3.32 \times 30 = 99.7$ yr ✓

**20. B — $x^6 y^4$.** $(x^3)^2 = x^6$; $(y^{-2})^2 = y^{-4}$; and $y^{-4}$
in the denominator of a fraction flips to $y^4$ in the numerator. The
expression is $x^6 / y^{-4} = x^6 y^4$. (A) has $y^4$ in the denominator,
which would require an extra negative flip. (§5.1)

**21. B.** Product rule: $\log_b(x^3 y^{1/2}) = \log_b x^3 + \log_b y^{1/2}$.
Power rule on each: $= 3\log_b x + \frac{1}{2}\log_b y$. (§5.5)

**22. A — $x = 4$ only.** Setting arguments equal: $x^2 - 4 = 3x \Rightarrow
x^2 - 3x - 4 = 0 \Rightarrow (x-4)(x+1) = 0 \Rightarrow x = 4$ or $x = -1$.

Check $x = -1$: $\ln((-1)^2 - 4) = \ln(-3)$ — undefined. Extraneous.

Check $x = 4$: $\ln(16-4) = \ln(12)$ and $\ln(12)$. ✓ (§5.7)

**23. C — $\tau$.** $e^{-\tau/\tau} = e^{-1} = 1/e \approx 0.368$. The value
$e^{-1}$ is by definition the value at exactly one time constant. (§5.3)

**24. B — $4\times$.** $+3$ dB $\approx 2\times$ power. $+6$ dB $= 2 \times
(+3$ dB$) \approx 2 \times 2 = 4\times$ power. Verify: $10\log_{10}(4) =
10(0.602) = 6.02$ dB ✓. (§5.8)

**25. B — 2.** $6^2 = 36$, so $\log_6 36 = 2$. (D) would be the change-of-
base formula for $\log_{10} 36$, not $\log_6 36$. (§5.4)

**26. C — $\log x / \log b$.** The change-of-base formula: $\log_b x = \ln x
/ \ln b = \log x / \log b$. (D) inverts the fraction. (§5.5)

---

## Quick Reference

**Laws of Exponents**

| Law | Form |
|---|---|
| Product | $b^m b^n = b^{m+n}$ |
| Quotient | $b^m/b^n = b^{m-n}$ |
| Power of a power | $(b^m)^n = b^{mn}$ |
| Power of a product | $(ab)^n = a^n b^n$ |
| Zero exponent | $b^0 = 1$ |
| Negative exponent | $b^{-n} = 1/b^n$ |
| Fractional exponent | $b^{m/n} = (\sqrt[n]{b})^m$ |

**Laws of Logarithms** — *Handbook p. 37*

$$\log_b(xy) = \log_b x + \log_b y$$
$$\log_b(x/y) = \log_b x - \log_b y$$
$$\log_b(x^r) = r\log_b x$$
$$\log_b x = \frac{\ln x}{\ln b} = \frac{\log x}{\log b}$$

**What logarithms cannot do**

$$\log_b(x+y) \ne \log_b x + \log_b y \qquad (\log_b x)^r \ne r\log_b x$$

**Cancellation identities**

$$\log_b(b^x) = x \qquad b^{\log_b x} = x$$

**The natural exponential**

$$e \approx 2.71828 \quad \text{(use calculator key)}$$

$$f(t) = Ae^{-t/\tau}: \quad t = \tau \Rightarrow 36.8\%A \quad t = 5\tau \Rightarrow \approx 0\%$$

**Decibels**

$$\text{dB} = 10\log_{10}\frac{P_2}{P_1} \qquad \text{dB} = 20\log_{10}\frac{V_2}{V_1}$$

Key values: $+3$ dB $= 2\times P$; $+6$ dB $= 4\times P = 2\times V$;
$+10$ dB $= 10\times P$; $+20$ dB $= 100\times P = 10\times V$

**Solving strategies**

*Exponential:* match bases by inspection, or take $\ln$ of both sides and
apply power rule.

*Logarithmic:* consolidate to single log, convert to exponential form, then
solve algebraically. **Always check for extraneous solutions.**

**Not in the Handbook — memorize**

Definition of $e$ and its significance · 5-tau rule · exponential decay model
$Ae^{-t/\tau}$ · equation-solving strategies · extraneous-solution check

---

## What's Next

Apprentice, two chapters into Tier 1B. Exponents and logarithms are now
yours.

In **Chapter 01-06: Functions, Graphs, and Transformations**, we make the
connection between an equation and its shape. Every engineering graph you'll
read — a frequency response, a stress-strain curve, a load-displacement
diagram, a Moody chart — is a function plotted. Knowing what transformations
do to a function's shape lets you read those graphs with the same fluency
you're building with the algebra.

Then in Chapter 01-07, we add the polynomial toolset — including the
quadratic formula, which appears constantly in circuit analysis, structural
mechanics, and optimization.

Bring your Handbook open to page 36. We're working in the Mathematics section
from here through the end of Tier 1B.

See you there.

— Your Mentor
