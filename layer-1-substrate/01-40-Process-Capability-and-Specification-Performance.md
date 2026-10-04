---
chapter: "01-40"
title: "Process Capability and Specification Performance"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-040-01, MATH-1D-040-02, MATH-1D-040-03, MATH-1D-040-04, MATH-1D-040-05, MATH-1D-040-06, MATH-1D-040-07]
routes: [industrial-systems, mechanical, chemical, civil, electrical-computer, environmental, other-disciplines]
status: drafted
---

# Chapter 01-40: Process Capability and Specification Performance

> *"A stable process may still be too wide for the tolerance band. Capability
> compares what the process naturally does with what the specification allows."*

---

## Before You Start

**Prerequisites:** [01-30 The Normal Distribution and the Central Limit Theorem](01-30-The-Normal-Distribution-and-the-Central-Limit-Theorem.md) ·
[01-39 Statistical Process Control and Control Charts](01-39-Statistical-Process-Control-and-Control-Charts.md)

**Skip if:** You can distinguish specification limits from control limits;
compute potential capability $C_p$ and actual capability $C_{pk}$; explain why
$C_p$ measures spread while $C_{pk}$ also penalizes off-centering; show that
$C_{pk}\le C_p$; calculate upper- and lower-side capability; estimate process
standard deviation from a stable control-chart baseline; interpret capability
only after process stability has been established; and explain why a capability
index is not itself a defect probability or engineering acceptance criterion.

**Time:** About 90–110 min reading and worked examples · 35–45 min review
questions · 60–75 min practice problems.

**Working convention:** Capability calculations use the process mean $\mu$ and
process standard deviation $\sigma$, or defensible estimates of them from a
stable process. The formulas do not repair an unstable process. If the process
is shifting while the capability study is being performed, a single capability
number can be misleading.

---

## On the Board Today

Chapter 01-39 asked:

> Is the process statistically stable?

This chapter asks a different question:

> If the process is stable, does its natural variation fit inside the required
> specification band?

Let the engineering specification be

$$
LSL\le X\le USL.
$$

The total specification width is

$$
\boxed{
USL-LSL.
}
$$

A stable process with standard deviation

$$
\sigma
$$

has a natural six-sigma spread of

$$
\boxed{
6\sigma
}
$$

from approximately

$$
\mu-3\sigma
$$

to

$$
\mu+3\sigma.
$$

The FE Reference Handbook defines the **potential capability** of a centered
process as

$$
\boxed{
C_p
=
\frac{USL-LSL}{6\sigma}.
}
$$

It defines **actual capability** as

$$
\boxed{
C_{pk}
=
\min
\left[
\frac{\mu-LSL}{3\sigma},
\frac{USL-\mu}{3\sigma}
\right].
}
$$

These two numbers answer related but different questions.

$C_p$ asks whether the spread could fit.

$C_{pk}$ asks how well the current mean and spread actually fit.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **40.1** Distinguish statistical-control limits from engineering specification limits
* **40.2** Define specification width and natural process spread
* **40.3** Compute and interpret potential capability $C_p$
* **40.4** Compute upper- and lower-side capability
* **40.5** Compute and interpret actual capability $C_{pk}$
* **40.6** Explain why $C_{pk}\le C_p$
* **40.7** Quantify the effect of process off-centering
* **40.8** Estimate $\sigma$ from a stable $\bar X$-$R$ or $\bar X$-$S$ baseline
* **40.9** Compute capability using an estimated process standard deviation
* **40.10** Relate capability to normal-distribution nonconformance only when a normal model is justified
* **40.11** Handle one-sided specification problems
* **40.12** State the limitations of capability indices and avoid treating them as universal acceptance rules

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $LSL$ | lower specification limit | engineering/customer/design requirement |
| $USL$ | upper specification limit | engineering/customer/design requirement |
| $\mu$ | stable process mean | process center |
| $\sigma$ | stable process standard deviation | process spread |
| $C_p$ | potential capability | assumes centered process |
| $C_{pk}$ | actual capability | includes current centering |
| $C_{pu}$ | upper-side capability | distance from mean to USL in $3\sigma$ units |
| $C_{pl}$ | lower-side capability | distance from LSL to mean in $3\sigma$ units |
| $\hat\sigma$ | estimated process standard deviation | may come from $\bar R/d_2$ or $\bar S/c_4$ |
| $m$ | midpoint of specification band | $(USL+LSL)/2$ |
| CL, UCL, LCL | control-chart center and limits | process-monitoring quantities, not specifications |

---

## 40.1 Specification Limits and Natural Process Spread

A specification limit is imposed by what the product or process must satisfy.

A control limit is estimated from how the process behaves.

They must not be substituted for one another.

### Specification width

For a two-sided specification,

$$
\boxed{
W_{\text{spec}}
=
USL-LSL.
}
$$

Specification midpoint:

$$
\boxed{
m
=
\frac{USL+LSL}{2}.
}
$$

### Natural process spread

