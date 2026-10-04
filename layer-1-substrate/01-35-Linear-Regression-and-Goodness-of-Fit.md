---
chapter: "01-35"
title: "Linear Regression and Goodness of Fit"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-035-01, MATH-1D-035-02, MATH-1D-035-03, MATH-1D-035-04, MATH-1D-035-05, MATH-1D-035-06, MATH-1D-035-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-35: Linear Regression and Goodness of Fit

> *"A fitted line is not evidence merely because it can be drawn. Regression is
> useful when the line summarizes a relationship, the residuals behave as the
> model expects, and the interpretation stays inside what the data support."*

---

## Before You Start

**Prerequisites:** [01-04 Expressions, Equations, and Inequalities](01-04-Expressions-Equations-and-Inequalities.md) ·
[01-29 Random Variables and Probability Distributions](01-29-Random-Variables-and-Probability-Distributions.md) ·
[01-32 Estimation and Confidence Intervals](01-32-Estimation-and-Confidence-Intervals.md) ·
[01-33 Hypothesis Testing and Statistical Decisions](01-33-Hypothesis-Testing-and-Statistical-Decisions.md)

**Skip if:** You can compute a least-squares line from $S_{xx}$ and $S_{xy}$;
interpret slope and intercept with units; calculate fitted values and residuals;
compute the residual sum of squares and standard error of estimate; calculate and
interpret the sample correlation coefficient $R$ and coefficient of determination
$R^2$; construct confidence intervals for slope and intercept; distinguish
interpolation from extrapolation; identify common residual-pattern warnings; and
explain why correlation does not establish causation.

**Time:** About 105–125 min reading and worked examples · 40–50 min review
questions · 65–85 min practice problems.

**Working convention:** The response variable is plotted vertically and the
predictor horizontally. A fitted value is denoted $\hat y$. A residual is always

$$
\boxed{
e_i=y_i-\hat y_i.
}
$$

Keep that sign convention consistent.

---

## On the Board Today

ANOVA compared groups.

Regression replaces group labels with a quantitative predictor.

Instead of asking

> Do treatment means differ?

we ask

> How does the expected response change as the predictor changes?

The simplest model is a straight line:

$$
\boxed{
\hat y=\hat a+\hat b x.
}
$$

The slope $\hat b$ tells you how much fitted response changes per unit change in
$x$.

The intercept $\hat a$ tells you the fitted response at

$$
x=0.
$$

But a regression line is not chosen by eye.

Least squares selects the line that minimizes the total squared vertical
residuals:

$$
\boxed{
\sum_{i=1}^{n}(y_i-\hat y_i)^2.
}
$$

Once the line is fitted, the work is not over.

You still need to ask:

- How large are the residuals?
- How much of the observed response variation does the line explain?
- Is the relationship actually close to linear?
- Does the scatter change across the predictor range?
- Are you interpolating or extrapolating?
- Does the physical context support a causal interpretation?

Those questions separate a calculation from a usable regression analysis.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **35.1** Define predictor, response, fitted value, residual, slope, and intercept
* **35.2** Explain the least-squares criterion geometrically and algebraically
* **35.3** Compute $S_{xx}$, $S_{yy}$, and $S_{xy}$
* **35.4** Calculate the least-squares slope and intercept
* **35.5** Calculate fitted values, residuals, residual sum of squares, and standard error of estimate
* **35.6** Interpret the units and physical meaning of regression coefficients
* **35.7** Compute and interpret the sample correlation coefficient $R$
* **35.8** Compute and interpret the coefficient of determination $R^2$
* **35.9** Construct confidence intervals for the fitted slope and intercept
* **35.10** Distinguish interpolation from extrapolation
* **35.11** Use residual behavior to identify curvature, nonconstant spread, and other model warnings
* **35.12** Distinguish statistical association from causal evidence and recognize the limits of simple linear regression

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $x_i$ | predictor value for observation $i$ | horizontal-axis variable |
| $y_i$ | observed response for observation $i$ | vertical-axis variable |
| $\bar x,\bar y$ | sample means | centers of the observed data |
| $\hat y_i$ | fitted response at $x_i$ | value on fitted line |
| $\hat a$ | fitted intercept | predicted $y$ at $x=0$ |
| $\hat b$ | fitted slope | change in fitted $y$ per unit $x$ |
| $e_i$ | residual | $y_i-\hat y_i$ |
| $S_{xx}$ | predictor corrected sum of squares | $\sum(x_i-\bar x)^2$ |
| $S_{yy}$ | response corrected sum of squares | $\sum(y_i-\bar y)^2$ |
| $S_{xy}$ | corrected cross-product sum | $\sum(x_i-\bar x)(y_i-\bar y)$ |
| $SSE$ | residual/error sum of squares | $\sum e_i^2$ |
| $MSE$ | residual mean square | $SSE/(n-2)$ for simple linear regression |
| $S_e$ | standard error of estimate | $\sqrt{MSE}$ |
| $R$ | sample correlation coefficient | between $-1$ and $+1$ |
| $R^2$ | coefficient of determination | fraction of sample response variation explained by the fitted line |
| $\nu$ | residual degrees of freedom | $n-2$ in simple linear regression |

**Notation note.** The FE Reference Handbook writes the fitted regression line,
residual, standard error of estimate, correlation coefficient, coefficient of
determination, and confidence intervals for slope and intercept in its
*Linear Regression and Goodness of Fit* section on printed pp. 70–71.

---

## 35.1 The Regression Model and Least Squares

For paired observations

$$
(x_1,y_1),\ldots,(x_n,y_n),
$$

simple linear regression fits

$$
\boxed{
\hat y=\hat a+\hat b x.
}
$$

### Predictor and response

The **predictor** $x$ is the variable used to explain or predict changes in the
response.

The **response** $y$ is the measured outcome.

The distinction matters because ordinary least squares minimizes **vertical**
residuals in $y$.

