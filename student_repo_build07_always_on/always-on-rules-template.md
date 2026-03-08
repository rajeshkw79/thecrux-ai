# Always-On Rules Template

Copy this section into your CLAUDE.md and fill in the blanks. These rules tell Claude what deserves your attention and what doesn't.

---

```markdown
## Always-On Rules

### URGENT (alert me immediately on Telegram):
- Emails from: [name 1, role], [name 2, role]
- Keywords in subject/body: urgent, deadline, escalation, [your keywords]
- Any email about money over [amount, e.g., INR 5 lakh / $10,000]
- Calendar conflicts (double-booked meetings)
- [Add your own triggers]

### IMPORTANT (include in daily briefing):
- Project updates from: [team member names]
- Meeting invites for this week
- Emails from: [important but not urgent contacts]
- [Add your own]

### IGNORE (never alert me):
- Newsletters and marketing emails
- Automated notifications (CI/CD, monitoring, etc.)
- [Add your own]

### MEETING PREP (alert 30 min before):
- Any meeting with: [key people who need prep]
- Meetings tagged: [tags like "client", "board", "investor"]
- If someone in a meeting also emailed me today, mention it
```

---

## Tips for Good Rules

- **Be specific.** "Emails from my boss" is vague. "Emails from Rajesh Sharma, CEO, especially about board, investor, or quarterly" is actionable.
- **Think about last week.** What caught you off guard? What rule would have flagged it early?
- **Think about your EA/PA.** If you had a human assistant, what would you train them on? Those ARE your rules.
- **Start strict, loosen later.** It's better to get too few alerts than too many. Silence is the feature.
