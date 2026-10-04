---
chapter: "01-28"
title: "Probability Fundamentals"
layer: 1
tier: D
template: technical
ledger_ids: [MATH-1D-028-01, MATH-1D-028-02, MATH-1D-028-03, MATH-1D-028-04, MATH-1D-028-05, MATH-1D-028-06, MATH-1D-028-07]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-28: Probability Fundamentals

> *"Probability does not tell you what must happen next. It gives you a disciplined
> way to reason about what could happen, how likely each outcome is, and how new
> information should change that judgment."*

---

## Before You Start

**Prerequisites:** [01-01 Numbers, Magnitude, and Metric Prefixes](01-01-numbers-magnitude-and-metric-prefixes.md) ·
[01-04 Expressions, Equations, and Inequalities](01-04-expressions-equations-inequalities.md) ·
[01-27 Algorithm and Logic Development](01-27-Algorithm-and-Logic-Development.md)

**Skip if:** You can define a sample space and event; distinguish union,
intersection, and complement; count ordered and unordered selections; apply the
addition and multiplication laws of probability; distinguish mutually exclusive
events from independent events; compute conditional probability; use Bayes'
theorem with a complete partition; and verify that a probability result lies in
the physically meaningful range from 0 to 1.

**Time:** About 100–120 min reading and worked examples · 40–50 min review
questions · 65–80 min practice problems.

**Working convention:** Probabilities are carried as exact fractions when
convenient and otherwise with guard digits until the final report. A probability
must satisfy

$$0\le P(E)\le1.$$

A result outside that interval is not a small arithmetic error; it is evidence
that the setup is wrong.

---

## On the Board Today

Engineering decisions are often made before the outcome is known.

A component may fail or survive. A measurement may fall inside or outside a
tolerance band. A test may be positive or negative. A sample may contain a defect.
A communication packet may arrive intact or corrupted. A project estimate may
land above or below a budget threshold.

Probability gives those uncertain outcomes a mathematical structure.

The first discipline is to separate three ideas:

1. **What outcomes are possible?**
2. **Which outcomes make up the event you care about?**
3. **How is probability assigned to those outcomes?**

Once those are clear, the familiar rules are not isolated formulas. They are
consequences of how events overlap, how conditions restrict the sample space, and
how counting supports equally likely outcomes.

The most common FE errors in probability are not advanced. They are structural:

- adding probabilities when events overlap without subtracting the overlap,
- multiplying probabilities as though events were independent when they are not,
- confusing "A or B" with "A and B,"
- using permutations when order does not matter,
- and reversing a conditional probability.

This chapter builds the foundation that prevents those mistakes.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **28.1** Define an experiment, outcome, sample space, and event
* **28.2** Use complements, unions, and intersections to describe engineering events
* **28.3** Apply the fundamental counting principle, permutations, and combinations
* **28.4** Compute probabilities from equally likely outcomes
* **28.5** Apply the addition law for overlapping and mutually exclusive events
* **28.6** Compute conditional probability and joint probability
* **28.7** Distinguish independent events from mutually exclusive events
* **28.8** Use multiplication rules for independent and dependent events
* **28.9** Apply Bayes' theorem to update a probability after new evidence
* **28.10** Use a complete partition and the law of total probability
* **28.11** Represent multi-stage probability problems with trees and tables
* **28.12** Check probability results using bounds, complements, and total-probability sums

---

## Notation Used Here

| Symbol | Meaning | Notes |
|---|---|---|
| $S$ | sample space | set of all possible outcomes |
| $A,B,C$ | events | subsets of $S$ |
| $A^c$ | complement of $A$ | outcomes in $S$ that are not in $A$ |
| $A\cup B$ | union | $A$ or $B$ or both |
| $A\cap B$ | intersection | both $A$ and $B$ |
| $P(A)$ | probability of event $A$ | between 0 and 1 |
| $P(A\mid B)$ | conditional probability | probability of $A$ given $B$ occurred |
| $n$ | total number of objects or trials | context dependent |
| $r$ | number selected | for permutations/combinations |
| $n!$ | factorial | $n(n-1)\cdots2\cdot1$ |
| $P(n,r)$ | permutations | order matters |
| $C(n,r)$ | combinations | order does not matter |

**Handbook notation note.** On printed pp. 65–66, the FE Reference Handbook
uses notation such as $A+B$ for event union and $P(A,B)$ for joint probability.
This chapter uses the more visually explicit set notation $A\cup B$ and
$A\cap B$, then shows the Handbook form in the dedicated lookup section.

---

## 28.1 Experiments, Outcomes, Sample Spaces, and Events

A **random experiment** is a process whose possible outcomes are known but whose
specific next outcome is uncertain.

Examples:

- inspect a manufactured part,
- observe whether a breaker trips under a test condition,
- record a sensor reading,
- select a component from inventory,
- transmit a bit through a noisy channel.

An **outcome** is one possible result.

The **sample space** $S$ is the set of all possible outcomes.

An **event** is any subset of the sample space.

### Discrete example

A two-bit message has outcomes

$$S=\{00,01,10,11\}.$$

