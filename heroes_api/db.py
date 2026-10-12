import sqlite3

HEROES = [
    ("Brisk", "Runs faster than a tram. Files expense reports weeks late"),
    ("Findwell", "Finds any lost file, key or umbrella within the hour"),
    ("Quorum", "Can make any meeting reach a decision"),
    ("Lady Lanyard", "Opens any badge-controlled door"),
    ("The Untangler", "Untangles any cable, queue or rota"),
    ("Mute Button", "Silences all noise within ten metres"),
    ("Forecaster", "Knows the weather twenty minutes ahead"),
    ("Merge Lane", "Clears a traffic jam in under five minutes"),
    ("Inbox Zero", "Reads and sorts ten thousand emails a minute"),
    ("Pivot", "Spots the error in any spreadsheet at a glance"),
    ("Ballast", "Cannot be moved while seated. Holds doors in a gale"),
    ("Lowtide", "Moves puddles, ponds and the odd fountain"),
    ("Thermostat", "Sets any room to the right temperature. Nobody agrees what that is"),
    ("Late Shift", "Never needs sleep, but only works from 11pm to 7am"),
    ("Paperweight", "Can make anything too heavy to blow away"),
]

SCHEMA = """
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    plan TEXT NOT NULL,
    seats INTEGER NOT NULL,
    contact_email TEXT
);
CREATE TABLE IF NOT EXISTS heroes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    power TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(id),
    hero_id INTEGER NOT NULL REFERENCES heroes(id),
    mission TEXT NOT NULL,
    start TEXT NOT NULL,
    end TEXT NOT NULL
);
"""


def connect(path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.executemany("INSERT OR IGNORE INTO heroes (name, power) VALUES (?, ?)", HEROES)
    conn.commit()
