---
name: source-of-truth
description: Build your Source of Truth, the one document that holds your whole business plan, ready to hand to any AI. Pulls every filled section of your plan from Perfect Little Business HQ into brain/source-of-truth.md and names what's still empty and which step fills it. Use when the user wants to compile, refresh, or build their Source of Truth / business SOT / master brand doc, or says "source of truth", "my master doc", "pull down my plan", "refresh my source of truth", "download my plan".
---

# Source of Truth

Your Source of Truth is your whole business plan in one document: the thing you hand to Claude, ChatGPT or a new team member so they know your business. In Perfect Little Business HQ the plan fills in section by section as you finish your planning steps. This skill pulls it down into `brain/source-of-truth.md`, so every session in this project works from the current plan.

It doesn't run an interview of its own. The story part of the old Source of Truth is now the **Your Story** step (`your-story`).

## How it runs

### 1. Read the plan
Call `get_plan` from the Perfect Little Business connection, with no section.
- **The tool isn't available:** the user hasn't signed in to their Perfect Little Business connection yet. Tell them how, for where they're working, then stop:
  - Claude desktop app or claude.ai: Customize, then Connectors, then Perfect Little Business, then Connect.
  - Claude Code: type `/mcp`, choose `plugin:perfectlittlebusiness:perfectlittlebusiness`, then Authenticate.
  - Codex: in a terminal, run `codex mcp login perfectlittlebusiness`.
  Signing in opens HQ's sign-in page in their browser. They use the email of their HQ account.
- **It says the workspace isn't an active client yet:** relay that warmly and stop.
- **It says their plan in HQ isn't switched on:** use the fallback at the end of this file.

### 2. Pull each filled section
For every section the overview shows as filled, call `get_plan` with its key and take the full document.

### 3. Write the Source of Truth
Write `brain/source-of-truth.md` (create `brain/` if needed), replacing what was there, in this shape:

```
# {Business name}: Source of Truth

Your business plan from Perfect Little Business HQ, pulled down {today's date}. Run `source-of-truth` again whenever your plan changes.

## 1. Business at a glance
{the card, then the full document}

## 2. Ideal client
{the full document}

... every filled section, in the plan's order, with its number and title ...

---

Not filled in yet: {titles of the empty sections}.
```

- Use each section's full document as it stands. Don't rewrite, summarize or tidy it.
- Nest each document's own headings one level under its section heading (a `#` heading becomes `###`).
- For Business at a glance, put the card first and then the document, because the card holds what the business does and the document holds the sign-up facts.

### 4. Tell the user
In a few plain lines:
- It's saved to `brain/source-of-truth.md`, and how many sections it holds.
- Which sections are still empty, each with the step that fills it: Business at a glance (`business-today`), Ideal client (`avatar-profile`), Problem and promise and Your offers (`offer-architect`), What makes you different (`what-makes-you-different`), Values and convictions (`conviction-map`), Brand (`brand-style-guide`), Your story (`your-story`), Goals and vision (`goals-and-vision`), Sales path (`sales-path`), Marketing plan (`marketing-plan`). Website and Authority Directory fills from Website Copy or the Directory Dossier, which open in HQ after a short call with the Perfect Little Business team.
- Offer to start the first empty one.

## Fallback: the plan isn't switched on in HQ
Run the Source of Truth step instead, the way this skill used to:
1. Call `get_stage_prompt` with `stage_key: "source_of_truth"`. What comes back already holds the user's profile and every step they've finished in HQ.
2. Also read `brain/` and `CLAUDE.md`, and use them for anything HQ's text doesn't have yet. Never ask for what either one already holds.
3. Operate exactly as the returned instructions say. Open with the opening message, word for word. One question at a time. When the final document is ready, show it as a clean document (the completion protocol's output markers are for the HQ app's screen: leave them out here).
4. Ask: "Shall I save this to Perfect Little Business HQ? I'll keep a copy in `brain/source-of-truth.md` too." On a yes, call `save_step` with `stage_key: "source_of_truth"`, the complete final document and `made_by: "source-of-truth"`, then write the same document to `brain/source-of-truth.md`, and tell the user what HQ said. If they'd rather not save it to HQ, keep just the local copy. If HQ refuses or the save fails, say so plainly and keep the local copy.

## How to talk about it
Call it "your plan in Perfect Little Business HQ" or "HQ", and "your Perfect Little Business connection". Never use technical names for the connection.
