---
name: weekly-review
description: Writes the department's weekly review from the last seven days of work: what missed its target, what's still open, the main themes and what needs a decision. Use it whenever someone asks for the weekly review, a weekly summary of the team's work, what's overdue or what missed target, and when the scheduled weekly review runs.
---

# Weekly review

> Read [CONTEXT.md](../../CONTEXT.md) for the department's targets and rules, and [CONNECTORS.md](../../CONNECTORS.md) if you see a `~~` placeholder. If CONTEXT.md still has text in angle brackets, say which parts are missing and use only the parts that are filled in.

## 1. Get the work

- If `~~work queue` is connected, pull the last seven days, or the period you were asked for.
- Otherwise, use the newest export in the folder or project. Match columns by meaning, not only by name.
- Say which source you used and which dates it covers.

## 2. Check it against the targets

For each item, check it against the targets in CONTEXT.md. Compute counts and misses with code, not by hand.

## 3. Write the review

Write `weekly-review.md` with:

1. **Missed targets.** A table of every item that missed, the most serious first.
2. **Still open.** What's waiting, oldest or most urgent first.
3. **Themes.** Items grouped by type, with counts and one line on the biggest group.
4. **For the lead.** Three lines at most: what needs a decision this week.

Keep it to one page. Report by type, client or request, never by the person who handled it.
