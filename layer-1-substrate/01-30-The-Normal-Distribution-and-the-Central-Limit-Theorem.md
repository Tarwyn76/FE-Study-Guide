---
chapter: "01-30"
title: "The Normal Distribution and the Central Limit Theorem"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-030-01, MATH-1D-030-02, MATH-1D-030-03, MATH-1D-030-04, MATH-1D-030-05, MATH-1D-030-06, MATH-1D-030-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-30: The Normal Distribution and the Central Limit Theorem

> *"The normal distribution is useful not because every engineering quantity is normal, but because many sums, averages, and accumulated effects become close enough to normal that one standardized scale can answer a large class of engineering questions."*

---

## Before You Start

**Prerequisites:** [01-29 Random Variables and Probability Distributions](01-29-Random-Variables-and-Probability-Distributions.md) · [01-11 Trigonometric Functions and Identities](01-11-Trigonometric-Functions-and-Identities.md)

**Skip if:** You can identify the mean and standard deviation of a normal model; convert between $x$ and $z$; use the FE Reference Handbook's $F$, $R$, and $W$ columns correctly; compute one-sided, two-sided, and interval probabilities; reverse a normal probability to obtain a threshold; distinguish an individual observation from a sample mean; compute the mean and standard deviation of a sum and a sample mean; and explain what the Central Limit Theorem does and does not guarantee.

**Time:** About 100–120 min reading and worked examples · 40–50 min review questions · 65–80 min practice problems.

**Working convention:** Normal-distribution probabilities are areas. Always translate the verbal event into a shaded region or inequality before selecting a table column. Carry the $z$ value and probability with guard digits until the final report.

---

## On the Board Today

The normal distribution is the bell-shaped curve that appears throughout engineering statistics.

Its usefulness comes from two different facts. First, some physical quantities are reasonably modeled as normal because many small influences push the result up and down around a central value. Second, even when the underlying population is **not** normal, sums and averages of many independent, similarly distributed observations often become approximately normal. That is the Central Limit Theorem.

Those are different ideas:

- **normal population model:** the individual variable itself is modeled as normal;
- **Central Limit Theorem:** the distribution of a sum or average becomes approximately normal under stated conditions as sample size grows.

Most FE normal-distribution problems reduce to four moves:

1. identify the random quantity,
2. identify its mean and standard deviation,
3. standardize it,
4. match the requested area to the Handbook table.

The arithmetic is usually short. The interpretation determines whether the arithmetic is correct.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **30.1** Recognize the defining shape and parameters of a normal distribution
* **30.2** Interpret $\mu$ as location and $\sigma$ as scale for a normal variable
* **30.3** Convert an observation $x$ to a standard score $z$
* **30.4** Convert a standard score back to the original engineering units
* **30.5** Use the Handbook's $F(z)$, $R(z)$, and $W(z)$ normal-table columns
* **30.6** Compute left-tail, right-tail, central, and finite-interval probabilities
* **30.7** Use symmetry to handle negative $z$ values
* **30.8** Use normal fractiles to determine thresholds from specified probabilities
* **30.9** Distinguish the spread of individual observations from the spread of a sample mean
* **30.10** Compute the mean and standard deviation of sums and sample means
* **30.11** State and apply the Central Limit Theorem at the FE level
* **30.12** Recognize when a normal/CLT approximation is unsupported or requires caution

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $X$ | normal random variable | original engineering units |
| $x$ | one observed or threshold value | same units as $X$ |
| $\mu$ | population mean | center of the normal curve |
| $\sigma$ | population standard deviation | positive scale parameter |
| $\sigma^2$ | population variance | $\sigma^2=V[X]$ |
| $Z$ | standard normal random variable | mean 0, standard deviation 1 |
| $z$ | one standardized value | dimensionless |
| $F(z)$ | left-tail unit-normal probability | Handbook: area from $-\infty$ to $z$ |
| $R(z)$ | right-tail unit-normal probability | Handbook: area from $z$ to $\infty$ |
| $W(z)$ | central unit-normal probability | Handbook: area from $-z$ to $+z$ for $z\ge0$ |
| $\bar X$ | sample mean | average of $n$ observations |
| $n$ | sample size | number of observations |
| $\sigma_{\bar X}$ | standard deviation of $\bar X$ | $\sigma/\sqrt n$ for independent observations |

**Notation discipline.** A lowercase $x$ has physical units. A $z$ score is dimensionless because the numerator and denominator have the same units.

---

## 30.1 The Normal Distribution — Location, Scale, and Shape

A normal random variable has probability density

