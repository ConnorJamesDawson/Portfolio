# Character-state continuity — findings

*Answers the brief in `continuity-methods-prompt.md`. Read §1 first; it
disagrees with the brief's own framing, and the disagreement changes what
should be built.*

---

## 0. Research conditions — read before trusting any citation

This ran under a **restricted network egress policy**, and it damaged the
craft half of the brief badly enough that you should discount it there.

- **`WebSearch` worked.** **`WebFetch` was blocked for most of the open
  web** — `en.wikipedia.org`, `arxiv.org`, `aclanthology.org`, `jair.org`,
  `coppermind.net`, `theoryland.com`, `*.fandom.com`,
  `chicagomanualofstyle.org`,
  `ciep.uk`, `the-efa.org`, `hollylisle.com`, `bladesinthedark.com` all
  returned `403` at the CONNECT tunnel. The session-wide search budget was
  also exhausted (200/200) partway through.
- **What stayed reachable was `github.com` and `raw.githubusercontent.com`.**
  So the strongest-sourced material below is whatever keeps its primary text
  in git — specifications, engine source, compiler documentation. That is a
  real bias and it runs the wrong way for questions 1, 2, 3 and 6.
- **Consequence, stated plainly.** Four of the ten areas searched —
  **series bibles, TV writers' rooms, the who-knows-what-when matrix, and the
  craft literature on timing** — returned **zero pages actually opened**.
  Everything reported from those four is search-summary or training-data
  recall, and is marked as such. Do not quote them at a page number.
  **They deserve a re-run on an unrestricted connection.**

**One evidential hole is more important than any of that.** Across roughly
sixty practices surveyed, **not one came with a field report of it actually
catching a premature-capability error in real production.** The corpus has
descriptions, schemas and source code, and exactly one spectacular *negative*
field report (Sanderson, below). Every "would have caught it" verdict here,
mine included, is a reconstruction. Treat the ranking as an argument, not as
evidence, and instrument whatever you adopt so it produces its own record.

---

## 1. Where I disagree with the framing

> *"Strong event bookkeeping, strong rule bookkeeping, no state
> bookkeeping."*

**That names the right absence and draws the wrong conclusion from it.** The
missing artifact is not a table of what a character possesses at month N. It
is **a line in each scene's plan declaring what that scene needs to be
already true.** State is the vocabulary; the requirement is the check.

### The evidence that decides it

Sort every practice found by what its artifact is *keyed on*.

**Character-keyed artifacts — every one scores `no` against the creed
error.** The production-bible character profile; the Lucasfilm Holocron; the
copyeditor's character register; fan-wiki character pages; Marvel's handbook
cards; Jordan's per-entity file database; append-only entity-state ledgers
with as-of-story-time snapshots; a bitemporal truth store with time-travel
queries; a `knows`/`unaware_of` schema; three-array state files. Zero for
twelve.

That list is not a gap in the literature. **It is your proposal, built
independently at least four times, scoring zero every time.** Two of those
four are precisely the thing the brief asks for — event-sourced dated state
changes, fold-to-any-month queries — and neither built a check on top of the
store. The ledger is the easy half.

**Scene-keyed requirement declarations — this is where the `yes` verdicts
live.** The storylet `requires:`/`grants:` header is the single practice in
the whole corpus rated *established craft* **and** `caught: yes`, verified
against engine source. Declared preconditions with a reachability check:
yes. The script supervisor's story-day breakdown with forward-propagated
carried-in state: yes. Gramps' `UnbornParent` rule: yes. The invariant
quantified over months: yes.

And the honest verifier on the long-series-authors question, who thought the
brief's hypothesis was *confirmed*, wrote the sentence that refutes it:

> **"nothing anywhere in the documented field asks what a scene requires."**

### Your own files already say this

`falsified.md` #16 killed the local patch — *she lives on geometry*, the
child's position in the building — and the entry's closing note is the
finding:

> **"The pattern is not caution about power. It is reaching for a mechanism
> when the answer was in the calendar"** — and the calendar was already
> written: `timeline.md` had her in that cellar for two months before any of
> this was drafted.

**The state data was not missing. It was underived and unqueried.**
`timeline.md` held every fact needed to catch the creed error eight months
before it was made. Nothing forced a comparison, because nothing in the
design system ever makes a *claim* on the world that could be contradicted.

### The generalisation, which is the actual diagnosis

Look at the tense of every artifact this project owns. The event timeline:
recorded **after** drafting. "Revised on the page": written **after**. The
falsification ledger: fires **after** a rule has died on the page. The
watch list: rules already under pressure. The only prospective artifact is
the per-chapter design plan, and it plans **beats**.

> **This project has a complete adjudication stack and no detection stack.**

A falsification ledger is an excellent post-mortem instrument and a
categorically wrong prevention instrument. Keep it. Stop expecting it to
prevent anything.

### The other four candidate causes, judged

- **Granularity — false, and the worked example kills it.** Both facts were
  already on the tracked timeline, eight months apart, at month resolution,
  in a tracked thread. Weekly resolution prints the same two rows further
  apart. The untracked third thread is a real exposure and worth fixing; it
  is not this cause, and fixing it would not have caught the creed.
