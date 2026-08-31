# Connected Apps

Every app your business uses that your assistant can access. This gets filled in during /setup or /connect.

You do not need to fill this in yourself. Your assistant updates it when you connect apps.

---

## What we use

| App | What it does | What your assistant can see |
|---|---|---|
| Microsoft 365 (Outlook) | Business email — Kate@kateburda.com | Emails (confirmed working, 2026.08.25), drafts. Read-only: can't drop drafts straight into Outlook, will draft in chat or type into Outlook on the web via Claude in Chrome instead. |
| Microsoft 365 (Calendar) | Scheduling | Read-only. Write access tested twice 2026.08.26 — denied both before and after Kate reconnected via /connect, same error both times (`Calendars.ReadWrite` not consented on the connector's own app registration). This isn't a re-auth/consent issue Kate can fix by reconnecting; it's the connector itself. Treat calendar as read-only until Anthropic's Microsoft 365 connector adds this scope. Workaround for creating/editing events: Claude in Chrome on Outlook on the web (same fallback already used for email drafts). Kate adds/edits events herself otherwise. |
| OneDrive / SharePoint | Files | Confirmed working via the Microsoft 365 connector (not just local sync), 2026.08.25, full search access across Kate's OneDrive, including the `Ignite` folder tree |
| QuickBooks Online | Accounting | Confirmed connected, 2026.08.25. Company: Kate Burda & Company. Can pull P&L, balance sheet, AR/AP aging, sales by customer/product, invoices, estimates, cash flow, and more. |
| Canva | Design/creative | Confirmed connected, 2026.08.26. One brand kit found on the account. Maxell can generate designs (carousels, social graphics, etc.) directly using the brand kit. |
| Zoho CRM | Sales pipeline / CRM | Confirmed connected, 2026.08.26. Org "Kate Burda & Company," created 2026-08-05, professional plan, 1 license. Can read/write Leads, Contacts, Accounts, Deals, Quotes, Campaigns, Invoices, and more. As of 2026.08.26: Deals is empty (no pipeline logged), Leads has one unworked batch of 20 from "Kisaco Research" (imported 2026-08-20). |
| Strava | Fitness/training data | Confirmed connected, 2026.08.28. Megan (fitness coach) uses this to see Kate's actual activities, performance, and training load instead of relying on self-reporting. |

---

## What it can connect to

Three tiers, depending on how much setup is needed.

### Tier 1: Your essentials (connected during /setup)

Email, calendar, and files. Works with Google, Microsoft 365, or both. Connect whichever your business runs on. Most people use one side; connect both if you use both.

- **Google Workspace** - Gmail, Google Calendar, Google Drive
- **Microsoft 365** - Outlook (email + calendar), OneDrive
- Claude in Chrome (optional browser extension, reaches any website)

These get walked through during /setup. No technical knowledge needed.

**One difference worth knowing.** The Google (Gmail) connection can read your inbox AND save draft replies straight into Gmail. Microsoft's connector is read-only: it reads your Outlook inbox, calendar, and files, but it cannot save drafts into Outlook. So for Outlook your assistant writes the reply in chat for you to paste, or types it straight into Outlook for you using Claude in Chrome. Same result, one extra step. Either way it never sends. You always send.

Microsoft 365 business accounts sometimes need a one-time approval from whoever administers your Microsoft 365, which is often you. Personal Outlook.com or Hotmail accounts connect through Claude in Chrome instead.

### Tier 2: One-click inside the Claude app

- Slack
- Stripe
- Canva
- Webflow
- Notion
- GitHub
- More being added by Anthropic regularly

These are already available in the Claude desktop app's connector menu. Open the Claude app's settings, find the Connectors section, click Add next to the app you want, sign in, and authorise. Your assistant can walk you through any of them on request.

### Tier 3: Advanced, ask your assistant

- Meta Ads
- Xero / MYOB
- HubSpot, Salesforce, custom CRMs
- Anything with an API

These need a small one-off setup (an MCP config). Type /support and your assistant will walk you through it. Some work first try, others take a bit longer. As a fallback you can always paste the data into chat.

If your assistant cannot reach a tool directly, paste the data into chat. It still works with everything you give it.

---

## Reporting rhythm

[How often do you look at your numbers? What do you track?

Example:
- Weekly: social media engagement
- Monthly: revenue report, new client count
- Quarterly: business review]

---

## Notes

- Add apps here as you start using them
- Keep passwords in your password manager, not in this file
