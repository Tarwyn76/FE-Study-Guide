---
chapter: "01-29"
title: "Random Variables and Probability Distributions"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-029-01, MATH-1D-029-02, MATH-1D-029-03, MATH-1D-029-04, MATH-1D-029-05, MATH-1D-029-06, MATH-1D-029-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-29: Random Variables and Probability Distributions

> *"Probability begins with uncertain events. A random variable turns those events
> into numbers that can be summarized, combined, and used in engineering decisions."*

---

## Before You Start

**Prerequisites:** [01-28 Probability Fundamentals](01-28-Probability-Fundamentals.md) ·
[01-19 Antiderivatives and the Definite Integral](01-19-Antiderivatives-and-the-Definite-Integral.md)

**Skip if:** You can distinguish discrete from continuous random variables; build
and validate a probability mass function; interpret a probability density as area
rather than point probability; use a cumulative distribution function; compute
expected value, variance, standard deviation, and coefficient of variation;
propagate means and variances through independent linear combinations; recognize
a valid binomial experiment; and calculate exact binomial probabilities.

**Time:** About 105–125 min reading and worked examples · 40–50 min review
questions · 65–85 min practice problems.

**Working convention:** A distribution must satisfy its normalization rule before
any expected value or probability calculated from it can be trusted. For discrete
variables,

$$\sum_k P(X=x_k)=1.$$

For continuous variables,

$$\int_{-\infty}^{\infty}f(x)\,dx=1.$$

Normalization is the first check, not the last.

---

## On the Board Today

Chapter 01-28 treated probability as a property of **events**.

This chapter adds a numerical layer.

Suppose three components are tested and you care about how many fail. The physical
outcomes may be strings such as

$$PPF,\quad FPP,\quad PFF,\quad \ldots$$

but the engineering quantity of interest may simply be

$$X=\text{number of failed components}.$$

The random variable $X$ maps many detailed outcomes onto the numerical values

$$0,\ 1,\ 2,\ 3.$$

Once outcomes have numerical values, new questions become meaningful:

- What is the average value of $X$ over many repetitions?
- How much does $X$ vary?
- What is the probability that $X$ falls below a limit?
- How does a sum of uncertain quantities behave?
- What distribution describes the count of successes in repeated trials?

Those questions are answered by probability distributions.

The key discipline is to keep three objects separate:

1. the **random variable** $X$,
2. the **possible numerical values** $x$,
3. the **probability rule** assigned to those values.

Confusing the variable with one realized value is a small notation error that
quickly becomes a large reasoning error.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **29.1** Define a random variable as a numerical mapping from outcomes
* **29.2** Distinguish discrete and continuous random variables
* **29.3** Construct and validate a probability mass function
* **29.4** Interpret a probability density function and compute probabilities as areas
* **29.5** Construct and use cumulative distribution functions
* **29.6** Compute expected value for discrete and continuous random variables
* **29.7** Compute variance, standard deviation, and coefficient of variation
* **29.8** Evaluate the expected value of a function of a random variable
* **29.9** Compute the mean and variance of linear combinations of random variables
* **29.10** Identify when independence is required for variance addition
* **29.11** Recognize the assumptions of a binomial experiment and use the binomial PMF
* **29.12** Use binomial mean, variance, complements, and cumulative reasoning to check results

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $X$ | random variable | uppercase denotes the variable |
| $x$ | one possible numerical value of $X$ | lowercase denotes a value |
| $P(X=x)$ | point probability | meaningful for discrete variables |
| $f(x)$ | PMF or PDF depending on context | identify discrete vs continuous first |
| $F(x)$ | cumulative distribution function | $F(x)=P(X\le x)$ |
| $\mu$ | population mean / expected value | $\mu=E[X]$ |
| $\sigma^2$ | population variance | $V[X]$ |
| $\sigma$ | population standard deviation | $\sqrt{V[X]}$ |
| $E[g(X)]$ | expected value of a function of $X$ | weighted sum or integral |
| $Y=\sum a_iX_i$ | linear combination | coefficients $a_i$ are constants |
| $n$ | number of binomial trials | fixed before the experiment |
| $p$ | probability of success per trial | constant for a binomial model |
| $q$ | probability of failure | $q=1-p$ |
| $x$ | number of successes in a binomial model | integer $0,\ldots,n$ |

**Notation warning.** The Handbook uses the same symbol $f(x)$ for a discrete
probability mass function and a continuous probability density function. This is
standard, but the interpretation changes completely. For a discrete variable,
$f(x)$ is a probability at a point. For a continuous variable, $f(x)$ is a
density and probability comes from area.

---

## 29.1 Random Variables — From Outcomes to Numbers

A **random variable** is a rule that assigns a numerical value to each outcome in
a sample space.

The outcome itself need not be numerical.

Suppose two components are tested and each either passes (P) or fails (F):

$$S=\{PP,PF,FP,FF\}.$$

Define

$$X=\text{number of failures}.$$

Then

| Outcome | $X$ |
|---|---:|
| PP | 0 |
| PF | 1 |
| FP | 1 |
| FF | 2 |

Several outcomes can map to the same value of $X$.

That is the purpose of the random variable: it keeps the numerical feature you
care about and discards detail you do not need.

![FIG-01-29-001: Mapping diagram from a sample space to a random variable. On the left, outcomes PP, PF, FP, FF are shown as four labeled cards. Arrows map PP to X=0, PF and FP to X=1, and FF to X=2. On the right, the numeric axis 0,1,2 is labeled "random variable X = number of failures." A caption states that multiple physical outcomes may map to one numerical value.](../figures/FIG-01-29-001-random-variable-mapping.png)

