---
chapter: "01-36"
title: "Measurement Uncertainty and Statistical Error Propagation"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-036-01, MATH-1D-036-02, MATH-1D-036-03, MATH-1D-036-04, MATH-1D-036-05, MATH-1D-036-06, MATH-1D-036-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-36: Measurement Uncertainty and Statistical Error Propagation

> *"An uncertainty calculation is not decoration added after the answer. It is
> part of the answer, because every calculated result inherits the uncertainty
> of the measurements used to produce it."*

---

## Before You Start

**Prerequisites:** [01-03 Accuracy, Precision, and Significant Figures](01-03-Accuracy-Precision-and-Significant-Figures.md) ·
[01-23 Partial Derivatives and Vector Calculus](01-23-Partial-Derivatives-and-Vector-Calculus.md) ·
[01-29 Random Variables and Probability Distributions](01-29-Random-Variables-and-Probability-Distributions.md) ·
[01-30 The Normal Distribution and the Central Limit Theorem](01-30-The-Normal-Distribution-and-the-Central-Limit-Theorem.md)

**Skip if:** You can distinguish measurement error from measurement uncertainty;
separate systematic and random disturbances conceptually; identify an output
sensitivity coefficient; apply the Kline–McClintock root-sum-square equation for
uncorrelated inputs; derive the relative uncertainty shortcut for power-law
models; distinguish statistical standard uncertainty from worst-case tolerance
propagation; convert standard uncertainty to expanded uncertainty using a stated
coverage factor; explain why repeated measurements reduce random averaging
uncertainty but do not automatically remove systematic bias; and report a
calculated result with an appropriate uncertainty statement.

**Time:** About 105–125 min reading and worked examples · 40–50 min review
questions · 70–85 min practice problems.

**Working convention:** This chapter uses $u_x$ for a standard uncertainty when
developing the method and translates that quantity to the Handbook's
$\sigma_x$ or $w_x$ notation where appropriate. An input tolerance, error bound,
and standard deviation are **not automatically interchangeable**.

---

## On the Board Today

Earlier chapters used two different ideas that can look deceptively similar.

Chapter 01-23 used a first-order **worst-case tolerance** estimate:

$$
\left|\Delta y\right|
\lesssim
\sum_i
\left|
\frac{\partial f}{\partial x_i}
\right|
\left|\Delta x_i\right|.
$$

That calculation assumes the input deviations may all push the output in their
worst possible directions at the same time.

The FE Reference Handbook gives a different model for **standard uncertainty**
when the input quantities are uncorrelated:

$$
\boxed{
u_y
=
\sqrt{
\sum_i
\left(
\frac{\partial f}{\partial x_i}u_{x_i}
\right)^2
}.
}
$$

The individual uncertainty contributions are squared, added, and square-rooted.

That is a root-sum-square calculation.

Neither formula is "more correct" in isolation.

The correct one depends on what the input numbers mean.

If the inputs are deterministic tolerance bounds, the worst-case sum may be the
appropriate engineering estimate.

If the inputs are standard uncertainties associated with uncorrelated random
quantities, the Handbook's root-sum-square structure is the relevant model.

This chapter is about choosing the model before pressing the calculator buttons.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **36.1** Distinguish measurement error, measurement uncertainty, accuracy, and precision
* **36.2** Interpret systematic and random measurement disturbances
* **36.3** Identify sensitivity coefficients for a calculated result
* **36.4** Apply the Kline–McClintock root-sum-square uncertainty equation for uncorrelated inputs
* **36.5** Derive and use relative uncertainty formulas for products and powers
* **36.6** Distinguish root-sum-square statistical propagation from worst-case tolerance propagation
* **36.7** Recognize when input correlation invalidates the uncorrelated-input formula
* **36.8** Compute expanded uncertainty from a standard uncertainty and coverage factor
* **36.9** Explain how repeated measurements affect random uncertainty of an average
* **36.10** Explain why repeated measurements do not automatically eliminate systematic error
* **36.11** Rank uncertainty contributors using sensitivity-weighted contributions
* **36.12** Report a measured or calculated result with units, uncertainty, and coverage information

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $x$ | measured quantity value | Handbook measurement-error model |
| $x_{\text{ref}}$ | reference quantity value | comparison value |
| $d_{\text{systematic}}$ | systematic disturbance | bias/drift-type contribution |
| $d_{\text{random}}$ | random disturbance | noise-type contribution |
| $y=f(x_1,\ldots,x_n)$ | calculated result | depends on measured inputs |
| $u_{x_i}$ | standard uncertainty of input $x_i$ | guide notation |
| $\sigma_{x_i}$ | standard deviation/standard uncertainty notation | Handbook probability/statistics form |
| $w_i$ | input uncertainty | Handbook instrumentation form |
| $c_i$ | sensitivity coefficient | $c_i=\partial f/\partial x_i$ |
| $u_y$ | combined standard uncertainty of $y$ | guide notation |
| $\sigma_y$ | standard uncertainty of output | Handbook probability/statistics notation |
| $w_R$ | uncertainty of calculated result $R$ | Handbook instrumentation notation |
| $k$ | coverage factor | Handbook notes $k=2$ is typically used for approximately 95% |
| $U$ | expanded uncertainty | $U=ku_y$ |
| $\bar x$ | average of repeated measurements | sample mean |
| $s$ | sample standard deviation | random scatter estimate |
| $s_{\bar x}$ | standard error of the mean | $s/\sqrt n$ |

**Notation translation.** The Handbook presents the same root-sum-square
sensitivity structure in two locations:

- printed p. 70 using standard deviations/standard uncertainties,
- printed p. 231 using measured values $x_i\pm w_i$ and calculated result
  uncertainty $w_R$.

---

## 36.1 Measurement Error Is Not Measurement Uncertainty

The Handbook defines **measurement error** as measured quantity value minus a
reference quantity value.

In symbols,

$$
\boxed{
e_x=x-x_{\text{ref}}.
}
$$

This is a signed difference.

If a reference voltage is exactly 10.000 V and the instrument reports 10.024 V,

$$
e_x
=
10.024-10.000
=
\boxed{+0.024\text{ V}}.
$$

