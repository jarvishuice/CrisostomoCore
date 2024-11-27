from App.Infrastructure.Providers.DB.PsqlProvider import PsqlProvider

# Obtener la instancia de la clase
conn_pool = PsqlProvider.get_instance()

# Obtener una conexión
conn = conn_pool.get_connection()

# Ejecutar una consulta para obtener todos los usuarios de una tabla
with conn.cursor() as cur:
    cur.execute("SELECT * FROM usuarios")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Devolver la conexión al pool
conn_pool.return_connection(conn)

# Realizar otra consulta (ejemplo)
conn = conn_pool.get_connection()
with conn.cursor() as cur:
    cur.execute("INSERT INTO usuarios (nombre, apellido) VALUES (%s, %s)", ('Juan', 'Pérez'))
    conn.commit()
conn_pool.return_connection(conn)

# Cerrar todas las conexiones (al finalizar la aplicación)
conn_pool.close_all_connections()