### Discrete random variable

A random variable is **discrete** when its possible values are countable.

Examples:

- number of failed components,
- number of defects on a board,
- number of packets requiring retransmission,
- number of customers arriving in a fixed interval.

Discrete values often arise from counting.

### Continuous random variable

A random variable is **continuous** when it can take values over a continuum.

Examples:

- temperature,
- pressure,
- voltage,
- mass,
- time to failure,
- dimensional measurement.

A continuous measurement can, in principle, fall anywhere within an interval,
even though an instrument reports only finitely many digits.

### Worked Example 1 — Identify the Variable Type

Classify each random variable.

(a) $X=$ number of cracked welds in 50 inspected joints  
(b) $Y=$ measured diameter of a shaft  
(c) $Z=$ number of attempts required before a device boots successfully  
(d) $T=$ elapsed operating time until a relay fails

**Solution.**

(a) **Discrete** — it is a count.  
(b) **Continuous** — diameter varies along a continuum.  
(c) **Discrete** — attempts take integer values.  
(d) **Continuous** — elapsed time is modeled on a continuum.

**Check.** The issue is not whether a calculator displays decimals. The issue is
whether the model's possible values are countable or continuous.

---

## 29.2 Probability Mass Functions — Discrete Distributions

For a discrete random variable $X$, the **probability mass function (PMF)** assigns
probability to each possible value:

$$\boxed{
f(x_k)=P(X=x_k).
}$$

A valid PMF must satisfy two conditions:

$$\boxed{f(x_k)\ge0}$$

for every possible value and

$$\boxed{
\sum_k f(x_k)=1.
}$$

### Example PMF

Suppose the number of unscheduled stops during a shift has distribution:

| $x$ | 0 | 1 | 2 | 3 |
|---:|---:|---:|---:|---:|
| $P(X=x)$ | 0.50 | 0.30 | 0.15 | 0.05 |

Normalization check:

$$0.50+0.30+0.15+0.05=1.00.$$

Probability of at least two stops:

$$P(X\ge2)
=P(X=2)+P(X=3)$$

$$=0.15+0.05
=\boxed{0.20}.$$

![FIG-01-29-002: Discrete PMF displayed as vertical probability bars at x=0,1,2,3 with heights 0.50, 0.30, 0.15, 0.05. The bars are separated rather than connected. A side checklist states f(x)>=0 and sum f(x)=1. The bars at x=2 and x=3 are bracketed to illustrate P(X>=2)=0.20.](../figures/FIG-01-29-002-discrete-pmf.png)

### Worked Example 2 — Find an Unknown PMF Entry

**Given.**

| $x$ | 0 | 1 | 2 | 3 |
|---:|---:|---:|---:|---:|
| $P(X=x)$ | 0.18 | 0.34 | $k$ | 0.16 |

**Find.** $k$ and $P(X\le1)$.

**Solution.**

Normalization requires

$$0.18+0.34+k+0.16=1.$$

Therefore

$$k=1-0.68=\boxed{0.32}.$$

Then

$$P(X\le1)
=0.18+0.34
=\boxed{0.52}.$$

**Check.** All PMF entries lie between 0 and 1 and sum to 1.

### A PMF is not a histogram of raw data

A sample histogram is an empirical summary of observed data.

A PMF is a probability model.

Observed frequencies can be used to estimate a PMF, but the two objects are not
identical.

---

## 29.3 Probability Density Functions — Continuous Distributions

For a continuous random variable, probability is represented by **area under a
probability density function (PDF)**.

A valid PDF satisfies

$$\boxed{f(x)\ge0}$$

and

$$\boxed{
\int_{-\infty}^{\infty}f(x)\,dx=1.
}$$

Probability over an interval is

$$\boxed{
P(a\le X\le b)
=
\int_a^b f(x)\,dx.
}$$

### Point probability is zero

For a continuous variable,

$$\boxed{P(X=a)=0.}$$

That does **not** mean the value $a$ is impossible.

It means a single point has zero width and therefore zero area under a continuous
density.

As a result,

$$P(a<X<b)
=
P(a\le X\le b)
$$

for a continuous distribution.

Endpoint inclusion does not change the probability.

![FIG-01-29-003: Smooth continuous density curve f(x) above a horizontal x-axis. The area between a and b is shaded and labeled P(a<=X<=b)=integral_a^b f(x)dx. A single vertical line at x=a has zero area and is labeled P(X=a)=0. A normalization strip beneath shows total area under f(x) equals 1.](../figures/FIG-01-29-003-continuous-pdf-area.png)

### Worked Example 3 — Constant Density on an Interval

**Given.**

$$
f(x)=
\begin{cases}
0.10, & 0\le x\le10,\\
0, & \text{otherwise}.
\end{cases}
$$

**Find.**

(a) Verify normalization.  
(b) Find $P(2\le X\le5)$.  
(c) Find $P(X=4)$.

**Solution.**

(a)

$$
\int_0^{10}0.10\,dx
=0.10(10)
=1.
$$

So the density is normalized.

(b)

$$
P(2\le X\le5)
=
\int_2^5 0.10\,dx
=0.10(3)
=\boxed{0.30}.
$$

(c)

Because $X$ is continuous,

$$\boxed{P(X=4)=0}.$$

**Check.** The interval from 2 to 5 occupies 3 of the 10 equal-density units, so
0.30 is geometrically consistent.