Let

$$A=\{\text{exactly one bit is 1}\}.$$

Then

$$A=\{01,10\}.$$

Let

$$B=\{\text{first bit is 1}\}=\{10,11\}.$$

An event does not have to contain only one outcome.

### Complement

The complement $A^c$ contains every outcome in $S$ that is not in $A$.

For the two-bit example,

$$A^c=\{00,11\}.$$

Because $A$ and $A^c$ exhaust the sample space without overlap,

$$\boxed{P(A^c)=1-P(A).}$$

The complement rule is often the fastest path when "at least one" would
otherwise require several cases.

![FIG-01-28-001: A sample-space diagram for two binary trials. A rectangular universe S contains four equally sized outcome cells labeled 00, 01, 10, 11. Event A highlights 01 and 10 for "exactly one 1"; A-complement highlights 00 and 11. A side callout states P(A^c)=1−P(A) and distinguishes outcome, sample space, and event.](../figures/FIG-01-28-001-sample-space-event-complement.png)

### Worked Example 1 — At Least One Success by Complement

**Given.** A device passes a short self-test with probability 0.92. Two
independent devices are tested.

**Find.** The probability that at least one passes.

**Approach.** "At least one passes" is the complement of "both fail."

For one device,

$$P(\text{fail})=1-0.92=0.08.$$

With independence,

$$P(\text{both fail})=(0.08)^2=0.0064.$$

Therefore

$$P(\text{at least one pass})
=1-0.0064
=\boxed{0.9936}.$$

**Check.** The answer must exceed the single-device pass probability of 0.92,
and it does.

> ---
> **Mentor's Margin**
>
> "At least one" is a signal to look for a complement. The direct path may
> require several cases; the complement often requires only one.
>
> ---

---

## 28.2 Counting — When Probability Depends on How Many Ways

When outcomes are equally likely,

$$\boxed{
P(A)=\frac{\text{number of outcomes in }A}
{\text{number of outcomes in }S}.
}$$

The difficulty is often not probability itself. It is counting the outcomes
correctly.

### Fundamental counting principle

If a process has $m$ choices for one step and $n$ choices for the next, then the
two-step process has

$$\boxed{mn}$$

possible ordered outcomes, provided each first-step choice can be paired with each
second-step choice.

For several stages:

$$N=N_1N_2\cdots N_k.$$

### Factorial

For positive integer $n$,

$$\boxed{n!=n(n-1)(n-2)\cdots2\cdot1}$$

and

$$0!=1.$$

### Permutations — order matters

The number of ways to select and arrange $r$ distinct objects from $n$ distinct
objects is

$$\boxed{
P(n,r)=\frac{n!}{(n-r)!}.
}$$

### Combinations — order does not matter

The number of ways to select $r$ objects from $n$ distinct objects is

$$\boxed{
C(n,r)=\frac{n!}{r!(n-r)!}.
}$$

The relationship is

$$P(n,r)=r!\,C(n,r).$$

Every unordered group of $r$ objects has $r!$ possible internal orderings.

![FIG-01-28-002: A decision graphic comparing counting methods. A top question asks "Does order matter?" The Yes path leads to permutations P(n,r)=n!/(n−r)! and shows ABC, ACB, BAC as different outcomes. The No path leads to combinations C(n,r)=n!/[r!(n−r)!] and shows {A,B,C} as one selection regardless of order. A lower strip shows a three-stage counting tree with N1*N2*N3 outcomes.](../figures/FIG-01-28-002-permutation-combination-choice.png)

### Worked Example 2 — Choose the Correct Counting Model

**Given.** Six engineers are available.

**Find.**

(a) How many ways can a chair, recorder, and reviewer be assigned?  
(b) How many three-person review teams can be formed?

**Approach.**

Part (a) assigns distinct roles, so order matters.

Part (b) selects only membership, so order does not matter.

**Solution.**

(a)

$$P(6,3)=\frac{6!}{3!}
=6(5)(4)
=\boxed{120}.$$

(b)

$$C(6,3)=\frac{6!}{3!3!}
=\boxed{20}.$$

**Check.**

$$120=3!(20)=6(20),$$

which confirms the permutation/combination relationship.

### Repeated objects

If $n$ objects include repeated types, with $n_1,n_2,\ldots,n_k$ identical
objects of each type and

$$n_1+n_2+\cdots+n_k=n,$$

then distinct full arrangements are

$$\boxed{
\frac{n!}{n_1!n_2!\cdots n_k!}.
}$$

This form is also printed in the Handbook.

---

## 28.3 Set Operations and Venn-Diagram Logic

Events combine the same way sets do.

### Union — "A or B"

$$A\cup B$$

means outcomes in $A$, or $B$, or both.

### Intersection — "A and B"

$$A\cap B$$

means outcomes common to both events.

### Complement — "not A"

$$A^c$$

means outcomes outside $A$ but inside the sample space.

### De Morgan's laws

The complement of a union is the intersection of the complements:

$$\boxed{
(A\cup B)^c=A^c\cap B^c.
}$$

The complement of an intersection is the union of the complements:

$$\boxed{
(A\cap B)^c=A^c\cup B^c.
}$$

In words:

**not(A or B) = not A and not B**

and

**not(A and B) = not A or not B.**

This is the same logic that appeared in Chapter 01-27, now expressed as events.

![FIG-01-28-003: Four-panel Venn diagram reference inside a sample-space rectangle. Panels show A union B shaded, A intersection B shaded, A-complement shaded outside A, and the De Morgan equivalence (A union B)^c = A^c intersection B^c using matching shading. Each panel includes the matching plain-language phrase "A or B", "A and B", or "not A".](../figures/FIG-01-28-003-venn-set-operations.png)

### Mutually exclusive events

Events are **mutually exclusive** if they cannot occur together:

$$\boxed{A\cap B=\varnothing.}$$

Then

$$P(A\cap B)=0.$$

Examples:

- one measured value cannot be simultaneously below 10 and above 20,
- one selected part cannot simultaneously be labeled accepted and rejected if
  those categories are defined as exclusive.

Mutual exclusivity describes overlap.

It does **not** mean independence.

---

## 28.4 The Addition Law — Probability of "A or B"

For any two events,

$$\boxed{
P(A\cup B)
=
P(A)+P(B)-P(A\cap B).
}$$

Why subtract the intersection?

Because adding $P(A)+P(B)$ counts the overlap twice.

For mutually exclusive events,

$$P(A\cap B)=0,$$

so the rule simplifies to

$$\boxed{
P(A\cup B)=P(A)+P(B).
}$$

The FE Reference Handbook labels this relationship the **Law of Total
Probability** on printed p. 65. Later in this chapter we will also use the phrase
"law of total probability" for a complete partition of the sample space, which is
the standard modern usage in many probability texts. The formulas are related but
serve different purposes, so keep the context clear.

![FIG-01-28-004: Two overlapping circles A and B inside sample space S. The entire union is shaded. The intersection is cross-hatched and labeled "counted twice in P(A)+P(B), subtract once." Beneath, the general addition law P(A union B)=P(A)+P(B)−P(A intersection B) is shown, followed by the mutually exclusive special case where the circles do not overlap.](../figures/FIG-01-28-004-addition-law-overlap.png)

### Worked Example 3 — Overlap Matters

**Given.** In a group of engineering students:

$$P(A)=0.55$$

for students using calculator model A,

$$P(B)=0.40$$

for students using a spreadsheet for practice, and

$$P(A\cap B)=0.25.$$

**Find.** The probability that a randomly selected student uses calculator A
or a spreadsheet for practice.

**Solution.**

$$P(A\cup B)
=0.55+0.40-0.25
=\boxed{0.70}.$$

**Check.** Simply adding 0.55 and 0.40 would give 0.95 and double-count the
25% who are in both groups.

### More than two mutually exclusive events

If $A_1,\ldots,A_k$ are mutually exclusive,

$$\boxed{
P\left(\bigcup_{i=1}^{k}A_i\right)
=
\sum_{i=1}^{k}P(A_i).
}$$

If they also cover the complete sample space,

$$\boxed{
\sum_{i=1}^{k}P(A_i)=1.
}$$

That sum-to-one condition becomes a powerful check later.

---

## 28.5 Conditional Probability, Joint Probability, and Independence

A conditional probability changes the sample space.

$$P(A\mid B)$$

means:

> probability that $A$ occurs, given that $B$ is known to have occurred.

The definition is

$$\boxed{
P(A\mid B)
=
\frac{P(A\cap B)}{P(B)},
\qquad P(B)>0.
}$$

Rearranging gives the multiplication rule:

$$\boxed{
P(A\cap B)
=
P(B)P(A\mid B)
=
P(A)P(B\mid A).
}$$

This is the Handbook's **Law of Compound or Joint Probability**.

### Independence

Events $A$ and $B$ are independent when learning that one occurred does not
change the probability of the other:

$$\boxed{
P(A\mid B)=P(A)
}$$

and equivalently

$$\boxed{
P(A\cap B)=P(A)P(B).
}$$

### Independence versus mutual exclusivity

These are very different.

**Mutually exclusive:** the events cannot occur together.

**Independent:** one event does not alter the probability of the other.

If two nonzero-probability events are mutually exclusive, then

$$P(A\mid B)=0,$$

which differs from $P(A)>0$.

Therefore nonzero mutually exclusive events are **not independent**.

![FIG-01-28-005: Side-by-side comparison. Left panel "Mutually exclusive" shows two non-overlapping event circles and states P(A intersection B)=0; learning B occurred makes A impossible. Right panel "Independent" shows overlapping events and states P(A intersection B)=P(A)P(B) and P(A|B)=P(A). A center warning says "exclusive is about overlap; independent is about information." ](../figures/FIG-01-28-005-exclusive-versus-independent.png)

### Worked Example 4 — Conditional Probability from Counts

**Given.** A production lot contains 200 parts:

| | Pass final test | Fail final test | Total |
|---|---:|---:|---:|
| Supplier A | 92 | 8 | 100 |
| Supplier B | 85 | 15 | 100 |
| **Total** | 177 | 23 | 200 |

