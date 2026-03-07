# The Conceptual Map: What Just Happened in Build 0

**Reading time:** 10 minutes | **When to read:** After completing Build 0

---

You just spent 40 minutes doing things with Claude Code. This document explains *why* those things worked the way they did — the mental models that make everything click.

---

## 1. Claude Code is not a chatbot

Most people's experience with AI looks like this: you open a website, type into a text box, get a response, copy-paste it somewhere useful. The AI lives in a browser tab. It can't see your files. It can't touch your computer. It's a conversation in a box.

Claude Code is fundamentally different. It runs in your terminal — the same place your operating system lives. This gives it three capabilities that browser-based AI doesn't have:

| Capability | What it means | What you saw in Build 0 |
|-----------|--------------|------------------------|
| **File access** | Claude can read, create, and edit files on your machine | It read 6 business files, created a meeting summary, cleaned up messy action items |
| **System access** | Claude can run terminal commands on your computer | It checked your battery, found CPU-heavy processes, mapped your directories |
| **Persistent workspace** | Claude works *inside* a folder on your machine, with real files that stay after the session ends | The files Claude created are still there — open Finder and check |

This isn't a small difference. It's the difference between an AI that *talks about* your work and an AI that *does* your work.

---

## 2. The permission model: you are the decision-maker

Here's the deal Claude Code makes with you:

> **Claude proposes. You approve. Nothing happens without your say-so.**

Every time Claude wants to do something — read a file, create a file, edit a file, run a command — it asks you first. You saw this repeatedly in Build 0. That permission prompt is not a formality. It's the core design principle.

Think of it like a senior colleague who drafts things for you. They write the email, prepare the analysis, reorganize the data — but they put it on your desk for review before sending anything. You can approve, reject, or redirect.

This model has three levels:

```
Ask every time     →  Maximum control, default for most actions
Allow for session  →  "I trust you on this type of action for now"
Always allow       →  "You can always do this in this project"
```

Start with "ask every time." As you build trust, you'll loosen the controls. But the principle never changes: **you are always the decision-maker, Claude is always the executor.**

---

## 3. Context is the lever — not prompting tricks

There's a common misconception that getting good results from AI requires special prompting techniques — magic words, specific formats, clever tricks. That's mostly wrong.

The real lever is **context**. You experienced this directly in Build 0:

**Without context:**
```
Summarize the vendor comparison
```
→ You get a generic summary. Accurate, but useless for decision-making.

**With context:**
```
Summarize the vendor comparison. I'm Kavita, the CEO. We have 10 months
of runway, the migration is already delayed, and I need to make a vendor
decision this week. What do you recommend and why?
```
→ You get a decision-oriented recommendation weighted by urgency, runway, and risk.

Same AI. Same files. Completely different output. The difference is context — who you are, what you care about, what decision you're trying to make.

This is the single most important idea in this entire bootcamp:

> **The quality of Claude's output is directly proportional to the context you give it.**

In Build 1, you'll learn how to make this context *permanent* so you never have to repeat yourself. But the principle starts here.

---

## 4. The conversation is a workspace, not a Q&A

In a chatbot, each message is basically independent. You ask, it answers, you ask again. The conversation is a series of one-off exchanges.

In Claude Code, the conversation is a **workspace**. Claude remembers everything you've discussed. You build on previous responses. You refine, redirect, and iterate.

You experienced this when you asked for key risks in 3 bullets, then said "now do the same for Neha's email." Claude understood "the same" because it remembered the format you asked for. Then you said "make it shorter" and it knew what "it" referred to.

This changes how you should work:

| Old habit (chatbot thinking) | New habit (workspace thinking) |
|------------------------------|-------------------------------|
| Write a perfect prompt upfront | Start with a rough ask, then refine |
| If the output is wrong, rewrite the whole prompt | Say what to change: "make it shorter" / "remove the third point" |
| Each question is standalone | Build on previous responses |
| Start over when stuck | Use `/clear` only when truly stuck, not as a first resort |

The practical rule: **if Claude gives you something 70% right, iterate. Don't restart.** Three quick follow-ups ("make it more formal," "add a risk section," "change the recommendation") are faster and better than one perfect prompt.

---

## 5. The control panel: what each command actually does

You learned several slash commands. Here's the mental model for when to use each one:

### Awareness commands — "What's going on?"

- **`/cost`** — How much have I spent this session? (tokens used)
- **`/usage`** — Am I hitting my plan limits? (daily/weekly quota)
- **`/context`** — Is Claude's memory getting full? (context window usage)

