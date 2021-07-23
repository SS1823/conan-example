# Conan package sample
This is a sample package for conan

Remember that the scripts build.sh and build bat will select default configuration.
On windows this will be the newest Visual Studio installed.

# Conan installation

## Windows
This example uses powershell

create virtual environment
`py -m venv path_to_virtualenv`

activate
`path_to_virtualenv\Scripts\Activate.ps1`
conan should now be available as a sommand

alternatively, without isntallation, use full path `path_to_virtualenv\Scripts\conan.exe`

# Linux

create virtual environment
`py -m venv path_to_virtualenv`

activate (mind the dot at the beginning)
`. path_to_virtualenv\Scripts\activate.sh`
conan should now be available as a sommand

alternatively, without isntallation, use full path `path_to_virtualenv\bin\conan`
