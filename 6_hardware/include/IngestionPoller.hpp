// IngestionPoller.hpp
// ----------------------
// Polls a connected WearableDevice on an interval, builds a validated
// WearableReading each cycle, and forwards it via a callback. Keeps
// the polling loop decoupled from whatever consumes the readings
// (e.g. sending them to the backend API, or logging them locally).

#pragma once
#include <functional>
#include "WearableDevice.hpp"
#include "WearableReading.hpp"

class IngestionPoller {
public:
    // on_reading is called once per valid reading; invalid/out-of-range
    // readings are discarded and logged instead of forwarded.
    IngestionPoller(WearableDevice& device,
                     std::string device_id,
                     std::function<void(const WearableReading&)> on_reading,
                     int interval_seconds = 5);

    // Blocking loop — call from a background thread in real usage.
    void run(int iterations = -1);  // -1 = run forever

private:
    WearableDevice& device_;
    std::string device_id_;
    std::function<void(const WearableReading&)> on_reading_;
    int interval_seconds_;
};
