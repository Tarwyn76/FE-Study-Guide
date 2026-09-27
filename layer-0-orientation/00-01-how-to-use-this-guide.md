---
chapter: "00-01"
title: "How to Use This Guide"
layer: 0
tier: null
template: orientation
ledger_ids: [ORIENT-0-001-01]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: revised
---

# Chapter 00-01: How to Use This Guide

> *"Every engineer who ever passed this exam started where you are: not
> knowing something. The difference between the ones who make it and the
> ones who don't isn't talent. It's whether they built their foundation in
> the right order."*

---

## Before You Start

**Prerequisites:** None. This is the first chapter in the guide.

**Skip if:** Never. Every route begins here, and this chapter is the only
place the guide explains how to read itself.

**Time:** ~20 min read · ~15 min review questions

---

## On the Board Today

Apprentice, before you open a single chapter on statics or circuits, spend
twenty minutes here. This guide is not built like most textbooks, and if
you read it like one you'll fight it the whole way.

Let me tell you what problem this guide was built to solve.

Most exam prep assumes you took the coursework and just need reminding.
It'll name a section property and its formula and move right along, as
though you had it at hand. If you took that class four years ago, fine. If
you never took it, that sentence is a locked door with no key.

I've watched that failure mode wreck good, capable people. Not because they
couldn't learn engineering. Because the material assumed a foundation they
were never given, and then made them feel stupid for not having it. The
fault was in the writing, every time.

So this guide makes a different promise, and I want to state it plainly
before you go any further.

**Nothing is used before it's taught.** Not once. Every term, every symbol,
every equation appears for the first time in a chapter that builds it from
something you already have. The first thing you build stands on arithmetic.
Everything after that stands on what came before.

That promise is not a matter of me being careful. Careful doesn't scale to a
guide this size. There's a script that reads every chapter, checks every
technical term against a master list, and refuses to build the book if any
term shows up before the chapter that defines it. If I break the promise,
the guide doesn't compile.

|-----------|
|> **Mentor's Margin:** I'd rather be caught by a machine than by you at|
|> midnight, three days before your exam, staring at a sentence that assumes|
|> something nobody ever taught you. That's the whole reason the linter|
|> exists.|
|-------------|

There are two narrow exceptions, and I'd rather name them now than have you
discover them and think I cheated.

**Illustrative mentions.** Occasionally I'll name something you haven't met,
purely as an example of a category — a search term to type, a symbol that
collides with another symbol, the kind of question a section contains. You
aren't expected to know it and nothing in the chapter depends on it. These
are marked in the source so the linter lets them through, and in the text
they're always clearly a name rather than a tool.

**Preview notes and primers.** When a chapter genuinely needs a later tool,
it says so explicitly. Both devices are explained in §0.6.

There's a second problem. "The FE exam" isn't one exam — it's seven. A
civil candidate and an electrical candidate sit for tests that overlap in
maybe half their content and diverge completely in the rest. Write one book
for all seven and it's bloated for everybody. Write seven books and you've
written the same statistics chapter seven times, badly.

So this guide is layered. Shared foundation first, written once. Discipline
specifics last, written separately. You read the foundation your exam needs
and skip the rest — but the rest is still here, still finished, still
readable, if you ever get curious or change disciplines.

Let's walk through how it's put together.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* **LO-1** Explain how this guide is organized and why it's organized that way
* **LO-2** Locate your discipline's route map and identify your reading path
* **LO-3** Decide when to skip a chapter and when skipping will cost you
* **LO-4** Use the test-out quizzes to skip material you already know
* **LO-5** Describe the anatomy of a chapter and the purpose of each part
* **LO-6** Distinguish a primer from a preview note and explain when each appears
* **LO-7** Distinguish the three types of review question and explain what each tests
* **LO-8** Describe the three levels of examination in this guide and when to take each
* **LO-9** Identify the study habits that determine whether this guide works for you
* **LO-10** Execute the first-week sequence that turns this chapter into action

---

## 0.1 The Five Parts

Five parts, in reading order.

