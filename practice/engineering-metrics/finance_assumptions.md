# Mettle & Co: finance assumptions for the engineering review

Everything here is invented for the exercise.

These are the numbers the finance partner and the engineering sponsor agreed before Claude Code was switched on. The monthly review uses them as they are. If a number changes, change it here and say so in the review.

| Item | Agreed value | Agreed by |
|---|---|---|
| Loaded hourly rate for an engineer | $85 | Marguerite Holt, Finance Director |
| How saved time is booked | Capacity created, not cost avoided | Marguerite Holt |
| Hours saved per Claude-assisted pull request | 0.6 hours | From a timed sample, below |
| One-off rollout cost | 120 hours at the loaded rate, which is $10,200 | Admin setup 30 hours, champions 40, training and preparation 50 |
| Budget owner | Marguerite Holt | |
| Who approves an overage | Marguerite Holt, reachable within one business day. Backup: Callum Reid | |
| Weekly spend read | Callum Reid | |

## The timed sample

Before the rollout, five small pull requests were timed by hand from first commit to ready for review. They averaged 3.4 hours. In the first month of use, five Claude-assisted pull requests of similar size were timed the same way and averaged 2.8 hours. The difference is 0.6 hours per assisted pull request. Five is a small sample, so the figure is a starting point, and the review says so.

## Metrics set at kickoff

Deployed pull requests per engineer per week, median lead time for changes, median review wait, change failure rate and median failed-deployment recovery time. The baseline is the 13 weeks before the first week of Claude Code usage, taken from the pull-request and incident history in this folder.

## Spend limits in force

See `spend_limits.csv`. An empty limit means no limit is set. An individual limit overrides the group limit, and the org ceiling is the hard cap above everything.
