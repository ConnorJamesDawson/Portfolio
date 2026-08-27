# Blind trial — raw artifacts

Test method and results: `../continuity-methods-findings.md` §7.

The design was reconstructed at **`e0dc697`** — the commit at which the creed
error was live, before `falsified.md` #16 killed it. Three workers read only
that tree; none was told an error existed, or what was being tested.

| File | What it is |
|---|---|
| `vocab.json` | 204 state atoms, derived blind from the design files |
| `ledger.json` | 204 acquisition rows, dated, with qualifier and provenance |
| `plan.json` | `month`/`requires`/`grants` for ch10 (11 scenes) and ch11 (10) |
| `check.py` | the precondition check |

Reproduce:

    python3 check.py ledger.json plan.json

**Result: zero precondition violations, strict and loose.** The check did not
catch the creed error. Why, and what it caught instead, is §7.
