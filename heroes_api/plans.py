from dataclasses import dataclass


@dataclass(frozen=True)
class Plan:
    name: str
    price_per_seat: int
    included_hours_per_seat: int


PLANS = {
    "Pro": Plan("Pro", 9_000, 160),
    "Max": Plan("Max", 16_000, 250),
    "Enterprise": Plan("Enterprise", 28_000, 400),
}


def get_plan(name: str) -> Plan:
    return PLANS[name]
