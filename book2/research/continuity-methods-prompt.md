# Research brief — character-state continuity in long-form serial fiction

*A prompt to paste into a web-enabled research session. It is written to be
run by someone with search access and no prior context on this project.*

---

## What you are being asked to find

**Working practices, named methods, and reusable instruction artifacts that
prevent one specific failure mode in long-form fiction planning — and an
honest assessment of which are worth adopting.**

The requester is a novelist working with an AI collaborator (Claude Code)
on book two of a multi-book novelisation. Roughly 20,000-word chapters,
three parallel POV threads, an eleven-file design system kept in a git
repo. The AI drafts chapter plans and prose; the human rules on design
questions. **Both halves of that pair are producing the failure, so
solutions that assume a single human author are still in scope, and so are
solutions that only make sense for an AI collaborator.**

---

## The failure mode, stated precisely

**Planning attention flows to major beats. Character state between beats
is never tracked, so attributes get assigned to the moment they are first
dramatically convenient rather than the moment they would have been
acquired.**

It has four observed parts. Treat them as separable — a source that
addresses one is still useful.

### A. Late acquisition

A character trait, rule, skill, possession, belief, or relationship is
dated to the scene that shows it off, not to the scene that first needs
it. **Worked example, from this project:** the protagonist's moral creed —
*"stay your hand from the blood of the innocent"* — was dated to age
eleven, because that is where a strong scene for acquiring it sat. Eight
months of story time earlier, at age ten, he goes berserk in a building
containing a child he is about to rescue. **Nothing in the design noticed
that the rescue required a governor he would not have for another year.**
Every major beat lined up perfectly; the state underneath them did not
exist. The author caught it. The design system did not, and had no
mechanism that could have.

### A2. Frozen state — the same defect running the other way

**A state written down once is later read as a permanent property**, so
the character silently stops developing and nobody decides that they
should. **Second worked example, same project, found while writing this
brief:** a design file describes a girl's medical skill *at age ten* — the
section is literally titled *fixed on the page in chapter 4*, and its
second sentence says the real technique takes six years to learn. **That
file was then quoted as her ceiling in a discussion of events seven years
later**, and used to argue she would always be limited to palliative care.
**The file was correct. The reading froze her.**

> **A and A2 are one missing artifact seen from two sides.** *A: an
> attribute dated to the wrong moment. A2: an attribute that never gets a
> second moment.* **Nothing in the system answers *what is true of this
> person as of month N*** — only what happened (an event timeline) and
> what the rules are (a rule ledger).

### B. Patch the scene, not the timeline

When A is discovered, the reflex is to **invent a local mechanism that
lets the scene survive** — in the worked example, an elaborate rationale
about the child's physical position in the building — rather than move the
acquisition date and absorb the consequences. **Local patches are cheaper
to write, read as ingenuity, and are structurally worse**, because they
add machinery whose only job is to protect a scheduling error.

### C. Inference written in the voice of decision

Constraints the AI *inferred* get written into design files in the same
register as constraints the author *ruled*. Three have had to be killed in
one working session. Once written down they are load-bearing, and nobody
can tell later which were decided and which were guessed.

### D. Major-beat gravity, generally

The set pieces get planning depth. The connective tissue — habits, minor
characters' arcs, small acquisitions, offscreen months, the reasons
institutions do things — gets compressed. **Continuity errors concentrate
in the compressed regions**, which are also the regions nobody re-reads.

---

## What already exists here, so you can skip it

Do not return advice to do things this project already does. It has:

- **A month-by-month event timeline** for two of three POV threads,
  running the length of the book, with each chapter's clock recorded after
  drafting.
- **A falsification ledger** — every rule that has been overturned, with
  the replacement constraint that had to be named in the same entry. *No
  rule may die without a replacement.*
- **Per-chapter design plans** written before drafting, each with a
  "revised on the page" section written after.
- **Thread ledgers, character portraits, a combat-mechanics file, a
  world register, an act-structure file, and a method file.**
- **A hard rule against summary where a scene belongs.**

**So the gap is specifically: strong event bookkeeping, strong rule
bookkeeping, no state bookkeeping.** Nothing answers *what does this
character possess, know, believe, and is bound by, as of month N.*