Capability formulas use

$$
6\sigma
$$

as the process spread measure.

For a normal model, the interval

$$
\mu\pm3\sigma
$$

contains approximately 99.73% of the distribution.

But the capability formulas themselves are ratios of specification distances to
process spread. They do not by themselves prove the process is normal.

![FIG-01-40-001: Specification-band versus process-spread diagram. Horizontal axis shows LSL and USL as fixed external boundaries. A centered bell-shaped process distribution spans approximately mu ± 3 sigma. Brackets label specification width USL-LSL and natural process spread 6 sigma. A separate small panel contrasts control limits with specification limits and states that they answer different questions.](../figures/FIG-01-40-001-specification-versus-process-spread.png)

### Worked Example 1 — Compare Widths Before Computing an Index

A process has

$$
LSL=9.5\text{ mm},
\qquad
USL=10.5\text{ mm},
$$

and stable standard deviation

$$
\sigma=0.10\text{ mm}.
$$

Specification width:

$$
USL-LSL
=
10.5-9.5
=
\boxed{1.0\text{ mm}}.
$$

Natural process spread:

$$
6\sigma
=
6(0.10)
=
\boxed{0.60\text{ mm}}.
$$

The process spread is narrower than the specification band.

That suggests potential capability greater than 1, but centering still has to be
checked.

---

## 40.2 Potential Capability — $C_p$

The Handbook labels

$$
C_p
$$

as the potential capability for a centered process.

$$
\boxed{
C_p
=
\frac{USL-LSL}{6\sigma}.
}
$$

Interpret the ratio geometrically.

### If $C_p=1$

Then

$$
USL-LSL
=
6\sigma.
$$

A perfectly centered natural six-sigma process spread just matches the
specification width.

### If $C_p>1$

The specification band is wider than the natural six-sigma spread.

There is potential room for the process distribution to fit.

### If $C_p<1$

The natural six-sigma spread is wider than the specification band.

Even perfect centering cannot make the six-sigma spread fit.

![FIG-01-40-002: Three centered-process panels comparing Cp below 1, equal to 1, and above 1. Each panel has fixed LSL/USL lines and a centered process distribution. Cp<1 shows process spread wider than specs; Cp=1 just touches both specs at ±3 sigma; Cp>1 fits inside with margin.](../figures/FIG-01-40-002-cp-centered-capability.png)

### Worked Example 2 — Potential Capability

Continue Worked Example 1.

$$
C_p
=
\frac{10.5-9.5}{6(0.10)}
$$

$$
=
\frac{1.0}{0.60}
$$

$$
=
\boxed{1.667}.
$$

Interpretation:

> If the process is centered in the specification band, its six-sigma spread is
> substantially narrower than the specification width.

That is a statement about **potential** capability.

It does not yet say where the process mean is located.

---

## 40.3 Actual Capability — $C_{pk}$

The Handbook defines actual capability by comparing the process mean with both
specification limits.

Define the upper-side capability:

$$
\boxed{
C_{pu}
=
\frac{USL-\mu}{3\sigma}.
}
$$

Define the lower-side capability:

$$
\boxed{
C_{pl}
=
\frac{\mu-LSL}{3\sigma}.
}
$$

Then

$$
\boxed{
C_{pk}
=
\min(C_{pl},C_{pu}).
}
$$

The smaller side controls because that is the specification boundary the process
mean is closer to in standard-deviation units.

![FIG-01-40-003: Off-centered capability diagram. A process distribution is shifted toward USL. Arrows from mu to LSL and USL are labeled 3 sigma times Cpl and Cpu. The shorter upper-side distance determines Cpk=min(Cpl,Cpu). A centered comparison shows equal side indices.](../figures/FIG-01-40-003-cpk-off-centering.png)

### Worked Example 3 — Same Spread, Shifted Mean

Keep

$$
LSL=9.5,
\qquad
USL=10.5,
\qquad
\sigma=0.10,
$$

but let

$$
\mu=10.20.
$$

Potential capability remains

$$
C_p
=
\frac{1.0}{0.60}
=
1.667.
$$

Lower-side capability:

$$
C_{pl}
=
\frac{10.20-9.50}{3(0.10)}
=
\frac{0.70}{0.30}
=
\boxed{2.333}.
$$

Upper-side capability:

$$
C_{pu}
=
\frac{10.50-10.20}{0.30}
=
\boxed{1.000}.
$$

Therefore

$$
\boxed{
C_{pk}=1.000.
}
$$

The process still has the same spread.

The drop from

$$
C_p=1.667
$$

to

$$
C_{pk}=1.000
$$

comes entirely from off-centering.

---

## 40.4 Why $C_{pk}\le C_p$

The specification midpoint is

$$
m
=
\frac{USL+LSL}{2}.
$$

When

$$
\mu=m,
$$

the two side distances are equal:

$$
USL-\mu
=
\mu-LSL
=
\frac{USL-LSL}{2}.
$$

Then

