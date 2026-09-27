# Style Guide

Every rule here exists because breaking it would either violate the
zero-forward-reference constraint or fail a reader with no college
background.
## Voice: the mentor's bench

The reader is an apprentice. You are the mentor beside them — someone who
has done the work, respects the person learning it, and has decided to hand
over what they know without making them feel small for not knowing it yet.

### The persona carries forward

Same mentor as *The Mentor's Bench*. Two decades as a military medic
teaching medics, nurses, and doctors, then Bachelor's degrees in Electrical
Engineering and Computer Engineering. The credential that matters is the
second one; the *skill* that matters is the first. This mentor is candid
about what he is and isn't: not a thirty-year field veteran, but someone
with deep formal training and a career built on making technical material
land with people who had to actually understand it.

That honesty is part of the voice. Never claim experience you don't have.
Name the limit and then explain why it doesn't matter for the task at hand.

### What it sounds like

| Do | Don't |
|---|---|
| "Apprentice, let me show you why this matters." | "Welcome to Chapter 1!" |
| "I'm going to be honest with you: this is the chapter most students want to skip." | "This section is often overlooked." |
| "Burn that into your memory." | "This is important to remember." |
| "Spend a real week with this chapter." | "Take your time with this material." |
| "Get out your calculator. Today we make this familiar." | "Let us now examine…" |
| "Bring your curiosity. Leave your fear of math at the door." | "Prerequisites: basic algebra." |
| "See you there." | "Proceed to the next chapter." |

### Rules

1. **Direct address, warmly.** "Apprentice" opens chapters and major
   sections. Second person throughout: "you" and "we."
2. **Say why before what.** Every chapter opens by explaining the purpose
   of the material before teaching any of it.
3. **Name difficulty out loud.** "This one trips people up, so we'll go
   slow." Pretending a hard thing is easy makes a struggling reader think
   the problem is them.
4. **Explain the reason behind the rule.** Not "always draw a free-body
   diagram" but "draw it because the sign errors you make in your head are
   the ones you never catch."
5. **Analogies that connect to what the reader already has.** Water in
   pipes for current. Pressure for voltage. Use them, then say plainly
   where the analogy breaks.
6. **Mnemonics are welcome.** If a memory trick works, teach it.
7. **History, sparingly, when it teaches.** Ørsted's compass needle.
   Bardeen, Brattain, and Shockley. Two sentences, then back to work.
8. **Make promises and keep them.** "I promise you two things." The reader
   is trusting you with a year of their life and a career gate.
9. **Earned encouragement.** No praise before work is done. When the reader
   has done something hard, say so and move on.
10. **Respect the exam.** It is genuinely hard and their career depends on
    it. Never condescend about it, and never pretend it's easy.
11. **Em-dashes are fine.** So is the occasional exclamation point. The
    voice is warm, not clipped.

### The one thing to avoid

Cheerfulness substituting for clarity. Warmth does not rescue a paragraph
that could be clearer. The kindest thing a mentor does is explain well.

## Recurring structural devices

Carried over from *The Mentor's Bench*, unchanged unless noted.

**Epigraph.** Every chapter opens with a short quoted aphorism in the
mentor's voice that captures the chapter's stake.

**On the Board Today.** *(Renamed from "On the Bench Today" — FE candidates
work at a desk, not a bench. Say the word if you'd rather keep continuity
with the original name.)* Frames what the chapter is about and why it
matters, in the mentor's voice, before any technical content.

**Learning Objectives.** Numbered, mapped to NCEES specification line items
exactly as the CETa book mapped to ETA competencies.

**Primer.** *(Adopted wholesale — see below.)*

**Mentor's Margin.** Boxed asides carrying field-tested advice, a warning
about a common mistake, a shortcut, or a story. Rendered as a blockquote
with a bolded label.

**Worked Example N — Descriptive Title.** Problem, then numbered steps with
units carried through every line, then a **Verify** or **Check** step. The
verification step is mandatory; it teaches the habit that catches errors
under exam pressure.

**Key Terms.** Two-column table at chapter end. Every term defined in the
chapter appears here.

**Review Questions**, in three parts:

| Part | Tests | Calculator | Handbook | Count |
|---|---|---|---|---|
| **Conceptual** | Understanding | No | No | 5–10 |
| **Calculation** | Procedural fluency | Yes | Yes | 5–10 |
| **Multiple Choice** | Exam format | Yes | Yes | 5–10 |

**Answer Key with Explanations.** One key covering all three parts. Every
answer explained, including why the distractors are wrong. Even correct
answers get an explanation.

**Quick Reference.** Formula-dense one-page review block, where the chapter
has formulas.

**What's Next.** Closes every chapter. Names what was just built, names
what the next chapter builds on it, and sends the reader forward.

## The Primer device

*The Mentor's Bench* solved the forward-reference problem before I did, and
its solution is better than mine. Chapter 1 needs Ohm's law before Chapter 2
teaches it, so it opens with a **Safety Math Primer — Read This First**:
symbols, units, exactly the three calculations needed, one worked example,
and an explicit statement that the full development comes later.

This is now the sanctioned mechanism for the rare case where a chapter
genuinely needs a tool ahead of its home chapter. Rules:

1. A Primer is a **last resort**, not a convenience. Reorder chapters first.
   The dependency graph exists to make Primers unnecessary.
2. A Primer teaches only what the current chapter needs. Nothing more.
3. It states plainly where the full treatment lives:
   *"Chapter 02-23 develops equilibrium fully. In this chapter, use ΣF = 0
   only as a bookkeeping tool."*
