# Open issues

## HB-101 Block bookings for a hero who is already on a mission

Type: feature. Reporter: Rosa Delgado. Opened 2026-08-04.

Dispatch double-booked Merge Lane on 28 July, once for the Eastgate bridge reopening and once for a supermarket car park. He can only clear one traffic jam at a time. The API accepts any booking as long as the hero and client exist.

Acceptance criteria:

- `POST /bookings` returns 409 when the hero has another booking that overlaps the requested time
- A booking that starts exactly when another ends is allowed
- The error message names the clashing mission
- Tests cover the overlap, the back-to-back case and a different hero at the same time

## HB-102 July invoice includes a mission that starts on 1 August

Type: bug. Reporter: Owen Pritchard. Opened 2026-08-06.

Wrenfield Town Council's July invoice listed Lowtide's fete field mission, which ran on 1 August. The same mission will show again on the August invoice, so the client sees its hours twice.

Steps to reproduce:

1. Create a client: `POST /clients` with `{"name": "Wrenfield Town Council", "plan": "Enterprise", "seats": 22}`
2. Book a mission on the first day of the next month: `POST /bookings` with `{"client_id": 1, "hero": "Lowtide", "mission": "Drain the fete field", "start": "2026-08-01T09:00", "end": "2026-08-01T11:00"}`
3. Get the July invoice: `GET /clients/1/invoices/2026-07`

Expected: `missions` is empty and `hero_hours` is 0.

Actual: `missions` lists the 1 August booking and `hero_hours` is 2.

## HB-103 Keep plan prices in one place

Type: refactor. Reporter: Mei-Lin Zhou. Opened 2026-07-21.

Seat prices are defined in `heroes_api/plans.py` and again in `SEAT_PRICES` in `heroes_api/invoices.py`. When the Enterprise price went up, only one of them was changed at first. The comment next to `plan_price` still gives the old Enterprise figures.

Acceptance criteria:

- `invoices.py` reads prices from `plans.py`
- `SEAT_PRICES` and `plan_price` are removed or become thin wrappers over `get_plan`
- No change to any API response
- Existing tests pass without edits, apart from imports

## HB-104 Invoice endpoint returns 500 for a bad month

Type: bug. Reporter: Lukas Brandt. Opened 2026-09-02.

`GET /clients/1/invoices/2026-13` and `GET /clients/1/invoices/september` both crash with a 500 and a stack trace in the logs.

Expected: a 422 with a message saying the month must be `YYYY-MM`.

## HB-105 Clients can be created with zero or negative seats

Type: bug. Reporter: Owen Pritchard. Opened 2026-09-09.

`POST /clients` accepts `"seats": -2` and returns 201. The invoice then shows a negative total. A client needs at least one seat.

Acceptance criteria:

- `POST /clients` returns 422 when seats is below 1
- A test covers it

## HB-106 Bill mid-month tier changes pro rata

Type: feature. Reporter: Owen Pritchard. Assignee: Aisha Bello. Opened 2026-08-18.

When a client moves from Max to Enterprise on the 15th, the invoice charges Enterprise for the whole month. Finance refunds the difference by hand. `prorate_tier_change` in `invoices.py` was written for this but nothing calls it, and it has no tests.

Acceptance criteria:

- The service records the date of each tier change
- The invoice for that month bills old-plan days at the old price and the rest at the new price
- Tests for `prorate_tier_change`, including a change on the 1st and on the last day of the month

## HB-107 Warn clients before they use up their included hero-hours

Type: feature. Reporter: Luis Ferreira. Opened 2026-11-25.

Support had several tickets from Pro clients surprised that they had used all their included hours. The invoice shows `hero_hours` and `included_hours`, but nothing warns the client before they run out.

Acceptance criteria:

- `POST /bookings` returns a `warning` field when the booking takes the client past 80% of their included hours for that month
- The booking still succeeds
- Tests cover under, at and over the threshold

## HB-108 Show which heroes are free in a time window

Type: feature. Reporter: Rosa Delgado. Assignee: Yuki Tanaka. Opened 2026-09-22.

Dispatch checks each hero's bookings one by one before calling a client back. They need a single view.

Acceptance criteria:

- `GET /heroes/available?start=...&end=...` lists heroes with no booking that overlaps the window
- Depends on the overlap check from HB-101, so both should share one function
