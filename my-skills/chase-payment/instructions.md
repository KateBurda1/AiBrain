---
name: chase-payment
description: Writes a friendly but firm payment reminder for overdue invoices. Use when you hear "chase payment", "overdue invoice", "they haven't paid", "payment reminder", "chase [name]", or "/chase-payment".
---

# Chase a Payment

## Goal
Write a payment reminder that is warm enough to keep the relationship but firm enough to get paid. Remove the awkwardness so the business owner actually sends it.

## Inputs
- Who owes the money?
- How much?
- How long overdue?
- Invoice number or reference (if known)?
- Any context (good customer having a rough patch, serial late payer, etc.)?

## Steps

### Step 1: Pull context
Read `my-business (context)/my-voice.md` for how the owner actually writes. If it still has square-bracket placeholders, use `my-business (context)/how-we-sound.md` instead.
If known client, check `my-business (context)/our-clients.md`.

### Step 2: Choose the right tone

**First reminder (1-7 days overdue):** Assume it was forgotten. Light and casual. "Just a heads up that invoice #X is outstanding."

**Second reminder (7-14 days overdue):** Slightly firmer but still friendly. "Wanted to follow up on this one."

**Third reminder (14-30 days overdue):** Direct. State the amount, the date it was due, and ask for a specific payment date. "Can you let me know when I can expect this to be sorted?"

**Seriously overdue (30+ days):** Professional and firm. Mention next steps without threatening. "I need to get this resolved. Please let me know your plan for payment by [date]."

### Step 3: Write the message
- Subject line: include the invoice number or amount. "Invoice #1234 - $340 outstanding"
- Opening: friendly but direct. Get to the point immediately.
- Body: state the amount, the due date, and how long overdue. Keep it factual.
- Close: ask for a specific action. "Can you sort this by Friday?" is better than "Please pay at your earliest convenience."
- Keep it under 80 words. Short messages get faster responses.

### Step 4: Review
- Is it firm enough to get paid?
- Is it warm enough to keep the relationship?
- Is there a specific ask (date or action)?
- No passive-aggressive tone?

## Output format
Display the message for review. The user copies and sends it themselves.

## Quality check
- Under 80 words
- States the amount and how long overdue
- Has a specific ask (not "at your earliest convenience")
- Firm but not hostile
