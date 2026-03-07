# Build 2: Shark Tank — Pitch Under Fire

**Duration:** 60 minutes | **Skill unlocked:** Agent tool, parallel execution, agent teams, multi-perspective analysis

---

## What You'll Build

By the end of this session, you'll have:

1. Watched 5 AI shark agents evaluate a startup pitch **simultaneously** — each with a distinct personality
2. Used **parallel coaching agents** to prep a pitch across storytelling, financials, media strategy, and customer appeal
3. Run the **iterate-and-improve loop** — sharks critique, coaches fix, sharks re-evaluate — and seen the pitch get measurably stronger
4. Experienced how Claude Code can orchestrate **teams of agents** working in parallel — the most powerful pattern in AI-assisted work

**The big idea:** One Claude is useful. Five Claudes working in parallel — each with a different personality, expertise, and agenda — is a superpower. Agent teams turn Claude from an assistant into an entire advisory board.

---

## Learning Goals

- **Agents multiply perspectives** — A single AI gives you one viewpoint. Agent teams give you five competing viewpoints simultaneously, surfacing blind spots you'd never catch alone
- **Parallel execution saves time** — Instead of asking five questions sequentially (25 minutes), you ask five agents in parallel (5 minutes). Same depth, 5x faster
- **Context shapes personality** — The same AI becomes a heart-driven brand builder OR a ruthless numbers shark depending on the context you give it. Profiles are prompts
- **Iteration is the real power** — One round of feedback is useful. But the loop — critique → coach → refine → re-evaluate — is where ideas transform. And with agents, each loop takes minutes, not weeks

---

## Getting Started

Open your terminal and navigate to this repo:

```bash
cd student_repo_build02_shark_tank
claude
```

Take 2 minutes to explore what's here:

```
Look at the files and folders in this repo. Read casestudy.md to understand
what we're building today. Give me a quick summary.
```

---

## Part 1: Meet the Sharks — See Agents in Action (10 min)

The `sharks/` folder has 5 shark profiles. The `pitches/` folder has 3 startup pitches. Let's see what happens when we unleash the sharks on a pitch.

### Step 1: Read a pitch

```
Read the FarmLoop pitch in pitches/pitch_farmloop.md. Give me a 30-second
summary — the kind a founder would give in an elevator.
```

### Step 2: Unleash ONE shark

```
Read the shark profile for Nandini Rajan in sharks/shark_nandini_rajan.md.

Now, role-play AS Nandini. You've just heard FarmLoop's pitch. React the way
she would — what excites you? What concerns you? What's your first question
to the founders? Stay in character.
```

Watch how the shark profile transforms Claude's response. Same AI, completely different personality.

### Step 3: Now ALL FIVE sharks — in parallel

Now we're going to spin up **5 agents simultaneously**, each role-playing a different shark:

```
I want you to simulate a Shark Tank panel for FarmLoop. Read all 5 shark
profiles from the sharks/ folder and the FarmLoop pitch from pitches/.

Then spin up 5 agents IN PARALLEL — one for each shark. Each agent should:
1. Stay fully in character as their shark
2. Give their initial reaction to the pitch (excited, skeptical, intrigued?)
3. Ask their top 2-3 questions for the founders
4. Give a preliminary verdict: interested in a deal, on the fence, or out

Run all 5 simultaneously. I want to see how different brains see the same pitch.

Save all the shark reactions to output/findings/shark-reactions.md.
```

**Watch what happens.** Five agents spin up at the same time. Five different reactions come back. Some sharks love it, some are skeptical, some want more data. That's the power of parallel agent execution. And the reactions are saved to `output/findings/shark-reactions.md` so you can reference them later.

---

## Part 2: The Coaching Room — Parallel Prep (15 min)

The sharks just ripped the pitch apart from 5 angles. Now let's get coached. The `coaches/` folder has 5 coaching specialists.

### Step 1: Pick your pitch

Choose one of the three pitches — or if you have your own startup/business idea, use that:

- **FarmLoop** — Agritech, emotional founder story, tight runway
- **MediBridge** — Healthtech AI, strong team, ambitious valuation
- **StyleBox** — D2C fashion, solo founder, great unit economics

### Step 2: Launch the coaching team

In Part 1, you manually told Claude to spin up 5 agents. Now let's try something more powerful — **agent teams**. One natural prompt, and Claude creates a coordinated team:

```
Let's launch an agent team of coaches (from our coaches folder profiles)
to prep me for pitching [FarmLoop / MediBridge / StyleBox] on Shark Tank.
Each coach should analyze the pitch from their expertise, flag vulnerabilities
the sharks will attack, and give me specific coaching advice with exact
lines to use. Then synthesize everything into a Pitch Prep Cheat Sheet.
Save the cheat sheet to output/findings/coaching-cheatsheet.md.
```

**Watch the difference.** Claude doesn't just run 5 agents — it creates a formal team, names each coach, coordinates their work, AND synthesizes the results. One prompt did what took two steps before.

