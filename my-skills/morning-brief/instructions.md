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

### Step 2: ZoomInfo cadence reply check (Kate, 2026.09.29 — Session 6 sign-off)
Real replies from ZoomInfo cadence contacts need to land in Zoho as Deal records, so the 11/9 evaluation checkpoint (Session 6 Tech Stack Review, `my-work (outputs)/internal/Session 6 - Tech Stack Review/2026.09.23 - Internal - Session 6 Tech Stack Review - Outputs.md`) has real data instead of another zero. Jack owns creating those Deal records but only runs when invoked — there is no other standing process re-checking the inbox on its own, so this step is that check, every weekday morning.

1. **Know which cadences are actually live.** Open `my-work (outputs)/internal/2026.09.28 - Internal - Cadence Turn-On Tracker.xlsx` (the same file used in the cadence turn-on check below) and see which topics are switched on and sending. As of 2026.09.29 that's ABM only (70 tagged contacts). Add Business Transformation (324 contacts) once it switches on 10/6, and Sales Intelligence (50 contacts) once it switches on 10/8 — extend the check automatically the day each one goes live, no separate instruction needed. Never check a cadence that has not switched on: no sends yet means no genuine reply is possible yet.
2. **Pull the enrolled contact list from Zoho CRM** for each live cadence. Use `executeCOQLQuery` (the Zoho MCP tools are prefixed `mcp__bb06c58e-629d-4fff-a006-c30be8ba1af8__`; load with ToolSearch first if deferred — the working call shape is `{"body": {"select_query": "..."}}`). **Verified 2026.09.29 directly against live Zoho, correcting an earlier wrong guess: there is no `ZI - [Topic]` prefix.** The `ZI_Intent_Topic` field on Contacts is a plain semicolon-delimited multi-select — filter with `select Email, First_Name, Last_Name, Account_Name from Contacts where ZI_Intent_Topic like '%Business Transformation%'` (swap in `%ABM%`... actually ABM's field is `ZI Workflow Source` not `ZI Intent Topic`, see the project memory for that distinction — or `%Sales Intelligence%`, matching plain text, no special prefix). For reference, the matching Zoho Custom Views (cosmetic, not required for the COQL query itself) are named **"Business Transformation Auto-Enroll ZI Intent Topic"** and **"Sales Intelligence Contacts"** — note Sales Intelligence does NOT have a separately-named "Auto-Enroll" view the way Business Transformation and Market Expansion do; its live cadence is bound directly to "Sales Intelligence Contacts." If Zoho cannot be reached, say so plainly in the brief ("Zoho CRM connection is down, cadence reply check not run today") rather than reporting a quiet result.
3. **Cross-check against this morning's inbox sort** (Step 1's "Waiting on you" and "Worth a look" piles — Noise is already excluded). Find any sender whose email address matches an enrolled contact. A genuine reply is a real message from that person: never a bounce or delivery-failure notice, an out-of-office or automatic reply, or a newsletter, even if one of those slipped into "Worth a look." If a match is ambiguous, say so in the brief instead of guessing either way.
4. **Hand each genuine match to Jack, do not log it yourself.** Creating the Deal record is Jack's lane, same division of labor Kate confirmed 9/29 (Jack logs a Deal at "Contacted" on any genuine reply, escalating the stage himself as it progresses). Call Jack with the contact's name, company, which cadence they're on, and the email itself, and ask him to log the Deal.
5. **Surface every match plainly in the brief**, not just a silent backend log: who replied, which cadence, and what happened ("logged as a Deal at Contacted in Zoho" or "flagged to Jack, log not yet confirmed"). Put the first genuine reply on a newly-live cadence in **Top 3**; later ones can sit in **Loose ends**. If nothing came in from a cadence contact today, say so in one plain line ("No ZoomInfo cadence replies today") rather than staying silent or padding — this is tracking toward a hard checkpoint, so a null result is itself worth stating.

