# Slack Thread: #product-launches (Jan 22)

**@priya** (10:15 AM)
Heads up - the notification system v2 is ready for staging. Can someone from platform team review the API changes before we push to prod?

**@rohit** (10:22 AM)
I'll take a look this afternoon. Any breaking changes?

**@priya** (10:24 AM)
One breaking change: the webhook payload format changed. Old format still works but deprecated. We should give enterprise customers 30 days notice before removing old format.

**@suresh** (10:31 AM)
Who's handling the customer communication about the deprecation? We can't just push this and hope for the best.

**@me** (10:45 AM)
I'll own the communication. Let me draft something. @priya can you list which enterprise customers are using the webhook? I need the full list.

**@priya** (11:02 AM)
Sent via DM. 14 customers on the webhook currently. Acme Corp is one of them.

**@me** (11:15 AM)
Of course Acme is on it. Let's be extra careful with their migration timeline given the renewal situation. I'll reach out to Anita directly.

**@rohit** (2:30 PM)
Reviewed. API changes look clean. One concern: the rate limit on the new webhook endpoint is set to 100/min. Some enterprise customers (Acme, TechCo, GlobalInc) will exceed that. Recommend bumping to 500/min or making it configurable.

**@me** (2:45 PM)
Good catch. @suresh can engineering make rate limits configurable per customer? That's been requested before.

**@suresh** (3:10 PM)
It's a 2-day task. I can squeeze it into next sprint if we deprioritize something. What's the priority call?

**@me** (3:15 PM)
Let me think about it and come back tomorrow with a priority recommendation.