### Density may exceed 1

A PDF value is not itself a probability.

A density can exceed 1 if its support is narrow enough, provided total area remains
1.

For example,

$$f(x)=2,\qquad 0\le x\le0.5$$

is valid because

$$2(0.5)=1.$$

This is one reason not to interpret the vertical PDF axis as "probability at x."

---

## 29.4 Cumulative Distribution Functions — Probability Up to a Value

The **cumulative distribution function (CDF)** is

$$\boxed{
F(x)=P(X\le x).
}$$

For a discrete random variable,

$$\boxed{
F(x)=\sum_{x_k\le x}P(X=x_k).
}$$

For a continuous random variable,

$$\boxed{
F(x)=\int_{-\infty}^{x}f(t)\,dt.
}$$

The integration variable $t$ is a dummy variable so that $x$ can remain the upper
limit.

### CDF properties

Every CDF must satisfy:

1. $0\le F(x)\le1$
2. $F(x)$ never decreases
3. $F(x)\to0$ as $x\to-\infty$
4. $F(x)\to1$ as $x\to+\infty$

For a continuous distribution with differentiable CDF,

$$\boxed{
f(x)=\frac{dF}{dx}.
}$$

### Discrete CDFs have steps

Using the PMF from §29.2:

| $x$ | $P(X=x)$ | $F(x)=P(X\le x)$ |
|---:|---:|---:|
| 0 | 0.50 | 0.50 |
| 1 | 0.30 | 0.80 |
| 2 | 0.15 | 0.95 |
| 3 | 0.05 | 1.00 |

The CDF jumps at each possible discrete value.

### Interval probabilities from a CDF

For any random variable,

$$\boxed{
P(a<X\le b)=F(b)-F(a).
}$$

For continuous variables, endpoint inclusion does not matter.

For discrete variables, it does. Be precise about whether the probability at
$a$ is included.

![FIG-01-29-004: Two-panel CDF comparison. Left panel starts from a discrete PMF and shows the corresponding right-continuous step CDF rising to 0.50, 0.80, 0.95, and 1.00. Right panel shows a smooth PDF and its smooth increasing CDF, with the accumulated area up to x linked by an arrow to F(x). A callout gives P(a<X<=b)=F(b)-F(a).](../figures/FIG-01-29-004-cdf-discrete-continuous.png)

### Worked Example 4 — Use the CDF Instead of Re-Summing

Using the discrete CDF above, find

$$P(1<X\le3).$$

**Solution.**

$$P(1<X\le3)
=F(3)-F(1)$$

$$=1.00-0.80
=\boxed{0.20}.$$

This includes $X=2$ and $X=3$, which agrees with the direct PMF sum

$$0.15+0.05=0.20.$$

**Check.** The two methods agree.

---

## 29.5 Expected Value, Variance, and Standard Deviation

A probability distribution tells you more than individual probabilities. It also
describes location and spread.

### Expected value — discrete

For a discrete random variable,

$$\boxed{
E[X]
=
\mu
=
\sum_k x_k f(x_k).
}$$

The expected value is a probability-weighted average.

It need not be a value that the random variable can actually take.

### Expected value — continuous

For a continuous random variable,

$$\boxed{
E[X]
=
\mu
=
\int_{-\infty}^{\infty}x f(x)\,dx.
}$$

### Expected value of a function

For $Y=g(X)$,

discrete:

$$\boxed{
E[g(X)]
=
\sum_k g(x_k)f(x_k)
}$$

continuous:

$$\boxed{
E[g(X)]
=
\int_{-\infty}^{\infty}g(x)f(x)\,dx.
}$$

You do not need to derive the full distribution of $Y$ merely to find its expected
value.

### Variance

Variance measures average squared distance from the mean:

$$\boxed{
V[X]
=
\sigma^2
=
E[(X-\mu)^2].
}$$

The computational identity is

$$\boxed{
V[X]
=
E[X^2]-\mu^2.
}$$

Standard deviation is

$$\boxed{
\sigma=\sqrt{V[X]}.
}$$

Variance has squared units. Standard deviation has the same units as $X$.

### Coefficient of variation

When the mean is nonzero and a relative spread is meaningful,

$$\boxed{
CV=\frac{\sigma}{\mu}.
}$$

Often it is reported as a percentage.

Do not use $CV$ mechanically when $\mu$ is zero or when the zero point of the
measurement scale is arbitrary.

![FIG-01-29-005: A discrete distribution with a vertical line at the mean mu and arrows showing deviations x-mu. Beside it, a formula ladder shows E[X]=sum x f(x), E[X^2]=sum x^2 f(x), variance=E[X^2]-mu^2, standard deviation=sqrt(variance), and CV=sigma/mu. A units note shows variance has squared units while standard deviation has the original units.](../figures/FIG-01-29-005-mean-variance-standard-deviation.png)

### Worked Example 5 — Mean and Spread of a Discrete Distribution

Use:

| $x$ | 0 | 1 | 2 | 3 |
|---:|---:|---:|---:|---:|
| $P(X=x)$ | 0.50 | 0.30 | 0.15 | 0.05 |

**Find.** $\mu$, $\sigma^2$, and $\sigma$.

**Solution.**

Mean:

$$
E[X]
=
0(0.50)+1(0.30)+2(0.15)+3(0.05)
$$

$$
=0.30+0.30+0.15
=\boxed{0.75}.
$$

Second moment:

