# Requerimos una versión mínima de CMake, 3.10 es una buena elección
cmake_minimum_required(VERSION 3.10)

# El nombre de tu proyecto
project(CrisostomoCore)

# Habilita la compilación de bibliotecas compartidas
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Agrega los subdirectorios para que CMake los procese
add_subdirectory(Domain)
# add_subdirectory(Application)
# add_subdirectory(Infrastructure)
# add_subdirectory(Presentation)