| Part | What's in it | Chapters |
|---|---|---|
| **Layer 0** | Orientation. What the exam is, how the Handbook works, how to use this guide. | 3 |
| **Layer 1** | The mathematical substrate. Arithmetic through differential equations and statistics. | 41 |
| **Layer 2** | Core engineering science. Six tiers, shared across the disciplines. | 70 |
| **Layer 3** | Seven discipline tracks. Your specialty. | ~100 |
| **Reference** | Every formula, symbol, and term in one place, each linked back to where it was taught. | 15 |

Plus the examinations, which get their own section below.

![FIG-00-01-001: Layer structure flowchart showing the five parts of the guide stacked vertically, with Layer 2 expanded to show six tiers 2A through 2F](../figures/FIG-00-01-001-layer-structure.png)

Layer 1 starts at genuine zero. Place value. Order of operations. Scientific
notation. If you already know that material, don't sit through it — there's
a way to test out, and I'll show you in a moment. But it's there because
some of you have been out of a classroom for a decade, and you deserve a
real starting line instead of a polite fiction about one.

---

## 0.2 Tiers — Why Skipping Is Safe

Layers 1 and 2 are divided into **tiers**: lettered groups of related
chapters that get taken or skipped as a unit.

Layer 2's six tiers:

| Tier | Subject |
|---|---|
| **2A** | Professional practice — economics, ethics, licensure |
| **2B** | Physical science and safety — chemistry, biology, materials, hazards |
| **2C** | Mechanics — statics, dynamics, strength of materials |
| **2D** | Thermal and fluid sciences — fluids, thermodynamics, heat transfer |
| **2E** | Electrical — circuits, AC power, machines |
| **2F** | Measurement and control — sensors, signals, feedback |

Tiers exist so that skipping is clean. You don't skip scattered chapters and
hope you didn't need chapter 41. You skip Tier 2C — all nineteen chapters of
it — because your exam contains no mechanics whatsoever. That's a decision
you can make with confidence instead of anxiety.

|-----------|
|> **Mentor's Margin:** If you're sitting for Electrical & Computer, you skip|
|> Tiers 2C and 2D entirely. That's thirty-seven chapters. It feels wrong the|
|> first time you do it, like you're getting away with something. You aren't.|
|> Go look at your specification sheet and confirm it for yourself: no|
|> statics, no dynamics, no mechanics of materials, no fluids, no thermo, no|
|> heat transfer. The skip is deliberate, and it's the whole reason this guide|
|> is layered.|
|-----------|
> **Source verification.** Which tiers a given discipline skips is derived
> from that discipline's NCEES exam specification. The Electrical & Computer
> example above drives a thirty-seven-chapter decision, so confirm it against
> your own specification sheet before acting on it. Your route map lists the
> specification areas each tier maps to.

---

## 0.3 Prerequisites — The Thing That Makes This Navigable

Every chapter opens with a **prerequisites** list: the specific earlier
chapters it stands on. Not "you should know some algebra." Actual chapter
numbers.

That list is what lets you read this guide out of order without getting
lost.

Say you're an electrical candidate, you've skipped all of mechanics, and six
months from now you get curious about how a beam carries load. You open the
beam chapter cold. It tells you exactly which three chapters you'd need
first. You go get those three, come back, and read the beam chapter. No
guessing. No reading nineteen chapters to find the four that mattered.

---

## 0.4 Route Maps — Find Yours Now

A **route map** is your reading path: the chapters your exam requires, in
order, with everything else marked optional.

Go find yours before you read anything else.

| Discipline | Route map |
|---|---|
| Chemical | `routes/route-chemical.md` |
| Civil | `routes/route-civil.md` |
| Electrical & Computer | `routes/route-electrical-computer.md` |
| Environmental | `routes/route-environmental.md` |
| Industrial & Systems | `routes/route-industrial-systems.md` |
| Mechanical | `routes/route-mechanical.md` |
| Other Disciplines | `routes/route-other-disciplines.md` |

Every chapter also carries a **skip-if** line in its Before You Start block,
telling you whether it's on your route. So even if you wander off the map,
the map finds you.

---