**Find.**

(a) $P(\text{fail})$  
(b) $P(A\mid\text{fail})$  
(c) $P(\text{fail}\mid A)$

**Solution.**

(a)

$$P(\text{fail})=\frac{23}{200}=\boxed{0.115}.$$

(b) Restrict attention to the 23 failed parts:

$$P(A\mid\text{fail})
=\frac{8}{23}
=\boxed{0.3478}.$$

(c) Restrict attention to the 100 Supplier A parts:

$$P(\text{fail}\mid A)
=\frac{8}{100}
=\boxed{0.0800}.$$

**Check.** The two conditional probabilities are not the same because their
denominators are different.

This distinction is the foundation of Bayes' theorem.

---

## 28.6 Probability Trees and Multi-Stage Events

A probability tree is useful when a process unfolds in stages.

At each branch:

- outgoing conditional probabilities must sum to 1,
- multiply along a complete path,
- add probabilities of distinct paths that represent the same final event.

Suppose 60% of parts come from Supplier A and 40% from Supplier B.

Failure probabilities are:

$$P(F\mid A)=0.02,$$

$$P(F\mid B)=0.05.$$

Then:

$$P(A\cap F)=P(A)P(F\mid A)
=(0.60)(0.02)
=0.012,$$

$$P(B\cap F)=P(B)P(F\mid B)
=(0.40)(0.05)
=0.020.$$

The total failure probability is

$$P(F)=0.012+0.020=\boxed{0.032}.$$

This is a partition calculation: every part came from exactly one supplier.

![FIG-01-28-006: Probability tree for two suppliers. First branch splits to A with 0.60 and B with 0.40. From A, branches Pass 0.98 and Fail 0.02; from B, Pass 0.95 and Fail 0.05. Each terminal path shows its joint probability obtained by multiplication. The two failure paths are bracketed and added to give P(F)=0.032. A note states "multiply along; add across disjoint paths." ](../figures/FIG-01-28-006-probability-tree-total-probability.png)

### Worked Example 5 — At Least One Defect in Three Independent Items

**Given.** Each independently produced item has defect probability

$$p=0.04.$$

**Find.** The probability of at least one defect among three items.

**Approach.** Use the complement: no defects.

Probability one item is good:

$$1-p=0.96.$$

All three good:

$$P(\text{none defective})=(0.96)^3=0.884736.$$

Therefore

$$P(\text{at least one defect})
=1-0.884736
=\boxed{0.115264}.$$

**Check.** The result is less than the crude upper bound $3(0.04)=0.12$ because
cases with multiple defects would otherwise be double-counted in that simple sum.

---

## 28.7 Bayes' Theorem — Updating After Evidence

Bayes' theorem reverses the direction of a conditional probability.

Suppose $A_1,A_2,\ldots,A_n$ are mutually exclusive events that partition the
sample space:

$$A_1\cup A_2\cup\cdots\cup A_n=S.$$

If evidence $B$ occurs, then

$$\boxed{
P(A_j\mid B)
=
\frac{P(B\mid A_j)P(A_j)}
{\displaystyle\sum_{i=1}^{n}P(B\mid A_i)P(A_i)}.
}$$

The denominator is the total probability of the evidence:

$$\boxed{
P(B)=
\sum_{i=1}^{n}P(B\mid A_i)P(A_i).
}$$

Bayes does not create new information.

It combines:

- a **prior probability** $P(A_j)$,
- a **likelihood** $P(B\mid A_j)$,
- and the total probability of the evidence $P(B)$,

to produce an updated or **posterior probability** $P(A_j\mid B)$.

### Worked Example 6 — Which Supplier Produced the Failed Part?

Use the supplier example:

$$P(A)=0.60,\qquad P(B)=0.40,$$

$$P(F\mid A)=0.02,\qquad P(F\mid B)=0.05.$$

From §28.6,

$$P(F)=0.032.$$

Find

$$P(B\mid F).$$

Bayes:

$$P(B\mid F)
=
\frac{P(F\mid B)P(B)}{P(F)}$$

$$=
\frac{(0.05)(0.40)}{0.032}
=
\frac{0.020}{0.032}
=
\boxed{0.625}.$$

Although Supplier B supplies only 40% of all parts, it accounts for 62.5% of
failed parts because its conditional failure rate is higher.

**Check.** Likewise,

$$P(A\mid F)=\frac{0.012}{0.032}=0.375,$$

and

$$0.375+0.625=1.$$

![FIG-01-28-007: Bayes update diagram using the supplier example. Left column shows priors A=0.60 and B=0.40. Middle multiplies each prior by failure likelihood: A path 0.60*0.02=0.012, B path 0.40*0.05=0.020. These combine to evidence total P(F)=0.032. Right column normalizes the failure-path weights to posterior shares A|F=0.375 and B|F=0.625. Arrows emphasize "prior × likelihood → joint weight → normalize".](../figures/FIG-01-28-007-bayes-update.png)

