# Rollout plan: Support desk plugin

Built from `rollout-brief.md`.

## Who

| Role | Person | What they do |
|---|---|---|
| Sponsor | Luis Ferreira, VP Customer Support | Announces it, asks about it at the stand-up |
| Plugin owner | Chloe Dubois, Support Team Lead | Keeps the house rules current, collects feedback, asks for new versions |
| Champions | Two daily Claude users on Ravi Chandran's shift (to name) | Help their shift in the first two weeks. With 90 seats, two champions is about one per 45 people |
| Claude Owner | Owner in Engineering | Publishes the plugin, sets it for the Customer Support group, adds the Zendesk connector |

## How it's provisioned

- Customer Support group: **Installed by default**, so nobody installs anything and anyone can switch it off.
- Everyone else: **Not available** until another team asks.
- Not **Required**: the team needs room to say what doesn't work.

## Launch message (from Luis, in the Support Slack channels)

> From Monday, everyone in Customer Support has the Support desk plugin in Claude, with nothing to install. Three things it does: the weekly triage (ready before the 9:30 stand-up), drafting a reply with the right prices and targets, and turning a client call into a follow-up email. Chloe owns it: if an answer is wrong, tell her and she'll fix it for everyone, and your shift's champion can show you in ten minutes. Client names and call notes stay inside Customer Support, so don't paste them into other teams' chats. I'll read the triage every Monday before the stand-up, so I'll be using it with you.

## First week

| Day | What happens | Owner |
|---|---|---|
| Before launch | Zendesk connector added, and each lead connects it. Weekly triage scheduled for Mondays at 8:00 from the CSV export | Claude Owner, Chloe |
| Monday | Stand-up opens with the triage | Ravi and Chloe |
| Tuesday to Thursday | Champions sit with each shift for 15 minutes: one real reply drafted with the plugin | Champions |
| Friday | Chloe collects what was wrong or missing | Chloe |

## What to measure

- Weekly triage run every Monday, and time to prepare the stand-up: from about 2 hours per lead to a few minutes. This is the before-and-after measure.
- Enterprise misses noticed within a week.
- Weekly active users in Customer Support, against its 90 seats.

## Keeping it current

- Monthly: Chloe updates the house rules if a price, target or rule changes, and raises the version.
- Quarterly curation review (first one three months after launch): what's used, what's stale, what to add. The monthly report for Luis is the first candidate.
