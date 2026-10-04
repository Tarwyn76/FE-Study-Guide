---
chapter: "01-39"
title: "Statistical Process Control and Control Charts"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-039-01, MATH-1D-039-02, MATH-1D-039-03, MATH-1D-039-04, MATH-1D-039-05, MATH-1D-039-06, MATH-1D-039-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-39: Statistical Process Control and Control Charts

> *"A control chart does not ask whether every measurement is perfect. It asks
> whether the process producing the measurements still behaves like the same
> process."*

---

## Before You Start

**Prerequisites:** [01-30 The Normal Distribution and the Central Limit Theorem](01-30-The-Normal-Distribution-and-the-Central-Limit-Theorem.md) ·
[01-31 Sampling Distributions, Student's t, and Chi-Square](01-31-Sampling-Distributions-Students-t-and-Chi-Square.md) ·
[01-38 Common Engineering Probability Distributions](01-38-Common-Engineering-Probability-Distributions.md)

**Skip if:** You can distinguish common-cause from special-cause variation;
form rational subgroups; calculate subgroup averages and ranges; calculate
$\bar{\bar X}$ and $\bar R$; construct Handbook $\bar X$ and $R$ control
limits using $A_2$, $D_3$, and $D_4$; construct $\bar X$ and $S$ limits using
$A_3$, $B_3$, and $B_4$; estimate process standard deviation from $\bar R/d_2$
or $\bar S/c_4$; apply the Handbook's four tests for out-of-control behavior;
and distinguish statistical control limits from engineering specification
limits.

**Time:** About 105–125 min reading and worked examples · 40–50 min review
questions · 70–85 min practice problems.

**Working convention:** The Handbook uses subgroup statistics. A process baseline
is established from multiple subgroups, and future subgroup statistics are
compared with the resulting limits. Do not recalculate the limits every time an
unusual future point appears; doing so can hide the very shift the chart is meant
to detect.

---

## On the Board Today

A production process varies even when nothing is wrong.

Machines vibrate.

Materials differ slightly.

Sensors contain noise.

Operators and ambient conditions are never perfectly identical.

The statistical-control question is therefore not

> Is there variation?

There will be.

The useful question is

> Is the observed variation consistent with the process that established the
> baseline, or is there evidence that something changed?

Control charts separate two broad kinds of behavior.

**Common-cause variation** is the routine background variation produced by the
current process system.

**Special-cause variation** is evidence of a change, disturbance, assignable
event, or nonrandom pattern that is not consistent with the baseline process.

The FE Reference Handbook gives the numerical machinery for:

- average-and-range charts,
- average-and-standard-deviation charts,
- chart constants,
- process-spread approximations,
- and four tests for out-of-control behavior.

The Handbook gives equations and tables.

This chapter develops how to use them without confusing control with
specification compliance.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **39.1** Distinguish common-cause and special-cause variation
* **39.2** Explain why control charts use ordered subgroups rather than one unordered data set
* **39.3** Compute subgroup averages, ranges, and standard deviations
* **39.4** Compute $\bar{\bar X}$, $\bar R$, and $\bar S$
* **39.5** Construct $\bar X$ and $R$ charts using Handbook constants
* **39.6** Construct $\bar X$ and $S$ charts using Handbook constants
* **39.7** Estimate process standard deviation using $d_2$ or $c_4$
* **39.8** Apply the Handbook's four tests for out-of-control behavior
* **39.9** Convert three-sigma control limits into one- and two-sigma zone boundaries when needed for run rules
* **39.10** Distinguish statistical control from conformance to specification limits
* **39.11** Decide whether to investigate process center, process spread, or both
* **39.12** State what a control-chart signal does and does not prove

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $X_{ij}$ | observation $j$ in subgroup $i$ | individual measurement |
| $n$ | observations per subgroup | Handbook table uses $n=2$ through 10 |
| $k$ | number of subgroups | baseline groups |
| $\bar X_i$ | mean of subgroup $i$ | plotted on average chart |
| $R_i$ | range of subgroup $i$ | maximum minus minimum |
| $S_i$ | sample standard deviation of subgroup $i$ | plotted on $S$ chart |
| $\bar{\bar X}$ | average of subgroup means | center line of $\bar X$ chart |
| $\bar R$ | average subgroup range | center line of $R$ chart |
| $\bar S$ | average subgroup standard deviation | center line of $S$ chart |
| $A_2,D_3,D_4$ | Handbook constants | $\bar X$-$R$ charts |
| $A_3,B_3,B_4$ | Handbook constants | $\bar X$-$S$ charts |
| $d_2,c_4$ | Handbook approximation constants | used to estimate process $\sigma$ |
| CL | center line | baseline central statistic |
| UCL | upper control limit | upper three-sigma-type boundary |
| LCL | lower control limit | lower three-sigma-type boundary |
| USL, LSL | upper/lower specification limits | engineering/customer limits, not control limits |

**Notation warning.** The symbol $\bar X$ is used both for a subgroup mean and,
with a second bar, for the average of subgroup means. Write the second quantity
clearly as

$$
\bar{\bar X}.
$$

---

## 39.1 Statistical Control — Stability Before Capability

A stable process does not mean every observation is identical.

It means the pattern of variation remains statistically consistent with the
baseline process.

### Common-cause variation

Common causes are the routine sources built into the present process system.

Examples might include small fluctuations in:

- raw material properties,
- machine vibration,
- ambient temperature,
- measurement noise.

If only common causes are acting, the process can still produce substantial
variation.

Statistical control means the process is **stable**, not necessarily **good**.

### Special-cause variation

A special cause is evidence that the process has changed.

Examples might include:

- tool breakage,
- incorrect setup,
- sensor shift,
- material-lot change,
- unexpected temperature excursion.

The specific physical cause is not identified by the chart alone.

The chart only supplies statistical evidence that the baseline model may no
longer describe the process.

### Control limits are not specification limits

A control limit comes from observed process behavior.

A specification limit comes from an engineering, customer, regulatory, or design
requirement.

These answer different questions.

Control chart:

> Is the process stable?

Specification:

> Is the output acceptable?

A process may be:

- stable but incapable of meeting specifications,
- unstable while every recent point still happens to lie inside specifications,
- stable and capable,
- unstable and incapable.

![FIG-01-39-001: Four-panel distinction between statistical control and specification compliance. Panel A stable process comfortably inside LSL/USL; Panel B stable but spread wider than specifications; Panel C unstable shift while points temporarily remain within specs; Panel D unstable and out of spec. Control limits and specification limits are drawn as different line styles and labeled explicitly.](../figures/FIG-01-39-001-control-versus-specification.png)

### Worked Example 1 — Stable Does Not Mean Acceptable

A process is centered at

$$
10.0\text{ mm}
$$

with stable natural variation that frequently produces values between

$$
9.4\text{ mm}
$$

and

$$
10.6\text{ mm}.
$$

The specification is

$$
9.8\le X\le10.2\text{ mm}.
$$

Even if the process is perfectly stable, much of its routine variation is wider
than the allowable specification band.

Correct conclusion:

> The process can be statistically stable and still fail the specification
> requirement.

Do not widen control limits merely to match the specification.

---

## 39.2 Rational Subgroups and Baseline Statistics

Control charts preserve the order in which the process was observed.

Data are collected in **subgroups**.

A subgroup should represent observations produced under conditions close enough
that its internal spread is meaningful as short-term process variation.

That design idea is called **rational subgrouping**.

The Handbook defines:

$$
n=\text{subgroup size}
$$

and

$$
k=\text{number of subgroups}.
$$

### Subgroup average

For subgroup $i$,

$$
\boxed{
\bar X_i
=
\frac1n
\sum_{j=1}^{n}X_{ij}.
}
$$

### Subgroup range

$$
\boxed{
R_i
=
X_{i,\max}
-
X_{i,\min}.
}
$$

### Average of subgroup means

$$
\boxed{
\bar{\bar X}
=
\frac1k
\sum_{i=1}^{k}\bar X_i.
}
$$

### Average range

$$
\boxed{
\bar R
=
\frac1k
\sum_{i=1}^{k}R_i.
}
$$

For an $S$ chart,

$$
\boxed{
\bar S
=
\frac1k
\sum_{i=1}^{k}S_i.
}
$$

![FIG-01-39-002: Rational-subgroup diagram. A time-ordered process stream is partitioned into several subgroups of n observations. Within each subgroup, arrows compute X-bar_i and R_i. The subgroup means then average to X-double-bar and the subgroup ranges average to R-bar. A note emphasizes preserving time order between subgroups.](../figures/FIG-01-39-002-rational-subgroups.png)

### Worked Example 2 — Subgroup Means and Ranges

Six subgroups contain five measurements each:

| Subgroup | Measurements |
|---:|---|
| 1 | 10.1, 9.9, 10.0, 10.2, 9.8 |
| 2 | 10.2, 10.1, 9.9, 10.0, 10.3 |
| 3 | 9.8, 10.0, 9.9, 10.1, 10.2 |
| 4 | 10.1, 10.0, 10.2, 10.3, 9.9 |
| 5 | 9.9, 9.8, 10.0, 10.1, 9.7 |
| 6 | 10.2, 10.3, 10.1, 10.0, 10.4 |

Subgroup means are:

$$
10.0,\quad10.1,\quad10.0,\quad10.1,\quad9.9,\quad10.2.
$$

Each subgroup range is

$$
0.4.
$$

Therefore

$$
\bar{\bar X}
=
\frac{10.0+10.1+10.0+10.1+9.9+10.2}{6}
=
\boxed{10.05}.
$$

and

$$
\bar R
=
\frac{6(0.4)}6
=
\boxed{0.40}.
$$

These baseline statistics now feed the control-limit formulas.

---

## 39.3 Average and Range Charts — $\bar X$ and $R$

For subgroup sizes listed in the Handbook, select

$$
A_2,\quad D_3,\quad D_4
$$

from printed p. 83.

### $R$ chart

The Handbook gives:

$$
\boxed{CL_R=\bar R}
$$

$$
\boxed{UCL_R=D_4\bar R}
$$

$$
\boxed{LCL_R=D_3\bar R.}
$$

The $R$ chart monitors within-subgroup spread.

### $\bar X$ chart using ranges

The Handbook gives:

$$
\boxed{CL_{\bar X}=\bar{\bar X}}
$$

$$
\boxed{
UCL_{\bar X}
=
\bar{\bar X}
+
A_2\bar R
}
$$

$$
\boxed{
LCL_{\bar X}
=
\bar{\bar X}
-
A_2\bar R.
}
$$

The $\bar X$ chart monitors process center through subgroup means.

### Which chart should be checked first?

The spread chart matters because the mean-chart limits rely on a stable estimate
of process variation.

If the $R$ chart signals an unstable spread, interpret the mean chart cautiously
until the source of spread instability is understood.

![FIG-01-39-003: Paired X-bar and R charts sharing a subgroup-number horizontal axis. Upper chart shows subgroup means with CL = X-double-bar and limits X-double-bar ± A2 R-bar. Lower chart shows ranges with CL=R-bar and limits D3 R-bar and D4 R-bar. A callout says "check spread stability before trusting the mean-chart interpretation."](../figures/FIG-01-39-003-xbar-r-chart-anatomy.png)

### Worked Example 3 — Construct $\bar X$ and $R$ Limits

Continue Worked Example 2.

Here

$$
n=5.
$$

From the Handbook table:

$$
A_2=0.577,\qquad D_3=0,\qquad D_4=2.114.
$$

With

$$
\bar{\bar X}=10.05,
\qquad
\bar R=0.40,
$$

the $R$ limits are

$$
CL_R=0.40,
$$

$$
UCL_R=2.114(0.40)=\boxed{0.8456},
$$

$$
LCL_R=0(0.40)=\boxed0.
$$

The mean-chart limits are

$$
UCL_{\bar X}
=
10.05+0.577(0.40)
=
\boxed{10.2808},
$$

and

$$
LCL_{\bar X}
=
10.05-0.577(0.40)
=
\boxed{9.8192}.
$$

All six baseline subgroup means lie between those limits, and each baseline range
lies within the $R$-chart limits.

That establishes the baseline used for monitoring.

### Worked Example 4 — A New Mean Signal

After the baseline is frozen, a seventh subgroup has

$$
\bar X_7=10.40
$$

and

$$
R_7=0.40.
$$

The range remains below

$$
UCL_R=0.8456.
$$

But the mean is above

$$
UCL_{\bar X}=10.2808.
$$

Therefore the new subgroup triggers the Handbook's most direct out-of-control
test:

$$
\boxed{\text{one point outside the three-sigma control limits}.}
$$

This is evidence to investigate a possible shift in process center.

Do **not** immediately recompute the baseline including the 10.40 point.

---

## 39.4 Average and Standard-Deviation Charts — $\bar X$ and $S$

When subgroup variability is summarized using the sample standard deviation
rather than range, the Handbook provides constants

$$
A_3,\quad B_3,\quad B_4.
$$

### $\bar X$ chart using $\bar S$

$$
\boxed{CL_{\bar X}=\bar{\bar X}}
$$

$$
\boxed{
UCL_{\bar X}
=
\bar{\bar X}
+
A_3\bar S
}
$$

$$
\boxed{
LCL_{\bar X}
=
\bar{\bar X}
-
A_3\bar S.
}
$$

### $S$ chart

$$
\boxed{CL_S=\bar S}
$$

$$
\boxed{UCL_S=B_4\bar S}
$$

$$
\boxed{LCL_S=B_3\bar S.}
$$

The Handbook table on printed p. 83 gives these constants for subgroup sizes
2 through 10.

![FIG-01-39-004: X-bar and S chart formula map. Subgroup standard deviations S_i average to S-bar. S-bar feeds B3 and B4 for S-chart limits and A3 for X-bar limits. The diagram contrasts the R-chart path using R-bar with the S-chart path using S-bar, emphasizing that the constants must match the chosen spread statistic.](../figures/FIG-01-39-004-xbar-s-chart.png)

### Worked Example 5 — $\bar X$-$S$ Limits

Suppose a baseline has

$$
n=5,
\qquad
\bar{\bar X}=50.00,
\qquad
\bar S=0.20.
$$

From the Handbook:

$$
A_3=1.427,\qquad B_3=0,\qquad B_4=2.089.
$$

Mean-chart limits:

$$
UCL_{\bar X}
=
50.00+1.427(0.20)
=
\boxed{50.2854},
$$

$$
LCL_{\bar X}
=
50.00-1.427(0.20)
=
\boxed{49.7146}.
$$

Spread-chart limits:

$$
UCL_S
=
2.089(0.20)
=
\boxed{0.4178},
$$

$$
LCL_S
=
0(0.20)
=
\boxed0.
$$

If a future subgroup has

$$
S_i=0.45,
$$

then

$$
0.45>0.4178.
$$

The process spread has produced an out-of-control signal even if its subgroup
mean lies near 50.00.

---

## 39.5 Estimating Process Standard Deviation

Printed p. 84 supplies approximation constants including

$$
d_2
$$

and

$$
c_4.
$$

For a stable process, these support initial estimates of process standard
deviation.

### From average range

$$
\boxed{
\hat\sigma
\approx
\frac{\bar R}{d_2}.
}
$$

### From average subgroup standard deviation

$$
\boxed{
\hat\sigma
\approx
\frac{\bar S}{c_4}.
}
$$

These are process-spread estimates.

They are not specification limits.

They are also not substitutes for investigating an unstable spread chart.

![FIG-01-39-005: Process-sigma estimation diagram. Left path: subgroup ranges -> R-bar -> divide by d2 -> sigma-hat. Right path: subgroup standard deviations -> S-bar -> divide by c4 -> sigma-hat. A warning box states "estimate sigma only from a baseline whose spread is reasonably stable."](../figures/FIG-01-39-005-process-sigma-estimation.png)

### Worked Example 6 — Estimate $\sigma$ from $\bar R$

Use the range-chart baseline from Worked Example 3:

$$
n=5,
\qquad
\bar R=0.40.
$$

From printed p. 84:

$$
d_2=2.326.
$$

Then

$$
\hat\sigma
=
\frac{0.40}{2.326}
\approx
\boxed{0.1720}.
$$

### Worked Example 7 — Estimate $\sigma$ from $\bar S$

Use the $S$-chart example:

$$
n=5,
\qquad
\bar S=0.20.
$$

The Handbook gives

$$
c_4=0.9400.
$$

Therefore

$$
\hat\sigma
=
\frac{0.20}{0.9400}
\approx
\boxed{0.2128}.
$$

These examples use different baseline datasets, so their two numerical estimates
are not expected to match.

---

## 39.6 Handbook Tests for Out-of-Control Behavior

Printed p. 84 gives four explicit tests.

A process is signaled as out of control when any of the following occurs.

### Test 1 — One point beyond three sigma

A single point falls outside the three-sigma control limits.

### Test 2 — Two of three beyond two sigma on the same side

Two out of three successive points fall on the same side of the center line and
more than two sigma units from it.

### Test 3 — Four of five beyond one sigma on the same side

Four out of five successive points fall on the same side of the center line and
more than one sigma unit from it.

### Test 4 — Eight successive points on one side

Eight successive points fall on the same side of the center line.

These rules detect nonrandom patterns before a point necessarily crosses the
three-sigma limit.

### Zone boundaries

If UCL and LCL are symmetric three-sigma limits around the center line, define

$$
d=UCL-CL.
$$

Then the upper one- and two-sigma zone boundaries are

$$
\boxed{CL+\frac d3}
$$

and

$$
\boxed{CL+\frac{2d}{3}.}
$$

The corresponding lower boundaries are

$$
CL-\frac d3
$$

and

$$
CL-\frac{2d}{3}.
$$

This zone construction is a guide-developed operational step for applying the
Handbook's stated run rules.

![FIG-01-39-006: Control-chart zone diagram. Horizontal center line with symmetric ±1 sigma, ±2 sigma, and ±3 sigma lines. Four annotated examples show: one point outside 3 sigma; two of three beyond 2 sigma on same side; four of five beyond 1 sigma on same side; eight points on same side of center.](../figures/FIG-01-39-006-out-of-control-tests.png)

### Worked Example 8 — Two of Three Beyond Two Sigma

Suppose a mean chart has

$$
CL=100.0
$$

and

$$
UCL=103.0,
\qquad
LCL=97.0.
$$

The distance from center to a three-sigma limit is

$$
d=3.0.
$$

So the upper two-sigma boundary is

$$
100+\frac{2(3)}3
=
\boxed{102.0}.
$$

Three successive subgroup means are

$$
102.3,\quad101.4,\quad102.5.
$$

Two of the three are on the same side of the center and more than two sigma
units above it.

Therefore the sequence triggers Handbook Test 2 even though no point exceeds

$$
UCL=103.0.
$$

### Worked Example 9 — Eight on One Side

Suppose eight successive subgroup means are

$$
50.1,\ 50.2,\ 50.1,\ 50.3,\ 50.2,\ 50.1,\ 50.4,\ 50.2
$$

with

$$
CL=50.0.
$$

Every point lies above the center line.

Even if all eight are far inside the UCL,

$$
\boxed{\text{Handbook Test 4 is triggered}.}
$$

The signal is the nonrandom sequence, not the magnitude of any one point.

---

## 39.7 Reading the Charts as an Engineering Diagnostic

A control-chart signal is a prompt to investigate.

It is not itself a root-cause analysis.

### Mean chart signals, spread chart stable

This pattern suggests investigation of factors that shift process center, such as:

- setup offset,
- calibration shift,
- changed target,
- material mean shift.

### Spread chart signals

This suggests investigation of factors affecting consistency, such as:

- tool wear or damage,
- fixture looseness,
- mixed material populations,
- measurement-system instability,
- changing operating conditions.

### Both charts signal

The process may have changed in center and spread, or a large disturbance may be
affecting both.

### No control-chart signal

Absence of a signal means the observed subgroup statistics remain compatible with
the baseline chart rules.

It does **not** prove:

- the process meets specification,
- every item is acceptable,
- no defect can occur,
- the baseline process is economically desirable.

### Baseline discipline

A useful sequence is:

1. collect subgroups in time order,
2. calculate subgroup statistics,
3. construct provisional charts,
4. investigate assignable signals,
5. correct documented special causes where justified,
6. establish the stable baseline,
7. freeze the monitoring limits,
8. compare future subgroup statistics with the baseline.

![FIG-01-39-007: Statistical-process-control workflow. Collect rational subgroups -> compute subgroup mean and spread -> chart spread -> if unstable investigate special cause -> chart mean -> apply four Handbook tests -> if signal investigate and document -> if stable freeze baseline -> monitor future subgroups. A separate branch points from "stable process" to "compare with specifications/capability" and warns that control and capability are different questions.](../figures/FIG-01-39-007-spc-workflow.png)

### Control chart versus hypothesis test

A control chart has conceptual similarities to repeated statistical testing, but
its purpose is operational monitoring.

The Handbook's run rules deliberately use patterns across successive points, not
only isolated limit crossings.

That sequence information is why you should not shuffle the subgroup order before
plotting.

### False alarms

Even a stable random process can occasionally produce an unusual sequence.

Therefore:

> a control-chart signal is evidence to investigate, not automatic proof of a
> particular physical failure.

The engineering response is to check process history, measurement integrity,
materials, setup, and operating conditions before assigning a cause.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed p. 83 contains *Statistical
> Quality Control*, including the $A_2$, $D_3$, $D_4$ table for average-and-range
> charts, the $\bar X$ and $R$ chart equations, and the $A_3$, $B_3$, $B_4$
> table and equations for standard-deviation charts. Printed p. 84 provides
> approximation constants including $c_4$, $d_2$, and $d_3$, and lists four
> explicit tests for out-of-control behavior.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Average and Range Charts | 83 | Defines subgroup size, number of groups, range, $\bar X_i$, $\bar{\bar X}$, and $\bar R$ structure |
| $R$ Chart | 83 | $CL=\bar R$, $UCL=D_4\bar R$, $LCL=D_3\bar R$ |
| $\bar X$ Chart using $\bar R$ | 83 | $CL=\bar{\bar X}$ and limits using $A_2\bar R$ |
| Standard Deviation Charts | 83 | Gives $A_3$, $B_3$, $B_4$ constants and $\bar X$-$S$ chart equations |
| Approximation Constants | 84 | Gives $c_4$, $d_2$, $d_3$ by subgroup size |
| Tests for Out of Control | 84 | Lists the one-point, 2-of-3, 4-of-5, and 8-on-one-side rules |

### Guide-developed interpretation

The supplied Handbook pages are compact calculation references. They do not
provide a full narrative treatment of:

- common-cause versus special-cause variation,
- rational subgrouping,
- why spread should be checked before trusting the mean chart,
- the difference between control limits and specification limits,
- baseline freezing,
- root-cause investigation,
- or false-alarm interpretation.

Those explanations are developed here so the Handbook formulas are used for the
question they actually answer.

**Know without a lookup:**

- control limits describe process behavior,
- specification limits describe requirements,
- subgroup order matters,
- mean and spread are monitored separately,
- a signal means investigate,
- and the Handbook's four out-of-control tests include patterns that can occur
  entirely inside the three-sigma limits.

---

## Where This Goes Wrong

**Calling all variation a defect.** Stable processes still vary.

**Calling every unusual point a proven special cause.** The chart signals
investigation; the physical cause still has to be established.

**Mixing observations from widely different operating conditions inside one
subgroup without considering the subgrouping logic.**

**Shuffling time order before plotting.** Run rules depend on sequence.

**Using the wrong constant table for the subgroup size.**

**Using $A_2$ with $\bar S$ or $A_3$ with $\bar R$.**

**Using $D_3$ and $D_4$ on a standard-deviation chart.**

**Using $B_3$ and $B_4$ on a range chart.**

**Confusing $\bar X_i$ with $\bar{\bar X}$.**

**Calculating one giant range from all observations instead of averaging subgroup
ranges.**

**Recomputing control limits after every signal.** This can move the baseline
toward the disturbance and hide it.

**Checking only for points beyond UCL/LCL.** The Handbook lists three additional
pattern tests.

**Applying the 2-of-3 rule across both sides of the center.** The points must be
on the same side.

**Applying the 8-point rule only when points are near the limits.** The rule only
requires eight successive points on the same side of the center line.

**Assuming an in-control process meets specifications.**

**Using specification limits as control limits.**

**Estimating process $\sigma$ from an obviously unstable spread baseline without
qualification.**

---

## Key Terms

| Term | Definition |
|---|---|
| statistical process control (SPC) | use of time-ordered statistical monitoring to assess process stability |
| control chart | plot of subgroup statistic against time/order with center line and control limits |
| common-cause variation | background variation generated by the current process system |
| special-cause variation | evidence of a process change or assignable disturbance beyond baseline behavior |
| rational subgroup | set of observations grouped so within-subgroup variation represents short-term process behavior |
| subgroup mean | average $\bar X_i$ within one subgroup |
| subgroup range | $R_i=X_{\max}-X_{\min}$ within one subgroup |
| subgroup standard deviation | $S_i$ within one subgroup |
| grand subgroup mean | $\bar{\bar X}$, average of subgroup means |
| average range | $\bar R$, average of subgroup ranges |
| average subgroup standard deviation | $\bar S$ |
| center line | baseline central statistic plotted on a control chart |
| upper control limit | upper statistical monitoring boundary |
| lower control limit | lower statistical monitoring boundary |
| specification limit | external acceptance/design boundary such as USL or LSL |
| average chart | chart of subgroup means |
| range chart | chart of subgroup ranges |
| standard-deviation chart | chart of subgroup standard deviations |
| out-of-control signal | chart pattern meeting a stated detection rule |
| baseline | historical stable period used to establish monitoring limits |
| control-chart zone | one-, two-, or three-sigma region around the center line |

---

## Review Questions

### Conceptual

1. Distinguish common-cause variation from special-cause variation.
2. What question does a control chart answer?
3. Why must subgroup order be preserved?
4. What is a rational subgroup?
5. Why should a spread chart be examined when interpreting a mean chart?
6. Distinguish control limits from specification limits.
7. What does $\bar{\bar X}$ represent?
8. What does $\bar R$ represent?
9. What does an out-of-control signal prove, and what does it not prove?
10. Why should baseline limits usually remain fixed during future monitoring?

### Calculation

11. A subgroup contains 8.1, 8.4, 8.0, 8.3, 8.2. Find $\bar X_i$ and $R_i$.
12. Subgroup means are 10.0, 10.2, 9.9, 10.1. Find $\bar{\bar X}$.
13. Subgroup ranges are 0.4, 0.5, 0.3, 0.4. Find $\bar R$.
14. For $n=5$, use $A_2=0.577$. If $\bar{\bar X}=20.00$ and $\bar R=0.50$, find the $\bar X$ limits.
15. For Question 14, use $D_3=0$ and $D_4=2.114$. Find the $R$ limits.
16. For $n=5$, $\bar{\bar X}=40.0$, $\bar S=0.30$, and $A_3=1.427$. Find the $\bar X$ limits.
17. For Question 16, use $B_3=0$ and $B_4=2.089$. Find the $S$ limits.
18. If $\bar R=0.60$ and $d_2=2.326$, estimate process $\sigma$.
19. A chart has $CL=50$ and $UCL=56$. Find the upper one-sigma and two-sigma zone boundaries.

### Multiple Choice

20. Which chart monitors subgroup spread using maximum minus minimum?
A) $\bar X$ chart  B) $R$ chart  C) decision tree  D) regression chart.

