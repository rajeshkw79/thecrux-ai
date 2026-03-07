# Build 0: Claude Start

**Duration:** 40 minutes | **Skill unlocked:** file reading, file creation, file editing, slash commands, permissions, workspace hygiene, conversation flow

---

## What You'll Build

- [ ] Read and explore real business files using Claude Code
- [ ] Create new documents and clean up messy ones
- [ ] Master the slash commands and controls that make you fast
- [ ] Set up a clean workspace habit that prevents headaches later
- [ ] Learn the prompting patterns that get great results (and the ones that don't)

## The big idea

Claude Code reads, writes, and edits files on your machine — you just tell it what you need in plain language, and it does the work while you stay in control.

## Learning Goals

- **Read and comprehend** — See how Claude reads entire files, connects information across documents, and answers questions about your business content
- **Create and edit** — Experience Claude writing new files and improving existing ones, with you approving every change
- **Control the tool** — Learn the slash commands, permissions, and shortcuts that keep your workflow smooth and efficient
- **Organize your workspace** — Build the folder hygiene habit that prevents the #1 source of confusion with Claude Code

## Getting Started

### Missed the pre-bootcamp setup?

If you didn't create the bootcamp folder yesterday, do it now:

**Mac/Linux:**
```bash
mkdir ~/thecrux-ai-bootcamp
```

**Windows (PowerShell):**
```powershell
mkdir $HOME\thecrux-ai-bootcamp
```

Once created, continue with Step 1 below.

---

### Step 1: Open your terminal and navigate to the bootcamp folder

**Mac/Linux:**
```bash
cd ~/thecrux-ai-bootcamp
```

**Windows (PowerShell):**
```powershell
cd $HOME\thecrux-ai-bootcamp
```

### Step 2: Confirm you're in the right place

```bash
pwd
```

You should see something like `/Users/yourname/thecrux-ai-bootcamp`. If you see your home directory or something else, run the `cd` command above again.

### Step 3: Start Claude Code

```bash
claude
```

You should see Claude's prompt waiting for your input. You're in.

### Step 4: Clone the session repo

Now ask Claude to clone the practice files for this session:

```
Let's clone this repo here - https://github.com/thecrux-ai/student_repo_build00_claude_start
```

Claude will ask for permission to run a git command — approve it. Once it's done, you'll have a new folder called `student_repo_build00_claude_start` with all the files you need for this session.

### Step 5: Move into the repo folder

```
Navigate into the student_repo_build00_claude_start folder we just cloned
```

Claude will `cd` into the folder. Now all the practice files are accessible and you're ready to go.

### Choose your mode

You have two ways to do this session:

**Guided mode** — Type `guide me` and Claude walks you through each step. Just say "next" to move forward. Great if this is your first time.

**Self-paced mode** — Follow this handbook at your own speed. Copy-paste the prompts below into Claude. If you get stuck, just ask Claude for help.

You can switch anytime during the session — say "guide me" to hand over control, or "I'll drive" to go solo.

---

## Part 1: First Flight — Read and Explore (10 min)

The goal here is simple: see Claude read and understand your files. Not just list them — actually comprehend what's inside.

### Step 1: Read a single file

Start by asking Claude to read the leadership team's meeting notes.

```
Read the file practice-files/team-meeting-notes.md and give me a quick summary of the key decisions
```

Claude will read the entire file and summarize the decisions — the hiring freeze, the Acme renewal, the migration delay, the board deck deadline. Notice that it doesn't just quote the file back at you. It understands the content.

### Step 2: Explore the whole folder

Now ask Claude to look at everything.

```
Look at all the files in the practice-files/ folder and tell me what we're working with
```

Claude will read every file — the CSV, the markdown docs, the messy text file, the email — and give you a map of what's there. Six files about the same company, the same team, the same set of challenges.

### Step 3: Ask a cross-file question

This is where it gets interesting. Ask something that requires connecting dots across files.

```
What's the connection between the vendor comparison and the issues discussed in the meeting notes?
```

Claude will link Priya's migration delay (meeting notes) to the vendor comparison details — the timeline differences, the CloudServ proposal expiring, Ravi's cost concerns against the burn rate problem. Information that lives in two separate files, connected in seconds.

> **What just happened?** You didn't copy-paste anything. You didn't open a single file yourself. Claude read six files, understood the business context — a Series B SaaS company with cash pressure, a delayed migration, a competitor threat, and a team stretched thin — and answered questions that required synthesizing information across documents. This is what "AI-assisted work" actually looks like.

### Step 4: Beyond files — Claude talks to your computer

Here's where it gets really interesting. Claude Code doesn't just read files — it can access your underlying operating system. It can run terminal commands, inspect your system, and answer questions about your actual machine.

Try these — one at a time:

**Check your battery health:**

```
Show me the health of my battery — current charge, cycle count, and overall condition
```

Claude will run the appropriate system command, read the output, and explain it in plain English. No googling for terminal commands. No Stack Overflow.

**Find what's straining your computer:**

```
Which services are consuming the most CPU right now? Is anything straining my computer?
```

Claude will check your running processes and tell you what's eating resources — maybe Chrome with 47 tabs, maybe a runaway process you didn't know about.

**Search across your system:**

```
Search my system and find my user profile — where are my documents, downloads, desktop? Give me a map of my home directory.
```

**Check your downloads folder:**

```
How much space is my Downloads folder taking up? What are the biggest files in there?
```

**Find duplicates:**

```
Are there any duplicate files in my Downloads folder? Files with the same name or same size that might be copies.
```

**Audit your applications:**

```
What software or applications got installed on my computer in the past 90 days?
```

Claude will dig through your system to find recently installed apps — you might be surprised by what's there.

```
What are the applications on my computer that I haven't used in the last 90 days?
```

This one's gold for a digital cleanup. Claude will find the apps collecting dust — the ones you installed for "that one thing" six months ago and never opened again.

> **What just happened?** Claude isn't a chatbot trapped in a text box. It has access to your operating system. It can run any terminal command, read the output, and explain it to you. You didn't need to know a single terminal command — you asked in plain English and Claude figured out the right commands to run. This is the real power: Claude as your system-aware assistant, not just a file reader.
>
> **A note on permissions:** You'll notice Claude asks permission before running system commands, just like it does for file edits. Always read what it's proposing to run. For these exercises, everything is safe — but the habit of reviewing before approving matters.

---

## Part 2: Claude Takes Action — Create and Edit (10 min)

Reading is impressive. But now we let Claude write. This is where you'll see the permission model in action — Claude proposes changes, and you decide whether to approve them.

### Step 1: Create a new document

Ask Claude to produce something new from the meeting notes.

```
Create a file called practice-files/meeting-summary.md with a clean executive summary of the leadership meeting. Include: key decisions, owners, deadlines, and open risks. Format it so I could share it with the board.
```

Claude will draft the file and show you what it wants to write. You'll see a prompt asking you to approve the file creation. Read what it's proposing, then approve it.

### Step 2: Improve an existing document

The draft proposal has open questions and gaps. Ask Claude to strengthen it.

```
Read practice-files/draft-proposal.md and improve it. Fill in the open questions with reasonable recommendations, add a timeline visualization, and make the budget section more specific. Keep Arjun's voice.
```

Claude will show you the proposed edits. This time, pay attention — it's modifying an existing file. You can see exactly what changes it wants to make before you say yes.

### Step 3: Clean up messy data

The action items file is a mess — scattered notes, personal reminders mixed with work tasks, no structure. Ask Claude to fix it.

```
Read practice-files/action-items.txt and create a clean, organized version at practice-files/action-items-organized.md. Group by meeting source, add owners and deadlines where they're mentioned, and flag which items are work vs personal.
```

### Step 4: Undo it — Reverting changes

You just watched Claude edit a file. But what if you didn't like the changes? What if Claude went too far, or you want the original back?

This is where `/rewind` comes in. It's your undo button — not just for the conversation, but for the files too.

Try it now:

```
/rewind
```

You'll see a list of previous points in your conversation. Use the arrow keys to pick the moment *before* Claude edited the draft proposal (Step 2). When you select it, Claude will ask if you want to **also undo the file changes** made after that point. Say yes.

Now check the file:

```
Read practice-files/draft-proposal.md — is this the original version or the edited one?
```

It's back to the original. The edits are gone. You just time-traveled.

**When to use `/rewind`:**
- Claude edited a file and you don't like the result
- You went down the wrong path three prompts ago and want to back up
- You approved something by accident and want to undo it

**`/rewind` vs `/clear`:** `/clear` wipes your conversation but leaves files as they are. `/rewind` goes back to a specific point and can undo file changes too. `/rewind` is surgical; `/clear` is a reset.

> **What just happened?** Claude created a new file, edited an existing one, transformed messy data into something structured — and then you learned to undo it all. Every change Claude makes is reversible. You are never locked in. The permission model means Claude proposes and you approve. `/rewind` means even after you approve, you can take it back. You are always in control.

---

## Part 3: Your Control Panel — Commands, Permissions, and Workspace (10 min)

Now that you know Claude can read and write, let's learn the full control panel. This is what separates someone who "uses Claude" from someone who's *fast* with Claude.

### Essential Slash Commands

Try each of these right now:

**`/help` — See everything available:**

```
/help
```

This shows you every command Claude Code supports. Scan it. You don't need to memorize it — just know it's there.

**`/cost` — Check your session spend:**

```
/cost
```

Shows token usage for this session. Good habit to build.

**`/usage` — Check your plan limits:**

```
/usage
```

This is different from `/cost`. `/cost` shows this session's tokens. `/usage` shows your overall plan limits and rate status — how much of your daily/weekly quota you've used. Check this if Claude suddenly feels slow (you might be rate-limited).

**`/context` — See what's eating your context:**

```
/context
```

This shows a visual grid of your context window — how much is filled, what's taking space. When Claude starts feeling "forgetful" or slow, this tells you why. If it's nearly full, time to `/compact` or `/clear`.

**`/compact` — Compress your conversation:**

```
/compact
```

This summarizes your conversation history to free up context space. Claude keeps the key points but drops the verbose details. Use this when your context grid looks full.

**`/clear` — Fresh start:**

```
/clear
```

Wipes the conversation completely. Claude forgets everything. Use this when Claude seems confused, when you're switching tasks, or when you want a clean slate. Your files are untouched.

**`/model` — Switch models or adjust effort:**

```
/model
```

This lets you switch between different Claude models. You'll see a list — use arrow keys to select. Some models also support **effort levels** (use left/right arrows to adjust).

**Try this experiment** to see the difference:

First, ask Claude a question at normal settings:

```
Based on the quarterly metrics, what's the single biggest red flag for this company?
```

Note the answer and how long it took. Now switch to a faster, lighter model:

```
/model
```

Select **Haiku** (the fastest model) from the list. Then ask the exact same question:

```
Based on the quarterly metrics, what's the single biggest red flag for this company?
```

You'll notice: Haiku answers in a fraction of the time, but the analysis is shallower. It might catch the obvious red flag (churn spike) but miss the nuance (connecting it to CompetitorX pressure and the burn rate trend).

Now switch back to the more powerful model:

```
/model
```

Select **Sonnet** or **Opus** (whichever you started with).

**The mental model:**
- **Haiku** — Fast, cheap. Great for quick lookups, simple formatting, "what's in this file?" questions
- **Sonnet** — Balanced. Good default for most work
- **Opus** — Most thorough. Use for complex analysis, cross-file reasoning, important deliverables

You don't need to switch models constantly. But knowing you CAN is powerful — especially when you're burning through your daily quota on simple tasks that Haiku could handle.

**`/doctor` — Self-diagnose problems:**

```
/doctor
```

If something feels broken — Claude won't launch, commands don't work, connections fail — run `/doctor`. It checks your installation, settings, and connectivity and tells you what's wrong.

### Understanding Permissions

When Claude wants to read a file, create a file, edit a file, or run a command, it asks you first. This is the permission model. You've already seen it in Part 2.

Check your current permission settings:

```
/permissions
```

You'll see what Claude is currently allowed to do. There are different levels:

- **Ask every time** — Claude asks permission for each action (default for most things)
- **Allow for this session** — You approve once, Claude can repeat similar actions without asking again
- **Always allow** — Permanent permission for this type of action in this project

For now, stick with the defaults. As you get comfortable, you'll learn when it makes sense to give broader permissions. The key thing: **you can always check and change permissions with `/permissions`**.

> **Tip:** When Claude asks permission and you see the options, look carefully. You might see "Allow once", "Allow for session", or "Always allow". During this bootcamp, "Allow once" or "Allow for session" is fine. Don't "Always allow" until you're confident about what you're approving.

### Sandbox Mode — The Safety Net

```
/sandbox
```

Sandbox mode restricts Claude from making changes to your file system. It can read files and answer questions, but it can't create, edit, or delete anything. Think of it as "read-only mode."

**When to use sandbox:**
- When you're exploring files and don't want accidental changes
- When you're working with important files and want to be extra careful
- When you just want to ask questions without Claude touching anything

Toggle it on, ask a question, toggle it off when you're ready to let Claude take action again.

### Keyboard Controls

| Key | What it does |
|-----|-------------|
| `Escape` | Cancel Claude mid-response |
| `Ctrl+C` | Hard stop / exit Claude |

Try this now — ask Claude something long and hit `Escape` while it's responding:

```
Write me a very detailed 2000-word analysis of our quarterly metrics
```

Hit `Escape` after a few seconds. Claude stops immediately. Nothing gets saved. You're in control.

### Multi-turn Conversations

Claude remembers your conversation. You don't need to repeat yourself. Try this sequence:

```
Summarize the key risks from the meeting notes in 3 bullet points
```

Wait for the response. Then:

```
Now do the same thing but for the email from Neha
```

Claude knows "the same thing" means "summarize the key risks in 3 bullet points." It carries context forward. This is how you work fast — build on previous responses instead of starting from scratch.

### Correcting Claude

If Claude gives you something that's not quite right, don't re-prompt from zero. Just redirect:

```
Make it shorter — just one line per risk, no explanations
```

Or be specific about what to change:

```
No, remove the third point and add something about the pricing pressure instead
```

Claude takes direction well. Treat it like a sharp colleague who drafted something — you'd say "change this part," not repeat the whole brief.

> **What just happened?** You now know the full control panel: commands to check usage (`/cost`, `/usage`, `/context`), commands to manage your session (`/clear`, `/compact`), commands to control Claude (`/model`, `/permissions`, `/sandbox`), and commands to troubleshoot (`/doctor`). Plus keyboard controls and multi-turn conversations. You're not a passenger anymore — you're the pilot.

---

## Part 4: The Gotcha Guide — Best Practices (10 min)

This is the part that saves you frustration for the rest of the weekend.

### Workspace Hygiene — The #1 Habit

Before we talk about prompts, let's talk about where you work. This is the single most important habit for avoiding confusion with Claude Code.

**The rule: Always create a dedicated folder for your work. Never work from your home directory or desktop.**

Here's the setup that works:

```
~/claude-projects/           <-- Your top-level Claude workspace
├── serious/                 <-- Long-running projects, important work
│   ├── q1-board-prep/
│   ├── client-proposals/
│   └── team-planning/
├── casual/                  <-- Experiments, learning, exploration
│   ├── bootcamp-practice/
│   └── try-new-things/
└── adhoc/                   <-- Quick one-off tasks
    ├── summarize-report/
    └── draft-email/
```

**Why this matters:**
- Claude reads files in your current directory. If you're in your home folder, it might read things you don't want it to.
- Each folder can have its own CLAUDE.md (you'll learn about this in Build 1), giving Claude different context for different projects.
- When something goes wrong, the first question is always "where am I?" — `pwd` — and a clean structure makes the answer obvious.

**The habit:** Before starting any Claude session, always:

```bash
pwd                          # Where am I?
mkdir -p ~/claude-projects/adhoc/my-task   # Create a folder if needed
cd ~/claude-projects/adhoc/my-task         # Go there
claude                       # Then start Claude
```

You'll thank yourself later. Every "file not found" error, every "Claude is reading the wrong files" confusion — almost all of it traces back to not being in the right directory.

### Do This, Not That

**1. Be specific, not vague**

Bad prompt:

```
Look at the csv
```

Good prompt:

```
Read practice-files/quarterly-metrics.csv and flag any metrics where Q1 actuals are significantly worse than target. Tell me which ones should worry a CEO preparing for a board meeting.
```

Try both. See the difference in what you get back.

**2. Give context — it changes everything**

Without context:

```
Summarize the vendor comparison
```

With context:

```
Summarize the vendor comparison. I'm Kavita, the CEO. We have 10 months of runway, the migration is already delayed, and I need to make a vendor decision this week. What do you recommend and why?
```

The second prompt gives Claude a lens. It knows what matters to you. Try both and compare the outputs.

**3. Iterate, don't restart**

When Claude gives you a draft that's 80% right, don't write a brand new prompt. Build on it:

```
Good, but make the recommendation section more decisive. I don't want "consider" — I want "we should do X because Y."
```

```
Add a one-paragraph risk section at the end.
```

```
Make the tone more formal — this is going to the board.
```

Each follow-up is a 5-second prompt that gets you closer. Restarting from scratch wastes context and time.

**4. Use /clear when Claude seems stuck**

If Claude starts repeating itself, giving circular answers, or seems confused — don't keep pushing. Clear and start fresh.

```
/clear
```

**5. Check your directory — always**

If Claude says it can't find a file:

```
pwd
```

You should see your project directory. If you don't, `cd` back to it. Ninety percent of "Claude can't read my file" problems are directory problems.

**6. Approve carefully**

When Claude proposes a file edit, read what it's changing. Especially when it's modifying existing files. If something looks off, say so — "Don't change the budget numbers, only update the timeline."

### Commands to Avoid (For Now)

Claude Code has many slash commands. Some are powerful but not relevant yet — they'll be covered in later sessions. **Don't worry about these today:**

| Command | Why to skip it for now |
|---------|----------------------|
| `/hooks` | Advanced automation — covered in a later session |
| `/mcp` | External tool connections — covered in a later session |
| `/agents` | Agent management — covered in a later session |
| `/skills` | Skill plugins — covered in a later session |
| `/review`, `/pr-comments` | Developer/code review tools — not relevant for this bootcamp |
| `/init` | Creates a CLAUDE.md — you'll do this properly in Build 1 |

If you accidentally type one of these, no harm done. Just `/clear` and move on.

### Commands You Should Never Approve

Claude can propose terminal commands to interact with your computer. Most are safe, but some are destructive. **If Claude proposes any of these, stop and think before approving:**

| Command | What it does | Why it's dangerous |
|---------|-------------|-------------------|
| `rm -rf` / `rm -r` | Deletes files or folders permanently | No recycle bin. Gone forever. Even `rm` on a single file is permanent. |
| `sudo ...` | Runs anything as administrator | Full system access. One wrong command can break your OS. |
| `chmod 777` | Opens file permissions to everyone | Security risk — makes files readable/writable by anyone. |
| `mv` to unknown locations | Moves files somewhere | You might lose track of where your file went. |
| `curl ... \| bash` | Downloads and runs code from the internet | Executes unknown code on your machine. Never do this blindly. |
| `kill -9` / `killall` | Force-stops applications | Can cause data loss in apps that haven't saved. |
| `diskutil` / `dd` | Low-level disk operations | Can erase or corrupt your entire drive. |
| `defaults write` | Changes macOS system settings | Can break system behavior in subtle, hard-to-undo ways. |
| Any command you don't understand | — | If Claude proposes a command and you don't know what it does, **ask Claude to explain it first**. |

Claude is powerful and generally safe — the permission model means nothing runs without your approval. But your approval is only as good as your attention. The golden rule: **When in doubt, ask Claude: "What exactly will this command do? Is it reversible?" before approving.**

> **What just happened?** You now have the workspace habit (always work in a dedicated folder), six prompting rules, you know which commands to use now vs later, and you know which terminal commands to watch out for. These patterns apply to every session for the rest of the weekend — and to every day after that.

---

## What You Built

- [x] Read files and answered cross-file questions about a real business scenario
- [x] Created new documents from existing content
- [x] Edited and improved drafts with Claude proposing and you approving
- [x] Understood permissions (`/permissions`) and sandbox mode (`/sandbox`)
- [x] Used keyboard controls: `Escape` to cancel, `Ctrl+C` to stop
- [x] Practiced multi-turn conversations and correcting Claude
- [x] Compared bad prompts vs good prompts
- [x] Learned workspace hygiene — always work in a dedicated folder

---

## Take It Home

### Quick Reference — Slash Commands

**Session management:**

| Command | What it does | When to use it |
|---------|-------------|----------------|
| `/help` | Shows all commands | When you forget what's available |
| `/clear` | Wipes conversation | When Claude is confused or you're switching tasks |
| `/compact` | Compresses context | When conversation is long and Claude is slowing down |

**Monitoring and awareness:**

| Command | What it does | When to use it |
|---------|-------------|----------------|
| `/cost` | Session token usage | To track this session's spend |
| `/usage` | Plan limits and rate status | To check if you're rate-limited |
| `/context` | Visual context grid | To see how full your context window is |

**Control:**

| Command | What it does | When to use it |
|---------|-------------|----------------|
| `/model` | Switch model or effort level | When you want faster/deeper responses |
| `/permissions` | View/change permission settings | To check what Claude can do |
| `/sandbox` | Toggle read-only mode | When you want to explore without changes |
| `/doctor` | Diagnose problems | When something feels broken |

### Quick Reference — Keyboard Controls

| Key | What it does |
|-----|-------------|
| `Escape` | Cancel current response |
| `Ctrl+C` | Hard stop / exit |

### The Workspace Rule

```
Always: mkdir → cd → claude
Never: run claude from ~ or Desktop
```

### The 6 Prompting Rules

1. **Be specific** — Tell Claude exactly what you want, not just what to look at
2. **Give context** — Who are you, what's this for, what matters to you
3. **Iterate** — Build on responses, don't restart from scratch
4. **Clear when stuck** — `/clear` is your reset button
5. **Check your directory** — `pwd` solves most "file not found" problems
6. **Approve carefully** — Read the changes before you say yes

---

## If You Finish Early

**Try `/rewind` — your undo button:**

Type `/rewind` to go back to any previous point in your conversation — and optionally undo the file changes Claude made after that point. Think of it as "undo" for your entire conversation. Made a wrong turn three prompts ago? `/rewind` takes you back. This is a safety net you'll use often.

**Try these stretch prompts to push further:**

```
Read all the practice files and write a 1-page "State of the Business" brief that Kavita could send to the board as a pre-read. Cover financials, product, sales, and risks.
```

```
Based on the email from Neha and the quarterly metrics, draft Arjun's response email. He should acknowledge the competitive pressure, share what Product is doing about it, and propose the 30-minute meeting she asked for.
```

```
Read the quarterly metrics CSV and the meeting notes. Create a file called practice-files/board-talking-points.md with the 5 things Kavita absolutely must address at the March 20 board meeting, with data to back each one.
```

```
Compare the action items across all files — the meeting notes, the action-items.txt, the proposal's next steps, and the email. Are there any duplicates? Anything that's been committed to but has no clear owner or deadline?
```

---

> **Key Takeaway:** Claude Code is not magic and it's not a search engine. It's a capable collaborator that reads your files, understands your context, and does the work — with you making every decision. The better you communicate what you need, the better it performs. That's the skill you just started building.
