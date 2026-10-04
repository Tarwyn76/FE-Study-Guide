---
chapter: "01-41"
title: "Acceptance Sampling and Operating Characteristic Curves"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-041-01, MATH-1D-041-02, MATH-1D-041-03, MATH-1D-041-04, MATH-1D-041-05, MATH-1D-041-06, MATH-1D-041-07]
routes: [industrial-systems, mechanical, chemical, civil, electrical-computer, environmental, other-disciplines]
status: drafted
---

# Chapter 01-41: Acceptance Sampling and Operating Characteristic Curves

> *"A sample can support a lot-disposition decision. It cannot turn incomplete
> information into certainty."*

---

## Before You Start

**Prerequisites:** [01-28 Probability Fundamentals](01-28-Probability-Fundamentals.md) ·
[01-29 Random Variables and Probability Distributions](01-29-Random-Variables-and-Probability-Distributions.md) ·
[01-38 Common Engineering Probability Distributions](01-38-Common-Engineering-Probability-Distributions.md) ·
[01-39 Statistical Process Control and Control Charts](01-39-Statistical-Process-Control-and-Control-Charts.md) ·
[01-40 Process Capability and Specification Performance](01-40-Process-Capability-and-Specification-Performance.md)

**Skip if:** You can interpret a single-sampling plan $(n,c)$; calculate lot
acceptance probability with the binomial model; calculate exact finite-lot
acceptance probability with the hypergeometric model; construct and interpret an
operating characteristic curve; explain producer's and consumer's risk; use
acceptable and rejectable quality points; explain how sample size and acceptance
number alter a plan; distinguish single sampling from double sampling
conceptually; and explain why acceptance sampling is not a replacement for
statistical process control.

**Time:** About 100–120 min reading and worked examples · 40–50 min review
questions · 65–80 min practice problems.

**Working convention:** In this chapter, a sampled unit is classified as
**conforming** or **nonconforming**. Let

$$
X=\text{number of nonconforming units found in the sample}.
$$

For a single-sampling attributes plan

$$
(n,c),
$$

accept the lot when

$$
\boxed{X\le c}
$$

and reject it when

$$
\boxed{X>c}.
$$

The acceptance number $c$ is a decision-rule parameter. It is not the expected
number of nonconforming units.

---

## On the Board Today

A submitted lot may contain thousands of units.

Inspecting every unit may be:

- expensive,
- slow,
- destructive,
- unnecessary,
- or operationally impractical.

Acceptance sampling uses a sample to decide whether the submitted lot should be
accepted or rejected under a stated sampling rule.

The rule does not tell you with certainty whether every unit in the lot is good.

It tells you the probability with which a lot of a given quality would be
accepted by the plan.

That distinction leads directly to the **operating characteristic curve**.

For a single-sampling plan,

$$
(n,c),
$$

the plan asks:

1. inspect $n$ sampled units,
2. count the number of nonconforming units $X$,
3. accept if $X\le c$,
4. reject if $X>c$.

If the model is binomial with nonconforming probability $p$,

$$
\boxed{
P_a(p)
=
P(X\le c)
=
\sum_{x=0}^{c}
\binom nx
p^x(1-p)^{n-x}.
}
$$

The function

$$
P_a(p)
$$

is the foundation of the OC curve.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **41.1** Define lot acceptance sampling and a single-sampling attributes plan
* **41.2** Interpret sample size $n$ and acceptance number $c$
* **41.3** Compute binomial lot-acceptance probability
* **41.4** Compute exact finite-lot acceptance probability with the hypergeometric distribution
* **41.5** Construct and interpret an operating characteristic curve
* **41.6** Define producer's risk and consumer's risk at stated quality levels
* **41.7** Distinguish acceptable quality and rejectable quality design points
* **41.8** Explain how $n$ and $c$ change sampling-plan behavior
* **41.9** Recognize when a binomial approximation is inappropriate for a finite lot
* **41.10** Explain the logic of double sampling without inventing unsupported Handbook formulas
* **41.11** Distinguish lot-disposition sampling from process control and process capability
* **41.12** State the limitations of acceptance sampling and avoid treating sample acceptance as proof that every unit conforms

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $N$ | lot size | finite-lot model |
| $D$ | number of nonconforming units in lot | finite-lot model |
| $p$ | fraction/probability nonconforming | binomial model |
| $n$ | sample size | units inspected |
| $c$ | acceptance number | accept if $X\le c$ |
| $X$ | number nonconforming in sample | discrete random variable |
| $P_a$ | probability of accepting the lot | function of lot quality and plan |
| AQL | acceptable quality level | guide-developed quality-engineering design point |
| RQL | rejectable quality level | guide-developed quality-engineering design point |
| $\alpha$ | producer's risk | probability of rejection at the stated AQL |
| $\beta$ | consumer's risk | probability of acceptance at the stated RQL |
| OC curve | operating characteristic curve | plots $P_a$ versus lot quality |

