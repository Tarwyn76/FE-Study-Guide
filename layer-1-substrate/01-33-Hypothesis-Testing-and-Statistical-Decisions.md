---
chapter: "01-33"
title: "Hypothesis Testing and Statistical Decisions"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-033-01, MATH-1D-033-02, MATH-1D-033-03, MATH-1D-033-04, MATH-1D-033-05, MATH-1D-033-06, MATH-1D-033-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-33: Hypothesis Testing and Statistical Decisions

> *"A hypothesis test does not prove a claim true or false. It asks whether the
> observed sample would be sufficiently unusual if a specified claim were true."*

---

## Before You Start

**Prerequisites:** [01-31 Sampling Distributions, Student's t, and Chi-Square](01-31-Sampling-Distributions-Students-t-and-Chi-Square.md) ·
[01-32 Estimation and Confidence Intervals](01-32-Estimation-and-Confidence-Intervals.md)

**Skip if:** You can write null and alternative hypotheses from engineering
language; distinguish one-sided and two-sided alternatives; interpret significance
level $\alpha$; distinguish Type I and Type II errors; select $z$, $t$,
$\chi^2$, or $F$ for the parameter being tested; compute a test statistic; use a
critical-value rejection rule; interpret a p-value; and connect a two-sided
hypothesis test at significance $\alpha$ to a $100(1-\alpha)\%$ confidence
interval.

**Time:** About 110–130 min reading and worked examples · 40–50 min review
questions · 70–90 min practice problems.

**Working convention:** A statistical decision is stated as either **reject
$H_0$** or **fail to reject $H_0$**. Do not replace "fail to reject" with
"prove $H_0$ true." The sample may simply be too weak to justify rejection.

---

## On the Board Today

A confidence interval begins with a sample and asks:

> Which parameter values remain compatible with these data?

A hypothesis test begins with a specific claim and asks:

> If that claim were true, how unusual would these data be?

The procedure is controlled by the **null hypothesis**.

You assume the null model long enough to determine the sampling distribution of a
test statistic. Then you ask whether the observed statistic falls in a region
that would be too unlikely under that model.

The test therefore has five parts:

1. state $H_0$ and $H_1$,
2. choose a significance level,
3. choose and compute the correct test statistic,
4. compare the statistic with a rejection criterion or p-value,
5. state the decision in engineering context.

The arithmetic is usually not the difficult part.

The difficult parts are deciding:

- which direction the alternative points,
- whether population spread is known,
- which degrees of freedom apply,
- whether the evidence belongs in one tail or two,
- and what the decision actually permits you to say.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **33.1** State null and alternative hypotheses from an engineering claim
* **33.2** Distinguish left-tailed, right-tailed, and two-sided tests
* **33.3** Interpret significance level $\alpha$ as the probability of a Type I error under the test design
* **33.4** Distinguish Type I and Type II errors and relate power to $1-\beta$
* **33.5** Select $z$ or $t$ for one- and two-mean tests
* **33.6** Use critical-value rejection regions for $z$ and $t$
* **33.7** Interpret p-values and compare them with $\alpha$
* **33.8** Test a normal-population variance using chi-square
* **33.9** Compare two normal-population variances using an $F$ statistic
* **33.10** Distinguish statistical significance from engineering importance
* **33.11** Connect two-sided hypothesis tests with confidence intervals
* **33.12** State conclusions without claiming that failure to reject proves the null hypothesis

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $H_0$ | null hypothesis | reference claim used to build the test statistic |
| $H_1$ | alternative hypothesis | claim supported when $H_0$ is rejected |
| $\alpha$ | significance level | probability of Type I error under the test design |
| $\beta$ | probability of Type II error | depends on the true alternative value |
| $1-\beta$ | power | probability of rejecting $H_0$ when the specified alternative is true |
| $\mu_0$ | hypothesized population mean | value stated in $H_0$ |
| $\sigma_0^2$ | hypothesized population variance | variance stated in $H_0$ |
| $Z_0$ | observed $z$ test statistic | Handbook notation |
| $t_0$ | observed Student's $t$ statistic | Handbook notation |
| $\chi_0^2$ | observed chi-square statistic | variance test |
| $F_0$ | observed $F$ statistic | ratio of sample variances |
| $\nu$ | degrees of freedom | depends on the procedure |
| $p$ | p-value | tail probability at least as extreme as the observed statistic under $H_0$ |

**Notation warning.** The Handbook uses upper-tail critical values such as
$Z_\alpha$, $t_{\alpha,\nu}$, $\chi^2_{\alpha,\nu}$, and
$F_{\alpha,\nu_1,\nu_2}$. Always identify whether the problem is one-tailed or
two-sided before selecting the critical value.

---

## 33.1 Null and Alternative Hypotheses

A statistical test begins with two competing statements.

The **null hypothesis** $H_0$ contains the reference parameter value.

The **alternative hypothesis** $H_1$ states the departure the test is designed to
detect.

### Two-sided alternative

If the engineering question is whether the parameter is **different** from a
specified value:

$$
\boxed{
H_0:\mu=\mu_0
}
$$

$$
\boxed{
H_1:\mu\ne\mu_0.
}
$$

Evidence in either direction can cause rejection.

### Left-tailed alternative

If the question is whether the parameter is **less than** the reference:

$$
\boxed{
H_0:\mu=\mu_0
}
$$

$$
\boxed{
H_1:\mu<\mu_0.
}
$$

Only unusually low test-statistic values support the alternative.

### Right-tailed alternative

If the question is whether the parameter is **greater than** the reference:

$$
\boxed{
H_0:\mu=\mu_0
}
$$

$$
\boxed{
H_1:\mu>\mu_0.
}
$$

Only unusually high test-statistic values support the alternative.

The direction of $H_1$ is determined by the engineering question **before**
looking at the data.

![FIG-01-33-001: Three hypothesis-test normal curves. Left panel is two-sided with alpha/2 shaded in both tails and H1: parameter not equal to reference. Middle is left-tailed with alpha shaded in the left tail and H1: parameter less than reference. Right is right-tailed with alpha shaded in the right tail and H1: parameter greater than reference. A warning states "choose direction from the engineering claim before examining the sample result."](../figures/FIG-01-33-001-hypothesis-directions.png)

### Worked Example 1 — Translate the Engineering Claim

A manufacturer claims the mean output voltage is 5.00 V.

**(a)** Test whether the mean differs from 5.00 V.

$$
H_0:\mu=5.00\text{ V}
$$

$$
\boxed{
H_1:\mu\ne5.00\text{ V}
}
$$

Two-sided.

**(b)** Test whether the mean output is below 5.00 V.

$$
H_0:\mu=5.00\text{ V}
$$

$$
\boxed{
H_1:\mu<5.00\text{ V}
}
$$

Left-tailed.

**(c)** Test whether mean breaking strength exceeds 500 MPa.

$$
H_0:\mu=500\text{ MPa}
$$

$$
\boxed{
H_1:\mu>500\text{ MPa}
}
$$

Right-tailed.

**Check.** The alternative signs match the words different, below, and exceeds.

---

## 33.2 Type I Error, Type II Error, Significance, and Power

A hypothesis test can make two kinds of decision error.

### Type I error

A **Type I error** occurs when $H_0$ is rejected even though $H_0$ is true.

Its probability is

$$
\boxed{
\alpha=P(\text{Type I error}).
}
$$

The Handbook calls $\alpha$ the **level of significance**.

If

$$
\alpha=0.05,
$$

the rejection region is designed so that, when the null model is true, a result
falls into that rejection region only 5% of the time.

### Type II error

A **Type II error** occurs when the test fails to reject $H_0$ even though a
specified alternative condition is true.

Its probability is

$$
\boxed{
\beta=P(\text{Type II error}).
}
$$

The supplied Handbook uses the older wording "accepting $H_0$ when it is wrong."
This guide uses **fail to reject $H_0$** because a non-rejection does not prove
the null hypothesis true.

### Power

The probability of correctly rejecting the null when a specified alternative is
true is

$$
\boxed{
\text{power}=1-\beta.
}
$$

Power is not one fixed number unless the alternative parameter value is specified.

A test may have high power for a large departure and low power for a small one.

![FIG-01-33-002: Two overlapping sampling distributions, one under H0 and one under a specific H1. A vertical critical boundary separates retain/fail-to-reject and reject regions. Area under H0 in the reject region is labeled alpha, Type I. Area under H1 in the fail-to-reject region is labeled beta, Type II. Remaining H1 rejection area is labeled 1−beta, power.](../figures/FIG-01-33-002-alpha-beta-power.png)

### Worked Example 2 — Identify the Decision Error

A pressure relief system is designed around the claim

$$
H_0:\mu=900\text{ kPa}
$$

versus

$$
H_1:\mu>900\text{ kPa}.
$$

**Type I error:** Conclude that mean pressure exceeds 900 kPa when the actual
mean is 900 kPa.

**Type II error:** Fail to detect an actual mean pressure above 900 kPa.

Which error is more serious is an engineering-risk question, not a purely
statistical one.

### Changing $\alpha$

For fixed sample size and variability:

- reducing $\alpha$ makes rejection harder,
- which generally reduces Type I error probability,
- but may increase $\beta$ for a specified alternative,
- thereby reducing power.

Increasing sample size can improve power without requiring the same tradeoff.

> ---
> **Mentor's Margin**
>
> Statistical error probabilities are design choices. Engineering consequences
> determine whether a false alarm or a missed condition is more costly.
>
> ---

---

## 33.3 Tests on a Mean — Known Population Variance

When population standard deviation $\sigma$ is known, test

$$
H_0:\mu=\mu_0
$$

with

$$
\boxed{
Z_0
=
\frac{\bar X-\mu_0}{\sigma/\sqrt n}.
}
$$

This is the same standardized quantity used in confidence intervals, but now the
question is whether the observed value is too extreme under $H_0$.

### Handbook rejection rules

For a two-sided test,

$$
H_1:\mu\ne\mu_0,
$$

reject when

$$
\boxed{
|Z_0|>Z_{\alpha/2}.
}
$$

For a left-tailed test,

$$
H_1:\mu<\mu_0,
$$

reject when

$$
\boxed{
Z_0<-Z_\alpha.
}
$$

For a right-tailed test,

$$
H_1:\mu>\mu_0,
$$

reject when

$$
\boxed{
Z_0>Z_\alpha.
}
$$

![FIG-01-33-003: Critical-region diagram for mean z tests. Three rows show two-sided rejection at ±Z_(alpha/2), left-tailed rejection below −Z_alpha, and right-tailed rejection above +Z_alpha. Each row includes the corresponding H1 inequality and a sample observed Z0 marker to demonstrate reject versus fail-to-reject.](../figures/FIG-01-33-003-z-test-rejection-regions.png)

### Worked Example 3 — Two-Sided $z$ Test

**Given.**

A process is claimed to have

$$
\mu=100.
$$

Population standard deviation is known:

$$
\sigma=12.
$$

A sample of

$$
n=36
$$

has

$$
\bar x=104.
$$

Test at

$$
\alpha=0.05
$$

whether the population mean differs from 100.

**Hypotheses.**

$$
H_0:\mu=100
$$

$$
H_1:\mu\ne100.
$$

**Statistic.**

$$
Z_0
=
\frac{104-100}{12/\sqrt{36}}
=
\frac4{2}
=
\boxed{2.00}.
$$

**Critical value.**

For a two-sided 5% test,

$$
Z_{0.025}=1.960.
$$

Reject if

$$
|Z_0|>1.960.
$$

Since

$$
2.00>1.960,
$$

$$
\boxed{\text{reject }H_0.}
$$

**Conclusion.** At the 5% significance level, the sample provides sufficient
evidence that the population mean differs from 100.

### p-value view

From the unit-normal table,

$$
R(2.00)=0.0228.
$$

Two-sided p-value:

$$
p
=
2(0.0228)
=
\boxed{0.0456}.
$$

Since

$$
p<0.05,
$$

the same rejection decision follows.

---

## 33.4 Tests on a Mean — Unknown Population Variance

If population $\sigma$ is unknown and sample standard deviation $s$ is used, the
one-sample statistic is

$$
\boxed{
t_0
=
\frac{\bar X-\mu_0}{s/\sqrt n}
}
$$

with

$$
\boxed{
\nu=n-1.
}
$$

The Handbook gives the corresponding rejection rules.

Two-sided:

$$
\boxed{
|t_0|>t_{\alpha/2,n-1}.
}
$$

Left-tailed:

$$
\boxed{
t_0<-t_{\alpha,n-1}.
}
$$

Right-tailed:

$$
\boxed{
t_0>t_{\alpha,n-1}.
}
$$

### Worked Example 4 — One-Sample $t$ Test

Use the sample from Chapter 01-31:

$$
n=10,
\qquad
\bar x=52.4,
\qquad
s=3.0.
$$

Test

$$
H_0:\mu=50
$$

against

$$
H_1:\mu\ne50
$$

at

$$
\alpha=0.05.
$$

**Statistic.**

$$
t_0
=
\frac{52.4-50}{3/\sqrt{10}}
\approx
\boxed{2.5298}.
$$

Degrees of freedom:

$$
\nu=9.
$$

Critical value:

$$
t_{0.025,9}=2.262.
$$

Because

$$
|2.5298|>2.262,
$$

$$
\boxed{\text{reject }H_0.}
$$

**p-value bracket.**

The Handbook table gives

$$
t_{0.025,9}=2.262
$$

and

$$
t_{0.01,9}=2.821.
$$

Since

$$
2.262<2.5298<2.821,
$$

the upper-tail probability lies between 0.01 and 0.025.

For a symmetric two-sided test,

$$
\boxed{
0.02<p<0.05.
}
$$

That agrees with rejection at $\alpha=0.05$.

### Two-sample mean tests

The Handbook also provides tests for

$$
H_0:\mu_1-\mu_2=\gamma.
$$

With known population variances:

$$
\boxed{
Z_0
=
\frac{
(\bar X_1-\bar X_2)-\gamma
}{
\sqrt{
\sigma_1^2/n_1+\sigma_2^2/n_2
}
}.
}
$$

With unknown variances, the Handbook provides both:

- a pooled equal-variance $t$ statistic,
- an unequal-variance $t$ statistic with approximate degrees of freedom.

Those formulas are the test counterparts of the two-sample confidence intervals
from Chapter 01-32.

---

## 33.5 Rejection Regions and p-Values

The **critical-value method** and the **p-value method** answer the same decision
question in different ways.

### Critical-value method

Choose $\alpha$ first.

Then determine the rejection region.

If the observed statistic falls inside it:

$$
\boxed{\text{reject }H_0.}
$$

Otherwise:

$$
\boxed{\text{fail to reject }H_0.}
$$

### p-value

The **p-value** is the probability, assuming $H_0$ is true, of obtaining a test
statistic at least as extreme in the direction specified by $H_1$ as the one
observed.

Decision rule:

$$
\boxed{
p\le\alpha
\quad\Rightarrow\quad
\text{reject }H_0.
}
$$

and

$$
\boxed{
p>\alpha
\quad\Rightarrow\quad
\text{fail to reject }H_0.
}
$$

### Tail direction matters

For $z_0>0$:

Right-tailed:

$$
p=P(Z\ge z_0)=R(z_0).
$$

Two-sided:

$$
p=2R(|z_0|).
$$

For a left-tailed negative statistic:

$$
p=P(Z\le z_0).
$$

The p-value is not:

- the probability that $H_0$ is true,
- the probability that the results happened "by chance,"
- or a measure of engineering importance.

![FIG-01-33-004: p-value geometry on three curves. Right-tailed example shades area beyond observed z0. Left-tailed example shades area below observed negative z0. Two-sided example shades both tails beyond ±|z0|. A decision box states p<=alpha -> reject H0; p>alpha -> fail to reject H0. A warning states "p is computed assuming H0 is true."](../figures/FIG-01-33-004-p-value-tail-geometry.png)

### Worked Example 5 — Same Statistic, Different Alternative

Suppose

$$
z_0=1.80.
$$

Using the standard normal table,

$$
R(1.80)\approx0.0359.
$$

**Right-tailed alternative**

$$
H_1:\mu>\mu_0.
$$

Then

$$
p\approx0.0359.
$$

At $\alpha=0.05$:

$$
\boxed{\text{reject }H_0.}
$$

**Two-sided alternative**

$$
H_1:\mu\ne\mu_0.
$$

Then

$$
p
\approx
2(0.0359)
=
0.0718.
$$

At $\alpha=0.05$:

$$
\boxed{\text{fail to reject }H_0.}
$$

Same observed statistic.

Different alternative.

Different p-value and decision.

This is why choosing the test direction after seeing the data is invalid.

### Source note

The supplied Handbook explicitly gives hypotheses, Type I/II errors,
significance, test statistics, and rejection criteria. A general p-value
definition was not located on those hypothesis-test pages. The p-value workflow
in this section is included as guide-developed statistical interpretation
consistent with the same reference distributions and rejection regions.

---

## 33.6 Tests on Variances — Chi-Square and $F$

Mean tests are not the only hypothesis tests in the Handbook.

### One normal-population variance

Test

$$
H_0:\sigma^2=\sigma_0^2.
$$

Use

$$
\boxed{
\chi_0^2
=
\frac{(n-1)s^2}{\sigma_0^2}
}
$$

with

$$
\nu=n-1.
$$

For a two-sided test,

$$
H_1:\sigma^2\ne\sigma_0^2,
$$

reject when the statistic is too small or too large.

Using the Handbook's upper-tail notation:

$$
\boxed{
\chi_0^2
<
\chi^2_{1-\alpha/2,\nu}
}
$$

or

$$
\boxed{
\chi_0^2
>
\chi^2_{\alpha/2,\nu}.
}
$$

### Worked Example 6 — Chi-Square Variance Test

**Given.**

A normal-population sample has

$$
n=10,
\qquad
s^2=4.00.
$$

Test

$$
H_0:\sigma^2=9.00
$$

against

$$
H_1:\sigma^2\ne9.00
$$

at

$$
\alpha=0.05.
$$

Statistic:

$$
\chi_0^2
=
\frac{(9)(4)}{9}
=
\boxed{4.00}.
$$

Degrees of freedom:

$$
\nu=9.
$$

Critical values:

$$
\chi^2_{0.975,9}
\approx
2.7004,
$$

$$
\chi^2_{0.025,9}
\approx
19.0228.
$$

Reject outside

$$
[2.7004,\ 19.0228].
$$

Since

$$
2.7004<4.00<19.0228,
$$

$$
\boxed{\text{fail to reject }H_0.}
$$

The sample does not provide sufficient evidence at the 5% level that population
variance differs from 9.

### Comparing two normal-population variances

For independent normal samples, the Handbook uses an $F$ statistic based on the
sample-variance ratio:

$$
\boxed{
F_0
=
\frac{s_1^2}{s_2^2}.
}
$$

Under equal population variances,

$$
H_0:\sigma_1^2=\sigma_2^2,
$$

the statistic follows an $F$ distribution with numerator and denominator degrees
of freedom determined by the sample sizes.

For a one-sided test

$$
H_1:\sigma_1^2>\sigma_2^2,
$$

with

$$
\nu_1=n_1-1,
\qquad
\nu_2=n_2-1,
$$

reject for sufficiently large

$$
F_0.
$$

![FIG-01-33-005: Variance-test comparison. Left panel shows an asymmetric chi-square curve with lower and upper rejection tails for a two-sided one-variance test. Right panel shows a right-skewed F curve with an upper-tail rejection region for testing sigma1²>sigma2². Formula callouts show chi0²=(n−1)s²/sigma0² and F0=s1²/s2² with the relevant degrees of freedom.](../figures/FIG-01-33-005-chi-square-f-variance-tests.png)

### Worked Example 7 — One-Sided $F$ Test

Two independent normal-process samples have

$$
n_1=10,
\qquad
s_1^2=12,
$$

$$
n_2=10,
\qquad
s_2^2=3.
$$

Test

$$
H_0:\sigma_1^2=\sigma_2^2
$$

against

$$
H_1:\sigma_1^2>\sigma_2^2
$$

at

$$
\alpha=0.05.
$$

Statistic:

$$
F_0
=
\frac{12}{3}
=
\boxed{4.00}.
$$

Degrees of freedom:

$$
\nu_1=9,
\qquad
\nu_2=9.
$$

The 5% upper-tail critical value is approximately

$$
F_{0.05,9,9}
\approx
3.18.
$$

Because

$$
4.00>3.18,
$$

$$
\boxed{\text{reject }H_0.}
$$

The sample provides evidence that population 1 has the larger variance.

**Check.** The alternative placed variance 1 in the numerator, so large values of
$F_0$ support $H_1$.

> ---
> **Mentor's Margin**
>
> In an $F$ test, numerator and denominator degrees of freedom are not
> interchangeable. Label the variance ratio before opening the table.
>
> ---

---

## 33.7 Statistical Significance, Engineering Importance, and Confidence Intervals

A statistically significant result is not automatically important in practice.

With a sufficiently large sample, a very small physical difference can produce a
small p-value.

Conversely, a practically important difference may fail to reach statistical
significance when the sample is small or highly variable.

### Statistical significance

A result is statistically significant at level $\alpha$ when the test rejects
$H_0$ under the chosen rule.

This is a statement about the sample relative to a reference model.

### Engineering significance

Engineering importance asks questions such as:

- Is the difference large enough to affect safety?
- Does it exceed tolerance or design margin?
- Does it change cost or reliability materially?
- Is it practically measurable?
- Is it large relative to natural process variation?

Those questions require domain thresholds, not only a p-value.

### Confidence interval connection

For a two-sided test

$$
H_0:\mu=\mu_0
$$

at significance level

$$
\alpha,
$$

the corresponding

$$
100(1-\alpha)\%
$$

confidence interval gives the same decision under the same model and assumptions.

If

$$
\mu_0
$$

lies **outside** the interval:

$$
\boxed{\text{reject }H_0.}
$$

If

$$
\mu_0
$$

lies **inside** the interval:

$$
\boxed{\text{fail to reject }H_0.}
$$

The same relationship applies to a two-sided test of

$$
\mu_1-\mu_2=0:
$$

if zero is outside the corresponding confidence interval for the difference, the
two-sided null is rejected at the matching significance level.

![FIG-01-33-006: Confidence-interval and hypothesis-test equivalence. Left shows a 95% interval centered at an estimate with null value mu0 outside; arrow maps to two-sided alpha=0.05 rejection. Right shows another 95% interval containing mu0; arrow maps to fail-to-reject. A footer states "same model, same standard error, same critical values, same two-sided decision."](../figures/FIG-01-33-006-ci-test-equivalence.png)

### Worked Example 8 — Confidence Interval Predicts the Test Decision

Chapter 01-32 produced the 95% confidence interval

$$
1.49
<
\mu_1-\mu_2
<
6.51.
$$

Consider the two-sided test

$$
H_0:\mu_1-\mu_2=0
$$

versus

$$
H_1:\mu_1-\mu_2\ne0
$$

at

$$
\alpha=0.05.
$$

The null value

$$
0
$$

is outside the 95% confidence interval.

Therefore the matching two-sided test must

$$
\boxed{\text{reject }H_0.}
$$

No new arithmetic is needed.

### Worked Example 9 — Failure to Reject Is Not Proof

Suppose a test gives

$$
p=0.18
$$

with

$$
\alpha=0.05.
$$

Because

$$
0.18>0.05,
$$

the decision is

$$
\boxed{\text{fail to reject }H_0.}
$$

Correct statement:

> The sample does not provide sufficient evidence at the 5% significance level
> to reject the null hypothesis.

Incorrect statement:

> The null hypothesis has been proven true.

A weak, noisy, or small sample may simply lack power.

### Decision workflow

A complete hypothesis-test solution should read in this order:

1. **Parameter and assumptions**
2. **$H_0$ and $H_1$**
3. **$\alpha$**
4. **Reference distribution and degrees of freedom**
5. **Test statistic**
6. **Critical value or p-value**
7. **Reject / fail to reject**
8. **Engineering conclusion**

![FIG-01-33-007: Full hypothesis-testing workflow flowchart. Start with engineering claim -> define parameter -> write H0/H1 before data-direction choice -> choose alpha -> select reference distribution z/t/chi-square/F -> compute statistic -> critical region or p-value -> decision reject/fail-to-reject -> state conclusion in engineering context -> separate statistical significance from practical importance.](../figures/FIG-01-33-007-hypothesis-test-workflow.png)

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed p. 73 defines the null and
> alternative hypotheses, Type I and Type II errors, $\alpha$, $\beta$, and
> significance level. Printed p. 74 gives tests on normal-distribution means
> with variance known and unknown. Printed p. 75 gives tests on normal
> variances, including chi-square and $F$ procedures. Printed pp. 77–80 provide
> the normal, Student's $t$, $F$, and chi-square critical-value tables.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Null and alternative hypotheses | 73 | Introduces a null parameter value and a two-sided alternative |
| Type I and Type II errors | 73 | Defines the two decision-error types and symbols $\alpha$ and $\beta$ |
| Level of significance | 73 | Identifies $\alpha$ as probability of Type I error / significance level |
| Tests on means — variance known | 74 | Gives one- and two-sided one-sample and two-sample $z$ tests |
| Tests on means — variance unknown | 74 | Gives one- and two-sided one-sample and two-sample $t$ tests |
| Tests on variances | 75 | Gives chi-square one-variance tests and $F$ two-variance tests |
| Unit normal table | 77 | Supports $z$ critical values and tail probabilities |
| Student's $t$ table | 78 | Supports $t_{\alpha,\nu}$ critical values |
| Critical values of the $F$ distribution | 79 | Upper-tail $F_{\alpha,\nu_1,\nu_2}$ values |
| Chi-square critical values | 80 | Upper-tail $\chi^2_{\alpha,\nu}$ values |

### Handbook wording for Type II error

The supplied Handbook says that **accepting $H_0$ when it is wrong** is a Type II
error.

This guide uses the more cautious decision language

> **fail to reject $H_0$ when the relevant alternative is true**

because standard hypothesis testing generally does not prove the null hypothesis.
The underlying error event is the same one the Handbook is describing.

### Material developed in this guide

The following interpretation is included to make the Handbook rejection tables
usable but was not located as a general definition on the supplied hypothesis-test
pages:

- the general p-value definition,
- the decision rule $p\le\alpha$,
- statistical significance versus engineering importance,
- power notation $1-\beta$,
- and the explicit two-sided confidence-interval/test equivalence.

These are standard statistical interpretations built from the same sampling
distributions. They should not be mistaken for quotations from the Handbook.

**Know without a lookup:**

- $H_0$ contains the reference claim,
- $H_1$ determines the tail direction,
- Type I error probability is $\alpha$,
- reject when the statistic enters the rejection region,
- $p\le\alpha$ means reject,
- known $\sigma$ mean → $z$,
- estimated $s$ mean → $t$,
- one normal variance → $\chi^2$,
- ratio of two normal variances → $F$,
- and fail to reject is not the same as prove true.

---

## Where This Goes Wrong

**Writing the hypotheses after looking at the sample result.** The alternative
direction must come from the engineering question.

**Putting the sample statistic in $H_0$.** Hypotheses concern population
parameters, not observed sample means.

**Writing both $H_0$ and $H_1$ with equality.** The equality belongs in the null
reference claim.

**Using a two-sided test when the stated alternative is directional.**

**Using a one-sided test merely to obtain a smaller p-value.**

**Confusing $\alpha$ with the p-value.** $\alpha$ is chosen before the data;
the p-value is computed from the observed statistic.

**Calling the p-value the probability that $H_0$ is true.** It is a probability
of data at least as extreme as observed, calculated under $H_0$.

**Rejecting because $p>\alpha$.** The inequality is the other way around.

**Using $z$ with sample $s$ when the intended model is Student's $t$.**

**Forgetting degrees of freedom in a $t$, chi-square, or $F$ test.**

**Forgetting to split $\alpha$ between two tails.**

**Using chi-square symmetry.** It has none.

**Using a negative chi-square critical value.** Chi-square is nonnegative.

**Reversing the numerator and denominator in an $F$ test without changing the
degrees of freedom and rejection rule.**

**Saying "accept $H_0$" when the evidence only fails to justify rejection.**

**Equating statistical significance with practical importance.**

**Ignoring assumptions because the calculator produced a p-value.** A precise
number from the wrong reference distribution is still wrong.

**Claiming a nonsignificant result proves no effect exists.** It may reflect low
power.

**Comparing a confidence interval with the wrong null value.** For a difference
of means, the usual no-difference null value is 0, not either individual mean.

---

## Key Terms

| Term | Definition |
|---|---|
| hypothesis test | procedure for evaluating a specified population claim using sample data |
| null hypothesis | reference claim denoted $H_0$ |
| alternative hypothesis | competing claim denoted $H_1$ |
| two-sided test | test with rejection regions in both tails |
| left-tailed test | test with rejection region in the lower tail |
| right-tailed test | test with rejection region in the upper tail |
| significance level | chosen Type I error probability $\alpha$ |
| Type I error | rejecting a true null hypothesis |
| Type II error | failing to reject the null under a specified true alternative |
| power | probability $1-\beta$ of rejecting $H_0$ under a specified alternative |
| test statistic | standardized sample quantity whose null distribution is known |
| rejection region | set of test-statistic values that cause rejection of $H_0$ |
| critical value | boundary separating rejection and non-rejection regions |
| p-value | null-model tail probability at least as extreme as the observed statistic |
| statistical significance | rejection of $H_0$ at the chosen significance level |
| engineering significance | practical importance of the estimated effect in context |
| $z$ test | test using the standard normal reference distribution |
| $t$ test | test using Student's $t$ reference distribution |
| chi-square test | test using the chi-square reference distribution |
| $F$ test | test based on a ratio with an $F$ reference distribution |

---

## Review Questions

### Conceptual

1. What is the purpose of the null hypothesis?
2. How does a two-sided alternative differ from a one-sided alternative?
3. Define a Type I error.
4. Define a Type II error using the guide's decision language.
5. What does the significance level $\alpha$ control?
6. What is statistical power?
7. What does a p-value represent?
8. Why is failure to reject $H_0$ not proof that $H_0$ is true?
9. Distinguish statistical significance from engineering importance.
10. State the relationship between a two-sided test at level $\alpha$ and the matching $100(1-\alpha)\%$ confidence interval.

### Calculation

11. Write $H_0$ and $H_1$ for testing whether a population mean differs from 25.
12. Write $H_0$ and $H_1$ for testing whether a mean is greater than 100.
13. A known-$\sigma$ test has $\bar x=54$, $\mu_0=50$, $\sigma=10$, and $n=25$. Compute $Z_0$.
14. For Question 13, use $\alpha=0.05$ and a two-sided critical value 1.96. State the decision.
15. A one-sample $t$ test has $\bar x=21.5$, $\mu_0=20$, $s=3$, and $n=9$. Compute $t_0$ and $\nu$.
16. Using $t_{0.025,8}=2.306$, state the two-sided $\alpha=0.05$ decision for Question 15.
17. If a right-tailed $z$ test gives $z_0=1.80$ and $R(1.80)=0.0359$, give the p-value and decision at $\alpha=0.05$.
18. A variance test has $n=12$, $s^2=25$, and $\sigma_0^2=16$. Compute $\chi_0^2$.
19. Two samples have $s_1^2=18$ and $s_2^2=6$. Compute $F_0=s_1^2/s_2^2$.

### Multiple Choice

20. Rejecting a true $H_0$ is:
A) Type I error  B) Type II error  C) power  D) confidence.

