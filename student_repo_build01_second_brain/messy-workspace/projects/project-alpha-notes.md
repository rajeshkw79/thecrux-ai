# Project Alpha - Internal Notes

## What is it
New self-serve onboarding flow for SMB customers. Currently onboarding takes 2 weeks with a CSM. Goal: reduce to 2 days with zero-touch.

## Why now
- CSM team is at capacity (handling 40 accounts each, should be 25)
- SMB customers churning because onboarding takes too long
- Competitors (CompetitorX, CompetitorY) have self-serve already
- Board is asking about unit economics - CSM cost per SMB customer doesn't work

## Current status
- PRD approved (Meera's doc, v3)
- Design phase: Figma mockups due Feb 20
- Eng estimation: Suresh's team says 6-8 weeks build
- Dependencies: Need API changes from Platform team (Rohit)

## Risks
1. Platform team is also working on payment gateway (competing priority)
2. We've never done self-serve - organizational muscle doesn't exist
3. If we ship half-baked self-serve, SMB churn could get WORSE
4. Meera's research showed 60% of SMBs want video walkthroughs, not docs

## Key metrics we'll track
- Time to first value (target: <48 hours)
- Onboarding completion rate (target: >80%)
- CSM ticket volume from new SMB customers (target: -60%)
- NPS at day 30 (target: >45)

## Open questions
- Do we sunset the CSM-led flow for SMB or keep both?
- How do we handle the 40% who need hand-holding (Meera's research)?
- Budget for video production (the walkthroughs)?
