# CMake build for the 6_hardware C++ module.
# Build with:
#   cmake -S 6_hardware -B 6_hardware/build
#   cmake --build 6_hardware/build

cmake_minimum_required(VERSION 3.15)
project(hardware_module CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(include)

add_executable(hardware_module
    src/WearableDevice.cpp
    src/IngestionPoller.cpp
    src/main.cpp
)
