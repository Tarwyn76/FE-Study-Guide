---
chapter: "01-38"
title: "Common Engineering Probability Distributions"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-038-01, MATH-1D-038-02, MATH-1D-038-03, MATH-1D-038-04, MATH-1D-038-05, MATH-1D-038-06, MATH-1D-038-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-38: Common Engineering Probability Distributions

> *"A probability distribution is not chosen because its equation looks
> familiar. It is chosen because its assumptions match the way the random
> quantity is generated."*

---

## Before You Start

**Prerequisites:** [01-28 Probability Fundamentals](01-28-Probability-Fundamentals.md) ·
[01-29 Random Variables and Probability Distributions](01-29-Random-Variables-and-Probability-Distributions.md)

**Skip if:** You can distinguish sampling with and without replacement; choose
between binomial and hypergeometric models; use the Poisson model for event
counts; distinguish geometric from negative-binomial waiting counts; compute
probabilities, means, and variances for uniform and triangular models; use the
exponential distribution as a waiting-time model; use the Weibull distribution
as a flexible lifetime model; and select a distribution from physical assumptions
rather than from formula appearance.

**Time:** About 110–130 min reading and worked examples · 40–50 min review
questions · 70–90 min practice problems.

**Working convention:** Every distribution problem begins with four questions:

1. Is the variable **discrete** or **continuous**?
2. What does it **count or measure**?
3. What assumptions define how observations are generated?
4. Which Handbook distribution matches those assumptions?

Only then should you substitute numbers.

---

## On the Board Today

Chapter 01-29 developed the binomial distribution in detail, and Chapter 01-30
focused on the normal distribution.

The FE Reference Handbook also provides a compact table of additional
probability and density functions on printed p. 85.

That table includes:

- hypergeometric,
- Poisson,
- geometric,
- negative binomial,
- uniform,
- exponential,
- Weibull,
- triangular,

along with their means and variances.

The formulas look similar enough that choosing by memory alone is dangerous.

Consider four engineering questions:

- How many defectives are found in a sample drawn **without replacement**?
- How many failures occur in a fixed interval of time?
- How many trials are required until the **first** success?
- How long until a component fails?

All involve uncertainty.

They do not use the same distribution.

The model comes from the experiment.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **38.1** Select a probability distribution from the structure of an engineering experiment
* **38.2** Apply the hypergeometric distribution to sampling without replacement
* **38.3** Apply the Poisson distribution to event counts over a fixed exposure
* **38.4** Distinguish geometric and negative-binomial waiting-count models
* **38.5** Apply uniform and triangular continuous distributions to bounded quantities
* **38.6** Apply the exponential distribution to waiting-time and lifetime models
* **38.7** Use the exponential survival and memoryless relationships
* **38.8** Apply the Weibull distribution as a flexible lifetime model
* **38.9** Interpret Weibull shape and scale parameters qualitatively
* **38.10** Compute means and variances from the Handbook parameterizations
* **38.11** Distinguish discrete event-count distributions from continuous waiting-time distributions
* **38.12** Reject a distribution when its physical assumptions are not satisfied

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $N$ | finite population size | hypergeometric |
| $r$ | number of successes in population, or target success count | meaning depends on distribution |
| $n$ | sample size / fixed number of draws | hypergeometric |
| $x$ | realized count | discrete models |
| $\lambda$ | Poisson mean event count | also Poisson variance |
| $p$ | success probability on each Bernoulli trial | geometric / negative binomial |
| $q$ | failure probability | $q=1-p$ |
| $y$ | trial count to the $r$th success | negative binomial |
| $a,b$ | lower and upper bounds | uniform / triangular |
| $m$ | mode of triangular distribution | $a\le m\le b$ |
| $\beta$ | scale parameter | exponential and Weibull Handbook notation |
| $\alpha$ | Weibull shape parameter | positive |
| $\Gamma(\cdot)$ | gamma function | used in Weibull mean and variance |
| $F(x)$ | cumulative distribution function | $P(X\le x)$ |
| $S(x)$ | survival probability | $P(X>x)=1-F(x)$ |

**Parameterization warning.** Probability distributions can be written using
different parameter conventions in different books. This chapter follows the
forms listed in the supplied FE Reference Handbook 10.6.

---

## 38.1 Model Selection — Start with the Experiment

Before memorizing equations, classify the random quantity.

### Discrete count models

Use a discrete distribution when the outcome is a count such as

$$
0,1,2,\ldots
$$

or a trial number such as

$$
1,2,3,\ldots.
$$

Common questions:

- number of defectives in a sample,
- number of arrivals in an hour,
- trial number of the first success,
- trial number of the $r$th success.

### Continuous measurement models

Use a continuous distribution for quantities such as:

- time,
- length,
- load,
- lifetime,
- uncertain bounded parameter.

### Selection map

| Question structure | Candidate model |
|---|---|
| fixed sample without replacement from finite population | hypergeometric |
| count of events in a fixed exposure with constant mean rate | Poisson |
| trial number until first success | geometric |
| trial number until $r$th success | negative binomial |
| all values in a bounded interval equally likely | uniform |
| bounded interval with a most likely value | triangular |
| nonnegative waiting time with constant hazard / memoryless model | exponential |
| flexible positive lifetime model | Weibull |

