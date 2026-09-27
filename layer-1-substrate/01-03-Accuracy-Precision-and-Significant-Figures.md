---
chapter: "01-03"
title: "Accuracy, Precision, and Significant Figures"
layer: 1
tier: A
template: technical
ledger_ids: [MATH-1A-003-01, MATH-1A-003-02]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-03: Accuracy, Precision, and Significant Figures

> *"Every number you write is a claim. Not just about a quantity — about how
> well you know it. Report too many digits and you're lying. Report too few
> and you're throwing away information you paid for. The goal is to say
> exactly as much as you know and not one digit more."*

---

## Before You Start

**Prerequisites:** [01-01 Numbers, Magnitude, and Metric Prefixes](01-01-numbers-magnitude-prefixes.md) · [01-02 Units, Dimensions, and the Pound Problem](01-02-units-dimensions-pound-problem.md)

**Skip if:** You pass the Tier 1A test-out quiz. But read §3.6 on rounding
mid-calculation before you skip — that one is not obvious and it shows up in
multi-step problems across the entire guide.

**Time:** ~45 min read · ~20 min review questions · ~45 min practice problems

---

## On the Board Today

Apprentice, this chapter is quieter than the last one. No unit traps. No
hidden constants. Just the discipline of reporting numbers honestly.

I'm going to make the case that significant figures aren't a style preference
or a classroom formality. They're a communication protocol. When you write a
number with a certain number of digits, you're making a claim about how
precisely that number is known. Your reviewer reads that claim. A structural
engineer who reports a beam stress as 152.447 MPa when her strain gauge reads
to three digits has not been precise — she's been false.

Two things happen in this chapter.

First, we'll work through the six rules the Handbook prints for identifying
significant figures and for carrying them through arithmetic. All six, with
the tricky cases named clearly, because two of them trip nearly everyone the
first time.

Second, we'll talk about when to round and when not to — specifically, why
you should carry full precision through every intermediate step of a
calculation and round exactly once at the end. If you've ever gotten a
slightly different answer than a colleague on a problem you both set up the
same way, intermediate rounding is the most likely culprit. It's also the most
likely culprit when your exam answer is "almost right" — close enough to smell
the answer but wrong enough to mark incorrect.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 3.1 Distinguish accuracy from precision
* 3.2 Distinguish systematic error from random error
* 3.3 Apply the six Handbook rules to determine the number of significant
  figures in any given number
* 3.4 Carry significant figures correctly through addition, subtraction,
  multiplication, and division
* 3.5 Apply the engineering convention of three to four significant figures
  in a final answer
* 3.6 Identify intermediate rounding as a source of compounding error and
  describe the correct practice
* 3.7 Compute absolute error, relative error, and percent error
* 3.8 Distinguish error from uncertainty in a measurement context

---

## Notation Used Here

| Symbol | Meaning in this chapter | Units |
|---|---|---|
| $x_{true}$ | true value of a quantity | same as $x$ |
| $x_{meas}$ | measured value | same as $x$ |
| $E_{abs}$ | absolute error | same as $x$ |
| $E_{rel}$ | relative error | dimensionless |
| $E_{\%}$ | percent error | % |
| $n$ | number of significant figures | — |

No collisions with later chapters. The error symbols are local to this chapter
and to Tier 1F (probability and statistics), where they reappear in a broader
context.

---

## 3.1 Accuracy and Precision

Two words that mean different things and get used interchangeably everywhere
except engineering.

**Accuracy** is how close a measurement is to the true value. An accurate
measurement is one that hits the target.

**Precision** is how repeatable a measurement is — how tightly clustered
repeated measurements are, regardless of whether they're near the true value.

The dartboard picture is the cleanest explanation:

| | High accuracy | Low accuracy |
|---|---|---|
| **High precision** | Tight cluster at the bullseye | Tight cluster, wrong location |
| **Low precision** | Scattered around the bullseye | Scattered everywhere |

A measurement can be:
- **Accurate and precise:** tightly clustered at the right value
- **Precise but inaccurate:** tightly clustered at the wrong value — suggests
  a systematic error
- **Accurate but imprecise:** scattered around the right value — random errors
  averaging out
- **Neither:** scattered and wrong — suggests both types of error

> ---
> **Mentor's Margin**
>
> The precise-but-inaccurate case is the insidious one. If your instrument
> has a calibration error, every reading will be consistently wrong by the
> same amount. High reproducibility looks like precision, and it is — but
> the systematic offset means every measurement is lying to you the same way.
> Calibration exists to catch this. An instrument that has never been
> verified against a known standard is not to be trusted, no matter how
> consistent its readings are.
>
> ---

### Types of error

**Systematic error** shifts all measurements in the same direction. A
consistently low reading. A scale that zeroed wrong. A thermocouple with a
calibration drift. Systematic errors affect accuracy and *cannot* be improved
by taking more measurements — you need to find and eliminate the source.

**Random error** scatters measurements unpredictably around the true value.
Electronic noise. Slight variations in technique. Reading a scale at slightly
different angles. Random errors affect precision and *can* be reduced by
averaging many measurements.

> ---
> **Mentor's Margin**
>
> In practice, real measurements have both. A calibration error shifts the
> mean; noise scatters readings around that shifted mean. Your goal is a
> calibrated instrument (minimizes systematic error) and good technique
> (minimizes random error). In this guide, "error" will almost always mean
> the difference between a calculated or measured value and the accepted true
> value — which is the usage on the exam. The statistical treatment of random
> error belongs in Tier 1F.
>
> ---

---

## 3.2 Error Calculations

Three ways to express how wrong a measurement is.

**Absolute error** — the raw difference, with sign dropped:

$$\boxed{E_{abs} = \lvert x_{meas} - x_{true} \rvert}$$

Same units as the quantity. Tells you how big the mistake was in real terms.

**Relative error** — the ratio of absolute error to true value:

$$\boxed{E_{rel} = \frac{\lvert x_{meas} - x_{true} \rvert}{x_{true}}}$$

