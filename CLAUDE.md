# CLAUDE.md — marketplace-root

The "Perfect Little Business" Claude plugin + marketplace repo. Full
project briefing lives in root `_00_CLAUDE_CODE/CLAUDE.md` §05
(`marketplace-root`) — including the Cowork build geography. This file
exists to carry the canonical brain pointer for dev sessions.

---

## ⚓ PLB CANONICAL BRAIN (2026-06-10)

The canonical source for ALL Perfect Little Business strategy, brand, and
offer files is, permanently:

`/Users/cindymolchany/Business/business-os/brain/`

- Read `business-os/brain/_INDEX.md` first — it holds the file map and the
  inheritance order (Offer Stack → SOT v7.0 → everything else).
- Read brain files directly from that path. Never copy brain files into
  this project.
- Any local PLB SOT, brand, or offer docs in this repo are SUPERSEDED by
  the brain. Archive them; don't delete them.
- **Dev sessions only.** This plugin is client-installed: never bake
  brain content, brain file copies, or this path into the shipped plugin
  (`perfectlittlebusiness/`). Client projects never reference or inherit
  the PLB brain.

---

## Status surface (PLB Business OS)

At the end of every session (and whenever /end runs), update the AREA file:
`~/Business/business-os/status/delivery.json`
following the schema in `business-os/status/_schema.md`.

The convention changed with the business-os migration: it is now one JSON file
per business **area**, not one per project, so the client-installed plugin
reports into `delivery.json` alongside the rest of delivery rather than owning
its own file. The old
`Dropbox/_00_COWORK_OS/status/marketplace-root.status.json` and
`_00_COWORK_OS/STATUS_CONVENTION.md` are superseded and the paths are dead.
Do not write there.

Rules:
- Progress surface ONLY: state, phase, now, next, blockers, open items.
  Never code, secrets, or client deliverable content.
- Keep `now` and `next` to one line each. Blockers are the most valuable
  field — never omit a real one.
- This file is how the business OS sees this project. If it's stale, the
  project looks stale.