21. For an $\bar X$-$R$ chart, the mean-chart constant is:
A) $A_2$  B) $D_4$  C) $B_3$  D) $c_4$.

22. For an $R$ chart, the upper limit is:
A) $A_2\bar R$  
B) $D_4\bar R$  
C) $\bar{\bar X}+D_4$  
D) $B_4\bar S$.

23. A single point beyond the three-sigma limit is:
A) always ignored  
B) one Handbook out-of-control test  
C) a specification rule only  
D) proof of the physical root cause.

24. Which sequence triggers a Handbook rule even when all points are inside the three-sigma limits?
A) eight successive points on one side of center  
B) two points total anywhere  
C) one point exactly on center  
D) alternating points.

25. Statistical control means:
A) every product meets specification  
B) the process is behaving stably relative to its baseline  
C) process variance is zero  
D) no future signal can occur.

26. $\bar R/d_2$ is used to estimate:
A) process mean  
B) process standard deviation  
C) specification width  
D) sample size.

27. Specification limits should generally be:
A) substituted for UCL/LCL  
B) treated as external requirements distinct from statistical control limits  
C) recomputed from each subgroup  
D) ignored whenever a control chart is used.

---

## Answer Key with Explanations

### Conceptual

1. Common-cause variation is the routine background variation of the current
   process system. Special-cause variation is evidence that the process has
   changed relative to that baseline. (§39.1)