**Source-boundary note.** The supplied FE Handbook explicitly lists
**sampling plans** and **OC curves** in the Industrial and Systems FE
specification. The supplied Handbook does **not** contain a standalone
acceptance-sampling formula section that was located during this review. The
probability calculations in this chapter are therefore direct applications of
the Handbook's binomial and hypergeometric distributions. AQL, RQL,
producer's risk, consumer's risk, and double-sampling terminology are
guide-developed quality-engineering context rather than quoted Handbook
definitions.

---

## 41.1 Single-Sampling Plans — The Decision Rule

A **single-sampling attributes plan** is written

$$
\boxed{(n,c)}.
$$

The two parameters have different jobs.

### Sample size $n$

The sample size controls how much information is collected from the lot.

### Acceptance number $c$

The acceptance number controls how many nonconforming units may be observed while
still accepting the lot.

Decision rule:

$$
\boxed{
X\le c
\Rightarrow
\text{accept lot}
}
$$

$$
\boxed{
X>c
\Rightarrow
\text{reject lot}.
}
$$

### Worked Example 1 — Apply the Plan Before Calculating Probabilities

A lot is evaluated using

$$
(n,c)=(25,1).
$$

If the sample contains

$$
X=1
$$

nonconforming unit,

$$
1\le1,
$$

so

$$
\boxed{\text{accept the lot}.}
$$

If the sample contains

$$
X=2,
$$

then

$$
2>1,
$$

so

$$
\boxed{\text{reject the lot}.}
$$

No probability calculation is needed once the actual sample count is known.

![FIG-01-41-001: Single-sampling attributes-plan flow diagram. A submitted lot feeds a random sample of n units. Units are classified conforming/nonconforming, count X is formed, then a decision diamond compares X with acceptance number c. X≤c leads to Accept Lot; X>c leads to Reject Lot. A warning states that acceptance is a lot-disposition decision, not proof that every unit conforms.](../figures/FIG-01-41-001-single-sampling-plan.png)

### Sampling error is unavoidable

Two lots with the same true quality can produce different sample counts.

A relatively good lot can be rejected.

A relatively poor lot can be accepted.

Those possibilities are not calculation mistakes.

They are consequences of making a lot-level decision from a sample.

---

## 41.2 Binomial Acceptance Probability

When sampled classifications can reasonably be modeled as independent Bernoulli
trials with constant nonconforming probability

$$
p,
$$

the Handbook binomial distribution applies:

$$
P(X=x)
=
\binom nx
p^x(1-p)^{n-x}.
$$

A lot is accepted when

$$
X\le c.
$$

Therefore

$$
\boxed{
P_a(p)
=
\sum_{x=0}^{c}
\binom nx
p^x(1-p)^{n-x}.
}
$$

This is not a new probability distribution.

It is the binomial cumulative probability of the **acceptance event**.

### Worked Example 2 — Acceptance Probability for a Good Lot

Use

$$
(n,c)=(20,1)
$$

and suppose the modeled nonconforming fraction is

$$
p=0.02.
$$

The lot is accepted if

$$
X=0
$$

or

$$
X=1.
$$

Therefore

$$
P_a
=
P(X=0)+P(X=1).
$$

Compute:

$$
P_a
=
(0.98)^{20}
+
\binom{20}{1}(0.02)(0.98)^{19}.
$$

Thus

$$
\boxed{
P_a(0.02)
\approx
0.9401.
}
$$

Under this model, a lot at 2% nonconforming would be accepted about 94.0% of the
time by this plan.

### Worked Example 3 — Same Plan, Poorer Lot

Keep

$$
(n,c)=(20,1)
$$

but change lot quality to

$$
p=0.10.
$$

Then

$$
P_a(0.10)
=
(0.90)^{20}
+
20(0.10)(0.90)^{19}.
$$

Therefore

$$
\boxed{
P_a(0.10)
\approx
0.3917.
}
$$

The plan accepts a 10% nonconforming lot about 39.2% of the time under the
binomial model.

That may or may not be an acceptable protection level.

The OC curve makes that tradeoff visible.

![FIG-01-41-002: Binomial acceptance-probability diagram for plan (n,c). A binomial bar chart for X=0,1,... shades bars 0 through c as the acceptance region and bars above c as rejection. A formula box shows Pa(p)=sum from x=0 to c of C(n,x)p^x(1-p)^(n-x).](../figures/FIG-01-41-002-binomial-acceptance-probability.png)

### Special case — zero acceptance number

If

$$
c=0,
$$

the lot is accepted only when the sample contains no nonconforming units.

Then

$$
\boxed{
P_a(p)
=
(1-p)^n.
}
$$

This shortcut is useful, but a zero-acceptance plan is not automatically
appropriate for every quality problem.

---

## 41.3 Finite Lots — Exact Hypergeometric Acceptance Probability

The binomial model assumes a constant nonconforming probability from draw to
draw.

Sampling without replacement from a finite lot changes the composition of the
remaining lot.

If the lot contains exactly

$$
D
$$

nonconforming units among

$$
N
$$

total units, the Handbook hypergeometric model gives

