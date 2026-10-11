---
name: business-today
description: Run the Your Business Today step, the first planning step, a ten-minute check-in on where the business stands right now (how it makes money, the numbers today, where clients come from, where it's going). Saves to the Business at a glance section of the user's plan in Perfect Little Business HQ and to brain/business-today.md. Use when the user says "business today", "your business today", "where my business stands", "start my plan", "first planning step", or wants to record their starting numbers.
---

# Your Business Today

Runs the **Your Business Today** step from Perfect Little Business HQ, then saves the result in two places: the **Business at a glance** section of the user's business plan in HQ, and `brain/business-today.md` in this project. The step's instructions live in HQ and are fetched fresh every time. Never copy them into this file.

## How it runs

### 1. Fetch the step
Call `get_stage_prompt` from the Perfect Little Business connection with `stage_key: "business_today"`.
- **The tool isn't available:** the user hasn't signed in to their Perfect Little Business connection yet. Tell them how, for where they're working, then stop:
  - Claude desktop app or claude.ai: Customize, then Connectors, then Perfect Little Business, then Connect.
  - Claude Code: type `/mcp`, choose `plugin:perfectlittlebusiness:perfectlittlebusiness`, then Authenticate.
  - Codex: in a terminal, run `codex mcp login perfectlittlebusiness`.
  Signing in opens HQ's sign-in page in their browser. They use the email of their HQ account.
- **It says the workspace isn't an active client yet:** relay that warmly and stop.

### 2. Gather what the step already knows
The step's instructions say to read the "operator profile" before the first reply. Inside HQ that is loaded for it; here it isn't, so gather it before you say anything:
- Call `get_plan` with `section: "business_at_a_glance"`. Its document holds the sign-up answers: name, business name, type of business, area of expertise, website, address, phone.
- Read `brain/business-today.md` if it exists (an earlier run) and `CLAUDE.md` for the business description.
- Treat all of it as the operator profile. Never ask for anything it already holds.
- If `get_plan` says the plan isn't switched on, carry on with the local files alone.

### 3. Run the step
Operate exactly as the returned system prompt instructs. Open with its opening message, word for word. One question at a time. Don't add, skip, reorder or summarize away anything it specifies. Where it mentions output markers, the deliverable is simply the finished document, in the shape it gives.

### 4. Save, once it's finished
The step asks the user to confirm the snapshot before it produces the deliverable, so a finished deliverable is an agreed one. If they ask for changes afterwards, make them first.

1. **Local copy.** Write the deliverable to `brain/business-today.md` (create `brain/` if needed), replacing what was there.
2. **HQ.** Business at a glance is shared with the sign-up answers, so keep them:
   - **document:** the sign-up facts from the current Business at a glance document, then a blank line, then the new deliverable. If that document already holds an earlier "Your Business Today", replace that part rather than adding a second one.
   - **summary:** the card, written to the rules below. Brief: *what the business is and who it serves, in one or two sentences, then up to three short facts (how it makes money, where it stands today, where it is going). Use the current card for what the business does and who it serves, and the new snapshot for where it stands today; where they disagree, the owner's own answers win.*
   - Call `save_plan_section` with `section: "business_at_a_glance"`, the summary, the document, and `made_by: "business-today"`.
3. **Tell the user**, in one or two plain lines: it's on their business plan in Perfect Little Business HQ (Business at a glance), and in `brain/business-today.md`. Then give the step's own closing line.

If the save to HQ fails or their plan isn't switched on, say the work is safe in `brain/business-today.md` and that it can go to HQ once their plan is on. Don't retry in a loop.

### Card rules
- Use only what the document says. Never invent, never add advice, never fill a gap with a guess.
- Write to the owner: "you" and "your". Never name the owner. Their customers are "your clients" (or the word the document uses).
- Plain words. 70 words at most: one or two short sentences, or up to four short bullets, or a sentence followed by bullets.
- No heading, no title, no preamble, no closing line.
- No em dashes or en dashes.

## How to talk about it
Call it "your plan in Perfect Little Business HQ" or "HQ", and "your Perfect Little Business connection". Never use technical names for the connection.

## Scope
Run only this step. The next step is `avatar-profile`. For anything else, point the user to the right planning step and come back.