$$
E[X^2]
=
0^2(0.50)+1^2(0.30)+2^2(0.15)+3^2(0.05)
$$

$$
=0.30+0.60+0.45
=1.35.
$$

Variance:

$$
\sigma^2
=
1.35-(0.75)^2
$$

$$
=1.35-0.5625
=\boxed{0.7875}.
$$

Standard deviation:

$$
\sigma
=
\sqrt{0.7875}
\approx
\boxed{0.8874}.
$$

**Check.** The random variable ranges only from 0 to 3, so a mean of 0.75 and
standard deviation under 1 are plausible.

### Worked Example 6 — Expected Cost Without Deriving a New Distribution

Suppose the cost associated with $X$ stops is

$$C=50+120X$$

dollars per shift.

From Worked Example 5,

$$E[X]=0.75.$$

By direct expectation,

$$E[C]
=
E[50+120X]
$$

$$
=50+120E[X]
$$

$$
=50+120(0.75)
=\boxed{\$140}.
$$

The average cost is not computed by substituting the most likely value of $X$.
It comes from the probability-weighted average.

---

## 29.6 Linear Combinations of Random Variables

Engineering totals often combine several uncertain quantities.

Let

$$
Y=a_1X_1+a_2X_2+\cdots+a_nX_n.
$$

### Mean of a linear combination

Expected value is linear:

$$\boxed{
E[Y]
=
a_1E[X_1]+a_2E[X_2]+\cdots+a_nE[X_n].
}$$

This result does **not** require independence.

### Variance of an independent linear combination

If the random variables are statistically independent,

$$\boxed{
V[Y]
=
a_1^2V[X_1]+a_2^2V[X_2]+\cdots+a_n^2V[X_n].
}$$

Therefore

$$\boxed{
\sigma_Y
=
\sqrt{
a_1^2\sigma_1^2+
a_2^2\sigma_2^2+
\cdots+
a_n^2\sigma_n^2
}.
}$$

The coefficients are squared in the variance calculation.

### Why independence matters

For two variables in general,

$$
V[X+Y]
=
V[X]+V[Y]+2\,\operatorname{Cov}(X,Y).
$$

If $X$ and $Y$ are independent, their covariance is zero and the simple
sum-of-variances formula follows.

This chapter does not develop covariance in detail; the important rule here is:

> Do not use variance addition unless the independence/uncorrelated condition
> required by the problem is justified.

![FIG-01-29-006: Linear-combination diagram. Independent random variables X1, X2, X3 enter weighted blocks a1, a2, a3 and combine into Y. Above, mean arrows combine linearly as a1 mu1 + a2 mu2 + a3 mu3. Below, variance arrows show squared coefficients a1² sigma1² + a2² sigma2² + a3² sigma3² with a bold "independent" condition attached.](../figures/FIG-01-29-006-linear-combination-random-variables.png)

### Worked Example 7 — Total Process Time

Two independent process stages have:

$$
E[X_1]=4.0\text{ min},
\qquad
\sigma_1=1.0\text{ min}
$$

and

$$
E[X_2]=6.0\text{ min},
\qquad
\sigma_2=2.0\text{ min}.
$$

Let

$$Y=X_1+X_2.$$

**Find.** $E[Y]$ and $\sigma_Y$.

**Solution.**

Mean:

$$
E[Y]
=
4.0+6.0
=
\boxed{10.0\text{ min}}.
$$

Variance:

$$
V[Y]
=
1.0^2+2.0^2
=
5.0\text{ min}^2.
$$

Standard deviation:

$$
\sigma_Y
=
\sqrt5
\approx
\boxed{2.236\text{ min}}.
$$

Notice:

$$
\sigma_Y\ne\sigma_1+\sigma_2.
$$

Independent random spread combines through **variance**, not by directly adding
standard deviations.

**Check.** Since the stages are independent, the combined standard deviation
should lie above the larger individual standard deviation 2.0 min but below the
direct sum 3.0 min. It does.

---

## 29.7 The Binomial Distribution

The **binomial distribution** models the number of successes in a fixed number of
independent trials.

A binomial model requires all four conditions:

1. fixed number of trials $n$,
2. two outcomes per trial, labeled success/failure,
3. trials are independent,
4. success probability $p$ remains constant from trial to trial.

Let

$$X=\text{number of successes in }n\text{ trials}.$$

Then

$$X=0,1,\ldots,n.$$

With

$$q=1-p,$$

the binomial PMF is

$$\boxed{
P(X=x)
=
\binom{n}{x}
p^x q^{\,n-x}.
}$$

The combination term counts which $x$ trials are the successes.

The probability term

$$p^xq^{n-x}$$

gives the probability of any one specific sequence containing exactly $x$
successes.

### Mean and variance

For a binomial random variable,

$$\boxed{\mu=np}$$

and

$$\boxed{\sigma^2=npq.}$$

Therefore

$$\boxed{
\sigma=\sqrt{npq}.
}$$

The supplied Handbook explicitly prints the binomial probability form and
variance; its distribution summary table also lists mean $np$.

![FIG-01-29-007: Binomial distribution concept figure. A row of n Bernoulli trial boxes shows success/failure outcomes with constant p and q. A bracket selects x success positions and points to C(n,x). Beneath, the PMF P(X=x)=C(n,x)p^xq^(n-x) is decomposed into "number of sequences" times "probability of each sequence." A side checklist shows fixed n, two outcomes, independent trials, constant p, plus mean np and variance npq.](../figures/FIG-01-29-007-binomial-model.png)