$$\boxed{f(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left[-\frac12\left(\frac{x-\mu}{\sigma}\right)^2\right]}$$

for $-\infty<x<\infty$, with $\sigma>0$.

You usually do **not** integrate this expression by hand on the FE exam. Its value is in understanding the parameters and then using the standardized table.

### What $\mu$ controls

The mean $\mu$ sets the center. For a normal distribution:

- mean = median = mode,
- the curve is symmetric about $\mu$,
- half the area lies below $\mu$,
- half lies above $\mu$.

### What $\sigma$ controls

The standard deviation controls spread. A smaller $\sigma$ produces a taller, narrower curve; a larger $\sigma$ produces a shorter, wider curve. Both curves still have total area 1.

The normal curve's inflection points occur at

$$\boxed{x=\mu-\sigma,\qquad x=\mu+\sigma.}$$

That feature is explicitly described in the FE Reference Handbook.

![FIG-01-30-001: Three normal curves on the same horizontal axis. All have the same total area. Two share mean mu but have different standard deviations, showing narrow/tall versus wide/short. A third is shifted to a different mean without changing spread. The central curve marks mu, mu−sigma, and mu+sigma, with inflection points at the latter two.](../figures/FIG-01-30-001-normal-location-scale.png)

### Worked Example 1 — Read Parameters Before Calculating

Two manufacturing processes are modeled as normal:

$$X_A\sim N(50,2^2)$$

and

$$X_B\sim N(50,5^2).$$

**Find.** Which process has the greater probability of producing values far from 50?

**Solution.** The means are identical, so both distributions are centered at 50. But $\sigma_A=2$ and $\sigma_B=5$. Process B has the larger standard deviation and therefore the wider distribution. Values far from 50 are more likely under process B.

**Check.** This conclusion comes from spread, not from the common mean.

### The 68–95–99.7 pattern

From the unit-normal table,

$$P(|Z|\le1)\approx0.6827,$$

$$P(|Z|\le2)\approx0.9545,$$

$$P(|Z|\le3)\approx0.9973.$$

This is often summarized as the **68–95–99.7 rule**. It is useful for mental checking, but it is not a substitute for the table when the problem gives a specific $z$ value.

> ---
> **Mentor's Margin**
>
> If an answer says that 40% of a normal population lies more than three standard deviations from the mean, stop. Before checking a formula, use the shape you already know: three standard deviations is deep in the tails.
>
> ---

---

## 30.2 Standardization — One Normal Curve for Every $\mu$ and $\sigma$

Every normal variable can be converted to the **standard normal** distribution, which has

$$\mu_Z=0,\qquad \sigma_Z=1.$$

The transformation is

$$\boxed{z=\frac{x-\mu}{\sigma}.}$$

The $z$ score tells you how many standard deviations the value lies from the mean:

- $z=0$: at the mean,
- $z=+1$: one standard deviation above,
- $z=-2$: two standard deviations below.

To return to engineering units,

$$\boxed{x=\mu+z\sigma.}$$

![FIG-01-30-002: Two aligned horizontal normal curves. The upper axis is in engineering units with marks mu−2sigma, mu−sigma, mu, mu+sigma, mu+2sigma. The lower standard-normal axis aligns those same points with z=−2,−1,0,+1,+2. A vertical mapping arrow shows z=(x−mu)/sigma and the reverse x=mu+z sigma.](../figures/FIG-01-30-002-standardization-map.png)

### Worked Example 2 — Convert a Measurement to $z$

**Given.** Shaft diameter is modeled as

$$X\sim N(25.00\text{ mm},0.10^2\text{ mm}^2).$$

A shaft measures $x=25.20$ mm.

**Find.** Its $z$ score.

**Solution.**

$$z=\frac{25.20-25.00}{0.10}=\boxed{2.00}.$$

The shaft is two standard deviations above the process mean.

**Unit check.** mm/mm = 1, so $z$ is dimensionless.

### Worked Example 3 — Convert a $z$ Threshold Back to Units

For the same process, find the diameter corresponding to $z=-1.5$.

$$x=\mu+z\sigma=25.00+(-1.5)(0.10)=\boxed{24.85\text{ mm}}.$$

**Check.** A negative $z$ must produce a value below the mean.

---

## 30.3 Using the Handbook Unit-Normal Table

The FE Reference Handbook includes a **Unit Normal Distribution** table on printed p. 77. For nonnegative table argument $z$, it provides

$$\boxed{F(z)=P(Z\le z)}$$

$$\boxed{R(z)=P(Z\ge z)}$$

and

$$\boxed{W(z)=P(-z\le Z\le z).}$$

Because the distribution is continuous, writing $<$ or $\le$ at a single endpoint does not change the probability.

The table also lists $2R(z)$, the combined probability in the two symmetric tails beyond $\pm z$.

### The columns are related

For $z\ge0$,

$$\boxed{F(z)+R(z)=1}$$

and

$$\boxed{W(z)=1-2R(z).}$$

Also,

$$\boxed{F(-z)=1-F(z)=R(z).}$$

The Handbook explicitly states the symmetry relationship $F(-x)=1-F(x)$.

### Example table values

| $z$ | $F(z)$ | $R(z)$ | $W(z)$ |
|---:|---:|---:|---:|
| 0.0 | 0.5000 | 0.5000 | 0.0000 |
| 1.0 | 0.8413 | 0.1587 | 0.6827 |
| 1.5 | 0.9332 | 0.0668 | 0.8664 |
| 2.0 | 0.9772 | 0.0228 | 0.9545 |
| 2.5 | 0.9938 | 0.0062 | 0.9876 |
| 3.0 | 0.9987 | 0.0013 | 0.9973 |

![FIG-01-30-003: Standard normal curve shown in four miniature panels tied to the FE Handbook table. Panel F shades from negative infinity to +z. Panel R shades from +z to infinity. Panel W shades the symmetric center from −z to +z. Panel 2R shades both tails beyond ±z. A table-column callout emphasizes matching the requested verbal event to the shaded region before selecting F, R, W, or 2R.](../figures/FIG-01-30-003-handbook-normal-table-columns.png)

### Worked Example 4 — Left Tail

**Given.** $X\sim N(100,15^2)$.

**Find.** $P(X\le115)$.

$$z=\frac{115-100}{15}=1.0.$$

The event is a left tail, so use $F(1.0)$:

$$P(X\le115)=F(1.0)=\boxed{0.8413}.$$

**Check.** 115 is above the mean, so the left-tail probability must exceed 0.5.

### Worked Example 5 — Right Tail

Using the same distribution, find $P(X>130)$.

$$z=\frac{130-100}{15}=2.0.$$

Use the right-tail column:

$$P(X>130)=R(2.0)=\boxed{0.0228}.$$

**Check.** Two standard deviations above the mean should leave only a few percent in the upper tail.

---

## 30.4 Symmetry and Finite Intervals

Not every requested probability is a single table column.

For a negative value,

$$P(Z<-1.5)=P(Z>1.5)=R(1.5)=\boxed{0.0668}.$$

For a central interval,

$$P(-1.5<Z<1.5)=W(1.5)=\boxed{0.8664}.$$

For an interval on one side,

$$P(1<Z<2)=F(2)-F(1)=0.9772-0.8413=\boxed{0.1359}.$$

For an interval crossing zero,

$$P(-1<Z<2)=F(2)-F(-1).$$

Since $F(-1)=R(1)=0.1587$,

$$P(-1<Z<2)=0.9772-0.1587=\boxed{0.8185}.$$

![FIG-01-30-004: A four-row normal-area translation chart. Row 1 shades Z<−z and maps it by symmetry to R(z). Row 2 shades −z<Z<z and maps to W(z). Row 3 shades a<Z<b on the positive side and maps to F(b)−F(a). Row 4 shades −a<Z<b across zero and maps to F(b)−F(−a). Each row pairs the inequality, shaded curve, and formula.](../figures/FIG-01-30-004-normal-area-translation.png)

### Worked Example 6 — Engineering Tolerance Band

**Given.** A process output is modeled as $X\sim N(50.0,2.0^2)$. A specification accepts values from 47.0 through 53.0.

**Find.** The fraction expected to meet specification.

Lower and upper standardized limits are

$$z_L=\frac{47-50}{2}=-1.5,$$

$$z_U=\frac{53-50}{2}=+1.5.$$

The band is symmetric, so

$$P(47\le X\le53)=W(1.5)=\boxed{0.8664}.$$

Expected nonconforming fraction:

$$1-0.8664=\boxed{0.1336}.$$

Because the limits are symmetric, each tail contains $0.0668$.

**Check.** The tail result agrees with $R(1.5)$.

---

## 30.5 Inverse Normal Problems and Fractiles

Sometimes the probability is known and the threshold is unknown. Reverse the process:

1. identify the required area,
2. find the corresponding standard-normal fractile $z$,
3. convert back with $x=\mu+z\sigma$.

The Handbook's unit-normal table includes common fractiles:

| Left-tail probability $F(z)$ | $z$ |
|---:|---:|
| 0.9000 | 1.2816 |
| 0.9500 | 1.6449 |
| 0.9750 | 1.9600 |
| 0.9800 | 2.0537 |
| 0.9900 | 2.3263 |
| 0.9950 | 2.5758 |

![FIG-01-30-005: Inverse-normal workflow. A left-tail normal curve is shaded to a specified cumulative probability, then an arrow goes to a Handbook fractile lookup, then to z, then through x=mu+z sigma to an engineering-unit threshold. A second miniature panel shows a two-sided 95% central region with 2.5% in each tail and z=±1.9600.](../figures/FIG-01-30-005-inverse-normal-fractiles.png)

### Worked Example 7 — Set a One-Sided Threshold

**Given.** Breaking strength is modeled as $X\sim N(500\text{ MPa},25^2\text{ MPa}^2)$.

**Find.** The value exceeded by only 5% of specimens.

"Exceeded by only 5%" means

$$P(X>x)=0.05,$$

so

$$P(X\le x)=0.95.$$

The Handbook fractile is $z=1.6449$. Therefore

$$x=500+(1.6449)(25)=541.1225\text{ MPa},$$

or

$$\boxed{x\approx541.1\text{ MPa}}.$$

**Check.** A 95th-percentile threshold must lie above the mean.

### Two-sided central percentages

A central 95% interval leaves 0.05 outside, or 0.025 in each tail. The upper cumulative probability is 0.975, corresponding to $z=1.9600$. Thus

$$\boxed{P(\mu-1.96\sigma\le X\le\mu+1.96\sigma)\approx0.95.}$$

This geometry will reappear in confidence intervals. The interpretation changes there: a confidence interval is about an estimated parameter, not simply the probability that one observation falls inside a band.

---

## 30.6 Sums, Averages, and Standard Error

Chapter 01-29 established that for independent random variables, means add and variances add.

Suppose $X_1,\ldots,X_n$ are independent and identically distributed with

$$E[X_i]=\mu$$

and

$$V[X_i]=\sigma^2.$$

### Sum

Define

$$Y=X_1+X_2+\cdots+X_n.$$

Then

$$\boxed{E[Y]=n\mu}$$

and

$$\boxed{V[Y]=n\sigma^2}.$$

Therefore

$$\boxed{\sigma_Y=\sigma\sqrt n.}$$

The absolute spread of the **sum** grows with $\sqrt n$.

### Sample mean

Define

$$\bar X=\frac1n\sum_{i=1}^nX_i.$$

Then

$$\boxed{E[\bar X]=\mu}$$

and

$$\boxed{V[\bar X]=\frac{\sigma^2}{n}.}$$

Therefore

$$\boxed{\sigma_{\bar X}=\frac{\sigma}{\sqrt n}.}$$

The quantity $\sigma/\sqrt n$ is the **standard error of the mean** when the population standard deviation $\sigma$ is known.

![FIG-01-30-006: Side-by-side sum and sample-mean scaling diagram. Left shows n independent Xi feeding a SUM block with mean n mu and standard deviation sigma sqrt(n). Right shows the same Xi feeding an AVERAGE block with mean mu and standard deviation sigma/sqrt(n). Below, normal-like curves for individual X and sample mean X-bar share center mu, with the X-bar curve narrower.](../figures/FIG-01-30-006-sum-mean-standard-error.png)

### Worked Example 8 — Individual Observation versus Sample Mean

**Given.** Individual fill mass has $\mu=500$ g and $\sigma=12$ g. Independent samples of $n=36$ containers are averaged.

**Find.** (a) $\mu_{\bar X}$, (b) $\sigma_{\bar X}$, and (c) the $z$ score corresponding to $\bar X=504$ g.

**Solution.**

$$\mu_{\bar X}=\boxed{500\text{ g}}.$$

$$\sigma_{\bar X}=\frac{12}{\sqrt{36}}=\boxed{2\text{ g}}.$$

Then

$$z=\frac{504-500}{2}=\boxed{2.0}.$$

If the sampling distribution is normal or adequately approximated as normal,

$$P(\bar X>504)=R(2.0)=\boxed{0.0228}.$$

**Critical distinction.** For one individual container,

$$z=\frac{504-500}{12}=0.333\ldots,$$

not 2.0. The standard deviation of individual observations and the standard error of a sample mean are not interchangeable.

---

## 30.7 The Central Limit Theorem

The Central Limit Theorem explains why normal methods apply far beyond perfectly normal populations.

At the FE level, suppose $X_1,\ldots,X_n$ are independent and identically distributed random variables with finite mean $\mu$ and variance $\sigma^2$.

For sufficiently large $n$, the sum

$$Y=X_1+\cdots+X_n$$

is approximately normal. Equivalently, the sample mean

$$\bar X=Y/n$$

is approximately normal with

$$\boxed{\mu_{\bar X}=\mu}$$

and

$$\boxed{\sigma_{\bar X}=\frac{\sigma}{\sqrt n}.}$$

### What the theorem says

As $n$ grows, the distribution of standardized sums or averages approaches a normal form under the theorem's conditions.

### What the theorem does not say

It does **not** say:

- the original population becomes normal,
- every small sample is normal,
- dependence between observations can be ignored,
- or "$n=30$ always works" as a universal law.

The required sample size depends on the underlying population. A nearly symmetric population may need only a modest $n$; a highly skewed or heavy-tailed population may require much more data.

![FIG-01-30-007: Central Limit Theorem progression. Top row shows three different non-normal parent distributions: right-skewed, uniform, and bimodal. Below each are sampling distributions of the mean for n=2, n=10, and n=40, progressively approaching bell-shaped curves centered at the same mu while narrowing as sigma/sqrt(n). A caption states "the parent distribution does not become normal; the distribution of sums/means does." ](../figures/FIG-01-30-007-central-limit-theorem.png)

### Worked Example 9 — CLT for a Skewed Population

**Given.** Individual service times have $\mu=8.0$ min and $\sigma=6.0$ min. The individual distribution is strongly right-skewed. For independent samples of $n=100$, estimate the probability that the sample mean exceeds 9.2 min.

**Solution.**

$$\mu_{\bar X}=8.0,$$

$$\sigma_{\bar X}=\frac{6.0}{\sqrt{100}}=0.60\text{ min}.$$

Then

$$z=\frac{9.2-8.0}{0.60}=2.0.$$

Therefore

$$P(\bar X>9.2)\approx R(2.0)=\boxed{0.0228}.$$

**Check.** The original variable need not be normal. The approximation is being applied to the mean of 100 independent observations.

### Worked Example 10 — CLT for a Sum

Suppose independent daily demand has $\mu=40$ units/day and $\sigma=8$ units/day. For 25 days, let total demand be

$$Y=\sum_{i=1}^{25}X_i.$$

**Find.** The mean and standard deviation of total demand and approximate $P(Y>1080)$.

$$\mu_Y=25(40)=1000.$$

$$\sigma_Y=8\sqrt{25}=40.$$

Standardize:

$$z=\frac{1080-1000}{40}=2.0.$$

Thus

$$P(Y>1080)\approx R(2.0)=\boxed{0.0228}.$$

**Check.** Sum and mean spreads move in opposite ways with $n$: $\sigma\sqrt n$ for a sum, $\sigma/\sqrt n$ for a mean.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook 10.6*, eighth printing, April 2026. Printed p. 68 introduces the normal distribution, standardization, the $F$, $R$, and $W$ table notation, and the Central Limit Theorem. Printed p. 77 contains the Unit Normal Distribution table and common fractiles. In the supplied PDF these correspond to PDF pages 74 and 83.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Normal Distribution (Gaussian Distribution) | 68 | Defines the normal PDF, identifies $\mu$ and $\sigma$, states unimodality and inflection points at $\mu\pm\sigma$ |
| Standardized / unit normal distribution | 68 | Defines the $\mu=0$, $\sigma=1$ case |
| Standardization | 68 | Gives the transformation $z=(x-\mu)/\sigma$ |
| Unit-normal table notation | 68 | Defines $F(x)$, $R(x)$, $W(x)$ and symmetry $F(-x)=1-F(x)$ |
| Central Limit Theorem | 68 | States that sums of independent identically distributed observations become approximately normal for large $n$ |
| Unit Normal Distribution table | 77 | Gives $f(x)$, $F(x)$, $R(x)$, $2R(x)$, $W(x)$, and common fractiles |

### Handbook table strategy

Before touching the table, write the event:

$$P(Z<1.5)\Rightarrow F(1.5),$$

$$P(Z>1.5)\Rightarrow R(1.5),$$

$$P(-1.5<Z<1.5)\Rightarrow W(1.5),$$

$$P(|Z|>1.5)\Rightarrow2R(1.5).$$

This is faster and safer than memorizing a table column by position.

### Guide-derived results

The formulas

$$E[\bar X]=\mu,\qquad \sigma_{\bar X}=\frac{\sigma}{\sqrt n}$$

and

$$E[Y]=n\mu,\qquad \sigma_Y=\sigma\sqrt n$$

follow directly from the linear-combination mean and independent-variance rules developed in Chapter 01-29. They are used here to operationalize the Handbook's Central Limit Theorem statement.

The **68–95–99.7 rule** is presented here as a useful interpretation of normal-table areas, not as a separate formula claimed from the Handbook text.

**Know without a lookup:** $z=(x-\mu)/\sigma$; positive $z$ is above the mean; negative $z$ is below; $F$ is left area; $R$ is right area; $W$ is symmetric center area; sample-mean standard error is $\sigma/\sqrt n$; and the CLT concerns the distribution of sums/averages, not transformation of the original population itself.

---

## Where This Goes Wrong

**Using variance in the $z$ denominator.** Standardization uses $\sigma$, not $\sigma^2$.

**Keeping units on $z$.** A $z$ score is dimensionless.

**Using the wrong table column.** A correct $z$ with the wrong area column still gives the wrong answer.

**Forgetting to state the requested region.** Translate "above," "below," "between," or "outside" before lookup.

**Using $F(z)$ for a right-tail problem.** Use $R(z)$ or $1-F(z)$.

**Handling negative $z$ incorrectly.** For the Handbook's positive-entry table, $F(-z)=R(z)$ for $z>0$.

**Confusing central area with one-sided area.** $W(1.96)$ is a central two-sided area; $F(1.96)$ is a left cumulative area.

**Using 1.96 for a one-sided 95% threshold.** One-sided 95% corresponds to $F(z)=0.95$, so $z=1.6449$. The value 1.96 corresponds to 97.5% left area and a central 95% two-sided region.

**Using $\sigma$ instead of $\sigma/\sqrt n$ for a sample mean.**

**Using $\sigma/\sqrt n$ for an individual observation.**

**Using $\sigma/\sqrt n$ for a sum.** A sum has standard deviation $\sigma\sqrt n$.

**Claiming that larger samples make the population less variable.** Sample size changes the distribution of the sample mean, not the physical spread $\sigma$ of individual observations.

**Saying the CLT makes raw data normal.** It applies to sums/averages under its conditions.

**Treating "$n\ge30$" as a theorem.** It is at most a rough classroom heuristic, not a universal requirement.

**Ignoring dependence.** Strongly dependent observations can invalidate the simple independent-sample formulas and ordinary CLT setup used here.

**Using the normal model simply because the curve is familiar.** A bounded, strongly skewed, multimodal, or discrete engineering variable may need another model.

---

## Key Terms

| Term | Definition |
|---|---|
| normal distribution | continuous symmetric bell-shaped distribution determined by $\mu$ and $\sigma$ |
| Gaussian distribution | another name for the normal distribution |
| normal density | probability density function of a normal random variable |
| standard normal distribution | normal distribution with mean 0 and standard deviation 1 |
| standard score | dimensionless $z=(x-\mu)/\sigma$ |
| $z$ score | number of standard deviations a value lies from the mean |
| left-tail probability | probability below a threshold |
| right-tail probability | probability above a threshold |
| central probability | probability between symmetric limits around the mean |
| fractile | value of a distribution corresponding to a specified cumulative probability |
| percentile | value below which a stated percentage of the distribution lies |
| sampling distribution | probability distribution of a statistic across repeated samples |
| sample mean | arithmetic mean $\bar X$ of sampled observations |
| standard error | standard deviation of a sampling distribution |
| standard error of the mean | $\sigma/\sqrt n$ for independent observations with known population $\sigma$ |
| Central Limit Theorem | result giving approximate normality of properly standardized sums/means under stated conditions as sample size grows |
| independent and identically distributed (iid) | observations sharing a common distribution and satisfying mutual independence |

---

## Review Questions

### Conceptual

1. What roles do $\mu$ and $\sigma$ play in a normal distribution?
2. Where are the inflection points of a normal curve?
3. What does a $z$ score of $-2$ mean physically?
4. What do the Handbook columns $F(z)$, $R(z)$, and $W(z)$ represent?
5. Why is $P(Z<-1.5)=P(Z>1.5)$?
6. Distinguish a one-sided 95% threshold from a central 95% interval.
7. What is the standard error of the mean?
8. Why does the distribution of $\bar X$ become narrower as $n$ grows?
9. State the Central Limit Theorem in words at the level used in this chapter.
10. What is wrong with the statement "the CLT makes the original population normal"?

### Calculation

11. For $X\sim N(80,10^2)$, find the $z$ score for $x=95$.
12. For the same distribution, find the $x$ value corresponding to $z=-1.2$.
13. Use $F(1.0)=0.8413$ to find $P(Z>1.0)$.
14. Use $F(2.0)=0.9772$ and $F(1.0)=0.8413$ to find $P(1<Z<2)$.
15. Using $R(1.5)=0.0668$, find $P(|Z|>1.5)$.
16. For $X\sim N(100,15^2)$, find $P(X<85)$ using the Handbook table.
17. A normal process has $\mu=40$ and $\sigma=4$. Find the 95th-percentile threshold using $z=1.6449$.
18. A population has $\mu=20$ and $\sigma=6$. For $n=36$, find $\mu_{\bar X}$ and $\sigma_{\bar X}$.
19. Independent observations have $\mu=12$ and $\sigma=3$. For a sum of $n=16$, find the sum's mean and standard deviation.

### Multiple Choice

20. The standardization formula is:
A) $z=(x-\mu)/\sigma$  
B) $z=(x-\sigma)/\mu$  
C) $z=x/\sigma^2$  
D) $z=(\mu-x)/\sigma^2$.

