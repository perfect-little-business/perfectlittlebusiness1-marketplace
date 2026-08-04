# CLAUDE.md — marketplace-root

The "Perfect Little Business" Claude plugin + marketplace repo. The full
project briefing lives in `business-os/ROOT-ORCHESTRATION.md` §05, which is
auto-loaded in any root session as `~/Business/CLAUDE.md`. That includes the
Cowork build geography. This file exists to carry the canonical brain pointer
for dev sessions.

*Pointer corrected 2026-08-03: this previously named
`_00_CLAUDE_CODE/CLAUDE.md`, the pre-migration Dropbox path, tombstoned since
2026-07-29.*

---

## Publishing to clients (read this before shipping anything)

**Clients do not install from this repo.** They install from
`perfect-little-business/perfectlittlebusiness1-marketplace`. This repo is
where the work happens; that one is the shop window.

The "1" is not a mistake or a stray duplicate. Claude Cowork caches the
marketplace list, so pushing an update here left clients on a stale copy. A
second marketplace under a distinct name forces Cowork to pull fresh. That is
why `.claude-plugin/marketplace.json` reads `"name": "plb"` here and
`"name": "plb1"` there. **That single field is the only thing that may ever
differ between the two repos.** Never sync it.

**How to publish: bump the version.** That is the whole procedure.

Edit the version in `perfectlittlebusiness/.claude-plugin/plugin.json` (and
the matching one in `.claude-plugin/marketplace.json`), push to `main`, and
`.github/workflows/publish-to-clients.yml` copies this repo into the client
repo within about a minute. Pushing without changing the version publishes
nothing, which is deliberate: it means day-to-day commits never leak
half-finished work to clients.

`.github/` is excluded from the sync in both directions, so each repo keeps
its own automation.

**Why this exists:** the two repos silently drifted a full release apart. The
client-facing copy sat on v1.3.0 with 20 skills for six weeks while the work
here reached v1.4.0 with 21, and a voice-qa bug that had been fixed here was
still shipping to clients. Verified and corrected 2026-08-02.

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
