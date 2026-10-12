# Hero bookings service

A practice repository for learning Claude Code. Mettle & Co is a fictional company that signs superheroes and sells their services to councils and businesses. All people, data and email addresses are invented.

The booking and dispatch API for Mettle & Co. Clients sign a contract on one of three plans, book heroes for missions, and get a monthly invoice.

Plans are priced per seat per month. A seat is one dedicated patrol post that a client reserves each month.

| Plan | Price per seat | Hero-hours included per seat each month |
|---|---|---|
| Pro | $9,000 | 160 |
| Max | $16,000 | 250 |
| Enterprise | $28,000 | 400 |

## Setup

You need Python 3.12.

With uv:

```
uv sync
uv run pytest
```

With pip:

```
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e . pytest httpx
pytest
```

## Run the API

```
uv run uvicorn --factory heroes_api.main:create_app --reload
```

The database is a SQLite file, `heroes.db` in the current folder. Set `HEROES_DB` to use another path. The 15 signed heroes are added on first start. Open http://127.0.0.1:8000/docs to try the endpoints.

## Endpoints

- `POST /clients` creates a client with a name, plan, seats and optional contact email
- `GET /clients` lists clients
- `POST /clients/{id}/tier` changes a client's plan
- `GET /heroes` lists the signed heroes and their powers
- `POST /bookings` books a hero for a mission, with a start and end time
- `GET /clients/{id}/bookings` lists a client's bookings
- `GET /clients/{id}/invoices/{YYYY-MM}` builds the invoice for one month

## Layout

- `heroes_api/main.py` has the FastAPI app and routes
- `heroes_api/db.py` has the schema and the hero roster
- `heroes_api/models.py` has the request models
- `heroes_api/plans.py` has plan prices and included hours
- `heroes_api/bookings.py` creates and lists bookings
- `heroes_api/invoices.py` builds monthly invoices
- `tests/` has the pytest suite

Open work is in `issues.md`.