The measurement is high relative to the reference.

### Measurement model

The Handbook models a measurement as

$$
\boxed{
x
=
x_{\text{ref}}
+
d_{\text{systematic}}
+
d_{\text{random}}.
}
$$

The two disturbance types serve different roles.

**Systematic disturbance** may arise from:

- calibration offset,
- drift,
- scale-factor error,
- consistent thermal bias.

**Random disturbance** may arise from:

- electrical noise,
- small uncontrolled fluctuations,
- repeatability variation.

### Measurement uncertainty

The Handbook defines measurement uncertainty as a quantitative estimate of the
range of values about the reported or measured value in which the true value is
believed to lie.

Uncertainty describes **how well the value is known**.

Error describes a difference from a reference.

A large uncertainty does not prove a large error.

A small observed error against one reference does not prove that future
measurements have negligible uncertainty.

### Accuracy and precision

On printed p. 231, the Handbook also distinguishes:

- **accuracy** — closeness of agreement between a measured value and a true
  quantity value,
- **precision** — closeness of agreement among replicate measurements under
  specified conditions.

Precision concerns repeatability.

Accuracy concerns closeness to truth/reference.

![FIG-01-36-001: Four-part measurement concept diagram. Panel 1 shows a reference value and a measured value separated by signed error e=x−xref. Panel 2 shows repeated measurements tightly grouped but offset from the reference, labeled precise but biased. Panel 3 shows wide random scatter centered near the reference, labeled low precision but little apparent bias. Panel 4 shows a reported result with an uncertainty interval. A footer distinguishes error, uncertainty, accuracy, and precision.](../figures/FIG-01-36-001-error-uncertainty-accuracy-precision.png)

### Worked Example 1 — Error and Uncertainty Are Different Statements

An instrument reports

$$
x=50.3\text{ kPa}
$$

against a reference of

$$
x_{\text{ref}}=50.0\text{ kPa}.
$$

The observed measurement error is

$$
e_x
=
50.3-50.0
=
\boxed{+0.3\text{ kPa}}.
$$

Suppose its calibrated measurement result is reported as

$$
50.3\pm0.5\text{ kPa}
$$

at a stated coverage level.

The numbers

$$
0.3\text{ kPa}
$$

and

$$
0.5\text{ kPa}
$$

answer different questions.

The first is a measured-reference difference.

The second describes the uncertainty assigned to the reported measurement.

---

## 36.2 Sensitivity Coefficients and the Kline–McClintock Equation

Suppose a calculated result depends on measured inputs:

$$
\boxed{
y=f(x_1,x_2,\ldots,x_n).
}
$$

A small change in input $x_i$ changes the output approximately according to the
partial derivative

$$
\boxed{
c_i
=
\frac{\partial f}{\partial x_i}.
}
$$

The quantity $c_i$ is a **sensitivity coefficient**.

Its units are

$$
\frac{\text{output units}}
{\text{input }i\text{ units}}.
$$

So

$$
c_i u_{x_i}
$$

has output units.

### Kline–McClintock equation

For uncorrelated input quantities, the Handbook gives the root-sum-square
uncertainty structure

$$
\boxed{
u_y
=
\sqrt{
\sum_{i=1}^{n}
\left(
c_i u_{x_i}
\right)^2
}.
}
$$

Equivalently,

$$
\boxed{
u_y
=
\sqrt{
\sum_{i=1}^{n}
\left[
\left(
\frac{\partial f}{\partial x_i}
\right)
u_{x_i}
\right]^2
}.
}
$$

The Handbook's p. 70 form uses standard deviations of the inputs.

Its p. 231 instrumentation form uses uncertainties $w_i$ and output uncertainty
$w_R$.

The calculation structure is the same.

![FIG-01-36-002: Kline-McClintock propagation diagram. Inputs x1, x2, x3 each have a standard uncertainty u_xi. Each passes through a sensitivity block c_i = partial f/partial x_i, producing output-unit contributions c_i u_xi. The contributions are squared, summed, and square-rooted to produce combined standard uncertainty u_y. A banner states "Handbook assumption: input quantities uncorrelated."](../figures/FIG-01-36-002-kline-mcclintock-rss.png)

### Worked Example 2 — Linear Combination

**Given.**

$$
y=3x_1-2x_2
$$

with uncorrelated standard uncertainties

$$
u_{x_1}=0.20,
\qquad
u_{x_2}=0.40.
$$

**Find.** $u_y$.

Sensitivity coefficients:

$$
c_1
=
\frac{\partial y}{\partial x_1}
=
3,
$$

$$
c_2
=
\frac{\partial y}{\partial x_2}
=
-2.
$$

Sensitivity-weighted contributions:

$$
c_1u_{x_1}
=
3(0.20)
=
0.60,
$$

$$
c_2u_{x_2}
=
-2(0.40)
=
-0.80.
$$

The signs disappear when squared:

$$
u_y
=
\sqrt{
(0.60)^2+(-0.80)^2
}
$$

$$
=
\sqrt{0.36+0.64}
=
\boxed{1.00}.
$$

**Check.** The two uncertainty contributions form a 0.6–0.8–1.0 right triangle.

### Why the sign disappears

A negative sensitivity means increasing the input moves the output downward.

That direction matters for deterministic changes.

But standard uncertainty measures spread.

Variance contributions are squared, so positive and negative sensitivities both
increase output uncertainty.

---

## 36.3 Products, Powers, and Relative Standard Uncertainty

Many engineering equations have the form

$$
\boxed{
y=Cx_1^{a_1}x_2^{a_2}\cdots x_n^{a_n}.
}
$$

For one input,

$$
\frac{\partial y}{\partial x_i}
=
a_i\frac{y}{x_i}.
$$

Therefore the sensitivity contribution is

$$
\left(
\frac{\partial y}{\partial x_i}
\right)u_{x_i}
=
a_i y\frac{u_{x_i}}{x_i}.
$$

Substitute into the root-sum-square equation:

$$
u_y
=
|y|
\sqrt{
\sum_i
\left(
a_i\frac{u_{x_i}}{x_i}
\right)^2
}.
$$

So the relative standard uncertainty is