21. The probability of Type I error is:
A) $\beta$  B) $1-\beta$  C) $\alpha$  D) $p$ always.

22. A two-sided mean test at $\alpha=0.05$ uses:
A) all 0.05 in one tail  
B) 0.025 in each tail  
C) 0.05 in each tail  
D) no rejection region.

23. If $p=0.012$ and $\alpha=0.05$:
A) fail to reject $H_0$  
B) reject $H_0$  
C) prove $H_1$  
D) set $\alpha=0.012$ after the test.

24. Mean test with known population $\sigma$ uses:
A) $z$  B) $t$  C) $\chi^2$  D) $F$.

25. Mean test with unknown $\sigma$ replaced by $s$ uses:
A) $z$  B) $t$  C) $\chi^2$  D) binomial.

26. A one-normal-population variance test uses:
A) $z$  B) $t$  C) $\chi^2$  D) Poisson.

27. A test comparing two normal-population variances commonly uses:
A) $z$  B) $t$  C) $\chi^2$ only  D) $F$.

---

## Answer Key with Explanations

### Conceptual

1. $H_0$ supplies the reference population claim under which the sampling
   distribution and rejection criterion are constructed. (§33.1)

2. A two-sided alternative looks for departure in either direction. A one-sided
   alternative specifies only lower or only higher departures. (§33.1)

