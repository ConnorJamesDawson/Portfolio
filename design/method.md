# Method — how a chapter gets written

A portable instruction set. Written as prompt lines: each is a directive,
in the order it is executed. Sections A–C are process; D–H are craft.

---

## A. BEFORE PLANNING — the research pass

1. Read the previous chapter's entry in `threads.md` (§C, most recent) —
   it is the authoritative list of what is now true.
2. Read the last three rows of the chapter clock in `timeline.md`, plus the
   FIXED blocks: the standing week, the price scale, where Tsunade lives.
3. Read `falsified.md` in full before touching any mechanic. A rule that
   was true forty chapters ago is not evidence.
4. Grep the prose for any fact about to be used: `grep -rn "<detail>"
   prose/`. Never write a fact from memory that the text has already
   established. Memory drifts; the file does not.
5. Identify every thread that is due, overdue, or scheduled into this
   chapter's dates. List them before deciding what the chapter is about.
6. State the chapter's dates explicitly. Check them against the standing
   week before assigning any scene to a weekday.

## B. PLANNING — the shape

7. Lead the plan with a recommendation, not a menu. Decide what the chapter
   is, then say why, then name what is being deferred and to where.
8. Give the chapter one spine and at most two subplots. A chapter that
   carries four is a chapter that summarises three.
9. Decide the emotional movement first and the events second. Ask: what is
   different in these people at the end that was not true at the start?
10. Place the chapter's largest beat at roughly two-thirds. Do not close on
    it; close on the small thing that beat makes possible.
11. Assign POV per scene before writing. Give a non-protagonist POV to any
    beat whose meaning is invisible from inside the protagonist.
12. Push back on the author's plan where it is wrong, once, with the
    specific failure mode named. Then build what was asked for, properly.
13. Get explicit approval before writing. Never draft prose off a planning
    conversation that has not been signed off.

## C. WRITING — the mechanics

14. Target 14,000–20,000 words: eight to eleven scenes of 1,800–2,600.
15. Write scenes in order, one per file, `chNN-sceneNN.md`.
16. Head every file: title, then an italic block giving act/part, location,
    character age, POV, and word count.
17. Hard-wrap every line at 78 characters. No exceptions.
18. One POV per scene. Change POV only at a scene break, never within.
19. Third-person limited past throughout.
20. When a beat would be narrated in summary, stop. Ask whether it is a
    scene. If a paragraph of retrospect is doing the work, it is a scene.
21. Ban montage transitions — "the week settled into a rhythm", "the days
    took on a shape". They are the primary density failure.
22. After the last scene: normalise word counts in the headers, then run
    `awk 'length>78'` across every file and fix what it finds.
23. Update `threads.md` with a new §C entry — fixed facts only, in the
    chapter's own language, with the load-bearing lines quoted verbatim.
24. Update the chapter clock in `timeline.md`: dates, scene count, word
    count, the beats, and which scenes carry which POV.
25. Commit with a summary of what changed in the story, not what changed in
    the files. Push.
26. Stitch the scenes into one reading copy and deliver it.

## D. VOICE — the discipline that matters most

27. Give every POV a distinct interior grammar. If two POVs could swap
    narrators without the reader noticing, one of them is not written yet.
28. Do not let the protagonist's mannerisms colonise the cast. Where a
    character has caught a habit from another, the text must have shown
    them catching it, and it must be remarked on somewhere.
29. Derive interior grammar from the character's trade and history, not
    from their mood. A jeweller thinks in tolerances; a medic thinks in
    presentations; a boy raised hungry thinks in who feeds whom.
30. Give each POV its own sentence length. Analytical characters get long
    accumulating sentences; physical characters get short ones that move.
31. Reserve any formatting device — italic interiority, ledger entries,
    numbered findings — to the characters who own it.

## E. DIALOGUE

32. Let people answer the question actually asked, not the one implied.
    Characters who always understand each other are characters nobody has
    to listen to.
33. Give the best line in an argument to whoever is right, and let it cost
    them something anyway.
34. Distribute wit unevenly. If everyone is funny, no one is characterised
    by humour.
35. Write specialists talking shop at full technical density. Do not
    simplify for the reader; make the emotional stake legible instead.
36. End dialogue scenes one beat earlier than feels natural.
37. Never have a character explain the theme. If it must be said, give it
    to someone who is slightly wrong about it.

## F. THE CRAFT MOVES — techniques that recur

38. Say the large thing through equipment. Let a character deliver a
    confession as a report, a proposal as a docket, a declaration as an
    audit finding. The format is the load path; the feeling arrives intact
    and the character survives saying it.
39. Cost every emotional statement physically. A level voice plus a visible
    physiological price is more moving than either alone.
40. Number things. Specific counts — four seconds, eleven minutes, nine
    hundred articles — read as observed rather than invented, and let a
    change in the number carry a change in the person.
41. Solve problems from both ends. When two characters each move toward the
    other in secret, let them collide; the collision is the scene.
42. Let the discovery come in arrears. A character noticing a fact eleven
    days late is more truthful, and more painful, than noticing on time.
43. Withhold one clause. Give the reader a document, an answer, or a
    rationale with a piece explicitly held back — and let the withholding
    itself be characterisation.
44. Prefer the object to the statement. A washed glass, a mended charm, a
    kept button will carry more than a paragraph of feeling.
45. Pay debts quietly. When a long-planted thread resolves, resolve it in
    passing, inside a scene about something else.
46. Give secondary characters one perception the protagonist lacks, and let
    it be correct.
47. Make competence the comedy. Let capable people fail at exactly the
    thing their competence cannot reach.
48. When a scene turns on physical intimacy, keep the camera on faces,
    voices, and interiority. Write what it means to the people; leave
    mechanics in implication.
49. Close chapters on the smallest true image available.

## G. CONTINUITY — the standing corrections

50. Treat every established rule as dated. When the story falsifies one,
    record the event, the date, and the chapter that killed it, and mark
    the corpse where it lived.
51. Never re-derive a fact that a file already holds. Check the file.
52. When the author reports an error, verify it against the text before
    conceding — and when they are right, fix it in the same pass as the
    ledger entry, not later.
53. Keep a list of what the chapter has deliberately deferred, and carry it
    forward in the "Open into" line of the threads entry.

## H. THE STANDING RULES OF THIS PROJECT

54. Do not write prose without an explicit go-ahead.
55. When asked to plan, plan the next chapter — do not summarise the last.
56. Deliver a stitched reading copy after every chapter, unprompted.
57. Say plainly when something cannot be written, and offer the nearest
    thing that can.
