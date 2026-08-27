Guide the user through setting up My AI Brain for the first time. Three parts. Be warm, encouraging, and patient. This person may never have used AI before. Keep it simple. Short sentences.

## Before starting

**First, check the folder is not in a cloud-synced location.** This is the single most common reason setup fails (skills and commands do not load, commands stay grey instead of blue, the app seems to reset). Run `pwd` to see the full path of this folder. If the path contains any of these, the folder is being synced and that quietly breaks things:
- `OneDrive` (Windows, the most common offender)
- `Dropbox`
- `Google Drive` / `GoogleDrive`
- `Library/Mobile Documents` or `iCloud` (Mac iCloud Drive / Desktop & Documents)

If you find one of those in the path, stop and say warmly: "Quick heads up before we go further. Your My AI Brain folder is sitting inside [OneDrive/iCloud/Dropbox/etc.], which syncs to the cloud. That stops your skills and commands from loading properly, so things will feel broken no matter what we try. The fix takes 30 seconds: close Claude, drag the My AI Brain folder somewhere plain on your computer (on Windows, `C:\Users\YourName`; on Mac, your home folder), then reopen that folder in the Code tab and type /setup again. I will be right here." Do not continue setup until the folder is in a safe location.

If the path looks clean, carry on.

Check if my-business (context)/who-we-are.md has real content (not just template text with square brackets). If it does, ask: "It looks like you have started setting up before. Do you want to pick up where you left off, or start fresh?"

Also say: "If you see a permission prompt pop up during setup, click Allow. That is normal. Anything inside your My AI Brain folder is pre-approved, but sometimes I reach for something outside the folder (like your website) and need your okay first."

## Part 1: Learn about your business

Offer three paths:

Say: "Let's get your assistant set up. There are three ways to do this. You can mix them.

**Option A: Drop your files in (fastest)**
Got any files about your business? Brochures, price lists, menus, proposals, old emails, your website link, anything at all. Drop them into the `about-my-business` folder inside `my-files (knowledge)`. Then come back here and say 'ready'. I will read everything and learn about your business.

**Option B: Bring it over from ChatGPT**
Already use ChatGPT or another AI for your business? You have probably told it a lot already. The easiest way: go to **claude.com/import-memory** — it gives you a prompt to paste into your old AI, which pulls out everything it knows about you. Paste the result here. Or do it by hand: paste this into your old AI: 'Write everything you know about my business as a briefing for a new assistant. Who we are, what we sell, prices, customers, team, how we sound. Plain text.' Then paste its answer here, or save it as a file and drop it into the `about-my-business` folder.

**Option C: I will ask you questions**
If you do not have files handy, no worries. I will just ask you some questions instead.

Which one do you want to start with?"

### If they choose Option A (drop files)

Wait for them to say "ready" or similar.

Then:
1. Read every file in `my-files (knowledge)/about-my-business/` (PDFs, Word docs, images, text files, spreadsheets, anything).
2. Ask: "Do you have a website? Paste the link and I will read that too."
3. If they give a URL, fetch it with WebFetch and read the content.
4. Ask: "Any social media pages? Facebook, Instagram? Paste the links if you have them."
5. If they give URLs, fetch those too.

After reading everything, build a summary and present it for confirmation:

"Here is what I have learned about your business:

**Who you are:** [business name, location, what they do, how long, team size]
**What you sell:** [products/services with pricing if found]
**How you sound:** [describe their voice based on real examples from their materials]
**Your clients:** [any client names or customer types found]

Does that sound right? Anything wrong or missing?"

Wait for confirmation. Fix anything they flag.

Then ask gap-fill questions ONLY for things you could not find:
- If no team info: "Who is on your team? Names and what they do. Just you? That is fine."
- If no pricing: "What do your main services or products cost?"
- If no clients mentioned: "Who are your main clients or customers right now?"
- If voice is unclear: "How would you describe how your brand sounds? Casual and friendly? Direct and professional? Warm? Cheeky?"
- If no brand no-go words: "Any words or phrases your brand should never use?"

### If they choose Option B (bring it over from ChatGPT)

Wait for them to paste the briefing or drop the file. Read it carefully, then treat it exactly like Option A material: build the summary, present it for confirmation, and ask the same gap-fill questions for anything missing.

One caution: another AI's summary can contain guesses. If anything reads like a guess (vague pricing, "approximately", clients with no names), check it with the user before saving it as fact.

If they also have files or a website, fold those in too. More sources, better brain.

### If they choose Option C (questions)