3. A Type I error is rejecting $H_0$ when $H_0$ is actually true. (§33.2)

4. A Type II error is failing to reject $H_0$ when the specified alternative
   condition is actually true. (§33.2)

5. $\alpha$ controls the designed probability of rejecting a true null
   hypothesis—the Type I error probability. (§33.2)

6. Power is $1-\beta$, the probability of rejecting $H_0$ when a specified
   alternative is true. (§33.2)

7. It is the probability, under $H_0$, of obtaining a test statistic at least as
   extreme in the direction specified by the alternative as the observed one.
   (§33.5)

8. Non-rejection may result from weak evidence, high variability, small sample
   size, or a genuinely small effect. It does not establish exact equality.
   (§33.7)

9. Statistical significance concerns evidence relative to a null sampling model.
   Engineering importance concerns the practical magnitude and consequences of
   the effect. (§33.7)

10. Under the same model and assumptions, the two-sided test rejects a null value
    exactly when that value lies outside the matching
    $100(1-\alpha)\%$ confidence interval. (§33.7)

### Calculation

11.

    $$
    \boxed{
    H_0:\mu=25
    }
    $$

    $$
    \boxed{
    H_1:\mu\ne25.
    }
    $$

12.

    $$
    \boxed{
    H_0:\mu=100
    }
    $$

    $$
    \boxed{
    H_1:\mu>100.
    }
    $$

