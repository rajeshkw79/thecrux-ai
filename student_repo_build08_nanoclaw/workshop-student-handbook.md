# NanoClaw Workshop — Student Handbook

**Duration:** 60 minutes
**Prerequisites:** Claude Code installed, Docker Desktop installed, WhatsApp on your phone

---

## Part 1: What Are We Building? (5 min — Instructor explains)

You're going to set up a personal AI assistant that lives on your machine and talks to you via WhatsApp. When you message it, here's what happens:

```
You (WhatsApp) → NanoClaw (Node.js on your machine) → Docker Container → Claude Agent SDK → Response → WhatsApp
```

**Key concepts:**

- **NanoClaw** is a small Node.js process (~3,000 lines) that connects WhatsApp to Claude
- **Each message** triggers a Docker container where Claude runs with full coding/browsing/tool capabilities
- **Each group** gets its own isolated container, filesystem, and personality (via `CLAUDE.md` files)
- **Baileys** is the open-source library that connects to WhatsApp (no official API needed)
- **Credential Proxy** — your API keys never enter the container. A proxy on your machine injects them at the network level

**Why containers?** If you give an AI agent Bash access (which Claude Code has), you want it sandboxed. The container can only see directories you explicitly mount. It can't touch your host filesystem, read your `.env`, or run commands on your machine.

**When are containers created?**
- A new container is spawned each time you send a message (or batch of messages)
- It stays alive for 30 minutes waiting for follow-up messages
- After the idle timeout, it's destroyed
- Scheduled tasks also spawn their own containers (destroyed after the task completes)

---

## Part 2: Install NanoClaw (15 min)

The entire installation happens through Claude Code. You type 3 commands in your terminal, then Claude handles everything else.

### Step 1: Clone and launch Claude Code

**Mac (Terminal) or Windows (PowerShell):**
```bash
git clone https://github.com/qwibitai/nanoclaw.git
cd nanoclaw
claude
```

That's it for terminal commands. Everything else happens inside Claude Code.

Claude may ask if you want to fork the repository. **Select "Continue without fork"** to keep things simple.

### Step 2: Run setup

Type this inside the Claude Code prompt:

```
/setup
```

Claude will:

1. **Check your environment** — verifies Docker is running (if Docker Desktop isn't started, Claude will tell you to open it — just open the app, wait for the green icon, and tell Claude to continue)
2. **Install dependencies** — runs `npm install`
3. **Build the container** — builds the `nanoclaw-agent:latest` Docker image (~2-3 min first time)
4. **Connect WhatsApp** — authenticates your WhatsApp account (see below)
5. **Register your main group** — sets up your self-chat as the admin channel
6. **Install the service** — configures NanoClaw to run in the background

### Step 3: Choose authentication method

During setup, Claude will ask how you want to authenticate with Anthropic. **Select "Claude Code OAuth"** (not "Anthropic API Key").

OAuth uses your existing Claude Code login — the same account you're already signed into. It's free with your Claude Pro or Max subscription. The API key option requires a separate Anthropic developer account with pay-per-use billing, which you don't need.

**Generate the OAuth token now.** Open a **separate terminal window** (do NOT run this inside Claude Code) and run:

**Mac (new Terminal window):**
```bash
claude setup-token
```

**Windows (new PowerShell window):**
```powershell
claude setup-token
```

This will generate an OAuth token. Copy it, then:

1. In your NanoClaw root directory (`nanoclaw/`), rename `.env.example` to `.env`
2. Open `.env` and add your token:
   ```
   CLAUDE_CODE_OAUTH_TOKEN=<your_token>
   ```

**DO NOT paste the token into the Claude Code chat session.** It goes in the `.env` file only.

Go back to your Claude Code window and tell it you've added the token.

### Step 4: Choose messaging channels

Claude will ask which messaging channels to enable. **Just select WhatsApp for now.** You can always add more channels later (Telegram, Slack, Discord) by chatting with your bot — no need to re-run setup.

Claude will then ask to fetch external code from a remote git repo (`nanoclaw-whatsapp`). **Say yes.** This is how NanoClaw works — the core codebase is deliberately kept tiny (just hundreds of lines) so you can read and understand the whole thing. Channels, integrations, and capabilities are pulled in as separate code packages only when you need them. You never end up with code for features you don't use.

### Step 5: WhatsApp Authentication

Claude will ask how to link WhatsApp. **Choose "QR code in browser".**

A browser window will open with a QR code. On your phone:

1. Open WhatsApp
2. Go to **Settings → Linked Devices → Link a Device**
3. Scan the QR code before it expires (60 seconds — if it expires, Claude will regenerate it)

> **Important:** You're linking your real WhatsApp account. NanoClaw connects as a "linked device" (like WhatsApp Web). It can read and send messages as you.

### Step 6: Name your bot and choose chat type

Claude will ask you two things:

1. **Trigger word** — the word that wakes up your agent. Must start with `@` (e.g., `@Andy`, `@Jarvis`, `@Buddy`). Your bot only responds when a message starts with this trigger.
2. **Bot name** — the display name for your assistant. Pick whatever you like.

Claude will ask if you want the agent sandboxed (running in a Docker container). **Select yes.** This is the safe default — the agent can only access what you explicitly allow. Once you're more confident with the system, you can change this later.

Claude will then ask which chat type to register as your main channel. **Select "Self-chat"** (the "Message yourself" conversation in WhatsApp). This becomes your private admin channel for managing the bot.

### Step 7: Start the service and watch the logs

Claude will call `launchctl` (Mac) or `systemctl` (Linux) to start NanoClaw as a background service.

Open a **new terminal window** and tail the logs to see messages flowing in:

**Mac:**
```bash
cd ~/nanoclaw
tail -f logs/nanoclaw.log
```

**Windows (PowerShell):**
```powershell
cd $HOME\nanoclaw
Get-Content -Path "logs\nanoclaw.log" -Wait
```

This is just for debugging and checking things — you don't need to keep this running. Close it anytime.

### Step 8: Customize your agent's personality

Go into the `groups/` directory in your NanoClaw folder. You'll see folders for different channels — there should be one called `whatsapp_main`. Open it and edit the `CLAUDE.md` file inside to give your agent more context and guardrails.

**Mac:**
```bash
cd ~/nanoclaw/groups/whatsapp_main
open CLAUDE.md    # opens in your default text editor
```

**Windows:**
```powershell
cd $HOME\nanoclaw\groups\whatsapp_main
notepad CLAUDE.md
```

This is where you tell your agent who it is, how to behave, and what it knows. For example:

```markdown
You are Jarvis, a personal assistant for Shameek.
Be concise. Use bullet points. No fluff.
You know that Shameek works at Mantid AI and is based in India.
Never share personal information with anyone else.
```

Save the file. The next time your bot responds, it will use this personality.

You can also edit `groups/global/CLAUDE.md` — this applies to your bot across **all** groups, not just the main one. Think of it as the base personality.

When you register new WhatsApp groups with your bot, each group gets its own directory under `groups/`. You can create a separate `CLAUDE.md` in each group folder to tailor different context and rules per group — or just ask your bot to do it for you via chat.

> **From this point on, most additional setup, changes, or new functionality can be done by simply chatting with your bot via WhatsApp!** You don't need to go back to the terminal or Claude Code for most things.

### Step 9: Verify it works

Once setup completes, open your WhatsApp self-chat (the "Message yourself" chat) and type:

```
@Andy hello
```

(Replace `@Andy` with whatever trigger name was configured during setup.)

You should get a response within 10-30 seconds.

> **Troubleshooting:** If no response after 60 seconds, go back to Claude Code and type: "Why isn't the bot responding?" or run `/debug`.

---

## Part 3: Watch the Logs (5 min)

Open a **new terminal window** (keep Claude Code running in the other one).

**Mac:**
```bash
cd ~/nanoclaw
tail -f logs/nanoclaw.log
```

**Windows (PowerShell):**
```powershell
cd $HOME\nanoclaw
Get-Content -Path "logs\nanoclaw.log" -Wait
```

Now send another WhatsApp message. Watch the logs — you'll see:

1. `Processing messages` — message received from WhatsApp
2. `Spawning container agent` — Docker container starting
3. `Container completed` — agent finished, response sent

**Container-specific logs** (one file per container run):

Mac:
```bash
ls -la groups/whatsapp_main/logs/
cat groups/whatsapp_main/logs/container-*.log | tail -50
```

Windows:
```powershell
ls groups\whatsapp_main\logs\
Get-Content (Get-ChildItem groups\whatsapp_main\logs\container-*.log | Sort-Object LastWriteTime | Select-Object -Last 1).FullName | Select-Object -Last 50
```

These show the exact Docker command, mounted directories, stdin/stdout, and any errors.

---

## Part 4: Add Composio for Email & Calendar (15 min)

### What is Composio?

Composio is a tool integration platform. Instead of building custom code for each app (Gmail, Calendar, Slack, etc.), you connect once through Composio and your agent gets access to 500+ apps through a single SDK.

### Why Tool Router instead of MCP?

You may have heard of **MCP (Model Context Protocol)** — it's the standard way to give AI agents tools. Each MCP server is a separate process that exposes specific tools.

**Composio's Tool Router** takes a different approach for external SaaS apps:

| | MCP Approach | Composio Tool Router |
|---|---|---|
| Gmail integration | Install `gmail-mcp-server`, handle OAuth yourself, manage token refresh | `session.authorize('gmail')` — done |
| Adding Calendar | Install another MCP server, another OAuth flow | `session.authorize('googlecalendar')` — done |
| 10 apps | 10 MCP servers, 10 OAuth implementations | 1 SDK, 10 authorize calls |
| Tool discovery | Static — you configure which tools are available | Dynamic — agent searches "how do I send email?" |
| Token management | You build refresh logic | Composio handles it |

**MCP is great for local tools** (file access, databases, local APIs). **Composio is great for external SaaS integrations** where OAuth and API maintenance are the hard parts.

With Composio's tool router, your agent gets 6 meta-tools:
- `COMPOSIO_SEARCH_TOOLS` — "find a tool that can send emails"
- `COMPOSIO_GET_TOOL_SCHEMAS` — "what parameters does GMAIL_SEND_EMAIL need?"
- `COMPOSIO_MULTI_EXECUTE_TOOL` — execute the tool
- `COMPOSIO_MANAGE_CONNECTIONS` — trigger new OAuth flows on the fly
- Plus 2 more for remote execution

### Step 1: Create a Composio account

1. Go to [app.composio.dev](https://app.composio.dev)
2. Sign up with Google or GitHub (free tier works)
3. Go to **Settings** → copy your **API Key** (starts with `ak_`)
4. Find your **User ID** in your account settings

### Step 2: Tell Claude Code to add Composio

Go back to Claude Code and say:

```
Add Composio integration to NanoClaw. My API key is ak_XXXXX and my user ID is YYYYY.

1. Add COMPOSIO_API_KEY and COMPOSIO_USER_ID to .env
2. In src/container-runner.ts, use readEnvFile() to read these keys and pass them to the container via -e flags
3. In container/agent-runner, install @composio/core and @composio/claude-agent-sdk
4. In container/agent-runner/src/index.ts, import Composio and ClaudeAgentSDKProvider, create a session, get tools, create an MCP server with createSdkMcpServer, and add it to the mcpServers config and allowedTools
5. Rebuild the container and restart NanoClaw
```

Claude will do everything — edit files, install packages, rebuild Docker, restart the service.

### Step 3: Authorize Gmail

Tell Claude Code:

```
Run a script using @composio/core to authorize Gmail for my user ID. Use session.authorize('gmail') and give me the redirect URL.
```

Claude generates a URL — open it, sign in with Google, authorize.

### Step 4: Authorize Google Calendar

```
Same thing but for googlecalendar
```

Open the URL, authorize.

### Step 5: Test it

Send WhatsApp messages to your bot:

```
@Andy what are my latest emails?
```

```
@Andy what meetings do I have today?
```

```
@Andy summarize my unread emails from this morning
```

The agent discovers the right tools via Composio, gets their schemas, and executes them. All dynamically.

---

## Part 5: Scheduled Tasks (5 min)

NanoClaw can run tasks on a schedule. Each task spawns a fresh container, runs a prompt, and can message you back.

### Create a scheduled task

Send this via WhatsApp:

```
@Andy every weekday at 9am, check my email and send me a summary of anything important
```

The agent uses the `schedule_task` tool to create a cron job: `0 9 * * 1-5`.

### More examples

```
@Andy every Monday at 8am, check my calendar for the week and send me an overview
```

```
@Andy in 30 minutes, remind me to follow up with the client
```

### Manage tasks

```
@Andy list all scheduled tasks
@Andy pause the email summary task
@Andy cancel the Monday overview task
```

**Schedule types supported:**
- **Cron**: `0 9 * * 1-5` (9am weekdays) — for recurring schedules
- **Interval**: every N milliseconds — for periodic checks
- **Once**: a specific date/time — for reminders

---

## Part 6: Group Personalities & Knowledge Bases (5 min)

Each WhatsApp group gets its own AI personality and isolated knowledge base.

### How it works

```
groups/
├── global/
│   └── CLAUDE.md          ← Shared across ALL groups (read-only for non-main)
├── whatsapp_main/
│   └── CLAUDE.md          ← Your self-chat (admin channel)
└── whatsapp_family-chat/
    └── CLAUDE.md          ← This group's personality + knowledge
```

Each group's container only sees its own folder. The global `CLAUDE.md` provides a base personality; per-group files override or extend it.

### Example

**Global** (`groups/global/CLAUDE.md`):
```markdown
You are Andy, a helpful personal assistant. Be concise and direct.
Today's date is always available via the system.
```

**Family group** (`groups/whatsapp_family-chat/CLAUDE.md`):
```markdown
In this group, help with family logistics — meal planning, school schedules,
grocery lists. Keep responses casual and fun.

Family members: Mom (Priya), Dad (Rahul), kids Aarav (12) and Meera (8).
Aarav has football practice Tuesdays and Thursdays.
Meera has dance class Mondays and Wednesdays.
```

**Work group** (`groups/whatsapp_work-project/CLAUDE.md`):
```markdown
This is the Alpha Project team. Help track project status and draft communications.
Be professional. Sprint ends every other Friday.

Team: Shameek (PM), Amit (Tech Lead), Priya (Design), Raj (Backend).
Jira board: ALPHA-xxx. Slack channel: #alpha-project.
```

The agent in each group has a completely different personality, knowledge, and can even store persistent files in its group folder.

---

## Part 7: Extending NanoClaw (5 min)

NanoClaw is designed to be extended. There are three ways to do it:

### Method 1: Ask your bot directly (via WhatsApp)

Your bot runs Claude Code inside a container — it can write and modify code. Ask it to do things and it will figure out how:

```
@Andy add a tool that checks Hacker News top stories every morning
@Andy when I send you a PDF, extract the text and summarize it
@Andy start tracking my expenses when I send you receipts
```

The bot can create files, write scripts, and persist data in its group folder. It's a full coding agent, not just a chatbot.

### Method 2: Use Claude Code directly (via terminal)

Open Claude Code in the NanoClaw directory and tell it what you want:

```bash
cd nanoclaw
claude
```

Then describe the change:
```
Change the trigger word to @Jarvis
Make responses shorter by default
Add a custom greeting when someone says good morning
Connect to my Notion workspace and sync meeting notes
```

Claude reads the codebase, makes the changes, rebuilds if needed. The codebase is ~3,000 lines — small enough for Claude to safely modify any part of it.

### Method 3: Apply skills made by others

Skills are pre-built recipes that teach Claude Code how to transform your NanoClaw installation. Run them inside Claude Code:

**Add channels:**
```
/add-telegram        # Add a Telegram bot
/add-slack           # Add Slack (Socket Mode, no public URL needed)
/add-discord         # Add Discord bot
```

**Add capabilities:**
```
/add-voice-transcription   # Transcribe WhatsApp voice notes
/add-image-vision          # Understand images sent via WhatsApp
/add-pdf-reader            # Read PDF attachments
```

Skills are community-contributed. Check the [NanoClaw GitHub](https://github.com/qwibitai/nanoclaw) for available skills, or ask in the [Discord](https://discord.gg/VDdww8qS42).

### Which method to use?

| Method | When to use |
|---|---|
| **Ask the bot** | Quick automations, data tracking, things that live inside the bot's container |
| **Claude Code** | Structural changes — new channels, new integrations, modifying how NanoClaw works |
| **Skills** | Well-tested integrations that someone else already built and shared |

---

## Troubleshooting

### Bot not responding?

1. **Is NanoClaw running?**
   - Mac: `launchctl list | grep nanoclaw`
   - Windows: check the terminal where you started it
2. **Check logs:** `tail -f logs/nanoclaw.log` (Mac) or `Get-Content logs\nanoclaw.log -Wait` (Windows)
3. **Run `/debug`** in Claude Code — it checks everything

### WhatsApp disconnected?

- Look for `connection.update` in the logs
- Re-run `/setup` and redo the WhatsApp authentication step
- WhatsApp linked devices disconnect if your phone is offline for ~14 days

### Container build failing?

- Is Docker Desktop running? Check the icon in your taskbar/menu bar
- Try manually: `docker build -t nanoclaw-agent:latest ./container/`
- Low disk space? `docker system df` to check, `docker system prune` to clean up

### Composio tools not working?

- Check container logs for `COMPOSIO_API_KEY not set` — means the env var isn't reaching the container
- Verify your OAuth connections at [app.composio.dev](https://app.composio.dev) under Connected Accounts
- The agent needs network access — make sure Docker has internet connectivity

### Slow responses?

- First message is slowest (container startup + TypeScript compilation)
- Follow-up messages are faster (container stays alive for 30 min)
- Composio tool calls add latency (network round-trips to external APIs)

---

## Appendix A: NanoClaw vs OpenClaw vs Simple Telegram Bot

| | NanoClaw | OpenClaw | Simple Bot (Telegram/WhatsApp) |
|---|---|---|---|
| **Codebase** | ~3,000 lines | ~500,000 lines | ~100 lines |
| **Security** | OS-level container isolation | App-level permission checks | None |
| **Agent capability** | Full Claude Code (Bash, files, web, MCP tools) | Full Claude Code | API text completion only |
| **Customization** | Modify code directly (Claude helps) | Config files + plugins | Code it yourself |
| **Setup** | Claude Code guides everything | Complex, many config files | Manual |
| **Multi-group** | Yes, isolated containers per group | Yes | Single bot instance |
| **Scheduled tasks** | Built-in (cron, interval, once) | Built-in | Build it yourself |
| **External tools** | MCP + Composio | MCP | Build it yourself |
| **Dependencies** | Node.js, Docker | Node.js, 70+ packages | Node.js or Python |

**When to use what:**
- **NanoClaw** — you want a secure, customizable assistant you can fully understand and modify
- **OpenClaw** — you want batteries-included and don't mind complexity you can't fully audit
- **Simple Bot** — you just want basic Q&A, no tools, no file access, no scheduling

---

## Appendix B: Hosting Options

### Your machine (what we did today)

- **Cost:** Free
- **Pros:** Zero latency, access to local files and apps
- **Cons:** Only works when your machine is on and connected

### Cheap VPS ($4-12/month)

| Provider | Specs | Price |
|---|---|---|
| Hetzner CX22 | 2 vCPU, 4GB RAM | ~$4/month |
| DigitalOcean Basic | 2 vCPU, 2GB RAM | ~$12/month |
| Oracle Cloud Free | 4 ARM cores, 24GB RAM | Free forever |

**Setup on VPS:**
1. Provision Ubuntu 22.04+ or Debian 12+
2. Install Docker, Node.js 20+, Claude Code
3. `git clone`, `cd nanoclaw`, `claude`, `/setup`
4. Uses `systemd` instead of `launchd` for service management

**Key difference:** No access to local files (Granola, Obsidian, etc.). WhatsApp linked devices disconnect if your phone is offline for ~14 days.

### When to self-host vs VPS

- **Self-host:** Personal use, you want local file access, you're at your machine most of the time
- **VPS:** You want 24/7 uptime, running bots for teams/groups, don't need local file access

---

## Appendix C: Further Reading

**NanoClaw:**
- [GitHub Repository](https://github.com/qwibitai/nanoclaw)
- [Discord Community](https://discord.gg/VDdww8qS42)

**Claude & Agent SDK:**
- [Claude Code Docs](https://code.claude.com/docs)
- [Claude Agent SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [Agent Teams (Swarms)](https://code.claude.com/docs/en/agent-teams)

**Composio:**
- [Documentation](https://docs.composio.dev)
- [Tool Router Guide](https://docs.composio.dev/tool-router/overview)
- [Supported Apps](https://composio.dev/toolkits)

**Background:**
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io)
- [Baileys — WhatsApp Web API](https://github.com/WhiskeySockets/Baileys)
- [Why Container Isolation Matters](https://docs.docker.com/engine/security/)