$$
\boxed{
\frac{u_y}{|y|}
=
\sqrt{
\sum_i
\left(
a_i\frac{u_{x_i}}{x_i}
\right)^2
}.
}
$$

This is the statistical root-sum-square counterpart to the worst-case power-law
tolerance relation from Chapter 01-23.

![FIG-01-36-003: Power-law uncertainty diagram for y=C x^a z^b. Each input's relative uncertainty u_x/x and u_z/z is multiplied by the magnitude of its exponent, producing |a|u_x/x and |b|u_z/z. These are combined by root-sum-square to form u_y/|y|. A comparison strip shows statistical RSS beside the worst-case sum-of-magnitudes formula.](../figures/FIG-01-36-003-relative-power-law-uncertainty.png)

### Worked Example 3 — Cylinder Volume with Standard Uncertainties

**Given.**

$$
V=\pi r^2h
$$

with

$$
r=25.0\text{ mm},
\qquad
u_r=0.30\text{ mm},
$$

$$
h=80.0\text{ mm},
\qquad
u_h=0.50\text{ mm}.
$$

Assume the input uncertainties are standard uncertainties and are uncorrelated.

Nominal volume:

$$
V
=
\pi(25.0)^2(80.0)
=
157079.6\text{ mm}^3.
$$

Relative uncertainty:

$$
\frac{u_V}{V}
=
\sqrt{
\left(
2\frac{0.30}{25.0}
\right)^2
+
\left(
\frac{0.50}{80.0}
\right)^2
}.
$$

The two relative contributions are

$$
0.02400
$$

and

$$
0.00625.
$$

Therefore

$$
\frac{u_V}{V}
=
\sqrt{
0.024^2+0.00625^2
}
$$

$$
\approx
\boxed{0.02480}.
$$

So

$$
u_V
=
0.02480(157079.6)
\approx
\boxed{3896\text{ mm}^3}.
$$

A suitable standard-uncertainty report is approximately

$$
\boxed{
V=(157.1\pm3.9)\times10^3\text{ mm}^3
}
$$

with the statement that the quoted uncertainty is one combined standard
uncertainty under the uncorrelated-input model.

**Important.** If the numbers 0.30 mm and 0.50 mm were instead guaranteed
tolerance bounds, this statistical interpretation would not automatically be
valid.

---

## 36.4 Statistical RSS versus Worst-Case Tolerance Propagation

This distinction is central.

### Worst-case first-order propagation

For bounded input deviations,

$$
\boxed{
\Delta y_{\text{worst}}
\approx
\sum_i
\left|
c_i
\right|
\Delta x_i.
}
$$

This assumes contributions may align in the same adverse direction.

### Standard uncertainty propagation

For uncorrelated standard uncertainties,

$$
\boxed{
u_y
=
\sqrt{
\sum_i
(c_i u_{x_i})^2
}.
}
$$

The root-sum-square result is normally smaller than the sum of magnitudes when
multiple nonzero contributions are present.

### Worked Example 4 — Same Numbers, Different Meaning

Suppose two output contributions each have magnitude

$$
10.
$$

If they are worst-case bounds,

$$
\Delta y_{\text{worst}}
=
10+10
=
\boxed{20}.
$$

If they are uncorrelated one-standard-uncertainty contributions,

$$
u_y
=
\sqrt{10^2+10^2}
=
10\sqrt2
\approx
\boxed{14.14}.
$$

The difference did not come from algebra.

It came from the **meaning assigned to the inputs**.

![FIG-01-36-004: Side-by-side uncertainty-model comparison. Left: two bounded arrows can align in the same direction and are added as |c1|Δx1 + |c2|Δx2, labeled worst-case tolerance. Right: two uncorrelated standard-uncertainty components are shown as perpendicular axes and combined geometrically by root-sum-square. A warning states "do not choose the smaller formula merely because it is smaller."](../figures/FIG-01-36-004-worst-case-versus-rss.png)

### Input correlation

The Handbook's Kline–McClintock statement explicitly assumes the input
quantities are uncorrelated.

If two inputs are correlated, do **not** silently apply the uncorrelated
root-sum-square expression.

Correlation can make input deviations tend to move together or oppositely.

The supplied Handbook passage does not provide the general covariance form in
this section. When a problem provides correlation/covariance information, use the
model specified by that problem rather than pretending the uncorrelated formula
still applies.

### Worked Example 5 — Recognize an Invalid Assumption

A temperature-corrected length uses two quantities generated from the same sensor
record. Their uncertainties are known to be strongly correlated.

Question:

> May the Chapter 36 uncorrelated RSS equation be applied directly?

Answer:

$$
\boxed{\text{No.}}
$$

The Handbook condition for that equation has been violated.

The correct response is to use a correlation-aware model if one is supplied, or
state that the uncorrelated-input calculation is not justified.

---

## 36.5 Expanded Uncertainty and Coverage Factor

A combined standard uncertainty is a one-standard-uncertainty scale.

Engineering reports often communicate a wider interval called **expanded
uncertainty**:

$$
\boxed{
U=ku_y,
}
$$

where

$$
k
$$

is a coverage factor.

The Handbook states that expanded uncertainties are typically given at an
approximately 95% confidence level using

$$
\boxed{k=2}
$$

for a normal probability distribution.

For an ideal normal model,

$$
\pm2\sigma
$$

contains approximately 95.45% of the distribution, so the Handbook's "about
95%" wording is appropriate.

### Worked Example 6 — From Standard to Expanded Uncertainty

Suppose a calculated result is

$$
y=100.0
$$

with combined standard uncertainty

$$
u_y=1.5.
$$

Using

$$
k=2,
$$

expanded uncertainty is

$$
U
=
2(1.5)
=
\boxed{3.0}.
$$

Report:

$$
\boxed{
y=100.0\pm3.0
}
$$

with a note such as:

> expanded uncertainty $U=3.0$, using coverage factor $k=2$, approximately 95%
> under the stated normal-model assumption.

![FIG-01-36-005: Normal-distribution uncertainty reporting diagram. Center marks measured/calculated value y. Narrow interval ±u_y is labeled combined standard uncertainty. Wider interval ±2u_y is labeled expanded uncertainty U=ku_y with k=2 and approximately 95% coverage under a normal model. A reporting box includes value, units, U, k, and coverage statement.](../figures/FIG-01-36-005-expanded-uncertainty-coverage.png)

### Do not omit the coverage statement

The notation

$$
100\pm3
$$

is incomplete if the reader does not know whether 3 is:

- one standard deviation,
- a 95% expanded uncertainty,
- an instrument tolerance,
- a maximum error specification,
- or something else.

State the basis.

---

## 36.6 Repeated Measurements — What Averaging Does and Does Not Fix

Suppose repeated observations contain random scatter with sample standard
deviation

$$
s.
$$

The standard error of their mean is

$$
\boxed{
s_{\bar x}
=
\frac{s}{\sqrt n}.
}
$$

So averaging more independent repeated measurements reduces the random
uncertainty associated with the estimated mean.

### What averaging does not automatically remove

Suppose every reading contains a calibration offset of +0.5 units.

Taking 100 readings does not force that common offset to average to zero.

A systematic component may need:

- calibration correction,
- physical modeling,
- independent reference comparison,
- or a separately characterized uncertainty allowance.

The Handbook's measurement model

$$
x=x_{\text{ref}}+d_{\text{systematic}}+d_{\text{random}}
$$

is useful precisely because it prevents systematic and random disturbances from
being treated as the same thing.

![FIG-01-36-006: Repeated-measurement diagram. Left panel shows random scatter around a centered value; averaging n measurements narrows the uncertainty of the mean as s/sqrt(n). Right panel shows tightly clustered measurements all shifted from the reference by a systematic bias; increasing n narrows the cluster around the wrong center but does not remove the offset.](../figures/FIG-01-36-006-averaging-random-systematic.png)

### Worked Example 7 — Random Averaging plus a Systematic Uncertainty Component

A set of repeated measurements has random standard deviation

$$
s=0.80.
$$

There are

$$
n=16
$$

independent repeats.

The random standard uncertainty of the mean is

$$
u_{\text{rand}}
=
\frac{0.80}{\sqrt{16}}
=
\boxed{0.20}.
$$

Suppose a separate calibration analysis assigns an uncorrelated standard
uncertainty component

$$
u_{\text{cal}}=0.30.
$$

Then the combined standard uncertainty is

$$
u_c
=
\sqrt{
0.20^2+0.30^2
}
$$

$$
=
\sqrt{0.13}
\approx
\boxed{0.3606}.
$$

With

$$
k=2,
$$

$$
U
=
2(0.3606)
\approx
\boxed{0.721}.
$$

**Interpretation.** Increasing the number of repeated readings further reduces
the 0.20 random component, but it does not automatically reduce the 0.30
calibration component.

### Diminishing returns

As

$$
n\rightarrow\infty,
$$

the random averaging component approaches zero:

$$
\frac{s}{\sqrt n}\rightarrow0.
$$

But a nonzero independent calibration component sets a practical floor on the
combined uncertainty.

---

## 36.7 Uncertainty Budgets, Dominant Contributors, and Reporting

The combined variance-like quantity is

$$
u_y^2
=
\sum_i
(c_i u_{x_i})^2.
$$

This naturally creates an **uncertainty budget**.

Define the squared contribution from input $i$ as

$$
\boxed{
q_i=(c_i u_{x_i})^2.
}
$$

Then the fractional contribution to combined variance is

$$
\boxed{
\eta_i
=
\frac{q_i}
{\sum_j q_j}.
}
$$

The contributions satisfy

$$
\sum_i\eta_i=1.
$$

This helps identify which measurement improvement will reduce total uncertainty
most effectively.

### Worked Example 8 — Flow Rate Uncertainty Budget

Consider

$$
Q
=
\frac{\pi D^2}{4}v.
$$

Let

$$
D=0.150\text{ m},
\qquad
u_D=0.001\text{ m},
$$

$$
v=2.40\text{ m/s},
\qquad
u_v=0.05\text{ m/s},
$$

with uncorrelated standard uncertainties.

Nominal flow:

$$
Q
=
\frac{\pi(0.150)^2}{4}(2.40)
$$

$$
\approx
0.0424115\text{ m}^3/\text{s}.
$$

Relative diameter contribution:

$$
2\frac{u_D}{D}
=
2\frac{0.001}{0.150}
=
0.013333.
$$

Relative velocity contribution:

$$
\frac{u_v}{v}
=
\frac{0.05}{2.40}
=
0.020833.
$$

Combined relative standard uncertainty:

$$
\frac{u_Q}{Q}
=
\sqrt{
0.013333^2+0.020833^2
}
$$

$$
\approx
\boxed{0.02474}.
$$

Therefore

$$
u_Q
=
0.02474(0.0424115)
\approx
\boxed{0.001049\text{ m}^3/\text{s}}.
$$

Using

$$
k=2,
$$

$$
U
\approx
\boxed{0.00210\text{ m}^3/\text{s}}.
$$

So a reasonable expanded-uncertainty report is

$$
\boxed{
Q
=
0.0424
\pm
0.0021
\text{ m}^3/\text{s},
\quad
k=2.
}
$$

### Contribution ranking

Squared relative contributions:

$$
q_D
=
(0.013333)^2
\approx
0.00017778,
$$

$$
q_v
=
(0.020833)^2
\approx
0.00043403.
$$

Total:

$$
q_T
\approx
0.00061181.
$$

Shares:

$$
\eta_D
\approx
\boxed{29.1\%},
$$

$$
\eta_v
\approx
\boxed{70.9\%}.
$$

The velocity measurement dominates the statistical uncertainty budget.

Improving $v$ therefore produces the larger first-order reduction in combined
uncertainty.

![FIG-01-36-007: Uncertainty-budget figure for flow Q=(pi D^2/4)v. A sensitivity tree shows D weighted by exponent 2 and v weighted by exponent 1, then squared contributions combine by RSS. A bar or pie-style contribution graphic labels diameter about 29% and velocity about 71% of variance contribution. A final reporting box shows nominal Q, combined standard uncertainty, expanded uncertainty, k=2, and units.](../figures/FIG-01-36-007-uncertainty-budget-reporting.png)

### Reporting checklist

A defensible uncertainty statement should identify:

1. **the reported value,**
2. **units,**
3. **whether the quoted uncertainty is standard or expanded,**
4. **coverage factor $k$ if expanded,**
5. **important assumptions**, such as uncorrelated inputs,
6. **appropriate significant digits.**

A compact report might read:

> $Q=0.0424\pm0.0021\ \mathrm{m^3/s}$, expanded uncertainty with $k=2$,
> based on first-order propagation of uncorrelated input standard uncertainties.

That sentence tells the next engineer what the number means.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed p. 69 begins *Propagation of
> Error* and defines measurement error, systematic disturbance, random
> disturbance, and linear combinations. Printed p. 70 defines measurement
> uncertainty, gives the Kline–McClintock standard-uncertainty calculation for
> uncorrelated inputs, and states that expanded uncertainty is typically reported
> at approximately 95% with coverage factor $k=2$. Printed p. 231 repeats the
> measurement-uncertainty concept in the *Instrumentation, Measurement, and
> Control* section, defines measurement accuracy and precision, emphasizes
> reporting uncertainty with measurement results, and gives the same
> Kline–McClintock structure using $w_i$ and $w_R$ notation.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Propagation of Error / Measurement Error | 69 | Defines measurement error and models systematic and random disturbances |
| Linear Combinations | 69 | Points to variance/standard-deviation combination for random variables |
| Measurement Uncertainty | 70 | Defines uncertainty and states the Kline–McClintock uncorrelated-input method |
| Expanded Uncertainty | 70 | States approximately 95% reporting is typically associated with $k=2$ under a normal distribution |
| Measurement Accuracy | 231 | Defines closeness to a true quantity value |
| Measurement Precision | 231 | Defines agreement among replicate measurements under specified conditions |
| Instrumentation Measurement Uncertainty | 231 | Emphasizes reporting uncertainty and gives the $R=f(x_i)$ / $w_R$ Kline–McClintock form |

### Relationship to Chapter 01-23

Chapter 01-23 already introduced the partial-derivative machinery needed to
evaluate

$$
\frac{\partial f}{\partial x_i}.
$$

It also deliberately distinguished its **sum-of-magnitudes first-order tolerance
estimate** from the Handbook's **root-sum-square standard-uncertainty formula**.
That distinction is preserved here. fileciteturn163file7

### Material developed in this guide

The supplied Handbook gives the measurement model, uncertainty definition,
uncorrelated-input Kline–McClintock relation, and expanded-uncertainty statement.

This chapter develops the operational consequences:

- sensitivity-coefficient interpretation,
- the relative power-law RSS shortcut,
- explicit comparison with worst-case tolerance propagation,
- uncertainty-budget contribution ranking,
- averaging of independent random scatter through $s/\sqrt n$ using earlier
  statistics chapters,
- and a reporting checklist.

The supplied Handbook passage does **not** give a general covariance formula for
correlated inputs in this section. This chapter therefore does not silently
extend the Kline–McClintock equation to correlated quantities; it states that the
uncorrelated assumption has failed.

**Know without a lookup:**

- error and uncertainty are different,
- systematic and random disturbances are different,
- $c_i=\partial f/\partial x_i$,
- uncorrelated standard uncertainties combine by RSS after sensitivity weighting,
- worst-case bounds add magnitudes instead,
- $k=2$ means expanded uncertainty of about 95% under the stated normal model,
- repeated averaging reduces random standard error as $1/\sqrt n$,
- and every uncertainty report needs its basis stated.

---

## Where This Goes Wrong

**Calling uncertainty "error."** They are different quantities.

**Treating a signed calibration error as though it were a standard deviation.**

**Treating every tolerance as one standard uncertainty.** A manufacturing
tolerance, instrument accuracy specification, uniform bound, and standard
deviation are not automatically the same thing.

**Choosing RSS simply because it produces the smaller answer.**

**Choosing worst-case addition when the problem explicitly gives uncorrelated
standard uncertainties.**

**Forgetting the sensitivity coefficient.** Raw input uncertainties with
different units cannot simply be combined.

**Dropping the exponent in a power-law relation.** If

$$
y\propto x^2,
$$

the relative sensitivity contribution is approximately

$$
2u_x/x.
$$

**Keeping the sign of a sensitivity coefficient inside an RSS sum as though it
could cancel another uncertainty contribution.** Squaring removes the sign.

**Applying the uncorrelated-input formula to known correlated quantities.**

**Assuming repeated measurements remove systematic bias.**

**Using $s$ instead of $s/\sqrt n$ for uncertainty of an average.**

**Using $s/\sqrt n$ as though it were the uncertainty of an individual
measurement.**

**Multiplying by $k=2$ twice.** First compute the combined standard uncertainty,
then expand once.

**Saying $k=2$ always means exactly 95%.** The Handbook describes approximately
95% under a normal probability distribution.

**Reporting an uncertainty with no units.**

**Giving more decimal places in the result than the uncertainty supports.**

**Reporting "$x\pm U$" without stating whether $U$ is standard uncertainty,
expanded uncertainty, or a tolerance.**

**Ranking inputs by raw uncertainty alone.** Sensitivity weighting can reverse
the ranking.

---

## Key Terms

| Term | Definition |
|---|---|
| measurement error | measured quantity value minus a reference quantity value |
| measurement uncertainty | quantitative estimate describing the range associated with a reported/measured value |
| systematic disturbance | repeatable or structured measurement disturbance such as bias or drift |
| random disturbance | varying measurement disturbance such as noise |
| accuracy | closeness of a measured value to a true quantity value |
| precision | closeness of agreement among replicate measurements under specified conditions |
| measurand | quantity intended to be measured |
| sensitivity coefficient | partial derivative $\partial f/\partial x_i$ describing output sensitivity to an input |
| standard uncertainty | uncertainty expressed on a standard-deviation scale |
| combined standard uncertainty | root-sum-square combination of sensitivity-weighted standard uncertainties under the stated model |
| root-sum-square (RSS) | square root of the sum of squared contributions |
| Kline–McClintock equation | first-order uncertainty-propagation relation used by the Handbook for uncorrelated inputs |
| relative standard uncertainty | standard uncertainty divided by magnitude of the reported quantity |
| expanded uncertainty | standard uncertainty multiplied by a coverage factor |
| coverage factor | multiplier $k$ used to obtain expanded uncertainty |
| uncertainty budget | organized list of uncertainty components and their contributions |
| dominant contributor | uncertainty component responsible for the largest sensitivity-weighted contribution |
| standard error of the mean | random sampling uncertainty scale $s/\sqrt n$ |
| worst-case tolerance propagation | sum-of-magnitudes first-order bound assuming contributions may align adversely |
| uncorrelated inputs | input quantities with zero correlation under the propagation model |

---

## Review Questions

### Conceptual

1. Distinguish measurement error from measurement uncertainty.
2. Distinguish accuracy from precision.
3. What roles do $d_{\text{systematic}}$ and $d_{\text{random}}$ play in the Handbook measurement model?
4. What is a sensitivity coefficient?
5. Why do sensitivity-weighted uncertainty contributions have output units?
6. State the Handbook assumption required for the simple Kline–McClintock RSS formula.
7. Why does statistical RSS usually produce a smaller value than worst-case addition?
8. What does coverage factor $k$ do?
9. Why does repeated averaging not automatically remove systematic error?
10. Why should an uncertainty budget rank $c_i u_i$ contributions rather than raw $u_i$ values?

### Calculation

11. A measured value is 12.08 V and the reference is 12.00 V. Find the signed measurement error.
12. For $y=4x_1+3x_2$, with uncorrelated $u_{x_1}=0.20$ and $u_{x_2}=0.10$, find $u_y$.
13. For $y=x^2$, with $x=10.0$ and $u_x=0.20$, estimate the relative and absolute standard uncertainty of $y$.
14. For $y=xz$, with relative standard uncertainties 2% and 3%, uncorrelated, find the relative standard uncertainty of $y$.
15. Two sensitivity-weighted standard-uncertainty contributions are 6 and 8 output units. Find their RSS combination.
16. If the same 6 and 8 values are worst-case bounds, find the sum-of-magnitudes bound.
17. A combined standard uncertainty is 0.45 mm. Find expanded uncertainty using $k=2$.
18. Repeated measurements have $s=1.2$ units and $n=36$. Find the standard error of the mean.
19. An output uncertainty budget has squared contributions 9, 16, and 25. Find each percentage contribution.

### Multiple Choice

20. Measurement error is:
A) always a standard deviation  
B) measured value minus reference value  
C) always positive  
D) the same as expanded uncertainty.