21. If $z=0$:
A) $x=0$ always  B) $x=\mu$  C) $x=\sigma$  D) $P(X=x)=1$.

22. The Handbook's $R(z)$ represents:
A) area left of $z$  B) area right of $z$  C) area between $-z$ and $z$  D) density height only.

23. The central probability between $-2$ and $+2$ is approximately:
A) 0.5000  B) 0.6827  C) 0.9545  D) 0.9973.

24. A one-sided upper 5% threshold uses approximately:
A) $z=0$  B) $z=1.0000$  C) $z=1.6449$  D) $z=1.9600$.

25. For independent observations with population standard deviation $\sigma$, the standard deviation of $\bar X$ is:
A) $\sigma n$  B) $\sigma\sqrt n$  C) $\sigma/n$  D) $\sigma/\sqrt n$.

26. For the sum of $n$ iid observations, the standard deviation is:
A) $\sigma/\sqrt n$  B) $\sigma\sqrt n$  C) $n\sigma$  D) $\sigma/n$.

27. The Central Limit Theorem primarily concerns:
A) every raw observation becoming normal  
B) the approximate distribution of sums or averages as sample size grows  
C) variance becoming zero  
D) every sample of size 30 being exactly normal.

---

## Answer Key with Explanations

### Conceptual

1. $\mu$ sets center/location; $\sigma$ sets horizontal spread/scale. (§30.1)
2. The inflection points are $\boxed{\mu-\sigma}$ and $\boxed{\mu+\sigma}$. (§30.1)
3. The observed value is two population standard deviations below the mean. (§30.2)
4. $F(z)$ is left cumulative area, $R(z)$ is right-tail area, and $W(z)$ is the symmetric central area between $-z$ and $+z$. (§30.3)
5. The standard normal distribution is symmetric about zero, so mirror-image tails have equal area. (§30.4)
6. A one-sided 95% upper cumulative threshold leaves 5% in one tail and uses $z=1.6449$. A central 95% interval leaves 2.5% in each tail and uses approximately $\pm1.9600$. (§30.5)
7. It is the standard deviation of the sampling distribution of the mean: $\sigma_{\bar X}=\sigma/\sqrt n$ for independent observations with known $\sigma$. (§30.6)
8. Averaging independent fluctuations causes partial cancellation. Variance of the mean is $\sigma^2/n$, so standard deviation decreases as $1/\sqrt n$. (§30.6)
9. Under the stated iid finite-variance setup, the distribution of properly scaled sums or sample means approaches a normal form as $n$ becomes sufficiently large. (§30.7)
10. The CLT concerns the **sampling distribution of sums/means**. It does not alter the distribution of individual observations. (§30.7)

