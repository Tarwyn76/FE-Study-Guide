---
chapter: "01-34"
title: "Analysis of Variance and Design of Experiments"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-034-01, MATH-1D-034-02, MATH-1D-034-03, MATH-1D-034-04, MATH-1D-034-05, MATH-1D-034-06, MATH-1D-034-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-34: Analysis of Variance and Design of Experiments

> *"ANOVA asks whether differences among group means are large compared with the
> variation that remains inside the groups. Design of experiments determines
> whether that comparison is worth trusting."*

---

## Before You Start

**Prerequisites:** [01-29 Random Variables and Probability Distributions](01-29-Random-Variables-and-Probability-Distributions.md) ·
[01-31 Sampling Distributions, Student's t, and Chi-Square](01-31-Sampling-Distributions-Students-t-and-Chi-Square.md) ·
[01-33 Hypothesis Testing and Statistical Decisions](01-33-Hypothesis-Testing-and-Statistical-Decisions.md)

**Skip if:** You can identify factors, levels, treatments, responses, experimental
units, replication, randomization, and blocks; partition total variation into
treatment and error components; construct a one-way ANOVA table; compute mean
squares and an $F$ statistic; interpret a significant ANOVA without claiming that
every group differs; explain why blocking can remove nuisance variation; construct
a randomized complete block ANOVA table; distinguish main effects from interaction
in a two-factor experiment; and recognize the role of replication in estimating
experimental error.

**Time:** About 110–130 min reading and worked examples · 40–50 min review
questions · 70–90 min practice problems.

**Working convention:** ANOVA calculations are organized through **sums of
squares**, **degrees of freedom**, **mean squares**, and **$F$ ratios**. Keep those
four layers separate. A correct sum of squares divided by the wrong degrees of
freedom produces the wrong test.

---

## On the Board Today

Suppose three process settings produce sample means

$$
8,\qquad 12,\qquad 9.
$$

Those means are different.

But sample means are almost always different.

The statistical question is whether the differences are large compared with the
variation expected among observations exposed to the same treatment.

ANOVA—**analysis of variance**—answers that question by partitioning variability.

For a one-factor experiment,

$$
\boxed{
SS_{\text{total}}
=
SS_{\text{treatments}}
+
SS_{\text{error}}.
}
$$

The treatment term measures variation associated with differences among group
means.

The error term measures variation remaining within the groups.

Each sum of squares is converted to a **mean square** by dividing by its degrees
of freedom.

Then ANOVA forms the ratio

$$
\boxed{
F
=
\frac{MS_{\text{treatments}}}
{MS_{\text{error}}}.
}
$$

If the treatment means are genuinely different relative to the background
variation, the numerator becomes large compared with the denominator.

But ANOVA is only part of the story.

A poor experiment can produce a mathematically correct $F$ ratio that answers
the wrong question.

That is why this chapter treats **experimental design** and **ANOVA** together.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **34.1** Identify factors, levels, treatments, responses, experimental units, replicates, and blocks
* **34.2** Explain why randomization, replication, and blocking serve different purposes
* **34.3** State the one-way ANOVA null and alternative hypotheses
* **34.4** Partition one-way total variation into treatment and error sums of squares
* **34.5** Construct the one-way ANOVA table and compute its $F$ statistic
* **34.6** Interpret an ANOVA rejection without claiming which individual means differ
* **34.7** Explain the purpose of a randomized complete block design
* **34.8** Partition variation into treatment, block, and error terms
* **34.9** Construct a randomized complete block ANOVA table
* **34.10** Distinguish Factor A, Factor B, and $AB$ interaction in a two-factor factorial design
* **34.11** Construct the two-factor factorial ANOVA degrees of freedom and $F$ ratios
* **34.12** Check whether the design and ANOVA assumptions support the intended engineering conclusion

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $y_{ij}$ | observation $j$ under treatment $i$ | one-way notation |
| $y_{ijk}$ | observation $k$ at factor combination $(i,j)$ | two-factor notation |
| $k$ | number of treatments | one-way / block design |
| $n_i$ | sample size for treatment $i$ | may differ by treatment |
| $N$ | total number of observations | $N=\sum_i n_i$ |
| $\bar y_i$ | mean response for treatment $i$ | one-way |
| $\bar y$ | grand mean | mean of all observations |
| $SS$ | sum of squares | measure of variation |
| $MS$ | mean square | $SS$ divided by its df |
| $MST$ | treatment mean square | one-way / block design |
| $MSE$ | error mean square | denominator for ANOVA $F$ tests |
| $MSB$ | block mean square | randomized block design |
| $SSA,SSB$ | main-effect sums of squares | two-factor design |
| $SSAB$ | interaction sum of squares | two-factor design |
| $F$ | ratio of mean squares | compared with an $F$ critical value |
| $a,b$ | levels of Factors A and B | two-factor factorial design |
| $n$ | repetitions per factor combination | two-factor factorial design |

**Handbook dot notation.** The FE Reference Handbook uses a dot subscript to
indicate summation over that subscript. For example, $y_{i\bullet}$ denotes the
total over observations for treatment $i$, and $y_{\bullet\bullet}$ denotes the
grand total. This chapter uses both dot-total notation and sample-mean notation.

---

## 34.1 Design of Experiments — What Is Being Changed and What Is Being Measured?

A **factor** is an input or condition deliberately studied.

A **level** is one setting or category of a factor.

A **treatment** is the experimental condition applied to an experimental unit.

For a one-factor experiment, the factor levels are the treatments.

A **response** is the measured output.

An **experimental unit** is the smallest unit independently assigned to a
treatment.

### Example

Suppose an engineer studies curing temperature at

$$
150^\circ\text{C},
\quad
175^\circ\text{C},
\quad
200^\circ\text{C}
$$

and measures tensile strength.

Then:

- factor: curing temperature,
- levels: 150, 175, 200 °C,
- treatments: the three temperature settings,
- response: tensile strength,
- experimental units: the independently cured specimens.

### Replication

**Replication** means applying a treatment independently to more than one
experimental unit.

Replication provides information about experimental variability.

Repeatedly reading the same specimen with the same instrument may characterize
measurement repeatability, but it is not automatically equivalent to independent
experimental replication.

### Randomization

**Randomization** assigns treatments or run order using a random mechanism.

Its purpose is to reduce systematic alignment between treatments and uncontrolled
conditions such as:

- warm-up drift,
- operator fatigue,
- material-lot order,
- ambient temperature,
- tool wear.

### Blocking

A **block** groups experimental units that are similar with respect to a known
nuisance source of variability.

Examples:

- material lot,
- test day,
- operator,
- machine,
- location.

Within a block, the treatments are compared under more nearly comparable
conditions.

![FIG-01-34-001: Design-of-experiments terminology diagram. A factor "curing temperature" branches to three levels 150, 175, 200 C. Each level is assigned to several independently prepared specimens labeled experimental units. Tensile strength is shown as the response. A separate panel distinguishes replication, randomization of run order, and blocking by material lot, with short captions describing the purpose of each.](../figures/FIG-01-34-001-doe-terminology.png)

### Worked Example 1 — Identify the Design Elements

A lab compares four coating formulations. Each formulation is applied to six
separate steel coupons. Coupons come from three material lots, and each lot
receives every formulation.

Identify the design elements.

**Solution.**

Factor:

$$
\boxed{\text{coating formulation}}
$$

Levels/treatments:

$$
\boxed{4}
$$

Response: whichever coating-performance quantity is measured, such as adhesion
strength or corrosion loss.

Experimental units:

$$
\boxed{\text{individual steel coupons}}
$$

Replication: multiple independently coated coupons receive each formulation.

Block candidate:

$$
\boxed{\text{material lot}}
$$

Because every lot receives every formulation, the lot structure can support a
complete-block comparison if the allocation is balanced appropriately.

---

## 34.2 One-Way ANOVA — Partitioning Total Variation

Suppose $k$ independent treatment groups contain a total of $N$ observations.

The one-way ANOVA null hypothesis is

$$
\boxed{
H_0:
\mu_1=\mu_2=\cdots=\mu_k.
}
$$

The alternative is

$$
\boxed{
H_1:
\text{not all treatment means are equal}.
}
$$

Notice what $H_1$ does **not** say.

It does not say every mean differs from every other mean.

### Total variation

Using deviations from the grand mean,

$$
\boxed{
SS_{\text{total}}
=
\sum_{i=1}^{k}
\sum_{j=1}^{n_i}
(y_{ij}-\bar y)^2.
}
$$

### Treatment variation

Variation associated with differences among treatment means is

$$
\boxed{
SS_{\text{treatments}}
=
\sum_{i=1}^{k}
n_i
(\bar y_i-\bar y)^2.
}
$$

Equivalent dot-total formulas are printed in the Handbook.

### Error variation

Within-treatment variation is

$$
\boxed{
SS_{\text{error}}
=
\sum_{i=1}^{k}
\sum_{j=1}^{n_i}
(y_{ij}-\bar y_i)^2.
}
$$

The decomposition is

$$
\boxed{
SS_{\text{total}}
=
SS_{\text{treatments}}
+
SS_{\text{error}}.
}
$$

![FIG-01-34-002: One-way ANOVA variation decomposition. Three treatment groups are shown as vertical clusters with group means and one grand mean line. Horizontal arrows from group means to the grand mean are labeled between-treatment variation; vertical scatter of observations around each group mean is labeled within-treatment/error variation. The equation SS_total = SS_treatments + SS_error appears beneath.](../figures/FIG-01-34-002-one-way-variation-decomposition.png)

### Worked Example 2 — Compute the One-Way Sums of Squares

Three treatments produce:

| Treatment A | Treatment B | Treatment C |
|---:|---:|---:|
| 8 | 12 | 9 |
| 9 | 11 | 10 |
| 7 | 13 | 8 |

Treatment means:

$$
\bar y_A=8,
\qquad
\bar y_B=12,
\qquad
\bar y_C=9.
$$

Grand mean:

$$
\bar y
=
\frac{87}{9}
=
\frac{29}{3}
\approx
9.6667.
$$

Treatment sum of squares:

$$
SS_{\text{treatments}}
=
3\left[
\left(8-\frac{29}{3}\right)^2
+
\left(12-\frac{29}{3}\right)^2
+
\left(9-\frac{29}{3}\right)^2
\right].
$$

Therefore

$$
\boxed{
SS_{\text{treatments}}=26.
}
$$

Within each treatment, the squared deviations sum to 2:

$$
A:\quad
(8-8)^2+(9-8)^2+(7-8)^2=2,
$$

$$
B:\quad
(12-12)^2+(11-12)^2+(13-12)^2=2,
$$

$$
C:\quad
(9-9)^2+(10-9)^2+(8-9)^2=2.
$$

Thus

$$
\boxed{
SS_{\text{error}}=6.
}
$$

and

$$
\boxed{
SS_{\text{total}}=26+6=32.
}
$$

**Check.** The decomposition closes exactly.

---

## 34.3 The One-Way ANOVA Table and $F$ Test

The Handbook gives the one-way ANOVA table in the following structure:

| Source | Degrees of freedom | Sum of squares | Mean square | $F$ |
|---|---:|---:|---:|---:|
| Between Treatments | $k-1$ | $SS_{\text{treatments}}$ | $MST=SS_{\text{treatments}}/(k-1)$ | $MST/MSE$ |
| Error | $N-k$ | $SS_{\text{error}}$ | $MSE=SS_{\text{error}}/(N-k)$ | — |
| Total | $N-1$ | $SS_{\text{total}}$ | — | — |

The degrees of freedom also partition:

$$
\boxed{
N-1
=
(k-1)+(N-k).
}
$$

### Why the $F$ ratio works

If the treatment means are all describing the same population mean, both

$$
MST
$$

and

$$
MSE
$$

represent variation on approximately the same scale.

Then an $F$ ratio near 1 is not surprising.

If treatment means are separated far beyond the within-group scatter,

$$
MST
$$

becomes large relative to

$$
MSE.
$$

Large $F$ values support rejection of equal means.

![FIG-01-34-003: One-way ANOVA table anatomy. A table highlights Source, df, SS, MS, and F columns. Arrows show SS divided by df to create MST and MSE, then MST divided by MSE to create F. A small F-distribution curve shows an upper-tail rejection region because large F supports treatment differences.](../figures/FIG-01-34-003-one-way-anova-table.png)

### Worked Example 3 — Complete the One-Way ANOVA

Continue Worked Example 2.

There are

$$
k=3
$$

treatments and

$$
N=9
$$

observations.

Treatment degrees of freedom:

$$
k-1=2.
$$

Error degrees of freedom:

$$
N-k=6.
$$

Total degrees of freedom:

$$
N-1=8.
$$

Treatment mean square:

$$
MST
=
\frac{26}{2}
=
13.
$$

Error mean square:

$$
MSE
=
\frac{6}{6}
=
1.
$$

Therefore

$$
\boxed{
F_0
=
\frac{13}{1}
=
13.
}
$$

ANOVA table:

| Source | df | SS | MS | $F_0$ |
|---|---:|---:|---:|---:|
| Treatments | 2 | 26 | 13 | 13 |
| Error | 6 | 6 | 1 | — |
| Total | 8 | 32 | — | — |

At

$$
\alpha=0.05,
$$

the Handbook $F$ table gives approximately

$$
F_{0.05,2,6}=5.14.
$$

Because

$$
13>5.14,
$$

$$
\boxed{\text{reject }H_0.}
$$

There is evidence that the three population treatment means are not all equal.

### What ANOVA did not tell you

The conclusion is **not**

> all three population means differ.

The global $F$ test only establishes that the equal-means model is not supported.

Determining which treatment pairs differ requires an additional comparison
procedure or a specifically planned contrast. That follow-up machinery is not
developed in the supplied Handbook ANOVA pages and is outside this chapter's core
scope.

---

## 34.4 Randomized Complete Block Design

A randomized complete block design is useful when one known nuisance factor may
create large variability.

The Handbook defines the design for:

- $k$ treatments,
- $b$ blocks,
- every block containing every treatment once.

The response is modeled through three variation components:

$$
\boxed{
SS_{\text{total}}
=
SS_{\text{treatments}}
+
SS_{\text{blocks}}
+
SS_{\text{error}}.
}
$$

Blocking attempts to move predictable nuisance variation out of the error term.

### Sums of squares

With one observation per treatment-block combination:

$$
SS_{\text{total}}
=
\sum_i\sum_j
(y_{ij}-\bar y)^2.
$$

Treatment variation:

$$
\boxed{
SS_{\text{treatments}}
=
b
\sum_{i=1}^{k}
(\bar y_{i\bullet}-\bar y)^2.
}
$$

Block variation:

$$
\boxed{
SS_{\text{blocks}}
=
k
\sum_{j=1}^{b}
(\bar y_{\bullet j}-\bar y)^2.
}
$$

Then

$$
\boxed{
SS_{\text{error}}
=
SS_{\text{total}}
-
SS_{\text{treatments}}
-
SS_{\text{blocks}}.
}
$$

### Degrees of freedom

| Source | df |
|---|---:|
| Treatments | $k-1$ |
| Blocks | $b-1$ |
| Error | $(k-1)(b-1)$ |
| Total | $kb-1$ |

Treatment test:

$$
\boxed{
F_{\text{treatments}}
=
\frac{MST}{MSE}.
}
$$

Block test:

$$
\boxed{
F_{\text{blocks}}
=
\frac{MSB}{MSE}.
}
$$

![FIG-01-34-004: Randomized complete block design matrix. Rows are four blocks such as material lots; columns are treatments A, B, C. Each row contains all three treatments, with randomized within-row order indicated. Arrows show total variation being partitioned into treatment, block, and residual error. A side note states that blocking removes a known nuisance source from the error term.](../figures/FIG-01-34-004-randomized-complete-block.png)

### Worked Example 4 — Why Blocking Helps

Suppose three treatments are compared across four material lots:

| Block | A | B | C |
|---|---:|---:|---:|
| 1 | 8 | 10 | 9 |
| 2 | 7 | 9 | 8 |
| 3 | 10 | 13 | 11 |
| 4 | 9 | 11 | 10 |

The treatment means are

$$
8.50,\quad10.75,\quad9.50.
$$

The block means are

$$
9.00,\quad8.00,\quad11.3333,\quad10.00.
$$

There is substantial block-to-block movement.

If that material-lot effect were ignored, it would inflate the apparent
within-experiment noise.

Blocking gives it its own sum of squares.

### Worked Example 5 — Complete the Block ANOVA

For the data above,

$$
\bar y
=
9.5833.
$$

The sums of squares are

$$
SS_{\text{total}}
=
28.9167,
$$

$$
SS_{\text{treatments}}
=
10.1667,
$$

$$
SS_{\text{blocks}}
=
18.2500,
$$

and

$$
SS_{\text{error}}
=
28.9167-10.1667-18.2500
=
0.5000.
$$

Degrees of freedom:

$$
df_T=3-1=2,
$$

$$
df_B=4-1=3,
$$

$$
df_E=(3-1)(4-1)=6,
$$

$$
df_{\text{total}}=12-1=11.
$$

Mean squares:

$$
MST
=
\frac{10.1667}{2}
=
5.0833,
$$

$$
MSB
=
\frac{18.25}{3}
=
6.0833,
$$

$$
MSE
=
\frac{0.5}{6}
=
0.08333.
$$

Therefore

$$
F_T
=
\frac{5.0833}{0.08333}
\approx
\boxed{61.0},
$$

and

$$
F_B
=
\frac{6.0833}{0.08333}
\approx
\boxed{73.0}.
$$

The large block $F$ ratio confirms that the nuisance factor captured substantial
variation in this constructed example.

**Design lesson.** A useful block can sharply reduce the residual error against
which treatments are compared.

---

## 34.5 Two-Factor Factorial Designs and Interaction

A **factorial design** studies more than one factor simultaneously.

The Handbook's two-factor factorial formulas use:

- $a$ levels of Factor A,
- $b$ levels of Factor B,
- $n$ repetitions per treatment combination or **cell**.

There are

$$
ab
$$

factor combinations and

$$
abn
$$

observations.

The total variation partitions as

$$
\boxed{
SS_{\text{total}}
=
SSA+SSB+SSAB+SS_{\text{error}}.
}
$$

### Main effect of Factor A

A main effect asks whether average response changes across levels of A, averaging
over B.

### Main effect of Factor B

Likewise, the B main effect compares levels of B, averaging over A.

### Interaction

An **interaction** occurs when the effect of one factor depends on the level of
the other factor.

For two levels of each factor, compare simple effects.

If the B effect at $A_1$ is

$$
\Delta_B(A_1)
$$

and the B effect at $A_2$ is

$$
\Delta_B(A_2),
$$

then unequal effects suggest interaction.

A difference-of-differences expression is

$$
\boxed{
\Delta_B(A_2)-\Delta_B(A_1).
}
$$

If the interaction is substantial, main effects must be interpreted cautiously
because an average effect can hide different behavior at different factor
combinations.

![FIG-01-34-005: Two-panel interaction plot. Left panel shows response versus Factor B for two levels of Factor A with nearly parallel lines, labeled little/no interaction. Right panel shows nonparallel lines whose separation changes strongly across B, labeled interaction. A callout says "interaction: effect of one factor depends on the level of the other."](../figures/FIG-01-34-005-factorial-interaction.png)

### Worked Example 6 — Detect Interaction from Cell Means

Suppose cell means are:

| | $B_1$ | $B_2$ |
|---|---:|---:|
| $A_1$ | 11 | 15 |
| $A_2$ | 19 | 31 |

At $A_1$, the B effect is

$$
15-11
=
4.
$$

At $A_2$, the B effect is

$$
31-19
=
12.
$$

Difference of differences:

$$
12-4
=
\boxed{8}.
$$

The effect of B is not constant across A.

This is interaction behavior.

### Two-factor ANOVA degrees of freedom

For a replicated two-factor design:

| Source | df |
|---|---:|
| Factor A | $a-1$ |
| Factor B | $b-1$ |
| $AB$ interaction | $(a-1)(b-1)$ |
| Error | $ab(n-1)$ |
| Total | $abn-1$ |

Mean squares are formed by dividing each sum of squares by its degrees of freedom.

Then

$$
\boxed{
F_A=\frac{MSA}{MSE}
}
$$

$$
\boxed{
F_B=\frac{MSB}{MSE}
}
$$

and

$$
\boxed{
F_{AB}=\frac{MSAB}{MSE}.
}
$$

---

## 34.6 Two-Factor ANOVA — A Complete Small Example

Consider a $2\times2$ factorial experiment with two independent repetitions per
cell:

| | $B_1$ | $B_2$ |
|---|---|---|
| $A_1$ | 10, 12 | 14, 16 |
| $A_2$ | 18, 20 | 30, 32 |

The cell means are

$$
11,\quad15,\quad19,\quad31.
$$

The grand mean is

$$
\bar y=19.
$$

Factor-A means:

$$
\bar y_{A_1}=13,
\qquad
\bar y_{A_2}=25.
$$

Factor-B means:

$$
\bar y_{B_1}=15,
\qquad
\bar y_{B_2}=23.
$$

### Sum-of-squares results

Using the Handbook factorial decomposition,

$$
\boxed{
SSA=288,
}
$$

$$
\boxed{
SSB=128,
}
$$

$$
\boxed{
SSAB=32,
}
$$

$$
\boxed{
SS_{\text{error}}=8.
}
$$

Thus

$$
SS_{\text{total}}
=
288+128+32+8
=
\boxed{456}.
$$

### Degrees of freedom

Here

$$
a=2,\qquad b=2,\qquad n=2.
$$

Therefore

$$
df_A=1,
$$

$$
df_B=1,
$$

$$
df_{AB}=1,
$$

$$
df_E=ab(n-1)=4,
$$

$$
df_{\text{total}}=8-1=7.
$$

### Mean squares and $F$

$$
MSA=288,
$$

$$
MSB=128,
$$

$$
MSAB=32,
$$

$$
MSE=\frac84=2.
$$

So

$$
\boxed{
F_A=144,
}
$$

$$
\boxed{
F_B=64,
}
$$

$$
\boxed{
F_{AB}=16.
}
$$

For numerator df 1 and denominator df 4, the 5% upper-tail Handbook critical
value is approximately

$$
F_{0.05,1,4}=7.71.
$$

All three constructed-example $F$ ratios exceed the critical value.

Thus the data provide evidence for:

- a Factor A effect,
- a Factor B effect,
- and an $AB$ interaction.

Because the interaction is significant, the main effects should not be described
without also examining how each factor behaves across the levels of the other.

![FIG-01-34-006: Complete two-factor ANOVA table for a 2x2 replicated example. Rows A, B, AB Interaction, Error, Total show df 1,1,1,4,7; SS 288,128,32,8,456; MS 288,128,32,2; F 144,64,16. Beside the table, the corresponding interaction plot uses cell means 11,15,19,31.](../figures/FIG-01-34-006-two-factor-anova-example.png)

### Worked Example 7 — Why Replication Matters

Suppose the same $2\times2$ experiment had only one observation in each cell.

Then

$$
n=1.
$$

The Handbook's replicated factorial error degrees of freedom would be

$$
ab(n-1)
=
(2)(2)(0)
=
\boxed{0}.
$$

Without replication, the standard replicated two-factor table has no independent
within-cell error estimate.

That means you cannot simply compute

$$
F_A,\quad F_B,\quad F_{AB}
$$

using the same error denominator as though replication existed.

Design determines what can be estimated.

---

## 34.7 Designing, Checking, and Interpreting an ANOVA

Before computing an ANOVA, ask whether the experimental design supports the
intended conclusion.

### One-way design

Use when:

- one factor is intentionally varied,
- treatments are compared,
- no explicit nuisance factor is being modeled.

### Randomized complete block design

Use when:

- one treatment factor is primary,
- one known nuisance factor can define blocks,
- each block can receive every treatment.

### Two-factor factorial design

Use when:

- two factors are of scientific or engineering interest,
- main effects matter,
- interaction may matter,
- combinations of factor levels can be run.

### Core assumptions used by the standard ANOVA model

The Handbook pages provide the ANOVA formulas and tables but do not develop a
full assumptions checklist. The following is the operational framework used in
this guide:

- experimental errors are independent,
- the error distribution within treatment combinations is adequately modeled for
  the intended $F$ inference,
- error variance is reasonably common across the compared groups,
- treatment assignment/randomization supports independence from nuisance trends,
- observations used as replicates are genuinely independent experimental units.

For classical small-sample ANOVA, normal-error assumptions underlie the exact
$F$ reference distribution.

### Residual thinking

A residual is conceptually

$$
\boxed{
e
=
\text{observed response}
-
\text{fitted response}.
}
$$

In one-way ANOVA, the fitted response is the treatment mean:

$$
e_{ij}
=
y_{ij}-\bar y_i.
$$

Residuals should not show obvious structure with:

- run order,
- fitted value,
- treatment,
- block,
- another known operating condition.

Structured residuals suggest that the statistical model has left explainable
behavior inside the "error" term.

![FIG-01-34-007: ANOVA design-selection and checking workflow. Start with experimental question. Branch to one factor -> one-way ANOVA; one treatment factor plus nuisance grouping -> randomized complete block; two factors of interest -> two-factor factorial. Then boxes for randomize, replicate, collect response, partition sums of squares, compute F ratios, compare with F critical values, inspect residual structure, and state limited conclusion. A warning says "significant global F does not identify which means differ."](../figures/FIG-01-34-007-anova-design-workflow.png)

### Worked Example 8 — Choose the Design

**Case A.** Compare four heat-treatment temperatures using independently prepared
specimens from one homogeneous batch.

Use:

$$
\boxed{\text{one-way design}.}
$$

**Case B.** Compare those same four temperatures, but specimens come from six
material lots known to differ.

If each lot can receive all four temperatures, use:

$$
\boxed{\text{randomized complete block design}}
$$

with lot as the block.

**Case C.** Study both temperature and cooling method because the effect of
temperature may depend on cooling method.

Use:

$$
\boxed{\text{two-factor factorial design}.}
$$

### Worked Example 9 — Interpret a Significant Global $F$

A one-way ANOVA comparing four treatments rejects

$$
H_0:
\mu_1=\mu_2=\mu_3=\mu_4.
$$

What may you conclude?

Correct:

> At least one population treatment mean differs from at least one other mean.

Not justified by the global test alone:

> Every pair of treatment means differs.

Also not justified:

> Treatment 4 is best.

The ANOVA $F$ test detects evidence against equality. It does not by itself rank
the treatments or identify each differing pair.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed p. 71 gives the one-way ANOVA
> decomposition. Printed p. 72 gives randomized complete block and two-factor
> factorial sum-of-squares formulas and the one-way ANOVA table. Printed p. 73
> gives the randomized complete block and two-way factorial ANOVA tables.
> Printed p. 79 provides upper-tail critical values of the $F$ distribution.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| One-Way Analysis of Variance (ANOVA) | 71 | Gives total, treatment, and error sum-of-squares decomposition |
| Randomized Complete Block Design | 72 | Gives total, treatment, block, and error decomposition |
| Two-Factor Factorial Designs | 72 | Gives Factor A, Factor B, interaction, error, and total sums of squares |
| One-Way ANOVA Table | 72 | Gives treatment/error/total df, mean squares, and $F=MST/MSE$ |
| Randomized Complete Block ANOVA Table | 73 | Gives treatment, block, error, total df and $F$ ratios |
| Two-Way Factorial ANOVA Table | 73 | Gives A, B, AB interaction, error, and total df plus $F$ ratios |
| Critical Values of the F Distribution | 79 | Gives upper-tail $F$ critical values by numerator and denominator df |

### Handbook structure to remember

For one-way ANOVA:

$$
SS_{\text{total}}
=
SS_{\text{treatments}}
+
SS_{\text{error}}.
$$

For a randomized complete block design:

$$
SS_{\text{total}}
=
SS_{\text{treatments}}
+
SS_{\text{blocks}}
+
SS_{\text{error}}.
$$

For a replicated two-factor factorial design:

$$
SS_{\text{total}}
=
SSA+SSB+SSAB+SS_{\text{error}}.
$$

Each source gets:

1. a sum of squares,
2. degrees of freedom,
3. a mean square where appropriate,
4. an $F$ ratio against $MSE$ where a test is defined.

### Guide-developed design interpretation

The supplied Handbook pages are formula- and table-focused. They do not provide
a complete narrative treatment of randomization, replication, experimental units,
ANOVA assumptions, residual diagnostics, or the limits of a significant global
$F$ test.

Those operational explanations are developed in this chapter so the Handbook
formulas are used in the correct experimental context.

The chapter does **not** introduce a specific multiple-comparison procedure
because none was located in the supplied ANOVA pages.

**Know without a lookup:**

- factor, level, treatment, response, experimental unit,
- replication, randomization, and blocking are different ideas,
- one-way ANOVA partitions treatment and error variation,
- $F$ is a mean-square ratio,
- large $F$ supports treatment differences,
- a global ANOVA rejection means "not all means are equal,"
- blocking separates a nuisance source from residual error,
- interaction means one factor's effect depends on another factor's level,
- and replicated factorial designs need an error estimate.

---

## Where This Goes Wrong

**Comparing sample means without considering within-group variation.** Means are
almost never exactly equal, even under equal population means.

**Using ANOVA to compare variances when the intended parameter is the mean.**
ANOVA uses variance decomposition to test mean structure.

**Confusing a factor with a response.** The factor is controlled or classified;
the response is measured.

**Calling repeated readings on one experimental unit independent replicates.**

**Skipping randomization because the design is balanced.** Balance does not
protect against run-order bias.

**Blocking on a variable that is actually the primary factor of interest.**

**Failing to include every treatment in every block of a complete-block design.**

**Putting block variation into the treatment sum of squares.**

**Using total degrees of freedom for a mean square denominator.**

**Computing $F=MS_{\text{error}}/MS_{\text{treatments}}$ in a one-way ANOVA.**
The Handbook table uses

$$
F=MST/MSE.
$$

**Using a lower-tail $F$ rejection region for the standard ANOVA ratio.**
Treatment differences make the numerator large, so the standard ANOVA rejection
region is in the upper tail.

**Concluding every treatment differs after a significant global ANOVA.**

**Concluding which treatment is best from the global $F$ statistic alone.**

**Ignoring block effects when a known nuisance source changes strongly across
runs.**

**Treating an interaction as just another main effect.** Interaction means the
effect of one factor changes with the other.

**Interpreting main effects without checking a strong interaction.**

**Running a replicated two-factor ANOVA formula with $n=1$ and pretending there
is an error mean square.**

**Assuming equal variance and normal-error behavior without checking whether the
experiment supports those assumptions.**

**Ignoring residual patterns.** A trend in residuals may indicate omitted
structure, drift, or nonconstant variability.

**Believing statistical significance guarantees engineering importance.** The
magnitude and consequence of treatment differences still matter.

---

## Key Terms

| Term | Definition |
|---|---|
| analysis of variance (ANOVA) | method that partitions variation and compares mean-square components |
| factor | controlled or classified experimental input |
| level | setting or category of a factor |
| treatment | experimental condition applied to an experimental unit |
| response | measured output of an experiment |
| experimental unit | smallest unit independently assigned to a treatment |
| replication | independent application of a treatment to multiple experimental units |
| randomization | random assignment or run-order procedure used to reduce systematic bias |
| block | group of similar experimental units defined by a nuisance source |
| nuisance factor | source of variation not central to the primary treatment question |
| sum of squares | measure of variation attributed to a source |
| treatment sum of squares | variation associated with treatment-mean differences |
| error sum of squares | residual within-model variation |
| mean square | sum of squares divided by its degrees of freedom |
| grand mean | mean across all observations |
| one-way ANOVA | ANOVA with one treatment factor |
| randomized complete block design | design in which every block receives every treatment |
| factorial design | design containing combinations of levels of multiple factors |
| main effect | average effect of one factor across levels of another |
| interaction | dependence of one factor's effect on the level of another factor |
| cell | one factor-level combination in a factorial design |
| residual | observed response minus fitted response |
| $F$ statistic | ratio of mean squares used for an ANOVA test |

---

## Review Questions

### Conceptual

1. Distinguish a factor, level, treatment, and response.
2. What is an experimental unit?
3. How does replication differ from repeated measurement?
4. What problem is randomization intended to reduce?
5. What problem is blocking intended to reduce?
6. State the one-way ANOVA null hypothesis for $k$ treatments.
7. What does a significant global one-way ANOVA establish?
8. Why is $MSE$ used as the denominator of the treatment $F$ ratio?
9. What is an interaction in a two-factor experiment?
10. Why is replication important in a replicated factorial ANOVA?

### Calculation

11. Three treatment groups have sizes 4, 5, and 6. Find $N$, treatment df, error df, and total df.
12. A one-way ANOVA has $SS_{\text{treatments}}=24$, $SS_{\text{error}}=18$, $k=3$, and $N=12$. Find $MST$ and $MSE$.
13. Using Question 12, find the $F$ statistic.
14. If $F_0=6.00$ and the 5% critical value is 4.26, state the ANOVA decision.
15. In a complete block design with $k=4$ treatments and $b=5$ blocks, find treatment, block, error, and total df.
16. A block design has $SS_{\text{total}}=90$, $SS_{\text{treatments}}=30$, and $SS_{\text{blocks}}=40$. Find $SS_{\text{error}}$.
17. A two-factor experiment has $a=3$, $b=2$, and $n=4$ repetitions per cell. Find df for A, B, AB, error, and total.
18. A factorial ANOVA has $MSA=18$ and $MSE=3$. Find $F_A$.
19. Cell means are 10 and 14 at $A_1$, and 20 and 32 at $A_2$. Find the B simple effect at each A level and the difference of differences.

### Multiple Choice

20. Which design principle deliberately changes run order to reduce systematic bias?
A) replication  B) randomization  C) blocking  D) interpolation.