2. Whether the time-ordered subgroup statistics remain consistent with the
   baseline process behavior. (§39.1)

3. The Handbook's pattern tests use successive observations; shuffling destroys
   that information. (§39.6)

4. A subgroup formed so its within-group variation meaningfully represents
   short-term process behavior under comparable conditions. (§39.2)

5. Mean-chart limits depend on an estimate of process spread. An unstable spread
   weakens the interpretation of the mean chart. (§39.3)

6. Control limits are statistically derived from process behavior.
   Specification limits are external engineering/customer/design requirements.
   (§39.1)

7. It is the average of the subgroup means. (§39.2)

8. It is the average of subgroup ranges. (§39.2)

9. It provides statistical evidence that the baseline model may no longer
   describe the process. It does not identify the physical root cause by itself.
   (§39.6–39.7)

10. Moving the limits after every unusual point can absorb the disturbance into
    the baseline and hide the shift being monitored. (§39.7)

### Calculation

11.

    $$
    \bar X_i
    =
    \frac{8.1+8.4+8.0+8.3+8.2}{5}
    =
    \boxed{8.2}.
    $$

    $$
    R_i
    =
    8.4-8.0
    =
    \boxed{0.4}.
    $$

12.

    $$
    \bar{\bar X}
    =
    \frac{10.0+10.2+9.9+10.1}{4}
    =
    \boxed{10.05}.
    $$