### Calculation

11. $z=(95-80)/10=\boxed{1.5}$.
12. $x=80+(-1.2)(10)=\boxed{68}$.
13. $P(Z>1)=1-0.8413=\boxed{0.1587}$.
14. $P(1<Z<2)=0.9772-0.8413=\boxed{0.1359}$.
15. $P(|Z|>1.5)=2(0.0668)=\boxed{0.1336}$.
16. $z=(85-100)/15=-1$. Thus $P(X<85)=F(-1)=R(1)=\boxed{0.1587}$.
17. $x=40+(1.6449)(4)=\boxed{46.58\text{ approximately}}$.
18. $\mu_{\bar X}=\boxed{20}$ and $\sigma_{\bar X}=6/\sqrt{36}=\boxed{1}$.
19. $\mu_Y=16(12)=\boxed{192}$ and $\sigma_Y=3\sqrt{16}=\boxed{12}$.

### Multiple Choice

20. **A.** Standardization subtracts the mean and divides by the standard deviation. (§30.2)
21. **B.** $z=0$ means zero standard deviations from the mean, so $x=\mu$. (§30.2)
22. **B.** $R$ is the right-tail area. (§30.3)
23. **C.** The Handbook's $W(2.0)$ is approximately 0.9545. (§30.3)
24. **C.** The 95th percentile has left area 0.95 and $z=1.6449$. (§30.5)
25. **D.** The sample-mean standard error is $\sigma/\sqrt n$. (§30.6)
26. **B.** Independent variances add, giving sum standard deviation $\sigma\sqrt n$. (§30.6)
27. **B.** The theorem concerns the limiting shape of distributions of sums or averages, not exact normality of raw observations. (§30.7)