21. In one-way ANOVA, $F$ is:
A) $MSE/MST$  B) $MST/MSE$  C) $SS_{\text{total}}/N$  D) $MST+MSE$.

22. One-way treatment df for $k$ treatments is:
A) $k$  B) $k+1$  C) $k-1$  D) $N-k$.

23. A significant global one-way ANOVA means:
A) every treatment pair differs  
B) at least one population mean differs from at least one other  
C) all variances are equal  
D) the largest sample mean is optimal.

24. A randomized complete block design adds which modeled source?
A) block variation  B) only interaction  C) regression slope  D) covariance only.

25. In a replicated two-factor design, interaction df are:
A) $ab$  B) $(a-1)(b-1)$  C) $ab(n-1)$  D) $a+b-2$.

26. If two interaction-plot lines are strongly nonparallel, this suggests:
A) no factor effects  
B) interaction  
C) zero error variance necessarily  
D) identical treatment means.

27. In a replicated two-factor design, error df are:
A) $ab(n-1)$  B) $abn-1$  C) $a-1$  D) $b-1$.

---

## Answer Key with Explanations

### Conceptual

1. A **factor** is an experimental input; a **level** is one setting of that
   factor; a **treatment** is the condition applied to an experimental unit; the
   **response** is the measured output. (§34.1)