## 0.5 Anatomy of a Chapter

Same structure every time, so you stop spending attention on the format and
spend it on the content.

Seventeen sections, in this order:

| # | Part | What it's for |
|---|---|---|
| 1 | **Epigraph** | The stake. Why this chapter matters, in one breath. |
| 2 | **Before You Start** | Prerequisites, skip-if line, and time estimate. |
| 3 | **On the Board Today** | Purpose before content. The "why" before the "what." |
| 4 | **Learning Objectives** | Mapped to your NCEES specification. This is what the exam tests. |
| 5 | **Primer** *(rare)* | Just enough of a later tool to get through this chapter. |
| 6 | **Notation Used Here** | Every symbol in this chapter, with units. |
| 7 | **The idea** | Plain language. What's physically happening. No equations. |
| 8 | **Building the result** | The derivation, every step justified by something already taught. |
| 9 | **As the Handbook States It** | The same result in the exact form you'll see on exam day, with the page number. |
| 10 | **Source Verification** | Named wherever a fact comes from outside this guide, with instructions for confirming it yourself. |
| 11 | **Worked Examples** | Warm-up, typical, exam-level. Every one ends with a check. |
| 12 | **Where This Goes Wrong** | The mistakes people actually make here. |
| 13 | **Key Terms** | Every term this chapter defined. |
| 14 | **Review Questions** | Conceptual, Calculation, Multiple Choice. |
| 15 | **Answer Key with Explanations** | Full explanations, including why the wrong answers are wrong. |
| 16 | **Quick Reference** | Formula-dense review card. |
| 17 | **What's Next** | Where you're going and what it builds on. |

|-----------|
|> **Mentor's Margin** is not in that list because it isn't a section. Those are|
|> scattered throughout — warnings, shortcuts, things I'd tell you if I were|
|> sitting beside you.|
|-----------|
Orientation chapters like this one have no notation table, no derivation, and
no Handbook form, because there's nothing to derive. Everything else is the
same.