Swapping $x$ and $y$ generally produces a different fitted line.

### Fitted value

At predictor value $x_i$,

$$
\boxed{
\hat y_i=\hat a+\hat b x_i.
}
$$

### Residual

The residual is

$$
\boxed{
e_i=y_i-\hat y_i.
}
$$

A positive residual means the observed response lies above the fitted line.

A negative residual means it lies below.

### Least-squares criterion

The least-squares line minimizes

$$
\boxed{
SSE
=
\sum_{i=1}^{n}
e_i^2
=
\sum_{i=1}^{n}
(y_i-\hat a-\hat b x_i)^2.
}
$$

Squaring prevents positive and negative residuals from canceling and penalizes
larger deviations more strongly.

![FIG-01-35-001: Scatterplot with a fitted straight line. Several observations have vertical segments drawn to the line and labeled residual e_i = y_i - y-hat_i. Positive residuals extend upward from the line to a point; negative residuals extend downward. A formula box states least squares chooses a-hat and b-hat to minimize sum e_i^2.](../figures/FIG-01-35-001-least-squares-residuals.png)

### Worked Example 1 — Interpret Slope Units Before Fitting

Suppose:

- $x=$ curing temperature in °C,
- $y=$ tensile strength in MPa.

A fitted slope of

$$
\hat b=1.8\ \frac{\text{MPa}}{^\circ\text{C}}
$$

means:

> Within the modeled data range, the fitted mean tensile strength increases by
> about 1.8 MPa for each 1 °C increase in curing temperature.

The slope units are

$$
\boxed{
\frac{\text{response units}}
{\text{predictor units}}.
}
$$

The statement does not automatically prove that temperature **causes** the
increase. That conclusion depends on design and context.

---

## 35.2 Computing the Least-Squares Line

The Handbook defines the corrected sums

$$
\boxed{
S_{xx}
=
\sum_{i=1}^{n}
(x_i-\bar x)^2
}
$$

$$
\boxed{
S_{yy}
=
\sum_{i=1}^{n}
(y_i-\bar y)^2
}
$$

and

$$
\boxed{
S_{xy}
=
\sum_{i=1}^{n}
(x_i-\bar x)(y_i-\bar y).
}
$$

Equivalent computational forms are

$$
S_{xx}
=
\sum x_i^2
-
\frac{(\sum x_i)^2}{n},
$$

$$
S_{yy}
=
\sum y_i^2
-
\frac{(\sum y_i)^2}{n},
$$

$$
S_{xy}
=
\sum x_i y_i
-
\frac{(\sum x_i)(\sum y_i)}{n}.
$$

The fitted slope is

$$
\boxed{
\hat b
=
\frac{S_{xy}}{S_{xx}}.
}
$$

The fitted intercept is

$$
\boxed{
\hat a
=
\bar y-\hat b\bar x.
}
$$

Therefore the least-squares line always passes through

$$
\boxed{
(\bar x,\bar y).
}
$$

![FIG-01-35-002: Regression computation flow diagram. Raw paired data feed sample means x-bar and y-bar, then corrected sums Sxx, Syy, Sxy. Sxy/Sxx produces slope b-hat; y-bar - b-hat x-bar produces intercept a-hat. The final fitted line y-hat=a-hat+b-hat x is shown passing through the point (x-bar,y-bar).](../figures/FIG-01-35-002-regression-computation-flow.png)

### Worked Example 2 — Fit a Least-Squares Line

Use the data:

| $x$ | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|
| $y$ | 2 | 3 | 5 | 4 | 6 |

Means:

$$
\bar x=3,
\qquad
\bar y=4.
$$

Corrected predictor sum:

$$
S_{xx}
=
(-2)^2+(-1)^2+0^2+1^2+2^2
=
10.
$$

Corrected response sum:

$$
S_{yy}
=
(-2)^2+(-1)^2+1^2+0^2+2^2
=
10.
$$

Cross-product sum:

$$
S_{xy}
=
(-2)(-2)+(-1)(-1)+(0)(1)+(1)(0)+(2)(2)
$$

$$
=
4+1+0+0+4
=
9.
$$

Slope:

$$
\hat b
=
\frac9{10}
=
\boxed{0.9}.
$$

Intercept:

$$
\hat a
=
4-(0.9)(3)
=
\boxed{1.3}.
$$

Therefore

$$
\boxed{
\hat y=1.3+0.9x.
}
$$

**Check.**

At

$$
x=\bar x=3,
$$

the fitted response is

$$
\hat y
=
1.3+0.9(3)
=
4
=
\bar y.
$$

The line passes through the data centroid as required.

---

## 35.3 Fitted Values, Residuals, and Standard Error of Estimate

Once the line is known, compute

$$
\hat y_i
=
\hat a+\hat b x_i
$$

and

$$
e_i
=
y_i-\hat y_i.
$$

For a least-squares line with intercept, two useful checks are

$$
\boxed{
\sum e_i\approx0
}
$$

and

$$
\boxed{
\sum x_i e_i\approx0.
}
$$

Small differences from zero may appear from rounding.

### Residual sum of squares

The residual sum of squares is

$$
\boxed{
SSE
=
\sum e_i^2.
}
$$

For simple linear regression,

$$
\boxed{
SSE
=
S_{yy}
-
\frac{S_{xy}^2}{S_{xx}}.
}
$$

### Why $n-2$ degrees of freedom?

Two parameters were estimated from the same data:

- intercept,
- slope.

Therefore residual degrees of freedom are

$$
\boxed{
\nu=n-2.
}
$$

Residual mean square:

$$
\boxed{
MSE
=
\frac{SSE}{n-2}.
}
$$

The **standard error of estimate** is

$$
\boxed{
S_e
=
\sqrt{MSE}
=
\sqrt{\frac{SSE}{n-2}}.
}
$$

It has the same units as the response $y$.

