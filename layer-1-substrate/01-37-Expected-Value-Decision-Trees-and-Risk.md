---
chapter: "01-37"
title: "Expected Value, Decision Trees, and Risk"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-037-01, MATH-1D-037-02, MATH-1D-037-03, MATH-1D-037-04, MATH-1D-037-05, MATH-1D-037-06, MATH-1D-037-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-37: Expected Value, Decision Trees, and Risk

> *"Expected value compresses uncertain outcomes into one probability-weighted
> average. Decision analysis begins there, but engineering judgment decides
> whether that average is enough."*

---

## Before You Start

**Prerequisites:** [01-28 Probability Fundamentals](01-28-Probability-Fundamentals.md) ·
[01-29 Random Variables and Probability Distributions](01-29-Random-Variables-and-Probability-Distributions.md)

**Skip if:** You can compute the expected value of discrete outcomes; distinguish
expected benefit, expected cost, and expected loss; identify decision, chance, and
outcome nodes; evaluate a decision tree by rolling it back from right to left;
handle conditional branch probabilities; compare alternatives using expected
value; compute opportunity loss and expected opportunity loss; explain the value
of additional information; and recognize situations where expected value alone
is not a sufficient engineering decision rule.

**Time:** About 95–115 min reading and worked examples · 40–50 min review
questions · 65–80 min practice problems.

**Working convention:** Benefits are treated as positive and costs/losses as
negative when a single net-value convention is used. If a table is written in
costs only, lower expected cost is preferred. State the convention before doing
the arithmetic.

---

## On the Board Today

Probability tells you what might happen.

Expected value tells you the probability-weighted average consequence.

Suppose an engineering choice can produce outcomes

$$
C_1,C_2,\ldots,C_m
$$

with probabilities

$$
p_1,p_2,\ldots,p_m,
$$

where

$$
\sum_{i=1}^{m}p_i=1.
$$

Then

$$
\boxed{
EV
=
\sum_{i=1}^{m}p_iC_i.
}
$$

That is the same expected-value idea developed for random variables in Chapter
01-29, now applied to a decision consequence.

A decision tree organizes the sequence when choices and uncertain events occur in
stages.

The FE Reference Handbook distinguishes:

- **decision nodes** — the decision maker chooses a path,
- **chance nodes** — a probabilistic event chooses a path,
- **outcome nodes** — the final consequence is recorded.

The calculation proceeds backward.

At a chance node, take a probability-weighted average.

At a decision node, choose the preferred available branch.

That process is called **rollback**.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **37.1** Compute expected value from discrete outcomes and probabilities
* **37.2** Distinguish expected benefit, expected cost, expected loss, and net expected value
* **37.3** Construct and interpret decision, chance, and outcome nodes
* **37.4** Verify probability completeness at each chance node
* **37.5** Roll back a one-stage or multistage decision tree
* **37.6** Use conditional probabilities correctly on sequential branches
* **37.7** Compare alternatives using expected value under a stated decision convention
* **37.8** Build and use an opportunity-loss table
* **37.9** Compute expected opportunity loss
* **37.10** Compute expected value of perfect information for a finite decision table
* **37.11** Perform sensitivity checks when probabilities or consequences are uncertain
* **37.12** Explain why expected value alone may be insufficient when safety, irreversible loss, or risk tolerance matters

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $C_i$ | consequence of outcome $i$ | benefit, cost, loss, or net value |
| $p_i$ | probability of outcome $i$ | $0\le p_i\le1$ |
| $EV$ | expected value | probability-weighted average consequence |
| $EC$ | expected cost | lower is preferred in a cost-only model |
| $EL$ | expected loss | lower is preferred |
| $R_{ij}$ | regret/opportunity loss for decision $i$ under state $j$ | nonnegative when defined against best state-specific choice |
| $EOL_i$ | expected opportunity loss of decision $i$ | probability-weighted regret |
| $EV_{\text{PI}}$ | expected value with perfect information | best decision chosen after state is known |
| $EVPI$ | expected value of perfect information | $EV_{\text{PI}}-\max EV$ for benefit/net-value problems |

**Sign convention.** If benefits and costs are mixed in one calculation, convert
them to one consistent net-value basis before taking the expected value.

---

## 37.1 Expected Value — A Probability-Weighted Average

For discrete consequences,

$$
\boxed{
EV
=
\sum_i p_i C_i.
}
$$

This is not the most likely outcome.

It is not a guaranteed future result.

It is the long-run average consequence if the same probabilistic situation could
be repeated many times under the stated model.

### Probability check

Before calculating,

$$
\boxed{
\sum_i p_i=1
}
$$

must hold for mutually exclusive and collectively exhaustive branches.

If branch probabilities sum to

$$
0.92
$$