21. The Handbook Kline–McClintock equation in this section assumes:
A) perfectly correlated inputs  
B) uncorrelated inputs  
C) zero measurement uncertainty  
D) identical units for all inputs.

22. A sensitivity coefficient is:
A) $\partial f/\partial x_i$  
B) $f/x_i$ always  
C) $u_i^2$  
D) the coverage factor.

23. Uncorrelated standard uncertainties combine through:
A) simple arithmetic mean  
B) root-sum-square after sensitivity weighting  
C) maximum only  
D) subtraction.

24. Worst-case bounded contributions are commonly combined by:
A) sum of magnitudes  
B) multiplying standard deviations  
C) taking their average  
D) ignoring the largest.

25. Expanded uncertainty is:
A) $u/k$  
B) $ku$  
C) $u^2$  
D) $1-u$.

26. For independent repeated random measurements, standard error of the mean scales as:
A) $\sqrt n$  
B) $n$  
C) $1/\sqrt n$  
D) $1/n^2$.

27. If two inputs are known to be strongly correlated, the uncorrelated-input RSS formula should:
A) be used unchanged  
B) be rejected unless a suitable correlation-aware model is supplied  
C) always be replaced by zero  
D) be multiplied by two.

---

## Answer Key with Explanations

### Conceptual

1. Measurement error is a difference between a measured value and reference
   value. Measurement uncertainty characterizes how well the reported value is
   known. (§36.1)

