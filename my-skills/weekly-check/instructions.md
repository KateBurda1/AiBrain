---
name: weekly-check
description: Gives you a quick snapshot of how your week went. Revenue, appointments, what happened. Use when you hear "how did this week go", "weekly check", "weekly summary", "how are we tracking", or "/weekly-check".
---

# Weekly Check

## Goal
Give the business owner a quick, clear snapshot of their week. Numbers, highlights, and anything that needs attention. Under 2 minutes to read.

## Inputs
- None required. Your assistant pulls from connected apps and business files.

## Steps

### Step 1: Gather data from connected tools

If Stripe is connected: pull this week's revenue, transaction count, and compare to last week.

If a calendar is connected (Google or Outlook): count this week's appointments or events. Note any upcoming ones in the next 7 days.

If email is connected (Gmail or Outlook): count unread emails. Flag any that look important or overdue.

If no tools are connected: ask the user for their numbers manually. "How much revenue did you do this week? How many jobs or appointments? Anything notable?"

If a tool is connected but the read fails (sign-in expired, connection broken): say plainly which figure you could not pull and why, and point to /connect. For example: "I could not read Stripe, so this week's revenue is missing. The connection needs a re-authorise, type /connect." Never show a failed read as a 0 or an empty line, and never present missing data as a real number.

### Step 2: Build the snapshot

**Your week at a glance**

Revenue: $X (up/down X% vs last week)
Jobs/appointments: X
New enquiries: X (if email connected)
Unread emails: X
Upcoming this week: [next few events]

**Highlights**
- [Anything notable, positive trends, big jobs]

**Needs attention**
- [Overdue invoices, unanswered enquiries, gaps in the schedule]

**One thing to focus on next week**
- [One actionable suggestion based on the data]

### Step 3: Review
- Are all numbers accurate and pulled from real data?
- Is the "needs attention" section genuinely useful, not just filler?
- Is the suggestion practical and specific?

## Output format
Display the snapshot in the conversation. Short and scannable.

## Quality check
- Takes under 2 minutes to read
- Numbers are real, not estimated
- A broken connection is reported as broken, never shown as a 0 or an empty line
- One clear action for next week
- No fluff
