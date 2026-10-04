---
chapter: "01-31"
title: "Sampling Distributions, Student's t, and Chi-Square"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-031-01, MATH-1D-031-02, MATH-1D-031-03, MATH-1D-031-04, MATH-1D-031-05, MATH-1D-031-06, MATH-1D-031-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-31: Sampling Distributions, Student's t, and Chi-Square

> *"A sample gives you numbers. A sampling distribution tells you how those
> numbers would behave if you repeated the sampling process again and again."*

---

## Before You Start

**Prerequisites:** [01-29 Random Variables and Probability Distributions](01-29-Random-Variables-and-Probability-Distributions.md) ·
[01-30 The Normal Distribution and the Central Limit Theorem](01-30-The-Normal-Distribution-and-the-Central-Limit-Theorem.md)

**Skip if:** You can distinguish a population parameter from a sample statistic;
compute sample mean, sample variance, and sample standard deviation; explain why
sample variance uses $n-1$; interpret degrees of freedom; standardize a sample
mean with Student's $t$ when population $\sigma$ is unknown; read the Handbook's
$t_{\alpha,\nu}$ table; explain why $t$ approaches the normal distribution as
degrees of freedom increase; recognize a chi-square random variable; and form the
chi-square statistic associated with sample variance from a normal population.

**Time:** About 105–125 min reading and worked examples · 40–50 min review
questions · 65–85 min practice problems.

**Working convention:** Population quantities use Greek symbols such as $\mu$ and
$\sigma$. Sample quantities use statistics such as $\bar X$, $s^2$, and $s$.
Do not switch between them silently. The choice between $z$, $t$, and
$\chi^2$ depends on which population parameter is being standardized and which
population quantities are known.

---

## On the Board Today

Chapter 01-30 showed how a known population mean and standard deviation define a
normal model and how sample means fluctuate with standard error

$$
\frac{\sigma}{\sqrt n}.
$$

In practice, $\sigma$ is often unknown.

You estimate it from the same sample used to estimate the mean.

That extra uncertainty changes the standardized variable. Instead of

$$
Z=
\frac{\bar X-\mu}{\sigma/\sqrt n},
$$

you use

$$
T=
\frac{\bar X-\mu}{s/\sqrt n},
$$

and the reference distribution is Student's $t$, not the standard normal.

A second sampling distribution appears when the quantity of interest is variance.
For a normal population, the scaled sample variance

$$
\frac{(n-1)s^2}{\sigma^2}
$$

follows a chi-square distribution.

Those two distributions are not arbitrary additions to a formula sheet.

They arise because **sample estimates vary from sample to sample**.

That is the central idea of this chapter.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **31.1** Distinguish population parameters from sample statistics
* **31.2** Compute sample mean, sample variance, and sample standard deviation
* **31.3** Explain why estimating the mean consumes one degree of freedom
* **31.4** Interpret a sampling distribution as the distribution of a statistic over repeated samples
* **31.5** Identify when Student's $t$ replaces the standard normal $z$ statistic
* **31.6** Compute a one-sample $t$ statistic and its degrees of freedom
* **31.7** Read the Handbook's $t_{\alpha,\nu}$ critical-value table and use symmetry
* **31.8** Explain how the $t$ distribution approaches the standard normal as $\nu$ grows
* **31.9** Recognize the chi-square distribution as a sum of squared standard normal variables
* **31.10** Form the chi-square statistic for sample variance from a normal population
* **31.11** Read upper-tail chi-square critical values and account for asymmetry
* **31.12** Select $z$, $t$, or $\chi^2$ based on the parameter and known information

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $\mu$ | population mean | fixed but often unknown |
| $\sigma^2$ | population variance | fixed population parameter |
| $\sigma$ | population standard deviation | square root of $\sigma^2$ |
| $\bar X$ | sample mean | random statistic before sampling |
| $\bar x$ | realized sample mean | numerical value from one sample |
| $s^2$ | sample variance | uses denominator $n-1$ |
| $s$ | sample standard deviation | $\sqrt{s^2}$ |
| $n$ | sample size | number of observations |
| $\nu$ | degrees of freedom | often $n-1$ in one-sample problems |
| $Z$ | standard normal statistic | typically when population $\sigma$ is known |
| $T$ | Student's $t$ statistic | typically when $\sigma$ is unknown and replaced by $s$ |
| $t_{\alpha,\nu}$ | $t$ critical value | upper-tail area $\alpha$, df $\nu$ |
| $\chi^2$ | chi-square statistic | nonnegative |
| $\chi^2_{\alpha,\nu}$ | chi-square critical value | upper-tail area $\alpha$, df $\nu$ |

**Notation warning.** The FE Reference Handbook uses $v$ for degrees of freedom
in several places. This chapter uses the Greek letter $\nu$ to reduce confusion
with velocity. They mean the same role.

---

## 31.1 Population Parameters and Sample Statistics

A **population** is the full collection of items or outcomes being modeled.

A **sample** is the subset actually observed.

A **parameter** describes the population.

A **statistic** is computed from the sample.

| Population quantity | Sample counterpart |
|---|---|
| mean $\mu$ | sample mean $\bar X$ |
| variance $\sigma^2$ | sample variance $s^2$ |
| standard deviation $\sigma$ | sample standard deviation $s$ |

The distinction is conceptual, not cosmetic.

Once a sample has been observed, $\bar x$ and $s$ are known numbers.

Before sampling, $\bar X$ and $S$ are random because a different random sample
would generally produce different values.

That repeated-sample variability is what creates a **sampling distribution**.