![FIG-01-35-003: Table linking observed y_i, fitted y-hat_i, residual e_i, and squared residual e_i^2 for several points. Arrows show the squared residuals summing to SSE, then division by n-2 to form MSE, then square root to form S_e. A unit callout says S_e has the response variable's units.](../figures/FIG-01-35-003-residual-standard-error.png)

### Worked Example 3 — Residual Table and $S_e$

Continue the fitted line

$$
\hat y=1.3+0.9x.
$$

| $x_i$ | $y_i$ | $\hat y_i$ | $e_i=y_i-\hat y_i$ | $e_i^2$ |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2.2 | -0.2 | 0.04 |
| 2 | 3 | 3.1 | -0.1 | 0.01 |
| 3 | 5 | 4.0 | 1.0 | 1.00 |
| 4 | 4 | 4.9 | -0.9 | 0.81 |
| 5 | 6 | 5.8 | 0.2 | 0.04 |

Residual sum:

$$
-0.2-0.1+1.0-0.9+0.2
=
\boxed{0}.
$$

Residual sum of squares:

$$
SSE
=
0.04+0.01+1.00+0.81+0.04
=
\boxed{1.90}.
$$

Check from corrected sums:

$$
SSE
=
10-\frac{9^2}{10}
=
10-8.1
=
1.9.
$$

Residual degrees of freedom:

$$
n-2=3.
$$

Mean square:

$$
MSE
=
\frac{1.9}{3}
=
0.63333.
$$

Standard error:

$$
S_e
=
\sqrt{0.63333}
\approx
\boxed{0.7958}.
$$

**Interpretation.** Residual scatter around the line is on the order of
0.8 response units.

---

## 35.4 Correlation and Coefficient of Determination

The Handbook gives the sample correlation coefficient

$$
\boxed{
R
=
\frac{S_{xy}}
{\sqrt{S_{xx}S_{yy}}}.
}
$$

Its range is

$$
\boxed{
-1\le R\le1.
}
$$

### Sign

- $R>0$: increasing linear association,
- $R<0$: decreasing linear association,
- $R=0$: no **linear** association in the sample.

A value near zero does not prove there is no relationship. A strong curved
relationship can have small linear correlation.

### Magnitude

Values closer to

$$
|R|=1
$$

indicate points lying more tightly around a straight-line pattern.

### Coefficient of determination

For simple linear regression with an intercept,

$$
\boxed{
R^2
=
\frac{S_{xy}^2}
{S_{xx}S_{yy}}.
}
$$

Equivalent:

$$
\boxed{
R^2
=
1-\frac{SSE}{S_{yy}}.
}
$$

Interpretation:

> $R^2$ is the fraction of the observed sample variation in $y$ accounted for by
> the fitted linear relationship with $x$.

It is not the percentage of individual observations predicted correctly.

It is not proof of causation.

![FIG-01-35-004: Four scatterplots with labels: strong positive linear R near +1, strong negative linear R near -1, weak linear R near 0, and strong curved relationship with small linear R. A side formula panel shows R=Sxy/sqrt(Sxx Syy) and R²=1-SSE/Syy.](../figures/FIG-01-35-004-correlation-r-squared.png)

### Worked Example 4 — Compute $R$ and $R^2$

For the five-point example,

$$
S_{xx}=10,
\qquad
S_{yy}=10,
\qquad
S_{xy}=9.
$$

Therefore

$$
R
=
\frac9{\sqrt{(10)(10)}}
=
\boxed{0.90}.
$$

Then

$$
R^2
=
(0.90)^2
=
\boxed{0.81}.
$$

Check using residual variation:

$$
1-\frac{SSE}{S_{yy}}
=
1-\frac{1.9}{10}
=
0.81.
$$

**Interpretation.** In this sample, 81% of the observed variation in $y$ about
its sample mean is accounted for by the fitted straight-line relationship with
$x$.

### $R^2$ is not enough

Two models can have similar $R^2$ but very different residual patterns.

A high $R^2$ does not rescue:

- severe curvature,
- one influential point,
- nonconstant residual spread,
- extrapolation beyond the data,
- or a physically meaningless model.

Goodness of fit requires more than one number.

---

## 35.5 Confidence Intervals for Slope and Intercept

The supplied Handbook provides confidence intervals for both the fitted intercept
and fitted slope on printed p. 71.

For simple linear regression, residual degrees of freedom are

$$
\boxed{
\nu=n-2.
}
$$

### Slope standard error

The fitted slope has estimated standard error

$$
\boxed{
SE_{\hat b}
=
\frac{S_e}{\sqrt{S_{xx}}}.
}
$$

A two-sided

$$
100(1-\alpha)\%
$$

confidence interval is

$$
\boxed{
\hat b
\pm
t_{\alpha/2,n-2}
\frac{S_e}{\sqrt{S_{xx}}}.
}
$$

### Intercept standard error

The fitted intercept has estimated standard error

$$
\boxed{
SE_{\hat a}
=
S_e
\sqrt{
\frac1n
+
\frac{\bar x^2}{S_{xx}}
}.
}
$$

A two-sided interval is

$$
\boxed{
\hat a
\pm
t_{\alpha/2,n-2}
S_e
\sqrt{
\frac1n
+
\frac{\bar x^2}{S_{xx}}
}.
}
$$

The intercept may be estimated imprecisely when

$$
x=0
$$

is far from the observed predictor range.

That is one reason to avoid attaching physical meaning to the intercept
automatically.

![FIG-01-35-005: Regression line with a confidence concept overlay. A slope triangle identifies b-hat. Beside it, formula boxes show SE_b = S_e/sqrt(Sxx) and SE_a = S_e sqrt(1/n + x-bar^2/Sxx), each multiplied by t_(alpha/2,n-2) for a confidence interval. A note warns that an intercept at x=0 may be far outside the observed x range.](../figures/FIG-01-35-005-slope-intercept-confidence.png)

### Worked Example 5 — Confidence Interval for the Slope

Continue the example:

$$
\hat b=0.9,
\qquad
S_e\approx0.7958,
\qquad
S_{xx}=10,
\qquad
n=5.
$$

Degrees of freedom:

$$
\nu=5-2=3.
$$

For 95% confidence,

$$
t_{0.025,3}\approx3.182.
$$

Slope standard error:

$$
SE_{\hat b}
=
\frac{0.7958}{\sqrt{10}}
\approx
0.2517.
$$

Margin:

$$
3.182(0.2517)
\approx
0.8008.
$$

So

$$
\boxed{
0.099
<
b
<
1.701
}
$$

approximately.

The interval is wide because the sample contains only five observations.

### Worked Example 6 — Confidence Interval for the Intercept

For the same data,

$$
\hat a=1.3,
\qquad
\bar x=3.
$$

Intercept standard error:

$$
SE_{\hat a}
=
0.7958
\sqrt{
\frac15+\frac{3^2}{10}
}
$$

$$
=
0.7958\sqrt{1.1}
\approx
0.8347.
$$

Margin:

$$
3.182(0.8347)
\approx
2.656.
$$

Therefore

$$
\boxed{
-1.356
<
a
<
3.956
}
$$

approximately.

**Interpretation.** The intercept is substantially less precise than the slope in
this small example. Also, the observed predictor range is 1 through 5, so
$x=0$ lies outside the data range.

---

## 35.6 Interpolation, Extrapolation, and Residual Checks

Regression is often used for prediction, but the location of the requested
predictor matters.

### Interpolation

**Interpolation** predicts inside the observed predictor range.

If data were collected for

$$
1\le x\le5,
$$

then predicting at

$$
x=3.5
$$

is interpolation.

The fitted line gives

$$
\hat y
=
1.3+0.9(3.5)
=
\boxed{4.45}.
$$

### Extrapolation

**Extrapolation** predicts outside the observed predictor range.

At

$$
x=8,
$$

the same formula gives

$$
\hat y
=
1.3+0.9(8)
=
8.5.
$$

The arithmetic is valid.

The inference may not be.

The physical relationship may bend, saturate, change mechanism, or cease to
exist outside the range used to fit the line.

### Residual plots

A useful linear-model residual plot should look approximately like unstructured
scatter around zero.

Warning patterns include:

**Curvature**

Residuals systematically positive in one region and negative in another suggest
that a straight line misses a curved relationship.

**Funnel shape**

Residual spread increasing or decreasing with fitted value suggests
nonconstant variance.

**Run-order trend**

Residual drift with experimental order suggests time dependence, warm-up,
wear, ambient change, or another omitted condition.

**Extreme point**

A single unusual predictor-response combination may strongly influence slope and
correlation.

![FIG-01-35-006: Four residual plots. Panel 1 shows random scatter around zero labeled acceptable linear pattern. Panel 2 shows a U-shaped curve labeled curvature. Panel 3 shows a widening funnel labeled nonconstant variance. Panel 4 shows a monotonic run-order trend labeled drift/dependence. All plots share a horizontal zero-residual line.](../figures/FIG-01-35-006-residual-patterns.png)

### Worked Example 7 — A High $R^2$ Can Still Need Investigation

Suppose a regression reports

$$
R^2=0.94,
$$

but residuals form a clear U-shaped pattern.

Conclusion:

- the model accounts for a large fraction of sample variation,
- but the residual pattern shows systematic curvature left unexplained,
- therefore a straight-line model is structurally incomplete.

Do not write:

> The linear model is excellent because $R^2=0.94$.

A goodness-of-fit metric and a diagnostic plot answer different questions.

### Worked Example 8 — Extrapolation Warning

For

$$
\hat y=1.3+0.9x,
$$

the observed range is

$$
1\le x\le5.
$$

Prediction at

$$
x=4.5
$$

is interpolation:

$$
\hat y=5.35.
$$

Prediction at

$$
x=10
$$

is extrapolation:

$$
\hat y=10.3.
$$

The second number should be labeled as extrapolated and should not be treated as
equally supported by the data.

---

## 35.7 Association, Causation, Curve Fitting, and Model Scope

A regression model describes association between variables in the observed data.

It does not automatically establish cause and effect.

### Correlation is not causation

A strong relationship may arise because:

- $x$ causes changes in $y$,
- $y$ affects $x$,
- a third variable affects both,
- the data were selected in a biased way,
- both variables trend with time,
- or the association is coincidental.

Causal interpretation is much stronger when treatment assignment is controlled
and randomized, as in a designed experiment.

That connection is why Chapter 01-34 matters.

### Curve fitting

A straight line is one model.

If residuals show curvature, possible responses include:

- use a physically justified transformation,
- fit a different model,
- restrict the linear model to a range where it is adequate.

Examples sometimes linearized by transformation include relationships of the
form

$$
y=Ae^{bx}
$$

or

$$
y=Ax^b.
$$

Taking logarithms can produce a linear relationship in transformed variables:

$$
\ln y
=
\ln A+bx
$$

or

$$
\ln y
=
\ln A+b\ln x.
$$

These transformations change the error structure and interpretation. They should
not be applied solely to force a large $R^2$.

### Multiple regression

Some FE discipline specifications mention **multiple regression**. The simple
least-squares formulas printed on Handbook pp. 70–71 are for one predictor.

A multiple linear model has the conceptual form

$$
\boxed{
\hat y
=
\hat\beta_0
+
\hat\beta_1x_1
+
\hat\beta_2x_2
+\cdots+
\hat\beta_px_p.
}
$$

Each coefficient describes an adjusted linear contribution while the other
predictors are held fixed in the model.

The supplied Handbook regression pages do not provide a full matrix-development
procedure for estimating a general multiple-regression model, so this chapter
does not invent a Handbook formula that is not there.

The key transferable ideas remain:

- fitted values,
- residuals,
- sums of squared error,
- coefficient interpretation,
- uncertainty,
- residual diagnostics,
- and avoiding causal claims without design support.

![FIG-01-35-007: Model-scope diagram. Left: observational scatter with a strong trend but a hidden third-variable arrow, captioned "association does not prove causation." Center: randomized designed experiment with controlled x leading more credibly to causal interpretation. Right: three model forms—a straight line, a curved raw relationship that becomes straight after a justified transformation, and a conceptual multiple-regression plane with x1 and x2 predicting y.](../figures/FIG-01-35-007-association-causation-model-scope.png)

### Worked Example 9 — What Can the Regression Claim?

An observational dataset shows

$$
R=0.93
$$

between equipment age and annual maintenance cost.

Appropriate conclusion:

> The sample shows a strong positive linear association between equipment age and
> annual maintenance cost.

Not established by correlation alone:

> Increasing age by one year causes the exact fitted increase in maintenance
> cost.

Possible confounding variables include:

- duty cycle,
- equipment type,
- operating environment,
- maintenance policy.

Regression quantifies association. Experimental design and subject-matter
evidence support causal interpretation.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. The section *Linear Regression and
> Goodness of Fit* begins on printed p. 70 and continues onto printed p. 71.
> The Handbook index also identifies least squares and regression on p. 70,
> residuals on p. 70, and confidence intervals plus the sample correlation
> coefficient and coefficient of determination on p. 71.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Least Squares | 70 | Gives the fitted line, slope, intercept, and corrected-sum formulas |
| $S_{xx}$, $S_{yy}$, $S_{xy}$ | 70 | Defines centered sums/cross-products and equivalent computational forms |
| Residual | 70 | Defines observed minus fitted response |
| Standard Error of Estimate | 70 | Gives the regression residual-error measure / MSE structure |
| Confidence Interval for Intercept | 71 | Provides an interval for the fitted intercept |
| Confidence Interval for Slope | 71 | Provides an interval for the fitted slope |
| Sample Correlation Coefficient | 71 | Provides $R$ |
| Coefficient of Determination | 71 | Provides $R^2$ |

### Core Handbook relationships used here

Least-squares line:

$$
\boxed{
\hat y=\hat a+\hat b x
}
$$

Slope:

$$
\boxed{
\hat b=\frac{S_{xy}}{S_{xx}}
}
$$

Intercept:

$$
\boxed{
\hat a=\bar y-\hat b\bar x
}
$$

Residual:

$$
\boxed{
e_i=y_i-\hat y_i
}
$$

Sample correlation:

$$
\boxed{
R
=
\frac{S_{xy}}
{\sqrt{S_{xx}S_{yy}}}
}
$$

and for simple linear regression with an intercept,

$$
\boxed{
R^2
=
\frac{S_{xy}^2}
{S_{xx}S_{yy}}.
}
$$

### Material developed in this guide

The supplied Handbook pages are compact formula references. The following
interpretive material is developed here to make those formulas usable:

- the geometric least-squares explanation,
- interpolation versus extrapolation,
- residual-pattern diagnosis,
- the warning that a high $R^2$ does not by itself validate a model,
- the distinction between association and causation,
- and the conceptual extension to multiple regression and transformed curve
  fitting.

The Handbook supports confidence intervals for slope and intercept; the guide
writes them explicitly in the familiar simple-regression standard-error form and
uses residual degrees of freedom $n-2$.

**Know without a lookup:**

- residual $=$ observed minus fitted,
- slope units are response units per predictor unit,
- $\hat b=S_{xy}/S_{xx}$,
- $\hat a=\bar y-\hat b\bar x$,
- the fitted line passes through $(\bar x,\bar y)$,
- $R$ measures linear association,
- $R^2$ measures explained sample variation in the simple linear model,
- extrapolation is less supported than interpolation,
- and correlation alone does not establish causation.

---

## Where This Goes Wrong

**Swapping predictor and response without realizing the regression changes.**

**Minimizing horizontal distance instead of vertical response residuals.**
Ordinary least squares here minimizes squared $y$ residuals.

**Using $S_{yy}$ in the slope denominator.**

$$
\hat b
=
S_{xy}/S_{xx},
$$

not $S_{xy}/S_{yy}$.

**Forgetting the intercept formula after finding slope.**

**Giving the slope no units.** Regression coefficients carry physical units.

**Interpreting the intercept physically when $x=0$ is outside the observed or
meaningful range.**

**Defining residual as fitted minus observed.** This chapter and the Handbook
use observed minus fitted.

**Using $n-1$ residual degrees of freedom.** Simple linear regression estimates
two parameters, so residual df are $n-2$.

**Calling $S_e^2$ the standard error.** $S_e$ is the square root and has response
units.

**Assuming $R=0$ means no relationship of any kind.** It means no sample linear
association as measured by correlation.

**Assuming a large $|R|$ proves causation.**

**Interpreting $R^2=0.81$ as "81% of predictions are correct."**

**Using $R^2$ without looking at residual behavior.**

**Ignoring curvature because the fitted slope is statistically significant.**

**Ignoring nonconstant residual spread.**

**Using a fitted line far outside the observed predictor range without warning.**

**Forcing a transformation solely to improve $R^2$.**

**Treating repeated observations at nearly identical predictor settings as though
they necessarily cover a broad predictive range.**

**Reporting excessive digits in fitted coefficients.** Coefficients should be
reported at a precision justified by the data.

**Treating an observational regression as a controlled experiment.**

---

## Key Terms

| Term | Definition |
|---|---|
| regression | method for modeling response behavior as a function of predictor information |
| simple linear regression | regression with one predictor and a straight-line mean model |
| predictor | input/explanatory variable denoted $x$ |
| response | measured outcome denoted $y$ |
| fitted line | estimated relation $\hat y=\hat a+\hat b x$ |
| fitted value | predicted response $\hat y_i$ at an observed predictor value |
| slope | fitted response change per unit predictor change |
| intercept | fitted response at $x=0$ |
| residual | observed response minus fitted response |
| least squares | criterion that minimizes the sum of squared residuals |
| residual sum of squares | $SSE=\sum e_i^2$ |
| residual mean square | $MSE=SSE/(n-2)$ in simple linear regression |
| standard error of estimate | residual scale $S_e=\sqrt{MSE}$ |
| corrected sum of squares | centered variation measure such as $S_{xx}$ or $S_{yy}$ |
| corrected cross-product | $S_{xy}$ |
| correlation coefficient | standardized measure $R$ of sample linear association |
| coefficient of determination | $R^2$, proportion of sample response variation explained by the simple fitted line |
| interpolation | prediction inside the observed predictor range |
| extrapolation | prediction outside the observed predictor range |
| residual plot | diagnostic plot of residuals against fitted value, predictor, or run order |
| confounding | mixing of predictor association with another influential variable |
| multiple regression | linear model with more than one predictor |
| curve fitting | fitting a model whose form may be nonlinear in the original variables |

---

## Review Questions

### Conceptual

1. Distinguish predictor and response variables.
2. What quantity does ordinary least squares minimize in this chapter?
3. What does a positive residual mean geometrically?
4. Why does the fitted least-squares line pass through $(\bar x,\bar y)$?
5. What are the units of a regression slope?
6. What does $S_e$ measure?
7. What does the sign of $R$ indicate?
8. What does $R^2$ measure in simple linear regression with an intercept?
9. Why can a high $R^2$ coexist with a poor linear model?
10. Why does strong correlation not establish causation?

### Calculation

11. For $x=1,2,3$ and $y=2,4,6$, find $\bar x$ and $\bar y$.
12. Using Question 11, find $S_{xx}$ and $S_{xy}$.
13. Using Questions 11–12, find $\hat b$ and $\hat a$.
14. For $\hat y=1+2x$, find $\hat y$ at $x=3.5$.
15. If observed $y=9$ and fitted $\hat y=8.4$, find the residual.
16. If $S_{yy}=20$ and $SSE=5$, find $R^2$.
17. If $S_{xx}=16$, $S_{yy}=25$, and $S_{xy}=-12$, find $R$.
18. A regression has $SSE=24$ and $n=8$. Find $MSE$ and $S_e$.
19. A regression has $\hat b=3.0$, $S_e=2.0$, $S_{xx}=25$, and $n=12$. Using $t_{0.025,10}=2.228$, find a 95% confidence interval for the slope.

### Multiple Choice

20. A residual is:
A) $\hat y-y$  
B) $y-\hat y$  
C) $x-\bar x$  
D) $y-\bar y$.