or

$$
1.13,
$$

stop. The chance model is incomplete or inconsistent.

![FIG-01-37-001: Expected-value balance diagram. Several possible outcomes C1, C2, C3 with probabilities p1, p2, p3 feed a weighted-sum block EV=sum p_i C_i. A side check shows probabilities summing to 1. The figure contrasts "most likely outcome" with "probability-weighted average" to show they are not the same.](../figures/FIG-01-37-001-expected-value-weighted-average.png)

### Worked Example 1 — Expected Net Value

A design modification has the following annual net outcomes:

| Outcome | Probability | Net value |
|---|---:|---:|
| strong demand | 0.30 | \$120,000 |
| normal demand | 0.50 | \$40,000 |
| weak demand | 0.20 | -\$30,000 |

Expected value:

$$
EV
=
0.30(120000)
+
0.50(40000)
+
0.20(-30000).
$$

Therefore

$$
EV
=
36000+20000-6000
=
\boxed{\$50,000}.
$$

**Check.** Probabilities sum to 1.

The expected value is not itself one of the listed outcomes. That is normal.

### Worked Example 2 — Expected Cost

A component has two maintenance outcomes:

- routine service: probability 0.85, cost \$2,000,
- major repair: probability 0.15, cost \$14,000.

Expected cost:

$$
EC
=
0.85(2000)
+
0.15(14000)
$$

$$
=
1700+2100
=
\boxed{\$3,800}.
$$

For a cost-only model, lower expected cost is preferred.

---

## 37.2 Expected Loss and Opportunity Loss

Sometimes consequences are naturally stated as losses.

Then

$$
\boxed{
EL
=
\sum_i p_i L_i.
}
$$

Lower expected loss is preferred.

### Opportunity loss

Suppose several decisions are possible and the best decision would depend on
which future state occurs.

For each state, define opportunity loss as

$$
\boxed{
R_{ij}
=
\text{best payoff in state }j
-
\text{payoff from decision }i.
}
$$

For a benefit/payoff table,

$$
R_{ij}\ge0.
$$

The best decision in each state has regret 0 for that state.

Expected opportunity loss is

$$
\boxed{
EOL_i
=
\sum_j p_j R_{ij}.
}
$$

Choose the decision with the smallest expected opportunity loss.

![FIG-01-37-002: Payoff-to-regret transformation. A two-decision by three-state payoff table is shown on the left. For each state column, the highest payoff is highlighted. On the right, each payoff is converted to regret = state-best payoff minus chosen payoff, creating zeros for state-best decisions. Expected opportunity loss is shown as the probability-weighted row total.](../figures/FIG-01-37-002-opportunity-loss-table.png)

### Worked Example 3 — Expected Opportunity Loss

Two alternatives have net payoffs:

| State | Probability | Alternative A | Alternative B |
|---|---:|---:|---:|
| high demand | 0.40 | 100 | 160 |
| low demand | 0.60 | 60 | 20 |

Payoffs are in thousands of dollars.

For high demand, the best payoff is 160.

Regrets:

$$
R_{A,H}=160-100=60,
$$

$$
R_{B,H}=160-160=0.
$$

For low demand, the best payoff is 60.

$$
R_{A,L}=60-60=0,
$$

$$
R_{B,L}=60-20=40.
$$

Expected opportunity loss:

$$
EOL_A
=
0.40(60)+0.60(0)
=
24,
$$

$$
EOL_B
=
0.40(0)+0.60(40)
=
24.
$$

So

$$
\boxed{
EOL_A=EOL_B=24
}
$$

thousand dollars.

The alternatives tie under this probability model.

Check directly by expected payoff:

$$
EV_A
=
0.40(100)+0.60(60)
=
76,
$$

$$
EV_B
=
0.40(160)+0.60(20)
=
76.
$$

The same tie appears.

---

## 37.3 Decision Trees — Nodes, Branches, and Probabilities

The FE Reference Handbook provides three decision-tree symbols.

### Decision node

A **decision node** represents a point where the decision maker chooses among
available paths.

It is not averaged.

You retain the preferred branch.

### Chance node

A **chance node** represents an uncertain event.

Each branch carries a probability.

At the chance node, compute

$$
\boxed{
EV_{\text{chance}}
=
\sum_i p_i C_i.
}
$$

### Outcome node

An **outcome node** records the terminal consequence of one complete path.

### Branch probabilities

At each chance node,

$$
\boxed{
\sum_i p_i=1.
}
$$

In a multistage tree, path probabilities follow the conditional-probability rules
from Chapter 01-28.