### Sample mean

For observations

$$
x_1,x_2,\ldots,x_n,
$$

the sample mean is

$$
\boxed{
\bar x
=
\frac{1}{n}
\sum_{i=1}^{n}x_i.
}
$$

### Sample variance

The sample variance is

$$
\boxed{
s^2
=
\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar x)^2.
}
$$

Sample standard deviation:

$$
\boxed{
s=\sqrt{s^2}.
}
$$

The FE Reference Handbook prints the sample variance and sample standard
deviation in the *Engineering Probability and Statistics* section on printed
p. 64.

![FIG-01-31-001: Population-to-sample diagram. A large population cloud is labeled with fixed parameters mu and sigma. Several different random samples of equal size are drawn from it; each sample has a different x-bar and s. Arrows lead to two sampling distributions, one for X-bar and one for S-squared. A caption states "parameters describe the population; statistics vary from sample to sample."](../figures/FIG-01-31-001-population-sample-statistics.png)

### Worked Example 1 — Compute Sample Statistics

**Given.** Five measurements are

$$
10,\ 12,\ 13,\ 15,\ 20.
$$

**Find.** $\bar x$, $s^2$, and $s$.

**Solution.**

Mean:

$$
\bar x
=
\frac{10+12+13+15+20}{5}
=
\frac{70}{5}
=
\boxed{14}.
$$

Deviations from the sample mean:

$$
-4,\ -2,\ -1,\ 1,\ 6.
$$

Squared deviations:

$$
16,\ 4,\ 1,\ 1,\ 36.
$$

Sum:

$$
16+4+1+1+36
=
58.
$$

Sample variance:

$$
s^2
=
\frac{58}{5-1}
=
\boxed{14.5}.
$$

Sample standard deviation:

$$
s
=
\sqrt{14.5}
\approx
\boxed{3.8079}.
$$

**Check.** The largest observation, 20, lies 6 units above the mean, so a
standard deviation of a few units is plausible.

---

## 31.2 Sampling Distributions and Degrees of Freedom

A **sampling distribution** is the probability distribution of a statistic over
all possible random samples of a specified size from the same population.

Do not confuse:

- the distribution of individual observations $X$,
- the distribution of the sample mean $\bar X$,
- the distribution of the sample variance $S^2$.

These are different random variables.

### Why $n-1$ appears in sample variance

Once the sample mean is calculated, the deviations satisfy

$$
\boxed{
\sum_{i=1}^{n}(x_i-\bar x)=0.
}
$$

That equation is a constraint.

If you know the first $n-1$ deviations, the final deviation is forced.

Example with four deviations:

$$
d_1+d_2+d_3+d_4=0.
$$

Choose any three. Then

$$
d_4=-(d_1+d_2+d_3).
$$

Only three are independently adjustable.

So after using the sample to estimate one mean,

$$
\boxed{
\nu=n-1
}
$$

degrees of freedom remain for estimating spread.

This is why the sample variance divides by $n-1$ rather than $n$.

![FIG-01-31-002: Degrees-of-freedom diagram for n=4 observations. Four deviation boxes d1,d2,d3,d4 are connected to the constraint d1+d2+d3+d4=0. Three boxes are labeled "free to vary" and the fourth "forced by the zero-sum constraint." A formula callout states estimating one mean leaves nu=n−1 degrees of freedom.](../figures/FIG-01-31-002-degrees-of-freedom.png)

### Worked Example 2 — The Last Deviation Is Not Free

**Given.** A sample of four observations has first three deviations from the
sample mean

$$
-3,\quad 1,\quad 4.
$$

**Find.** The fourth deviation.

**Solution.**

Because deviations from the sample mean sum to zero,

$$
-3+1+4+d_4=0.
$$

So

$$
2+d_4=0
$$

and

$$
\boxed{d_4=-2}.
$$

The fourth deviation was determined by the other three.

Therefore the residual deviations have

$$
\nu=4-1=\boxed{3}
$$

degrees of freedom.

### Degrees of freedom are not "sample size minus one" everywhere

That formula belongs to a specific structure: one mean estimated from one sample.

Other procedures consume other numbers of independent constraints.

The rule to remember is:

> Degrees of freedom count how many independent pieces of information remain
> after required constraints or estimated parameters are accounted for.

---

## 31.3 Student's $t$ Distribution — Unknown Population Standard Deviation

When the population standard deviation $\sigma$ is known, Chapter 01-30 used

$$
Z
=
\frac{\bar X-\mu}{\sigma/\sqrt n}.
$$

When $\sigma$ is unknown, replace it with the sample standard deviation $s$:

$$
\boxed{
T
=
\frac{\bar X-\mu}{s/\sqrt n}.
}
$$

For a random sample from a normal population,

$$
\boxed{
T\sim t_{\nu},
\qquad
\nu=n-1.
}
$$

The denominator is now random because $s$ changes from sample to sample.

That extra uncertainty gives Student's $t$ distribution **heavier tails** than
the standard normal.

### Shape

The $t$ distribution is:

- symmetric about zero,
- bell-shaped,
- more spread out than standard normal for small $\nu$,
- increasingly close to standard normal as $\nu$ grows.

The limiting row of the Handbook $t$ table is labeled

$$
\nu=\infty.
$$

Its critical values match the familiar standard-normal values.

For example:

$$
t_{0.05,\infty}=1.645,
$$

$$
t_{0.025,\infty}=1.960.
$$

