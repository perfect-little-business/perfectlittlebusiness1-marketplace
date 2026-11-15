---
name: voice-review
description: Your voice review. Compares what your AI drafted for you with what you actually sent or posted, shows how much of each draft you kept, and turns the changes you make again and again into voice rules for your yes, so your AI sounds more like you every week. Use when the user says /voice-review, "run my voice review", "voice review", "how much of my drafts am I keeping", "what do I keep changing", or "approve my voice rules". Best once a week.
---

# /voice-review: teach your AI your voice from your own edits

Every time you change a draft before sending it, that change says something about how you write.
This skill reads those changes, scores them, and suggests rules. The numbers and the rules live on
your Voice review page in Perfect Little Business HQ. Your emails and posts never leave your own
email and files: HQ scores each pair and keeps only the numbers.

## 0. Check the connection

This needs the Perfect Little Business connection. If its tools aren't available, tell them in one
line that voice review runs through their HQ connection and how to sign in for where they're
working, then stop. If a tool says voice review comes with working with Perfect Little Business,
pass that on warmly, in a sentence, and stop.

## 1. Find the drafts waiting to be compared

Look in `brain/reference/drafts/` and `brain/reference/social-drafts/` for drafts with no
`scored:` line at the top. Your AI saves a copy there whenever it drafts an email or post for them
to send. Take the ones at least a day old.

None there? Say so in one line. Tell them their AI keeps a copy of each email or post it drafts
from now on, and to come back in a week. Then go to step 4, which still has news if rules are
waiting.

## 2. Find what they actually sent

For each draft, oldest first:

- **An email, with their email connected:** search their Sent mail for it. Use the recipient, a
  word or two from the subject, and dates after the draft's. Take only the new text: cut the
  quoted earlier messages and the signature.
- **A post, or no email connection:** ask, one draft at a time: "Here's the draft for {who or
  what}. Paste what you actually sent, or say 'sent as is' or 'didn't send'."
- **Didn't send, or can't be found after two weeks:** add `scored: not sent` at the top of the
  file and move on.

## 3. Score each one

Call `score_voice_pair` with:

- `pair_id`: the draft's file name.
- `kind`: one of these.
  - `client`: an email to a current client
  - `prospect`: an email to a potential client
  - `partner`: an email to their team or a partner
  - `reply`: any other reply
  - `other-email`: any other email
  - `newsletter`
  - `social`: a post or comment
  - `article`
- `draft` and `sent`: the two texts.
- `tags`: what changed, only from too-long, too-short, tone, different-opening, changed-the-ask,
  added-personal-detail, removed-something, wrong-approach, fact-fix, sent-as-is.
- `note`: one plain line on what they changed, e.g. "cut the opening pleasantry; ended with a
  question". Describe the change. Never quote the person they wrote to.

Then add `scored: {today's date}, kept {N}%` at the top of the draft file.

## 4. Suggest rules, then bring in the approved ones

Look across everything scored today, and earlier notes if you have them, for a change they made in
**at least two different pieces**. One edit is a choice. A repeat is a rule. Leave out anything
already in `brain/brand-style-guide.md`.

Call `propose_voice_rules` with each one:

- **The rule:** one sentence their AI could check a draft against, like "Open a client email with
  the answer, not a pleasantry."
- **The evidence:** how often it was seen, and the change in your own words.

Then call `get_voice_rules`. For each approved rule not already in `brain/brand-style-guide.md`,
add it under a heading "Voice rules from my edits", with the date. That file is what every draft
reads, so the next draft follows it.

## 5. Tell them, in plain words

In three or four lines:

- **How much of your drafts they kept this time**, and this month, if HQ said.
- **What they changed most.**
- **Rules waiting for their yes.** Say how many, and that they approve or drop each one on their
  Voice review page in HQ (give the link the tool returned).
- **Rules added to their brand style guide** today, if any.

Never send, edit or delete an email or a post. Never paste their emails or posts anywhere but the
scoring call.
