---
name: start
description: Session opener. Loads CLAUDE.md, the brain/ folder, git status, your business plan from Perfect Little Business HQ and this week's content calendar at the beginning of every session. Run this first in every session.
---

# /start: Session Opener

## Purpose

Load full project context at the beginning of every session so Claude knows exactly where the user left off, who they are, what they believe, what they've discovered, what their plan says, and what's planned this week.

## When To Use

- Every single session, as the very first command
- After any context loss
- Returning to a project after time away

## Execution Instructions

Execute in this exact order:

### Step 1: Read Core Files

1. Read `CLAUDE.md` from the project root.
2. Read every `.md` file at the top level of `brain/`. Depending on which planning steps the user has run, that can include source-of-truth.md, business-today.md, avatar-profile.md, offer-architecture.md, convictions.md, what-makes-you-different.md, brand-style-guide.md, your-story.md, goals-and-vision.md, sales-path.md, marketing-plan.md, plus learnings.md, decisions.md and wins.md.
3. Note (but don't read every file in) voice-samples/, reference/, templates/, inspiration/, dossiers/. Just note what's there.

### Step 2: Load the Plan and This Week from HQ

If the Perfect Little Business connection's tools are available:
1. Call `get_plan` with no section. It lists every section of the user's business plan in Perfect Little Business HQ, with its card and whether it's filled.
2. Call `get_calendar` with `from` set to today and `to` set to six days from today (YYYY-MM-DD). It lists this week's planned and drafted content pieces.

Keep both in mind for the whole session: the plan is the current truth about the business, and it wins over an older local file where they disagree.

- **The tools aren't available:** skip this step and add one line to the briefing (below). Don't stop.
- **`get_plan` says their plan in HQ isn't switched on:** skip this step and leave the HQ lines out of the briefing.

### Step 3: Check Project State

1. Run `git status` to see uncommitted changes (skip quietly if this folder isn't a git repository).
2. Read the last 2 entries in MEMORY.md (most recent first).

### Step 4: Produce a Session Briefing

Output exactly this format. Fill in dynamically from what you read:

```
**Project:** [name from CLAUDE.md]
**Last session:** [date and brief summary from MEMORY.md]
**Open items from last session:** [from most recent MEMORY.md entry, if any]
**Your plan in HQ:** [N of M sections filled. Next to fill: section title (the step that fills it)]
**This quarter:** [the one priority and focus areas from the Goals and vision card]
**This week's content:** [one short line per piece: day, platform, kind, planned or drafted]
**Recent learnings to keep in mind:** [1-3 key items from learnings.md, if any]
**Recent decisions in play:** [1-2 from decisions.md, if any]
**Uncommitted changes:** [yes or no, and what they are if yes]

Ready to work. What are we focused on today?
```

Rules for the HQ lines:
- **Your plan in HQ:** "Next to fill" is the first empty section in the plan's order, skipping Website and Authority Directory (that one opens in HQ after a short call with the Perfect Little Business team). Name the step that fills it: business-today, avatar-profile, offer-architect, what-makes-you-different, conviction-map, brand-style-guide, your-story, goals-and-vision, sales-path or marketing-plan. When every section is filled, say so.
- **This quarter:** leave the line out when Goals and vision is empty. If the plan says Goals and Vision is due for a new quarter, say that instead: "A new quarter: time to set this quarter's goals (goals-and-vision)."
- **This week's content:** if the calendar is empty, say "Nothing planned this week" and, when Marketing plan is empty, add "(marketing-plan fills your calendar)".
- If the HQ tools weren't available, replace the three HQ lines with one: "**HQ:** not connected. Sign in to your Perfect Little Business connection to bring your plan into every session."
- If a section in HQ was updated after `brain/source-of-truth.md` was last changed, add: "Your plan in HQ has changed since your Source of Truth was last pulled down. Run source-of-truth to refresh it."

### Step 5: Wait

Do not proceed to any work until the user responds.

---

## Notes for Claude Executing This Skill

- If any file is missing, flag it but don't fail. Note: "brain/learnings.md not found. You may want to create it."
- If MEMORY.md only has the setup entry, that's expected for a new project. Briefing should say: "First working session in this project."
- Briefing should be scannable: the user is starting their session, not reading a report.
- If learnings.md or decisions.md are empty, omit those briefing lines rather than printing "(empty)".
- Call it "your plan in Perfect Little Business HQ" or "HQ" and "your Perfect Little Business connection". Never use technical names for the connection.
