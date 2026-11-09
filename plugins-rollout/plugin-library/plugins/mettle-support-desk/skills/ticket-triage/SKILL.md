---
name: ticket-triage
description: Triages Mettle & Co support tickets against the first-reply target for each client's plan. Works on one ticket or a whole week or month of tickets from the support platform or a CSV export. Use it whenever someone asks to triage tickets, check first-reply times, find missed targets, group tickets by theme, or prepare the weekly Support review, and when the scheduled weekly triage runs.
---

# Ticket triage

> Read [CONTEXT.md](../../CONTEXT.md) for the first-reply targets and house rules, and [CONNECTORS.md](../../CONNECTORS.md) if you see a `~~` placeholder.

## 1. Get the tickets

- If `~~support platform` is connected, pull the tickets for the period you were asked about. If no period was given, use the last seven days.
- Otherwise, use the ticket CSV you were given. It usually has: `id, date, customer, plan, category, priority, status, first_reply_hours, text`. Match columns by meaning if the names differ.
- Say which source you used and which dates it covers.

## 2. Check every ticket against its target

A ticket missed its target when `first_reply_hours` is greater than the target for its plan in CONTEXT.md. Compute this with code, not by hand.

## 3. Write the triage

Write `weekly-triage.md` (or the file name you were asked for) with these sections:

1. **Missed first-reply targets.** A table: ticket, date, customer, plan, hours to first reply, target, status. Enterprise first, then Max, then Pro. Below it, one line per open or pending miss on what to do next and who owns it.
2. **Still open.** Open and pending tickets, urgent and high first.
3. **Themes.** Tickets grouped by category, with the count and one line on what's driving the biggest group.
4. **Repeat clients.** Any client with more than one ticket in the period, or a second Enterprise miss this year if earlier files are available.
5. **For the team lead.** Three lines at most: what needs a decision this week.

## Rules

- Damage claims go to the damage claims manager. Conduct tickets go to the Director of Dispatch.
- Don't name an individual agent as the cause of a miss. Report by plan, category and client.
- Keep it to one page. Put the detail in tables and keep sentences for what matters.
- Check every count and total adds up before you finish.
