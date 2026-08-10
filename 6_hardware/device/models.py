"""
Device data models
--------------------
Typed structure for one wearable reading, used everywhere the reading
travels (ingestion, API, DB) so the shape stays consistent.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class WearableReading:
    device_id: str
    heart_rate_bpm: int
    temperature_c: float
    recorded_at: datetime

    def is_within_normal_range(self) -> bool:
        # Basic sanity check, NOT a medical judgment — just flags obviously
        # bad sensor data before it reaches the database.
        return 30 <= self.heart_rate_bpm <= 220 and 30.0 <= self.temperature_c <= 42.0
