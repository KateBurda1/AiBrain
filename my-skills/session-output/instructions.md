---
name: session-output
description: Turns an Advisory/Ignite strategy session into a branded output PPT (decisions, outcomes, next steps) and feeds the right next steps into the Weekly Compass pipeline and the Master Plan backlog. Use at the close of any numbered session (S1-S7), when Janice has been present for a session, or when you hear "session output", "wrap this session", "write up the session", or "/session-output".
---

# Session Output

## Goal
Every Advisory/Ignite strategy session produces three things automatically, not as a separate ask each time:
1. A branded PPT that memorializes what was decided, what got produced, and what's next.
2. This-week action items handed into the existing Weekly Compass pipeline.
3. Later action items captured in the Master Plan so nothing beyond this week gets lost either.

This is the mechanism behind the standing instruction in `my-work (outputs)/internal/2026.08.31 - Internal - Session Handoff for Weekly Compass.md` ("every future session... gets a dated entry appended here") and the 2026.09.20 addition to it (Janice present live in every session). This skill is how that gets executed, not just logged.

## Inputs
- Which session this is (S1, S2, S3A, S3B-i, S3B-ii, S4, S5, S6, or S7) — determines the brand.
- The session's raw discussion: read back through the current conversation (same approach as the `hand-off` skill), or take pasted notes if the session happened elsewhere.
- Today's date, and the session's actual date if different (use the session's real date in the filename, not necessarily today's).
- Attendees.

## Brand rule
- **KB&Co brand:** S1, S2, S5, S6, S7 — the Advisory / Kate & Co-level and operational sessions.
- **Ignite brand:** S3A, S3B-i, S3B-ii, S4 — the Ignite-specific sessions.
If a future session doesn't map cleanly onto this list, ask Kate which brand applies rather than guessing.

## Steps

### Step 1: Read and organize
Same discipline as `meeting-notes`: pull out Decisions, Outcomes/Output, and Next Steps, with an owner on every next step.

### Step 2: Split next steps
For each next step, decide: **this week** or **later**.
- **This week** → goes into the Session Handoff file's running log, same table format already used there (Action | Owner | Category | Note). This is what Janice converts into the actual Weekly Compass on Sunday, which in turn feeds the `weekly-compass-reminders` scheduled skill.
- **Later** → goes into that session's `Actions` checklist in the Master Plan doc (`my-work (outputs)/internal/...Advisory and Ignite Master Plan.md`), using the existing `☐` checkbox pattern already there. Don't create a new tracking file — that doc is already the backlog.
If it's genuinely unclear which bucket an item belongs in, ask Kate rather than guessing — a mis-bucketed item either nags her this week for no reason or actually gets lost.

### Step 3: Generate the PPT
Use `my-workflows (automations)/live/session_output_deck.py`'s `build_deck()` function. Four slides: Title, Decisions, Outcomes, Next Steps (two columns: This Week / Later). Brand values and font substitutes are already defined in that script, sourced from `my-business (context)/brand-standards.md` and `ignite-brand-standards.md` — don't redefine them elsewhere or hand-roll a new template; extend that script if the template itself needs to change.

Save into that session's own subfolder of `my-work (outputs)/internal/`, one folder per session (standing convention since 2026.09.20 — all session outputs live under their session, not flat in `internal/`):
```
my-work (outputs)/internal/Session <N> - <Session Name>/yyyy.mm.dd - Internal - Session <N> <Session Name> - Outputs.pptx
```
Create the folder if it doesn't exist yet. Use the session's real date in the filename. Any other artifact from that session (a spreadsheet, a working doc) goes in the same folder, not scattered elsewhere.

### Step 4: File the next steps
- Append this-week items to the Session Handoff file, following its existing table format, under a new dated section header for this session.
- Append later items to the Master Plan's Actions checklist for this session.
Read both files back afterward to confirm the append landed cleanly and didn't duplicate anything already there.

### Step 5: Report back
Tell Kate what was assumed (this-week vs. later calls that weren't explicit, brand choice if it wasn't obvious) per CLAUDE.md's "make reasonable assumptions and report what was assumed" rule. Point to the PPT's file path.

## Output format
- The PPTX file, saved as above.
- A short chat summary: what got decided, what's due this week vs. later, and where each landed (Session Handoff / Master Plan).

## Quality check
- Every next step has an owner and a clear this-week/later bucket.
- Brand matches the session per the rule above.
- No duplicate entries in the Session Handoff file or Master Plan checklist.
- PPT file name and date follow the existing internal-docs naming convention.