### Worked Example 8 — Exactly Two Failures

**Given.** Each of five independently tested modules fails with probability

$$p=0.08.$$

Let $X$ be the number of failures.

**Find.** $P(X=2)$.

**Solution.**

Here

$$n=5,\qquad x=2,\qquad p=0.08,\qquad q=0.92.$$

Therefore

$$
P(X=2)
=
\binom52(0.08)^2(0.92)^3.
$$

Since

$$\binom52=10,$$

$$
P(X=2)
=
10(0.0064)(0.778688)
$$

$$
=\boxed{0.0498360\text{ approximately}}.
$$

**Check.** The event is possible but relatively uncommon because the expected
number of failures is only

$$np=5(0.08)=0.40.$$

### Worked Example 9 — At Least One Failure

Using the same model, find

$$P(X\ge1).$$

The complement is

$$X=0.$$

So

$$
P(X\ge1)
=
1-P(X=0)
$$

$$
=
1-(0.92)^5
$$

$$
=
1-0.6590815232
$$

$$
=\boxed{0.3409185}.
$$

Directly summing $P(X=1)+\cdots+P(X=5)$ would give the same answer, but the
complement is faster and less error-prone.

### When a binomial model is invalid

A problem is **not binomial** when:

- the number of trials is not fixed,
- more than two outcome categories matter per trial,
- trials affect one another,
- or the success probability changes across trials.

For example, sampling components **without replacement** from a small finite lot
usually changes the success probability from draw to draw. Treating those draws
as independent binomial trials can be inaccurate.

> ---
> **Mentor's Margin**
>
> Do not choose a distribution because the formula looks familiar. First check
> the assumptions. Distribution selection is a modeling decision before it is a
> calculator decision.
>
> ---

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed pp. 66–68 of *Engineering
> Probability and Statistics* contain the material developed in this chapter.
> In the supplied PDF these correspond to PDF pages 72–74.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Random variables and discrete probability | 66 | Defines a random variable, discrete possible values, and the PMF $f(x_k)=P(X=x_k)$ |
| Probability Density Function | 66 | Defines continuous probability by integrating the density over an interval |
| Cumulative Distribution Functions | 66 | Defines discrete and continuous CDFs and states that $F(a)=P(X\le a)$ |
| Expected Values | 66–67 | Gives discrete expectation, continuous expectation, and $E[g(X)]$ |
| Variance and standard deviation | 67 | Gives variance forms and standard deviation |
| Coefficient of variation | 67 | Gives $\sigma/\mu$ |
| Combinations of Random Variables | 67 | Gives the mean of a linear combination and variance combination for statistically independent variables |
| Binomial Distribution | 67–68 | Gives $P(X=x)=C(n,x)p^xq^{n-x}$ and $\sigma^2=npq$ |
| Probability/Density summary table | later in the section | Lists standard distribution means and variances, including binomial mean $np$ |

### Handbook notation cautions

The Handbook uses $f(x)$ for both PMF and PDF. Always identify whether the random
variable is discrete or continuous before interpreting the expression.

For a discrete variable,

$$
f(x_k)=P(X=x_k).
$$

For a continuous variable,

$$
P(a\le X\le b)=\int_a^b f(x)\,dx.
$$

The same symbol does not imply the same pointwise meaning.

### What is developed beyond the table

This chapter adds several interpretive rules that are essential for using the
Handbook correctly:

- a continuous density value is not a point probability,
- $P(X=a)=0$ for a continuous model,
- discrete CDFs jump while continuous CDFs accumulate area smoothly,
- variance has squared units while standard deviation has the original units,
- the simple variance-addition rule depends on independence,
- and the four assumptions of the binomial model must be checked before applying
  the formula.

**Know without a lookup:**

- discrete versus continuous,
- PMF versus PDF,
- what a CDF means,
- how to distinguish $X$ from a possible value $x$,
- why expected value is a weighted average rather than "the most likely value,"
- why standard deviations do not simply add for independent quantities,
- and the four binomial assumptions.

---

## Where This Goes Wrong

**Calling every uncertain quantity continuous.** Counts are discrete even when a
calculator displays them with decimals.

**Calling every measurement discrete because the instrument has finite
resolution.** The mathematical model may still be continuous.

**Forgetting PMF normalization.** If the probabilities do not sum to 1, every
downstream result is suspect.

**Treating a PDF height as a probability.** Probability is area.

**Rejecting a PDF because $f(x)>1$.** Density can exceed 1; total area must equal
1.

**Assigning nonzero probability to one exact point of a continuous
distribution.**

$$P(X=a)=0.$$

**Using discrete endpoint logic on a continuous variable.** For continuous
variables, including or excluding isolated endpoints does not change probability.

**Forgetting that a discrete CDF includes point masses.** $F(a)=P(X\le a)$
includes the probability at $a$.

**Computing variance as $E[X^2]$ only.** You must subtract the squared mean:

$$V[X]=E[X^2]-\mu^2.$$

**Reporting variance in the original units.** Variance carries squared units.

**Adding standard deviations directly.** For independent linear combinations,
variances combine after coefficient squaring.

**Assuming independence because variables are different quantities.**
Independence is a probabilistic condition, not a naming condition.

**Using the independent variance formula for dependent variables.** Covariance
terms are then missing.

**Using a binomial model when probability changes from trial to trial.**

**Forgetting the combination factor in binomial probability.**
$p^xq^{n-x}$ describes one arrangement of successes and failures; the
combination counts how many such arrangements exist.