13.

    $$
    Z_0
    =
    \frac{54-50}{10/\sqrt{25}}
    =
    \frac4{2}
    =
    \boxed{2.00}.
    $$

14. For a two-sided 5% test:

    $$
    |Z_0|=2.00>1.96.
    $$

    Therefore

    $$
    \boxed{\text{reject }H_0.}
    $$

15.

    $$
    t_0
    =
    \frac{21.5-20}{3/\sqrt9}
    =
    \frac{1.5}{1}
    =
    \boxed{1.50}.
    $$

    Degrees of freedom:

    $$
    \boxed{\nu=8}.
    $$

16.

    $$
    |1.50|<2.306.
    $$

    Therefore

    $$
    \boxed{\text{fail to reject }H_0.}
    $$

17.

    $$
    \boxed{p=0.0359}.
    $$

    Since

    $$
    0.0359<0.05,
    $$

    $$
    \boxed{\text{reject }H_0.}
    $$

18.

    $$
    \chi_0^2
    =
    \frac{(12-1)(25)}{16}
    =
    \frac{275}{16}
    =
    \boxed{17.1875}.
    $$

19.

    $$
    F_0
    =
    \frac{18}{6}
    =
    \boxed{3.00}.
    $$

### Multiple Choice

20. **A.** Rejecting a true null is a Type I error. (§33.2)

