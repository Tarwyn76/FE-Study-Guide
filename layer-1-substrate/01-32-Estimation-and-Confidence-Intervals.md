---
chapter: "01-32"
title: "Estimation and Confidence Intervals"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-032-01, MATH-1D-032-02, MATH-1D-032-03, MATH-1D-032-04, MATH-1D-032-05, MATH-1D-032-06, MATH-1D-032-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-32: Estimation and Confidence Intervals

> *"A point estimate tells you what the sample says. A confidence interval tells
> you how much uncertainty the sampling process leaves around that estimate."*

---

## Before You Start

**Prerequisites:** [01-30 The Normal Distribution and the Central Limit Theorem](01-30-The-Normal-Distribution-and-the-Central-Limit-Theorem.md) ·
[01-31 Sampling Distributions, Student's t, and Chi-Square](01-31-Sampling-Distributions-Students-t-and-Chi-Square.md)

**Skip if:** You can distinguish point estimates from interval estimates; interpret
a confidence level using repeated sampling; construct a confidence interval for a
population mean with known $\sigma$; switch correctly to Student's $t$ when
$\sigma$ is unknown; construct a confidence interval for the difference between
two means; construct a chi-square confidence interval for a normal-population
variance; convert that interval to one for standard deviation; compute margin of
error; and determine the required sample size for a specified mean-estimation
precision.

**Time:** About 110–130 min reading and worked examples · 40–50 min review
questions · 70–90 min practice problems.

**Working convention:** State the parameter before choosing a formula. Then state
what is known about population spread. A confidence interval is not just
"estimate ± a number"; its critical value, standard error, degrees of freedom,
and assumptions must all match the parameter being estimated.

---

## On the Board Today

A sample gives an estimate.

But two different samples from the same population will usually give different
estimates.

That is not a defect in sampling. It is the reason statistical inference exists.

Suppose a sample mean is

$$
\bar x=101.4.
$$

That number alone does not tell you whether the population mean is likely to be
101.3, 100.0, or 95.0.

You also need to know:

- how variable the observations are,
- how many observations were collected,
- which sampling distribution applies,
- and what confidence level you want.

A confidence interval combines those pieces.

The basic structure is

$$
\boxed{
\text{estimate}
\ \pm\
\text{critical value}
\times
\text{standard error}.
}
$$

That structure works directly for symmetric mean intervals.

Variance intervals look different because the chi-square distribution is
asymmetric, but the idea is the same: use the sampling distribution to determine
which population values remain compatible with the observed statistic at the
chosen confidence level.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **32.1** Distinguish point estimates, interval estimates, confidence level, and confidence coefficient
* **32.2** Interpret confidence intervals using repeated-sampling coverage rather than posterior probability language
* **32.3** Construct a confidence interval for a mean when population $\sigma$ is known
* **32.4** Construct a confidence interval for a mean when population $\sigma$ is unknown
* **32.5** Explain how confidence level, standard deviation, and sample size affect interval width
* **32.6** Construct confidence intervals for the difference between two independent means
* **32.7** Distinguish pooled and unequal-variance two-sample procedures
* **32.8** Construct a chi-square confidence interval for a normal-population variance
* **32.9** Convert a variance interval into a standard-deviation interval
* **32.10** Compute margin of error for a mean estimate
* **32.11** Determine required sample size for a specified margin of error when planning with a known or estimated $\sigma$
* **32.12** Select and check an interval procedure from the parameter, assumptions, and available information

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $\theta$ | generic population parameter | fixed but usually unknown |
| $\hat\theta$ | point estimator / point estimate | statistic used to estimate $\theta$ |
| $1-\alpha$ | confidence level | e.g. 0.95 |
| $\alpha$ | total probability outside a two-sided confidence region | split into two tails for symmetric intervals |
| $E$ | margin of error | half-width for symmetric intervals |
| $\bar X$ | sample mean statistic | random before sampling |
| $\bar x$ | observed sample mean | numerical result from one sample |
| $\mu$ | population mean | target parameter in mean intervals |
| $\sigma$ | population standard deviation | known in a $z$ interval |
| $s$ | sample standard deviation | used in a $t$ interval |
| $z_{\alpha/2}$ | standard-normal upper-tail critical value | leaves $\alpha/2$ to the right |
| $t_{\alpha/2,\nu}$ | Student's $t$ upper-tail critical value | $\nu$ degrees of freedom |
| $\chi^2_{\alpha,\nu}$ | chi-square upper-tail critical value | Handbook-style tail convention |
| $\nu$ | degrees of freedom | often $n-1$ |
| $n$ | sample size | positive integer |

**Notation warning.** In this guide, $z_{\alpha/2}$ and
$t_{\alpha/2,\nu}$ denote **upper-tail** critical values. For chi-square,
$\chi^2_{\alpha,\nu}$ also denotes an upper-tail critical value. This matters
when the two chi-square values are placed in the variance interval denominator.

---

## 32.1 Point Estimates, Interval Estimates, and Confidence Level

A **point estimate** is one numerical estimate of a population parameter.

Examples:

$$
\bar x
$$

estimates

$$
\mu,
$$

and

$$
s^2
$$

estimates

$$
\sigma^2.
$$

A point estimate is compact, but it hides sampling uncertainty.

An **interval estimate** reports a range of parameter values supported by the
sampling model at a stated confidence level.

### Confidence level

A confidence level is written

$$
\boxed{
1-\alpha.
}
$$

For a 95% confidence interval,

$$
1-\alpha=0.95
$$

so

$$
\alpha=0.05.
$$

For a symmetric two-sided normal or $t$ interval, the outside probability is
split:

$$
\frac{\alpha}{2}=0.025
$$

in each tail.

### The repeated-sampling meaning

A classical 95% confidence procedure is designed so that, under its assumptions,
about 95% of intervals constructed from repeated random samples in the same way
would contain the fixed population parameter.

Once one particular interval has been calculated, the population parameter is
not treated as randomly moving in and out of that interval.

So this statement is appropriate:

> "The method has 95% long-run coverage."

This common shorthand is acceptable when used carefully:

> "We are 95% confident that the interval captures $\mu$."

But this statement is not the classical frequentist interpretation:

> "There is a 95% probability that this fixed $\mu$ lies in this already
> calculated interval."

The probability statement belongs to the **procedure before sampling**, not to a
fixed parameter after the data are observed.

![FIG-01-32-001: Repeated-sampling confidence-interval illustration. A vertical line marks the fixed true parameter mu. Twenty horizontal sample intervals are stacked; most cross the vertical line while a few miss it. The intervals have different centers because the sample means differ. A caption states "confidence level describes long-run coverage of the interval procedure, not movement of the fixed parameter."](../figures/FIG-01-32-001-confidence-coverage.png)

### Worked Example 1 — Convert Confidence Level to Tail Area

**Given.** A two-sided 98% confidence interval is required.

**Find.** $\alpha$ and the probability in each tail.

**Solution.**

$$
1-\alpha=0.98
$$

so

$$
\alpha=0.02.
$$

Each tail contains

$$
\frac{\alpha}{2}
=
0.01.
$$

Therefore the required symmetric critical value is indexed by

$$
\boxed{
\alpha/2=0.01.
}
$$

For the standard normal distribution, the Handbook gives approximately

$$
z_{0.01}=2.3263.
$$

**Check.** A 98% interval must be wider than a 95% interval, so its critical
value must exceed 1.9600. It does.

---

## 32.2 Confidence Interval for a Mean — Population $\sigma$ Known

Suppose a population mean $\mu$ is unknown but the population standard deviation
$\sigma$ is known.

From Chapter 01-30,

$$
Z
=
\frac{\bar X-\mu}{\sigma/\sqrt n}
$$

has the standard normal distribution under the stated model.

For a central confidence level

$$
1-\alpha,
$$

the standard-normal probability statement is

$$
P\left(
-z_{\alpha/2}
\le
\frac{\bar X-\mu}{\sigma/\sqrt n}
\le
z_{\alpha/2}
\right)
=
1-\alpha.
$$

Solving the inequality for $\mu$ gives

$$
\boxed{
\bar X
-
z_{\alpha/2}\frac{\sigma}{\sqrt n}
\le
\mu
\le
\bar X
+
z_{\alpha/2}\frac{\sigma}{\sqrt n}.
}
$$

After sampling, use the observed $\bar x$:

$$
\boxed{
\mu:
\quad
\bar x
\pm
z_{\alpha/2}
\frac{\sigma}{\sqrt n}.
}
$$

### Margin of error

The half-width is

$$
\boxed{
E
=
z_{\alpha/2}
\frac{\sigma}{\sqrt n}.
}
$$

So the interval is simply

$$
\boxed{
\bar x\pm E.
}
$$

![FIG-01-32-002: Symmetric confidence-interval derivation for known sigma. Top panel shows a standard normal curve with central area 1−alpha between −z_(alpha/2) and +z_(alpha/2). Middle panel shows the standardized sample mean expression. Bottom panel maps the inequality back to engineering units, producing x-bar ± z_(alpha/2) sigma/sqrt(n). Margin of error E is labeled as the half-width.](../figures/FIG-01-32-002-z-confidence-interval.png)

### Worked Example 2 — Mean Interval with Known $\sigma$

**Given.**

A controlled process has known population standard deviation

$$
\sigma=12\text{ g}.
$$

A random sample of

$$
n=36
$$

containers has mean

$$
\bar x=503.0\text{ g}.
$$

**Find.** A 95% confidence interval for $\mu$.

**Approach.** Population $\sigma$ is known, so use a $z$ interval.

For 95% confidence,

$$
z_{0.025}=1.9600.
$$

Standard error:

$$
\frac{\sigma}{\sqrt n}
=
\frac{12}{6}
=
2\text{ g}.
$$

Margin of error:

$$
E
=
1.9600(2)
=
3.92\text{ g}.
$$

Therefore

$$
\mu:
\quad
503.0\pm3.92
$$

or

$$
\boxed{
499.08\text{ g}
\le
\mu
\le
506.92\text{ g}.
}
$$

**Check.** The interval is centered exactly on the sample mean 503.0 g and has
equal half-widths.

### What changes the width?

From

$$
E
=
z_{\alpha/2}
\frac{\sigma}{\sqrt n},
$$

the interval becomes wider when:

- confidence level increases,
- population variability $\sigma$ increases.

It becomes narrower when:

- sample size $n$ increases.

But sample size appears under a square root. Cutting the margin of error in half
requires approximately four times as many observations.

---

## 32.3 Confidence Interval for a Mean — Population $\sigma$ Unknown

When population $\sigma$ is unknown and estimated using sample standard deviation
$s$, use Student's $t$ distribution.

For the one-sample normal-population model developed in Chapter 01-31,

$$
T
=
\frac{\bar X-\mu}{s/\sqrt n}
$$

with

$$
\nu=n-1.
$$

Therefore the two-sided interval is

$$
\boxed{
\mu:
\quad
\bar x
\pm
t_{\alpha/2,n-1}
\frac{s}{\sqrt n}.
}
$$

Margin of error:

$$
\boxed{
E
=
t_{\alpha/2,n-1}
\frac{s}{\sqrt n}.
}
$$

The structure looks like the $z$ interval, but both the scale estimate and the
critical value have changed.

![FIG-01-32-003: Comparison of known-sigma z interval and unknown-sigma t interval at the same sample size and nominal confidence. Both are centered at x-bar. The t interval is shown wider for a modest sample because t_(alpha/2,nu) exceeds z_(alpha/2). A side panel lists the t workflow: compute s, set nu=n−1, obtain t critical value, compute s/sqrt(n), form x-bar ± t*SE.](../figures/FIG-01-32-003-t-confidence-interval.png)

### Worked Example 3 — Mean Interval with Unknown $\sigma$

**Given.**

A sample of

$$
n=10
$$

measurements has

$$
\bar x=52.4,
\qquad
s=3.0.
$$

Assume the one-sample $t$ model is appropriate.

**Find.** A 95% confidence interval for $\mu$.

**Solution.**

Degrees of freedom:

$$
\nu=10-1=9.
$$

From the Handbook $t$ table,

$$
t_{0.025,9}=2.262.
$$

Standard error:

$$
\frac{s}{\sqrt n}
=
\frac{3}{\sqrt{10}}
\approx
0.94868.
$$

Margin of error:

$$
E
=
2.262(0.94868)
\approx
2.146.
$$

Therefore

$$
\mu:
\quad
52.4\pm2.146
$$

or

$$
\boxed{
50.254
<
\mu
<
54.546.
}
$$

Rounded consistently with the input data,

$$
\boxed{
50.3
<
\mu
<
54.5.
}
$$

**Check.** The point estimate 52.4 lies at the interval center.

### Worked Example 4 — Why $t$ Is Wider Than $z$

Using the same sample standard error,

$$
SE=0.94868,
$$

compare a 95% $z$ interval with the correct 95% $t$ interval for $\nu=9$.

Normal critical value:

$$
z_{0.025}=1.960.
$$

Hypothetical $z$ margin:

$$
E_z
=
1.960(0.94868)
\approx
1.859.
$$

Correct $t$ margin:

$$
E_t
=
2.262(0.94868)
\approx
2.146.
$$

So

$$
\boxed{
E_t>E_z.
}
$$

The difference represents additional uncertainty from estimating population
spread using the finite sample.

As sample size increases, $t_{\alpha/2,\nu}$ approaches the normal critical
value and this difference shrinks.

> ---
> **Mentor's Margin**
>
> Do not choose $z$ because the sample is "large enough" until you have read the
> problem's assumptions. The first decision is whether population $\sigma$ is
> known. The sampling model and exam wording then determine whether a $z$ or
> $t$ procedure is intended.
>
> ---

---

## 32.4 Confidence Interval for the Difference Between Two Means

Sometimes the parameter of interest is not one population mean but the
difference

$$
\boxed{
\mu_1-\mu_2.
}
$$

The point estimate is

$$
\boxed{
\bar x_1-\bar x_2.
}
$$

### Population standard deviations known

For independent samples with known $\sigma_1$ and $\sigma_2$,

$$
\boxed{
(\mu_1-\mu_2):
\quad
(\bar x_1-\bar x_2)
\pm
z_{\alpha/2}
\sqrt{
\frac{\sigma_1^2}{n_1}
+
\frac{\sigma_2^2}{n_2}
}.
}
$$

### Population standard deviations unknown — equal-variance model

If the problem justifies a common population variance, use the pooled variance

$$
\boxed{
s_p^2
=
\frac{
(n_1-1)s_1^2
+
(n_2-1)s_2^2
}{
n_1+n_2-2
}
}
$$

with

$$
\boxed{
\nu=n_1+n_2-2.
}
$$

Then

$$
\boxed{
(\mu_1-\mu_2):
\quad
(\bar x_1-\bar x_2)
\pm
t_{\alpha/2,\nu}
s_p
\sqrt{
\frac{1}{n_1}+\frac{1}{n_2}
}.
}
$$

### Population standard deviations unknown — unequal-variance model

When equal variances are not assumed,

$$
\boxed{
SE
=
\sqrt{
\frac{s_1^2}{n_1}
+
\frac{s_2^2}{n_2}
}.
}
$$

A Welch-style degrees-of-freedom approximation is

$$
\boxed{
\nu
\approx
\frac{
\left(
s_1^2/n_1+s_2^2/n_2
\right)^2
}{
\frac{(s_1^2/n_1)^2}{n_1-1}
+
\frac{(s_2^2/n_2)^2}{n_2-1}
}.
}
$$

Then use

$$
(\bar x_1-\bar x_2)
\pm
t_{\alpha/2,\nu}SE.
$$

The Handbook presents both equal- and unequal-variance two-sample structures in
the same Engineering Probability and Statistics section.

![FIG-01-32-004: Two-sample confidence-interval decision diagram. Start with target parameter mu1−mu2. Branch: both population sigmas known -> z and SE=sqrt(sigma1²/n1+sigma2²/n2). If unknown, branch again: equal variances justified -> pooled sp and df=n1+n2−2; unequal variances -> unpooled SE and Welch degrees of freedom. All branches end at estimate difference ± critical value times SE.](../figures/FIG-01-32-004-two-mean-confidence-intervals.png)

### Worked Example 5 — Difference of Two Means with Known Spread

**Given.**

Two independent processes have known population standard deviations:

$$
\sigma_1=4,
\qquad
\sigma_2=6.
$$

Samples give

$$
\bar x_1=102,
\qquad
n_1=25,
$$

$$
\bar x_2=98,
\qquad
n_2=36.
$$

**Find.** A 95% confidence interval for

$$
\mu_1-\mu_2.
$$

**Solution.**

Point estimate:

$$
\bar x_1-\bar x_2
=
102-98
=
4.
$$

Standard error:

$$
SE
=
\sqrt{
\frac{4^2}{25}
+
\frac{6^2}{36}
}
$$

$$
=
\sqrt{
0.64+1
}
=
\sqrt{1.64}
\approx
1.2806.
$$

For 95% confidence,

$$
z_{0.025}=1.960.
$$

Margin of error:

$$
E
=
1.960(1.2806)
\approx
2.510.
$$

Therefore

$$
(\mu_1-\mu_2):
\quad
4\pm2.510
$$

or

$$
\boxed{
1.49
<
\mu_1-\mu_2
<
6.51.
}
$$

**Check.** Zero is not contained in this interval. The statistical implication of
that fact will be developed formally in the hypothesis-testing chapter.

---

## 32.5 Confidence Interval for a Normal-Population Variance

Mean intervals were symmetric because $z$ and $t$ are symmetric.

Variance intervals are different.

For a normal population,

$$
\frac{(n-1)S^2}{\sigma^2}
\sim
\chi^2_{\nu},
\qquad
\nu=n-1.
$$

Using the Handbook's **upper-tail** notation, a two-sided
$100(1-\alpha)\%$ confidence interval for population variance is

$$
\boxed{
\frac{(n-1)s^2}
{\chi^2_{\alpha/2,\nu}}
<
\sigma^2
<
\frac{(n-1)s^2}
{\chi^2_{1-\alpha/2,\nu}}.
}
$$

Notice the denominator ordering:

- $\chi^2_{\alpha/2,\nu}$ is the **large** upper critical value and produces the
  lower variance endpoint,
- $\chi^2_{1-\alpha/2,\nu}$ is the **small** critical value and produces the
  upper variance endpoint.

The interval is generally asymmetric.

### Standard-deviation interval

Because square root is increasing for positive values, take square roots of both
variance endpoints:

$$
\boxed{
\sqrt{L_{\sigma^2}}
<
\sigma
<
\sqrt{U_{\sigma^2}}.
}
$$

![FIG-01-32-005: Asymmetric chi-square confidence-interval construction. A right-skewed chi-square curve shows alpha/2 in each tail with lower critical value chi²_(1−alpha/2,nu) and upper critical value chi²_(alpha/2,nu). Arrows show inversion when solving for sigma²: the large chi-square denominator creates the lower variance bound, and the small denominator creates the upper bound.](../figures/FIG-01-32-005-variance-confidence-interval.png)

### Worked Example 6 — Variance and Standard-Deviation Interval

**Given.**

A normal-population sample has

$$
n=10
$$

and

$$
s^2=4.00.
$$

**Find.** A 95% confidence interval for $\sigma^2$ and for $\sigma$.

**Solution.**

Degrees of freedom:

$$
\nu=9.
$$

For 95% confidence,

$$
\alpha=0.05,
\qquad
\frac{\alpha}{2}=0.025.
$$

From the chi-square table for $\nu=9$,

$$
\chi^2_{0.025,9}
\approx
19.0228,
$$

and

$$
\chi^2_{0.975,9}
\approx
2.7004.
$$

Numerator:

$$
(n-1)s^2
=
9(4)
=
36.
$$

Lower variance bound:

$$
L
=
\frac{36}{19.0228}
\approx
1.8925.
$$

Upper variance bound:

$$
U
=
\frac{36}{2.7004}
\approx
13.331.
$$

Therefore

$$
\boxed{
1.89
<
\sigma^2
<
13.33.
}
$$

For population standard deviation:

$$
\sqrt{1.8925}
\approx
1.3757,
$$

$$
\sqrt{13.331}
\approx
3.6512.
$$

So

$$
\boxed{
1.38
<
\sigma
<
3.65.
}
$$

**Check.** The interval is not symmetric about $s^2=4$. That is expected because
the chi-square distribution is not symmetric.

### Assumption warning

The exact chi-square variance interval depends strongly on the normal-population
model.

Do not assume the Central Limit Theorem automatically repairs a strongly
nonnormal variance problem.

---

## 32.6 Margin of Error and Sample-Size Planning

For a known-$\sigma$ mean interval,

$$
E
=
z_{\alpha/2}
\frac{\sigma}{\sqrt n}.
$$

If a required margin of error $E$ is specified, solve for $n$:

$$
E\sqrt n
=
z_{\alpha/2}\sigma,
$$

$$
\sqrt n
=
\frac{z_{\alpha/2}\sigma}{E},
$$

so

$$
\boxed{
n
=
\left(
\frac{z_{\alpha/2}\sigma}{E}
\right)^2.
}
$$

Because sample size must be an integer and insufficient sample size fails the
precision requirement,

$$
\boxed{\text{always round }n\text{ upward}.}
$$

Even if the calculation gives

$$
n=96.02,
$$

you need

$$
n=97.
$$

### If $\sigma$ is not known during planning

A planning value may come from:

- prior validated process data,
- a pilot sample,
- a conservative engineering estimate.

If $s$ from a small pilot is substituted for $\sigma$, the result is a planning
approximation, not a guarantee.

An exact $t$-based sample-size calculation is iterative because the critical
$t$ value depends on

$$
\nu=n-1,
$$

which depends on the very sample size being chosen.

For FE-scale planning questions, use the formula and assumptions supplied by the
problem.

![FIG-01-32-006: Margin-of-error and sample-size design figure. Left panel shows E=z sigma/sqrt(n) and arrows: higher confidence -> larger E, larger sigma -> larger E, larger n -> smaller E. Right panel rearranges to n=(z sigma/E)^2 and shows an example calculated n=96.04 being rounded upward to 97. A small curve shows diminishing returns: interval width falls with 1/sqrt(n).](../figures/FIG-01-32-006-margin-error-sample-size.png)

### Worked Example 7 — Required Sample Size

**Given.**

A process has planning standard deviation

$$
\sigma=12\text{ g}.
$$

You want a 95% confidence interval for the mean with margin of error no greater
than

$$
E=3\text{ g}.
$$

**Find.** Required sample size.

**Solution.**

For 95% confidence,

$$
z_{0.025}=1.960.
$$

Then

$$
n
=
\left(
\frac{1.960(12)}{3}
\right)^2
$$

$$
=
(7.84)^2
=
61.4656.
$$

Round upward:

$$
\boxed{n=62}.
$$

**Check.** Using 61 instead would make the margin slightly larger than the design
target.

### Worked Example 8 — Sample Size and Diminishing Returns

Suppose all else is unchanged and the current sample size is

$$
n=25.
$$

If the sample size is increased to

$$
n=100,
$$

then

$$
\frac{E_{100}}{E_{25}}
=
\frac{1/\sqrt{100}}{1/\sqrt{25}}
=
\frac{1/10}{1/5}
=
\frac12.
$$

So quadrupling the sample size halves the margin of error.

To reduce margin by a factor of 10 requires approximately 100 times as many
observations.

That square-root law is one of the most important practical realities of sampling
design.

---

## 32.7 Selecting and Checking the Interval

A confidence-interval problem should be classified before any arithmetic.

### Step 1 — Identify the parameter

Is the target:

- one mean $\mu$,
- difference of means $\mu_1-\mu_2$,
- one variance $\sigma^2$,
- one standard deviation $\sigma$?

### Step 2 — Identify what is known

For a mean:

- known population $\sigma$ → $z$,
- unknown population $\sigma$, estimated by $s$ → $t$ under the stated model.

For a variance:

- normal-population variance inference → chi-square.

### Step 3 — Identify the confidence level

Convert

$$
1-\alpha
$$

to

$$
\alpha
$$

and then to

$$
\alpha/2
$$

for a two-sided interval.

### Step 4 — Compute the standard error or pivot

Mean intervals use a standard error.

Variance intervals use the chi-square pivot.

### Step 5 — Check the result

Useful checks include:

- interval is centered at the point estimate when the reference distribution and
  construction are symmetric,
- higher confidence produces a wider interval,
- larger $n$ narrows a mean interval,
- variance limits are positive,
- chi-square variance limits need not be symmetric,
- all units match the parameter being estimated.

![FIG-01-32-007: Confidence-interval selection flowchart. Start: "What parameter?" Mean -> "one or two samples?" One sample -> "population sigma known?" yes -> z interval; no -> t interval with df=n−1. Two samples -> known sigmas -> z difference interval; unknown -> pooled or unequal-variance t depending assumptions. Variance/standard deviation -> chi-square interval with normal-population assumption. Final box: check confidence level, tail split, units, interval direction, and assumptions.](../figures/FIG-01-32-007-confidence-interval-selection.png)

### Worked Example 9 — Choose the Procedure

Identify the appropriate interval family.

**(a)** Estimate one process mean from $n=40$ when a validated long-run
population $\sigma$ is given.

Use:

$$
\boxed{\text{one-sample }z\text{ interval}.}
$$

**(b)** Estimate one mean from $n=12$, with population $\sigma$ unknown and the
sample standard deviation supplied, under a normal model.

Use:

$$
\boxed{\text{one-sample }t\text{ interval},\quad \nu=11.}
$$

**(c)** Estimate the variance of a normal process from one sample.

Use:

$$
\boxed{\chi^2\text{ interval}.}
$$

**(d)** Estimate $\mu_1-\mu_2$ from two independent samples with known
$\sigma_1$ and $\sigma_2$.

Use:

$$
\boxed{\text{two-sample }z\text{ interval}.}
$$

### Interpretation discipline

An interval that excludes zero for a difference of means or excludes a benchmark
value for a mean is suggestive of a corresponding two-sided test result.

But do not skip ahead.

Formal hypothesis testing requires:

- an explicit null hypothesis,
- an alternative,
- a significance level,
- a test statistic,
- a rejection criterion or p-value,
- and a decision stated in context.

That is the next chapter.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed p. 75 begins the section
> *Confidence Intervals, Sample Distributions and Sample Size* and the
> confidence interval for the mean of a normal distribution. Printed p. 76
> gives confidence intervals for the difference between two means, confidence
> intervals for the variance of a normal distribution, sample-size material,
> test-statistic definitions, and a table of common $Z_{\alpha/2}$ values.
> Printed pp. 77, 78, and 80 supply the normal, Student's $t$, and chi-square
> critical-value tables used by these procedures.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Confidence interval for mean of a normal distribution | 75 | Distinguishes known-spread and sample-estimated-spread cases |
| Confidence interval for difference between two means | 76 | Gives known-variance and unknown-variance structures |
| Confidence interval for variance of a normal distribution | 76 | Uses chi-square critical values |
| Sample size | 75–76 | Places sample-size planning with confidence-interval and inferential material |
| Test-statistic definitions | 76 | Distinguishes normal $Z$ and sample-based $t$ statistics |
| Common $Z_{\alpha/2}$ values | 76 | Lists 80%, 90%, 95%, 96%, 98%, and 99% critical values |
| Unit Normal Distribution | 77 | Supplies normal critical areas/fractiles |
| Student's $t$ table | 78 | Supplies $t_{\alpha,\nu}$ values |
| Chi-square table | 80 | Supplies upper-tail $\chi^2_{\alpha,\nu}$ values |

### Common Handbook $Z_{\alpha/2}$ values

| Confidence level | $Z_{\alpha/2}$ |
|---:|---:|
| 80% | 1.2816 |
| 90% | 1.6449 |
| 95% | 1.9600 |
| 96% | 2.0537 |
| 98% | 2.3263 |
| 99% | 2.5758 |

### Guide-developed interpretation

The repeated-sampling interpretation of confidence level, the explicit
"estimate ± critical value × standard error" organizing template, and the
square-root explanation of diminishing returns in sample size are developed here
to make the Handbook formulas operational.

The known-$\sigma$ planning relation

$$
n
=
\left(
\frac{z_{\alpha/2}\sigma}{E}
\right)^2
$$

follows algebraically from the known-$\sigma$ margin-of-error expression. When
the problem does not provide a known planning $\sigma$, the source of the
planning spread estimate must be stated.

**Know without a lookup:**

- confidence level $=1-\alpha$,
- two-sided symmetric intervals split $\alpha/2$ into each tail,
- known $\sigma$ → $z$,
- unknown $\sigma$ estimated by $s$ → $t$,
- variance → chi-square under the normal-population model,
- mean-interval width decreases as $1/\sqrt n$,
- and required sample size is rounded upward.

---

## Where This Goes Wrong

**Treating the point estimate as the parameter.** $\bar x$ estimates $\mu$; it
does not become $\mu$.

**Saying a classical 95% interval gives a 95% posterior probability that the
fixed parameter is inside the realized interval.** The 95% belongs to the
long-run coverage of the procedure.

**Using $\alpha$ instead of $\alpha/2$ for a two-sided interval.**

**Using $z$ when $\sigma$ is unknown and the intended procedure is $t$.**

**Using $s$ in the formula but a normal critical value from the $z$ table.**

**Forgetting degrees of freedom in a $t$ interval.**

**Using a one-sided critical value for a two-sided confidence interval.**

**Comparing intervals only by their confidence level.** Width also depends on
sample size and variability.

**Assuming a higher confidence interval is more precise.** Higher confidence,
with the same data, produces a wider interval.

**Assuming a narrower interval is always better.** An artificially narrow
interval caused by the wrong standard error or wrong critical value is not more
informative; it is incorrect.

**Adding two standard errors directly.** Independent mean differences combine
variances under the square root.

**Pooling two sample variances without an equal-variance assumption.**

**Using the unequal-variance degrees of freedom as simply $n_1+n_2-2$.**
That degree-of-freedom formula belongs to the pooled equal-variance model.

**Putting chi-square critical values in the wrong denominator positions.**
With upper-tail notation, the large $\chi^2_{\alpha/2,\nu}$ goes in the lower
variance bound.

**Expecting a chi-square variance interval to be symmetric.**

**Reporting a standard-deviation interval without square-rooting the variance
limits.**

**Rounding required sample size downward.** Always round up.

**Claiming that quadrupling sample size quarters the margin of error.**
It halves it because precision scales with $1/\sqrt n$.

**Ignoring units.** A mean interval has the original units; a variance interval
has squared units.

---

## Key Terms

| Term | Definition |
|---|---|
| point estimate | single sample-based estimate of a population parameter |
| interval estimate | range of parameter values produced by an inferential procedure |
| confidence interval | interval generated by a procedure with stated long-run coverage under its assumptions |
| confidence level | long-run coverage probability $1-\alpha$ |
| confidence coefficient | numerical value $1-\alpha$ |
| significance complement | total outside probability $\alpha$ associated with a confidence level |
| margin of error | symmetric confidence-interval half-width |
| critical value | reference-distribution cutoff associated with a specified tail probability |
| standard error | standard deviation of an estimator's sampling distribution |
| one-sample interval | confidence interval based on one sample |
| two-sample interval | confidence interval for a relationship such as $\mu_1-\mu_2$ |
| pooled variance | weighted estimate of a common variance from two samples |
| unequal-variance procedure | two-sample method that does not assume a common population variance |
| Welch degrees of freedom | approximate df used for unequal-variance two-sample $t$ inference |
| variance interval | confidence interval for population variance $\sigma^2$ |
| standard-deviation interval | square-root transformation of a variance confidence interval |
| sample-size planning | choosing $n$ to meet a stated precision or inferential requirement |
| coverage | long-run fraction of intervals from a procedure that contain the target parameter |

---

## Review Questions

### Conceptual

1. Distinguish a point estimate from an interval estimate.
2. What does a 95% confidence level mean under repeated sampling?
3. Why is $\alpha/2$ used in each tail of a symmetric two-sided interval?
4. When is a $z$ confidence interval for a mean appropriate?
5. Why does an unknown population $\sigma$ lead to a $t$ interval?
6. What happens to interval width when confidence level increases but the data stay fixed?
7. What happens to a mean interval's margin of error when sample size is quadrupled?
8. Why is a chi-square variance interval generally asymmetric?
9. Why must a calculated required sample size be rounded upward?
10. What assumption distinguishes pooled from unequal-variance two-sample $t$ procedures?

### Calculation

11. For 90% confidence, find $\alpha$ and $\alpha/2$.
12. A known-$\sigma$ mean problem has $\bar x=50$, $\sigma=8$, $n=64$. Using $z_{0.025}=1.96$, find the 95% margin of error.
13. Using Question 12, construct the 95% confidence interval.
14. A sample has $\bar x=20$, $s=4$, $n=16$. Using $t_{0.025,15}=2.131$, find the 95% margin of error.
15. Using Question 14, construct the 95% confidence interval.
16. Two independent known-$\sigma$ samples have $\bar x_1=30$, $\bar x_2=26$, $\sigma_1=5$, $\sigma_2=4$, $n_1=n_2=25$. Find the standard error of $\bar X_1-\bar X_2$.
17. Using Question 16 and $z_{0.025}=1.96$, construct the 95% confidence interval for $\mu_1-\mu_2$.
18. A normal-population sample has $n=10$, $s^2=4$. Using $\chi^2_{0.025,9}=19.0228$ and $\chi^2_{0.975,9}=2.7004$, find the 95% variance interval.
19. For known $\sigma=10$, 95% confidence, and desired margin $E=2$, find the required sample size.

### Multiple Choice

20. A 95% confidence level corresponds to:
A) $\alpha=0.95$  
B) $\alpha=0.50$  
C) $\alpha=0.05$  
D) $\alpha=0.025$.

