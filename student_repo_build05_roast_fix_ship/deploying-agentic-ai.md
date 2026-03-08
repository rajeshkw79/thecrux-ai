# Deploying Agentic AI: From Your Laptop to the Real World

**For:** Non-engineers who've used Claude Code locally and want to know what's next | **Read time:** 15 minutes

---

## The Question

You've used Claude Code on your laptop. You gave it a goal, it read files, made decisions, used tools, and delivered a result. It felt powerful.

Then the question hits: **"This only works when my laptop is open and I'm sitting here. How do I make this run on its own?"**

That's the deployment question. And it's the right one to ask.

---

## What "Deploying" an Agent Actually Means

When you run Claude Code on your laptop, three things are true:

1. **Your machine is the brain** — Claude runs here
2. **Your files are the context** — Claude reads from your folders
3. **You are the trigger** — nothing happens until you type a prompt

Deploying means changing one or more of these:

| What changes | What it means | Example |
|---|---|---|
| **The trigger** | Something other than you starts the agent | A schedule, a webhook, an incoming email |
| **The machine** | It runs on a server, not your laptop | A cloud VM, a serverless function, a platform |
| **The context** | It reads from shared systems, not your local files | A database, an API, a shared drive |

You don't have to change all three at once. In fact, the smartest path is to change one at a time.

---

## The Three Paths

Each path is a real option. They're ordered from "you can do this today" to "you'll need some help."

---

### Path 1: Keep It on Your Machine, Add a Schedule

**Difficulty:** Low | **What changes:** The trigger | **You still need:** Your laptop running

This is the simplest deployment. Your agent runs on your laptop, but instead of you typing a prompt, a scheduler triggers it automatically.

**What this looks like:**

You tell Claude Code: "Every Monday at 8 AM, read my sales-notes folder, identify what's overdue, and write a priorities file."

The agent is the same one you've been using. The only difference is you're not the one pressing "go."

**How to set it up:**

Claude Code has a built-in scheduler. In your Claude Code session:

```
/scheduler:schedule-add
```