![FIG-01-38-001: Distribution-selection flowchart. Start with discrete versus continuous. Discrete branches: finite sampling without replacement -> hypergeometric; event count over exposure -> Poisson; trials until first success -> geometric; trials until rth success -> negative binomial. Continuous branches: bounded equally likely -> uniform; bounded with mode -> triangular; constant-hazard waiting time -> exponential; flexible lifetime/hazard -> Weibull.](../figures/FIG-01-38-001-distribution-selection.png)

### Worked Example 1 — Choose the Model Before Calculating

Identify the best model family.

**(a)** Sample 8 circuit boards without replacement from a lot of 50 containing
6 defective boards; count defectives.

$$
\boxed{\text{Hypergeometric}}
$$

because the sample comes from a finite population without replacement.

**(b)** Count particles detected during a fixed 10-second interval when events are
modeled by a constant average rate.

$$
\boxed{\text{Poisson}}
$$

**(c)** Repeated independent trials with constant success probability until the
first success.

$$
\boxed{\text{Geometric}}
$$

**(d)** Time to failure with constant hazard.

$$
\boxed{\text{Exponential}}
$$

**(e)** Lifetime where the failure tendency may increase or decrease with age.

$$
\boxed{\text{Weibull}}
$$

The formula is chosen after the physical structure is identified.

---

## 38.2 Hypergeometric Distribution — Sampling Without Replacement

The **hypergeometric distribution** models the number of successes in a sample
drawn without replacement from a finite population.

Let:

- $N$ = population size,
- $r$ = number of successes in the population,
- $n$ = sample size,
- $X$ = number of successes in the sample.

Then

$$
\boxed{
P(X=x)
=
\frac{
\binom{r}{x}
\binom{N-r}{n-x}
}{
\binom{N}{n}
}.
}
$$

The numerator counts favorable samples:

- choose $x$ successes from the $r$ available,
- choose $n-x$ failures from the $N-r$ available.

The denominator counts all possible samples of size $n$.

### Mean and variance

The Handbook table gives

$$
\boxed{
\mu
=
\frac{nr}{N}.
}
$$

and

$$
\boxed{
\sigma^2
=
n
\left(\frac{r}{N}\right)
\left(1-\frac{r}{N}\right)
\frac{N-n}{N-1}.
}
$$

Equivalent form:

$$
\boxed{
\sigma^2
=
\frac{
nr(N-r)(N-n)
}{
N^2(N-1)
}.
}
$$

The factor

$$
\frac{N-n}{N-1}
$$

is the **finite-population correction** for the variance.

![FIG-01-38-002: Hypergeometric sampling diagram. A finite lot of N items contains r marked successes and N-r non-successes. A sample of n is drawn without replacement. A callout shows favorable combinations C(r,x) C(N-r,n-x) divided by total combinations C(N,n). A comparison strip contrasts changing success probability without replacement with constant-p binomial sampling.](../figures/FIG-01-38-002-hypergeometric-without-replacement.png)

### Worked Example 2 — Defectives in a Finite Lot

A lot contains

$$
N=20
$$

components, of which

$$
r=4
$$

are defective.

A sample of

$$
n=5
$$

is drawn without replacement.

Find

$$
P(X=2).
$$

Use

$$
P(X=2)
=
\frac{
\binom42\binom{16}{3}
}{
\binom{20}{5}
}.
$$

Compute:

$$
\binom42=6,
$$

$$
\binom{16}{3}=560,
$$

$$
\binom{20}{5}=15504.
$$

Therefore

$$
P(X=2)
=
\frac{3360}{15504}
\approx
\boxed{0.2167}.
$$

Mean:

$$
\mu
=
\frac{(5)(4)}{20}
=
\boxed{1}.
$$

### Hypergeometric versus binomial

The binomial model assumes constant success probability across independent
trials.

Without replacement, the composition of the remaining population changes after
each draw.

If the sample is a very small fraction of a large population, a binomial
approximation may sometimes be reasonable, but the Handbook table itself gives
the exact hypergeometric model for finite sampling without replacement.

---

## 38.3 Poisson Distribution — Counts Over an Exposure

The **Poisson distribution** models a nonnegative event count under a constant
mean-count model.

The Handbook form is

$$
\boxed{
P(X=x)
=
\frac{
e^{-\lambda}\lambda^x
}{
x!
},
\qquad
x=0,1,2,\ldots
}
$$

where

$$
\lambda>0
$$

is the expected count over the specified exposure.

### Mean and variance

The Handbook table gives

$$
\boxed{
\mu=\lambda
}
$$

and

$$
\boxed{
\sigma^2=\lambda.
}
$$

Therefore

$$
\boxed{
\sigma=\sqrt{\lambda}.
}
$$

This equality of mean and variance is a useful diagnostic of the basic Poisson
model.

![FIG-01-38-003: Poisson event-count figure. A time axis of fixed duration contains randomly spaced event ticks. Above it, lambda is labeled expected number of events in the interval. Beside it, discrete bars for x=0,1,2,... show a Poisson PMF. A formula box states mean=lambda and variance=lambda.](../figures/FIG-01-38-003-poisson-counts.png)

### Worked Example 3 — Events in a Fixed Interval

A detector records an average of

$$
\lambda=2.5
$$

events per observation interval.

Find the probability of exactly 3 events.

$$
P(X=3)
=
\frac{
e^{-2.5}(2.5)^3
}{
3!
}.
$$