**Using $p$ for failure in one line and success in the next.** Define "success"
explicitly before substituting.

**Summing many binomial terms when a complement is shorter.** For "at least one,"
try $1-P(X=0)$ first.

---

## Key Terms

| Term | Definition |
|---|---|
| random variable | numerical function defined on outcomes of a random experiment |
| discrete random variable | random variable with countable possible values |
| continuous random variable | random variable modeled over a continuum of possible values |
| probability distribution | rule assigning probability behavior to the possible values of a random variable |
| probability mass function (PMF) | discrete rule $f(x)=P(X=x)$ |
| probability density function (PDF) | continuous nonnegative function whose interval areas give probabilities |
| cumulative distribution function (CDF) | $F(x)=P(X\le x)$ |
| expected value | probability-weighted long-run average, $E[X]$ |
| population mean | mean of a random-variable distribution, usually denoted $\mu$ |
| variance | expected squared deviation from the mean |
| population standard deviation | square root of population variance |
| coefficient of variation | ratio $\sigma/\mu$ when meaningful |
| second moment | expected value $E[X^2]$ |
| linear combination | weighted sum $a_1X_1+\cdots+a_nX_n$ |
| covariance | measure of paired variation appearing in variance of dependent sums |
| binomial experiment | fixed number of independent two-outcome trials with constant success probability |
| binomial distribution | distribution of the number of successes in a binomial experiment |
| Bernoulli trial | one two-outcome trial with success probability $p$ and failure probability $q=1-p$ |

---

## Review Questions

### Conceptual

1. What is the difference between an outcome and a random variable?
2. Distinguish discrete and continuous random variables and give one engineering example of each.
3. State the two requirements for a valid PMF.
4. Why is a PDF value not the same as a probability?
5. Why is $P(X=a)=0$ for a continuous random variable?
6. What does the CDF $F(x)$ represent?
7. Explain why a discrete CDF contains jumps.
8. Distinguish expected value from the most likely value.
9. Why does variance have squared units while standard deviation has the original units?
10. State the four conditions required for a binomial model.

### Calculation

11. A PMF has probabilities 0.25, 0.30, $k$, and 0.15. Find $k$.
12. For the PMF $P(X=0)=0.4$, $P(X=1)=0.4$, $P(X=2)=0.2$, find $P(X\ge1)$.
13. A continuous density is $f(x)=0.25$ on $0\le x\le4$. Find $P(1<X<3)$.
14. Using the same density, find $P(X=2)$.
15. For $P(X=0)=0.2$, $P(X=1)=0.5$, $P(X=2)=0.3$, find $E[X]$.
16. For the distribution in Question 15, find $E[X^2]$ and $V[X]$.
17. Independent variables have $\mu_1=5$, $\sigma_1=2$, $\mu_2=8$, $\sigma_2=3$. For $Y=2X_1-X_2$, find $E[Y]$ and $V[Y]$.
18. A binomial variable has $n=6$ and $p=0.20$. Find its mean and variance.
19. For the same binomial variable, find $P(X=0)$.

### Multiple Choice

20. Which quantity is a valid discrete random variable?
A) exact temperature in a pipe  
B) number of defective items in a sample  
C) elapsed lifetime of a bearing  
D) exact voltage across a resistor.

21. For a valid PMF:
A) probabilities may sum to any positive number  
B) each probability must exceed 1  
C) probabilities are nonnegative and sum to 1  
D) every possible value must have equal probability.

22. For a continuous random variable:
A) $P(X=a)=f(a)$  
B) $P(X=a)=0$  
C) $F(x)=f(x)$ always  
D) the PDF must stay below 1.

23. The CDF is:
A) $F(x)=P(X=x)$  
B) $F(x)=P(X\ge x)$  
C) $F(x)=P(X\le x)$  
D) $F(x)=1/f(x)$.

24. Variance may be computed as:
A) $E[X^2]-E[X]^2$  
B) $E[X^2]+E[X]^2$  
C) $\sqrt{E[X]}$  
D) $1-E[X]$.

25. For independent $X$ and $Y$:
A) $V[X+Y]=V[X]+V[Y]$  
B) $\sigma_{X+Y}=\sigma_X+\sigma_Y$ always  
C) $E[X+Y]=E[X]E[Y]$  
D) $V[X+Y]=0$.

26. A binomial model requires:
A) changing $p$ from trial to trial  
B) dependent trials  
C) a fixed number of independent two-outcome trials with constant $p$  
D) a continuous outcome.

27. For a binomial random variable:
A) $\mu=np$  
B) $\mu=n/p$  
C) $\sigma^2=n+p$  
D) $\sigma=npq$.

---

## Answer Key with Explanations

### Conceptual

1. An **outcome** is one possible physical result. A **random variable** maps
   outcomes to numerical values chosen to represent the feature of interest.
   (§29.1)

2. A discrete variable has countable possible values, such as number of failed
   components. A continuous variable is modeled over a continuum, such as
   pressure or elapsed time. (§29.1)

3. A PMF must satisfy $f(x)\ge0$ for all possible values and
   $\sum f(x)=1$. (§29.2)

4. A PDF is a density. Probability comes from **area**, so interval probabilities
   require an integral of the density. (§29.3)

5. A single point has zero width and therefore zero area under a continuous
   density. (§29.3)

6. $F(x)$ is the probability that the random variable is no greater than $x$:
   $F(x)=P(X\le x)$. (§29.4)

7. Each discrete point carries nonzero probability mass, so the cumulative total
   jumps by that amount at the point. (§29.4)

