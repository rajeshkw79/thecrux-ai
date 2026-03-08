# Build 7: Always On — Your Agent Never Sleeps

**Duration:** 60 minutes | **What you unlock:** A proactive AI agent on your phone that watches your inbox and calendar and alerts you — without being asked.

---

## The Big Idea

You built a brain (CLAUDE.md). You gave it a voice (Ghost Writer). You gave it a mouth (Telegram bot) and eyes (Gmail + Calendar MCP). But everything so far required YOU to ask first.

**Today, your agent becomes proactive.** It checks your world on a schedule, applies YOUR rules, and alerts you only when something needs your attention. No alert = nothing urgent. Silence is the feature.

```
WHAT YOU'VE BUILT:
  Brain       — CLAUDE.md (identity, rules, preferences)
  Skills      — Ghost Writer, expert teams
  Mouth       — Telegram bot (Phase 1 today)
  Eyes        — Gmail + Calendar MCP (pre-work)

WHAT YOU BUILD TODAY:
  Connection  — Composio + MCP (how Claude plugs into your tools)
  Judgment    — Always-On Rules (what matters vs. what doesn't)
  Autonomy    — always-on-check.sh (checks your world without being asked)
  Schedule    — Cron (runs every N minutes, forever)

THE RESULT:
  Your phone buzzes. Not because you asked.
  Because your agent decided you needed to know.
```

---

## Getting Started

You should already be in your student repo with Claude Code open. If not:

```bash
cd student_repo_build07_always_on
claude
```

Your CLAUDE.md from earlier sessions should already be in this directory. If not, copy it over now.

---

## Phase 1: Telegram Bot (20 min)

**Goal:** Every student has a working Telegram bot on their phone that talks to Claude and knows who they are.

### Step 1: Create Your Bot (5 min)

If you don't have Telegram yet, download it from the App Store / Play Store.

**On your phone:**

1. Open Telegram and tap the **search bar** at the top of your Chats screen
2. Search for **BotFather** (look for the one with the blue checkmark)
3. Tap it, then tap `/start`
4. Send `/newbot`
5. Give it a name (e.g., "My Claude", "Always On Agent")
6. Give it a username (must end in `bot`, e.g., `yourname_always_on_bot`)
7. BotFather will reply with a **bot token** (looks like `123456:ABC-DEF...`) — don't close this chat yet
8. Now go back to search, search for **userinfobot**
9. Tap it, then tap `/start`
10. It will reply with your **user ID** (a number like `123456789`)

**Getting the token and ID to your laptop:**

1. Open **web.telegram.org** in your laptop browser
2. It will show a QR code — scan it with your phone's Telegram app (Settings > Devices > Link Desktop Device)
3. Now you have Telegram open on your laptop — find the BotFather and userinfobot chats
4. Copy-paste the bot token and user ID directly into your `.env` file (you will find a .env.example file here - you can make the changes there and rename it to .env (Why are we doing this ? Can you guess ? ))

Alternative: email them to yourself, or use any notes app that syncs between phone and laptop.

### Step 2: Wire the Bot (8 min)

Save your bot token and user ID in the `.env` file (you will find .env.example in this folder - you can make the changes there and then rename it to .env):

```
TELEGRAM_BOT_TOKEN=<paste your bot token here>
TELEGRAM_USER_ID=<paste your user ID here>
```

Now install and run — **open a new terminal window** for this (not inside Claude Code). The bot needs to keep running while you continue building.

```bash
pip install python-telegram-bot python-dotenv
python telegram_bot.py
```

You must be in the project directory — the bot uses `claude -p` which reads your CLAUDE.md from the current directory.

Leave this terminal running. Don't close it.

> **Bot not working?** There's a tested reference script in your repo. Run `python telegram_bot_reference.py` instead. Same functionality, guaranteed to work with your .env file.

### Step 3: Quick Test (5 min)

Open Telegram on your phone and message your bot:

- **"What do you know about me?"** — Claude reads CLAUDE.md, knows you
- **"Write a 3-line email declining a meeting"** — writes in your tone
- **"What are my pet peeves?"** — knows your preferences

That's YOUR AI assistant. On YOUR phone. It knows YOUR name, YOUR style. And it took under 15 minutes.

