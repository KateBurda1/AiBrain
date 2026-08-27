Load the business context and brief the user.

## First-run check

Before reading anything else, open `my-business (context)/who-we-are.md`. If the content still contains template placeholders in square brackets (e.g. `[Your business name]`, `[Describe what your business does...]`), the user has not run /setup yet.

In that case, skip the briefing and say:

"Welcome. Looks like your assistant has not been set up yet. Type /setup and I will get you set up in about 20 to 25 minutes. You only do this once."

Then stop. Do not run the rest of /prime.

## Normal briefing

If /setup has been completed, do the following:

1. Read `CLAUDE.md`.
2. Read `SAFETY.md`. These rules govern everything you do this session.
3. Read every file in `my-business (context)/`.
4. Read `my-connections (MCP)/connected-apps.md` to see what apps are connected.

Then return a short briefing (under 200 words):

- **Who you are:** business name, what you do, where you are based
- **What you sell:** one-line summary from what-we-sell.md
- **Connected apps:** list the ones that are live (or say "none yet, type /connect when you are ready")
- **Skills available:** list the built-in skills by category (Your day, Sales, Operations, Marketing, Team, System) plus any custom skills in `my-skills/`

If email is connected (Gmail or Outlook) but `my-voice.md` still has square-bracket placeholders, add one line: "Tip: type /learn-my-voice and your drafts will start sounding like you."

**Freshness check.** While reading the business files, notice anything that looks stale: a file that has not changed in a couple of months, a "current" client list that contradicts recent email, prices that differ from the website. If something looks out of date, add one line to the briefing: "Heads up: [file] looks out of date ([reason]). Type /fill-my-brain and I will refresh it from your real email and website." Maximum one such line per briefing - flag the most important, not all of them.

End with: "Ready. What do you want to work on?"
