// <summary>
// Main application entry point
// </summary>
#include"Domain/Kernel/ConfigValues.hpp"
#include"Infrastructure/Providers/Logs.hpp"
#include "Infrastructure/Providers/StaticConnPsql.hpp"

int main() {
    // Inicializar la configuración
    Domain::Kernel::ConfigValues::start();
    Logger::instance().init(Domain::Kernel::ConfigValues::LOG_PATH, LogLevel::DEBUG, true);
    std::cout << "DB Host: " << Domain::Kernel::ConfigValues::DB_HOST << "\n";
    std::cout << "DB Port: " << Domain::Kernel::ConfigValues::DB_PORT << "\n";
    std::cout << "DB User: " << Domain::Kernel::ConfigValues::DB_USER << "\n";
    std::cout << "DB Password: " << Domain::Kernel::ConfigValues::DB_PASSWORD << "\n";
    std::cout << "DB Name: " << Domain::Kernel::ConfigValues::DB_NAME << "\n";
    Logger::instance().info("Configuración cargada correctamente");
    StaticConnPoolPsql::initialize(
        "host="+Domain::Kernel::ConfigValues::DB_HOST + " port=" + Domain::Kernel::ConfigValues::DB_PORT +
        " user=" + Domain::Kernel::ConfigValues::DB_USER +
        " password=" + Domain::Kernel::ConfigValues::DB_PASSWORD +
        " dbname=" + Domain::Kernel::ConfigValues::DB_NAME,
        10 // Tamaño del pool de conexiones
    );
    
    auto& log = Logger::instance();
    // Acceder a los valores de configuración
    log.info("Aplicación iniciada");
    log.debug("Nivel de log DEBUG activado");
    log.warn("Este es un mensaje de advertencia");
    log.error("Este es un mensaje de error");
    std::cout << "DB Host: " << Domain::Kernel::ConfigValues::DB_HOST << "\n";
    std::cout << "DB Port: " << Domain::Kernel::ConfigValues::DB_PORT << "\n";
    std::cout << "DB User: " << Domain::Kernel::ConfigValues::DB_USER << "\n";
    std::cout << "DB Password: " << Domain::Kernel::ConfigValues::DB_PASSWORD << "\n";
    std::cout << "DB Name: " << Domain::Kernel::ConfigValues::DB_NAME << "\n";
    std::cout << "Log Path: " << Domain::Kernel::ConfigValues::LOG_PATH << "\n";
    std::cout << "Log Level: " << Domain::Kernel::ConfigValues::LOG_LEVEL << "\n";
    std::cout << "Server Port: " << Domain::Kernel::ConfigValues::SERVER_PORT << "\n";

    return 0;
}