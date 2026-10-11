---
name: your-story
description: >-
  Run the Your Story planning step: the story behind the business in the owner's own voice (where it began, why it exists, what they bring, what they ask of clients, the impact), then a short look over the whole plan for gaps. Saves it to the user's plan in Perfect Little Business HQ (the Your story card) and to brain/your-story.md. Use when the user says "your story", "my story", "my origin story", "about page story", or "why my business exists".
---

# Your Story

Runs the **Your Story** step from Perfect Little Business HQ, then, once the user says yes, saves it to HQ exactly as if they'd done it in the HQ app: the step is marked finished, the Your story card on their business plan fills itself, and a copy goes to `brain/your-story.md` in this project. The step's instructions live in HQ and are fetched fresh every time. Never copy them into this file.

## How it runs

### 1. Fetch the step
Call `get_stage_prompt` from the Perfect Little Business connection with `stage_key: "your_story"`. What comes back is everything HQ wraps around this step: today's date, the user's profile, every step they've already finished, the shared rules, the step's own instructions, and how to finish and save it.
- **The tool isn't available:** the user hasn't signed in to their Perfect Little Business connection yet. Tell them how, for where they're working, then stop:
  - Claude desktop app or claude.ai: Customize, then Connectors, then Perfect Little Business, then Connect.
  - Claude Code: type `/mcp`, choose `plugin:perfectlittlebusiness:perfectlittlebusiness`, then Authenticate.
  - Codex: in a terminal, run `codex mcp login perfectlittlebusiness`.
  Signing in opens HQ's sign-in page in their browser. They use the email of their HQ account.
- **It says the workspace isn't an active client yet:** relay that warmly and stop.

### 2. Add what's only on this computer
Read these files if they exist: `brain/business-today.md`, `brain/avatar-profile.md`, `brain/offer-architecture.md`, `brain/convictions.md`, `brain/what-makes-you-different.md`, `brain/brand-style-guide.md`, `brain/your-story.md`, and `CLAUDE.md`. HQ's text already holds everything the user has finished in HQ, so use these only for what it doesn't have yet. Never ask the user for anything either one already holds.

### 3. Run the step
Operate exactly as the returned instructions say. Open with the opening message, word for word. One question at a time. Don't add, skip, reorder or summarize away anything they specify. When the final document is ready, show it to the user as a clean document. The completion protocol's output markers are for the HQ app's screen: leave them out here.

The step ends with a short look over the plan, naming up to three gaps. That list comes after the final document and stays in the conversation: it isn't part of what you save. Name each gap's step by its command here (for example `goals-and-vision`).

### 4. Ask, then save
When the final document is finished, ask one plain question before saving anything: "Shall I save this to your plan in Perfect Little Business HQ? I'll keep a copy in `brain/your-story.md` too." Wait for a yes. If they want changes, make them, show the result and ask again.

On a yes:
1. **HQ.** Call `save_step` with `stage_key: "your_story"`, `document`: the complete final document, exactly as the user agreed to it, and `made_by: "your-story"`. 
2. **Local copy.** Write the same document to `brain/your-story.md` (create `brain/` if needed), replacing what was there.
3. **Tell the user** what HQ said (its reply is written for them), plus one line that a copy is in `brain/your-story.md`.

If they'd rather not save it to HQ, offer to keep just the local copy. If HQ refuses the save or it fails, tell them plainly what it said, keep the local copy, and don't retry in a loop.

## How to talk about it
Call it "your plan in Perfect Little Business HQ" or "HQ", and "your Perfect Little Business connection". Never use technical names for the connection.

## Scope
Run only this step. The next step is `goals-and-vision`. (Website Copy and the Directory Dossier sit between them in HQ; they open in HQ after a short call with the Perfect Little Business team.) The planning steps, in order: business-today, avatar-profile, offer-architect, conviction-map, what-makes-you-different, brand-style-guide, your-story, goals-and-vision, sales-path, marketing-plan. For anything else, point the user to the right one and come back.
