#!/usr/bin/env python3
"""Send a scene brief to an OpenRouter model and save the result.

Stdlib only -- no pip install. See tools/README.md.
"""

import argparse
import datetime as _dt
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

API_ROOT = "https://openrouter.ai/api/v1"
REPO = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_BRIEF = REPO / "tools" / "briefs" / "sazare-tsunade.md"
DEFAULT_OUT = REPO / "tools" / "out"


def die(msg, code=1):
    print(f"scene-gen: {msg}", file=sys.stderr)
    raise SystemExit(code)


def api_key():
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        die("OPENROUTER_API_KEY is not set.\n"
            "  export OPENROUTER_API_KEY='sk-or-...'\n"
            "Get one at https://openrouter.ai/keys")
    return key


def request(path, payload=None, stream=False, timeout=600):
    url = f"{API_ROOT}{path}"
    headers = {
        "Authorization": f"Bearer {api_key()}",
        "Content-Type": "application/json",
        # OpenRouter uses these for its dashboard attribution. Harmless.
        "HTTP-Referer": "https://localhost/scene-gen",
        "X-Title": "scene-gen",
    }
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers,
                                 method="POST" if data else "GET")
    try:
        return urllib.request.urlopen(req, timeout=timeout)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            body = json.dumps(json.loads(body), indent=2)
        except ValueError:
            pass
        die(f"HTTP {e.code} from OpenRouter:\n{body}")
    except urllib.error.URLError as e:
        die(f"could not reach OpenRouter: {e.reason}")


# --------------------------------------------------------------- models

def list_models(pattern):
    models = json.load(request("/models"))["data"]
    rx = re.compile(pattern, re.I) if pattern else None
    rows = []
    for m in models:
        mid = m.get("id", "")
        if rx and not (rx.search(mid) or rx.search(m.get("name", ""))):
            continue
        pricing = m.get("pricing", {}) or {}

        def per_m(v):
            try:
                return f"${float(v) * 1e6:.2f}"
            except (TypeError, ValueError):
                return "?"

        rows.append((mid, str(m.get("context_length", "?")),
                     per_m(pricing.get("prompt")),
                     per_m(pricing.get("completion"))))
    if not rows:
        die(f"no models matched {pattern!r}")
    rows.sort()
    w = max(len(r[0]) for r in rows)
    print(f"{'MODEL'.ljust(w)}  {'CTX':>9}  {'IN/M':>9}  {'OUT/M':>9}")
    for mid, ctx, pin, pout in rows:
        print(f"{mid.ljust(w)}  {ctx:>9}  {pin:>9}  {pout:>9}")
    print(f"\n{len(rows)} model(s). Pass one to --model.")


# ---------------------------------------------------------------- prompt

# The brief ships with section 7 as an unfilled placeholder. The author
# replaces that heading when they write their own spec into it, so the
# marker's presence is a reliable "still a stub" signal.
SLOT_STUB = "FILL THIS IN YOURSELF"


def read(path, label):
    p = pathlib.Path(path)
    if not p.is_file():
        die(f"{label} not found: {p}")
    return p.read_text(encoding="utf-8")


def check_slot(brief, path):
    """Warn if the author's explicit-register section is still a stub."""
    if SLOT_STUB not in brief:
        return
    print(f"scene-gen: warning -- section 7 of {path} is still the\n"
          "  placeholder. That section is where you specify explicitness\n"
          "  and which acts are in frame; edit it and remove the\n"
          f"  '{SLOT_STUB}' marker from the heading. Without it the model\n"
          "  averages across every book that isn't yours.\n",
          file=sys.stderr)


GAP = re.compile(r"<!--\s*GAP:\s*(.*?)-->", re.S)


def split_gap(path, context_words):
    """Find <!-- GAP: ... --> and return the prose either side of it.

    The model matching a voice does far better shown both edges than
    told about them, and a seam is what an inline insert fails at."""
    text = read(path, "gap file")
    hits = list(GAP.finditer(text))
    if not hits:
        die(f"no <!-- GAP: ... --> marker in {path}")
    if len(hits) > 1:
        die(f"{len(hits)} GAP markers in {path}; fill one at a time")
    m = hits[0]
    return (text, m, m.group(1).strip(),
            _tail_words(text[:m.start()], context_words),
            _head_words(text[m.end():], context_words))


def _tail_words(text, n):
    """Last n words, with line breaks intact.

    Slicing the original string rather than rejoining split() keeps the
    paragraphing -- which is the thing the fill has to match."""
    words = list(re.finditer(r"\S+", text))
    return text if len(words) <= n else text[words[-n].start():]


def _head_words(text, n):
    words = list(re.finditer(r"\S+", text))
    return text if len(words) <= n else text[:words[n - 1].end()]


