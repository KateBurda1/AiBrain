# Right, or Just Lucky? Landing page, live draft record

**Built 2026.09.27 from the desktop (iMac), straight into kateburda.com. Both pages are DRAFTS. Nothing is published.**

| What | ID | Address once published | Edit | Preview |
|---|---|---|---|---|
| Landing page | 915 | kateburda.com/right-or-just-lucky | https://kateburda.com/wp-admin/post.php?post=915&action=edit | https://kateburda.com/?page_id=915&preview=true |
| Thank-you page (child of 915) | 916 | kateburda.com/right-or-just-lucky/thank-you | https://kateburda.com/wp-admin/post.php?post=916&action=edit | https://kateburda.com/?page_id=916&preview=true |

**Media uploaded:**
- Report PDF, media 912: https://kateburda.com/wp-content/uploads/2026/09/right-or-just-lucky-kate-burda-co.pdf (use in the thank-you page, done, and the Zoho confirmation email)
- Piece 1 GIF, media 913: https://kateburda.com/wp-content/uploads/2026/09/right-or-just-lucky-piece-1.gif (use in Touch 1 of the Zoho cadence)
- Coin image, media 914: https://kateburda.com/wp-content/uploads/2026/09/right-or-just-lucky-coin.png (landing and thank-you hero)

**Already on the page:** SEO title and description, the Zoho UTM tracking script (same as Built for the Climate), and a dashed "Zoho form goes here" box. Booking button on the thank-you page goes to https://calendly.com/kate7792/new-meeting.

**Local copy:** `wordpress-landing-page.html` (this folder). `preview-landing-page.png` is a full-page screenshot.

---

## Done 2026.09.27 (evening)

- Zoho Form **"Right or Just Lucky: Report Download"** built (duplicated from Built for the Climate). Permalink: https://forms.zohopublic.com/kateburdaandcompany1/form/RIghtorJustLuckyReportDownload/formperma/_PO-knGOLJpCLdAyJK5huytJ3x7ST3Axk33wYT-1afU
- Hidden field **Content Downloaded** = "Right, or Just Lucky" (visibility Hide). Same field added to the Built for the Climate form, value "Built for the Climate". It was missing there, so BT downloads were never tagged.
- CRM mapping: Content Downloaded mapped, Automation & Process Management ticked, on both forms. Lead Source stays mapped to utm_source (Kate's call).
- Redirect: https://kateburda.com/right-or-just-lucky/thank-you/ (parent window).
- Respondent email: subject "Your report: Right, or Just Lucky?", Kate's "Fair warning" line, link to the new PDF. Sign-off unchanged ("Enjoy! Kate Burda").
- Form iframe placed on page 915, replacing the dashed box.

## What's left, in order

1. **Zoho Form (Kate, in Zoho Forms).** Duplicate "Built for the Climate: Report Download" and rename it *Right, or Just Lucky: Report Download*.
   - Visible fields, all required: First Name, Work email, Company.
   - Hidden `content` default value: **Right, or Just Lucky**. Hidden `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` fill from URL parameters.
   - Zoho CRM integration: Contacts, update if the email exists. Map the hidden **Content Downloaded** field to **Content Downloaded**, and utm_medium, utm_campaign and utm_content to their UTM fields. **Kate's decision 2026.09.27: Lead Source stays mapped to utm_source** (shows "zoho" for cadence-email downloads; these contacts come from the email, not the web). Tick Actions > Automation & Process Management so workflow rules fire.
   - After submit: `https://kateburda.com/right-or-just-lucky/thank-you/`
   - Confirmation email subject: "Your report: Right, or Just Lucky?" Body: one warm line from Kate plus the PDF link above.
   - Button color `#D51067`, square corners.
   - Share > Embed: send Claude the iframe code. Claude swaps it into page 915 in place of the dashed box.
2. **Noindex the thank-you page (916)** in the SEO plugin, so it's only reached after the form. The connection here couldn't set it directly.
3. **Workflow rule in Zoho CRM** (Part 5 of the Zoho update package): `Content_Downloaded` = Right, or Just Lucky pulls the contact out of the cadence and starts the download follow-up.
4. **Test:** fill the form yourself, land on the thank-you page, get the email, check the Zoho contact fields.
5. **Publish both pages**, then link the landing page from the Insights page.

**Tracked links for every piece:** `kateburda.com/right-or-just-lucky/?utm_source=linkedin&utm_medium=social&utm_campaign=si-series&utm_content=piece-1` (LinkedIn) and `...?utm_source=zoho&utm_medium=email&utm_campaign=si-series&utm_content=piece-1` (email). Pieces 2 to 6 swap the last value.
