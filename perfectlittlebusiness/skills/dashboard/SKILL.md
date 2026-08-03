---
name: dashboard
description: Stand up your personal Cowork OS dashboard as a live, pinnable Artifact. Use when the user wants to install, set up, build, or open their dashboard / Cowork OS / AIOS dashboard, or says "dashboard", "set up my dashboard", "my Cowork OS", "build my dashboard". Personalizes the bundled dashboard template with the user's connectors, skills, and business, then delivers it as a Cowork Artifact.
---

# /dashboard — Stand Up Your Cowork OS Dashboard

Turn the bundled Cowork OS dashboard template into the user's own personalized, live dashboard, delivered as a Cowork Artifact they can pin and open every day. The dashboard is the visual home of their AIOS Brain: pipeline, day, goals, projects, the numbers, and their skills, in one pane.

The template (`cowork-os-dashboard.html`, in this skill's folder) ships with connector placeholders and generic demo content. This skill personalizes it for the specific user, then hands it to them as an Artifact. **Never edit the template in place — always produce a personalized copy.**

## How it runs

### 1. Read the template
Load `cowork-os-dashboard.html` from this skill's folder. You will produce a personalized copy of it, not modify the original.

### 2. Personalize the connectors (the one genuinely user-specific input)
The config block at the top of the file uses four placeholders:
- `__YOUR_CALENDAR_CONNECTOR__` (Google Calendar)
- `__YOUR_GMAIL_CONNECTOR__` (Gmail)
- `__YOUR_OBSIDIAN_CONNECTOR__` (notes / Obsidian)
- `__YOUR_GRANOLA_CONNECTOR__` (Granola meetings)

Detect the user's connected MCP servers if you can; otherwise ask which of these four they have and the exact connector name for each. Replace **every** occurrence of each placeholder with the real connector name. If the user does not have one, leave that placeholder and tell them that tab stays empty until they connect it. Do not invent connector names.

### 3. Personalize the "Skills & agents" view as TWO sections
Replace the `SKILLS` data with two clearly-labelled groups:

- **Your installed skills** — the plugin's operating skills and AIOS Brain tools: `/start`, `/end`, `/hygiene`, `/learn`, `/decide`, `/recap`, `/digest`, `/ask`, `/how-to`, `/granola-pull`, `/draft-social`, `/voice-qa`, `/avatar-profile`, `/offer-architect`, `/conviction-map`, `/brand-style-guide`, `/source-of-truth`, `/gravity-dossier`, `/dossier-qa`, `/setup`. Use each skill's real one-line description.
- **Your custom agents** — the user's own workflow agents. Scan their installed skills for anything beyond the plugin's set and list those. If they have none yet, show a single neutral line: "Your custom agents will appear here as you build them."

Render these as two sections (a heading per group), not one flat list.

### 4. Neutralize the demo persona
The template's Jarvis sample questions and any example prompts reference a generic creator persona. Rewrite the Jarvis sample questions to neutral, business-appropriate prompts grounded in the user's actual business (read `brain/source-of-truth.md` if it exists). Good neutral examples: "What's in my content pipeline?", "What meetings do I have today?", "What did I commit to on my last call?", "What should I work on next?". Remove creator-specific references (subscribers, YouTube, Skool) unless they genuinely apply to this user.

### 5. Deliver as a Cowork Artifact
Output the fully personalized HTML as a Cowork Artifact. Tell the user:
- It is now in their Artifacts list.
- Open it and pin it; open it at the start of each work day.
- The Projects tab reads each Claude Code project's `status.json`, so it fills in automatically as they run `/end` in their projects.

### 6. Hand off to the built-in guide
Point the user to the dashboard's own **Get set up** tab. It walks them through connecting Calendar and Gmail, touring the tabs, and the three-phase onboarding, with progress saved on their device.

## Notes for Claude executing this skill

- The bundled template is read-only. Produce a personalized copy; never write changes back to `cowork-os-dashboard.html`.
- Connectors are the input most worth getting exactly right. Confirm names before substituting.
- If the user just wants a quick preview, you may render the template as-is, but warn them the connector-driven tabs (Calendar, Gmail, meetings) stay empty until personalized.
- Keep the user's brand voice: if `brain/brand-style-guide.md` exists, honor it in any copy you write into the dashboard.
