# Perfect Little Business: Your AI Operating System

The Perfect Little Business plugin is the infrastructure layer of your AI Operating System, installed in Claude (Cowork), Claude Code and Codex. It is also your way into Perfect Little Business HQ from your own AI: every planning step in HQ runs here too, and either way the result lands on your business plan in HQ.

Install it once. You get your AIOS Brain (the `brain/` folder), ten planning steps that save to your plan in HQ, the Source of Truth, twenty-eight working skills in all, the voice-qa gate, three protective hooks, and the self-improvement loop that makes every session smarter than the last.

This is the operating system. Your AIOS Brain populates inside it.

---

## What This Plugin Installs

### Your planning steps

The same steps as in Perfect Little Business HQ, in the same order. Each one fetches the step fresh from HQ and works from everything you've already finished. When you're done, it asks before it saves. Then the step counts in HQ exactly as if you'd done it there: it's marked finished, its card on your business plan fills in, and a copy goes to your `brain/` folder.

- `/business-today`: Your Business Today. Where your business stands right now, in plain numbers.
- `/avatar-profile`: Avatar Emotional Profile. Who you serve.
- `/offer-architect`: Offer Architect. The problem you solve, your promise, and what you sell.
- `/conviction-map`: Conviction Map. What you believe and stand for.
- `/what-makes-you-different`: What Makes You Different. Why your ideal client chooses you.
- `/brand-style-guide`: Brand Style Guide. How you sound and look.
- `/your-story`: Your Story. Where it began, why it exists, the impact you're here to make.
- `/goals-and-vision`: Goals and Vision. The next 12 months and this quarter's goal. Run it again each quarter.
- `/sales-path`: Your Sales Path. How a stranger becomes a paying client, and the numbers it needs.
- `/marketing-plan`: Marketing Plan. Where your marketing energy goes this quarter. Saving it fills your content calendar in HQ.

Website Copy and the Directory Dossier stay in HQ. They open there after a short call with the Perfect Little Business team.

### Your Source of Truth
- `/source-of-truth`: Pulls your whole business plan from HQ into one document, `brain/source-of-truth.md`, ready to hand to any AI. Run it again whenever your plan changes.

### Operating skills

**Core infrastructure:**
- `/setup`: Sets up your AI Operating System in a folder, one checked step at a time, with your plan from HQ already in it. Run it again when `/start` says the setup has improved: it keeps everything you've written. The setup itself lives in HQ, so it improves without a plugin update.
- `/hq`: Your front door to HQ. Shows where your plan stands and what's next, and runs any step or guide by name, including ones newer than this plugin.
- `/start`: Loads your context at the beginning of every session, including your plan in HQ and this week's content calendar.
- `/end`: Closes the session cleanly. Updates MEMORY.md, learnings.md, wins.md, and commits.
- `/hygiene`: Weekly health check.
- `/recap`: "Where am I?" lifeline when returning to a project.

**Brain-building:**
- `/learn`: Capture an insight mid-session without ending the session.
- `/decide`: Log a decision with full context and rationale.
- `/hold`: Hold on to a story, quote, idea or observation you want to use later, with your own words about what you would connect it to. Finds them again when you draft, and stamps them when they ship.
- `/ask`: Ask Claude a question grounded in your full AIOS Brain.

**Thought leadership:**
- `/gravity-dossier`: Interview yourself, or bring notes or a transcript, on one topic and get back a voice-preserved, three-layer Thought Leadership Dossier: the source-of-truth document your content gets built from.
- `/dossier-qa`: The cross-dossier consistency gate. Checks a dossier against your other dossiers and your Source of Truth for term conflicts, fact contradictions, topic overlap, and stale predictions. The Dossier runs it automatically; you can also run it on your whole dossiers folder as a periodic audit.

**Getting unstuck:**
- `/how-to`: Name a goal you want to reach with Claude and get walked there one beginner-proof step at a time, until you have built it yourself.

**Test-drive automations (use these while you build your AIOS Brain):**
- `/digest`: Personal weekly summary from your MEMORY, learnings, and wins.
- `/granola-pull`: Pull a Granola meeting into your AIOS Brain. Surfaces candidate learnings.
- `/draft-social`: Draft social posts in your voice from your recent learnings and wins. Offers the pieces planned on your content calendar in HQ, and marks the finished post as drafted there.

### The voice-qa gate
- `/voice-qa`: Checks any draft against your brand voice rules and the universal "sounds like AI" tells before it ships. The Dossier runs it automatically; you can also run it on anything.

### Three Protective Hooks

- **Credential guard**: Blocks accidental commits of API keys, secrets, and credentials.
- **Forbidden-language guard**: Catches the hype-culture clichés your brand never uses before they ship.
- **Session-end nudge**: Reminds you to run `/end` at natural session-closing moments.

