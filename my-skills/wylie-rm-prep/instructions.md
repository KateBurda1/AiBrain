---
name: wylie-rm-prep
description: Checks whether tomorrow's calendar has the Wylie Inn Revenue Management call, and if so, reminds Kate to pull the four source files and run the weekly report. Called from morning-brief, not run standalone.
---

# Wylie RM Call Prep

## Why this exists
The Wylie Inn Revenue Management call is booked individually each week (no
standing recurring meeting, per Kate — scheduling varies with the client), so
there's no fixed day to hang a reminder on. Kate preps the report the day
before the call. This skill makes that prep show up in the morning brief the
morning before, whatever day that turns out to be.

## Steps

1. Search Kate's calendar for events matching "Wylie" and "RM" (subject
   pattern seen historically: `RM- Wylie`) landing **tomorrow**.
2. If nothing matches, this skill contributes nothing to the brief — stay
   silent, don't pad the brief with a non-event.
3. If a match is found, add a line to the brief's **Loose ends** section:
   - The call's time tomorrow.
   - The four files to pull before it:
     1. CoStar/STR — Weekly STAR Report (manual download)
     2. Lighthouse — Rates export (.xlsx, Next 90 days covers enough range)
     3. Booking.com — Sales statistics → Print → Save as PDF
     4. Synxis — Reports → Inventory (Download) → Generate Report → View
        Reports → Download (ignore the misleading Start/End Date columns in
        that table; the CSV's own footer has the real range)
   - The command to run once the four files are downloaded:
     ```
     python3 "my-workflows (automations)/live/wylie_weekly_revenue_report.py" \
       --str <STR file> --lighthouse <Lighthouse file> \
       --booking-pdf <Booking.com PDF> --synxis-csv <Synxis CSV> \
       --out "my-work (outputs)/clients/wylie-inn/02 - Deliverables/<date> - Wylie Inn - Weekly Revenue Report.docx"
     ```
   - Offer to run the script herself if Kate hands over the four files instead
     of running it herself.

## Notes
- Full source detail and the "why" behind each step lives in the automation
  spec: `my-workflows (automations)/specs/2026.09.02 - Wylie Inn - Weekly
  Revenue Report Automation Spec.md`.
- Expedia has no automatable source (confirmed no export on the two screens
  Kate checks) — the report's Expedia section is a manual-entry table, filled
  in from Expedia Partner Central directly, not part of this prep step.
- If Kate is traveling or out, this reminder still fires — she said she'll
  pull the files herself regardless of where she is.