Since

$$
3!=6,
$$

$$
P(X=3)
\approx
\boxed{0.2138}.
$$

### Worked Example 4 — No Events and At Least One Event

Using the same model,

$$
P(X=0)
=
e^{-2.5}
\approx
0.08208.
$$

Therefore

$$
P(X\ge1)
=
1-P(X=0)
$$

$$
=
1-e^{-2.5}
$$

$$
\approx
\boxed{0.9179}.
$$

The complement is much faster than summing infinitely many probabilities.

### Exposure scaling

If a constant-rate model has average rate

$$
\rho
$$

per unit exposure and the exposure length is

$$
t,
$$

then the expected count is

$$
\boxed{
\lambda=\rho t.
}
$$

That rate-times-exposure relation is a guide-level modeling interpretation of the
Handbook's Poisson parameter, not a separate formula printed in the summary
table.

---

## 38.4 Geometric and Negative-Binomial Distributions — Waiting in Trials

These distributions count how many Bernoulli trials are required to obtain
successes.

The trials are modeled as independent with constant success probability

$$
p.
$$

### Geometric distribution

Let

$$
X
=
\text{trial number on which the first success occurs}.
$$

Then

$$
X=1,2,3,\ldots
$$

and the Handbook gives

$$
\boxed{
P(X=x)
=
p(1-p)^{x-1}.
}
$$

Mean:

$$
\boxed{
\mu=\frac1p.
}
$$

Variance:

$$
\boxed{
\sigma^2
=
\frac{1-p}{p^2}.
}
$$

### Negative-binomial distribution

Let

$$
Y
=
\text{trial number on which the }r\text{th success occurs}.
$$

Then

$$
y=r,r+1,\ldots
$$

and

$$
\boxed{
P(Y=y)
=
\binom{y-1}{r-1}
p^r(1-p)^{y-r}.
}
$$

Mean:

$$
\boxed{
\mu=\frac rp.
}
$$

Variance:

$$
\boxed{
\sigma^2
=
\frac{r(1-p)}{p^2}.
}
$$

The geometric distribution is the special case

$$
r=1.
$$

![FIG-01-38-004: Bernoulli-trial sequence comparison. Top row shows failures followed by the first success at trial x, labeled geometric. Bottom row shows failures and successes until the rth success occurs at trial y, labeled negative binomial. Formula callouts show p(1-p)^(x-1) and C(y-1,r-1)p^r(1-p)^(y-r).](../figures/FIG-01-38-004-geometric-negative-binomial.png)

### Worked Example 5 — First Success

Each independent test succeeds with probability

$$
p=0.20.
$$

Find the probability that the first success occurs on trial 4.

The first three must fail, then the fourth must succeed:

$$
P(X=4)
=
(0.80)^3(0.20)
$$

$$
=
\boxed{0.1024}.
$$

Expected trial number of first success:

$$
E[X]
=
\frac1{0.20}
=
\boxed{5}.
$$

### Worked Example 6 — Third Success on Trial 7

Let

$$
p=0.30,
\qquad
r=3.
$$

Find the probability that the third success occurs on trial 7.

The seventh trial must be a success.

Among the first six trials, exactly two must be successes:

$$
P(Y=7)
=
\binom62
(0.30)^3
(0.70)^4.
$$

Thus

$$
P(Y=7)
\approx
\boxed{0.0973}.
$$

The combination term is

$$
\binom62,
$$

not

$$
\binom73,
$$

because the final trial is already fixed as the $r$th success.

---

## 38.5 Uniform and Triangular Distributions — Bounded Continuous Models

Some engineering uncertainties are naturally bounded.

### Uniform distribution

For

$$
a\le X\le b,
$$

a uniform model assigns constant density

$$
\boxed{
f(x)
=
\frac1{b-a}.
}
$$

The mean is

$$
\boxed{
\mu
=
\frac{a+b}{2}.
}
$$

The variance is

$$
\boxed{
\sigma^2
=
\frac{(b-a)^2}{12}.
}
$$

Because the density is constant, interval probability is proportional to interval
length.

For

$$
a\le c<d\le b,
$$

$$
\boxed{
P(c\le X\le d)
=
\frac{d-c}{b-a}.
}
$$

### Triangular distribution

A triangular model uses:

- lower bound $a$,
- upper bound $b$,
- mode $m$,

with

$$
a\le m\le b.
$$

Its density is

$$
\boxed{
f(x)
=
\begin{cases}
\dfrac{2(x-a)}{(b-a)(m-a)}, & a\le x\le m,\\[8pt]
\dfrac{2(b-x)}{(b-a)(b-m)}, & m<x\le b,\\[8pt]
0, & \text{otherwise.}
\end{cases}
}
$$

The Handbook table gives

$$
\boxed{
\mu
=
\frac{a+b+m}{3}
}
$$

and

$$
\boxed{
\sigma^2
=
\frac{
a^2+b^2+m^2-ab-am-bm
}{18}.
}
$$

A triangular model is useful when only a plausible minimum, maximum, and most
likely value are available.

That interpretation is guide-developed; the Handbook table supplies the density,
mean, and variance.

![FIG-01-38-005: Side-by-side bounded PDFs. Left: uniform rectangle between a and b with constant height 1/(b-a), mean at midpoint. Right: triangular density rising from a to mode m and falling to b, with a, m, b labeled. Formula boxes show the two means and variances.](../figures/FIG-01-38-005-uniform-triangular.png)