2. It is the smallest unit that can independently receive a treatment assignment.
   (§34.1)

3. Replication applies the treatment independently to multiple experimental
   units. Repeated measurements may only remeasure the same unit and therefore
   need not provide independent experimental-error information. (§34.1)

4. Randomization reduces systematic alignment between treatments and uncontrolled
   run-order or assignment effects. (§34.1)

5. Blocking isolates a known nuisance source so its variation does not remain
   entirely inside the residual error term. (§34.1, §34.4)

6.

   $$
   \boxed{
   H_0:\mu_1=\mu_2=\cdots=\mu_k.
   }
   $$

   (§34.2)

7. It establishes evidence that the population treatment means are **not all
   equal**. It does not identify every differing pair. (§34.3)

8. $MSE$ estimates the residual or within-treatment variation against which the
   between-treatment mean-square variation is compared. (§34.3)

9. Interaction means the effect of one factor changes depending on the level of
   another factor. (§34.5)

10. Replication creates within-cell information and therefore an independent
    estimate of experimental error for the replicated factorial ANOVA table.
    (§34.6)

### Calculation

11.

    $$
    N=4+5+6=\boxed{15}.
    $$

    Treatment df:

    $$
    k-1=3-1=\boxed{2}.
    $$

    Error df:

    $$
    N-k=15-3=\boxed{12}.
    $$

    Total df:

    $$
    N-1=\boxed{14}.
    $$

