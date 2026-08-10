"""
DB seed script
-----------------
Populates a fresh database with sample records for local development.
Run with: python 4_ops/scripts/seed_db.py
"""

import asyncio

from 2_backend.db.connection import init_db, close_db
from 2_backend.db.models import insert_record


async def main():
    await init_db()
    sample_records = [
        {"id": "seed-1", "payload": {"note": "first seeded record"}},
        {"id": "seed-2", "payload": {"note": "second seeded record"}},
    ]
    for record in sample_records:
        await insert_record(record["id"], record["payload"])
        print(f"Seeded record: {record['id']}")
    await close_db()


if __name__ == "__main__":
    asyncio.run(main())