---

## Practice Problems

1. **Standardization.** A pressure measurement is modeled as $X\sim N(250\text{ kPa},15^2\text{ kPa}^2)$. Find the $z$ scores for 220 kPa and 280 kPa.
2. **Back transformation.** For Problem 1, find the physical pressures corresponding to $z=-1.5$ and $z=2.0$.
3. **Left tail.** A normal variable has $\mu=60$ and $\sigma=5$. Use $F(1.0)=0.8413$ to find $P(X\le65)$.
4. **Right tail.** For the same distribution, find $P(X>70)$ using $R(2.0)=0.0228$.
5. **Central specification.** A dimension is normal with $\mu=10.00$ mm and $\sigma=0.20$ mm. Specifications are 9.70 to 10.30 mm. Use $W(1.5)=0.8664$ to find the conforming fraction.
6. **One-sided percentile.** Strength is normal with $\mu=300$ MPa and $\sigma=20$ MPa. Find the 99th-percentile strength using $z=2.3263$.
7. **Sample mean.** Individual measurement noise has $\mu=0$ and $\sigma=4$ units. For $n=64$ independent readings, find the standard error of the mean and the $z$ score of $\bar X=1.0$.
8. **CLT probability.** A right-skewed population has $\mu=30$ and $\sigma=10$. For $n=100$ independent observations, use the CLT to approximate $P(\bar X>32)$.
9. **CLT sum.** Daily demand has $\mu=20$ units and $\sigma=5$ units. For 36 independent days, approximate $P(Y>750)$ for total demand $Y$.
10. **Interpretation.** A student claims: "Because $n=64$, individual observations have standard deviation $\sigma/8$." Explain the error and state which random quantity actually has that standard deviation.