12.

    $$
    MST
    =
    \frac{24}{3-1}
    =
    \boxed{12}.
    $$

    $$
    MSE
    =
    \frac{18}{12-3}
    =
    \frac{18}{9}
    =
    \boxed{2}.
    $$

13.

    $$
    F
    =
    \frac{12}{2}
    =
    \boxed{6}.
    $$

14. Since

    $$
    6.00>4.26,
    $$

    $$
    \boxed{\text{reject the equal-means null hypothesis}.}
    $$

15. Treatment df:

    $$
    4-1=\boxed{3}.
    $$

    Block df:

    $$
    5-1=\boxed{4}.
    $$

    Error df:

    $$
    (4-1)(5-1)
    =
    3(4)
    =
    \boxed{12}.
    $$

    Total df:

    $$
    4(5)-1
    =
    \boxed{19}.
    $$

16.

    $$
    SS_{\text{error}}
    =
    90-30-40
    =
    \boxed{20}.
    $$

17.

    $$
    df_A=a-1=2,
    $$

    $$
    df_B=b-1=1,
    $$

    $$
    df_{AB}=(a-1)(b-1)=2,
    $$

    $$
    df_E=ab(n-1)
    =(3)(2)(3)
    =
    18,
    $$

    $$
    df_{\text{total}}
    =abn-1
    =24-1
    =
    23.
    $$

    Therefore

    $$
    \boxed{2,\ 1,\ 2,\ 18,\ 23}.
    $$