21. The least-squares slope is:
A) $S_{xx}/S_{xy}$  
B) $S_{xy}/S_{xx}$  
C) $S_{yy}/S_{xx}$  
D) $S_{xy}/S_{yy}$.

22. The fitted intercept is:
A) $\bar y-\hat b\bar x$  
B) $\bar x-\hat b\bar y$  
C) $\bar y+\hat b\bar x$  
D) $SSE/(n-2)$.

23. In simple linear regression, residual df are:
A) $n$  B) $n-1$  C) $n-2$  D) 2.

24. $R=-0.95$ indicates:
A) strong positive linear association  
B) strong negative linear association  
C) no association of any kind  
D) causation.

25. $R^2=0.70$ means:
A) 70% of individual predictions are exactly correct  
B) 70% of sample response variation about its mean is accounted for by the fitted linear model  
C) the slope is 0.70  
D) correlation equals 0.70 necessarily.

26. Prediction outside the observed predictor range is:
A) interpolation  B) extrapolation  C) blocking  D) replication.

27. A U-shaped residual plot most directly suggests:
A) perfect linear fit  
B) curvature not captured by the straight-line model  
C) zero variance  
D) causation.

---

## Answer Key with Explanations

### Conceptual

1. The predictor $x$ is the explanatory/input variable; the response $y$ is the
   measured outcome modeled as changing with $x$. (§35.1)