21. For a symmetric 95% two-sided interval, each tail contains:
A) 0.95  B) 0.05  C) 0.025  D) 0.005.

22. If population $\sigma$ is known, the one-mean confidence interval uses:
A) $z$  B) $t$  C) $\chi^2$  D) $F$.

23. If population $\sigma$ is unknown and replaced by sample $s$ in the one-sample normal model, use:
A) $z$  B) $t$  C) binomial  D) Poisson.

24. Increasing confidence level while holding sample data fixed generally:
A) narrows the interval  
B) widens the interval  
C) leaves width unchanged  
D) sets margin of error to zero.

25. For a known-$\sigma$ mean interval, doubling $n$ changes the margin of error by a factor of:
A) $2$  B) $1/2$  C) $1/\sqrt2$  D) $1/4$.

26. A confidence interval for one normal-population variance uses:
A) standard normal  
B) Student's $t$  
C) chi-square  
D) binomial.

27. If the sample-size formula gives $n=48.02$, the required integer sample size is:
A) 48  B) 49  C) 48.02  D) 50 always.

---

## Answer Key with Explanations

### Conceptual

1. A point estimate is one sample-derived number used to estimate a parameter. An
   interval estimate adds a range determined from the sampling distribution and a
   stated confidence level. (§32.1)