$$
P(X=x)
=
\frac{
\binom Dx
\binom{N-D}{n-x}
}{
\binom Nn
}.
$$

Therefore the exact finite-lot acceptance probability is

$$
\boxed{
P_a(D)
=
\sum_{x=0}^{c}
\frac{
\binom Dx
\binom{N-D}{n-x}
}{
\binom Nn
},
}
$$

with impossible terms omitted.

### Worked Example 4 — Exact Finite-Lot Acceptance

A lot has

$$
N=100
$$

units, of which exactly

$$
D=5
$$

are nonconforming.

A sample of

$$
n=10
$$

is drawn without replacement and the lot is accepted if

$$
c=1.
$$

Then

$$
P_a
=
P(X=0)+P(X=1).
$$

So

$$
P_a
=
\frac{
\binom50\binom{95}{10}
}{
\binom{100}{10}
}
+
\frac{
\binom51\binom{95}{9}
}{
\binom{100}{10}
}.
$$

Numerically,

$$
\boxed{
P_a
\approx
0.9231.
}
$$

### Binomial approximation comparison

The lot fraction nonconforming is

$$
p
=
\frac5{100}
=
0.05.
$$

If we approximate with a binomial model,

$$
P_a
\approx
(0.95)^{10}
+
10(0.05)(0.95)^9
$$

$$
\approx
0.9139.
$$

Exact hypergeometric:

$$
0.9231.
$$

Binomial approximation:

$$
0.9139.
$$

The difference is modest here, but not zero.

As the sampling fraction

$$
\frac nN
$$

becomes larger, the without-replacement structure becomes more important.

![FIG-01-41-003: Finite-lot sampling comparison. Left panel shows a finite lot with N units and D nonconforming, sampled without replacement, feeding the hypergeometric acceptance sum. Right panel shows a large-lot/independent approximation using p=D/N and the binomial acceptance sum. A callout emphasizes checking n/N before assuming constant p.](../figures/FIG-01-41-003-hypergeometric-versus-binomial.png)

### Do not mix the two models halfway through

If the problem gives exact

$$
N
$$

and

$$
D
$$

and sampling is without replacement, the hypergeometric model is exact.

If the problem gives a defect probability

$$
p
$$

with independent-trial assumptions, use the binomial model.

Choose the probability model first.

---

## 41.4 Operating Characteristic Curves

An **operating characteristic curve** plots

$$
\boxed{
P_a(p)
}
$$

against the incoming lot nonconforming fraction

$$
p.
$$

For a fixed plan

$$
(n,c),
$$

the OC curve answers:

> If the true incoming quality were $p$, how often would this sampling plan
> accept the lot?

### Worked Example 5 — Build OC-Curve Points

For the plan

$$
(n,c)=(20,1),
$$

selected binomial acceptance probabilities are:

| Fraction nonconforming $p$ | $P_a(p)$ |
|---:|---:|
| 0.01 | 0.9831 |
| 0.02 | 0.9401 |
| 0.05 | 0.7358 |
| 0.10 | 0.3917 |
| 0.15 | 0.1756 |

The curve decreases as lot quality worsens.

At

$$
p=0,
$$

the sample contains no nonconforming units, so

$$
P_a(0)=1.
$$

As

$$
p
$$

approaches 1, acceptance probability approaches 0 for ordinary plans with

$$
c<n.
$$

![FIG-01-41-004: Operating characteristic curve for a representative single-sampling plan. Horizontal axis is fraction nonconforming p from 0 to higher values; vertical axis is probability of acceptance Pa from 0 to 1. The curve descends from near 1 toward 0. Marked points show good-quality lots accepted often and poor-quality lots accepted less often.](../figures/FIG-01-41-004-operating-characteristic-curve.png)

### The OC curve describes the plan, not one observed lot

After one sample is observed, the actual disposition is simply accept or reject.

The OC curve describes the **repeated-use behavior** of the sampling rule over
lots of different underlying quality levels.

That is why an OC curve is a plan-design and plan-evaluation tool.

---

## 41.5 Producer's Risk, Consumer's Risk, AQL, and RQL

The FE specification names sampling plans and OC curves, but the supplied
Handbook section does not provide standalone definitions of the following
quality-engineering terms.

They are developed here because they give engineering meaning to the OC curve.

### Acceptable quality level — AQL

The **AQL** is a stated relatively good quality level used as a design point for
the sampling plan.

A good lot can still be rejected by chance.

The probability of that rejection is the **producer's risk**:

$$
\boxed{
\alpha
=
1-P_a(\text{AQL}).
}
$$

### Rejectable quality level — RQL

The **RQL** is a stated poor quality level that the plan should have a low
probability of accepting.

The probability of accepting such a lot is the **consumer's risk**:

$$
\boxed{
\beta
=
P_a(\text{RQL}).
}
$$

These are conditional plan risks at specified quality points.

They are not universal properties of all lots.