13.

    $$
    \bar R
    =
    \frac{0.4+0.5+0.3+0.4}{4}
    =
    \boxed{0.40}.
    $$

14.

    $$
    UCL_{\bar X}
    =
    20.00+0.577(0.50)
    =
    \boxed{20.2885},
    $$

    $$
    LCL_{\bar X}
    =
    20.00-0.577(0.50)
    =
    \boxed{19.7115}.
    $$

15.

    $$
    UCL_R
    =
    2.114(0.50)
    =
    \boxed{1.057},
    $$

    $$
    LCL_R
    =
    0(0.50)
    =
    \boxed0.
    $$

16.

    $$
    UCL_{\bar X}
    =
    40.0+1.427(0.30)
    =
    \boxed{40.4281},
    $$

    $$
    LCL_{\bar X}
    =
    40.0-1.427(0.30)
    =
    \boxed{39.5719}.
    $$

17.

    $$
    UCL_S
    =
    2.089(0.30)
    =
    \boxed{0.6267},
    $$

    $$
    LCL_S
    =
    0(0.30)
    =
    \boxed0.
    $$

18.

    $$
    \hat\sigma
    =
    \frac{0.60}{2.326}
    \approx
    \boxed{0.2580}.
    $$

19. Three-sigma distance:

    $$
    d=56-50=6.
    $$

    One-sigma upper boundary:

    $$
    50+\frac63
    =
    \boxed{52}.
    $$

    Two-sigma upper boundary:

    $$
    50+\frac{2(6)}3
    =
    \boxed{54}.
    $$