![FIG-01-31-003: Standard normal curve overlaid with Student t curves for nu=2, nu=5, and nu=30. All are centered at zero and symmetric. Low-df t curves have visibly heavier tails and lower central peaks; as df increases, the t curve approaches the normal. Tail regions are highlighted to show why t critical values are larger for small df.](../figures/FIG-01-31-003-t-versus-normal.png)

### Worked Example 3 — Compute a $t$ Statistic

**Given.**

A sample has

$$
n=10,
\qquad
\bar x=52.4,
\qquad
s=3.0.
$$

Standardize relative to

$$
\mu=50.
$$

**Find.** The $t$ statistic and degrees of freedom.

**Solution.**

Standard error based on the sample:

$$
\frac{s}{\sqrt n}
=
\frac{3.0}{\sqrt{10}}
\approx
0.94868.
$$

Therefore

$$
t
=
\frac{52.4-50}{0.94868}
$$

$$
=
\boxed{2.5298}.
$$

Degrees of freedom:

$$
\nu=n-1=10-1=\boxed{9}.
$$

**Check.** The sample mean is 2.4 units above the reference mean and the sample
standard error is just under 1 unit, so a standardized distance near 2.5 is
reasonable.

> ---
> **Mentor's Margin**
>
> Replacing $\sigma$ with $s$ is not a harmless symbol swap. It changes the
> reference distribution because the denominator is now estimated from the same
> finite sample.
>
> ---

---

## 31.4 Reading the Handbook $t$ Table

The Handbook's Student's $t$ table is on printed p. 78.

Its columns are upper-tail probabilities $\alpha$, and its rows are degrees of
freedom $\nu$.

The notation

$$
\boxed{
t_{\alpha,\nu}
}
$$

means the positive value satisfying

$$
\boxed{
P(T>t_{\alpha,\nu})=\alpha.
}
$$

### Example values from the Handbook

For

$$
\nu=9,
$$

the table gives approximately:

| Upper-tail area $\alpha$ | $t_{\alpha,9}$ |
|---:|---:|
| 0.10 | 1.383 |
| 0.05 | 1.833 |
| 0.025 | 2.262 |
| 0.01 | 2.821 |
| 0.005 | 3.250 |

### Symmetry

Because the $t$ distribution is symmetric,

$$
\boxed{
P(T<-t_{\alpha,\nu})=\alpha.
}
$$

The Handbook expresses the same idea with

$$
t_{1-\alpha,\nu}
=
-t_{\alpha,\nu}.
$$

### Two tails

If total outside probability is $\alpha$, symmetry gives

$$
\frac{\alpha}{2}
$$

in each tail.

So the symmetric central region uses

$$
\boxed{
\pm t_{\alpha/2,\nu}.
}
$$

This is the table geometry needed later for confidence intervals and
two-sided hypothesis tests.

![FIG-01-31-004: Student t table interpretation. Left panel shows a symmetric t curve with one upper tail shaded alpha and critical value t_(alpha,nu). Middle panel mirrors the same area into the lower tail at −t_(alpha,nu). Right panel shows a central region 1−alpha with alpha/2 in each tail and boundaries ±t_(alpha/2,nu). A small row excerpt for nu=9 lists 1.833, 2.262, and 2.821 under alpha=.05,.025,.01.](../figures/FIG-01-31-004-t-table-tail-areas.png)

### Worked Example 4 — Locate a $t$ Statistic in the Table

Use the result from Worked Example 3:

$$
t=2.5298,
\qquad
\nu=9.
$$

From the Handbook row:

$$
t_{0.025,9}=2.262
$$

and

$$
t_{0.01,9}=2.821.
$$

Because

$$
2.262<2.5298<2.821,
$$

the **upper-tail probability** lies between

$$
0.01
$$

and

$$
0.025.
$$

So

$$
\boxed{
0.01<P(T>2.5298)<0.025.
}
$$

This is a table-bracketing statement, not yet a formal hypothesis-test
conclusion.

### Worked Example 5 — Central 95% $t$ Region

For a sample of size

$$
n=10,
$$

the degrees of freedom are

$$
\nu=9.
$$

A central 95% region leaves total outside probability

$$
\alpha=0.05,
$$

or

$$
0.025
$$

in each tail.

Use

$$
t_{0.025,9}=2.262.
$$

Therefore

$$
\boxed{
P(-2.262<T<2.262)=0.95.
}
$$

Compare with the normal value

$$
1.960.
$$

The $t$ limits are farther from zero because estimating $\sigma$ adds
uncertainty.

---

## 31.5 The Chi-Square Distribution

The chi-square distribution is built from squared standard normal variables.

If

$$
Z_1,Z_2,\ldots,Z_\nu
$$

are independent standard normal random variables, then

$$
\boxed{
\chi^2
=
Z_1^2+Z_2^2+\cdots+Z_\nu^2
}
$$

has a chi-square distribution with

$$
\nu
$$

degrees of freedom.

The FE Reference Handbook states this construction on printed p. 69.

### Immediate consequences

Because it is a sum of squares,

$$
\boxed{
\chi^2\ge0.
}
$$

Unlike $z$ and $t$, the chi-square distribution is **not symmetric**.

For small degrees of freedom it is strongly right-skewed.

As $\nu$ increases, it becomes less skewed.

![FIG-01-31-005: Chi-square density curves for nu=2, nu=5, and nu=15 on an x-axis beginning at zero. The nu=2 curve is strongly right-skewed, nu=5 less so, and nu=15 more rounded. A left boundary at zero is emphasized with "chi-square cannot be negative." A formula above shows chi-square=sum of squared independent standard normals.](../figures/FIG-01-31-005-chi-square-shapes.png)

