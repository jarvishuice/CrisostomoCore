# Crea la biblioteca compartida 'domain' a partir de los archivos de la capa
add_library(domain SHARED 
    Entities/EntityBase.hpp
    Entities/UserEntity.hpp
    # Agrega otros archivos de la capa de dominio aquí
)

# Asegura que otros módulos puedan encontrar los archivos de encabezado
target_include_directories(domain PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/Enitities)

# Añade una propiedad para que los otros CMakeLists.txt la puedan encontrar
set_target_properties(domain PROPERTIES PUBLIC_HEADER
    Enitities/EntityBase.hpp
)
