# Build 5: Roast, Fix, Ship

**Duration:** 90 minutes | **Skill unlocked:** Multi-agent critique, iterative design, production deployment, real-world shipping

---

## Dependency: Install the Frontend Design Skill

This session generates production-quality HTML. Before starting, install the `frontend-design` plugin — it gives Claude the design knowledge to produce polished, professional layouts rather than generic output.

**Step 1: Add the Anthropic plugins marketplace** (once, not needed again after this)

Inside Claude, run:

```
/plugin marketplace add anthropics/claude-code
```

**Step 2: Install the frontend-design plugin**

```
/plugin install frontend-design@anthropics-claude-code
```

**Step 3: Activate it at the start of every Claude session for this build**

```
/frontend-design
```

If it responds with design guidance, you're set.

> This skill must be active before you generate any HTML in this session. All generation phases — copy variants, design variants, and final page — depend on it for production-quality output.

---

## What You'll Build

By the end of this session, you'll have:

1. A production-quality landing page for a real product — built entirely by Claude, refined by you
2. Experienced a structured multi-variant workflow: 2 copies → pick → 2 designs → pick → 2 logos → final
3. Had a team of 5 AI experts roast your page, debate it, and hand you a prioritised fix list
4. Deployed a live website to a public URL on Vercel — something you can share tonight
5. (Stretch) A working lead gen form with responses captured in Supabase

**The big idea:** Claude doesn't just generate — it iterates. The gap between "good enough" and "actually good" is one more round of structured critique. This session is about building that loop.

---

## Learning Goals

- **Variation is the superpower** — Generating 2 versions and comparing them produces dramatically better output than generating 1 and trying to improve it. Volume first, curation second.
- **Context compounds** — Every decision you make (which copy, which design, which logo) gets fed back into Claude as context, and the final result reflects all of it.
- **Multi-agent critique beats self-review** — A panel of AI experts with distinct perspectives finds things you and Claude would both miss. This is the roast — and it's the most valuable part.
- **Shipping is a Claude skill** — From HTML file to live URL, Claude can walk you through deployment step by step. The terminal is not scary when you have a guide.

---

## Before You Start

Open your terminal and navigate to this repo:

```bash
cd student_repo_build05_roast_fix_ship
claude
```

Read the founder profile first. This is your brief:

```
Read the founder profile in founder-profile/priya-nair.md carefully.
Tell me in 3 bullet points: who is the target customer, what is the
core product promise, and what does Priya want the homepage to do.
```

Make sure Claude understood the brief before you generate anything.

> **Output folder structure:** All generated files go into organised subfolders. Claude will create these automatically when it saves files:
>
> - `output/html/` — all HTML pages (copy variants, designs, final pages, hubs)
> - `output/logos/` — SVG logo files
> - `output/findings/` — expert roast fix list

---

## Phase 1: Two Copies (15 min)

You're going to generate 2 complete HTML landing pages — each with a different copywriting angle. Same product. Dramatically different positioning.

### Why 2 before you choose

One version is a guess. Two gives you a real contrast. You'll quickly see which angle speaks to your audience and which one doesn't feel right — and that clarity is what makes the next step fast.

### Generate Both Copy Variations — In Parallel

```
Read founder-profile/priya-nair.md thoroughly.

Now use parallel agents to generate both copy variations simultaneously.
Spawn 2 separate agents and have them run at the same time:

Agent 1 → output/html/copy-v1.html: Lead with Priya's founder story. Emotional,
  specific, personal. The moment she saw smart people wasting 30%
  of their week.

Agent 2 → output/html/copy-v2.html: Lead with ROI and time saved. Data-driven.
  Open with a stat like "Your team spends 11 hours a week on tasks
  that should already be automated."

Both must include: hero (tagline + CTA), core offering, how it works
(3 steps), pricing table (Free/Pro/Team/Enterprise with INR prices from
the brief), competition comparison, about (story, team, vision/mission),
iOS/Android app download placeholders, footer with T&C and Privacy.
Mobile-friendly. Fully self-contained HTML.

Important constraint: Do not mention any real brand names, real company
names, or real investor names anywhere in the copy. Use generic descriptors
instead (e.g., "a leading payments platform" instead of a specific company
name, "backed by a top-tier Indian VC" instead of a named fund).

Apply frontend-design skill standards to all HTML output: strong visual
hierarchy, consistent spacing scale, clean typography, polished components.

Confirm when both are done.
```

