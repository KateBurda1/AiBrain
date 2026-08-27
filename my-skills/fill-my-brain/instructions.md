---
name: fill-my-brain
description: Fills in your business files automatically by reading your real email, your website, and your documents, instead of you typing everything in. Use when you hear "fill my brain", "learn my business", "get my info in", "read my inbox and learn", or "/fill-my-brain".
---

# Fill My Brain

## Goal
Fill in the files in `my-business (context)/` with real facts about the business, pulled from sources the owner already has: their email, their website, and their documents. The owner confirms every fact before it is saved. Nothing is invented.

This is the fastest way to a smart assistant. Typing your business in by hand takes an hour. Letting your assistant read what already exists takes minutes.

It can run three ways. Ask which the owner wants, or run all three:

1. **From your email** - mines your inbox and sent mail for facts: who your customers are, what you charge, what you have promised, who your key contacts are.
2. **From your website** - reads your own website and public pages for what you tell the world: services, prices, story, tone.
3. **From your files** - reads documents in `my-files (knowledge)/` (or a folder the owner points at): brochures, proposals, price lists, brand guides.

## Inputs
- For email: email connected (Gmail or Microsoft 365). If not connected, offer /connect first, or skip this source.
- For website: the business website address (check `my-business (context)/who-we-are.md` and ask if missing).
- For files: documents dropped into `my-files (knowledge)/`, or a folder path the owner gives.
- None of the three is required. Use what they have.

## Hard rules for this skill
- **Read only.** This skill never sends, deletes, moves, or changes anything in their email, website, or files. It only reads and takes notes.
- **Facts, not chit-chat.** A fact is something true about the business: a customer name, a price, a service, a promise, a key contact. Skip gossip, pleasantries, and anything personal that is not business.
- **Never paste a full private email into the conversation.** Quote short snippets only, and only when needed to confirm a fact.
- **Confirm before saving.** Show the owner what was found, grouped by file, and let them correct it before anything is written.
- **Never guess.** If two sources disagree (the website says one price, an email says another), show both and ask which is right.
- **Add, do not wipe.** New facts get added to the business files. Good context already there stays unless the owner says it is wrong.

## Steps

### Step 1: Ask what to read
Say what this skill does in one line, then ask which sources to use: email, website, files, or all of them. If email is not connected, say so and offer /connect or skip.

For email, also ask:
- How far back to look (default: the last 6 months).
- Anyone or anything off-limits (a person, a topic, a thread they want left alone).

### Step 2: Read the sources

**Email.** Read across the inbox and sent mail inside the agreed window. Focus on threads that carry real business facts: customer work, quotes, prices, deadlines, introductions, decisions. Skip newsletters, receipts, and automated mail. Report roughly how many threads were read and from whom - do not paste them.

**Website.** Fetch their site and its main pages (services, pricing, about, contact). Note what the business says publicly: what it sells, prices shown, the story, the tone, who it serves.

**Files.** Read what is in `my-files (knowledge)/` (or the folder they gave). Pull facts from proposals, price lists, brochures, and guides.

If a source cannot be read (connection broken, site down, folder empty), say so plainly and carry on with the others. Never quietly skip one and act like it was read.

### Step 3: Sort the facts
Group every fact under the file it belongs in:

- Who the business is, its story, its details -> `who-we-are.md`
- What it sells and the prices -> `what-we-sell.md`
- Who the customers and clients are -> `our-clients.md`
- Who is on the team and who does what -> `our-team.md`
- How the business sounds in public -> `how-we-sound.md`

Show the grouped facts as plain bullets. Flag anything that looks out of date, and anywhere two sources disagree. If the website says something different from what is in the brain already, point it out - the owner decides which is true.

### Step 4: Save what the owner confirms
For each file:
1. Add the confirmed facts. Keep what was already there unless the owner said it was wrong.
2. Show what changed in each file, briefly.
3. Fold in corrections without re-explaining.

### Step 5: Close out
Tell the owner in plain words:
- Which files were updated and the headline facts added.
- Anything that looked stale or contradictory, so they can fix it.
- Anything left out because it was unclear.
- What got smarter: "Every reply, quote, and post I draft now knows this."

If their voice profile is not built yet, suggest /learn-my-voice as the natural next step.

## Output format
- Updated files in `my-business (context)/`.
- A short summary in the conversation of what was added and from where.

## Quality check
- Every saved fact was shown to the owner first.
- Nothing was sent, changed, or deleted in any source.
- No full private emails pasted into the conversation.
- Disagreements between sources were surfaced, not silently resolved.
- The business files read better than before, with no good context lost.
