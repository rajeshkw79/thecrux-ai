# Build 2: Concept Map — How Agent Teams Work

**Read time:** 10 minutes | **When to read:** After completing the session, or if you want the theory before diving in

---

## The Big Picture

In Build 1, you learned that **one Claude + your context = a different experience**. In Build 2, you learned that **five Claudes + five different contexts = an entire advisory board**.

Here's the visual map of everything that happened:

```
                        YOUR PITCH
                            |
                            v
            +----- SHARK PANEL (Round 1) -----+
            |                                  |
     +------+------+-------+-------+-------+  |
     |      |      |       |       |       |  |
     v      v      v       v       v       |  |
  Nandini  Raj   Vikram  Zara  Karthik    |  |
  (Heart) (Gut) (Numbers)(Data) (Value)    |  |
     |      |      |       |       |       |  |
     v      v      v       v       v       |  |
   "Love  "Good  "Margins "Where's "Valuation
    the    team,   are     the      is too
   story"  but.." thin"   data?"   optimistic"
            |                                  |
            +------ shark-reactions.md  --------+
                            |
                            v
            +----- COACHING TEAM -----+
            |                         |
     +------+------+------+------+   |
     |      |      |      |      |   |
     v      v      v      v      v   |
   Ravi  Kavitha  Priya Sameer Sunil |
  (Story)(Invest)(Cust)(Media)(Fin)  |
     |      |      |      |      |   |
     v      v      v      v      v   |
   "Open  "Pre-  "Lead  "Your  "Show
    with   empt   with   sound  unit
    the    the    the    bite   econ
   farm"  ask"   user"  is.."  early"
            |                         |
            +-- coaching-cheatsheet.md +
                            |
                            v
                    REFINED PITCH
                            |
                            v
            +----- SHARK PANEL (Round 2) -----+
            |                                  |
     +------+------+-------+-------+-------+  |
     |      |      |       |       |       |  |
     v      v      v       v       v       |  |
  Nandini  Raj   Vikram  Zara  Karthik    |  |
     |      |      |       |       |       |  |
     v      v      v       v       v       |  |
    DEAL!  DEAL! "Better, "Still  "Moved   |  |
                  leaning  need   from 5x
                  in"     data"  to 4x"    |  |
            |                                  |
            +--- shark-reactions-v2.md  --------+
                            |
                            v
                   TARGETED COACHING
                    (only the gaps)
                            |
                            v
                      FINAL PITCH
```

---

## Four Core Concepts

### 1. Agents = Claude with a Character Sheet

An agent is just Claude given a detailed profile and told to stay in character. Nothing magical — it's Build 1's lesson (context shapes output) applied at scale.

```
  +------------------+        +------------------+
  |   SAME Claude    |        |   SAME Claude    |
  |                  |        |                  |
  |  + Nandini's     |        |  + Karthik's     |
  |    profile       |        |    profile       |
  |                  |        |                  |
  |  = Emotional,    |        |  = Ruthless,     |
  |    founder-      |        |    valuation-    |
  |    first         |        |    obsessed      |
  |    investor      |        |    investor      |
  +------------------+        +------------------+
```

The profile IS the prompt. A vague profile gives a generic response. A rich profile — with decision-making style, pet peeves, signature questions — creates a convincing character.

**Why this matters beyond Shark Tank:** Any time you need a perspective, write a profile. A skeptical customer. A hostile journalist. A cautious CFO. A supportive mentor. The profile turns Claude into that person.

---

### 2. Parallel Execution = Width, Not Depth

Without agents, you ask questions one at a time. Each answer builds on the last. That's **depth** — useful, but slow.

With parallel agents, you ask the same question to five different perspectives simultaneously. That's **width** — you get the full landscape in one shot.

```
  SEQUENTIAL (without agents)          PARALLEL (with agents)

  Ask Nandini -----> wait              Ask all 5 ----> wait once
  Ask Raj ---------> wait                   |
  Ask Vikram ------> wait              All 5 respond
  Ask Zara --------> wait              simultaneously
  Ask Karthik -----> wait

  Total: 5 waits                       Total: 1 wait
  Time: ~5 minutes                     Time: ~1 minute
  Same quality                         Same quality
```

**The pattern:** Diverge for perspectives, converge for action.

- **Diverge:** Run multiple agents with different profiles on the same input. You get 5 honest, independent reactions — they don't influence each other.
- **Converge:** Synthesize the 5 reactions into one actionable summary. What do they agree on? Where do they disagree? What's the consensus?

---

### 3. Agent Teams vs. Parallel Agents — One Level Up

Parallel agents (Part 1) and agent teams (Part 2) look similar but are fundamentally different:

```
  PARALLEL AGENTS                    AGENT TEAMS
  (you orchestrate)                  (Claude orchestrates)

  You: "Spin up 5 agents,            You: "Launch a coaching team
        one per shark, and                 to prep my pitch."
        evaluate FarmLoop."
                                      Claude:
  Claude:                             - Creates the team
  - Runs 5 agents                     - Names each member
  - Returns 5 responses               - Assigns roles
                                      - Coordinates their work
  You: "Now synthesize."              - Synthesizes into one output
                                      - Returns a cheat sheet
  Claude: Synthesizes.
                                      One prompt. Done.
  Two steps.
```