![FIG-00-01-002: Chapter anatomy diagram showing the 17 sections grouped into three zones — orientation, content, and assessment — with Mentor's Margin shown as a scattered element spanning all three](../figures/FIG-00-01-002-chapter-anatomy.png)

The idea always comes before the algebra. If you've ever been handed an
equation and told to trust it, you know why that ordering matters.

Three of those sections exist only because of the FE's format, and they're
worth calling out.

**As the Handbook States It.** The FE gives you the *FE Reference Handbook*
and nothing else — no notes, no textbook, no personal copy. So every result
in this guide gets shown twice: once the way we derive it, once the way the
Handbook prints it, with the page number. Sometimes the notation differs.
When it does, I'll say so and show you both, because on exam day you're
reading the Handbook's version, not mine.

**Source Verification.** NCEES revises specifications, policies, and the
Handbook itself on their own schedule. Anywhere this guide states a fact that
could go stale — a question count, a page number, a calculator rule — there's
a block naming where the fact came from and telling you to confirm it. I'd
rather hand you a citation than ask for your trust.

**Where This Goes Wrong.** Six hours. Time pressure does strange things to
careful people. This section collects the errors that people who *understood
the material* still made. It's the most concentrated value per word in the
whole guide.

|-----------|
|> **Mentor's Margin:** Read "Where This Goes Wrong" twice. Once when you work|
|> the chapter, and once the week before your exam. It's the only section I'd|
|> tell you to reread on purpose.|
|-----------|

---

## 0.6 Primers and Preview Notes

Two devices handle the places where a chapter brushes against material that
hasn't arrived yet. They are not the same thing and the difference matters.

### A primer

Occasionally a chapter genuinely needs a tool before that tool's home
chapter arrives. Safety needs a little Ohm's law before the electrical
theory chapter. That sort of thing.

When that happens, the chapter opens with a **primer**: symbols, units,
exactly the calculations that chapter needs, one worked example, and a plain
statement of where the full treatment lives.

A primer is not a shortcut and it isn't a substitute. It's a loan. You get
just enough to finish the chapter in front of you, and the real development
comes later, in its proper place, built from the ground up.

Primers are rare by design. The whole dependency structure of this guide
exists to make them unnecessary. When you see one, it means I couldn't
reorder my way out of the problem.

### A preview note

A **preview note** is much smaller: one or two sentences naming a concept
that arrives later, flagging why it matters, and pointing at its chapter. It
teaches nothing. It loans nothing. It exists so that when I need to tell you
a hazard is coming, I can name the hazard without pretending you've already
met it.

Like this:

> **Preview note.** The customary-units treatment of force and mass is the
> sharpest edge on this exam, and it gets its own full development in
> Chapter 01-02. For now, all you need is the awareness that it's there.

The rule of thumb: if you have to *use* something to finish the chapter, it
gets a primer. If you only have to *know it's coming*, it gets a preview
note.

---

## 0.7 Three Kinds of Review Question

Every chapter ends with three kinds of question, and they are not
interchangeable.

| | **Conceptual** | **Calculation** | **Multiple Choice** |
|---|---|---|---|
| Tests | Do you understand it | Can you do it | Can you do it their way |
| Calculator | No | Yes | Yes |
| Handbook | No | Yes | Yes |
| Format | Short answer | Show your work | Four choices |
| Timing | Untimed | Work carefully | ~3 minutes each |

Conceptual questions ask things like *which assumption fails here*, *what
happens to this when that doubles*, *why is the sign negative*. You can't
calculate your way through them. Either the idea landed or it didn't.

Here's why I separate them. It is entirely possible to grind through a
procedure correctly, get the right number, and have no idea what you just
did. That works right up until the exam changes the setup slightly and your
memorized procedure doesn't fit. Then you're stuck — and stuck in a way that
working more problems won't fix.

So: conceptual questions first. If you can't answer one, the answer key
tells you which section to reread. Go reread it. Then do the calculations.

Then do the multiple choice, because that's the format you'll actually face,
and the FE's distractors are built specifically to catch people who did the
math right and read the question wrong.

|-----------|
|> **Mentor's Margin:** Don't skip the conceptual questions because they look|
|> easier. They aren't easier. They're quieter. And write your answers down on|
|> paper before you check the key — the act of producing an answer builds|
|> memory in a way that recognizing one never will.|
|-----------|
---

## 0.8 The Three Levels of Examination

**Test-out quizzes.** Short diagnostics at the front of each tier. Twelve to
twenty questions. Pass it and skip the tier — you already know the material
and you don't need me walking you through it. Fail it and you've learned
something valuable for the cost of fifteen minutes.

Use these. Especially in Layer 1. If you've got recent calculus, testing out
of Tier 1C saves you ten chapters and about three weeks.

**Tier review exams.** Twelve of them, one per tier, at the end of the tier.
Twenty to forty-five questions, timed. Every question maps back to the
chapter it came from, so a wrong answer isn't a vague instruction to study
harder — it's a specific chapter to reread.

Take these seriously. A tier review is the last checkpoint before that
material becomes the foundation for something else. Weak spots here compound.

**Full practice exams.** Two per discipline, fourteen in all. 110 questions,
six hours, built to the same blueprint proportions as the real exam. Each
comes with a quick answer key, full worked solutions, a blueprint showing
which knowledge area every question tested, and a scoring guide that turns
your results into a reading list.

**Version A is diagnostic.** Take it *before* you start your discipline
track, so you know where you stand and what to prioritize.

**Version B is simulation.** Take it cold, timed, in one sitting, no
interruptions, when you think you're ready. That number is the most honest
estimate you'll get.

|-----------|
|> **Mentor's Margin:** You will not feel ready. Nobody feels ready. Take|
|> Version A early, while a bad score is still information instead of a|
|> verdict. A rough result in month one tells you where to work. A rough|
|> result in week fifty-one is a problem.|
|-----------|
---

## 0.9 Where This Goes Wrong

Ways people misuse this guide. I've watched every one of them happen.

**Skipping Layer 1 because it looks basic.** The first three chapters cover
units, unit conversion, and significant figures. It looks like grade school.
It is not. There's a distinction in there, in the customary units, between
two quantities that sound like the same thing and aren't — and it costs more
exam points than any other single topic in the foundation. It costs those
points from people who were certain they already knew units. Take the
test-out quiz. If you pass, skip freely. Don't skip on confidence alone.

> **Preview note.** That distinction is pound-mass versus pound-force, and
> the conversion constant that connects them. Chapter 01-02 develops all
> three from scratch. You don't need them yet — you only need to know that a
> chapter titled "units" is not a chapter you skip on instinct.

**Reading without working.** You can read this entire guide and pass
nothing. Engineering knowledge doesn't transfer by reading. It transfers by
doing the problem, getting it wrong, and finding out why. The worked
examples are a demonstration of a method you're about to have to execute
yourself. Cover the solution with your hand and try it first.

**Treating optional chapters as forbidden.** Off-route chapters aren't
banned. They're just not required. If your exam doesn't need thermodynamics
but you want to know how a refrigerator actually works, go read it. The
prerequisites are listed. Curiosity isn't a detour from becoming an
engineer — it's most of the job.

**Studying by fear instead of by dependency.** The temptation is to attack
your scariest exam topic first. Resist it. If your weakness is geotechnical
engineering, and geotechnical stands on mechanics of materials, which stands
on statics, which stands on vectors, then charging straight at geotechnical
is how you end up memorizing formulas you can't reason about. Follow the
route. It's ordered for a reason.

**Skipping a tier because the *title* looks irrelevant.** The skip decision
belongs to your route map and your test-out quiz, not to your reaction to a
tier name. A route map skip is derived from your specification. A hunch
isn't.

**Cramming.** Sleep consolidates learning. All-nighters produce short-term
memory that evaporates in hour four of a six-hour exam. This is not
motivational advice; it's how the machinery works.

---

## 0.10 Your First Week

Orientation is worth nothing until it turns into motion. Here is the whole
first week, in order. None of it is studying. All of it is setup that pays
back for a year.

**Day one — decide what you're taking.** Chapter 00-02 lists the seven exams
and how to choose between them. Read it, then commit to one.

**Day one — download your specification.** Go to ncees.org, get the current
exam specification for the discipline you chose, and print it. Two to four
pages. Put it where you study. It is the most valuable free document NCEES
publishes and it is the source this entire guide was built from.

**Day two — find your route map.** `routes/route-<your-discipline>.md`. Read
it end to end. You'll see which tiers you're taking and which you're
skipping, and roughly how long the path is.

**Day two — read your state board's rules.** Their website, their published
requirements, not a forum post. Twenty minutes. Chapter 00-02 explains why
this is the board's call and not NCEES's.

**Day three — buy your calculator.** From the current NCEES approved list,
which you should check the same day you buy. Then use that calculator for
every calculation in this guide, starting with Chapter 01-01. Fluency is
worth real points and it takes months, not days.

**Day four — take the Tier 1A test-out quiz.** Fifteen minutes. It tells you
whether you start at Chapter 01-01 or at Tier 1B. Either answer is useful.

**Day five — take the free NCEES practice exam.** Not for the score. For the
interface. It's the only authoritative preview of what the screen looks like,
how the on-screen Handbook behaves, and where the flag and timer live.

**Day six — schedule something.** Either your exam appointment or a
provisional target date. Chapter 00-02 makes the case for doing this earlier
than feels comfortable.

**Day seven — start Chapter 01-01**, or wherever your test-out result put
you.

|-----------|
|> **Mentor's Margin:** Notice that Practice Exam A isn't in that list. It|
|> comes later, right before your discipline track, once you've got the shared|
|> foundation under you. The NCEES practice exam in day five is a different|
|> instrument with a different job: it's a tour of the building, not a|
|> measurement of you.|
|-----------|

---

## Key Terms

| Term | Definition |
|---|---|
| Layer | One of the five major parts of this guide; read in order |
| Tier | A lettered group of related chapters in Layer 1 or 2, taken or skipped as a unit |
| Prerequisite | A specific earlier chapter that a given chapter stands on |
| Route map | The ordered reading path for one discipline |
| Skip-if line | The note in each chapter's Before You Start block stating whether it's on your route |
| Primer | A minimal loan of a later tool, used only when a chapter can't be reordered |
| Preview note | A one-or-two-sentence flag naming a concept that arrives in a later chapter, teaching nothing |
| Illustrative mention | A name used purely as an example of a category, which nothing in the chapter depends on |
| Test-out quiz | A short diagnostic at the front of a tier; passing lets you skip the tier |
| Tier review exam | A timed exam at the end of a tier, mapped back to source chapters |
| Practice exam | A full 110-question, six-hour simulation; two per discipline |
| Version A / Version B | Diagnostic and simulation forms of the practice exam |
| Forward reference | Use of a concept before the chapter that teaches it; prohibited and machine-checked |

---

## Review Questions

### Conceptual

1. State the central promise this guide makes about the order in which
   material appears.
2. Why is that promise enforced by a script rather than by careful editing?
3. Why is this guide layered instead of published as seven separate books?
4. What is a tier, and what problem does grouping chapters into tiers solve?
5. You open an off-route chapter out of curiosity and don't understand the
   first paragraph. What does the chapter give you to fix that, and where?
6. In every technical chapter, why does the idea come before the derivation?
7. What is the difference between a primer and a preview note? Give the test
   you'd use to decide which one a situation calls for.
8. Two review questions might cover the same topic — one conceptual, one
   calculation. What does each test that the other doesn't?
9. Which of the three examination types should you take *before* studying a
   tier, and what decision does it let you make?
10. Why does this guide show every result twice — once as derived, once as
    the Handbook prints it?
11. Two readers skip Tier 2D. One skipped it because their route map says to.
    The other skipped it because thermodynamics sounds hard. Both skipped the
    same eighteen chapters. Why is only one of those decisions safe, and what
    would you tell the second reader to do?
12. A reader passes the Tier 1A test-out quiz but hasn't looked at units in
    eleven years. Section §0.9 says not to skip Layer 1 on confidence alone.
    Does the quiz result count as confidence, or as evidence? Explain the
    distinction the guide is drawing.

### Calculation

None. This chapter has no computation. Your first calculations arrive in
Chapter 01-01.

### Multiple Choice

13. The prohibition on using a concept before it is taught is enforced by:
    A) Careful editing and peer review
    B) A build-time script that fails if a term appears before its definition
    C) A reader-reported errata process
    D) The prerequisite lists at the top of each chapter

