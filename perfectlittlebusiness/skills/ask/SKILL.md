---
name: ask
description: Ask Claude a question grounded in your full brain context. Forces Claude to read CLAUDE.md and brain/ before answering, ensuring the response is specific to your business, not generic.
---

# /ask — Contextual Brain Query

## Purpose

Force Claude to answer using the user's full context, not generic knowledge. Use whenever the answer should be specific to *their* business, *their* convictions, *their* avatar, *their* methodology — not Claude's defaults.

## When To Use

- "Based on everything you know about me..."
- "What should I do about X?"
- "How does this fit my methodology?"
- "Is this aligned with my convictions?"
- Strategic questions that deserve a contextual answer

## Execution Instructions

### Step 1: Get the Question

If the user typed `/ask` alone, ask: "What's your question?"

If the user typed `/ask [question]`, use the content directly.

### Step 2: Read Everything Relevant

Read in this order:
1. CLAUDE.md
2. brain/source-of-truth.md
3. brain/convictions.md
4. brain/avatar-profile.md
5. brain/learnings.md (especially recent entries)
6. brain/decisions.md (especially recent)
7. brain/wins.md
8. brain/inspiration/_INDEX.md, if it exists (open an entry only when it plausibly bears on the question)

### Step 3: Answer

Provide an answer that:
- Explicitly references their context (their conviction, their avatar, their recent learning)
- Flags conflicts between the question and their stated convictions
- Avoids generic advice that could apply to any business
- Names tradeoffs if there are real tradeoffs

Format the response as natural prose, not a bullet list. Reference specific files/insights when you draw from them: "Per your learnings.md from [date], you noted X. That suggests..."

### Step 4: Offer Follow-Up

End with: "Want me to go deeper on any part of this, or capture anything new to brain/?"

---

## Notes for Claude Executing This Skill

- This skill exists to prevent generic answers. If you can't tie the answer to their context, say so: "Your brain doesn't yet have enough context to answer this specifically. Here's a generic answer — and here's what to populate in your brain to get a better one next time."
- If their question conflicts with their stated convictions, flag it directly but warmly.
- Don't pad responses with generic best-practices. Their brain is the source. Stay close to it.