2. Over repeated random samples analyzed by the same valid procedure, about 95%
   of the constructed intervals would contain the fixed target parameter.
   (§32.1)

3. A two-sided interval has total outside probability $\alpha$. Symmetry divides
   that probability equally between the lower and upper tails. (§32.1)

4. Use a $z$ interval when the relevant population standard deviation is known
   and the stated sampling model supports the normal-standardized procedure.
   (§32.2)

5. Replacing fixed $\sigma$ with random sample $s$ adds uncertainty. Student's
   $t$ accounts for that uncertainty using degrees of freedom. (§32.3)

6. The critical value increases, so the interval becomes wider. (§32.2–32.3)

7. Margin scales as $1/\sqrt n$. Quadrupling $n$ multiplies margin by
   $1/\sqrt4=1/2$. (§32.6)

8. The chi-square distribution is asymmetric, and the parameter appears in the
   denominator of the chi-square pivot. The resulting endpoints are therefore
   not symmetric about $s^2$. (§32.5)

9. Rounding down would produce fewer observations than the derived minimum and
   could exceed the allowed margin of error. (§32.6)

10. Pooling assumes the two populations share a common variance. Without that
    assumption, use the unequal-variance standard error and its corresponding
    approximate degrees of freedom. (§32.4)

### Calculation

