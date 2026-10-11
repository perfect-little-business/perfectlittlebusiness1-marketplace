---
name: setup
description: One-time orchestrator that installs your AI Operating System in this project. Creates CLAUDE.md, MEMORY.md, and your AIOS Brain (the brain/ folder), then confirms everything is in place. If you already have a business plan in Perfect Little Business HQ, it brings that plan into the brain/ folder. Run this once per new project.
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

### Phase 1b: Check for a Plan in Perfect Little Business HQ

If the Perfect Little Business connection's tools are available, call `get_plan` with no section.
- **It returns their plan:** this user already has a Perfect Little Business HQ account. Note which sections are filled. Tell them in one line: "You already have a business plan in Perfect Little Business HQ, so I'll bring it into this project instead of starting from scratch."
- **It says the plan isn't switched on, or the workspace isn't an active client yet, or the tools aren't available:** carry on as a new setup. Don't stop to fix the connection here; the completion message says how to sign in.

### Phase 2: Gather Context (Five Questions)

Ask one at a time. Wait for each answer before continuing.

If Phase 1b found a plan, don't ask Q3, Q4 or Q5 cold. Draft each answer from the plan and ask the user to confirm or correct it, one at a time: Q3 from Business at a glance (plus Ideal client and Problem and promise, if filled), Q4 from Brand, Q5 from Values and convictions. Ask Q1 and Q2 as written. Ask any question the plan doesn't cover as written.

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
- `inspiration/README.md` — instructions for the things you hold on to (stories, quotes, ideas) via `/hold`

The planning files are your AIOS Brain. `/setup` stubs five of them; the planning steps fill them in, and add their own files as they run (business-today.md, what-makes-you-different.md, your-story.md, goals-and-vision.md, sales-path.md, marketing-plan.md).

**If Phase 1b found a plan, pull it down now.** For each filled section, call `get_plan` with its key and write its full document to the matching file, replacing the stub:

| Plan section | File |
|---|---|
| business_at_a_glance | `brain/business-today.md` |
| ideal_client | `brain/avatar-profile.md` |
| problem_and_promise, your_offers | `brain/offer-architecture.md` (if both hold the same document, write it once; if not, write each under its own heading) |
| what_makes_you_different | `brain/what-makes-you-different.md` |
| values_and_convictions | `brain/convictions.md` (in place of the Q5 template) |
| brand | `brain/brand-style-guide.md` |
| your_story | `brain/your-story.md` |
| website_and_directory | `brain/website-and-directory.md` |
| goals_and_vision | `brain/goals-and-vision.md` |
| sales_path | `brain/sales-path.md` |
| marketing_plan | `brain/marketing-plan.md` |

Then write `brain/source-of-truth.md` the way the `source-of-truth` skill does: the whole plan in one document, in place of the stub. Empty sections keep their stub, or get no file. Write each document as it stands; don't rewrite or summarize it.

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
- [ ] brain/inspiration/README.md
- [ ] If Phase 1b found a plan: one file per filled section, from the table in Phase 4

### Phase 6: Completion Message

Output exactly this message:

```
✅ Your AI Operating System is installed.

**What's now running in this project:**
- Core files: CLAUDE.md, MEMORY.md, .gitignore, README.md
- Your AIOS Brain: the brain/ folder, ready to grow with you [if Phase 1b found a plan, add: ", with your business plan from Perfect Little Business HQ already in it"]
- Operating skills: /start, /end, /hygiene, /learn, /decide, /hold, /recap, /digest, /ask, /granola-pull, /draft-social, /how-to
- Your planning steps, the same ones as in Perfect Little Business HQ. Each saves to your plan in HQ and to brain/: /business-today, /avatar-profile, /offer-architect, /conviction-map, /what-makes-you-different, /brand-style-guide, /your-story, /goals-and-vision, /sales-path, /marketing-plan
- /source-of-truth: your whole plan from HQ in one document
- Plus /voice-qa (brand-voice gate), /gravity-dossier, and /dossier-qa (dossier consistency gate)
- Three protective hooks: credential guard, forbidden-language guard, session-end nudge

**Your test-drive automations are live immediately:**
- `/digest` — your personal weekly summary
- `/granola-pull` — pull meetings into your brain
- `/draft-social` — draft posts in your voice

**Next move:** Type `/start` to confirm the system loads. Then [if Phase 1b found a plan: "pick up your plan where it stands; /start names the next step." Otherwise: "start your plan with `/business-today`."]

The operating system is installed. Your AIOS Brain is what you build inside it.
```

