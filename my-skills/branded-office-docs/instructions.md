# Branded Office Docs

Set 2026.09.28, at Kate's direction: "For things I have to look at vs. you can you put them into a word doc vs. a markdown? ... Or excel. or ppt." Then: "How come you always forget the brand standards? ... Please use this for outputs."

Anything Kate reads goes to her as a branded Office file. The Office file is what Kate opens, so link to that one.

**No markdown files in the AI Brain** (Kate, 2026.10.06): "please don't use md files in the ai brain ... unless we are using it for developers." Write the markdown draft in the session's scratch folder, run the script there, then move only the finished `.docx` into the right `my-work (outputs)/` folder. Developer work is the exception: code, READMEs, and system files like skill instructions.

## Which format

- **Word:** reports, plans, write-ups, packing lists, schedules to read
- **Excel:** lists, trackers, checklists, anything with rows she'll tick off or sort
- **PowerPoint:** anything presented. Start from `my-files (knowledge)/Brand/Kate & Co- Administrative/3. PPT Template/kb_PPT-Template.pptx`

## Word, the one-step way

```
python3 "my-skills/branded-office-docs/branded_docx.py" "<file.md>"
```

**Two looks (Kate, 2026.09.28): "can you use kb & Co letter head for reports vs. the word doc. or if you use the word doc can you put the title on the first page the content starting the second?"**

- **Reports use the letterhead:** `python3 "my-skills/branded-office-docs/branded_docx.py" --letterhead "<file.md>"`. Built on `my-files (knowledge)/Brand/Kate & Co- Administrative/9. Envelopes & Letterhead/Letterhead.docx`: KB logo at the top and the contact line at the bottom of page 1, and the title starts right under the logo.
- **Memos and Word docs use the letterhead too** (Kate, 2026.10.06): "Can use letter head for memo and the .doc. Or ask me what you need to use for the output." So `--letterhead` is the default for anything in Word. If it's unclear which format or template an output needs, ask Kate before building.
- **Cover-page look, only when Kate asks for it:** the command without `--letterhead` uses the Word Template with a cover page. The title and the lines under it sit alone on page 1, and the content starts on page 2 at the first `##` heading.

Check the real pages by exporting to PDF through Word. Quick Look shows one long page and hides page breaks and bullets.

This writes `<file>.docx` next to the markdown, which is why the draft lives in the scratch folder: move the `.docx` into the AI Brain and leave the `.md` behind. It:
- uses the real KB&Co Word Template (logo, background, styles)
- forces Franklin Gothic Book everywhere
- colors headings PMS 675 (#B52372) and PMS 214 (#D51067)
- gives tables a PMS 675 header row with grey rules

**Bullets, when appropriate** (Kate, 2026.09.28): use real bullets for checklists, steps and parallel items. Keep explanations and reasoning as prose. In the markdown, leave a blank line before every list, or pandoc runs it into the paragraph above. The script turns the bullets into real Word bullets: a pink PMS 214 dot, then a dash, then a small circle for deeper levels, in Franklin Gothic.

Needs `pandoc` and `python-docx`, both installed on this Mac. Check the result with `qlmanage -t -s 1100 -o <dir> <file.docx>` and look at the PNG.

## Excel

Use openpyxl with these settings:
- Franklin Gothic Book throughout
- header row filled #B52372 with white bold text
- title in #B52372
- thin #A0A1A2 borders
- frozen header row, and a filter on lists
- a Yes/No dropdown for "done" or "packed" columns

## Ignite work uses Ignite's brand, not KB&Co's

See `my-business (context)/ignite-brand-standards.md`.

## Full brand spec

The palette, fonts and logo rules are in `my-business (context)/brand-standards.md`.
