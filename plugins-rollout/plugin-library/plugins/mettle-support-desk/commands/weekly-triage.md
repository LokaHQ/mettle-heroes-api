---
description: Run the weekly Support triage on the last seven days of tickets, or on the ticket file or period you name.
argument-hint: "[ticket file or period, optional]"
---

Run the ticket-triage skill for this week's Support review.

- Period: $ARGUMENTS if given, otherwise the last seven days.
- Source: `~~support platform` if connected, otherwise the newest ticket CSV in the folder or project.
- Write `weekly-triage.md`. If one already exists for an earlier week, add the week to the file name instead of overwriting it.
- End with the three lines "For the team lead".
