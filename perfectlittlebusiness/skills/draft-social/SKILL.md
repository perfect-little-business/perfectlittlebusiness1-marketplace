---
name: draft-social
description: Draft social media posts in your voice from your recent learnings, wins, and convictions. Produces 3 versions to choose from. Calibrated to your voice samples and stated brand voice.
---

# /draft-social — Voice-Calibrated Social Drafter

## Purpose

Remove the blank page. Draft social posts that sound like the user, grounded in their actual recent insights — not generic AI content. This skill works even with a sparse brain because it leans on convictions + recent learnings + voice samples.

## When To Use

- User has been wanting to post but stalled
- Recent learning or win deserves to be shared publicly
- Building distribution discipline
- Testing what resonates with audience

## Execution Instructions

### Step 1: Get the Topic

Ask: "What do you want to post about? You can:
- Give me a specific topic
- Tell me to pull from a recent learning
- Tell me to pull from a recent win
- Say 'surprise me' and I'll suggest 3 candidate topics from your recent brain activity"

### Step 2: Load Voice Context

Read:
1. CLAUDE.md (brand voice section)
2. brain/convictions.md
3. brain/voice-samples/ (all files — these are critical for tone match)
4. brain/learnings.md (recent entries — for content material)
5. brain/wins.md (recent entries)

### Step 3: Handle Different Topic Inputs

**If user gave a specific topic:** Use it directly. Draw supporting material from convictions, learnings, wins where relevant.

**If user said "pull from a recent learning":** Pick the most postable recent learning. Show: "Drafting from this learning: [bullet]. Sound right?" Get approval, then proceed.

**If user said "pull from a recent win":** Same flow but with wins.

**If user said "surprise me":** Generate 3 candidate topics:
```
Three topics I noticed in your recent brain activity:

1. [Topic suggestion grounded in a specific learning]
2. [Topic suggestion grounded in a specific win or conviction]
3. [Topic suggestion grounded in something you discovered]

Which one? Or give me a different topic.
```

Wait for selection. Then proceed.

### Step 4: Draft Three Versions

Produce three distinct angles on the same topic. Each in their voice. Each different in tone/structure:

```
**📝 THREE DRAFTS — [TOPIC]**

---

**Version 1: [Angle name — e.g., "The Observation"]**

[Draft 1 — typically 50-150 words, voice-calibrated]

---

**Version 2: [Angle name — e.g., "The Contrast"]**

[Draft 2 — different structure, same voice]

---

**Version 3: [Angle name — e.g., "The Question"]**

[Draft 3 — different opening hook]

---

All three are calibrated to your voice based on your samples and PLB voice guidelines. Pick one, ask for edits, or ask for a different angle.
```

### Step 5: Iterate

User responses possibilities:
- "I like version 2 but soften the opening" → revise
- "Combine 1's opening with 2's middle" → combine
- "Try a different angle" → produce three new versions
- "Version 3 is good — copy ready" → present clean copy-paste version

### Step 6: Offer Capture

When user lands on a final version, ask: "Want me to save this to brain/reference/social-drafts/ for reference?"

If yes, save with date and topic in filename.

---

## Voice Calibration Rules

When drafting, ALWAYS:
- Mirror sentence rhythm and structure from voice-samples/
- Maintain the user's stated three-word brand voice (from CLAUDE.md)
- Stay grounded in their actual conviction, not abstract trend-talk
- Avoid the phrases the forbidden-language-guard hook blocks (hustle, crush it, guru, level up, passive income, game-changer, "let's dive in", "unlock the power of", etc.) — if you draft these, the hook will block the write anyway

- Rewrite zombie nouns: when a noun ending in -tion, -ment, -ity, -ance, -ence, -ness, or -ization hides a shorter verb, rewrite around the verb with a human subject ("we stay in communication" becomes "we keep talking"). Nouns that name a product, deliverable, or coined term are exempt — the rule targets buried actions, not named things.
- Cold-audience openers blame the external system, never the reader's state: name what changed or failed around them, then point up to their ambition. Never open by naming what the reader might fear becoming, even to negate it — reassurance forces the rescue frame, and readers want a guide, not a rescue.

Three voice versions should differ by:
- Opening hook structure (observation / contrast / question / story)
- Sentence rhythm (short staccato / longer flowing / mixed)
- Where the conviction or insight lands (start / middle / end)

NOT differ by:
- The underlying conviction
- The core point
- The user's voice

---

## Notes for Claude Executing This Skill

- **If voice-samples/ is empty,** flag this: "Your voice-samples folder is empty. I'll draft based on your stated brand voice, but the match will improve dramatically once you drop 2-3 writing samples in brain/voice-samples/."
- Don't generate corporate-sounding hooks ("In today's fast-paced digital landscape..."). Hooks should feel like an observation from a thoughtful person, not a marketing pull.
- Don't include hashtags unless user requests them or their voice samples consistently use them.
- Keep drafts at posting length — usually 50-200 words per draft. Long-form is a different skill.
- If the user's recent learnings are thin and the topic doesn't match anything in their brain, say so: "Your brain doesn't have much on this topic yet. Want me to draft generically, or pick a topic I have more material on?"