### Worked Example 7 — Uniform Probability

A measurement error is modeled uniformly between

$$
-0.5
$$

and

$$
+0.5.
$$

Find

$$
P(-0.1\le X\le0.2).
$$

Total width:

$$
b-a
=
1.0.
$$

Requested width:

$$
0.2-(-0.1)
=
0.3.
$$

Therefore

$$
P(-0.1\le X\le0.2)
=
\frac{0.3}{1.0}
=
\boxed{0.30}.
$$

### Worked Example 8 — Triangular Mean and Variance

Suppose project duration is modeled by a triangular distribution with

$$
a=4,
\qquad
m=6,
\qquad
b=10
$$

days.

Mean:

$$
\mu
=
\frac{4+6+10}{3}
=
\boxed{\frac{20}{3}\approx6.667\text{ days}}.
$$

Variance:

$$
\sigma^2
=
\frac{
4^2+10^2+6^2
-(4)(10)
-(4)(6)
-(10)(6)
}{18}.
$$

So

$$
\sigma^2
=
\frac{16+100+36-40-24-60}{18}
$$

$$
=
\frac{28}{18}
$$

$$
=
\boxed{1.5556\text{ day}^2}.
$$

Thus

$$
\sigma
\approx
\boxed{1.247\text{ days}}.
$$

---

## 38.6 Exponential Distribution — Waiting Time with Constant Hazard

The Handbook table gives the exponential density in scale-parameter form:

$$
\boxed{
f(x)
=
\frac1\beta
e^{-x/\beta},
\qquad
x\ge0,
\quad
\beta>0.
}
$$

Mean:

$$
\boxed{
\mu=\beta.
}
$$

Variance:

$$
\boxed{
\sigma^2=\beta^2.
}
$$

Thus

$$
\boxed{
\sigma=\beta.
}
$$

### CDF and survival probability

Integrating the density gives

$$
F(x)
=
1-e^{-x/\beta}
$$

for

$$
x\ge0.
$$

Therefore the survival probability is

$$
\boxed{
S(x)
=
P(X>x)
=
e^{-x/\beta}.
}
$$

### Constant hazard interpretation

The exponential model corresponds to a constant hazard rate

$$
\boxed{
h=\frac1\beta.
}
$$

This is the continuous waiting-time counterpart of a memoryless process.

The memoryless relationship is

$$
\boxed{
P(X>s+t\mid X>s)
=
P(X>t).
}
$$

The Handbook table supplies the exponential density, mean, and variance. The CDF,
survival, hazard, and memoryless interpretation are guide-developed consequences
of that density.

![FIG-01-38-006: Exponential waiting-time figure. Left panel shows a decreasing exponential PDF beginning at 1/beta. Right panel shows survival S(t)=e^(-t/beta), with mean beta marked on the time axis. A memoryless inset compares surviving an additional t after already surviving s with a fresh t interval.](../figures/FIG-01-38-006-exponential-waiting-time.png)

### Worked Example 9 — Exponential Lifetime

A component lifetime is modeled exponentially with mean

$$
\beta=500\text{ h}.
$$

Find the probability it survives beyond

$$
800\text{ h}.
$$

Use

$$
S(800)
=
e^{-800/500}
=
e^{-1.6}.
$$

Therefore

$$
\boxed{
P(X>800)
\approx0.2019.
}
$$

Probability of failure by 800 h:

$$
F(800)
=
1-0.2019
=
\boxed{0.7981}.
$$

**Check.** Because 800 h exceeds the mean lifetime 500 h, survival should be
well below 0.5.

---

## 38.7 Weibull Distribution — Flexible Lifetime Modeling

The Weibull distribution generalizes the exponential lifetime model.

Using the Handbook's shape-scale notation,

$$
\alpha>0,
\qquad
\beta>0,
$$

the density is

$$
\boxed{
f(x)
=
\frac{\alpha}{\beta}
\left(
\frac{x}{\beta}
\right)^{\alpha-1}
e^{-(x/\beta)^\alpha},
\qquad
x\ge0.
}
$$

### Mean

The Handbook table gives

$$
\boxed{
\mu
=
\beta
\Gamma\left(
1+\frac1\alpha
\right).
}
$$

Equivalent form:

$$
\mu
=
\beta
\Gamma\left(
\frac{\alpha+1}{\alpha}
\right).
$$

### Variance

$$
\boxed{
\sigma^2
=
\beta^2
\left[
\Gamma\left(
1+\frac2\alpha
\right)
-
\Gamma^2\left(
1+\frac1\alpha
\right)
\right].
}
$$

### CDF and survival

Integrating the density gives

$$
\boxed{
F(x)
=
1-e^{-(x/\beta)^\alpha}
}
$$

and

$$
\boxed{
S(x)
=
e^{-(x/\beta)^\alpha}.
}
$$

### Shape interpretation

The shape parameter changes the lifetime behavior.

A useful engineering interpretation is:

- $\alpha=1$: Weibull becomes exponential,
- $\alpha>1$: failure tendency increases with age,
- $\alpha<1$: failure tendency decreases with age.

The density/mean/variance are grounded in the Handbook table. The hazard-based
interpretation is guide-developed engineering context.