### Worked Example 6 — Build a Chi-Square Value from Standard Normals

**Given.**

$$
Z_1=1.0,\qquad
Z_2=-0.5,\qquad
Z_3=2.0.
$$

**Find.**

$$
\chi^2
=
Z_1^2+Z_2^2+Z_3^2.
$$

**Solution.**

$$
\chi^2
=
(1.0)^2+(-0.5)^2+(2.0)^2
$$

$$
=
1+0.25+4
=
\boxed{5.25}.
$$

Degrees of freedom:

$$
\boxed{\nu=3}.
$$

**Check.** The negative sign on $Z_2$ disappears when squared; chi-square cannot
be negative.

---

## 31.6 Sample Variance and Chi-Square Scaling

For a random sample of size $n$ from a normal population with variance
$\sigma^2$,

$$
\boxed{
\frac{(n-1)S^2}{\sigma^2}
\sim
\chi^2_{n-1}.
}
$$

This is the sampling-distribution relationship that makes chi-square useful for
variance inference.

Notice the structure:

- numerator contains the **sample variance**,
- denominator contains the **population variance**,
- degrees of freedom are
  $$n-1.$$

### Why variance leads to chi-square

Sample variance is built from squared deviations.

For normal data, properly standardized squared deviations combine into a
chi-square quantity.

That is why:

- inference about a mean uses $z$ or $t$,
- inference about one normal-population variance uses $\chi^2$.

### Worked Example 7 — Form the Chi-Square Variance Statistic

**Given.**

$$
n=10,
\qquad
s^2=4.00,
$$

and consider population variance

$$
\sigma^2=9.00.
$$

**Find.** The corresponding chi-square statistic.

**Solution.**

Degrees of freedom:

$$
\nu=n-1=9.
$$

Statistic:

$$
\chi^2
=
\frac{(n-1)s^2}{\sigma^2}
$$

$$
=
\frac{(9)(4)}{9}
$$

$$
=
\boxed{4.00}.
$$

**Check.** The sample variance is less than the population variance in the
denominator, so the scaled result is below its degrees-of-freedom count 9. That
direction is reasonable.

![FIG-01-31-006: Variance-to-chi-square transformation diagram. A normal population with variance sigma² feeds repeated samples of size n; each produces s². A scaling block applies chi-square=(n−1)s²/sigma² and outputs a chi-square curve with nu=n−1. A side note emphasizes that this result requires a normal population for the exact one-sample variance relationship.](../figures/FIG-01-31-006-sample-variance-chi-square.png)

### Reading the chi-square table

The Handbook's chi-square table is on printed p. 80.

Its critical values are indexed by:

- degrees of freedom $\nu$,
- upper-tail area $\alpha$.

The notation

$$
\boxed{
\chi^2_{\alpha,\nu}
}
$$

means

$$
\boxed{
P(\Chi^2>\chi^2_{\alpha,\nu})=\alpha.
}
$$

Because chi-square is not symmetric,

$$
\chi^2_{0.025,\nu}
$$

and

$$
\chi^2_{0.975,\nu}
$$

are not negatives of one another.

They are both positive and generally quite different.

For

$$
\nu=4,
$$

the Handbook table gives approximately

$$
\chi^2_{0.95,4}=0.7107
$$

and

$$
\chi^2_{0.05,4}=9.4877.
$$

That wide asymmetry is exactly what the shape predicts.

### Worked Example 8 — Interpret Two Chi-Square Critical Values

For

$$
\nu=4,
$$

consider

$$
0.7107
$$

and

$$
9.4877.
$$

By the table definition:

$$
P(\Chi^2>0.7107)\approx0.95,
$$

so

$$
P(\Chi^2<0.7107)\approx0.05.
$$

Likewise,

$$
P(\Chi^2>9.4877)\approx0.05.
$$

Therefore the probability between the two values is approximately

$$
1-0.05-0.05
=
\boxed{0.90}.
$$

So

$$
\boxed{
P(0.7107<\Chi^2<9.4877)\approx0.90
}
$$

for $\nu=4$.

**Check.** The interval is not symmetric around its midpoint. Chi-square itself
is asymmetric.

> ---
> **Mentor's Margin**
>
> Do not try to force chi-square into the normal-table mental model. There is no
> negative mirror tail. Read both tail columns explicitly.
>
> ---

---

## 31.7 Choosing Between $z$, $t$, and $\chi^2$

At this stage the distributions can look similar because all three appear in
standardization formulas.

The parameter being studied tells you which family to use.

### Mean, population $\sigma$ known

For a sample mean:

$$
\boxed{
Z
=
\frac{\bar X-\mu}{\sigma/\sqrt n}.
}
$$

Use the standard normal distribution.

### Mean, population $\sigma$ unknown

For a normal population, or where the intended $t$ procedure is justified:

$$
\boxed{
T
=
\frac{\bar X-\mu}{s/\sqrt n},
\qquad
\nu=n-1.
}
$$

Use Student's $t$ distribution.

### One population variance

For a normal population:

$$
\boxed{
\Chi^2
=
\frac{(n-1)S^2}{\sigma^2},
\qquad
\nu=n-1.
}
$$

Use the chi-square distribution.