2. Accuracy concerns closeness to a true/reference value; precision concerns
   agreement among replicate measurements. (§36.1)

3. $d_{\text{systematic}}$ represents structured bias/drift-type disturbance;
   $d_{\text{random}}$ represents varying noise/scatter-type disturbance.
   (§36.1)

4. It is the local derivative

   $$
   c_i=\partial f/\partial x_i,
   $$

   describing how strongly the calculated output responds to input $i$.
   (§36.2)

5. $c_i$ has output-units/input-units, so multiplying by an input uncertainty
   produces output units. (§36.2)

6. The input quantities must be treated as **uncorrelated** for the Handbook's
   simple RSS form. (§36.2, §36.4)

7. Worst-case addition assumes adverse alignment of bounded contributions. RSS
   treats uncorrelated standard-uncertainty contributions statistically, so
   their squares rather than magnitudes are added. (§36.4)

8. It multiplies combined standard uncertainty to produce expanded uncertainty.
   (§36.5)

9. A common bias can be present in every repeated reading. Averaging reduces
   independent random scatter but need not reduce a systematic offset. (§36.6)

10. The effect of an input depends both on its uncertainty and on how sensitive
    the output is to that input. (§36.7)

### Calculation

11.

    $$
    e_x
    =
    12.08-12.00
    =
    \boxed{+0.08\text{ V}}.
    $$

