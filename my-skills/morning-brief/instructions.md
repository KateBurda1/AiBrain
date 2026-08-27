---
name: morning-brief
description: Preps your whole day in one go. Sorts your inbox, checks your calendar, and tells you the three things that matter most. Use when you hear "morning brief", "what's on today", "prep my day", "start my day", or "/morning-brief".
---

# Morning Brief

## Goal
The owner types one command with their first coffee and gets their day handed to them: what came in overnight, what is on the calendar, replies already drafted, and the short list of things that actually need them. Five minutes of reading replaces an hour of inbox-and-calendar shuffling.

## Inputs
- None. The assistant pulls everything from connected apps.
- Works with whatever is connected, Gmail or Outlook for email, Google or Outlook for calendar. Email only? Inbox section only. Nothing connected? Say so and offer /connect.

## Steps

### Step 1: Sort the inbox
Run the `sort-my-inbox` skill (read `my-skills/sort-my-inbox/instructions.md` and follow it). Do not rewrite its logic here. One skill does email; this brief uses it.

Hold the result for the brief instead of presenting it separately.

### Step 2: Check the calendar
If a calendar is connected (Google or Outlook):
- Today's events in order, with times.
- Flag anything unusual: an early start, a double-booking, a meeting with no location or link.
- Look at tomorrow morning too, so nothing ambushes them at 8am.

### Step 3: Check for loose ends
Scan for things that slipped:
- Emails in "Waiting on you" older than 2 days.
- Anything the owner said they would do in a recent sent email ("I'll send that over Friday") that has not gone out. Only flag clear, concrete commitments. Never invent a task.
- If Stripe is connected: any payment that looks overdue.

### Step 4: Deliver the brief

**Good morning. Here is your day.**

**Top 3** - the three things that matter most today, sharpest first. A meeting to prep for, a customer waiting two days, an invoice to chase. If fewer than three things genuinely matter, list fewer. Never pad.

**Today's calendar** - events in order. One line each.

**Inbox** - the sort-my-inbox summary: waiting on you (drafts ready), worth a look, noise count.

**Loose ends** - anything from step 3, with a suggested next move for each.

End with the right line for how their email is connected:
- **Gmail:** "Drafts are in your Gmail drafts folder, ready to review and send. What do you want to tackle first?"
- **Outlook (read-only connector):** "Your replies are drafted below for you to paste into Outlook (or I can type them straight in for you if you have Claude in Chrome). What do you want to tackle first?"

### If something is broken
If any app cannot be read, the brief says which section is missing and why: "Calendar section missing, the connection needs a re-authorise, type /connect." A broken tool is never reported as a quiet day.

## Output format
One brief in chat. Replies handled by the sort-my-inbox skill: saved to the Gmail drafts folder, or shown in chat to paste (Outlook).

## Quality check
- Reads in under five minutes.
- Top 3 is genuinely the top 3, not a dump of everything.
- Nothing was sent anywhere. Drafts only.
- Broken connections reported, not papered over.

## Tip for the user
This works best as a habit: same time, every morning, one command. If you want it fully automatic, ask your assistant about scheduled tasks. Depending on your Claude plan, it may be able to run this on a timer and have the brief waiting for you.
