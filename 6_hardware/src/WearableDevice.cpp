// WearableDevice.cpp
// ---------------------
// Reference implementation stub. Replace the body of each method with
// real calls into your platform's BLE stack (e.g. Windows.Devices.Bluetooth
// on Windows via WinRT/C++, or BlueZ D-Bus APIs on Linux).

#include "WearableDevice.hpp"
#include <stdexcept>
#include <iostream>

WearableDevice::WearableDevice(const std::string& mac_address)
    : mac_address_(mac_address) {}

bool WearableDevice::connect() {
    // TODO: open a real BLE GATT connection to mac_address_.
    std::cout << "[hardware] Connecting to device " << mac_address_ << "...\n";
    connected_ = true;
    return connected_;
}

void WearableDevice::disconnect() {
    // TODO: close the real BLE GATT connection.
    std::cout << "[hardware] Disconnecting from device " << mac_address_ << "\n";
    connected_ = false;
}

int WearableDevice::read_heart_rate() {
    if (!connected_) {
        throw std::runtime_error("Device not connected. Call connect() first.");
    }
    // TODO: read HEART_RATE_UUID characteristic from the real device.
    // Placeholder value until the real GATT read is wired in.
    return 72;
}

double WearableDevice::read_temperature() {
    if (!connected_) {
        throw std::runtime_error("Device not connected. Call connect() first.");
    }
    // TODO: read TEMPERATURE_UUID characteristic from the real device.
    // Placeholder value until the real GATT read is wired in.
    return 36.6;
}