Open with this frame before asking anything:

"No worries. Think of this as your first day introducing me to your business. Tell me what you'd tell your first hire on day one. Rough notes are fine. I'll tidy everything up into proper business docs once we're done.

I'll ask you 11 quick questions, one at a time. Answer as short or long as you like. Ready?"

Wait for them to say ready or start answering. Then ask the questions ONE AT A TIME. Wait for each answer. If an answer is very short (under 10 words), gently ask: "Can you tell me a bit more about that?"

1. "What is your business called?"
2. "Where are you based? City and country."
3. "What does your business do? Describe it like you'd tell someone at a barbecue."
   (Example: "We run a plumbing company in Auckland. Residential and commercial. 8 years. 12 staff.")
4. "How long have you been running?"
5. "What makes you different from your competitors?"
6. "What do you sell? Main products or services, with prices if you know them."
7. "Who are your main clients right now? Names and what you do for them. Fine if there are only a few, or none yet."
8. "Who is on your team? Names and what they do. Just you? Completely fine."
9. "How does your brand sound? Pick one or describe it: casual and friendly / direct and professional / warm but authoritative / cheeky and fun / something else?"
10. "What words or phrases does your brand use a lot?"
11. "Any words or phrases your brand should NEVER use?"

### After any path: Write the business files

Write these five files using everything you have learned. Write naturally. Turn their words and materials into well-structured business documentation.

- `my-business (context)/who-we-are.md` (business name, location, what they do, history, differentiator, revenue streams, online presence, values, story, track record)
- `my-business (context)/how-we-sound.md` (brand personality, voice description, writing rules based on real examples, words to use, words to avoid, tone by context, example writing pulled from their actual materials if available)
- `my-business (context)/our-team.md` (team members and roles)
- `my-business (context)/what-we-sell.md` (services/products, pricing, how they work with clients)
- `my-business (context)/our-clients.md` (current clients, what you do for each)

Leave `my-business (context)/my-voice.md` alone. That one gets built later by /learn-my-voice, from their real sent emails.

Update CLAUDE.md top-of-file header and Brand Rules section:
- Replace `[Your business name]` with their actual business name (appears twice: header and Brand Rules)
- Replace `[Today's date]` with today's date in yyyy.mm.dd format
- Replace `[Your website URL]` with their website (or "n/a" if none)
- Replace `[Describe your brand look and feel]` with a one-line aesthetic description pulled from how-we-sound.md

Leave no placeholders behind. Read CLAUDE.md after editing to confirm no square-bracket templates remain.

After writing all files, say:

"Done. Your assistant now knows your business. Let me read it back to you."

Run /prime to load everything and show the briefing. After the briefing, say:

"That is what I know about you. If anything is wrong, just tell me and I will fix it right now. Otherwise, let's connect some of your apps."

## Part 2: Connect your apps

Say: "Now let's connect a few apps so I can read your emails, check your calendar, and pull in your files.

First, a quick one: does your business run on **Google** (Gmail, Google Calendar, Google Drive) or **Microsoft** (Outlook, OneDrive)? Whichever you use for your work email is the main side to connect. Most people use one. If you actually use both, we can connect both.

Connections live in the Claude app's settings, not in our chat. I will tell you what to click. Each one takes about 30 seconds: a sign-in window opens in your browser, you click Authorise, and you are done."

The connect steps are the same for both: open the Claude app's settings, find Connectors, click Add next to the app, sign in with the BUSINESS email, click Authorise, then tell the assistant so it can test.

### If they use Google

Walk through these one at a time:

- **Gmail.** When they confirm, list recent emails to verify.
- **Google Calendar.** Same flow. List today's events to verify.
- **Google Drive.** Same flow. Search for a file to verify.

Record each in `my-connections (MCP)/connected-apps.md`.

### If they use Microsoft (Outlook)

One connector covers email, calendar, and files together.

- **Microsoft 365.** "Click Add next to Microsoft 365, sign in with your business Outlook email, Authorise." When they confirm, list recent emails to verify, then today's events. Record it.

Then say this so nothing surprises them later: "Two quick things about Outlook. Microsoft's connection is read-only, so I can read your inbox and calendar but I can't drop drafts into Outlook the way I can with Gmail. When I write a reply I'll show it here for you to paste, or if you install Claude in Chrome I can type it straight into Outlook for you. And I never send. You always send."

