---
name: setup
description: Set up your AI Operating System in this folder, with your business plan from Perfect Little Business HQ already in it. Walks you through it one step at a time (about 60 to 90 minutes, and you can stop after any step) and checks each step before moving on. Run it once in a new folder, and again whenever /start says the setup has improved: it brings your system up to date and keeps everything you've written. Use when the user says /setup, "set up my AI operating system", "install my AIOS", "set up this folder", "continue my setup", or "update my setup".
---

# /setup: your AI Operating System, step by step

The setup lives in Perfect Little Business HQ and is fetched fresh every time, so every improvement reaches you without an update to this plugin. This file only opens it. Never rebuild the setup from memory, or from an earlier version of this file.

## How it runs

### 1. Open the guide
Call `get_guide` from the Perfect Little Business connection with `slug: "aios-setup"`. It returns why the setup matters, its steps' titles, the rules that hold in every step, and how to run a guide.
- **The tool isn't available:** the user hasn't signed in to their Perfect Little Business connection yet. Tell them how, for where they're working, then stop. The setup builds from their plan in HQ, so it needs the connection.
  - Claude desktop app or claude.ai: Customize, then Connectors, then Perfect Little Business, then Connect.
  - Claude Code: type `/mcp`, choose `plugin:perfectlittlebusiness:perfectlittlebusiness`, then Authenticate.
  - Codex: in a terminal, run `codex mcp login perfectlittlebusiness`.
  Signing in opens HQ's sign-in page in their browser. They use the email of their HQ account.
- **It says the workspace isn't an active client yet:** relay that warmly and stop.
- **The connection works but has no `get_guide`, or says there's no guide called "aios-setup":** HQ isn't ready for this version of the plugin yet. Tell the user the setup isn't available just now and that nothing has changed in their folder, then stop. Never fall back to an older setup.

### 2. Run it exactly as the guide says
Follow the guide's "How to run a guide" and its rules. One step at a time: fetch each step with `get_guide`, `slug: "aios-setup"` and the step's number, only when you reach it.

### 3. Continuing, or updating an earlier setup
- **"Continue my setup":** read the setup entry in `MEMORY.md`, tell them where they are, and pick up at the next unfinished step.
- **A folder that already has a setup** (a `CLAUDE.md` or a `brain/` folder): the guide's first step offers to keep it, improve it to today's standard, or start fresh. Improving never replaces what they wrote.

## How to talk about it
Call it "your plan in Perfect Little Business HQ" or "HQ", and "your Perfect Little Business connection". Never use technical names for the connection.

## When it's done
Don't start other work in the same response. Their next move is to open a new session and type `/start`.