> **What just happened:** You didn't issue 2 prompts. You issued 1 and Claude orchestrated 2 agents in parallel. This is the agent concept from earlier today — applied to building your product. This is how you 2x your output without 2x the effort.

---

## Phase 1 Checkpoint: The Comparison Tool

Now generate a comparison page so you can see all 5 side by side and pick your winning elements:

```
I have 2 HTML files in output/html/: copy-v1.html and copy-v2.html,
all for theboringtasks.com.

Create output/html/comparison.html that does the following:
1. Shows each major section (hero headline + subtext, features, pricing, about intro)
   from both versions in a side-by-side comparison table
2. Puts a checkbox next to each section in each version so I can select my favourite
3. Adds a "Generate My Prompt" button at the bottom that — when clicked — looks at
   my checkbox selections and generates a Claude prompt I can copy. The prompt should
   instruct Claude to build the final copy using specifically the sections I selected
   (e.g., "Use the hero from V2, the features section from V4, the pricing from V1...")

Make comparison.html fully functional. Open it in a browser to use it.
```

Open `output/html/comparison.html` in your browser. Read each section. Check the boxes for what resonates. Click "Generate My Prompt". Copy the output — you'll use it next.

---

## Phase 2: Two Designs (15 min)

You now have your winning copy direction. Time to generate 2 visually distinct designs.

**First, add reference screenshots to the references/ folder** — read the README.md there for instructions. Even 2-3 screenshots will significantly improve Claude's design output.

**Then: pick your 2 design directions.**

Choose from the list below — or write your own. Pick the two that feel closest to your product's personality.

| #   | Style                      | Feels like                      |
| --- | -------------------------- | ------------------------------- |
| A   | Dark mode, technical-clean | Linear, Raycast, Vercel         |
| B   | Clean white, modern SaaS   | Notion, Clerk, Stripe           |
| C   | Warm and human             | Framer, Superhuman, Loom        |
| D   | Bold and editorial         | Dropbox, Mailchimp, Figma       |
| E   | Minimal and typographic    | iA Writer, Readwise, Craft      |
| F   | My own direction           | Describe it in the prompt below |

Pick any 2 from A–F. Then use this prompt, filling in your choices:

```
Using the winning copy direction from my comparison selections, spawn 2 parallel
agents to generate design variations simultaneously:

Agent 1 → output/html/design-v1.html: [paste your first choice — e.g., "Dark mode,
  technical-clean (think Linear, Raycast)" or describe your own direction]

Agent 2 → output/html/design-v2.html: [paste your second choice — e.g., "Warm and
  human — softer tones, approachable, less corporate" or describe your own direction]

Each agent should also check the references/ folder for screenshots and factor
in the visual aesthetic it finds there.

Both must include: SVG logo placeholder, mobile responsive layout, working
hover states on CTAs. Apply frontend-design skill standards: production-grade
layout, intentional colour palette, refined spacing, pixel-clean components.
Confirm when both are done.
```

### Design Comparison Hub

```
Create output/html/design-hub.html that shows a visual comparison of my 2 design
variations (all in output/html/). Include thumbnail previews (use iframes scaled
down to 25%) and direct links to open each full design. Add a "Notes" field next
to each where I can type what I like about it. Make it look professional — this
is my design review board.
```

Open `output/html/design-hub.html`, click through each design, and decide which one or which combination of elements you want.

### Extract the Color Palette (30 seconds)

Once you've picked your design, extract its exact colors — you'll need these for the logo and final page:

```
Read output/html/design-v[X].html (my chosen design) and extract:
- Primary background color
- Primary text color
- Accent / CTA color (the main button or highlight color)
- Secondary / supporting colors if any

List them as hex codes. I'll use these to keep the logo and final page consistent.
```

Note down the hex codes — you'll paste them into the next two phases.

---

## Phase 3: The Logo (10 min)

Two logo directions, both in SVG.