### Your AIOS Brain folder

`/setup` builds a whole folder around it: `CLAUDE.md` (the briefing your AI reads every session), `README.md`, `MEMORY.md`, `ops/` (what your AI can do freely and what waits for your yes), `loop/insights.md` (an inbox for things worth keeping), `clients/` (one confidential folder per client, if you work with clients one to one), `work/`, `archive/`, and a folder for each other business you run. Your plan from HQ comes into `brain/`, alongside who's who (`people.md`) and your ownership and confidentiality lines (`boundaries.md`). Each planning step adds or updates its own file as you run it:

```
brain/
├── source-of-truth.md          your whole plan in one document
├── business-today.md           where the business stands
├── avatar-profile.md           who you serve
├── offer-architecture.md       what you sell
├── convictions.md              what you believe
├── what-makes-you-different.md why clients choose you
├── brand-style-guide.md        how you sound and look
├── your-story.md               where it began, why it exists
├── goals-and-vision.md         where it's going, this quarter
├── sales-path.md               how a stranger becomes a client
├── marketing-plan.md           where marketing energy goes
├── learnings.md                what you've discovered (grows session by session)
├── decisions.md                decisions made, with rationale
├── wins.md                     what's working
├── voice-samples/              your writing examples for tone matching
├── reference/                  PDFs, articles, transcripts
├── templates/                  reusable formats
└── inspiration/                stories, quotes and ideas you are holding on to (via /hold)
```

Your AIOS Brain is yours. Edit any file any time. The plugin never touches it on updates.

---

## Installation

### In Claude (Cowork)

1. Open **Customize**, then **Personal plugins**.
2. Click **+**, then **Add marketplace**, then **Sync a marketplace from a GitHub repository**.
3. Paste `perfect-little-business/perfectlittlebusiness1-marketplace`.
4. Install the **perfectlittlebusiness** plugin. Its connection to Perfect Little Business HQ and all its skills install with it.

### In Claude Code

```
/plugin marketplace add perfect-little-business/perfectlittlebusiness1-marketplace
/plugin install perfectlittlebusiness@plb1
```

### In Codex

```
codex plugin marketplace add perfect-little-business/perfectlittlebusiness1-marketplace
codex plugin add perfectlittlebusiness@plb1
```

### Then sign in to HQ, once

The plugin's planning steps read and save your plan in Perfect Little Business HQ, so the first time you run one, sign in with the email of your HQ account:

- **Claude (Cowork):** Customize, then Connectors, then Perfect Little Business, then Connect.
- **Claude Code:** type `/mcp`, choose `plugin:perfectlittlebusiness:perfectlittlebusiness`, then Authenticate.
- **Codex:** run `codex mcp login perfectlittlebusiness` in a terminal.

Then in any project folder, run `/setup`. Command names are bare in Cowork (`/setup`) and start with the plugin's name in Claude Code (`/perfectlittlebusiness:setup`).

---

## Where You Are Right Now

If you're reading this, you've installed the **Perfect Little Business plugin** and stood up your AI Operating System.

The infrastructure is running. Your plan is what you build next.

### Build your plan

Run your planning steps in order, here or in HQ, whichever suits you:

`/business-today` → `/avatar-profile` → `/offer-architect` → `/conviction-map` → `/what-makes-you-different` → `/brand-style-guide` → `/your-story` → `/goals-and-vision` → `/sales-path` → `/marketing-plan`

Each one asks before it saves, then saves to your business plan in HQ and to your `brain/` folder. `/start` tells you which one is next.

→ [hq.perfectlittlebusiness.com](https://hq.perfectlittlebusiness.com)

---

## When Your Plan Is in Place

Your plan in Perfect Little Business HQ is home base. Every step you finish shows there, and your content calendar fills from your Marketing Plan.

When you're ready for a website or an Authority Directory (the public asset AI engines read when someone asks who to hire in your field), Website Copy and the Directory Dossier open in HQ after a short call with the Perfect Little Business team. You can book it from your plan in HQ.

---

## About Perfect Little Business

Perfect Little Business builds AI Operating Layers for entrepreneurs who are subject matter experts: coaches, consultants, specialists, and founder-led companies.

- Founder: [Cindy Molchany](https://perfectlittlebusiness.com)
- Web: [perfectlittlebusiness.com](https://perfectlittlebusiness.com)
- Contact: hello@perfectlittlebusiness.com

---

## License

Proprietary. Perfect Little Business. This plugin is provided to Perfect Little Business clients for personal use. Please don't redistribute. If a friend needs this, send them to [perfectlittlebusiness.com](https://perfectlittlebusiness.com).

Cindy Molchany