**The key difference:**

| | Parallel Agents | Agent Teams |
|---|---|---|
| **Who orchestrates?** | You | Claude |
| **Synthesis** | Separate step | Automatic |
| **Output** | 5 separate responses | 1 coordinated deliverable |
| **Prompts needed** | 2 (run + synthesize) | 1 (describe what you need) |
| **Best for** | Explicit control, seeing raw reactions | Efficiency, when you want a ready-to-use output |

**Why the distinction matters:** As you get comfortable with agents, you'll shift from manually orchestrating everything (parallel agents) to describing outcomes and letting Claude coordinate the team (agent teams). This is the same shift a manager makes — from doing the work to directing a team. The skill is knowing which mode fits the situation.

---

### 4. The Iteration Loop = Compress Weeks into Minutes

One round of feedback is an opinion. Three rounds of feedback, with coaching in between, is transformation.

```
  THE LOOP:

  +---> EVALUATE (sharks) ----+
  |         |                  |
  |         v                  |
  |     Weaknesses             |
  |     identified             |
  |         |                  |
  |         v                  |
  |     COACH (coaches) ----+  |
  |         |               |  |
  |         v               |  |
  |     Refined pitch       |  |
  |         |               |  |
  +-------- + <-------------+  |
            |                  |
            v                  |
        EVALUATE again --------+
            |
            v
        Smaller gaps
            |
            v
        TARGETED coaching
        (only 1-2 coaches)
            |
            v
        Final version

  Each loop: ~5 minutes
  Real world equivalent: ~2-4 weeks
```

**Why the loop works:** Each round catches different problems.

| Round | What it catches | Improvement |
|-------|----------------|-------------|
| 1 | Big structural issues — missing data, weak opening, wrong emphasis | ~70% |
| 2 | Subtler issues — tone, specific objections, sound bites | ~20% |
| 3 | Polish — word choice, confidence, flow | ~10% |

After 3 rounds, you've captured ~100% of what agents can find. Further improvement requires real-world data (actual customer reactions, real investor meetings).

---

## How the Pieces Fit Together

```
  BUILD 1                    BUILD 2

  CLAUDE.md                  Agent Profiles
  (your context)             (character contexts)
       |                          |
       v                          v
  Claude knows YOU           Claude becomes THEM
       |                          |
       v                          v
  Personalized output        Multiple perspectives
                                   |
                                   v
                             Parallel execution
                             (5 at once)
                                   |
                                   v
                             Iteration loop
                             (evaluate -> coach -> refine)
                                   |
                                   v
                             Measurably better output
```

Build 1's lesson: context is the #1 lever.
Build 2's lesson: **multiply that lever** — five contexts, running in parallel, iterated until strong.

---

## The Pattern, Generalized

You can apply this to any high-stakes deliverable. Replace "sharks" and "coaches" with whatever fits:

```
  +------------------+------------------+-------------------+
  | YOUR SITUATION   | "SHARKS"         | "COACHES"         |
  |                  | (evaluators)     | (improvers)       |
  +------------------+------------------+-------------------+
  | Pitch deck       | Investors with   | Story, finance,   |
  |                  | different thesis | design advisors   |
  +------------------+------------------+-------------------+
  | Job interview    | Hiring manager,  | Career coach,     |
  |                  | skip-level, HR,  | industry mentor,  |
  |                  | peer, recruiter  | interview prep    |
  +------------------+------------------+-------------------+
  | Product launch   | Customer, press, | PM, marketer,     |
  |                  | competitor,      | engineer,         |
  |                  | regulator        | support lead      |
  +------------------+------------------+-------------------+
  | Strategy doc     | Optimist,        | Domain experts    |
  |                  | pessimist,       | for each risk     |
  |                  | pragmatist, CEO  | area              |
  +------------------+------------------+-------------------+
  | Sales proposal   | Buyer, their     | Pricing, value    |
  |                  | boss, finance,   | prop, objection   |
  |                  | legal, end user  | handling          |
  +------------------+------------------+-------------------+
```

The formula is always the same:

1. **Define 3-5 evaluator profiles** (the "sharks") — people who will judge your work from different angles
2. **Run them in parallel** on your first draft — get the full landscape of reactions
3. **Save the output** — so you don't lose context
4. **Define 3-5 coach profiles** (the "coaches") — specialists who can fix the gaps
5. **Run them in parallel** — get targeted advice from every angle
6. **Save the coaching output** — so you can reference it during refinement
7. **Refine** the deliverable using the coaching
8. **Re-run the evaluators** on the refined version — measure improvement
9. **Target remaining gaps** with specific coaches — precision, not breadth
10. **Repeat** until strong

---

## One Sentence to Remember

> Five perspectives, iterated three times, in thirty minutes — that's not a shortcut. That's a better process than most teams run in a month.