### Worked Example 7 — Positive Test Does Not Mean 98% Probability of Defect

**Given.**

A rare defect occurs in 1% of units:

$$P(D)=0.01.$$

A screening test has:

$$P(+\mid D)=0.98$$

and false-positive rate

$$P(+\mid D^c)=0.04.$$

**Find.**

$$P(D\mid +).$$

**Solution.**

First calculate total positive probability:

$$P(+)
=
P(+\mid D)P(D)
+
P(+\mid D^c)P(D^c).$$

So

$$P(+)
=
(0.98)(0.01)
+
(0.04)(0.99)$$

$$=0.0098+0.0396
=0.0494.$$

Now Bayes:

$$P(D\mid+)
=
\frac{(0.98)(0.01)}{0.0494}
=\boxed{0.1984}.$$

A positive test raises the defect probability from 1% to about 19.8%, but it
does not make the defect 98% likely.

The 98% number was

$$P(+\mid D),$$

not

$$P(D\mid+).$$

**Check.** Imagine 10,000 units:

- about 100 are defective; 98 test positive,
- about 9,900 are good; 396 test positive falsely.

Total positive tests:

$$98+396=494.$$

Defective among positive:

$$\frac{98}{494}=0.1984.$$

The frequency check agrees exactly with Bayes.

> ---
> **Mentor's Margin**
>
> Conditional probability is directional. Before substituting a number, say
> the condition in words: "probability of ___ given ___." Reversing the order
> is one of the most common probability errors.
>
> ---

---

## As the Handbook States It

> **Source verification.** Checked against the supplied *FE Reference Handbook
> 10.6*, eighth printing, April 2026. The *Engineering Probability and
> Statistics* section begins on printed p. 64. Printed p. 65 contains
> permutations and combinations, set laws, the general character of
> probability, and the addition law. Printed p. 66 contains the compound/joint
> probability law and Bayes' theorem, then begins random variables and
> probability distributions. In the supplied PDF these correspond to PDF
> pages 70–72.

Use the lookup method from
[00-03 Navigating the FE Reference Handbook](../layer-0-orientation/00-03-navigating-the-fe-reference-book.md):
identify whether the problem is a counting problem, set/event problem,
conditional-probability problem, or distribution problem before searching.

| Handbook topic | Printed page | Verified coverage |
|---|---:|---|
| Permutations and Combinations | 65 | Gives $P(n,r)$, $C(n,r)$, alternative notation, and repeated-object permutations |
| Sets | 65 | Gives De Morgan, associative, and distributive laws |
| General Character of Probability | 65 | States $0\le P(E)\le1$, impossible event 0, certain event 1 |
| Law of Total Probability | 65 | Gives the two-event addition rule in Handbook notation |
| Law of Compound or Joint Probability | 66 | Gives $P(A,B)=P(A)P(B\mid A)=P(B)P(A\mid B)$ |
| Bayes' Theorem | 66 | Gives the partition form used to reverse a conditional probability |
| Probability Functions, Distributions, and Expected Values | 66–67 | Begins the next topic: discrete/continuous random variables, PMF/PDF/CDF, expected value, and variance |

### Handbook notation translation

The Handbook uses:

$$P(A+B)$$

where this chapter writes

$$P(A\cup B),$$

and uses

$$P(A,B)$$

where this chapter writes

$$P(A\cap B).$$

So the Handbook's addition law

$$P(A+B)=P(A)+P(B)-P(A,B)$$

is the same relationship as

$$\boxed{
P(A\cup B)=P(A)+P(B)-P(A\cap B).
}$$

Likewise, its joint-probability law is the same as

$$\boxed{
P(A\cap B)=P(A)P(B\mid A)=P(B)P(A\mid B).
}$$

**Know without a lookup:**

- what an event is,
- the meaning of "and," "or," "not," and "given,"
- whether order matters in a counting problem,
- the difference between independence and mutual exclusivity,
- how complements simplify "at least one,"
- and which direction a conditional probability is asking.

Those are interpretation skills; a formula table cannot choose them for you.

---

## Where This Goes Wrong

**Treating probability as a percentage automatically.** Probability may be
reported as a fraction, decimal, or percent. Keep the mathematical value between
0 and 1 until the final formatting step.

**Using favorable/total when outcomes are not equally likely.** Counting works
directly only when the elementary outcomes have equal probability.

**Using permutations when order does not matter.** A committee is usually a
combination. Assigned roles are usually a permutation.

**Forgetting repeated objects.** Dividing by repeated-type factorials prevents
counting visually identical arrangements multiple times.

**Reading "or" as exclusive-or.** In probability, $A\cup B$ normally includes
the possibility that both occur.

**Adding overlapping events without subtracting the intersection.**

$$P(A)+P(B)$$

is correct only when $A$ and $B$ are mutually exclusive.

**Multiplying marginal probabilities without independence.**

$$P(A\cap B)=P(A)P(B)$$

requires independence.

The general rule is

$$P(A\cap B)=P(A)P(B\mid A).$$

**Confusing independence with mutual exclusivity.** Nonzero mutually exclusive
events cannot be independent.