2. It minimizes

   $$
   \sum e_i^2
   =
   \sum(y_i-\hat y_i)^2.
   $$

   (§35.1)

3. The observed response lies above the fitted line at that predictor value.
   (§35.1)

4. Least-squares normal-equation relationships give
   $\hat a=\bar y-\hat b\bar x$, so substituting $x=\bar x$ gives
   $\hat y=\bar y$. (§35.2)

5. Response units divided by predictor units. (§35.1)

6. It estimates the typical residual scatter about the fitted line and has the
   same units as the response. (§35.3)

7. The sign indicates the direction of sample linear association: positive or
   negative. (§35.4)

8. It is the fraction of sample response variation about $\bar y$ accounted for
   by the fitted simple linear relationship. (§35.4)

9. $R^2$ summarizes variation reduction, not residual structure. Systematic
   curvature or changing spread can remain even when $R^2$ is large. (§35.6)

10. Observed association can result from confounding, selection, reverse
    direction, common trends, or other uncontrolled causes. (§35.7)

### Calculation

11.

    $$
    \bar x
    =
    \frac{1+2+3}{3}
    =
    \boxed2,
    $$

    $$
    \bar y
    =
    \frac{2+4+6}{3}
    =
    \boxed4.
    $$

12.

    $$
    S_{xx}
    =
    (-1)^2+0^2+1^2
    =
    \boxed2.
    $$

    $$
    S_{xy}
    =
    (-1)(-2)+(0)(0)+(1)(2)
    =
    \boxed4.
    $$