21. **C.** $\alpha$ is the Type I error probability. (§33.2)

22. **B.** A symmetric two-sided 5% test places 2.5% in each tail. (§33.1)

23. **B.** Since $p<\alpha$, reject $H_0$. (§33.5)

24. **A.** Known population $\sigma$ gives the standard-normal $z$ statistic.
    (§33.3)

25. **B.** Estimated spread uses Student's $t$ under the stated model. (§33.4)

26. **C.** One normal-population variance is tested with chi-square. (§33.6)

27. **D.** A ratio of two normal-population variance estimates leads to an
    $F$ test. (§33.6)

---

## Practice Problems

1. **Hypothesis direction.** A supplier claims mean thickness is 2.00 mm.
   Write hypotheses for:
   (a) detecting any change,
   (b) detecting a decrease,
   (c) detecting an increase.

2. **Type I / Type II.** A safety monitor tests
   $H_0:$ mean concentration is at or below the reference condition
   against an alternative representing excessive concentration.
   Describe the practical Type I and Type II errors.

3. **Known-$\sigma$ $z$ test.** A process has known $\sigma=6$.
   A sample of $n=36$ has $\bar x=42$. Test
   $H_0:\mu=40$ against $H_1:\mu>40$ at $\alpha=0.05$ using
   $z_{0.05}=1.6449$.