> **⚠ Test that framing rather than accepting it.** It is the requester's
> current hypothesis and may be wrong, or may be a symptom of something
> more basic. If the literature says the real cause is elsewhere — planning
> order, revision-pass design, outline granularity, POV discipline — say
> so and argue it.

---

## Questions to answer

**1. Is there a named craft practice for tracking character state over
story time?** Not the event timeline — the state underneath it. Look at:
series bibles and continuity bibles as actually specified (what fields do
professional ones carry?); TV writers'-room artifacts — the board, the
grid, the script coordinator's job, continuity/"bible" maintenance on
long-running serials; the "who knows what when" matrix used in mystery and
ensemble writing; game and interactive-fiction practice, where this is
literally a state machine and the discipline is mature.

**2. Is there craft literature on the specific error of dating a character
change to its best scene rather than its causal moment?** Candidate
frames worth checking and reporting on honestly, including if they turn
out not to fit: Truby's moral-argument sequencing, which tracks moral
change beat by beat rather than as a single conversion; Swain's
scene/sequel structure; McKee on gaps and progressive complication;
anything on "off-page change" and how serial writers schedule it.

**3. What do long-series authors actually do?** Prefer accounts with
specifics — file structures, spreadsheet columns, what gets checked and
when — over interviews that say "I keep a bible." Multi-book fantasy and
crime series are the richest sources. Fan-run series wikis are also
evidence: what do readers track that authors do not?

**4. Are there existing agent instruction artifacts for this?** Claude
Code skills, CLAUDE.md patterns, system-prompt libraries, prompt
collections, GitHub repos aimed at long-form fiction continuity,
worldbuilding bibles, or consistency checking with an LLM. **Expect this
category to be thin and mostly low quality — say so if it is**, and do not
pad the answer with near-misses.

**5. Is any of it mechanically checkable?** Continuity linting, timeline
validators, state-assertion passes, "does scene N require anything not yet
acquired" checks. Anything where a script or a scripted review pass could
catch the error rather than a human noticing.

**6. What revision-pass discipline catches this?** Named single-purpose
passes, what order they run in, and which pass would have caught the
worked example.

**7. On failure C specifically** — is there established practice, in any
collaborative-writing context (co-authors, ghostwriting, writers' rooms,
editorial), for **marking the provenance of a decision**: who decided it,
whether it was ruled or assumed, and how provisional it is?

---

## Acceptance test

**Score every candidate practice against BOTH worked examples** — the
creed dated too late (A), and the medical skill frozen at its first
recorded state (A2). For each practice, state plainly: *would this have
caught these before they reached the page, and what would the catch have
looked like?* **A practice that catches one and not the other is still
worth reporting — say which**, because the two failures may need
different instruments. A practice
that would not have caught it can still be worth reporting — but say that
it would not have.

**Reject and do not report:** generic "how to write a novel" listicles;
AI-generated content-farm posts on consistency; NaNoWriMo-tier blog
advice; anything that says "keep a series bible" without specifying its
contents; tool marketing pages for outlining software unless the page
documents an actual method.

**Flag thin evidence.** If a practice is one person's blog post rather
than established craft, say so. If a category returns nothing good, report
the absence rather than filling it.

---

## Output

1. **A ranked shortlist** of practices worth adopting, each with: what it
   is, where it comes from, the source, what it would cost to run on a
   20k-words-per-chapter three-thread book, and its verdict on the
   acceptance test.
2. **Anything worth stealing verbatim** — field lists, grid columns,
   checklist items — quoted, with attribution.
3. **Draft instruction text** for the two surfaces this project has:
   - a **project-level working agreement** (`CLAUDE.md`) — general rules
     about how the collaborator behaves, applicable beyond this book;
   - a **book-level method file** (`method-delta.md`) — rules specific to
     drafting this book.
   **Say which of your recommendations belongs in which**, and keep the
   two lists short. A working agreement nobody can hold in their head is
   the same as no working agreement.
4. **A statement of what you did not find**, and where you looked.
5. **Your disagreement**, if you have one, with the framing in *"What
   already exists here"* — argued, not hedged.
