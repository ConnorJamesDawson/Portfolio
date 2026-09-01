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
        for choice in obj.get("choices", []):
            piece = (choice.get("delta") or {}).get("content")
            if piece:
                chunks.append(piece)
                sys.stdout.write(piece)
                sys.stdout.flush()
            if choice.get("finish_reason"):
                finish = choice["finish_reason"]
    print()
    return "".join(chunks), finish


def save(args, text, finish, request_text, samples):
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    slug = re.sub(r"[^a-z0-9]+", "-", args.model.lower()).strip("-")
    path = out_dir / f"{stamp}-{slug}.md"
    header = [
        f"<!-- model: {args.model}",
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

    if not args.request:
        ap.error("--request is required (or --list-models)")
    if not args.model and not args.dry_run:
        ap.error("--model is required; run --list-models to find one")

    request_text = args.request
    if request_text.startswith("@"):
        request_text = read(request_text[1:], "request file")

    brief = read(args.brief, "brief")
    check_slot(brief, args.brief)

    samples = [(p, read(p, "sample")) for p in args.sample]
    messages = build_messages(brief, request_text, samples)

    if args.dry_run:
        for msg in messages:
            print(f"===== {msg['role'].upper()} "
                  f"({word_count(msg['content'])} words) =====")
            print(msg["content"])
            print()
        return

    text, finish = generate(args, messages)
    if not text.strip():
        die("model returned nothing")

    path = save(args, text, finish, request_text, samples)
    print(f"\n--- {word_count(text)} words, finish_reason={finish}",
          file=sys.stderr)
    print(f"--- saved to {path}", file=sys.stderr)
    if finish == "length":
        print("--- truncated: raise --max-tokens", file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted", file=sys.stderr)
        raise SystemExit(130)
