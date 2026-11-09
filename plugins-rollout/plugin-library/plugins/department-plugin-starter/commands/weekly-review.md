---
description: Run the department's weekly review on the last seven days, or on the file or period you name.
argument-hint: "[file or period, optional]"
---

Run the weekly-review skill.

- Period: $ARGUMENTS if given, otherwise the last seven days.
- Source: `~~work queue` if connected, otherwise the newest export in the folder or project.
- Write `weekly-review.md`. If one already exists for an earlier week, add the week to the file name instead of overwriting it.