12. Sensitivities:

    $$
    c_1=4,\qquad c_2=3.
    $$

    Therefore

    $$
    u_y
    =
    \sqrt{
    (4(0.20))^2+(3(0.10))^2
    }
    $$

    $$
    =
    \sqrt{0.64+0.09}
    =
    \sqrt{0.73}
    \approx
    \boxed{0.854}.
    $$

13.

    $$
    y=x^2=100.
    $$

    Relative standard uncertainty:

    $$
    \frac{u_y}{y}
    =
    2\frac{0.20}{10.0}
    =
    \boxed{0.040=4.0\%}.
    $$

    Absolute:

    $$
    u_y
    =
    0.04(100)
    =
    \boxed4.
    $$

14.

    $$
    \frac{u_y}{y}
    =
    \sqrt{
    (0.02)^2+(0.03)^2
    }
    $$

    $$
    =
    \sqrt{0.0013}
    \approx
    \boxed{0.0361=3.61\%}.
    $$

15.

    $$
    u
    =
    \sqrt{6^2+8^2}
    =
    \sqrt{100}
    =
    \boxed{10}.
    $$

16.

    $$
    \Delta_{\text{worst}}
    =
    6+8
    =
    \boxed{14}.
    $$

17.

    $$
    U
    =
    ku
    =
    2(0.45)
    =
    \boxed{0.90\text{ mm}}.
    $$

