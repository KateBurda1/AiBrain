---
name: hand-off
description: Saves a handoff note of the current work so you can continue it in a fresh conversation without losing anything. Use when a long session is slowing down, when Claude says the conversation is getting long, or when you hear "hand off", "save my place", "continue this later", or "/hand-off".
---

# Hand Off

## Goal
Build one short document that captures everything about the current work, so a brand-new conversation can pick it up and continue as if nothing was interrupted. Long conversations eventually slow down or fill up - this is how you move house without losing the furniture.

## Inputs
- Nothing. The assistant reads back through the current conversation.

## Steps

### Step 1: Read back through the session
Go back through the whole conversation and work out:
- What we are trying to do, and why.
- What has actually been done, versus only talked about.
- Which files were created or changed.
- What was tried that did not work, so the next session does not repeat it.
- What is still open.

### Step 2: Write the handoff note
Use exactly this shape:

```markdown
# Continue: [what the work is, in a few words]

**Date:** [today's date and time]

## The goal
[1-3 sentences. What we are building and why it matters.]

## Where things stand
[Plain facts about what exists right now. If something is half-done, say so.]

## Files involved
[Each file created or changed this session, with one line on what changed.]

## What did not work
[Dead ends tried this session, and why, so they are not repeated. "None" is fine.]

## Still to do
[A numbered list. Done items ticked, open items not.]

## Next step
[ONE concrete action. The first thing the new conversation should do.]
```

### Step 3: Be honest about state
Do not invent progress. If you are not sure something is finished, list it as open. A wrong "done" costs more than an honest "not sure".

### Step 4: Save it and tell the owner how to use it
Save to `my-work (outputs)/internal/handoffs/` with the usual file naming (date first). Create the folder if it does not exist.

Then tell the owner, in plain words: "Saved. Start a new conversation whenever you like and say: read the latest file in my-work (outputs)/internal/handoffs and continue. I will pick up exactly where we left off."

## Output format
- One markdown file in `my-work (outputs)/internal/handoffs/`.
- One line in the conversation telling the owner how to resume.

## Quality check
- The note stands alone: someone with no memory of this session could continue from it.
- Every touched file is listed.
- Nothing is marked done that is not actually done.
- The next step is a single concrete action, not a list.