Dimensionless. Tells you how big the mistake was in proportion to the quantity.

**Percent error**:

$$\boxed{E_{\%} = \frac{\lvert x_{meas} - x_{true} \rvert}{x_{true}} \times 100\%}$$

Percent error says more than absolute error alone. An error of 5 mm in a
100 mm measurement is 5% — serious. An error of 5 mm in a 10,000 mm
measurement is 0.05% — negligible. Same absolute error, very different
significance.

### Worked Example 1 — Computing Errors

**Given.** A digital gauge reads a pressure as $138.4 \text{ kPa}$. The true
pressure, measured by a calibrated reference, is $142.0 \text{ kPa}$.

**Find.** Absolute error, relative error, and percent error.

**Solution.**

$$E_{abs} = \lvert 138.4 - 142.0 \rvert = 3.6 \text{ kPa}$$

$$E_{rel} = \frac{3.6}{142.0} = 0.02535$$

$$E_{\%} = 0.02535 \times 100 = 2.5\%$$

**Check.** Relative error should be the ratio of absolute error to the true
value. $3.6/142.0 = 0.0254$, and $0.0254 \times 100 = 2.54\%$. ✓ Round to
three significant figures gives $E_{\%} = 2.5\%$.

> ---
> **Mentor's Margin**
>
> Note that we used the **true value** in the denominator, not the measured
> value. Some textbooks use the measured value and get a slightly different
> answer. The exam will typically state which form to use, or the difference
> will be small enough not to matter. When in doubt, use the true value —
> that's what the Handbook's definition implies.
>
> ---

---

## 3.3 Significant Figures — The Six Rules

The Handbook prints six numbered rules on page 2. Here they are, with the
tricky cases named explicitly.

### Rule 1: Non-zero digits are always significant.

$847$ has three significant figures. $6.52$ has three. Simple.

### Rule 2: Zeros between non-zero digits are always significant.

$4{,}008$ has four significant figures — the two zeros are sandwiched and
count. $5.0006$ has five.

### Rule 3: Leading zeros are never significant.

$0.0043$ has **two** significant figures: the 4 and the 3. The zeros before
the 4 are placeholders only. They tell you where the decimal is; they contain
no information about precision.

Scientific notation makes this unambiguous: $0.0043 = 4.3 \times 10^{-3}$.
The mantissa has two digits, so two significant figures.

### Rule 4: Trailing zeros to the right of the decimal point are significant.

$3.400$ has **four** significant figures. The trailing zeros are there because
someone put them there — they're asserting precision. Compare: $3.4$ has two
significant figures. $3.40$ has three. $3.400$ has four. Same value, different
claims about precision.

This rule is why it matters how you write a number. If you measure to four
significant figures and write 3.4, you've lost two of them.

### Rule 5: Trailing zeros in a whole number without a decimal point are ambiguous.

$1{,}300$ could be two, three, or four significant figures. The zeros might be
placeholders, or might indicate precision out to the tens or ones place.

**This is the rule most people don't know exists, and it generates real
ambiguity on engineering drawings and calculations.**

The resolution: use scientific notation or explicit notation.
- $1.3 \times 10^3$ — two significant figures
- $1.30 \times 10^3$ — three significant figures
- $1.300 \times 10^3$ — four significant figures

The Handbook notes an alternative: some writers place a decimal point after
the final zero to indicate all zeros are significant. $1{,}300.$ means four
significant figures. This convention works, but scientific notation is
universally unambiguous.

### Rule 6: Exact numbers have unlimited significant figures.

Defined quantities — $1 \text{ ft} = 12 \text{ in}$ exactly, $\pi$ is exact,
a count of 6 bolts is exactly 6 — do not limit the significant figures of a
calculation. They carry infinite precision because they're not measurements.

> ---
> **Mentor's Margin**
>
> The practical consequence of Rule 6: when you multiply a measured quantity
> by a defined constant like $\pi$ or 2, the result's significant figures are
> limited by the measurement, not the constant. The circumference of a circle
> measured to three significant figures is known to three significant figures,
> not to the infinite precision of $\pi$. This seems obvious, but it catches
> people who look at a calculation like $C = 2\pi r$, see $\pi$ to many
> decimal places, and report more digits than $r$ justified.
>
> ---

### The summary table

| Situation | Significant? | Example | Sig figs |
|---|---|---|---|
| Non-zero digits | Always | 846 | 3 |
| Zeros between non-zeros | Always | 7,008 | 4 |
| Leading zeros | Never | 0.0052 | 2 |
| Trailing zeros after decimal | Always | 6.300 | 4 |
| Trailing zeros in whole number | Ambiguous | 4,500 | 2, 3, or 4 |
| Defined constants, exact counts | Unlimited | $\pi$, 12 in/ft | ∞ |

### Worked Example 2 — Identifying Significant Figures

**Given.** Identify the number of significant figures in each:

(a) $0.00720$
(b) $14{,}000$
(c) $14{,}000.$
(d) $1.4000 \times 10^4$
(e) $80,050$
(f) $10.0$

**Solution.**

(a) $0.00720$ — leading zeros don't count, trailing zero after decimal does.
**Three:** 7, 2, 0.

(b) $14{,}000$ — trailing zeros in a whole number, no decimal point.
**Ambiguous: two, three, four, or five.** As written, most conventions default
to two significant figures (1 and 4), but this should be written in scientific
notation to be unambiguous.

(c) $14{,}000.$ — decimal point present, so all digits including trailing zeros
are significant. **Five:** 1, 4, 0, 0, 0.

(d) $1.4000 \times 10^4$ — mantissa has trailing zeros after the decimal,
which are significant. **Five:** 1, 4, 0, 0, 0. And now there's no ambiguity.

(e) $80{,}050$ — non-zero digits and the sandwiched zero are significant;
trailing zero in whole number is ambiguous. **Four certain, possibly five:**
8, 0 (sandwiched), 0 (sandwiched), 5. The final zero is uncertain.
$8.0050 \times 10^4$ would make five explicit; $8.005 \times 10^4$ makes four
explicit.

