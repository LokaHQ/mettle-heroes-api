# Plugin plan: Customer Support

Built from `support-team-brief.md`, `faq.md` and `profile.md`.

## What goes in the plugin

| Workflow | How often | Time today | Becomes | Why |
|---|---|---|---|---|
| Weekly ticket review | Every Monday | About 2 hours per lead | A **command** (`/weekly-triage`) backed by a **skill** (ticket-triage) | Same steps every week, run on purpose at a set time. Can be scheduled |
| Replying to tickets | Every day | 10 to 15 minutes a reply | A **skill** (reply-drafting) | Claude should use it whenever someone asks for a reply, without anyone typing a command |
| Follow-up after a client call | 2 or 3 a week | About 45 minutes each | A **skill** (call-follow-up) | Same four outputs every time: summary, commitments, email, ticket update |

Shared by all three: a house rules file (first-reply targets, rules, tone, the FAQ answers that are out of date) and the connectors for the help desk, chat and knowledge base.

## Connectors it needs

| Category | Tool | Needed by |
|---|---|---|
| Support platform | Zendesk | Weekly triage, reply drafting |
| Knowledge base | Notion (the FAQ) | Reply drafting |
| Chat | Slack | Call follow-up (posting commitments) |

## Left out, and why

- Damage claim intake: it's a form-filling job with photos. Revisit once the help desk connector works.
- Monthly report for Luis: built from the weekly reviews. Add it in the next version, once the weekly triage is in use.
- Rewriting the FAQ, choosing a ticketing tool, training new starters: one-off work. A plugin is for work that repeats.

## Owner

To name before rollout. The plugin needs one person who keeps the house rules current.