$$
C_{pu}
=
C_{pl}
=
\frac{USL-LSL}{6\sigma}
=
C_p.
$$

Thus for a centered process,

$$
\boxed{
C_{pk}=C_p.
}
$$

If the mean shifts away from the midpoint, one side distance gets smaller.

Therefore

$$
\boxed{
C_{pk}<C_p
}
$$

for an off-centered two-sided process.

In general,

$$
\boxed{
C_{pk}\le C_p.
}
$$

### A useful centering form

For a two-sided specification, define the half-width

$$
h
=
\frac{USL-LSL}{2}.
$$

The distance from the mean to the nearest specification limit is

$$
h-|\mu-m|.
$$

Therefore

$$
\boxed{
C_{pk}
=
\frac{
h-|\mu-m|
}{
3\sigma
}.
}
$$

Since

$$
C_p
=
\frac{h}{3\sigma},
$$

the difference between potential and actual capability is directly tied to the
mean's distance from the specification midpoint.

This equivalent centering form is guide-derived from the Handbook equations.

![FIG-01-40-004: Centering-penalty diagram. A fixed specification band has midpoint m and half-width h. One centered distribution has mu=m and Cpk=Cp. A shifted distribution shows offset |mu-m| and nearest-spec distance h-|mu-m|, with an equation Cpk=[h-|mu-m|]/(3 sigma).](../figures/FIG-01-40-004-centering-penalty.png)

### Worked Example 4 — Quantify the Centering Penalty

Let

$$
LSL=90,
\qquad
USL=110,
\qquad
\sigma=2,
\qquad
\mu=104.
$$

Then

$$
m=100,
\qquad
h=10.
$$

Potential capability:

$$
C_p
=
\frac{20}{12}
=
\boxed{1.667}.
$$

Offset:

$$
|\mu-m|
=
|104-100|
=
4.
$$

Nearest-spec distance:

$$
h-|\mu-m|
=
10-4
=
6.
$$

Therefore

$$
C_{pk}
=
\frac6{3(2)}
=
\boxed{1.000}.
$$

Again, the spread is potentially capable, but the mean location consumes the
available margin.

---

## 40.5 Estimating $\sigma$ from a Stable Control-Chart Baseline

In practice, the true process standard deviation is rarely known.

Chapter 01-39 developed the Handbook approximations

$$
\boxed{
\hat\sigma
\approx
\frac{\bar R}{d_2}
}
$$

and

$$
\boxed{
\hat\sigma
\approx
\frac{\bar S}{c_4}.
}
$$

A capability study can use these estimates when the underlying control-chart
baseline is reasonably stable.

### Capability from a range-chart estimate

Substitute

$$
\hat\sigma
=
\frac{\bar R}{d_2}
$$

into

$$
C_p
=
\frac{USL-LSL}{6\hat\sigma}.
$$

Likewise,

$$
C_{pk}
=
\min
\left[
\frac{\bar{\bar X}-LSL}{3\hat\sigma},
\frac{USL-\bar{\bar X}}{3\hat\sigma}
\right].
$$

The use of

$$
\bar{\bar X}
$$

as the mean estimate and

$$
\bar R/d_2
$$

as the spread estimate connects control-chart analysis directly to capability
analysis.

![FIG-01-40-005: Control-to-capability workflow. Stable X-bar/R baseline supplies X-double-bar as mu-hat and R-bar/d2 as sigma-hat. These enter Cp and Cpk equations alongside LSL/USL. An unstable-chart branch stops before capability and says "investigate stability first."](../figures/FIG-01-40-005-control-chart-to-capability.png)

### Worked Example 5 — Capability from $\bar R$

A stable process has

$$
LSL=24.70\text{ mm},
\qquad
USL=25.30\text{ mm}.
$$

From an $\bar X$-$R$ baseline with subgroup size

$$
n=5,
$$

suppose

$$
\bar{\bar X}=25.02\text{ mm},
\qquad
\bar R=0.12\text{ mm}.
$$

For

$$
n=5,
$$

the Handbook gives

$$
d_2=2.326.
$$

Estimate process standard deviation:

$$
\hat\sigma
=
\frac{0.12}{2.326}
$$

$$
\approx
\boxed{0.05159\text{ mm}}.
$$

Potential capability:

$$
C_p
=
\frac{25.30-24.70}{6(0.05159)}
$$

$$
\approx
\boxed{1.938}.
$$

Lower-side capability:

$$
C_{pl}
=
\frac{25.02-24.70}{3(0.05159)}
$$

$$
\approx
2.067.
$$

Upper-side capability:

$$
C_{pu}
=
\frac{25.30-25.02}{3(0.05159)}
$$

$$
\approx
1.809.
$$

Therefore

$$
\boxed{
C_{pk}\approx1.809.
}
$$

The upper specification is the limiting side.

---

## 40.6 Capability and Expected Nonconformance

A capability index is not itself a defect probability.

To convert specification distances into expected nonconformance, you need a
probability model for individual output.