![FIG-01-31-007: Distribution-selection flowchart. Start with "What parameter is being standardized?" Branch 1: Mean. Next question "Population sigma known?" Yes leads to z=(x-bar−mu)/(sigma/sqrt n), standard normal. No leads to t=(x-bar−mu)/(s/sqrt n), nu=n−1. Branch 2: One normal-population variance leads to chi-square=(n−1)s²/sigma², nu=n−1. Footer warns "distribution choice follows parameter + known information + assumptions."](../figures/FIG-01-31-007-z-t-chi-square-selection.png)

### Worked Example 9 — Select the Distribution Before Calculating

For each situation, choose the reference distribution.

**(a)** Mean shaft diameter from $n=25$, population standard deviation known from
a controlled long-run process study.

Use:

$$
\boxed{z}.
$$

**(b)** Mean tensile strength from $n=12$, population standard deviation unknown
and estimated from the sample, with a normal-population model.

Use:

$$
\boxed{t,\qquad \nu=11}.
$$

**(c)** Variability of a normal process based on a sample of $n=20$.

Use:

$$
\boxed{\chi^2,\qquad \nu=19}.
$$

The correct distribution is chosen **before** inserting numbers.

### Assumption discipline

For the exact small-sample one-sample $t$ and chi-square relationships in this
chapter, normal-population assumptions matter.

The Central Limit Theorem can make mean-based normal approximations robust for
large samples, but it does not make the chi-square variance result automatically
robust to strong nonnormality.

Variance procedures are more sensitive to population shape than many mean
procedures.

That distinction becomes important when you begin estimation and hypothesis
testing.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed p. 64 contains the sample mean,
> sample variance, and sample standard deviation. Printed p. 69 contains the
> Student's $t$ distribution and chi-square definition. Printed p. 78 contains
> the Student's $t$ critical-value table, and printed p. 80 contains the
> chi-square critical-value table. Printed pp. 74–76 later apply the same
> standardized forms in hypothesis tests and confidence intervals; those
> inferential procedures are deferred to following chapters.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Sample mean and sample variance | 64 | Defines $\bar X$, sample variance with denominator $n-1$, and sample standard deviation |
| Student's $t$ distribution | 69 | Gives the $t$ density, degrees of freedom $\nu=n-1$, and the standardized sample-mean form using $s/\sqrt n$ |
| $t$ symmetry | 69 | States $t_{1-\alpha,\nu}=-t_{\alpha,\nu}$ |
| Chi-square distribution | 69 | Defines chi-square as a sum of squares of independent unit-normal variables |
| Student's $t$ critical values | 78 | Tabulates $t_{\alpha,\nu}$ by upper-tail area and degrees of freedom |
| Chi-square critical values | 80 | Tabulates $\chi^2_{\alpha,\nu}$ by upper-tail area and degrees of freedom |
| Mean-test statistics | 74–75 | Uses $z$ when population spread is known and $t$ when spread is estimated from the sample |
| Variance-test statistic | 75 | Uses a chi-square statistic proportional to $(n-1)s^2/\sigma_0^2$ for a normal population |

### What this chapter derives explicitly

The Handbook prints the sample-variance formula and the relevant distributions,
but it does not stop to explain why $n-1$ represents the residual degrees of
freedom after estimating the mean. That interpretation is developed here.

Likewise, this chapter makes the distribution-selection logic explicit:

- mean + known $\sigma$ → $z$,
- mean + estimated $s$ → $t$,
- normal-population variance → $\chi^2$.

Those are guide-level organizing rules built from the Handbook formulas.

### Table-navigation discipline

For the $t$ table:

$$
t_{\alpha,\nu}
\quad\Longrightarrow\quad
\text{upper-tail area } \alpha.
$$

For the chi-square table:

$$
\chi^2_{\alpha,\nu}
\quad\Longrightarrow\quad
\text{upper-tail area } \alpha.
$$

Do not assume a table uses left-tail probabilities simply because the normal
table's $F(z)$ column does.

**Know without a lookup:**

- parameter versus statistic,
- $\nu=n-1$ for one sample after estimating one mean,
- $t=(\bar X-\mu)/(s/\sqrt n)$,
- $t$ is symmetric and heavier-tailed than normal for small $\nu$,
- chi-square is nonnegative and asymmetric,
- $(n-1)s^2/\sigma^2$ is the one-sample variance scaling for normal data,
- and the choice of reference distribution depends on both the parameter and
  what is known.

---

## Where This Goes Wrong

**Calling $\bar x$ a population mean.** It is a sample statistic estimating
$\mu$.

**Using $n$ instead of $n-1$ in the sample variance formula.**

**Saying $n-1$ is a magic correction factor.** It comes from the lost degree of
freedom after fitting the sample mean.

**Using $z$ when population $\sigma$ is unknown and a small-sample $t$ procedure
is intended.**

**Using $s$ but still reading the normal table.** Once the sample standard
deviation replaces population $\sigma$, the standardized variable follows the
$t$ reference model under the stated assumptions.

**Forgetting degrees of freedom when looking up $t$.**

**Using $\alpha$ instead of $\alpha/2$ for a symmetric two-tail region.**

**Treating $t$ as asymmetric.** Student's $t$ is symmetric about zero.

**Assuming $t$ and $z$ are always very different.** As $\nu$ grows, their
critical values converge.

**Allowing a negative chi-square value.** A sum of squares cannot be negative.

**Using symmetry for chi-square tails.** Chi-square is skewed.

**Assuming $\chi^2_{0.975,\nu}=-\chi^2_{0.025,\nu}$.** Both values are positive.

**Forgetting the normal-population assumption behind the exact sample-variance
chi-square relationship.**

**Using chi-square to analyze a mean.** Chi-square is the reference distribution
here for one normal-population variance, not the sample mean.