**Reversing the condition.**

$$P(A\mid B)\ne P(B\mid A)$$

in general.

**Using the wrong denominator in conditional probability.** Once $B$ is given,
the relevant sample space is $B$.

**Ignoring the base rate in Bayes' theorem.** A highly sensitive test can still
have a modest posterior probability when the event itself is rare.

**Building an incomplete partition.** Bayes' denominator must include every
mutually exclusive route by which the evidence can occur.

**Forgetting tree-branch normalization.** Probabilities leaving a node must sum
to 1.

**Adding path probabilities that overlap.** Only disjoint terminal paths may be
added directly.

**Accepting an answer outside $[0,1]$.** Stop and repair the setup.

---

## Key Terms

| Term | Definition |
|---|---|
| random experiment | repeatable process with uncertain individual outcome |
| outcome | one possible result of an experiment |
| sample space | set of all possible outcomes |
| event | subset of a sample space |
| complement | outcomes in the sample space not belonging to an event |
| union | event containing outcomes in either event or both |
| intersection | event containing outcomes common to both events |
| factorial | product $n(n-1)\cdots1$ for nonnegative integer counting |
| fundamental counting principle | multiply the number of choices available at successive stages |
| permutation | ordered selection |
| combination | unordered selection |
| equally likely outcomes | outcomes assigned the same probability |
| mutually exclusive events | events that cannot occur together |
| conditional probability | probability of one event after another event is known to have occurred |
| joint probability | probability that specified events occur together |
| independent events | events for which occurrence of one does not change the probability of the other |
| probability tree | branching representation of sequential conditional probabilities |
| partition | mutually exclusive events whose union is the entire sample space |
| law of total probability | sum of disjoint partition-path probabilities producing an event |
| Bayes' theorem | rule for reversing a conditional probability using prior and evidence probabilities |
| prior probability | probability assigned before incorporating specified new evidence |
| likelihood | probability of observed evidence under a particular condition or hypothesis |
| posterior probability | updated probability after incorporating evidence |

---

## Review Questions

### Conceptual

1. Distinguish an outcome, sample space, and event.
2. Why is the complement method often useful for "at least one" problems?
3. What question determines whether to use a permutation or a combination?
4. What does $A\cup B$ mean? What does $A\cap B$ mean?
5. State De Morgan's two event laws in words.
6. What does it mean for two events to be mutually exclusive?
7. What does it mean for two events to be independent?
8. Why can two nonzero mutually exclusive events not be independent?
9. Explain why $P(A\mid B)$ and $P(B\mid A)$ are generally different.
10. In a probability tree, what operations are normally used along a path and across disjoint terminal paths?

### Calculation

11. A fair six-sided die is rolled once. Find the probability of an even result.
12. A system has 4 connector types and 3 cable lengths. How many type-length combinations are possible?
13. From 8 candidates, how many ways can a chair and recorder be assigned?
14. From the same 8 candidates, how many two-person teams can be selected?
15. If $P(A)=0.60$, $P(B)=0.35$, and $P(A\cap B)=0.20$, find $P(A\cup B)$.
16. If $P(A)=0.40$ and $P(B\mid A)=0.25$, find $P(A\cap B)$.
17. If $P(A\cap B)=0.12$ and $P(B)=0.30$, find $P(A\mid B)$.
18. A component succeeds independently with probability 0.95 on each of two trials. Find the probability of at least one success.
19. Supplier A provides 70% of parts with 1% defects. Supplier B provides 30% with 4% defects. Find the total defect probability.

### Multiple Choice

20. Which expression represents "A or B"?
A) $A\cap B$  B) $A\cup B$  C) $A^c$  D) $P(A\mid B)$.

21. Which expression represents the complement rule?
A) $P(A^c)=P(A)$  
B) $P(A^c)=1-P(A)$  
C) $P(A^c)=1/P(A)$  
D) $P(A^c)=P(A)^2$.

22. If order matters when selecting $r$ objects from $n$, use:
A) combinations  B) permutations  C) complements  D) Bayes.

23. If $A$ and $B$ are mutually exclusive:
A) $P(A\cap B)=1$  
B) $P(A\cap B)=0$  
C) $P(A)=P(B)$  
D) $P(A\mid B)=P(A)$.

24. If $A$ and $B$ are independent:
A) $P(A\cap B)=P(A)P(B)$  
B) $P(A\cup B)=0$  
C) $P(A\mid B)=0$  
D) they cannot occur together.

25. The denominator in $P(A\mid B)$ is:
A) $P(A)$  B) $P(B)$  C) $P(A\cup B)$  D) 1 always.

26. Bayes' theorem is principally used to:
A) count arrangements  
B) reverse a conditional probability using prior and evidence information  
C) calculate factorials  
D) prove two events are mutually exclusive.

27. A probability value of 1.08 should be interpreted as:
A) a highly likely valid event  
B) 108% probability, which is acceptable  
C) evidence of an invalid setup or arithmetic error  
D) a certain event.

---

## Answer Key with Explanations

### Conceptual