### Multiple Choice

20. **B.** The $R$ chart plots subgroup ranges. (§39.3)

21. **A.** $A_2$ is the mean-chart constant paired with $\bar R$. (§39.3)

22. **B.** $UCL_R=D_4\bar R$. (§39.3)

23. **B.** It is the first Handbook out-of-control test. (§39.6)

24. **A.** Eight successive points on one side of the center line trigger the
    fourth Handbook rule. (§39.6)

25. **B.** Control concerns process stability, not guaranteed conformance.
    (§39.1)

26. **B.** $\bar R/d_2$ estimates process standard deviation. (§39.5)

27. **B.** Specifications and statistical control limits answer different
    questions. (§39.1)

---

## Practice Problems

1. **Subgroup statistics.** Five measurements are
   $$25.2,\ 25.0,\ 25.4,\ 24.9,\ 25.1.$$
   Find the subgroup mean and range.

2. **Baseline summaries.** Five subgroup means are
   $$30.1,\ 29.9,\ 30.0,\ 30.2,\ 29.8$$
   and corresponding ranges are
   $$0.5,\ 0.4,\ 0.6,\ 0.5,\ 0.4.$$
   Find $\bar{\bar X}$ and $\bar R$.

3. **$\bar X$-$R$ limits.** For Problem 2, subgroup size is $n=5$.
   Use
   $$A_2=0.577,\quad D_3=0,\quad D_4=2.114.$$
   Find all six chart quantities: the two center lines and four limits.