### Step 3: Check the calendar
If a calendar is connected (Google or Outlook):
- Today's events in order, with times.
- Flag anything unusual: an early start, a double-booking, a meeting with no location or link.
- Look at tomorrow morning too, so nothing ambushes them at 8am.

### Step 4: Check for loose ends
Scan for things that slipped:
- Emails in "Waiting on you" older than 2 days.
- Anything the owner said they would do in a recent sent email ("I'll send that over Friday") that has not gone out. Only flag clear, concrete commitments. Never invent a task.
- If Stripe is connected: any payment that looks overdue.
- Run the `wylie-rm-prep` skill (read `my-skills/wylie-rm-prep/instructions.md`
  and follow it) to check whether tomorrow's calendar has the Wylie RM call.
  It stays silent if there's no match; fold its reminder into loose ends if
  there is one.
- Check `my-work (outputs)/internal/flagged-priorities.md` for any **Open**
  entry dated today. These are one-off flags someone deliberately set for
  this exact date (a dependency to check before a post goes out, a
  time-sensitive action), not generated from the calendar or inbox, so
  nothing else will surface them if this step is skipped. If today's date
  has an open entry, it goes in **Top 3** below, not buried in loose ends,
  with its full detail (assets, links, and especially any dependency called
  out in the entry). Don't mark it Done yourself — that only happens when
  Kate confirms it. If nothing matches today's date, stay silent, don't pad
  the brief.
- **Cadence turn-on check (Kate, 2026.09.28).** Open
  `my-work (outputs)/internal/2026.09.28 - Internal - Cadence Turn-On Tracker.xlsx`
  and compare it with where Kate really is, using the latest Weekly Compass
  (that's how you know whether she's on track or behind on building touches).
  The rule: a cadence sends a touch every 7 days, so Touch N reaches the first
  contact 7 x (N-1) days after it's switched on. A cadence is safe to switch
  on only if every unbuilt touch will be built at least 2 days before the
  first contact could reach it, and every unbuilt touch holds holding copy
  (never old copy).
  - Kate decides when anything switches on, and nothing goes out until it's
    built (Kate, 2026.09.28). When a topic reaches its "Earliest safe" date
    and its "Before you switch on" list is done, say so once in the brief:
    "[topic] could go on now. Your call." Never switch anything on yourself.
  - If Kate has slipped, move the earliest-safe date out, update the tracker, and say so in one line.
  - **Target switch-on dates (Kate, 2026.09.29).** The tracker's "Target
    switch-on (Kate)" column holds the dates Kate set (Business Transformation
    Tue 10/6, Sales Intelligence Thu 10/8). The "Switch-On Checklist" tab lists
    every item that must be Done first. Kate asked Janice to watch how far she
    gets and move the date if the list isn't done:
    - Every morning before a target: one line per topic with how many items
      are still open, naming them only in the last 3 days before the target.
    - On the target morning, if every item is Done: "[topic] is ready to
      switch on today. Your call." Never switch it on yourself.
    - On the target morning, if anything is still open: move the target out
      one week (never earlier than Earliest safe), write the new date in the
      tracker with "(moved from X)", and say it in one line with what's open.
    - Pages and posts for a topic go live keyed to its real switch-on day,
      never on a fixed date of their own.
  - If a cadence is already switched on and the next unbuilt touch is less
    than 2 days from its first send, that's urgent: **Top 3**, with the touch
    and the date it sends.
  - Before a topic is called ready, check its Zoho templates for
    "[PLACEHOLDER]". On 9/28, Site Visit Targeting sent a placeholder to 150
    contacts because nobody checked.
  - Stay silent on days when none of this applies.
