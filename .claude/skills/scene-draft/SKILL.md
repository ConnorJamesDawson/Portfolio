---
name: scene-draft
description: Draft an explicit scene for the novel by driving an outside model through tools/scene-gen.py, then review the result against the book's canon and voice. Use when the user asks to draft, generate, or revise a scene that tools/briefs/ covers.
---

# Scene drafting loop

An outside model writes the explicit prose; this session specifies the
job and audits what comes back. Both halves are needed — the generator
has no access to the ledgers, and cannot tell when it has contradicted
chapter 73.

**Network:** `tools/scene-gen.py` calls OpenRouter and only works where
egress allows it. Probe once with a cheap call (`--list-models`); if
CONNECT fails, do not retry the direct route -- use the Actions relay
below. Local sessions, and remote environments whose network policy
allows `openrouter.ai`, can run the tool directly.

## Remote sessions: the Actions relay

When egress is blocked, the `scene-fill` workflow
(`.github/workflows/scene-fill.yml`) runs the tool on a GitHub runner
instead. It needs the `OPENROUTER_API_KEY` repository secret; if a run
fails on a missing key, tell the user to add it under the repo's
Actions secrets rather than retrying.

The relay loop, drivable end to end from this session:

1. Write the scene with one `<!-- GAP: ... -->` marker. Commit and
   push it to the working branch.
2. Dispatch `scene-fill` via the GitHub MCP actions tools with
   `ref` = the working branch and `file` = the prose file. Pass
   samples deliberately, per step 2.
3. Do not poll in a loop. Schedule one `send_later` check-in a few
   minutes out; on firing, check the run. If it failed, read the job
   logs, fix, re-dispatch once the cause is fixed.
4. On success the runner has pushed a `Fill gap in ...` commit. Pull
   the branch, then review per step 4 -- joins first.
5. Land or revise per steps 5-6. Revision = restore the marker with
   sharper direction, push, re-dispatch.

The runner commits the filled file sight unseen; the review step is
what stands between the relay and the book. Never skip it because the
diff "looks fine" in the commit view.

**Key:** `OPENROUTER_API_KEY` must be in the environment. If it is
missing the tool says so and exits; relay that, do not work around it.

## The loop

### 1. Write the request, do not improvise it

Ask what scene, whose POV, and where it sits in the timeline. Then
check `design/threads.md` and `design/timeline.md` for that chapter
before writing the request — the ledgers hold facts the brief does not,
and a request that contradicts them wastes the round trip.

Put anything longer than a sentence in a file and pass `@path`.

### 2. Pick samples deliberately

`--sample` attaches published prose as a register reference. The
context window is large; two to five is reasonable. Choose scenes
adjacent in voice and situation, not just adjacent in number.

Note that samples anchor hard. If the user is testing whether the brief
carries on its own, run without them first and compare.

### 3. Generate

```sh
tools/scene-gen.py -r "@req.md" -s prose/ch73-scene06.md
```

Use `--dry-run` first when the brief or samples changed, to check what
is actually being sent. Output lands in `tools/out/` with a header
recording the served build.

If the run warns that an alias re-pointed, tell the user before
discussing quality — a difference from the last run may be the model,
not their edit.

### 3a. Inline gaps are a different job

When the explicit passage sits *inside* prose this session wrote, do
not ask for a whole scene. Write the scene to the edge of the gap, mark
it, and let the tool bridge the two ends:

```
<!-- GAP: what happens here -->
```

```sh
tools/scene-gen.py --fill prose/ch67-scene04.md --splice
```

Write the marker text as a director's note — what happens and what it
has to accomplish — not as a description of the prose you want.

**Judge an insert at its joins first.** A short one is harder than a
whole scene, because finished paragraphs sit directly above and below
it and any drift in rhythm shows. If a join reads as a step, that is
the finding; the content between them is secondary.

`--splice` keeps the original as `<file>.pre-fill`. Check the joins,
then delete it — do not commit it.

### 4. Review — this is the part that earns the loop

Read the draft against the fixed canon in section 6 of the brief and
against `design/threads.md` for the surrounding chapters. Report:

1. **Canon contradictions.** Anything that conflicts with what is
   already on the page. Quote both sides.
2. **Voice drift.** Does he still sound like himself under load? The
   analytical apparatus should keep running at a distance, not switch
   off and hand over to a generic narrator. This is the main failure.
3. **Missing humour.** Sixty lines without a dry note means the
   character has been lost.
4. **Staging.** Apply section 5 of the brief. Could a reader draw it?
   Does every action land a consequence in the other body? If two beats
   can be swapped unnoticed, the chain is broken.
5. **Lifted phrasing.** Samples are a register reference. Check the
   draft has not reused their sentences or images.

Be specific and quote lines. A verdict without a quotation is not
usable.

### 5. Revise

Revisions go back through the generator with the notes appended to the
request — not by rewriting the prose in this session. **This session
does not write the explicit passages.** It specifies, audits and edits
structure and continuity; the outside model writes the content. Say so
plainly if asked, once, and carry on with the part that is available.

Non-explicit material — a scene's framing paragraphs, the surrounding
narration, continuity fixes — is ordinary work and is not covered by
that line.

### 6. Land it

Only on the user's say-so. Accepted prose goes to `prose/` on the
house conventions: scene header, 78-character wrap, one POV per scene.
Update `design/threads.md` and `design/timeline.md` for the chapter,
and add a REVISED ON THE PAGE note to the chapter plan if the draft
changed anything the plan asserted.

## Files

| Path | What |
|---|---|
| `tools/scene-gen.py` | the client; `--help` for options |
| `tools/briefs/` | system prompts, one per pairing |
| `tools/out/` | generated drafts, gitignored |
| `tools/README.md` | setup, model slugs, flags |