11.

    $$
    1-\alpha=0.90
    $$

    so

    $$
    \boxed{\alpha=0.10}
    $$

    and

    $$
    \boxed{\alpha/2=0.05}.
    $$

12.

    $$
    E
    =
    1.96\frac{8}{\sqrt{64}}
    =
    1.96(1)
    =
    \boxed{1.96}.
    $$

13.

    $$
    50\pm1.96
    $$

    gives

    $$
    \boxed{
    48.04<\mu<51.96.
    }
    $$

14.

    $$
    E
    =
    2.131\frac{4}{\sqrt{16}}
    =
    2.131(1)
    =
    \boxed{2.131}.
    $$

15.

    $$
    20\pm2.131
    $$

    gives

    $$
    \boxed{
    17.869<\mu<22.131.
    }
    $$

16.

    $$
    SE
    =
    \sqrt{
    \frac{5^2}{25}
    +
    \frac{4^2}{25}
    }
    $$

    $$
    =
    \sqrt{1+0.64}
    =
    \boxed{1.2806\text{ approximately}}.
    $$

17. Point estimate:

    $$
    30-26=4.
    $$

    Margin:

    $$
    E
    =
    1.96(1.2806)
    \approx
    2.510.
    $$

    Therefore

    $$
    \boxed{
    1.49<\mu_1-\mu_2<6.51.
    }
    $$

