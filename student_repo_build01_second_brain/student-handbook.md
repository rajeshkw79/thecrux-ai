# Build 1: Your Second Brain

**Duration:** 60 minutes | **Skill unlocked:** CLAUDE.md, file operations, context-driven AI

---

## What You'll Build

By the end of this session, you'll have:

1. Watched Claude read, analyze, and organize 20+ messy files in seconds
2. Built a personal **CLAUDE.md** that makes Claude understand who YOU are
3. Seen the dramatic before/after difference when Claude has your context
4. Created a **second brain** folder structure tailored to your role — ready for YOUR data
5. Tested it with a real-work question

**The big idea:** The same AI becomes dramatically more useful when you give it context about who you are. CLAUDE.md is the single highest-leverage file you'll create this weekend.

---

## Getting Started

Open your terminal and navigate to this repo:

```bash
cd student_repo_build01_second_brain
claude
```

If Claude Code isn't open yet, type `claude` to start a session.

---

## Part 1: Arjun's Mess — See What Claude Can Do (10 min)

There's a folder called `messy-workspace/` in this repo. It belongs to **Arjun Mehta**, a fictional VP of Product at a Series B SaaS company in Bangalore. 20+ files — meeting notes, budgets, client emails, to-do lists, Slack threads, half-finished drafts. Total chaos.

**Read `casestudy.md` first** to understand Arjun's situation and why this mess will feel familiar no matter your role.

### Step 1: Let Claude loose

Copy and paste this prompt into Claude:

```
Look at everything in the messy-workspace folder. Read the files and tell me:
what kind of professional left this mess? What are they working on? What seems urgent?
```

Watch what happens. Claude will read every file, analyze the contents, and paint a picture of Arjun's work life.

### Step 2: Organize it

```
Organize messy-workspace into a clean structure. Create folders, move files
where they belong, rename anything with a bad name. Create a table-of-contents
README when you're done.
```

When Claude asks permission to move files — say yes. That's the permission model at work. You're always in control.

### Step 3: Search across everything

```
What did the client from Acme Corp say about the timeline?
And what's the budget situation looking like for Q1?
```

Notice: you didn't tell Claude which file to look in. It searched everything and found the answer.

**What just happened:** Claude read 20+ files, understood their contents, reorganized them, and answered cross-file questions — all in under a minute. That's the power of file system access.

---

## Part 2: Build Your CLAUDE.md — The Before/After Moment (15 min)

Everything Claude just did was generic — the same output for everyone in the room. Now we change that.

**CLAUDE.md** is a special file that Claude reads automatically every time you start a session. It's your second brain's memory.

### The "Before" Snapshot

First, ask Claude this question and note the answer:

```
Write me a one-paragraph executive summary of what's happening
in Arjun's messy-workspace files. What should he focus on?
```

Save this output mentally — or scroll up to find it later. You'll compare it to the "after" version.

### Build YOUR CLAUDE.md through conversation

We're NOT writing CLAUDE.md by hand. Claude will interview you and build it.

```
I want to create my personal CLAUDE.md file. This will be saved at the root
of this project and will tell you who I am so every future conversation
is personalized.

Interview me to build this. Ask me about:
1. My role, industry, and what my company does
2. What I'm working on right now (top 2-3 priorities)
3. How I like information presented (bullets vs prose, formal vs casual, etc.)
4. What I want to use Claude for most

Ask 2-3 questions at a time. After I answer, ask the next batch.
When you have enough, create the CLAUDE.md file.
```

Spend about 8 minutes going through the interview. Answer with specifics from YOUR real work — the more real you are, the better Claude gets.

**Stuck on what to say?** Think: What did you do at work last Monday? What took too long? What do you wish someone else could handle?

### The "After" Moment

Now ask the same question about Arjun's files again — but this time, Claude knows who YOU are:

```
Now write me that executive summary of Arjun's messy-workspace files again.
But this time, frame it for ME — based on what you know about me from CLAUDE.md.
What would I care about most in Arjun's situation? What would I notice that
a generic summary would miss?
```

Compare the two answers. Same files. Same question. Completely different lens.

A sales person notices the Acme Corp renewal risk and the unsent ROI email. A finance person spots the over-budget cloud infra and the expiring vendor contract. A founder zeroes in on the board meeting prep and the competitive threat. A consultant sees 5 unfinished deliverables and a client at risk.