4. **Future subgroup.** Using the Problem 3 baseline, a new subgroup has
   $$\bar X=30.35,\qquad R=0.45.$$
   Determine whether either chart gives a one-point control-limit signal.

5. **$\bar X$-$S$ limits.** A baseline has
   $$n=4,\quad \bar{\bar X}=75.0,\quad\bar S=0.50.$$
   Use
   $$A_3=1.628,\quad B_3=0,\quad B_4=2.266.$$
   Find the $\bar X$ and $S$ limits.

6. **Sigma from range.** For
   $$n=5,\quad \bar R=0.70,\quad d_2=2.326,$$
   estimate process $\sigma$.

7. **Sigma from standard deviation.** For
   $$n=5,\quad \bar S=0.28,\quad c_4=0.9400,$$
   estimate process $\sigma$.

8. **Zone test.** A chart has
   $$CL=100,\quad UCL=106,\quad LCL=94.$$
   Three successive points are
   $$104.3,\ 101.0,\ 104.6.$$
   Determine whether the Handbook 2-of-3 beyond two-sigma rule is triggered.

9. **Eight-point rule.** A center line is 20.0. Eight successive values are
   $$20.1,\ 20.3,\ 20.2,\ 20.1,\ 20.4,\ 20.2,\ 20.1,\ 20.3.$$
   All are inside the control limits. State whether a Handbook signal occurs
   and why.

