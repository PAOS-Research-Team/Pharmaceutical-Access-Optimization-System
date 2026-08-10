// IngestionPoller.cpp
#include "IngestionPoller.hpp"
#include <thread>
#include <chrono>
#include <iostream>

IngestionPoller::IngestionPoller(WearableDevice& device,
                                  std::string device_id,
                                  std::function<void(const WearableReading&)> on_reading,
                                  int interval_seconds)
    : device_(device),
      device_id_(std::move(device_id)),
      on_reading_(std::move(on_reading)),
      interval_seconds_(interval_seconds) {}

void IngestionPoller::run(int iterations) {
    device_.connect();

    for (int i = 0; iterations < 0 || i < iterations; ++i) {
        WearableReading reading{
            device_id_,
            device_.read_heart_rate(),
            device_.read_temperature(),
            std::chrono::system_clock::now()
        };

        if (reading.is_within_normal_range()) {
            on_reading_(reading);
        } else {
            std::cout << "[hardware] Discarded out-of-range reading\n";
        }

        std::this_thread::sleep_for(std::chrono::seconds(interval_seconds_));
    }

    device_.disconnect();
}