**That's the power of context.** The AI didn't get smarter. You gave it YOUR brain.

### Make it better

```
Read my CLAUDE.md and suggest 3 things I should add to make you more useful
to me. What's missing that would help you help me better?
```

This is the core loop: **build, test, iterate.** You'll use this pattern all weekend.

---

## Part 3: Build YOUR Second Brain (15 min)

Arjun's mess showed you what Claude can do with files. Your CLAUDE.md taught Claude who you are. Now let's build the actual system — **your** second brain. Not Arjun's. Yours.

This is an empty folder structure tailored to YOUR role, ready for you to start filling with your own files starting Monday.

### Create the structure

```
I want to set up a "my-second-brain" folder structure in this project.
Based on what you know about me from CLAUDE.md, create a directory
structure that would be useful for MY work and serve as my second brain, helping me organize my work.

Create the folders, add a README in each one explaining what goes there,
and create 2-3 starter templates that would be useful for my specific role.

Also update CLAUDE.md to include a section about this second brain —
where things live, what goes where, so you always know how to find things.
```

Notice how Claude uses YOUR CLAUDE.md to decide the folder structure. A PM gets different folders than a founder. A sales head gets a pipeline tracker template while a consultant gets a client engagement template.

### Seed it with something real

Your second brain is ready but empty. Let's put one real thing in it right now.

**Option A — Paste real notes:**

```
I'm going to paste some notes from a real meeting I had recently.
Save them in the right place in my second brain, and extract any
action items or follow-ups into the appropriate tracker.

[paste your real notes, a to-do list, or even a recent email thread]
```

**Option B — Dictate from memory:**

```
Here's a rough dump of what's on my plate right now:

[type out 3-5 things you're currently working on, worrying about,
or need to follow up on — just stream of consciousness, messy is fine]

Organize this into my second brain. Put things where they belong.
Create any files needed. Update my trackers.
```

**Option C — If you'd rather not use real data right now:**

```
Create a realistic sample set of 3-4 files for my second brain based on
what you know about my role from CLAUDE.md. Make them feel like things
I'd actually have — meeting notes, a project status, a to-do list.
Put them in the right folders.
```

### Test it

```
Based on everything in my second brain, what are the most important things
I should focus on this week? Where in my second brain can I find the
relevant files?
```

This is the moment it clicks — Claude searches your second brain, cross-references your files, and gives you a personalized answer with file references.

---

## Part 4: Make It Stick — The Monday Setup (10 min)

You have a CLAUDE.md, a second brain structure, and some real content in it. Let's make sure you actually use this on Monday.

### Set up your daily workflow

```
Add a section to my CLAUDE.md called "Daily Workflow" that describes how I
should use my second brain each day. Include:
- What to do when I start my day (morning review)
- How to capture notes during the day (just dump files in the right folder)
- What to do at end of week (weekly review)
```

### The Monday morning test

Think about what you'd actually face on Monday morning. Ask Claude:

**For PMs:**

```
I have a stakeholder review on Wednesday. Based on my second brain,
draft a 5-bullet status update covering my current projects.
Flag anything that looks like it needs escalation.
```

**For Founders:**

```
Summarize everything in my second brain that relates to revenue or customers.
What patterns do you see? What should I be worried about?
```

**For Sales / BD:**

```
I have 3 client calls this week. Based on what's in my second brain,
draft a prep brief for each — key talking points and open items.
```

**For Consultants:**

```
What deliverables are in progress? Draft a status update for my clients
based on what's in my second brain.
```

**For Finance / Ops:**

```
What are the open items that need approvals or decisions this week?
Flag anything overdue or at risk.
```

---

## What You Built

By now you should have:

- [ ] Experienced Claude reading and organizing Arjun's 20+ files
- [ ] A personal **CLAUDE.md** tailored to your role and work
- [ ] Seen the before/after — how context transforms Claude's output
- [ ] A **my-second-brain** folder structure with READMEs and role-specific templates
- [ ] At least one real piece of content seeded into your second brain
- [ ] A **Daily Workflow** section in CLAUDE.md
- [ ] Tested asking Claude a real Monday morning question