**Confusing sample variability with sampling variability.** The sample standard
deviation $s$ describes spread of observations within one sample; the standard
error describes variation of a statistic such as $\bar X$ across repeated
samples.

**Jumping ahead to a conclusion before selecting the reference distribution.**
Choose parameter, assumptions, statistic, degrees of freedom, and table first.

---

## Key Terms

| Term | Definition |
|---|---|
| population | complete collection of items or outcomes under study |
| sample | observed subset drawn from a population |
| parameter | fixed numerical characteristic of a population |
| statistic | numerical quantity computed from sample data |
| sampling distribution | probability distribution of a statistic over repeated samples |
| sample mean | arithmetic mean $\bar X$ of a sample |
| sample variance | spread statistic $s^2=\sum(x_i-\bar x)^2/(n-1)$ |
| sample standard deviation | $s=\sqrt{s^2}$ |
| degree of freedom | independent piece of information remaining after constraints or fitted quantities are accounted for |
| residual deviation | sample deviation $x_i-\bar x$ |
| Student's $t$ distribution | symmetric heavy-tailed reference distribution used when a normal-population mean is standardized with sample $s$ |
| $t$ statistic | $(\bar X-\mu)/(s/\sqrt n)$ |
| $t$ critical value | value leaving specified tail area under a $t$ distribution |
| chi-square distribution | distribution of a sum of squares of independent standard normal variables |
| chi-square statistic | standardized nonnegative quantity compared with a chi-square distribution |
| upper-tail area | probability to the right of a critical value |
| variance statistic | $(n-1)s^2/\sigma^2$ for a normal population |
| reference distribution | probability distribution used to interpret a standardized statistic |

---

## Review Questions

### Conceptual

1. Distinguish a population parameter from a sample statistic.
2. Why is $\bar X$ considered a random variable before the sample is collected?
3. Why does sample variance divide by $n-1$?
4. What does "degrees of freedom" mean in a one-sample variance calculation?
5. Why does replacing $\sigma$ with $s$ change the standard normal statistic into a $t$ statistic?
6. How does Student's $t$ differ from the standard normal for small degrees of freedom?
7. What does $t_{\alpha,\nu}$ mean geometrically?
8. Why can chi-square never be negative?
9. Why are chi-square critical values not symmetric about zero?
10. Which reference distribution is associated with a one-sample normal-population variance?

### Calculation

11. For data $4,6,8,10$, find $\bar x$.
12. For the same data, find the deviations from $\bar x$ and verify they sum to zero.
13. For the same data, find $s^2$ and $s$.
14. A sample has $n=16$, $\bar x=104$, $s=8$, and reference mean $\mu=100$. Find the $t$ statistic and degrees of freedom.
15. For $\nu=9$, the Handbook gives $t_{0.05,9}=1.833$. What upper-tail probability is associated with $t=1.833$?
16. For $\nu=9$, what two $t$ values bound the central 95% region if $t_{0.025,9}=2.262$?
17. Compute $\chi^2$ for standard normal values $1,-1,0.5,-2$.
18. A normal-population sample has $n=12$, $s^2=25$, and reference variance $\sigma^2=16$. Compute the chi-square statistic.
19. For $\nu=4$, the Handbook gives $\chi^2_{0.05,4}=9.4877$. What probability lies to the right of 9.4877?

### Multiple Choice

20. Which is a population parameter?
A) $\bar x$  B) $s$  C) $\mu$  D) sample range.

21. The one-sample sample variance denominator is:
A) $n+1$  B) $n$  C) $n-1$  D) $\sqrt n$.

22. For a sample of size 14 used to estimate one mean, the degrees of freedom are:
A) 12  B) 13  C) 14  D) 15.

23. If population $\sigma$ is unknown and replaced by sample $s$ in a normal-population mean problem, use:
A) $z$  B) $t$  C) $\chi^2$  D) binomial.

24. As $\nu$ increases, Student's $t$:
A) becomes more skewed  
B) approaches the standard normal  
C) becomes nonnegative only  
D) loses symmetry.

25. The notation $t_{0.025,9}$ identifies:
A) 2.5% area to the right  
B) 2.5% area to the left only  
C) 95% area to the right  
D) a chi-square critical value.

26. A chi-square random variable is:
A) always symmetric  
B) permitted to be negative  
C) nonnegative and generally right-skewed  
D) identical to $z$.

27. For one normal-population variance, the standardized statistic is:
A) $(\bar X-\mu)/(\sigma/\sqrt n)$  
B) $(\bar X-\mu)/(s/\sqrt n)$  
C) $(n-1)s^2/\sigma^2$  
D) $s/\bar X$.

---

## Answer Key with Explanations

### Conceptual

1. A parameter describes the entire population and is fixed, though perhaps
   unknown. A statistic is calculated from a sample and changes from sample to
   sample. (§31.1)

2. Before sampling, different random samples would produce different means, so
   $\bar X$ has its own probability distribution. (§31.1)

3. Estimating the sample mean imposes the constraint that the residual deviations
   sum to zero. Only $n-1$ deviations remain independently variable. (§31.2)

4. Degrees of freedom count the number of independent pieces of information left
   after required constraints or fitted quantities are accounted for. (§31.2)

5. $s$ is itself random. Its uncertainty makes the standardized sample mean more
   variable than when the true population $\sigma$ is known; Student's $t$
   captures that extra uncertainty. (§31.3)

6. It is symmetric like the normal distribution but has heavier tails and a lower
   central peak. The difference shrinks as $\nu$ increases. (§31.3)