14. A reader sitting for the Electrical & Computer exam should:
    A) Read all six Layer 2 tiers
    B) Skip Tiers 2C and 2D entirely
    C) Skip Layer 1 and begin at Layer 2
    D) Read only Layer 3

15. The purpose of a test-out quiz is to:
    A) Assign a grade for the tier
    B) Determine whether you can skip the tier
    C) Simulate exam conditions
    D) Replace the tier review exam

16. Practice Exam Version A should be taken:
    A) After finishing your discipline track, as a final check
    B) Before starting your discipline track, as a diagnostic
    C) Only if you fail Version B
    D) On the same day as Version B

17. A primer exists to:
    A) Summarize a chapter before you read it
    B) Provide the minimum of a later tool needed to finish the current chapter
    C) Replace a chapter you've chosen to skip
    D) Collect formulas for exam-day reference

18. Which of the following is the correct use of a preview note?
    A) Teaching a later concept in compressed form so the reader can use it now
    B) Naming a concept that arrives later, with no expectation that the
       reader can use it
    C) Listing the prerequisites a chapter stands on
    D) Flagging an error found after publication

---

## Answer Key with Explanations

**1.** Nothing is used before it's taught. Every term, symbol, and equation
first appears in a chapter that builds it from earlier material, and the
first chapter builds on arithmetic alone. The two narrow exceptions —
illustrative mentions and explicitly flagged primers and preview notes — are
both named in the chapter and neither requires knowledge the reader doesn't
have. (§On the Board Today, §0.6)