A common approximation is a stable normal process.

### Centered normal process with $C_p=1$

For a centered process,

$$
C_p=1
$$

means the specification limits are at

$$
\mu\pm3\sigma.
$$

Under a normal model,

$$
P(|Z|>3)
\approx
0.0027.
$$

So about

$$
0.27\%
$$

falls outside the two-sided limits.

That percentage comes from the normal distribution, not from the definition of
$C_p$ itself.

### Worked Example 6 — Capability and Normal Tail Area

Suppose a stable normal process has

$$
\mu=50.0,
\qquad
\sigma=0.50,
$$

with

$$
LSL=49.0,
\qquad
USL=51.0.
$$

Potential capability:

$$
C_p
=
\frac{2.0}{6(0.50)}
=
\boxed{0.667}.
$$

Because the process is centered,

$$
C_{pk}=0.667.
$$

Standardize the upper limit:

$$
z_U
=
\frac{51.0-50.0}{0.50}
=
2.0.
$$

Lower limit:

$$
z_L=-2.0.
$$

For a normal model,

$$
P(|Z|>2)
\approx
2(0.0228)
=
\boxed{0.0456}.
$$

So about 4.56% is expected outside the specification under the stated normal
model.

The capability index alone did not produce that percentage; the normal
distribution supplied the tail area.

### Non-normal caution

If the process distribution is strongly non-normal, the relationship between a
capability index and actual nonconformance can differ substantially from the
normal-model interpretation.

Do not attach a normal tail probability unless a normal model is justified.

---

## 40.7 One-Sided Specifications and Engineering Interpretation

Some requirements have only one meaningful limit.

Examples:

- contamination must be **below** a maximum,
- strength must be **above** a minimum,
- leakage must be **below** a maximum.

For an upper-only specification,

$$
\boxed{
C_{pu}
=
\frac{USL-\mu}{3\sigma}.
}
$$

For a lower-only specification,

$$
\boxed{
C_{pl}
=
\frac{\mu-LSL}{3\sigma}.
}
$$

Do not invent a second specification merely so that $C_p$ can be calculated.

### Worked Example 7 — Upper-Only Requirement

A stable process has

$$
\mu=2.4\text{ ppm},
\qquad
\sigma=0.30\text{ ppm},
$$

with only an upper specification:

$$
USL=4.0\text{ ppm}.
$$

Upper capability:

$$
C_{pu}
=
\frac{4.0-2.4}{3(0.30)}
$$

$$
=
\frac{1.6}{0.9}
$$

$$
=
\boxed{1.778}.
$$

There is no lower specification in the problem, so a two-sided $C_p$ is not
defined from the stated requirement.

### Capability is not the acceptance criterion

A specification may be tied to:

- safety,
- fit,
- performance,
- regulation,
- customer contract,
- reliability.

The capability index summarizes process position and spread relative to those
limits.

It does not replace the specification's engineering meaning.

![FIG-01-40-006: One-sided and two-sided capability comparison. Top: two-sided LSL/USL with Cp and Cpk. Lower left: upper-only specification with Cpu=(USL-mu)/(3 sigma). Lower right: lower-only specification with Cpl=(mu-LSL)/(3 sigma). Warning states not to invent a missing specification limit.](../figures/FIG-01-40-006-one-sided-capability.png)

### Worked Example 8 — Same $C_p$, Different $C_{pk}$

Two stable processes have the same specifications:

$$
LSL=0,
\qquad
USL=12,
$$

and the same standard deviation:

$$
\sigma=1.
$$

Therefore both have

$$
C_p
=
\frac{12}{6}
=
2.
$$

Process A has

$$
\mu=6.
$$

Then

$$
C_{pk,A}=2.
$$

Process B has

$$
\mu=9.
$$

Then

$$
C_{pl}
=
\frac9{3}
=
3,
$$

$$
C_{pu}
=
\frac{12-9}{3}
=
1.
$$

So

$$
\boxed{
C_{pk,B}=1.
}
$$

Same potential spread capability.

Very different actual centering.

### Worked Example 9 — Improve Spread or Improve Center?

Suppose

$$
LSL=95,
\qquad
USL=105,
$$

$$
\mu=103,
\qquad
\sigma=1.
$$

Then

$$
C_p
=
\frac{10}{6}
=
1.667,
$$

but

$$
C_{pk}
=
\min
\left(
\frac{8}{3},
\frac2{3}
\right)
=
\boxed{0.667}.
$$

The dominant problem is centering, not overall spread.

Reducing $\sigma$ helps both indices, but shifting the mean back toward the
specification midpoint addresses the immediate limiting side.

A capability calculation should therefore guide diagnosis, not merely generate
a score.