![FIG-01-37-003: Decision-tree symbol legend modeled after the Handbook concept but redrawn. A square decision node branches to two selectable alternatives. A circular chance node branches to three probabilistic outcomes labeled p1, p2, p3 with sum 1. Terminal outcome nodes show final values. A footer says decision node=choose, chance node=average, outcome node=record consequence.](../figures/FIG-01-37-003-decision-tree-node-types.png)

### Worked Example 4 — One Decision, One Chance Node

A project manager can choose Design A or Design B.

Design A gives a certain net value of

$$
\$70,000.
$$

Design B has:

- 60% chance of \$110,000,
- 40% chance of \$20,000.

Expected value of Design B:

$$
EV_B
=
0.60(110000)+0.40(20000)
$$

$$
=
66000+8000
=
\$74,000.
$$

At the decision node:

$$
EV_A=70000,
$$

$$
EV_B=74000.
$$

If expected net value is the sole decision criterion,

$$
\boxed{\text{choose Design B}.}
$$

The margin is only

$$
\$4,000,
$$

which makes a sensitivity check appropriate.

---

## 37.4 Rolling Back a Multistage Decision Tree

Decision trees are evaluated from right to left.

This is **rollback**.

At each chance node:

$$
\boxed{\text{replace the node by its expected value}.}
$$

At each decision node:

$$
\boxed{\text{replace the node by the preferred branch value}.}
$$

Continue until the initial decision node is reached.

The order matters because future choices may depend on earlier uncertain
outcomes.

![FIG-01-37-004: Multistage decision tree with a square decision node on the left, followed by chance nodes and a later decision node on one branch. Arrows show rollback from terminal outcomes toward the left. Chance nodes are replaced by expected values; decision nodes retain the best branch. Intermediate rolled-back values are printed beside the nodes.](../figures/FIG-01-37-004-decision-tree-rollback.png)

### Worked Example 5 — Two-Stage Rollback

An engineering team can either **test** a prototype or **skip testing**.

If they skip testing, expected net value is known to be

$$
\$52,000.
$$

Testing costs

$$
\$8,000.
$$

After the test:

- favorable result occurs with probability 0.60,
- unfavorable result occurs with probability 0.40.

After a favorable result, the team may:

- launch: net value before test cost = \$100,000,
- stop: net value before test cost = \$0.

Choose launch, so favorable branch value before test cost is

$$
100000.
$$

After an unfavorable result, they may:

- launch: net value before test cost = \$10,000,
- stop: net value before test cost = \$0.

Choose launch because 10,000 exceeds 0.

Expected value before subtracting test cost:

$$
0.60(100000)+0.40(10000)
=
60000+4000
=
64000.
$$

Subtract test cost:

$$
EV_{\text{test}}
=
64000-8000
=
\boxed{\$56,000}.
$$

Compare:

$$
EV_{\text{test}}=56000,
$$

$$
EV_{\text{skip}}=52000.
$$

Expected-value criterion:

$$
\boxed{\text{test the prototype}.}
$$

**Rollback lesson.** The later decisions were optimized before the earlier test
decision was compared.

---

## 37.5 Conditional Probabilities in Sequential Decisions

Multistage trees often use conditional probabilities.

Suppose a diagnostic test can be positive or negative and a later failure event
depends on that result.

Then branches might use

$$
P(F\mid +)
$$

and

$$
P(F\mid -),
$$

not the unconditional

$$
P(F).
$$

A complete path probability is the product of the conditional branches along
that path.

For example,

$$
\boxed{
P(+\text{ and }F)
=
P(+)\,P(F\mid+).
}
$$

This is the compound-probability rule from Chapter 01-28.

### Worked Example 6 — Path Probabilities

A screening process gives:

$$
P(+)=0.30,
$$

$$
P(-)=0.70.
$$

Conditional failure probabilities are

$$
P(F\mid+)=0.10,
$$

$$
P(F\mid-)=0.02.
$$

Then

$$
P(+\cap F)
=
0.30(0.10)
=
0.03,
$$

and

$$
P(-\cap F)
=
0.70(0.02)
=
0.014.
$$

Total failure probability:

$$
P(F)
=
0.03+0.014
=
\boxed{0.044}.
$$

The tree reproduces the law of total probability.

### Probability integrity check

At every chance node, branch probabilities must sum to 1 **conditional on having
reached that node**.

Do not combine branch probabilities from different nodes into one sum.

---

## 37.6 Value of Information and Sensitivity Analysis

Information is valuable when it changes a decision.

### Expected value with perfect information

For each future state, suppose you could know the state before choosing.

Then you would choose the best decision separately in each state.

For a payoff problem,

$$
\boxed{
EV_{\text{PI}}
=
\sum_j
p_j
\left(
\max_i C_{ij}
\right).
}
$$

Without perfect information, choose one decision in advance:

$$
\boxed{
EV_{\text{current}}
=
\max_i
\sum_j p_j C_{ij}.
}
$$