4. **Two-sided $z$ p-value.** A test statistic is $z_0=-2.00$.
   Given $R(2.00)=0.0228$, find the two-sided p-value and state the decision
   at $\alpha=0.05$.

5. **One-sample $t$ test.** A normal-population sample has
   $n=16$, $\bar x=104$, $s=8$. Test
   $H_0:\mu=100$ against $H_1:\mu\ne100$ at $\alpha=0.05$ using
   $t_{0.025,15}=2.131$.

6. **p-value bracket from $t$ table.** For $\nu=9$, an observed
   $|t_0|=2.53$. Given
   $t_{0.025,9}=2.262$ and $t_{0.01,9}=2.821$, bracket the two-sided p-value.

7. **Chi-square variance test.** A normal-population sample has
   $n=10$, $s^2=4$, and null variance $\sigma_0^2=9$.
   Use lower critical value 2.7004 and upper critical value 19.0228 for a
   two-sided 5% test. State the decision.

8. **$F$ variance test.** Independent normal-process samples have
   $n_1=n_2=10$, $s_1^2=12$, $s_2^2=3$. Test
   $H_0:\sigma_1^2=\sigma_2^2$ against
   $H_1:\sigma_1^2>\sigma_2^2$ at $\alpha=0.05$ using
   $F_{0.05,9,9}=3.18$.