18.

    $$
    s_{\bar x}
    =
    \frac{1.2}{\sqrt{36}}
    =
    \frac{1.2}{6}
    =
    \boxed{0.20}.
    $$

19. Total squared contribution:

    $$
    9+16+25
    =
    50.
    $$

    Therefore:

    $$
    \frac9{50}=18\%,
    $$

    $$
    \frac{16}{50}=32\%,
    $$

    $$
    \frac{25}{50}=50\%.
    $$

    The shares are

    $$
    \boxed{18\%,\ 32\%,\ 50\%}.
    $$

### Multiple Choice

20. **B.** The Handbook defines measurement error as measured value minus
    reference value. (§36.1)

21. **B.** The stated Kline–McClintock equation assumes uncorrelated inputs.
    (§36.2)

22. **A.** $c_i=\partial f/\partial x_i$. (§36.2)

23. **B.** Square sensitivity-weighted contributions, add, then square-root.
    (§36.2)

24. **A.** Worst-case first-order bounds use the sum of magnitudes. (§36.4)

25. **B.** $U=ku$. (§36.5)

26. **C.** Standard error decreases as $1/\sqrt n$. (§36.6)

27. **B.** The Handbook equation's uncorrelated-input assumption has failed.
    (§36.4)

---

## Practice Problems

1. **Error versus uncertainty.** A calibrated reference is 100.00 °C. A sensor
   reads 99.72 °C and is reported with expanded uncertainty ±0.40 °C.
   Find the signed measurement error and explain why 0.28 °C and 0.40 °C are not
   interchangeable.

2. **Linear propagation.** Let
   $$R=2A-5B+0.5C.$$
   Uncorrelated standard uncertainties are
   $$u_A=0.30,\quad u_B=0.10,\quad u_C=0.80.$$
   Find $u_R$.

3. **Power-law propagation.** Electrical power is
   $$P=VI.$$
   If
   $$V=24.0\text{ V},\quad u_V=0.20\text{ V},$$
   $$I=3.00\text{ A},\quad u_I=0.05\text{ A},$$
   and the inputs are uncorrelated, find $P$, relative standard uncertainty,
   and $u_P$.

4. **Squared variable.** Area is
   $$A=\pi r^2.$$
   For
   $$r=50.0\text{ mm},\quad u_r=0.4\text{ mm},$$
   find the relative and absolute standard uncertainty of $A$.

5. **RSS versus worst case.** Three sensitivity-weighted contributions are
   2, 3, and 6 units.
   (a) Find the uncorrelated RSS standard uncertainty.
   (b) Find the worst-case sum-of-magnitudes bound.
   (c) Explain why the smaller answer is not automatically preferable.

6. **Expanded uncertainty.** A calculated mass flow is
   $$12.40\text{ kg/s}$$
   with combined standard uncertainty
   $$u=0.18\text{ kg/s}.$$
   Report expanded uncertainty using $k=2$ and write a complete compact result.

7. **Averaging.** Instrument readings have random sample standard deviation
   2.4 units.
   Find the standard error of the mean for
   (a) $n=4$,
   (b) $n=16$,
   (c) $n=100$.
   Describe the scaling.

8. **Random plus calibration uncertainty.** A mean has random standard error
   0.15 mm and independent calibration standard uncertainty 0.20 mm.
   Find combined standard uncertainty and expanded uncertainty for $k=2$.

9. **Uncertainty budget.** A result has sensitivity-weighted standard-uncertainty
   contributions 1.0, 2.0, and 4.0 units.
   Find total standard uncertainty and each contribution's percentage of the
   combined variance.

10. **Assumption check.** A model uses two values calculated from the same
    temperature sensor record, and their errors are known to rise and fall
    together. Explain why the simple uncorrelated Kline–McClintock equation is
    not justified and what information/model would be needed before combining
    them statistically.

---

## Practice Problem Solutions

1. Measurement error:

   $$
   e
   =
   99.72-100.00
   =
   \boxed{-0.28^\circ\text{C}}.
   $$

   The expanded uncertainty is

   $$
   \boxed{\pm0.40^\circ\text{C}}.
   $$

   The first is a signed observed difference from a reference. The second is an
   uncertainty statement around the reported measurement at its stated coverage
   basis. They describe different quantities.

2. Sensitivities:

   $$
   c_A=2,\qquad c_B=-5,\qquad c_C=0.5.
   $$

   Contributions:

   $$
   2(0.30)=0.60,
   $$

   $$
   -5(0.10)=-0.50,
   $$

   $$
   0.5(0.80)=0.40.
   $$

   Therefore

   $$
   u_R
   =
   \sqrt{
   0.60^2+(-0.50)^2+0.40^2
   }
   $$

   $$
   =
   \sqrt{0.36+0.25+0.16}
   =
   \sqrt{0.77}
   $$

   $$
   \boxed{
   u_R\approx0.877.
   }
   $$

3. Nominal power:

   $$
   P
   =
   VI
   =
   24.0(3.00)
   =
   \boxed{72.0\text{ W}}.
   $$

   Relative voltage uncertainty:

   $$
   \frac{0.20}{24.0}
   =
   0.008333.
   $$

   Relative current uncertainty:

   $$
   \frac{0.05}{3.00}
   =
   0.016667.
   $$

   Combined relative uncertainty:

   $$
   \frac{u_P}{P}
   =
   \sqrt{
   0.008333^2+0.016667^2
   }
   $$

   $$
   \approx
   \boxed{0.01863=1.863\%}.
   $$

   Therefore

   $$
   u_P
   =
   72.0(0.01863)
   \approx
   \boxed{1.34\text{ W}}.
   $$

