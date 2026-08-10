"""
Service layer (glue)
-----------------------
Connects the API layer to 1_core business logic and to the DB layer.
This is the ONLY layer allowed to talk to both 1_core and 2_backend/db,
which keeps the dependency direction clean: api -> services -> (core, db).
"""

from 1_core.domain.models import Record
from 2_backend.db.models import insert_record, fetch_record


async def create_record(data: dict) -> dict:
    """Validate via the domain model, then persist."""
    record = Record(id=data["id"], payload=data["payload"])
    if not record.is_valid():
        raise ValueError("Record payload cannot be empty")
    return await insert_record(record.id, record.payload)


async def get_record(record_id: str) -> dict | None:
    """Fetch a record by id, delegating straight to the DB layer."""
    return await fetch_record(record_id)