![FIG-01-41-005: OC curve annotated with AQL and RQL. At AQL, the vertical acceptance probability is high; the small rejection portion 1-Pa is labeled producer's risk alpha. At RQL, the acceptance probability is low and labeled consumer's risk beta. Arrows emphasize that both risks belong to the same sampling plan at different quality points.](../figures/FIG-01-41-005-producer-consumer-risk.png)

### Worked Example 6 — Compute Both Risks

Consider

$$
(n,c)=(50,2).
$$

Let the design points be

$$
\text{AQL}=0.02
$$

and

$$
\text{RQL}=0.10.
$$

At

$$
p=0.02,
$$

the binomial acceptance probability is

$$
P_a(0.02)
=
\sum_{x=0}^{2}
\binom{50}{x}
(0.02)^x
(0.98)^{50-x}
$$

$$
\approx
0.9216.
$$

Therefore

$$
\boxed{
\alpha
=
1-0.9216
=
0.0784.
}
$$

Producer's risk is about 7.84%.

At

$$
p=0.10,
$$

$$
P_a(0.10)
=
\sum_{x=0}^{2}
\binom{50}{x}
(0.10)^x
(0.90)^{50-x}
$$

$$
\approx
0.1117.
$$

Therefore

$$
\boxed{
\beta
\approx
0.1117.
}
$$

Consumer's risk is about 11.17%.

### No sampling plan makes both risks zero with finite inspection

A finite sample cannot perfectly separate all good lots from all poor lots.

Sampling-plan design is therefore a tradeoff among:

- sample size,
- producer protection,
- consumer protection,
- inspection cost,
- inspection destructiveness,
- operational delay.

---

## 41.6 How Sample Size and Acceptance Number Change the Plan

The plan parameters

$$
n
$$

and

$$
c
$$

shape the OC curve.

### Increasing $c$ with fixed $n$

A larger acceptance number allows more nonconforming units in the sample before
rejection.

Therefore the plan becomes more permissive:

$$
\boxed{
P_a(p)\text{ increases for fixed }n,p.
}
$$

### Worked Example 7 — Effect of Acceptance Number

Let

$$
n=30
$$

and

$$
p=0.05.
$$

For

$$
c=0,
$$

$$
P_a
=
(0.95)^{30}
\approx
\boxed{0.2146}.
$$

For

$$
c=1,
$$

$$
P_a
\approx
\boxed{0.5535}.
$$

For

$$
c=2,
$$

$$
P_a
\approx
\boxed{0.8122}.
$$

Same sample size.

Same incoming quality.

Larger

$$
c
$$

means a more permissive lot-disposition rule.

### Increasing $n$ with fixed $c$

For

$$
p>0,
$$

increasing sample size while holding the same acceptance number generally makes
the plan more stringent because there are more opportunities to observe
nonconforming units.

Example with

$$
c=1,
\qquad
p=0.10:
$$

$$
P_a(20,1)
\approx
0.3917,
$$

while

$$
P_a(50,1)
\approx
0.0338.
$$

In actual plan design, $n$ and $c$ are usually chosen together to shape the OC
curve and meet stated risk objectives.

![FIG-01-41-006: Family of OC curves showing plan sensitivity. One comparison holds n fixed and increases c, shifting acceptance probabilities upward. A second comparison illustrates a larger n with fixed c producing a more stringent curve. A note states that real plan design selects n and c together to meet risk targets.](../figures/FIG-01-41-006-plan-parameter-effects.png)

### Double sampling — conceptual logic

A **double-sampling plan** uses the first sample to make one of three decisions:

- accept immediately,
- reject immediately,
- or take a second sample because the first result is inconclusive.

The second-stage decision then uses the specified plan rules.

This can reduce average inspection when lot quality is clearly good or clearly
poor.

However, the supplied Handbook material reviewed for this chapter does not give
a standalone double-sampling formula set.

Therefore this guide does not invent one.

The exam-relevant foundation developed here is:

- count nonconforming units,
- apply the stated decision thresholds,
- use binomial or hypergeometric probability according to the sampling model,
- and evaluate acceptance probability from the actual rules given.

---

## 41.7 Acceptance Sampling Is Not Process Control

Acceptance sampling, SPC, and process capability answer different questions.

### Acceptance sampling

> Should this submitted lot be accepted under the sampling rule?

### Statistical process control

> Is the process statistically stable over time?

### Process capability

> Can the stable process fit within the engineering specification limits?

A lot can pass acceptance sampling even when it came from an unstable process.

A lot can fail acceptance sampling even when the long-run process is normally
quite good.

Sampling variation allows both outcomes.

![FIG-01-41-007: Three-tool quality map. SPC monitors the process over time and asks "stable?". Process capability compares stable process spread and centering with LSL/USL and asks "capable?". Acceptance sampling takes a submitted lot, samples n units, and asks "accept this lot?". Arrows show related information flow but warn that none of the three tools substitutes for the others.](../figures/FIG-01-41-007-quality-tool-comparison.png)

### Worked Example 8 — Accepted Lot Does Not Prove Zero Nonconforming Units

A lot with true modeled quality

$$
p=0.05
$$

is evaluated using

$$
(n,c)=(20,1).
$$