18. Numerator:

    $$
    (n-1)s^2
    =
    9(4)
    =
    36.
    $$

    Lower:

    $$
    \frac{36}{19.0228}
    \approx
    1.8925.
    $$

    Upper:

    $$
    \frac{36}{2.7004}
    \approx
    13.331.
    $$

    Therefore

    $$
    \boxed{
    1.89<\sigma^2<13.33.
    }
    $$

19.

    $$
    n
    =
    \left(
    \frac{1.96(10)}{2}
    \right)^2
    $$

    $$
    =
    (9.8)^2
    =
    96.04.
    $$

    Round upward:

    $$
    \boxed{n=97}.
    $$

### Multiple Choice

20. **C.** $1-\alpha=0.95$ gives $\alpha=0.05$. (§32.1)

21. **C.** $0.05/2=0.025$ in each tail. (§32.1)

22. **A.** Known population standard deviation uses the standard-normal critical
    value. (§32.2)

23. **B.** Sample-estimated spread leads to Student's $t$ under the stated model.
    (§32.3)

24. **B.** Greater confidence requires more central sampling-distribution area,
    which pushes critical values farther into the tails. (§32.2–32.3)

25. **C.** Since $E\propto1/\sqrt n$, doubling $n$ multiplies $E$ by
    $1/\sqrt2$. (§32.6)