![FIG-01-40-007: Capability-diagnosis matrix. Four cells compare low/high Cp and Cpk. Low Cp indicates excessive spread; high Cp with low Cpk indicates off-centering; high Cp and Cpk indicates capable centered behavior; unstable process is shown outside the matrix with "capability interpretation deferred until stability established." A workflow points to reduce spread, recenter process, or both.](../figures/FIG-01-40-007-capability-diagnosis.png)

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. In the Industrial and Systems Engineering
> section, printed p. 423 contains *Process Capability*. It gives actual
> capability as the minimum of the lower- and upper-side three-sigma
> specification distances and potential capability for a centered process as
> specification width divided by $6\sigma$. It defines $\mu$ and $\sigma$ as the
> process mean and standard deviation and identifies LSL and USL as the lower and
> upper specification limits.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Process Capability | 423 | Defines actual and potential process capability |
| Actual Capability | 423 | $C_{pk}=\min[(\mu-LSL)/(3\sigma),(USL-\mu)/(3\sigma)]$ |
| Potential Capability | 423 | $C_p=(USL-LSL)/(6\sigma)$ for a centered process |
| Symbols | 423 | Defines $\mu$, $\sigma$, LSL, and USL |

### Connection to the general statistics section

Printed pp. 83–84 provide the control-chart and process-spread tools developed
in Chapter 01-39. Those tools can produce defensible estimates of process center
and spread once statistical stability has been established.

This chapter therefore combines two Handbook locations:

1. statistical-control tools from the general probability/statistics section,
2. capability formulas from the Industrial and Systems Engineering section.

### Guide-developed interpretation

The Handbook p. 423 entry is formula-focused. This chapter adds:

- geometric interpretation of $C_p$ and $C_{pk}$,
- the proof that $C_{pk}\le C_p$,
- explicit upper- and lower-side notation $C_{pu}$ and $C_{pl}$,
- the midpoint/centering form for $C_{pk}$,
- use of $\bar R/d_2$ and $\bar S/c_4$ estimates from the preceding chapter,
- one-sided specification interpretation,
- and the normal-tail example connecting capability to expected
  nonconformance.

The normal-tail calculation is a distribution-based consequence under an
explicit normal model; it is not part of the p. 423 capability definition.

**Know without a lookup:**

- stability before capability,
- $C_p$ measures potential spread fit,
- $C_{pk}$ includes centering,
- $C_{pk}\le C_p$,
- the smaller specification side controls $C_{pk}$,
- and specification limits are not control limits.

---

## Where This Goes Wrong

**Calculating capability before checking stability.**

**Using control limits as LSL and USL.**

**Using specification limits as UCL and LCL.**

**Forgetting the factor of 6 in $C_p$.**

**Forgetting the factor of 3 in each side of $C_{pk}$.**

**Taking the larger of $C_{pl}$ and $C_{pu}$.** Actual capability is controlled
by the smaller side.

**Assuming $C_p=C_{pk}$ for an off-centered process.**

**Interpreting high $C_p$ as proof of actual capability without checking the
mean.**

**Treating $C_{pk}$ as a percentage conforming.** It is a dimensionless distance
ratio.

**Converting $C_{pk}$ to defect probability without a distribution model.**

**Assuming a normal model solely because capability formulas contain
$\sigma$.**

**Using an unstable estimate of $\sigma$ in a capability calculation.**

**Inventing a lower specification for an upper-only requirement.**

**Inventing an upper specification for a lower-only requirement.**

**Treating a company capability target such as 1.33 as a universal law.**
Required capability thresholds come from the applicable engineering,
organizational, customer, or regulatory requirement.

**Believing process capability can replace product inspection or engineering
verification in every application.**

**Ignoring units when checking the inputs.** $C_p$ and $C_{pk}$ are
dimensionless, but $\mu$, $\sigma$, LSL, and USL must use consistent units.

---

## Key Terms

| Term | Definition |
|---|---|
| process capability | relationship between stable process behavior and specification requirements |
| specification limit | externally imposed engineering/customer/design boundary |
| specification width | $USL-LSL$ |
| natural process spread | six-standard-deviation spread $6\sigma$ used by capability formulas |
| potential capability | $C_p$, spread-based capability assuming centered process |
| actual capability | $C_{pk}$, capability including current mean location |
| upper capability | $C_{pu}=(USL-\mu)/(3\sigma)$ |
| lower capability | $C_{pl}=(\mu-LSL)/(3\sigma)$ |
| centered process | process whose mean lies at the specification midpoint |
| off-centered process | process whose mean does not lie at the specification midpoint |
| specification midpoint | $(USL+LSL)/2$ |
| limiting side | specification boundary producing the smaller side capability |
| stable process | process whose time-ordered behavior is statistically consistent with its baseline |
| nonconformance | output outside a stated specification requirement |
| capability study | assessment of stable process location and spread relative to specifications |
| one-sided specification | requirement having only an upper or only a lower limit |

---

## Review Questions

### Conceptual

1. What is the difference between statistical control and process capability?
2. What does $C_p$ measure?
3. What does $C_{pk}$ measure that $C_p$ does not?
4. Why is $C_{pk}$ the minimum of two side indices?
5. Under what condition does $C_{pk}=C_p$?
6. Why must $C_{pk}\le C_p$ for a two-sided specification?
7. Why should capability normally be evaluated after stability?
8. Why is a capability index not itself a defect probability?
9. How should a one-sided specification be handled?
10. Why is a required capability threshold not universal?