![FIG-01-38-007: Weibull lifetime comparison. Three curves or hazard sketches are labeled alpha<1 decreasing failure tendency, alpha=1 constant hazard/exponential, and alpha>1 increasing failure tendency. A formula strip shows S(t)=exp[-(t/beta)^alpha] and notes beta as the scale parameter.](../figures/FIG-01-38-007-weibull-shape-parameter.png)

### Worked Example 10 — Weibull Survival

A component lifetime follows a Weibull model with

$$
\alpha=2,
\qquad
\beta=1000\text{ h}.
$$

Find the probability of surviving beyond

$$
800\text{ h}.
$$

Use

$$
S(800)
=
e^{-(800/1000)^2}.
$$

Therefore

$$
S(800)
=
e^{-0.64}
\approx
\boxed{0.5273}.
$$

So the modeled probability of failure by 800 h is

$$
1-0.5273
=
\boxed{0.4727}.
$$

### Exponential as a Weibull special case

Set

$$
\alpha=1.
$$

Then

$$
S(x)
=
e^{-(x/\beta)}
$$

and

$$
f(x)
=
\frac1\beta e^{-x/\beta}.
$$

That is exactly the exponential model.

This special-case relationship is a useful check when moving between the two
distributions.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed p. 85 contains the table
> *Probability and Density Functions: Means and Variances*. It lists binomial
> coefficient, binomial, hypergeometric, Poisson, geometric, negative binomial,
> multinomial, uniform, gamma, exponential, Weibull, normal, and triangular
> distributions. The table provides an equation plus mean and variance for each
> listed distribution. Earlier printed pp. 66–68 provide the PMF/PDF/CDF,
> expected-value, variance, binomial, and normal foundations used to interpret
> the table. fileciteturn177file0

| Handbook distribution | Printed page | Developed here |
|---|---:|---|
| Hypergeometric | 85 | sampling without replacement, PMF, mean, variance |
| Poisson | 85 | count PMF, mean, variance |
| Geometric | 85 | first-success trial count, PMF, mean, variance |
| Negative binomial | 85 | $r$th-success trial count, PMF, mean, variance |
| Uniform | 85 | PDF, mean, variance, interval probability |
| Exponential | 85 | PDF, mean, variance |
| Weibull | 85 | PDF, mean, variance |
| Triangular | 85 | piecewise PDF, mean, variance |

### Distributions in the table not developed as separate sections here

The same Handbook table also lists:

- multinomial,
- gamma,
- normal,
- binomial.

Binomial and normal were already developed in Chapters 01-29 and 01-30.
Multinomial and gamma remain available in the Handbook table, but the established
scope of this chapter is the set named at the end of Chapter 01-37. They are
therefore not silently expanded into additional major sections here.

### Guide-developed interpretation

The Handbook summary table is formula-focused. This chapter adds:

- model-selection questions,
- the finite-population interpretation of hypergeometric sampling,
- rate-times-exposure interpretation of the Poisson parameter,
- the "trial of first success" and "trial of $r$th success" narratives,
- interval probability for the uniform model,
- the bounded-engineering-estimate interpretation of the triangular model,
- survival, hazard, and memoryless consequences of the exponential density,
- Weibull survival and qualitative shape-parameter interpretation.

Those additions are consequences or modeling context, not quotations from the
Handbook table.

**Know without a lookup:**

- without replacement → hypergeometric,
- count over exposure → Poisson,
- first success trial → geometric,
- $r$th success trial → negative binomial,
- bounded equally likely → uniform,
- bounded with a mode → triangular,
- constant-hazard waiting time → exponential,
- flexible positive lifetime → Weibull.

---

## Where This Goes Wrong

**Choosing binomial for sampling without replacement from a small finite lot.**

**Using the hypergeometric population-success count $r$ as though it were a
probability.**

**Forgetting that hypergeometric draws are dependent.**

**Using a Poisson model without defining the exposure interval.**

**Treating $\lambda$ as a rate when it has already been specified as the expected
count for the complete exposure.**

**Forgetting the factorial in the Poisson PMF.**

**Using geometric $x=0$.** Under the Handbook form used here, the first success
can occur on trial 1, so

$$
x=1,2,\ldots.
$$

**Using $\binom yr$ in the negative-binomial PMF.** The last trial is already
fixed as the $r$th success, so choose the prior $r-1$ successes from the first
$y-1$ trials.

**Confusing a waiting count with a waiting time.** Geometric and negative
binomial are discrete. Exponential and Weibull are continuous.

**Treating a uniform PDF height as an interval probability.** Probability is
area.

**Using a triangular distribution without satisfying**

$$
a\le m\le b.
$$

**Calling $\beta$ a rate in the Handbook exponential parameterization.**
Here $\beta$ is the mean/scale; the corresponding constant hazard is $1/\beta$.

**Assuming every lifetime is exponential.** Exponential imposes a constant
hazard.

**Using Weibull shape $\alpha$ and scale $\beta$ without stating the
parameterization.**

**Assuming $\alpha=2$ means the mean is $2\beta$.** Weibull mean uses the gamma
function.

**Choosing the model by resemblance of the equation rather than the experiment
that generated the data.**

---

## Key Terms