1. An **outcome** is one possible result. The **sample space** contains all
   possible outcomes. An **event** is any subset of that sample space. (§28.1)

2. "At least one" is the complement of "none." The complement often converts
   several overlapping cases into one simple calculation. (§28.1)

3. Ask whether order changes the outcome. If yes, use permutations. If no, use
   combinations. (§28.2)

4. $A\cup B$ means A or B or both. $A\cap B$ means both A and B. (§28.3)

5. Not(A or B) means not A **and** not B. Not(A and B) means not A **or**
   not B. (§28.3)

6. Mutually exclusive events have no common outcome:
   $A\cap B=\varnothing$. (§28.3)

7. Independent events are events for which knowing one occurred does not change
   the probability of the other. (§28.5)

8. If nonzero events are mutually exclusive, occurrence of one makes the other
   impossible, so its conditional probability becomes zero rather than remaining
   unchanged. (§28.5)

9. The condition changes the denominator/sample space. $P(A\mid B)$ restricts
   attention to B; $P(B\mid A)$ restricts attention to A. (§28.5)

10. Multiply probabilities along a complete path. Add probabilities across
    mutually exclusive terminal paths representing the desired event. (§28.6)

### Calculation

11. Even outcomes are $\{2,4,6\}$:

    $$P(\text{even})=\frac36=\boxed{\frac12}.$$

12.

    $$4(3)=\boxed{12}.$$

13. Assigned roles mean order matters:

    $$P(8,2)=8(7)=\boxed{56}.$$

14. Team membership only:

    $$C(8,2)=\frac{8!}{2!6!}
    =\boxed{28}.$$

15.

    $$P(A\cup B)=0.60+0.35-0.20
    =\boxed{0.75}.$$

16.

    $$P(A\cap B)=P(A)P(B\mid A)
    =(0.40)(0.25)
    =\boxed{0.10}.$$

17.

    $$P(A\mid B)
    =\frac{P(A\cap B)}{P(B)}
    =\frac{0.12}{0.30}
    =\boxed{0.40}.$$

18. Probability both trials fail:

    $$(0.05)^2=0.0025.$$

    Therefore

    $$P(\text{at least one success})
    =1-0.0025
    =\boxed{0.9975}.$$

19.

    $$P(D)
    =(0.70)(0.01)+(0.30)(0.04)$$

    $$=0.007+0.012
    =\boxed{0.019}.$$

### Multiple Choice

20. **B.** Union represents A or B or both. (§28.3)

21. **B.** An event and its complement exhaust the sample space, so their
    probabilities sum to 1. (§28.1)

22. **B.** Permutations count ordered selections. (§28.2)

23. **B.** Mutually exclusive events have zero intersection probability.
    (§28.3)

24. **A.** Independence gives
    $P(A\cap B)=P(A)P(B)$. (§28.5)

25. **B.** By definition,
    $P(A\mid B)=P(A\cap B)/P(B)$. (§28.5)

26. **B.** Bayes reverses the conditional direction by combining a prior,
    likelihood, and total evidence probability. (§28.7)

27. **C.** Every valid probability must lie from 0 through 1 inclusive.
    (§28.1)

---

## Practice Problems

1. **Sample space.** Two components are each classified Pass (P) or Fail (F).
   List the complete sample space. Define event A = "exactly one fails" and
   event B = "the first component passes." Find $A\cap B$ and $A\cup B$.

2. **Counting.** Seven different test fixtures are available. Four must be
   selected for a validation set.
   (a) How many four-fixture sets are possible?
   (b) How many ordered four-fixture test sequences are possible?

3. **Repeated objects.** How many distinct arrangements can be formed from the
   letters in `LEVEL`?

4. **Addition law.** In a survey,
   $P(A)=0.48$, $P(B)=0.52$, and $P(A\cap B)=0.19$.
   Find $P(A\cup B)$ and the probability of neither A nor B.

5. **Conditional probability.** Of 500 inspected parts, 40 fail dimensional
   inspection. Of those 40, 18 also fail surface inspection. Find
   $P(\text{surface fail}\mid\text{dimensional fail})$.

6. **Independence.** A sensor packet is transmitted over two independent links.
   Link 1 succeeds with probability 0.98 and Link 2 with probability 0.97.
   Find the probability both succeed and the probability at least one fails.

7. **Probability tree.** Supplier A provides 75% of parts and has a 2% defect
   rate. Supplier B provides 25% and has a 6% defect rate.
   Find the total defect probability.

8. **Bayes.** Using Problem 7, if a randomly selected part is defective, find
   the probability it came from Supplier B.

9. **Screening test.** A fault occurs in 3% of units. A test has
   $P(+\mid F)=0.95$ and $P(+\mid F^c)=0.08$.
   Find $P(F\mid+)$.

10. **At least one.** Four independent modules each fail during a test with
    probability 0.02. Find the probability that at least one fails.

---

## Practice Problem Solutions

1. The sample space is

   $$S=\{PP,PF,FP,FF\}.$$

   Exactly one fails:

   $$A=\{PF,FP\}.$$

   First component passes:

   $$B=\{PP,PF\}.$$

   Therefore

   $$A\cap B=\boxed{\{PF\}},$$

   $$A\cup B=\boxed{\{PP,PF,FP\}}.$$