26. **C.** The normal-population variance interval uses chi-square critical
    values. (§32.5)

27. **B.** Sample size must be a whole number and must be rounded upward to meet
    the required precision. (§32.6)

---

## Practice Problems

1. **Confidence level.** For a 96% two-sided confidence interval, determine
   $\alpha$, $\alpha/2$, and the Handbook normal critical value.

2. **Known $\sigma$.** A voltage process has known $\sigma=0.40$ V. A sample of
   $n=64$ has $\bar x=12.10$ V. Construct a 95% confidence interval for $\mu$.

3. **Unknown $\sigma$.** A sample of $n=16$ has $\bar x=75.0$ and $s=8.0$.
   Use $t_{0.025,15}=2.131$ to construct a 95% confidence interval for $\mu$.

4. **Width comparison.** For the same standard error, compare the margin of error
   using $z=1.960$ versus $t=2.262$. By what percentage is the $t$ margin larger?

5. **Two means, known spread.** Independent samples have:
   $$\bar x_1=44,\quad \sigma_1=6,\quad n_1=36,$$
   $$\bar x_2=40,\quad \sigma_2=4,\quad n_2=25.$$
   Construct a 95% confidence interval for $\mu_1-\mu_2$.

6. **Pooled variance.** Two independent samples have
   $$n_1=10,\ s_1^2=4,\qquad n_2=12,\ s_2^2=9.$$
   Compute the pooled variance $s_p^2$ and pooled degrees of freedom.