**2.** Because carefulness doesn't scale across a guide this size. A script
checks every technical term in every chapter against the master concept list
and refuses to build the guide if a term appears before its defining chapter.
A machine catches what an editor's attention eventually won't. (§On the Board
Today)

**3.** The seven FE exams share roughly half their content. One book for all
seven is bloated for every reader; seven separate books mean writing the
same shared chapters — statistics, ethics, economics — seven times over.
Layering writes the shared material once and separates only what actually
differs. (§On the Board Today)

**4.** A tier is a lettered group of related chapters in Layer 1 or Layer 2,
taken or skipped as a unit. Grouping makes skipping *clean*: you skip a
whole coherent subject with confidence rather than picking through
individual chapters hoping none of them mattered. (§0.2)

**5.** Its prerequisites list, in the Before You Start block at the top of
the chapter, naming the specific earlier chapters it stands on by number.
Read those, then come back. (§0.3)

**6.** So that the derivation is something you follow rather than something
you trust. The idea section explains what's physically happening with no
equations; the derivation then has somewhere to land. Handing a reader an
equation first teaches memorization, not understanding. (§0.5)

**7.** A **primer** is a minimal loan of a later tool — symbols, units, only
the calculations the current chapter needs, one worked example, and a
statement of where the full treatment lives. A **preview note** is one or two
sentences naming a later concept and why it matters; it teaches nothing and
loans nothing. The test: if you have to *use* the thing to finish the
chapter, it's a primer. If you only have to know it's coming, it's a preview
note. (§0.6)

