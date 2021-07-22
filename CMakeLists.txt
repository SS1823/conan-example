cmake_minimum_required(VERSION 3.14)
project(conan-test)

if(EXISTS ${CMAKE_BINARY_DIR}/conan_paths.cmake)
include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
endif()

option(LIB_SHARED "Build as a shared library" OFF)

if(LIB_SHARED)
    set(LIB_TYPE SHARED)
else()
    set(LIB_TYPE STATIC)
endif()

find_package(nlohmann_json REQUIRED)

add_library(
    sample
    ${LIB_TYPE}
    src.cpp
)
target_include_directories(
    sample
    PUBLIC
    include
)

install(
    TARGETS sample
)
install(
    DIRECTORY include
    TYPE INCLUDE
)
