import pymssql

# Datos de conexión

server = '192.168.201.212'  # Por ejemplo: 'localhost' o 'mi_servidor'
database = 'DNCN_ComercioExt'
username = 'sa'
password = ''

try:
    # Establecer la conexión
    conn = pymssql.connect(server, username, password, database)
    print("Conexión exitosa.")

    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Ejecutar una consulta de ejemplo
    cursor.execute("""
		SELECT
			p.name AS ProcedimientoNombre
		FROM
			sys.procedures AS p
		INNER JOIN
			sys.sql_modules AS m
			ON p.object_id = m.object_id
		WHERE
			m.definition LIKE '%comextma_importacion3%'
	""")

    # Imprimir los resultados
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except pymssql.Error as e:
    print("Error en la conexión:", e)

finally:
    # Cerrar la conexión
    if conn:
        conn.close()
        print("Conexión cerrada.")