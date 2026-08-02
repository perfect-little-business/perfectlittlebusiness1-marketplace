#!/usr/bin/env python3
"""
voice_check.py - deterministic, brand-agnostic voice-QA pass.

Catches the universal "this reads like AI / weak writing" tells (em/en-dashes,
filler amplifiers, AI-slop constructions) so the model can focus on your brand's
OWN rules - loaded from your brand voice file - and the judgment calls
(zombie nouns, voice feel, demonstrate-don't-narrate).

Usage:
    python3 voice_check.py <draft_file> [--surface <type>]

    --surface is optional and only widens or narrows two prose checks. Any
    value not in NON_BRAND_VOICED (the default) is treated as brand-voiced
    prose. Pass --surface reference (or spec / internal / technical) for a
    spec or reference doc, where deliberately formal prose is correct and the
    longhand FAIL and contraction floor would be noise.

Exit code 0 = no FAILs found. Exit code 1 = at least one FAIL.

This is a first-pass scanner, NOT the whole rubric. The skill applies your
brand-specific checks (from your voice rules) and the judgment checks on top.
Your brand's own voice rules are always the final authority.

2026-08-02 revision. A banned construction shipped in a real document
("It is not a separate product ... It is the reason ...") and scored clean,
because the check grepped for the *contracted examples* of the X-not-Y flip
instead of the *pattern* they illustrate. The same construction written
longhand matched nothing. Three checks were added:
  1. CONTRAST_FLIP - pattern-based X-not-Y detection, longhand and contracted
  2. flip density   - legitimate individually, a tic in volume
  3. contractions   - dodging (1) by writing longhand is its own AI tell

All three are universal AI-writing tells, not brand preferences, which is why
they belong in this brand-agnostic pass. Anything brand-specific still comes
from your voice file.
"""

import re
import sys

# ---- FAIL: em/en-dashes are the strongest "written by AI" tell ----
DASHES = {
    "em-dash (—)": "—",
    "en-dash (–)": "–",
}

# Surfaces that are NOT brand-voiced prose. On these, the longhand FAIL and the
# contraction floor are off: a spec, a reference doc, or an internal technical
# note is written formally on purpose. Everything else defaults to brand-voiced,
# because QA'ing a brand-voiced draft is what this skill is for.
NON_BRAND_VOICED = ("reference", "spec", "internal", "technical", "code")

# ---- FAIL: longhand where a conversational voice would contract ----
# Writing these out is how a draft dodges the X-not-Y check below and lands in
# zero-contraction prose, which is itself the tell.
#
# A bare bigram match is wrong twice over, and both were caught on real copy:
#   "month one of it is training"  - "it" is the object of "of"; the "is"
#                                    belongs to a different subject
#   "so nobody has to guess where you are."  - a clause-final copula cannot
#                                    contract in English ("where you're." is
#                                    ungrammatical)
# So candidates are filtered on the word before and the character after.
COPULA_PAIR = re.compile(r"\b(it|that|there|you)\s+(is|are)\b", re.IGNORECASE)
NEGATOR = re.compile(r"\b(?:is not|do not|does not|cannot)\b", re.IGNORECASE)
PREV_WORD = re.compile(r"([\w'’-]+)\s*$")

# The pronoun only counts as a SUBJECT if it starts a clause. Whitelisting
# clause starts beats blacklisting prepositions: a blacklist missed "the only
# way to do that is to share my timeline", where "that" is the object of "do"
# and "is" belongs to "the only way".
CLAUSE_OPENERS = {
    "and", "but", "so", "because", "or", "yet", "then", "if", "when",
    "while", "although", "though", "since", "unless", "until", "however",
    "therefore", "meanwhile", "also", "plus", "still", "besides",
}
OPENER_PUNCT = ".!?:;,…"
# markdown furniture to see past when looking for the real preceding token
MD_TRIM = " \t*_~`>#|-“”\"'‘’([{"
CLAUSE_END = ".,;:!?)]\"'”’"

# Contraction tokens that cannot be mistaken for a possessive. Undercounts
# slightly ("Melissa's the hub" is not counted); the threshold is set against
# measured real drafts, so the undercount is already priced in.
CONTRACTION = re.compile(
    r"\b\w+n[''’]t\b"
    r"|\b\w+[''’](?:re|ve|ll|m|d)\b"
    r"|\b(?:it|that|there|here|what|who|let|he|she|how|where)[''’]s\b",
    re.IGNORECASE,
)

# ---- FLAG: the X-not-Y contrast flip, as a PATTERN not as examples ----
# The rule is the shape, not the spelling. These cover longhand, contracted,
# and negative-contraction forms, plus noun subjects and the but/rather form.
_NEG_OPEN = r"(?:it|this|that)(?:[''’]s|\s+is|\s+was)\s+not|(?:it|this|that)\s+(?:is|was)n[''’]?t"
_POS_CLOSE = r"(?:it|this|that)(?:[''’]s|\s+is|\s+was)"
_HEDGE = r"(?:just\s+|only\s+|merely\s+|simply\s+)?"