```
Based on the founder brief in founder-profile/priya-nair.md, generate 2 different
SVG logo designs for theboringtasks.com. Each should be a mark + wordmark combination.

Rules from Priya's brief:
- Must work on both dark and light backgrounds
- No robots, no gears, no brains, no AI clichés
- The mark should suggest: repetition, reliability, a task being completed, or a loop
- The name is intentionally boring — the logo can lean into that dry confidence

Design direction chosen: [paste your chosen style, e.g., "Dark mode, technical-clean"]
Color palette from chosen design:
- Background: [hex]
- Text: [hex]
- Accent: [hex]

Generate logos that use or complement this palette. The mark color should either use
the accent color directly or a hue that harmonises with it.

Save each as an individual SVG file in output/logos/: logo-v1.svg and logo-v2.svg.

Create output/html/logos-showcase.html that displays both logos at various sizes
(small, medium, large) on both dark and light backgrounds so I can evaluate them
properly. Reference the SVGs using relative path ../logos/logo-vX.svg.
```

Open `output/html/logos-showcase.html`. Pick your favourite. Note the filename.

---

## Phase 4: The Final Page (10 min)

Bring it all together. One final, complete, production-quality page.

```
I've made my selections:
- Copy direction: [describe which copy angle you chose and what you liked about it]
- Design direction: [describe which design variation you chose, or what you're combining]
- Logo: [state which logo file, e.g., output/logos/logo-v2.svg]

Color palette to use throughout (from my chosen design):
- Background: [hex]
- Text: [hex]
- Accent: [hex]

Build the final production version: output/html/final-v1.html

This should be the complete website with all sections:
hero, core offering, how it works, pricing, competition comparison, about
(story, team, vision/mission), iOS/Android app download placeholders,
T&C and Privacy placeholders in footer.

Inline the chosen logo SVG directly into the HTML. Ensure the inlined logo's mark
color matches or complements the accent color above. If there is any mismatch between
the logo SVG colors and the design palette, adjust the SVG fill values to harmonise.
The final page should look like the logo and design were made together.

Apply frontend-design skill standards throughout — this is the production version:
real CSS (not inline styles), strong visual hierarchy, refined spacing scale, mobile
responsive. No placeholder lorem ipsum — all copy should be final and polished.
```

Open `output/html/final-v1.html`. This is your draft for the roast.

---

## Phase 5: The Expert Roast (15 min)

This is the session's centrepiece. You're going to assemble a panel of 5 experts and have them critique your page — together.

They will argue, disagree, and push each other. The output will be a prioritised fix list: P0 (launch blocker), P1 (important before launch), P2 (nice to have).

```
I need a critical expert review of my landing page at output/html/final-v1.html.

Assemble a panel of 5 experts and simulate a discussion between them. Each expert
should read the full page, give their honest reaction, challenge each other's views,
and together produce a final consolidated feedback list.

The experts:

1. Shreya Iyer — Senior Brand Strategist & Copywriter. 12 years in B2B SaaS.
   Her lens: Does the copy speak to a real person? Is there a clear point of view?
   Is it distinctive or generic?

2. Marcus Tan — Product Designer, obsessed with conversion. Ex-Figma, ex-Stripe.
   His lens: Does the visual design serve the message? What's the first thing you see?
   Are the CTAs clear? Mobile experience?

3. Ankit Verma — Growth Marketer. Runs paid acquisition for Series A/B SaaS startups.
   His lens: Would I pay to send traffic to this page? What's the conversion rate going
   to be? Is the value prop clear in 5 seconds?

4. Meera Nambiar — VP Operations at a 250-person logistics company. The exact target
   customer. She is busy, sceptical of AI hype, and has been burned by tools that
   overpromised. Her lens: Does this feel like it's for me? Do I trust it? Will I join
   the waitlist?

5. Rohit Kapoor — Angel investor who has reviewed 600+ pitch decks and landing pages.
   His lens: Is the positioning credible? Is the market real? Does this look like a
   real company or a weekend project?

Format:
- Start with each expert's first reaction (2-3 sentences each)
- Then show the discussion where they debate at least 3 major points
- End with their consolidated feedback list sorted into P0, P1, P2

P0 = launch blocker — this must be fixed before any paid traffic goes to this page
P1 = important — fix before public launch
P2 = nice to have — do eventually but not blocking
```

Read the output carefully. This panel will find things you missed.

---

## Phase 5 Checkpoint: Your Fix List

After the roast, generate your personal fix list:

```
Based on the expert panel feedback, show me a clean table with:
- Priority (P0 / P1 / P2)
- What to fix
- Which expert raised it
- Estimated effort (small / medium / large)

Add a checkbox next to each row. I want to select which fixes to apply.

Also save this table as output/findings/fix-list.md so I have a record of it.
```

Read through the table. Check the boxes for the fixes you want. Note: you don't have to implement every P1. Use your judgment. This is your product.

---

## Phase 6: Apply the Fixes (10 min)

```
Apply the following fixes to output/html/final-v1.html and save the updated
version as output/html/final-v2.html:

[List the specific fixes you selected — copy the descriptions from the table]

After making the changes, summarise what you changed and why each change addresses
the feedback it was responding to.
```

Open `output/html/final-v2.html`. Compare with `output/html/final-v1.html`. Feel the difference.

---

## Phase 7: Ship It — Deploy to Vercel (10 min)

Your page is production-ready. Time to put it on the internet. You'll push your final page to GitHub and then deploy from GitHub on Vercel — the same way real products are shipped.

Pick your path based on what you have available.

---

### Path A: Let Claude do it (recommended if gh CLI is set up)

**Check if you're ready:**

```bash
gh auth status
```

If it shows your GitHub username, skip the install step and run the Claude prompt below.

> **Note:** The install and auth steps below require your input in the terminal and browser. Once `gh auth status` shows your username, Claude handles the rest.

If it says `command not found`, install gh CLI first:

**Mac:**
Go to [github.com/cli/cli/releases/latest](https://github.com/cli/cli/releases/latest), download the **macOS universal** `.pkg` file, and run it.

Alternatively, if you have Homebrew installed (`brew --version` prints a version number), run: `brew install gh`

**Windows:**
Go to [github.com/cli/cli/releases/latest](https://github.com/cli/cli/releases/latest), download the **Windows amd64** `.msi` file, and run it.

Already have winget? You can also run: `winget install GitHub.cli`

Then authenticate:

```bash
gh auth login
```

Choose **GitHub.com → HTTPS → Login with a web browser** and follow the prompts.

**Now run this in your Claude session:**

```
I want to push my landing page to GitHub so I can deploy it. Please:
1. Find the thecrux-ai-bootcamp folder in my home directory and create a
   new subfolder called my-landing-page inside it
2. Copy output/html/final-v2.html into it and rename it to index.html
3. Create a new public GitHub repository called my-landing-page
4. Initialise git in that folder, commit the file, and push it to the new repo

Do this step by step. Tell me if you need me to do anything in the browser.
```

Claude will handle everything. Just follow along.

---

### Path B: Do it manually on GitHub (no tools needed)

**Step 1: Rename your file first**

Before uploading, rename `final-v2.html` to `index.html` on your computer. Open your `output/html/` folder in Finder or File Explorer, right-click the file, and rename it.

**Step 2: Create a GitHub repository and upload**

1. Go to [github.com](https://github.com) and sign in (or create a free account)
2. Click **+** (top right) → **New repository**
3. Name it `my-landing-page`, set it to **Public**, click **Create repository**
4. On the next page, click **uploading an existing file**
5. Drag `index.html` onto the upload area
6. Click **Commit changes**

Your file is now on GitHub.

---

### Step 2: Deploy from GitHub on Vercel

1. Go to [vercel.com](https://vercel.com) and sign up / sign in (free account)
2. Click **Add New → Project**
3. If you're asked to connect a Git provider, click **Connect GitHub** and authorise Vercel — this is a one-time step
4. Click **Import** next to your `my-landing-page` repository
5. Leave all settings as default
6. Click **Deploy**

Vercel will give you a live URL in about 30 seconds. Share it.

> **Bonus:** Every time you push new changes to GitHub from now on, Vercel will automatically redeploy. Your URL always stays current.

### Step 3 (optional): Connect a custom domain

Your `vercel.app` URL is permanent and shareable — you don't need a custom domain. But if you own one and want to connect it, see the separate guide:

📄 **[custom-domain-setup.md](./custom-domain-setup.md)** — step-by-step instructions for connecting any domain (GoDaddy, Namecheap, Google Domains, etc.) to your Vercel deployment.

---

## Lock In the Pattern

You just ran the most complete creative workflow of the bootcamp. Save it to your CLAUDE.md so you can reuse it for any product, service, or personal brand.

```
Add a new section to my CLAUDE.md called "## Creative Shipping Workflow".

Include:

### The Pattern
Brief → 2 copy variants (parallel) → compare → 2 design variants (parallel) → logo → final → expert roast → fix → ship

### Expert Roast Panel
Save the full panel so I can reuse it anytime:
- Shreya Iyer — Brand Strategist. Lens: Is the copy distinctive? Does it speak to a real person?
- Marcus Tan — Product Designer. Lens: Does the design serve the message? Are CTAs clear?
- Ankit Verma — Growth Marketer. Lens: Would I pay to send traffic here? 5-second value prop?
- Meera Nambiar — VP Ops (target customer). Lens: Do I trust this? Is it for me?
- Rohit Kapoor — Angel investor. Lens: Is the positioning credible? Real company or weekend project?

### What I Shipped
- Product: theboringtasks.com (Priya Nair's product — the demo)
- Live URL: [paste your Vercel URL]
- Copy direction: [what you chose and why]
- Design direction: [what you chose and why]
```

Now when you want to launch something — a landing page, a product, a personal brand — ask Claude: "Run the creative shipping workflow on this." It knows the pattern.

---

## What You Built

- [ ] 3 HTML copy variations for theboringtasks.com
- [ ] A working comparison tool that generated a build prompt
- [ ] 3 visual design variations
- [ ] A design review hub
- [ ] 3 SVG logo options
- [ ] A production-quality final landing page
- [ ] A multi-agent expert critique with P0/P1/P2 feedback
- [ ] A fixed final version incorporating selected feedback
- [ ] A live URL on Vercel

---

## Take It Home

Everything you just did works for any product, service, or personal brand you want to launch. The workflow is reusable:

**The pattern:**

```
Brief → 5 copies → compare → 5 designs → compare → logo → final → roast → fix → ship
```

To use this for your own product:

1. Create a new folder
2. Write a founder brief (use priya-nair.md as a template)
3. Add reference screenshots to a references/ folder
4. Run the same phases with your content

The agent panel works for anything — landing pages, pitch decks, product specs, marketing campaigns. Change the experts to match what you're building. A legal brief needs a lawyer in the panel. A pitch deck needs an investor and a founder who failed once.

---

## If You Finish Early

**Stretch Goal: Lead Gen Form + Supabase**

Add a working waitlist signup to your deployed page:

```
I want to add a waitlist form to output/html/final-v2.html. When someone enters their name,
email, and role and clicks "Join Waitlist", the data should be saved to a
Supabase table.

Walk me through:
1. Creating a Supabase project and table (waitlist: id, name, email, role, created_at)
2. Getting the Supabase URL and anon key
3. Adding the Supabase JS SDK to my HTML file
4. Wiring up the form to insert a row on submit
5. Showing a success message after submission

Give me step-by-step instructions I can follow from the Supabase dashboard.
```

**Stretch Goal: Make It Next.js**

If you want to go further and learn how to turn this into a proper React app:

```
I have a landing page at output/html/final-v2.html. Walk me through converting it to a
Next.js app so it can have dynamic routes, server-side rendering, and easier
component management. Assume I have Node.js installed but have never set up
a Next.js project before.
```

**Stretch Goal: Customise for YOUR product**

You've been building for Priya's product. Now build for yours:

```
I want to build a landing page for my own product/service: [describe it].
Here is my target customer: [describe].
Here is my pricing model: [describe].
Start by asking me the questions you need to build a founder brief like the
one in founder-profile/priya-nair.md. Then we'll run the same 3-copy → 3-design
→ logo → final → roast workflow.

```

---

## Key Takeaway

> "You didn't just build a website today. You built a workflow. Brief, generate, compare, decide, roast, fix, ship. That workflow works for anything you want to put into the world — and you can run it in an afternoon."

---

## The Bigger Picture

You've now done all 5 builds. Look at what you've accumulated in your CLAUDE.md across the sessions. Claude knows:

- Who you are and what you do
- Your communication style
- Your tools and how you like to work
- How to analyse data in your context
- How to think from multiple expert perspectives
- How to build and ship real things

This is not the end of the journey. This is the starting line. Every week from here, you're faster.