| Term | Definition |
|---|---|
| hypergeometric distribution | discrete model for success count in finite sampling without replacement |
| finite-population correction | factor reducing hypergeometric variance because sampling depletes the population |
| Poisson distribution | discrete event-count model parameterized by expected count $\lambda$ |
| Poisson parameter | expected event count over the specified exposure |
| geometric distribution | discrete model for trial number of the first success |
| negative-binomial distribution | discrete model for trial number of the $r$th success |
| waiting count | number of discrete trials required to reach a success criterion |
| uniform distribution | continuous bounded distribution with constant density |
| triangular distribution | bounded continuous distribution described by minimum, maximum, and mode |
| exponential distribution | continuous nonnegative waiting-time model with constant hazard |
| survival function | $S(x)=P(X>x)$ |
| hazard | instantaneous failure/event tendency conditional on survival |
| memoryless property | future exponential survival probability does not depend on elapsed survival time |
| Weibull distribution | flexible positive continuous lifetime distribution with shape and scale parameters |
| Weibull shape parameter | $\alpha$, controlling distribution/hazard shape |
| Weibull scale parameter | $\beta$, setting the lifetime scale |
| event count | discrete number of events in a defined exposure |
| exposure | time, area, volume, length, or other domain over which events are counted |

---

## Review Questions

### Conceptual

1. What distinguishes a hypergeometric model from a binomial model?
2. What does the Poisson parameter $\lambda$ represent?
3. Why are Poisson mean and variance numerically equal?
4. What random quantity does the geometric distribution model?
5. What random quantity does the negative-binomial distribution model?
6. What physical assumption distinguishes a uniform distribution from a triangular distribution?
7. What does the exponential scale parameter $\beta$ equal?
8. What does the exponential memoryless property mean?
9. What role does the Weibull shape parameter $\alpha$ play?
10. Why should distribution selection begin with the experiment rather than the equation?

### Calculation

11. A finite lot has $N=30$ items, $r=6$ successes, and a sample of $n=5$. Find the hypergeometric mean.
12. Using Question 11, compute the hypergeometric variance.
13. For a Poisson variable with $\lambda=4$, find $P(X=0)$.
14. For a Poisson variable with $\lambda=4$, find $P(X\ge1)$.
15. If $p=0.25$, find the geometric mean and variance.
16. If $p=0.40$ and $r=3$, find the negative-binomial mean.
17. A uniform variable lies on $[2,10]$. Find its mean and variance.
18. An exponential lifetime has $\beta=200$ h. Find $P(X>300)$.
19. A triangular distribution has $a=2$, $m=5$, $b=8$. Find its mean.

### Multiple Choice

20. Sampling without replacement from a finite population most directly suggests:
A) Poisson  B) hypergeometric  C) exponential  D) uniform.

21. A fixed-interval event count most directly suggests:
A) Poisson  B) Weibull  C) triangular  D) geometric time.

22. Trial number of the first success most directly suggests:
A) uniform  B) geometric  C) normal  D) Weibull.

23. Trial number of the fifth success most directly suggests:
A) negative binomial  B) Poisson  C) exponential  D) triangular.

24. The variance of a uniform distribution on $[a,b]$ is:
A) $(b-a)^2/12$  
B) $(a+b)/2$  
C) $\beta^2$  
D) $\lambda$.

25. Under the Handbook exponential parameterization, the mean is:
A) $1/\beta$  B) $\beta$  C) $\beta^2$  D) $\alpha\beta$.

26. A Weibull model with $\alpha=1$ reduces to:
A) uniform  B) exponential  C) geometric  D) normal.

27. A triangular model requires:
A) $m<a$  
B) $m>b$  
C) $a\le m\le b$  
D) $a=b$ always.

---

## Answer Key with Explanations

### Conceptual

1. Hypergeometric sampling is from a finite population **without replacement**,
   so trial probabilities change. Binomial trials use constant $p$ and the
   standard independent-trial model. (§38.2)

2. It is the expected count over the defined exposure. (§38.3)

3. That equality is a defining property of the basic Poisson model:
   $\mu=\sigma^2=\lambda$. (§38.3)

4. The trial number on which the **first** success occurs. (§38.4)

5. The trial number on which the **$r$th** success occurs. (§38.4)

6. Uniform density is constant across the bounded interval. Triangular density
   rises toward or falls from a specified mode. (§38.5)

7.

   $$
   \boxed{\mu=\beta}.
   $$

   (§38.6)

8. Conditional on having already survived for time $s$, the additional
   exponential waiting-time distribution is the same as from a fresh start.
   (§38.6)

9. It changes the shape and lifetime/hazard behavior. $\alpha=1$ gives the
   exponential special case. (§38.7)

10. Different formulas represent different data-generation assumptions. A
    physically invalid assumption cannot be repaired by correct arithmetic.
    (§38.1)

### Calculation

11.

    $$
    \mu
    =
    \frac{nr}{N}
    =
    \frac{(5)(6)}{30}
    =
    \boxed1.
    $$

12.

    $$
    \sigma^2
    =
    n
    \left(\frac rN\right)
    \left(1-\frac rN\right)
    \frac{N-n}{N-1}
    $$

    $$
    =
    5(0.2)(0.8)\frac{25}{29}
    $$

    $$
    \approx
    \boxed{0.6897}.
    $$

13.

    $$
    P(X=0)
    =
    e^{-4}
    \approx
    \boxed{0.01832}.
    $$

14.

    $$
    P(X\ge1)
    =
    1-e^{-4}
    $$

    $$
    \approx
    \boxed{0.98168}.
    $$