10. **Control versus specification.** A process is stable with control limits
    48 to 52, while product specifications are 49.5 to 50.5.
    Explain what can be concluded about stability and why the chart alone does
    not establish acceptable process capability.

---

## Practice Problem Solutions

1.

   $$
   \bar X
   =
   \frac{25.2+25.0+25.4+24.9+25.1}{5}
   =
   \boxed{25.12}.
   $$

   $$
   R
   =
   25.4-24.9
   =
   \boxed{0.50}.
   $$

2.

   $$
   \bar{\bar X}
   =
   \frac{30.1+29.9+30.0+30.2+29.8}{5}
   =
   \boxed{30.0}.
   $$

   $$
   \bar R
   =
   \frac{0.5+0.4+0.6+0.5+0.4}{5}
   =
   \boxed{0.48}.
   $$

3.

   $$
   CL_{\bar X}
   =
   \boxed{30.0}.
   $$

   $$
   UCL_{\bar X}
   =
   30.0+0.577(0.48)
   =
   \boxed{30.27696},
   $$

   $$
   LCL_{\bar X}
   =
   30.0-0.577(0.48)
   =
   \boxed{29.72304}.
   $$

   $$
   CL_R
   =
   \boxed{0.48}.
   $$

   $$
   UCL_R
   =
   2.114(0.48)
   =
   \boxed{1.01472},
   $$

   $$
   LCL_R
   =
   \boxed0.
   $$