(f) $10.0$ — decimal point present, trailing zero is significant. **Three:**
1, 0, 0.

**Check.** The cleanest way to verify is to convert to scientific notation and
count the digits in the mantissa. They all agree with the counts above.

---

## 3.4 Arithmetic with Significant Figures

Different rules for addition/subtraction and multiplication/division.

### Multiplication and division: limit to the least significant figures

The result has as many significant figures as the **least precise input**.

$$3.724 \times 2.1 = 7.8204 \rightarrow \boxed{7.8}$$

The factor $2.1$ has two significant figures, so the product rounds to two.

$$\frac{186.4}{3.12} = 59.74... \rightarrow \boxed{59.7}$$

Both inputs have three significant figures; result rounds to three.

### Addition and subtraction: limit to the least significant decimal place

The result is limited by the input with the **fewest decimal places** — the
one that is least precise in absolute terms.

$$12.3 + 4.56 + 0.789 = 17.649 \rightarrow \boxed{17.6}$$

The first term, $12.3$, is only known to the tenths place, so the sum can
only be reported to the tenths place.

$$\underbrace{12.3}_{\text{tenths}} + \underbrace{4.56}_{\text{hundredths}} + \underbrace{0.789}_{\text{thousandths}} = 17.649 \rightarrow 17.6$$

$$1{,}283 - 276.8 = 1{,}006.2 \rightarrow \boxed{1{,}006}$$

$1{,}283$ is known only to the ones place (no decimal), so the result rounds
to the ones place.

### Why the rules differ

Multiplication and division produce a result whose *relative* uncertainty is
dominated by the least precise factor. Addition and subtraction produce a
result whose *absolute* uncertainty is dominated by the least precisely known
term.

You don't need to track through the uncertainty mathematics to use the rules —
but understanding that the rules are about *uncertainty propagation*, not
arbitrary convention, helps you apply them correctly when a situation seems
ambiguous.

> ---
> **Mentor's Margin**
>
> A common source of confusion: mixed operations. In a chain of calculations
> with both multiplication and addition, round only at the **end of the entire
> chain**, not after each individual step. We'll address this directly in §3.5.
> When the Handbook presents a multi-step example, it carries full precision
> through every intermediate step and rounds the final answer only.
>
> ---

### Worked Example 3 — Mixed Operations

**Given.** Calculate $(3.4 \times 10^3) + (8.52 \times 10^2) - (120)$, reporting the result
with appropriate significant figures.

**Solution.**

Step 1 — Convert to the same units for alignment:

$$3{,}400 + 852 - 120 = 4{,}132$$

Step 2 — Identify the limiting decimal places:

- $3{,}400$ is ambiguous without context. In an engineering calculation where
  this is a measurement, treat as known to the hundreds place (two significant
  figures in typical reading of $3.4 \times 10^3$). So least precise is the
  tens or hundreds place.
- For a clean illustration, if $3{,}400$ is known to the ones place (i.e.
  $3{,}400.$), then the least precise is $120$, known only to the tens place.
- Result rounds to the tens place: $4{,}132 \rightarrow \boxed{4{,}130}$

**Check.** Always more useful: state your assumptions clearly in a real
problem. Use scientific notation to eliminate the ambiguity rather than
guessing. $3.400 \times 10^3 + 8.52 \times 10^2 - 1.20 \times 10^2 =
4{,}132 \rightarrow 4{,}130$ (four sig figs). ✓

---

## 3.5 The Engineering Convention

The Handbook states this directly:

> *"In engineering calculations, the answer should generally be rounded to
> three or four significant figures."*

This convention reflects several practical facts:

- **Input data rarely justifies more.** Material properties from a datasheet,
  dimensions from a drawing, loads from a code — most of these are known to
  three or four digits. More digits in the answer claim more precision than the
  inputs had.
- **FE exam answers are separated enough to be found with three digits.** The
  distractors are not placed so close together that you need a fifth digit to
  distinguish them. If your answer doesn't match one of the choices to three
  or four significant figures, you've made a mistake — you haven't run out of
  digits.
- **Three to four digits are readable.** Seven-digit output from a calculator
  is not information when the inputs had three.

### What this means on exam day

Your answer should generally end up in **three to four significant figures**
before you compare it to the choices. If a choice requires five or six digits
to be unique, use more — but that's rare.

If the answer choices are, say, 147.3, 149.2, 151.8, and 155.0, and your
computation gives 151.847, you're selecting 151.8. If you'd rounded too early
and got 150, none of the choices would look right.

> ---
> **Mentor's Margin**
>
> The answer that is "close but not quite" is almost always an intermediate-
> rounding error. Not a setup error, not a wrong equation — just a round
> taken one step too early. If you've checked your setup and your equation and
> the answer still doesn't match, recompute carrying full precision through
> every step. This resolves the problem roughly half the time.
>
> ---

---

## 3.6 The Intermediate Rounding Problem

This is the section I asked you not to skip even if you tested out of Tier 1A.

Here is the failure mode, precisely described.

A problem requires four steps. You calculate step 1, round the result to three
significant figures, enter that rounded number into step 2, round again, enter
into step 3, and so on. Each rounding introduces a small error. Those small
errors **do not stay small** — they compound.

### A concrete case

**Given.** Compute $(1.256 \times 0.8834) \div 0.6214$.

**Correct:** Full precision throughout, round once at the end.

$$1.256 \times 0.8834 = 1.10939...$$
$$\frac{1.10939...}{0.6214} = 1.78536...$$
$$\boxed{1.785}$$

**Wrong:** Round after each step.

$$1.256 \times 0.8834 = 1.109 \quad\text{(rounded to 4 sig figs)}$$
$$\frac{1.109}{0.6214} = 1.785 \quad\text{(rounds to 4 sig figs)}$$

Happens to agree here. Now a case where it doesn't.

**Given.** Compute
$$\frac{(12.47 \times 0.0834)}{(0.7512 - 0.7481)}$$

