# Project Alpha — Self-Serve SMB Onboarding
**Priority:** High — board-level initiative; directly tied to unit economics thesis
**Target:** Onboarding time 2 weeks → 2 days, zero CSM touch

---

## Current Status
| Milestone | Owner | Due | Status |
|-----------|-------|-----|--------|
| PRD (v3) | Meera | Done | Complete |
| Figma mockups | Meera | Feb 20 | In progress |
| Eng estimation | Suresh | Done | 6-8 weeks build |
| API changes (dependency) | Rohit (Platform) | TBD | Blocked by competing priority |

## Why This Exists
- CSM team at capacity: 40 accounts each vs sustainable 25
- SMB customers churning due to 2-week onboarding lag
- Competitors (CompetitorX, CompetitorY) already have self-serve
- Board pushing on unit economics — CSM cost per SMB doesn't scale

## Key Research Finding
**60% of SMB customers want video walkthroughs, not text documentation.** This materially changes scope and budget — video production costs not yet estimated or approved.

## Success Metrics
| Metric | Target |
|--------|--------|
| Time to first value | < 48 hours |
| Onboarding completion rate | > 80% |
| CSM ticket volume from new SMBs | -60% |
| Day-30 NPS | > 45 |

## Risks (Flagged)
| Risk | Severity | Mitigation |
|------|----------|-----------|
| Platform team competing priority (payment gateway) | High | Rohit agreed to lend 2 devs — not yet confirmed |
| No video production budget approved | High | Must be scoped and approved before Feb 20 |
| No self-serve muscle in the org | Medium | Phased rollout recommended |
| Half-baked launch could worsen SMB churn | High | Define minimum viable onboarding before committing to timeline |

## Open Decisions
- Keep CSM-led flow for SMB in parallel, or sunset it?
- How to serve the 40% who need hand-holding (Meera's research)?
- Budget for video production — who approves, what is the number?