15.

    $$
    \mu
    =
    \frac1{0.25}
    =
    \boxed4.
    $$

    $$
    \sigma^2
    =
    \frac{1-0.25}{0.25^2}
    =
    \frac{0.75}{0.0625}
    =
    \boxed{12}.
    $$

16.

    $$
    \mu
    =
    \frac rp
    =
    \frac3{0.40}
    =
    \boxed{7.5}.
    $$

17.

    $$
    \mu
    =
    \frac{2+10}{2}
    =
    \boxed6.
    $$

    $$
    \sigma^2
    =
    \frac{(10-2)^2}{12}
    =
    \frac{64}{12}
    =
    \boxed{5.3333}.
    $$

18.

    $$
    P(X>300)
    =
    e^{-300/200}
    =
    e^{-1.5}
    $$

    $$
    \approx
    \boxed{0.2231}.
    $$

19.

    $$
    \mu
    =
    \frac{2+5+8}{3}
    =
    \boxed5.
    $$

### Multiple Choice

20. **B.** Finite sampling without replacement is hypergeometric. (§38.2)

21. **A.** A Poisson model is the standard count model in this list. (§38.3)

22. **B.** First-success trial count is geometric. (§38.4)

23. **A.** Trial count to the $r$th success is negative binomial. (§38.4)

24. **A.** Uniform variance is $(b-a)^2/12$. (§38.5)

25. **B.** In the Handbook scale form, exponential mean is $\beta$. (§38.6)

26. **B.** Weibull with $\alpha=1$ becomes exponential. (§38.7)

27. **C.** The mode must lie inside the bounded interval. (§38.5)

---

## Practice Problems

1. **Hypergeometric.** A shipment has 40 parts, 5 of which are defective. Six
   parts are sampled without replacement. Find the probability of exactly one
   defective.

2. **Hypergeometric mean/variance.** For Problem 1, find the mean and variance of
   the number of defectives in the sample.

3. **Poisson count.** Calls arrive according to a Poisson model with expected
   count $\lambda=3.2$ per interval. Find the probability of exactly two calls.

4. **Poisson complement.** Using Problem 3, find the probability of at least one
   call.

5. **Geometric.** Independent tests succeed with probability $p=0.15$.
   Find the probability the first success occurs on trial 5 and find the mean
   trial number.

6. **Negative binomial.** Independent trials succeed with $p=0.30$.
   Find the probability the fourth success occurs on trial 9.

7. **Uniform.** A quantity is uniformly distributed from 12 to 20.
   Find its mean, standard deviation, and $P(14\le X\le17)$.

8. **Triangular.** A triangular distribution has $a=2$, $m=4$, $b=10$.
   Find its mean and variance.

9. **Exponential.** A lifetime is exponential with mean 600 h.
   Find the probabilities of surviving beyond 900 h and failing by 900 h.

10. **Weibull.** A lifetime has Weibull parameters
    $\alpha=3$, $\beta=1200$ h.
    Find $P(X>1000)$ and state whether the model's failure tendency is increasing,
    constant, or decreasing with age according to the guide interpretation.

---

## Practice Problem Solutions

1. Here

   $$
   N=40,\qquad r=5,\qquad n=6,\qquad x=1.
   $$

   Therefore

   $$
   P(X=1)
   =
   \frac{
   \binom51\binom{35}{5}
   }{
   \binom{40}{6}
   }.
   $$

   Numerically,

   $$
   \boxed{
   P(X=1)\approx0.4208.
   }
   $$

2. Mean:

   $$
   \mu
   =
   \frac{nr}{N}
   =
   \frac{(6)(5)}{40}
   =
   \boxed{0.75}.
   $$

   Variance:

   $$
   \sigma^2
   =
   6
   \left(\frac5{40}\right)
   \left(\frac{35}{40}\right)
   \frac{40-6}{40-1}
   $$

   $$
   \approx
   \boxed{0.5721}.
   $$

3.

   $$
   P(X=2)
   =
   \frac{
   e^{-3.2}(3.2)^2
   }{2!}
   $$

   $$
   \approx
   \boxed{0.2087}.
   $$

4.

   $$
   P(X\ge1)
   =
   1-P(X=0)
   $$

   $$
   =
   1-e^{-3.2}
   $$

   $$
   \approx
   \boxed{0.9592}.
   $$

5.

   $$
   P(X=5)
   =
   (1-0.15)^4(0.15)
   $$

   $$
   =
   (0.85)^4(0.15)
   $$

   $$
   \approx
   \boxed{0.0783}.
   $$

   Mean:

   $$
   E[X]
   =
   \frac1{0.15}
   \approx
   \boxed{6.667}.
   $$

6. For the fourth success on trial 9:

   $$
   P(Y=9)
   =
   \binom83
   (0.30)^4
   (0.70)^5.
   $$

   Therefore

   $$
   \boxed{
   P(Y=9)\approx0.0763.
   }
   $$

7. Mean:

   $$
   \mu
   =
   \frac{12+20}{2}
   =
   \boxed{16}.
   $$

   Variance:

   $$
   \sigma^2
   =
   \frac{(20-12)^2}{12}
   =
   \frac{64}{12}
   =
   5.3333.
   $$

   Standard deviation:

   $$
   \sigma
   =
   \sqrt{5.3333}
   \approx
   \boxed{2.309}.
   $$

   Interval probability:

   $$
   P(14\le X\le17)
   =
   \frac{17-14}{20-12}
   =
   \boxed{0.375}.
   $$