**Correct:**

$$12.47 \times 0.0834 = 1.03996...$$
$$0.7512 - 0.7481 = 0.0031$$
$$\frac{1.03996}{0.0031} = 335.47... \approx \boxed{335}$$

**Wrong — round the subtraction first:**

$$0.7512 - 0.7481 = 0.003 \quad\text{(rounded to 1 sig fig)}$$
$$\frac{1.04}{0.003} = 347 \quad\text{(12 away from 335)}$$

That's a 3.5% error from a single premature rounding, and it produces a result
that wouldn't match any of the answer choices.

The denominator involves **catastrophic cancellation** — the subtraction of
two nearly equal numbers. A small absolute error in the difference becomes a
large relative error in the quotient. This pattern appears in beam deflection,
difference amplifiers, floating point computation, and thermodynamic
efficiency — anywhere two nearly equal quantities are subtracted and the
difference used in further arithmetic.

> ---
> **Mentor's Margin**
>
> **The rule is simple: carry full precision through every step and round
> exactly once, at the final answer.**
>
> In practice this means: don't write down intermediate results and re-enter
> them. Leave the full answer in your calculator's memory or in the expression,
> add the next operation, and continue. If you must write a number down to
> carry to the next step, write all the digits your calculator shows.
>
> This habit costs nothing — it's actually faster than rounding and re-
> entering — and it eliminates the entire class of intermediate-rounding
> errors.
>
> ---

### Catastrophic cancellation — the pattern to watch for

Whenever your calculation has the form:

$$\frac{\text{something}}{(\text{large number}) - (\text{large number close to the first})}$$

flag it before you compute. The denominator's absolute error is small, but its
*relative* error may be enormous after subtraction.

Examples that trigger this:

| Context | Subtraction | Danger |
|---|---|---|
| Beam deflection | $L^3 - (L-a)^3$ when $a \ll L$ | Large $L$, small difference |
| Thermal efficiency | $T_H - T_L$ when reservoirs are close | Temperatures nearly equal |
| Differential pressure | $p_1 - p_2$ when readings are close | Instrument precision matters |
| AC power | $P_{\text{in}} - P_{\text{loss}}$ in an efficient system | Small fraction of large |

In all of these, **carry maximum precision through the subtraction** and round
only after the division is complete.

---

## 3.7 Rounding Rules

When you do round, how you round matters.

**Standard rule (round half up):** If the digit to be dropped is less than 5,
round down. If it is 5 or more, round up.

$$3.745 \rightarrow 3.75 \quad (3 \text{ sig figs}) \qquad 3.744 \rightarrow 3.74$$

