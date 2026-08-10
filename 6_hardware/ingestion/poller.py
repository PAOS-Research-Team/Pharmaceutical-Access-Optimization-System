"""
Ingestion pipeline
---------------------
Polls a connected WearableDevice on an interval, wraps each reading
in the WearableReading model, and forwards valid readings on to the
backend service layer for storage. Invalid/out-of-range readings are
dropped and logged rather than silently stored.
"""

import asyncio
from datetime import datetime

from 6_hardware.device.wearable_connector import WearableDevice
from 6_hardware.device.models import WearableReading


async def poll_device(device: WearableDevice, device_id: str, interval_seconds: int = 5):
    """
    Continuously reads from `device` every `interval_seconds` and yields
    validated WearableReading objects. Caller decides what to do with
    each reading (e.g. pass to 2_backend/services to persist it).
    """
    await device.connect()
    try:
        while True:
            heart_rate = await device.read_heart_rate()
            temperature = await device.read_temperature()

            reading = WearableReading(
                device_id=device_id,
                heart_rate_bpm=heart_rate,
                temperature_c=temperature,
                recorded_at=datetime.utcnow(),
            )

            if reading.is_within_normal_range():
                yield reading
            else:
                print(f"[hardware] Discarded out-of-range reading: {reading}")

            await asyncio.sleep(interval_seconds)
    finally:
        await device.disconnect()