Think of these as dashboard gauges. Glance at them periodically, especially when Claude starts feeling slow or forgetful.

### Session commands — "Reset or refresh"

- **`/compact`** — Claude's memory is getting full but the conversation is still useful. Compress it — keep the key points, drop the verbose details. Like summarizing your notes instead of throwing them away.
- **`/clear`** — Nuclear reset. Claude forgets everything. Use when you're switching tasks or Claude is genuinely confused. Don't use this just because one response was bad — try redirecting first.

The progression: try redirecting → try `/compact` → use `/clear` as a last resort.

### Control commands — "Change how Claude works"

- **`/model`** — Switch between AI models with different speed/depth tradeoffs:
  - **Haiku** — Fast, lightweight. "What's in this file?" "Format this list."
  - **Sonnet** — Balanced. Your daily driver for most work.
  - **Opus** — Deep, thorough. Complex analysis, important deliverables, cross-file reasoning.
- **`/permissions`** — Check and change what Claude is allowed to do.
- **`/sandbox`** — Read-only mode. Claude can look but can't touch. Great for exploring sensitive files.

### Diagnostic commands — "Something is broken"

- **`/doctor`** — Self-diagnosis. Checks installation, settings, connectivity. Run this before panicking.

---

## 6. Your file system is Claude's world

This is the concept that causes the most confusion, so let's be explicit:

**Claude Code sees the folder you're in.** When you run `claude` from a directory, that directory becomes Claude's workspace. It can read files there, create files there, and navigate from there.

This means:
- If you run `claude` from your home directory (`~`), Claude can see *everything* — documents, downloads, desktop, hidden files. That's messy and potentially risky.
- If you run `claude` from a dedicated project folder, Claude sees only that project. Clean and focused.

The habit you learned:

```
mkdir → cd → claude
```

This isn't just organization advice. It's a **scope control**. You're deciding what Claude can see before you start working. A dedicated folder means Claude focuses on the right files, doesn't accidentally read things you didn't intend, and keeps its outputs contained.

```
~/claude-projects/
├── serious/          ← Long-running work (client projects, team planning)
├── casual/           ← Experiments and learning
└── adhoc/            ← Quick one-off tasks (summarize a report, draft an email)
```

When something goes wrong — "Claude can't find my file," "Claude is reading the wrong document," "Where did that file go?" — the answer is almost always: **check what folder you're in.** Run `pwd`. That's your diagnostic.

---

## 7. The six rules, and why each one matters

You learned six prompting rules in Build 0. Here's the *why* behind each:

### 1. Be specific
Claude is literal. "Look at the CSV" gives you a description of the CSV. "Flag metrics where Q1 actuals are worse than target and tell me which should worry a CEO" gives you actionable analysis. Specificity isn't about being verbose — it's about telling Claude what *output* you want, not just what *input* to look at.

### 2. Give context
Claude has no idea who you are, what you care about, or what decision you're making — unless you tell it. Context acts as a filter. It tells Claude what to emphasize, what to skip, and what lens to use. "I'm the CEO with 10 months of runway" produces completely different output than "I'm the engineering lead worried about migration timelines."

### 3. Iterate, don't restart
Every time you restart a conversation, you lose context. Claude forgets your preferences, your previous requests, the direction you were heading. Iteration preserves all of that. Say "make it shorter" instead of writing a new prompt that says "give me a short version of..."

### 4. /clear when stuck
Sometimes Claude gets into a loop — repeating itself, giving circular answers, misunderstanding your intent. This usually means the conversation context has become confusing. `/clear` gives you a fresh start. But try redirecting first — `/clear` is expensive because you lose everything.

### 5. Check your directory
`pwd` is the most useful debugging command you'll ever learn. It tells you where you are. Most "Claude can't find my file" problems are actually "I'm in the wrong folder" problems.

### 6. Approve carefully
The permission model only protects you if you actually read what Claude is proposing. When Claude shows you a file edit, look at what's changing. When it proposes a terminal command, make sure you understand what it does. "What will this command do?" is always a valid question.

---

## The mental model to carry forward

Here's the one-sentence version of everything above:

> **Claude Code is a capable collaborator that works inside your file system, proposes actions for your approval, and gets dramatically better when you give it context about who you are and what you need.**

In Build 1, you'll learn how to make that context permanent — so Claude remembers who you are, what you care about, and how you like things done, every single time you start a session. That's where it goes from impressive to indispensable.

But the foundation is what you built today: you know how to read, write, edit, control, and communicate with Claude Code. Everything else builds on this.

---

*This document is a reference. Come back to it whenever you need a reminder of how Claude Code works and why it works that way.*