**Round half to even (banker's rounding):** When the digit to be dropped is
exactly 5 and nothing follows it, round to the nearest even digit. Reduces
accumulated bias over many roundings.

$$2.35 \rightarrow 2.4 \qquad 2.45 \rightarrow 2.4 \qquad 2.55 \rightarrow 2.6$$

The Handbook uses standard rounding. Banker's rounding appears in statistics
and computing. On the FE, use standard rounding unless told otherwise — the
choices will be separated enough that it doesn't matter.

### Worked Example 4 — Rounding a Multi-Step Problem

**Given.** A solid circular shaft of diameter $d = 38 \text{ mm}$ carries a
torque $T_q = 1{,}250 \text{ N} \cdot \text{m}$. The shear stress at the outer
surface is:

$$\tau = \frac{T_q \cdot c}{J}$$

where $c = d/2$ is the outer radius and $J = \pi d^4 / 32$ is the polar
moment of inertia. Find $\tau$ in MPa.

*(You'll see this equation in full context in Tier 2C. For now, treat it as an
exercise in not rounding early.)*

**Approach.** Set up and compute in one continuous chain. Round once at the
end.

**Solution.**

Step 1 — Compute $c$ in metres.

$$c = \frac{38}{2} = 19 \text{ mm} = 0.019 \text{ m}$$

Step 2 — Compute $J$, carrying full precision.

$$J = \frac{\pi (0.038)^4}{32}$$

Do not round $0.038^4$ partway. Keep the full value in the calculator:

$$0.038^4 = 2.08527... \times 10^{-6} \text{ m}^4$$

$$J = \frac{\pi \times 2.08527 \times 10^{-6}}{32} = \frac{6.55126 \times 10^{-6}}{32} = 2.04727 \times 10^{-7} \text{ m}^4$$

Step 3 — Compute $\tau$.

$$\tau = \frac{T_q \cdot c}{J} = \frac{(1{,}250)(0.019)}{2.04727 \times 10^{-7}}$$

Numerator: $(1{,}250)(0.019) = 23.75 \text{ N} \cdot \text{m}^2$

$$\tau = \frac{23.75}{2.04727 \times 10^{-7}} = 1.16005 \times 10^8 \text{ Pa}$$

Step 4 — Express and round at the end.

$$\tau = 116.0 \text{ MPa} \approx \boxed{116 \text{ MPa}}$$

**Check.** Order of magnitude: a torque of 1,250 N·m on a 38 mm shaft is a
fairly heavy loading, and 116 MPa is a plausible shear stress for a steel or
aluminium shaft. ✓

**What if you'd rounded $J$ prematurely?**

$$J_{\text{rounded}} \approx 2.05 \times 10^{-7} \text{ m}^4$$

$$\tau = \frac{23.75}{2.05 \times 10^{-7}} = 1.159 \times 10^8 \text{ Pa} = 115.9 \text{ MPa}$$

That rounds to 116 MPa — same answer, and you got lucky. But $d^4$ is a
fourth-power operation, and the relative error in $J$ from rounding $d$
earlier would be four times the relative error in $d$. On a longer calculation
with more steps, the accumulated error would not stay lucky.

> ---
> **Mentor's Margin**
>
> The shear stress example is forgiving because $d^4$ puts all the precision
> in one step and the other inputs are exact whole numbers. The catastrophic
> cancellation example in §3.6 is not forgiving at all. You cannot tell in
> advance which problems will be sensitive to intermediate rounding and which
> won't — so the rule is the same for all of them: **one rounding, at the
> end.**
>
> ---

---

## As the Handbook States It

> **Handbook 10.6, p. 2** — *Units and Conversion Factors*

The Handbook prints six rules for significant figures, then states:

> *"The engineering convention is that final results should be given to three
> or four significant figures."*

**The six rules, as stated in the Handbook:**

1. Non-zero digits are significant.
2. Zeros between significant figures are significant.
3. Zeros that are leading are not significant.
4. Zeros that follow a non-zero digit and are after the decimal point are
   significant.
5. Trailing zeros in a number without a decimal point may or may not be
   significant; use scientific notation to avoid ambiguity.
6. Exact numbers and defined constants have unlimited significant figures.

**Notation note.** The Handbook uses the phrase "significant figures"
consistently; some sources say "significant digits." They mean the same thing.

**What the Handbook does not include:**

- The intermediate-rounding problem
- Catastrophic cancellation
- The distinction between accuracy and precision
- The accuracy–precision–error framework

All of that is **memorize** material. It will be tested through problem
context rather than direct recall — you won't see "define accuracy" but you
will see problems where applying the wrong rounding practice produces a wrong
answer.

---

## Where This Goes Wrong

**Counting leading zeros as significant.** $0.0043$ has two significant
figures, not four or six. The zeros are placeholders. Convert to scientific
notation and count the mantissa digits if unsure.

**Forgetting that trailing zeros after a decimal are significant.** $3.400$
has four significant figures. Someone who writes $3.4$ when they measured
$3.400$ has discarded two digits of real information.

**Treating trailing zeros in a whole number as definite.** $1{,}300$ is
ambiguous. When reporting your own results, use scientific notation. When
reading someone else's, don't assume more precision than is explicit.

**Applying the multiplication rule to addition.** Three significant figures
plus three significant figures does not guarantee three in the sum — it
depends on decimal places. $1{,}230 + 4.56 = 1{,}234.56 \rightarrow 1{,}235$
(four significant figures, because $1{,}230$ is known to the ones place).

**Applying the addition rule to multiplication.** You must use the right rule
for the right operation.

**Rounding after each step.** The most expensive practical error in this
chapter, covered at length in §3.6. Round once, at the very end.

**Catastrophic cancellation blindness.** Seeing a subtraction of two nearly
equal numbers and not recognizing the hazard. The absolute error in the
difference may be small; the relative error may be enormous.

**Over-precision on a final answer.** Reporting $151.84729 \text{ MPa}$ when
your inputs had three significant figures is false precision. Three or four
digits for a final answer.

**Under-precision because of false modesty.** Rounding to one significant
figure "to be safe" throws away real information. If the inputs justify three
digits, give three.

**Confusing accuracy and precision.** These are different quantities and the
error analysis behind them is different. An instrument that is precise but
inaccurate needs calibration, not more measurements.

---

## Key Terms

| Term | Definition |
|---|---|
| Accuracy | How close a measurement is to the true value |
| Precision | How repeatable a measurement is; how tightly clustered repeated results are |
| Systematic error | A consistent offset in all measurements in the same direction; affects accuracy |
| Random error | Unpredictable scatter in repeated measurements; affects precision |
| Significant figures (sig figs) | The digits in a number that carry meaningful information about precision |
| Leading zeros | Zeros to the left of the first non-zero digit; never significant |
| Trailing zeros (after decimal) | Zeros at the right end of a decimal number; always significant |
| Trailing zeros (whole number) | Zeros at the right end of a whole number; ambiguous without a decimal point or scientific notation |
| Absolute error | $\lvert x_{meas} - x_{true} \rvert$; same units as the quantity |
| Relative error | Absolute error divided by the true value; dimensionless |
| Percent error | Relative error expressed as a percentage |
| Intermediate rounding | Rounding a result before it is used in the next step; causes compounding error |
| Catastrophic cancellation | Loss of significant figures when two nearly equal quantities are subtracted |
| Engineering convention | Reporting final results to three or four significant figures |
| Exact number | A defined or counted quantity with unlimited significant figures |

---

## Review Questions

### Conceptual

1. Explain the difference between accuracy and precision using your own
   example, not the dartboard.
2. Why does systematic error not improve with repeated measurements? What
   does improve with repeated measurements?
3. State the six Handbook rules for significant figures in your own words.
4. Why do addition/subtraction and multiplication/division have different
   significant figure rules? Explain the reason, not just the rules.
5. Explain catastrophic cancellation. Why is the relative error in a
   difference large when two nearly equal numbers are subtracted?
6. You are partway through a four-step calculation. Your intermediate result
   is $14.7329$. A colleague rounds this to $14.7$ before proceeding. You
   carry the full value. Who is more likely to match the correct answer
   choice, and why?
7. An instrument consistently reads 2% high. Is this a systematic error or
   a random error? Will taking the average of twenty readings fix it?
8. The Handbook says to report final answers to three or four significant
   figures. A calculation gives $78.43219$. What should you report?
9. What is the significant-figure status of the number in each position:
   (a) the zero in $10.4$, (b) the zeros in $0.0050$, (c) the zero in $3.05$?

### Calculation

10. State the number of significant figures in each:
    (a) $0.00360$
    (b) $5{,}300$
    (c) $5{,}300.$
    (d) $5.300 \times 10^3$
    (e) $1.0050$
    (f) $300{,}100$
    (g) $0.010$

11. Perform each calculation and round to the appropriate number of
    significant figures:
    (a) $3.61 \times 10^4 \times 1.8 \times 10^{-2}$
    (b) $\dfrac{4.728}{0.042}$
    (c) $18.34 + 5.2 + 0.846$
    (d) $1{,}280.0 - 976.3$
    (e) $(6.4 \times 10^3)(8.21 \times 10^{-2}) \div 1.8$
    (f) $14.82 + 0.003 - 5.7$

12. A gauge reads $58.3 \text{ psi}$. The true pressure is $61.0 \text{ psi}$.
    (a) Absolute error in psi.
    (b) Relative error.
    (c) Percent error.
    (d) Is this a measurement you'd trust for a system rated to 75 psi?
    Justify your answer quantitatively.

13. A micrometer reads $25.48 \text{ mm}$ for a shaft that is known to be
    $25.00 \text{ mm}$ in diameter.
    (a) Absolute error.
    (b) Percent error.
    (c) If this micrometer reads consistently high by the same amount, is
    this primarily systematic or random error?

14. Compute the following, **carrying full precision** and rounding only at
    the end:
    (a) $\dfrac{(3.216)(4.87)}{3.216 - 3.174}$
    (b) $\dfrac{(45.2)^2 \times 0.00381}{(45.2 - 44.6)}$

    Then recompute (a) and (b) rounding each intermediate result to three
    significant figures. Calculate the percent error introduced by the
    premature rounding.

15. A rectangular beam cross-section has width $b = 75 \text{ mm}$ and height
    $h = 120 \text{ mm}$. The moment of inertia is $I = bh^3/12$.
    (a) Compute $I$ in mm⁴, carrying full precision.
    (b) Express the result in m⁴.
    (c) How many significant figures are justified? Explain.

16. Five repeated measurements of a dimension give: $42.3$, $42.7$, $42.1$,
    $42.5$, $42.4$ mm. The true value is $43.0$ mm.
    (a) Compute the average of the five measurements.
    (b) Compute the absolute error of the average.
    (c) Compute the percent error of the average.
    (d) The measurements are close together but all less than the true value.
    What type of error dominates?

### Multiple Choice

17. Which of the following has exactly three significant figures?
    A) $0.00300$
    B) $3{,}000$
    C) $30{,}00$
    D) $300.0$

