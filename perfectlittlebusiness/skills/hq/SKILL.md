---
name: hq
description: Your front door to Perfect Little Business HQ from your own AI. Shows where your business plan stands and what's next, then runs any planning step or guide by name, including ones newer than this plugin. Use when the user says /hq, "what's next", "what's my next step", "where am I in HQ", "what can I do in HQ", "what guides are there", "run the [name] step", or names an HQ step or guide that has no command of its own, such as Website Copy or the Directory Dossier.
---

# /hq: your front door to HQ

HQ holds the client's plan, every planning step and every guide. This skill asks HQ what exists and what's open for this person, then runs it. Because the list comes from HQ, a step or guide added there works here the same day, with no plugin update. Never run a step or guide from memory: fetch it from HQ every time.

## 1. Read where they stand
Call `get_client_progress` and `get_guide` (no arguments) from the Perfect Little Business connection.
- **The tools aren't available:** the user hasn't signed in to their Perfect Little Business connection yet. Tell them how, for where they're working, then stop:
  - Claude desktop app or claude.ai: Customize, then Connectors, then Perfect Little Business, then Connect.
  - Claude Code: type `/mcp`, choose `plugin:perfectlittlebusiness:perfectlittlebusiness`, then Authenticate.
  - Codex: in a terminal, run `codex mcp login perfectlittlebusiness`.
  Signing in opens HQ's sign-in page in their browser. They use the email of their HQ account.
- **It says the workspace isn't an active client yet:** relay that warmly and stop.
- **`get_guide` isn't there:** carry on with the planning steps and leave guides out.

## 2. If they didn't name anything, show them where they are
A short briefing, then a choice:

```
**Your plan in HQ:** {N} of {M} sections filled. Next: {section} ({the step that fills it}).
**Guides:** {one line each: title, how long it takes}
```

- If this folder has no `CLAUDE.md` and no `brain/` folder, say the AI Operating System setup comes first, and make it the recommended choice.
- Otherwise offer: the next step (recommended), a guide, or something else. Use your app's question tool if it has one, or a short numbered list.

## 3. Run what they choose

### A planning step
Match their words to a stage key from HQ: business_today, avatar_profile, offer_architect, conviction_map, what_makes_you_different, brand_style_guide, your_story, goals_and_vision, sales_path, marketing_plan, website_copy, directory_dossier.
1. **Fetch it.** Call `get_stage_prompt` with the stage key. It returns the opening message, the step's full instructions (wrapped in everything HQ already knows about them), how to save it, and where to keep their copy. If it says the step opens after a short call with the Perfect Little Business team, tell them that, give them the link it gives, and stop.
2. **Add what's only on this computer.** Read `CLAUDE.md` and the file named under "Keeping a copy", if they exist. HQ's text already holds everything they've finished in HQ, so use these only for what it doesn't have. Never ask for anything either one already holds.
3. **Run it.** Operate exactly as the returned instructions say. Open with the opening message, word for word. One question at a time. Don't add, skip, reorder or summarize away anything they specify. When the final document is ready, show it as a clean document; the completion protocol's output markers are for the HQ app's screen, so leave them out.
4. **Ask, then save.** Ask one plain question before saving anything: "Shall I save this to your plan in Perfect Little Business HQ? I'll keep a copy in {the file} too." Wait for a yes. If they want changes, make them, show the result and ask again. On a yes, do what "Saving it to HQ" says (`save_step` with the stage key, the complete document exactly as they agreed to it, and `made_by: "hq"`), write the copy where "Keeping a copy" says, and tell them what HQ said, plus one line that the copy is in place. If the step can't be saved from here, keep the copy and tell them it saves when they run it in the HQ app. If HQ refuses or the save fails, say so plainly, keep the copy, and don't retry in a loop.

### A guide
Call `get_guide` with its slug and run it exactly as its "How to run a guide" says, fetching one step at a time. The AI Operating System setup is slug `aios-setup` (the same thing `/setup` runs).

## How to talk about it
Call it "your plan in Perfect Little Business HQ" or "HQ", and "your Perfect Little Business connection". Never use technical names for the connection, the tools or the stage keys: say "Avatar Profile", not "avatar_profile".

## Scope
One step or guide at a time. When it's finished, show what's next (section 2) and let them choose.