18.

    $$
    F_A
    =
    \frac{18}{3}
    =
    \boxed{6}.
    $$

19. At $A_1$:

    $$
    14-10
    =
    \boxed{4}.
    $$

    At $A_2$:

    $$
    32-20
    =
    \boxed{12}.
    $$

    Difference of differences:

    $$
    12-4
    =
    \boxed{8}.
    $$

    The changing B effect suggests interaction.

### Multiple Choice

20. **B.** Randomization changes assignment/run order to reduce systematic bias.
    (§34.1)

21. **B.** The one-way ANOVA ratio is $MST/MSE$. (§34.3)

22. **C.** Treatment df are $k-1$. (§34.3)

23. **B.** A global rejection means not all population means are equal. (§34.3)

24. **A.** Blocking adds a modeled nuisance source. (§34.4)

25. **B.** Interaction df are $(a-1)(b-1)$. (§34.5)

26. **B.** Nonparallel response patterns are characteristic of interaction.
    (§34.5)

27. **A.** Replicated two-factor error df are $ab(n-1)$. (§34.5–34.6)

---

## Practice Problems

1. **Design vocabulary.** An engineer studies three lubricant types at two load
   levels and measures bearing temperature. Identify the factors, levels, and
   response.

2. **One-way sums of squares.** Three groups are:
   $$A:\ 4,5,6,$$
   $$B:\ 7,8,9,$$
   $$C:\ 5,6,7.$$
   Find the treatment means, grand mean, $SS_{\text{treatments}}$,
   $SS_{\text{error}}$, and $SS_{\text{total}}$.