Then

$$
\boxed{
EVPI
=
EV_{\text{PI}}
-
EV_{\text{current}}.
}
$$

For a payoff problem,

$$
EVPI\ge0.
$$

It is the maximum expected amount worth paying for perfect information under the
expected-value model.

![FIG-01-37-005: Value-of-information diagram. Left path "decide now" selects one alternative before state is known and produces current best expected value. Right path "perfect information" reveals the future state first, then selects the best action for that state. EVPI is shown as EV_with_perfect_information minus best_current_EV.](../figures/FIG-01-37-005-expected-value-perfect-information.png)

### Worked Example 7 — EVPI

Use the payoff table from Worked Example 3.

Without information,

$$
EV_A=76,
$$

$$
EV_B=76.
$$

So

$$
EV_{\text{current}}=76.
$$

With perfect information:

- if high demand occurs, choose B and receive 160,
- if low demand occurs, choose A and receive 60.

Thus

$$
EV_{\text{PI}}
=
0.40(160)+0.60(60)
$$

$$
=
64+36
=
100.
$$

Therefore

$$
\boxed{
EVPI
=
100-76
=
24
}
$$

thousand dollars.

Notice that this equals the minimum expected opportunity loss:

$$
\boxed{
EVPI=\min EOL=24
}
$$

for this finite payoff model.

### Sensitivity to probability

Suppose Alternative A pays:

- 100 in high demand,
- 60 in low demand.

Alternative B pays:

- 160 in high demand,
- 20 in low demand.

Let

$$
p=P(\text{high demand}).
$$

Then

$$
EV_A
=
100p+60(1-p)
=
60+40p,
$$

$$
EV_B
=
160p+20(1-p)
=
20+140p.
$$

Set them equal:

$$
60+40p
=
20+140p.
$$

So

$$
40
=
100p
$$

and

$$
\boxed{
p=0.40.
}
$$

At exactly 0.40 the decisions tie.

If

$$
p>0.40,
$$

B has the larger expected payoff.

If

$$
p<0.40,
$$

A has the larger expected payoff.

This is a **decision threshold**.

![FIG-01-37-006: Sensitivity graph with probability p on the horizontal axis and expected payoff on the vertical axis. EV_A=60+40p and EV_B=20+140p are straight lines crossing at p=0.40. The regions p<0.40 and p>0.40 are labeled preferred A and preferred B respectively.](../figures/FIG-01-37-006-decision-probability-sensitivity.png)

---

## 37.7 Risk and the Limits of Expected Value

Expected value is powerful, but it compresses an entire distribution to one
number.

Two alternatives can have the same expected value and radically different risk.

### Worked Example 8 — Same Expected Value, Different Risk

Alternative X guarantees

$$
\$50,000.
$$

Alternative Y gives:

- 50% chance of \$150,000,
- 50% chance of -\$50,000.

Expected value of Y:

$$
EV_Y
=
0.50(150000)
+
0.50(-50000)
$$

$$
=
75000-25000
=
\boxed{\$50,000}.
$$

Thus

$$
EV_X=EV_Y.
$$

But their risk profiles are not the same.

Alternative X has no modeled outcome variation.

Alternative Y includes a substantial loss possibility.

Expected value alone cannot tell you whether that loss is acceptable.

### Engineering constraints can dominate EV

An alternative may have the highest expected monetary value but still be
unacceptable because it violates:

- safety criteria,
- environmental limits,
- reliability requirements,
- legal obligations,
- maximum-loss constraints,
- liquidity/budget constraints.

In such cases, expected value is a calculation inside the decision process, not
the entire decision rule.

### Risk-neutral interpretation

Choosing the largest expected monetary value corresponds to a **risk-neutral**
criterion for the modeled consequences.

A real organization may be risk-averse toward catastrophic loss even when the
average monetary value looks favorable.

The FE Reference Handbook prints expected-value decision-tree mechanics, but it
does not provide a general utility-theory treatment in the cited section.

This chapter therefore stops at the engineering warning:

> Do not allow an average benefit to hide an unacceptable tail consequence.

![FIG-01-37-007: Two alternatives with identical expected value but different outcome distributions. Alternative X is a single certain outcome at 50. Alternative Y has two outcomes, -50 and 150, each with probability 0.5, also averaging to 50. A safety-gate symbol below shows that an unacceptable loss constraint can eliminate an alternative before expected-value ranking.](../figures/FIG-01-37-007-same-ev-different-risk.png)

### Worked Example 9 — Apply a Hard Constraint Before EV Ranking

Two design alternatives have expected net values:

$$
EV_A=\$90,000,
$$

$$
EV_B=\$75,000.
$$

