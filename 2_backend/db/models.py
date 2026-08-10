"""
DB models & queries
---------------------
Raw data-access functions. Each function maps directly to a table/
query and returns plain dicts/dataclasses, no ORM magic hidden here,
so it stays easy to reason about and swap.
"""

from 2_backend.db.connection import get_pool


async def insert_record(record_id: str, payload: dict) -> dict:
    """Insert a new record row. Replace body with a real SQL/ORM call."""
    get_pool()  # Ensures the pool is initialized before use.
    return {"id": record_id, "payload": payload}


async def fetch_record(record_id: str) -> dict | None:
    """Fetch a record row by id. Replace body with a real SQL/ORM call."""
    get_pool()
    return None  # Placeholder: no persistence wired up yet.
