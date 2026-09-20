---
name: sort-my-inbox
description: Goes through your unread email, tells you what matters, and drafts replies for the ones waiting on you. Use when you hear "sort my inbox", "check my email", "what's in my inbox", "go through my emails", or "/sort-my-inbox".
---

# Sort My Inbox

## Goal
Clear the mental load of an unread inbox. Read the new mail, sort it into what needs the owner and what does not, and draft a reply for everything waiting on an answer. The owner reads one summary instead of forty emails.

Drafts only. This skill never sends anything. Ever.

## Inputs
- Email connected (Gmail or Outlook). If it is not, say: "I need your email connected for this one. Type /connect and I will walk you through it."
- Optional: a limit ("just today's emails", "last 20").
- If both Gmail and Outlook are connected, ask which inbox to go through, or offer to do both.

**Gmail vs Outlook, one difference.** Gmail lets you save drafts straight into the mailbox. Outlook's connector is read-only, so it can read the inbox but cannot save drafts there. For Outlook, show each reply in chat to paste, or, if Claude in Chrome is installed, offer to type it straight into Outlook on the web. Reading and sorting work the same on both. Sending never happens on either.

## Steps

### Step 1: Read the new mail
Pull unread emails from the inbox. Default to the last 2 days if the user did not say. If there are more than 30, do the most recent 30 and say so in the summary. Never silently skip mail.

If the inbox cannot be read (connection broken, sign-in expired), STOP and say so plainly: "I cannot read your inbox right now, so nothing has been checked. Type /connect to fix the connection." Never present a failed read as an empty inbox.

### Step 2: Sort each email into one of three piles

- **Waiting on you.** A real person needs an answer. A customer enquiry, a question, someone trying to book, a supplier waiting on a decision.
- **Worth a look.** No reply needed but the owner should see it. An invoice received, a notification that matters, an FYI from a real person.
- **Noise.** Newsletters, receipts, marketing, automated notifications. Safe to ignore.

One rule when unsure: if it could be a real person waiting on a reply, it goes in "Waiting on you". A wasted draft costs nothing. A customer left hanging costs real money.

### Step 3: Draft replies for the "Waiting on you" pile
For each one:

1. Read what they actually asked.
2. Pull what you need to answer properly: `my-business (context)/my-voice.md` for how the owner writes (fall back to `how-we-sound.md` if the voice profile is not built yet), `what-we-sell.md` for pricing and services, `our-clients.md` if they are a known client, the calendar if they asked about availability.
   Then match the relationship: search the sent folder for 3-5 past emails the owner wrote to this same person and mirror that register. The owner writes to a long-time client differently than to a stranger, and their own history shows exactly how. No history: use the voice profile's examples.
3. If you can do the legwork the email asks for, do it before drafting. Someone asks for a time: check the calendar and offer a real one. Someone asks for a price: put the real price in. The draft should read like the work is already done, not "I'll get back to you".
4. Draft the reply in the owner's voice. Before saving or showing it, check it against the never-rules in my-voice.md and how-we-sound.md (sign-offs they never use, phrases they hate); if it breaks one, rewrite it once. Then: if the email connection can save drafts (Gmail), save it to their drafts folder. If it is read-only (Outlook), show the draft in chat to paste, or offer to type it into Outlook on the web via Claude in Chrome if that is installed.
5. If an email needs a decision only the owner can make (a discount, a complaint, a contract), do not guess. Put it in the summary as a question with the facts laid out.

### Step 4: Deliver one summary

**Your inbox: X new emails**

**Waiting on you (X)** - for each: who, what they want, and "draft ready in your drafts folder" (Gmail) or "draft below" (Outlook, paste it in) or "needs your call: [the question]".

**Worth a look (X)** - one line each.

**Noise (X)** - just the count, plus "want me to list them?"

Every email read lands in exactly one of the three. None disappear.

## Output format
One summary in chat. Drafts saved to Gmail drafts, or shown in chat to paste (Outlook).

## Quality check
- Nothing was sent. Drafts only.
- Every email is in the summary. Nothing silently dropped.
- Drafts answer the actual question and sound like the owner.
- A broken connection was reported as broken, never as "inbox clear".