Alternative A also has a 2% modeled chance of exceeding a mandatory safety limit.

Alternative B satisfies the stated limit across all modeled outcomes.

If the safety requirement is a hard design constraint, the correct logic is:

1. eliminate alternatives that violate the constraint,
2. compare expected values among feasible alternatives.

Therefore A is not selected merely because

$$
90000>75000.
$$

Expected value does not override mandatory feasibility.

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. Printed pp. 66–67 define expected value
> for discrete and continuous random variables. Printed p. 237 in
> *Engineering Economics* defines decision, chance, and outcome nodes for
> economic decision trees and prints the expected-value relation
> $EV=(C_1)(p_1)+(C_2)(p_2)+\cdots$.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Expected Values | 66–67 | Defines expected value as probability-weighted outcome for random variables |
| Economic Decision Trees | 237 | Defines decision node, chance node, and outcome node |
| Expected Value in Decision Tree | 237 | Gives $EV=(C_1)(p_1)+(C_2)(p_2)+\cdots$ |

### What this chapter adds

The supplied Handbook gives the expected-value formula and decision-tree node
types but does not develop a complete rollback tutorial, opportunity-loss table,
EVPI derivation, probability-sensitivity threshold, or risk-neutrality warning in
the cited section.

Those are guide-developed tools built from the Handbook's probability and
expected-value foundations.

The identity

$$
EVPI=\min EOL
$$

for the finite payoff-table framework follows algebraically from the same payoff
and probability model; it is not presented here as a quoted Handbook formula.

**Know without a lookup:**

- probabilities at a chance node must sum to 1,
- chance node → probability-weighted average,
- decision node → choose the preferred branch,
- roll a tree back from right to left,
- keep benefit/cost signs consistent,
- expected value is not a guaranteed outcome,
- and a hard engineering constraint can supersede expected-value ranking.

---

## Where This Goes Wrong

**Treating expected value as the most likely outcome.**

**Assuming the expected value must be one of the possible outcomes.**

**Using branch probabilities that do not sum to 1 at a chance node.**

**Adding conditional probabilities from different nodes as though they belong to
the same sample space.**

**Multiplying probabilities across branches that are mutually exclusive rather
than sequential.**

**Averaging at a decision node.** Decision nodes are optimized, not averaged.

**Choosing at a chance node.** Chance nodes are averaged, not optimized.

**Rolling the tree from left to right.** Evaluate future nodes first.

**Forgetting to subtract an information or test cost from the branch that incurs
it.**

**Mixing positive costs with positive benefits without defining a net-value
convention.**

**Choosing the largest expected cost.** In a cost-only model, smaller is better.

**Defining regret from the wrong state-specific benchmark.** Each state uses the
best payoff available in that state.

**Allowing negative regret in a standard opportunity-loss table.** If the
state-best payoff is used correctly, regret is nonnegative.

**Paying more than EVPI for perfect information under the expected-value model.**

**Assuming estimated probabilities are exact.** Sensitivity analysis may change
the preferred decision.

**Using expected monetary value to override a mandatory safety or legal
constraint.**

**Calling the highest-EV alternative "risk free."** Expected value does not show
tail severity by itself.

---

## Key Terms

| Term | Definition |
|---|---|
| expected value | probability-weighted average consequence |
| expected cost | probability-weighted average cost |
| expected loss | probability-weighted average loss |
| net value | benefit minus cost under a stated sign convention |
| decision tree | branching representation of sequential choices and chance events |
| decision node | point at which the decision maker chooses a branch |
| chance node | point at which a probabilistic event determines a branch |
| outcome node | terminal result of a decision-tree path |
| rollback | evaluation of a decision tree from terminal outcomes back toward the initial decision |
| opportunity loss | shortfall from the best payoff available for a realized state |
| regret | another name for opportunity loss |
| expected opportunity loss | probability-weighted average regret |
| perfect information | hypothetical knowledge of the future state before a decision is chosen |
| expected value of perfect information | improvement in expected value available from perfect state information |
| decision threshold | parameter or probability value at which two alternatives have equal decision value |
| sensitivity analysis | study of how the preferred decision changes as model inputs vary |
| risk-neutral criterion | decision rule based on maximizing expected net value or minimizing expected cost/loss |
| tail consequence | low-probability extreme outcome that may matter despite modest effect on the mean |
| feasibility constraint | requirement an alternative must satisfy before value ranking is applied |

---

## Review Questions

### Conceptual

1. What does expected value represent?
2. Why does expected value not have to equal one of the possible outcomes?
3. What is the difference between a decision node and a chance node?
4. What must the branch probabilities at a chance node sum to?
5. What does rollback mean in a decision tree?
6. Distinguish expected loss from opportunity loss.
7. How is expected opportunity loss constructed?
8. What does EVPI represent?
9. Why should probability sensitivity be checked when alternatives have similar expected values?
10. Why can a safety constraint override an expected-value ranking?