- **The missing sequel (Swain) — a good account of the drift, a bad account
  of the failure.** It explains the *pull* that drags an acquisition toward
  whatever scene can dramatise it. It supplies no *pointer*: install sequels
  everywhere and still nothing directs attention to month 12 of year 0. Keep
  sequels as the repair site once a date moves. They are not the detector.
- **Authority (failure C) — the second-most-important finding, and still not
  the cause.** Marking the creed's date `INFERRED` would have changed nothing
  at plan time; provenance is a property of a row, not a scan. What it
  actually fixes is **B**: a ruled date deserves a local patch, an inferred
  one deserves to move, and without the marking every argument about which is
  a matter of taste — and taste favours the cheaper patch. **C is the correct
  medicine for B.**
- **Maintenance economics — survive, and they indict the state-table
  proposal.** A per-character state document over three threads at 20k words
  a chapter will rot, and a rotted state table is worse than none because it
  reads as authoritative. The archetype's own testimony, verified this
  session:

  > "I have a database. Yes… a huge collection of files organized on
  > characters, on cultures, um (pause) organizations, anything that I think
  > I might need to know about the world. **But to tell you the truth, I
  > usually go into those files to add in new things that I've come up with.
  > It's not that often that I go in there to check on things.**"
  > — Robert Jordan, Theoryland interview #128, 5 December 2000

  Maintained character-side documents are **write-mostly by nature**: they
  cost on every chapter and pay out only when someone chooses to look.
  Preconditions do not rot, because a stale one fails the check.

**So: if state is kept at all, it must be *derived*.** One append-only row
per acquisition; state at month N computed as a fold; never a second
hand-maintained document that can disagree with `timeline.md`.

### What follows

Three lines per scene in the chapter plan, written before drafting, over a
closed named vocabulary:

```
month:     0/12
requires:  creed_bound>=1, kit/blade, at/kadono-dera
grants:    —
```

An empty `requires:` is an error, not a default. One deterministic pass
asserts every required atom was granted at an earlier month. Plus the
**zero-count report**: every quality granted but never required — which is a
direct detector for failure mode A, because *a trait nothing depends on is a
trait that exists only to be shown off.*

**Against the worked example.** The month-12 plan must state what its outcome
presupposes: a berserker leaves a building with a child alive in it. The
truthful `requires:` is `creed_bound >= 1`. The ledger grants it eight months
later. The check prints scene, atom and both months, before a word is
drafted.

**The residual failure is real and must be said.** If nobody writes the
`requires` line, nothing fires. A plan declaring `requires: at/kadono-dera,
kit/blade` and omitting the governor passes clean and silent. The formalism
makes the question compulsory **in form, not in content**. The two mitigations
are the mandatory non-empty field and the zero-count report, which finds the
creed from the other end. That is a real and large win; it is not omniscience.

---

## 2. Ranked shortlist

Ranked by *what it would have done about the creed*, then by cost. Source
marks: **[verified]** = primary text fetched and read this session;
**[summary]** = search result only, page never opened; **[recall]** =
training data, unsourced.

---

### 1. `requires:` / `grants:` on every scene in the chapter plan

**The one recommendation. Everything else is support for it.**

**What it is.** A storylet is a chunk of narrative stored beside a
machine-readable *precondition* over named world state, and a *postcondition*
that mutates it. The load-bearing property is not the engine: the precondition
is **a first-class field, authored at the same moment as the plan, in the same
file, by the same person** — not a note elsewhere.

**Where from.** Coined at Failbetter Games (*Fallen London*); formalised by
Kreminski & Wardrip-Fruin, ICIDS 2018. Implementations: Dendry, ink,
SimpleQBN, StoryNexus, *Reigns*, *Ice-Bound*.

**Sources. [verified]** Kreminski & Wardrip-Fruin, "Sketching a Map of the
Storylets Design Space", ICIDS 2018 (PDF text extracted directly). Dendry
`doc/dry/scene.md` and `lib/engine.js` (field list real; semantics confirmed
in engine at lines 691, 708, 807–829). ink `WritingWithInk.md`. SimpleQBN
README.

**Cost.** 3–6 lines per scene → **20–40 minutes per chapter plan**. The real
bill is one-off: enumerating the quality vocabulary for book two — every
trait, rule, skill, possession, belief, relationship, oath, injury and
institutional fact any scene leans on. **Half a day to a day.** Budget for
inventing it; the exemplars do not have one you can copy.

**Acceptance test: YES** — the only unqualified yes in the corpus, on two
structural conditions:

1. The precondition is authored at **plan** time, never extracted from the
   draft afterwards. Extraction reproduces failure A exactly — the extractor
   reads the scene that shows the trait off and dates the trait there.
2. `requires:` means *what must be true before the first line of this scene*,
   not *what this scene demonstrates*. `requires: berserk_state` is the
   predictable AI failure and is wrong.

