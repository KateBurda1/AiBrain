Walk the user through connecting apps to Claude Code. This can be run any time.

## Before starting

Check `my-connections (MCP)/connected-apps.md` for what is already connected. If something is listed there, ask: "Looks like [app] is already connected. Want me to test it is still working?" Try a small action to confirm (e.g. list recent emails). If it works, say so. If it errors, walk through reconnecting.

## How connections actually work

Be honest with the user about the steps. Connections are managed inside the Claude Code desktop app itself, not by typing magic words in chat. Your job is to guide them through the app's settings panel.

Say: "Connections live in the Claude Code app's settings, not in our chat. I will tell you what to click. Each one takes about 30 seconds. A sign-in window pops up in your browser, you click Authorise, and you are done. Skip anything you do not use."

## Core apps (one-click, no technical setup)

These are your email, calendar, and files. They connect without any technical setup. The Tier 2 and Tier 3 apps further down can be added too, whenever the user wants them.

### First, find out which side they are on

Ask: "Quick one: does your business run on **Google** (Gmail, Google Calendar, Google Drive) or **Microsoft** (Outlook, OneDrive)? Whichever you use for your work email is the one to connect."

Connect whichever side they use. Most businesses run on one, but if they genuinely use both Gmail and Outlook you can connect both, just run the same steps for each. The connect steps are identical: open the Claude app's settings, find Connectors, click Add next to the one you want, a sign-in window opens, sign in with your BUSINESS email, click Authorise, come back and tell me. If both end up connected, when they ask you to check or sort email and it is not obvious which inbox they mean, ask.

### If they use Google

Walk through these one at a time:

1. **Gmail.** "Open the Claude app's settings, find Connectors, click Add next to Gmail, sign in with your business email, click Authorise. Tell me when it's done." When they confirm, list recent emails to verify.
2. **Google Calendar.** Same flow. List today's events to verify.
3. **Google Drive.** Same flow. Search for a file to verify.

Record each success in `my-connections (MCP)/connected-apps.md`.

### If they use Microsoft (Outlook)

There is **one** Microsoft connector that covers email, calendar, and files together.

1. "Open the Claude app's settings, find Connectors, click Add next to **Microsoft 365**, sign in with your business Outlook email, click Authorise. Tell me when it's done."
2. When they confirm, list recent emails to verify, then list today's events.

Record success in `my-connections (MCP)/connected-apps.md`.

**Be honest about how Outlook works**, so nothing surprises them later. Say: "Two things to know about Outlook. First, Microsoft's connection is read-only, so I can read your inbox and calendar but I can't drop drafts into Outlook the way I can with Gmail. When I write you a reply, I'll show it here for you to paste, or if you've got Claude in Chrome I can type it straight into Outlook for you. Same result, just one extra step. Second, I never send. You always send."

Two things that can trip up the Outlook connect, handle them if they come up:
- **"It says an administrator needs to approve this."** A Microsoft 365 business account sometimes needs a one-time approval from whoever manages your Microsoft 365. For a lot of small businesses that is you, signed in as the owner. If someone else manages your Microsoft, they approve it once and then you connect normally. If that is a dead end for now, say: "No drama, we'll use Claude in Chrome on Outlook on the web instead, it does the same job with zero setup."
- **A personal account** (@outlook.com, @hotmail.com, @live.com). The Microsoft 365 connector is built for business/work accounts. For a personal Outlook, skip the connector and use **Claude in Chrome** on outlook.live.com instead. Offer to set that up.

### Claude in Chrome (browser extension)

Ask: "Do you want to install Claude in Chrome? It is a browser extension that lets me read and click inside websites for you. Means I can help with Canva, Stripe, Xero, your CRM, or anything web-based even if we do not have a direct connection for it yet."

If the user connected **Outlook**, flag this as extra useful: "For you on Outlook this is worth it. Microsoft's connection only lets me read. With Claude in Chrome I can type drafts straight into Outlook on the web and tidy your inbox there, which the read-only connection can't do."

If yes, walk them through:
1. "Open Chrome."
2. "Go to the Chrome Web Store and search for **Claude in Chrome**."
3. "Click **Add to Chrome**."
4. "Sign in with your Claude account when it prompts you."
5. "Come back and tell me when it is installed."

Once confirmed, record it in `my-connections (MCP)/connected-apps.md` as installed. You do not need to test it. Once the extension is signed in, it is ready.

## Tier 2: one-click inside the Claude app

If the user asks about Slack, Stripe, Canva, Webflow, Notion, GitHub, or any other Anthropic-supported connector:

Say: "That one is already available inside the Claude desktop app's connector menu. Want me to walk you through adding it? It's the same flow as Gmail: open the Claude app's settings, find the Connectors section, click Add next to [app], sign in, authorise. Takes 30 seconds."

Then walk them through it. After they confirm, record it in `my-connections (MCP)/connected-apps.md`.

## Tier 3: advanced setups (you walk them through)

If the user asks about Meta Ads, Xero, MYOB, HubSpot, Salesforce, or another tool not in the Claude connector menu:

Say: "That one needs a small one-off setup, an MCP config. Possible, just not one-click. I can walk you through it now if you want. We'll need an API key from [tool] and a few minutes. Worst case, you can always paste the data into chat and I'll work with it."

If the user says yes, you (the assistant) walk them through the MCP setup directly. Look up the tool's MCP server (search the MCP registry or the tool's docs), explain what to install, where to get the API key, and how to add it to the Claude desktop app's MCP config. Be patient. Confirm each step before moving on.

If it gets stuck or the user gets frustrated, fall back to: "Let's pause this and use the paste-into-chat method for now. Whenever you want to try the proper connection again, just ask."

## When a connection fails

"That one didn't work. Most common reasons: signed in with the wrong email (use your business one, not a personal account), closed the window too early, or, for Outlook, your Microsoft 365 needs a one-time admin approval first. Want to try again, or skip for now? If Outlook keeps refusing, we can use Claude in Chrome on Outlook on the web instead, no setup needed."

If they skip, note it in `my-connections (MCP)/connected-apps.md` as "skipped" so we know to revisit later.

## After going through everything

Summarise what is connected and what isn't. Then say: "Connections done. Type /connect any time to add more or fix one. What do you want to work on?"