**This carries forward into every session today.** Your CLAUDE.md grows with each build — by the end of the day, Claude will know your voice (Build 3), your tools (Build 4), and ship products for you (Build 5).

---

## Take It Home: Making This Permanent

Everything you built today lives inside this bootcamp repo - now that you have cloned it, we will make this repo private. Here's how to make it part of your actual daily life.

### How CLAUDE.md actually works

Claude Code automatically reads CLAUDE.md files every time you start a session. No special command needed. It checks three levels:


| Level                  | Location                                        | When it loads                | Put what here                                                   |
| ------------------------ | ------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------- |
| **Global**             | `~/.claude/CLAUDE.md`                           | Every session, in any folder | Who you are — role, industry, preferences, communication style |
| **Project**            | `CLAUDE.md` in the folder you run `claude` from | Only in that folder          | Project-specific context — folder map, workflows, rules        |
| **Parent directories** | Any`CLAUDE.md` in folders above you             | Inherited by child folders   | Shared context for related projects                             |

### What makes a great CLAUDE.md

A vague CLAUDE.md gives you vague output. A specific one gives you output that feels like it came from someone who's worked with you for months. Here's what to aim for.

**For your personal / global CLAUDE.md (`~/.claude/CLAUDE.md`):**

This is your identity file. It should answer: "If a brilliant new colleague joined my team today, what would I tell them about me in the first 30 minutes?"

**Include:**

- **Who you are** — Role, company, industry, team size, who you report to, key stakeholders. Not a resume — a working context. "I'm VP Sales at a mid-size auto dealership group in Tamil Nadu, managing 14 salespeople across 3 showrooms. I report to the MD."
- **What you're working on right now** — Your top 2-3 priorities this quarter. Update this as priorities shift. "Biggest priority: improve conversion rate on walk-ins. Second: launch the used car vertical. Third: prep for the annual dealer conference in April."
- **How you think and communicate** — Bullets or prose? Formal or direct? Do you want options or recommendations? "Give me bullet points, not paragraphs. Be direct — tell me what's wrong, not just what's working. When there are tradeoffs, show me a comparison table."
- **What you DON'T want** — This is underrated. "Don't give me generic advice. Don't sugarcoat problems. Don't write in a corporate tone — I talk like a real person."
- **What you use Claude for most** — Helps Claude calibrate its responses. "I mostly use Claude for: prepping for meetings, drafting client emails, analyzing sales data, and brainstorming strategy."

**Don't include:**