### Calculation

11. Outcomes are 10, 30, and 80 with probabilities 0.2, 0.5, and 0.3. Find the expected value.
12. A repair costs \$1,000 with probability 0.9 and \$8,000 with probability 0.1. Find expected cost.
13. A decision has payoffs 50 and 120 under two states with probabilities 0.7 and 0.3. Find expected payoff.
14. Alternative A has payoffs 80 and 40; B has 120 and 10. State probabilities are 0.4 and 0.6. Find both expected values.
15. For Question 14, construct the regret table and calculate both expected opportunity losses.
16. A chance node has branch probabilities 0.15, 0.25, and 0.60 with values 100, 40, and -20. Find the node value.
17. A branch has probability 0.30, followed by a conditional event of probability 0.20. Find the complete-path probability.
18. A decision gives certain value 55. Another gives 0.5 probability of 90 and 0.5 probability of 30. Which has higher expected value?
19. If $EV_A=40+30p$ and $EV_B=70-20p$, find the probability at which the two alternatives tie.

### Multiple Choice

20. At a chance node you:
A) choose the largest branch  
B) calculate a probability-weighted average  
C) ignore probabilities  
D) always choose the lowest value.

21. At a decision node you:
A) average all branches  
B) multiply all branch probabilities  
C) retain the preferred feasible branch  
D) require probabilities to sum to 1.

22. Rollback evaluates a decision tree:
A) left to right  
B) right to left  
C) top to bottom only  
D) randomly.

23. Expected opportunity loss is preferred when it is:
A) largest  
B) smallest  
C) negative only  
D) equal to the largest payoff.

24. EVPI is:
A) always negative  
B) the value improvement available from perfect state information under the model  
C) the largest single payoff  
D) the probability of the best outcome.

25. If costs only are being compared, the expected-value rule prefers:
A) the largest expected cost  
B) the smallest expected cost  
C) the largest variance always  
D) the largest branch probability only.

26. Sequential path probabilities are generally formed using:
A) conditional-probability multiplication  
B) simple addition of all probabilities  
C) subtraction from 2  
D) the sample mean.

27. A hard safety constraint should be applied:
A) only after maximizing expected money  
B) before expected-value ranking among feasible alternatives  
C) only when EV is negative  
D) never in decision analysis.

---

## Answer Key with Explanations

### Conceptual

1. It is the probability-weighted average consequence under the stated outcome
   model. (§37.1)

2. It is a weighted average across possible outcomes and may lie between them.
   (§37.1)

3. A decision node is controlled by the decision maker; a chance node is resolved
   probabilistically. (§37.3)

4.

   $$
   \boxed{1}.
   $$

   (§37.1, §37.3)

5. Evaluate terminal outcomes first, reduce chance nodes to expected values,
   reduce later decision nodes to preferred branches, and continue backward.
   (§37.4)

6. Expected loss averages actual losses. Opportunity loss measures the shortfall
   from the best decision that could have been chosen for the realized state.
   (§37.2)

7. Multiply each state-specific regret by that state's probability and sum.
   (§37.2)

8. It is the maximum expected improvement available if the future state could be
   known perfectly before the decision. (§37.6)

9. Small changes in an uncertain probability estimate may reverse which
   alternative has the larger expected value. (§37.6)

10. Expected value ranks consequences only among alternatives allowed by the
    decision framework. A mandatory safety requirement is a feasibility
    condition, not a monetary preference. (§37.7)

### Calculation

11.

    $$
    EV
    =
    0.2(10)+0.5(30)+0.3(80)
    $$

    $$
    =
    2+15+24
    =
    \boxed{41}.
    $$

12.

    $$
    EC
    =
    0.9(1000)+0.1(8000)
    $$

    $$
    =
    900+800
    =
    \boxed{\$1,700}.
    $$

13.

    $$
    EV
    =
    0.7(50)+0.3(120)
    $$

    $$
    =
    35+36
    =
    \boxed{71}.
    $$

14.

    $$
    EV_A
    =
    0.4(80)+0.6(40)
    =
    32+24
    =
    \boxed{56}.
    $$

    $$
    EV_B
    =
    0.4(120)+0.6(10)
    =
    48+6
    =
    \boxed{54}.
    $$

    Alternative A has the larger expected payoff.

15. State 1 best payoff is 120:

    $$
    R_{A1}=40,
    \qquad
    R_{B1}=0.
    $$

    State 2 best payoff is 40:

    $$
    R_{A2}=0,
    \qquad
    R_{B2}=30.
    $$

    Therefore

    $$
    EOL_A
    =
    0.4(40)+0.6(0)
    =
    \boxed{16},
    $$

    $$
    EOL_B
    =
    0.4(0)+0.6(30)
    =
    \boxed{18}.
    $$

    A has the smaller expected opportunity loss.