2. (a) Order does not matter:

   $$C(7,4)
   =\frac{7!}{4!3!}
   =\boxed{35}.$$

   (b) Order matters:

   $$P(7,4)
   =\frac{7!}{3!}
   =7(6)(5)(4)
   =\boxed{840}.$$

3. `LEVEL` has 5 letters with two Ls and two Es:

   $$N=\frac{5!}{2!2!}
   =\frac{120}{4}
   =\boxed{30}.$$

4.

   $$P(A\cup B)
   =0.48+0.52-0.19
   =\boxed{0.81}.$$

   Neither:

   $$1-0.81=\boxed{0.19}.$$

5. The condition restricts the denominator to the 40 dimensional failures:

   $$P(S\mid D)
   =\frac{18}{40}
   =\boxed{0.45}.$$

6. Both succeed:

   $$P(S_1\cap S_2)
   =(0.98)(0.97)
   =\boxed{0.9506}.$$

   At least one fails is the complement:

   $$1-0.9506
   =\boxed{0.0494}.$$

7.

   $$P(D)
   =(0.75)(0.02)+(0.25)(0.06)$$

   $$=0.015+0.015
   =\boxed{0.030}.$$

8.

   $$P(B\mid D)
   =
   \frac{P(D\mid B)P(B)}{P(D)}$$

   $$=
   \frac{(0.06)(0.25)}{0.030}
   =\frac{0.015}{0.030}
   =\boxed{0.50}.$$

9. First calculate total positive probability:

   $$P(+)
   =(0.95)(0.03)+(0.08)(0.97)$$

   $$=0.0285+0.0776
   =0.1061.$$

   Then

   $$P(F\mid+)
   =
   \frac{(0.95)(0.03)}{0.1061}
   =\boxed{0.2686\text{ approximately}}.$$

   So a positive result raises the fault probability from 3% to about 26.9%.

10. Probability no module fails:

    $$(0.98)^4=0.92236816.$$

    Therefore

    $$P(\text{at least one failure})
    =1-0.92236816
    =\boxed{0.07763184}.$$

---

## Quick Reference

**Probability bounds**

$$\boxed{0\le P(A)\le1}$$

$$P(S)=1,\qquad P(\varnothing)=0.$$

**Complement**

$$\boxed{P(A^c)=1-P(A)}$$

**Equally likely outcomes**

$$\boxed{
P(A)=\frac{N(A)}{N(S)}.
}$$

**Counting**

$$n!=n(n-1)\cdots1,\qquad 0!=1$$

Permutation:

$$\boxed{
P(n,r)=\frac{n!}{(n-r)!}
}$$

Combination:

$$\boxed{
C(n,r)=\frac{n!}{r!(n-r)!}
}$$

Repeated objects:

$$\boxed{
\frac{n!}{n_1!n_2!\cdots n_k!}
}$$

**Event operations**

$$A\cup B=\text{A or B or both}$$

$$A\cap B=\text{A and B}$$

$$A^c=\text{not A}$$

De Morgan:

$$(A\cup B)^c=A^c\cap B^c$$

$$(A\cap B)^c=A^c\cup B^c$$

**Addition law**

$$\boxed{
P(A\cup B)
=
P(A)+P(B)-P(A\cap B)
}$$

Mutually exclusive:

$$P(A\cap B)=0.$$

**Conditional probability**

$$\boxed{
P(A\mid B)
=
\frac{P(A\cap B)}{P(B)}
}$$

**Joint probability**

$$\boxed{
P(A\cap B)
=
P(A)P(B\mid A)
=
P(B)P(A\mid B)
}$$

**Independence**

$$\boxed{
P(A\mid B)=P(A)
}$$

$$\boxed{
P(A\cap B)=P(A)P(B)
}$$

**Partition total**

$$\boxed{
P(B)=
\sum_i P(B\mid A_i)P(A_i)
}$$

**Bayes**

$$\boxed{
P(A_j\mid B)
=
\frac{P(B\mid A_j)P(A_j)}
{\sum_iP(B\mid A_i)P(A_i)}
}$$

**Tree rule**

multiply along a path · add across mutually exclusive paths.

---

## What's Next

This chapter treated probability at the event level: outcomes, counting, unions,
intersections, conditions, independence, and Bayes updates.

The next step is to attach numerical values to uncertain outcomes and describe
their probability behavior systematically.

**Chapter 01-29 — Random Variables and Probability Distributions** will build:

- discrete and continuous random variables,
- probability mass functions and probability density functions,
- cumulative distribution functions,
- expected value and variance,
- binomial probability,
- and the connection between event probabilities and areas or sums under a
  distribution.

The FE Reference Handbook begins that material immediately after Bayes' theorem
on printed p. 66 and continues through the standard distributions on later pages.

Carry one distinction forward:

> An event is a set of outcomes. A random variable assigns a numerical value to
> those outcomes.

That distinction is what turns probability into statistics.

— Your Mentor