4. Nominal area:

   $$
   A
   =
   \pi(50.0)^2
   =
   7853.98\text{ mm}^2.
   $$

   Relative uncertainty:

   $$
   \frac{u_A}{A}
   =
   2\frac{0.4}{50.0}
   =
   \boxed{0.0160=1.60\%}.
   $$

   Absolute uncertainty:

   $$
   u_A
   =
   0.0160(7853.98)
   \approx
   \boxed{125.7\text{ mm}^2}.
   $$

5. **(a) RSS**

   $$
   u
   =
   \sqrt{
   2^2+3^2+6^2
   }
   $$

   $$
   =
   \sqrt{49}
   =
   \boxed7.
   $$

   **(b) Worst-case**

   $$
   \Delta_{\text{worst}}
   =
   2+3+6
   =
   \boxed{11}.
   $$

   **(c)** The two values correspond to different input models. RSS is
   appropriate for the stated uncorrelated standard-uncertainty interpretation;
   worst-case addition is appropriate for bounded deviations that may align
   adversely. The formula is selected by meaning, not by desired size.

6.

   $$
   U
   =
   2(0.18)
   =
   \boxed{0.36\text{ kg/s}}.
   $$

   A compact report is

   $$
   \boxed{
   \dot m
   =
   12.40\pm0.36\text{ kg/s},
   \quad k=2
   }
   $$

   with approximately 95% coverage under the stated normal model.

7. **(a)**

   $$
   \frac{2.4}{\sqrt4}
   =
   \boxed{1.2}.
   $$

   **(b)**

   $$
   \frac{2.4}{\sqrt{16}}
   =
   \boxed{0.6}.
   $$

   **(c)**

   $$
   \frac{2.4}{\sqrt{100}}
   =
   \boxed{0.24}.
   $$

   Standard error scales as

   $$
   \boxed{1/\sqrt n}.
   $$

8.

   $$
   u_c
   =
   \sqrt{
   0.15^2+0.20^2
   }
   $$

   $$
   =
   \sqrt{0.0225+0.0400}
   =
   \sqrt{0.0625}
   =
   \boxed{0.25\text{ mm}}.
   $$

   Expanded:

   $$
   U
   =
   2(0.25)
   =
   \boxed{0.50\text{ mm}}.
   $$

9. Combined standard uncertainty:

   $$
   u
   =
   \sqrt{
   1^2+2^2+4^2
   }
   =
   \sqrt{21}
   \approx
   \boxed{4.583}.
   $$

   Squared contribution total:

   $$
   1+4+16
   =
   21.
   $$

   Shares:

   $$
   \frac1{21}
   \approx
   \boxed{4.76\%},
   $$

   $$
   \frac4{21}
   \approx
   \boxed{19.05\%},
   $$

   $$
   \frac{16}{21}
   \approx
   \boxed{76.19\%}.
   $$

10. The two inputs are correlated because their errors tend to move together.
    The Handbook's simple Kline–McClintock relation in this section assumes
    uncorrelated inputs, so direct RSS would omit the dependence between them.

    A valid statistical combination requires a model that includes the
    correlation/covariance information or another uncertainty model explicitly
    supplied for those linked quantities.

---

## Quick Reference

**Measurement error**

$$
\boxed{
e_x=x-x_{\text{ref}}
}
$$

**Handbook measurement model**

$$
\boxed{
x
=
x_{\text{ref}}
+
d_{\text{systematic}}
+
d_{\text{random}}
}
$$

**Calculated result**

$$
y=f(x_1,\ldots,x_n)
$$

**Sensitivity coefficient**

$$
\boxed{
c_i
=
\frac{\partial f}{\partial x_i}
}
$$

**Combined standard uncertainty — uncorrelated inputs**

$$
\boxed{
u_y
=
\sqrt{
\sum_i
(c_i u_{x_i})^2
}
}
$$

or

$$
\boxed{
u_y
=
\sqrt{
\sum_i
\left[
\left(
\frac{\partial f}{\partial x_i}
\right)
u_{x_i}
\right]^2
}.
}
$$

**Power-law relative standard uncertainty**

For

$$
y=C\prod_i x_i^{a_i},
$$

$$
\boxed{
\frac{u_y}{|y|}
=
\sqrt{
\sum_i
\left(
a_i\frac{u_{x_i}}{x_i}
\right)^2
}.
}
$$

**Worst-case first-order tolerance**

$$
\boxed{
\Delta y_{\text{worst}}
\approx
\sum_i
|c_i|\Delta x_i
}
$$

Do not interchange this with RSS without checking what the inputs mean.

**Expanded uncertainty**

$$
\boxed{
U=ku_y
}
$$

Handbook typical statement:

$$
\boxed{
k=2
\Rightarrow
\text{approximately 95% under a normal model}.
}
$$

**Random uncertainty of an average**

$$
\boxed{
s_{\bar x}
=
\frac{s}{\sqrt n}
}
$$

**Uncertainty-budget share**

$$
q_i=(c_i u_i)^2
$$

$$
\boxed{
\eta_i
=
\frac{q_i}{\sum_jq_j}.
}
$$

**Reporting**

value + units + uncertainty type + coverage factor/basis + important assumptions.

---

## What's Next

Measurement uncertainty completes the statistical measurement thread by linking
calculus sensitivity, probability, and instrumentation.

The remaining Layer 1 material now turns toward engineering decisions under
uncertainty.

**Chapter 01-37 — Expected Value, Decision Trees, and Risk** will develop:

- expected monetary or engineering value,
- chance and decision nodes,
- branch probabilities,
- rollback calculations,
- comparison of alternatives under uncertainty,
- expected loss and opportunity concepts,
- and the limits of expected value when consequences and risk tolerance matter.

The FE Reference Handbook includes expected-value decision trees in the
*Engineering Economics* section, and the Other Disciplines exam specification
explicitly names expected value and expected error in decision making.

Carry one distinction forward:

> Uncertainty propagation tells you how uncertain a calculated quantity is.
> Decision analysis asks what you should do when the possible outcomes and their
> probabilities are uncertain.

— Your Mentor