If the Perfect Little Business connection's tools weren't available in Phase 1b, add one line after the message: "To connect this project to your plan in Perfect Little Business HQ, sign in to your Perfect Little Business connection (in Claude: Customize, then Connectors; in Claude Code: type /mcp; in Codex: run `codex mcp login perfectlittlebusiness` in a terminal), then run /source-of-truth."

---

## CLAUDE.md Template

Use this template. Replace [BRACKETED] with user answers. Replace [TODAY'S_DATE] with current date.

```markdown
# CLAUDE.md — [PROJECT_NAME]

**Project:** [PROJECT_NAME]
**Role:** [USER_ROLE]
**Installed:** [TODAY'S_DATE]
**AI Operating System version:** perfectlittlebusiness v1.5.0

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
- Use `/hold` to hold on to a story, quote or idea you want to use later
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
    ├── source-of-truth.md    (your whole plan, pulled from HQ)
    ├── business-today.md     (where the business stands)
    ├── avatar-profile.md     (who you serve)
    ├── offer-architecture.md (what you sell)
    ├── convictions.md        (what you believe)
    ├── what-makes-you-different.md
    ├── brand-style-guide.md  (how you sound and look)
    ├── your-story.md         (where it began, why it exists)
    ├── goals-and-vision.md   (where it's going, this quarter)
    ├── sales-path.md         (how a stranger becomes a client)
    ├── marketing-plan.md     (where marketing energy goes)
    ├── learnings.md          (what you've discovered)
    ├── decisions.md          (decisions made, with rationale)
    ├── wins.md               (what's working)
    ├── voice-samples/        (writing examples for tone matching)
    ├── reference/            (PDFs, articles, source docs)
    ├── templates/            (reusable formats)
    └── inspiration/          (stories, quotes, ideas you are holding on to)
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

This plugin installs the *infrastructure layer*: your AIOS Brain and the operating skills. The planning steps themselves live in **Perfect Little Business HQ** (hq.perfectlittlebusiness.com) and are kept current there; each one runs here or in HQ and saves to your plan in HQ.

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
Initialized the AI Operating System using perfectlittlebusiness v1.5.0. Created CLAUDE.md, MEMORY.md, .gitignore, README.md, and the full AIOS Brain (brain/ folder). Your operating skills, your planning steps, and three protective hooks are now available.

**Git state:** Not yet committed
**Deploy state:** Not configured (optional, for later)

**Open items / next session:**
- Build your plan, in order: `/business-today`, `/avatar-profile`, `/offer-architect`, `/conviction-map`, `/what-makes-you-different`, `/brand-style-guide`, `/your-story`, `/goals-and-vision`, `/sales-path`, `/marketing-plan`. Each one saves to your plan in Perfect Little Business HQ and to brain/.
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

[TODAY'S_DATE] using perfectlittlebusiness v1.5.0
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

**Note:** This file is your north star. Claude reads it every session. Run `/source-of-truth` to replace it with your whole business plan from Perfect Little Business HQ, and again whenever your plan changes.
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

### brain/inspiration/README.md

```markdown
# Inspiration

The things you hold on to. A story a podcast guest told, a line you want to keep,
an idea for an episode or a post, something you noticed that connects to your work.
You do not decide up front what it is for. You say "hold on to this" and it lands here.

How it works:

- `/hold` captures one. It keeps the thing in your words, plus one sentence from you
  about what you would connect it to. That sentence is what makes it findable later.
- `_INDEX.md` is one line per entry, generated. Never edit it by hand.
- `/hold find {topic}` brings back the entries that fit when you are drafting.
- `/hold used {entry} in {where}` stamps one when it ships, so you never repeat it.

Empty at install. It fills from the first "hold on to this."
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