16.

    $$
    EV
    =
    0.15(100)+0.25(40)+0.60(-20)
    $$

    $$
    =
    15+10-12
    =
    \boxed{13}.
    $$

17.

    $$
    P(\text{complete path})
    =
    0.30(0.20)
    =
    \boxed{0.06}.
    $$

18. Certain alternative:

    $$
    EV_A=55.
    $$

    Uncertain alternative:

    $$
    EV_B
    =
    0.5(90)+0.5(30)
    =
    45+15
    =
    60.
    $$

    Thus

    $$
    \boxed{\text{the uncertain alternative has higher EV}.}
    $$

19. Set equal:

    $$
    40+30p
    =
    70-20p.
    $$

    Therefore

    $$
    50p=30
    $$

    and

    $$
    \boxed{p=0.60}.
    $$

### Multiple Choice

20. **B.** Chance nodes are probability-weighted averages. (§37.3)

21. **C.** At a decision node, retain the preferred feasible branch. (§37.3)

22. **B.** Rollback proceeds from outcomes toward the initial decision. (§37.4)

23. **B.** Lower expected opportunity loss is preferred. (§37.2)

24. **B.** EVPI is the expected-value improvement from knowing the state before
    choosing. (§37.6)

25. **B.** Lower expected cost is preferred. (§37.1)

26. **A.** Sequential branch probabilities follow conditional-probability
    multiplication. (§37.5)

27. **B.** Feasibility and mandatory safety conditions are applied before
    ranking feasible alternatives by EV. (§37.7)

---

## Practice Problems

1. **Expected value.** A component redesign has outcomes of \$80k, \$20k, and
   -\$40k with probabilities 0.25, 0.55, and 0.20. Find expected net value.

2. **Expected cost.** A maintenance strategy produces annual cost \$5k with
   probability 0.80 and \$25k with probability 0.20. Find expected annual cost.

3. **Decision comparison.** Alternative A has a certain value of 60. Alternative
   B has a 0.70 chance of 100 and a 0.30 chance of -20. Compare expected values.

4. **Regret table.** Two decisions have payoffs:
   - A: 90 in State 1, 50 in State 2
   - B: 140 in State 1, 20 in State 2
   with state probabilities 0.30 and 0.70.
   Construct the regret table and find each EOL.

5. **Decision-tree rollback.** A test costs 5. If performed, a favorable result
   occurs with probability 0.40 and leads to a best later decision worth 100;
   an unfavorable result occurs with probability 0.60 and leads to a best later
   decision worth 30. Skipping the test has value 50. Which branch has higher
   expected net value?

6. **Conditional branches.** A first-stage event has probability 0.25. Given
   that event, a second event occurs with probability 0.40. Find the joint path
   probability.

7. **Perfect information.** Using Problem 4, find current best expected payoff,
   expected payoff with perfect information, and EVPI.

8. **Sensitivity threshold.** Alternative A has
   $$EV_A=30+80p$$
   and Alternative B has
   $$EV_B=70+20p.$$
   Find the tie probability and preferred alternative on either side.

9. **Equal EV, unequal risk.** Option X pays 40 for certain. Option Y pays 100
   with probability 0.5 and -20 with probability 0.5. Find both EVs and explain
   one decision-relevant difference the EV does not capture.

10. **Constraint before ranking.** Alternative A has EV 120 but violates a
    mandatory pressure limit in one modeled state. Alternative B has EV 95 and
    satisfies all stated constraints. Explain the correct decision order.

---

## Practice Problem Solutions

1.

   $$
   EV
   =
   0.25(80)+0.55(20)+0.20(-40)
   $$

   $$
   =
   20+11-8
   =
   \boxed{23\text{ thousand dollars}}.
   $$

2.

   $$
   EC
   =
   0.80(5000)+0.20(25000)
   $$

   $$
   =
   4000+5000
   =
   \boxed{\$9,000}.
   $$

3. Alternative A:

   $$
   EV_A=60.
   $$

   Alternative B:

   $$
   EV_B
   =
   0.70(100)+0.30(-20)
   $$

   $$
   =
   70-6
   =
   \boxed{64}.
   $$

   By expected value alone,

   $$
   \boxed{\text{B is preferred}.}
   $$

4. State 1 best payoff = 140:

   $$
   R_{A1}=50,\qquad R_{B1}=0.
   $$

   State 2 best payoff = 50:

   $$
   R_{A2}=0,\qquad R_{B2}=30.
   $$

   Therefore

   $$
   EOL_A
   =
   0.30(50)+0.70(0)
   =
   \boxed{15},
   $$

   $$
   EOL_B
   =
   0.30(0)+0.70(30)
   =
   \boxed{21}.
   $$

   A has the smaller EOL.

