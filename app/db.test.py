import psycopg2

# Parámetros de conexión
host = "localhost"
port = "5432"
database = "postgres"
user = "postgres"

# La nueva contraseña que quieras poner
nueva_pass = "m4Nu6l1T0"

try:
    # Conexión usando trust temporal: no ponemos password
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=database,
        user=user
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Cambiar la contraseña
    cursor.execute(f"ALTER USER {user} WITH PASSWORD '{nueva_pass}';")
    print("Contraseña cambiada con éxito")
    conn.close()

except Exception as e:
    print("Error:", e)
