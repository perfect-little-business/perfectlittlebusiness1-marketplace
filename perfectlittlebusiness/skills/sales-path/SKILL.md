---
name: sales-path
description: >-
  Run the Your Sales Path planning step: how a stranger becomes a paying client (where they first meet you, the free offer, the follow-up, the conversation, the yes), then the monthly numbers it needs to reach the goal. Saves to the Sales path section of the user's plan in Perfect Little Business HQ and to brain/sales-path.md. Use when the user says "sales path", "my sales process", "how clients buy from me", "my funnel", or "map my sales path".
---

# Your Sales Path

Runs the **Your Sales Path** step from Perfect Little Business HQ, then saves the result in two places: the **Sales path** section of the user's business plan in HQ, and `brain/sales-path.md` in this project. The step's instructions live in HQ and are fetched fresh every time. Never copy them into this file.

## How it runs

### 1. Fetch the step
Call `get_stage_prompt` from the Perfect Little Business connection with `stage_key: "sales_path"`.
- **The tool isn't available:** the user hasn't signed in to their Perfect Little Business connection yet. Tell them how, for where they're working, then stop:
  - Claude desktop app or claude.ai: Customize, then Connectors, then Perfect Little Business, then Connect.
  - Claude Code: type `/mcp`, choose `plugin:perfectlittlebusiness:perfectlittlebusiness`, then Authenticate.
  - Codex: in a terminal, run `codex mcp login perfectlittlebusiness`.
  Signing in opens HQ's sign-in page in their browser. They use the email of their HQ account.
- **It says the workspace isn't an active client yet:** relay that warmly and stop.

### 2. Gather what the step already knows
The step's instructions say to read the client brain before the first reply. Inside HQ that is loaded for it; here it isn't, so gather it before you say anything:
- Call `get_plan` with no section to see which sections of their plan are filled.
- For each of these that is filled, call `get_plan` with its key and read the full document: `business_at_a_glance`, `ideal_client`, `your_offers`, `what_makes_you_different`, `goals_and_vision`, `sales_path`.
- Read these files if they exist: `brain/business-today.md`, `brain/avatar-profile.md`, `brain/offer-architecture.md`, `brain/goals-and-vision.md`, `brain/sales-path.md`, and `CLAUDE.md`.
- Treat all of it as the client brain (and the sign-up facts in Business at a glance as the operator profile). Never ask for anything it already holds.
- If `get_plan` says the plan isn't switched on, carry on with the local files alone.

### 3. Run the step
Operate exactly as the returned system prompt instructs. Open with its opening message, word for word. One question at a time. Don't add, skip, reorder or summarize away anything it specifies. Where it mentions output markers or a completion protocol, the deliverable is simply the finished final document, in the shape it gives.

### 4. Save, once it's finished
The step has the user confirm (or lock) its parts before it produces the final document, so a finished final document is an agreed one. If they ask for changes afterwards, make them first.

1. **Local copy.** Write the final document to `brain/sales-path.md` (create `brain/` if needed), replacing what was there.
2. **HQ.** Call `save_plan_section` with `section: "sales_path"`, `document`: the whole final document, `summary`: the card (rules below), and `made_by: "sales-path"`. Card brief: *How a new person becomes a client, as a short line of steps in order: where they first meet the business, the free offer if there is one, the conversation, and how they buy. Then the monthly numbers it needs (new clients and conversations), if the document gives them.*
3. **Tell the user**, in one or two plain lines: it's on their business plan in Perfect Little Business HQ (Sales path), and in `brain/sales-path.md`. Then give the step's own closing line.

If the save to HQ fails or their plan isn't switched on, say the work is safe in `brain/sales-path.md` and that it can go to HQ once their plan is on. Don't retry in a loop.

### Card rules
- Use only what the document says. Never invent, never add advice, never fill a gap with a guess.
- Write to the owner: "you" and "your". Never name the owner. Their customers are "your clients" (or the word the document uses); where the document speaks to those customers as "you", rewrite it from the owner's side.
- Plain words. 90 words at most: one or two short sentences, or up to four short bullets, or a sentence followed by bullets.
- No heading, no title, no preamble, no closing line.
- No em dashes or en dashes.

## How to talk about it
Call it "your plan in Perfect Little Business HQ" or "HQ", and "your Perfect Little Business connection". Never use technical names for the connection.

## Scope
Run only this step. The next step is `marketing-plan`. The planning steps, in order: business-today, avatar-profile, offer-architect, conviction-map, what-makes-you-different, brand-style-guide, your-story, goals-and-vision, sales-path, marketing-plan. For anything else, point the user to the right one and come back.