8. Expected value is a probability-weighted average. It may not equal the mode
   and may not even be one of the possible discrete values. (§29.5)

9. Variance averages squared deviations, so its units are squared. Standard
   deviation takes the square root and returns to the original units. (§29.5)

10. Fixed $n$; two outcomes per trial; independent trials; constant success
    probability $p$. (§29.7)

### Calculation

11.

    $$0.25+0.30+k+0.15=1$$

    so

    $$\boxed{k=0.30}.$$

12.

    $$P(X\ge1)=0.4+0.2=\boxed{0.60}.$$

    Equivalently,

    $$1-P(X=0)=1-0.4=0.60.$$

13.

    $$P(1<X<3)
    =\int_1^3 0.25\,dx
    =0.25(2)
    =\boxed{0.50}.$$

14. Continuous point probability:

    $$\boxed{P(X=2)=0}.$$

15.

    $$E[X]
    =0(0.2)+1(0.5)+2(0.3)
    =0.5+0.6
    =\boxed{1.1}.$$

16.

    $$E[X^2]
    =0^2(0.2)+1^2(0.5)+2^2(0.3)
    =0.5+1.2
    =\boxed{1.7}.$$

    Therefore

    $$V[X]
    =1.7-(1.1)^2
    =1.7-1.21
    =\boxed{0.49}.$$

17.

    $$E[Y]
    =2(5)-8
    =\boxed{2}.$$

    Because the variables are independent,

    $$V[Y]
    =2^2(2^2)+(-1)^2(3^2)
    =16+9
    =\boxed{25}.$$

18.

    $$\mu=np=6(0.20)=\boxed{1.20}.$$

    With $q=0.80$,

    $$\sigma^2=npq
    =6(0.20)(0.80)
    =\boxed{0.96}.$$

19.

    $$P(X=0)
    =\binom60(0.20)^0(0.80)^6
    =(0.80)^6
    =\boxed{0.262144}.$$

### Multiple Choice

20. **B.** A count of defective items is discrete. (§29.1)

21. **C.** PMF values must be nonnegative and sum to 1. (§29.2)

22. **B.** One exact point has zero probability under a continuous model.
    (§29.3)

23. **C.** $F(x)=P(X\le x)$. (§29.4)

24. **A.** $V[X]=E[X^2]-E[X]^2$. (§29.5)

25. **A.** Independent-variable variances add for a direct sum. Standard
    deviations generally do not. (§29.6)

26. **C.** Those are the defining binomial assumptions. (§29.7)

27. **A.** The binomial mean is $np$. Its variance is $npq$. (§29.7)

---

## Practice Problems

1. **Random-variable mapping.** Three devices are tested, each Pass or Fail.
   Let $X$ be the number that fail.
   (a) List the possible values of $X$.
   (b) How many physical outcomes map to $X=1$?

2. **PMF validation.** Determine whether the following is a valid PMF:
   $P(X=0)=0.10$, $P(X=1)=0.25$, $P(X=2)=0.40$, $P(X=3)=0.30$.
   If not, state exactly why.

3. **Unknown PMF value.** A discrete variable has
   $P(X=0)=0.15$, $P(X=1)=0.35$, $P(X=2)=k$, $P(X=3)=0.10$.
   Find $k$ and $P(X\ge2)$.

4. **Continuous density.** Let
   $$f(x)=\frac{x}{8},\qquad0\le x\le4,$$
   and zero otherwise.
   (a) Verify normalization.
   (b) Find $P(1\le X\le3)$.

5. **CDF from a PMF.** For
   $P(X=0)=0.20$, $P(X=1)=0.45$, $P(X=2)=0.25$, $P(X=3)=0.10$,
   construct $F(0)$, $F(1)$, $F(2)$, and $F(3)$.
   Then find $P(1<X\le3)$ using the CDF.

6. **Expected value and variance.** Using the PMF in Problem 5, calculate
   $\mu$, $E[X^2]$, $\sigma^2$, and $\sigma$.

7. **Function of a random variable.** Using Problem 5, define
   $$C=25+80X.$$
   Find $E[C]$.

8. **Independent linear combination.** Independent process times have
   $(\mu_1,\sigma_1)=(3,0.5)$ min and
   $(\mu_2,\sigma_2)=(7,1.2)$ min.
   For $Y=X_1+2X_2$, find $E[Y]$ and $\sigma_Y$.

9. **Binomial exact probability.** A component passes a test independently with
   probability 0.90. Five components are tested. Find the probability exactly
   four pass.

10. **Binomial complement.** A packet transmission fails independently with
    probability 0.03. Eight packets are sent. Find the probability that at least
    one packet fails.

---

## Practice Problem Solutions

1. Possible failure counts are

   $$\boxed{X=0,1,2,3}.$$

   Exactly one failure can occur as

   $$FPP,\quad PFP,\quad PPF,$$

   so

   $$\boxed{3\text{ outcomes}}.$$

2. Sum:

   $$0.10+0.25+0.40+0.30=1.05.$$

   Therefore it is **not** a valid PMF because the probabilities do not sum to 1.

3.

   $$0.15+0.35+k+0.10=1$$

   gives

   $$\boxed{k=0.40}.$$

   Then

   $$P(X\ge2)=0.40+0.10=\boxed{0.50}.$$