**Addresses:** A directly and mechanically; B partly; D — a compressed
connective scene still needs a header, so it gets the same scrutiny as a set
piece.

---

### 2. The acquisition ledger as a derived, append-only, valid-time table

**What it is.** Not a state document. **One append-only row per acquisition**
— attribute, character, story-month, acquiring event, provenance — with state
at month N computed as a fold, never maintained as a second document that can
disagree with `timeline.md`.

The formal name for the project's whole problem is **bitemporality**, and
having the name changes what is buildable. Two independent time axes:
**valid time** (when it is true in the story) and **system time** (when we
came to believe it).

> **"In short, any time you hear the phrase 'as of' or 'with effect from' in
> a requirement, the answer is probably 'valid time'."**
> — XTDB, `docs/…/time-in-xtdb.md` **[verified]**

The brief's own missing question — *"what does this character possess, know,
believe, and is bound by, **as of** month N"* — is a valid-time query,
verbatim. Restated precisely: **the project keeps system time for rules
(`falsified.md`) and valid time for nothing.**

**Where from.** SQL:2011 application-time period tables; standard across the
industry. Two hobby fiction tools reached for it independently, which is
corroboration that the standard answer fits.

**Cost.** Low **as a convention** — two columns and three named reads. High
if anyone installs a database, which nobody should. Markdown rows get 90% of
it; the 10% lost is query efficiency, which does not matter at one novel.

**Acceptance test: NO.** A schema does not detect. Adopting this alone, with
no checker, the creed error reaches the page exactly as it did. It is the
substrate items 1, 3 and 4 are unwritable without.

**The one rule that makes it work:** correcting an acquisition date is a
change to `valid_from` and **must never be done by editing the row in place**.
Append a new row; the old one stays. That is `falsified.md`'s "no rule dies
without a replacement" extended to state — and it makes failure B *more*
expensive than the correct move rather than cheaper, because the correct move
is one append and the patch requires inventing and defending a mechanism.

---

### 3. Write the check as an invariant over months, not a pass over scenes

**What it is.** Failure D says attention concentrates on beats and errors
concentrate in the compressed regions nobody re-reads. Every other remedy
answers this with *more attention* — another pass, another reviewer. This one
answers it structurally.

> "Often there are invariants that you want to ensure are met after every step
> in a process. It would be possible to add these as rules that are run, but
> **they would be run zero or multiple times between other rules.**"
> — Hypothesis, `docs/stateful.rst` **[verified]**

**The steal:** quantify over **months**, not over scenes.

> For every character, for every month M from the first month of the book to
> the last: every capability, possession, rule, belief and binding exercised
> by that character in month M has an acquisition month ≤ M.

The loop does not skip months in which nothing dramatic happens. That is the
entire difference from every review-pass practice found, and it is the same
predicate quantified differently — it costs nothing extra to write.

**The trap, and it matters.** Hypothesis also has `@precondition`, which
**filters** rather than fails: an unsatisfied precondition means *do not take
this step*. In a novel the step has already been taken. **The precondition
must be evaluated in its failing form, not its filtering form.** Get it
backwards and the checker silently skips the scenes it should be shouting
about.

**Where from.** HypothesisWorks/hypothesis, `stateful.py` `invariant()` line
1104, `precondition()` line 1027. **[verified]**

**Cost.** Very low given item 2 — a nested loop over months × characters.
Unimplementable without it.

**Acceptance test: YES**, and it is **the only practice in the corpus whose
catching mechanism is aimed at D rather than A.** It reports by **month**,
not by scene — `month 0/12: T exercises "governor/creed" (acquired 1/—)` —
and naming the interval is what makes the *timeline* the obvious repair
target rather than the scene. It catches the creed even if nobody ever
thought of the rescue as a scene worth checking, because it has no list of
scenes worth checking.

---

### 4. A small rule engine: severity, strict/loose modes, world
constants, and an adjudicated ignore file

**What it is.** Gramps — a twenty-year-old genealogy application — ships
*Tools → Verify the Data*: a rule engine over dated facts about people, 45
named rules, each a subclass with a `broken()` predicate and a one-line
message. A large fraction of them **are this project's failure mode A** — an
event whose participant lacks a prerequisite state at that date.

**`UnbornParent` is the creed error, already written:**

```python
class UnbornParent(FamilyRule):
    """test if each family's parent was not yet born at a child's birth"""
    ID = 24
    SEVERITY = Rule.ERROR
```

An actor performing a role requiring a state — being alive — they do not
acquire until later. `ERROR`, not warning. Message: `"Unborn father"`.

Four design features are worth more than the rule list:

- **Strict and loose modes over imprecise dates.** Every date is stored as a
  *pair*: index 0 counts only fully-known dates (few findings, no false
  positives); index 1 counts approximate ones too. This is what lets a checker
  run against a ledger where some acquisition dates are `ABT` or `BET…AND`
  without either ignoring them or drowning in noise. **Strict for the gate,
  loose for the review pass.**
- **World constants as tunable thresholds in one options block**, not
  hardcoded in rules.