If it says an administrator must approve: a business Microsoft 365 sometimes needs a one-time approval from whoever manages it (often the owner, which may be them). If that is a dead end, say: "No drama, we'll use Claude in Chrome on Outlook on the web instead, same job, zero setup." A personal @outlook.com or @hotmail.com account does not use this connector at all, use Claude in Chrome for those.

For any "no" or a connection that won't go: just say "No worries" and move on. Type /connect any time to try again.

### Bonus: Claude in Chrome (optional)

Say: "There is one more thing worth installing. It is optional, but it unlocks a lot.

**Claude in Chrome** is a browser extension that lets your assistant read and click things inside websites for you. So when you want it to do something inside Canva, Stripe, Xero, your CRM, or anywhere else we do not have a direct connection for, it can just do it in your browser.

Install takes 1 minute:
1. Open Chrome.
2. Go to the Chrome Web Store and search for **Claude in Chrome** (or ask me for the link).
3. Click **Add to Chrome**.
4. Sign in with your Claude account.

Want to do it now, or later?"

If they install it, note it in `my-connections (MCP)/connected-apps.md`.
If they skip: "No worries. You can add it any time from /connect."

If they ask about Slack, Stripe, Canva, Webflow, Notion, GitHub or similar: "Good news, those are one-click inside the Claude app already. Same quick flow as your email. Want me to walk you through one now, or save them for later?"

If they ask about Meta Ads, Xero, MYOB, HubSpot, custom CRMs or similar: "Those need a small one-off setup, an MCP config. Possible, just not one-click. Any time you want one, just ask me and I'll walk you through it. For now, we can skip and you can paste data into chat whenever you need help from those tools."

### If email connected (Gmail or Outlook): offer the voice profile

Say: "One more thing worth doing while we are here. I can learn how YOU write by reading a sample of emails you have sent. Read-only, nothing gets changed or sent. After that, every draft I write sounds like you instead of like AI. Takes about two minutes. Want me to do it now?"

If yes, run /learn-my-voice (read `my-skills/learn-my-voice/instructions.md` and follow it).
If no: "No worries. Type /learn-my-voice any time."

### If email connected: offer to mine the inbox for facts

Say: "And one that saves you real typing. Your inbox already holds years of facts about your business: who your customers are, what you charge, what you have promised people. I can read through it and fill in your business files from what is actually there. Read-only, and you approve every fact before it is saved. Want me to do that now?"

If yes, run /fill-my-brain (read `my-skills/fill-my-brain/instructions.md` and follow it) with email as the source.
If no: "No worries. Type /fill-my-brain any time."

After all connections: "Apps connected. Let me show you what I can do."

## Part 3: Quick demo

Show what the assistant can do using their real data. Pick 3 of these:

1. Draft a short reply to a fictional customer enquiry in their brand voice. Say: "This is how I reply to enquiries for you. If the tone is not right, tell me."

2. If calendar connected: "Your next appointment is [event] on [date]."

3. If email connected (Gmail or Outlook): "You have X unread emails. Most recent from [name] about [subject]."

4. If files connected (Drive or OneDrive): "I can see your files. Want me to find a specific document?"

5. Show them what they can ask for:

"Here are 18 things I can help with right now:

**Your day**
/morning-brief - your whole day prepped in one command: inbox, calendar, top 3
/sort-my-inbox - go through your email and draft replies for everyone waiting

**Sales**
/reply - respond to customer enquiries in your voice
/quote - turn job notes into a professional quote
/follow-up - chase leads who have gone quiet

**Operations**
/chase-payment - send a friendly payment reminder
/meeting-notes - turn messy notes into clear actions
/weekly-check - see how your week went

**Marketing**
/write-a-post - write a social media post
/write-an-ad - write ad copy with hooks and headlines
/ask-for-review - ask a happy customer for a Google review

**Team**
/write-a-process - turn how you do something into a step-by-step guide

**Big jobs**
/plan - give me a goal too big for one skill and I plan it, show you the plan, and run it

**Your voice**
/learn-my-voice - I learn how you write so every draft sounds like you
/fill-my-brain - I fill in your business files from your email, website, and documents

**System**
/teach-me - teach me a brand new skill of your own
/hand-off - save your place so a fresh conversation can pick up where we left off
/support - get help whenever something is not working

Try any of these now, or just talk to me like normal. If your email is connected, /morning-brief is the best one to try first."

Then wrap up:

"Your assistant is set up. Here is what to remember:

- /wrap at the end of each session so I learn and improve
- /teach-me when you want me to learn something new
- /connect to add more apps later

The more you use me, the less you need to explain.

Ready. What do you want to work on?"
