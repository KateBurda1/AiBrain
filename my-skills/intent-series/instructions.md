---
name: intent-series
description: Build a 5-part outreach and content series for one ZoomInfo intent topic in Zoho (Business Transformation, Sales Transformation, Digital Marketing, and the rest). Walks the buyer journey as a 5 x 6 matrix, lands a value proposition and differentiated message per stage, then produces the creative brief, content, and visuals.
---

# Intent Series

Owner: Kate. Team: Jack (who is on the list, cadence fit), Maxell (copy), Scout (angles), Shelby (visual build).
Created 2026.09.24, first run on Business Transformation (Track 6).

## Where everything lives

`my-work (outputs)/prospects/outreach/[intent-slug]/`
- `yyyy.mm.dd - Outreach - [Intent].md` holds the Zoho cadence, the journey matrix, the creative brief, and the social content for that intent
- `visuals/` holds the rendered PNGs and carousel PDFs, with `visuals/source/build.py` to regenerate them

Cadence source for all tracks: [[2026.08.26 - Internal - Zoho Intent Branching Engagement Spec]].

## How to run it

**Ask Kate one question at a time.** Wait for the answer, fold it in, then ask the next. Never batch questions.

**Before asking anything, pull what the systems already know:**
1. Query Zoho Contacts where `ZI_Intent_Topic` contains the intent. Summarize titles by function and seniority, top companies and industries, and which other intent tags overlap. This answers "who is the buyer" without asking.
2. Read [[what-we-sell]], [[how-we-sound]], [[my-voice]], and the intent's existing outreach file.

## Start with the instigator, before any grid row (Kate, 2026.09.27)

Before writing Thinking and feeling, answer: **why is this signal firing at all?** An intent topic name can mean several things, so make the assumption explicitly and confirm it with Kate.
1. **Who is really searching.** If Zoho shows most of a company's C-suite tagged at once, that's a company-level research surge landing on senior names, not the CEO personally reading. The actual researcher is usually sales leadership, RevOps, or someone building a vendor shortlist.
2. **List the likely instigators, strongest first,** grounded in the overlap tags, the calendar (budget season, fiscal year, renewals), and Kate's own case studies and articles in `my-files (knowledge)/`. Include "not a buyer at all" (competitors, data sellers) as an honest option.
3. **Pick with Kate,** then name what the instigators have in common. That becomes the thesis.
4. Leadership-change instigators get their own play later via ZoomInfo Scoops, not folded into the main series.

## Depth standard for every stage (Kate, 2026.09.27: "I like the depth... it enriches the value prop, thus the messaging")

Build all six rows of a stage at once, at this depth, then show Kate the whole column before moving on. Nothing goes to the file until she's seen it.
- **What changed:** one or two lines on what's different from the last stage.
- **Thinking and feeling:** the addressee's real questions in their own voice (three or so, not one), then a named emotional state ("uneasy, about to put a number in front of the board they can't back up"), then the committee thread: one line per chair (CFO, sales, marketing, CTO) showing their version of the same worry.
- **Focus:** three or four bullets of what they care about right now, including the urgency or window (e.g. "before the budget locks"), plus one line on how the committee sees the same focus from their chair.
- **What we have:** specific methodology pieces, Ignite features, and real precedents from the knowledge base, never generic.
- **Impact, value proposition, message:** each built from the rows above it. Offer two or three message options with a recommendation, and show the footing.

The depth in the top rows is the point. Thin thinking and feeling produces a generic value proposition, which produces a clever-but-empty message.

## The journey matrix: 5 stages, not 6

**Current rule (Kate, 2026.09.29, repeated 2026.09.30: "there are 5.. not six"):** five stages across: Point of inspiration, Informed, Explore, Aware of product, Validate. Rows down each stage: Thinking and feeling, Focus, What we have, Impact, Value proposition, Message. One stage per touch, five touches. The 6-stage table below is superseded history, kept only for reference.

### Superseded: the 6 x 6 version (2026.09.27)

**Corrected by Kate, 2026.09.27 — this replaces the earlier 5-stage version.** Columns are the 6 stages. Each stage maps to one of the pieces of content and one step of the email cadence.

| | 1. Point of inspiration | 2. Aware of situation | 3. Informed | 4. Aware of product | 5. Validate | 6. The decision |
|---|---|---|---|---|---|---|
| **Thinking and feeling** | | | | | | |
| **Focus (what they care about)** | | | | | | |
| **What we have** | | | | | | |
| **Impact (what we have, on their focus)** | | | | | | |
| **Value proposition** | | | | | | |
| **Differentiated message** | | | | | | |