It will ask you:
- **What to run:** Your prompt (the same kind you've been typing)
- **When to run:** A schedule (e.g., "every Monday at 8 AM", "every weekday at 6 PM")
- **Where to run:** Which project folder

That's it. Claude Code will execute the prompt on schedule, as long as your machine is on.

**Real examples:**

| Schedule | What the agent does |
|---|---|
| Every Monday 8 AM | Reads your work notes, creates a weekly priorities list |
| Every Friday 5 PM | Summarises what you accomplished this week from your files |
| Every day 9 AM | Checks a shared folder for new client briefs, flags urgent ones |
| Every month 1st | Pulls your expense CSVs, categorises them, generates a summary |

**Limitations:**
- Your laptop must be running (lid open or set to not sleep)
- If your laptop is off on Monday at 8 AM, the task doesn't run
- Only has access to files on your machine

**When this is enough:** Personal productivity workflows, weekly reports, file organisation, anything where "it runs when my machine is on" is acceptable.

---

### Path 2: Move It to a Server (Always On)

**Difficulty:** Medium | **What changes:** The trigger + the machine | **You need:** A cloud account (AWS, Google Cloud, Railway, or similar)

This is the step where your agent runs even when your laptop is closed. The agent lives on a server in the cloud — a computer that's always on, always connected.

**What this looks like:**

You write a script that calls the Claude API (not Claude Code, but the API behind it). The script runs on a cloud server on a schedule or when triggered by an event. It reads data from wherever you point it — a database, an API, a Google Sheet — and takes action.

**The key shift:** You're no longer using Claude Code (the terminal tool). You're using the Claude API — the same intelligence, accessed programmatically.

**How to set it up (the conceptual steps):**

1. **Write a script** that calls the Claude API with your prompt and tools
2. **Give the script access** to the data it needs (database credentials, API keys — this is where environment variables matter)
3. **Deploy the script** to a cloud platform
4. **Set a trigger** — a cron schedule, a webhook, or an event

**Concrete example — a weekly sales summary agent:**

```
Your script (Python):
1. Connects to your CRM API → pulls last week's deals
2. Sends the data to Claude API → "Analyse this and write a summary"
3. Claude responds with the summary
4. Script sends the summary via email using SendGrid API

Deployed on: Railway (or AWS Lambda, or Google Cloud Functions)
Trigger: Runs every Monday at 7 AM IST
```

**Platforms that make this easier:**

| Platform | What it does | Difficulty |
|---|---|---|
| **Railway** | Deploy scripts with a `git push`. Add a schedule. Done. | Low-medium |
| **Replit** | Write and deploy in the browser. Good for prototyping. | Low |
| **AWS Lambda** | Serverless functions that run on triggers. Pay per execution. | Medium |
| **Google Cloud Run** | Containerised scripts that run on schedule. | Medium |
| **Vercel** (with API routes) | If you already deployed your landing page here, you can add API routes that call Claude | Medium |

**What you'll need to learn:**
- How to use the Claude API (it's an HTTP call — Claude Code can write this for you)
- Environment variables (you already know this — see the environment variables guide)
- Basic deployment on one of these platforms (Claude Code can walk you through it)

**When this is the right path:** You want the agent running reliably without your laptop. Business workflows, automated reports, monitoring tasks.

---

### Path 3: Build a Full Agent System (Production-Grade)

**Difficulty:** High | **What changes:** Everything | **You need:** A developer or significant time to learn

This is what companies build when they want agentic AI as a core part of their product or operations. It's not a single script — it's a system.

**What this looks like:**

A multi-step agent that:
- Listens for triggers (a new customer signs up, a support ticket is filed, a deal moves stages)
- Plans its approach based on the situation
- Uses multiple tools (CRM, email, Slack, databases, other APIs)
- Handles errors gracefully (retries, fallbacks, alerts)
- Logs what it did so humans can audit it
- Has guardrails so it can't do anything catastrophic

**Real-world example — a customer onboarding agent:**

```
Trigger: New customer signs up on your product

Agent workflow:
1. Reads the customer's profile and plan tier
2. Decides which onboarding sequence to use (SMB vs. Enterprise)
3. Creates a personalised welcome email using Claude
4. Schedules a series of check-in emails for days 1, 3, 7
5. If Enterprise: creates a Slack channel and notifies the account manager
6. If the customer hasn't logged in by day 3: adjusts the day-3 email to be more urgent
7. Logs all actions to a dashboard for the CS team to review
```

**Frameworks and tools for building this:**

| Tool | What it does |
|---|---|
| **Claude Agent SDK** | Anthropic's official SDK for building multi-step agents with tool use |
| **LangChain / LangGraph** | Framework for chaining AI calls with tools, memory, and branching logic |
| **CrewAI** | Multi-agent framework — multiple AI agents collaborating on a task |
| **Temporal** | Workflow orchestration — handles retries, state, and long-running processes |
| **MCP (Model Context Protocol)** | Standard for connecting AI agents to external tools and data sources |

**When this is the right path:** You're building agentic AI into a product, or you have a complex business process that runs daily with real stakes. This is not a weekend project — it's an engineering effort.

---

## How to Think About Which Path to Choose

```
Start here:
│
├─ "I want MY workflow to be automated"
│   ├─ My laptop is always on → Path 1 (Scheduler)
│   └─ It needs to run even when I'm away → Path 2 (Server)
│
├─ "I want to automate a TEAM workflow"
│   ├─ Simple (one trigger, one action) → Path 2 (Server)
│   └─ Complex (multiple steps, multiple tools, error handling) → Path 3 (Agent System)
│
└─ "I want to build this INTO a product"
    └─ Path 3 (Agent System)
```

**The honest advice:** Start with Path 1. Today. Right now. Get one workflow running on a schedule. Live with it for a week. See what breaks, what's missing, what you wish it could do. That experience will tell you whether you need Path 2 or 3 — and exactly what you need from it.

---

## What You Can Do Right Now (5 minutes)

Pick one of these and set it up before you leave today:

**Option A: Morning briefing**
```
/scheduler:schedule-add

Prompt: Read all files in my work-notes/ folder. What are the 3 most
important things I should focus on today? Write the answer to
daily-brief.md.

Schedule: Every weekday at 7:30 AM
```

**Option B: Weekly review**
```
/scheduler:schedule-add

Prompt: Read all files modified this week in my projects/ folder.
Summarise what I worked on, what's done, and what's still open.
Write it to weekly-review.md.

Schedule: Every Friday at 5:00 PM
```

**Option C: File organiser**
```
/scheduler:schedule-add

Prompt: Look at my Downloads/ folder. Move any PDFs to Documents/pdfs/,
any images to Documents/images/, and any CSVs to Documents/data/.
Tell me what you moved.

Schedule: Every day at 9:00 PM
```

Set one up. Let it run for a week. Then decide your next step.

---

## The Progression

| Where you are now | What you just learned | Next step |
|---|---|---|
| Used Claude Code locally | Agentic AI works — you've seen it | Set up a scheduled agent (Path 1) |
| Running scheduled agents | You know what's worth automating | Deploy to a server (Path 2) |
| Running agents on a server | You know what a reliable agent needs | Build a production system (Path 3) or hire someone who can |

You don't jump from "I used Claude Code once" to "production agent system." You climb the ladder one rung at a time. Each rung teaches you what the next one needs.

---

## Common Questions

**"Do I need to learn to code for Path 2?"**
You need to be comfortable reading code, not necessarily writing it from scratch. Claude Code can generate the script for you. You need to understand what it does, set up the environment variables, and deploy it. Think of it as driving a car, not building one.

**"How much does this cost?"**
- Path 1: Free (uses your existing Claude Code subscription)
- Path 2: Claude API usage (pay per call — a weekly summary might cost ₹5-15 per run) + server hosting (Railway free tier covers most personal projects, paid plans from ~₹500/month)
- Path 3: Depends entirely on scale. Enterprise budgets.

**"What if my agent does something wrong?"**
Start with low-stakes tasks (file organisation, summaries, reports). Never give an agent the ability to send emails, post publicly, or spend money until you've watched it run correctly at least 10 times. Add a "draft for review" step before any external action.

**"Can I use Claude Code on a server instead of the API?"**
Yes, technically. Claude Code can run in headless mode on a server. But the API gives you more control, better error handling, and lower cost at scale. Think of Claude Code as the workshop and the API as the factory.

**"I built something cool on Path 1. How do I share it with my team?"**
That's exactly when you move to Path 2. A server-based agent can be triggered by anyone (via a Slack command, a form submission, or a shared schedule), not just from your laptop.