4. Mean:

   $$
   30.35>30.27696.
   $$

   The $\bar X$ chart gives a one-point upper-limit signal.

   Range:

   $$
   0<0.45<1.01472.
   $$

   The $R$ chart does not give a one-point limit signal.

   Therefore

   $$
   \boxed{\text{center signal, no range-limit signal}.}
   $$

5.

   $$
   UCL_{\bar X}
   =
   75.0+1.628(0.50)
   =
   \boxed{75.814},
   $$

   $$
   LCL_{\bar X}
   =
   75.0-1.628(0.50)
   =
   \boxed{74.186}.
   $$

   $$
   CL_S
   =
   \boxed{0.50},
   $$

   $$
   UCL_S
   =
   2.266(0.50)
   =
   \boxed{1.133},
   $$

   $$
   LCL_S
   =
   \boxed0.
   $$

6.

   $$
   \hat\sigma
   =
   \frac{0.70}{2.326}
   \approx
   \boxed{0.3009}.
   $$

7.

   $$
   \hat\sigma
   =
   \frac{0.28}{0.9400}
   \approx
   \boxed{0.2979}.
   $$

8. The distance from center to UCL is

   $$
   106-100=6.
   $$

   The upper two-sigma boundary is

   $$
   100+\frac{2(6)}3
   =
   104.
   $$

   Two of the three points,

   $$
   104.3
   $$

   and

   $$
   104.6,
   $$

   are above 104 and on the same side of the center.

   Therefore

   $$
   \boxed{\text{the Handbook 2-of-3 rule is triggered}.}
   $$

9. Every one of the eight successive values lies above

   $$
   CL=20.0.
   $$

   Therefore

   $$
   \boxed{\text{Handbook Test 4 is triggered}.}
   $$

   The fact that all eight points remain inside UCL/LCL does not cancel the
   run-rule signal.

10. The process may be statistically stable because the stated control limits
    describe a consistent baseline.

    But the specification band

    $$
    49.5\text{ to }50.5
    $$

    is much narrower than the process control band

    $$
    48\text{ to }52.
    $$

    Stability alone does not establish that the process can routinely meet the
    specification.

    Control and capability are different questions.

---

## Quick Reference

**Subgroup statistics**

$$
\bar X_i=\frac1n\sum_jX_{ij},
\qquad
R_i=X_{\max}-X_{\min}.
$$

$$
\bar{\bar X}
=
\frac1k\sum_i\bar X_i,
\qquad
\bar R
=
\frac1k\sum_iR_i,
\qquad
\bar S
=
\frac1k\sum_iS_i.
$$

**$\bar X$-$R$ charts**

$$
CL_R=\bar R,
\qquad
UCL_R=D_4\bar R,
\qquad
LCL_R=D_3\bar R.
$$

$$
CL_{\bar X}=\bar{\bar X},
$$

$$
UCL_{\bar X}
=
\bar{\bar X}+A_2\bar R,
\qquad
LCL_{\bar X}
=
\bar{\bar X}-A_2\bar R.
$$

**$\bar X$-$S$ charts**

$$
UCL_{\bar X}
=
\bar{\bar X}+A_3\bar S,
\qquad
LCL_{\bar X}
=
\bar{\bar X}-A_3\bar S.
$$

$$
CL_S=\bar S,
\qquad
UCL_S=B_4\bar S,
\qquad
LCL_S=B_3\bar S.
$$

**Process standard-deviation approximations**

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

**Handbook out-of-control tests**

1. one point outside three-sigma control limits,
2. two of three successive points on the same side and beyond two sigma,
3. four of five successive points on the same side and beyond one sigma,
4. eight successive points on the same side of the center line.

**Zone boundaries**

If

$$
d=UCL-CL,
$$

then

$$
1\sigma:\quad CL\pm\frac d3,
$$

$$
2\sigma:\quad CL\pm\frac{2d}{3}.
$$

**Core distinction**

control limits → **process behavior**  
specification limits → **engineering requirement**.

---

## What's Next

Control charts tell you whether a process is statistically stable.

A stable process can still be too wide, too far off target, or otherwise unable
to meet the required tolerance band.

**Chapter 01-40 — Process Capability and Specification Performance** will develop:

- potential process capability,
- actual process capability,
- $C_p$ and $C_{pk}$,
- upper and lower specification limits,
- the effect of process centering,
- the relationship between process spread and specification width,
- capability interpretation only after stability is established,
- and why capability indices do not replace the engineering meaning of the
  specification itself.

The FE Reference Handbook gives process-capability relationships in the
Industrial and Systems Engineering section on printed p. 423.

Carry one distinction forward:

> Statistical control asks whether the process is stable. Process capability
> asks whether a stable process can fit inside the required specification band.

— Your Mentor
