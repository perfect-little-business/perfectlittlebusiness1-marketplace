# Perfect Little Business — Your AI Operating System

The Perfect Little Business plugin is the infrastructure layer of your AI Operating System, installed in Claude (Cowork) and Claude Code.

Install it once. You get your AIOS Brain (the `brain/` folder and five foundational tools), twenty-one working skills, the voice-qa gate, three protective hooks, your Cowork OS dashboard, and the self-improvement loop that makes every session smarter than the last.

This is the operating system. Your AIOS Brain populates inside it.

---

## What This Plugin Installs

### Your AIOS Brain (five foundational tools)

Run these to build the second brain your whole system reads from. Each runs live from Authority HQ through the bundled connector and saves into your `brain/` folder.

- `/avatar-profile`: Your Avatar Emotional Profile — who you serve.
- `/offer-architect`: Your Offer Architecture — what you sell.
- `/conviction-map`: Your Conviction Map — what you believe and stand for.
- `/brand-style-guide`: Your Brand Style Guide — how you sound and look.
- `/source-of-truth`: Your Source of Truth — the master document that unifies the rest.

### Operating skills

**Core infrastructure:**
- `/setup`: One-time orchestrator. Creates your project structure, AIOS Brain folder, and CLAUDE.md.
- `/start`: Loads your context at the beginning of every session.
- `/end`: Closes the session cleanly. Updates MEMORY.md, learnings.md, wins.md, and commits.
- `/hygiene`: Weekly health check.
- `/recap`: "Where am I?" lifeline when returning to a project.

**Brain-building:**
- `/learn`: Capture an insight mid-session without ending the session.
- `/decide`: Log a decision with full context and rationale.
- `/ask`: Ask Claude a question grounded in your full AIOS Brain.

**Thought leadership:**
- `/gravity-dossier`: Interview yourself, or bring notes or a transcript, on one topic and get back a voice-preserved, three-layer Thought Leadership Dossier: the source-of-truth document your content gets built from.
- `/dossier-qa`: The cross-dossier consistency gate. Checks a dossier against your other dossiers and your Source of Truth for term conflicts, fact contradictions, topic overlap, and stale predictions. The Dossier runs it automatically; you can also run it on your whole dossiers folder as a periodic audit.

**Getting unstuck:**
- `/how-to`: Name a goal you want to reach with Claude and get walked there one beginner-proof step at a time, until you have built it yourself.

**Test-drive automations (use these while you build your AIOS Brain):**
- `/digest`: Personal weekly summary from your MEMORY, learnings, and wins.
- `/granola-pull`: Pull a Granola meeting into your AIOS Brain. Surfaces candidate learnings.
- `/draft-social`: Draft social posts in your voice from your recent learnings and wins.

### Your dashboard
- `/dashboard`: Stands up your personalized Cowork OS dashboard as a pinnable Artifact — pipeline, day, goals, projects, the numbers, and your skills in one pane.

### The voice-qa gate
- `/voice-qa`: Checks any draft against your brand voice rules and the universal "sounds like AI" tells before it ships. The Dossier runs it automatically; you can also run it on anything.

### Three Protective Hooks

- **Credential guard** — Blocks accidental commits of API keys, secrets, and credentials.
- **Forbidden-language guard** — Catches the hype-culture clichés your brand never uses before they ship.
- **Session-end nudge** — Reminds you to run `/end` at natural session-closing moments.

### Your AIOS Brain folder

When you run `/setup`, the plugin creates a `brain/` folder seeded with eleven files and folders:

```
brain/
├── source-of-truth.md      what you know
├── convictions.md          what you believe
├── avatar-profile.md       who you serve
├── offer-architecture.md   what you sell
├── brand-style-guide.md    how you sound and look
├── learnings.md            what you've discovered (grows session by session)
├── decisions.md            decisions made, with rationale
├── wins.md                 what's working
├── voice-samples/          your writing examples for tone matching
├── reference/              PDFs, articles, transcripts
└── templates/              reusable formats
```

Your AIOS Brain is yours. Edit any file any time. The plugin never touches it on updates.

---

## Installation

### In Claude (Cowork)

1. Open **Customize → Personal plugins**.
2. Click **+ → Add marketplace → Sync a marketplace from a GitHub repository**.
3. Paste `cmolchany/perfectlittlebusiness-marketplace`.
4. Install the **perfectlittlebusiness** plugin. The bundled connector and all skills install with it. No tokens, no configuration.

### In Claude Code (CLI)

```
/plugin marketplace add cmolchany/perfectlittlebusiness-marketplace
/plugin install perfectlittlebusiness@plb
```

Then in any project folder, run `/setup` (bare in Cowork; `/perfectlittlebusiness:setup` in Claude Code). Answer five questions. Your AIOS Brain is installed.

---

## Where You Are Right Now

If you're reading this, you've installed the **Perfect Little Business plugin** and stood up your AI Operating System.

The infrastructure is running. The intelligence layer is what you populate next.

### Build your AIOS Brain

Run your five foundational tools, in order:

`/avatar-profile` → `/offer-architect` → `/conviction-map` → `/brand-style-guide` → `/source-of-truth`

Each runs live from Authority HQ and saves into your `brain/` folder. When they're done, your AIOS Brain holds the second brain that makes every future session smarter than the last.

→ [hq.perfectlittlebusiness.com](https://hq.perfectlittlebusiness.com)

---

## After Your AIOS Brain

When your foundation is in place, two paths stay open.

### Collective Wisdom

The ongoing methodology and community, where the full Perfect Little Business doctrine lives and stays current. You'll get plugin updates, methodology evolutions, and the community of other AIOS operators building alongside you.

### Authority Directory

When you're ready to build the public-facing asset AI recommends in your domain:

- **Self-install** — your own Authority Directory codebase, configured and yours to run
- **Done-for-you** — built by the PLB team

Ask about current options on a call.

---

## About Perfect Little Business

PLB builds AI Operating Layers for entrepreneurs who are subject matter experts — coaches, consultants, specialists, and founder-led companies.

- Founder: [Cindy Molchany](https://perfectlittlebusiness.com)
- Web: [perfectlittlebusiness.com](https://perfectlittlebusiness.com)
- Contact: hello@perfectlittlebusiness.com
- Plugin issues: [github.com/cmolchany/perfectlittlebusiness-marketplace/issues](https://github.com/cmolchany/perfectlittlebusiness-marketplace/issues)

---

## License

Proprietary. Perfect Little Business. This plugin is provided to Perfect Little Business clients for personal use. Please don't redistribute. If a friend needs this, send them to [perfectlittlebusiness.com](https://perfectlittlebusiness.com).

— Cindy Molchany