---

## Practice Problem Solutions

1. For 220 kPa, $z=(220-250)/15=\boxed{-2.0}$. For 280 kPa, $z=(280-250)/15=\boxed{2.0}$.
2. At $z=-1.5$, $x=250-22.5=\boxed{227.5\text{ kPa}}$. At $z=2.0$, $x=250+30=\boxed{280\text{ kPa}}$.
3. $z=(65-60)/5=1$, so $P(X\le65)=F(1)=\boxed{0.8413}$.
4. $z=(70-60)/5=2$, so $P(X>70)=R(2)=\boxed{0.0228}$.
5. $z_L=-1.5$ and $z_U=+1.5$, so $P(9.70\le X\le10.30)=W(1.5)=\boxed{0.8664}$.
6. $x=300+(2.3263)(20)=300+46.526=\boxed{346.5\text{ MPa approximately}}$.
7. $\sigma_{\bar X}=4/\sqrt{64}=\boxed{0.5}$. Then $z=(1.0-0)/0.5=\boxed{2.0}$.
8. $\sigma_{\bar X}=10/\sqrt{100}=1$. Then $z=(32-30)/1=2$, so $P(\bar X>32)\approx R(2)=\boxed{0.0228}$.
9. $\mu_Y=36(20)=720$ and $\sigma_Y=5\sqrt{36}=30$. Thus $z=(750-720)/30=1$, so $P(Y>750)\approx R(1)=\boxed{0.1587}$.
10. The population standard deviation $\sigma$ describes individual observations and does not shrink because more observations are collected. The quantity with standard deviation $\sigma/\sqrt{64}=\sigma/8$ is the **sample mean** $\bar X$, not an individual $X_i$.