### Phase 1 Checkpoint

- [ ] Bot created via @BotFather
- [ ] .env file has your token and user ID
- [ ] Bot responds on your phone
- [ ] Bot knows your name and preferences

> **Hard cutoff at 20 minutes.** If your bot isn't working yet, use `telegram_bot_reference.py` and move on. Phase 2 doesn't need the bot running.

---

## Phase 2: Composio + MCP + Always-On Rules (20 min)

**Goal:** Understand how Claude connects to external tools, set up (or verify) Gmail and Calendar access, then give Claude the judgment to know what matters to YOU.

### Why Composio?

Claude is powerful — but by default, it can't see your email, calendar, or any external tool. To give Claude "eyes," you'd normally need to build API integrations yourself: OAuth flows, token management, data parsing. That's days of work per tool.

**Composio does this for you.** You authenticate once (click "Connect Gmail"), and Claude gets clean, ready-to-use tools — "read emails," "check calendar," etc. Same pattern for 900+ apps.

```
Without Composio:
  You → build Gmail API integration → handle OAuth → manage tokens
  → parse responses → feed to Claude
  (may take an hour to setup)

With Composio:
  You → click "Connect Gmail" → done
  Claude gets: read_email, send_email, search_email tools
  (5 minutes, no code)
```

### What is MCP?

MCP (Model Context Protocol) is HOW Claude talks to Composio — and to any external tool.

Think of MCP as a USB port for AI. It's a standardized connection that lets any tool plug into Claude. Composio hosts MCP servers for each app. You tell Claude Code where to find them, and Claude discovers the available tools automatically.

```
The connection chain:

  Claude Code ←→ MCP ←→ Composio ←→ Gmail / Google Calendar
       ↑              ↑              ↑
  Your AI agent    The protocol    The adapter
                   (like USB)      (handles APIs)
```

MCP is an open standard created by Anthropic. Any developer can build MCP servers for any tool. Composio just happens to host hundreds of pre-built ones.

### Step 1: Set Up Composio (5 min)

**If you did the pre-work, skip to Step 2 (Verify Gmail).**

If not, follow these steps now:

**1. Create a Composio account:**

