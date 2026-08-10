// main.cpp
// -----------
// Example entrypoint wiring a WearableDevice into an IngestionPoller.
// Replace the MAC address with your real device's, and on_reading with
// real forwarding logic (e.g. an HTTP POST to 2_backend/api/records).

#include <iostream>
#include "WearableDevice.hpp"
#include "IngestionPoller.hpp"

int main() {
    WearableDevice device("AA:BB:CC:DD:EE:FF");

    IngestionPoller poller(
        device,
        "device-001",
        [](const WearableReading& reading) {
            std::cout << "[hardware] HR=" << reading.heart_rate_bpm
                      << "bpm Temp=" << reading.temperature_c << "C\n";
        },
        5
    );

    poller.run(10);  // demo: 10 readings then stop
    return 0;
}
