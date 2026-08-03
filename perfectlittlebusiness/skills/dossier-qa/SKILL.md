---
name: dossier-qa
description: >
  Cross-check quality gate for Thought Leadership Dossiers. Compares a dossier
  (new draft or existing) against the OTHER dossiers in the brain and the
  Source of Truth, flagging term-ownership conflicts, topic overlap, fact
  contradictions, stale predictions, internal redundancy, and structural
  drift from the three-layer template. Use whenever the user says "dossier
  qa", "cross-check the dossier", "check the dossier against the brain",
  "audit my dossiers", "are my dossiers consistent", "any conflicts between
  dossiers", or as the final gate after gravity-dossier produces a draft
  (chained after voice-qa). Also run it standalone on the whole dossiers
  folder as a periodic hygiene audit. Report-only: it flags and proposes
  fixes but NEVER edits a dossier or brain file without explicit approval.
  Do NOT use it for voice/style checking — that is voice-qa's job.
---

# dossier-qa — Cross-Dossier Consistency Gate

voice-qa protects how a dossier *sounds*. This skill protects what the dossier
*claims* — against every other dossier in the brain. The failure it exists to
prevent: a downstream AI loads two dossiers, finds the same concept under two
names (or two dossiers claiming the same term), blends them, and ships copy
that contradicts the expert's own canon.

**Report-only.** This skill never edits a dossier and never writes to any
brain file. It produces a verdict report with proposed fixes. In chained mode
the calling skill (gravity-dossier) applies approved fixes; standalone, the
user approves each fix before anyone applies it.

---

## Inputs

- **Target**: one dossier file (chained mode / single audit), or the whole
  dossiers folder (standalone audit mode — check every dossier against every
  other).
- **BRAIN_PATH** — resolve the same way gravity-dossier does: explicit path →
  `PLB_BRAIN_PATH` env var → `./brain`. Dossiers live in
  `{BRAIN_PATH}/dossiers/` (including subfolders like `thought-leadership/`).
- **Reference set**: all sibling dossiers, plus the Source of Truth and offer
  docs if resolvable (role-based: `*sot*` / `*source*of*truth*` patterns or
  `brain-manifest.json`). If a sibling dossier is in the old flat format
  (no Metadata section), scan its full text for terms and facts instead of
  reading its term-ownership block — and flag the format drift (Check 6).

Ignore anything in archive folders (`_ARCHIVE`, `archive/`, files marked
retired or test) — retired dossiers are not canon.

---

## The Six Checks

Run all six. For each, output PASS or FLAG(s).

### 1. Term ownership
Build a term inventory: every named framework, coined term, and ™-marked
phrase in the target and in each sibling (from their Metadata blocks when
present, full-text scan otherwise). Flag:
- The same term defined/claimed by two dossiers (who owns it?)
- The same underlying concept under two different names across dossiers
  (vocabulary fork — the most dangerous flag, because downstream AIs blend
  forks silently)
- The target using a sibling-owned term without listing it under "terms owned
  elsewhere" in its Metadata

### 2. Topic overlap & redundancy across dossiers
Flag sections of the target that cover territory a sibling dossier owns as its
core topic. Some overlap is natural (topics touch); the flag threshold is a
section that could be lifted into the sibling without edits. Proposed fix is
always the same shape: ONE dossier owns the territory, the other carries a
one-line cross-reference to it.

### 3. Fact consistency
Compare the target's Canonical Facts (or, for old-format dossiers, its numbers
and credentials in prose) against every sibling's and the SOT. Flag any
number, credential, or claim that appears in two places with different values,
and any fact tagged [verified] in one dossier but stated differently
elsewhere. The proposed fix names which source should win (newest dated
document wins by default; the user confirms).

### 4. Staleness
Flag: predictions whose expiry year has passed; a review-by date in Metadata
that has lapsed; date-anchored claims ("this year", "in twelve months")
written long enough ago to have shifted meaning. For each, propose refresh,
re-date, or removal.

### 5. Internal redundancy
Within the target itself: flag any core claim restated in full more than
twice. Signature phrases repeating is voice; whole arguments repeating is
dilution. Propose which single location keeps the full statement and which
repeats collapse into references.

### 6. Structural compliance
Against the three-layer template: Metadata block present and complete
(version, dates, term ownership)? Layer markers present? Verbatim Quote Bank
present and actually verbatim (excerpts that read like polished prose are a
flag)? DERIVED layer fenced with the do-not-reuse note? Method at teaching
depth (each stage more than a one-liner)? Old-format dossiers get one summary
flag ("pre-template format") plus an offer to restructure rather than a
per-item list.

---

## Report format

```
# dossier-qa report: <target> · <date>

Checked against: <n> sibling dossiers, SOT [y/n]

| # | Check | Verdict |
|---|-------|---------|
| 1 | Term ownership        | PASS / n FLAGS |
| 2 | Topic overlap         | ... |
| 3 | Fact consistency      | ... |
| 4 | Staleness             | ... |
| 5 | Internal redundancy   | ... |
| 6 | Structural compliance | ... |

## Flags
FLAG 1 [check-n, severity high/med/low]
  Where: <section, both files if cross-dossier>
  Evidence: <the two conflicting passages, quoted>
  Proposed fix: <specific, minimal>
...
```

Severity: **high** = a downstream AI would produce wrong or contradictory
output (vocabulary forks, fact conflicts, lapsed predictions); **med** =
signal dilution (redundancy, overlap); **low** = housekeeping (metadata gaps,
format drift).

Keep the report tight. Zero flags is a legitimate outcome; do not manufacture
findings to look thorough. One high-signal flag beats ten trivia.

---

## After the report

- **Chained mode** (called by gravity-dossier): hand the report back; the
  calling skill walks the user through the flags and applies approved fixes to
  the draft before saving.
- **Standalone mode**: walk the user through flags one at a time, highest
  severity first. Apply a fix only on explicit approval, and only to dossier
  files — never to brain/learnings, decisions, SOT, or voice rules. If a fix
  implies changing a NON-dossier file (e.g. the SOT has the wrong number),
  stage it as a recommendation in the report instead and tell the user where
  it needs to go.
- If the audit surfaces a genuine learning (e.g. "vocabulary forks every time
  a dossier is built from BYO notes"), offer to log it to the insight inbox —
  never write it to the brain directly.