4. It carries at least one worked example.
5. Every Primer is registered in the ledger as a `primer: true` entry with
   its own concept ID, so `lint_forward_refs.py` treats the borrowed terms
   as defined at the Primer, not at the later chapter.
6. **Inline preview notes** handle the smaller case — a single sentence
   naming a concept that arrives later, marked as such:
   *"Preview note: full-wave rectification is explained in Chapter 18. Here
   the center tap is introduced only as a transformer connection."*

`check_primers.py` is added to the toolchain: it fails the build if a Primer
teaches material beyond what the chapter's ledger entries actually require.

## FE-specific additions

Two sections the CETa book has no need for, because that exam is closed-book
with no reference.

**As the Handbook States It.** The FE gives you the *FE Reference Handbook*
and nothing else. So every result gets shown twice: once as the guide
derives it, once in the exact form and notation the Handbook prints, with
the page number. When the guide's notation differs from the Handbook's, say
so and show both.

**Where This Goes Wrong.** *The Mentor's Bench* distributes common errors
into Mentor's Margin boxes. The FE book keeps those *and* adds a dedicated
section, because six hours of time pressure across 110 questions makes error
patterns worth concentrating in one place the reader can reread the night
before.

## Teaching order inside a chapter

Non-negotiable, and it is the local version of the global constraint:

1. **Physical or intuitive idea first, no equations.** What is happening
   and why anyone cares.
2. **Then the derivation**, every step justified by something already
   taught. When a step uses a prerequisite, link it inline on first use.
3. **Then the Handbook form**, with page and any notation difference
   stated.
4. **Then examples**, warm-up to exam-level.

A chapter that opens with an equation has failed the zero-baseline
requirement.

## Prerequisite discipline

- Every technical term is either defined in the current chapter or links
  to the chapter that defines it. There is no third option.
- Link on first use per chapter, not every use.
- Link format: `[02-23 Equilibrium of rigid bodies](path)` — number and
  title, so the reader knows where they are being sent before clicking.
- Forward links appear **only** in section 9, *Going further*, and only
  when marked optional.

## Notation

- Chapter banner is mandatory. See `meta/notation.md` Rule 6.
- Variables italic, units upright, always.
- Introduce a symbol in the banner before its first appearance in prose.

## Mathematics presentation

- Every derivation step gets a one-line justification.
- Inline math for single symbols and short expressions.
- Display math for anything a reader would need to parse twice.
- Number displayed equations only when referenced later.
- State assumptions before the equation that depends on them, never after.

## Worked examples

Fixed five-part structure. Skipping a part is the most common way an
example stops teaching and starts merely demonstrating.

```markdown
### Example 2 — Reaction at a pinned support

**Given.** ...
**Find.** ...
**Approach.** {one or two sentences, before any arithmetic}
**Solution.** {numbered steps, units carried through every line}
**Check.** {order of magnitude, sign, limiting case, or units}
```

The **Check** step is mandatory. It teaches the habit that catches errors
under exam pressure.

## Review questions vs practice problems

| | Review questions (§6) | Practice problems (§7) |
|---|---|---|
| Tests | conceptual understanding | procedural fluency |
| Calculator | no | yes |
| Handbook | no | yes |
| Count | 10–15 | 8–12 |
| Answer form | short answer + section link | full worked solution |
| Timing | untimed | 3 min per item |

Review questions must be answerable from the chapter alone with no
computation. Good forms: "which assumption fails if…", "what happens to X
when Y doubles", "why is the sign negative here", "name the condition
that makes this equation invalid."

## Units in problems

Mixed SI and USCS across the problem set, matching the exam. Roughly 60/40
SI to USCS. Every USCS problem involving force or mass exercises `g_c`,
because that is where readers lose points.

## Handbook references

- Format: `> **Handbook 10.6, p. 98** — *Statics*`
- Set `handbook_verified: true` in the ledger only after confirming the
  page against the PDF. Section start pages are verified; interior pages
  are inferred until checked.
- When the guide's notation differs from the Handbook's, say so in
  section 3 and show both forms.

## The memorize flag

Every ledger entry sets `memorize: true` or `false`. True means the
content is **not** in the Handbook and must be known cold. These are
collected into a master memorization list in the Reference part. This flag
is the practical payoff of Handbook 10.6's own statement that basic
theories, conversions, formulas, and definitions are omitted.

## Accessibility

- Every figure has alt text describing the physical situation, not just
  naming it. "Free-body diagram of a beam with a pin support at the left
  end and a roller at the right, carrying a downward point load at
  midspan" — not "Figure 2."
- Never convey information by color alone.
- Tables get header rows. No merged cells.
- Heading levels descend without skipping.
- Math is authored so it renders as text, not images.

## File naming

`{chapter-number}-{kebab-case-title}.md` — `02-24-trusses.md`

## Front matter

```yaml
---
chapter: "02-24"
title: "Trusses"
layer: 2
tier: C
ledger_ids: [MECH-2C-024-01, MECH-2C-024-02]
routes: [civil, mechanical, other-disciplines]
status: planned
---
```

`routes` drives the skip banner. `ledger_ids` lets the linter know which
concepts this file is responsible for defining.

## Prohibited constructions

| Don't write | Write instead |
|-------------|---------------|
| "As you know from physics…" | link to the chapter that teaches it |
| "It can be shown that…" | show it, or link to where it is shown |
| "Recall the standard result…" | link, or derive |
| "This is beyond the scope…" | move it to §9 *Going further* |
| "See any textbook on…" | give the chapter, or cut the claim |
| "Obviously / clearly / simply" | delete the word |