13.

    $$
    \hat b
    =
    \frac42
    =
    \boxed2.
    $$

    $$
    \hat a
    =
    4-(2)(2)
    =
    \boxed0.
    $$

    Thus

    $$
    \hat y=2x.
    $$

14.

    $$
    \hat y
    =
    1+2(3.5)
    =
    \boxed8.
    $$

15.

    $$
    e
    =
    9-8.4
    =
    \boxed{0.6}.
    $$

16.

    $$
    R^2
    =
    1-\frac5{20}
    =
    \boxed{0.75}.
    $$

17.

    $$
    R
    =
    \frac{-12}{\sqrt{(16)(25)}}
    =
    \frac{-12}{20}
    =
    \boxed{-0.60}.
    $$

18.

    $$
    MSE
    =
    \frac{24}{8-2}
    =
    \boxed4.
    $$

    $$
    S_e
    =
    \sqrt4
    =
    \boxed2.
    $$

19. Slope standard error:

    $$
    SE_{\hat b}
    =
    \frac{2}{\sqrt{25}}
    =
    0.4.
    $$

    Margin:

    $$
    2.228(0.4)
    =
    0.8912.
    $$

    Interval:

    $$
    3.0\pm0.8912,
    $$

    so

    $$
    \boxed{
    2.109<b<3.891.
    }
    $$