The value proposition comes out of thinking and feeling, focus, what we have, and impact. The differentiated message comes out of the value proposition.

**Note on the two new columns (pending full definitions, confirm as we build each series):** Kate confirmed Aware of situation and Informed "really go together" — adjacent stages, both about the buyer coming to fuller understanding of the problem before any vendor search starts. Validate is "where they are looking at options" (vetting us against alternatives, later than Aware of product, not earlier — a due-diligence stage, not early-stage shopping). The decision is the final close stage (what the old 5-stage model called Validate: proof, board-readiness, reputation on the line). Existing series built under the old 5-stage model (Business Transformation) haven't been retrofitted to this yet.

**Rules for the differentiated message:** clearly different from what every other consultant says, clever, and it leads them to think rather than telling them. It should read like a question they can't answer comfortably, or a mirror they recognize themselves in, not a claim about us.

## What each stage means (Kate's definitions, 2026.09.24)

Use these for every intent. The buyer knows more at each stage, so their head is in a different place.

1. **Point of inspiration.** They've been watching trends for a while. They're concerned about how big the shift is, how quickly they could report back wins, and what the lift would be. Nothing is decided.
2. **Informed.** They understand the situation more fully and may already know parts of the game plan. The quarterly clock is running (earnings calls, quarterly reviews). They want the top line moving in the right direction fast.
3. **Explore.** They still have concerns, but they're working toward resolving them. They're figuring out the path and the players to get there. Trust matters here. They're looking for insight and foresight, not just products and services.
4. **Aware of product.** They've found us. They want specifics: scope, speed, what it takes from their people, and a clear first step before any big commitment.
5. **Validate.** They're close. They're checking proof and risk, thinking about the board, and asking whether it will hold. Their reputation is on the line.

**Advisor first, then paid.** Kate finds them, but shows up as an advisor, not a vendor. Stages 1 to 3 give insight and foresight without selling. Stage 4 is where it turns into "you should pay me," with a contained first paid step. Never push products and services before Stage 4.

## The per-stage formula (confirmed by Kate 2026.09.24)

Map every stage the same way, as its own full column. Don't carry assumptions forward from the stage before: at each stage the buyer knows more, so what they think and feel changes. For example, at Informed they understand the situation more fully and may already know parts of the game plan.

For each stage:
1. **What changed since the last stage?** What do they know now that they didn't before?
2. **Thinking and feeling:** what's in their head, in their words, and what they're uneasy about. If the buyer for this topic is a committee rather than one clean persona (Zoho shows a whole account's exec bench tagged together, not one title), capture **both threads**: the primary addressee (keep the addressee consistent with other series, e.g. always the CEO/President) and the broader watching committee (CFO, CTO, CMO, etc., each independently arriving at their own version of the same realization). Don't split into multiple personas, let this row carry the cross-functional texture instead.
3. **Focus:** what they care about at this moment.
4. **What we have:** the specific piece of the methodology that meets that focus.
5. **Impact:** what that piece does to their focus.
6. **Value proposition:** built from rows 2 to 5, explicitly as "because they're focused on X, we have Y, which creates impact Z on what they care about."
7. **Differentiated message:** built from the value proposition. It leads them to think rather than telling them.
8. **Draft the full column, save it to the intent file, then ask Kate one question** to confirm or correct it before moving to the next stage.

**Understand before you solve (Kate, 2026.09.27, applies to every grid build):** walk rows 1 to 6 in strict order before touching messaging. Don't validate or lock in a differentiated message, even one that sounds right, even one reused from an earlier series or an old draft, until it foots back through thinking/feeling, focus, what we have, and impact. A message that sounds right isn't confirmed right until it's been derived that way, not assumed.

**Keep it on the top line, not the discipline.** Presidents and CEOs think about top-line revenue, not the sales and marketing functions. Kate's framing: the science and strategy first (revenue goal, strategies, actions), then the customer engagement approach.

**The message has to foot.** Like a ledger, each differentiated message must trace back to that stage's thinking and feeling, then focus, then what we have. Clever but not footed is just clever messaging. Add a footing table under the matrix: for each stage, show which words in the message pick up which row.

**A signature hook can be used more than once, across stages or across series, as long as it holds water each time (Kate, 2026.09.27, loosens the earlier one-use-only rule: "you can use it many times if it holds water").** Don't force a hook into a stage it doesn't foot in just because it worked elsewhere, but don't cap it at one use either. "Be right, not just lucky" sat at Aware of product for Business Transformation (the Revenue Reveal's opening question); it can also land at a different stage, or in a different intent series, if that stage's own thinking/feeling, focus, and what-we-have logic actually earns it there.