---

## Quick Reference

**Normal PDF**

$$\boxed{f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac12\left(\frac{x-\mu}{\sigma}\right)^2}}$$

**Standardization**

$$\boxed{z=\frac{x-\mu}{\sigma}}$$

$$\boxed{x=\mu+z\sigma}$$

**Unit normal**

$$\mu_Z=0,\qquad \sigma_Z=1.$$

**Handbook table**

$$F(z)=P(Z\le z)$$

$$R(z)=P(Z\ge z)$$

$$W(z)=P(-z\le Z\le z)$$

$$2R(z)=P(|Z|\ge z)$$

for $z\ge0$.

Symmetry:

$$\boxed{F(-z)=1-F(z)=R(z)}$$

**Useful central areas**

$$P(|Z|\le1)\approx0.6827$$

$$P(|Z|\le2)\approx0.9545$$

$$P(|Z|\le3)\approx0.9973$$

**Common fractiles**

$$F(1.2816)=0.9000$$

$$F(1.6449)=0.9500$$

$$F(1.9600)=0.9750$$

$$F(2.3263)=0.9900$$

$$F(2.5758)=0.9950$$

**Sum of $n$ iid observations**

$$\boxed{\mu_Y=n\mu}$$

$$\boxed{\sigma_Y=\sigma\sqrt n}$$

**Sample mean**

$$\boxed{\mu_{\bar X}=\mu}$$

$$\boxed{\sigma_{\bar X}=\frac{\sigma}{\sqrt n}}$$

**CLT workflow**

identify sum/mean · compute its mean · compute its standard deviation · standardize · use normal table · state approximation.

---

## What's Next

The normal distribution gives you probability areas once $\mu$ and $\sigma$ are known.

Engineering statistics often has a harder problem: $\sigma$ is **not** known and must be estimated from the same finite sample used to estimate the mean. That changes the reference distribution.

**Chapter 01-31 — Sampling Distributions, Student's t, and Chi-Square** will develop:

- the distinction between population parameters and sample statistics,
- degrees of freedom,
- Student's $t$ distribution when population $\sigma$ is unknown,
- chi-square behavior for variance,
- and the sampling-distribution ideas needed before confidence intervals and hypothesis tests.

The FE Reference Handbook places the $t$ and chi-square distributions immediately after the normal distribution and Central Limit Theorem on printed p. 69, with critical-value tables later in the section.

Carry one question forward:

> Is the population spread known, or am I estimating it from the sample?

That decision determines whether a normal $z$ method is appropriate or whether the next distribution is needed.

— Your Mentor