- Go to [composio.dev](https://composio.dev) → Sign Up with your test Google account

**2. Get your API key:**

- Settings → API Key → Copy it

**3. Connect Gmail + Google Calendar:**

Go to the All Toolkits tab.

- Integrations → Search "Gmail" → Connect → Authorize with your test Google account
- Search "Google Calendar" → Connect → Authorize (same account)

  It willl add these integrations to the default project that composio already created.

**4. Run the setup script** (from your terminal, in the project directory):

```bash
python setup_composio.py
```

The script will:
- Install `composio-core` if needed
- Ask for your API key (or read it from the `COMPOSIO_API_KEY` env var)
- Let you pick which apps to connect (Gmail, Google Calendar, etc.)
- Open a browser for OAuth login if an app isn't connected yet
- Create a single ToolRouter MCP session and run the `claude mcp add` command for you

**5. Restart Claude Code** (exit and reopen) so it picks up the new MCP server.

> **What just happened:** The script created a single Composio ToolRouter — one MCP connection that gives Claude access to all your selected apps (Gmail, Calendar, etc.). Each time Claude needs your emails, it calls Composio through this MCP server, Composio calls the right API, and the data flows back. One connection, multiple apps, no manual API wiring.

### Step 2: Verify Gmail MCP (2 min)

In Claude Code, test your Gmail connection:

```
Read my 3 most recent emails. For each one: who it's from, subject, one-sentence summary.
```

If you see your actual emails summarized, Gmail MCP is working.

> **Not working?** Use the fallback: `Read sample-inbox.md and summarize the 3 most urgent emails.`

### Step 3: Verify Calendar MCP (2 min)

```
What's on my calendar today? List each meeting with time, title, and attendees.
```

> **Not working?** Use the fallback: `Read sample-calendar.csv and tell me what's on my schedule today.`

### Step 4: Add Always-On Rules to CLAUDE.md (6 min)

Open `always-on-rules-template.md` in your repo. It has a fill-in-the-blank template. Fill it in and add it to your CLAUDE.md.

**The template:**

```markdown
## Always-On Rules

### URGENT (alert me immediately on Telegram):
- Emails from: [name 1, role], [name 2, role]
- Keywords in subject/body: urgent, deadline, escalation, [your keywords]
- Any email about money over [amount, e.g., INR 5 lakh / $10,000]
- Calendar conflicts (double-booked meetings)

### IMPORTANT (include in daily briefing):
- Project updates from: [team member names]
- Meeting invites for this week
- Emails from: [important but not urgent contacts]

### IGNORE (never alert me):
- Newsletters and marketing emails
- Automated notifications (CI/CD, monitoring, etc.)
```

**Tips:**

- Be specific. "Emails from my boss" is vague. "Emails from Rajesh Sharma, CEO, especially about board, investor, or quarterly" is actionable.
- Think about last week. What caught you off guard? That's a rule.
- Start strict. Too few alerts > too many. **Silence is the feature.**

You can ask Claude to help:

```
Add the Always-On Rules section to my CLAUDE.md. Here are my rules:

URGENT: [paste your filled-in rules]
IMPORTANT: [paste your filled-in rules]
IGNORE: [paste your filled-in rules]
```

### Phase 2 Checkpoint

- [ ] Understand what MCP is and why Composio exists
- [ ] Composio account created with Gmail + Calendar connected
- [ ] MCP servers added to Claude Code (`claude mcp add` commands run)
- [ ] Gmail MCP works (or using sample-inbox.md fallback)
- [ ] Calendar MCP works (or using sample-calendar.csv fallback)
- [ ] Always-On Rules added to CLAUDE.md
- [ ] Rules are specific (names, amounts, keywords — not vague categories)

---

## Phase 3: Always On (18 min)

**Goal:** Build a script that checks your email + calendar, applies your rules, and sends a Telegram alert — all without you asking. Then schedule it to run automatically.

### Step 1: Build always-on-check.sh (8 min)

Ask Claude to build the script:

```
Create always-on-check.sh that:

1. Sources .env for TELEGRAM_BOT_TOKEN and TELEGRAM_USER_ID
2. Runs claude -p with this prompt:
   "Read my recent emails (last 2 hours) and today's calendar.
    Apply my Always-On Rules from CLAUDE.md.
    Check for: urgent emails, calendar conflicts, upcoming meetings
    needing prep (next 60 min).

    If ANYTHING needs my attention, output a SHORT alert message
    (max 5 lines). Format:
    🚨 [URGENT] or 📋 [HEADS UP]
    - What needs attention
    - Why it's urgent
    - Suggested action

    If NOTHING needs attention, output exactly: ALL_CLEAR"

3. Captures the output
4. If output is NOT "ALL_CLEAR":
   - Sends it to Telegram via curl using the Bot API:
     https://api.telegram.org/bot$TOKEN/sendMessage
   - Chat ID = TELEGRAM_USER_ID
5. If output IS "ALL_CLEAR": do nothing. No message. Silence.
6. Make it executable (chmod +x)

IMPORTANT: The script must cd to this project directory before
running claude -p, so Claude reads my CLAUDE.md and has access
to my MCP connections.
```

> **If Gmail MCP isn't connected:** Modify the prompt to say "Read sample-inbox.md and sample-calendar.csv" instead of "Read my recent emails."

### Step 2: Test It (2 min)

Run it manually:

```bash
./always-on-check.sh
```

Check your phone. If any of your test emails match your URGENT rules, you should get a Telegram alert. If nothing is urgent, silence — that's correct behavior.

**Quick debug:** If the script errors out, check:

- Is `.env` populated with your real token and user ID?
- Are you in the right directory?
- Does `claude -p "hello"` work from this directory?

### Step 3: Set the Cron (3 min)

For the in-class demo, we'll set it to every 2 minutes so you can see it fire. Ask Claude to do it:

```
Set up a cron job that runs always-on-check.sh every 2 minutes.
Use the full absolute path to the script.
```

Claude will run the `crontab` commands for you. Verify it's set:

```
Show me my current crontab entries.
```

> **Windows users:** Ask Claude: "I'm on Windows. Set up a scheduled task that runs always-on-check.sh every 2 minutes." Claude will walk you through Task Scheduler or set up a Git Bash loop.

### Step 4: THE MOMENT (5 min)

Put your phone on the table. Wait.

Don't message the bot. Don't do anything.

Within 2 minutes, your phone will buzz. An alert you didn't ask for. Your agent checked your email, applied your rules, found something that needs your attention, and told you.

**You didn't ask for that. Your agent decided you needed to know.**

That's the difference between a tool and an agent. A tool waits for you. An agent watches for you.

### Phase 3 Checkpoint

- [ ] always-on-check.sh runs without errors
- [ ] Sends Telegram alert for urgent items
- [ ] Stays silent when nothing is urgent
- [ ] Cron is set and fires automatically

---

## The Payoff (7 min)

### Change to a Real Schedule (3 min)

The every-2-minutes cron was for the demo. Now set a real schedule. Pick one based on your Composio plan:

| Your Composio Plan             | Suggested Schedule              | What It Means     |
| ------------------------------ | ------------------------------- | ----------------- |
| Free tier (~1,000 calls/month) | 3x/day: 9am, 1pm, 5pm           | Most conservative |
| Starter (~5,000 calls/month)   | Every 30 min, 8am-6pm, weekdays | Good balance      |
| Pro (~20,000+ calls/month)     | Every 15 min, 8am-8pm, weekdays | Near real-time    |

Ask Claude to update it:

```
Change my always-on-check.sh cron job from every 2 minutes to
[pick one]:
- 3 times a day (9am, 1pm, 5pm) on weekdays
- every 30 minutes during work hours (8am-6pm) on weekdays
- every 15 minutes during work hours (8am-8pm) on weekdays
```

**Start conservative.** You can always increase later. Monitor your Composio usage dashboard.

Each cron run = 1 Claude call + 2-3 Composio tool calls (read emails, read calendar).

> **Cost note:** `claude -p` runs on your Claude Pro/Max subscription — no extra API cost. But Composio has tool call limits on their free tier. Check your plan.

### The Full Picture (3 min)

Look at what you built this weekend:

```
YOUR AI SYSTEM:

BRAIN       — CLAUDE.md (who you are, how you think)
MEMORY      — Second Brain (your knowledge base)
VOICE       — Ghost Writer (writes like you)
MOUTH       — Telegram bot (you talk to it from your phone)
EYES        — Gmail + Calendar MCP (it sees your world)
JUDGMENT    — Always-On Rules (it knows what matters to YOU)
AUTONOMY    — Cron + always-on-check.sh (it acts without being asked)

YOUR MONDAY MORNING:

You wake up. Your phone has a Telegram alert:
"🚨 [URGENT] CEO Rajesh emailed at 11pm about board deck.
 Sequoia investor wants intro call this week. You have a
 calendar conflict at 2pm — Budget Review overlaps with
 Client Prep. Suggested: move Budget Review to 3pm."

You didn't open email. You didn't check your calendar.
Your agent already did — and told you what matters.
```

That's not a demo. That's your new reality. Your agent never sleeps.

---

## What's Next: Ideas to Build After This

You now have all the building blocks: CLAUDE.md + Telegram + MCP + cron. Here are workflows you can build with the same pattern. Just tell Claude what you want.

**Email & Communication:**

- Morning Briefing — 3-agent pipeline (scan, triage, format) delivered at 7:55 AM every weekday
- Smart Email Drafts — agent drafts replies to urgent emails in your voice, sends for your approval
- Meeting Prep Bot — 30 min before each meeting, agent sends context about who you're meeting and recent emails from them

**Work & Productivity:**

- Action Item Tracker — paste meeting notes into Telegram, agent extracts and tracks action items
- Daily Standup Generator — agent reads your git commits / project files, drafts standup update each morning
- Stakeholder Update — weekly cron that drafts status updates for different audiences

**Content & Social Media:**

- LinkedIn Auto-Publisher — daily topic research + Ghost Writer draft + one-tap publish
- Twitter/X Curator — agent scans RSS feeds, picks the best article, pre-formats a tweet

**How to build any of these:** Just tell Claude. Start with: "Help me build a [workflow name] automation that checks [source] every [frequency] and sends me [output] on Telegram."

---

## Beyond DIY: NanoClaw and OpenClaw

What you built today runs while your laptop is open. For true always-on (24/7, even while you sleep), check out these open-source tools:

|            | What You Built Today         | NanoClaw                                  | OpenClaw                   |
| ---------- | ---------------------------- | ----------------------------------------- | -------------------------- |
| Setup time | 20 min                       | ~30 min                                   | ~1 hour                    |
| Channels   | Telegram only                | Telegram, WhatsApp, Slack, Discord, Gmail | 20+ channels               |
| Always-on  | While laptop is open         | Yes (runs in container)                   | Yes (local or cloud)       |
| Complexity | Beginner-friendly            | Intermediate                              | Intermediate-Advanced      |
| Cost       | Free                         | Free (self-hosted)                        | Free (self-hosted)         |
| Best for   | Learning, quick personal use | Multi-channel, security-conscious         | Full AI assistant platform |

**NanoClaw** (`qwibitai/nanoclaw` on GitHub) — Built on Anthropic's Agent SDK. Runs Claude in containers. Supports WhatsApp, Telegram, Slack, Discord. Each chat gets its own isolated CLAUDE.md and sandbox.

**OpenClaw** (`openclaw/openclaw` on GitHub, 68K+ stars) — Full personal AI agent platform. 20+ channels, 100+ preconfigured skills, runs locally or on cloud.

**Our recommendation:** Start with what you built today. When you want WhatsApp or true 24/7, try NanoClaw. When you want the full platform, try OpenClaw.

---

## Platform-Specific Scheduling (Reference)

In class, you asked Claude to set up cron for you. Here's what's happening under the hood, and how to change it later.

### macOS/Linux — cron

Claude ran something like:

```bash
# List current cron jobs
crontab -l

# Add/update a cron entry
(crontab -l 2>/dev/null; echo "*/30 8-18 * * 1-5 /path/to/always-on-check.sh") | crontab -
```

To change your schedule later, just ask Claude:

```
Change my always-on-check.sh cron to run every 15 minutes during work hours on weekdays.
```

Or to remove it: `Remove the cron job for always-on-check.sh.`

### Windows — Task Scheduler

Ask Claude: "I'm on Windows. Help me set up a scheduled task to run always-on-check.sh every 30 minutes during work hours." Claude will walk you through Task Scheduler step by step, or set up a simpler Git Bash loop:

```bash
while true; do ./always-on-check.sh; sleep 1800; done
```

(1800 seconds = 30 minutes. Close the terminal to stop.)

---

## Troubleshooting

| Problem                   | Fix                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Bot doesn't respond       | Check: is telegram_bot.py running? Token correct? User ID correct? Try `telegram_bot_reference.py`.                             |
| pip install fails         | Try `pip3 install python-telegram-bot python-dotenv`. Check Python version.                                                     |
| Gmail MCP doesn't work    | Use `sample-inbox.md` fallback. Run `/mcp` in Claude Code to check connections.                                               |
| Calendar MCP doesn't work | Use `sample-calendar.csv` fallback.                                                                                             |
| always-on-check.sh errors | Check `.env` is populated. Check `claude -p "hello"` works. Check you're in the right directory.                              |
| Cron doesn't fire         | Ask Claude: "Show my crontab and check if always-on-check.sh is scheduled correctly." Also try running the script manually first. |
| Alert message is empty    | Claude may have returned ALL_CLEAR. Send yourself a clearly urgent test email and re-run.                                         |
| Too many alerts           | Tighten your IGNORE rules. Add more keywords to ignore.                                                                           |
| No alerts at all          | Loosen your URGENT rules. Or send yourself a test email with "URGENT" in the subject.                                             |

---

## What You Built Today

- [ ] **Telegram bot** — Claude on your phone, knows who you are
- [ ] **Gmail + Calendar connected** — Claude sees your inbox and schedule
- [ ] **Always-On Rules** — Claude knows what YOU consider urgent
- [ ] **always-on-check.sh** — Proactive check that runs without you asking
- [ ] **Cron schedule** — Automatic, recurring, always watching
- [ ] **THE MOMENT** — Your phone buzzed with an alert you didn't ask for

Your agent never sleeps. And neither does its judgment — because you taught it what matters.
