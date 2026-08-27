---
name: teach-me
description: Build or update a reusable skill. Use when you hear "teach it how to", "create a skill for", "make a new one for", "I want it to do", or "/teach-me".
---

# Teach Me

Builds new skills or updates existing ones for your assistant.

## How skills work

A skill is a folder in `my-skills/` containing an `instructions.md` file. Every skill also needs a matching file in `.claude/commands/` so you can type /name to use it.

```
my-skills/
└── skill-name/
    └── instructions.md
```

```
.claude/commands/
└── skill-name.md
```

The folder name and the file in .claude/commands/ must match.

## Step 1: Understand what they need

Ask these questions before writing anything:

1. What should we call this? (keep it short and simple)
2. What does it produce? (an email, a plan, a report, a document, etc.)
3. What would you type to use it? (e.g. /send-invoice, /write-welcome-email)
4. What does it need to know? (does it read client files, your tone of voice, external data?)

Do not start writing until these are answered.

## Step 2: Write the instructions.md

### Frontmatter (required)

```yaml
---
name: skill-name
description: [What it produces] + [When to use it, including trigger phrases]. Under 1024 characters.
---
```

**Good description:**
```
description: Drafts a client email in the company tone of voice. Use when you hear "write an email to", "draft an email", "email [client name]", or "send a message to".
```

**Bad description:**
```
description: Helps with emails.
```

The description must include BOTH what the skill does AND specific trigger phrases.

### Body structure

```markdown
# Skill Name

## Goal
One paragraph. What does a perfect output look like?

## Inputs
What does this skill need to do its job?

## Steps

### Step 1: [name]
What to do. What to produce. What to check.

### Step 2: [name]
...

## Output format
Where does the output go? What file name? What structure?

## Quality check
What to verify before finishing.
```

### Writing rules

- Short sentences. Simple words.
- Be specific. "Check the tone matches the brand" is vague. "Read my-business (context)/how-we-sound.md and match the writing rules listed there" is specific.
- Reference business files instead of copying them inline.

## Step 3: Write the slash command file

Create `.claude/commands/[skill-name].md`:

```markdown
Read `my-skills/skill-name/instructions.md` and follow it exactly.
```

This file must exist or the command will not work.

## Step 4: Update CLAUDE.md

Add the new skill to the "What you can ask for" section in `CLAUDE.md`:

```markdown
| /skill-name | What it does |
```

## Step 5: Confirm

Report back:
- Skill created at: `my-skills/[name]/instructions.md`
- Command file created at: `.claude/commands/[name].md`
- What triggers it
- What it produces

## Naming rules

- Lowercase with hyphens: `write-an-email`, `prep-a-meeting`
- No spaces, no capitals, no underscores
