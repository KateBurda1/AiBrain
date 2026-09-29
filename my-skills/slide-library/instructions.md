# KB&Co Slide Library

Set 2026.09.29, at Kate's direction: "I loaded into the AI Brain templates these are all the slides I have we can use them or shift them up for decks and proposals." Addressed to Jack, Maxell and Maya.

**How to treat it (Kate, 2026.09.29):** "these are reference that we can pull up when needed ... you can redesign what you need to." The library is a reference for Kate's content, frameworks and proof, not a rule. Pull a slide as is when it fits. Redesign it when a cleaner, sharper version would serve the client better, keeping the KB&Co brand (Franklin Gothic, PMS 214 and 675). Kate thinks the team often does better than the older designs. Ignite decks use Ignite's brand, not this library.

The fully designed KB&Co PowerPoint templates also live in OneDrive: `my-files (knowledge)/Brand/Kate & Co- Administrative/3. PPT Template/` (`kb_PPT-Template.pptx` is the full designed set, `kb_PPT-Template-Blank.pptx` the blank). Use them as a style reference or starting point for redesigned slides.

## Where it lives

`my-files (knowledge)/ppt Templates used in presentations/KB & Co PPT Library/`

- `PPT Master LIbrary.pptx` is **the master: 85 slides, the current version.** Slide 85 (Tristan's bio) was added 2026.09.29; OneDrive version history holds the 84-slide original. Use this one.
- `Individual Slides/PPT Master LIbrary.pptx` is an older 72-slide copy. Don't pull from it. Its only slide the master lacks is "Profitable Growth / Where you win" (old slide 68), which also sits on its own in `Individual Slides/Where you win 2.pptx`.
- `Individual Slides/` also holds single-slide files and PNG/JPG versions (Execs Unsatisfied, Emerging Demand, Results Mechanism, Where you win, Proactive Effects, CEB Road map). The PNGs work for emails, LinkedIn and landing pages. `testimonials.pptx` is empty.
- `PPT Deck Reference Spreadsheet.xlsx` is Kate's older map of slide to offer. Its numbering doesn't match the current master. The index below replaces it.
- A blank branded template for new slides: `my-files (knowledge)/Brand/Kate & Co- Administrative/3. PPT Template/kb_PPT-Template.pptx`

## Build a deck in one step

```
python3 "my-skills/slide-library/build_deck.py" "<output.pptx>" 1-3 4 5 33 37-38 48
```

This copies the master and keeps only the slides you name, in the order you name them. Layouts, images and brand stay intact. Then edit the words in the new file. Save client decks to `my-work (outputs)/clients/<client>/03 - Working Files/` (draft) or `02 - Deliverables/` (final), named `yyyy.mm.dd - Client Name - Deck Name.pptx`.

## Standard deck spines

Use these as a starting order, then swap in picture blocks and proof slides that fit the client.

| Deck | Slides |
|---|---|
| Revenue Strategy proposal | 1, 2, 3, 4, 5, 8, 10, 22, 23, 24, 27, 28, 30, 37, 38, 40, 41, 42, 43, 85, 47, 48, 52, 53, 54 |
| Sales Effectiveness proposal | 1, 2, 3, 4, 5, 9, 10, 11, 13, 14, 23, 25, 26, 34, 38, 40, 41, 42, 43, 85, 47, 48, 54 |
| Marketing / brand proposal | 1, 2, 3, 6, 16, 17, 18, 19, 21, 29, 37, 38, 41, 42, 43, 85, 47, 48, 54 |
| Website engagement proposal | 1, 66, 3, 6, 7, 60, 37, 38, 41, 42, 43, 85, 47, 48, 52, 53, 54 |
| First conversation / capabilities (Jack) | 1, 2, 3, 71, 10, 13, 4, 40, 41, 43, 85, 47, 48, 54 |
| Speaking / keynote (Maya) | 67, 68, 64, 65, 10, 11, 13, 14, 71, 72, 78, 54 |

## The index

**Check before use** means the slide carries old client names, prices, people or placeholder text. Fix it before anything leaves the building.

| # | Section | Slide | Use it for | Check before use |
|---|---|---|---|---|
| 1 | Cover | Prepared for / A Conversation of Possibility | Every deck | Fill in client name |
| 2 | Picture block | Bringing Simplicity to Your Complexity | Opener | |
| 3 | Want / Get / Can | We Create Impact | Every proposal | |
| 4 | Method | 5-Step Rapid Revenue Return, Insight to Impact | Revenue, Sales, Marketing | |
| 5 | Method | Rapid Revenue Return deliverables | Revenue, Sales, Marketing | |
| 6 | Method | Pathway (branding to care and feeding) | Marketing, Website | |
| 7 | Method | Strategic Engagement Deliverables | Website | |
| 8 | Proof of thinking | What the Best Do Differently | Revenue Strategy | |
| 9 | Proof of thinking | What makes organizations effective in a transformation | Sales, Marketing | |
| 10 | Data | Execs Are Unsatisfied With Interactions (Forrester) | Sales, Revenue, prospecting | |
| 11 | Framework | Outside In Thinking, customer-centric value chain (1 of 2) | Sales, Revenue | |
| 12 | Framework | Outside In Thinking (2 of 2, filled in) | Sales | |
| 13 | Framework | Emerging vs. Established Demand | Sales, prospecting | |
| 14 | Framework | How Sales and Marketing Create Demand (Huthwaite) | Sales | |
| 15 | Framework | Same as 14 | | Duplicate of 14 |
| 16 | Framework | The Marketing Trifecta | Marketing | |
| 17 | Framework | Big idea / brand positioning questions | Marketing | |
| 18 | Framework | Brand Framework | Marketing | |
| 19 | Framework | Building the Future, Brand Strategy Plan | Marketing | |
| 20 | Framework | Awareness to Consideration to Conversion | Marketing | Template filler text ("Green marketing...", "YOUR TITLE 05") |
| 21 | Framework | Targeting the Most Valuable Customer, customer journey | Marketing, Sales | |
| 22 | Approach | Revenue Reveal, the approach (circle) | Revenue, Sales, Marketing, Website | |
| 23 | Approach | Revenue Reveal, performance pyramid | Sales, Revenue | |
| 24 | Approach | Insight Intelligence Report, what you get / so you can | Revenue, Sales | |
| 25 | Approach | Insight to Execution, Go-To-Market columns | Sales, Marketing | |
| 26 | Approach | Foundation / Framework / Focus | Sales | |
| 27 | Roadmap | Vision-to-Value Roadmap implementation plan | Revenue, Sales | |
| 28 | Roadmap | Vision-to-Value Roadmap, why it matters | Revenue, Sales | |
| 29 | Roadmap | Customer journey / most valuable member questions | Marketing, associations | Says "member"; shift for non-associations |
| 30 | Roadmap | Vision-to-Value Roadmap (illustrative) | Revenue, Sales | |
| 31 | Client example | FEI Membership Growth Formula | Associations only | FEI-specific |
| 32 | Client example | Building Blocks to Achieve FEI's Vision | Associations only | FEI-specific |
| 33 | Approach | Implementation of vetted roadmap | Revenue, Sales | |
| 34 | Approach | Lead, Coach + Sponsor / CONNECT / Design, Install, Alive | Sales | |
| 35 | Roadmap | Vision-to-Value Roadmap, designed foundation | Revenue, Sales | |
| 36 | Method | ADDIE Model | Training engagements | |
| 37 | Timeline | Illustrative Timeline | Every proposal | Adjust dates and steps |
| 38 | Investment | Investment for Performance (blank) | Every proposal | Add pricing |
| 39 | Proof | Where you win | Sales, Revenue | |
| 40 | Proof | Results (distressed hotel, unhappy associates, 17% lift) | Every proposal | |
| 41 | Proof | What it is like to work with us (testimonials) | Every proposal | |
| 42 | Divider | Who we are | Every proposal | |
| 43 | Bio | Kate Burda | Every proposal | |
| 44 | Bio | David Garrard | | Not active (our-team.md). Leave out |
| 45 | Bio | Sharla Hibberd | Only if Sharla is on the project | As-needed PM |
| 46 | Bio | Jawaria | Only when Jawaria is involved in the engagement (Kate, 2026.09.29) | |
| 47 | Divider | In good company | Every proposal | |
| 48 | Proof | Companies that have taken this journey (logos by industry) | Every proposal | |
| 49 | Proof | Where We Serve (memberships, SAMA) | Credibility | |
| 50 | Proof | Articles & Speaking Engagements | Credibility | |
| 51 | Proof | Speaking panels 2019, 2022, 2023 | Credibility | |
| 52 | Agreement | Client information and agreement | Proposals that close | Says Sandy Springs Hospitality & Tourism; replace |
| 53 | Agreement | Standard Terms and Conditions | Proposals that close | |
| 54 | Close | Thank you + contacts | Every deck | Lists Sharla; trim if she's not on it |
| 55 | Divider | Appendices | Long proposals | |
| 56 | Appendix | Foundational Discovery, Marketing | Marketing | |
| 57 | Appendix | Foundational Discovery, Sales | Sales | |
| 58 | Appendix | Foundational Discovery, Revenue Management | Revenue | |
| 59 | Appendix | Revenue methodology wheel | Revenue | |
| 60 | Appendix | Digital methodology (reach, reinforce, respond, repeat) | Marketing, Website | |
| 61 | Picture block | The Cinderella player | Sales, hiring conversations | |
| 62 | Picture block | Reinvent | Keynote, opener | |
| 63 | Picture block | (blank image slide) | | Empty |
| 64 | Picture block | Elevating the revenue approach (designed in 1970) | Revenue, Sales | |
| 65 | Picture block | Yet we expect today's performance | Revenue, Sales | |
| 66 | Picture block | A website is just the beginning (race car) | Website, Marketing | |
| 67 | Picture block | The weather has changed | Keynote, opener | |
| 68 | Picture block | A world ripe with disruption | Keynote, opener | |
| 69 | Picture block | Points of consideration and differentiation | Proposals | |
| 70 | Picture block | Known, comfortable, convenient isn't unique | Marketing, Sales | |
| 71 | Picture block | Sea of Sameness / don't invest in parity | Everything | |
| 72 | Picture block | A problem identified is half solved | Keynote, close | |
| 73 | Picture block | Move from activity-based focus | Sales | |
| 74 | Data | Execs are Unsatisfied (alternate) | | Duplicate of 10 |
| 75 | Framework | Emerging vs. Established Demand (alternate) | | Duplicate of 13 |
| 76 | Proof | What it is like to work with us (alternate) | | Duplicate of 41 |
| 77 | Proof | Results (hotel openings, RGI -5.3 to flat) | Hotel clients | Hotel version of 40 |
| 78 | Picture block | You can't give away what you don't have | Keynote, culture | |
| 79 | Framework | Customer-centric value chain (you / customer / customer's customer) | Sales | |
| 80 | Client example | Amadeus customer journey and value proposition | | Amadeus-specific |
| 81 | Picture block | Think Different | Keynote | |
| 82 | Framework | Customer value chain (want / care about / bring) | Sales | |
| 83 | Client example | Customer value chain, Marriott example | | Marriott-specific |
| 84 | Investment | Investment for Performance, FEI pricing ($8,250 Part 1) | Pricing layout reference | FEI prices; never send as is |
| 85 | Bio | Tristan Carty (photo and bio from kateburda.com/who-we-are) | Every proposal, right after Kate's bio (43) | |

## Team bios

Kate's bio (43) goes in every deck. **Tristan Carty is key (Kate, 2026.09.29)** and goes right after Kate: his bio is slide 85, so every spine reads 43, 85. Jawaria (46) and Sharla (45) go in only when they're involved in that engagement. David Garrard (44) stays out.

## Who uses it how

- **Jack (sales):** capabilities decks for first conversations and proposals that close. Proof slides (40, 41, 48) and the Forrester data (10) do the heavy lifting.
- **Maxell (marketing):** the frameworks (13, 16, 21, 71) become campaign and landing page angles, and the PNGs in `Individual Slides/` drop straight into emails.
- **Maya (writing):** picture blocks (61 to 73, 78, 81) are ready-made LinkedIn hooks and keynote openers. One slide, one post.

Before any deck goes to Kate, fix any flagged old details on the slides used (Kate's call: fix them when a slide gets used), and run it through the "Check before use" column and the voice rules in `my-business (context)/how-we-sound.md`.