- **Severity per rule, binary.** "Attribute relied on before acquisition" is
  ERROR and blocks; "acquired suspiciously close to first use" is WARNING.
- **A persistent adjudicated exceptions file**, keyed by rule id **plus the
  rule's parameters** plus the object — so settled questions stay settled, and
  **changing a threshold un-settles every exception that depended on it.**
  Nothing else found solves "the checker keeps raising things we already ruled
  on", which is the reason checkers get switched off.

**Where from.** `gramps-project/gramps`, `gramps/plugins/tool/verify.py`,
commit `a32b463`. **[verified]** — rule list at 1358–2605, `Rule` base at
1269, date pairs at 179–262, ignore persistence at 834–880.

**Cost.** Moderate, front-loaded, and the front-loading is unavoidable:
rules are worthless without item 2's ledger and item 1's declarations. Once
those exist the checker is small — Gramps' rules are 20–50 lines each and
this project needs perhaps six, not 45.

**Acceptance test: YES**, conditional on the ledger existing and the
prerequisite being declared. Output is a findings row: `ERROR | rule 1 | T |
month 0/12 | "governor/creed" not acquired until 1/— (CAL)`. Two dates and a
name, no prose. **Why it fires rather than being patched away:** ERROR blocks;
the ignore file demands a written reason rather than a silent local mechanism;
and because the acquisition date is marked calculated, the cheapest legitimate
resolution is to move the date, not to invent a governor substitute for one
scene. **That is failure B addressed structurally, not by exhortation.**

---

### 5. Graded certainty *inside* the constraint — and the AI may not
write the top level

**This is the answer to failure mode C, and it is one word per line.**

**What it is.** Inform marks the epistemic status of a constraint inside the
constraint. `A dead end is usually dark` is a **default** — exceptions
permitted, silent. `A dead end is always dark` is a **law** — the compiler
refuses to build any exception. And where Inform must *infer*, it explicitly
demotes the inference:

> "When Inform makes guesses like this, it treats them as being **less certain
> than anything explicitly stated in the source**. Inform will quietly
> overturn
> its assumption if information comes to hand which shows that it was wrong…
> These two sentences are not contradictory."
> — *Writing with Inform*, "Degrees of certainty" **[verified]**

**Two statements that contradict an inference are not an error — they are new
information.** Two statements that contradict each other, or contradict an
`always`, are a Problem naming **both** sentences.

**Why it beats every "mark your assumptions" convention:** the marking is
**not documentation *about* the constraint, it is *in* the constraint**, so it
cannot drift out of sync with it. That drift is what kills the conventions
that live in a separate file.

**Where from.** Graham Nelson / Inform 7, `Writing with Inform.md`, read from
the compiler repo. **[verified]**

**Cost.** Almost free and retrofittable: one leading keyword per line, half a
day of human passes one file at a time, one word per new constraint
thereafter.

**Acceptance test: NO — say so plainly.** A certainty marker on *"the creed is
acquired at eleven"* does not make its collision with an age-ten scene
visible. Nothing here scans, compares or reports.

**What it does instead** is remove the resistance to fixing it once found —
failure B — and prevent C from arising at all. Had the age-eleven dating been
marked inferred (because a strong scene sat there, not because you ruled it),
then when the collision surfaced, the correct move — move the date, absorb the
consequences — would have been the cheap and obvious one. **Overturning an
inference costs nothing and needs no `falsified.md` entry.** Marked as your
ruling, the same collision forces an explicit recorded ruling with a named
replacement. Either way the decision is made in the open.

---

### 6. Uncertainty encoded in the date itself

**What it is.** Genealogy has spent forty years on "what was true of this
person at time N, and how do I know", at a scale of millions of records, and
solved one piece the entire fiction corpus missed: **the acquisition date is
not required to be a point, and its epistemic status is part of its syntax.**

FamilySearch GEDCOM 7's date grammar, with the meanings given verbatim:

| Production | Meaning |
|---|---|
| `BET` *x* `AND` *y* | Exact date unknown, but no earlier than *x* / no later than *y*. |
| `BEF` *x* / `AFT` *x* | Exact date unknown, one-sided bound. |
| `ABT` *x* | Exact date unknown, but near *x*. |
| `CAL` *x* | ***x* is calculated from other data.** |
| `EST` *x* | Near *x*, and *x* is calculated from other data. |

**`CAL` is failure mode C solved in three characters.** It means: nobody
recorded this date; I derived it from other things I hold. It sits in the same
field as a ruled date, is machine-distinguishable from one, and is impossible
to write by accident.

**Where from.** `FamilySearch/GEDCOM`, `specification/gedcom-2-data-types.md`,
commit `126140c`. **[verified]** — ABNF and meaning table read in full.

**Cost.** Very low. A notation convention plus one line in the method file. No
tooling. Retrofit lazily: qualify a date the first time you touch it.