18. The result of $4.32 \times 2.7$ should be reported as:
    A) $11.664$
    B) $11.7$
    C) $12$
    D) $11.66$

19. The result of $136.4 + 2.08 + 0.004$ should be reported as:
    A) $138.484$
    B) $138.5$
    C) $138.48$
    D) $138$

20. An instrument that gives the same wrong reading every time has:
    A) High random error only
    B) High systematic error only
    C) High random error and high systematic error
    D) Neither systematic nor random error

21. Which of the following would introduce catastrophic cancellation?
    A) $1{,}253 \times 4.61$
    B) $1{,}253 + 4.61$
    C) $\dfrac{1{,}254.3 - 1{,}251.7}{0.435}$
    D) $\dfrac{1{,}253}{4.61}$

22. The number $0.05030$ has how many significant figures?
    A) Two
    B) Three
    C) Four
    D) Five

23. When should an intermediate result in a multi-step calculation be rounded?
    A) After each step, to three significant figures
    B) After each step, to four significant figures
    C) Never; carry full precision and round only the final answer
    D) Before the step that involves a subtraction

24. A measurement has a percent error of 1.5%. The true value is $200 \text{
    N}$. The absolute error is:
    A) $1.5 \text{ N}$
    B) $3.0 \text{ N}$
    C) $4.5 \text{ N}$
    D) $0.75 \text{ N}$

25. The engineering convention for a final answer is:
    A) As many digits as the calculator shows
    B) One significant figure for safety
    C) Three or four significant figures
    D) Exactly three significant figures, never four

---

## Answer Key with Explanations

**1.** Any valid example illustrating the two-by-two table. Example: a pressure
gauge calibrated correctly but with a loose needle that vibrates when read:
*precise* means the readings cluster tightly each time you tap the glass;
*accurate* means the cluster is at the true pressure. A stiff gauge with a
calibration error is *precise* (same reading every time) but *inaccurate*
(consistently wrong). (§3.1)

**2.** Systematic error is a consistent offset: every measurement is shifted
the same direction and roughly the same amount. Taking more measurements
doesn't change the average shift — the mean of twenty biased readings is just
as biased as one. **Random error** improves with repetition, because random
errors scatter around the true value and averaging tends to cancel them out.
(§3.1)

**3.** (1) Non-zero digits: always significant. (2) Zeros sandwiched between
non-zero digits: always significant. (3) Leading zeros: never significant —
they're placeholders. (4) Trailing zeros after a decimal point: always
significant — they're deliberately written. (5) Trailing zeros in a whole
number without a decimal point: ambiguous — use scientific notation. (6)
Exact numbers and defined constants: unlimited significant figures. (§3.3)

**4.** **Multiplication/division** propagates *relative* uncertainty —
multiplying a 1% uncertain value by a 2% uncertain value gives a roughly 2%
uncertain product. The result is limited by the input with the worst relative
precision: the fewest significant figures. **Addition/subtraction** propagates
*absolute* uncertainty — adding quantities shifts their absolute errors. The
result is limited by the input with the worst absolute precision: the fewest
decimal places. Different operations, different error propagation, different
rules. (§3.4)