8. Mean:

   $$
   \mu
   =
   \frac{2+4+10}{3}
   =
   \boxed{\frac{16}{3}\approx5.333}.
   $$

   Variance:

   $$
   \sigma^2
   =
   \frac{
   2^2+10^2+4^2
   -(2)(10)
   -(2)(4)
   -(10)(4)
   }{18}
   $$

   $$
   =
   \frac{4+100+16-20-8-40}{18}
   $$

   $$
   =
   \frac{52}{18}
   $$

   $$
   \boxed{\approx2.8889}.
   $$

9.

   $$
   P(X>900)
   =
   e^{-900/600}
   =
   e^{-1.5}
   $$

   $$
   \approx
   \boxed{0.2231}.
   $$

   Therefore

   $$
   P(X\le900)
   =
   1-0.2231
   =
   \boxed{0.7769}.
   $$

10.

    $$
    S(1000)
    =
    e^{-(1000/1200)^3}.
    $$

    Since

    $$
    \left(\frac{1000}{1200}\right)^3
    \approx
    0.57870,
    $$

    $$
    S(1000)
    =
    e^{-0.57870}
    \approx
    \boxed{0.5605}.
    $$

    Because

    $$
    \alpha=3>1,
    $$

    the guide interpretation is

    $$
    \boxed{\text{increasing failure tendency with age}.}
    $$

---

## Quick Reference

### Hypergeometric

$$
\boxed{
P(X=x)
=
\frac{
\binom rx
\binom{N-r}{n-x}
}{
\binom Nn
}
}
$$

$$
\boxed{
\mu=\frac{nr}{N}
}
$$

$$
\boxed{
\sigma^2
=
\frac{
nr(N-r)(N-n)
}{
N^2(N-1)
}
}
$$

### Poisson

$$
\boxed{
P(X=x)
=
\frac{e^{-\lambda}\lambda^x}{x!}
}
$$

$$
\boxed{
\mu=\lambda,
\qquad
\sigma^2=\lambda.
}
$$

### Geometric

$$
\boxed{
P(X=x)
=
p(1-p)^{x-1},
\quad
x=1,2,\ldots
}
$$

$$
\boxed{
\mu=\frac1p,
\qquad
\sigma^2=\frac{1-p}{p^2}.
}
$$

### Negative binomial

$$
\boxed{
P(Y=y)
=
\binom{y-1}{r-1}
p^r(1-p)^{y-r}
}
$$

$$
\boxed{
\mu=\frac rp,
\qquad
\sigma^2=\frac{r(1-p)}{p^2}.
}
$$

### Uniform

$$
\boxed{
f(x)=\frac1{b-a},
\qquad
a\le x\le b
}
$$

$$
\boxed{
\mu=\frac{a+b}{2},
\qquad
\sigma^2=\frac{(b-a)^2}{12}.
}
$$

### Triangular

$$
\boxed{
\mu=\frac{a+b+m}{3}
}
$$

$$
\boxed{
\sigma^2
=
\frac{
a^2+b^2+m^2-ab-am-bm
}{18}.
}
$$

### Exponential

$$
\boxed{
f(x)=\frac1\beta e^{-x/\beta},
\qquad x\ge0
}
$$

$$
\boxed{
\mu=\beta,
\qquad
\sigma^2=\beta^2
}
$$

$$
\boxed{
S(x)=e^{-x/\beta}.
}
$$

### Weibull

$$
\boxed{
f(x)
=
\frac{\alpha}{\beta}
\left(\frac{x}{\beta}\right)^{\alpha-1}
e^{-(x/\beta)^\alpha}
}
$$

$$
\boxed{
S(x)
=
e^{-(x/\beta)^\alpha}
}
$$

$$
\boxed{
\mu
=
\beta\Gamma\left(1+\frac1\alpha\right)
}
$$

$$
\boxed{
\sigma^2
=
\beta^2
\left[
\Gamma\left(1+\frac2\alpha\right)
-
\Gamma^2\left(1+\frac1\alpha\right)
\right].
}
$$

### Selection cues

without replacement → hypergeometric  
count over exposure → Poisson  
first success trial → geometric  
$r$th success trial → negative binomial  
bounded equally likely → uniform  
bounded with most likely value → triangular  
constant-hazard waiting time → exponential  
flexible lifetime model → Weibull.

---

## What's Next

The probability models in this chapter describe how random variation behaves.

The next question is whether a real production process is behaving **consistently
over time** or whether something has changed.

**Chapter 01-39 — Statistical Process Control and Control Charts** will develop:

- common-cause versus special-cause variation,
- subgroup averages and ranges,
- $\bar X$ and $R$ charts,
- $\bar X$ and $S$ charts,
- center lines and three-sigma control limits,
- Handbook constants such as $A_2$, $D_3$, $D_4$, $A_3$, $B_3$, and $B_4$,
- the Handbook's tests for out-of-control behavior,
- and the difference between statistical control and engineering specification compliance.

The FE Reference Handbook provides these control-chart equations and constants on
printed pp. 83–84.

Carry one distinction forward:

> A probability distribution describes random variation. A control chart asks
> whether the process generating that variation has remained stable.

— Your Mentor