From the OC calculation,

$$
P_a(0.05)
\approx
0.7358.
$$

So such lots are accepted about 73.6% of the time under the model.

Acceptance does **not** imply

$$
p=0.
$$

It means only that the observed sample count met the plan's acceptance rule.

### Worked Example 9 — Finite Lot versus Process Probability

Suppose a finite lot contains exactly

$$
D=5
$$

nonconforming units among

$$
N=50.
$$

A sample of

$$
n=10
$$

is drawn without replacement and the plan accepts if

$$
c=1.
$$

Exact hypergeometric acceptance probability:

$$
P_a
\approx
\boxed{0.7419}.
$$

A binomial approximation using

$$
p=0.10
$$

gives

$$
P_a
\approx
\boxed{0.7361}.
$$

The results are close here, but the models are not identical.

The exact model uses known finite-lot composition.

The binomial model treats each sampled classification as if it had constant
probability

$$
p.
$$

### Worked Example 10 — What a Rejection Means

A lot is rejected because a sample of 30 units contains 3 nonconforming units
under a plan

$$
(30,2).
$$

Correct conclusion:

> The lot fails the stated sampling-plan acceptance rule.

Incorrect conclusions include:

- every unit in the lot is nonconforming,
- the process that made the lot is proven unstable,
- the process capability index is below 1,
- the exact lot fraction nonconforming is $3/30$.

The sample fraction

$$
3/30
$$

is an observation from the sample, not proof of the exact lot composition or
the long-run process state.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. The Industrial and Systems FE exam
> specification on printed p. 493 explicitly includes **sampling plans** and
> **OC curves** under Quality Control. The Engineering Probability and
> Statistics section on printed pp. 67–68 gives the binomial probability
> function, and printed p. 85 lists the hypergeometric distribution. No
> standalone acceptance-sampling/OC-curve equation section was located in the
> supplied Handbook.

| Source material | Printed page | Use in this chapter |
|---|---:|---|
| Binomial distribution | 67–68 | acceptance probability for independent/constant-$p$ sample model |
| Hypergeometric distribution | 85 | exact acceptance probability for finite lots sampled without replacement |
| Industrial & Systems FE specification — Quality Control | 493 | explicitly names sampling plans and OC curves |

### What is source-derived

The following are directly grounded in the supplied Handbook:

- the binomial probability form,
- the hypergeometric probability form,
- the Industrial and Systems specification's inclusion of sampling plans,
- the Industrial and Systems specification's inclusion of OC curves.

### What is guide-developed

The following are standard quality-engineering interpretations developed in this
guide because the supplied Handbook does not provide a standalone acceptance
sampling section:

- single-sampling notation $(n,c)$,
- acceptance event $X\le c$,
- $P_a(p)$ as the cumulative probability of the acceptance event,
- operating characteristic curve interpretation,
- AQL and RQL design points,
- producer's risk $\alpha$,
- consumer's risk $\beta$,
- double-sampling logic,
- the comparison among acceptance sampling, SPC, and capability.

Those additions are not presented as quotations or hidden Handbook formulas.

**Know without a lookup:**

- $(n,c)$ means sample size and acceptance number,
- accept when $X\le c$,
- binomial for independent constant-$p$ sampling,
- hypergeometric for exact finite sampling without replacement,
- OC curve plots $P_a$ against lot quality,
- producer's risk is rejection of a relatively good lot at the stated design point,
- consumer's risk is acceptance of a relatively poor lot at the stated design point,
- and lot acceptance is not process control.

---

## Where This Goes Wrong

**Treating the acceptance number $c$ as an expected count.**

**Rejecting when $X=c$.** For the convention used here, accept when

$$
X\le c.
$$

**Using $P(X=c)$ instead of $P(X\le c)$ for the acceptance probability.**

**Forgetting the $x=0$ term in the acceptance sum.**

**Using a binomial model for a small finite lot sampled without replacement
without checking the approximation.**

**Using hypergeometric probability when the problem supplies independent trials
with constant $p$.**

**Plotting fraction conforming on the OC horizontal axis while interpreting it as
fraction nonconforming.**

**Interpreting a high acceptance probability as proof that a lot is good.**
$P_a$ is plan behavior at a specified quality level.

**Interpreting one accepted lot as proof of zero nonconforming units.**

**Interpreting one rejected lot as proof that the manufacturing process is
unstable.**

**Confusing producer's risk with consumer's risk.**

Producer's risk:

$$
\alpha
=
P(\text{reject}\mid\text{stated good-quality point}).
$$

Consumer's risk:

$$
\beta
=
P(\text{accept}\mid\text{stated poor-quality point}).
$$

**Assuming AQL means every lot at or better than AQL must be accepted.**

**Assuming RQL means every lot at or worse than RQL must be rejected.**

**Increasing $c$ and claiming the plan became stricter.** Larger $c$ with fixed
$n$ makes the plan more permissive.

**Increasing $n$ while holding $c$ fixed and ignoring the resulting change in
acceptance probability.**

