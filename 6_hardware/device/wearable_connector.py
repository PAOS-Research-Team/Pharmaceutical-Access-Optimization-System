"""
Wearable device connector
--------------------------
Handles the Bluetooth Low Energy (BLE) connection to a wearable
(heart rate, temperature, motion) and reads raw sensor values. Keeps
device I/O isolated from the rest of the app — swap this file if you
change device brand/protocol, nothing else needs to change.
"""

import asyncio
from bleak import BleakClient  # pip install bleak

# Standard BLE GATT characteristic UUIDs (adjust to match your device's spec sheet).
HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
TEMPERATURE_UUID = "00002a1c-0000-1000-8000-00805f9b34fb"


class WearableDevice:
    def __init__(self, mac_address: str):
        self.mac_address = mac_address
        self.client: BleakClient | None = None

    async def connect(self):
        self.client = BleakClient(self.mac_address)
        await self.client.connect()

    async def disconnect(self):
        if self.client:
            await self.client.disconnect()

    async def read_heart_rate(self) -> int:
        """Reads the current heart rate value (bpm) from the device."""
        raw = await self.client.read_gatt_char(HEART_RATE_UUID)
        # First byte is flags, second byte is the heart rate value (per BLE spec).
        return raw[1]

    async def read_temperature(self) -> float:
        """Reads the current body temperature (°C) from the device."""
        raw = await self.client.read_gatt_char(TEMPERATURE_UUID)
        return int.from_bytes(raw[1:5], byteorder="little") / 100.0