4. (a)

   $$\int_0^4 \frac{x}{8}\,dx
   =
   \left[\frac{x^2}{16}\right]_0^4
   =1.$$

   Normalized.

   (b)

   $$P(1\le X\le3)
   =
   \int_1^3\frac{x}{8}\,dx$$

   $$=
   \left[\frac{x^2}{16}\right]_1^3
   =
   \frac{9-1}{16}
   =\boxed{0.50}.$$

5.

   $$F(0)=0.20,$$

   $$F(1)=0.20+0.45=0.65,$$

   $$F(2)=0.90,$$

   $$F(3)=1.00.$$

   Therefore

   $$P(1<X\le3)
   =F(3)-F(1)
   =1.00-0.65
   =\boxed{0.35}.$$

6. Mean:

   $$\mu
   =0(0.20)+1(0.45)+2(0.25)+3(0.10)
   =0.45+0.50+0.30
   =\boxed{1.25}.$$

   Second moment:

   $$E[X^2]
   =1^2(0.45)+2^2(0.25)+3^2(0.10)$$

   $$=0.45+1.00+0.90
   =\boxed{2.35}.$$

   Variance:

   $$\sigma^2
   =2.35-(1.25)^2
   =2.35-1.5625
   =\boxed{0.7875}.$$

   Standard deviation:

   $$\sigma
   =\sqrt{0.7875}
   \approx\boxed{0.8874}.$$

7.

   $$E[C]
   =25+80E[X]
   =25+80(1.25)
   =\boxed{125}.$$

8.

   $$E[Y]
   =3+2(7)
   =\boxed{17\text{ min}}.$$

   Since $X_1$ and $X_2$ are independent,

   $$V[Y]
   =(1)^2(0.5)^2+(2)^2(1.2)^2$$

   $$=0.25+5.76
   =6.01.$$

   Therefore

   $$\sigma_Y
   =\sqrt{6.01}
   \approx\boxed{2.452\text{ min}}.$$

9. Let $X=$ number that pass.

   $$n=5,\qquad x=4,\qquad p=0.90,\qquad q=0.10.$$

   $$P(X=4)
   =
   \binom54(0.90)^4(0.10)$$

   $$=
   5(0.6561)(0.10)
   =\boxed{0.32805}.$$

10. Let failure be "success" for the binomial count.

    Probability of no failures:

    $$(0.97)^8\approx0.78374336.$$

    Therefore

    $$P(X\ge1)
    =1-(0.97)^8
    \approx\boxed{0.21625664}.$$

---

## Quick Reference

**Random variable**

A numerical mapping from outcomes to values.

Discrete = countable values.  
Continuous = continuum of values.

**Discrete PMF**

$$\boxed{
f(x_k)=P(X=x_k)
}$$

$$f(x_k)\ge0,\qquad
\sum_k f(x_k)=1.$$

**Continuous PDF**

$$\boxed{
P(a\le X\le b)
=
\int_a^b f(x)\,dx
}$$

$$f(x)\ge0,\qquad
\int_{-\infty}^{\infty}f(x)\,dx=1.$$

For continuous $X$:

$$\boxed{P(X=a)=0.}$$

**CDF**

$$\boxed{
F(x)=P(X\le x)
}$$

Discrete:

$$F(x)=\sum_{x_k\le x}P(X=x_k).$$

Continuous:

$$F(x)=\int_{-\infty}^{x}f(t)\,dt.$$

Interval:

$$\boxed{
P(a<X\le b)=F(b)-F(a).
}$$

**Expected value**

Discrete:

$$\boxed{
E[X]=\sum_kx_kf(x_k)
}$$

Continuous:

$$\boxed{
E[X]=\int_{-\infty}^{\infty}xf(x)\,dx
}$$

Function of $X$:

$$E[g(X)]
=
\sum g(x_k)f(x_k)
$$

or

$$E[g(X)]
=
\int g(x)f(x)\,dx.
$$

**Variance and standard deviation**

$$\boxed{
V[X]
=
E[(X-\mu)^2]
=
E[X^2]-\mu^2
}$$

$$\boxed{
\sigma=\sqrt{V[X]}.
}$$

$$CV=\frac{\sigma}{\mu}$$

when meaningful.

**Linear combination**

$$Y=\sum_i a_iX_i$$

$$\boxed{
E[Y]=\sum_i a_iE[X_i]
}$$

If independent:

$$\boxed{
V[Y]=\sum_i a_i^2V[X_i].
}$$

**Binomial**

Conditions:

fixed $n$ · two outcomes · independent trials · constant $p$.

$$q=1-p$$

$$\boxed{
P(X=x)
=
\binom nx p^xq^{n-x}
}$$

$$\boxed{\mu=np}$$

$$\boxed{\sigma^2=npq}$$

$$\boxed{\sigma=\sqrt{npq}}.$$

---

## What's Next

The binomial distribution showed how a particular physical experiment produces a
particular probability model.

The next chapter develops the distribution that appears most often in engineering
statistics:

**Chapter 01-30 — The Normal Distribution and the Central Limit Theorem.**

You will learn to:

- interpret the normal curve through $\mu$ and $\sigma$,
- standardize a value with a $z$ score,
- read the Handbook's unit-normal table correctly,
- convert left-tail, right-tail, and central probabilities,
- recognize when a normal model is appropriate,
- and use the Central Limit Theorem to understand why sums and averages so often
  become approximately normal.

The Handbook begins the normal distribution immediately after the binomial
material on printed p. 68.

Carry one idea forward:

> A distribution is not merely a formula. It is a model with assumptions,
> normalization, parameters, and a physical interpretation.

— Your Mentor