CONTRAST_FLIP = [
    # It is not X. It is Y.  /  It's not just X, it's Y.  /  This isn't X, this is Y.
    r"\b(?:" + _NEG_OPEN + r")\s+" + _HEDGE + r"[^.?!\n]{2,90}?[.,;:]\s+(?:and\s+|but\s+)?(?:" + _POS_CLOSE + r")\b",
    # ... is not X, it is Y  (subject is a noun, not a pronoun)
    r"\b(?:is|are|was|were)\s+not\s+" + _HEDGE + r"[^.?!\n]{2,90}?,\s+(?:it|they|that|this|these|those)\s+(?:is|are|was|were)\b",
    # not a X but a Y  /  not just X but Y  /  not the X rather the Y
    r"\bnot\s+(?:a|an|the|just|only|merely|simply)\s+[^.?!\n]{2,70}?\s+(?:but|rather)\b",
]

# Legacy loose forms from the original list, kept so nothing that used to be
# caught silently stops being caught.
CONTRAST_FLIP_LEGACY = [
    r"it'?s not (just )?[\w\s]+?[,.]? it'?s",
    r"this isn'?t [\w\s]+?[,.]? this is",
]

# ---- FLAG: universal AI-slop constructions ----
BANNED_CONSTRUCTIONS = [
    r"here'?s the thing",
    r"here'?s what most people miss",
    r"the truth is",
    r"what if i told you",
    r"imagine this",
    r"picture (this|yourself)",
    r"in a world where",
    r"let me explain",
    r"let'?s break this down",
    r"whether you'?re [\w\s]+? or ",
    r"more than just ",
    r"not your average ",
    r"^\s*(look|listen),",
    r"trust me when i say",
    r"let'?s be honest",
    r"that'?s where [\w\s]+? comes in",
]

# ---- FLAG: universal filler / AI amplifiers ----
BANNED_WORDS = [
    r"\bleverage(s|d|ing)?\b", r"\bnavigat(e|es|ed|ing)\b", r"\brobust\b",
    r"\bseamless(ly)?\b", r"\belevate(s|d|ing)?\b", r"\bunleash(es|ed|ing)?\b",
    r"\bunlock(s|ed|ing)?\b", r"\btransformative\b", r"\bgame-?changer\b",
    r"\bdeep dive\b", r"\bcrucial\b", r"\bvital\b", r"\bessential\b",
    r"\btruly\b", r"\breally\b", r"\bvery\b", r"\bactually\b",
    r"\bpowerful\b", r"\brevolutionary\b", r"\bcutting-?edge\b",
    r"\bnext-?level\b", r"\bworld-?class\b", r"\bultimate\b",
]

# ---- WARN: density. Each instance is fine; the volume is the tell. ----
TRAILING_FLIP = re.compile(r",\s+not\s+\S|\brather than\b", re.IGNORECASE)
FLIP_PER_1K_WARN = 2.0
CONTRACTIONS_PER_1K_WARN = 15.0


def _is_clause_start(prefix):
    """True if what precedes the pronoun leaves it heading its own clause."""
    p = prefix.rstrip(MD_TRIM)
    if not p:
        return True                                   # start of line
    if p[-1] in OPENER_PUNCT:
        return True                                   # ". It is" / ", there is"
    m = PREV_WORD.search(p)
    return bool(m and m.group(1).lower() in CLAUSE_OPENERS)


def _longhand_hits(ln):
    """Longhand pairs on this line that could genuinely have been contracted."""
    spans = []

    for m in COPULA_PAIR.finditer(ln):
        pron, cop = m.group(1).lower(), m.group(2).lower()
        if (pron == "you") != (cop == "are"):
            continue                                  # "there are", "you is"
        if not _is_clause_start(ln[: m.start()]):
            continue                                  # "of it is", "do that is"
        rest = ln[m.end():].lstrip()
        if not rest or rest[0] in CLAUSE_END:
            continue                                  # clause-final copula
        spans.append((m.start(), m.end(), m.group(0)))

    for m in NEGATOR.finditer(ln):
        rest = ln[m.end():].lstrip()
        if rest and rest[0] in CLAUSE_END:
            continue
        spans.append((m.start(), m.end(), m.group(0)))

    # "there is not X" matches both patterns; report the span once
    spans.sort()
    kept = []
    for s, e, txt in spans:
        if kept and s < kept[-1][1]:
            continue
        kept.append((s, e, txt))
    return [txt for _, _, txt in kept]


def _strip_code_fences(lines):
    """Return lines with fenced code blocks blanked out (still line-aligned)."""
    out, in_fence = [], False
    for ln in lines:
        if ln.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else ln)
    return out


