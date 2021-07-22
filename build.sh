#!/bin/bash -e

mkdir -p build

(
cd build
conan install -g cmake_find_package -g cmake_paths ..
conan build ..
conan package ..
conan export-pkg ..
)