**Using acceptance sampling as a substitute for process control.**

**Using sampling inspection to redefine the engineering specification.**

**Claiming a double-sampling formula is in the Handbook when no standalone
acceptance-sampling formula section was located.**

---

## Key Terms

| Term | Definition |
|---|---|
| acceptance sampling | use of a sample and stated decision rule to accept or reject a submitted lot |
| lot | defined collection of units submitted for disposition |
| conforming unit | unit satisfying the classification requirement |
| nonconforming unit | unit failing the classification requirement |
| attributes sampling | sampling in which units are classified into categories such as conforming/nonconforming |
| sampling plan | rule specifying sample size and disposition criteria |
| single-sampling plan | one sample followed by an accept/reject decision |
| sample size | number $n$ of units inspected |
| acceptance number | largest observed nonconforming count $c$ that still permits acceptance |
| probability of acceptance | $P_a$, probability the sampling rule accepts a lot at a specified quality level |
| operating characteristic curve | graph of acceptance probability versus incoming lot quality |
| acceptable quality level | stated relatively good quality design point for plan evaluation |
| rejectable quality level | stated poor quality design point for plan evaluation |
| producer's risk | probability of rejecting a lot at the stated acceptable-quality design point |
| consumer's risk | probability of accepting a lot at the stated rejectable-quality design point |
| double-sampling plan | plan allowing a second sample when the first sample is inconclusive |
| lot disposition | accept/reject action taken on a submitted lot |

---

## Review Questions

### Conceptual

1. What does a single-sampling plan $(n,c)$ specify?
2. Under the convention used here, when is a lot accepted?
3. Why can two lots with identical true quality receive different sampling decisions?
4. When is the binomial model appropriate for an acceptance-probability calculation?
5. When is the hypergeometric model exact?
6. What does an OC curve plot?
7. What is producer's risk?
8. What is consumer's risk?
9. How does increasing $c$ affect a plan when $n$ is fixed?
10. Why is acceptance sampling not a substitute for SPC?

### Calculation

11. For a plan $(20,1)$, is a lot accepted when $X=1$? What about $X=2$?
12. For $(n,c)=(10,0)$ and $p=0.03$, find $P_a$.
13. For $(n,c)=(5,1)$ and $p=0.10$, write the binomial acceptance-probability sum and evaluate it.
14. For $(n,c)=(20,1)$ and $p=0.05$, find $P_a$.
15. A finite lot has $N=20$, $D=4$, and a sample of $n=5$ is accepted if $c=1$. Write the exact hypergeometric expression for $P_a$.
16. Evaluate the hypergeometric probability in Question 15.
17. If a plan has $P_a(\text{AQL})=0.95$, find producer's risk.
18. If a plan has $P_a(\text{RQL})=0.08$, find consumer's risk.
19. For fixed $n=30$ and $p=0.05$, which is more permissive: $c=1$ or $c=2$?

### Multiple Choice

20. A lot is accepted under plan $(n,c)$ when:
A) $X<c$ only  
B) $X\le c$  
C) $X>c$  
D) $X=n$.

21. The OC curve vertical axis is:
A) sample size  
B) probability of acceptance  
C) specification width  
D) process mean.

22. Exact sampling without replacement from a finite lot most directly uses:
A) normal  
B) exponential  
C) hypergeometric  
D) geometric.

23. For independent classifications with constant nonconforming probability $p$,
the sample nonconforming count is modeled as:
A) binomial  
B) Weibull  
C) triangular  
D) uniform.

24. Producer's risk is associated with:
A) rejecting a stated relatively good lot  
B) accepting a stated poor lot  
C) process capability only  
D) control-chart UCL only.

25. Consumer's risk is associated with:
A) rejecting every lot  
B) accepting a stated poor lot  
C) increasing sample size only  
D) process centering.

26. Increasing $c$ with fixed $n$ generally makes a plan:
A) more permissive  
B) more stringent  
C) unchanged  
D) continuous.

27. Acceptance sampling primarily makes a decision about:
A) process stability  
B) submitted lot disposition  
C) regression slope  
D) process-control limits.

---

## Answer Key with Explanations

### Conceptual

1. It specifies sample size $n$ and acceptance number $c$. (§41.1)

2. Accept when

   $$
   \boxed{X\le c}.
   $$

   (§41.1)

3. Sampling counts are random. Different samples from lots of the same quality
   can contain different numbers of nonconforming units. (§41.1)

4. When sampled classifications can reasonably be modeled as independent trials
   with constant nonconforming probability $p$. (§41.2)

5. For a finite lot with known $N$ and $D$ when sampling is without replacement.
   (§41.3)

6. Probability of acceptance $P_a$ versus incoming lot quality, commonly
   fraction nonconforming $p$. (§41.4)

7. The probability of rejecting a lot at the stated acceptable-quality design
   point:

   $$
   \alpha=1-P_a(\text{AQL}).
   $$

   (§41.5)

8. The probability of accepting a lot at the stated rejectable-quality design
   point:

   $$
   \beta=P_a(\text{RQL}).
   $$

   (§41.5)