7. **Variance interval.** A normal-population sample has
   $$n=12,\qquad s^2=9.$$
   Use
   $$\chi^2_{0.025,11}=21.9200$$
   and
   $$\chi^2_{0.975,11}=3.8157$$
   to construct a 95% confidence interval for $\sigma^2$.

8. **Standard-deviation interval.** Convert the variance interval from Problem 7
   into a confidence interval for $\sigma$.

9. **Sample size.** A known planning standard deviation is 15 units. Determine
   the minimum sample size required for a 95% confidence interval with margin of
   error at most 4 units.

10. **Interpretation.** Explain why the statement "there is a 95% probability
    that the fixed population mean is inside this already calculated classical
    confidence interval" is not the usual frequentist interpretation.

---

## Practice Problem Solutions

1. For 96% confidence,

   $$
   1-\alpha=0.96
   $$

   so

   $$
   \boxed{\alpha=0.04}
   $$

   and

   $$
   \boxed{\alpha/2=0.02}.
   $$

   The Handbook table gives

   $$
   \boxed{z_{0.02}=2.0537}.
   $$

2. Standard error:

   $$
   \frac{\sigma}{\sqrt n}
   =
   \frac{0.40}{8}
   =
   0.05\text{ V}.
   $$

   Margin:

   $$
   E
   =
   1.96(0.05)
   =
   0.098\text{ V}.
   $$

   Interval:

   $$
   12.10\pm0.098
   $$

   so

   $$
   \boxed{
   12.002\text{ V}<\mu<12.198\text{ V}.
   }
   $$

