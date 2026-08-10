"""
Domain models & business rules
-------------------------------
Pure, framework-agnostic business logic. Nothing in this file should
import from 2_backend (no FastAPI, no DB drivers, no HTTP). This keeps
the core logic testable in isolation and reusable across services.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Record:
    """A single unit of domain data flowing through the platform."""
    id: str
    payload: dict
    created_at: datetime = datetime.utcnow()

    def is_valid(self) -> bool:
        # Business rule: a record must have a non-empty payload to be usable.
        return bool(self.payload)


def deduplicate_records(records: list[Record]) -> list[Record]:
    """Business rule: keep only the first occurrence of each record id."""
    seen_ids = set()
    unique_records = []
    for record in records:
        if record.id not in seen_ids:
            seen_ids.add(record.id)
            unique_records.append(record)
    return unique_records