3. **One-way ANOVA.** Use Problem 2 to construct the ANOVA df, mean squares, and
   $F$ statistic.

4. **One-way decision.** For Problem 3, use
   $$F_{0.05,2,6}=5.14.$$
   State the decision and the correct scope of the conclusion.

5. **Block degrees of freedom.** A complete block design has five treatments and
   six blocks. Find all ANOVA degrees of freedom.

6. **Block decomposition.** A block design has
   $$SS_{\text{total}}=140,$$
   $$SS_{\text{treatments}}=45,$$
   $$SS_{\text{blocks}}=65.$$
   Find $SS_{\text{error}}$.

7. **Interaction.** Cell means for a $2\times2$ experiment are:
   $$A_1B_1=20,\quad A_1B_2=26,$$
   $$A_2B_1=30,\quad A_2B_2=45.$$
   Find the effect of B at each A level and the difference of differences.

8. **Factorial degrees of freedom.** A design has
   $a=2$, $b=3$, and $n=5$ independent repetitions per cell.
   Find df for A, B, AB, error, and total.

9. **Factorial $F$ ratios.** A factorial ANOVA has
   $$MSA=24,\quad MSB=9,\quad MSAB=15,\quad MSE=3.$$
   Find $F_A$, $F_B$, and $F_{AB}$.

