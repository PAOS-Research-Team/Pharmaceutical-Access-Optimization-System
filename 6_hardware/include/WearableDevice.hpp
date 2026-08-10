// WearableDevice.hpp
// ---------------------
// Handles the Bluetooth Low Energy (BLE) connection to a wearable and
// exposes simple read_heart_rate() / read_temperature() calls. Device
// I/O is isolated here — swap the .cpp implementation if you change
// device brand/protocol, nothing else in the project needs to change.

#pragma once
#include <string>

// Standard BLE GATT characteristic UUIDs (adjust to match your
// device's spec sheet — these are the generic BLE standard ones).
constexpr const char* HEART_RATE_UUID  = "00002a37-0000-1000-8000-00805f9b34fb";
constexpr const char* TEMPERATURE_UUID = "00002a1c-0000-1000-8000-00805f9b34fb";

class WearableDevice {
public:
    explicit WearableDevice(const std::string& mac_address);

    bool connect();
    void disconnect();

    int read_heart_rate();       // bpm
    double read_temperature();   // degrees Celsius

private:
    std::string mac_address_;
    bool connected_ = false;

    // Opaque handle to the platform BLE stack (e.g. WinRT Bluetooth API
    // on Windows, BlueZ on Linux). Implementation lives in the .cpp file
    // so this header stays platform-independent.
    void* native_handle_ = nullptr;
};
