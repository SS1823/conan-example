mkdir build


cd build
# generate cmake_paths so we can use automatic setting of CMAKE_PREFIX_PATH & CMAKE_MODULE_PATH, so cmake can find modules easily
# generate cmake_find_package so Findxxx modules are there
conan install -g cmake_find_package -g cmake_paths ..

# build sources
conan build ..

# build package
conan package ..

# export package to local cache
conan export-pkg ..