9. **Confidence interval connection.** A 95% confidence interval for
   $\mu_1-\mu_2$ is
   $$[-0.8,\ 3.1].$$
   What is the corresponding decision for
   $H_0:\mu_1-\mu_2=0$ versus a two-sided alternative at $\alpha=0.05$?

10. **Significance versus importance.** A very large study finds a process
    difference of 0.02 units with $p=0.001$, but the engineering tolerance is
    ±2 units. Explain what can and cannot be concluded from statistical
    significance alone.

---

## Practice Problem Solutions

1. **(a) Any change**

   $$
   H_0:\mu=2.00
   $$

   $$
   \boxed{
   H_1:\mu\ne2.00.
   }
   $$

   **(b) Decrease**

   $$
   H_0:\mu=2.00
   $$

   $$
   \boxed{
   H_1:\mu<2.00.
   }
   $$

   **(c) Increase**

   $$
   H_0:\mu=2.00
   $$

   $$
   \boxed{
   H_1:\mu>2.00.
   }
   $$

2. A **Type I error** is declaring an excessive condition when the null/reference
   condition is actually true. This can trigger an unnecessary alarm or shutdown.

   A **Type II error** is failing to reject the reference condition when the
   excessive condition is actually present. This can miss a real safety problem.

   Which error is more costly depends on the application.