You'll get **5 coaching perspectives** synthesized into one cheat sheet:
- Ravi (veteran founder) coaching your storytelling
- Kavitha (ex-VC) stress-testing your valuation
- Priya (customer) checking if real people would buy
- Sameer (media) crafting your sound bites
- Sunil (finance) drilling your numbers

This is the meta-skill: **agent teams gather diverse perspectives AND converge them into action — in a single step.** Want to go deeper? Read the [Agent Teams documentation](https://code.claude.com/docs/en/agent-teams).

---

## Part 3: The Iteration Loop — Refine and Re-Pitch (20 min)

This is the most important part. One round of feedback is good. But the real magic is the **loop**: sharks critique → coaches fix → pitch improves → sharks re-evaluate. Each cycle takes minutes. In the real world, this loop takes weeks.

### Step 1: Identify the gaps

Look at your cheat sheet from Part 2. The coaches identified vulnerabilities. The sharks from Part 1 had concerns. Now let's address them head-on.

```
Read output/findings/shark-reactions.md and output/findings/coaching-cheatsheet.md. Based on the shark
reactions and the coaching advice, what are the 3 biggest weaknesses in
this pitch? For each weakness:

1. What exactly is the concern?
2. Which shark(s) would care most about this?
3. What's the strongest possible answer or reframe?

Write the improved answers as if the founder is speaking directly to the shark.
```

### Step 2: Build the refined pitch

```
Read output/findings/coaching-cheatsheet.md for the coaching advice. Now write a REFINED
version of the pitch — a 2-minute opening statement that incorporates
all the coaching advice. This version should:

1. Open with the strongest emotional hook (from Ravi's coaching)
2. Hit the key numbers early (from Sunil's coaching)
3. Pre-emptively address the top 2 vulnerabilities before sharks ask
4. Include the best sound bites (from Sameer's coaching)
5. End with a clear, confident ask

Write it as a script the founder would deliver.

Save the refined pitch to output/findings/refined-pitch.md.
```

### Step 3: Re-run the sharks on the improved pitch

Now the powerful moment — send the refined pitch back through the same 5 sharks:

```
Here's the refined pitch for [your startup]. Run the shark panel again —
same 5 sharks, same profiles, but THIS time they're hearing the improved
version.

Spin up 5 agents IN PARALLEL, one per shark. Each should:
1. React to the REFINED pitch (not the original)
2. Note what improved vs. the first version
3. Ask any remaining questions
4. Give their updated verdict: deal, on the fence, or out
5. If interested, state their offer (amount and equity)

Run all 5 simultaneously.

Save the updated shark reactions to output/findings/shark-reactions-v2.md.
```

**Compare the results.** Did more sharks lean in? Did the skeptics soften? Did anyone flip from "out" to "interested"? That's the iteration loop working.

### Step 4: Go another round (if time allows)

The loop is infinitely repeatable. Each cycle sharpens the pitch:

```
[If sharks still have concerns]
Two sharks are still skeptical — Vikram wants better margin clarity and
Zara wants retention data we don't have yet.

Spin up JUST those two coaches who can help:
- Sunil (financial advisor) to strengthen the margin story
- Kavitha (investor insider) to handle the "we don't have that data yet" response

Then give me updated talking points for Vikram and Zara specifically.
Save the updated talking points to output/findings/refined-pitch-v2.md.
```

Notice what just happened: you didn't re-run all 5 coaches. You targeted the specific gaps. **Precision iteration** — focus agents only where the weaknesses are.

### The Pattern You Just Learned

```
ROUND 1: Sharks evaluate → identify weaknesses
ROUND 2: Coaches address weaknesses → refine pitch
ROUND 3: Sharks re-evaluate → see improvement → new (smaller) concerns
ROUND 4: Targeted coaching on remaining gaps → final polish
...repeat until the pitch is bulletproof
```

Each round takes 3-5 minutes with parallel agents. In the real world, this would be weeks of meetings, revisions, and advisor calls. You just did it in 20 minutes.

---

## Part 4: Make It Stick (10 min)

### Step 1: The before/after comparison

```
Compare the original pitch to the final refined version side by side.
Create a "Pitch Evolution Report":

1. What changed between version 1 and the final version?
2. Which coach's advice had the biggest impact?
3. Which shark went from "out" to "interested" (or closer to interested)?
4. What's the single most important improvement?
```

This makes the iteration visible. Students can see exactly how multi-agent feedback transformed the pitch.

### Step 2: Create the CLAUDE.md pattern

```
Create a CLAUDE.md entry for the agent teams and iteration pattern:

## Agent Teams Pattern
When I need multi-perspective analysis on any decision, document, or strategy:
1. Define 3-5 distinct personas with specific expertise and viewpoints
2. Give each the same input to evaluate
3. Run all agents in parallel for speed
4. Synthesize results into a single actionable summary
5. Address the gaps and iterate — re-run the evaluation until strong

## Iteration Loop
For any high-stakes deliverable (pitch, proposal, strategy, document):
- Round 1: Evaluate with diverse agents → identify weaknesses
- Round 2: Coach/fix weaknesses → refine
- Round 3: Re-evaluate → confirm improvement → find remaining gaps
- Round 4+: Targeted fixes on specific gaps
- Each round takes minutes with parallel agents
```

### Step 3: See where else this applies

```
Give me 3 specific examples of how I could use the agent teams + iteration
pattern in my actual work as a [your role]. For each example:
- Who are the "sharks" (evaluators with different perspectives)?
- Who are the "coaches" (specialists who improve the work)?
- What's the deliverable being refined?
- How many iteration rounds would I realistically need?
```

---

## What You Built

By now, you should have:

- [ ] Seen 5 shark agents evaluate a pitch **in parallel** — each with distinct personalities
- [ ] Used 5 coaching agents **simultaneously** to prep a pitch from every angle
- [ ] Created a **synthesized cheat sheet** from diverse coaching perspectives
- [ ] Run the **iteration loop** — shark feedback → coaching → refined pitch → re-evaluation
- [ ] Watched a pitch get **measurably stronger** through agent-driven iteration
- [ ] Added the **Agent Teams + Iteration Pattern** to your CLAUDE.md

---

## Take It Home

### The Skill: Agent Teams + Iteration

What you learned today isn't about Shark Tank — it's about **using multiple AI agents with different perspectives to stress-test and iteratively improve any high-stakes deliverable.**

This pattern works for:
- **Hiring:** Spin up agents as the candidate, the hiring manager, the skip-level, the peer — each evaluates differently
- **Product launches:** Agent team as the customer, the competitor, the journalist, the investor, the support team
- **Negotiations:** Agent team as your counterpart, their boss, the mediator, your advisor
- **Strategy:** Agent team as the optimist, the pessimist, the pragmatist, the customer, the regulator
- **Writing:** Agent team as the editor, the reader, the critic, the subject matter expert

### Try the Live Pitch on Your Own

Now that you've seen the iteration loop, try the full interactive simulation at home:

```
Set up a Shark Tank simulation:

SETUP:
- I am the founder of [your startup]. I'll be pitching live.
- You will play ALL 5 sharks, staying in character based on their profiles.
- The format:
  1. I deliver my opening pitch (you listen)
  2. Sharks ask questions in rounds (each shark gets 1-2 questions per round)
  3. After 3 rounds of questions, each shark decides: deal, counter-offer, or out
  4. If any shark makes an offer, I can negotiate

RULES:
- Sharks should react to MY answers, not just ask scripted questions
- If I fumble a number, the numbers sharks (Karthik, Vikram) should pounce
- If my story is compelling, Nandini and Raj should warm up
- If my product is impressive, Zara should get interested
- Sharks can go out at any time if they hear something they don't like
- Sharks can make competing offers and try to outbid each other

Start by introducing the sharks (one line each, in character), then tell me
to begin my pitch.
```

The live simulation is where you play the founder, answer questions in real-time, negotiate deals, and experience the pressure. Use it to:
- Test your own startup or business idea
- Practice for an actual investor meeting
- Prep for a big presentation or sales pitch
- Just have fun and see if you can land all 5 sharks

### Make it YOUR pitch

```
I have my own [business idea / startup / side project / career pitch].
Here's what it is: [describe briefly]

Create a Shark Tank pitch for THIS — my real thing. Then run it through the
full iteration loop:
1. 5 sharks evaluate it in parallel
2. 5 coaches prep me in parallel
3. Refine the pitch based on feedback
4. Re-run the sharks on the improved version
5. Keep iterating until I'm confident
```

---

## If You Finish Early

### Try a different pitch
```
Run the full iteration loop with MediBridge instead.
How do the sharks react differently to a healthtech pitch vs agritech?
```

### Create adversarial sharks
```
Create a 6th shark — the most brutal, hardest-to-impress investor you can
imagine. Add them to the panel and re-run the pitch. Can you survive?
```

### Run a "Shark vs Shark" debate
```
Nandini loves FarmLoop but Karthik thinks it's overvalued.
Simulate a debate between them about whether to invest.
Each shark argues their position for 3 rounds.
```

### The post-show playbook
```
Spin up the Media Strategist coach (Sameer Khan) as an agent.
Create a "Post-Show Playbook" for [your startup]:
1. Press release draft for the day after the episode airs
2. Social media strategy for the week of airing
3. Website changes to make before the episode goes live
4. How to frame the outcome (deal or no deal) as a win
```

### Multi-round negotiation
```
I got an offer from Raj for INR 3 crore at 25% equity (I wanted 15%).
Simulate the negotiation. I'll counter-offer. Let's go back and forth
until we reach a deal or walk away.
```

---

> **Key Takeaway:** "One round of feedback is an opinion. Five perspectives iterated three times is intelligence. The best founders don't just have a good pitch — they've run it through the loop until every weakness is a strength."
