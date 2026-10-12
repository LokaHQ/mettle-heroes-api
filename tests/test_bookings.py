def book(client, client_id, hero="Brisk", start="2026-09-14T09:00", end="2026-09-14T12:00"):
    return client.post(
        "/bookings",
        json={"client_id": client_id, "hero": hero, "start": start, "end": end, "mission": "Market patrol"},
    )


def test_list_heroes_returns_the_signed_roster(client):
    response = client.get("/heroes")

    assert response.status_code == 200
    names = [h["name"] for h in response.json()]
    assert len(names) == 15
    assert "Findwell" in names
    assert "Lady Lanyard" in names


def test_book_hero_for_a_mission(client, harbour_council):
    response = book(client, harbour_council["id"])

    assert response.status_code == 201
    body = response.json()
    assert body["hero"] == "Brisk"
    assert body["hours"] == 3


def test_booking_an_unknown_hero_returns_404(client, harbour_council):
    response = book(client, harbour_council["id"], hero="Nobody In Particular")

    assert response.status_code == 404


def test_booking_for_an_unknown_client_returns_404(client):
    response = book(client, 999)

    assert response.status_code == 404


def test_booking_must_end_after_it_starts(client, harbour_council):
    response = book(client, harbour_council["id"], start="2026-09-14T12:00", end="2026-09-14T09:00")

    assert response.status_code == 422


def test_list_bookings_for_a_client(client, harbour_council):
    book(client, harbour_council["id"], hero="Quorum")
    book(client, harbour_council["id"], hero="Pivot")

    response = client.get(f"/clients/{harbour_council['id']}/bookings")

    assert response.status_code == 200
    assert [b["hero"] for b in response.json()] == ["Quorum", "Pivot"]
