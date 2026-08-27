# Automations

A workflow is anything you do the same way every time. Write it down here and your assistant can run it for you.

## How this folder works

- `specs/` holds workflows you have written down but not yet tested.
- `live/` holds workflows you trust and run regularly.

## How to add one

1. Tell your assistant: "I want to automate something."
2. Describe it in plain English: what starts it, the steps, the result.
3. Your assistant writes it up and saves it in `specs/`.
4. Run it a few times. When it works every time, ask your assistant to move it to `live/`.
5. Want to trigger it by typing a command? Type /teach-me and your assistant turns it into a skill.

## Example

- Name: New enquiry reply
- Starts when: someone fills in the contact form
- Steps: read the enquiry, draft a reply in our tone, suggest a time to talk
- Result: a ready-to-send reply and a calendar suggestion

## Ideas to steal

- Monday morning: pull last week's numbers and brief me (/weekly-check already does this)
- New client signed: create their folder and an onboarding checklist
- End of month: list unpaid invoices and draft the reminders (/chase-payment helps here)
- Before a meeting: pull everything we know about the person I am meeting

Start small. One workflow that runs every week beats five that never get used.
