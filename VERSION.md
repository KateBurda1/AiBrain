# Version

```
version: 2.0.1
released: 2026-08-14
```

---

## What's new

### v2.0.1 (August 2026)

- **SAFETY.md: connecting tools that need an API key now has a safe, explicit routine.** Your assistant opens a blank Desktop file, you paste the key and save, it moves the key into your computer's own settings, tests it, and deletes the file. The key never appears in the chat and never lives in a brain file.
- **SAFETY.md: the never-sends rule is now written as a rule, not a description of today's connectors** — if an email connection ever gains the power to send, nothing changes: things go out only after you approve them.

### v2.0 (August 2026)

- **/fill-my-brain.** Your assistant fills in your business files by reading your real email, your website, and your documents, instead of you typing everything in. Read-only, and you approve every fact before it is saved. The fastest way to a smart assistant, and the fix any time your files go stale.
- **/plan.** Give your assistant a goal too big for one skill ("get more bookings this month") and it plans the steps, shows you the plan, then runs your skills and agents to get it done. Anything that would send, post, or pay is prepared and held for you.
- **/hand-off.** Long conversations eventually slow down. This saves your place in one note so a fresh conversation picks up exactly where you left off.
- **Drafts that match the relationship.** Before drafting a reply, your assistant now reads a few of your past emails to that same person and matches how you actually write to them. You write to a long-time client differently than to a stranger, and now so does it. It also checks every draft against your "never" rules (sign-offs you never use, phrases you hate) before showing it.
- **A fresher brain.** /prime now flags business files that look out of date and offers to refresh them with /fill-my-brain. And /setup offers to mine your inbox for facts right after you connect your email.
- **Stronger rulebook.** SAFETY.md now spells out that your assistant never bends its own rules to make a job easier, and reports loopholes instead of using them.

### v1.3.1 (July 2026)

- **A setup video.** The Start Here guide now links a short video walking through the folder step, the one part worth getting right.

### v1.3 (July 2026)

- **Your agents can use your connected apps.** Fixed a bug that stopped the named agents reaching Gmail, Calendar and Drive once you had connected them. Ask Ada for your morning brief and she can actually read your inbox now.
- **Outlook and Microsoft 365.** Setup now walks you through the Microsoft 365 connector as well as Gmail.
- **Clearer Windows setup.** The guide now covers installing Git on Windows, which is what caused the red "Git is required" box for some people.
- **A tidier download.** The kit is now just your `My AI Brain` folder plus the Start Here guide. Nothing else to sort through.

### v1.2 (June 2026)

- **Your agent team, ready to go.** Eight named agents now ship built in, generic and ready to work for any business. Call any of them by name:
  - **Ada** - your assistant and right hand (inbox, calendar, the morning brief)
  - **Leo** - your writer (posts, long-form, in your voice)
  - **Maya** - your marketer (ads, offers, funnels, image prompts)
  - **Sage** - your community voice
  - **Scout** - your researcher
  - **Finn** - your numbers
  - **Pete** - your outreach
  - **Nova** - your builder (tools, dashboards, simple automations)

### v1.1 (June 2026)

- **/learn-my-voice.** Your assistant reads a sample of your real sent emails (read-only) and learns how you actually write. Every draft after that sounds like you, not like AI.
- **/sort-my-inbox.** Goes through your unread email, tells you what matters, and drafts replies for everyone waiting on you. Drafts only. You send.
- **/morning-brief.** One command with your first coffee: inbox sorted, calendar checked, replies drafted, and the three things that matter most today.
- **SAFETY.md.** The plain-English rulebook for what your assistant does on its own and what always stays with you.
- **Bring your context with you.** Already use ChatGPT? /setup can now import what you have already taught it about your business.
- **This file**, so you always know which version you are on.

### v1.0 (May 2026)

The original kit: ten skills, five agents, /setup onboarding, connected apps, /teach-me, /wrap.

---

## Updating to a newer version

Your business files are the valuable part. They are yours and a new version never replaces them. The skills and system files are ours, and updates make them better. So the rule is simple: keep your files, swap the system.

When a new version comes out:

1. **Keep these. Do not overwrite them.**
   - Everything in `my-business (context)/`
   - Everything in `my-files (knowledge)/` and `my-work (outputs)/`
   - Everything in `my-workflows (automations)/`
   - `my-connections (MCP)/connected-apps.md`
   - Any skills you created with /teach-me
   - Your own rules at the bottom of `SAFETY.md`

2. **Replace these with the new version's copies.**
   - The built-in skills in `my-skills/`
   - The `.claude/` folder
   - `CLAUDE.md`, `SAFETY.md`, `VERSION.md`
   - (Your business name and brand details get written back into the new `CLAUDE.md` from your business files. Your assistant does this as part of the update.)

3. **The easy way:** download the new kit next to your current folder, then ask your assistant: "Update me to the new version, keep my business files." It knows this list and does the swap for you.

   One exception: your assistant is not allowed to edit `SAFETY.md` (that file is yours alone, by design). So if you added your own rules at the bottom, it will show them to you and you paste them into the new `SAFETY.md` yourself. Thirty seconds.

4. **Afterwards**, your assistant re-reads everything and tells you what is new.

If anything goes wrong, your old folder is still there untouched until you delete it yourself.