**5.** When two nearly equal numbers are subtracted, their absolute errors
(which haven't changed) become a large fraction of the small result. Example:
$1{,}254.3 \pm 0.1$ minus $1{,}251.7 \pm 0.1$ gives $2.6 \pm 0.2$ — the
absolute error is unchanged at 0.1 for each term, but the relative error in
the result is $0.2/2.6 \approx 8\%$, whereas the inputs had relative errors of
$0.1/1{,}253 \approx 0.008\%$. The cancellation of the large parts leaves the
small errors dominant. (§3.6)

**6.** You are more likely to match. The colleague's early rounding introduced
an error that compounded through the remaining steps, particularly dangerous
if any step involves dividing by a small number. Full precision throughout
followed by one final rounding is guaranteed to minimize rounding error.
(§3.6)

**7.** **Systematic error.** A consistent 2%-high bias is the same direction
every time — a calibration offset. Averaging twenty readings gives a very
**precise** measurement of the wrong value, not a more accurate one. Accuracy
requires finding and correcting the calibration offset; taking more readings
does not help. (§3.1)

**8.** Three or four significant figures: $78.4$ (three sig figs) is the
appropriate answer. If the answer choices distinguish between $78.4$ and
$78.5$, report four: $78.43$. Reporting $78.43219$ claims more precision than
any standard engineering input justifies. (§3.5)

**9.**
(a) The zero in $10.4$ is sandwiched between non-zero digits — **significant**.
(b) The first zeros in $0.0050$ are leading — **not significant**. The final
zero is trailing after a decimal point — **significant**.
(c) The zero in $3.05$ is sandwiched — **significant**. (§3.3)

**10.**
(a) $0.00360$: leading zeros not significant, trailing zero after decimal
significant → **three**: 3, 6, 0.
(b) $5{,}300$: trailing zeros in whole number, no decimal → **ambiguous**; two
is the conservative reading.
(c) $5{,}300.$: decimal point present, all zeros significant → **four**.
(d) $5.300 \times 10^3$: mantissa has four digits → **four**.
(e) $1.0050$: all zeros significant (sandwiched and trailing after decimal) →
**five**.
(f) $300{,}100$: non-zero digits and sandwiched zero are significant; trailing
zero is ambiguous → **five certain**, possibly six.
(g) $0.010$: leading zero not significant, trailing zero after decimal
significant → **two**.

**11.**
(a) Mantissas: $3.61 \times 1.8 = 6.498$. Exponents: $4 + (-2) = 2$.
Result $= 6.498 \times 10^2$. Limiting: 2 sig figs (from 1.8).
$\boxed{6.5 \times 10^2}$

(b) $4.728 \div 0.042 = 112.57...$. Limiting: 2 sig figs (from 0.042).
$\boxed{110}$ or $1.1 \times 10^2$.

(c) Decimal-place rule. $18.34$ (hundredths), $5.2$ (tenths), $0.846$
(thousandths). Limiting: tenths from $5.2$. Sum $= 24.386 \rightarrow
\boxed{24.4}$

(d) $1{,}280.0 - 976.3 = 303.7$. Both to tenths → $\boxed{303.7}$.

(e) $(6.4 \times 10^3)(8.21 \times 10^{-2}) = 526.4$, then $\div 1.8 =
292.4...$. Limiting: 2 sig figs (from 6.4 and 1.8) → $\boxed{290}$ or $2.9
\times 10^2$.

(f) $14.82 + 0.003 - 5.7$. Tenths from $5.7$ is limiting. $= 9.123
\rightarrow \boxed{9.1}$.

**12.**
(a) $E_{abs} = \lvert 58.3 - 61.0 \rvert = \boxed{2.7 \text{ psi}}$

(b) $E_{rel} = 2.7/61.0 = \boxed{0.044}$

(c) $E_{\%} = 4.4\%$

(d) The gauge reads 4.4% low. For a system rated to 75 psi, 4.4% of 75 is
about 3.3 psi. If the operating pressure ever approached 75 psi, the gauge
would read about 71.7 psi — below the rated limit — while the actual pressure
had already reached 75 psi. Whether this is acceptable depends on the safety
margin, but a 4.4% offset is worth flagging for calibration. The quantitative
answer is: at the rated operating limit, the gauge would under-read by
$0.044 \times 75 \approx 3.3 \text{ psi}$.

**13.**
(a) $E_{abs} = \lvert 25.48 - 25.00 \rvert = \boxed{0.48 \text{ mm}}$

(b) $E_{\%} = \dfrac{0.48}{25.00} \times 100 = \boxed{1.92\%}$

(c) **Systematic error.** The offset is consistent: always 0.48 mm high. More
measurements will keep confirming $25.48 \pm$ noise, not averaging toward
25.00. (§3.1)

**14.**
**(a) Full precision:**

$3.216 - 3.174 = 0.042$ (exact, no rounding)

$$\frac{(3.216)(4.87)}{0.042} = \frac{15.66192}{0.042} = 372.9...$$

$$\boxed{373}$$

**(a) Rounded intermediates (3 sig figs):**

$(3.216)(4.87) = 15.7$ (3 sig figs), then $3.216 - 3.174 = 0.042$,
then $15.7/0.042 = 373.8... \approx 374$

Percent error: $\lvert(374 - 373)/373\rvert \times 100 = 0.27\%$. Small
here, because the subtraction happened to come out clean.

**(b) Full precision:**

$(45.2)^2 = 2{,}043.04$

$45.2 - 44.6 = 0.6$

$$\frac{2{,}043.04 \times 0.00381}{0.6} = \frac{7.78399}{0.6} = 12.97...$$

$$\boxed{13.0}$$

**(b) Rounded intermediates:**

$(45.2)^2 = 2{,}040$ (3 sig figs), then $2{,}040 \times 0.00381 = 7.77$,
denominator $0.6$, quotient $7.77/0.6 = 12.95 \approx 13.0$.

Percent error: $\lvert(12.95 - 12.97)/12.97\rvert \times 100 = 0.15\%$.

*Note:* Part (b) is also forgiving because the denominator ($0.6$) is not the
result of a near-cancellation. Part (a) is the one to watch — the denominator
$0.042$ came from subtracting $3.174$ from $3.216$, and even one premature
rounding of that subtraction could change the final answer materially.

**15.**
(a) $I = \dfrac{(75)(120)^3}{12} = \dfrac{75 \times 1{,}728{,}000}{12} = \dfrac{129{,}600{,}000}{12} = \boxed{10{,}800{,}000 \text{ mm}^4} = 1.08 \times 10^7 \text{ mm}^4$

(b) Converting: $(10^{-3})^4 = 10^{-12}$ m⁴/mm⁴:

$$1.08 \times 10^7 \times 10^{-12} = \boxed{1.08 \times 10^{-5} \text{ m}^4}$$

(c) The inputs $b = 75$ mm and $h = 120$ mm each have **two significant
figures** (both are exact whole numbers with no decimal, so most conservatively
two, though in context they might be three). The formula $h^3/12$ involves a
cube — the third power amplifies relative error. With inputs at two to three
significant figures, three significant figures in the result is justified.
The answer $1.08 \times 10^7$ has three, which is appropriate. (§3.5)

**16.**
(a) Average: $\dfrac{42.3 + 42.7 + 42.1 + 42.5 + 42.4}{5} = \dfrac{212.0}{5} = \boxed{42.4 \text{ mm}}$

(b) $E_{abs} = \lvert 42.4 - 43.0 \rvert = \boxed{0.6 \text{ mm}}$

(c) $E_{\%} = \dfrac{0.6}{43.0} \times 100 = \boxed{1.4\%}$

(d) **Systematic error dominates.** All five readings are below the true value
by amounts close to 0.6 mm. They are precise (clustered within ±0.3 mm of
each other) but consistently inaccurate (all on the same side). Random error
would scatter readings above and below the true value; this one-sided pattern
indicates a calibration offset. (§3.1)

**17. A — $0.00300$.**
(A) Leading zeros not significant, trailing zero after decimal significant →
three: 3, 0, 0. ✓
(B) $3{,}000$ — ambiguous, conservatively one or two.
(C) "$30{,}00$" is an unusual notation; if the comma is a decimal point (European
convention), it's $30.00$, which has four. As written with a US comma, it's the
same ambiguity as (B).
(D) $300.0$ has four significant figures: 3, 0, 0, 0. (§3.3)

**18. C — $12$.** $4.32 \times 2.7$: the factor $2.7$ has two significant
figures, so the product rounds to two. $4.32 \times 2.7 = 11.664$, rounded to
two sig figs is $12$

**19. B — $138.5$.**
$136.4 + 2.08 + 0.004 = 138.484$. The limiting term is $136.4$, known to the
tenths place. Sum rounds to tenths: $138.5$. (§3.4)

**20. B — High systematic error only.** "The same wrong reading every time"
means consistent offset (systematic), zero scatter (no random). (§3.1)

**21. C.** $\dfrac{1{,}254.3 - 1{,}251.7}{0.435}$ has a numerator that is the
difference of two nearly equal numbers: $1{,}254.3 - 1{,}251.7 = 2.6$. Small
absolute error in each input becomes large relative error in the difference.
(A), (B), and (D) have no cancellation. (§3.6)

**22. C — Four.** $0.05030$: leading zeros not significant (two of them),
non-zero 5 is significant, zero sandwiched between 5 and 3 is significant, 3
is significant, trailing zero after decimal is significant: **5, 0, 3, 0** —
four significant figures. (§3.3)

**23. C — Never; carry full precision and round only the final answer.** This
is the fundamental rule of §3.6. Early rounding compounds. (§3.6)

**24. B — $3.0 \text{ N}$.** Percent error is $1.5\%$, true value is $200$:

$$E_{abs} = \frac{1.5}{100} \times 200 = 3.0 \text{ N}$$

(§3.2)

**25. C — Three or four significant figures.** The Handbook states "three or
four." (D) is too restrictive — sometimes four is needed to distinguish among
close answer choices. (§3.5)

---

## Quick Reference

**Accuracy vs precision**

- **Accuracy:** closeness to the true value
- **Precision:** repeatability, tightness of clustering
- **Systematic error:** consistent offset; affects accuracy; doesn't improve
  with more measurements
- **Random error:** scatter; affects precision; does improve with averaging

**Error calculations**

$$E_{abs} = \lvert x_{meas} - x_{true} \rvert \qquad E_{rel} = \frac{E_{abs}}{x_{true}} \qquad E_{\%} = E_{rel} \times 100\%$$

**The six significant figure rules** — *Handbook p. 2*

| Rule | Status |
|---|---|
| Non-zero digits | Always significant |
| Zeros between non-zeros | Always significant |
| Leading zeros | Never significant |
| Trailing zeros after decimal | Always significant |
| Trailing zeros in whole number | **Ambiguous** — use scientific notation |
| Exact/defined numbers | Unlimited significant figures |

**Arithmetic rules**

- **Multiply/divide:** round to the number of sig figs in the least precise
  input
- **Add/subtract:** round to the fewest decimal places of any input

**The engineering convention** — *Handbook p. 2*

Final results: **three or four significant figures.**

**Intermediate rounding**

$$\boxed{\text{ONE rounding. At the final answer. Never before.}}$$

Carrying full precision costs nothing and eliminates an entire class of errors.

**Catastrophic cancellation**

Subtract two nearly equal numbers → small absolute error becomes large
relative error. Flag any calculation of the form:

$$\frac{\text{something}}{(\text{large}) - (\text{large, slightly smaller})}$$

Keep full precision through the subtraction.

**Not in the Handbook — memorize**

Accuracy vs precision · systematic vs random error · error formulas ·
intermediate rounding rule · catastrophic cancellation · the *reason* the
rules are what they are

---

## Tier 1A Review

Apprentice, that's Tier 1A. Three chapters:

**01-01** built your fluency across forty orders of magnitude.
**01-02** settled the pound problem — properly, in structural terms.
**01-03** gave you the reporting discipline that makes your results mean
something.

Before you move to Tier 1B, take the **Tier 1A Review Exam**. It's in
`appendices/review-exams/RE-1A-quantities-units-sigfigs.md`. Twenty
questions, fifty minutes. Every question maps back to a specific chapter
and section, so a wrong answer gives you an exact reading list.

If you score below the threshold listed there, go back to the sections
flagged by the wrong answers. Don't skim — reread and redo the problems.
The material in Tier 1B (algebra, geometry, vectors, matrices) assumes
everything in Tier 1A is solid, and a shaky foundation compounds.

If you pass, move on.

In **Chapter 01-04: Expressions, Equations, and Inequalities**, we start
Tier 1B. That's where the mathematics gets richer: manipulating expressions,
solving equations, working with inequalities — the mechanical fluency that
every subsequent chapter in the guide relies on.

You've done the hard foundation work. Now we build on it.

See you in Tier 1B.

— Your Mentor