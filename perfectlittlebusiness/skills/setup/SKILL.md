---
name: setup
description: One-time orchestrator that installs your AI Operating System in this project. Creates CLAUDE.md, MEMORY.md, and your AIOS Brain (the brain/ folder), then confirms everything is in place. Run this once per new project.
---

# /setup — AIOS Brain & Operating System Installer

## Purpose

Install the complete AI Operating System in the current project folder, including your AIOS Brain. This is a one-time command per project. Creates all files, populates them with the user's context, and runs verification.

## When To Use

- First time setting up Claude in a new project folder
- After installing the perfectlittlebusiness plugin
- When starting a new business, offer, or directory build

Do not run this in a project that already has CLAUDE.md unless the user wants to start fresh.

## Execution Instructions

### Phase 1: Verify Environment

1. Check if CLAUDE.md already exists at project root.
2. If it does, ask: "I see this project already has CLAUDE.md. Should I (a) abort to protect your existing setup, (b) back up the current files and create fresh, or (c) skip file creation and just install brain folder?"
3. Wait for user choice before proceeding.
4. If no existing setup, continue.

### Phase 2: Gather Context (Five Questions)

Ask one at a time. Wait for each answer before continuing.

**Q1:** "What's your project name? (e.g., coaching-directory, saas-platform, creative-studio)"

**Q2:** "What's your role? (e.g., founder, consultant, coach, creator, subject matter expert)"

**Q3:** "In one paragraph, what does your AIOS Brain need to know about your business? What do you do, who do you serve, what's the core problem you solve?"

**Q4:** "Give me three words that describe your brand voice. (e.g., calm/warm/intelligent or direct/playful/bold)"

**Q5:** "What's one core conviction that drives your work? Something you believe to be true that shapes how you operate."

Store all five answers. You'll use them in the next phase.

### Phase 3: Create Root Files

Create these files at the project root:

1. **CLAUDE.md** — populate using the template in this skill's reference section below. Fill in user's answers.

2. **MEMORY.md** — initialize with today's setup entry.

3. **.gitignore** — use standard content (see reference below).

4. **README.md** — brief project overview.

### Phase 4: Create the AIOS Brain

Create `brain/` with these files (templates in the reference section below):

- `source-of-truth.md` — populated with Q3 answer expanded
- `convictions.md` — populated with Q5 answer as Conviction 1
- `avatar-profile.md` — stub; populated when the user runs `/avatar-profile`
- `offer-architecture.md` — stub; populated when the user runs `/offer-architect`
- `brand-style-guide.md` — stub; populated when the user runs `/brand-style-guide`
- `learnings.md` — empty, ready to grow
- `decisions.md` — empty, ready to grow
- `wins.md` — empty, ready to grow
- `voice-samples/README.md` — instructions for adding voice samples
- `reference/README.md` — instructions for reference docs
- `templates/README.md` — instructions for reusable formats

The five foundational-tool files (`source-of-truth`, `convictions`, `avatar-profile`, `offer-architecture`, `brand-style-guide`) are your AIOS Brain. `/setup` stubs them; the five AIOS Brain tools fill them in.

### Phase 5: Verification

Confirm each file exists:

- [ ] CLAUDE.md
- [ ] MEMORY.md
- [ ] .gitignore
- [ ] README.md
- [ ] brain/source-of-truth.md
- [ ] brain/convictions.md
- [ ] brain/avatar-profile.md
- [ ] brain/offer-architecture.md
- [ ] brain/brand-style-guide.md
- [ ] brain/learnings.md
- [ ] brain/decisions.md
- [ ] brain/wins.md
- [ ] brain/voice-samples/README.md
- [ ] brain/reference/README.md
- [ ] brain/templates/README.md

### Phase 6: Completion Message

Output exactly this message:

```
✅ Your AI Operating System is installed.

**What's now running in this project:**
- Core files: CLAUDE.md, MEMORY.md, .gitignore, README.md
- Your AIOS Brain: the brain/ folder, eleven files ready to grow with you
- Operating skills: /start, /end, /hygiene, /learn, /decide, /recap, /digest, /ask, /granola-pull, /draft-social, /how-to
- Your five AIOS Brain tools: /avatar-profile, /offer-architect, /conviction-map, /brand-style-guide, /source-of-truth
- Plus /voice-qa (brand-voice gate), /gravity-dossier, and /dossier-qa (dossier consistency gate)
- Three protective hooks: credential guard, forbidden-language guard, session-end nudge

**Your test-drive automations are live immediately:**
- `/digest` — your personal weekly summary
- `/granola-pull` — pull meetings into your brain
- `/draft-social` — draft posts in your voice

**Next move:** Type `/start` to confirm the system loads. Then build your AIOS Brain by running your five foundational tools, beginning with `/avatar-profile`.

The operating system is installed. Your AIOS Brain is what you build inside it.
```

---

## CLAUDE.md Template

