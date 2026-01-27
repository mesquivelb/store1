import psycopg2

# Parámetros de conexión al servidor
host = "localhost"
port = "5432"
user = "postgres"
password = "m4Nu6l1T0"  # pon la contraseña actual de postgres
database = "postgres"        # usamos la base por defecto para conectarnos

try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=database,
        user=user,
        password=password
    )
    cursor = conn.cursor()
    
    # Listar todas las bases
    cursor.execute("SELECT datname FROM pg_database;")
    bases = cursor.fetchall()
    
    print("Bases de datos en el servidor:")
    for b in bases:
        print("-", b[0])
    
    conn.close()
except Exception as e:
    print("Error:", e)
