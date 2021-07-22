from conans import ConanFile, CMake, tools

class SampleLib(ConanFile):
    name = "SampleLib"
    version = "1.0"
    license = "Public Domain"
    author = ""
    description = "Example project"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    no_copy_source = True

    requires = 'nlohmann_json/3.9.1'
    generators = 'cmake'

    def _config_cmake(self):
        cmake = CMake(self)
        if self.options.shared:
            cmake.definitions['LIB_SHARED'] = 'ON'
        else:
            cmake.definitions['LIB_SHARED'] = 'OFF'
        cmake.configure(source_dir=self.source_folder)
        return cmake
    
    def build(self):
        cmake = self._config_cmake()
        cmake.build()

    def package(self):
        cmake = self._config_cmake()
        cmake.install()