### Calculation

11. If $LSL=40$, $USL=52$, and $\sigma=1.5$, find $C_p$.
12. For Question 11, if $\mu=46$, find $C_{pl}$, $C_{pu}$, and $C_{pk}$.
13. For Question 11, if $\mu=49$, find $C_{pk}$.
14. A process has $C_p=1.50$ and is perfectly centered. What is $C_{pk}$?
15. A process has $LSL=95$, $USL=105$, $\mu=101$, and $\sigma=0.8$. Find $C_p$ and $C_{pk}$.
16. A stable $n=5$ range-chart baseline has $\bar R=0.20$ and $d_2=2.326$. Estimate $\sigma$.
17. Using Question 16, with $LSL=19.5$, $USL=20.5$, and $\mu=20.1$, find $C_p$ and $C_{pk}$.
18. An upper-only requirement has $USL=12$, $\mu=9$, and $\sigma=0.5$. Find $C_{pu}$.
19. A centered normal process has specification limits at $\mu\pm2\sigma$. Find $C_p$ and the approximate two-sided nonconformance using $P(|Z|>2)\approx0.0456$.

### Multiple Choice

20. Potential capability is:
A) $C_p$  B) $C_{pk}$  C) UCL  D) $\bar R$.

21. Actual two-sided capability is:
A) the larger side index  
B) the smaller side index  
C) the average of specification limits  
D) always equal to $C_p$.

22. A centered process has:
A) $C_{pk}>C_p$  
B) $C_{pk}=C_p$  
C) $C_{pk}=0$  
D) $C_p=0$.

23. If $C_p$ is high but $C_{pk}$ is much lower, the most direct concern is:
A) off-centering  
B) zero variance  
C) missing specification limits  
D) excessive sample size.

24. $C_p<1$ means:
A) the six-sigma process spread is wider than the specification width  
B) the process is automatically unstable  
C) every unit is defective  
D) the process mean equals the midpoint.

25. Which should be checked before interpreting capability?
A) statistical stability  
B) only the largest individual observation  
C) only the specification midpoint  
D) only the sample size.

26. For an upper-only specification, the relevant basic index is:
A) $C_{pu}$  
B) $C_{pl}$  
C) $D_4$  
D) $A_2$.

27. A capability index is:
A) a dimensionless process-to-specification ratio  
B) a probability automatically  
C) a control limit  
D) a specification limit.

---

## Answer Key with Explanations

### Conceptual

1. Statistical control asks whether the process is stable relative to its
   baseline. Capability asks whether a stable process fits within the external
   specification. (§40.1)

2. $C_p$ compares specification width with the process six-sigma spread and
   therefore describes potential capability if centered. (§40.2)

3. $C_{pk}$ includes the process mean's location relative to each specification
   boundary. (§40.3)

4. The nearer specification boundary is the limiting side for actual
   capability. (§40.3)

5. When the process mean equals the specification midpoint. (§40.4)

6. Off-centering can only reduce the distance to the nearer specification
   boundary relative to the centered case. (§40.4)

7. Capability assumes the reported mean and spread describe a consistent
   process. An unstable process does not have one reliable stationary center
   and spread. (§40.5)

8. $C_p$ and $C_{pk}$ are distance/spread ratios. A defect probability also
   requires a distributional model. (§40.6)

9. Use the relevant upper- or lower-side capability. Do not invent the missing
   specification boundary. (§40.7)

10. The required threshold depends on applicable customer, regulatory,
    organizational, or engineering requirements. (§40.7)

### Calculation

11.

    $$
    C_p
    =
    \frac{52-40}{6(1.5)}
    =
    \frac{12}{9}
    =
    \boxed{1.333}.
    $$

12. With

    $$
    \mu=46,
    $$

    $$
    C_{pl}
    =
    \frac{46-40}{4.5}
    =
    \boxed{1.333},
    $$

    $$
    C_{pu}
    =
    \frac{52-46}{4.5}
    =
    \boxed{1.333}.
    $$

    Therefore

    $$
    \boxed{C_{pk}=1.333}.
    $$

13.

    $$
    C_{pl}
    =
    \frac{49-40}{4.5}
    =
    2.000,
    $$

    $$
    C_{pu}
    =
    \frac{52-49}{4.5}
    =
    0.667.
    $$

    Therefore

    $$
    \boxed{C_{pk}=0.667}.
    $$

14. A perfectly centered two-sided process has

    $$
    \boxed{C_{pk}=C_p=1.50}.
    $$

