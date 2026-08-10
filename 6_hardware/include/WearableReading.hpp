// WearableReading.hpp
// ---------------------
// Plain data struct for a single wearable sensor reading. Shared by
// the device connector and the ingestion poller so the reading shape
// stays consistent everywhere it travels.

#pragma once
#include <string>
#include <chrono>

struct WearableReading {
    std::string device_id;
    int heart_rate_bpm;
    double temperature_c;
    std::chrono::system_clock::time_point recorded_at;

    // Basic sanity check, NOT a medical judgment — just flags obviously
    // bad sensor data before it gets forwarded to the backend.
    bool is_within_normal_range() const {
        return heart_rate_bpm >= 30 && heart_rate_bpm <= 220
            && temperature_c >= 30.0 && temperature_c <= 42.0;
    }
};