### Multiple Choice

20. **B.** Residual equals observed minus fitted. (§35.1)

21. **B.** $\hat b=S_{xy}/S_{xx}$. (§35.2)

22. **A.** $\hat a=\bar y-\hat b\bar x$. (§35.2)

23. **C.** Two coefficients are estimated, leaving $n-2$ residual df. (§35.3)

24. **B.** Magnitude near 1 with negative sign indicates strong negative linear
    association. (§35.4)

25. **B.** That is the simple-regression variation interpretation of $R^2$.
    (§35.4)

26. **B.** Prediction beyond the observed predictor range is extrapolation.
    (§35.6)

27. **B.** Systematic U-shaped residual behavior indicates curvature. (§35.6)

---

## Practice Problems

1. **Least-squares components.** For
   $$x: 1,2,3,4$$
   and
   $$y: 3,5,4,8,$$
   compute $\bar x$, $\bar y$, $S_{xx}$, $S_{yy}$, and $S_{xy}$.

2. **Fit the line.** Using Problem 1, calculate $\hat b$, $\hat a$, and the
   fitted regression equation.

3. **Residuals.** Using Problem 2, calculate all fitted values and residuals.
   Verify that the residuals sum to approximately zero.

4. **Goodness of fit.** For Problem 1, compute $SSE$, $MSE$, $S_e$, $R$, and
   $R^2$.

5. **Prediction.** Use the fitted line from Problem 2 to predict $y$ at
   $x=2.5$ and $x=7$. Classify each prediction as interpolation or
   extrapolation.

6. **Slope confidence interval.** A simple regression has
   $$n=10,\quad \hat b=1.60,\quad S_e=0.80,\quad S_{xx}=20.$$
   Use $t_{0.025,8}=2.306$ to construct a 95% confidence interval for the
   slope.

7. **Intercept confidence interval.** A regression has
   $$n=10,\quad \hat a=4.0,\quad S_e=0.80,\quad \bar x=5,\quad S_{xx}=20.$$
   Use $t_{0.025,8}=2.306$ to construct a 95% confidence interval for the
   intercept.

8. **Correlation interpretation.** Compare the meanings of
   $R=0.85$, $R=-0.85$, and $R=0.05$.
   State what none of those values proves by itself.

9. **Residual diagnosis.** A fitted line has $R^2=0.92$, but residual spread
   grows steadily as fitted response increases. What model concern does this
   raise, and why is $R^2$ insufficient?

10. **Causation.** An observational regression shows a strong positive
    relationship between machine operating hours and defect count.
    Give two plausible reasons why the fitted association alone does not prove
    that operating hours are the sole cause of defects.

---

## Practice Problem Solutions

1. Data:

   $$
   x:1,2,3,4,
   \qquad
   y:3,5,4,8.
   $$

   Means:

   $$
   \bar x
   =
   \frac{10}{4}
   =
   \boxed{2.5},
   $$

   $$
   \bar y
   =
   \frac{20}{4}
   =
   \boxed5.
   $$

   Predictor deviations:

   $$
   -1.5,-0.5,0.5,1.5.
   $$

   Response deviations:

   $$
   -2,0,-1,3.
   $$

   Therefore

   $$
   S_{xx}
   =
   2.25+0.25+0.25+2.25
   =
   \boxed5,
   $$

   $$
   S_{yy}
   =
   4+0+1+9
   =
   \boxed{14},
   $$

   $$
   S_{xy}
   =
   3+0-0.5+4.5
   =
   \boxed7.
   $$

2. Slope:

   $$
   \hat b
   =
   \frac75
   =
   \boxed{1.4}.
   $$

   Intercept:

   $$
   \hat a
   =
   5-(1.4)(2.5)
   =
   5-3.5
   =
   \boxed{1.5}.
   $$

   So

   $$
   \boxed{
   \hat y=1.5+1.4x.
   }
   $$

3. Fitted values:

   $$
   x=1:\quad \hat y=2.9,
   $$

   $$
   x=2:\quad \hat y=4.3,
   $$

   $$
   x=3:\quad \hat y=5.7,
   $$

   $$
   x=4:\quad \hat y=7.1.
   $$

   Residuals:

   $$
   3-2.9=0.1,
   $$

   $$
   5-4.3=0.7,
   $$

   $$
   4-5.7=-1.7,
   $$

   $$
   8-7.1=0.9.
   $$

   Sum:

   $$
   0.1+0.7-1.7+0.9
   =
   \boxed0.
   $$