- **Booking catch (Kate, 2026.09.29, updated 2026.10.01).** Calendly is
  gone. Bookings come through Zoho Bookings. **Fixed and verified 10/1,
  3:30 PM:** a booking now creates a Meeting on the contact in Zoho CRM,
  and the "Booking - Stop Cadences" workflow ticks Meeting Booked a second
  later, which un-enrolls them from every live cadence. Your job is now a
  safety check only: for each new booking found in step 1, confirm the
  contact's `Meeting_Booked` is true. If it is, just list the booking. If
  it isn't, the sync has broken again, so do steps 2 and 3 and flag "Zoho
  Bookings to CRM sync broke" in Top 3. The original fallback steps:
  1. Search Kate's Outlook calendar for events titled **"20 minutes with
     Kate & Co. with [Name]"** created since the last brief. Zoho Bookings
     sends Kate no email, so check the calendar, not the inbox. Use the
     attendee's email address.
  2. Look that email up in Zoho CRM Contacts. If the contact exists and
     `Meeting_Booked` isn't already true, **set `Meeting_Booked` = true**
     (Kate approved this on 10/1). Every live cadence (ABM, ABM Auto-Enroll,
     Sales Intelligence Auto-Enroll, Business Transformation Auto-Enroll
     Live) un-enrolls anyone with Meeting Booked ticked, so this is what
     stops the emails. Don't touch the cadences directly.
  3. Put it in **Top 3**: "[Name] at [Company] booked [day/time]. Ticked
     Meeting Booked, so they're out of [cadence]." If the email isn't a
     Zoho contact, just list the booking.
  4. Skip Kate's own test bookings (kate@kateburda.com, kateburda@aol.com).
  Retire this check once a real booking shows up in Zoho CRM as a meeting on
  the contact with Meeting Booked ticked by the "Booking - Stop Cadences"
  workflow rule.

### Step 5: Deliver the brief

**Good morning. Here is your day.**

**Top 3** - the three things that matter most today, sharpest first. A meeting to prep for, a customer waiting two days, an invoice to chase, a flagged priority from `flagged-priorities.md` dated today, or the first genuine ZoomInfo cadence reply from step 2. If fewer than three things genuinely matter, list fewer. Never pad.

**Today's calendar** - events in order. One line each.

**Inbox** - the sort-my-inbox summary: waiting on you (drafts ready), worth a look, noise count.

**ZoomInfo cadence replies** - one line per genuine reply found in step 2 (who, which cadence, what happened with Jack and Zoho), or "No ZoomInfo cadence replies today."

**Loose ends** - anything from step 4, with a suggested next move for each.

In the Inbox section, include a one-line **Drafts status**: "X drafts saved to [Gmail/Outlook], Y shown in the brief because the save failed." Before sorting the inbox, confirm the draft-save tool is actually available (for Outlook, `outlook_create_reply_draft`; load it with ToolSearch if it is deferred). If it is missing, say so at the top of the brief and write every draft out in full.

End with the line that is true for this run:
- **All drafts saved, Gmail:** "Drafts are in your Gmail drafts folder, ready to review and send. What do you want to tackle first?"
- **All drafts saved, Outlook:** "Drafts are in your Outlook Drafts folder, ready to review and send. What do you want to tackle first?"
- **Any save failed:** "Draft saving failed for [which ones]. The full text is above to paste. What do you want to tackle first?"

### If something is broken
If any app cannot be read, the brief says which section is missing and why: "Calendar section missing, the connection needs a re-authorise, type /connect." A broken tool is never reported as a quiet day.

## Output format
One brief in chat. Replies handled by the sort-my-inbox skill: saved to the Gmail or Outlook drafts folder.

## Quality check
- Reads in under five minutes.
- Top 3 is genuinely the top 3, not a dump of everything.
- Nothing was sent anywhere. Drafts only.
- Broken connections reported, not papered over.

## Tip for the user
This works best as a habit: same time, every morning, one command. If you want it fully automatic, ask your assistant about scheduled tasks. Depending on your Claude plan, it may be able to run this on a timer and have the brief waiting for you.