3. Statistic:

   $$
   Z_0
   =
   \frac{42-40}{6/\sqrt{36}}
   =
   \frac2{1}
   =
   \boxed{2.00}.
   $$

   Right-tail rejection criterion:

   $$
   Z_0>1.6449.
   $$

   Since

   $$
   2.00>1.6449,
   $$

   $$
   \boxed{\text{reject }H_0.}
   $$

   There is sufficient evidence at the 5% level that $\mu>40$.

4. Two-sided p-value:

   $$
   p
   =
   2R(2.00)
   =
   2(0.0228)
   =
   \boxed{0.0456}.
   $$

   Since

   $$
   0.0456<0.05,
   $$

   $$
   \boxed{\text{reject }H_0.}
   $$

5. Statistic:

   $$
   t_0
   =
   \frac{104-100}{8/\sqrt{16}}
   =
   \frac4{2}
   =
   \boxed{2.00}.
   $$

   Degrees of freedom:

   $$
   \nu=15.
   $$

   Critical value:

   $$
   t_{0.025,15}=2.131.
   $$

   Since

   $$
   |2.00|<2.131,
   $$

   $$
   \boxed{\text{fail to reject }H_0.}
   $$

6. Since

   $$
   2.262<2.53<2.821,
   $$

   the one-tail area satisfies

   $$
   0.01<p_{\text{one tail}}<0.025.
   $$

   Double for the symmetric two-sided test:

   $$
   \boxed{
   0.02<p_{\text{two-sided}}<0.05.
   }
   $$

7. Statistic:

   $$
   \chi_0^2
   =
   \frac{(10-1)(4)}{9}
   =
   \boxed{4.00}.
   $$

   Non-rejection region:

   $$
   2.7004<\chi_0^2<19.0228.
   $$

   Since 4.00 lies inside,

   $$
   \boxed{\text{fail to reject }H_0.}
   $$

8. Statistic:

   $$
   F_0
   =
   \frac{12}{3}
   =
   \boxed{4.00}.
   $$

   Since

   $$
   4.00>3.18,
   $$

   $$
   \boxed{\text{reject }H_0.}
   $$

   There is evidence at the 5% level that population 1 has greater variance.

9. The interval

   $$
   [-0.8,\ 3.1]
   $$

   contains the null value 0.

   Therefore the matching two-sided 5% test

   $$
   \boxed{\text{fails to reject }H_0.}
   $$

10. The small p-value indicates that the observed difference is statistically
    inconsistent with the exact no-difference null under the test model.

    It does **not** establish that a 0.02-unit difference matters in practice.
    Compared with an engineering tolerance of ±2 units, the effect may be
    operationally negligible.

    Statistical significance answers an evidence question; engineering
    significance answers a consequence/magnitude question.

---

## Quick Reference

**Hypotheses**

Two-sided:

$$
H_0:\theta=\theta_0,
\qquad
H_1:\theta\ne\theta_0.
$$

Left-tailed:

$$
H_1:\theta<\theta_0.
$$

Right-tailed:

$$
H_1:\theta>\theta_0.
$$

**Decision errors**

$$
\boxed{
\alpha=P(\text{Type I error})
}
$$

$$
\boxed{
\beta=P(\text{Type II error})
}
$$

$$
\boxed{
\text{power}=1-\beta
}
$$

**One mean — known $\sigma$**

$$
\boxed{
Z_0
=
\frac{\bar X-\mu_0}{\sigma/\sqrt n}
}
$$

Two-sided reject:

$$
\boxed{
|Z_0|>Z_{\alpha/2}
}
$$

Left reject:

$$
Z_0<-Z_\alpha.
$$

Right reject:

$$
Z_0>Z_\alpha.
$$

**One mean — unknown $\sigma$**

$$
\boxed{
t_0
=
\frac{\bar X-\mu_0}{s/\sqrt n}
}
$$

$$
\nu=n-1.
$$

Two-sided reject:

$$
\boxed{
|t_0|>t_{\alpha/2,\nu}.
}
$$

**p-value rule**

$$
\boxed{
p\le\alpha
\Rightarrow
\text{reject }H_0
}
$$

$$
\boxed{
p>\alpha
\Rightarrow
\text{fail to reject }H_0
}
$$

**One normal-population variance**

$$
\boxed{
\chi_0^2
=
\frac{(n-1)s^2}{\sigma_0^2}
}
$$

$$
\nu=n-1.
$$

**Two normal-population variances**

$$
\boxed{
F_0
=
\frac{s_1^2}{s_2^2}
}
$$

with numerator and denominator degrees of freedom matched to the variance ratio.

**Confidence interval connection**

For a two-sided test at significance $\alpha$:

null value outside matching $100(1-\alpha)\%$ CI → reject.

null value inside matching CI → fail to reject.

**Final wording**

Reject:

> sufficient evidence to support the stated alternative at level $\alpha$.

Fail to reject:

> insufficient evidence to reject the null at level $\alpha$.

Do not write "proved true."

---

## What's Next

Hypothesis testing answered questions about one or two parameters.

Engineering experiments often compare several treatment conditions at once.

Testing every pair separately creates a new problem: the overall chance of at
least one false positive grows as the number of comparisons increases.

**Chapter 01-34 — Analysis of Variance and Design of Experiments** will develop:

- partitioning total variability into explainable and residual components,
- sums of squares and mean squares,
- one-way ANOVA,
- the ANOVA $F$ statistic,
- randomized block designs,
- two-factor factorial experiments,
- interaction effects,
- and the logic of experimental design.

The FE Reference Handbook develops design-of-experiments and ANOVA material on
printed pp. 71–73 immediately before its hypothesis-testing section.

Carry one question forward:

> Is the observed difference between group means large relative to the variation
> that remains within the groups?

ANOVA turns that question into an $F$ ratio.

— Your Mentor
