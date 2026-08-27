#!/usr/bin/env python3
"""Precondition check over a scene plan and an acquisition ledger.

Fires only when the EARLIEST POSSIBLE acquisition of an atom is strictly after
the month of a scene that requires it. Imprecise dates therefore cannot produce
a false positive -- the Gramps strict/loose split, transposed.
"""
import json, re, sys
from collections import defaultdict

def parse_month(s):
    """'Y0M12' -> 12 ; 'Y1M?' -> None (year known, month not)."""
    if not s: return (None, None)
    m = re.match(r'^Y(-?\d+)M(\d+|\?)$', s.strip())
    if not m: return (None, None)
    y = int(m.group(1))
    if m.group(2) == '?': return (y, None)
    return (y, int(m.group(2)))

def earliest(row):
    """Earliest story-month index at which the atom could possibly be held."""
    y, mo = parse_month(row.get('story_month'))
    if y is None: return None
    q = (row.get('qualifier') or 'RULED').upper()
    if q == 'BEF':            # acquired at some point before x -> no lower bound
        return None
    base = y * 12 + (mo if mo is not None else 1)   # 'M?' -> earliest in that year
    if q == 'ABT':
        return base - 2       # allow slack either side of an approximate date
    return base               # RULED / CAL / BET / AFT all lower-bound at x

def is_exact(row):
    y, mo = parse_month(row.get('story_month'))
    return (row.get('qualifier') or '').upper() == 'RULED' and mo is not None

def run(ledger, plan, strict):
    acq = defaultdict(list)
    for r in ledger.get('rows', []):
        if strict and not is_exact(r): continue
        e = earliest(r)
        if e is None: continue
        acq[r['atom_id']].append((e, r))

    errors, dangling, required, granted = [], [], set(), set()
    for ch in plan.get('chapters', []):
        for sc in ch.get('scenes', []):
            y, mo = parse_month(sc.get('month'))
            smi = None if y is None else y * 12 + (mo if mo is not None else 12)
            for a in sc.get('grants', []) or []: granted.add(a)
            for a in sc.get('requires', []) or []:
                required.add(a)
                if a not in acq:
                    dangling.append((ch['chapter'], sc['n'], sc.get('month'), a))
                    continue
                if smi is None: continue
                first, row = min(acq[a], key=lambda t: t[0])
                if first > smi:
                    errors.append({
                        'chapter': ch['chapter'], 'scene': sc['n'],
                        'scene_month': sc.get('month'), 'atom': a,
                        'acquired': row.get('story_month'),
                        'qualifier': row.get('qualifier'),
                        'provenance': row.get('provenance'),
                        'gap_months': first - smi,
                        'event': row.get('acquiring_event', ''),
                    })
    return errors, dangling, required, granted

def main(lp, pp):
    ledger, plan = json.load(open(lp)), json.load(open(pp))
    for strict in (True, False):
        errs, dang, req, gr = run(ledger, plan, strict)
        mode = 'STRICT (only pinned, author-ruled dates count)' if strict else \
               'LOOSE  (calculated and approximate dates count too)'
        print(f'\n{"="*72}\n{mode}\n{"="*72}')
        if not errs:
            print('  no precondition violations')
        for e in sorted(errs, key=lambda x: -x['gap_months']):
            print(f"  ERROR  {e['chapter']} scene {e['scene']} ({e['scene_month']}): "
                  f"requires {e['atom']}")
            print(f"         not acquired until {e['acquired']} [{e['qualifier']}"
                  f"/{e['provenance']}] — {e['gap_months']} months later")
            if e['event']: print(f"         acquiring event: {e['event']}")
        if strict: continue
        print(f'\n  -- dangling (required, never in the ledger) --')
        for c, s, m, a in dang or []: print(f'     {c} scene {s} ({m}): {a}')
        if not dang: print('     none')
        print(f'\n  -- zero-count (granted by a scene, required by none) --')
        z = sorted(gr - req)
        for a in z: print(f'     {a}')
        if not z: print('     none')
        print(f'\n  counts: {len(req)} atoms required, {len(gr)} granted, '
              f'{len(ledger.get("rows", []))} ledger rows')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