9. It permits more nonconforming sample units before rejection, so acceptance
   probability increases. (§41.6)

10. Acceptance sampling disposes of a lot. SPC evaluates time-ordered process
    stability. Those are different questions. (§41.7)

### Calculation

11. For

    $$
    c=1,
    $$

    $$
    X=1
    $$

    is accepted and

    $$
    X=2
    $$

    is rejected.

12. With zero acceptance number,

    $$
    P_a
    =
    (1-p)^n
    =
    (0.97)^{10}
    $$

    $$
    \approx
    \boxed{0.7374}.
    $$

13.

    $$
    P_a
    =
    P(X=0)+P(X=1)
    $$

    $$
    =
    (0.90)^5
    +
    \binom51(0.10)(0.90)^4.
    $$

    Therefore

    $$
    P_a
    =
    0.59049+0.32805
    =
    \boxed{0.91854}.
    $$

14.

    $$
    P_a
    =
    (0.95)^{20}
    +
    20(0.05)(0.95)^{19}
    $$

    $$
    \approx
    \boxed{0.7358}.
    $$

15.

    $$
    P_a
    =
    \frac{
    \binom40\binom{16}{5}
    }{
    \binom{20}{5}
    }
    +
    \frac{
    \binom41\binom{16}{4}
    }{
    \binom{20}{5}
    }.
    $$

16. Numerically,

    $$
    P_a
    =
    \boxed{0.7513\text{ approximately}}.
    $$

17.

    $$
    \alpha
    =
    1-0.95
    =
    \boxed{0.05}.
    $$

18.

    $$
    \beta
    =
    \boxed{0.08}.
    $$

19. The

    $$
    c=2
    $$

    plan is more permissive because it accepts all sample outcomes accepted by
    $c=1$ plus the additional case

    $$
    X=2.
    $$

### Multiple Choice

20. **B.** The stated convention accepts when $X\le c$. (§41.1)

21. **B.** The OC vertical axis is probability of acceptance. (§41.4)

22. **C.** Finite sampling without replacement uses the hypergeometric model.
    (§41.3)

23. **A.** The count is binomial under independent constant-$p$ assumptions.
    (§41.2)

24. **A.** Producer's risk is rejection at the stated good-quality design point.
    (§41.5)

25. **B.** Consumer's risk is acceptance at the stated poor-quality design
    point. (§41.5)

26. **A.** Larger $c$ with fixed $n$ is more permissive. (§41.6)

27. **B.** Acceptance sampling is a lot-disposition tool. (§41.7)

---

## Practice Problems

1. **Apply the decision rule.** A single-sampling plan is
   $$(n,c)=(40,2).$$
   State the decision for sample counts $X=0$, $X=2$, and $X=3$.

2. **Zero-acceptance plan.** For
   $$(n,c)=(15,0)$$
   and
   $$p=0.04,$$
   find the binomial probability of accepting the lot.

3. **Binomial acceptance.** For
   $$(n,c)=(10,1)$$
   and
   $$p=0.05,$$
   calculate $P_a$.

4. **Another OC point.** For the same plan in Problem 3, calculate $P_a$ at
   $$p=0.15.$$
   Compare the result with Problem 3.

5. **Finite-lot acceptance.** A lot contains
   $$N=30$$
   units with exactly
   $$D=3$$
   nonconforming. A sample of
   $$n=6$$
   is accepted if
   $$c=0.$$
   Find the exact hypergeometric acceptance probability.

6. **Finite-lot acceptance with $c=1$.** Use the same lot and sample as Problem
   5 but change the acceptance number to
   $$c=1.$$
   Find $P_a$.

7. **Producer and consumer risk.** A plan gives
   $$P_a(0.01)=0.97$$
   and
   $$P_a(0.08)=0.12.$$
   If 1% is designated AQL and 8% is designated RQL, find $\alpha$ and $\beta$.

8. **Acceptance-number effect.** For
   $$n=20,\quad p=0.10,$$
   calculate $P_a$ for
   $$c=0$$
   and
   $$c=1.$$
   State which plan is more permissive.

9. **Model selection.** Explain whether binomial or hypergeometric probability is
   the exact model for each:
   (a) 8 units sampled without replacement from a known lot of 40 containing 4
   nonconforming units;
   (b) 8 independently produced units, each with modeled nonconforming
   probability 0.10.

10. **Quality-tool distinction.** A submitted lot passes a sampling plan, but
    the production process that made it has an $\bar X$ chart point above UCL.
    Explain what can and cannot be concluded from the two facts.

---

## Practice Problem Solutions

1. The plan accepts when

   $$
   X\le2.
   $$

   Therefore:

   - $X=0$: accept,
   - $X=2$: accept,
   - $X=3$: reject.

2. For

   $$
   c=0,
   $$

   $$
   P_a
   =
   (1-0.04)^{15}
   =
   (0.96)^{15}
   $$

   $$
   \approx
   \boxed{0.5421}.
   $$