Use this template. Replace [BRACKETED] with user answers. Replace [TODAY'S_DATE] with current date.

```markdown
# CLAUDE.md — [PROJECT_NAME]

**Project:** [PROJECT_NAME]
**Role:** [USER_ROLE]
**Installed:** [TODAY'S_DATE]
**AI Operating System version:** perfectlittlebusiness v1.4.0

---

## What This Project Is

[USER_ANSWER_3 — expanded into 2-3 sentences if needed]

---

## Brand Voice

Three-word essence: [USER_ANSWER_4]

[Expand into a brief paragraph describing the tone, energy, and language style this implies. Keep under 100 words.]

---

## Core Conviction

[USER_ANSWER_5]

This shapes every decision in this project. Reference it when making strategic choices, writing content, or evaluating options. Additional convictions live in brain/convictions.md as they emerge.

---

## How To Work In This Project

### At Session Start
- Run `/start` to load full context
- Claude reads this file and your brain/ folder

### During The Session
- One project per session — do not switch contexts
- Use `/learn` to capture insights mid-session
- Use `/decide` after meaningful decisions
- Use `/ask` for questions grounded in your context

### At Session End
- Run `/end` to log the session and capture learnings
- Commit changes before closing

### Weekly
- Run `/hygiene` once per week (Sundays recommended)
- Run `/digest` for your weekly summary

---

## Folder Structure

```
[project-root]/
├── CLAUDE.md          ← This file (master briefing)
├── MEMORY.md          ← Session log
├── README.md          ← Project overview
├── .gitignore         ← Exclusion list
└── brain/             ← Your AIOS Brain
    ├── source-of-truth.md    (what you know)
    ├── convictions.md        (what you believe)
    ├── avatar-profile.md     (who you serve)
    ├── offer-architecture.md (what you sell)
    ├── brand-style-guide.md  (how you sound and look)
    ├── learnings.md          (what you've discovered)
    ├── decisions.md          (decisions made, with rationale)
    ├── wins.md               (what's working)
    ├── voice-samples/        (writing examples for tone matching)
    ├── reference/            (PDFs, articles, source docs)
    └── templates/            (reusable formats)
```

The AIOS Brain is yours. Edit any file any time.

---

## Guardrails

- One project per session
- Never commit API keys, passwords, or credentials (the credential hook protects this)
- Approve before deploying
- Commit before closing
- Run `/end` at session close

---

## The Self-Improvement Loop

This system gets smarter every session through two files:

- **MEMORY.md** = project timeline (what happened)
- **brain/learnings.md** = business intelligence (what you discovered)

Every `/start` reads both. Every `/end` updates both. Over time, Claude builds an accurate model of this business — not from training data, but from your actual lived experience.

When advising you, Claude prioritizes your learnings.md over generic best practices. Your learnings reflect what's actually working for *this* business.

---

## Where the Methodology Lives

This plugin installs the *infrastructure layer* — your AIOS Brain and the operating skills. The Perfect Little Business methodology and full doctrine live in **Collective Wisdom** (perfectlittlebusiness.com), kept current there as the methodology evolves.

This file is yours. Your `brain/` folder is yours. Both stay clean by living separately from the methodology.
```

---

## MEMORY.md Template

```markdown
# Project Memory Log

This file is the timeline of every session. Updated automatically by `/end`.

---

## [TODAY'S_DATE] — AI Operating System Installed

**What happened:**
Initialized the AI Operating System using perfectlittlebusiness v1.4.0. Created CLAUDE.md, MEMORY.md, .gitignore, README.md, and the full AIOS Brain (brain/ folder). Your operating skills, your five AIOS Brain tools, and three protective hooks are now available.

**Git state:** Not yet committed
**Deploy state:** Not configured (optional, for later)

**Open items / next session:**
- Build your AIOS Brain: run `/avatar-profile`, `/offer-architect`, `/conviction-map`, `/brand-style-guide`, then `/source-of-truth`
- Drop 2-3 voice samples in brain/voice-samples/
- Run `/start` to confirm the system loads
- Try `/digest`, `/draft-social`, or `/granola-pull` to test-drive the automations

**To verify the system is working:** Type `/start` in your next session. Claude should read everything and ask what you want to work on.
```

---

## .gitignore Template

```
# System noise
.DS_Store
Thumbs.db

# Generated output
dist/
build/

# Dependencies
node_modules/

# Netlify artifacts
.netlify/

# Sensitive files (the credential hook protects these too)
.env
.env.local
*.env
*.key
*.pem

# Logs and archives
*.log
*.zip

# Large data folders (uncomment if needed)
# transcripts/
# raw-recordings/
```

---

## README.md Template

```markdown
# [PROJECT_NAME]

[One-line description from USER_ANSWER_3]

## Quick Start

1. Type `/start` to load context
2. Tell Claude what you want to work on
3. Approve changes before executing
4. Type `/end` to close cleanly and update memory

## Key Files

- **CLAUDE.md** — master project briefing
- **MEMORY.md** — session log
- **brain/** — your AIOS Brain

## Created

[TODAY'S_DATE] using perfectlittlebusiness v1.4.0
```

---

## Brain File Templates

### brain/source-of-truth.md

```markdown
# Source of Truth

The master document about this business. Update as your understanding evolves.

## Who This Is

[USER_ANSWER_2 — their role]

## What You Do

[USER_ANSWER_3 — expanded]

## Who You Serve

[Extract from Q3 if mentioned, otherwise: "To populate: describe your ideal client or audience."]

## Core Problem You Solve

[Extract from Q3 if mentioned, otherwise: "To populate: what problem do you solve uniquely?"]

## Your Solution / Approach

[To populate: how do you solve it? What's your method?]

## Key Frameworks or Methodologies

[To populate: list any frameworks, systems, or IP you've developed.]

---

**Note:** This file is your north star. Claude reads it every session. Keep it current. Run `/source-of-truth` to build it out properly.
```

### brain/convictions.md

```markdown
# Core Convictions

What you believe to be true. What drives your decisions.

## Conviction 1 (Foundational)

[USER_ANSWER_5]

**Why it matters:** [Brief expansion — why this belief shapes your work]

## Conviction 2

[To populate]

## Conviction 3

[To populate]

## What You Stand Against

[To populate: what conventional wisdom, language, or approaches do you reject?]

---

**Note:** Convictions evolve. Run `/conviction-map` to build this out properly.
```

### brain/avatar-profile.md

```markdown
# Avatar / Audience Profile

Who you serve. Not demographics — emotional and behavioral profile.

## Who They Are

[To populate]

## Their Core Problem

[To populate]

## What They're Searching For

[To populate]

## What Attracts Them

[To populate]

## What Repels Them

[To populate]

## How They Make Decisions

[To populate]

---

**Note:** Run `/avatar-profile` to build this out properly. It gets more specific over time as you learn from real conversations.
```

### brain/offer-architecture.md

```markdown
# Offer Architecture

What you sell and how it's structured.

## Your Core Offer

[To populate]

## Offer Stack

[To populate]

## Who It's For / What It Solves

[To populate]

---

**Note:** Run `/offer-architect` to build this out properly.
```

### brain/brand-style-guide.md

```markdown
# Brand Style Guide

How you sound and look.

## Voice & Tone

[To populate]

## Words You Use / Words You Never Use

[To populate]

## Visual Identity

[To populate]

---

**Note:** Run `/brand-style-guide` to build this out properly. Claude checks this before drafting anything in your name.
```

### brain/learnings.md

```markdown
# Business Learnings & Discoveries

The self-improving layer of your operating system.

**Purpose:** Capture what you discover about your business. Patterns, insights, market signals, what's working, what's not. Claude reads this every session.

**How it grows:** `/learn` captures mid-session. `/end` prompts at session close.

---

## What's Working

[Empty for now — fills in as you work]

## What's Not Working

[Empty]

## Market Signals

[Empty]

## Positioning Refinements

[Empty]

## Strategic Pivots

[Empty]

## Open Questions

[Empty]

---

**Last updated:** [TODAY'S_DATE] — initialized
```

### brain/decisions.md

```markdown
# Decision Log

Meaningful decisions made in this project, with full context and rationale.

Populated by `/decide` after each significant call.

---

(No decisions logged yet.)
```

### brain/wins.md

```markdown
# Wins

What's worked. What's landing. What's converting.

Populated by `/end` at session close, or manually whenever something works.

---

(No wins logged yet.)
```

### brain/voice-samples/README.md

```markdown
# Voice Samples

Drop 3-5 pieces of your writing in this folder. Claude reads them to match your voice when drafting.

Good samples include:
- A newsletter or blog post you're proud of
- A social post that landed well
- A client email that captured your tone
- A piece of sales copy that worked

Don't overthink it. Variety helps. Update as your voice evolves.

Suggested filenames:
- example-newsletter.md
- example-social-post.md
- example-client-email.md
- example-sales-copy.md
```

### brain/reference/README.md

```markdown
# Reference Materials

Drop reference docs here — PDFs, articles, transcripts, past work.

Examples:
- Past client work samples
- Articles that shaped your thinking
- Transcripts of key conversations
- Meeting notes (or use `/granola-pull` to auto-import)
- Frameworks you've developed

Organize as you like. Subfolders are fine.
```

### brain/templates/README.md

```markdown
# Templates

Reusable formats you discover you need over and over.

Examples:
- newsletter-format.md
- proposal-format.md
- email-response-templates.md
- launch-sequence-format.md

Empty for now. Add templates as patterns emerge.
```

---

## Notes for Claude Executing This Skill

- Do not skip questions. All five are required.
- Do not auto-generate content for files not explicitly templated above.
- If the user gives a very short answer to Q3, ask one clarifying question before proceeding. Then move on.
- If the user is uncomfortable answering Q5, accept a placeholder ("to be discovered") and note it in convictions.md.
- After completion, do NOT proceed to other work in the same response. The user needs to type `/start` to verify the install before doing anything else.
