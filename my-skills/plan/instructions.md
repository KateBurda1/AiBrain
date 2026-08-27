---
name: plan
description: Give your assistant a goal too big for one skill ("get more bookings this month", "onboard this new client properly") and it plans the steps, shows you the plan, then runs your skills and agents to get it done. Use when you hear "help me plan", "I need to sort out", "we need more", or "/plan".
---

# Plan

## Goal
Take a business goal in plain words, work out what is really being asked, build a plan from the skills and agents this assistant actually has, show the owner the plan, then run it to a finished result. This is the skill that runs the other skills.

Use it when a request needs several steps. If the ask is one clear task ("write a post about our sale"), just run that skill instead - do not bring out the project manager for a single job.

## Inputs
- A goal or problem in one or two sentences. That is enough. The assistant finds the rest.

## Steps

### Phase 1: Understand the goal
Most of the effort goes here. A goal that is well understood is easy to plan.

1. **Say it back.** Work out what is really being asked and the goal behind it. Say it back in one line so the owner can confirm. "More sign-ups for the launch" might really mean "fill the 12 spots by the 20th".
2. **Read what the brain knows.** Read the business files the goal touches: who-we-are, what-we-sell, our-clients, plus the calendar, recent email, and connected apps if the goal involves real people or dates.
3. **Sketch two or three ways to get there,** with the trade-off of each in one line. Pick the one most likely to work. If it is genuinely a taste call (brand, tone, a big bet), give the owner the options and let them pick - taste is theirs, not the assistant's.

### Phase 2: Build the plan
4. **Break the chosen approach into jobs.** Map every job to a real skill in `my-skills/` or a real agent (Janice, Maya, Maxell, Steph, Scout, Finn, Jack, Shelby). Never invent a capability. If a job needs a skill that does not exist yet, say so - that is a /teach-me moment, not something to improvise.
5. **Put the jobs in order** and note what each one produces, so it is clear later whether it worked.
6. **Check your own plan before showing it.** Read it back looking for holes: missing steps, wrong order, jobs that do not actually move the goal. Fix what you find. A weak plan is not shown.
7. **Show the plan and wait for a yes.** Keep it short: the goal, the jobs, who does each, what the owner will need to decide or send at the end. Small, safe jobs inside the workspace can just be done - but any plan with more than a couple of steps gets shown first.

### Phase 3: Run it
8. **Run each job in order** using the real skill or agent. Follow SAFETY.md the whole way: work inside the workspace runs freely; anything that would send, post, pay, or commit gets prepared and held for the owner. The hold is on sending, not building - draft the client-facing thing fully, then park it for approval.
9. **Check each job's result** against what it was meant to produce. If it fell short, rework that piece before moving on. Never show half-finished work as done.

### Phase 4: Close out
10. **No loose ends.** Every job is finished and checked, or clearly parked with the owner with what they need to act. If something is still open, it is not done - go back and finish it.
11. **Report.** What got done and where it lives, then the short list of things only the owner can do: send this, decide that, approve the other. Sharpest first.
12. **Save what worked.** If the plan worked, note the recipe (goal, jobs, order) in `my-work (outputs)/internal/playbooks/` so the same kind of goal is faster next time. Only save plans that actually worked.

## Rules
- Spend the most effort understanding the goal. Do not start breaking it into jobs before it is confirmed.
- Only plan with skills and agents that exist. A missing skill is flagged, never faked.
- Never shrink the goal to be cautious. Build everything up to the line; hold only the send, the payment, the commitment.
- The owner decides taste. The assistant can check its own work for correctness, not for style.
- Done means the real result exists. "I ran the steps" is not done.

## Output format
- The plan, shown for approval.
- The finished work, saved in the right `my-work (outputs)/` folders.
- A closing report: done list, then needs-you list.

## Quality check
- Goal was said back and confirmed before planning.
- Every job mapped to a real skill or agent.
- Plan was self-checked before being shown.
- Nothing was sent, posted, or paid by the assistant.
- Every job is either done and checked, or parked with the owner with a clear next step.