3. Standard error:

   $$
   \frac{s}{\sqrt n}
   =
   \frac{8}{4}
   =
   2.
   $$

   Margin:

   $$
   E
   =
   2.131(2)
   =
   4.262.
   $$

   Interval:

   $$
   \boxed{
   70.738<\mu<79.262.
   }
   $$

4. Since both use the same standard error,

   $$
   \frac{E_t}{E_z}
   =
   \frac{2.262}{1.960}
   \approx
   1.15408.
   $$

   Therefore the $t$ margin is approximately

   $$
   \boxed{15.4\%}
   $$

   larger.

5. Difference estimate:

   $$
   \bar x_1-\bar x_2
   =
   4.
   $$

   Standard error:

   $$
   SE
   =
   \sqrt{
   \frac{6^2}{36}
   +
   \frac{4^2}{25}
   }
   $$

   $$
   =
   \sqrt{
   1+0.64
   }
   =
   1.2806.
   $$

   Margin:

   $$
   E
   =
   1.96(1.2806)
   \approx
   2.510.
   $$

   Interval:

   $$
   \boxed{
   1.49<\mu_1-\mu_2<6.51.
   }
   $$

6. Pooled degrees of freedom:

   $$
   \nu
   =
   10+12-2
   =
   \boxed{20}.
   $$

   Pooled variance:

   $$
   s_p^2
   =
   \frac{
   (10-1)(4)
   +
   (12-1)(9)
   }{20}
   $$

   $$
   =
   \frac{36+99}{20}
   =
   \frac{135}{20}
   =
   \boxed{6.75}.
   $$

7. Degrees of freedom:

   $$
   \nu
   =
   12-1
   =
   11.
   $$

   Numerator:

   $$
   (n-1)s^2
   =
   11(9)
   =
   99.
   $$

   Lower bound:

   $$
   L
   =
   \frac{99}{21.9200}
   \approx
   4.516.
   $$

   Upper bound:

   $$
   U
   =
   \frac{99}{3.8157}
   \approx
   25.945.
   $$

   Therefore

   $$
   \boxed{
   4.52<\sigma^2<25.95.
   }
   $$

8. Take square roots:

   $$
   \sqrt{4.516}
   \approx
   2.125,
   $$

   $$
   \sqrt{25.945}
   \approx
   5.094.
   $$

   So

   $$
   \boxed{
   2.13<\sigma<5.09.
   }
   $$

9.

   $$
   n
   =
   \left(
   \frac{1.96(15)}{4}
   \right)^2
   $$

   $$
   =
   (7.35)^2
   =
   54.0225.
   $$

   Round upward:

   $$
   \boxed{n=55}.
   $$

10. In classical frequentist inference, the population mean is treated as fixed.
    The random object is the interval-producing procedure before sampling.
    A 95% confidence procedure is designed so that about 95% of intervals from
    repeated samples contain the fixed mean. After one interval is observed, the
    conventional frequentist statement concerns the procedure's coverage rather
    than assigning a 95% posterior probability to the fixed parameter.

---

## Quick Reference

**Confidence level**

$$
\boxed{
1-\alpha
}
$$

Two-sided symmetric tail area:

$$
\boxed{
\alpha/2
}
$$

per tail.

**General symmetric structure**

$$
\boxed{
\text{estimate}
\pm
(\text{critical value})(\text{standard error})
}
$$

**One mean — $\sigma$ known**

$$
\boxed{
\bar x
\pm
z_{\alpha/2}
\frac{\sigma}{\sqrt n}
}
$$

Margin:

$$
\boxed{
E
=
z_{\alpha/2}
\frac{\sigma}{\sqrt n}
}
$$

**One mean — $\sigma$ unknown**

$$
\boxed{
\bar x
\pm
t_{\alpha/2,n-1}
\frac{s}{\sqrt n}
}
$$

**Difference of means — known population standard deviations**

$$
\boxed{
(\bar x_1-\bar x_2)
\pm
z_{\alpha/2}
\sqrt{
\frac{\sigma_1^2}{n_1}
+
\frac{\sigma_2^2}{n_2}
}
}
$$

**Pooled variance**

$$
\boxed{
s_p^2
=
\frac{
(n_1-1)s_1^2
+
(n_2-1)s_2^2
}{
n_1+n_2-2
}
}
$$

**Difference of means — unknown but equal population variances**

$$
\boxed{
(\bar x_1-\bar x_2)
\pm
t_{\alpha/2,\nu}
s_p
\sqrt{
\frac1{n_1}
+
\frac1{n_2}
}
}
$$

$$
\nu=n_1+n_2-2.
$$

**One normal-population variance**

With upper-tail chi-square notation:

$$
\boxed{
\frac{(n-1)s^2}
{\chi^2_{\alpha/2,n-1}}
<
\sigma^2
<
\frac{(n-1)s^2}
{\chi^2_{1-\alpha/2,n-1}}
}
$$

**Population standard deviation**

Square-root both variance bounds.

**Known-$\sigma$ sample-size planning**

$$
\boxed{
n
=
\left(
\frac{z_{\alpha/2}\sigma}{E}
\right)^2
}
$$

Always round upward.

**Width relationships**

$$
E\propto z_{\alpha/2},
\qquad
E\propto\sigma,
\qquad
E\propto\frac1{\sqrt n}.
$$

---

## What's Next

A confidence interval asks:

> Which parameter values remain compatible with the sample at this confidence
> level?

A hypothesis test asks the complementary decision question:

> Does the sample provide enough evidence to reject a specified parameter value
> or model?

**Chapter 01-33 — Hypothesis Testing and Statistical Decisions** will develop:

- null and alternative hypotheses,
- one-sided and two-sided tests,
- significance level $\alpha$,
- Type I and Type II errors,
- $z$, $t$, chi-square, and $F$ test statistics,
- rejection regions,
- p-values,
- and the connection between two-sided hypothesis tests and confidence
  intervals.

The FE Reference Handbook places hypothesis-test tables immediately before the
confidence-interval material on printed pp. 74–75, so the formulas you have just
used will reappear with a different question attached to them.

Carry one distinction forward:

> A confidence interval estimates a parameter. A hypothesis test evaluates a
> specified claim about a parameter.

— Your Mentor