5. Test branch before test cost:

   $$
   0.40(100)+0.60(30)
   =
   40+18
   =
   58.
   $$

   Subtract cost:

   $$
   EV_{\text{test}}
   =
   58-5
   =
   \boxed{53}.
   $$

   Skip:

   $$
   EV_{\text{skip}}
   =
   50.
   $$

   Therefore

   $$
   \boxed{\text{test}}
   $$

   has the larger expected net value.

6.

   $$
   P
   =
   0.25(0.40)
   =
   \boxed{0.10}.
   $$

7. Expected payoffs:

   $$
   EV_A
   =
   0.30(90)+0.70(50)
   =
   27+35
   =
   62,
   $$

   $$
   EV_B
   =
   0.30(140)+0.70(20)
   =
   42+14
   =
   56.
   $$

   Current best:

   $$
   EV_{\text{current}}
   =
   \boxed{62}.
   $$

   With perfect information:

   $$
   EV_{\text{PI}}
   =
   0.30(140)+0.70(50)
   =
   42+35
   =
   \boxed{77}.
   $$

   Therefore

   $$
   EVPI
   =
   77-62
   =
   \boxed{15}.
   $$

   This equals the minimum EOL from Problem 4.

8. Set equal:

   $$
   30+80p
   =
   70+20p.
   $$

   Therefore

   $$
   60p=40
   $$

   and

   $$
   \boxed{
   p=\frac23\approx0.6667.
   }
   $$

   For

   $$
   p<2/3,
   $$

   B is larger.

   For

   $$
   p>2/3,
   $$

   A is larger.

9. Option X:

   $$
   EV_X
   =
   40.
   $$

   Option Y:

   $$
   EV_Y
   =
   0.5(100)+0.5(-20)
   =
   50-10
   =
   \boxed{40}.
   $$

   The expected values tie.

   But Y includes a possible loss of 20 while X is certain at 40. EV alone does
   not capture that difference in outcome spread/tail loss.

10. First apply the mandatory pressure constraint.

    Alternative A is infeasible under the stated requirement and is removed from
    consideration.

    Then compare value among feasible alternatives.

    Therefore B remains the admissible choice despite its lower numerical EV.

---

## Quick Reference

**Expected value**

$$
\boxed{
EV
=
\sum_i p_iC_i
}
$$

with

$$
\boxed{
\sum_i p_i=1.
}
$$

**Expected cost / loss**

$$
EC=\sum_i p_iC_i
$$

$$
EL=\sum_i p_iL_i.
$$

For cost/loss models: lower is preferred.

**Chance node**

$$
\boxed{
EV_{\text{node}}
=
\sum_i p_iC_i.
}
$$

**Decision node**

retain the preferred feasible branch.

**Rollback**

evaluate from terminal outcomes toward the initial decision.

**Sequential path probability**

$$
\boxed{
P(A\cap B)
=
P(A)P(B\mid A).
}
$$

**Opportunity loss**

For payoff table:

$$
\boxed{
R_{ij}
=
\max_i(C_{ij})-C_{ij}.
}
$$

**Expected opportunity loss**

$$
\boxed{
EOL_i
=
\sum_j p_jR_{ij}.
}
$$

Choose the minimum.

**Perfect information**

$$
\boxed{
EV_{\text{PI}}
=
\sum_jp_j\max_i(C_{ij})
}
$$

$$
\boxed{
EVPI
=
EV_{\text{PI}}
-
\max_iEV_i.
}
$$

For the finite payoff model,

$$
\boxed{
EVPI=\min_iEOL_i.
}
$$

**Sensitivity threshold**

set competing expected-value equations equal and solve for the uncertain
probability/parameter.

**Risk warning**

expected value is an average, not a guarantee and not a substitute for mandatory
engineering constraints.

---

## What's Next

Expected value and decision trees use probabilities once the outcome model is
known.

The FE Reference Handbook also provides a compact table of common probability
and density functions whose means and variances are useful across reliability,
waiting-time, count, and bounded-range problems.

**Chapter 01-38 — Common Engineering Probability Distributions** will develop:

- hypergeometric sampling without replacement,
- Poisson counts,
- geometric and negative-binomial waiting counts,
- uniform distributions,
- exponential waiting-time models,
- Weibull lifetime models,
- triangular engineering-estimate models,
- and distribution selection from assumptions rather than formula appearance.

Carry one rule forward:

> The distribution name is the last step in model selection, not the first.
> Start with what the random quantity counts or measures and how the data are
> generated.

— Your Mentor
