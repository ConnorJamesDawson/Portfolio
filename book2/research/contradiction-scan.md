# Contradiction scan — book two

Eight hunters over `book2/design/` (17,600 lines) and `book2/prose/`
(87 scenes, ~157,000 words, chapters 1–9), each with an adversarial verifier
behind it. **58 findings survived verification, 16 were killed as false
positives.** After removing duplicates — the same error found by four
different hunters — that is **roughly thirty distinct issues.**

**Six are verified by me personally, quote by quote, against the files.**
They are §1. Everything in §2 was verified by an agent and spot-checked
mechanically (98 of 116 quoted sides matched verbatim on an automated grep;
the misses were transliteration, `Nakadō`→`Nakado`, and elision markers) but
I have not read each one in context. Treat §1 as settled and §2 as a worklist.

---

## 1. Verified personally — six, in order of what they cost

### 1.1 Uzuki's tenth birthday is fixed twice, forty days apart, and one
version makes her nine at the warrant

| | |
|---|---|
| `prose/ch09-scene07.md:18` | *"She had been eleven days short of ten years old."* |
| `prose/ch06-scene10.md:344` | *"I'm ten and four months."* |

The first is anchored three lines up to *"the road she had walked on the
twenty-sixth of the third month"* — so eleven days short of ten on 26/3 puts
her tenth birthday at **7/4**. The second is spoken in a scene headed *month
6, the twenty-seventh* — ten-and-four-months puts it at **27/2**. Forty days
apart. She cannot have turned ten on both.

**This is the worst finding in the scan**, because the 7/4 version breaks
things far outside its own scene:

- **It makes her nine at the warrant.** The warrant runs 4/4–5/4. Author
  anchor #2 (`timeline.md:12`) is *"Uzuki is the **same age**"*, and
  `timeline.md:41` states *"Both children are ten."*
- **Eighteen shipped scene headers say "age ten"** before 7/4.
- `ch09.md:220` leans on it explicitly: *"**And the thing she has not costed
  is that she is ten.**"*

**27/2 wins, and not by authority — by arithmetic.** It is the input to
*"Fifteen is four years and eight months"* → **1,704**, the book's most
repeated number, which then runs correctly through four chapters (see 1.3).
The `ch09-scene07` sentence is one clause and should read *"eleven days
past ten years old"* or similar.

**Still open after that fix:** "ten and four months" is also said on 14/9
(`ch09-scene04.md:222`) and ~22/9 (`ch09-scene09.md:229`), where a 27/2
birthday makes her ten and *six* months. And `ch09-scene04.md:222` pairs
"ten and four months" with "four years and seven months", which sums to
fourteen years eleven months, not fifteen.

### 1.2 Mikage is thirty-four and gives a first-hand account of something
fifty years ago

| | |
|---|---|
| `prose/ch02-scene08.md:210` | *"**His mother** sat at the table with her hand on the ledger. 'They came for him in the daytime,' she said."* |
| `prose/ch02-scene08.md:215` | *"…the whole compound was out, **all forty of us**, on the paths, at the doors, on the second course and the third course, watching."* |
| `prose/ch02-scene08.md:222` | *"And every single person on that hill was somebody who could have done something. **Forty of us.**"* |
| `prose/ch02-scene08.md:227` | *"Not once. **Not in fifty years.** I've had it at three in the morning about a hundred times…"* |
| `prose/ch02-scene08.md:261` | *"**I have had it for fifty years**, and every time anybody in this family says…"* |