**Acceptance test: NO.** A notation detects nothing. But the creed line would
have read `CAL year-11` — calculated — and the question *"calculated from
what?"* becomes askable, with the honest answer (*"from where the good scene
sits"*) visibly not a reason. More usefully **the correct entry was always
`BET age-10 AND age-11`**, and under that entry the rescue at ten sits
*inside* the acquisition interval rather than safely before a point — a
visible unresolved question instead of a silent contradiction.

**It converts the error from invisible to inspectable. Item 3 raises it.**

---

### 7. Offscreen institutions as records with goals and progress counters

**What it is.** You were right that faction clocks are offscreen-state
advancement — but they are state *advancement with a counter*, not state
tracking, and the distinction matters. In Blades in the Dark the world's
institutions are not described in prose; they are records with a **stated
want, in the imperative, in under six words**, a **size** (4/6/8/12 segments —
an estimate of how much story it takes, declared in advance), a **progress
count**, and an explicit **`(repeating)`** marker for a goal that never
completes and generates pressure indefinitely.

Verified examples, from the shipped 43-record compendium: *The Crows, tier 2 —
"Reestablish control of Crow's Foot", 6 · "Rise in Tier", 6*; *Lord Scurlock,
tier 3 — "Fulfill debt to Setarra", 12 · "Obtain arcane secrets (repeating)",
6*; *The Lost, tier 1 — "Destroy cruel workhouses (repeating)", 4*.

"Why would this institution do this?" — the question failure D eats — is
**answered by construction, before play, for all 43.**

**Where from.** `megastruktur/foundryvtt-blades-in-the-dark`, `template.json`
and `packs/factions.db`, commit `1838f29`, CC-BY of John Harper's rules.
**[verified]** for the record shape and the 43 records. The GM's
between-session
advancement discipline is **[recall]** — `bladesinthedark.com` was blocked and
I am not citing it as verified.

**Cost.** An hour for a dozen institutions; a few minutes per chapter plan
thereafter. **The recurring cost is the point** — it is a forced touch of the
compressed regions.

**Acceptance test: NO. Not remotely.** The creed is an internal capability;
this apparatus models institutions and never looks at a person's attributes.
I report it because it was asked for, it is real, verified and cheap, and it
is **the only artifact found anywhere that treats the gaps between chapters as
having required content.** If you can afford one new artifact this is not it —
item 1 is.

---

### Scored and not recommended

| Practice | Verdict | Why not |
|---|---|---|
| The production/series bible character profile | `no` | A static prose paragraph re-versioned once a season. Asserts properties of a character, never of a character *at a time*. The negative control for the whole question. |
| Lucasfilm Holocron continuity database | `no` | Entities with a coarse era tag and an overwritten description. No time-indexed state field anywhere. Its canon letter records **canon tier, not epistemic provenance** — an adjudication mechanism, not a detection one, which is why Lucasfilm still needed a full-time administrator. |
| The beat board / season grid / screen-time grid | `no` | Track beats and appearances. Nothing carries what a character *has*. |
| Copyeditor's style sheet (character register) | `no` | Four independent implementations read; **no column anywhere records when a trait became true.** Its *query discipline* is worth stealing — see §3. |
| Fan-wiki per-character epoch architecture | `partly` | Prints an adjacency (scene date + active epoch), not a contradiction. No wiki convention carries a precondition side. |
| Truby's moral-argument sequence | `no` | Sequences moral change but supplies no check on whether a change is *dated* correctly. Reported because it was asked for; it does not fit. |
| Dara Marks's staged decline of the fatal flaw | `no` | A hair from reject. Describes shape, not schedule. |
| Story Grid spreadsheet | `no` | Scene-keyed value shifts; no acquisition axis. |
| Franchise canon tiers (G/T/C/S/N) | `no` | Provenance on facts, but adjudication after a human finds the error. |
| Per-scene continuity subagent fan-out | `no` | Uniform attention, but each agent sees one scene and the creed error is a relation between two scenes eight months apart. Retain for D only. |

---

## 3. Worth stealing verbatim

**The scene header.** Six lines of state declaration above the prose, from a
real shipped storylet — an age window plus a once-only flag, and a
postcondition that advances the clock:

```
title: Church
subtitle: Where you spend most of the time when you're not at home.
frequency: 1000
view-if: age > 4 and age < 8 and church-introduced = 0
on-arrival: age += 1; church-introduced = 1
tags: plot, top
```
— *Bee* in Dendry, `source/scenes/church.scene.dry`, verified byte-for-byte.
*(Attribution care: the storylet design is Emily Short's, from the Varytale
original; the `view-if:` syntax as quoted is the porter's, Autumn Chen.)*

**The definition, for the method file:**

> "storylets are discrete, self-contained, and reorderable modules of
> narrative content, gated by preconditions that determine whether they can
> be presented to the player at any given moment in time"
> — Kreminski & Wardrip-Fruin, ICIDS 2018

**The four-part action, which is the shape a scene declaration copies:**

```
action walk(character : character, from : place, to : place) {
	precondition:
		from != to & alive(character) & at(character) == from;
	effect:
		at(character) = to;
	consenting: character;
	observing(c : character): at(c) == from | at(c) == to;
};
```
— Sabre narrative planner, `readme.md`. And the clause worth more than the
precondition, for failure mode D:

> "A list of zero, one, or many `character`s who must have a reason to take
> the action. […] When there are two or more characters, each must have a
> reason, but they can have different reasons."
> — Sabre, *Consenting Characters*

**That is the formal version of "why would this institution do this?"** — and
institutions never get POV chapters, which is precisely why D eats them. A
`consents / why` column on each beat of a chapter plan is a ten-minute
addition that needs no software at all.

**The framing to keep in view while building any of this:**

> "A narrative planner is not meant to replace human authors but to assist
> them in telling interactive stories. **People are better than algorithms at
> telling stories.**"
> — Sabre, `readme.md`

**The date qualifiers** — keep the GEDCOM spellings; they are terse,
greppable, and nearly absent from English prose:

- `ABT month-N` — near month N, not pinned, nobody has ruled it.
- `CAL month-N` — **calculated by me from other rows.** If any of those move,
  this must move.
- `BET month-A AND month-B` — the honest form for "acquired somewhere in this
  stretch". **This is the one that would have kept the creed out of trouble.**
- `AFT` / `BEF month-N` — one-sided bounds, which is what most inferences are.
- **A bare month means the author ruled it. The assistant may not write one.**

**The credibility grade**, and the specification's own caveat, worth stealing
along with the field:

> "Some systems use this feature to rank multiple conflicting opinions for
> display of most likely information first. **It is not intended to eliminate
> the receivers' need to evaluate the evidence for themselves.**"
> — GEDCOM 7, on `QUAY`

And the note underneath it, which is itself the finding:

> "The structures for representing the strength of and confidence in various
> claims are known to be inadequate and are likely to change in a future
> version of this specification."

**The largest, oldest, most heavily-implemented schema for dated personal
facts in existence considers its own confidence modelling inadequate.** Treat
any confidence column this project adopts as provisional.

**The contradiction message**, which is a free upgrade to `falsified.md` —
Inform quotes **both** offending sentences back:

> "You wrote 'South of the Attic is the Winery', but in another sentence
> 'South of the Attic is the Old Furniture': this looks like a contradiction,
> which might be because I have misunderstood what was meant to be the subject
> of one or both of those sentences."

`falsified.md` already names the replacement constraint. What it lacks is the
habit of **quoting the superseded text alongside it**.

**The query discipline**, from a working publisher's internal canon document —
this is the human-interface half of failure mode C:

> "Queries are questions, not instructions… One query per issue *pattern*, not
> per instance — flag the pattern, list locations, let the author rule once.
> **The author's ruling is final on their own book and is recorded on the
> style sheet so it never has to be re-asked downstream.**"
> — J Merrill Publishing, `line-copyedit-proof.md` §0.4

And the shape of a good query — note that it names the conflict and the
decision needed, and does **not** disguise a rewrite preference as a question:

> `1. "Short identifying quotation" — The scene says Mara injured her left
> hand, but the prior continuity note lists her right hand. Which is correct?`
> — WriteMaster, `novel-copy-editor/SKILL.md`

**And the line that applies directly to a multi-book project:**

> "For series titles, the style sheet extends the volume-1 sheet and the
> continuity ledger — **never starts fresh**."
> — J Merrill Publishing, `line-copyedit-proof.md` §2.5

---

## 4. Draft instruction text

**Both of these are drafts for you to rule on, not edits I have made.**
`method-delta.md` is a governing file and adding to it is a design ruling;
`CLAUDE.md` is your working agreement. I have left both untouched.

Kept deliberately short. A working agreement nobody can hold in their head is
the same as no working agreement.

### For `CLAUDE.md` — general, applies beyond this book

Everything here is about **how the collaborator behaves**, and none of it is
fiction-specific — it applies to an architecture recommendation exactly as
much as to a design file.

```markdown
## Provenance

Inference and decision are written in different registers, always.

- Never state an inference in the register of a decision. If you worked it
  out rather than being told it, the sentence has to say so — in the
  sentence, not in a note elsewhere, so it cannot drift out of sync.
- Three levels, one word each: **RULED** (the user decided it), **USUALLY**
  (a working default; deviate without ceremony), **INFERRED** (you deduced
  it; it yields silently to anything the user says to the contrary).
  **You may not write RULED.** Only the user promotes a line to it.
- An inference contradicted by new information is not an error and needs no
  ceremony to overturn. Say so and move on. A RULED line contradicted by new
  information is an escalation, not a judgement call.
- When you carry a constraint from a working document into a reference
  document, carry its provenance marker with it. Stripping the marker on
  promotion is how a guess becomes load-bearing.
- Contradictions are not resolved at your discretion. When something you are
  building contradicts something already established, stop and put the
  conflict up — naming both sides and what each would cost. Do not invent a
  local mechanism that lets both survive.
- A query is a question, not a disguised instruction. Name the conflict and
  the decision needed; do not dress a preference you hold as a question. One
  query per pattern, not per instance. Record the ruling so it is never
  re-asked.
```

**Why this is the `CLAUDE.md` half:** failure C is not a property of this
novel. It is a property of an assistant that writes fluently in whatever
register surrounds it, and it would do the same damage in a design document
about a database schema.

**One measurement, because it is not hypothetical.** In this repo `spec.md`
marks `PROPOSED` 48 times and `RULED` 4. The live files that actually govern
drafting carry roughly one provenance marker each: `combat.md` (89
blockquoted constraints), `team.md` (78), `portraits.md` (69).
**The vocabulary
already exists and is recorded on arrival, then stripped on promotion.** That
is the leak, and it has a location.

`falsified.md` has also already invented the fix — the **"Whose rule it was"**
row — but it appears twice, both times as a post-mortem on a rule that had
already died. **Move it from the death certificate to the birth certificate.**

### For `method-delta.md` — specific to drafting this book

```markdown
## 11. EVERY SCENE DECLARES WHAT IT NEEDS

> **A scene that does not say what must already be true is not planned.**

Three lines per scene in the chapter plan, before drafting:

    month:     0/12
    requires:  creed_bound>=1, kit/blade, at/kadono-dera
    grants:    —

**`requires:` is what must be true before the first line** — not what the
scene demonstrates. `requires: berserk_state` is the error to watch for; so
is an empty field. **An empty `requires:` is an error, not a default.**

Written at plan time, never extracted from the draft afterwards. Extraction
reproduces the disease: the extractor reads the scene that shows the trait
off, and dates the trait there.

**Two reports, both arithmetic, neither judgement.**
1. Every atom a scene requires was granted at an earlier month, or it is an
   ERROR and it blocks.
2. **Every atom granted and never required.** A trait nothing depends on is a
   trait that exists only to be shown off, and that is the disease's own
   signature.

## 12. THE ACQUISITION LEDGER IS DERIVED, AND ITS DATES ARE QUALIFIED

> **`timeline.md` stays the anchor. The ledger is a projection of it, never a
> second document that can disagree with it.**

One append-only row per acquisition: attribute, character, story-month,
acquiring event, provenance. State at month N is a **fold**, computed, never
maintained.

**Correcting an acquisition date is an append, never an edit in place.** The
old row stays with its reasoning. This is `falsified.md`'s rule extended to
state — and it is what makes moving the date *cheaper* than inventing a
mechanism, which is the whole point.

**Every date carries a qualifier; a bare month means the author ruled it:**
`ABT` near, `CAL` calculated from other rows, `BET…AND` an honest interval,
`AFT`/`BEF` one-sided. **The assistant may not write a bare month.**

The check runs as an **invariant over months, not a pass over scenes** — for
every character, for every month from the first to the last, everything
exercised in that month has an acquisition month at or before it. **It does
not skip the months where nothing happens.** That is the entire point: those
are the months this book will get wrong.
```

**Why this is the `method-delta.md` half:** it is mechanism, it costs time per
chapter, and it is calibrated to this book's shape — three threads, a month
clock, an age ledger that is already an anchor.

### What I deliberately left out of both

- **The institutions file** (§2 item 7). Real and cheap, but it is a *third*
  artifact aimed at a different quadrant, and adding two rules and a file in
  one pass is how disciplines get abandoned. Add it after items 11 and 12
  have survived two chapters.
- **A confidence grade** (`QUAY`). The specification that invented it says its
  own confidence modelling is inadequate. Three levels are enough.
- **Anything requiring software you do not have.** The checks above are a
  nested loop over a table. Do not build a planner; a formal domain for a
  novel is a research project that will not survive chapter three.

---

## 5. What I did not find, and where I looked

### The AI-artifacts category is as thin as you predicted — and thin in a
specific way

Fourteen sources fetched and independently re-verified; **no fabricated
citation and no fabricated source**, which is worth saying. But after strict
re-scoring, **not one practice in this category would have caught the creed
error as shipped.** The strongest catches it only if a human first declares
the requirement — which is precisely the act that failed.

Two structural findings, and they are the real yield:

- **Everything in this space detects CONTRADICTION, not UNMET PREREQUISITE.**
  Two statements that disagree, it finds. A scene silently leaning on a state
  nobody has granted yet, it does not.
- **Almost everything is forward-looking** — later text violating earlier
  canon. **The creed error is backward-looking:** an earlier scene
  presupposing later-dated state. Nothing is pointed that way.

**The sharpest negative datum in this whole report.** GitHub code search, run
across all public code:

| Query | Results |
|---|---|
| `acquired_chapter` | **0** |
| `acquired_in_chapter` | **0** |
| `learned_in_chapter` | **0** |
| `state_at_chapter` | **0** |
| `state_as_of` | **0** |
| `snapshot_at_chapter` | **0** |

**Nobody is dating acquisitions or querying state-as-of-story-time in fiction
tooling.** Not thinly — not at all. The repos that exist are 0–220 stars, some
self-evidently AI-authored, none with a finished multi-book series behind
them. **The corpus contains no example of a state ledger that survived contact
with a second book.**

### The evidence that does not exist anywhere

**No field report of a catch.** Sixty-odd practices, and not one account of
any of them actually catching a premature-capability error in production. What
does exist is one detailed *negative* report, and it is the most useful single
piece of evidence found:

> "The first step is to re-read the entire Wheel of Time. *Towers of Midnight*
> had some small continuity errors — **mostly me forgetting who knows what.**"
> — Brandon Sanderson, 3 January 2011

He had eight detail-obsessed beta readers on that book and a paid continuity
department. They all missed it. His remedy was **a four-month full re-read of
the entire series.** Whatever you adopt, assume it leaks, and instrument it so
it produces the field report the literature lacks.

### Blocked, and worth re-running on an open connection

The four dimensions with **zero pages opened** — series bibles, TV writers'
rooms, the who-knows-what-when matrix, and the craft literature on timing.
Specifically unreachable: the Chicago Manual, CIEP, EFA and every professional
editing body; `hollylisle.com` (the One-Pass Revision method); every academic
host (`arxiv.org`, `aclanthology.org`, `jair.org`); every fan wiki; Wikipedia;
`theoryland.com` except via a GitHub mirror; `bladesinthedark.com`.

**On question 3 in particular** — the who-knows-what-when matrix generalised
beyond knowledge, to possessions, capabilities, obligations and bindings — I
could not settle it. It was flagged in the brief as potentially the most
valuable find, and it remains open. What I can say is that the *knowledge*
form is real and documented, and that no source I reached generalises it to
the other four categories.

### Domains nobody ran, ranked by what I would chase first

1. **Legal case chronology — the best remaining lead, and I could not reach a
   single source.** Litigation chronologies are keyed on a **fact**, not an
   event, and each row reportedly carries a date (including explicitly
   imprecise dates), the fact, its **sources**, who it is material to, and a
   **status** distinguishing undisputed / disputed / **prospective**.
   *Prospective* is the field worth verifying: **a fact you intend to
   establish and have not yet**, carried openly, blocking nothing until relied
   upon. That is structurally different from a "proposed" *decision*, because
   it attaches to a fact about the world, at a date. **[recall] — do not cite
   it, run it.** Second reason to chase it: the fact-witness matrix is the
   only knowledge matrix I know of that is routinely audited *by an
   adversary*. Every matrix in this report is self-audited.
2. **Historical fiction and biography — the chronology file, the "day book".**
   The biographer's problem is exactly "what was true of this person in month
   N, and what is my warrant". Unreached.
3. **Apocalypse World "Fronts"** — grim portents, impending doom, countdown
   clocks. A grim portent is *a dated consequence that arrives if unopposed*,
   which is the more sophisticated artifact than the faction clock in §2 item
   7, and I could not verify a word of it.
4. **Theatre and opera revival practice, the prompt book.** Predicted low: it
   records blocking and business for one fixed staging. It answers "where was
   the actor standing", never "when did the character acquire this".
5. **Accounting reconciliation.** You will shortly have two records — the
   event timeline and the acquisition ledger. Accounting's discipline is not
   that either is right; it is that they are periodically **forced to agree
   and every difference must be explained.** Nobody proposed reconciliation as
   a recurring act, and a monthly "does the ledger's acquisition set equal the
   timeline's acquiring events?" pass is cheap.

### Three risks in the recommendation that nothing in the literature addresses

- **The multi-POV concurrency problem is untouched.** Every state artifact
  found is single-timeline. Three parallel threads means state indexed by
  (character, month) **and** cross-thread: what thread B's character knows in
  month N depends on whether thread A's courier arrived. Nothing found solves
  this. You will be inventing it.
- **Nobody asked what happens when the AI maintains the ledger.** The whole
  design is self-referential — **the agent that commits failure C is the agent
  that would write the provenance column.** No practice anywhere defends
  against an assistant writing "ruled" on a row it guessed. The only
  mitigation found is the structural one in §4: *the assistant may not write
  the top level, ever, and may not write a bare date.* That is a rule, not a
  mechanism, and rules of that kind are exactly what this project's history
  says get eroded one reasonable entry at a time.
- **Retrofit is the expensive part and nobody costs it.** Not one source in
  sixty reports its maintenance burden. For a 20k-word chapter across three
  threads, the difference between twenty minutes and three hours per chapter
  decides whether any of this survives, and I am estimating rather than
  citing.

---

## 6. If you adopt one thing

**Item 1, and only item 1, for two chapters.** `requires:` / `grants:` on
every scene of the chapter plan, with an empty `requires:` treated as an
error, plus the zero-count report.

It needs no software, no new file, and no ledger — the chapter plan already
exists and already gets written before drafting. The ledger (item 2), the
invariant (item 3) and the rule engine (item 4) are the same artifact built in
increments, and each increment is individually useful. **Build them in that
order, and only once the previous one has survived a chapter you actually
drafted.**

And the thing to watch for, because it is the failure this recommendation will
actually have: **a `requires:` line that restates the scene instead of
constraining it.** When that starts happening the discipline is already dead,
and the zero-count report is the only instrument that will tell you.