4. Residual sum of squares:

   $$
   SSE
   =
   0.1^2+0.7^2+(-1.7)^2+0.9^2
   $$

   $$
   =
   0.01+0.49+2.89+0.81
   =
   \boxed{4.20}.
   $$

   With

   $$
   n-2=2,
   $$

   $$
   MSE
   =
   \frac{4.2}{2}
   =
   \boxed{2.10}.
   $$

   $$
   S_e
   =
   \sqrt{2.10}
   \approx
   \boxed{1.449}.
   $$

   Correlation:

   $$
   R
   =
   \frac7{\sqrt{(5)(14)}}
   =
   \frac7{\sqrt{70}}
   \approx
   \boxed{0.8367}.
   $$

   $$
   R^2
   =
   \frac{49}{70}
   =
   \boxed{0.70}.
   $$

   Check:

   $$
   1-\frac{4.2}{14}
   =
   0.70.
   $$

5. At

   $$
   x=2.5,
   $$

   $$
   \hat y
   =
   1.5+1.4(2.5)
   =
   \boxed5.
   $$

   Since

   $$
   1\le2.5\le4,
   $$

   this is

   $$
   \boxed{\text{interpolation}.}
   $$

   At

   $$
   x=7,
   $$

   $$
   \hat y
   =
   1.5+1.4(7)
   =
   \boxed{11.3}.
   $$

   Since 7 is outside the observed range,

   $$
   \boxed{\text{extrapolation}.}
   $$

6. Slope standard error:

   $$
   SE_{\hat b}
   =
   \frac{0.80}{\sqrt{20}}
   \approx
   0.17889.
   $$

   Margin:

   $$
   2.306(0.17889)
   \approx
   0.4125.
   $$

   Therefore

   $$
   \boxed{
   1.188<b<2.013
   }
   $$

   approximately.

7. Intercept standard error:

   $$
   SE_{\hat a}
   =
   0.80
   \sqrt{
   \frac1{10}
   +
   \frac{25}{20}
   }
   $$

   $$
   =
   0.80\sqrt{1.35}
   \approx
   0.9295.
   $$

   Margin:

   $$
   2.306(0.9295)
   \approx
   2.143.
   $$

   Therefore

   $$
   \boxed{
   1.857<a<6.143
   }
   $$

   approximately.

8. $R=0.85$ indicates strong positive linear association.

   $R=-0.85$ indicates strong negative linear association of similar magnitude.

   $R=0.05$ indicates very weak sample **linear** association.

   None of these values alone proves causation.

9. The growing residual spread suggests **nonconstant variance**.

   $R^2$ only summarizes variation accounted for by the fitted relationship; it
   does not show whether residual variance is stable across the predictor or
   fitted-value range.

10. Possible explanations include:

    - older/high-hour machines may also experience heavier duty cycles,
    - maintenance frequency may differ systematically with machine age,
    - machine model or environment may confound both operating hours and defects,
    - defect reporting may increase with inspection frequency.

    A strong observational regression quantifies association but does not isolate
    the sole causal mechanism.

---

## Quick Reference

**Fitted line**

$$
\boxed{
\hat y=\hat a+\hat b x
}
$$

**Corrected sums**

$$
\boxed{
S_{xx}
=
\sum(x_i-\bar x)^2
}
$$

$$
\boxed{
S_{yy}
=
\sum(y_i-\bar y)^2
}
$$

$$
\boxed{
S_{xy}
=
\sum(x_i-\bar x)(y_i-\bar y)
}
$$

**Slope**

$$
\boxed{
\hat b
=
\frac{S_{xy}}{S_{xx}}
}
$$

**Intercept**

$$
\boxed{
\hat a
=
\bar y-\hat b\bar x
}
$$

**Residual**

$$
\boxed{
e_i
=
y_i-\hat y_i
}
$$

**Residual variation**

$$
\boxed{
SSE=\sum e_i^2
}
$$

$$
\boxed{
MSE=\frac{SSE}{n-2}
}
$$

$$
\boxed{
S_e=\sqrt{MSE}
}
$$

Equivalent:

$$
SSE
=
S_{yy}
-
\frac{S_{xy}^2}{S_{xx}}.
$$

**Correlation**

$$
\boxed{
R
=
\frac{S_{xy}}
{\sqrt{S_{xx}S_{yy}}}
}
$$

$$
-1\le R\le1.
$$

**Coefficient of determination**

$$
\boxed{
R^2
=
\frac{S_{xy}^2}
{S_{xx}S_{yy}}
=
1-\frac{SSE}{S_{yy}}.
}
$$

**Slope interval**

$$
\boxed{
\hat b
\pm
t_{\alpha/2,n-2}
\frac{S_e}{\sqrt{S_{xx}}}
}
$$

**Intercept interval**

$$
\boxed{
\hat a
\pm
t_{\alpha/2,n-2}
S_e
\sqrt{
\frac1n+\frac{\bar x^2}{S_{xx}}
}
}
$$

**Prediction discipline**

inside observed $x$ range → interpolation  
outside observed $x$ range → extrapolation.

**Residual warnings**

curve → missing nonlinear structure  
funnel → changing variance  
run-order trend → drift/dependence  
isolated extreme point → investigate influence/data quality.

**Interpretation**

correlation $\ne$ causation.

---

## What's Next

Regression models the relationship between measured variables.

The next chapter returns to a closely related engineering question:

> If the inputs themselves are uncertain, how uncertain is the calculated
> result?

**Chapter 01-36 — Measurement Uncertainty and Statistical Error Propagation**
will develop:

- measurement error versus measurement uncertainty,
- systematic and random components,
- standard uncertainty,
- sensitivity coefficients,
- the Kline-McClintock root-sum-square relation for uncorrelated inputs,
- expanded uncertainty and coverage factor,
- the difference between worst-case tolerance propagation and statistical
  uncertainty propagation,
- and how to report a result with an uncertainty statement.

The FE Reference Handbook places measurement error and uncertainty immediately
before linear regression, on printed pp. 69–70. Earlier chapters used
first-order differentials for deterministic sensitivity; the next chapter will
connect that calculus to the statistical uncertainty model printed in the
Handbook.

Carry one distinction forward:

> Regression asks how a response changes with a predictor. Uncertainty
> propagation asks how uncertain inputs make the calculated response uncertain.

— Your Mentor
