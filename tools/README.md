# scene-gen

Sends a scene brief to a model on OpenRouter and saves what comes back.
Stdlib Python 3 only — nothing to install.

It exists so drafting a scene with an outside model is one command
instead of assembling a prompt by hand and pasting it into a chat
window.

## Setup

```sh
export OPENROUTER_API_KEY='sk-or-...'      # https://openrouter.ai/keys
```

Put it in your shell profile or a `.env` you source. **Do not commit
it** — `.env` and `tools/out/` are both gitignored.

## Find a model

OpenRouter slugs change and new ones appear constantly, so look the id
up rather than guessing it:

```sh
tools/scene-gen.py --list-models deepseek
```

Prints id, context length, and per-million input/output price for
everything matching. Pin the one you want:

```sh
export SCENE_GEN_MODEL='deepseek/deepseek-v4-flash-0731'
```

### DeepSeek V4 Flash

| Slug | What it is |
|---|---|
| `deepseek/deepseek-v4-flash-latest` | alias; re-points to the newest build in the family |
| `deepseek/deepseek-v4-flash-0731` | the 31 Jul 2026 re-post-trained build |
| `deepseek/deepseek-v4-flash` | the 0423 preview |
| `deepseek/deepseek-v4-flash-vision-exp` | vision variant |
| `deepseek/deepseek-v4-pro` | the larger sibling |

Roughly $0.03/M in and $0.16/M out, with a 1.3M-token context and up to
393k completion tokens. At that price a 4,000-word scene off a 4,000-word
prompt costs well under a cent, so run the comparisons.

**Prefer a dated build over `-latest` for anything you are measuring.**
An alias silently re-points, and then a change in output quality could be
your brief or could be a new model underneath you, with no way to tell
which. That defeats the header this tool writes into every result. Use
`-latest` for casual drafting and a pinned build whenever you are
comparing two prompts.

The 1.3M context also means style samples are effectively free — attach
several rather than agonising over which two.

## Generate

```sh
tools/scene-gen.py \
    --request "The morning after ch73 s6. Tsunade POV. She wakes first." \
    --sample prose/ch73-scene06.md \
    --sample prose/ch70-scene10.md
```

Output streams to the terminal and is saved to
`tools/out/<timestamp>-<model>.md` with a header recording the model,
temperature, brief, samples and finish reason — so a good result is
reproducible and a bad one is diagnosable.

`--request @path/to/file.md` reads the ask from a file instead, which
is easier for anything longer than a sentence.

## Options

| Flag | Default | Notes |
|---|---|---|
| `--model` / `-m` | `$SCENE_GEN_MODEL` | OpenRouter model id |
| `--brief` / `-b` | `tools/briefs/sazare-tsunade.md` | the system prompt |
| `--request` / `-r` | — | required; `@file` to read from disk |
| `--sample` / `-s` | none | prose file as style reference; repeatable |
| `--temperature` / `-t` | `0.9` | |
| `--top-p` | unset | omitted from the request unless given |
| `--max-tokens` | `4000` | ~2,800 words; raise for longer scenes |
| `--out-dir` | `tools/out` | |
| `--dry-run` | — | print the assembled prompt, make no API call |

Use `--dry-run` before spending tokens on a new brief. It prints each
message with a word count, which is also the fastest way to catch a
sample you didn't mean to attach.

## Briefs

`tools/briefs/` holds the system prompts. `sazare-tsunade.md` covers
the two characters, their voices, the state of the relationship, the
staging discipline, and the canon a scene must not contradict.

**Section 7 of that brief is a placeholder.** It is where the
explicitness level and the acts in frame get specified, and it is the
author's to write. The tool warns on every run until the
`FILL THIS IN YOURSELF` marker is gone from the heading.

Copy the file to start a brief for a different pairing or a different
book.

## Style samples

Attaching published scenes transmits voice far better than describing
it — but it anchors hard, and you can get pastiche instead of a real
test of whether the brief carries on its own.

Worth running both ways and comparing:

```sh
tools/scene-gen.py -r "@req.md"                          # brief only
tools/scene-gen.py -r "@req.md" -s prose/ch73-scene06.md # with sample
```

The system prompt tells the model samples are a register reference and
not material to remix, but check the output for lifted phrasing anyway.
