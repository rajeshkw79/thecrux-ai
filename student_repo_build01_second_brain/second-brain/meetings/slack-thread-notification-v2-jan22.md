# Notification v2 — Webhook Deprecation (Slack Thread)
**Date:** January 22, 2025 | **Channel:** #product-launches
**⚠️ Enterprise customer impact: 14 customers affected, including Acme Corp**

---

## What Happened
Notification v2 is ready for staging. The webhook payload format has changed. Old format is deprecated — enterprise customers need 30 days notice before removal.

## Decisions Made in Thread
| Decision | Owner | Status |
|----------|-------|--------|
| Customer communication about deprecation | Arjun ("I'll own it") | **No follow-up logged** |
| Rate limit bumped from 100/min → configurable per customer | Suresh (2-day task) | **Arjun said he'd respond "tomorrow" — no record of response** |
| Acme Corp handled with extra care given renewal | Arjun (direct outreach to Anita) | **Unknown — not confirmed** |

## Risk Assessment
| Risk | Detail | Severity |
|------|--------|----------|
| No formal deprecation notice sent | 14 enterprise customers at risk | High |
| Acme Corp on affected webhook list | Renewal conversation already fragile | Critical |
| Rate limit fix not confirmed in sprint | TechCo, GlobalInc also at risk of hitting 100/min | Medium |
| No written communication plan exists | Verbal Slack commitment, no document | High |

## Required Actions (All Overdue)
- [ ] Confirm deprecation notice has been drafted and sent to all 14 customers
- [ ] Confirm direct outreach to Anita (Acme) happened
- [ ] Get Suresh confirmation on rate limit fix — was it included in next sprint?
- [ ] Document the deprecation timeline formally (not just in a Slack thread)

## Ops Note
A compliance-adjacent communication commitment was made in Slack and not tracked to completion. 14 enterprise customers — including the company's largest at-risk account — may have received no formal notice of a breaking API change. This needs immediate verification.
