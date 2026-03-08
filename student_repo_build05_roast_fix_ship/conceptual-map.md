# Build 5: Conceptual Map — What Just Happened (and Why)

**Read time:** 10 minutes | **When to read:** After you've completed the session, or if you want to understand the thinking behind the workflow before you start.

---

## The One-Sentence Version

You ran a professional creative production pipeline — the same loop that agencies, studios, and product teams use — compressed into 90 minutes with AI as your entire team.

---

## The Three Mental Models Behind This Session

### 1. Diverge, Then Converge

The biggest shift in this session is how you used AI.

In most AI interactions, you ask for **one thing** and try to make it better. That's the "perfection-first" model — prompt, evaluate, tweak, re-prompt, repeat. It feels productive but it's actually slow and narrow. You're optimising within a single direction you chose before you knew the options.

Build 5 flips this. You generated **3 versions** of everything — copy, design, logos — before making any decisions. This is the "diverge-converge" model:

```
DIVERGE                          CONVERGE
  |                                 |
  |   V1 (founder story)           |
  |   V2 (ROI data)         -->  Pick elements  -->  Final page
  |   V3 (launch energy)          |
  |                                |
```

**Why 3?** One version is a guess. Two is a coin flip. Three is the minimum where you develop a real opinion. By V3, you're not just reacting ("this is bad") — you're comparing ("V1's hero is stronger but V3's pricing section converts better"). That's creative direction, not prompting.

**The principle:** Generate volume first. Curate deliberately second. This works for landing pages, pitch decks, proposals, email campaigns, product names — anything where the "right answer" is a matter of taste and context.

---

### 2. Context Compounding

Every decision you made in this session became input for the next stage.

```
Founder brief
    |
    v
3 copy variants --> You pick hero from V1, pricing from V3
    |
    v
3 design variants --> You pick dark mode with V2's layout
    |
    v
Logo selection --> You pick the minimal mark
    |
    v
Final page (reflects ALL your choices)
    |
    v
Expert roast (reads your final page with full context)
    |
    v
Fixed version (addresses specific feedback on YOUR page)
```

This is not Claude getting smarter. It's Claude getting **more context**. The final page feels like "yours" because it literally is — it's the accumulation of 10+ micro-decisions you made along the way, each one fed back in.

**The principle:** AI output quality is a function of context, not prompt cleverness. The more decisions you make and feed back, the more the output reflects your judgment. This is why CLAUDE.md matters — it's context that persists across sessions.

---

### 3. Multi-Perspective Critique (The Roast)

This is the conceptual centrepiece of the session.

All weekend, you worked with Claude as **one voice**. One assistant, one perspective. The expert roast changed that. You asked Claude to simulate **5 distinct perspectives** — each with different incentives, different expertise, and different definitions of "good."

| Expert | Their Lens | What They Catch |
|--------|-----------|-----------------|
| Shreya (Brand Strategist) | Is the copy distinctive? | Generic messaging, weak positioning |
| Marcus (Product Designer) | Does design serve the message? | Visual hierarchy problems, CTA confusion |
| Ankit (Growth Marketer) | Would I pay to send traffic here? | Unclear value prop, conversion friction |
| Meera (Target Customer) | Do I trust this company? | Missing trust signals, AI hype, vagueness |
| Rohit (Investor) | Is this positioning credible? | Market confusion, "weekend project" feel |

**Why this works better than asking "is my page good?":**

A single reviewer optimises for one thing. Meera doesn't care about your colour palette — she cares whether she'd give you her email. Rohit doesn't care about the CTA button — he cares whether the market positioning is defensible. When they disagree (and they do), the friction surface is where the real insights live.

**The principle:** One perspective finds problems. Multiple perspectives find the *right* problems. When you need to evaluate creative work, assemble a panel with diverse incentives — not just diverse titles. A lawyer, a customer, and a competitor will find different things than three marketers.

---

## The Complete Workflow Pattern

Here's the full pattern you ran, abstracted from the specific session:

```
1. BRIEF          Write down who it's for, what it does, what success looks like.
                   (10 min of brief saves hours of wrong-direction work.)

2. DIVERGE        Generate 3+ variants with distinct angles.
                   Don't iterate on one. Explore the range.

3. COMPARE        Build a comparison view. See them side by side.
                   Your taste activates when you compare, not when you stare at one thing.

4. CONVERGE       Pick elements. Mix and match. Describe your selection specifically.
                   "Hero from V1, pricing from V3" — not "make it better."

5. ASSEMBLE       Generate the final version from your selections.
                   Context from all prior decisions compounds here.

6. ROAST          Multi-perspective critique. 3-5 experts with different lenses.
                   P0 (launch blocker) / P1 (fix before launch) / P2 (nice to have).

7. FIX            Apply selected fixes. You decide what's worth fixing today
                   vs. what's version 2. You're the founder, not the panel.

8. SHIP           Deploy. Get a URL. Make it real.
                   An imperfect thing on the internet beats a perfect thing on your laptop.
```

This pattern is not specific to landing pages. It works for:

- **Pitch decks** — 3 narrative angles, compare, roast with an investor + customer + co-founder panel
- **Proposals** — 3 positioning strategies, compare, roast with the client's perspective in the panel
- **Product specs** — 3 approaches to the same problem, compare, roast with engineering + design + customer
- **Email campaigns** — 3 subject line / body combinations, compare, roast with a deliverability expert + target reader
- **Personal brand** — 3 bio directions, compare, roast with your industry peers + a recruiter + a journalist

The experts change. The workflow doesn't.

---

## What's Actually Happening Under the Hood

A few things worth understanding about what Claude did during this session:

**Parallel agents (Phase 1 and 2):** When you asked Claude to generate 3 variants "simultaneously," it spawned separate sub-agents — each working on one variant independently. This is not Claude writing V1, then V2, then V3 in sequence. The agents run in parallel, which is why 3 variants take roughly the same time as 1. This is the "agents" concept made practical.

**File system as memory:** Claude read the founder brief from a file, wrote HTML files, read them back for the roast, and wrote the fix list to another file. The file system is Claude's working memory across a complex multi-step workflow. This is why organising output into folders (output/html/, output/logos/, output/findings/) matters — it's not just tidiness, it's giving Claude a structured workspace.

**The comparison tool:** When Claude generated comparison.html with checkboxes and a "Generate My Prompt" button, it built a small interactive application that creates a prompt for itself. You used a Claude-generated tool to give Claude better instructions. This is a pattern worth remembering: Claude can build tools that make Claude work better.

**The roast as structured prompting:** The expert panel is not magic. It's a structured prompt that forces Claude to evaluate the same artifact from 5 distinct angles with 5 distinct success criteria. You could achieve something similar by running 5 separate prompts ("evaluate this as a brand strategist... now as a growth marketer..."), but the discussion format creates something extra: the experts challenge each other, which surfaces tensions that isolated reviews miss.

---

## The Takeaway

You didn't learn how to build a website today. You learned a workflow for turning ideas into real things:

**Brief. Diverge. Compare. Converge. Roast. Fix. Ship.**

The website was just the proof that it works. The workflow is what you keep.
