---
name: quote
description: Turns rough job notes into a professional quote or proposal. Use when you hear "write a quote", "send a quote", "quote for", "proposal for", "price up", or "/quote".
---

# Write a Quote

## Goal
Turn rough notes, job descriptions, or verbal instructions into a clean, professional quote or proposal that the customer can say yes to.

## Inputs
- Who is the quote for? (name, business, contact details if known)
- What is the job or project?
- Any specific requirements, quantities, or scope details?
- Timeline or deadline?

## Steps

### Step 1: Pull context
Read `my-business (context)/what-we-sell.md` for standard pricing and services.
Read `my-business (context)/how-we-sound.md` for tone.
If the client is known, check `my-business (context)/our-clients.md`.

### Step 2: Build the quote
Structure it as:

**Subject line or heading:** Clear description of the work.

**Introduction:** One sentence confirming what was discussed or requested.

**Scope of work:** Bullet list of exactly what is included. Be specific. No ambiguity.

**Pricing:** Line items with costs. Show the total clearly. Include tax (sales tax, VAT, GST) if relevant in your country.

**What is NOT included:** List anything that could be assumed but is not covered. This prevents scope creep.

**Timeline:** When the work would start and finish.

**Validity:** How long the quote is valid for (default: 30 days).

**Next step:** One clear action ("Reply to confirm and we will book you in").

### Step 3: Review
- Is the scope clear enough that there is no room for misunderstanding?
- Does the pricing match what-we-sell.md?
- Is the tone professional but still sounds like the business?
- Is there a clear next step?

## Output format
Display the quote in the conversation for review. If approved, save to the relevant client folder under `my-work (outputs)/clients/`, or `my-work (outputs)/content/other/` if there is no client folder yet.

## Quality check
- Scope is specific and unambiguous
- Pricing is clear with total visible
- Exclusions are listed
- One clear call to action