def build_fill_messages(brief, instruction, before, after, target, samples):
    system = [brief]
    if samples:
        system.append(
            "\n\n---\n\n# STYLE SAMPLES\n\n"
            "Published prose from this novel. Match the voice, interior\n"
            "grammar and paragraph rhythm. Do NOT reuse their sentences,\n"
            "images or beats -- they are a register reference, not source\n"
            "material to remix."
        )
        for path, text in samples:
            system.append(f"\n\n## SAMPLE: {path}\n\n{text}")

    user = f"""You are filling a gap inside an existing scene. The prose
either side of it is final and will not be edited, so your passage has
to join onto both ends without a visible seam.

# WHAT GOES IN THE GAP

{instruction}

# THE PROSE IMMEDIATELY BEFORE THE GAP

{before}

# THE PROSE IMMEDIATELY AFTER THE GAP

{after}

# RULES

- Roughly {target} words. Length is a target, not a quota; a seam that
  works at two thirds of it beats padding.
- **Start where the before-text stops.** Do not re-establish position,
  restate what it already said, or recap the moment leading in. It has
  happened; the reader was there.
- **End so the after-text follows without a step.** Read its first
  sentence and make yours the one it wants to come after.
- Match the sentence rhythm and paragraph length of the surrounding
  prose exactly. That, not vocabulary, is what a reader notices.
- Same interior grammar as the passage around it. If the before-text
  is in his italics and counting, yours counts too.
- Output the gap text ONLY. No heading, no framing, no note, and do
  not repeat any part of the before- or after-text."""

    return [
        {"role": "system", "content": "".join(system)},
        {"role": "user", "content": user},
    ]


def build_messages(brief, request_text, samples):
    system = [brief]
    if samples:
        system.append(
            "\n\n---\n\n# STYLE SAMPLES\n\n"
            "Published prose from this novel. Match the voice, interior\n"
            "grammar and paragraph rhythm. Do NOT reuse their sentences,\n"
            "images or beats -- they are a register reference, not source\n"
            "material to remix."
        )
        for path, text in samples:
            system.append(f"\n\n## SAMPLE: {path}\n\n{text}")
    return [
        {"role": "system", "content": "".join(system)},
        {"role": "user", "content": request_text},
    ]


# ------------------------------------------------------------ generation

def generate(args, messages):
    payload = {
        "model": args.model,
        "messages": messages,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "stream": True,
    }
    if args.top_p is not None:
        payload["top_p"] = args.top_p

    resp = request("/chat/completions", payload, stream=True)
    chunks, finish = [], None
    # An alias like ...-flash-latest resolves server-side; the response
    # reports which build actually served the request. Record that, or a
    # result generated months apart is not reproducible.
    served, gen_id = None, None
    for raw in resp:
        line = raw.decode("utf-8", "replace").strip()
        if not line.startswith("data:"):
            continue
        data = line[5:].strip()
        if data == "[DONE]":
            break
        try:
            obj = json.loads(data)
        except ValueError:
            continue
        if obj.get("error"):
            print()
            die(f"stream error: {json.dumps(obj['error'], indent=2)}")
        served = obj.get("model") or served
        gen_id = obj.get("id") or gen_id
        for choice in obj.get("choices", []):
            piece = (choice.get("delta") or {}).get("content")
            if piece:
                chunks.append(piece)
                sys.stdout.write(piece)
                sys.stdout.flush()
            if choice.get("finish_reason"):
                finish = choice["finish_reason"]
    print()
    return "".join(chunks), finish, served, gen_id


def save(args, text, finish, served, gen_id, request_text, samples):
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    # Name the file after the build that served it, so an alias does not
    # collapse two different models into one filename.
    slug = re.sub(r"[^a-z0-9]+", "-", (served or args.model).lower()).strip("-")
    path = out_dir / f"{stamp}-{slug}.md"
    header = [
        f"<!-- requested_model: {args.model}",
        f"     served_model: {served or 'unreported'}",
        f"     generation_id: {gen_id or 'unreported'}",
        f"     temperature: {args.temperature}  max_tokens: {args.max_tokens}",
        f"     brief: {args.brief}",
        f"     samples: {', '.join(p for p, _ in samples) or 'none'}",
        f"     finish_reason: {finish}",
        f"     generated: {stamp}",
        f"     request: {request_text.strip()[:300]}",
        "-->",
        "",
    ]
    path.write_text("\n".join(header) + text.rstrip() + "\n", encoding="utf-8")
    return path