**8.** The conceptual question tests whether the idea landed — it can't be
answered by computation and needs no calculator. The calculation question
tests whether you can execute the procedure. Getting the number right
doesn't prove you understood it; understanding it doesn't prove you can
produce it in three minutes. (§0.7)

**9.** The test-out quiz, at the front of each tier. Passing means you can
skip the tier; failing means the tier is worth your time, and you found that
out for about fifteen minutes of cost. (§0.8)

**10.** Because the *FE Reference Handbook* is the only resource you get on
exam day. You'll be reading the Handbook's notation under time pressure, not
this guide's. Where the two differ, the guide shows both so there's no
surprise in the testing center. (§0.5)

**11.** The first skip is derived from the reader's NCEES exam
specification — the route map exists because someone mapped the
specification's knowledge areas onto tiers. Nothing in Tier 2D appears on
that exam, so the eighteen chapters are genuinely unnecessary. The second
skip is derived from a feeling about a word. Those two decisions produce the
same action and carry completely different risk. Tell the second reader to
open their route map and their specification and find out whether the skip is
actually theirs to make. If it is, skip freely. If it isn't, they were about
to remove eighteen chapters of tested material on the strength of a hunch.
(§0.2, §0.9)

**12.** It counts as **evidence**, and that's the whole point of the quiz
existing. The guide's objection is to skipping on *self-assessment* —
"units, sure, I know units" — which is unreliable precisely because the
material looks more familiar than it is. A quiz result is an external
measurement of the same question. Section §0.9 says "take the test-out quiz;
if you pass, skip freely," which is exactly this distinction: confidence is
not permission, a passing score is. If the eleven-year gap makes the reader
uneasy, the cheap resolution is to work Chapter 01-02 anyway — it's the
highest-leverage chapter in the foundation and it costs an afternoon.
(§0.8, §0.9)

**13. B — a build-time script** that fails if a term appears before its
definition. (A) is what the chapter explicitly says isn't sufficient: careful
editing doesn't scale. (C) is reactive — errata fix a book after readers are
already hurt by it. (D) is tempting and wrong: prerequisite lists tell a
*reader* what to go read, which is navigation, not enforcement. They can't
detect a violation because they're written by the same person who wrote the
violation. (§On the Board Today)

**14. B — skip Tiers 2C and 2D entirely**, on the strength of the
specification, which contains no statics, dynamics, mechanics of materials,
fluids, thermodynamics, or heat transfer. (A) means reading thirty-seven
chapters the exam doesn't test. (C) inverts the design — Layer 1 is the
mathematical substrate every route requires, and it's the one layer nobody
skips wholesale. (D) leaves the discipline track standing on prerequisites
the reader never met, which is the exact failure the layering exists to
prevent. (§0.2)