10. **Design selection.** Choose one-way ANOVA, randomized complete block, or
    two-factor factorial:
    (a) compare four adhesives;
    (b) compare four adhesives across seven known substrate lots, every lot
    receiving every adhesive;
    (c) study both adhesive type and cure temperature because their effects may
    interact.

---

## Practice Problem Solutions

1. Factors:

   - lubricant type: 3 levels,
   - load: 2 levels.

   Response:

   $$
   \boxed{\text{bearing temperature}.}
   $$

   This is naturally a two-factor factorial question if all lubricant-load
   combinations are studied.

2. Treatment means:

   $$
   \bar y_A=5,
   \qquad
   \bar y_B=8,
   \qquad
   \bar y_C=6.
   $$

   Grand mean:

   $$
   \bar y
   =
   \frac{15+24+18}{9}
   =
   \frac{57}{9}
   =
   \frac{19}{3}
   \approx6.3333.
   $$

   Treatment sum of squares:

   $$
   SS_{\text{treatments}}
   =
   3\left[
   \left(5-\frac{19}{3}\right)^2
   +
   \left(8-\frac{19}{3}\right)^2
   +
   \left(6-\frac{19}{3}\right)^2
   \right]
   $$

   $$
   =
   \boxed{14}.
   $$

   Within each group, squared deviations sum to 2:

   $$
   SS_{\text{error}}
   =
   2+2+2
   =
   \boxed{6}.
   $$

   Therefore

   $$
   SS_{\text{total}}
   =
   14+6
   =
   \boxed{20}.
   $$