15.

    $$
    C_p
    =
    \frac{105-95}{6(0.8)}
    =
    \frac{10}{4.8}
    =
    \boxed{2.083}.
    $$

    Lower side:

    $$
    C_{pl}
    =
    \frac{101-95}{2.4}
    =
    2.500.
    $$

    Upper side:

    $$
    C_{pu}
    =
    \frac{105-101}{2.4}
    =
    1.667.
    $$

    Therefore

    $$
    \boxed{C_{pk}=1.667}.
    $$

16.

    $$
    \hat\sigma
    =
    \frac{0.20}{2.326}
    \approx
    \boxed{0.0860}.
    $$

17. Use

    $$
    \hat\sigma\approx0.08598.
    $$

    Then

    $$
    C_p
    =
    \frac{1.0}{6(0.08598)}
    \approx
    \boxed{1.938}.
    $$

    Lower side:

    $$
    C_{pl}
    =
    \frac{20.1-19.5}{3(0.08598)}
    \approx
    2.326.
    $$

    Upper side:

    $$
    C_{pu}
    =
    \frac{20.5-20.1}{3(0.08598)}
    \approx
    1.551.
    $$

    Therefore

    $$
    \boxed{C_{pk}\approx1.551}.
    $$

18.

    $$
    C_{pu}
    =
    \frac{12-9}{3(0.5)}
    =
    \frac3{1.5}
    =
    \boxed2.
    $$

19. Specification width is

    $$
    4\sigma.
    $$

    Therefore

    $$
    C_p
    =
    \frac{4\sigma}{6\sigma}
    =
    \boxed{0.667}.
    $$

    Given the stated normal tail area,

    $$
    \boxed{P(\text{nonconforming})\approx0.0456=4.56\%}.
    $$

### Multiple Choice

20. **A.** $C_p$ is potential capability. (§40.2)

21. **B.** The smaller side controls actual capability. (§40.3)

22. **B.** Centering makes the two side distances equal and gives
    $C_{pk}=C_p$. (§40.4)

23. **A.** Large separation between $C_p$ and $C_{pk}$ indicates a centering
    penalty. (§40.4)

24. **A.** The process six-sigma spread is wider than the specification width.
    (§40.2)

25. **A.** Capability interpretation assumes a stable process. (§40.5)

26. **A.** Use $C_{pu}$ for an upper-only requirement. (§40.7)

27. **A.** Capability indices are dimensionless ratios. (§40.2–40.3)

---

## Practice Problems

1. **Centered capability.** A stable process has
   $$LSL=18,\quad USL=22,\quad \mu=20,\quad \sigma=0.40.$$
   Find $C_p$ and $C_{pk}$.

2. **Off-centered process.** Keep the specifications and $\sigma$ from Problem
   1, but let $\mu=21.2$. Find $C_{pl}$, $C_{pu}$, and $C_{pk}$.

3. **Spread problem.** A centered process has
   $$LSL=48,\quad USL=52,\quad \sigma=0.90.$$
   Find $C_p$ and state what the value says about six-sigma spread.

4. **Centering problem.** A process has
   $$C_p=1.80,\quad C_{pk}=0.90.$$
   Explain what those two numbers imply qualitatively.

5. **Sigma estimate from range.** For a stable $n=5$ process,
   $$\bar R=0.15,\quad d_2=2.326.$$
   Estimate $\sigma$.

6. **Capability from control-chart data.** Use Problem 5 with
   $$LSL=49.6,\quad USL=50.4,\quad \bar{\bar X}=50.05.$$
   Find $C_p$, $C_{pl}$, $C_{pu}$, and $C_{pk}$.

7. **Upper-only specification.** A contaminant concentration has
   $$USL=5.0,\quad \mu=3.2,\quad \sigma=0.40.$$
   Find $C_{pu}$.

8. **Lower-only specification.** A strength requirement has
   $$LSL=250,\quad \mu=280,\quad \sigma=8.$$
   Find $C_{pl}$.

9. **Normal-model nonconformance.** A centered normal process has
   $$LSL=97,\quad USL=103,\quad \mu=100,\quad \sigma=1.$$
   Find $C_p=C_{pk}$ and use the normal result
   $$P(|Z|>3)\approx0.0027$$
   to estimate the nonconforming fraction.

10. **Stability first.** A process produces a calculated
    $$C_{pk}=1.60,$$
    but its current $\bar X$ chart contains a point above UCL and its $R$ chart
    shows a run-rule signal. Explain why the numerical $C_{pk}$ should not be
    treated as a reliable capability summary yet.

---

## Practice Problem Solutions

1.

   $$
   C_p
   =
   \frac{22-18}{6(0.40)}
   =
   \frac4{2.4}
   =
   \boxed{1.667}.
   $$

   The process is centered:

   $$
   \boxed{C_{pk}=1.667}.
   $$

2.

   $$
   C_{pl}
   =
   \frac{21.2-18}{3(0.40)}
   =
   \frac{3.2}{1.2}
   =
   \boxed{2.667},
   $$

   $$
   C_{pu}
   =
   \frac{22-21.2}{1.2}
   =
   \boxed{0.667}.
   $$

   Therefore

   $$
   \boxed{C_{pk}=0.667}.
   $$