**Never compare across different intents to justify a placement (Kate, 2026.09.27: "don't compare different intents, different people, the messaging is based off where they are, it might fit, it might not").** A different intent topic means a different buyer, watching from a different place in their own journey. A hook's placement in one series is never evidence for its placement in another, even when it's the same hook. Check the footing independently, from that series' own buyer data and journey reasoning, every time — never "it worked there, so it'll work here."

Other hooks: "Do less, make it mean more," the silent saboteur, the War Room, Outside-In Thinking, "bringing simplicity to your complexity."

**Bring the team in.** Have Maxell pressure-test each stage's value proposition and message. Have Jack check the stage against the matching cadence step.

## Questions to ask, in order, one at a time

1. At the point of inspiration, what does this buyer say out loud when they first feel the problem? Get Kate's real words.
2. What proof can we use at Validate for this buyer: named clients, results, before-and-after numbers?
3. How hard should the messaging push: mirror (they see themselves), dare (a question they can't answer comfortably), or contrarian (it flips a belief)? Can vary by stage.
4. Walk each stage column top to bottom, confirming or correcting the draft before moving to the next.

## Outputs

1. **Creative brief:** audience from the Zoho data, the thesis, the matrix, tone setting, proof, channels, and the call to action per stage.
2. **Content:** 5 LinkedIn posts (caption and slide text), timed to the cadence steps, plus any edits the matrix suggests for the emails.
3. **Look and feel:** Kate likes carousels with movement, like a short embeddable video. Her reference is her own animated piece `OneDrive/ABM It just doesn't make sense.gif`: centered elegant serif, white and black frames alternating, a pink capitals reveal line, ellipsis pacing, one black and white image, thin rule and pink KB logo, about 25 seconds. Deliver each piece as MP4 (LinkedIn), GIF (email), carousel PDF and a cover PNG. The [[2026.09.24 - Outreach - Business Transformation - Creative Brief|Business Transformation creative brief]] is the worked example. **Approved template (Kate, 2026.09.24, "DAMN THIS IS BEAUTIFUL"):** `prospects/outreach/business-transformation/motion/piece-1-inspiration/`. Copy its `source/` folder (piece1.html plus render.py), swap the frames and text, and re-render. Playfair Display serif, white and black frames, brand pink #D51067, lines fading up one at a time, about 28 seconds, MP4 plus GIF under 5 MB plus stills. Older alternative: the Commercial Excellence look (black, hot pink #d53d72, "COMMERCIAL EXCELLENCE" eyebrow, KB logo, kateburda.com, vertical @kateburda.com). If Canva is connected, duplicate an existing Commercial Excellence page and swap the text in. If not, copy `prospects/outreach/business-transformation/visuals/source/build.py`, change the slide text, and run it (needs Chrome).
4. **Zoho update package, mandatory once the grid and messages are confirmed.** The matrix and creative brief are draft work until this exists, and the intent isn't done until it does. Save `[Intent] - Zoho Update Package.md` in the intent's folder, with three parts:
   - **Cadence copy:** the live Zoho Cadence for this intent (check its real current steps first, don't assume the original branching spec is still what's running) rewritten step by step to the confirmed stage messages, in Zoho's own step/subject/body format, ready to paste in.
   - **Email template copy:** any Zoho Email Template tied to this intent, updated the same way.
   - **Workflow rule spec:** the branch logic in plain "when this happens, Zoho does this" rules (see the Business Transformation branch table as the model). This tool has no access to build Zoho Cadence, Email Templates, or Workflow Rules directly, confirmed 2026.09.24, so this spec is what Kate pastes in herself or hands to Tristan. Never assume the live cadence already matches the grid, check it.

## Voice guardrails

The buyer is always in charge. Never imply we take the controls or replace their people (Kate picked "navigator" over "pilot", "co-pilot" and "crew" for this reason). No em dashes. Never "actually." Short sentences. Warm, clever, thought-provoking, occasionally sarcastic, even cheeky (Kate, 2026.09.27). Nothing that reads as AI. Nothing goes out without Kate's approval.

**Look:** mostly black, white and greys, with the KB brand colors held back for impact: PMS 214 raspberry and PMS 675 berry (KB pieces use KB colors only, Kate 2026.09.27). White (negative) logo on grey frames. See `my-business (context)/brand-standards.md`.
