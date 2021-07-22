cmake_minimum_required(VERSION 3.14)
project(conan-test)

# for easier package lookup from conan we use this generated file
# this can be omitted, but one must do it by hand
if(EXISTS ${CMAKE_BINARY_DIR}/conan_paths.cmake)
include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
endif()

# this is used in conan too, we can generate multiple packages
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

# install is tied with conan packaging, so it should be defined
install(
    TARGETS sample
)
install(
    DIRECTORY include
    TYPE INCLUDE
)