3.

   $$
   C_p
   =
   \frac{52-48}{6(0.90)}
   =
   \frac4{5.4}
   =
   \boxed{0.741}.
   $$

   Since

   $$
   C_p<1,
   $$

   the six-sigma spread is wider than the specification band even when centered.

4. The spread is potentially strong because

   $$
   C_p=1.80.
   $$

   But actual capability is much lower:

   $$
   C_{pk}=0.90.
   $$

   This indicates a substantial centering problem. The process is much closer
   to one specification boundary than the other.

5.

   $$
   \hat\sigma
   =
   \frac{0.15}{2.326}
   \approx
   \boxed{0.06449}.
   $$

6. Using

   $$
   \hat\sigma\approx0.06449,
   $$

   potential capability:

   $$
   C_p
   =
   \frac{50.4-49.6}{6(0.06449)}
   $$

   $$
   \approx
   \boxed{2.068}.
   $$

   Lower side:

   $$
   C_{pl}
   =
   \frac{50.05-49.6}{3(0.06449)}
   $$

   $$
   \approx
   \boxed{2.326}.
   $$

   Upper side:

   $$
   C_{pu}
   =
   \frac{50.4-50.05}{3(0.06449)}
   $$

   $$
   \approx
   \boxed{1.809}.
   $$

   Therefore

   $$
   \boxed{C_{pk}\approx1.809}.
   $$

7.

   $$
   C_{pu}
   =
   \frac{5.0-3.2}{3(0.40)}
   =
   \frac{1.8}{1.2}
   =
   \boxed{1.50}.
   $$

8.

   $$
   C_{pl}
   =
   \frac{280-250}{3(8)}
   =
   \frac{30}{24}
   =
   \boxed{1.25}.
   $$

9.

   $$
   C_p
   =
   \frac{103-97}{6(1)}
   =
   \boxed1.
   $$

   Because the process is centered,

   $$
   \boxed{C_{pk}=1}.
   $$

   Under the stated normal model,

   $$
   \boxed{
   P(\text{nonconforming})
   \approx
   0.0027
   =
   0.27\%.
   }
   $$

10. Capability indices summarize a process using a mean and standard deviation.
    The current control charts show evidence that the process is not stable.

    Therefore one fixed mean and one fixed standard deviation may not describe
    the process adequately.

    Investigate the control-chart signals first, establish a stable baseline,
    then recompute capability from that stable process.

---

## Quick Reference

**Specification midpoint**

$$
\boxed{
m
=
\frac{USL+LSL}{2}
}
$$

**Specification width**

$$
\boxed{
W_{\text{spec}}
=
USL-LSL
}
$$

**Potential capability**

$$
\boxed{
C_p
=
\frac{USL-LSL}{6\sigma}
}
$$

**Lower-side capability**

$$
\boxed{
C_{pl}
=
\frac{\mu-LSL}{3\sigma}
}
$$

**Upper-side capability**

$$
\boxed{
C_{pu}
=
\frac{USL-\mu}{3\sigma}
}
$$

**Actual capability**

$$
\boxed{
C_{pk}
=
\min(C_{pl},C_{pu})
}
$$

**Centered process**

$$
\boxed{
\mu=m
\Rightarrow
C_{pk}=C_p.
}
$$

**General relationship**

$$
\boxed{
C_{pk}\le C_p.
}
$$

**Sigma estimates from stable control-chart baselines**

$$
\boxed{
\hat\sigma
\approx
\frac{\bar R}{d_2}
}
$$

$$
\boxed{
\hat\sigma
\approx
\frac{\bar S}{c_4}
}
$$

**Normal-model warning**

Capability index $\ne$ defect probability.

To estimate expected nonconformance, combine specification distances with an
appropriate probability model.

**Sequence**

1. establish statistical stability,
2. estimate process center and spread,
3. compare with specification limits,
4. diagnose spread and/or centering,
5. apply the actual engineering acceptance requirement.

---

## What's Next

Process capability compares a stable continuous process with specification
limits.

The final Layer 1 chapter extends the same probability-and-quality foundation to
lot acceptance.

**Chapter 01-41 — Acceptance Sampling and Operating Characteristic Curves** will
develop:

- acceptance sampling by attributes,
- sample size and acceptance number,
- binomial and hypergeometric acceptance probabilities,
- operating characteristic curves,
- producer's and consumer's risk,
- acceptable quality and rejectable quality concepts,
- and why acceptance sampling is a lot-disposition tool rather than a substitute
  for process control.

The Industrial and Systems FE exam specification explicitly names **sampling
plans** and **OC curves** within Quality Control. The supplied Handbook provides
the binomial and hypergeometric probability formulas needed for the underlying
acceptance-probability calculations, even though a standalone acceptance-sampling
formula section was not located.

Carry one distinction forward:

> Capability evaluates the process. Acceptance sampling evaluates a submitted
> lot using a sampling rule.

— Your Mentor
