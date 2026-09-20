---
name: learn-my-voice
description: Learns how you actually write by reading your real sent emails, then saves a voice profile so every draft sounds like you. Use when you hear "learn my voice", "sound more like me", "that doesn't sound like me", or "/learn-my-voice".
---

# Learn My Voice

## Goal
Build a profile of how the business owner actually writes, from their real sent emails. Save it to `my-business (context)/my-voice.md`. Every skill that drafts messages reads this file, so after this runs, drafts sound like them instead of like AI.

This is different from `how-we-sound.md`. That file is the brand voice (how the business sounds in ads and posts). This file is the personal voice (how the owner writes an email to a real person).

## Inputs
- Email connected (Gmail or Outlook). Reading sent mail is read-only, so this works the same on both. If neither is connected, say: "I need your email connected for this one. Type /connect and I will walk you through it. Or paste 5-10 emails you have sent and I will work from those instead."
- Nothing else. The assistant does the reading.

## Steps

### Step 1: Ask permission first
Say: "I am going to read a sample of emails you have sent, so I can learn how you write. I only read. I do not change or send anything. Okay to go ahead?"

Wait for a yes.

### Step 2: Read their sent mail
Search their sent folder for 20-30 recent emails they wrote themselves. Skip anything automated (receipts, calendar responses, forwarded newsletters, one-word replies).

Aim for a mix: replies to customers, messages to suppliers or partners, anything longer than a couple of sentences.

If no email is connected and they pasted emails instead, use those.

### Step 3: Study how they write
Look for patterns, not one-offs:

- **Openers.** How do they start? "Hi Sarah," "Hey mate," "Morning,"? Do they open with a pleasantry or get straight to it?
- **Sign-offs.** "Cheers," "Thanks," "Talk soon,"? Full name, first name, or initial?
- **Length.** Are their emails three lines or three paragraphs?
- **Sentences.** Short and punchy or longer and flowing?
- **Formality.** Contractions? Slang? Emoji? Exclamation marks?
- **How they ask for things.** Direct ("Can you send that over today?") or soft ("Whenever you get a chance...")?
- **How they say no or deliver bad news.**
- **Phrases they reach for again and again.**
- **Things they never do.** Never use a greeting? Never write more than five lines? Never use "Kind regards"?

### Step 4: Write the voice profile
Fill in `my-business (context)/my-voice.md` with what you found. Quote 2-3 short real examples (a sentence or two each, nothing private or sensitive). Strip out anything confidential: names of customers, amounts, personal details. The pattern matters, not the content.

End the profile with a **Never rules** section: a short, hard list of things the owner never writes ("never signs 'Kind regards'", "never opens with 'I hope this email finds you well'", "never uses emoji with clients"). Every drafting skill checks its draft against this list before showing it, so make each rule concrete enough to check.

Also note in the profile: when drafting to someone the owner has emailed before, the assistant should read a few of those past emails first and match that specific relationship. The profile is the fallback; the owner's real history with a person is the gold standard.

### Step 5: Prove it works
Draft a two-line test email in their voice ("a customer asked if you are available next week"). Show it and ask: "Does this sound like you?"

If they say no, ask what is off, fix the profile, and test again. Do not finish until they say yes.

### Step 6: Confirm
Say: "Done. Your voice is saved. Every reply, follow-up, and payment reminder I draft from now on will sound like you. If a draft ever sounds off, just tell me and I will update your profile."

## Output format
- `my-business (context)/my-voice.md` filled in.
- One test draft confirmed by the user.

## Quality check
- The profile describes patterns found in their real mail, not guesses.
- No private or sensitive content copied into the profile.
- The user confirmed the test draft sounds like them.
- Nothing was sent, changed, or deleted in their mailbox.