def scan(path, surface="draft"):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.readlines()
    lines = _strip_code_fences(raw)
    text = "".join(lines)

    brand_voiced = surface.lower() not in NON_BRAND_VOICED

    fails, flags, warns = [], [], []

    # FAILs: dashes
    for label, ch in DASHES.items():
        for i, ln in enumerate(lines, 1):
            if ch in ln:
                fails.append((i, label, ln.strip()[:80]))

    # FAILs: longhand where the voice would contract. Blockquoted lines are
    # exempt: a verbatim quote of what someone actually said is not your prose.
    if brand_voiced:
        for i, ln in enumerate(lines, 1):
            if ln.lstrip().startswith(">"):
                continue
            for hit in _longhand_hits(ln):
                fails.append((i, 'longhand "%s" (contract it)' % hit, ln.strip()[:80]))

    # FLAGs: constructions + filler words
    for i, ln in enumerate(lines, 1):
        low_ln = ln.lower()

        # one flag per line for the whole contrast-flip family, so overlapping
        # patterns on the same sentence report once
        for pat in CONTRAST_FLIP + CONTRAST_FLIP_LEGACY:
            if re.search(pat, low_ln, re.IGNORECASE):
                flags.append((i, "banned construction: X-not-Y contrast flip", ln.strip()[:80]))
                break

        for pat in BANNED_CONSTRUCTIONS:
            if re.search(pat, low_ln, re.IGNORECASE):
                flags.append((i, "banned construction", ln.strip()[:80]))
        for pat in BANNED_WORDS:
            for m in re.finditer(pat, low_ln):
                flags.append((i, "filler/amplifier: %s" % m.group(0), ln.strip()[:80]))

    # ---- density checks ----
    words = len(re.findall(r"\b[\w'’-]+\b", text)) or 1
    per_1k = 1000.0 / words

    flips = len(TRAILING_FLIP.findall(text))
    flip_rate = flips * per_1k
    if flip_rate > FLIP_PER_1K_WARN:
        warns.append((0, "contrast-flip density %.1f per 1k words (%d in %d) - reads as a tic above %.1f"
                      % (flip_rate, flips, words, FLIP_PER_1K_WARN), ""))

    contractions = len(CONTRACTION.findall(text))
    contraction_rate = contractions * per_1k
    if brand_voiced and contraction_rate < CONTRACTIONS_PER_1K_WARN:
        warns.append((0, "contraction density %.1f per 1k words (%d in %d) - below %.1f reads stiff/AI"
                      % (contraction_rate, contractions, words, CONTRACTIONS_PER_1K_WARN), ""))

    stats = {
        "words": words,
        "flips": flips,
        "flip_rate": flip_rate,
        "contractions": contractions,
        "contraction_rate": contraction_rate,
        "brand_voiced": brand_voiced,
    }
    return fails, flags, warns, stats


def main():
    if len(sys.argv) < 2:
        print("usage: voice_check.py <draft_file> [--surface <type>]")
        sys.exit(2)
    path = sys.argv[1]
    surface = "draft"
    if "--surface" in sys.argv:
        surface = sys.argv[sys.argv.index("--surface") + 1]

    fails, flags, warns, st = scan(path, surface)

    print("VOICE QA (deterministic pass) - surface: %s%s"
          % (surface, "" if st["brand_voiced"] else " (not brand-voiced)"))
    print("=" * 52)
    if not fails:
        print("VERDICT: no mechanical FAILs ✅  (brand + judgment checks still required)")
    else:
        print("VERDICT: FAIL ❌  (%d must-fix)" % len(fails))

    if fails:
        print("\nMUST FIX (FAIL):")
        for ln, rule, txt in fails:
            loc = "line %d" % ln if ln else "document"
            print('  [%s] %s' % (loc, rule) + (('  "%s"' % txt) if txt else ""))

    if flags:
        print("\nREVISE (FLAG) - %d:" % len(flags))
        for ln, rule, txt in flags:
            loc = "line %d" % ln if ln else "document"
            print('  [%s] %s' % (loc, rule) + (('  "%s"' % txt) if txt else ""))

    if warns:
        print("\nWARN - %d:" % len(warns))
        for ln, rule, txt in warns:
            loc = "line %d" % ln if ln else "document"
            print('  [%s] %s' % (loc, rule) + (('  "%s"' % txt) if txt else ""))

    print("\nDENSITY: %d words | contrast flips %d (%.1f/1k, warn >%.1f) | contractions %d (%.1f/1k, warn <%.1f)"
          % (st["words"], st["flips"], st["flip_rate"], FLIP_PER_1K_WARN,
             st["contractions"], st["contraction_rate"], CONTRACTIONS_PER_1K_WARN))
    print("\nReminder: this is the universal mechanical pass only. Apply your")
    print("brand's own voice rules and the judgment checks (zombie nouns,")
    print("voice feel, demonstrate-don't-narrate) on top. Verbatim quotes")
    print("(blockquoted lines) are exempt from the longhand FAIL.")

    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