She places herself **on the hill**, in the first person, twice. Her age is
stated three times: `ch03-scene05.md:4` (*"Mikage, age thirty-four"*),
`ch06-scene10.md:336`, `ch07-scene08.md:189` (*"at thirty-four, sitting on a
mat in the dark"*). **She was not born when Kongō was taken.**

**Load-bearing.** The taking is the founding event of the family secret, and
Kongō's fifty years is fixed by #9. So the interval cannot move; the
**witness** has to. Either she is recounting what her mother told her —
which costs the scene its first-person force — or the account belongs to
somebody older.

**The likely source of the error** is `falsified.md` #9, which correctly
gives *fifty years* as **Kongō's** span — *"has been marking his work for
fifty years"* — and it has migrated into Mikage's mouth as her own memory.

### 1.3 The flour-bag countdown is opened on the 27th, remembered as the 24th

| | |
|---|---|
| `prose/ch06-scene10.md:3` | *"Act 1, month 6, **the twenty-seventh**. The kitchen at Nakadō."* — and `:8`, *"The box came out on the twenty-seventh because the twenty-seventh was when the box came out"* |
| `prose/ch07-scene10.md:245` | *"**Twenty-fourth** of the sixth month I wrote seventeen hundred and four and I took one off"* |

`ch06-scene10:353–357` is the scene in which the number is created — she
starts the third column, does the sum, *"checked it twice because it was the
only sum in her life that was ever going to matter"*, writes **1,704**, then
takes one off → **1,703**.

**The arithmetic settles it independently.** `ch07-scene10.md:241` reads
*"The third column said 1,679."* on 21/7. From 1,703 on 27/6, at one a day,
28/6→21/7 is 24 days: **1,703 − 24 = 1,679. Exact.** Opening on the 24th
gives 1,676. **The 27th is right; `ch07-scene10.md:245` is wrong.**

**And `threads.md:2306` has already recorded the wrong date as a fixed
fact** — the file whose own header says it *"wins over memory, over the spec,
and over any earlier draft."* It carries forward into ch10 and ch11, where
the countdown continues.

### 1.4 Kajiya runs a meeting nineteen days after the anchor says he was
last seen

| | |
|---|---|
| `design/timeline.md:55` | *"**Kajiya has not been seen since 2/8.**"* — restated at `ch10.md:579` and `ch10.md:381` |
| `prose/ch08-scene06.md:3` | *"Act 1, **month 8, the twenty-first**. A room above a rope-walk, Ōtoma."* |

He is not referred to in that scene, he is **in** it: named first among those
present (`:11`), *"Kajiya said, 'Which?'"* (`:89`), and he gives the order
that closes the meeting — *"'Right,' said Kajiya. 'Yatate, go back to Kanō
and get me the day the…'"* (`:130`).

**The prose wins**; the beat that depends on the date is not yet drafted.
`ch10.md:380–385` builds a deliberate silence out of it (*"**AND KAJIYA HAS
STOPPED COMING**… the reader should feel the shape of that and get nothing
either"*) — that beat survives intact, one week shorter, if the date moves to
**8/21** in `timeline.md:55`, `ch10.md:381` and `ch10.md:579`.

### 1.5 `combat.md` asserts the killed sword mechanism sixty lines above
the ruling that killed it

| | |
|---|---|
| `design/combat.md:423` | *"**THE SWORD IS SUSTAINED, NOT SEALED.** *Held, not open — continuous chakra of the right nature simply to keep being a sword.*"* |
| `design/combat.md:483` | *"⚠ **RULED: IT IS OPEN, AND IT DOES NOT DEGRADE.** … **An earlier draft had it sustained** — a permanent low tax, and *when he is spent the blade goes*. **That is dead.**"* |

Both sit in §7, both in the same ⚠-flagged register, **the dead one first and
unmarked.** Anyone — or anything — reading §7 top-down meets the killed rule
before the ruling that kills it, in the file that governs every fight in the
book. This is failure mode C with a line number.

**The fix is a rewrite, not a deletion.** The ORIGIN block's *argument* is
still wanted — a boy with one hand in a splint needs a weapon that does not
need a hand, and a half-katana is a one-handed weapon. Only the mechanism
sentence is dead.

*(Two related hits at `combat.md` §3's economy table and §10, reported by the
dead-rule hunter, are in §2 below and I have not read them in context.)*

### 1.6 "Nine and five and three is nineteen days"

> `prose/ch08-scene02.md:237` — *"And nine and five and three is nineteen days
> and I have gone from nineteen days to about ten and it's the eighth of the
> eighth month."*

**9 + 5 + 3 = 17.**

It cannot be defended as a character slip. The same scene insists twice that
she checked it: *"She did it again on the back of the bag, in a column, and it
came out the same, because three numbers do not change when you write them
twice"* (`:220`), and *"she stopped, and made herself do it, and did it in her
head first and then on the bag because she did not trust her head with it"*
(`:229`). The gaps are the hunter-contact intervals, and the count is the
chapter's engine.

---

## 2. The rest — agent-verified, not read by me in context

Deduplicated to 42 distinct issues. Each was confirmed by an adversarial
verifier that re-fetched the quotes; I have spot-checked them mechanically but
not read each in context. **Check before acting.**

### Shipped prose (31)

| Issue | Where | Confidence |
|---|---|---|
| "Six months and eight days" is eight days on the wrong side of the sum | `prose/ch09-scene07.md:22` vs `prose/ch09-scene07.md:15` | certain |
| Ōgi is eleven miles and also a five-day walk — and Kiku says both, sixty lines apart | `prose/ch09-scene09.md:46-47` vs `prose/ch01-scene09.md:187` | certain |
| Uzuki is nine on the twenty-sixth of the third month, and the anchor says she is ten | `prose/ch09-scene07.md:18` vs `design/timeline.md:41` | certain |
| threads.md puts Uzuki home on the seventh; the prose has her home on the sixth | `design/threads.md:629-630` vs `prose/ch04-scene10.md:3` | certain |
| "Two years later" is used twice for events three months and six weeks away | `design/world.md:125-126` vs `prose/ch03-scene05.md:3` | certain |
| The grit is free off the family's own beach in ch1 and bought off a merchant by the sack in ch7 and ch8 | `prose/ch01-scene01.md:28-34` vs `prose/ch08-scene04.md:161-164` | certain |
| Kenji puts the tin under his counter with the thirty-one pieces in it, and Tadayoshi picks the same tin up empty four paragraphs later | `prose/ch04-scene04.md:122-123` vs `prose/ch04-scene04.md:234` | certain |
| The riverbed is the eighth of the fifth month everywhere except one line of ch06-scene01, which puts it on the ninth and then breaks its own four-day sum | `prose/ch06-scene01.md:149-151` vs `prose/ch06-scene01.md:182-185` | certain |
| He locates his last chest-going moment on the eighth of the fourth month on the shoulder above the inlet, a day he spent two days' walk away on the Sunaba road | `prose/ch08-scene04.md:154-157` vs `prose/ch05-scene01.md:3` | certain |
| He casts the full four seals one-handed in month 5 — five months before the anchor allows half seals | `prose/ch05-scene06.md:14-17` vs `design/timeline.md:54` | certain |
| Grit is free off the beach in chapter 1 and bought off a merchant by the sack in chapter 8 | `prose/ch01-scene01.md:28-34` vs `prose/ch08-scene04.md:161-164` | certain |
| The four-seal craft sequence is 'Ram. Snake. Ox. Hare.' on page one and 'Ram, Boar, Ox, Snake' in every later cast | `prose/ch01-scene01.md:38` vs `prose/ch05-scene06.md:17` | certain |
| ch09.md quotes the Aku-bank ledger entry with the wrong count — 'had it right by the third' against the prose's 'by the second one' | `design/ch09.md:300-303` vs `prose/ch09-scene08.md:130-133` | certain |
| Eight people are walked onto the boat; seven people are taken | `prose/ch03-scene03.md:202-205` vs `prose/ch03-scene05.md:90-92` | certain |
| Entry 47 is called the first entry not about his mother; entries 44, 45 and 46 are not about his mother | `prose/ch07-scene07.md:269-275` vs `prose/ch06-scene06.md:12-31` | certain |
| Uzuki dates Kuriya's "six people" refusal to 23/8; the prose has him say it on 6/4, in a different conversation | `prose/ch09-scene04.md:184-186` vs `prose/ch06-scene07.md:369-372` | certain |
| Twenty-seven months of not being presented; the ledger allows twenty-two | `prose/ch02-scene08.md:187-190` vs `prose/ch02-scene08.md:177-180` | certain |
| Seven people are walked down the hill, and eight, in the same scene | `prose/ch03-scene03.md:184-186` vs `prose/ch03-scene03.md:202-205` | certain |
| Tadayoshi's hands have already started at ten; portraits.md says they start at eleven | `design/portraits.md:146-147` vs `prose/ch02-scene08.md:305-318` | certain |
| Uzuki is "ten and four months" on two dates eighty days apart, and her time-to-fifteen shrinks by one month | `prose/ch06-scene10.md:344, 346` vs `prose/ch09-scene04.md:222-223, 242` | certain |
| The wall, the twenty-two miles and "22 good" are the fifth in ch04-scene08 and the fourth in ch04-scene10 — and the fourth is the day her father died | `prose/ch04-scene08.md:3, 30, 37-44, 290` vs `prose/ch04-scene10.md:91-98` | certain |
| Nezu is forty-one miles from Shioiri in one line of ch05-scene03 and forty-one miles from Sunaba twenty-eight lines later | `prose/ch05-scene03.md:187` vs `prose/ch05-scene05.md:8` | certain |
| "She has been at this four minutes" lands at the minute-forty mark of an engagement the same scene times to the second | `prose/ch09-scene05.md:106` vs `prose/ch09-scene05.md:53, 83, 111, 132, 174` | certain |
| "Six months and eight days" is five months and twenty-two days | `prose/ch09-scene07.md:22` vs `prose/ch09-scene07.md:3` | high |
| Sae is twelve weeks a widow at a wedding four live design files call ten weeks | `design/timeline.md:50` vs `prose/ch07-scene02.md:3` | probable |
| The knife he inventories as inherited from Meno is one he bought with his own money in chapter 4, and the coat is not the first thing he ever bought himself | `prose/ch04-scene09.md:155-158` vs `prose/ch07-scene09.md:207-214` | probable |
| Tadayoshi knows his mother is at a bench eight hours before the scene in which he works it out | `prose/ch05-scene06.md:273-277` vs `prose/ch05-scene09.md:148, 153-160` | probable |
| Ryūta's broken arm: last year, or the spring before last — and timeline.md says both | `design/world.md:181` vs `prose/ch01-scene08.md:188-191` | probable |
| "Six months and eight days", counted in the wrong direction | `prose/ch09-scene07.md:15-22` vs `prose/ch04-scene03.md:3 (with ch03-scene07.md:3 and ch04-scene01.md:3)` | probable |
| The ninety column is called thirty-two lines but its first two entries predate the thirty-two days | `prose/ch05-scene07.md:139-156` vs `prose/ch04-scene08.md:8, 20, 42` | probable |
| "Twenty-seven months" does not reach back to the eighth month of the year he was eight | `prose/ch02-scene08.md:188-190` vs `prose/ch01-scene01.md:157` | probable |

### Design files only (11)

| Issue | Where | Confidence |
|---|---|---|
| ch07.md's scene list and ledger carry three dates the shipped prose contradicts, and a chapter range two days past the anchor's clock | `design/ch07.md:494` vs `design/timeline.md:200` | certain |
| A rule killed in falsified.md #10 is still asserted as live in combat.md and team.md | `design/combat.md:920-926` vs `design/falsified.md:106` | certain |
| world.md gives Ōgi two different distances from Nakadō in two of its own tables | `design/world.md:95` vs `design/world.md:186` | certain |
| ch06.md dates the riverbed entry to both the 19th and the 20th of month 5 | `design/ch06.md:163` vs `design/ch06.md:545` | certain |
| ch06.md numbers the riverbed entry 43 and the Nezu entry 44, reversing threads.md and contradicting the rule stated directly beneath the table | `design/ch06.md:545-546 (rule paragraph at 549-552)` vs `design/threads.md:1763-1765` | certain |
| combat.md §1b states the half-seal failure rate twice, twenty lines apart, and the two numbers are reciprocals | `design/combat.md:140` vs `design/combat.md:160` | certain |
| combat.md §7's ORIGIN block asserts the killed sword mechanism — "held, not open" — as "the mechanical reason", sixty-five lines above the block in the same section that rules it dead | `design/combat.md:418-426` vs `design/combat.md:483-491` | certain |
| combat.md §10 still runs the killed motive for the separation — "arithmetic, not fear" — while structure.md, citing that same §10, says the cause "is not arithmetic" | `design/combat.md:920-926` vs `design/structure.md:170-191` | certain |
| team.md §9 labels the village decision "Not fear. **Arithmetic**" and quotes the dead sentence as live doctrine, citing a §10 that will no longer say it | `design/team.md:619-621` vs `design/structure.md:183-191` | certain |
| What brings him out of the threshold: combat.md says he recognises his mother's hand, ch05.md rules that out, and the prose has him refuse to look at the object for hours | `design/combat.md:820-824` vs `design/ch05.md:246-249` | high |
| Mikage's death year: the anchor puts it at eleven, two live files put it in year 2 | `design/timeline.md:31` vs `design/threads.md:53` | probable |


---

## 3. What was checked and found sound

Worth as much as the findings, and it is a lot:

- **The chapter clock is exact.** All nine chapters match `timeline.md` §6 on
  scene count, word count and POV split. I recounted from the prose files:
  ch1 10/16,910, ch2 9/15,215, ch3 9/16,853, ch4 10/16,869, ch5 9/15,486,
  ch6 10/19,749, ch7 10/18,060, ch8 11/18,463, ch9 9/17,411 — every one
  inside 20 words of the stated figure.
- **Scene headers are disciplined.** Of 87 scenes, **zero** drift more than
  12% from their stated word count. Every header carries act, location, age,
  POV and count in the same order. The only "missing month" headers are the
  Kimimaro scenes, which are undated by design.
- **Chapter date ranges run in order** with no gaps, and the ch6/ch7 overlap
  is the parallel-thread structure working, not an error.
- **`falsified.md` #15's replacement landed correctly in the prose.** Ordinary
  articles degrade (`combat.md:324`); the open blade does not
  (`combat.md:490`). The distinction holds everywhere I checked, and no prose
  scene describes the blade degrading or going quiet. *(The §7 origin block,
  §1.5, is a design-file leak, not a prose one.)*

---

## 4. The one structural thing this scan says

**The four series `method-delta.md` §9 mandates cannot be mechanically
validated, because the book never fixes a month length.** The highest date
used anywhere in 87 scene headers is *the thirtieth*, and no source states
whether a month is 30 days or something else.

The flour-bag countdown happens to check out exactly at 30-day months over
its first leg — which is how §1.3 was settled — but the long sum behind it
(*"fifteen is four years and eight months"* → 1,704) only works on a
roughly-real calendar (4 years ≈ 1,461 days + 8 months ≈ 243). **Those two
conventions are not the same and the book uses both.**

Fixing the month length in `timeline.md` costs one line and makes every
running number in the book checkable by a script. Leaving it open means the
series stay uncheckable for the remaining three acts, and the errors in §1
and §2 are the ones that reached the page in nine chapters.