def note_drift(args, served):
    """Say so, loudly, when an alias starts resolving somewhere new.

    Comparing two prompts across a silent model change misattributes the
    difference to the prompt, so the change has to be visible."""
    stamp_file = pathlib.Path(args.out_dir) / ".resolved.json"
    try:
        seen = json.loads(stamp_file.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        seen = {}
    previous = seen.get(args.model)
    if previous and previous != served:
        print(f"\n!!! {args.model} previously resolved to {previous}.\n"
              f"!!! It now resolves to {served}.\n"
              "!!! Results before and after this point are NOT comparable.\n"
              f"!!! Pin {previous} or {served} to compare prompts.\n",
              file=sys.stderr)
    seen[args.model] = served
    try:
        stamp_file.write_text(json.dumps(seen, indent=2), encoding="utf-8")
    except OSError:
        pass


def splice(path, text, marker, filled):
    """Replace the marker in place, keeping the pre-fill copy alongside."""
    backup = pathlib.Path(f"{path}.pre-fill")
    backup.write_text(text, encoding="utf-8")
    merged = text[:marker.start()] + filled.strip() + text[marker.end():]
    pathlib.Path(path).write_text(merged, encoding="utf-8")
    return backup


def word_count(text):
    return len([w for w in re.split(r"\s+", text) if w])


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser(
        description="Send a scene brief to an OpenRouter model.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""examples:
  # find the model id you want (OpenRouter slugs change; don't guess)
  scene-gen.py --list-models deepseek

  # generate, with two published scenes as a style reference
  scene-gen.py --model deepseek/deepseek-chat \\
      --request "The morning after ch73 s6. Tsunade POV." \\
      --sample prose/ch73-scene06.md --sample prose/ch70-scene10.md

  # fill a gap inside a scene you have already written, in place.
  # mark it first:  <!-- GAP: what happens here -->
  scene-gen.py --fill prose/ch67-scene04.md --splice \
      --target-words 250 --sample prose/ch73-scene06.md
""")
    ap.add_argument("--list-models", nargs="?", const="", metavar="FILTER",
                    help="list available models (optional regex filter) "
                         "and exit")
    ap.add_argument("--model", "-m",
                    default=os.environ.get("SCENE_GEN_MODEL"),
                    help="OpenRouter model id (or set SCENE_GEN_MODEL)")
    ap.add_argument("--brief", "-b", default=str(DEFAULT_BRIEF),
                    help=f"brief file (default: {DEFAULT_BRIEF.name})")
    ap.add_argument("--request", "-r",
                    help="what to write; @path reads it from a file")
    ap.add_argument("--fill", "-f", metavar="PROSE_FILE",
                    help="fill a <!-- GAP: ... --> marker in an existing "
                         "scene, given the prose either side of it")
    ap.add_argument("--context-words", type=int, default=400,
                    help="words of prose to show each side of the gap "
                         "(default: 400)")
    ap.add_argument("--target-words", type=int, default=350,
                    help="rough length for the filled gap (default: 350)")
    ap.add_argument("--splice", action="store_true",
                    help="write the result back over the marker, keeping "
                         "a .pre-fill copy of the original")
    ap.add_argument("--sample", "-s", action="append", default=[],
                    metavar="PATH",
                    help="prose file to attach as a style sample "
                         "(repeatable)")
    ap.add_argument("--temperature", "-t", type=float, default=0.9)
    ap.add_argument("--top-p", type=float, default=None)
    ap.add_argument("--max-tokens", type=int, default=4000)
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT))
    ap.add_argument("--dry-run", action="store_true",
                    help="assemble and print the prompt; make no API call")
    args = ap.parse_args()

    if args.list_models is not None:
        list_models(args.list_models)
        return

    if not args.request and not args.fill:
        ap.error("one of --request or --fill is required "
                 "(or --list-models)")
    if args.request and args.fill:
        ap.error("--request and --fill are alternatives, not a pair")
    if args.splice and not args.fill:
        ap.error("--splice only applies to --fill")
    if not args.model and not args.dry_run:
        ap.error("--model is required; run --list-models to find one")

    brief = read(args.brief, "brief")
    check_slot(brief, args.brief)
    samples = [(p, read(p, "sample")) for p in args.sample]

    gap = None
    if args.fill:
        gap = split_gap(args.fill, args.context_words)
        _, _, instruction, before, after = gap
        request_text = f"[fill gap in {args.fill}] {instruction}"
        messages = build_fill_messages(brief, instruction, before, after,
                                       args.target_words, samples)
    else:
        request_text = args.request
        if request_text.startswith("@"):
            request_text = read(request_text[1:], "request file")
        messages = build_messages(brief, request_text, samples)

    if args.dry_run:
        for msg in messages:
            print(f"===== {msg['role'].upper()} "
                  f"({word_count(msg['content'])} words) =====")
            print(msg["content"])
            print()
        return

    text, finish, served, gen_id = generate(args, messages)
    if not text.strip():
        die("model returned nothing")

    path = save(args, text, finish, served, gen_id, request_text, samples)
    print(f"\n--- {word_count(text)} words, finish_reason={finish}",
          file=sys.stderr)
    if served and served != args.model:
        print(f"--- {args.model} resolved to {served}", file=sys.stderr)
        note_drift(args, served)
    print(f"--- saved to {path}", file=sys.stderr)
    if finish == "length":
        print("--- truncated: raise --max-tokens", file=sys.stderr)

    if args.splice:
        full_text, marker = gap[0], gap[1]
        backup = splice(args.fill, full_text, marker, text)
        print(f"--- spliced into {args.fill} "
              f"(original kept at {backup})", file=sys.stderr)
    elif args.fill:
        print("--- not spliced; pass --splice to write it in place",
              file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted", file=sys.stderr)
        raise SystemExit(130)