- Your full career history (Claude doesn't need your resume)
- Generic statements like "I value quality" (everyone does — this adds nothing)
- Things that change daily (put those in project-level CLAUDE.md)

**For a project CLAUDE.md (in any project folder):**

This is the operating manual for a specific project or workspace. It should answer: "If I handed this project folder to a smart colleague, what would they need to know to be useful immediately?"

**Include:**

- **What this project/folder is** — One-liner. "This is my second brain — a personal knowledge management system for my work files."
- **Folder structure** — What lives where. Claude uses this to file things correctly and find things fast. "meetings/ has meeting notes named YYYY-MM-DD-topic.md. clients/ has one subfolder per client. inbox/ is for unsorted captures."
- **Naming conventions** — How files should be named, how dates should be formatted. "All meeting notes start with the date: 2026-03-06-weekly-standup.md"
- **Workflows** — What you want Claude to do when you give it certain types of tasks. "When I dump files in inbox/, sort them into the right folders, extract action items, and update the todo tracker."
- **Rules and guardrails** — Things Claude should always or never do in this project. "Never delete files without asking. Always create a backup before reorganizing. When in doubt, ask me."
- **Key context** — Important information that shapes how Claude should work here. "Acme Corp is our biggest client (45L/year), renewal is at risk. Anything related to Acme is high priority."

**The golden rule: specificity beats length.** Five specific lines are worth more than fifty generic ones. "I'm a PM" tells Claude almost nothing. "I'm a PM at a Series B edtech startup, building a course recommendation engine, reporting to the CTO, and my biggest challenge is getting engineering bandwidth" — that's a CLAUDE.md that works.

**Keep it alive.** Your CLAUDE.md should change as your work changes. When you start a new project, update it. When your priorities shift, update it. When Claude gives you output that misses the mark, ask yourself: "What context was I assuming it had?" — then add it to CLAUDE.md.

### The setup that works

**Step 1: Create your global CLAUDE.md**

This is the "who I am" file. It follows you everywhere.

```bash
mkdir -p ~/.claude
```

**Can't find the `.claude` folder in Finder / File Explorer?** Folders starting with a dot are hidden by default on Mac and Windows. Your OS hides them so you don't accidentally break config files. They're there — you just can't see them.

- **Mac Finder:** Press `Cmd + Shift + .` to show hidden files
- **Windows Explorer:** View > Show > Hidden items
- **Terminal:** `ls -a` always shows them (the `-a` flag means "all, including hidden")

Then ask Claude:

```
Take the personal sections from my current CLAUDE.md (my role, priorities,
preferences, communication style) and save them to ~/.claude/CLAUDE.md.
This will be my global identity file that loads in every Claude session.
```

**Step 2: Set up your second brain as a real folder**

Move your second brain out of the bootcamp repo and into your actual file system:

```bash
mkdir -p ~/my-second-brain
```

Then ask Claude:

```
Copy my-second-brain folder structure (with all READMEs and templates)
to ~/my-second-brain/. Create a CLAUDE.md there with just the folder map
and daily workflow sections — the project-specific stuff.
```

**Step 3: Use it**

From Monday onwards:

```bash
cd ~/my-second-brain
claude
```

Claude now loads your global identity (`~/.claude/CLAUDE.md`) AND your second brain's operating manual (`~/my-second-brain/CLAUDE.md`). It knows who you are and where everything lives. Just start talking.

### The daily habit

- **Morning:** `cd ~/my-second-brain && claude` then ask "What should I focus on today?"
- **During the day:** Dump files, notes, ideas into the right folders (or just dump them in and ask Claude to sort them)
- **End of week:** Ask Claude to create a weekly summary

That's it. The system works because CLAUDE.md loads automatically and your files are always there. No setup, no remembering, no friction.

### The inbox trick: capture now, organize later

Add one more folder to your second brain: **`inbox/`**

This is your dumping ground. Everything goes here first — no thinking about where it belongs. Then once a day (or whenever it gets full), ask Claude to sort it.

**The workflow:**

1. Drop anything into `inbox/` — meeting notes, screenshots, copy-pasted email threads, voice memo transcriptions, random thoughts, PDFs
2. Run one prompt:

```
Process my inbox. Read everything in the inbox/ folder, file each item
into the right second brain folder, extract any action items or follow-ups
into my trackers, and empty the inbox when you're done.
```

3. Inbox is clean. Everything is filed. Action items are tracked.

This is the same "messy files to organized structure" magic you saw with Arjun's workspace — except now it's YOUR stuff, and you do it daily.

**What can go into the inbox:**


| What you capture                            | How to get it there                                                                                                           |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Meeting notes (Granola, Otter, etc.)        | Set your transcription app's export folder to`~/my-second-brain/inbox/` — notes land there automatically after every meeting |
| Voice memos                                 | Transcribe on your phone, paste into a text file in inbox                                                                     |
| Email threads                               | Copy-paste into a text file in inbox                                                                                          |
| Screenshots of whiteboards, designs, errors | Drop the image file in inbox — Claude can read images                                                                        |
| WhatsApp or Slack threads                   | Copy-paste the conversation into inbox                                                                                        |
| Articles or web clippings                   | Save or paste into inbox                                                                                                      |
| Scanned documents or PDFs                   | Drop in inbox — Claude reads PDFs                                                                                            |
| Random thoughts or ideas                    | Just create a quick text file in inbox                                                                                        |

**The key insight:** You don't need to organize in the moment. Just capture. Let Claude do the sorting later. The friction of "where does this go?" is what kills most note-taking systems. The inbox eliminates that friction.

---

## If You Finish Early

Push Claude further:

```
Read my CLAUDE.md and my second brain. Tell me 3 insights about my work
that I might be missing. What patterns do you see that I should pay attention to?
```

Or pair up with someone nearby. Compare your CLAUDE.md files — what did they include that you didn't? Steal good ideas.

---

## Key Takeaway

> CLAUDE.md is the highest-leverage thing you'll build this weekend. Ten minutes now saves you hours every week. Same AI + your context = a completely different experience.