3. Here

   $$
   k=3,\qquad N=9.
   $$

   Degrees of freedom:

   $$
   df_T=2,
   \qquad
   df_E=6,
   \qquad
   df_{\text{total}}=8.
   $$

   Mean squares:

   $$
   MST
   =
   \frac{14}{2}
   =
   7,
   $$

   $$
   MSE
   =
   \frac{6}{6}
   =
   1.
   $$

   Therefore

   $$
   \boxed{F=7}.
   $$

4. Since

   $$
   7>5.14,
   $$

   reject

   $$
   H_0:\mu_A=\mu_B=\mu_C.
   $$

   Correct conclusion:

   $$
   \boxed{\text{at least one population treatment mean differs}.}
   $$

   The global test alone does not identify every differing pair.

5. With

   $$
   k=5,\qquad b=6,
   $$

   treatment df:

   $$
   5-1=\boxed4.
   $$

   Block df:

   $$
   6-1=\boxed5.
   $$

   Error df:

   $$
   (5-1)(6-1)
   =
   4(5)
   =
   \boxed{20}.
   $$

   Total df:

   $$
   5(6)-1
   =
   \boxed{29}.
   $$

6.

   $$
   SS_{\text{error}}
   =
   140-45-65
   =
   \boxed{30}.
   $$

7. B effect at $A_1$:

   $$
   26-20
   =
   \boxed6.
   $$

   B effect at $A_2$:

   $$
   45-30
   =
   \boxed{15}.
   $$

   Difference of differences:

   $$
   15-6
   =
   \boxed9.
   $$

   The B effect changes strongly with A, indicating interaction.

8. With

   $$
   a=2,\qquad b=3,\qquad n=5,
   $$

   $$
   df_A=2-1=\boxed1,
   $$

   $$
   df_B=3-1=\boxed2,
   $$

   $$
   df_{AB}=(1)(2)=\boxed2,
   $$

   $$
   df_E=ab(n-1)
   =(2)(3)(4)
   =
   \boxed{24},
   $$

   $$
   df_{\text{total}}
   =abn-1
   =30-1
   =
   \boxed{29}.
   $$

9.

   $$
   F_A
   =
   \frac{24}{3}
   =
   \boxed8,
   $$

   $$
   F_B
   =
   \frac{9}{3}
   =
   \boxed3,
   $$

   $$
   F_{AB}
   =
   \frac{15}{3}
   =
   \boxed5.
   $$

10. **(a)** Four adhesives only:

    $$
    \boxed{\text{one-way ANOVA}.}
    $$

    **(b)** Four adhesives, substrate lot as known nuisance factor, every lot
    receiving every adhesive:

    $$
    \boxed{\text{randomized complete block design}.}
    $$

    **(c)** Adhesive type and cure temperature are both of interest and may
    interact:

    $$
    \boxed{\text{two-factor factorial design}.}
    $$

---

## Quick Reference

**One-way hypotheses**

$$
\boxed{
H_0:\mu_1=\mu_2=\cdots=\mu_k
}
$$

$$
\boxed{
H_1:\text{not all means are equal}.
}
$$

**One-way decomposition**

$$
\boxed{
SS_{\text{total}}
=
SS_{\text{treatments}}
+
SS_{\text{error}}
}
$$

$$
SS_{\text{treatments}}
=
\sum_i
n_i(\bar y_i-\bar y)^2
$$

$$
SS_{\text{error}}
=
\sum_i\sum_j
(y_{ij}-\bar y_i)^2
$$

**One-way df**

$$
df_T=k-1
$$

$$
df_E=N-k
$$

$$
df_{\text{total}}=N-1.
$$

**One-way mean squares**

$$
\boxed{
MST
=
\frac{SS_{\text{treatments}}}{k-1}
}
$$

$$
\boxed{
MSE
=
\frac{SS_{\text{error}}}{N-k}
}
$$

**One-way test**

$$
\boxed{
F=\frac{MST}{MSE}
}
$$

Large upper-tail $F$ → evidence against equal means.

**Randomized complete block decomposition**

$$
\boxed{
SS_{\text{total}}
=
SS_{\text{treatments}}
+
SS_{\text{blocks}}
+
SS_{\text{error}}
}
$$

df:

$$
k-1,\qquad b-1,\qquad(k-1)(b-1),\qquad kb-1.
$$

**Two-factor replicated decomposition**

$$
\boxed{
SS_{\text{total}}
=
SSA+SSB+SSAB+SS_{\text{error}}
}
$$

df:

$$
a-1,
\qquad
b-1,
\qquad
(a-1)(b-1),
$$

$$
ab(n-1),
\qquad
abn-1.
$$

Tests:

$$
\boxed{
F_A=\frac{MSA}{MSE},
\quad
F_B=\frac{MSB}{MSE},
\quad
F_{AB}=\frac{MSAB}{MSE}.
}
$$

**Design principles**

randomization → reduce systematic assignment/run-order bias  
replication → estimate experimental variation  
blocking → remove known nuisance variation from error  
factorial design → estimate main effects and interaction.

---

## What's Next

ANOVA compares structured groups.

The next statistical tool replaces group labels with a quantitative predictor and
asks whether a mathematical relationship can explain the response.

**Chapter 01-35 — Linear Regression and Goodness of Fit** will develop:

- the least-squares line,
- slope and intercept,
- fitted values and residuals,
- sums of squares used in regression,
- standard error of estimate,
- correlation coefficient,
- coefficient of determination,
- confidence intervals for slope and intercept,
- and the distinction between association and causation.

The FE Reference Handbook develops *Linear Regression and Goodness of Fit* on
printed pp. 70–71, immediately before the ANOVA material used in this chapter.

Carry one idea forward:

> ANOVA explains variation using group structure. Regression explains variation
> using a quantitative relationship.

— Your Mentor