**15. B — determine whether you can skip the tier.** (A) misreads the
instrument: nothing in this guide is graded, and a test-out quiz produces a
routing decision, not a score you keep. (C) describes Practice Exam B, which
is timed, six hours, and taken cold. (D) confuses the two ends of a tier —
the test-out quiz runs *before* to let you skip, the tier review runs *after*
to find weak spots. They're different instruments pointing opposite
directions. (§0.8)

**16. B — before starting your discipline track, as a diagnostic.** (A)
describes Version B's job. (C) inverts the sequence: A comes first precisely
so that B can be a clean measurement later, and using A only as a
consolation prize wastes it. (D) defeats both purposes at once — A's value is
that it's early enough for the result to be actionable, and B's value is that
it's cold. Taking them the same day gives you two contaminated numbers
instead of one honest one. (§0.8)

**17. B — provide the minimum of a later tool needed to finish the current
chapter.** (A) describes something this guide doesn't do; the *On the Board
Today* section states purpose, not content. (C) is the most common
misunderstanding: a primer is a loan against a chapter you'll still read
later, not a substitute for one you skipped. (D) describes the Quick
Reference card and the Reference part of the guide. (§0.6)

**18. B — naming a concept that arrives later, with no expectation that the
reader can use it.** (A) describes a primer, which is the heavier device and
the one that carries actual content. (C) describes the prerequisites list,
which points backward at chapters already written; a preview note points
forward. (D) describes errata. The distinguishing feature of a preview note
is that nothing in the chapter depends on it — remove it and the chapter
still works, you're just less warned. (§0.6)

---

## Quick Reference

**Structure**

Layer 0 orientation → Layer 1 math substrate → Layer 2 core engineering →
Layer 3 discipline track → Reference

Layer 2 tiers: 2A professional · 2B physical science & safety · 2C mechanics
· 2D thermal-fluids · 2E electrical · 2F measurement & control

**The core promise**

No concept used before it's taught. Enforced at build time. Prerequisites
listed by chapter number. Exceptions are illustrative mentions, primers, and
preview notes — all explicitly marked.

**Navigation**

Find your route map in `routes/` before reading anything else. Every
chapter's skip-if line tells you whether it's yours. Off-route chapters are
optional, not forbidden — prerequisites are listed.

**Chapter anatomy** *(17 sections)*

Epigraph → Before You Start → On the Board Today → Objectives → [Primer] →
Notation → Idea → Derivation → Handbook form → Source verification → Worked
examples → Where this goes wrong → Key terms → Review questions → Answer key
→ Quick reference → What's next

Mentor's Margin is scattered, not sequential.

**Primer vs preview note**

Have to *use* it to finish the chapter → primer. Only have to know it's
coming → preview note.

**Assessment**

| Type | When | Purpose |
|---|---|---|
| Test-out quiz | Before a tier | Skip what you already know |
| Tier review exam | After a tier | Find weak spots before they compound |
| Practice Exam A | Before your track | Diagnostic |
| Practice Exam B | When you think you're ready | Honest readiness estimate |

**First week**

Choose your exam · download the specification · find your route map · read
your state board's rules · buy an approved calculator · take the Tier 1A
test-out quiz · take the free NCEES practice exam · schedule a date · start
Chapter 01-01

**Habits that decide the outcome**

Take the test-out quizzes. Work the problems, don't read them. Write answers
on paper before checking the key. Read "Where This Goes Wrong" twice. Take
Version A early. Follow the route, not your fear. Sleep.

---

## What's Next

Apprentice, you now know how this guide is built and how to move through it.
That's not engineering yet — but it's the difference between a year of
efficient work and a year of thrashing.

In **Chapter 00-02: The Exam and the CBT Format**, we'll look at what exam
day actually consists of.

Then in **Chapter 00-03: Navigating the FE Reference Handbook**, we tackle
the most underestimated skill in FE preparation.

Go find your route map. Then meet me in 00-02.

— Your Mentor
