from conan import ConanFile


class ConanRecipe(ConanFile):
    settings = 'os', 'build_type', 'arch', 'compiler'
    generators = 'CMakeToolchain', 'CMakeDeps'

    def requirements(self):
        pass