7. $t_{\alpha,\nu}$ is the positive critical value with upper-tail probability
   $\alpha$ for a $t$ distribution with $\nu$ degrees of freedom. (§31.4)

8. It is constructed from a sum of squared quantities, and each square is
   nonnegative. (§31.5)

9. Chi-square is supported only on nonnegative values and is right-skewed rather
   than symmetric. (§31.5–31.6)

10. The chi-square distribution, using
    $(n-1)s^2/\sigma^2$ for normal-population data. (§31.6)

### Calculation

11.

    $$
    \bar x
    =
    \frac{4+6+8+10}{4}
    =
    \frac{28}{4}
    =
    \boxed{7}.
    $$

12. Deviations:

    $$
    -3,\ -1,\ 1,\ 3.
    $$

    Sum:

    $$
    -3-1+1+3
    =
    \boxed{0}.
    $$

13. Squared deviations:

    $$
    9,\ 1,\ 1,\ 9.
    $$

    Sum:

    $$
    20.
    $$

    Sample variance:

    $$
    s^2
    =
    \frac{20}{4-1}
    =
    \boxed{\frac{20}{3}\approx6.6667}.
    $$

    Sample standard deviation:

    $$
    s
    =
    \sqrt{\frac{20}{3}}
    \approx
    \boxed{2.5820}.
    $$

14.

    $$
    t
    =
    \frac{104-100}{8/\sqrt{16}}
    =
    \frac{4}{2}
    =
    \boxed{2.00}.
    $$

    Degrees of freedom:

    $$
    \nu=16-1=\boxed{15}.
    $$

15. By definition,

    $$
    P(T>1.833)
    =
    \boxed{0.05}
    $$

    for $\nu=9$.

16. Central 95% leaves 2.5% in each tail:

    $$
    \boxed{-2.262<T<2.262}.
    $$

17.

    $$
    \chi^2
    =
    1^2+(-1)^2+(0.5)^2+(-2)^2
    $$

    $$
    =
    1+1+0.25+4
    =
    \boxed{6.25}.
    $$

18.

    $$
    \chi^2
    =
    \frac{(12-1)(25)}{16}
    =
    \frac{275}{16}
    =
    \boxed{17.1875}.
    $$

    Degrees of freedom are

    $$
    \nu=11.
    $$

19. By the Handbook table definition,

    $$
    P(\Chi^2>9.4877)
    =
    \boxed{0.05}
    $$

    for $\nu=4$.

### Multiple Choice

20. **C.** $\mu$ is a population parameter. (§31.1)

21. **C.** Sample variance uses $n-1$. (§31.1–31.2)

22. **B.** $\nu=n-1=13$. (§31.2)

23. **B.** Replacing unknown population $\sigma$ with sample $s$ leads to
    Student's $t$ under the stated assumptions. (§31.3)

24. **B.** The $t$ distribution approaches standard normal as degrees of freedom
    increase. (§31.3)

25. **A.** The Handbook's $t_{\alpha,\nu}$ notation uses upper-tail area
    $\alpha$. (§31.4)

26. **C.** Chi-square is nonnegative and generally right-skewed. (§31.5)

27. **C.** The normal-population variance scaling is
    $(n-1)s^2/\sigma^2$. (§31.6)

---

## Practice Problems

1. **Sample statistics.** For data
   $$8,\ 9,\ 11,\ 12,\ 15,$$
   calculate $\bar x$, $s^2$, and $s$.

2. **Degrees of freedom.** A sample contains 18 observations and one sample mean
   is estimated. How many residual degrees of freedom remain? Explain why.

3. **Residual constraint.** Four of five deviations from a sample mean are
   $$-2,\ 1,\ 3,\ -4.$$
   Find the fifth deviation.

4. **$t$ statistic.** A normal-population sample has
   $$n=9,\quad \bar x=21.5,\quad s=3.0.$$
   Standardize relative to $\mu=20$ and state the degrees of freedom.

5. **$t$ table.** For $\nu=8$, the Handbook gives approximately
   $$t_{0.05,8}=1.860,\qquad t_{0.025,8}=2.306.$$
   A positive statistic is $t=2.00$.
   Bracket its upper-tail probability.

6. **Two-tail $t$ region.** For $\nu=8$, use
   $t_{0.025,8}=2.306$ to state the central 95% region.

7. **Chi-square construction.** Compute
   $$Z_1^2+Z_2^2+Z_3^2$$
   for
   $$Z_1=1.5,\quad Z_2=-1.0,\quad Z_3=0.5.$$

8. **Variance scaling.** A normal-population sample has
   $$n=15,\quad s^2=9.$$
   Compute the chi-square statistic associated with reference variance
   $$\sigma^2=6.$$

9. **Distribution selection.** Choose $z$, $t$, or $\chi^2$:
   (a) mean with known population $\sigma$;
   (b) mean with unknown $\sigma$, estimated by $s$;
   (c) one normal-population variance.

10. **Concept check.** Explain why increasing sample size makes $t$ critical
    values approach normal $z$ critical values.

---

## Practice Problem Solutions

1. Mean:

   $$
   \bar x
   =
   \frac{8+9+11+12+15}{5}
   =
   \frac{55}{5}
   =
   \boxed{11}.
   $$

   Deviations:

   $$
   -3,\ -2,\ 0,\ 1,\ 4.
   $$

   Squared deviations:

   $$
   9,\ 4,\ 0,\ 1,\ 16.
   $$

   Sum:

   $$
   30.
   $$

   Sample variance:

   $$
   s^2
   =
   \frac{30}{4}
   =
   \boxed{7.5}.
   $$

   Standard deviation:

   $$
   s
   =
   \sqrt{7.5}
   \approx
   \boxed{2.7386}.
   $$