3.

   $$
   P_a
   =
   (0.95)^{10}
   +
   10(0.05)(0.95)^9.
   $$

   Therefore

   $$
   \boxed{
   P_a\approx0.9139.
   }
   $$

4.

   $$
   P_a
   =
   (0.85)^{10}
   +
   10(0.15)(0.85)^9
   $$

   $$
   \approx
   \boxed{0.5443}.
   $$

   The acceptance probability is lower than in Problem 3 because the modeled
   lot quality is poorer.

5. Acceptance requires zero nonconforming units:

   $$
   P_a
   =
   \frac{
   \binom30\binom{27}{6}
   }{
   \binom{30}{6}
   }.
   $$

   Therefore

   $$
   \boxed{
   P_a\approx0.4985.
   }
   $$

6.

   $$
   P_a
   =
   \frac{
   \binom30\binom{27}{6}
   +
   \binom31\binom{27}{5}
   }{
   \binom{30}{6}
   }.
   $$

   Therefore

   $$
   \boxed{
   P_a\approx0.9064.
   }
   $$

7. Producer's risk:

   $$
   \alpha
   =
   1-0.97
   =
   \boxed{0.03}.
   $$

   Consumer's risk:

   $$
   \beta
   =
   \boxed{0.12}.
   $$

8. For

   $$
   c=0,
   $$

   $$
   P_a
   =
   (0.90)^{20}
   \approx
   \boxed{0.1216}.
   $$

   For

   $$
   c=1,
   $$

   $$
   P_a
   =
   (0.90)^{20}
   +
   20(0.10)(0.90)^{19}
   $$

   $$
   \approx
   \boxed{0.3917}.
   $$

   Therefore

   $$
   \boxed{c=1}
   $$

   is more permissive.

9. **(a)** Hypergeometric is exact because a finite lot with known composition
   is sampled without replacement.

   **(b)** Binomial is the appropriate exact model under the stated independent
   constant-$p$ assumptions.

10. The accepted sample means the submitted lot met the sampling-plan decision
    rule.

    The control-chart signal means the process shows statistical evidence of a
    possible shift relative to its baseline.

    Neither result cancels the other.

    The lot disposition and the process-stability investigation are separate
    decisions.

---

## Quick Reference

**Single-sampling attributes plan**

$$
\boxed{(n,c)}
$$

accept when

$$
\boxed{X\le c}
$$

reject when

$$
\boxed{X>c}.
$$

**Binomial acceptance probability**

$$
\boxed{
P_a(p)
=
\sum_{x=0}^{c}
\binom nx
p^x(1-p)^{n-x}
}
$$

for independent constant-$p$ classifications.

**Zero-acceptance plan**

$$
\boxed{
P_a(p)
=
(1-p)^n
}
$$

when

$$
c=0.
$$

**Finite-lot hypergeometric acceptance**

$$
\boxed{
P_a(D)
=
\sum_{x=0}^{c}
\frac{
\binom Dx
\binom{N-D}{n-x}
}{
\binom Nn
}
}
$$

for sampling without replacement from a lot with known

$$
N,\ D.
$$

**Operating characteristic curve**

horizontal axis:

$$
p=\text{incoming fraction nonconforming}
$$

vertical axis:

$$
P_a=\text{probability of acceptance}.
$$

**Producer's risk**

$$
\boxed{
\alpha
=
1-P_a(\text{AQL})
}
$$

**Consumer's risk**

$$
\boxed{
\beta
=
P_a(\text{RQL})
}
$$

**Plan effects**

fixed $n$, larger $c$ → more permissive  
fixed $c$, larger $n$ → generally more stringent for $p>0$.

**Model choice**

finite known lot, without replacement → hypergeometric  
independent constant-$p$ classifications → binomial.

**Quality-tool distinction**

SPC → process stability  
capability → stable process versus specifications  
acceptance sampling → submitted lot disposition.

---

## What's Next

**Layer 1 is complete.**

The mathematical and statistical substrate now runs from basic arithmetic,
units, algebra, geometry, trigonometry, calculus, linear algebra, numerical
methods, algorithms, probability, inference, regression, uncertainty,
statistical quality control, capability, and acceptance sampling.

The guide now moves to **Layer 2 — Core Engineering Science**.

Layer 2 is organized into the established tiers:

- **2A — Professional**
- **2B — Physical Science & Safety**
- **2C — Mechanics**
- **2D — Thermal-Fluids**
- **2E — Electrical**
- **2F — Measurement & Control**

A specific Layer 2 chapter number is not named here because the next chapter
must come from the ledger/build order rather than being invented as a forward
reference.

Before moving into Layer 2, the Layer 1 control files should be synchronized:

- register Chapters 01-38 through 01-41 in the concept ledger,
- register `FIG-01-38-001` through `FIG-01-41-007` in the figure manifest,
- run the forward-reference linter,
- run coverage and prerequisite checks,
- and resolve any remaining Layer 1 validation findings.

Carry the Layer 1 rule forward:

> Use the mathematics as a tool, but keep asking what engineering question the
> calculation actually answers.

— Your Mentor