2. One fitted mean consumes one independent constraint:

   $$
   \nu
   =
   n-1
   =
   18-1
   =
   \boxed{17}.
   $$

   The residual deviations must sum to zero, so once 17 are set the last one is
   determined.

3. The deviations must sum to zero:

   $$
   -2+1+3-4+d_5=0.
   $$

   The known deviations sum to

   $$
   -2.
   $$

   Therefore

   $$
   \boxed{d_5=2}.
   $$

4.

   $$
   \frac{s}{\sqrt n}
   =
   \frac{3}{3}
   =
   1.
   $$

   Therefore

   $$
   t
   =
   \frac{21.5-20}{1}
   =
   \boxed{1.5}.
   $$

   Degrees of freedom:

   $$
   \nu
   =
   9-1
   =
   \boxed{8}.
   $$

5. The Handbook values are

   $$
   t_{0.05,8}=1.860
   $$

   and

   $$
   t_{0.025,8}=2.306.
   $$

   Since

   $$
   1.860<2.00<2.306,
   $$

   the upper-tail probability satisfies

   $$
   \boxed{
   0.025<P(T>2.00)<0.05.
   }
   $$

6. A central 95% region leaves

   $$
   0.025
   $$

   in each tail.

   Therefore

   $$
   \boxed{
   -2.306<T<2.306.
   }
   $$

7.

   $$
   \chi^2
   =
   (1.5)^2+(-1)^2+(0.5)^2
   $$

   $$
   =
   2.25+1+0.25
   =
   \boxed{3.50}.
   $$

8. Degrees of freedom:

   $$
   \nu
   =
   15-1
   =
   14.
   $$

   Statistic:

   $$
   \chi^2
   =
   \frac{(14)(9)}{6}
   =
   \frac{126}{6}
   =
   \boxed{21.0}.
   $$

9. (a) Mean with known $\sigma$:

   $$\boxed{z}.$$

   (b) Mean with unknown $\sigma$, estimated by $s$:

   $$\boxed{t}.$$

   (c) One normal-population variance:

   $$\boxed{\chi^2}.$$

10. As sample size grows,

    $$
    \nu=n-1
    $$

    grows. The sample standard deviation $s$ becomes a more stable estimate of
    population $\sigma$, so the additional denominator uncertainty that produces
    the heavy $t$ tails diminishes. The $t$ distribution therefore approaches
    the standard normal distribution.

---

## Quick Reference

**Sample mean**

$$
\boxed{
\bar x
=
\frac{1}{n}
\sum_{i=1}^{n}x_i
}
$$

**Sample variance**

$$
\boxed{
s^2
=
\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar x)^2
}
$$

**Sample standard deviation**

$$
\boxed{s=\sqrt{s^2}}
$$

**Residual constraint**

$$
\boxed{
\sum_{i=1}^{n}(x_i-\bar x)=0
}
$$

**One-sample residual degrees of freedom**

$$
\boxed{\nu=n-1}
$$

**Known population $\sigma$**

$$
\boxed{
Z
=
\frac{\bar X-\mu}{\sigma/\sqrt n}
}
$$

**Unknown population $\sigma$**

$$
\boxed{
T
=
\frac{\bar X-\mu}{s/\sqrt n}
}
$$

with

$$
\boxed{\nu=n-1.}
$$

**$t$ critical value**

$$
\boxed{
P(T>t_{\alpha,\nu})=\alpha
}
$$

Symmetry:

$$
\boxed{
P(T<-t_{\alpha,\nu})=\alpha
}
$$

Central $1-\alpha$ region:

$$
\boxed{
-t_{\alpha/2,\nu}
<
T
<
t_{\alpha/2,\nu}.
}
$$

**Chi-square definition**

$$
\boxed{
\Chi^2
=
\sum_{i=1}^{\nu}Z_i^2
}
$$

with independent standard normal $Z_i$.

**Normal-population sample variance**

$$
\boxed{
\frac{(n-1)S^2}{\sigma^2}
\sim
\chi^2_{n-1}
}
$$

**Chi-square critical value**

$$
\boxed{
P(\Chi^2>\chi^2_{\alpha,\nu})=\alpha
}
$$

**Distribution selection**

mean + known $\sigma$ → $z$  
mean + unknown $\sigma$ estimated by $s$ → $t$  
one normal-population variance → $\chi^2$.

---

## What's Next

You now have the sampling distributions needed to move from descriptive
statistics into statistical estimation.

A sample mean is not the population mean.

A sample standard deviation is not the population standard deviation.

But the $z$, $t$, and chi-square reference distributions tell you how those
sample quantities behave relative to the population parameters they estimate.

**Chapter 01-32 — Estimation and Confidence Intervals** will use that machinery
to build:

- point estimates,
- margin of error,
- confidence intervals for a mean when $\sigma$ is known,
- confidence intervals for a mean when $\sigma$ is unknown,
- confidence intervals for a population variance,
- and sample-size calculations.

The Handbook develops confidence intervals on printed pp. 75–76 and supplies the
same normal, $t$, and chi-square critical-value tables used in this chapter.

Carry one rule forward:

> A confidence interval is built from a statistic plus or minus—or around—a
> sampling-distribution allowance for uncertainty.

The next chapter turns that statement into a calculation.

— Your Mentor
